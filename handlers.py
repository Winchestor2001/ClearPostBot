from aiogram import types, F
from aiogram.dispatcher.router import Router
from loader import bot

router = Router()

async def is_admin(chat_id: int) -> bool:
    admins = await bot.get_chat_administrators(chat_id)
    bot_user = await bot.get_me()
    return any(admin.user.id == bot_user.id for admin in admins)


@router.channel_post()
async def text_post_handler(message: types.Message):
    if await is_admin(message.chat.id):
        if not (message.photo or message.video or message.animation or message.document):
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
