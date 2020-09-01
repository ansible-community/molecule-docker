"""Functional tests."""
import os

import pytest
import sh
from molecule import logger
from molecule.test.conftest import change_dir_to, run_command

LOG = logger.get_logger(__name__)


# @pytest.mark.xfail(reason="need to fix template path")
def test_command_init_scenario(temp_dir, DRIVER):
    """Verify that init scenario works."""
    role_directory = os.path.join(temp_dir.strpath, "test-init")
    options = {}
    cmd = sh.molecule.bake("init", "role", "test-init", **options)
    run_command(cmd)

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")
        options = {"role_name": "test-init", "driver-name": DRIVER}
        cmd = sh.molecule.bake("init", "scenario", "test-scenario", **options)
        run_command(cmd)

        assert os.path.isdir(scenario_directory)

        cmd = sh.molecule.bake("--debug", "test", "-s", "test-scenario")
        run_command(cmd)
