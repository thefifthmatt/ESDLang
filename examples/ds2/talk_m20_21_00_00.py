# -*- coding: utf-8 -*-
def talk_m20_21_7000():
    """Dragon Miko (within the castle)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        Label('L0')
        SetEventFlag(221020167, 1)
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(flag19=103520, flag20=104020, flag21=221020161)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=70009200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L1')
                call = talk_m20_21_x6(flag18=221020162, text15=70009500, text16=70009500, z35=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L2')
                    talk_m20_21_x7(text18=70009600, z37=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L2')
        elif call.Get() == 0:
            while True:
                """State 10: Dragon Miko: Conversation (within the Royal Castle) _SubState"""
                call = talk_m20_21_x52()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 11: Waiting for hostility: Dragon Maiden (in the Royal Castle) _SubState"""
                    Label('L3')
                    call = talk_m20_21_x67()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L2')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 5: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(flag24=103520, text23=70009100, z38=0, z39=0)
                        if call.Done():
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L2')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(221020056) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(221020055) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(221020054) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(221020053) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(221020052) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(221020051) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(221020050) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020166) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020165) != 1:
                    Goto('L3')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=70009300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 3: Conversation: Delete key guide"""
    DeleteKeyGuideArea()
    assert GetEventFlag(221020167) != 1
    Goto('L0')

def talk_m20_21_7001():
    """Dragon Miko (before clear)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        Label('L0')
        SetEventFlag(221020174, 1)
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m20_21_x9(flag19=103520, flag20=104020, flag21=221020171)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=70009200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L1')
                call = talk_m20_21_x6(flag18=221020172, text15=70009500, text16=70009500, z35=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L2')
                    talk_m20_21_x7(text18=70009600, z37=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L2')
        elif call.Get() == 0:
            while True:
                """State 10: Dragon Miko: Conversation (before clear) _SubState"""
                call = talk_m20_21_x55()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 11: Waiting for hostility: Dragon Miko (before clear) _SubState"""
                    Label('L3')
                    call = talk_m20_21_x68()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L2')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 5: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(flag24=103520, text23=70009100, z38=0, z39=0)
                        if call.Done():
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L2')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(221020066) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(221020065) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(221020064) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(221020063) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(221020062) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(221020061) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(221020060) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(221020176) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(221020175) != 1:
                    Goto('L3')
        """State 9: [Lib] Killing state_SubState"""
        talk_m20_21_x8(text17=70009300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 3: Conversation: Delete key guide"""
    DeleteKeyGuideArea()
    assert GetEventFlag(221020177) != 1
    Goto('L0')

def talk_m20_21_7030():
    """Queen"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            """State 5: [Lib] Event: Branch_SubState"""
            call = talk_m20_21_x9(flag19=103540, flag20=104040, flag21=221020181)
            if call.Get() == 1:
                """State 6: [Lib] Reunion hostility_SubState"""
                talk_m20_21_x3(text8=70209200, z24=0, z25=20, z26=80)
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
                                          flag22=221020185, flag23=221020186)
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
    Quit()

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
        call = talk_m20_21_x9(flag19=103590, flag20=104090, flag21=221020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=72119200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(flag18=221020122, text15=72119500, text16=72119500, z35=72119500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=72119600, z37=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
            """State 9: [Lib] Killing state_SubState"""
            Label('L2')
            talk_m20_21_x8(text17=72119300, z36=0)
            Quit()
        elif call.Get() == 0:
            pass
        """State 10: Prime Minister: Conversation_SubState"""
        Label('L3')
        assert talk_m20_21_x56()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: [Lib] First adversification_SubState"""
    call = talk_m20_21_x4(flag24=103590, text23=72119100, z38=0, z39=0)
    if call.Done():
        Goto('L0')
    elif KilledPlayer() != 0:
        Goto('L2')
    elif (HpValue() > 1) != 1:
        Goto('L1')
    """State 6: [Lib] Hostile waiting_SubState"""
    call = talk_m20_21_x5(text19=72119400, text20=72119400, text21=72119400, text22=72119400, flag22=221020125,
                          flag23=221020126)
    if call.Done():
        Goto('L3')
    elif KilledPlayer() != 0:
        Goto('L2')
    elif (HpValue() > 1) != 1:
        Goto('L1')

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
        call = talk_m20_21_x9(flag19=103623, flag20=104120, flag21=221020101)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=72509200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(flag18=221020102, text15=72509500, text16=72509500, z35=72509500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 11: [Lib] Death state_ (pledge cancellation) _SubState"""
                    Label('L1')
                    talk_m20_21_x50(text5=72509600, z14=0, val2=9)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Pilgrim in Shenzhen: Conversation_SubState"""
                call = talk_m20_21_x22(flag1=221020104, flag2=102326, z1=221020107, z2=20213000, flag3=102332,
                                       z3=60, flag4=102316, z4=221020109)
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
                                          flag22=221020105, flag23=221020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 5: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m20_21_x15(flag17=103620, text9=72509100, z27=0, val3=9, z28=200908,
                                               z29=103623)
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
        talk_m20_21_x8(text17=72509300, z36=0)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()
    Quit()

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
        call = talk_m20_21_x9(flag19=103662, flag20=104160, flag21=221020141)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=74309200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(flag18=221020142, text15=74309500, text16=74309500, z35=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=74309600, z37=104162)
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
                                          flag22=221020145, flag23=221020146)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(flag24=103660, text23=74309100, z38=0, z39=103662)
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
        talk_m20_21_x8(text17=74309300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

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
        call = talk_m20_21_x9(flag19=103740, flag20=104240, flag21=221020151)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m20_21_x3(text8=76029200, z24=0, z25=20, z26=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m20_21_x6(flag18=221020152, text15=76029500, text16=76029500, z35=76029500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m20_21_x7(text18=76029600, z37=0)
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
                                          flag22=221020154, flag23=221020155)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m20_21_x4(flag24=103740, text23=76029100, z38=0, z39=0)
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
        talk_m20_21_x8(text17=76029300, z36=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m20_21_x0(text10=_, z42=_, z43=_):
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

def talk_m20_21_x1(text1=_, z27=_, z40=_, z41=0):
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

def talk_m20_21_x2(text5=_, z14=_):
    """[Lib] Conversation: Event end
    text5: Conversation ID
    z14: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text5, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z14, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m20_21_x3(text8=_, z24=0, z25=20, z26=80):
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
    assert talk_m20_21_x37(text8=text8, z24=z24, z25=z25, z26=z26)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m20_21_x4(flag24=_, text23=_, z38=0, z39=_):
    """[Lib] First hostility
    flag24: Hostile: Global event flag
    text23: Conversation ID
    z38: Conversation flag
    z39: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag24, 1)
    SetEventFlag(z39, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag24) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m20_21_x1(text1=text23, z27=z38, z40=-1, z41=0)
    """State 4: First hostility: end"""
    return 0

def talk_m20_21_x5(text19=_, text20=_, text21=_, text22=_, flag22=_, flag23=_):
    """[Lib] Hostile waiting
    text19: Conversation ID: 1 attacked
    text20: Conversation ID: Attacked 2
    text21: Conversation ID: 3 attacked
    text22: Conversation ID: 4 attacked
    flag22: No use: Area and other flags
    flag23: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag23) != 1, flag23, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag22) != 1, flag22, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m20_21_x1(text1=text22, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m20_21_x1(text1=text21, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_21_x1(text1=text20, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_21_x1(text1=text19, z27=0, z40=-1, z41=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m20_21_x6(flag18=_, text15=_, text16=_, z35=_):
    """[Lib] Hostile state
    flag18: Area and other flags: HP decreased
    text15: Conversation ID: HP drop 1
    text16: Conversation ID: HP drop 2
    z35: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag18) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m20_21_x10(text15=text15, flag18=flag18)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m20_21_x10(text15=text16, flag18=flag18)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m20_21_x10(text15=text16, flag18=flag18)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m20_21_x7(text18=_, z37=_):
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
    talk_m20_21_x2(text5=text18, z14=z37)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m20_21_x8(text17=_, z36=0):
    """[Lib] Murder status
    text17: Conversation ID
    z36: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m20_21_x2(text5=text17, z14=z36)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m20_21_x9(flag19=_, flag20=_, flag21=_):
    """[Lib] Event: Branch
    flag19: Hostile flag
    flag20: death flag
    flag21: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag20) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag21) != 0
    elif GetEventFlag(flag19) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m20_21_x10(text15=_, flag18=_):
    """[Lib] Conversation: HP drop
    text15: Conversation ID
    flag18: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text15, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag18, 1)
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

def talk_m20_21_x12(z32=0, z33=220, z16=_, z34=0):
    """[Lib] Menu start: General purpose
    z32: Camera parameter ID
    z33: Target Damipoly ID
    z16: NPC event parameter ID
    z34: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z34, z32, z33, z16)
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

