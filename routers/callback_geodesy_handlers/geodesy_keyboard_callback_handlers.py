from aiogram import Router, F, types
from aiogram.types import CallbackQuery
from pyexpat.errors import messages

from keyboards.inline_keyboards.geodesy_keyboard import geodesyActions, geodesyCbData, build_geodesy_kb, \
    build_ellipsoid_kb, ellipsoidsCbData, ellipsoidsActions, build_ct_kb
from mathematics.geodetic_values import ellipsoids_values
from mathematics.geodesy_mathematics import BLH_XYZ


router = Router(name=__name__)

@router.callback_query(geodesyCbData.filter(F.action == geodesyActions.BLH_XYZ))
async def handle_BLH_XYZ_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Введите координаты, а затем выберите эллипсоид\n"
             "Пример: ",
        reply_markup=build_ellipsoid_kb()
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.WGS_84))
async def WGS_84_CT(call: CallbackQuery):
    await call.answer()
    a = ellipsoids_values.WGS_84[0]
    e_2 = ellipsoids_values.WGS_84[3]
    print(a, e_2)
    text = "Обработка..."
    await call.message.edit_text(
        text=text,
        reply_markup=build_ct_kb(),
        cache_time=5
    )

@router.callback_query(geodesyCbData.filter(F.action == geodesyActions.XYZ_BLH))
async def handle_XYZ_BLH_button(call: CallbackQuery):
    await call.answer(
        "Обработка...",
        cache_time=5
    )

@router.callback_query(geodesyCbData.filter(F.action == geodesyActions.root))
async def handle_BLH_XYZ_button_back(call: CallbackQuery):
    await call.answer()
    text = "Введите координаты. Пример:\n"\
           "<B°>, <L°>, <H, м>"
    await call.message.edit_text(
        text=text,
        reply_markup=build_geodesy_kb(),
        cache_time=5
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.root))
async def handle_BLH_XYZ_button_back(call: CallbackQuery):
    await call.answer()
    text = "Выберите действие"
    await call.message.edit_text(
        text=text,
        reply_markup=build_ellipsoid_kb(),
        cache_time=5
    )