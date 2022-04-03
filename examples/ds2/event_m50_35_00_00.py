# -*- coding: utf-8 -*-
def event_m50_35_2000():
    """Elevator in MAP_city_upper layer"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(2030) != 0
    """State 3: [Preset] Elevator with lid_SubState"""
    assert event_m50_35_x138(z138=50351202, z139=200000, z140=200001, z141=50353404, z142=50353405)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_2010():
    """Elevator in MAP_city_upper layer_on switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(2030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z149=50351202, z150=10, z151=50353404)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_2020():
    """Elevator in MAP_city_upper layer_under switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(2030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z149=50351202, z150=40, z151=50353405)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_2030():
    """MAP elevator_city_upper layer_start"""
    """State 0,2: [Preset] Elevator with lid_Startup_SubState"""
    assert event_m50_35_x137(z143=50353404, z144=50353405, z145=50351202, z146=50353913, z147=10, z148=50353404)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_3000():
    """Elevator in MAP_city_lower layer"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(3030) != 0
    """State 3: [Preset] Elevator with lid_SubState"""
    assert event_m50_35_x138(z138=50351204, z139=300000, z140=300001, z141=50353406, z142=50353407)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_3010():
    """Elevator in MAP_city_lower layer_on switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(3030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z149=50351204, z150=10, z151=50353406)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_3020():
    """Elevator in MAP_city_lower layer_under switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(3030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z149=50351204, z150=40, z151=50353407)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_3030():
    """Elevator in MAP_city_lower layer_start"""
    """State 0,2: [Preset] Elevator with lid_Startup_SubState"""
    assert event_m50_35_x137(z143=50353406, z144=50353407, z145=50351204, z146=50353913, z147=10, z148=50353406)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_4000():
    """Elevator in MAP_city_bonfire 2"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Preset] Elevator with lid_SubState"""
    assert event_m50_35_x138(z138=50351206, z139=400000, z140=400001, z141=50353400, z142=50353401)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_4010():
    """Elevator in MAP_city_on bonfire 2_switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z149=50351206, z150=10, z151=50353400)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_4020():
    """Elevator in MAP _ Town _ Bonfire 2_ Below switch"""
    """State 0,2: Has the startup event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Preset] Elevator with lid_Switch_SubState"""
    assert event_m50_35_x136(z149=50351206, z150=40, z151=50353401)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_4030():
    """Elevator in MAP _ City _ Bonfire 2_ Start"""
    """State 0,2: [Preset] Elevator with lid_Startup_SubState"""
    assert event_m50_35_x137(z143=50353400, z144=50353401, z145=50351206, z146=50353914, z147=40, z148=50353401)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_6000():
    """Stone board to elevate bridge tower"""
    """State 0,3: [Preset] Stone board to raise the tower of the bridge_SubState"""
    call = event_m50_35_x121(z157=50353740)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_35_6020():
    """Bridge tower rising"""
    """State 0,2: [Preset] Bridge tower rises_SubState"""
    assert event_m50_35_x95(z177=50353740, z178=50353751, z179=50353750)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_6030():
    """The tower of the bridge rises"""
    """State 0,2: [Preset] Bridge tower rises_Navigation switch_SubState"""
    assert event_m50_35_x110(z152=50353751, z153=50353750, z154=603010, z155=603020, z156=50353740)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_7000():
    """OBJ_pillar running on stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353575, z115=50353906, z116=700000, z117=700010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_8000():
    """OBJ_Jumping out_1 running on a stone switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353890, z115=50353900, z116=800000, z117=800010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_8010():
    """OBJ_Jump out_2 operating with a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353825, z115=50353901, z116=801000, z117=801010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_8060():
    """Enemy activation on the building_Jump 2"""
    """State 0,2: [Preset] Enemy activation on the building_SubState"""
    assert event_m50_35_x233(z31=50353825, z32=535020024)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_9000():
    """OBJ_bullet barrier_1 running on a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353606, z115=50353909, z116=900000, z117=900010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_10000():
    """OBJ_Item_1 working with stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353850, z115=50353902, z116=1000000, z117=1000010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_10010():
    """OBJ_Item_2 working with stone statue switch"""
    """State 0,2: [Preset] OBJ_Navigation 1 version_SubState running on stone statue switch"""
    assert event_m50_35_x169(z107=50353875, z108=50353912, z109=1001000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_11000():
    """OBJ_wall pillars working with stone statue switches"""
    """State 0,2: [Preset] OBJ_Navigation 1 version_SubState running on stone statue switch"""
    assert event_m50_35_x169(z107=50353650, z108=50353903, z109=1100000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_12000():
    """OBJ_wall trabeculars_1 running on a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353701, z115=50353905, z116=1200000, z117=1200010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_12010():
    """OBJ_wall trabeculars_2 operated by stone statue switch_2"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353700, z115=50353904, z116=1201000, z117=1201010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13000():
    """OBJ_Roofwalk_1 running on a stone switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353608, z115=50353911, z116=1300000, z117=1300010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13010():
    """OBJ_Roofwalk_2 operated by a stone statue switch_2"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353609, z115=50353910, z116=1301000, z117=1301010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13020():
    """OBJ_Roofwalk_3 with stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353603, z115=50353907, z116=1302000, z117=1302010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13030():
    """OBJ_Roofwalk_4 with a stone statue switch"""
    """State 0,2: [Preset] OBJ_SubState running on the stone statue switch"""
    assert event_m50_35_x162(z114=50353604, z115=50353908, z116=1303000, z117=1303010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13050():
    """Change navigation between buildings_1"""
    """State 0,2: [Preset] Change navigation between buildings_SubState"""
    assert event_m50_35_x176(z99=50353608, z100=50353609, z101=1305010, z102=1305000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13060():
    """Change navigation between buildings_2"""
    """State 0,2: [Preset] Change navigation between buildings_SubState"""
    assert event_m50_35_x176(z99=50353609, z100=50353603, z101=1306010, z102=1306000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_13070():
    """Change navigation between buildings_3"""
    """State 0,2: [Preset] Change navigation between buildings_SubState"""
    assert event_m50_35_x176(z99=50353603, z100=50353604, z101=1307010, z102=1307000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20000():
    """Door that turns with switch"""
    """State 0,2: [Preset] Door rotated by switch_SubState"""
    assert event_m50_35_x50(z205=50351210, z206=50353408, z207=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20010():
    """Rotating door with doors_Aisle_Navi switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z172=50351210, val2=2001010, val3=2001000, z173=535020042)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20020():
    """Door that turns with switch_Thorn room"""
    """State 0,2: [Preset] Door rotated by switch_SubState"""
    assert event_m50_35_x50(z205=50351211, z206=50353402, z207=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20030():
    """Rotating door with switch_Thorn room_Navigation switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z172=50351211, val2=2003010, val3=2003000, z173=535020044)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20040():
    """Rotating door with switch"""
    """State 0,2: [Preset] Rotating door with switch_Two switches_SubState"""
    assert event_m50_35_x185(z84=50351213, z85=50353410, z86=32, z87=50353412)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20050():
    """Doors that rotate with switch_Blow-out_Navi switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z172=50351213, val2=2005010, val3=2005000, z173=535020046)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_20060():
    """Door rotated by switch_135 degree version"""
    """State 0,3: [Preset] Door that rotates with switch_135 degree version_Two switch version_SubState"""
    assert event_m50_35_x189(z80=50351215, z81=50353409, z82=32, z83=50353411)
    """State 1: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 2: [Preset] Rotating door with switch_135 degree version_SubState"""
    event_m50_35_x172(z104=50351215, z105=50353409, z106=32)
    Quit()

def event_m50_35_20070():
    """Rotating door with switch_135 degree version_Navigation switching and flag switching"""
    """State 0,2: [Preset] Doors that rotate with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x107(z172=50351215, val2=2007010, val3=2007000, z173=535020040)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_21000():
    """Door opened with switch_Crossroad"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353203, z198=50351221, z199=2100000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_21010():
    """Door opened with switch_Ghost Knight Room"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353200, z198=50351220, z199=2101000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_21020():
    """Door opened with switch_Elevator room"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353209, z198=50351222, z199=2102000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_21030():
    """Door opened with switch_Revolving door passage"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353213, z198=50351223, z199=2103000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_21040():
    """Door that opens with switch_Thorn Zone"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353211, z198=50351224, z199=2104000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_21050():
    """Door opened with switch_Thorn Zone Heights"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353212, z198=50351225, z199=2105000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_21060():
    """Door opened with switch_Straight tip"""
    """State 0,2: [Preset] Door that opens only once with a switch_SubState"""
    assert event_m50_35_x63(z197=50353308, z198=50351226, z199=2106000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_22000():
    """Spear from the left and right with the switch"""
    """State 0,2: [Preset] Switch left and right with switch_SubState"""
    assert event_m50_35_x59(z200=50353100, z201=0.2, z202=0.3)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_23000():
    """Machine gun bow and arrow _ hill room"""
    """State 0,2: [Preset] Machine gun bow and arrow_SubState"""
    assert event_m50_35_x67(z194=50351450, z195=50353115, z196=1.5)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_25000():
    """Multiple doors of ruins"""
    """State 0,2: [Preset] Multiple doors of ruins_Continuous version_SubState"""
    assert event_m50_35_x55(z203=5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_25010():
    """Multiple doors in ruins"""
    """State 0,2: [Preset] Ruins Multiple Doors_Navigation Switch_SubState"""
    assert event_m50_35_x102()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_26000():
    """C root key door"""
    """State 0,3: [Preset] C root key_SubState"""
    call = event_m50_35_x151(z136=50350400, z137=2600000)
    if call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()

def event_m50_35_27000():
    """Switch thorn floor with switch"""
    """State 0,2: [Preset] Switch the thorn floor with a switch_SubState"""
    assert event_m50_35_x91(z33=50353310, z34=50351750, z35=50351760)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_28000():
    """Ghost Knight's Materialization_Character_The Beginning of the Ruins_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000050, z189=4001, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28010():
    """Ghost Knight's Materialization_Character_The Beginning of Ruins_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000051, z189=4002, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28050():
    """Ghost Knight's Materialization_Character_Mausoleum_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000052, z189=5000, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28060():
    """Ghost Knight's Materialization_Character_Mausoleum_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000053, z189=5002, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28070():
    """Ghost Knight Materialization_Character_Rei_3"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000054, z189=5202, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28080():
    """Ghost Knight Materialization_Character_Reiper_4"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000055, z189=5400, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28090():
    """Ghost Knight Materialization_Character_Mausoleum_5"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000056, z189=5800, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28100():
    """Ghost Knight's Materialization_Character_Mausoleum_6"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000057, z189=5801, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_28110():
    """Ghost Knight's Materialization_Character_Mausoleum_7"""
    """State 0,2: [Preset] Ghost Knight Materialization_Character_SubState"""
    assert event_m50_35_x76(z188=535000058, z189=5802, z190=96650000, z191=96650010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29000():
    """The Ghost Knight's Materialization_OBJ_The Beginning of the Ruins_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351600, z193=535000050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29010():
    """Realization of the Ghost Knight_OBJ_Beginning of Ruins_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351601, z193=535000051)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29050():
    """Ghost knight materialization_OBJ_ mausoleum_1"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351610, z193=535000052)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29060():
    """Ghost knight materialization_OBJ_ mausoleum_2"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351613, z193=535000053)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29070():
    """Ghost knight materialization_OBJ_ mausoleum_3"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351615, z193=535000054)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29080():
    """Ghost knight materialization_OBJ_ mausoleum_4"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351611, z193=535000055)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29090():
    """Ghost knight materialization_OBJ_ mausoleum_5"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351614, z193=535000056)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29100():
    """Ghost knight materialization_OBJ_ mausoleum_6"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351616, z193=535000057)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_29110():
    """Ghost knight materialization_OBJ_ mausoleum_7"""
    """State 0,2: [Preset] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x75(z192=50351612, z193=535000058)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_30000():
    """Boss: Underground Queen_Battle"""
    """State 0,2: [Preset] Boss Battle _ BGM playback and HP display with activation state release_SubState"""
    assert (event_m50_35_x111(flag16=535000081, z158=501, z159=5030000, z160=535020080, z161=6.5, z162=3000000,
            z163=900, z164=4))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_30010():
    """Boss: Queen's enemy summons"""
    """State 0,3: [Preset] Queen's Enemy Summon _No Duplicate Version_SubState"""
    call = event_m50_35_x181(z6=900, z7=50001000, z8=50001039)
    if call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Done():
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m50_35_30020():
    """Doors opened by destroying bosses: mural"""
    """State 0,3: [Preset] Door opened by boss defeat_SubState"""
    call = event_m50_35_x71(z64=50351500, flag9=535000081, val1=3002000, z65=8)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_35_30030():
    """Boss: Queen's voice"""
    """State 0,3: [Preset] Queen's singing voice_SubState"""
    call = event_m50_35_x153(z120=503500002, z121=900, z122=20, z123=3003000, z124=3003003, z125=2)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_35_30040():
    """Boss: Queen's lines"""
    """State 0,2: [Preset] Queen's lines_SubState"""
    assert event_m50_35_x193(z76=5030000, z77=4.5, flag11=535000081, z78=900, z79=535020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_33000():
    """Boss: Petrochemical root boss_battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m50_35_x1(flag21=535000091, z259=3300000, z260=3300000, z261=504, z262=5030020, z263=535020090,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_34000():
    """Boss: Poison Dragon_Battle"""
    """State 0,2: [Preset] Poison Dragon Battle_SubState"""
    assert (event_m50_35_x209(flag8=535000096, z54=502, z55=5030030, z56=535020095, z57=5.5, z58=3400000,
            z59=901, z60=3400010))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_34010():
    """The crown that appears when you destroy a boss"""
    """State 0,3: [Preset] Crown _SubState that appears when a boss is destroyed"""
    # action:5310:"A faint heat lingers in the ancient crown"
    call = event_m50_35_x223(z1=50356110, flag1=535000036, z2=535000096, z3=5, action1=5310)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_35_34020():
    """NPC bow management"""
    """State 0,2: [Preset] NPC bow management_SubState"""
    assert event_m50_35_x252(flag2=535000096, z4=901, z5=535020038)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_34030():
    """Boss: Dragon Battle Filter Change"""
    """State 0,2: [Preset] Change dragon battle filter_SubState"""
    assert event_m50_35_x197(z66=901, z67=3.3, z68=535020095, flag10=535000096, z69=3403000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_34050():
    """Awakening Dragon"""
    """State 0,2: [Preset] Awakening Dragon_SubState"""
    assert (event_m50_35_x99(flag6=535000032, flag7=535000034, z47=50352100, z48=3405000, z49=3405010,
            z50=3405011, z51=3405001))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_35010():
    """Treasure on a pillar_2"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z256=50353850, z257=150, z258=50356400)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_35020():
    """Treasure on a pillar_3"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z256=50353609, z257=150, z258=50356570)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_35030():
    """Treasure on the pillar_4"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z256=50353609, z257=151, z258=50356580)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_35040():
    """Treasure on the pillar_5"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_35_x11(z256=50353875, z257=150, z258=50356410)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_36000():
    """Hidden door navigation mesh change_1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_35_x12(z251=50351008, z252=20, z253=3600000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

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
    Quit()

def event_m50_35_51000():
    """Start from the bottom"""
    """State 0,1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_52000():
    """Return to the bottom"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m50_35_x30(z232=50351800, z233=10250000, z234=5200000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_35_53000():
    """Door that opens with DLC purchase"""
    """State 0,3: [Preset] Door that opens with DLC purchase_SubState"""
    call = event_m50_35_x80(z61=50352000, z62=5300000, z63=5300010)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_35_55000():
    """Inter-DLC event"""
    """State 0,2: [Preset] Inter-DLC events _ Completely annihilated _SubState"""
    assert event_m50_35_x243(z25=6000, z26=6001, z27=6002, z28=6003, z29=6004, flag4=100700)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_55010():
    """DLC event_Dragon Blood Knight"""
    """State 0,2: [Preset] Inter-DLC event_Dragon Blood Knight Extermination_SubState"""
    assert event_m50_35_x245(z19=6500, z20=6510, z21=6530, z22=6531, z23=6540, z24=6550, flag3=100701)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_55020():
    """Inter-DLC event _C route petrochemical clearing"""
    """State 0,2: [Preset] Inter-DLC event _ Clear C root petrification_SubState"""
    assert event_m50_35_x239(z30=101053, flag5=100702)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_80000():
    """Reproduction fire 01_Starting point"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035000, z249=5035099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_81000():
    """Regeneration of fire 02_city end"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035100, z249=5035199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_83000():
    """Rebirth Fire 04_Poison Dragon"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035300, z249=5035399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_84000():
    """Reproduction Fire 05_Hidden room of the ruins"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035400, z249=5035499)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_85000():
    """Regenerative fireworks 06_ cave"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035500, z249=5035599)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_86000():
    """Rebirth of fire 07_The hidden door of the large room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035600, z249=5035699)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_87000():
    """Reproduction of fire 08_city"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_35_x20(z248=5035700, z249=5035799)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_89000():
    """Shop lineup expansion_Queen"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_35_x32(z231=101050, flag20=101200)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_89010():
    """Shop lineup expansion_Dragon"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_35_x32(z231=101051, flag20=101201)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_x0(z264=0, z265=0, z233=10250000, z234=5200000):
    """[Lib] Warp between maps after poly play
    z264: Pre-warp poly play ID
    z265: Poly Play ID after Warp
    z233: Map ID
    z234: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z264, z265, z233, z234, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m50_35_x1(flag21=535000091, z259=3300000, z260=3300000, z261=504, z262=5030020, z263=535020090,
                    mode2=0):
    """[Lib] [Preset] Boss Battle Start
    flag21: Boss destruction flag
    z259: Start point ID
    z260: End point ID
    z261: Sound ID
    z262: Boss Battle ID
    z263: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m50_35_x2(flag21=flag21)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m50_35_x3(z259=z259, z260=z260)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m50_35_x4(z261=z261, z262=z262, z263=z263)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m50_35_x5()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m50_35_x6(z262=z262)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m50_35_x7(z261=z261, z262=z262, z263=z263, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m50_35_x2(flag21=535000091):
    """[Reproduction] Boss Battle_Start
    flag21: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag21) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_35_x3(z259=3300000, z260=3300000):
    """[Condition] Boss Battle_Start
    z259: Start point ID
    z260: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z259, z260, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z259, z260, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x4(z261=504, z262=5030020, z263=535020090):
    """[Execution] Boss Battle_Start
    z261: Sound ID
    z262: Boss Battle ID
    z263: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z261)
    """State 1: Boss battle start notification"""
    StartBossFight(z262)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z263, 1)
    """State 4: End state"""
    return 0

def event_m50_35_x5():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x6(z262=5030020):
    """[Condition] Boss Battle_End Judgment
    z262: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z262, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x7(z261=504, z262=5030020, z263=535020090, mode2=0):
    """[Execute] Boss Battle_End
    z261: Sound ID
    z262: Boss Battle ID
    z263: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z263, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z262)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z261)
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

def event_m50_35_x10(z256=_, z257=_, z258=_):
    """[Lib] [execute] OBJ attach
    z256: Parent OBJ instance ID
    z257: Parent Damipoli ID
    z258: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z256, z257, z258)
    """State 2: End state"""
    return 0

def event_m50_35_x11(z256=_, z257=_, z258=_):
    """[Lib] [Preset] OBJ attach
    z256: Parent OBJ instance ID
    z257: Parent Damipoli ID
    z258: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m50_35_x8()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m50_35_x9()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m50_35_x10(z256=z256, z257=z257, z258=z258)
    """State 4: End state"""
    return 0

def event_m50_35_x12(z251=50351008, z252=20, z253=3600000, z254=0, z255=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z251: Object instance ID
    z252: OBJ state ID
    z253: Navimesh switching point ID
    z254: Additional attributes
    z255: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m50_35_x13(z251=z251, z252=z252, z253=z253, z255=z255, z254=z254)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m50_35_x14(z251=z251, z252=z252, z253=z253)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m50_35_x15(z251=z251, z252=z252, z253=z253, z254=z254, z255=z255)
    """State 4: End state"""
    return 0

def event_m50_35_x13(z251=50351008, z252=20, z253=3600000, z255=2, z254=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z251: Target OBJ instance ID
    z252: Target OBJ state ID
    z253: Navimesh switching point ID
    z255: Additional attributes
    z254: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z251, z252, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z253, z255)
        DeleteNavimeshAttribute(z253, z254)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m50_35_x14(z251=50351008, z252=20, z253=3600000):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z251: Target OBJ instance ID
    z252: Target OBJ state ID
    z253: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z251, z252, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x15(z251=50351008, z252=20, z253=3600000, z254=0, z255=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z251: Target OBJ instance ID
    z252: Target OBJ state ID
    z253: Navimesh switching point ID
    z254: Additional attributes
    z255: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z253, z254)
    DeleteNavimeshAttribute(z253, z255)
    """State 2: End state"""
    return 0

def event_m50_35_x16(z250=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z250: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z250)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m50_35_x17():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x18(z248=_, z249=_):
    """[Lib] [execute] Rebirth fire
    z248: Flag start ID
    z249: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z248, z249, 0)
    """State 2: End state"""
    return 0

def event_m50_35_x19():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x20(z248=_, z249=_):
    """[Lib] [Preset] Rebirth
    z248: Flag start ID
    z249: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m50_35_x17()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m50_35_x19()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m50_35_x18(z248=z248, z249=z249)
    """State 4: End state"""
    return 0

def event_m50_35_x21(z244=535000081, z245=102436, z246=205, z247=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z244: Defeat Boss 1: Area and other flags
    z245: Summon Achievement: Global Event Flag
    z246: Summon achievement count: global variable
    z247: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z245, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z244, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z246, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z246, NpcInfoValue(z247, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z245, 1)
                CompareEventFlag(0, z245, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m50_35_x22(z240=_, z241=_, z242=0, z243=0.2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z240: Summon range
    z241: Generator ID
    z242: Appearance: Minimum time
    z243: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z240, z240, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z242, 3, z243)
        IsPlayerInsidePoint(1, z240, z240, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z241)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m50_35_x23(z235=102430, z236=715, z237=104160, z238=103660, z239=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z235: White Phantom can appear: Global event flag
    z236: White Phantom: Generator ID
    z237: Death: Global event flag
    z238: Hostile: Global event flag
    z239: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z236)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z237, 1)
        CompareEventFlag(1, z238, 1)
        CompareEventFlag(2, z235, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z236)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z237, 1)
            CompareEventFlag(1, z238, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z236)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z237, 1)
            CompareEventFlag(1, z238, 1)
            HasNpcPhantomSpawned(2, z236, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z236, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z236)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m50_35_x24(flag20=_):
    """[Lib] [Reproduction] Shop Lineup
    flag20: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(flag20) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m50_35_x25(flag20=_):
    """[Lib] [execution] shop lineup
    flag20: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(flag20, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x26(z232=50351800):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z232: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z232)
    """State 2: End state"""
    return 0

