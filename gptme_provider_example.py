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
        name="gpt-4",
        context_window=128_000,
        cost_per_1k_input=0.03,
        cost_per_1k_output=0.06,
    ),
    ModelMeta(
        name="gpt-3.5-turbo",
        context_window=16_385,
        cost_per_1k_input=0.50e-3,
        cost_per_1k_output=1.50e-3,
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
