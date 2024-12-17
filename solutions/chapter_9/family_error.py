class FamilyError(Exception):
    """
    Custom exception for Family class errors.
    """

    def __init__(self, message):
        super().__init__(message)
