# -*- coding: utf-8 -*-
def event_m10_16_2000():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z57=10161070, z58=10161025, z59=30, z60=200000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_2010():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z57=10161060, z58=10161026, z59=30, z60=201000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_2020():
    """Iron lattice rising with wall hole lever _ underground"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z57=10161062, z58=10161027, z59=20, z60=202000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_2030():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Lattice open by lever_passage_SubState"""
    assert event_m10_16_x202(z27=10161071, z28=10161072, z29=10161028, z30=203000, z31=203001, z32=30)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_2040():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z57=10161073, z58=10161029, z59=30, z60=204000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_3000():
    """Elevator (below boss room)"""
    """State 0,2: Standby for initial position setting"""
    assert EventEnded(3030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_16_x16(z138=10161020, z139=300000, z140=300001, z141=10161021, z142=10161022)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_3010():
    """Elevator (below boss room) lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z194=10161020, z195=10161021, z196=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_3020():
    """Elevator (below boss room) under lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z194=10161020, z195=10161022, z196=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_3030():
    """Elevator (under boss room) initial position setting"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m10_16_x29(z191=10161020, z192=40, flag24=116000005, z193=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4000():
    """Bell guard_bell lever"""
    """State 0,3: [Lib] [Preset] Bell guard_Lever that rings the bell_SubState"""
    call = event_m10_16_x93(z100=10161023, z101=10161050, mode3=0, z102=0, z103=0, z104=10161051, z105=10160620,
                            z106=400000)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m10_16_4010():
    """Kanemori_Receiving the bell net"""
    """State 0,2: [Lib] [Preset] Kanemori_Net reception_SubState"""
    assert event_m10_16_x85(z111=12000, mode4=1, mode5=1, mode6=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_4020():
    """Jewel guard"""
    """State 0,2: [Lib] [Preset] Kanemori _ Judgment Spirit Lever Use Decision_SubState"""
    assert event_m10_16_x92(z110=10161023)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_5000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161150, z150=20, z151=500000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_5010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161185, z150=20, z151=501000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_5020():
    """Hidden Door Navi Mesh Change 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161170, z150=20, z151=502000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_5030():
    """Hidden Door Navi Mesh Change 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161190, z150=20, z151=503000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_6000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_16_x34(z181=10161030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_6010():
    """[Insect key] Hidden door ① 1"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_16_x44(z179=10161030, val3=10160000, z180=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_6030():
    """[Insect Key] 1_Navimesh change for hidden doors ①"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161100, z150=20, z151=603000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_6100():
    """[Insect key] Hidden door ② For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_16_x34(z181=10161031)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_6110():
    """[Insect key] Hidden door ②"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_16_x44(z179=10161031, val3=10160010, z180=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_6120():
    """[Insect key] Hidden door ②_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161110, z150=20, z151=612000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_8000():
    """Boss room lighting_Right"""
    """State 0,2: [Preset] Boss room lighting_SubState"""
    assert event_m10_16_x162(z64=10160753, z65=10161002, z66=10161000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_8010():
    """Boss room lighting_Left"""
    """State 0,2: [Preset] Boss room lighting_SubState"""
    assert event_m10_16_x162(z64=10160752, z65=10161003, z66=10161001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_8020():
    """Boss room lock-on parameter change"""
    """State 0,3: [Preset] Change lock ID of boss room_SubState"""
    call = event_m10_16_x172(z2=116000086, z3=10161000, z4=10161001, z5=802000, z6=626000, z7=626001,
                             z8=626002, z9=1016010)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_16_9000():
    """Changed Navimesh of wall 1 to destroy with flame barrel"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161040, z150=20, z151=900000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_9010():
    """Changed Navimesh of Wall 2 to be destroyed by a flame barrel"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161045, z150=20, z151=901000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_10000():
    """Treasure corpse falls due to tower destruction"""
    """State 0,2: [Reproduction] Treasure corpse fall due to yagura destruction_Sky_SubState"""
    assert event_m10_16_x166()
    """State 4: [Condition] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_16_x167(z63=10161300)
    """State 3: [Execution] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_16_x168(z61=10166010, z62=70)
    """State 1: Finish"""
    Quit()

def event_m10_16_11000():
    """Navimesh change due to yagura destruction 1"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x181(z49=10161300, z50=1100000, z51=1100001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_11010():
    """Navimesh change due to yagura destruction 2"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x181(z49=10161325, z50=1101000, z51=1101001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_11020():
    """Navimesh change due to yagura destruction 3"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x181(z49=10161320, z50=1102000, z51=1102001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_13000():
    """When a stone is hit, an enemy-filled spear appears from the well"""
    """State 0,2: [Preset] Encroachment of enemies from a well when hitting a stone_SubState"""
    assert event_m10_16_x193(z37=10162000, z38=10162010, z39=116020015, z40=4, z41=116000016)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_14000():
    """Boss: Warrior in the Mirror_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_16_x9(flag25=116000081, z197=1400000, z198=1400000, z199=102, z200=1016000, z201=116020080,
            mode8=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_14100():
    """Navi mesh change of hidden door in boss room 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161160, z150=20, z151=1410000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_14110():
    """Navi mesh change of hidden door in boss room 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161155, z150=20, z151=1411000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_14120():
    """Navi mesh change of hidden door in boss room 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161165, z150=20, z151=1412000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_14130():
    """Navi mesh change of hidden door in boss room 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161175, z150=20, z151=1413000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_14140():
    """Navi mesh change of hidden door in boss room 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z149=10161180, z150=20, z151=1414000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_15000():
    """Boss: Forgotten Sinner_Battle"""
    """State 0,2: Is the poly drama replay event over?"""
    assert EventEnded(15010) != 0
    """State 3: [Preset] Boss: Forgotten Sinner Battle_SubState"""
    assert (event_m10_16_x218(flag4=116000086, z18=1500000, z19=1016010, z20=116020085, z21=5, z22=848,
            z23=101, mode1=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_15010():
    """Boss: Forgotten Sinner_Poly Play"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m10_16_x33(z186=10160602, z187=101610, flag23=116000087, z188=1501000, z189=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_15020():
    """Boss: Forgotten Sinner _ Zako Launch"""
    """State 0,2: [Preset] Forgotten Sinner_Zako Launch_SubState"""
    assert event_m10_16_x188(z47=1016010, z48=848)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_16000():
    """Boss: Gargoyle (Zakobos) _Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_16_x9(flag25=116000091, z197=1600000, z198=1600000, z199=103, z200=1016020, z201=116020090,
            mode8=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_16010():
    """Boss: Gargoyle statues starting sequentially"""
    """State 0,6: [Preset] Sequentially activated gargoyle image_SubState"""
    assert event_m10_16_x192(flag5=116000091, z42=1016020, z43=100, z44=116020092, z45=1, z46=2)
    """State 2: [Preset] Sequentially activated gargoyle image_1_SubState"""
    assert event_m10_16_x192(flag5=116000091, z42=1016020, z43=100, z44=116020092, z45=10, z46=1)
    """State 3: [Preset] Sequentially activated gargoyle image_2_SubState"""
    assert event_m10_16_x192(flag5=116000091, z42=1016020, z43=90, z44=116020092, z45=10, z46=1)
    """State 4: [Preset] Sequentially activated gargoyle image_3_SubState"""
    assert event_m10_16_x192(flag5=116000091, z42=1016020, z43=70, z44=116020092, z45=10, z46=1)
    """State 5: [Preset] Sequentially activated gargoyle image_4_SubState"""
    assert event_m10_16_x192(flag5=116000091, z42=1016020, z43=50, z44=116020092, z45=10, z46=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_17000():
    """One-way door of the round tower"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m10_16_x6(z212=0, z213=1101, z214=1700000, z215=116000057)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_17010():
    """OBJ blocking a one-way door"""
    """State 0,2: [Preset] OBJ_SubState that blocks a one-way door"""
    assert event_m10_16_x208(z25=10161550, z26=116000057)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18010():
    """The lock door that opens with `` jail key '' _ 2"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000041)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18030():
    """The lock door_4 that opens with the key of the prison_4"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000043)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18050():
    """The lock door_6 that opens with the key of the prison_6"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000045)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18060():
    """The key door to open with the key of the prison _7"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000046)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18120():
    """The key door to open with the key of the prison _13"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000052)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18130():
    """Key door to open with `` jail key '' _ 14"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000053)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_18140():
    """Key door to open with `` jail key '' _ 15"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50800000, z219=116000054)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_19000():
    """Navi-mesh changes after removing the petrified fossil"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_16_x77(z122=1900000, z123=0, z124=2, flag21=0, flag22=102741)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_22000():
    """Rolling flame barrels_1F staircase"""
    """State 0,2: [Preset] Rolling flame barrel_1F staircase_SubState"""
    assert event_m10_16_x179(z52=2200000, z53=2200010, z54=10164900, z55=116020013, z56=9990, flag6=116000011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_23000():
    """One door open from the beginning"""
    """State 0,2: Make one door open"""
    ChangeObjState(10160401, 74)
    assert CompareObjStateId(10160401, 30, 0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_23010():
    """Lock door that is open from the beginning"""
    """State 0,2: Keep the key door open"""
    ChangeObjState(10160431, 74)
    DisableObjKeyGuide(10160431, 1)
    assert CompareObjStateId(10160431, 30, 0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_24000():
    """Blacksmith treasure chest"""
    """State 0,3: Event end judgment"""
    assert EventEnded(111374) != 0
    """State 4: [Preset] Blacksmith Treasure Box_SubState"""
    call = event_m10_16_x200(z33=10165150, z34=165, z35=103790, z36=104290)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_16_25000():
    """End bonfire _ sinner"""
    """State 0,3: [Lib] [Preset] End special bonfire_SubState"""
    assert event_m10_16_x102(z109=10162200, flag18=100300)
    """State 1: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 2: [Lib] [Preset] Terminal Lighthouse_SubState"""
    # action:2022:"A primal bonfire was rekindled"
    event_m10_16_x84(z112=10162200, action1=2022, flag19=100300)
    Quit()

def event_m10_16_26000():
    """Torture lift_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_Relief_SubState"""
    assert event_m10_16_x113(z97=10162020, z98=30, flag15=116000020, z99=32)
    """State 3: [Lib] [Preset] Elevator_Initialization_Relief_2_SubState"""
    assert event_m10_16_x113(z97=10162021, z98=31, flag15=116000021, z99=33)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_26010():
    """Torture lift"""
    """State 0,2: [Lib] [Preset] Torture lift_operation_SubState"""
    assert (event_m10_16_x45(z171=26000, z172=10162020, z173=10162021, z174=30, z175=2600003, z176=2600002,
            z177=2600001, z178=2600000))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_26020():
    """Torture lift_action judgment"""
    """State 0,2: [Lib] [Preset] Torture lift_Action judgment_SubState"""
    assert (event_m10_16_x49(z165=10162020, z166=10162021, z167=2600003, z168=2600002, z169=2600001,
            z170=2600000))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_27000():
    """Elevator (former / hidden port)"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_16_x16(z138=10161610, z139=2700010, z140=2700000, z141=10161601, z142=10161600)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_27010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z194=10161610, z195=10161601, z196=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_27020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z194=10161610, z195=10161600, z196=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_28000():
    """Key door that opens with "old keys" """
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z216=1005, z217=1105, z218=50840000, z219=116000055)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_29000():
    """Launching enemies with matryoshka destruction_1"""
    """State 0,2: [Preset] Launch enemy by destroying Matryoshka_SubState"""
    assert event_m10_16_x222(z16=10161700, z17=116020025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_29010():
    """Launching enemies with matryoshka destruction_2"""
    """State 0,2: [Preset] Launch enemy by destroying Matryoshka_SubState"""
    assert event_m10_16_x222(z16=10161701, z17=116020026)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_30000():
    """Open door"""
    """State 0,2: [Preset] Open door_SubState"""
    assert event_m10_16_x226(z15=10160420)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_80000():
    """Rebirth Fire 01_ Prison Stop"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016000, z130=1016099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_81000():
    """Regenerative fire 02_Left room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016100, z130=1016199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_82000():
    """Regenerative fireworks 03_ The broken tower that the outer wall has advanced (hawk warp point)"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016200, z130=1016299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_83000():
    """Reproduction of fire 04_ on the outer wall ahead of the Kanemori area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016300, z130=1016399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_84000():
    """Regeneration of fire 05_after the flame barrel destruction wall"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016400, z130=1016499)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_85000():
    """Rebirth of Fire 06_Refectory after Warrior in Boss Mirror"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016500, z130=1016599)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_87000():
    """Regeneration of fire 08_ outside the tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z129=1016700, z130=1016799)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_87010():
    """Shop lineup expansion_forgotten sinners"""
    """State 0,2: [Lib] [Preset] Shop Lineup_SubState"""
    # bonfire:16685:The Saltfort
    assert event_m10_16_x107(bonfire1=16685, z107=116000086, flag16=101102)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_90000():
    """Trophy_Sinner Light"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_16_x103(flag17=100300, z108=6)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_x0(z229=0, z230=0, z231=10040000, z232=200000):
    """[Lib] Warp between maps after poly play
    z229: Pre-warp poly play ID
    z230: Poly Play ID after Warp
    z231: Map ID
    z232: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z229, z230, z231, z232, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_16_x1(z225=_, z226=_, z227=_, z228=_):
    """[Lib] NPC: Grave Placement: General purpose
    z225: Death map: Global event flag
    z226: Tomb: OBJ instance ID
    z227: Tomb move to: Generator ID
    z228: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z225, 1)
    IsGraveGeneratable(8, z228, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z226, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z226, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_16_x2(z222=_, z223=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z222: Global: death flag
    z223: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z223, 10, 0)
    CompareObjState(1, z223, 20, 0)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        Goto('L0')
    """State 10: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """State 2: Key guide: Key guide display"""
    Label('L0')
    CreateKeyGuideArea(34, 610)
    """State 11: Key guide: Waiting for input"""
    IsObjSearched(0, z223)
    IsPlayerInTheMap(1, 0, 0)
    if ConditionGroup(0):
        """State 3: Key Guide: Use Soul dialog"""
        # action:1211:"[ChrName]\nOffer souls to grave?\nSouls needed: %d"
        DisplayOwnYesNoMenu(1211, 0, 190, 1, GraveSoulsRequired(npc1), NpcParamTextId(npc1))
        assert YesNoMenuDisplay() != 0
        """State 7: Key Guide: Use Soul dialog: Wait for input"""
        if (YesNoMenuResult() == 1) != 0 and (CurrentSouls() > GraveSoulsRequired(npc1)) != 1:
            """State 4: Key guide: Soul shortage dialog"""
            # action:1016:"Insufficient souls"
            DisplayOwnOkMenu(1016, 3, 15, 190, 0, 0, 0)
            assert OkMenuDisplay() != 0
            """State 8: Key guide: Soul shortage dialog: Waiting for input"""
            assert OkMenuDisplay() != 1
        elif (YesNoMenuResult() == 1) != 0:
            """State 9: Key guide: Delete key guide"""
            DeleteKeyGuideArea()
            """State 12: End state"""
            return 0
        elif (YesNoMenuResult() == 2) != 0:
            pass
        elif (YesNoMenuResult() == 3) != 0:
            pass
    elif ConditionGroup(1):
        pass
    """State 6: Key guide: Reset"""
    DeleteKeyGuideArea()
    RestartMachine()
    Quit()

def event_m10_16_x3(z220=_, z221=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z220: Area other flags: Ghost appearance
    z221: Area other flags: Conversation start
    npc1: NPC information parameter ID
    """
    """State 0,5: Appearance of ghost: Player action starts"""
    PlayerActionRequest(6)
    IsPlayerPlayingMotion(0, 6, 1)
    assert ConditionGroup(0)
    """State 6: Ghost appearance: Seoul consumption"""
    AddSouls(-1 * GraveSoulsRequired(npc1))
    """State 7: Appearance of ghost: Waiting for player action"""
    CompareStateTime(0, 4, 2, 4)
    assert ConditionGroup(0)
    """State 1: Ghost appearance: Appearance"""
    SetEventFlag(z220, 1)
    CompareEventFlag(0, z220, 1)
    assert ConditionGroup(0)
    """State 8: Ghost appearance: waiting for completion"""
    CompareStateTime(0, 4, 2, 4)
    assert ConditionGroup(0)
    """State 3: Appearance of ghost: End of player action"""
    EndPlayerActionRequest()
    """State 2: Ghost appearance: Character action waiting"""
    IsPlayerPlayingMotion(0, 6, 0)
    assert ConditionGroup(0)
    """State 9: Ghost appearance: Waiting for conversation"""
    CompareStateTime(0, 2.1, 2, 2.1)
    assert ConditionGroup(0)
    """State 4: Ghost appearance: Conversation start flag"""
    SetEventFlag(z221, 1)
    CompareEventFlag(0, z221, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_16_x4(z220=_, z221=_, z222=_, z223=_, z224=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z220: Ghost Appearance: Area Other Flag
    z221: Conversation start: Area and other flags
    z222: Death: Global event flag
    z223: Tomb: OBJ instance ID
    z224: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z224, 1, 0)
    CompareEventFlag(9, z220, 1)
    CompareObjState(9, z223, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z221, 1)
        CompareEventFlag(0, z221, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_16_x2(z222=z222, z223=z223, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_16_x3(z220=z220, z221=z221, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_16_x5(z216=1005, z217=1105, z218=_, z219=_):
    """[Lib] Item specified door unlocking_2
    z216: Text ID when opened
    z217: Text ID when not opened
    z218: item
    z219: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z218, z216, z217, z219, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x6(z212=0, z213=1101, z214=1700000, z215=116000057):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z212: Text ID when opened
    z213: Text ID when not opened
    z214: Point ID
    z215: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z214, 0, z212, z213, z215, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x7(z204=102481, z205=102482, z206=102483, z207=102485, z208=102490, z209=102486, z210=102487,
                    z211=102488):
    """[Lib] NPC: Woman Knight: Appearance Judgment
    z204: Sub 1 encountering: Global event flag
    z205: During sub-2 encounter: Global event flag
    z206: Sub 3 encountering: Global event flag
    z207: Generation stop: Global event flag
    z208: Appearance permission: Global event flag
    z209: Sub 1 generation stop: Global event flag
    z210: Sub 2 generation stop: Global event flag
    z211: Sub 3 generation stop: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    CompareEventFlag(1, 104190, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Appearance determination: Death determination"""
        CompareEventFlag(0, 104190, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 6: Appearance determination: Generation stop determination"""
            CompareEventFlag(0, z207, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 2: Appearance determination: Judgment while encountering other maps"""
                CompareEventFlag(8, z204, 1)
                CompareEventFlag(8, z209, 0)
                CompareEventFlag(9, z205, 1)
                CompareEventFlag(9, z210, 0)
                CompareEventFlag(10, z206, 1)
                CompareEventFlag(10, z211, 0)
                if ConditionGroup(8):
                    pass
                elif ConditionGroup(9):
                    pass
                elif ConditionGroup(10):
                    pass
                else:
                    """State 8: Appearance determination: Adversity determination"""
                    CompareEventFlag(0, 103692, 1)
                    CompareEventFlag(1, 103693, 1)
                    CompareEventFlag(2, 103691, 1)
                    CompareEventFlag(3, 103694, 1)
                    if ConditionGroup(0):
                        pass
                    elif ConditionGroup(1):
                        pass
                    elif ConditionGroup(2):
                        pass
                    elif ConditionGroup(3):
                        pass
                    else:
                        """State 4: Appearance determination: Appearance allowed"""
                        SetEventFlag(z208, 1)
                        CompareEventFlag(0, z208, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
        """State 3: Appearance judgment: Appearance impossible"""
        SetEventFlag(z208, 0)
        CompareEventFlag(0, z208, 0)
        assert ConditionGroup(0)
    """State 5: Appearance determination: System: Event end"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_16_x8(z202=90, z203=104192):
    """[Lib] NPC: Death determination: General purpose
    z202: Generator ID
    z203: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z203, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z202)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z203, 1)
            CompareEventFlag(0, z203, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_16_x9(flag25=_, z197=_, z198=_, z199=_, z200=_, z201=_, mode8=0):
    """[Lib] [Preset] Boss Battle Start
    flag25: Boss destruction flag
    z197: Start point ID
    z198: End point ID
    z199: Sound ID
    z200: Boss Battle ID
    z201: Other flags for logic
    mode8: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_16_x10(flag25=flag25)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_16_x11(z197=z197, z198=z198)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_16_x12(z199=z199, z200=z200, z201=z201)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_16_x13()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_16_x14(z200=z200)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_16_x15(z199=z199, z200=z200, z201=z201, mode8=mode8)
    """State 7: End state"""
    return 0

def event_m10_16_x10(flag25=_):
    """[Reproduction] Boss Battle_Start
    flag25: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag25) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_16_x11(z197=_, z198=_):
    """[Condition] Boss Battle_Start
    z197: Start point ID
    z198: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z197, z198, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z197, z198, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x12(z199=_, z200=_, z201=_):
    """[Execution] Boss Battle_Start
    z199: Sound ID
    z200: Boss Battle ID
    z201: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z199)
    """State 1: Boss battle start notification"""
    StartBossFight(z200)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z201, 1)
    """State 4: End state"""
    return 0

def event_m10_16_x13():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x14(z200=_):
    """[Condition] Boss Battle_End Judgment
    z200: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z200, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x15(z199=_, z200=_, z201=_, mode8=0):
    """[Execute] Boss Battle_End
    z199: Sound ID
    z200: Boss Battle ID
    z201: Other flags for logic
    mode8: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z201, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z200)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode8) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z199)
    """State 5: End state"""
    return 0

def event_m10_16_x16(z138=_, z139=_, z140=_, z141=_, z142=_):
    """[Lib] [Preset] Elevator
    z138: OBJ instance ID of the elevator
    z139: On elevator point ID_
    z140: Elevator point ID_below
    z141: Upper lever OBJ instance ID
    z142: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_16_x17()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_16_x18(z138=z138, z139=z139, z140=z140, z141=z141, z142=z142)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_16_x66(z138=z138, z140=z140)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_16_x65(z138=z138, z139=z139)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_16_x19(z138=z138, z139=z139)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_16_x20(z138=z138, z140=z140)
    """State 7: End state"""
    return 0

def event_m10_16_x17():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x18(z138=_, z139=_, z140=_, z141=_, z142=_):
    """[Condition] Elevator
    z138: Elevator OBJ instance ID
    z139: On elevator point ID_
    z140: Elevator point ID_below
    z141: Upper lever OBJ instance ID
    z142: Lower lever OBJ instance ID
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
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z140, z140, 1)
        CompareObjState(0, z141, 74, 0)
        CompareObjState(0, z141, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z139, z139, 1)
        CompareObjState(0, z142, 74, 0)
        CompareObjState(0, z142, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_16_x19(z138=_, z139=_):
    """[Execution] Elevator_Rise
    z138: Elevator OBJ instance ID
    z139: On point ID_
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
    """State 3: Switch returns"""
    ChangeObjState(z138, 71)
    assert CompareObjStateId(z138, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_16_x20(z138=_, z140=_):
    """[Execution] Elevator_Descent
    z138: Elevator OBJ instance ID
    z140: Point ID_below
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
    """State 3: Switch returns"""
    ChangeObjState(z138, 81)
    assert CompareObjStateId(z138, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_16_x21(z194=_, z195=_, z196=_):
    """[Lib] [Preset] Elevator lever
    z194: OBJ instance ID of the elevator
    z195: Lever OBJ instance ID
    z196: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_16_x22()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_16_x23(z194=z194, z195=z195, z196=z196)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_16_x24(z194=z194, z195=z195, z196=z196)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_16_x25(z194=z194, z195=z195, z196=z196)
    """State 5: Rerun"""
    return 0

def event_m10_16_x22():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x23(z194=_, z195=_, z196=_):
    """[Condition] Elevator lever_use judgment
    z194: OBJ instance ID of the elevator
    z195: Lever OBJ instance ID
    z196: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z194, z196, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_16_x24(z194=_, z195=_, z196=_):
    """[Execution] Elevator lever_Key guide valid
    z194: OBJ instance ID of the elevator
    z195: Lever OBJ instance ID
    z196: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z195, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z194, z196, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x25(z194=_, z195=_, z196=_):
    """[Execute] Elevator lever_key guide disabled
    z194: OBJ instance ID of the elevator
    z195: Lever OBJ instance ID
    z196: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z195, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z194, z196, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x26(flag24=116000005):
    """[Lib] [Reproduction] Elevator_Initialization
    flag24: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag24) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m10_16_x27():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_16_x28(z191=10161020, z192=40, flag24=116000005, z193=40):
    """[Lib] [Execution] Elevator_Initialization
    z191: Elevator OBJ instance ID
    z192: Initial position OBJ state ID
    flag24: Initialization completion flag
    z193: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z191, z192)
    assert CompareObjStateId(z191, z193, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag24, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x29(z191=10161020, z192=40, flag24=116000005, z193=40):
    """[Lib] [Preset] Elevator_Initialization
    z191: Elevator OBJ instance ID
    z192: Initial position OBJ state ID
    flag24: Initialization completion flag
    z193: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m10_16_x26(flag24=flag24)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m10_16_x27()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m10_16_x28(z191=z191, z192=z192, flag24=flag24, z193=z193)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m10_16_x30(flag23=116000087):
    """[Reproduction] Boss Battle_Poly Play Replay
    flag23: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(flag23) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_16_x31(z186=10160602):
    """[Condition] Boss Battle_Poly Play Replay
    z186: Changed Navimesh of wall 1 to destroy with flame barrel
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z186, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x32(z187=101610, flag23=116000087, z188=1501000, z190=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z187: Poly play ID
    flag23: Poly drama played flag
    z188: Warp point ID
    z190: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z187, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(flag23, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z188)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_16_x33(z186=10160602, z187=101610, flag23=116000087, z188=1501000, z189=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z186: White door instance ID
    z187: Poly play ID
    flag23: Poly drama played flag
    z188: Warp point ID
    z189: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m10_16_x30(flag23=flag23)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m10_16_x31(z186=z186)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m10_16_x32(z187=z187, flag23=flag23, z188=z188, z190=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_16_x34(z181=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z181: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_16_x35(z181=z181)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_16_x39(z181=z181)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_16_x40()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_16_x36(z181=z181, mode7=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_16_x37(z181=z181, z183=38, z184=3, z185=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_16_x38(z181=z181, z182=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_16_x35(z181=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z181: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z181, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z181, 10)
        assert CompareObjStateId(z181, 10, 0)
    elif CompareObjStateId(z181, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z181, 74, 1) and CompareObjStateId(z181, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_16_x36(z181=_, mode7=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z181: Object instance ID
    mode7: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z181)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode7) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_16_x37(z181=_, z183=38, z184=3, z185=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z181: Object instance ID
    z183: Key guide type
    z184: Event action
    z185: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z181, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z181, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z181, 30)
        assert CompareObjStateId(z181, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z181, z183, z184)
        assert PlayerIsInEventAction(z184) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z184, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z181, 74, 0)
        CompareObjState(1, z181, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z185)
            assert CompareObjStateId(z181, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z181, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_16_x38(z181=_, z182=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z181: Object instance ID
    z182: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z181, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_16_x39(z181=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z181: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z181, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x40():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x41(z179=_, val3=_):
    """[Reproduction] Hidden door 1_face SFX
    z179: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z179, 20, 0):
        pass
    else:
        Goto('L0')
    """State 2: Event light reproduction judgment"""
    if (not val3) != 0:
        pass
    else:
        """State 3: Event light ON"""
        SetPointLightEnabled(val3, 1, 0)
    """State 6: Hidden door status judgment"""
    if CompareOwnObjStateId(10, 0):
        """State 7: Hidden door lighting: 30"""
        ChangeOwnObjState(30)
        assert CompareOwnObjStateId(30, 0)
    else:
        pass
    """State 8: Activated"""
    return 0
    """State 5: Event light usage judgment"""
    Label('L0')
    if (not val3) != 0:
        pass
    else:
        """State 4: Event light OFF"""
        SetPointLightEnabled(val3, 0, 0)
    """State 9: Not started"""
    return 1

def event_m10_16_x42(z179=_):
    """[Conditions] Hidden door 1_Face SFX
    z179: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z179, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x43(z179=_, val3=_, z180=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z179: OBJ instance ID of the bug key
    val3: Event light ID
    z180: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,2: Event light usage judgment"""
    if (not val3) != 0:
        """State 5: Wait until face SFX playback"""
        assert (GetStateTime() > val4) != 0
        """State 4: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    else:
        """State 1: Event light ON"""
        SetPointLightEnabled(val3, 1, z180)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_16_x44(z179=_, val3=_, z180=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z179: OBJ instance ID of the bug key
    val3: Event light ID
    z180: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_16_x41(z179=z179, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_16_x42(z179=z179)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_16_x43(z179=z179, val3=val3, z180=z180, val4=val4)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_16_x45(z171=26000, z172=10162020, z173=10162021, z174=30, z175=2600003, z176=2600002, z177=2600001,
                     z178=2600000):
    """[Lib] [Preset] Torture lift
    z171: Initialization event ID
    z172: Reference lift_object instance ID
    z173: Mirror lift_object instance ID
    z174: Safety time
    z175: Reference lift point_on
    z176: Reference lift point_below
    z177: Mirror lift point_on
    z178: Mirror lift point_bottom
    """
    """State 0,2: [Reproduction] Torture lift_operation_SubState"""
    assert event_m10_16_x46(z171=z171)
    """State 3: [Condition] Torture lift_operation_SubState"""
    call = event_m10_16_x47(z172=z172, z173=z173, z175=z175, z176=z176, z177=z177, z178=z178)
    if call.Get() == 0:
        """State 4: [Execution] Torture lift_operation_SubState"""
        assert event_m10_16_x48(z172=z172, z173=z173, z174=z174, z178=z178, z175=z175)
    elif call.Get() == 1:
        """State 5: [Execution] Torture lift_operation_2_SubState"""
        assert event_m10_16_x48(z172=z173, z173=z172, z174=z174, z178=z178, z175=z175)
    """State 1: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_16_x46(z171=26000):
    """[Lib] [Reproduction] Torture lift_operation
    z171: Initialization event ID
    """
    """State 0,2: [Compatible with SEQ17677] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 1: Whether the event has ended"""
    assert EventEnded(z171) != 0
    """State 3: End state"""
    return 0

def event_m10_16_x47(z172=10162020, z173=10162021, z175=2600003, z176=2600002, z177=2600001, z178=2600000):
    """[Lib] [Condition] Torture lift _operation
    z172: Reference lift_object instance ID
    z173: Mirror lift_object instance ID
    z175: Reference lift point_on
    z176: Reference lift point_below
    z177: Mirror lift point_on
    z178: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z172, 32, 0)
    IsPlayerInsidePoint(8, z175, z175, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z172, 33, 0)
    IsPlayerInsidePoint(9, z176, z176, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(1, 9)
    CompareObjState(10, z173, 32, 0)
    IsPlayerInsidePoint(10, z177, z177, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z173, 33, 0)
    IsPlayerInsidePoint(11, z178, z178, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(0, 11)
    if ConditionGroup(0):
        """State 2: Standard is from top to bottom"""
        return 0
    elif ConditionGroup(1):
        """State 3: Mirror from top to bottom"""
        return 1

def event_m10_16_x48(z172=_, z173=_, z174=30, z178=2600000, z175=2600003):
    """[Lib] [execution] torture lift
    z172: Top lift_object instance ID
    z173: Lower lift_object instance ID
    z174: Safety time
    z178: Point start
    z175: End of point
    """
    """State 0,1: Execution"""
    ChangeObjState(z172, 70)
    ChangeObjState(z173, 71)
    """State 2: Waiting for next start"""
    CompareObjState(8, z173, 32, 0)
    CompareObjState(8, z172, 33, 0)
    IsPlayerInsidePoint(8, z178, z175, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    CompareStateTime(1, z174, 3, z174)
    SetConditionGroup(1, 8)
    assert HostConditionGroup(1)
    """State 3: End state"""
    return 0

def event_m10_16_x49(z165=10162020, z166=10162021, z167=2600003, z168=2600002, z169=2600001, z170=2600000):
    """[Lib] [Preset] Torture lift_action judgment
    z165: Reference lift_object instance ID
    z166: Mirror lift_object instance ID
    z167: Reference lift point_on
    z168: Reference lift point_below
    z169: Mirror lift point_on
    z170: Mirror lift point_bottom
    """
    """State 0,1: [Reproduction] Torture lift_action judgment_empty_SubState"""
    assert event_m10_16_x50()
    """State 4: [Condition] Torture lift_Action determination_Start determination_SubState"""
    call = event_m10_16_x51(z165=z165, z166=z166, z167=z167, z168=z168, z169=z169, z170=z170)
    if call.Get() == 1:
        """State 2: [Execution] Torture lift_Action judgment_Action start_SubState"""
        assert event_m10_16_x52(z165=z165)
        """State 7: [Reproduction] Torture lift_action judgment_empty_2_SubState"""
        assert event_m10_16_x50()
        """State 5: [Condition] Torture lift_Action judgment_End judgment_SubState"""
        assert event_m10_16_x53(z165=z165, z167=z167, z168=z168)
        """State 3: [Execution] Torture lift_Action judgment_Action end_SubState"""
        assert event_m10_16_x54(z165=z165, z167=z167, z168=z168)
    elif call.Get() == 0:
        """State 6: [Execution] Torture Lift_Action Judgment_Action Start_2_SubState"""
        assert event_m10_16_x52(z165=z166)
        """State 8: [Reproduction] Torture lift_Action judgment_Empty_3_SubState"""
        assert event_m10_16_x50()
        """State 10: [Condition] Torture lift_Action judgment_End judgment_2_SubState"""
        assert event_m10_16_x53(z165=z166, z167=z169, z168=z170)
        """State 9: [Execution] Torture lift_Action judgment_Action end_2_SubState"""
        assert event_m10_16_x54(z165=z166, z167=z169, z168=z170)
    """State 11: End state"""
    return 0

def event_m10_16_x50():
    """[Lib] [reproduction] Torture lift_action judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x51(z165=10162020, z166=10162021, z167=2600003, z168=2600002, z169=2600001, z170=2600000):
    """[Lib] [Condition] Torture lift_Action judgment_Start judgment
    z165: Reference lift_object instance ID
    z166: Mirror lift_object instance ID
    z167: Reference lift point_on
    z168: Reference lift point_below
    z169: Mirror lift point_on
    z170: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z165, 70, 0)
    IsPlayerInsidePoint(8, z167, z167, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z165, 71, 0)
    IsPlayerInsidePoint(9, z168, z168, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(0, 9)
    CompareObjState(10, z166, 70, 0)
    IsPlayerInsidePoint(10, z169, z169, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z166, 71, 0)
    IsPlayerInsidePoint(11, z170, z170, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(1, 11)
    if ConditionGroup(0):
        """State 3: Standard"""
        return 1
    elif ConditionGroup(1):
        """State 2: mirror"""
        return 0

def event_m10_16_x52(z165=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action start
    z165: Lift_object instance ID
    """
    """State 0,1: Action request"""
    ObjAnimationPlayerControlRequest(z165, 34, 10)
    """State 2: End state"""
    return 0

def event_m10_16_x53(z165=_, z167=_, z168=_):
    """[Lib] [Condition] Torture lift_Action judgment_End judgment
    z165: Lift_object instance ID
    z167: Lift point_on
    z168: Lift point_down
    """
    """State 0,1: Wait"""
    CompareObjState(8, z165, 32, 0)
    CompareObjState(9, z165, 33, 0)
    SetConditionGroup(0, 8)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Finish"""
    return 0

def event_m10_16_x54(z165=_, z167=_, z168=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action end
    z165: Lift_object instance ID
    z167: Lift point_on
    z168: Lift point_down
    """
    """State 0,1: Action request"""
    EndPlayerActionRequest()
    """State 2: Wait"""
    IsPlayerInsidePoint(0, z167, z167, 1)
    IsPlayerInsidePoint(0, z168, z168, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x55():
    """[Lib] [Reproduction] OBJ attach_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x56():
    """[Lib] [Condition] OBJ attach_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x57(z162=10162000, z163=150, z164=10166490):
    """[Lib] [execute] OBJ attach
    z162: Parent OBJ instance ID
    z163: Parent Damipoli ID
    z164: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z162, z163, z164)
    """State 2: End state"""
    return 0

def event_m10_16_x58(z162=10162000, z163=150, z164=10166490):
    """[Lib] [Preset] OBJ attach
    z162: Parent OBJ instance ID
    z163: Parent Damipoli ID
    z164: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m10_16_x55()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m10_16_x56()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m10_16_x57(z162=z162, z163=z163, z164=z164)
    """State 4: End state"""
    return 0

def event_m10_16_x59(z154=_, z155=_, z156=15, z157=_, z158=_, z159=1600, z160=_, z161=_):
    """[Lib] Character: Petrochemical: Key guide
    z154: generator
    z155: Death: Global event flag
    z156: Event action
    z157: Petrified: Area and other flags
    z158: Petrified: Global event flag
    z159: Key guide parameters
    z160: Petrification start state ID
    z161: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z154, z160, 0)
    CompareEventStatus(8, z161, 1, 0)
    CompareEventFlag(2, z157, 1)
    CompareEventFlag(3, z158, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(2):
        pass
    elif ConditionGroup(3):
        pass
    elif ConditionGroup(8):
        Goto('L0')
    else:
        pass
    """State 17: End state"""
    return 0
    """State 2: Petrochemical: Key guide: Display"""
    Label('L0')
    CreateKeyGuideArea(34, z159)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z154)
    IsPlayerInTheMap(1, 0, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 5: Petrification: Key guide: Deleted"""
        DeleteKeyGuideArea()
        # goods:60537000:Fragrant Branch of Yore
        if (ItemCount(60537000, 1, 1, 0) > 1) != 1:
            """State 12: Petrification: Item not owned dialog"""
            # action:1017:"A statue blocks your way"
            DisplayOwnOkMenu(1017, 3, 15, 220, 2, 0, 0)
            assert OkMenuDisplay() != 0
            """State 13: Petrochemical: Item not owned dialog: Waiting for input"""
            assert OkMenuDisplay() != 1
        else:
            """State 10: Petrochemical: Item usage selection dialog"""
            # action:1002:"Use %s?", goods:60537000:Fragrant Branch of Yore
            DisplayOwnYesNoMenu(1002, 3, 220, 2, 60537000, 0)
            assert YesNoMenuDisplay() != 0
            """State 11: Petrochemical: Item usage selection dialog: Waiting for input"""
            if (YesNoMenuResult() == 3) != 0:
                pass
            elif (YesNoMenuResult() == 2) != 0:
                pass
            elif (YesNoMenuResult() == 1) != 0:
                """State 15,14: Petrochemical: Event action: Start"""
                DoesPlayerEventAction(0, 1)
                assert ConditionGroup(0)
                """State 6: Petrification: Event action: Regeneration"""
                PlayerActionRequest(z156)
                IsPlayerPlayingMotion(0, z156, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z157, 1)
                CompareEventFlag(0, z157, 1)
                SetEventFlag(z158, 1)
                CompareEventFlag(1, z158, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z156, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()
    Quit()

def event_m10_16_x60(z149=_, z150=20, z151=_, z152=0, z153=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z149: Object instance ID
    z150: OBJ state ID
    z151: Navimesh switching point ID
    z152: Additional attributes
    z153: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_16_x61(z149=z149, z150=z150, z151=z151, z153=z153, z152=z152)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_16_x62(z149=z149, z150=z150, z151=z151)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_16_x63(z149=z149, z150=z150, z151=z151, z152=z152, z153=z153)
    """State 4: End state"""
    return 0

def event_m10_16_x61(z149=_, z150=20, z151=_, z153=2, z152=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z149: Target OBJ instance ID
    z150: Target OBJ state ID
    z151: Navimesh switching point ID
    z153: Additional attributes
    z152: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z149, z150, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z151, z153)
        DeleteNavimeshAttribute(z151, z152)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_16_x62(z149=_, z150=20, z151=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z149: Target OBJ instance ID
    z150: Target OBJ state ID
    z151: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z149, z150, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x63(z149=_, z150=20, z151=_, z152=0, z153=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z149: Target OBJ instance ID
    z150: Target OBJ state ID
    z151: Navimesh switching point ID
    z152: Additional attributes
    z153: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z151, z152)
    DeleteNavimeshAttribute(z151, z153)
    """State 2: End state"""
    return 0

def event_m10_16_x64(z143=102500, z144=546, z145=104190, z146=61, z147=103690, z148=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z143: White Phantom can appear: Global event flag
    z144: White Phantom: Generator ID
    z145: Death: Global event flag
    z146: Body: Generator group ID
    z147: Hostile: Global event flag
    z148: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z144)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z145, 1)
        CompareEventFlag(1, z147, 1)
        CompareEventFlag(2, z143, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z144)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z145, 1)
            CompareEventFlag(1, z147, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z144)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z145, 1)
            CompareEventFlag(1, z147, 1)
            HasNpcPhantomSpawned(2, z144, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z146, 0)
                HasNpcPhantomSpawned(0, z144, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z144)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_16_x65(z138=_, z139=_):
    """[Execution] Elevator_Return switch after lift
    z138: Elevator OBJ instance ID
    z139: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z138, 30, 0)
    IsPlayerInsidePoint(8, z139, z139, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z138, 71)
    assert CompareObjStateId(z138, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_16_x66(z138=_, z140=_):
    """[Execution] Elevator_Return switch after descending
    z138: Elevator OBJ instance ID
    z140: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z138, 41, 0)
    IsPlayerInsidePoint(8, z140, z140, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z138, 81)
    assert CompareObjStateId(z138, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_16_x67(z132=_, z133=_, z134=_, z135=_, z136=0, z137=_):
    """[Lib] Character: Petrified: Appearance setting
    z132: Generator ID
    z133: Death: Global event flag
    z134: Petrified: Area and other flags
    z135: Petrified: Global event flag
    z136: Startup state
    z137: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z132)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z133, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z134, 1)
                CompareEventFlag(1, z135, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z132, z136)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_16_x68(z131=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z131: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z131)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_16_x69():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x70(z129=_, z130=_):
    """[Lib] [execute] Rebirth fire
    z129: Flag start ID
    z130: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z129, z130, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x71():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x72(z129=_, z130=_):
    """[Lib] [Preset] Rebirth
    z129: Flag start ID
    z130: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_16_x69()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_16_x71()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_16_x70(z129=z129, z130=z130)
    """State 4: End state"""
    return 0

def event_m10_16_x73(z125=116000086, z126=102498, z127=204, z128=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z125: Defeat Boss 1: Area and other flags
    z126: Summon Achievement: Global Event Flag
    z127: Summon achievement count: global variable
    z128: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z126, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z125, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z127, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z127, NpcInfoValue(z128, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z126, 1)
                CompareEventFlag(0, z126, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_16_x74(flag21=_, flag22=_, z124=2, z123=0, z122=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    flag21: Other flags
    flag22: Global flag
    z124: Additional attributes
    z123: Delete attribute
    z122: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(flag21) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(flag22) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z122, z124)
        DeleteNavimeshAttribute(z122, z123)
        """State 3: Flag OFF"""
        return 0

def event_m10_16_x75(flag21=_, flag22=_):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    flag21: Other flags
    flag22: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, flag21, 1)
    CompareEventFlag(0, flag22, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_16_x76(z122=_, z123=0, z124=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z122: Navimesh switching point ID
    z123: Additional attributes
    z124: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z122, z123)
    DeleteNavimeshAttribute(z122, z124)
    """State 2: End state"""
    return 0

def event_m10_16_x77(z122=_, z123=0, z124=2, flag21=_, flag22=_):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z122: Navimesh switching point ID
    z123: Additional attributes
    z124: Delete attribute
    flag21: Other flags
    flag22: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_16_x74(flag21=flag21, flag22=flag22, z124=z124, z123=z123, z122=z122)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_16_x75(flag21=flag21, flag22=flag22)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_16_x76(z122=z122, z123=z123, z124=z124)
    """State 4: End state"""
    return 0

def event_m10_16_x78(z118=10002000, z119=540, z120=0, z121=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z118: Summon range
    z119: Generator ID
    z120: Appearance: Minimum time
    z121: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z118, z118, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z120, 3, z121)
        IsPlayerInsidePoint(1, z118, z118, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z119)
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

def event_m10_16_x79(z114=10001000, z115=541, z116=0, z117=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z114: Summon range
    z115: Generator ID
    z116: Appearance: Minimum time
    z117: Appearance: Maximum time
    """
    """State 0,10: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Black Phantom Appearance: Online"""
        IsOffline(0, 0)
        if ConditionGroup(0):
            """State 9: Black Phantom Appearance: Sign removed"""
            DeleteNpcPhantom(z115)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z114, z114, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z116, 3, z117)
                IsPlayerInsidePoint(1, z114, z114, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z115)
                    Goto('L0')
                elif ConditionGroup(1):
                    pass
                elif ConditionGroup(2):
                    pass
            elif ConditionGroup(0):
                pass
        """State 6: Black Phantom Appearance: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 4: Black Phantom Appearance: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_16_x80(flag20=_, z113=_):
    """[Lib] [Preset] Get trophy
    flag20: Acquisition trigger_other flags
    z113: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag20) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag20, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z113)
    """State 4: End state"""
    return 0

