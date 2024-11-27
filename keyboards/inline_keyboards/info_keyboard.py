from aiogram import types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.chat_action import ChatActionSender


def build_info_keyboard():
    GOST = InlineKeyboardButton(
        text="✅ Ссылка на ГОСТ",
        url='https://racurs.ru/downloads/documentation/gost_r_32453-2017.pdf'
    )
    source_code_bot = InlineKeyboardButton(
        text="🤖 Исходный код",
        url='https://github.com/dem1d0ff/Test_Bot'
    )
    row = [GOST, source_code_bot]
    rows = [row]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return keyboard



