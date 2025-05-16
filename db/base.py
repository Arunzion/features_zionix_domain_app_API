# Import all the models, so that Base has them before being imported by Alembic
from db.session import Base
from models.domain import Domain
from models.application import Application