def event_m10_16_x81(flag19=100300):
    """[Lib] [Reproduction] Terminal Lighthouse
    flag19: Lighting completion flag
    """
    """State 0,1: Is it already lit?"""
    if GetEventFlag(flag19) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_16_x82(z112=10162200):
    """[Lib] [Conditions] Terminal lighthouse
    z112: Lighthouse OBJ instance ID
    """
    """State 0,1: Waiting for lighting"""
    CompareObjState(0, z112, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x83(z112=10162200, action1=2022, flag19=100300):
    """[Lib] [execution] terminal lighthouse
    z112: Lighthouse OBJ instance ID
    action1: Text ID
    flag19: Lighting completion flag
    """
    """State 0,1: Production FE display"""
    OpenPresentationWindow(20)
    """State 4,2: Event message display"""
    # action:2022:"A primal bonfire was rekindled"
    DisplayEventMessage(action1, 0, 0, 0)
    """State 3: Lighting completion flag ON"""
    SetEventFlag(flag19, 1)
    """State 5: End state"""
    return 0

def event_m10_16_x84(z112=10162200, action1=2022, flag19=100300):
    """[Lib] [Preset] Terminal Lighthouse
    z112: Lighthouse OBJ instance ID
    action1: Text ID
    flag19: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] Terminal Lighthouse_SubState"""
    call = event_m10_16_x81(flag19=flag19)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Terminal lighthouse_SubState"""
        assert event_m10_16_x82(z112=z112)
        """State 2: [Lib] [Execution] Terminal Lighthouse_SubState"""
        assert event_m10_16_x83(z112=z112, action1=action1, flag19=flag19)
    """State 4: End state"""
    return 0

def event_m10_16_x85(z111=12000, mode4=1, mode5=1, mode6=1):
    """[Lib] [Preset] Kanemori_Net reception
    z111: Event sound ID for bell
    mode4: Wait 1 after SE playback
    mode5: Wait 2 after SE playback
    mode6: Wait 3 after playing SE
    """
    """State 0,1: [Lib] [Reproduction] Kanemori_Net reception_SubState"""
    assert event_m10_16_x86()
    """State 3: [Lib] [Conditions] Kanemori_Net reception_SubState"""
    assert event_m10_16_x87()
    """State 2: [Lib] [Execution] Kanemori_Net reception_SubState"""
    assert event_m10_16_x88(z111=z111, mode4=mode4, mode5=mode5, mode6=mode6)
    """State 4: End state"""
    return 0

def event_m10_16_x86():
    """[Lib] [Reproduction] Kanemori_Net reception"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x87():
    """[Lib] [Conditions] Kanemori_Net reception"""
    """State 0,1: Waiting for reception: If a host dies in a multiplayer, it will not be played back"""
    IsBellKeeperRingingHistoryCleared(8, 1)
    IsHostDead(8, 0)
    IsBellKeeperRingingHistoryCleared(9, 1)
    IsHostDead(9, 1)
    IsMultiplayer(9, 1, 0)
    if ConditionGroup(9):
        """State 2: Have you finished multiplayer?"""
        IsMultiplayer(0, 0, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        pass
    """State 3: Reception: Bell ringing process"""
    return 0

def event_m10_16_x88(z111=12000, mode4=1, mode5=1, mode6=1):
    """[Lib] [Execution] Kanemori_Net reception_Playback
    z111: Event sound ID for bell
    mode4: Wait 1 after SE playback
    mode5: Wait 2 after SE playback
    mode6: Wait 3 after playing SE
    """
    """State 0,1: Ring the bell: first time"""
    PlaySoundAtPoint(z111)
    assert (GetStateTime() > mode4) != 0
    """State 4: Ring the bell: second time"""
    PlaySoundAtPoint(z111)
    assert (GetStateTime() > mode5) != 0
    """State 5: Ring the bell: 3rd time"""
    PlaySoundAtPoint(z111)
    assert (GetStateTime() > mode6) != 0
    """State 2: Clear reception history"""
    ClearBellKeeperRingingHistory()
    """State 3: Clear confirmation of received history"""
    IsBellKeeperRingingHistoryCleared(0, 0)
    assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_16_x89(z110=10161023):
    """[Lib] [reproduction] Kanemori _ judgment of lever use of Kanemori spirit
    z110: Lever OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 4: Host: Exit"""
        return 1
    else:
        """State 2: Disable key guide"""
        DisableObjKeyGuide(z110, 1)
        """State 3: Guest: Spirit guard"""
        return 0

def event_m10_16_x90():
    """[Lib] [Conditions] Kanemori _ Judgment spirit lever usage judgment"""
    """State 0,1: Has the host died?"""
    IsHostDead(0, 1)
    assert ConditionGroup(0)
    """State 2: Bell guard spirit: lever operation possible"""
    return 0

def event_m10_16_x91(z110=10161023):
    """[Lib] [Execution] Kanemori _ Judgment Spirit use lever judgment
    z110: Lever OBJ instance ID
    """
    """State 0,1: Activate key guide"""
    DisableObjKeyGuide(z110, 0)
    """State 2: Finish"""
    return 0

def event_m10_16_x92(z110=10161023):
    """[Lib] [Preset] Kanemori _ Judgment Spirit's lever usage judgment
    z110: Lever OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] Kanemori _ Jerusalem Spirit Lever Use Judgment_SubState"""
    call = event_m10_16_x89(z110=z110)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Conditions] Kanemori_Bellguard spirit lever usage judgment_SubState"""
        assert event_m10_16_x90()
        """State 2: [Lib] [Execution] Kanemori_Legend of lever guard_SubState"""
        assert event_m10_16_x91(z110=z110)
    """State 4: Finish"""
    return 0

def event_m10_16_x93(z100=10161023, z101=10161050, mode3=0, z102=0, z103=0, z104=10161051, z105=10160620,
                     z106=400000):
    """[Lib] [Preset] Bell guard_bell lever
    z100: Lever_OBJ instance ID
    z101: Bell 1_OBJ instance ID
    mode3: Bell 2_OBJ instance ID
    z102: Bell 3_OBJ instance ID
    z103: Bell 4_OBJ instance ID
    z104: Door OBJ instance ID
    z105: Changed Navimesh of wall 1 to destroy with flame barrel
    z106: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Bell guard_Lever that bell rings_SubState"""
    call = event_m10_16_x94(z104=z104, z105=z105, z106=z106)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        Goto('L0')
    """State 3: [Lib] [Conditions] Bell guard_Lever that rings bell_SubState"""
    call = event_m10_16_x95(z100=z100)
    if call.Get() == 0:
        """State 4: [Lib] [execution] bell guard_bell lever_host_SubState"""
        assert (event_m10_16_x96(z100=z100, z101=z101, mode3=mode3, z102=z102, z103=z103, z104=z104,
                z105=z105, z106=z106))
    elif call.Get() == 1:
        """State 2: [Lib] [execution] bell guard_bell lever_guest_SubState"""
        assert event_m10_16_x97(z100=z100, z101=z101, mode3=mode3, z102=z102, z103=z103)
    """State 7: Rerun"""
    return 0
    """State 6: [Lib] [Conditions] Bell guard_Lever that rings bell_Guest_SubState"""
    Label('L0')
    assert event_m10_16_x108(z104=z104)
    """State 5: [Lib] [Execution] Bell guard_Lever that bell rings_Navigation change_SubState"""
    assert event_m10_16_x109(z104=z104, z106=z106)
    """State 8: Guest termination"""
    return 1

def event_m10_16_x94(z104=10161051, z105=10160620, z106=400000):
    """[Lib] [reproduction] bell guard _ bell ringing lever
    z104: Door OBJ instance ID
    z105: Changed Navimesh of wall 1 to destroy with flame barrel
    z106: Navigation change point ID
    """
    """State 0,3: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is the door open?"""
    if CompareObjStateId(z104, 10, 0):
        """State 2: White door key guide disabled"""
        DisableWhiteDoorKeyGuide(z105, 1)
    else:
        """State 4: Navimesh change: passable"""
        DeleteNavimeshAttribute(z106, 2)
    """State 5: host"""
    return 0
    """State 6: Guest termination"""
    Label('L0')
    return 1

def event_m10_16_x95(z100=10161023):
    """[Lib] [Conditions] Bell guard_bell lever
    z100: OBJ instance ID of the lever
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z100, 74, 0)
    CompareObjState(0, z100, 84, 0)
    SetConditionGroup(8, 0)
    IsHostDead(8, 0)
    CompareObjState(1, z100, 74, 0)
    CompareObjState(1, z100, 84, 0)
    SetConditionGroup(9, 1)
    IsHostDead(9, 1)
    if ConditionGroup(8):
        """State 2: Host is alive: Host processing"""
        return 0
    elif ConditionGroup(9):
        """State 3: Host dies: guest processing"""
        return 1