def talk_m20_21_x13(text13=_, text14=_):
    """[Lib] Menu exit: General purpose
    text13: Conversation ID (at the time of purchase)
    text14: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m20_21_x1(text1=text13, z27=0, z40=-1, z41=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m20_21_x1(text1=text14, z27=0, z40=-1, z41=0)
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
    assert talk_m20_21_x1(text1=text12, z27=0, z40=-1, z41=0)
    """State 4: End state"""
    return 0

def talk_m20_21_x15(flag17=103620, text9=72509100, z27=0, val3=9, z28=200908, z29=103623):
    """[Lib] First hostility _ (pledge cancellation)
    flag17: Hostile: Global event flag
    text9: Conversation ID
    z27: Conversation flag
    val3: Cancellation pledge name
    z28: Pledge cancellation: Global conversation flag
    z29: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag17, 1)
    SetEventFlag(z29, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag17) != 0 and GetEventFlag(103999) != 0
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
    assert talk_m20_21_x1(text1=text9, z27=z27, z40=-1, z41=0)
    """State 6: First hostility: end"""
    return 0

def talk_m20_21_x16(text4=_, z11=0, lot6=_, flag9=_, z12=218, z3=60):
    """[Lib] Conversation: Pledge ranking
    text4: Ranking: Conversation ID
    z11: Ranking: Conversation flag
    lot6: Item lottery
    flag9: Ranking transfer: Global event flag
    z12: Previous rank: Global variable
    z3: Current rank: Area variable
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
    SetEventFlag(z11, 1)
    if CanGetItemLot(lot6, 1) != 1 and GetEventFlag(flag9) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z13=1011, lot1=lot6)
    elif GetEventFlag(flag9) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m20_21_x19(lot1=lot6, flag5=flag9)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z12, GetAreaVariable(z3))
    """State 11: End state"""
    return 0

def talk_m20_21_x17(val1=9, z5=8, lot2=0, flag6=0, action1=1338, action2=1348, z4=221020109):
    """[Lib] Menu item: Make a pledge
    val1: Pledge name
    z5: Event action
    lot2: Item lottery ID
    flag6: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m20_21_x18(action5=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m20_21_x41(val1=val1, z5=z5, lot2=lot2, flag6=flag6, action1=action1, action2=action2,
                               z4=z4)
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

def talk_m20_21_x19(lot1=_, flag5=_):
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

def talk_m20_21_x20(flag1=221020104, text10=72505100, text11=72505000):
    """[Lib] Conversation: Greeting: Single
    flag1: Area other flag: Contact flag
    text10: Text ID: Talk to_continuous
    text11: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(flag1) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m20_21_x0(text10=text10, z42=0, z43=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m20_21_x0(text10=text11, z42=0, z43=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(flag1, 1)
    """State 5: End state"""
    return 0

def talk_m20_21_x21(lot5=1725000, z10=102320, text3=72506300):
    """[Lib] Equipment transfer: Mes⇒Item
    lot5: Item lottery ID
    z10: Global event flag
    text3: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m20_21_x1(text1=text3, z27=0, z40=-1, z41=0)
    # lot:1725000:Dragon Chime
    if call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z13=1011, lot1=lot5)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m20_21_x19(lot1=lot5, flag5=z10)
    """State 5: End state"""
    return 0

