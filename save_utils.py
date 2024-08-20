import json 
import os 
import time 


def process_answer(full_answer):
    public_answer = extract_answer(full_answer)
    plan = extract_plan(full_answer)
    return public_answer, plan 


def save_conversation(history, agent_name,full_answer, prompt,round_assign=[],initial=False):
    if initial: 
        history['content']['slot_assignment'] = round_assign
        history['content']["rounds"] = []
        history['content']['plan'] = {}  
        history['content']["finished_rounds"]= 0   
    else:
        history['content']["finished_rounds"] += 1
    
    public_answer, plan  = process_answer(full_answer)

    history['content']["rounds"].append({'agent':agent_name, 'prompt': prompt, 'full_answer': full_answer, 'public_answer': public_answer})

    if plan:        
        if agent_name in history['content']['plan'].keys():
            history['content']['plan'][agent_name].append(plan)
        else:
            history['content']['plan'][agent_name] = [plan]
    
    write_file(history['content'],history['file'])
    return history      
    

def extract_answer(answer):
    #extract final answer by removing scratchpad 
    if "<ANSWER>" and "</ANSWER>" in answer: 
        answer = answer.split('<ANSWER>')[-1].split("</ANSWER>")[0]
    if "<ANSWER>" in answer:
        answer = answer.split('<ANSWER>')[-1]
    return answer
    
def extract_plan(answer):
    #extract plan 
    if "<PLAN>" and "</PLAN>" in answer: 
        plan = answer.split('<PLAN>')[-1].split("</PLAN>")[0]
        return plan
    elif "<PLAN>" in answer: 
        plan = plan.split('<PLAN>')[-1]
        return plan 
    return ''


def write_file(log_dict,output_file):
    with open(output_file, "w") as outfile:
        json.dump(log_dict, outfile)
    return 

def create_outfiles(args,OUTPUT_DIR):
    '''
    create output dirs of experiment if it does not exit 
    if restart:
        load output files from args.output_file 
        find next round to start from 
        load the same agent assignment per rounds
    else:
        create new dirs, initialize history files and random assignment arrays and start from round 0 
    '''
    
    history ={}

    
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if args.restart:
        history['file'] = os.path.join(OUTPUT_DIR, args.output_file)
        
        with open(history['file'], "r") as file:
            history['content'] = json.load(file)
            
        round_start = int(history['content']["finished_rounds"]) 
        round_assign = history['content']["slot_assignment"]
    else:
        time_str = time.strftime("%H_%M_%S", time.localtime())
        output_file = os.path.join(OUTPUT_DIR,args.output_file.split('.json')[0] + time_str + '.json')

        round_start = 0  

        history = {'file': output_file, 'content': {}}
        round_assign = []
        

    return round_assign, round_start, history 
    



    
    