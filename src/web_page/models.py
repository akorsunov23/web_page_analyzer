from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text

from src.core.database import Base


class WebPageSourceCode(Base):
    """Модель хранения исходного кода страницы."""
    __tablename__ = 'web_page_source_code'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime, default=datetime.now(), comment='Дата/время добавления в БД')
    url = Column(String(300), nullable=False, comment='URL исходной кода')
    source_code = Column(Text, nullable=False, comment='Исходный код')
