# -*- coding: utf-8 -*-
def talk_m20_21_7000():
    """Dragon Miko (within the castle)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        SetEventFlag(221020167, 1)
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(z54=103520, z55=104020, z56=221020161)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=70009200, z40=0, z41=20, z42=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(z52=221020162, text15=70009500, text16=70009500, z53=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=70009600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Dragon Miko: Conversation (within the Royal Castle) _SubState"""
                call = talk_m20_21_x52()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 11: Waiting for hostility: Dragon Maiden (in the Royal Castle) _SubState"""
                    Label('L2')
                    call = talk_m20_21_x67()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 5: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(z61=103520, text23=70009100, z62=0, z63=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(221020056) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(221020055) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(221020054) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(221020053) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(221020052) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(221020051) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(221020050) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020166) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020165) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=70009300, z57=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_21_7001():
    """Dragon Miko (before clear)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        SetEventFlag(221020174, 1)
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(z54=103520, z55=104020, z56=221020171)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=70009200, z40=0, z41=20, z42=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(z52=221020172, text15=70009500, text16=70009500, z53=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=70009600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Dragon Miko: Conversation (before clear) _SubState"""
                call = talk_m20_21_x55()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 11: Waiting for hostility: Dragon Miko (before clear) _SubState"""
                    Label('L2')
                    call = talk_m20_21_x68()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 5: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(z61=103520, text23=70009100, z62=0, z63=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(221020066) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(221020065) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(221020064) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(221020063) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(221020062) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(221020061) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(221020060) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020176) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020175) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=70009300, z57=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_21_7030():
    """Queen"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            """State 5: [Lib] Event: Branch_SubState"""
            call = talk_m20_21_x9(z54=103540, z55=104040, z56=221020181)
            if call.Get() == 1:
                """State 6: [Lib] Reunion hostility_SubState"""
                talk_m20_21_x3(text8=70209200, z40=0, z41=20, z42=80)
                Quit()
            elif call.Get() == 0:
                pass
            while True:
                """State 8: Queen: Conversation_SubState"""
                call = talk_m20_21_x61()
                if call.Done():
                    Continue('mainloop')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L0')
                    call = talk_m20_21_x5(text19=70209400, text20=70209410, text21=70209400, text22=70209410,
                                          z59=221020185, z60=221020186)
                    if call.Done():
                        pass
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 2: Queen: Set generation stop flag"""
                        SetEventFlag(102140, 1)
                        assert (GetEventFlag(102140) != 0 and (GetStateTime() > GetRandomValueForStateTime(3,
                                3)) != 0)
                        """State 4: Queen: Erase setting"""
                        DeleteEnemyByGeneratorGroup(61, 0)
                        Break('mainloop')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020186) != 1:
                    Goto('L0')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020185) != 1:
                    Goto('L0')
    """State 3: Conversation: System: End"""
    EndMachine()

def talk_m20_21_7211():
    """Prime Minister's Spirit"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(z54=103590, z55=104090, z56=221020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=72119200, z40=0, z41=20, z42=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                call = talk_m20_21_x6(z52=221020122, text15=72119500, text16=72119500, z53=72119500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L0')
                    talk_m20_21_x7(text18=72119600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L0')
            """State 9: [Lib] Killing state_SubState"""
            talk_m20_21_x8(text17=72119300, z57=0)
            Quit()
        elif call.Get() == 0:
            pass
        """State 10: Prime Minister: Conversation_SubState"""
        assert talk_m20_21_x56()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_21_7250():
    """Shenzhen Pilgrim (Dolan Greig)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(z54=103623, z55=104120, z56=221020101)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=72509200, z40=0, z41=20, z42=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(z52=221020102, text15=72509500, text16=72509500, z53=72509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 11: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m20_21_x50(text5=72509600, z23=0, val2=9)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Pilgrim in Shenzhen: Conversation_SubState"""
                call = talk_m20_21_x22(z1=221020104, z2=102326, z3=221020107, z4=20213000, z5=102332,
                                       z6=60, z7=102316, z8=221020109)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_21_x5(text19=72509400, text20=72509410, text21=72509420, text22=72509400,
                                          z59=221020105, z60=221020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 5: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m20_21_x15(z43=103620, text9=72509100, z44=0, val3=9, z45=200908,
                                               z46=103623)
                        if call.Done():
                            """State 2: Shenzhen Pilgrim: Magic Square Flag OFF"""
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020105) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=72509300, z57=0)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()

def talk_m20_21_7430():
    """Tsukimitsu (Doran Greig: second encounter)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(z54=103662, z55=104160, z56=221020141)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=74309200, z40=0, z41=20, z42=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(z52=221020142, text15=74309500, text16=74309500, z53=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=74309600, z58=104162)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Tsukimitsu: Conversation_SubState"""
                call = talk_m20_21_x59()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_21_x5(text19=74309400, text20=74309410, text21=74309420, text22=74309400,
                                          z59=221020145, z60=221020146)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(z61=103660, text23=74309100, z62=0, z63=103662)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020146) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020145) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=74309300, z57=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_21_7602():
    """Captive girl"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(z54=103740, z55=104240, z56=221020151)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=76029200, z40=0, z41=20, z42=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(z52=221020152, text15=76029500, text16=76029500, z53=76029500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=76029600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0 and GetEventFlag(104240) != 0:
            """State 11: Captive Girl: Conversation (Death) _SubState"""
            assert talk_m20_21_x66()
            continue
        elif call.Get() == 0:
            while True:
                """State 10: Captive Girl: Conversation (Living) _SubState"""
                call = talk_m20_21_x64()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m20_21_x5(text19=76029400, text20=76029410, text21=76029420, text22=76029400,
                                          z59=221020154, z60=221020155)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(z61=103740, text23=76029100, z62=0, z63=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020155) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020154) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=76029300, z57=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m20_21_x0(text10=_, z66=_, z67=_):
    """[Lib] Conversation: General purpose
    text10: Conversation ID
    z66: Conversation flag
    z67: Global event flag
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
    SetEventFlag(z66, 1)
    SetEventFlag(z67, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_21_x1(text1=_, z44=_, z64=_, z65=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z44: Conversation flag
    z64: Display distance
    z65: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z64)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z44, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m20_21_x2(text5=_, z23=_):
    """[Lib] Conversation: Event end
    text5: Conversation ID
    z23: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text5, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z23, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_21_x3(text8=_, z40=0, z41=20, z42=80):
    """[Lib] Reunion hostility
    text8: Conversation message ID
    z40: Conversation flag ID
    z41: Display distance
    z42: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m20_21_x37(text8=text8, z40=z40, z41=z41, z42=z42)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_21_x4(z61=_, text23=_, z62=0, z63=_):
    """[Lib] First hostility
    z61: Hostile: Global event flag
    text23: Conversation ID
    z62: Conversation flag
    z63: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z61, 1)
    SetEventFlag(z63, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z61) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m20_21_x1(text1=text23, z44=z62, z64=-1, z65=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_21_x5(text19=_, text20=_, text21=_, text22=_, z59=_, z60=_):
    """[Lib] Hostile waiting
    text19: Conversation ID: 1 attacked
    text20: Conversation ID: Attacked 2
    text21: Conversation ID: 3 attacked
    text22: Conversation ID: 4 attacked
    z59: No use: Area and other flags
    z60: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z60) != 1, z60, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z59) != 1, z59, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m20_21_x1(text1=text22, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_21_x1(text1=text21, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_21_x1(text1=text20, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_21_x1(text1=text19, z44=0, z64=-1, z65=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_21_x6(z52=_, text15=_, text16=_, z53=_):
    """[Lib] Hostile state
    z52: Area and other flags: HP decreased
    text15: Conversation ID: HP drop 1
    text16: Conversation ID: HP drop 2
    z53: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z52) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m20_21_x10(text15=text15, z52=z52)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_21_x10(text15=text16, z52=z52)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_21_x10(text15=text16, z52=z52)

