import httpretty
import pytest
from prompt_wrangler import PromptWrangler, PromptResponse
import os


@pytest.fixture
def prompt_path():
    return "composer-ai/reason-next-web-command"


@pytest.fixture
def prompt_wrangler():
    # Set Prompt Wrangler API Key environment variable

    return PromptWrangler()


@httpretty.activate
def test_run_prompt(
    prompt_wrangler, prompt_path
):  # Use the fixtures in the function arguments
    httpretty.register_uri(
        httpretty.POST,
        f"https://prompt-wrangler.com/api/predict/{prompt_path}",
        body='{"prediction": "sample_prediction"}',
        content_type="application/json",
        status=200,
    )

    prompt = prompt_wrangler.prompt(prompt_path)  # Use the 'prompt_wrangler' fixture
    result = prompt.run(args={"input_text": "some input"})

    assert isinstance(result, PromptResponse)
    assert result.prediction == "sample_prediction"
