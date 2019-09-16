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
        call = talk_m10_29_x9(z18=103661, z19=104161, z20=129020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_29_x3(text2=74309200, z8=0, z9=20, z10=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_29_x6(z16=129020102, text6=74309500, text7=74309500, z17=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_29_x7(text9=74309600, z22=0)
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
                                          z23=129020105, z24=129020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_29_x4(z25=103660, text14=74309100, z26=0, z27=103661)
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
        talk_m10_29_x8(text8=74309300, z21=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

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
        call = talk_m10_29_x9(z18=103771, z19=104271, z20=129020111)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            # talk:76305010:"I won't let you do this..."
            call = talk_m10_29_x3(text2=76305010, z8=0, z9=20, z10=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:76305060:"B-but why?"
                call = talk_m10_29_x6(z16=129020112, text6=76305060, text7=76305060, z17=76305060)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 9: [Lib] Death state_SubState"""
                    Label('L1')
                    # talk:76305070:"Eeeek!"
                    talk_m10_29_x7(text9=76305070, z22=0)
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
                                          z23=129020115, z24=129020116)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 11: [Lib] First adversification_SubState"""
                        # talk:76305000:"How could you..."
                        call = talk_m10_29_x4(z25=103770, text14=76305000, z26=0, z27=103771)
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
        talk_m10_29_x8(text8=76305020, z21=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_29_x0(text15=_, z30=_, z31=0):
    """[Lib] Conversation: General purpose
    text15: Conversation ID
    z30: Conversation flag
    z31: Global event flag
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
    SetEventFlag(z30, 1)
    SetEventFlag(z31, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_29_x1(text1=_, z26=_, z28=-1, z29=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z26: Conversation flag
    z28: Display distance
    z29: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z28)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z26, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_29_x2(text8=_, z21=0):
    """[Lib] Conversation: Event end
    text8: Conversation ID
    z21: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z21, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_29_x3(text2=_, z8=0, z9=20, z10=80):
    """[Lib] Reunion hostility
    text2: Conversation message ID
    z8: Conversation flag ID
    z9: Display distance
    z10: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_29_x18(text2=text2, z8=z8, z9=z9, z10=z10)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_29_x4(z25=_, text14=_, z26=0, z27=_):
    """[Lib] First hostility
    z25: Hostile: Global event flag
    text14: Conversation ID
    z26: Conversation flag
    z27: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z25, 1)
    SetEventFlag(z27, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z25) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_29_x1(text1=text14, z26=z26, z28=-1, z29=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_29_x5(text10=_, text11=_, text12=_, text13=_, z23=_, z24=_):
    """[Lib] Hostile waiting
    text10: Conversation ID: 1 attacked
    text11: Conversation ID: Attacked 2
    text12: Conversation ID: 3 attacked
    text13: Conversation ID: 4 attacked
    z23: No use: Area and other flags
    z24: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z24) != 1, z24, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z23) != 1, z23, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_29_x1(text1=text13, z26=0, z28=-1, z29=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_29_x1(text1=text12, z26=0, z28=-1, z29=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_29_x1(text1=text11, z26=0, z28=-1, z29=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_29_x1(text1=text10, z26=0, z28=-1, z29=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_29_x6(z16=_, text6=_, text7=_, z17=_):
    """[Lib] Hostile state
    z16: Area and other flags: HP decreased
    text6: Conversation ID: HP drop 1
    text7: Conversation ID: HP drop 2
    z17: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z16) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_29_x10(text6=text6, z16=z16)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_29_x10(text6=text7, z16=z16)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_29_x10(text6=text7, z16=z16)

def talk_m10_29_x7(text9=_, z22=0):
    """[Lib] Death status
    text9: Conversation ID
    z22: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_29_x2(text8=text9, z21=z22)

def talk_m10_29_x8(text8=_, z21=0):
    """[Lib] Murder status
    text8: Conversation ID
    z21: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_29_x2(text8=text8, z21=z21)

def talk_m10_29_x9(z18=_, z19=_, z20=_):
    """[Lib] Event: Branch
    z18: Hostile flag
    z19: death flag
    z20: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z19) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z20) != 0
    elif GetEventFlag(z18) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_29_x10(text6=_, z16=_):
    """[Lib] Conversation: HP drop
    text6: Conversation ID
    z16: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z16, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_29_x11(z13=0, z14=220, z6=_, z15=0):
    """[Lib] Menu start: General purpose
    z13: Camera parameter ID
    z14: Target Damipoly ID
    z6: NPC event parameter ID
    z15: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z15, z13, z14, z6)
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

def talk_m10_29_x12(text4=76303200, text5=76303200):
    """[Lib] Menu exit: General purpose
    text4: Conversation ID (at the time of purchase)
    text5: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_29_x1(text1=text4, z26=0, z28=-1, z29=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_29_x1(text1=text5, z26=0, z28=-1, z29=0)
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
    assert talk_m10_29_x1(text1=text3, z26=0, z28=-1, z29=0)
    """State 4: End state"""
    return 0

def talk_m10_29_x14(lot1=_, z1=_, text1=_, z2=_, z3=_):
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
    call = talk_m10_29_x1(text1=text1, z26=0, z28=-1, z29=0)
    if call.Done() and GetEventFlag(z1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_29_x22(z4=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_29_x15(lot1=lot1, z1=z1, z2=z2, z3=z3, z11=0, z12=0)
    """State 9: End state"""
    return 0

def talk_m10_29_x15(lot1=_, z1=_, z2=_, z3=_, z11=0, z12=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z11: Emigration permission: Global event flag
    z12: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z12, 1)
    SetEventFlag(z11, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
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

def talk_m10_29_x18(text2=_, z8=0, z9=20, z10=80):
    """[Lib] Conversation: Hostile display only
    text2: Conversation ID
    z8: Conversation flag
    z9: Display distance
    z10: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text2, GetCommonEventParamDecimal(7), z9)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z8, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_29_x19(goods1=63008000, z5=102435):
    """[Lib] Menu item: Gesture
    goods1: Gesture: Item ID
    z5: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_29_x21(goods1=goods1, z5=z5)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_29_x20(goods1=63008000, z5=102435, z6=74300000, z7=74300001):
    """[Lib] NPC menu: Gesture alone
    goods1: Item: Event item
    z5: Item transfer: Global event flag
    z6: NPC menu: With gesture
    z7: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(z5) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            # goods:63008000:"Joy" Gesture
            if (ItemCount(goods1, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_29_x11(z13=0, z14=220, z6=z6, z15=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m10_29_x19(goods1=goods1, z5=z5)
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
        call = talk_m10_29_x11(z13=0, z14=220, z6=z7, z15=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_29_x21(goods1=63008000, z5=102435):
    """[Lib] Get gesture dialog
    goods1: Item ID
    z5: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods1, 0, -1)
    SetEventFlag(z5, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_29_x22(z4=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z4: Text ID
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
            assert talk_m10_29_x14(lot1=1743000, z1=102420, text1=74306000, z2=0, z3=129020107)
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
        assert talk_m10_29_x0(text15=74300100, z30=0, z31=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:74300000:"Have you business with me?"
        assert talk_m10_29_x0(text15=74300000, z30=203300, z31=0)
    """State 4: End state"""
    return 0

def talk_m10_29_x25():
    """Tsukimitsu Minoru: A petrochemical release conversation"""
    """State 0,1: Petrochemical conversation: start"""
    if GetEventFlag(203301) != 0:
        """State 5: Magician Petrification Cancellation: Second Time_SubState"""
        # talk:74300300:"I am in yer debt."
        call = talk_m10_29_x0(text15=74300300, z30=0, z31=0)
        if call.Done() and GetEventFlag(102435) != 1:
            """State 6: [Lib] NPC menu: Gesture alone_SubState"""
            # goods:63008000:"Joy" Gesture
            assert talk_m10_29_x20(goods1=63008000, z5=102435, z6=74300000, z7=74300001)
        elif call.Done():
            pass
    else:
        """State 4: Sorcerer Decalcification_SubState"""
        # talk:74300200:"What?! Clearing the way was your doing, was it?"
        assert talk_m10_29_x0(text15=74300200, z30=203301, z31=0)
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
        assert talk_m10_29_x0(text15=76300300, z30=204403, z31=0)
    elif GetEventFlag(204401) != 0:
        """State 10: Speak: Part 3_SubState"""
        # lot:1763000:Prism Stone, talk:76300200:"Oh, you're that traveller!"
        assert talk_m10_29_x14(lot1=1763000, z1=102642, text1=76300200, z2=204402, z3=0)
    elif GetEventFlag(104270) != 0 and GetEventFlag(204401) != 1:
        """State 9: Talk: 2.5_SubState"""
        Label('L0')
        assert talk_m10_29_x0(text15=76300150, z30=204401, z31=0)
    elif GetEventFlag(102641) != 0 and GetEventFlag(204401) != 1:
        Goto('L0')
    elif GetEventFlag(204400) != 0 and GetEventFlag(104270) != 1:
        """State 5: Talk to: 2_SubState"""
        # talk:76300100:"I'm fine, I think. Hrgg!"
        assert talk_m10_29_x0(text15=76300100, z30=204401, z31=0)
    elif GetEventFlag(104270) != 1:
        """State 4: Talk: Part 1_SubState"""
        # talk:76300000:"Cough! Cough cough!"
        assert talk_m10_29_x0(text15=76300000, z30=204400, z31=0)
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
            call = talk_m10_29_x11(z13=0, z14=220, z6=76300001, z15=0)
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
            call = talk_m10_29_x11(z13=0, z14=220, z6=76300000, z15=0)
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
        assert talk_m10_29_x0(text15=76300900, z30=0, z31=0)
    elif ((not GetGlobalVariable(240)) != 0 and (not GetGlobalVariable(241)) != 0 and (not GetGlobalVariable(242))
          != 0 and (not GetGlobalVariable(243)) != 0):
        """State 3: Dress-up request: Part 1_SubState"""
        # talk:76300400:"Um...I hate to burden you further,\nas you've already saved my life..."
        assert talk_m10_29_x0(text15=76300400, z30=204410, z31=0)
    else:
        """State 5: Dress-up request: None_SubState"""
        # talk:76300800:"I'm going back to Majula."
        assert talk_m10_29_x0(text15=76300800, z30=0, z31=0)
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
        assert talk_m10_29_x1(text1=76300600, z26=204420, z28=-1, z29=0)
    elif GetEventFlag(204420) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:76300700:"I'm rather unskilled... Milord probably ditched me."
        assert talk_m10_29_x1(text1=76300700, z26=204421, z28=-1, z29=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 6: End state"""
    return 0

