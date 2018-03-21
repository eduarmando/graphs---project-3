#!/usr/bin/env python3
# coding:utf-8

import argparse
# from time import time
from logger.messages import status
# from logger.messages import error
# from logger.messages import verbose
from logger import messages
# from graphs import messages
from graphs.graphs import procesar1
from graphs.graphs import procesar2

__header__ = """
                              -`
              ...            .o+`
           .+++s+   .h`.    `ooo/
          `+++%++  .h+++   `+oooo:
          +++o+++ .hhs++. `+oooooo:
          +s%%so%.hohhoo"  "oooooo+:
          `+ooohs+h+sh++`/:  ++oooo+:
           hh+o+hoso+h+`/++++.+++++++:
            `+h+++h.+ `/++++++++++++++:
                     `/+++ooooooooooooo/`
                    ./ooosssso++osssssso+`
                   .oossssso-````/osssss::`
                  -osssssso.      :ssss``to.
                 :osssssss/  Mike  osssl   +
                /ossssssss/   8a   +sssslb
              `/ossssso+/:-        -:/+ossss".-
             `+sso+:-`                 `.-/+oso:
            `++:.                           `-/+/
            .`                                 `/
"""

__version__ = "0.1.1"


def __parse_arguments():
    """ Function to parse CLI args
    :returns: object with the CLI arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose messages",
        required=False,
        dest="verbose",
        action="store_true")
    parser.add_argument(
        "-l",
        "--logger",
        help="Enable logger",
        required=False,
        dest="logger",
        action="store_true")
    parser.add_argument(
        "-q",
        "--quiet",
        help="Silence all stout output",
        required=False,
        dest="quiet",
        action="store_true")
    parser.add_argument(
        "-t",
        "--txt",
        help="Text file with the initial registers",
        required=False,
        type=str,
        dest="txt")
    parser.add_argument(
        "--version",
        help="Shows the version",
        required=False,
        dest="version",
        action="store_true")

    cli_args = parser.parse_args()

    return cli_args


def print_menu():
    print('1. 20 Ciudades')
    print('2. 100 Ciudades')
    print('3. 150 Ciudades')
    print('4. 200 Ciudades')
    print('5. Salir\n')


def main():
    """Main CLI function
    :returns: TODO

    """
    global debug_mode
    global start_time

    cli_args = __parse_arguments()

    if cli_args.version:
        status("Current version {0}".format(__version__))
        return 0

    messages.debug_mode = cli_args.verbose
    messages.quiet = cli_args.quiet
    messages.logger = cli_args.logger

    menu_choice = 0
    print_menu()
    while menu_choice != 5:
        menu_choice = int(input("Ingresa un numero (1-5): "))
        if menu_choice == 1:
            procesar1()
        elif menu_choice == 2:
            procesar2('samples/kroA100.txt')
        elif menu_choice == 3:
            procesar2('samples/kroA150.txt')
        elif menu_choice == 4:
            procesar2('samples/kroA200.txt')
        elif menu_choice != 5:
            print_menu()


if __name__ == "__main__":
    main()
else:
    raise Exception("Main file is just an executable, not a module")