def event_m50_35_x27(z232=50351800):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z232: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z232, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z232)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m50_35_x28(z232=50351800, z233=10250000, z234=5200000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z232: Warp OBJ instance ID
    z233: Map ID
    z234: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z232, 1)
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
        assert event_m50_35_x0(z264=0, z265=0, z233=z233, z234=z234)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m50_35_x29(z232=50351800):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z232: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z232, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x30(z232=50351800, z233=10250000, z234=5200000):
    """[Lib] [Preset] Warp move between main part and DLC
    z232: Warp OBJ instance ID
    z233: Map ID
    z234: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m50_35_x26(z232=z232)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m50_35_x27(z232=z232)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m50_35_x29(z232=z232)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m50_35_x28(z232=z232, z233=z233, z234=z234)
    """State 5: End state"""
    return 0

def event_m50_35_x31(z231=_):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z231: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z231, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x32(z231=_, flag20=_):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z231: Boss destruction flag
    flag20: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m50_35_x24(flag20=flag20)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m50_35_x31(z231=z231)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m50_35_x25(flag20=flag20)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x33(z226=_, z227=_, z228=0, z229=0.2, z230=_):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON
    z226: Summon range
    z227: Generator ID
    z228: Appearance: Minimum time
    z229: Appearance: Maximum time
    z230: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z226, z226, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z228, 3, z229)
        IsPlayerInsidePoint(1, z226, z226, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z227)
            SetEventFlag(z230, 1)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m50_35_x34(flag17=535020010, flag18=535000011):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag17: Lottery determination flag
    flag18: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag18) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag17) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m50_35_x35(z214=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z214: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z214, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m50_35_x36(flag17=535020010, z215=5, z216=20):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag17: Lottery determination flag
    z215: Number of appearance judgment points
    z216: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag17, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z215)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z216, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m50_35_x37(flag17=535020010, z214=14, flag18=535000011, z215=5, z216=20):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag17: Lottery determination flag
    z214: Random number comparison value
    flag18: Defeat flag
    z215: Number of appearance judgment points
    z216: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m50_35_x34(flag17=flag17, flag18=flag18)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m50_35_x35(z214=z214)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m50_35_x36(flag17=flag17, z215=z215, z216=z216)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m50_35_x46(flag17=flag17, z216=z216)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m50_35_x38(val4=_, z223=20):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val4: Appearance judgment number
    z223: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z223) == val4) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_35_x39(z219=_, z220=0, z221=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z219: Appearance judgment point ID
    z220: Minimum appearance time
    z221: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z219, z219, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z220, 3, z221)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_35_x40(z222=974, z224=_, z225=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z222: Generator ID
    z224: Appearance start point ID
    z225: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z222, z224, z225)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z222)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m50_35_x41(flag19=535000011):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag19: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag19) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m50_35_x42(z219=_, z220=0, z221=5, z222=974, val4=_, z223=20, z224=_, z225=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z219: Intrusion detection point ID
    z220: Minimum appearance time
    z221: Maximum time to appear
    z222: Generator ID
    val4: Appearance judgment number
    z223: Lottery result point variable
    z224: Appearance start point ID
    z225: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m50_35_x38(val4=val4, z223=z223)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m50_35_x39(z219=z219, z220=z220, z221=z221)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m50_35_x40(z222=z222, z224=z224, z225=z225)
    """State 4: Finish"""
    return 0

def event_m50_35_x43(z217=974, mode1=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z217: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z217)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m50_35_x44(flag19=535000011, z218=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag19: Defeat flag
    z218: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag19, 1)
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
                    SetEventFlag(z218, 1)
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

def event_m50_35_x45(flag19=535000011, z217=974, mode1=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag19: Defeat flag
    z217: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m50_35_x41(flag19=flag19)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m50_35_x43(z217=z217, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m50_35_x44(flag19=flag19, z218=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m50_35_x44(flag19=flag19, z218=102755)
    """State 5: End state"""
    return 0

def event_m50_35_x46(flag17=535020010, z216=20):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag17: Lottery determination flag
    z216: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag17, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z216, 0)
    """State 3: End state"""
    return 0

def event_m50_35_x47(z206=_, z205=_, z207=10):
    """[Reproduction] Door rotated by switch
    z206: Switch OBJ instance ID
    z205: Revolving door OBJ instance ID
    z207: Initial state OBJ state ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z205, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z205, z207)
        assert CompareObjStateId(z205, z207, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z206, 30, 0) and CompareObjStateId(z205, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z206, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z206, 10, 0)
    elif CompareObjStateId(z206, 30, 0) and CompareObjStateId(z205, 10, 0):
        Goto('L0')
    elif CompareObjStateId(z206, 30, 0) and CompareObjStateId(z205, 32, 0):
        Goto('L0')
    elif CompareObjStateId(z206, 30, 0) and CompareObjStateId(z205, 34, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x48(z206=_, z205=_):
    """[Condition] Door rotated by switch
    z206: Switch OBJ instance ID
    z205: Revolving door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z205, 10, 0)
    CompareObjState(1, z205, 30, 0)
    CompareObjState(2, z205, 32, 0)
    CompareObjState(3, z205, 34, 0)
    CompareObjState(4, z205, 70, 0)
    CompareObjState(5, z205, 72, 0)
    CompareObjState(6, z205, 74, 0)
    CompareObjState(7, z205, 76, 0)
    if ConditionGroup(4):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z205, 30, 0)
        assert ConditionGroup(0)
        """State 22: Top: Switch back"""
        return 4
    elif ConditionGroup(5):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z205, 32, 0)
        assert ConditionGroup(0)
        """State 23: Right: Switch back"""
        return 5
    elif ConditionGroup(6):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z205, 34, 0)
        assert ConditionGroup(0)
        """State 24: Bottom: Switch back"""
        return 6
    elif ConditionGroup(7):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z205, 10, 0)
        assert ConditionGroup(0)
        """State 25: Left: Switch back"""
        return 7
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z206, -1, -4, 0)
        CompareObjState(0, z206, 30, 0)
        assert ConditionGroup(0)
        """State 18: Door up from left"""
        return 0
    elif ConditionGroup(1):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z206, -1, -4, 0)
        CompareObjState(0, z206, 30, 0)
        assert ConditionGroup(0)
        """State 19: Door from top to right"""
        return 1
    elif ConditionGroup(2):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z206, -1, -4, 0)
        CompareObjState(0, z206, 30, 0)
        assert ConditionGroup(0)
        """State 20: Door from right to bottom"""
        return 2
    elif ConditionGroup(3):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z206, -1, -4, 0)
        CompareObjState(0, z206, 30, 0)
        assert ConditionGroup(0)
        """State 21: Door from bottom to left"""
        return 3

def event_m50_35_x49(z104=_, z210=_, z211=_, z105=_, z212=80, z213=10):
    """[Execution] Door rotated by switch
    z104: Revolving door OBJ instance ID
    z210: Pillar operation OBJ state ID
    z211: OBJ state ID for which the column has ended
    z105: Switch OBJ instance ID
    z212: Switch operation OBJ state ID
    z213: Switch operation end OBJ state ID
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z105, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z105, 30, 0)
    assert ConditionGroup(0)
    """State 1: The door rotates"""
    ChangeObjState(z104, z210)
    """State 3: Waiting for the column to finish operation"""
    CompareObjState(0, z104, z211, 0)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z105, z212)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z105, z213, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_35_x50(z205=_, z206=_, z207=10):
    """[Preset] Door rotated by switch
    z205: Revolving door OBJ instance ID
    z206: Switch OBJ instance ID
    z207: Initial state OBJ state ID
    """
    """State 0,1: [Reproduction] Door Rotated by Switch_SubState"""
    assert event_m50_35_x47(z206=z206, z205=z205, z207=z207)
    """State 3: [Condition] Door rotated by switch_SubState"""
    call = event_m50_35_x48(z206=z206, z205=z205)
    if call.Get() == 0:
        """State 2: [Execution] Door rotated by switch_SubState"""
        assert event_m50_35_x49(z104=z205, z210=70, z211=30, z105=z206, z212=80, z213=10)
    elif call.Get() == 1:
        """State 4: [Execution] Door rotated by switch_2_SubState"""
        assert event_m50_35_x49(z104=z205, z210=72, z211=32, z105=z206, z212=80, z213=10)
    elif call.Get() == 2:
        """State 5: [Execution] Door rotated by switch_3_SubState"""
        assert event_m50_35_x49(z104=z205, z210=74, z211=34, z105=z206, z212=80, z213=10)
    elif call.Get() == 3:
        """State 6: [Execution] Door rotated by switch_4_SubState"""
        assert event_m50_35_x49(z104=z205, z210=76, z211=10, z105=z206, z212=80, z213=10)
    elif call.Get() == 4:
        """State 7: [Execution] Door revolving with switch_Return switch_SubState"""
        assert event_m50_35_x51(z105=z206, z208=80, z209=10)
    elif call.Get() == 5:
        """State 8: [Execution] Door revolving with switch_Return switch_2_SubState"""
        assert event_m50_35_x51(z105=z206, z208=80, z209=10)
    elif call.Get() == 6:
        """State 9: [Execution] Door rotated by switch_Switch return_3_SubState"""
        assert event_m50_35_x51(z105=z206, z208=80, z209=10)
    elif call.Get() == 7:
        """State 10: [Execution] Door rotated by switch_Switch return_4_SubState"""
        assert event_m50_35_x51(z105=z206, z208=80, z209=10)
    """State 11: End state"""
    return 0

def event_m50_35_x51(z105=_, z208=80, z209=10):
    """[Execution] Door rotated by switch_Return switch
    z105: Switch OBJ instance ID
    z208: Switch operation OBJ state ID
    z209: Switch operation end OBJ state ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z105, z208)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z105, z209, 0)
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

def event_m50_35_x53(z203=5, z204=50351350):
    """[Conditions] Multiple doors in ruins
    z203: Reaction distance
    z204: Door OBJ instance ID
    """
    """State 0,1: Did you approach the door?"""
    CompareObjPlayerDistance(0, z204, z203, 5)
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

def event_m50_35_x55(z203=5):
    """[Preset] Multiple doors of ruins
    z203: Reaction distance
    """
    """State 0,1: [Reproduction] Multiple doors of ruins_continuous version_SubState"""
    call = event_m50_35_x52()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Multiple doors of ruins_SubState"""
        assert event_m50_35_x53(z203=z203, z204=50351350)
        """State 2: [Execution] Multiple doors of ruins_Continuous version_SubState"""
        assert event_m50_35_x54()
    elif call.Get() == 2:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x56(z200=50353100):
    """[Reproduction] Spear from the left and right with the switch
    z200: Switch OBJ instance ID
    """
    """State 0,1: Is the switch down?"""
    if CompareObjStateId(z200, 30, 0):
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
        ChangeObjState(z200, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z200, 10, 0)
    else:
        pass
    """State 5: End state"""
    return 0

