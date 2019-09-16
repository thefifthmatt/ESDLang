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
        call = talk_m10_32_x9(z51=103500, z52=104000, z53=132020171)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=30709200, z37=0, z38=20, z39=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(z49=132020172, text15=30709500, text16=30709500, z50=30709500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=30709600, z55=0)
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
                                          z56=132020175, z57=132020176)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(z58=103500, text23=30709100, z59=0, z60=0)
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
        talk_m10_32_x8(text17=30709300, z54=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

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
        call = talk_m10_32_x9(z51=103930, z52=104430, z53=132020151)
        # goods:40610000:Ring of Whispers
        if call.Get() == 1 and (EquippedItemCount(40610000) >= 0) != 1:
            """State 13: [Lib] Reunion hostility (no ring) _SubState"""
            # talk:50209998:"...!"
            call = talk_m10_32_x3(text8=50209998, z37=0, z38=20, z39=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(z49=132020152, text15=50209500, text16=50209500, z50=50209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=50209600, z55=0)
                    Quit()
                # goods:40610000:Ring of Whispers
                elif (EquippedItemCount(40610000) >= 0) != 1:
                    """State 14: [Lib] Hostile state (without ring) _SubState"""
                    Label('L2')
                    # talk:50209998:"...!"
                    call = talk_m10_32_x6(z49=132020152, text15=50209998, text16=50209998, z50=50209998)
                    if KilledPlayer() != 0:
                        """State 15: [Lib] Killing state (without ring) _SubState"""
                        Label('L3')
                        # talk:50209998:"...!"
                        talk_m10_32_x8(text17=50209998, z54=0)
                        Quit()
                    elif (HpValue() > 1) != 1:
                        """State 16: [Lib] Death state (no ring) _SubState"""
                        Label('L4')
                        # talk:50209998:"...!"
                        talk_m10_32_x7(text18=50209998, z55=0)
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
            call = talk_m10_32_x3(text8=50209200, z37=0, z38=20, z39=80)
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
                                          z56=132020155, z57=132020156)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        Goto('L3')
                    elif (HpValue() > 1) != 1:
                        Goto('L4')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 12: [Lib] First hostility (no ring) _SubState"""
                        # talk:50209998:"...!"
                        call = talk_m10_32_x4(z58=103930, text23=50209998, z59=0, z60=0)
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
                                          z56=132020155, z57=132020156)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(z58=103930, text23=50209100, z59=0, z60=0)
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
        talk_m10_32_x8(text17=50209300, z54=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

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
        call = talk_m10_32_x9(z51=103622, z52=104120, z53=132020101)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=72509200, z37=0, z38=20, z39=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(z49=132020102, text15=72509500, text16=72509500, z50=72509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 11: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m10_32_x49(text6=72509600, z24=0, val2=9)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Pilgrim in Shenzhen: Conversation_SubState"""
                call = talk_m10_32_x22(z1=132020104, z2=102327, z3=132020107, z4=10323000, z5=102333,
                                       z6=60, z7=102317, z8=132020109)
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
                                          z56=132020105, z57=132020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 5: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_32_x15(z40=103620, text9=72509100, z41=0, val3=9, z42=200908,
                                               z43=103622)
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
        talk_m10_32_x8(text17=72509300, z54=0)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()

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
        call = talk_m10_32_x9(z51=103652, z52=104150, z53=132020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=74209200, z37=0, z38=20, z39=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(z49=132020122, text15=74209500, text16=74209500, z50=74209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=74209600, z55=0)
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
                                          z56=132020125, z57=132020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(z58=103650, text23=74209100, z59=0, z60=103652)
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
        talk_m10_32_x8(text17=74209300, z54=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

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
        call = talk_m10_32_x9(z51=103861, z52=104360, z53=132020191)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_32_x3(text8=77509200, z37=0, z38=20, z39=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_32_x6(z49=132020192, text15=77509500, text16=77509500, z50=77509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_32_x7(text18=77509600, z55=0)
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
                                          z56=132020195, z57=132020196)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_32_x4(z58=103860, text23=77509100, z59=0, z60=103861)
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
        talk_m10_32_x8(text17=77509300, z54=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_32_x0(text10=_, z63=_, z64=0):
    """[Lib] Conversation: General purpose
    text10: Conversation ID
    z63: Conversation flag
    z64: Global event flag
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
    SetEventFlag(z63, 1)
    SetEventFlag(z64, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_32_x1(text1=_, z41=_, z61=-1, z62=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z41: Conversation flag
    z61: Display distance
    z62: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z61)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z41, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_32_x2(text6=_, z24=0):
    """[Lib] Conversation: Event end
    text6: Conversation ID
    z24: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z24, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_32_x3(text8=_, z37=0, z38=20, z39=80):
    """[Lib] Reunion hostility
    text8: Conversation message ID
    z37: Conversation flag ID
    z38: Display distance
    z39: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_32_x36(text8=text8, z37=z37, z38=z38, z39=z39)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_32_x4(z58=_, text23=_, z59=0, z60=_):
    """[Lib] First hostility
    z58: Hostile: Global event flag
    text23: Conversation ID
    z59: Conversation flag
    z60: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z58, 1)
    SetEventFlag(z60, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z58) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_32_x1(text1=text23, z41=z59, z61=-1, z62=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_32_x5(text19=_, text20=_, text21=_, text22=_, z56=_, z57=_):
    """[Lib] Hostile waiting
    text19: Conversation ID: 1 attacked
    text20: Conversation ID: Attacked 2
    text21: Conversation ID: 3 attacked
    text22: Conversation ID: 4 attacked
    z56: No use: Area and other flags
    z57: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z57) != 1, z57, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z56) != 1, z56, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_32_x1(text1=text22, z41=0, z61=-1, z62=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_32_x1(text1=text21, z41=0, z61=-1, z62=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_32_x1(text1=text20, z41=0, z61=-1, z62=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_32_x1(text1=text19, z41=0, z61=-1, z62=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_32_x6(z49=_, text15=_, text16=_, z50=_):
    """[Lib] Hostile state
    z49: Area and other flags: HP decreased
    text15: Conversation ID: HP drop 1
    text16: Conversation ID: HP drop 2
    z50: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z49) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_32_x10(text15=text15, z49=z49)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_32_x10(text15=text16, z49=z49)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_32_x10(text15=text16, z49=z49)

def talk_m10_32_x7(text18=_, z55=0):
    """[Lib] Death status
    text18: Conversation ID
    z55: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_32_x2(text6=text18, z24=z55)

def talk_m10_32_x8(text17=_, z54=0):
    """[Lib] Murder status
    text17: Conversation ID
    z54: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_32_x2(text6=text17, z24=z54)

def talk_m10_32_x9(z51=_, z52=_, z53=_):
    """[Lib] Event: Branch
    z51: Hostile flag
    z52: death flag
    z53: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z52) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z53) != 0
    elif GetEventFlag(z51) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_32_x10(text15=_, z49=_):
    """[Lib] Conversation: HP drop
    text15: Conversation ID
    z49: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text15, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z49, 1)
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

def talk_m10_32_x12(z46=0, z47=220, z27=_, z48=0):
    """[Lib] Menu start: General purpose
    z46: Camera parameter ID
    z47: Target Damipoly ID
    z27: NPC event parameter ID
    z48: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z48, z46, z47, z27)
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

def talk_m10_32_x13(text13=_, text14=_):
    """[Lib] Menu exit: General purpose
    text13: Conversation ID (at the time of purchase)
    text14: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_32_x1(text1=text13, z41=0, z61=-1, z62=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_32_x1(text1=text14, z41=0, z61=-1, z62=0)
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
    assert talk_m10_32_x1(text1=text12, z41=0, z61=-1, z62=0)
    """State 4: End state"""
    return 0

def talk_m10_32_x15(z40=103620, text9=72509100, z41=0, val3=9, z42=200908, z43=103622):
    """[Lib] First hostility _ (pledge cancellation)
    z40: Hostile: Global event flag
    text9: Conversation ID
    z41: Conversation flag
    val3: Cancellation pledge name
    z42: Pledge cancellation: Global conversation flag
    z43: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z40, 1)
    SetEventFlag(z43, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z40) != 0 and GetEventFlag(103999) != 0
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
    assert talk_m10_32_x1(text1=text9, z41=z41, z61=-1, z62=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_32_x16(text5=_, z20=0, lot6=_, z21=_, z22=218, z6=60):
    """[Lib] Conversation: Pledge ranking
    text5: Ranking: Conversation ID
    z20: Ranking: Conversation flag
    lot6: Item lottery
    z21: Ranking transfer: Global event flag
    z22: Previous rank: Global variable
    z6: Current rank: Area variable
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
    SetEventFlag(z20, 1)
    if CanGetItemLot(lot6, 1) != 1 and GetEventFlag(z21) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z23=1011, lot1=lot6)
    elif GetEventFlag(z21) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_32_x19(lot1=lot6, z9=z21)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z22, GetAreaVariable(z6))
    """State 11: End state"""
    return 0

def talk_m10_32_x17(val1=9, z14=8, lot3=0, z15=0, action1=1338, action2=1348, z8=132020109):
    """[Lib] Menu item: Make a pledge
    val1: Pledge name
    z14: Event action
    lot3: Item lottery ID
    z15: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_32_x18(action5=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m10_32_x40(val1=val1, z14=z14, lot3=lot3, z15=z15, action1=action1, action2=action2,
                               z8=z8)
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

def talk_m10_32_x19(lot1=_, z9=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    z9: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z9, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x20(z1=132020104, text10=72505100, text11=72505000):
    """[Lib] Conversation: Greeting: Single
    z1: Area other flag: Contact flag
    text10: Text ID: Talk to_continuous
    text11: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(z1) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m10_32_x0(text10=text10, z63=0, z64=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m10_32_x0(text10=text11, z63=0, z64=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(z1, 1)
    """State 5: End state"""
    return 0

def talk_m10_32_x21(lot5=1725000, z19=102320, text4=72506300):
    """[Lib] Equipment transfer: Mes⇒Item
    lot5: Item lottery ID
    z19: Global event flag
    text4: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_32_x1(text1=text4, z41=0, z61=-1, z62=0)
    # lot:1725000:Dragon Chime
    if call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z23=1011, lot1=lot5)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_32_x19(lot1=lot5, z9=z19)
    """State 5: End state"""
    return 0

def talk_m10_32_x22(z1=132020104, z2=102327, z3=132020107, z4=10323000, z5=102333, z6=60, z7=102317,
                    z8=132020109):
    """[Lib] Pilgrim in Shenzhen: Conversation
    z1: Contact: Area and other flags
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Direction: Area and Other Flags
    z4: Magic Square: OBJ instance ID
    z5: Main encounter: Global event flag
    z6: Current pledge rank: Area variable
    z7: Main generation stop: Global event flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102321) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: greeting conversation_SubState"""
        assert talk_m10_32_x23(z1=z1, z6=z6)
        """State 4: [Lib] Pilgrim in Shenzhen: Menu_SubState"""
        assert talk_m10_32_x24(z2=z2, z3=z3, z4=z4, z6=z6, z8=z8)
    elif GetEventFlag(104120) != 0:
        """State 6: [Lib] Conversation: General purpose_SubState"""
        assert talk_m10_32_x0(text10=72509000, z63=0, z64=0)
    else:
        """State 5: [Lib] Pilgrim in Shenzhen: First conversation_SubState"""
        assert talk_m10_32_x27(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, z7=z7, z8=z8)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m10_32_x23(z1=132020104, z6=60):
    """[Lib] Pilgrim in Shenzhen: greeting conversation
    z1: Contact: Area and other flags
    z6: Current pledge rank: Area variable
    """
    """State 0,1: Greeting: Start"""
    if (GetPlayerCovenant() == 9) != 0 and GetEventFlag(102319) != 1:
        """State 8: When pledge ring is not acquired: Insurance_SubState"""
        # lot:2006000:Abyss Seal
        assert talk_m10_32_x47(lot1=2006000, z9=102319)
        """State 3: [Lib] Conversation: Greeting: Single _SubState"""
        Label('L0')
        # talk:72505000:"Young Undead, do you expect me to just keel over?"
        assert talk_m10_32_x20(z1=z1, text10=72505100, text11=72505000)
    else:
        """State 4: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m10_32_x42(z32=9, z6=z6, z33=218, z34=102337, z35=102338, z36=102339)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z6) > 1) != 0 and GetEventFlag(102337) != 1:
                """State 5: Conversation: Pledge Ranking 1_SubState"""
                # talk:72506000:"Young Undead, my work is done...", lot:2006011:Resonant Soul
                assert talk_m10_32_x16(text5=72506000, z20=0, lot6=2006011, z21=102337, z22=218, z6=z6)
            elif (GetAreaVariable(z6) > 2) != 0 and GetEventFlag(102338) != 1:
                """State 6: Conversation: Pledge Ranking 2_SubState"""
                # lot:2006012:Great Resonant Soul
                assert talk_m10_32_x16(text5=72506100, z20=0, lot6=2006012, z21=102338, z22=218, z6=z6)
            elif (GetAreaVariable(z6) > 3) != 0 and GetEventFlag(102339) != 1:
                """State 7: Conversation: Pledge Ranking 3_SubState"""
                # lot:2006013:Climax
                assert talk_m10_32_x16(text5=72506200, z20=0, lot6=2006013, z21=102339, z22=218, z6=z6)
            else:
                Goto('L0')
        elif call.Get() == 0:
            Goto('L0')
    """State 9: End state"""
    return 0

def talk_m10_32_x24(z2=102327, z3=132020107, z4=10323000, z6=60, z8=132020109):
    """[Lib] Pilgrims in Shenzhen: Menu
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    z6: Current pledge rank: Area variable
    z8: For trophies: Area and other flags
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 2: Menu: Branch"""
        if GetEventFlag(100979) != 0:
            """State 10: [Lib] Menu start: No passing _SubState"""
            call = talk_m10_32_x12(z46=0, z47=220, z27=72500001, z48=0)
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
                call = talk_m10_32_x17(val1=9, z14=8, lot3=0, z15=0, action1=1338, action2=1348, z8=z8)
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
            call = talk_m10_32_x12(z46=0, z47=220, z27=72500000, z48=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 6:
                Goto('L1')
            elif call.Get() == 8:
                """State 7: [Lib] Pilgrim in Shenzhen: menu passing _SubState"""
                # goods:60151000:Human Effigy
                call = talk_m10_32_x25(goods1=60151000, z2=z2, z3=z3, z4=z4)
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

def talk_m10_32_x25(goods1=60151000, z2=102327, z3=132020107, z4=10323000):
    """[Lib] Pilgrim in Shenzhen: hand over menu
    goods1: Event items
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    """
    """State 0,1: Pass: start"""
    if GetEventFlag(z2) != 0:
        """State 10: Confirmation dialog during magic square release_SubState"""
        # action:1213:"Cannot give now"
        assert talk_m10_32_x18(action5=1213)
    else:
        """State 5: Menu to pass ○○: Conversation to pass_SubState"""
        assert talk_m10_32_x1(text1=72505200, z41=0, z61=-1, z62=0)
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
            assert talk_m10_32_x48(z25=15, goods2=60151000)
            """State 3: 3rd encounter: Magic square: Open"""
            SetEventFlag(z3, 1)
            """State 4,6: Menu to pass ○○: Conversation to pass: YES_SubState"""
            assert talk_m10_32_x1(text1=72505300, z41=0, z61=-1, z62=0)
            Goto('L0')
        """State 7: Menu to pass ○○: Conversation to pass: NO_SubState"""
        assert talk_m10_32_x1(text1=72505400, z41=0, z61=-1, z62=0)
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
        assert talk_m10_32_x21(lot5=1725000, z19=102320, text4=72506300)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        assert talk_m10_32_x1(text1=72505500, z41=0, z61=-1, z62=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_32_x27(z1=132020104, z2=102327, z3=132020107, z4=10323000, z5=102333, z7=102317, z8=132020109):
    """[Lib] Pilgrim in Shenzhen: first conversation
    z1: Contact: Area and other flags
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    z5: Main encounter: Global event flag
    z7: Main generation stop: Global event flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: First conversation: start"""
    if GetEventFlag(202752) != 0 and GetEventFlag(z5) != 0:
        """State 4: [Lib] Pilgrim in Shenzhen: Encounter 3rd conversation _SubState"""
        Label('L0')
        assert talk_m10_32_x30(z2=z2, z3=z3, z4=z4, z5=z5, z8=z8)
    elif GetEventFlag(202751) != 0 and GetEventFlag(z5) != 1:
        Goto('L0')
    elif GetEventFlag(202751) != 0 and GetEventFlag(z5) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: second encounter _SubState"""
        Label('L1')
        assert talk_m10_32_x29(z7=z7, z5=z5)
    elif GetEventFlag(202750) != 0 and GetEventFlag(z5) != 1:
        Goto('L1')
    else:
        """State 2: [Lib] Pilgrims in Shenzhen: first encounter conversation_SubState"""
        assert talk_m10_32_x28(z7=z7, z5=z5)
    """State 5: End state"""
    return 0

def talk_m10_32_x28(z7=102317, z5=102333):
    """[Lib] Pilgrim in Shenzhen: first encounter
    z7: Generation stop: Global event flag
    z5: Encounter: Global event flag
    """
    """State 0,1: First encounter conversation: Start"""
    if GetEventFlag(202750) != 0:
        """State 4: Talk: 1st encounter: Loop_SubState"""
        # talk:72500100:"The Dark is still nascent within you.\nMay the Dark shine your way..."
        assert talk_m10_32_x0(text10=72500100, z63=0, z64=0)
    else:
        """State 3: Talk: 1st encounter_SubState"""
        # talk:72500000:"Ahh, look how far this Undead has wandered."
        call = talk_m10_32_x0(text10=72500000, z63=202750, z64=0)
        if call.Done() and GetEventFlag(z7) != 1:
            """State 2: First encounter: stop generation"""
            Label('L0')
            SetEventFlag(z5, 1)
            SetEventFlag(z7, 1)
            assert GetEventFlag(z7) != 0 and GetEventFlag(z5) != 0
        elif call.Done() and GetEventFlag(z5) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 5: End state"""
    return 0

def talk_m10_32_x29(z7=102317, z5=102333):
    """[Lib] Pilgrim in Shenzhen: second encounter
    z7: Generation stop: Global event flag
    z5: Encounter: Global event flag
    """
    """State 0,1: Encounter 2nd conversation: Start"""
    if GetEventFlag(202751) != 0:
        """State 4: Talk: Second encounter: Loop_SubState"""
        # talk:72500300:"May we meet again, somewhere, some time..."
        assert talk_m10_32_x0(text10=72500300, z63=0, z64=0)
    else:
        """State 3: Speak: Second encounter_SubState"""
        # talk:72500200:"Young Undead, don't let this curse weigh upon you."
        call = talk_m10_32_x0(text10=72500200, z63=202751, z64=0)
        if call.Done() and GetEventFlag(z7) != 1:
            """State 2: Second encounter: Stop generation"""
            Label('L0')
            SetEventFlag(z5, 1)
            SetEventFlag(z7, 1)
            assert GetEventFlag(z7) != 0 and GetEventFlag(z5) != 0
        elif call.Done() and GetEventFlag(z5) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 5: End state"""
    return 0

def talk_m10_32_x30(z2=102327, z3=132020107, z4=10323000, z5=102333, z8=132020109):
    """[Lib] Pilgrim in Shenzhen: 3rd encounter
    z2: Magic Square Open: Global Event Flag
    z3: Magic Square Open: Area Other Flag
    z4: Magic Square: OBJ instance ID
    z5: Main encounter: Global event flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: Encounter 3rd conversation: Start"""
    if GetEventFlag(202752) != 0:
        """State 6: Speak: 3rd encounter: YES / NO dialog: NO: Loop_SubState"""
        # talk:72500900:"We meet again, young Undead."
        assert talk_m10_32_x0(text10=72500900, z63=0, z64=0)
    else:
        """State 5: Talk: 3rd encounter_SubState"""
        # talk:72500400:"We meet again, young Undead."
        assert talk_m10_32_x0(text10=72500400, z63=202752, z64=0)
    """State 10: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:2006000:Abyss Seal, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
    call = talk_m10_32_x40(val1=9, z14=8, lot3=2006000, z15=102319, action1=1338, action2=1348, z8=z8)
    if call.Get() == 1:
        """State 2: 3rd encounter: After signing the pledge: Set flag"""
        SetEventFlag(102321, 1)
        assert GetEventFlag(102321) != 0
        """State 3: 3rd encounter: Magic square: Open"""
        SetEventFlag(z3, 1)
        """State 4,9: Speak: 3rd encounter: YES / NO dialog: YES_SubState"""
        # talk:72500500:"There you are, you are now a Pilgrim of Dark."
        assert talk_m10_32_x1(text1=72500500, z41=0, z61=-1, z62=0)
    elif call.Get() == 0 and GetEventFlag(202753) != 0:
        """State 8: Speak: 3rd encounter: YES / NO dialog: NO: Loop: YES / NO dialog: NO_SubState"""
        # talk:72501000:"Then choose your own path."
        assert talk_m10_32_x1(text1=72501000, z41=0, z61=-1, z62=0)
    elif call.Get() == 0:
        """State 7: Speak: 3rd encounter: YES / NO dialog: NO_SubState"""
        # talk:72500800:"Hmm... Perhaps I was wrong."
        assert talk_m10_32_x1(text1=72500800, z41=202753, z61=-1, z62=0)
    """State 11: End state"""
    return 0

def talk_m10_32_x31(lot2=_, z10=_, z11=0, z13=_, z44=0, z45=0):
    """[Lib] Item acquisition dialog: Conversation
    lot2: Item lottery ID
    z10: Item transfer: Global event flag
    z11: Conversation: Global conversation flag
    z13: Trophy acquisition: Area and other flags
    z44: Emigration permission: Global event flag
    z45: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z45, 1)
    SetEventFlag(z44, 1)
    SetEventFlag(z13, 1)
    SetEventFlag(z11, 1)
    SetEventFlag(z10, 1)
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x32(lot4=1307000, z16=102001, text2=30706000, text3=30706020, z17=0, z18=132020177):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z16: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z17: Conversation: Global conversation flag
    z18: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_32_x1(text1=text2, z41=0, z61=-1, z62=0)
    if call.Done() and GetEventFlag(z16) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z17, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_32_x1(text1=text3, z41=0, z61=-1, z62=0)
    # lot:1307000:Vengarl's Helm
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z23=1011, lot1=lot4)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_32_x31(lot2=lot4, z10=z16, z11=z17, z13=z18, z44=0, z45=0)
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

def talk_m10_32_x36(text8=_, z37=0, z38=20, z39=80):
    """[Lib] Conversation: Hostile display only
    text8: Conversation ID
    z37: Conversation flag
    z38: Display distance
    z39: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), z38)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z37, 1)
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

