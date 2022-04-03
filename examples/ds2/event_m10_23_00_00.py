# -*- coding: utf-8 -*-
def event_m10_23_10():
    """Duel start"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel start_SubState"""
    assert (event_m10_23_x32(z75=10231800, z76=10231801, z77=10231802, z78=10231803, z79=10231804, z80=10231805,
            z81=10, z82=17))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_1200():
    """Falling tree_Navimesh change"""
    """State 0,2: [Lib] [Preset] Falling tree _SubState"""
    assert event_m10_23_x30(z84=10231200, z85=120010)
    """State 1: End notification"""
    EndMachine()
    Quit()

def event_m10_23_1400():
    """Rogue activation with plate destruction or view"""
    """State 0,2: [Preset] Rogue activation or SubState with board destruction or view"""
    assert event_m10_23_x94()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_1410():
    """Rogue activated by opening door or approaching"""
    """State 0,2: [Preset] Opening door or approaching Rogue _SubState"""
    assert event_m10_23_x98()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_1411():
    """Rogue activated by opening door * Deleted after state support"""
    """State 0,2: [Preset] Rogue activated by opening the door_SubState"""
    assert event_m10_23_x110()
    """State 1: Finish"""
    Quit()

def event_m10_23_1700():
    """Launch of torturer on pile_1"""
    """State 0,2: [Preset] Pile torturer activation_SubState"""
    assert event_m10_23_x114(z22=170000, z23=170010, z24=123020003, z25=173010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_1710():
    """Launch of torturer on pile_2"""
    """State 0,2: [Preset] Pile torturer activation_2_SubState"""
    assert event_m10_23_x116(z18=171000, z19=171010, z20=123020004, z21=173010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_1720():
    """Launch of torture person on the pile_3rd body"""
    """State 0,2: [Preset] Pile torturer activation_SubState"""
    assert event_m10_23_x114(z22=172000, z23=172010, z24=123020005, z25=173010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_1730():
    """Launch of torture person on the pile_4th body"""
    """State 0,2: [Preset] Pile torturer activation_SubState"""
    assert event_m10_23_x114(z22=173000, z23=173010, z24=123020006, z25=173010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_3010():
    """Chariot's iron grid and lever"""
    """State 0,2: [Preset] Chariot's iron grid and lever_state reproduction_SubState"""
    assert event_m10_23_x126(z7=1023010, z8=123000081, z9=10234900, z10=10234910)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_3020():
    """Iron lattice and chariot destruction judgment"""
    """State 0,4: Host?"""
    if IsGuest() != 1:
        """State 3: Has the initialization event been completed?"""
        assert EventEnded(3010) != 0
        """State 5: [Reproduction] Iron lattice state_SubState"""
        assert event_m10_23_x69()
        """State 9: [Conditions] Iron lattice fracture judgment_SubState"""
        call = event_m10_23_x70()
        if call.Get() == 0:
            """State 7: [Execution] Lowering the iron grid_SubState"""
            assert event_m10_23_x73(z45=302000)
        elif call.Get() == 1:
            """State 8: [Execution] Raise the iron grid_SubState"""
            assert event_m10_23_x72(z46=302000)
        elif call.Get() == 2:
            """State 6: [Execution] Destroy iron lattice and carriage_SubState"""
            assert event_m10_23_x71(z47=302000)
            Goto('L0')
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    else:
        pass
    """State 2: Finish"""
    Label('L0')
    EndMachine()
    Quit()

def event_m10_23_3100():
    """Chariot immortal release"""
    """State 0,2: [Preset] Chariots immortal release_SubState"""
    assert event_m10_23_x102()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4000():
    """The entrance side becomes brighter when the wooden board is broken"""
    """State 0,2: [Preset] _SubState brightens when breaking a wooden board"""
    assert event_m10_23_x77(z43=10231410, z44=10230010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4010():
    """The door side becomes brighter when the wooden board is broken"""
    """State 0,2: [Preset] _SubState brightens when breaking a wooden board"""
    assert event_m10_23_x77(z43=10231400, z44=10230020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4020():
    """Breaking a wooden board makes it brighter"""
    """State 0,2: [Reproduction] Large light determination_SubState"""
    call = event_m10_23_x78(z39=10231410, z40=10231400, z41=10230030, z42=2)
    if call.Get() == 0:
        """State 3: [Condition] Large light determination_SubState"""
        assert event_m10_23_x79(z37=10231410, z38=10231400)
    elif call.Get() == 1:
        pass
    """State 4: [Execution] Large light determination_SubState"""
    assert event_m10_23_x80(z35=10230030, z36=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_5000():
    """Working bridge"""
    """State 0,2: Disable OBJ sync"""
    SetObjSync(10231500, 0)
    """State 3: [Reproduction] Operation Bridge_SubState"""
    assert event_m10_23_x81()
    """State 5: [Condition] Working bridge_SubState"""
    assert event_m10_23_x82(z34=10231510)
    """State 4: [Execution] Operation Bridge_SubState"""
    assert event_m10_23_x83(z32=500000, z33=123000032)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_6000():
    """Shortcut iron lattice_cave route"""
    """State 0,2: Disable OBJ sync"""
    SetObjSync(10231600, 0)
    """State 3: [Reproduction] Shortcut iron grid_SubState"""
    assert event_m10_23_x84()
    """State 5: [Condition] Shortcut iron grid_SubState"""
    assert event_m10_23_x85(z31=10231610)
    """State 4: [Execution] Shortcut iron grid_SubState"""
    assert event_m10_23_x86(z30=600000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_7000():
    """Generate enemy upon death of skeleton aristocrat_1"""
    """State 0,2: [Preset] Create another enemy by destroying the enemy_SubState"""
    assert event_m10_23_x106(z26=839, val1=5200, val2=5201, val3=0, val4=0, val5=0, z27=700000, z28=700049)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_7010():
    """Enemy generation upon death of skeleton aristocrat_2"""
    """State 0,2: [Preset] Create another enemy by destroying the enemy_SubState"""
    assert (event_m10_23_x106(z26=840, val1=5210, val2=5211, val3=5212, val4=5213, val5=5214, z27=701000,
            z28=701049))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_7020():
    """Enemy generation when skeleton nobleman dies_3"""
    """State 0,2: [DC] [Preset] Enemy Destroy creates another enemy_12 body version_SubState"""
    assert event_m10_23_x137(z2=841, z3=702000, z4=702049)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_7030():
    """Skeleton aristocrat_cane_explosive behavior"""
    """State 0,2: [Preset] Skeleton Aristocrat_Cane_Large Explosion_SubState"""
    assert event_m10_23_x122(z11=840, z12=841, z13=123020035)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_8000():
    """Boss Battle_Skeleton Nobility"""
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(0, 800000, 800000, 1)
    if GetEventFlag(123000086) != 0:
        pass
    elif ConditionGroup(0):
        """State 4: Boss BGM playback"""
        PlaySoundAtPoint(101)
        """State 2: Boss battle start notification"""
        StartBossFight(1023000)
        """State 3: Boss battle flag notification for logic"""
        SetEventFlag(123020085, 1)
        """State 9: Did you beat the boss?"""
        IsEventBossKill(0, 1023000, 0, 1)
        assert ConditionGroup(0)
        """State 5: Logic flag OFF"""
        SetEventFlag(123020085, 0)
        """State 6: Boss battle end notification"""
        EndBossFight(1023000)
        """State 11: BGM stop standby"""
        assert (GetStateTime() > 0) != 0
        """State 7: Boss BGM stop"""
        StopSoundAtPoint(101)
    """State 8: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 10: Did you pass the white door?"""
    CompareObjState(0, 10230600, 100, 0)
    Quit()

def event_m10_23_8010():
    """Chair 1 seat where skeleton nobility sits"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_23_x18(z94=10231750, z95=20, z96=801000, z97=0, z98=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_8020():
    """The skeleton aristocratic chair 2_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_23_x18(z94=10231751, z95=20, z96=802000, z97=0, z98=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_8030():
    """Chair 3 seat where skeleton nobility sits"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_23_x18(z94=10231752, z95=20, z96=803000, z97=0, z98=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_9000():
    """Boss Battle_Silver Chariots"""
    """State 0,12: Is the boss battle over?"""
    if GetEventFlag(123000081) != 0:
        pass
    else:
        """State 11: Is the poly drama event finished? Did you get into the point?"""
        CompareEventStatus(8, 9010, 1, 0)
        IsHost(8, 1, 0)
        IsPlayerInsidePoint(8, 900000, 900000, 1)
        SetConditionGroup(0, 8)
        CompareEventStatus(9, 9010, 1, 0)
        IsHost(9, 0, 0)
        IsPlayerInsidePoint(9, 900000, 900000, 1)
        SetConditionGroup(0, 9)
        assert ConditionGroup(0)
        """State 1: Boss BGM playback"""
        PlaySoundAtPoint(102)
        """State 10: Chariots generation flag ON"""
        SetEventFlag(123020083, 1)
        """State 3: Boss battle start notification"""
        StartBossFight(1023010)
        """State 5: Boss battle flag notification for logic"""
        SetEventFlag(123020080, 1)
        """State 8: Did you beat the boss?"""
        IsEventBossKill(0, 1023010, 0, 1)
        assert ConditionGroup(0)
        """State 6: Logic flag OFF"""
        SetEventFlag(123020080, 0)
        """State 4: Boss battle end notification"""
        EndBossFight(1023010)
        """State 13: BGM stop standby"""
        assert (GetStateTime() > 0) != 0
        """State 2: Boss BGM stop"""
        StopSoundAtPoint(102)
    """State 9: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: Zako enemy annihilation"""
    EnemyActionRequest(6000, 1)
    EnemyActionRequest(6001, 1)
    EnemyActionRequest(6002, 1)
    EnemyActionRequest(6003, 1)
    EnemyActionRequest(6004, 1)
    EnemyActionRequest(6005, 1)
    EnemyActionRequest(6006, 1)
    EnemyActionRequest(6030, 1)
    EnemyActionRequest(6031, 1)
    Quit()

def event_m10_23_9010():
    """Boss Battle _ Silver Chariots _ Poly Play"""
    """State 0,8: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Did you pass the white door? Have you already destroyed the boss? Is the poly drama already played?"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    elif GetEventFlag(123000082) != 0:
        pass
    elif CompareObjStateId(10230605, 100, 0) and GetEventFlag(123000082) != 1:
        """State 2: For time adjustment"""
        assert (GetStateTime() > 1) != 0
        """State 4: Poly play"""
        PlayCutscene(102310, 1, 1)
        assert (CutscenePlaying() == 1) != 0
        """State 5: During the poly play"""
        assert (not CutscenePlaying()) != 0
        """State 7: Host judgment"""
        WarpAndSyncRemoteCharacters()
        if IsGuest() != 1:
            """State 6: warp"""
            SetEventFlag(123000082, 1)
            WarpPlayersWithinMap(900010)
            SaveExecution()
        else:
            pass
    """State 3: End notification"""
    EndMachine()
    Quit()

def event_m10_23_10000():
    """Key door_Fire room"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_23_x4(z115=1005, z116=1105, z117=50970000, z118=123000020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_11000():
    """Switching of Madura's revolving door related flags"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_23_x26(z86=105400, z87=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_23_12000():
    """Skeleton immortality management_before cave_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4000, z6=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12010():
    """Skeleton immortality management_before cave_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4003, z6=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12020():
    """Skeleton immortality management_before cave_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4010, z6=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12030():
    """Skeleton immortality management_before cave_4"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4012, z6=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12040():
    """Skeleton immortality management_before cave_5"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4013, z6=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12500():
    """Skeleton immortality management_back of cave_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4050, z6=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12510():
    """Skeleton immortality management_back of cave_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4053, z6=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12520():
    """Skeleton immortal management_back of cave_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4054, z6=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_12530():
    """Skeleton immortal management_back of cave_4"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=4055, z6=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13000():
    """Skeleton immortality management_before prison_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6000, z6=6031)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13010():
    """Skeleton immortality management_before prison_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6001, z6=6031)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13020():
    """Skeleton immortality management_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6002, z6=6031)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13500():
    """Skeleton immortality management_back of prison_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6003, z6=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13510():
    """Skeleton immortality management_back of prison_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6004, z6=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13520():
    """Skeleton immortal management_back of prison_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6005, z6=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_13530():
    """Skeleton immortality management_back of prison_4"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z5=6006, z6=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_15000():
    """Torture lift_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_Relief_SubState"""
    assert event_m10_23_x52(z60=10231700, z61=30, flag4=123000050, z62=32)
    """State 3: [Lib] [Preset] Elevator_Initialization_Relief_2_SubState"""
    assert event_m10_23_x52(z60=10231701, z61=31, flag4=123000051, z62=33)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_15010():
    """Torture lift"""
    """State 0,2: [Lib] [Preset] Torture lift_operation_SubState"""
    assert (event_m10_23_x8(z105=15000, z106=10231700, z107=10231701, z108=30, z109=1501015, z110=1501010,
            z111=1501005, z112=1501000))
    """State 1: Rerun notification"""
    RestartMachine()
    Quit()

def event_m10_23_15020():
    """Torture lift_character action judgment"""
    """State 0,2: [Lib] [Preset] Torture lift_Action judgment_SubState"""
    assert event_m10_23_x12(z99=10231700, z100=10231701, z101=1501015, z102=1501010, z103=1501005, z104=1501000)
    """State 1: Rerun notification"""
    RestartMachine()
    Quit()

def event_m10_23_18000():
    """Hidden door ② on lift_Navimesh change"""
    """State 0,2: [Preset] Hidden Door 2_Invisible Key Guide_SubState"""
    assert event_m10_23_x87(z29=1800000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_19000():
    """Hidden door ② under lift_Navimesh change"""
    """State 0,2: [Preset] Hidden Door 2_Invisible Key Guide_SubState"""
    assert event_m10_23_x87(z29=1900000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_20000():
    """Hunting Forest-Tame Valley Operation Bridge"""
    """State 0,3: [Preset] Hunting Forest-Tame Valley Operation Bridge_SubState"""
    call = event_m10_23_x121(z14=10231460, z15=10231450, z16=2000001, z17=2000002)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_23_21000():
    """Hunting forest MAP discard flag switching"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_23_x26(z86=105440, z87=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_23_70000():
    """Duel request_1"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62110000:Token of Spite
    assert event_m10_23_x45(z63=3, z64=10239000, z65=10239001, z66=10231760, z67=40, val6=3, goods1=62110000)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_23_70010():
    """Duel Request_2"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62110000:Token of Spite
    assert event_m10_23_x45(z63=4, z64=10239000, z65=10239001, z66=10231761, z67=40, val6=3, goods1=62110000)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_23_70020():
    """Duel Request_3"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62110000:Token of Spite
    assert event_m10_23_x45(z63=5, z64=10239000, z65=10239001, z66=10231762, z67=40, val6=3, goods1=62110000)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_23_80000():
    """Reproduction fire 01_Starting point"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z73=1023000, z74=1023099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_81000():
    """Regenerative fire 02_under pillar of suspension bridge"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z73=1023100, z74=1023199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_82000():
    """Regenerative fireworks 03_within the key door torch"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z73=1023200, z74=1023299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_83000():
    """After the boss 04"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z73=1023300, z74=1023399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_x0(z124=_, z125=_, z126=_, z127=_):
    """[Lib] NPC: Grave Placement: General purpose
    z124: Death map: Global event flag
    z125: Tomb: OBJ instance ID
    z126: Tomb move to: Generator ID
    z127: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z124, 1)
    IsGraveGeneratable(8, z127, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z125, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z125, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_23_x1(z121=_, z122=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z121: Global: death flag
    z122: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z122, 10, 0)
    CompareObjState(1, z122, 20, 0)
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
    IsObjSearched(0, z122)
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

def event_m10_23_x2(z119=_, z120=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z119: Area other flags: Ghost appearance
    z120: Area other flags: Conversation start
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
    SetEventFlag(z119, 1)
    CompareEventFlag(0, z119, 1)
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
    SetEventFlag(z120, 1)
    CompareEventFlag(0, z120, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_23_x3(z119=_, z120=_, z121=_, z122=_, z123=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z119: Ghost Appearance: Area Other Flag
    z120: Conversation start: Area and other flags
    z121: Death: Global event flag
    z122: Tomb: OBJ instance ID
    z123: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z123, 1, 0)
    CompareEventFlag(9, z119, 1)
    CompareObjState(9, z122, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z120, 1)
        CompareEventFlag(0, z120, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_23_x1(z121=z121, z122=z122, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_23_x2(z119=z119, z120=z120, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_23_x4(z115=1005, z116=1105, z117=50970000, z118=123000020):
    """[Lib] Item specified door unlocking_2
    z115: Text ID when opened
    z116: Text ID when not opened
    z117: item
    z118: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z117, z115, z116, z118, 0)
    """State 2: End state"""
    return 0

def event_m10_23_x5(z113=55, z114=104151):
    """[Lib] NPC: Death determination: General purpose
    z113: Generator ID
    z114: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z114, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z113)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z114, 1)
            CompareEventFlag(0, z114, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_23_x6():
    """[Lib] [Reproduction] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x7():
    """[Lib] [Condition] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x8(z105=15000, z106=10231700, z107=10231701, z108=30, z109=1501015, z110=1501010, z111=1501005,
                    z112=1501000):
    """[Lib] [Preset] Torture lift
    z105: Initialization event ID
    z106: Reference lift_object instance ID
    z107: Mirror lift_object instance ID
    z108: Safety time
    z109: Reference lift point_on
    z110: Reference lift point_below
    z111: Mirror lift point_on
    z112: Mirror lift point_bottom
    """
    """State 0,2: [Reproduction] Torture lift_operation_SubState"""
    assert event_m10_23_x9(z105=z105)
    """State 3: [Condition] Torture lift_operation_SubState"""
    call = event_m10_23_x10(z106=z106, z107=z107, z109=z109, z110=z110, z111=z111, z112=z112)
    if call.Get() == 0:
        """State 4: [Execution] Torture lift_operation_SubState"""
        assert event_m10_23_x11(z106=z106, z107=z107, z108=z108, z112=z112, z109=z109)
    elif call.Get() == 1:
        """State 5: [Execution] Torture lift_operation_2_SubState"""
        assert event_m10_23_x11(z106=z107, z107=z106, z108=z108, z112=z112, z109=z109)
    """State 1: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_23_x9(z105=15000):
    """[Lib] [Reproduction] Torture lift_operation
    z105: Initialization event ID
    """
    """State 0,2: [Compatible with SEQ17677] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 1: Whether the event has ended"""
    assert EventEnded(z105) != 0
    """State 3: End state"""
    return 0

def event_m10_23_x10(z106=10231700, z107=10231701, z109=1501015, z110=1501010, z111=1501005, z112=1501000):
    """[Lib] [Condition] Torture lift _operation
    z106: Reference lift_object instance ID
    z107: Mirror lift_object instance ID
    z109: Reference lift point_on
    z110: Reference lift point_below
    z111: Mirror lift point_on
    z112: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z106, 32, 0)
    IsPlayerInsidePoint(8, z109, z109, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z106, 33, 0)
    IsPlayerInsidePoint(9, z110, z110, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(1, 9)
    CompareObjState(10, z107, 32, 0)
    IsPlayerInsidePoint(10, z111, z111, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z107, 33, 0)
    IsPlayerInsidePoint(11, z112, z112, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(0, 11)
    if ConditionGroup(0):
        """State 2: Standard is from top to bottom"""
        return 0
    elif ConditionGroup(1):
        """State 3: Mirror from top to bottom"""
        return 1

def event_m10_23_x11(z106=_, z107=_, z108=30, z112=1501000, z109=1501015):
    """[Lib] [execution] torture lift
    z106: Top lift_object instance ID
    z107: Lower lift_object instance ID
    z108: Safety time
    z112: Point start
    z109: End of point
    """
    """State 0,1: Execution"""
    ChangeObjState(z106, 70)
    ChangeObjState(z107, 71)
    """State 2: Waiting for next start"""
    CompareObjState(8, z107, 32, 0)
    CompareObjState(8, z106, 33, 0)
    IsPlayerInsidePoint(8, z112, z109, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    CompareStateTime(1, z108, 3, z108)
    SetConditionGroup(1, 8)
    assert HostConditionGroup(1)
    """State 3: End state"""
    return 0

def event_m10_23_x12(z99=10231700, z100=10231701, z101=1501015, z102=1501010, z103=1501005, z104=1501000):
    """[Lib] [Preset] Torture lift_action judgment
    z99: Reference lift_object instance ID
    z100: Mirror lift_object instance ID
    z101: Reference lift point_on
    z102: Reference lift point_below
    z103: Mirror lift point_on
    z104: Mirror lift point_bottom
    """
    """State 0,1: [Reproduction] Torture lift_action judgment_empty_SubState"""
    assert event_m10_23_x13()
    """State 4: [Condition] Torture lift_Action determination_Start determination_SubState"""
    call = event_m10_23_x14(z99=z99, z100=z100, z101=z101, z102=z102, z103=z103, z104=z104)
    if call.Get() == 1:
        """State 2: [Execution] Torture lift_Action judgment_Action start_SubState"""
        assert event_m10_23_x15(z99=z99)
        """State 7: [Reproduction] Torture lift_action judgment_empty_2_SubState"""
        assert event_m10_23_x13()
        """State 5: [Condition] Torture lift_Action judgment_End judgment_SubState"""
        assert event_m10_23_x16(z99=z99, z101=z101, z102=z102)
        """State 3: [Execution] Torture lift_Action judgment_Action end_SubState"""
        assert event_m10_23_x17(z99=z99, z101=z101, z102=z102)
    elif call.Get() == 0:
        """State 6: [Execution] Torture Lift_Action Judgment_Action Start_2_SubState"""
        assert event_m10_23_x15(z99=z100)
        """State 8: [Reproduction] Torture lift_Action judgment_Empty_3_SubState"""
        assert event_m10_23_x13()
        """State 10: [Condition] Torture lift_Action judgment_End judgment_2_SubState"""
        assert event_m10_23_x16(z99=z100, z101=z103, z102=z104)
        """State 9: [Execution] Torture lift_Action judgment_Action end_2_SubState"""
        assert event_m10_23_x17(z99=z100, z101=z103, z102=z104)
    """State 11: End state"""
    return 0

def event_m10_23_x13():
    """[Lib] [reproduction] Torture lift_action judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x14(z99=10231700, z100=10231701, z101=1501015, z102=1501010, z103=1501005, z104=1501000):
    """[Lib] [Condition] Torture lift_Action judgment_Start judgment
    z99: Reference lift_object instance ID
    z100: Mirror lift_object instance ID
    z101: Reference lift point_on
    z102: Reference lift point_below
    z103: Mirror lift point_on
    z104: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z99, 70, 0)
    IsPlayerInsidePoint(8, z101, z101, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z99, 71, 0)
    IsPlayerInsidePoint(9, z102, z102, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(0, 9)
    CompareObjState(10, z100, 70, 0)
    IsPlayerInsidePoint(10, z103, z103, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z100, 71, 0)
    IsPlayerInsidePoint(11, z104, z104, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(1, 11)
    if ConditionGroup(0):
        """State 3: Standard"""
        return 1
    elif ConditionGroup(1):
        """State 2: mirror"""
        return 0

def event_m10_23_x15(z99=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action start
    z99: Lift_object instance ID
    """
    """State 0,1: Action request"""
    ObjAnimationPlayerControlRequest(z99, 34, 10)
    """State 2: End state"""
    return 0

def event_m10_23_x16(z99=_, z101=_, z102=_):
    """[Lib] [Condition] Torture lift_Action judgment_End judgment
    z99: Lift_object instance ID
    z101: Lift point_on
    z102: Lift point_down
    """
    """State 0,1: Wait"""
    CompareObjState(8, z99, 32, 0)
    CompareObjState(9, z99, 33, 0)
    SetConditionGroup(0, 8)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Finish"""
    return 0

def event_m10_23_x17(z99=_, z101=_, z102=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action end
    z99: Lift_object instance ID
    z101: Lift point_on
    z102: Lift point_down
    """
    """State 0,1: Action request"""
    EndPlayerActionRequest()
    """State 2: Wait"""
    IsPlayerInsidePoint(0, z101, z101, 1)
    IsPlayerInsidePoint(0, z102, z102, 1)
    """State 3: End state"""
    return 0

def event_m10_23_x18(z94=_, z95=20, z96=_, z97=0, z98=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z94: Object instance ID
    z95: OBJ state ID
    z96: Navimesh switching point ID
    z97: Additional attributes
    z98: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_23_x19(z94=z94, z95=z95, z96=z96, z98=z98, z97=z97)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_23_x20(z94=z94, z95=z95, z96=z96)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_23_x21(z94=z94, z95=z95, z96=z96, z97=z97, z98=z98)
    """State 4: End state"""
    return 0

def event_m10_23_x19(z94=_, z95=20, z96=_, z98=2, z97=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z94: Target OBJ instance ID
    z95: Target OBJ state ID
    z96: Navimesh switching point ID
    z98: Additional attributes
    z97: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z94, z95, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z96, z98)
        DeleteNavimeshAttribute(z96, z97)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_23_x20(z94=_, z95=20, z96=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z94: Target OBJ instance ID
    z95: Target OBJ state ID
    z96: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z94, z95, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x21(z94=_, z95=20, z96=_, z97=0, z98=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z94: Target OBJ instance ID
    z95: Target OBJ state ID
    z96: Navimesh switching point ID
    z97: Additional attributes
    z98: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z96, z97)
    DeleteNavimeshAttribute(z96, z98)
    """State 2: End state"""
    return 0

def event_m10_23_x22(z88=102405, z89=587, z90=104150, z91=60, z92=103650, z93=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z88: White Phantom can appear: Global event flag
    z89: White Phantom: Generator ID
    z90: Death: Global event flag
    z91: Body: Generator group ID
    z92: Hostile: Global event flag
    z93: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z89)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z90, 1)
        CompareEventFlag(1, z92, 1)
        CompareEventFlag(2, z88, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z89)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z90, 1)
            CompareEventFlag(1, z92, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z89)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z90, 1)
            CompareEventFlag(1, z92, 1)
            HasNpcPhantomSpawned(2, z89, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z91, 0)
                HasNpcPhantomSpawned(0, z89, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z89)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_23_x23():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x24():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x25(z86=_, z87=_):
    """[Lib] [Execution] Switch to connection flag when in map
    z86: Global event flag for connection
    z87: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z86, z87)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z86, z87)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_23_x26(z86=_, z87=_):
    """[Lib] [Preset] Switch the connection flag when in the map
    z86: Global event flag for connection
    z87: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_23_x23()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_23_x24()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_23_x25(z86=z86, z87=z87)
    """State 4: End state"""
    return 0

def event_m10_23_x27():
    """[Lib] [Reproduction] Falling Tree"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x28(z84=10231200):
    """[Lib] [Condition] Falling tree
    z84: OBJ instance ID of the tree
    """
    """State 0,1: Wait for tree to fall"""
    CompareObjState(0, z84, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x29(z85=120010):
    """[Lib] [execution] fallen tree
    z85: Navigation change point ID
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z85, 2)
    """State 2: End state"""
    return 0

def event_m10_23_x30(z84=10231200, z85=120010):
    """[Lib] [Preset] Falling Tree
    z84: OBJ instance ID of the tree
    z85: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Falling tree _SubState"""
    assert event_m10_23_x27()
    """State 3: [Lib] [Condition] Falling tree _SubState"""
    assert event_m10_23_x28(z84=z84)
    """State 2: [Lib] [Execution] Falling tree _SubState"""
    assert event_m10_23_x29(z85=z85)
    """State 4: End state"""
    return 0

def event_m10_23_x31(z83=586):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z83: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z83)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_23_x32(z75=10231800, z76=10231801, z77=10231802, z78=10231803, z79=10231804, z80=10231805,
                     z81=10, z82=17):
    """[Lib] [Asynchronous] [Preset] Duel start
    z75: Door instance IDA
    z76: Door instance IDB
    z77: Door instance IDC
    z78: Door instance IDD
    z79: Door instance IDE
    z80: Door instance IDF
    z81: Event sound ID
    z82: Production FE type
    """
    """State 0,1: [Lib] [Reproduction] Dummy_SubState"""
    assert event_m10_23_x6()
    """State 2: [Lib] [Condition] Dummy_SubState"""
    assert event_m10_23_x7()
    """State 3: [Lib] [Execution] Duel Start_SubState"""
    assert event_m10_23_x33(z75=z75, z76=z76, z77=z77, z78=z78, z79=z79, z80=z80, z81=z81, z82=z82)
    """State 4: End state"""
    return 0

def event_m10_23_x33(z75=10231800, z76=10231801, z77=10231802, z78=10231803, z79=10231804, z80=10231805,
                     z81=10, z82=17):
    """[Private] [Asynchronous] [Execution] Start of duel
    z75: Door instance IDA
    z76: Door instance IDB
    z77: Door instance IDC
    z78: Door instance IDD
    z79: Door instance IDE
    z80: Door instance IDF
    z81: Event sound ID
    z82: Production FE type
    """
    """State 0,1: Jingle sound playback"""
    PlaySoundAtPoint(z81)
    """State 4: Preparation time"""
    assert (GetStateTime() > 5) != 0
    """State 2: Start: open the door"""
    ChangeObjState(z75, 70)
    ChangeObjState(z76, 70)
    ChangeObjState(z77, 70)
    ChangeObjState(z78, 70)
    ChangeObjState(z79, 70)
    ChangeObjState(z80, 70)
    """State 3: Production FE display"""
    OpenPresentationWindow(z82)
    """State 5: End state"""
    return 0

def event_m10_23_x34(z63=_):
    """[Private] [Asynchronous] [Execution] Duel Request_Start
    z63: Duel type
    """
    """State 0,1: Motion start"""
    PlayerActionRequest(14)
    ProhibitInGameMenu(1)
    """State 2: Matching start"""
    StartDuelMatch(z63)
    """State 3: End state"""
    return 0

def event_m10_23_x35(z66=_, z67=40):
    """[Private] [Asynchronous] [Condition] Duel request_wait
    z66: Object instance ID
    z67: Hit group
    """
    """State 0,2: A little wait"""
    assert (GetStateTime() >= 0) != 0
    """State 1: Wait to examine"""
    IsObjSearched(0, z66)
    IsDuelStartPossible(0, 0)
    IsPlayerDamaged(0)
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(0, z67, 0, 0, 2)
    IsPlayerPlayingMotion(0, 14, 0)
    IsDuelMatching(0, 0)
    HasDuelMatched(1, 1)
    if ConditionGroup(0):
        """State 4: Cancel"""
        return 0
    elif ConditionGroup(1):
        """State 3,5: Duel-matched"""
        return 1

def event_m10_23_x36():
    """[Private] [Asynchronous] [Execution] Duel request_wait_cancel"""
    """State 0,1: Motion cancellation"""
    EndPlayerActionRequest()
    """State 2: Duel cancellation"""
    CancelDuelMatch()
    ProhibitInGameMenu(0)
    """State 3: End state"""
    return 0

def event_m10_23_x37(z67=40, z65=10239001):
    """[Private] [Asynchronous] [Reproduction] Duel request_wait
    z67: Hit group
    z65: Key guide parameters
    """
    """State 0,1: Key guide creation"""
    CreateKeyGuideArea(34, z65)
    """State 2: Finish"""
    return 0

def event_m10_23_x38():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x39(z73=_, z74=_):
    """[Lib] [execute] Rebirth fire
    z73: Flag start ID
    z74: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z73, z74, 0)
    """State 2: End state"""
    return 0

def event_m10_23_x40():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x41(z73=_, z74=_):
    """[Lib] [Preset] Rebirth
    z73: Flag start ID
    z74: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_23_x38()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_23_x40()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_23_x39(z73=z73, z74=z74)
    """State 4: End state"""
    return 0

def event_m10_23_x42(z69=12000000, z70=580, z71=0, z72=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z69: Summon range
    z70: Generator ID
    z71: Appearance: Minimum time
    z72: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z69, z69, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z71, 3, z72)
        IsPlayerInsidePoint(1, z69, z69, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z70)
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

def event_m10_23_x43(flag5=123020127, z68=20):
    """[Lib] [Preset] Get trophy
    flag5: Acquisition trigger_other flags
    z68: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag5) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag5, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z68)
    """State 4: End state"""
    return 0

def event_m10_23_x44():
    """[Private] [Asynchronous] [Execution] Duel request_wait_matched"""
    """State 0,3: Cannot cancel motion"""
    ForceDisablePlayerAnimationCancelling(1)
    DeleteKeyGuideArea()
    IsDuelMatching(0, 0)
    assert ConditionGroup(0)
    """State 1: Motion cancellation"""
    EndPlayerActionRequest()
    ForceDisablePlayerAnimationCancelling(0)
    """State 2: Duel cancellation"""
    CancelDuelMatch()
    ProhibitInGameMenu(0)
    """State 4: End state"""
    return 0

def event_m10_23_x45(z63=_, z64=10239000, z65=10239001, z66=_, z67=40, val6=3, goods1=62110000):
    """[Lib] [Asynchronous] [Preset] Duel Request
    z63: Duel type
    z64: Start key guide parameter
    z65: Cancel key guide parameter
    z66: Object instance ID
    z67: Hit group
    val6: Pledge
    goods1: item
    """
    """State 0,8: [Private] [Asynchronous] [Reproduction] Duel Request_Start_Training_SubState"""
    call = event_m10_23_x47(z67=z67, z64=z64, val6=val6)
    if call.Get() == 1:
        """State 10: [Private] [Asynchronous] [Condition] Duel request_Start_Key guide wait_Training_SubState"""
        call = event_m10_23_x46(z66=z66, z67=z67, val6=val6, goods1=goods1)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 3: [Private] [Asynchronous] [Execution] Duel Request_Start_SubState"""
            assert event_m10_23_x34(z63=z63)
            """State 4: [Private] [Asynchronous] [Reproduction] Duel Request_Standby_SubState"""
            assert event_m10_23_x37(z67=z67, z65=z65)
            """State 5: [Private] [Asynchronous] [Condition] Duel Request_Standby_SubState"""
            call = event_m10_23_x35(z66=z66, z67=z67)
            if call.Get() == 0:
                """State 6: [Private] [Asynchronous] [Execution] Duel Request_Wait_Cancel_SubState"""
                assert event_m10_23_x36()
            elif call.Get() == 1:
                """State 7: [Private] [Asynchronous] [Execution] Duel Request_Waiting_Matched_SubState"""
                assert event_m10_23_x44()
            """State 2: Rerun_2"""
            RestartMachine()
            Quit()
    elif call.Done():
        """State 9: [Private] [Asynchronous] [Condition] Duel Request_Start_Key Guide Invalidation Wait_Training_SubState"""
        assert event_m10_23_x48(z67=z67, val6=val6)
    """State 1: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_23_x46(z66=_, z67=40, val6=3, goods1=62110000):
    """[Private] [Asynchronous] [Condition] Duel request_Start_Key guide wait
    z66: Object instance ID
    z67: Hit group
    val6: Pledge
    goods1: item
    """
    """State 0,1: Wait to examine"""
    IsObjSearched(0, z66)
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(1, z67, 0, 0, 2)
    IsPlayerInCovenant(1, val6, 0)
    IsOffline(1, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Item confirmation"""
        # goods:62110000:Token of Spite
        if (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 2: Don't have display"""
            # action:1013:"No %s\nin inventory", goods:62110000:Token of Spite
            DisplayOwnOkMenu(1013, 0, 0, 190, 2, goods1, 0)
            assert OkMenuDisplay() != 1
            Goto('L0')
        elif (GetPlayerCovenant() == 2) != 0:
            """State 4: Usage confirmation"""
            # action:1002:"Use %s?", goods:62110000:Token of Spite
            DisplayOwnYesNoMenu(1002, 0, 190, 2, goods1, 0)
            assert YesNoMenuDisplay() != 1
            """State 5: Result branch"""
            if (YesNoMenuResult() == 1) != 1:
                Goto('L0')
            else:
                pass
        else:
            pass
        """State 6: Establishment"""
        return 0
    """State 7: Not established"""
    Label('L0')
    return 1

def event_m10_23_x47(z67=40, z64=10239000, val6=3):
    """[Private] [Asynchronous] [Reproduction] Duel Request_Start
    z67: Hit group
    z64: Key guide parameters
    val6: Pledge
    """
    """State 0,1: Branch"""
    if (CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(z67, 0, 1) != 1 and (GetPlayerCovenant()
        == val6) != 0 and IsOffline() != 1):
        """State 2: Key guide creation"""
        CreateKeyGuideArea(34, z64)
        """State 5: There are no enemies around"""
        return 1
    else:
        """State 3: Delete key guide"""
        DeleteKeyGuideArea()
        """State 4: There are enemies around"""
        return 0

def event_m10_23_x48(z67=40, val6=3):
    """[Private] [Asynchronous] [Condition] Duel request_Start_Key guide invalidation waiting
    z67: Hit group
    val6: Pledge
    """
    """State 0,1: Wait"""
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(8, z67, 0, 0, 5)
    IsPlayerInCovenant(8, val6, 1)
    IsOffline(8, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_23_x49(flag4=_, z60=_, z61=_, z62=_):
    """[Lib] [Reproduction] Elevator_Initialization_Relief
    flag4: Initialization completion flag
    z60: Elevator OBJ instance ID
    z61: Initial position OBJ state ID
    z62: OBJ state after initialization
    """
    """State 0,4: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 1: Already initialized?"""
    if GetEventFlag(flag4) != 0:
        pass
    else:
        Goto('L0')
    """State 2: [Remedy] Is it in the initial state?"""
    if CompareObjStateId(z60, 10, 0):
        """State 3: Elevator initialization"""
        ChangeObjState(z60, z61)
        assert CompareObjStateId(z60, z62, 0)
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

def event_m10_23_x50():
    """[Lib] [Condition] Elevator_Initialization_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x51(z60=_, z61=_, flag4=_, z62=_):
    """[Lib] [Run] Elevator_Initialization_Relief
    z60: Elevator OBJ instance ID
    z61: Initial position OBJ state ID
    flag4: Initialization completion flag
    z62: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z60, z61)
    assert CompareObjStateId(z60, z62, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag4, 1)
    """State 3: End state"""
    return 0

def event_m10_23_x52(z60=_, z61=_, flag4=_, z62=_):
    """[Lib] [Preset] Elevator_Initialization_Relief
    z60: Elevator OBJ instance ID
    z61: Initial position OBJ state ID
    flag4: Initialization completion flag
    z62: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_Relief_SubState"""
    call = event_m10_23_x49(flag4=flag4, z60=z60, z61=z61, z62=z62)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 3:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_Empty_SubState"""
        assert event_m10_23_x50()
        """State 2: [Lib] [Execution] Elevator_Initialization_Relief_SubState"""
        assert event_m10_23_x51(z60=z60, z61=z61, flag4=flag4, z62=z62)
    """State 4: End state"""
    return 0

def event_m10_23_x53(flag3=123000042):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag3: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag3) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_23_x54(z58=944, mode1=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z58: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z58)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_23_x55(flag3=123000042, z59=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag3: Defeat flag
    z59: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag3, 1)
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
                    SetEventFlag(z59, 1)
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

def event_m10_23_x56(flag3=123000042, z58=944, mode1=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag3: Defeat flag
    z58: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_23_x53(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_23_x54(z58=z58, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_23_x55(flag3=flag3, z59=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_23_x55(flag3=flag3, z59=102755)
    """State 5: End state"""
    return 0

def event_m10_23_x57(z56=9500, z57=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z56: Generator ID
    z57: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z56, z57)
    """State 2: End state"""
    return 0

def event_m10_23_x58(z56=9500, z57=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z56: Generator ID
    z57: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z56, z57, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_23_x59(z56=9500):
    """[Lib] [DC] [Condition] Transparent characters
    z56: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z56)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x60(z56=9500, z57=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z56: Generator ID
    z57: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_23_x58(z56=z56, z57=z57)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_23_x59(z56=z56)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_23_x57(z56=z56, z57=z57)
    """State 4: End state"""
    return 0

def event_m10_23_x61():
    """[Lib] [Reproduction] Wanderer_Fixed Appearance"""
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        """State 4: The guests"""
        return 1
    else:
        """State 3: host"""
        return 0

def event_m10_23_x62(z54=944, z55=123020043):
    """[Lib] [execution] wanderer_fixed appearance
    z54: Generator ID
    z55: Startup flag
    """
    """State 0,1: Wanderer: Generate Start flag ON"""
    GenerateNpcPhantom(z54)
    SetEventFlag(z55, 1)
    """State 2: Finish"""
    return 0

def event_m10_23_x63(z50=6000000, z51=6000000, z52=0, z53=2):
    """[Lib] [Condition] Wanderer_Fixed Appearance
    z50: Judgment start point ID
    z51: Judgment end point ID
    z52: Minimum appearance time
    z53: Maximum time to appear
    """
    """State 0,1: Appearance determination"""
    IsPlayerInsidePoint(0, z51, z51, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z52, 3, z53)
    assert ConditionGroup(0)
    """State 3: Appearance"""
    return 0

def event_m10_23_x64(z50=6000000, z51=6000000, z52=0, z53=2, z54=944, z55=123020043):
    """[Lib] [Preset] Wanderer_Fixed Appearance
    z50: Judgment start point ID
    z51: Judgment end point ID
    z52: Minimum appearance time
    z53: Maximum time to appear
    z54: Generator ID
    z55: Startup flag
    """
    """State 0,1: [Lib] [Reproduction] Wanderer_Fixed Appearance_SubState"""
    assert event_m10_23_x61()
    """State 3: [Lib] [Condition] Wanderer_Fixed Appearance_SubState"""
    assert event_m10_23_x63(z50=z50, z51=z51, z52=z52, z53=z53)
    """State 2: [Lib] [execution] wanderer_fixed appearance_SubState"""
    assert event_m10_23_x62(z54=z54, z55=z55)
    """State 4: Finish"""
    return 0

def event_m10_23_x65(flag2=123000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag2: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag2) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_23_x66(z48=816):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z48: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z48, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x67(z49=123020084):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z49: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z49, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x68(flag2=123000081, z48=816, z49=123020084):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag2: Boss destruction flag
    z48: Boss generator ID
    z49: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_23_x65(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_23_x66(z48=z48)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_23_x67(z49=z49)
    """State 4: End state"""
    return 0

def event_m10_23_x69():
    """[Reproduction] Iron lattice state"""
    """State 0,1: Did you destroy the boss or boss during the boss battle?"""
    if GetEventFlag(123000081) != 0:
        pass
    elif BossBattleOngoing(1023010) != 0:
        pass
    else:
        """State 2: Initialize related OBJ"""
        InitializeObj(10234920)
        InitializeObj(10234930)
    """State 3: End state"""
    return 0

def event_m10_23_x70():
    """[Conditions] Iron lattice breakage"""
    """State 0,1: Barred state judgment"""
    CompareObjState(0, 10234900, 10, 0)
    CompareObjState(0, 10234900, 71, 0)
    CompareObjState(1, 10234900, 70, 0)
    CompareObjState(1, 10234900, 30, 0)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        Goto('L0')
    """State 2: Lattice is up_Lever switching standby"""
    CompareObjState(0, 10234910, 74, 0)
    CompareObjState(0, 10234910, 84, 0)
    assert ConditionGroup(0)
    """State 4: Chariots point judgment"""
    IsChrInsidePoint(0, 816, 100020, 100020, 0)
    assert ConditionGroup(0)
    """State 6: Lower the bar"""
    return 0
    """State 3: Lattice down_lever switching or destruction standby"""
    Label('L0')
    CompareObjState(0, 10234910, 84, 0)
    CompareObjState(0, 10234910, 74, 0)
    CompareObjState(8, 10234900, 30, 0)
    IsChrInsidePoint(8, 816, 100010, 100010, 1)
    if ConditionGroup(8):
        pass
    elif ConditionGroup(0):
        """State 5: Chariots point judgment or destruction waiting"""
        IsChrInsidePoint(0, 816, 100020, 100020, 0)
        CompareObjState(8, 10234900, 30, 0)
        IsChrInsidePoint(8, 816, 100010, 100010, 1)
        if ConditionGroup(8):
            pass
        elif ConditionGroup(0):
            """State 7: Raise the bar"""
            return 1
    """State 8: Broken iron bars and carriages"""
    return 2

def event_m10_23_x71(z47=302000):
    """[Execution] Destroy iron grid and carriage
    z47: Navigation change point ID
    """
    """State 0,6: Destroyed bar"""
    ChangeOwnObjState(72)
    """State 8: Disabling the key guide of the lever"""
    DisableObjKeyGuide(10234910, 1)
    """State 7: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z47, 2)
    """State 1: Chariot's Logic Flag ON & Immortal Cancellation"""
    SetEventFlag(123020001, 1)
    SetEventFlag(123020002, 1)
    SetEnemySpEffect(816, 96191020, 19, 4)
    """State 4: Comparison of carriage HP ratio"""
    CompareChrHpRatio(0, 816, 30, 3)
    CompareChrHpRatio(1, 816, 30, 4)
    if ConditionGroup(0):
        """State 5: Carriage collision damage occurred"""
        AttachBulletToTheEnemy(816, 161919000)
    elif ConditionGroup(1):
        pass
    """State 3: OBJ Warp"""
    WarpObjToCharacter(10234930, 816, 91)
    WarpObjToCharacter(10234920, 816, 92)
    """State 2: OBJ state transition (animation playback)"""
    ChangeObjState(10234930, 70)
    ChangeObjState(10234920, 50)
    """State 9: End state"""
    return 0

def event_m10_23_x72(z46=302000):
    """[Execution] Raise the iron grid
    z46: Navigation change point ID
    """
    """State 0,1: Raise the bar"""
    ChangeOwnObjState(71)
    assert CompareOwnObjStateId(10, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z46, 2)
    """State 3: End state"""
    return 0

def event_m10_23_x73(z45=302000):
    """[Execution] Lower the iron grid
    z45: Navigation change point ID
    """
    """State 0,1: Unload the bar"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(30, 0)
    """State 2: Navimesh attribute added"""
    AddNavimeshAttribute(z45, 2)
    """State 3: End state"""
    return 0

def event_m10_23_x74(z43=_, z44=_):
    """[Reproduction] When you break a wooden board, it becomes brighter
    z43: Wood board OBJ instance ID
    z44: Event light ID
    """
    """State 0,1: Is the wood board broken?"""
    if CompareOwnObjStateId(20, 0):
        """State 3: Is broken"""
        return 0
    else:
        """State 2: Small light OFF"""
        SetPointLightEnabled(z44, 0, 0)
        """State 4: Not broken"""
        return 1

def event_m10_23_x75(z43=_):
    """[Condition] Wood board destruction judgment
    z43: Wood board OBJ instance ID
    """
    """State 0,1: Wood board destruction waiting"""
    IsObjBroken(0, z43, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x76(z44=_):
    """[Execution] Small light on
    z44: Event light ID
    """
    """State 0,1: Small light on"""
    SetPointLightEnabled(z44, 1, 0.5)
    """State 2: End state"""
    return 0

def event_m10_23_x77(z43=_, z44=_):
    """[Preset] Brighten up by breaking the wooden board
    z43: Wood board OBJ instance ID
    z44: Event light ID
    """
    """State 0,1: [Reproduction] _SubState brightens when breaking a wooden board"""
    call = event_m10_23_x74(z43=z43, z44=z44)
    if call.Get() == 1:
        """State 2: [Condition] Wood board destruction judgment_SubState"""
        assert event_m10_23_x75(z43=z43)
    elif call.Get() == 0:
        pass
    """State 3: [Execution] Small light ON_SubState"""
    assert event_m10_23_x76(z44=z44)
    """State 4: End state"""
    return 0

def event_m10_23_x78(z39=10231410, z40=10231400, z41=10230030, z42=2):
    """[Reproduction] Large light judgment
    z39: OBJ instance ID of the wooden board on the entrance side
    z40: Door side wooden board OBJ instance ID
    z41: Large event light ID
    z42: Hit group ID
    """
    """State 0,1: Are the two wooden boards broken?"""
    if CompareObjStateId(z39, 20, 0) and CompareObjStateId(z40, 20, 0):
        """State 5: 2 wooden boards destroyed"""
        return 1
    else:
        """State 2: Event light large OFF"""
        SetPointLightEnabled(z41, 0, 0)
        """State 3: Brightness switch"""
        ChangeHitBrightnessSetting(z42, 0)
        """State 4: Not destroyed"""
        return 0

def event_m10_23_x79(z37=10231410, z38=10231400):
    """[Condition] Large light judgment
    z37: OBJ instance ID of the wooden board on the entrance side
    z38: Door side wooden board OBJ instance ID
    """
    """State 0,1: Wait for destruction of two wooden boards"""
    IsObjBroken(8, z37, 1)
    IsObjBroken(8, z38, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_23_x80(z35=10230030, z36=2):
    """[Execution] Large light determination
    z35: Large event light ID
    z36: Hit group ID
    """
    """State 0,1: Event Light University ON"""
    SetPointLightEnabled(z35, 1, 0.5)
    """State 2: Brightness switch"""
    ChangeHitBrightnessSetting(z36, 1)
    """State 3: End state"""
    return 0

def event_m10_23_x81():
    """[Reproduction] Working bridge"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x82(z34=10231510):
    """[Conditions] Working bridge
    z34: Lever OBJ instance ID
    """
    """State 0,1: [Preset] _SubState brightens when breaking a wooden board"""
    CompareObjState(0, z34, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x83(z32=500000, z33=123000032):
    """[Execution] Operation Bridge
    z32: Navigation change point ID
    z33: Enemy activation flag
    """
    """State 0,1: Working bridge animation playback"""
    ChangeOwnObjState(70)
    """State 3: Enemy activation flag ON"""
    SetEventFlag(z33, 1)
    assert CompareOwnObjStateId(20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z32, 2)
    """State 4: End state"""
    return 0

def event_m10_23_x84():
    """[Reproduction] Shortcut iron grid"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x85(z31=10231610):
    """[Conditions] Shortcut iron grid
    z31: Wall lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z31, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x86(z30=600000):
    """[Execution] Shortcut iron grid
    z30: Navigation change point ID
    """
    """State 0,1: Iron lattice animation playback"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z30, 2)
    """State 3: End state"""
    return 0

def event_m10_23_x87(z29=_):
    """[Preset] Hidden door 2_ Invisible key guide
    z29: Navigation change point ID
    """
    """State 0,1: [Reproduction] Hidden door 2_SubState"""
    assert event_m10_23_x88()
    """State 3: [Condition] Hidden door 2_SubState"""
    assert event_m10_23_x89()
    """State 2: [Execution] Hidden door 2_SubState"""
    assert event_m10_23_x90(z29=z29)
    """State 4: End state"""
    return 0

def event_m10_23_x88():
    """[Reproduction] Hidden door 2"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x89():
    """[Condition] Hidden door 2"""
    """State 0,1: Hidden door status judgment"""
    assert CompareOwnObjStateId(20, 0)
    """State 2: End state"""
    return 0

def event_m10_23_x90(z29=_):
    """[Execution] Hidden door 2
    z29: Navigation change point ID
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z29, 2)
    """State 2: End state"""
    return 0

def event_m10_23_x91():
    """[Reproduction] Rogue activation with plate destruction or view"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x92():
    """[Condition] Rogue activation with plate destruction or view"""
    """State 0,4: Black or red spirit?"""
    if ComparePlayerPhantom(7) != 0:
        pass
    elif ComparePlayerPhantom(8) != 0:
        pass
    elif ComparePlayerPhantom(9) != 0:
        pass
    elif ComparePlayerPhantom(10) != 0:
        pass
    else:
        Goto('L0')
    """State 7: Simple end"""
    return 1
    """State 1: Is the wooden board broken?"""
    Label('L0')
    IsObjBroken(0, 10231410, 1)
    IsObjBroken(1, 10231410, 0)
    if ConditionGroup(0):
        """State 3: Point intrusion standby"""
        IsPlayerInsidePoint(0, 163000, 163000, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(1):
        """State 2: Plate destruction or point entry standby"""
        IsObjBroken(0, 10231410, 1)
        IsPlayerInsidePoint(0, 163000, 163000, 1)
        assert ConditionGroup(0)
        """State 5: Point intrusion standby_2"""
        IsPlayerInsidePoint(0, 163000, 163010, 1)
        assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_23_x93():
    """[Execution] Rogue activation with plate destruction or view"""
    """State 0,1: Flag ON"""
    SetEventFlag(123020030, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x94():
    """[Preset] Rogue activation with plate destruction or view"""
    """State 0,1: [Reproduction] Rogue activation with sub-board destruction or view_SubState"""
    assert event_m10_23_x91()
    """State 2: [Condition] Rogue activation with sub-board destruction or view_SubState"""
    call = event_m10_23_x92()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Execution] Rogue activation with sub-board destruction or view_SubState"""
        assert event_m10_23_x93()
    """State 4: End state"""
    return 0

def event_m10_23_x95():
    """[Reproduction] Opening door or approaching rogue"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x96():
    """[Condition] Rogue starts when door is opened or approached"""
    """State 0,2: Black or red spirit?"""
    if ComparePlayerPhantom(7) != 0:
        pass
    elif ComparePlayerPhantom(8) != 0:
        pass
    elif ComparePlayerPhantom(10) != 0:
        pass
    elif ComparePlayerPhantom(9) != 0:
        pass
    else:
        """State 1: Open the door or wait for point intrusion"""
        CompareEventFlag(0, 123020031, 1)
        IsPlayerInsidePoint(1, 164000, 164000, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 4: Flag stand"""
            return 1
    """State 3: Simple end"""
    return 0

def event_m10_23_x97():
    """[Execution] Rogue activated by opening door or approaching"""
    """State 0,1: Start flag ON"""
    SetEventFlag(123020031, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x98():
    """[Preset] Rogue activated by opening door or approaching"""
    """State 0,1: [Reproduction] Rogue activation by opening the door or approaching_SubState"""
    assert event_m10_23_x95()
    """State 2: [Condition] Rogue activated by opening door or approaching_SubState"""
    call = event_m10_23_x96()
    if call.Get() == 0:
        pass
    elif call.Done():
        """State 3: [Execution] Rogue activated by opening door or approaching_SubState"""
        assert event_m10_23_x97()
    """State 4: End state"""
    return 0

def event_m10_23_x99():
    """[Reproduction] Chariots immortal release"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x100():
    """[Conditions] Chariots immortal cancellation"""
    """State 0,1: HP drop & area intrusion standby"""
    IsChrInsidePoint(8, 816, 310010, 310010, 1)
    CompareChrHpRatio(8, 816, 30, 5)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_23_x101():
    """[Execution] Chariots immortal release"""
    """State 0,1: Chariot immortal release"""
    SetEnemySpEffect(816, 96191020, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_23_x102():
    """[Preset] Chariots immortal release"""
    """State 0,1: [Reproduction] Chariots immortal release_SubState"""
    assert event_m10_23_x99()
    """State 2: [Condition] Chariots immortal release_SubState"""
    assert event_m10_23_x100()
    """State 3: [Execution] Chariots immortal release_SubState"""
    assert event_m10_23_x101()
    """State 4: End state"""
    return 0

def event_m10_23_x103():
    """[Reproduction] Create another enemy by destroying the enemy _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x104(z2=_):
    """[Condition] Create another enemy by destroying the enemy
    z2: Death enemy ID
    """
    """State 0,1: Enemy death waiting"""
    IsChrDead(0, z2)
    assert ConditionGroup(0)
    """State 2: Time lapse state"""
    assert (GetStateTime() > 6) != 0
    """State 3: End state"""
    return 0

def event_m10_23_x105(val1=_, val2=_, val3=_, val4=_, val5=_, z26=_, z27=_, z28=_):
    """[Execution] Create another enemy by destroying the enemy
    val1: Operation generator ID_1
    val2: Operation generator ID_2
    val3: Operation generator ID_3
    val4: Operation generator ID_4
    val5: Operation generator ID_5
    z26: Death enemy ID
    z27: Generation point start ID
    z28: Generation point end ID
    """
    """State 0,6: Does the generator exist?"""
    if (not val1) != 0:
        pass
    else:
        """State 11: Time lapse state_2"""
        assert (GetStateTime() > 0.3) != 0
        """State 1: Generator operation"""
        ForceGenerationFromPointBasedOnPosition(val1, z26, z27, z28, 1, 0)
    """State 7: Does the generator exist? _2"""
    if (not val2) != 0:
        pass
    else:
        """State 12: Elapsed state_3"""
        assert (GetStateTime() > 1.2) != 0
        """State 2: Generator operation_2"""
        ForceGenerationFromPointBasedOnPosition(val2, z26, z27, z28, 2, 0)
    """State 8: Does the generator exist? _3"""
    if (not val3) != 0:
        pass
    else:
        """State 13: Time elapsed state_4"""
        assert (GetStateTime() > 2) != 0
        """State 3: Generator operation_3"""
        ForceGenerationFromPointBasedOnPosition(val3, z26, z27, z28, 3, 0)
    """State 9: Does the generator exist? _Four"""
    if (not val4) != 0:
        pass
    else:
        """State 14: Elapsed state_5"""
        assert (GetStateTime() > 0.8) != 0
        """State 4: Generator operation_4"""
        ForceGenerationFromPointBasedOnPosition(val4, z26, z27, z28, 4, 0)
    """State 10: Does the generator exist? _Five"""
    if (not val5) != 0:
        pass
    else:
        """State 15: Time elapsed state_6"""
        assert (GetStateTime() > 1.7) != 0
        """State 5: Generator operation_5"""
        ForceGenerationFromPointBasedOnPosition(val5, z26, z27, z28, 5, 0)
    """State 16: End state"""
    return 0

def event_m10_23_x106(z26=_, val1=_, val2=_, val3=_, val4=_, val5=_, z27=_, z28=_):
    """[Preset] Create another enemy by destroying the enemy
    z26: Death enemy ID
    val1: Operation generator ID_1
    val2: Operation generator ID_2
    val3: Operation generator ID_3
    val4: Operation generator ID_4
    val5: Operation generator ID_5
    z27: Generation point start ID
    z28: Generation point end ID
    """
    """State 0,1: [Reproduction] Creating another enemy by destroying the enemy_Sky_SubState"""
    assert event_m10_23_x103()
    """State 2: [Condition] Another enemy created by destroying an enemy_SubState"""
    assert event_m10_23_x104(z2=z26)
    """State 3: [Execute] Create another enemy by destroying the enemy_SubState"""
    assert (event_m10_23_x105(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, z26=z26, z27=z27,
            z28=z28))
    """State 4: End state"""
    return 0

def event_m10_23_x107():
    """[Reproduction] Opening the door and starting rogue"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x108():
    """[Condition] Rogue starts when door is opened"""
    """State 0,4: Black or red spirit?"""
    if ComparePlayerPhantom(7) != 0:
        pass
    elif ComparePlayerPhantom(8) != 0:
        pass
    elif ComparePlayerPhantom(9) != 0:
        pass
    elif ComparePlayerPhantom(10) != 0:
        pass
    else:
        Goto('L0')
    """State 7: Simple end"""
    return 1
    """State 1: Is the door broken or already open?"""
    Label('L0')
    if DoorOpen(0) != 1:
        """State 2: Point intrusion standby"""
        IsPlayerInsidePoint(0, 164000, 164005, 1)
        assert ConditionGroup(0)
    else:
        """State 3: Open the door or wait for destruction"""
        assert DoorOpen(0) != 1
        """State 5: Point intrusion standby_2"""
        IsPlayerInsidePoint(0, 164000, 164005, 1)
        assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_23_x109():
    """[Execution] Rogue activated by opening the door"""
    """State 0,1: Start flag ON"""
    SetEventFlag(123020031, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x110():
    """[Preset] Rogue activated by opening the door"""
    """State 0,1: [Reproduction] Rogue activation by opening the door_empty_SubState"""
    assert event_m10_23_x107()
    """State 2: [Condition] Rogue starts by opening the door_SubState"""
    call = event_m10_23_x108()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Execution] Rogue activation by opening the door_SubState"""
        assert event_m10_23_x109()
    """State 4: End state"""
    return 0

def event_m10_23_x111():
    """[Reproduction] Pile torture person activation _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x112(z22=_, z23=_, z25=173010):
    """[Conditions] Pile torturer activation
    z22: Intrusion area ID_before
    z23: After intrusion area ID_
    z25: Intrusion area ID_reverse run
    """
    """State 0,2: Black or red spirit?"""
    if ComparePlayerPhantom(7) != 0:
        pass
    elif ComparePlayerPhantom(8) != 0:
        pass
    elif ComparePlayerPhantom(9) != 0:
        pass
    elif ComparePlayerPhantom(10) != 0:
        pass
    elif ComparePlayerPhantom(5) != 0:
        pass
    elif ComparePlayerPhantom(6) != 0:
        pass
    else:
        Goto('L0')
    """State 5: Simple end"""
    return 1
    """State 1: Point intrusion standby"""
    Label('L0')
    IsPlayerInsidePoint(0, z22, z23, 1)
    IsPlayerInsidePoint(1, z25, z25, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Time elapse or point escape standby"""
        IsPlayerInsidePoint(0, z22, z23, 0)
        CompareStateTime(0, 5, 3, 5)
        assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_23_x113(z20=_):
    """[Execution] Pile torturer launch
    z20: Torturer starting flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z20, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x114(z22=_, z23=_, z24=_, z25=173010):
    """[Preset] Pile torturer launch
    z22: Intrusion area ID_before
    z23: After intrusion area ID_
    z24: Torturer starting flag
    z25: Intrusion area ID_reverse run
    """
    """State 0,1: [Reproduction] Pile-top torture person activation _ empty _SubState"""
    assert event_m10_23_x111()
    """State 2: [Conditions] Pile torturer activation_SubState"""
    call = event_m10_23_x112(z22=z22, z23=z23, z25=z25)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Execution] Pile torturer activation_SubState"""
        assert event_m10_23_x113(z20=z24)
    """State 4: End state"""
    return 0

def event_m10_23_x115(z18=171000, z19=171010, z21=173010):
    """[Condition] Pile torturer activation_2
    z18: Intrusion area ID_before
    z19: After intrusion area ID_
    z21: Intrusion area ID_reverse run
    """
    """State 0,2: Black or red spirit?"""
    if ComparePlayerPhantom(7) != 0:
        pass
    elif ComparePlayerPhantom(8) != 0:
        pass
    elif ComparePlayerPhantom(9) != 0:
        pass
    elif ComparePlayerPhantom(10) != 0:
        pass
    elif ComparePlayerPhantom(5) != 0:
        pass
    elif ComparePlayerPhantom(6) != 0:
        pass
    else:
        Goto('L0')
    """State 5: Simple end"""
    return 1
    """State 1: Point intrusion standby"""
    Label('L0')
    IsPlayerInsidePoint(0, z18, z19, 1)
    IsPlayerInsidePoint(1, z21, z21, 1)
    if ConditionGroup(0):
        """State 3: Time elapse or point escape standby"""
        IsPlayerInsidePoint(0, z18, z19, 0)
        CompareStateTime(0, 5, 3, 5)
        IsChrDead(8, 5010)
        SetConditionGroup(8, 0)
        if ConditionGroup(8):
            pass
        elif ConditionGroup(0):
            """State 6: End state_2"""
            return 2
    elif ConditionGroup(1):
        pass
    """State 4: End state"""
    return 0

def event_m10_23_x116(z18=171000, z19=171010, z20=123020004, z21=173010):
    """[Preset] Pile torturer activation_2
    z18: Intrusion area ID_before
    z19: After intrusion area ID_
    z20: Torturer starting flag
    z21: Intrusion area ID_reverse run
    """
    """State 0,1: [Reproduction] Pile-top torture person activation _ empty _SubState"""
    assert event_m10_23_x111()
    """State 4: [Conditions] Pile torturer activation_SubState"""
    call = event_m10_23_x115(z18=z18, z19=z19, z21=z21)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 3: [Execution] Pile torturer activation_2_SubState"""
        assert event_m10_23_x117()
    elif call.Done():
        """State 2: [Execution] Pile torturer activation_SubState"""
        assert event_m10_23_x113(z20=z20)
    """State 5: End state"""
    return 0

def event_m10_23_x117():
    """[Execution] Pile torturer launch_2"""
    """State 0,1: Start flag ON"""
    SetEventFlag(123020006, 1)
    assert (GetStateTime() > 0.5) != 0
    """State 2: Startup flag ON_2"""
    SetEventFlag(123020005, 1)
    assert (GetStateTime() > 0.3) != 0
    """State 3: Startup flag ON_3"""
    SetEventFlag(123020004, 1)
    """State 4: End state"""
    return 0

def event_m10_23_x118(z14=10231460, z15=10231450):
    """[Reproduction] Hunting Forest-Tame Valley Operation Bridge
    z14: Bridge instance ID
    z15: Lever instance ID
    """
    """State 0,3: Event ends for guests"""
    if IsGuest() != 0:
        """State 6: Simple end"""
        return 1
    else:
        """State 1: OBJ state initialization: working bridge"""
        InitializeObj(z14)
        """State 2: Enable key guide for lever"""
        DisableObjKeyGuide(z15, 0)
        """State 4: Navigation mesh change"""
        AddNavimeshAttribute(2000000, 2)
        """State 5: End state"""
        return 0

def event_m10_23_x119(z15=10231450):
    """[Conditions] Hunting Forest-Tame Valley Operation Bridge
    z15: Lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z15, 74, 0)
    CompareObjState(0, z15, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x120(z14=10231460, z15=10231450, z16=2000001, z17=2000002):
    """[Execution] Hunting Forest-Tame Valley Operation Bridge
    z14: Bridge instance ID
    z15: Lever instance ID
    z16: Point ID for bridge initialization determination_start
    z17: Point ID for bridge initialization determination_end
    """
    """State 0,1: OBJ state transition: Working bridge: 70"""
    ChangeObjState(z14, 70)
    """State 2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z15, 1)
    """State 5: Has the moving bridge animation ended?"""
    CompareObjState(0, z14, 20, 0)
    assert ConditionGroup(0)
    """State 4: Navigation mesh change"""
    DeleteNavimeshAttribute(2000000, 2)
    """State 3: Did you enter the specified point?"""
    IsPlayerInsidePoint(0, z16, z17, 1)
    assert ConditionGroup(0)
    """State 6: OBJ state transition: Working bridge: 71"""
    ChangeObjState(z14, 71)
    """State 7: Has the moving bridge animation ended? _2"""
    CompareObjState(0, z14, 10, 0)
    assert ConditionGroup(0)
    """State 8: End state"""
    return 0

def event_m10_23_x121(z14=10231460, z15=10231450, z16=2000001, z17=2000002):
    """[Preset] Hunting Forest-Tame Valley Operation Bridge
    z14: Bridge instance ID
    z15: Lever instance ID
    z16: Point ID for bridge initialization determination_start
    z17: Point ID for bridge initialization determination_end
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z14, 0)
    """State 2: [Reproduction] Hunting Forest-Tame Valley Operation Bridge_SubState"""
    call = event_m10_23_x118(z14=z14, z15=z15)
    if call.Get() == 1:
        """State 6: End state_2"""
        return 1
    elif call.Done():
        """State 3: [Conditions] Hunting Forest-Tame Valley Operation Bridge_SubState"""
        assert event_m10_23_x119(z15=z15)
        """State 4: [Execution] Hunting Forest-Tame Valley Operation Bridge_SubState"""
        assert event_m10_23_x120(z14=z14, z15=z15, z16=z16, z17=z17)
        """State 5: End state"""
        return 0

def event_m10_23_x122(z11=840, z12=841, z13=123020035):
    """[Preset] Skeleton aristocrat_cane_big explosion
    z11: Enemy generator ID1 for performing death checks
    z12: Enemy generator ID2 for performing death checks
    z13: Skeleton aristocratic explosion flag
    """
    """State 0,1: [Reproduction] Skeleton aristocrat_cane_explosion_SubState"""
    assert event_m10_23_x123()
    """State 2: [Conditions] Skeleton aristocrat_Wand_Large explosion_SubState"""
    assert event_m10_23_x124(z11=z11, z12=z12)
    """State 3: [Execution] Skeleton aristocrat_Cane_Large explosion_SubState"""
    assert event_m10_23_x125(z13=z13)
    """State 4: End state"""
    return 0

def event_m10_23_x123():
    """[Reproduction] Skeleton aristocrat_cane_big explosion"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x124(z11=840, z12=841):
    """[Conditions] Skeleton aristocrat_cane_big explosion
    z11: Enemy generator ID1 for performing death checks
    z12: Enemy generator ID2 for performing death checks
    """
    """State 0,1: Is the skeleton aristocrat sickle or ax moth dead?"""
    IsChrDead(0, z11)
    IsChrDead(0, z12)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x125(z13=123020035):
    """[Execution] Skeleton aristocrat_cane_big explosion
    z13: Skeleton aristocratic explosion flag
    """
    """State 0,1: Action 23 Big explosion flag ON"""
    SetEventFlag(z13, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x126(z7=1023010, z8=123000081, z9=10234900, z10=10234910):
    """[Preset] Chariot's iron grid and lever _ state reproduction
    z7: Boss Battle ID
    z8: Boss destruction flag
    z9: Instance ID of the iron lattice OBJ
    z10: Lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Chariot's iron grid and lever_state reproduction_SubState"""
    call = event_m10_23_x127(z10=z10)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Chariot's iron grid and lever_state reproduction_SubState"""
        call = event_m10_23_x128(z7=z7, z8=z8, z9=z9)
        if call.Get() == 1:
            """State 3: [Execution] Chariot's iron grid and lever _ State reproduction _ Initialization _ SubState"""
            assert event_m10_23_x129(z9=z9, z10=z10)
        elif call.Get() == 2:
            """State 4: [Execution] Chariot's iron grid and lever_State reproduction_Key guide disabled_SubState"""
            assert event_m10_23_x130(z10=z10)
        elif call.Get() == 0:
            pass
    """State 5: End state"""
    return 0

def event_m10_23_x127(z10=10234910):
    """[Reproduction] Chariot's iron grid and lever_state reproduction
    z10: Lever OBJ instance ID
    """
    """State 0,1: Are you a guest?"""
    if IsGuest() != 0:
        """State 4: The guests"""
        return 1
    else:
        """State 2: Enable key guide for lever"""
        DisableObjKeyGuide(z10, 0)
        """State 3: host"""
        return 0

def event_m10_23_x128(z7=1023010, z8=123000081, z9=10234900):
    """[Conditions] Chariot's iron grid and lever_state reproduction
    z7: Boss Battle ID
    z8: Boss destruction flag
    z9: Instance ID of the iron lattice OBJ
    """
    """State 0,1: Did you destroy the boss or boss during the boss battle?"""
    IsEventBossBattle(0, z7, 1)
    CompareEventFlag(0, z8, 1)
    if ConditionGroup(0):
        """State 2: Is the iron grid broken?"""
        CompareObjState(0, z9, 20, 0)
        CompareObjState(0, z9, 72, 0)
        if ConditionGroup(0):
            """State 6: Disable key guide"""
            return 2
        else:
            """State 3: Is the barred?"""
            CompareObjState(0, z9, 30, 0)
            CompareObjState(0, z9, 70, 0)
            if ConditionGroup(0):
                pass
            else:
                """State 4: End state"""
                return 0
    else:
        pass
    """State 5: Initialization process"""
    return 1

def event_m10_23_x129(z9=10234900, z10=10234910):
    """[Execution] Chariot's iron grid and lever _ State reproduction _ Initialization
    z9: Instance ID of the iron lattice OBJ
    z10: Lever OBJ instance ID
    """
    """State 0,1: Iron grid and lever initialization"""
    InitializeObj(z9)
    InitializeObj(z10)
    """State 2: End state"""
    return 0

def event_m10_23_x130(z10=10234910):
    """[Execution] Chariot's iron grid and lever _ State reproduction _ Key guide disabled
    z10: Lever OBJ instance ID
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z10, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x131():
    """[Reproduction] Skeleton immortality management_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x132(z6=_, z5=_):
    """[Conditions] Skeleton immortality management
    z6: Dark Wizard generator ID
    z5: Skeleton generator ID
    """
    """State 0,1: Skeleton and dark wizard judgment"""
    IsChrDead(0, z6)
    IsChrMaxRespawnCount(0, z6, 1, 0)
    CompareChrEzStateValue(1, z6, 7, 1, 0)
    IsChrDead(2, z5)
    if ConditionGroup(2):
        """State 4: Skeleton death: do nothing"""
        return 2
    elif ConditionGroup(0):
        """State 2: Upper limit or death: cancel immortality"""
        return 0
    elif ConditionGroup(1):
        """State 3: Resurrection behavior: Resurrection processing"""
        return 1

def event_m10_23_x133(z5=_):
    """[Execution] Skeleton immortality management_release
    z5: Skeleton generator ID
    """
    """State 0,1: Special effect grant: Immortal release"""
    SetEnemySpEffect(z5, 91320030, 19, 4)
    assert (GetStateTime() >= 0) != 0
    """State 2: [DC] Is the skeleton's HP 1 or less?"""
    CompareChrHpValue(0, z5, 1, 5)
    assert ConditionGroup(0)
    """State 3: [DC] Special effects: suicide"""
    SetEnemySpEffect(z5, 91320020, 19, 4)
    """State 4: Finish"""
    return 0

def event_m10_23_x134(z5=_, z6=_):
    """[Execution] Skeleton immortality management_Resurrection
    z5: Skeleton generator ID
    z6: Dark Wizard generator ID
    """
    """State 0,3: Skip if not running"""
    CompareChrStartUpState(0, z5, 0, 0)
    CompareChrStartUpState(1, z5, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: Special effects: Resurrection processing"""
        SetEnemySpEffect(z5, 91320010, 19, 4)
    """State 2: Wait for next decision"""
    CompareChrEzStateValue(0, z6, 7, 0, 0)
    IsChrDead(0, z6)
    IsChrDead(0, z5)
    assert ConditionGroup(0)
    """State 4: Finish"""
    return 0

def event_m10_23_x135(z5=_, z6=_):
    """[Preset] Skeleton immortality management
    z5: Skeleton generator ID
    z6: Dark Wizard generator ID
    """
    """State 0,1: [Reproduction] Skeleton immortality management_sky_SubState"""
    assert event_m10_23_x131()
    """State 4: [Condition] Skeleton immortality management_SubState"""
    call = event_m10_23_x132(z6=z6, z5=z5)
    if call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Skeleton immortality management_Release_SubState"""
        assert event_m10_23_x133(z5=z5)
    elif call.Get() == 1:
        """State 3: [Execution] Skeleton immortality management_Resurrection_SubState"""
        assert event_m10_23_x134(z5=z5, z6=z6)
        """State 6: Rerun"""
        return 1
    """State 5: Finish"""
    return 0

def event_m10_23_x136(z2=841, z3=702000, z4=702049):
    """[DC] [execution] Another enemy generation by destroying enemies _12 body version
    z2: Death enemy ID
    z3: Generation point start ID
    z4: Generation point end ID
    """
    """State 0,6: Elapsed state_1"""
    assert (GetStateTime() > 0.3) != 0
    """State 1: Generator operation"""
    ForceGenerationFromPointBasedOnPosition(5220, z2, z3, z4, 1, 0)
    """State 7: Time lapse state_2"""
    assert (GetStateTime() > 0.6) != 0
    """State 2: Generator operation_2"""
    ForceGenerationFromPointBasedOnPosition(5221, z2, z3, z4, 2, 0)
    """State 8: Elapsed state_3"""
    assert (GetStateTime() > 1) != 0
    """State 3: Generator operation_3"""
    ForceGenerationFromPointBasedOnPosition(5222, z2, z3, z4, 3, 0)
    """State 9: Time elapsed state_4"""
    assert (GetStateTime() > 0.4) != 0
    """State 4: Generator operation_4"""
    ForceGenerationFromPointBasedOnPosition(5223, z2, z3, z4, 4, 0)
    """State 10: Elapsed state_5"""
    assert (GetStateTime() > 0.9) != 0
    """State 5: Generator operation_5"""
    ForceGenerationFromPointBasedOnPosition(5224, z2, z3, z4, 5, 0)
    """State 12: Time elapsed state_6"""
    assert (GetStateTime() > 0.2) != 0
    """State 11: Generator operation_6"""
    ForceGenerationFromPointBasedOnPosition(5225, z2, z3, z4, 6, 0)
    """State 14: Elapsed state_7"""
    assert (GetStateTime() > 0.3) != 0
    """State 13: Generator operation_7"""
    ForceGenerationFromPointBasedOnPosition(5226, z2, z3, z4, 7, 0)
    """State 16: Elapsed state_8"""
    assert (GetStateTime() > 1.2) != 0
    """State 15: Generator operation_8"""
    ForceGenerationFromPointBasedOnPosition(5227, z2, z3, z4, 8, 0)
    """State 18: Elapsed state_9"""
    assert (GetStateTime() > 0.6) != 0
    """State 17: Generator operation_9"""
    ForceGenerationFromPointBasedOnPosition(5228, z2, z3, z4, 9, 0)
    """State 20: Time lapse state_10"""
    assert (GetStateTime() > 0.6) != 0
    """State 19: Generator operation_10"""
    ForceGenerationFromPointBasedOnPosition(5229, z2, z3, z4, 10, 0)
    """State 22: Time elapsed state_11"""
    assert (GetStateTime() > 0.3) != 0
    """State 21: Generator operation_11"""
    ForceGenerationFromPointBasedOnPosition(5230, z2, z3, z4, 11, 0)
    """State 24: [Others] Boss battle started"""
    assert (GetStateTime() > 0.2) != 0
    """State 23: Generator operation_12"""
    ForceGenerationFromPointBasedOnPosition(5231, z2, z3, z4, 12, 0)
    """State 25: End state"""
    return 0

def event_m10_23_x137(z2=841, z3=702000, z4=702049):
    """[DC] [Preset] 12 enemy versions generated by destroying enemies
    z2: Death enemy ID
    z3: Generation point start ID
    z4: Generation point end ID
    """
    """State 0,1: [Reproduction] Creating another enemy by destroying the enemy_Sky_SubState"""
    assert event_m10_23_x103()
    """State 2: [Condition] Another enemy created by destroying an enemy_SubState"""
    assert event_m10_23_x104(z2=z2)
    """State 3: [DC] [Execution] Another enemy generation by destroying an enemy_12 body version_SubState"""
    assert event_m10_23_x136(z2=z2, z3=z3, z4=z4)
    """State 4: End state"""
    return 0

def event_m10_23_x138(flag1=123000086, z1=123020087):
    """[DC] [Preset] NPC White Spirit_Gesture Management_Skeleton Nobility
    flag1: Boss destruction flag
    z1: Gesture flag
    """
    """State 0,1: [DC] [Reproduction] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
    call = event_m10_23_x139(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Conditions] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
        assert event_m10_23_x140()
        """State 2: [DC] [Execution] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
        assert event_m10_23_x141(z1=z1)
    """State 4: End state"""
    return 0

def event_m10_23_x139(flag1=123000086):
    """[DC] [Reproduction] NPC White Spirit_Gesture Management_Skeleton Nobility
    flag1: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag1) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_23_x140():
    """[DC] [Conditions] NPC White Spirit_Gesture Management_Skeleton Nobility"""
    """State 0,1: Has the HP of all wheel skeletons dropped below 0?"""
    CompareChrHpValue(8, 5200, 0, 5)
    CompareChrHpValue(8, 5201, 0, 5)
    assert ConditionGroup(8)
    """State 2: Has the armor skeleton's HP dropped below 0?"""
    CompareChrHpValue(8, 5210, 0, 5)
    CompareChrHpValue(8, 5211, 0, 5)
    CompareChrHpValue(8, 5212, 0, 5)
    CompareChrHpValue(8, 5213, 0, 5)
    CompareChrHpValue(8, 5214, 0, 5)
    assert ConditionGroup(8)
    """State 3: Has the HP of all skeletons become 0 or less?"""
    CompareChrHpValue(8, 5220, 0, 5)
    CompareChrHpValue(8, 5221, 0, 5)
    CompareChrHpValue(8, 5222, 0, 5)
    CompareChrHpValue(8, 5223, 0, 5)
    CompareChrHpValue(8, 5224, 0, 5)
    CompareChrHpValue(8, 5225, 0, 5)
    CompareChrHpValue(8, 5226, 0, 5)
    CompareChrHpValue(8, 5227, 0, 5)
    CompareChrHpValue(8, 5228, 0, 5)
    CompareChrHpValue(8, 5229, 0, 5)
    CompareChrHpValue(8, 5230, 0, 5)
    CompareChrHpValue(8, 5231, 0, 5)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_23_x141(z1=123020087):
    """[DC] [Execution] NPC White Spirit_Gesture Management_Skeleton Nobility
    z1: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z1, 1)
    """State 2: End state"""
    return 0

def event_m10_23_111232():
    """NPC: Wandering Warrior: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_23_x0(z124=104151, z125=10234200, z126=56, z127=7420)
    Quit()

def event_m10_23_111233():
    """NPC: Wandering Warrior: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_23_x3(z119=123010110, z120=123020111, z121=104150, z122=10234200, z123=111232, npc1=7420)
    Quit()

def event_m10_23_111234():
    """NPC: Wanderer Warrior: Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_23_x5(z113=55, z114=104151)
    Quit()

def event_m10_23_111422():
    """NPC: Darkness Shop: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_23_x0(z124=104330, z125=10234000, z126=156, z127=7700)
    Quit()

def event_m10_23_111423():
    """NPC: Dark Art Shop: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7700:Felkin the Outcast
    event_m10_23_x3(z119=123010130, z120=123020131, z121=104330, z122=10234000, z123=111422, npc1=7700)
    Quit()

def event_m10_23_111472():
    """NPC: Black Phantom Shop: Grave"""
    """State 0,1: NPC: Black Phantom Shop: Grave Placement_SubState"""
    event_m10_23_x0(z124=104380, z125=10234100, z126=276, z127=7830)
    Quit()

def event_m10_23_111473():
    """NPC: Black Phantom Shop: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7830:Titchy Gren
    event_m10_23_x3(z119=123010120, z120=123020121, z121=104380, z122=10234100, z123=111472, npc1=7830)
    Quit()

def event_m10_23_118100():
    """Multi-use NPC: White Spirit Test 1: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_23_x31(z83=586)
    Quit()

def event_m10_23_118110():
    """Multi-use NPC: Clayton: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_23_x22(z88=102405, z89=587, z90=104150, z91=60, z92=103650, z93=-1)
    Quit()

def event_m10_23_118210():
    """Multi-use NPC: Shinigami (Female): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_23_x42(z69=12000000, z70=580, z71=0, z72=2)
    Quit()

def event_m10_23_120020():
    """Trophy: Pledge for blood"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_23_x43(flag5=123020127, z68=20)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_23_4000000():
    """[DC] Wanderer A_ fixed appearance"""
    """State 0,2: [Lib] [Preset] Wanderer_Fixed Appearance_SubState"""
    assert event_m10_23_x64(z50=6000000, z51=6000000, z52=0, z53=2, z54=944, z55=123020043)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_23_x56(flag3=123000042, z58=944, mode1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_23_x60(z56=9500, z57=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4031000():
    """[DC] NPC White Spirit_Gesture Management_Silver Chariots"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_23_x68(flag2=123000081, z48=816, z49=123020084)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_23_4031010():
    """[DC] NPC White Spirit_Gesture Management_Skeleton Nobility"""
    """State 0,2: [DC] [Preset] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
    assert event_m10_23_x138(flag1=123000086, z1=123020087)
    """State 1: Finish"""
    EndMachine()
    Quit()

