from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

class geodesyActions(IntEnum):
    BLH_XYZ = auto()
    XYZ_BLH = auto()
    SK_SK = auto()
    root = auto()

class geodesyCbData(CallbackData, prefix="geodesy"):
    action: geodesyActions

class ellipsoidsActions(IntEnum):
    WGS_84 = auto()
    GSK_2011 = auto()
    PZ_90_11 = auto()
    Krasovsky_42 = auto()
    GRS_80 = auto()
    root = auto()

class ellipsoidsCbData(CallbackData, prefix="ellipsoids"):
    action: ellipsoidsActions

def build_geodesy_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Из BLH(°) в XYZ",
        callback_data=geodesyCbData(action=geodesyActions.BLH_XYZ).pack()
    )
    builder.button(
        text="Из XYZ в BLH",
        callback_data=geodesyCbData(action=geodesyActions.XYZ_BLH).pack()
    )
    builder.button(
        text="Из СК в другую СК",
        callback_data=geodesyCbData(action=geodesyActions.SK_SK).pack()
    )
    builder.adjust(1)
    return builder.as_markup()

def build_ellipsoid_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="WGS-84",
        callback_data=ellipsoidsCbData(action=ellipsoidsActions.WGS_84).pack()
    )
    builder.button(
        text="ГСК-2011",
        callback_data=ellipsoidsCbData(action=ellipsoidsActions.GSK_2011).pack()
    )
    builder.button(
        text="ПЗ-90.11",
        callback_data=ellipsoidsCbData(action=ellipsoidsActions.PZ_90_11).pack()
    )
    builder.button(
        text="Красовский (СК-42/95)",
        callback_data=ellipsoidsCbData(action=ellipsoidsActions.Krasovsky_42).pack()
    )
    builder.button(
        text="GRS-80",
        callback_data=ellipsoidsCbData(action=ellipsoidsActions.GRS_80).pack()
    )
    builder.button(
        text="🔙 Назад",
        callback_data=geodesyCbData(action=geodesyActions.root).pack()
    )
    builder.adjust(1)
    return builder.as_markup()

def build_ct_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text = "🔙 Назад",
        callback_data = ellipsoidsCbData(action=ellipsoidsActions.root).pack()
    )
    builder.adjust(1)
    return builder.as_markup()