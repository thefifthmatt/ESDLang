# -*- coding: utf-8 -*-
def event_m50_35_2000():
    """Elevator in MAP_city_upper layer"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(2030) != 0
    """State 3: [Preset] Elevator with lid_SubState"""
    assert event_m50_35_x138(z153=50351202, z154=200000, z155=200001, z156=50353404, z157=50353405)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_2010():
    """Elevator in MAP_city_upper layer_on switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(2030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z164=50351202, z165=10, z166=50353404)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_2020():
    """Elevator in MAP_city_upper layer_under switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(2030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z164=50351202, z165=40, z166=50353405)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_2030():
    """MAP elevator_city_upper layer_start"""
    """State 0,2: [Preset] Elevator with lid_Startup_SubState"""
    assert event_m50_35_x137(z158=50353404, z159=50353405, z160=50351202, z161=50353913, z162=10, z163=50353404)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_3000():
    """Elevator in MAP_city_lower layer"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(3030) != 0
    """State 3: [Preset] Elevator with lid_SubState"""
    assert event_m50_35_x138(z153=50351204, z154=300000, z155=300001, z156=50353406, z157=50353407)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_3010():
    """Elevator in MAP_city_lower layer_on switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(3030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z164=50351204, z165=10, z166=50353406)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_3020():
    """Elevator in MAP_city_lower layer_under switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(3030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z164=50351204, z165=40, z166=50353407)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_3030():
    """Elevator in MAP_city_lower layer_start"""
    """State 0,2: [Preset] Elevator with lid_Startup_SubState"""
    assert event_m50_35_x137(z158=50353406, z159=50353407, z160=50351204, z161=50353913, z162=10, z163=50353406)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_4000():
    """Elevator in MAP_city_bonfire 2"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Preset] Elevator with lid_SubState"""
    assert event_m50_35_x138(z153=50351206, z154=400000, z155=400001, z156=50353400, z157=50353401)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_4010():
    """Elevator in MAP_city_on bonfire 2_switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z164=50351206, z165=10, z166=50353400)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_4020():
    """Elevator in MAP _ Town _ Bonfire 2_ Below switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z164=50351206, z165=40, z166=50353401)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_4030():
    """Elevator in MAP _ City _ Bonfire 2_ Start"""
    """State 0,2: [Preset] Elevator with lid_Startup_SubState"""
    assert event_m50_35_x137(z158=50353400, z159=50353401, z160=50351206, z161=50353914, z162=40, z163=50353401)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_6000():
    """Stone board to elevate bridge tower"""
    """State 0,3: [Preset] Stone board to raise the tower of the bridge_SubState"""
    call = event_m50_35_x121(z172=50353740)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_35_6020():
    """Bridge tower rising"""
    """State 0,2: [Preset] Bridge tower rises_SubState"""
    assert event_m50_35_x95(z193=50353740, z194=50353751, z195=50353750)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_6030():
    """The tower of the bridge rises"""
    """State 0,2: [Preset] Bridge tower rises_Navigation switch_SubState"""
    assert event_m50_35_x110(z167=50353751, z168=50353750, z169=603010, z170=603020, z171=50353740)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_7000():
    """OBJ_pillar running on stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353575, z128=50353906, z129=700000, z130=700010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_8000():
    """OBJ_Jumping out_1 running on a stone switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353890, z128=50353900, z129=800000, z130=800010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_8010():
    """OBJ_Jump out_2 operating with a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353825, z128=50353901, z129=801000, z130=801010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_8060():
    """Enemy activation on the building_Jump 2"""
    """State 0,2: [Preset] Enemy activation on the building_SubState"""
    assert event_m50_35_x233(z36=50353825, z37=535020024)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_9000():
    """OBJ_bullet barrier_1 running on a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353606, z128=50353909, z129=900000, z130=900010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_10000():
    """OBJ_Item_1 working with stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353850, z128=50353902, z129=1000000, z130=1000010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_10010():
    """OBJ_Item_2 working with stone statue switch"""
    """State 0,2: [Preset] OBJ_Navigation 1 version_SubState running on stone statue switch"""
    assert event_m50_35_x169(z120=50353875, z121=50353912, z122=1001000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_11000():
    """OBJ_wall pillars working with stone statue switches"""
    """State 0,2: [Preset] OBJ_Navigation 1 version_SubState running on stone statue switch"""
    assert event_m50_35_x169(z120=50353650, z121=50353903, z122=1100000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_12000():
    """OBJ_wall trabeculars_1 running on a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353701, z128=50353905, z129=1200000, z130=1200010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_12010():
    """OBJ_wall trabeculars_2 operated by stone statue switch_2"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353700, z128=50353904, z129=1201000, z130=1201010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13000():
    """OBJ_Roofwalk_1 running on a stone switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353608, z128=50353911, z129=1300000, z130=1300010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13010():
    """OBJ_Roofwalk_2 operated by a stone statue switch_2"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353609, z128=50353910, z129=1301000, z130=1301010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13020():
    """OBJ_Roofwalk_3 with stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353603, z128=50353907, z129=1302000, z130=1302010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13030():
    """OBJ_Roofwalk_4 with a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z127=50353604, z128=50353908, z129=1303000, z130=1303010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13050():
    """Change navigation between buildings_1"""
    """State 0,2: [Preset] Change navigation between buildings_SubState"""
    assert event_m50_35_x176(z112=50353608, z113=50353609, z114=1305010, z115=1305000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13060():
    """Change navigation between buildings_2"""
    """State 0,2: [Preset] Change navigation between buildings_SubState"""
    assert event_m50_35_x176(z112=50353609, z113=50353603, z114=1306010, z115=1306000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_13070():
    """Change navigation between buildings_3"""
    """State 0,2: [Preset] Change navigation between buildings_SubState"""
    assert event_m50_35_x176(z112=50353603, z113=50353604, z114=1307010, z115=1307000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20000():
    """Door that turns with switch"""
    """State 0,2: [Preset] Door rotated by switch_SubState"""
    assert event_m50_35_x50(z221=50351210, z222=50353408, z223=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20010():
    """Rotating door with doors_Aisle_Navi switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z188=50351210, val2=2001010, val3=2001000, z189=535020042)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20020():
    """Door that turns with switch_Thorn room"""
    """State 0,2: [Preset] Door rotated by switch_SubState"""
    assert event_m50_35_x50(z221=50351211, z222=50353402, z223=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20030():
    """Rotating door with switch_Thorn room_Navigation switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z188=50351211, val2=2003010, val3=2003000, z189=535020044)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20040():
    """Rotating door with switch"""
    """State 0,2: [Preset] Rotating door with switch_Two switches_SubState"""
    assert event_m50_35_x185(z95=50351213, z96=50353410, z97=32, z98=50353412)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20050():
    """Doors that rotate with switch_Blow-out_Navi switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z188=50351213, val2=2005010, val3=2005000, z189=535020046)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20060():
    """Door rotated by switch_135 degree version"""
    """State 0,3: [Preset] Door that rotates with switch_135 degree version_Two switch version_SubState"""
    assert event_m50_35_x189(z91=50351215, z92=50353409, z93=32, z94=50353411)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_20070():
    """Rotating door with switch_135 degree version_Navigation switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z188=50351215, val2=2007010, val3=2007000, z189=535020040)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_21000():
    """Door opened with switch_Crossroad"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353203, z214=50351221, z215=2100000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_21010():
    """Door opened with switch_Ghost Knight Room"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353200, z214=50351220, z215=2101000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_21020():
    """Door opened with switch_Elevator room"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353209, z214=50351222, z215=2102000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_21030():
    """Door opened with switch_Revolving door passage"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353213, z214=50351223, z215=2103000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_21040():
    """Door that opens with switch_Thorn Zone"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353211, z214=50351224, z215=2104000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_21050():
    """Door opened with switch_Thorn Zone Heights"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353212, z214=50351225, z215=2105000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_21060():
    """Door opened with switch_Straight tip"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z213=50353308, z214=50351226, z215=2106000)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_22000():
    """Spear from the left and right with the switch"""
    """State 0,2: [Preset] Switch left and right with switch_SubState"""
    assert event_m50_35_x59(z216=50353100, z217=0.2, z218=0.3)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_23000():
    """Machine gun bow and arrow _ hill room"""
    """State 0,2: [Preset] Machine gun bow and arrow_SubState"""
    assert event_m50_35_x67(z210=50351450, z211=50353115, z212=1.5)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_25000():
    """Multiple doors of ruins"""
    """State 0,2: [Preset] Multiple doors of ruins_Continuous version_SubState"""
    assert event_m50_35_x55(z219=5)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_25010():
    """Multiple doors in ruins"""
    """State 0,2: [Preset] Ruins Multiple Doors_Navigation Switch_SubState"""
    assert event_m50_35_x102()
    """State 1: Finish"""
    EndMachine()

def event_m50_35_26000():
    """C root key door"""
    """State 0,3: [Preset] C root key_SubState"""
    call = event_m50_35_x151(z151=50350400, z152=2600000)
    if call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
    elif call.Get() == 0:
        """State 1: Finish"""
        EndMachine()

def event_m50_35_27000():
    """Switch thorn floor with switch"""
    """State 0,2: [Preset] Switch the thorn floor with a switch_SubState"""
    assert event_m50_35_x91(z38=50353310, z39=50351750, z40=50351760)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_28000():
    """Ghost Knight's Materialization_Character_The Beginning of the Ruins_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000050, z205=4001, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28010():
    """Ghost Knight's Materialization_Character_The Beginning of Ruins_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000051, z205=4002, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28050():
    """Ghost Knight's Materialization_Character_Mausoleum_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000052, z205=5000, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28060():
    """Ghost Knight's Materialization_Character_Mausoleum_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000053, z205=5002, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28070():
    """Ghost Knight Materialization_Character_Rei_3"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000054, z205=5202, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28080():
    """Ghost Knight Materialization_Character_Reiper_4"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000055, z205=5400, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28090():
    """Ghost Knight Materialization_Character_Mausoleum_5"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000056, z205=5800, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28100():
    """Ghost Knight's Materialization_Character_Mausoleum_6"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000057, z205=5801, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_28110():
    """Ghost Knight's Materialization_Character_Mausoleum_7"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z204=535000058, z205=5802, z206=96650000, z207=96650010)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29000():
    """The Ghost Knight's Materialization_OBJ_The Beginning of the Ruins_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351600, z209=535000050)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29010():
    """Realization of the Ghost Knight_OBJ_Beginning of Ruins_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351601, z209=535000051)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29050():
    """Ghost knight materialization_OBJ_ mausoleum_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351610, z209=535000052)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29060():
    """Ghost knight materialization_OBJ_ mausoleum_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351613, z209=535000053)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29070():
    """Ghost knight materialization_OBJ_ mausoleum_3"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351615, z209=535000054)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29080():
    """Ghost knight materialization_OBJ_ mausoleum_4"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351611, z209=535000055)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29090():
    """Ghost knight materialization_OBJ_ mausoleum_5"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351614, z209=535000056)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29100():
    """Ghost knight materialization_OBJ_ mausoleum_6"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351616, z209=535000057)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_29110():
    """Ghost knight materialization_OBJ_ mausoleum_7"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z208=50351612, z209=535000058)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_30000():
    """Boss: Underground Queen_Battle"""
    """State 0,2: [Preset] Boss Battle _ BGM playback and HP display with activation state release_SubState"""
    assert (event_m50_35_x111(z173=535000081, z174=501, z175=5030000, z176=535020080, z177=6.5, z178=3000000,
            z179=900, z180=4))
    """State 1: Finish"""
    EndMachine()

def event_m50_35_30010():
    """Boss: Queen's enemy summons"""
    """State 0,3: [Preset] Queen's Enemy Summon _No Duplicate Version_SubState"""
    call = event_m50_35_x181(z8=900, z9=50001000, z10=50001039)
    if call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Done():
        """State 2: Finish"""
        EndMachine()

def event_m50_35_30020():
    """Doors opened by destroying bosses: mural"""
    """State 0,3: [Preset] Door opened by boss defeat_SubState"""
    call = event_m50_35_x71(z72=50351500, z73=535000081, val1=3002000, z74=8)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_35_30030():
    """Boss: Queen's voice"""
    """State 0,3: [Preset] Queen's singing voice_SubState"""
    call = event_m50_35_x153(z133=503500002, z134=900, z135=20, z136=3003000, z137=3003003, z138=2)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_35_30040():
    """Boss: Queen's lines"""
    """State 0,2: [Preset] Queen's lines_SubState"""
    assert event_m50_35_x193(z86=5030000, z87=4.5, z88=535000081, z89=900, z90=535020082)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_33000():
    """Boss: Petrochemical root boss_battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m50_35_x1(z279=535000091, z280=3300000, z281=3300000, z282=504, z283=5030020, z284=535020090,
            mode2=0))
    """State 1: Finish"""
    EndMachine()

def event_m50_35_34000():
    """Boss: Poison Dragon_Battle"""
    """State 0,2: [Preset] Poison Dragon Battle_SubState"""
    assert (event_m50_35_x209(z61=535000096, z62=502, z63=5030030, z64=535020095, z65=5.5, z66=3400000,
            z67=901, z68=3400010))
    """State 1: Finish"""
    EndMachine()

def event_m50_35_34010():
    """The crown that appears when you destroy a boss"""
    """State 0,3: [Preset] Crown _SubState that appears when a boss is destroyed"""
    # action:5310:"A faint heat lingers in the ancient crown"
    call = event_m50_35_x223(z1=50356110, z2=535000036, z3=535000096, z4=5, action1=5310)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_35_34020():
    """NPC bow management"""
    """State 0,2: [Preset] NPC bow management_SubState"""
    assert event_m50_35_x252(z5=535000096, z6=901, z7=535020038)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_34030():
    """Boss: Dragon Battle Filter Change"""
    """State 0,2: [Preset] Change dragon battle filter_SubState"""
    assert event_m50_35_x197(z75=901, z76=3.3, z77=535020095, z78=535000096, z79=3403000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_34050():
    """Awakening Dragon"""
    """State 0,2: [Preset] Awakening Dragon_SubState"""
    assert (event_m50_35_x99(z52=535000032, z53=535000034, z54=50352100, z55=3405000, z56=3405010, z57=3405011,
            z58=3405001))
    """State 1: Finish"""
    EndMachine()

def event_m50_35_35010():
    """Treasure on a pillar_2"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z276=50353850, z277=150, z278=50356400)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_35020():
    """Treasure on a pillar_3"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z276=50353609, z277=150, z278=50356570)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_35030():
    """Treasure on the pillar_4"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z276=50353609, z277=151, z278=50356580)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_35040():
    """Treasure on the pillar_5"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z276=50353875, z277=150, z278=50356410)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_36000():
    """Hidden door navigation mesh change_1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_35_x12(z271=50351008, z272=20, z273=3600000, z274=0, z275=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_40000():
    """Disabling damage"""
    """State 0,1: Zako: Petrified damage disabled"""
    SetDamageImmunityByCharacterId(206001, 310050000, 1)
    SetDamageImmunityByCharacterId(206001, 310060001, 1)
    SetDamageImmunityByCharacterId(666001, 310050000, 1)
    SetDamageImmunityByCharacterId(666001, 310060001, 1)
    SetDamageImmunityByCharacterId(666011, 310050000, 1)
    SetDamageImmunityByCharacterId(666011, 310060001, 1)
    SetDamageImmunityByCharacterId(666021, 310050000, 1)
    SetDamageImmunityByCharacterId(666021, 310060001, 1)
    SetDamageImmunityByCharacterId(666041, 310050000, 1)
    SetDamageImmunityByCharacterId(666041, 310060001, 1)
    SetDamageImmunityByCharacterId(666080, 310050000, 1)
    SetDamageImmunityByCharacterId(666080, 310060001, 1)
    SetDamageImmunityByCharacterId(671100, 310050000, 1)
    SetDamageImmunityByCharacterId(671100, 310060001, 1)
    """State 6: White Spirit NPC: Petrification disabled"""
    SetDamageImmunityByGeneratorId(711, 167110000, 1)
    SetDamageImmunityByGeneratorId(711, 167110001, 1)
    SetDamageImmunityByGeneratorId(711, 167110002, 1)
    SetDamageImmunityByGeneratorId(711, 167110003, 1)
    SetDamageImmunityByGeneratorId(711, 310050000, 1)
    SetDamageImmunityByGeneratorId(711, 310060001, 1)
    SetDamageImmunityByGeneratorId(714, 167110000, 1)
    SetDamageImmunityByGeneratorId(714, 167110001, 1)
    SetDamageImmunityByGeneratorId(714, 167110002, 1)
    SetDamageImmunityByGeneratorId(714, 167110003, 1)
    SetDamageImmunityByGeneratorId(714, 310050000, 1)
    SetDamageImmunityByGeneratorId(714, 310060001, 1)
    """State 5: Three bosses: Petrification disabled"""
    SetDamageImmunityByCharacterId(862000, 310050000, 1)
    SetDamageImmunityByCharacterId(862000, 167110000, 1)
    SetDamageImmunityByCharacterId(862000, 167110001, 1)
    SetDamageImmunityByCharacterId(862000, 167110002, 1)
    SetDamageImmunityByCharacterId(862000, 167110003, 1)
    SetDamageImmunityByCharacterId(863000, 310050000, 1)
    SetDamageImmunityByCharacterId(863000, 167110000, 1)
    SetDamageImmunityByCharacterId(863000, 167110001, 1)
    SetDamageImmunityByCharacterId(863000, 167110002, 1)
    SetDamageImmunityByCharacterId(863000, 167110003, 1)
    SetDamageImmunityByCharacterId(864000, 310050000, 1)
    SetDamageImmunityByCharacterId(864000, 167110000, 1)
    SetDamageImmunityByCharacterId(864000, 167110001, 1)
    SetDamageImmunityByCharacterId(864000, 167110002, 1)
    SetDamageImmunityByCharacterId(864000, 167110003, 1)
    """State 4: Enemy: Damage nullification for Dragon Bridge event"""
    SetDamageImmunityByCharacterId(666010, 310080004, 1)
    """State 3: PC: Disable damage in Dragon Bridge event"""
    SetDamageImmunityByCharacterId(100, 310080008, 1)
    """State 2: Finish"""
    EndMachine()

def event_m50_35_51000():
    """Start from the bottom"""
    """State 0,1: Finish"""
    EndMachine()

def event_m50_35_52000():
    """Return to the bottom"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m50_35_x30(z252=50351800, z253=10250000, z254=5200000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_35_53000():
    """Door that opens with DLC purchase"""
    """State 0,3: [Preset] Door that opens with DLC purchase_SubState"""
    call = event_m50_35_x80(z69=50352000, z70=5300000, z71=5300010)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_35_55000():
    """Inter-DLC event"""
    """State 0,2: [Preset] Inter-DLC events _ Completely annihilated _SubState"""
    assert event_m50_35_x243(z28=6000, z29=6001, z30=6002, z31=6003, z32=6004, z33=100700)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_55010():
    """DLC event_Dragon Blood Knight"""
    """State 0,2: [Preset] Inter-DLC event_Dragon Blood Knight Extermination_SubState"""
    assert event_m50_35_x245(z21=6500, z22=6510, z23=6530, z24=6531, z25=6540, z26=6550, z27=100701)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_55020():
    """Inter-DLC event _C route petrochemical clearing"""
    """State 0,2: [Preset] Inter-DLC event _ Clear C root petrification_SubState"""
    assert event_m50_35_x239(z34=101053, z35=100702)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_80000():
    """Reproduction fire 01_Starting point"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035000, z269=5035099)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_81000():
    """Regeneration of fire 02_city end"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035100, z269=5035199)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_83000():
    """Rebirth Fire 04_Poison Dragon"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035300, z269=5035399)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_84000():
    """Reproduction Fire 05_Hidden room of the ruins"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035400, z269=5035499)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_85000():
    """Regenerative fireworks 06_ cave"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035500, z269=5035599)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_86000():
    """Rebirth of fire 07_The hidden door of the large room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035600, z269=5035699)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_87000():
    """Reproduction of fire 08_city"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z268=5035700, z269=5035799)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_89000():
    """Shop lineup expansion_Queen"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_35_x32(z250=101050, z251=101200)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_89010():
    """Shop lineup expansion_Dragon"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_35_x32(z250=101051, z251=101201)
    """State 1: Finish"""
    EndMachine()

def event_m50_35_x0(z285=0, z286=0, z253=10250000, z254=5200000):
    """[Lib] Warp between maps after poly play
    z285: Pre-warp poly play ID
    z286: Poly Play ID after Warp
    z253: Map ID
    z254: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z285, z286, z253, z254, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m50_35_x1(z279=535000091, z280=3300000, z281=3300000, z282=504, z283=5030020, z284=535020090,
                    mode2=0):
    """[Lib] [Preset] Boss Battle Start
    z279: Boss destruction flag
    z280: Start point ID
    z281: End point ID
    z282: Sound ID
    z283: Boss Battle ID
    z284: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m50_35_x2(z279=z279)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m50_35_x3(z280=z280, z281=z281)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m50_35_x4(z282=z282, z283=z283, z284=z284)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m50_35_x5()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m50_35_x6(z283=z283)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m50_35_x7(z282=z282, z283=z283, z284=z284, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m50_35_x2(z279=535000091):
    """[Reproduction] Boss Battle_Start
    z279: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z279) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_35_x3(z280=3300000, z281=3300000):
    """[Condition] Boss Battle_Start
    z280: Start point ID
    z281: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z280, z281, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z280, z281, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x4(z282=504, z283=5030020, z284=535020090):
    """[Execution] Boss Battle_Start
    z282: Sound ID
    z283: Boss Battle ID
    z284: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z282)
    """State 1: Boss battle start notification"""
    StartBossFight(z283)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z284, 1)
    """State 4: End state"""
    return 0

def event_m50_35_x5():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x6(z283=5030020):
    """[Condition] Boss Battle_End Judgment
    z283: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z283, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x7(z282=504, z283=5030020, z284=535020090, mode2=0):
    """[Execute] Boss Battle_End
    z282: Sound ID
    z283: Boss Battle ID
    z284: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z284, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z283)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z282)
    """State 5: End state"""
    return 0

def event_m50_35_x8():
    """[Lib] [Reproduction] OBJ attach_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x9():
    """[Lib] [Condition] OBJ attach_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x10(z276=_, z277=_, z278=_):
    """[Lib] [execute] OBJ attach
    z276: Parent OBJ instance ID
    z277: Parent Damipoli ID
    z278: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z276, z277, z278)
    """State 2: End state"""
    return 0

def event_m50_35_x11(z276=_, z277=_, z278=_):
    """[Lib] [Preset] OBJ attach
    z276: Parent OBJ instance ID
    z277: Parent Damipoli ID
    z278: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m50_35_x8()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m50_35_x9()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m50_35_x10(z276=z276, z277=z277, z278=z278)
    """State 4: End state"""
    return 0

def event_m50_35_x12(z271=50351008, z272=20, z273=3600000, z274=0, z275=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z271: Object instance ID
    z272: OBJ state ID
    z273: Navimesh switching point ID
    z274: Additional attributes
    z275: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m50_35_x13(z271=z271, z272=z272, z273=z273, z275=z275, z274=z274)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m50_35_x14(z271=z271, z272=z272, z273=z273)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m50_35_x15(z271=z271, z272=z272, z273=z273, z274=z274, z275=z275)
    """State 4: End state"""
    return 0

def event_m50_35_x13(z271=50351008, z272=20, z273=3600000, z275=2, z274=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z271: Target OBJ instance ID
    z272: Target OBJ state ID
    z273: Navimesh switching point ID
    z275: Additional attributes
    z274: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z271, z272, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z273, z275)
        DeleteNavimeshAttribute(z273, z274)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m50_35_x14(z271=50351008, z272=20, z273=3600000):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z271: Target OBJ instance ID
    z272: Target OBJ state ID
    z273: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z271, z272, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x15(z271=50351008, z272=20, z273=3600000, z274=0, z275=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z271: Target OBJ instance ID
    z272: Target OBJ state ID
    z273: Navimesh switching point ID
    z274: Additional attributes
    z275: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z273, z274)
    DeleteNavimeshAttribute(z273, z275)
    """State 2: End state"""
    return 0

def event_m50_35_x16(z270=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z270: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z270)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m50_35_x17():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x18(z268=_, z269=_):
    """[Lib] [execute] Rebirth fire
    z268: Flag start ID
    z269: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z268, z269, 0)
    """State 2: End state"""
    return 0

