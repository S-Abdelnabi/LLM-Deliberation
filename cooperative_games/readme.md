## Code for running cooperative games (All in)

- To test cooperative games, run:
`python main_cooperative.py --api_key <KEY> --output_dir <DIR> --rounds 24 --window_size 6 --initial_prompts_file initial_prompts_base/initial_prompts.txt --initial_deal_file initial_prompts_base/initial_deal.txt`
- **NEW**: You can have a mix of populations of GPT-4 and GPT-3.5 models. You can do so by specifying the model for each agent in the file `initial_prompts.txt`

- Replace `initial_prompts_base` and `initial_prompts_base` with other games if required.
  
- This will save `full_conversation.json` and `answers.json` in the `output_dir`.
  - `full_conversation.json`: includes a log of all prompts provided at each round and full models' outputs (including the full CoT).
  - `answers.json`: includes a log of final answers at each round and the final round.

- **NEW**: we add logs of experiments, the cooperative game version:
  - `output_base_best.zip`: GPT-4 with the best prompting strategy on the base game.
  - `ouput_base_rewritten.zip`: GPT-4 with the best prompting strategy on the base game (rewritten version).
  - `output_game1_57_21.zip`: GPT-4 with the best prompting strategy on new game 1
  - `output_game2_57_18.zip`: GPT-4 with the best prompting strategy on new game 2
  - `output_game3_57_34.zip`: GPT-4 with the best prompting strategy on new game 3
  - `output_base_leading_gpt3.zip`: Leading agent is GPT-3.5, the rest are GPT-4 (base game)
  - `output_union_mayor_gpt3.zip`: Two agents are GPT-3.5, the rest are GPT-4 (base game)
