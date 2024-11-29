from aiogram import Router, types, html, F
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.text_decorations import html_decoration

from keyboards.inline_keyboards.geodesy_keyboard import build_geodesy_kb
from mathematics.geodesy_mathematics import BLH_XYZ
from keyboards.start_keyboard import ButtonText, start_kb

router = Router(name=__name__)

@router.message(Command("BLH_to_XYZ", prefix='/'))
async def coords_command(message: types.Message, command: CommandObject):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    if command.args is None:
        await message.answer("Нет данных")
        return
    try:
        B, L, H = command.args.split(" ")
    except ValueError:
        await message.answer("Введены не все данные. Пример:\n/BLH_to_XYZ <B> <L> <H>")
        return
    result = BLH_XYZ(float(B), float(L), float(H))

    await message.answer(f"Координата X: {result[0]}\n"
                         f"Координата Y: {result[1]}\n"
                         f"Координата Z: {result[2]}\n"
                         )

@router.message(F.text == ButtonText.BLH_XYZ)
@router.message(Command("BLH_XYZ"))
async def handler_help(message: types.Message):
    async with ChatActionSender.typing(
        bot=message.bot,
        chat_id=message.chat.id
    ):
        text = "Перевод координат из BLH в XYZ. Пример:\n/BLH_to_XYZ <X> <Y> <Z>"
        await message.answer(text=text)

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