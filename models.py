from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Таблица ассоциации для отношения многие ко многим между товарами и тегами
item_tag_association = Table(
    'item_tag_association',
    Base.metadata,
    Column('item_id', Integer, ForeignKey('items.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Category(Base):
    """
    Модель для категорий товаров.
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    items = relationship('Item', back_populates='category')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())

class Item(Base):
    """
    Модель для товаров.
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='items')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
    tags = relationship('Tag', secondary=item_tag_association, back_populates='items')

class User(Base):
    """
    Модель для пользователей.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
    items = relationship('Item', back_populates='user')

class Tag(Base):
    """
    Модель для тегов товаров.
    """
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
    items = relationship('Item', secondary=item_tag_association, back_populates='tags')
