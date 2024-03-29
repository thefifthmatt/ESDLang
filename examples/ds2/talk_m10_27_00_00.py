# -*- coding: utf-8 -*-
def talk_m10_27_6000():
    """Ancient dragon"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            pass
        elif GetEventFlag(103970) != 0:
            break
        else:
            """State 6: Ancient Dragon: Conversation_SubState"""
            call = talk_m10_27_x18()
            if call.Done():
                continue
            elif (GetAreaVariable(63) > 3) != 0:
                break
            elif (NumberOfTimesDamaged(1) > 1) != 0:
                """State 2: Hostility: Set damage flag"""
                AddAreaVariable(63, 1)
                if (GetAreaVariable(63) > 3) != 0:
                    break
                else:
                    """State 5: Enmity: Damage reset"""
                    ResetDamageTakenCount()
                    continue
            elif (NumberOfTimesDamaged(1) > 3) != 0:
                break
        """State 4: Conversation: System: End"""
        Label('L0')
        EndMachine()
        Quit()
    """State 3: Hostility: Set flag"""
    DeleteKeyGuideArea()
    SetEventFlag(103970, 1)
    SetEventFlag(103999, 1)
    SaveExecution()
    assert GetEventFlag(103970) != 0
    Goto('L0')

def talk_m10_27_7000():
    """Dragon Maiden (Andir's House)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_27_x8(flag5=103520, flag6=104020, flag7=127020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_27_x3(text8=70009200, z12=0, z13=20, z14=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_27_x5(flag4=127020122, text9=70009500, text10=70009500, z16=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_27_x6(text12=70009600, z18=104020)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: Dragon Miko: Conversation (Andyle Hall) _SubState"""
                call = talk_m10_27_x19()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 10: Waiting for hostility: Dragon Miko _SubState"""
                    Label('L2')
                    call = talk_m10_27_x21()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_27_x4(flag8=103520, text13=70009100, z19=0, z20=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(127020132) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(127020131) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(127020130) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(127020129) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(127020128) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(127020127) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(127020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(127020125) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(127020124) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_27_x7(text11=70009300, z17=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_27_x0(text14=70004300, z23=0, z24=0):
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
    # talk:70004300:"Listen to what the dragon says."
    StartConversation(text14, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z23, 1)
    SetEventFlag(z24, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_27_x1(text1=_, z19=_, z21=_, z22=0):
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

def talk_m10_27_x2(text11=_, z17=_):
    """[Lib] Conversation: Event end
    text11: Conversation ID
    z17: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text11, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z17, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_27_x3(text8=70009200, z12=0, z13=20, z14=80):
    """[Lib] Reunion hostility
    text8: Conversation message ID
    z12: Conversation flag ID
    z13: Display distance
    z14: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_27_x14(text8=text8, z12=z12, z13=z13, z14=z14)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_27_x4(flag8=103520, text13=70009100, z19=0, z20=0):
    """[Lib] First hostility
    flag8: Hostile: Global event flag
    text13: Conversation ID
    z19: Conversation flag
    z20: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag8, 1)
    SetEventFlag(z20, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag8) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_27_x1(text1=text13, z19=z19, z21=-1, z22=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_27_x5(flag4=127020122, text9=70009500, text10=70009500, z16=70009500):
    """[Lib] Hostile state
    flag4: Area and other flags: HP decreased
    text9: Conversation ID: HP drop 1
    text10: Conversation ID: HP drop 2
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
            assert talk_m10_27_x9(text9=text9, flag4=flag4)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_27_x9(text9=text10, flag4=flag4)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_27_x9(text9=text10, flag4=flag4)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_27_x6(text12=70009600, z18=104020):
    """[Lib] Death status
    text12: Conversation ID
    z18: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_27_x2(text11=text12, z17=z18)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_27_x7(text11=70009300, z17=0):
    """[Lib] Murder status
    text11: Conversation ID
    z17: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_27_x2(text11=text11, z17=z17)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_27_x8(flag5=103520, flag6=104020, flag7=127020121):
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

def talk_m10_27_x9(text9=70009500, flag4=127020122):
    """[Lib] Conversation: HP drop
    text9: Conversation ID
    flag4: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag4, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_27_x10(action1=1011):
    """[Lib] OK dialog
    action1: Text ID
    """
    """State 0,1: OK dialog: Display"""
    # action:1011:"Your inventory bag is full"
    DisplayOwnOkMenu(action1, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_27_x11(lot4=1787000, z15=103140):
    """[Lib] Item acquisition dialog
    lot4: Item lottery ID
    z15: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z15, 1)
    # lot:1787000:Ashen Mist Heart
    AwardItem(lot4, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_27_x12(lot3=1701000, flag3=102096, text5=70004200, text6=70004260, z4=201180, z5=0, z6=0, z7=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot3: Item lottery ID
    flag3: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z4: Conversation: Global conversation flag
    z5: Trophy acquisition: Area and other flags
    z6: Emigration permission: Global event flag
    z7: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_27_x1(text1=text5, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag3) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z4, 1)
        SetEventFlag(z6, 1)
        SetEventFlag(z7, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_27_x1(text1=text6, z19=0, z21=-1, z22=0)
    # lot:1701000:Aged Feather
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_27_x17(z8=1011, lot1=lot3)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_27_x13(lot1=lot3, flag1=flag3, z1=z4, z3=z5, z6=z6, z7=z7)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_27_x13(lot1=1701000, flag1=102096, z1=201180, z3=0, z6=0, z7=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    z1: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z6: Emigration permission: Global event flag
    z7: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z7, 1)
    SetEventFlag(z6, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z1, 1)
    SetEventFlag(flag1, 1)
    # lot:1701000:Aged Feather
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_27_x14(text8=70009200, z12=0, z13=20, z14=80):
    """[Lib] Conversation: Hostile display only
    text8: Conversation ID
    z12: Conversation flag
    z13: Display distance
    z14: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), z13)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z12, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_27_x15(text7=_, z9=_, z10=_, z11=_):
    """[Lib] Conversation: For unique key guide
    text7: Conversation ID
    z9: Conversation flag
    z10: Key guide parameters
    z11: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z10)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), z11)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z9, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_27_x16(lot2=1701000, flag2=102096, text3=70004200, text4=70004260, z2=201180, z3=0, goods2=60355000):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Important items
    lot2: Item lottery ID
    flag2: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    goods2: Important items
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_27_x1(text1=text3, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag2) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z2, 1)
    # goods:60355000:Aged Feather
    elif call.Done() and (ItemCount(goods2, 1, 1, 1) > 1) != 0:
        Goto('L0')
    # lot:1701000:Aged Feather
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_27_x17(z8=1011, lot1=lot2)
        Goto('L0')
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_27_x13(lot1=lot2, flag1=flag2, z1=z2, z3=z3, z6=0, z7=0)
    """State 4: Item transfer: Second half of conversation _SubState"""
    assert talk_m10_27_x1(text1=text4, z19=0, z21=-1, z22=0)
    """State 7: End state"""
    return 0

def talk_m10_27_x17(z8=1011, lot1=1701000):
    """[Lib] Inventory full dialog: Item display
    z8: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    # lot:1701000:Aged Feather
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_27_x18():
    """Old Dragon: Conversation"""
    """State 0,1: Conversation: Start"""
    if GetEventFlag(206600) != 0:
        """State 6: [Lib] Conversation: Old Dragon only: Part 2_SubState"""
        # talk:60000100:"......"
        assert talk_m10_27_x15(text7=60000100, z9=0, z10=10279000, z11=50)
    else:
        """State 4: [Lib] Conversation: _SubState for the ancient dragon"""
        # talk:60000000:"The murk shifts and stirs."
        call = talk_m10_27_x15(text7=60000000, z9=206600, z10=10279000, z11=50)
        # lot:1787000:Ashen Mist Heart
        if call.Done() and (GetEventFlag(103140) != 1 and CanGetItemLot(1787000, 1) != 1):
            """State 5: Inventory full confirmation dialog_SubState"""
            # action:1011:"Your inventory bag is full"
            assert talk_m10_27_x10(action1=1011)
        elif call.Done() and GetEventFlag(103140) != 0:
            pass
        elif call.Done():
            """State 3: [Lib] Item acquisition dialog_SubState"""
            # lot:1787000:Ashen Mist Heart
            assert talk_m10_27_x11(lot4=1787000, z15=103140)
    """State 2,7: End state"""
    return 0

