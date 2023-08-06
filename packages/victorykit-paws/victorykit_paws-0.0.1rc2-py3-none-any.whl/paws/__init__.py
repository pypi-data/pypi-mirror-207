#!/usr/bin/env python3
"""Create and maintain AWS CLI profiles requiring MFA-authenticated STS sessions
with ease.
"""
from configparser import ConfigParser
from dataclasses import dataclass, field, asdict, fields
from os import environ
from pathlib import Path
import json
from sys import exit, stdout, stdin
from subprocess import check_output
from typing import Dict, Optional, TextIO, List, Tuple
from warnings import warn

from paws.helper.logging import get_default_logger
from paws.helper.dataclasses import sanitize, sanitize2

logger = get_default_logger(__name__)


ENVIRONMENT_MAP = {
    'aws_access_key_id': 'AWS_ACCESS_KEY_ID',
    'aws_secret_access_key': 'AWS_SECRET_ACCESS_KEY',
    'ca_bundle': 'AWS_CA_BUNDLE',
    'max_attempts': 'AWS_MAX_ATTEMPTS',
    'cli_pager': 'AWS_PAGER',
    'region': 'AWS_REGION',
    'output': 'AWS_OUTPUT',
    'retry_mode': 'AWS_RETRY_MODE',
    'role_arn': 'AWS_ROLE_ARN',
    'role_session_name': 'AWS_ROLE_SESSION_NAME',
    'aws_session_token': 'AWS_SESSION_TOKEN',
    'use_fips_endpoint': 'AWS_USE_FIPS_ENDPOINT',
    'web_identity_token_file': 'AWS_WEB_IDENTITY_TOKEN_FILE',
    'paws_virtual_mfa_device_arn': 'PAWS_VIRTUAL_MFA_DEVICE_ARN',
    'paws_session_expiration': 'PAWS_SESSION_EXPIRATION',
    'paws_session_source': 'PAWS_SESSION_SOURCE'
}


@dataclass
class Credential:

    #: AWS access key associated with an IAM account.
    aws_access_key_id: str

    #: This is essentially the "password" for the access key.
    aws_secret_access_key: str

    #: required if using temporary security credentials from AWS STS session
    aws_session_token: Optional[str] = ''


@dataclass
class Global:

    region: str

    #: specifies the output format to use
    output: str


@dataclass
class Reference:

    source_profile: str = ''


@dataclass
class General:

    #: name of assumed role in AWS STS session
    role_session_name: Optional[str] = None

    #: certificate bundle to use for HTTPS certificate validation
    ca_bundle: Optional[str] = None

    #: maximum retry attempts the AWS CLI retry handler uses
    max_attempts: Optional[str] = None

    #: pager program used for output
    cli_pager: Optional[str] = None

    #: ARN of AWS IAM role to assume
    role_arn: Optional[str] = None

    #: use AWS service endpoints supporting FIPS 140-2 compliant TLS transport
    use_fips_endpoint: Optional[str] = None

    #: OAuth 2.0 access token or OIDC token
    web_identity_token_file: Optional[str] = None

    #: OAuth 2.0 access token or OIDC token
    retry_mode: Optional[str] = None


@dataclass
class Paws:
    """
    """

    paws_virtual_mfa_device_arn: str = None


@dataclass
class PawsSession:
    """
    """

    paws_session_expiration: str = None

    paws_session_source: str = None


@dataclass
class PartialLongTermSharedCredentialsProfile(Credential):
    """
    """


@dataclass
class PartialLongTermConfigProfile(General, Reference, Paws, Global):
    """
    """


@dataclass
class Profile(General, Paws, PawsSession, Credential, Global):
    """
    """


@dataclass
class FilesystemEnvironment:
    """
    """

    AWS_CONFIG_FILE: Optional[str] = None

    AWS_SHARED_CREDENTIALS_FILE: Optional[str] = None

    AWS_PROFILE: Optional[str] = None

    AWS_DEFAULT_REGION: Optional[str] = None

    AWS_DEFAULT_OUTPUT: Optional[str] = None


@dataclass
class CredentialEnvironment:
    """
    """

    AWS_ACCESS_KEY_ID: str

    AWS_SECRET_ACCESS_KEY: str


@dataclass
class CredentialSupportEnvironment:
    """
    """

    AWS_ACCESS_KEY_ID: str = None

    AWS_SECRET_ACCESS_KEY: str = None


@dataclass
class GlobalEnvironment:

    AWS_REGION: str

    AWS_OUTPUT: str