def talk_m20_21_x7(text18=_, z58=_):
    """[Lib] Death status
    text18: Conversation ID
    z58: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m20_21_x2(text5=text18, z23=z58)

def talk_m20_21_x8(text17=_, z57=0):
    """[Lib] Murder status
    text17: Conversation ID
    z57: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_21_x2(text5=text17, z23=z57)

def talk_m20_21_x9(z54=_, z55=_, z56=_):
    """[Lib] Event: Branch
    z54: Hostile flag
    z55: death flag
    z56: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z55) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z56) != 0
    elif GetEventFlag(z54) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m20_21_x10(text15=_, z52=_):
    """[Lib] Conversation: HP drop
    text15: Conversation ID
    z52: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text15, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z52, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_21_x11(action1=_):
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

def talk_m20_21_x12(z49=0, z50=220, z26=_, z51=0):
    """[Lib] Menu start: General purpose
    z49: Camera parameter ID
    z50: Target Damipoly ID
    z26: NPC event parameter ID
    z51: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z51, z49, z50, z26)
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

def talk_m20_21_x13(text13=_, text14=_):
    """[Lib] Menu exit: General purpose
    text13: Conversation ID (at the time of purchase)
    text14: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m20_21_x1(text1=text13, z44=0, z64=-1, z65=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m20_21_x1(text1=text14, z44=0, z64=-1, z65=0)
    """State 4: End state"""
    return 0

def talk_m20_21_x14(text12=_):
    """[Lib] Menu cancellation: General purpose
    text12: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m20_21_x1(text1=text12, z44=0, z64=-1, z65=0)
    """State 4: End state"""
    return 0

def talk_m20_21_x15(z43=103620, text9=72509100, z44=0, val3=9, z45=200908, z46=103623):
    """[Lib] First hostility _ (pledge cancellation)
    z43: Hostile: Global event flag
    text9: Conversation ID
    z44: Conversation flag
    val3: Cancellation pledge name
    z45: Pledge cancellation: Global conversation flag
    z46: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z43, 1)
    SetEventFlag(z46, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z43) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m20_21_x36(val2=val3)
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
    assert talk_m20_21_x1(text1=text9, z44=z44, z64=-1, z65=0)
    """State 6: First hostility: end"""
    return 0

def talk_m20_21_x16(text4=_, z19=0, lot6=_, z20=_, z21=218, z6=60):
    """[Lib] Conversation: Pledge ranking
    text4: Ranking: Conversation ID
    z19: Ranking: Conversation flag
    lot6: Item lottery
    z20: Ranking transfer: Global event flag
    z21: Previous rank: Global variable
    z6: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m20_21_x18(action5=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text4, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z19, 1)
    if CanGetItemLot(lot6, 1) != 1 and GetEventFlag(z20) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z22=1011, lot1=lot6)
    elif GetEventFlag(z20) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m20_21_x19(lot1=lot6, z9=z20)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z21, GetAreaVariable(z6))
    """State 11: End state"""
    return 0

def talk_m20_21_x17(val1=9, z10=8, lot2=0, z11=0, action1=1338, action2=1348, z8=221020109):
    """[Lib] Menu item: Make a pledge
    val1: Pledge name
    z10: Event action
    lot2: Item lottery ID
    z11: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m20_21_x18(action5=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m20_21_x41(val1=val1, z10=z10, lot2=lot2, z11=z11, action1=action1, action2=action2,
                               z8=z8)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m20_21_x18(action5=_):
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

def talk_m20_21_x19(lot1=_, z9=_):
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

def talk_m20_21_x20(z1=221020104, text10=72505100, text11=72505000):
    """[Lib] Conversation: Greeting: Single
    z1: Area other flag: Contact flag
    text10: Text ID: Talk to_continuous
    text11: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(z1) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m20_21_x0(text10=text10, z66=0, z67=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m20_21_x0(text10=text11, z66=0, z67=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(z1, 1)
    """State 5: End state"""
    return 0

def talk_m20_21_x21(lot5=1725000, z18=102320, text3=72506300):
    """[Lib] Equipment transfer: Mes⇒Item
    lot5: Item lottery ID
    z18: Global event flag
    text3: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m20_21_x1(text1=text3, z44=0, z64=-1, z65=0)
    # lot:1725000:Dragon Chime
    if call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z22=1011, lot1=lot5)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m20_21_x19(lot1=lot5, z9=z18)
    """State 5: End state"""
    return 0