def event_m50_35_x19():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x20(z268=_, z269=_):
    """[Lib] [Preset] Rebirth
    z268: Flag start ID
    z269: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m50_35_x17()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m50_35_x19()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m50_35_x18(z268=z268, z269=z269)
    """State 4: End state"""
    return 0

def event_m50_35_x21(z264=535000081, z265=102436, z266=205, z267=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z264: Defeat Boss 1: Area and other flags
    z265: Summon Achievement: Global Event Flag
    z266: Summon achievement count: global variable
    z267: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z265, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z264, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z266, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z266, NpcInfoValue(z267, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z265, 1)
                CompareEventFlag(0, z265, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m50_35_x22(z260=_, z261=_, z262=0, z263=0.2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z260: Summon range
    z261: Generator ID
    z262: Appearance: Minimum time
    z263: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z260, z260, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z262, 3, z263)
        IsPlayerInsidePoint(1, z260, z260, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z261)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_35_x23(z255=102430, z256=715, z257=104160, z258=103660, z259=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z255: White Phantom can appear: Global event flag
    z256: White Phantom: Generator ID
    z257: Death: Global event flag
    z258: Hostile: Global event flag
    z259: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z256)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z257, 1)
        CompareEventFlag(1, z258, 1)
        CompareEventFlag(2, z255, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z256)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z257, 1)
            CompareEventFlag(1, z258, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z256)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z257, 1)
            CompareEventFlag(1, z258, 1)
            HasNpcPhantomSpawned(2, z256, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z256, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z256)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m50_35_x24(z251=_):
    """[Lib] [Reproduction] Shop Lineup
    z251: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(z251) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m50_35_x25(z251=_):
    """[Lib] [execution] shop lineup
    z251: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(z251, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x26(z252=50351800):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z252)
    """State 2: End state"""
    return 0

def event_m50_35_x27(z252=50351800):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z252, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z252)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m50_35_x28(z252=50351800, z253=10250000, z254=5200000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    z253: Map ID
    z254: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z252, 1)
    """State 4: Warp PC action"""
    PlayerActionRequest(6)
    assert PlayerIsInEventAction(6) != 0
    """State 5: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 6, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 6: Warp SFX playback PC invincible"""
        PlaySfxSelfGenerated(8002, 219, 200)
        SetPlayerInvincible(1)
        assert (GetStateTime() > 2.5) != 0
        """State 2: Multiplayer prohibited state: ON"""
        ProhibitMultiplayer(1)
        """State 3: Save execution"""
        SaveExecution()
        """State 9: [Lib] Warp between maps after poly play_SubState"""
        assert event_m50_35_x0(z285=0, z286=0, z253=z253, z254=z254)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m50_35_x29(z252=50351800):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z252: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z252, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x30(z252=50351800, z253=10250000, z254=5200000):
    """[Lib] [Preset] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    z253: Map ID
    z254: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m50_35_x26(z252=z252)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m50_35_x27(z252=z252)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m50_35_x29(z252=z252)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m50_35_x28(z252=z252, z253=z253, z254=z254)
    """State 5: End state"""
    return 0

def event_m50_35_x31(z250=_):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z250: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z250, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x32(z250=_, z251=_):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z250: Boss destruction flag
    z251: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m50_35_x24(z251=z251)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m50_35_x31(z250=z250)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m50_35_x25(z251=z251)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x33(z245=_, z246=_, z247=0, z248=0.2, z249=_):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON
    z245: Summon range
    z246: Generator ID
    z247: Appearance: Minimum time
    z248: Appearance: Maximum time
    z249: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z245, z245, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z247, 3, z248)
        IsPlayerInsidePoint(1, z245, z245, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z246)
            SetEventFlag(z249, 1)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_35_x34(z230=535020010, z232=535000011):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z230: Lottery determination flag
    z232: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z232) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z230) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m50_35_x35(z231=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z231: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z231, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m50_35_x36(z230=535020010, z233=5, z234=20):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z230: Lottery determination flag
    z233: Number of appearance judgment points
    z234: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z230, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z233)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z234, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m50_35_x37(z230=535020010, z231=14, z232=535000011, z233=5, z234=20):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z230: Lottery determination flag
    z231: Random number comparison value
    z232: Defeat flag
    z233: Number of appearance judgment points
    z234: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m50_35_x34(z230=z230, z232=z232)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m50_35_x35(z231=z231)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m50_35_x36(z230=z230, z233=z233, z234=z234)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m50_35_x46(z230=z230, z234=z234)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m50_35_x38(val4=_, z242=20):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val4: Appearance judgment number
    z242: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z242) == val4) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_35_x39(z238=_, z239=0, z240=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z238: Appearance judgment point ID
    z239: Minimum appearance time
    z240: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z238, z238, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z239, 3, z240)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_35_x40(z241=974, z243=_, z244=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z241: Generator ID
    z243: Appearance start point ID
    z244: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z241, z243, z244)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z241)
    """State 4: Finish"""
    return 0

def event_m50_35_x41(z235=535000011):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z235: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z235) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m50_35_x42(z238=_, z239=0, z240=5, z241=974, val4=_, z242=20, z243=_, z244=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z238: Intrusion detection point ID
    z239: Minimum appearance time
    z240: Maximum time to appear
    z241: Generator ID
    val4: Appearance judgment number
    z242: Lottery result point variable
    z243: Appearance start point ID
    z244: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m50_35_x38(val4=val4, z242=z242)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m50_35_x39(z238=z238, z239=z239, z240=z240)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m50_35_x40(z241=z241, z243=z243, z244=z244)
    """State 4: Finish"""
    return 0

def event_m50_35_x43(z236=974, mode1=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z236: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z236)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m50_35_x44(z235=535000011, z237=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z235: Defeat flag
    z237: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z235, 1)
    """State 2: Head flag judgment"""
    CompareEventFlag(0, 102750, 1)
    if ConditionGroup(0):
        """State 4: Hand flag judgment"""
        CompareEventFlag(0, 102752, 1)
        if ConditionGroup(0):
            """State 5: Foot flag judgment"""
            CompareEventFlag(0, 102753, 1)
            if ConditionGroup(0):
                """State 6: Torso flag judgment"""
                CompareEventFlag(0, 102751, 1)
                if ConditionGroup(0):
                    """State 10: Weapon flag ON"""
                    SetEventFlag(z237, 1)
                else:
                    """State 7: Torso flag ON"""
                    SetEventFlag(102751, 1)
            else:
                """State 9: Foot flag ON"""
                SetEventFlag(102753, 1)
        else:
            """State 8: Hand flag ON"""
            SetEventFlag(102752, 1)
    else:
        """State 3: Head flag ON"""
        SetEventFlag(102750, 1)
    """State 11: End state"""
    return 0

def event_m50_35_x45(z235=535000011, z236=974, mode1=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z235: Defeat flag
    z236: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m50_35_x41(z235=z235)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m50_35_x43(z236=z236, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m50_35_x44(z235=z235, z237=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m50_35_x44(z235=z235, z237=102755)
    """State 5: End state"""
    return 0

def event_m50_35_x46(z230=535020010, z234=20):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z230: Lottery determination flag
    z234: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z230, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z234, 0)
    """State 3: End state"""
    return 0

def event_m50_35_x47(z222=_, z221=_, z223=10):
    """[Reproduction] Door rotated by switch
    z222: Switch OBJ instance ID
    z221: Revolving door OBJ instance ID
    z223: Initial state OBJ state ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z221, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z221, z223)
        assert CompareObjStateId(z221, z223, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z222, 30, 0) and CompareObjStateId(z221, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z222, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z222, 10, 0)
    elif CompareObjStateId(z222, 30, 0) and CompareObjStateId(z221, 10, 0):
        Goto('L0')
    elif CompareObjStateId(z222, 30, 0) and CompareObjStateId(z221, 32, 0):
        Goto('L0')
    elif CompareObjStateId(z222, 30, 0) and CompareObjStateId(z221, 34, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x48(z222=_, z221=_):
    """[Condition] Door rotated by switch
    z222: Switch OBJ instance ID
    z221: Revolving door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z221, 10, 0)
    CompareObjState(1, z221, 30, 0)
    CompareObjState(2, z221, 32, 0)
    CompareObjState(3, z221, 34, 0)
    CompareObjState(4, z221, 70, 0)
    CompareObjState(5, z221, 72, 0)
    CompareObjState(6, z221, 74, 0)
    CompareObjState(7, z221, 76, 0)
    if ConditionGroup(4):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z221, 30, 0)
        assert ConditionGroup(0)
        """State 22: Top: Switch back"""
        return 4
    elif ConditionGroup(5):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z221, 32, 0)
        assert ConditionGroup(0)
        """State 23: Right: Switch back"""
        return 5
    elif ConditionGroup(6):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z221, 34, 0)
        assert ConditionGroup(0)
        """State 24: Bottom: Switch back"""
        return 6
    elif ConditionGroup(7):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z221, 10, 0)
        assert ConditionGroup(0)
        """State 25: Left: Switch back"""
        return 7
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z222, -1, -4, 0)
        CompareObjState(0, z222, 30, 0)
        assert ConditionGroup(0)
        """State 18: Door up from left"""
        return 0
    elif ConditionGroup(1):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z222, -1, -4, 0)
        CompareObjState(0, z222, 30, 0)
        assert ConditionGroup(0)
        """State 19: Door from top to right"""
        return 1
    elif ConditionGroup(2):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z222, -1, -4, 0)
        CompareObjState(0, z222, 30, 0)
        assert ConditionGroup(0)
        """State 20: Door from right to bottom"""
        return 2
    elif ConditionGroup(3):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z222, -1, -4, 0)
        CompareObjState(0, z222, 30, 0)
        assert ConditionGroup(0)
        """State 21: Door from bottom to left"""
        return 3

def event_m50_35_x49(z117=_, z226=_, z227=_, z118=_, z228=80, z229=10):
    """[Execution] Door rotated by switch
    z117: Revolving door OBJ instance ID
    z226: Pillar operation OBJ state ID
    z227: OBJ state ID for which the column has ended
    z118: Switch OBJ instance ID
    z228: Switch operation OBJ state ID
    z229: Switch operation end OBJ state ID
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z118, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z118, 30, 0)
    assert ConditionGroup(0)
    """State 1: The door rotates"""
    ChangeObjState(z117, z226)
    """State 3: Waiting for the column to finish operation"""
    CompareObjState(0, z117, z227, 0)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z118, z228)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z118, z229, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_35_x50(z221=_, z222=_, z223=10):
    """[Preset] Door rotated by switch
    z221: Revolving door OBJ instance ID
    z222: Switch OBJ instance ID
    z223: Initial state OBJ state ID
    """
    """State 0,1: [Reproduction] Door Rotated by Switch_SubState"""
    assert event_m50_35_x47(z222=z222, z221=z221, z223=z223)
    """State 3: [Condition] Door rotated by switch_SubState"""
    call = event_m50_35_x48(z222=z222, z221=z221)
    if call.Get() == 0:
        """State 2: [Execution] Door rotated by switch_SubState"""
        assert event_m50_35_x49(z117=z221, z226=70, z227=30, z118=z222, z228=80, z229=10)
    elif call.Get() == 1:
        """State 4: [Execution] Door rotated by switch_2_SubState"""
        assert event_m50_35_x49(z117=z221, z226=72, z227=32, z118=z222, z228=80, z229=10)
    elif call.Get() == 2:
        """State 5: [Execution] Door rotated by switch_3_SubState"""
        assert event_m50_35_x49(z117=z221, z226=74, z227=34, z118=z222, z228=80, z229=10)
    elif call.Get() == 3:
        """State 6: [Execution] Door rotated by switch_4_SubState"""
        assert event_m50_35_x49(z117=z221, z226=76, z227=10, z118=z222, z228=80, z229=10)
    elif call.Get() == 4:
        """State 7: [Execution] Door revolving with switch_Return switch_SubState"""
        assert event_m50_35_x51(z118=z222, z224=80, z225=10)
    elif call.Get() == 5:
        """State 8: [Execution] Door revolving with switch_Return switch_2_SubState"""
        assert event_m50_35_x51(z118=z222, z224=80, z225=10)
    elif call.Get() == 6:
        """State 9: [Execution] Door rotated by switch_Switch return_3_SubState"""
        assert event_m50_35_x51(z118=z222, z224=80, z225=10)
    elif call.Get() == 7:
        """State 10: [Execution] Door rotated by switch_Switch return_4_SubState"""
        assert event_m50_35_x51(z118=z222, z224=80, z225=10)
    """State 11: End state"""
    return 0

def event_m50_35_x51(z118=_, z224=80, z225=10):
    """[Execution] Door rotated by switch_Return switch
    z118: Switch OBJ instance ID
    z224: Switch operation OBJ state ID
    z225: Switch operation end OBJ state ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z118, z224)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z118, z225, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x52():
    """[Reproduction] Multiple doors of ruins"""
    """State 0,10: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L4')
    """State 1: Judgment of door A status"""
    if CompareObjStateId(50351350, 10, 1):
        pass
    else:
        Goto('L3')
    """State 2: Judgment of door B status"""
    if CompareObjStateId(50351351, 10, 1):
        """State 3: Judgment of door C status"""
        if CompareObjStateId(50351352, 10, 1):
            """State 4: Judgment of door D status"""
            if CompareObjStateId(50351353, 10, 1):
                """State 5: Judgment of door E status"""
                if CompareObjStateId(50351354, 10, 1):
                    pass
                else:
                    """State 9: Door E opens"""
                    Label('L0')
                    ChangeObjState(50351354, 70)
            else:
                """State 8: Door D opens"""
                Label('L1')
                ChangeObjState(50351353, 70)
                assert (GetStateTime() > 1) != 0
                Goto('L0')
        else:
            """State 7: Door C opens"""
            Label('L2')
            ChangeObjState(50351352, 70)
            assert (GetStateTime() > 1) != 0
            Goto('L1')
    else:
        """State 6: Door B opens"""
        ChangeObjState(50351351, 70)
        assert (GetStateTime() > 1) != 0
        Goto('L2')
    """State 12: Finished"""
    return 1
    """State 11: Not in operation"""
    Label('L3')
    return 0
    """State 13: The guests"""
    Label('L4')
    return 2

def event_m50_35_x53(z219=5, z220=50351350):
    """[Conditions] Multiple doors in ruins
    z219: Reaction distance
    z220: Door OBJ instance ID
    """
    """State 0,1: Did you approach the door?"""
    CompareObjPlayerDistance(0, z220, z219, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x54():
    """[Execution] Multiple doors of ruins"""
    """State 0,1: Door A opens"""
    ChangeObjState(50351350, 70)
    """State 3: Weight A"""
    CompareStateTime(0, 1.7, 3, 1.7)
    assert ConditionGroup(0)
    """State 4: Door B opens"""
    ChangeObjState(50351351, 70)
    """State 5: Weight B"""
    CompareStateTime(0, 2, 3, 2)
    assert ConditionGroup(0)
    """State 6: Door C opens"""
    ChangeObjState(50351352, 70)
    """State 7: Weight C"""
    CompareStateTime(0, 2.1, 3, 2.1)
    assert ConditionGroup(0)
    """State 8: Door D opens"""
    ChangeObjState(50351353, 70)
    """State 9: Weight D"""
    CompareStateTime(0, 1, 3, 1)
    assert ConditionGroup(0)
    """State 10: Door E opens"""
    ChangeObjState(50351354, 70)
    """State 11: Weight E"""
    CompareStateTime(0, 0.7, 3, 0.7)
    assert ConditionGroup(0)
    """State 2: OBJ transition wait"""
    CompareObjState(0, 50351354, 20, 0)
    assert ConditionGroup(0)
    """State 12: End state"""
    return 0

def event_m50_35_x55(z219=5):
    """[Preset] Multiple doors of ruins
    z219: Reaction distance
    """
    """State 0,1: [Reproduction] Multiple doors of ruins_continuous version_SubState"""
    call = event_m50_35_x52()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Multiple doors of ruins_SubState"""
        assert event_m50_35_x53(z219=z219, z220=50351350)
        """State 2: [Execution] Multiple doors of ruins_Continuous version_SubState"""
        assert event_m50_35_x54()
    elif call.Get() == 2:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x56(z216=50353100):
    """[Reproduction] Spear from the left and right with the switch
    z216: Switch OBJ instance ID
    """
    """State 0,1: Is the switch down?"""
    if CompareObjStateId(z216, 30, 0):
        """State 4: Initialize all spears"""
        InitializeObj(50351390)
        InitializeObj(50351391)
        InitializeObj(50351392)
        InitializeObj(50351393)
        InitializeObj(50351394)
        InitializeObj(50351395)
        InitializeObj(50351396)
        InitializeObj(50351397)
        assert CompareObjStateId(50351390, 10, 0)
        """State 2: Return only the switch"""
        ChangeObjState(z216, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z216, 10, 0)
    else:
        pass
    """State 5: End state"""
    return 0

