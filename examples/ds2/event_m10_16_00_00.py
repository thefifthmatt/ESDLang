# -*- coding: utf-8 -*-
def event_m10_16_2000():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z63=10161070, z64=10161025, z65=30, z66=200000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_2010():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z63=10161060, z64=10161026, z65=30, z66=201000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_2020():
    """Iron lattice rising with wall hole lever _ underground"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z63=10161062, z64=10161027, z65=20, z66=202000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_2030():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Lattice open by lever_passage_SubState"""
    assert event_m10_16_x202(z31=10161071, z32=10161072, z33=10161028, z34=203000, z35=203001, z36=30)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_2040():
    """Iron grid rising with wall hole lever"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m10_16_x175(z63=10161073, z64=10161029, z65=30, z66=204000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_3000():
    """Elevator (below boss room)"""
    """State 0,2: Standby for initial position setting"""
    assert EventEnded(3030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_16_x16(z160=10161020, z161=300000, z162=300001, z163=10161021, z164=10161022)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_3010():
    """Elevator (below boss room) lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z218=10161020, z219=10161021, z220=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_3020():
    """Elevator (below boss room) under lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z218=10161020, z219=10161022, z220=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_3030():
    """Elevator (under boss room) initial position setting"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m10_16_x29(z214=10161020, z215=40, z216=116000005, z217=40)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4000():
    """Bell guard_bell lever"""
    """State 0,3: [Lib] [Preset] Bell guard_Lever that rings the bell_SubState"""
    call = event_m10_16_x93(z115=10161023, z116=10161050, mode3=0, z117=0, z118=0, z119=10161051, z120=10160620,
                            z121=400000)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()

