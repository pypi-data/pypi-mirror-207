"""Test all YAML plugins."""
import pytest
import yaml
from importlib import resources

from geoips.interfaces.base import YamlPluginValidator


validator = YamlPluginValidator()


def yield_plugins():
    """Yield plugins."""
    fpath = resources.files("geoips_clavrx") / "plugins/yaml"
    plugin_files = fpath.rglob("*.yaml")
    for pf in plugin_files:
        yield yaml.safe_load(open(pf, "r"))


@pytest.mark.parametrize("plugin", yield_plugins())
def test_is_plugin_valid(plugin):
    """Test if plugin is valid."""
    validator.validate(plugin)
