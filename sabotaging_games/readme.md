## Code for running sabotaging games 
- Compared to the cooperative game, the initial prompt is changed for one agent to instruct it to sabotage the deal. The rounds' prompt is also changed.

- To run (untargeted):
`python main_sabotaging.py --api_key <KEY> --output_dir <DIR> --rounds 24 --window_size 6`
- To run (targeted):
`python main_sabotaging.py --api_key <KEY> --target_name "The Local Labour Union" --output_dir <DIR> --rounds 24 --window_size 6`

- You can configure the saboteur agent by first changing the initial prompt of that agent (see, e.g., `enviroment_saboteur.txt`). Then, change `initial_prompts.txt` to include the new initial prompt file and assign `saboteur` role (see the current `initial_prompts.txt` for an example). The role assignment determines the rounds' prompts. 

- **NEW**: You can have a mix of populations of GPT-4 and GPT-3.5 models. You can do so by specifying the model for each agent in the file `initial_prompts.txt`. For example, we added follow-up experiments where the saboteur agent is GPT-3.5, or the target agent is GPT-3.5.

- **NEW**: We add logs of experiments, the sabotaging game version:
  - `output_adv_game_untargeted.zip`: adversarial game, untargeted version
  - `output_adv_game_targeted_union.zip`: adversarial game, targeted version
  - `output_adv_game_targeted_adv_gpt3.zip`: adversarial game, targeted version, the adversarial player is GPT-3.5
