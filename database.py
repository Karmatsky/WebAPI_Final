# Импорт необходимых модулей из SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Определение URL SQLite базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.sqlite"

# Создание SQLAlchemy движка с использованием URL базы данных SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Создание фабрики сессий с использованием sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Определение базового класса для декларативных моделей
Base = declarative_base()

# Функция зависимости для получения сессии базы данных
async def get_db():
    # Создание новой сессии базы данных
    db = SessionLocal()
    try:
        # Предоставление сессии базы данных вызывающей стороне
        yield db
    finally:
        # Закрытие сессии базы данных после использования
        db.close()
