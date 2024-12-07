from aiogram import Router, types, html, F
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.text_decorations import html_decoration

from keyboards.inline_keyboards.geodesy_keyboard import build_geodesy_kb
from mathematics.geodesy_mathematics import BLH_XYZ
from keyboards.start_keyboard import ButtonText, start_kb

router = Router(name=__name__)

@router.message(Command("geodesy"))
async def handle_geodesy(message: types.Message):
    async with ChatActionSender.typing(
        bot=message.bot,
        chat_id=message.chat.id
    ):
        text = "Выберите действие"
        await message.answer(
            text=text,
            reply_markup=build_geodesy_kb()
        )