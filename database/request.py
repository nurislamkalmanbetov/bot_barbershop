from database.models import *

from sqlalchemy import select, update, delete, insert


async def get_masters():
    async with async_session() as session:
        result = await session.scalars(select(Masters))
        return result
