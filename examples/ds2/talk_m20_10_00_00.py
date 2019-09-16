# -*- coding: utf-8 -*-
def talk_m20_10_7240():
    """Kingdom commander"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_10_x9(z21=103610, z22=104110, z23=210020161)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_10_x3(text4=72409200, z13=0, z14=20, z15=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_10_x6(z19=210020162, text5=72409500, text6=72409500, z20=72409500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 9: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m20_10_x8(text7=72409300, z24=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Kingdom Captain: Conversation_SubState"""
            while True:
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
                                          z26=210020165, z27=210020166)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_10_x4(z28=103610, text13=72409100, z29=0, z30=0)
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
        talk_m20_10_x7(text8=72409600, z25=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_10_7430():
    """Tsukimitsu (Shadow Forest: 4th encounter)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_10_x9(z21=103664, z22=104160, z23=210020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m20_10_x3(text4=74309200, z13=0, z14=20, z15=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_10_x6(z19=210020102, text5=74309500, text6=74309500, z20=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_10_x7(text8=74309600, z25=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Tsukimitsu: Conversation_SubState"""
            while True:
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
                                          z26=210020105, z27=210020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(0) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m20_10_x4(z28=103660, text13=74309100, z29=0, z30=103664)
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
        talk_m20_10_x8(text7=74309300, z24=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_10_x0(text14=_, z33=_, z34=0):
    """[Lib] Conversation: General purpose
    text14: Conversation ID
    z33: Conversation flag
    z34: Global event flag
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
    SetEventFlag(z33, 1)
    SetEventFlag(z34, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_10_x1(text1=_, z29=0, z31=-1, z32=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z29: Conversation flag
    z31: Display distance
    z32: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z31)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z29, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m20_10_x2(text7=_, z24=0):
    """[Lib] Conversation: Event end
    text7: Conversation ID
    z24: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z24, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_10_x3(text4=_, z13=0, z14=20, z15=80):
    """[Lib] Reunion hostility
    text4: Conversation message ID
    z13: Conversation flag ID
    z14: Display distance
    z15: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m20_10_x17(text4=text4, z13=z13, z14=z14, z15=z15)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_10_x4(z28=_, text13=_, z29=0, z30=_):
    """[Lib] First hostility
    z28: Hostile: Global event flag
    text13: Conversation ID
    z29: Conversation flag
    z30: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z28, 1)
    SetEventFlag(z30, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z28) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m20_10_x1(text1=text13, z29=z29, z31=-1, z32=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_10_x5(text9=_, text10=_, text11=_, text12=_, z26=_, z27=_):
    """[Lib] Hostile waiting
    text9: Conversation ID: 1 attacked
    text10: Conversation ID: Attacked 2
    text11: Conversation ID: 3 attacked
    text12: Conversation ID: 4 attacked
    z26: No use: Area and other flags
    z27: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z27) != 1, z27, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z26) != 1, z26, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m20_10_x1(text1=text12, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_10_x1(text1=text11, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_10_x1(text1=text10, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_10_x1(text1=text9, z29=0, z31=-1, z32=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_10_x6(z19=_, text5=_, text6=_, z20=_):
    """[Lib] Hostile state
    z19: Area and other flags: HP decreased
    text5: Conversation ID: HP drop 1
    text6: Conversation ID: HP drop 2
    z20: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    """State 2: Hostile state: standby"""
    while True:
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z19) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m20_10_x10(text5=text5, z19=z19)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_10_x10(text5=text6, z19=z19)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_10_x10(text5=text6, z19=z19)

def talk_m20_10_x7(text8=_, z25=0):
    """[Lib] Death status
    text8: Conversation ID
    z25: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m20_10_x2(text7=text8, z24=z25)

def talk_m20_10_x8(text7=_, z24=0):
    """[Lib] Murder status
    text7: Conversation ID
    z24: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_10_x2(text7=text7, z24=z24)

def talk_m20_10_x9(z21=_, z22=_, z23=_):
    """[Lib] Event: Branch
    z21: Hostile flag
    z22: death flag
    z23: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z22) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z23) != 0
    elif GetEventFlag(z21) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m20_10_x10(text5=_, z19=_):
    """[Lib] Conversation: HP drop
    text5: Conversation ID
    z19: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text5, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z19, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_10_x11(z16=0, z17=220, z11=_, z18=0):
    """[Lib] Menu start: General purpose
    z16: Camera parameter ID
    z17: Target Damipoly ID
    z11: NPC event parameter ID
    z18: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z18, z16, z17, z11)
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

def talk_m20_10_x12(lot2=1724000, z4=102300, text2=72406000, text3=72406010, z5=0, z6=210020167, z7=0, z8=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot2: Item lottery ID
    z4: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    z7: Emigration permission: Global event flag
    z8: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m20_10_x1(text1=text2, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z4) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z5, 1)
        SetEventFlag(z7, 1)
        SetEventFlag(z8, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m20_10_x1(text1=text3, z29=0, z31=-1, z32=0)
    # lot:1724000:Drangleic Helm
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_10_x21(z9=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_10_x14(lot1=lot2, z1=z4, z2=z5, z3=z6, z7=z7, z8=z8)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m20_10_x13(lot1=1743000, z1=102420, text1=74306000, z2=0, z3=210020108):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    text1: Conversation ID
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m20_10_x1(text1=text1, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    # lot:1743000:Bluemoon Greatsword
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_10_x21(z9=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_10_x14(lot1=lot1, z1=z1, z2=z2, z3=z3, z7=0, z8=0)
    """State 9: End state"""
    return 0

def talk_m20_10_x14(lot1=_, z1=_, z2=0, z3=_, z7=0, z8=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z7: Emigration permission: Global event flag
    z8: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
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

def talk_m20_10_x17(text4=_, z13=0, z14=20, z15=80):
    """[Lib] Conversation: Hostile display only
    text4: Conversation ID
    z13: Conversation flag
    z14: Display distance
    z15: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text4, GetCommonEventParamDecimal(7), z14)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z13, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m20_10_x18(goods1=_, z10=_):
    """[Lib] Menu item: Gesture
    goods1: Gesture: Item ID
    z10: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m20_10_x20(goods1=goods1, z10=z10)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m20_10_x19(goods1=_, z10=_, z11=_, z12=_):
    """[Lib] NPC menu: Gesture alone
    goods1: Item: Event item
    z10: Item transfer: Global event flag
    z11: NPC menu: With gesture
    z12: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(z10) != 0:
        pass
    else:
        """State 3: Menu: Branch"""
        while True:
            if (ItemCount(goods1, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m20_10_x11(z16=0, z17=220, z11=z11, z18=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m20_10_x18(goods1=goods1, z10=z10)
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
        call = talk_m20_10_x11(z16=0, z17=220, z11=z12, z18=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m20_10_x20(goods1=_, z10=_):
    """[Lib] Get gesture dialog
    goods1: Item ID
    z10: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods1, 0, -1)
    SetEventFlag(z10, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_10_x21(z9=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z9: Text ID
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
        assert (talk_m20_10_x12(lot2=1724000, z4=102300, text2=72406000, text3=72406010, z5=0, z6=210020167,
                z7=0, z8=0))
    elif GetEventFlag(202504) != 0:
        """State 10: Talk to: 6_SubState"""
        # talk:72400500:"Be gone with you, this fort will soon fall."
        call = talk_m20_10_x0(text14=72400500, z33=0, z34=0)
        if call.Done() and GetEventFlag(102302) != 1:
            """State 3: Conversation: White phantom can appear"""
            SetEventFlag(102302, 1)
            if GetEventFlag(102301) != 1 and GetEventFlag(102302) != 0:
                """State 11: [Lib] NPC menu: Gesture alone_SubState"""
                Label('L0')
                # goods:63011000:"Hurrah!" Gesture
                assert talk_m20_10_x19(goods1=63011000, z10=102301, z11=72400000, z12=72400001)
            elif GetEventFlag(102302) != 0:
                pass
        elif call.Done() and GetEventFlag(102301) != 1:
            Goto('L0')
        elif call.Done():
            pass
    elif GetEventFlag(202503) != 0:
        """State 9: Talk: Part 5_SubState"""
        # talk:72400400:"Did you see him?\nThat towering monster among them."
        assert talk_m20_10_x0(text14=72400400, z33=202504, z34=0)
    elif GetEventFlag(202502) != 0:
        """State 8: Talk: 4_SubState"""
        # talk:72400300:"Long ago, the King crossed the seas,\npillaged the land of Giants, and brought back a "prize"."
        assert talk_m20_10_x0(text14=72400300, z33=202503, z34=0)
    elif GetEventFlag(202501) != 0:
        """State 7: Speak: Part 3_SubState"""
        # talk:72400200:"Soon, the Giants will descend upon this fort."
        assert talk_m20_10_x0(text14=72400200, z33=202502, z34=0)
    elif GetEventFlag(202500) != 0:
        """State 6: Talk to: 2_SubState"""
        # talk:72400100:"I am Drummond,\nand the Lord has placed this fort in my hands."
        assert talk_m20_10_x0(text14=72400100, z33=202501, z34=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:72400000:"What are you doing here?"
        assert talk_m20_10_x0(text14=72400000, z33=202500, z34=0)
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
        assert talk_m20_10_x13(lot1=1743000, z1=102420, text1=74306000, z2=0, z3=210020108)
    elif GetEventFlag(203330) != 0:
        """State 6: Talk to: 2_SubState"""
        # talk:74303100:"My homeland is in the far east.\nA kingdom of honourable fighting men."
        call = talk_m20_10_x0(text14=74303100, z33=0, z34=0)
        if call.Done() and GetEventFlag(102432) != 1:
            """State 3: Conversation: White Phantom can appear: Set flag"""
            SetEventFlag(102432, 1)
            if GetEventFlag(102435) != 1 and GetEventFlag(102432) != 0:
                """State 7: [Lib] NPC menu: Gesture alone_SubState"""
                Label('L0')
                # goods:63008000:"Joy" Gesture
                assert talk_m20_10_x19(goods1=63008000, z10=102435, z11=74300000, z12=74300001)
            elif GetEventFlag(102432) != 0:
                pass
        elif call.Done() and GetEventFlag(102435) != 1:
            Goto('L0')
        elif call.Done():
            pass
    else:
        """State 5: Talk: Part 1_SubState"""
        # talk:74303000:"Oh! Look at you! Old friend!"
        assert talk_m20_10_x0(text14=74303000, z33=203330, z34=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 8: End state"""
    return 0