def talk_m20_21_x22(flag1=221020104, flag2=102326, z1=221020107, z2=20213000, flag3=102332, z3=60, flag4=102316,
                    z4=221020109):
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
        assert talk_m20_21_x23(flag1=flag1, z3=z3)
        """State 4: [Lib] Pilgrim in Shenzhen: Menu_SubState"""
        assert talk_m20_21_x24(flag2=flag2, z1=z1, z2=z2, z3=z3, z4=z4)
    elif GetEventFlag(104120) != 0:
        """State 6: [Lib] Conversation: General purpose_SubState"""
        assert talk_m20_21_x0(text10=72509000, z42=0, z43=0)
    else:
        """State 5: [Lib] Pilgrim in Shenzhen: First conversation_SubState"""
        assert talk_m20_21_x27(flag1=flag1, flag2=flag2, z1=z1, z2=z2, flag3=flag3, flag4=flag4, z4=z4)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m20_21_x23(flag1=221020104, z3=60):
    """[Lib] Pilgrim in Shenzhen: greeting conversation
    flag1: Contact: Area and other flags
    z3: Current pledge rank: Area variable
    """
    """State 0,1: Greeting: Start"""
    if (GetPlayerCovenant() == 9) != 0 and GetEventFlag(102319) != 1:
        """State 8: When pledge ring is not acquired: Insurance_SubState"""
        # lot:2006000:Abyss Seal
        assert talk_m20_21_x48(lot1=2006000, flag5=102319)
        """State 3: [Lib] Conversation: Greeting: Single _SubState"""
        Label('L0')
        # talk:72505000:"Young Undead, do you expect me to just keel over?"
        assert talk_m20_21_x20(flag1=flag1, text10=72505100, text11=72505000)
    else:
        """State 4: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m20_21_x43(z22=9, z3=z3, z23=218, flag14=102337, flag15=102338, flag16=102339)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z3) > 1) != 0 and GetEventFlag(102337) != 1:
                """State 5: Conversation: Pledge Ranking 1_SubState"""
                # talk:72506000:"Young Undead, my work is done...", lot:2006011:Resonant Soul
                assert talk_m20_21_x16(text4=72506000, z11=0, lot6=2006011, flag9=102337, z12=218, z3=z3)
            elif (GetAreaVariable(z3) > 2) != 0 and GetEventFlag(102338) != 1:
                """State 6: Conversation: Pledge Ranking 2_SubState"""
                # lot:2006012:Great Resonant Soul
                assert talk_m20_21_x16(text4=72506100, z11=0, lot6=2006012, flag9=102338, z12=218, z3=z3)
            elif (GetAreaVariable(z3) > 3) != 0 and GetEventFlag(102339) != 1:
                """State 7: Conversation: Pledge Ranking 3_SubState"""
                # lot:2006013:Climax
                assert talk_m20_21_x16(text4=72506200, z11=0, lot6=2006013, flag9=102339, z12=218, z3=z3)
            else:
                Goto('L0')
        elif call.Get() == 0:
            Goto('L0')
    """State 9: End state"""
    return 0

def talk_m20_21_x24(flag2=102326, z1=221020107, z2=20213000, z3=60, z4=221020109):
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
            call = talk_m20_21_x12(z32=0, z33=220, z16=72500001, z34=0)
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
                call = talk_m20_21_x17(val1=9, z5=8, lot2=0, flag6=0, action1=1338, action2=1348, z4=z4)
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
            call = talk_m20_21_x12(z32=0, z33=220, z16=72500000, z34=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 6:
                Goto('L1')
            elif call.Get() == 8:
                """State 7: [Lib] Pilgrim in Shenzhen: menu passing _SubState"""
                # goods:60151000:Human Effigy
                call = talk_m20_21_x25(goods1=60151000, flag2=flag2, z1=z1, z2=z2)
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

def talk_m20_21_x25(goods1=60151000, flag2=102326, z1=221020107, z2=20213000):
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
        assert talk_m20_21_x18(action5=1213)
    else:
        """State 5: Menu to pass ○○: Conversation to pass_SubState"""
        assert talk_m20_21_x1(text1=72505200, z27=0, z40=-1, z41=0)
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
            assert talk_m20_21_x49(z15=15, goods2=60151000)
            """State 3: 3rd encounter: Magic square: Open"""
            SetEventFlag(z1, 1)
            """State 4,6: Menu to pass ○○: Conversation to pass: YES_SubState"""
            assert talk_m20_21_x1(text1=72505300, z27=0, z40=-1, z41=0)
            Goto('L0')
        """State 7: Menu to pass ○○: Conversation to pass: NO_SubState"""
        assert talk_m20_21_x1(text1=72505400, z27=0, z40=-1, z41=0)
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
        assert talk_m20_21_x21(lot5=1725000, z10=102320, text3=72506300)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        assert talk_m20_21_x1(text1=72505500, z27=0, z40=-1, z41=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m20_21_x27(flag1=221020104, flag2=102326, z1=221020107, z2=20213000, flag3=102332, flag4=102316,
                    z4=221020109):
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
        assert talk_m20_21_x30(flag2=flag2, z1=z1, z2=z2, flag3=flag3, z4=z4)
    elif GetEventFlag(202751) != 0 and GetEventFlag(flag3) != 1:
        Goto('L0')
    elif GetEventFlag(202751) != 0 and GetEventFlag(flag3) != 0:
        """State 3: [Lib] Pilgrim in Shenzhen: second encounter _SubState"""
        Label('L1')
        assert talk_m20_21_x29(flag4=flag4, flag3=flag3)
    elif GetEventFlag(202750) != 0 and GetEventFlag(flag3) != 1:
        Goto('L1')
    else:
        """State 2: [Lib] Pilgrims in Shenzhen: first encounter conversation_SubState"""
        assert talk_m20_21_x28(flag4=flag4, flag3=flag3)
    """State 5: End state"""
    return 0

def talk_m20_21_x28(flag4=102316, flag3=102332):
    """[Lib] Pilgrim in Shenzhen: first encounter
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    """
    """State 0,1: First encounter conversation: Start"""
    if GetEventFlag(202750) != 0:
        """State 4: Talk: 1st encounter: Loop_SubState"""
        # talk:72500100:"The Dark is still nascent within you.\nMay the Dark shine your way..."
        assert talk_m20_21_x0(text10=72500100, z42=0, z43=0)
    else:
        """State 3: Talk: 1st encounter_SubState"""
        # talk:72500000:"Ahh, look how far this Undead has wandered."
        call = talk_m20_21_x0(text10=72500000, z42=202750, z43=0)
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

def talk_m20_21_x29(flag4=102316, flag3=102332):
    """[Lib] Pilgrim in Shenzhen: second encounter
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    """
    """State 0,1: Encounter 2nd conversation: Start"""
    if GetEventFlag(202751) != 0:
        """State 4: Talk: Second encounter: Loop_SubState"""
        # talk:72500300:"May we meet again, somewhere, some time..."
        assert talk_m20_21_x0(text10=72500300, z42=0, z43=0)
    else:
        """State 3: Speak: Second encounter_SubState"""
        # talk:72500200:"Young Undead, don't let this curse weigh upon you."
        call = talk_m20_21_x0(text10=72500200, z42=202751, z43=0)
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

def talk_m20_21_x30(flag2=102326, z1=221020107, z2=20213000, flag3=102332, z4=221020109):
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
        assert talk_m20_21_x0(text10=72500900, z42=0, z43=0)
    else:
        """State 5: Talk: 3rd encounter_SubState"""
        # talk:72500400:"We meet again, young Undead."
        assert talk_m20_21_x0(text10=72500400, z42=202752, z43=0)
    """State 10: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:2006000:Abyss Seal, action:1338:"Join the Pilgrims of Dark covenant?", action:1348:"Abandon your covenant and\njoin the Pilgrims of Dark?"
    call = talk_m20_21_x41(val1=9, z5=8, lot2=2006000, flag6=102319, action1=1338, action2=1348, z4=z4)
    if call.Get() == 1:
        """State 2: 3rd encounter: After signing the pledge: Set flag"""
        SetEventFlag(102321, 1)
        assert GetEventFlag(102321) != 0
        """State 3: 3rd encounter: Magic square: Open"""
        SetEventFlag(z1, 1)
        """State 4,9: Speak: 3rd encounter: YES / NO dialog: YES_SubState"""
        # talk:72500500:"There you are, you are now a Pilgrim of Dark."
        assert talk_m20_21_x1(text1=72500500, z27=0, z40=-1, z41=0)
    elif call.Get() == 0 and GetEventFlag(202753) != 0:
        """State 8: Speak: 3rd encounter: YES / NO dialog: NO: Loop: YES / NO dialog: NO_SubState"""
        # talk:72501000:"Then choose your own path."
        assert talk_m20_21_x1(text1=72501000, z27=0, z40=-1, z41=0)
    elif call.Get() == 0:
        """State 7: Speak: 3rd encounter: YES / NO dialog: NO_SubState"""
        # talk:72500800:"Hmm... Perhaps I was wrong."
        assert talk_m20_21_x1(text1=72500800, z27=202753, z40=-1, z41=0)
    """State 11: End state"""
    return 0

