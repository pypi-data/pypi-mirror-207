
This program is a non-destructive command-line utility for maintaining local 
AWS CLI profiles of AWS IAM entities for AWS API authentication. If you know 
your (AWS) stuff but tend to forget how the credential stuff is done, this is 
the tool for you.

*paws* offers multiple interfaces for programmatic, and interactive CRU
(without the D) operations on local AWS CLI profiles in a non-destructive 
fashion, whilst supporting all standard AWS CLI profile properties. 
Additionally convenience functionalities are available for repetitive tasks.

When using *paws* you should only be required to interact with AWS CLI 
configuration files when deleting a profile from them.

About
#####

Local management of AWS access keys can become quite cumbersome. There are 
tools for simplifying local AWS access key management, however they add their
own abstraction, which (in the author's opinion) complexifies it even further.
The tool was born to make access key management simple, without introducing an 
extra-layer of abstraction. 

You should have a basic understanding of how AWS offers programmatic access to 
the AWS API. If you are new to AWS, make sure to check out the learning path 
for the AWS cloud practicioner to get you started.

You may authenticate programmatically against AWS through AWS access keys. 
There are two types AWS access keys (credentials): long-term access keys 
(ids prefixed with *AKIA*) and session access keys (ids prefixed with *ASIA*).

Long-term access keys are linked to AWS IAM user entities, whereas session 
access keys are linked to intermediate AWS IAM entities (AWS STS sessions). 
Session access keys can be generated through long-term access keys or other 
session access keys. Long-term access keys can only be generated manually.

The access key (and additional information) is being used to generate an 
*AWS Sigv4* API request signature. The signature of an AWS API request is 
responsible for the authentication of an AWS API request. 

In 2015, AWS introduced the AWS CLI, which offers a programmatic interface for 
shell environments. In addition to the interface itself, AWS established an 
inofficial specification for AWS API shell client configurations, which today 
is used by other AWS software suites, in addition to third-party software. AWS 
introduced an abstraction for AWS access key management called CLI profiles
(a.k.a. *named profiles*, or just *profiles*) which defines a pattern for 
interoperable storage of AWS API client configurations, as well as AWS access 
keys.

AWS profiles can exist on a filesystem, or in a shell environment, whereas 
shell profiles take precedence over filesystem profiles.

An AWS profile consists of multiple key/value properties, some are part of a 
generic AWS API client configuration (e.g. ``cli_pager``, ``output``), some are 
part of AWS credentials (e.g. ``aws_access_key_id``).

A profile existing on a filesystem may be split across two partial profiles, 
where the AWS API client configuration is defined in ``$AWS_CONFIG_FILE`` 
(e.g. ~/.aws/config), and the AWS credential is defined in 
``$AWS_SHARED_CREDENTIALS_FILE`` (e.g. ~/.aws/credentials). Both files are 
formatted in the INI-format, where each INI section is equal to a partial (
or whole) profile.

.. note::
    Both partial profiles may contain any (whole) profile property, except for
    ``source_profile``.

The identifier for the configuration (INI section name) of the partial profile 
is prefixed with ``profile `` and may contain any character besides ``\n`` or 
``]``.

The identifier for the AWS credential partial profile may contain any 
characters besides ``\n`` or ``]``.

The configuration partial profile may reference an AWS credential partial 
profile through the ``source_profile`` field. By default, the 
``source_profile`` property will default to ``default``, meaning, it will, by 
default, reference an AWS credential partial profile named ``default``. 
*Yo Dawg, i heard you like defaults. So by default, i put a default in your 
default.*

The two aforementioned partial profiles form a whole profile, however both 
partial profiles are legal to be a whole profile on their own.

A profile existing in a shell environment is defined through ``AWS_`` 
prefixed environment variables and has no identifier/name. Some of the 
environment variables are also used for interacting with filesystem profiles.

Inside ``$AWS_SHARED_CREDENTIALS_FILE``, there SHOULD only be AWS credential 
properties (access key id, secret access key, optionally session token). 
Inside ``$AWS_CONFIG`` there SHOULD only be properties not part of an 
AWS credential.
A difference between long-term profiles and session profiles exists only by the
addition of a session token.

How It Works
############

You input a profile, and out comes a profile. In between, you have the option 
to manipulate the input profile. You can update properties interactively, or
through stdin piping. You can also create, or update session profiles from a 
long-term (or other session) profile. The output profile can be formatted as 
INI, JSON, and for POSIX environments as well as PowerShell environments. 
Write-back to the filesystem is optional, but integrated. 

Getting Started
###############

.. 
    .. argparse::
       :module: aws_myfa.__main__
       :func: get_parser
       :prog: paws

The following commands are required:

* :code:`python3` (>= 3.11)
* :code:`pip`
* :code:`pipenv` (Development)

Install *paws* and make sure the command is available.