def event_m50_35_x57(z200=50353100):
    """[Condition] Spear from the left and right with the switch
    z200: Switch OBJ instance ID
    """
    """State 0,1: Switch judgment"""
    IsObjDamaged(0, z200, -1, -4, 0)
    CompareObjState(0, z200, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x58(z200=50353100, z201=0.2, z202=0.3):
    """[Execute] Spear from the left and right with the switch
    z200: Switch OBJ instance ID
    z201: Wait time
    z202: Cool time
    """
    """State 0,13: Switch is up"""
    ChangeObjState(z200, 70)
    """State 14: Waiting for switch operation to end"""
    CompareObjState(0, z200, 30, 0)
    assert ConditionGroup(0)
    """State 1: Spear jumps out"""
    ChangeObjState(50351397, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 5: Spear jumps out_2"""
    ChangeObjState(50351396, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 6: Spear jumps out _3"""
    ChangeObjState(50351395, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 7: Spear jumps out _4"""
    ChangeObjState(50351394, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 8: Spear jumps out _5"""
    ChangeObjState(50351393, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 9: Spear jumps out _6"""
    ChangeObjState(50351392, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 10: Spear jumps out_7"""
    ChangeObjState(50351391, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 11: Spear jumps out_8"""
    ChangeObjState(50351390, 70)
    CompareStateTime(0, z201, 2, z201)
    assert ConditionGroup(0)
    """State 3: Waiting for spear operation to end"""
    CompareObjState(0, 50351390, 10, 0)
    assert ConditionGroup(0)
    """State 12: Cool time"""
    CompareStateTime(0, z202, 2, z202)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z200, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z200, 10, 0)
    assert ConditionGroup(0)
    """State 15: End state"""
    return 0

def event_m50_35_x59(z200=50353100, z201=0.2, z202=0.3):
    """[Preset] Switch from the left and right with the switch
    z200: Switch OBJ instance ID
    z201: Wait time
    z202: Cool time
    """
    """State 0,1: [Reproduction] Spear _SubState from the left and right with the switch"""
    assert event_m50_35_x56(z200=z200)
    """State 3: [Condition] From the left and right with the switch _SubState"""
    assert event_m50_35_x57(z200=z200)
    """State 2: [Execute] From the left and right with the switch _SubState"""
    assert event_m50_35_x58(z200=z200, z201=z201, z202=z202)
    """State 4: End state"""
    return 0

def event_m50_35_x60(z198=_, z197=_, z199=_):
    """[Reproduction] Door that opens only once with a switch
    z198: Door OBJ instance ID
    z197: Switch OBJ instance ID
    z199: Navigation switching point ID
    """
    """State 0,2: Is the door in the initial state?"""
    if CompareObjStateId(z198, 10, 1):
        """State 3: Waiting for door to finish operation"""
        assert CompareObjStateId(z198, 20, 0)
        """State 1: Navi switching_passable"""
        DeleteNavimeshAttribute(z199, 2)
        """State 5: End of operation"""
        return 1
    else:
        """State 4: Not executed"""
        return 0

def event_m50_35_x61(z197=_):
    """[Condition] Door that opens only once with switch
    z197: Switch OBJ instance ID
    """
    """State 0,1: Switch damage judgment"""
    IsObjDamaged(0, z197, -1, -4, 0)
    assert ConditionGroup(0)
    """State 2: Activate the door"""
    return 0

def event_m50_35_x62(z198=_, z197=_, z199=_):
    """[Execute] Door that opens only once with a switch
    z198: Door OBJ instance ID
    z197: Switch OBJ instance ID
    z199: Navigation switching point ID
    """
    """State 0,3: Switch is up"""
    ChangeObjState(z197, 70)
    """State 4: Waiting for switch operation to end"""
    CompareObjState(0, z197, 30, 0)
    assert ConditionGroup(0)
    """State 1: The door is in operation"""
    ChangeObjState(z198, 70)
    """State 2: Waiting for door to finish operation"""
    CompareObjState(0, z198, 20, 0)
    assert ConditionGroup(0)
    """State 5: Navi mesh switching_passable"""
    DeleteNavimeshAttribute(z199, 2)
    """State 6: End state"""
    return 0

def event_m50_35_x63(z197=_, z198=_, z199=_):
    """[Preset] Door that opens only once with a switch
    z197: Switch OBJ instance ID
    z198: Door OBJ instance ID
    z199: Navigation switching point ID
    """
    """State 0,1: [Reproduction] Door that opens only once with switch _SubState"""
    call = event_m50_35_x60(z198=z198, z197=z197, z199=z199)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Door that opens only once with switch_SubState"""
        assert event_m50_35_x61(z197=z197)
        """State 2: [Execution] Door that opens only once with a switch_SubState"""
        assert event_m50_35_x62(z198=z198, z197=z197, z199=z199)
    """State 4: End state"""
    return 0

def event_m50_35_x64(z195=50353115, z194=50351450):
    """[Reproduction] Machine gun bow and arrow
    z195: Switch OBJ instance ID
    z194: Injection port OBJ instance ID
    """
    """State 0,1: The injection port is stationary, but the switch remains down?"""
    if CompareObjStateId(z195, 30, 0) and CompareObjStateId(z194, 10, 0):
        """State 2: Return only the switch"""
        ChangeObjState(z195, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z195, 10, 0)
    else:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x65(z195=50353115):
    """[Condition] Machine gun bow and arrow
    z195: Switch OBJ instance ID
    """
    """State 0,1: Switch judgment"""
    IsObjDamaged(0, z195, -1, -4, 0)
    CompareObjState(0, z195, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x66(z194=50351450, z195=50353115, z196=1.5):
    """[Execution] machine gun bow and arrow
    z194: Injection port OBJ instance ID
    z195: Switch OBJ instance ID
    z196: Cool time
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z195, 70)
    """State 7: Waiting for switch operation to end"""
    CompareObjState(0, z195, 30, 0)
    assert ConditionGroup(0)
    """State 1: Arrows pop out"""
    ChangeObjState(z194, 70)
    """State 5: Spear waiting"""
    CompareObjState(0, z194, 70, 0)
    assert ConditionGroup(0)
    """State 3: Cool time"""
    CompareStateTime(0, z196, 2, z196)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z195, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z195, 10, 0)
    assert ConditionGroup(0)
    """State 8: End state"""
    return 0

def event_m50_35_x67(z194=50351450, z195=50353115, z196=1.5):
    """[Preset] Machine gun bow and arrow
    z194: Injection port OBJ instance ID
    z195: Switch OBJ instance ID
    z196: Cool time
    """
    """State 0,1: [Reproduction] Machine gun bow and arrow_SubState"""
    assert event_m50_35_x64(z195=z195, z194=z194)
    """State 3: [Condition] Machine gun bow and arrow_SubState"""
    assert event_m50_35_x65(z195=z195)
    """State 2: [Execution] machine gun bow and arrow_SubState"""
    assert event_m50_35_x66(z194=z194, z195=z195, z196=z196)
    """State 4: End state"""
    return 0

def event_m50_35_x68(flag9=535000081, z65=8):
    """[Conditions] Door that opens when the boss is destroyed
    flag9: Boss destruction flag
    z65: Weight until door opens
    """
    """State 0,1: Has the boss been destroyed? Single?"""
    CompareEventFlag(0, flag9, 1)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 3: Multi start: Waiting for end"""
        IsMultiplayer(0, 0, 0)
        assert ConditionGroup(0)
        """State 5: Multi-end: Re-execute"""
        return 1
    elif ConditionGroup(0):
        """State 2: Wait"""
        CompareStateTime(0, z65, 3, z65)
        assert ConditionGroup(0)
        """State 4: End state"""
        return 0

def event_m50_35_x69(z64=50351500, val1=3002000):
    """[Execution] Door opened by boss destruction
    z64: Door OBJ instance ID
    val1: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z64, 70)
    """State 4: Ignored if there is no navigation switching"""
    if (not val1) != 0:
        pass
    else:
        """State 3: Waiting for the door to open"""
        CompareObjState(0, z64, 20, 0)
        assert ConditionGroup(0)
        """State 2: Navigation switching"""
        DeleteNavimeshAttribute(val1, 2)
    """State 5: End state"""
    return 0

def event_m50_35_x70(z64=50351500, flag9=535000081, val1=3002000):
    """[Reproduction] Door opened by boss destruction
    z64: Door OBJ instance ID
    flag9: Boss destruction flag
    val1: Navigation switching point ID
    """
    """State 0,6: Ignored if there is no navigation switching"""
    if (not val1) != 0:
        pass
    else:
        """State 3: Navigation switching_initialization"""
        AddNavimeshAttribute(val1, 2)
    """State 1: Has the boss been destroyed?"""
    if GetEventFlag(flag9) != 0:
        """State 2: Door opens"""
        ChangeObjState(z64, 70)
        """State 7: Ignored if there is no navigation switch_2"""
        if (not val1) != 0:
            pass
        else:
            """State 5: Waiting for the door to open"""
            assert CompareObjStateId(z64, 20, 0)
            """State 4: Navigation switching"""
            DeleteNavimeshAttribute(val1, 2)
        """State 9: Defeated"""
        return 1
    else:
        """State 8: Undefeated"""
        return 0

def event_m50_35_x71(z64=50351500, flag9=535000081, val1=3002000, z65=8):
    """[Preset] Door opened by boss defeat
    z64: Door OBJ instance ID
    flag9: Boss destruction flag
    val1: Navigation switching point ID
    z65: Weight until door opens
    """
    """State 0,1: [Reproduction] Door _SubState opened by boss destruction"""
    call = event_m50_35_x70(z64=z64, flag9=flag9, val1=val1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Door opened by boss destruction_SubState"""
        call = event_m50_35_x68(flag9=flag9, z65=z65)
        if call.Get() == 1:
            """State 4: [Execution] Door to open by destroying boss_Sky_SubState"""
            assert event_m50_35_x213()
            """State 6: Rerun"""
            return 1
        elif call.Done():
            """State 2: [Execution] Door opened by boss destruction_SubState"""
            assert event_m50_35_x69(z64=z64, val1=val1)
    """State 5: Finish"""
    return 0

def event_m50_35_x72():
    """[Reproduction] ghost knight materialization_OBJ"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x73(z192=_):
    """[Condition] Realization of ghost knight_OBJ
    z192: Materialized OBJ instance ID
    """
    """State 0,1: Has the materialized OBJ been destroyed?"""
    IsObjBroken(0, z192, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x74(z193=_):
    """[Execution] Realization of Ghost Knight_OBJ
    z193: Materialization flag
    """
    """State 0,1: Materialization flag ON"""
    SetEventFlag(z193, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x75(z192=_, z193=_):
    """[Preset] Realization of Ghost Knight_OBJ
    z192: Materialized OBJ instance ID
    z193: Materialization flag
    """
    """State 0,1: [Reproduction] Ghost Knight Materialization_OBJ_SubState"""
    assert event_m50_35_x72()
    """State 3: [Condition] Realization of ghost knight_OBJ_SubState"""
    assert event_m50_35_x73(z192=z192)
    """State 2: [Execution] Realization of Ghost Knight_OBJ_SubState"""
    assert event_m50_35_x74(z193=z193)
    """State 4: End state"""
    return 0

def event_m50_35_x76(z188=_, z189=_, z190=96650000, z191=96650010):
    """[Preset] Ghost Knight Materialization_Character
    z188: Materialization flag
    z189: Generator ID
    z190: Materialized special effect ID
    z191: Special effect ID for production
    """
    """State 0,1: [Reproduction] Realization of Ghost Knight_Character_SubState"""
    assert event_m50_35_x77()
    """State 3: [Condition] Realization of ghost knight_Chara_SubState"""
    call = event_m50_35_x78(z188=z188)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 2: [Execution] Realization of Ghost Knight_Character_SubState"""
        assert event_m50_35_x79(z189=z189, z190=z190, z188=z188, z191=z191)
    """State 4: End state"""
    return 0

def event_m50_35_x77():
    """[Reproduction] Realization of a ghost knight character"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x78(z188=_):
    """[Condition] Realization of ghost knight _ character
    z188: Materialization flag
    """
    """State 0,1: Materialization flag determination"""
    CompareEventFlag(0, z188, 1)
    if ConditionGroup(0):
        """State 2: Entity state"""
        return 0
    else:
        """State 3: Ghost state"""
        return 1

def event_m50_35_x79(z189=_, z190=96650000, z188=_, z191=96650010):
    """[Execution] Realization of a ghost knight character
    z189: Generator ID
    z190: Materialized special effect ID
    z188: Materialization flag
    z191: Special effect ID for production
    """
    """State 0,1: Grants special effects to ghost knights"""
    SetEnemySpEffect(z189, z190, 19, 4)
    """State 2: Materialization flag determination"""
    CompareEventFlag(0, z188, 1)
    assert ConditionGroup(0)
    """State 3: Cancel special effects"""
    ClearEnemySpEffect(z189, z190)
    """State 4: Special effects for directing ghost knights"""
    SetEnemySpEffect(z189, z191, 19, 4)
    """State 5: End state"""
    return 0

def event_m50_35_x80(z61=50352000, z62=5300000, z63=5300010):
    """[Preset] Door that opens with DLC purchase
    z61: Door OBJ instance ID
    z62: Navigation switching point ID
    z63: Judgment point ID
    """
    """State 0,1: [Reproduction] Doors opened with DLC purchase_SubState"""
    call = event_m50_35_x81(z61=z61, z62=z62)
    if call.Get() == 0:
        """State 3: [Conditions] Doors opened by DLC purchase_SubState"""
        call = event_m50_35_x82(z61=z61, z63=z63)
        if call.Get() == 0:
            """State 6: [Execution] Door opened by DLC purchase_Manual_SubState"""
            assert event_m50_35_x214(z61=z61, z62=z62)
            Goto('L0')
        elif call.Get() == 2:
            """State 5: [Execution] Door opened with DLC purchase_Auto_SubState"""
            assert event_m50_35_x83(z61=z61, z62=z62)
            Goto('L0')
        elif call.Get() == 1:
            """State 7: [Execution] Door that opens with DLC purchase_No access_Front_SubState"""
            assert event_m50_35_x84(z61=z61)
        elif call.Get() == 3:
            """State 8: [Execution] Door opened with DLC purchase_No access_Back_SubState"""
            assert event_m50_35_x224(z61=z61)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Conditions] Doors opened by DLC purchase_Guest_SubState"""
        assert event_m50_35_x85(z61=z61)
        """State 2: [Execution] Door opened with DLC purchase_Guest_SubState"""
        assert event_m50_35_x86(z61=z61, z62=z62)
    """State 10: Finish"""
    Label('L0')
    return 1

def event_m50_35_x81(z61=50352000, z62=5300000):
    """[Reproduction] Door opened with DLC purchase
    z61: Door OBJ instance ID
    z62: Navigation switching point ID
    """
    """State 0,2: Navigation switching_initialization"""
    AddNavimeshAttribute(z62, 2)
    """State 1: Host?"""
    if IsGuest() != 1:
        """State 3: Safety: Door initialization"""
        InitializeObj(z61)
        assert CompareObjStateId(z61, 10, 0)
        """State 4: Disable key guide"""
        DisableObjKeyGuide(z61, 1)
        """State 5: Not passed"""
        return 0
    else:
        """State 6: The guests"""
        return 1

def event_m50_35_x82(z61=50352000, z63=5300010):
    """[Conditions] Doors opened by DLC purchase
    z61: Door OBJ instance ID
    z63: Judgment point ID
    """
    """State 0,2: Distance judgment or point judgment"""
    CompareObjPlayerDistance(0, z61, 4, 5)
    SetConditionGroup(1, 8)
    IsPlayerInsidePoint(8, z63, z63, 1)
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

def event_m50_35_x83(z61=50352000, z62=5300000):
    """[Execution] Door opened with DLC purchase_Auto
    z61: Door OBJ instance ID
    z62: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z61, 20)
    """State 2: Waiting for the door to finish"""
    CompareObjState(0, z61, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z62, 2)
    """State 4: End state"""
    return 0

def event_m50_35_x84(z61=50352000):
    """[Execution] Door opened with DLC purchase
    z61: Door OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z61, 8, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x85(z61=50352000):
    """[Conditions] Doors opened with DLC purchase_Guest
    z61: Door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z61, 20, 0)
    assert ConditionGroup(0)
    """State 2: Mural opened"""
    return 0

def event_m50_35_x86(z61=50352000, z62=5300000):
    """[Execution] Door opened with DLC purchase_Guest
    z61: King's door OBJ instance ID
    z62: Navigation switching point ID
    """
    """State 0,1: Change navigation"""
    DeleteNavimeshAttribute(z62, 2)
    """State 2: End state"""
    return 0

def event_m50_35_x87(z33=50353310, z34=50351750, z35=50351760, z185=250, z186=251, z187=535000028):
    """[Reproduction] Switching thorn floor with switch
    z33: Switch OBJ instance ID
    z34: Thorn ① OBJ instance ID
    z35: Thorn ② OBJ instance ID
    z185: Replacement GM ①
    z186: Replacement GM ②
    z187: Thorn floor state flag
    """
    """State 0,4: Thorn state judgment"""
    if CompareObjStateId(z34, 10, 0) and CompareObjStateId(z35, 10, 0):
        """State 6: Thorn is falling or descending"""
        Label('L0')
        """State 10: Thorn floor state flag OFF"""
        SetEventFlag(z187, 0)
        """State 5: Grand material switching"""
        SetGroundMaterial(10, z185, 0)
        SetGroundMaterial(10, z186, 0)
    elif CompareObjStateId(z34, 80, 0) and CompareObjStateId(z35, 80, 0):
        Goto('L0')
    elif CompareObjStateId(z34, 30, 0) and CompareObjStateId(z35, 30, 0):
        """State 8: Thorns are rising or rising"""
        Label('L1')
        """State 9: Thorn floor state flag ON"""
        SetEventFlag(z187, 1)
        """State 7: Grand material switching_2"""
        SetGroundMaterial(10, z185, 1)
        SetGroundMaterial(10, z186, 1)
    elif CompareObjStateId(z34, 70, 0) and CompareObjStateId(z35, 70, 0):
        Goto('L1')
    """State 1: The thorns are stationary, but the switch remains down?"""
    if CompareObjStateId(z33, 30, 0) and CompareObjStateId(z34, 30, 0) and CompareObjStateId(z35, 30, 0):
        """State 2: Return only the switch"""
        Label('L2')
        ChangeObjState(z33, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z33, 10, 0)
    elif CompareObjStateId(z33, 30, 0) and CompareObjStateId(z34, 10, 0) and CompareObjStateId(z35, 10, 0):
        Goto('L2')
    else:
        pass
    """State 11: End state"""
    return 0

def event_m50_35_x88(z33=50353310, z34=50351750, z35=50351760):
    """[Condition] Switching thorn floor with switch
    z33: Switch OBJ instance ID
    z34: Thorn ① OBJ instance ID
    z35: Thorn ② OBJ instance ID
    """
    """State 0,2: Thorn state judgment"""
    CompareObjState(8, z34, 10, 0)
    CompareObjState(8, z35, 10, 0)
    CompareObjState(9, z34, 30, 0)
    CompareObjState(9, z35, 30, 0)
    CompareObjState(10, z34, 80, 0)
    CompareObjState(10, z35, 70, 0)
    CompareObjState(11, z34, 80, 0)
    CompareObjState(11, z35, 70, 0)
    if ConditionGroup(10):
        """State 6,8: Waiting for thorn to finish operation"""
        CompareObjState(8, z34, 10, 0)
        CompareObjState(8, z35, 10, 0)
        assert ConditionGroup(8)
        """State 12: Switch back after lowering"""
        return 2
    elif ConditionGroup(11):
        """State 5,9: Waiting for thorn to finish operation_2"""
        CompareObjState(8, z34, 30, 0)
        CompareObjState(8, z35, 30, 0)
        assert ConditionGroup(8)
        """State 13: Switch back after lift"""
        return 3
    elif ConditionGroup(8):
        """State 3,1: Switch judgment"""
        IsObjDamaged(0, z33, -1, -4, 0)
        assert ConditionGroup(0)
        """State 10: Raise thorns"""
        return 0
    elif ConditionGroup(9):
        """State 4,7: Switch judgment_2"""
        IsObjDamaged(0, z33, -1, -4, 0)
        assert ConditionGroup(0)
        """State 11: Lower thorns"""
        return 1

def event_m50_35_x89(z34=50351750, z180=_, z181=_, z33=50353310, z35=50351760, z182=250, z183=251, z184=_):
    """[Execute] Switch thorn floor with switch_flag ON
    z34: Thorn ① OBJ instance ID
    z180: Operating OBJ state ID
    z181: Thorn Operation End OBJ State ID
    z33: Switch OBJ instance ID
    z35: Thorn ② OBJ instance ID
    z182: Replacement GM ①
    z183: Replacement GM ②
    z184: GM slot
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z33, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z33, 30, 0)
    assert ConditionGroup(0)
    """State 1: Thorn is in operation"""
    ChangeObjState(z34, z180)
    ChangeObjState(z35, z180)
    """State 8: weight"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 7: Grand material switching"""
    SetGroundMaterial(10, z182, z184)
    SetGroundMaterial(10, z183, z184)
    """State 3: Waiting for thorn to finish operation"""
    CompareObjState(8, z34, z181, 0)
    CompareObjState(8, z35, z181, 0)
    assert ConditionGroup(8)
    """State 9: Thorn floor state flag ON"""
    SetEventFlag(535000028, 1)
    """State 2: Switch back"""
    ChangeObjState(z33, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z33, 10, 0)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m50_35_x90(z33=50353310):
    """[Execution] Switch thorn floor with switch_Return switch
    z33: Switch OBJ instance ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z33, 80)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z33, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x91(z33=50353310, z34=50351750, z35=50351760):
    """[Preset] Switch thorn floor with switch
    z33: Switch OBJ instance ID
    z34: Thorn ① OBJ instance ID
    z35: Thorn ② OBJ instance ID
    """
    """State 0,1: [Reproduction] Switching thorn floor with switch_SubState"""
    assert event_m50_35_x87(z33=z33, z34=z34, z35=z35, z185=250, z186=251, z187=535000028)
    """State 4: [Condition] Switching thorn floor with switch_SubState"""
    call = event_m50_35_x88(z33=z33, z34=z34, z35=z35)
    if call.Get() == 2:
        """State 6: [Execution] Switch thorn floor with switch_Return switch after descending_SubState"""
        assert event_m50_35_x90(z33=z33)
    elif call.Get() == 3:
        """State 3: [Execution] Switch thorn floor with switch_Return switch after rising_SubState"""
        assert event_m50_35_x90(z33=z33)
    elif call.Get() == 0:
        """State 8: [Execute] Switch thorn floor with switch_flag ON_SubState"""
        assert event_m50_35_x89(z34=z34, z180=70, z181=30, z33=z33, z35=z35, z182=250, z183=251, z184=1)
    elif call.Get() == 1:
        """State 7: [Execute] Switch thorn floor with switch_Flag OFF_SubState"""
        assert event_m50_35_x229(z34=z34, z36=80, z37=10, z33=z33, z35=z35, z38=250, z39=251, z40=0)
    """State 9: End state"""
    return 0
    """Unused"""
    """State 2: [Execution] Switching thorn floor with switch_Rise_SubState"""
    event_m50_35_x89(z34=z34, z180=70, z181=30, z33=z33, z35=z35, z182=250, z183=251, z184=1)
    Quit()
    """State 5: [Execution] Switching thorn floor with switch_Descent_SubState"""
    event_m50_35_x89(z34=z34, z180=80, z181=10, z33=z33, z35=z35, z182=250, z183=251, z184=0)
    Quit()

def event_m50_35_x92(z177=50353740, z178=50353751, z179=50353750):
    """[Reproduction] Bridge tower rises
    z177: Switch OBJ instance ID
    z178: Bridge tower ②_OBJ instance ID
    z179: Bridge tower ③_OBJ instance ID
    """
    """State 0,1: Do you have dragon eyes?"""
    if CompareObjStateId(z177, 20, 0):
        pass
    else:
        Goto('L1')
    """State 4: State determination of bridge 2"""
    if CompareObjStateId(z178, 10, 1):
        """State 5: State determination of bridge 3"""
        if CompareObjStateId(z179, 10, 1):
            pass
        else:
            """State 3: Bridge 3 rises"""
            Label('L0')
            ChangeObjState(z179, 70)
    else:
        """State 2: Bridge 2 rises"""
        ChangeObjState(z178, 70)
        assert (GetStateTime() > 3) != 0
        Goto('L0')
    """State 7: End of operation"""
    return 1
    """State 6: Not executed"""
    Label('L1')
    return 0

def event_m50_35_x93(z177=50353740):
    """[Condition] Bridge tower rises
    z177: Switch OBJ instance ID
    """
    """State 0,1: Judgment of dragon's eyes"""
    CompareObjState(0, z177, 20, 0)
    assert ConditionGroup(0)
    """State 2: Lift the bridge"""
    return 0

def event_m50_35_x94(z177=50353740, z178=50353751, z179=50353750):
    """[Execution] Bridge tower rises
    z177: Switch OBJ instance ID
    z178: Bridge tower ②_OBJ instance ID
    z179: Bridge tower ③_OBJ instance ID
    """
    """State 0,1: Bridge 2 rises"""
    ChangeObjState(z178, 70)
    """State 3: Weight_2"""
    CompareStateTime(0, 3, 3, 3)
    assert ConditionGroup(0)
    """State 4: Bridge 3 rises"""
    ChangeObjState(z179, 70)
    """State 2: Waiting for completion of bridge operation"""
    CompareObjState(8, z178, 20, 0)
    CompareObjState(8, z179, 20, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m50_35_x95(z177=50353740, z178=50353751, z179=50353750):
    """[Preset] Bridge tower rises
    z177: Switch OBJ instance ID
    z178: Bridge tower ②_OBJ instance ID
    z179: Bridge tower ③_OBJ instance ID
    """
    """State 0,1: [Reproduction] Bridge tower rises_SubState"""
    call = event_m50_35_x92(z177=z177, z178=z178, z179=z179)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Bridge tower rises_SubState"""
        assert event_m50_35_x93(z177=z177)
        """State 2: [Execution] Bridge tower rises_SubState"""
        assert event_m50_35_x94(z177=z177, z178=z178, z179=z179)
    """State 4: End state"""
    return 0

def event_m50_35_x96(flag6=535000032, flag7=535000034, z47=50352100):
    """[Reproduction] Awakening Dragon
    flag6: Event 1 executed flag
    flag7: Event 2 executed flag
    z47: Dragon OBJ instance ID
    """
    """State 0,2: Have you completed flight event 2?"""
    if GetEventFlag(flag7) != 0:
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
    ChangeObjState(z47, 20)
    assert CompareObjStateId(z47, 20, 0)
    """State 8: Event complete"""
    return 2
    """State 1: Has flight event 1 been executed?"""
    Label('L0')
    if GetEventFlag(flag6) != 0:
        """State 4: Dragon on top"""
        ChangeObjState(z47, 30)
        assert CompareObjStateId(z47, 30, 0)
        """State 7: Resume from event 2"""
        return 1
    else:
        """State 6: Event not executed"""
        return 0

def event_m50_35_x97(z47=50352100, z48=3405000, z51=3405001):
    """[Condition] Awakening Dragon
    z47: Dragon OBJ instance ID
    z48: Flight 1 start point ID
    z51: Flight 1 end point ID
    """
    """State 0,1: Damaged or point intrusion"""
    IsObjDamaged(0, z47, -1, -3, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(8, z48, z51, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(0)
    """State 2: Flight event"""
    return 0

def event_m50_35_x98(flag6=535000032, z47=50352100, z175=70, z176=30):
    """[Execution] Awakening Dragon
    flag6: Event executed flag
    z47: Dragon OBJ instance ID
    z175: Flight OBJ State ID
    z176: OBJ state ID after flight
    """
    """State 0,1: Executed flag ON"""
    SetEventFlag(flag6, 1)
    """State 2: Dragon flying"""
    ChangeObjState(z47, z175)
    """State 3: Wait for end of flight"""
    CompareObjState(0, z47, z176, 0)
    assert ConditionGroup(0)
    """State 4: Finish"""
    return 0

def event_m50_35_x99(flag6=535000032, flag7=535000034, z47=50352100, z48=3405000, z49=3405010, z50=3405011,
                     z51=3405001):
    """[Preset] Awakening Dragon
    flag6: Event 1 executed flag
    flag7: Event 2 executed flag
    z47: Dragon OBJ instance ID
    z48: Flight 1 start point ID
    z49: Flight 2 start point ID
    z50: Flight 2 end point ID
    z51: Flight 1 end point ID
    """
    """State 0,1: [Reproduction] Awakening Dragon_SubState"""
    call = event_m50_35_x96(flag6=flag6, flag7=flag7, z47=z47)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        """State 5: [Condition] Awakening Dragon_Points only_SubState"""
        Label('L0')
        assert event_m50_35_x161(z47=z47, z49=z49, z50=z50)
        """State 6: [Execution] Awakening Dragon _ 2nd_SubState"""
        assert event_m50_35_x226(flag7=flag7, z47=z47, z52=71, z53=20)
    elif call.Get() == 0:
        """State 3: [Condition] Awakening Dragon_SubState"""
        assert event_m50_35_x97(z47=z47, z48=z48, z51=z51)
        """State 2: [Execution] Awakening Dragon_SubState"""
        assert event_m50_35_x98(flag6=flag6, z47=z47, z175=70, z176=30)
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

def event_m50_35_x104(z172=_, val2=_, val3=_, z173=_):
    """[Reproduction] Door that rotates with switch_Navigation switching and flag switching
    z172: Revolving door instance ID
    val2: Upper navigation switching point ID
    val3: Lower navigation switching point ID
    z173: Enemy activation flag
    """
    """State 0,7: Navigation switching"""
    AddNavimeshAttribute(val2, 2)
    AddNavimeshAttribute(val3, 2)
    """State 1: Judgment of door status"""
    if CompareObjStateId(z172, 10, 0):
        """State 2,15: Enemy activation flag OFF"""
        SetEventFlag(z173, 0)
    elif CompareObjStateId(z172, 30, 0):
        """State 3,8: Navigation switching_Upper traffic"""
        DeleteNavimeshAttribute(val2, 2)
        """State 14: Enemy activation flag ON"""
        SetEventFlag(z173, 1)
    elif CompareObjStateId(z172, 32, 0):
        """State 4,18: Enemy activation flag OFF_4"""
        SetEventFlag(z173, 0)
    elif CompareObjStateId(z172, 34, 0):
        """State 5,9: Navigation switch"""
        DeleteNavimeshAttribute(val3, 2)
        """State 20: Enemy activation flag OFF_6"""
        SetEventFlag(z173, 0)
    elif CompareObjStateId(z172, 41, 0):
        """State 10,16: Enemy activation flag OFF_2"""
        SetEventFlag(z173, 0)
    elif CompareObjStateId(z172, 40, 0):
        """State 11,17: Enemy activation flag OFF_3"""
        SetEventFlag(z173, 0)
    elif CompareObjStateId(z172, 43, 0):
        """State 12,19: Enemy activation flag OFF_5"""
        SetEventFlag(z173, 0)
    elif CompareObjStateId(z172, 42, 0):
        """State 13,21: Enemy activation flag OFF_7"""
        SetEventFlag(z173, 0)
    else:
        """State 6,22: Enemy activation flag OFF_8"""
        SetEventFlag(z173, 0)
    """State 23: End state"""
    return 0

def event_m50_35_x105(z172=_, val2=_, val3=_):
    """[Conditions] Doors rotated by switch_Navigation switching and flag switching
    z172: Revolving door instance ID
    val2: Upper navigation switching point
    val3: Bottom navigation switching point
    """
    """State 0,6: Waiting for door rotation"""
    CompareObjState(0, z172, 70, 0)
    CompareObjState(0, z172, 72, 0)
    CompareObjState(0, z172, 74, 0)
    CompareObjState(0, z172, 76, 0)
    CompareObjState(0, z172, 80, 0)
    CompareObjState(0, z172, 81, 0)
    CompareObjState(0, z172, 82, 0)
    CompareObjState(0, z172, 83, 0)
    CompareObjState(0, z172, 84, 0)
    CompareObjState(0, z172, 85, 0)
    CompareObjState(0, z172, 86, 0)
    CompareObjState(0, z172, 87, 0)
    assert ConditionGroup(0)
    """State 7: Navigation switching"""
    AddNavimeshAttribute(val2, 2)
    AddNavimeshAttribute(val3, 2)
    """State 1: Judgment of door status"""
    CompareObjState(0, z172, 10, 0)
    CompareObjState(1, z172, 41, 0)
    CompareObjState(2, z172, 30, 0)
    CompareObjState(3, z172, 40, 0)
    CompareObjState(4, z172, 32, 0)
    CompareObjState(5, z172, 43, 0)
    CompareObjState(6, z172, 34, 0)
    CompareObjState(7, z172, 42, 0)
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

def event_m50_35_x106(val2=_, z173=_, z174=_):
    """[Execution] Rotating door with a switch
    val2: Point ID of the navigation to switch
    z173: Enemy activation flag
    z174: Flag ONOFF
    """
    """State 0,3: Is switching required?"""
    if (not val2) != 0:
        pass
    else:
        """State 1: Navigation switching"""
        DeleteNavimeshAttribute(val2, 2)
    """State 2: Switch enemy activation flag"""
    SetEventFlag(z173, z174)
    """State 4: End state"""
    return 0

def event_m50_35_x107(z172=_, val2=_, val3=_, z173=_):
    """[Preset] Rotating door with switch _ Navi switching and flag switching
    z172: Revolving door instance ID
    val2: Upper navigation switching point
    val3: Bottom navigation switching point
    z173: Enemy activation flag
    """
    """State 0,1: [Reproduction] Door that rotates with switch_Navigation switching and flag switching_SubState"""
    assert event_m50_35_x104(z172=z172, val2=val2, val3=val3, z173=z173)
    """State 3: [Condition] Door rotated by switch_Navigation switching and flag switching_SubState"""
    call = event_m50_35_x105(z172=z172, val2=val2, val3=val3)
    if call.Get() == 0:
        """State 2: [Execution] Door rotated by switch_Navigation switching and flag switching_SubState"""
        assert event_m50_35_x106(val2=0, z173=z173, z174=0)
    elif call.Get() == 4:
        """State 4: [Execution] Door rotated by switch_Navigation switching and flag switching_2_SubState"""
        assert event_m50_35_x106(val2=0, z173=z173, z174=0)
    elif call.Get() == 1:
        """State 5: [Execution] Door rotated by switch_Navigation switching and flag switching_3_SubState"""
        assert event_m50_35_x106(val2=val2, z173=z173, z174=1)
    elif call.Get() == 5:
        """State 6: [Execution] Door rotated by switch_Navigation switching and flag switching_4_SubState"""
        assert event_m50_35_x106(val2=0, z173=z173, z174=0)
    elif call.Get() == 2:
        """State 7: [Execution] Door rotated by switch_Navigation switching and flag switching_5_SubState"""
        assert event_m50_35_x106(val2=0, z173=z173, z174=0)
    elif call.Get() == 6:
        """State 8: [Execution] Door rotated by switch_Navigation switching and flag switching_6_SubState"""
        assert event_m50_35_x106(val2=0, z173=z173, z174=0)
    elif call.Get() == 3:
        """State 9: [Execution] Door rotated by switch_Navigation switching and flag switching_7_SubState"""
        assert event_m50_35_x106(val2=val3, z173=z173, z174=0)
    elif call.Get() == 7:
        """State 10: [Execution] Door rotated by switch_Navigation switching and flag switching_8_SubState"""
        assert event_m50_35_x106(val2=0, z173=z173, z174=0)
    """State 11: End state"""
    return 0

def event_m50_35_x108(z152=50353751, z153=50353750, z154=603010, z155=603020):
    """[Reproduction] Bridge tower rises _ navigation switching
    z152: Instance ID of bridge 2
    z153: Instance ID of bridge 3
    z154: Bridge 2 navigation switching point ID
    z155: Bridge 3 navigation switching point ID
    """
    """State 0,1: Judgment of bridge 2 status"""
    if CompareObjStateId(z152, 10, 1):
        """State 2: Standby waiting for Bridge 2"""
        assert CompareObjStateId(z152, 20, 0)
        """State 3: Bridge 2 navigation switch_operation waiting for bridge 3"""
        DeleteNavimeshAttribute(z154, 2)
        assert CompareObjStateId(z153, 20, 0)
        """State 4: Bridge 3 navigation switching"""
        DeleteNavimeshAttribute(z155, 2)
        """State 6: Finished"""
        return 1
    else:
        """State 5: End state"""
        return 0

def event_m50_35_x109(z152=50353751, z171=50353751, z154=603010, z155=603020):
    """[Execution] Bridge tower rises
    z152: Instance ID of bridge 2
    z171: Instance ID of bridge 3
    z154: Bridge 2 navigation switching point ID
    z155: Bridge 3 navigation switching point ID
    """
    """State 0,1: Standby waiting for Bridge 2"""
    CompareObjState(0, z152, 20, 0)
    assert ConditionGroup(0)
    """State 2: Bridge 2 navigation switching"""
    DeleteNavimeshAttribute(z154, 2)
    """State 3: Standby operation of bridge 3"""
    CompareObjState(0, z171, 20, 0)
    assert ConditionGroup(0)
    """State 4: Bridge 3 navigation switching"""
    DeleteNavimeshAttribute(z155, 2)
    """State 5: End state"""
    return 0

def event_m50_35_x110(z152=50353751, z153=50353750, z154=603010, z155=603020, z156=50353740):
    """[Preset] Bridge tower rises
    z152: Tower 2 instance ID
    z153: Tower 3 instance ID
    z154: Tower 2 navigation switching point ID
    z155: Tower 3 navigation switching point ID
    z156: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] The tower of the bridge is rising_Navigation switching_SubState"""
    call = event_m50_35_x108(z152=z152, z153=z153, z154=z154, z155=z155)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Condition] Bridge tower rises_Navigation switch_SubState"""
        assert event_m50_35_x128(z156=z156)
        """State 2: [Execution] Bridge tower rises_Navigation switch_SubState"""
        assert event_m50_35_x109(z152=z152, z171=z152, z154=z154, z155=z155)
    """State 4: End state"""
    return 0

def event_m50_35_x111(flag16=535000081, z158=501, z159=5030000, z160=535020080, z161=6.5, z162=3000000,
                      z163=900, z164=4):
    """[Preset] Boss battle _ BGM playback and HP display by canceling the activation state
    flag16: Boss destruction flag
    z158: Sound ID
    z159: Boss Battle ID
    z160: Other flags for logic
    z161: Wait time
    z162: Start and end point ID
    z163: Boss generator ID
    z164: Wait until startup
    """
    """State 0,1: [Reproduction] Boss Battle_BGM playback and HP display with start state release_Start_SubState"""
    call = event_m50_35_x112(flag16=flag16)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle _ BGM playback and HP display with start state release _ Start _ SubState"""
        assert event_m50_35_x113(z162=z162, z170=z162)
        """State 3: [Execution] Boss Battle _ BGM playback and HP display with start state release _ Start _ SubState"""
        assert event_m50_35_x114(z159=z159, z160=z160, z164=z164)
        """State 7: [Reproduction] HP display and BGM playback_empty_SubState"""
        assert event_m50_35_x115()
        """State 9: [Condition] HP display and BGM playback_SubState"""
        call = event_m50_35_x116(z163=z163, z168=2, z169=535000085)
        if call.Get() == 0:
            """State 8: [Execution] HP display and BGM playback_SubState"""
            assert event_m50_35_x117(z158=z158, z161=z161, z159=z159, z166=535020084, z167=535000085)
        elif call.Get() == 1:
            """State 10: [Execution] HP display and BGM playback_2_SubState"""
            assert event_m50_35_x117(z158=z158, z161=8, z159=z159, z166=535020084, z167=535000085)
        """State 2: [Reproduction] Boss battle _ BGM playback and HP display with start state release _ End _ Empty _ SubState"""
        assert event_m50_35_x118()
        """State 6: [Condition] Boss Battle _ BGM playback and HP display with start state release _ End judgment _ SubState"""
        assert event_m50_35_x119(z159=z159)
        """State 4: [Execution] Boss Battle _ BGM playback and HP display by canceling the startup state _ End _ SubState"""
        assert event_m50_35_x120(z158=z158, z159=z159, z160=z160, z165=0)
    """State 11: End state"""
    return 0

def event_m50_35_x112(flag16=535000081):
    """[Reproduction] Boss Battle _ BGM playback and HP display with start state release _ Start
    flag16: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag16) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_35_x113(z162=3000000, z170=3000000):
    """[Condition] Boss Battle _ Start BGM playback and HP display _ start state release
    z162: Start point ID
    z170: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z162, z170, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z162, z170, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x114(z159=5030000, z160=535020080, z164=4):
    """[Execution] Boss Battle_BGM playback and HP display with start state release_Start
    z159: Boss Battle ID
    z160: Logic flag
    z164: Wait until boss activation
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z159)
    """State 3: Wait until startup"""
    CompareStateTime(0, z164, 3, z164)
    CompareEventFlag(0, 535020080, 1)
    assert ConditionGroup(0)
    """State 2: Logic flag ON"""
    SetEventFlag(z160, 1)
    """State 4: End state"""
    return 0

def event_m50_35_x115():
    """[Reproduction] HP display and BGM playback_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x116(z163=900, z168=2, z169=535000085):
    """[Condition] HP display and BGM playback
    z163: Boss generator ID
    z168: Activation state ID
    z169: Rematch flag
    """
    """State 0,1: Did the boss release the activation state?"""
    CompareChrEzStateValue(0, z163, 7, 1, 0)
    IsEventBossKill(0, z163, 0, 1)
    CompareChrStartUpState(0, z163, z168, 1)
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

def event_m50_35_x117(z158=501, z161=_, z159=5030000, z166=535020084, z167=535000085):
    """[Execution] HP display and BGM playback
    z158: Sound ID
    z161: Wait time until display
    z159: Boss Battle ID
    z166: BGM and gauge display flag
    z167: Rematch flag
    """
    """State 0,3: Wait until BGM playback and HP display"""
    CompareStateTime(0, z161, 2, z161)
    IsEventBossKill(1, z159, 0, 1)
    CompareEventFlag(0, z166, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z158)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 4: BGM and gauge display flag ON"""
    SetEventFlag(z166, 1)
    """State 5: Rematch determination flag ON"""
    SetEventFlag(z167, 1)
    """State 6: End state"""
    return 0

def event_m50_35_x118():
    """[Reproduction] Boss Battle _ BGM playback and HP display with start state release _ End _ Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x119(z159=5030000):
    """[Conditions] Boss battle_BGM playback and HP display with start state release_End judgment
    z159: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z159, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x120(z158=501, z159=5030000, z160=535020080, z165=0):
    """[Execution] Boss battle _ BGM playback and HP display _ end by canceling the startup state
    z158: Sound ID
    z159: Boss Battle ID
    z160: Other flags for logic
    z165: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z160, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z159)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > 0) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z158)
    """State 5: End state"""
    return 0

def event_m50_35_x121(z157=50353740):
    """[Preset] Stone board to raise the tower of the bridge
    z157: Key person OBJ instance ID
    """
    """State 0,1: [Reproduction] Stone board to raise the tower of the bridge _SubState"""
    call = event_m50_35_x122(z157=z157)
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
    call = event_m50_35_x127(z157=z157)
    if call.Get() == 0:
        """State 3: [Execution] Stone board to raise the tower of the bridge_Host_Startable_SubState"""
        call = event_m50_35_x124(z157=z157)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: Start and end"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Stone board to raise the tower of the bridge _ Host _ Unable to start _ SubState"""
        assert event_m50_35_x125(z157=z157)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Stone board to lift the tower of the bridge_Guest_SubState"""
    Label('L1')
    assert event_m50_35_x126(z157=z157)
    """State 2: [Execution] Stone board to raise the tower of the bridge_Guest_Sky_SubState"""
    assert event_m50_35_x123()
    """State 9: Guest termination"""
    return 2

def event_m50_35_x122(z157=50353740):
    """[Reproduction] Stone board to lift the tower of the bridge
    z157: Key person OBJ instance ID
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
    if CompareObjStateId(z157, 30, 0):
        """State 3: OBJ initialization ： 10"""
        Label('L1')
        ChangeObjState(z157, 10)
        assert CompareObjStateId(z157, 10, 0)
    elif CompareObjStateId(z157, 70, 0):
        Goto('L1')
    elif CompareObjStateId(z157, 74, 1) and CompareObjStateId(z157, 20, 1):
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

def event_m50_35_x124(z157=50353740):
    """[Execution] Stone board to raise the tower of the bridge_Host_Startable
    z157: Key person OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:52650000:Dragon Stone
    DisplayYesNoMenu(1002, 1.8, z157, 190, 2, 52650000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 6: Stone board transition waiting: 30"""
        ChangeObjState(z157, 30)
        assert CompareObjStateId(z157, 30, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z157, 38, 3)
        assert PlayerIsInEventAction(11) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 3, 0)
        # goods:52650000:Dragon Stone
        DoesPlayerHaveItem(0, 52650000, 0, 5, 1, 1, 0)
        CompareObjState(1, z157, 74, 0)
        CompareObjState(1, z157, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Dragon eye consumption"""
            # goods:52650000:Dragon Stone
            ConsumeItem(52650000, 1)
            assert CompareObjStateId(z157, 20, 0)
            """State 8: Start and end"""
            return 0
    else:
        pass
    """State 7: Stone board: Initial state: 10"""
    ChangeObjState(z157, 10)
    """State 9: Rerun"""
    return 1

def event_m50_35_x125(z157=50353740):
    """[Execution] Stone board to raise the tower of the bridge
    z157: Key person OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:52650000:Dragon Stone
    DisplayOkMenu(1013, 0, 0, z157, 190, 2, 52650000, 0)
    assert OkMenuDisplay() != 1
    """State 2: Startup failure_rerun"""
    return 0

def event_m50_35_x126(z157=50353740):
    """[Condition] Stone board to lift the tower of the bridge_Guest
    z157: Key person OBJ instance ID
    """
    """State 0,1: Stone board end waiting"""
    CompareObjState(0, z157, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x127(z157=50353740):
    """[Condition] Stone board to lift the tower of the bridge_Host
    z157: Key person OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z157)
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

def event_m50_35_x128(z156=50353740):
    """[Condition] Bridge tower rises
    z156: Switch OBJ instance ID
    """
    """State 0,1: Judgment of dragon's eyes"""
    CompareObjState(0, z156, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x129(z143=_, z144=_, z145=_):
    """[Reproduction] Elevator with lid_Startup
    z143: Upper switch OBJ instance ID
    z144: Lower switch OBJ instance ID
    z145: Elevator OBJ instance ID
    """
    """State 0,2: Is the elevator started?"""
    if CompareObjStateId(z145, 11, 0):
        """State 1: Switch override for elevator"""
        Label('L0')
        ChangeObjState(z143, 30)
        ChangeObjState(z144, 30)
        """State 3: End state"""
        return 0
    elif CompareObjStateId(z145, 90, 0):
        Goto('L0')
    else:
        """State 4: Activated"""
        return 1

def event_m50_35_x130(z143=_, z144=_, z145=_, z146=_):
    """[Condition] Elevator with lid_Startup
    z143: Upper switch OBJ instance ID
    z144: Lower switch OBJ instance ID
    z145: Elevator OBJ instance ID
    z146: Stone statue switch OBJ instance ID
    """
    """State 0,1: Switch judgment"""
    IsObjDamaged(0, z146, -1, -4, 0)
    CompareObjState(0, z146, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x131(z148=_, z145=_, z146=_, z147=_):
    """[Execution] Elevator with lid_Start
    z148: Activation switch OBJ instance ID
    z145: Elevator OBJ instance ID
    z146: Stone statue switch OBJ instance ID
    z147: Elevator state after opening the lid
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z146, 70)
    """State 5: weight"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 1: Elevator operation with lid open: 90"""
    ChangeObjState(z145, 90)
    """State 2: Elevator lift waiting"""
    CompareObjState(0, z145, z147, 0)
    assert ConditionGroup(0)
    """State 3: Switch activation for elevator"""
    ChangeObjState(z148, 80)
    """State 4: Waiting for switch to be valid"""
    CompareObjState(0, z148, 10, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_35_x132():
    """[Reproduction] Elevator with lid_Switch_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x133(z149=_, z150=_):
    """[Condition] Elevator with lid_Switch
    z149: Elevator OBJ instance ID
    z150: Elevator state ID opposite the switch
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z149, z150, 0):
        """State 3: Switch activation"""
        return 1
    else:
        """State 2: Disable switch"""
        return 0

def event_m50_35_x134(z149=_, z150=_, z151=_):
    """[Execution] Elevator with lid_Switch_Effective
    z149: Elevator OBJ instance ID
    z150: Elevator state ID opposite the switch
    z151: Switch OBJ instance ID
    """
    """State 0,1: Activating the switch"""
    ChangeObjState(z151, 80)
    """State 2: Wait for switch activation"""
    CompareObjState(0, z151, 10, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    CompareObjState(0, z149, z150, 1)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x135(z149=_, z150=_, z151=_):
    """[Execution] Elevator with lid_Switch_Invalid
    z149: Elevator OBJ instance ID
    z150: Elevator state ID opposite the switch
    z151: Switch OBJ instance ID
    """
    """State 0,1: Disable switch"""
    ChangeObjState(z151, 70)
    """State 2: Wait for switch invalidation"""
    CompareObjState(0, z151, 30, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    CompareObjState(0, z149, z150, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x136(z149=_, z150=_, z151=_):
    """[Preset] Elevator with lid_Switch
    z149: Elevator OBJ instance ID
    z150: Elevator state ID opposite the switch
    z151: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator with lid_Switch_Empty_SubState"""
    assert event_m50_35_x132()
    """State 4: [Condition] Elevator with lid_Switch_SubState"""
    call = event_m50_35_x133(z149=z149, z150=z150)
    if call.Get() == 1:
        """State 3: [Execution] Elevator with lid_Switch_Effective_SubState"""
        assert event_m50_35_x134(z149=z149, z150=z150, z151=z151)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator with lid_Switch_Invalid_SubState"""
        assert event_m50_35_x135(z149=z149, z150=z150, z151=z151)
    """State 5: Rerun"""
    return 0

def event_m50_35_x137(z143=_, z144=_, z145=_, z146=_, z147=_, z148=_):
    """[Preset] Elevator with lid_Startup
    z143: Upper switch OBJ instance ID
    z144: Lower switch OBJ instance ID
    z145: Elevator OBJ instance ID
    z146: Stone statue switch OBJ instance ID
    z147: Elevator state after opening the lid
    z148: Activation switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator with lid_Startup_SubState"""
    call = event_m50_35_x129(z143=z143, z144=z144, z145=z145)
    if call.Get() == 0:
        """State 3: [Condition] Elevator with lid_Startup_SubState"""
        assert event_m50_35_x130(z143=z143, z144=z144, z145=z145, z146=z146)
        """State 2: [Execution] Elevator with lid_Startup_SubState"""
        assert event_m50_35_x131(z148=z148, z145=z145, z146=z146, z147=z147)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x138(z138=_, z139=_, z140=_, z141=_, z142=_):
    """[Preset] Elevator with lid
    z138: OBJ instance ID of the elevator
    z139: On elevator point ID_
    z140: Elevator point ID_below
    z141: Upper switch OBJ instance ID
    z142: Lower switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator with lid_SubState"""
    assert event_m50_35_x139()
    """State 6: [Condition] Elevator with lid_SubState"""
    call = event_m50_35_x140(z138=z138, z139=z139, z140=z140, z141=z141, z142=z142)
    if call.Get() == 2:
        """State 3: [Execution] Elevator with lid_Return switch after descending_SubState"""
        assert event_m50_35_x144(z138=z138, z140=z140, z141=z141, z142=z142)
    elif call.Get() == 3:
        """State 5: [Execution] Elevator with lid_Return switch after ascending_SubState"""
        assert event_m50_35_x143(z138=z138, z139=z139, z141=z141, z142=z142)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator with lid_Rise_SubState"""
        assert event_m50_35_x141(z138=z138, z139=z139, z142=z142, z141=z141)
    elif call.Get() == 1:
        """State 2: [Execution] Elevator with lid_Descent_SubState"""
        assert event_m50_35_x142(z138=z138, z140=z140, z141=z141, z142=z142)
    """State 7: End state"""
    return 0

def event_m50_35_x139():
    """[Reproduction] Elevator with lid"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x140(z138=_, z139=_, z140=_, z141=_, z142=_):
    """[Condition] Elevator with lid
    z138: Elevator OBJ instance ID
    z139: On elevator point ID_
    z140: Elevator point ID_below
    z141: Upper switch OBJ instance ID
    z142: Lower switch OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z138, 10, 0)
    CompareObjState(1, z138, 40, 0)
    CompareObjState(2, z138, 80, 0)
    CompareObjState(2, z138, 41, 0)
    CompareObjState(3, z138, 70, 0)
    CompareObjState(3, z138, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or switch standby"""
        IsPlayerInsidePoint(0, z140, z140, 1)
        IsObjDamaged(0, z141, -1, 0, 0)
        CompareObjState(0, z141, 30, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or switch standby_2"""
        IsPlayerInsidePoint(0, z139, z139, 1)
        IsObjDamaged(0, z142, -1, 0, 0)
        CompareObjState(0, z142, 30, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m50_35_x141(z138=_, z139=_, z142=_, z141=_):
    """[Execution] Elevator with lid _ Ascent
    z138: Elevator OBJ instance ID
    z139: On point ID_
    z142: Lower switch OBJ instance ID
    z141: Upper switch OBJ instance ID
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z138, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z138, 30, 0)
    IsPlayerInsidePoint(8, z139, z139, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Elevator switch returns"""
    ChangeObjState(z138, 71)
    """State 5: Wait for return of elevator switch"""
    CompareObjState(0, z138, 40, 0)
    assert ConditionGroup(0)
    """State 4: Waiting for switch status"""
    CompareObjState(8, z142, 10, 0)
    CompareObjState(8, z141, 30, 0)
    assert ConditionGroup(8)
    """State 6: End state"""
    return 0

def event_m50_35_x142(z138=_, z140=_, z141=_, z142=_):
    """[Execution] Elevator with lid_Descent
    z138: Elevator OBJ instance ID
    z140: Point ID_below
    z141: Upper switch OBJ instance ID
    z142: Lower switch OBJ instance ID
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z138, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z138, 41, 0)
    IsPlayerInsidePoint(8, z140, z140, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Elevator switch returns"""
    ChangeObjState(z138, 81)
    """State 5: Wait for return of elevator switch"""
    CompareObjState(0, z138, 10, 0)
    assert ConditionGroup(0)
    """State 4: Waiting for switch status"""
    CompareObjState(8, z141, 10, 0)
    CompareObjState(8, z142, 30, 0)
    assert ConditionGroup(8)
    """State 6: End state"""
    return 0

def event_m50_35_x143(z138=_, z139=_, z141=_, z142=_):
    """[Execution] Elevator with lid_Return the switch after the lift
    z138: Elevator OBJ instance ID
    z139: On point ID_
    z141: Upper switch OBJ instance ID
    z142: Lower switch OBJ instance ID
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z138, 30, 0)
    IsPlayerInsidePoint(8, z139, z139, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Elevator switch returns"""
    ChangeObjState(z138, 71)
    """State 4: Wait for return of elevator switch"""
    CompareObjState(0, z138, 40, 0)
    assert ConditionGroup(0)
    """State 3: Waiting for switch status"""
    CompareObjState(8, z142, 10, 0)
    CompareObjState(8, z141, 30, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m50_35_x144(z138=_, z140=_, z141=_, z142=_):
    """[Execution] Elevator with lid_Return switch after lowering
    z138: Elevator OBJ instance ID
    z140: Point ID_below
    z141: Upper switch OBJ instance ID
    z142: Lower switch OBJ instance ID
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z138, 41, 0)
    IsPlayerInsidePoint(8, z140, z140, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Elevator switch returns"""
    ChangeObjState(z138, 81)
    """State 4: Wait for return of elevator switch"""
    CompareObjState(0, z138, 10, 0)
    assert ConditionGroup(0)
    """State 3: Waiting for switch status"""
    CompareObjState(8, z141, 10, 0)
    CompareObjState(8, z142, 30, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m50_35_x145(z136=50350400, z137=2600000):
    """[Reproduction] C root key door
    z136: Key door OBJ instance ID
    z137: Navigation change point ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is the door open?"""
    if CompareObjStateId(z136, 10, 0):
        """State 6: Not open"""
        return 1
    else:
        """State 3: Waiting for the door to open"""
        assert CompareObjStateId(z136, 20, 0)
        """State 4: Navi mesh switching"""
        DeleteNavimeshAttribute(z137, 2)
        """State 7: Finish"""
        return 2
    """State 5: The guests"""
    Label('L0')
    return 0

def event_m50_35_x146(z136=50350400):
    """[Conditions] C root key door
    z136: Key door OBJ instance ID
    """
    """State 0,1: Judgment to examine the door"""
    IsObjSearched(0, z136)
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

def event_m50_35_x147(z136=50350400, z137=2600000):
    """[Execution] C root key_open
    z136: Key door OBJ instance ID
    z137: Navigation change point ID
    """
    """State 0,2: The door opens: 70"""
    ChangeObjState(z136, 70)
    """State 1: Message display"""
    # action:1005:"Used %s", goods:52300000:Eternal Sanctum Key
    DisplayOwnOkMenu(1005, 0, 0, 190, 2, 52300000, 0)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z136, 20, 0)
    assert ConditionGroup(0)
    """State 4: Navi mesh switching"""
    DeleteNavimeshAttribute(z137, 2)
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

def event_m50_35_x149(z137=2600000):
    """[Execution] C root key_guest
    z137: Navigation change point ID
    """
    """State 0,1: Navi mesh switching"""
    DeleteNavimeshAttribute(z137, 2)
    """State 2: End state"""
    return 0

def event_m50_35_x150(z136=50350400):
    """[Conditions] C root key_guest
    z136: Key door OBJ instance ID
    """
    """State 0,1: Waiting for the door to open"""
    CompareObjState(0, z136, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x151(z136=50350400, z137=2600000):
    """[Preset] C root key door
    z136: Key door OBJ instance ID
    z137: Navigation change point ID
    """
    """State 0,1: [Reproduction] C root key_SubState"""
    call = event_m50_35_x145(z136=z136, z137=z137)
    if call.Get() == 1:
        """State 5: [Condition] C root key door_SubState"""
        call = event_m50_35_x146(z136=z136)
        if call.Get() == 0:
            """State 4: [Execute] C root key_open_SubState"""
            assert event_m50_35_x147(z136=z136, z137=z137)
        elif call.Get() == 1:
            """State 3: [Execution] C root key_Do not open_SubState"""
            assert event_m50_35_x148()
            """State 8: Rerun"""
            return 1
    elif call.Get() == 0:
        """State 6: [Conditions] C root key_guest_SubState"""
        assert event_m50_35_x150(z136=z136)
        """State 2: [Execution] C root key_guest_SubState"""
        assert event_m50_35_x149(z137=z137)
    elif call.Get() == 2:
        pass
    """State 7: Finish"""
    return 0

def event_m50_35_x152(z129=8503, z130=8504, z131=8505, z132=8500, z133=8501, z134=8502, z135=8506):
    """[Execution] Queen's enemy summoning
    z129: Generator ① ID
    z130: Generator ② ID
    z131: Generator ③ ID
    z132: Generator ④ ID
    z133: Generator ⑤ ID
    z134: Generator ⑥ ID
    z135: Generator ⑦ ID
    """
    """State 0,1: Summon character death process"""
    EnemyActionRequest(z129, 1)
    EnemyActionRequest(z130, 1)
    EnemyActionRequest(z131, 1)
    EnemyActionRequest(z132, 1)
    EnemyActionRequest(z133, 1)
    EnemyActionRequest(z134, 1)
    EnemyActionRequest(z135, 1)
    EnemyActionRequest(8507, 1)
    EnemyActionRequest(8508, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x153(z120=503500002, z121=900, z122=20, z123=3003000, z124=3003003, z125=2):
    """[Preset] Queen's voice
    z120: Sound ID
    z121: Generator ID
    z122: Hit group ID
    z123: Stop start point ID
    z124: Stop end point ID
    z125: Stop weight
    """
    """State 0,1: [Reproduction] Queen's singing voice_SubState"""
    call = event_m50_35_x154(flag14=535000081, z121=z121, flag15=535020080)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Queen's singing voice_SubState"""
        assert event_m50_35_x156(z122=z122)
        """State 3: [Execution] Queen's singing voice_Play_SubState"""
        assert event_m50_35_x158(z120=z120, z121=z121)
        """State 2: [Reproduction] Queen's singing voice_Sky_SubState"""
        assert event_m50_35_x155()
        """State 6: [Condition] Queen's singing voice_stop judgment_SubState"""
        call = event_m50_35_x157(z126=535000081, z121=z121, z122=z122, z127=5030000, z123=z123, z124=z124,
                                 z125=z125, z128=535020080)
        if call.Get() == 1:
            """State 7: [Execution] Queen singing voice_stop_2_SubState"""
            assert event_m50_35_x159(z121=z121)
        elif call.Get() == 0:
            """State 4: [Execution] Queen singing voice_stop_SubState"""
            assert event_m50_35_x159(z121=z121)
            """State 9: Rerun"""
            return 1
    """State 8: Finish"""
    return 0

def event_m50_35_x154(flag14=535000081, z121=900, flag15=535020080):
    """[Reproduction] Queen's voice
    flag14: Boss destruction flag
    z121: Generator ID
    flag15: Boss activation flag
    """
    """State 0,1: Did you defeat the queen?"""
    if GetEventFlag(flag14) != 0:
        pass
    else:
        """State 3: Is the boss already activated?"""
        if GetEventFlag(flag15) != 0:
            pass
        else:
            """State 4: Not defeated"""
            return 0
    """State 2: Stop generator following sound"""
    StopSoundFollowingGenerator(z121)
    """State 5: Defeated and activated"""
    return 1

def event_m50_35_x155():
    """[Reproduction] Queen's singing voice_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x156(z122=20):
    """[Condition] Queen's singing voice
    z122: Hit group ID
    """
    """State 0,1: Got a starting hit?"""
    IsPlayerOnHitGroup(8, z122, 1)
    assert ConditionGroup(8)
    """State 2: Play singing voice"""
    return 0

def event_m50_35_x157(z126=535000081, z121=900, z122=20, z127=5030000, z123=3003000, z124=3003003, z125=2,
                      z128=535020080):
    """[Condition] Queen's singing voice_stop judgment
    z126: Boss destruction flag
    z121: Generator ID
    z122: Hit group ID
    z127: Boss Battle ID
    z123: Stop start point ID
    z124: Stop end point ID
    z125: Weight to stop
    z128: Boss activation flag
    """
    """State 0,1: Did you destroy the or boss who entered the stop point or started the boss battle?"""
    IsPlayerInsidePoint(8, z123, z124, 1)
    CompareEventFlag(2, z126, 1)
    CompareEventFlag(2, z128, 1)
    IsEventBossBattle(1, z127, 1)
    if ConditionGroup(8):
        """State 3: Stop singing voice: restart"""
        return 0
    elif ConditionGroup(2):
        pass
    elif ConditionGroup(1):
        """State 2: Stop weight"""
        CompareStateTime(0, z125, 3, z125)
        assert ConditionGroup(0)
    """State 4: Stop singing: End"""
    return 1

def event_m50_35_x158(z120=503500002, z121=900):
    """[Execution] Queen's singing voice
    z120: Sound ID
    z121: Generator ID
    """
    """State 0,1: Play generator-following sound"""
    PlaySoundFollowingGenerator(5, z120, z121)
    """State 2: End state"""
    return 0

def event_m50_35_x159(z121=900):
    """[Execution] Queen singing voice_stop
    z121: Generator ID
    """
    """State 0,1: Stop generator following sound"""
    StopSoundFollowingGenerator(z121)
    """State 2: End state"""
    return 0

def event_m50_35_x160():
    """[Reproduction] Awakening Dragon_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x161(z47=50352100, z49=3405010, z50=3405011):
    """[Condition] Awakening Dragon_Points only
    z47: Dragon OBJ instance ID
    z49: Flight start point ID
    z50: Flight end point ID
    """
    """State 0,1: Did you invade the point?"""
    IsPlayerInsidePoint(8, z49, z50, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: Flight event"""
    return 0

def event_m50_35_x162(z114=_, z115=_, z116=_, z117=_):
    """[Preset] OBJ operated with stone switch
    z114: Active OBJ instance ID
    z115: Switch OBJ instance ID
    z116: Navigation change point ID before operation
    z117: Navigation change point ID after operation
    """
    """State 0,1: [Reproduction] OBJ_SubState running on a stone statue switch"""
    assert event_m50_35_x163(z115=z115, z114=z114, z116=z116, z117=z117)
    """State 4: [Condition] OBJ_SubState running on stone statue switch"""
    call = event_m50_35_x164(z108=z115, z107=z114)
    if call.Get() == 0:
        """State 2: [Execution] OBJ_SubState running on the stone switch"""
        assert event_m50_35_x165(z114=z114, z118=70, z119=30, z115=z115, z117=z117, z116=z116)
    elif call.Get() == 1:
        """State 5: [Execution] OBJ_2_SubState running on stone switch"""
        assert event_m50_35_x165(z114=z114, z118=80, z119=10, z115=z115, z117=z116, z116=z117)
    elif call.Get() == 3:
        """State 3: [Execution] OBJ_Switch_Return_SubState running on the stone statue switch"""
        assert event_m50_35_x166(z108=z115)
    elif call.Get() == 2:
        """State 6: [Execution] OBJ_Switch that works with the stone statue switch_2_SubState"""
        assert event_m50_35_x166(z108=z115)
    """State 7: End state"""
    return 0

def event_m50_35_x163(z115=_, z114=_, z116=_, z117=_):
    """[Reproduction] OBJ operated with stone statue switch
    z115: Switch OBJ instance ID
    z114: Active OBJ instance ID
    z116: Navigation change point ID before operation
    z117: Navigation change point ID after operation
    """
    """State 0,3: OBJ status judgment"""
    if CompareObjStateId(z114, 70, 0):
        """State 7,10: Change navigation_3"""
        AddNavimeshAttribute(z116, 2)
        AddNavimeshAttribute(z117, 2)
        """State 11: OBJ operation waiting"""
        assert CompareObjStateId(z114, 30, 0)
        """State 14: Change navigation_5"""
        DeleteNavimeshAttribute(z117, 2)
        AddNavimeshAttribute(z116, 2)
    elif CompareObjStateId(z114, 80, 0):
        """State 6,12: Change navigation_4"""
        AddNavimeshAttribute(z116, 2)
        AddNavimeshAttribute(z117, 2)
        """State 13: OBJ waiting_2"""
        assert CompareObjStateId(z114, 10, 0)
        """State 15: Change navigation_6"""
        DeleteNavimeshAttribute(z116, 2)
        AddNavimeshAttribute(z117, 2)
    elif CompareObjStateId(z114, 10, 0):
        """State 4,8: Change navigation"""
        DeleteNavimeshAttribute(z116, 2)
        AddNavimeshAttribute(z117, 2)
    elif CompareObjStateId(z114, 30, 0):
        """State 5,9: Change navigation_2"""
        DeleteNavimeshAttribute(z117, 2)
        AddNavimeshAttribute(z116, 2)
    """State 16: Is the switch in the initial state?"""
    if CompareObjStateId(z115, 10, 0):
        pass
    else:
        """State 17: Is the switch descending?"""
        if CompareObjStateId(z115, 70, 0):
            """State 18: Wait for switch to fall"""
            assert CompareObjStateId(z115, 30, 0)
        else:
            pass
        """State 1: Return only the switch"""
        ChangeObjState(z115, 80)
        """State 2: Wait for switch to finish"""
        assert CompareObjStateId(z115, 10, 0)
    """State 19: End state"""
    return 0

def event_m50_35_x164(z108=_, z107=_):
    """[Conditions] OBJ operated with stone statue switch
    z108: Switch OBJ instance ID
    z107: Active OBJ instance ID
    """
    """State 0,2: OBJ status judgment"""
    CompareObjState(0, z107, 10, 0)
    CompareObjState(1, z107, 30, 0)
    CompareObjState(2, z107, 70, 0)
    CompareObjState(3, z107, 80, 0)
    if ConditionGroup(2):
        """State 6,8: Wait for OBJ operation to end"""
        CompareObjState(0, z107, 30, 0)
        assert ConditionGroup(0)
        """State 12: Switch back after return"""
        return 2
    elif ConditionGroup(3):
        """State 5,9: Waiting for OBJ to end operation_2"""
        CompareObjState(0, z107, 10, 0)
        assert ConditionGroup(0)
        """State 13: Switch back after operation"""
        return 3
    elif ConditionGroup(0):
        """State 3,1: Switch judgment"""
        IsObjDamaged(0, z108, -1, -4, 0)
        assert ConditionGroup(0)
        """State 10: Run OBJ"""
        return 0
    elif ConditionGroup(1):
        """State 4,7: Switch judgment_2"""
        IsObjDamaged(0, z108, -1, -4, 0)
        assert ConditionGroup(0)
        """State 11: Get OBJ back"""
        return 1

def event_m50_35_x165(z114=_, z118=_, z119=_, z115=_, z117=_, z116=_):
    """[Execution] OBJ running on a stone statue switch
    z114: Active OBJ instance ID
    z118: OBJ state ID during operation
    z119: End of operation OBJ state ID
    z115: Switch OBJ instance ID
    z117: Passable navigation change point ID
    z116: Non-passable navigation change point ID
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z115, 70)
    """State 5: weight"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 7: Change navigation"""
    AddNavimeshAttribute(z117, 2)
    AddNavimeshAttribute(z116, 2)
    """State 1: OBJ is in operation"""
    ChangeObjState(z114, z118)
    """State 3: Wait for OBJ operation to end"""
    CompareObjState(0, z114, z119, 0)
    assert ConditionGroup(0)
    """State 8: Change navigation_2"""
    AddNavimeshAttribute(z116, 2)
    DeleteNavimeshAttribute(z117, 2)
    """State 2: Switch back"""
    ChangeObjState(z115, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z115, 10, 0)
    assert ConditionGroup(0)
    """State 9: End state"""
    return 0

def event_m50_35_x166(z108=_):
    """[Execution] OBJ_ switch operating with stone statue switch
    z108: Switch OBJ instance ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z108, 80)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z108, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x167(z108=_, z107=_, z109=_):
    """[Reproduction] One version of OBJ_Navi running on a stone statue switch
    z108: Switch OBJ instance ID
    z107: Active OBJ instance ID
    z109: Navigation change point ID
    """
    """State 0,3: OBJ status judgment"""
    if CompareObjStateId(z107, 70, 0):
        """State 7,10: Change navigation_3"""
        AddNavimeshAttribute(z109, 2)
        """State 11: OBJ operation waiting"""
        assert CompareObjStateId(z107, 30, 0)
        """State 14: Change navigation_5"""
        DeleteNavimeshAttribute(z109, 2)
    elif CompareObjStateId(z107, 80, 0):
        """State 6,12: Change navigation_4"""
        AddNavimeshAttribute(z109, 2)
        """State 13: OBJ waiting_2"""
        assert CompareObjStateId(z107, 10, 0)
        """State 15: Change navigation_6"""
        AddNavimeshAttribute(z109, 2)
    elif CompareObjStateId(z107, 10, 0):
        """State 4,8: Change navigation"""
        AddNavimeshAttribute(z109, 2)
    elif CompareObjStateId(z107, 30, 0):
        """State 5,9: Change navigation_2"""
        DeleteNavimeshAttribute(z109, 2)
    """State 16: Is the switch in the initial state?"""
    if CompareObjStateId(z108, 10, 0):
        pass
    else:
        """State 17: Is the switch descending?"""
        if CompareObjStateId(z108, 70, 0):
            """State 18: Wait for switch to fall"""
            assert CompareObjStateId(z108, 30, 0)
        else:
            pass
        """State 1: Return only the switch"""
        ChangeObjState(z108, 80)
        """State 2: Wait for switch to finish"""
        assert CompareObjStateId(z108, 10, 0)
    """State 19: End state"""
    return 0

def event_m50_35_x168(z107=_, z110=_, z111=_, z108=_, z109=_, z112=_, z113=_):
    """[Execution] One version of OBJ_Navi running on a stone statue switch
    z107: Active OBJ instance ID
    z110: OBJ state ID during operation
    z111: End of operation OBJ state ID
    z108: Switch OBJ instance ID
    z109: Navigation change point ID
    z112: Navigation additional attributes
    z113: Navi delete attribute
    """
    """State 0,6: Switch is up"""
    ChangeObjState(z108, 70)
    """State 5: weight"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 7: Change navigation"""
    AddNavimeshAttribute(z109, 2)
    """State 1: OBJ is in operation"""
    ChangeObjState(z107, z110)
    """State 3: Wait for OBJ operation to end"""
    CompareObjState(0, z107, z111, 0)
    assert ConditionGroup(0)
    """State 8: Change navigation_2"""
    AddNavimeshAttribute(z109, z112)
    DeleteNavimeshAttribute(z109, z113)
    """State 2: Switch back"""
    ChangeObjState(z108, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z108, 10, 0)
    assert ConditionGroup(0)
    """State 9: End state"""
    return 0

def event_m50_35_x169(z107=_, z108=_, z109=_):
    """[Preset] One version of OBJ_Navi running on a stone statue switch
    z107: Active OBJ instance ID
    z108: Switch OBJ instance ID
    z109: Navigation change point ID
    """
    """State 0,4: [Reproduction] OBJ_Navi 1 version _SubState running on stone statue switch"""
    assert event_m50_35_x167(z108=z108, z107=z107, z109=z109)
    """State 2: [Condition] OBJ_SubState running on stone statue switch"""
    call = event_m50_35_x164(z108=z108, z107=z107)
    if call.Get() == 3:
        """State 1: [Execution] OBJ_Switch_Return_SubState running on the stone statue switch"""
        assert event_m50_35_x166(z108=z108)
    elif call.Get() == 2:
        """State 3: [Execution] OBJ_Switch that works with the stone statue switch_2_SubState"""
        assert event_m50_35_x166(z108=z108)
    elif call.Get() == 0:
        """State 5: [Execution] OBJ_Navigation 1 version_SubState running on the stone statue switch"""
        assert event_m50_35_x168(z107=z107, z110=70, z111=30, z108=z108, z109=z109, z112=0, z113=2)
    elif call.Get() == 1:
        """State 6: [Execution] One version of OBJ_Navi running on stone switch_2_SubState"""
        assert event_m50_35_x168(z107=z107, z110=80, z111=10, z108=z108, z109=z109, z112=2, z113=0)
    """State 7: End state"""
    return 0

def event_m50_35_x170(z105=50353409, z104=50351215, z106=32):
    """[Reproduction] Door rotated by switch _135 degree version
    z105: Switch OBJ instance ID
    z104: Revolving door OBJ instance ID
    z106: Initial state OBJ state ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z104, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z104, z106)
        assert CompareObjStateId(z104, z106, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z105, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z105, 10, 0)
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 10, 0):
        Goto('L0')
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 32, 0):
        Goto('L0')
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 34, 0):
        Goto('L0')
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 40, 0):
        Goto('L0')
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 41, 0):
        Goto('L0')
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 42, 0):
        Goto('L0')
    elif CompareObjStateId(z105, 30, 0) and CompareObjStateId(z104, 43, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x171(z105=50353409, z104=50351215):
    """[Condition] Door rotated by switch _135 degree version
    z105: Switch OBJ instance ID
    z104: Revolving door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z104, 10, 0)
    CompareObjState(1, z104, 41, 0)
    CompareObjState(2, z104, 30, 0)
    CompareObjState(3, z104, 40, 0)
    CompareObjState(4, z104, 32, 0)
    CompareObjState(5, z104, 43, 0)
    CompareObjState(6, z104, 34, 0)
    CompareObjState(7, z104, 42, 0)
    CompareObjState(8, z104, 80, 0)
    CompareObjState(9, z104, 83, 0)
    CompareObjState(10, z104, 86, 0)
    CompareObjState(11, z104, 81, 0)
    CompareObjState(12, z104, 84, 0)
    CompareObjState(13, z104, 87, 0)
    CompareObjState(14, z104, 82, 0)
    CompareObjState(15, z104, 85, 0)
    if ConditionGroup(8):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z104, 40, 0)
        assert ConditionGroup(0)
        """State 38: Upper right: Switch back"""
        return 4
    elif ConditionGroup(9):
        """State 22,30: Waiting for door to finish operation_5"""
        CompareObjState(0, z104, 32, 0)
        assert ConditionGroup(0)
        """State 45: Right: Switch back"""
        return 11
    elif ConditionGroup(10):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z104, 43, 0)
        assert ConditionGroup(0)
        """State 39: Lower right: Switch back"""
        return 5
    elif ConditionGroup(11):
        """State 23,31: Waiting for the door to finish operation_6"""
        CompareObjState(0, z104, 34, 0)
        assert ConditionGroup(0)
        """State 46: Bottom: Switch back"""
        return 12
    elif ConditionGroup(12):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z104, 42, 0)
        assert ConditionGroup(0)
        """State 40: Lower left: Switch back"""
        return 6
    elif ConditionGroup(13):
        """State 24,32: Waiting for the door to finish operation_7"""
        CompareObjState(0, z104, 10, 0)
        assert ConditionGroup(0)
        """State 47: Left: Switch back"""
        return 13
    elif ConditionGroup(14):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z104, 41, 0)
        assert ConditionGroup(0)
        """State 41: Upper left: Switch back"""
        return 7
    elif ConditionGroup(15):
        """State 25,33: Waiting for the door to finish operation_8"""
        CompareObjState(0, z104, 30, 0)
        assert ConditionGroup(0)
        """State 48: Top: Switch back"""
        return 14
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 34: Door from left to top right"""
        return 0
    elif ConditionGroup(1):
        """State 18,26: Switch judgment_5"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 42: Door from upper left to right"""
        return 8
    elif ConditionGroup(2):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 35: Door from top to bottom right"""
        return 1
    elif ConditionGroup(3):
        """State 19,27: Switch judgment_6"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 43: Door from top right to bottom"""
        return 9
    elif ConditionGroup(4):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 36: Door from right to bottom left"""
        return 2
    elif ConditionGroup(5):
        """State 20,28: Switch judgment_7"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 44: Door from lower right to left"""
        return 10
    elif ConditionGroup(6):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 37: Door from bottom to top left"""
        return 3
    elif ConditionGroup(7):
        """State 21,29: Switch judgment_8"""
        IsObjDamaged(0, z105, -1, -4, 0)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 49: Door from bottom left to top"""
        return 15

def event_m50_35_x172(z104=50351215, z105=50353409, z106=32):
    """[Preset] Rotating door with switch _135 degree version
    z104: Revolving door OBJ instance ID
    z105: Switch OBJ instance ID
    z106: Initial state OBJ state ID
    """
    """State 0,1: [Reproduction] Door rotating with switch _135 degree version_SubState"""
    assert event_m50_35_x170(z105=z105, z104=z104, z106=z106)
    """State 4: [Condition] Door rotated by switch_135 degree version_SubState"""
    call = event_m50_35_x171(z105=z105, z104=z104)
    if call.Get() == 0:
        """State 2: [Execution] Door rotated by switch_SubState"""
        assert event_m50_35_x49(z104=z104, z210=80, z211=40, z105=z105, z212=80, z213=10)
    elif call.Get() == 8:
        """State 5: [Execution] Door rotated by switch_2_SubState"""
        assert event_m50_35_x49(z104=z104, z210=83, z211=32, z105=z105, z212=80, z213=10)
    elif call.Get() == 1:
        """State 6: [Execution] Door rotated by switch_3_SubState"""
        assert event_m50_35_x49(z104=z104, z210=86, z211=43, z105=z105, z212=80, z213=10)
    elif call.Get() == 9:
        """State 7: [Execution] Door rotated by switch_4_SubState"""
        assert event_m50_35_x49(z104=z104, z210=81, z211=34, z105=z105, z212=80, z213=10)
    elif call.Get() == 2:
        """State 8: [Execution] Door rotated by switch_5_SubState"""
        assert event_m50_35_x49(z104=z104, z210=84, z211=42, z105=z105, z212=80, z213=10)
    elif call.Get() == 10:
        """State 9: [Execution] Door rotated by switch_6_SubState"""
        assert event_m50_35_x49(z104=z104, z210=87, z211=10, z105=z105, z212=80, z213=10)
    elif call.Get() == 3:
        """State 10: [Execution] Door rotated by switch_7_SubState"""
        assert event_m50_35_x49(z104=z104, z210=82, z211=41, z105=z105, z212=80, z213=10)
    elif call.Get() == 15:
        """State 11: [Execution] Door rotated by switch_8_SubState"""
        assert event_m50_35_x49(z104=z104, z210=85, z211=30, z105=z105, z212=80, z213=10)
    elif call.Get() == 13:
        """State 3: [Execution] Door revolving with switch_Return switch_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 7:
        """State 12: [Execution] Door revolving with switch_Return switch_2_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 14:
        """State 13: [Execution] Door rotated by switch_Switch return_3_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 4:
        """State 14: [Execution] Door rotated by switch_Switch return_4_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 11:
        """State 15: [Execution] Door rotated by switch_Switch return_5_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 5:
        """State 16: [Execution] Door rotated by switch_Switch return_6_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 12:
        """State 17: [Execution] Door revolving with switch_Return switch_7_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    elif call.Get() == 6:
        """State 18: [Execution] Door revolving with switch_Switch return_8_SubState"""
        assert event_m50_35_x51(z105=z105, z208=80, z209=10)
    """State 19: End state"""
    return 0

def event_m50_35_x173(z101=_, z102=_):
    """[Reproduction] Navigation changes between buildings
    z101: Navigation change point_on
    z102: Navigation change point under
    """
    """State 0,1: Navi mesh switching: Not allowed"""
    AddNavimeshAttribute(z101, 2)
    AddNavimeshAttribute(z102, 2)
    """State 2: End state"""
    return 0

def event_m50_35_x174(z99=_, z100=_):
    """[Condition] Change navigation between buildings
    z99: Building OBJ① Instance ID
    z100: Building OBJ② Instance ID
    """
    """State 0,1: Judgment of building condition"""
    CompareObjState(8, z99, 10, 0)
    CompareObjState(8, z100, 10, 0)
    CompareObjState(9, z99, 30, 0)
    CompareObjState(9, z100, 30, 0)
    if ConditionGroup(8):
        """State 3: Both buildings are below"""
        return 1
    elif ConditionGroup(9):
        """State 2: Both buildings are on"""
        return 0

def event_m50_35_x175(z99=_, z100=_, z102=_, z101=_, z103=_):
    """[Execution] Navigation changes between buildings
    z99: Building OBJ① Instance ID
    z100: Building OBJ② Instance ID
    z102: Passable point
    z101: Impassable points
    z103: Building stop OBJ state ID
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z102, 2)
    AddNavimeshAttribute(z101, 2)
    """State 2: Building operation standby"""
    CompareObjState(0, z99, z103, 1)
    CompareObjState(0, z100, z103, 1)
    assert ConditionGroup(0)
    """State 3: Finish"""
    return 0

def event_m50_35_x176(z99=_, z100=_, z101=_, z102=_):
    """[Preset] Change navigation between buildings
    z99: Building OBJ① Instance ID
    z100: Building OBJ② Instance ID
    z101: Navigation change point_on
    z102: Navigation change point under
    """
    """State 0,1: [Reproduction] Navigation change between buildings_SubState"""
    assert event_m50_35_x173(z101=z101, z102=z102)
    """State 3: [Condition] Change navigation between buildings_SubState"""
    call = event_m50_35_x174(z99=z99, z100=z100)
    if call.Get() == 1:
        """State 2: [Execution] Change navigation between buildings_SubState"""
        assert event_m50_35_x175(z99=z99, z100=z100, z102=z102, z101=z101, z103=10)
    elif call.Get() == 0:
        """State 4: [Execution] Navigation change between buildings_2_SubState"""
        assert event_m50_35_x175(z99=z99, z100=z100, z102=z101, z101=z102, z103=30)
    """State 5: Rerun"""
    return 0

def event_m50_35_x177(z6=900):
    """[Condition] Queen's enemy summons
    z6: Boss generator ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Queen's Summoning Action Judgment"""
        CompareChrEzStateValue(8, z6, 6, 0, 1)
        CompareChrEzStateValue(8, z6, 7, 1, 0)
        IsChrDead(0, z6)
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
                    assert event_m50_35_x178(z96=0, z97=69, z98=99)
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
                    IsChrDead(3, z6)
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
                    assert event_m50_35_x178(z96=0, z97=50, z98=99)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 22: Random number generation to 3 lottery _ Everyone died _3_SubState"""
                    assert event_m50_35_x178(z96=0, z97=30, z98=99)
                    Goto('L0')
            elif ConditionGroup(8):
                """State 10: Multi-person determination_2"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 17: 3 random drawing from random number generation"""
                    assert event_m50_35_x178(z96=0, z97=69, z98=99)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 23: Random number generation to 3 lottery _ Survival of all _2 _ SubState"""
                    assert event_m50_35_x178(z96=0, z97=50, z98=99)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 24: Random number generation to 3 lottery _ survival_3_SubState"""
                    assert event_m50_35_x178(z96=0, z97=30, z98=99)
                    Goto('L0')
            elif ConditionGroup(14):
                """State 11: Multi-person determination_3"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 15: Random number generation from two lottery _ pig or skeleton _ SubState"""
                    assert event_m50_35_x179(z94=70, z95=0, flag12=535020001, flag13=535020002)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 25: Random number generator to lottery_pig or skeleton_2_SubState"""
                    assert event_m50_35_x179(z94=50, z95=0, flag12=535020001, flag13=535020002)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 26: Random number generation from 2 lottery_pig or skeleton_3_SubState"""
                    assert event_m50_35_x179(z94=30, z95=0, flag12=535020001, flag13=535020002)
                    Goto('L0')
            elif ConditionGroup(12):
                """State 12: Multi-person determination_4"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 18: Random number generation to draw 2 bodies_Skeleton or Queen Knight B_SubState"""
                    assert event_m50_35_x179(z94=99, z95=69, flag12=535020002, flag13=535020003)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 27: Random number generation from two lotteries_Skeleton or Queen Knight B_2_SubState"""
                    assert event_m50_35_x179(z94=99, z95=49, flag12=535020002, flag13=535020003)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 28: Random number generation from two bodies _ Skeleton or Queen Knight B_3_SubState"""
                    assert event_m50_35_x179(z94=99, z95=29, flag12=535020002, flag13=535020003)
                    Goto('L0')
            elif ConditionGroup(13):
                """State 13: Multi-person determination_5"""
                CompareMultiplayerPlayerCount(0, 1, 1, 0, 0)
                CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
                CompareMultiplayerPlayerCount(2, 1, 1, 2, 3)
                if ConditionGroup(0):
                    """State 19: Random number generation from two lottery _ Pig or Queen Knight B_SubState"""
                    assert event_m50_35_x179(z94=29, z95=0, flag12=535020001, flag13=535020003)
                    Goto('L0')
                elif ConditionGroup(1):
                    """State 29: Random number generation to draw 2 bodies _ Pig or Queen Knight B_2_SubState"""
                    assert event_m50_35_x179(z94=49, z95=0, flag12=535020001, flag13=535020003)
                    Goto('L0')
                elif ConditionGroup(2):
                    """State 30: Random number generation from two lottery _ Pig or Queen Knight B_3_SubState"""
                    assert event_m50_35_x179(z94=69, z95=0, flag12=535020001, flag13=535020003)
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

def event_m50_35_x178(z96=0, z97=_, z98=99):
    """Three lottery from random number generation
    z96: Pig random_comparison value
    z97: Bone random number_comparison value
    z98: Knight random number_comparison value
    """
    """State 0,2: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 1: Character lottery"""
    CompareEventRandValue(0, 0, z96, 5)
    CompareEventRandValue(1, 0, z97, 5)
    CompareEventRandValue(2, 0, z98, 5)
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

def event_m50_35_x179(z94=_, z95=_, flag12=_, flag13=_):
    """Two lottery from random number generation
    z94: Random_max
    z95: Random number_1 comparison value
    flag12: Winning A flag
    flag13: Winning B flag
    """
    """State 0,2: Random number generation"""
    GenerateRandomNumber(0, 0, z94)
    """State 1: Character lottery"""
    CompareEventRandValue(0, 0, z95, 5)
    CompareEventRandValue(1, 0, z94, 5)
    if ConditionGroup(0):
        """State 3: Chara A winning"""
        SetEventFlag(flag12, 1)
        assert GetEventFlag(flag12) != 0
    elif ConditionGroup(1):
        """State 4: Chara B winning"""
        SetEventFlag(flag13, 1)
        assert GetEventFlag(flag13) != 0
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

def event_m50_35_x181(z6=900, z7=50001000, z8=50001039):
    """[Preset] Queen's enemy summons
    z6: Boss generator ID
    z7: Start point ID
    z8: End point ID
    """
    """State 0,1: [Reproduction] Queen's enemy summon _SubState"""
    assert event_m50_35_x103()
    """State 3: [Condition] Queen's Enemy Summoning_No Duplicate Version_SubState"""
    call = event_m50_35_x177(z6=z6)
    if call.Get() == 0:
        """State 5: [Execution] Queen's enemy summon _3 body version_pig_SubState"""
        assert event_m50_35_x228(z6=z6, z41=8503, z42=8504, z43=8505, z7=z7, z8=z8, z44=70)
    elif call.Get() == 2:
        """State 6: [Execution] Queen's enemy summon _3 body version_Skeleton_SubState"""
        assert event_m50_35_x228(z6=z6, z41=8500, z42=8501, z43=8502, z7=z7, z8=z8, z44=71)
    elif call.Get() == 4:
        """State 7: [Execution] Queen's enemy summon _4 body version_Skeleton_SubState"""
        assert event_m50_35_x247(z6=z6, z14=8500, z15=8501, z16=8502, z7=z7, z8=z8, z17=71, z18=8507)
    elif call.Get() == 5:
        """State 8: [Execution] Queen's enemy summon _5 body version_Skeleton_SubState"""
        assert event_m50_35_x248(z6=z6, z9=8500, z10=8501, z11=8502, z7=z7, z8=z8, z12=8507, z13=8508)
    elif call.Get() == 3:
        """State 4: [Execution] Queen's Enemy Summon _1 body_Queen's Knight B_SubState"""
        assert event_m50_35_x227(z6=z6, z45=8506, z7=z7, z8=z8, z46=72)
    elif call.Get() == 1:
        """State 2: [Execution] Queen's Enemy Summoning_Enemy Death_SubState"""
        assert event_m50_35_x152(z129=8503, z130=8504, z131=8505, z132=8500, z133=8501, z134=8502, z135=8506)
        """State 9: Defeat Boss: Finish"""
        return 0
    """State 10: Rerun"""
    return 1

def event_m50_35_x182(z84=50351213, z86=32, z85=50353410, z87=50353412):
    """[Reproduction] Door rotated by switch_Two switches version
    z84: Revolving door OBJ instance ID
    z86: Initial state OBJ state ID
    z85: Switch ① OBJ instance ID
    z87: Switch ②OBJ instance ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z84, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z84, z86)
        assert CompareObjStateId(z84, z86, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z85, 30, 0) and CompareObjStateId(z84, 30, 0) and CompareObjStateId(z87, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z85, 80)
        ChangeObjState(z87, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z85, 10, 0) and CompareObjStateId(z87, 10, 0)
    elif CompareObjStateId(z85, 30, 0) and CompareObjStateId(z84, 10, 0) and CompareObjStateId(z87, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z85, 30, 0) and CompareObjStateId(z84, 32, 0) and CompareObjStateId(z87, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z85, 30, 0) and CompareObjStateId(z84, 34, 0) and CompareObjStateId(z87, 30, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x183(z85=50353410, z84=50351213, z87=50353412):
    """[Condition] Door rotated by switch_Two-switch version
    z85: Switch ① OBJ instance ID
    z84: Revolving door OBJ instance ID
    z87: Switch ②OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z84, 10, 0)
    CompareObjState(1, z84, 30, 0)
    CompareObjState(2, z84, 32, 0)
    CompareObjState(3, z84, 34, 0)
    CompareObjState(4, z84, 70, 0)
    CompareObjState(5, z84, 72, 0)
    CompareObjState(6, z84, 74, 0)
    CompareObjState(7, z84, 76, 0)
    if ConditionGroup(4):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z84, 30, 0)
        assert ConditionGroup(0)
        """State 22: Top: Switch back"""
        return 4
    elif ConditionGroup(5):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z84, 32, 0)
        assert ConditionGroup(0)
        """State 23: Right: Switch back"""
        return 5
    elif ConditionGroup(6):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z84, 34, 0)
        assert ConditionGroup(0)
        """State 24: Bottom: Switch back"""
        return 6
    elif ConditionGroup(7):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z84, 10, 0)
        assert ConditionGroup(0)
        """State 25: Left: Switch back"""
        return 7
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z85, -1, -4, 0)
        CompareObjState(0, z85, 30, 0)
        IsObjDamaged(0, z87, -1, -4, 0)
        CompareObjState(0, z87, 30, 0)
        assert ConditionGroup(0)
        """State 18: Door up from left"""
        return 0
    elif ConditionGroup(1):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z85, -1, -4, 0)
        CompareObjState(0, z85, 30, 0)
        IsObjDamaged(0, z87, -1, -4, 0)
        CompareObjState(0, z87, 30, 0)
        assert ConditionGroup(0)
        """State 19: Door from top to right"""
        return 1
    elif ConditionGroup(2):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z85, -1, -4, 0)
        CompareObjState(0, z85, 30, 0)
        IsObjDamaged(0, z87, -1, -4, 0)
        CompareObjState(0, z87, 30, 0)
        assert ConditionGroup(0)
        """State 20: Door from right to bottom"""
        return 2
    elif ConditionGroup(3):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z85, -1, -4, 0)
        CompareObjState(0, z85, 30, 0)
        IsObjDamaged(0, z87, -1, -4, 0)
        CompareObjState(0, z87, 30, 0)
        assert ConditionGroup(0)
        """State 21: Door from bottom to left"""
        return 3

