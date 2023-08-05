import spacy
from allennlp.predictors.predictor import Predictor
import neuralcoref
from typing import List
from spacy.tokens import Doc, Span
import pandas as pd
import os
import openai
import re
import subprocess
import importlib

class SpanBERTResolver:
    """
    Add desc here
    """
    def __init__(self, model_url: str = 'default_model_url'):
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            print("Model not found. Downloading 'en-small' model...")
            subprocess.check_call(['pip', 'install', "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz"])
            spacy_module = importlib.import_module('en_core_web_sm')
            self.nlp = spacy_module.load()
            #self.nlp = spacy.load('en_core_web_sm')
        neuralcoref.add_to_pipe(self.nlp)
        if model_url == 'default_model_url':
            model_url = 'https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz'
        self.predictor = Predictor.from_path(model_url)

    def core_logic_part(self, document: Doc, coref: List[int], resolved: List[str], mention_span: Span):
        final_token = document[coref[1]]
        if final_token.tag_ in ["PRP$", "POS"]:
            resolved[coref[0]] = mention_span.text + "'s" + final_token.whitespace_
        else:
            resolved[coref[0]] = mention_span.text + final_token.whitespace_
        for i in range(coref[0] + 1, coref[1] + 1):
            resolved[i] = ""
        return resolved

    def original_replace_corefs(self, document: Doc, clusters: List[List[List[int]]]) -> str:
        resolved = list(tok.text_with_ws for tok in document)

        for cluster in clusters:
            mention_start, mention_end = cluster[0][0], cluster[0][1] + 1
            mention_span = document[mention_start:mention_end]

            for coref in cluster[1:]:
                self.core_logic_part(document, coref, resolved, mention_span)

        return "".join(resolved)

    def get_span_noun_indices(self, doc: Doc, cluster: List[List[int]]) -> List[int]:
        spans = [doc[span[0]:span[1]+1] for span in cluster]
        spans_pos = [[token.pos_ for token in span] for span in spans]
        span_noun_indices = [i for i, span_pos in enumerate(spans_pos)
            if any(pos in span_pos for pos in ['NOUN', 'PROPN'])]
        return span_noun_indices

    def get_cluster_head(self, doc: Doc, cluster: List[List[int]], noun_indices: List[int]):
        head_idx = noun_indices[0]
        head_start, head_end = cluster[head_idx]
        head_span = doc[head_start:head_end+1]
        return head_span, [head_start, head_end]

    def is_containing_other_spans(self, span: List[int], all_spans: List[List[int]]):
        return any([s[0] >= span[0] and s[1] <= span[1] and s != span for s in all_spans])

    def improved_replace_corefs(self, document, clusters):
        resolved = list(tok.text_with_ws for tok in document)
        all_spans = [span for cluster in clusters for span in cluster]  # flattened list of all spans

        for cluster in clusters:
            noun_indices = self.get_span_noun_indices(document, cluster)

            if noun_indices:
                mention_span, mention = self.get_cluster_head(document, cluster, noun_indices)

                for coref in cluster:
                    if coref != mention and not self.is_containing_other_spans(coref, all_spans):
                        self.core_logic_part(document, coref, resolved, mention_span)

        return "".join(resolved)

    def resolve_coref(self, query: str) -> str:
        try:
            clusters = self.predictor.predict(query)['clusters']
        except AssertionError as e:
            return ""
        doc = self.nlp(query)
        return self.improved_replace_corefs(doc,clusters)
    

# query_to_resolve = "When is the next service appointment, vehicle check or oil change? With Teleservices, your BMW knows exactly when the next inspection is due. When maintenance work is required or if there is a malfunction, it sends all relevant data to you and your preferred service partner. Even before your BMW Service Partner calls you to make an appointment, he or she already knows the condition of your vehicle, can order spare parts and is perfectly prepared to meet the individual requirements of your vehicle. This also shortens the wait time during the appointment."
# allennlp =  SpanBERTResolver()
# print("SPANBERT:",allennlp.resolve_coref(query_to_resolve))





### Check how they pass on the prompts in BMW repo ###

few_shot_prompt = """ Perform co-reference resolution on the current query based on the context \n\n 

    ###
    Context: Can I use Alexa in my car? With Alexa Integration in your vehicle, you can benefit from effortless access to Amazon's voice service behind the wheel of your BMW, just as you've come to expect from your Alexa-enabled devices at home. \n 
    Current query:  How can I integrate it?
    Resolved answer: How can I integrate Alexa?


    Context: What makes the iX an innovative car? The BMW iX is the BMW Group’s first model to feature driver assistance systems from a new technology toolkit. The new technology toolkit gives the vehicle outstanding intelligence when it comes to monitoring its surroundings and transferring and processing data. Tell me more about this technology toolkit. 
    current query: Tell me more about this technology toolkit
    Resolved answer: Tell me more about BMW iX technology toolkit
    ###\n
    """


class GPTResolver:
    """
    Add desc here
    """
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def resolve_coref(self, query_to_resolve:str, few_shot_prompt:str = None, engine:str="text-davinci-003") -> str :
        if not few_shot_prompt:
            few_shot_prompt = """
            
{ "input": "Resolve the coreferences in the following sentence and do not paraphrase: {John and Jane went to the park. They had a picnic and played frisbee. When they were done, they walked home together.}", "output": "Resolved_query: {John and Jane went to the park. John and Jane had a picnic and played frisbee. When John and Jane were done, John and Jane walked home together.}" }
{ "input": "Resolve the coreferences in the following sentence and do not paraphrase: {My car needs an oil change. When can I have the next appointment for it? }", "output": "Resolved_query: {My car needs an oil change. When can I have the next appointment for an oil change?}" }

"""
        formatted_input_query = f'{{"input": "Resolve the coreferences in the following sentence and do not paraphrase: {query_to_resolve}"}}'
        gpt_prompt = few_shot_prompt + formatted_input_query
        response = openai.Completion.create(
            engine=engine,
            prompt=gpt_prompt,
            temperature=0.5,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        response = response['choices'][0]['text']
        try:
            clean_response = response[response.index("Resolved_query: ") + len("Resolved_query: "):]  ### accepts all the string after "Resolved_query:"" in the output
            clean_response = re.sub(r'(\w)[^\w]*$', r'\1', clean_response) ### cleans all the entailing special character after an english word
        except ValueError:
            raise ValueError("The generated output is in a format that is not supported by the system.")
        return clean_response
    

# query_to_resolve = "The chef prepared a delicious meal. It included steak, mashed potatoes, and green beans."
# query_to_resolve = "Wouldn't it be incredible if your BMW was also your personal assistant? Imagine if it could understand you, help you and think with you. That is exactly what the BMW Intelligent Personal Assistant does. Activate it with the voice command 'Hey, BMW' and it will be there for you, ready to help with any needs or questions about your vehicle. You can personalise it and give it a new name ('Hey, BMW. Change the activation word.'). \n\nYour personal assistant is a vehicle expert with whom you can operate numerous vehicle functions using natural voice commands. It also helps you to get to know and use your BMW better. It can explain features ('Hey BMW. How does the High-beam Assistant work?') and understands your vehicle's status ('Hey, BMW. Is my tyre pressure okay?'). \n\n\nSimply say: 'Hey, BMW. I'm hungry,' and your Personal Assistant immediately plans the route and finds the best-rated restaurants on request. Through regular updates, the BMW Intelligent Personal Assistant will be able to handle a growing number of commands and functions."

# GPT = GPTResolver()
# print("GPT3:",GPT.resolve_coref(query_to_resolve))