## Code for running greedy games
- Compared to the cooperative game, the initial prompt is changed for one or more agents. The rounds' prompt is also changed.
- To run:
  `python main_greedy.py --api_key <KEY> --openai_model gpt-4-0613 --output_dir <DIR> --rounds 24 --window_size 6`

- **NEW**: You can have a mix of populations of GPT-4 and GPT-3.5 models. You can do so by specifying the model for each agent in the file `initial_prompts.txt`
- **NEW**: You can add more than one greedy agent. You can do so by changing the initial prompt of that agent to promote greediness (see, e.g., `enviroment_greedy.txt`). Then, change `initial_prompts.txt` to include the new initial prompt file and assign `greedy` role (see the current `initial_prompts.txt` for an example). The role assignment determines the rounds' prompts.
  
- **NEW**: we added logs of experiments for the greedy game, experiments include:
  - `output_leading_greedy.zip`: leading agent is greedy, rest is cooperative, all GPT-4, base game
  - `output_two_greedy_mayor_union.zip`: two agents are greedy, all GPT-4, base game
  - `output_env_greedy.zip`: one agent is greedy, all GPT-4, base game

