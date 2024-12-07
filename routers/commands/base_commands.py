from aiogram import Router, types, html, F
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils.chat_action import ChatActionSender

from keyboards.start_keyboard import ButtonText, start_kb
from keyboards.inline_keyboards.info_keyboard import build_info_keyboard

router = Router(name=__name__)

text_help = '''
/start - запуск бота 
/help - помощь
/geodesy - геодезический калькулятор
/info - полезная информация
'''

@router.message(F.text == ButtonText.HELLO)
@router.message(CommandStart())
async def handler_start(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    await message.answer(
        text = f"Привет👋, {html.bold(message.from_user.full_name)} (@{message.from_user.username})!\n"
               f"Что я умею /help",
        parse_mode=ParseMode.HTML,
        reply_markup=start_kb()
    )

@router.message(F.text == ButtonText.HELP)
@router.message(Command("help"))
async def handler_help(message: types.Message):
    async with ChatActionSender.typing(
        bot=message.bot,
        chat_id=message.chat.id
    ):
        text = text_help
        await message.answer(text=text)

@router.message(Command("info"))
async def handler_help(message: types.Message):
    async with ChatActionSender.typing(
        bot=message.bot,
        chat_id=message.chat.id
    ):
        keyboard = build_info_keyboard()
        text = "Тестовый геодезический бот"
        await message.answer(text=text, reply_markup=keyboard)