def talk_m10_32_x39(goods3=_, z26=_):
    """[Lib] Menu item: Gesture
    goods3: Gesture: Item ID
    z26: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_32_x46(goods3=goods3, z26=z26)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_32_x40(val1=9, z14=8, lot3=_, z15=_, action1=1338, action2=1348, z8=132020109):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z14: Event action
    lot3: Item lottery ID
    z15: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z8, 1)
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
            assert talk_m10_32_x41(z14=z14, val1=val1, lot3=lot3, z15=z15) and ItemAwardDisplay() != 1
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

def talk_m10_32_x41(z14=8, val1=9, lot3=_, z15=_):
    """[Lib] Event action: Pledge
    z14: Event action
    val1: Pledge type
    lot3: Item lottery ID
    z15: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z14)
    assert PlayerIsInEventAction(z14) != 0
    """State 3: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z14) != 1 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(z15) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(z15) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_32_x50(z23=1011, lot1=lot3)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z14) != 1 and GetEventFlag(z15) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z14) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z15, 1)
        AwardItem(lot3, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z14) != 1
    """State 8: End state"""
    return 0

def talk_m10_32_x42(z32=9, z6=60, z33=218, z34=102337, z35=102338, z36=102339):
    """[Lib] Pledge: Rank up: Conversation: 1
    z32: Pledge: Pledge type
    z6: Current rank: Area variable
    z33: Previous rank: Global variable
    z34: Ranking 1: Item transfer: Global event flag
    z35: Ranking 2: Item transfer: Global event flag
    z36: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z6, GetPlayerCovenantLevel(z32))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z33) > GetAreaVariable(z6)) != 1 and (GetGlobalVariable(z33) == GetAreaVariable(z6))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z33) > GetAreaVariable(z6)) != 0 and (GetGlobalVariable(z33) == GetAreaVariable(z6))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z33, GetAreaVariable(z6))
    elif GetEventFlag(z34) != 1 and (GetGlobalVariable(z33) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(z35) != 1 and (GetGlobalVariable(z33) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(z36) != 1 and (GetGlobalVariable(z33) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_32_x43(goods3=_, z26=_, z27=_, z28=_):
    """[Lib] NPC menu: Gesture alone
    goods3: Item: Event item
    z26: Item transfer: Global event flag
    z27: NPC menu: With gesture
    z28: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(z26) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            if (ItemCount(goods3, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_32_x12(z46=0, z47=220, z27=z27, z48=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m10_32_x39(goods3=goods3, z26=z26)
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
        call = talk_m10_32_x12(z46=0, z47=220, z27=z28, z48=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_32_x44(text7=_, z29=_, z30=10329010, z31=-1):
    """[Lib] Conversation: For unique key guide
    text7: Conversation ID
    z29: Conversation flag
    z30: Key guide parameters
    z31: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z30)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), z31)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z29, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_32_x45(lot2=_, z10=_, text1=_, z11=0, z12=10329010, z13=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: UnicKey
    lot2: Item lottery ID
    z10: Get: Global event flag
    text1: Conversation ID
    z11: Conversation: Global conversation flag
    z12: Key guide parameters
    z13: Trophy: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, z12)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m10_32_x1(text1=text1, z41=0, z61=-1, z62=0)
    if call.Done() and GetEventFlag(z10) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z11, 1)
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_32_x50(z23=1011, lot1=lot2)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_32_x31(lot2=lot2, z10=z10, z11=z11, z13=z13, z44=0, z45=0)
    """State 9: End state"""
    return 0

