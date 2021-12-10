from os import mkdir as createFolder
from os.path import join

INDEX_MD = """---
title: {name}
image: "img/sections/{name}.jpeg"
---

{description}
<!-- more -->"""

HEADER_MD = """---
name: {name}
location: {location}
price: {price}
capacity: {capacity}
---


"""

CONTENT_MD = """## {menuName}
* Primer plato
    #### {first}
* Segundo plato
    #### {second}
* Postre
    #### {desert}

"""


def populateContents(hugoDir: str, sections: list, elements: dict, *, insideContent: str = "") -> None:
    """
    Populate '.../content/*' folder with sections and
    elements
    """

    # precondition
    assert isinstance(sections, list)
    assert isinstance(elements, dict)

    # logic
    SECTION_NAME = "name"
    CONTENT_NAME = "name"
    CONTENT_MENU = "menu"

    for section in sections:
        sectionPath = join(hugoDir, "content", insideContent, section[SECTION_NAME])
        createFolder(sectionPath)
        # _index.md
        with open(join(sectionPath, '_index.md', 'w', encoding='utf8')) as f:
            f.write(INDEX_MD.format(**section))

        # *.md
        for content in elements[section[SECTION_NAME]]:
            contentFileName = content[CONTENT_NAME].strip().replace(" ", "_")
            with open(join(sectionPath, contentFileName + ".md"), "w") as f:
                f.write(HEADER_MD.format(**content))
                for menu in content[CONTENT_MENU]:
                    f.write(CONTENT_MD.format(**menu))
