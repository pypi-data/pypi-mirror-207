from dotenv import load_dotenv

load_dotenv()

from prompt_wrangler import PromptWrangler, PromptResponse


def test_private_prompt():  # Use the fixtures in the function arguments
    pw = PromptWrangler()
    prompt = pw.prompt("ms-test/test-prompt")

    result = prompt.run(args={"input": "some input"})

    assert isinstance(result, PromptResponse)

    # Check for Total Time
    total_time = result
    assert total_time

    # Check for Links
    links = result.links
    assert links

    # Assert prediction exists
    assert result.prediction


def test_public_prompt_json():  # Use the fixtures in the function arguments
    pw = PromptWrangler()
    prompt = pw.prompt("test-workspace/test-json")

    result = prompt.run(args={"input": "animal"})

    assert isinstance(result, PromptResponse)

    # Get prediction
    prediction = result.prediction

    # Get Animal
    animal = prediction.get("animal")
    # Assert prediction exists
    assert animal
