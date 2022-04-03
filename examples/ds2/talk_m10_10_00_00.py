# -*- coding: utf-8 -*-
def talk_m10_10_7430():
    """Tsukimitsu (Giant Forest: 3rd encounter)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_10_x9(flag9=103663, flag10=104160, flag11=110020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_10_x3(text10=74309200, z18=0, z19=20, z20=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_10_x6(flag8=110020102, text18=74309500, text19=74309500, z24=74309500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_10_x7(text21=74309600, z26=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Tsukimitsu: Conversation_SubState"""
                call = talk_m10_10_x32()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_10_x5(text22=74309400, text23=74309410, text24=74309420, text25=74309400,
                                          flag12=110020105, flag13=110020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_10_x4(flag14=103660, text26=74309100, z27=0, z28=103663)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(110020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(110020105) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_10_x8(text20=74309300, z25=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_10_7440():
    """Patch (Giant Forest)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_10_x9(flag9=103671, flag10=104170, flag11=110020111)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_10_x3(text10=74409200, z18=0, z19=20, z20=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_10_x6(flag8=110020112, text18=74409500, text19=74409500, z24=74409500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_10_x7(text21=74409600, z26=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Patch: Conversation_SubState"""
                call = talk_m10_10_x34()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_10_x5(text22=74409400, text23=74409410, text24=74409420, text25=74409400,
                                          flag12=110020115, flag13=110020116)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_10_x4(flag14=103670, text26=74409100, z27=0, z28=103671)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(110020116) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(110020115) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_10_x8(text20=74409300, z25=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_10_7510():
    """Map writing (Giant Forest)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_10_x9(flag9=103681, flag10=104180, flag11=110020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_10_x3(text10=75109200, z18=0, z19=20, z20=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_10_x6(flag8=110020122, text18=75109500, text19=75109500, z24=75109500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_10_x7(text21=75109600, z26=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Map writing: Conversation_SubState"""
                call = talk_m10_10_x33()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_10_x5(text22=75109400, text23=75109410, text24=75109420, text25=75109400,
                                          flag12=110020125, flag13=110020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_10_x4(flag14=103680, text26=75109100, z27=0, z28=103681)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(110020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(110020125) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_10_x8(text20=75109300, z25=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_10_7540():
    """Yorozu Baba"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_10_x9(flag9=103711, flag10=104210, flag11=110020131)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            # talk:75409200:"I'll have your guts for garters! "
            call = talk_m10_10_x3(text10=75409200, z18=0, z19=20, z20=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:75409500:"That's not very nice, is it?"
                call = talk_m10_10_x6(flag8=110020132, text18=75409500, text19=75409500, z24=75409500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 5: [Lib] Killing state_SubState"""
                    Label('L1')
                    # talk:75409300:"Cruel, cruel world, this is... Keh heh heh..."
                    talk_m10_10_x8(text20=75409300, z25=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: Yorozu Baba: Conversation_SubState"""
                call = talk_m10_10_x28()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    # talk:75409400:"Keh heh heh..."
                    call = talk_m10_10_x5(text22=75409400, text23=75409410, text24=75409400, text25=75409410,
                                          flag12=110020135, flag13=110020136)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        # talk:75409100:"You've no respect! Die, you rotten lout!"
                        call = talk_m10_10_x4(flag14=103710, text26=75409100, z27=0, z28=103711)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(110020136) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(110020135) != 1:
                    Goto('L2')
        """State 6: [Lib] Death state_SubState"""
        # talk:75409600:"..."
        talk_m10_10_x7(text21=75409600, z26=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_10_x0(text14=_, z31=_, z32=0):
    """[Lib] Conversation: General purpose
    text14: Conversation ID
    z31: Conversation flag
    z32: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text14, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z31, 1)
    SetEventFlag(z32, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_10_x1(text1=_, z27=_, z29=-1, z30=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z27: Conversation flag
    z29: Display distance
    z30: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z29)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z27, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_10_x2(text20=_, z25=0):
    """[Lib] Conversation: Event end
    text20: Conversation ID
    z25: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text20, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z25, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_10_x3(text10=_, z18=0, z19=20, z20=80):
    """[Lib] Reunion hostility
    text10: Conversation message ID
    z18: Conversation flag ID
    z19: Display distance
    z20: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_10_x22(text10=text10, z18=z18, z19=z19, z20=z20)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_10_x4(flag14=_, text26=_, z27=0, z28=_):
    """[Lib] First hostility
    flag14: Hostile: Global event flag
    text26: Conversation ID
    z27: Conversation flag
    z28: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag14, 1)
    SetEventFlag(z28, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag14) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_10_x1(text1=text26, z27=z27, z29=-1, z30=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_10_x5(text22=_, text23=_, text24=_, text25=_, flag12=_, flag13=_):
    """[Lib] Hostile waiting
    text22: Conversation ID: 1 attacked
    text23: Conversation ID: Attacked 2
    text24: Conversation ID: 3 attacked
    text25: Conversation ID: 4 attacked
    flag12: No use: Area and other flags
    flag13: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag13) != 1, flag13, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag12) != 1, flag12, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_10_x1(text1=text25, z27=0, z29=-1, z30=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_10_x1(text1=text24, z27=0, z29=-1, z30=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_10_x1(text1=text23, z27=0, z29=-1, z30=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_10_x1(text1=text22, z27=0, z29=-1, z30=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_10_x6(flag8=_, text18=_, text19=_, z24=_):
    """[Lib] Hostile state
    flag8: Area and other flags: HP decreased
    text18: Conversation ID: HP drop 1
    text19: Conversation ID: HP drop 2
    z24: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag8) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_10_x10(text18=text18, flag8=flag8)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_10_x10(text18=text19, flag8=flag8)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_10_x10(text18=text19, flag8=flag8)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_10_x7(text21=_, z26=0):
    """[Lib] Death status
    text21: Conversation ID
    z26: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_10_x2(text20=text21, z25=z26)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_10_x8(text20=_, z25=0):
    """[Lib] Murder status
    text20: Conversation ID
    z25: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_10_x2(text20=text20, z25=z25)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_10_x9(flag9=_, flag10=_, flag11=_):
    """[Lib] Event: Branch
    flag9: Hostile flag
    flag10: death flag
    flag11: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag10) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag11) != 0
    elif GetEventFlag(flag9) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_10_x10(text18=_, flag8=_):
    """[Lib] Conversation: HP drop
    text18: Conversation ID
    flag8: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text18, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag8, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_10_x11(flag7=110020134, text14=75400200, text15=75400300, text16=75400400, text17=75400500):
    """[Lib] Conversation: Greeting: General
    flag7: Area other flag: Contact flag
    text14: Text ID: Talk to_continuous 1
    text15: Text ID: Talk to_continuous 2
    text16: Text ID: Talk to _After a long time 1
    text17: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(flag7) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_10_x0(text14=text14, z31=0, z32=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_10_x0(text14=text15, z31=0, z32=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_10_x0(text14=text16, z31=0, z32=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_10_x0(text14=text17, z31=0, z32=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(flag7, 1)
    """State 10: End state"""
    return 0

def talk_m10_10_x12(z21=0, z22=220, z16=_, z23=0):
    """[Lib] Menu start: General purpose
    z21: Camera parameter ID
    z22: Target Damipoly ID
    z16: NPC event parameter ID
    z23: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z23, z21, z22, z16)
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

def talk_m10_10_x13(text12=75400600, text13=75400700):
    """[Lib] Menu exit: General purpose
    text12: Conversation ID (at the time of purchase)
    text13: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_10_x1(text1=text12, z27=0, z29=-1, z30=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_10_x1(text1=text13, z27=0, z29=-1, z30=0)
    """State 4: End state"""
    return 0

def talk_m10_10_x14(text11=75400800):
    """[Lib] Menu cancellation: General purpose
    text11: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_10_x1(text1=text11, z27=0, z29=-1, z30=0)
    """State 4: End state"""
    return 0

def talk_m10_10_x15(action1=1011):
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

def talk_m10_10_x16(lot5=_, flag5=_, text8=_, text9=_, z11=_, z12=0, z13=_, z14=_):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot5: Item lottery ID
    flag5: Item transfer: Global event flag
    text8: First half: Conversation ID
    text9: Second half: Conversation ID
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
    call = talk_m10_10_x1(text1=text8, z27=0, z29=-1, z30=0)
    if call.Done() and GetEventFlag(flag5) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z11, 1)
        SetEventFlag(z13, 1)
        SetEventFlag(z14, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_10_x1(text1=text9, z27=0, z29=-1, z30=0)
    elif call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_10_x27(z15=1011, lot2=lot5)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_10_x18(lot1=lot5, flag1=flag5, z1=z11, z2=z12, z3=z13, z4=z14)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_10_x17(lot4=1743000, flag4=102420, text7=74306000, z9=0, z10=110020108):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot4: Item lottery ID
    flag4: Item transfer: Global event flag
    text7: Conversation ID
    z9: Conversation: Global conversation flag
    z10: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m10_10_x1(text1=text7, z27=0, z29=-1, z30=0)
    if call.Done() and GetEventFlag(flag4) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z9, 1)
    # lot:1743000:Bluemoon Greatsword
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_10_x27(z15=1011, lot2=lot4)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_10_x18(lot1=lot4, flag1=flag4, z1=z9, z2=z10, z3=0, z4=0)
    """State 9: End state"""
    return 0

def talk_m10_10_x18(lot1=_, flag1=_, z1=_, z2=_, z3=_, z4=_):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    z1: Conversation: Global conversation flag
    z2: Trophy acquisition: Area and other flags
    z3: Emigration permission: Global event flag
    z4: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z4, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
    SetEventFlag(flag1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_10_x19(lot3=1754000, flag3=102520, text5=75406000, text6=75406010, z7=0, z8=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot3: Item lottery ID
    flag3: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_10_x1(text1=text5, z27=0, z29=-1, z30=0)
    if call.Done() and GetEventFlag(flag3) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z7, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_10_x1(text1=text6, z27=0, z29=-1, z30=0)
    # lot:1754000:Covetous Silver Serpent Ring+1
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_10_x27(z15=1011, lot2=lot3)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_10_x18(lot1=lot3, flag1=flag3, z1=z7, z2=z8, z3=0, z4=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_10_x20():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m10_10_x21():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_10_x22(text10=_, z18=0, z19=20, z20=80):
    """[Lib] Conversation: Hostile display only
    text10: Conversation ID
    z18: Conversation flag
    z19: Display distance
    z20: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text10, GetCommonEventParamDecimal(7), z19)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_10_x23(goods2=63008000, flag6=102435):
    """[Lib] Menu item: Gesture
    goods2: Gesture: Item ID
    flag6: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_10_x25(goods2=goods2, flag6=flag6)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_10_x24(goods2=63008000, flag6=102435, z16=74300000, z17=74300001):
    """[Lib] NPC menu: Gesture alone
    goods2: Item: Event item
    flag6: Item transfer: Global event flag
    z16: NPC menu: With gesture
    z17: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(flag6) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            # goods:63008000:"Joy" Gesture
            if (ItemCount(goods2, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_10_x12(z21=0, z22=220, z16=z16, z23=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m10_10_x23(goods2=goods2, flag6=flag6)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        pass
                elif call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    """State 6: [Lib] Menu exit: No Mes_SubState"""
                    Label('L0')
                    assert talk_m10_10_x20()
                    Goto('L2')
            """State 7: [Lib] Menu canceled: No Mes_SubState"""
            Label('L1')
            assert talk_m10_10_x21()
            Goto('L2')
        """State 5: [Lib] Menu start: No gesture _SubState"""
        call = talk_m10_10_x12(z21=0, z22=220, z16=z17, z23=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_10_x25(goods2=63008000, flag6=102435):
    """[Lib] Get gesture dialog
    goods2: Item ID
    flag6: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods2, 0, -1)
    SetEventFlag(flag6, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_10_x26(lot2=1751000, flag2=102471, text3=75100410, text4=75100440, z5=203504, z6=0, goods1=50860000):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Important items
    lot2: Item lottery ID
    flag2: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    goods1: Important items
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_10_x1(text1=text3, z27=0, z29=-1, z30=0)
    if call.Done() and GetEventFlag(flag2) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z5, 1)
    # goods:50860000:House Key
    elif call.Done() and (ItemCount(goods1, 1, 1, 1) > 1) != 0:
        Goto('L0')
    # lot:1751000:House Key
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_10_x27(z15=1011, lot2=lot2)
        Goto('L0')
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_10_x18(lot1=lot2, flag1=flag2, z1=z5, z2=z6, z3=0, z4=0)
    """State 4: Item transfer: Second half of conversation _SubState"""
    assert talk_m10_10_x1(text1=text4, z27=0, z29=-1, z30=0)
    """State 7: End state"""
    return 0

def talk_m10_10_x27(z15=1011, lot2=_):
    """[Lib] Inventory full dialog: Item display
    z15: Text ID
    lot2: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot2, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_10_x28():
    """Yorozu Baba: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Yorozu Baba: First conversation_SubState"""
    assert talk_m10_10_x29()
    """State 4: Yorozu Baba: NPC Menu_SubState"""
    assert talk_m10_10_x30()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_10_x29():
    """Yorozu Baba: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(203800) != 0:
        """State 4: Talk: Greeting_SubState"""
        # talk:75400200:"Buy something, anything...", talk:75400300:"Thank you kindly. Keh heh heh...", talk:75400400:"Keh heh heh...", talk:75400500:"You again? Keh heh heh..."
        assert talk_m10_10_x11(flag7=110020134, text14=75400200, text15=75400300, text16=75400400, text17=75400500)
    else:
        """State 3: Talk to (first time) _SubState"""
        # talk:75400000:"Buy something, anything... "
        assert talk_m10_10_x0(text14=75400000, z31=203800, z32=0)
        """State 2: First conversation: Set contact flag"""
        SetEventFlag(110020134, 1)
    """State 5: End state"""
    return 0

def talk_m10_10_x30():
    """Yorozu Baba: NPC Menu"""
    """State 0: Start state"""
    while True:
        """State 1,4: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_10_x12(z21=0, z22=220, z16=75400000, z23=0)
        if call.Get() == 2:
            """State 5: Yorozu Baba: Menu conversation_SubState"""
            call = talk_m10_10_x31()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3: [Lib] Exit menu: General purpose_SubState"""
            # talk:75400600:"Thank you kindly. Keh heh heh...", talk:75400700:"Lowly times, these are..."
            assert talk_m10_10_x13(text12=75400600, text13=75400700)
        """State 6: End state"""
        Label('L0')
        return 0
    """State 2: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:75400800:"Keh heh heh..."
    assert talk_m10_10_x14(text11=75400800)
    Goto('L0')

def talk_m10_10_x31():
    """Yorozu Baba: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102520) != 1 and (GetGlobalVariable(220) > NpcInfoValue(7540, 0)) != 0 and GetEventFlag(104210)
        != 1):
        """State 8: Equipment transfer (Conditions: Shop purchase total is above a certain level) _SubState"""
        # lot:1754000:Covetous Silver Serpent Ring+1, talk:75406000:"Everyone's so stingy around here. ", talk:75406010:"Everyone's so stingy everywhere!"
        assert talk_m10_10_x19(lot3=1754000, flag3=102520, text5=75406000, text6=75406010, z7=0, z8=0)
    elif GetEventFlag(203803) != 0:
        """State 7: Menu conversation: 4_SubState"""
        # talk:75405300:"It's high time that I pick up and move."
        call = talk_m10_10_x1(text1=75405300, z27=0, z29=-1, z30=0)
        if call.Done() and GetEventFlag(102521) != 1:
            """State 2: Menu conversation: Set movement permission flag"""
            SetEventFlag(102521, 1)
            assert GetEventFlag(102521) != 0
        elif call.Done():
            pass
    elif GetEventFlag(203802) != 0:
        """State 6: Menu conversation: 3_SubState"""
        # talk:75405200:"Everyone's so stingy around here. "
        assert talk_m10_10_x1(text1=75405200, z27=203803, z29=-1, z30=0)
    elif GetEventFlag(203801) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:75405100:"Seemed like the battles would never end."
        assert talk_m10_10_x1(text1=75405100, z27=203802, z29=-1, z30=0)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:75405000:"My name is Melentia."
        assert talk_m10_10_x1(text1=75405000, z27=203801, z29=-1, z30=0)
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_10_x32():
    """Moonlight Jun: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetEventFlag(102420) != 1 and GetEventFlag(102436) != 0 and GetEventFlag(104160) != 1 and GetEventFlag(203322)
        != 0):
        """State 4: Equipment transfer (condition: white phantom summon achievement) _SubState"""
        # lot:1743000:Bluemoon Greatsword, talk:74306000:"A man's journey...is never done..."
        assert talk_m10_10_x17(lot4=1743000, flag4=102420, text7=74306000, z9=0, z10=110020108)
    elif GetEventFlag(203322) != 0:
        """State 7: Talk: 4_SubState"""
        # talk:74302300:"I've a great debt to you.\nAnd I'll never forget it."
        call = talk_m10_10_x0(text14=74302300, z31=0, z32=0)
        if call.Done() and GetEventFlag(102423) != 1:
            """State 3: Conversation: Set migration permission flag"""
            SetEventFlag(102423, 1)
            if GetEventFlag(102435) != 1 and GetEventFlag(102423) != 0:
                """State 9: [Lib] Satoshi Tsutsumi: NPC Menu_SubState"""
                Label('L0')
                # goods:63008000:"Joy" Gesture
                assert talk_m10_10_x24(goods2=63008000, flag6=102435, z16=74300000, z17=74300001)
            elif GetEventFlag(102423) != 0:
                pass
        elif call.Done() and GetEventFlag(102435) != 1:
            Goto('L0')
        elif call.Done():
            pass
    elif GetEventFlag(203321) != 0:
        """State 8: Speak: Part 3_SubState"""
        # talk:74302200:"I see you've taken a liking to the sword.\nWell, I applaud you, for you've a sharp eye."
        assert talk_m10_10_x0(text14=74302200, z31=203322, z32=0)
    elif GetEventFlag(203320) != 0:
        """State 6: Talk to: 2_SubState"""
        # talk:74302100:"See the old sword's caught your attention?\nWell, you've a good eye, then."
        assert talk_m10_10_x0(text14=74302100, z31=203321, z32=0)
    else:
        """State 5: Talk: Part 1_SubState"""
        # talk:74302000:"Well, we meet again! What you doing here?"
        assert talk_m10_10_x0(text14=74302000, z31=203320, z32=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 10: End state"""
    return 0

def talk_m10_10_x33():
    """Map writing: Conversation"""
    """State 0,1: Conversation: Start"""
    if GetEventFlag(203505) != 0:
        """State 9: Talk: Part 7_SubState"""
        # talk:75100600:"I'll be back in Majula soon."
        call = talk_m10_10_x0(text14=75100600, z31=0, z32=0)
        if call.Done() and GetEventFlag(102460) != 1:
            """State 3: Conversation: Set migration permission flag"""
            SetEventFlag(102460, 1)
            assert GetEventFlag(102460) != 0
        elif call.Done():
            pass
    elif GetEventFlag(203504) != 0:
        """State 8: Talk: Part 6: 1_SubState"""
        # talk:75100500:"Incredible really, isn't it? Such a map, to be chiselled in stone..."
        assert talk_m10_10_x0(text14=75100500, z31=203505, z32=0)
        """State 13: Talk: Part 6: 2_SubState"""
        # talk:75100510:"Oh, but one thing..."
        assert talk_m10_10_x1(text1=75100510, z27=0, z29=-1, z30=0)
        """State 14: Talk: Part 6: 3_SubState"""
        # talk:75100530:"I can't be certain, but...\nI've heard disturbing noises..."
        assert talk_m10_10_x1(text1=75100530, z27=0, z29=-1, z30=0)
    elif GetEventFlag(203503) != 0:
        """State 12: Talk: Part 5: 1_SubState"""
        # talk:75100400:"Were you looking for that map?"
        assert talk_m10_10_x0(text14=75100400, z31=0, z32=0)
        """State 15: Speak: Part 5: 2_SubState"""
        # lot:1751000:House Key, talk:75100410:"Wonderful! Then you're fascinated\nby maps, just like me?!", talk:75100440:"What a joy to meet a kindred spirit out here...", goods:50860000:House Key
        assert (talk_m10_10_x26(lot2=1751000, flag2=102471, text3=75100410, text4=75100440, z5=203504,
                z6=0, goods1=50860000))
    elif GetEventFlag(203502) != 0:
        """State 7: Talk: Part 4: 1_SubState"""
        # talk:75100300:"Inside the mansion, I found a strange map.\nLike none I'd ever seen."
        assert talk_m10_10_x0(text14=75100300, z31=203503, z32=0)
        """State 10: Talk: Part 4: 2_SubState"""
        # talk:75100330:"Yes, yes, that's it!\nThat's why I came to the kingdom!"
        assert talk_m10_10_x1(text1=75100330, z27=0, z29=-1, z30=0)
        """State 11: Speak: Part 4: 3_SubState"""
        # talk:75100340:"Wait...No, that wasn't it..."
        assert talk_m10_10_x1(text1=75100340, z27=0, z29=-1, z30=0)
    elif GetEventFlag(203501) != 0:
        """State 6: Speak: Part 3_SubState"""
        # talk:75100200:"I came to this land some time ago."
        assert talk_m10_10_x0(text14=75100200, z31=203502, z32=0)
    elif GetEventFlag(203500) != 0:
        """State 5: Talk to: 2_SubState"""
        # talk:75100100:"Why cartography, you ask?"
        assert talk_m10_10_x0(text14=75100100, z31=203501, z32=0)
    else:
        """State 4: Talk: Part 1_SubState"""
        # talk:75100000:"Oh, I'm sorry.\nI was just...daydreaming, I think."
        assert talk_m10_10_x0(text14=75100000, z31=203500, z32=0)
    """State 2,16: End state"""
    return 0

def talk_m10_10_x34():
    """Patch: Conversation"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        ClearNpcMenuResults()
        if GetEventFlag(102441) != 1 and GetEventFlag(102452) != 0 and GetEventFlag(104170) != 1:
            """State 4: Equipment transfer (condition: white phantom summon achievement) _SubState"""
            # lot:1744010:Pate's Spear, talk:74406000:"Heh heh heh..."
            assert (talk_m10_10_x16(lot5=1744010, flag5=102441, text8=74406000, text9=74406010, z11=0,
                    z12=0, z13=0, z14=0))
        elif GetEventFlag(203400) != 1 and GetEventFlag(102443) != 0:
            """State 7: Patch: Unread before activation After activation: Conversation_SubState"""
            assert talk_m10_10_x37()
        elif GetEventFlag(102443) != 0:
            break
        else:
            """State 5: Patch: Before trap activation: Conversation_SubState"""
            call = talk_m10_10_x35()
            if call.Done():
                pass
            elif GetEventFlag(102443) != 0:
                """State 3: Conversation: Key Guide: Delete"""
                DeleteKeyGuideArea()
                continue
        """State 2: Conversation: End"""
        Label('L0')
        ClearNpcMenuResults()
        """State 8: End state"""
        return 0
    """State 6: Patch: After trap activation: Conversation_SubState"""
    assert talk_m10_10_x36()
    Goto('L0')

def talk_m10_10_x35():
    """Patch: Before trap activation: Conversation"""
    """State 0,1: Before trap activation: Start"""
    if GetEventFlag(203401) != 0:
        """State 4: Before trap activation: Talk to 3_SubState"""
        # talk:74400200:"I'll leave this one to you.\nI'm worried about what might be inside."
        assert talk_m10_10_x0(text14=74400200, z31=0, z32=0)
    elif GetEventFlag(203400) != 0:
        """State 3: Before trap activation: Talk to 2_SubState"""
        # talk:74400100:"Oh yes, you be cautious\nif you go any farther."
        assert talk_m10_10_x0(text14=74400100, z31=203401, z32=0)
    else:
        """State 2: Before trap activation: Talk to 1_SubState"""
        # talk:74400000:"Hello there. Travelling all alone in these treacherous times?"
        assert talk_m10_10_x0(text14=74400000, z31=203400, z32=0)
    """State 5: End state"""
    return 0

def talk_m10_10_x36():
    """Patch: After trap activation: Conversation"""
    """State 0,1: After trap activation: Start"""
    if GetEventFlag(203411) != 0:
        """State 4: After trap activation: Talk to 3_SubState"""
        # talk:74400300:"Well, I see you managed to escape."
        assert talk_m10_10_x0(text14=74400300, z31=0, z32=0)
    elif GetEventFlag(203410) != 0:
        """State 5: [Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key: Patch_SubState"""
        # lot:1744020:White Sign Soapstone, talk:74400330:"There's a right foul creature lurking this way.\nI'd say, why disturb the thing?", talk:74400360:"It allows Undead to call out for help\nto one another, across the fissures between worlds."
        assert (talk_m10_10_x38(lot1=1744020, flag1=102444, text1=74400330, text2=74400360, z1=203411,
                z2=0, z3=102450, z4=102442))
    else:
        """State 2: After trap activation: Talk to 1_SubState"""
        # talk:74400300:"Well, I see you managed to escape."
        assert talk_m10_10_x0(text14=74400300, z31=203410, z32=0)
    """State 6: End state"""
    Label('L0')
    return 0
    """Unused"""
    """State 3: After trap activation: Talk to 2_SubState"""
    # lot:1744020:White Sign Soapstone, talk:74400330:"There's a right foul creature lurking this way.\nI'd say, why disturb the thing?", talk:74400360:"It allows Undead to call out for help\nto one another, across the fissures between worlds."
    assert (talk_m10_10_x16(lot5=1744020, flag5=102444, text8=74400330, text9=74400360, z11=203411, z12=0,
            z13=102450, z14=102442))
    Goto('L0')

def talk_m10_10_x37():
    """Patch: Unread before triggering After triggering: Conversation"""
    """State 0,1: After unread before triggering: Start"""
    if GetEventFlag(203421) != 0:
        """State 5: Unread before trap activation: After trap activation: Talk to 3_SubState"""
        # talk:74400700:"Good to see you safe."
        assert talk_m10_10_x0(text14=74400700, z31=0, z32=0)
    elif GetEventFlag(203420) != 0:
        """State 6: [Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key: Patch_SubState"""
        # lot:1744020:White Sign Soapstone, talk:74400330:"There's a right foul creature lurking this way.\nI'd say, why disturb the thing?", talk:74400360:"It allows Undead to call out for help\nto one another, across the fissures between worlds."
        assert (talk_m10_10_x38(lot1=1744020, flag1=102444, text1=74400330, text2=74400360, z1=203421,
                z2=0, z3=102450, z4=102442))
    else:
        """State 3: Unread before trap activation: After trap activation: Talk to 1_SubState"""
        # talk:74400500:"Well, that was a close call! Heh heh..."
        assert talk_m10_10_x0(text14=74400500, z31=203420, z32=0)
    """State 7: End state"""
    Label('L0')
    return 0
    """Unused"""
    """State 2: Set migration permission flag"""
    Label('L1')
    SetEventFlag(102450, 1)
    SetEventFlag(102442, 1)
    assert GetEventFlag(102450) != 0 and GetEventFlag(102442) != 0
    Goto('L0')
    """State 4: Unread before trap activation: After trap activation: Talk to 2_SubState"""
    # lot:1744020:White Sign Soapstone, talk:74400330:"There's a right foul creature lurking this way.\nI'd say, why disturb the thing?", talk:74400360:"It allows Undead to call out for help\nto one another, across the fissures between worlds."
    assert (talk_m10_10_x16(lot5=1744020, flag5=102444, text8=74400330, text9=74400360, z11=203421, z12=0,
            z13=0, z14=0))
    Goto('L1')

def talk_m10_10_x38(lot1=1744020, flag1=102444, text1=74400330, text2=74400360, z1=_, z2=0, z3=102450,
                    z4=102442):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key: Patch
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z1: Conversation: Global conversation flag
    z2: Trophy acquisition: Area and other flags
    z3: Emigration permission: Global event flag
    z4: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_10_x1(text1=text1, z27=0, z29=-1, z30=0)
    if call.Done() and GetEventFlag(flag1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z1, 1)
        SetEventFlag(z3, 1)
        SetEventFlag(z4, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L1')
        assert talk_m10_10_x1(text1=text2, z27=0, z29=-1, z30=0)
    # goods:62030000:White Sign Soapstone
    elif call.Done() and (ItemCount(62030000, 1, 1, 1) > 1) != 0:
        Goto('L0')
    # lot:1744020:White Sign Soapstone
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 9: Inventory full confirmation dialog_SubState"""
        # action:1011:"Your inventory bag is full"
        assert talk_m10_10_x15(action1=1011)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_10_x18(lot1=lot1, flag1=flag1, z1=z1, z2=z2, z3=z3, z4=z4)
        Goto('L1')
    """State 10: End state"""
    return 0