def talk_m20_21_x22(z1=221020104, z2=102326, z3=221020107, z4=20213000, z5=102332, z6=60, z7=102316,
                    z8=221020109):
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
        assert talk_m20_21_x23(z1=z1, z6=z6)
        """State 4: [Lib] Pilgrim in Shenzhen: Menu_SubState"""
        assert talk_m20_21_x24(z2=z2, z3=z3, z4=z4, z6=z6, z8=z8)
    elif GetEventFlag(104120) != 0:
        """State 6: [Lib] Conversation: General purpose_SubState"""
        assert talk_m20_21_x0(text10=72509000, z66=0, z67=0)
    else:
        """State 5: [Lib] Pilgrim in Shenzhen: First conversation_SubState"""
        assert talk_m20_21_x27(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, z7=z7, z8=z8)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m20_21_x23(z1=221020104, z6=60):
    """[Lib] Pilgrim in Shenzhen: greeting conversation
    z1: Contact: Area and other flags
    z6: Current pledge rank: Area variable
    """
    """State 0,1: Greeting: Start"""
    if (GetPlayerCovenant() == 9) != 0 and GetEventFlag(102319) != 1:
        """State 8: When pledge ring is not acquired: Insurance_SubState"""
        # lot:2006000:Abyss Seal
        assert talk_m20_21_x48(lot1=2006000, z9=102319)
        """State 3: [Lib] Conversation: Greeting: Single _SubState"""
        Label('L0')
        # talk:72505000:"Young Undead, do you expect me to just keel over?"
        assert talk_m20_21_x20(z1=z1, text10=72505100, text11=72505000)
    else:
        """State 4: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m20_21_x43(z35=9, z6=z6, z36=218, z37=102337, z38=102338, z39=102339)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z6) > 1) != 0 and GetEventFlag(102337) != 1:
                """State 5: Conversation: Pledge Ranking 1_SubState"""
                # talk:72506000:"Young Undead, my work is done...", lot:2006011:Resonant Soul
                assert talk_m20_21_x16(text4=72506000, z19=0, lot6=2006011, z20=102337, z21=218, z6=z6)
            elif (GetAreaVariable(z6) > 2) != 0 and GetEventFlag(102338) != 1:
                """State 6: Conversation: Pledge Ranking 2_SubState"""
                # lot:2006012:Great Resonant Soul
                assert talk_m20_21_x16(text4=72506100, z19=0, lot6=2006012, z20=102338, z21=218, z6=z6)
            elif (GetAreaVariable(z6) > 3) != 0 and GetEventFlag(102339) != 1:
                """State 7: Conversation: Pledge Ranking 3_SubState"""
                # lot:2006013:Climax
                assert talk_m20_21_x16(text4=72506200, z19=0, lot6=2006013, z20=102339, z21=218, z6=z6)
            else:
                Goto('L0')
        elif call.Get() == 0:
            Goto('L0')
    """State 9: End state"""
    return 0

def talk_m20_21_x24(z2=102326, z3=221020107, z4=20213000, z6=60, z8=221020109):
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
            call = talk_m20_21_x12(z49=0, z50=220, z26=72500001, z51=0)
            if call.Get() == 2:
                """State 9: [Lib] Pilgrim in Shenzhen: Menu conversation_SubState"""
                Label('L0')
                call = talk_m20_21_x26()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 6:
                """State 8: [Lib] Menu item: _SubState with a pledge"""
                Label('L1')
                # lot:0:No Item, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
                call = talk_m20_21_x17(val1=9, z10=8, lot2=0, z11=0, action1=1338, action2=1348, z8=z8)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L2')
                assert talk_m20_21_x13(text13=72501200, text14=72501300)
        else:
            """State 4: [Lib] Menu start: General purpose_SubState"""
            call = talk_m20_21_x12(z49=0, z50=220, z26=72500000, z51=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 6:
                Goto('L1')
            elif call.Get() == 8:
                """State 7: [Lib] Pilgrim in Shenzhen: menu passing _SubState"""
                # goods:60151000:Human Effigy
                call = talk_m20_21_x25(goods1=60151000, z2=z2, z3=z3, z4=z4)
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
    assert talk_m20_21_x14(text12=72501100)
    Goto('L3')

def talk_m20_21_x25(goods1=60151000, z2=102326, z3=221020107, z4=20213000):
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
        assert talk_m20_21_x18(action5=1213)
    else:
        """State 5: Menu to pass ○○: Conversation to pass_SubState"""
        assert talk_m20_21_x1(text1=72505200, z44=0, z64=-1, z65=0)
        """State 8: Execution selection dialog to pass_SubState"""
        # action:1200:"Give\n%s?", goods:60151000:Human Effigy
        call = talk_m20_21_x38(action4=1200, goods4=60151000)
        if call.Get() == 2:
            pass
        elif call.Get() == 1:
            pass
        # goods:60151000:Human Effigy
        elif call.Get() == 0 and (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 9: No target confirmation dialog_SubState"""
            # action:1206:"You do not have\n%s"
            assert talk_m20_21_x39(action3=1206, goods1=goods1)
        elif call.Get() == 0:
            """State 11: [Lib] Event action: Pass _SubState"""
            # goods:60151000:Human Effigy
            assert talk_m20_21_x49(z24=15, goods2=60151000)
            """State 3: 3rd encounter: Magic square: Open"""
            SetEventFlag(z3, 1)
            """State 4,6: Menu to pass ○○: Conversation to pass: YES_SubState"""
            assert talk_m20_21_x1(text1=72505300, z44=0, z64=-1, z65=0)
            Goto('L0')
        """State 7: Menu to pass ○○: Conversation to pass: NO_SubState"""
        assert talk_m20_21_x1(text1=72505400, z44=0, z64=-1, z65=0)
    """State 2: Pass: Exit"""
    Label('L0')
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m20_21_x26():
    """[Lib] Pilgrims in Shenzhen: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(100979) != 0 and GetEventFlag(102320) != 1 and GetEventFlag(104120) != 1:
        """State 4: Equipment transfer (Condition: Defeated Agaduran) _SubState"""
        # lot:1725000:Dragon Chime
        assert talk_m20_21_x21(lot5=1725000, z18=102320, text3=72506300)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        assert talk_m20_21_x1(text1=72505500, z44=0, z64=-1, z65=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m20_21_x27(z1=221020104, z2=102326, z3=221020107, z4=20213000, z5=102332, z7=102316, z8=221020109):
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
        assert talk_m20_21_x30(z2=z2, z3=z3, z4=z4, z5=z5, z8=z8)
    elif GetEventFlag(202751) != 0 and GetEventFlag(z5) != 1:
        Goto('L0')
    elif GetEventFlag(202751) != 0 and GetEventFlag(z5) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: second encounter _SubState"""
        Label('L1')
        assert talk_m20_21_x29(z7=z7, z5=z5)
    elif GetEventFlag(202750) != 0 and GetEventFlag(z5) != 1:
        Goto('L1')
    else:
        """State 2: [Lib] Pilgrims in Shenzhen: first encounter conversation_SubState"""
        assert talk_m20_21_x28(z7=z7, z5=z5)
    """State 5: End state"""
    return 0

