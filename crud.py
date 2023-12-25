from sqlalchemy.orm import Session
import schemas
from models import Category, Item

# Операции CRUD для категорий

def create_category(db: Session, schema: schemas.CategoryCreate):
    """
    Создание новой категории в базе данных.
    """
    db_category = Category(**schema.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    """
    Получение списка категорий из базы данных с пагинацией.
    """
    return db.query(Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: int):
    """
    Получение категории по её идентификатору.
    """
    return get_entity_by_id(db, Category, category_id)

def update_category(db: Session, category_id: int, category_data: schemas.CategoryUpdate | dict):
    """
    Обновление данных категории в базе данных.
    """
    return update_entity(db, Category, category_id, category_data)

def delete_category(db: Session, category_id: int):
    """
    Удаление категории из базы данных.
    """
    return delete_entity(db, Category, category_id)


# Операции CRUD для элементов

def create_item(db: Session, schema: schemas.ItemCreate):
    """
    Создание нового элемента в базе данных.
    """
    db_item = Item(**schema.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    """
    Получение списка элементов из базы данных с пагинацией.
    """
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    """
    Получение элемента по его идентификатору.
    """
    return get_entity_by_id(db, Item, item_id)

def update_item(db: Session, item_id: int, item_data: schemas.ItemUpdate | dict):
    """
    Обновление данных элемента в базе данных.
    """
    return update_entity(db, Item, item_id, item_data)

def delete_item(db: Session, item_id: int):
    """
    Удаление элемента из базы данных.
    """
    return delete_entity(db, Item, item_id)


# Общие функции

def get_entity_by_id(db: Session, model, entity_id: int):
    """
    Получение сущности по её идентификатору.
    """
    return db.query(model).filter_by(id=entity_id).first()

def update_entity(db: Session, model, entity_id: int, entity_data: dict):
    """
    Обновление данных сущности в базе данных.
    """
    db_entity = get_entity_by_id(db, model, entity_id)

    if db_entity:
        for key, value in entity_data.items():
            if hasattr(db_entity, key):
                setattr(db_entity, key, value)

        db.commit()
        db.refresh(db_entity)
        return db_entity
    return None

def delete_entity(db: Session, model, entity_id: int):
    """
    Удаление сущности из базы данных.
    """
    db_entity = get_entity_by_id(db, model, entity_id)
    if db_entity:
        db.delete(db_entity)
        db.commit()
        return True
    return False