def talk_m10_32_x46(goods3=_, z26=_):
    """[Lib] Get gesture dialog
    goods3: Item ID
    z26: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods3, 0, -1)
    SetEventFlag(z26, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_32_x47(lot1=2006000, z9=102319):
    """[Lib] Conversation: Item transfer: Item: Key
    lot1: Item lottery
    z9: Item transfer: Global event flag
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
        assert talk_m10_32_x50(z23=1011, lot1=lot1)
    elif GetEventFlag(z9) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_32_x19(lot1=lot1, z9=z9)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m10_32_x48(z25=15, goods2=60151000):
    """[Lib] Event action: Pass
    z25: Event action
    goods2: Item to be handed: Event item
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z25)
    assert PlayerIsInEventAction(z25) != 0
    """State 2: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z25) != 1
    """State 4: Event action: Pass: Item transfer"""
    # goods:60151000:Human Effigy
    ConsumeItem(goods2, 1)
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z25) != 1
    """State 5: End state"""
    return 0

def talk_m10_32_x49(text6=72509600, z24=0, val2=9):
    """[Lib] Death status_ (pledge cancellation)
    text6: Conversation ID
    z24: Global: death flag
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
    talk_m10_32_x2(text6=text6, z24=z24)

def talk_m10_32_x50(z23=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z23: Text ID
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
        assert talk_m10_32_x0(text10=30700400, z63=201004, z64=0)
        """State 8: Menu: Exit state"""
        return 1
    elif GetEventFlag(201002) != 0:
        """State 5: Talk: 4_SubState"""
        # talk:30700300:"I know not what brings you on this journey,\nnor will I deign to ask."
        assert talk_m10_32_x0(text10=30700300, z63=201003, z64=0)
    elif GetEventFlag(201001) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:30700200:"Long ago, I was hired to defend the kingdom."
        assert talk_m10_32_x0(text10=30700200, z63=201002, z64=0)
    elif GetEventFlag(201000) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:30700100:"What business have you here, traveller?"
        assert talk_m10_32_x0(text10=30700100, z63=201001, z64=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:30700000:"Leave me be."
        assert talk_m10_32_x0(text10=30700000, z63=201000, z64=0)
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
            call = talk_m10_32_x12(z46=0, z47=220, z27=30700001, z48=0)
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
            call = talk_m10_32_x12(z46=0, z47=220, z27=30700000, z48=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 9: [Lib] Menu item: Gesture_SubState"""
                call = talk_m10_32_x39(goods3=63017000, z26=0)
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
        assert talk_m10_32_x1(text1=30705000, z41=201020, z61=-1, z62=0)
    elif GetEventFlag(201012) != 0 and GetEventFlag(102001) != 1 and GetEventFlag(104000) != 1:
        """State 8: Equipment transfer (Condition: Durahan destroyed) _SubState"""
        # lot:1307000:Vengarl's Helm, talk:30706000:"I like quiet. It's all I ever wished for."
        assert talk_m10_32_x32(lot4=1307000, z16=102001, text2=30706000, text3=30706020, z17=0, z18=132020177)
    elif GetEventFlag(201012) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(201010, 0)
        SetEventFlag(201011, 0)
        SetEventFlag(201012, 0)
        """State 5: Menu conversation: Part 1_SubState"""
        Label('L0')
        assert talk_m10_32_x1(text1=30705100, z41=201010, z61=-1, z62=0)
    elif GetEventFlag(201011) != 0:
        """State 7: Menu conversation: 3_SubState"""
        assert talk_m10_32_x1(text1=30705300, z41=201012, z61=-1, z62=0)
    elif GetEventFlag(201010) != 0:
        """State 6: Menu conversation: 2_SubState"""
        assert talk_m10_32_x1(text1=30705200, z41=201011, z61=-1, z62=0)
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
        assert talk_m10_32_x44(text7=50200700, z29=0, z30=10329010, z31=-1)
    elif GetEventFlag(206105) != 0:
        """State 9: Before the defeat: Talk to: 7_SubState"""
        # talk:50200600:"We seem to be at a standstill.\nThe wounds we exchange are never lethal."
        assert talk_m10_32_x44(text7=50200600, z29=206106, z30=10329010, z31=-1)
        """State 2: Before defeat: White phantom can appear"""
        SetEventFlag(102980, 1)
        assert GetEventFlag(102980) != 0
    elif GetEventFlag(206104) != 0:
        """State 8: Before the defeat: Talk to: 6_SubState"""
        # talk:50200500:"I wish to ask a favour of you.\nI want you to kill my betrothed."
        assert talk_m10_32_x44(text7=50200500, z29=206105, z30=10329010, z31=-1)
    elif GetEventFlag(206103) != 0:
        """State 7: Before the defeat: Talk to: 5_SubState"""
        # talk:50200400:"Nobody knows when we were born."
        assert talk_m10_32_x44(text7=50200400, z29=206104, z30=10329010, z31=-1)
    elif GetEventFlag(206102) != 0:
        """State 6: Before the defeat: Talk to: 4_SubState"""
        # talk:50200300:"Our master was a tragically lonely soul."
        assert talk_m10_32_x44(text7=50200300, z29=206103, z30=10329010, z31=-1)
    elif GetEventFlag(206101) != 0:
        """State 5: Before the defeat: Talk: Part 3_SubState"""
        # talk:50200200:"We once had a master.\nHe created us long, long ago."
        assert talk_m10_32_x44(text7=50200200, z29=206102, z30=10329010, z31=-1)
    elif GetEventFlag(206100) != 0:
        """State 4: Before the defeat: Talk to: 2_SubState"""
        # talk:50200100:"Are you not afraid of me?"
        assert talk_m10_32_x44(text7=50200100, z29=206101, z30=10329010, z31=-1)
    else:
        """State 3: Before the defeat: Talk: Part 1_SubState"""
        # talk:50200000:"Human, are we?"
        assert talk_m10_32_x44(text7=50200000, z29=206100, z30=10329010, z31=-1)
    """State 11: End state"""
    return 0

