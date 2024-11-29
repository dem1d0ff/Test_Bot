from aiogram import Router

from .geodesy_keyboard_callback_handlers import router as geodesy_kb_callback_router

router = Router(name=__name__)

router.include_router(
    geodesy_kb_callback_router
)