# -*- coding: utf-8 -*-
def talk_m10_32_3070():
    """Durahan"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_32_x9(flag16=103500, flag17=104000, flag18=132020171)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=30709200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(flag15=132020172, text15=30709500, text16=30709500, z35=30709500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=30709600, z37=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: Durahan: Conversation_SubState"""
                call = talk_m10_32_x51()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_32_x5(text19=30709400, text20=30709410, text21=30709420, text22=30709400,
                                          flag19=132020175, flag20=132020176)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(flag21=103500, text23=30709100, z38=0, z39=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(132020176) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(132020175) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_32_x8(text17=30709300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_32_5020():
    """Manscorpion"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_32_x9(flag16=103930, flag17=104430, flag18=132020151)
        # goods:40610000:Ring of Whispers
        if call.Get() == 1 and (EquippedItemCount(40610000) >= 0) != 1:
            """State 13: [Lib] Reunion hostility (no ring) _SubState"""
            # talk:50209998:"...!"
            call = talk_m10_32_x3(text8=50209998, z24=0, z25=20, z26=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(flag15=132020152, text15=50209500, text16=50209500, z35=50209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=50209600, z37=0)
                    Quit()
                # goods:40610000:Ring of Whispers
                elif (EquippedItemCount(40610000) >= 0) != 1:
                    """State 14: [Lib] Hostile state (without ring) _SubState"""
                    Label('L2')
                    # talk:50209998:"...!"
                    call = talk_m10_32_x6(flag15=132020152, text15=50209998, text16=50209998, z35=50209998)
                    if KilledPlayer() != 0:
                        """State 15: [Lib] Killing state (without ring) _SubState"""
                        Label('L3')
                        # talk:50209998:"...!"
                        talk_m10_32_x8(text17=50209998, z36=0)
                        Quit()
                    elif (HpValue() > 1) != 1:
                        """State 16: [Lib] Death state (no ring) _SubState"""
                        Label('L4')
                        # talk:50209998:"...!"
                        talk_m10_32_x7(text18=50209998, z37=0)
                        Quit()
                    # goods:40610000:Ring of Whispers
                    elif (EquippedItemCount(40610000) >= 0) != 0:
                        Goto('L0')
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=50209200, z24=0, z25=20, z26=80)
            if call.Done():
                Goto('L0')
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Manscorpion 会話: Conversation_SubState"""
                call = talk_m10_32_x55()
                if call.Done():
                    Continue('mainloop')
                # goods:40610000:Ring of Whispers
                elif KilledPlayer() != 0 and (EquippedItemCount(40610000) >= 0) != 1:
                    Goto('L3')
                elif KilledPlayer() != 0:
                    break
                # goods:40610000:Ring of Whispers
                elif (HpValue() > 1) != 1 and (EquippedItemCount(40610000) >= 0) != 1:
                    Goto('L4')
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                # goods:40610000:Ring of Whispers
                elif (NumberOfTimesDamaged(1) > 3) != 0 and (EquippedItemCount(40610000) >= 0) != 1:
                    """State 11: [Lib] Hostile waiting (without ring) _SubState"""
                    Label('L5')
                    # talk:50209998:"...!"
                    call = talk_m10_32_x5(text19=50209998, text20=50209998, text21=50209998, text22=50209998,
                                          flag19=132020155, flag20=132020156)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        Goto('L3')
                    elif (HpValue() > 1) != 1:
                        Goto('L4')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 12: [Lib] First hostility (no ring) _SubState"""
                        # talk:50209998:"...!"
                        call = talk_m10_32_x4(flag21=103930, text23=50209998, z38=0, z39=0)
                        if call.Done():
                            Goto('L2')
                        elif KilledPlayer() != 0:
                            Goto('L3')
                        elif (HpValue() > 1) != 1:
                            Goto('L4')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L6')
                    call = talk_m10_32_x5(text19=50209400, text20=50209410, text21=50209420, text22=50209400,
                                          flag19=132020155, flag20=132020156)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(flag21=103930, text23=50209100, z38=0, z39=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                # goods:40610000:Ring of Whispers
                elif ((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(132020156) != 1 and (EquippedItemCount(40610000)
                      >= 0) != 1):
                    Goto('L5')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(132020156) != 1:
                    Goto('L6')
                # goods:40610000:Ring of Whispers
                elif ((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(132020155) != 1 and (EquippedItemCount(40610000)
                      >= 0) != 1):
                    Goto('L5')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(132020155) != 1:
                    Goto('L6')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_32_x8(text17=50209300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_32_7250():
    """Shenzhen Pilgrim (Shadow Forest)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_32_x9(flag16=103622, flag17=104120, flag18=132020101)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=72509200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(flag15=132020102, text15=72509500, text16=72509500, z35=72509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 11: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m10_32_x49(text6=72509600, z15=0, val2=9)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Pilgrim in Shenzhen: Conversation_SubState"""
                call = talk_m10_32_x22(flag1=132020104, flag2=102327, z1=132020107, z2=10323000, flag3=102333,
                                       z3=60, flag4=102317, z4=132020109)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_32_x5(text19=72509400, text20=72509410, text21=72509420, text22=72509400,
                                          flag19=132020105, flag20=132020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 5: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_32_x15(flag14=103620, text9=72509100, z27=0, val3=9, z28=200908,
                                               z29=103622)
                        if call.Done():
                            """State 2: Shenzhen Pilgrim: Magic Square Flag OFF"""
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(132020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(132020105) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_32_x8(text17=72509300, z36=0)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_32_7420():
    """Wandering Warrior (Shadow Forest)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_32_x9(flag16=103652, flag17=104150, flag18=132020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=74209200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(flag15=132020122, text15=74209500, text16=74209500, z35=74209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=74209600, z37=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Wandering Warrior: Conversation_SubState"""
                call = talk_m10_32_x58()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_32_x5(text19=74209400, text20=74209410, text21=74209420, text22=74209400,
                                          flag19=132020125, flag20=132020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(flag21=103650, text23=74209100, z38=0, z39=103652)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(132020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(132020125) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_32_x8(text17=74209300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_32_7760():
    """Upper weapon store (Shadow Forest)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_32_x9(flag16=103861, flag17=104360, flag18=132020191)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=77509200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(flag15=132020192, text15=77509500, text16=77509500, z35=77509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=77509600, z37=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Higher weapon shop: Conversation_SubState"""
                call = talk_m10_32_x59()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_32_x5(text19=77509400, text20=77509410, text21=77509420, text22=77509400,
                                          flag19=132020195, flag20=132020196)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(flag21=103860, text23=77509100, z38=0, z39=103861)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(132020196) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(132020195) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_32_x8(text17=77509300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_32_x0(text10=_, z42=_, z43=0):
    """[Lib] Conversation: General purpose
    text10: Conversation ID
    z42: Conversation flag
    z43: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text10, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z42, 1)
    SetEventFlag(z43, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_32_x1(text1=_, z27=_, z40=-1, z41=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z27: Conversation flag
    z40: Display distance
    z41: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z40)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z27, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_32_x2(text6=_, z15=0):
    """[Lib] Conversation: Event end
    text6: Conversation ID
    z15: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z15, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_32_x3(text8=_, z24=0, z25=20, z26=80):
    """[Lib] Reunion hostility
    text8: Conversation message ID
    z24: Conversation flag ID
    z25: Display distance
    z26: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_32_x36(text8=text8, z24=z24, z25=z25, z26=z26)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_32_x4(flag21=_, text23=_, z38=0, z39=_):
    """[Lib] First hostility
    flag21: Hostile: Global event flag
    text23: Conversation ID
    z38: Conversation flag
    z39: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag21, 1)
    SetEventFlag(z39, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag21) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_32_x1(text1=text23, z27=z38, z40=-1, z41=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_32_x5(text19=_, text20=_, text21=_, text22=_, flag19=_, flag20=_):
    """[Lib] Hostile waiting
    text19: Conversation ID: 1 attacked
    text20: Conversation ID: Attacked 2
    text21: Conversation ID: 3 attacked
    text22: Conversation ID: 4 attacked
    flag19: No use: Area and other flags
    flag20: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag20) != 1, flag20, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag19) != 1, flag19, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_32_x1(text1=text22, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_32_x1(text1=text21, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_32_x1(text1=text20, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_32_x1(text1=text19, z27=0, z40=-1, z41=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_32_x6(flag15=_, text15=_, text16=_, z35=_):
    """[Lib] Hostile state
    flag15: Area and other flags: HP decreased
    text15: Conversation ID: HP drop 1
    text16: Conversation ID: HP drop 2
    z35: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag15) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_32_x10(text15=text15, flag15=flag15)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_32_x10(text15=text16, flag15=flag15)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_32_x10(text15=text16, flag15=flag15)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_32_x7(text18=_, z37=0):
    """[Lib] Death status
    text18: Conversation ID
    z37: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_32_x2(text6=text18, z15=z37)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_32_x8(text17=_, z36=0):
    """[Lib] Murder status
    text17: Conversation ID
    z36: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_32_x2(text6=text17, z15=z36)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_32_x9(flag16=_, flag17=_, flag18=_):
    """[Lib] Event: Branch
    flag16: Hostile flag
    flag17: death flag
    flag18: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag17) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag18) != 0
    elif GetEventFlag(flag16) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_32_x10(text15=_, flag15=_):
    """[Lib] Conversation: HP drop
    text15: Conversation ID
    flag15: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text15, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag15, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_32_x11(action1=_):
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

def talk_m10_32_x12(z32=0, z33=220, z17=_, z34=0):
    """[Lib] Menu start: General purpose
    z32: Camera parameter ID
    z33: Target Damipoly ID
    z17: NPC event parameter ID
    z34: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z34, z32, z33, z17)
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

def talk_m10_32_x13(text13=_, text14=_):
    """[Lib] Menu exit: General purpose
    text13: Conversation ID (at the time of purchase)
    text14: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_32_x1(text1=text13, z27=0, z40=-1, z41=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_32_x1(text1=text14, z27=0, z40=-1, z41=0)
    """State 4: End state"""
    return 0

def talk_m10_32_x14(text12=_):
    """[Lib] Menu cancellation: General purpose
    text12: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_32_x1(text1=text12, z27=0, z40=-1, z41=0)
    """State 4: End state"""
    return 0

def talk_m10_32_x15(flag14=103620, text9=72509100, z27=0, val3=9, z28=200908, z29=103622):
    """[Lib] First hostility _ (pledge cancellation)
    flag14: Hostile: Global event flag
    text9: Conversation ID
    z27: Conversation flag
    val3: Cancellation pledge name
    z28: Pledge cancellation: Global conversation flag
    z29: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag14, 1)
    SetEventFlag(z29, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag14) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_32_x35(val2=val3)
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
    assert talk_m10_32_x1(text1=text9, z27=z27, z40=-1, z41=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_32_x16(text5=_, z12=0, lot6=_, flag9=_, z13=218, z3=60):
    """[Lib] Conversation: Pledge ranking
    text5: Ranking: Conversation ID
    z12: Ranking: Conversation flag
    lot6: Item lottery
    flag9: Ranking transfer: Global event flag
    z13: Previous rank: Global variable
    z3: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_32_x18(action5=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text5, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z12, 1)
    if CanGetItemLot(lot6, 1) != 1 and GetEventFlag(flag9) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z14=1011, lot1=lot6)
    elif GetEventFlag(flag9) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_32_x19(lot1=lot6, flag5=flag9)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z13, GetAreaVariable(z3))
    """State 11: End state"""
    return 0

def talk_m10_32_x17(val1=9, z8=8, lot3=0, flag7=0, action1=1338, action2=1348, z4=132020109):
    """[Lib] Menu item: Make a pledge
    val1: Pledge name
    z8: Event action
    lot3: Item lottery ID
    flag7: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_32_x18(action5=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m10_32_x40(val1=val1, z8=z8, lot3=lot3, flag7=flag7, action1=action1, action2=action2,
                               z4=z4)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_32_x18(action5=_):
    """[Lib] OK dialog
    action5: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action5, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x19(lot1=_, flag5=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    flag5: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(flag5, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x20(flag1=132020104, text10=72505100, text11=72505000):
    """[Lib] Conversation: Greeting: Single
    flag1: Area other flag: Contact flag
    text10: Text ID: Talk to_continuous
    text11: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(flag1) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m10_32_x0(text10=text10, z42=0, z43=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m10_32_x0(text10=text11, z42=0, z43=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(flag1, 1)
    """State 5: End state"""
    return 0

def talk_m10_32_x21(lot5=1725000, z11=102320, text4=72506300):
    """[Lib] Equipment transfer: Mes⇒Item
    lot5: Item lottery ID
    z11: Global event flag
    text4: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_32_x1(text1=text4, z27=0, z40=-1, z41=0)
    # lot:1725000:Dragon Chime
    if call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z14=1011, lot1=lot5)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_32_x19(lot1=lot5, flag5=z11)
    """State 5: End state"""
    return 0

def talk_m10_32_x22(flag1=132020104, flag2=102327, z1=132020107, z2=10323000, flag3=102333, z3=60, flag4=102317,
                    z4=132020109):
    """[Lib] Pilgrim in Shenzhen: Conversation
    flag1: Contact: Area and other flags
    flag2: Magic Square Open: Global Event Flag
    z1: Magic Square Direction: Area and Other Flags
    z2: Magic Square: OBJ instance ID
    flag3: Main encounter: Global event flag
    z3: Current pledge rank: Area variable
    flag4: Main generation stop: Global event flag
    z4: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102321) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: greeting conversation_SubState"""
        assert talk_m10_32_x23(flag1=flag1, z3=z3)
        """State 4: [Lib] Pilgrim in Shenzhen: Menu_SubState"""
        assert talk_m10_32_x24(flag2=flag2, z1=z1, z2=z2, z3=z3, z4=z4)
    elif GetEventFlag(104120) != 0:
        """State 6: [Lib] Conversation: General purpose_SubState"""
        assert talk_m10_32_x0(text10=72509000, z42=0, z43=0)
    else:
        """State 5: [Lib] Pilgrim in Shenzhen: First conversation_SubState"""
        assert talk_m10_32_x27(flag1=flag1, flag2=flag2, z1=z1, z2=z2, flag3=flag3, flag4=flag4, z4=z4)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m10_32_x23(flag1=132020104, z3=60):
    """[Lib] Pilgrim in Shenzhen: greeting conversation
    flag1: Contact: Area and other flags
    z3: Current pledge rank: Area variable
    """
    """State 0,1: Greeting: Start"""
    if (GetPlayerCovenant() == 9) != 0 and GetEventFlag(102319) != 1:
        """State 8: When pledge ring is not acquired: Insurance_SubState"""
        # lot:2006000:Abyss Seal
        assert talk_m10_32_x47(lot1=2006000, flag5=102319)
        """State 3: [Lib] Conversation: Greeting: Single _SubState"""
        Label('L0')
        # talk:72505000:"Young Undead, do you expect me to just keel over?"
        assert talk_m10_32_x20(flag1=flag1, text10=72505100, text11=72505000)
    else:
        """State 4: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m10_32_x42(z22=9, z3=z3, z23=218, flag11=102337, flag12=102338, flag13=102339)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z3) > 1) != 0 and GetEventFlag(102337) != 1:
                """State 5: Conversation: Pledge Ranking 1_SubState"""
                # talk:72506000:"Young Undead, my work is done...", lot:2006011:Resonant Soul
                assert talk_m10_32_x16(text5=72506000, z12=0, lot6=2006011, flag9=102337, z13=218, z3=z3)
            elif (GetAreaVariable(z3) > 2) != 0 and GetEventFlag(102338) != 1:
                """State 6: Conversation: Pledge Ranking 2_SubState"""
                # lot:2006012:Great Resonant Soul
                assert talk_m10_32_x16(text5=72506100, z12=0, lot6=2006012, flag9=102338, z13=218, z3=z3)
            elif (GetAreaVariable(z3) > 3) != 0 and GetEventFlag(102339) != 1:
                """State 7: Conversation: Pledge Ranking 3_SubState"""
                # lot:2006013:Climax
                assert talk_m10_32_x16(text5=72506200, z12=0, lot6=2006013, flag9=102339, z13=218, z3=z3)
            else:
                Goto('L0')
        elif call.Get() == 0:
            Goto('L0')
    """State 9: End state"""
    return 0

def talk_m10_32_x24(flag2=102327, z1=132020107, z2=10323000, z3=60, z4=132020109):
    """[Lib] Pilgrims in Shenzhen: Menu
    flag2: Magic Square Open: Global Event Flag
    z1: Magic Square Open: Area Other Flag
    z2: Magic Square: OBJ instance ID
    z3: Current pledge rank: Area variable
    z4: For trophies: Area and other flags
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 2: Menu: Branch"""
        if GetEventFlag(100979) != 0:
            """State 10: [Lib] Menu start: No passing _SubState"""
            call = talk_m10_32_x12(z32=0, z33=220, z17=72500001, z34=0)
            if call.Get() == 2:
                """State 9: [Lib] Pilgrim in Shenzhen: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_32_x26()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 6:
                """State 8: [Lib] Menu item: _SubState with a pledge"""
                Label('L1')
                # lot:0:No Item, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
                call = talk_m10_32_x17(val1=9, z8=8, lot3=0, flag7=0, action1=1338, action2=1348, z4=z4)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L2')
                assert talk_m10_32_x13(text13=72501200, text14=72501300)
        else:
            """State 4: [Lib] Menu start: General purpose_SubState"""
            call = talk_m10_32_x12(z32=0, z33=220, z17=72500000, z34=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 6:
                Goto('L1')
            elif call.Get() == 8:
                """State 7: [Lib] Pilgrim in Shenzhen: menu passing _SubState"""
                # goods:60151000:Human Effigy
                call = talk_m10_32_x25(goods1=60151000, flag2=flag2, z1=z1, z2=z2)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L2')
        """State 3: Menu: Exit"""
        Label('L3')
        ClearNpcMenuResults()
        """State 11: End state"""
        return 0
    """State 6: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:72501100:"As you wish, yes, as you wish."
    assert talk_m10_32_x14(text12=72501100)
    Goto('L3')

def talk_m10_32_x25(goods1=60151000, flag2=102327, z1=132020107, z2=10323000):
    """[Lib] Pilgrim in Shenzhen: hand over menu
    goods1: Event items
    flag2: Magic Square Open: Global Event Flag
    z1: Magic Square Open: Area Other Flag
    z2: Magic Square: OBJ instance ID
    """
    """State 0,1: Pass: start"""
    if GetEventFlag(flag2) != 0:
        """State 10: Confirmation dialog during magic square release_SubState"""
        # action:1213:"Cannot give now"
        assert talk_m10_32_x18(action5=1213)
    else:
        """State 5: Menu to pass ○○: Conversation to pass_SubState"""
        assert talk_m10_32_x1(text1=72505200, z27=0, z40=-1, z41=0)
        """State 8: Execution selection dialog to pass_SubState"""
        # action:1200:"Give\n%s?", goods:60151000:Human Effigy
        call = talk_m10_32_x37(action4=1200, goods4=60151000)
        if call.Get() == 2:
            pass
        elif call.Get() == 1:
            pass
        # goods:60151000:Human Effigy
        elif call.Get() == 0 and (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 9: No target confirmation dialog_SubState"""
            # action:1206:"You do not have\n%s"
            assert talk_m10_32_x38(action3=1206, goods1=goods1)
        elif call.Get() == 0:
            """State 11: [Lib] Event action: Pass _SubState"""
            # goods:60151000:Human Effigy
            assert talk_m10_32_x48(z16=15, goods2=60151000)
            """State 3: 3rd encounter: Magic square: Open"""
            SetEventFlag(z1, 1)
            """State 4,6: Menu to pass ○○: Conversation to pass: YES_SubState"""
            assert talk_m10_32_x1(text1=72505300, z27=0, z40=-1, z41=0)
            Goto('L0')
        """State 7: Menu to pass ○○: Conversation to pass: NO_SubState"""
        assert talk_m10_32_x1(text1=72505400, z27=0, z40=-1, z41=0)
    """State 2: Pass: Exit"""
    Label('L0')
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_32_x26():
    """[Lib] Pilgrims in Shenzhen: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(100979) != 0 and GetEventFlag(102320) != 1 and GetEventFlag(104120) != 1:
        """State 4: Equipment transfer (Condition: Defeated Agaduran) _SubState"""
        # lot:1725000:Dragon Chime
        assert talk_m10_32_x21(lot5=1725000, z11=102320, text4=72506300)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        assert talk_m10_32_x1(text1=72505500, z27=0, z40=-1, z41=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_32_x27(flag1=132020104, flag2=102327, z1=132020107, z2=10323000, flag3=102333, flag4=102317,
                    z4=132020109):
    """[Lib] Pilgrim in Shenzhen: first conversation
    flag1: Contact: Area and other flags
    flag2: Magic Square Open: Global Event Flag
    z1: Magic Square Open: Area Other Flag
    z2: Magic Square: OBJ instance ID
    flag3: Main encounter: Global event flag
    flag4: Main generation stop: Global event flag
    z4: For trophies: Area and other flags
    """
    """State 0,1: First conversation: start"""
    if GetEventFlag(202752) != 0 and GetEventFlag(flag3) != 0:
        """State 4: [Lib] Pilgrim in Shenzhen: Encounter 3rd conversation _SubState"""
        Label('L0')
        assert talk_m10_32_x30(flag2=flag2, z1=z1, z2=z2, flag3=flag3, z4=z4)
    elif GetEventFlag(202751) != 0 and GetEventFlag(flag3) != 1:
        Goto('L0')
    elif GetEventFlag(202751) != 0 and GetEventFlag(flag3) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: second encounter _SubState"""
        Label('L1')
        assert talk_m10_32_x29(flag4=flag4, flag3=flag3)
    elif GetEventFlag(202750) != 0 and GetEventFlag(flag3) != 1:
        Goto('L1')
    else:
        """State 2: [Lib] Pilgrims in Shenzhen: first encounter conversation_SubState"""
        assert talk_m10_32_x28(flag4=flag4, flag3=flag3)
    """State 5: End state"""
    return 0

def talk_m10_32_x28(flag4=102317, flag3=102333):
    """[Lib] Pilgrim in Shenzhen: first encounter
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    """
    """State 0,1: First encounter conversation: Start"""
    if GetEventFlag(202750) != 0:
        """State 4: Talk: 1st encounter: Loop_SubState"""
        # talk:72500100:"The Dark is still nascent within you.\nMay the Dark shine your way..."
        assert talk_m10_32_x0(text10=72500100, z42=0, z43=0)
    else:
        """State 3: Talk: 1st encounter_SubState"""
        # talk:72500000:"Ahh, look how far this Undead has wandered."
        call = talk_m10_32_x0(text10=72500000, z42=202750, z43=0)
        if call.Done() and GetEventFlag(flag4) != 1:
            """State 2: First encounter: stop generation"""
            Label('L0')
            SetEventFlag(flag3, 1)
            SetEventFlag(flag4, 1)
            assert GetEventFlag(flag4) != 0 and GetEventFlag(flag3) != 0
        elif call.Done() and GetEventFlag(flag3) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 5: End state"""
    return 0

def talk_m10_32_x29(flag4=102317, flag3=102333):
    """[Lib] Pilgrim in Shenzhen: second encounter
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    """
    """State 0,1: Encounter 2nd conversation: Start"""
    if GetEventFlag(202751) != 0:
        """State 4: Talk: Second encounter: Loop_SubState"""
        # talk:72500300:"May we meet again, somewhere, some time..."
        assert talk_m10_32_x0(text10=72500300, z42=0, z43=0)
    else:
        """State 3: Speak: Second encounter_SubState"""
        # talk:72500200:"Young Undead, don't let this curse weigh upon you."
        call = talk_m10_32_x0(text10=72500200, z42=202751, z43=0)
        if call.Done() and GetEventFlag(flag4) != 1:
            """State 2: Second encounter: Stop generation"""
            Label('L0')
            SetEventFlag(flag3, 1)
            SetEventFlag(flag4, 1)
            assert GetEventFlag(flag4) != 0 and GetEventFlag(flag3) != 0
        elif call.Done() and GetEventFlag(flag3) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 5: End state"""
    return 0

def talk_m10_32_x30(flag2=102327, z1=132020107, z2=10323000, flag3=102333, z4=132020109):
    """[Lib] Pilgrim in Shenzhen: 3rd encounter
    flag2: Magic Square Open: Global Event Flag
    z1: Magic Square Open: Area Other Flag
    z2: Magic Square: OBJ instance ID
    flag3: Main encounter: Global event flag
    z4: For trophies: Area and other flags
    """
    """State 0,1: Encounter 3rd conversation: Start"""
    if GetEventFlag(202752) != 0:
        """State 6: Speak: 3rd encounter: YES / NO dialog: NO: Loop_SubState"""
        # talk:72500900:"We meet again, young Undead."
        assert talk_m10_32_x0(text10=72500900, z42=0, z43=0)
    else:
        """State 5: Talk: 3rd encounter_SubState"""
        # talk:72500400:"We meet again, young Undead."
        assert talk_m10_32_x0(text10=72500400, z42=202752, z43=0)
    """State 10: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:2006000:Abyss Seal, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
    call = talk_m10_32_x40(val1=9, z8=8, lot3=2006000, flag7=102319, action1=1338, action2=1348, z4=z4)
    if call.Get() == 1:
        """State 2: 3rd encounter: After signing the pledge: Set flag"""
        SetEventFlag(102321, 1)
        assert GetEventFlag(102321) != 0
        """State 3: 3rd encounter: Magic square: Open"""
        SetEventFlag(z1, 1)
        """State 4,9: Speak: 3rd encounter: YES / NO dialog: YES_SubState"""
        # talk:72500500:"There you are, you are now a Pilgrim of Dark."
        assert talk_m10_32_x1(text1=72500500, z27=0, z40=-1, z41=0)
    elif call.Get() == 0 and GetEventFlag(202753) != 0:
        """State 8: Speak: 3rd encounter: YES / NO dialog: NO: Loop: YES / NO dialog: NO_SubState"""
        # talk:72501000:"Then choose your own path."
        assert talk_m10_32_x1(text1=72501000, z27=0, z40=-1, z41=0)
    elif call.Get() == 0:
        """State 7: Speak: 3rd encounter: YES / NO dialog: NO_SubState"""
        # talk:72500800:"Hmm... Perhaps I was wrong."
        assert talk_m10_32_x1(text1=72500800, z27=202753, z40=-1, z41=0)
    """State 11: End state"""
    return 0

def talk_m10_32_x31(lot2=_, flag6=_, z5=0, z7=_, z30=0, z31=0):
    """[Lib] Item acquisition dialog: Conversation
    lot2: Item lottery ID
    flag6: Item transfer: Global event flag
    z5: Conversation: Global conversation flag
    z7: Trophy acquisition: Area and other flags
    z30: Emigration permission: Global event flag
    z31: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z31, 1)
    SetEventFlag(z30, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(z5, 1)
    SetEventFlag(flag6, 1)
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x32(lot4=1307000, flag8=102001, text2=30706000, text3=30706020, z9=0, z10=132020177):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    flag8: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z9: Conversation: Global conversation flag
    z10: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_32_x1(text1=text2, z27=0, z40=-1, z41=0)
    if call.Done() and GetEventFlag(flag8) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z9, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_32_x1(text1=text3, z27=0, z40=-1, z41=0)
    # lot:1307000:Vengarl's Helm
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z14=1011, lot1=lot4)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_32_x31(lot2=lot4, flag6=flag8, z5=z9, z7=z10, z30=0, z31=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_32_x33():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m10_32_x34():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x35(val2=9):
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

def talk_m10_32_x36(text8=_, z24=0, z25=20, z26=80):
    """[Lib] Conversation: Hostile display only
    text8: Conversation ID
    z24: Conversation flag
    z25: Display distance
    z26: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), z25)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z24, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_32_x37(action4=1200, goods4=60151000):
    """[Lib] Selection dialog: Item display
    action4: Dialog: Text ID
    goods4: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    # action:1200:"Give\n%s?", goods:60151000:Human Effigy
    DisplayOwnYesNoMenu(action4, 0, -1, 2, goods4, 0)
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

def talk_m10_32_x38(action3=1206, goods1=60151000):
    """[Lib] OK dialog: Item display
    action3: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: OK dialog: Display"""
    # action:1206:"You do not have\n%s", goods:60151000:Human Effigy
    DisplayOwnOkMenu(action3, 0, 0, -1, 2, goods1, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x39(goods3=_, flag10=_):
    """[Lib] Menu item: Gesture
    goods3: Gesture: Item ID
    flag10: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_32_x46(goods3=goods3, flag10=flag10)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_32_x40(val1=9, z8=8, lot3=_, flag7=_, action1=1338, action2=1348, z4=132020109):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z8: Event action
    lot3: Item lottery ID
    flag7: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z4, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_32_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_32_x18(action5=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_32_x41(z8=z8, val1=val1, lot3=lot3, flag7=flag7) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_32_x18(action5=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_32_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_32_x35(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_32_x41(z8=8, val1=9, lot3=_, flag7=_):
    """[Lib] Event action: Pledge
    z8: Event action
    val1: Pledge type
    lot3: Item lottery ID
    flag7: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z8)
    assert PlayerIsInEventAction(z8) != 0
    """State 3: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z8) != 1 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(flag7) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(flag7) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_32_x50(z14=1011, lot1=lot3)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z8) != 1 and GetEventFlag(flag7) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z8) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(flag7, 1)
        AwardItem(lot3, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z8) != 1
    """State 8: End state"""
    return 0

def talk_m10_32_x42(z22=9, z3=60, z23=218, flag11=102337, flag12=102338, flag13=102339):
    """[Lib] Pledge: Rank up: Conversation: 1
    z22: Pledge: Pledge type
    z3: Current rank: Area variable
    z23: Previous rank: Global variable
    flag11: Ranking 1: Item transfer: Global event flag
    flag12: Ranking 2: Item transfer: Global event flag
    flag13: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z3, GetPlayerCovenantLevel(z22))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z23) > GetAreaVariable(z3)) != 1 and (GetGlobalVariable(z23) == GetAreaVariable(z3))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z23) > GetAreaVariable(z3)) != 0 and (GetGlobalVariable(z23) == GetAreaVariable(z3))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z23, GetAreaVariable(z3))
    elif GetEventFlag(flag11) != 1 and (GetGlobalVariable(z23) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(flag12) != 1 and (GetGlobalVariable(z23) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(flag13) != 1 and (GetGlobalVariable(z23) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_32_x43(goods3=_, flag10=_, z17=_, z18=_):
    """[Lib] NPC menu: Gesture alone
    goods3: Item: Event item
    flag10: Item transfer: Global event flag
    z17: NPC menu: With gesture
    z18: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(flag10) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            if (ItemCount(goods3, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_32_x12(z32=0, z33=220, z17=z17, z34=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m10_32_x39(goods3=goods3, flag10=flag10)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        pass
                elif call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    """State 6: [Lib] Menu exit: No Mes_SubState"""
                    Label('L0')
                    assert talk_m10_32_x33()
                    Goto('L2')
            """State 7: [Lib] Menu canceled: No Mes_SubState"""
            Label('L1')
            assert talk_m10_32_x34()
            Goto('L2')
        """State 5: [Lib] Menu start: No gesture _SubState"""
        call = talk_m10_32_x12(z32=0, z33=220, z17=z18, z34=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_32_x44(text7=_, z19=_, z20=10329010, z21=-1):
    """[Lib] Conversation: For unique key guide
    text7: Conversation ID
    z19: Conversation flag
    z20: Key guide parameters
    z21: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z20)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), z21)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z19, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_32_x45(lot2=_, flag6=_, text1=_, z5=0, z6=10329010, z7=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: UnicKey
    lot2: Item lottery ID
    flag6: Get: Global event flag
    text1: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Key guide parameters
    z7: Trophy: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, z6)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m10_32_x1(text1=text1, z27=0, z40=-1, z41=0)
    if call.Done() and GetEventFlag(flag6) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z5, 1)
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z14=1011, lot1=lot2)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_32_x31(lot2=lot2, flag6=flag6, z5=z5, z7=z7, z30=0, z31=0)
    """State 9: End state"""
    return 0

