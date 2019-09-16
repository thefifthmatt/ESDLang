# -*- coding: utf-8 -*-
def event_m10_23_10():
    """Duel start"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel start_SubState"""
    assert (event_m10_23_x32(z80=10231800, z81=10231801, z82=10231802, z83=10231803, z84=10231804, z85=10231805,
            z86=10, z87=17))
    """State 1: Finish"""
    EndMachine()

def event_m10_23_1200():
    """Falling tree_Navimesh change"""
    """State 0,2: [Lib] [Preset] Falling tree _SubState"""
    assert event_m10_23_x30(z89=10231200, z90=120010)
    """State 1: End notification"""
    EndMachine()

def event_m10_23_1400():
    """Rogue activation with plate destruction or view"""
    """State 0,2: [Preset] Rogue activation or SubState with board destruction or view"""
    assert event_m10_23_x94()
    """State 1: Finish"""
    EndMachine()

def event_m10_23_1410():
    """Rogue activated by opening door or approaching"""
    """State 0,2: [Preset] Opening door or approaching Rogue _SubState"""
    assert event_m10_23_x98()
    """State 1: Finish"""
    EndMachine()

def event_m10_23_1411():
    """Rogue activated by opening door * Deleted after state support"""
    """State 0,2: [Preset] Rogue activated by opening the door_SubState"""
    assert event_m10_23_x110()
    """State 1: Finish"""

def event_m10_23_1700():
    """Launch of torturer on pile_1"""
    """State 0,2: [Preset] Pile torturer activation_SubState"""
    assert event_m10_23_x114(z23=170000, z24=170010, z25=123020003, z26=173010)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_1710():
    """Launch of torturer on pile_2"""
    """State 0,2: [Preset] Pile torturer activation_2_SubState"""
    assert event_m10_23_x116(z19=171000, z20=171010, z21=123020004, z22=173010)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_1720():
    """Launch of torture person on the pile_3rd body"""
    """State 0,2: [Preset] Pile torturer activation_SubState"""
    assert event_m10_23_x114(z23=172000, z24=172010, z25=123020005, z26=173010)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_1730():
    """Launch of torture person on the pile_4th body"""
    """State 0,2: [Preset] Pile torturer activation_SubState"""
    assert event_m10_23_x114(z23=173000, z24=173010, z25=123020006, z26=173010)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_3010():
    """Chariot's iron grid and lever"""
    """State 0,2: [Preset] Chariot's iron grid and lever_state reproduction_SubState"""
    assert event_m10_23_x126(z8=1023010, z9=123000081, z10=10234900, z11=10234910)
    """State 1: Finish"""
    EndMachine()

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
            assert event_m10_23_x73(z46=302000)
        elif call.Get() == 1:
            """State 8: [Execution] Raise the iron grid_SubState"""
            assert event_m10_23_x72(z47=302000)
        elif call.Get() == 2:
            """State 6: [Execution] Destroy iron lattice and carriage_SubState"""
            assert event_m10_23_x71(z48=302000)
            Goto('L0')
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    else:
        pass
    """State 2: Finish"""
    Label('L0')
    EndMachine()

def event_m10_23_3100():
    """Chariot immortal release"""
    """State 0,2: [Preset] Chariots immortal release_SubState"""
    assert event_m10_23_x102()
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4000():
    """The entrance side becomes brighter when the wooden board is broken"""
    """State 0,2: [Preset] _SubState brightens when breaking a wooden board"""
    assert event_m10_23_x77(z44=10231410, z45=10230010)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4010():
    """The door side becomes brighter when the wooden board is broken"""
    """State 0,2: [Preset] _SubState brightens when breaking a wooden board"""
    assert event_m10_23_x77(z44=10231400, z45=10230020)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4020():
    """Breaking a wooden board makes it brighter"""
    """State 0,2: [Reproduction] Large light determination_SubState"""
    call = event_m10_23_x78(z40=10231410, z41=10231400, z42=10230030, z43=2)
    if call.Get() == 0:
        """State 3: [Condition] Large light determination_SubState"""
        assert event_m10_23_x79(z38=10231410, z39=10231400)
    elif call.Get() == 1:
        pass
    """State 4: [Execution] Large light determination_SubState"""
    assert event_m10_23_x80(z36=10230030, z37=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_5000():
    """Working bridge"""
    """State 0,2: Disable OBJ sync"""
    SetObjSync(10231500, 0)
    """State 3: [Reproduction] Operation Bridge_SubState"""
    assert event_m10_23_x81()
    """State 5: [Condition] Working bridge_SubState"""
    assert event_m10_23_x82(z35=10231510)
    """State 4: [Execution] Operation Bridge_SubState"""
    assert event_m10_23_x83(z33=500000, z34=123000032)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_6000():
    """Shortcut iron lattice_cave route"""
    """State 0,2: Disable OBJ sync"""
    SetObjSync(10231600, 0)
    """State 3: [Reproduction] Shortcut iron grid_SubState"""
    assert event_m10_23_x84()
    """State 5: [Condition] Shortcut iron grid_SubState"""
    assert event_m10_23_x85(z32=10231610)
    """State 4: [Execution] Shortcut iron grid_SubState"""
    assert event_m10_23_x86(z31=600000)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_7000():
    """Generate enemy upon death of skeleton aristocrat_1"""
    """State 0,2: [Preset] Create another enemy by destroying the enemy_SubState"""
    assert event_m10_23_x106(z27=839, val1=5200, val2=5201, val3=0, val4=0, val5=0, z28=700000, z29=700049)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_7010():
    """Enemy generation upon death of skeleton aristocrat_2"""
    """State 0,2: [Preset] Create another enemy by destroying the enemy_SubState"""
    assert (event_m10_23_x106(z27=840, val1=5210, val2=5211, val3=5212, val4=5213, val5=5214, z28=701000,
            z29=701049))
    """State 1: Finish"""
    EndMachine()

def event_m10_23_7020():
    """Enemy generation when skeleton nobleman dies_3"""
    """State 0,2: [DC] [Preset] Enemy Destroy creates another enemy_12 body version_SubState"""
    assert event_m10_23_x137(z3=841, z4=702000, z5=702049)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_7030():
    """Skeleton aristocrat_cane_explosive behavior"""
    """State 0,2: [Preset] Skeleton Aristocrat_Cane_Large Explosion_SubState"""
    assert event_m10_23_x122(z12=840, z13=841, z14=123020035)
    """State 1: Finish"""
    EndMachine()

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

def event_m10_23_8010():
    """Chair 1 seat where skeleton nobility sits"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_23_x18(z99=10231750, z100=20, z101=801000, z102=0, z103=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_8020():
    """The skeleton aristocratic chair 2_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_23_x18(z99=10231751, z100=20, z101=802000, z102=0, z103=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_8030():
    """Chair 3 seat where skeleton nobility sits"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_23_x18(z99=10231752, z100=20, z101=803000, z102=0, z103=2)
    """State 1: Finish"""
    EndMachine()

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

def event_m10_23_10000():
    """Key door_Fire room"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_23_x4(z120=1005, z121=1105, z122=50970000, z123=123000020)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_11000():
    """Switching of Madura's revolving door related flags"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_23_x26(z91=105400, z92=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_23_12000():
    """Skeleton immortality management_before cave_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4000, z7=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12010():
    """Skeleton immortality management_before cave_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4003, z7=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12020():
    """Skeleton immortality management_before cave_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4010, z7=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12030():
    """Skeleton immortality management_before cave_4"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4012, z7=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12040():
    """Skeleton immortality management_before cave_5"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4013, z7=4020)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12500():
    """Skeleton immortality management_back of cave_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4050, z7=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12510():
    """Skeleton immortality management_back of cave_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4053, z7=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12520():
    """Skeleton immortal management_back of cave_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4054, z7=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_12530():
    """Skeleton immortal management_back of cave_4"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=4055, z7=4060)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13000():
    """Skeleton immortality management_before prison_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6000, z7=6031)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13010():
    """Skeleton immortality management_before prison_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6001, z7=6031)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13020():
    """Skeleton immortality management_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6002, z7=6031)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13500():
    """Skeleton immortality management_back of prison_1"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6003, z7=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13510():
    """Skeleton immortality management_back of prison_2"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6004, z7=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13520():
    """Skeleton immortal management_back of prison_3"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6005, z7=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_13530():
    """Skeleton immortality management_back of prison_4"""
    """State 0,3: [Preset] Skeleton immortality management_SubState"""
    call = event_m10_23_x135(z6=6006, z7=6030)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_23_15000():
    """Torture lift_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_Relief_SubState"""
    assert event_m10_23_x52(z63=10231700, z64=30, z65=123000050, z66=32)
    """State 3: [Lib] [Preset] Elevator_Initialization_Relief_2_SubState"""
    assert event_m10_23_x52(z63=10231701, z64=31, z65=123000051, z66=33)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_15010():
    """Torture lift"""
    """State 0,2: [Lib] [Preset] Torture lift_operation_SubState"""
    assert (event_m10_23_x8(z110=15000, z111=10231700, z112=10231701, z113=30, z114=1501015, z115=1501010,
            z116=1501005, z117=1501000))
    """State 1: Rerun notification"""
    RestartMachine()

def event_m10_23_15020():
    """Torture lift_character action judgment"""
    """State 0,2: [Lib] [Preset] Torture lift_Action judgment_SubState"""
    assert (event_m10_23_x12(z104=10231700, z105=10231701, z106=1501015, z107=1501010, z108=1501005,
            z109=1501000))
    """State 1: Rerun notification"""
    RestartMachine()

def event_m10_23_18000():
    """Hidden door ② on lift_Navimesh change"""
    """State 0,2: [Preset] Hidden Door 2_Invisible Key Guide_SubState"""
    assert event_m10_23_x87(z30=1800000)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_19000():
    """Hidden door ② under lift_Navimesh change"""
    """State 0,2: [Preset] Hidden Door 2_Invisible Key Guide_SubState"""
    assert event_m10_23_x87(z30=1900000)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_20000():
    """Hunting Forest-Tame Valley Operation Bridge"""
    """State 0,3: [Preset] Hunting Forest-Tame Valley Operation Bridge_SubState"""
    call = event_m10_23_x121(z15=10231460, z16=10231450, z17=2000001, z18=2000002)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()

def event_m10_23_21000():
    """Hunting forest MAP discard flag switching"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_23_x26(z91=105440, z92=0)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_23_70000():
    """Duel request_1"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62110000:Token of Spite
    assert event_m10_23_x45(z67=3, z68=10239000, z69=10239001, z70=10231760, z71=40, val6=3, goods1=62110000)
    """State 1: State"""
    EndMachine()

def event_m10_23_70010():
    """Duel Request_2"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62110000:Token of Spite
    assert event_m10_23_x45(z67=4, z68=10239000, z69=10239001, z70=10231761, z71=40, val6=3, goods1=62110000)
    """State 1: State"""
    EndMachine()

def event_m10_23_70020():
    """Duel Request_3"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62110000:Token of Spite
    assert event_m10_23_x45(z67=5, z68=10239000, z69=10239001, z70=10231762, z71=40, val6=3, goods1=62110000)
    """State 1: State"""
    EndMachine()

def event_m10_23_80000():
    """Reproduction fire 01_Starting point"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z78=1023000, z79=1023099)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_81000():
    """Regenerative fire 02_under pillar of suspension bridge"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z78=1023100, z79=1023199)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_82000():
    """Regenerative fireworks 03_within the key door torch"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z78=1023200, z79=1023299)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_83000():
    """After the boss 04"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_23_x41(z78=1023300, z79=1023399)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_x0(z129=_, z130=_, z131=_, z132=_):
    """[Lib] NPC: Grave Placement: General purpose
    z129: Death map: Global event flag
    z130: Tomb: OBJ instance ID
    z131: Tomb move to: Generator ID
    z132: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z129, 1)
    IsGraveGeneratable(8, z132, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z130, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z130, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_23_x1(z126=_, z127=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z126: Global: death flag
    z127: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z127, 10, 0)
    CompareObjState(1, z127, 20, 0)
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
    IsObjSearched(0, z127)
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

def event_m10_23_x2(z124=_, z125=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z124: Area other flags: Ghost appearance
    z125: Area other flags: Conversation start
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
    SetEventFlag(z124, 1)
    CompareEventFlag(0, z124, 1)
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
    SetEventFlag(z125, 1)
    CompareEventFlag(0, z125, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_23_x3(z124=_, z125=_, z126=_, z127=_, z128=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z124: Ghost Appearance: Area Other Flag
    z125: Conversation start: Area and other flags
    z126: Death: Global event flag
    z127: Tomb: OBJ instance ID
    z128: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z128, 1, 0)
    CompareEventFlag(9, z124, 1)
    CompareObjState(9, z127, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z125, 1)
        CompareEventFlag(0, z125, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_23_x1(z126=z126, z127=z127, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_23_x2(z124=z124, z125=z125, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_23_x4(z120=1005, z121=1105, z122=50970000, z123=123000020):
    """[Lib] Item specified door unlocking_2
    z120: Text ID when opened
    z121: Text ID when not opened
    z122: item
    z123: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z122, z120, z121, z123, 0)
    """State 2: End state"""
    return 0

