from typing import List, Dict

import argunparse


def to_arg_unparse(
    argunparser_kwargs: Dict = None,
    command: str = None,
    sub_command: str = None,
    options: Dict = None,
    arguments: List = None,
) -> List[str]:
    """
    Usage:
    to_arg_unparse(command="cmd", sub_command="sub", options={'foo':True, 'bar':'baz}, args=['file.txt'])
    > cmd sub --foo --bar=baz file.txt
    """
    unparser = argunparse.ArgumentUnparser(**(argunparser_kwargs or {}))
    data = unparser.unparse_options_and_args(options, arguments, to_list=True)
    data = [command, sub_command] + data
    return list(filter(lambda x: x is not None, iter(data)))
