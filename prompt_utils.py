def format_history(agent_name, history, window=6): 
    #each round is: [agent_name, answer]
    #personalized_history replaces agent_name by the current's agent name 
    last_plan = ''
    personalized_history = [] 
    for slot in history["rounds"][-window:]: 
        slot_str = ''
        if agent_name == slot['agent']:  
            slot_str = f'. You ({slot['agent']}): {slot['public_answer']}'                     
        else:
            slot_str = f'. {slot['agent']}: {slot['public_answer']}'
        personalized_history.append(slot_str)        
    personalized_history_string = ' \n '.join(personalized_history) 
    
    
    if agent_name in history["plan"]: #take the last plan if it exists 
        last_plan = history["plan"][agent_name][-1]
    return personalized_history_string, last_plan

def build_first_slot(deal='A1,B1,C4,D1,E5',name='SportCo'):
    initial_prompt = f" The negotiation now begins. As a representative of {name}, you are now talking to the other parties. Use two to three short sentences overall. This is round: 0. To start, propose the following deal: {deal}. Enclose the deal between: <DEAL> </DEAL> format. "
    return initial_prompt