def talk_m20_21_x28(z7=102316, z5=102332):
    """[Lib] Pilgrim in Shenzhen: first encounter
    z7: Generation stop: Global event flag
    z5: Encounter: Global event flag
    """
    """State 0,1: First encounter conversation: Start"""
    if GetEventFlag(202750) != 0:
        """State 4: Talk: 1st encounter: Loop_SubState"""
        # talk:72500100:"The Dark is still nascent within you.\nMay the Dark shine your way..."
        assert talk_m20_21_x0(text10=72500100, z66=0, z67=0)
    else:
        """State 3: Talk: 1st encounter_SubState"""
        # talk:72500000:"Ahh, look how far this Undead has wandered."
        call = talk_m20_21_x0(text10=72500000, z66=202750, z67=0)
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

def talk_m20_21_x29(z7=102316, z5=102332):
    """[Lib] Pilgrim in Shenzhen: second encounter
    z7: Generation stop: Global event flag
    z5: Encounter: Global event flag
    """
    """State 0,1: Encounter 2nd conversation: Start"""
    if GetEventFlag(202751) != 0:
        """State 4: Talk: Second encounter: Loop_SubState"""
        # talk:72500300:"May we meet again, somewhere, some time..."
        assert talk_m20_21_x0(text10=72500300, z66=0, z67=0)
    else:
        """State 3: Speak: Second encounter_SubState"""
        # talk:72500200:"Young Undead, don't let this curse weigh upon you."
        call = talk_m20_21_x0(text10=72500200, z66=202751, z67=0)
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

def talk_m20_21_x30(z2=102326, z3=221020107, z4=20213000, z5=102332, z8=221020109):
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
        assert talk_m20_21_x0(text10=72500900, z66=0, z67=0)
    else:
        """State 5: Talk: 3rd encounter_SubState"""
        # talk:72500400:"We meet again, young Undead."
        assert talk_m20_21_x0(text10=72500400, z66=202752, z67=0)
    """State 10: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:2006000:Abyss Seal, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
    call = talk_m20_21_x41(val1=9, z10=8, lot2=2006000, z11=102319, action1=1338, action2=1348, z8=z8)
    if call.Get() == 1:
        """State 2: 3rd encounter: After signing the pledge: Set flag"""
        SetEventFlag(102321, 1)
        assert GetEventFlag(102321) != 0
        """State 3: 3rd encounter: Magic square: Open"""
        SetEventFlag(z3, 1)
        """State 4,9: Speak: 3rd encounter: YES / NO dialog: YES_SubState"""
        # talk:72500500:"There you are, you are now a Pilgrim of Dark."
        assert talk_m20_21_x1(text1=72500500, z44=0, z64=-1, z65=0)
    elif call.Get() == 0 and GetEventFlag(202753) != 0:
        """State 8: Speak: 3rd encounter: YES / NO dialog: NO: Loop: YES / NO dialog: NO_SubState"""
        # talk:72501000:"Then choose your own path."
        assert talk_m20_21_x1(text1=72501000, z44=0, z64=-1, z65=0)
    elif call.Get() == 0:
        """State 7: Speak: 3rd encounter: YES / NO dialog: NO_SubState"""
        # talk:72500800:"Hmm... Perhaps I was wrong."
        assert talk_m20_21_x1(text1=72500800, z44=202753, z64=-1, z65=0)
    """State 11: End state"""
    return 0

def talk_m20_21_x31(lot4=_, z15=_, text2=_, z16=0, z17=_):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot4: Item lottery ID
    z15: Item transfer: Global event flag
    text2: Conversation ID
    z16: Conversation: Global conversation flag
    z17: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m20_21_x1(text1=text2, z44=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z15) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z16, 1)
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z22=1011, lot1=lot4)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_21_x32(lot3=lot4, z12=z15, z13=z16, z14=z17, z47=0, z48=0)
    """State 9: End state"""
    return 0

def talk_m20_21_x32(lot3=_, z12=_, z13=0, z14=_, z47=0, z48=0):
    """[Lib] Item acquisition dialog: Conversation
    lot3: Item lottery ID
    z12: Item transfer: Global event flag
    z13: Conversation: Global conversation flag
    z14: Trophy acquisition: Area and other flags
    z47: Emigration permission: Global event flag
    z48: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z48, 1)
    SetEventFlag(z47, 1)
    SetEventFlag(z14, 1)
    SetEventFlag(z13, 1)
    SetEventFlag(z12, 1)
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_21_x33(lot3=1721000, z12=102260, text1=72119800, z13=0, z14=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot3: Item lottery ID
    z12: Item transfer: Global event flag
    text1: Conversation ID
    z13: Conversation: Global conversation flag
    z14: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m20_21_x1(text1=text1, z44=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z12) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z13, 1)
    # lot:1721000:Royal Dirk
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z22=1011, lot1=lot3)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_21_x32(lot3=lot3, z12=z12, z13=z13, z14=z14, z47=0, z48=0)
    """State 6: End state"""
    return 0

