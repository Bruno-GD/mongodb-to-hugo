from src.utils.hugo.checkFolderStructure import isFolderStructure
from os import getcwd
from os.path import join
# pytest
import pytest
from logging import getLogger as gL
LOGGER = gL(__name__)

@pytest.mark.folder_structure
def test_folder_structure():
    LOGGER.info('checking folder structure')
    assert isFolderStructure(join(getcwd(), 'content')) == True