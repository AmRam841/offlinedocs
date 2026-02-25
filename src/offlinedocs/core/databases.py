from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from .config import settings

# 1. Create the Async Engine
# echo=True prints SQL queries to terminal (Great for debugging execution plans later)
engine = create_async_engine(
    settings.DATABASE_URL, 
    echo=True, 
    future=True
)

# 2. Create the Session Factory
# This generates database sessions for every request/command
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

# 3. Define the Base Class for models
class Base(DeclarativeBase):
    pass

# 4. Dependency Injection Helper
# We will use this in FastAPI later to get a DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session