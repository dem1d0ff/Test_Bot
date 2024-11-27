__all__ = ("router")

from aiogram import Router

from .base_commands import router as base_commands_router
from .geodesy_commands import router as geodesy_commands_router

router = Router(name=__name__)

router.include_router(base_commands_router)
router.include_router(geodesy_commands_router)