def talk_m20_21_x31(lot4=_, flag8=_, text2=_, z8=0, z9=_):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot4: Item lottery ID
    flag8: Item transfer: Global event flag
    text2: Conversation ID
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
    call = talk_m20_21_x1(text1=text2, z27=0, z40=-1, z41=0)
    if call.Done() and GetEventFlag(flag8) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z8, 1)
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z13=1011, lot1=lot4)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_21_x32(lot3=lot4, flag7=flag8, z6=z8, z7=z9, z30=0, z31=0)
    """State 9: End state"""
    return 0

def talk_m20_21_x32(lot3=_, flag7=_, z6=0, z7=_, z30=0, z31=0):
    """[Lib] Item acquisition dialog: Conversation
    lot3: Item lottery ID
    flag7: Item transfer: Global event flag
    z6: Conversation: Global conversation flag
    z7: Trophy acquisition: Area and other flags
    z30: Emigration permission: Global event flag
    z31: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z31, 1)
    SetEventFlag(z30, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(z6, 1)
    SetEventFlag(flag7, 1)
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m20_21_x33(lot3=1721000, flag7=102260, text1=72119800, z6=0, z7=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot3: Item lottery ID
    flag7: Item transfer: Global event flag
    text1: Conversation ID
    z6: Conversation: Global conversation flag
    z7: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m20_21_x1(text1=text1, z27=0, z40=-1, z41=0)
    if call.Done() and GetEventFlag(flag7) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z6, 1)
    # lot:1721000:Royal Dirk
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m20_21_x51(z13=1011, lot1=lot3)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m20_21_x32(lot3=lot3, flag7=flag7, z6=z6, z7=z7, z30=0, z31=0)
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

def talk_m20_21_x37(text8=_, z24=0, z25=20, z26=80):
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

def talk_m20_21_x40(goods3=_, flag10=_):
    """[Lib] Menu item: Gesture
    goods3: Gesture: Item ID
    flag10: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m20_21_x47(goods3=goods3, flag10=flag10)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m20_21_x41(val1=9, z5=8, lot2=_, flag6=_, action1=1338, action2=1348, z4=221020109):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z5: Event action
    lot2: Item lottery ID
    flag6: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z4, 1)
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
            assert talk_m20_21_x42(z5=z5, val1=val1, lot2=lot2, flag6=flag6) and ItemAwardDisplay() != 1
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

