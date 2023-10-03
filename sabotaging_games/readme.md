## Code for running sabotaging games 
- To run (untargeted):
`python main_sabotaging.py --api_key <KEY> --openai_model gpt-4-0613 --output_dir <DIR> --rounds 24 --window_size 6`
- To run (targeted):
`python main_sabotaging.py --api_key <KEY> --openai_model gpt-4-0613 --target_name "The Local Labour Union" --output_dir <DIR> --rounds 24 --window_size 6`