def event_m50_35_x57(z216=50353100):
    """[Condition] Spear from the left and right with the switch
    z216: Switch OBJ instance ID
    """
    """State 0,1: Switch judgment"""
    IsObjDamaged(0, z216, -1, -4, 0)
    CompareObjState(0, z216, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x58(z216=50353100, z217=0.2, z218=0.3):
    """[Execute] Spear from the left and right with the switch
    z216: Switch OBJ instance ID
    z217: Wait time
    z218: Cool time
    """
    """State 0,13: Switch is up"""
    ChangeObjState(z216, 70)
    """State 14: Waiting for switch operation to end"""
    CompareObjState(0, z216, 30, 0)
    assert ConditionGroup(0)
    """State 1: Spear jumps out"""
    ChangeObjState(50351397, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 5: Spear jumps out_2"""
    ChangeObjState(50351396, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 6: Spear jumps out _3"""
    ChangeObjState(50351395, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 7: Spear jumps out _4"""
    ChangeObjState(50351394, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 8: Spear jumps out _5"""
    ChangeObjState(50351393, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 9: Spear jumps out _6"""
    ChangeObjState(50351392, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 10: Spear jumps out_7"""
    ChangeObjState(50351391, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 11: Spear jumps out_8"""
    ChangeObjState(50351390, 70)
    CompareStateTime(0, z217, 2, z217)
    assert ConditionGroup(0)
    """State 3: Waiting for spear operation to end"""
    CompareObjState(0, 50351390, 10, 0)
    assert ConditionGroup(0)
    """State 12: Cool time"""
    CompareStateTime(0, z218, 2, z218)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z216, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z216, 10, 0)
    assert ConditionGroup(0)
    """State 15: End state"""
    return 0

def event_m50_35_x59(z216=50353100, z217=0.2, z218=0.3):
    """[Preset] Switch from the left and right with the switch
    z216: Switch OBJ instance ID
    z217: Wait time
    z218: Cool time
    """
    """State 0,1: [Reproduction] Spear _SubState from the left and right with the switch"""
    assert event_m50_35_x56(z216=z216)
    """State 3: [Condition] From the left and right with the switch _SubState"""
    assert event_m50_35_x57(z216=z216)
    """State 2: [Execute] From the left and right with the switch _SubState"""
    assert event_m50_35_x58(z216=z216, z217=z217, z218=z218)
    """State 4: End state"""
    return 0

def event_m50_35_x60(z214=_, z213=_, z215=_):
    """[Reproduction] Door that opens only once with a switch
    z214: Door OBJ instance ID
    z213: Switch OBJ instance ID
    z215: Navigation switching point ID
    """
    """State 0,2: Is the door in the initial state?"""
    if CompareObjStateId(z214, 10, 1):
        """State 3: Waiting for door to finish operation"""
        assert CompareObjStateId(z214, 20, 0)
        """State 1: Navi switching_passable"""
        DeleteNavimeshAttribute(z215, 2)
        """State 5: End of operation"""
        return 1
    else:
        """State 4: Not executed"""
        return 0

def event_m50_35_x61(z213=_):
    """[Condition] Door that opens only once with switch
    z213: Switch OBJ instance ID
    """
    """State 0,1: Switch damage judgment"""
    IsObjDamaged(0, z213, -1, -4, 0)
    assert ConditionGroup(0)
    """State 2: Activate the door"""
    return 0

def event_m50_35_x62(z214=_, z213=_, z215=_):
    """[Execute] Door that opens only once with a switch
    z214: Door OBJ instance ID
    z213: Switch OBJ instance ID
    z215: Navigation switching point ID
    """
    """State 0,3: Switch is up"""
    ChangeObjState(z213, 70)
    """State 4: Waiting for switch operation to end"""
    CompareObjState(0, z213, 30, 0)
    assert ConditionGroup(0)
    """State 1: The door is in operation"""
    ChangeObjState(z214, 70)
    """State 2: Waiting for door to finish operation"""
    CompareObjState(0, z214, 20, 0)
    assert ConditionGroup(0)
    """State 5: Navi mesh switching_passable"""
    DeleteNavimeshAttribute(z215, 2)
    """State 6: End state"""
    return 0

def event_m50_35_x63(z213=_, z214=_, z215=_):
    """[Preset] Door that opens only once with a switch
    z213: Switch OBJ instance ID
    z214: Door OBJ instance ID
    z215: Navigation switching point ID
    """
    """State 0,1: [Reproduction] Door that opens only once with switch _SubState"""
    call = event_m50_35_x60(z214=z214, z213=z213, z215=z215)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Door that opens only once with switch_SubState"""
        assert event_m50_35_x61(z213=z213)
        """State 2: [Execution] Door that opens only once with a switch_SubState"""
        assert event_m50_35_x62(z214=z214, z213=z213, z215=z215)
    """State 4: End state"""
    return 0

def event_m50_35_x64(z211=50353115, z210=50351450):
    """[Reproduction] Machine gun bow and arrow
    z211: Switch OBJ instance ID
    z210: Injection port OBJ instance ID
    """
    """State 0,1: The injection port is stationary, but the switch remains down?"""
    if CompareObjStateId(z211, 30, 0) and CompareObjStateId(z210, 10, 0):
        """State 2: Return only the switch"""
        ChangeObjState(z211, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z211, 10, 0)
    else:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x65(z211=50353115):
    """[Condition] Machine gun bow and arrow
    z211: Switch OBJ instance ID
    """
    """State 0,1: Switch judgment"""
    IsObjDamaged(0, z211, -1, -4, 0)
    CompareObjState(0, z211, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x66(z210=50351450, z211=50353115, z212=1.5):
    """[Execution] machine gun bow and arrow
    z210: Injection port OBJ instance ID
    z211: Switch OBJ instance ID
    z212: Cool time
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z211, 70)
    """State 7: Waiting for switch operation to end"""
    CompareObjState(0, z211, 30, 0)
    assert ConditionGroup(0)
    """State 1: Arrows pop out"""
    ChangeObjState(z210, 70)
    """State 5: Spear waiting"""
    CompareObjState(0, z210, 70, 0)
    assert ConditionGroup(0)
    """State 3: Cool time"""
    CompareStateTime(0, z212, 2, z212)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z211, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z211, 10, 0)
    assert ConditionGroup(0)
    """State 8: End state"""
    return 0

def event_m50_35_x67(z210=50351450, z211=50353115, z212=1.5):
    """[Preset] Machine gun bow and arrow
    z210: Injection port OBJ instance ID
    z211: Switch OBJ instance ID
    z212: Cool time
    """
    """State 0,1: [Reproduction] Machine gun bow and arrow_SubState"""
    assert event_m50_35_x64(z211=z211, z210=z210)
    """State 3: [Condition] Machine gun bow and arrow_SubState"""
    assert event_m50_35_x65(z211=z211)
    """State 2: [Execution] machine gun bow and arrow_SubState"""
    assert event_m50_35_x66(z210=z210, z211=z211, z212=z212)
    """State 4: End state"""
    return 0

def event_m50_35_x68(z73=535000081, z74=8):
    """[Conditions] Door that opens when the boss is destroyed
    z73: Boss destruction flag
    z74: Weight until door opens
    """
    """State 0,1: Has the boss been destroyed? Single?"""
    CompareEventFlag(0, z73, 1)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 3: Multi start: Waiting for end"""
        IsMultiplayer(0, 0, 0)
        assert ConditionGroup(0)
        """State 5: Multi-end: Re-execute"""
        return 1
    elif ConditionGroup(0):
        """State 2: Wait"""
        CompareStateTime(0, z74, 3, z74)
        assert ConditionGroup(0)
        """State 4: End state"""
        return 0

def event_m50_35_x69(z72=50351500, val1=3002000):
    """[Execution] Door opened by boss destruction
    z72: Door OBJ instance ID
    val1: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z72, 70)
    """State 4: Ignored if there is no navigation switching"""
    if (not val1) != 0:
        pass
    else:
        """State 3: Waiting for the door to open"""
        CompareObjState(0, z72, 20, 0)
        assert ConditionGroup(0)
        """State 2: Navigation switching"""
        DeleteNavimeshAttribute(val1, 2)
    """State 5: End state"""
    return 0

def event_m50_35_x70(z72=50351500, z73=535000081, val1=3002000):
    """[Reproduction] Door opened by boss destruction
    z72: Door OBJ instance ID
    z73: Boss destruction flag
    val1: Navigation switching point ID
    """
    """State 0,6: Ignored if there is no navigation switching"""
    if (not val1) != 0:
        pass
    else:
        """State 3: Navigation switching_initialization"""
        AddNavimeshAttribute(val1, 2)
    """State 1: Has the boss been destroyed?"""
    if GetEventFlag(z73) != 0:
        """State 2: Door opens"""
        ChangeObjState(z72, 70)
        """State 7: Ignored if there is no navigation switch_2"""
        if (not val1) != 0:
            pass
        else:
            """State 5: Waiting for the door to open"""
            assert CompareObjStateId(z72, 20, 0)
            """State 4: Navigation switching"""
            DeleteNavimeshAttribute(val1, 2)
        """State 9: Defeated"""
        return 1
    else:
        """State 8: Undefeated"""
        return 0

def event_m50_35_x71(z72=50351500, z73=535000081, val1=3002000, z74=8):
    """[Preset] Door opened by boss defeat
    z72: Door OBJ instance ID
    z73: Boss destruction flag
    val1: Navigation switching point ID
    z74: Weight until door opens
    """
    """State 0,1: [Reproduction] Door _SubState opened by boss destruction"""
    call = event_m50_35_x70(z72=z72, z73=z73, val1=val1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Door opened by boss destruction_SubState"""
        call = event_m50_35_x68(z73=z73, z74=z74)
        if call.Get() == 1:
            """State 4: [Execution] Door to open by destroying boss_Sky_SubState"""
            assert event_m50_35_x213()
            """State 6: Rerun"""
            return 1
        elif call.Done():
            """State 2: [Execution] Door opened by boss destruction_SubState"""
            assert event_m50_35_x69(z72=z72, val1=val1)
    """State 5: Finish"""
    return 0

def event_m50_35_x72():
    """[Reproduction] ghost knight materialization_OBJ"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x73(z208=_):
    """[Condition] Realization of ghost knight_OBJ
    z208: Materialized OBJ instance ID
    """
    """State 0,1: Has the materialized OBJ been destroyed?"""
    IsObjBroken(0, z208, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x74(z209=_):
    """[Execution] Realization of Ghost Knight_OBJ
    z209: Materialization flag
    """
    """State 0,1: Materialization flag ON"""
    SetEventFlag(z209, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x75(z208=_, z209=_):
    """[Preset] Realization of Ghost Knight_OBJ
    z208: Materialized OBJ instance ID
    z209: Materialization flag
    """
    """State 0,1: [Reproduction] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x72()
    """State 3: [Condition] Realization of ghost knight_OBJ_SubState"""
    assert event_m50_35_x73(z208=z208)
    """State 2: [Execution] Realization of Ghost Knight_OBJ_SubState"""
    assert event_m50_35_x74(z209=z209)
    """State 4: End state"""
    return 0

def event_m50_35_x76(z204=_, z205=_, z206=96650000, z207=96650010):
    """[Preset] Ghost Knight Materialization_Character
    z204: Materialization flag
    z205: Generator ID
    z206: Materialized special effect ID
    z207: Special effect ID for production
    """
    """State 0,1: [Reproduction] Realization of Ghost Knight_Character_SubState"""
    assert event_m50_35_x77()
    """State 3: [Condition] Realization of ghost knight_Chara_SubState"""
    call = event_m50_35_x78(z204=z204)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 2: [Execution] Realization of Ghost Knight_Character_SubState"""
        assert event_m50_35_x79(z205=z205, z206=z206, z204=z204, z207=z207)
    """State 4: End state"""
    return 0

def event_m50_35_x77():
    """[Reproduction] Realization of a ghost knight character"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x78(z204=_):
    """[Condition] Realization of ghost knight _ character
    z204: Materialization flag
    """
    """State 0,1: Materialization flag determination"""
    CompareEventFlag(0, z204, 1)
    if ConditionGroup(0):
        """State 2: Entity state"""
        return 0
    else:
        """State 3: Ghost state"""
        return 1

def event_m50_35_x79(z205=_, z206=96650000, z204=_, z207=96650010):
    """[Execution] Realization of a ghost knight character
    z205: Generator ID
    z206: Materialized special effect ID
    z204: Materialization flag
    z207: Special effect ID for production
    """
    """State 0,1: Grants special effects to ghost knights"""
    SetEnemySpEffect(z205, z206, 19, 4)
    """State 2: Materialization flag determination"""
    CompareEventFlag(0, z204, 1)
    assert ConditionGroup(0)
    """State 3: Cancel special effects"""
    ClearEnemySpEffect(z205, z206)
    """State 4: Special effects for directing ghost knights"""
    SetEnemySpEffect(z205, z207, 19, 4)
    """State 5: End state"""
    return 0

def event_m50_35_x80(z69=50352000, z70=5300000, z71=5300010):
    """[Preset] Door that opens with DLC purchase
    z69: Door OBJ instance ID
    z70: Navigation switching point ID
    z71: Judgment point ID
    """
    """State 0,1: [Reproduction] Doors opened with DLC purchase_SubState"""
    call = event_m50_35_x81(z69=z69, z70=z70)
    if call.Get() == 0:
        """State 3: [Conditions] Doors opened by DLC purchase_SubState"""
        call = event_m50_35_x82(z69=z69, z71=z71)
        if call.Get() == 0:
            """State 6: [Execution] Door opened by DLC purchase_Manual_SubState"""
            assert event_m50_35_x214(z69=z69, z70=z70)
            Goto('L0')
        elif call.Get() == 2:
            """State 5: [Execution] Door opened with DLC purchase_Auto_SubState"""
            assert event_m50_35_x83(z69=z69, z70=z70)
            Goto('L0')
        elif call.Get() == 1:
            """State 7: [Execution] Door that opens with DLC purchase_No access_Front_SubState"""
            assert event_m50_35_x84(z69=z69)
        elif call.Get() == 3:
            """State 8: [Execution] Door opened with DLC purchase_No access_Back_SubState"""
            assert event_m50_35_x224(z69=z69)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Conditions] Doors opened by DLC purchase_Guest_SubState"""
        assert event_m50_35_x85(z69=z69)
        """State 2: [Execution] Door opened with DLC purchase_Guest_SubState"""
        assert event_m50_35_x86(z69=z69, z70=z70)
    """State 10: Finish"""
    Label('L0')
    return 1

def event_m50_35_x81(z69=50352000, z70=5300000):
    """[Reproduction] Door opened with DLC purchase
    z69: Door OBJ instance ID
    z70: Navigation switching point ID
    """
    """State 0,2: Navigation switching_initialization"""
    AddNavimeshAttribute(z70, 2)
    """State 1: Host?"""
    if IsGuest() != 1:
        """State 3: Safety: Door initialization"""
        InitializeObj(z69)
        assert CompareObjStateId(z69, 10, 0)
        """State 4: Disable key guide"""
        DisableObjKeyGuide(z69, 1)
        """State 5: Not passed"""
        return 0
    else:
        """State 6: The guests"""
        return 1

def event_m50_35_x82(z69=50352000, z71=5300010):
    """[Conditions] Doors opened by DLC purchase
    z69: Door OBJ instance ID
    z71: Judgment point ID
    """
    """State 0,2: Distance judgment or point judgment"""
    CompareObjPlayerDistance(0, z69, 4, 5)
    SetConditionGroup(1, 8)
    IsPlayerInsidePoint(8, z71, z71, 1)
    IsHost(8, 1, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4,5: Player status determination_2"""
    CompareEventFlag(8, 100600, 1)
    CompareEventFlag(8, 100610, 1)
    # goods:52000000:Dragon Talon
    DoesPlayerHaveItem(8, 52000000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 8: Back: Allowed"""
        return 2
    else:
        """State 9: Back: No traffic"""
        return 3
    """State 3: Approach from the front"""
    Label('L0')
    """State 1: Player status determination"""
    CompareEventFlag(8, 100600, 1)
    CompareEventFlag(8, 100610, 1)
    # goods:52000000:Dragon Talon
    DoesPlayerHaveItem(8, 52000000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 6: Front: Allowed"""
        return 0
    else:
        """State 7: Front: No traffic"""
        return 1

def event_m50_35_x83(z69=50352000, z70=5300000):
    """[Execution] Door opened with DLC purchase_Auto
    z69: Door OBJ instance ID
    z70: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z69, 20)
    """State 2: Waiting for the door to finish"""
    CompareObjState(0, z69, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z70, 2)
    """State 4: End state"""
    return 0

def event_m50_35_x84(z69=50352000):
    """[Execution] Door opened with DLC purchase
    z69: Door OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z69, 8, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x85(z69=50352000):
    """[Conditions] Doors opened with DLC purchase_Guest
    z69: Door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z69, 20, 0)
    assert ConditionGroup(0)
    """State 2: Mural opened"""
    return 0

def event_m50_35_x86(z69=50352000, z70=5300000):
    """[Execution] Door opened with DLC purchase_Guest
    z69: King's door OBJ instance ID
    z70: Navigation switching point ID
    """
    """State 0,1: Change navigation"""
    DeleteNavimeshAttribute(z70, 2)
    """State 2: End state"""
    return 0

def event_m50_35_x87(z38=50353310, z39=50351750, z40=50351760, z201=250, z202=251, z203=535000028):
    """[Reproduction] Switching thorn floor with switch
    z38: Switch OBJ instance ID
    z39: Thorn ① OBJ instance ID
    z40: Thorn ② OBJ instance ID
    z201: Replacement GM ①
    z202: Replacement GM ②
    z203: Thorn floor state flag
    """
    """State 0,4: Thorn state judgment"""
    if CompareObjStateId(z39, 10, 0) and CompareObjStateId(z40, 10, 0):
        """State 6: Thorn is falling or descending"""
        Label('L0')
        """State 10: Thorn floor state flag OFF"""
        SetEventFlag(z203, 0)
        """State 5: Grand material switching"""
        SetGroundMaterial(10, z201, 0)
        SetGroundMaterial(10, z202, 0)
    elif CompareObjStateId(z39, 80, 0) and CompareObjStateId(z40, 80, 0):
        Goto('L0')
    elif CompareObjStateId(z39, 30, 0) and CompareObjStateId(z40, 30, 0):
        """State 8: Thorns are rising or rising"""
        Label('L1')
        """State 9: Thorn floor state flag ON"""
        SetEventFlag(z203, 1)
        """State 7: Grand material switching_2"""
        SetGroundMaterial(10, z201, 1)
        SetGroundMaterial(10, z202, 1)
    elif CompareObjStateId(z39, 70, 0) and CompareObjStateId(z40, 70, 0):
        Goto('L1')
    """State 1: The thorns are stationary, but the switch remains down?"""
    if CompareObjStateId(z38, 30, 0) and CompareObjStateId(z39, 30, 0) and CompareObjStateId(z40, 30, 0):
        """State 2: Return only the switch"""
        Label('L2')
        ChangeObjState(z38, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z38, 10, 0)
    elif CompareObjStateId(z38, 30, 0) and CompareObjStateId(z39, 10, 0) and CompareObjStateId(z40, 10, 0):
        Goto('L2')
    else:
        pass
    """State 11: End state"""
    return 0

def event_m50_35_x88(z38=50353310, z39=50351750, z40=50351760):
    """[Condition] Switching thorn floor with switch
    z38: Switch OBJ instance ID
    z39: Thorn ① OBJ instance ID
    z40: Thorn ② OBJ instance ID
    """
    """State 0,2: Thorn state judgment"""
    CompareObjState(8, z39, 10, 0)
    CompareObjState(8, z40, 10, 0)
    CompareObjState(9, z39, 30, 0)
    CompareObjState(9, z40, 30, 0)
    CompareObjState(10, z39, 80, 0)
    CompareObjState(10, z40, 70, 0)
    CompareObjState(11, z39, 80, 0)
    CompareObjState(11, z40, 70, 0)
    if ConditionGroup(10):
        """State 6,8: Waiting for thorn to finish operation"""
        CompareObjState(8, z39, 10, 0)
        CompareObjState(8, z40, 10, 0)
        assert ConditionGroup(8)
        """State 12: Switch back after lowering"""
        return 2
    elif ConditionGroup(11):
        """State 5,9: Waiting for thorn to finish operation_2"""
        CompareObjState(8, z39, 30, 0)
        CompareObjState(8, z40, 30, 0)
        assert ConditionGroup(8)
        """State 13: Switch back after lift"""
        return 3
    elif ConditionGroup(8):
        """State 3,1: Switch judgment"""
        IsObjDamaged(0, z38, -1, -4, 0)
        assert ConditionGroup(0)
        """State 10: Raise thorns"""
        return 0
    elif ConditionGroup(9):
        """State 4,7: Switch judgment_2"""
        IsObjDamaged(0, z38, -1, -4, 0)
        assert ConditionGroup(0)
        """State 11: Lower thorns"""
        return 1

def event_m50_35_x89(z39=50351750, z196=_, z197=_, z38=50353310, z40=50351760, z198=250, z199=251, z200=_):
    """[Execute] Switch thorn floor with switch_flag ON
    z39: Thorn ① OBJ instance ID
    z196: Operating OBJ state ID
    z197: Thorn Operation End OBJ State ID
    z38: Switch OBJ instance ID
    z40: Thorn ② OBJ instance ID
    z198: Replacement GM ①
    z199: Replacement GM ②
    z200: GM slot
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z38, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z38, 30, 0)
    assert ConditionGroup(0)
    """State 1: Thorn is in operation"""
    ChangeObjState(z39, z196)
    ChangeObjState(z40, z196)
    """State 8: weight"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 7: Grand material switching"""
    SetGroundMaterial(10, z198, z200)
    SetGroundMaterial(10, z199, z200)
    """State 3: Waiting for thorn to finish operation"""
    CompareObjState(8, z39, z197, 0)
    CompareObjState(8, z40, z197, 0)
    assert ConditionGroup(8)
    """State 9: Thorn floor state flag ON"""
    SetEventFlag(535000028, 1)
    """State 2: Switch back"""
    ChangeObjState(z38, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z38, 10, 0)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m50_35_x90(z38=50353310):
    """[Execution] Switch thorn floor with switch_Return switch
    z38: Switch OBJ instance ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z38, 80)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z38, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x91(z38=50353310, z39=50351750, z40=50351760):
    """[Preset] Switch thorn floor with switch
    z38: Switch OBJ instance ID
    z39: Thorn ① OBJ instance ID
    z40: Thorn ② OBJ instance ID
    """
    """State 0,1: [Reproduction] Switching thorn floor with switch_SubState"""
    assert event_m50_35_x87(z38=z38, z39=z39, z40=z40, z201=250, z202=251, z203=535000028)
    """State 4: [Condition] Switching thorn floor with switch_SubState"""
    call = event_m50_35_x88(z38=z38, z39=z39, z40=z40)
    if call.Get() == 2:
        """State 6: [Execution] Switch thorn floor with switch_Return switch after descending_SubState"""
        assert event_m50_35_x90(z38=z38)
    elif call.Get() == 3:
        """State 3: [Execution] Switch thorn floor with switch_Return switch after rising_SubState"""
        assert event_m50_35_x90(z38=z38)
    elif call.Get() == 0:
        """State 8: [Execute] Switch thorn floor with switch_flag ON_SubState"""
        assert event_m50_35_x89(z39=z39, z196=70, z197=30, z38=z38, z40=z40, z198=250, z199=251, z200=1)
    elif call.Get() == 1:
        """State 7: [Execute] Switch thorn floor with switch_Flag OFF_SubState"""
        assert event_m50_35_x229(z39=z39, z41=80, z42=10, z38=z38, z40=z40, z43=250, z44=251, z45=0)
    """State 9: End state"""
    return 0

def event_m50_35_x92(z193=50353740, z194=50353751, z195=50353750):
    """[Reproduction] Bridge tower rises
    z193: Switch OBJ instance ID
    z194: Bridge tower ②_OBJ instance ID
    z195: Bridge tower ③_OBJ instance ID
    """
    """State 0,1: Do you have dragon eyes?"""
    if CompareObjStateId(z193, 20, 0):
        pass
    else:
        Goto('L1')
    """State 4: State determination of bridge 2"""
    if CompareObjStateId(z194, 10, 1):
        """State 5: State determination of bridge 3"""
        if CompareObjStateId(z195, 10, 1):
            pass
        else:
            """State 3: Bridge 3 rises"""
            Label('L0')
            ChangeObjState(z195, 70)
    else:
        """State 2: Bridge 2 rises"""
        ChangeObjState(z194, 70)
        assert (GetStateTime() > 3) != 0
        Goto('L0')
    """State 7: End of operation"""
    return 1
    """State 6: Not executed"""
    Label('L1')
    return 0

def event_m50_35_x93(z193=50353740):
    """[Condition] Bridge tower rises
    z193: Switch OBJ instance ID
    """
    """State 0,1: Judgment of dragon's eyes"""
    CompareObjState(0, z193, 20, 0)
    assert ConditionGroup(0)
    """State 2: Lift the bridge"""
    return 0

def event_m50_35_x94(z193=50353740, z194=50353751, z195=50353750):
    """[Execution] Bridge tower rises
    z193: Switch OBJ instance ID
    z194: Bridge tower ②_OBJ instance ID
    z195: Bridge tower ③_OBJ instance ID
    """
    """State 0,1: Bridge 2 rises"""
    ChangeObjState(z194, 70)
    """State 3: Weight_2"""
    CompareStateTime(0, 3, 3, 3)
    assert ConditionGroup(0)
    """State 4: Bridge 3 rises"""
    ChangeObjState(z195, 70)
    """State 2: Waiting for completion of bridge operation"""
    CompareObjState(8, z194, 20, 0)
    CompareObjState(8, z195, 20, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m50_35_x95(z193=50353740, z194=50353751, z195=50353750):
    """[Preset] Bridge tower rises
    z193: Switch OBJ instance ID
    z194: Bridge tower ②_OBJ instance ID
    z195: Bridge tower ③_OBJ instance ID
    """
    """State 0,1: [Reproduction] Bridge tower rises_SubState"""
    call = event_m50_35_x92(z193=z193, z194=z194, z195=z195)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Bridge tower rises_SubState"""
        assert event_m50_35_x93(z193=z193)
        """State 2: [Execution] Bridge tower rises_SubState"""
        assert event_m50_35_x94(z193=z193, z194=z194, z195=z195)
    """State 4: End state"""
    return 0

def event_m50_35_x96(z52=535000032, z53=535000034, z54=50352100):
    """[Reproduction] Awakening Dragon
    z52: Event 1 executed flag
    z53: Event 2 executed flag
    z54: Dragon OBJ instance ID
    """
    """State 0,2: Have you completed flight event 2?"""
    if GetEventFlag(z53) != 0:
        pass
    else:
        Goto('L0')
    """State 5: Exit Damipoli"""
    ChangeObjState(50352200, 20)
    ChangeObjState(50352201, 20)
    ChangeObjState(50352202, 20)
    ChangeObjState(50352250, 20)
    ChangeObjState(50352251, 20)
    ChangeObjState(50352252, 20)
    """State 3: Hide dragon"""
    ChangeObjState(z54, 20)
    assert CompareObjStateId(z54, 20, 0)
    """State 8: Event complete"""
    return 2
    """State 1: Has flight event 1 been executed?"""
    Label('L0')
    if GetEventFlag(z52) != 0:
        """State 4: Dragon on top"""
        ChangeObjState(z54, 30)
        assert CompareObjStateId(z54, 30, 0)
        """State 7: Resume from event 2"""
        return 1
    else:
        """State 6: Event not executed"""
        return 0

def event_m50_35_x97(z54=50352100, z55=3405000, z58=3405001):
    """[Condition] Awakening Dragon
    z54: Dragon OBJ instance ID
    z55: Flight 1 start point ID
    z58: Flight 1 end point ID
    """
    """State 0,1: Damaged or point intrusion"""
    IsObjDamaged(0, z54, -1, -3, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(8, z55, z58, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(0)
    """State 2: Flight event"""
    return 0

def event_m50_35_x98(z52=535000032, z54=50352100, z191=70, z192=30):
    """[Execution] Awakening Dragon
    z52: Event executed flag
    z54: Dragon OBJ instance ID
    z191: Flight OBJ State ID
    z192: OBJ state ID after flight
    """
    """State 0,1: Executed flag ON"""
    SetEventFlag(z52, 1)
    """State 2: Dragon flying"""
    ChangeObjState(z54, z191)
    """State 3: Wait for end of flight"""
    CompareObjState(0, z54, z192, 0)
    assert ConditionGroup(0)
    """State 4: Finish"""
    return 0

def event_m50_35_x99(z52=535000032, z53=535000034, z54=50352100, z55=3405000, z56=3405010, z57=3405011,
                     z58=3405001):
    """[Preset] Awakening Dragon
    z52: Event 1 executed flag
    z53: Event 2 executed flag
    z54: Dragon OBJ instance ID
    z55: Flight 1 start point ID
    z56: Flight 2 start point ID
    z57: Flight 2 end point ID
    z58: Flight 1 end point ID
    """
    """State 0,1: [Reproduction] Awakening Dragon_SubState"""
    call = event_m50_35_x96(z52=z52, z53=z53, z54=z54)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        """State 5: [Condition] Awakening Dragon_Points only_SubState"""
        Label('L0')
        assert event_m50_35_x161(z54=z54, z56=z56, z57=z57)
        """State 6: [Execution] Awakening Dragon _ 2nd_SubState"""
        assert event_m50_35_x226(z53=z53, z54=z54, z59=71, z60=20)
    elif call.Get() == 0:
        """State 3: [Condition] Awakening Dragon_SubState"""
        assert event_m50_35_x97(z54=z54, z55=z55, z58=z58)
        """State 2: [Execution] Awakening Dragon_SubState"""
        assert event_m50_35_x98(z52=z52, z54=z54, z191=70, z192=30)
        """State 4: [Reproduction] Awakening Dragon_Sky_SubState"""
        assert event_m50_35_x160()
        Goto('L0')
    """State 7: End state"""
    return 0

def event_m50_35_x100():
    """[Reproduction] Multiple doors in ruins _ Navigation switching"""
    """State 0,1: Judgment of door A status"""
    if CompareObjStateId(50351350, 10, 1):
        """State 2: Operation waiting for door A"""
        assert CompareObjStateId(50351350, 20, 0)
        """State 3: Door A navigation switch_door B standby"""
        DeleteNavimeshAttribute(2501000, 2)
        assert CompareObjStateId(50351351, 20, 0)
        """State 4: Door B navigation switch_door C standby"""
        DeleteNavimeshAttribute(2501010, 2)
        assert CompareObjStateId(50351352, 20, 0)
        """State 5: Door C navigation switching _ Door D operation standby"""
        DeleteNavimeshAttribute(2501020, 2)
        assert CompareObjStateId(50351353, 20, 0)
        """State 6: Door D navigator switching _ Door E standby"""
        DeleteNavimeshAttribute(2501030, 2)
        assert CompareObjStateId(50351354, 20, 0)
        """State 7: Door E navigation switching"""
        DeleteNavimeshAttribute(2501040, 2)
        """State 9: Finished"""
        return 1
    else:
        """State 8: End state"""
        return 0

def event_m50_35_x101():
    """[Conditions & Execution] Multiple doors in ruins"""
    """State 0,1: Operation waiting for door A"""
    CompareObjState(0, 50351350, 20, 0)
    assert ConditionGroup(0)
    """State 2: Door A navigation switching"""
    DeleteNavimeshAttribute(2501000, 2)
    """State 3: Operation waiting for door B"""
    CompareObjState(0, 50351351, 20, 0)
    assert ConditionGroup(0)
    """State 4: Door B navigation switching"""
    DeleteNavimeshAttribute(2501010, 2)
    """State 5: Operation waiting for door C"""
    CompareObjState(0, 50351352, 20, 0)
    assert ConditionGroup(0)
    """State 6: Door C navigation switching"""
    DeleteNavimeshAttribute(2501020, 2)
    """State 7: Operation waiting for door D"""
    CompareObjState(0, 50351353, 20, 0)
    assert ConditionGroup(0)
    """State 8: Door D navigation switching"""
    DeleteNavimeshAttribute(2501030, 2)
    """State 9: Operation waiting for door E"""
    CompareObjState(0, 50351354, 20, 0)
    assert ConditionGroup(0)
    """State 10: Door E navigation switching"""
    DeleteNavimeshAttribute(2501040, 2)
    """State 11: End state"""
    return 0

def event_m50_35_x102():
    """[Preset] Multiple doors in ruins _ Navigation switching"""
    """State 0,1: [Reproduction] Multiple doors of ruins_Navigation switching_SubState"""
    call = event_m50_35_x100()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Conditions & Execution] Ruins Multiple Doors_Navigation Switch_SubState"""
        assert event_m50_35_x101()
    """State 3: End state"""
    return 0

def event_m50_35_x103():
    """[Reproduction] Summon the Queen's enemy"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x104(z188=_, val2=_, val3=_, z189=_):
    """[Reproduction] Door that rotates with switch_Navigation switching and flag switching
    z188: Revolving door instance ID
    val2: Upper navigation switching point ID
    val3: Lower navigation switching point ID
    z189: Enemy activation flag
    """
    """State 0,7: Navigation switching"""
    AddNavimeshAttribute(val2, 2)
    AddNavimeshAttribute(val3, 2)
    """State 1: Judgment of door status"""
    if CompareObjStateId(z188, 10, 0):
        """State 2,15: Enemy activation flag OFF"""
        SetEventFlag(z189, 0)
    elif CompareObjStateId(z188, 30, 0):
        """State 3,8: Navigation switching_Upper traffic"""
        DeleteNavimeshAttribute(val2, 2)
        """State 14: Enemy activation flag ON"""
        SetEventFlag(z189, 1)
    elif CompareObjStateId(z188, 32, 0):
        """State 4,18: Enemy activation flag OFF_4"""
        SetEventFlag(z189, 0)
    elif CompareObjStateId(z188, 34, 0):
        """State 5,9: Navigation switch"""
        DeleteNavimeshAttribute(val3, 2)
        """State 20: Enemy activation flag OFF_6"""
        SetEventFlag(z189, 0)
    elif CompareObjStateId(z188, 41, 0):
        """State 10,16: Enemy activation flag OFF_2"""
        SetEventFlag(z189, 0)
    elif CompareObjStateId(z188, 40, 0):
        """State 11,17: Enemy activation flag OFF_3"""
        SetEventFlag(z189, 0)
    elif CompareObjStateId(z188, 43, 0):
        """State 12,19: Enemy activation flag OFF_5"""
        SetEventFlag(z189, 0)
    elif CompareObjStateId(z188, 42, 0):
        """State 13,21: Enemy activation flag OFF_7"""
        SetEventFlag(z189, 0)
    else:
        """State 6,22: Enemy activation flag OFF_8"""
        SetEventFlag(z189, 0)
    """State 23: End state"""
    return 0

def event_m50_35_x105(z188=_, val2=_, val3=_):
    """[Conditions] Doors rotated by switch_Navigation switching and flag switching
    z188: Revolving door instance ID
    val2: Upper navigation switching point
    val3: Bottom navigation switching point
    """
    """State 0,6: Waiting for door rotation"""
    CompareObjState(0, z188, 70, 0)
    CompareObjState(0, z188, 72, 0)
    CompareObjState(0, z188, 74, 0)
    CompareObjState(0, z188, 76, 0)
    CompareObjState(0, z188, 80, 0)
    CompareObjState(0, z188, 81, 0)
    CompareObjState(0, z188, 82, 0)
    CompareObjState(0, z188, 83, 0)
    CompareObjState(0, z188, 84, 0)
    CompareObjState(0, z188, 85, 0)
    CompareObjState(0, z188, 86, 0)
    CompareObjState(0, z188, 87, 0)
    assert ConditionGroup(0)
    """State 7: Navigation switching"""
    AddNavimeshAttribute(val2, 2)
    AddNavimeshAttribute(val3, 2)
    """State 1: Judgment of door status"""
    CompareObjState(0, z188, 10, 0)
    CompareObjState(1, z188, 41, 0)
    CompareObjState(2, z188, 30, 0)
    CompareObjState(3, z188, 40, 0)
    CompareObjState(4, z188, 32, 0)
    CompareObjState(5, z188, 43, 0)
    CompareObjState(6, z188, 34, 0)
    CompareObjState(7, z188, 42, 0)
    if ConditionGroup(0):
        """State 2,12: Mouth left 1"""
        return 0
    elif ConditionGroup(1):
        """State 8,16: Mouth is upper left 1"""
        return 4
    elif ConditionGroup(2):
        """State 3,13: Mouth up 1"""
        return 1
    elif ConditionGroup(0):
        """State 9,17: Mouth upper right 1"""
        return 5
    elif ConditionGroup(4):
        """State 4,14: Mouth is right 1"""
        return 2
    elif ConditionGroup(5):
        """State 10,18: Mouth lower right 1"""
        return 6
    elif ConditionGroup(6):
        """State 5,15: Mouth down 1"""
        return 3
    elif ConditionGroup(7):
        """State 11,19: Mouth lower left 1"""
        return 7

def event_m50_35_x106(val2=_, z189=_, z190=_):
    """[Execution] Rotating door with a switch
    val2: Point ID of the navigation to switch
    z189: Enemy activation flag
    z190: Flag ONOFF
    """
    """State 0,3: Is switching required?"""
    if (not val2) != 0:
        pass
    else:
        """State 1: Navigation switching"""
        DeleteNavimeshAttribute(val2, 2)
    """State 2: Switch enemy activation flag"""
    SetEventFlag(z189, z190)
    """State 4: End state"""
    return 0

def event_m50_35_x107(z188=_, val2=_, val3=_, z189=_):
    """[Preset] Rotating door with switch _ Navi switching and flag switching
    z188: Revolving door instance ID
    val2: Upper navigation switching point
    val3: Bottom navigation switching point
    z189: Enemy activation flag
    """
    """State 0,1: [Reproduction] Door that rotates with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x104(z188=z188, val2=val2, val3=val3, z189=z189)
    """State 3: [Condition] Door rotated by switch_Navigation switching and flag switching_SubState"""
    call = event_m50_35_x105(z188=z188, val2=val2, val3=val3)
    if call.Get() == 0:
        """State 2: [Execution] Door rotated by switch_Navigation switching and flag switching_SubState"""
        assert event_m50_35_x106(val2=0, z189=z189, z190=0)
    elif call.Get() == 4:
        """State 4: [Execution] Door rotated by switch_Navigation switching and flag switching_2_SubState"""
        assert event_m50_35_x106(val2=0, z189=z189, z190=0)
    elif call.Get() == 1:
        """State 5: [Execution] Door rotated by switch_Navigation switching and flag switching_3_SubState"""
        assert event_m50_35_x106(val2=val2, z189=z189, z190=1)
    elif call.Get() == 5:
        """State 6: [Execution] Door rotated by switch_Navigation switching and flag switching_4_SubState"""
        assert event_m50_35_x106(val2=0, z189=z189, z190=0)
    elif call.Get() == 2:
        """State 7: [Execution] Door rotated by switch_Navigation switching and flag switching_5_SubState"""
        assert event_m50_35_x106(val2=0, z189=z189, z190=0)
    elif call.Get() == 6:
        """State 8: [Execution] Door rotated by switch_Navigation switching and flag switching_6_SubState"""
        assert event_m50_35_x106(val2=0, z189=z189, z190=0)
    elif call.Get() == 3:
        """State 9: [Execution] Door rotated by switch_Navigation switching and flag switching_7_SubState"""
        assert event_m50_35_x106(val2=val3, z189=z189, z190=0)
    elif call.Get() == 7:
        """State 10: [Execution] Door rotated by switch_Navigation switching and flag switching_8_SubState"""
        assert event_m50_35_x106(val2=0, z189=z189, z190=0)
    """State 11: End state"""
    return 0

def event_m50_35_x108(z167=50353751, z168=50353750, z169=603010, z170=603020):
    """[Reproduction] Bridge tower rises _ navigation switching
    z167: Instance ID of bridge 2
    z168: Instance ID of bridge 3
    z169: Bridge 2 navigation switching point ID
    z170: Bridge 3 navigation switching point ID
    """
    """State 0,1: Judgment of bridge 2 status"""
    if CompareObjStateId(z167, 10, 1):
        """State 2: Standby waiting for Bridge 2"""
        assert CompareObjStateId(z167, 20, 0)
        """State 3: Bridge 2 navigation switch_operation waiting for bridge 3"""
        DeleteNavimeshAttribute(z169, 2)
        assert CompareObjStateId(z168, 20, 0)
        """State 4: Bridge 3 navigation switching"""
        DeleteNavimeshAttribute(z170, 2)
        """State 6: Finished"""
        return 1
    else:
        """State 5: End state"""
        return 0

def event_m50_35_x109(z167=50353751, z187=50353751, z169=603010, z170=603020):
    """[Execution] Bridge tower rises
    z167: Instance ID of bridge 2
    z187: Instance ID of bridge 3
    z169: Bridge 2 navigation switching point ID
    z170: Bridge 3 navigation switching point ID
    """
    """State 0,1: Standby waiting for Bridge 2"""
    CompareObjState(0, z167, 20, 0)
    assert ConditionGroup(0)
    """State 2: Bridge 2 navigation switching"""
    DeleteNavimeshAttribute(z169, 2)
    """State 3: Standby operation of bridge 3"""
    CompareObjState(0, z187, 20, 0)
    assert ConditionGroup(0)
    """State 4: Bridge 3 navigation switching"""
    DeleteNavimeshAttribute(z170, 2)
    """State 5: End state"""
    return 0

def event_m50_35_x110(z167=50353751, z168=50353750, z169=603010, z170=603020, z171=50353740):
    """[Preset] Bridge tower rises
    z167: Tower 2 instance ID
    z168: Tower 3 instance ID
    z169: Tower 2 navigation switching point ID
    z170: Tower 3 navigation switching point ID
    z171: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] The tower of the bridge is rising_Navigation switching_SubState"""
    call = event_m50_35_x108(z167=z167, z168=z168, z169=z169, z170=z170)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Condition] Bridge tower rises_Navigation switch_SubState"""
        assert event_m50_35_x128(z171=z171)
        """State 2: [Execution] Bridge tower rises_Navigation switch_SubState"""
        assert event_m50_35_x109(z167=z167, z187=z167, z169=z169, z170=z170)
    """State 4: End state"""
    return 0

def event_m50_35_x111(z173=535000081, z174=501, z175=5030000, z176=535020080, z177=6.5, z178=3000000,
                      z179=900, z180=4):
    """[Preset] Boss battle _ BGM playback and HP display by canceling the activation state
    z173: Boss destruction flag
    z174: Sound ID
    z175: Boss Battle ID
    z176: Other flags for logic
    z177: Wait time
    z178: Start and end point ID
    z179: Boss generator ID
    z180: Wait until startup
    """
    """State 0,1: [Reproduction] Boss Battle_BGM playback and HP display with start state release_Start_SubState"""
    call = event_m50_35_x112(z173=z173)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle _ BGM playback and HP display with start state release _ Start _ SubState"""
        assert event_m50_35_x113(z178=z178, z186=z178)
        """State 3: [Execution] Boss Battle _ BGM playback and HP display with start state release _ Start _ SubState"""
        assert event_m50_35_x114(z175=z175, z176=z176, z180=z180)
        """State 7: [Reproduction] HP display and BGM playback_empty_SubState"""
        assert event_m50_35_x115()
        """State 9: [Condition] HP display and BGM playback_SubState"""
        call = event_m50_35_x116(z179=z179, z184=2, z185=535000085)
        if call.Get() == 0:
            """State 8: [Execution] HP display and BGM playback_SubState"""
            assert event_m50_35_x117(z174=z174, z177=z177, z175=z175, z182=535020084, z183=535000085)
        elif call.Get() == 1:
            """State 10: [Execution] HP display and BGM playback_2_SubState"""
            assert event_m50_35_x117(z174=z174, z177=8, z175=z175, z182=535020084, z183=535000085)
        """State 2: [Reproduction] Boss battle _ BGM playback and HP display with start state release _ End _ Empty _ SubState"""
        assert event_m50_35_x118()
        """State 6: [Condition] Boss Battle _ BGM playback and HP display with start state release _ End judgment _ SubState"""
        assert event_m50_35_x119(z175=z175)
        """State 4: [Execution] Boss Battle _ BGM playback and HP display by canceling the startup state _ End _ SubState"""
        assert event_m50_35_x120(z174=z174, z175=z175, z176=z176, z181=0)
    """State 11: End state"""
    return 0

def event_m50_35_x112(z173=535000081):
    """[Reproduction] Boss Battle _ BGM playback and HP display with start state release _ Start
    z173: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z173) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_35_x113(z178=3000000, z186=3000000):
    """[Condition] Boss Battle _ Start BGM playback and HP display _ start state release
    z178: Start point ID
    z186: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z178, z186, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z178, z186, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x114(z175=5030000, z176=535020080, z180=4):
    """[Execution] Boss Battle_BGM playback and HP display with start state release_Start
    z175: Boss Battle ID
    z176: Logic flag
    z180: Wait until boss activation
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z175)
    """State 3: Wait until startup"""
    CompareStateTime(0, z180, 3, z180)
    CompareEventFlag(0, 535020080, 1)
    assert ConditionGroup(0)
    """State 2: Logic flag ON"""
    SetEventFlag(z176, 1)
    """State 4: End state"""
    return 0

def event_m50_35_x115():
    """[Reproduction] HP display and BGM playback_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x116(z179=900, z184=2, z185=535000085):
    """[Condition] HP display and BGM playback
    z179: Boss generator ID
    z184: Activation state ID
    z185: Rematch flag
    """
    """State 0,1: Did the boss release the activation state?"""
    CompareChrEzStateValue(0, z179, 7, 1, 0)
    IsEventBossKill(0, z179, 0, 1)
    CompareChrStartUpState(0, z179, z184, 1)
    assert ConditionGroup(0)
    """State 2: Rematch determination"""
    CompareEventFlag(0, 535000085, 0)
    CompareEventFlag(1, 535000085, 1)
    if ConditionGroup(0):
        """State 3: First battle"""
        return 0
    elif ConditionGroup(1):
        """State 4: rematch"""
        return 1

def event_m50_35_x117(z174=501, z177=_, z175=5030000, z182=535020084, z183=535000085):
    """[Execution] HP display and BGM playback
    z174: Sound ID
    z177: Wait time until display
    z175: Boss Battle ID
    z182: BGM and gauge display flag
    z183: Rematch flag
    """
    """State 0,3: Wait until BGM playback and HP display"""
    CompareStateTime(0, z177, 2, z177)
    IsEventBossKill(1, z175, 0, 1)
    CompareEventFlag(0, z182, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z174)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 4: BGM and gauge display flag ON"""
    SetEventFlag(z182, 1)
    """State 5: Rematch determination flag ON"""
    SetEventFlag(z183, 1)
    """State 6: End state"""
    return 0

def event_m50_35_x118():
    """[Reproduction] Boss Battle _ BGM playback and HP display with start state release _ End _ Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x119(z175=5030000):
    """[Conditions] Boss battle_BGM playback and HP display with start state release_End judgment
    z175: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z175, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x120(z174=501, z175=5030000, z176=535020080, z181=0):
    """[Execution] Boss battle _ BGM playback and HP display _ end by canceling the startup state
    z174: Sound ID
    z175: Boss Battle ID
    z176: Other flags for logic
    z181: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z176, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z175)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > 0) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z174)
    """State 5: End state"""
    return 0

def event_m50_35_x121(z172=50353740):
    """[Preset] Stone board to raise the tower of the bridge
    z172: Key person OBJ instance ID
    """
    """State 0,1: [Reproduction] Stone board to raise the tower of the bridge _SubState"""
    call = event_m50_35_x122(z172=z172)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L1')
    """State 8: End of reproduction"""
    return 1
    """State 6: [Condition] Stone board to raise the tower of the bridge_Host_SubState"""
    Label('L0')
    call = event_m50_35_x127(z172=z172)
    if call.Get() == 0:
        """State 3: [Execution] Stone board to raise the tower of the bridge_Host_Startable_SubState"""
        call = event_m50_35_x124(z172=z172)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: Start and end"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Stone board to raise the tower of the bridge _ Host _ Unable to start _ SubState"""
        assert event_m50_35_x125(z172=z172)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Stone board to lift the tower of the bridge_Guest_SubState"""
    Label('L1')
    assert event_m50_35_x126(z172=z172)
    """State 2: [Execution] Stone board to raise the tower of the bridge_Guest_Sky_SubState"""
    assert event_m50_35_x123()
    """State 9: Guest termination"""
    return 2

def event_m50_35_x122(z172=50353740):
    """[Reproduction] Stone board to lift the tower of the bridge
    z172: Key person OBJ instance ID
    """
    """State 0,2: Host judgment"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 4: Guest termination"""
    return 0
    """State 1: Slab OBJ status judgment"""
    Label('L0')
    if CompareObjStateId(z172, 30, 0):
        """State 3: OBJ initialization ： 10"""
        Label('L1')
        ChangeObjState(z172, 10)
        assert CompareObjStateId(z172, 10, 0)
    elif CompareObjStateId(z172, 70, 0):
        Goto('L1')
    elif CompareObjStateId(z172, 74, 1) and CompareObjStateId(z172, 20, 1):
        pass
    else:
        """State 6: After execution"""
        return 2
    """State 5: Before execution"""
    return 1

def event_m50_35_x123():
    """[Execution] Stone board to lift the tower of the bridge_Guest_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x124(z172=50353740):
    """[Execution] Stone board to raise the tower of the bridge_Host_Startable
    z172: Key person OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:52650000:Dragon Stone
    DisplayYesNoMenu(1002, 1.8, z172, 190, 2, 52650000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 6: Stone board transition waiting: 30"""
        ChangeObjState(z172, 30)
        assert CompareObjStateId(z172, 30, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z172, 38, 3)
        assert PlayerIsInEventAction(11) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 3, 0)
        # goods:52650000:Dragon Stone
        DoesPlayerHaveItem(0, 52650000, 0, 5, 1, 1, 0)
        CompareObjState(1, z172, 74, 0)
        CompareObjState(1, z172, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Dragon eye consumption"""
            # goods:52650000:Dragon Stone
            ConsumeItem(52650000, 1)
            assert CompareObjStateId(z172, 20, 0)
            """State 8: Start and end"""
            return 0
    else:
        pass
    """State 7: Stone board: Initial state: 10"""
    ChangeObjState(z172, 10)
    """State 9: Rerun"""
    return 1

def event_m50_35_x125(z172=50353740):
    """[Execution] Stone board to raise the tower of the bridge
    z172: Key person OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:52650000:Dragon Stone
    DisplayOkMenu(1013, 0, 0, z172, 190, 2, 52650000, 0)
    assert OkMenuDisplay() != 1
    """State 2: Startup failure_rerun"""
    return 0

def event_m50_35_x126(z172=50353740):
    """[Condition] Stone board to lift the tower of the bridge_Guest
    z172: Key person OBJ instance ID
    """
    """State 0,1: Stone board end waiting"""
    CompareObjState(0, z172, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x127(z172=50353740):
    """[Condition] Stone board to lift the tower of the bridge_Host
    z172: Key person OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z172)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:52650000:Dragon Stone
    DoesPlayerHaveItem(0, 52650000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 3: Bootable"""
        return 0
    else:
        """State 4: Activation impossible"""
        return 1

def event_m50_35_x128(z171=50353740):
    """[Condition] Bridge tower rises
    z171: Switch OBJ instance ID
    """
    """State 0,1: Judgment of dragon's eyes"""
    CompareObjState(0, z171, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x129(z158=_, z159=_, z160=_):
    """[Reproduction] Elevator with lid_Startup
    z158: Upper switch OBJ instance ID
    z159: Lower switch OBJ instance ID
    z160: Elevator OBJ instance ID
    """
    """State 0,2: Is the elevator started?"""
    if CompareObjStateId(z160, 11, 0):
        """State 1: Switch override for elevator"""
        Label('L0')
        ChangeObjState(z158, 30)
        ChangeObjState(z159, 30)
        """State 3: End state"""
        return 0
    elif CompareObjStateId(z160, 90, 0):
        Goto('L0')
    else:
        """State 4: Activated"""
        return 1

def event_m50_35_x130(z158=_, z159=_, z160=_, z161=_):
    """[Condition] Elevator with lid_Startup
    z158: Upper switch OBJ instance ID
    z159: Lower switch OBJ instance ID
    z160: Elevator OBJ instance ID
    z161: Stone statue switch OBJ instance ID
    """
    """State 0,1: Switch judgment"""
    IsObjDamaged(0, z161, -1, -4, 0)
    CompareObjState(0, z161, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x131(z163=_, z160=_, z161=_, z162=_):
    """[Execution] Elevator with lid_Start
    z163: Activation switch OBJ instance ID
    z160: Elevator OBJ instance ID
    z161: Stone statue switch OBJ instance ID
    z162: Elevator state after opening the lid
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z161, 70)
    """State 5: weight"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 1: Elevator operation with lid open: 90"""
    ChangeObjState(z160, 90)
    """State 2: Elevator lift waiting"""
    CompareObjState(0, z160, z162, 0)
    assert ConditionGroup(0)
    """State 3: Switch activation for elevator"""
    ChangeObjState(z163, 80)
    """State 4: Waiting for switch to be valid"""
    CompareObjState(0, z163, 10, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_35_x132():
    """[Reproduction] Elevator with lid_Switch_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x133(z164=_, z165=_):
    """[Condition] Elevator with lid_Switch
    z164: Elevator OBJ instance ID
    z165: Elevator state ID opposite the switch
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z164, z165, 0):
        """State 3: Switch activation"""
        return 1
    else:
        """State 2: Disable switch"""
        return 0

def event_m50_35_x134(z164=_, z165=_, z166=_):
    """[Execution] Elevator with lid_Switch_Effective
    z164: Elevator OBJ instance ID
    z165: Elevator state ID opposite the switch
    z166: Switch OBJ instance ID
    """
    """State 0,1: Activating the switch"""
    ChangeObjState(z166, 80)
    """State 2: Wait for switch activation"""
    CompareObjState(0, z166, 10, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    CompareObjState(0, z164, z165, 1)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x135(z164=_, z165=_, z166=_):
    """[Execution] Elevator with lid_Switch_Invalid
    z164: Elevator OBJ instance ID
    z165: Elevator state ID opposite the switch
    z166: Switch OBJ instance ID
    """
    """State 0,1: Disable switch"""
    ChangeObjState(z166, 70)
    """State 2: Wait for switch invalidation"""
    CompareObjState(0, z166, 30, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    CompareObjState(0, z164, z165, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x136(z164=_, z165=_, z166=_):
    """[Preset] Elevator with lid_Switch
    z164: Elevator OBJ instance ID
    z165: Elevator state ID opposite the switch
    z166: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator with lid_Switch_Empty_SubState"""
    assert event_m50_35_x132()
    """State 4: [Condition] Elevator with lid_Switch_SubState"""
    call = event_m50_35_x133(z164=z164, z165=z165)
    if call.Get() == 1:
        """State 3: [Execution] Elevator with lid_Switch_Effective_SubState"""
        assert event_m50_35_x134(z164=z164, z165=z165, z166=z166)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator with lid_Switch_Invalid_SubState"""
        assert event_m50_35_x135(z164=z164, z165=z165, z166=z166)
    """State 5: Rerun"""
    return 0

def event_m50_35_x137(z158=_, z159=_, z160=_, z161=_, z162=_, z163=_):
    """[Preset] Elevator with lid_Startup
    z158: Upper switch OBJ instance ID
    z159: Lower switch OBJ instance ID
    z160: Elevator OBJ instance ID
    z161: Stone statue switch OBJ instance ID
    z162: Elevator state after opening the lid
    z163: Activation switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator with lid_Startup_SubState"""
    call = event_m50_35_x129(z158=z158, z159=z159, z160=z160)
    if call.Get() == 0:
        """State 3: [Condition] Elevator with lid_Startup_SubState"""
        assert event_m50_35_x130(z158=z158, z159=z159, z160=z160, z161=z161)
        """State 2: [Execution] Elevator with lid_Startup_SubState"""
        assert event_m50_35_x131(z163=z163, z160=z160, z161=z161, z162=z162)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x138(z153=_, z154=_, z155=_, z156=_, z157=_):
    """[Preset] Elevator with lid
    z153: OBJ instance ID of the elevator
    z154: On elevator point ID_
    z155: Elevator point ID_below
    z156: Upper switch OBJ instance ID
    z157: Lower switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator with lid_SubState"""
    assert event_m50_35_x139()
    """State 6: [Condition] Elevator with lid_SubState"""
    call = event_m50_35_x140(z153=z153, z154=z154, z155=z155, z156=z156, z157=z157)
    if call.Get() == 2:
        """State 3: [Execution] Elevator with lid_Return switch after descending_SubState"""
        assert event_m50_35_x144(z153=z153, z155=z155, z156=z156, z157=z157)
    elif call.Get() == 3:
        """State 5: [Execution] Elevator with lid_Return switch after ascending_SubState"""
        assert event_m50_35_x143(z153=z153, z154=z154, z156=z156, z157=z157)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator with lid_Rise_SubState"""
        assert event_m50_35_x141(z153=z153, z154=z154, z157=z157, z156=z156)
    elif call.Get() == 1:
        """State 2: [Execution] Elevator with lid_Descent_SubState"""
        assert event_m50_35_x142(z153=z153, z155=z155, z156=z156, z157=z157)
    """State 7: End state"""
    return 0

def event_m50_35_x139():
    """[Reproduction] Elevator with lid"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x140(z153=_, z154=_, z155=_, z156=_, z157=_):
    """[Condition] Elevator with lid
    z153: Elevator OBJ instance ID
    z154: On elevator point ID_
    z155: Elevator point ID_below
    z156: Upper switch OBJ instance ID
    z157: Lower switch OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z153, 10, 0)
    CompareObjState(1, z153, 40, 0)
    CompareObjState(2, z153, 80, 0)
    CompareObjState(2, z153, 41, 0)
    CompareObjState(3, z153, 70, 0)
    CompareObjState(3, z153, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or switch standby"""
        IsPlayerInsidePoint(0, z155, z155, 1)
        IsObjDamaged(0, z156, -1, 0, 0)
        CompareObjState(0, z156, 30, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or switch standby_2"""
        IsPlayerInsidePoint(0, z154, z154, 1)
        IsObjDamaged(0, z157, -1, 0, 0)
        CompareObjState(0, z157, 30, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m50_35_x141(z153=_, z154=_, z157=_, z156=_):
    """[Execution] Elevator with lid _ Ascent
    z153: Elevator OBJ instance ID
    z154: On point ID_
    z157: Lower switch OBJ instance ID
    z156: Upper switch OBJ instance ID
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z153, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z153, 30, 0)
    IsPlayerInsidePoint(8, z154, z154, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Elevator switch returns"""
    ChangeObjState(z153, 71)
    """State 5: Wait for return of elevator switch"""
    CompareObjState(0, z153, 40, 0)
    assert ConditionGroup(0)
    """State 4: Waiting for switch status"""
    CompareObjState(8, z157, 10, 0)
    CompareObjState(8, z156, 30, 0)
    assert ConditionGroup(8)
    """State 6: End state"""
    return 0

def event_m50_35_x142(z153=_, z155=_, z156=_, z157=_):
    """[Execution] Elevator with lid_Descent
    z153: Elevator OBJ instance ID
    z155: Point ID_below
    z156: Upper switch OBJ instance ID
    z157: Lower switch OBJ instance ID
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z153, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z153, 41, 0)
    IsPlayerInsidePoint(8, z155, z155, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Elevator switch returns"""
    ChangeObjState(z153, 81)
    """State 5: Wait for return of elevator switch"""
    CompareObjState(0, z153, 10, 0)
    assert ConditionGroup(0)
    """State 4: Waiting for switch status"""
    CompareObjState(8, z156, 10, 0)
    CompareObjState(8, z157, 30, 0)
    assert ConditionGroup(8)
    """State 6: End state"""
    return 0

def event_m50_35_x143(z153=_, z154=_, z156=_, z157=_):
    """[Execution] Elevator with lid_Return the switch after the lift
    z153: Elevator OBJ instance ID
    z154: On point ID_
    z156: Upper switch OBJ instance ID
    z157: Lower switch OBJ instance ID
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z153, 30, 0)
    IsPlayerInsidePoint(8, z154, z154, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Elevator switch returns"""
    ChangeObjState(z153, 71)
    """State 4: Wait for return of elevator switch"""
    CompareObjState(0, z153, 40, 0)
    assert ConditionGroup(0)
    """State 3: Waiting for switch status"""
    CompareObjState(8, z157, 10, 0)
    CompareObjState(8, z156, 30, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m50_35_x144(z153=_, z155=_, z156=_, z157=_):
    """[Execution] Elevator with lid_Return switch after lowering
    z153: Elevator OBJ instance ID
    z155: Point ID_below
    z156: Upper switch OBJ instance ID
    z157: Lower switch OBJ instance ID
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z153, 41, 0)
    IsPlayerInsidePoint(8, z155, z155, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Elevator switch returns"""
    ChangeObjState(z153, 81)
    """State 4: Wait for return of elevator switch"""
    CompareObjState(0, z153, 10, 0)
    assert ConditionGroup(0)
    """State 3: Waiting for switch status"""
    CompareObjState(8, z156, 10, 0)
    CompareObjState(8, z157, 30, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m50_35_x145(z151=50350400, z152=2600000):
    """[Reproduction] C root key door
    z151: Key door OBJ instance ID
    z152: Navigation change point ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is the door open?"""
    if CompareObjStateId(z151, 10, 0):
        """State 6: Not open"""
        return 1
    else:
        """State 3: Waiting for the door to open"""
        assert CompareObjStateId(z151, 20, 0)
        """State 4: Navi mesh switching"""
        DeleteNavimeshAttribute(z152, 2)
        """State 7: Finish"""
        return 2
    """State 5: The guests"""
    Label('L0')
    return 0

def event_m50_35_x146(z151=50350400):
    """[Conditions] C root key door
    z151: Key door OBJ instance ID
    """
    """State 0,1: Judgment to examine the door"""
    IsObjSearched(0, z151)
    assert ConditionGroup(0)
    """State 2: Key item possession determination"""
    # goods:52300000:Eternal Sanctum Key
    DoesPlayerHaveItem(0, 52300000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 3: open"""
        return 0
    else:
        """State 4: will not open"""
        return 1

def event_m50_35_x147(z151=50350400, z152=2600000):
    """[Execution] C root key_open
    z151: Key door OBJ instance ID
    z152: Navigation change point ID
    """
    """State 0,2: The door opens: 70"""
    ChangeObjState(z151, 70)
    """State 1: Message display"""
    # action:1005:"Used %s", goods:52300000:Eternal Sanctum Key
    DisplayOwnOkMenu(1005, 0, 0, 190, 2, 52300000, 0)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z151, 20, 0)
    assert ConditionGroup(0)
    """State 4: Navi mesh switching"""
    DeleteNavimeshAttribute(z152, 2)
    assert OkMenuDisplay() != 1
    """State 5: End state"""
    return 0

def event_m50_35_x148():
    """[Execution] C root key door_Do not open"""
    """State 0,1: Message display"""
    # action:1105:"It's locked"
    DisplayOwnOkMenu(1105, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m50_35_x149(z152=2600000):
    """[Execution] C root key_guest
    z152: Navigation change point ID
    """
    """State 0,1: Navi mesh switching"""
    DeleteNavimeshAttribute(z152, 2)
    """State 2: End state"""
    return 0

def event_m50_35_x150(z151=50350400):
    """[Conditions] C root key_guest
    z151: Key door OBJ instance ID
    """
    """State 0,1: Waiting for the door to open"""
    CompareObjState(0, z151, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x151(z151=50350400, z152=2600000):
    """[Preset] C root key door
    z151: Key door OBJ instance ID
    z152: Navigation change point ID
    """
    """State 0,1: [Reproduction] C root key_SubState"""
    call = event_m50_35_x145(z151=z151, z152=z152)
    if call.Get() == 1:
        """State 5: [Condition] C root key door_SubState"""
        call = event_m50_35_x146(z151=z151)
        if call.Get() == 0:
            """State 4: [Execute] C root key_open_SubState"""
            assert event_m50_35_x147(z151=z151, z152=z152)
        elif call.Get() == 1:
            """State 3: [Execution] C root key_Do not open_SubState"""
            assert event_m50_35_x148()
            """State 8: Rerun"""
            return 1
    elif call.Get() == 0:
        """State 6: [Conditions] C root key_guest_SubState"""
        assert event_m50_35_x150(z151=z151)
        """State 2: [Execution] C root key_guest_SubState"""
        assert event_m50_35_x149(z152=z152)
    elif call.Get() == 2:
        pass
    """State 7: Finish"""
    return 0

def event_m50_35_x152(z144=8503, z145=8504, z146=8505, z147=8500, z148=8501, z149=8502, z150=8506):
    """[Execution] Queen's enemy summoning
    z144: Generator ① ID
    z145: Generator ② ID
    z146: Generator ③ ID
    z147: Generator ④ ID
    z148: Generator ⑤ ID
    z149: Generator ⑥ ID
    z150: Generator ⑦ ID
    """
    """State 0,1: Summon character death process"""
    EnemyActionRequest(z144, 1)
    EnemyActionRequest(z145, 1)
    EnemyActionRequest(z146, 1)
    EnemyActionRequest(z147, 1)
    EnemyActionRequest(z148, 1)
    EnemyActionRequest(z149, 1)
    EnemyActionRequest(z150, 1)
    EnemyActionRequest(8507, 1)
    EnemyActionRequest(8508, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x153(z133=503500002, z134=900, z135=20, z136=3003000, z137=3003003, z138=2):
    """[Preset] Queen's voice
    z133: Sound ID
    z134: Generator ID
    z135: Hit group ID
    z136: Stop start point ID
    z137: Stop end point ID
    z138: Stop weight
    """
    """State 0,1: [Reproduction] Queen's singing voice_SubState"""
    call = event_m50_35_x154(z142=535000081, z134=z134, z143=535020080)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Queen's singing voice_SubState"""
        assert event_m50_35_x156(z135=z135)
        """State 3: [Execution] Queen's singing voice_Play_SubState"""
        assert event_m50_35_x158(z133=z133, z134=z134)
        """State 2: [Reproduction] Queen's singing voice_Sky_SubState"""
        assert event_m50_35_x155()
        """State 6: [Condition] Queen's singing voice_stop judgment_SubState"""
        call = event_m50_35_x157(z139=535000081, z134=z134, z135=z135, z140=5030000, z136=z136, z137=z137,
                                 z138=z138, z141=535020080)
        if call.Get() == 1:
            """State 7: [Execution] Queen singing voice_stop_2_SubState"""
            assert event_m50_35_x159(z134=z134)
        elif call.Get() == 0:
            """State 4: [Execution] Queen singing voice_stop_SubState"""
            assert event_m50_35_x159(z134=z134)
            """State 9: Rerun"""
            return 1
    """State 8: Finish"""
    return 0

def event_m50_35_x154(z142=535000081, z134=900, z143=535020080):
    """[Reproduction] Queen's voice
    z142: Boss destruction flag
    z134: Generator ID
    z143: Boss activation flag
    """
    """State 0,1: Did you defeat the queen?"""
    if GetEventFlag(z142) != 0:
        pass
    else:
        """State 3: Is the boss already activated?"""
        if GetEventFlag(z143) != 0:
            pass
        else:
            """State 4: Not defeated"""
            return 0
    """State 2: Stop generator following sound"""
    StopSoundFollowingGenerator(z134)
    """State 5: Defeated and activated"""
    return 1

def event_m50_35_x155():
    """[Reproduction] Queen's singing voice_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x156(z135=20):
    """[Condition] Queen's singing voice
    z135: Hit group ID
    """
    """State 0,1: Got a starting hit?"""
    IsPlayerOnHitGroup(8, z135, 1)
    assert ConditionGroup(8)
    """State 2: Play singing voice"""
    return 0

def event_m50_35_x157(z139=535000081, z134=900, z135=20, z140=5030000, z136=3003000, z137=3003003, z138=2,
                      z141=535020080):
    """[Condition] Queen's singing voice_stop judgment
    z139: Boss destruction flag
    z134: Generator ID
    z135: Hit group ID
    z140: Boss Battle ID
    z136: Stop start point ID
    z137: Stop end point ID
    z138: Weight to stop
    z141: Boss activation flag
    """
    """State 0,1: Did you destroy the or boss who entered the stop point or started the boss battle?"""
    IsPlayerInsidePoint(8, z136, z137, 1)
    CompareEventFlag(2, z139, 1)
    CompareEventFlag(2, z141, 1)
    IsEventBossBattle(1, z140, 1)
    if ConditionGroup(8):
        """State 3: Stop singing voice: restart"""
        return 0
    elif ConditionGroup(2):
        pass
    elif ConditionGroup(1):
        """State 2: Stop weight"""
        CompareStateTime(0, z138, 3, z138)
        assert ConditionGroup(0)
    """State 4: Stop singing: End"""
    return 1

def event_m50_35_x158(z133=503500002, z134=900):
    """[Execution] Queen's singing voice
    z133: Sound ID
    z134: Generator ID
    """
    """State 0,1: Play generator-following sound"""
    PlaySoundFollowingGenerator(5, z133, z134)
    """State 2: End state"""
    return 0

def event_m50_35_x159(z134=900):
    """[Execution] Queen singing voice_stop
    z134: Generator ID
    """
    """State 0,1: Stop generator following sound"""
    StopSoundFollowingGenerator(z134)
    """State 2: End state"""
    return 0

def event_m50_35_x160():
    """[Reproduction] Awakening Dragon_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x161(z54=50352100, z56=3405010, z57=3405011):
    """[Condition] Awakening Dragon_Points only
    z54: Dragon OBJ instance ID
    z56: Flight start point ID
    z57: Flight end point ID
    """
    """State 0,1: Did you invade the point?"""
    IsPlayerInsidePoint(8, z56, z57, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: Flight event"""
    return 0

def event_m50_35_x162(z127=_, z128=_, z129=_, z130=_):
    """[Preset] OBJ operated with stone switch
    z127: Active OBJ instance ID
    z128: Switch OBJ instance ID
    z129: Navigation change point ID before operation
    z130: Navigation change point ID after operation
    """
    """State 0,1: [Reproduction] OBJ_SubState running on a stone statue switch"""
    assert event_m50_35_x163(z128=z128, z127=z127, z129=z129, z130=z130)
    """State 4: [Condition] OBJ_SubState running on stone statue switch"""
    call = event_m50_35_x164(z121=z128, z120=z127)
    if call.Get() == 0:
        """State 2: [Execution] OBJ_SubState running on the stone switch"""
        assert event_m50_35_x165(z127=z127, z131=70, z132=30, z128=z128, z130=z130, z129=z129)
    elif call.Get() == 1:
        """State 5: [Execution] OBJ_2_SubState running on stone switch"""
        assert event_m50_35_x165(z127=z127, z131=80, z132=10, z128=z128, z130=z129, z129=z130)
    elif call.Get() == 3:
        """State 3: [Execution] OBJ_Switch_Return_SubState running on the stone statue switch"""
        assert event_m50_35_x166(z121=z128)
    elif call.Get() == 2:
        """State 6: [Execution] OBJ_Switch that works with the stone statue switch_2_SubState"""
        assert event_m50_35_x166(z121=z128)
    """State 7: End state"""
    return 0

def event_m50_35_x163(z128=_, z127=_, z129=_, z130=_):
    """[Reproduction] OBJ operated with stone statue switch
    z128: Switch OBJ instance ID
    z127: Active OBJ instance ID
    z129: Navigation change point ID before operation
    z130: Navigation change point ID after operation
    """
    """State 0,3: OBJ status judgment"""
    if CompareObjStateId(z127, 70, 0):
        """State 7,10: Change navigation_3"""
        AddNavimeshAttribute(z129, 2)
        AddNavimeshAttribute(z130, 2)
        """State 11: OBJ operation waiting"""
        assert CompareObjStateId(z127, 30, 0)
        """State 14: Change navigation_5"""
        DeleteNavimeshAttribute(z130, 2)
        AddNavimeshAttribute(z129, 2)
    elif CompareObjStateId(z127, 80, 0):
        """State 6,12: Change navigation_4"""
        AddNavimeshAttribute(z129, 2)
        AddNavimeshAttribute(z130, 2)
        """State 13: OBJ waiting_2"""
        assert CompareObjStateId(z127, 10, 0)
        """State 15: Change navigation_6"""
        DeleteNavimeshAttribute(z129, 2)
        AddNavimeshAttribute(z130, 2)
    elif CompareObjStateId(z127, 10, 0):
        """State 4,8: Change navigation"""
        DeleteNavimeshAttribute(z129, 2)
        AddNavimeshAttribute(z130, 2)
    elif CompareObjStateId(z127, 30, 0):
        """State 5,9: Change navigation_2"""
        DeleteNavimeshAttribute(z130, 2)
        AddNavimeshAttribute(z129, 2)
    """State 16: Is the switch in the initial state?"""
    if CompareObjStateId(z128, 10, 0):
        pass
    else:
        """State 17: Is the switch descending?"""
        if CompareObjStateId(z128, 70, 0):
            """State 18: Wait for switch to fall"""
            assert CompareObjStateId(z128, 30, 0)
        else:
            pass
        """State 1: Return only the switch"""
        ChangeObjState(z128, 80)
        """State 2: Wait for switch to finish"""
        assert CompareObjStateId(z128, 10, 0)
    """State 19: End state"""
    return 0

def event_m50_35_x164(z121=_, z120=_):
    """[Conditions] OBJ operated with stone statue switch
    z121: Switch OBJ instance ID
    z120: Active OBJ instance ID
    """
    """State 0,2: OBJ status judgment"""
    CompareObjState(0, z120, 10, 0)
    CompareObjState(1, z120, 30, 0)
    CompareObjState(2, z120, 70, 0)
    CompareObjState(3, z120, 80, 0)
    if ConditionGroup(2):
        """State 6,8: Wait for OBJ operation to end"""
        CompareObjState(0, z120, 30, 0)
        assert ConditionGroup(0)
        """State 12: Switch back after return"""
        return 2
    elif ConditionGroup(3):
        """State 5,9: Waiting for OBJ to end operation_2"""
        CompareObjState(0, z120, 10, 0)
        assert ConditionGroup(0)
        """State 13: Switch back after operation"""
        return 3
    elif ConditionGroup(0):
        """State 3,1: Switch judgment"""
        IsObjDamaged(0, z121, -1, -4, 0)
        assert ConditionGroup(0)
        """State 10: Run OBJ"""
        return 0
    elif ConditionGroup(1):
        """State 4,7: Switch judgment_2"""
        IsObjDamaged(0, z121, -1, -4, 0)
        assert ConditionGroup(0)
        """State 11: Get OBJ back"""
        return 1

def event_m50_35_x165(z127=_, z131=_, z132=_, z128=_, z130=_, z129=_):
    """[Execution] OBJ running on a stone statue switch
    z127: Active OBJ instance ID
    z131: OBJ state ID during operation
    z132: End of operation OBJ state ID
    z128: Switch OBJ instance ID
    z130: Passable navigation change point ID
    z129: Non-passable navigation change point ID
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z128, 70)
    """State 5: weight"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 7: Change navigation"""
    AddNavimeshAttribute(z130, 2)
    AddNavimeshAttribute(z129, 2)
    """State 1: OBJ is in operation"""
    ChangeObjState(z127, z131)
    """State 3: Wait for OBJ operation to end"""
    CompareObjState(0, z127, z132, 0)
    assert ConditionGroup(0)
    """State 8: Change navigation_2"""
    AddNavimeshAttribute(z129, 2)
    DeleteNavimeshAttribute(z130, 2)
    """State 2: Switch back"""
    ChangeObjState(z128, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z128, 10, 0)
    assert ConditionGroup(0)
    """State 9: End state"""
    return 0

def event_m50_35_x166(z121=_):
    """[Execution] OBJ_ switch operating with stone statue switch
    z121: Switch OBJ instance ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z121, 80)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z121, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x167(z121=_, z120=_, z122=_):
    """[Reproduction] One version of OBJ_Navi running on a stone statue switch
    z121: Switch OBJ instance ID
    z120: Active OBJ instance ID
    z122: Navigation change point ID
    """
    """State 0,3: OBJ status judgment"""
    if CompareObjStateId(z120, 70, 0):
        """State 7,10: Change navigation_3"""
        AddNavimeshAttribute(z122, 2)
        """State 11: OBJ operation waiting"""
        assert CompareObjStateId(z120, 30, 0)
        """State 14: Change navigation_5"""
        DeleteNavimeshAttribute(z122, 2)
    elif CompareObjStateId(z120, 80, 0):
        """State 6,12: Change navigation_4"""
        AddNavimeshAttribute(z122, 2)
        """State 13: OBJ waiting_2"""
        assert CompareObjStateId(z120, 10, 0)
        """State 15: Change navigation_6"""
        AddNavimeshAttribute(z122, 2)
    elif CompareObjStateId(z120, 10, 0):
        """State 4,8: Change navigation"""
        AddNavimeshAttribute(z122, 2)
    elif CompareObjStateId(z120, 30, 0):
        """State 5,9: Change navigation_2"""
        DeleteNavimeshAttribute(z122, 2)
    """State 16: Is the switch in the initial state?"""
    if CompareObjStateId(z121, 10, 0):
        pass
    else:
        """State 17: Is the switch descending?"""
        if CompareObjStateId(z121, 70, 0):
            """State 18: Wait for switch to fall"""
            assert CompareObjStateId(z121, 30, 0)
        else:
            pass
        """State 1: Return only the switch"""
        ChangeObjState(z121, 80)
        """State 2: Wait for switch to finish"""
        assert CompareObjStateId(z121, 10, 0)
    """State 19: End state"""
    return 0

def event_m50_35_x168(z120=_, z123=_, z124=_, z121=_, z122=_, z125=_, z126=_):
    """[Execution] One version of OBJ_Navi running on a stone statue switch
    z120: Active OBJ instance ID
    z123: OBJ state ID during operation
    z124: End of operation OBJ state ID
    z121: Switch OBJ instance ID
    z122: Navigation change point ID
    z125: Navigation additional attributes
    z126: Navi delete attribute
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z121, 70)
    """State 5: weight"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 7: Change navigation"""
    AddNavimeshAttribute(z122, 2)
    """State 1: OBJ is in operation"""
    ChangeObjState(z120, z123)
    """State 3: Wait for OBJ operation to end"""
    CompareObjState(0, z120, z124, 0)
    assert ConditionGroup(0)
    """State 8: Change navigation_2"""
    AddNavimeshAttribute(z122, z125)
    DeleteNavimeshAttribute(z122, z126)
    """State 2: Switch back"""
    ChangeObjState(z121, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z121, 10, 0)
    assert ConditionGroup(0)
    """State 9: End state"""
    return 0

def event_m50_35_x169(z120=_, z121=_, z122=_):
    """[Preset] One version of OBJ_Navi running on a stone statue switch
    z120: Active OBJ instance ID
    z121: Switch OBJ instance ID
    z122: Navigation change point ID
    """
    """State 0,4: [Reproduction] OBJ_Navi 1 version _SubState running on stone statue switch"""
    assert event_m50_35_x167(z121=z121, z120=z120, z122=z122)
    """State 2: [Condition] OBJ_SubState running on stone statue switch"""
    call = event_m50_35_x164(z121=z121, z120=z120)
    if call.Get() == 3:
        """State 1: [Execution] OBJ_Switch_Return_SubState running on the stone statue switch"""
        assert event_m50_35_x166(z121=z121)
    elif call.Get() == 2:
        """State 3: [Execution] OBJ_Switch that works with the stone statue switch_2_SubState"""
        assert event_m50_35_x166(z121=z121)
    elif call.Get() == 0:
        """State 5: [Execution] OBJ_Navigation 1 version_SubState running on the stone statue switch"""
        assert event_m50_35_x168(z120=z120, z123=70, z124=30, z121=z121, z122=z122, z125=0, z126=2)
    elif call.Get() == 1:
        """State 6: [Execution] One version of OBJ_Navi running on stone switch_2_SubState"""
        assert event_m50_35_x168(z120=z120, z123=80, z124=10, z121=z121, z122=z122, z125=2, z126=0)
    """State 7: End state"""
    return 0

def event_m50_35_x170(z118=50353409, z117=50351215, z119=32):
    """[Reproduction] Door rotated by switch _135 degree version
    z118: Switch OBJ instance ID
    z117: Revolving door OBJ instance ID
    z119: Initial state OBJ state ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z117, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z117, z119)
        assert CompareObjStateId(z117, z119, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z118, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z118, 10, 0)
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 10, 0):
        Goto('L0')
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 32, 0):
        Goto('L0')
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 34, 0):
        Goto('L0')
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 40, 0):
        Goto('L0')
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 41, 0):
        Goto('L0')
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 42, 0):
        Goto('L0')
    elif CompareObjStateId(z118, 30, 0) and CompareObjStateId(z117, 43, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x171(z118=50353409, z117=50351215):
    """[Condition] Door rotated by switch _135 degree version
    z118: Switch OBJ instance ID
    z117: Revolving door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z117, 10, 0)
    CompareObjState(1, z117, 41, 0)
    CompareObjState(2, z117, 30, 0)
    CompareObjState(3, z117, 40, 0)
    CompareObjState(4, z117, 32, 0)
    CompareObjState(5, z117, 43, 0)
    CompareObjState(6, z117, 34, 0)
    CompareObjState(7, z117, 42, 0)
    CompareObjState(8, z117, 80, 0)
    CompareObjState(9, z117, 83, 0)
    CompareObjState(10, z117, 86, 0)
    CompareObjState(11, z117, 81, 0)
    CompareObjState(12, z117, 84, 0)
    CompareObjState(13, z117, 87, 0)
    CompareObjState(14, z117, 82, 0)
    CompareObjState(15, z117, 85, 0)
    if ConditionGroup(8):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z117, 40, 0)
        assert ConditionGroup(0)
        """State 38: Upper right: Switch back"""
        return 4
    elif ConditionGroup(9):
        """State 22,30: Waiting for door to finish operation_5"""
        CompareObjState(0, z117, 32, 0)
        assert ConditionGroup(0)
        """State 45: Right: Switch back"""
        return 11
    elif ConditionGroup(10):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z117, 43, 0)
        assert ConditionGroup(0)
        """State 39: Lower right: Switch back"""
        return 5
    elif ConditionGroup(11):
        """State 23,31: Waiting for the door to finish operation_6"""
        CompareObjState(0, z117, 34, 0)
        assert ConditionGroup(0)
        """State 46: Bottom: Switch back"""
        return 12
    elif ConditionGroup(12):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z117, 42, 0)
        assert ConditionGroup(0)
        """State 40: Lower left: Switch back"""
        return 6
    elif ConditionGroup(13):
        """State 24,32: Waiting for the door to finish operation_7"""
        CompareObjState(0, z117, 10, 0)
        assert ConditionGroup(0)
        """State 47: Left: Switch back"""
        return 13
    elif ConditionGroup(14):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z117, 41, 0)
        assert ConditionGroup(0)
        """State 41: Upper left: Switch back"""
        return 7
    elif ConditionGroup(15):
        """State 25,33: Waiting for the door to finish operation_8"""
        CompareObjState(0, z117, 30, 0)
        assert ConditionGroup(0)
        """State 48: Top: Switch back"""
        return 14
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 34: Door from left to top right"""
        return 0
    elif ConditionGroup(1):
        """State 18,26: Switch judgment_5"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 42: Door from upper left to right"""
        return 8
    elif ConditionGroup(2):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 35: Door from top to bottom right"""
        return 1
    elif ConditionGroup(3):
        """State 19,27: Switch judgment_6"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 43: Door from top right to bottom"""
        return 9
    elif ConditionGroup(4):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 36: Door from right to bottom left"""
        return 2
    elif ConditionGroup(5):
        """State 20,28: Switch judgment_7"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 44: Door from lower right to left"""
        return 10
    elif ConditionGroup(6):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 37: Door from bottom to top left"""
        return 3
    elif ConditionGroup(7):
        """State 21,29: Switch judgment_8"""
        IsObjDamaged(0, z118, -1, -4, 0)
        CompareObjState(0, z118, 30, 0)
        assert ConditionGroup(0)
        """State 49: Door from bottom left to top"""
        return 15

def event_m50_35_x172(z117=50351215, z118=50353409, z119=32):
    """[Preset] Rotating door with switch _135 degree version
    z117: Revolving door OBJ instance ID
    z118: Switch OBJ instance ID
    z119: Initial state OBJ state ID
    """
    """State 0,1: [Reproduction] Door rotating with switch _135 degree version_SubState"""
    assert event_m50_35_x170(z118=z118, z117=z117, z119=z119)
    """State 4: [Condition] Door rotated by switch_135 degree version_SubState"""
    call = event_m50_35_x171(z118=z118, z117=z117)
    if call.Get() == 0:
        """State 2: [Execution] Door rotated by switch_SubState"""
        assert event_m50_35_x49(z117=z117, z226=80, z227=40, z118=z118, z228=80, z229=10)
    elif call.Get() == 8:
        """State 5: [Execution] Door rotated by switch_2_SubState"""
        assert event_m50_35_x49(z117=z117, z226=83, z227=32, z118=z118, z228=80, z229=10)
    elif call.Get() == 1:
        """State 6: [Execution] Door rotated by switch_3_SubState"""
        assert event_m50_35_x49(z117=z117, z226=86, z227=43, z118=z118, z228=80, z229=10)
    elif call.Get() == 9:
        """State 7: [Execution] Door rotated by switch_4_SubState"""
        assert event_m50_35_x49(z117=z117, z226=81, z227=34, z118=z118, z228=80, z229=10)
    elif call.Get() == 2:
        """State 8: [Execution] Door rotated by switch_5_SubState"""
        assert event_m50_35_x49(z117=z117, z226=84, z227=42, z118=z118, z228=80, z229=10)
    elif call.Get() == 10:
        """State 9: [Execution] Door rotated by switch_6_SubState"""
        assert event_m50_35_x49(z117=z117, z226=87, z227=10, z118=z118, z228=80, z229=10)
    elif call.Get() == 3:
        """State 10: [Execution] Door rotated by switch_7_SubState"""
        assert event_m50_35_x49(z117=z117, z226=82, z227=41, z118=z118, z228=80, z229=10)
    elif call.Get() == 15:
        """State 11: [Execution] Door rotated by switch_8_SubState"""
        assert event_m50_35_x49(z117=z117, z226=85, z227=30, z118=z118, z228=80, z229=10)
    elif call.Get() == 13:
        """State 3: [Execution] Door revolving with switch_Return switch_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 7:
        """State 12: [Execution] Door revolving with switch_Return switch_2_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 14:
        """State 13: [Execution] Door rotated by switch_Switch return_3_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 4:
        """State 14: [Execution] Door rotated by switch_Switch return_4_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 11:
        """State 15: [Execution] Door rotated by switch_Switch return_5_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 5:
        """State 16: [Execution] Door rotated by switch_Switch return_6_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 12:
        """State 17: [Execution] Door revolving with switch_Return switch_7_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    elif call.Get() == 6:
        """State 18: [Execution] Door revolving with switch_Switch return_8_SubState"""
        assert event_m50_35_x51(z118=z118, z224=80, z225=10)
    """State 19: End state"""
    return 0

def event_m50_35_x173(z114=_, z115=_):
    """[Reproduction] Navigation changes between buildings
    z114: Navigation change point_on
    z115: Navigation change point under
    """
    """State 0,1: Navi mesh switching: Not allowed"""
    AddNavimeshAttribute(z114, 2)
    AddNavimeshAttribute(z115, 2)
    """State 2: End state"""
    return 0

def event_m50_35_x174(z112=_, z113=_):
    """[Condition] Change navigation between buildings
    z112: Building OBJ① Instance ID
    z113: Building OBJ② Instance ID
    """
    """State 0,1: Judgment of building condition"""
    CompareObjState(8, z112, 10, 0)
    CompareObjState(8, z113, 10, 0)
    CompareObjState(9, z112, 30, 0)
    CompareObjState(9, z113, 30, 0)
    if ConditionGroup(8):
        """State 3: Both buildings are below"""
        return 1
    elif ConditionGroup(9):
        """State 2: Both buildings are on"""
        return 0

def event_m50_35_x175(z112=_, z113=_, z115=_, z114=_, z116=_):
    """[Execution] Navigation changes between buildings
    z112: Building OBJ① Instance ID
    z113: Building OBJ② Instance ID
    z115: Passable point
    z114: Impassable points
    z116: Building stop OBJ state ID
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z115, 2)
    AddNavimeshAttribute(z114, 2)
    """State 2: Building operation standby"""
    CompareObjState(0, z112, z116, 1)
    CompareObjState(0, z113, z116, 1)
    assert ConditionGroup(0)
    """State 3: Finish"""
    return 0

def event_m50_35_x176(z112=_, z113=_, z114=_, z115=_):
    """[Preset] Change navigation between buildings
    z112: Building OBJ① Instance ID
    z113: Building OBJ② Instance ID
    z114: Navigation change point_on
    z115: Navigation change point under
    """
    """State 0,1: [Reproduction] Navigation change between buildings_SubState"""
    assert event_m50_35_x173(z114=z114, z115=z115)
    """State 3: [Condition] Change navigation between buildings_SubState"""
    call = event_m50_35_x174(z112=z112, z113=z113)
    if call.Get() == 1:
        """State 2: [Execution] Change navigation between buildings_SubState"""
        assert event_m50_35_x175(z112=z112, z113=z113, z115=z115, z114=z114, z116=10)
    elif call.Get() == 0:
        """State 4: [Execution] Navigation change between buildings_2_SubState"""
        assert event_m50_35_x175(z112=z112, z113=z113, z115=z114, z114=z115, z116=30)
    """State 5: Rerun"""
    return 0

def event_m50_35_x177(z8=900):
    """[Condition] Queen's enemy summons
    z8: Boss generator ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Queen's Summoning Action Judgment"""
        CompareChrEzStateValue(8, z8, 6, 0, 1)
        CompareChrEzStateValue(8, z8, 7, 1, 0)
        IsChrDead(0, z8)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Flag reset"""
            SetEventFlag(535020001, 0)
            SetEventFlag(535020002, 0)
            SetEventFlag(535020003, 0)
            SetEventFlag(535020004, 0)
            SetEventFlag(535020005, 0)
            SetEventFlag(535020006, 0)
            """State 20: Character survival judgment_SubState"""
            assert event_m50_35_x180()
            """State 4: Lottery branch from survival results"""
            CompareEventFlag(8, 535020004, 1)
            CompareEventFlag(8, 535020005, 1)
            CompareEventFlag(8, 535020006, 1)
            CompareEventFlag(9, 535020004, 1)
            CompareEventFlag(9, 535020005, 1)
            CompareEventFlag(9, 535020006, 0)
            CompareEventFlag(10, 535020004, 0)
            CompareEventFlag(10, 535020005, 1)
            CompareEventFlag(10, 535020006, 1)
            CompareEventFlag(11, 535020004, 1)
            CompareEventFlag(11, 535020005, 0)
            CompareEventFlag(11, 535020006, 1)
            CompareEventFlag(12, 535020004, 1)
            CompareEventFlag(12, 535020005, 0)
            CompareEventFlag(12, 535020006, 0)
            CompareEventFlag(13, 535020004, 0)
            CompareEventFlag(13, 535020005, 1)
            CompareEventFlag(13, 535020006, 0)
            CompareEventFlag(14, 535020004, 0)
            CompareEventFlag(14, 535020005, 0)
            CompareEventFlag(14, 535020006, 1)
            CompareEventFlag(15, 535020004, 0)
            CompareEventFlag(15, 535020005, 0)
            CompareEventFlag(15, 535020006, 0)
            if ConditionGroup(15):
                """State 9: Multi-person determination"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 16: Random number generation from 3 lotteries"""
                    assert event_m50_35_x178(z109=0, z110=69, z111=99)
                    """State 14: Guest waiting"""
                    Label('L0')
                    SetConditionGroupTrue(0)
                    assert HostConditionGroup(0)
                    """State 8: Win flag determination"""
                    CompareEventFlag(0, 535020001, 1)
                    CompareEventFlag(8, 535020002, 1)
                    CompareMultiplayerPlayerCount(8, 1, 1, 0, 0)
                    CompareEventFlag(9, 535020002, 1)
                    CompareMultiplayerPlayerCount(9, 1, 1, 1, 0)
                    CompareEventFlag(10, 535020002, 1)
                    CompareMultiplayerPlayerCount(10, 1, 1, 2, 3)
                    CompareEventFlag(2, 535020003, 1)
                    IsChrDead(3, z8)
                    if HostConditionGroup(3):
                        pass
                    elif HostConditionGroup(0):
                        """State 31: 3 pigs"""
                        return 0
                    elif HostConditionGroup(8):
                        """State 33: 3 skeletons"""
                        return 2
                    elif HostConditionGroup(9):
                        """State 35: 4 skeletons"""
                        return 4
                    elif HostConditionGroup(10):
                        """State 36: 5 skeletons"""
                        return 5
                    elif HostConditionGroup(2):
                        """State 34: Queen Knight B"""
                        return 3
                elif ConditionGroup(1):
                    """State 21: Random number generation from 3 lotteries_all dead_2_SubState"""
                    assert event_m50_35_x178(z109=0, z110=50, z111=99)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 22: Random number generation to 3 lottery _ Everyone died _3_SubState"""
                    assert event_m50_35_x178(z109=0, z110=30, z111=99)
                    Goto('L0')
            elif ConditionGroup(8):
                """State 10: Multi-person determination_2"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 17: 3 random drawing from random number generation"""
                    assert event_m50_35_x178(z109=0, z110=69, z111=99)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 23: Random number generation to 3 lottery _ Survival of all _2 _ SubState"""
                    assert event_m50_35_x178(z109=0, z110=50, z111=99)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 24: Random number generation to 3 lottery _ survival_3_SubState"""
                    assert event_m50_35_x178(z109=0, z110=30, z111=99)
                    Goto('L0')
            elif ConditionGroup(14):
                """State 11: Multi-person determination_3"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 15: Random number generation from two lottery _ pig or skeleton _ SubState"""
                    assert event_m50_35_x179(z105=70, z106=0, z107=535020001, z108=535020002)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 25: Random number generator to lottery_pig or skeleton_2_SubState"""
                    assert event_m50_35_x179(z105=50, z106=0, z107=535020001, z108=535020002)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 26: Random number generation from 2 lottery_pig or skeleton_3_SubState"""
                    assert event_m50_35_x179(z105=30, z106=0, z107=535020001, z108=535020002)
                    Goto('L0')
            elif ConditionGroup(12):
                """State 12: Multi-person determination_4"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 18: Random number generation to draw 2 bodies_Skeleton or Queen Knight B_SubState"""
                    assert event_m50_35_x179(z105=99, z106=69, z107=535020002, z108=535020003)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 27: Random number generation from two lotteries_Skeleton or Queen Knight B_2_SubState"""
                    assert event_m50_35_x179(z105=99, z106=49, z107=535020002, z108=535020003)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 28: Random number generation from two bodies _ Skeleton or Queen Knight B_3_SubState"""
                    assert event_m50_35_x179(z105=99, z106=29, z107=535020002, z108=535020003)
                    Goto('L0')
            elif ConditionGroup(13):
                """State 13: Multi-person determination_5"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 19: Random number generation from two lottery _ Pig or Queen Knight B_SubState"""
                    assert event_m50_35_x179(z105=29, z106=0, z107=535020001, z108=535020003)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 29: Random number generation to draw 2 bodies _ Pig or Queen Knight B_2_SubState"""
                    assert event_m50_35_x179(z105=49, z106=0, z107=535020001, z108=535020003)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 30: Random number generation from two lottery _ Pig or Queen Knight B_3_SubState"""
                    assert event_m50_35_x179(z105=69, z106=0, z107=535020001, z108=535020003)
                    Goto('L0')
            elif ConditionGroup(10):
                """State 5: Pig winning"""
                SetEventFlag(535020001, 1)
                Goto('L0')
            elif ConditionGroup(11):
                """State 6: Skeleton winning"""
                SetEventFlag(535020002, 1)
                Goto('L0')
            elif ConditionGroup(9):
                """State 7: Queen Knight B won"""
                SetEventFlag(535020003, 1)
                Goto('L0')
    else:
        Goto('L0')
    """State 32: Defeat the boss"""
    return 1

def event_m50_35_x178(z109=0, z110=_, z111=99):
    """Three lottery from random number generation
    z109: Pig random_comparison value
    z110: Bone random number_comparison value
    z111: Knight random number_comparison value
    """
    """State 0,2: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 1: Character lottery"""
    CompareEventRandValue(0, 0, z109, 5)
    CompareEventRandValue(1, 0, z110, 5)
    CompareEventRandValue(2, 0, z111, 5)
    if ConditionGroup(0):
        """State 3: Pig winning"""
        SetEventFlag(535020001, 1)
        assert GetEventFlag(535020001) != 0
    elif ConditionGroup(1):
        """State 4: Skeleton winning"""
        SetEventFlag(535020002, 1)
        assert GetEventFlag(535020002) != 0
    elif ConditionGroup(2):
        """State 5: Queen Knight B won"""
        SetEventFlag(535020003, 1)
        assert GetEventFlag(535020003) != 0
    """State 6: End state"""
    return 0

def event_m50_35_x179(z105=_, z106=_, z107=_, z108=_):
    """Two lottery from random number generation
    z105: Random_max
    z106: Random number_1 comparison value
    z107: Winning A flag
    z108: Winning B flag
    """
    """State 0,2: Random number generation"""
    GenerateRandomNumber(0, 0, z105)
    """State 1: Character lottery"""
    CompareEventRandValue(0, 0, z106, 5)
    CompareEventRandValue(1, 0, z105, 5)
    if ConditionGroup(0):
        """State 3: Chara A winning"""
        SetEventFlag(z107, 1)
        assert GetEventFlag(z107) != 0
    elif ConditionGroup(1):
        """State 4: Chara B winning"""
        SetEventFlag(z108, 1)
        assert GetEventFlag(z108) != 0
    """State 5: End state"""
    return 0

def event_m50_35_x180():
    """Character survival judgment"""
    """State 0,1: Pig presence determination"""
    IsChrActive(0, 8503, 1)
    IsChrActive(0, 8504, 1)
    IsChrActive(0, 8505, 1)
    if ConditionGroup(0):
        """State 2: Pig presence flag ON"""
        SetEventFlag(535020004, 1)
        assert GetEventFlag(535020004) != 0
    else:
        pass
    """State 4: Skeleton presence determination"""
    IsChrActive(0, 8500, 1)
    IsChrActive(0, 8501, 1)
    IsChrActive(0, 8502, 1)
    IsChrActive(0, 8507, 1)
    IsChrActive(0, 8508, 1)
    if ConditionGroup(0):
        """State 3: Skeleton presence flag ON"""
        SetEventFlag(535020005, 1)
        assert GetEventFlag(535020005) != 0
    else:
        pass
    """State 6: Queen Knight B Existence Determination"""
    IsChrActive(0, 8506, 1)
    if ConditionGroup(0):
        """State 5: Queen Knight B presence flag ON"""
        SetEventFlag(535020006, 1)
        assert GetEventFlag(535020006) != 0
    else:
        pass
    """State 7: End state"""
    return 0

def event_m50_35_x181(z8=900, z9=50001000, z10=50001039):
    """[Preset] Queen's enemy summons
    z8: Boss generator ID
    z9: Start point ID
    z10: End point ID
    """
    """State 0,1: [Reproduction] Queen's enemy summon _SubState"""
    assert event_m50_35_x103()
    """State 3: [Condition] Queen's Enemy Summoning_No Duplicate Version_SubState"""
    call = event_m50_35_x177(z8=z8)
    if call.Get() == 0:
        """State 5: [Execution] Queen's enemy summon _3 body version_pig_SubState"""
        assert event_m50_35_x228(z8=z8, z46=8503, z47=8504, z48=8505, z9=z9, z10=z10, z49=70)
    elif call.Get() == 2:
        """State 6: [Execution] Queen's enemy summon _3 body version_Skeleton_SubState"""
        assert event_m50_35_x228(z8=z8, z46=8500, z47=8501, z48=8502, z9=z9, z10=z10, z49=71)
    elif call.Get() == 4:
        """State 7: [Execution] Queen's enemy summon _4 body version_Skeleton_SubState"""
        assert event_m50_35_x247(z8=z8, z16=8500, z17=8501, z18=8502, z9=z9, z10=z10, z19=71, z20=8507)
    elif call.Get() == 5:
        """State 8: [Execution] Queen's enemy summon _5 body version_Skeleton_SubState"""
        assert event_m50_35_x248(z8=z8, z11=8500, z12=8501, z13=8502, z9=z9, z10=z10, z14=8507, z15=8508)
    elif call.Get() == 3:
        """State 4: [Execution] Queen's Enemy Summon _1 body_Queen's Knight B_SubState"""
        assert event_m50_35_x227(z8=z8, z50=8506, z9=z9, z10=z10, z51=72)
    elif call.Get() == 1:
        """State 2: [Execution] Queen's Enemy Summoning_Enemy Death_SubState"""
        assert event_m50_35_x152(z144=8503, z145=8504, z146=8505, z147=8500, z148=8501, z149=8502, z150=8506)
        """State 9: Defeat Boss: Finish"""
        return 0
    """State 10: Rerun"""
    return 1

def event_m50_35_x182(z95=50351213, z97=32, z96=50353410, z98=50353412):
    """[Reproduction] Door rotated by switch_Two switches version
    z95: Revolving door OBJ instance ID
    z97: Initial state OBJ state ID
    z96: Switch ① OBJ instance ID
    z98: Switch ②OBJ instance ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z95, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z95, z97)
        assert CompareObjStateId(z95, z97, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z96, 30, 0) and CompareObjStateId(z95, 30, 0) and CompareObjStateId(z98, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z96, 80)
        ChangeObjState(z98, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z96, 10, 0) and CompareObjStateId(z98, 10, 0)
    elif CompareObjStateId(z96, 30, 0) and CompareObjStateId(z95, 10, 0) and CompareObjStateId(z98, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z96, 30, 0) and CompareObjStateId(z95, 32, 0) and CompareObjStateId(z98, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z96, 30, 0) and CompareObjStateId(z95, 34, 0) and CompareObjStateId(z98, 30, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x183(z96=50353410, z95=50351213, z98=50353412):
    """[Condition] Door rotated by switch_Two-switch version
    z96: Switch ① OBJ instance ID
    z95: Revolving door OBJ instance ID
    z98: Switch ②OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z95, 10, 0)
    CompareObjState(1, z95, 30, 0)
    CompareObjState(2, z95, 32, 0)
    CompareObjState(3, z95, 34, 0)
    CompareObjState(4, z95, 70, 0)
    CompareObjState(5, z95, 72, 0)
    CompareObjState(6, z95, 74, 0)
    CompareObjState(7, z95, 76, 0)
    if ConditionGroup(4):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z95, 30, 0)
        assert ConditionGroup(0)
        """State 22: Top: Switch back"""
        return 4
    elif ConditionGroup(5):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z95, 32, 0)
        assert ConditionGroup(0)
        """State 23: Right: Switch back"""
        return 5
    elif ConditionGroup(6):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z95, 34, 0)
        assert ConditionGroup(0)
        """State 24: Bottom: Switch back"""
        return 6
    elif ConditionGroup(7):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z95, 10, 0)
        assert ConditionGroup(0)
        """State 25: Left: Switch back"""
        return 7
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z96, -1, -4, 0)
        CompareObjState(0, z96, 30, 0)
        IsObjDamaged(0, z98, -1, -4, 0)
        CompareObjState(0, z98, 30, 0)
        assert ConditionGroup(0)
        """State 18: Door up from left"""
        return 0
    elif ConditionGroup(1):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z96, -1, -4, 0)
        CompareObjState(0, z96, 30, 0)
        IsObjDamaged(0, z98, -1, -4, 0)
        CompareObjState(0, z98, 30, 0)
        assert ConditionGroup(0)
        """State 19: Door from top to right"""
        return 1
    elif ConditionGroup(2):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z96, -1, -4, 0)
        CompareObjState(0, z96, 30, 0)
        IsObjDamaged(0, z98, -1, -4, 0)
        CompareObjState(0, z98, 30, 0)
        assert ConditionGroup(0)
        """State 20: Door from right to bottom"""
        return 2
    elif ConditionGroup(3):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z96, -1, -4, 0)
        CompareObjState(0, z96, 30, 0)
        IsObjDamaged(0, z98, -1, -4, 0)
        CompareObjState(0, z98, 30, 0)
        assert ConditionGroup(0)
        """State 21: Door from bottom to left"""
        return 3

