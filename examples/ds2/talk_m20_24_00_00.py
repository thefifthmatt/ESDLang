# -*- coding: utf-8 -*-
def talk_m20_24_5060():
    """Tomb guard"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_24_x9(z29=103510, z30=104010, z31=224020101)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_24_x3(text5=50609200, z18=0, z19=20, z20=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_24_x6(z27=224020102, text9=50609500, text10=50609500, z28=50609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_24_x7(text12=50609600, z33=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Gravekeeper: Conversation_SubState"""
                call = talk_m20_24_x25()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif GetEventFlag(104010) != 1 and GetEventFlag(103510) != 0:
                    """State 11: [Lib] First hostility_ (with distance) _SubState"""
                    # talk:50600100:"I warned you."
                    call = talk_m20_24_x21(z5=103510, text2=50600100, z6=0, z7=50, z8=80)
                    if call.Done():
                        Goto('L0')
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_24_x5(text13=50609400, text14=50609410, text15=50609420, text16=50609400,
                                          z34=224020105, z35=224020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_24_x4(z36=103510, text17=50609100, z37=0, z38=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(224020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(224020105) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_24_x8(text11=50609300, z32=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_24_7000():
    """Dragon Maiden"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_24_x9(z29=103523, z30=104020, z31=224020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_24_x3(text5=70009200, z18=0, z19=20, z20=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_24_x6(z27=224020122, text9=70009500, text10=70009500, z28=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_24_x7(text12=70009600, z33=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: Dragon Miko: Conversation (within the Royal Castle) _SubState"""
                call = talk_m20_24_x23()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 10: Waiting for hostility: Dragon Miko _SubState"""
                    Label('L2')
                    call = talk_m20_24_x30()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_24_x4(z36=103520, text17=70009100, z37=0, z38=103523)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(224020134) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(224020133) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(224020132) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(224020131) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(224020130) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(224020129) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(224020128) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(224020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(224020125) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m20_24_x8(text11=70009300, z32=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_24_x0(text18=_, z40=_, z41=0):
    """[Lib] Conversation: General purpose
    text18: Conversation ID
    z40: Conversation flag
    z41: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text18, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z40, 1)
    SetEventFlag(z41, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_24_x1(text2=_, z6=_, z7=_, z39=0):
    """[Lib] Conversation: Display only
    text2: Conversation ID
    z6: Conversation flag
    z7: Display distance
    z39: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text2, GetCommonEventParamDecimal(7), z7)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z6, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m20_24_x2(text11=_, z32=0):
    """[Lib] Conversation: Event end
    text11: Conversation ID
    z32: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text11, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z32, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_24_x3(text5=_, z18=0, z19=20, z20=80):
    """[Lib] Reunion hostility
    text5: Conversation message ID
    z18: Conversation flag ID
    z19: Display distance
    z20: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m20_24_x16(text5=text5, z18=z18, z19=z19, z20=z20)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_24_x4(z36=_, text17=_, z37=0, z38=_):
    """[Lib] First hostility
    z36: Hostile: Global event flag
    text17: Conversation ID
    z37: Conversation flag
    z38: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z36, 1)
    SetEventFlag(z38, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z36) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m20_24_x1(text2=text17, z6=z37, z7=-1, z39=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_24_x5(text13=50609400, text14=50609410, text15=50609420, text16=50609400, z34=224020105,
                   z35=224020106):
    """[Lib] Hostile waiting
    text13: Conversation ID: 1 attacked
    text14: Conversation ID: Attacked 2
    text15: Conversation ID: 3 attacked
    text16: Conversation ID: 4 attacked
    z34: No use: Area and other flags
    z35: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z35) != 1, z35, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z34) != 1, z34, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m20_24_x1(text2=text16, z6=0, z7=-1, z39=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_24_x1(text2=text15, z6=0, z7=-1, z39=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_24_x1(text2=text14, z6=0, z7=-1, z39=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_24_x1(text2=text13, z6=0, z7=-1, z39=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_24_x6(z27=_, text9=_, text10=_, z28=_):
    """[Lib] Hostile state
    z27: Area and other flags: HP decreased
    text9: Conversation ID: HP drop 1
    text10: Conversation ID: HP drop 2
    z28: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z27) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m20_24_x10(text9=text9, z27=z27)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_24_x10(text9=text10, z27=z27)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_24_x10(text9=text10, z27=z27)

def talk_m20_24_x7(text12=_, z33=0):
    """[Lib] Death status
    text12: Conversation ID
    z33: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m20_24_x2(text11=text12, z32=z33)

def talk_m20_24_x8(text11=_, z32=0):
    """[Lib] Murder status
    text11: Conversation ID
    z32: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_24_x2(text11=text11, z32=z32)

def talk_m20_24_x9(z29=_, z30=_, z31=_):
    """[Lib] Event: Branch
    z29: Hostile flag
    z30: death flag
    z31: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z30) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z31) != 0
    elif GetEventFlag(z29) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m20_24_x10(text9=_, z27=_):
    """[Lib] Conversation: HP drop
    text9: Conversation ID
    z27: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z27, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_24_x11(z23=0, z24=220, z25=_, z26=0):
    """[Lib] Menu start: General purpose
    z23: Camera parameter ID
    z24: Target Damipoly ID
    z25: NPC event parameter ID
    z26: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z26, z23, z24, z25)
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

def talk_m20_24_x12(text7=50600900, text8=50601000):
    """[Lib] Menu exit: General purpose
    text7: Conversation ID (at the time of purchase)
    text8: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m20_24_x1(text2=text7, z6=0, z7=-1, z39=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m20_24_x1(text2=text8, z6=0, z7=-1, z39=0)
    """State 4: End state"""
    return 0

def talk_m20_24_x13(text6=50600800):
    """[Lib] Menu cancellation: General purpose
    text6: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m20_24_x1(text2=text6, z6=0, z7=-1, z39=0)
    """State 4: End state"""
    return 0

def talk_m20_24_x14(lot1=1506000, z1=102021, z2=0, z3=0, z21=0, z22=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z21: Emigration permission: Global event flag
    z22: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z22, 1)
    SetEventFlag(z21, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
    # lot:1506000:Darkdrift
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_24_x15(lot1=1506000, z1=102021, text1=50606000, z2=0, z3=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    text1: Conversation ID
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m20_24_x1(text2=text1, z6=0, z7=-1, z39=0)
    if call.Done() and GetEventFlag(z1) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    # lot:1506000:Darkdrift
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_24_x22(z4=1011, lot1=lot1)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_24_x14(lot1=lot1, z1=z1, z2=z2, z3=z3, z21=0, z22=0)
    """State 6: End state"""
    return 0

def talk_m20_24_x16(text5=_, z18=0, z19=20, z20=80):
    """[Lib] Conversation: Hostile display only
    text5: Conversation ID
    z18: Conversation flag
    z19: Display distance
    z20: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text5, GetCommonEventParamDecimal(7), z19)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m20_24_x17(z9=63015000, z10=0):
    """[Lib] Menu item: Gesture
    z9: Gesture: Item ID
    z10: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m20_24_x20(z9=z9, z10=z10)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m20_24_x18(text4=_, z14=_, z15=224020127, z16=0, z17=0):
    """[Lib] Conversation: Canceling startup state
    text4: Conversation ID
    z14: Conversation flag
    z15: Activation state release: Area and other flags
    z16: Rock sitting 1: Poke your cheek with your hand
    z17: Extend both hands back
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 10: Conversation: Cancel start state: Branch"""
    if GetEventFlag(z15) != 0:
        """State 8: Conversation: Activation state release: Second time"""
        Label('L0')
        DeleteKeyGuideArea()
        SetEventFlag(z15, 1)
    elif GetEventFlag(z16) != 1 and GetEventFlag(z17) != 1:
        Goto('L0')
    else:
        """State 7: Conversation: Activation state release: First use"""
        DeleteKeyGuideArea()
        SetEventFlag(z15, 1)
        assert GetEventFlag(z15) != 0
        """State 9: Conversation: Release hood: Wait"""
        KeyGuideTemporarilyInvalidIf(GetEventFlag(z16) != 0, 3.5)
        KeyGuideTemporarilyInvalidIf(GetEventFlag(z17) != 0, 3.5)
        assert (GetStateTime() > GetRandomValueForStateTime(3, 3)) != 0
    """State 4: Conversation: Message"""
    StartConversation(text4, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z14, 1)
    """State 11: Conversation: End"""
    return 0

def talk_m20_24_x19(text3=_, z11=_, z12=9901, z13=15):
    """[Lib] Conversation: For unique key guide
    text3: Conversation ID
    z11: Conversation flag
    z12: Key guide parameters
    z13: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z12)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text3, GetCommonEventParamDecimal(7), z13)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z11, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_24_x20(z9=63015000, z10=0):
    """[Lib] Get gesture dialog
    z9: Item ID
    z10: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(z9, 0, -1)
    SetEventFlag(z10, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_24_x21(z5=103510, text2=50600100, z6=0, z7=50, z8=80):
    """[Lib] First hostility _ (with distance)
    z5: Hostile: Global event flag
    text2: Conversation ID
    z6: Conversation flag
    z7: Display distance
    z8: Audible distance ratio
    """
    """State 0,1: First hostility: start"""
    SetEventFlag(z5, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    assert GetEventFlag(z5) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: [Lib] Conversation: Display only _SubState"""
    assert talk_m20_24_x1(text2=text2, z6=z6, z7=z7, z39=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_24_x22(z4=1011, lot1=1506000):
    """[Lib] Inventory full dialog: Item display
    z4: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    # lot:1506000:Darkdrift
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_24_x23():
    """Dragon Miko: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Dragon Miko: Get King's Ring_SubState"""
    assert talk_m20_24_x24()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 4: End state"""
    return 0

def talk_m20_24_x24():
    """Dragon Miko: Obtaining King's Ring"""
    """State 0,1: After obtaining the king's ring: Start"""
    if GetEventFlag(201160) != 0:
        """State 4: Talk: Part 1 (Single loop) _SubState"""
        # talk:70002800:"Bearer of the curse. Go to the east."
        assert talk_m20_24_x18(text4=70002800, z14=0, z15=224020127, z16=0, z17=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:70002700:"This ring is the symbol of the King."
        assert talk_m20_24_x18(text4=70002700, z14=201160, z15=224020127, z16=0, z17=0)
        """State 2: After obtaining the king's ring: Set the generation stop flag"""
        SetEventFlag(102087, 1)
    """State 5: End state"""
    return 0

def talk_m20_24_x25():
    """Gravekeeper: Conversation"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        ClearNpcMenuResults()
        """State 4: Gravekeeper: First conversation_SubState"""
        call = talk_m20_24_x27()
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            break
        elif (GetEventFlag(224020107) != 0 and GetEventFlag(104010) != 1 and ConversationEnded() != 0
              and GetEventFlag(224020109) != 1):
            """State 3: Gravekeeper: Approach Conversation_SubState"""
            Label('L0')
            assert talk_m20_24_x26()
            continue
        elif (GetEventFlag(224020108) != 0 and GetEventFlag(104010) != 1 and ConversationEnded() != 0
              and GetEventFlag(224020109) != 1):
            Goto('L0')
        """State 2: Conversation: End"""
        Label('L1')
        ClearNpcMenuResults()
        """State 6: End state"""
        return 0
    """State 5: Gravekeeper: NPC Menu_SubState"""
    assert talk_m20_24_x28()
    Goto('L1')

def talk_m20_24_x26():
    """Gravekeeper: Approaching conversation"""
    """State 0,1: Approaching conversation: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(201400) != 0:
        pass
    else:
        """State 4: Automatic conversation_SubState"""
        # talk:50600000:"Halt."
        assert talk_m20_24_x1(text2=50600000, z6=201400, z7=50, z39=0)
    """State 2: Approaching conversation: Branch"""
    if GetEventFlag(224020107) != 0:
        """State 5: Automatic conversation: With light source_SubState"""
        # talk:50600010:"Human.\nPut that light out."
        assert talk_m20_24_x1(text2=50600010, z6=0, z7=50, z39=0)
    elif GetEventFlag(224020108) != 0:
        """State 6: Automatic conversation: No light source_SubState"""
        # talk:50600020:"Human.\nDo not produce light."
        assert talk_m20_24_x1(text2=50600020, z6=0, z7=50, z39=0)
    """State 7: Automatic conversation: End_SubState"""
    # talk:50600030:"Light, and all those who bear it,\nare unwelcome in this place."
    assert talk_m20_24_x1(text2=50600030, z6=0, z7=50, z39=0)
    """State 3: Approaching conversation: End"""
    SetEventFlag(224020109, 1)
    """State 8: End state"""
    return 0

def talk_m20_24_x27():
    """Gravekeeper: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(201405) != 0:
        """State 8: Talk to: 6_SubState"""
        # talk:50600700:"What do you require, human?"
        assert talk_m20_24_x0(text18=50600700, z40=0, z41=0)
    elif GetEventFlag(201404) != 0:
        """State 7: Talk: Part 5_SubState"""
        # talk:50600600:"This place is welcome to all, \nprovided due reverence is shown."
        assert talk_m20_24_x0(text18=50600600, z40=201405, z41=0)
        """State 2: Initial conversation: White phantom appearance flag set"""
        SetEventFlag(102030, 1)
        assert GetEventFlag(102030) != 0
    elif GetEventFlag(201403) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:50600500:"In the past, humans were one with the dark."
        assert talk_m20_24_x0(text18=50600500, z40=201404, z41=0)
        """State 9: Normal: End state"""
        Label('L0')
        return 0
    elif GetEventFlag(201402) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:50600400:"Did you come for him?\nThe one called Vendrick. "
        assert talk_m20_24_x0(text18=50600400, z40=201403, z41=0)
        Goto('L0')
    elif GetEventFlag(201401) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:50600300:"I am a Fenito.\nWe weave death, and watch over the dead."
        assert talk_m20_24_x0(text18=50600300, z40=201402, z41=0)
        Goto('L0')
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:50600200:"I am Agdayne.\nGuardian of the crypt."
        assert talk_m20_24_x0(text18=50600200, z40=201401, z41=0)
        Goto('L0')
    """State 10: Menu: Exit state"""
    return 1

def talk_m20_24_x28():
    """Gravekeeper: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 3: Menu: Branch"""
        # goods:63015000:"Have mercy!" Gesture
        if (ItemCount(63015000, 1, 1, 0) > 1) != 0:
            """State 7: [Lib] Menu start: No gesture _SubState"""
            call = talk_m20_24_x11(z23=0, z24=220, z25=50600001, z26=0)
            if call.Get() == 2:
                """State 9: Gravekeeper: Menu conversation_SubState"""
                Label('L0')
                call = talk_m20_24_x29()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:50600900:"Farewell, human.", talk:50601000:"Crude human, do as you please."
                assert talk_m20_24_x12(text7=50600900, text8=50601000)
        else:
            """State 4: [Lib] Menu start: With gesture_SubState"""
            call = talk_m20_24_x11(z23=0, z24=220, z25=50600000, z26=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 8: [Lib] Menu item: Gesture_SubState"""
                call = talk_m20_24_x17(z9=63015000, z10=0)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L1')
        """State 2: Menu: Exit"""
        Label('L2')
        ClearNpcMenuResults()
        """State 10: End state"""
        return 0
    """State 6: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:50600800:"Going so soon?"
    assert talk_m20_24_x13(text6=50600800)
    Goto('L2')

def talk_m20_24_x29():
    """Gravekeeper: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    # goods:40510000:King's Ring
    if GetEventFlag(102021) != 1 and (ItemCount(40510000, 1, 1, 0) > 1) != 0 and GetEventFlag(104010) != 1:
        """State 5: Equipment transfer (condition: possession of king's ring) _SubState"""
        # lot:1506000:Darkdrift, talk:50606000:"A long rest awaits me.\nFarewell, human."
        assert talk_m20_24_x15(lot1=1506000, z1=102021, text1=50606000, z2=0, z3=0)
    elif GetEventFlag(201412) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(201410, 0)
        SetEventFlag(201411, 0)
        SetEventFlag(201412, 0)
        """State 6: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:50600300:"I am a Fenito.\nWe weave death, and watch over the dead."
        assert talk_m20_24_x1(text2=50600300, z6=201410, z7=-1, z39=0)
    elif GetEventFlag(201411) != 0:
        """State 4: Menu conversation: 3_SubState"""
        # talk:50600600:"This place is welcome to all, \nprovided due reverence is shown."
        assert talk_m20_24_x1(text2=50600600, z6=201412, z7=-1, z39=0)
    elif GetEventFlag(201410) != 0:
        """State 7: Menu conversation: 2_SubState"""
        # talk:50600500:"In the past, humans were one with the dark."
        assert talk_m20_24_x1(text2=50600500, z6=201411, z7=-1, z39=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m20_24_x30():
    """Waiting for hostility: Dragon Miko"""
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 40)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(224020134) != 1, 224020134, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(224020133) != 1, 224020133, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(224020132) != 1, 224020132, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(224020131) != 1, 224020131, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(224020130) != 1, 224020130, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(224020129) != 1, 224020129, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(224020128) != 1, 224020128, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(224020126) != 1, 224020126, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(224020125) != 1, 224020125, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 30 and GetRandomValue(0) < 40) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_24_x1(text2=70009420, z6=0, z7=-1, z39=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_24_x1(text2=70009410, z6=0, z7=-1, z39=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_24_x1(text2=70009400, z6=0, z7=-1, z39=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_24_x31():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(100764) != 0 and GetEventFlag(208011) != 0:
        """State 7: [Lib] Conversation: Talk to 3_SubState"""
        # talk:69200500:"Once, the Lord of Light banished Dark,\nand all that stemmed from humanity."
        assert talk_m20_24_x19(text3=69200500, z11=208012, z12=9901, z13=15)
        """State 4: YN dialog"""
        # action:1220:"What is your choice?"
        DisplayOwnYesNoMenu(1220, 15, -1, 0, 0, 0)
        if (YesNoMenuResult() == 1) != 0:
            """State 8: [Lib] Conversation: After selection _SubState"""
            Label('L0')
            # talk:69200600:"Vendrick, the near-true monarch,\nis here, and not far off."
            assert talk_m20_24_x1(text2=69200600, z6=208013, z7=15, z39=0)
            """State 3: End encounter flag"""
            SetEventFlag(100745, 1)
        elif (YesNoMenuResult() == 2) != 0:
            Goto('L0')
        elif (YesNoMenuResult() == 3) != 0:
            pass
    elif GetEventFlag(100764) != 0 and GetEventFlag(208010) != 0:
        """State 6: [Lib] Conversation: Talk to 2_SubState"""
        # talk:69200400:"Life is brilliant. Beautiful.\nIt enchants us, to the point of obsession."
        assert talk_m20_24_x19(text3=69200400, z11=208011, z12=9901, z13=15)
    elif GetEventFlag(100764) != 0:
        """State 5: [Lib] Conversation: Talk to 1_SubState"""
        # talk:69200300:"Heheh, I believe we've been acquainted."
        assert talk_m20_24_x19(text3=69200300, z11=208010, z12=9901, z13=15)
    """State 2,9: End state"""
    return 0

def talk_m20_24_4100000():
    """Andyel"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(100745) != 0:
            break
        else:
            """State 3: Anne Deal_SubState"""
            assert talk_m20_24_x31()
    """State 2: Conversation: System termination"""
    EndMachine()

