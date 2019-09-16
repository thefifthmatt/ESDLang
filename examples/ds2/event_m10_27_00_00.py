# -*- coding: utf-8 -*-
def event_m10_27_1000():
    """Flying Wyvern _ crossing the bridge 1"""
    """State 0,2: [Preset] Wyvern in the middle to distant view_SubState"""
    assert event_m10_27_x90(z22=70)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_2000():
    """Flying Wyvern _ 2 across the bridge"""
    """State 0,2: [Preset] Wyvern in the middle to distant view_SubState"""
    assert event_m10_27_x90(z22=72)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_3000():
    """Flying Wyvern_Bridge Drop"""
    """State 0,3: [DC] [Preset] Bridge destruction event activation determination_SubState"""
    call = event_m10_27_x116(z3=10271200, z4=10271800, z5=300000, z6=300001, z7=10271210)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        Label('L0')
        RestartMachine()
    elif call.Get() == 2:
        Goto('L0')

def event_m10_27_3010():
    """Determining the number of Wyvern eggs destroyed"""
    """State 0,2: [Preset] Determining the number of eggs destroyed_1 to 7_SubState"""
    assert event_m10_27_x91(z20=1, z21=127020010)
    """State 3: [Preset] Egg Destruction Count_8-14_SubState"""
    assert event_m10_27_x91(z20=8, z21=127020011)
    """State 4: [Preset] Egg destruction count determination_15-21_SubState"""
    assert event_m10_27_x91(z20=15, z21=127020012)
    """State 5: [Preset] Egg destruction count judgment_22 ~ 28_SubState"""
    assert event_m10_27_x91(z20=22, z21=127020013)
    """State 6: [Preset] Determining the number of eggs destroyed _29 ~ _SubState"""
    assert event_m10_27_x91(z20=29, z21=127020014)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4000():
    """Flying Wyvern_Swirl 1"""
    """State 0,2: [Preset] Wyvern in the middle to distant view_SubState"""
    assert event_m10_27_x90(z22=78)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_5000():
    """Flying Wyvern _ Turn 2"""
    """State 0,2: [Preset] Wyvern in the middle to distant view_SubState"""
    assert event_m10_27_x90(z22=80)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_6000():
    """Connection flag ON"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_27_x27(z85=105425, z86=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_27_7000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_27_x13(z104=10272000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_7010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_27_x17(z102=10272000, val2=10270010, z103=0.6, val3=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_7020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_27_x20(z87=10272500, z88=20, z89=702000, z90=0, z91=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_8000():
    """Get an old dragon egg"""
    """State 0,2: [Preset] Get the dragon egg _SubState"""
    assert event_m10_27_x104(z18=10272600, z19=100866)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_9000():
    """Wyvern attack power UP1 when breaking an egg"""
    """State 0,2: [Preset] Wyvern attack power UP_SubState"""
    assert event_m10_27_x105(z10=1101, z11=10273100, z12=10273199, z13=3, z14=10, z15=127020001, z16=127020001)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_9010():
    """Wyvern attack power UP2 when breaking an egg"""
    """State 0,2: [Preset] Wyvern attack power UP_SubState"""
    assert event_m10_27_x105(z10=1102, z11=10273200, z12=10273299, z13=3, z14=10, z15=127020002, z16=127020002)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_9020():
    """Wyvern attack power UP3 when breaking an egg"""
    """State 0,2: [Preset] Wyvern attack power UP_SubState"""
    assert event_m10_27_x105(z10=1100, z11=10273300, z12=10273399, z13=3, z14=10, z15=127020003, z16=127020003)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_10000():
    """Hostile with the ancient dragon"""
    """State 0,2: Did you host an old dragon?"""
    assert GetEventFlag(103970) != 0
    """State 3: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m10_27_x0(z109=127000081, z110=1000000, z111=1000000, z112=101, z113=1027000, z114=127020080,
            mode3=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_27_10010():
    """White door condition monitoring"""
    """State 0,2: [Preset] Old Dragon White Door Management_SubState"""
    assert event_m10_27_x100()
    """State 1: Finish"""
    EndMachine()

def event_m10_27_11000():
    """An old dragon warrior is powered down by subjugating the Wyvern 1"""
    """State 0,2: [Preset] Old dragon warrior power down by Wyvern subjugation_SubState"""
    assert event_m10_27_x109(z8=1100, z9=127020020)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_11010():
    """Old dragon warrior power down 2"""
    """State 0,2: [Preset] Old dragon warrior power down by Wyvern subjugation_SubState"""
    assert event_m10_27_x109(z8=1101, z9=127020021)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_11020():
    """An old dragon warrior is powered down by the Wyvern subjugation 3"""
    """State 0,2: [Preset] Old dragon warrior power down by Wyvern subjugation_SubState"""
    assert event_m10_27_x109(z8=1102, z9=127020022)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_80000():
    """Regenerative fire 01_in the rock ahead of the starting point"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_27_x33(z76=1027000, z77=1027099)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_81000():
    """Rebirth of Fire 02_Across the bridge destroyed by Wyvern"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_27_x33(z76=1027100, z77=1027199)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_x0(z109=127000081, z110=1000000, z111=1000000, z112=101, z113=1027000, z114=127020080,
                    mode3=0):
    """[Lib] [Preset] Boss Battle Start
    z109: Boss destruction flag
    z110: Start point ID
    z111: End point ID
    z112: Sound ID
    z113: Boss Battle ID
    z114: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_27_x1(z109=z109)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_27_x2(z110=z110, z111=z111)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_27_x3(z112=z112, z113=z113, z114=z114)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_27_x4()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_27_x5(z113=z113)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_27_x6(z112=z112, z113=z113, z114=z114, mode3=mode3)
    """State 7: End state"""
    return 0

def event_m10_27_x1(z109=127000081):
    """[Reproduction] Boss Battle_Start
    z109: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z109) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_27_x2(z110=1000000, z111=1000000):
    """[Condition] Boss Battle_Start
    z110: Start point ID
    z111: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z110, z111, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z110, z111, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x3(z112=101, z113=1027000, z114=127020080):
    """[Execution] Boss Battle_Start
    z112: Sound ID
    z113: Boss Battle ID
    z114: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z112)
    """State 1: Boss battle start notification"""
    StartBossFight(z113)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z114, 1)
    """State 4: End state"""
    return 0

def event_m10_27_x4():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x5(z113=1027000):
    """[Condition] Boss Battle_End Judgment
    z113: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z113, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x6(z112=101, z113=1027000, z114=127020080, mode3=0):
    """[Execute] Boss Battle_End
    z112: Sound ID
    z113: Boss Battle ID
    z114: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z114, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z113)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode3) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z112)
    """State 5: End state"""
    return 0

