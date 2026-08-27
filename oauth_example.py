"""
Advanced OAuth provider example for gptme.

This demonstrates how to add a custom authentication flow (e.g., OAuth) to a
provider plugin. Unlike the simple example, this requires user interaction
during setup but provides better security and long-term credential management.

Example use case: Aurelo, a provider that uses OAuth instead of static API keys.

Setup:
  1. Install this module: pip install -e .
  2. Run gptme: gptme --model oauth-example/default
     (First run launches a browser for OAuth login)
  3. Subsequent runs use the stored credentials automatically
"""

from gptme.llm.models.types import ModelMeta, ProviderPlugin


OAUTH_MODELS = [
    ModelMeta(
        name="default",
        context_window=128_000,
        cost_per_1k_input=0.01,
        cost_per_1k_output=0.02,
    ),
    ModelMeta(
        name="fast",
        context_window=16_385,
        cost_per_1k_input=0.001,
        cost_per_1k_output=0.002,
    ),
]


def oauth_setup_flow(config):
    """
    Custom authentication flow using OAuth.

    This function is called once per gptme session during `init()`.
    It should:
      1. Check if the user has already authenticated
      2. If not, launch a browser for OAuth login
      3. Exchange the authorization code for an API key
      4. Store the key in config.user.providers[provider_name]
    """
    provider_name = "oauth-example"

    # Check if we already have a stored credential
    if not hasattr(config.user, "providers"):
        config.user.providers = {}

    if provider_name in config.user.providers:
        # Already authenticated, nothing to do
        return

    # TODO: Implement real OAuth flow here
    # This is a placeholder showing the structure:
    #
    # 1. Generate a random state token (CSRF protection)
    # 2. Build OAuth authorize URL
    # 3. Launch browser: webbrowser.open(auth_url)
    # 4. Spin up a local callback server to catch the authorization code
    # 5. Exchange code for token using your provider's token endpoint
    # 6. Store the token in config.user.providers[provider_name]
    #
    # Real implementation example patterns:
    # - gptme/llm/llm_openrouter_subscription.py (OAuth to get API key)
    # - gptme/llm/llm_grok_subscription.py (OAuth to get API key)

    print(f"[gptme] First-time setup for {provider_name}:")
    print("  1. Visit: https://oauth.myprovider.com/authorize")
    print("  2. Approve gptme access")
    print("  3. The token will be saved to your gptme config")

    # For demo: placeholder token (DO NOT use in production)
    config.user.providers[provider_name] = "oauth_token_placeholder"
    print("[gptme] (Demo mode: using placeholder token)")


# Create the provider plugin instance.
provider = ProviderPlugin(
    name="oauth-example",
    api_key_env="OAUTH_EXAMPLE_TOKEN",  # Environment variable as a fallback
    base_url="https://api.myprovider.com/v1",  # Your provider's endpoint
    models=OAUTH_MODELS,
    init=oauth_setup_flow,  # ← This is the key difference from simple example
)
