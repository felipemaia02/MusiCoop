"""
    Módulo responsavel pelos métados de querys com a tabela usuário
"""

from sqlalchemy.orm import Session

from musicoop.schemas.user import UserSchema
from musicoop.models.user import User

from musicoop.settings.logs import logging

logger = logging.getLogger(__name__)


def get_user(email: str, database: Session) -> User:
    """
      Description
      -----------

      Parameters
      ----------

    """

    user = database.query(User).filter(User.email == email).first()
    logger.info("FOI RETORNADO DO BANCO O SEGUINTE EMAIL: %s", email)

    return user

def create_user(request: UserSchema, database: Session) -> User:
    """
      Description
      -----------

      Parameters
      ----------

    """

    new_user = User(email=request.email, name=request.name, username=request.username)
    database.add(new_user)
    database.commit()
    logger.info("FOI CRIADO NO BANCO O SEGUINTE USUÁRIO: %s", new_user)
    return new_user