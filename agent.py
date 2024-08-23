from openai import OpenAI
import json
import argparse
import time
import re
import random 
import numpy as np 
import os
from openai import AzureOpenAI
from vertexai.preview.generative_models import GenerativeModel


class Agent():
    def __init__(self, initial_prompt_cls, round_prompt_cls, agent_name, temperature, model, rounds_num=24, agents_num=6, azure=False, hf_models={}):
        self.model = model

        self.agent_name = agent_name        
        self.temperature = temperature
        self.initial_prompt_cls = initial_prompt_cls 
        self.rounds_num = rounds_num 
        self.agents_num = agents_num

        self.initial_prompt = initial_prompt_cls.return_initial_prompt()
        self.messages = [{"role": "user", "content": self.initial_prompt}]

        
        self.round_prompt_cls = round_prompt_cls 
        if 'gemini' in self.model:
            self.model_instance = GenerativeModel(model)
        self.azure = azure 
        if azure:
            self.client = AzureOpenAI(
            azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
            api_version="2023-05-15"
            )
        elif 'gpt' in model:
            self.client = OpenAI()
        self.hf_model = True if 'hf' in model else False
        if 'hf' in model:
            self.hf_model, self.hf_tokenizer, self.hf_pipeline_gen = hf_models[model]

    def execute_round(self, answer_history, round_idx):
        '''
        construct the prompt and call model
        '''        
        slot_prompt = self.round_prompt_cls.build_slot_prompt(answer_history,round_idx) 
        agent_response = self.prompt("user", slot_prompt)    
        return slot_prompt, agent_response

        
    def prompt(self,role, msg):
        '''
        call each model 
        '''
        if 'gpt' in self.model and not self.azure:        
            messages = self.messages + [ {"role": role, "content": msg} ]
            response = self.client.chat.completions.create(model=self.model, messages=messages,temperature=self.temperature)
            content = response.choices[0].message
            return content 
        
        elif 'gpt' in self.model and self.azure:
            messages = self.messages + [ {"role": role, "content": msg} ]
            response = self.client.chat.completions.create(
            model=self.model, 
            messages=messages,
            temperature=self.temperature 
            )
            return response.choices[0].message.content
        
        elif 'gemini' in self.model: 
            responses = self.model_instance.generate_content(
            self.initial_prompt + msg,
            generation_config={
            "temperature": self.temperature,
            "top_p": 1
            },
            stream = True 
            )
            content = ''
            for response in responses:
                content += response.text
            return content
        
        elif self.hf_model:
            chat = [{"role": "user", "content": self.initial_prompt+msg}]
            model_input = self.hf_tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True, return_tensors="pt")
            output_text = self.hf_pipeline_gen(model_input, do_sample=True, temperature = self.temperature)[0]['generated_text']
            return output_text