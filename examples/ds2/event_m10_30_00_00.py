# -*- coding: utf-8 -*-
def event_m10_30_1000():
    """Elevator Hidden Port"""
    """State 0,1: Has the initialization event been completed?"""
    assert EventEnded(1030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_30_x0(z12=10302000, z13=100000, z14=100010, z15=10301000, z16=10301010)
    """State 2: Rerun"""
    RestartMachine()
    Quit()

def event_m10_30_1010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_30_x5(z35=10302000, z36=10301000, z37=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_30_1020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_30_x5(z35=10302000, z36=10301010, z37=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_30_1030():
    """Elevator_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m10_30_x13(z32=10302000, z33=40, flag3=130000001, z34=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_30_1040():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m10_30_x19(z17=104000, z18=10302000, z19=105415, z20=10, z21=20, z22=0, z23=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_30_80000():
    """Reproduction Fire 01_Heide Great Fire Tower_Boss Heavy Cavalry Lighthouse"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_30_x28(z4=1030000, z5=1030099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_30_x0(z12=10302000, z13=100000, z14=100010, z15=10301000, z16=10301010):
    """[Lib] [Preset] Elevator
    z12: OBJ instance ID of the elevator
    z13: On elevator point ID_
    z14: Elevator point ID_below
    z15: Upper lever OBJ instance ID
    z16: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_30_x1()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_30_x2(z12=z12, z13=z13, z14=z14, z15=z15, z16=z16)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_30_x23(z12=z12, z14=z14)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_30_x22(z12=z12, z13=z13)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_30_x3(z12=z12, z13=z13)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_30_x4(z12=z12, z14=z14)
    """State 7: End state"""
    return 0

def event_m10_30_x1():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x2(z12=10302000, z13=100000, z14=100010, z15=10301000, z16=10301010):
    """[Condition] Elevator
    z12: Elevator OBJ instance ID
    z13: On elevator point ID_
    z14: Elevator point ID_below
    z15: Upper lever OBJ instance ID
    z16: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z12, 10, 0)
    CompareObjState(1, z12, 40, 0)
    CompareObjState(2, z12, 80, 0)
    CompareObjState(2, z12, 41, 0)
    CompareObjState(3, z12, 70, 0)
    CompareObjState(3, z12, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z14, z14, 1)
        CompareObjState(0, z15, 74, 0)
        CompareObjState(0, z15, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z13, z13, 1)
        CompareObjState(0, z16, 74, 0)
        CompareObjState(0, z16, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_30_x3(z12=10302000, z13=100000):
    """[Execution] Elevator_Rise
    z12: Elevator OBJ instance ID
    z13: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z12, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z12, 30, 0)
    IsPlayerInsidePoint(8, z13, z13, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z12, 71)
    assert CompareObjStateId(z12, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_30_x4(z12=10302000, z14=100010):
    """[Execution] Elevator_Descent
    z12: Elevator OBJ instance ID
    z14: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z12, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z12, 41, 0)
    IsPlayerInsidePoint(8, z14, z14, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z12, 81)
    assert CompareObjStateId(z12, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_30_x5(z35=10302000, z36=_, z37=_):
    """[Lib] [Preset] Elevator lever
    z35: OBJ instance ID of the elevator
    z36: Lever OBJ instance ID
    z37: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_30_x6()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_30_x7(z35=z35, z36=z36, z37=z37)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_30_x8(z35=z35, z36=z36, z37=z37)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_30_x9(z35=z35, z36=z36, z37=z37)
    """State 5: Rerun"""
    return 0

def event_m10_30_x6():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x7(z35=10302000, z36=_, z37=_):
    """[Condition] Elevator lever_use judgment
    z35: OBJ instance ID of the elevator
    z36: Lever OBJ instance ID
    z37: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z35, z37, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_30_x8(z35=10302000, z36=_, z37=_):
    """[Execution] Elevator lever_Key guide valid
    z35: OBJ instance ID of the elevator
    z36: Lever OBJ instance ID
    z37: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z36, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z35, z37, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x9(z35=10302000, z36=_, z37=_):
    """[Execute] Elevator lever_key guide disabled
    z35: OBJ instance ID of the elevator
    z36: Lever OBJ instance ID
    z37: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z36, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z35, z37, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x10(flag3=130000001):
    """[Lib] [Reproduction] Elevator_Initialization
    flag3: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag3) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m10_30_x11():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_30_x12(z32=10302000, z33=40, flag3=130000001, z34=40):
    """[Lib] [Execution] Elevator_Initialization
    z32: Elevator OBJ instance ID
    z33: Initial position OBJ state ID
    flag3: Initialization completion flag
    z34: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z32, z33)
    assert CompareObjStateId(z32, z34, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag3, 1)
    """State 3: End state"""
    return 0

def event_m10_30_x13(z32=10302000, z33=40, flag3=130000001, z34=40):
    """[Lib] [Preset] Elevator_Initialization
    z32: Elevator OBJ instance ID
    z33: Initial position OBJ state ID
    flag3: Initialization completion flag
    z34: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m10_30_x10(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m10_30_x11()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m10_30_x12(z32=z32, z33=z33, flag3=flag3, z34=z34)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m10_30_x14(z24=9000, z25=0, z26=15, z27=130000010, z28=0, z29=1600, z30=6, z31=4000010):
    """[Lib] Character: Petrochemical: Key guide
    z24: generator
    z25: Death: Global event flag
    z26: Event action
    z27: Petrified: Area and other flags
    z28: Petrified: Global event flag
    z29: Key guide parameters
    z30: Petrification start state ID
    z31: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z24, z30, 0)
    CompareEventStatus(8, z31, 1, 0)
    CompareEventFlag(2, z27, 1)
    CompareEventFlag(3, z28, 1)
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
    CreateKeyGuideArea(34, z29)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z24)
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
                PlayerActionRequest(z26)
                IsPlayerPlayingMotion(0, z26, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z27, 1)
                CompareEventFlag(0, z27, 1)
                SetEventFlag(z28, 1)
                CompareEventFlag(1, z28, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z26, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()
    Quit()

def event_m10_30_x15():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x16(z17=104000, z18=10302000, z20=10, z21=20):
    """[Lib] [Condition] Elevator_Connection replacement
    z17: Replacement point
    z18: OBJ instance ID of the elevator
    z20: Top_Hit group ID
    z21: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z17, z17, 1)
    CompareObjState(8, z18, 70, 0)
    IsPlayerInsidePoint(9, z17, z17, 1)
    CompareObjState(9, z18, 80, 0)
    IsPlayerOnHitGroup(0, z20, 1)
    IsPlayerOnHitGroup(1, z21, 1)
    if ConditionGroup(8):
        """State 2: Ascent point intrusion"""
        return 0
    elif ConditionGroup(9):
        """State 3: Point entry while descending"""
        return 1
    elif ConditionGroup(0):
        """State 4: Be on top"""
        return 2
    elif ConditionGroup(1):
        """State 5: Be down"""
        return 3

def event_m10_30_x17(z17=104000, z19=105415, z22=0, z20=10, z18=10302000):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z17: Replacement point
    z19: Global flag for connection
    z22: ON / OFF of global flag
    z20: Top_Hit group ID
    z18: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z19, z22)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z17, z17, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z20, 1)
    IsPlayerInsidePoint(8, z17, z17, 1)
    CompareObjState(8, z18, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_30_x18(z19=105415, z22=0, z20=10, z17=104000, z18=10302000):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z19: Global flag for connection
    z22: ON / OFF of global flag
    z20: Hit group ID
    z17: Replacement point ID
    z18: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z19, z22)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z20, 0)
    IsPlayerInsidePoint(8, z17, z17, 1)
    CompareObjState(8, z18, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x19(z17=104000, z18=10302000, z19=105415, z20=10, z21=20, z22=0, z23=1):
    """[Lib] [Preset] Elevator_Connection replacement
    z17: Replacement point
    z18: OBJ instance ID of the elevator
    z19: Global flag for connection
    z20: Top_Hit group ID
    z21: Bottom_Hit group ID
    z22: Up_Global flag when rising
    z23: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m10_30_x15()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m10_30_x16(z17=z17, z18=z18, z20=z20, z21=z21)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m10_30_x17(z17=z17, z19=z19, z22=z22, z20=z20, z18=z18)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m10_30_x21(z17=z17, z19=z19, z23=z23, z21=z21, z18=z18)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m10_30_x18(z19=z19, z22=z22, z20=z20, z17=z17, z18=z18)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m10_30_x20(z19=z19, z23=z23, z21=z21, z17=z17, z18=z18)
    """State 7: End state"""
    return 0

def event_m10_30_x20(z19=105415, z23=1, z21=20, z17=104000, z18=10302000):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z19: Global flag for connection
    z23: ON / OFF of global flag
    z21: Hit group ID
    z17: Replacement point ID
    z18: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z19, z23)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z21, 0)
    IsPlayerInsidePoint(8, z17, z17, 1)
    CompareObjState(8, z18, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x21(z17=104000, z19=105415, z23=1, z21=20, z18=10302000):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z17: Replacement point
    z19: Global flag for connection
    z23: ON / OFF of global flag
    z21: Bottom_Hit group ID
    z18: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z19, z23)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z17, z17, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z21, 1)
    IsPlayerInsidePoint(8, z17, z17, 1)
    CompareObjState(8, z18, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_30_x22(z12=10302000, z13=100000):
    """[Execution] Elevator_Return switch after lift
    z12: Elevator OBJ instance ID
    z13: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z12, 30, 0)
    IsPlayerInsidePoint(8, z13, z13, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z12, 71)
    assert CompareObjStateId(z12, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_30_x23(z12=10302000, z14=100010):
    """[Execution] Elevator_Return switch after descending
    z12: Elevator OBJ instance ID
    z14: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z12, 41, 0)
    IsPlayerInsidePoint(8, z14, z14, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z12, 81)
    assert CompareObjStateId(z12, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_30_x24(z6=9000, z7=0, z8=130000010, z9=0, z10=0, z11=4000000):
    """[Lib] Character: Petrified: Appearance setting
    z6: Generator ID
    z7: Death: Global event flag
    z8: Petrified: Area and other flags
    z9: Petrified: Global event flag
    z10: Startup state
    z11: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z6)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z7, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z8, 1)
                CompareEventFlag(1, z9, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z6, z10)
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

def event_m10_30_x25():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x26(z4=1030000, z5=1030099):
    """[Lib] [execute] Rebirth fire
    z4: Flag start ID
    z5: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z4, z5, 0)
    """State 2: End state"""
    return 0

