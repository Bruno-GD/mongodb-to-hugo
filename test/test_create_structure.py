from src.utils.hugo.createHugoStructure import createHugoStructure
from src.utils.hugo.hugoCommands import startHugoSite
from os.path import join
from os import getcwd
# pytest
import pytest
from logging import getLogger as gL

LOGGER = gL(__name__)

@pytest.mark.create_hugo_structure
def test_create_structure():
    hugoFolder = join(getcwd(), 'site')
    LOGGER.info('create structure, no force')
    createHugoStructure(hugoFolder, ['section_one', 'section_two'])

@pytest.mark.create_hugo_structure
def test_create_structure_force():
    hugoFolder = join(getcwd(), 'site')
    LOGGER.info('create structure, but forced')
    createHugoStructure(hugoFolder, ['section_one', 'section_two'], force=True)

@pytest.mark.run_hugo_command
def test_create_structure_with_hugo():
    hugoFolder = join(getcwd(), 'site')
    LOGGER.info('create structure with Hugo command')
    startHugoSite(hugoFolder)