def event_m50_35_x184(z91=_, z101=_, z102=_, z92=_, z103=80, z104=10, z94=_):
    """[Execution] Door rotated by switch_Two switches version
    z91: Revolving door OBJ instance ID
    z101: Pillar operation OBJ state ID
    z102: OBJ state ID for which the column has ended
    z92: Switch ① OBJ instance ID
    z103: Switch operation OBJ state ID
    z104: Switch operation end OBJ state ID
    z94: Switch ②OBJ instance ID
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z92, 70)
    ChangeObjState(z94, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z92, 30, 0)
    CompareObjState(0, z94, 30, 0)
    assert ConditionGroup(0)
    """State 1: The door rotates"""
    ChangeObjState(z91, z101)
    """State 3: Waiting for the column to finish operation"""
    CompareObjState(0, z91, z102, 0)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z92, z103)
    ChangeObjState(z94, z103)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z92, z104, 0)
    CompareObjState(0, z94, z104, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_35_x185(z95=50351213, z96=50353410, z97=32, z98=50353412):
    """[Preset] Rotating door with switch_Two-switch version
    z95: Revolving door OBJ instance ID
    z96: Switch ① OBJ instance ID
    z97: Initial state OBJ state ID
    z98: Switch ②OBJ instance ID
    """
    """State 0,1: [Reproduction] Door rotating with switch_Two switches_SubState"""
    assert event_m50_35_x182(z95=z95, z97=z97, z96=z96, z98=z98)
    """State 3: [Condition] Door rotated by switch_Two switches_SubState"""
    call = event_m50_35_x183(z96=z96, z95=z95, z98=z98)
    if call.Get() == 0:
        """State 2: [Execution] Door that rotates with switch_Two switches_SubState"""
        assert event_m50_35_x184(z91=z95, z101=70, z102=30, z92=z96, z103=80, z104=10, z94=z98)
    elif call.Get() == 1:
        """State 5: [Execution] Door rotated by switch_Two switch version_2_SubState"""
        assert event_m50_35_x184(z91=z95, z101=72, z102=32, z92=z96, z103=80, z104=10, z94=z98)
    elif call.Get() == 2:
        """State 6: [Execution] Door rotated by switch_Two switches_3_SubState"""
        assert event_m50_35_x184(z91=z95, z101=74, z102=34, z92=z96, z103=80, z104=10, z94=z98)
    elif call.Get() == 3:
        """State 7: [Execution] Door rotated by switch_Two switches_4_SubState"""
        assert event_m50_35_x184(z91=z95, z101=76, z102=10, z92=z96, z103=80, z104=10, z94=z98)
    elif call.Get() == 4:
        """State 4: [Execution] Door rotated by switch_Return switch_Two switches_SubState"""
        assert event_m50_35_x186(z92=z96, z99=80, z100=10, z94=z98)
    elif call.Get() == 5:
        """State 8: [Execution] Door rotated by switch_Return switch_Two switch version_2_SubState"""
        assert event_m50_35_x186(z92=z96, z99=80, z100=10, z94=z98)
    elif call.Get() == 6:
        """State 9: [Execution] Door rotated by switch_Switch return_Two switch version_3_SubState"""
        assert event_m50_35_x186(z92=z96, z99=80, z100=10, z94=z98)
    elif call.Get() == 7:
        """State 10: [Execution] Door that rotates with switch_Return switch_Two switches_4_SubState"""
        assert event_m50_35_x186(z92=z96, z99=80, z100=10, z94=z98)
    """State 11: End state"""
    return 0

def event_m50_35_x186(z92=_, z99=80, z100=10, z94=_):
    """[Execution] Door rotated by switch_Switch return_Two switch version
    z92: Switch ① OBJ instance ID
    z99: Switch operation OBJ state ID
    z100: Switch operation end OBJ state ID
    z94: Switch ②OBJ instance ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z92, z99)
    ChangeObjState(z94, z99)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z92, z100, 0)
    CompareObjState(0, z94, z100, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x187(z92=50353409, z91=50351215, z93=32, z94=50353411):
    """[Reproduction] Door rotating with switch _135 degree version_Two switch version
    z92: Switch ① OBJ instance ID
    z91: Revolving door OBJ instance ID
    z93: Initial state OBJ state ID
    z94: Switch ②OBJ instance ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z91, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z91, z93)
        assert CompareObjStateId(z91, z93, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 30, 0) and CompareObjStateId(z94, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z92, 80)
        ChangeObjState(z94, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z92, 10, 0) and CompareObjStateId(z94, 10, 0)
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 10, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 32, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 34, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 40, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 41, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 42, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z92, 30, 0) and CompareObjStateId(z91, 43, 0) and CompareObjStateId(z94, 30, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x188(z92=50353409, z91=50351215, z94=50353411):
    """[Condition] Door rotated by switch_135 degree version_Two switch version
    z92: Switch ① OBJ instance ID
    z91: Revolving door OBJ instance ID
    z94: Switch ②OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z91, 10, 0)
    CompareObjState(1, z91, 41, 0)
    CompareObjState(2, z91, 30, 0)
    CompareObjState(3, z91, 40, 0)
    CompareObjState(4, z91, 32, 0)
    CompareObjState(5, z91, 43, 0)
    CompareObjState(6, z91, 34, 0)
    CompareObjState(7, z91, 42, 0)
    CompareObjState(8, z91, 80, 0)
    CompareObjState(9, z91, 83, 0)
    CompareObjState(10, z91, 86, 0)
    CompareObjState(11, z91, 81, 0)
    CompareObjState(12, z91, 84, 0)
    CompareObjState(13, z91, 87, 0)
    CompareObjState(14, z91, 82, 0)
    CompareObjState(15, z91, 85, 0)
    if ConditionGroup(8):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z91, 40, 0)
        assert ConditionGroup(0)
        """State 38: Upper right: Switch back"""
        return 4
    elif ConditionGroup(9):
        """State 22,30: Waiting for door to finish operation_5"""
        CompareObjState(0, z91, 32, 0)
        assert ConditionGroup(0)
        """State 45: Right: Switch back"""
        return 11
    elif ConditionGroup(10):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z91, 43, 0)
        assert ConditionGroup(0)
        """State 39: Lower right: Switch back"""
        return 5
    elif ConditionGroup(11):
        """State 23,31: Waiting for the door to finish operation_6"""
        CompareObjState(0, z91, 34, 0)
        assert ConditionGroup(0)
        """State 46: Bottom: Switch back"""
        return 12
    elif ConditionGroup(12):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z91, 42, 0)
        assert ConditionGroup(0)
        """State 40: Lower left: Switch back"""
        return 6
    elif ConditionGroup(13):
        """State 24,32: Waiting for the door to finish operation_7"""
        CompareObjState(0, z91, 10, 0)
        assert ConditionGroup(0)
        """State 47: Left: Switch back"""
        return 13
    elif ConditionGroup(14):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z91, 41, 0)
        assert ConditionGroup(0)
        """State 41: Upper left: Switch back"""
        return 7
    elif ConditionGroup(15):
        """State 25,33: Waiting for the door to finish operation_8"""
        CompareObjState(0, z91, 30, 0)
        assert ConditionGroup(0)
        """State 48: Top: Switch back"""
        return 14
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 34: Door from left to top right"""
        return 0
    elif ConditionGroup(1):
        """State 18,26: Switch judgment_5"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 42: Door from upper left to right"""
        return 8
    elif ConditionGroup(2):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 35: Door from top to bottom right"""
        return 1
    elif ConditionGroup(3):
        """State 19,27: Switch judgment_6"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 43: Door from top right to bottom"""
        return 9
    elif ConditionGroup(4):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 36: Door from right to bottom left"""
        return 2
    elif ConditionGroup(5):
        """State 20,28: Switch judgment_7"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 44: Door from lower right to left"""
        return 10
    elif ConditionGroup(6):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 37: Door from bottom to top left"""
        return 3
    elif ConditionGroup(7):
        """State 21,29: Switch judgment_8"""
        IsObjDamaged(0, z92, -1, -4, 0)
        CompareObjState(0, z92, 30, 0)
        IsObjDamaged(0, z94, -1, -4, 0)
        CompareObjState(0, z94, 30, 0)
        assert ConditionGroup(0)
        """State 49: Door from bottom left to top"""
        return 15

def event_m50_35_x189(z91=50351215, z92=50353409, z93=32, z94=50353411):
    """[Preset] Rotating door with switch_135 degree version_Two switch version
    z91: Revolving door OBJ instance ID
    z92: Switch ① OBJ instance ID
    z93: Initial state OBJ state ID
    z94: Switch ②OBJ instance ID
    """
    """State 0,4: [Reproduction] Door that rotates with switch_135 degree version_Two switch version_SubState"""
    assert event_m50_35_x187(z92=z92, z91=z91, z93=z93, z94=z94)
    """State 3: [Condition] Door rotated by switch_135 degree version_Two switch version_SubState"""
    call = event_m50_35_x188(z92=z92, z91=z91, z94=z94)
    if call.Get() == 0:
        """State 1: [Execution] Door that rotates with switch_Two switches_SubState"""
        assert event_m50_35_x184(z91=z91, z101=80, z102=40, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 8:
        """State 5: [Execution] Door rotated by switch_Two switch version_2_SubState"""
        assert event_m50_35_x184(z91=z91, z101=83, z102=32, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 1:
        """State 6: [Execution] Door rotated by switch_Two switches_3_SubState"""
        assert event_m50_35_x184(z91=z91, z101=86, z102=43, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 9:
        """State 7: [Execution] Door rotated by switch_Two switches_4_SubState"""
        assert event_m50_35_x184(z91=z91, z101=81, z102=34, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 2:
        """State 8: [Execution] Door rotated by switch_Two switches_5_SubState"""
        assert event_m50_35_x184(z91=z91, z101=84, z102=42, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 10:
        """State 9: [Execution] Rotating door with switch_Two switches_6_SubState"""
        assert event_m50_35_x184(z91=z91, z101=87, z102=10, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 3:
        """State 10: [Execution] Door rotated by switch_Two switches_7_SubState"""
        assert event_m50_35_x184(z91=z91, z101=82, z102=41, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Get() == 15:
        """State 11: [Execution] Door that rotates with switch_Two switches_8_SubState"""
        assert event_m50_35_x184(z91=z91, z101=85, z102=30, z92=z92, z103=80, z104=10, z94=z94)
    elif call.Done():
        """State 2: [Execution] Door rotated by switch_Return switch_Two switches_SubState"""
        assert event_m50_35_x186(z92=z92, z99=80, z100=10, z94=z94)
    """State 12: End state"""
    return 0

def event_m50_35_x190(z88=535000081, z89=900):
    """[Reproduction] Queen's lines
    z88: Boss destruction flag
    z89: Generator ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Did you defeat the queen?"""
    if GetEventFlag(z88) != 0:
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Not defeated"""
        return 0
    """State 5: The guests"""
    Label('L0')
    return 2

