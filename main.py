import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, admin_id
from databases import UsersCRUD


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)
user_db = UsersCRUD()


async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флуди...")


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text=f"Соединение открыто")

async def send_to_admin_shd(dp):
    user_db.close_conn()
    await bot.send_message(chat_id=admin_id, text=f"Соединение закрыто")

if __name__ == "__main__":
    from handlers.commands import dp
    executor.start_polling(dp, on_startup=send_to_admin, on_shutdown=send_to_admin_shd)
    import handlers