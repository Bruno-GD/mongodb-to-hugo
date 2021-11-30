from os import mkdir as createFolder
from os.path import join

DEFAULT_MD = \
"""---
title: %s
---"""

def populateContents(hugoDir: str, sections: list, elements: dict) -> None:
    """
    Populate '.../content/*' folder with sections and
    elements
    """

    # precondition
    assert isinstance(sections, list)
    assert isinstance(elements, dict)

    # logic
    for section in sections:
        sectionPath = join(hugoDir, 'content', section)
        createFolder(sectionPath)
        with open(join(sectionPath, 'index.md'), 'w') as f:
            f.write(DEFAULT_MD % section)
