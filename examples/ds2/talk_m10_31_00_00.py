# -*- coding: utf-8 -*-
def talk_m10_31_7690():
    """Miraculous person"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_31_x9(z40=103821, z41=104320, z42=131020111)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_31_x3(text9=76909200, z27=0, z28=20, z29=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_31_x6(z38=131020112, text14=76909500, text15=76909500, z39=76909500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_31_x7(text17=76909600, z44=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                Goto('L1')
            elif KilledPlayer() != 0:
                pass
        elif call.Get() == 0:
            """State 10: Miracle People: Conversation_SubState"""
            while True:
                call = talk_m10_31_x39()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif KilledPlayer() != 0:
                    break
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_31_x5(text18=76909400, text19=76909410, text20=76909420, text21=76909400,
                                          z45=131020115, z46=131020116)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif KilledPlayer() != 0:
                        break
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_31_x4(z47=103820, text22=76909100, z48=0, z49=103821)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(131020116) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(131020115) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_31_x8(text16=76909300, z43=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_31_7850():
    """Guardian knight"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_31_x9(z40=103900, z41=104400, z42=131020011)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_31_x3(text9=78509200, z27=0, z28=20, z29=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_31_x6(z38=131020012, text14=78509500, text15=78509500, z39=78509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m10_31_x30(text8=78509600, z18=0, val2=2)
                    Quit()
            elif (HpValue() > 1) != 1:
                Goto('L1')
            elif KilledPlayer() != 0:
                pass
        elif call.Get() == 0:
            """State 9: Guardian Knight: Conversation_SubState"""
            while True:
                call = talk_m10_31_x32()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif KilledPlayer() != 0:
                    break
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_31_x5(text18=78509400, text19=78509410, text20=78509420, text21=78509400,
                                          z45=131020015, z46=131020016)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif KilledPlayer() != 0:
                        break
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 6: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_31_x15(z30=103900, text10=78509100, z31=0, val3=2, z32=200901,
                                               z33=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(131020016) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(131020015) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_31_x8(text16=78509300, z43=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_31_x0(text23=_, z52=_, z53=0):
    """[Lib] Conversation: General purpose
    text23: Conversation ID
    z52: Conversation flag
    z53: Global event flag
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
    SetEventFlag(z52, 1)
    SetEventFlag(z53, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_31_x1(text1=_, z31=_, z50=-1, z51=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z31: Conversation flag
    z50: Display distance
    z51: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z50)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z31, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_31_x2(text8=_, z18=0):
    """[Lib] Conversation: Event end
    text8: Conversation ID
    z18: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_31_x3(text9=_, z27=0, z28=20, z29=80):
    """[Lib] Reunion hostility
    text9: Conversation message ID
    z27: Conversation flag ID
    z28: Display distance
    z29: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_31_x24(text9=text9, z27=z27, z28=z28, z29=z29)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_31_x4(z47=103820, text22=76909100, z48=0, z49=103821):
    """[Lib] First hostility
    z47: Hostile: Global event flag
    text22: Conversation ID
    z48: Conversation flag
    z49: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z47, 1)
    SetEventFlag(z49, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z47) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_31_x1(text1=text22, z31=z48, z50=-1, z51=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_31_x5(text18=_, text19=_, text20=_, text21=_, z45=_, z46=_):
    """[Lib] Hostile waiting
    text18: Conversation ID: 1 attacked
    text19: Conversation ID: Attacked 2
    text20: Conversation ID: 3 attacked
    text21: Conversation ID: 4 attacked
    z45: No use: Area and other flags
    z46: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z46) != 1, z46, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z45) != 1, z45, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_31_x1(text1=text21, z31=0, z50=-1, z51=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_31_x1(text1=text20, z31=0, z50=-1, z51=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_31_x1(text1=text19, z31=0, z50=-1, z51=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_31_x1(text1=text18, z31=0, z50=-1, z51=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_31_x6(z38=_, text14=_, text15=_, z39=_):
    """[Lib] Hostile state
    z38: Area and other flags: HP decreased
    text14: Conversation ID: HP drop 1
    text15: Conversation ID: HP drop 2
    z39: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    """State 2: Hostile state: standby"""
    while True:
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z38) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_31_x10(text14=text14, z38=z38)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_31_x10(text14=text15, z38=z38)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_31_x10(text14=text15, z38=z38)

def talk_m10_31_x7(text17=76909600, z44=0):
    """[Lib] Death status
    text17: Conversation ID
    z44: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_31_x2(text8=text17, z18=z44)

def talk_m10_31_x8(text16=_, z43=0):
    """[Lib] Murder status
    text16: Conversation ID
    z43: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_31_x2(text8=text16, z18=z43)

def talk_m10_31_x9(z40=_, z41=_, z42=_):
    """[Lib] Event: Branch
    z40: Hostile flag
    z41: death flag
    z42: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z41) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z42) != 0
    elif GetEventFlag(z40) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_31_x10(text14=_, z38=_):
    """[Lib] Conversation: HP drop
    text14: Conversation ID
    z38: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text14, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z38, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_31_x11(action1=_):
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

def talk_m10_31_x12(z34=0, z35=220, z36=_, z37=0):
    """[Lib] Menu start: General purpose
    z34: Camera parameter ID
    z35: Target Damipoly ID
    z36: NPC event parameter ID
    z37: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z37, z34, z35, z36)
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

def talk_m10_31_x13(text12=_, text13=_):
    """[Lib] Menu exit: General purpose
    text12: Conversation ID (at the time of purchase)
    text13: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_31_x1(text1=text12, z31=0, z50=-1, z51=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_31_x1(text1=text13, z31=0, z50=-1, z51=0)
    """State 4: End state"""
    return 0

def talk_m10_31_x14(text11=_):
    """[Lib] Menu cancellation: General purpose
    text11: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_31_x1(text1=text11, z31=0, z50=-1, z51=0)
    """State 4: End state"""
    return 0

def talk_m10_31_x15(z30=103900, text10=78509100, z31=0, val3=2, z32=200901, z33=0):
    """[Lib] First hostility _ (pledge cancellation)
    z30: Hostile: Global event flag
    text10: Conversation ID
    z31: Conversation flag
    val3: Cancellation pledge name
    z32: Pledge cancellation: Global conversation flag
    z33: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z30, 1)
    SetEventFlag(z33, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z30) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_31_x23(val2=val3)
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
    assert talk_m10_31_x1(text1=text10, z31=z31, z50=-1, z51=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_31_x16(text7=_, z13=0, lot5=_, z14=_, z15=211, z16=60):
    """[Lib] Conversation: Pledge ranking
    text7: Ranking: Conversation ID
    z13: Ranking: Conversation flag
    lot5: Item lottery
    z14: Ranking transfer: Global event flag
    z15: Previous rank: Global variable
    z16: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_31_x17(action3=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z13, 1)
    if CanGetItemLot(lot5, 1) != 1 and GetEventFlag(z14) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_31_x31(z17=1011, lot1=lot5)
    elif GetEventFlag(z14) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_31_x19(lot4=lot5, z12=z14)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z15, GetAreaVariable(z16))
    """State 11: End state"""
    return 0

def talk_m10_31_x17(action3=_):
    """[Lib] OK dialog
    action3: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action3, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_31_x18(lot4=1769000, z12=102760, text5=76906000, text6=76906010):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z12: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_31_x1(text1=text5, z31=0, z50=-1, z51=0)
    # lot:1769000:Idol's Chime
    if call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_31_x31(z17=1011, lot1=lot4)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_31_x19(lot4=lot4, z12=z12)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_31_x1(text1=text6, z31=0, z50=-1, z51=0)
    """State 6: End state"""
    return 0

def talk_m10_31_x19(lot4=_, z12=_):
    """[Lib] Item acquisition dialog
    lot4: Item lottery ID
    z12: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z12, 1)
    AwardItem(lot4, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_31_x20(lot3=2002000, z7=102920, text3=78500300, text4=78500320, z8=0, z9=0, z10=0, z11=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot3: Item lottery ID
    z7: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z8: Conversation: Global conversation flag
    z9: Trophy acquisition: Area and other flags
    z10: Emigration permission: Global event flag
    z11: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_31_x1(text1=text3, z31=0, z50=-1, z51=0)
    if call.Done() and GetEventFlag(z7) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z8, 1)
        SetEventFlag(z10, 1)
        SetEventFlag(z11, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_31_x1(text1=text4, z31=0, z50=-1, z51=0)
    # lot:2002000:Guardian's Seal
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_31_x31(z17=1011, lot1=lot3)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_31_x21(lot2=lot3, z4=z7, z5=z8, z6=z9, z10=z10, z11=z11)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_31_x21(lot2=_, z4=_, z5=0, z6=0, z10=0, z11=0):
    """[Lib] Item acquisition dialog: Conversation
    lot2: Item lottery ID
    z4: Item transfer: Global event flag
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    z10: Emigration permission: Global event flag
    z11: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z11, 1)
    SetEventFlag(z10, 1)
    SetEventFlag(z6, 1)
    SetEventFlag(z5, 1)
    SetEventFlag(z4, 1)
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_31_x22(lot2=_, z4=_, text1=_, text2=_, z5=0, z6=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot2: Item lottery ID
    z4: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_31_x1(text1=text1, z31=0, z50=-1, z51=0)
    if call.Done() and GetEventFlag(z4) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z5, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_31_x1(text1=text2, z31=0, z50=-1, z51=0)
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_31_x31(z17=1011, lot1=lot2)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_31_x21(lot2=lot2, z4=z4, z5=z5, z6=z6, z10=0, z11=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_31_x23(val2=2):
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

def talk_m10_31_x24(text9=_, z27=0, z28=20, z29=80):
    """[Lib] Conversation: Hostile display only
    text9: Conversation ID
    z27: Conversation flag
    z28: Display distance
    z29: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), z28)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z27, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_31_x25(z19=63005000, z20=0):
    """[Lib] Menu item: Gesture
    z19: Gesture: Item ID
    z20: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_31_x29(z19=z19, z20=z20)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_31_x26(val1=2, z1=8, lot1=0, z2=0, action1=1331, action2=1341, z3=131020017):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z1: Event action
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z3, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_31_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_31_x17(action3=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_31_x27(z1=z1, val1=val1, lot1=lot1, z2=z2) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_31_x17(action3=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_31_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_31_x23(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_31_x27(z1=8, val1=2, lot1=0, z2=0):
    """[Lib] Event action: Pledge
    z1: Event action
    val1: Pledge type
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z1)
    assert PlayerIsInEventAction(z1) != 0
    """State 3: IventAction: Motion_Waiting"""
    # lot:0:No Item
    if PlayerIsInEventAction(z1) != 1 and CanGetItemLot(lot1, 1) != 1 and GetEventFlag(z2) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        # lot:0:No Item
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot1, 1) != 1 and GetEventFlag(z2) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_31_x31(z17=1011, lot1=lot1)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z1) != 1 and GetEventFlag(z2) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z1) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z2, 1)
        # lot:0:No Item
        AwardItem(lot1, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z1) != 1
    """State 8: End state"""
    return 0

def talk_m10_31_x28(z21=2, z22=60, z23=211, z24=102921, z25=102922, z26=102923):
    """[Lib] Pledge: Rank up: Conversation: 1
    z21: Pledge: Pledge type
    z22: Current rank: Area variable
    z23: Previous rank: Global variable
    z24: Ranking 1: Item transfer: Global event flag
    z25: Ranking 2: Item transfer: Global event flag
    z26: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z22, GetPlayerCovenantLevel(z21))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z23) > GetAreaVariable(z22)) != 1 and (GetGlobalVariable(z23) == GetAreaVariable(z22))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z23) > GetAreaVariable(z22)) != 0 and (GetGlobalVariable(z23) == GetAreaVariable(z22))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z23, GetAreaVariable(z22))
    elif GetEventFlag(z24) != 1 and (GetGlobalVariable(z23) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(z25) != 1 and (GetGlobalVariable(z23) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(z26) != 1 and (GetGlobalVariable(z23) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_31_x29(z19=63005000, z20=0):
    """[Lib] Get gesture dialog
    z19: Item ID
    z20: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(z19, 0, -1)
    SetEventFlag(z20, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_31_x30(text8=78509600, z18=0, val2=2):
    """[Lib] Death status_ (pledge cancellation)
    text8: Conversation ID
    z18: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_31_x23(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_31_x2(text8=text8, z18=z18)

def talk_m10_31_x31(z17=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z17: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_31_x32():
    """Guardian Knight: Conversation"""
    """State 0,1: Conversation: Start"""
    while True:
        ClearNpcMenuResults()
        if (GetPlayerCovenant() == 2) != 0:
            """State 6: Guardian Knight: Pledge Conversation_SubState"""
            call = talk_m10_31_x35()
            if call.Get() == 0:
                """State 4: Guardian Knight: NPC Menu_SubState"""
                Label('L0')
                assert talk_m10_31_x37()
            elif call.Get() == 1:
                pass
        elif GetEventFlag(200901) != 0:
            break
        # goods:62100000:Token of Fidelity
        elif (ItemCount(62100000, 1, 1, 0) > 1) != 0:
            """State 7: Guardian Knight: Uncontracted Conversation_SubState"""
            call = talk_m10_31_x34()
            if call.Done():
                pass
            # goods:62100000:Token of Fidelity
            elif GetEventFlag(102920) != 1 and (ItemCount(62100000, 1, 1, 0) > 1) != 1:
                continue
        else:
            """State 3: Guardian Knight: Proof of Goodwill: Not Owned_SubState"""
            assert talk_m10_31_x33()
        """State 2: Conversation: End"""
        Label('L1')
        ClearNpcMenuResults()
        """State 8: End state"""
        return 0
    """State 5: Guardian Knight: Re-contract conversation_SubState"""
    call = talk_m10_31_x38()
    if call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L1')

def talk_m10_31_x33():
    """Guardian Knight: Proof of Goodwill: Not Owned"""
    """State 0,2: First look: Start"""
    if GetEventFlag(205800) != 0:
        """State 4: If you don't have good faith: loop _SubState"""
        # talk:78500100:"Transient being, nothing has changed."
        call = talk_m10_31_x0(text23=78500100, z52=0, z53=0)
        if call.Done():
            pass
        # goods:62100000:Token of Fidelity
        elif (ItemCount(62100000, 1, 1, 0) > 1) != 0:
            """State 1: First look: Delete key guide"""
            Label('L0')
            DeleteKeyGuideArea()
    else:
        """State 3: If you do n’t have a good faith proof: First Look _SubState"""
        # talk:78500000:"Transient being."
        call = talk_m10_31_x0(text23=78500000, z52=205800, z53=0)
        if call.Done():
            pass
        # goods:62100000:Token of Fidelity
        elif (ItemCount(62100000, 1, 1, 0) > 1) != 0:
            Goto('L0')
    """State 5: End state"""
    return 0

def talk_m10_31_x34():
    """Guardian Knight: Uncontracted Conversation"""
    """State 0,1: Uncontracted conversation: Start"""
    if GetEventFlag(205801) != 0:
        """State 5: If you have a good will: First look: YES / NO dialog: NO selection: First look _SubState"""
        # talk:78500500:"You are a wandering transient."
        assert talk_m10_31_x0(text23=78500500, z52=0, z53=0)
    else:
        """State 4: If you have a proof of good faith: First Look _SubState"""
        # talk:78500200:"Transient being."
        assert talk_m10_31_x0(text23=78500200, z52=205801, z53=0)
    """State 6: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item, action:1331:"Join the Blue Sentinels covenant?", action:1341:"Abandon your covenant and\njoin the Blue Sentinels?"
    call = talk_m10_31_x26(val1=2, z1=8, lot1=0, z2=0, action1=1331, action2=1341, z3=131020017)
    if call.Get() == 1:
        """State 7: If you have good faith: YES / NO dialog: YES_SubState"""
        # lot:2002000:Guardian's Seal, talk:78500300:"You are no longer a mere vagabond.\nYou are now a guardian, a Knight of the Blue.", talk:78500320:"Wear this ring, and shine light upon stone."
        assert talk_m10_31_x22(lot2=2002000, z4=102920, text1=78500300, text2=78500320, z5=0, z6=0)
    elif call.Get() == 0 and GetEventFlag(205802) != 0:
        """State 3: If you have a good will: After selecting NO: YES / NO dialog: Select NO_SubState"""
        # talk:78500600:"Ohh Gods...have mercy..."
        assert talk_m10_31_x1(text1=78500600, z31=0, z50=-1, z51=0)
    elif call.Get() == 0:
        """State 2: If you have good faith: YES / NO dialog: NO: First Look _SubState"""
        # talk:78500400:"Do my ears deceive me?"
        assert talk_m10_31_x1(text1=78500400, z31=205802, z50=-1, z51=0)
    """State 8: End state"""
    return 0

def talk_m10_31_x35():
    """Guardian Knight: Pledge Conversation"""
    """State 0,1: Pledge conversation: start"""
    if GetEventFlag(102920) != 1:
        """State 4: When ring is not transferred: Insurance_SubState"""
        # lot:2002000:Guardian's Seal, talk:78500300:"You are no longer a mere vagabond.\nYou are now a guardian, a Knight of the Blue.", talk:78500320:"Wear this ring, and shine light upon stone."
        assert (talk_m10_31_x20(lot3=2002000, z7=102920, text3=78500300, text4=78500320, z8=0, z9=0,
                z10=0, z11=0))
    else:
        """State 5: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m10_31_x28(z21=2, z22=60, z23=211, z24=102921, z25=102922, z26=102923)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(60) > 1) != 0 and GetEventFlag(102921) != 1:
                """State 6: Conversation: Pledge Ranking 1_SubState"""
                # talk:78506000:"Brave knight...be proud.", lot:2002011:Spirit Tree Shield
                assert talk_m10_31_x16(text7=78506000, z13=0, lot5=2002011, z14=102921, z15=211, z16=60)
                Goto('L0')
            elif (GetAreaVariable(60) > 2) != 0 and GetEventFlag(102922) != 1:
                """State 7: Conversation: Pledge Ranking 2_SubState"""
                # lot:2002012:Wrath of the Gods
                assert talk_m10_31_x16(text7=78506100, z13=0, lot5=2002012, z14=102922, z15=211, z16=60)
                Goto('L0')
            elif (GetAreaVariable(60) > 3) != 0 and GetEventFlag(102923) != 1:
                """State 8: Conversation: Pledge Ranking 3_SubState"""
                # lot:2002013:Bountiful Sunlight
                assert talk_m10_31_x16(text7=78506200, z13=0, lot5=2002013, z14=102923, z15=211, z16=60)
                Goto('L0')
            else:
                pass
        elif call.Get() == 0:
            pass
        """State 3: After pledge contract_SubState"""
        # talk:78500700:"Proud knight, you may come to me, Targray, for help."
        assert talk_m10_31_x0(text23=78500700, z52=0, z53=0)
        """State 9: Menu: Exit state"""
        return 0
    """State 10: Normal: End state"""
    Label('L0')
    return 1

def talk_m10_31_x36():
    """Guardian Knight: Menu Conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102930) != 1 and (GetPlayerCovenantLevel(2) > 3) != 0 and GetEventFlag(104400) != 1:
        """State 7: Equipment transfer (condition: pledge level MAX) _SubState"""
        # lot:1785040:Targray's Helm
        assert talk_m10_31_x22(lot2=1785040, z4=102930, text1=78506300, text2=78506310, z5=0, z6=0)
    elif GetEventFlag(205812) != 0:
        """State 2: Menu conversation: flag clear"""
        SetEventFlag(205810, 0)
        SetEventFlag(205811, 0)
        SetEventFlag(205812, 0)
        """State 4: NPC menu conversation_part1_SubState"""
        Label('L0')
        # talk:78505000:"You are my greatest challenge."
        assert talk_m10_31_x1(text1=78505000, z31=205810, z50=-1, z51=0)
    elif GetEventFlag(205811) != 0:
        """State 6: NPC Menu Conversation_Part 3_SubState"""
        assert talk_m10_31_x1(text1=78505200, z31=205812, z50=-1, z51=0)
    elif GetEventFlag(205810) != 0:
        """State 5: NPC menu conversation_2_SubState"""
        assert talk_m10_31_x1(text1=78505100, z31=205811, z50=-1, z51=0)
    else:
        Goto('L0')
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m10_31_x37():
    """Guardian Knight: NPC Menu"""
    """State 0,2: Menu: Start"""
    ClearNpcMenuResults()
    """State 3: Menu: Branch"""
    while True:
        # goods:63005000:"Duel bow" Gesture
        if (ItemCount(63005000, 1, 1, 0) > 1) != 0:
            """State 8: [Lib] Menu start: No gesture _SubState"""
            call = talk_m10_31_x12(z34=0, z35=220, z36=78500001, z37=0)
            if call.Get() == 2:
                """State 4: Guardian Knight: Menu Conversation_SubState"""
                Label('L0')
                call = talk_m10_31_x36()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 6: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:78501000:"There are others in this forsaken place\nwho have only a lust for blood.", talk:78501100:"Ooh... Ooooh... Unthinkable..."
                assert talk_m10_31_x13(text12=78501000, text13=78501100)
        else:
            """State 7: [Lib] Menu start: With gesture_SubState"""
            call = talk_m10_31_x12(z34=0, z35=220, z36=78500000, z37=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 9: [Lib] Menu item: Gesture_SubState"""
                call = talk_m10_31_x25(z19=63005000, z20=0)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L1')
        """State 1: Menu: Exit"""
        Label('L2')
        ClearNpcMenuResults()
        """State 10: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:78501200:"Be gone... There is no mercy for your kind."
    assert talk_m10_31_x14(text11=78501200)
    Goto('L2')

def talk_m10_31_x38():
    """Guardian Knight: Recontracted conversation"""
    """State 0,1: Re-contract conversation: start"""
    if GetEventFlag(205820) != 0:
        """State 3: After pledge cancellation: Loop _SubState"""
        # talk:78500500:"You are a wandering transient."
        assert talk_m10_31_x0(text23=78500500, z52=0, z53=0)
    else:
        """State 2: After vow cancellation: First look _SubState"""
        # talk:78500500:"You are a wandering transient."
        assert talk_m10_31_x0(text23=78500500, z52=205820, z53=0)
    """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item, action:1331:"Join the Blue Sentinels covenant?", action:1341:"Abandon your covenant and\njoin the Blue Sentinels?"
    call = talk_m10_31_x26(val1=2, z1=8, lot1=0, z2=0, action1=1331, action2=1341, z3=131020017)
    if call.Get() == 0:
        """State 6: Normal: End state"""
        return 0
    elif call.Get() == 1 and GetEventFlag(102920) != 1:
        """State 5: When ring is not transferred: Insurance_SubState"""
        # lot:2002000:Guardian's Seal, talk:78500300:"You are no longer a mere vagabond.\nYou are now a guardian, a Knight of the Blue.", talk:78500320:"Wear this ring, and shine light upon stone."
        assert (talk_m10_31_x20(lot3=2002000, z7=102920, text3=78500300, text4=78500320, z8=0, z9=0,
                z10=0, z11=0))
    elif call.Get() == 1:
        pass
    """State 7: Menu: Exit state"""
    return 1

def talk_m10_31_x39():
    """Miracle: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Miracle: First conversation_SubState"""
    assert talk_m10_31_x40()
    """State 4: Miracle: NPC Menu_SubState"""
    assert talk_m10_31_x41()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_31_x40():
    """Miracle: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(205000) != 0:
        """State 3: Talk: First time 2_SubState"""
        # talk:76901100:"Just speak up if you're in need of miracles."
        assert talk_m10_31_x0(text23=76901100, z52=0, z53=0)
    else:
        """State 2: Talk: First 1_SubState"""
        # talk:76900000:"Are you from these parts?"
        assert talk_m10_31_x0(text23=76900000, z52=205000, z53=0)
    """State 4: End state"""
    return 0

def talk_m10_31_x41():
    """Miracles: NPC menu"""
    """State 0,2: Menu: Start"""
    ClearNpcMenuResults()
    """State 5: [Lib] Menu start: General purpose_SubState"""
    while True:
        call = talk_m10_31_x12(z34=0, z35=220, z36=76900001, z37=0)
        if call.Get() == 2:
            """State 6: Miracle: Menu conversation_SubState"""
            call = talk_m10_31_x42()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Exit menu: General purpose_SubState"""
            # talk:76901300:"May the power of miracles be with you.", talk:76901400:"No need for miracles?"
            assert talk_m10_31_x13(text12=76901300, text13=76901400)
        """State 1: Menu: Exit"""
        Label('L0')
        ClearNpcMenuResults()
        """State 7: End state"""
        return 0
    """State 3: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76901500:"Oh? Done so soon?"
    assert talk_m10_31_x14(text11=76901500)
    Goto('L0')

def talk_m10_31_x42():
    """Miracle: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102760) != 1 and (GetPlayerStat(6, 1) > NpcInfoValue(7690, 3)) != 0 and GetEventFlag(104320)
        != 1):
        """State 8: Equipment transfer (Condition: Belief over a certain level) _SubState"""
        # lot:1769000:Idol's Chime, talk:76906000:"Seek...miracles..."
        assert talk_m10_31_x18(lot4=1769000, z12=102760, text5=76906000, text6=76906010)
    elif GetEventFlag(205012) != 0:
        """State 7: Menu conversation: 4_SubState"""
        # talk:76900400:"I expected this cathedral to be bustling,\nbut there's hardly a soul to be found here."
        assert talk_m10_31_x1(text1=76900400, z31=0, z50=-1, z51=0)
        """State 3: Menu conversation: Set migration permission flag"""
        SetEventFlag(102765, 1)
        assert GetEventFlag(102765) != 0
    elif GetEventFlag(205011) != 0:
        """State 6: Menu conversation: 3_SubState"""
        # talk:76900300:"Sometimes I fight the urge\nto pack up and go back home."
        assert talk_m10_31_x1(text1=76900300, z31=205012, z50=-1, z51=0)
    elif GetEventFlag(205010) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:76900200:"Why did I come here?\nWell..."
        assert talk_m10_31_x1(text1=76900200, z31=205011, z50=-1, z51=0)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:76900100:"I'd heard awful rumours about this place,\nand I'm afraid they were all true."
        assert talk_m10_31_x1(text1=76900100, z31=205010, z50=-1, z51=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

