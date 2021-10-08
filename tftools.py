#! /usr/local/bin/python3
"""
Simple wrapper tool for convert2tf and convert2rb!
"""
import sys
from termcolor import cprint

import convert2erb
import convert2tf


def main():
    print(" ".join(sys.argv))
    cprint(
        "\n================================ [tftools] ================================\n",
        "blue", attrs=["bold"]
    )
    if (".tf.erb" in " ".join(sys.argv)) and ".yaml" in " ".join(sys.argv):
        cprint('\nRunning - convert2tf\n', 'cyan')
        convert2tf.parse_user_args(sys.argv)
    elif ".tf" in " ".join(sys.argv):
        cprint('\nRunning - convert2erb\n', 'cyan')
        convert2erb.parse_user_args(sys.argv)
    else:
        print("Received no valid user inputs! Please check usage details @")
        cprint(
            "\n\thttps://github.com/msampathkumar/MagicModules-TerraformTools/tree/command_line_tool#usage\n",
            "cyan",
        )
    cprint(
        "\n================================ [tftools] ================================\n",
        "blue", attrs=["bold"]
    )


if __name__ == "__main__":
    main()