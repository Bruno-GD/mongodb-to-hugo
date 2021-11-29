
def generateSite(sections: list, elements: dict) -> None:
    """
    
    """

    # preconditions
    assert isinstance(sections, list)
    assert isinstance(elements, dict)

if __name__ == '__main__':
    # collect data from MongoDB
    from .utils.db.getDataFromDB import getDataFromDB
    sections, elements = getDataFromDB()

    # generate site with collected data
    generateSite(sections, elements)