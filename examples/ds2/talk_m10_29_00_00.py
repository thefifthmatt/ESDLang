# -*- coding: utf-8 -*-
def talk_m10_29_7430():
    """Tsukimitsu (Connection between Madura and Kagenomori): first encounter)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_29_x9(flag4=103661, flag5=104161, flag6=129020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_29_x3(text2=74309200, z6=0, z7=20, z8=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_29_x6(flag3=129020102, text6=74309500, text7=74309500, z14=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_29_x7(text9=74309600, z16=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Tsukimitsu: Conversation_SubState"""
                call = talk_m10_29_x23()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_29_x5(text10=74309400, text11=74309410, text12=74309420, text13=74309400,
                                          flag7=129020105, flag8=129020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_29_x4(flag9=103660, text14=74309100, z17=0, z18=103661)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(129020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(129020105) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_29_x8(text8=74309300, z15=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_29_7630():
    """Sorcerer (Madura and Shadow Forest connection)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(129010110) != 0:
            pass
        else:
            """State 3: Waiting for petrochemical release"""
            assert (GetCurrentActivationState() == 16) != 0
            """State 4: Petrochemical release: damage reset"""
            ResetDamageTakenCount()
        """State 5: [Lib] Event: Branch_SubState"""
        call = talk_m10_29_x9(flag4=103771, flag5=104271, flag6=129020111)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            # talk:76305010:"I won't let you do this..."
            call = talk_m10_29_x3(text2=76305010, z6=0, z7=20, z8=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:76305060:"B-but why?"
                call = talk_m10_29_x6(flag3=129020112, text6=76305060, text7=76305060, z14=76305060)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 9: [Lib] Death state_SubState"""
                    Label('L1')
                    # talk:76305070:"Eeeek!"
                    talk_m10_29_x7(text9=76305070, z16=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 12: Magician: Conversation_SubState"""
                call = talk_m10_29_x26()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    # talk:76305030:"Please, stop this!", talk:76305040:"C-calm...calm yourself!", talk:76305050:"Ouch!"
                    call = talk_m10_29_x5(text10=76305030, text11=76305040, text12=76305050, text13=76305030,
                                          flag7=129020115, flag8=129020116)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 11: [Lib] First adversification_SubState"""
                        # talk:76305000:"How could you..."
                        call = talk_m10_29_x4(flag9=103770, text14=76305000, z17=0, z18=103771)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(129020116) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(129020115) != 1:
                    Goto('L2')
        """State 10: [Lib] Killing state_SubState"""
        # talk:76305020:"Goodness, are you alright?"
        talk_m10_29_x8(text8=76305020, z15=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_29_x0(text15=_, z21=_, z22=0):
    """[Lib] Conversation: General purpose
    text15: Conversation ID
    z21: Conversation flag
    z22: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text15, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z21, 1)
    SetEventFlag(z22, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_29_x1(text1=_, z17=_, z19=-1, z20=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z17: Conversation flag
    z19: Display distance
    z20: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z19)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z17, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_29_x2(text8=_, z15=0):
    """[Lib] Conversation: Event end
    text8: Conversation ID
    z15: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z15, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_29_x3(text2=_, z6=0, z7=20, z8=80):
    """[Lib] Reunion hostility
    text2: Conversation message ID
    z6: Conversation flag ID
    z7: Display distance
    z8: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_29_x18(text2=text2, z6=z6, z7=z7, z8=z8)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_29_x4(flag9=_, text14=_, z17=0, z18=_):
    """[Lib] First hostility
    flag9: Hostile: Global event flag
    text14: Conversation ID
    z17: Conversation flag
    z18: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag9, 1)
    SetEventFlag(z18, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag9) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_29_x1(text1=text14, z17=z17, z19=-1, z20=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_29_x5(text10=_, text11=_, text12=_, text13=_, flag7=_, flag8=_):
    """[Lib] Hostile waiting
    text10: Conversation ID: 1 attacked
    text11: Conversation ID: Attacked 2
    text12: Conversation ID: 3 attacked
    text13: Conversation ID: 4 attacked
    flag7: No use: Area and other flags
    flag8: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag8) != 1, flag8, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag7) != 1, flag7, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_29_x1(text1=text13, z17=0, z19=-1, z20=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_29_x1(text1=text12, z17=0, z19=-1, z20=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_29_x1(text1=text11, z17=0, z19=-1, z20=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_29_x1(text1=text10, z17=0, z19=-1, z20=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_29_x6(flag3=_, text6=_, text7=_, z14=_):
    """[Lib] Hostile state
    flag3: Area and other flags: HP decreased
    text6: Conversation ID: HP drop 1
    text7: Conversation ID: HP drop 2
    z14: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag3) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_29_x10(text6=text6, flag3=flag3)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_29_x10(text6=text7, flag3=flag3)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_29_x10(text6=text7, flag3=flag3)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_29_x7(text9=_, z16=0):
    """[Lib] Death status
    text9: Conversation ID
    z16: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_29_x2(text8=text9, z15=z16)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_29_x8(text8=_, z15=0):
    """[Lib] Murder status
    text8: Conversation ID
    z15: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_29_x2(text8=text8, z15=z15)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_29_x9(flag4=_, flag5=_, flag6=_):
    """[Lib] Event: Branch
    flag4: Hostile flag
    flag5: death flag
    flag6: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag5) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag6) != 0
    elif GetEventFlag(flag4) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_29_x10(text6=_, flag3=_):
    """[Lib] Conversation: HP drop
    text6: Conversation ID
    flag3: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag3, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_29_x11(z11=0, z12=220, z4=_, z13=0):
    """[Lib] Menu start: General purpose
    z11: Camera parameter ID
    z12: Target Damipoly ID
    z4: NPC event parameter ID
    z13: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z13, z11, z12, z4)
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

def talk_m10_29_x12(text4=76303200, text5=76303200):
    """[Lib] Menu exit: General purpose
    text4: Conversation ID (at the time of purchase)
    text5: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_29_x1(text1=text4, z17=0, z19=-1, z20=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_29_x1(text1=text5, z17=0, z19=-1, z20=0)
    """State 4: End state"""
    return 0

def talk_m10_29_x13(text3=_):
    """[Lib] Menu cancellation: General purpose
    text3: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_29_x1(text1=text3, z17=0, z19=-1, z20=0)
    """State 4: End state"""
    return 0

def talk_m10_29_x14(lot1=_, flag1=_, text1=_, z1=_, z2=_):
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
    call = talk_m10_29_x1(text1=text1, z17=0, z19=-1, z20=0)
    if call.Done() and GetEventFlag(flag1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z1, 1)
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_29_x22(z3=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_29_x15(lot1=lot1, flag1=flag1, z1=z1, z2=z2, z9=0, z10=0)
    """State 9: End state"""
    return 0

def talk_m10_29_x15(lot1=_, flag1=_, z1=_, z2=_, z9=0, z10=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    z1: Conversation: Global conversation flag
    z2: Trophy acquisition: Area and other flags
    z9: Emigration permission: Global event flag
    z10: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z10, 1)
    SetEventFlag(z9, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
    SetEventFlag(flag1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_29_x16():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m10_29_x17():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_29_x18(text2=_, z6=0, z7=20, z8=80):
    """[Lib] Conversation: Hostile display only
    text2: Conversation ID
    z6: Conversation flag
    z7: Display distance
    z8: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text2, GetCommonEventParamDecimal(7), z7)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z6, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_29_x19(goods1=63008000, flag2=102435):
    """[Lib] Menu item: Gesture
    goods1: Gesture: Item ID
    flag2: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_29_x21(goods1=goods1, flag2=flag2)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_29_x20(goods1=63008000, flag2=102435, z4=74300000, z5=74300001):
    """[Lib] NPC menu: Gesture alone
    goods1: Item: Event item
    flag2: Item transfer: Global event flag
    z4: NPC menu: With gesture
    z5: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(flag2) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            # goods:63008000:"Joy" Gesture
            if (ItemCount(goods1, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_29_x11(z11=0, z12=220, z4=z4, z13=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m10_29_x19(goods1=goods1, flag2=flag2)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        pass
                elif call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    """State 6: [Lib] Menu exit: No Mes_SubState"""
                    Label('L0')
                    assert talk_m10_29_x16()
                    Goto('L2')
            """State 7: [Lib] Menu canceled: No Mes_SubState"""
            Label('L1')
            assert talk_m10_29_x17()
            Goto('L2')
        """State 5: [Lib] Menu start: No gesture _SubState"""
        call = talk_m10_29_x11(z11=0, z12=220, z4=z5, z13=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_29_x21(goods1=63008000, flag2=102435):
    """[Lib] Get gesture dialog
    goods1: Item ID
    flag2: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods1, 0, -1)
    SetEventFlag(flag2, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_29_x22(z3=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z3: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_29_x23():
    """Moonlight Jun: Conversation"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        ClearNpcMenuResults()
        if (GetEventFlag(102420) != 1 and GetEventFlag(102436) != 0 and GetEventFlag(104160) != 1 and
            GetEventFlag(102640) != 0 and GetEventFlag(203301) != 0):
            """State 5: Equipment transfer (Condition: White Phantom Summon? Achieved times) _SubState"""
            # lot:1743000:Bluemoon Greatsword, talk:74306000:"A man's journey...is never done..."
            assert talk_m10_29_x14(lot1=1743000, flag1=102420, text1=74306000, z1=0, z2=129020107)
        elif GetEventFlag(102640) != 0:
            break
        else:
            """State 3: Tsukimitsu: First conversation_SubState"""
            call = talk_m10_29_x24()
            if call.Done():
                pass
            elif GetEventFlag(102640) != 0:
                continue
        """State 2: Conversation: End"""
        Label('L0')
        ClearNpcMenuResults()
        """State 6: End state"""
        return 0
    """State 4: Tsukimitsu Minoru: Petrification Cancellation_SubState"""
    assert talk_m10_29_x25()
    Goto('L0')

def talk_m10_29_x24():
    """Tsukimitsu: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(203300) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:74300100:"See that statue? Gives me the willies.\nStare at it for long enough, it starts to look alive."
        assert talk_m10_29_x0(text15=74300100, z21=0, z22=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:74300000:"Have you business with me?"
        assert talk_m10_29_x0(text15=74300000, z21=203300, z22=0)
    """State 4: End state"""
    return 0

def talk_m10_29_x25():
    """Tsukimitsu Minoru: A petrochemical release conversation"""
    """State 0,1: Petrochemical conversation: start"""
    if GetEventFlag(203301) != 0:
        """State 5: Magician Petrification Cancellation: Second Time_SubState"""
        # talk:74300300:"I am in yer debt."
        call = talk_m10_29_x0(text15=74300300, z21=0, z22=0)
        if call.Done() and GetEventFlag(102435) != 1:
            """State 6: [Lib] NPC menu: Gesture alone_SubState"""
            # goods:63008000:"Joy" Gesture
            assert talk_m10_29_x20(goods1=63008000, flag2=102435, z4=74300000, z5=74300001)
        elif call.Done():
            pass
    else:
        """State 4: Sorcerer Decalcification_SubState"""
        # talk:74300200:"What?! Clearing the way was your doing, was it?"
        assert talk_m10_29_x0(text15=74300200, z21=203301, z22=0)
        """State 2: Petrochemical conversation: Set migration permission flag"""
        SetEventFlag(102421, 1)
        assert GetEventFlag(102421) != 0
        """State 3: Petrification Cancellation: White Phantom Appearance: Flag Setting"""
        SetEventFlag(102430, 1)
        assert GetEventFlag(102430) != 0
    """State 7: End state"""
    return 0

def talk_m10_29_x26():
    """Magician: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Conversation: branch"""
    if GetEventFlag(204403) != 0:
        """State 7: Magician: Greeting_SubState"""
        assert talk_m10_29_x28()
        """State 8: Magician: NPC Menu_SubState"""
        assert talk_m10_29_x27()
    elif GetEventFlag(204402) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:76300300:"I was attacked, and turned to stone...I think..."
        assert talk_m10_29_x0(text15=76300300, z21=204403, z22=0)
    elif GetEventFlag(204401) != 0:
        """State 10: Speak: Part 3_SubState"""
        # lot:1763000:Prism Stone, talk:76300200:"Oh, you're that traveller!"
        assert talk_m10_29_x14(lot1=1763000, flag1=102642, text1=76300200, z1=204402, z2=0)
    elif GetEventFlag(104270) != 0 and GetEventFlag(204401) != 1:
        """State 9: Talk: 2.5_SubState"""
        Label('L0')
        assert talk_m10_29_x0(text15=76300150, z21=204401, z22=0)
    elif GetEventFlag(102641) != 0 and GetEventFlag(204401) != 1:
        Goto('L0')
    elif GetEventFlag(204400) != 0 and GetEventFlag(104270) != 1:
        """State 5: Talk to: 2_SubState"""
        # talk:76300100:"I'm fine, I think. Hrgg!"
        assert talk_m10_29_x0(text15=76300100, z21=204401, z22=0)
    elif GetEventFlag(104270) != 1:
        """State 4: Talk: Part 1_SubState"""
        # talk:76300000:"Cough! Cough cough!"
        assert talk_m10_29_x0(text15=76300000, z21=204400, z22=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 11: End state"""
    return 0

def talk_m10_29_x27():
    """Magician: NPC menu"""
    """State 0: Start state"""
    while True:
        """State 1: Menu: Start"""
        if GetEventFlag(104270) != 0:
            """State 9: [Lib] Menu start: At death_SubState"""
            call = talk_m10_29_x11(z11=0, z12=220, z4=76300001, z13=0)
            if call.Get() == 2:
                """State 7: Sorcerer: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_29_x29()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:76303200:"Be safe."
                assert talk_m10_29_x12(text4=76303200, text5=76303200)
        else:
            """State 4: [Lib] Menu start: General purpose_SubState"""
            call = talk_m10_29_x11(z11=0, z12=220, z4=76300000, z13=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 0 and ((GetGlobalVariable(240) > 1) != 0 and GetEventFlag(204411) != 1):
                """State 3: Menu: Thank you conversation: Flag setting"""
                Label('L2')
                SetEventFlag(102652, 1)
                SetEventFlag(204411, 1)
                """State 8: Menu: Thank you conversation_SubState"""
                # talk:76300500:"Thank you so much!\nI'm very happy for this gift."
                call = talk_m10_29_x13(text3=76300500)
                if call.Done():
                    pass
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0 and ((GetGlobalVariable(241) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 0 and ((GetGlobalVariable(242) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 0 and ((GetGlobalVariable(243) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 1 and ((GetGlobalVariable(240) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 1 and ((GetGlobalVariable(241) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 1 and ((GetGlobalVariable(242) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 1 and ((GetGlobalVariable(243) > 1) != 0 and GetEventFlag(204411) != 1):
                Goto('L2')
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L1')
        """State 2: Menu: Exit"""
        Label('L3')
        """State 10: End state"""
        return 0
    """State 6: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76303300:"Wait! Where are you...cough..."
    assert talk_m10_29_x13(text3=76303300)
    Goto('L3')

def talk_m10_29_x28():
    """Magician: Greeting"""
    """State 0,1: Greeting: Start"""
    if ((not GetGlobalVariable(240)) != 0 and (not GetGlobalVariable(241)) != 0 and (not GetGlobalVariable(242))
        != 0 and (not GetGlobalVariable(243)) != 0 and GetEventFlag(204410) != 0):
        """State 4: Dress-up request: Part 2_SubState"""
        # talk:76300900:"Er...could you spare me something to wear?"
        assert talk_m10_29_x0(text15=76300900, z21=0, z22=0)
    elif ((not GetGlobalVariable(240)) != 0 and (not GetGlobalVariable(241)) != 0 and (not GetGlobalVariable(242))
          != 0 and (not GetGlobalVariable(243)) != 0):
        """State 3: Dress-up request: Part 1_SubState"""
        # talk:76300400:"Um...I hate to burden you further,\nas you've already saved my life..."
        assert talk_m10_29_x0(text15=76300400, z21=204410, z22=0)
    else:
        """State 5: Dress-up request: None_SubState"""
        # talk:76300800:"I'm going back to Majula."
        assert talk_m10_29_x0(text15=76300800, z21=0, z22=0)
    """State 2,6: End state"""
    return 0

def talk_m10_29_x29():
    """Magician: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(204421) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(204420, 0)
        SetEventFlag(204421, 0)
        """State 4: Menu conversation: 1_SubState"""
        Label('L0')
        # talk:76300600:"I have my very own teacher."
        assert talk_m10_29_x1(text1=76300600, z17=204420, z19=-1, z20=0)
    elif GetEventFlag(204420) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:76300700:"I'm rather unskilled... Milord probably ditched me."
        assert talk_m10_29_x1(text1=76300700, z17=204421, z19=-1, z20=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 6: End state"""
    return 0

