"""Functional tests."""
import os
import subprocess

import pytest
from molecule import logger, util
from molecule.test.conftest import change_dir_to
from molecule.util import run_command

LOG = logger.get_logger(__name__)


def format_result(result: subprocess.CompletedProcess):
    """Return friendly representation of completed process run."""
    return (
        f"RC: {result.returncode}\n"
        + f"STDOUT: {result.stdout}\n"
        + f"STDERR: {result.stderr}"
    )


def test_command_init_and_test_scenario(temp_dir, DRIVER):
    """Verify that init scenario works."""
    role_directory = os.path.join(temp_dir.strpath, "test_init")
    cmd = ["molecule", "init", "role", "test_init"]
    result = run_command(cmd)
    assert result.returncode == 0

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")
        options = {"role-name": "test_init", "driver-name": DRIVER}
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


def test_command_static_scenario() -> None:
    """Validate that the scenario we included with code still works."""
    cmd = ["molecule", "test"]

    result = run_command(cmd)
    assert result.returncode == 0
