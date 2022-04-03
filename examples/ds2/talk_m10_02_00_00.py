# -*- coding: utf-8 -*-
def talk_m10_02_7050():
    """Retired fire prevention woman 1 (Strohn)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_02_x8(flag7=103560, flag8=104060, flag9=102020106)
        if call.Get() == 1:
            """State 7: [Lib] Reunion hostility_SubState"""
            call = talk_m10_02_x3(text12=70509010, z9=0, z10=20, z11=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_02_x6(flag6=102020107, text14=70509090, text15=70509090, z17=70509090)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 9: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_02_x7(text16=70509020, z18=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Retired fire prevention woman 1: Conversation_SubState"""
                call = talk_m10_02_x21()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (HpValue() > 1) != 1:
                    break
                elif GetEventFlag(103570) != 0 and GetEventFlag(104060) != 1:
                    """State 2: Conversation: Delete key guide"""
                    Label('L2')
                    DeleteKeyGuideArea()
                    """State 11: [Lib] First adversification_ (No Mes) _SubState"""
                    call = talk_m10_02_x15(flag5=103560, z12=0)
                    if call.Done():
                        Goto('L0')
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                elif GetEventFlag(103580) != 0 and GetEventFlag(104060) != 1:
                    Goto('L2')
                elif GetEventFlag(103600) != 0 and GetEventFlag(104060) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L3')
                    call = talk_m10_02_x5(text17=70509020, text18=70509030, text19=70509040, text20=70509040,
                                          flag10=102020120, flag11=102020121)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 6: [Lib] First adversification_SubState"""
                        call = talk_m10_02_x4(flag12=103560, text21=70509000, z19=0, z20=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(102020121) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(102020120) != 1:
                    Goto('L3')
        """State 12: Death state: Dedicated _SubState"""
        talk_m10_02_x32(text1=70509060, z1=103560)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_02_7051():
    """Retired Fire Guard 2 (Gliant)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_02_x8(flag7=103570, flag8=104070, flag9=102020111)
        if call.Get() == 1:
            """State 8: [Lib] Reunion hostility_SubState"""
            call = talk_m10_02_x3(text12=70519200, z9=0, z10=20, z11=80)
            if call.Done():
                """State 9: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_02_x6(flag6=102020112, text14=70519500, text15=70519500, z17=70519500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 10: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_02_x7(text16=70519500, z18=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 5: Retired Firemen 2 & 3: Conversation_SubState"""
                # talk:70511000:"Hah hah hah...", talk:70511100:"..."
                call = talk_m10_02_x24(text4=70511000, text5=70511100, flag1=202000)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (HpValue() > 1) != 1:
                    break
                elif GetEventFlag(103560) != 0 and GetEventFlag(104070) != 1:
                    """State 2: Conversation: Delete key guide"""
                    Label('L2')
                    DeleteKeyGuideArea()
                    """State 11: [Lib] First adversification_ (No Mes) _SubState"""
                    call = talk_m10_02_x15(flag5=103570, z12=0)
                    if call.Done():
                        Goto('L0')
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                elif GetEventFlag(103580) != 0 and GetEventFlag(104070) != 1:
                    Goto('L2')
                elif GetEventFlag(103600) != 0 and GetEventFlag(104070) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L3')
                    call = talk_m10_02_x5(text17=70519300, text18=70519300, text19=70519400, text20=70519410,
                                          flag10=102020122, flag11=102020123)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 7: [Lib] First adversification_SubState"""
                        call = talk_m10_02_x4(flag12=103570, text21=70519100, z19=0, z20=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(102020123) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(102020122) != 1:
                    Goto('L3')
        """State 12: Death state: Dedicated _SubState"""
        talk_m10_02_x32(text1=70519600, z1=103570)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_02_7053():
    """Retired fire prevention woman 3 (mol)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_02_x8(flag7=103580, flag8=104080, flag9=102020116)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_02_x3(text12=70529200, z9=0, z10=20, z11=80)
            if call.Done():
                """State 9: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_02_x6(flag6=102020117, text14=70529500, text15=70529500, z17=70529500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 6: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_02_x7(text16=70529500, z18=0)
                    Quit()
            elif KilledPlayer() != 0:
                Goto('L1')
            elif (HpValue() > 1) != 1:
                pass
        elif call.Get() == 0:
            while True:
                """State 11: Retired Firemen 2 & 3: Conversation_SubState"""
                # talk:70521000:"Hah hah hah...", talk:70521100:"..."
                call = talk_m10_02_x24(text4=70521000, text5=70521100, flag1=202100)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (HpValue() > 1) != 1:
                    break
                elif GetEventFlag(103560) != 0 and GetEventFlag(104080) != 1:
                    """State 2: Conversation: Delete key guide"""
                    Label('L2')
                    DeleteKeyGuideArea()
                    """State 10: [Lib] First adversification_ (No Mes) _SubState"""
                    call = talk_m10_02_x15(flag5=103580, z12=0)
                    if call.Done():
                        Goto('L0')
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                elif GetEventFlag(103570) != 0 and GetEventFlag(104080) != 1:
                    Goto('L2')
                elif GetEventFlag(103600) != 0 and GetEventFlag(104080) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 8: [Lib] Hostile waiting_SubState"""
                    Label('L3')
                    call = talk_m10_02_x5(text17=70529300, text18=70529300, text19=70529400, text20=70529410,
                                          flag10=102020124, flag11=102020125)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 7: [Lib] First adversification_SubState"""
                        call = talk_m10_02_x4(flag12=103580, text21=70529100, z19=0, z20=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(102020125) != 1:
                    Goto('L3')
                elif GetEventFlag(102020124) != 1 and (NumberOfTimesDamaged(1) > 1) != 0:
                    Goto('L3')
        """State 12: Death state: Dedicated _SubState"""
        talk_m10_02_x32(text1=70529600, z1=103580)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_02_7230():
    """Firefighter housekeeper"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_02_x8(flag7=103600, flag8=104100, flag9=102020101)
        if call.Get() == 1:
            """State 7: [Lib] Reunion hostility_SubState"""
            call = talk_m10_02_x3(text12=72309200, z9=0, z10=20, z11=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_02_x6(flag6=102020102, text14=72309500, text15=72309500, z17=72309500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 9: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_02_x7(text16=72309300, z18=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 11: Firekeeper's Housekeeper: Conversation_SubState"""
                call = talk_m10_02_x25()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (HpValue() > 1) != 1:
                    break
                elif GetEventFlag(103560) != 0 and GetEventFlag(104100) != 1:
                    """State 2: Conversation: Delete key guide"""
                    Label('L2')
                    DeleteKeyGuideArea()
                    """State 10: [Lib] First adversarial (at the time of fire woman attack) _SubState"""
                    # talk:72305000:"What are you doing!"
                    call = talk_m10_02_x4(flag12=103600, text21=72305000, z19=0, z20=0)
                    if call.Done():
                        Goto('L0')
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                elif GetEventFlag(103570) != 0 and GetEventFlag(104100) != 1:
                    Goto('L2')
                elif GetEventFlag(103580) != 0 and GetEventFlag(104100) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L3')
                    call = talk_m10_02_x5(text17=72309400, text18=72309410, text19=72309420, text20=72309400,
                                          flag10=102020126, flag11=102020127)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 6: [Lib] First adversification_SubState"""
                        call = talk_m10_02_x4(flag12=103600, text21=72309100, z19=0, z20=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(102020127) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(102020126) != 1:
                    Goto('L3')
        """State 12: Death state: Dedicated _SubState"""
        talk_m10_02_x32(text1=72309600, z1=103600)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_02_7900():
    """Glitter girl"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        Label('L0')
        if IsGuest() != 0:
            break
        elif (GetStateTime() >= 0) != 0 and (GetStateTime() > GetRandomValueForStateTime(0.1, 3)) != 0:
            pass
        elif (DistanceFromPlayer() > 4) != 0:
            Goto('L3')
        """State 9: Kirakira Musume: Area Intrusion_SubState"""
        call = talk_m10_02_x31()
        if call.Done():
            continue
        elif (not GetAreaVariable(60)) != 1:
            """State 5: Kirakira Musume: Gacha Run"""
            Label('L1')
            if (GetAreaVariable(60) == 1) != 0 and CrowExhangePossibleDisplay() != 0:
                """State 8: _SubState with non-exchangeable items"""
                # talk:78600400:"You, you,\nnot like that."
                assert talk_m10_02_x1(text2=78600400, z19=0, z21=3, z22=0)
            elif (GetAreaVariable(60) == 4) != 0 and CrowExhangePossibleDisplay() != 0:
                """State 7: _SubState with eggs fossil or small or slippery stones"""
                Label('L2')
                # talk:78600300:"Yah, yah.\nSo nice, so smooth."
                assert talk_m10_02_x1(text2=78600300, z19=0, z21=3, z22=0)
            elif (GetAreaVariable(60) == 2) != 0 and CrowExhangePossibleDisplay() != 0:
                Goto('L2')
            elif (GetAreaVariable(60) == 3) != 0 and CrowExhangePossibleDisplay() != 0:
                Goto('L2')
            elif (GetAreaVariable(60) == 5) != 0 and CrowExhangePossibleDisplay() != 0:
                Goto('L2')
            """State 4: Kirakira Musume: Area variable: Reset"""
            SetAreaVariable(60, 0)
            continue
        elif ConversationEnded() != 0 and (DistanceFromPlayer() > 6) != 0:
            continue
        """State 3: Kirakira Musume: No area intrusion"""
        Label('L3')
        SetEventFlag(102020001, 0)
        assert (DistanceFromPlayer() > 3) != 1
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: Kirakira Musume: After acquisition: Wait"""
    if ConversationEnded() != 0 and (DistanceFromPlayer() > 6) != 0:
        Goto('L0')
    elif ItemAwardDisplay() != 0:
        Goto('L1')
    elif (GetStateTime() > GetRandomValueForStateTime(180, 180)) != 0:
        Goto('L0')

def talk_m10_02_x0(text4=_, flag1=_, z23=0):
    """[Lib] Conversation: General purpose
    text4: Conversation ID
    flag1: Conversation flag
    z23: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text4, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(flag1, 1)
    SetEventFlag(z23, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_02_x1(text2=_, z19=_, z21=_, z22=0):
    """[Lib] Conversation: Display only
    text2: Conversation ID
    z19: Conversation flag
    z21: Display distance
    z22: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text2, GetCommonEventParamDecimal(7), z21)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z19, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_02_x2(text1=_, z18=0):
    """[Lib] Conversation: Event end
    text1: Conversation ID
    z18: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_02_x3(text12=_, z9=0, z10=20, z11=80):
    """[Lib] Reunion hostility
    text12: Conversation message ID
    z9: Conversation flag ID
    z10: Display distance
    z11: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_02_x16(text12=text12, z9=z9, z10=z10, z11=z11)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_02_x4(flag12=_, text21=_, z19=0, z20=0):
    """[Lib] First hostility
    flag12: Hostile: Global event flag
    text21: Conversation ID
    z19: Conversation flag
    z20: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag12, 1)
    SetEventFlag(z20, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag12) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_02_x1(text2=text21, z19=z19, z21=-1, z22=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_02_x5(text17=_, text18=_, text19=_, text20=_, flag10=_, flag11=_):
    """[Lib] Hostile waiting
    text17: Conversation ID: 1 attacked
    text18: Conversation ID: Attacked 2
    text19: Conversation ID: 3 attacked
    text20: Conversation ID: 4 attacked
    flag10: No use: Area and other flags
    flag11: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag11) != 1, flag11, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag10) != 1, flag10, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_02_x1(text2=text20, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_02_x1(text2=text19, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_02_x1(text2=text18, z19=0, z21=-1, z22=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_02_x1(text2=text17, z19=0, z21=-1, z22=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_02_x6(flag6=_, text14=_, text15=_, z17=_):
    """[Lib] Hostile state
    flag6: Area and other flags: HP decreased
    text14: Conversation ID: HP drop 1
    text15: Conversation ID: HP drop 2
    z17: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag6) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_02_x9(text14=text14, flag6=flag6)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_02_x9(text14=text15, flag6=flag6)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_02_x9(text14=text15, flag6=flag6)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_02_x7(text16=_, z18=0):
    """[Lib] Murder status
    text16: Conversation ID
    z18: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_02_x2(text1=text16, z18=z18)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_02_x8(flag7=_, flag8=_, flag9=_):
    """[Lib] Event: Branch
    flag7: Hostile flag
    flag8: death flag
    flag9: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag8) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag9) != 0
    elif GetEventFlag(flag7) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_02_x9(text14=_, flag6=_):
    """[Lib] Conversation: HP drop
    text14: Conversation ID
    flag6: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text14, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag6, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_02_x10(z13=0, z14=220, z15=70500000, z16=0):
    """[Lib] Menu start: General purpose
    z13: Camera parameter ID
    z14: Target Damipoly ID
    z15: NPC event parameter ID
    z16: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z16, z13, z14, z15)
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