def event_m50_35_x191(z86=5030000, z87=4.5):
    """[Condition] Queen's lines
    z86: Boss Battle ID
    z87: Weight to serif
    """
    """State 0,1: Has the boss battle started?"""
    IsEventBossBattle(0, z86, 1)
    assert ConditionGroup(0)
    """State 2: Weight to serif"""
    CompareStateTime(0, z87, 3, z87)
    IsEventBossKill(1, z86, 0, 1)
    if ConditionGroup(1):
        """State 4: Defeat the boss"""
        return 1
    elif ConditionGroup(0):
        """State 3: End state"""
        return 0

def event_m50_35_x192(z90=535020082):
    """[Execution] Queen's lines
    z90: Line flag
    """
    """State 0,1: Line flag ON"""
    SetEventFlag(z90, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x193(z86=5030000, z87=4.5, z88=535000081, z89=900, z90=535020082):
    """[Preset] Queen's lines
    z86: Boss Battle ID
    z87: Weight to serif
    z88: Boss destruction flag
    z89: Generator ID
    z90: Line flag
    """
    """State 0,1: [Reproduction] Queen's lines_SubState"""
    call = event_m50_35_x190(z88=z88, z89=z89)
    if call.Get() == 0:
        """State 3: [Condition] Queen's lines_SubState"""
        call = event_m50_35_x191(z86=z86, z87=z87)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Queen's lines_SubState"""
            assert event_m50_35_x192(z90=z90)
    elif call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x194(z78=535000096, z79=3403000):
    """[Reproduction] Filter change for Dragon Battle
    z78: Boss destruction flag
    z79: Change point ID
    """
    """State 0,2: Filter status judgment"""
    if (GetFogFilterOverride() == 7) != 0 and (GetParallelLightFilterOverride() == 7) != 0:
        """State 3: Pop fog and parallel light filter"""
        PopFogFilter(0)
        PopParallelLightFilter(0)
        """State 4: Waiting for pop"""
        assert (GetFogFilterOverride() == 7) != 1 and (GetParallelLightFilterOverride() == 7) != 1
    else:
        pass
    """State 1: Has the boss been destroyed?"""
    if GetEventFlag(z78) != 0:
        """State 6: Defeated"""
        return 1
    else:
        """State 5: Undefeated"""
        return 0

def event_m50_35_x195(z75=901, z76=3.3, z77=535020095):
    """[Condition] Change the filter of Dragon Battle
    z75: Generator ID
    z76: Adjustment weight
    z77: Boss activation flag
    """
    """State 0,1: Did the boss start?"""
    CompareEventFlag(0, z77, 1)
    assert ConditionGroup(0)
    """State 2: Adjustment weight"""
    CompareStateTime(0, z76, 3, z76)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x196(z79=3403000):
    """[Execution] Filter change for Dragon Battle
    z79: Change point ID
    """
    """State 0,5: Filter status judgment"""
    if (GetFogFilterOverride() == 7) != 1 and (GetParallelLightFilterOverride() == 7) != 1:
        """State 1: Push fog and parallel light filter"""
        PushFogFilter(7, 0)
        PushParallelLightFilter(7, 0)
        assert (GetFogFilterOverride() == 7) != 0 and (GetParallelLightFilterOverride() == 7) != 0
    else:
        pass
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z79, z79, 0)
    assert ConditionGroup(0)
    """State 3: Pop fog and parallel light filter"""
    PopFogFilter(0)
    PopParallelLightFilter(0)
    """State 4: Waiting for pop"""
    assert (GetFogFilterOverride() == 7) != 1 and (GetParallelLightFilterOverride() == 7) != 1
    """State 6: End state"""
    return 0

