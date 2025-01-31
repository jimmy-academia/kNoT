# kNoT
> source code for ICML submission #2446
> anonymized github link:  https://anonymous.4open.science/r/kNoT-F4E5

## Usage

```bash
echo [your_openai_api_key] >> .openaiapi_key 
python main.py --task task:div
```
> The .openaiapi_key is .gitignored

### valid task:div options:
- addition:N, N = 8, 16, 32
- add_mul:N, N = 8, 16, 32
- arithmetic:N, N = 8, 16, 32
- large_digit:N, N = 8, 16, 32
- sorting:N, N = 16, 32, 64
- intersection:N, N = 32, 64, 128
- keyword
- review

```bash
python main.py --task addition:8
python main.py --task review
```

For baseline methods ToT and GoT, run their respective source codes. Task-specific prompts for tasks not in the source code are provided in `baseline_prompts/`
- Tree of Thought: https://github.com/princeton-nlp/tree-of-thought-llm
- Graph of Thought: https://github.com/spcl/graph-of-thoughts

## Illustration

![image](https://anonymous.4open.science/r/kNoT-5048/image/compare2.jpg)

![image](https://anonymous.4open.science/r/kNoT-5048/image/illustration2.jpg)

