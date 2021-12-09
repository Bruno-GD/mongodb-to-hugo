import logging

LOGGER = logging.getLogger(__name__)


def checkMongoURI(URI):
    if URI.find("srv") != -1:
        LOGGER.warning('Using URI with "srv" requires "pymongo[srv]" extension')
