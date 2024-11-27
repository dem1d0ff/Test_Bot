from aiogram import Router, types, html
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.text_decorations import html_decoration
from mathematics.geodesy_mathematics import BLH_XYZ

router = Router(name=__name__)

@router.message(Command("BLH_XYZ", prefix='/'))
async def coords_command(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer("Нет данных")
        return
    try:
        B, L, H = command.args.split(" ")
        print(B, L, H)
    except ValueError:
        await message.answer("Введены не все данные. Пример:\n/coords <B> <L> <H>")
        return

    result = BLH_XYZ(float(B), float(L), float(H))
    X = result[0]
    Y = result[1]
    Z = result[2]
    print(result)

    await message.answer(f"Координата X: {X}\n"
                         f"Координата Y: {Y}\n"
                         f"Координата Z: {Z}\n"
                         )