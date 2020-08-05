import os


def get_env_var(var):
    try:
        return os.environ[var]
    except KeyError:
        raise Exception(f'set {var} environment variable')


INSTALLED_APPS = [
        'ocfl_http',
    ]

ROOT_URLCONF = 'config.urls'

OCFL_STORAGE_ROOT = get_env_var('OCFL_STORAGE_ROOT')
