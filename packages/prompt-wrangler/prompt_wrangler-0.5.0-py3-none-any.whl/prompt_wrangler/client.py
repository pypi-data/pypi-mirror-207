import requests
from typing import Any, Dict, Optional
import os
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


class APIException(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.reason = response.reason
        self.text = response.text
        super().__init__(
            f"Status code: {self.status_code}, Reason: {self.reason}, Response body: {self.text}"
        )


class APIException5xx(APIException):
    """Exception raised for 5xx status codes."""


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(APIException5xx),
)
def make_request(url, method="GET", headers=None, params=None, data=None):
    if method.upper() == "GET":
        response = requests.get(url, headers=headers, params=params)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, params=params, json=data)
    else:
        raise ValueError(f"Unsupported method: {method}")

    if response.status_code == 200:
        result = response.json()
        return PromptResponse(result)
    else:
        # Print response details
        print(
            f"Status code: {response.status_code}, Reason: {response.reason}, Response body: {response.text}"
        )

        # Raise custom exception with response details
        if 500 <= response.status_code < 600:
            raise APIException5xx(response)
        else:
            raise APIException(response)


class PromptWrangler:
    """Prompt Wrangler client."""

    def __init__(self, base_url: str = "https://prompt-wrangler.com/api") -> None:
        """
        Initialize the PromptWrangler client.

        :param workspace: The workspace identifier.
        """

        self.base_url = base_url

        # Confirm that either PROMPT_WRANGLER_API_KEY exists or OPENAI_API_KEY exists
        self.prompt_wrangler_api_key = os.getenv("PROMPT_WRANGLER_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        # Print env
        if self.prompt_wrangler_api_key is None and self.openai_api_key is None:
            raise Exception(
                "Prompt Wrangler API key not found. Please set environment variable PROMPT_WRANGLER_API_KEY or OPENAI_API_KEY. Make sure the environment is loaded."
            )

    def prompt(self, prompt_path: str) -> "PromptWranglerPrompt":
        """
        Add a prompt to the PromptWrangler client.

        :param prompt_path: The page to the prompt - workspace/prompt-slug.
        :return: A PromptWranglerPrompt instance.
        """
        return PromptWranglerPrompt(self, prompt_path)


class PromptWranglerPrompt:
    def __init__(self, prompt_wrangler: PromptWrangler, prompt_path: str) -> None:
        """
        Initialize a PromptWranglerPrompt.

        :param prompt_wrangler: The PromptWrangler client.
        :param prompt_slug: The prompt slug.
        """
        self.prompt_wrangler = prompt_wrangler
        self.prompt_path = prompt_path

    def run(self, args: Optional[Dict[str, Any]] = None) -> "PromptResponse":
        """
        Run the prompt and return a PromptResponse object.

        :param args: Optional dictionary of arguments to be passed to the API.
        :return: A PromptResponse instance.
        """
        headers = {
            "Content-Type": "application/json",
        }

        if self.prompt_wrangler.prompt_wrangler_api_key:
            headers["x-api-key"] = self.prompt_wrangler.prompt_wrangler_api_key

        if self.prompt_wrangler.openai_api_key:
            headers["x-openai-api-key"] = self.prompt_wrangler.openai_api_key

        url = f"{self.prompt_wrangler.base_url}/predict/{self.prompt_path}"
        payload = {"args": args} if args else {}
        response = make_request(url, method="POST", headers=headers, data=payload)
        return response


class PromptResponse:
    def __init__(self, data: Dict[str, Any]) -> None:
        """
        Initialize a PromptResponse object.
        :param data: The response data containing prediction and other fields.
        """
        self.prediction = data["prediction"]
        self.total_time = data.get("totalTime", None)
        self.links = data.get("links", None)

    def __repr__(self) -> str:
        return f"PromptResponse(prediction={self.prediction}, totalTime={self.total_time}, links={self.links})"
