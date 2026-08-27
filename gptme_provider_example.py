"""
Minimal OpenAI-compatible provider example for gptme.

This demonstrates the simplest way to add a custom model provider to gptme.

Setup:
  1. Set your API key: export EXAMPLE_API_KEY="sk-..."
  2. Install this module: pip install -e .
  3. Run gptme: gptme --model example/gpt-4

The provider will be auto-discovered via entry points.
"""

from gptme.llm.models.types import ModelMeta, ProviderPlugin


# Define available models (metadata only, OpenAI API handles actual inference).
# Copy values from your provider's documentation.
# Note: model names must be fully qualified as "<provider>/<model>", and
# price_input/price_output are per 1M tokens (not per 1k).
EXAMPLE_MODELS = [
    ModelMeta(
        provider="unknown",
        model="example/gpt-4",
        context=128_000,
        price_input=30.0,
        price_output=60.0,
    ),
    ModelMeta(
        provider="unknown",
        model="example/gpt-3.5-turbo",
        context=16_385,
        price_input=0.5,
        price_output=1.5,
    ),
]

# Create the provider plugin instance.
# This is what gptme will discover and load.
provider = ProviderPlugin(
    name="example",
    api_key_env="EXAMPLE_API_KEY",
    base_url="https://api.example.com/v1",  # Replace with your provider's URL
    models=EXAMPLE_MODELS,
    # init=None,  # Custom auth not needed for OpenAI-compatible providers
)