def event_m10_16_4010():
    """Kanemori_Receiving the bell net"""
    """State 0,2: [Lib] [Preset] Kanemori_Net reception_SubState"""
    assert event_m10_16_x85(z129=12000, mode4=1, mode5=1, mode6=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_4020():
    """Jewel guard"""
    """State 0,2: [Lib] [Preset] Kanemori _ Judgment Spirit Lever Use Decision_SubState"""
    assert event_m10_16_x92(z128=10161023)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_5000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161150, z172=20, z173=500000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_5010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161185, z172=20, z173=501000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_5020():
    """Hidden Door Navi Mesh Change 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161170, z172=20, z173=502000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_5030():
    """Hidden Door Navi Mesh Change 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161190, z172=20, z173=503000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_6000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_16_x34(z203=10161030)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_6010():
    """[Insect key] Hidden door ① 1"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_16_x44(z201=10161030, val3=10160000, z202=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_6030():
    """[Insect Key] 1_Navimesh change for hidden doors ①"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161100, z172=20, z173=603000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_6100():
    """[Insect key] Hidden door ② For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_16_x34(z203=10161031)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_6110():
    """[Insect key] Hidden door ②"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_16_x44(z201=10161031, val3=10160010, z202=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_6120():
    """[Insect key] Hidden door ②_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161110, z172=20, z173=612000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_8000():
    """Boss room lighting_Right"""
    """State 0,2: [Preset] Boss room lighting_SubState"""
    assert event_m10_16_x162(z71=10160753, z72=10161002, z73=10161000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_8010():
    """Boss room lighting_Left"""
    """State 0,2: [Preset] Boss room lighting_SubState"""
    assert event_m10_16_x162(z71=10160752, z72=10161003, z73=10161001)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_8020():
    """Boss room lock-on parameter change"""
    """State 0,3: [Preset] Change lock ID of boss room_SubState"""
    call = event_m10_16_x172(z3=116000086, z4=10161000, z5=10161001, z6=802000, z7=626000, z8=626001,
                             z9=626002, z10=1016010)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_16_9000():
    """Changed Navimesh of wall 1 to destroy with flame barrel"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161040, z172=20, z173=900000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_9010():
    """Changed Navimesh of Wall 2 to be destroyed by a flame barrel"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161045, z172=20, z173=901000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_10000():
    """Treasure corpse falls due to tower destruction"""
    """State 0,2: [Reproduction] Treasure corpse fall due to yagura destruction_Sky_SubState"""
    assert event_m10_16_x166()
    """State 4: [Condition] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_16_x167(z70=10161300)
    """State 3: [Execution] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_16_x168(z68=10166010, z69=70)
    """State 1: Finish"""

def event_m10_16_11000():
    """Navimesh change due to yagura destruction 1"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x181(z54=10161300, z55=1100000, z56=1100001)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_11010():
    """Navimesh change due to yagura destruction 2"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x181(z54=10161325, z55=1101000, z56=1101001)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_11020():
    """Navimesh change due to yagura destruction 3"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x181(z54=10161320, z55=1102000, z56=1102001)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_13000():
    """When a stone is hit, an enemy-filled spear appears from the well"""
    """State 0,2: [Preset] Encroachment of enemies from a well when hitting a stone_SubState"""
    assert event_m10_16_x193(z41=10162000, z42=10162010, z43=116020015, z44=4, z45=116000016)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_14000():
    """Boss: Warrior in the Mirror_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_16_x9(z221=116000081, z222=1400000, z223=1400000, z224=102, z225=1016000, z226=116020080,
            mode8=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_16_14100():
    """Navi mesh change of hidden door in boss room 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161160, z172=20, z173=1410000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_14110():
    """Navi mesh change of hidden door in boss room 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161155, z172=20, z173=1411000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_14120():
    """Navi mesh change of hidden door in boss room 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161165, z172=20, z173=1412000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_14130():
    """Navi mesh change of hidden door in boss room 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161175, z172=20, z173=1413000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_14140():
    """Navi mesh change of hidden door in boss room 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_16_x60(z171=10161180, z172=20, z173=1414000, z174=0, z175=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_15000():
    """Boss: Forgotten Sinner_Battle"""
    """State 0,2: Is the poly drama replay event over?"""
    assert EventEnded(15010) != 0
    """State 3: [Preset] Boss: Forgotten Sinner Battle_SubState"""
    assert (event_m10_16_x218(z21=116000086, z22=1500000, z23=1016010, z24=116020085, z25=5, z26=848,
            z27=101, mode1=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_16_15010():
    """Boss: Forgotten Sinner_Poly Play"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m10_16_x33(z208=10160602, z209=101610, z210=116000087, z211=1501000, z212=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_15020():
    """Boss: Forgotten Sinner _ Zako Launch"""
    """State 0,2: [Preset] Forgotten Sinner_Zako Launch_SubState"""
    assert event_m10_16_x188(z52=1016010, z53=848)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_16000():
    """Boss: Gargoyle (Zakobos) _Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_16_x9(z221=116000091, z222=1600000, z223=1600000, z224=103, z225=1016020, z226=116020090,
            mode8=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_16_16010():
    """Boss: Gargoyle statues starting sequentially"""
    """State 0,6: [Preset] Sequentially activated gargoyle image_SubState"""
    assert event_m10_16_x192(z46=116000091, z47=1016020, z48=100, z49=116020092, z50=1, z51=2)
    """State 2: [Preset] Sequentially activated gargoyle image_1_SubState"""
    assert event_m10_16_x192(z46=116000091, z47=1016020, z48=100, z49=116020092, z50=10, z51=1)
    """State 3: [Preset] Sequentially activated gargoyle image_2_SubState"""
    assert event_m10_16_x192(z46=116000091, z47=1016020, z48=90, z49=116020092, z50=10, z51=1)
    """State 4: [Preset] Sequentially activated gargoyle image_3_SubState"""
    assert event_m10_16_x192(z46=116000091, z47=1016020, z48=70, z49=116020092, z50=10, z51=1)
    """State 5: [Preset] Sequentially activated gargoyle image_4_SubState"""
    assert event_m10_16_x192(z46=116000091, z47=1016020, z48=50, z49=116020092, z50=10, z51=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_17000():
    """One-way door of the round tower"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m10_16_x6(z237=0, z238=1101, z239=1700000, z240=116000057)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_17010():
    """OBJ blocking a one-way door"""
    """State 0,2: [Preset] OBJ_SubState that blocks a one-way door"""
    assert event_m10_16_x208(z29=10161550, z30=116000057)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18010():
    """The lock door that opens with `` jail key '' _ 2"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000041)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18030():
    """The lock door_4 that opens with the key of the prison_4"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000043)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18050():
    """The lock door_6 that opens with the key of the prison_6"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000045)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18060():
    """The key door to open with the key of the prison _7"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000046)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18120():
    """The key door to open with the key of the prison _13"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000052)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18130():
    """Key door to open with `` jail key '' _ 14"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000053)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_18140():
    """Key door to open with `` jail key '' _ 15"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50800000, z244=116000054)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_19000():
    """Navi-mesh changes after removing the petrified fossil"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_16_x77(z142=1900000, z143=0, z144=2, z145=0, z146=102741)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_22000():
    """Rolling flame barrels_1F staircase"""
    """State 0,2: [Preset] Rolling flame barrel_1F staircase_SubState"""
    assert event_m10_16_x179(z57=2200000, z58=2200010, z59=10164900, z60=116020013, z61=9990, z62=116000011)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_23000():
    """One door open from the beginning"""
    """State 0,2: Make one door open"""
    ChangeObjState(10160401, 74)
    assert CompareObjStateId(10160401, 30, 0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_23010():
    """Lock door that is open from the beginning"""
    """State 0,2: Keep the key door open"""
    ChangeObjState(10160431, 74)
    DisableObjKeyGuide(10160431, 1)
    assert CompareObjStateId(10160431, 30, 0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_24000():
    """Blacksmith treasure chest"""
    """State 0,3: Event end judgment"""
    assert EventEnded(111374) != 0
    """State 4: [Preset] Blacksmith Treasure Box_SubState"""
    call = event_m10_16_x200(z37=10165150, z38=165, z39=103790, z40=104290)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_16_25000():
    """End bonfire _ sinner"""
    """State 0,3: [Lib] [Preset] End special bonfire_SubState"""
    assert event_m10_16_x102(z126=10162200, z127=100300)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_26000():
    """Torture lift_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_Relief_SubState"""
    assert event_m10_16_x113(z111=10162020, z112=30, z113=116000020, z114=32)
    """State 3: [Lib] [Preset] Elevator_Initialization_Relief_2_SubState"""
    assert event_m10_16_x113(z111=10162021, z112=31, z113=116000021, z114=33)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_26010():
    """Torture lift"""
    """State 0,2: [Lib] [Preset] Torture lift_operation_SubState"""
    assert (event_m10_16_x45(z193=26000, z194=10162020, z195=10162021, z196=30, z197=2600003, z198=2600002,
            z199=2600001, z200=2600000))
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_26020():
    """Torture lift_action judgment"""
    """State 0,2: [Lib] [Preset] Torture lift_Action judgment_SubState"""
    assert (event_m10_16_x49(z187=10162020, z188=10162021, z189=2600003, z190=2600002, z191=2600001,
            z192=2600000))
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_27000():
    """Elevator (former / hidden port)"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_16_x16(z160=10161610, z161=2700010, z162=2700000, z163=10161601, z164=10161600)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_27010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z218=10161610, z219=10161601, z220=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_27020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_16_x21(z218=10161610, z219=10161600, z220=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_28000():
    """Key door that opens with "old keys" """
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_16_x5(z241=1005, z242=1105, z243=50840000, z244=116000055)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_29000():
    """Launching enemies with matryoshka destruction_1"""
    """State 0,2: [Preset] Launch enemy by destroying Matryoshka_SubState"""
    assert event_m10_16_x222(z19=10161700, z20=116020025)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_29010():
    """Launching enemies with matryoshka destruction_2"""
    """State 0,2: [Preset] Launch enemy by destroying Matryoshka_SubState"""
    assert event_m10_16_x222(z19=10161701, z20=116020026)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_30000():
    """Open door"""
    """State 0,2: [Preset] Open door_SubState"""
    assert event_m10_16_x226(z18=10160420)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_80000():
    """Rebirth Fire 01_ Prison Stop"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016000, z152=1016099)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_81000():
    """Regenerative fire 02_Left room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016100, z152=1016199)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_82000():
    """Regenerative fireworks 03_ The broken tower that the outer wall has advanced (hawk warp point)"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016200, z152=1016299)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_83000():
    """Reproduction of fire 04_ on the outer wall ahead of the Kanemori area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016300, z152=1016399)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_84000():
    """Regeneration of fire 05_after the flame barrel destruction wall"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016400, z152=1016499)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_85000():
    """Rebirth of Fire 06_Refectory after Warrior in Boss Mirror"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016500, z152=1016599)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_87000():
    """Regeneration of fire 08_ outside the tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_16_x72(z151=1016700, z152=1016799)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_87010():
    """Shop lineup expansion_forgotten sinners"""
    """State 0,2: [Lib] [Preset] Shop Lineup_SubState"""
    # bonfire:16685:The Saltfort
    assert event_m10_16_x107(bonfire1=16685, z122=116000086, z123=101102)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_90000():
    """Trophy_Sinner Light"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_16_x103(z124=100300, z125=6)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_x0(z254=0, z255=0, z256=10040000, z257=200000):
    """[Lib] Warp between maps after poly play
    z254: Pre-warp poly play ID
    z255: Poly Play ID after Warp
    z256: Map ID
    z257: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z254, z255, z256, z257, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_16_x1(z250=_, z251=_, z252=_, z253=_):
    """[Lib] NPC: Grave Placement: General purpose
    z250: Death map: Global event flag
    z251: Tomb: OBJ instance ID
    z252: Tomb move to: Generator ID
    z253: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z250, 1)
    IsGraveGeneratable(8, z253, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z251, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z251, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_16_x2(z247=_, z248=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z247: Global: death flag
    z248: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z248, 10, 0)
    CompareObjState(1, z248, 20, 0)
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
    IsObjSearched(0, z248)
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

def event_m10_16_x3(z245=_, z246=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z245: Area other flags: Ghost appearance
    z246: Area other flags: Conversation start
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
    SetEventFlag(z245, 1)
    CompareEventFlag(0, z245, 1)
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
    SetEventFlag(z246, 1)
    CompareEventFlag(0, z246, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_16_x4(z245=_, z246=_, z247=_, z248=_, z249=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z245: Ghost Appearance: Area Other Flag
    z246: Conversation start: Area and other flags
    z247: Death: Global event flag
    z248: Tomb: OBJ instance ID
    z249: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z249, 1, 0)
    CompareEventFlag(9, z245, 1)
    CompareObjState(9, z248, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z246, 1)
        CompareEventFlag(0, z246, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_16_x2(z247=z247, z248=z248, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_16_x3(z245=z245, z246=z246, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_16_x5(z241=1005, z242=1105, z243=_, z244=_):
    """[Lib] Item specified door unlocking_2
    z241: Text ID when opened
    z242: Text ID when not opened
    z243: item
    z244: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z243, z241, z242, z244, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x6(z237=0, z238=1101, z239=1700000, z240=116000057):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z237: Text ID when opened
    z238: Text ID when not opened
    z239: Point ID
    z240: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z239, 0, z237, z238, z240, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x7(z229=102481, z230=102482, z231=102483, z232=102485, z233=102490, z234=102486, z235=102487,
                    z236=102488):
    """[Lib] NPC: Woman Knight: Appearance Judgment
    z229: Sub 1 encountering: Global event flag
    z230: During sub-2 encounter: Global event flag
    z231: Sub 3 encountering: Global event flag
    z232: Generation stop: Global event flag
    z233: Appearance permission: Global event flag
    z234: Sub 1 generation stop: Global event flag
    z235: Sub 2 generation stop: Global event flag
    z236: Sub 3 generation stop: Global event flag
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
            CompareEventFlag(0, z232, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 2: Appearance determination: Judgment while encountering other maps"""
                CompareEventFlag(8, z229, 1)
                CompareEventFlag(8, z234, 0)
                CompareEventFlag(9, z230, 1)
                CompareEventFlag(9, z235, 0)
                CompareEventFlag(10, z231, 1)
                CompareEventFlag(10, z236, 0)
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
                        SetEventFlag(z233, 1)
                        CompareEventFlag(0, z233, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
        """State 3: Appearance judgment: Appearance impossible"""
        SetEventFlag(z233, 0)
        CompareEventFlag(0, z233, 0)
        assert ConditionGroup(0)
    """State 5: Appearance determination: System: Event end"""
    Label('L0')
    EndMachine()

def event_m10_16_x8(z227=90, z228=104192):
    """[Lib] NPC: Death determination: General purpose
    z227: Generator ID
    z228: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z228, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z227)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z228, 1)
            CompareEventFlag(0, z228, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_16_x9(z221=_, z222=_, z223=_, z224=_, z225=_, z226=_, mode8=0):
    """[Lib] [Preset] Boss Battle Start
    z221: Boss destruction flag
    z222: Start point ID
    z223: End point ID
    z224: Sound ID
    z225: Boss Battle ID
    z226: Other flags for logic
    mode8: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_16_x10(z221=z221)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_16_x11(z222=z222, z223=z223)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_16_x12(z224=z224, z225=z225, z226=z226)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_16_x13()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_16_x14(z225=z225)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_16_x15(z224=z224, z225=z225, z226=z226, mode8=mode8)
    """State 7: End state"""
    return 0

def event_m10_16_x10(z221=_):
    """[Reproduction] Boss Battle_Start
    z221: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z221) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_16_x11(z222=_, z223=_):
    """[Condition] Boss Battle_Start
    z222: Start point ID
    z223: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z222, z223, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z222, z223, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x12(z224=_, z225=_, z226=_):
    """[Execution] Boss Battle_Start
    z224: Sound ID
    z225: Boss Battle ID
    z226: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z224)
    """State 1: Boss battle start notification"""
    StartBossFight(z225)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z226, 1)
    """State 4: End state"""
    return 0

def event_m10_16_x13():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x14(z225=_):
    """[Condition] Boss Battle_End Judgment
    z225: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z225, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x15(z224=_, z225=_, z226=_, mode8=0):
    """[Execute] Boss Battle_End
    z224: Sound ID
    z225: Boss Battle ID
    z226: Other flags for logic
    mode8: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z226, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z225)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode8) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z224)
    """State 5: End state"""
    return 0

def event_m10_16_x16(z160=_, z161=_, z162=_, z163=_, z164=_):
    """[Lib] [Preset] Elevator
    z160: OBJ instance ID of the elevator
    z161: On elevator point ID_
    z162: Elevator point ID_below
    z163: Upper lever OBJ instance ID
    z164: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_16_x17()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_16_x18(z160=z160, z161=z161, z162=z162, z163=z163, z164=z164)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_16_x66(z160=z160, z162=z162)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_16_x65(z160=z160, z161=z161)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_16_x19(z160=z160, z161=z161)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_16_x20(z160=z160, z162=z162)
    """State 7: End state"""
    return 0

def event_m10_16_x17():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x18(z160=_, z161=_, z162=_, z163=_, z164=_):
    """[Condition] Elevator
    z160: Elevator OBJ instance ID
    z161: On elevator point ID_
    z162: Elevator point ID_below
    z163: Upper lever OBJ instance ID
    z164: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z160, 10, 0)
    CompareObjState(1, z160, 40, 0)
    CompareObjState(2, z160, 80, 0)
    CompareObjState(2, z160, 41, 0)
    CompareObjState(3, z160, 70, 0)
    CompareObjState(3, z160, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z162, z162, 1)
        CompareObjState(0, z163, 74, 0)
        CompareObjState(0, z163, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z161, z161, 1)
        CompareObjState(0, z164, 74, 0)
        CompareObjState(0, z164, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_16_x19(z160=_, z161=_):
    """[Execution] Elevator_Rise
    z160: Elevator OBJ instance ID
    z161: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z160, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z160, 30, 0)
    IsPlayerInsidePoint(8, z161, z161, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z160, 71)
    assert CompareObjStateId(z160, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_16_x20(z160=_, z162=_):
    """[Execution] Elevator_Descent
    z160: Elevator OBJ instance ID
    z162: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z160, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z160, 41, 0)
    IsPlayerInsidePoint(8, z162, z162, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z160, 81)
    assert CompareObjStateId(z160, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_16_x21(z218=_, z219=_, z220=_):
    """[Lib] [Preset] Elevator lever
    z218: OBJ instance ID of the elevator
    z219: Lever OBJ instance ID
    z220: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_16_x22()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_16_x23(z218=z218, z219=z219, z220=z220)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_16_x24(z218=z218, z219=z219, z220=z220)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_16_x25(z218=z218, z219=z219, z220=z220)
    """State 5: Rerun"""
    return 0

def event_m10_16_x22():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x23(z218=_, z219=_, z220=_):
    """[Condition] Elevator lever_use judgment
    z218: OBJ instance ID of the elevator
    z219: Lever OBJ instance ID
    z220: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z218, z220, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_16_x24(z218=_, z219=_, z220=_):
    """[Execution] Elevator lever_Key guide valid
    z218: OBJ instance ID of the elevator
    z219: Lever OBJ instance ID
    z220: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z219, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z218, z220, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x25(z218=_, z219=_, z220=_):
    """[Execute] Elevator lever_key guide disabled
    z218: OBJ instance ID of the elevator
    z219: Lever OBJ instance ID
    z220: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z219, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z218, z220, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x26(z216=116000005):
    """[Lib] [Reproduction] Elevator_Initialization
    z216: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(z216) != 0:
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

def event_m10_16_x28(z214=10161020, z215=40, z216=116000005, z217=40):
    """[Lib] [Execution] Elevator_Initialization
    z214: Elevator OBJ instance ID
    z215: Initial position OBJ state ID
    z216: Initialization completion flag
    z217: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z214, z215)
    assert CompareObjStateId(z214, z217, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z216, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x29(z214=10161020, z215=40, z216=116000005, z217=40):
    """[Lib] [Preset] Elevator_Initialization
    z214: Elevator OBJ instance ID
    z215: Initial position OBJ state ID
    z216: Initialization completion flag
    z217: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m10_16_x26(z216=z216)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m10_16_x27()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m10_16_x28(z214=z214, z215=z215, z216=z216, z217=z217)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m10_16_x30(z210=116000087):
    """[Reproduction] Boss Battle_Poly Play Replay
    z210: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z210) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_16_x31(z208=10160602):
    """[Condition] Boss Battle_Poly Play Replay
    z208: Changed Navimesh of wall 1 to destroy with flame barrel
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z208, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x32(z209=101610, z210=116000087, z211=1501000, z213=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z209: Poly play ID
    z210: Poly drama played flag
    z211: Warp point ID
    z213: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z209, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z210, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z211)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_16_x33(z208=10160602, z209=101610, z210=116000087, z211=1501000, z212=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z208: White door instance ID
    z209: Poly play ID
    z210: Poly drama played flag
    z211: Warp point ID
    z212: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m10_16_x30(z210=z210)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m10_16_x31(z208=z208)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m10_16_x32(z209=z209, z210=z210, z211=z211, z213=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_16_x34(z203=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z203: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_16_x35(z203=z203)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_16_x39(z203=z203)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_16_x40()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_16_x36(z203=z203, mode7=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_16_x37(z203=z203, z205=38, z206=3, z207=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_16_x38(z203=z203, z204=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_16_x35(z203=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z203: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z203, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z203, 10)
        assert CompareObjStateId(z203, 10, 0)
    elif CompareObjStateId(z203, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z203, 74, 1) and CompareObjStateId(z203, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_16_x36(z203=_, mode7=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z203: Object instance ID
    mode7: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z203)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode7) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_16_x37(z203=_, z205=38, z206=3, z207=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z203: Object instance ID
    z205: Key guide type
    z206: Event action
    z207: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z203, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z203, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z203, 30)
        assert CompareObjStateId(z203, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z203, z205, z206)
        assert PlayerIsInEventAction(z206) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z206, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z203, 74, 0)
        CompareObjState(1, z203, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z207)
            assert CompareObjStateId(z203, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z203, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_16_x38(z203=_, z204=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z203: Object instance ID
    z204: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z203, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_16_x39(z203=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z203: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z203, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x40():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x41(z201=_, val3=_):
    """[Reproduction] Hidden door 1_face SFX
    z201: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z201, 20, 0):
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

def event_m10_16_x42(z201=_):
    """[Conditions] Hidden door 1_Face SFX
    z201: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z201, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x43(z201=_, val3=_, z202=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z201: OBJ instance ID of the bug key
    val3: Event light ID
    z202: Light fade time
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
        SetPointLightEnabled(val3, 1, z202)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_16_x44(z201=_, val3=_, z202=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z201: OBJ instance ID of the bug key
    val3: Event light ID
    z202: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_16_x41(z201=z201, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_16_x42(z201=z201)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_16_x43(z201=z201, val3=val3, z202=z202, val4=val4)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_16_x45(z193=26000, z194=10162020, z195=10162021, z196=30, z197=2600003, z198=2600002, z199=2600001,
                     z200=2600000):
    """[Lib] [Preset] Torture lift
    z193: Initialization event ID
    z194: Reference lift_object instance ID
    z195: Mirror lift_object instance ID
    z196: Safety time
    z197: Reference lift point_on
    z198: Reference lift point_below
    z199: Mirror lift point_on
    z200: Mirror lift point_bottom
    """
    """State 0,2: [Reproduction] Torture lift_operation_SubState"""
    assert event_m10_16_x46(z193=z193)
    """State 3: [Condition] Torture lift_operation_SubState"""
    call = event_m10_16_x47(z194=z194, z195=z195, z197=z197, z198=z198, z199=z199, z200=z200)
    if call.Get() == 0:
        """State 4: [Execution] Torture lift_operation_SubState"""
        assert event_m10_16_x48(z194=z194, z195=z195, z196=z196, z200=z200, z197=z197)
    elif call.Get() == 1:
        """State 5: [Execution] Torture lift_operation_2_SubState"""
        assert event_m10_16_x48(z194=z195, z195=z194, z196=z196, z200=z200, z197=z197)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_16_x46(z193=26000):
    """[Lib] [Reproduction] Torture lift_operation
    z193: Initialization event ID
    """
    """State 0,2: [Compatible with SEQ17677] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 1: Whether the event has ended"""
    assert EventEnded(z193) != 0
    """State 3: End state"""
    return 0

def event_m10_16_x47(z194=10162020, z195=10162021, z197=2600003, z198=2600002, z199=2600001, z200=2600000):
    """[Lib] [Condition] Torture lift _operation
    z194: Reference lift_object instance ID
    z195: Mirror lift_object instance ID
    z197: Reference lift point_on
    z198: Reference lift point_below
    z199: Mirror lift point_on
    z200: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z194, 32, 0)
    IsPlayerInsidePoint(8, z197, z197, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z194, 33, 0)
    IsPlayerInsidePoint(9, z198, z198, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(1, 9)
    CompareObjState(10, z195, 32, 0)
    IsPlayerInsidePoint(10, z199, z199, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z195, 33, 0)
    IsPlayerInsidePoint(11, z200, z200, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(0, 11)
    if ConditionGroup(0):
        """State 2: Standard is from top to bottom"""
        return 0
    elif ConditionGroup(1):
        """State 3: Mirror from top to bottom"""
        return 1

def event_m10_16_x48(z194=_, z195=_, z196=30, z200=2600000, z197=2600003):
    """[Lib] [execution] torture lift
    z194: Top lift_object instance ID
    z195: Lower lift_object instance ID
    z196: Safety time
    z200: Point start
    z197: End of point
    """
    """State 0,1: Execution"""
    ChangeObjState(z194, 70)
    ChangeObjState(z195, 71)
    """State 2: Waiting for next start"""
    CompareObjState(8, z195, 32, 0)
    CompareObjState(8, z194, 33, 0)
    IsPlayerInsidePoint(8, z200, z197, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    CompareStateTime(1, z196, 3, z196)
    SetConditionGroup(1, 8)
    assert HostConditionGroup(1)
    """State 3: End state"""
    return 0

def event_m10_16_x49(z187=10162020, z188=10162021, z189=2600003, z190=2600002, z191=2600001, z192=2600000):
    """[Lib] [Preset] Torture lift_action judgment
    z187: Reference lift_object instance ID
    z188: Mirror lift_object instance ID
    z189: Reference lift point_on
    z190: Reference lift point_below
    z191: Mirror lift point_on
    z192: Mirror lift point_bottom
    """
    """State 0,1: [Reproduction] Torture lift_action judgment_empty_SubState"""
    assert event_m10_16_x50()
    """State 4: [Condition] Torture lift_Action determination_Start determination_SubState"""
    call = event_m10_16_x51(z187=z187, z188=z188, z189=z189, z190=z190, z191=z191, z192=z192)
    if call.Get() == 1:
        """State 2: [Execution] Torture lift_Action judgment_Action start_SubState"""
        assert event_m10_16_x52(z187=z187)
        """State 7: [Reproduction] Torture lift_action judgment_empty_2_SubState"""
        assert event_m10_16_x50()
        """State 5: [Condition] Torture lift_Action judgment_End judgment_SubState"""
        assert event_m10_16_x53(z187=z187, z189=z189, z190=z190)
        """State 3: [Execution] Torture lift_Action judgment_Action end_SubState"""
        assert event_m10_16_x54(z187=z187, z189=z189, z190=z190)
    elif call.Get() == 0:
        """State 6: [Execution] Torture Lift_Action Judgment_Action Start_2_SubState"""
        assert event_m10_16_x52(z187=z188)
        """State 8: [Reproduction] Torture lift_Action judgment_Empty_3_SubState"""
        assert event_m10_16_x50()
        """State 10: [Condition] Torture lift_Action judgment_End judgment_2_SubState"""
        assert event_m10_16_x53(z187=z188, z189=z191, z190=z192)
        """State 9: [Execution] Torture lift_Action judgment_Action end_2_SubState"""
        assert event_m10_16_x54(z187=z188, z189=z191, z190=z192)
    """State 11: End state"""
    return 0

def event_m10_16_x50():
    """[Lib] [reproduction] Torture lift_action judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x51(z187=10162020, z188=10162021, z189=2600003, z190=2600002, z191=2600001, z192=2600000):
    """[Lib] [Condition] Torture lift_Action judgment_Start judgment
    z187: Reference lift_object instance ID
    z188: Mirror lift_object instance ID
    z189: Reference lift point_on
    z190: Reference lift point_below
    z191: Mirror lift point_on
    z192: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z187, 70, 0)
    IsPlayerInsidePoint(8, z189, z189, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z187, 71, 0)
    IsPlayerInsidePoint(9, z190, z190, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(0, 9)
    CompareObjState(10, z188, 70, 0)
    IsPlayerInsidePoint(10, z191, z191, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z188, 71, 0)
    IsPlayerInsidePoint(11, z192, z192, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(1, 11)
    if ConditionGroup(0):
        """State 3: Standard"""
        return 1
    elif ConditionGroup(1):
        """State 2: mirror"""
        return 0

def event_m10_16_x52(z187=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action start
    z187: Lift_object instance ID
    """
    """State 0,1: Action request"""
    ObjAnimationPlayerControlRequest(z187, 34, 10)
    """State 2: End state"""
    return 0

def event_m10_16_x53(z187=_, z189=_, z190=_):
    """[Lib] [Condition] Torture lift_Action judgment_End judgment
    z187: Lift_object instance ID
    z189: Lift point_on
    z190: Lift point_down
    """
    """State 0,1: Wait"""
    CompareObjState(8, z187, 32, 0)
    CompareObjState(9, z187, 33, 0)
    SetConditionGroup(0, 8)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Finish"""
    return 0

def event_m10_16_x54(z187=_, z189=_, z190=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action end
    z187: Lift_object instance ID
    z189: Lift point_on
    z190: Lift point_down
    """
    """State 0,1: Action request"""
    EndPlayerActionRequest()
    """State 2: Wait"""
    IsPlayerInsidePoint(0, z189, z189, 1)
    IsPlayerInsidePoint(0, z190, z190, 1)
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

def event_m10_16_x57(z184=10162000, z185=150, z186=10166490):
    """[Lib] [execute] OBJ attach
    z184: Parent OBJ instance ID
    z185: Parent Damipoli ID
    z186: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z184, z185, z186)
    """State 2: End state"""
    return 0

def event_m10_16_x58(z184=10162000, z185=150, z186=10166490):
    """[Lib] [Preset] OBJ attach
    z184: Parent OBJ instance ID
    z185: Parent Damipoli ID
    z186: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m10_16_x55()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m10_16_x56()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m10_16_x57(z184=z184, z185=z185, z186=z186)
    """State 4: End state"""
    return 0

def event_m10_16_x59(z176=_, z177=_, z178=15, z179=_, z180=_, z181=1600, z182=_, z183=_):
    """[Lib] Character: Petrochemical: Key guide
    z176: generator
    z177: Death: Global event flag
    z178: Event action
    z179: Petrified: Area and other flags
    z180: Petrified: Global event flag
    z181: Key guide parameters
    z182: Petrification start state ID
    z183: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z176, z182, 0)
    CompareEventStatus(8, z183, 1, 0)
    CompareEventFlag(2, z179, 1)
    CompareEventFlag(3, z180, 1)
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
    CreateKeyGuideArea(34, z181)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z176)
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
                PlayerActionRequest(z178)
                IsPlayerPlayingMotion(0, z178, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z179, 1)
                CompareEventFlag(0, z179, 1)
                SetEventFlag(z180, 1)
                CompareEventFlag(1, z180, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z178, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_16_x60(z171=_, z172=20, z173=_, z174=0, z175=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z171: Object instance ID
    z172: OBJ state ID
    z173: Navimesh switching point ID
    z174: Additional attributes
    z175: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_16_x61(z171=z171, z172=z172, z173=z173, z175=z175, z174=z174)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_16_x62(z171=z171, z172=z172, z173=z173)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_16_x63(z171=z171, z172=z172, z173=z173, z174=z174, z175=z175)
    """State 4: End state"""
    return 0

def event_m10_16_x61(z171=_, z172=20, z173=_, z175=2, z174=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z171: Target OBJ instance ID
    z172: Target OBJ state ID
    z173: Navimesh switching point ID
    z175: Additional attributes
    z174: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z171, z172, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z173, z175)
        DeleteNavimeshAttribute(z173, z174)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_16_x62(z171=_, z172=20, z173=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z171: Target OBJ instance ID
    z172: Target OBJ state ID
    z173: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z171, z172, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x63(z171=_, z172=20, z173=_, z174=0, z175=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z171: Target OBJ instance ID
    z172: Target OBJ state ID
    z173: Navimesh switching point ID
    z174: Additional attributes
    z175: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z173, z174)
    DeleteNavimeshAttribute(z173, z175)
    """State 2: End state"""
    return 0

def event_m10_16_x64(z165=102500, z166=546, z167=104190, z168=61, z169=103690, z170=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z165: White Phantom can appear: Global event flag
    z166: White Phantom: Generator ID
    z167: Death: Global event flag
    z168: Body: Generator group ID
    z169: Hostile: Global event flag
    z170: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z166)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z167, 1)
        CompareEventFlag(1, z169, 1)
        CompareEventFlag(2, z165, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z166)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z167, 1)
            CompareEventFlag(1, z169, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z166)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z167, 1)
            CompareEventFlag(1, z169, 1)
            HasNpcPhantomSpawned(2, z166, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z168, 0)
                HasNpcPhantomSpawned(0, z166, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z166)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m10_16_x65(z160=_, z161=_):
    """[Execution] Elevator_Return switch after lift
    z160: Elevator OBJ instance ID
    z161: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z160, 30, 0)
    IsPlayerInsidePoint(8, z161, z161, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z160, 71)
    assert CompareObjStateId(z160, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_16_x66(z160=_, z162=_):
    """[Execution] Elevator_Return switch after descending
    z160: Elevator OBJ instance ID
    z162: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z160, 41, 0)
    IsPlayerInsidePoint(8, z162, z162, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z160, 81)
    assert CompareObjStateId(z160, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_16_x67(z154=_, z155=_, z156=_, z157=_, z158=0, z159=_):
    """[Lib] Character: Petrified: Appearance setting
    z154: Generator ID
    z155: Death: Global event flag
    z156: Petrified: Area and other flags
    z157: Petrified: Global event flag
    z158: Startup state
    z159: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z154)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z155, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z156, 1)
                CompareEventFlag(1, z157, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z154, z158)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()

def event_m10_16_x68(z153=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z153: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z153)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_16_x69():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x70(z151=_, z152=_):
    """[Lib] [execute] Rebirth fire
    z151: Flag start ID
    z152: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z151, z152, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x71():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x72(z151=_, z152=_):
    """[Lib] [Preset] Rebirth
    z151: Flag start ID
    z152: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_16_x69()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_16_x71()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_16_x70(z151=z151, z152=z152)
    """State 4: End state"""
    return 0

def event_m10_16_x73(z147=116000086, z148=102498, z149=204, z150=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z147: Defeat Boss 1: Area and other flags
    z148: Summon Achievement: Global Event Flag
    z149: Summon achievement count: global variable
    z150: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z148, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z147, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z149, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z149, NpcInfoValue(z150, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z148, 1)
                CompareEventFlag(0, z148, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m10_16_x74(z145=_, z146=_, z144=2, z143=0, z142=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z145: Other flags
    z146: Global flag
    z144: Additional attributes
    z143: Delete attribute
    z142: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z145) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z146) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z142, z144)
        DeleteNavimeshAttribute(z142, z143)
        """State 3: Flag OFF"""
        return 0

def event_m10_16_x75(z145=_, z146=_):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z145: Other flags
    z146: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z145, 1)
    CompareEventFlag(0, z146, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_16_x76(z142=_, z143=0, z144=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z142: Navimesh switching point ID
    z143: Additional attributes
    z144: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z142, z143)
    DeleteNavimeshAttribute(z142, z144)
    """State 2: End state"""
    return 0

def event_m10_16_x77(z142=_, z143=0, z144=2, z145=_, z146=_):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z142: Navimesh switching point ID
    z143: Additional attributes
    z144: Delete attribute
    z145: Other flags
    z146: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_16_x74(z145=z145, z146=z146, z144=z144, z143=z143, z142=z142)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_16_x75(z145=z145, z146=z146)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_16_x76(z142=z142, z143=z143, z144=z144)
    """State 4: End state"""
    return 0

def event_m10_16_x78(z138=10002000, z139=540, z140=0, z141=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z138: Summon range
    z139: Generator ID
    z140: Appearance: Minimum time
    z141: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z138, z138, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z140, 3, z141)
        IsPlayerInsidePoint(1, z138, z138, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z139)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_16_x79(z134=10001000, z135=541, z136=0, z137=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z134: Summon range
    z135: Generator ID
    z136: Appearance: Minimum time
    z137: Appearance: Maximum time
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
            DeleteNpcPhantom(z135)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z134, z134, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z136, 3, z137)
                IsPlayerInsidePoint(1, z134, z134, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z135)
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

def event_m10_16_x80(z132=_, z133=_):
    """[Lib] [Preset] Get trophy
    z132: Acquisition trigger_other flags
    z133: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z132) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z132, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z133)
    """State 4: End state"""
    return 0

def event_m10_16_x81(z131=100300):
    """[Lib] [Reproduction] Terminal Lighthouse
    z131: Lighting completion flag
    """
    """State 0,1: Is it already lit?"""
    if GetEventFlag(z131) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_16_x82(z130=10162200):
    """[Lib] [Conditions] Terminal lighthouse
    z130: Lighthouse OBJ instance ID
    """
    """State 0,1: Waiting for lighting"""
    CompareObjState(0, z130, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x83(z130=10162200, action1=2022, z131=100300):
    """[Lib] [execution] terminal lighthouse
    z130: Lighthouse OBJ instance ID
    action1: Text ID
    z131: Lighting completion flag
    """
    """State 0,1: Production FE display"""
    OpenPresentationWindow(20)
    """State 4,2: Event message display"""
    # action:2022:"A primal bonfire was rekindled"
    DisplayEventMessage(action1, 0, 0, 0)
    """State 3: Lighting completion flag ON"""
    SetEventFlag(z131, 1)
    """State 5: End state"""
    return 0

def event_m10_16_x84(z130=10162200, action1=2022, z131=100300):
    """[Lib] [Preset] Terminal Lighthouse
    z130: Lighthouse OBJ instance ID
    action1: Text ID
    z131: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] Terminal Lighthouse_SubState"""
    call = event_m10_16_x81(z131=z131)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Terminal lighthouse_SubState"""
        assert event_m10_16_x82(z130=z130)
        """State 2: [Lib] [Execution] Terminal Lighthouse_SubState"""
        assert event_m10_16_x83(z130=z130, action1=action1, z131=z131)
    """State 4: End state"""
    return 0

def event_m10_16_x85(z129=12000, mode4=1, mode5=1, mode6=1):
    """[Lib] [Preset] Kanemori_Net reception
    z129: Event sound ID for bell
    mode4: Wait 1 after SE playback
    mode5: Wait 2 after SE playback
    mode6: Wait 3 after playing SE
    """
    """State 0,1: [Lib] [Reproduction] Kanemori_Net reception_SubState"""
    assert event_m10_16_x86()
    """State 3: [Lib] [Conditions] Kanemori_Net reception_SubState"""
    assert event_m10_16_x87()
    """State 2: [Lib] [Execution] Kanemori_Net reception_SubState"""
    assert event_m10_16_x88(z129=z129, mode4=mode4, mode5=mode5, mode6=mode6)
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

def event_m10_16_x88(z129=12000, mode4=1, mode5=1, mode6=1):
    """[Lib] [Execution] Kanemori_Net reception_Playback
    z129: Event sound ID for bell
    mode4: Wait 1 after SE playback
    mode5: Wait 2 after SE playback
    mode6: Wait 3 after playing SE
    """
    """State 0,1: Ring the bell: first time"""
    PlaySoundAtPoint(z129)
    assert (GetStateTime() > mode4) != 0
    """State 4: Ring the bell: second time"""
    PlaySoundAtPoint(z129)
    assert (GetStateTime() > mode5) != 0
    """State 5: Ring the bell: 3rd time"""
    PlaySoundAtPoint(z129)
    assert (GetStateTime() > mode6) != 0
    """State 2: Clear reception history"""
    ClearBellKeeperRingingHistory()
    """State 3: Clear confirmation of received history"""
    IsBellKeeperRingingHistoryCleared(0, 0)
    assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_16_x89(z128=10161023):
    """[Lib] [reproduction] Kanemori _ judgment of lever use of Kanemori spirit
    z128: Lever OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 4: Host: Exit"""
        return 1
    else:
        """State 2: Disable key guide"""
        DisableObjKeyGuide(z128, 1)
        """State 3: Guest: Spirit guard"""
        return 0

def event_m10_16_x90():
    """[Lib] [Conditions] Kanemori _ Judgment spirit lever usage judgment"""
    """State 0,1: Has the host died?"""
    IsHostDead(0, 1)
    assert ConditionGroup(0)
    """State 2: Bell guard spirit: lever operation possible"""
    return 0

def event_m10_16_x91(z128=10161023):
    """[Lib] [Execution] Kanemori _ Judgment Spirit use lever judgment
    z128: Lever OBJ instance ID
    """
    """State 0,1: Activate key guide"""
    DisableObjKeyGuide(z128, 0)
    """State 2: Finish"""
    return 0

def event_m10_16_x92(z128=10161023):
    """[Lib] [Preset] Kanemori _ Judgment Spirit's lever usage judgment
    z128: Lever OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] Kanemori _ Jerusalem Spirit Lever Use Judgment_SubState"""
    call = event_m10_16_x89(z128=z128)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Conditions] Kanemori_Bellguard spirit lever usage judgment_SubState"""
        assert event_m10_16_x90()
        """State 2: [Lib] [Execution] Kanemori_Legend of lever guard_SubState"""
        assert event_m10_16_x91(z128=z128)
    """State 4: Finish"""
    return 0

def event_m10_16_x93(z115=10161023, z116=10161050, mode3=0, z117=0, z118=0, z119=10161051, z120=10160620,
                     z121=400000):
    """[Lib] [Preset] Bell guard_bell lever
    z115: Lever_OBJ instance ID
    z116: Bell 1_OBJ instance ID
    mode3: Bell 2_OBJ instance ID
    z117: Bell 3_OBJ instance ID
    z118: Bell 4_OBJ instance ID
    z119: Door OBJ instance ID
    z120: Changed Navimesh of wall 1 to destroy with flame barrel
    z121: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Bell guard_Lever that bell rings_SubState"""
    call = event_m10_16_x94(z119=z119, z120=z120, z121=z121)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        Goto('L0')
    """State 3: [Lib] [Conditions] Bell guard_Lever that rings bell_SubState"""
    call = event_m10_16_x95(z115=z115)
    if call.Get() == 0:
        """State 4: [Lib] [execution] bell guard_bell lever_host_SubState"""
        assert (event_m10_16_x96(z115=z115, z116=z116, mode3=mode3, z117=z117, z118=z118, z119=z119,
                z120=z120, z121=z121))
    elif call.Get() == 1:
        """State 2: [Lib] [execution] bell guard_bell lever_guest_SubState"""
        assert event_m10_16_x97(z115=z115, z116=z116, mode3=mode3, z117=z117, z118=z118)
    """State 7: Rerun"""
    return 0
    """State 6: [Lib] [Conditions] Bell guard_Lever that rings bell_Guest_SubState"""
    Label('L0')
    assert event_m10_16_x108(z119=z119)
    """State 5: [Lib] [Execution] Bell guard_Lever that bell rings_Navigation change_SubState"""
    assert event_m10_16_x109(z119=z119, z121=z121)
    """State 8: Guest termination"""
    return 1

def event_m10_16_x94(z119=10161051, z120=10160620, z121=400000):
    """[Lib] [reproduction] bell guard _ bell ringing lever
    z119: Door OBJ instance ID
    z120: Changed Navimesh of wall 1 to destroy with flame barrel
    z121: Navigation change point ID
    """
    """State 0,3: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is the door open?"""
    if CompareObjStateId(z119, 10, 0):
        """State 2: White door key guide disabled"""
        DisableWhiteDoorKeyGuide(z120, 1)
    else:
        """State 4: Navimesh change: passable"""
        DeleteNavimeshAttribute(z121, 2)
    """State 5: host"""
    return 0
    """State 6: Guest termination"""
    Label('L0')
    return 1

def event_m10_16_x95(z115=10161023):
    """[Lib] [Conditions] Bell guard_bell lever
    z115: OBJ instance ID of the lever
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z115, 74, 0)
    CompareObjState(0, z115, 84, 0)
    SetConditionGroup(8, 0)
    IsHostDead(8, 0)
    CompareObjState(1, z115, 74, 0)
    CompareObjState(1, z115, 84, 0)
    SetConditionGroup(9, 1)
    IsHostDead(9, 1)
    if ConditionGroup(8):
        """State 2: Host is alive: Host processing"""
        return 0
    elif ConditionGroup(9):
        """State 3: Host dies: guest processing"""
        return 1

def event_m10_16_x96(z115=10161023, z116=10161050, mode3=0, z117=0, z118=0, z119=10161051, z120=10160620,
                     z121=400000):
    """[Lib] [Execution] Kanemori_Lever that rings the bell_Host
    z115: Lever_OBJ instance ID
    z116: Bell 1_OBJ instance ID
    mode3: Bell 2_OBJ instance ID
    z117: Bell 3_OBJ instance ID
    z118: Bell 4_OBJ instance ID
    z119: Door OBJ instance ID
    z120: Changed Navimesh of wall 1 to destroy with flame barrel
    z121: Navigation change point ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z115, 1)
    """State 9: Ringing bell judgment"""
    if (not mode3) != 0:
        """State 10: Ring bell 1"""
        ChangeObjState(z116, 70)
        """State 8: Bell 1 animation playback judgment"""
        CompareObjState(0, z116, 70, 0)
        assert ConditionGroup(0)
        """State 4: Bell 1 animation end"""
        CompareObjState(0, z116, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z116, 70)
        ChangeObjState(mode3, 70)
        ChangeObjState(z117, 70)
        ChangeObjState(z118, 70)
        """State 11: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z116, 70, 0)
        CompareObjState(0, mode3, 70, 0)
        CompareObjState(0, z117, 70, 0)
        CompareObjState(0, z118, 70, 0)
        assert ConditionGroup(0)
        """State 12: Bell 1 ~ 4 anime end judgment"""
        CompareObjState(8, z116, 10, 0)
        CompareObjState(8, mode3, 10, 0)
        CompareObjState(8, z117, 10, 0)
        CompareObjState(8, z118, 10, 0)
        assert ConditionGroup(8)
    """State 5: Judgment of door"""
    CompareObjState(0, z119, 10, 0)
    CompareObjState(1, z119, 10, 1)
    if ConditionGroup(0):
        """State 6: Open the door: 70"""
        ChangeObjState(z119, 70)
        """State 7: Door animation end judgment"""
        CompareObjState(0, z119, 20, 0)
        assert ConditionGroup(0)
        """State 14: Navimesh change: passable"""
        DeleteNavimeshAttribute(z121, 2)
        """State 13: Enable key guide for white door"""
        DisableWhiteDoorKeyGuide(z120, 0)
    elif ConditionGroup(1):
        pass
    """State 3: Lever key guide enabled"""
    DisableObjKeyGuide(z115, 0)
    """State 15: End state"""
    return 0

def event_m10_16_x97(z115=10161023, z116=10161050, mode3=0, z117=0, z118=0):
    """[Lib] [execution] Kanemori _ Lever singing bell _ Guest
    z115: Lever_OBJ instance ID
    z116: Bell 1_OBJ instance ID
    mode3: Bell 2_OBJ instance ID
    z117: Bell 3_OBJ instance ID
    z118: Bell 4_OBJ instance ID
    """
    """State 0,5: Ringing bell judgment"""
    if (not mode3) != 0:
        """State 6: Ring bell 1"""
        ChangeObjState(z116, 70)
        """State 3: Ringing the bell_server information"""
        NotifyServerOfBellKeeperRinging()
        """State 4: Bell 1 animation playback judgment"""
        CompareObjState(0, z116, 70, 0)
        assert ConditionGroup(0)
        """State 2: Bell 1 animation end"""
        CompareObjState(0, z116, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z116, 70)
        ChangeObjState(mode3, 70)
        ChangeObjState(z117, 70)
        ChangeObjState(z118, 70)
        """State 8: Bell ringing_server information transmission_2"""
        NotifyServerOfBellKeeperRinging()
        """State 9: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z116, 70, 0)
        CompareObjState(0, mode3, 70, 0)
        CompareObjState(0, z117, 70, 0)
        CompareObjState(0, z118, 70, 0)
        assert ConditionGroup(0)
        """State 7: Anime end judgment for bells 1 to 4_2"""
        CompareObjState(8, z116, 10, 0)
        CompareObjState(8, mode3, 10, 0)
        CompareObjState(8, z117, 10, 0)
        CompareObjState(8, z118, 10, 0)
        assert ConditionGroup(8)
    """State 10: End state"""
    return 0