def talk_m10_32_x57():
    """Manscorpion 後: After defeat"""
    """State 0,1: After defeat: Start"""
    if (GetEventFlag(102981) != 0 and GetEventFlag(100951) != 0 and GetEventFlag(104430) != 1 and GetEventFlag(102982)
        != 1):
        """State 7: Equipment transfer: Defeat the queen of the eagle_SubState"""
        # lot:1502010:Black Scorpion Stinger, talk:50206000:"Young human..."
        assert talk_m10_32_x45(lot2=1502010, z10=102982, text1=50206000, z11=0, z12=10329010, z13=0)
    elif GetEventFlag(102981) != 0:
        """State 5: After defeat: Talk to: 3_SubState"""
        # talk:50201200:"I have no gods to pray to."
        call = talk_m10_32_x44(text7=50201200, z29=206111, z30=10329010, z31=-1)
        if call.Done() and GetEventFlag(102983) != 1:
            """State 2: [Lib] NPC menu: Gesture alone_SubState"""
            # goods:63010000:"Warmup" Gesture
            assert talk_m10_32_x43(goods3=63010000, z26=102983, z27=50200000, z28=50200001)
        elif call.Done():
            pass
    else:
        """State 3: After defeat: Speak: Part 1_SubState"""
        # lot:1502000:Fragrant Branch of Yore, talk:50201000:"You've defeated my better half."
        assert talk_m10_32_x45(lot2=1502000, z10=102981, text1=50201000, z11=0, z12=10329010, z13=0)
    """State 8: End state"""
    return 0

