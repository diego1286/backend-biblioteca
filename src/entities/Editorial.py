"""

Modelo de Editorial

"""
 
import uuid
 
from sqlalchemy import Column, String

from sqlalchemy.dialects.postgresql import UUID
 
from src.database.config import Base
 
 
class Editorial(Base):

    __tablename__ = "tbl_editoriales"
 
    id_editorial = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4,

        index=True,

    )
 
    nombre = Column(

        String(150),

        nullable=False,

        unique=True,

    )
 
    pais = Column(

        String(100),

        nullable=False,

    )
 
    def __repr__(self):

        return f"<Editorial(id_editorial={self.id_editorial}, nombre='{self.nombre}')>"
 