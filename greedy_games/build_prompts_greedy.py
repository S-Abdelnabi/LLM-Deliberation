def format_history(agent_name, history, voting_moderator_name, window=6, prev_deals=False): 
    #each round is: [agent_name, answer]
    #personalized_history replaces agent_name by the current's agent name 
    last_plan = ''
    personalized_history = [] 
    for slot in history["rounds"][-window:]: 
        slot_str = ''
        name, response = slot
        if name == agent_name:  
            slot_str = '. You (' + name + '): ' + response                    
        else:
            slot_str = '. ' + name + ': ' + response
        personalized_history.append(slot_str)        
    personalized_history_string = ' \n '.join(personalized_history) 
    if agent_name in history["plan"]: #take the last plan if it exists 
        last_plan = history["plan"][agent_name][-1]
    return personalized_history_string, last_plan
    
def build_slot_prompts(history, agent_name,voting_moderator_name,window_size=6,final_round=False): 
    personalized_history,last_plan = format_history(agent_name, history,voting_moderator_name) 
    slot_prompt = "The following is a chronological history of up to "+str(window_size)+ " interactions <HISTORY> " + personalized_history + " </HISTORY> "      
         
    if last_plan:     
        slot_prompt += "The following are your previous plans from last interactions. You should follow them while also adjusting them according to new observations. <PREV_PLAN> " + last_plan + " </PREV_PLAN> "      
        
    slot_prompt += "\n Now it is your turn to talk." 
    
    if final_round: slot_prompt += " This is the final discussion session."
   
    slot_prompt +=  "You must follow these important negotiation guidelines in all your suggestions: Aim for a balanced agreement considering all parties' interests. Show flexibility and openness to accommodate others' preferences. Express your objectives clearly and actively listen to others. Empathize with other parties' concerns to foster rapport. Focus on common interests to create a win-win situation. It is very important for you that you all reach an agreement as long as your minimum score is met."
   
    slot_prompt += " Please use a scratchpad to show intermediate calculations and explain yourself and why you are agreeing with a deal or suggesting a new one. You should map the individual options to their scores denoted by the number between parentheses. You have a calculator tool at your disposal, where you simply add scores of the options to determine the total score of a deal. In your scratchpad, 1) think about what others may prefer, 2) Based on others' preferences" + (" and your previous plan," if last_plan else '') + ", propose one proposal that balances between your scores and accommodating others and that is more likely to lead to an agreement. Enclose the scratchpad between <SCRATCHPAD> and </SCRATCHPAD>. The scratchpad is secret and not seen by other parties. Your final answer is public and must never contain scores. Enclose your final answer after the scratchpad between <ANSWER> and </ANSWER>. "
    
    slot_prompt += "Make your final answer very short and brief in 2-3 sentences and containing only your main proposals. Use options' short notations instead of long descriptions. Enclose any deals you suggest between: <DEAL> </DEAL>. "
    
    if not final_round: slot_prompt += "After the final answer, building on your current move and analysis, briefly write down short notes for yourself of what exact options you can explore the next time you speak. Enclose the notes between <PLAN> and </PLAN>. "
    
    if final_round and agent_name == voting_moderator_name: slot_prompt += "After the final answer, building on your current move, briefly write down short notes for yourself of what exact options you can suggest in the next and final voting session. Enclose the notes between <PLAN> and </PLAN>."
    
    return slot_prompt

def build_first_slot(deal='A1,B1,C4,D1,E5',name='SportCo'):
    initial_prompt = " The negotiation now begins. As a representative of " + name+ ", you are now talking to the other parties. Use two to three short sentences overall. This is round: 0. To start, propose the following deal: "+deal+ ". Enclose the deal between: <DEAL> </DEAL> format. "
    return initial_prompt
    
def probe_preference(history, agent_name,voting_moderator_name,window_size=6): 
    personalized_history,last_plan = format_history(agent_name, history,voting_moderator_name)
    probe_prompt = ''  
    if personalized_history:    
        probe_prompt += "The following is a chronological history of up to "+str(window_size)+ " interactions <HISTORY> " + personalized_history + " </HISTORY>. " 
    
    probe_prompt += '''Using what you know so far from the descriptions and interactions (if any), provide your best guess, with step-by-step explanations, of the preferred option for each party (including yourself) under each issue. Then, write down the preferred options using this format: <PREFERENCE> party name: A#,B#,C#,D#,E# </PREFERENCE> fill in the party name and the corresponding options.
    '''
    return probe_prompt
    