def event_m10_16_x96(z100=10161023, z101=10161050, mode3=0, z102=0, z103=0, z104=10161051, z105=10160620,
                     z106=400000):
    """[Lib] [Execution] Kanemori_Lever that rings the bell_Host
    z100: Lever_OBJ instance ID
    z101: Bell 1_OBJ instance ID
    mode3: Bell 2_OBJ instance ID
    z102: Bell 3_OBJ instance ID
    z103: Bell 4_OBJ instance ID
    z104: Door OBJ instance ID
    z105: Changed Navimesh of wall 1 to destroy with flame barrel
    z106: Navigation change point ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z100, 1)
    """State 9: Ringing bell judgment"""
    if (not mode3) != 0:
        """State 10: Ring bell 1"""
        ChangeObjState(z101, 70)
        """State 8: Bell 1 animation playback judgment"""
        CompareObjState(0, z101, 70, 0)
        assert ConditionGroup(0)
        """State 4: Bell 1 animation end"""
        CompareObjState(0, z101, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z101, 70)
        ChangeObjState(mode3, 70)
        ChangeObjState(z102, 70)
        ChangeObjState(z103, 70)
        """State 11: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z101, 70, 0)
        CompareObjState(0, mode3, 70, 0)
        CompareObjState(0, z102, 70, 0)
        CompareObjState(0, z103, 70, 0)
        assert ConditionGroup(0)
        """State 12: Bell 1 ~ 4 anime end judgment"""
        CompareObjState(8, z101, 10, 0)
        CompareObjState(8, mode3, 10, 0)
        CompareObjState(8, z102, 10, 0)
        CompareObjState(8, z103, 10, 0)
        assert ConditionGroup(8)
    """State 5: Judgment of door"""
    CompareObjState(0, z104, 10, 0)
    CompareObjState(1, z104, 10, 1)
    if ConditionGroup(0):
        """State 6: Open the door: 70"""
        ChangeObjState(z104, 70)
        """State 7: Door animation end judgment"""
        CompareObjState(0, z104, 20, 0)
        assert ConditionGroup(0)
        """State 14: Navimesh change: passable"""
        DeleteNavimeshAttribute(z106, 2)
        """State 13: Enable key guide for white door"""
        DisableWhiteDoorKeyGuide(z105, 0)
    elif ConditionGroup(1):
        pass
    """State 3: Lever key guide enabled"""
    DisableObjKeyGuide(z100, 0)
    """State 15: End state"""
    return 0