def event_m50_35_x197(z75=901, z76=3.3, z77=535020095, z78=535000096, z79=3403000):
    """[Preset] Change the Dragon Battle filter
    z75: Generator ID
    z76: Adjustment weight
    z77: Boss activation flag
    z78: Boss destruction flag
    z79: Change point ID
    """
    """State 0,1: [Reproduce] Change Dragon Battle Filter_SubState"""
    call = event_m50_35_x194(z78=z78, z79=z79)
    if call.Get() == 1:
        """State 7: [Conditions] Dragon Battle Filter Change_Point Judgment_2_SubState"""
        assert event_m50_35_x210(z79=z79, z80=1)
        """State 8: [Execution] Filter change for Dragon Battle_Sky_2_SubState"""
        assert event_m50_35_x212()
        """State 9: [Reproduction] Dragon Battle Filter Change_Sky_2_SubState"""
        assert event_m50_35_x211()
    elif call.Get() == 0:
        """State 6: [Condition] Change of Dragon Battle Filter_Point Judgment_SubState"""
        assert event_m50_35_x210(z79=z79, z80=1)
        """State 4: [Execution] Dragon Battle Filter Change_Sky_SubState"""
        assert event_m50_35_x212()
        """State 2: [Reproduction] Dragon Battle Filter Change_Sky_SubState"""
        assert event_m50_35_x211()
        """State 5: [Condition] Change filter of Dragon Battle_SubState"""
        assert event_m50_35_x195(z75=z75, z76=z76, z77=z77)
    """State 3: [Execution] Dragon Battle Filter Change_SubState"""
    assert event_m50_35_x196(z79=z79)
    """State 10: Rerun"""
    return 0

