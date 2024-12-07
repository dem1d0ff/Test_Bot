from aiogram.fsm.state import StatesGroup, State

class geodesyStates(StatesGroup):

    BLH_XYZ = State()
    BLH_XYZ_WGS_84 = State()
    BLH_XYZ_GSK_2011 = State()
    BLH_XYZ_PZ_90_11 = State()
    BLH_XYZ_Krasovsky_42 = State()
    BLH_XYZ_GRS_80 = State()

    XYZ_BLH = State()
    XYZ_BLH_WGS_84 = State()
    XYZ_BLH_GSK_2011 = State()
    XYZ_BLH_PZ_90_11 = State()
    XYZ_BLH_Krasovsky_42 = State()
    XYZ_BLH_GRS_80 = State()
