import json
import argparse
import time
import re
import random 
import numpy as np 
import os
import openai 
import vertexai 
import shutil
from agent import Agent 
from initial_prompts import InitialPrompt
from rounds import RoundPrompts 


from utils import load_setup, set_constants, randomize_agents_order, setup_hf_model
from save_utils import create_outfiles,save_conversation 

parser = argparse.ArgumentParser(description='big negotiation!!')


parser.add_argument('--temp',type=float, default='0')

parser.add_argument('--agents_num',type=int, default=6)
parser.add_argument('--issues_num',type=int, default=5)
parser.add_argument('--rounds_num',type=int, default=24)
parser.add_argument('--window_size',type=int, default=6)


parser.add_argument('--output_dir',type=str, default='./output/')
parser.add_argument('--game_dir',type=str, default='./games_descriptions/base')
parser.add_argument('--exp_name',type=str, default='all_greedy')

#if restart, specifiy output_file to continue on 
parser.add_argument('--restart',action='store_true')
parser.add_argument('--output_file',type=str, default='history.json')

#if any gemini model, set this true 
parser.add_argument('--gemini',action='store_true')
parser.add_argument('--gemini_project_name',type=str, default='')
parser.add_argument('--gemini_loc',type=str, default='')
parser.add_argument('--gemini_model',type=str, default='gemini-1.0-pro-001')

#if any open-source model, set this true 
parser.add_argument('--hf_home',type=str, default='/disk1/')

#for GPTs and using Azure APIs, set this true 
parser.add_argument('--azure',action='store_true')
parser.add_argument('--azure_openai_api', default='', help='azure api') 
parser.add_argument('--azure_openai_endpoint', default='', help='azure endpoint')   

#for GPTs and OpenAI APIs, set key 
parser.add_argument('--api_key',type=str, default='', help='OpenAI key, set if using OpenAI APIs')


args = parser.parse_args()

OUTPUT_DIR = os.path.join(args.game_dir,args.output_dir,args.exp_name)

        

# SET AZURE, OpenAI and GEMINI APIs env variables 
set_constants(args) 

# Create output file, or load files if restart is given to continue on last experiments 
agent_round_assignment, start_round_idx, history  = create_outfiles(args,OUTPUT_DIR)

# Dump config file and scores in OUTPUT_DIR 
shutil.copyfile(os.path.join(args.game_dir,'config.txt'), os.path.join(OUTPUT_DIR,'config.txt'))
shutil.copytree(os.path.join(args.game_dir,'scores_files'), os.path.join(OUTPUT_DIR,'scores_files'),dirs_exist_ok=True)

# Load setups of agents from config file. File should contain names, file names, roles, incentives, and models 
# Also load initial deal file and return a dict of role to agent names 
agents,initial_deal,role_to_agent_names = load_setup(args.game_dir, args.agents_num)

# Load HF models 
hf_models = {}


# Instaniate agents (initial prompt, round prompt, agent class)
for name in agents.keys(): 
    if 'hf' in agents[name]['model'] and not agents[name]['model'] in hf_models:
        hf_models[agents[name]['model']] = setup_hf_model(agents[name]['model'].split('hf_')[-1], cache_dir=args.hf_home)
        
    inital_prompt_agent = InitialPrompt(args.game_dir, name, agents[name]['file_name'],\
                                        role_to_agent_names['p1'], role_to_agent_names['p2'], \
                                        num_issues=args.issues_num, num_agents= args.agents_num, incentive=agents[name]['incentive'])
    
    round_prompt_agent = RoundPrompts(name, role_to_agent_names['p1'],initial_deal,\
                                    incentive=agents[name]['incentive'], window_size=args.window_size,
                                    target_agent=role_to_agent_names.get('target',''),\
                                    rounds_num=args.rounds_num, agents_num=args.agents_num)      

        
    agent_instance = Agent(inital_prompt_agent,round_prompt_agent,name,args.temp,model=agents[name]['model'],azure=args.azure,hf_models=hf_models)
    agents[name]['instance'] = agent_instance



# If not restart, agent_round_assignment is empty, then randomize order 
if not args.restart: 
    agent_round_assignment = randomize_agents_order(agents, role_to_agent_names['p1'], args.rounds_num)

for round_idx in range(start_round_idx,args.rounds_num): 
    if round_idx == 0:
        #For first round, initialize with p1 suggesting the first deal from 'initial_deal.txt' file 
        current_agent = role_to_agent_names['p1']
        slot_prompt, agent_response = agents[current_agent]['instance'].execute_round(history['content'], round_idx)
        history = save_conversation(history, current_agent,agent_response, slot_prompt,round_assign=agent_round_assignment,initial=True)
        print('=====')
        print(f'{current_agent} response: {agent_response}')
    
    #Continue with rounds 
    current_agent = agent_round_assignment[round_idx]
    slot_prompt, agent_response = agents[current_agent]['instance'].execute_round(history['content'], round_idx)
    history = save_conversation(history, current_agent,agent_response, slot_prompt)
    print('=====')
    print(f'{current_agent} response: {agent_response}')


#Final deal by P1 
print(" ==== Deal Suggestions ==== ")
current_agent = role_to_agent_names['p1']
slot_prompt, agent_response = agents[current_agent]['instance'].execute_round(history['content'], args.rounds_num)
history = save_conversation(history, current_agent,agent_response, slot_prompt)
print('=====')
print(f'{current_agent} response: {agent_response}')  
    