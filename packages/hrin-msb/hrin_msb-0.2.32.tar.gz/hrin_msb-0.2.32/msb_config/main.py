import os

from .constants import (ENVIRONMENT_VARIABLE_NAME, ENV_LOAD_STATUS_KEY, DEBUG_VARIABLE_NAME, DEBUG_VARIABLE_VALUE)
from .var import EnvVar
from msb_env import (NameConst)


class Config:

	@staticmethod
	def load(env_path: str = '', main_file: str = '', local_file: str = ''):
		from .core import load_config
		load_config(env_path, main_file, local_file)

	@staticmethod
	def is_loaded() -> bool:
		return os.environ.get(NameConst.ENV_LOAD_STATUS_KEY_NAME) is not None

	@staticmethod
	def get(key: str = '', default=None) -> EnvVar:
		return EnvVar(key=key, value=os.environ.get(key, default=default))

	@staticmethod
	def debug():
		return Config.get(NameConst.DEBUG_VARIABLE_NAME).as_bool(default=False)

	@staticmethod
	def env_name() -> str | None:
		return Config.get(NameConst.ENVIRONMENT_VARIABLE_NAME).as_str(default=None)

	@staticmethod
	def is_local_env():
		return Config.env_name() == 'local'

	@staticmethod
	def is_dev_or_test_env() -> bool:
		return str(Config.env_name()).lower() in NameConst.DEV_OR_TEST_ENV_NAMES_LIST
