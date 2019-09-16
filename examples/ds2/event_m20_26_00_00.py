# -*- coding: utf-8 -*-
def event_m20_26_1000():
    """Ancient Dragon memory time limit"""
    """State 0,2: [Preset] Time limit of memory of old dragon_SubState"""
    # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
    assert (event_m20_26_x5(z4=1, z5=226010001, val1=150, val2=290, z6=300, action1=2012, action2=2013,
            z7=900000))
    """State 1: Finish"""
    EndMachine()

def event_m20_26_2000():
    """Warp to Geldra"""
    """State 0,2: [Preset] Warp _SubState to Geldra"""
    # lot:60005000:Ancient Dragon Soul, goods:64230000:Ancient Dragon Soul
    assert event_m20_26_x0(z1=20261000, lot1=60005000, z2=226000020, z3=1, goods1=64230000)
    """State 1: Finish"""
    EndMachine()

def event_m20_26_x0(z1=20261000, lot1=60005000, z2=226000020, z3=1, goods1=64230000):
    """[Preset] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    lot1: Lottery ID for item acquisition
    z2: Item acquisition confirmation flag
    z3: Global timer ID
    goods1: Acquisition judgment item ID
    """
    """State 0,4: [Reproduction] Warp to Subway_SubState"""
    call = event_m20_26_x4(z1=z1, z2=z2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: [Condition] Warp_SubState to Geldra"""
    assert event_m20_26_x1(z1=z1, goods1=0)
    """State 3: [Execution] Warp_SubState to Geldra"""
    assert event_m20_26_x2(z1=z1, z3=z3)
    """State 8: End state"""
    return 0
    """State 2: [Condition] Warp to Jedra_Item Acquisition_SubState"""
    Label('L0')
    call = event_m20_26_x1(z1=z1, goods1=goods1)
    if call.Get() == 0:
        """State 6: [Execution] Warp to Gerdra_Item acquisition_SubState"""
        assert event_m20_26_x3(z1=z1, lot1=lot1, z2=z2)
    elif call.Get() == 1:
        """State 7: [Execution] Warp to Geldra_Items cannot be acquired_SubState"""
        assert event_m20_26_x11(z1=z1, lot1=lot1)
    """State 1: Rerun"""
    RestartMachine()

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

def event_m20_26_x2(z1=20261000, z3=1):
    """[Execution] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    z3: Global timer ID
    """
    """State 0,2: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 3: Wait for transition completion"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 1: Warp to Geldra"""
    EndGlobalTimer(z3)
    PlayCutsceneAndWarpToMap(0, 0, 10140000, 900000, 0)
    """State 4: End state"""
    return 0

def event_m20_26_x3(z1=20261000, lot1=60005000, z2=226000020):
    """[Execution] Warp to Jedra_Item acquisition
    z1: Instance ID of the ancient dragon OBJ
    lot1: Lottery ID for item acquisition
    z2: Item acquisition confirmation flag
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
    SetEventFlag(z2, 1)
    SetEventFlag(100905, 1)
    """State 5: End state"""
    return 0

def event_m20_26_x4(z1=20261000, z2=226000020):
    """[Reproduction] Warp to Geldra
    z1: Instance ID of the ancient dragon OBJ
    z2: Item acquisition confirmation flag
    """
    """State 0,2: Key guide activation: 30"""
    ChangeObjState(z1, 30)
    """State 3: Wait for transition"""
    assert CompareObjStateId(z1, 30, 0)
    """State 1: Did you get the item?"""
    if GetEventFlag(z2) != 0:
        """State 5: It has been acquired"""
        return 1
    else:
        """State 4: Unacquired"""
        return 0

def event_m20_26_x5(z4=1, z5=226010001, val1=150, val2=290, z6=300, action1=2012, action2=2013, z7=900000):
    """[Preset] Memory time limit for ancient dragons
    z4: Global timer ID
    z5: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    z6: Execution start time of the third phase process
    action1: Text ID to display in the first phase
    action2: Text ID to display in the third phase
    z7: Return Warp Point ID
    """
    """State 0,1: [Reproduction] Time limit of memory of ancient dragon_SubState"""
    call = event_m20_26_x6(z4=z4, z5=z5, val1=val1, val2=val2)
    if call.Get() == 3:
        """State 8: [Conditions & Execution] Old Dragon Memory Time Limit_0th Phase_SubState"""
        # action:2011:"One cannot reside within memory for long"
        assert event_m20_26_x10(z4=z4, z8=5, action3=2011)
        """State 2: [Conditions & Execution] Old Dragon Memory Time Limit_First Phase_SubState"""
        assert event_m20_26_x7(z4=z4, val1=val1, action1=action1)
        """State 3: [Conditions & Execution] Old Dragon Memory Time Limit_Second Phase_SubState"""
        assert event_m20_26_x8(z4=z4, val2=val2, z5=z5)
        """State 4: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_SubState"""
        assert event_m20_26_x9(z4=z4, z6=z6, action2=action2, z7=z7)
    elif call.Get() == 0:
        """State 9: [Conditions & Execution] Old Dragon Memory Time Limit_First Phase_2_SubState"""
        assert event_m20_26_x7(z4=z4, val1=val1, action1=action1)
        """State 5: [Conditions & Execution] Old Dragon Memory Time Limit_Second Phase_2_SubState"""
        assert event_m20_26_x8(z4=z4, val2=val2, z5=z5)
        """State 6: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_2_SubState"""
        assert event_m20_26_x9(z4=z4, z6=z6, action2=action2, z7=z7)
    elif call.Get() == 1:
        """State 10: [Conditions & Execution] Old Dragon Memory Time Limit_Second Phase_3_SubState"""
        assert event_m20_26_x8(z4=z4, val2=val2, z5=z5)
        """State 7: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_3_SubState"""
        assert event_m20_26_x9(z4=z4, z6=z6, action2=action2, z7=z7)
    elif call.Get() == 2:
        """State 11: [Conditions & Execution] Old Dragon Memory Time Limit_3rd Phase_4_SubState"""
        assert event_m20_26_x9(z4=z4, z6=z6, action2=action2, z7=z7)
    """State 12: End state"""
    return 0

def event_m20_26_x6(z4=1, z5=226010001, val1=150, val2=290):
    """[Reproduction] Memory time limit of the ancient dragon
    z4: Global timer ID
    z5: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    """
    """State 0,1: Timer start judgment"""
    if (GetGlobalTimerTime(z4) > val2) != 0:
        """State 5: Restart global timer_3"""
        RestartGlobalTimer(z4)
        """State 6: Time limit notification flag ON"""
        SetEventFlag(z5, 1)
        """State 9: From the third phase"""
        return 2
    elif (GetGlobalTimerTime(z4) > val1) != 0:
        """State 4: Restart global timer_2"""
        RestartGlobalTimer(z4)
        """State 8: From the second phase"""
        return 1
    elif (GetGlobalTimerTime(z4) > 1) != 0:
        """State 3: Restart global timer"""
        RestartGlobalTimer(z4)
        """State 7: From the first phase"""
        return 0
    else:
        """State 2: Starting the global timer"""
        StartGlobalTimer(z4)
        """State 10: From the 0th phase"""
        return 3

def event_m20_26_x7(z4=1, val1=150, action1=2012):
    """[Conditions & Execution] Time limit of memory of old dragon _ 1st phase
    z4: Global timer ID
    val1: Execution start time of the first phase process
    action1: Text ID to display in the first phase
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z4, val1, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2012:"The ashen mist has thinned..."
    DisplayEventMessage(action1, 0, 0, 0)
    """State 3: End state"""
    return 0

def event_m20_26_x8(z4=1, val2=290, z5=226010001):
    """[Conditions & Execution] Time limit of memory of old dragon _ 2nd phase
    z4: Global timer ID
    val2: Execution start time of the second phase process
    z5: Time limit notification flag
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z4, val2, 3)
    assert ConditionGroup(0)
    """State 2: Time limit notification flag ON"""
    SetEventFlag(z5, 1)
    """State 3: End state"""
    return 0

def event_m20_26_x9(z4=1, z6=300, action2=2013, z7=900000):
    """[Conditions & Execution] Time limit of memory of old dragon _ 3rd phase
    z4: Global timer ID
    z6: Execution start time of the third phase process
    action2: Text ID to display in the third phase
    z7: Return Warp Point ID
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z4, z6, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2013:"The ashen mist fades..."
    DisplayEventMessage(action2, 0, 0, 0)
    """State 3: Return to Geldra"""
    EndGlobalTimer(z4)
    PlayCutsceneAndWarpToMap(0, 0, 10140000, z7, 0)
    """State 4: End state"""
    return 0

def event_m20_26_x10(z4=1, z8=5, action3=2011):
    """[Conditions & Execution] Time limit of memory of old dragon _ 0th phase
    z4: Global timer ID
    z8: Execution start time of the 0th phase process
    action3: Text ID displayed in the 0th phase
    """
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 3: Wait for a certain time"""
    CompareStateTime(0, z8, 3, z8)
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