@dataclass
class GlobalSupportEnvironment:

    AWS_REGION: str = None

    AWS_OUTPUT: str = None


@dataclass
class GeneralEnvironment:

    AWS_CA_BUNDLE: Optional[str] = None

    AWS_MAX_ATTEMPTS: Optional[str] = None

    AWS_PAGER: Optional[str] = None

    AWS_RETRY_MODE: Optional[str] = None

    AWS_ROLE_ARN: Optional[str] = None

    AWS_ROLE_SESSION_NAME: Optional[str] = None

    AWS_SESSION_TOKEN: Optional[str] = None

    AWS_USE_FIPS_ENDPOINT: Optional[str] = None

    AWS_WEB_IDENTITY_TOKEN_FILE: Optional[str] = None

    AWS_DEFAULT_REGION: Optional[str] = None

    AWS_DEFAULT_OUTPUT: Optional[str] = None

    PAWS_VIRTUAL_MFA_DEVICE_ARN: Optional[str] = None

    PAWS_SESSION_EXPIRATION: Optional[str] = None

    PAWS_SESSION_SOURCE: Optional[str] = None


@dataclass
class Environment(
    GeneralEnvironment,
    CredentialEnvironment,
    GlobalEnvironment
):
    """
    """


@dataclass
class StandardEnvironment(
    GeneralEnvironment,
    CredentialSupportEnvironment,
    GlobalSupportEnvironment
):
    """
    """


@dataclass
class FilesystemDump:

    profile_name: str

    config: dict

    config_file: str

    source_profile_name: str

    shared_credentials: dict

    shared_credentials_file: str


@dataclass
class FilesystemProfileQueryResult:

    #: the profile retrieved from a query
    profile: Profile

    #: the name of the profile
    profile_name: str


@dataclass
class Filesystem:

    config_path: Path

    config: ConfigParser

    shared_credentials: ConfigParser

    shared_credentials_path: Path


def get_filesystem(
    env: FilesystemEnvironment = FilesystemEnvironment()
) -> Filesystem:
    """
    """
    props = sanitize2(asdict(env))

    basepath = Path.home() / '.aws'

    config_file = props.get('AWS_CONFIG_FILE') or environ.get('AWS_CONFIG_FILE') or str(basepath / 'config')

    shared_credentials_file = props.get('AWS_SHARED_CREDENTIALS_FILE') or  environ.get('AWS_SHARED_CREDENTIALS_FILE') or str(basepath / 'credentials')

    config = ConfigParser()

    shared_credentials = ConfigParser()

    config.read(config_file)

    shared_credentials.read(shared_credentials_file)

    return Filesystem(
        config = config,
        shared_credentials = shared_credentials,
        config_path = config_file,
        shared_credentials_path = shared_credentials_file
    )


def get_profile_from_filesystem(
    env: FilesystemEnvironment = FilesystemEnvironment()
) -> Tuple[Profile, str]:
    """
    """
    fs = get_filesystem(env)

    props = asdict(env)

    profile = props.get('AWS_PROFILE') or environ.get('AWS_PROFILE') or'default'

    logger.debug(f'config file: {fs.config_path}')

    try:

        _proto = fs.config[f'profile {profile}' if profile != 'default' else profile]

    except KeyError as err:

        config_partial = None

        raise Exception(
            f'no section named \'{profile}\' in \'{fs.config_path}\''
        ) from err
    else:

        config_partial = PartialLongTermConfigProfile(**sanitize(
            _proto,
            PartialLongTermConfigProfile
        ))

    source_profile = profile

    proto = {}

    if config_partial and config_partial.source_profile:

        source_profile = config_partial.source_profile

        proto = {
            **proto,
            **asdict(config_partial),
        }

    logger.debug(f'shared credentials file: {fs.shared_credentials_path}')

    try:

        _proto = fs.shared_credentials[source_profile]

    except KeyError as err:

        shared_credentials_partial = None

        raise Exception(
            f'no section named \'{source_profile}\' in \'{shared_credentials_file}\''
        ) from err
    else:

        shared_credentials_partial = PartialLongTermSharedCredentialsProfile(**sanitize(
            _proto,
            PartialLongTermSharedCredentialsProfile
        ))

    proto = {
        **proto,
        **asdict(shared_credentials_partial)
    }

    region = props.get(
        'AWS_DEFAULT_REGION',
        environ.get('AWS_DEFAULT_REGION', '')
    )

    output = props.get(
        'AWS_DEFAULT_OUTPUT',
        environ.get('AWS_DEFAULT_OUTPUT', '')
    )

    if region:

        proto.set_default('region', region)

    if output:

        proto.set_default('output', output)

    return Profile(**sanitize(proto, Profile)), source_profile


