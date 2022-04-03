# -*- coding: utf-8 -*-
def talk_m20_11_7600():
    """Bard Girl 1"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_11_x9(flag6=103720, flag7=104220, flag8=211020101)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_11_x3(text7=76009200, z12=0, z13=20, z14=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_11_x6(flag5=211020102, text8=76009500, text9=76009500, z15=76009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_11_x7(text11=76009600, z17=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Bard Girl 1: Conversation_SubState"""
                call = talk_m20_11_x18()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_11_x5(text12=76009400, text13=76009410, text14=76009420, text15=76009400,
                                          flag9=211020105, flag10=211020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_11_x4(flag11=103720, text16=76009100, z18=0, z19=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(211020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(211020105) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_11_x8(text10=76009300, z16=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m20_11_7601():
    """Bard Girl 2"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_11_x9(flag6=103730, flag7=104230, flag8=211020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_11_x3(text7=76019200, z12=0, z13=20, z14=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_11_x6(flag5=211020122, text8=76019500, text9=76019500, z15=76019500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_11_x7(text11=76019600, z17=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Bard Girl 2: Conversation_SubState"""
                call = talk_m20_11_x19()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_11_x5(text12=76019400, text13=76019410, text14=76019420, text15=76019400,
                                          flag9=211020125, flag10=211020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_11_x4(flag11=103730, text16=76019100, z18=0, z19=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(211020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(211020125) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_11_x8(text10=76019300, z16=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m20_11_x0(text17=_, z22=_, z23=0):
    """[Lib] Conversation: General purpose
    text17: Conversation ID
    z22: Conversation flag
    z23: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text17, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z22, 1)
    SetEventFlag(z23, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_11_x1(text1=_, z18=0, z20=-1, z21=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z18: Conversation flag
    z20: Display distance
    z21: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z20)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m20_11_x2(text10=_, z16=0):
    """[Lib] Conversation: Event end
    text10: Conversation ID
    z16: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text10, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z16, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_11_x3(text7=_, z12=0, z13=20, z14=80):
    """[Lib] Reunion hostility
    text7: Conversation message ID
    z12: Conversation flag ID
    z13: Display distance
    z14: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m20_11_x16(text7=text7, z12=z12, z13=z13, z14=z14)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_11_x4(flag11=_, text16=_, z18=0, z19=0):
    """[Lib] First hostility
    flag11: Hostile: Global event flag
    text16: Conversation ID
    z18: Conversation flag
    z19: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag11, 1)
    SetEventFlag(z19, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag11) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m20_11_x1(text1=text16, z18=z18, z20=-1, z21=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_11_x5(text12=_, text13=_, text14=_, text15=_, flag9=_, flag10=_):
    """[Lib] Hostile waiting
    text12: Conversation ID: 1 attacked
    text13: Conversation ID: Attacked 2
    text14: Conversation ID: 3 attacked
    text15: Conversation ID: 4 attacked
    flag9: No use: Area and other flags
    flag10: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag10) != 1, flag10, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag9) != 1, flag9, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m20_11_x1(text1=text15, z18=0, z20=-1, z21=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_11_x1(text1=text14, z18=0, z20=-1, z21=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_11_x1(text1=text13, z18=0, z20=-1, z21=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_11_x1(text1=text12, z18=0, z20=-1, z21=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_11_x6(flag5=_, text8=_, text9=_, z15=_):
    """[Lib] Hostile state
    flag5: Area and other flags: HP decreased
    text8: Conversation ID: HP drop 1
    text9: Conversation ID: HP drop 2
    z15: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag5) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m20_11_x10(text8=text8, flag5=flag5)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_11_x10(text8=text9, flag5=flag5)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_11_x10(text8=text9, flag5=flag5)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m20_11_x7(text11=_, z17=0):
    """[Lib] Death status
    text11: Conversation ID
    z17: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m20_11_x2(text10=text11, z16=z17)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m20_11_x8(text10=_, z16=0):
    """[Lib] Murder status
    text10: Conversation ID
    z16: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_11_x2(text10=text10, z16=z16)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m20_11_x9(flag6=_, flag7=_, flag8=_):
    """[Lib] Event: Branch
    flag6: Hostile flag
    flag7: death flag
    flag8: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag7) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag8) != 0
    elif GetEventFlag(flag6) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m20_11_x10(text8=_, flag5=_):
    """[Lib] Conversation: HP drop
    text8: Conversation ID
    flag5: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag5, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_11_x11(lot4=1760010, flag4=102551, text5=76000500, text6=76000520, z7=0, z8=0, z9=0, z10=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot4: Item lottery ID
    flag4: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    z9: Emigration permission: Global event flag
    z10: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m20_11_x1(text1=text5, z18=0, z20=-1, z21=0)
    if call.Done() and GetEventFlag(flag4) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z7, 1)
        SetEventFlag(z9, 1)
        SetEventFlag(z10, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m20_11_x1(text1=text6, z18=0, z20=-1, z21=0)
    # lot:1760010:Smooth & Silky Stone
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z11=1011, lot1=lot4)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot4, flag1=flag4, z1=z7, z2=z8, z9=z9, z10=z10)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m20_11_x12(lot3=_, flag3=_, text4=_, z5=0, z6=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot3: Item lottery ID
    flag3: Item transfer: Global event flag
    text4: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m20_11_x1(text1=text4, z18=0, z20=-1, z21=0)
    if call.Done() and GetEventFlag(flag3) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z5, 1)
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z11=1011, lot1=lot3)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot3, flag1=flag3, z1=z5, z2=z6, z9=0, z10=0)
    """State 9: End state"""
    return 0

def talk_m20_11_x13(lot1=_, flag1=_, z1=0, z2=0, z9=0, z10=0):
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

def talk_m20_11_x14(lot2=1760110, flag2=102561, text2=76010420, text3=76010430, z3=0, z4=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot2: Item lottery ID
    flag2: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z3: Conversation: Global conversation flag
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m20_11_x1(text1=text2, z18=0, z20=-1, z21=0)
    if call.Done() and GetEventFlag(flag2) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z3, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m20_11_x1(text1=text3, z18=0, z20=-1, z21=0)
    # lot:1760110:Petrified Something
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z11=1011, lot1=lot2)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot2, flag1=flag2, z1=z3, z2=z4, z9=0, z10=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m20_11_x15(lot1=1760120, flag1=102562, text1=76010520, z1=0, z2=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    text1: Conversation ID
    z1: Conversation: Global conversation flag
    z2: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m20_11_x1(text1=text1, z18=0, z20=-1, z21=0)
    if call.Done() and GetEventFlag(flag1) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z1, 1)
    # lot:1760120:Fire Seed
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z11=1011, lot1=lot1)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot1, flag1=flag1, z1=z1, z2=z2, z9=0, z10=0)
    """State 6: End state"""
    return 0

def talk_m20_11_x16(text7=_, z12=0, z13=20, z14=80):
    """[Lib] Conversation: Hostile display only
    text7: Conversation ID
    z12: Conversation flag
    z13: Display distance
    z14: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), z13)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z12, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m20_11_x17(z11=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z11: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_11_x18():
    """Bard Girl 1: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102580) != 0 and GetEventFlag(102552) != 1 and GetEventFlag(203904) != 0:
        """State 9: Captive Girl: Achieved Rescue_SubState"""
        # lot:1760020:Divine Blessing, talk:76000600:"We hear a song in the distance."
        assert talk_m20_11_x12(lot3=1760020, flag3=102552, text4=76000600, z5=0, z6=0)
    elif (GetEventFlag(100950) != 0 and GetEventFlag(102550) != 1 and GetEventFlag(203904) != 0 and GetEventFlag(104220)
          != 1):
        """State 10: Equipment transfer_SubState"""
        # lot:1760000:Divine Blessing, talk:76006000:"All we can do...is sing..."
        assert talk_m20_11_x12(lot3=1760000, flag3=102550, text4=76006000, z5=0, z6=0)
    elif GetEventFlag(203904) != 0 and GetEventFlag(102551) != 1:
        """State 8: Conversation: Item transfer_SubState"""
        # lot:1760010:Smooth & Silky Stone, talk:76000500:"Is there anything wrong?", talk:76000520:"This is all that we can do."
        assert (talk_m20_11_x11(lot4=1760010, flag4=102551, text5=76000500, text6=76000520, z7=0, z8=0,
                z9=0, z10=0))
    elif GetEventFlag(203903) != 0:
        """State 7: Talk: Part 5_SubState"""
        # talk:76000400:"When we sing, the little ones dance."
        call = talk_m20_11_x0(text17=76000400, z22=203904, z23=0)
        if call.Done():
            pass
        elif (GetEventFlag(100950) != 0 and GetEventFlag(102550) != 1 and GetEventFlag(203904) != 0 and
              GetEventFlag(104220) != 1):
            pass
    elif GetEventFlag(203902) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:76000300:"Do you seek King Vendrick?"
        assert talk_m20_11_x0(text17=76000300, z22=203903, z23=0)
    elif GetEventFlag(203901) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:76000200:"We will sing here, forever,\nas we always have, from long, long ago."
        assert talk_m20_11_x0(text17=76000200, z22=203902, z23=0)
    elif GetEventFlag(203900) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:76000100:"We are Milfanito."
        assert talk_m20_11_x0(text17=76000100, z22=203901, z23=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:76000000:"We knew you were coming..."
        assert talk_m20_11_x0(text17=76000000, z22=203900, z23=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 11: End state"""
    return 0

def talk_m20_11_x19():
    """Bard Girl 2: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    if GetEventFlag(102580) != 0 and GetEventFlag(102562) != 1 and GetEventFlag(204003) != 0:
        """State 9: Captive Girl: Rescued Achievement: 1_SubState"""
        # talk:76010500:"We hear a song in the distance."
        assert talk_m20_11_x0(text17=76010500, z22=0, z23=0)
        """State 8: Captive Girl: Rescued Achievement: 2_SubState"""
        # lot:1760120:Fire Seed, talk:76010520:"Take this...\nWe Milfanito thank you."
        assert talk_m20_11_x15(lot1=1760120, flag1=102562, text1=76010520, z1=0, z2=0)
    elif (GetEventFlag(100950) != 0 and GetEventFlag(102560) != 1 and GetEventFlag(204003) != 0 and GetEventFlag(104230)
          != 1):
        """State 7: Equipment transfer_SubState"""
        # lot:1760100:Divine Blessing, talk:76016000:"We exist...to sing..."
        assert talk_m20_11_x12(lot3=1760100, flag3=102560, text4=76016000, z5=0, z6=0)
    elif GetEventFlag(204003) != 0 and GetEventFlag(102561) != 1:
        """State 11: Conversation: Item transfer: 1_SubState"""
        # talk:76010400:"Do you seek comfort, too?"
        assert talk_m20_11_x0(text17=76010400, z22=204003, z23=0)
        """State 10: Conversation: Item transfer: 2_SubState"""
        # lot:1760110:Petrified Something, talk:76010420:"Take this, at the very least.", talk:76010430:"This is all that we can do."
        assert talk_m20_11_x14(lot2=1760110, flag2=102561, text2=76010420, text3=76010430, z3=0, z4=0)
    elif GetEventFlag(204002) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:76010300:"The little ones\nwere born from the Great Dead One."
        call = talk_m20_11_x0(text17=76010300, z22=204003, z23=0)
        if call.Done():
            pass
        elif (GetEventFlag(100950) != 0 and GetEventFlag(102560) != 1 and GetEventFlag(204003) != 0 and
              GetEventFlag(104230) != 1):
            pass
    elif GetEventFlag(204001) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:76010200:"We sing eternally for those who\nbear death and Dark within themselves."
        assert talk_m20_11_x0(text17=76010200, z22=204002, z23=0)
    elif GetEventFlag(204000) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:76010100:"Milfanito, that is what we are called."
        assert talk_m20_11_x0(text17=76010100, z22=204001, z23=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:76010000:"Who are you..."
        assert talk_m20_11_x0(text17=76010000, z22=204000, z23=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 12: End state"""
    return 0