def event_m10_23_x5(z118=55, z119=104151):
    """[Lib] NPC: Death determination: General purpose
    z118: Generator ID
    z119: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z119, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z118)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z119, 1)
            CompareEventFlag(0, z119, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_23_x6():
    """[Lib] [Reproduction] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x7():
    """[Lib] [Condition] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x8(z110=15000, z111=10231700, z112=10231701, z113=30, z114=1501015, z115=1501010, z116=1501005,
                    z117=1501000):
    """[Lib] [Preset] Torture lift
    z110: Initialization event ID
    z111: Reference lift_object instance ID
    z112: Mirror lift_object instance ID
    z113: Safety time
    z114: Reference lift point_on
    z115: Reference lift point_below
    z116: Mirror lift point_on
    z117: Mirror lift point_bottom
    """
    """State 0,2: [Reproduction] Torture lift_operation_SubState"""
    assert event_m10_23_x9(z110=z110)
    """State 3: [Condition] Torture lift_operation_SubState"""
    call = event_m10_23_x10(z111=z111, z112=z112, z114=z114, z115=z115, z116=z116, z117=z117)
    if call.Get() == 0:
        """State 4: [Execution] Torture lift_operation_SubState"""
        assert event_m10_23_x11(z111=z111, z112=z112, z113=z113, z117=z117, z114=z114)
    elif call.Get() == 1:
        """State 5: [Execution] Torture lift_operation_2_SubState"""
        assert event_m10_23_x11(z111=z112, z112=z111, z113=z113, z117=z117, z114=z114)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_23_x9(z110=15000):
    """[Lib] [Reproduction] Torture lift_operation
    z110: Initialization event ID
    """
    """State 0,2: [Compatible with SEQ17677] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 1: Whether the event has ended"""
    assert EventEnded(z110) != 0
    """State 3: End state"""
    return 0

def event_m10_23_x10(z111=10231700, z112=10231701, z114=1501015, z115=1501010, z116=1501005, z117=1501000):
    """[Lib] [Condition] Torture lift _operation
    z111: Reference lift_object instance ID
    z112: Mirror lift_object instance ID
    z114: Reference lift point_on
    z115: Reference lift point_below
    z116: Mirror lift point_on
    z117: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z111, 32, 0)
    IsPlayerInsidePoint(8, z114, z114, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z111, 33, 0)
    IsPlayerInsidePoint(9, z115, z115, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(1, 9)
    CompareObjState(10, z112, 32, 0)
    IsPlayerInsidePoint(10, z116, z116, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z112, 33, 0)
    IsPlayerInsidePoint(11, z117, z117, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(0, 11)
    if ConditionGroup(0):
        """State 2: Standard is from top to bottom"""
        return 0
    elif ConditionGroup(1):
        """State 3: Mirror from top to bottom"""
        return 1

def event_m10_23_x11(z111=_, z112=_, z113=30, z117=1501000, z114=1501015):
    """[Lib] [execution] torture lift
    z111: Top lift_object instance ID
    z112: Lower lift_object instance ID
    z113: Safety time
    z117: Point start
    z114: End of point
    """
    """State 0,1: Execution"""
    ChangeObjState(z111, 70)
    ChangeObjState(z112, 71)
    """State 2: Waiting for next start"""
    CompareObjState(8, z112, 32, 0)
    CompareObjState(8, z111, 33, 0)
    IsPlayerInsidePoint(8, z117, z114, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    CompareStateTime(1, z113, 3, z113)
    SetConditionGroup(1, 8)
    assert HostConditionGroup(1)
    """State 3: End state"""
    return 0

def event_m10_23_x12(z104=10231700, z105=10231701, z106=1501015, z107=1501010, z108=1501005, z109=1501000):
    """[Lib] [Preset] Torture lift_action judgment
    z104: Reference lift_object instance ID
    z105: Mirror lift_object instance ID
    z106: Reference lift point_on
    z107: Reference lift point_below
    z108: Mirror lift point_on
    z109: Mirror lift point_bottom
    """
    """State 0,1: [Reproduction] Torture lift_action judgment_empty_SubState"""
    assert event_m10_23_x13()
    """State 4: [Condition] Torture lift_Action determination_Start determination_SubState"""
    call = event_m10_23_x14(z104=z104, z105=z105, z106=z106, z107=z107, z108=z108, z109=z109)
    if call.Get() == 1:
        """State 2: [Execution] Torture lift_Action judgment_Action start_SubState"""
        assert event_m10_23_x15(z104=z104)
        """State 7: [Reproduction] Torture lift_action judgment_empty_2_SubState"""
        assert event_m10_23_x13()
        """State 5: [Condition] Torture lift_Action judgment_End judgment_SubState"""
        assert event_m10_23_x16(z104=z104, z106=z106, z107=z107)
        """State 3: [Execution] Torture lift_Action judgment_Action end_SubState"""
        assert event_m10_23_x17(z104=z104, z106=z106, z107=z107)
    elif call.Get() == 0:
        """State 6: [Execution] Torture Lift_Action Judgment_Action Start_2_SubState"""
        assert event_m10_23_x15(z104=z105)
        """State 8: [Reproduction] Torture lift_Action judgment_Empty_3_SubState"""
        assert event_m10_23_x13()
        """State 10: [Condition] Torture lift_Action judgment_End judgment_2_SubState"""
        assert event_m10_23_x16(z104=z105, z106=z108, z107=z109)
        """State 9: [Execution] Torture lift_Action judgment_Action end_2_SubState"""
        assert event_m10_23_x17(z104=z105, z106=z108, z107=z109)
    """State 11: End state"""
    return 0

def event_m10_23_x13():
    """[Lib] [reproduction] Torture lift_action judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x14(z104=10231700, z105=10231701, z106=1501015, z107=1501010, z108=1501005, z109=1501000):
    """[Lib] [Condition] Torture lift_Action judgment_Start judgment
    z104: Reference lift_object instance ID
    z105: Mirror lift_object instance ID
    z106: Reference lift point_on
    z107: Reference lift point_below
    z108: Mirror lift point_on
    z109: Mirror lift point_bottom
    """
    """State 0,1: Wait"""
    CompareObjState(8, z104, 70, 0)
    IsPlayerInsidePoint(8, z106, z106, 1)
    DoesPlayerEventAction(8, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z104, 71, 0)
    IsPlayerInsidePoint(9, z107, z107, 1)
    DoesPlayerEventAction(9, 1)
    SetConditionGroup(0, 9)
    CompareObjState(10, z105, 70, 0)
    IsPlayerInsidePoint(10, z108, z108, 1)
    DoesPlayerEventAction(10, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z105, 71, 0)
    IsPlayerInsidePoint(11, z109, z109, 1)
    DoesPlayerEventAction(11, 1)
    SetConditionGroup(1, 11)
    if ConditionGroup(0):
        """State 3: Standard"""
        return 1
    elif ConditionGroup(1):
        """State 2: mirror"""
        return 0

def event_m10_23_x15(z104=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action start
    z104: Lift_object instance ID
    """
    """State 0,1: Action request"""
    ObjAnimationPlayerControlRequest(z104, 34, 10)
    """State 2: End state"""
    return 0

def event_m10_23_x16(z104=_, z106=_, z107=_):
    """[Lib] [Condition] Torture lift_Action judgment_End judgment
    z104: Lift_object instance ID
    z106: Lift point_on
    z107: Lift point_down
    """
    """State 0,1: Wait"""
    CompareObjState(8, z104, 32, 0)
    CompareObjState(9, z104, 33, 0)
    SetConditionGroup(0, 8)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Finish"""
    return 0

def event_m10_23_x17(z104=_, z106=_, z107=_):
    """[Lib] [Execution] Torture lift_Action judgment_Action end
    z104: Lift_object instance ID
    z106: Lift point_on
    z107: Lift point_down
    """
    """State 0,1: Action request"""
    EndPlayerActionRequest()
    """State 2: Wait"""
    IsPlayerInsidePoint(0, z106, z106, 1)
    IsPlayerInsidePoint(0, z107, z107, 1)
    """State 3: End state"""
    return 0

def event_m10_23_x18(z99=_, z100=20, z101=_, z102=0, z103=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z99: Object instance ID
    z100: OBJ state ID
    z101: Navimesh switching point ID
    z102: Additional attributes
    z103: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_23_x19(z99=z99, z100=z100, z101=z101, z103=z103, z102=z102)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_23_x20(z99=z99, z100=z100, z101=z101)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_23_x21(z99=z99, z100=z100, z101=z101, z102=z102, z103=z103)
    """State 4: End state"""
    return 0

def event_m10_23_x19(z99=_, z100=20, z101=_, z103=2, z102=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z99: Target OBJ instance ID
    z100: Target OBJ state ID
    z101: Navimesh switching point ID
    z103: Additional attributes
    z102: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z99, z100, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z101, z103)
        DeleteNavimeshAttribute(z101, z102)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_23_x20(z99=_, z100=20, z101=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z99: Target OBJ instance ID
    z100: Target OBJ state ID
    z101: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z99, z100, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x21(z99=_, z100=20, z101=_, z102=0, z103=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z99: Target OBJ instance ID
    z100: Target OBJ state ID
    z101: Navimesh switching point ID
    z102: Additional attributes
    z103: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z101, z102)
    DeleteNavimeshAttribute(z101, z103)
    """State 2: End state"""
    return 0

def event_m10_23_x22(z93=102405, z94=587, z95=104150, z96=60, z97=103650, z98=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z93: White Phantom can appear: Global event flag
    z94: White Phantom: Generator ID
    z95: Death: Global event flag
    z96: Body: Generator group ID
    z97: Hostile: Global event flag
    z98: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z94)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z95, 1)
        CompareEventFlag(1, z97, 1)
        CompareEventFlag(2, z93, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z94)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z95, 1)
            CompareEventFlag(1, z97, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z94)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z95, 1)
            CompareEventFlag(1, z97, 1)
            HasNpcPhantomSpawned(2, z94, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z96, 0)
                HasNpcPhantomSpawned(0, z94, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z94)
    """State 4: Appearance: System: End"""
    EndMachine()

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

def event_m10_23_x25(z91=_, z92=_):
    """[Lib] [Execution] Switch to connection flag when in map
    z91: Global event flag for connection
    z92: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z91, z92)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z91, z92)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_23_x26(z91=_, z92=_):
    """[Lib] [Preset] Switch the connection flag when in the map
    z91: Global event flag for connection
    z92: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_23_x23()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_23_x24()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_23_x25(z91=z91, z92=z92)
    """State 4: End state"""
    return 0

def event_m10_23_x27():
    """[Lib] [Reproduction] Falling Tree"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x28(z89=10231200):
    """[Lib] [Condition] Falling tree
    z89: OBJ instance ID of the tree
    """
    """State 0,1: Wait for tree to fall"""
    CompareObjState(0, z89, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x29(z90=120010):
    """[Lib] [execution] fallen tree
    z90: Navigation change point ID
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z90, 2)
    """State 2: End state"""
    return 0

def event_m10_23_x30(z89=10231200, z90=120010):
    """[Lib] [Preset] Falling Tree
    z89: OBJ instance ID of the tree
    z90: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Falling tree _SubState"""
    assert event_m10_23_x27()
    """State 3: [Lib] [Condition] Falling tree _SubState"""
    assert event_m10_23_x28(z89=z89)
    """State 2: [Lib] [Execution] Falling tree _SubState"""
    assert event_m10_23_x29(z90=z90)
    """State 4: End state"""
    return 0

def event_m10_23_x31(z88=586):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z88: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z88)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_23_x32(z80=10231800, z81=10231801, z82=10231802, z83=10231803, z84=10231804, z85=10231805,
                     z86=10, z87=17):
    """[Lib] [Asynchronous] [Preset] Duel start
    z80: Door instance IDA
    z81: Door instance IDB
    z82: Door instance IDC
    z83: Door instance IDD
    z84: Door instance IDE
    z85: Door instance IDF
    z86: Event sound ID
    z87: Production FE type
    """
    """State 0,1: [Lib] [Reproduction] Dummy_SubState"""
    assert event_m10_23_x6()
    """State 2: [Lib] [Condition] Dummy_SubState"""
    assert event_m10_23_x7()
    """State 3: [Lib] [Execution] Duel Start_SubState"""
    assert event_m10_23_x33(z80=z80, z81=z81, z82=z82, z83=z83, z84=z84, z85=z85, z86=z86, z87=z87)
    """State 4: End state"""
    return 0

def event_m10_23_x33(z80=10231800, z81=10231801, z82=10231802, z83=10231803, z84=10231804, z85=10231805,
                     z86=10, z87=17):
    """[Private] [Asynchronous] [Execution] Start of duel
    z80: Door instance IDA
    z81: Door instance IDB
    z82: Door instance IDC
    z83: Door instance IDD
    z84: Door instance IDE
    z85: Door instance IDF
    z86: Event sound ID
    z87: Production FE type
    """
    """State 0,1: Jingle sound playback"""
    PlaySoundAtPoint(z86)
    """State 4: Preparation time"""
    assert (GetStateTime() > 5) != 0
    """State 2: Start: open the door"""
    ChangeObjState(z80, 70)
    ChangeObjState(z81, 70)
    ChangeObjState(z82, 70)
    ChangeObjState(z83, 70)
    ChangeObjState(z84, 70)
    ChangeObjState(z85, 70)
    """State 3: Production FE display"""
    OpenPresentationWindow(z87)
    """State 5: End state"""
    return 0

def event_m10_23_x34(z67=_):
    """[Private] [Asynchronous] [Execution] Duel Request_Start
    z67: Duel type
    """
    """State 0,1: Motion start"""
    PlayerActionRequest(14)
    ProhibitInGameMenu(1)
    """State 2: Matching start"""
    StartDuelMatch(z67)
    """State 3: End state"""
    return 0

def event_m10_23_x35(z70=_, z71=40):
    """[Private] [Asynchronous] [Condition] Duel request_wait
    z70: Object instance ID
    z71: Hit group
    """
    """State 0,2: A little wait"""
    assert (GetStateTime() >= 0) != 0
    """State 1: Wait to examine"""
    IsObjSearched(0, z70)
    IsDuelStartPossible(0, 0)
    IsPlayerDamaged(0)
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(0, z71, 0, 0, 2)
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

def event_m10_23_x37(z71=40, z69=10239001):
    """[Private] [Asynchronous] [Reproduction] Duel request_wait
    z71: Hit group
    z69: Key guide parameters
    """
    """State 0,1: Key guide creation"""
    CreateKeyGuideArea(34, z69)
    """State 2: Finish"""
    return 0

def event_m10_23_x38():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x39(z78=_, z79=_):
    """[Lib] [execute] Rebirth fire
    z78: Flag start ID
    z79: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z78, z79, 0)
    """State 2: End state"""
    return 0

def event_m10_23_x40():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x41(z78=_, z79=_):
    """[Lib] [Preset] Rebirth
    z78: Flag start ID
    z79: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_23_x38()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_23_x40()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_23_x39(z78=z78, z79=z79)
    """State 4: End state"""
    return 0

def event_m10_23_x42(z74=12000000, z75=580, z76=0, z77=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z74: Summon range
    z75: Generator ID
    z76: Appearance: Minimum time
    z77: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z74, z74, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z76, 3, z77)
        IsPlayerInsidePoint(1, z74, z74, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z75)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_23_x43(z72=123020127, z73=20):
    """[Lib] [Preset] Get trophy
    z72: Acquisition trigger_other flags
    z73: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z72) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z72, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z73)
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

