# -*- coding: utf-8 -*-
def event_m20_26_1000():
    """Ancient Dragon memory time limit"""
    """State 0,2: [Preset] Time limit of memory of old dragon_SubState"""
    # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
    assert (event_m20_26_x5(z3=1, z4=226010001, val1=150, val2=290, z5=300, action1=2012, action2=2013,
            z6=900000))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_26_2000():
    """Warp to Geldra"""
    """State 0,2: [Preset] Warp _SubState to Geldra"""
    # lot:60005000:Ancient Dragon Soul, goods:64230000:Ancient Dragon Soul
    assert event_m20_26_x0(z1=20261000, lot1=60005000, flag1=226000020, z2=1, goods1=64230000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_26_x0(z1=20261000, lot1=60005000, flag1=226000020, z2=1, goods1=64230000):
    """[Preset] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    lot1: Lottery ID for item acquisition
    flag1: Item acquisition confirmation flag
    z2: Global timer ID
    goods1: Acquisition judgment item ID
    """
    """State 0,4: [Reproduction] Warp to Subway_SubState"""
    call = event_m20_26_x4(z1=z1, flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: [Condition] Warp_SubState to Geldra"""
    assert event_m20_26_x1(z1=z1, goods1=0)
    """State 3: [Execution] Warp_SubState to Geldra"""
    assert event_m20_26_x2(z1=z1, z2=z2)
    """State 8: End state"""
    return 0
    """State 2: [Condition] Warp to Jedra_Item Acquisition_SubState"""
    Label('L0')
    call = event_m20_26_x1(z1=z1, goods1=goods1)
    if call.Get() == 0:
        """State 6: [Execution] Warp to Gerdra_Item acquisition_SubState"""
        assert event_m20_26_x3(z1=z1, lot1=lot1, flag1=flag1)
    elif call.Get() == 1:
        """State 7: [Execution] Warp to Geldra_Items cannot be acquired_SubState"""
        assert event_m20_26_x11(z1=z1, lot1=lot1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_26_x1(z1=20261000, goods1=_):
    """[Condition] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    goods1: Item ID
    """
    """State 0,1: Have you examined OBJ?"""
    IsObjSearched(0, z1)
    assert ConditionGroup(0)
    """State 2: Can you get an old dragon soul?"""
    if CanGetItem(goods1, 1) != 0:
        """State 3: Available"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m20_26_x2(z1=20261000, z2=1):
    """[Execution] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    z2: Global timer ID
    """
    """State 0,2: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 3: Wait for transition completion"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 1: Warp to Geldra"""
    EndGlobalTimer(z2)
    PlayCutsceneAndWarpToMap(0, 0, 10140000, 900000, 0)
    """State 4: End state"""
    return 0

def event_m20_26_x3(z1=20261000, lot1=60005000, flag1=226000020):
    """[Execution] Warp to Jedra_Item acquisition
    z1: Instance ID of the ancient dragon OBJ
    lot1: Lottery ID for item acquisition
    flag1: Item acquisition confirmation flag
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60005000:Ancient Dragon Soul
    AwardItem(lot1, 1)
    """State 4: Turn on the item acquisition flag"""
    SetEventFlag(flag1, 1)
    SetEventFlag(100905, 1)
    """State 5: End state"""
    return 0

def event_m20_26_x4(z1=20261000, flag1=226000020):
    """[Reproduction] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    flag1: Item acquisition confirmation flag
    """
    """State 0,2: Key guide activation: 30"""
    ChangeObjState(z1, 30)
    """State 3: Wait for transition"""
    assert CompareObjStateId(z1, 30, 0)
    """State 1: Did you get the item?"""
    if GetEventFlag(flag1) != 0:
        """State 5: It has been acquired"""
        return 1
    else:
        """State 4: Unacquired"""
        return 0

def event_m20_26_x5(z3=1, z4=226010001, val1=150, val2=290, z5=300, action1=2012, action2=2013, z6=900000):
    """[Preset] Memory time limit for ancient dragons
    z3: Global timer ID
    z4: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    z5: Execution start time of the third phase process
    action1: Text ID to display in the first phase
    action2: Text ID to display in the third phase
    z6: Return Warp Point ID
    """
    """State 0,1: [Reproduction] Time limit of memory of ancient dragon_SubState"""
    call = event_m20_26_x6(z3=z3, z4=z4, val1=val1, val2=val2)
    if call.Get() == 3:
        """State 8: [Conditions & Execution] Old Dragon Memory Time Limit_0th Phase_SubState"""
        # action:2011:"One cannot reside within memory for long"
        assert event_m20_26_x10(z3=z3, z7=5, action3=2011)
        """State 2: [Conditions & Execution] Old Dragon Memory Time Limit_First Phase_SubState"""
        assert event_m20_26_x7(z3=z3, val1=val1, action1=action1)
        """State 3: [Conditions & Execution] Old Dragon Memory Time Limit_Second Phase_SubState"""
        assert event_m20_26_x8(z3=z3, val2=val2, z4=z4)
        """State 4: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_SubState"""
        assert event_m20_26_x9(z3=z3, z5=z5, action2=action2, z6=z6)
    elif call.Get() == 0:
        """State 9: [Conditions & Execution] Old Dragon Memory Time Limit_First Phase_2_SubState"""
        assert event_m20_26_x7(z3=z3, val1=val1, action1=action1)
        """State 5: [Conditions & Execution] Old Dragon Memory Time Limit_Second Phase_2_SubState"""
        assert event_m20_26_x8(z3=z3, val2=val2, z4=z4)
        """State 6: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_2_SubState"""
        assert event_m20_26_x9(z3=z3, z5=z5, action2=action2, z6=z6)
    elif call.Get() == 1:
        """State 10: [Conditions & Execution] Old Dragon Memory Time Limit_Second Phase_3_SubState"""
        assert event_m20_26_x8(z3=z3, val2=val2, z4=z4)
        """State 7: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_3_SubState"""
        assert event_m20_26_x9(z3=z3, z5=z5, action2=action2, z6=z6)
    elif call.Get() == 2:
        """State 11: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_4_SubState"""
        assert event_m20_26_x9(z3=z3, z5=z5, action2=action2, z6=z6)
    """State 12: End state"""
    return 0

def event_m20_26_x6(z3=1, z4=226010001, val1=150, val2=290):
    """[Reproduction] Memory time limit of the ancient dragon
    z3: Global timer ID
    z4: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    """
    """State 0,1: Timer start judgment"""
    if (GetGlobalTimerTime(z3) > val2) != 0:
        """State 5: Restart global timer_3"""
        RestartGlobalTimer(z3)
        """State 6: Time limit notification flag ON"""
        SetEventFlag(z4, 1)
        """State 9: From the third phase"""
        return 2
    elif (GetGlobalTimerTime(z3) > val1) != 0:
        """State 4: Restart global timer_2"""
        RestartGlobalTimer(z3)
        """State 8: From the second phase"""
        return 1
    elif (GetGlobalTimerTime(z3) > 1) != 0:
        """State 3: Restart global timer"""
        RestartGlobalTimer(z3)
        """State 7: From the first phase"""
        return 0
    else:
        """State 2: Starting the global timer"""
        StartGlobalTimer(z3)
        """State 10: From the 0th phase"""
        return 3

def event_m20_26_x7(z3=1, val1=150, action1=2012):
    """[Conditions & Execution] Time limit of memory of old dragon _ 1st phase
    z3: Global timer ID
    val1: Execution start time of the first phase process
    action1: Text ID to display in the first phase
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z3, val1, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2012:"The ashen mist has thinned..."
    DisplayEventMessage(action1, 0, 0, 0)
    """State 3: End state"""
    return 0

def event_m20_26_x8(z3=1, val2=290, z4=226010001):
    """[Conditions & Execution] Time limit of memory of old dragon _ 2nd phase
    z3: Global timer ID
    val2: Execution start time of the second phase process
    z4: Time limit notification flag
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z3, val2, 3)
    assert ConditionGroup(0)
    """State 2: Time limit notification flag ON"""
    SetEventFlag(z4, 1)
    """State 3: End state"""
    return 0

def event_m20_26_x9(z3=1, z5=300, action2=2013, z6=900000):
    """[Conditions & Execution] Time limit of memory of old dragon _ 3rd phase
    z3: Global timer ID
    z5: Execution start time of the third phase process
    action2: Text ID to display in the third phase
    z6: Return Warp Point ID
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z3, z5, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2013:"The ashen mist fades..."
    DisplayEventMessage(action2, 0, 0, 0)
    """State 3: Return to Geldra"""
    EndGlobalTimer(z3)
    PlayCutsceneAndWarpToMap(0, 0, 10140000, z6, 0)
    """State 4: End state"""
    return 0

def event_m20_26_x10(z3=1, z7=5, action3=2011):
    """[Conditions & Execution] Time limit of memory of old dragon _ 0th phase
    z3: Global timer ID
    z7: Execution start time of the 0th phase process
    action3: Text ID displayed in the 0th phase
    """
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 3: Wait for a certain time"""
    CompareStateTime(0, z7, 3, z7)
    assert ConditionGroup(0)
    """State 1: Event message display"""
    # action:2011:"One cannot reside within memory for long"
    DisplayEventMessage(action3, 0, 0, 0)
    """State 4: End state"""
    return 0

def event_m20_26_x11(z1=20261000, lot1=60005000):
    """[Execution] Warp to Geldra_Item acquisition not possible
    z1: Instance ID of the ancient dragon OBJ
    lot1: Lottery ID for item acquisition
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: Acquisition failure window display"""
    # lot:60005000:Ancient Dragon Soul
    DisplayItemAwardFailure(lot1, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 4: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 5: End state"""
    return 0

