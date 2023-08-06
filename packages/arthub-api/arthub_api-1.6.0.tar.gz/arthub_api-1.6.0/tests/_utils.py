from arthub_api import (
    api_config_oa,
    api_config_qq,
    api_config_oa_test,
    api_config_qq_test
)

_env_map = {
    "oa": api_config_oa,
    "qq": api_config_qq,
    "oa_test": api_config_oa_test,
    "qq_test": api_config_qq_test,
}


def get_config(env):
    c = _env_map.get(env)
    if not c:
        return api_config_oa
    return c