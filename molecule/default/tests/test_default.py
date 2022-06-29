"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["unzip", "tar"])
def test_packages(host, pkg):
    """Test that the appropriate packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("d", ["/tools/cs2modrewrite"])
def test_directories(host, d):
    """Test that the expected directories were created and are not empty."""
    assert host.file(d).exists
    assert host.file(d).is_directory
    assert host.file(d).listdir()
    assert host.file(d).mode == 0o755


@pytest.mark.parametrize("f", ["/tools/cs2modrewrite/cs2modrewrite.py"])
def test_files(host, f):
    """Test that the expected files were created and are non-empty."""
    assert host.file(f).exists
    assert host.file(f).is_file
    assert host.file(f).content
