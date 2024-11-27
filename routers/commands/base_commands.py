from aiogram import Router, types, html
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.text_decorations import html_decoration

router = Router(name=__name__)


@router.message(CommandStart())
async def handler_start(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await message.answer(
        text = f"Привет👋, {html.bold(message.from_user.full_name)} (@{message.from_user.username})!",
        parse_mode=ParseMode.HTML
    )


@router.message(Command("help"))
async def handler_help(message: types.Message):
    async with ChatActionSender.typing(
        bot=message.bot,
        chat_id=message.chat.id
    ):
        text = "I'm Van, 30 y.o."
        await message.answer(text=text)
