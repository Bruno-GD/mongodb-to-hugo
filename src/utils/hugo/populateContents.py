from os import mkdir as createFolder
from os.path import join

FORMATABLE_MD = \
"""---
name: {name}
location: {location}
price: {price}
capacity: {capacity}
---

# Menú
"""

MENU_MD = \
"""## {menuName}
1. {first}
2. {second}
3. {desert}
"""

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
        contents = list(elements[section].find({}))
        for content in contents:
            with open(join(sectionPath, content['name'] + '.md'), 'w') as f:
                f.write(FORMATABLE_MD.format(**content))
                for menu in content['menu']:
                    f.write(MENU_MD.format(**menu))