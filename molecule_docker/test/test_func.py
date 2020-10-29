"""Functional tests."""
import os
import subprocess

import pytest
from molecule import logger, util
from molecule.test.conftest import change_dir_to
from molecule.util import run_command

import molecule_docker

LOG = logger.get_logger(__name__)


def format_result(result: subprocess.CompletedProcess):
    """Return friendly representation of completed process run."""
    return (
        f"RC: {result.returncode}\n"
        + f"STDOUT: {result.stdout}\n"
        + f"STDERR: {result.stderr}"
    )


# @pytest.mark.xfail(reason="need to fix template path")
def test_command_init_scenario(temp_dir, DRIVER):
    """Verify that init scenario works."""
    role_directory = os.path.join(temp_dir.strpath, "test-init")
    cmd = ["molecule", "init", "role", "test-init"]
    result = run_command(cmd)
    assert result.returncode == 0

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")
        options = {"role_name": "test-init", "driver-name": DRIVER}
        cmd = [
            "molecule",
            "init",
            "scenario",
            "test-scenario",
            *util.dict2args(options),
        ]
        result = run_command(cmd)
        assert result.returncode == 0

        assert os.path.isdir(scenario_directory)

        cmd = ["molecule", "--debug", "test", "-s", "test-scenario"]
        result = run_command(cmd)
        assert result.returncode == 0


def test_dockerfile():
    """Verify that our embedded dockerfile can be build."""
    result = subprocess.run(
        ["ansible-playbook", "--version"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
        shell=False,
        universal_newlines=True,
    )
    assert result.returncode == 0, result
    assert "ansible-playbook" in result.stdout

    module_path = os.path.dirname(molecule_docker.__file__)
    assert os.path.isdir(module_path)
    env = os.environ.copy()
    env["ANSIBLE_FORCE_COLOR"] = "0"
    result = subprocess.run(
        ["ansible-playbook", "-i", "localhost,", "playbooks/validate-dockerfile.yml"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
        shell=False,
        cwd=module_path,
        universal_newlines=True,
        env=env,
    )
    assert result.returncode == 0, format_result(result)
    # , result
