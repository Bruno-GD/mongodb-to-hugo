from shutil import which as checkPath

def isHugoAvailable() -> bool:
    """
    Check wether Hugo is installed on shell or not
    """
    return checkPath('hugo') != None