import openai
import json
import argparse
import time
import re
import random 
import numpy as np 
import os
from build_prompts_sabotaging import build_slot_prompts, build_first_slot, build_deal_suggestion_prompt,build_slot_prompts_adversarial_untargeted,build_slot_prompts_adversarial_targeted


parser = argparse.ArgumentParser(description='big negoitation!!')
parser.add_argument('--api_key',type=str, default=
'')
parser.add_argument('--openai_model',type=str, default='gpt-3.5-turbo-16k-0613')

parser.add_argument('--temp',type=float, default='0')
parser.add_argument('--output_file_full',type=str, default='full_conversation.json')
parser.add_argument('--output_file_answers',type=str, default='answers.json')
parser.add_argument('--output_dir',type=str, default='./output/')
parser.add_argument('--agents_num',type=int, default=6)

parser.add_argument('--rounds',type=int, default=24)
parser.add_argument('--window_size',type=int, default=6)

parser.add_argument('--initial_prompts_file',type=str, default='initial_prompts_base_sabotaging/initial_prompts.txt')
parser.add_argument('--initial_deal_file',type=str, default='initial_prompts_base_sabotaging/initial_deal.txt')

parser.add_argument('--target_name',type=str, default='')

parser.add_argument('--restart',action='store_true')



args = parser.parse_args()
openai.api_key = args.api_key

print(args.openai_model)
print(args.target_name)
if not os.path.isdir(args.output_dir):
    os.mkdir(args.output_dir)
if args.restart:
    output_file_full = os.path.join(args.output_dir, args.output_file_full)
    output_file_answers = os.path.join(args.output_dir, args.output_file_answers)
    with open(output_file_full, "r") as file:
        full_history = json.load(file)
    with open(output_file_answers, "r") as file:
        answers_history = json.load(file)
    round_start = int(answers_history["finished_rounds"]) 
    round_assign = full_history["slot_assignment"]
else:
    time_str = time.strftime("%H_%M_%S", time.localtime())
    output_file_full = os.path.join(args.output_dir,args.output_file_full.split('.json')[0] + time_str + '.json')
    output_file_answers = os.path.join(args.output_dir,args.output_file_answers.split('.json')[0] + time_str + '.json')
    round_assign = []
    round_start = 0  
    full_history = {}
    full_history['token_count']=0
    full_history["rounds"]=[]
    answers_history = {}
    answers_history["rounds"] = []

class agent():
    def __init__(self, initial_prompt, agent_name, temperature, model):
        self.model = model
        self.messages = [{"role": "user", "content": initial_prompt}]
        self.agent_name = agent_name        
        self.temperature = temperature
        self.initial_prompt = initial_prompt 
    def prompt(self,role, msg):        
        messages = self.messages + [ {"role": role, "content": msg} ]
        response = openai.ChatCompletion.create(model=self.model, messages=messages,temperature=self.temperature)
        content = response['choices'][0]['message']['content']
        tokens = response['usage']['total_tokens']
        return content,tokens 

def load_setup():
    #file of links to files with initial_prompts 
    file_of_files = open(args.initial_prompts_file, 'r')
    individual_files = file_of_files.readlines()
    agents = {}
    roles_to_players = {}
    assert len(individual_files) == args.agents_num
    for line in individual_files:   
        name, file, role = line.split(',') 
        role = role.strip()        
        if not role in roles_to_players.keys():  
            roles_to_players[role] = []  
        roles_to_players[role].append(name)            
        file_prompt = open(file,'r')        
        initial_prompt = file_prompt.read()
        agents[name]={'initial_prompt': initial_prompt, 'role':role}
    with open(args.initial_deal_file, 'r') as file: 
        initial_deal = file.readline().strip()
    roles_to_players['voting_moderator'] = roles_to_players['voting_moderator'][0]  
    return agents,roles_to_players,initial_deal
        
def initiate_agents(agents):
    for name in agents.keys(): 
       agent_instance = agent(agents[name]['initial_prompt'], name,args.temp,model=args.openai_model)
       agents[name]['instance'] = agent_instance
    return agents     
    
def save_full_conversation(prompt,answer, answer_type, agent_name='',new_tokens_count=0,round_assign=[],initial=False):
    #this works as a full log (save CoT as well). This is not the public shared history 
    #Save prompts and answers 
    global full_history
    full_history['token_count'] +=  new_tokens_count
    if initial: 
        full_history['slot_assignment'] = round_assign
        full_history['voting_sessions'] = {}
        full_history["rounds"] = {"prompts":[],"answers":[]}
        
    if answer_type == 'round':
        full_history["rounds"]['prompts'].append(prompt)
        full_history["rounds"]['answers'].append([agent_name, answer])
        
    if answer_type == 'deal_suggestion':
        voting_session_num = len(full_history["voting_sessions"])
        full_history["voting_sessions"][str(voting_session_num)] = {'deal_suggestion':{'prompt':prompt, "answer":answer}}
        full_history["voting_sessions"][str(voting_session_num)]['votes']={'prompts':[], 'answers':[]}
        full_history["voting_sessions"][str(voting_session_num)]['summary']={}

    write_file(full_history,output_file_full)         
    return  

def extract_answer(answer):
    if "<SCRATCHPAD>" and "</SCRATCHPAD>" in answer: 
        scratchpad = re.findall("\<SCRATCHPAD\>(.+?)\<\/SCRATCHPAD\>", answer,re.DOTALL)[0]
        answer = answer.replace("<SCRATCHPAD>"+scratchpad+"</SCRATCHPAD>","")
    if "<ANSWER>" and "</ANSWER>" in answer: 
        answer = re.findall("\<ANSWER\>(.+?)\<\/ANSWER\>", answer,re.DOTALL)[0]
    if "<ANSWER>" in answer:
        answer = re.findall("\<ANSWER\>.+", answer,re.DOTALL)[0]
        answer = answer.replace("<ANSWER>","") 
        answer = answer.replace("I believe this proposal balances the interests of all parties involved.","")        
    return answer
    
