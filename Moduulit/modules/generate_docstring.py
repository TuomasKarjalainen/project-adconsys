def generate_docstring(arg1=1, arg2=2):
    """[Prints docstring template example]

    Args:
        arg1 ([type]): [description]
        arg2 ([type]): [description]

    Returns:
        [str]: [prints docstring template that can be modified and used to descripe other functions.]
    """

    return     print('''
    """[summary]

    Args:
        arg1 ([type]): [description]
        arg2 ([type]): [description]

    Returns:
        [type]: [description]
    """''')