def get_profile_from_stdin(
    env: StandardEnvironment = StandardEnvironment(),
    prompt: Optional[bool] = True,
    prefer_env: Optional[bool] = False,
    prefer_defaults: Optional[bool] = True,
    filter_names: List[str] = [],
    discrete=False,
    prompt_prefix: str = '',
    default_shared_credentials_profile = 'default'
) -> Tuple[Profile, str]:
    """

    :param env: 
    :param inp: s
    :param prompt: whether to treat input line-by-line (with defaults) or whole
    :param overwrite_defaults: 
    """
    props = asdict(env)

    config = ConfigParser()

    proto = {}

    shared_credentials_profile_name = None

    if not prompt:

        proto = sanitize(dict(config.read_string(stdin.read())), Profile)

        return Profile(**proto)

    prompt = f"{prompt_prefix}source_profile [{default_shared_credentials_profile}]: "

    if not prefer_env:

        shared_credentials_profile_name = input(prompt) or default_shared_credentials_profile

        if shared_credentials_profile_name != default_shared_credentials_profile:

            logger.info(
                'getting partial profile overrides from shared credential '
                f'\'{shared_credentials_profile_name}\''
            )

            fs = get_filesystem()

            partial_proto = dict(fs.shared_credentials).get(shared_credentials_profile_name) or {}

            if not partial_proto:

                logger.warning(
                    f'shared credential \'{shared_credentials_profile_name}\' '
                    'does not exist, applying no overrides'
                )

            overrides = sanitize(
                partial_proto,
                PartialLongTermSharedCredentialsProfile
            )

            for k, v in overrides.items():

                name = ENVIRONMENT_MAP[k]

                props[name] = v

    else:

        shared_credentials_profile_name = default_shared_credentials_profile

        if not discrete:

            print(prompt)

    for ini_name, env_name in sorted(ENVIRONMENT_MAP.items()):

        env_default = props.get(env_name)

        if env_default and ('secret' in ini_name or 'token' in ini_name):

            prompt_default = '*' * 16
        else:

            prompt_default = env_default

        prompt = f"{prompt_prefix}{ini_name} [%s]" % (
            prompt_default if prompt_default else ''
        )

        if filter_names and ini_name in filter_names and not (prefer_env and env_default):

            value = input(f"{prompt}: ")

            proto[ini_name] = value if value else env_default

            continue

        elif prefer_env and env_default:

            proto[ini_name] = env_default

            if not discrete:

                print(prompt)

            continue

        elif prefer_defaults and not env_default and hasattr(Profile, ini_name):

            proto[ini_name] = getattr(Profile, ini_name)

            if not discrete:

                print(prompt)

            continue

        value = input(f"{prompt}: ")

        proto[ini_name] = value if value else env_default

    return Profile(**sanitize2(proto)), shared_credentials_profile_name


def get_profile_from_environment(
    env: Environment
) -> Profile:
    """
    """

    names = [f.name for f in fields(env)]

    proto = {}

    reversed_map = {v:k for k,v in ENVIRONMENT_MAP.items()}

    for name in names:

        value = environ.get(name)

        if not value:

            continue

        proto[reversed_map[name]] = value

    return Profile(**proto)


def get_profile(
    env: FilesystemEnvironment = FilesystemEnvironment(),
    prompt: Optional[bool] = True,
    prefer_env: Optional[bool] = False,
    prefer_defaults: Optional[bool] = True,
    filter_names: List[str] = [],
    stdin: bool = False,
    discrete: bool = False,
    prompt_prefix: str = '',
) -> Tuple[Profile, str]:
    """

    :param env: 
    :param inp: s
    :param prompt: whether to treat input line-by-line (with defaults) or whole
    :param overwrite_defaults: 
    """

    source_profile_name = None

    try:

        if prefer_env:
            profile = get_profile_from_environment(
                Environment(**sanitize(dict(environ), Environment))
            )
        else:
            raise TypeError

        logger.info('using environment profile')
    except TypeError as err:

        try:

            profile, source_profile_name = get_profile_from_filesystem(env)
        except Exception as err:

            logger.warning(f'unable to get filesystem profile \'%s\': {err}' % (env.AWS_PROFILE if env.AWS_PROFILE else 'default'))

            profile = None
        else:

            logger.info('using filesystem profile \'%s\'' % (env.AWS_PROFILE if env.AWS_PROFILE else 'default'))

    finally:

        proto = asdict(profile) if profile else {}

    if profile:

        _env = StandardEnvironment(**{
            ENVIRONMENT_MAP[k]:v for k, v in asdict(profile).items() if k != 'source_profile'
        })
    else:

        _env = StandardEnvironment()

    if (prompt or stdin):

        logger.info(f'getting profile from stdin')

        _profile, source_profile_name = get_profile_from_stdin(
            _env,
            prompt=(not stdin and prompt),
            prefer_env=prefer_env,
            prefer_defaults=prefer_defaults,
            filter_names=filter_names,
            discrete=discrete,
            prompt_prefix = prompt_prefix,
            default_shared_credentials_profile = source_profile_name or 'default'
        )

        proto = asdict(_profile)

    return Profile(**sanitize2(proto)), source_profile_name