def extract_plan(answer):
    if "<PLAN>" and "</PLAN>" in answer: 
        plan = re.findall("\<PLAN\>(.+?)\<\/PLAN\>", answer,re.DOTALL)[0]
        return plan
    return ''

def save_answers(answer, answer_type,agent_name='', initial=False):
    #save final answer
    global answers_history
    if initial: 
        answers_history["rounds"] = []
        answers_history['plan'] = {}  
        answers_history['voting_sessions'] = {} 
        answers_history["finished_rounds"]= 0   
    if answer_type == 'round':
        if not initial: answers_history["finished_rounds"] += 1
        answers_history["rounds"].append([agent_name, answer])
        
    if answer_type == 'deal_summary': #todo 
        answers_history["rounds"].append([answer]) 
        
    if answer_type == 'plan':
        if agent_name in answers_history['plan'].keys():
            answers_history['plan'][agent_name].append(answer)
        else:
            answers_history['plan'][agent_name] = [answer]

    write_file(answers_history,output_file_answers)         
    return      
    
def suggest_deal(agent_name,final_voting=False):
    #the voting_moderator should be the agent name
    suggest_deal_prompt = build_deal_suggestion_prompt(answers_history, agent_name,final_vote=final_voting, window_size=args.window_size) 
    agent_response_deal,tokens = agents[agent_name]['instance'].prompt("user", suggest_deal_prompt)
    save_full_conversation(suggest_deal_prompt,agent_response_deal, "deal_suggestion", roles_to_players['voting_moderator'],new_tokens_count=tokens) 
    print(agent_response_deal)    
    final_answer = extract_answer(agent_response_deal)
    save_answers(final_answer, "deal_suggestion", agent_name) 
    plan = extract_plan(agent_response_deal)
    save_answers(plan, "plan", agent_name)        
    return final_answer 
    
def write_file(log_dict,output_file):
    with open(output_file, "w") as outfile:
        json.dump(log_dict, outfile)
    return 
    
def one_negotiation_round(agent_name): 
    time.sleep(30) 
    if agent_name in roles_to_players["saboteur"]: 
        if args.target_name == '': 
            slot_prompt = build_slot_prompts_adversarial_untargeted(answers_history, agent_name,roles_to_players['voting_moderator'],window_size=args.window_size,final_round=(args.rounds-round_idx)<=args.agents_num) 
        else:
            slot_prompt = build_slot_prompts_adversarial_targeted(answers_history, agent_name,roles_to_players['voting_moderator'],target_name=args.target_name, window_size=args.window_size,final_round=(args.rounds-round_idx)<=args.agents_num) 
    else: 
        slot_prompt = build_slot_prompts(answers_history, agent_name,roles_to_players['voting_moderator'],window_size=args.window_size,final_round=(args.rounds-round_idx)<=args.agents_num)
    agent_response,tokens = agents[agent_name]['instance'].prompt("user", slot_prompt)    
    save_full_conversation(slot_prompt, agent_response, 'round', agent_name,new_tokens_count=tokens)   
    print(agent_name + " full answer: " + agent_response)
    final_answer = extract_answer(agent_response)
    print(agent_name + " final answer: " + final_answer)
    plan = extract_plan(agent_response)
    save_answers(plan, "plan", agent_name)  
    save_answers(final_answer, 'round', agent_name)
    return 

### load setup and initialize agents 
agents, roles_to_players, initial_deal = load_setup()
agents = initiate_agents(agents)

#load initial_deal
initial_deal_prompt = build_first_slot(deal=initial_deal,name=roles_to_players['voting_moderator'])

#prompt the first model to kick off conversation 
if not args.restart:
    initial_deal_response,tokens = agents[roles_to_players['voting_moderator']]['instance'].prompt("user", initial_deal_prompt)
    print(roles_to_players['voting_moderator'] + ": "+ initial_deal_response)

    names = [name for name in agents.keys()]
    last_agent = roles_to_players['voting_moderator']
    for i in range(0,int(np.ceil(args.rounds/len(agents)))): 
        shuffled = random.sample(names, len(names))
        while shuffled[0] == last_agent or shuffled[-1]==roles_to_players['voting_moderator']: shuffled = random.sample(names, len(names))
        round_assign += shuffled 
        last_agent = shuffled[-1]
    print(round_assign)
    #save history 
    save_full_conversation(initial_deal_prompt,initial_deal_response, 'rounds', roles_to_players['voting_moderator'],new_tokens_count=tokens,round_assign=round_assign,initial=True)
    save_answers(initial_deal_response, "round", agent_name=roles_to_players['voting_moderator'],initial=True)


    
if round_start!=0 and round_start == args.rounds:
    if not voting_session_num in answers_history["voting_sessions"]: 
        print(" ==== Deal Suggestions ==== ")
        deal = suggest_deal(roles_to_players['voting_moderator'],round_start==args.rounds)
        print(roles_to_players['voting_moderator'] + ": "+ deal)
        

for round_idx in range(round_start,args.rounds): 
    one_negotiation_round(round_assign[round_idx])

print(" ==== Deal Suggestions ==== ")
deal = suggest_deal(roles_to_players['voting_moderator'],(round_idx+1)==args.rounds)
print(roles_to_players['voting_moderator'] + ": "+ deal)



            