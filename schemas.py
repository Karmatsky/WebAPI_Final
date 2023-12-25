from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Модель для категорий товаров
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = None

class Category(CategoryBase):
    """
    Модель данных для категорий товаров.
    """
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


# Модель для товаров
class ItemBase(BaseModel):
    name: str
    category_id: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: Optional[str] = None
    category_id: Optional[int] = None

class Item(ItemBase):
    """
    Модель данных для товаров.
    """
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
