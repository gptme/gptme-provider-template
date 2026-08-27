# gptme Provider Template

A minimal example of how to create a custom model provider plugin for gptme.

This template shows the **absolute minimum** needed to add a new OpenAI-compatible provider to gptme. No custom auth, no complex setup — just three files.

## What's Included

- `gptme_provider_example.py` — The provider plugin (entry point registration happens here)
- `pyproject.toml` — Package metadata + entry point configuration
- `README.md` — This file

## Setup (5 minutes)

### 1. Set Your API Key

```bash
export EXAMPLE_API_KEY="your-api-key-here"
```

### 2. Install the Template

From this directory:

```bash
pip install -e .
```

Or, if using `uv`:

```bash
uv pip install -e .
```

### 3. Verify Installation

```bash
gptme models | grep example
```

You should see:
```
example/gpt-4
example/gpt-3.5-turbo
```

### 4. Use It

```bash
gptme --model example/gpt-4
```

## Customization

Edit `gptme_provider_example.py`:

1. **Change the provider name**: Replace `"example"` with your provider's name (e.g., `"groq"`, `"anthropic-custom"`)
2. **Update the API key env var**: Replace `"EXAMPLE_API_KEY"` with your provider's convention (e.g., `"GROQ_API_KEY"`)
3. **Update the base URL**: Replace `"https://api.example.com/v1"` with your provider's actual endpoint
4. **Add your models**: Copy model names and metadata from your provider's documentation

That's it. No other changes needed for OpenAI-compatible providers.

## Advanced: Custom Auth (OAuth)

See `oauth_example.py` in this directory for a complete working example.

If your provider requires OAuth or custom authentication:

1. Define an `init()` callback that handles authentication:

```python
def oauth_setup_flow(config):
    """Custom OAuth setup called during gptme startup."""
    provider_name = "my_provider"

    # Check if already authenticated
    if provider_name in config.user.providers:
        return

    # Perform OAuth flow:
    # - Build authorize URL
    # - Launch browser
    # - Catch callback token
    # - Store in config.user.providers[provider_name]
```

2. Pass it to `ProviderPlugin`:

```python
provider = ProviderPlugin(
    name="my_provider",
    api_key_env="MY_PROVIDER_API_KEY",  # Fallback for env var
    base_url="https://api.myprovider.com/v1",
    models=MY_MODELS,
    init=oauth_setup_flow,  # ← Called once per session
)
```

3. Reference implementations in gptme source:
   - `gptme/llm/llm_openrouter_subscription.py` — OAuth → API key + browser flow
   - `gptme/llm/llm_grok_subscription.py` — Same pattern for Grok

## How It Works

When gptme starts, it:

1. Discovers all installed providers via entry points (`gptme.plugins`)
2. Loads each provider's `ProviderPlugin` instance
3. Calls the `init()` callback (if provided) for setup
4. Merges models into the global model catalog
5. Routes requests to the correct `base_url` based on the model's provider prefix

## Entry Point Registration

In `pyproject.toml`:

```toml
[project.entry-points."gptme.plugins"]
example = "gptme_provider_example:provider"
```

This tells Python (and gptme) where to find the provider plugin. The `provider` is the `ProviderPlugin` instance you create in `gptme_provider_example.py`.

## Testing

To test locally without publishing:

```bash
# From the template directory:
pip install -e .

# Verify gptme sees your provider:
gptme models | grep your-provider

# Try a request:
gptme --model your-provider/model-name "Hello"
```

## Publishing to PyPI

Once you're ready to share your provider:

```bash
python -m build
twine upload dist/*
```

Then users can install it with:

```bash
pip install gptme-provider-yourname
```

And use it immediately:

```bash
export YOUR_PROVIDER_API_KEY="..."
gptme --model yourprovider/modelname
```

## Support

For questions or issues:

- gptme documentation: https://docs.gptme.org
- gptme repository: https://github.com/gptme/gptme
- Provider interface: See `gptme/llm/models/types.py:ProviderPlugin`

---

**Last updated**: 2026-08-16