def event_m10_23_x45(z67=_, z68=10239000, z69=10239001, z70=_, z71=40, val6=3, goods1=62110000):
    """[Lib] [Asynchronous] [Preset] Duel Request
    z67: Duel type
    z68: Start key guide parameter
    z69: Cancel key guide parameter
    z70: Object instance ID
    z71: Hit group
    val6: Pledge
    goods1: item
    """
    """State 0,8: [Private] [Asynchronous] [Reproduction] Duel Request_Start_Training_SubState"""
    call = event_m10_23_x47(z71=z71, z68=z68, val6=val6)
    if call.Get() == 1:
        """State 10: [Private] [Asynchronous] [Condition] Duel request_Start_Key guide wait_Training_SubState"""
        call = event_m10_23_x46(z70=z70, z71=z71, val6=val6, goods1=goods1)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 3: [Private] [Asynchronous] [Execution] Duel Request_Start_SubState"""
            assert event_m10_23_x34(z67=z67)
            """State 4: [Private] [Asynchronous] [Reproduction] Duel Request_Standby_SubState"""
            assert event_m10_23_x37(z71=z71, z69=z69)
            """State 5: [Private] [Asynchronous] [Condition] Duel Request_Standby_SubState"""
            call = event_m10_23_x35(z70=z70, z71=z71)
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
        assert event_m10_23_x48(z71=z71, val6=val6)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_23_x46(z70=_, z71=40, val6=3, goods1=62110000):
    """[Private] [Asynchronous] [Condition] Duel request_Start_Key guide wait
    z70: Object instance ID
    z71: Hit group
    val6: Pledge
    goods1: item
    """
    """State 0,1: Wait to examine"""
    IsObjSearched(0, z70)
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(1, z71, 0, 0, 2)
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

def event_m10_23_x47(z71=40, z68=10239000, val6=3):
    """[Private] [Asynchronous] [Reproduction] Duel Request_Start
    z71: Hit group
    z68: Key guide parameters
    val6: Pledge
    """
    """State 0,1: Branch"""
    if (CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(z71, 0, 1) != 1 and (GetPlayerCovenant()
        == val6) != 0 and IsOffline() != 1):
        """State 2: Key guide creation"""
        CreateKeyGuideArea(34, z68)
        """State 5: There are no enemies around"""
        return 1
    else:
        """State 3: Delete key guide"""
        DeleteKeyGuideArea()
        """State 4: There are enemies around"""
        return 0

def event_m10_23_x48(z71=40, val6=3):
    """[Private] [Asynchronous] [Condition] Duel request_Start_Key guide invalidation waiting
    z71: Hit group
    val6: Pledge
    """
    """State 0,1: Wait"""
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(8, z71, 0, 0, 5)
    IsPlayerInCovenant(8, val6, 1)
    IsOffline(8, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_23_x49(z65=_, z63=_, z64=_, z66=_):
    """[Lib] [Reproduction] Elevator_Initialization_Relief
    z65: Initialization completion flag
    z63: Elevator OBJ instance ID
    z64: Initial position OBJ state ID
    z66: OBJ state after initialization
    """
    """State 0,4: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 1: Already initialized?"""
    if GetEventFlag(z65) != 0:
        pass
    else:
        Goto('L0')
    """State 2: [Remedy] Is it in the initial state?"""
    if CompareObjStateId(z63, 10, 0):
        """State 3: Elevator initialization"""
        ChangeObjState(z63, z64)
        assert CompareObjStateId(z63, z66, 0)
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

def event_m10_23_x51(z63=_, z64=_, z65=_, z66=_):
    """[Lib] [Run] Elevator_Initialization_Relief
    z63: Elevator OBJ instance ID
    z64: Initial position OBJ state ID
    z65: Initialization completion flag
    z66: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z63, z64)
    assert CompareObjStateId(z63, z66, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z65, 1)
    """State 3: End state"""
    return 0

