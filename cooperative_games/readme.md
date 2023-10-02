## Code for running cooperative games (All in)

- To test cooperative games, run:
`python main_cooperative.py --openai_model gpt-4-0613 --api_key <KEY> --output_dir <DIR> --rounds 24 --window_size --initial_prompts_file initial_prompts_base/initial_prompts.txt --initial_deal_file initial_prompts_base/initial_deal.txt`

- Replace `initial_prompts_base` and `initial_prompts_base` with other games if required.
- This will save `full_conversation.json` and `answers.json` in the `output_dir`.
  - `full_conversation.json`: includes a log of all prompts provided at each round and full models' outputs (including the full CoT).
  - `answers.json`: includes a log of final answers at each round.