def talk_m10_32_x58():
    """Wandering Warrior: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203212) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:74200700:"For the good of the world, and for my own honour."
        call = talk_m10_32_x0(text10=74200700, z63=0, z64=0)
        if call.Done() and GetEventFlag(102406) != 1:
            """State 3: Conversation: Set movement permission flag"""
            SetEventFlag(102406, 1)
            assert GetEventFlag(102406) != 0
        elif call.Done():
            pass
        """State 7: [Lib] NPC menu: Gesture alone_SubState"""
        # goods:63018000:"Fist pump" Gesture
        assert talk_m10_32_x43(goods3=63018000, z26=102403, z27=74200000, z28=74200001)
    elif GetEventFlag(203211) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:74200600:"That bastard with the ring lives in Brightstone Cove down the way."
        assert talk_m10_32_x0(text10=74200600, z63=203212, z64=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:74200400:"Heh heh... Just wait, you dirty rat..."
        assert talk_m10_32_x0(text10=74200400, z63=203210, z64=0)
        """State 8: Talk to: 2_SubState"""
        # talk:74200500:"Hm? Oh...oh!\nI-I remember you?!"
        assert talk_m10_32_x1(text1=74200500, z41=203211, z61=-1, z62=0)
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
        assert talk_m10_32_x0(text10=77500200, z63=0, z64=0)
    else:
        """State 4: 1_SubState to talk to"""
        # talk:77500100:"Thank you for helping me.\nHow awkward...that I fell for such a trap."
        call = talk_m10_32_x0(text10=77500100, z63=205400, z64=0)
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
    assert talk_m10_32_x0(text10=30700800, z63=0, z64=0)
    """State 3: End state"""
    return 0

def talk_m10_32_x61():
    """Manscorpion ♂: ring not installed"""
    """State 0,1,2: When not wearing a ring_SubState"""
    # talk:50209999:"...?"
    assert talk_m10_32_x44(text7=50209999, z29=0, z30=10329010, z31=-1)
    """State 3: End state"""
    return 0