def event_m10_27_x7(z104=10272000):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z104: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z104, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z104, 10)
        assert CompareObjStateId(z104, 10, 0)
    elif CompareObjStateId(z104, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z104, 74, 1) and CompareObjStateId(z104, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_27_x8(z104=10272000, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z104: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z104)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_27_x9(z104=10272000, z106=38, z107=12, z108=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z104: Object instance ID
    z106: Key guide type
    z107: Event action
    z108: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z104, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z104, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z104, 30)
        assert CompareObjStateId(z104, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z104, z106, z107)
        assert PlayerIsInEventAction(z107) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z107, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z104, 74, 0)
        CompareObjState(1, z104, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z108)
            assert CompareObjStateId(z104, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z104, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_27_x10(z104=10272000, z105=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z104: Object instance ID
    z105: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z104, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_27_x11(z104=10272000):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z104: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z104, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x12():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x13(z104=10272000):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z104: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_27_x7(z104=z104)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_27_x11(z104=z104)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_27_x12()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_27_x8(z104=z104, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_27_x9(z104=z104, z106=38, z107=12, z108=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_27_x10(z104=z104, z105=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_27_x14(z102=10272000, val2=10270010):
    """[Reproduction] Hidden door 1_face SFX
    z102: OBJ instance ID of the bug key
    val2: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z102, 20, 0):
        pass
    else:
        Goto('L0')
    """State 2: Event light reproduction judgment"""
    if (not val2) != 0:
        pass
    else:
        """State 3: Event light ON"""
        SetPointLightEnabled(val2, 1, 0)
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
    if (not val2) != 0:
        pass
    else:
        """State 4: Event light OFF"""
        SetPointLightEnabled(val2, 0, 0)
    """State 9: Not started"""
    return 1

def event_m10_27_x15(z102=10272000):
    """[Conditions] Hidden door 1_Face SFX
    z102: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z102, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x16(z102=10272000, val2=10270010, z103=0.6, val3=1.5):
    """[Execution] Hidden door 1_Face SFX
    z102: OBJ instance ID of the bug key
    val2: Event light ID
    z103: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,2: Event light usage judgment"""
    if (not val2) != 0:
        """State 5: Wait until face SFX playback"""
        assert (GetStateTime() > val3) != 0
        """State 4: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    else:
        """State 1: Event light ON"""
        SetPointLightEnabled(val2, 1, z103)
        assert (GetStateTime() > val3) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_27_x17(z102=10272000, val2=10270010, z103=0.6, val3=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z102: OBJ instance ID of the bug key
    val2: Event light ID
    z103: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_27_x14(z102=z102, val2=val2)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_27_x15(z102=z102)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_27_x16(z102=z102, val2=val2, z103=z103, val3=val3)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_27_x18(z100=104020, z101=102087):
    """[Lib] Map intrusion detection: General purpose
    z100: Death: Global event flag
    z101: Intrusion: Global event flag
    """
    """State 0,2: Intrusion detection: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Intrusion detection: Death determination"""
        CompareEventFlag(0, z100, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Intrusion detection: Flag determination"""
            CompareEventFlag(0, z101, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Intrusion detection: Map intrusion determination"""
                SetEventFlag(z101, 1)
                CompareEventFlag(0, z101, 1)
                assert ConditionGroup(0)
    """State 1: Intrusion detection: System: Exit"""
    EndMachine()

def event_m10_27_x19(z92=6000, z93=0, z94=15, z95=127000030, z96=0, z97=1600, z98=6, z99=4004010):
    """[Lib] Character: Petrochemical: Key guide
    z92: generator
    z93: Death: Global event flag
    z94: Event action
    z95: Petrified: Area and other flags
    z96: Petrified: Global event flag
    z97: Key guide parameters
    z98: Petrification start state ID
    z99: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z92, z98, 0)
    CompareEventStatus(8, z99, 1, 0)
    CompareEventFlag(2, z95, 1)
    CompareEventFlag(3, z96, 1)
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
    CreateKeyGuideArea(34, z97)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z92)
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
                PlayerActionRequest(z94)
                IsPlayerPlayingMotion(0, z94, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z95, 1)
                CompareEventFlag(0, z95, 1)
                SetEventFlag(z96, 1)
                CompareEventFlag(1, z96, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z94, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_27_x20(z87=10272500, z88=20, z89=702000, z90=0, z91=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z87: Object instance ID
    z88: OBJ state ID
    z89: Navimesh switching point ID
    z90: Additional attributes
    z91: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_27_x21(z87=z87, z88=z88, z89=z89, z91=z91, z90=z90)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_27_x22(z87=z87, z88=z88, z89=z89)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_27_x23(z87=z87, z88=z88, z89=z89, z90=z90, z91=z91)
    """State 4: End state"""
    return 0

def event_m10_27_x21(z87=10272500, z88=20, z89=702000, z91=2, z90=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z87: Target OBJ instance ID
    z88: Target OBJ state ID
    z89: Navimesh switching point ID
    z91: Additional attributes
    z90: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z87, z88, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z89, z91)
        DeleteNavimeshAttribute(z89, z90)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_27_x22(z87=10272500, z88=20, z89=702000):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z87: Target OBJ instance ID
    z88: Target OBJ state ID
    z89: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z87, z88, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x23(z87=10272500, z88=20, z89=702000, z90=0, z91=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z87: Target OBJ instance ID
    z88: Target OBJ state ID
    z89: Navimesh switching point ID
    z90: Additional attributes
    z91: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z89, z90)
    DeleteNavimeshAttribute(z89, z91)
    """State 2: End state"""
    return 0

def event_m10_27_x24():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x25():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x26(z85=105425, z86=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z85: Global event flag for connection
    z86: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z85, z86)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z85, z86)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_27_x27(z85=105425, z86=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z85: Global event flag for connection
    z86: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_27_x24()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_27_x25()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_27_x26(z85=z85, z86=z86)
    """State 4: End state"""
    return 0

def event_m10_27_x28(z79=6000, z80=0, z81=127000030, z82=0, z83=0, z84=4004000):
    """[Lib] Character: Petrified: Appearance setting
    z79: Generator ID
    z80: Death: Global event flag
    z81: Petrified: Area and other flags
    z82: Petrified: Global event flag
    z83: Startup state
    z84: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z79)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z80, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z81, 1)
                CompareEventFlag(1, z82, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z79, z83)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()

def event_m10_27_x29(z78=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z78: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z78)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_27_x30():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x31(z76=_, z77=_):
    """[Lib] [execute] Rebirth fire
    z76: Flag start ID
    z77: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z76, z77, 0)
    """State 2: End state"""
    return 0

def event_m10_27_x32():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x33(z76=_, z77=_):
    """[Lib] [Preset] Rebirth
    z76: Flag start ID
    z77: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_27_x30()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_27_x32()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_27_x31(z76=z76, z77=z77)
    """State 4: End state"""
    return 0

def event_m10_27_x34(z74=127000030, z75=0, z73=2, z72=0, z71=6004020):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z74: Other flags
    z75: Global flag
    z73: Additional attributes
    z72: Delete attribute
    z71: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z74) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z75) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z71, z73)
        DeleteNavimeshAttribute(z71, z72)
        """State 3: Flag OFF"""
        return 0

def event_m10_27_x35(z74=127000030, z75=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z74: Other flags
    z75: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z74, 1)
    CompareEventFlag(0, z75, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_27_x36(z71=6004020, z72=0, z73=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z71: Navimesh switching point ID
    z72: Additional attributes
    z73: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z71, z72)
    DeleteNavimeshAttribute(z71, z73)
    """State 2: End state"""
    return 0

def event_m10_27_x37(z71=6004020, z72=0, z73=2, z74=127000030, z75=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z71: Navimesh switching point ID
    z72: Additional attributes
    z73: Delete attribute
    z74: Other flags
    z75: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_27_x34(z74=z74, z75=z75, z73=z73, z72=z72, z71=z71)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_27_x35(z74=z74, z75=z75)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_27_x36(z71=z71, z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m10_27_x38(z65=102810, z66=10000000, z67=600, z68=104340, z69=0, z70=0):
    """[Lib] NPC Black Phantom Appearance: Online
    z65: Summoning conditions: Global event flag
    z66: Summon range
    z67: Generator ID
    z68: Death: Global event flag
    z69: Appearance: Minimum time
    z70: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z68, 1)
        CompareEventFlag(8, z65, 1)
        IsPlayerInsidePoint(8, z66, z66, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z68, 1)
            CompareStateTime(1, z69, 3, z70)
            IsPlayerInsidePoint(2, z66, z66, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z67)
                HasNpcPhantomSpawned(0, z67, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_27_x39(z61=_, z62=_, z63=0, z64=_):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z61: Summon range
    z62: Generator ID
    z63: Appearance: Minimum time
    z64: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z61, z61, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z63, 3, z64)
        IsPlayerInsidePoint(1, z61, z61, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z62)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_27_x40(z56=102000, z57=606, z58=104000, z59=103500, z60=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z56: White Phantom can appear: Global event flag
    z57: White Phantom: Generator ID
    z58: Death: Global event flag
    z59: Hostile: Global event flag
    z60: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z57)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z58, 1)
        CompareEventFlag(1, z59, 1)
        CompareEventFlag(2, z56, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z57)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z58, 1)
            CompareEventFlag(1, z59, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z57)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z58, 1)
            CompareEventFlag(1, z59, 1)
            HasNpcPhantomSpawned(2, z57, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z57, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z57)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m10_27_x41(z55=10272700):
    """[Lib] [BEST] [Reproduction] Phantom management of Andyel
    z55: Ander OBJ instance ID
    """
    """State 0,1: Are you a guest?"""
    if IsGuest() != 1:
        pass
    else:
        """State 2: Has the Andyir appeared?"""
        if CompareObjStateId(z55, 20, 0):
            pass
        else:
            """State 3: The guests"""
            return 0
    """State 4: Finish"""
    return 1

def event_m10_27_x42(z55=10272700):
    """[Lib] [BEST] [Condition] Phantom management of Andyel
    z55: Ander OBJ instance ID
    """
    """State 0,1: OBJ active judgment"""
    IsObjActive(0, z55, 1)
    CompareObjState(1, z55, 20, 0)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Illusion"""
        return 0

def event_m10_27_x43(z55=10272700):
    """[Lib] [BEST] [Execution] Phantom management of Andyel
    z55: Ander OBJ instance ID
    """
    """State 0,2: Phantom processing"""
    SetObjPhantomParameters(z55, 15)
    """State 1: Next judgment"""
    IsObjActive(0, z55, 0)
    CompareObjState(0, z55, 20, 0)
    assert ConditionGroup(0)
    """State 3: Illusion"""
    return 0

def event_m10_27_x44(z55=10272700):
    """[Lib] [BEST] [Preset] Phantom management of Andyel
    z55: Ander OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Phantom management of Andy _SubState"""
    call = event_m10_27_x41(z55=z55)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [BEST] [Condition] Phantom management of Andy_SubState"""
        call = event_m10_27_x42(z55=z55)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Lib] [BEST] [Execution] Phantom management of Andy_SubState"""
            assert event_m10_27_x43(z55=z55)
            """State 5: Rerun"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_27_x45(z53=10272700, z54=10270655):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z53: Ander OBJ instance ID
    z54: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z53, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z54, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_27_x46(z53=10272700):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z53: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z53, 10, 0)
    CompareObjState(0, z53, 31, 0)
    CompareObjState(0, z53, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_27_x47(z53=10272700, z54=10270655):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z53: Ander OBJ instance ID
    z54: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z54, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z53, 10, 1)
    CompareObjState(8, z53, 31, 1)
    CompareObjState(8, z53, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_27_x48(z53=10272700, z54=10270655):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z53: Ander OBJ instance ID
    z54: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z54, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z53, 10, 0)
    CompareObjState(0, z53, 31, 0)
    CompareObjState(0, z53, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_27_x49(z53=10272700, z54=10270655):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z53: Ander OBJ instance ID
    z54: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_27_x45(z53=z53, z54=z54)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_27_x46(z53=z53)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_27_x47(z53=z53, z54=z54)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_27_x48(z53=z53, z54=z54)
    """State 6: Rerun"""
    return 1

def event_m10_27_x50(z51=10272700, z52=10270655):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z51: Ander OBJ instance ID
    z52: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z51, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z52, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_27_x51(z51=10272700):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z51: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z51, 10, 0)
    CompareObjState(0, z51, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_27_x52(z51=10272700, z52=10270655):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z51: Ander OBJ instance ID
    z52: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z52, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z51, 10, 1)
    CompareObjState(8, z51, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_27_x53(z51=10272700, z52=10270655):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z51: Ander OBJ instance ID
    z52: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z52, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z51, 10, 0)
    CompareObjState(0, z51, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_27_x54(z51=10272700, z52=10270655):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z51: Ander OBJ instance ID
    z52: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_27_x50(z51=z51, z52=z52)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_27_x51(z51=z51)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_27_x52(z51=z51, z52=z52)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_27_x53(z51=z51, z52=z52)
    """State 5: Rerun"""
    return 0

def event_m10_27_x55(z45=10272700, z46=100747, z48=100765, z47=100748, z49=100745, z50=10270655):
    """[Lib] [BEST] [Reproduction] Andyel_Appearance Judgment_2
    z45: Ander OBJ instance ID
    z46: Event completion flag
    z48: Conversation start flag
    z47: Encounter flag
    z49: Last encounter determination flag
    z50: Bonfire OBJ instance ID
    """
    """State 0,1: Has the event been completed?"""
    if GetEventFlag(z46) != 0:
        pass
    else:
        Goto('L0')
    """State 7: Finish"""
    return 0
    """State 2: Was it in conversation?"""
    Label('L0')
    if GetEventFlag(z48) != 0:
        pass
    else:
        """State 3: Was it in the middle of appearance?"""
        if CompareObjStateId(z45, 72, 0):
            """State 4: Wait for completion"""
            Label('L1')
            assert CompareObjStateId(z45, 30, 0)
            """State 5: Conversation start flag ON"""
            SetEventFlag(z48, 1)
        elif CompareObjStateId(z45, 73, 0):
            Goto('L1')
        elif CompareObjStateId(z45, 70, 0):
            Goto('L1')
        elif CompareObjStateId(z45, 30, 0):
            Goto('L1')
        else:
            """State 6: Is it in game?"""
            assert InGame() != 0
            """State 9: Appearance determination"""
            return 2
    """State 8: Disappearance judgment"""
    return 1

def event_m10_27_x56(z49=100745, z50=10270655):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_2
    z49: Last encounter determination flag
    z50: Bonfire OBJ instance ID
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z49, 1)
    IsObjActive(8, z50, 1)
    CompareEventFlag(9, z49, 1)
    IsObjActive(9, z50, 1)
    CompareObjState(9, z50, 30, 0)
    if ConditionGroup(9):
        """State 3: Ignited"""
        return 1
    elif ConditionGroup(8):
        """State 2: Waiting for ignition"""
        return 0

