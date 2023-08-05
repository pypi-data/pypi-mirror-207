import os
from qtc.env_config import EnvConfig


def get_env_config(env=None, env_config_file=None, **overrides):
    if env_config_file is None:
        env_config_file = os.path.join(os.path.dirname(__file__), 'env_config.cfg')

    EnvConfig.set_env_config_file(env_config_file=env_config_file)

    return EnvConfig.get_instance(env=env, overrides=overrides)