def talk_m20_21_x42(z5=8, val1=9, lot2=_, flag6=_):
    """[Lib] Event action: Pledge
    z5: Event action
    val1: Pledge type
    lot2: Item lottery ID
    flag6: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z5)
    assert PlayerIsInEventAction(z5) != 0
    """State 3: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z5) != 1 and CanGetItemLot(lot2, 1) != 1 and GetEventFlag(flag6) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot2, 1) != 1 and GetEventFlag(flag6) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m20_21_x51(z13=1011, lot1=lot2)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z5) != 1 and GetEventFlag(flag6) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z5) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(flag6, 1)
        AwardItem(lot2, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z5) != 1
    """State 8: End state"""
    return 0

def talk_m20_21_x43(z22=9, z3=60, z23=218, flag14=102337, flag15=102338, flag16=102339):
    """[Lib] Pledge: Rank up: Conversation: 1
    z22: Pledge: Pledge type
    z3: Current rank: Area variable
    z23: Previous rank: Global variable
    flag14: Ranking 1: Item transfer: Global event flag
    flag15: Ranking 2: Item transfer: Global event flag
    flag16: Ranking 3: Item transfer: Global event flag
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
    elif GetEventFlag(flag14) != 1 and (GetGlobalVariable(z23) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(flag15) != 1 and (GetGlobalVariable(z23) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(flag16) != 1 and (GetGlobalVariable(z23) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m20_21_x44(goods3=63008000, flag10=102435, z16=74300000, z17=74300001):
    """[Lib] NPC menu: Gesture alone
    goods3: Item: Event item
    flag10: Item transfer: Global event flag
    z16: NPC menu: With gesture
    z17: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(flag10) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            # goods:63008000:"Joy" Gesture
            if (ItemCount(goods3, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m20_21_x12(z32=0, z33=220, z16=z16, z34=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m20_21_x40(goods3=goods3, flag10=flag10)
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
        call = talk_m20_21_x12(z32=0, z33=220, z16=z17, z34=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m20_21_x45(text7=_, z21=_, flag11=_, flag12=_, flag13=0):
    """[Lib] Conversation: Canceling startup state
    text7: Conversation ID
    z21: Conversation flag
    flag11: Activation state release: Area and other flags
    flag12: Rock sitting 1: Poke your cheek with your hand
    flag13: Extend both hands back
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 10: Conversation: Cancel start state: Branch"""
    if GetEventFlag(flag11) != 0:
        """State 8: Conversation: Activation state release: Second time"""
        Label('L0')
        DeleteKeyGuideArea()
        SetEventFlag(flag11, 1)
    elif GetEventFlag(flag12) != 1 and GetEventFlag(flag13) != 1:
        Goto('L0')
    else:
        """State 7: Conversation: Activation state release: First use"""
        DeleteKeyGuideArea()
        SetEventFlag(flag11, 1)
        assert GetEventFlag(flag11) != 0
        """State 9: Conversation: Release hood: Wait"""
        KeyGuideTemporarilyInvalidIf(GetEventFlag(flag12) != 0, 3.5)
        KeyGuideTemporarilyInvalidIf(GetEventFlag(flag13) != 0, 3.5)
        assert (GetStateTime() > GetRandomValueForStateTime(3, 3)) != 0
    """State 4: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z21, 1)
    """State 11: Conversation: End"""
    return 0

def talk_m20_21_x46(text6=_, z18=_, z19=20219000, z20=45):
    """[Lib] Conversation: For unique key guide
    text6: Conversation ID
    z18: Conversation flag
    z19: Key guide parameters
    z20: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z19)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text6, GetCommonEventParamDecimal(7), z20)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m20_21_x47(goods3=_, flag10=_):
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

def talk_m20_21_x48(lot1=2006000, flag5=102319):
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
        assert talk_m20_21_x51(z13=1011, lot1=lot1)
    elif GetEventFlag(flag5) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m20_21_x19(lot1=lot1, flag5=flag5)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m20_21_x49(z15=15, goods2=60151000):
    """[Lib] Event action: Pass
    z15: Event action
    goods2: Item to be handed: Event item
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z15)
    assert PlayerIsInEventAction(z15) != 0
    """State 2: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z15) != 1
    """State 4: Event action: Pass: Item transfer"""
    # goods:60151000:Human Effigy
    ConsumeItem(goods2, 1)
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z15) != 1
    """State 5: End state"""
    return 0

