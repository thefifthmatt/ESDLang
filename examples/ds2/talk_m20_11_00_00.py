# -*- coding: utf-8 -*-
def talk_m20_11_7600():
    """Bard Girl 1"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_11_x9(z21=103720, z22=104220, z23=211020101)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_11_x3(text7=76009200, z16=0, z17=20, z18=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_11_x6(z19=211020102, text8=76009500, text9=76009500, z20=76009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_11_x7(text11=76009600, z25=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Bard Girl 1: Conversation_SubState"""
            while True:
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
                                          z26=211020105, z27=211020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_11_x4(z28=103720, text16=76009100, z29=0, z30=0)
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
        talk_m20_11_x8(text10=76009300, z24=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_11_7601():
    """Bard Girl 2"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_11_x9(z21=103730, z22=104230, z23=211020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_11_x3(text7=76019200, z16=0, z17=20, z18=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_11_x6(z19=211020122, text8=76019500, text9=76019500, z20=76019500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_11_x7(text11=76019600, z25=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Bard Girl 2: Conversation_SubState"""
            while True:
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
                                          z26=211020125, z27=211020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_11_x4(z28=103730, text16=76019100, z29=0, z30=0)
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
        talk_m20_11_x8(text10=76019300, z24=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_11_x0(text17=_, z33=_, z34=0):
    """[Lib] Conversation: General purpose
    text17: Conversation ID
    z33: Conversation flag
    z34: Global event flag
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
    SetEventFlag(z33, 1)
    SetEventFlag(z34, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_11_x1(text1=_, z29=0, z31=-1, z32=0):
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

def talk_m20_11_x2(text10=_, z24=0):
    """[Lib] Conversation: Event end
    text10: Conversation ID
    z24: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text10, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z24, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_11_x3(text7=_, z16=0, z17=20, z18=80):
    """[Lib] Reunion hostility
    text7: Conversation message ID
    z16: Conversation flag ID
    z17: Display distance
    z18: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m20_11_x16(text7=text7, z16=z16, z17=z17, z18=z18)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_11_x4(z28=_, text16=_, z29=0, z30=0):
    """[Lib] First hostility
    z28: Hostile: Global event flag
    text16: Conversation ID
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
    assert talk_m20_11_x1(text1=text16, z29=z29, z31=-1, z32=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_11_x5(text12=_, text13=_, text14=_, text15=_, z26=_, z27=_):
    """[Lib] Hostile waiting
    text12: Conversation ID: 1 attacked
    text13: Conversation ID: Attacked 2
    text14: Conversation ID: 3 attacked
    text15: Conversation ID: 4 attacked
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
        assert talk_m20_11_x1(text1=text15, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_11_x1(text1=text14, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_11_x1(text1=text13, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_11_x1(text1=text12, z29=0, z31=-1, z32=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_11_x6(z19=_, text8=_, text9=_, z20=_):
    """[Lib] Hostile state
    z19: Area and other flags: HP decreased
    text8: Conversation ID: HP drop 1
    text9: Conversation ID: HP drop 2
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
            assert talk_m20_11_x10(text8=text8, z19=z19)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_11_x10(text8=text9, z19=z19)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_11_x10(text8=text9, z19=z19)

def talk_m20_11_x7(text11=_, z25=0):
    """[Lib] Death status
    text11: Conversation ID
    z25: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m20_11_x2(text10=text11, z24=z25)

def talk_m20_11_x8(text10=_, z24=0):
    """[Lib] Murder status
    text10: Conversation ID
    z24: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_11_x2(text10=text10, z24=z24)

def talk_m20_11_x9(z21=_, z22=_, z23=_):
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

def talk_m20_11_x10(text8=_, z19=_):
    """[Lib] Conversation: HP drop
    text8: Conversation ID
    z19: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z19, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_11_x11(lot4=1760010, z10=102551, text5=76000500, text6=76000520, z11=0, z12=0, z13=0, z14=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot4: Item lottery ID
    z10: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z11: Conversation: Global conversation flag
    z12: Trophy acquisition: Area and other flags
    z13: Emigration permission: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m20_11_x1(text1=text5, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z10) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z11, 1)
        SetEventFlag(z13, 1)
        SetEventFlag(z14, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m20_11_x1(text1=text6, z29=0, z31=-1, z32=0)
    # lot:1760010:Smooth & Silky Stone
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z15=1011, lot1=lot4)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot4, z1=z10, z2=z11, z3=z12, z13=z13, z14=z14)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m20_11_x12(lot3=_, z7=_, text4=_, z8=0, z9=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot3: Item lottery ID
    z7: Item transfer: Global event flag
    text4: Conversation ID
    z8: Conversation: Global conversation flag
    z9: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m20_11_x1(text1=text4, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z7) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z8, 1)
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z15=1011, lot1=lot3)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot3, z1=z7, z2=z8, z3=z9, z13=0, z14=0)
    """State 9: End state"""
    return 0

def talk_m20_11_x13(lot1=_, z1=_, z2=0, z3=0, z13=0, z14=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z13: Emigration permission: Global event flag
    z14: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z14, 1)
    SetEventFlag(z13, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_11_x14(lot2=1760110, z4=102561, text2=76010420, text3=76010430, z5=0, z6=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot2: Item lottery ID
    z4: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m20_11_x1(text1=text2, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z4) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z5, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m20_11_x1(text1=text3, z29=0, z31=-1, z32=0)
    # lot:1760110:Petrified Something
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z15=1011, lot1=lot2)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot2, z1=z4, z2=z5, z3=z6, z13=0, z14=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m20_11_x15(lot1=1760120, z1=102562, text1=76010520, z2=0, z3=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot1: Item lottery ID
    z1: Item transfer: Global event flag
    text1: Conversation ID
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m20_11_x1(text1=text1, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z1) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    # lot:1760120:Fire Seed
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_11_x17(z15=1011, lot1=lot1)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_11_x13(lot1=lot1, z1=z1, z2=z2, z3=z3, z13=0, z14=0)
    """State 6: End state"""
    return 0

def talk_m20_11_x16(text7=_, z16=0, z17=20, z18=80):
    """[Lib] Conversation: Hostile display only
    text7: Conversation ID
    z16: Conversation flag
    z17: Display distance
    z18: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), z17)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z16, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m20_11_x17(z15=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z15: Text ID
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
        assert talk_m20_11_x12(lot3=1760020, z7=102552, text4=76000600, z8=0, z9=0)
    elif (GetEventFlag(100950) != 0 and GetEventFlag(102550) != 1 and GetEventFlag(203904) != 0 and GetEventFlag(104220)
          != 1):
        """State 10: Equipment transfer_SubState"""
        # lot:1760000:Divine Blessing, talk:76006000:"All we can do...is sing..."
        assert talk_m20_11_x12(lot3=1760000, z7=102550, text4=76006000, z8=0, z9=0)
    elif GetEventFlag(203904) != 0 and GetEventFlag(102551) != 1:
        """State 8: Conversation: Item transfer_SubState"""
        # lot:1760010:Smooth & Silky Stone, talk:76000500:"Is there anything wrong?", talk:76000520:"This is all that we can do."
        assert (talk_m20_11_x11(lot4=1760010, z10=102551, text5=76000500, text6=76000520, z11=0, z12=0,
                z13=0, z14=0))
    elif GetEventFlag(203903) != 0:
        """State 7: Talk: Part 5_SubState"""
        # talk:76000400:"When we sing, the little ones dance."
        call = talk_m20_11_x0(text17=76000400, z33=203904, z34=0)
        if call.Done():
            pass
        elif (GetEventFlag(100950) != 0 and GetEventFlag(102550) != 1 and GetEventFlag(203904) != 0 and
              GetEventFlag(104220) != 1):
            pass
    elif GetEventFlag(203902) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:76000300:"Do you seek King Vendrick?"
        assert talk_m20_11_x0(text17=76000300, z33=203903, z34=0)
    elif GetEventFlag(203901) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:76000200:"We will sing here, forever,\nas we always have, from long, long ago."
        assert talk_m20_11_x0(text17=76000200, z33=203902, z34=0)
    elif GetEventFlag(203900) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:76000100:"We are Milfanito."
        assert talk_m20_11_x0(text17=76000100, z33=203901, z34=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:76000000:"We knew you were coming..."
        assert talk_m20_11_x0(text17=76000000, z33=203900, z34=0)
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
        assert talk_m20_11_x0(text17=76010500, z33=0, z34=0)
        """State 8: Captive Girl: Rescued Achievement: 2_SubState"""
        # lot:1760120:Fire Seed, talk:76010520:"Take this...\nWe Milfanito thank you."
        assert talk_m20_11_x15(lot1=1760120, z1=102562, text1=76010520, z2=0, z3=0)
    elif (GetEventFlag(100950) != 0 and GetEventFlag(102560) != 1 and GetEventFlag(204003) != 0 and GetEventFlag(104230)
          != 1):
        """State 7: Equipment transfer_SubState"""
        # lot:1760100:Divine Blessing, talk:76016000:"We exist...to sing..."
        assert talk_m20_11_x12(lot3=1760100, z7=102560, text4=76016000, z8=0, z9=0)
    elif GetEventFlag(204003) != 0 and GetEventFlag(102561) != 1:
        """State 11: Conversation: Item transfer: 1_SubState"""
        # talk:76010400:"Do you seek comfort, too?"
        assert talk_m20_11_x0(text17=76010400, z33=204003, z34=0)
        """State 10: Conversation: Item transfer: 2_SubState"""
        # lot:1760110:Petrified Something, talk:76010420:"Take this, at the very least.", talk:76010430:"This is all that we can do."
        assert talk_m20_11_x14(lot2=1760110, z4=102561, text2=76010420, text3=76010430, z5=0, z6=0)
    elif GetEventFlag(204002) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:76010300:"The little ones\nwere born from the Great Dead One."
        call = talk_m20_11_x0(text17=76010300, z33=204003, z34=0)
        if call.Done():
            pass
        elif (GetEventFlag(100950) != 0 and GetEventFlag(102560) != 1 and GetEventFlag(204003) != 0 and
              GetEventFlag(104230) != 1):
            pass
    elif GetEventFlag(204001) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:76010200:"We sing eternally for those who\nbear death and Dark within themselves."
        assert talk_m20_11_x0(text17=76010200, z33=204002, z34=0)
    elif GetEventFlag(204000) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:76010100:"Milfanito, that is what we are called."
        assert talk_m20_11_x0(text17=76010100, z33=204001, z34=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:76010000:"Who are you..."
        assert talk_m20_11_x0(text17=76010000, z33=204000, z34=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 12: End state"""
    return 0

