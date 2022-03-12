""" main module """


def hello_world(name: str) -> str:
    """
    Retuns hello name
    Args
    ----------
    name: string
        name to say hello
    Returns
    ----------
    text: string
        hello name text
    """

    text = f"hello {name}"
    print(text)
    return text