def talk_m10_02_x11(text13=70509020):
    """[Lib] Menu cancellation: General purpose
    text13: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_02_x1(text2=text13, z19=0, z21=-1, z22=0)
    """State 4: End state"""
    return 0

def talk_m10_02_x12(lot2=1723000, flag3=102280, text7=72306000, text8=72306020, z4=0, z5=0, z6=0, z7=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot2: Item lottery ID
    flag3: Item transfer: Global event flag
    text7: First half: Conversation ID
    text8: Second half: Conversation ID
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
    call = talk_m10_02_x1(text2=text7, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag3) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z4, 1)
        SetEventFlag(z6, 1)
        SetEventFlag(z7, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_02_x1(text2=text8, z19=0, z21=-1, z22=0)
    # lot:1723000:Handmaid's Ladle
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_02_x20(z8=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_02_x13(lot1=lot2, flag2=flag3, z2=z4, z3=z5, z6=z6, z7=z7)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_02_x13(lot1=_, flag2=_, z2=0, z3=0, z6=0, z7=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    flag2: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z6: Emigration permission: Global event flag
    z7: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z7, 1)
    SetEventFlag(z6, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(flag2, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_02_x14(lot1=1705000, flag2=102180, text6=70509070, z2=0, z3=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot1: Item lottery ID
    flag2: Item transfer: Global event flag
    text6: Conversation ID
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m10_02_x1(text2=text6, z19=0, z21=-1, z22=0)
    if call.Done() and GetEventFlag(flag2) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    # lot:1705000:Human Effigy
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_02_x20(z8=1011, lot1=lot1)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_02_x13(lot1=lot1, flag2=flag2, z2=z2, z3=z3, z6=0, z7=0)
    """State 6: End state"""
    return 0

def talk_m10_02_x15(flag5=_, z12=0):
    """[Lib] First hostility _ (without Mes)
    flag5: Hostile: Global event flag
    z12: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag5, 1)
    SetEventFlag(z12, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag5) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: First hostility: end"""
    return 0

def talk_m10_02_x16(text12=_, z9=0, z10=20, z11=80):
    """[Lib] Conversation: Hostile display only
    text12: Conversation ID
    z9: Conversation flag
    z10: Display distance
    z11: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text12, GetCommonEventParamDecimal(7), z10)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z9, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_02_x17(action2=1200, goods2=50960000):
    """[Lib] Selection dialog: Item display
    action2: Dialog: Text ID
    goods2: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    # action:1200:"Give\n%s?", goods:50960000:Soul Vessel
    DisplayOwnYesNoMenu(action2, 0, -1, 2, goods2, 0)
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

def talk_m10_02_x18(action1=1206, goods1=50960000):
    """[Lib] OK dialog: Item display
    action1: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: OK dialog: Display"""
    # action:1206:"You do not have\n%s", goods:50960000:Soul Vessel
    DisplayOwnOkMenu(action1, 0, 0, -1, 2, goods1, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_02_x19(text9=70501500, text10=70501300, text11=70501310, flag4=102020128):
    """[Lib] Menu ends: 2 times when not purchased
    text9: Conversation ID (at the time of purchase)
    text10: Conversation ID (when not purchasing: 1)
    text11: Conversation ID (when not purchasing: 2)
    flag4: Purchase flag: Area other flags
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(flag4) != 0:
        """State 2: Purchase and leave _SubState"""
        Label('L0')
        assert talk_m10_02_x1(text2=text9, z19=0, z21=-1, z22=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        Goto('L0')
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase: 1_SubState"""
        assert talk_m10_02_x1(text2=text10, z19=0, z21=-1, z22=0)
        """State 4: Leave without purchase: 2_SubState"""
        assert talk_m10_02_x1(text2=text11, z19=0, z21=-1, z22=0)
    """State 5: End state"""
    return 0

def talk_m10_02_x20(z8=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z8: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_02_x21():
    """Retired fire prevention woman 1: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102181) != 0:
        """State 3: Retired Fire Defense 1: Conversation after moving to Madura_SubState"""
        assert talk_m10_02_x23()
    else:
        """State 2: Retired Fire Defense Woman 1: Conversation before moving to Madura_SubState"""
        assert talk_m10_02_x22()
    """State 4: End state"""
    return 0