def event_m50_35_x198(z61=535000096):
    """[Reproduction] Poison Dragon Battle_Start
    z61: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z61) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_35_x199(z66=3400000, z85=3400000):
    """[Condition] Poison Dragon Battle_Start
    z66: Start point ID
    z85: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z66, z85, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z66, z85, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x200(z63=5030030):
    """[Execution] Poison Dragon Battle Start
    z63: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z63)
    """State 2: End state"""
    return 0

def event_m50_35_x201():
    """[Reproduction] Poison Dragon Battle_HP Display and BGM Playback_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x202(z62=502, z65=5.5, z63=5030030, z82=1, z83=535020097, z84=535020098):
    """[Execution] Poison Dragon Battle _HP display and BGM playback
    z62: Sound ID
    z65: Weight until BGM display
    z63: Boss Battle ID
    z82: Weight until HP display
    z83: BGM display flag
    z84: HP gauge display flag
    """
    """State 0,3: Wait until BGM playback"""
    CompareStateTime(0, z65, 2, z65)
    CompareEventFlag(0, z83, 1)
    IsEventBossKill(1, z63, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z62)
        """State 5: BGM display flag ON"""
        SetEventFlag(z83, 1)
        """State 4: Weight until HP display"""
        CompareStateTime(0, z82, 2, z82)
        CompareEventFlag(0, z84, 1)
        IsEventBossKill(1, z63, 0, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            pass
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 6: HP gauge display flag ON"""
    SetEventFlag(z84, 1)
    """State 7: End state"""
    return 0

def event_m50_35_x203():
    """[Reproduction] Poison Dragon Battle_HP Display and BGM Playback_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x204(z63=5030030):
    """[Condition] Poison Dragon Battle_HP Display and BGM Playback_End
    z63: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z63, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x205(z62=502, z63=5030030, z64=535020095, z81=0):
    """[Execution] Poison Dragon Battle_HP Display and BGM Playback_End
    z62: Sound ID
    z63: Boss Battle ID
    z64: Other flags for logic
    z81: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z64, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z63)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > 0) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z62)
    """State 5: End state"""
    return 0

