# -*- coding: utf-8 -*-
def talk_m10_16_7520():
    """Woman Knight (Forgetting Castle)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_16_x9(flag15=103692, flag16=104190, flag17=116020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_16_x3(text12=75209200, z26=0, z27=20, z28=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_16_x6(flag14=116020102, text17=75209500, text18=75209500, z36=75209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_16_x7(text20=75209600, z38=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: [Lib] Female knight: Before last: Conversation_SubState"""
                call = talk_m10_16_x25(flag4=102480, flag5=102485, flag6=102500, z8=116020109)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_16_x5(text21=75209400, text22=75209410, text23=75209420, text24=75209400,
                                          flag18=116020105, flag19=116020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_16_x4(flag20=103690, text25=75209100, z39=0, z40=103692)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(116020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(116020105) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_16_x8(text19=75209300, z37=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_16_7530():
    """Kanemori: Aken"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_16_x9(flag15=103700, flag16=104200, flag17=116020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_16_x3(text12=75309200, z26=0, z27=20, z28=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_16_x6(flag14=116020122, text17=75309500, text18=75309500, z36=75309500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 7: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_16_x8(text19=75309300, z37=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: [Lib] Kanemori: Conversation_SubState"""
                # action:1335:"Join the Bell Keeper covenant?", action:1345:"Abandon your covenant and\njoin the Bell Keeper covenant?"
                call = talk_m10_16_x30(z1=60, action1=1335, action2=1345, z2=116020127)
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_16_x5(text21=75309400, text22=75309410, text23=75309420, text24=75309400,
                                          flag18=116020125, flag19=116020126)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 8: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_16_x15(flag13=103700, text13=75309100, z29=0, val3=6, z30=200905,
                                               z31=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(116020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(116020125) != 1:
                    Goto('L2')
        """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
        talk_m10_16_x43(text10=75309600, z18=0, val2=6)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_16_7643():
    """EX Blacksmith"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_16_x9(flag15=103790, flag16=104290, flag17=116020141)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_16_x3(text12=76439200, z26=0, z27=20, z28=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_16_x6(flag14=116020142, text17=76439500, text18=76439500, z36=76439500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_16_x7(text20=76439600, z38=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: EX Blacksmith: Conversation_SubState"""
                call = talk_m10_16_x50()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_16_x5(text21=76439400, text22=76439410, text23=76439420, text24=76439400,
                                          flag18=116020145, flag19=116020146)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_16_x4(flag20=103790, text25=76439100, z39=0, z40=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(116020146) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(116020145) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_16_x8(text19=76439300, z37=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_16_7680():
    """Spell mania"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(116010150) != 0:
            pass
        else:
            """State 3: Conversation: Petrified release: Wait"""
            assert GetEventFlag(102741) != 0 and (GetCurrentActivationState() == 3) != 1
            """State 4: Conversation: Release petrification: Damage reset"""
            ResetDamageTakenCount()
        """State 5: [Lib] Event: Branch_SubState"""
        call = talk_m10_16_x9(flag15=103810, flag16=104310, flag17=116020151)
        if call.Get() == 1:
            """State 7: [Lib] Reunion hostility_SubState"""
            call = talk_m10_16_x3(text12=76809200, z26=0, z27=20, z28=80)
            if call.Done():
                """State 9: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_16_x6(flag14=116020152, text17=76809500, text18=76809500, z36=76809500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 10: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_16_x7(text20=76809600, z38=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 12: Spermia: Conversation_SubState"""
                call = talk_m10_16_x45()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 8: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_16_x5(text21=76809400, text22=76809410, text23=76809420, text24=76809400,
                                          flag18=116020155, flag19=116020156)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 6: [Lib] First adversification_SubState"""
                        call = talk_m10_16_x4(flag20=103810, text25=76809100, z39=0, z40=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(116020156) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(116020155) != 1:
                    Goto('L2')
        """State 11: [Lib] Killing state_SubState"""
        talk_m10_16_x8(text19=76809300, z37=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_16_x0(text26=_, z43=_, z44=0):
    """[Lib] Conversation: General purpose
    text26: Conversation ID
    z43: Conversation flag
    z44: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text26, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z43, 1)
    SetEventFlag(z44, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_16_x1(text1=_, z29=_, z41=-1, z42=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z29: Conversation flag
    z41: Display distance
    z42: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z41)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z29, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_16_x2(text10=_, z18=0):
    """[Lib] Conversation: Event end
    text10: Conversation ID
    z18: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text10, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_16_x3(text12=_, z26=0, z27=20, z28=80):
    """[Lib] Reunion hostility
    text12: Conversation message ID
    z26: Conversation flag ID
    z27: Display distance
    z28: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_16_x35(text12=text12, z26=z26, z27=z27, z28=z28)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_16_x4(flag20=_, text25=_, z39=0, z40=_):
    """[Lib] First hostility
    flag20: Hostile: Global event flag
    text25: Conversation ID
    z39: Conversation flag
    z40: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag20, 1)
    SetEventFlag(z40, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag20) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_16_x1(text1=text25, z29=z39, z41=-1, z42=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_16_x5(text21=_, text22=_, text23=_, text24=_, flag18=_, flag19=_):
    """[Lib] Hostile waiting
    text21: Conversation ID: 1 attacked
    text22: Conversation ID: Attacked 2
    text23: Conversation ID: 3 attacked
    text24: Conversation ID: 4 attacked
    flag18: No use: Area and other flags
    flag19: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag19) != 1, flag19, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag18) != 1, flag18, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_16_x1(text1=text24, z29=0, z41=-1, z42=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_16_x1(text1=text23, z29=0, z41=-1, z42=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_16_x1(text1=text22, z29=0, z41=-1, z42=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_16_x1(text1=text21, z29=0, z41=-1, z42=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_16_x6(flag14=_, text17=_, text18=_, z36=_):
    """[Lib] Hostile state
    flag14: Area and other flags: HP decreased
    text17: Conversation ID: HP drop 1
    text18: Conversation ID: HP drop 2
    z36: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag14) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_16_x10(text17=text17, flag14=flag14)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_16_x10(text17=text18, flag14=flag14)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_16_x10(text17=text18, flag14=flag14)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_16_x7(text20=_, z38=0):
    """[Lib] Death status
    text20: Conversation ID
    z38: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_16_x2(text10=text20, z18=z38)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_16_x8(text19=_, z37=0):
    """[Lib] Murder status
    text19: Conversation ID
    z37: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_16_x2(text10=text19, z18=z37)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_16_x9(flag15=_, flag16=_, flag17=_):
    """[Lib] Event: Branch
    flag15: Hostile flag
    flag16: death flag
    flag17: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag16) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag17) != 0
    elif GetEventFlag(flag15) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_16_x10(text17=_, flag14=_):
    """[Lib] Conversation: HP drop
    text17: Conversation ID
    flag14: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text17, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag14, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_16_x11(action1=_):
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

def talk_m10_16_x12(z32=0, z33=220, z34=_, z35=0):
    """[Lib] Menu start: General purpose
    z32: Camera parameter ID
    z33: Target Damipoly ID
    z34: NPC event parameter ID
    z35: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z35, z32, z33, z34)
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

def talk_m10_16_x13(text15=_, text16=_):
    """[Lib] Menu exit: General purpose
    text15: Conversation ID (at the time of purchase)
    text16: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_16_x1(text1=text15, z29=0, z41=-1, z42=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_16_x1(text1=text16, z29=0, z41=-1, z42=0)
    """State 4: End state"""
    return 0

def talk_m10_16_x14(text14=_):
    """[Lib] Menu cancellation: General purpose
    text14: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_16_x1(text1=text14, z29=0, z41=-1, z42=0)
    """State 4: End state"""
    return 0

def talk_m10_16_x15(flag13=103700, text13=75309100, z29=0, val3=6, z30=200905, z31=0):
    """[Lib] First hostility _ (pledge cancellation)
    flag13: Hostile: Global event flag
    text13: Conversation ID
    z29: Conversation flag
    val3: Cancellation pledge name
    z30: Pledge cancellation: Global conversation flag
    z31: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag13, 1)
    SetEventFlag(z31, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag13) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_16_x34(val2=val3)
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
    assert talk_m10_16_x1(text1=text13, z29=z29, z41=-1, z42=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_16_x16(text9=_, z15=0, lot7=_, flag9=_, z16=215, z1=60):
    """[Lib] Conversation: Pledge ranking
    text9: Ranking: Conversation ID
    z15: Ranking: Conversation flag
    lot7: Item lottery
    flag9: Ranking transfer: Global event flag
    z16: Previous rank: Global variable
    z1: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_16_x17(action4=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text9, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z15, 1)
    if CanGetItemLot(lot7, 1) != 1 and GetEventFlag(flag9) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_16_x44(z17=1011, lot1=lot7)
    elif GetEventFlag(flag9) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_16_x19(lot6=lot7, z14=flag9)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z16, GetAreaVariable(z1))
    """State 11: End state"""
    return 0

def talk_m10_16_x17(action4=_):
    """[Lib] OK dialog
    action4: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action4, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_16_x18(lot6=1768000, z14=102740, text7=76806000, text8=76806010):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot6: Item lottery ID
    z14: Global event flag
    text7: First half: Conversation ID
    text8: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_16_x1(text1=text7, z29=0, z41=-1, z42=0)
    # lot:1768000:Black Hood
    if call.Done() and CanGetItemLot(lot6, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_16_x44(z17=1011, lot1=lot6)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_16_x19(lot6=lot6, z14=z14)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_16_x1(text1=text8, z29=0, z41=-1, z42=0)
    """State 6: End state"""
    return 0

def talk_m10_16_x19(lot6=_, z14=_):
    """[Lib] Item acquisition dialog
    lot6: Item lottery ID
    z14: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z14, 1)
    AwardItem(lot6, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_16_x20(lot5=_, flag8=_, text5=_, text6=_, z11=_, z8=_, z12=0, z13=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot5: Item lottery ID
    flag8: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z11: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    z12: Emigration permission: Global event flag
    z13: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_16_x1(text1=text5, z29=0, z41=-1, z42=0)
    if call.Done() and GetEventFlag(flag8) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z11, 1)
        SetEventFlag(z12, 1)
        SetEventFlag(z13, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_16_x1(text1=text6, z29=0, z41=-1, z42=0)
    elif call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_16_x44(z17=1011, lot1=lot5)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_16_x22(lot2=lot5, flag2=flag8, z4=z11, z5=z8, z12=z12, z13=z13)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_16_x21(lot4=1752020, flag7=102496, text4=75201100, z9=203620, z10=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot4: Item lottery ID
    flag7: Item transfer: Global event flag
    text4: Conversation ID
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
    call = talk_m10_16_x1(text1=text4, z29=0, z41=-1, z42=0)
    if call.Done() and GetEventFlag(flag7) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z9, 1)
    # lot:1752020:Ring of Steel Protection+1
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_16_x44(z17=1011, lot1=lot4)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_16_x22(lot2=lot4, flag2=flag7, z4=z9, z5=z10, z12=0, z13=0)
    """State 9: End state"""
    return 0

def talk_m10_16_x22(lot2=_, flag2=_, z4=_, z5=_, z12=0, z13=0):
    """[Lib] Item acquisition dialog: Conversation
    lot2: Item lottery ID
    flag2: Item transfer: Global event flag
    z4: Conversation: Global conversation flag
    z5: Trophy acquisition: Area and other flags
    z12: Emigration permission: Global event flag
    z13: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z13, 1)
    SetEventFlag(z12, 1)
    SetEventFlag(z5, 1)
    SetEventFlag(z4, 1)
    SetEventFlag(flag2, 1)
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_16_x23(lot3=1753020, flag3=102511, text2=75300300, text3=75300310, z6=0, z7=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot3: Item lottery ID
    flag3: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z6: Conversation: Global conversation flag
    z7: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_16_x1(text1=text2, z29=0, z41=-1, z42=0)
    if call.Done() and GetEventFlag(flag3) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z6, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_16_x1(text1=text3, z29=0, z41=-1, z42=0)
    # lot:1753020:Bell Keeper's Seal
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_16_x44(z17=1011, lot1=lot3)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_16_x22(lot2=lot3, flag2=flag3, z4=z6, z5=z7, z12=0, z13=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_16_x24(lot2=1764300, flag2=102681, text1=76436000, z4=0, z5=116020148):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot2: Item lottery ID
    flag2: Item transfer: Global event flag
    text1: Conversation ID
    z4: Conversation: Global conversation flag
    z5: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m10_16_x1(text1=text1, z29=0, z41=-1, z42=0)
    if call.Done() and GetEventFlag(flag2) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z4, 1)
    # lot:1764300:Titanite Slab
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_16_x44(z17=1011, lot1=lot2)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_16_x22(lot2=lot2, flag2=flag2, z4=z4, z5=z5, z12=0, z13=0)
    """State 6: End state"""
    return 0

def talk_m10_16_x25(flag4=102480, flag5=102485, flag6=102500, z8=116020109):
    """[Lib] Woman Knight: Before Last: Conversation
    flag4: Encounter: Global event flag
    flag5: Generation establishment: Global event flag
    flag6: White Phantom Appearance: Global Event Flag
    z8: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203630) != 0 and GetEventFlag(flag4) != 0:
        """State 5: Woman Knight: Encounter 4th: Conversation_SubState"""
        Label('L0')
        assert talk_m10_16_x29(flag5=flag5, flag4=flag4, flag6=flag6)
    elif GetEventFlag(203623) != 0 and GetEventFlag(flag4) != 1:
        Goto('L0')
    elif GetEventFlag(203620) != 0 and GetEventFlag(flag4) != 0:
        """State 4: Woman Knight: Encounter 3rd: Conversation_SubState"""
        Label('L1')
        assert talk_m10_16_x28(flag5=flag5, flag4=flag4, flag6=flag6)
    elif GetEventFlag(203614) != 0 and GetEventFlag(flag4) != 1:
        Goto('L1')
    elif GetEventFlag(203610) != 0 and GetEventFlag(flag4) != 0:
        """State 3: Woman Knight: Encounter 2nd: Conversation_SubState"""
        Label('L2')
        assert talk_m10_16_x27(flag5=flag5, flag4=flag4, flag6=flag6)
    elif GetEventFlag(203602) != 0 and GetEventFlag(flag4) != 1:
        Goto('L2')
    elif GetEventFlag(203600) != 0 and GetEventFlag(flag4) != 0:
        """State 2: Woman Knight: First encounter: Conversation_SubState"""
        Label('L3')
        assert talk_m10_16_x26(flag5=flag5, flag4=flag4, flag6=flag6)
    else:
        Goto('L3')
    """State 7: End state"""
    Label('L4')
    return 0
    """Unused"""
    """State 6: Woman Knight: Equipment Transfer_SubState"""
    # lot:1752000:Mirrah Greatsword, talk:75206000:"Please...find my brother..."
    assert (talk_m10_16_x20(lot5=1752000, flag8=102497, text5=75206000, text6=75206010, z11=0, z8=z8,
            z12=0, z13=0))
    Goto('L4')

def talk_m10_16_x26(flag5=102485, flag4=102480, flag6=102500):
    """Woman Knight: First encounter: Conversation
    flag5: Generation stop: Global event flag
    flag4: Encounter: Global event flag
    flag6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: First encounter: Start"""
    if GetEventFlag(203601) != 0:
        """State 7: First encounter: Talk: Part 3: 1_SubState"""
        # talk:75200300:"You are an odd one, indeed.\nI've always made a point of avoiding people."
        assert talk_m10_16_x0(text26=75200300, z43=0, z44=0)
        """State 10: First encounter: Talk: Part 3: 2_SubState"""
        # talk:75200310:"While you've made a point of engaging me."
        assert talk_m10_16_x1(text1=75200310, z29=0, z41=-1, z42=0)
        """State 11: First encounter: Talk: Part 3: 3_SubState"""
        # talk:75200320:"I can see that you are mid-journey.\nIf you require assistance, I will help you."
        assert talk_m10_16_x1(text1=75200320, z29=203602, z41=-1, z42=0)
        """State 4: First encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag6, 1)
        assert GetEventFlag(flag6) != 0
        """State 2: First encounter: stop generation"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
    elif GetEventFlag(203600) != 0:
        """State 6: First encounter: Talk: Part 2: 1_SubState"""
        # talk:75200100:"Phew..."
        assert talk_m10_16_x0(text26=75200100, z43=0, z44=0)
        """State 8: First encounter: Talk: Part 2: 2_SubState"""
        # talk:75200110:"Heh heh. You are an odd one."
        assert talk_m10_16_x1(text1=75200110, z29=0, z41=-1, z42=0)
        """State 9: First encounter: Talk: Part 2: 3_SubState"""
        # talk:75200120:"Normally, people keep a safe distance\nwhen they see this mask. But you..."
        assert talk_m10_16_x1(text1=75200120, z29=203601, z41=-1, z42=0)
        """State 3: First encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    else:
        """State 5: First encounter: Talk: Part 1_SubState"""
        # talk:75200000:"What is it?"
        assert talk_m10_16_x0(text26=75200000, z43=203600, z44=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_16_x27(flag5=102485, flag4=102480, flag6=102500):
    """Woman Knight: Second encounter: Conversation
    flag5: Generation stop: Global event flag
    flag4: Encounter: Global event flag
    flag6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter second time: Start"""
    if GetEventFlag(203614) != 0:
        """State 10: Encounter 2nd time: Speak: Part 5 (Single loop) _SubState"""
        # talk:75201000:"I'm sorry...to burden you with talk of my fate."
        assert talk_m10_16_x0(text26=75201000, z43=0, z44=0)
        """State 3: 2nd encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203613) != 0:
        """State 9: Encounter second time: Talk: Part 5: 1_SubState"""
        # talk:75200900:"Have you heard of the Undead?\nThese poor souls affected by the curse."
        assert talk_m10_16_x0(text26=75200900, z43=0, z44=0)
        """State 13: Encounter second time: Talk: Part 5: 2_SubState"""
        # talk:75200910:"An Undead gradually loses his humanity,\nuntil his wits degrade completely."
        assert talk_m10_16_x1(text1=75200910, z29=0, z41=-1, z42=0)
        """State 14: Encounter second time: Speak: Part 5: 3_SubState"""
        # talk:75200960:"I can only hope...that they are."
        assert talk_m10_16_x1(text1=75200960, z29=203614, z41=-1, z42=0)
        """State 4: Second encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag6, 1)
        assert GetEventFlag(flag6) != 0
        """State 2: Second encounter: Stop generation"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
    elif GetEventFlag(203612) != 0:
        """State 8: Encounter 2nd time: Talk: 4_SubState"""
        # talk:75200800:"I was raised to wield a sword from birth."
        assert talk_m10_16_x0(text26=75200800, z43=203613, z44=0)
        Goto('L0')
    elif GetEventFlag(203611) != 0:
        """State 7: Encounter second time: Talk: Part 3_SubState"""
        # talk:75200700:"Our land of Mirrah is surrounded by enemies,\nand constantly at war."
        assert talk_m10_16_x0(text26=75200700, z43=203612, z44=0)
        Goto('L0')
    elif GetEventFlag(203610) != 0:
        """State 6: Encounter second time: Speak: Part 2_SubState"""
        # lot:1752010:Human Effigy, talk:75200600:"Ah, yes, I have not thanked you\nfor humouring me the other day.", talk:75200620:"Of course, I've no idea what it is.\nHeh heh."
        assert (talk_m10_16_x20(lot5=1752010, flag8=102495, text5=75200600, text6=75200620, z11=203611,
                z8=0, z12=0, z13=0))
        Goto('L0')
    else:
        """State 5: Encounter second time: Speak: Part 1: 1_SubState"""
        # talk:75200500:"I thought that might be you.\nYou haven't changed a bit, have you? Heh heh."
        assert talk_m10_16_x0(text26=75200500, z43=0, z44=0)
        """State 11: Encounter second time: Talk: Part 1: 2_SubState"""
        # talk:75200520:"A wretched place, indeed, but not \nwithout traces of its former glory."
        assert talk_m10_16_x1(text1=75200520, z29=0, z41=-1, z42=0)
        """State 12: Encounter second time: Talk: Part 1: 3_SubState"""
        # talk:75200530:"What could have caused such degradation?"
        assert talk_m10_16_x1(text1=75200530, z29=203610, z41=-1, z42=0)
        Goto('L0')
    """State 15: End state"""
    return 0

def talk_m10_16_x28(flag5=102485, flag4=102480, flag6=102500):
    """Woman Knight: Encounter 3rd: Conversation
    flag5: Generation stop: Global event flag
    flag4: Encounter: Global event flag
    flag6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 3rd: Start"""
    if GetEventFlag(203622) != 0:
        """State 8: Encounter 3rd time: Talk: 4_SubState"""
        # talk:75201400:"If only someone would hear my tale..."
        assert talk_m10_16_x0(text26=75201400, z43=203623, z44=0)
        """State 4: 3rd encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag6, 1)
        assert GetEventFlag(flag6) != 0
        """State 2: Encounter 3rd: Stop generation"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
    elif GetEventFlag(203621) != 0:
        """State 7: Encounter third time: Speak: Part 3: 1_SubState"""
        # talk:75201300:"I had an older brother. We learned to fence together."
        assert talk_m10_16_x0(text26=75201300, z43=0, z44=0)
        """State 11: Encounter third time: Speak: Part 3: 2_SubState"""
        # talk:75201340:"But then, one day...he was gone,\nlost without a trace."
        assert talk_m10_16_x1(text1=75201340, z29=203622, z41=-1, z42=0)
        """State 3: 3rd encounter: Set flag during encounter"""
        Label('L0')
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203620) != 0:
        """State 6: Encounter 3rd time: Speak: Part 2: 1_SubState"""
        # talk:75201200:"I've found my thoughts growing hazy."
        assert talk_m10_16_x0(text26=75201200, z43=0, z44=0)
        """State 9: Encounter third time: Talk: Part 2: 2_SubState"""
        # talk:75201220:"The curse is doing its work upon me."
        assert talk_m10_16_x1(text1=75201220, z29=0, z41=-1, z42=0)
        """State 10: Encounter third time: Speak: Part 2: 3_SubState"""
        # talk:75201230:"I am frightened... Terribly so..."
        assert talk_m10_16_x1(text1=75201230, z29=203621, z41=-1, z42=0)
        Goto('L0')
    else:
        """State 5: Encounter 3rd time: Speak: Part 1_SubState"""
        # lot:1752020:Ring of Steel Protection+1, talk:75201100:"Still on the road, are you?"
        assert talk_m10_16_x21(lot4=1752020, flag7=102496, text4=75201100, z9=203620, z10=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_16_x29(flag5=102485, flag4=102480, flag6=102500):
    """Woman Knight: Encounter 4th: Conversation
    flag5: Generation stop: Global event flag
    flag4: Encounter: Global event flag
    flag6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 4th: Start"""
    if GetEventFlag(203632) != 0:
        """State 8: Encounter 4th: Speak: Part 4_SubState"""
        # talk:75201800:"Sometimes, I feel obsessed...\nwith this insignificant thing called "self"."
        assert talk_m10_16_x0(text26=75201800, z43=203633, z44=0)
        """State 4: 4th encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag6, 1)
        assert GetEventFlag(flag6) != 0
        """State 2: Encounter 4th: Stop generation"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
    elif GetEventFlag(203631) != 0:
        """State 7: Encounter 4th: Speak: Part 3_SubState"""
        # talk:75201700:"Loss frightens me no end.\nLoss of memory, loss of self."
        assert talk_m10_16_x0(text26=75201700, z43=203632, z44=0)
        """State 3: 4th encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203630) != 0:
        """State 6: Encounter 4th: Speak: Part 2: 1_SubState"""
        # talk:75201600:"What is this curse?"
        assert talk_m10_16_x0(text26=75201600, z43=0, z44=0)
        """State 9: Encounter 4th: Speak: Part 2: 2_SubState"""
        # talk:75201610:"The question rings in my mind,\nbut I haven't the focus to answer it."
        assert talk_m10_16_x1(text1=75201610, z29=203631, z41=-1, z42=0)
        Goto('L0')
    else:
        """State 5: Encounter 4th: Speak: Part 1_SubState"""
        # talk:75201500:"Oh... You..."
        assert talk_m10_16_x0(text26=75201500, z43=203630, z44=0)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_16_x30(z1=60, action1=1335, action2=1345, z2=116020127):
    """[Lib] Kanemori: Conversation
    z1: Current pledge rank: Area variable
    action1: Pledge text
    action2: Overwriting pledge text
    z2: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetPlayerCovenant() == 6) != 0:
        """State 4: Kanemori: Pledge conversation_SubState"""
        assert talk_m10_16_x32(z1=z1)
    elif GetEventFlag(200905) != 0:
        """State 5: Kanemori: Re-pledge conversation_SubState"""
        assert talk_m10_16_x33(action1=action1, action2=action2, z2=z2)
    else:
        """State 3: Kanemori: Unpowed conversation_SubState"""
        assert talk_m10_16_x31(action1=action1, action2=action2, z2=z2)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_16_x31(action1=1335, action2=1345, z2=116020127):
    """Kanemori: Unpowed conversation
    action1: Pledge text
    action2: Overwriting pledge text
    z2: For trophies: Area and other flags
    """
    """State 0,1: Unpowed conversation: Start"""
    if GetEventFlag(203701) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:75300200:"Hah hah hah, ooh hoo hoo!"
        assert talk_m10_16_x0(text26=75300200, z43=0, z44=0)
        """State 6: [Lib] Pledge conclusion: General purpose_SubState"""
        # lot:0:No Item
        call = talk_m10_16_x38(val1=6, z3=8, lot1=0, flag1=0, action1=action1, action2=action2, z2=z2)
        if call.Get() == 1:
            """State 7: Speak: Part 3: YES_SubState"""
            # lot:1753020:Bell Keeper's Seal, talk:75300300:"Hah hah, heh! Here, for you!", talk:75300310:"When you're 'round the bell,\nyou'll be brought near!"
            assert (talk_m10_16_x23(lot3=1753020, flag3=102511, text2=75300300, text3=75300310, z6=0,
                    z7=0))
        elif call.Get() == 0:
            """State 5: Speak: Part 3: NO_SubState"""
            # talk:75300400:"Gah hah hah hah hah!"
            assert talk_m10_16_x1(text1=75300400, z29=0, z41=-1, z42=0)
    elif GetEventFlag(203700) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:75300100:"A long, long, long time ago,\nthe Princess, she made me, yes, just like so!"
        assert talk_m10_16_x0(text26=75300100, z43=203701, z44=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:75300000:"Undead! Undead!"
        assert talk_m10_16_x0(text26=75300000, z43=203700, z44=0)
    """State 8: End state"""
    return 0

def talk_m10_16_x32(z1=60):
    """Kanemori: Pledge conversation
    z1: Current pledge rank: Area variable
    """
    """State 0,1: Pledge conversation: start"""
    SetAreaVariable(z1, GetPlayerCovenantLevel(6))
    if GetEventFlag(102511) != 1:
        """State 10: When ring is not transferred: Insurance_SubState"""
        # lot:1753020:Bell Keeper's Seal, talk:75300300:"Hah hah, heh! Here, for you!", talk:75300310:"When you're 'round the bell,\nyou'll be brought near!"
        assert (talk_m10_16_x20(lot5=1753020, flag8=102511, text5=75300300, text6=75300310, z11=0, z8=0,
                z12=0, z13=0))
    elif (GetEventFlag(102510) != 1 and (PhantomMultiplayerCount(11) > NpcInfoValue(7530, 0)) != 0 and
          GetEventFlag(104200) != 1):
        """State 4: Equipment transfer (Condition: Achieved Summon Phantom Summon) _SubState"""
        # lot:1753000:Rusted Coin, talk:75306000:"Forever...for true!"
        assert (talk_m10_16_x20(lot5=1753000, flag8=102510, text5=75306000, text6=75306020, z11=0, z8=0,
                z12=0, z13=0))
    else:
        """State 6: [Lib] Pledge: Rank up: Conversation_SubState"""
        call = talk_m10_16_x40(z24=6, z1=z1, z25=215, flag10=102512, flag11=102513, flag12=102514)
        if call.Get() == 1:
            """State 3: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z1) > 1) != 0 and GetEventFlag(102512) != 1:
                """State 7: Conversation: Pledge Ranking 1_SubState"""
                # talk:75300700:"Gah hah! Hah hah hah!", lot:2004011:Titanite Slab
                assert talk_m10_16_x16(text9=75300700, z15=0, lot7=2004011, flag9=102512, z16=215, z1=z1)
                Goto('L0')
            elif (GetAreaVariable(z1) > 2) != 0 and GetEventFlag(102513) != 1:
                """State 8: Conversation: Pledge Ranking 2_SubState"""
                # talk:75300800:"Bravo, my friend, look how they've bled!", lot:2004012:Hidden Weapon
                assert talk_m10_16_x16(text9=75300800, z15=0, lot7=2004012, flag9=102513, z16=215, z1=z1)
                Goto('L0')
            elif (GetAreaVariable(z1) > 3) != 0 and GetEventFlag(102514) != 1:
                """State 9: Conversation: Pledge Ranking 3_SubState"""
                # talk:75300900:"Hah! Haaaah!", lot:2004013:Bell Keeper Helmet
                assert talk_m10_16_x16(text9=75300900, z15=0, lot7=2004013, flag9=102514, z16=215, z1=z1)
                Goto('L0')
            else:
                pass
        elif call.Get() == 0:
            pass
        """State 5: When pledged: Talk: Part 1_SubState"""
        # talk:75300600:"Ah hah hah! The Princess made me!\nTo guard the Bell of Alken!"
        assert talk_m10_16_x0(text26=75300600, z43=0, z44=0)
    """State 2: Pledge conversation: End"""
    Label('L0')
    ClearNpcMenuSelection()
    """State 11: End state"""
    return 0

def talk_m10_16_x33(action1=1335, action2=1345, z2=116020127):
    """Kanemori: Re-pledge conversation
    action1: Pledge text
    action2: Overwriting pledge text
    z2: For trophies: Area and other flags
    """
    """State 0,1,3: Re-pledge: Talk: Part 1_SubState"""
    # talk:75300500:"You want to guard the bell, do you?"
    assert talk_m10_16_x0(text26=75300500, z43=0, z44=0)
    """State 6: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item
    call = talk_m10_16_x38(val1=6, z3=8, lot1=0, flag1=0, action1=action1, action2=action2, z2=z2)
    if call.Get() == 0:
        """State 5: Speak: Part 3: NO_SubState"""
        # talk:75300400:"Gah hah hah hah hah!"
        assert talk_m10_16_x1(text1=75300400, z29=0, z41=-1, z42=0)
    elif call.Get() == 1 and GetEventFlag(102511) != 1:
        """State 7: When ring is not transferred: Insurance_SubState"""
        # lot:1753020:Bell Keeper's Seal, talk:75300300:"Hah hah, heh! Here, for you!", talk:75300310:"When you're 'round the bell,\nyou'll be brought near!"
        assert (talk_m10_16_x20(lot5=1753020, flag8=102511, text5=75300300, text6=75300310, z11=0, z8=0,
                z12=0, z13=0))
    elif call.Get() == 1:
        """State 4: Laughter_SubState"""
        assert talk_m10_16_x1(text1=75306020, z29=0, z41=-1, z42=0)
    """State 2: Re-pow conversation: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m10_16_x34(val2=6):
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

def talk_m10_16_x35(text12=_, z26=0, z27=20, z28=80):
    """[Lib] Conversation: Hostile display only
    text12: Conversation ID
    z26: Conversation flag
    z27: Display distance
    z28: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text12, GetCommonEventParamDecimal(7), z27)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z26, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_16_x36(action3=1200, goods1=50990000):
    """[Lib] Selection dialog: Item display
    action3: Dialog: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    # action:1200:"Give\n%s?", goods:50990000:Dull Ember
    DisplayOwnYesNoMenu(action3, 0, -1, 2, goods1, 0)
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

def talk_m10_16_x37(z19=63019000, z20=0):
    """[Lib] Menu item: Gesture
    z19: Gesture: Item ID
    z20: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_16_x42(z19=z19, z20=z20)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_16_x38(val1=6, z3=8, lot1=0, flag1=0, action1=1335, action2=1345, z2=116020127):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z3: Event action
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z2: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z2, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_16_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_16_x17(action4=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_16_x39(z3=z3, val1=val1, lot1=lot1, flag1=flag1) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_16_x17(action4=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_16_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_16_x34(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_16_x39(z3=8, val1=6, lot1=0, flag1=0):
    """[Lib] Event action: Pledge
    z3: Event action
    val1: Pledge type
    lot1: Item lottery ID
    flag1: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z3)
    assert PlayerIsInEventAction(z3) != 0
    """State 3: IventAction: Motion_Waiting"""
    # lot:0:No Item
    if PlayerIsInEventAction(z3) != 1 and CanGetItemLot(lot1, 1) != 1 and GetEventFlag(flag1) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        # lot:0:No Item
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot1, 1) != 1 and GetEventFlag(flag1) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_16_x44(z17=1011, lot1=lot1)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z3) != 1 and GetEventFlag(flag1) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z3) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(flag1, 1)
        # lot:0:No Item
        AwardItem(lot1, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z3) != 1
    """State 8: End state"""
    return 0

def talk_m10_16_x40(z24=6, z1=60, z25=215, flag10=102512, flag11=102513, flag12=102514):
    """[Lib] Pledge: Rank up: Conversation: 1
    z24: Pledge: Pledge type
    z1: Current rank: Area variable
    z25: Previous rank: Global variable
    flag10: Ranking 1: Item transfer: Global event flag
    flag11: Ranking 2: Item transfer: Global event flag
    flag12: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z1, GetPlayerCovenantLevel(z24))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z25) > GetAreaVariable(z1)) != 1 and (GetGlobalVariable(z25) == GetAreaVariable(z1))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z25) > GetAreaVariable(z1)) != 0 and (GetGlobalVariable(z25) == GetAreaVariable(z1))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z25, GetAreaVariable(z1))
    elif GetEventFlag(flag10) != 1 and (GetGlobalVariable(z25) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(flag11) != 1 and (GetGlobalVariable(z25) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(flag12) != 1 and (GetGlobalVariable(z25) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_16_x41(text11=_, z21=_, z22=9901, z23=-1):
    """[Lib] Conversation: For unique key guide
    text11: Conversation ID
    z21: Conversation flag
    z22: Key guide parameters
    z23: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z22)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text11, GetCommonEventParamDecimal(7), z23)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z21, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_16_x42(z19=63019000, z20=0):
    """[Lib] Get gesture dialog
    z19: Item ID
    z20: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(z19, 0, -1)
    SetEventFlag(z20, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_16_x43(text10=75309600, z18=0, val2=6):
    """[Lib] Death status_ (pledge cancellation)
    text10: Conversation ID
    z18: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_16_x34(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_16_x2(text10=text10, z18=z18)
    Quit()
    """Unused"""
    """State 5: End state"""
    return 0

def talk_m10_16_x44(z17=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z17: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_16_x45():
    """Spel Mania: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Conversation: branch"""
    if GetEventFlag(204901) != 0:
        """State 5: Spell mania: Status above a certain level_SubState"""
        assert talk_m10_16_x47()
        """State 6: Spell mania: NPC menu_SubState"""
        Label('L0')
        assert talk_m10_16_x48()
    else:
        """State 4: Spell mania: status below a certain level_SubState"""
        call = talk_m10_16_x46()
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m10_16_x46():
    """Spermia: status below a certain level"""
    """State 0,1: Below a certain level: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(204900) != 1:
        """State 2: Talk: Part 1_SubState"""
        # talk:76800000:"Still a bit stiff, I'm afraid. Heh heh heh..."
        assert talk_m10_16_x0(text26=76800000, z43=204900, z44=0)
    elif ((GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 0 and (GetPlayerStat(6, 1) > NpcInfoValue(7680,
          1)) != 0):
        """State 6: Speak: Part 2: Reason / Faith is above a certain level_SubState"""
        # talk:76800400:"Hm-hmm..."
        assert talk_m10_16_x0(text26=76800400, z43=204901, z44=0)
        """State 9: Menu: Exit state"""
        return 1
    elif ((GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 1 and (GetPlayerStat(6, 1) > NpcInfoValue(7680,
          1)) != 1):
        """State 3: Speak: Part 2: Reason / Faith is below a certain level: 1_SubState"""
        # talk:76800100:"I sense the curse within you."
        call = talk_m10_16_x0(text26=76800100, z43=0, z44=0)
        if call.Done():
            """State 7: Speak: Part 2: Reason / Faith is below a certain level: 2_SubState"""
            # talk:76800110:"It has made you terribly frail."
            call = talk_m10_16_x1(text1=76800110, z29=0, z41=-1, z42=0)
            if call.Done():
                pass
            elif (GetPlayerStat(6, 1) > NpcInfoValue(7680, 1)) != 0:
                pass
            elif (GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 0:
                pass
        elif (GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 0:
            pass
        elif (GetPlayerStat(6, 1) > NpcInfoValue(7680, 1)) != 0:
            pass
    elif (GetPlayerStat(6, 1) > NpcInfoValue(7680, 1)) != 1:
        """State 5: Speak: Part 2: Faith is below a certain level_SubState"""
        # talk:76800300:"Cursed one, you lack faith."
        call = talk_m10_16_x0(text26=76800300, z43=0, z44=0)
        if call.Done():
            pass
        elif (GetPlayerStat(6, 1) > NpcInfoValue(7680, 1)) != 0:
            pass
        elif ((GetPlayerStat(6, 1) > NpcInfoValue(7680, 1)) != 0 and (GetPlayerStat(5, 1) > NpcInfoValue(7680,
              0)) != 0):
            pass
    elif (GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 1:
        """State 4: Speak: Part 2: Reason is below a certain level_SubState"""
        # talk:76800200:"Cursed one, you lack intelligence."
        call = talk_m10_16_x0(text26=76800200, z43=0, z44=0)
        if call.Done():
            pass
        elif (GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 0:
            pass
        elif ((GetPlayerStat(5, 1) > NpcInfoValue(7680, 0)) != 0 and (GetPlayerStat(6, 1) > NpcInfoValue(7680,
              1)) != 0):
            pass
    """State 8: Normal: End state"""
    return 0

def talk_m10_16_x47():
    """Spermia: Status above a certain level"""
    """State 0,1: Above a certain level: Start"""
    GenerateRandomNumber(0, 0, 30)
    """State 3: Above a certain level: Owned item judgment"""
    # goods:64050000:Ruin Sentinel Soul
    if (ItemCount(64050000, 1, 1, 0) > 1) != 0:
        """State 4: Above a certain level: Message branching"""
        Label('L0')
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Menu: Start conversation: Item possession 3_SubState"""
            # talk:76801000:"Well! This is a most twisted soul."
            assert talk_m10_16_x0(text26=76801000, z43=204912, z44=0)
        elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 20) != 0:
            """State 7: Menu: Start conversation: Item possession 2_SubState"""
            # talk:76800900:"Well! This is a most charming soul."
            assert talk_m10_16_x0(text26=76800900, z43=204911, z44=0)
        else:
            """State 6: Menu: Start conversation: Item possession 1_SubState"""
            # talk:76800800:"Well! This is a most peculiar soul."
            assert talk_m10_16_x0(text26=76800800, z43=204910, z44=0)
    # goods:64130000:Royal Rat Vanguard Soul
    elif (ItemCount(64130000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64150000:Scorpioness Najka Soul
    elif (ItemCount(64150000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64160000:Royal Rat Authority Soul
    elif (ItemCount(64160000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64200000:Soul of Velstadt
    elif (ItemCount(64200000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64240000:Giant Lord Soul
    elif (ItemCount(64240000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64280000:Darklurker Soul
    elif (ItemCount(64280000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64300000:Old Witch Soul
    elif (ItemCount(64300000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64310000:Old King Soul
    elif (ItemCount(64310000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64320000:Old Dead One Soul
    elif (ItemCount(64320000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:64330000:Old Paledrake Soul
    elif (ItemCount(64330000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    else:
        """State 5: Menu: Start conversation_SubState"""
        # talk:76800500:"Souls! I need souls!\nYou cursed fool!"
        assert talk_m10_16_x0(text26=76800500, z43=0, z44=0)
    """State 2,9: End state"""
    return 0

def talk_m10_16_x48():
    """Spermania: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 3: Menu: Branch"""
        # goods:63019000:"Mock" Gesture
        if (ItemCount(63019000, 1, 1, 0) > 1) != 0:
            """State 9: [Lib] Menu start: No gesture _SubState"""
            call = talk_m10_16_x12(z32=0, z33=220, z34=76800001, z35=0)
            if call.Get() == 2:
                """State 7: Spermia: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_16_x49()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 5: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:76800600:"Feeble cursed one!", talk:76800700:"Feeble cursed one!"
                assert talk_m10_16_x13(text15=76800600, text16=76800700)
        else:
            """State 4: [Lib] Menu start: With gesture_SubState"""
            call = talk_m10_16_x12(z32=0, z33=220, z34=76800000, z35=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 8: [Lib] Menu item: Gesture_SubState"""
                call = talk_m10_16_x37(z19=63019000, z20=0)
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
    # talk:76802000:"Don't just walk off, cursed one. Heh heh..."
    assert talk_m10_16_x14(text14=76802000)
    Goto('L2')

def talk_m10_16_x49():
    """Spelmania: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102740) != 1 and (GetGlobalVariable(223) > 4) != 0 and GetEventFlag(104310) != 1:
        """State 10: Equipment transfer (conditions: barter exchanges) _SubState"""
        # lot:1768000:Black Hood, talk:76806000:"Weak, so terribly weak..."
        assert talk_m10_16_x18(lot6=1768000, z14=102740, text7=76806000, text8=76806010)
    elif GetEventFlag(204925) != 0:
        """State 3: Menu conversation: initialization settings"""
        SetEventFlag(204924, 0)
        SetEventFlag(204923, 0)
        SetEventFlag(204922, 0)
        SetEventFlag(204921, 0)
        SetEventFlag(204920, 0)
        SetEventFlag(204925, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76805000:"Weak, so terribly weak..."
        assert talk_m10_16_x1(text1=76805000, z29=204920, z41=-1, z42=0)
    elif GetEventFlag(204924) != 0:
        """State 9: Menu conversation: 6_SubState"""
        assert talk_m10_16_x1(text1=76805500, z29=204925, z41=-1, z42=0)
    elif GetEventFlag(204923) != 0:
        """State 8: Menu conversation: 5_SubState"""
        assert talk_m10_16_x1(text1=76805400, z29=204924, z41=-1, z42=0)
    elif GetEventFlag(204922) != 0:
        """State 7: Menu conversation: 4_SubState"""
        assert talk_m10_16_x1(text1=76805300, z29=204923, z41=-1, z42=0)
    elif GetEventFlag(204921) != 0:
        """State 6: Menu conversation: 3_SubState"""
        assert talk_m10_16_x1(text1=76805200, z29=204922, z41=-1, z42=0)
    elif GetEventFlag(204920) != 0:
        """State 5: Menu conversation: 2_SubState"""
        assert talk_m10_16_x1(text1=76805100, z29=204921, z41=-1, z42=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 11: End state"""
    return 0

def talk_m10_16_x50():
    """EX Blacksmith: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102680) != 0:
        """State 3: EX Blacksmith: Conversation with Fire_SubState"""
        assert talk_m10_16_x52()
        """State 4: EX Blacksmith: NPC Menu_SubState"""
        Label('L0')
        assert talk_m10_16_x53()
    else:
        """State 5: EX Blacksmith: No Fire Conversation_SubState"""
        call = talk_m10_16_x51()
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_16_x51():
    """EX Blacksmith: No Fire"""
    """State 0,1: No fire: Start"""
    # goods:50990000:Dull Ember
    if (ItemCount(50990000, 1, 1, 0) > 1) != 0 and GetEventFlag(204602) != 0:
        """State 7: Talk: Part 4: Fire _SubState"""
        # talk:76430400:"Flame flame...I smell flame upon you."
        assert talk_m10_16_x0(text26=76430400, z43=0, z44=0)
        """State 10: Fireworks transfer selection dialog_SubState"""
        # action:1200:"Give\n%s?", goods:50990000:Dull Ember
        call = talk_m10_16_x36(action3=1200, goods1=50990000)
        if call.Get() == 1:
            """State 8: Speak: Part 4: Fire: NO_SubState"""
            Label('L0')
            # talk:76430600:"What?!"
            assert talk_m10_16_x1(text1=76430600, z29=0, z41=-1, z42=0)
        elif call.Get() == 2:
            Goto('L0')
        elif call.Get() == 0:
            """State 2: No fire: Set fire reception flag"""
            # goods:50990000:Dull Ember
            ConsumeItem(50990000, 1)
            SetEventFlag(102680, 1)
            """State 9: Talk: Part 4: Fire: YES: 1_SubState"""
            # talk:76430500:"Oh-hoh! What a marvellous ember!"
            assert talk_m10_16_x1(text1=76430500, z29=0, z41=-1, z42=0)
            """State 11: Speak: Part 4: Fire: YES: 2_SubState"""
            # talk:76430510:"You've got stones, I pray."
            assert talk_m10_16_x1(text1=76430510, z29=0, z41=-1, z42=0)
            """State 13: Menu: Exit state"""
            return 1
    elif GetEventFlag(204602) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:76430300:"I ought to fetch a new ember..."
        assert talk_m10_16_x0(text26=76430300, z43=0, z44=0)
    elif GetEventFlag(204601) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:76430200:"Oh-hoh hoh hoh! That's it, yes, that's the way!"
        assert talk_m10_16_x0(text26=76430200, z43=204602, z44=0)
    elif GetEventFlag(204600) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:76430100:"Hmph! Hmm! We've got a wild one here!"
        assert talk_m10_16_x0(text26=76430100, z43=204601, z44=0)
    else:
        """State 3: Talk: Part 1_SubState"""
        # talk:76430000:"Meh heh heh..."
        assert talk_m10_16_x0(text26=76430000, z43=204600, z44=0)
    """State 12: Normal: End state"""
    return 0

def talk_m10_16_x52():
    """EX Blacksmith: Conversation with Fire"""
    """State 0,1,2: Talk: 4_SubState"""
    # talk:76430300:"I ought to fetch a new ember..."
    assert talk_m10_16_x0(text26=76430300, z43=0, z44=0)
    """State 3: End state"""
    return 0

def talk_m10_16_x53():
    """EX Blacksmith: NPC Menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 3: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_16_x12(z32=0, z33=220, z34=76430000, z35=0)
        if call.Get() == 2:
            """State 6: EX Blacksmith: Menu conversation_SubState"""
            call = talk_m10_16_x54()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Exit menu: General purpose_SubState"""
            # talk:76430700:"Flame, dear flame...", talk:76430800:"Be gone."
            assert talk_m10_16_x13(text15=76430700, text16=76430800)
            """State 2: Menu: Exit"""
            ClearNpcMenuSelection()
        """State 7: End state"""
        Label('L0')
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76430700:"Flame, dear flame..."
    assert talk_m10_16_x14(text14=76430700)
    Goto('L0')

def talk_m10_16_x54():
    """EX Blacksmith: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102681) != 1 and (GetGlobalVariable(226) > NpcInfoValue(7643, 1)) != 0 and GetEventFlag(104290)
        != 1):
        """State 7: Equipment transfer (Conditions: total equipment enhancement / attribute change usage) _SubState"""
        # lot:1764300:Titanite Slab, talk:76436000:"Flame, dear flame..."
        assert talk_m10_16_x24(lot2=1764300, flag2=102681, text1=76436000, z4=0, z5=116020148)
    elif GetEventFlag(204612) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(204610, 0)
        SetEventFlag(204611, 0)
        SetEventFlag(204612, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76435000:"You've offended the flames!"
        assert talk_m10_16_x1(text1=76435000, z29=204610, z41=-1, z42=0)
    elif GetEventFlag(204611) != 0:
        """State 6: Menu conversation: 3_SubState"""
        assert talk_m10_16_x1(text1=76435200, z29=204612, z41=-1, z42=0)
    elif GetEventFlag(204610) != 0:
        """State 5: Menu conversation: 2_SubState"""
        assert talk_m10_16_x1(text1=76435100, z29=204611, z41=-1, z42=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m10_16_x55():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(100761) != 0 and GetEventFlag(208001) != 0:
        """State 6: [Lib] Conversation: Talk to 3_SubState"""
        # talk:69200200:"Young Hollow, seek after Vendrick."
        assert talk_m10_16_x41(text11=69200200, z21=0, z22=9901, z23=-1)
        """State 3: End encounter flag"""
        SetEventFlag(100740, 1)
    elif GetEventFlag(100761) != 0 and GetEventFlag(208000) != 0:
        """State 5: [Lib] Conversation: Talk to 2_SubState"""
        # talk:69200100:"Young Hollow, there are but two paths.\nInherit the order of this world, or destroy it."
        assert talk_m10_16_x41(text11=69200100, z21=208001, z22=9901, z23=-1)
    elif GetEventFlag(100761) != 0:
        """State 4: [Lib] Conversation: Talk to 1_SubState"""
        # talk:69200010:"No one has come this far,\nnot for a very long while."
        assert talk_m10_16_x41(text11=69200010, z21=208000, z22=9901, z23=-1)
    """State 2,7: End state"""
    return 0

def talk_m10_16_4100000():
    """Andyel"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(100740) != 0:
            break
        else:
            """State 3: Anne Deal_SubState"""
            assert talk_m10_16_x55()
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

