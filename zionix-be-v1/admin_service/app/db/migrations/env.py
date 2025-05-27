import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Add parent directory to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, BASE_DIR)

from app.db.base import Base
from app.core.config import settings

# this is the Alembic Config object
config = context.config

# Set sqlalchemy.url
config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata