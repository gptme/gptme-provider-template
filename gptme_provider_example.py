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
EXAMPLE_MODELS = [
    ModelMeta(
        provider="unknown",
        model="example/large",
        context=128_000,
        max_output=16_384,
        price_input=3.00,
        price_output=15.00,
        supports_vision=True,
    ),
    ModelMeta(
        provider="unknown",
        model="example/balanced",
        context=64_000,
        max_output=8_192,
        price_input=1.00,
        price_output=5.00,
    ),
    ModelMeta(
        provider="unknown",
        model="example/fast",
        context=16_384,
        max_output=4_096,
        price_input=0.10,
        price_output=0.40,
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