.. code-block:: shell

    $ python3 -m pip install victorykit-paws
    $ paws --help

Alternatively, you can clone the repository and install via pipenv

.. code-block:: shell

    $ mkdir paws && cd $_ && git clone git@bitbucket.org:victorykit/py-paws.git .

.. code-block:: shell

    $ python3 -m pipenv install -d

.. code-block:: shell

    $ python3 -m pipenv run paws --help

The documentation can be built through the pipenv enironment

.. code-block:: shell

    $ python3 -m pipenv run htmldocgen

.. code-block:: shell

    $ python3 -m pipenv run mddocgen

Usage Examples
##############

Let's look at the default profile

.. code-block::

    $ paws session-profile

Unlikely, that the default profile is linked to a session access key. Instead, 
let's look at at the default profile, as if it was linked to a long-term access 
key.

.. code-block::

    $ paws long-term-profile
    region=moon-copernicus-1
    output=json
    aws_access_key_id=AKIATXXXXXXXXXXXXXX
    aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

All properties empty? That's because we don't have a default profile. Doesn't 
matter, we can just continue (if your default profile really doesn't exist, 
please do the mental acrobatics of having one).

Who would have thought, the region was misconfigured. Let's change the region.

.. code-block:: shell

    $ paws long-term-profile --configure --quick
    source_profile [default]: 
    aws_access_key_id [AKIATXXXXXXXXXXXXXX]: 
    aws_secret_access_key [****************]: 
    output [json]: 
    region [moon-copernicus-1]: eu-central-1
    region=eu-central-1
    output=json
    aws_access_key_id=AKIATXXXXXXXXXXXXXX
    aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Ok, that's fixed. Let's look at our profile again.

.. code-block:: shell

    $ paws long-term-profile
    region=moon-copernicus-1
    output=json
    aws_access_key_id=AKIATXXXXXXXXXXXXXX
    aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

It still is the same, that's because *paws* is non-destructive and does not 
actively write to neither the filesystem, nor the shell environment. If you
want to write-back to the filesystem like you would probably expect (config 
file and shared credentials file), we can do so.

.. code-block:: shell

    $ paws long-term-profile --configure --quick \
        --write-fs-config yayconfig \
        --write-fs-shared-credentials yaycredentials

*paws* also writes-back to the filesystem in a non-destructive way. All 
non-default profile properties are preserved, as well as any other INI 
component.

Ok, so now we have a working default profile. Let's create a new profile 
named ``default-mfa`` for new session access keys by authenticating with this 
long-term access key. We could require session access key, if we were to assume 
a role, authenticate via SAML, AWS MFA, or OIDC. In this case, we need to 
authenticate via MFA.

.. code-block:: shell

    $ paws session-profile 'default-mfa' --from 'default' --configure --quick \
        --mfa-token-code 123456 \
        --write-fs-config ~/.aws/config \
        --write-fs-config ~/.aws/credentials

You will see, that now, additionally, you are prompted for the 
``paws_virtual_mfa_device_arn`` property. We could have also just added this 
property by configuring the default profile without supplying the ``--quick`` 
flag. After that, you will be able to also configure the new profile.

You now have a new profile called ``default-mfa``. If you want more details on
what's happening, you can always supply the ``--log-level`` flag.

.. code-block:: shell

    $ paws session-profile --log-level DEBUG

We could new refresh our new profile by running

.. code-block:: shell

    $ paws session-profile 'default-mfa' \
        --mfa-token-code 123456 \
        --force-session-renewal \
        --write-fs-config ~/.aws/config \
        --write-fs-config ~/.aws/credentials


We can easily migrate the access key of a profile to another AWS credential
partial profile by overwriting the source_profile attribute.

We could have also configured the profile by piping from *stdin* in INI-format. 
Overrides for the ``from`` profile and target profile are seperated by an empty 
line.

.. code-block:: shell

    $ cat << EOF | paws session-profile --stdin --configure --mfa-token-code 123456
    paws_virtual_mfa_device_arn=arn:aws:iam::XXXXXXXXXXX:mfa/me

    region=eu-west-1
    EOF

Create a system daemon or shell script (CRON, etc.) to rotate the STS session. 
The expiration time of the requested STS session is being stored as part of the
authenticated source profile.
Software for unattended virtual MFA devices exist, however, the point of MFA is  
to have multiple authentication factors on multiple systems. The greater the 
separation between the systems, the better.
Having both, a password and a token-device on the same physical system is bad 
enough, but having it in the same software system (e.g. like 1Password, 
Bitwarden, etc.) is questionable.

License
#######

.. literalinclude:: ../LICENSE

.. only:: readme

    .. toctree::
        :hidden:
        :maxdepth: 1

        CHANGELOG

.. only:: not readme

    .. toctree::
        :hidden:
        :maxdepth: 1

        CONTRIBUTING
        SBOM
        NOTICE