from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

class geodesyActions(IntEnum):
    CT_BLH_XYZ = auto()
    CT_SK_SK = auto()
    root = auto()

class geodesyCbData(CallbackData, prefix="CT"):
    action: geodesyActions

class BLHXYZActions(IntEnum):
    BLH_XYZ = auto()
    XYZ_BLH = auto()
    root = auto()

class BLHXYZCbData(CallbackData, prefix="BLHXYZ"):
    action: BLHXYZActions

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
        text="BLH(°) ↔ XYZ",
        callback_data=geodesyCbData(action=geodesyActions.CT_BLH_XYZ).pack()
    )
    builder.button(
        text="СК ↔ СК",
        callback_data=geodesyCbData(action=geodesyActions.CT_SK_SK).pack()
    )
    builder.adjust(1)
    return builder.as_markup()

def build_BLH_XYZ_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="BLH(°) → XYZ",
        callback_data=BLHXYZCbData(action=BLHXYZActions.BLH_XYZ).pack()
    )
    builder.button(
        text="XYZ → BLH",
        callback_data=BLHXYZCbData(action=BLHXYZActions.XYZ_BLH).pack()
    )
    builder.button(
        text="🔙 Назад",
        callback_data=geodesyCbData(action=geodesyActions.root).pack()
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
        callback_data=BLHXYZCbData(action=BLHXYZActions.root).pack()
    )
    builder.adjust(1)
    return builder.as_markup()

def build_ct_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text = "🔙 Назад",
        callback_data=ellipsoidsCbData(action=ellipsoidsActions.root).pack()
    )
    builder.adjust(1)
    return builder.as_markup()