def event_m10_23_x52(z63=_, z64=_, z65=_, z66=_):
    """[Lib] [Preset] Elevator_Initialization_Relief
    z63: Elevator OBJ instance ID
    z64: Initial position OBJ state ID
    z65: Initialization completion flag
    z66: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_Relief_SubState"""
    call = event_m10_23_x49(z65=z65, z63=z63, z64=z64, z66=z66)
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
        assert event_m10_23_x51(z63=z63, z64=z64, z65=z65, z66=z66)
    """State 4: End state"""
    return 0

def event_m10_23_x53(z60=123000042):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z60: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z60) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_23_x54(z61=944, mode1=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z61: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z61)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_23_x55(z60=123000042, z62=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z60: Defeat flag
    z62: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z60, 1)
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
                    SetEventFlag(z62, 1)
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

def event_m10_23_x56(z60=123000042, z61=944, mode1=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z60: Defeat flag
    z61: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_23_x53(z60=z60)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_23_x54(z61=z61, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_23_x55(z60=z60, z62=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_23_x55(z60=z60, z62=102755)
    """State 5: End state"""
    return 0

def event_m10_23_x57(z58=9500, z59=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z58: Generator ID
    z59: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z58, z59)
    """State 2: End state"""
    return 0

def event_m10_23_x58(z58=9500, z59=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z58: Generator ID
    z59: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z58, z59, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_23_x59(z58=9500):
    """[Lib] [DC] [Condition] Transparent characters
    z58: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z58)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x60(z58=9500, z59=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z58: Generator ID
    z59: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_23_x58(z58=z58, z59=z59)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_23_x59(z58=z58)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_23_x57(z58=z58, z59=z59)
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

def event_m10_23_x62(z56=944, z57=123020043):
    """[Lib] [execution] wanderer_fixed appearance
    z56: Generator ID
    z57: Startup flag
    """
    """State 0,1: Wanderer: Generate Start flag ON"""
    GenerateNpcPhantom(z56)
    SetEventFlag(z57, 1)
    """State 2: Finish"""
    return 0

def event_m10_23_x63(z52=6000000, z53=6000000, z54=0, z55=2):
    """[Lib] [Condition] Wanderer_Fixed Appearance
    z52: Judgment start point ID
    z53: Judgment end point ID
    z54: Minimum appearance time
    z55: Maximum time to appear
    """
    """State 0,1: Appearance determination"""
    IsPlayerInsidePoint(0, z53, z53, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z54, 3, z55)
    assert ConditionGroup(0)
    """State 3: Appearance"""
    return 0

def event_m10_23_x64(z52=6000000, z53=6000000, z54=0, z55=2, z56=944, z57=123020043):
    """[Lib] [Preset] Wanderer_Fixed Appearance
    z52: Judgment start point ID
    z53: Judgment end point ID
    z54: Minimum appearance time
    z55: Maximum time to appear
    z56: Generator ID
    z57: Startup flag
    """
    """State 0,1: [Lib] [Reproduction] Wanderer_Fixed Appearance_SubState"""
    assert event_m10_23_x61()
    """State 3: [Lib] [Condition] Wanderer_Fixed Appearance_SubState"""
    assert event_m10_23_x63(z52=z52, z53=z53, z54=z54, z55=z55)
    """State 2: [Lib] [execution] wanderer_fixed appearance_SubState"""
    assert event_m10_23_x62(z56=z56, z57=z57)
    """State 4: Finish"""
    return 0

def event_m10_23_x65(z49=123000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z49: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z49) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_23_x66(z50=816):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z50: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z50, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x67(z51=123020084):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z51: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z51, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x68(z49=123000081, z50=816, z51=123020084):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z49: Boss destruction flag
    z50: Boss generator ID
    z51: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_23_x65(z49=z49)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_23_x66(z50=z50)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_23_x67(z51=z51)
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

def event_m10_23_x71(z48=302000):
    """[Execution] Destroy iron grid and carriage
    z48: Navigation change point ID
    """
    """State 0,6: Destroyed bar"""
    ChangeOwnObjState(72)
    """State 8: Disabling the key guide of the lever"""
    DisableObjKeyGuide(10234910, 1)
    """State 7: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z48, 2)
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

def event_m10_23_x72(z47=302000):
    """[Execution] Raise the iron grid
    z47: Navigation change point ID
    """
    """State 0,1: Raise the bar"""
    ChangeOwnObjState(71)
    assert CompareOwnObjStateId(10, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z47, 2)
    """State 3: End state"""
    return 0

def event_m10_23_x73(z46=302000):
    """[Execution] Lower the iron grid
    z46: Navigation change point ID
    """
    """State 0,1: Unload the bar"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(30, 0)
    """State 2: Navimesh attribute added"""
    AddNavimeshAttribute(z46, 2)
    """State 3: End state"""
    return 0

def event_m10_23_x74(z44=_, z45=_):
    """[Reproduction] When you break a wooden board, it becomes brighter
    z44: Wood board OBJ instance ID
    z45: Event light ID
    """
    """State 0,1: Is the wood board broken?"""
    if CompareOwnObjStateId(20, 0):
        """State 3: Is broken"""
        return 0
    else:
        """State 2: Small light OFF"""
        SetPointLightEnabled(z45, 0, 0)
        """State 4: Not broken"""
        return 1

def event_m10_23_x75(z44=_):
    """[Condition] Wood board destruction judgment
    z44: Wood board OBJ instance ID
    """
    """State 0,1: Wood board destruction waiting"""
    IsObjBroken(0, z44, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x76(z45=_):
    """[Execution] Small light on
    z45: Event light ID
    """
    """State 0,1: Small light on"""
    SetPointLightEnabled(z45, 1, 0.5)
    """State 2: End state"""
    return 0

def event_m10_23_x77(z44=_, z45=_):
    """[Preset] Brighten up by breaking the wooden board
    z44: Wood board OBJ instance ID
    z45: Event light ID
    """
    """State 0,1: [Reproduction] _SubState brightens when breaking a wooden board"""
    call = event_m10_23_x74(z44=z44, z45=z45)
    if call.Get() == 1:
        """State 2: [Condition] Wood board destruction judgment_SubState"""
        assert event_m10_23_x75(z44=z44)
    elif call.Get() == 0:
        pass
    """State 3: [Execution] Small light ON_SubState"""
    assert event_m10_23_x76(z45=z45)
    """State 4: End state"""
    return 0

def event_m10_23_x78(z40=10231410, z41=10231400, z42=10230030, z43=2):
    """[Reproduction] Large light judgment
    z40: OBJ instance ID of the wooden board on the entrance side
    z41: Door side wooden board OBJ instance ID
    z42: Large event light ID
    z43: Hit group ID
    """
    """State 0,1: Are the two wooden boards broken?"""
    if CompareObjStateId(z40, 20, 0) and CompareObjStateId(z41, 20, 0):
        """State 5: 2 wooden boards destroyed"""
        return 1
    else:
        """State 2: Event light large OFF"""
        SetPointLightEnabled(z42, 0, 0)
        """State 3: Brightness switch"""
        ChangeHitBrightnessSetting(z43, 0)
        """State 4: Not destroyed"""
        return 0

def event_m10_23_x79(z38=10231410, z39=10231400):
    """[Condition] Large light judgment
    z38: OBJ instance ID of the wooden board on the entrance side
    z39: Door side wooden board OBJ instance ID
    """
    """State 0,1: Wait for destruction of two wooden boards"""
    IsObjBroken(8, z38, 1)
    IsObjBroken(8, z39, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_23_x80(z36=10230030, z37=2):
    """[Execution] Large light determination
    z36: Large event light ID
    z37: Hit group ID
    """
    """State 0,1: Event Light University ON"""
    SetPointLightEnabled(z36, 1, 0.5)
    """State 2: Brightness switch"""
    ChangeHitBrightnessSetting(z37, 1)
    """State 3: End state"""
    return 0

def event_m10_23_x81():
    """[Reproduction] Working bridge"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x82(z35=10231510):
    """[Conditions] Working bridge
    z35: Lever OBJ instance ID
    """
    """State 0,1: [Preset] _SubState brightens when breaking a wooden board"""
    CompareObjState(0, z35, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x83(z33=500000, z34=123000032):
    """[Execution] Operation Bridge
    z33: Navigation change point ID
    z34: Enemy activation flag
    """
    """State 0,1: Working bridge animation playback"""
    ChangeOwnObjState(70)
    """State 3: Enemy activation flag ON"""
    SetEventFlag(z34, 1)
    assert CompareOwnObjStateId(20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z33, 2)
    """State 4: End state"""
    return 0

def event_m10_23_x84():
    """[Reproduction] Shortcut iron grid"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x85(z32=10231610):
    """[Conditions] Shortcut iron grid
    z32: Wall lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z32, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x86(z31=600000):
    """[Execution] Shortcut iron grid
    z31: Navigation change point ID
    """
    """State 0,1: Iron lattice animation playback"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z31, 2)
    """State 3: End state"""
    return 0

def event_m10_23_x87(z30=_):
    """[Preset] Hidden door 2_ Invisible key guide
    z30: Navigation change point ID
    """
    """State 0,1: [Reproduction] Hidden door 2_SubState"""
    assert event_m10_23_x88()
    """State 3: [Condition] Hidden door 2_SubState"""
    assert event_m10_23_x89()
    """State 2: [Execution] Hidden door 2_SubState"""
    assert event_m10_23_x90(z30=z30)
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

def event_m10_23_x90(z30=_):
    """[Execution] Hidden door 2
    z30: Navigation change point ID
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z30, 2)
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

def event_m10_23_x104(z3=_):
    """[Condition] Create another enemy by destroying the enemy
    z3: Death enemy ID
    """
    """State 0,1: Enemy death waiting"""
    IsChrDead(0, z3)
    assert ConditionGroup(0)
    """State 2: Time lapse state"""
    assert (GetStateTime() > 6) != 0
    """State 3: End state"""
    return 0

def event_m10_23_x105(val1=_, val2=_, val3=_, val4=_, val5=_, z27=_, z28=_, z29=_):
    """[Execution] Create another enemy by destroying the enemy
    val1: Operation generator ID_1
    val2: Operation generator ID_2
    val3: Operation generator ID_3
    val4: Operation generator ID_4
    val5: Operation generator ID_5
    z27: Death enemy ID
    z28: Generation point start ID
    z29: Generation point end ID
    """
    """State 0,6: Does the generator exist?"""
    if (not val1) != 0:
        pass
    else:
        """State 11: Time lapse state_2"""
        assert (GetStateTime() > 0.3) != 0
        """State 1: Generator operation"""
        ForceGenerationFromPointBasedOnPosition(val1, z27, z28, z29, 1, 0)
    """State 7: Does the generator exist? _2"""
    if (not val2) != 0:
        pass
    else:
        """State 12: Elapsed state_3"""
        assert (GetStateTime() > 1.2) != 0
        """State 2: Generator operation_2"""
        ForceGenerationFromPointBasedOnPosition(val2, z27, z28, z29, 2, 0)
    """State 8: Does the generator exist? _3"""
    if (not val3) != 0:
        pass
    else:
        """State 13: Time elapsed state_4"""
        assert (GetStateTime() > 2) != 0
        """State 3: Generator operation_3"""
        ForceGenerationFromPointBasedOnPosition(val3, z27, z28, z29, 3, 0)
    """State 9: Does the generator exist? _Four"""
    if (not val4) != 0:
        pass
    else:
        """State 14: Elapsed state_5"""
        assert (GetStateTime() > 0.8) != 0
        """State 4: Generator operation_4"""
        ForceGenerationFromPointBasedOnPosition(val4, z27, z28, z29, 4, 0)
    """State 10: Does the generator exist? _Five"""
    if (not val5) != 0:
        pass
    else:
        """State 15: Time elapsed state_6"""
        assert (GetStateTime() > 1.7) != 0
        """State 5: Generator operation_5"""
        ForceGenerationFromPointBasedOnPosition(val5, z27, z28, z29, 5, 0)
    """State 16: End state"""
    return 0

def event_m10_23_x106(z27=_, val1=_, val2=_, val3=_, val4=_, val5=_, z28=_, z29=_):
    """[Preset] Create another enemy by destroying the enemy
    z27: Death enemy ID
    val1: Operation generator ID_1
    val2: Operation generator ID_2
    val3: Operation generator ID_3
    val4: Operation generator ID_4
    val5: Operation generator ID_5
    z28: Generation point start ID
    z29: Generation point end ID
    """
    """State 0,1: [Reproduction] Creating another enemy by destroying the enemy_Sky_SubState"""
    assert event_m10_23_x103()
    """State 2: [Condition] Another enemy created by destroying an enemy_SubState"""
    assert event_m10_23_x104(z3=z27)
    """State 3: [Execute] Create another enemy by destroying the enemy_SubState"""
    assert (event_m10_23_x105(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, z27=z27, z28=z28,
            z29=z29))
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

def event_m10_23_x112(z23=_, z24=_, z26=173010):
    """[Conditions] Pile torturer activation
    z23: Intrusion area ID_before
    z24: After intrusion area ID_
    z26: Intrusion area ID_reverse run
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
    IsPlayerInsidePoint(0, z23, z24, 1)
    IsPlayerInsidePoint(1, z26, z26, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Time elapse or point escape standby"""
        IsPlayerInsidePoint(0, z23, z24, 0)
        CompareStateTime(0, 5, 3, 5)
        assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_23_x113(z21=_):
    """[Execution] Pile torturer launch
    z21: Torturer starting flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z21, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x114(z23=_, z24=_, z25=_, z26=173010):
    """[Preset] Pile torturer launch
    z23: Intrusion area ID_before
    z24: After intrusion area ID_
    z25: Torturer starting flag
    z26: Intrusion area ID_reverse run
    """
    """State 0,1: [Reproduction] Pile-top torture person activation _ empty _SubState"""
    assert event_m10_23_x111()
    """State 2: [Conditions] Pile torturer activation_SubState"""
    call = event_m10_23_x112(z23=z23, z24=z24, z26=z26)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Execution] Pile torturer activation_SubState"""
        assert event_m10_23_x113(z21=z25)
    """State 4: End state"""
    return 0

def event_m10_23_x115(z19=171000, z20=171010, z22=173010):
    """[Condition] Pile torturer activation_2
    z19: Intrusion area ID_before
    z20: After intrusion area ID_
    z22: Intrusion area ID_reverse run
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
    IsPlayerInsidePoint(0, z19, z20, 1)
    IsPlayerInsidePoint(1, z22, z22, 1)
    if ConditionGroup(0):
        """State 3: Time elapse or point escape standby"""
        IsPlayerInsidePoint(0, z19, z20, 0)
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

def event_m10_23_x116(z19=171000, z20=171010, z21=123020004, z22=173010):
    """[Preset] Pile torturer activation_2
    z19: Intrusion area ID_before
    z20: After intrusion area ID_
    z21: Torturer starting flag
    z22: Intrusion area ID_reverse run
    """
    """State 0,1: [Reproduction] Pile-top torture person activation _ empty _SubState"""
    assert event_m10_23_x111()
    """State 4: [Conditions] Pile torturer activation_SubState"""
    call = event_m10_23_x115(z19=z19, z20=z20, z22=z22)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 3: [Execution] Pile torturer activation_2_SubState"""
        assert event_m10_23_x117()
    elif call.Done():
        """State 2: [Execution] Pile torturer activation_SubState"""
        assert event_m10_23_x113(z21=z21)
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

def event_m10_23_x118(z15=10231460, z16=10231450):
    """[Reproduction] Hunting Forest-Tame Valley Operation Bridge
    z15: Bridge instance ID
    z16: Lever instance ID
    """
    """State 0,3: Event ends for guests"""
    if IsGuest() != 0:
        """State 6: Simple end"""
        return 1
    else:
        """State 1: OBJ state initialization: working bridge"""
        InitializeObj(z15)
        """State 2: Enable key guide for lever"""
        DisableObjKeyGuide(z16, 0)
        """State 4: Navigation mesh change"""
        AddNavimeshAttribute(2000000, 2)
        """State 5: End state"""
        return 0

def event_m10_23_x119(z16=10231450):
    """[Conditions] Hunting Forest-Tame Valley Operation Bridge
    z16: Lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z16, 74, 0)
    CompareObjState(0, z16, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x120(z15=10231460, z16=10231450, z17=2000001, z18=2000002):
    """[Execution] Hunting Forest-Tame Valley Operation Bridge
    z15: Bridge instance ID
    z16: Lever instance ID
    z17: Point ID for bridge initialization determination_start
    z18: Point ID for bridge initialization determination_end
    """
    """State 0,1: OBJ state transition: Working bridge: 70"""
    ChangeObjState(z15, 70)
    """State 2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z16, 1)
    """State 5: Has the moving bridge animation ended?"""
    CompareObjState(0, z15, 20, 0)
    assert ConditionGroup(0)
    """State 4: Navigation mesh change"""
    DeleteNavimeshAttribute(2000000, 2)
    """State 3: Did you enter the specified point?"""
    IsPlayerInsidePoint(0, z17, z18, 1)
    assert ConditionGroup(0)
    """State 6: OBJ state transition: Working bridge: 71"""
    ChangeObjState(z15, 71)
    """State 7: Has the moving bridge animation ended? _2"""
    CompareObjState(0, z15, 10, 0)
    assert ConditionGroup(0)
    """State 8: End state"""
    return 0

def event_m10_23_x121(z15=10231460, z16=10231450, z17=2000001, z18=2000002):
    """[Preset] Hunting Forest-Tame Valley Operation Bridge
    z15: Bridge instance ID
    z16: Lever instance ID
    z17: Point ID for bridge initialization determination_start
    z18: Point ID for bridge initialization determination_end
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z15, 0)
    """State 2: [Reproduction] Hunting Forest-Tame Valley Operation Bridge_SubState"""
    call = event_m10_23_x118(z15=z15, z16=z16)
    if call.Get() == 1:
        """State 6: End state_2"""
        return 1
    elif call.Done():
        """State 3: [Conditions] Hunting Forest-Tame Valley Operation Bridge_SubState"""
        assert event_m10_23_x119(z16=z16)
        """State 4: [Execution] Hunting Forest-Tame Valley Operation Bridge_SubState"""
        assert event_m10_23_x120(z15=z15, z16=z16, z17=z17, z18=z18)
        """State 5: End state"""
        return 0

def event_m10_23_x122(z12=840, z13=841, z14=123020035):
    """[Preset] Skeleton aristocrat_cane_big explosion
    z12: Enemy generator ID1 for performing death checks
    z13: Enemy generator ID2 for performing death checks
    z14: Skeleton aristocratic explosion flag
    """
    """State 0,1: [Reproduction] Skeleton aristocrat_cane_explosion_SubState"""
    assert event_m10_23_x123()
    """State 2: [Conditions] Skeleton aristocrat_Wand_Large explosion_SubState"""
    assert event_m10_23_x124(z12=z12, z13=z13)
    """State 3: [Execution] Skeleton aristocrat_Cane_Large explosion_SubState"""
    assert event_m10_23_x125(z14=z14)
    """State 4: End state"""
    return 0

def event_m10_23_x123():
    """[Reproduction] Skeleton aristocrat_cane_big explosion"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x124(z12=840, z13=841):
    """[Conditions] Skeleton aristocrat_cane_big explosion
    z12: Enemy generator ID1 for performing death checks
    z13: Enemy generator ID2 for performing death checks
    """
    """State 0,1: Is the skeleton aristocrat sickle or ax moth dead?"""
    IsChrDead(0, z12)
    IsChrDead(0, z13)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_23_x125(z14=123020035):
    """[Execution] Skeleton aristocrat_cane_big explosion
    z14: Skeleton aristocratic explosion flag
    """
    """State 0,1: Action 23 Big explosion flag ON"""
    SetEventFlag(z14, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x126(z8=1023010, z9=123000081, z10=10234900, z11=10234910):
    """[Preset] Chariot's iron grid and lever _ state reproduction
    z8: Boss Battle ID
    z9: Boss destruction flag
    z10: Instance ID of the iron lattice OBJ
    z11: Lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Chariot's iron grid and lever_state reproduction_SubState"""
    call = event_m10_23_x127(z11=z11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Chariot's iron grid and lever_state reproduction_SubState"""
        call = event_m10_23_x128(z8=z8, z9=z9, z10=z10)
        if call.Get() == 1:
            """State 3: [Execution] Chariot's iron grid and lever _ State reproduction _ Initialization _ SubState"""
            assert event_m10_23_x129(z10=z10, z11=z11)
        elif call.Get() == 2:
            """State 4: [Execution] Chariot's iron grid and lever_State reproduction_Key guide disabled_SubState"""
            assert event_m10_23_x130(z11=z11)
        elif call.Get() == 0:
            pass
    """State 5: End state"""
    return 0

def event_m10_23_x127(z11=10234910):
    """[Reproduction] Chariot's iron grid and lever_state reproduction
    z11: Lever OBJ instance ID
    """
    """State 0,1: Are you a guest?"""
    if IsGuest() != 0:
        """State 4: The guests"""
        return 1
    else:
        """State 2: Enable key guide for lever"""
        DisableObjKeyGuide(z11, 0)
        """State 3: host"""
        return 0

def event_m10_23_x128(z8=1023010, z9=123000081, z10=10234900):
    """[Conditions] Chariot's iron grid and lever_state reproduction
    z8: Boss Battle ID
    z9: Boss destruction flag
    z10: Instance ID of the iron lattice OBJ
    """
    """State 0,1: Did you destroy the boss or boss during the boss battle?"""
    IsEventBossBattle(0, z8, 1)
    CompareEventFlag(0, z9, 1)
    if ConditionGroup(0):
        """State 2: Is the iron grid broken?"""
        CompareObjState(0, z10, 20, 0)
        CompareObjState(0, z10, 72, 0)
        if ConditionGroup(0):
            """State 6: Disable key guide"""
            return 2
        else:
            """State 3: Is the barred?"""
            CompareObjState(0, z10, 30, 0)
            CompareObjState(0, z10, 70, 0)
            if ConditionGroup(0):
                pass
            else:
                """State 4: End state"""
                return 0
    else:
        pass
    """State 5: Initialization process"""
    return 1

def event_m10_23_x129(z10=10234900, z11=10234910):
    """[Execution] Chariot's iron grid and lever _ State reproduction _ Initialization
    z10: Instance ID of the iron lattice OBJ
    z11: Lever OBJ instance ID
    """
    """State 0,1: Iron grid and lever initialization"""
    InitializeObj(z10)
    InitializeObj(z11)
    """State 2: End state"""
    return 0

def event_m10_23_x130(z11=10234910):
    """[Execution] Chariot's iron grid and lever _ State reproduction _ Key guide disabled
    z11: Lever OBJ instance ID
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z11, 1)
    """State 2: End state"""
    return 0

def event_m10_23_x131():
    """[Reproduction] Skeleton immortality management_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_23_x132(z7=_, z6=_):
    """[Conditions] Skeleton immortality management
    z7: Dark Wizard generator ID
    z6: Skeleton generator ID
    """
    """State 0,1: Skeleton and dark wizard judgment"""
    IsChrDead(0, z7)
    IsChrMaxRespawnCount(0, z7, 1, 0)
    CompareChrEzStateValue(1, z7, 7, 1, 0)
    IsChrDead(2, z6)
    if ConditionGroup(2):
        """State 4: Skeleton death: do nothing"""
        return 2
    elif ConditionGroup(0):
        """State 2: Upper limit or death: cancel immortality"""
        return 0
    elif ConditionGroup(1):
        """State 3: Resurrection behavior: Resurrection processing"""
        return 1

def event_m10_23_x133(z6=_):
    """[Execution] Skeleton immortality management_release
    z6: Skeleton generator ID
    """
    """State 0,1: Special effect grant: Immortal release"""
    SetEnemySpEffect(z6, 91320030, 19, 4)
    assert (GetStateTime() >= 0) != 0
    """State 2: [DC] Is the skeleton's HP 1 or less?"""
    CompareChrHpValue(0, z6, 1, 5)
    assert ConditionGroup(0)
    """State 3: [DC] Special effects: suicide"""
    SetEnemySpEffect(z6, 91320020, 19, 4)
    """State 4: Finish"""
    return 0

def event_m10_23_x134(z6=_, z7=_):
    """[Execution] Skeleton immortality management_Resurrection
    z6: Skeleton generator ID
    z7: Dark Wizard generator ID
    """
    """State 0,3: Skip if not running"""
    CompareChrStartUpState(0, z6, 0, 0)
    CompareChrStartUpState(1, z6, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: Special effects: Resurrection processing"""
        SetEnemySpEffect(z6, 91320010, 19, 4)
    """State 2: Wait for next decision"""
    CompareChrEzStateValue(0, z7, 7, 0, 0)
    IsChrDead(0, z7)
    IsChrDead(0, z6)
    assert ConditionGroup(0)
    """State 4: Finish"""
    return 0

def event_m10_23_x135(z6=_, z7=_):
    """[Preset] Skeleton immortality management
    z6: Skeleton generator ID
    z7: Dark Wizard generator ID
    """
    """State 0,1: [Reproduction] Skeleton immortality management_sky_SubState"""
    assert event_m10_23_x131()
    """State 4: [Condition] Skeleton immortality management_SubState"""
    call = event_m10_23_x132(z7=z7, z6=z6)
    if call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Skeleton immortality management_Release_SubState"""
        assert event_m10_23_x133(z6=z6)
    elif call.Get() == 1:
        """State 3: [Execution] Skeleton immortality management_Resurrection_SubState"""
        assert event_m10_23_x134(z6=z6, z7=z7)
        """State 6: Rerun"""
        return 1
    """State 5: Finish"""
    return 0

def event_m10_23_x136(z3=841, z4=702000, z5=702049):
    """[DC] [execution] Another enemy generation by destroying enemies _12 body version
    z3: Death enemy ID
    z4: Generation point start ID
    z5: Generation point end ID
    """
    """State 0,6: Elapsed state_1"""
    assert (GetStateTime() > 0.3) != 0
    """State 1: Generator operation"""
    ForceGenerationFromPointBasedOnPosition(5220, z3, z4, z5, 1, 0)
    """State 7: Time lapse state_2"""
    assert (GetStateTime() > 0.6) != 0
    """State 2: Generator operation_2"""
    ForceGenerationFromPointBasedOnPosition(5221, z3, z4, z5, 2, 0)
    """State 8: Elapsed state_3"""
    assert (GetStateTime() > 1) != 0
    """State 3: Generator operation_3"""
    ForceGenerationFromPointBasedOnPosition(5222, z3, z4, z5, 3, 0)
    """State 9: Time elapsed state_4"""
    assert (GetStateTime() > 0.4) != 0
    """State 4: Generator operation_4"""
    ForceGenerationFromPointBasedOnPosition(5223, z3, z4, z5, 4, 0)
    """State 10: Elapsed state_5"""
    assert (GetStateTime() > 0.9) != 0
    """State 5: Generator operation_5"""
    ForceGenerationFromPointBasedOnPosition(5224, z3, z4, z5, 5, 0)
    """State 12: Time elapsed state_6"""
    assert (GetStateTime() > 0.2) != 0
    """State 11: Generator operation_6"""
    ForceGenerationFromPointBasedOnPosition(5225, z3, z4, z5, 6, 0)
    """State 14: Elapsed state_7"""
    assert (GetStateTime() > 0.3) != 0
    """State 13: Generator operation_7"""
    ForceGenerationFromPointBasedOnPosition(5226, z3, z4, z5, 7, 0)
    """State 16: Elapsed state_8"""
    assert (GetStateTime() > 1.2) != 0
    """State 15: Generator operation_8"""
    ForceGenerationFromPointBasedOnPosition(5227, z3, z4, z5, 8, 0)
    """State 18: Elapsed state_9"""
    assert (GetStateTime() > 0.6) != 0
    """State 17: Generator operation_9"""
    ForceGenerationFromPointBasedOnPosition(5228, z3, z4, z5, 9, 0)
    """State 20: Time lapse state_10"""
    assert (GetStateTime() > 0.6) != 0
    """State 19: Generator operation_10"""
    ForceGenerationFromPointBasedOnPosition(5229, z3, z4, z5, 10, 0)
    """State 22: Time elapsed state_11"""
    assert (GetStateTime() > 0.3) != 0
    """State 21: Generator operation_11"""
    ForceGenerationFromPointBasedOnPosition(5230, z3, z4, z5, 11, 0)
    """State 24: [Others] Boss battle started"""
    assert (GetStateTime() > 0.2) != 0
    """State 23: Generator operation_12"""
    ForceGenerationFromPointBasedOnPosition(5231, z3, z4, z5, 12, 0)
    """State 25: End state"""
    return 0

def event_m10_23_x137(z3=841, z4=702000, z5=702049):
    """[DC] [Preset] 12 enemy versions generated by destroying enemies
    z3: Death enemy ID
    z4: Generation point start ID
    z5: Generation point end ID
    """
    """State 0,1: [Reproduction] Creating another enemy by destroying the enemy_Sky_SubState"""
    assert event_m10_23_x103()
    """State 2: [Condition] Another enemy created by destroying an enemy_SubState"""
    assert event_m10_23_x104(z3=z3)
    """State 3: [DC] [Execution] Another enemy generation by destroying an enemy_12 body version_SubState"""
    assert event_m10_23_x136(z3=z3, z4=z4, z5=z5)
    """State 4: End state"""
    return 0

def event_m10_23_x138(z1=123000086, z2=123020087):
    """[DC] [Preset] NPC White Spirit_Gesture Management_Skeleton Nobility
    z1: Boss destruction flag
    z2: Gesture flag
    """
    """State 0,1: [DC] [Reproduction] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
    call = event_m10_23_x139(z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Conditions] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
        assert event_m10_23_x140()
        """State 2: [DC] [Execution] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
        assert event_m10_23_x141(z2=z2)
    """State 4: End state"""
    return 0

def event_m10_23_x139(z1=123000086):
    """[DC] [Reproduction] NPC White Spirit_Gesture Management_Skeleton Nobility
    z1: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z1) != 0:
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

def event_m10_23_x141(z2=123020087):
    """[DC] [Execution] NPC White Spirit_Gesture Management_Skeleton Nobility
    z2: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z2, 1)
    """State 2: End state"""
    return 0

def event_m10_23_111232():
    """NPC: Wandering Warrior: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_23_x0(z129=104151, z130=10234200, z131=56, z132=7420)

def event_m10_23_111233():
    """NPC: Wandering Warrior: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_23_x3(z124=123010110, z125=123020111, z126=104150, z127=10234200, z128=111232, npc1=7420)

def event_m10_23_111234():
    """NPC: Wanderer Warrior: Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_23_x5(z118=55, z119=104151)

def event_m10_23_111422():
    """NPC: Darkness Shop: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_23_x0(z129=104330, z130=10234000, z131=156, z132=7700)

def event_m10_23_111423():
    """NPC: Dark Art Shop: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7700:Felkin the Outcast
    event_m10_23_x3(z124=123010130, z125=123020131, z126=104330, z127=10234000, z128=111422, npc1=7700)

def event_m10_23_111472():
    """NPC: Black Phantom Shop: Grave"""
    """State 0,1: NPC: Black Phantom Shop: Grave Placement_SubState"""
    event_m10_23_x0(z129=104380, z130=10234100, z131=276, z132=7830)

def event_m10_23_111473():
    """NPC: Black Phantom Shop: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7830:Titchy Gren
    event_m10_23_x3(z124=123010120, z125=123020121, z126=104380, z127=10234100, z128=111472, npc1=7830)

def event_m10_23_118100():
    """Multi-use NPC: White Spirit Test 1: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_23_x31(z88=586)

def event_m10_23_118110():
    """Multi-use NPC: Clayton: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_23_x22(z93=102405, z94=587, z95=104150, z96=60, z97=103650, z98=-1)

def event_m10_23_118210():
    """Multi-use NPC: Shinigami (Female): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_23_x42(z74=12000000, z75=580, z76=0, z77=2)

def event_m10_23_120020():
    """Trophy: Pledge for blood"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_23_x43(z72=123020127, z73=20)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_23_4000000():
    """[DC] Wanderer A_ fixed appearance"""
    """State 0,2: [Lib] [Preset] Wanderer_Fixed Appearance_SubState"""
    assert event_m10_23_x64(z52=6000000, z53=6000000, z54=0, z55=2, z56=944, z57=123020043)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_23_x56(z60=123000042, z61=944, mode1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_23_x60(z58=9500, z59=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4031000():
    """[DC] NPC White Spirit_Gesture Management_Silver Chariots"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_23_x68(z49=123000081, z50=816, z51=123020084)
    """State 1: Finish"""
    EndMachine()

def event_m10_23_4031010():
    """[DC] NPC White Spirit_Gesture Management_Skeleton Nobility"""
    """State 0,2: [DC] [Preset] NPC White Spirit_Gesture Management_Skeleton Nobility_SubState"""
    assert event_m10_23_x138(z1=123000086, z2=123020087)
    """State 1: Finish"""
    EndMachine()