def event_m10_16_x97(z100=10161023, z101=10161050, mode3=0, z102=0, z103=0):
    """[Lib] [execution] Kanemori _ Lever singing bell _ Guest
    z100: Lever_OBJ instance ID
    z101: Bell 1_OBJ instance ID
    mode3: Bell 2_OBJ instance ID
    z102: Bell 3_OBJ instance ID
    z103: Bell 4_OBJ instance ID
    """
    """State 0,5: Ringing bell judgment"""
    if (not mode3) != 0:
        """State 6: Ring bell 1"""
        ChangeObjState(z101, 70)
        """State 3: Ringing the bell_server information"""
        NotifyServerOfBellKeeperRinging()
        """State 4: Bell 1 animation playback judgment"""
        CompareObjState(0, z101, 70, 0)
        assert ConditionGroup(0)
        """State 2: Bell 1 animation end"""
        CompareObjState(0, z101, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z101, 70)
        ChangeObjState(mode3, 70)
        ChangeObjState(z102, 70)
        ChangeObjState(z103, 70)
        """State 8: Bell ringing_server information transmission_2"""
        NotifyServerOfBellKeeperRinging()
        """State 9: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z101, 70, 0)
        CompareObjState(0, mode3, 70, 0)
        CompareObjState(0, z102, 70, 0)
        CompareObjState(0, z103, 70, 0)
        assert ConditionGroup(0)
        """State 7: Anime end judgment for bells 1 to 4_2"""
        CompareObjState(8, z101, 10, 0)
        CompareObjState(8, mode3, 10, 0)
        CompareObjState(8, z102, 10, 0)
        CompareObjState(8, z103, 10, 0)
        assert ConditionGroup(8)
    """State 10: End state"""
    return 0

def event_m10_16_x98(flag18=100300):
    """[Lib] [Reproduction] Special bonfire at the end
    flag18: Lighting completion flag
    """
    """State 0,1: Is the bonfire already lit?"""
    if GetEventFlag(flag18) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_16_x99(z109=10162200):
    """[Lib] [Condition] Terminal special fire
    z109: Bonfire OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z109)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x100(z109=10162200, flag18=100300):
    """[Lib] [Execution] End special bonfire_ignition
    z109: Bonfire OBJ instance ID
    flag18: Lighting completion flag
    """
    """State 0,6: Bonfire light action"""
    PlayerActionRequest(5)
    assert PlayerIsInEventAction(5) != 0
    """State 7: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 5, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 5: Bonfire ignition"""
        ChangeObjState(z109, 70)
        """State 3: Lighting completion flag ON"""
        SetEventFlag(flag18, 1)
        """State 1: Production FE display"""
        OpenPresentationWindow(20)
        assert PresentationWindowDisplay() != 0
        """State 4: Waiting for non-display of production FE"""
        assert PresentationWindowDisplay() != 1
        """State 2: Event message display"""
        # action:2022:"A primal bonfire was rekindled"
        DisplayEventMessage(2022, 0, 0, 0)
        assert EventMessageDisplay() != 0
    """State 8: End state"""
    return 0