def event_m50_35_x184(z80=_, z90=_, z91=_, z81=_, z92=80, z93=10, z83=_):
    """[Execution] Door rotated by switch_Two switches version
    z80: Revolving door OBJ instance ID
    z90: Pillar operation OBJ state ID
    z91: OBJ state ID for which the column has ended
    z81: Switch ① OBJ instance ID
    z92: Switch operation OBJ state ID
    z93: Switch operation end OBJ state ID
    z83: Switch ②OBJ instance ID
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z81, 70)
    ChangeObjState(z83, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z81, 30, 0)
    CompareObjState(0, z83, 30, 0)
    assert ConditionGroup(0)
    """State 1: The door rotates"""
    ChangeObjState(z80, z90)
    """State 3: Waiting for the column to finish operation"""
    CompareObjState(0, z80, z91, 0)
    assert ConditionGroup(0)
    """State 2: Switch back"""
    ChangeObjState(z81, z92)
    ChangeObjState(z83, z92)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z81, z93, 0)
    CompareObjState(0, z83, z93, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_35_x185(z84=50351213, z85=50353410, z86=32, z87=50353412):
    """[Preset] Rotating door with switch_Two-switch version
    z84: Revolving door OBJ instance ID
    z85: Switch ① OBJ instance ID
    z86: Initial state OBJ state ID
    z87: Switch ②OBJ instance ID
    """
    """State 0,1: [Reproduction] Door rotating with switch_Two switches_SubState"""
    assert event_m50_35_x182(z84=z84, z86=z86, z85=z85, z87=z87)
    """State 3: [Condition] Door rotated by switch_Two switches_SubState"""
    call = event_m50_35_x183(z85=z85, z84=z84, z87=z87)
    if call.Get() == 0:
        """State 2: [Execution] Door that rotates with switch_Two switches_SubState"""
        assert event_m50_35_x184(z80=z84, z90=70, z91=30, z81=z85, z92=80, z93=10, z83=z87)
    elif call.Get() == 1:
        """State 5: [Execution] Door rotated by switch_Two switch version_2_SubState"""
        assert event_m50_35_x184(z80=z84, z90=72, z91=32, z81=z85, z92=80, z93=10, z83=z87)
    elif call.Get() == 2:
        """State 6: [Execution] Door rotated by switch_Two switches_3_SubState"""
        assert event_m50_35_x184(z80=z84, z90=74, z91=34, z81=z85, z92=80, z93=10, z83=z87)
    elif call.Get() == 3:
        """State 7: [Execution] Door rotated by switch_Two switches_4_SubState"""
        assert event_m50_35_x184(z80=z84, z90=76, z91=10, z81=z85, z92=80, z93=10, z83=z87)
    elif call.Get() == 4:
        """State 4: [Execution] Door rotated by switch_Return switch_Two switches_SubState"""
        assert event_m50_35_x186(z81=z85, z88=80, z89=10, z83=z87)
    elif call.Get() == 5:
        """State 8: [Execution] Door rotated by switch_Return switch_Two switch version_2_SubState"""
        assert event_m50_35_x186(z81=z85, z88=80, z89=10, z83=z87)
    elif call.Get() == 6:
        """State 9: [Execution] Door rotated by switch_Switch return_Two switch version_3_SubState"""
        assert event_m50_35_x186(z81=z85, z88=80, z89=10, z83=z87)
    elif call.Get() == 7:
        """State 10: [Execution] Door that rotates with switch_Return switch_Two switches_4_SubState"""
        assert event_m50_35_x186(z81=z85, z88=80, z89=10, z83=z87)
    """State 11: End state"""
    return 0

def event_m50_35_x186(z81=_, z88=80, z89=10, z83=_):
    """[Execution] Door rotated by switch_Switch return_Two switch version
    z81: Switch ① OBJ instance ID
    z88: Switch operation OBJ state ID
    z89: Switch operation end OBJ state ID
    z83: Switch ②OBJ instance ID
    """
    """State 0,1: Switch back"""
    ChangeObjState(z81, z88)
    ChangeObjState(z83, z88)
    """State 2: Wait for switch to finish"""
    CompareObjState(0, z81, z89, 0)
    CompareObjState(0, z83, z89, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x187(z81=50353409, z80=50351215, z82=32, z83=50353411):
    """[Reproduction] Door rotating with switch _135 degree version_Two switch version
    z81: Switch ① OBJ instance ID
    z80: Revolving door OBJ instance ID
    z82: Initial state OBJ state ID
    z83: Switch ②OBJ instance ID
    """
    """State 0,4: Is it an initialization state?"""
    if CompareObjStateId(z80, 100, 0):
        """State 5: Transition to initial state"""
        ChangeObjState(z80, z82)
        assert CompareObjStateId(z80, z82, 0)
    else:
        pass
    """State 1: The door is stationary, but the switch remains down?"""
    if CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 30, 0) and CompareObjStateId(z83, 30, 0):
        """State 2: Return only the switch"""
        Label('L0')
        ChangeObjState(z81, 80)
        ChangeObjState(z83, 80)
        """State 3: Wait for switch to finish"""
        assert CompareObjStateId(z81, 10, 0) and CompareObjStateId(z83, 10, 0)
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 10, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 32, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 34, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 40, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 41, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 42, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 30, 0) and CompareObjStateId(z80, 43, 0) and CompareObjStateId(z83, 30, 0):
        Goto('L0')
    else:
        pass
    """State 6: End state"""
    return 0

def event_m50_35_x188(z81=50353409, z80=50351215, z83=50353411):
    """[Condition] Door rotated by switch_135 degree version_Two switch version
    z81: Switch ① OBJ instance ID
    z80: Revolving door OBJ instance ID
    z83: Switch ②OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z80, 10, 0)
    CompareObjState(1, z80, 41, 0)
    CompareObjState(2, z80, 30, 0)
    CompareObjState(3, z80, 40, 0)
    CompareObjState(4, z80, 32, 0)
    CompareObjState(5, z80, 43, 0)
    CompareObjState(6, z80, 34, 0)
    CompareObjState(7, z80, 42, 0)
    CompareObjState(8, z80, 80, 0)
    CompareObjState(9, z80, 83, 0)
    CompareObjState(10, z80, 86, 0)
    CompareObjState(11, z80, 81, 0)
    CompareObjState(12, z80, 84, 0)
    CompareObjState(13, z80, 87, 0)
    CompareObjState(14, z80, 82, 0)
    CompareObjState(15, z80, 85, 0)
    if ConditionGroup(8):
        """State 3,11: Waiting for door to finish operation"""
        CompareObjState(0, z80, 40, 0)
        assert ConditionGroup(0)
        """State 38: Upper right: Switch back"""
        return 4
    elif ConditionGroup(9):
        """State 22,30: Waiting for door to finish operation_5"""
        CompareObjState(0, z80, 32, 0)
        assert ConditionGroup(0)
        """State 45: Right: Switch back"""
        return 11
    elif ConditionGroup(10):
        """State 5,15: Waiting for the door to finish operation_2"""
        CompareObjState(0, z80, 43, 0)
        assert ConditionGroup(0)
        """State 39: Lower right: Switch back"""
        return 5
    elif ConditionGroup(11):
        """State 23,31: Waiting for the door to finish operation_6"""
        CompareObjState(0, z80, 34, 0)
        assert ConditionGroup(0)
        """State 46: Bottom: Switch back"""
        return 12
    elif ConditionGroup(12):
        """State 6,16: Waiting for the door to finish operation_3"""
        CompareObjState(0, z80, 42, 0)
        assert ConditionGroup(0)
        """State 40: Lower left: Switch back"""
        return 6
    elif ConditionGroup(13):
        """State 24,32: Waiting for the door to finish operation_7"""
        CompareObjState(0, z80, 10, 0)
        assert ConditionGroup(0)
        """State 47: Left: Switch back"""
        return 13
    elif ConditionGroup(14):
        """State 9,17: Waiting for the door to finish operation_4"""
        CompareObjState(0, z80, 41, 0)
        assert ConditionGroup(0)
        """State 41: Upper left: Switch back"""
        return 7
    elif ConditionGroup(15):
        """State 25,33: Waiting for the door to finish operation_8"""
        CompareObjState(0, z80, 30, 0)
        assert ConditionGroup(0)
        """State 48: Top: Switch back"""
        return 14
    elif ConditionGroup(0):
        """State 2,10: Switch judgment"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 34: Door from left to top right"""
        return 0
    elif ConditionGroup(1):
        """State 18,26: Switch judgment_5"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 42: Door from upper left to right"""
        return 8
    elif ConditionGroup(2):
        """State 4,12: Switch judgment_2"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 35: Door from top to bottom right"""
        return 1
    elif ConditionGroup(3):
        """State 19,27: Switch judgment_6"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 43: Door from top right to bottom"""
        return 9
    elif ConditionGroup(4):
        """State 7,13: Switch judgment_3"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 36: Door from right to bottom left"""
        return 2
    elif ConditionGroup(5):
        """State 20,28: Switch judgment_7"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 44: Door from lower right to left"""
        return 10
    elif ConditionGroup(6):
        """State 8,14: Switch judgment_4"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 37: Door from bottom to top left"""
        return 3
    elif ConditionGroup(7):
        """State 21,29: Switch judgment_8"""
        IsObjDamaged(0, z81, -1, -4, 0)
        CompareObjState(0, z81, 30, 0)
        IsObjDamaged(0, z83, -1, -4, 0)
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 49: Door from bottom left to top"""
        return 15

def event_m50_35_x189(z80=50351215, z81=50353409, z82=32, z83=50353411):
    """[Preset] Rotating door with switch_135 degree version_Two switch version
    z80: Revolving door OBJ instance ID
    z81: Switch ① OBJ instance ID
    z82: Initial state OBJ state ID
    z83: Switch ②OBJ instance ID
    """
    """State 0,4: [Reproduction] Door that rotates with switch_135 degree version_Two switch version_SubState"""
    assert event_m50_35_x187(z81=z81, z80=z80, z82=z82, z83=z83)
    """State 3: [Condition] Door rotated by switch_135 degree version_Two switch version_SubState"""
    call = event_m50_35_x188(z81=z81, z80=z80, z83=z83)
    if call.Get() == 0:
        """State 1: [Execution] Door that rotates with switch_Two switches_SubState"""
        assert event_m50_35_x184(z80=z80, z90=80, z91=40, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 8:
        """State 5: [Execution] Door rotated by switch_Two switch version_2_SubState"""
        assert event_m50_35_x184(z80=z80, z90=83, z91=32, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 1:
        """State 6: [Execution] Door rotated by switch_Two switches_3_SubState"""
        assert event_m50_35_x184(z80=z80, z90=86, z91=43, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 9:
        """State 7: [Execution] Door rotated by switch_Two switches_4_SubState"""
        assert event_m50_35_x184(z80=z80, z90=81, z91=34, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 2:
        """State 8: [Execution] Door rotated by switch_Two switches_5_SubState"""
        assert event_m50_35_x184(z80=z80, z90=84, z91=42, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 10:
        """State 9: [Execution] Rotating door with switch_Two switches_6_SubState"""
        assert event_m50_35_x184(z80=z80, z90=87, z91=10, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 3:
        """State 10: [Execution] Door rotated by switch_Two switches_7_SubState"""
        assert event_m50_35_x184(z80=z80, z90=82, z91=41, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Get() == 15:
        """State 11: [Execution] Door that rotates with switch_Two switches_8_SubState"""
        assert event_m50_35_x184(z80=z80, z90=85, z91=30, z81=z81, z92=80, z93=10, z83=z83)
    elif call.Done():
        """State 2: [Execution] Door rotated by switch_Return switch_Two switches_SubState"""
        assert event_m50_35_x186(z81=z81, z88=80, z89=10, z83=z83)
    """State 12: End state"""
    return 0

def event_m50_35_x190(flag11=535000081, z78=900):
    """[Reproduction] Queen's lines
    flag11: Boss destruction flag
    z78: Generator ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Did you defeat the queen?"""
    if GetEventFlag(flag11) != 0:
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Not defeated"""
        return 0
    """State 5: The guests"""
    Label('L0')
    return 2