def talk_m20_21_x50(text5=72509600, z14=0, val2=9):
    """[Lib] Death status_ (pledge cancellation)
    text5: Conversation ID
    z14: Global: death flag
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
    talk_m20_21_x2(text5=text5, z14=z14)
    Quit()
    """Unused"""
    """State 5: End state"""
    return 0

def talk_m20_21_x51(z13=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z13: Text ID
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
    assert talk_m20_21_x45(text7=70002000, z21=0, flag11=221020167, flag12=0, flag13=0)
    """State 2: End state"""
    return 0

def talk_m20_21_x54():
    """Dragon Miko: After defeating 4 bosses"""
    """State 0,1: After defeating the boss: Start"""
    if GetEventFlag(201140) != 0:
        """State 4: Speak: After defeating 4 bosses (single loop) _SubState"""
        # talk:70002250:"End your journey...and mine."
        assert talk_m20_21_x45(text7=70002250, z21=0, flag11=221020167, flag12=0, flag13=0)
    else:
        """State 3: Talk: After defeating 4 bosses_SubState"""
        # talk:70002210:"This castle is isolated."
        assert talk_m20_21_x45(text7=70002210, z21=201140, flag11=221020167, flag12=0, flag13=0)
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
        assert talk_m20_21_x45(text7=70009999, z21=0, flag11=221020177, flag12=0, flag13=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:70004400:"My journey is already complete."
        assert talk_m20_21_x45(text7=70004400, z21=201150, flag11=221020177, flag12=221020174, flag13=0)
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
        assert talk_m20_21_x0(text10=72110800, z42=202307, z43=0)
    elif GetEventFlag(202305) != 0:
        """State 8: Talk: Part 7_SubState"""
        # talk:72110700:"Is this...some sort of a dream?"
        assert talk_m20_21_x0(text10=72110700, z42=202306, z43=0)
    elif GetEventFlag(202304) != 0:
        """State 7: Talk to: 6_SubState"""
        # talk:72110600:"A peace so deep...it was like..."
        assert talk_m20_21_x0(text10=72110600, z42=202305, z43=0)
    elif GetEventFlag(202303) != 0:
        """State 6: Talk: Part 5_SubState"""
        # talk:72110500:"With the Golems,\nthe king created this castle."
        assert talk_m20_21_x0(text10=72110500, z42=202304, z43=0)
    elif GetEventFlag(202302) != 0:
        """State 5: Talk: 4_SubState"""
        # talk:72110400:"The King had a dear Queen,\na woman of unparalleled beauty."
        assert talk_m20_21_x0(text10=72110400, z42=202303, z43=0)
    elif GetEventFlag(202301) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:72110200:"My Lord made magnificent findings on souls...\nAn accomplishment for the ages..."
        assert talk_m20_21_x0(text10=72110200, z42=202302, z43=0)
    elif GetEventFlag(202300) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:72110100:"You are a guest of our castle.\nI am the Chancellor, Wellager."
        assert talk_m20_21_x0(text10=72110100, z42=202301, z43=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:72110000:"Who are you..."
        assert talk_m20_21_x0(text10=72110000, z42=202300, z43=0)
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
            call = talk_m20_21_x12(z32=0, z33=220, z16=72110001, z34=0)
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
            call = talk_m20_21_x12(z32=0, z33=220, z16=72110000, z34=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 9: [Lib] Menu item: Gesture_SubState"""
                call = talk_m20_21_x40(goods3=63014000, flag10=0)
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
        assert talk_m20_21_x31(lot4=1743000, flag8=102420, text2=74306000, z8=0, z9=221020148)
    elif GetEventFlag(203311) != 0:
        """State 8: Speak: Part 3_SubState"""
        # talk:74301200:"This land is a right mess, eh?"
        call = talk_m20_21_x0(text10=74301200, z42=0, z43=0)
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
                assert talk_m20_21_x44(goods3=63008000, flag10=102435, z16=74300000, z17=74300001)
            elif GetEventFlag(102431) != 0:
                pass
        elif call.Done() and GetEventFlag(102435) != 1:
            Goto('L0')
        elif call.Done():
            pass
    elif GetEventFlag(203310) != 0:
        """State 7: Talk to: 2_SubState"""
        # talk:74301100:"I journeyed from the distant east\nto perfect my swordsmanship."
        assert talk_m20_21_x0(text10=74301100, z42=203311, z43=0)
    else:
        """State 6: Talk: Part 1_SubState"""
        # talk:74301000:"Ho! Well met, friend."
        assert talk_m20_21_x0(text10=74301000, z42=203310, z43=0)
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
        assert talk_m20_21_x33(lot3=1721000, flag7=102260, text1=72119800, z6=0, z7=0)
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
        assert talk_m20_21_x1(text1=72110200, z27=202310, z40=-1, z41=0)
    elif GetEventFlag(202313) != 0:
        """State 8: Menu conversation: 7_SubState"""
        # talk:72110700:"Is this...some sort of a dream?"
        assert talk_m20_21_x1(text1=72110700, z27=202314, z40=-1, z41=0)
    elif GetEventFlag(202312) != 0:
        """State 7: Menu conversation: 6_SubState"""
        # talk:72110600:"A peace so deep...it was like..."
        assert talk_m20_21_x1(text1=72110600, z27=202313, z40=-1, z41=0)
    elif GetEventFlag(202311) != 0:
        """State 6: Menu conversation: 5_SubState"""
        # talk:72110500:"With the Golems,\nthe king created this castle."
        assert talk_m20_21_x1(text1=72110500, z27=202312, z40=-1, z41=0)
    elif GetEventFlag(202310) != 0:
        """State 5: Menu conversation: 4_SubState"""
        # talk:72110400:"The King had a dear Queen,\na woman of unparalleled beauty."
        assert talk_m20_21_x1(text1=72110400, z27=202311, z40=-1, z41=0)
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
        assert talk_m20_21_x46(text6=70200300, z18=201702, z19=20219000, z20=45)
    elif GetEventFlag(201701) != 0:
        """State 5: Talk to: 2.1_SubState"""
        # talk:70200220:"We have no need for two rulers..."
        assert talk_m20_21_x46(text6=70200220, z18=201703, z19=20219000, z20=45)
    elif GetEventFlag(201700) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:70200200:"Brave Undead,\nperhaps you are the true monarch."
        assert talk_m20_21_x46(text6=70200200, z18=201701, z19=20219000, z20=45)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:70200000:"You have fought admirably on your journey,\ncursed Undead."
        assert talk_m20_21_x46(text6=70200000, z18=201700, z19=20219000, z20=45)
    """State 6: End state"""
    return 0