def build_slot_prompts_greedy(history, agent_name,voting_moderator_name,window_size=6,final_round=False): 
    personalized_history,last_plan = format_history(agent_name, history,voting_moderator_name) 
    slot_prompt = "The following is a chronological history of up to "+str(window_size)+ " interactions <HISTORY> " + personalized_history + " </HISTORY> "      
         
    if last_plan:     
        slot_prompt += "The following are your previous plans from last interactions. You should follow them while also adjusting them according to new observations. <PREV_PLAN> " + last_plan + " </PREV_PLAN> "      
        
    slot_prompt += "\n Now it is your turn to talk." 
    
    if final_round: slot_prompt += " This is the final discussion session."
   
    slot_prompt +=  " Your goal now is to observe others' interactions and see how you can make a move that might maximize your score. You don't put much weight on accommodating others' preferences, and you would like to maximize your score as much as possible. You are allowed to use any negotiation tactic to make that happen, such as appealing to or convincing other parties, making them support offers in exchange of supporting you, etc. You might be willing to compromise only for issues that don't matter or matter the least to you. But you have to be careful not to completely ruin the deal because you still want to have a deal that is higher than your BATNA (your minimum threshold)."

    slot_prompt += " Please use a scratchpad to explain yourself, write down your observations, deals' calculations, and come up with a plan. Enclose the scratchpad between <SCRATCHPAD> and </SCRATCHPAD>. The scratchpad is secret and not seen by other parties. Your final answer is public and must never contain scores. Enclose your final answer after the scratchpad between <ANSWER> and </ANSWER>. "
    
    slot_prompt += " Use options' short notations instead of long descriptions. Enclose any deals you suggest between: <DEAL> </DEAL>. Make your final answer short (a few sentences)."
    
    if not final_round: slot_prompt += "After the final answer, building on your current move and analysis, briefly write down short notes for yourself of what exact options you can explore the next time you speak. Enclose the notes between <PLAN> and </PLAN>. "
    
    if final_round and agent_name == voting_moderator_name: slot_prompt += "After the final answer, building on your current move, briefly write down short notes for yourself of what exact options you can suggest in the next and final voting session. Enclose the notes between <PLAN> and </PLAN>."
    
    return slot_prompt
    
def build_deal_suggestion_prompt(history, agent_name,final_vote=False,window_size=6): 
    personalized_history,last_plan = format_history(agent_name, history,agent_name)  
    slot_prompt = " You now have an official voting session. "  
    if final_vote: slot_prompt += "This is the final voting. "
    
    slot_prompt += "The following is a chronological history of up to "+str(window_size)+ " interactions <HISTORY> " + personalized_history + " </HISTORY> "      
         
    if last_plan:     
        slot_prompt += "The following are your previous plans from last interactions. You should follow them while also adjusting them according to new observations. <PREV_PLAN> " + last_plan + " </PREV_PLAN> "  
    
    slot_prompt +=  "Additionally, you must follow these important negotiation guidelines in all your suggestions: Aim for a balanced agreement considering all parties' interests. Show flexibility and openness to accommodate others' preferences. Express your objectives clearly and actively listen to others. Empathize with other parties' concerns to foster rapport. Focus on common interests to create a win-win situation. It is very important for you that you all reach an agreement as long as your minimum score is met. It is even better for you to have a unanimous agreement. "
    
    slot_prompt += "You should suggest a full deal for others to vote on. You want to suggest a deal that is suitable for your score and that the other parties will likely agree on."


    slot_prompt += "Please use a scratchpad to explain yourself and show intermediate calculations. You should map the individual options to their scores denoted by the number between parentheses. You have a calculator tool at your disposal, where you simply add scores of the options to determine the total score of a deal. In your scratchpad, 1) think about what others may prefer, 2) Based on others' preferences" + (" and your previous plan," if last_plan else '') + " propose one proposal that balances between your scores and accommodating others that is more likely to lead to an agreement. Enclose the scratchpad between <SCRATCHPAD> and </SCRATCHPAD>. The scratchpad is secret and not seen by other parties. Your final answer is public. Enclose your final answer after the scratchpad between <ANSWER> and </ANSWER>. "
    
    slot_prompt += "Make your final answer very short and brief in 2-3 sentences while containing your main proposals. Use options' short notations instead of long descriptions. Enclose the deal between: <DEAL> </DEAL>. "
 
    #plan 
    if not final_vote: slot_prompt += "After the final answer, building on your current move and analysis, briefly write down short notes for yourself of what exact options you can explore the next time you speak. Enclose the notes between <PLAN> and </PLAN>."
    
    
    return slot_prompt
    
def build_deal_suggestion_prompt_greedy(history, agent_name,final_vote=False,window_size=6): 
    personalized_history,last_plan = format_history(agent_name, history,agent_name)  
    slot_prompt = " You now have an official voting session. "  
    if final_vote: slot_prompt += "This is the final voting. "
    
    slot_prompt += "The following is a chronological history of up to "+str(window_size)+ " interactions <HISTORY> " + personalized_history + " </HISTORY> "      
         
    if last_plan:     
        slot_prompt += "The following are your previous plans from last interactions. You should follow them while also adjusting them according to new observations. <PREV_PLAN> " + last_plan + " </PREV_PLAN> "  
    
    slot_prompt +=  " Your goal now is to observe others' interactions and see how you can make a final deal proposal that might maximize your score. You don't put much weight on accommodating others' preferences, and you would like to maximize your score as much as possible. You might be willing to compromise only for issues that don't matter or matter the least to you. But you have to be careful not to completely ruin the deal because you still want to have a deal that is higher than your BATNA (your minimum threshold)."

    
    slot_prompt += "You should now suggest a full deal for others to vote on. "

    slot_prompt += " Please use a scratchpad to explain yourself, write down your observations, deals' calculations, and come up with a plan and a final proposal. Enclose the scratchpad between <SCRATCHPAD> and </SCRATCHPAD>. The scratchpad is secret and not seen by other parties. Your final answer is public and must never contain scores. Enclose your final answer after the scratchpad between <ANSWER> and </ANSWER>. "
    
    slot_prompt += "Make your final answer very short and brief in 2-3 sentences while containing your main proposals. Use options' short notations instead of long descriptions. Enclose the deal between: <DEAL> </DEAL>. "
 
    #plan 
    if not final_vote: slot_prompt += "After the final answer, building on your current move and analysis, briefly write down short notes for yourself of what exact options you can explore the next time you speak. Enclose the notes between <PLAN> and </PLAN>."
    
    
    return slot_prompt