def talk_m10_27_x19():
    """Dragon Miko: Conversation (Andyle Hall)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Dragon Miko: After encountering the ancient dragon_SubState"""
    assert talk_m10_27_x20()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 4: End state"""
    return 0

def talk_m10_27_x20():
    """Dragon Miko: After encountering the ancient dragon"""
    """State 0,1: After encountering the ancient dragon: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(201180) != 0:
        """State 3: Talk: Part 1 (Single loop) _SubState"""
        # talk:70004300:"Listen to what the dragon says."
        assert talk_m10_27_x0(text14=70004300, z23=0, z24=0)
    else:
        """State 6: Conversation: Item transfer: Mes⇒Item⇒Mes: Key_SubState"""
        # lot:1701000:Aged Feather, talk:70004200:"Bearer of the curse.", talk:70004260:"Do not resist. The dragon welcomes you.", goods:60355000:Aged Feather
        assert (talk_m10_27_x22(lot1=1701000, flag1=102096, text1=70004200, text2=70004260, z1=201180,
                goods1=60355000))
        """State 2: After encountering the ancient dragon: Set generation stop flag"""
        Label('L0')
        SetEventFlag(102088, 1)
        assert GetEventFlag(102088) != 0
    """State 7: End state"""
    return 0
    """Unused"""
    """State 4: Talk: Part 1_SubState"""
    # lot:1701000:Aged Feather, talk:70004200:"Bearer of the curse.", talk:70004260:"Do not resist. The dragon welcomes you."
    assert (talk_m10_27_x12(lot3=1701000, flag3=102096, text5=70004200, text6=70004260, z4=201180, z5=0,
            z6=0, z7=0))
    Goto('L0')
    """State 5: [Lib] Conversation: Item Transfer: Mes⇒Item⇒Mes: Important Item_SubState"""
    # lot:1701000:Aged Feather, talk:70004200:"Bearer of the curse.", talk:70004260:"Do not resist. The dragon welcomes you.", goods:60355000:Aged Feather
    assert (talk_m10_27_x16(lot2=1701000, flag2=102096, text3=70004200, text4=70004260, z2=201180, z3=0,
            goods2=60355000))
    Goto('L0')