def talk_m20_21_x34():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m20_21_x35():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_21_x36(val2=9):
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

def talk_m20_21_x37(text8=_, z40=0, z41=20, z42=80):
    """[Lib] Conversation: Hostile display only
    text8: Conversation ID
    z40: Conversation flag
    z41: Display distance
    z42: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), z41)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z40, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m20_21_x38(action4=1200, goods4=60151000):
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

def talk_m20_21_x39(action3=1206, goods1=60151000):
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

def talk_m20_21_x40(goods3=_, z25=_):
    """[Lib] Menu item: Gesture
    goods3: Gesture: Item ID
    z25: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m20_21_x47(goods3=goods3, z25=z25)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m20_21_x41(val1=9, z10=8, lot2=_, z11=_, action1=1338, action2=1348, z8=221020109):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z10: Event action
    lot2: Item lottery ID
    z11: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z8, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m20_21_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m20_21_x18(action5=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m20_21_x42(z10=z10, val1=val1, lot2=lot2, z11=z11) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m20_21_x18(action5=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m20_21_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m20_21_x36(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m20_21_x42(z10=8, val1=9, lot2=_, z11=_):
    """[Lib] Event action: Pledge
    z10: Event action
    val1: Pledge type
    lot2: Item lottery ID
    z11: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z10)
    assert PlayerIsInEventAction(z10) != 0
    """State 3: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z10) != 1 and CanGetItemLot(lot2, 1) != 1 and GetEventFlag(z11) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot2, 1) != 1 and GetEventFlag(z11) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m20_21_x51(z22=1011, lot1=lot2)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z10) != 1 and GetEventFlag(z11) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z10) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z11, 1)
        AwardItem(lot2, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z10) != 1
    """State 8: End state"""
    return 0