def event_m10_16_x98(z127=100300):
    """[Lib] [Reproduction] Special bonfire at the end
    z127: Lighting completion flag
    """
    """State 0,1: Is the bonfire already lit?"""
    if GetEventFlag(z127) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_16_x99(z126=10162200):
    """[Lib] [Condition] Terminal special fire
    z126: Bonfire OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z126)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x100(z126=10162200, z127=100300):
    """[Lib] [Execution] End special bonfire_ignition
    z126: Bonfire OBJ instance ID
    z127: Lighting completion flag
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
        ChangeObjState(z126, 70)
        """State 3: Lighting completion flag ON"""
        SetEventFlag(z127, 1)
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

def event_m10_16_x101(z126=10162200, z127=100300):
    """[Lib] [Execution] End special bonfire_warp
    z126: Bonfire OBJ instance ID
    z127: Lighting completion flag
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
        assert event_m10_16_x0(z254=0, z255=0, z256=10040000, z257=200000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m10_16_x102(z126=10162200, z127=100300):
    """[Lib] [Preset] Special bonfire at the end
    z126: Bonfire OBJ instance ID
    z127: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] End special bonfire _SubState"""
    call = event_m10_16_x98(z127=z127)
    if call.Get() == 1:
        """State 5: [Lib] [Condition] End special bonfire_2_SubState"""
        assert event_m10_16_x99(z126=z126)
        """State 2: [Lib] [Execution] End special bonfire_warp_SubState"""
        assert event_m10_16_x101(z126=z126, z127=z127)
    elif call.Get() == 0:
        """State 4: [Lib] [Condition] End special bonfire_SubState"""
        assert event_m10_16_x99(z126=z126)
        """State 3: [Lib] [Execution] End special bonfire_At ignition_SubState"""
        assert event_m10_16_x100(z126=z126, z127=z127)
    """State 6: Rerun"""
    return 0

def event_m10_16_x103(z124=100300, z125=6):
    """[Lib] [Preset] Trophy Acquisition_Global
    z124: Acquisition trigger_global flag
    z125: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z124) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z124, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z125)
    """State 4: End state"""
    return 0

