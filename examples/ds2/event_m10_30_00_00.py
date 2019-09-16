# -*- coding: utf-8 -*-
def event_m10_30_1000():
    """Elevator Hidden Port"""
    """State 0,1: Has the initialization event been completed?"""
    assert EventEnded(1030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_30_x0(z14=10302000, z15=100000, z16=100010, z17=10301000, z18=10301010)
    """State 2: Rerun"""
    RestartMachine()

def event_m10_30_1010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_30_x5(z38=10302000, z39=10301000, z40=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_30_1020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_30_x5(z38=10302000, z39=10301010, z40=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_30_1030():
    """Elevator_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m10_30_x13(z34=10302000, z35=40, z36=130000001, z37=40)
    """State 1: Finish"""
    EndMachine()

def event_m10_30_1040():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m10_30_x19(z19=104000, z20=10302000, z21=105415, z22=10, z23=20, z24=0, z25=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_30_80000():
    """Reproduction Fire 01_Heide Great Fire Tower_Boss Heavy Cavalry Lighthouse"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_30_x28(z6=1030000, z7=1030099)
    """State 1: Finish"""
    EndMachine()

def event_m10_30_x0(z14=10302000, z15=100000, z16=100010, z17=10301000, z18=10301010):
    """[Lib] [Preset] Elevator
    z14: OBJ instance ID of the elevator
    z15: On elevator point ID_
    z16: Elevator point ID_below
    z17: Upper lever OBJ instance ID
    z18: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_30_x1()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_30_x2(z14=z14, z15=z15, z16=z16, z17=z17, z18=z18)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_30_x23(z14=z14, z16=z16)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_30_x22(z14=z14, z15=z15)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_30_x3(z14=z14, z15=z15)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_30_x4(z14=z14, z16=z16)
    """State 7: End state"""
    return 0

def event_m10_30_x1():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x2(z14=10302000, z15=100000, z16=100010, z17=10301000, z18=10301010):
    """[Condition] Elevator
    z14: Elevator OBJ instance ID
    z15: On elevator point ID_
    z16: Elevator point ID_below
    z17: Upper lever OBJ instance ID
    z18: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z14, 10, 0)
    CompareObjState(1, z14, 40, 0)
    CompareObjState(2, z14, 80, 0)
    CompareObjState(2, z14, 41, 0)
    CompareObjState(3, z14, 70, 0)
    CompareObjState(3, z14, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z16, z16, 1)
        CompareObjState(0, z17, 74, 0)
        CompareObjState(0, z17, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z15, z15, 1)
        CompareObjState(0, z18, 74, 0)
        CompareObjState(0, z18, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_30_x3(z14=10302000, z15=100000):
    """[Execution] Elevator_Rise
    z14: Elevator OBJ instance ID
    z15: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z14, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z14, 30, 0)
    IsPlayerInsidePoint(8, z15, z15, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z14, 71)
    assert CompareObjStateId(z14, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_30_x4(z14=10302000, z16=100010):
    """[Execution] Elevator_Descent
    z14: Elevator OBJ instance ID
    z16: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z14, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z14, 41, 0)
    IsPlayerInsidePoint(8, z16, z16, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z14, 81)
    assert CompareObjStateId(z14, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_30_x5(z38=10302000, z39=_, z40=_):
    """[Lib] [Preset] Elevator lever
    z38: OBJ instance ID of the elevator
    z39: Lever OBJ instance ID
    z40: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_30_x6()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_30_x7(z38=z38, z39=z39, z40=z40)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_30_x8(z38=z38, z39=z39, z40=z40)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_30_x9(z38=z38, z39=z39, z40=z40)
    """State 5: Rerun"""
    return 0

def event_m10_30_x6():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x7(z38=10302000, z39=_, z40=_):
    """[Condition] Elevator lever_use judgment
    z38: OBJ instance ID of the elevator
    z39: Lever OBJ instance ID
    z40: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z38, z40, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_30_x8(z38=10302000, z39=_, z40=_):
    """[Execution] Elevator lever_Key guide valid
    z38: OBJ instance ID of the elevator
    z39: Lever OBJ instance ID
    z40: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z39, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z38, z40, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x9(z38=10302000, z39=_, z40=_):
    """[Execute] Elevator lever_key guide disabled
    z38: OBJ instance ID of the elevator
    z39: Lever OBJ instance ID
    z40: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z39, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z38, z40, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x10(z36=130000001):
    """[Lib] [Reproduction] Elevator_Initialization
    z36: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(z36) != 0:
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

def event_m10_30_x12(z34=10302000, z35=40, z36=130000001, z37=40):
    """[Lib] [Execution] Elevator_Initialization
    z34: Elevator OBJ instance ID
    z35: Initial position OBJ state ID
    z36: Initialization completion flag
    z37: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z34, z35)
    assert CompareObjStateId(z34, z37, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z36, 1)
    """State 3: End state"""
    return 0

def event_m10_30_x13(z34=10302000, z35=40, z36=130000001, z37=40):
    """[Lib] [Preset] Elevator_Initialization
    z34: Elevator OBJ instance ID
    z35: Initial position OBJ state ID
    z36: Initialization completion flag
    z37: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m10_30_x10(z36=z36)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m10_30_x11()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m10_30_x12(z34=z34, z35=z35, z36=z36, z37=z37)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m10_30_x14(z26=9000, z27=0, z28=15, z29=130000010, z30=0, z31=1600, z32=6, z33=4000010):
    """[Lib] Character: Petrochemical: Key guide
    z26: generator
    z27: Death: Global event flag
    z28: Event action
    z29: Petrified: Area and other flags
    z30: Petrified: Global event flag
    z31: Key guide parameters
    z32: Petrification start state ID
    z33: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z26, z32, 0)
    CompareEventStatus(8, z33, 1, 0)
    CompareEventFlag(2, z29, 1)
    CompareEventFlag(3, z30, 1)
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
    CreateKeyGuideArea(34, z31)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z26)
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
                PlayerActionRequest(z28)
                IsPlayerPlayingMotion(0, z28, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z29, 1)
                CompareEventFlag(0, z29, 1)
                SetEventFlag(z30, 1)
                CompareEventFlag(1, z30, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z28, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_30_x15():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x16(z19=104000, z20=10302000, z22=10, z23=20):
    """[Lib] [Condition] Elevator_Connection replacement
    z19: Replacement point
    z20: OBJ instance ID of the elevator
    z22: Top_Hit group ID
    z23: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z19, z19, 1)
    CompareObjState(8, z20, 70, 0)
    IsPlayerInsidePoint(9, z19, z19, 1)
    CompareObjState(9, z20, 80, 0)
    IsPlayerOnHitGroup(0, z22, 1)
    IsPlayerOnHitGroup(1, z23, 1)
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

def event_m10_30_x17(z19=104000, z21=105415, z24=0, z22=10, z20=10302000):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z19: Replacement point
    z21: Global flag for connection
    z24: ON / OFF of global flag
    z22: Top_Hit group ID
    z20: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z21, z24)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z19, z19, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z22, 1)
    IsPlayerInsidePoint(8, z19, z19, 1)
    CompareObjState(8, z20, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_30_x18(z21=105415, z24=0, z22=10, z19=104000, z20=10302000):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z21: Global flag for connection
    z24: ON / OFF of global flag
    z22: Hit group ID
    z19: Replacement point ID
    z20: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z21, z24)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z22, 0)
    IsPlayerInsidePoint(8, z19, z19, 1)
    CompareObjState(8, z20, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x19(z19=104000, z20=10302000, z21=105415, z22=10, z23=20, z24=0, z25=1):
    """[Lib] [Preset] Elevator_Connection replacement
    z19: Replacement point
    z20: OBJ instance ID of the elevator
    z21: Global flag for connection
    z22: Top_Hit group ID
    z23: Bottom_Hit group ID
    z24: Up_Global flag when rising
    z25: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m10_30_x15()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m10_30_x16(z19=z19, z20=z20, z22=z22, z23=z23)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m10_30_x17(z19=z19, z21=z21, z24=z24, z22=z22, z20=z20)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m10_30_x21(z19=z19, z21=z21, z25=z25, z23=z23, z20=z20)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m10_30_x18(z21=z21, z24=z24, z22=z22, z19=z19, z20=z20)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m10_30_x20(z21=z21, z25=z25, z23=z23, z19=z19, z20=z20)
    """State 7: End state"""
    return 0

def event_m10_30_x20(z21=105415, z25=1, z23=20, z19=104000, z20=10302000):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z21: Global flag for connection
    z25: ON / OFF of global flag
    z23: Hit group ID
    z19: Replacement point ID
    z20: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z21, z25)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z23, 0)
    IsPlayerInsidePoint(8, z19, z19, 1)
    CompareObjState(8, z20, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_30_x21(z19=104000, z21=105415, z25=1, z23=20, z20=10302000):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z19: Replacement point
    z21: Global flag for connection
    z25: ON / OFF of global flag
    z23: Bottom_Hit group ID
    z20: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z21, z25)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z19, z19, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z23, 1)
    IsPlayerInsidePoint(8, z19, z19, 1)
    CompareObjState(8, z20, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_30_x22(z14=10302000, z15=100000):
    """[Execution] Elevator_Return switch after lift
    z14: Elevator OBJ instance ID
    z15: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z14, 30, 0)
    IsPlayerInsidePoint(8, z15, z15, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z14, 71)
    assert CompareObjStateId(z14, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_30_x23(z14=10302000, z16=100010):
    """[Execution] Elevator_Return switch after descending
    z14: Elevator OBJ instance ID
    z16: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z14, 41, 0)
    IsPlayerInsidePoint(8, z16, z16, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z14, 81)
    assert CompareObjStateId(z14, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_30_x24(z8=9000, z9=0, z10=130000010, z11=0, z12=0, z13=4000000):
    """[Lib] Character: Petrified: Appearance setting
    z8: Generator ID
    z9: Death: Global event flag
    z10: Petrified: Area and other flags
    z11: Petrified: Global event flag
    z12: Startup state
    z13: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z8)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z9, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z10, 1)
                CompareEventFlag(1, z11, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z8, z12)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()

def event_m10_30_x25():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x26(z6=1030000, z7=1030099):
    """[Lib] [execute] Rebirth fire
    z6: Flag start ID
    z7: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z6, z7, 0)
    """State 2: End state"""
    return 0