def talk_m20_21_x43(z35=9, z6=60, z36=218, z37=102337, z38=102338, z39=102339):
    """[Lib] Pledge: Rank up: Conversation: 1
    z35: Pledge: Pledge type
    z6: Current rank: Area variable
    z36: Previous rank: Global variable
    z37: Ranking 1: Item transfer: Global event flag
    z38: Ranking 2: Item transfer: Global event flag
    z39: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z6, GetPlayerCovenantLevel(z35))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z36) > GetAreaVariable(z6)) != 1 and (GetGlobalVariable(z36) == GetAreaVariable(z6))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z36) > GetAreaVariable(z6)) != 0 and (GetGlobalVariable(z36) == GetAreaVariable(z6))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z36, GetAreaVariable(z6))
    elif GetEventFlag(z37) != 1 and (GetGlobalVariable(z36) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(z38) != 1 and (GetGlobalVariable(z36) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(z39) != 1 and (GetGlobalVariable(z36) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m20_21_x44(goods3=63008000, z25=102435, z26=74300000, z27=74300001):
    """[Lib] NPC menu: Gesture alone
    goods3: Item: Event item
    z25: Item transfer: Global event flag
    z26: NPC menu: With gesture
    z27: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(z25) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            # goods:63008000:"Joy" Gesture
            if (ItemCount(goods3, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m20_21_x12(z49=0, z50=220, z26=z26, z51=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m20_21_x40(goods3=goods3, z25=z25)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        pass
                elif call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    """State 6: [Lib] Menu exit: No Mes_SubState"""
                    Label('L0')
                    assert talk_m20_21_x34()
                    Goto('L2')
            """State 7: [Lib] Menu canceled: No Mes_SubState"""
            Label('L1')
            assert talk_m20_21_x35()
            Goto('L2')
        """State 5: [Lib] Menu start: No gesture _SubState"""
        call = talk_m20_21_x12(z49=0, z50=220, z26=z27, z51=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m20_21_x45(text7=_, z31=_, z32=_, z33=_, z34=0):
    """[Lib] Conversation: Canceling startup state
    text7: Conversation ID
    z31: Conversation flag
    z32: Activation state release: Area and other flags
    z33: Rock sitting 1: Poke your cheek with your hand
    z34: Extend both hands back
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 10: Conversation: Cancel start state: Branch"""
    if GetEventFlag(z32) != 0:
        """State 8: Conversation: Activation state release: Second time"""
        Label('L0')
        DeleteKeyGuideArea()
        SetEventFlag(z32, 1)
    elif GetEventFlag(z33) != 1 and GetEventFlag(z34) != 1:
        Goto('L0')
    else:
        """State 7: Conversation: Activation state release: First use"""
        DeleteKeyGuideArea()
        SetEventFlag(z32, 1)
        assert GetEventFlag(z32) != 0
        """State 9: Conversation: Release hood: Wait"""
        KeyGuideTemporarilyInvalidIf(GetEventFlag(z33) != 0, 3.5)
        KeyGuideTemporarilyInvalidIf(GetEventFlag(z34) != 0, 3.5)
        assert (GetStateTime() > GetRandomValueForStateTime(3, 3)) != 0
    """State 4: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z31, 1)
    """State 11: Conversation: End"""
    return 0

def talk_m20_21_x46(text6=_, z28=_, z29=20219000, z30=45):
    """[Lib] Conversation: For unique key guide
    text6: Conversation ID
    z28: Conversation flag
    z29: Key guide parameters
    z30: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z29)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text6, GetCommonEventParamDecimal(7), z30)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z28, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_21_x47(goods3=_, z25=_):
    """[Lib] Get gesture dialog
    goods3: Item ID
    z25: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods3, 0, -1)
    SetEventFlag(z25, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_21_x48(lot1=2006000, z9=102319):
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
        assert talk_m20_21_x51(z22=1011, lot1=lot1)
    elif GetEventFlag(z9) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m20_21_x19(lot1=lot1, z9=z9)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m20_21_x49(z24=15, goods2=60151000):
    """[Lib] Event action: Pass
    z24: Event action
    goods2: Item to be handed: Event item
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z24)
    assert PlayerIsInEventAction(z24) != 0
    """State 2: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z24) != 1
    """State 4: Event action: Pass: Item transfer"""
    # goods:60151000:Human Effigy
    ConsumeItem(goods2, 1)
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z24) != 1
    """State 5: End state"""
    return 0

def talk_m20_21_x50(text5=72509600, z23=0, val2=9):
    """[Lib] Death status_ (pledge cancellation)
    text5: Conversation ID
    z23: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m20_21_x36(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m20_21_x2(text5=text5, z23=z23)

def talk_m20_21_x51(z22=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z22: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_21_x52():
    """Dragon Miko: Conversation (within the Royal Castle)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetEventFlag(100963) != 0 and GetEventFlag(100952) != 0 and GetEventFlag(100966) != 0 and GetEventFlag(100951)
        != 0):
        """State 4: Dragon Miko: After defeating 4 bosses_SubState"""
        assert talk_m20_21_x54()
    else:
        """State 3: Dragon Miko: Before Submission of 4 Boss_SubState"""
        assert talk_m20_21_x53()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m20_21_x53():
    """Dragon Miko: Before Defeating the 4 Boss"""
    """State 0,1: Talk to: 4 bosses before defeating _SubState"""
    # talk:70002000:"Your soul is still frail and pallid..."
    assert talk_m20_21_x45(text7=70002000, z31=0, z32=221020167, z33=0, z34=0)
    """State 2: End state"""
    return 0

def talk_m20_21_x54():
    """Dragon Miko: After defeating 4 bosses"""
    """State 0,1: After defeating the boss: Start"""
    if GetEventFlag(201140) != 0:
        """State 4: Speak: After defeating 4 bosses (single loop) _SubState"""
        # talk:70002250:"End your journey...and mine."
        assert talk_m20_21_x45(text7=70002250, z31=0, z32=221020167, z33=0, z34=0)
    else:
        """State 3: Talk: After defeating 4 bosses_SubState"""
        # talk:70002210:"This castle is isolated."
        assert talk_m20_21_x45(text7=70002210, z31=201140, z32=221020167, z33=0, z34=0)
        """State 2: After destroying the boss: Set generation stop flag"""
        SetEventFlag(102086, 1)
        assert GetEventFlag(102086) != 0
    """State 5: End state"""
    return 0

def talk_m20_21_x55():
    """Dragon Miko: Conversation (before clear)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(201150) != 0:
        """State 5: Talk to: 2_SubState"""
        # talk:70009999:"..."
        assert talk_m20_21_x45(text7=70009999, z31=0, z32=221020177, z33=0, z34=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:70004400:"My journey is already complete."
        assert talk_m20_21_x45(text7=70004400, z31=201150, z32=221020177, z33=221020174, z34=0)
        """State 3: Conversation: Stop generation: Set flag"""
        SetEventFlag(102089, 1)
        assert GetEventFlag(102089) != 0
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m20_21_x56():
    """Chancellor's Spirit: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: The Spirit of the Prime Minister: First conversation_SubState"""
    call = talk_m20_21_x57()
    if call.Done() and GetEventFlag(202307) != 0:
        """State 4: The Spirit of the Chancellor: NPC Menu_SubState"""
        assert talk_m20_21_x58()
    elif call.Done():
        pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m20_21_x57():
    """Prime Minister of the Prime Minister: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(202306) != 0:
        """State 9: Talk to that: 8_SubState"""
        # talk:72110800:"Welcome, visitor..."
        assert talk_m20_21_x0(text10=72110800, z66=202307, z67=0)
    elif GetEventFlag(202305) != 0:
        """State 8: Talk: Part 7_SubState"""
        # talk:72110700:"Is this...some sort of a dream?"
        assert talk_m20_21_x0(text10=72110700, z66=202306, z67=0)
    elif GetEventFlag(202304) != 0:
        """State 7: Talk to: 6_SubState"""
        # talk:72110600:"A peace so deep...it was like..."
        assert talk_m20_21_x0(text10=72110600, z66=202305, z67=0)
    elif GetEventFlag(202303) != 0:
        """State 6: Talk: Part 5_SubState"""
        # talk:72110500:"With the Golems,\nthe king created this castle."
        assert talk_m20_21_x0(text10=72110500, z66=202304, z67=0)
    elif GetEventFlag(202302) != 0:
        """State 5: Talk: 4_SubState"""
        # talk:72110400:"The King had a dear Queen,\na woman of unparalleled beauty."
        assert talk_m20_21_x0(text10=72110400, z66=202303, z67=0)
    elif GetEventFlag(202301) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:72110200:"My Lord made magnificent findings on souls...\nAn accomplishment for the ages..."
        assert talk_m20_21_x0(text10=72110200, z66=202302, z67=0)
    elif GetEventFlag(202300) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:72110100:"You are a guest of our castle.\nI am the Chancellor, Wellager."
        assert talk_m20_21_x0(text10=72110100, z66=202301, z67=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:72110000:"Who are you..."
        assert talk_m20_21_x0(text10=72110000, z66=202300, z67=0)
    """State 10: End state"""
    return 0

def talk_m20_21_x58():
    """The Spirit of the Prime Minister: NPC Menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 3: Menu branch"""
        # goods:63014000:"This one's me" Gesture
        if (ItemCount(63014000, 1, 1, 0) > 1) != 0:
            """State 8: [Lib] Menu start: No gesture _SubState"""
            call = talk_m20_21_x12(z49=0, z50=220, z26=72110001, z51=0)
            if call.Get() == 2:
                """State 7: The Spirit of the Chancellor: Menu Conversation_SubState"""
                Label('L0')
                call = talk_m20_21_x60()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:72111000:"Gone so soon?"
                assert talk_m20_21_x13(text13=72111000, text14=72111000)
        else:
            """State 4: [Lib] Menu start: With gesture_SubState"""
            call = talk_m20_21_x12(z49=0, z50=220, z26=72110000, z51=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 9: [Lib] Menu item: Gesture_SubState"""
                call = talk_m20_21_x40(goods3=63014000, z25=0)
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
    # talk:72111100:"Where has His Royal Highness gone..."
    assert talk_m20_21_x14(text12=72111100)
    Goto('L2')

def talk_m20_21_x59():
    """Moonlight Jun: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetEventFlag(102420) != 1 and GetEventFlag(102436) != 0 and GetEventFlag(104160) != 1 and GetEventFlag(203311)
        != 0):
        """State 5: Equipment transfer (Condition: White Phantom Summon? Achieved times) _SubState"""
        # lot:1743000:Bluemoon Greatsword, talk:74306000:"A man's journey...is never done..."
        assert talk_m20_21_x31(lot4=1743000, z15=102420, text2=74306000, z16=0, z17=221020148)
    elif GetEventFlag(203311) != 0:
        """State 8: Speak: Part 3_SubState"""
        # talk:74301200:"This land is a right mess, eh?"
        call = talk_m20_21_x0(text10=74301200, z66=0, z67=0)
        if call.Done() and GetEventFlag(102422) != 1:
            """State 3: Conversation: Set migration permission flag"""
            SetEventFlag(102422, 1)
            assert GetEventFlag(102422) != 0
            """State 4: Conversation: White Phantom can appear: Set flag"""
            SetEventFlag(102431, 1)
            if GetEventFlag(102431) != 0 and GetEventFlag(102435) != 1:
                """State 9: [Lib] NPC menu: Gesture alone_SubState"""
                Label('L0')
                # goods:63008000:"Joy" Gesture
                assert talk_m20_21_x44(goods3=63008000, z25=102435, z26=74300000, z27=74300001)
            elif GetEventFlag(102431) != 0:
                pass
        elif call.Done() and GetEventFlag(102435) != 1:
            Goto('L0')
        elif call.Done():
            pass
    elif GetEventFlag(203310) != 0:
        """State 7: Talk to: 2_SubState"""
        # talk:74301100:"I journeyed from the distant east\nto perfect my swordsmanship."
        assert talk_m20_21_x0(text10=74301100, z66=203311, z67=0)
    else:
        """State 6: Talk: Part 1_SubState"""
        # talk:74301000:"Ho! Well met, friend."
        assert talk_m20_21_x0(text10=74301000, z66=203310, z67=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 10: End state"""
    return 0

def talk_m20_21_x60():
    """The Spirit of the Prime Minister: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102260) != 1 and GetEventFlag(100972) != 0 and GetEventFlag(104090) != 1:
        """State 9: Equipment transfer (Conditions: Defeat new giant advanced soldier (living)) _ SubState"""
        # lot:1721000:Royal Dirk
        assert talk_m20_21_x33(lot3=1721000, z12=102260, text1=72119800, z13=0, z14=0)
    elif GetEventFlag(202314) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(202310, 0)
        SetEventFlag(202311, 0)
        SetEventFlag(202312, 0)
        SetEventFlag(202313, 0)
        SetEventFlag(202314, 0)
        """State 4: Menu conversation: 3_SubState"""
        Label('L0')
        # talk:72110200:"My Lord made magnificent findings on souls...\nAn accomplishment for the ages..."
        assert talk_m20_21_x1(text1=72110200, z44=202310, z64=-1, z65=0)
    elif GetEventFlag(202313) != 0:
        """State 8: Menu conversation: 7_SubState"""
        # talk:72110700:"Is this...some sort of a dream?"
        assert talk_m20_21_x1(text1=72110700, z44=202314, z64=-1, z65=0)
    elif GetEventFlag(202312) != 0:
        """State 7: Menu conversation: 6_SubState"""
        # talk:72110600:"A peace so deep...it was like..."
        assert talk_m20_21_x1(text1=72110600, z44=202313, z64=-1, z65=0)
    elif GetEventFlag(202311) != 0:
        """State 6: Menu conversation: 5_SubState"""
        # talk:72110500:"With the Golems,\nthe king created this castle."
        assert talk_m20_21_x1(text1=72110500, z44=202312, z64=-1, z65=0)
    elif GetEventFlag(202310) != 0:
        """State 5: Menu conversation: 4_SubState"""
        # talk:72110400:"The King had a dear Queen,\na woman of unparalleled beauty."
        assert talk_m20_21_x1(text1=72110400, z44=202311, z64=-1, z65=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 10: End state"""
    return 0

def talk_m20_21_x61():
    """Queen: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    # goods:50910000:Ashen Mist Heart
    if (ItemCount(50910000, 1, 1, 0) > 1) != 0 and GetEventFlag(201701) != 0:
        """State 5: Queen: Conversation after getting dragon chaos (new) _SubState"""
        assert talk_m20_21_x65()
    # goods:40510000:King's Ring
    elif (ItemCount(40510000, 1, 1, 0) > 1) != 0 and GetEventFlag(201701) != 0:
        """State 4: Queen: Conversation after getting the king's ring_SubState"""
        assert talk_m20_21_x63()
    else:
        """State 3: Queen: Normal conversation_SubState"""
        assert talk_m20_21_x62()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m20_21_x62():
    """Queen: Normal conversation"""
    """State 0,1: Normal conversation: Start"""
    if GetEventFlag(201703) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:70200300:"Brave Undead, seek a fiercer curse."
        assert talk_m20_21_x46(text6=70200300, z28=201702, z29=20219000, z30=45)
    elif GetEventFlag(201701) != 0:
        """State 5: Talk to: 2.1_SubState"""
        # talk:70200220:"We have no need for two rulers..."
        assert talk_m20_21_x46(text6=70200220, z28=201703, z29=20219000, z30=45)
    elif GetEventFlag(201700) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:70200200:"Brave Undead,\nperhaps you are the true monarch."
        assert talk_m20_21_x46(text6=70200200, z28=201701, z29=20219000, z30=45)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:70200000:"You have fought admirably on your journey,\ncursed Undead."
        assert talk_m20_21_x46(text6=70200000, z28=201700, z29=20219000, z30=45)
    """State 6: End state"""
    return 0

def talk_m20_21_x63():
    """Queen: Conversation after obtaining the king's ring"""
    """State 0,1: King's Ring: Start"""
    if GetEventFlag(201710) != 0:
        """State 3: Obtaining a king's ring: Talk: Part 2_SubState"""
        # talk:70200500:"Brave Undead, seek the throne."
        assert talk_m20_21_x46(text6=70200500, z28=201711, z29=20219000, z30=45)
    else:
        """State 2: Obtaining a king's ring: Talk: Part 1_SubState"""
        # talk:70200400:"Brave Undead, vanquisher of King Vendrick,\nand bearer of the symbol of the monarch."
        assert talk_m20_21_x46(text6=70200400, z28=201710, z29=20219000, z30=45)
    """State 4: End state"""
    return 0

def talk_m20_21_x64():
    """Captive Girl: Conversation (Living)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 6: Talk: Part 1_SubState"""
    # talk:76029000:""
    assert talk_m20_21_x0(text10=76029000, z66=0, z67=102580)
    """State 3: Conversation: stop generation"""
    SetEventFlag(104240, 1)
    SetEventFlag(102582, 1)
    assert GetEventFlag(102582) != 0
    """State 4: Conversation: waiting"""
    ExecuteEvent(111325)
    assert EventEnded(111325) != 0 and GetEventFlag(104240) != 0
    """State 5: Conversation: System: End"""
    EndMachine()

def talk_m20_21_x65():
    """Queen: Conversation after getting dragon chaos (new)"""
    """State 0,1: After getting dragon chaos: Start"""
    if GetEventFlag(201720) != 0:
        """State 2: Get Dragon Chaos: Talk: Part 1 (Single Loop) _SubState"""
        # talk:70200700:"Brave Undead, you've met that dragon?\nThat living, breathing sham."
        assert talk_m20_21_x46(text6=70200700, z28=0, z29=20219000, z30=45)
    else:
        """State 3: Get the chaos of the dragon: Talk: Part 1 (new) _SubState"""
        # talk:70200600:"Brave Undead, what did that dragon tell you?"
        assert talk_m20_21_x46(text6=70200600, z28=201720, z29=20219000, z30=45)
    """State 4: End state"""
    return 0

def talk_m20_21_x66():
    """Captive Girl: Conversation (Death)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Talk: Part 1_SubState"""
    # talk:76029000:""
    assert talk_m20_21_x0(text10=76029000, z66=0, z67=102580)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 4: End state"""
    return 0

def talk_m20_21_x67():
    """Waiting for hostility: Dragon maiden (within the castle)"""
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 40)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(221020056) != 1, 221020056, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(221020055) != 1, 221020055, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(221020054) != 1, 221020054, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(221020053) != 1, 221020053, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(221020052) != 1, 221020052, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(221020051) != 1, 221020051, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(221020050) != 1, 221020050, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020166) != 1, 221020166, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020165) != 1, 221020165, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 30 and GetRandomValue(0) < 40) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_21_x1(text1=70009420, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_21_x1(text1=70009410, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_21_x1(text1=70009400, z44=0, z64=-1, z65=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_21_x68():
    """Waiting for hostility: Dragon Maiden (before clear)"""
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 40)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(221020066) != 1, 221020066, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(221020065) != 1, 221020065, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(221020064) != 1, 221020064, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(221020063) != 1, 221020063, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(221020062) != 1, 221020062, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(221020061) != 1, 221020061, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(221020060) != 1, 221020060, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020176) != 1, 221020176, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020175) != 1, 221020175, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 30 and GetRandomValue(0) < 40) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_21_x1(text1=70009420, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_21_x1(text1=70009410, z44=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_21_x1(text1=70009400, z44=0, z64=-1, z65=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_21_x69():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(221000006) != 0 and PlayerInPoint(10003000) != 0:
        """State 4: Ann Deal postwar timer"""
        assert (GetStateTime() > 4.5) != 0
        """State 5: [Lib] Conversation: Conversation after Defeating Anne Deal_SubState"""
        # talk:69201200:"I lost everything, but remained here, patiently."
        assert talk_m20_21_x1(text1=69201200, z44=208030, z64=50, z65=0)
    elif GetEventFlag(208031) != 1 and GetEventFlag(221000001) != 0 and PlayerInPoint(10003000) != 0:
        """State 3: Timer before the Battle of Anne Deal"""
        assert (GetStateTime() > 4.5) != 0
        """State 6: [Lib] Conversation: Conversation before the Battle of Anne Deal_SubState"""
        # talk:69201400:"Many monarchs have come and gone."
        assert talk_m20_21_x1(text1=69201400, z44=208031, z64=50, z65=0)
    """State 2,7: End state"""
    return 0

def talk_m20_21_4100000():
    """Andyel"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(208030) != 0:
            break
        else:
            """State 3: Anne Deal_SubState"""
            assert talk_m20_21_x69()
    """State 2: Conversation: System termination"""
    EndMachine()