def talk_m10_02_x22():
    """Retired Fire Defense 1: Conversation before moving to Madura"""
    """State 0,1: Conversation: Start"""
    if GetEventFlag(201900) != 0:
        """State 3: Talk: Loop_SubState"""
        # talk:70501100:"Now, go along, go along... Heh heh..."
        assert talk_m10_02_x0(text4=70501100, flag1=0, z23=0)
    else:
        """State 2: Talk: First time: 1_SubState"""
        # talk:70501000:"You must go, on a journey without rest."
        assert talk_m10_02_x0(text4=70501000, flag1=0, z23=0)
        """State 4: Talk: First time: 2_SubState"""
        # talk:70501040:"Hah hah hah..."
        assert talk_m10_02_x1(text2=70501040, z19=201900, z21=-1, z22=0)
    """State 5: End state"""
    return 0

def talk_m10_02_x23():
    """Retired Fire Defense 1: Conversation after moving to Madura"""
    """State 0,1,2: Talk to: Restate status_SubState"""
    # talk:70501200:"Still determined as ever, I see... Heh heh..."
    assert talk_m10_02_x0(text4=70501200, flag1=0, z23=0)
    """State 3: Retired fire prevention woman 1: NPC menu_SubState"""
    assert talk_m10_02_x26()
    """State 4: End state"""
    return 0