def event_m10_30_x27():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_30_x28(z6=1030000, z7=1030099):
    """[Lib] [Preset] Rebirth
    z6: Flag start ID
    z7: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_30_x25()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_30_x27()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_30_x26(z6=z6, z7=z7)
    """State 4: End state"""
    return 0

def event_m10_30_x29(z4=130000010, z5=0, z3=2, z2=0, z1=6000020):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z4: Other flags
    z5: Global flag
    z3: Additional attributes
    z2: Delete attribute
    z1: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z4) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z5) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z1, z3)
        DeleteNavimeshAttribute(z1, z2)
        """State 3: Flag OFF"""
        return 0

def event_m10_30_x30(z4=130000010, z5=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z4: Other flags
    z5: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z4, 1)
    CompareEventFlag(0, z5, 1)
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

def event_m10_30_x32(z1=6000020, z2=0, z3=2, z4=130000010, z5=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z1: Navimesh switching point ID
    z2: Additional attributes
    z3: Delete attribute
    z4: Other flags
    z5: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_30_x29(z4=z4, z5=z5, z3=z3, z2=z2, z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_30_x30(z4=z4, z5=z5)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_30_x31(z1=z1, z2=z2, z3=z3)
    """State 4: End state"""
    return 0

def event_m10_30_4000000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_30_x14(z26=9000, z27=0, z28=15, z29=130000010, z30=0, z31=1600, z32=6, z33=4000010)
    """State 1: Finish"""
    EndMachine()

def event_m10_30_4000010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_30_x24(z8=9000, z9=0, z10=130000010, z11=0, z12=0, z13=4000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_30_4000020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_30_x32(z1=6000020, z2=0, z3=2, z4=130000010, z5=0)
    """State 1: Finish"""
    EndMachine()

