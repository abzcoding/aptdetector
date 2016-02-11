"""sample"""


class FileParsingException(Exception):
    """sample"""

    def __init__(self, errorArgs):
        """sample"""
        Exception.__init__(self,
                           "File Parsing Exception {0}".format(errorArgs))