def event_m10_27_x57(z45=10272700):
    """[Lib] [BEST] [Execution] Andyel_Appearance determination_2
    z45: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z45, 31)
    """State 2: End state"""
    return 0

def event_m10_27_x58():
    """[Lib] [BEST] [Reproduction] Andiel_Appearance_2"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x59(z45=10272700):
    """[Lib] [BEST] [Condition] Andyel_Appearance_2
    z45: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z45)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x60(z45=10272700, z48=100765, z47=100748):
    """[Lib] [BEST] [Execution] Andyel_Appearance_2
    z45: Ander OBJ instance ID
    z48: Conversation start flag
    z47: Encounter flag
    """
    """State 0,7: Host?"""
    if IsGuest() != 1:
        """State 4: Bonfire light action"""
        PlayerActionRequest(5)
        assert PlayerIsInEventAction(5) != 0
    else:
        pass
    """State 5: Wait for action to finish"""
    CompareStateTime(8, 1.5, 2, 1.5)
    IsHost(8, 1, 0)
    IsPlayerPlayingMotion(9, 5, 0)
    IsHost(9, 1, 0)
    if ConditionGroup(9):
        """State 9: Rerun"""
        return 1
    elif ConditionGroup(8):
        """State 6: Andel encounter flag ON"""
        SetEventFlag(z47, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z45, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z45, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(z48, 1)
        """State 8: End state"""
        return 0

def event_m10_27_x61():
    """[Lib] [BEST] [Reproduction] Anderel_Deletion Judgment_2"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x62(z46=100747):
    """[Lib] [BEST] [Conditions] Anderel_Deletion Judgment_2 or later
    z46: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, z46, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x63(z45=10272700):
    """[Lib] [BEST] [Execution] Andel_Deletion Judgment_2 or later
    z45: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z45, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z45, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_27_x64(z45=10272700, z46=100747, z47=100748, z48=100765, z49=100745, z50=10270655):
    """[Lib] [BEST] [Preset] Andyel_2 or later
    z45: Ander OBJ instance ID
    z46: Event completion flag
    z47: Encounter flag
    z48: Conversation start flag
    z49: Last encounter determination flag
    z50: Bonfire OBJ instance ID
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Andiel_Appearance determination_2 and subsequent times_SubState"""
    call = event_m10_27_x55(z45=z45, z46=z46, z48=z48, z47=z47, z49=z49, z50=z50)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation determination _ 2nd and later _SubState"""
        Label('L0')
        assert event_m10_27_x61()
        """State 9: [Lib] [BEST] [Condition] Ander _ annihilation judgment _ 2nd and later _SubState"""
        assert event_m10_27_x62(z46=z46)
        """State 6: [Lib] [BEST] [Execution] Ander _ disappearance determination _ 2nd and later _SubState"""
        assert event_m10_27_x63(z45=z45)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Andyel_Appearance determination_2 and subsequent times_SubState"""
        call = event_m10_27_x56(z49=z49, z50=z50)
        if call.Get() == 1:
            """State 10: [Lib] [BEST] [Execution] Andel _ Appearance determination _ 2nd or later _ Ignition completed _SubState"""
            assert event_m10_27_x65(z45=z45, z48=z48)
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Anderl_Appearance determination_2 and subsequent times_SubState"""
            assert event_m10_27_x57(z45=z45)
            """State 1: [Lib] [BEST] [Reproduction] Andiel _ Appearance _ 2nd and later _SubState"""
            assert event_m10_27_x58()
            """State 7: [Lib] [BEST] [Conditions] Andyel_Appearance_2 and later _SubState"""
            assert event_m10_27_x59(z45=z45)
            """State 4: [Lib] [BEST] [Execution] Andyel_Appearance_2 and subsequent times_SubState"""
            call = event_m10_27_x60(z45=z45, z48=z48, z47=z47)
            if call.Get() == 1:
                """State 12: Rerun"""
                return 1
            elif call.Get() == 0:
                Goto('L0')
    """State 11: Finish"""
    return 0

def event_m10_27_x65(z45=10272700, z48=100765):
    """[Lib] [BEST] [Execution] Andiel _ Appearance determination _ 2nd and later _ Ignited
    z45: Ander OBJ instance ID
    z48: Conversation start flag
    """
    """State 0,1: Andyle waiting state: 30"""
    ChangeObjState(z45, 30)
    """State 3: Waiting for waiting"""
    CompareObjState(0, z45, 30, 0)
    assert ConditionGroup(0)
    """State 2: Host?"""
    if IsGuest() != 1:
        """State 4: Conversation start flag ON"""
        SetEventFlag(z48, 1)
    else:
        pass
    """State 5: Guest waiting"""
    SetConditionGroupTrue(0)
    assert HostConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_27_x66(z30=127020040, z32=127000041):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z30: Lottery determination flag
    z32: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z32) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z30) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_27_x67(z31=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z31: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z31, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_27_x68(z30=127020040, z33=3, z34=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z30: Lottery determination flag
    z33: Number of appearance judgment points
    z34: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z30, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z33)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z34, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_27_x69(z30=127020040, z31=14, z32=127000041, z33=3, z34=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z30: Lottery determination flag
    z31: Random number comparison value
    z32: Defeat flag
    z33: Number of appearance judgment points
    z34: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_27_x66(z30=z30, z32=z32)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_27_x67(z31=z31)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_27_x68(z30=z30, z33=z33, z34=z34)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_27_x78(z30=z30, z34=z34)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_27_x70(val1=_, z42=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z42: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z42) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_27_x71(z38=_, z39=0, z40=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z38: Appearance judgment point ID
    z39: Minimum appearance time
    z40: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z38, z38, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z39, 3, z40)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_27_x72(z41=950, z43=_, z44=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z41: Generator ID
    z43: Appearance start point ID
    z44: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z41, z43, z44)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z41)
    """State 4: Finish"""
    return 0

def event_m10_27_x73(z35=127000041):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z35: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z35) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_27_x74(z38=_, z39=0, z40=5, z41=950, val1=_, z42=10, z43=_, z44=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z38: Intrusion detection point ID
    z39: Minimum appearance time
    z40: Maximum time to appear
    z41: Generator ID
    val1: Appearance judgment number
    z42: Lottery result point variable
    z43: Appearance start point ID
    z44: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_27_x70(val1=val1, z42=z42)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_27_x71(z38=z38, z39=z39, z40=z40)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_27_x72(z41=z41, z43=z43, z44=z44)
    """State 4: Finish"""
    return 0

def event_m10_27_x75(z36=950, mode1=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z36: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z36)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_27_x76(z35=127000041, z37=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z35: Defeat flag
    z37: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z35, 1)
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
                    SetEventFlag(z37, 1)
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

def event_m10_27_x77(z35=127000041, z36=950, mode1=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z35: Defeat flag
    z36: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_27_x73(z35=z35)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_27_x75(z36=z36, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_27_x76(z35=z35, z37=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_27_x76(z35=z35, z37=102755)
    """State 5: End state"""
    return 0

def event_m10_27_x78(z30=127020040, z34=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z30: Lottery determination flag
    z34: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z30, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z34, 0)
    """State 3: End state"""
    return 0

def event_m10_27_x79():
    """[Lib] [DC] [Reproduction] Character _ Unlockable management _ Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x80(z26=_, z27=6, z28=1):
    """[Lib] [DC] [Condition] Character _ Unlockable management
    z26: Generator ID
    z27: Share flag
    z28: Comparison value
    """
    """State 0,1: State judgment"""
    CompareChrEzStateValue(0, z26, z27, z28, 1)
    CompareChrEzStateValue(1, z26, z27, z28, 0)
    if ConditionGroup(1):
        """State 3: Can lock"""
        return 1
    elif ConditionGroup(0):
        """State 2: Can't lock"""
        return 0