def event_m50_35_x206(z68=3400010, z67=901, z64=535020095):
    """[Condition] Poison Dragon Battle_Start
    z68: Boss activation point ID
    z67: Generator ID
    z64: Logic flag
    """
    """State 0,1: Entered the activation point or dealt damage or activated or destroyed"""
    IsPlayerInsidePoint(0, z68, z68, 1)
    CompareChrHpRatio(0, z67, 100, 4)
    CompareEventFlag(0, z64, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x207(z64=535020095):
    """[Execution] Poison Dragon Battle _Start
    z64: Logic flag
    """
    """State 0,1: Logic flag ON"""
    SetEventFlag(z64, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x208():
    """Event not executed"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x209(z61=535000096, z62=502, z63=5030030, z64=535020095, z65=5.5, z66=3400000, z67=901,
                      z68=3400010):
    """[Preset] Poison Dragon Battle
    z61: Boss destruction flag
    z62: Sound ID
    z63: Boss Battle ID
    z64: Other flags for logic
    z65: Wait time
    z66: Start and end point ID
    z67: Boss generator ID
    z68: Boss activation point ID
    """
    """State 0,3: [Reproduction] Poison Dragon Battle_Start_SubState"""
    call = event_m50_35_x198(z61=z61)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 10: [Condition] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x199(z66=z66, z85=z66)
        """State 7: [Execution] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x200(z63=z63)
        """State 4: [Reproduction] Poison Dragon Battle_Start_Sky_SubState"""
        assert event_m50_35_x208()
        """State 11: [Condition] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x206(z68=z68, z67=z67, z64=z64)
        """State 8: [Execution] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x207(z64=z64)
        """State 1: [Reproduction] Poison Dragon Battle_HP Display and BGM Playback_Sky_SubState"""
        assert event_m50_35_x201()
        """State 12: [Condition] Poison Dragon Battle_HP Display and BGM Playback_Sky_SubState"""
        assert event_m50_35_x225()
        """State 5: [Execution] Poison Dragon Battle_HP Display and BGM Playback_SubState"""
        assert event_m50_35_x202(z62=z62, z65=z65, z63=z63, z82=1, z83=535020097, z84=535020098)
        """State 2: [Reproduction] Poison Dragon Battle_HP Display and BGM Playback_End_Sky_SubState"""
        assert event_m50_35_x203()
        """State 9: [Condition] Poison Dragon Battle_HP Display and BGM Playback_End_SubState"""
        assert event_m50_35_x204(z63=z63)
        """State 6: [Execution] Poison Dragon Battle_HP Display and BGM Playback_End_SubState"""
        assert event_m50_35_x205(z62=z62, z63=z63, z64=z64, z81=0)
    """State 13: End state"""
    return 0

def event_m50_35_x210(z79=3403000, z80=1):
    """[Condition] Filter change for dragon battle_Point judgment
    z79: Change point ID
    z80: Are you inside
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z79, z79, z80)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x211():
    """[Reproduction] Change of Dragon Battle Filter_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x212():
    """[Execution] Dragon Battle Filter Change_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x213():
    """[Execution] Door opened by destroying boss _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x214(z69=50352000, z70=5300000):
    """[Execution] Door opened with DLC purchase_Manual
    z69: Door OBJ instance ID
    z70: Navigation switching point ID
    """
    """State 0,3: Activate key guide"""
    DisableObjKeyGuide(z69, 0)
    """State 1: Waiting for the door to finish"""
    CompareObjState(0, z69, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation switching"""
    DeleteNavimeshAttribute(z70, 2)
    """State 4: End state"""
    return 0

def event_m50_35_x215(z2=535000036, z1=50356110):
    """[Reproduction] Crown that appears when a boss is destroyed
    z2: Crown acquisition flag
    z1: Crown OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you acquired the crown?"""
    if GetEventFlag(z2) != 1:
        """State 3: Hide crown"""
        ChangeObjState(z1, 10)
        assert CompareObjStateId(z1, 10, 0)
        """State 4: Waiting for appearance"""
        return 0
    else:
        """State 6: End: Hide"""
        return 2
    """State 5: Guest user"""
    Label('L0')
    return 1

def event_m50_35_x216():
    """[Reproduction] Crown that appears by destroying boss _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x217(z3=535000096):
    """[Condition] Crown that appears when a boss is destroyed
    z3: Defeat flag
    """
    """State 0,1: Did you defeat the poison dragon or become multiplayer?"""
    CompareEventFlag(0, 535000096, 1)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 2: Multi start: Waiting for end"""
        IsMultiplayer(0, 0, 0)
        assert ConditionGroup(0)
        """State 4: Multi-end: Re-execute"""
        return 1
    elif ConditionGroup(0):
        """State 3: Crown display"""
        return 0

def event_m50_35_x218(z1=50356110):
    """[Conditions] Examining the crown that appears when a boss is destroyed
    z1: Crown OBJ instance ID
    """
    """State 0,1: Did you check the crown or became a boss battle?"""
    IsObjSearched(0, z1)
    IsEventBossBattle(1, 5030030, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4: During the boss battle"""
    return 1
    """State 2: Can items be acquired?"""
    Label('L0')
    # goods:21650100:Crown of the Sunken King
    if CanGetItem(21650100, 1) != 0:
        """State 3: Item acquisition"""
        return 0
    else:
        """State 5: Not available"""
        return 2

def event_m50_35_x219(z1=50356110):
    """[Execution] Crowns that appear when a boss is destroyed
    z1: Crown OBJ instance ID
    """
    """State 0,1: Crown display: 30"""
    ChangeObjState(z1, 30)
    """State 2: End state"""
    return 0

def event_m50_35_x220(z1=50356110):
    """[Execution] Crowns that appear when the boss is destroyed
    z1: Crown OBJ instance ID
    """
    """State 0,1: Crown OBJ hidden: 10"""
    ChangeObjState(z1, 10)
    """State 2: End state"""
    return 0

def event_m50_35_x221(z1=50356110, z2=535000036, z4=5, action1=5310):
    """[Execution] Crowns that appear when the boss is destroyed
    z1: Crown OBJ instance ID
    z2: Crown acquisition flag
    z4: weight
    action1: Text ID
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60020000:Crown of the Sunken King
    AwardItem(60020000, 1)
    """State 4: Turn on the crown acquisition flag"""
    SetEventFlag(z2, 1)
    """State 5: weight"""
    CompareStateTime(0, z4, 3, z4)
    assert ConditionGroup(0)
    """State 6: Text display"""
    # action:5310:"A faint heat lingers in the ancient crown"
    DisplayEventMessage(action1, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 7: End state"""
    return 0

def event_m50_35_x222(z1=50356110):
    """[Execution] Crown that appears when the boss is destroyed
    z1: Crown OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z1, 1)
    """State 2: Is the boss battle over?"""
    IsEventBossBattle(0, 5030030, 0)
    assert ConditionGroup(0)
    """State 3: Enable key guide"""
    DisableObjKeyGuide(z1, 0)
    """State 4: Rerun"""
    return 0

def event_m50_35_x223(z1=50356110, z2=535000036, z3=535000096, z4=5, action1=5310):
    """[Preset] Crown that appears when a boss is destroyed
    z1: Crown OBJ instance ID
    z2: Crown acquisition flag
    z3: Defeat flag
    z4: weight
    action1: Text ID
    """
    """State 0,1: [Reproduction] Crown _SubState that appears when a boss is destroyed"""
    call = event_m50_35_x215(z2=z2, z1=z1)
    if call.Get() == 0:
        """State 7: [Condition] Crown that appears when boss is destroyed _ Defeat determination_SubState"""
        call = event_m50_35_x217(z3=z3)
        if call.Get() == 1:
            """State 9: [Execution] Crown_Sky_SubState that appears when a boss is destroyed"""
            assert event_m50_35_x246()
        elif call.Get() == 0:
            """State 5: [Execution] Crown Appearing at Boss Defeat_Display Crown_SubState"""
            assert event_m50_35_x219(z1=z1)
            """State 2: [Reproduction] Crown _ Sky _ SubState that appears by destroying the boss"""
            assert event_m50_35_x216()
            """State 8: [Condition] Crown that appears when boss is destroyed"""
            call = event_m50_35_x218(z1=z1)
            if call.Get() == 1:
                """State 3: [Execution] Crown that appears by destroying the boss_Key guide switching_SubState"""
                assert event_m50_35_x222(z1=z1)
            elif call.Get() == 0:
                """State 4: [Execution] Crown Appearing at Boss Defeat_Get Crown_SubState"""
                assert event_m50_35_x221(z1=z1, z2=z2, z4=z4, action1=action1)
                Goto('L0')
            elif call.Get() == 2:
                """State 10: [Execution] Crown that appears after destroying the boss_Unacquired_SubState"""
                assert event_m50_35_x253(z1=z1)
        """State 12: Rerun"""
        return 1
    elif call.Get() == 2:
        """State 6: [Execution] Crown Appearing by Boss Defeat_Hide_SubState"""
        assert event_m50_35_x220(z1=z1)
    elif call.Get() == 1:
        pass
    """State 11: Finish"""
    Label('L0')
    return 0

def event_m50_35_x224(z69=50352000):
    """[Execution] Door opened with DLC purchase
    z69: Door OBJ instance ID
    """
    """State 0,3: Did you approach the door?"""
    CompareObjPlayerDistance(0, z69, 4, 5)
    assert ConditionGroup(0)
    """State 1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z69, 8, 3)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x225():
    """[Condition] Poison Dragon Battle_HP Display and BGM Playback_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x226(z53=535000034, z54=50352100, z59=71, z60=20):
    """[Execution] Awakening Dragon_2
    z53: Event executed flag
    z54: Dragon OBJ instance ID
    z59: Flight OBJ State ID
    z60: OBJ state ID after flight
    """
    """State 0,1: Executed flag ON"""
    SetEventFlag(z53, 1)
    """State 2: Dragon flight and breath request"""
    ChangeObjState(z54, z59)
    ChangeObjState(50352250, 70)
    ChangeObjState(50352251, 71)
    ChangeObjState(50352252, 72)
    assert (GetStateTime() > 3.7) != 0
    """State 4: Explosion on the bridge 1"""
    ChangeObjState(50352200, 70)
    assert (GetStateTime() > 0.1) != 0
    """State 5: Explosion on the bridge 2"""
    ChangeObjState(50352201, 70)
    assert (GetStateTime() > 0.1) != 0
    """State 6: Explosion on the bridge 3"""
    ChangeObjState(50352202, 70)
    """State 3: Wait for end of flight"""
    CompareObjState(0, z54, z60, 0)
    assert ConditionGroup(0)
    """State 7: Finish"""
    return 0

def event_m50_35_x227(z8=900, z50=8506, z9=50001000, z10=50001039, z51=72):
    """[Execution] Queen's enemy summons
    z8: Boss generator ID
    z50: Zako ① Generator ID
    z9: Start point ID
    z10: End point ID
    z51: OBJ state ID for SFX
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1"""
        SetAreaVariable(1, GetPointCloseToCharacter(z9, z10, z8, 2))
    else:
        pass
    """State 7: Host wait"""
    IsHost(0, 1, 0)
    assert HostConditionGroup(0)
    """State 4: Move Damipoly 1 for SFX"""
    WarpObjToPoint(50352050, GetAreaVariable(1))
    """State 8: SFX playback"""
    ChangeObjState(50352050, z51)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z8)
    if HostConditionGroup(1):
        pass
    elif HostConditionGroup(0):
        """State 5: Summon character 1 generation"""
        ForceGenerationFromPoint(z50, GetAreaVariable(1), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z8, 7, 1, 1)
        IsChrDead(0, z8)
        assert HostConditionGroup(0)
    """State 10: Rerun"""
    return 0

def event_m50_35_x228(z8=900, z46=_, z47=_, z48=_, z9=50001000, z10=50001039, z49=_):
    """[Execution] Queen's enemy summon _3 body version
    z8: Boss generator ID
    z46: Zako ① Generator ID
    z47: Zako ② Generator ID
    z48: Zako ③ Generator ID
    z9: Start point ID
    z10: End point ID
    z49: OBJ state ID for SFX
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1 to 3"""
        SetAreaVariable(1, GetPointCloseToCharacter(z9, z10, z8, 2))
        SetAreaVariable(2, GetPointCloseToCharacter(z9, z10, z8, 3))
        SetAreaVariable(3, GetPointCloseToCharacter(z9, z10, z8, 4))
    else:
        pass
    """State 7: Host wait"""
    IsHost(0, 1, 0)
    assert HostConditionGroup(0)
    """State 4: Moved Damipoly 1 to 3 for SFX"""
    WarpObjToPoint(50352050, GetAreaVariable(1))
    WarpObjToPoint(50352051, GetAreaVariable(2))
    WarpObjToPoint(50352052, GetAreaVariable(3))
    """State 8: SFX playback 1 to 3"""
    ChangeObjState(50352050, z49)
    ChangeObjState(50352051, z49)
    ChangeObjState(50352052, z49)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z8)
    if HostConditionGroup(0):
        """State 5: Generate 3 summoned characters 1"""
        ForceGenerationFromPoint(z46, GetAreaVariable(1), 1)
        ForceGenerationFromPoint(z47, GetAreaVariable(2), 1)
        ForceGenerationFromPoint(z48, GetAreaVariable(3), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z8, 7, 1, 1)
        IsChrDead(0, z8)
        assert HostConditionGroup(0)
    elif HostConditionGroup(1):
        pass
    """State 10: Rerun"""
    return 0

def event_m50_35_x229(z39=50351750, z41=80, z42=10, z38=50353310, z40=50351760, z43=250, z44=251, z45=0):
    """[Execution] Switch thorn floor switch with flag OFF
    z39: Thorn ① OBJ instance ID
    z41: Operating OBJ state ID
    z42: Thorn Operation End OBJ State ID
    z38: Switch OBJ instance ID
    z40: Thorn ② OBJ instance ID
    z43: Replacement GM ①
    z44: Replacement GM ②
    z45: GM slot
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z38, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z38, 30, 0)
    assert ConditionGroup(0)
    """State 1: Thorn is in operation"""
    ChangeObjState(z39, z41)
    ChangeObjState(z40, z41)
    """State 8: weight"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 7: Grand material switching"""
    SetGroundMaterial(10, z43, z45)
    SetGroundMaterial(10, z44, z45)
    """State 3: Waiting for thorn to finish operation"""
    CompareObjState(8, z39, z42, 0)
    CompareObjState(8, z40, z42, 0)
    assert ConditionGroup(8)
    """State 9: Thorn floor state flag OFF"""
    SetEventFlag(535000028, 0)
    """State 2: Switch back"""
    ChangeObjState(z38, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z38, 10, 0)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m50_35_x230(z36=50353825, z37=535020024):
    """[Reproduction] Enemy activation on the building
    z36: Building OBJ instance ID
    z37: Enemy activation flag
    """
    """State 0,1: Judgment of building condition"""
    if CompareObjStateId(z36, 70, 0):
        """State 2: The building is waiting to rise"""
        assert CompareObjStateId(z36, 30, 0)
        """State 6: Navigation change waiting"""
        assert (GetStateTime() > 0.2) != 0
        """State 4: Enemy activation flag ON"""
        SetEventFlag(z37, 1)
        """State 7: Building: on"""
        return 0
    else:
        """State 3,5: Enemy activation flag OFF"""
        SetEventFlag(z37, 0)
        """State 8: Building: not above"""
        return 1

def event_m50_35_x231(z36=50353825):
    """[Condition] Enemy activation on the building
    z36: Building OBJ instance ID
    """
    """State 0,2: The building started to rise?"""
    CompareObjState(0, z36, 70, 0)
    assert ConditionGroup(0)
    """State 1: Waiting for the building to rise"""
    CompareObjState(0, z36, 30, 0)
    assert ConditionGroup(0)
    """State 3: weight"""
    CompareStateTime(0, 0.2, 3, 0.2)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x232(z37=535020024, z36=50353825):
    """[Execution] Enemy activation on the building
    z37: Enemy activation flag
    z36: Building OBJ instance ID
    """
    """State 0,1: Enemy activation flag ON"""
    SetEventFlag(z37, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z36, 30, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x233(z36=50353825, z37=535020024):
    """[Preset] Enemy activation on the building
    z36: Building OBJ instance ID
    z37: Enemy activation flag
    """
    """State 0,1: [Reproduction] Enemy activation on the building_SubState"""
    call = event_m50_35_x230(z36=z36, z37=z37)
    if call.Get() == 0:
        """State 4: [Condition] Enemy activation on the building_Descent judgment_SubState"""
        assert event_m50_35_x234(z36=z36)
        """State 2: [Execution] Enemy activation on the building_After descent_SubState"""
        assert event_m50_35_x235(z37=z37, z36=z36)
    elif call.Get() == 1:
        """State 5: [Condition] Enemy activation on the building_Rise determination_SubState"""
        assert event_m50_35_x231(z36=z36)
        """State 3: [Execution] Enemy activation on the building_After rising_SubState"""
        assert event_m50_35_x232(z37=z37, z36=z36)
    """State 6: Rerun"""
    return 0

def event_m50_35_x234(z36=50353825):
    """[Condition] Enemy activation on the building
    z36: Building OBJ instance ID
    """
    """State 0,1: Did the building begin to descend?"""
    CompareObjState(0, z36, 80, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x235(z37=535020024, z36=50353825):
    """[Execution] Enemy activation on the building
    z37: Enemy activation flag
    z36: Building OBJ instance ID
    """
    """State 0,1: Enemy activation flag OFF"""
    SetEventFlag(z37, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z36, 70, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x236(z35=100702):
    """[Reproduction] Clear DLC event_C route petrification
    z35: Achievement flag
    """
    """State 0,1: Already cleared?"""
    if GetEventFlag(z35) != 0:
        """State 3: Cleared"""
        return 1
    else:
        """State 2: Not cleared"""
        return 0

def event_m50_35_x237(z34=101053):
    """[Conditions] Clear DLC event_C route petrification
    z34: Boss destruction flag
    """
    """State 0,1: Boss destruction waiting"""
    CompareEventFlag(0, z34, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x238(z35=100702):
    """[Execution] Clear DLC event_C route petrification
    z35: Achievement flag
    """
    """State 0,1: Clear flag ON"""
    SetEventFlag(z35, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x239(z34=101053, z35=100702):
    """[Preset] Clear DLC event_C root petrification
    z34: Boss destruction flag
    z35: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_Clation of C root petrification_SubState"""
    call = event_m50_35_x236(z35=z35)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Inter-DLC event_Clation of C route petrification_SubState"""
        assert event_m50_35_x237(z34=z34)
        """State 2: [Execution] Inter-DLC event_C route petrification clear_SubState"""
        assert event_m50_35_x238(z35=z35)
    """State 4: End state"""
    return 0

def event_m50_35_x240(z27=_):
    """[Reproduction] Inter-DLC event_annihilation
    z27: Achievement flag
    """
    """State 0,1: Already achieved?"""
    if GetEventFlag(z27) != 0:
        """State 3: Accomplished"""
        return 1
    else:
        """State 2: Not Achieved"""
        return 0

def event_m50_35_x241(z28=6000, z29=6001, z30=6002, z31=6003, z32=6004):
    """[Condition] Event between DLCs
    z28: Generator ① ID
    z29: Generator ② ID
    z30: Generator ③ ID
    z31: Generator ④ ID
    z32: Generator ⑤ ID
    """
    """State 0,1: Did you annihilate the improper?"""
    IsChrDeadOrRespawnOver(8, z28, 1)
    IsChrDeadOrRespawnOver(8, z29, 1)
    IsChrDeadOrRespawnOver(8, z30, 1)
    IsChrDeadOrRespawnOver(8, z31, 1)
    IsChrDeadOrRespawnOver(8, z32, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_35_x242(z27=_):
    """[Execution] Inter-DLC event_annihilation
    z27: Achievement flag
    """
    """State 0,1: Clear flag ON"""
    SetEventFlag(z27, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x243(z28=6000, z29=6001, z30=6002, z31=6003, z32=6004, z33=100700):
    """[Preset] Inter-DLC events
    z28: Generator ① ID
    z29: Generator ② ID
    z30: Generator ③ ID
    z31: Generator ④ ID
    z32: Generator ⑤ ID
    z33: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_annihilation_SubState"""
    call = event_m50_35_x240(z27=z33)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Inter-DLC event_Suspicious annihilation_SubState"""
        assert event_m50_35_x241(z28=z28, z29=z29, z30=z30, z31=z31, z32=z32)
        """State 2: [Execution] Inter-DLC event_annihilation_SubState"""
        assert event_m50_35_x242(z27=z33)
    """State 4: End state"""
    return 0

def event_m50_35_x244(z21=6500, z22=6510, z23=6530, z24=6531, z25=6540, z26=6550):
    """[Conditions] Event between DLC_Dragon Blood Knight
    z21: Generator ① ID
    z22: Generator ② ID
    z23: Generator ③ ID
    z24: Generator ④ ID
    z25: Generator ⑤ ID
    z26: Generator ⑥ ID
    """
    """State 0,1: Has the dragon blood knight been annihilated?"""
    IsChrDeadOrRespawnOver(8, z21, 1)
    IsChrDeadOrRespawnOver(8, z22, 1)
    IsChrDeadOrRespawnOver(8, z23, 1)
    IsChrDeadOrRespawnOver(8, z24, 1)
    IsChrDeadOrRespawnOver(8, z25, 1)
    IsChrDeadOrRespawnOver(8, z26, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_35_x245(z21=6500, z22=6510, z23=6530, z24=6531, z25=6540, z26=6550, z27=100701):
    """[Preset] Inter-DLC event_Dragon Blood Knight
    z21: Generator ① ID
    z22: Generator ② ID
    z23: Generator ③ ID
    z24: Generator ④ ID
    z25: Generator ⑤ ID
    z26: Generator ⑥ ID
    z27: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_annihilation_SubState"""
    call = event_m50_35_x240(z27=z27)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Event between DLC_Dragon Blood Knight Extermination_SubState"""
        assert event_m50_35_x244(z21=z21, z22=z22, z23=z23, z24=z24, z25=z25, z26=z26)
        """State 2: [Execution] Inter-DLC event_annihilation_SubState"""
        assert event_m50_35_x242(z27=z27)
    """State 4: End state"""
    return 0

def event_m50_35_x246():
    """[Execution] Crown that appears after destroying the boss_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x247(z8=900, z16=8500, z17=8501, z18=8502, z9=50001000, z10=50001039, z19=71, z20=8507):
    """[Execution] Queen's enemy summon _4 body version
    z8: Boss generator ID
    z16: Zako ① Generator ID
    z17: Zako ② Generator ID
    z18: Zako ③ Generator ID
    z9: Start point ID
    z10: End point ID
    z19: OBJ state ID for SFX
    z20: Zako ④ Generator ID
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1 to 4"""
        SetAreaVariable(1, GetPointCloseToCharacter(z9, z10, z8, 2))
        SetAreaVariable(2, GetPointCloseToCharacter(z9, z10, z8, 3))
        SetAreaVariable(3, GetPointCloseToCharacter(z9, z10, z8, 4))
        SetAreaVariable(4, GetPointCloseToCharacter(z9, z10, z8, 5))
    else:
        pass
    """State 7: Host wait"""
    IsHost(0, 1, 0)
    assert HostConditionGroup(0)
    """State 4: Moved Damipoly 1 to 4 for SFX"""
    WarpObjToPoint(50352050, GetAreaVariable(1))
    WarpObjToPoint(50352051, GetAreaVariable(2))
    WarpObjToPoint(50352052, GetAreaVariable(3))
    WarpObjToPoint(50352053, GetAreaVariable(4))
    """State 8: SFX playback 1 to 4"""
    ChangeObjState(50352050, z19)
    ChangeObjState(50352051, z19)
    ChangeObjState(50352052, z19)
    ChangeObjState(50352053, z19)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z8)
    if HostConditionGroup(0):
        """State 5: Generate 4 summoned characters"""
        ForceGenerationFromPoint(z16, GetAreaVariable(1), 1)
        ForceGenerationFromPoint(z17, GetAreaVariable(2), 1)
        ForceGenerationFromPoint(z18, GetAreaVariable(3), 1)
        ForceGenerationFromPoint(z20, GetAreaVariable(4), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z8, 7, 1, 1)
        IsChrDead(0, z8)
        assert HostConditionGroup(0)
    elif HostConditionGroup(1):
        pass
    """State 10: Rerun"""
    return 0

def event_m50_35_x248(z8=900, z11=8500, z12=8501, z13=8502, z9=50001000, z10=50001039, z14=8507, z15=8508):
    """[Execution] Queen's enemy summon _5 body version
    z8: Boss generator ID
    z11: Zako ① Generator ID
    z12: Zako ② Generator ID
    z13: Zako ③ Generator ID
    z9: Start point ID
    z10: End point ID
    z14: Zako ④ Generator ID
    z15: Zako ⑤ Generator ID
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1 to 5"""
        SetAreaVariable(1, GetPointCloseToCharacter(z9, z10, z8, 2))
        SetAreaVariable(2, GetPointCloseToCharacter(z9, z10, z8, 3))
        SetAreaVariable(3, GetPointCloseToCharacter(z9, z10, z8, 4))
        SetAreaVariable(4, GetPointCloseToCharacter(z9, z10, z8, 5))
        SetAreaVariable(5, GetPointCloseToCharacter(z9, z10, z8, 6))
    else:
        pass
    """State 7: Host wait"""
    IsHost(0, 1, 0)
    assert HostConditionGroup(0)
    """State 4: Moved Damipoly 1 to 5 for SFX"""
    WarpObjToPoint(50352050, GetAreaVariable(1))
    WarpObjToPoint(50352051, GetAreaVariable(2))
    WarpObjToPoint(50352052, GetAreaVariable(3))
    WarpObjToPoint(50352053, GetAreaVariable(4))
    WarpObjToPoint(50352054, GetAreaVariable(5))
    """State 8: SFX playback 1 to 5"""
    ChangeObjState(50352050, 71)
    ChangeObjState(50352051, 71)
    ChangeObjState(50352052, 71)
    ChangeObjState(50352053, 71)
    ChangeObjState(50352054, 71)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z8)
    if HostConditionGroup(0):
        """State 5: Generate summoned characters 1 to 5"""
        ForceGenerationFromPoint(z11, GetAreaVariable(1), 1)
        ForceGenerationFromPoint(z12, GetAreaVariable(2), 1)
        ForceGenerationFromPoint(z13, GetAreaVariable(3), 1)
        ForceGenerationFromPoint(z14, GetAreaVariable(4), 1)
        ForceGenerationFromPoint(z15, GetAreaVariable(5), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z8, 7, 1, 1)
        IsChrDead(0, z8)
        assert HostConditionGroup(0)
    elif HostConditionGroup(1):
        pass
    """State 10: Rerun"""
    return 0

def event_m50_35_x249(z5=535000096):
    """[Reproduction] Bowing management of NPC
    z5: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z5) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_35_x250(z6=901):
    """[Conditions] NPC bow management
    z6: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z6, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x251(z7=535020038):
    """[Execution] Bowing management of NPC
    z7: Bowing flag
    """
    """State 0,1: Bowing flag ON"""
    SetEventFlag(z7, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x252(z5=535000096, z6=901, z7=535020038):
    """[Preset] NPC bow management
    z5: Defeat flag
    z6: Boss generator ID
    z7: Bowing flag
    """
    """State 0,1: [Reproduction] NPC bow management_SubState"""
    call = event_m50_35_x249(z5=z5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] NPC bow management_SubState"""
        assert event_m50_35_x250(z6=z6)
        """State 2: [Execution] NPC bow management_SubState"""
        assert event_m50_35_x251(z7=z7)
    """State 4: End state"""
    return 0

def event_m50_35_x253(z1=50356110):
    """[Execution] Crown that appears when the boss is destroyed
    z1: Crown OBJ instance ID
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z1, 1)
    """State 1: Acquisition failure window display"""
    # lot:60020000:Crown of the Sunken King
    DisplayItemAwardFailure(60020000, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 2: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z1, 0)
    """State 5: End state"""
    return 0

def event_m50_35_110000():
    """White spirit sign display_01"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z270=710)

def event_m50_35_110001():
    """White spirit sign display_02"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z270=711)

def event_m50_35_110002():
    """White spirit sign display_03"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z270=712)

def event_m50_35_110003():
    """White spirit sign display_04"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z270=713)

def event_m50_35_110004():
    """White spirit sign display_05"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z270=714)

def event_m50_35_110005():
    """White spirit sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m50_35_x23(z255=102430, z256=715, z257=104160, z258=103660, z259=-1)

def event_m50_35_110006():
    """White spirit: Counting up the moonlight"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m50_35_x21(z264=535000081, z265=102436, z266=205, z267=7430)

def event_m50_35_110010():
    """Black spirit display_01"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_35_x33(z245=10000000, z246=700, z247=0, z248=0.2, z249=535020020)

def event_m50_35_110011():
    """Black Spirit Display_02"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_35_x33(z245=10000010, z246=720, z247=0, z248=0.2, z249=535020022)

def event_m50_35_4000000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m50_35_x37(z230=535020010, z231=14, z232=535000011, z233=5, z234=20)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m50_35_x42(z238=80000000, z239=0, z240=5, z241=974, val4=1, z242=20, z243=80000001,
                z244=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m50_35_x42(z238=80000100, z239=0, z240=5, z241=974, val4=2, z242=20, z243=80000101,
                z244=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m50_35_x42(z238=80000200, z239=0, z240=5, z241=974, val4=3, z242=20, z243=80000201,
                z244=80000299))
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert (event_m50_35_x42(z238=80000300, z239=0, z240=5, z241=974, val4=4, z242=20, z243=80000301,
                z244=80000399))
        """State 8: [Lib] [DC] [Preset] Wanderer_Generation_5_SubState"""
        assert (event_m50_35_x42(z238=80000400, z239=0, z240=5, z241=974, val4=5, z242=20, z243=80000401,
                z244=80000499))
        """State 2: Start flag ON"""
        SetEventFlag(535020012, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m50_35_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m50_35_x45(z235=535000011, z236=974, mode1=1)
    """State 1: Finish"""
    EndMachine()