def talk_m10_32_x46(goods3=_, flag10=_):
    """[Lib] Get gesture dialog
    goods3: Item ID
    flag10: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods3, 0, -1)
    SetEventFlag(flag10, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x47(lot1=2006000, flag5=102319):
    """[Lib] Conversation: Item transfer: Item: Key
    lot1: Item lottery
    flag5: Item transfer: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # lot:2006000:Abyss Seal
    if CanGetItemLot(lot1, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z14=1011, lot1=lot1)
    elif GetEventFlag(flag5) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_32_x19(lot1=lot1, flag5=flag5)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m10_32_x48(z16=15, goods2=60151000):
    """[Lib] Event action: Pass
    z16: Event action
    goods2: Item to be handed: Event item
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z16)
    assert PlayerIsInEventAction(z16) != 0
    """State 2: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z16) != 1
    """State 4: Event action: Pass: Item transfer"""
    # goods:60151000:Human Effigy
    ConsumeItem(goods2, 1)
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z16) != 1
    """State 5: End state"""
    return 0

def talk_m10_32_x49(text6=72509600, z15=0, val2=9):
    """[Lib] Death status_ (pledge cancellation)
    text6: Conversation ID
    z15: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_32_x35(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_32_x2(text6=text6, z15=z15)
    Quit()
    """Unused"""
    """State 5: End state"""
    return 0

def talk_m10_32_x50(z14=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z14: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x51():
    """Durahan: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(201004) != 0:
        """State 5: Durahan: Greetings_SubState"""
        assert talk_m10_32_x60()
        """State 4: Durahan: NPC menu_SubState"""
        Label('L0')
        assert talk_m10_32_x53()
    else:
        """State 3: Durahan: First conversation_SubState"""
        call = talk_m10_32_x52()
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_32_x52():
    """Durahan: first conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(201003) != 0:
        """State 6: Talk: Part 5_SubState"""
        # talk:30700400:"I learn new things every day.\nThings never learned in battle."
        assert talk_m10_32_x0(text10=30700400, z42=201004, z43=0)
        """State 8: Menu: Exit state"""
        return 1
    elif GetEventFlag(201002) != 0:
        """State 5: Talk: 4_SubState"""
        # talk:30700300:"I know not what brings you on this journey,\nnor will I deign to ask."
        assert talk_m10_32_x0(text10=30700300, z42=201003, z43=0)
    elif GetEventFlag(201001) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:30700200:"Long ago, I was hired to defend the kingdom."
        assert talk_m10_32_x0(text10=30700200, z42=201002, z43=0)
    elif GetEventFlag(201000) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:30700100:"What business have you here, traveller?"
        assert talk_m10_32_x0(text10=30700100, z42=201001, z43=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:30700000:"Leave me be."
        assert talk_m10_32_x0(text10=30700000, z42=201000, z43=0)
    """State 7: Normal: End state"""
    return 0

def talk_m10_32_x53():
    """Durahan: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuSelection()
    while True:
        """State 3: Menu: Branch"""
        # goods:63017000:"Decapitate" Gesture
        if (ItemCount(63017000, 1, 1, 0) > 1) != 0:
            """State 8: [Lib] Menu start: No gesture _SubState"""
            call = talk_m10_32_x12(z32=0, z33=220, z17=30700001, z34=0)
            if call.Get() == 2:
                """State 7: Durahan: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_32_x54()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:30700500:"Farewell. May we meet again, one day soon.", talk:30700600:"Farewell. I will retire to my silence."
                assert talk_m10_32_x13(text13=30700500, text14=30700600)
        else:
            """State 4: [Lib] Menu start: With gesture_SubState"""
            call = talk_m10_32_x12(z32=0, z33=220, z17=30700000, z34=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 9: [Lib] Menu item: Gesture_SubState"""
                call = talk_m10_32_x39(goods3=63017000, flag10=0)
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
        ClearNpcMenuSelection()
        """State 10: End state"""
        return 0
    """State 6: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:30700700:"Safe travels, then..."
    assert talk_m10_32_x14(text12=30700700)
    Goto('L2')

def talk_m10_32_x54():
    """Durahan: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102010) != 0 and GetEventFlag(201020) != 1:
        """State 4: Durahan Defeated_SubState"""
        # talk:30705000:"You fiend!"
        assert talk_m10_32_x1(text1=30705000, z27=201020, z40=-1, z41=0)
    elif GetEventFlag(201012) != 0 and GetEventFlag(102001) != 1 and GetEventFlag(104000) != 1:
        """State 8: Equipment transfer (Condition: Durahan destroyed) _SubState"""
        # lot:1307000:Vengarl's Helm, talk:30706000:"I like quiet. It's all I ever wished for."
        assert talk_m10_32_x32(lot4=1307000, flag8=102001, text2=30706000, text3=30706020, z9=0, z10=132020177)
    elif GetEventFlag(201012) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(201010, 0)
        SetEventFlag(201011, 0)
        SetEventFlag(201012, 0)
        """State 5: Menu conversation: Part 1_SubState"""
        Label('L0')
        assert talk_m10_32_x1(text1=30705100, z27=201010, z40=-1, z41=0)
    elif GetEventFlag(201011) != 0:
        """State 7: Menu conversation: 3_SubState"""
        assert talk_m10_32_x1(text1=30705300, z27=201012, z40=-1, z41=0)
    elif GetEventFlag(201010) != 0:
        """State 6: Menu conversation: 2_SubState"""
        assert talk_m10_32_x1(text1=30705200, z27=201011, z40=-1, z41=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_32_x55():
    """Manscorpion 会話: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    # goods:40610000:Ring of Whispers
    if (EquippedItemCount(40610000) >= 0) != 1:
        """State 5: Manscorpion ♂: Ring not installed_SubState"""
        call = talk_m10_32_x61()
        if call.Done():
            pass
        # goods:40610000:Ring of Whispers
        elif ConversationEnded() != 0 and (EquippedItemCount(40610000) >= 0) != 0:
            pass
    elif GetEventFlag(100957) != 0:
        """State 4: Manscorpion ♂: Substate _SubState"""
        call = talk_m10_32_x57()
        if call.Done():
            pass
        # goods:40610000:Ring of Whispers
        elif ConversationEnded() != 0 and (EquippedItemCount(40610000) >= 0) != 1:
            pass
    else:
        """State 3: Manscorpion ♂: _SubState before the defeat"""
        call = talk_m10_32_x56()
        if call.Done():
            pass
        elif GetEventFlag(100957) != 0:
            pass
        # goods:40610000:Ring of Whispers
        elif ConversationEnded() != 0 and (EquippedItemCount(40610000) >= 0) != 1:
            pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_32_x56():
    """Manscorpion ♂: Before defeat"""
    """State 0,1: Before defeat: Start"""
    if GetEventFlag(206106) != 0:
        """State 10: Before the defeat: Talk to: Part 8_SubState"""
        # talk:50200700:"Since I speak the tongue of men,\ndoes this mean I was once human?"
        assert talk_m10_32_x44(text7=50200700, z19=0, z20=10329010, z21=-1)
    elif GetEventFlag(206105) != 0:
        """State 9: Before the defeat: Talk to: 7_SubState"""
        # talk:50200600:"We seem to be at a standstill.\nThe wounds we exchange are never lethal."
        assert talk_m10_32_x44(text7=50200600, z19=206106, z20=10329010, z21=-1)
        """State 2: Before defeat: White phantom can appear"""
        SetEventFlag(102980, 1)
        assert GetEventFlag(102980) != 0
    elif GetEventFlag(206104) != 0:
        """State 8: Before the defeat: Talk to: 6_SubState"""
        # talk:50200500:"I wish to ask a favour of you.\nI want you to kill my betrothed."
        assert talk_m10_32_x44(text7=50200500, z19=206105, z20=10329010, z21=-1)
    elif GetEventFlag(206103) != 0:
        """State 7: Before the defeat: Talk to: 5_SubState"""
        # talk:50200400:"Nobody knows when we were born."
        assert talk_m10_32_x44(text7=50200400, z19=206104, z20=10329010, z21=-1)
    elif GetEventFlag(206102) != 0:
        """State 6: Before the defeat: Talk to: 4_SubState"""
        # talk:50200300:"Our master was a tragically lonely soul."
        assert talk_m10_32_x44(text7=50200300, z19=206103, z20=10329010, z21=-1)
    elif GetEventFlag(206101) != 0:
        """State 5: Before the defeat: Talk: Part 3_SubState"""
        # talk:50200200:"We once had a master.\nHe created us long, long ago."
        assert talk_m10_32_x44(text7=50200200, z19=206102, z20=10329010, z21=-1)
    elif GetEventFlag(206100) != 0:
        """State 4: Before the defeat: Talk to: 2_SubState"""
        # talk:50200100:"Are you not afraid of me?"
        assert talk_m10_32_x44(text7=50200100, z19=206101, z20=10329010, z21=-1)
    else:
        """State 3: Before the defeat: Talk: Part 1_SubState"""
        # talk:50200000:"Human, are we?"
        assert talk_m10_32_x44(text7=50200000, z19=206100, z20=10329010, z21=-1)
    """State 11: End state"""
    return 0

def talk_m10_32_x57():
    """Manscorpion 後: After defeat"""
    """State 0,1: After defeat: Start"""
    if (GetEventFlag(102981) != 0 and GetEventFlag(100951) != 0 and GetEventFlag(104430) != 1 and GetEventFlag(102982)
        != 1):
        """State 7: Equipment transfer: Defeat the queen of the eagle_SubState"""
        # lot:1502010:Black Scorpion Stinger, talk:50206000:"Young human..."
        assert talk_m10_32_x45(lot2=1502010, flag6=102982, text1=50206000, z5=0, z6=10329010, z7=0)
    elif GetEventFlag(102981) != 0:
        """State 5: After defeat: Talk to: 3_SubState"""
        # talk:50201200:"I have no gods to pray to."
        call = talk_m10_32_x44(text7=50201200, z19=206111, z20=10329010, z21=-1)
        if call.Done() and GetEventFlag(102983) != 1:
            """State 2: [Lib] NPC menu: Gesture alone_SubState"""
            Label('L0')
            # goods:63010000:"Warmup" Gesture
            assert talk_m10_32_x43(goods3=63010000, flag10=102983, z17=50200000, z18=50200001)
        elif call.Done():
            pass
    else:
        """State 3: After defeat: Speak: Part 1_SubState"""
        # lot:1502000:Fragrant Branch of Yore, talk:50201000:"You've defeated my better half."
        assert talk_m10_32_x45(lot2=1502000, flag6=102981, text1=50201000, z5=0, z6=10329010, z7=0)
    """State 8: End state"""
    Label('L1')
    return 0
    """Unused"""
    """State 4: After defeat: Speak: Part 2_SubState"""
    # talk:50201100:"Long ago, there was a being with powers similar to ours."
    assert talk_m10_32_x44(text7=50201100, z19=206110, z20=10329010, z21=-1)
    Goto('L1')
    """State 6: After defeat: Speak: Part 2 (for loop) _SubState"""
    # talk:50201100:"Long ago, there was a being with powers similar to ours."
    call = talk_m10_32_x44(text7=50201100, z19=0, z20=10329010, z21=-1)
    if call.Done() and GetEventFlag(102983) != 1:
        Goto('L0')
    elif call.Done():
        Goto('L1')

def talk_m10_32_x58():
    """Wandering Warrior: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203212) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:74200700:"For the good of the world, and for my own honour."
        call = talk_m10_32_x0(text10=74200700, z42=0, z43=0)
        if call.Done() and GetEventFlag(102406) != 1:
            """State 3: Conversation: Set movement permission flag"""
            SetEventFlag(102406, 1)
            assert GetEventFlag(102406) != 0
        elif call.Done():
            pass
        """State 7: [Lib] NPC menu: Gesture alone_SubState"""
        # goods:63018000:"Fist pump" Gesture
        assert talk_m10_32_x43(goods3=63018000, flag10=102403, z17=74200000, z18=74200001)
    elif GetEventFlag(203211) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:74200600:"That bastard with the ring lives in Brightstone Cove down the way."
        assert talk_m10_32_x0(text10=74200600, z42=203212, z43=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:74200400:"Heh heh... Just wait, you dirty rat..."
        assert talk_m10_32_x0(text10=74200400, z42=203210, z43=0)
        """State 8: Talk to: 2_SubState"""
        # talk:74200500:"Hm? Oh...oh!\nI-I remember you?!"
        assert talk_m10_32_x1(text1=74200500, z27=203211, z40=-1, z41=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_32_x59():
    """Higher weapon shop: conversation"""
    """State 0,1: Conversation: Start"""
    if GetEventFlag(205400) != 0:
        """State 5: 2_SubState to talk to"""
        # talk:77500200:"Thank you, kind traveller."
        assert talk_m10_32_x0(text10=77500200, z42=0, z43=0)
    else:
        """State 4: 1_SubState to talk to"""
        # talk:77500100:"Thank you for helping me.\nHow awkward...that I fell for such a trap."
        call = talk_m10_32_x0(text10=77500100, z42=205400, z43=0)
        if call.Done() and GetEventFlag(102841) != 1:
            """State 3: Conversation: Set migration permission flag"""
            SetEventFlag(102841, 1)
            assert GetEventFlag(102841) != 0
        elif call.Done():
            pass
    """State 2,6: End state"""
    return 0

def talk_m10_32_x60():
    """Durahan: Greetings"""
    """State 0,1,2: Greeting_SubState"""
    # talk:30700800:"Back again?\nWell, this is a pleasant surprise."
    assert talk_m10_32_x0(text10=30700800, z42=0, z43=0)
    """State 3: End state"""
    return 0

def talk_m10_32_x61():
    """Manscorpion ♂: ring not installed"""
    """State 0,1,2: When not wearing a ring_SubState"""
    # talk:50209999:"...?"
    assert talk_m10_32_x44(text7=50209999, z19=0, z20=10329010, z21=-1)
    """State 3: End state"""
    return 0