def event_m10_27_x81(z26=_, z27=6, z28=1, z29=170001000):
    """[Lib] [DC] [Execution] Character _ Unlockable management
    z26: Generator ID
    z27: Share flag
    z28: Comparison value
    z29: Special effect ID
    """
    """State 0,1: Grants a non-locking effect"""
    SetEnemySpEffect(z26, z29, 19, 4)
    """State 2: State judgment or character died?"""
    CompareChrEzStateValue(0, z26, z27, z28, 0)
    IsChrDead(0, z26)
    assert ConditionGroup(0)
    """State 3: Cancel lock disable effect"""
    ClearEnemySpEffect(z26, z29)
    """State 4: Finish"""
    return 0

def event_m10_27_x82(z26=_, z27=6, z28=1, z29=170001000):
    """[Lib] [DC] [Preset] Character _ Unlockable management
    z26: Generator ID
    z27: Share flag
    z28: Comparison value
    z29: Special effect ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Character _ Unlockable management _ Empty _SubState"""
    assert event_m10_27_x79()
    """State 3: [Lib] [DC] [Condition] Character_Unlockable_SubState"""
    call = event_m10_27_x80(z26=z26, z27=z27, z28=z28)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Lib] [DC] [Execution] Chara_Unlockable Management_SubState"""
        assert event_m10_27_x81(z26=z26, z27=z27, z28=z28, z29=z29)
    """State 4: Finish"""
    return 0

def event_m10_27_x83(z23=127000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z23: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z23) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_27_x84(z24=800):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z24: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z24, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x85(z25=127020083):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z25: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z25, 1)
    """State 2: End state"""
    return 0

def event_m10_27_x86(z23=127000081, z24=800, z25=127020083):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z23: Boss destruction flag
    z24: Boss generator ID
    z25: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_27_x83(z23=z23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_27_x84(z24=z24)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_27_x85(z25=z25)
    """State 4: End state"""
    return 0

def event_m10_27_x87():
    """[Reproduction] Wyvern in the middle to distant view"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x88():
    """[Condition] Wyvern in the middle to distant view_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x89(z22=_):
    """[Execution] Wyvern in the middle to distant view
    z22: Wyvern OBJ State ID
    """
    """State 0,1: OBJ state transition"""
    ChangeOwnObjState(z22)
    assert CompareOwnObjStateId(z22, 0)
    """State 2: End state"""
    return 0

def event_m10_27_x90(z22=_):
    """[Preset] Wyvern in the middle to distant view
    z22: Wyvern OBJ State ID
    """
    """State 0,2: [Reproduction] Wyvern in the middle to distant view_Sky_SubState"""
    assert event_m10_27_x87()
    """State 3: [Condition] Wyvern in the middle to distant view_Sky_SubState"""
    assert event_m10_27_x88()
    """State 1: [Execution] Wyvern in the middle to distant view_SubState"""
    assert event_m10_27_x89(z22=z22)
    """State 4: End state"""
    return 0

def event_m10_27_x91(z20=_, z21=_):
    """[Preset] Determining the number of eggs destroyed
    z20: Number of eggs destroyed
    z21: Flag ID to set
    """
    """State 0,1: [Reproduction] Determining the number of eggs destroyed_SubState"""
    assert event_m10_27_x92()
    """State 2: [Conditions] Determining the number of eggs destroyed_SubState"""
    assert event_m10_27_x93(z20=z20)
    """State 3: [Execution] Judgment number of egg destruction_SubState"""
    assert event_m10_27_x94(z21=z21)
    """State 4: End state"""
    return 0

def event_m10_27_x92():
    """[Reproduction] Determining the number of eggs destroyed"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x93(z20=_):
    """[Conditions] Judgment of number of egg destruction
    z20: Number of eggs destroyed
    """
    """State 0,1: Determining the number of eggs destroyed"""
    CompareObjBreakNum(0, 10273100, 10273399, z20, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x94(z21=_):
    """[Execution] Determining the number of eggs destroyed
    z21: Flag ID to set
    """
    """State 0,1: Set a flag to match the number of eggs destroyed"""
    SetEventFlag(z21, 1)
    """State 2: End state"""
    return 0

def event_m10_27_x95(z3=10271200, z4=10271800):
    """[Reproduction] Bridge break event activation judgment
    z3: Wyvern object instance ID
    z4: Bridge OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Is Wyvern OBJ in its initial state?"""
    if CompareObjStateId(z3, 10, 1):
        """State 3: Initialize Wyvern OBJ"""
        InitializeObj(z3)
        assert CompareObjStateId(z3, 10, 0)
    else:
        pass
    """State 4: Is the bridge OBJ in the initial state?"""
    if CompareObjStateId(z4, 10, 1):
        """State 5: Initialize the bridge OBJ"""
        InitializeObj(z4)
        assert CompareObjStateId(z4, 10, 0)
    else:
        pass
    """State 6: Host: Wait for event"""
    return 0
    """State 7: Guest: Exit"""
    Label('L0')
    return 1

def event_m10_27_x96(z3=10271200, z4=10271800, z7=10271210):
    """[Execution] Start judgment of bridge destruction event
    z3: Wyvern object instance ID
    z4: Bridge object instance ID
    z7: Wyvern OBJ instance ID across
    """
    """State 0,5: Auto save and menu prohibited"""
    DisableAutoSave(1)
    ProhibitInGameMenu(1)
    """State 1: Wyvern Bridge Lost: 74"""
    ChangeObjState(z3, 74)
    assert (GetStateTime() > 3.4) != 0
    """State 2: Bridge shaking timing: 70"""
    ChangeObjState(z4, 70)
    assert CompareObjStateId(z3, 20, 0) and CompareObjStateId(z4, 20, 0)
    """State 3: Finishing the bridge event"""
    StopCameraVibration()
    """State 6: Auto save and menu activation"""
    DisableAutoSave(0)
    ProhibitInGameMenu(0)
    """State 7: End state"""
    return 0

def event_m10_27_x97():
    """[Reproduction] White door management of old dragon"""
    """State 0,2: Turn on the white door control flag"""
    SetEventFlag(127000082, 1)
    """State 1: Has the old dragon been destroyed?"""
    if GetEventFlag(127000081) != 0:
        """State 4: Simple end"""
        return 1
    else:
        """State 3: End state"""
        return 0

def event_m10_27_x98():
    """[Condition] White door management of old dragon"""
    """State 0,1: Was it hostile to the ancient dragon?"""
    CompareEventFlag(0, 103970, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x99():
    """[Execution] White door management of old dragon"""
    """State 0,2: Set the white door control flag to OFF"""
    SetEventFlag(127000082, 0)
    """State 1: Did you destroy the ancient dragon?"""
    CompareEventFlag(0, 127000081, 1)
    assert ConditionGroup(0)
    """State 3: Turn on the white door control flag"""
    SetEventFlag(127000082, 1)
    """State 4: End state"""
    return 0

def event_m10_27_x100():
    """[Preset] Old Dragon White Door Management"""
    """State 0,1: [Reproduction] Old Dragon White Door Management_SubState"""
    call = event_m10_27_x97()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] White door management of old dragon_SubState"""
        assert event_m10_27_x98()
        """State 3: [Execution] White door management of old dragon_SubState"""
        assert event_m10_27_x99()
    """State 4: End state"""
    return 0

def event_m10_27_x101():
    """[Reproduction] Get the dragon egg"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x102(z18=10272600):
    """[Conditions] Obtain an old dragon egg
    z18: Old Dragon Egg OBJ Instance ID
    """
    """State 0,1: Got an old dragon egg?"""
    WasObjItemAcquired(0, z18, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x103(z19=100866):
    """[Execution] Get the dragon egg
    z19: Egg acquisition global event flag
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(z19, 1)
    """State 2: End state"""
    return 0

def event_m10_27_x104(z18=10272600, z19=100866):
    """[Preset] Get the dragon egg
    z18: Old Dragon Egg OBJ Instance ID
    z19: Egg acquisition global event flag
    """
    """State 0,1: [Reproduction] Obtaining an old dragon egg_Sky_SubState"""
    assert event_m10_27_x101()
    """State 3: [Condition] _SubState to get the dragon egg"""
    assert event_m10_27_x102(z18=z18)
    """State 2: [Execution] Get the dragon egg _SubState"""
    assert event_m10_27_x103(z19=z19)
    """State 4: End state"""
    return 0

def event_m10_27_x105(z10=_, z11=_, z12=_, z13=3, z14=10, z15=_, z16=_):
    """[Preset] Wyvern's attack power increases when breaking an egg
    z10: Wyvern generator ID that increases attack power
    z11: Egg OBJ destruction count_first instance ID
    z12: Determining the number of egg OBJ destruction_last instance ID
    z13: Egg OBJ destruction number 1
    z14: Egg OBJ destruction number 2 stage
    z15: Wyvern attack power UP flag 1st stage
    z16: Wyvern attack power UP flag 2nd stage
    """
    """State 0,1: [Reproduction] Wyvern attack power UP_SubState"""
    assert event_m10_27_x106()
    """State 2: [Condition] Wyvern's attack power UP_1 stage_SubState when egg is broken"""
    assert event_m10_27_x107(z11=z11, z12=z12, z13=z13)
    """State 3: [Execution] When the egg is broken, Wyvern's attack power UP_1 stage_SubState"""
    assert event_m10_27_x108(z15=z15, z10=z10, z17=92120010)
    """State 4: [Condition] When the egg is broken, the attack power of the Wyvern UP_2 stage_SubState"""
    assert event_m10_27_x107(z11=z11, z12=z12, z13=z14)
    """State 5: [Execution] When an egg is broken, Wyvern's attack power UP_2 stage_SubState"""
    assert event_m10_27_x108(z15=z16, z10=z10, z17=92120020)
    """State 6: End state"""
    return 0

def event_m10_27_x106():
    """[Reproduction] Wyvern's attack power increases when breaking an egg"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x107(z11=_, z12=_, z13=_):
    """[Condition] When the egg is broken, the attack power of the Wyvern increases.
    z11: Egg OBJ destruction count_first instance ID
    z12: Determining the number of egg OBJ destruction_last instance ID
    z13: Egg OBJ destruction number
    """
    """State 0,1: Egg destruction judgment"""
    CompareObjBreakNum(0, z11, z12, z13, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x108(z15=_, z10=_, z17=_):
    """[Execution] Increases attack power of Wyvern when breaking an egg
    z15: Wyvern attack power UP flag
    z10: Wyvern generator ID that increases attack power
    z17: Special effects
    """
    """State 0,2: Turn on the Wyvern attack power UP flag"""
    SetEventFlag(z15, 1)
    """State 1: Increase Wyvern's attack power"""
    SetEnemySpEffect(z10, z17, 19, 4)
    """State 3: End state"""
    return 0

def event_m10_27_x109(z8=_, z9=_):
    """[Preset] Old dragon warrior powers down with Wyvern subjugation
    z8: Wyvern generator ID
    z9: Power down flag
    """
    """State 0,1: [Reproduction] An old dragon warrior powers down at Wyvern subjugation_SubState"""
    assert event_m10_27_x110()
    """State 2: [Condition] The Wyvern subjugated the old dragon warrior power down_SubState"""
    assert event_m10_27_x111(z8=z8)
    """State 3: [Execution] Wyvern subjugated by the old dragon warrior power down_SubState"""
    assert event_m10_27_x112(z9=z9)
    """State 4: End state"""
    return 0

def event_m10_27_x110():
    """[Reproduction] Old dragon warrior powers down with Wyvern subjugation"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x111(z8=_):
    """[Conditions] Old dragon warrior powers down at Wyvern subjugation
    z8: Wyvern generator ID
    """
    """State 0,1: Wyvern status determination"""
    IsChrDead(0, z8)
    IsChrMaxRespawnCount(0, z8, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x112(z9=_):
    """[Execution] An old dragon warrior powers down on the Wyvern
    z9: Power down flag
    """
    """State 0,1: Turn on the power-down flag"""
    SetEventFlag(z9, 1)
    """State 2: End state"""
    return 0

def event_m10_27_x113(z5=300000):
    """[Condition] Judgment of bridge destruction event_Guest
    z5: Judgment point ID on bridge
    """
    """State 0,1: Point intrusion detection"""
    IsPlayerInsidePoint(0, z5, z5, 1)
    assert ConditionGroup(0)
    """State 4: End state"""
    StopCameraVibration()
    return 1

def event_m10_27_x114(z5=300000):
    """[Execution] Bridge break event activation judgment_Guest
    z5: Judgment point ID on bridge
    """
    """State 0,3: Shake the camera"""
    ShakeCameraAroundPoint(20000010, 10000, z5, 1)
    """State 1: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z5, z5, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    StopCameraVibration()
    return 1

def event_m10_27_x115(z5=300000, z6=300001):
    """[DC] [Condition] Judgment on start of bridge destruction event
    z5: Judgment point ID on bridge
    z6: Judgment point ID for whether you are in the Wyvern animation playback area
    """
    """State 0,1: Point intrusion detection"""
    IsPlayerInsidePoint(0, z5, z5, 1)
    assert ConditionGroup(0)
    """State 3: Shake the camera"""
    ShakeCameraAroundPoint(20000010, 10000, z5, 1)
    """State 2: Time judgment"""
    IsPlayerInsidePoint(8, z6, z6, 1)
    CompareStateTime(8, 12.5, 2, 12.5)
    IsPlayerInsidePoint(0, z5, z5, 0)
    if ConditionGroup(8):
        """State 4: In the area"""
        return 0
    elif ConditionGroup(0):
        """State 5: Outside the area"""
        StopCameraVibration()
        return 1

def event_m10_27_x116(z3=10271200, z4=10271800, z5=300000, z6=300001, z7=10271210):
    """[DC] [Preset] Judgment of bridge destruction event
    z3: Wyvern object instance ID
    z4: Bridge object instance ID
    z5: Judgment point ID on bridge
    z6: Judgment point ID for whether you are in the Wyvern animation playback area
    z7: Wyvern OBJ instance ID across
    """
    """State 0,1: [Reproduction] Bridge decision event activation judgment_SubState"""
    call = event_m10_27_x95(z3=z3, z4=z4)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        Goto('L0')
    """State 5: [DC] [Condition] Judgment of bridge destruction event_SubState"""
    call = event_m10_27_x115(z5=z5, z6=z6)
    if call.Get() == 0:
        """State 2: [Execution] Start determination of bridge destruction event_SubState"""
        assert event_m10_27_x96(z3=z3, z4=z4, z7=z7)
        """State 6: In area: End"""
        return 0
    elif call.Get() == 1:
        """State 7: Outside area: Re-execute"""
        return 1
    """State 4: [Condition] Judgment on start of bridge destruction event_Guest_SubState"""
    Label('L0')
    assert event_m10_27_x113(z5=z5)
    """State 3: [Execution] Start determination of bridge destruction event_Guest_SubState"""
    assert event_m10_27_x114(z5=z5)
    """State 8: Guest: Rerun"""
    return 2

def event_m10_27_x117():
    """[DC] [Reproduction] A guardian waits for the duel defeat"""
    """State 0,1: End state"""
    return 0

def event_m10_27_x118(z1=_):
    """[DC] [Condition] A guardian waits for the duel defeat
    z1: Generator ID
    """
    """State 0,1: Duel status determination"""
    IsChrDeadOrRespawnOver(0, z1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_27_x119(z2=_):
    """[DC] [execution] A guardian waits for the duel defeat
    z2: Defeat flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z2, 1)
    """State 2: End state"""
    return 0

def event_m10_27_x120(z1=_, z2=_):
    """[DC] [Preset] Guardian waits for defeat of duel
    z1: Generator ID
    z2: Defeat flag
    """
    """State 0,1: [DC] [Reproduction] Guardian waits for duel defeat _SubState"""
    assert event_m10_27_x117()
    """State 3: [DC] [Condition] A guardian waits for the duel defeat._SubState"""
    assert event_m10_27_x118(z1=z1)
    """State 2: [DC] [Execution] Guardian waits due to defeated duel_SubState"""
    assert event_m10_27_x119(z2=z2)
    """State 4: End state"""
    return 0

def event_m10_27_111015():
    """OBJ: Durahan: White phantom sign display"""
    """State 0,1: Appearance condition: Ancient Dragon"""
    CompareEventFlag(0, 103970, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m10_27_x40(z56=102000, z57=606, z58=104000, z59=103500, z60=-1)

def event_m10_27_111051():
    """OBJ: Dragon Maiden (Andiel's Hall): Approval for Appearance"""
    """State 0,1: Appearance permission: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Appearance permission: Death determination"""
        CompareEventFlag(0, 104020, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 5: Appearance permission: Judgment of generation stop"""
            CompareEventFlag(0, 102088, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 6: Appearance permission: Stop generation: Wait"""
                CompareEventFlag(0, 100977, 1)
                CompareEventFlag(1, 206600, 1)
                CompareEventFlag(2, 102088, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                elif ConditionGroup(2):
                    Goto('L0')
        """State 4: Appearance permission: Generation stop"""
        SetEventFlag(102088, 1)
        CompareEventFlag(0, 102088, 1)
        assert ConditionGroup(0)
        """State 7: Appearance permission: Character erasure"""
        DeleteEnemyByGeneratorGroup(60, 0)
    """State 2: Appearance permission: System: End"""
    Label('L0')
    EndMachine()

def event_m10_27_111052():
    """OBJ: Dragon Maiden (Invincible): Intrusion Judgment"""
    """State 0,1: [Lib] Map intrusion detection: General purpose_SubState"""
    event_m10_27_x18(z100=104020, z101=102087)

def event_m10_27_111053():
    """OBJ: Dragon Lady: Erasure"""
    """State 0,2: Erase: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 1: Erase: Judgment"""
    CompareEventFlag(0, 100977, 1)
    CompareEventFlag(1, 206600, 1)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        pass
    """State 3: Erase: Setting"""
    DeleteEnemyByGeneratorGroup(60, 0)
    """State 4: Erase: System: Exit"""
    EndMachine()

def event_m10_27_111435():
    """OBJ: Sealed Person: Black Phantom Appearance: Online"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_27_x38(z65=102810, z66=10000000, z67=600, z68=104340, z69=0, z70=0)

def event_m10_27_118140():
    """Multi-use NPC: Meat cut (female): White phantom sign display"""
    """State 0,1: Appearance determination"""
    CompareEventFlag(8, 104470, 1)
    CompareEventFlag(8, 103970, 1)
    assert ConditionGroup(8)
    """State 2: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_27_x29(z78=607)

def event_m10_27_118141():
    """Multi-use NPC: Small white: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_27_x29(z78=604)

def event_m10_27_118230():
    """Multi NPC: Old Dragon Swordsman (Male): Black Phantom Appearance: Online"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_27_x39(z61=10001000, z62=601, z63=0, z64=2)

def event_m10_27_118231():
    """Multi NPC: Edira: Black Phantom Appearance: Online"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_27_x39(z61=10002000, z62=608, z63=0, z64=0)

def event_m10_27_118232():
    """Multi NPC: Nest: Black Phantom Appearance: Online"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_27_x39(z61=10003000, z62=609, z63=0, z64=0)

def event_m10_27_4000000():
    """[BEST] Andel Appearance"""
    """State 0,3: [Lib] [BEST] [Preset] Andiel _ 2nd and later _SubState"""
    call = event_m10_27_x64(z45=10272700, z46=100747, z47=100748, z48=100765, z49=100745, z50=10270655)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_27_4001000():
    """[BEST] Phantom management of Andiel"""
    """State 0,3: [Lib] [BEST] [Preset] Phantom management of Andy_SubState"""
    call = event_m10_27_x44(z55=10272700)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_27_4002000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_27_x54(z51=10272700, z52=10270655)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_27_4003000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_27_x49(z53=10272700, z54=10270655)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_27_4004000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_27_x19(z92=6000, z93=0, z94=15, z95=127000030, z96=0, z97=1600, z98=6, z99=4004010)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4004010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_27_x28(z79=6000, z80=0, z81=127000030, z82=0, z83=0, z84=4004000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4004020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_27_x37(z71=6004020, z72=0, z73=2, z74=127000030, z75=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4005000():
    """[DC] Guardian waits due to defeated duel_1"""
    """State 0,2: [DC] [Preset] Waiter waits for duel defeat _SubState"""
    assert event_m10_27_x120(z1=2005, z2=127020025)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4005010():
    """[DC] Guardian waits due to defeated duel_2"""
    """State 0,2: [DC] [Preset] Waiter waits for duel defeat _SubState"""
    assert event_m10_27_x120(z1=2010, z2=127020026)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4005020():
    """[DC] Guardian waits for duel defeat _3"""
    """State 0,2: [DC] [Preset] Waiter waits for duel defeat _SubState"""
    assert event_m10_27_x120(z1=2030, z2=127020027)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4005030():
    """[DC] Guardian waits due to duel defeat_4"""
    """State 0,2: [DC] [Preset] Waiter waits for duel defeat _SubState"""
    assert event_m10_27_x120(z1=2033, z2=127020028)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4005040():
    """[DC] Guardian waits for duel defeat _5"""
    """State 0,2: [DC] [Preset] Waiter waits for duel defeat _SubState"""
    assert event_m10_27_x120(z1=608, z2=127020029)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4006000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_27_x69(z30=127020040, z31=14, z32=127000041, z33=3, z34=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_27_x74(z38=80000000, z39=0, z40=5, z41=950, val1=1, z42=10, z43=80000001, z44=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_27_x74(z38=80000100, z39=0, z40=5, z41=950, val1=2, z42=10, z43=80000101, z44=80000199)
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m10_27_x74(z38=80000200, z39=0, z40=5, z41=950, val1=3, z42=10, z43=80000201, z44=80000299)
        """State 2: Start flag ON"""
        SetEventFlag(127020042, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4006010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_27_x77(z35=127000041, z36=950, mode1=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007000():
    """[DC] Character _ Unlockable management_1"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=602, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007010():
    """[DC] Character _ Unlockable management_2"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=603, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007020():
    """[DC] Character _ Unlockable management_3"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4000, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007030():
    """[DC] Character _ Unlockable management_4"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4001, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007040():
    """[DC] Character _ Unlockable management_5"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4005, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007060():
    """[DC] Character _ Unlockable management _7"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4009, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007070():
    """[DC] Character _ Unlockable management_8"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4010, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007080():
    """[DC] Character _ Unlockable management _9"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4011, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007090():
    """[DC] Character _ Unlockable management_10"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4020, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007100():
    """[DC] Character _ Unlockable Management_11"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4030, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007110():
    """[DC] Character _ Unlockable management_12"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4031, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007120():
    """[DC] Character _ Unlockable Management_13"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4032, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007130():
    """[DC] Character _ Unlockable management_14"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4033, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007160():
    """[DC] Character_Unlockable Management_17"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4036, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007170():
    """[DC] Character _ Unlockable management_18"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4037, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007180():
    """[DC] Character _ Unlockable Management_19"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4038, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007190():
    """[DC] Character _ Unlockable management_20"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4039, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007200():
    """[DC] Character _ Unlockable Management_21"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4040, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007210():
    """[DC] Character _ Unlockable management_22"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4041, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4007220():
    """[DC] Character _ Unlockable Management_23"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_27_x82(z26=4042, z27=6, z28=1, z29=170001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_27_4031000():
    """[DC] NPC White Spirit_Gesture Management_Old Dragon"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_27_x86(z23=127000081, z24=800, z25=127020083)
    """State 1: Finish"""
    EndMachine()