def event_m10_16_x104(z123=101102):
    """[Lib] [Reproduction] Shop Lineup
    z123: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(z123) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m10_16_x105(bonfire1=16685, z122=116000086):
    """[Lib] [Conditions] Shop lineup
    bonfire1: Bonfire ID
    z122: Boss destruction flag
    """
    """State 0,1: Is the total number of laps 2 or more and is the boss destroyed?"""
    # bonfire:16685:The Saltfort
    CompareGameCycleForBonfire(8, bonfire1, 2, 2, 3)
    CompareEventFlag(8, z122, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_16_x106(z123=101102):
    """[Lib] [execution] shop lineup
    z123: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(z123, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x107(bonfire1=16685, z122=116000086, z123=101102):
    """[Lib] [Preset] Shop Lineup
    bonfire1: Bonfire ID
    z122: Boss destruction flag
    z123: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_16_x104(z123=z123)
    if call.Get() == 0:
        """State 3: [Lib] [Conditions] Shop lineup_SubState"""
        assert event_m10_16_x105(bonfire1=bonfire1, z122=z122)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_16_x106(z123=z123)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_16_x108(z119=10161051):
    """[Lib] [Conditions] Kanemori _ Lever that rings the bell _ Guest
    z119: Door OBJ instance ID
    """
    """State 0,1: Waiting for the door to open"""
    CompareObjState(0, z119, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x109(z119=10161051, z121=400000):
    """[Lib] [execution] bell guard_bell change lever_navigation change
    z119: Door OBJ instance ID
    z121: Navigation change point ID
    """
    """State 0,1: Navimesh change: passable"""
    DeleteNavimeshAttribute(z121, 2)
    """State 2: End state"""
    return 0

def event_m10_16_x110(z113=_, z111=_, z112=_, z114=_):
    """[Lib] [Reproduction] Elevator_Initialization_Relief
    z113: Initialization completion flag
    z111: Elevator OBJ instance ID
    z112: Initial position OBJ state ID
    z114: OBJ state after initialization
    """
    """State 0,4: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 1: Already initialized?"""
    if GetEventFlag(z113) != 0:
        pass
    else:
        Goto('L0')
    """State 2: [Remedy] Is it in the initial state?"""
    if CompareObjStateId(z111, 10, 0):
        """State 3: Elevator initialization"""
        ChangeObjState(z111, z112)
        assert CompareObjStateId(z111, z114, 0)
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

def event_m10_16_x112(z111=_, z112=_, z113=_, z114=_):
    """[Lib] [Run] Elevator_Initialization_Relief
    z111: Elevator OBJ instance ID
    z112: Initial position OBJ state ID
    z113: Initialization completion flag
    z114: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z111, z112)
    assert CompareObjStateId(z111, z114, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z113, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x113(z111=_, z112=_, z113=_, z114=_):
    """[Lib] [Preset] Elevator_Initialization_Relief
    z111: Elevator OBJ instance ID
    z112: Initial position OBJ state ID
    z113: Initialization completion flag
    z114: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_Relief_SubState"""
    call = event_m10_16_x110(z113=z113, z111=z111, z112=z112, z114=z114)
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
        assert event_m10_16_x112(z111=z111, z112=z112, z113=z113, z114=z114)
    """State 4: End state"""
    return 0

def event_m10_16_x114(z101=10162210):
    """[Lib] [BEST] [Condition] Andyel_Appearance_Termination
    z101: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z101)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x115(z101=10162210, z104=100761, z103=100742):
    """[Lib] [BEST] [Execution] Andyel_Appearance_Termination
    z101: Ander OBJ instance ID
    z104: Conversation start flag
    z103: Encounter flag
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
        SetEventFlag(z103, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z101, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z101, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(z104, 1)
        """State 7: End state"""
        return 0

def event_m10_16_x116(z102=100740):
    """[Lib] [BEST] [Conditions] Ander_Destruction_End_Termination
    z102: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, z102, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x117(z101=10162210):
    """[Lib] [BEST] [Execution] Andel_Deletion_End
    z101: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z101, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z101, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x118(z101=10162210, z102=100740, z104=100761, z103=100742):
    """[Lib] [BEST] [Reproduction] Anderl_Appearance determination_Termination
    z101: Ander OBJ instance ID
    z102: Event completion flag
    z104: Conversation start flag
    z103: Encounter flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been completed?"""
        if GetEventFlag(z102) != 0:
            pass
        else:
            """State 3: Was it in conversation?"""
            if GetEventFlag(z104) != 0:
                pass
            else:
                """State 4: Was it in the middle of appearance?"""
                if CompareObjStateId(z101, 72, 0):
                    pass
                elif CompareObjStateId(z101, 73, 0):
                    pass
                elif CompareObjStateId(z101, 70, 0):
                    pass
                elif CompareObjStateId(z101, 30, 0):
                    pass
                else:
                    """State 7: Was the appearance confirmed?"""
                    if GetEventFlag(z103) != 0:
                        """State 8: Standby state: 30"""
                        ChangeObjState(z101, 30)
                    else:
                        """State 11: Appearance determination"""
                        return 2
                """State 5: Wait for completion"""
                assert CompareObjStateId(z101, 30, 0)
                """State 6: Conversation start flag ON"""
                SetEventFlag(z104, 1)
            """State 10: Disappearance judgment"""
            return 1
    """State 9: Finish"""
    return 0

def event_m10_16_x119():
    """[Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x120(z101=10162210, z102=100740, z103=100742, z104=100761, z105=100300, z106=100360,
                      z107=100400, z108=100461):
    """[Lib] [BEST] [Preset] Andyel_Termination
    z101: Ander OBJ instance ID
    z102: Event completion flag
    z103: Encounter flag
    z104: Conversation start flag
    z105: Lighting completion flag
    z106: Bonfire lighting judgment flag ①
    z107: Bonfire lighting judgment flag ②
    z108: Bonfire lighting judgment flag ③
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Ander _ Appearance determination _ Termination _ SubState"""
    call = event_m10_16_x118(z101=z101, z102=z102, z104=z104, z103=z103)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty _ SubState"""
        Label('L0')
        assert event_m10_16_x119()
        """State 9: [Lib] [BEST] [Conditions] Ander_Deletion_Termination_Termination_SubState"""
        assert event_m10_16_x116(z102=z102)
        """State 6: [Lib] [BEST] [Execution] Andel_Destruction_End_SubState"""
        assert event_m10_16_x117(z101=z101)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Ander_Appearance determination_Termination_SubState"""
        call = event_m10_16_x127(z101=z101, z105=z105, z106=z106, z107=z107, z108=z108, z103=z103)
        if call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Andel_Appearance determination_Termination_SubState"""
            assert event_m10_16_x128(z101=z101)
            """State 1: [Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty_SubState"""
            assert event_m10_16_x126()
            """State 7: [Lib] [BEST] [Condition] Ander_Appearance_Termination_SubState"""
            assert event_m10_16_x114(z101=z101)
            """State 4: [Lib] [BEST] [Execution] Andel_Appearance_Termination_SubState"""
            call = event_m10_16_x115(z101=z101, z104=z104, z103=z103)
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

def event_m10_16_x121(z109=10162210, z110=10162200):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z109: Ander OBJ instance ID
    z110: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z109, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z110, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_16_x122(z109=10162210):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z109: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z109, 10, 0)
    CompareObjState(0, z109, 31, 0)
    CompareObjState(0, z109, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_16_x123(z109=10162210, z110=10162200):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z109: Ander OBJ instance ID
    z110: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z110, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z109, 10, 1)
    CompareObjState(8, z109, 31, 1)
    CompareObjState(8, z109, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_16_x124(z109=10162210, z110=10162200):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z109: Ander OBJ instance ID
    z110: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z110, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z109, 10, 0)
    CompareObjState(0, z109, 31, 0)
    CompareObjState(0, z109, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_16_x125(z109=10162210, z110=10162200):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z109: Ander OBJ instance ID
    z110: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_16_x121(z109=z109, z110=z110)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_16_x122(z109=z109)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_16_x123(z109=z109, z110=z110)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_16_x124(z109=z109, z110=z110)
    """State 6: Rerun"""
    return 1

def event_m10_16_x126():
    """[Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x127(z101=10162210, z105=100300, z106=100360, z107=100400, z108=100461, z103=100742):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_Termination
    z101: Ander OBJ instance ID
    z105: Lighting completion flag
    z106: Bonfire lighting judgment flag ①
    z107: Bonfire lighting judgment flag ②
    z108: Bonfire lighting judgment flag ③
    z103: Andyur encounter flag
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z105, 0)
    CompareEventFlag(8, z106, 1)
    CompareEventFlag(8, z107, 1)
    CompareEventFlag(8, z108, 1)
    CompareEventFlag(8, z103, 0)
    CompareEventFlag(0, z103, 1)
    if ConditionGroup(8):
        """State 2: End state"""
        return 0
    elif ConditionGroup(0):
        """State 3: Rerun"""
        return 1

def event_m10_16_x128(z101=10162210):
    """[Lib] [BEST] [Execution] Andel_Appearance determination_Termination
    z101: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z101, 31)
    """State 2: End state"""
    return 0

def event_m10_16_x129(z99=10162210, z100=10162200):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z99: Ander OBJ instance ID
    z100: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z99, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z100, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_16_x130(z99=10162210):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z99: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z99, 10, 0)
    CompareObjState(0, z99, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_16_x131(z99=10162210, z100=10162200):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z99: Ander OBJ instance ID
    z100: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z100, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z99, 10, 1)
    CompareObjState(8, z99, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_16_x132(z99=10162210, z100=10162200):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z99: Ander OBJ instance ID
    z100: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z100, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z99, 10, 0)
    CompareObjState(0, z99, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_16_x133(z99=10162210, z100=10162200):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z99: Ander OBJ instance ID
    z100: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_16_x129(z99=z99, z100=z100)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_16_x130(z99=z99)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_16_x131(z99=z99, z100=z100)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_16_x132(z99=z99, z100=z100)
    """State 5: Rerun"""
    return 0

def event_m10_16_x134(z77=116020060, z79=116000061):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z77: Lottery determination flag
    z79: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z79) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z77) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_16_x135(z78=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z78: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z78, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_16_x136(z77=116020060, z80=3, z81=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z77: Lottery determination flag
    z80: Number of appearance judgment points
    z81: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z77, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z80)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z81, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_16_x137(z77=116020060, z78=14, z79=116000061, z80=3, z81=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z77: Lottery determination flag
    z78: Random number comparison value
    z79: Defeat flag
    z80: Number of appearance judgment points
    z81: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_16_x134(z77=z77, z79=z79)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_16_x135(z78=z78)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_16_x136(z77=z77, z80=z80, z81=z81)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_16_x154(z77=z77, z81=z81)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_16_x138(val2=_, z96=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z96: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z96) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_16_x139(z92=_, z93=0, z94=10):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z92: Appearance judgment point ID
    z93: Minimum appearance time
    z94: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z92, z92, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z93, 3, z94)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_16_x140(z95=932, z97=_, z98=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z95: Generator ID
    z97: Appearance start point ID
    z98: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z95, z97, z98)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z95)
    """State 4: Finish"""
    return 0