def event_m10_16_x101(z109=10162200, flag18=100300):
    """[Lib] [Execution] End special bonfire_warp
    z109: Bonfire OBJ instance ID
    flag18: Lighting completion flag
    """
    """State 0,1: Warp PC action"""
    PlayerActionRequest(6)
    assert PlayerIsInEventAction(6) != 0
    """State 2: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 6, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Warp SFX playback PC invincible"""
        PlaySfxSelfGenerated(8002, 239, 200)
        SetPlayerInvincible(1)
        assert (GetStateTime() > 2.5) != 0
        """State 5: [Lib] Warp between maps after poly play_SubState"""
        assert event_m10_16_x0(z229=0, z230=0, z231=10040000, z232=200000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m10_16_x102(z109=10162200, flag18=100300):
    """[Lib] [Preset] Special bonfire at the end
    z109: Bonfire OBJ instance ID
    flag18: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] End special bonfire _SubState"""
    call = event_m10_16_x98(flag18=flag18)
    if call.Get() == 1:
        """State 5: [Lib] [Condition] End special bonfire_2_SubState"""
        assert event_m10_16_x99(z109=z109)
        """State 2: [Lib] [Execution] End special bonfire_warp_SubState"""
        assert event_m10_16_x101(z109=z109, flag18=flag18)
    elif call.Get() == 0:
        """State 4: [Lib] [Condition] End special bonfire_SubState"""
        assert event_m10_16_x99(z109=z109)
        """State 3: [Lib] [Execution] End special bonfire_At ignition_SubState"""
        assert event_m10_16_x100(z109=z109, flag18=flag18)
    """State 6: Rerun"""
    return 0

def event_m10_16_x103(flag17=100300, z108=6):
    """[Lib] [Preset] Trophy Acquisition_Global
    flag17: Acquisition trigger_global flag
    z108: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag17) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag17, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z108)
    """State 4: End state"""
    return 0

def event_m10_16_x104(flag16=101102):
    """[Lib] [Reproduction] Shop Lineup
    flag16: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(flag16) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m10_16_x105(bonfire1=16685, z107=116000086):
    """[Lib] [Conditions] Shop lineup
    bonfire1: Bonfire ID
    z107: Boss destruction flag
    """
    """State 0,1: Is the total number of laps 2 or more and is the boss destroyed?"""
    # bonfire:16685:The Saltfort
    CompareGameCycleForBonfire(8, bonfire1, 2, 2, 3)
    CompareEventFlag(8, z107, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_16_x106(flag16=101102):
    """[Lib] [execution] shop lineup
    flag16: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(flag16, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x107(bonfire1=16685, z107=116000086, flag16=101102):
    """[Lib] [Preset] Shop Lineup
    bonfire1: Bonfire ID
    z107: Boss destruction flag
    flag16: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_16_x104(flag16=flag16)
    if call.Get() == 0:
        """State 3: [Lib] [Conditions] Shop lineup_SubState"""
        assert event_m10_16_x105(bonfire1=bonfire1, z107=z107)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_16_x106(flag16=flag16)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_16_x108(z104=10161051):
    """[Lib] [Conditions] Kanemori _ Lever that rings the bell _ Guest
    z104: Door OBJ instance ID
    """
    """State 0,1: Waiting for the door to open"""
    CompareObjState(0, z104, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x109(z104=10161051, z106=400000):
    """[Lib] [execution] bell guard_bell change lever_navigation change
    z104: Door OBJ instance ID
    z106: Navigation change point ID
    """
    """State 0,1: Navimesh change: passable"""
    DeleteNavimeshAttribute(z106, 2)
    """State 2: End state"""
    return 0

def event_m10_16_x110(flag15=_, z97=_, z98=_, z99=_):
    """[Lib] [Reproduction] Elevator_Initialization_Relief
    flag15: Initialization completion flag
    z97: Elevator OBJ instance ID
    z98: Initial position OBJ state ID
    z99: OBJ state after initialization
    """
    """State 0,4: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 1: Already initialized?"""
    if GetEventFlag(flag15) != 0:
        pass
    else:
        Goto('L0')
    """State 2: [Remedy] Is it in the initial state?"""
    if CompareObjStateId(z97, 10, 0):
        """State 3: Elevator initialization"""
        ChangeObjState(z97, z98)
        assert CompareObjStateId(z97, z99, 0)
        """State 8: Relief flow"""
        return 3
    else:
        """State 6: Initialized"""
        return 1
    """State 5: Uninitialized"""
    Label('L0')
    return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_16_x111():
    """[Lib] [Condition] Elevator_Initialization_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x112(z97=_, z98=_, flag15=_, z99=_):
    """[Lib] [Run] Elevator_Initialization_Relief
    z97: Elevator OBJ instance ID
    z98: Initial position OBJ state ID
    flag15: Initialization completion flag
    z99: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z97, z98)
    assert CompareObjStateId(z97, z99, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag15, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x113(z97=_, z98=_, flag15=_, z99=_):
    """[Lib] [Preset] Elevator_Initialization_Relief
    z97: Elevator OBJ instance ID
    z98: Initial position OBJ state ID
    flag15: Initialization completion flag
    z99: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_Relief_SubState"""
    call = event_m10_16_x110(flag15=flag15, z97=z97, z98=z98, z99=z99)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 3:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_Empty_SubState"""
        assert event_m10_16_x111()
        """State 2: [Lib] [Execution] Elevator_Initialization_Relief_SubState"""
        assert event_m10_16_x112(z97=z97, z98=z98, flag15=flag15, z99=z99)
    """State 4: End state"""
    return 0

def event_m10_16_x114(z90=10162210):
    """[Lib] [BEST] [Condition] Andyel_Appearance_Termination
    z90: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z90)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x115(z90=10162210, flag14=100761, flag13=100742):
    """[Lib] [BEST] [Execution] Andyel_Appearance_Termination
    z90: Ander OBJ instance ID
    flag14: Conversation start flag
    flag13: Encounter flag
    """
    """State 0,4: Bonfire light action"""
    PlayerActionRequest(5)
    assert PlayerIsInEventAction(5) != 0
    """State 5: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 5, 0)
    if ConditionGroup(1):
        """State 8: Rerun"""
        return 1
    elif ConditionGroup(0):
        """State 6: Andel encounter flag ON"""
        SetEventFlag(flag13, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z90, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z90, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(flag14, 1)
        """State 7: End state"""
        return 0

def event_m10_16_x116(flag12=100740):
    """[Lib] [BEST] [Conditions] Ander_Destruction_End_Termination
    flag12: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, flag12, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x117(z90=10162210):
    """[Lib] [BEST] [Execution] Andel_Deletion_End
    z90: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z90, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z90, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x118(z90=10162210, flag12=100740, flag14=100761, flag13=100742):
    """[Lib] [BEST] [Reproduction] Anderl_Appearance determination_Termination
    z90: Ander OBJ instance ID
    flag12: Event completion flag
    flag14: Conversation start flag
    flag13: Encounter flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been completed?"""
        if GetEventFlag(flag12) != 0:
            pass
        else:
            """State 3: Was it in conversation?"""
            if GetEventFlag(flag14) != 0:
                pass
            else:
                """State 4: Was it in the middle of appearance?"""
                if CompareObjStateId(z90, 72, 0):
                    pass
                elif CompareObjStateId(z90, 73, 0):
                    pass
                elif CompareObjStateId(z90, 70, 0):
                    pass
                elif CompareObjStateId(z90, 30, 0):
                    pass
                else:
                    """State 7: Was the appearance confirmed?"""
                    if GetEventFlag(flag13) != 0:
                        """State 8: Standby state: 30"""
                        ChangeObjState(z90, 30)
                    else:
                        """State 11: Appearance determination"""
                        return 2
                """State 5: Wait for completion"""
                assert CompareObjStateId(z90, 30, 0)
                """State 6: Conversation start flag ON"""
                SetEventFlag(flag14, 1)
            """State 10: Disappearance judgment"""
            return 1
    """State 9: Finish"""
    return 0

def event_m10_16_x119():
    """[Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x120(z90=10162210, flag12=100740, flag13=100742, flag14=100761, z91=100300, z92=100360,
                      z93=100400, z94=100461):
    """[Lib] [BEST] [Preset] Andyel_Termination
    z90: Ander OBJ instance ID
    flag12: Event completion flag
    flag13: Encounter flag
    flag14: Conversation start flag
    z91: Lighting completion flag
    z92: Bonfire lighting judgment flag ①
    z93: Bonfire lighting judgment flag ②
    z94: Bonfire lighting judgment flag ③
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Ander _ Appearance determination _ Termination _ SubState"""
    call = event_m10_16_x118(z90=z90, flag12=flag12, flag14=flag14, flag13=flag13)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty _ SubState"""
        Label('L0')
        assert event_m10_16_x119()
        """State 9: [Lib] [BEST] [Conditions] Ander_Deletion_Termination_Termination_SubState"""
        assert event_m10_16_x116(flag12=flag12)
        """State 6: [Lib] [BEST] [Execution] Andel_Destruction_End_SubState"""
        assert event_m10_16_x117(z90=z90)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Ander_Appearance determination_Termination_SubState"""
        call = event_m10_16_x127(z90=z90, z91=z91, z92=z92, z93=z93, z94=z94, flag13=flag13)
        if call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Andel_Appearance determination_Termination_SubState"""
            assert event_m10_16_x128(z90=z90)
            """State 1: [Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty_SubState"""
            assert event_m10_16_x126()
            """State 7: [Lib] [BEST] [Condition] Ander_Appearance_Termination_SubState"""
            assert event_m10_16_x114(z90=z90)
            """State 4: [Lib] [BEST] [Execution] Andel_Appearance_Termination_SubState"""
            call = event_m10_16_x115(z90=z90, flag14=flag14, flag13=flag13)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                Goto('L0')
        elif call.Get() == 1:
            pass
        """State 11: Rerun"""
        return 1
    """State 10: Finish"""
    return 0

def event_m10_16_x121(z95=10162210, z96=10162200):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z95, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z96, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_16_x122(z95=10162210):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z95: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z95, 10, 0)
    CompareObjState(0, z95, 31, 0)
    CompareObjState(0, z95, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_16_x123(z95=10162210, z96=10162200):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z96, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z95, 10, 1)
    CompareObjState(8, z95, 31, 1)
    CompareObjState(8, z95, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_16_x124(z95=10162210, z96=10162200):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z96, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z95, 10, 0)
    CompareObjState(0, z95, 31, 0)
    CompareObjState(0, z95, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_16_x125(z95=10162210, z96=10162200):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_16_x121(z95=z95, z96=z96)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_16_x122(z95=z95)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_16_x123(z95=z95, z96=z96)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_16_x124(z95=z95, z96=z96)
    """State 6: Rerun"""
    return 1

def event_m10_16_x126():
    """[Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x127(z90=10162210, z91=100300, z92=100360, z93=100400, z94=100461, flag13=100742):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_Termination
    z90: Ander OBJ instance ID
    z91: Lighting completion flag
    z92: Bonfire lighting judgment flag ①
    z93: Bonfire lighting judgment flag ②
    z94: Bonfire lighting judgment flag ③
    flag13: Andyur encounter flag
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z91, 0)
    CompareEventFlag(8, z92, 1)
    CompareEventFlag(8, z93, 1)
    CompareEventFlag(8, z94, 1)
    CompareEventFlag(8, flag13, 0)
    CompareEventFlag(0, flag13, 1)
    if ConditionGroup(8):
        """State 2: End state"""
        return 0
    elif ConditionGroup(0):
        """State 3: Rerun"""
        return 1

def event_m10_16_x128(z90=10162210):
    """[Lib] [BEST] [Execution] Andel_Appearance determination_Termination
    z90: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z90, 31)
    """State 2: End state"""
    return 0

def event_m10_16_x129(z88=10162210, z89=10162200):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z88: Ander OBJ instance ID
    z89: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z88, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z89, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_16_x130(z88=10162210):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z88: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z88, 10, 0)
    CompareObjState(0, z88, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_16_x131(z88=10162210, z89=10162200):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z88: Ander OBJ instance ID
    z89: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z89, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z88, 10, 1)
    CompareObjState(8, z88, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_16_x132(z88=10162210, z89=10162200):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z88: Ander OBJ instance ID
    z89: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z89, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z88, 10, 0)
    CompareObjState(0, z88, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_16_x133(z88=10162210, z89=10162200):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z88: Ander OBJ instance ID
    z89: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_16_x129(z88=z88, z89=z89)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_16_x130(z88=z88)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_16_x131(z88=z88, z89=z89)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_16_x132(z88=z88, z89=z89)
    """State 5: Rerun"""
    return 0

def event_m10_16_x134(flag9=116020060, flag10=116000061):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag9: Lottery determination flag
    flag10: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag10) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag9) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_16_x135(z69=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z69: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z69, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_16_x136(flag9=116020060, z70=3, z71=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag9: Lottery determination flag
    z70: Number of appearance judgment points
    z71: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag9, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z70)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z71, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_16_x137(flag9=116020060, z69=14, flag10=116000061, z70=3, z71=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag9: Lottery determination flag
    z69: Random number comparison value
    flag10: Defeat flag
    z70: Number of appearance judgment points
    z71: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_16_x134(flag9=flag9, flag10=flag10)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_16_x135(z69=z69)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_16_x136(flag9=flag9, z70=z70, z71=z71)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_16_x154(flag9=flag9, z71=z71)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_16_x138(val2=_, z85=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z85: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z85) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_16_x139(z81=_, z82=0, z83=10):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z81: Appearance judgment point ID
    z82: Minimum appearance time
    z83: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z81, z81, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z82, 3, z83)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_16_x140(z84=932, z86=_, z87=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z84: Generator ID
    z86: Appearance start point ID
    z87: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z84, z86, z87)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z84)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m10_16_x141(flag11=116000061):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag11: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag11) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_16_x142(z81=_, z82=0, z83=10, z84=932, val2=_, z85=10, z86=_, z87=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z81: Intrusion detection point ID
    z82: Minimum appearance time
    z83: Maximum time to appear
    z84: Generator ID
    val2: Appearance judgment number
    z85: Lottery result point variable
    z86: Appearance start point ID
    z87: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_16_x138(val2=val2, z85=z85)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_16_x139(z81=z81, z82=z82, z83=z83)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_16_x140(z84=z84, z86=z86, z87=z87)
    """State 4: Finish"""
    return 0

def event_m10_16_x143(z79=932, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z79: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z79)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_16_x144(flag11=116000061, z80=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag11: Defeat flag
    z80: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag11, 1)
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
                    SetEventFlag(z80, 1)
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

def event_m10_16_x145(flag11=116000061, z79=932, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag11: Defeat flag
    z79: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_16_x141(flag11=flag11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_16_x143(z79=z79, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_16_x144(flag11=flag11, z80=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_16_x144(flag11=flag11, z80=102755)
    """State 5: End state"""
    return 0

def event_m10_16_x146():
    """[Lib] [DC] [Reproduction] Character deletion judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x147(z74=_, z75=7, z76=1, z77=0):
    """[Lib] [DC] [Condition] Character deletion judgment
    z74: Generator ID
    z75: Shared flag ID
    z76: Comparison value
    z77: Judgment comparison type
    """
    """State 0,2: Has the target character been generated?"""
    IsChrActive(0, z74, 1)
    assert ConditionGroup(0)
    """State 1: Has the target character completed the return action?"""
    CompareChrEzStateValue(0, z74, z75, z76, z77)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m10_16_x148(z74=_, z78=0):
    """[Lib] [DC] [Execution] Character deletion judgment
    z74: Generator ID
    z78: Whether to treat it as death
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z74, z78)
    """State 2: End state"""
    return 0

def event_m10_16_x149(z74=_, z75=7, z76=1, z77=0, z78=0):
    """[Lib] [DC] [Preset] Character deletion judgment
    z74: Generator ID
    z75: Shared flag ID
    z76: Comparison value
    z77: Judgment comparison type
    z78: Whether to treat it as death
    """
    """State 0,1: [Lib] [DC] [Reproduction] Character deletion judgment_empty_SubState"""
    assert event_m10_16_x146()
    """State 3: [Lib] [DC] [Condition] Character deletion judgment_SubState"""
    assert event_m10_16_x147(z74=z74, z75=z75, z76=z76, z77=z77)
    """State 2: [Lib] [DC] [Execution] Character deletion judgment_SubState"""
    assert event_m10_16_x148(z74=z74, z78=z78)
    """State 4: End state"""
    return 0

def event_m10_16_x150(z72=_, z73=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z72: Generator ID
    z73: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z72, z73)
    """State 2: End state"""
    return 0

def event_m10_16_x151(z72=_, z73=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z72: Generator ID
    z73: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z72, z73, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_16_x152(z72=_):
    """[Lib] [DC] [Condition] Transparent characters
    z72: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z72)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x153(z72=_, z73=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z72: Generator ID
    z73: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_16_x151(z72=z72, z73=z73)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_16_x152(z72=z72)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_16_x150(z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m10_16_x154(flag9=116020060, z71=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag9: Lottery determination flag
    z71: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag9, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z71, 0)
    """State 3: End state"""
    return 0

def event_m10_16_x155(flag8=116000086):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag8: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_16_x156(z67=848):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z67: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z67, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x157(z68=116020089):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z68: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z68, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x158(flag8=116000086, z67=848, z68=116020089):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag8: Boss destruction flag
    z67: Boss generator ID
    z68: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_16_x155(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_16_x156(z67=z67)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_16_x157(z68=z68)
    """State 4: End state"""
    return 0

def event_m10_16_x159():
    """[Reproduction] Lighting the boss room"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x160(z64=_):
    """[Condition] Boss room lighting
    z64: Igniter instance ID
    """
    """State 0,1: Ignition stand lighting standby"""
    CompareObjState(0, z64, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x161(z65=_, z66=_):
    """[Execute] Lighting the boss room
    z65: Damipoli ① Instance ID
    z66: Damipoli ② Instance ID
    """
    """State 0,1: OBJ state transition: Damipoli for fire riding"""
    ChangeObjState(z65, 71)
    ChangeObjState(z66, 70)
    """State 2: End state"""
    return 0

def event_m10_16_x162(z64=_, z65=_, z66=_):
    """[Preset] Boss room lighting
    z64: Igniter instance ID
    z65: Damipoli ① Instance ID
    z66: Damipoli ② Instance ID
    """
    """State 0,1: [Reproduction] Lighting the boss room_SubState"""
    assert event_m10_16_x159()
    """State 2: [Condition] Boss room lighting_SubState"""
    assert event_m10_16_x160(z64=z64)
    """State 3: [Execution] Lighting the boss room_SubState"""
    assert event_m10_16_x161(z65=z65, z66=z66)
    """State 4: End state"""
    return 0

def event_m10_16_x163(z57=_, z58=_, z60=_, z59=_):
    """[Reproduction] Iron lattice that opens with a lever
    z57: Object instance ID of the iron lattice OBJ
    z58: Lever OBJ object instance ID
    z60: Navigation mesh change
    z59: State ID of the state where the iron lattice OBJ is fully opened
    """
    """State 0,1: State determination of iron grid"""
    if CompareObjStateId(z57, 10, 1):
        """State 3: Disable key guide of lever"""
        DisableObjKeyGuide(z58, 1)
        """State 4: Is the iron grid open?"""
        assert CompareObjStateId(z57, z59, 0)
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z60, 2)
        """State 6: Opened"""
        return 1
    else:
        """State 5: Not open"""
        return 0

def event_m10_16_x164(z29=_):
    """[Conditions] Iron grid that opens with lever
    z29: Lever OBJ object instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z29, 74, 0)
    CompareObjState(0, z29, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x165(z57=_, z59=_, z60=_, z58=_):
    """[Execution] Iron grid that opens with lever
    z57: Object instance ID of the iron lattice OBJ
    z59: State ID of the state where the iron lattice OBJ is fully opened
    z60: Navigation mesh change
    z58: Lever OBJ object instance ID
    """
    """State 0,3: Disable key guide of lever"""
    DisableObjKeyGuide(z58, 1)
    """State 1: Iron lattice animation playback that opens with a lever"""
    ChangeObjState(z57, 70)
    """State 4: Is the iron grid open?"""
    CompareObjState(0, z57, z59, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z60, 2)
    """State 5: End state"""
    return 0

def event_m10_16_x166():
    """[Reproduction] Treasure corpse fall _ sky with yagura destruction"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x167(z63=10161300):
    """[Condition] Treasure corpse falls due to yagura destruction
    z63: Yagura instance ID
    """
    """State 0,1: Waiting for destruction of the tower"""
    IsObjBroken(0, z63, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x168(z61=10166010, z62=70):
    """[Execution] Treasure corpse falls due to yagura destruction
    z61: Instance ID of treasure corpse
    z62: Falling state ID
    """
    """State 0,1: Treasure corpse fall"""
    ChangeObjState(z61, z62)
    """State 2: End state"""
    return 0

def event_m10_16_x169(flag7=116000086):
    """[Reproduction] Changing the lock ID of the boss room
    flag7: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag7) != 0:
        """State 2: Returns lock on parameter"""
        ResetLockOnParameter()
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Not defeated"""
        return 0

def event_m10_16_x170(z2=116000086, z3=10161000, z4=10161001, z5=802000, z9=1016010):
    """[Condition] Change lock ID of boss room
    z2: Boss destruction flag
    z3: Right_Ignition table OBJ instance ID
    z4: Left_Ignition stand OBJ instance ID
    z5: Point ID
    z9: Boss Battle ID
    """
    """State 0,2: Did you invade points during the boss battle?"""
    IsPlayerInsidePoint(8, z5, z5, 1)
    IsEventBossBattle(8, z9, 1)
    assert ConditionGroup(8)
    """State 1: PC torch judgment and light lighting number judgment"""
    SetConditionGroup(0, 8)
    CompareObjState(8, z3, 20, 0)
    CompareObjState(8, z4, 20, 0)
    CompareObjState(1, z3, 20, 0)
    CompareObjState(2, z4, 20, 0)
    IsPlayerUsingTorch(3, 1)
    if ConditionGroup(0):
        """State 3: 2 lights"""
        return 0
    elif ConditionGroup(3):
        """State 7: Torches in use"""
        return 4
    elif ConditionGroup(1):
        """State 4: Right lights up"""
        return 1
    elif ConditionGroup(2):
        """State 6: Lit left"""
        return 3
    else:
        """State 5: Not lit"""
        return 2

def event_m10_16_x171(z7=626001, z4=_, z2=116000086):
    """[Execute] Changing the lock ID of the boss room
    z7: Lock-on parameter ID
    z4: OBJ instance ID waiting for lighting
    z2: Boss destruction flag
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z7)
    """State 2: Waiting for next lighting or waiting for use of torches or waiting to destroy boss"""
    CompareObjState(0, z4, 20, 0)
    CompareEventFlag(0, z2, 1)
    IsPlayerUsingTorch(0, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x172(z2=116000086, z3=10161000, z4=10161001, z5=802000, z6=626000, z7=626001, z8=626002,
                      z9=1016010):
    """[Preset] Changing the lock ID of the boss room
    z2: Boss destruction flag
    z3: Right_Ignition table OBJ instance ID
    z4: Left_Ignition stand OBJ instance ID
    z5: Point ID
    z6: Lock ID_short
    z7: Lock ID_
    z8: Lock ID_length
    z9: Boss Battle ID
    """
    """State 0,1: [Reproduction] Change lock ID of boss room_SubState"""
    assert event_m10_16_x169(flag7=116000086) == 0
    """State 2: [Condition] Change lock ID of boss room_SubState"""
    call = event_m10_16_x170(z2=z2, z3=z3, z4=z4, z5=z5, z9=z9)
    if call.Get() == 0:
        """State 3: [Execution] Change lock ID of boss room_Both lights up_SubState"""
        assert event_m10_16_x173(z2=z2, z8=z8)
        """State 9: Finish"""
        return 1
    elif call.Get() == 4:
        """State 7: [Execution] Changing the lock ID of the boss room_Torchlight in use_SubState"""
        assert event_m10_16_x239(z8=z8, z3=z3, z4=z4, z2=z2)
    elif call.Get() == 1:
        """State 5: [Execution] Change lock ID of boss room_One side is lit_SubState"""
        assert event_m10_16_x171(z7=z7, z4=z4, z2=z2)
    elif call.Get() == 3:
        """State 6: [Execution] Change lock ID of boss room_One side is lit_2_SubState"""
        assert event_m10_16_x171(z7=z7, z4=z3, z2=z2)
    elif call.Get() == 2:
        """State 4: [Execution] Changing the lock ID of the boss room_Unlit_SubState"""
        assert event_m10_16_x174(z6=z6, z3=z3, z4=z4, z2=z2)
    """State 8: Rerun"""
    return 0

def event_m10_16_x173(z2=116000086, z8=626002):
    """[Execution] Change lock ID of boss room
    z2: Boss destruction flag
    z8: Lock-on parameter ID
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z8)
    """State 2: Waiting for boss destruction"""
    CompareEventFlag(0, z2, 1)
    assert ConditionGroup(0)
    """State 3: Returns lock on parameter"""
    ResetLockOnParameter()
    """State 4: End state"""
    return 0

def event_m10_16_x174(z6=626000, z3=10161000, z4=10161001, z2=116000086):
    """[Execute] Changing lock ID of boss room
    z6: Lock-on parameter ID
    z3: Right_Ignition table OBJ instance ID
    z4: Left_Ignition stand OBJ instance ID
    z2: Boss destruction flag
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z6)
    """State 2: Waiting for next lighting or waiting for use of torches or waiting to destroy boss"""
    SetConditionGroup(0, 8)
    CompareObjState(8, z3, 20, 0)
    IsPlayerUsingTorch(8, 0)
    SetConditionGroup(0, 9)
    CompareObjState(9, z4, 20, 0)
    IsPlayerUsingTorch(9, 0)
    CompareEventFlag(0, z2, 1)
    IsPlayerUsingTorch(0, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x175(z57=_, z58=_, z59=_, z60=_):
    """[Preset] Opening with a lever
    z57: Object instance ID of the iron lattice OBJ
    z58: Lever OBJ object instance ID
    z59: State ID of the state where the iron lattice OBJ is fully opened
    z60: Navigation mesh change
    """
    """State 0,1: [Reproduction] Iron lattice _SubState opened with lever"""
    call = event_m10_16_x163(z57=z57, z58=z58, z60=z60, z59=z59)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Conditions] Iron lattice that opens with lever_SubState"""
        assert event_m10_16_x164(z29=z58)
        """State 3: [Execution] Iron lattices opened by lever_SubState"""
        assert event_m10_16_x165(z57=z57, z59=z59, z60=z60, z58=z58)
    """State 4: End state"""
    return 0

def event_m10_16_x176(z54=10164900, flag6=116000011):
    """[Reproduction] Rolling flame barrel _1F staircase
    z54: Barrel instance ID
    flag6: Event execution judgment flag
    """
    """State 0,2: Was the event executed once?"""
    if GetEventFlag(flag6) != 0:
        pass
    else:
        Goto('L0')
    """State 1: Flame barrel OBJ condition determination"""
    if CompareObjStateId(z54, 10, 0):
        """State 4: Executed_state transition"""
        return 1
    else:
        """State 5: Executed_End immediately"""
        return 2
    """State 3: Not executed"""
    Label('L0')
    return 0

def event_m10_16_x177(z52=2200000, z53=2200010, z56=9990):
    """[Conditions] Rolling flame barrel _1F staircase
    z52: Point ID when kicking
    z53: Point ID when not kicking
    z56: Generator ID of the enemy kicking the barrel
    """
    """State 0,1: Point determination and prison state determination"""
    IsPlayerInsidePoint(0, z52, z52, 1)
    CompareChrHpRatio(0, z56, 100, 1)
    IsPlayerInsidePoint(1, z53, z53, 1)
    IsChrDead(1, z56)
    if ConditionGroup(1):
        """State 3: Don't kick"""
        return 1
    elif ConditionGroup(0):
        """State 2: Kick"""
        return 0

def event_m10_16_x178(z55=116020013, z54=10164900, flag6=116000011):
    """[Execution] Rolling flame barrel_1F stair_kick
    z55: Kicking action flag
    z54: Barrel instance ID
    flag6: Event execution judgment flag
    """
    """State 0,1: Kicking action flag ON"""
    SetEventFlag(z55, 1)
    """State 4: Event execution flag ON"""
    SetEventFlag(flag6, 1)
    """State 2: Time adjustment state"""
    assert (GetStateTime() > 0.5) != 0
    """State 3: Rolling _ misfire"""
    ChangeObjState(z54, 70)
    assert CompareObjStateId(z54, 20, 0)
    """State 5: End state"""
    return 0

def event_m10_16_x179(z52=2200000, z53=2200010, z54=10164900, z55=116020013, z56=9990, flag6=116000011):
    """[Preset] Rolling flame barrel _1F staircase
    z52: Point ID when kicking
    z53: Point ID when not kicking
    z54: Barrel instance ID
    z55: Kicking action flag
    z56: Generator ID of the enemy kicking the barrel
    flag6: Event execution judgment flag
    """
    """State 0,1: [Reproduction] Rolling flame barrel _1F staircase_SubState"""
    call = event_m10_16_x176(z54=z54, flag6=flag6)
    if call.Get() == 1:
        """State 4: [Execution] Rolling flame barrel_1F staircase_Do not kick_SubState"""
        Label('L0')
        assert event_m10_16_x180(z54=z54, flag6=flag6)
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Rolling flame barrel _1F staircase_SubState"""
        call = event_m10_16_x177(z52=z52, z53=z53, z56=z56)
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            """State 3: [Execution] Rolling flame barrel_1F staircase_kick_SubState"""
            assert event_m10_16_x178(z55=z55, z54=z54, flag6=flag6)
    """State 5: End state"""
    return 0

def event_m10_16_x180(z54=10164900, flag6=116000011):
    """[Execution] Rolling flame barrel _1F staircase_Do not kick
    z54: Barrel instance ID
    flag6: Event executed flag
    """
    """State 0,1: Transition to misfire / dynamic state: 30"""
    ChangeObjState(z54, 30)
    """State 2: Event execution flag ON"""
    SetEventFlag(flag6, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x181(z49=_, z50=_, z51=_):
    """[Preset] Navimesh change due to yagura destruction
    z49: YAGURA OBJ instance ID
    z50: Point ID for changing Navimesh at the top of the tower
    z51: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: [Reproduction] Navi mesh change due to yagura destruction_SubState"""
    call = event_m10_16_x182(z49=z49)
    if call.Get() == 0:
        """State 2: [Condition] Navi mesh change due to yagura destruction_SubState"""
        assert event_m10_16_x183(z49=z49)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x184(z50=z50, z51=z51)
    """State 4: End state"""
    return 0

def event_m10_16_x182(z49=_):
    """[Reproduction] Navi mesh change due to yagura destruction
    z49: YAGURA OBJ instance ID
    """
    """State 0,1: State determination of yagura OBJ"""
    if CompareObjStateId(z49, 20, 1):
        """State 2: Undestructed"""
        return 0
    else:
        """State 3: Destroyed"""
        return 1

def event_m10_16_x183(z49=_):
    """[Condition] Navi mesh change due to yagura destruction
    z49: YAGURA OBJ instance ID
    """
    """State 0,1: Yagura OBJ transition waiting"""
    CompareObjState(0, z49, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x184(z50=_, z51=_):
    """[Execution] Navi mesh change due to yagura destruction
    z50: Point ID for changing Navimesh at the top of the tower
    z51: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: Added navigating mesh attributes at the top of the tower"""
    AddNavimeshAttribute(z50, 2)
    """State 2: Navimesh attribute deletion at the bottom of the tower"""
    DeleteNavimeshAttribute(z51, 2)
    """State 3: End state"""
    return 0

def event_m10_16_x185():
    """[Reproduction] Forgotten Sinner _ Zako Launch"""
    """State 0,2: Is the total number of laps 2 or more?"""
    if (GetGameCycleForBonfire(16685) > 2) != 0:
        pass
    else:
        Goto('L0')
    """State 1: Are you destroying the boss?"""
    if GetEventFlag(116000086) != 0:
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Not defeated"""
        return 0
    """State 5: The first lap of the game"""
    Label('L0')
    return 2

def event_m10_16_x186(z47=1016010, z48=848):
    """[Condition] Forgotten Sinner _ Start Zako
    z47: Boss Battle ID
    z48: Generator ID
    """
    """State 0,1: Boss battle start waiting"""
    IsEventBossBattle(0, z47, 1)
    assert ConditionGroup(0)
    """State 2: Has the boss's HP dropped below 70%?"""
    CompareChrHpRatio(0, z48, 70, 5)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x187():
    """[Execution] Forgotten Sinner _ Start Zako"""
    """State 0,1: Zako start flag ON"""
    SetEventFlag(116020088, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x188(z47=1016010, z48=848):
    """[Preset] Forgotten Sinner _ Start Zako
    z47: Boss Battle ID
    z48: Generator ID
    """
    """State 0,1: [Reproduction] Forgotten Sinner_Zako Launch_SubState"""
    call = event_m10_16_x185()
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Forgotten Sinner_Zako Launch_SubState"""
        assert event_m10_16_x186(z47=z47, z48=z48)
        """State 2: [Execution] Forgotten Sinner_Zako Launch_SubState"""
        assert event_m10_16_x187()
    """State 4: End state"""
    return 0

def event_m10_16_x189(flag5=116000091):
    """[Reproduction] Gargoyle image starting sequentially
    flag5: Boss destruction flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Undefeated"""
        return 0

def event_m10_16_x190(z42=1016020, z43=_):
    """[Conditions] Gargoyle images starting sequentially
    z42: Boss Battle ID
    z43: HP ratio at startup
    """
    """State 0,2: Boss battle start waiting"""
    IsEventBossBattle(0, z42, 1)
    assert ConditionGroup(0)
    """State 1: Is the total HP less than ○○?"""
    CompareEventBossHpRatio(0, z42, 0, z43, 5)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x191(z44=116020092, z45=_, z46=_):
    """[Execution] Gargoyle images starting sequentially
    z44: Gargoyle start flag
    z45: Cool time
    z46: Wait time
    """
    """State 0,1: Gargoyle start flag ON"""
    SetEventFlag(z44, 1)
    """State 2: Cool time"""
    CompareStateTime(0, z45, 3, z45)
    assert ConditionGroup(0)
    """State 3: Gargoyle start flag OFF"""
    SetEventFlag(z44, 0)
    """State 4: Logic weight"""
    CompareStateTime(0, z46, 3, z46)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m10_16_x192(flag5=116000091, z42=1016020, z43=_, z44=116020092, z45=_, z46=_):
    """[Preset] Gargoyle images starting sequentially
    flag5: Boss destruction flag
    z42: Boss Battle ID
    z43: HP ratio at startup
    z44: Gargoyle start flag
    z45: Cool time
    z46: Wait time
    """
    """State 0,1: [Reproduction] Gargoyle image_SubState starting sequentially"""
    call = event_m10_16_x189(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Gargoyle image_SubState which starts sequentially"""
        assert event_m10_16_x190(z42=z42, z43=z43)
        """State 2: [Execution] Gargoyle image_SubState starting sequentially"""
        assert event_m10_16_x191(z44=z44, z45=z45, z46=z46)
    """State 4: End state"""
    return 0

def event_m10_16_x193(z37=10162000, z38=10162010, z39=116020015, z40=4, z41=116000016):
    """[Preset] Enemies appear from the well when stones are hit
    z37: 檻 OBJ instance ID
    z38: Stone OBJ instance ID
    z39: Enemy action start flag
    z40: Waiting time until enemy action starts
    z41: Enemy generation stop flag
    """
    """State 0,1: [Reproduction] Encroaching enemies from a well when a stone is hit _SubState"""
    call = event_m10_16_x194(z37=z37, z38=z38, z39=z39, z41=z41)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] When you hit a stone, an enemy entering the well from the well_SubState"""
        assert event_m10_16_x195(z38=z38)
        """State 3: [Execution] Encroachment of enemies from a well when hitting a stone_SubState"""
        assert event_m10_16_x196(z37=z37, z38=z38, z39=z39, z40=z40, z41=z41)
    """State 4: End state"""
    return 0

def event_m10_16_x194(z37=10162000, z38=10162010, z39=116020015, z41=116000016):
    """[Reproduction] Encroachment of enemies from wells when stones are hit
    z37: 檻 OBJ instance ID
    z38: Stone OBJ instance ID
    z39: Enemy action start flag
    z41: Enemy generation stop flag
    """
    """State 0,1: Is 檻 in the initial state?"""
    if CompareObjStateId(z37, 10, 1):
        """State 3: Change of state of transparent stone OBJ"""
        ChangeObjState(z38, 20)
        assert (GetStateTime() > 4) != 0
        """State 2: Turn on enemy action start flag"""
        SetEventFlag(z39, 1)
        """State 4: Enemy generation stop flag ON"""
        SetEventFlag(z41, 1)
        """State 6: Already in operation"""
        return 1
    else:
        """State 5: Not in operation"""
        return 0

def event_m10_16_x195(z38=10162010):
    """[Condition] When a stone is hit, an enemy-filled trap appears from the well
    z38: Stone OBJ instance ID
    """
    """State 0,1: Stone attack waiting"""
    IsObjDamaged(0, z38, -1, -1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x196(z37=10162000, z38=10162010, z39=116020015, z40=4, z41=116000016):
    """[Execution] When a stone is hit, an enemy-filled trap appears from the well
    z37: 檻 OBJ instance ID
    z38: Stone OBJ instance ID
    z39: Enemy action start flag
    z40: Waiting time until enemy action starts
    z41: Enemy generation stop flag
    """
    """State 0,1: 檻 rise"""
    ChangeObjState(z37, 70)
    ChangeObjState(z38, 20)
    """State 3: Judgment whether the waiting time until the enemy's action start has passed"""
    CompareStateTime(0, z40, 2, z40)
    assert ConditionGroup(0)
    """State 2: Turn on enemy action start flag"""
    SetEventFlag(z39, 1)
    """State 4: Enemy generation stop flag ON"""
    SetEventFlag(z41, 1)
    """State 5: End state"""
    return 0

def event_m10_16_x197(z33=10165150):
    """[Reproduction] Blacksmith Treasure Chest
    z33: Treasure chest OBJ instance ID
    """
    """State 0,1: Activate key guide for treasure chest"""
    DisableObjKeyGuide(z33, 0)
    """State 2: Start state judgment"""
    return 0

def event_m10_16_x198(z34=165, z35=103790, z36=104290):
    """[Conditions] Blacksmith treasure chest
    z34: Generator ID
    z35: Hostile flag
    z36: death flag
    """
    """State 0,1: Blacksmith start-up state determination"""
    CompareChrStartUpState(8, z34, 4, 0)
    IsChrActive(8, z34, 1)
    CompareEventFlag(1, z35, 1)
    CompareEventFlag(1, z36, 1)
    IsChrDead(1, z34)
    if ConditionGroup(1):
        """State 3: Blacksmith: Hostile or dead"""
        return 1
    elif ConditionGroup(8):
        """State 2: Blacksmith: Starting state"""
        return 0

def event_m10_16_x199(z33=10165150, z34=165):
    """[Execution] Blacksmith Treasure Box
    z33: Treasure chest OBJ instance parameters
    z34: Generator ID
    """
    """State 0,1: Disable treasure chest key guide"""
    DisableObjKeyGuide(z33, 1)
    """State 2: Was the startup state released?"""
    CompareChrStartUpState(0, z34, 4, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x200(z33=10165150, z34=165, z35=103790, z36=104290):
    """[Preset] Blacksmith Treasure Chest
    z33: Treasure chest OBJ instance parameters
    z34: Generator ID
    z35: Hostile flag
    z36: death flag
    """
    """State 0,1: [Reproduction] Blacksmith Treasure Box_SubState"""
    assert event_m10_16_x197(z33=z33)
    """State 3: [Conditions] Blacksmith Treasure Box_SubState"""
    call = event_m10_16_x198(z34=z34, z35=z35, z36=z36)
    if call.Get() == 0:
        """State 2: [Execution] Blacksmith Treasure Box_Waiting for Next Decision_SubState"""
        assert event_m10_16_x199(z33=z33, z34=z34)
        """State 5: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Execution] Blacksmith Treasure Box_Activation Only_SubState"""
        assert event_m10_16_x201(z33=z33, z34=z34)
        """State 6: Finish"""
        return 1

def event_m10_16_x201(z33=10165150, z34=165):
    """[Execution] Blacksmith's Treasure Box_Activation Only
    z33: Treasure chest OBJ instance parameters
    z34: Generator ID
    """
    """State 0,1: Activate key guide for treasure chest"""
    DisableObjKeyGuide(z33, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x202(z27=10161071, z28=10161072, z29=10161028, z30=203000, z31=203001, z32=30):
    """[Preset] Lattice open by lever
    z27: Object instance ID of foreground OBJ
    z28: Object instance ID of the back iron lattice OBJ
    z29: Lever OBJ object instance ID
    z30: Change front Navimesh
    z31: Navimesh change in the back
    z32: State ID of the state where the iron lattice OBJ is fully opened
    """
    """State 0,1: [Reproduction] Iron lattice_passage_SubState opened with lever"""
    call = event_m10_16_x203(z27=z27, z28=z28, z29=z29, z30=z30, z31=z31, z32=z32)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Conditions] Iron lattice that opens with lever_SubState"""
        assert event_m10_16_x164(z29=z29)
        """State 3: [Execution] Lattice open by lever_passage_SubState"""
        assert event_m10_16_x204(z27=z27, z28=z28, z32=z32, z30=z30, z31=z31, z29=z29)
    """State 4: End state"""
    return 0

def event_m10_16_x203(z27=10161071, z28=10161072, z29=10161028, z30=203000, z31=203001, z32=30):
    """[Reproduction] Opening with a lever
    z27: Object instance ID of foreground OBJ
    z28: Object instance ID of the back iron lattice OBJ
    z29: Lever OBJ object instance ID
    z30: Change front Navimesh
    z31: Navimesh change in the back
    z32: State ID of the state where the iron lattice OBJ is fully opened
    """
    """State 0,1: Judging the state of the front iron grid"""
    if CompareObjStateId(z27, 10, 1):
        pass
    else:
        Goto('L0')
    """State 3: Disable key guide of lever"""
    DisableObjKeyGuide(z29, 1)
    """State 7: Is the front iron grid open?"""
    assert CompareObjStateId(z27, z32, 0)
    """State 2: Delete previous Navimesh attribute"""
    DeleteNavimeshAttribute(z30, 2)
    """State 5: Determining the state of the iron bar"""
    if CompareObjStateId(z28, z32, 0):
        pass
    else:
        """State 6: Animation reproduction of the iron grid in the back"""
        ChangeObjState(z28, 70)
        """State 8: Is the iron bar in the back open?"""
        assert CompareObjStateId(z28, z32, 0)
    """State 4: Delete back Navi Mesh attribute"""
    DeleteNavimeshAttribute(z31, 2)
    """State 10: Opened"""
    return 1
    """State 9: Not open"""
    Label('L0')
    return 0

def event_m10_16_x204(z27=10161071, z28=10161072, z32=30, z30=203000, z31=203001, z29=10161028):
    """[Execution] Lattice open by lever
    z27: Object instance ID of foreground OBJ
    z28: Object instance ID of the back iron lattice OBJ
    z32: State ID of the state where the iron lattice OBJ is fully opened
    z30: Change front Navimesh
    z31: Navimesh change in the back
    z29: Lever OBJ object instance ID
    """
    """State 0,3: Disable key guide of lever"""
    DisableObjKeyGuide(z29, 1)
    """State 1: Animation playback of the front grid"""
    ChangeObjState(z27, 70)
    """State 6: Is the front iron grid open?"""
    CompareObjState(0, z27, z32, 0)
    assert ConditionGroup(0)
    """State 2: Delete previous Navimesh attribute"""
    DeleteNavimeshAttribute(z30, 2)
    """State 4: Animation reproduction of the iron grid in the back"""
    ChangeObjState(z28, 70)
    """State 7: Is the iron bar in the back open?"""
    CompareObjState(0, z28, z32, 0)
    assert ConditionGroup(0)
    """State 5: Delete back Navi Mesh attribute"""
    DeleteNavimeshAttribute(z31, 2)
    """State 8: End state"""
    return 0

def event_m10_16_x205():
    """[Reproduction] OBJ_sky blocking one-way door"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x206(z25=10161550):
    """[Conditions] OBJ blocking a one-way door
    z25: OBJ instance ID to be destroyed
    """
    """State 0,1: Is the target OBJ broken?"""
    IsObjBroken(0, z25, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x207(z26=116000057):
    """[Execution] OBJ blocking one-way door
    z26: One-way door flag
    """
    """State 0,1: One-way flag ON"""
    SetEventFlag(z26, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x208(z25=10161550, z26=116000057):
    """[Preset] OBJ blocking the one-way door
    z25: OBJ instance ID to be destroyed
    z26: One-way door flag
    """
    """State 0,1: [Reproduction] OBJ_Sky_SubState that blocks a one-way door"""
    assert event_m10_16_x205()
    """State 3: [Condition] OBJ_SubState that blocks a one-way door"""
    assert event_m10_16_x206(z25=z25)
    """State 2: [Execution] OBJ_SubState to block the one-way door"""
    assert event_m10_16_x207(z26=z26)
    """State 4: End state"""
    return 0

def event_m10_16_x209(flag4=116000086):
    """[Reproduction] Forgotten Sinner Battle_Start
    flag4: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag4) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_16_x210(z18=1500000, z24=1500000):
    """[Condition] Forgotten Sinner Battle_Start
    z18: Start point ID
    z24: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z18, z24, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z18, z24, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x211(z19=1016010, z20=116020085):
    """[Execute] Forgotten Sinner Battle_Start
    z19: Boss Battle ID
    z20: Other flags for logic
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z19)
    """State 2: Logic flag ON"""
    SetEventFlag(z20, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x212():
    """[Reproduction] Boss BGM playback_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x213(z21=5, z22=848):
    """[Condition] Boss BGM playback
    z21: BGM playback start distance
    z22: Generator ID
    """
    """State 0,1: Did you approach the boss? Or did you give damage?"""
    CompareChrPlayerDistance(0, z22, z21, 5)
    CompareChrHpRatio(0, z22, 100, 4)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x214(z23=101, z19=1016010):
    """[Execute] Boss BGM playback
    z23: Sound ID
    z19: Boss Battle ID
    """
    """State 0,2: Did the boss die before playing BGM?"""
    IsEventBossKill(0, z19, 0, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z23)
    """State 3: End state"""
    return 0

def event_m10_16_x215():
    """[Reproduction] Forgotten Sinner Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x216(z19=1016010):
    """[Condition] Forgotten Sinner Battle_End Judgment
    z19: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z19, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x217(z23=101, z19=1016010, z20=116020085, mode1=0):
    """[Execute] Forgotten Sinner Battle_End
    z23: Sound ID
    z19: Boss Battle ID
    z20: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z20, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z19)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z23)
    """State 5: End state"""
    return 0

def event_m10_16_x218(flag4=116000086, z18=1500000, z19=1016010, z20=116020085, z21=5, z22=848, z23=101,
                      mode1=0):
    """[Preset] Boss: Forgotten Sinner Battle
    flag4: Boss destruction flag
    z18: Boss Battle Start Point ID
    z19: Boss Battle ID
    z20: Logic flag
    z21: BGM playback start distance
    z22: Generator ID
    z23: Sound ID
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Forgotten Sinner Battle_Start_SubState"""
    call = event_m10_16_x209(flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Forgotten Sinner Battle_Start_SubState"""
        assert event_m10_16_x210(z18=z18, z24=z18)
        """State 3: [Execution] Forgotten Sinner Battle_Start_SubState"""
        assert event_m10_16_x211(z19=z19, z20=z20)
        """State 7: [Reproduction] Boss BGM playback_Sky_SubState"""
        assert event_m10_16_x212()
        """State 9: [Condition] Boss BGM playback_SubState"""
        assert event_m10_16_x213(z21=z21, z22=z22)
        """State 8: [Execution] Boss BGM playback_SubState"""
        assert event_m10_16_x214(z23=z23, z19=z19)
        """State 2: [Reproduction] Forgotten Sinner Battle_End_Sky_SubState"""
        assert event_m10_16_x215()
        """State 6: [Condition] Forgotten Sinner Battle_End Judgment_SubState"""
        assert event_m10_16_x216(z19=z19)
        """State 4: [Execution] Forgotten Sinner Battle_End_SubState"""
        assert event_m10_16_x217(z23=z23, z19=z19, z20=z20, mode1=mode1)
    """State 10: End state"""
    return 0

def event_m10_16_x219():
    """[Reproduction] Launching enemies by destroying Matryoshka _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x220(z16=_):
    """[Conditions] Enemies activated by matryoshka destruction
    z16: Matryoshka OBJ instance ID
    """
    """State 0,1: Matryoshka waiting for destruction"""
    IsObjBroken(0, z16, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x221(z17=_):
    """[Execution] Enemies activated by matryoshka
    z17: Enemy activation flag
    """
    """State 0,1: Enemy activation flag ON"""
    SetEventFlag(z17, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x222(z16=_, z17=_):
    """[Preset] Enemies activated by matryoshka destruction
    z16: Matryoshka OBJ instance ID
    z17: Enemy activation flag
    """
    """State 0,1: [Reproduction] Enemy starts with Matryoshka destruction_Sky_SubState"""
    assert event_m10_16_x219()
    """State 3: [Condition] Enemies activated by Matryoshka destruction_SubState"""
    assert event_m10_16_x220(z16=z16)
    """State 2: [Execution] Enemies activated by Matryoshka destruction_SubState"""
    assert event_m10_16_x221(z17=z17)
    """State 4: End state"""
    return 0

def event_m10_16_x223():
    """[Reproduction] Leave the door open"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x224(z15=10160420):
    """[Conditions] Opened door
    z15: OBJ instance ID of the door
    """
    """State 0,1: Has the door opened?"""
    CompareObjState(0, z15, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x225(z15=10160420):
    """[Execution] Opened door
    z15: OBJ instance ID of the door
    """
    """State 0,1: Disable key guide for door"""
    DisableObjKeyGuide(z15, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x226(z15=10160420):
    """[Preset] Opened door
    z15: OBJ instance ID of the door
    """
    """State 0,1: [Reproduction] Open door _SubState"""
    assert event_m10_16_x223()
    """State 3: [Conditions] Opened door_SubState"""
    assert event_m10_16_x224(z15=z15)
    """State 2: [Execution] Leave the door open_SubState"""
    assert event_m10_16_x225(z15=z15)
    """State 4: End state"""
    return 0

def event_m10_16_x227():
    """[BEST] [Reproduction] Seoul acquisition suppression ring"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m10_16_x228():
    """[BEST] [Conditions] Seoul acquisition restraint ring"""
    """State 0,1: Is the cumulative amount of souls earned above a certain level?"""
    CompareCumulativeSouls(0, GetCommonEventParamInt(16), 3, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x229():
    """[BEST] [execution] Seoul acquisition restraint ring"""
    """State 0,1: Sales start flag ON"""
    SetEventFlag(100780, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x230():
    """[BEST] [Preset] Soul Acquisition Suppression Ring"""
    """State 0,1: [BEST] [Reproduction] Soul acquisition restraint ring_Sales start_SubState"""
    call = event_m10_16_x227()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [BEST] [Conditions] Seoul acquisition restraint ring_Sales start_SubState"""
        assert event_m10_16_x228()
        """State 2: [BEST] [Execution] Soul acquisition restraint ring_Sales start_SubState"""
        assert event_m10_16_x229()
    """State 4: End state"""
    return 0

def event_m10_16_x231(flag2=_, flag3=116000091, z12=_):
    """[DC] [Reproduction] Flying Gargoyle
    flag2: Event executed flag
    flag3: Boss destruction flag
    z12: Generator ID
    """
    """State 0,3: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 7: The guests"""
    return 2
    """State 2: Has the boss been destroyed?"""
    Label('L0')
    if GetEventFlag(flag3) != 0:
        pass
    else:
        """State 1: Has the event been executed?"""
        if GetEventFlag(flag2) != 0:
            pass
        else:
            """State 5: Event not executed"""
            return 0
    """State 4: Delete character"""
    DeleteEnemyByGenerator(z12, 0)
    """State 6: Event executed and destroyed"""
    return 1

def event_m10_16_x232(z12=_, flag3=116000091, z13=_):
    """[DC] [Conditions] Flying gargoyle
    z12: Generator ID
    flag3: Boss destruction flag
    z13: Event start point ID
    """
    """State 0,1: Defeat point or boss"""
    IsPlayerInsidePoint(8, z13, z13, 1)
    IsHost(8, 1, 0)
    CompareEventFlag(0, flag3, 1)
    if ConditionGroup(0):
        """State 3: Defeat the boss"""
        return 1
    elif ConditionGroup(8):
        """State 2: Flying gargoyle generation"""
        return 0

def event_m10_16_x233(flag2=_, z12=_, val1=_, z14=1605010):
    """[DC] [execution] Flying gargoyle
    flag2: Event executed flag
    z12: Generator ID
    val1: Weight until generation
    z14: Gargoyle judgment deletion point ID
    """
    """State 0,4: weight"""
    assert (GetStateTime() > val1) != 0
    """State 1: Executed flag ON"""
    SetEventFlag(flag2, 1)
    """State 2: Deletion point intrusion detection"""
    IsChrInsidePoint(0, z12, z14, z14, 1)
    assert ConditionGroup(0)
    """State 3: Delete character"""
    DeleteEnemyByGenerator(z12, 0)
    """State 5: Finish"""
    return 0

def event_m10_16_x234(flag2=_, flag3=116000091, z12=_, z13=_, z14=1605010, val1=_):
    """[DC] [Preset] Flying Gargoyle
    flag2: Event executed flag
    flag3: Boss destruction flag
    z12: Generator ID
    z13: Event start point ID
    z14: Gargoyle judgment deletion point ID
    val1: Weight until generation
    """
    """State 0,1: [DC] [Reproduction] Flying Gargoyle_SubState"""
    call = event_m10_16_x231(flag2=flag2, flag3=flag3, z12=z12)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Gargoyle_SubState to fly"""
        call = event_m10_16_x232(z12=z12, flag3=flag3, z13=z13)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [DC] [execution] Flying gargoyle_SubState"""
            assert event_m10_16_x233(flag2=flag2, z12=z12, val1=val1, z14=z14)
    """State 4: End state"""
    return 0

def event_m10_16_x235():
    """[DC] [Reproduction] Acquisition of old key_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x236(z10=10165240):
    """[DC] [Condition] Judgment of obtaining an old key
    z10: Iron treasure chest OBJ instance ID
    """
    """State 0,1: Got an old key?"""
    WasObjItemAcquired(0, z10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x237(z11=116000014):
    """[DC] [Execution] Judgment of obtaining an old key
    z11: Old key acquisition flag
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(116000014, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x238(z10=10165240, z11=116000014):
    """[DC] [Preset] Acquisition of old keys
    z10: Iron treasure chest OBJ instance ID
    z11: Old key acquisition flag
    """
    """State 0,1: [DC] [Reproduction] Old key acquisition determination_empty_SubState"""
    assert event_m10_16_x235()
    """State 3: [DC] [Condition] Judgment of old key acquisition_SubState"""
    assert event_m10_16_x236(z10=z10)
    """State 2: [DC] [Execution] Acquisition determination of old keys_SubState"""
    assert event_m10_16_x237(z11=z11)
    """State 4: End state"""
    return 0

def event_m10_16_x239(z8=626002, z3=10161000, z4=10161001, z2=116000086):
    """[Execute] Changing lock ID of boss room
    z8: Lock-on parameter ID
    z3: Right_Ignition table OBJ instance ID
    z4: Left_Ignition stand OBJ instance ID
    z2: Boss destruction flag
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z8)
    """State 2: Waiting for both lights to be turned on next or waiting for torches not used or waiting to destroy boss"""
    SetConditionGroup(0, 8)
    CompareObjState(8, z3, 20, 0)
    CompareObjState(8, z4, 20, 0)
    CompareEventFlag(0, z2, 1)
    IsPlayerUsingTorch(0, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x240(flag1=116000031):
    """[DC] [Condition] Door key guide disabled until petrochemical release
    flag1: Petrochemical release flag
    """
    """State 0,1: Was it petrified?"""
    CompareEventFlag(0, flag1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x241(z1=10160410):
    """[DC] [Execution] Door key guide disabled until petrochemical release
    z1: Door OBJ instance ID
    """
    """State 0,1: Activate key guide"""
    DisableObjKeyGuide(z1, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x242(flag1=116000031, z1=10160410):
    """[DC] [Reproduction] Door key guide disabled until petrification is canceled
    flag1: Petrochemical release flag
    z1: Door OBJ instance ID
    """
    """State 0,2: Petrified state judgment"""
    if GetEventFlag(flag1) != 0:
        """State 4: Canceled"""
        return 1
    else:
        """State 1: Disable key guide"""
        DisableObjKeyGuide(z1, 1)
        """State 3: Petrified state"""
        return 0

def event_m10_16_x243(flag1=116000031, z1=10160410):
    """[DC] [Preset] Door key guide disabled until petrochemical release
    flag1: Petrochemical release flag
    z1: Door OBJ instance ID
    """
    """State 0,1: [DC] [Reproduction] Door key guide disabled until the petrification is canceled_SubState"""
    call = event_m10_16_x242(flag1=flag1, z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Door key guide disabled until the petrification is canceled_SubState"""
        assert event_m10_16_x240(flag1=flag1)
    """State 2: [DC] [Execution] Door key guide disabled until the petrification is canceled_SubState"""
    assert event_m10_16_x241(z1=z1)
    """State 4: Finish"""
    return 0

def event_m10_16_111272():
    """OBJ: Woman Knight (Forgetting Prison): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z225=104192, z226=10164100, z227=91, z228=7520)
    Quit()

def event_m10_16_111273():
    """OBJ: Woman Knight (Forgetting Prison): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_16_x4(z220=116010100, z221=116020101, z222=104190, z223=10164100, z224=111272, npc1=7520)
    Quit()

def event_m10_16_111274():
    """OBJ: Woman Knight (forgetting prison): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_16_x8(z202=90, z203=104192)
    Quit()

def event_m10_16_111275():
    """OBJ: Female Knight (Forgetting Prison): Appearance Judgment"""
    """State 0,1: [Lib] NPC: Woman Knight: Appearance Judgment_SubState"""
    event_m10_16_x7(z204=102481, z205=102482, z206=102483, z207=102485, z208=102490, z209=102486, z210=102487,
                    z211=102488)
    Quit()

def event_m10_16_111276():
    """OBJ: Woman Knight (Forgetting Prison): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_16_x64(z143=102500, z144=546, z145=104190, z146=61, z147=103690, z148=-1)
    Quit()

def event_m10_16_111277():
    """OBJ: Woman Knight (Forgetting Prison): White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_16_x73(z125=116000086, z126=102498, z127=204, z128=7520)
    Quit()

def event_m10_16_111282():
    """OBJ: Kanemori: Aken: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z225=104200, z226=10164200, z227=96, z228=7530)
    Quit()

def event_m10_16_111283():
    """OBJ: Kanemori: Aken: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7530:Bell Keeper
    event_m10_16_x4(z220=116010120, z221=116020121, z222=104200, z223=10164200, z224=111282, npc1=7530)
    Quit()

def event_m10_16_111284():
    """NPC: Kanemori: Black Phantom Appearance: Offline"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
    event_m10_16_x79(z114=10001000, z115=541, z116=0, z117=2)
    Quit()

def event_m10_16_111372():
    """OBJ: EX Blacksmith: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z225=104290, z226=10164000, z227=166, z228=7643)
    Quit()

def event_m10_16_111373():
    """OBJ: EX Blacksmith: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7643:Steady Hand McDuff
    event_m10_16_x4(z220=116010140, z221=116020141, z222=104290, z223=10164000, z224=111372, npc1=7643)
    Quit()

def event_m10_16_111374():
    """OBJ: EX blacksmith: Judgment of movement"""
    """State 0,1: Judgment: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    else:
        """State 2: Movement judgment: Death judgment"""
        CompareEventFlag(0, 104290, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 7: Movement Judgment: Adversity Judgment"""
            CompareEventFlag(0, 103790, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 4: Movement judgment: Treasure chest open / close judgment"""
                CompareObjState(0, 10165150, 80, 0)
                if ConditionGroup(0):
                    """State 5: Movement judgment: Movement permission"""
                    Label('L0')
                    SetEventFlag(102690, 1)
                    CompareEventFlag(0, 102690, 1)
                    assert ConditionGroup(0)
                else:
                    """State 6: Movement judgment: Lighthouse use judgment"""
                    CompareObjState(0, 10160708, 30, 0)
                    if ConditionGroup(0):
                        Goto('L0')
                    else:
                        pass
                """State 8: Movement judgment: System termination: Wait"""
                CompareEventStatus(0, 111377, 1, 0)
                assert ConditionGroup(0)
    """State 3: Movement judgment: System: End"""
    EndMachine()
    Quit()

def event_m10_16_111376():
    """OBJ: EX Blacksmith: Appearance after moving"""
    """State 0,1: Appearance after movement: Start"""
    CompareEventStatus(0, 111374, 1, 0)
    assert ConditionGroup(0)
    """State 2: Appearance after movement: Adversity"""
    CompareEventFlag(8, 103790, 1)
    IsChrActive(8, 165, 1)
    CompareEventFlag(0, 102690, 0)
    if ConditionGroup(0):
        """State 4: Appearance after moving: Appearance not possible"""
        Label('L0')
        SetEventFlag(116010147, 0)
        CompareEventFlag(0, 116010147, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        Goto('L0')
    else:
        """State 3: Appearance after movement: Appearance allowed"""
        DeleteEnemyByGeneratorGroup(62, 0)
        SetEventFlag(116010147, 1)
        CompareEventFlag(0, 116010147, 1)
        assert ConditionGroup(0)
    """State 6: Appearance determination after moving: System termination: Wait"""
    CompareEventStatus(0, 111377, 1, 0)
    assert ConditionGroup(0)
    """State 5: Appearance after movement: System: End"""
    EndMachine()
    Quit()

def event_m10_16_111377():
    """OBJ: EX Blacksmith: Shop List"""
    """State 0,1: Shop list: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Shop list: Fire lap: Judgment"""
        # bonfire:16670:McDuff's Workshop
        CompareGameCycleForBonfire(0, 16670, 1, 2, 3)
        if ConditionGroup(0):
            """State 4: Shop list: Fire lap: Flag setting"""
            SetEventFlag(102682, 1)
            CompareEventFlag(0, 102682, 1)
            assert ConditionGroup(0)
        else:
            pass
    """State 3: Shop list: System: End"""
    EndMachine()
    Quit()

def event_m10_16_111402():
    """OBJ: Spermania: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z225=104310, z226=10164300, z227=146, z228=7680)
    Quit()

def event_m10_16_111403():
    """OBJ: Spermania: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7680:Straid of Olaphis
    event_m10_16_x4(z220=116010150, z221=116020151, z222=104310, z223=10164300, z224=111402, npc1=7680)
    Quit()

def event_m10_16_111404():
    """OBJ: Spermania: Petrification: Key guide"""
    """State 0,1: [Lib] Character: Petrified: Key Guide_SubState"""
    event_m10_16_x59(z154=145, z155=104310, z156=15, z157=0, z158=102741, z159=1600, z160=3, z161=111405)
    Quit()

def event_m10_16_111405():
    """OBJ: Spermania: Petrification: Appearance setting"""
    """State 0,1: [Lib] Character: Petrified: Appearance setting_SubState"""
    event_m10_16_x67(z132=145, z133=104310, z134=0, z135=102741, z136=0, z137=111404)
    Quit()

def event_m10_16_111407():
    """OBJ: Spermania: Move permission"""
    """State 0,1: Move permission: Start"""
    CompareEventFlag(8, 102741, 1)
    IsChrActive(8, 145, 0)
    assert ConditionGroup(8)
    """State 4: Move permission: Startup state override"""
    OverrideGeneratorStartupState(147, 0)
    CompareChrStartUpState(0, 147, 0, 0)
    assert ConditionGroup(0)
    """State 3: Move permission: Move permission setting"""
    SetEventFlag(102742, 1)
    CompareEventFlag(0, 102742, 1)
    assert ConditionGroup(0)
    """State 5: Move permission: Previous generator: Erase"""
    DeleteEnemyByGeneratorGroup(60, 0)
    """State 2: Move permission: System: Exit"""
    EndMachine()
    Quit()

def event_m10_16_118120():
    """Multi-use NPC: Sage (Female): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z131=547)
    Quit()

def event_m10_16_118121():
    """Multi-use NPC: Small White Spirit 1"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z131=548)
    Quit()

def event_m10_16_118122():
    """Multi NPC: White Spirit 2"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z131=549)
    Quit()

def event_m10_16_118123():
    """Multi-use NPC: Small White Spirit 2"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z131=550)
    Quit()

def event_m10_16_118200():
    """Multi-use NPC: Mercenary (Male): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_16_x78(z118=10002000, z119=540, z120=0, z121=2)
    Quit()

def event_m10_16_120050():
    """Trophy: Bell Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_16_x80(flag20=116020127, z113=23)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_16_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_16_x80(flag20=116020109, z113=33)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_16_120140():
    """Trophy: skilled craftsman"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_16_x80(flag20=116020148, z113=34)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_16_4000000():
    """[BEST] Andyur appearance _ oblivion"""
    """State 0,3: [Lib] [BEST] [Preset] Ander_Termination_SubState"""
    call = event_m10_16_x120(z90=10162210, flag12=100740, flag13=100742, flag14=100761, z91=100300, z92=100360,
                             z93=100400, z94=100461)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_16_4001000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_16_x133(z88=10162210, z89=10162200)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_16_4002000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_16_x125(z95=10162210, z96=10162200)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_16_4010000():
    """[BEST] Seoul acquisition restraint ring"""
    """State 0,2: [BEST] [Preset] Soul Acquisition Suppression Ring_Sales Start_SubState"""
    assert event_m10_16_x230()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4011000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_16_x59(z154=9900, z155=0, z156=15, z157=116000031, z158=0, z159=1600, z160=6, z161=4011010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4011010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_16_x67(z132=9900, z133=0, z134=116000031, z135=0, z136=0, z137=4011000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4011020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_16_x77(z122=6011020, z123=0, z124=2, flag21=116000031, flag22=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4011100():
    """[DC] Door key guide disabled until petrochemical release"""
    """State 0,2: [DC] [Preset] Door key guide disabled until the petrification is canceled_SubState"""
    assert event_m10_16_x243(flag1=116000031, z1=10160410)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4012000():
    """[DC] Vegrant Deletion Decision_1"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z74=4000, z75=7, z76=1, z77=0, z78=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4012010():
    """[DC] Vegrant Deletion Decision_2"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z74=4010, z75=7, z76=1, z77=0, z78=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4012020():
    """[DC] Vegrant Deletion Determination_3"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z74=4020, z75=7, z76=1, z77=0, z78=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4012030():
    """[DC] Vegrant Deletion Determination_4"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z74=4030, z75=7, z76=1, z77=0, z78=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4013000():
    """[DC] Gargoyle to fly_additional location_1"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(flag2=116000035, flag3=116000091, z12=8010, z13=1605000, z14=1605010, val1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4013010():
    """[DC] Flying gargoyle_additional location_2"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(flag2=116000036, flag3=116000091, z12=8011, z13=1605000, z14=1605010, val1=1.2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4013100():
    """[DC] Flying gargoyle_conventional position_1"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(flag2=116000037, flag3=116000091, z12=8012, z13=1605001, z14=1605010, val1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4013110():
    """[DC] Flying Gargoyle_Conventional Position_2"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(flag2=116000038, flag3=116000091, z12=8013, z13=1605001, z14=1605010, val1=1.2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4013120():
    """[DC] Flying Gargoyle_Conventional position_3"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(flag2=116000039, flag3=116000091, z12=8014, z13=1605001, z14=1605010, val1=1.8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4014000():
    """[DC] Disabling damage"""
    """State 0,1: STRAY: Petrified damage disabled"""
    SetDamageImmunityByCharacterId(768000, 112503110, 1)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4015000():
    """[DC] Treasure corpse on the well's foot_1"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_16_x58(z162=10162000, z163=150, z164=10166490)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4016000():
    """[DC] Acquisition of old keys"""
    """State 0,2: [DC] [Preset] Old key acquisition judgment_SubState"""
    assert event_m10_16_x238(z10=10165240, z11=116000014)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4017000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_16_x137(flag9=116020060, z69=14, flag10=116000061, z70=3, z71=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m10_16_x142(z81=80000000, z82=0, z83=10, z84=932, val2=1, z85=10, z86=80000001,
                z87=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m10_16_x142(z81=80000100, z82=0, z83=10, z84=932, val2=2, z85=10, z86=80000101,
                z87=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m10_16_x142(z81=80000200, z82=0, z83=10, z84=932, val2=3, z85=10, z86=80000201,
                z87=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(116020062, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4017010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_16_x145(flag11=116000061, z79=932, mode2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_16_x153(z72=8200, z73=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_16_x153(z72=8201, z73=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_16_x153(z72=8202, z73=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_16_4031000():
    """[DC] NPC White Spirit_Gesture Management_Forgotten Sinner"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_16_x158(flag8=116000086, z67=848, z68=116020089)
    """State 1: Finish"""
    EndMachine()
    Quit()

