"""HyFI: Hydra Fast Interface (Hydra and Pydantic based interface framework)"""
from .__cli__ import getLogger, hydra_main
from .env import __about__ as about
from .env import __global_config__ as global_config
from .env import __hydra_version_base__
from .main import HyFI
from .main import HyFI as H
from .main import HyFI as HI
