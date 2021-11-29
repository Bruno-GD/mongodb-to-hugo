from src.utils.hugo.createHugoStructure import createHugoStructure
from os.path import join
from os import getcwd
# pytest
import pytest
from logging import getLogger as gL
LOGGER = gL(__name__)

@pytest.mark.create_hugo_structure
def test_create_structure():
    hugoFolder = join(getcwd(), 'content')
    LOGGER.info('create structure, no force')
    createHugoStructure(hugoFolder, ['section_one', 'section_two'])

@pytest.mark.create_hugo_structure
def test_create_structure_force():
    hugoFolder = join(getcwd(), 'content')
    LOGGER.info('create structure, but forced')
    createHugoStructure(hugoFolder, ['section_one', 'section_two'], force=True)