def talk_m10_02_x24(text4=_, text5=_, flag1=_):
    """Retired Firemen 2 & 3: Conversation
    text4: Talking part 1
    text5: Talking part 2
    flag1: Speaking part 1: Global conversation flag
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(flag1) != 0:
        """State 4: Talk to: 2_SubState"""
        assert talk_m10_02_x0(text4=text5, flag1=0, z23=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        assert talk_m10_02_x0(text4=text4, flag1=flag1, z23=0)
    """State 2,5: End state"""
    return 0

def talk_m10_02_x25():
    """Firefighter Housekeeper: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102281) != 0 and GetEventFlag(102280) != 1 and GetEventFlag(104100) != 1:
        """State 7: Equipment transfer (condition: clear tutorial) _SubState"""
        # lot:1723000:Handmaid's Ladle, talk:72306000:"Have a safe journey..."
        assert (talk_m10_02_x12(lot2=1723000, flag3=102280, text7=72306000, text8=72306020, z4=0, z5=0,
                z6=0, z7=0))
    elif GetEventFlag(202402) != 0:
        """State 6: Talk: Part 5_SubState"""
        # talk:72300500:"The old women are sisters.\nI am told there was a fourth."
        assert talk_m10_02_x0(text4=72300500, flag1=0, z23=0)
    elif GetEventFlag(202401) != 0:
        """State 5: Talk: 4_SubState"""
        # talk:72300400:"The old women were keepers of the fire."
        assert talk_m10_02_x0(text4=72300400, flag1=202402, z23=0)
    elif GetEventFlag(202400) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:72300300:"My name is Milibeth."
        assert talk_m10_02_x0(text4=72300300, flag1=202401, z23=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:72300000:"That was dangerously close."
        assert talk_m10_02_x0(text4=72300000, flag1=202400, z23=0)
    """State 2,8: End state"""
    return 0

def talk_m10_02_x26():
    """Retired fire prevention woman 1: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 3,4: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_02_x10(z13=0, z14=220, z15=70500000, z16=0)
        if call.Get() == 11:
            """State 7: Retired Fire Guard 1: Status Reset_SubState"""
            call = talk_m10_02_x28()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0 and PlayerIsInEventAction(9) != 1:
                break
        elif call.Get() == 2:
            """State 6: Retired fire prevention woman 1: Menu conversation_SubState"""
            call = talk_m10_02_x27()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 1:
            """State 8: [Lib] Menu exit: Non-purchase x 2_SubState"""
            # talk:70501500:"Now, go along.", talk:70501300:"No, of course not.", talk:70501310:"Now, go along then... Heh heh..."
            assert talk_m10_02_x19(text9=70501500, text10=70501300, text11=70501310, flag4=102020128)
        elif call.Get() == 0:
            break
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuResults()
        EndPlayerActionRequest()
        """State 9: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    assert talk_m10_02_x11(text13=70509020)
    Goto('L0')

def talk_m10_02_x27():
    """Retired fire prevention woman 1: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    # goods:40510000:King's Ring
    if (ItemCount(40510000, 1, 1, 0) > 1) != 0 and GetEventFlag(102180) != 1 and GetEventFlag(104060) != 1:
        """State 4: Equipment transfer (condition: possession of king's ring) _SubState"""
        # lot:1705000:Human Effigy
        assert talk_m10_02_x14(lot1=1705000, flag2=102180, text6=70509070, z2=0, z3=0)
    else:
        """State 3: Talk to _First_SubState"""
        # talk:70501000:"You must go, on a journey without rest."
        assert talk_m10_02_x1(text2=70501000, z19=0, z21=-1, z22=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_02_x28():
    """Retired Fire Guard 1: Status Reset"""
    """State 0,1: Status reset: Start"""
    assert (GetStateTime() > GetRandomValueForStateTime(0.1, 0.1)) != 0
    """State 7: [Lib] Selection dialog: Item display_SubState"""
    # action:1200:"Give\n%s?", goods:50960000:Soul Vessel
    call = talk_m10_02_x17(action2=1200, goods2=50960000)
    # goods:50960000:Soul Vessel
    if call.Get() == 0 and (ItemCount(50960000, 1, 1, 0) > 1) != 1:
        """State 8: Item not possession confirmation dialog_SubState"""
        # action:1206:"You do not have\n%s", goods:50960000:Soul Vessel
        assert talk_m10_02_x18(action1=1206, goods1=50960000)
        """State 9: Status reset rejection: 1_SubState"""
        # talk:70501400:"Oh, but you don't have what's needed."
        assert talk_m10_02_x1(text2=70501400, z19=0, z21=-1, z22=0)
        """State 10: Status reset rejection: 2_SubState"""
        # talk:70501420:"Go along, then.\nOld hags don't bargain, dearie... Heh heh..."
        assert talk_m10_02_x1(text2=70501420, z19=0, z21=-1, z22=0)
        """State 2: Status reset: Finish"""
        Label('L0')
        EndPlayerActionRequest()
        ClearNpcMenuSelection()
    elif call.Get() == 0:
        """State 5: Status reset: kneeling"""
        PlayerActionRequest(9)
        """State 3: Status reset: Display"""
        OpenRespecMenu(0, 220, 0)
        assert RespecMenuDisplay() != 0
        """State 4: Status reset: Standby"""
        if RespecMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
            """State 6: Status reset: End of change"""
            EndPlayerActionRequest()
            ClearNpcMenuSelection()
            SetEventFlag(102020128, 1)
        elif RespecMenuDisplay() != 1:
            Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 2:
        Goto('L0')
    """State 11: End state"""
    return 0

def talk_m10_02_x29():
    """Kirakira Musume: Random playback"""
    """State 0,1: Random playback: Start"""
    GenerateRandomNumber(0, 0, 20)
    assert (GetStateTime() >= 0) != 0 and (GetStateTime() > GetRandomValueForStateTime(0.1, 3)) != 0
    """State 2: Random playback: Branch"""
    if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0 and ItemAwardDisplay() != 1:
        """State 3: Enter a certain area: Random 1_SubState"""
        # talk:78600000:"You, you,\ngive us smooth."
        assert talk_m10_02_x1(text2=78600000, z19=0, z21=3, z22=0)
        """State 5: Enter a certain area: Random 1: Continuous playback_SubState"""
        # talk:78600100:"You! You!\nGive us smooth!", talk:78600000:"You, you,\ngive us smooth."
        talk_m10_02_x30(text2=78600100, text3=78600000)
        Quit()
    elif ItemAwardDisplay() != 1:
        """State 4: Enter a certain area: Random 2_SubState"""
        # talk:78600100:"You! You!\nGive us smooth!"
        assert talk_m10_02_x1(text2=78600100, z19=0, z21=3, z22=0)
        """State 6: Enter a certain area: Random 2: Continuous playback_SubState"""
        # talk:78600000:"You, you,\ngive us smooth.", talk:78600100:"You! You!\nGive us smooth!"
        talk_m10_02_x30(text2=78600000, text3=78600100)
        Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_02_x30(text2=_, text3=_):
    """Kirakira Musume: Random playback: Playback
    text2: First conversation
    text3: Next conversation
    """
    """State 0: Start state"""
    while True:
        """State 1: Play: First conversation: Wait"""
        assert (GetStateTime() > GetRandomValueForStateTime(30, 60)) != 0
        """State 3: First conversation_SubState"""
        assert talk_m10_02_x1(text2=text2, z19=0, z21=3, z22=0)
        """State 2: Play: Next conversation: Wait"""
        assert (GetStateTime() > GetRandomValueForStateTime(30, 60)) != 0
        """State 4: Next conversation_SubState"""
        assert talk_m10_02_x1(text2=text3, z19=0, z21=3, z22=0)
    """Unused"""
    """State 5: End state"""
    return 0

def talk_m10_02_x31():
    """Kirakira Musume: Area invasion"""
    """State 0,1: Intrusion: Start"""
    SetEventFlag(102020001, 1)
    """State 2: Kirakira Musume: Random Playback_SubState"""
    assert talk_m10_02_x29()
    """State 3: End state"""
    return 0

def talk_m10_02_x32(text1=_, z1=_):
    """Death status: Dedicated
    text1: Conversation ID
    z1: Hostile: Global event flag
    """
    """State 0,1: Death status: Start"""
    SetEventFlag(z1, 1)
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_02_x2(text1=text1, z18=0)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

