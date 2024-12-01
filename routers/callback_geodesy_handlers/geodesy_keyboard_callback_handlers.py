from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from pyexpat.errors import messages

from keyboards.inline_keyboards.geodesy_keyboard import (BLHXYZActions, BLHXYZCbData,
                                                         geodesyActions, geodesyCbData,
                                                         build_geodesy_kb, build_ellipsoid_kb,
                                                         ellipsoidsCbData, ellipsoidsActions,
                                                         build_ct_kb, build_BLH_XYZ_kb
                                                         )
from mathematics.geodetic_values import ellipsoids_values
from mathematics.geodesy_mathematics import BLH_XYZ
from routers.commands.geodesy_states import geodesyStates


router = Router(name=__name__)

@router.callback_query(geodesyCbData.filter(F.action == geodesyActions.CT_BLH_XYZ))
async def handle_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Выберите действие",
        reply_markup=build_BLH_XYZ_kb()
    )

@router.callback_query(BLHXYZCbData.filter(F.action == BLHXYZActions.BLH_XYZ))
async def handle_BLH_XYZ_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Выберите эллипсоид",
        reply_markup=build_ellipsoid_kb()
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.WGS_84))
async def BLH_XYZ_CT(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(geodesyStates.BLH_XYZ)
    a = ellipsoids_values.WGS_84[0]
    e_2 = ellipsoids_values.WGS_84[3]
    await state.update_data(a=a, e_2=e_2)
    text = ("Введите координаты в виде:\n"
            "B° ; L° ; H(м)")
    await call.message.edit_text(
        text=text,
        reply_markup=build_ct_kb(),
        cache_time=5
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.GSK_2011))
async def BLH_XYZ_CT(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(geodesyStates.BLH_XYZ)
    a = ellipsoids_values.GSK_2011[0]
    e_2 = ellipsoids_values.GSK_2011[3]
    await state.update_data(a=a, e_2=e_2)
    text = ("Введите координаты в виде:\n"
            "B° ; L° ; H(м)")
    await call.message.edit_text(
        text=text,
        reply_markup=build_ct_kb(),
        cache_time=5
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.PZ_90_11))
async def BLH_XYZ_CT(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(geodesyStates.BLH_XYZ)
    a = ellipsoids_values.PZ_90_11[0]
    e_2 = ellipsoids_values.PZ_90_11[3]
    await state.update_data(a=a, e_2=e_2)
    text = ("Введите координаты в виде:\n"
            "B° ; L° ; H(м)")
    await call.message.edit_text(
        text=text,
        reply_markup=build_ct_kb(),
        cache_time=5
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.Krasovsky_42))
async def BLH_XYZ_CT(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(geodesyStates.BLH_XYZ)
    a = ellipsoids_values.Krasovsky_42[0]
    e_2 = ellipsoids_values.Krasovsky_42[3]
    await state.update_data(a=a, e_2=e_2)
    text = ("Введите координаты в виде:\n"
            "B° ; L° ; H(м)")
    await call.message.edit_text(
        text=text,
        reply_markup=build_ct_kb(),
        cache_time=5
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.GRS_80))
async def BLH_XYZ_CT(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(geodesyStates.BLH_XYZ)
    a = ellipsoids_values.GRS_80[0]
    e_2 = ellipsoids_values.GRS_80[3]
    await state.update_data(a=a, e_2=e_2)
    text = ("Введите координаты в виде:\n"
            "B° ; L° ; H(м)")
    await call.message.edit_text(
        text=text,
        reply_markup=build_ct_kb(),
        cache_time=5
    )

@router.message(geodesyStates.BLH_XYZ)
async def coords_command(message: types.Message, state: FSMContext):
    data = await state.get_data()
    a = data.get("a")
    e_2 = data.get("e_2")
    print(a, e_2)
    if message.text is None:
        otvet1 = await message.answer("Не введены координаты")
        return
    try:
        B, L, H = message.text.split(";")
    except ValueError:
        otvet2 = await message.answer("Введены не все данные. Пример:\n"
                             "B° ; L° ; H(м)",
                             reply_markup=build_ct_kb()
                             )
        return


    result = BLH_XYZ(float(a), float(e_2), float(B), float(L), float(H))
    await message.answer(f"Координата X: {result[0]}\n"
                         f"Координата Y: {result[1]}\n"
                         f"Координата Z: {result[2]}\n"
                         )
    await message.answer(text="Выберите эллипсоид", reply_markup=build_ellipsoid_kb())
    await state.clear()





@router.callback_query(geodesyCbData.filter(F.action == BLHXYZActions.XYZ_BLH))
async def handle_XYZ_BLH_button(call: CallbackQuery):
    await call.answer(
        "В работе...",
        cache_time=5
    )

@router.callback_query(geodesyCbData.filter(F.action == geodesyActions.root))
async def handle_BLH_XYZ_button_back(call: CallbackQuery):
    await call.answer()
    text = "Выберите нужную функцию:"
    await call.message.edit_text(
        text=text,
        reply_markup=build_geodesy_kb(),
        cache_time=5
    )

@router.callback_query(BLHXYZCbData.filter(F.action == BLHXYZActions.root))
async def handle_BLH_XYZ_button_back(call: CallbackQuery):
    await call.answer()
    text = "Выберите нужную функцию:"
    await call.message.edit_text(
        text=text,
        reply_markup=(build_BLH_XYZ_kb()),
        cache_time=5
    )

@router.callback_query(ellipsoidsCbData.filter(F.action == ellipsoidsActions.root))
async def handle_BLH_XYZ_button_back(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(geodesyStates.BLH_XYZ)
    text = "Выберите эллипсоид"
    await call.message.edit_text(
        text=text,
        reply_markup=build_ellipsoid_kb(),
        cache_time=5
    )
    await state.clear()