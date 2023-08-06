#!/usr/bin/env python3
""""""
import sys
from pathlib import Path
from importlib import import_module
from enum import Enum
from os import environ
from dataclasses import asdict
import logging
import json

from paws.helper.logging import get_default_logger
from paws.cli import get_parser

logger = get_default_logger(__name__)

sys.path.insert(0, Path(__file__).parent.parent.name)
paws = import_module('paws')


def profile(
    argv,
    allow_session: bool = True
):
    """work with session profiles
    """

    try:

        profile, shared_credentials_profile_name = paws.get_profile(
            env = paws.FilesystemEnvironment(
                AWS_PROFILE=argv['name']
            ),
            prompt = False
        )

    except TypeError as err:

        logger.info(f'initializing new profile')

        profile = paws.Profile(
            **{k:'' for k in paws.ENVIRONMENT_MAP.keys()}
        )

        shared_credentials_profile_name = argv['name']

    source_profile_name = ''

    source_profile = None

    if allow_session and argv['from']:

        source_profile_name = argv['from']

    elif profile.paws_session_source:

        source_profile_name = profile.paws_session_source

    if allow_session and source_profile_name:

        source_profile, _ = paws.get_profile(
            paws.FilesystemEnvironment(
                AWS_PROFILE=source_profile_name
            ),
            prompt = True,
            prefer_defaults = (not argv['configure'] or (argv['configure'] and argv['quick'])),
            prefer_env = (not argv['configure']),
            discrete = True,
            filter_names = ['paws_virtual_mfa_device_arn'],
            stdin = argv['stdin'] and argv['configure'],
            prompt_prefix = '(from) '
        )

    if (allow_session and (argv['mfa_token_code'] or argv['force_session_renewal'])):

        _profile = paws.new_session_profile(
            source_profile,
            argv['mfa_token_code']
        )

        profile = paws.Profile(**paws.sanitize2({
            **asdict(_profile),
            **{
                'paws_session_source': argv['from'] if argv['from'] else profile.paws_session_source
            }
        }))

    profile, shared_credentials_profile_name = paws.get_profile_from_stdin(
        env = paws.StandardEnvironment(**{
            paws.ENVIRONMENT_MAP[k]:v for k, v in asdict(profile).items() if k != 'source_profile'
        }),
        prompt = True,
        prefer_defaults = (not argv['configure'] or (argv['configure'] and argv['quick'])),
        prefer_env = (not argv['configure']),
        discrete = True,
        default_shared_credentials_profile = shared_credentials_profile_name
    )

    dump = paws.dump_profile_from_filesystem(
        profile,
        paws.FilesystemEnvironment(
            AWS_PROFILE = argv['name']
        )
    )

    full = {
        **paws.sanitize(dump.config, paws.Profile),
        **paws.sanitize(dump.shared_credentials, paws.Profile)
    }

    output = {
        'ini': lambda: '\n'.join(f"{k}={v}" for k, v in full.items()),
        'posix-environ': lambda: '\n'.join(f"export {paws.ENVIRONMENT_MAP[k]}='{v}'" for k, v in full.items()),
        'pwsh-environ': lambda: '\n'.join(f"$Env:{paws.ENVIRONMENT_MAP[k]} = '{v}'" for k, v in full.items()),
        'json': lambda: json.dumps(full, sort_keys=True)
    }[argv['output_format']]()

    print(output)

    fs = paws.get_filesystem()

    if argv['write_fs_config']:

        section_name = f'profile {argv["name"]}'

        fs.config.setdefault(section_name, {})

        for k, v in paws.sanitize(dump.config, paws.Profile).items():

            fs.config[section_name][k] = v

        if shared_credentials_profile_name == 'default':

            try:

                del fs.config[section_name]['source_profile']

            except KeyError:

                logger.debug('skipping removal of source profile (does not exist)')

                pass

        elif shared_credentials_profile_name:

            fs.config[section_name]['source_profile'] = shared_credentials_profile_name

        with open(argv['write_fs_config'], 'w') as fh:

            fs.config.write(fh)

    if argv['write_fs_shared_credentials']:

        section_name = shared_credentials_profile_name

        fs.shared_credentials.setdefault(section_name, {})

        for k, v in paws.sanitize(dump.shared_credentials, paws.Profile).items():

            fs.shared_credentials[section_name][k] = v

        with open(argv['write_fs_shared_credentials'], 'w') as fh:

            fs.shared_credentials.write(fh)

    return


def long_term_profile(argv):
    """AWS Long-term credential (AKIA) CLI profile management
    """
    return profile(argv, allow_session=False)


def session_profile(argv):
    """AWS Session credential (ASIA) CLI profile management
    """
    return profile(argv, allow_session=True)


def get_fancy_parser():

    return get_parser(
        doc = __doc__,
        session_profile_doc = session_profile.__doc__,
        long_term_profile_doc = long_term_profile.__doc__
    )


def main():
    """
    """
    argv = vars(get_fancy_parser().parse_args())

    paws.logger.setLevel(getattr(logging, argv['log_level']))

    logger.setLevel(getattr(logging, argv['log_level']))

    sys.exit({
        'long-term-profile': long_term_profile,
        'session-profile': session_profile,
    }[argv['command']](argv))


if __name__ == '__main__':

    main()