def new_session_profile(
    profile: Profile,
    token_code: Optional[str] = None,
    duration: int = 3000
) -> Profile:
    """create an MFA-authenticated session profile from a long-term profile

    :param profile: long-term AWS CLI profile
    :param tokenCode: Token code from virtual MFA device 
    """
    import botocore.session


    botocore_session = botocore.session.get_session();

    client = botocore_session.create_client(
        'sts',
        aws_access_key_id=profile.aws_access_key_id,
        aws_secret_access_key=profile.aws_secret_access_key,
        aws_session_token=profile.aws_session_token
    )

    request_proto = {
        'DurationSeconds': duration,
    }

    if token_code:

        logger.info('MFA-authentication')

        assert profile.paws_virtual_mfa_device_arn, 'virtual MFA device ARN specified'

        request_proto['SerialNumber'] = profile.paws_virtual_mfa_device_arn

        request_proto['TokenCode'] = token_code

    if profile.role_arn or profile.role_session_name:

        logger.info('AWS STS action: AssumeRole')

        assert profile.role_arn and profile.role_session_name, (
            'both `role_arn` and `role_session_name` must be specified'
        )

        request_proto = {
            **request_proto,
            **{
                'RoleArn': profile.role_arn,
                'RoleSessionName': profile.role_session_name,
            }
        } 

        response = client.assume_role(**request_proto)

        credential = response['Credentials']

        partial = {
            'aws_access_key_id': credential['AccessKeyId'],
            'aws_secret_access_key': credential['SecretAccessKey'],
            'aws_session_token': credential['SessionToken'],
            'paws_session_expiration': credential['Expiration'].isoformat(),
            'paws_virtual_mfa_device_arn': None,
            'role_arn': None,
            'role_session_name': None
        }

    else:

        logger.info('AWS STS action: GetSessionToken')

        response = client.get_session_token(**request_proto)

        credential = response['Credentials']

        partial = {
            'aws_access_key_id': credential['AccessKeyId'],
            'aws_secret_access_key': credential['SecretAccessKey'],
            'aws_session_token': credential['SessionToken'],
            'paws_session_expiration': credential['Expiration'].isoformat(),
            'paws_virtual_mfa_device_arn': None
        }

    return Profile(**sanitize2({
        **asdict(profile),
        **partial
    }))


def dump_profile_from_filesystem(
    profile: Profile,
    env: StandardEnvironment = None
) -> FilesystemDump:
    """
    """

    config_dump = {}

    shared_credentials_dump = {}

    if env:

        fs = get_filesystem(env)

        props = asdict(env)

        profile_name = props.get('AWS_PROFILE') or environ.get('AWS_PROFILE') or 'default'

        config_section_name = f'profile {profile_name}' if profile_name != 'default' else profile_name

        source_profile_name = dict(fs.config).get(config_section_name, {}).get('source_profile') or profile_name

        config_dump = dict(dict(fs.config).get(config_section_name, {}))

        shared_credentials_dump = dict(dict(fs.shared_credentials).get(source_profile_name, {}))

    for k, v in sanitize2(asdict(profile)).items():

        if not v:

            continue

        if k in [
            'aws_access_key_id',
            'aws_secret_access_key',
            'aws_session_token'
        ]:

            shared_credentials_dump[k] = v

        else:

            config_dump[k] = v

    return FilesystemDump(
        config = config_dump,
        shared_credentials = shared_credentials_dump,
        profile_name = profile_name,
        source_profile_name = source_profile_name,
        config_file = fs.config_path,
        shared_credentials_file = fs.shared_credentials_path
    )