def talk_m20_21_x63():
    """Queen: Conversation after obtaining the king's ring"""
    """State 0,1: King's Ring: Start"""
    if GetEventFlag(201710) != 0:
        """State 3: Obtaining a king's ring: Talk: Part 2_SubState"""
        # talk:70200500:"Brave Undead, seek the throne."
        assert talk_m20_21_x46(text6=70200500, z18=201711, z19=20219000, z20=45)
    else:
        """State 2: Obtaining a king's ring: Talk: Part 1_SubState"""
        # talk:70200400:"Brave Undead, vanquisher of King Vendrick,\nand bearer of the symbol of the monarch."
        assert talk_m20_21_x46(text6=70200400, z18=201710, z19=20219000, z20=45)
    """State 4: End state"""
    return 0

def talk_m20_21_x64():
    """Captive Girl: Conversation (Living)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 6: Talk: Part 1_SubState"""
    # talk:76029000:""
    assert talk_m20_21_x0(text10=76029000, z42=0, z43=102580)
    """State 3: Conversation: stop generation"""
    SetEventFlag(104240, 1)
    SetEventFlag(102582, 1)
    assert GetEventFlag(102582) != 0
    """State 4: Conversation: waiting"""
    ExecuteEvent(111325)
    assert EventEnded(111325) != 0 and GetEventFlag(104240) != 0
    """State 5: Conversation: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: Conversation: End"""
    Label('L0')
    ClearNpcMenuResults()
    Goto('L1')
    """State 7: Speak: Part 2 (Item Transfer) _SubState"""
    # lot:1760200:Ring of the Dead, talk:76020300:"Ahh...Ah..."
    assert talk_m20_21_x31(lot4=1760200, flag8=102581, text2=76020300, z8=0, z9=0)
    Goto('L0')
    """State 8: Talk to: 2_SubState"""
    # talk:76020300:"Ahh...Ah..."
    assert talk_m20_21_x0(text10=76020300, z42=0, z43=0)
    Goto('L0')
    """State 9: End state"""
    Label('L1')
    return 0

