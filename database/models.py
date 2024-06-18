from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from config import MYSQL_URL

# Create the async engine and session
engine = create_async_engine(MYSQL_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase, AsyncAttrs):
    pass



class Masters(Base):
    __tablename__ = 'masters'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    experience: Mapped[str] = mapped_column(String(100), nullable=False)


async def models_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        async with async_session() as session:
            new_master = Masters(
                first_name='Bruce',
                last_name='Willis',
                age=37,
                experience='Has Certificate for Barber with 15 years experience'
            )
            session.add(new_master)
            await session.commit()




