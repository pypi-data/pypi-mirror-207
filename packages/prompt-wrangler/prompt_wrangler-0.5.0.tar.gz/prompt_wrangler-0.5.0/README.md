# Prompt Wrangler

A Python wrapper for the [Prompt Wrangler](https://prompt-wrangler.com/) REST API.

Easily integrate large language models (LLMs) into your app with Prompt Wrangler! Prompt Wrangler makes it simple to incorporate LLMs into your application and enhance your prompts without updating your code. Best of all, it's 100% free!

## Installation

Install the package using pip:

```bash
pip install prompt-wrangler
```

## Environment Variables

Before you need to set environment variables.

If you want to use private prompts from your workspace you should set:

```txt
PROMPT_WRANGLER_API_KEY=<your_api_key>
```

If you want to use public prompts from the community you should set:

```txt
OPENAI_API_KEY=<open_ai_api_key>
```

> Note that if you set your `PROMPT_WRANGLER_API_KEY` you don't need to set `OPENAI_API_KEY` as it will be used as a fallback.

## Usage

```python
from prompt_wrangler import PromptWrangler

# Create a PromptWrangler instance
pw = PromptWrangler()

# Get a prompt
prompt_path = "my-workspace/my-prompt-slug"
prompt = prompt_wrangler.prompt(prompt_path)

# Run the prompt
args = {'input_text': 'some input'}
result = prompt.run(args=args)
prediction = result.prediction
```

## License

This project is licensed under the MIT License.

## Local Development

### Publish

Run. Username is exit38

```
./publish.sh
```