def talk_m20_21_x65():
    """Queen: Conversation after getting dragon chaos (new)"""
    """State 0,1: After getting dragon chaos: Start"""
    if GetEventFlag(201720) != 0:
        """State 2: Get Dragon Chaos: Talk: Part 1 (Single Loop) _SubState"""
        # talk:70200700:"Brave Undead, you've met that dragon?\nThat living, breathing sham."
        assert talk_m20_21_x46(text6=70200700, z18=0, z19=20219000, z20=45)
    else:
        """State 3: Get the chaos of the dragon: Talk: Part 1 (new) _SubState"""
        # talk:70200600:"Brave Undead, what did that dragon tell you?"
        assert talk_m20_21_x46(text6=70200600, z18=201720, z19=20219000, z20=45)
    """State 4: End state"""
    return 0

def talk_m20_21_x66():
    """Captive Girl: Conversation (Death)"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Talk: Part 1_SubState"""
    # talk:76029000:""
    assert talk_m20_21_x0(text10=76029000, z42=0, z43=102580)
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
        assert talk_m20_21_x1(text1=70009420, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_21_x1(text1=70009410, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_21_x1(text1=70009400, z27=0, z40=-1, z41=0)
    else:
        pass
    """State 8: Hostility: End"""
    Label('L0')
    return 0
    """Unused"""
    """State 7: Conversation: 4_SubState attacked"""
    assert talk_m20_21_x1(text1=70009400, z27=0, z40=-1, z41=0)
    Goto('L0')

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
        assert talk_m20_21_x1(text1=70009420, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m20_21_x1(text1=70009410, z27=0, z40=-1, z41=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m20_21_x1(text1=70009400, z27=0, z40=-1, z41=0)
    else:
        pass
    """State 8: Hostility: End"""
    Label('L0')
    return 0
    """Unused"""
    """State 7: Conversation: 4_SubState attacked"""
    assert talk_m20_21_x1(text1=70009400, z27=0, z40=-1, z41=0)
    Goto('L0')

def talk_m20_21_x69():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(221000006) != 0 and PlayerInPoint(10003000) != 0:
        """State 4: Ann Deal postwar timer"""
        assert (GetStateTime() > 4.5) != 0
        """State 5: [Lib] Conversation: Conversation after Defeating Anne Deal_SubState"""
        # talk:69201200:"I lost everything, but remained here, patiently."
        assert talk_m20_21_x1(text1=69201200, z27=208030, z40=50, z41=0)
    elif GetEventFlag(208031) != 1 and GetEventFlag(221000001) != 0 and PlayerInPoint(10003000) != 0:
        """State 3: Timer before the Battle of Anne Deal"""
        assert (GetStateTime() > 4.5) != 0
        """State 6: [Lib] Conversation: Conversation before the Battle of Anne Deal_SubState"""
        # talk:69201400:"Many monarchs have come and gone."
        assert talk_m20_21_x1(text1=69201400, z27=208031, z40=50, z41=0)
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
    Quit()

