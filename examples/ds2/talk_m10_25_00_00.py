# -*- coding: utf-8 -*-
def talk_m10_25_7250():
    """Shenzhen Pilgrim (Kuz bottom)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_25_x9(z51=103621, z52=104120, z53=125020101)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m10_25_x3(text8=72509200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_25_x6(z49=125020102, text15=72509500, text16=72509500, z50=72509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 11: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m10_25_x49(text6=72509600, z28=0, val2=9)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Pilgrim in Shenzhen: Conversation_SubState"""
                call = talk_m10_25_x22(z1=125020104, z2=102325, z3=125020107, z4=10253000, z5=102331,
                                       z6=60, z7=102315, z8=125020110)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_25_x5(text19=72509400, text20=72509410, text21=72509420, text22=72509400,
                                          z56=125020105, z57=125020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(125020109) != 1:
                        """State 5: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_25_x15(z41=103620, text9=72509100, z42=0, val3=9, z43=200908,
                                               z44=103621)
                        if call.Done():
                            """State 2: Shenzhen Pilgrim: Magic Square Flag OFF"""
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(125020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(125020105) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_25_x8(text17=72509300, z54=0)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()

def talk_m10_25_7520():
    """Woman Knight (Scrap bottom)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_25_x9(z51=103694, z52=104190, z53=125020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_25_x3(text8=75209200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_25_x6(z49=125020122, text15=75209500, text16=75209500, z50=75209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_25_x7(text18=75209600, z55=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: [Lib] Female knight: Before last: Conversation_SubState"""
                call = talk_m10_25_x34(z12=102483, z13=102488, z14=102503, z15=125020129)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_25_x5(text19=75209400, text20=75209410, text21=75209420, text22=75209400,
                                          z56=125020125, z57=125020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_25_x4(z58=103690, text23=75209100, z59=0, z60=103694)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(125020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(125020125) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_25_x8(text17=75209300, z54=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_25_x0(text10=_, z63=_, z64=0):
    """[Lib] Conversation: General purpose
    text10: Conversation ID
    z63: Conversation flag
    z64: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text10, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z63, 1)
    SetEventFlag(z64, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_25_x1(text1=_, z42=_, z61=-1, z62=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z42: Conversation flag
    z61: Display distance
    z62: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z61)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z42, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_25_x2(text6=_, z28=0):
    """[Lib] Conversation: Event end
    text6: Conversation ID
    z28: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z28, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_25_x3(text8=_, z38=0, z39=20, z40=80):
    """[Lib] Reunion hostility
    text8: Conversation message ID
    z38: Conversation flag ID
    z39: Display distance
    z40: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_25_x40(text8=text8, z38=z38, z39=z39, z40=z40)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_25_x4(z58=103690, text23=75209100, z59=0, z60=103694):
    """[Lib] First hostility
    z58: Hostile: Global event flag
    text23: Conversation ID
    z59: Conversation flag
    z60: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z58, 1)
    SetEventFlag(z60, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z58) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_25_x1(text1=text23, z42=z59, z61=-1, z62=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_25_x5(text19=_, text20=_, text21=_, text22=_, z56=_, z57=_):
    """[Lib] Hostile waiting
    text19: Conversation ID: 1 attacked
    text20: Conversation ID: Attacked 2
    text21: Conversation ID: 3 attacked
    text22: Conversation ID: 4 attacked
    z56: No use: Area and other flags
    z57: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z57) != 1, z57, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z56) != 1, z56, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_25_x1(text1=text22, z42=0, z61=-1, z62=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_25_x1(text1=text21, z42=0, z61=-1, z62=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_25_x1(text1=text20, z42=0, z61=-1, z62=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_25_x1(text1=text19, z42=0, z61=-1, z62=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_25_x6(z49=_, text15=_, text16=_, z50=_):
    """[Lib] Hostile state
    z49: Area and other flags: HP decreased
    text15: Conversation ID: HP drop 1
    text16: Conversation ID: HP drop 2
    z50: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z49) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_25_x10(text15=text15, z49=z49)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_25_x10(text15=text16, z49=z49)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_25_x10(text15=text16, z49=z49)

def talk_m10_25_x7(text18=75209600, z55=0):
    """[Lib] Death status
    text18: Conversation ID
    z55: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_25_x2(text6=text18, z28=z55)

def talk_m10_25_x8(text17=_, z54=0):
    """[Lib] Murder status
    text17: Conversation ID
    z54: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_25_x2(text6=text17, z28=z54)

def talk_m10_25_x9(z51=_, z52=_, z53=_):
    """[Lib] Event: Branch
    z51: Hostile flag
    z52: death flag
    z53: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z52) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z53) != 0
    elif GetEventFlag(z51) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_25_x10(text15=_, z49=_):
    """[Lib] Conversation: HP drop
    text15: Conversation ID
    z49: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text15, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z49, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_25_x11(action1=_):
    """[Lib] selection dialog
    action1: Dialog: Text ID
    """
    """State 0,1: Selection dialog: Display"""
    DisplayOwnYesNoMenu(action1, 0, -1, 0, 0, 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO"""
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        """State 5: End state: Cancel"""
        Label('L0')
        return 2
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_25_x12(z45=0, z46=220, z47=_, z48=0):
    """[Lib] Menu start: General purpose
    z45: Camera parameter ID
    z46: Target Damipoly ID
    z47: NPC event parameter ID
    z48: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z48, z45, z46, z47)
    """State 3: Menu start: Standby"""
    if (NpcMenuResult() == 19) != 0:
        """State 6: Cancel: End state"""
        return 0
    elif (NpcMenuResult() == 18) != 0:
        """State 7: Normal: End state"""
        Label('L0')
        return 1
    elif (NpcMenuResult() == 17) != 0:
        Goto('L0')
    elif (NpcMenuResult() == 16) != 0:
        """State 8: Conversation: end state"""
        return 2
    elif (NpcMenuResult() == 5) != 0:
        """State 12: Pledge: End state"""
        return 6
    elif (NpcMenuResult() == 9) != 0:
        """State 13: Immunity: End State"""
        return 7
    elif (NpcMenuResult() == 10) != 0:
        """State 9: Pledge Discard: End State"""
        return 3
    elif (NpcMenuResult() == 6) != 0:
        """State 10: Votive: End State"""
        return 4
    elif (NpcMenuResult() == 12) != 0:
        """State 11: Ladder: End state"""
        return 5
    elif (NpcMenuResult() == 13) != 0:
        """State 15: Route switching: End state"""
        return 9
    elif (NpcMenuResult() == 14) != 0:
        """State 14: Pass XX: End state"""
        return 8
    elif (NpcMenuResult() == 11) != 0:
        """State 16: Gesture: End state"""
        return 10
    elif (NpcMenuResult() == 1) != 0:
        """State 17: Point reassignment: end state"""
        return 11
    elif (NpcMenuResult() == 20) != 0:
        """State 18: Est bottle enhancement: end state"""
        return 12
    elif (NpcMenuResult() == 21) != 0:
        """State 19: Level up: End state"""
        return 13

def talk_m10_25_x13(text13=72501200, text14=72501300):
    """[Lib] Menu exit: General purpose
    text13: Conversation ID (at the time of purchase)
    text14: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_25_x1(text1=text13, z42=0, z61=-1, z62=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_25_x1(text1=text14, z42=0, z61=-1, z62=0)
    """State 4: End state"""
    return 0

def talk_m10_25_x14(text12=72501100):
    """[Lib] Menu cancellation: General purpose
    text12: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_25_x1(text1=text12, z42=0, z61=-1, z62=0)
    """State 4: End state"""
    return 0

def talk_m10_25_x15(z41=103620, text9=72509100, z42=0, val3=9, z43=200908, z44=103621):
    """[Lib] First hostility _ (pledge cancellation)
    z41: Hostile: Global event flag
    text9: Conversation ID
    z42: Conversation flag
    val3: Cancellation pledge name
    z43: Pledge cancellation: Global conversation flag
    z44: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z41, 1)
    SetEventFlag(z44, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z41) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_25_x39(val2=val3)
    if call.Done() and (GetPlayerCovenant() == val3) != 0:
        """State 3: First hostility: pledge change"""
        ChangePlayerCovenantIf((GetPlayerCovenant() == val3) != 0, 0)
        assert (GetStateTime() >= 0) != 0
        """State 2: First hostility: save execution"""
        SaveExecution()
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 4: Conversation: First hostilization_SubState"""
    assert talk_m10_25_x1(text1=text9, z42=z42, z61=-1, z62=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_25_x16(text5=_, z24=0, lot6=_, z25=_, z26=218, z6=60):
    """[Lib] Conversation: Pledge ranking
    text5: Ranking: Conversation ID
    z24: Ranking: Conversation flag
    lot6: Item lottery
    z25: Ranking transfer: Global event flag
    z26: Previous rank: Global variable
    z6: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_25_x18(action5=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text5, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z24, 1)
    if CanGetItemLot(lot6, 1) != 1 and GetEventFlag(z25) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_25_x50(z27=1011, lot1=lot6)
    elif GetEventFlag(z25) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_25_x19(lot1=lot6, z9=z25)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z26, GetAreaVariable(z6))
    """State 11: End state"""
    return 0

def talk_m10_25_x17(val1=9, z10=8, lot2=0, z11=0, action1=1338, action2=1348, z8=125020110):
    """[Lib] Menu item: Make a pledge
    val1: Pledge name
    z10: Event action
    lot2: Item lottery ID
    z11: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_25_x18(action5=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m10_25_x43(val1=val1, z10=z10, lot2=lot2, z11=z11, action1=action1, action2=action2,
                               z8=z8)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_25_x18(action5=_):
    """[Lib] OK dialog
    action5: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action5, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_25_x19(lot1=_, z9=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    z9: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z9, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_25_x20(z1=125020104, text10=72505100, text11=72505000):
    """[Lib] Conversation: Greeting: Single
    z1: Area other flag: Contact flag
    text10: Text ID: Talk to_continuous
    text11: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(z1) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m10_25_x0(text10=text10, z63=0, z64=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m10_25_x0(text10=text11, z63=0, z64=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(z1, 1)
    """State 5: End state"""
    return 0

def talk_m10_25_x21(lot5=1725000, z23=102320, text4=72506300):
    """[Lib] Equipment transfer: Mes⇒Item
    lot5: Item lottery ID
    z23: Global event flag
    text4: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_25_x1(text1=text4, z42=0, z61=-1, z62=0)
    # lot:1725000:Dragon Chime
    if call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_25_x50(z27=1011, lot1=lot5)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_25_x19(lot1=lot5, z9=z23)
    """State 5: End state"""
    return 0

def talk_m10_25_x22(z1=125020104, z2=102325, z3=125020107, z4=10253000, z5=102331, z6=60, z7=102315,
                    z8=125020110):
    """[Lib] Pilgrim in Shenzhen: Conversation
    z1: Contact: Area and other flags
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Direction: Area and Other Flags
    z4: Magic Square: OBJ instance ID
    z5: Main encounter: Global event flag
    z6: Current pledge rank: Area variable
    z7: Main generation stop: Global event flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102321) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: greeting conversation_SubState"""
        assert talk_m10_25_x23(z1=z1, z6=z6)
        """State 4: [Lib] Pilgrim in Shenzhen: Menu_SubState"""
        assert talk_m10_25_x24(z2=z2, z3=z3, z4=z4, z6=z6, z8=z8)
    elif GetEventFlag(104120) != 0:
        """State 6: [Lib] Conversation: General purpose_SubState"""
        assert talk_m10_25_x0(text10=72509000, z63=0, z64=0)
    else:
        """State 5: [Lib] Pilgrim in Shenzhen: First conversation_SubState"""
        assert talk_m10_25_x27(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, z7=z7, z8=z8)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m10_25_x23(z1=125020104, z6=60):
    """[Lib] Pilgrim in Shenzhen: greeting conversation
    z1: Contact: Area and other flags
    z6: Current pledge rank: Area variable
    """
    """State 0,1: Greeting: Start"""
    if (GetPlayerCovenant() == 9) != 0 and GetEventFlag(102319) != 1:
        """State 8: When pledge ring is not acquired: Insurance_SubState"""
        # lot:2006000:Abyss Seal
        assert talk_m10_25_x47(lot1=2006000, z9=102319)
        """State 3: [Lib] Conversation: Greeting: Single _SubState"""
        Label('L0')
        # talk:72505000:"Young Undead, do you expect me to just keel over?"
        assert talk_m10_25_x20(z1=z1, text10=72505100, text11=72505000)
    else:
        """State 4: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m10_25_x45(z33=9, z6=z6, z34=218, z35=102337, z36=102338, z37=102339)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z6) > 1) != 0 and GetEventFlag(102337) != 1:
                """State 5: Conversation: Pledge Ranking 1_SubState"""
                # talk:72506000:"Young Undead, my work is done...", lot:2006011:Resonant Soul
                assert talk_m10_25_x16(text5=72506000, z24=0, lot6=2006011, z25=102337, z26=218, z6=z6)
            elif (GetAreaVariable(z6) > 2) != 0 and GetEventFlag(102338) != 1:
                """State 6: Conversation: Pledge Ranking 2_SubState"""
                # lot:2006012:Great Resonant Soul
                assert talk_m10_25_x16(text5=72506100, z24=0, lot6=2006012, z25=102338, z26=218, z6=z6)
            elif (GetAreaVariable(z6) > 3) != 0 and GetEventFlag(102339) != 1:
                """State 7: Conversation: Pledge Ranking 3_SubState"""
                # lot:2006013:Climax
                assert talk_m10_25_x16(text5=72506200, z24=0, lot6=2006013, z25=102339, z26=218, z6=z6)
            else:
                Goto('L0')
        elif call.Get() == 0:
            Goto('L0')
    """State 9: End state"""
    return 0

def talk_m10_25_x24(z2=102325, z3=125020107, z4=10253000, z6=60, z8=125020110):
    """[Lib] Pilgrims in Shenzhen: Menu
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    z6: Current pledge rank: Area variable
    z8: For trophies: Area and other flags
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 2: Menu: Branch"""
        if GetEventFlag(100979) != 0:
            """State 10: [Lib] Menu start: No passing _SubState"""
            call = talk_m10_25_x12(z45=0, z46=220, z47=72500001, z48=0)
            if call.Get() == 2:
                """State 9: [Lib] Pilgrim in Shenzhen: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_25_x26()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 6:
                """State 8: [Lib] Menu item: _SubState with a pledge"""
                Label('L1')
                # lot:0:No Item, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
                call = talk_m10_25_x17(val1=9, z10=8, lot2=0, z11=0, action1=1338, action2=1348, z8=z8)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L2')
                assert talk_m10_25_x13(text13=72501200, text14=72501300)
        else:
            """State 4: [Lib] Menu start: General purpose_SubState"""
            call = talk_m10_25_x12(z45=0, z46=220, z47=72500000, z48=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 6:
                Goto('L1')
            elif call.Get() == 8:
                """State 7: [Lib] Pilgrim in Shenzhen: menu passing _SubState"""
                # goods:60151000:Human Effigy
                call = talk_m10_25_x25(goods1=60151000, z2=z2, z3=z3, z4=z4)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L2')
        """State 3: Menu: Exit"""
        Label('L3')
        ClearNpcMenuResults()
        """State 11: End state"""
        return 0
    """State 6: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:72501100:"As you wish, yes, as you wish."
    assert talk_m10_25_x14(text12=72501100)
    Goto('L3')

def talk_m10_25_x25(goods1=60151000, z2=102325, z3=125020107, z4=10253000):
    """[Lib] Pilgrim in Shenzhen: hand over menu
    goods1: Event items
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    """
    """State 0,1: Pass: start"""
    if GetEventFlag(z2) != 0:
        """State 10: Confirmation dialog during magic square release_SubState"""
        # action:1213:"Cannot give now"
        assert talk_m10_25_x18(action5=1213)
    else:
        """State 5: Menu to pass ○○: Conversation to pass_SubState"""
        assert talk_m10_25_x1(text1=72505200, z42=0, z61=-1, z62=0)
        """State 8: Execution selection dialog to pass_SubState"""
        # action:1200:"Give\n%s?", goods:60151000:Human Effigy
        call = talk_m10_25_x41(action4=1200, goods3=60151000)
        if call.Get() == 2:
            pass
        elif call.Get() == 1:
            pass
        # goods:60151000:Human Effigy
        elif call.Get() == 0 and (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 9: No target confirmation dialog_SubState"""
            # action:1206:"You do not have\n%s"
            assert talk_m10_25_x42(action3=1206, goods1=goods1)
        elif call.Get() == 0:
            """State 11: [Lib] Event action: Pass _SubState"""
            # goods:60151000:Human Effigy
            assert talk_m10_25_x48(z29=15, goods2=60151000)
            """State 3: 3rd encounter: Magic square: Open"""
            SetEventFlag(z3, 1)
            """State 4,6: Menu to pass ○○: Conversation to pass: YES_SubState"""
            assert talk_m10_25_x1(text1=72505300, z42=0, z61=-1, z62=0)
            Goto('L0')
        """State 7: Menu to pass ○○: Conversation to pass: NO_SubState"""
        assert talk_m10_25_x1(text1=72505400, z42=0, z61=-1, z62=0)
    """State 2: Pass: Exit"""
    Label('L0')
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_25_x26():
    """[Lib] Pilgrims in Shenzhen: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(100979) != 0 and GetEventFlag(102320) != 1 and GetEventFlag(104120) != 1:
        """State 4: Equipment transfer (Condition: Defeated Agaduran) _SubState"""
        # lot:1725000:Dragon Chime
        assert talk_m10_25_x21(lot5=1725000, z23=102320, text4=72506300)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        assert talk_m10_25_x1(text1=72505500, z42=0, z61=-1, z62=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_25_x27(z1=125020104, z2=102325, z3=125020107, z4=10253000, z5=102331, z7=102315, z8=125020110):
    """[Lib] Pilgrim in Shenzhen: first conversation
    z1: Contact: Area and other flags
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    z5: Main encounter: Global event flag
    z7: Main generation stop: Global event flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: First conversation: start"""
    if GetEventFlag(202752) != 0 and GetEventFlag(z5) != 0:
        """State 4: [Lib] Pilgrim in Shenzhen: Encounter 3rd conversation _SubState"""
        Label('L0')
        assert talk_m10_25_x30(z2=z2, z3=z3, z4=z4, z5=z5, z8=z8)
    elif GetEventFlag(202751) != 0 and GetEventFlag(z5) != 1:
        Goto('L0')
    elif GetEventFlag(202751) != 0 and GetEventFlag(z5) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: second encounter _SubState"""
        Label('L1')
        assert talk_m10_25_x29(z7=z7, z5=z5)
    elif GetEventFlag(202750) != 0 and GetEventFlag(z5) != 1:
        Goto('L1')
    else:
        """State 2: [Lib] Pilgrims in Shenzhen: first encounter conversation_SubState"""
        assert talk_m10_25_x28(z7=z7, z5=z5)
    """State 5: End state"""
    return 0

def talk_m10_25_x28(z7=102315, z5=102331):
    """[Lib] Pilgrim in Shenzhen: first encounter
    z7: Generation stop: Global event flag
    z5: Encounter: Global event flag
    """
    """State 0,1: First encounter conversation: Start"""
    if GetEventFlag(202750) != 0:
        """State 4: Talk: 1st encounter: Loop_SubState"""
        # talk:72500100:"The Dark is still nascent within you.\nMay the Dark shine your way..."
        assert talk_m10_25_x0(text10=72500100, z63=0, z64=0)
    else:
        """State 3: Talk: 1st encounter_SubState"""
        # talk:72500000:"Ahh, look how far this Undead has wandered."
        call = talk_m10_25_x0(text10=72500000, z63=202750, z64=0)
        if call.Done() and GetEventFlag(z7) != 1:
            """State 2: First encounter: stop generation"""
            Label('L0')
            SetEventFlag(z5, 1)
            SetEventFlag(z7, 1)
            assert GetEventFlag(z7) != 0 and GetEventFlag(z5) != 0
        elif call.Done() and GetEventFlag(z5) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 5: End state"""
    return 0

def talk_m10_25_x29(z7=102315, z5=102331):
    """[Lib] Pilgrim in Shenzhen: second encounter
    z7: Generation stop: Global event flag
    z5: Encounter: Global event flag
    """
    """State 0,1: Encounter 2nd conversation: Start"""
    if GetEventFlag(202751) != 0:
        """State 4: Talk: Second encounter: Loop_SubState"""
        # talk:72500300:"May we meet again, somewhere, some time..."
        assert talk_m10_25_x0(text10=72500300, z63=0, z64=0)
    else:
        """State 3: Speak: Second encounter_SubState"""
        # talk:72500200:"Young Undead, don't let this curse weigh upon you."
        call = talk_m10_25_x0(text10=72500200, z63=202751, z64=0)
        if call.Done() and GetEventFlag(z7) != 1:
            """State 2: Second encounter: Stop generation"""
            Label('L0')
            SetEventFlag(z5, 1)
            SetEventFlag(z7, 1)
            assert GetEventFlag(z7) != 0 and GetEventFlag(z5) != 0
        elif call.Done() and GetEventFlag(z5) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 5: End state"""
    return 0

def talk_m10_25_x30(z2=102325, z3=125020107, z4=10253000, z5=102331, z8=125020110):
    """[Lib] Pilgrim in Shenzhen: 3rd encounter
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    z5: Main encounter: Global event flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: Encounter 3rd conversation: Start"""
    if GetEventFlag(202752) != 0:
        """State 6: Speak: 3rd encounter: YES / NO dialog: NO: Loop_SubState"""
        # talk:72500900:"We meet again, young Undead."
        assert talk_m10_25_x0(text10=72500900, z63=0, z64=0)
    else:
        """State 5: Talk: 3rd encounter_SubState"""
        # talk:72500400:"We meet again, young Undead."
        assert talk_m10_25_x0(text10=72500400, z63=202752, z64=0)
    """State 10: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:2006000:Abyss Seal, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
    call = talk_m10_25_x43(val1=9, z10=8, lot2=2006000, z11=102319, action1=1338, action2=1348, z8=z8)
    if call.Get() == 1:
        """State 2: 3rd encounter: After signing the pledge: Set flag"""
        SetEventFlag(102321, 1)
        assert GetEventFlag(102321) != 0
        """State 3: 3rd encounter: Magic square: Open"""
        SetEventFlag(z3, 1)
        """State 4,9: Speak: 3rd encounter: YES / NO dialog: YES_SubState"""
        # talk:72500500:"There you are, you are now a Pilgrim of Dark."
        assert talk_m10_25_x1(text1=72500500, z42=0, z61=-1, z62=0)
    elif call.Get() == 0 and GetEventFlag(202753) != 0:
        """State 8: Speak: 3rd encounter: YES / NO dialog: NO: Loop: YES / NO dialog: NO_SubState"""
        # talk:72501000:"Then choose your own path."
        assert talk_m10_25_x1(text1=72501000, z42=0, z61=-1, z62=0)
    elif call.Get() == 0:
        """State 7: Speak: 3rd encounter: YES / NO dialog: NO_SubState"""
        # talk:72500800:"Hmm... Perhaps I was wrong."
        assert talk_m10_25_x1(text1=72500800, z42=202753, z61=-1, z62=0)
    """State 11: End state"""
    return 0

def talk_m10_25_x31(lot4=_, z19=_, text2=_, text3=_, z20=_, z15=_, z21=0, z22=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot4: Item lottery ID
    z19: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z20: Conversation: Global conversation flag
    z15: Trophy acquisition: Area and other flags
    z21: Emigration permission: Global event flag
    z22: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_25_x1(text1=text2, z42=0, z61=-1, z62=0)
    if call.Done() and GetEventFlag(z19) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z20, 1)
        SetEventFlag(z21, 1)
        SetEventFlag(z22, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_25_x1(text1=text3, z42=0, z61=-1, z62=0)
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_25_x50(z27=1011, lot1=lot4)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_25_x33(lot3=lot4, z16=z19, z17=z20, z18=z15, z21=z21, z22=z22)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_25_x32(lot3=1752020, z16=102496, text1=75201100, z17=203620, z18=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot3: Item lottery ID
    z16: Item transfer: Global event flag
    text1: Conversation ID
    z17: Conversation: Global conversation flag
    z18: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m10_25_x1(text1=text1, z42=0, z61=-1, z62=0)
    if call.Done() and GetEventFlag(z16) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z17, 1)
    # lot:1752020:Ring of Steel Protection+1
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_25_x50(z27=1011, lot1=lot3)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_25_x33(lot3=lot3, z16=z16, z17=z17, z18=z18, z21=0, z22=0)
    """State 9: End state"""
    return 0

def talk_m10_25_x33(lot3=_, z16=_, z17=_, z18=_, z21=0, z22=0):
    """[Lib] Item acquisition dialog: Conversation
    lot3: Item lottery ID
    z16: Item transfer: Global event flag
    z17: Conversation: Global conversation flag
    z18: Trophy acquisition: Area and other flags
    z21: Emigration permission: Global event flag
    z22: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z22, 1)
    SetEventFlag(z21, 1)
    SetEventFlag(z18, 1)
    SetEventFlag(z17, 1)
    SetEventFlag(z16, 1)
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_25_x34(z12=102483, z13=102488, z14=102503, z15=125020129):
    """[Lib] Woman Knight: Before Last: Conversation
    z12: Encounter: Global event flag
    z13: Generation establishment: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    z15: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203630) != 0 and GetEventFlag(z12) != 0:
        """State 5: Woman Knight: Encounter 4th: Conversation_SubState"""
        Label('L0')
        assert talk_m10_25_x38(z13=z13, z12=z12, z14=z14)
    elif GetEventFlag(203623) != 0 and GetEventFlag(z12) != 1:
        Goto('L0')
    elif GetEventFlag(203620) != 0 and GetEventFlag(z12) != 0:
        """State 4: Woman Knight: Encounter 3rd: Conversation_SubState"""
        Label('L1')
        assert talk_m10_25_x37(z13=z13, z12=z12, z14=z14)
    elif GetEventFlag(203614) != 0 and GetEventFlag(z12) != 1:
        Goto('L1')
    elif GetEventFlag(203610) != 0 and GetEventFlag(z12) != 0:
        """State 3: Woman Knight: Encounter 2nd: Conversation_SubState"""
        Label('L2')
        assert talk_m10_25_x36(z13=z13, z12=z12, z14=z14)
    elif GetEventFlag(203602) != 0 and GetEventFlag(z12) != 1:
        Goto('L2')
    elif GetEventFlag(203600) != 0 and GetEventFlag(z12) != 0:
        """State 2: Woman Knight: First encounter: Conversation_SubState"""
        Label('L3')
        assert talk_m10_25_x35(z13=z13, z12=z12, z14=z14)
    else:
        Goto('L3')
    """State 7: End state"""
    return 0

def talk_m10_25_x35(z13=102488, z12=102483, z14=102503):
    """Woman Knight: First encounter: Conversation
    z13: Generation stop: Global event flag
    z12: Encounter: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: First encounter: Start"""
    if GetEventFlag(203601) != 0:
        """State 7: First encounter: Talk: Part 3: 1_SubState"""
        # talk:75200300:"You are an odd one, indeed.\nI've always made a point of avoiding people."
        assert talk_m10_25_x0(text10=75200300, z63=0, z64=0)
        """State 10: First encounter: Talk: Part 3: 2_SubState"""
        # talk:75200310:"While you've made a point of engaging me."
        assert talk_m10_25_x1(text1=75200310, z42=0, z61=-1, z62=0)
        """State 11: First encounter: Talk: Part 3: 3_SubState"""
        # talk:75200320:"I can see that you are mid-journey.\nIf you require assistance, I will help you."
        assert talk_m10_25_x1(text1=75200320, z42=203602, z61=-1, z62=0)
        """State 4: First encounter: White phantom can appear: Set flag"""
        SetEventFlag(z14, 1)
        assert GetEventFlag(z14) != 0
        """State 2: First encounter: stop generation"""
        SetEventFlag(z13, 1)
        assert GetEventFlag(z13) != 0
    elif GetEventFlag(203600) != 0:
        """State 6: First encounter: Talk: Part 2: 1_SubState"""
        # talk:75200100:"Phew..."
        assert talk_m10_25_x0(text10=75200100, z63=0, z64=0)
        """State 8: First encounter: Talk: Part 2: 2_SubState"""
        # talk:75200110:"Heh heh. You are an odd one."
        assert talk_m10_25_x1(text1=75200110, z42=0, z61=-1, z62=0)
        """State 9: First encounter: Talk: Part 2: 3_SubState"""
        # talk:75200120:"Normally, people keep a safe distance\nwhen they see this mask. But you..."
        assert talk_m10_25_x1(text1=75200120, z42=203601, z61=-1, z62=0)
        """State 3: First encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z12, 1)
        assert GetEventFlag(z12) != 0
    else:
        """State 5: First encounter: Talk: Part 1_SubState"""
        # talk:75200000:"What is it?"
        assert talk_m10_25_x0(text10=75200000, z63=203600, z64=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_25_x36(z13=102488, z12=102483, z14=102503):
    """Woman Knight: Second encounter: Conversation
    z13: Generation stop: Global event flag
    z12: Encounter: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter second time: Start"""
    if GetEventFlag(203614) != 0:
        """State 10: Encounter 2nd time: Speak: Part 5 (Single loop) _SubState"""
        # talk:75201000:"I'm sorry...to burden you with talk of my fate."
        assert talk_m10_25_x0(text10=75201000, z63=0, z64=0)
        """State 3: 2nd encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z12, 1)
        assert GetEventFlag(z12) != 0
    elif GetEventFlag(203613) != 0:
        """State 9: Encounter second time: Talk: Part 5: 1_SubState"""
        # talk:75200900:"Have you heard of the Undead?\nThese poor souls affected by the curse."
        assert talk_m10_25_x0(text10=75200900, z63=0, z64=0)
        """State 13: Encounter second time: Talk: Part 5: 2_SubState"""
        # talk:75200910:"An Undead gradually loses his humanity,\nuntil his wits degrade completely."
        assert talk_m10_25_x1(text1=75200910, z42=0, z61=-1, z62=0)
        """State 14: Encounter second time: Speak: Part 5: 3_SubState"""
        # talk:75200960:"I can only hope...that they are."
        assert talk_m10_25_x1(text1=75200960, z42=203614, z61=-1, z62=0)
        """State 4: Second encounter: White phantom can appear: Set flag"""
        SetEventFlag(z14, 1)
        assert GetEventFlag(z14) != 0
        """State 2: Second encounter: Stop generation"""
        SetEventFlag(z13, 1)
        assert GetEventFlag(z13) != 0
    elif GetEventFlag(203612) != 0:
        """State 8: Encounter 2nd time: Talk: 4_SubState"""
        # talk:75200800:"I was raised to wield a sword from birth."
        assert talk_m10_25_x0(text10=75200800, z63=203613, z64=0)
        Goto('L0')
    elif GetEventFlag(203611) != 0:
        """State 7: Encounter second time: Talk: Part 3_SubState"""
        # talk:75200700:"Our land of Mirrah is surrounded by enemies,\nand constantly at war."
        assert talk_m10_25_x0(text10=75200700, z63=203612, z64=0)
        Goto('L0')
    elif GetEventFlag(203610) != 0:
        """State 6: Encounter second time: Speak: Part 2_SubState"""
        # lot:1752010:Human Effigy, talk:75200600:"Ah, yes, I have not thanked you\nfor humouring me the other day.", talk:75200620:"Of course, I've no idea what it is.\nHeh heh."
        assert (talk_m10_25_x31(lot4=1752010, z19=102495, text2=75200600, text3=75200620, z20=203611,
                z15=0, z21=0, z22=0))
        Goto('L0')
    else:
        """State 5: Encounter second time: Speak: Part 1: 1_SubState"""
        # talk:75200500:"I thought that might be you.\nYou haven't changed a bit, have you? Heh heh."
        assert talk_m10_25_x0(text10=75200500, z63=0, z64=0)
        """State 11: Encounter second time: Talk: Part 1: 2_SubState"""
        # talk:75200520:"A wretched place, indeed, but not \nwithout traces of its former glory."
        assert talk_m10_25_x1(text1=75200520, z42=0, z61=-1, z62=0)
        """State 12: Encounter second time: Talk: Part 1: 3_SubState"""
        # talk:75200530:"What could have caused such degradation?"
        assert talk_m10_25_x1(text1=75200530, z42=203610, z61=-1, z62=0)
        Goto('L0')
    """State 15: End state"""
    return 0

def talk_m10_25_x37(z13=102488, z12=102483, z14=102503):
    """Woman Knight: Encounter 3rd: Conversation
    z13: Generation stop: Global event flag
    z12: Encounter: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 3rd: Start"""
    if GetEventFlag(203622) != 0:
        """State 8: Encounter 3rd time: Talk: 4_SubState"""
        # talk:75201400:"If only someone would hear my tale..."
        assert talk_m10_25_x0(text10=75201400, z63=203623, z64=0)
        """State 4: 3rd encounter: White phantom can appear: Set flag"""
        SetEventFlag(z14, 1)
        assert GetEventFlag(z14) != 0
        """State 2: Encounter 3rd: Stop generation"""
        SetEventFlag(z13, 1)
        assert GetEventFlag(z13) != 0
    elif GetEventFlag(203621) != 0:
        """State 7: Encounter third time: Speak: Part 3: 1_SubState"""
        # talk:75201300:"I had an older brother. We learned to fence together."
        assert talk_m10_25_x0(text10=75201300, z63=0, z64=0)
        """State 11: Encounter third time: Speak: Part 3: 2_SubState"""
        # talk:75201340:"But then, one day...he was gone,\nlost without a trace."
        assert talk_m10_25_x1(text1=75201340, z42=203622, z61=-1, z62=0)
        """State 3: 3rd encounter: Set flag during encounter"""
        Label('L0')
        SetEventFlag(z12, 1)
        assert GetEventFlag(z12) != 0
    elif GetEventFlag(203620) != 0:
        """State 6: Encounter 3rd time: Speak: Part 2: 1_SubState"""
        # talk:75201200:"I've found my thoughts growing hazy."
        assert talk_m10_25_x0(text10=75201200, z63=0, z64=0)
        """State 9: Encounter third time: Talk: Part 2: 2_SubState"""
        # talk:75201220:"The curse is doing its work upon me."
        assert talk_m10_25_x1(text1=75201220, z42=0, z61=-1, z62=0)
        """State 10: Encounter third time: Speak: Part 2: 3_SubState"""
        # talk:75201230:"I am frightened... Terribly so..."
        assert talk_m10_25_x1(text1=75201230, z42=203621, z61=-1, z62=0)
        Goto('L0')
    else:
        """State 5: Encounter 3rd time: Speak: Part 1_SubState"""
        # lot:1752020:Ring of Steel Protection+1, talk:75201100:"Still on the road, are you?"
        assert talk_m10_25_x32(lot3=1752020, z16=102496, text1=75201100, z17=203620, z18=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_25_x38(z13=102488, z12=102483, z14=102503):
    """Woman Knight: Encounter 4th: Conversation
    z13: Generation stop: Global event flag
    z12: Encounter: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 4th: Start"""
    if GetEventFlag(203632) != 0:
        """State 8: Encounter 4th: Speak: Part 4_SubState"""
        # talk:75201800:"Sometimes, I feel obsessed...\nwith this insignificant thing called "self"."
        assert talk_m10_25_x0(text10=75201800, z63=203633, z64=0)
        """State 4: 4th encounter: White phantom can appear: Set flag"""
        SetEventFlag(z14, 1)
        assert GetEventFlag(z14) != 0
        """State 2: Encounter 4th: Stop generation"""
        SetEventFlag(z13, 1)
        assert GetEventFlag(z13) != 0
    elif GetEventFlag(203631) != 0:
        """State 7: Encounter 4th: Speak: Part 3_SubState"""
        # talk:75201700:"Loss frightens me no end.\nLoss of memory, loss of self."
        assert talk_m10_25_x0(text10=75201700, z63=203632, z64=0)
        """State 3: 4th encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z12, 1)
        assert GetEventFlag(z12) != 0
    elif GetEventFlag(203630) != 0:
        """State 6: Encounter 4th: Speak: Part 2: 1_SubState"""
        # talk:75201600:"What is this curse?"
        assert talk_m10_25_x0(text10=75201600, z63=0, z64=0)
        """State 9: Encounter 4th: Speak: Part 2: 2_SubState"""
        # talk:75201610:"The question rings in my mind,\nbut I haven't the focus to answer it."
        assert talk_m10_25_x1(text1=75201610, z42=203631, z61=-1, z62=0)
        Goto('L0')
    else:
        """State 5: Encounter 4th: Speak: Part 1_SubState"""
        # talk:75201500:"Oh... You..."
        assert talk_m10_25_x0(text10=75201500, z63=203630, z64=0)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_25_x39(val2=9):
    """[Lib] Pledge cancellation: Overwrite
    val2: Main pledge: pledge type
    """
    """State 0,1: Overwrite: Start"""
    if (not GetPlayerCovenant()) != 0:
        pass
    elif (GetPlayerCovenant() == val2) != 1:
        pass
    else:
        """State 2: Overwrite: Release flag"""
        SetEventFlagIf((GetPlayerCovenant() == 1) != 0, 200900, 1)
        SetEventFlagIf((GetPlayerCovenant() == 2) != 0, 200901, 1)
        SetEventFlagIf((GetPlayerCovenant() == 3) != 0, 200902, 1)
        SetEventFlagIf((GetPlayerCovenant() == 4) != 0, 200903, 1)
        SetEventFlagIf((GetPlayerCovenant() == 5) != 0, 200904, 1)
        SetEventFlagIf((GetPlayerCovenant() == 6) != 0, 200905, 1)
        SetEventFlagIf((GetPlayerCovenant() == 7) != 0, 200906, 1)
        SetEventFlagIf((GetPlayerCovenant() == 8) != 0, 200907, 1)
        SetEventFlagIf((GetPlayerCovenant() == 9) != 0, 200908, 1)
    """State 3: End state"""
    return 0

def talk_m10_25_x40(text8=_, z38=0, z39=20, z40=80):
    """[Lib] Conversation: Hostile display only
    text8: Conversation ID
    z38: Conversation flag
    z39: Display distance
    z40: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), z39)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z38, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_25_x41(action4=1200, goods3=60151000):
    """[Lib] Selection dialog: Item display
    action4: Dialog: Text ID
    goods3: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    # action:1200:"Give\n%s?", goods:60151000:Human Effigy
    DisplayOwnYesNoMenu(action4, 0, -1, 2, goods3, 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO"""
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        """State 5: End state: Cancel"""
        Label('L0')
        return 2
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_25_x42(action3=1206, goods1=60151000):
    """[Lib] OK dialog: Item display
    action3: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: OK dialog: Display"""
    # action:1206:"You do not have\n%s", goods:60151000:Human Effigy
    DisplayOwnOkMenu(action3, 0, 0, -1, 2, goods1, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_25_x43(val1=9, z10=8, lot2=_, z11=_, action1=1338, action2=1348, z8=125020110):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z10: Event action
    lot2: Item lottery ID
    z11: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z8, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_25_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_25_x18(action5=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_25_x44(z10=z10, val1=val1, lot2=lot2, z11=z11) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_25_x18(action5=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_25_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_25_x39(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_25_x44(z10=8, val1=9, lot2=_, z11=_):
    """[Lib] Event action: Pledge
    z10: Event action
    val1: Pledge type
    lot2: Item lottery ID
    z11: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z10)
    assert PlayerIsInEventAction(z10) != 0
    """State 3: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z10) != 1 and CanGetItemLot(lot2, 1) != 1 and GetEventFlag(z11) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot2, 1) != 1 and GetEventFlag(z11) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_25_x50(z27=1011, lot1=lot2)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z10) != 1 and GetEventFlag(z11) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z10) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z11, 1)
        AwardItem(lot2, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z10) != 1
    """State 8: End state"""
    return 0

def talk_m10_25_x45(z33=9, z6=60, z34=218, z35=102337, z36=102338, z37=102339):
    """[Lib] Pledge: Rank up: Conversation: 1
    z33: Pledge: Pledge type
    z6: Current rank: Area variable
    z34: Previous rank: Global variable
    z35: Ranking 1: Item transfer: Global event flag
    z36: Ranking 2: Item transfer: Global event flag
    z37: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z6, GetPlayerCovenantLevel(z33))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z34) > GetAreaVariable(z6)) != 1 and (GetGlobalVariable(z34) == GetAreaVariable(z6))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z34) > GetAreaVariable(z6)) != 0 and (GetGlobalVariable(z34) == GetAreaVariable(z6))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z34, GetAreaVariable(z6))
    elif GetEventFlag(z35) != 1 and (GetGlobalVariable(z34) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(z36) != 1 and (GetGlobalVariable(z34) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(z37) != 1 and (GetGlobalVariable(z34) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_25_x46(text7=_, z30=_, z31=9901, z32=-1):
    """[Lib] Conversation: For unique key guide
    text7: Conversation ID
    z30: Conversation flag
    z31: Key guide parameters
    z32: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z31)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), z32)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z30, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_25_x47(lot1=2006000, z9=102319):
    """[Lib] Conversation: Item transfer: Item: Key
    lot1: Item lottery
    z9: Item transfer: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # lot:2006000:Abyss Seal
    if CanGetItemLot(lot1, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_25_x50(z27=1011, lot1=lot1)
    elif GetEventFlag(z9) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_25_x19(lot1=lot1, z9=z9)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m10_25_x48(z29=15, goods2=60151000):
    """[Lib] Event action: Pass
    z29: Event action
    goods2: Item to be handed: Event item
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z29)
    assert PlayerIsInEventAction(z29) != 0
    """State 2: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z29) != 1
    """State 4: Event action: Pass: Item transfer"""
    # goods:60151000:Human Effigy
    ConsumeItem(goods2, 1)
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z29) != 1
    """State 5: End state"""
    return 0

def talk_m10_25_x49(text6=72509600, z28=0, val2=9):
    """[Lib] Death status_ (pledge cancellation)
    text6: Conversation ID
    z28: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_25_x39(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_25_x2(text6=text6, z28=z28)

def talk_m10_25_x50(z27=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z27: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_25_x51():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(100763) != 0 and GetEventFlag(208001) != 0:
        """State 6: [Lib] Conversation: Talk to 3_SubState"""
        # talk:69200200:"Young Hollow, seek after Vendrick."
        assert talk_m10_25_x46(text7=69200200, z30=0, z31=9901, z32=-1)
        """State 3: End encounter flag"""
        SetEventFlag(100740, 1)
    elif GetEventFlag(100763) != 0 and GetEventFlag(208000) != 0:
        """State 5: [Lib] Conversation: Talk to 2_SubState"""
        # talk:69200100:"Young Hollow, there are but two paths.\nInherit the order of this world, or destroy it."
        assert talk_m10_25_x46(text7=69200100, z30=208001, z31=9901, z32=-1)
    elif GetEventFlag(100763) != 0:
        """State 4: [Lib] Conversation: Talk to 1_SubState"""
        # talk:69200010:"No one has come this far,\nnot for a very long while."
        assert talk_m10_25_x46(text7=69200010, z30=208000, z31=9901, z32=-1)
    """State 2,7: End state"""
    return 0

def talk_m10_25_4100000():
    """Andyel"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(100740) != 0:
            break
        else:
            """State 3: Anne Deal_SubState"""
            assert talk_m10_25_x51()
    """State 2: Conversation: System termination"""
    EndMachine()

