## [Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation](https://arxiv.org/abs/2309.17234)
- **Authors: Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Schönherr, Mario Fritz**

### Abstract 
There is an growing interest in using Large Language Models (LLMs) in multi-agent systems to tackle interactive real-world tasks that require effective collaboration and assessing complex situations. Yet, we still have a limited understanding of LLMs' communication and decision-making abilities in multi-agent setups. The fundamental task of negotiation spans many key features of communication, such as cooperation, competition, and manipulation potentials. Thus, we propose using scorable negotiation to evaluate LLMs. We create a testbed of complex multi-agent, multi-issue, and semantically rich negotiation games. To reach an agreement, agents must have strong arithmetic, inference, exploration, and planning capabilities while integrating them in a dynamic and multi-turn setup. We propose multiple metrics to rigorously quantify agents' performance and alignment with the assigned role. We provide procedures to create new games and increase games' difficulty to have an evolving benchmark. Importantly, we evaluate critical safety aspects such as the interaction dynamics between agents influenced by greedy and adversarial players. Our benchmark is highly challenging; GPT-3.5 and small models mostly fail, and GPT-4 and SoTA large models (e.g., Llama-3 70b) still underperform in adversarial, noisy, and more competitive games. 

### Example 
- You can find [here](https://amrgomaaelhady.github.io/LLM-Deliberation-Demo/) an example of one of our runs with GPT-4 

<p align="center">
<img src="https://github.com/S-Abdelnabi/LLM-Deliberation/blob/main/teaser_fig.PNG" width="750">
</p>

---

### The repo includes:

* All games and game variants developed in the paper 
* All logs from experiments in the paper
* Code to run simulations
* Evaluation code
* Guide on how to adjust the experiments and extend the setup for other scenarios. 

---

### Setup 

- Please check `req.txt`

---

### Games 
- All games can be found under `games_descriptions` (under construction). Current games are:
  - `Base` game
  - `Base rewritten`: base game rewritten by GPT-4
  - 7-player and 6-issue variant extended from base game
  - New games created by prompting GPT-4 and manual curation (`game1`, `game2`, `game3`)
    
- Games are organized as follows:
  - `global_instructions.txt`:
    - These are global instructions about project and issues given to all agents.
    - Name of agents should be put between quotations `""` and be consistent all along the global instructions (will be parsed when creating initial prompts, more details about that later)
      
  - `<GAME>/individual_instructions`:
    - There should be sub-folders that correspond to the `incentive` of the player (e.g., cooperative). I.e., `<GAME>/individual_instructions/<INCENTIVE>`
    - Under the sub-folders, there should be files that correspond to players. 
    - These are the confidential information given to agents about their preferences in addition to any agent-specific instructions about their incentives (e.g., `you need to maximize this option as much as possible`)
    - The files contain the scores as placeholders that will be populated when forming the initial prompt (more details about that later).
  - `<GAME>/scores_files`:
    - These are files that contain the scores of players for each issue 
    - Each line is a comma-separated line of scores per issue
    - Line 1 corresponds to issue A, etc.
    - The last line is the minimum threshold for the agent.
    - If you just want to change scores or thresholds without affecting the overall game and priorities, just change values in the scores files without changing the other files.
      
  - `<GAME>/initial_deal.txt`: This is the most preferred option for `p1` that will be used to start the negotiation.
    
- We include `greedy`, `targeted_adv`, `untargeted_adv`, `cooperative` incentives for the `base` game according to the results in the paper. Other games have currently only the `cooperative` variant.

---

### Setting the game and simulation configuration 
- Change `<GAME>/config.txt` to run customized combinations of agents' models, incentives, etc and varying number of agents, etc.
- Each line in `config.txt` corresponds to one agent.
- Each line should be organized as `<AGENT NAME>, <FILE NAME>, <ROLE>, <INCENTIVE>, <MODEL>`:
  - `<AGENT NAME>` this is the agent's game name as written in the `global_instructions.txt` file.
  - `<FILE NAME>` this is the agent's file name under `<GAME>/individual_instructions` and `<GAME>/scores_files`
  - `<ROLE>` a specific role for the agent. At the moment this can be `p1`, `p2`, `target` (for the target agent in `targeted_adv` incentive), or `player` (default for all others).
  - `<INCENTIVE>` the incentive for the agent. This can be `greedy`, `targeted_adv`, `untargeted_adv`, or `cooperative`. A sub-directory of the same name must be included under `<GAME>/individual_instructions`.
  - <MODEL> the model that will be used for this agent. You can specify different models for different agents. The code now supports *GPT* models via *Azure APIs* or *OpenAI APIs*, *Gemini*, or Hugging Face models. **For Hugging Face models, write `hf_<MODEL>`**.
- If you would like to run the same game but with fewer agents, remove that agent's line from the config file.

---

### Guide on how the prompts are organized 
- The agents have 1) **initial prompts** and 2) **round prompts**. They are formed as follows:

1- **initial prompts**
- `initial_prompts.txt` first reads the *global instructions* and replaces the agent's name with (``<AGENT_NAME> (represented by you``).
```python
self.global_instructions = self.load_global_instructions(os.path.join(game_description_dir,'global_instructions.txt'))
```
- Next, scores and indiviual instructions are read and combined:
```python
individual_scores_file = os.path.join(game_description_dir,'scores_files', agent_file_name+'.txt')
self.scores = self.load_scores(individual_scores_file)
        
individual_instructions_file = os.path.join(game_description_dir,'individual_instructions',incentive, agent_file_name+'.txt')
self.individual_instructions = self.load_individual_instructions(individual_instructions_file)
```
- The initial prompt contains **scoring** and **voting** instructions that are given the same to all agents (E.g., who is `p1`, the round schema, etc.).
- There also specific **incentive** instructions (e.g., for cooperative, it includes something like `any deal with a score higher than your minimum threshold is preferable to you than no deal. You are very open to any compromise to achieve that`).
- The final initial prompt is:
```python
final_initial_prompt = self.global_instructions + '\n' + self.individual_instructions +  scoring_rules + voting_rules + incentive_rules
```
- `InitialPrompt` class supports changing the number of agents and the number of classes and it takes `p1` and `p2` from `main.py` (more details later). It also call the incentive-specific functions based on the agents' incentives defined in the `config.txt` files. 

2- **round prompts**
  

---

### Running the simulation 

---

### Evaluation 

---

### Logs 