def event_m50_35_x191(z76=5030000, z77=4.5):
    """[Condition] Queen's lines
    z76: Boss Battle ID
    z77: Weight to serif
    """
    """State 0,1: Has the boss battle started?"""
    IsEventBossBattle(0, z76, 1)
    assert ConditionGroup(0)
    """State 2: Weight to serif"""
    CompareStateTime(0, z77, 3, z77)
    IsEventBossKill(1, z76, 0, 1)
    if ConditionGroup(1):
        """State 4: Defeat the boss"""
        return 1
    elif ConditionGroup(0):
        """State 3: End state"""
        return 0

def event_m50_35_x192(z79=535020082):
    """[Execution] Queen's lines
    z79: Line flag
    """
    """State 0,1: Line flag ON"""
    SetEventFlag(z79, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x193(z76=5030000, z77=4.5, flag11=535000081, z78=900, z79=535020082):
    """[Preset] Queen's lines
    z76: Boss Battle ID
    z77: Weight to serif
    flag11: Boss destruction flag
    z78: Generator ID
    z79: Line flag
    """
    """State 0,1: [Reproduction] Queen's lines_SubState"""
    call = event_m50_35_x190(flag11=flag11, z78=z78)
    if call.Get() == 0:
        """State 3: [Condition] Queen's lines_SubState"""
        call = event_m50_35_x191(z76=z76, z77=z77)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Queen's lines_SubState"""
            assert event_m50_35_x192(z79=z79)
    elif call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    """State 4: End state"""
    return 0

def event_m50_35_x194(flag10=535000096, z69=3403000):
    """[Reproduction] Filter change for Dragon Battle
    flag10: Boss destruction flag
    z69: Change point ID
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
    if GetEventFlag(flag10) != 0:
        """State 6: Defeated"""
        return 1
    else:
        """State 5: Undefeated"""
        return 0

def event_m50_35_x195(z66=901, z67=3.3, z68=535020095):
    """[Condition] Change the filter of Dragon Battle
    z66: Generator ID
    z67: Adjustment weight
    z68: Boss activation flag
    """
    """State 0,1: Did the boss start?"""
    CompareEventFlag(0, z68, 1)
    assert ConditionGroup(0)
    """State 2: Adjustment weight"""
    CompareStateTime(0, z67, 3, z67)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x196(z69=3403000):
    """[Execution] Filter change for Dragon Battle
    z69: Change point ID
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
    IsPlayerInsidePoint(0, z69, z69, 0)
    assert ConditionGroup(0)
    """State 3: Pop fog and parallel light filter"""
    PopFogFilter(0)
    PopParallelLightFilter(0)
    """State 4: Waiting for pop"""
    assert (GetFogFilterOverride() == 7) != 1 and (GetParallelLightFilterOverride() == 7) != 1
    """State 6: End state"""
    return 0

def event_m50_35_x197(z66=901, z67=3.3, z68=535020095, flag10=535000096, z69=3403000):
    """[Preset] Change the Dragon Battle filter
    z66: Generator ID
    z67: Adjustment weight
    z68: Boss activation flag
    flag10: Boss destruction flag
    z69: Change point ID
    """
    """State 0,1: [Reproduce] Change Dragon Battle Filter_SubState"""
    call = event_m50_35_x194(flag10=flag10, z69=z69)
    if call.Get() == 1:
        """State 7: [Conditions] Dragon Battle Filter Change_Point Judgment_2_SubState"""
        assert event_m50_35_x210(z69=z69, z70=1)
        """State 8: [Execution] Filter change for Dragon Battle_Sky_2_SubState"""
        assert event_m50_35_x212()
        """State 9: [Reproduction] Dragon Battle Filter Change_Sky_2_SubState"""
        assert event_m50_35_x211()
    elif call.Get() == 0:
        """State 6: [Condition] Change of Dragon Battle Filter_Point Judgment_SubState"""
        assert event_m50_35_x210(z69=z69, z70=1)
        """State 4: [Execution] Dragon Battle Filter Change_Sky_SubState"""
        assert event_m50_35_x212()
        """State 2: [Reproduction] Dragon Battle Filter Change_Sky_SubState"""
        assert event_m50_35_x211()
        """State 5: [Condition] Change filter of Dragon Battle_SubState"""
        assert event_m50_35_x195(z66=z66, z67=z67, z68=z68)
    """State 3: [Execution] Dragon Battle Filter Change_SubState"""
    assert event_m50_35_x196(z69=z69)
    """State 10: Rerun"""
    return 0

def event_m50_35_x198(flag8=535000096):
    """[Reproduction] Poison Dragon Battle_Start
    flag8: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_35_x199(z58=3400000, z75=3400000):
    """[Condition] Poison Dragon Battle_Start
    z58: Start point ID
    z75: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z58, z75, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z58, z75, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x200(z55=5030030):
    """[Execution] Poison Dragon Battle Start
    z55: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z55)
    """State 2: End state"""
    return 0

def event_m50_35_x201():
    """[Reproduction] Poison Dragon Battle_HP Display and BGM Playback_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x202(z54=502, z57=5.5, z55=5030030, z72=1, z73=535020097, z74=535020098):
    """[Execution] Poison Dragon Battle _HP display and BGM playback
    z54: Sound ID
    z57: Weight until BGM display
    z55: Boss Battle ID
    z72: Weight until HP display
    z73: BGM display flag
    z74: HP gauge display flag
    """
    """State 0,3: Wait until BGM playback"""
    CompareStateTime(0, z57, 2, z57)
    CompareEventFlag(0, z73, 1)
    IsEventBossKill(1, z55, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z54)
        """State 5: BGM display flag ON"""
        SetEventFlag(z73, 1)
        """State 4: Weight until HP display"""
        CompareStateTime(0, z72, 2, z72)
        CompareEventFlag(0, z74, 1)
        IsEventBossKill(1, z55, 0, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            pass
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 6: HP gauge display flag ON"""
    SetEventFlag(z74, 1)
    """State 7: End state"""
    return 0

def event_m50_35_x203():
    """[Reproduction] Poison Dragon Battle_HP Display and BGM Playback_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x204(z55=5030030):
    """[Condition] Poison Dragon Battle_HP Display and BGM Playback_End
    z55: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z55, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x205(z54=502, z55=5030030, z56=535020095, z71=0):
    """[Execution] Poison Dragon Battle_HP Display and BGM Playback_End
    z54: Sound ID
    z55: Boss Battle ID
    z56: Other flags for logic
    z71: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z56, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z55)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > 0) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z54)
    """State 5: End state"""
    return 0

