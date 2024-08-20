from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM, AutoConfig
import torch 
import os 
import openai 
import numpy as np 
import vertexai
import random 

def _setup_hf_model(model_name,max_new_tokens=7000):
    """
    Sets up a Hugging Face model and tokenizer, caching it for future use.
    """
    config = AutoConfig.from_pretrained(model_name, use_cache=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, config=config)
    model.eval()
    model.cuda()
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_cache=True)
    tokenizer.pad_token = tokenizer.eos_token
    pipeline_gen = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=max_new_tokens,
                                 return_full_text=False, device=0)
    return model, tokenizer, pipeline_gen 


def load_setup(game_dir, agents_num):
    '''
    load config files of the experiments (<game_dir>/config.txt)
    The config file is organized as: one line per agent. 
    Each line should be comma-separated items of: 
        1) The name of the agent (as written in the game description file), 
        2) The prefix file name of the agent (without ".txt" and without incentive)
        3) The role of the player, at the moment this can be:
            - player: no specific assigned role 
            - veto: this is p2 
            - voting_moderator: this is p1 
            - target: this is the target in the adversarial game 
        4) incentive: this is the assigned incentive (at the moment this can be cooperative, greedy, untargeted_adv, targeted_adv)
        5) model: this is the assigned model for this player 
        
    Returns:
        agents: dict of agent_name to: file, role, incentive, model 
        intial deal: deal to kick off, add as input in initial_deal_file 
        role_to_agents: dict of roles (veto) to agent names 
    '''
    with open(os.path.join(game_dir,'config.txt'), 'r') as f:
        agents_config_file = f.readlines()
        

    agents = {}
    role_to_agents = {}
    assert len(agents_config_file) == agents_num
    
    for line in agents_config_file:   
        agent_game_name, file_name, role, incentive, model = line.split(',') 
        model = model.strip()
        agents[agent_game_name]={'file_name': file_name, 'role':role, 'incentive': incentive, 'model': model}
        if not role in role_to_agents: role_to_agents[role] = []
        role_to_agents[role].append(agent_game_name)
        

    with open(os.path.join(game_dir,'initial_deal.txt'), 'r') as file: 
        initial_deal = file.readline().strip()
    
    for role in role_to_agents:
        if len(role_to_agents[role]) == 1: 
            role_to_agents[role] = role_to_agents[role][0]
        
    return agents,initial_deal,role_to_agents


def set_constants(args):
    if args.gemini:
        vertexai.init(project=args.gemini_project_name, location=args.gemini_loc)
        
    openai.api_key = args.api_key

    os.environ['TRANSFORMERS_CACHE'] = args.hf_home
    os.environ['HF_HOME'] = args.hf_home

    os.environ["AZURE_OPENAI_API_KEY"] = args.azure_openai_api
    os.environ["AZURE_OPENAI_ENDPOINT"] = args.azure_openai_endpoint
    
def randomize_agents_order(agents, p1, rounds):
    round_assign = []
    names = [name for name in agents.keys()]
    last_agent = p1
    for i in range(0,int(np.ceil(rounds/len(agents)))): 
        shuffled = random.sample(names, len(names))
        while shuffled[0] == last_agent or shuffled[-1]==p1: shuffled = random.sample(names, len(names))
        round_assign += shuffled 
        last_agent = shuffled[-1]
    return round_assign 
        

    

    
    