def event_m10_16_x141(z89=116000061):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z89: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z89) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_16_x142(z92=_, z93=0, z94=10, z95=932, val2=_, z96=10, z97=_, z98=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z92: Intrusion detection point ID
    z93: Minimum appearance time
    z94: Maximum time to appear
    z95: Generator ID
    val2: Appearance judgment number
    z96: Lottery result point variable
    z97: Appearance start point ID
    z98: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_16_x138(val2=val2, z96=z96)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_16_x139(z92=z92, z93=z93, z94=z94)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_16_x140(z95=z95, z97=z97, z98=z98)
    """State 4: Finish"""
    return 0

def event_m10_16_x143(z90=932, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z90: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z90)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_16_x144(z89=116000061, z91=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z89: Defeat flag
    z91: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z89, 1)
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
                    SetEventFlag(z91, 1)
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

def event_m10_16_x145(z89=116000061, z90=932, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z89: Defeat flag
    z90: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_16_x141(z89=z89)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_16_x143(z90=z90, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_16_x144(z89=z89, z91=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_16_x144(z89=z89, z91=102755)
    """State 5: End state"""
    return 0

def event_m10_16_x146():
    """[Lib] [DC] [Reproduction] Character deletion judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x147(z84=_, z85=7, z86=1, z87=0):
    """[Lib] [DC] [Condition] Character deletion judgment
    z84: Generator ID
    z85: Shared flag ID
    z86: Comparison value
    z87: Judgment comparison type
    """
    """State 0,2: Has the target character been generated?"""
    IsChrActive(0, z84, 1)
    assert ConditionGroup(0)
    """State 1: Has the target character completed the return action?"""
    CompareChrEzStateValue(0, z84, z85, z86, z87)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m10_16_x148(z84=_, z88=0):
    """[Lib] [DC] [Execution] Character deletion judgment
    z84: Generator ID
    z88: Whether to treat it as death
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z84, z88)
    """State 2: End state"""
    return 0

def event_m10_16_x149(z84=_, z85=7, z86=1, z87=0, z88=0):
    """[Lib] [DC] [Preset] Character deletion judgment
    z84: Generator ID
    z85: Shared flag ID
    z86: Comparison value
    z87: Judgment comparison type
    z88: Whether to treat it as death
    """
    """State 0,1: [Lib] [DC] [Reproduction] Character deletion judgment_empty_SubState"""
    assert event_m10_16_x146()
    """State 3: [Lib] [DC] [Condition] Character deletion judgment_SubState"""
    assert event_m10_16_x147(z84=z84, z85=z85, z86=z86, z87=z87)
    """State 2: [Lib] [DC] [Execution] Character deletion judgment_SubState"""
    assert event_m10_16_x148(z84=z84, z88=z88)
    """State 4: End state"""
    return 0

def event_m10_16_x150(z82=_, z83=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z82: Generator ID
    z83: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z82, z83)
    """State 2: End state"""
    return 0

def event_m10_16_x151(z82=_, z83=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z82: Generator ID
    z83: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z82, z83, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_16_x152(z82=_):
    """[Lib] [DC] [Condition] Transparent characters
    z82: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z82)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x153(z82=_, z83=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z82: Generator ID
    z83: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_16_x151(z82=z82, z83=z83)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_16_x152(z82=z82)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_16_x150(z82=z82, z83=z83)
    """State 4: End state"""
    return 0

def event_m10_16_x154(z77=116020060, z81=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z77: Lottery determination flag
    z81: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z77, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z81, 0)
    """State 3: End state"""
    return 0

def event_m10_16_x155(z74=116000086):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z74: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z74) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_16_x156(z75=848):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z75: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z75, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x157(z76=116020089):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z76: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z76, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x158(z74=116000086, z75=848, z76=116020089):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z74: Boss destruction flag
    z75: Boss generator ID
    z76: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_16_x155(z74=z74)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_16_x156(z75=z75)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_16_x157(z76=z76)
    """State 4: End state"""
    return 0

def event_m10_16_x159():
    """[Reproduction] Lighting the boss room"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x160(z71=_):
    """[Condition] Boss room lighting
    z71: Igniter instance ID
    """
    """State 0,1: Ignition stand lighting standby"""
    CompareObjState(0, z71, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x161(z72=_, z73=_):
    """[Execute] Lighting the boss room
    z72: Damipoli ① Instance ID
    z73: Damipoli ② Instance ID
    """
    """State 0,1: OBJ state transition: Damipoli for fire riding"""
    ChangeObjState(z72, 71)
    ChangeObjState(z73, 70)
    """State 2: End state"""
    return 0

def event_m10_16_x162(z71=_, z72=_, z73=_):
    """[Preset] Boss room lighting
    z71: Igniter instance ID
    z72: Damipoli ① Instance ID
    z73: Damipoli ② Instance ID
    """
    """State 0,1: [Reproduction] Lighting the boss room_SubState"""
    assert event_m10_16_x159()
    """State 2: [Condition] Boss room lighting_SubState"""
    assert event_m10_16_x160(z71=z71)
    """State 3: [Execution] Lighting the boss room_SubState"""
    assert event_m10_16_x161(z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m10_16_x163(z63=_, z64=_, z66=_, z65=_):
    """[Reproduction] Iron lattice that opens with a lever
    z63: Object instance ID of the iron lattice OBJ
    z64: Lever OBJ object instance ID
    z66: Navigation mesh change
    z65: State ID of the state where the iron lattice OBJ is fully opened
    """
    """State 0,1: State determination of iron grid"""
    if CompareObjStateId(z63, 10, 1):
        """State 3: Disable key guide of lever"""
        DisableObjKeyGuide(z64, 1)
        """State 4: Is the iron grid open?"""
        assert CompareObjStateId(z63, z65, 0)
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z66, 2)
        """State 6: Opened"""
        return 1
    else:
        """State 5: Not open"""
        return 0

def event_m10_16_x164(z33=_):
    """[Conditions] Iron grid that opens with lever
    z33: Lever OBJ object instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z33, 74, 0)
    CompareObjState(0, z33, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x165(z63=_, z65=_, z66=_, z64=_):
    """[Execution] Iron grid that opens with lever
    z63: Object instance ID of the iron lattice OBJ
    z65: State ID of the state where the iron lattice OBJ is fully opened
    z66: Navigation mesh change
    z64: Lever OBJ object instance ID
    """
    """State 0,3: Disable key guide of lever"""
    DisableObjKeyGuide(z64, 1)
    """State 1: Iron lattice animation playback that opens with a lever"""
    ChangeObjState(z63, 70)
    """State 4: Is the iron grid open?"""
    CompareObjState(0, z63, z65, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z66, 2)
    """State 5: End state"""
    return 0

def event_m10_16_x166():
    """[Reproduction] Treasure corpse fall _ sky with yagura destruction"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x167(z70=10161300):
    """[Condition] Treasure corpse falls due to yagura destruction
    z70: Yagura instance ID
    """
    """State 0,1: Waiting for destruction of the tower"""
    IsObjBroken(0, z70, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x168(z68=10166010, z69=70):
    """[Execution] Treasure corpse falls due to yagura destruction
    z68: Instance ID of treasure corpse
    z69: Falling state ID
    """
    """State 0,1: Treasure corpse fall"""
    ChangeObjState(z68, z69)
    """State 2: End state"""
    return 0

def event_m10_16_x169(z67=116000086):
    """[Reproduction] Changing the lock ID of the boss room
    z67: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z67) != 0:
        """State 2: Returns lock on parameter"""
        ResetLockOnParameter()
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Not defeated"""
        return 0

def event_m10_16_x170(z3=116000086, z4=10161000, z5=10161001, z6=802000, z10=1016010):
    """[Condition] Change lock ID of boss room
    z3: Boss destruction flag
    z4: Right_Ignition table OBJ instance ID
    z5: Left_Ignition stand OBJ instance ID
    z6: Point ID
    z10: Boss Battle ID
    """
    """State 0,2: Did you invade points during the boss battle?"""
    IsPlayerInsidePoint(8, z6, z6, 1)
    IsEventBossBattle(8, z10, 1)
    assert ConditionGroup(8)
    """State 1: PC torch judgment and light lighting number judgment"""
    SetConditionGroup(0, 8)
    CompareObjState(8, z4, 20, 0)
    CompareObjState(8, z5, 20, 0)
    CompareObjState(1, z4, 20, 0)
    CompareObjState(2, z5, 20, 0)
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

def event_m10_16_x171(z8=626001, z5=_, z3=116000086):
    """[Execute] Changing the lock ID of the boss room
    z8: Lock-on parameter ID
    z5: OBJ instance ID waiting for lighting
    z3: Boss destruction flag
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z8)
    """State 2: Waiting for next lighting or waiting for use of torches or waiting to destroy boss"""
    CompareObjState(0, z5, 20, 0)
    CompareEventFlag(0, z3, 1)
    IsPlayerUsingTorch(0, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x172(z3=116000086, z4=10161000, z5=10161001, z6=802000, z7=626000, z8=626001, z9=626002,
                      z10=1016010):
    """[Preset] Changing the lock ID of the boss room
    z3: Boss destruction flag
    z4: Right_Ignition table OBJ instance ID
    z5: Left_Ignition stand OBJ instance ID
    z6: Point ID
    z7: Lock ID_short
    z8: Lock ID_
    z9: Lock ID_length
    z10: Boss Battle ID
    """
    """State 0,1: [Reproduction] Change lock ID of boss room_SubState"""
    assert event_m10_16_x169(z67=116000086) == 0
    """State 2: [Condition] Change lock ID of boss room_SubState"""
    call = event_m10_16_x170(z3=z3, z4=z4, z5=z5, z6=z6, z10=z10)
    if call.Get() == 0:
        """State 3: [Execution] Change lock ID of boss room_Both lights up_SubState"""
        assert event_m10_16_x173(z3=z3, z9=z9)
        """State 9: Finish"""
        return 1
    elif call.Get() == 4:
        """State 7: [Execution] Changing the lock ID of the boss room_Torchlight in use_SubState"""
        assert event_m10_16_x239(z9=z9, z4=z4, z5=z5, z3=z3)
    elif call.Get() == 1:
        """State 5: [Execution] Change lock ID of boss room_One side is lit_SubState"""
        assert event_m10_16_x171(z8=z8, z5=z5, z3=z3)
    elif call.Get() == 3:
        """State 6: [Execution] Change lock ID of boss room_One side is lit_2_SubState"""
        assert event_m10_16_x171(z8=z8, z5=z4, z3=z3)
    elif call.Get() == 2:
        """State 4: [Execution] Changing the lock ID of the boss room_Unlit_SubState"""
        assert event_m10_16_x174(z7=z7, z4=z4, z5=z5, z3=z3)
    """State 8: Rerun"""
    return 0

def event_m10_16_x173(z3=116000086, z9=626002):
    """[Execution] Change lock ID of boss room
    z3: Boss destruction flag
    z9: Lock-on parameter ID
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z9)
    """State 2: Waiting for boss destruction"""
    CompareEventFlag(0, z3, 1)
    assert ConditionGroup(0)
    """State 3: Returns lock on parameter"""
    ResetLockOnParameter()
    """State 4: End state"""
    return 0

def event_m10_16_x174(z7=626000, z4=10161000, z5=10161001, z3=116000086):
    """[Execute] Changing lock ID of boss room
    z7: Lock-on parameter ID
    z4: Right_Ignition table OBJ instance ID
    z5: Left_Ignition stand OBJ instance ID
    z3: Boss destruction flag
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z7)
    """State 2: Waiting for next lighting or waiting for use of torches or waiting to destroy boss"""
    SetConditionGroup(0, 8)
    CompareObjState(8, z4, 20, 0)
    IsPlayerUsingTorch(8, 0)
    SetConditionGroup(0, 9)
    CompareObjState(9, z5, 20, 0)
    IsPlayerUsingTorch(9, 0)
    CompareEventFlag(0, z3, 1)
    IsPlayerUsingTorch(0, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x175(z63=_, z64=_, z65=_, z66=_):
    """[Preset] Opening with a lever
    z63: Object instance ID of the iron lattice OBJ
    z64: Lever OBJ object instance ID
    z65: State ID of the state where the iron lattice OBJ is fully opened
    z66: Navigation mesh change
    """
    """State 0,1: [Reproduction] Iron lattice _SubState opened with lever"""
    call = event_m10_16_x163(z63=z63, z64=z64, z66=z66, z65=z65)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Conditions] Iron lattice that opens with lever_SubState"""
        assert event_m10_16_x164(z33=z64)
        """State 3: [Execution] Iron lattices opened by lever_SubState"""
        assert event_m10_16_x165(z63=z63, z65=z65, z66=z66, z64=z64)
    """State 4: End state"""
    return 0

def event_m10_16_x176(z59=10164900, z62=116000011):
    """[Reproduction] Rolling flame barrel _1F staircase
    z59: Barrel instance ID
    z62: Event execution judgment flag
    """
    """State 0,2: Was the event executed once?"""
    if GetEventFlag(z62) != 0:
        pass
    else:
        Goto('L0')
    """State 1: Flame barrel OBJ condition determination"""
    if CompareObjStateId(z59, 10, 0):
        """State 4: Executed_state transition"""
        return 1
    else:
        """State 5: Executed_End immediately"""
        return 2
    """State 3: Not executed"""
    Label('L0')
    return 0

def event_m10_16_x177(z57=2200000, z58=2200010, z61=9990):
    """[Conditions] Rolling flame barrel _1F staircase
    z57: Point ID when kicking
    z58: Point ID when not kicking
    z61: Generator ID of the enemy kicking the barrel
    """
    """State 0,1: Point determination and prison state determination"""
    IsPlayerInsidePoint(0, z57, z57, 1)
    CompareChrHpRatio(0, z61, 100, 1)
    IsPlayerInsidePoint(1, z58, z58, 1)
    IsChrDead(1, z61)
    if ConditionGroup(1):
        """State 3: Don't kick"""
        return 1
    elif ConditionGroup(0):
        """State 2: Kick"""
        return 0

def event_m10_16_x178(z60=116020013, z59=10164900, z62=116000011):
    """[Execution] Rolling flame barrel_1F stair_kick
    z60: Kicking action flag
    z59: Barrel instance ID
    z62: Event execution judgment flag
    """
    """State 0,1: Kicking action flag ON"""
    SetEventFlag(z60, 1)
    """State 4: Event execution flag ON"""
    SetEventFlag(z62, 1)
    """State 2: Time adjustment state"""
    assert (GetStateTime() > 0.5) != 0
    """State 3: Rolling _ misfire"""
    ChangeObjState(z59, 70)
    assert CompareObjStateId(z59, 20, 0)
    """State 5: End state"""
    return 0

def event_m10_16_x179(z57=2200000, z58=2200010, z59=10164900, z60=116020013, z61=9990, z62=116000011):
    """[Preset] Rolling flame barrel _1F staircase
    z57: Point ID when kicking
    z58: Point ID when not kicking
    z59: Barrel instance ID
    z60: Kicking action flag
    z61: Generator ID of the enemy kicking the barrel
    z62: Event execution judgment flag
    """
    """State 0,1: [Reproduction] Rolling flame barrel _1F staircase_SubState"""
    call = event_m10_16_x176(z59=z59, z62=z62)
    if call.Get() == 1:
        """State 4: [Execution] Rolling flame barrel_1F staircase_Do not kick_SubState"""
        Label('L0')
        assert event_m10_16_x180(z59=z59, z62=z62)
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Rolling flame barrel _1F staircase_SubState"""
        call = event_m10_16_x177(z57=z57, z58=z58, z61=z61)
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            """State 3: [Execution] Rolling flame barrel_1F staircase_kick_SubState"""
            assert event_m10_16_x178(z60=z60, z59=z59, z62=z62)
    """State 5: End state"""
    return 0

def event_m10_16_x180(z59=10164900, z62=116000011):
    """[Execution] Rolling flame barrel _1F staircase_Do not kick
    z59: Barrel instance ID
    z62: Event executed flag
    """
    """State 0,1: Transition to misfire / dynamic state: 30"""
    ChangeObjState(z59, 30)
    """State 2: Event execution flag ON"""
    SetEventFlag(z62, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x181(z54=_, z55=_, z56=_):
    """[Preset] Navimesh change due to yagura destruction
    z54: YAGURA OBJ instance ID
    z55: Point ID for changing Navimesh at the top of the tower
    z56: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: [Reproduction] Navi mesh change due to yagura destruction_SubState"""
    call = event_m10_16_x182(z54=z54)
    if call.Get() == 0:
        """State 2: [Condition] Navi mesh change due to yagura destruction_SubState"""
        assert event_m10_16_x183(z54=z54)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_16_x184(z55=z55, z56=z56)
    """State 4: End state"""
    return 0

def event_m10_16_x182(z54=_):
    """[Reproduction] Navi mesh change due to yagura destruction
    z54: YAGURA OBJ instance ID
    """
    """State 0,1: State determination of yagura OBJ"""
    if CompareObjStateId(z54, 20, 1):
        """State 2: Undestructed"""
        return 0
    else:
        """State 3: Destroyed"""
        return 1

def event_m10_16_x183(z54=_):
    """[Condition] Navi mesh change due to yagura destruction
    z54: YAGURA OBJ instance ID
    """
    """State 0,1: Yagura OBJ transition waiting"""
    CompareObjState(0, z54, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x184(z55=_, z56=_):
    """[Execution] Navi mesh change due to yagura destruction
    z55: Point ID for changing Navimesh at the top of the tower
    z56: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: Added navigating mesh attributes at the top of the tower"""
    AddNavimeshAttribute(z55, 2)
    """State 2: Navimesh attribute deletion at the bottom of the tower"""
    DeleteNavimeshAttribute(z56, 2)
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

def event_m10_16_x186(z52=1016010, z53=848):
    """[Condition] Forgotten Sinner _ Start Zako
    z52: Boss Battle ID
    z53: Generator ID
    """
    """State 0,1: Boss battle start waiting"""
    IsEventBossBattle(0, z52, 1)
    assert ConditionGroup(0)
    """State 2: Has the boss's HP dropped below 70%?"""
    CompareChrHpRatio(0, z53, 70, 5)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x187():
    """[Execution] Forgotten Sinner _ Start Zako"""
    """State 0,1: Zako start flag ON"""
    SetEventFlag(116020088, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x188(z52=1016010, z53=848):
    """[Preset] Forgotten Sinner _ Start Zako
    z52: Boss Battle ID
    z53: Generator ID
    """
    """State 0,1: [Reproduction] Forgotten Sinner_Zako Launch_SubState"""
    call = event_m10_16_x185()
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Forgotten Sinner_Zako Launch_SubState"""
        assert event_m10_16_x186(z52=z52, z53=z53)
        """State 2: [Execution] Forgotten Sinner_Zako Launch_SubState"""
        assert event_m10_16_x187()
    """State 4: End state"""
    return 0

def event_m10_16_x189(z46=116000091):
    """[Reproduction] Gargoyle image starting sequentially
    z46: Boss destruction flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z46) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Undefeated"""
        return 0

def event_m10_16_x190(z47=1016020, z48=_):
    """[Conditions] Gargoyle images starting sequentially
    z47: Boss Battle ID
    z48: HP ratio at startup
    """
    """State 0,2: Boss battle start waiting"""
    IsEventBossBattle(0, z47, 1)
    assert ConditionGroup(0)
    """State 1: Is the total HP less than ○○?"""
    CompareEventBossHpRatio(0, z47, 0, z48, 5)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x191(z49=116020092, z50=_, z51=_):
    """[Execution] Gargoyle images starting sequentially
    z49: Gargoyle start flag
    z50: Cool time
    z51: Wait time
    """
    """State 0,1: Gargoyle start flag ON"""
    SetEventFlag(z49, 1)
    """State 2: Cool time"""
    CompareStateTime(0, z50, 3, z50)
    assert ConditionGroup(0)
    """State 3: Gargoyle start flag OFF"""
    SetEventFlag(z49, 0)
    """State 4: Logic weight"""
    CompareStateTime(0, z51, 3, z51)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m10_16_x192(z46=116000091, z47=1016020, z48=_, z49=116020092, z50=_, z51=_):
    """[Preset] Gargoyle images starting sequentially
    z46: Boss destruction flag
    z47: Boss Battle ID
    z48: HP ratio at startup
    z49: Gargoyle start flag
    z50: Cool time
    z51: Wait time
    """
    """State 0,1: [Reproduction] Gargoyle image_SubState starting sequentially"""
    call = event_m10_16_x189(z46=z46)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Gargoyle image_SubState which starts sequentially"""
        assert event_m10_16_x190(z47=z47, z48=z48)
        """State 2: [Execution] Gargoyle image_SubState starting sequentially"""
        assert event_m10_16_x191(z49=z49, z50=z50, z51=z51)
    """State 4: End state"""
    return 0

def event_m10_16_x193(z41=10162000, z42=10162010, z43=116020015, z44=4, z45=116000016):
    """[Preset] Enemies appear from the well when stones are hit
    z41: 檻 OBJ instance ID
    z42: Stone OBJ instance ID
    z43: Enemy action start flag
    z44: Waiting time until enemy action starts
    z45: Enemy generation stop flag
    """
    """State 0,1: [Reproduction] Encroaching enemies from a well when a stone is hit _SubState"""
    call = event_m10_16_x194(z41=z41, z42=z42, z43=z43, z45=z45)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] When you hit a stone, an enemy entering the well from the well_SubState"""
        assert event_m10_16_x195(z42=z42)
        """State 3: [Execution] Encroachment of enemies from a well when hitting a stone_SubState"""
        assert event_m10_16_x196(z41=z41, z42=z42, z43=z43, z44=z44, z45=z45)
    """State 4: End state"""
    return 0

def event_m10_16_x194(z41=10162000, z42=10162010, z43=116020015, z45=116000016):
    """[Reproduction] Encroachment of enemies from wells when stones are hit
    z41: 檻 OBJ instance ID
    z42: Stone OBJ instance ID
    z43: Enemy action start flag
    z45: Enemy generation stop flag
    """
    """State 0,1: Is 檻 in the initial state?"""
    if CompareObjStateId(z41, 10, 1):
        """State 3: Change of state of transparent stone OBJ"""
        ChangeObjState(z42, 20)
        assert (GetStateTime() > 4) != 0
        """State 2: Turn on enemy action start flag"""
        SetEventFlag(z43, 1)
        """State 4: Enemy generation stop flag ON"""
        SetEventFlag(z45, 1)
        """State 6: Already in operation"""
        return 1
    else:
        """State 5: Not in operation"""
        return 0

def event_m10_16_x195(z42=10162010):
    """[Condition] When a stone is hit, an enemy-filled trap appears from the well
    z42: Stone OBJ instance ID
    """
    """State 0,1: Stone attack waiting"""
    IsObjDamaged(0, z42, -1, -1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x196(z41=10162000, z42=10162010, z43=116020015, z44=4, z45=116000016):
    """[Execution] When a stone is hit, an enemy-filled trap appears from the well
    z41: 檻 OBJ instance ID
    z42: Stone OBJ instance ID
    z43: Enemy action start flag
    z44: Waiting time until enemy action starts
    z45: Enemy generation stop flag
    """
    """State 0,1: 檻 rise"""
    ChangeObjState(z41, 70)
    ChangeObjState(z42, 20)
    """State 3: Judgment whether the waiting time until the enemy's action start has passed"""
    CompareStateTime(0, z44, 2, z44)
    assert ConditionGroup(0)
    """State 2: Turn on enemy action start flag"""
    SetEventFlag(z43, 1)
    """State 4: Enemy generation stop flag ON"""
    SetEventFlag(z45, 1)
    """State 5: End state"""
    return 0

def event_m10_16_x197(z37=10165150):
    """[Reproduction] Blacksmith Treasure Chest
    z37: Treasure chest OBJ instance ID
    """
    """State 0,1: Activate key guide for treasure chest"""
    DisableObjKeyGuide(z37, 0)
    """State 2: Start state judgment"""
    return 0

def event_m10_16_x198(z38=165, z39=103790, z40=104290):
    """[Conditions] Blacksmith treasure chest
    z38: Generator ID
    z39: Hostile flag
    z40: death flag
    """
    """State 0,1: Blacksmith start-up state determination"""
    CompareChrStartUpState(8, z38, 4, 0)
    IsChrActive(8, z38, 1)
    CompareEventFlag(1, z39, 1)
    CompareEventFlag(1, z40, 1)
    IsChrDead(1, z38)
    if ConditionGroup(1):
        """State 3: Blacksmith: Hostile or dead"""
        return 1
    elif ConditionGroup(8):
        """State 2: Blacksmith: Starting state"""
        return 0

def event_m10_16_x199(z37=10165150, z38=165):
    """[Execution] Blacksmith Treasure Box
    z37: Treasure chest OBJ instance parameters
    z38: Generator ID
    """
    """State 0,1: Disable treasure chest key guide"""
    DisableObjKeyGuide(z37, 1)
    """State 2: Was the startup state released?"""
    CompareChrStartUpState(0, z38, 4, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x200(z37=10165150, z38=165, z39=103790, z40=104290):
    """[Preset] Blacksmith Treasure Chest
    z37: Treasure chest OBJ instance parameters
    z38: Generator ID
    z39: Hostile flag
    z40: death flag
    """
    """State 0,1: [Reproduction] Blacksmith Treasure Box_SubState"""
    assert event_m10_16_x197(z37=z37)
    """State 3: [Conditions] Blacksmith Treasure Box_SubState"""
    call = event_m10_16_x198(z38=z38, z39=z39, z40=z40)
    if call.Get() == 0:
        """State 2: [Execution] Blacksmith Treasure Box_Waiting for Next Decision_SubState"""
        assert event_m10_16_x199(z37=z37, z38=z38)
        """State 5: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Execution] Blacksmith Treasure Box_Activation Only_SubState"""
        assert event_m10_16_x201(z37=z37, z38=z38)
        """State 6: Finish"""
        return 1

def event_m10_16_x201(z37=10165150, z38=165):
    """[Execution] Blacksmith's Treasure Box_Activation Only
    z37: Treasure chest OBJ instance parameters
    z38: Generator ID
    """
    """State 0,1: Activate key guide for treasure chest"""
    DisableObjKeyGuide(z37, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x202(z31=10161071, z32=10161072, z33=10161028, z34=203000, z35=203001, z36=30):
    """[Preset] Lattice open by lever
    z31: Object instance ID of foreground OBJ
    z32: Object instance ID of the back iron lattice OBJ
    z33: Lever OBJ object instance ID
    z34: Change front Navimesh
    z35: Navimesh change in the back
    z36: State ID of the state where the iron lattice OBJ is fully opened
    """
    """State 0,1: [Reproduction] Iron lattice_passage_SubState opened with lever"""
    call = event_m10_16_x203(z31=z31, z32=z32, z33=z33, z34=z34, z35=z35, z36=z36)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Conditions] Iron lattice that opens with lever_SubState"""
        assert event_m10_16_x164(z33=z33)
        """State 3: [Execution] Lattice open by lever_passage_SubState"""
        assert event_m10_16_x204(z31=z31, z32=z32, z36=z36, z34=z34, z35=z35, z33=z33)
    """State 4: End state"""
    return 0

def event_m10_16_x203(z31=10161071, z32=10161072, z33=10161028, z34=203000, z35=203001, z36=30):
    """[Reproduction] Opening with a lever
    z31: Object instance ID of foreground OBJ
    z32: Object instance ID of the back iron lattice OBJ
    z33: Lever OBJ object instance ID
    z34: Change front Navimesh
    z35: Navimesh change in the back
    z36: State ID of the state where the iron lattice OBJ is fully opened
    """
    """State 0,1: Judging the state of the front iron grid"""
    if CompareObjStateId(z31, 10, 1):
        pass
    else:
        Goto('L0')
    """State 3: Disable key guide of lever"""
    DisableObjKeyGuide(z33, 1)
    """State 7: Is the front iron grid open?"""
    assert CompareObjStateId(z31, z36, 0)
    """State 2: Delete previous Navimesh attribute"""
    DeleteNavimeshAttribute(z34, 2)
    """State 5: Determining the state of the iron bar"""
    if CompareObjStateId(z32, z36, 0):
        pass
    else:
        """State 6: Animation reproduction of the iron grid in the back"""
        ChangeObjState(z32, 70)
        """State 8: Is the iron bar in the back open?"""
        assert CompareObjStateId(z32, z36, 0)
    """State 4: Delete back Navi Mesh attribute"""
    DeleteNavimeshAttribute(z35, 2)
    """State 10: Opened"""
    return 1
    """State 9: Not open"""
    Label('L0')
    return 0

def event_m10_16_x204(z31=10161071, z32=10161072, z36=30, z34=203000, z35=203001, z33=10161028):
    """[Execution] Lattice open by lever
    z31: Object instance ID of foreground OBJ
    z32: Object instance ID of the back iron lattice OBJ
    z36: State ID of the state where the iron lattice OBJ is fully opened
    z34: Change front Navimesh
    z35: Navimesh change in the back
    z33: Lever OBJ object instance ID
    """
    """State 0,3: Disable key guide of lever"""
    DisableObjKeyGuide(z33, 1)
    """State 1: Animation playback of the front grid"""
    ChangeObjState(z31, 70)
    """State 6: Is the front iron grid open?"""
    CompareObjState(0, z31, z36, 0)
    assert ConditionGroup(0)
    """State 2: Delete previous Navimesh attribute"""
    DeleteNavimeshAttribute(z34, 2)
    """State 4: Animation reproduction of the iron grid in the back"""
    ChangeObjState(z32, 70)
    """State 7: Is the iron bar in the back open?"""
    CompareObjState(0, z32, z36, 0)
    assert ConditionGroup(0)
    """State 5: Delete back Navi Mesh attribute"""
    DeleteNavimeshAttribute(z35, 2)
    """State 8: End state"""
    return 0

def event_m10_16_x205():
    """[Reproduction] OBJ_sky blocking one-way door"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x206(z29=10161550):
    """[Conditions] OBJ blocking a one-way door
    z29: OBJ instance ID to be destroyed
    """
    """State 0,1: Is the target OBJ broken?"""
    IsObjBroken(0, z29, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x207(z30=116000057):
    """[Execution] OBJ blocking one-way door
    z30: One-way door flag
    """
    """State 0,1: One-way flag ON"""
    SetEventFlag(z30, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x208(z29=10161550, z30=116000057):
    """[Preset] OBJ blocking the one-way door
    z29: OBJ instance ID to be destroyed
    z30: One-way door flag
    """
    """State 0,1: [Reproduction] OBJ_Sky_SubState that blocks a one-way door"""
    assert event_m10_16_x205()
    """State 3: [Condition] OBJ_SubState that blocks a one-way door"""
    assert event_m10_16_x206(z29=z29)
    """State 2: [Execution] OBJ_SubState to block the one-way door"""
    assert event_m10_16_x207(z30=z30)
    """State 4: End state"""
    return 0

def event_m10_16_x209(z21=116000086):
    """[Reproduction] Forgotten Sinner Battle_Start
    z21: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z21) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_16_x210(z22=1500000, z28=1500000):
    """[Condition] Forgotten Sinner Battle_Start
    z22: Start point ID
    z28: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z22, z28, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z22, z28, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x211(z23=1016010, z24=116020085):
    """[Execute] Forgotten Sinner Battle_Start
    z23: Boss Battle ID
    z24: Other flags for logic
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z23)
    """State 2: Logic flag ON"""
    SetEventFlag(z24, 1)
    """State 3: End state"""
    return 0

def event_m10_16_x212():
    """[Reproduction] Boss BGM playback_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x213(z25=5, z26=848):
    """[Condition] Boss BGM playback
    z25: BGM playback start distance
    z26: Generator ID
    """
    """State 0,1: Did you approach the boss? Or did you give damage?"""
    CompareChrPlayerDistance(0, z26, z25, 5)
    CompareChrHpRatio(0, z26, 100, 4)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x214(z27=101, z23=1016010):
    """[Execute] Boss BGM playback
    z27: Sound ID
    z23: Boss Battle ID
    """
    """State 0,2: Did the boss die before playing BGM?"""
    IsEventBossKill(0, z23, 0, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z27)
    """State 3: End state"""
    return 0

def event_m10_16_x215():
    """[Reproduction] Forgotten Sinner Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x216(z23=1016010):
    """[Condition] Forgotten Sinner Battle_End Judgment
    z23: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z23, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x217(z27=101, z23=1016010, z24=116020085, mode1=0):
    """[Execute] Forgotten Sinner Battle_End
    z27: Sound ID
    z23: Boss Battle ID
    z24: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z24, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z23)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z27)
    """State 5: End state"""
    return 0

def event_m10_16_x218(z21=116000086, z22=1500000, z23=1016010, z24=116020085, z25=5, z26=848, z27=101,
                      mode1=0):
    """[Preset] Boss: Forgotten Sinner Battle
    z21: Boss destruction flag
    z22: Boss Battle Start Point ID
    z23: Boss Battle ID
    z24: Logic flag
    z25: BGM playback start distance
    z26: Generator ID
    z27: Sound ID
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Forgotten Sinner Battle_Start_SubState"""
    call = event_m10_16_x209(z21=z21)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Forgotten Sinner Battle_Start_SubState"""
        assert event_m10_16_x210(z22=z22, z28=z22)
        """State 3: [Execution] Forgotten Sinner Battle_Start_SubState"""
        assert event_m10_16_x211(z23=z23, z24=z24)
        """State 7: [Reproduction] Boss BGM playback_Sky_SubState"""
        assert event_m10_16_x212()
        """State 9: [Condition] Boss BGM playback_SubState"""
        assert event_m10_16_x213(z25=z25, z26=z26)
        """State 8: [Execution] Boss BGM playback_SubState"""
        assert event_m10_16_x214(z27=z27, z23=z23)
        """State 2: [Reproduction] Forgotten Sinner Battle_End_Sky_SubState"""
        assert event_m10_16_x215()
        """State 6: [Condition] Forgotten Sinner Battle_End Judgment_SubState"""
        assert event_m10_16_x216(z23=z23)
        """State 4: [Execution] Forgotten Sinner Battle_End_SubState"""
        assert event_m10_16_x217(z27=z27, z23=z23, z24=z24, mode1=mode1)
    """State 10: End state"""
    return 0

def event_m10_16_x219():
    """[Reproduction] Launching enemies by destroying Matryoshka _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x220(z19=_):
    """[Conditions] Enemies activated by matryoshka destruction
    z19: Matryoshka OBJ instance ID
    """
    """State 0,1: Matryoshka waiting for destruction"""
    IsObjBroken(0, z19, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x221(z20=_):
    """[Execution] Enemies activated by matryoshka
    z20: Enemy activation flag
    """
    """State 0,1: Enemy activation flag ON"""
    SetEventFlag(z20, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x222(z19=_, z20=_):
    """[Preset] Enemies activated by matryoshka destruction
    z19: Matryoshka OBJ instance ID
    z20: Enemy activation flag
    """
    """State 0,1: [Reproduction] Enemy starts with Matryoshka destruction_Sky_SubState"""
    assert event_m10_16_x219()
    """State 3: [Condition] Enemies activated by Matryoshka destruction_SubState"""
    assert event_m10_16_x220(z19=z19)
    """State 2: [Execution] Enemies activated by Matryoshka destruction_SubState"""
    assert event_m10_16_x221(z20=z20)
    """State 4: End state"""
    return 0

def event_m10_16_x223():
    """[Reproduction] Leave the door open"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x224(z18=10160420):
    """[Conditions] Opened door
    z18: OBJ instance ID of the door
    """
    """State 0,1: Has the door opened?"""
    CompareObjState(0, z18, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x225(z18=10160420):
    """[Execution] Opened door
    z18: OBJ instance ID of the door
    """
    """State 0,1: Disable key guide for door"""
    DisableObjKeyGuide(z18, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x226(z18=10160420):
    """[Preset] Opened door
    z18: OBJ instance ID of the door
    """
    """State 0,1: [Reproduction] Open door _SubState"""
    assert event_m10_16_x223()
    """State 3: [Conditions] Opened door_SubState"""
    assert event_m10_16_x224(z18=z18)
    """State 2: [Execution] Leave the door open_SubState"""
    assert event_m10_16_x225(z18=z18)
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

def event_m10_16_x231(z13=_, z14=116000091, z15=_):
    """[DC] [Reproduction] Flying Gargoyle
    z13: Event executed flag
    z14: Boss destruction flag
    z15: Generator ID
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
    if GetEventFlag(z14) != 0:
        pass
    else:
        """State 1: Has the event been executed?"""
        if GetEventFlag(z13) != 0:
            pass
        else:
            """State 5: Event not executed"""
            return 0
    """State 4: Delete character"""
    DeleteEnemyByGenerator(z15, 0)
    """State 6: Event executed and destroyed"""
    return 1

def event_m10_16_x232(z15=_, z14=116000091, z16=_):
    """[DC] [Conditions] Flying gargoyle
    z15: Generator ID
    z14: Boss destruction flag
    z16: Event start point ID
    """
    """State 0,1: Defeat point or boss"""
    IsPlayerInsidePoint(8, z16, z16, 1)
    IsHost(8, 1, 0)
    CompareEventFlag(0, z14, 1)
    if ConditionGroup(0):
        """State 3: Defeat the boss"""
        return 1
    elif ConditionGroup(8):
        """State 2: Flying gargoyle generation"""
        return 0

def event_m10_16_x233(z13=_, z15=_, val1=_, z17=1605010):
    """[DC] [execution] Flying gargoyle
    z13: Event executed flag
    z15: Generator ID
    val1: Weight until generation
    z17: Gargoyle judgment deletion point ID
    """
    """State 0,4: weight"""
    assert (GetStateTime() > val1) != 0
    """State 1: Executed flag ON"""
    SetEventFlag(z13, 1)
    """State 2: Deletion point intrusion detection"""
    IsChrInsidePoint(0, z15, z17, z17, 1)
    assert ConditionGroup(0)
    """State 3: Delete character"""
    DeleteEnemyByGenerator(z15, 0)
    """State 5: Finish"""
    return 0

def event_m10_16_x234(z13=_, z14=116000091, z15=_, z16=_, z17=1605010, val1=_):
    """[DC] [Preset] Flying Gargoyle
    z13: Event executed flag
    z14: Boss destruction flag
    z15: Generator ID
    z16: Event start point ID
    z17: Gargoyle judgment deletion point ID
    val1: Weight until generation
    """
    """State 0,1: [DC] [Reproduction] Flying Gargoyle_SubState"""
    call = event_m10_16_x231(z13=z13, z14=z14, z15=z15)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Gargoyle_SubState to fly"""
        call = event_m10_16_x232(z15=z15, z14=z14, z16=z16)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [DC] [execution] Flying gargoyle_SubState"""
            assert event_m10_16_x233(z13=z13, z15=z15, val1=val1, z17=z17)
    """State 4: End state"""
    return 0

def event_m10_16_x235():
    """[DC] [Reproduction] Acquisition of old key_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_16_x236(z11=10165240):
    """[DC] [Condition] Judgment of obtaining an old key
    z11: Iron treasure chest OBJ instance ID
    """
    """State 0,1: Got an old key?"""
    WasObjItemAcquired(0, z11, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x237(z12=116000014):
    """[DC] [Execution] Judgment of obtaining an old key
    z12: Old key acquisition flag
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(116000014, 1)
    """State 2: End state"""
    return 0

def event_m10_16_x238(z11=10165240, z12=116000014):
    """[DC] [Preset] Acquisition of old keys
    z11: Iron treasure chest OBJ instance ID
    z12: Old key acquisition flag
    """
    """State 0,1: [DC] [Reproduction] Old key acquisition determination_empty_SubState"""
    assert event_m10_16_x235()
    """State 3: [DC] [Condition] Judgment of old key acquisition_SubState"""
    assert event_m10_16_x236(z11=z11)
    """State 2: [DC] [Execution] Acquisition determination of old keys_SubState"""
    assert event_m10_16_x237(z12=z12)
    """State 4: End state"""
    return 0

def event_m10_16_x239(z9=626002, z4=10161000, z5=10161001, z3=116000086):
    """[Execute] Changing lock ID of boss room
    z9: Lock-on parameter ID
    z4: Right_Ignition table OBJ instance ID
    z5: Left_Ignition stand OBJ instance ID
    z3: Boss destruction flag
    """
    """State 0,1: Changing lock-on parameters"""
    ChangeLockOnParameter(z9)
    """State 2: Waiting for both lights to be turned on next or waiting for torches not used or waiting to destroy boss"""
    SetConditionGroup(0, 8)
    CompareObjState(8, z4, 20, 0)
    CompareObjState(8, z5, 20, 0)
    CompareEventFlag(0, z3, 1)
    IsPlayerUsingTorch(0, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_16_x240(z1=116000031):
    """[DC] [Condition] Door key guide disabled until petrochemical release
    z1: Petrochemical release flag
    """
    """State 0,1: Was it petrified?"""
    CompareEventFlag(0, z1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_16_x241(z2=10160410):
    """[DC] [Execution] Door key guide disabled until petrochemical release
    z2: Door OBJ instance ID
    """
    """State 0,1: Activate key guide"""
    DisableObjKeyGuide(z2, 0)
    """State 2: End state"""
    return 0

def event_m10_16_x242(z1=116000031, z2=10160410):
    """[DC] [Reproduction] Door key guide disabled until petrification is canceled
    z1: Petrochemical release flag
    z2: Door OBJ instance ID
    """
    """State 0,2: Petrified state judgment"""
    if GetEventFlag(z1) != 0:
        """State 4: Canceled"""
        return 1
    else:
        """State 1: Disable key guide"""
        DisableObjKeyGuide(z2, 1)
        """State 3: Petrified state"""
        return 0

def event_m10_16_x243(z1=116000031, z2=10160410):
    """[DC] [Preset] Door key guide disabled until petrochemical release
    z1: Petrochemical release flag
    z2: Door OBJ instance ID
    """
    """State 0,1: [DC] [Reproduction] Door key guide disabled until the petrification is canceled_SubState"""
    call = event_m10_16_x242(z1=z1, z2=z2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Door key guide disabled until the petrification is canceled_SubState"""
        assert event_m10_16_x240(z1=z1)
    """State 2: [DC] [Execution] Door key guide disabled until the petrification is canceled_SubState"""
    assert event_m10_16_x241(z2=z2)
    """State 4: Finish"""
    return 0

def event_m10_16_111272():
    """OBJ: Woman Knight (Forgetting Prison): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z250=104192, z251=10164100, z252=91, z253=7520)

def event_m10_16_111273():
    """OBJ: Woman Knight (Forgetting Prison): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_16_x4(z245=116010100, z246=116020101, z247=104190, z248=10164100, z249=111272, npc1=7520)

def event_m10_16_111274():
    """OBJ: Woman Knight (forgetting prison): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_16_x8(z227=90, z228=104192)

def event_m10_16_111275():
    """OBJ: Female Knight (Forgetting Prison): Appearance Judgment"""
    """State 0,1: [Lib] NPC: Woman Knight: Appearance Judgment_SubState"""
    event_m10_16_x7(z229=102481, z230=102482, z231=102483, z232=102485, z233=102490, z234=102486, z235=102487,
                    z236=102488)

def event_m10_16_111276():
    """OBJ: Woman Knight (Forgetting Prison): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_16_x64(z165=102500, z166=546, z167=104190, z168=61, z169=103690, z170=-1)

def event_m10_16_111277():
    """OBJ: Woman Knight (Forgetting Prison): White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_16_x73(z147=116000086, z148=102498, z149=204, z150=7520)

def event_m10_16_111282():
    """OBJ: Kanemori: Aken: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z250=104200, z251=10164200, z252=96, z253=7530)

def event_m10_16_111283():
    """OBJ: Kanemori: Aken: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7530:Bell Keeper
    event_m10_16_x4(z245=116010120, z246=116020121, z247=104200, z248=10164200, z249=111282, npc1=7530)

def event_m10_16_111284():
    """NPC: Kanemori: Black Phantom Appearance: Offline"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
    event_m10_16_x79(z134=10001000, z135=541, z136=0, z137=2)

def event_m10_16_111372():
    """OBJ: EX Blacksmith: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z250=104290, z251=10164000, z252=166, z253=7643)

def event_m10_16_111373():
    """OBJ: EX Blacksmith: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7643:Steady Hand McDuff
    event_m10_16_x4(z245=116010140, z246=116020141, z247=104290, z248=10164000, z249=111372, npc1=7643)

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

def event_m10_16_111402():
    """OBJ: Spermania: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_16_x1(z250=104310, z251=10164300, z252=146, z253=7680)

def event_m10_16_111403():
    """OBJ: Spermania: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7680:Straid of Olaphis
    event_m10_16_x4(z245=116010150, z246=116020151, z247=104310, z248=10164300, z249=111402, npc1=7680)

def event_m10_16_111404():
    """OBJ: Spermania: Petrification: Key guide"""
    """State 0,1: [Lib] Character: Petrified: Key Guide_SubState"""
    event_m10_16_x59(z176=145, z177=104310, z178=15, z179=0, z180=102741, z181=1600, z182=3, z183=111405)

def event_m10_16_111405():
    """OBJ: Spermania: Petrification: Appearance setting"""
    """State 0,1: [Lib] Character: Petrified: Appearance setting_SubState"""
    event_m10_16_x67(z154=145, z155=104310, z156=0, z157=102741, z158=0, z159=111404)

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

def event_m10_16_118120():
    """Multi-use NPC: Sage (Female): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z153=547)

def event_m10_16_118121():
    """Multi-use NPC: Small White Spirit 1"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z153=548)

def event_m10_16_118122():
    """Multi NPC: White Spirit 2"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z153=549)

def event_m10_16_118123():
    """Multi-use NPC: Small White Spirit 2"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_16_x68(z153=550)

def event_m10_16_118200():
    """Multi-use NPC: Mercenary (Male): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_16_x78(z138=10002000, z139=540, z140=0, z141=2)

def event_m10_16_120050():
    """Trophy: Bell Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_16_x80(z132=116020127, z133=23)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_16_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_16_x80(z132=116020109, z133=33)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_16_120140():
    """Trophy: skilled craftsman"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_16_x80(z132=116020148, z133=34)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_16_4000000():
    """[BEST] Andyur appearance _ oblivion"""
    """State 0,3: [Lib] [BEST] [Preset] Ander_Termination_SubState"""
    call = event_m10_16_x120(z101=10162210, z102=100740, z103=100742, z104=100761, z105=100300, z106=100360,
                             z107=100400, z108=100461)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_16_4001000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_16_x133(z99=10162210, z100=10162200)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_16_4002000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_16_x125(z109=10162210, z110=10162200)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_16_4010000():
    """[BEST] Seoul acquisition restraint ring"""
    """State 0,2: [BEST] [Preset] Soul Acquisition Suppression Ring_Sales Start_SubState"""
    assert event_m10_16_x230()
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4011000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_16_x59(z176=9900, z177=0, z178=15, z179=116000031, z180=0, z181=1600, z182=6, z183=4011010)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4011010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_16_x67(z154=9900, z155=0, z156=116000031, z157=0, z158=0, z159=4011000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4011020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_16_x77(z142=6011020, z143=0, z144=2, z145=116000031, z146=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4011100():
    """[DC] Door key guide disabled until petrochemical release"""
    """State 0,2: [DC] [Preset] Door key guide disabled until the petrification is canceled_SubState"""
    assert event_m10_16_x243(z1=116000031, z2=10160410)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4012000():
    """[DC] Vegrant Deletion Decision_1"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z84=4000, z85=7, z86=1, z87=0, z88=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4012010():
    """[DC] Vegrant Deletion Decision_2"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z84=4010, z85=7, z86=1, z87=0, z88=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4012020():
    """[DC] Vegrant Deletion Determination_3"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z84=4020, z85=7, z86=1, z87=0, z88=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4012030():
    """[DC] Vegrant Deletion Determination_4"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_16_x149(z84=4030, z85=7, z86=1, z87=0, z88=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4013000():
    """[DC] Gargoyle to fly_additional location_1"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(z13=116000035, z14=116000091, z15=8010, z16=1605000, z17=1605010, val1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4013010():
    """[DC] Flying gargoyle_additional location_2"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(z13=116000036, z14=116000091, z15=8011, z16=1605000, z17=1605010, val1=1.2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4013100():
    """[DC] Flying gargoyle_conventional position_1"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(z13=116000037, z14=116000091, z15=8012, z16=1605001, z17=1605010, val1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4013110():
    """[DC] Flying Gargoyle_Conventional Position_2"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(z13=116000038, z14=116000091, z15=8013, z16=1605001, z17=1605010, val1=1.2)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4013120():
    """[DC] Flying Gargoyle_Conventional position_3"""
    """State 0,2: [DC] [Preset] Flying Gargoyle_SubState"""
    assert event_m10_16_x234(z13=116000039, z14=116000091, z15=8014, z16=1605001, z17=1605010, val1=1.8)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4014000():
    """[DC] Disabling damage"""
    """State 0,1: STRAY: Petrified damage disabled"""
    SetDamageImmunityByCharacterId(768000, 112503110, 1)
    """State 2: Finish"""
    EndMachine()

def event_m10_16_4015000():
    """[DC] Treasure corpse on the well's foot_1"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_16_x58(z184=10162000, z185=150, z186=10166490)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4016000():
    """[DC] Acquisition of old keys"""
    """State 0,2: [DC] [Preset] Old key acquisition judgment_SubState"""
    assert event_m10_16_x238(z11=10165240, z12=116000014)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4017000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_16_x137(z77=116020060, z78=14, z79=116000061, z80=3, z81=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m10_16_x142(z92=80000000, z93=0, z94=10, z95=932, val2=1, z96=10, z97=80000001,
                z98=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m10_16_x142(z92=80000100, z93=0, z94=10, z95=932, val2=2, z96=10, z97=80000101,
                z98=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m10_16_x142(z92=80000200, z93=0, z94=10, z95=932, val2=3, z96=10, z97=80000201,
                z98=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(116020062, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4017010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_16_x145(z89=116000061, z90=932, mode2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_16_x153(z82=8200, z83=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_16_x153(z82=8201, z83=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_16_x153(z82=8202, z83=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_16_4031000():
    """[DC] NPC White Spirit_Gesture Management_Forgotten Sinner"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_16_x158(z74=116000086, z75=848, z76=116020089)
    """State 1: Finish"""
    EndMachine()

