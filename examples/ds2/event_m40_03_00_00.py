# -*- coding: utf-8 -*-
def event_m40_03_1000():
    """Elevator body"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m40_03_x7(z44=40031020, z45=100000, z46=100001, z47=40031010, z48=40031015)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m40_03_1010():
    """On elevator lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m40_03_x12(z52=40031020, z53=40031010, z54=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m40_03_1020():
    """Below the elevator lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m40_03_x12(z52=40031020, z53=40031015, z54=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m40_03_2000():
    """Boss: Agaturan Stand _ Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m40_03_x0(flag3=403000081, z55=200000, z56=200002, z57=101, z58=4003000, z59=403020080,
            mode1=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_2010():
    """Agaturan Wormhole Generation"""
    """State 0,3: [Preset] Wormhole generation_SubState"""
    call = event_m40_03_x30(z37=2000, z38=201000, z39=201029, z40=2, z41=811)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m40_03_2020():
    """Agaduran alternation"""
    """State 0,2: [Preset] Agaduran's alternate death process_SubState"""
    assert event_m40_03_x46(z25=4003000, z26=2100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_4000():
    """Fall into the hole and warp bottom"""
    """State 0,2: [Preset] Fall into the hole and warp_SubState"""
    assert event_m40_03_x31(z31=400002, z32=400005, z33=10250000, z34=400000, z35=403000003, z36=40030742)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_4010():
    """Fall into the hole and warp_Forest Shadow Forest"""
    """State 0,2: [Preset] Fall into the hole and warp_SubState"""
    assert event_m40_03_x31(z31=400000, z32=400003, z33=10320000, z34=400000, z35=403000001, z36=40030740)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_4020():
    """Falling into the hole and warping_Dragon Greig"""
    """State 0,2: [Preset] Fall into the hole and warp_SubState"""
    assert event_m40_03_x31(z31=400001, z32=400004, z33=20210000, z34=400000, z35=403000002, z36=40030741)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_4030():
    """Fall into the hole and warp (return from the boss room)"""
    """State 0,2: [Preset] Fall into the hole and warp (return from the boss room) _SubState"""
    assert event_m40_03_x40()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_5000():
    """Shenzhen Lighthouse 1"""
    """State 0,3: [Preset] Shenzhen Lighthouse_SubState"""
    call = event_m40_03_x36(flag2=403000001, z30=40030740)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m40_03_5010():
    """Shenzhen Lighthouse 2"""
    """State 0,3: [Preset] Shenzhen Lighthouse_SubState"""
    call = event_m40_03_x36(flag2=403000002, z30=40030741)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m40_03_5020():
    """Shenzhen Lighthouse 3"""
    """State 0,3: [Preset] Shenzhen Lighthouse_SubState"""
    call = event_m40_03_x36(flag2=403000003, z30=40030742)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m40_03_6000():
    """Water drops fall and torches disappear"""
    """State 0,2: [Lib] [Preset] _SubState that erases torches with point intrusion"""
    assert event_m40_03_x20(z49=600000, z50=600003, z51=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m40_03_8000():
    """White door opening setting_Scrap bottom"""
    """State 0,2: [Preset] Opening the white door_Scrap bottom_SubState"""
    assert event_m40_03_x47(z18=1005, z19=1006, z20=1007, z21=1008, z22=3200, z23=3210, z24=403020010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_8010():
    """White door opening setting_Forest shadow forest"""
    """State 0,2: [Preset] White door opening setting_Forest Shadow Forest_SubState"""
    assert event_m40_03_x53(z13=1000, z14=1002, z15=1003, z16=3000, z17=403020012)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_8020():
    """Opening the white door_Dolan Greig"""
    """State 0,2: [Preset] Opening of the white door_Drungreig_SubState"""
    assert event_m40_03_x54(z8=1004, z9=1009, z10=1012, z11=3100, z12=403020011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_9000():
    """Moya drawing switching"""
    """State 0,2: [Preset] Complicated drawing switching_SubState"""
    assert event_m40_03_x64(flag1=403000081, z1=40032010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_60000():
    """Pledge: Shenzhen Pilgrimage_Contribution UP"""
    """State 0,3: [Preset] Pledge: Shenzhen Pilgrimage_Contribution UP_SubState"""
    call = event_m40_03_x60(z2=400000, z3=400002, z4=403000001, z5=403000002, z6=403000003, z7=403000081)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m40_03_80000():
    """Rebirth of Fire 01_Dragon Craig_In front of the pilgrims in the underground Shenzhen"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m40_03_x26(z42=4003000, z43=4003099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m40_03_x0(flag3=403000081, z55=200000, z56=200002, z57=101, z58=4003000, z59=403020080, mode1=0):
    """[Lib] [Preset] Boss Battle Start
    flag3: Boss destruction flag
    z55: Start point ID
    z56: End point ID
    z57: Sound ID
    z58: Boss Battle ID
    z59: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m40_03_x1(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m40_03_x2(z55=z55, z56=z56)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m40_03_x3(z57=z57, z58=z58, z59=z59)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m40_03_x4()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m40_03_x5(z58=z58)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m40_03_x6(z57=z57, z58=z58, z59=z59, mode1=mode1)
    """State 7: End state"""
    return 0

def event_m40_03_x1(flag3=403000081):
    """[Reproduction] Boss Battle_Start
    flag3: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag3) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m40_03_x2(z55=200000, z56=200002):
    """[Condition] Boss Battle_Start
    z55: Start point ID
    z56: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z55, z56, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z55, z56, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m40_03_x3(z57=101, z58=4003000, z59=403020080):
    """[Execution] Boss Battle_Start
    z57: Sound ID
    z58: Boss Battle ID
    z59: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z57)
    """State 1: Boss battle start notification"""
    StartBossFight(z58)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z59, 1)
    """State 4: End state"""
    return 0

def event_m40_03_x4():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x5(z58=4003000):
    """[Condition] Boss Battle_End Judgment
    z58: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z58, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m40_03_x6(z57=101, z58=4003000, z59=403020080, mode1=0):
    """[Execute] Boss Battle_End
    z57: Sound ID
    z58: Boss Battle ID
    z59: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z59, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z58)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z57)
    """State 5: End state"""
    return 0

def event_m40_03_x7(z44=40031020, z45=100000, z46=100001, z47=40031010, z48=40031015):
    """[Lib] [Preset] Elevator
    z44: OBJ instance ID of the elevator
    z45: On elevator point ID_
    z46: Elevator point ID_below
    z47: Upper lever OBJ instance ID
    z48: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m40_03_x8()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m40_03_x9(z44=z44, z45=z45, z46=z46, z47=z47, z48=z48)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m40_03_x22(z44=z44, z46=z46)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m40_03_x21(z44=z44, z45=z45)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m40_03_x10(z44=z44, z45=z45)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m40_03_x11(z44=z44, z46=z46)
    """State 7: End state"""
    return 0

def event_m40_03_x8():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x9(z44=40031020, z45=100000, z46=100001, z47=40031010, z48=40031015):
    """[Condition] Elevator
    z44: Elevator OBJ instance ID
    z45: On elevator point ID_
    z46: Elevator point ID_below
    z47: Upper lever OBJ instance ID
    z48: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z44, 10, 0)
    CompareObjState(1, z44, 40, 0)
    CompareObjState(2, z44, 80, 0)
    CompareObjState(2, z44, 41, 0)
    CompareObjState(3, z44, 70, 0)
    CompareObjState(3, z44, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z46, z46, 1)
        CompareObjState(0, z47, 74, 0)
        CompareObjState(0, z47, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z45, z45, 1)
        CompareObjState(0, z48, 74, 0)
        CompareObjState(0, z48, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m40_03_x10(z44=40031020, z45=100000):
    """[Execution] Elevator_Rise
    z44: Elevator OBJ instance ID
    z45: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z44, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z44, 30, 0)
    IsPlayerInsidePoint(8, z45, z45, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z44, 71)
    assert CompareObjStateId(z44, 40, 0)
    """State 4: End state"""
    return 0

def event_m40_03_x11(z44=40031020, z46=100001):
    """[Execution] Elevator_Descent
    z44: Elevator OBJ instance ID
    z46: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z44, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z44, 41, 0)
    IsPlayerInsidePoint(8, z46, z46, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z44, 81)
    assert CompareObjStateId(z44, 10, 0)
    """State 4: End state"""
    return 0

def event_m40_03_x12(z52=40031020, z53=_, z54=_):
    """[Lib] [Preset] Elevator lever
    z52: OBJ instance ID of the elevator
    z53: Lever OBJ instance ID
    z54: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m40_03_x13()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m40_03_x14(z52=z52, z53=z53, z54=z54)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m40_03_x15(z52=z52, z53=z53, z54=z54)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m40_03_x16(z52=z52, z53=z53, z54=z54)
    """State 5: Rerun"""
    return 0

def event_m40_03_x13():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x14(z52=40031020, z53=_, z54=_):
    """[Condition] Elevator lever_use judgment
    z52: OBJ instance ID of the elevator
    z53: Lever OBJ instance ID
    z54: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z52, z54, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m40_03_x15(z52=40031020, z53=_, z54=_):
    """[Execution] Elevator lever_Key guide valid
    z52: OBJ instance ID of the elevator
    z53: Lever OBJ instance ID
    z54: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z53, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z52, z54, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m40_03_x16(z52=40031020, z53=_, z54=_):
    """[Execute] Elevator lever_key guide disabled
    z52: OBJ instance ID of the elevator
    z53: Lever OBJ instance ID
    z54: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z53, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z52, z54, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m40_03_x17():
    """[Lib] [Reproduction] Erase torches with point intrusion"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x18(z49=600000, z50=600003):
    """[Lib] [Condition] The torch is erased by point intrusion.
    z49: Start point ID
    z50: End point ID
    """
    """State 0,1: Did you enter the point with a torch on?"""
    IsPlayerInsidePoint(8, z49, z50, 1)
    IsPlayerUsingTorch(8, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m40_03_x19(z51=10, z49=600000, z50=600003):
    """[Lib] [Execution] erase torches with point intrusion
    z51: Torches digestion parameter ID
    z49: Start point ID
    z50: End point ID
    """
    """State 0,1: Turn off torches"""
    RemovePlayerTorches(z51)
    """State 2: Has the torch disappeared?"""
    IsPlayerUsingTorch(0, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m40_03_x20(z49=600000, z50=600003, z51=10):
    """[Lib] [Preset] Erase torches with point intrusion
    z49: Start point ID
    z50: End point ID
    z51: Torches digestion parameter ID
    """
    """State 0,1: [Lib] [Reproduction] _SubState that erases torches with point intrusion"""
    assert event_m40_03_x17()
    """State 3: [Lib] [Condition] _SubState that erases torches with point intrusion"""
    assert event_m40_03_x18(z49=z49, z50=z50)
    """State 2: [Lib] [Execution] _SubState that erases torches with point intrusion"""
    assert event_m40_03_x19(z51=z51, z49=z49, z50=z50)
    """State 4: End state"""
    return 0

def event_m40_03_x21(z44=40031020, z45=100000):
    """[Execution] Elevator_Return switch after lift
    z44: Elevator OBJ instance ID
    z45: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z44, 30, 0)
    IsPlayerInsidePoint(8, z45, z45, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z44, 71)
    assert CompareObjStateId(z44, 40, 0)
    """State 3: End state"""
    return 0

def event_m40_03_x22(z44=40031020, z46=100001):
    """[Execution] Elevator_Return switch after descending
    z44: Elevator OBJ instance ID
    z46: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z44, 41, 0)
    IsPlayerInsidePoint(8, z46, z46, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z44, 81)
    assert CompareObjStateId(z44, 10, 0)
    """State 3: End state"""
    return 0

def event_m40_03_x23():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x24(z42=4003000, z43=4003099):
    """[Lib] [execute] Rebirth fire
    z42: Flag start ID
    z43: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z42, z43, 0)
    """State 2: End state"""
    return 0

def event_m40_03_x25():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x26(z42=4003000, z43=4003099):
    """[Lib] [Preset] Rebirth
    z42: Flag start ID
    z43: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m40_03_x23()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m40_03_x25()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m40_03_x24(z42=z42, z43=z43)
    """State 4: End state"""
    return 0

def event_m40_03_x27():
    """[Reproduction] Generation of wormholes"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x28(z41=811):
    """[Condition] Wormhole generation
    z41: Agaduran Generator ID
    """
    """State 0,1: Agaduran special effects"""
    ChrHasSpEffect(0, z41, 95061010, 1)
    IsChrDead(1, z41)
    if ConditionGroup(1):
        """State 3: Defeat the boss"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m40_03_x29(z37=2000, z38=201000, z39=201029, z40=2, z41=811):
    """[Execution] Wormhole generation
    z37: Wormhole generator ID
    z38: Start point ID
    z39: End point ID
    z40: Generation distance order
    z41: Agaduran Generator ID
    """
    """State 0,1: Wormhole generation"""
    ForceGenerationFromPointBasedOnPosition(z37, 0, z38, z39, z40, 1)
    """State 3: Wormhole deletion judgment"""
    CompareChrEzStateValue(0, z37, 7, 1, 0)
    IsChrDead(1, z41)
    if ConditionGroup(1):
        """State 5: Delete Wormhole_2"""
        DeleteEnemyByGenerator(z37, 1)
        """State 7: Defeat the boss"""
        return 1
    elif ConditionGroup(0):
        """State 2: Deleting a wormhole"""
        DeleteEnemyByGenerator(z37, 1)
        """State 4: Agaduran special effects"""
        ChrHasSpEffect(0, z41, 95061010, 0)
        assert ConditionGroup(0)
        """State 6: End state"""
        return 0

def event_m40_03_x30(z37=2000, z38=201000, z39=201029, z40=2, z41=811):
    """[Preset] Wormhole generation
    z37: Wormhole generator ID
    z38: Start point ID
    z39: End point ID
    z40: Generation distance order
    z41: Agaduran Generator ID
    """
    """State 0,1: [Reproduction] Wormhole generation_SubState"""
    assert event_m40_03_x27()
    """State 3: [Condition] Wormhole generation_SubState"""
    call = event_m40_03_x28(z41=z41)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Execution] Wormhole generation_SubState"""
        call = event_m40_03_x29(z37=z37, z38=z38, z39=z39, z40=z40, z41=z41)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 4: Rerun"""
            return 0
    """State 5: Finish"""
    return 1

def event_m40_03_x31(z31=_, z32=_, z33=_, z34=400000, z35=_, z36=_):
    """[Preset] Drop into the hole and warp
    z31: Warp area point ID
    z32: Boss room warp point ID
    z33: MAPID has moved
    z34: Warp point ID of the moving MAP
    z35: Shenzhen Lighthouse Flag
    z36: Shenzhen Lighthouse OBJ instance ID
    """
    """State 0,1: [Reproduction] Falling into the hole and warp_SubState"""
    assert event_m40_03_x32()
    """State 2: [Condition] Fall into the hole and warp_SubState"""
    call = event_m40_03_x33(z31=z31, z35=z35, z36=z36)
    if call.Get() == 0:
        """State 3: [Execution] Fall into the hole and warp to boss room_SubState"""
        assert event_m40_03_x34(z32=z32)
    elif call.Done():
        """State 4: [Execution] Falling into the hole and warping _SubState to the moving MAP_SubState"""
        assert event_m40_03_x35(z33=z33, z34=z34)
    """State 5: End state"""
    return 0

def event_m40_03_x32():
    """[Reproduction] Warp falling into a hole"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x33(z31=_, z35=_, z36=_):
    """[Condition] Falling into the hole and warping
    z31: Warp area point ID
    z35: Shenzhen Lighthouse Flag
    z36: Shenzhen Lighthouse OBJ instance ID
    """
    """State 0,1: Did you enter the warp area?"""
    IsPlayerInsidePoint(0, z31, z31, 1)
    assert ConditionGroup(0)
    """State 4: Judgment of Shenzhen Lighthouse Flag State"""
    CompareEventFlag(0, z35, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 3: Judging the state of the lighthouse"""
        CompareObjState(0, z36, 10, 0)
        CompareObjState(0, z36, 30, 0)
        if ConditionGroup(0):
            pass
        else:
            """State 5: Raise the Shenzhen Lighthouse Flag"""
            SetEventFlag(z35, 1)
    """State 2: Can you go to the boss room?"""
    CompareEventFlag(8, 403000001, 1)
    CompareEventFlag(8, 403000002, 1)
    CompareEventFlag(8, 403000003, 1)
    if ConditionGroup(8):
        """State 6: Boss room"""
        return 0
    else:
        """State 7: Maps that have moved"""
        return 1

def event_m40_03_x34(z32=_):
    """[Execution] Fall into the hole and go to the warp boss room
    z32: Boss room warp point ID
    """
    """State 0,2: Save execution"""
    SaveExecution()
    """State 1: Warp to boss room"""
    PlayCutsceneAndWarpToMap(0, 0, 40030000, z32, 0)
    """State 3: End state"""
    return 0

def event_m40_03_x35(z33=_, z34=400000):
    """[Execution] Falling into the hole and going to the warped map
    z33: MAPID has moved
    z34: Warp point ID of the moving MAP
    """
    """State 0,3,2: Save execution"""
    SaveExecution()
    """State 1: Warp to MAP that has moved here"""
    PlayCutsceneAndWarpToMap(0, 0, z33, z34, 0)
    """State 4: End state"""
    return 0

def event_m40_03_x36(flag2=_, z30=_):
    """[Preset] Shenzhen Lighthouse
    flag2: Shenzhen Lighthouse Flag
    z30: Shenzhen Lighthouse OBJ instance ID
    """
    """State 0,1: [Reproduction] Lighthouse in Shenzhen_SubState"""
    call = event_m40_03_x37(flag2=flag2, z30=z30)
    if call.Get() == 0:
        """State 2: [Condition] Lighthouse in Shenzhen_SubState"""
        call = event_m40_03_x38(z30=z30)
        if call.Get() == 0:
            """State 3: [Execution] Shenzhen Lighthouse_SubState"""
            assert event_m40_03_x39(z30=z30)
        elif call.Get() == 1:
            """State 5: Rerun"""
            return 1
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m40_03_x37(flag2=_, z30=_):
    """[Reproduction] Lighthouse in Shenzhen
    flag2: Shenzhen Lighthouse Flag
    z30: Shenzhen Lighthouse OBJ instance ID
    """
    """State 0,1: Flag state determination"""
    if GetEventFlag(flag2) != 0:
        """State 2: Transition to lighting"""
        ChangeObjState(z30, 20)
    else:
        """State 3: Judgment of lighthouse OBJ status"""
        if CompareObjStateId(z30, 20, 0):
            pass
        elif CompareObjStateId(z30, 70, 0):
            pass
        else:
            """State 4: Unlit"""
            return 0
    """State 5: Lighted"""
    return 1

def event_m40_03_x38(z30=_):
    """[Conditions] Shenzhen Lighthouse
    z30: Lighthouse OBJ instance ID
    """
    """State 0,1: Judging the state of the lighthouse"""
    if CompareObjStateId(z30, 30, 0):
        """State 2: With key guide"""
        Label('L0')
        CompareObjState(0, z30, 70, 0)
        CompareObjState(0, z30, 20, 0)
        IsPlayerUsingTorch(8, 0)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 4: Transition to no key guide: 10"""
            ChangeObjState(z30, 10)
            CompareObjState(0, z30, 30, 1)
            assert ConditionGroup(0)
            """State 7: Rerun"""
            return 1
    else:
        """State 3: Without key guide"""
        CompareObjState(0, z30, 20, 0)
        CompareObjState(0, z30, 70, 0)
        IsPlayerUsingTorch(8, 1)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 5: Transition to key guide existence: 30"""
            ChangeObjState(z30, 30)
            Goto('L0')
    """State 6: Lighthouse: Lit"""
    return 0

def event_m40_03_x39(z30=_):
    """[Execution] Lighthouse in Shenzhen
    z30: Lighthouse OBJ instance ID
    """
    """State 0,1: Lights up: 70"""
    ChangeObjState(z30, 70)
    """State 2: Waiting for lighting"""
    assert CompareObjStateId(z30, 20, 0)
    """State 3,4: End state"""
    return 0

def event_m40_03_x40():
    """[Preset] Fall into the hole and warp (return from the boss room)"""
    """State 0,4: [Reproduction] Falling into the hole and warping (returning from the boss room) _SubState"""
    assert event_m40_03_x41()
    """State 5: [Condition] Fall into the hole and warp (return from the boss room) _SubState"""
    call = event_m40_03_x42(z27=102328, z28=102330, z29=102329)
    if call.Get() == 0:
        """State 1: [Execution] Falling into the hole and warping to the bottom of the waste_SubState"""
        assert event_m40_03_x35(z33=10250000, z34=400000)
    elif call.Get() == 1:
        """State 2: [Execution] Falling into the hole and warping to the forest of the shadow of shadows_SubState"""
        assert event_m40_03_x35(z33=10320000, z34=400000)
    elif call.Get() == 2:
        """State 3: [Execution] Falling into the hole and going to warp"""
        assert event_m40_03_x35(z33=20210000, z34=400000)
    """State 6: End state"""
    return 0

def event_m40_03_x41():
    """[Reproduction] Falling into the hole and warping (returning from the boss room)"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x42(z27=102328, z28=102330, z29=102329):
    """[Condition] Falling into the hole and warping (return from the boss room)
    z27: Judgment flag 1 from which map
    z28: Judgment flag 2 from which map
    z29: Flag 3 for judging which map came from
    """
    """State 0,1: Did you enter the warp area?"""
    IsPlayerInsidePoint(0, 401000, 401000, 1)
    assert ConditionGroup(0)
    """State 2: To the map that has moved: From which MAP?"""
    CompareEventFlag(0, z27, 1)
    CompareEventFlag(1, z28, 1)
    CompareEventFlag(2, z29, 1)
    if ConditionGroup(0):
        """State 4: The map that has moved (scrap bottom)"""
        return 0
    elif ConditionGroup(1):
        """State 5: A moving map (empty)"""
        return 1
    elif ConditionGroup(2):
        pass
    else:
        """State 3: None of the flags were standing"""
        pass
    """State 6: The map that has moved (Wangcheng)"""
    return 2

def event_m40_03_x43(z25=4003000):
    """[Conditions] Agaduran's alternate death treatment
    z25: Boss Battle ID
    """
    """State 0,2: Boss battle start waiting"""
    IsEventBossBattle(0, z25, 1)
    assert ConditionGroup(0)
    """State 1: Boss destruction waiting"""
    IsEventBossKill(0, z25, 0, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m40_03_x44():
    """[Reproduction] Agaduran's alternate death process"""
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(403000081) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m40_03_x45(z26=2100):
    """[Execution] Agaduran's alternate death process
    z26: Alternator generator ID
    """
    """State 0,1: Alternate death treatment"""
    EnemyActionRequest(z26, 1)
    """State 2: End state"""
    return 0

def event_m40_03_x46(z25=4003000, z26=2100):
    """[Preset] Agaduran's alternate death process
    z25: Boss Battle ID
    z26: Alternator generator ID
    """
    """State 0,1: [Reproduction] Agaduran's alternate death process_SubState"""
    call = event_m40_03_x44()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Agaduran's alternate death process_SubState"""
        assert event_m40_03_x43(z25=z25)
        """State 2: [Execution] Agaduran's alternate death process_SubState"""
        assert event_m40_03_x45(z26=z26)
    """State 4: End state"""
    return 0

def event_m40_03_x47(z18=1005, z19=1006, z20=1007, z21=1008, z22=3200, z23=3210, z24=403020010):
    """[Preset] Opening the white door_Scrap bottom
    z18: Generator ID of subjugation target 1
    z19: Generator ID of subjugation target 2
    z20: Generator ID of the target 3
    z21: Generator ID of subjugation target 4
    z22: Generator ID of subjugation target 5
    z23: Generator ID of the target 6
    z24: White door open flag
    """
    """State 0,1: [Reproduction] Opening the white door_SubState"""
    assert event_m40_03_x48()
    """State 2: [Conditions] Opening the white door_Scrap bottom_SubState"""
    assert event_m40_03_x49(z18=z18, z19=z19, z20=z20, z21=z21, z22=z22, z23=z23)
    """State 3: [Execution] Opening the white door_SubState"""
    assert event_m40_03_x50(z12=z24)
    """State 4: End state"""
    return 0

def event_m40_03_x48():
    """[Reproduction] Opening the white door"""
    """State 0,1: End state"""
    return 0

def event_m40_03_x49(z18=1005, z19=1006, z20=1007, z21=1008, z22=3200, z23=3210):
    """[Condition] White door opening setting_Scrap bottom
    z18: Generator ID of subjugation target 1
    z19: Generator ID of subjugation target 2
    z20: Generator ID of the target 3
    z21: Generator ID of subjugation target 4
    z22: Generator ID of subjugation target 5
    z23: Generator ID of the target 6
    """
    """State 0,1: Annihilation"""
    IsChrDeadOrRespawnOver(8, z18, 1)
    IsChrDeadOrRespawnOver(8, z19, 1)
    IsChrDeadOrRespawnOver(8, z20, 1)
    IsChrDeadOrRespawnOver(8, z21, 1)
    IsChrDeadOrRespawnOver(8, z22, 1)
    IsChrDeadOrRespawnOver(8, z23, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m40_03_x50(z12=_):
    """[Execution] Opening the white door
    z12: White door open flag
    """
    """State 0,1: Turn on the white door open flag"""
    SetEventFlag(z12, 1)
    """State 2: End state"""
    return 0

def event_m40_03_x51(z13=1000, z14=1002, z15=1003, z16=3000):
    """[Condition] Opening of white doors_Forest shadow forest
    z13: Generator ID of subjugation target 1
    z14: Generator ID of subjugation target 2
    z15: Generator ID of the target 3
    z16: Generator ID of subjugation target 4
    """
    """State 0,1: Annihilation"""
    IsChrDeadOrRespawnOver(8, z13, 1)
    IsChrDeadOrRespawnOver(8, z14, 1)
    IsChrDeadOrRespawnOver(8, z15, 1)
    IsChrDeadOrRespawnOver(8, z16, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m40_03_x52(z8=1004, z9=1009, z10=1012, z11=3100):
    """[Conditions] White door opening setting_Dolan Greig
    z8: Generator ID of subjugation target 1
    z9: Generator ID of subjugation target 2
    z10: Generator ID of the target 3
    z11: Generator ID of subjugation target 4
    """
    """State 0,1: Annihilation"""
    IsChrDeadOrRespawnOver(8, z8, 1)
    IsChrDeadOrRespawnOver(8, z9, 1)
    IsChrDeadOrRespawnOver(8, z10, 1)
    IsChrDeadOrRespawnOver(8, z11, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m40_03_x53(z13=1000, z14=1002, z15=1003, z16=3000, z17=403020012):
    """[Preset] White door opening setting_Forest shadow forest
    z13: Generator ID of subjugation target 1
    z14: Generator ID of subjugation target 2
    z15: Generator ID of the target 3
    z16: Generator ID of subjugation target 4
    z17: White door open flag
    """
    """State 0,1: [Reproduction] Opening the white door_SubState"""
    assert event_m40_03_x48()
    """State 2: [Conditions] Opening of white doors_Forest Shadow Forest_SubState"""
    assert event_m40_03_x51(z13=z13, z14=z14, z15=z15, z16=z16)
    """State 3: [Execution] Opening the white door_SubState"""
    assert event_m40_03_x50(z12=z17)
    """State 4: End state"""
    return 0

def event_m40_03_x54(z8=1004, z9=1009, z10=1012, z11=3100, z12=403020011):
    """[Preset] Opening the white door _ Dolan Greig
    z8: Generator ID of subjugation target 1
    z9: Generator ID of subjugation target 2
    z10: Generator ID of the target 3
    z11: Generator ID of subjugation target 4
    z12: White door open flag
    """
    """State 0,1: [Reproduction] Opening the white door_SubState"""
    assert event_m40_03_x48()
    """State 2: [Conditions] Opening the white door_Drungreig_SubState"""
    assert event_m40_03_x52(z8=z8, z9=z9, z10=z10, z11=z11)
    """State 3: [Execution] Opening the white door_SubState"""
    assert event_m40_03_x50(z12=z12)
    """State 4: End state"""
    return 0

def event_m40_03_x55():
    """[Reproduction] Pledge: Shenzhen Pilgrimage_Contribution UP"""
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 8: The guests"""
    return 4
    """State 3: Is the pledge a Shenzhen pilgrimage?"""
    Label('L0')
    if (GetPlayerCovenant() == 9) != 0:
        pass
    else:
        Goto('L1')
    """State 1: Shenzhen Pilgrimage: What are the pledge levels?"""
    if (GetPlayerCovenantLevel(9) > 3) != 0:
        """State 4: Level 3: Do nothing"""
        return 0
    elif (GetPlayerCovenantLevel(9) > 2) != 0:
        """State 5: Level 2: Boss destruction judgment"""
        return 1
    elif (GetPlayerCovenantLevel(9) > 1) != 0:
        """State 6: Level 1: Lighthouse judgment"""
        return 2
    else:
        """State 7: Level 0: Hole fall detection"""
        return 3
    """State 9: Pledge difference: End"""
    Label('L1')
    return 5

def event_m40_03_x56(z2=400000, z3=400002):
    """[Conditions] Pledge: Shenzhen Pilgrimage_Contribution UP_LV0
    z2: Hole warp_start point ID
    z3: Hole warp_end point ID
    """
    """State 0,1: Did you fall into the hole?"""
    IsPlayerInsidePoint(0, z2, z3, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m40_03_x57():
    """[Execution] Pledge: Shenzhen Pilgrimage_Contribution UP"""
    """State 0,1: Shenzhen Pilgrimage: Contribution +1"""
    AddPlayerCovenantContribution(9, 1)
    """State 2: End state"""
    return 0

def event_m40_03_x58(z4=403000001, z5=403000002, z6=403000003):
    """[Conditions] Pledge: Shenzhen Pilgrimage _ Contribution UP_LV1
    z4: Lighthouse ignition flag ①
    z5: Lighthouse ignition flag ②
    z6: Lighthouse ignition flag ③
    """
    """State 0,1: Are the three lighthouse lighting flags ON?"""
    CompareEventFlag(8, z4, 1)
    CompareEventFlag(8, z5, 1)
    CompareEventFlag(8, z6, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m40_03_x59(z7=403000081):
    """[Conditions] Pledge: Shenzhen Pilgrimage_Contribution UP_LV2
    z7: Boss destruction flag
    """
    """State 0,1: Boss: Did you destroy Agaduran?"""
    CompareEventFlag(0, z7, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m40_03_x60(z2=400000, z3=400002, z4=403000001, z5=403000002, z6=403000003, z7=403000081):
    """[Preset] Pledge: Shenzhen Pilgrimage_Contribution UP
    z2: Hole warp_start point ID
    z3: Hole warp_end point ID
    z4: Lighthouse ignition flag ①
    z5: Lighthouse ignition flag ②
    z6: Lighthouse ignition flag ③
    z7: Boss destruction flag
    """
    """State 0,1: [Reproduction] Pledge: Shenzhen Pilgrimage_Contribution UP_SubState"""
    call = event_m40_03_x55()
    if call.Get() == 4:
        """State 7: Finish"""
        Label('L0')
        return 1
    elif call.Get() == 5:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 3:
        """State 3: [Conditions] Pledge: Shenzhen Pilgrimage_Contribution UP_LV0_SubState"""
        assert event_m40_03_x56(z2=z2, z3=z3)
    elif call.Get() == 2:
        """State 4: [Conditions] Pledge: Shenzhen Pilgrimage_Contribution UP_LV1 o'clock_SubState"""
        assert event_m40_03_x58(z4=z4, z5=z5, z6=z6)
    elif call.Get() == 1:
        """State 5: [Conditions] Pledge: Shenzhen Pilgrimage_Contribution UP_LV2_SubState"""
        assert event_m40_03_x59(z7=z7)
    """State 2: [Execution] Pledge: Shenzhen Pilgrimage_Contribution UP_SubState"""
    assert event_m40_03_x57()
    """State 6: Rerun"""
    return 0

def event_m40_03_x61(flag1=403000081):
    """[Condition] Complicated drawing of haze
    flag1: Boss destruction flag
    """
    """State 0,1: Did you destroy the boss?"""
    CompareEventFlag(0, flag1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m40_03_x62(z1=40032010):
    """[Execution] Complicated drawing
    z1: Moya OBJ instance ID
    """
    """State 0,1: Display of haze"""
    ChangeObjState(z1, 10)
    """State 2: End state"""
    return 0

def event_m40_03_x63(z1=40032010, flag1=403000081):
    """[Reproduce] Complicated drawing
    z1: Moya OBJ instance ID
    flag1: Boss destruction flag
    """
    """State 0,2: Has the boss been destroyed?"""
    if GetEventFlag(flag1) != 0:
        """State 1: Display of haze"""
        ChangeObjState(z1, 10)
        """State 4: Finish"""
        return 0
    else:
        """State 3: Hidden hiding"""
        ChangeObjState(z1, 30)
        """State 5: Waiting for the white door to open"""
        return 1

def event_m40_03_x64(flag1=403000081, z1=40032010):
    """[Preset] Complicated drawing
    flag1: Boss destruction flag
    z1: Moya OBJ instance ID
    """
    """State 0,1: [Reproduction] Switching of Complicated Drawing_SubState"""
    call = event_m40_03_x63(z1=z1, flag1=flag1)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Condition] Switching of Complicated Drawing_SubState"""
        assert event_m40_03_x61(flag1=flag1)
        """State 2: [Execution] Complicated drawing_SubState"""
        assert event_m40_03_x62(z1=z1)
    """State 4: End state"""
    return 0