def talk_m10_27_x21():
    """Waiting for hostility: Dragon Miko"""
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 40)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(127020132) != 1, 127020132, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(127020131) != 1, 127020131, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(127020130) != 1, 127020130, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(127020129) != 1, 127020129, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(127020128) != 1, 127020128, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(127020127) != 1, 127020127, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(127020126) != 1, 127020126, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(127020125) != 1, 127020125, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(127020124) != 1, 127020124, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 30 and GetRandomValue(0) < 40) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_27_x1(text1=70009420, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_27_x1(text1=70009410, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_27_x1(text1=70009400, z19=0, z21=-1, z22=0)
    else:
        pass
    """State 8: Hostility: End"""
    Label('L0')
    return 0
    """Unused"""
    """State 7: Conversation: 4_SubState attacked"""
    assert talk_m10_27_x1(text1=70009400, z19=0, z21=-1, z22=0)
    Goto('L0')

def talk_m10_27_x22(lot1=1701000, flag1=102096, text1=70004200, text2=70004260, z1=201180, goods1=60355000):
    """Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z1: Conversation: Global conversation flag
    goods1: Important items
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_27_x1(text1=text1, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z1, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L1')
        assert talk_m10_27_x1(text1=text2, z19=0, z21=-1, z22=0)
    # goods:60355000:Aged Feather
    elif call.Done() and (ItemCount(goods1, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # lot:1701000:Aged Feather
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_27_x17(z8=1011, lot1=lot1)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_27_x13(lot1=lot1, flag1=flag1, z1=z1, z3=0, z6=0, z7=0)
        Goto('L1')
    """State 10: End state"""
    return 0

def talk_m10_27_x23():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(100765) != 0 and GetEventFlag(208021) != 0:
        """State 8: [Lib] Conversation: Talk to 3_SubState"""
        # talk:69200900:"All men trust fully the illusion of life."
        assert talk_m10_27_x15(text7=69200900, z9=208022, z10=9901, z11=15)
        """State 4: YN dialog"""
        # action:1220:"What is your choice?"
        DisplayOwnYesNoMenu(1220, 15, -1, 0, 0, 0)
        if (YesNoMenuResult() == 3) != 0:
            pass
        elif (YesNoMenuResult() == 1) != 0:
            """State 9: [Lib] Conversation: After selection _SubState"""
            Label('L0')
            # talk:69201000:"I am Aldia."
            assert talk_m10_27_x1(text1=69201000, z19=208023, z21=15, z22=0)
            """State 5: Conversation flag check"""
            if GetEventFlag(208023) != 0:
                """State 3: End encounter flag"""
                SetEventFlag(100747, 1)
            elif GetEventFlag(208023) != 1:
                pass
        elif (YesNoMenuResult() == 2) != 0:
            Goto('L0')
    elif GetEventFlag(100765) != 0 and GetEventFlag(208020) != 0:
        """State 7: [Lib] Conversation: Talk to 2_SubState"""
        # talk:69200800:"Peace grants men the illusion of life."
        assert talk_m10_27_x15(text7=69200800, z9=208021, z10=9901, z11=15)
    elif GetEventFlag(100765) != 0:
        """State 6: [Lib] Conversation: Talk to 1_SubState"""
        # talk:69200700:"Young Hollow."
        assert talk_m10_27_x15(text7=69200700, z9=208020, z10=9901, z11=15)
    """State 2,10: End state"""
    return 0

def talk_m10_27_4100000():
    """Andyel"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(100747) != 0:
            break
        else:
            """State 3: Andyel: Conversation_SubState"""
            assert talk_m10_27_x23()
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