def event_m10_30_x27():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x28(z4=1030000, z5=1030099):
    """[Lib] [Preset] Rebirth
    z4: Flag start ID
    z5: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_30_x25()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_30_x27()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_30_x26(z4=z4, z5=z5)
    """State 4: End state"""
    return 0

def event_m10_30_x29(flag1=130000010, flag2=0, z3=2, z2=0, z1=6000020):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    flag1: Other flags
    flag2: Global flag
    z3: Additional attributes
    z2: Delete attribute
    z1: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(flag1) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(flag2) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z1, z3)
        DeleteNavimeshAttribute(z1, z2)
        """State 3: Flag OFF"""
        return 0

def event_m10_30_x30(flag1=130000010, flag2=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    flag1: Other flags
    flag2: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, flag1, 1)
    CompareEventFlag(0, flag2, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_30_x31(z1=6000020, z2=0, z3=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z1: Navimesh switching point ID
    z2: Additional attributes
    z3: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z1, z2)
    DeleteNavimeshAttribute(z1, z3)
    """State 2: End state"""
    return 0

def event_m10_30_x32(z1=6000020, z2=0, z3=2, flag1=130000010, flag2=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z1: Navimesh switching point ID
    z2: Additional attributes
    z3: Delete attribute
    flag1: Other flags
    flag2: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_30_x29(flag1=flag1, flag2=flag2, z3=z3, z2=z2, z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_30_x30(flag1=flag1, flag2=flag2)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_30_x31(z1=z1, z2=z2, z3=z3)
    """State 4: End state"""
    return 0

def event_m10_30_4000000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_30_x14(z24=9000, z25=0, z26=15, z27=130000010, z28=0, z29=1600, z30=6, z31=4000010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_30_4000010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_30_x24(z6=9000, z7=0, z8=130000010, z9=0, z10=0, z11=4000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_30_4000020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_30_x32(z1=6000020, z2=0, z3=2, flag1=130000010, flag2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

