# -*- coding: utf-8 -*-
def talk_m10_33_7260():
    """Dwarf (Faros Doorway)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_33_x9(z45=103634, z46=104130, z47=133020111)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_33_x3(text9=72609200, z30=0, z31=20, z32=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_33_x6(z43=133020112, text14=72609500, text15=72609500, z44=72609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_33_x7(text17=72609600, z49=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Dwarf: Conversation_SubState"""
                call = talk_m10_33_x22(z15=133020113, z16=0, z17=102349)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_33_x5(text18=72609400, text19=72609410, text20=72609420, text21=72609400,
                                          z50=133020114, z51=133020115)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_33_x4(z52=103630, text22=72609100, z53=0, z54=103634)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(133020115) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(133020114) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_33_x8(text16=72609300, z48=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_33_7560():
    """The mouse king (Faros doorway)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_33_x9(z45=103920, z46=104420, z47=133020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_33_x3(text9=75609200, z30=0, z31=20, z32=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_33_x6(z43=133020102, text14=75609500, text15=75609500, z44=75609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m10_33_x44(text6=75609600, z20=0, val2=5)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 8: [Lib] The mouse king: Conversation_SubState"""
                call = talk_m10_33_x27(z1=60, z2=102971, z3=10349000, z4=133020107)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_33_x5(text18=75609400, text19=75609410, text20=75609420, text21=75609400,
                                          z50=133020105, z51=133020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_33_x15(z33=103920, text10=75609100, z34=0, val4=5, z35=200904,
                                               z36=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(133020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(133020105) != 1:
                    Goto('L2')
        """State 7: [Lib] Killing state_SubState"""
        talk_m10_33_x8(text16=75609300, z48=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_33_x0(text23=_, z57=_, z58=0):
    """[Lib] Conversation: General purpose
    text23: Conversation ID
    z57: Conversation flag
    z58: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text23, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z57, 1)
    SetEventFlag(z58, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_33_x1(text1=_, z34=_, z55=-1, z56=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z34: Conversation flag
    z55: Display distance
    z56: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z55)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z34, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_33_x2(text6=_, z20=0):
    """[Lib] Conversation: Event end
    text6: Conversation ID
    z20: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z20, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_33_x3(text9=_, z30=0, z31=20, z32=80):
    """[Lib] Reunion hostility
    text9: Conversation message ID
    z30: Conversation flag ID
    z31: Display distance
    z32: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_33_x34(text9=text9, z30=z30, z31=z31, z32=z32)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_33_x4(z52=103630, text22=72609100, z53=0, z54=103634):
    """[Lib] First hostility
    z52: Hostile: Global event flag
    text22: Conversation ID
    z53: Conversation flag
    z54: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z52, 1)
    SetEventFlag(z54, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z52) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_33_x1(text1=text22, z34=z53, z55=-1, z56=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_33_x5(text18=_, text19=_, text20=_, text21=_, z50=_, z51=_):
    """[Lib] Hostile waiting
    text18: Conversation ID: 1 attacked
    text19: Conversation ID: Attacked 2
    text20: Conversation ID: 3 attacked
    text21: Conversation ID: 4 attacked
    z50: No use: Area and other flags
    z51: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z51) != 1, z51, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z50) != 1, z50, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_33_x1(text1=text21, z34=0, z55=-1, z56=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_33_x1(text1=text20, z34=0, z55=-1, z56=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_33_x1(text1=text19, z34=0, z55=-1, z56=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_33_x1(text1=text18, z34=0, z55=-1, z56=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_33_x6(z43=_, text14=_, text15=_, z44=_):
    """[Lib] Hostile state
    z43: Area and other flags: HP decreased
    text14: Conversation ID: HP drop 1
    text15: Conversation ID: HP drop 2
    z44: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z43) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_33_x10(text14=text14, z43=z43)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_33_x10(text14=text15, z43=z43)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_33_x10(text14=text15, z43=z43)

def talk_m10_33_x7(text17=72609600, z49=0):
    """[Lib] Death status
    text17: Conversation ID
    z49: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_33_x2(text6=text17, z20=z49)

def talk_m10_33_x8(text16=_, z48=0):
    """[Lib] Murder status
    text16: Conversation ID
    z48: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_33_x2(text6=text16, z20=z48)

def talk_m10_33_x9(z45=_, z46=_, z47=_):
    """[Lib] Event: Branch
    z45: Hostile flag
    z46: death flag
    z47: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z46) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z47) != 0
    elif GetEventFlag(z45) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_33_x10(text14=_, z43=_):
    """[Lib] Conversation: HP drop
    text14: Conversation ID
    z43: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text14, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z43, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_33_x11(action1=_):
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

def talk_m10_33_x12(z39=0, z40=220, z41=_, z42=0):
    """[Lib] Menu start: General purpose
    z39: Camera parameter ID
    z40: Target Damipoly ID
    z41: NPC event parameter ID
    z42: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z42, z39, z40, z41)
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

def talk_m10_33_x13(text12=_, text13=_):
    """[Lib] Menu exit: General purpose
    text12: Conversation ID (at the time of purchase)
    text13: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_33_x1(text1=text12, z34=0, z55=-1, z56=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_33_x1(text1=text13, z34=0, z55=-1, z56=0)
    """State 4: End state"""
    return 0

def talk_m10_33_x14(text11=_):
    """[Lib] Menu cancellation: General purpose
    text11: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_33_x1(text1=text11, z34=0, z55=-1, z56=0)
    """State 4: End state"""
    return 0

def talk_m10_33_x15(z33=103920, text10=75609100, z34=0, val4=5, z35=200904, z36=0):
    """[Lib] First hostility _ (pledge cancellation)
    z33: Hostile: Global event flag
    text10: Conversation ID
    z34: Conversation flag
    val4: Cancellation pledge name
    z35: Pledge cancellation: Global conversation flag
    z36: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z33, 1)
    SetEventFlag(z36, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z33) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_33_x33(val2=val4)
    if call.Done() and (GetPlayerCovenant() == val4) != 0:
        """State 3: First hostility: pledge change"""
        ChangePlayerCovenantIf((GetPlayerCovenant() == val4) != 0, 0)
        assert (GetStateTime() >= 0) != 0
        """State 2: First hostility: save execution"""
        SaveExecution()
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 4: Conversation: First hostilization_SubState"""
    assert talk_m10_33_x1(text1=text10, z34=z34, z55=-1, z56=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_33_x16(action4=_):
    """[Lib] OK dialog
    action4: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action4, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_33_x17(goods1=62140000, val3=5, z1=60, z25=214, z26=15, lot7=0, z27=0, z28=102963):
    """[Lib] Menu item: Dedicated
    goods1: Special Offer: Event Item
    val3: Pledge name
    z1: Current pledge rank: Area variable
    z25: Last pledge rank: global variable
    z26: Event action
    lot7: Transfer: Item lottery
    z27: Transfer: Global event flag
    z28: Ranking 3 items: Global event flag
    """
    """State 0,1: Votive: Start"""
    if (GetPlayerCovenant() == val3) != 1:
        """State 8: Votive: Confirmation dialog not signed"""
        # action:1314:"You must belong to this covenant\nto make an offering"
        assert talk_m10_33_x16(action4=1314)
    elif GetEventFlag(z28) != 0 and (GetGlobalVariable(z25) == 3) != 0:
        """State 4: Dedication: No more dedication confirmation dialog_SubState"""
        Label('L0')
        # action:1309:"There is nothing more to offer.\nYou have done fine work."
        assert talk_m10_33_x16(action4=1309)
    elif GetEventFlag(z28) != 0 and (GetPlayerCovenantLevel(val3) > 3) != 0:
        Goto('L0')
    else:
        """State 6: Dedication: Dedication selection dialog_SubState"""
        # action:1306:"Offer\n%s?"
        call = talk_m10_33_x35(action3=1306, goods1=goods1)
        # goods:62140000:Rat Tail
        if call.Get() == 0 and (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 5: Votive: Confirmation of possession of possession _SubState"""
            # action:1310:"You have no offerings"
            assert talk_m10_33_x16(action4=1310)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Dedication_SubState"""
            assert talk_m10_33_x38(z29=15, goods1=goods1, z1=z1, val3=val3, lot7=lot7, z27=z27)
            """State 3: Delivery confirmation dialog_SubState"""
            # action:1307:"Your devotion to your\ncovenant has deepened"
            assert talk_m10_33_x16(action4=1307)
            """State 9: Rank up: End state"""
            return 0
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 2: Votive: Finish"""
    ClearNpcMenuSelection()
    """State 10: End state"""
    return 1

def talk_m10_33_x18(lot1=_, z5=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    z5: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z5, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_33_x19(lot5=1726000, z18=102355, text5=72606000):
    """[Lib] Equipment transfer: Mes⇒Item
    lot5: Item lottery ID
    z18: Global event flag
    text5: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_33_x1(text1=text5, z34=0, z55=-1, z56=0)
    # lot:1726000:Gyrm Greataxe
    if call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_33_x45(z19=1011, lot1=lot5)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_33_x18(lot1=lot5, z5=z18)
    """State 5: End state"""
    return 0

def talk_m10_33_x20(lot2=2005000, z6=102960, z7=_, z8=0, z37=0, z38=0):
    """[Lib] Item acquisition dialog: Conversation
    lot2: Item lottery ID
    z6: Item transfer: Global event flag
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    z37: Emigration permission: Global event flag
    z38: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z38, 1)
    SetEventFlag(z37, 1)
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(z6, 1)
    # lot:2005000:Crest of the Rat
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_33_x21(lot4=2005000, z12=102960, text3=75600300, text4=75600330, z13=206010, z14=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z12: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z13: Conversation: Global conversation flag
    z14: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_33_x1(text1=text3, z34=0, z55=-1, z56=0)
    if call.Done() and GetEventFlag(z12) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z13, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_33_x1(text1=text4, z34=0, z55=-1, z56=0)
    # lot:2005000:Crest of the Rat
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_33_x45(z19=1011, lot1=lot4)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_33_x20(lot2=lot4, z6=z12, z7=z13, z8=z14, z37=0, z38=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_33_x22(z15=133020113, z16=0, z17=102349):
    """[Lib] Dwarf: Conversation
    z15: Contact: Area and other flags
    z16: Emigration permission: Global event flag
    z17: Shop list: Global event flag
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    SetEventFlag(z17, 1)
    if GetEventFlag(202900) != 0:
        """State 4: Dwarf: Greetings_SubState"""
        assert talk_m10_33_x24(z15=z15, z16=z16)
    else:
        """State 3: Dwarf: First conversation_SubState"""
        assert talk_m10_33_x23(z15=z15, z16=z16)
    """State 5: Dwarf: NPC menu_SubState"""
    assert talk_m10_33_x25()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_33_x23(z15=133020113, z16=0):
    """Dwarf: First conversation
    z15: Contact: Area and other flags
    z16: Emigration permission: Global event flag
    """
    """State 0,1,3: Speak: Part 1: 1_SubState"""
    # talk:72600000:"Who you?"
    assert talk_m10_33_x0(text23=72600000, z57=202900, z58=0)
    """State 4: Talk: Part 1: 2_SubState"""
    # talk:72600060:"With Gavlan, you wheel?\nYou deal! Gah hah!"
    assert talk_m10_33_x1(text1=72600060, z34=202900, z55=-1, z56=0)
    """State 2: First conversation: Set contact flag"""
    SetEventFlag(z16, 1)
    SetEventFlag(z15, 1)
    assert GetEventFlag(z15) != 0
    """State 5: End state"""
    return 0

def talk_m10_33_x24(z15=133020113, z16=0):
    """Dwarf: Greeting
    z15: Contact: Area and other flags
    z16: Emigration permission: Global event flag
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z15) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 7: Talk to _continuous 1_SubState"""
            # talk:72600100:"What? You want?"
            assert talk_m10_33_x0(text23=72600100, z57=0, z58=0)
        else:
            """State 8: Talk to _continuous 2_SubState"""
            # talk:72600200:"Umm...You want? Want what?"
            assert talk_m10_33_x0(text23=72600200, z57=0, z58=0)
    else:
        """State 4: Long time no see: branch"""
        if GetEventFlag(202904) != 0:
            """State 5: Long time no see: Flag initialization"""
            SetEventFlag(202901, 0)
            SetEventFlag(202902, 0)
            SetEventFlag(202903, 0)
            SetEventFlag(202904, 0)
            """State 9: Talk to me after a long time 1_SubState"""
            Label('L0')
            # talk:72600300:"Umm...Gavlan know you."
            assert talk_m10_33_x0(text23=72600300, z57=202901, z58=0)
        elif GetEventFlag(202903) != 0:
            """State 12: Talk to _After a long time 4_SubState"""
            # talk:72600600:"You, again.\nGavlan, meet you again."
            assert talk_m10_33_x0(text23=72600600, z57=202904, z58=0)
        elif GetEventFlag(202902) != 0:
            """State 11: Talk to _After a long time 3_SubState"""
            # talk:72600500:"Oh Gavlan, know you.\nWhat you want?"
            assert talk_m10_33_x0(text23=72600500, z57=202903, z58=0)
        elif GetEventFlag(202901) != 0:
            """State 10: Talk to _After a long time 2_SubState"""
            # talk:72600400:"Make deal with Gavlan?"
            assert talk_m10_33_x0(text23=72600400, z57=202902, z58=0)
        else:
            Goto('L0')
        """State 6: Greeting: Contact flag setting"""
        SetEventFlag(z16, 1)
        SetEventFlag(z15, 1)
        assert GetEventFlag(z15) != 0
    """State 13: End state"""
    return 0

def talk_m10_33_x25():
    """Dwarf: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 6: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_33_x12(z39=0, z40=220, z41=72600000, z42=0)
        if call.Get() == 2:
            """State 5: Dwarf: Menu conversation_SubState"""
            call = talk_m10_33_x26()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3: [Lib] Exit menu: General purpose_SubState"""
            # talk:72600700:"Many deal...many thanks! Gah hah!", talk:72600800:"You? Go home?"
            assert talk_m10_33_x13(text12=72600700, text13=72600800)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuResults()
        """State 7: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:72600900:"Umm..."
    assert talk_m10_33_x14(text11=72600900)
    Goto('L0')

def talk_m10_33_x26():
    """Dwarf: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102355) != 1 and (GetGlobalVariable(200) > NpcInfoValue(7260, 0)) != 0 and GetEventFlag(104130)
        != 1):
        """State 3: Equipment transfer (Condition: Total purchase amount is above a certain level) _SubState"""
        # lot:1726000:Gyrm Greataxe, talk:72606000:"Wheel...deal..."
        assert talk_m10_33_x19(lot5=1726000, z18=102355, text5=72606000)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:72605000:"Umm...You strong."
        assert talk_m10_33_x1(text1=72605000, z34=0, z55=-1, z56=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_33_x27(z1=60, z2=102971, z3=10349000, z4=133020107):
    """[Lib] The Mouse King: Conversation
    z1: Current pledge rank: Area variable
    z2: Sub1: Generation stop: Global event flag
    z3: Key guide parameters
    z4: For trophies: Area and other flags
    """
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        ClearNpcMenuResults()
        if (GetPlayerCovenant() == 5) != 0:
            """State 4: Mouse king: pledge conversation_SubState"""
            assert talk_m10_33_x29(z1=z1, z3=z3)
        elif GetEventFlag(200904) != 0:
            break
        # goods:62140000:Rat Tail
        elif (ItemCount(62140000, 1, 1, 0) > 1) != 0 and GetEventFlag(206000) != 0:
            """State 3: The Mouse King: Unconfirmed Conversation_SubState"""
            call = talk_m10_33_x28(z3=z3, z4=z4)
            if call.Done():
                pass
            # goods:62140000:Rat Tail
            elif GetEventFlag(206010) != 1 and (ItemCount(62140000, 1, 1, 0) > 1) != 1:
                continue
        else:
            """State 6: Mouse King: Mouse Tail: Not Owned_SubState"""
            assert talk_m10_33_x39(z2=z2, z3=z3)
        """State 2: Conversation: End"""
        Label('L0')
        ClearNpcMenuResults()
        """State 7: End state"""
        return 0
    """State 5: The Mouse King: Re-pledge conversation_SubState"""
    assert talk_m10_33_x32(z3=z3, z4=z4)
    Goto('L0')

def talk_m10_33_x28(z3=10349000, z4=133020107):
    """Mouse king: unpowed conversation
    z3: Key guide parameters
    z4: For trophies: Area and other flags
    """
    """State 0,1: Unpowed conversation: Conversation"""
    if GetEventFlag(206001) != 0:
        """State 7: Talk: Item possession: 2nd time_SubState"""
        # talk:75600500:"Thou return'st?"
        assert talk_m10_33_x42(text7=75600500, z21=0, z3=z3, z22=-1)
    else:
        """State 6: Talk: Item possession_SubState"""
        # talk:75600200:"Is that a Rat Tail, human?"
        assert talk_m10_33_x42(text7=75600200, z21=206001, z3=z3, z22=-1)
    """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item, action:1334:"Join the Rat King covenant?", action:1344:"Abandon your covenant and\njoin the Rat King covenant?"
    call = talk_m10_33_x36(val1=5, z10=8, lot3=0, z11=0, action1=1334, action2=1344, z4=z4)
    if call.Get() == 1:
        """State 5: Speak: Item possession: YES_SubState"""
        # lot:2005000:Crest of the Rat, talk:75600300:"Thou hast the eyes of one who perceiveth true beauty.", talk:75600330:"The ring draws to thee those who would defile our burrow."
        assert (talk_m10_33_x21(lot4=2005000, z12=102960, text3=75600300, text4=75600330, z13=206010,
                z14=0))
    elif call.Get() == 0 and GetEventFlag(206004) != 0:
        """State 3: Talk: Item possession: Second time: NO_SubState"""
        # talk:75600600:"Then we need consort no longer."
        assert talk_m10_33_x1(text1=75600600, z34=0, z55=-1, z56=0)
    elif call.Get() == 0:
        """State 2: Talk: Item possession: NO_SubState"""
        # talk:75600400:"Of course. Humans are all alike."
        assert talk_m10_33_x1(text1=75600400, z34=206004, z55=-1, z56=0)
    """State 8: End state"""
    return 0

def talk_m10_33_x29(z1=60, z3=10349000):
    """Mouse king: pledge conversation
    z1: Current pledge rank: Area variable
    z3: Key guide parameters
    """
    """State 0,1: Pledge conversation: start"""
    if GetEventFlag(102960) != 1:
        """State 4: When ring is not transferred: Insurance_SubState"""
        # lot:2005000:Crest of the Rat, talk:75600300:"Thou hast the eyes of one who perceiveth true beauty.", talk:75600330:"The ring draws to thee those who would defile our burrow."
        assert (talk_m10_33_x43(lot2=2005000, z6=102960, text1=75600300, text2=75600330, z7=0, z8=0,
                z3=z3))
    else:
        """State 5: Pledge conversation: first time _SubState"""
        # talk:75600700:"Speak thy mind, servant."
        assert talk_m10_33_x42(text7=75600700, z21=0, z3=z3, z22=-1)
        """State 3: Mouse King: NPC Menu_SubState"""
        assert talk_m10_33_x30(z1=z1)
    """State 2: Pledge conversation: End"""
    ClearNpcMenuSelection()
    """State 6: End state"""
    return 0

def talk_m10_33_x30(z1=60):
    """The Mouse King: NPC Menu
    z1: Current pledge rank: Area variable
    """
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Menu: Start"""
        Label('L0')
        while True:
            """State 3: [Lib] Menu start: General purpose_SubState"""
            call = talk_m10_33_x12(z39=0, z40=220, z41=75600000, z42=0)
            if call.Get() == 2:
                """State 6: The Mouse King: Menu Conversation_SubState"""
                call = talk_m10_33_x31()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 4:
                """State 7: [Lib] Menu item: Dedicated _SubState"""
                # goods:62140000:Rat Tail, lot:0:No Item
                call = talk_m10_33_x17(goods1=62140000, val3=5, z1=z1, z25=214, z26=15, lot7=0, z27=0,
                                       z28=102963)
                if call.Get() == 1:
                    Continue('mainloop')
                elif call.Get() == 0:
                    Break('mainloop')
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 4: [Lib] Exit menu: General purpose_SubState"""
                # talk:75601300:"My servant, destroy my enemies.", talk:75601400:"My servant, do not disappoint me."
                assert talk_m10_33_x13(text12=75601300, text13=75601400)
            """State 2: Menu: Exit"""
            Label('L1')
            ClearNpcMenuSelection()
            """State 9: End state"""
            return 0
        """State 5: [Lib] Menu cancellation: General purpose_SubState"""
        Label('L2')
        # talk:75601500:"Go then, my servant."
        assert talk_m10_33_x14(text11=75601500)
        Goto('L1')
    """State 8: [Lib] Menu item: Dedicated: Mouse king: Pledge item award_SubState"""
    call = talk_m10_33_x40(z1=z1, z9=214)
    if call.Done():
        Goto('L0')
    elif (NpcMenuResult() == 19) != 0:
        Goto('L2')

def talk_m10_33_x31():
    """Mouse king: menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(206005) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(206002, 0)
        SetEventFlag(206003, 0)
        SetEventFlag(206005, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:75605000:"I will destroy thee, filthy human!"
        assert talk_m10_33_x1(text1=75605000, z34=206002, z55=-1, z56=0)
    elif GetEventFlag(206003) != 0:
        """State 6: Menu conversation: 3_SubState"""
        assert talk_m10_33_x1(text1=75605200, z34=206005, z55=-1, z56=0)
    elif GetEventFlag(206002) != 0:
        """State 5: Menu conversation: 2_SubState"""
        assert talk_m10_33_x1(text1=75605100, z34=206003, z55=-1, z56=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 7: End state"""
    return 0

def talk_m10_33_x32(z3=10349000, z4=133020107):
    """Mouse king: re-pledge conversation
    z3: Key guide parameters
    z4: For trophies: Area and other flags
    """
    """State 0,1,7: Re-pledge conversation: first time _SubState"""
    # talk:75601100:"Why comest thou here, human?"
    assert talk_m10_33_x42(text7=75601100, z21=0, z3=z3, z22=-1)
    """State 5: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item, action:1334:"Join the Rat King covenant?", action:1344:"Abandon your covenant and\njoin the Rat King covenant?"
    call = talk_m10_33_x36(val1=5, z10=8, lot3=0, z11=0, action1=1334, action2=1344, z4=z4)
    if call.Get() == 0:
        """State 4: Re-pledge conversation: First time: NO_SubState"""
        # talk:75601200:"Traitors will not be forgiven. Get thee gone."
        assert talk_m10_33_x1(text1=75601200, z34=0, z55=-1, z56=0)
    elif call.Get() == 1 and GetEventFlag(102960) != 1:
        """State 8: [Lib] Conversation: Item transfer: Item: UnicKey_SubState"""
        # lot:2005000:Crest of the Rat
        assert talk_m10_33_x46(lot1=2005000, z5=102960, z3=z3)
        """State 3: Re-pledge conversation: First time: YES_SubState"""
        Label('L0')
        # talk:75601400:"My servant, do not disappoint me."
        assert talk_m10_33_x1(text1=75601400, z34=0, z55=-1, z56=0)
    elif call.Get() == 1:
        Goto('L0')
    """State 2,9: End state"""
    return 0

def talk_m10_33_x33(val2=5):
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

def talk_m10_33_x34(text9=_, z30=0, z31=20, z32=80):
    """[Lib] Conversation: Hostile display only
    text9: Conversation ID
    z30: Conversation flag
    z31: Display distance
    z32: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), z31)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z30, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_33_x35(action3=1306, goods1=62140000):
    """[Lib] Selection dialog: Item display
    action3: Dialog: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    # action:1306:"Offer\n%s?", goods:62140000:Rat Tail
    DisplayOwnYesNoMenu(action3, 0, -1, 2, goods1, 0)
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

def talk_m10_33_x36(val1=5, z10=8, lot3=0, z11=0, action1=1334, action2=1344, z4=133020107):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z10: Event action
    lot3: Item lottery ID
    z11: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z4, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_33_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_33_x16(action4=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_33_x37(z10=z10, val1=val1, lot3=lot3, z11=z11) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_33_x16(action4=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_33_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_33_x33(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_33_x37(z10=8, val1=5, lot3=0, z11=0):
    """[Lib] Event action: Pledge
    z10: Event action
    val1: Pledge type
    lot3: Item lottery ID
    z11: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z10)
    assert PlayerIsInEventAction(z10) != 0
    """State 3: IventAction: Motion_Waiting"""
    # lot:0:No Item
    if PlayerIsInEventAction(z10) != 1 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(z11) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        # lot:0:No Item
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(z11) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_33_x45(z19=1011, lot1=lot3)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z10) != 1 and GetEventFlag(z11) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z10) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z11, 1)
        # lot:0:No Item
        AwardItem(lot3, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z10) != 1
    """State 8: End state"""
    return 0

def talk_m10_33_x38(z29=15, goods1=62140000, z1=60, val3=5, lot7=0, z27=0):
    """[Lib] Event action: Dedication
    z29: Event action
    goods1: Special Offer: Event Item
    z1: Current pledge level: area variable
    val3: Pledge type
    lot7: Transfer: Item lottery
    z27: Transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z29)
    assert PlayerIsInEventAction(z29) != 0
    """State 2: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z29) != 1 and GetEventFlag(z27) != 0:
        """State 4: Event action: votive delivery"""
        # goods:62140000:Rat Tail
        ConsumeItem(goods1, 1)
        AddPlayerCovenantContribution(val3, 1)
        SetAreaVariable(z1, GetPlayerCovenantLevel(val3))
        SaveExecution()
    elif PlayerIsInEventAction(z29) != 1:
        """State 5: Event action: Votive delivery: Item transfer"""
        # lot:0:No Item
        AwardItem(lot7, 1)
        SetEventFlag(z27, 1)
        # goods:62140000:Rat Tail
        ConsumeItem(goods1, 1)
        AddPlayerCovenantContribution(val3, 1)
        SetAreaVariable(z1, GetPlayerCovenantLevel(val3))
        SaveExecution()
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z29) != 1
    """State 6: End state"""
    return 0

def talk_m10_33_x39(z2=102971, z3=10349000):
    """Mouse King: Mouse Tail: Not Owned
    z2: Sub 1 generation stop: Global event flag
    z3: Key guide parameters
    """
    """State 0,1: Not possessed: Start"""
    if GetEventFlag(206000) != 0:
        """State 5: Talk: First time: Second time _SubState"""
        # talk:75600100:"Thy welcome wearest thin."
        call = talk_m10_33_x42(text7=75600100, z21=0, z3=z3, z22=-1)
        if call.Done():
            pass
        # goods:62140000:Rat Tail
        elif (ItemCount(62140000, 1, 1, 0) > 1) != 0 and GetEventFlag(206000) != 0:
            """State 2: Not possessed: Delete key guide"""
            Label('L0')
            DeleteKeyGuideArea()
    else:
        """State 4: Talk: First_SubState"""
        # talk:75600000:"Leave this place, human."
        call = talk_m10_33_x42(text7=75600000, z21=206000, z3=z3, z22=-1)
        if call.Done() and GetEventFlag(z2) != 1:
            """State 3: Not owned: Stop generation: Set flag"""
            SetEventFlag(z2, 1)
            assert GetEventFlag(z2) != 0
        elif call.Done():
            pass
        # goods:62140000:Rat Tail
        elif (ItemCount(62140000, 1, 1, 0) > 1) != 0 and GetEventFlag(206000) != 0:
            Goto('L0')
    """State 6: End state"""
    return 0

def talk_m10_33_x40(z1=60, z9=214):
    """[Lib] Menu item: Dedicated: Mouse king: Pledge item award
    z1: Current pledge rank: Area variable
    z9: Last pledge rank: global variable
    """
    """State 0,3: Dedication: rank up judgment"""
    if (GetGlobalVariable(z9) > GetAreaVariable(z1)) != 1:
        """State 2: Pledge ranking judgment"""
        Label('L0')
        # lot:2005011:Small Smooth & Silky Stone
        if (GetAreaVariable(z1) > 1) != 0 and GetEventFlag(102961) != 1 and CanGetItemLot(2005011, 1) != 1:
            """State 8: [Lib] Inventory full dialog (ranking 1) _SubState"""
            # lot:2005011:Small Smooth & Silky Stone
            assert talk_m10_33_x45(z19=1011, lot1=2005011)
        elif (GetAreaVariable(z1) > 1) != 0 and GetEventFlag(102961) != 1:
            """State 5: Pledge ranking 1 item acquisition dialog_SubState"""
            # talk:75601600:"I am aware of thine accomplishments, and they are not few.", lot:2005011:Small Smooth & Silky Stone
            assert talk_m10_33_x41(text8=75601600, z23=0, lot6=2005011, z24=102961)
            """State 1: Pledge ranking: area variable ⇒ global variable"""
            Label('L1')
            SetGlobalVariable(214, GetAreaVariable(z1))
        # lot:2005012:Smooth & Silky Stone
        elif (GetAreaVariable(z1) > 2) != 0 and GetEventFlag(102962) != 1 and CanGetItemLot(2005012, 1) != 1:
            """State 9: [Lib] Inventory full dialog (ranking 2) _SubState"""
            # lot:2005012:Smooth & Silky Stone
            assert talk_m10_33_x45(z19=1011, lot1=2005012)
        elif (GetAreaVariable(z1) > 2) != 0 and GetEventFlag(102962) != 1:
            """State 6: Pledge ranking 2 item acquisition dialog_SubState"""
            # talk:75601700:"Thy deeds are known to me.\nStill, there is ever more work to be done.", lot:2005012:Smooth & Silky Stone
            assert talk_m10_33_x41(text8=75601700, z23=0, lot6=2005012, z24=102962)
            Goto('L1')
        # lot:2005013:Slumbering Dragoncrest Ring
        elif (GetAreaVariable(z1) > 3) != 0 and GetEventFlag(102963) != 1 and CanGetItemLot(2005013, 1) != 1:
            """State 10: [Lib] Inventory full dialog (ranking 3) _SubState"""
            # lot:2005013:Slumbering Dragoncrest Ring
            assert talk_m10_33_x45(z19=1011, lot1=2005013)
        elif (GetAreaVariable(z1) > 3) != 0 and GetEventFlag(102963) != 1:
            """State 7: Pledge ranking 3 item acquisition dialog_SubState"""
            # talk:75601800:"My servant, well met indeed.", lot:2005013:Slumbering Dragoncrest Ring
            assert talk_m10_33_x41(text8=75601800, z23=0, lot6=2005013, z24=102963)
            Goto('L1')
        else:
            Goto('L1')
    elif (GetGlobalVariable(z9) > 1) != 0 and GetEventFlag(102961) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z9) > 2) != 0 and GetEventFlag(102962) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z9) > 3) != 0 and GetEventFlag(102963) != 1:
        Goto('L0')
    else:
        Goto('L1')
    """State 4: Pledge Ranking: End"""
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_33_x41(text8=_, z23=0, lot6=_, z24=_):
    """[Lib] Conversation: Pledge Ranking: Conversation: Menu
    text8: Ranking: Conversation ID
    z23: Ranking: Conversation flag
    lot6: Item lottery
    z24: Ranking transfer: Global event flag
    """
    """State 0,1,5: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_33_x16(action4=1308)
    """State 2: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    """State 3: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 4: Conversation: flag setting"""
    SetEventFlag(z23, 1)
    if GetEventFlag(z24) != 0:
        pass
    else:
        """State 6: Ranking item transfer_SubState"""
        assert talk_m10_33_x18(lot1=lot6, z5=z24)
    """State 7: End state"""
    return 0

def talk_m10_33_x42(text7=_, z21=_, z3=10349000, z22=-1):
    """[Lib] Conversation: For unique key guide
    text7: Conversation ID
    z21: Conversation flag
    z3: Key guide parameters
    z22: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z3)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), z22)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z21, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_33_x43(lot2=2005000, z6=102960, text1=75600300, text2=75600330, z7=0, z8=0, z3=10349000):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: UnicKey
    lot2: Item lottery ID
    z6: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    z3: Key guide parameters
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, z3)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_33_x1(text1=text1, z34=0, z55=-1, z56=0)
    if call.Done() and GetEventFlag(z6) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z7, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_33_x1(text1=text2, z34=0, z55=-1, z56=0)
    # lot:2005000:Crest of the Rat
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_33_x45(z19=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_33_x20(lot2=lot2, z6=z6, z7=z7, z8=z8, z37=0, z38=0)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_33_x44(text6=75609600, z20=0, val2=5):
    """[Lib] Death status_ (pledge cancellation)
    text6: Conversation ID
    z20: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_33_x33(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_33_x2(text6=text6, z20=z20)

def talk_m10_33_x45(z19=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z19: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_33_x46(lot1=2005000, z5=102960, z3=10349000):
    """[Lib] Conversation: Item transfer: Item: UnicKey
    lot1: Item lottery
    z5: Item transfer: Global event flag
    z3: Key guide parameters
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z3)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # lot:2005000:Crest of the Rat
    if CanGetItemLot(lot1, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_33_x45(z19=1011, lot1=lot1)
    elif GetEventFlag(z5) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_33_x18(lot1=lot1, z5=z5)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

