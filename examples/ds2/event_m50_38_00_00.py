# -*- coding: utf-8 -*-
def event_m50_38_51000():
    """Return to immortality_point or attack"""
    """State 0,2: [Preset] Return to Immortality_Point or Attack_SubState"""
    # action:2013:"The ashen mist fades..."
    assert event_m50_38_x4(z7=5100000, z8=63, action5=2013, z9=5000000, val3=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_38_52000():
    """Return to immortality_time limit"""
    """State 0,2: [Preset] Return to immortality_Time limit_SubState"""
    # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
    assert (event_m50_38_x5(z2=3, z3=538010001, val1=570, val2=590, z4=600, action2=2012, action3=2013,
            z5=5000000))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_38_53000():
    """Return to immortality_End of quest"""
    """State 0,2: [Preset] Return to Immortality_End of Quest_SubState"""
    # action:2013:"The ashen mist fades..."
    assert event_m50_38_x12(action1=2013, z1=5000000, mode1=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_38_100000():
    """Poly play"""
    """State 0: Start state"""
    assert GetEventFlag(538010110) != 0
    """State 3: [Lib] Normal poly play_SubState"""
    assert event_m50_38_x0(z10=503810, mode2=0, flag1=538020102, z11=1, z12=1)
    """State 2: Poly play end"""
    SetEventFlag(538010110, 0)
    assert GetEventFlag(538010110) != 1
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_38_x0(z10=503810, mode2=0, flag1=538020102, z11=1, z12=1):
    """[Lib] Normal poly play
    z10: Poly play ID
    mode2: Destination point ID after poly play
    flag1: Poly drama played flag
    z11: End fade
    z12: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(flag1) != 1:
        """State 1: Poly play"""
        PlayCutscene(z10, z11, z12)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((mode2 > 1) != 0, mode2)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((mode2 > 1) != 0, mode2)
    SetEventFlag(flag1, 1)
    """State 7: End state"""
    return 0

def event_m50_38_x1():
    """[Reproduction] Return to immortality _ point or attack"""
    """State 0,1: End state"""
    return 0

def event_m50_38_x2(z7=5100000, z8=63):
    """[Condition] Return to immortality _ point or attack
    z7: Point ID
    z8: Van clad attacks
    """
    """State 0,1: Did you satisfy the return condition?"""
    IsPlayerInsidePoint(0, z7, z7, 1)
    CompareEventFlagValue(0, 1, z8, 1, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_38_x3(action1=2013, z1=5000000, mode1=_):
    """[Execution] Return to Immortality_Point or Attack
    action1: Text ID to display in the third phase
    z1: Return Warp Point ID
    mode1: Time from message display to warp
    """
    """State 0,1: Event message display"""
    # action:2013:"The ashen mist fades..."
    DisplayEventMessage(action1, 0, 0, 0)
    """State 3: Time adjustment state"""
    assert (GetStateTime() > mode1) != 0
    """State 2: Return to immortality"""
    PlayCutsceneAndWarpToMap(0, 0, 20240000, z1, 0)
    """State 4: End state"""
    return 0

def event_m50_38_x4(z7=5100000, z8=63, action5=2013, z9=5000000, val3=1.5):
    """[Preset] Return to Immortality_Point or Attack
    z7: Point ID
    z8: Van clad attacks
    action5: Text ID to display
    z9: Return Warp Point ID
    val3: Time from message display to warp
    """
    """State 0,1: [Reproduction] Return to Immortality_Point or Attack_SubState"""
    assert event_m50_38_x1()
    """State 2: [Condition] Return to immortality_Point or attack_SubState"""
    assert event_m50_38_x2(z7=z7, z8=z8)
    """State 3: [Execution] Return to Immortality_Point or Attack_SubState"""
    assert event_m50_38_x3(action1=action5, z1=z9, mode1=val3)
    """State 4: End state"""
    return 0

def event_m50_38_x5(z2=3, z3=538010001, val1=570, val2=590, z4=600, action2=2012, action3=2013, z5=5000000):
    """[Preset] Return to Immortality_Time limit
    z2: Global timer ID
    z3: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    z4: Execution start time of the third phase process
    action2: Text ID to display in the first phase
    action3: Text ID to display in the third phase
    z5: Return Warp Point ID
    """
    """State 0,1: [Reproduction] Return to immortality_Time limit_SubState"""
    call = event_m50_38_x6(z2=z2, z3=z3, val1=val1, val2=val2)
    if call.Get() == 3:
        """State 8: [Conditions & Execution] Return to immortality_Time limit_0th phase_SubState"""
        # action:2011:"One cannot reside within memory for long"
        assert event_m50_38_x10(z2=z2, z6=5, action4=2011)
        """State 2: [Conditions & Execution] Return to Immortality_Time Limit_First Phase_SubState"""
        assert event_m50_38_x7(z2=z2, val1=val1, action2=action2)
        """State 3: [Conditions & Execution] Return to Immortality_Time Limit_Second Phase_SubState"""
        assert event_m50_38_x8(z2=z2, val2=val2, z3=z3)
        """State 4: [Conditions & Execution] Return to immortality_Time limit_3rd phase_SubState"""
        assert event_m50_38_x9(z2=z2, z4=z4, action3=action3, z5=z5)
    elif call.Get() == 0:
        """State 9: [Conditions & Execution] Return to Immortality_Time Limit_First Phase_2_SubState"""
        assert event_m50_38_x7(z2=z2, val1=val1, action2=action2)
        """State 5: [Conditions & Execution] Return to Immortality_Time Limit_Second Phase_2_SubState"""
        assert event_m50_38_x8(z2=z2, val2=val2, z3=z3)
        """State 6: [Conditions & Execution] Return to immortality_Time limit_3rd phase_2_SubState"""
        assert event_m50_38_x9(z2=z2, z4=z4, action3=action3, z5=z5)
    elif call.Get() == 1:
        """State 10: [Conditions & Execution] Return to immortality_Time limit_Second phase_3_SubState"""
        assert event_m50_38_x8(z2=z2, val2=val2, z3=z3)
        """State 7: [Conditions & Execution] Return to immortality_Time limit_3rd phase_3_SubState"""
        assert event_m50_38_x9(z2=z2, z4=z4, action3=action3, z5=z5)
    elif call.Get() == 2:
        """State 11: [Conditions & Execution] Return to immortality_Time limit_3rd phase_4_SubState"""
        assert event_m50_38_x9(z2=z2, z4=z4, action3=action3, z5=z5)
    """State 12: End state"""
    return 0

def event_m50_38_x6(z2=3, z3=538010001, val1=570, val2=590):
    """[Reproduction] Return to immortality_Time limit
    z2: Global timer ID
    z3: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    """
    """State 0,1: Timer start judgment"""
    if (GetGlobalTimerTime(z2) > val2) != 0:
        """State 5: Restart global timer_3"""
        RestartGlobalTimer(z2)
        """State 6: Time limit notification flag ON"""
        SetEventFlag(z3, 1)
        """State 9: From the third phase"""
        return 2
    elif (GetGlobalTimerTime(z2) > val1) != 0:
        """State 4: Restart global timer_2"""
        RestartGlobalTimer(z2)
        """State 8: From the second phase"""
        return 1
    elif (GetGlobalTimerTime(z2) > 1) != 0:
        """State 3: Restart global timer"""
        RestartGlobalTimer(z2)
        """State 7: From the first phase"""
        return 0
    else:
        """State 2: Starting the global timer"""
        StartGlobalTimer(z2)
        """State 10: From the 0th phase"""
        return 3

def event_m50_38_x7(z2=3, val1=570, action2=2012):
    """[Conditions & Execution] Return to immortality_Time limit_First phase
    z2: Global timer ID
    val1: Execution start time of the first phase process
    action2: Text ID to display in the first phase
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z2, val1, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2012:"The ashen mist has thinned..."
    DisplayEventMessage(action2, 0, 0, 0)
    """State 3: End state"""
    return 0

def event_m50_38_x8(z2=3, val2=590, z3=538010001):
    """[Conditions & Execution] Return to immortality_Time limit_Second phase
    z2: Global timer ID
    val2: Execution start time of the second phase process
    z3: Time limit notification flag
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z2, val2, 3)
    assert ConditionGroup(0)
    """State 2: Time limit notification flag ON"""
    SetEventFlag(z3, 1)
    """State 3: End state"""
    return 0

def event_m50_38_x9(z2=3, z4=600, action3=2013, z5=5000000):
    """[Conditions & Execution] Return to immortality_Time limit_3rd phase
    z2: Global timer ID
    z4: Execution start time of the third phase process
    action3: Text ID to display in the third phase
    z5: Return Warp Point ID
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z2, z4, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2013:"The ashen mist fades..."
    DisplayEventMessage(action3, 0, 0, 0)
    """State 4: Time adjustment state"""
    assert (GetStateTime() > 1) != 0
    """State 3: Return to immortality"""
    PlayCutsceneAndWarpToMap(0, 0, 20240000, z5, 0)
    """State 5: End state"""
    return 0

def event_m50_38_x10(z2=3, z6=5, action4=2011):
    """[Conditions & Execution] Return to immortality_Time limit_Phase 0
    z2: Global timer ID
    z6: Execution start time of the 0th phase process
    action4: Text ID displayed in the 0th phase
    """
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 3: Wait for a certain time"""
    CompareStateTime(0, z6, 3, z6)
    assert ConditionGroup(0)
    """State 1: Event message display"""
    # action:2011:"One cannot reside within memory for long"
    DisplayEventMessage(action4, 0, 0, 0)
    """State 4: End state"""
    return 0

def event_m50_38_x11():
    """[Condition] Return to immortality_End of quest"""
    """State 0,1: Is the quest end flag set?"""
    CompareEventFlag(0, 103200, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_38_x12(action1=2013, z1=5000000, mode1=1):
    """[Preset] Return to Immortality_End of quest
    action1: Text ID to display
    z1: Return Warp Point ID
    mode1: Time from message display to warp
    """
    """State 0,1: [Reproduction] Return to Immortality_Point or Attack_SubState"""
    assert event_m50_38_x1()
    """State 3: [Condition] Return to immortality_End of quest_SubState"""
    assert event_m50_38_x11()
    """State 2: [Execution] Return to Immortality_Point or Attack_SubState"""
    assert event_m50_38_x3(action1=action1, z1=z1, mode1=mode1)
    """State 4: End state"""
    return 0

