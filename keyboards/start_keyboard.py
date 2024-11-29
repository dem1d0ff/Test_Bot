from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELLO = "Привет"
    HELP = "Помощь"
    BLH_XYZ = "Перевод из BLH в XYZ"


def start_kb():
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.HELP)
    button_BLH_XYZ = KeyboardButton(text=ButtonText.BLH_XYZ)
    button_row_up = [button_hello, button_help]
    button_row_down = [button_BLH_XYZ]
    keyboard = ReplyKeyboardMarkup(keyboard=[button_row_up, button_row_down], resize_keyboard=True)
    return keyboard
