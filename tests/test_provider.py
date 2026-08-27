"""Contract tests for the example provider definitions."""

from importlib.metadata import entry_points

from gptme.llm.models.types import ProviderPlugin

from gptme_provider_example import provider
from oauth_example import provider as oauth_provider


def test_installed_entry_point_loads_provider() -> None:
    matches = [
        entry_point
        for entry_point in entry_points(group="gptme.providers")
        if entry_point.name == "example"
    ]

    assert len(matches) == 1
    assert matches[0].load() is provider


def test_example_provider_models_are_fully_qualified() -> None:
    assert isinstance(provider, ProviderPlugin)
    assert len(provider.models) == 3
    assert all(model.model.startswith("example/") for model in provider.models)


def test_oauth_example_declares_custom_initialization() -> None:
    assert isinstance(oauth_provider, ProviderPlugin)
    assert oauth_provider.init is not None
    assert all(model.model.startswith("oauth-example/") for model in oauth_provider.models)
