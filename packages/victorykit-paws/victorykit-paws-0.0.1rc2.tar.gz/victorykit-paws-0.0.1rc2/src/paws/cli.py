#!/usr/bin/env python3
""""""
from pathlib import Path
from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
    RawDescriptionHelpFormatter
)
from os import environ

import paws
from paws.helper.dataclasses import sanitize, sanitize2


class ArgparseFormatter(ArgumentDefaultsHelpFormatter, RawDescriptionHelpFormatter):
    """A formatter class for showing default values and not inserting new line
       when showing the help text header
    """


def get_parser(
    doc: str = '',
    session_profile_doc: str = '',
    long_term_profile_doc: str = ''
):
    """
    """

    env = [
        *[f"{k}={v}" for k, v in sanitize(dict(environ), paws.StandardEnvironment).items()],
        *[f"{k}={v}" for k, v in sanitize(dict(environ), paws.FilesystemEnvironment).items()]
    ]

    epilog = "detected environment configuration:\n  " + "\n  ".join(env) if env else ''

    parser = ArgumentParser(
        prog=Path(__file__).parent.name.replace('_', '-'),
        description=doc,
        epilog = epilog,
        formatter_class = ArgparseFormatter,
    )

    subparsers = parser.add_subparsers(help='command', dest="command",
                                       required=True)

    session_profile_parser = get_session_profile_subparser(
        subparsers,
        parser_args = ['session-profile'],
        parser_kwargs = {
            'description': session_profile_doc,
            'formatter_class': ArgparseFormatter,
            'epilog': epilog,
            'description': session_profile_doc,
            'help': (session_profile_doc.split('\n') or [''])[0]
        }
    )

    long_term_profile_parser = get_long_term_profile_subparser(
        subparsers,
        parser_args = ['long-term-profile'],
        parser_kwargs = {
            'description': long_term_profile_doc,
            'formatter_class': ArgparseFormatter,
            'epilog': epilog,
            'description': long_term_profile_doc,
            'help': (long_term_profile_doc.split('\n') or [''])[0]
        }
    )

    return parser


def get_profile_subparser(
    subparsers,
    parser_args: list = [],
    parser_kwargs: dict = {},
    allow_session: bool = True
):
    """
    """

    profile_parser = subparsers.add_parser(*parser_args, **parser_kwargs)

    profile_parser.add_argument('name',
        help="name of (filesystem) profile",
        nargs="?",
        default='default'
    )

    if allow_session:

        profile_parser.add_argument('--from', '-s',
            help="name of a long-term profile (or session profile) to create (or update) this session profile from",
            metavar="PROFILE",
            default=None
        )

        profile_parser.add_argument('--mfa-token-code', '-a',
            help="token code of `--from` virtual MFA device to authenticate with",
            metavar="CODE",
            default=None
        )

        profile_parser.add_argument('--force-session-renewal', '-f',
            help="force a new session, regardless of whether the configuration is sufficient",
            action="store_true",
            default=False
        )

    profile_parser.add_argument('--output-format', '-d',
        help="output format for STDOUT",
        choices=['pwsh-environ', 'posix-environ', 'json', 'ini'],
        default='ini'
    )

    profile_parser.add_argument('--configure', '-c',
        help="adjust session profile interactively before writing output",
        action="store_true",
        default=False
    )

    profile_parser.add_argument('--write-fs-config', '-m',
        help="write config partials output to a file",
        metavar="FILE",
        default=None
    )

    profile_parser.add_argument('--write-fs-shared-credentials', '-n',
        help="write shared credentials partials output to a file",
        metavar="FILE",
        default=None
    )

    profile_parser.add_argument('--log-level', '-l',
        help="set log level",
        choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR'
    )

    profile_parser.add_argument('--quick', '-q',
        help="skip prompts for defaults and optional properties",
        action="store_true",
        default=False
    )

    profile_parser.add_argument('--stdin', '-i',
        help="read from STDIN whole (as opposed to interactive line-by-line prompt), combine with `--configure`",
        action="store_true",
        default=False
    )

    return profile_parser


def get_long_term_profile_subparser(
    subparsers,
    parser_args: list = [],
    parser_kwargs: dict = {},
):
    """
    """
    return get_profile_subparser(
        subparsers,
        allow_session=False,
        parser_args = parser_args,
        parser_kwargs = parser_kwargs
    )


def get_session_profile_subparser(
    subparsers,
    parser_args: list = [],
    parser_kwargs: dict = {},
):
    """
    """
    return get_profile_subparser(
        subparsers,
        allow_session=True,
        parser_args = parser_args,
        parser_kwargs = parser_kwargs
    )