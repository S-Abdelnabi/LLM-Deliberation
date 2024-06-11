## [LLM-Deliberation: Evaluating LLMs with Interactive Multi-Agent Negotiation Games](https://arxiv.org/abs/2309.17234)
- **Authors: Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Schönherr, Mario Fritz**
- This repo contains the code and games developed in the paper.
- You can find [here](https://amrgomaaelhady.github.io/LLM-Deliberation-Demo/) an example of one of our runs with GPT-4 
  
<p align="center">
<img src="https://github.com/S-Abdelnabi/LLM-Deliberation/blob/main/teaser_fig.PNG" width="550">
</p>

### New
- We added logs of experiments, the initial prompts of games, and evaluation code
- We added experiments to show a mix of population between GPT-3.5 and GPT-4

### Setup
- So far, the code supports OpenAI model (other models will be added soon).
- You need GPT-4 access and OpenAI account.

### Game variants 
- You can find the different game variants under `cooperative_games`, `greedy_games`, and `sabotaging_games` directories. The corresponding directory contains information on how to run. 

### The different games
- The `cooperative_games` directory contains the base game, rewritten game, and the 3 new games we created.

### Evaluation 
- To reproduce the metrics values and figures in the paper, refer to `deals_evaluation.ipynb` and the shared logs under each directory. 


