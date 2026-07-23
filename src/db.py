# В начале работы любого приложения SQLAlchemy
# создается объект, называемый движком соединений Engine. 
# Этот объект выступает в качестве центрального источника 
# соединений с конкретной базой данных, предоставляя
# как фабрику, так и пространство для хранения этих
# соединений, называемое пулом соединений .
# Движок соединений обычно является глобальным объектом,
# создаваемым только один раз для конкретного сервера базы
# данных, и настраивается с помощью строки URL,
# которая описывает, как он должен подключаться к хосту
# базы данных или бэкэнду.

#Примеры postgresql
#dialect+driver://username:password@host:port/database
#engine = create_engine('postgresql+psycopg2://user:password@localhost/dbn
#Echo - Если задать True, то движок будет сохранять логи SQL в стандартный вывод.
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)


POSTGRES_URL = "postgresql+asyncpg://postgres:postgres@postgres:5432/home_chatbot"

# создаем движок SqlAlchemy
engine = create_async_engine(POSTGRES_URL, echo = True)

# создаем класс сессии

#bind: привязывает сессию бд к определенному движку,
#который применяется для установки подключения

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session