def event_m50_35_x206(z60=3400010, z59=901, z56=535020095):
    """[Condition] Poison Dragon Battle_Start
    z60: Boss activation point ID
    z59: Generator ID
    z56: Logic flag
    """
    """State 0,1: Entered the activation point or dealt damage or activated or destroyed"""
    IsPlayerInsidePoint(0, z60, z60, 1)
    CompareChrHpRatio(0, z59, 100, 4)
    CompareEventFlag(0, z56, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x207(z56=535020095):
    """[Execution] Poison Dragon Battle _Start
    z56: Logic flag
    """
    """State 0,1: Logic flag ON"""
    SetEventFlag(z56, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x208():
    """Event not executed"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x209(flag8=535000096, z54=502, z55=5030030, z56=535020095, z57=5.5, z58=3400000, z59=901,
                      z60=3400010):
    """[Preset] Poison Dragon Battle
    flag8: Boss destruction flag
    z54: Sound ID
    z55: Boss Battle ID
    z56: Other flags for logic
    z57: Wait time
    z58: Start and end point ID
    z59: Boss generator ID
    z60: Boss activation point ID
    """
    """State 0,3: [Reproduction] Poison Dragon Battle_Start_SubState"""
    call = event_m50_35_x198(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 10: [Condition] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x199(z58=z58, z75=z58)
        """State 7: [Execution] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x200(z55=z55)
        """State 4: [Reproduction] Poison Dragon Battle_Start_Sky_SubState"""
        assert event_m50_35_x208()
        """State 11: [Condition] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x206(z60=z60, z59=z59, z56=z56)
        """State 8: [Execution] Poison Dragon Battle_Start_SubState"""
        assert event_m50_35_x207(z56=z56)
        """State 1: [Reproduction] Poison Dragon Battle_HP Display and BGM Playback_Sky_SubState"""
        assert event_m50_35_x201()
        """State 12: [Condition] Poison Dragon Battle_HP Display and BGM Playback_Sky_SubState"""
        assert event_m50_35_x225()
        """State 5: [Execution] Poison Dragon Battle_HP Display and BGM Playback_SubState"""
        assert event_m50_35_x202(z54=z54, z57=z57, z55=z55, z72=1, z73=535020097, z74=535020098)
        """State 2: [Reproduction] Poison Dragon Battle_HP Display and BGM Playback_End_Sky_SubState"""
        assert event_m50_35_x203()
        """State 9: [Condition] Poison Dragon Battle_HP Display and BGM Playback_End_SubState"""
        assert event_m50_35_x204(z55=z55)
        """State 6: [Execution] Poison Dragon Battle_HP Display and BGM Playback_End_SubState"""
        assert event_m50_35_x205(z54=z54, z55=z55, z56=z56, z71=0)
    """State 13: End state"""
    return 0

def event_m50_35_x210(z69=3403000, z70=1):
    """[Condition] Filter change for dragon battle_Point judgment
    z69: Change point ID
    z70: Are you inside
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z69, z69, z70)
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

def event_m50_35_x214(z61=50352000, z62=5300000):
    """[Execution] Door opened with DLC purchase_Manual
    z61: Door OBJ instance ID
    z62: Navigation switching point ID
    """
    """State 0,3: Activate key guide"""
    DisableObjKeyGuide(z61, 0)
    """State 1: Waiting for the door to finish"""
    CompareObjState(0, z61, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation switching"""
    DeleteNavimeshAttribute(z62, 2)
    """State 4: End state"""
    return 0

def event_m50_35_x215(flag1=535000036, z1=50356110):
    """[Reproduction] Crown that appears when a boss is destroyed
    flag1: Crown acquisition flag
    z1: Crown OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you acquired the crown?"""
    if GetEventFlag(flag1) != 1:
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

def event_m50_35_x217(z2=535000096):
    """[Condition] Crown that appears when a boss is destroyed
    z2: Defeat flag
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

def event_m50_35_x221(z1=50356110, flag1=535000036, z3=5, action1=5310):
    """[Execution] Crowns that appear when the boss is destroyed
    z1: Crown OBJ instance ID
    flag1: Crown acquisition flag
    z3: weight
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
    SetEventFlag(flag1, 1)
    """State 5: weight"""
    CompareStateTime(0, z3, 3, z3)
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

def event_m50_35_x223(z1=50356110, flag1=535000036, z2=535000096, z3=5, action1=5310):
    """[Preset] Crown that appears when a boss is destroyed
    z1: Crown OBJ instance ID
    flag1: Crown acquisition flag
    z2: Defeat flag
    z3: weight
    action1: Text ID
    """
    """State 0,1: [Reproduction] Crown _SubState that appears when a boss is destroyed"""
    call = event_m50_35_x215(flag1=flag1, z1=z1)
    if call.Get() == 0:
        """State 7: [Condition] Crown that appears when boss is destroyed _ Defeat determination_SubState"""
        call = event_m50_35_x217(z2=z2)
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
                assert event_m50_35_x221(z1=z1, flag1=flag1, z3=z3, action1=action1)
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

def event_m50_35_x224(z61=50352000):
    """[Execution] Door opened with DLC purchase
    z61: Door OBJ instance ID
    """
    """State 0,3: Did you approach the door?"""
    CompareObjPlayerDistance(0, z61, 4, 5)
    assert ConditionGroup(0)
    """State 1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z61, 8, 3)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x225():
    """[Condition] Poison Dragon Battle_HP Display and BGM Playback_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x226(flag7=535000034, z47=50352100, z52=71, z53=20):
    """[Execution] Awakening Dragon_2
    flag7: Event executed flag
    z47: Dragon OBJ instance ID
    z52: Flight OBJ State ID
    z53: OBJ state ID after flight
    """
    """State 0,1: Executed flag ON"""
    SetEventFlag(flag7, 1)
    """State 2: Dragon flight and breath request"""
    ChangeObjState(z47, z52)
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
    CompareObjState(0, z47, z53, 0)
    assert ConditionGroup(0)
    """State 7: Finish"""
    return 0

def event_m50_35_x227(z6=900, z45=8506, z7=50001000, z8=50001039, z46=72):
    """[Execution] Queen's enemy summons
    z6: Boss generator ID
    z45: Zako ① Generator ID
    z7: Start point ID
    z8: End point ID
    z46: OBJ state ID for SFX
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1"""
        SetAreaVariable(1, GetPointCloseToCharacter(z7, z8, z6, 2))
    else:
        pass
    """State 7: Host wait"""
    IsHost(0, 1, 0)
    assert HostConditionGroup(0)
    """State 4: Move Damipoly 1 for SFX"""
    WarpObjToPoint(50352050, GetAreaVariable(1))
    """State 8: SFX playback"""
    ChangeObjState(50352050, z46)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z6)
    if HostConditionGroup(1):
        pass
    elif HostConditionGroup(0):
        """State 5: Summon character 1 generation"""
        ForceGenerationFromPoint(z45, GetAreaVariable(1), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z6, 7, 1, 1)
        IsChrDead(0, z6)
        assert HostConditionGroup(0)
    """State 10: Rerun"""
    return 0

def event_m50_35_x228(z6=900, z41=_, z42=_, z43=_, z7=50001000, z8=50001039, z44=_):
    """[Execution] Queen's enemy summon _3 body version
    z6: Boss generator ID
    z41: Zako ① Generator ID
    z42: Zako ② Generator ID
    z43: Zako ③ Generator ID
    z7: Start point ID
    z8: End point ID
    z44: OBJ state ID for SFX
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1 to 3"""
        SetAreaVariable(1, GetPointCloseToCharacter(z7, z8, z6, 2))
        SetAreaVariable(2, GetPointCloseToCharacter(z7, z8, z6, 3))
        SetAreaVariable(3, GetPointCloseToCharacter(z7, z8, z6, 4))
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
    ChangeObjState(50352050, z44)
    ChangeObjState(50352051, z44)
    ChangeObjState(50352052, z44)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z6)
    if HostConditionGroup(0):
        """State 5: Generate 3 summoned characters 1"""
        ForceGenerationFromPoint(z41, GetAreaVariable(1), 1)
        ForceGenerationFromPoint(z42, GetAreaVariable(2), 1)
        ForceGenerationFromPoint(z43, GetAreaVariable(3), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z6, 7, 1, 1)
        IsChrDead(0, z6)
        assert HostConditionGroup(0)
    elif HostConditionGroup(1):
        pass
    """State 10: Rerun"""
    return 0

def event_m50_35_x229(z34=50351750, z36=80, z37=10, z33=50353310, z35=50351760, z38=250, z39=251, z40=0):
    """[Execution] Switch thorn floor switch with flag OFF
    z34: Thorn ① OBJ instance ID
    z36: Operating OBJ state ID
    z37: Thorn Operation End OBJ State ID
    z33: Switch OBJ instance ID
    z35: Thorn ② OBJ instance ID
    z38: Replacement GM ①
    z39: Replacement GM ②
    z40: GM slot
    """
    """State 0,5: Switch is up"""
    ChangeObjState(z33, 70)
    """State 6: Waiting for switch operation to end"""
    CompareObjState(0, z33, 30, 0)
    assert ConditionGroup(0)
    """State 1: Thorn is in operation"""
    ChangeObjState(z34, z36)
    ChangeObjState(z35, z36)
    """State 8: weight"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 7: Grand material switching"""
    SetGroundMaterial(10, z38, z40)
    SetGroundMaterial(10, z39, z40)
    """State 3: Waiting for thorn to finish operation"""
    CompareObjState(8, z34, z37, 0)
    CompareObjState(8, z35, z37, 0)
    assert ConditionGroup(8)
    """State 9: Thorn floor state flag OFF"""
    SetEventFlag(535000028, 0)
    """State 2: Switch back"""
    ChangeObjState(z33, 80)
    """State 4: Wait for switch to finish"""
    CompareObjState(0, z33, 10, 0)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m50_35_x230(z31=50353825, z32=535020024):
    """[Reproduction] Enemy activation on the building
    z31: Building OBJ instance ID
    z32: Enemy activation flag
    """
    """State 0,1: Judgment of building condition"""
    if CompareObjStateId(z31, 70, 0):
        """State 2: The building is waiting to rise"""
        assert CompareObjStateId(z31, 30, 0)
        """State 6: Navigation change waiting"""
        assert (GetStateTime() > 0.2) != 0
        """State 4: Enemy activation flag ON"""
        SetEventFlag(z32, 1)
        """State 7: Building: on"""
        return 0
    else:
        """State 3,5: Enemy activation flag OFF"""
        SetEventFlag(z32, 0)
        """State 8: Building: not above"""
        return 1

def event_m50_35_x231(z31=50353825):
    """[Condition] Enemy activation on the building
    z31: Building OBJ instance ID
    """
    """State 0,2: The building started to rise?"""
    CompareObjState(0, z31, 70, 0)
    assert ConditionGroup(0)
    """State 1: Waiting for the building to rise"""
    CompareObjState(0, z31, 30, 0)
    assert ConditionGroup(0)
    """State 3: weight"""
    CompareStateTime(0, 0.2, 3, 0.2)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_35_x232(z32=535020024, z31=50353825):
    """[Execution] Enemy activation on the building
    z32: Enemy activation flag
    z31: Building OBJ instance ID
    """
    """State 0,1: Enemy activation flag ON"""
    SetEventFlag(z32, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z31, 30, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x233(z31=50353825, z32=535020024):
    """[Preset] Enemy activation on the building
    z31: Building OBJ instance ID
    z32: Enemy activation flag
    """
    """State 0,1: [Reproduction] Enemy activation on the building_SubState"""
    call = event_m50_35_x230(z31=z31, z32=z32)
    if call.Get() == 0:
        """State 4: [Condition] Enemy activation on the building_Descent judgment_SubState"""
        assert event_m50_35_x234(z31=z31)
        """State 2: [Execution] Enemy activation on the building_After descent_SubState"""
        assert event_m50_35_x235(z32=z32, z31=z31)
    elif call.Get() == 1:
        """State 5: [Condition] Enemy activation on the building_Rise determination_SubState"""
        assert event_m50_35_x231(z31=z31)
        """State 3: [Execution] Enemy activation on the building_After rising_SubState"""
        assert event_m50_35_x232(z32=z32, z31=z31)
    """State 6: Rerun"""
    return 0

def event_m50_35_x234(z31=50353825):
    """[Condition] Enemy activation on the building
    z31: Building OBJ instance ID
    """
    """State 0,1: Did the building begin to descend?"""
    CompareObjState(0, z31, 80, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x235(z32=535020024, z31=50353825):
    """[Execution] Enemy activation on the building
    z32: Enemy activation flag
    z31: Building OBJ instance ID
    """
    """State 0,1: Enemy activation flag OFF"""
    SetEventFlag(z32, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z31, 70, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_35_x236(flag5=100702):
    """[Reproduction] Clear DLC event_C route petrification
    flag5: Achievement flag
    """
    """State 0,1: Already cleared?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Cleared"""
        return 1
    else:
        """State 2: Not cleared"""
        return 0

def event_m50_35_x237(z30=101053):
    """[Conditions] Clear DLC event_C route petrification
    z30: Boss destruction flag
    """
    """State 0,1: Boss destruction waiting"""
    CompareEventFlag(0, z30, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x238(flag5=100702):
    """[Execution] Clear DLC event_C route petrification
    flag5: Achievement flag
    """
    """State 0,1: Clear flag ON"""
    SetEventFlag(flag5, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x239(z30=101053, flag5=100702):
    """[Preset] Clear DLC event_C root petrification
    z30: Boss destruction flag
    flag5: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_Clation of C root petrification_SubState"""
    call = event_m50_35_x236(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Inter-DLC event_Clation of C route petrification_SubState"""
        assert event_m50_35_x237(z30=z30)
        """State 2: [Execution] Inter-DLC event_C route petrification clear_SubState"""
        assert event_m50_35_x238(flag5=flag5)
    """State 4: End state"""
    return 0

def event_m50_35_x240(flag3=_):
    """[Reproduction] Inter-DLC event_annihilation
    flag3: Achievement flag
    """
    """State 0,1: Already achieved?"""
    if GetEventFlag(flag3) != 0:
        """State 3: Accomplished"""
        return 1
    else:
        """State 2: Not Achieved"""
        return 0

def event_m50_35_x241(z25=6000, z26=6001, z27=6002, z28=6003, z29=6004):
    """[Condition] Event between DLCs
    z25: Generator ① ID
    z26: Generator ② ID
    z27: Generator ③ ID
    z28: Generator ④ ID
    z29: Generator ⑤ ID
    """
    """State 0,1: Did you annihilate the improper?"""
    IsChrDeadOrRespawnOver(8, z25, 1)
    IsChrDeadOrRespawnOver(8, z26, 1)
    IsChrDeadOrRespawnOver(8, z27, 1)
    IsChrDeadOrRespawnOver(8, z28, 1)
    IsChrDeadOrRespawnOver(8, z29, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_35_x242(flag3=_):
    """[Execution] Inter-DLC event_annihilation
    flag3: Achievement flag
    """
    """State 0,1: Clear flag ON"""
    SetEventFlag(flag3, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x243(z25=6000, z26=6001, z27=6002, z28=6003, z29=6004, flag4=100700):
    """[Preset] Inter-DLC events
    z25: Generator ① ID
    z26: Generator ② ID
    z27: Generator ③ ID
    z28: Generator ④ ID
    z29: Generator ⑤ ID
    flag4: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_annihilation_SubState"""
    call = event_m50_35_x240(flag3=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Inter-DLC event_Suspicious annihilation_SubState"""
        assert event_m50_35_x241(z25=z25, z26=z26, z27=z27, z28=z28, z29=z29)
        """State 2: [Execution] Inter-DLC event_annihilation_SubState"""
        assert event_m50_35_x242(flag3=flag4)
    """State 4: End state"""
    return 0

def event_m50_35_x244(z19=6500, z20=6510, z21=6530, z22=6531, z23=6540, z24=6550):
    """[Conditions] Event between DLC_Dragon Blood Knight
    z19: Generator ① ID
    z20: Generator ② ID
    z21: Generator ③ ID
    z22: Generator ④ ID
    z23: Generator ⑤ ID
    z24: Generator ⑥ ID
    """
    """State 0,1: Has the dragon blood knight been annihilated?"""
    IsChrDeadOrRespawnOver(8, z19, 1)
    IsChrDeadOrRespawnOver(8, z20, 1)
    IsChrDeadOrRespawnOver(8, z21, 1)
    IsChrDeadOrRespawnOver(8, z22, 1)
    IsChrDeadOrRespawnOver(8, z23, 1)
    IsChrDeadOrRespawnOver(8, z24, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_35_x245(z19=6500, z20=6510, z21=6530, z22=6531, z23=6540, z24=6550, flag3=100701):
    """[Preset] Inter-DLC event_Dragon Blood Knight
    z19: Generator ① ID
    z20: Generator ② ID
    z21: Generator ③ ID
    z22: Generator ④ ID
    z23: Generator ⑤ ID
    z24: Generator ⑥ ID
    flag3: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_annihilation_SubState"""
    call = event_m50_35_x240(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Event between DLC_Dragon Blood Knight Extermination_SubState"""
        assert event_m50_35_x244(z19=z19, z20=z20, z21=z21, z22=z22, z23=z23, z24=z24)
        """State 2: [Execution] Inter-DLC event_annihilation_SubState"""
        assert event_m50_35_x242(flag3=flag3)
    """State 4: End state"""
    return 0

def event_m50_35_x246():
    """[Execution] Crown that appears after destroying the boss_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_35_x247(z6=900, z14=8500, z15=8501, z16=8502, z7=50001000, z8=50001039, z17=71, z18=8507):
    """[Execution] Queen's enemy summon _4 body version
    z6: Boss generator ID
    z14: Zako ① Generator ID
    z15: Zako ② Generator ID
    z16: Zako ③ Generator ID
    z7: Start point ID
    z8: End point ID
    z17: OBJ state ID for SFX
    z18: Zako ④ Generator ID
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1 to 4"""
        SetAreaVariable(1, GetPointCloseToCharacter(z7, z8, z6, 2))
        SetAreaVariable(2, GetPointCloseToCharacter(z7, z8, z6, 3))
        SetAreaVariable(3, GetPointCloseToCharacter(z7, z8, z6, 4))
        SetAreaVariable(4, GetPointCloseToCharacter(z7, z8, z6, 5))
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
    ChangeObjState(50352050, z17)
    ChangeObjState(50352051, z17)
    ChangeObjState(50352052, z17)
    ChangeObjState(50352053, z17)
    """State 9: Enemy regeneration weight or boss defeat determination"""
    CompareStateTime(0, 3.5, 3, 3.5)
    IsChrDead(1, z6)
    if HostConditionGroup(0):
        """State 5: Generate 4 summoned characters"""
        ForceGenerationFromPoint(z14, GetAreaVariable(1), 1)
        ForceGenerationFromPoint(z15, GetAreaVariable(2), 1)
        ForceGenerationFromPoint(z16, GetAreaVariable(3), 1)
        ForceGenerationFromPoint(z18, GetAreaVariable(4), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z6, 7, 1, 1)
        IsChrDead(0, z6)
        assert HostConditionGroup(0)
    elif HostConditionGroup(1):
        pass
    """State 10: Rerun"""
    return 0

def event_m50_35_x248(z6=900, z9=8500, z10=8501, z11=8502, z7=50001000, z8=50001039, z12=8507, z13=8508):
    """[Execution] Queen's enemy summon _5 body version
    z6: Boss generator ID
    z9: Zako ① Generator ID
    z10: Zako ② Generator ID
    z11: Zako ③ Generator ID
    z7: Start point ID
    z8: End point ID
    z12: Zako ④ Generator ID
    z13: Zako ⑤ Generator ID
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        """State 3: Point lottery 1 to 5"""
        SetAreaVariable(1, GetPointCloseToCharacter(z7, z8, z6, 2))
        SetAreaVariable(2, GetPointCloseToCharacter(z7, z8, z6, 3))
        SetAreaVariable(3, GetPointCloseToCharacter(z7, z8, z6, 4))
        SetAreaVariable(4, GetPointCloseToCharacter(z7, z8, z6, 5))
        SetAreaVariable(5, GetPointCloseToCharacter(z7, z8, z6, 6))
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
    IsChrDead(1, z6)
    if HostConditionGroup(0):
        """State 5: Generate summoned characters 1 to 5"""
        ForceGenerationFromPoint(z9, GetAreaVariable(1), 1)
        ForceGenerationFromPoint(z10, GetAreaVariable(2), 1)
        ForceGenerationFromPoint(z11, GetAreaVariable(3), 1)
        ForceGenerationFromPoint(z12, GetAreaVariable(4), 1)
        ForceGenerationFromPoint(z13, GetAreaVariable(5), 1)
        """State 2,1: End of summoning action of queen"""
        CompareChrEzStateValue(0, z6, 7, 1, 1)
        IsChrDead(0, z6)
        assert HostConditionGroup(0)
    elif HostConditionGroup(1):
        pass
    """State 10: Rerun"""
    return 0

def event_m50_35_x249(flag2=535000096):
    """[Reproduction] Bowing management of NPC
    flag2: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag2) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_35_x250(z4=901):
    """[Conditions] NPC bow management
    z4: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z4, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_35_x251(z5=535020038):
    """[Execution] Bowing management of NPC
    z5: Bowing flag
    """
    """State 0,1: Bowing flag ON"""
    SetEventFlag(z5, 1)
    """State 2: End state"""
    return 0

def event_m50_35_x252(flag2=535000096, z4=901, z5=535020038):
    """[Preset] NPC bow management
    flag2: Defeat flag
    z4: Boss generator ID
    z5: Bowing flag
    """
    """State 0,1: [Reproduction] NPC bow management_SubState"""
    call = event_m50_35_x249(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] NPC bow management_SubState"""
        assert event_m50_35_x250(z4=z4)
        """State 2: [Execution] NPC bow management_SubState"""
        assert event_m50_35_x251(z5=z5)
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
    event_m50_35_x16(z250=710)
    Quit()

def event_m50_35_110001():
    """White spirit sign display_02"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z250=711)
    Quit()

def event_m50_35_110002():
    """White spirit sign display_03"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z250=712)
    Quit()

def event_m50_35_110003():
    """White spirit sign display_04"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z250=713)
    Quit()

def event_m50_35_110004():
    """White spirit sign display_05"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_35_x16(z250=714)
    Quit()

def event_m50_35_110005():
    """White spirit sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m50_35_x23(z235=102430, z236=715, z237=104160, z238=103660, z239=-1)
    Quit()

def event_m50_35_110006():
    """White spirit: Counting up the moonlight"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m50_35_x21(z244=535000081, z245=102436, z246=205, z247=7430)
    Quit()

def event_m50_35_110010():
    """Black spirit display_01"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_35_x33(z226=10000000, z227=700, z228=0, z229=0.2, z230=535020020)
    Quit()
    """Unused"""
    """State 1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m50_35_x22(z240=10000000, z241=700, z242=0, z243=0.2)
    Quit()

def event_m50_35_110011():
    """Black Spirit Display_02"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_35_x33(z226=10000010, z227=720, z228=0, z229=0.2, z230=535020022)
    Quit()
    """Unused"""
    """State 1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m50_35_x22(z240=10000010, z241=720, z242=0, z243=0.2)
    Quit()

def event_m50_35_4000000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m50_35_x37(flag17=535020010, z214=14, flag18=535000011, z215=5, z216=20)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m50_35_x42(z219=80000000, z220=0, z221=5, z222=974, val4=1, z223=20, z224=80000001,
                z225=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m50_35_x42(z219=80000100, z220=0, z221=5, z222=974, val4=2, z223=20, z224=80000101,
                z225=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m50_35_x42(z219=80000200, z220=0, z221=5, z222=974, val4=3, z223=20, z224=80000201,
                z225=80000299))
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert (event_m50_35_x42(z219=80000300, z220=0, z221=5, z222=974, val4=4, z223=20, z224=80000301,
                z225=80000399))
        """State 8: [Lib] [DC] [Preset] Wanderer_Generation_5_SubState"""
        assert (event_m50_35_x42(z219=80000400, z220=0, z221=5, z222=974, val4=5, z223=20, z224=80000401,
                z225=80000499))
        """State 2: Start flag ON"""
        SetEventFlag(535020012, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_35_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m50_35_x45(flag19=535000011, z217=974, mode1=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

