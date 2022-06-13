import users_sub
from main import dp,user_db
from aiogram.types import Message


@dp.message_handler(commands='start')
async def conn(msg:Message):
    print(msg.text)
    user_ref = 0 if len(msg.text.split())< 2 else msg.text.split()[1]
    if user_db.add_new_user(user_id = msg.from_user.id,user_name=msg.from_user.username,user_ref=user_ref):
        return await msg.answer('Добро пожаловать')
    return await msg.answer('Вы уже были')


@dp.message_handler(commands='ref')
async def conn(msg:Message):
    if user_db.get_count_ref(msg.from_user.id) in [1, 2, 3, 4]:
        users_word= 'пользователя'
    else:
        users_word= 'пользователей'
    user_ref = f'У вас было приглашено {user_db.get_count_ref(msg.from_user.id)} {users_word}'
    link = ' https://t.me/AnonymousChat72rus_bot?start=' + str(msg.from_user.id)
    return await msg.answer(f'{user_ref}\nВаша рефералка'+link)


@dp.message_handler(commands='balance')
async def conn(msg:Message):
    return await msg.answer(f'Ваш баланс: {user_db.get_ballance(user_id=msg.from_user.id)} рублей')


@dp.message_handler(commands='who_sub')
async def buy_sub_cmd(msg:Message):
    us = user_db.get_user(msg.from_user.id)
    await msg.answer(f"У вас подписка {us.get_sub_time()}")


# @dp.message_handler(commands='sub')
# async def conn(msg:Message):
#     await msg.answer(User.get_sub_time())