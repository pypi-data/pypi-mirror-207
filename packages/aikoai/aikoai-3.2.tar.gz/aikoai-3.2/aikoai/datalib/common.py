INSTRUCTIONS = """

AikoAI error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install aikoai[datalib]

"""

NUMPY_INSTRUCTIONS = INSTRUCTIONS.format(library="numpy")


class MissingDependencyError(Exception):
    pass
