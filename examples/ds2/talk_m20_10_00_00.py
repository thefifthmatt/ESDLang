# -*- coding: utf-8 -*-
def talk_m20_10_7240():
    """Kingdom commander"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_10_x9(flag5=103610, flag6=104110, flag7=210020161)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_10_x3(text4=72409200, z10=0, z11=20, z12=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_10_x6(flag4=210020162, text5=72409500, text6=72409500, z16=72409500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 9: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m20_10_x8(text7=72409300, z17=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Kingdom Captain: Conversation_SubState"""
                call = talk_m20_10_x22()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_10_x5(text9=72409400, text10=72409410, text11=72409420, text12=72409400,
                                          flag8=210020165, flag9=210020166)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_10_x4(flag10=103610, text13=72409100, z19=0, z20=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(210020166) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(210020165) != 1:
                    Goto('L2')
        """State 8: [Lib] Death state_SubState"""
        talk_m20_10_x7(text8=72409600, z18=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m20_10_7430():
    """Tsukimitsu (Shadow Forest: 4th encounter)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_10_x9(flag5=103664, flag6=104160, flag7=210020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m20_10_x3(text4=74309200, z10=0, z11=20, z12=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_10_x6(flag4=210020102, text5=74309500, text6=74309500, z16=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_10_x7(text8=74309600, z18=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Tsukimitsu: Conversation_SubState"""
                call = talk_m20_10_x23()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(0) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_10_x5(text9=74309400, text10=74309410, text11=74309420, text12=74309400,
                                          flag8=210020105, flag9=210020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(0) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m20_10_x4(flag10=103660, text13=74309100, z19=0, z20=103664)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(0) > 2) != 0 and GetEventFlag(210020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(0) > 1) != 0 and GetEventFlag(210020105) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m20_10_x8(text7=74309300, z17=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m20_10_x0(text14=_, z23=_, z24=0):
    """[Lib] Conversation: General purpose
    text14: Conversation ID
    z23: Conversation flag
    z24: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text14, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z23, 1)
    SetEventFlag(z24, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_10_x1(text1=_, z19=0, z21=-1, z22=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z19: Conversation flag
    z21: Display distance
    z22: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z21)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z19, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m20_10_x2(text7=_, z17=0):
    """[Lib] Conversation: Event end
    text7: Conversation ID
    z17: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z17, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_10_x3(text4=_, z10=0, z11=20, z12=80):
    """[Lib] Reunion hostility
    text4: Conversation message ID
    z10: Conversation flag ID
    z11: Display distance
    z12: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m20_10_x17(text4=text4, z10=z10, z11=z11, z12=z12)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_10_x4(flag10=_, text13=_, z19=0, z20=_):
    """[Lib] First hostility
    flag10: Hostile: Global event flag
    text13: Conversation ID
    z19: Conversation flag
    z20: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag10, 1)
    SetEventFlag(z20, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag10) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m20_10_x1(text1=text13, z19=z19, z21=-1, z22=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_10_x5(text9=_, text10=_, text11=_, text12=_, flag8=_, flag9=_):
    """[Lib] Hostile waiting
    text9: Conversation ID: 1 attacked
    text10: Conversation ID: Attacked 2
    text11: Conversation ID: 3 attacked
    text12: Conversation ID: 4 attacked
    flag8: No use: Area and other flags
    flag9: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag9) != 1, flag9, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag8) != 1, flag8, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m20_10_x1(text1=text12, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_10_x1(text1=text11, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_10_x1(text1=text10, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_10_x1(text1=text9, z19=0, z21=-1, z22=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_10_x6(flag4=_, text5=_, text6=_, z16=_):
    """[Lib] Hostile state
    flag4: Area and other flags: HP decreased
    text5: Conversation ID: HP drop 1
    text6: Conversation ID: HP drop 2
    z16: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag4) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m20_10_x10(text5=text5, flag4=flag4)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_10_x10(text5=text6, flag4=flag4)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_10_x10(text5=text6, flag4=flag4)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m20_10_x7(text8=_, z18=0):
    """[Lib] Death status
    text8: Conversation ID
    z18: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m20_10_x2(text7=text8, z17=z18)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m20_10_x8(text7=_, z17=0):
    """[Lib] Murder status
    text7: Conversation ID
    z17: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_10_x2(text7=text7, z17=z17)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m20_10_x9(flag5=_, flag6=_, flag7=_):
    """[Lib] Event: Branch
    flag5: Hostile flag
    flag6: death flag
    flag7: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag6) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag7) != 0
    elif GetEventFlag(flag5) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m20_10_x10(text5=_, flag4=_):
    """[Lib] Conversation: HP drop
    text5: Conversation ID
    flag4: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text5, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag4, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_10_x11(z13=0, z14=220, z8=_, z15=0):
    """[Lib] Menu start: General purpose
    z13: Camera parameter ID
    z14: Target Damipoly ID
    z8: NPC event parameter ID
    z15: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z15, z13, z14, z8)
    """State 3: Menu start: Standby"""
    Label('L0')
    if (NpcMenuResult() == 19) != 0:
        """State 6: Cancel: End state"""
        return 0
    elif (NpcMenuResult() == 18) != 0:
        """State 7: Normal: End state"""
        Label('L1')
        return 1
    elif (NpcMenuResult() == 17) != 0:
        Goto('L1')
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
    """Unused"""
    """State 4: Menu start: Shop waiting"""
    Label('L2')
    Goto('L0')
    """State 5: Menu start: Shop start"""
    ClearNpcMenuSelection()
    Goto('L2')

def talk_m20_10_x12(lot2=1724000, flag2=102300, text2=72406000, text3=72406010, z3=0, z4=210020167, z5=0,
                    z6=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot2: Item lottery ID
    flag2: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z3: Conversation: Global conversation flag
    z4: Trophy acquisition: Area and other flags
    z5: Emigration permission: Global event flag
    z6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m20_10_x1(text1=text2, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag2) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z3, 1)
        SetEventFlag(z5, 1)
        SetEventFlag(z6, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m20_10_x1(text1=text3, z19=0, z21=-1, z22=0)
    # lot:1724000:Drangleic Helm
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_10_x21(z7=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_10_x14(lot1=lot2, flag1=flag2, z1=z3, z2=z4, z5=z5, z6=z6)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m20_10_x13(lot1=1743000, flag1=102420, text1=74306000, z1=0, z2=210020108):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    text1: Conversation ID
    z1: Conversation: Global conversation flag
    z2: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m20_10_x1(text1=text1, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z1, 1)
    # lot:1743000:Bluemoon Greatsword
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_10_x21(z7=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_10_x14(lot1=lot1, flag1=flag1, z1=z1, z2=z2, z5=0, z6=0)
    """State 9: End state"""
    return 0

def talk_m20_10_x14(lot1=_, flag1=_, z1=0, z2=_, z5=0, z6=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    z1: Conversation: Global conversation flag
    z2: Trophy acquisition: Area and other flags
    z5: Emigration permission: Global event flag
    z6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z6, 1)
    SetEventFlag(z5, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
    SetEventFlag(flag1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_10_x15():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m20_10_x16():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_10_x17(text4=_, z10=0, z11=20, z12=80):
    """[Lib] Conversation: Hostile display only
    text4: Conversation ID
    z10: Conversation flag
    z11: Display distance
    z12: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text4, GetCommonEventParamDecimal(7), z11)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z10, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m20_10_x18(goods1=_, flag3=_):
    """[Lib] Menu item: Gesture
    goods1: Gesture: Item ID
    flag3: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m20_10_x20(goods1=goods1, flag3=flag3)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m20_10_x19(goods1=_, flag3=_, z8=_, z9=_):
    """[Lib] NPC menu: Gesture alone
    goods1: Item: Event item
    flag3: Item transfer: Global event flag
    z8: NPC menu: With gesture
    z9: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(flag3) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            if (ItemCount(goods1, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m20_10_x11(z13=0, z14=220, z8=z8, z15=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m20_10_x18(goods1=goods1, flag3=flag3)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        pass
                elif call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    """State 6: [Lib] Menu exit: No Mes_SubState"""
                    Label('L0')
                    assert talk_m20_10_x15()
                    Goto('L2')
            """State 7: [Lib] Menu canceled: No Mes_SubState"""
            Label('L1')
            assert talk_m20_10_x16()
            Goto('L2')
        """State 5: [Lib] Menu start: No gesture _SubState"""
        call = talk_m20_10_x11(z13=0, z14=220, z8=z9, z15=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m20_10_x20(goods1=_, flag3=_):
    """[Lib] Get gesture dialog
    goods1: Item ID
    flag3: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods1, 0, -1)
    SetEventFlag(flag3, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_10_x21(z7=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z7: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_10_x22():
    """Kingdom Captain: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetEventFlag(100972) != 0 and GetEventFlag(102300) != 1 and GetEventFlag(104110) != 1 and GetEventFlag(202504)
        != 0):
        """State 5: Equipment transfer (Conditions: Defeat Giant King (New Giant Senior Soldier)) _ SubState"""
        # lot:1724000:Drangleic Helm, talk:72406000:"Matters are settled..."
        assert (talk_m20_10_x12(lot2=1724000, flag2=102300, text2=72406000, text3=72406010, z3=0, z4=210020167,
                z5=0, z6=0))
    elif GetEventFlag(202504) != 0:
        """State 10: Talk to: 6_SubState"""
        # talk:72400500:"Be gone with you, this fort will soon fall."
        call = talk_m20_10_x0(text14=72400500, z23=0, z24=0)
        if call.Done() and GetEventFlag(102302) != 1:
            """State 3: Conversation: White phantom can appear"""
            SetEventFlag(102302, 1)
            if GetEventFlag(102301) != 1 and GetEventFlag(102302) != 0:
                """State 11: [Lib] NPC menu: Gesture alone_SubState"""
                Label('L0')
                # goods:63011000:"Hurrah!" Gesture
                assert talk_m20_10_x19(goods1=63011000, flag3=102301, z8=72400000, z9=72400001)
            elif GetEventFlag(102302) != 0:
                pass
        elif call.Done() and GetEventFlag(102301) != 1:
            Goto('L0')
        elif call.Done():
            pass
    elif GetEventFlag(202503) != 0:
        """State 9: Talk: Part 5_SubState"""
        # talk:72400400:"Did you see him?\nThat towering monster among them."
        assert talk_m20_10_x0(text14=72400400, z23=202504, z24=0)
    elif GetEventFlag(202502) != 0:
        """State 8: Talk: 4_SubState"""
        # talk:72400300:"Long ago, the King crossed the seas,\npillaged the land of Giants, and brought back a "prize"."
        assert talk_m20_10_x0(text14=72400300, z23=202503, z24=0)
    elif GetEventFlag(202501) != 0:
        """State 7: Speak: Part 3_SubState"""
        # talk:72400200:"Soon, the Giants will descend upon this fort."
        assert talk_m20_10_x0(text14=72400200, z23=202502, z24=0)
    elif GetEventFlag(202500) != 0:
        """State 6: Talk to: 2_SubState"""
        # talk:72400100:"I am Drummond,\nand the Lord has placed this fort in my hands."
        assert talk_m20_10_x0(text14=72400100, z23=202501, z24=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:72400000:"What are you doing here?"
        assert talk_m20_10_x0(text14=72400000, z23=202500, z24=0)
    """State 2,12: End state"""
    return 0

def talk_m20_10_x23():
    """Moonlight Jun: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetEventFlag(102420) != 1 and GetEventFlag(102436) != 0 and GetEventFlag(104160) != 1 and GetEventFlag(203330)
        != 0):
        """State 4: Equipment transfer (Condition: White Phantom Summon? Achieved times) _SubState"""
        # lot:1743000:Bluemoon Greatsword, talk:74306000:"A man's journey...is never done..."
        assert talk_m20_10_x13(lot1=1743000, flag1=102420, text1=74306000, z1=0, z2=210020108)
    elif GetEventFlag(203330) != 0:
        """State 6: Talk to: 2_SubState"""
        # talk:74303100:"My homeland is in the far east.\nA kingdom of honourable fighting men."
        call = talk_m20_10_x0(text14=74303100, z23=0, z24=0)
        if call.Done() and GetEventFlag(102432) != 1:
            """State 3: Conversation: White Phantom can appear: Set flag"""
            SetEventFlag(102432, 1)
            if GetEventFlag(102435) != 1 and GetEventFlag(102432) != 0:
                """State 7: [Lib] NPC menu: Gesture alone_SubState"""
                Label('L0')
                # goods:63008000:"Joy" Gesture
                assert talk_m20_10_x19(goods1=63008000, flag3=102435, z8=74300000, z9=74300001)
            elif GetEventFlag(102432) != 0:
                pass
        elif call.Done() and GetEventFlag(102435) != 1:
            Goto('L0')
        elif call.Done():
            pass
    else:
        """State 5: Talk: Part 1_SubState"""
        # talk:74303000:"Oh! Look at you! Old friend!"
        assert talk_m20_10_x0(text14=74303000, z23=203330, z24=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 8: End state"""
    return 0

