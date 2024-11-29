__all__ = ("router")

from aiogram import Router

from .commands import router as commands_router
from .callback_geodesy_handlers import router as callback_geodesy_handlers_router

router = Router(name=__name__)

router.include_routers(
    commands_router,
    callback_geodesy_handlers_router
)