# -*- coding: utf-8 -*-
def talk_m10_14_7420():
    """Wandering Warrior: Combat Event (Pyrox Street Gerdra)"""
    """State 0,1: Conversation: Start"""
    Label('L0')
    ResetDamageTakenCountIf(GetEventFlag(114000150) != 0 and GetEventFlag(103653) != 1)
    SetEventFlagIf(GetEventFlag(114000150) != 0 and GetEventFlag(103653) != 1, 114000152, 0)
    if IsGuest() != 0:
        """State 5: Conversation: System: End"""
        EndMachine()
        Quit()
    elif GetEventFlag(104153) != 0:
        pass
    elif GetEventFlag(102402) != 0:
        pass
    else:
        """State 14: Wandering & Patch: Battle Event_SubState"""
        # talk:74401200:"He swung at me!\nPlease, lend me a hand!"
        call = talk_m10_14_x51(text1=74401200, z7=104170, z8=114020117, z9=10000010)
        if call.Done():
            """State 4: Conversation: Battle event: Waiting for completion"""
            Label('L1')
            if (HpValue() > 1) != 1 and GetEventFlag(114020117) != 1 and (NumberOfTimesDamaged(1) > 1) != 0:
                pass
            elif (GetEventFlag(114020117) != 1 and (NumberOfTimesDamaged(1) > 1) != 0 and ConversationEnded()
                  != 0):
                pass
            elif GetEventFlag(114000140) != 0:
                """State 2: Conversation: Initialize damage count"""
                ResetDamageTakenCount()
                Goto('L2')
        elif (HpValue() > 1) != 1 and GetEventFlag(114020117) != 1 and (NumberOfTimesDamaged(1) > 1) != 0:
            pass
        elif GetEventFlag(114020117) != 1 and (NumberOfTimesDamaged(1) > 1) != 0 and ConversationEnded() != 0:
            pass
        """State 6: Battle Event: Damaged by player"""
        SetEventFlag(114020117, 1)
        Goto('L1')
    while True:
        """State 7: [Lib] Event: Branch_SubState"""
        Label('L2')
        call = talk_m10_14_x9(z54=103653, z55=104150, z56=114020111)
        if call.Get() == 1:
            """State 8: [Lib] Reunion hostility_SubState"""
            call = talk_m10_14_x3(text16=74209200, z41=0, z42=20, z43=80)
            if call.Done():
                """State 15: [Lib] Hostile state_ (Gerdra) _SubState"""
                Label('L3')
                call = talk_m10_14_x27(z30=114020112, text11=74209500, text12=74209500, z31=74209500,
                                       z32=114000150)
                if GetEventFlag(103653) != 1 and GetEventFlag(103999) != 1:
                    """State 3: Conversation: Hostility: Initialization"""
                    SetEventFlag(114020112, 0)
                    SetEventFlag(114000114, 0)
                    SetEventFlag(114020115, 0)
                    SetEventFlag(114020116, 0)
                    continue
                elif KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 10: [Lib] Death state_SubState"""
                    Label('L4')
                    talk_m10_14_x7(text27=74209600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L4')
        elif call.Get() == 0:
            while True:
                """State 13: Wandering Warrior: Conversation_SubState"""
                call = talk_m10_14_x40()
                if call.Done():
                    Goto('L0')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L4')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 11: [Lib] Hostile waiting_SubState"""
                    Label('L5')
                    call = talk_m10_14_x5(text28=74209400, text29=74209410, text30=74209420, text31=74209400,
                                          z59=114020115, z60=114020116)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L4')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 12: [Lib] First adversification_SubState"""
                        call = talk_m10_14_x4(z61=103650, text32=74209100, z62=0, z63=103653)
                        if call.Done():
                            Goto('L3')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L4')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(114020116) != 1:
                    Goto('L5')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(114020115) != 1:
                    Goto('L5')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_14_x8(text26=74209300, z57=0)
        Quit()

def talk_m10_14_7421():
    """Wandering Warrior: Patch Dead (Pyrox Street Gerdra)"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        Label('L0')
        ResetDamageTakenCountIf(GetEventFlag(114000150) != 0 and GetEventFlag(103653) != 1)
        SetEventFlagIf(GetEventFlag(114000150) != 0 and GetEventFlag(103653) != 1, 114000152, 0)
        if IsGuest() != 0:
            """State 3: Conversation: System: End"""
            EndMachine()
            Quit()
        else:
            break
    while True:
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_14_x9(z54=103653, z55=104150, z56=114020111)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_14_x3(text16=74209200, z41=0, z42=20, z43=80)
            if call.Done():
                """State 12: [Lib] Hostile state_ (Gerdra) _SubState"""
                Label('L1')
                call = talk_m10_14_x27(z30=114020112, text11=74209500, text12=74209500, z31=74209500,
                                       z32=114000150)
                if GetEventFlag(103653) != 1 and GetEventFlag(103999) != 1:
                    """State 2: Conversation: Hostility: Initialization"""
                    SetEventFlag(114020112, 0)
                    SetEventFlag(114000114, 0)
                    SetEventFlag(114020115, 0)
                    SetEventFlag(114020116, 0)
                    continue
                elif KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L2')
                    talk_m10_14_x7(text27=74209600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L2')
        elif call.Get() == 0:
            while True:
                """State 10: Wandering Warrior: Conversation: Patch Death_SubState"""
                call = talk_m10_14_x43()
                if call.Get() == 1:
                    """State 11: [Lib] First adversification_ (No Mes) _SubState"""
                    call = talk_m10_14_x21(z44=103650, z45=103653)
                    if call.Done():
                        Goto('L1')
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L2')
                elif call.Get() == 0:
                    Goto('L0')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 8: [Lib] Hostile waiting_SubState"""
                    Label('L3')
                    call = talk_m10_14_x5(text28=74209400, text29=74209410, text30=74209420, text31=74209400,
                                          z59=114020115, z60=114020116)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L2')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_14_x4(z61=103650, text32=74209100, z62=0, z63=103653)
                        if call.Done():
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(114020116) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(114020115) != 1:
                    Goto('L3')
        """State 6: [Lib] Killing state_SubState"""
        talk_m10_14_x8(text26=74209300, z57=0)
        Quit()

def talk_m10_14_7440():
    """Patch (Pyrox Street Gerdola)"""
    """State 0,1: Conversation: Start"""
    Label('L0')
    ResetDamageTakenCountIf(GetEventFlag(114000151) != 0 and GetEventFlag(103673) != 1)
    SetEventFlagIf(GetEventFlag(114000151) != 0 and GetEventFlag(103673) != 1, 114000152, 0)
    if IsGuest() != 0:
        """State 5: Conversation: System: End"""
        EndMachine()
        Quit()
    elif GetEventFlag(104173) != 0:
        pass
    elif GetEventFlag(102445) != 0:
        pass
    else:
        """State 14: Wandering & Patch: Battle Event_SubState"""
        # talk:74201000:"Damn! You're tougher than you look!"
        call = talk_m10_14_x51(text1=74201000, z7=104150, z8=114020127, z9=10000020)
        if call.Done():
            """State 4: Conversation: Battle event: Waiting for completion"""
            Label('L1')
            if GetEventFlag(114020127) != 1 and (HpValue() > 1) != 1 and (NumberOfTimesDamaged(1) > 1) != 0:
                pass
            elif (GetEventFlag(114020127) != 1 and (NumberOfTimesDamaged(1) > 1) != 0 and ConversationEnded()
                  != 0):
                pass
            elif GetEventFlag(114000140) != 0:
                """State 2: Conversation: Initialize damage count"""
                ResetDamageTakenCount()
                Goto('L2')
        elif GetEventFlag(114020127) != 1 and (HpValue() > 1) != 1 and (NumberOfTimesDamaged(1) > 1) != 0:
            pass
        elif GetEventFlag(114020127) != 1 and (NumberOfTimesDamaged(1) > 1) != 0 and ConversationEnded() != 0:
            pass
        """State 6: Conversation: Damaged by player"""
        SetEventFlag(114020127, 1)
        Goto('L1')
    while True:
        """State 7: [Lib] Event: Branch_SubState"""
        Label('L2')
        call = talk_m10_14_x9(z54=103673, z55=104170, z56=114020121)
        if call.Get() == 1:
            """State 8: [Lib] Reunion hostility_SubState"""
            call = talk_m10_14_x3(text16=74409200, z41=0, z42=20, z43=80)
            if call.Done():
                """State 15: [Lib] Hostile state_ (Gerdra) _SubState"""
                Label('L3')
                call = talk_m10_14_x27(z30=114020122, text11=74409500, text12=74409500, z31=74409500,
                                       z32=114000151)
                if GetEventFlag(103673) != 1 and GetEventFlag(103999) != 1:
                    """State 3: Conversation: Hostility: Initialization"""
                    SetEventFlag(114020122, 0)
                    SetEventFlag(114000124, 0)
                    SetEventFlag(114020125, 0)
                    SetEventFlag(114020126, 0)
                    continue
                elif KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 10: [Lib] Death state_SubState"""
                    Label('L4')
                    talk_m10_14_x7(text27=74409600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L4')
        elif call.Get() == 0:
            while True:
                """State 13: Patch: Conversation_SubState"""
                call = talk_m10_14_x44()
                if call.Done():
                    Goto('L0')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L4')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 11: [Lib] Hostile waiting_SubState"""
                    Label('L5')
                    call = talk_m10_14_x5(text28=74409400, text29=74409410, text30=74409420, text31=74409400,
                                          z59=114020125, z60=114020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L4')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 12: [Lib] First adversification_SubState"""
                        call = talk_m10_14_x4(z61=103670, text32=74409100, z62=0, z63=103673)
                        if call.Done():
                            Goto('L3')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L4')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(114020126) != 1:
                    Goto('L5')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(114020125) != 1:
                    Goto('L5')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_14_x8(text26=74409300, z57=0)
        Quit()

def talk_m10_14_7760():
    """Upper weapon shop (Pyrox Street)"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        Label('L0')
        ResetDamageTakenCountIf(GetEventFlag(114000152) != 0 and GetEventFlag(103862) != 1)
        SetEventFlagIf(GetEventFlag(114000152) != 0 and GetEventFlag(103862) != 1, 114000152, 0)
        if IsGuest() != 0:
            """State 3: Conversation: System: End"""
            EndMachine()
            Quit()
        else:
            break
    while True:
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_14_x9(z54=103862, z55=104360, z56=114020131)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            # talk:77505010:"You again?"
            call = talk_m10_14_x3(text16=77505010, z41=0, z42=20, z43=80)
            if call.Done():
                """State 11: [Lib] Hostile state_ (Gerdra) _SubState"""
                Label('L1')
                # talk:77505060:""
                call = talk_m10_14_x27(z30=114020132, text11=77505060, text12=77505060, z31=77505060,
                                       z32=114000152)
                if GetEventFlag(103862) != 1 and GetEventFlag(103999) != 1:
                    """State 2: Conversation: Hostility: Initialization"""
                    SetEventFlag(114020132, 0)
                    SetEventFlag(114020134, 0)
                    SetEventFlag(114020135, 0)
                    SetEventFlag(114020136, 0)
                    continue
                elif KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L2')
                    # talk:77505070:"You humans are all alike..."
                    talk_m10_14_x7(text27=77505070, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L2')
        elif call.Get() == 0:
            while True:
                """State 10: Higher weapon shop: Conversation_SubState"""
                call = talk_m10_14_x45()
                if call.Done():
                    Goto('L0')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 8: [Lib] Hostile waiting_SubState"""
                    Label('L3')
                    # talk:77505030:"Skwaa!", talk:77505040:"What are you...!", talk:77505050:"Stop this!"
                    call = talk_m10_14_x5(text28=77505030, text29=77505040, text30=77505050, text31=77505030,
                                          z59=114020135, z60=114020136)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L2')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        # talk:77505000:"Oh, as you please..."
                        call = talk_m10_14_x4(z61=103860, text32=77505000, z62=0, z63=103862)
                        if call.Done():
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(114020136) != 1:
                    Goto('L3')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(114020135) != 1:
                    Goto('L3')
        """State 6: [Lib] Killing state_SubState"""
        # talk:77505020:"What a bother."
        talk_m10_14_x8(text26=77505020, z57=0)
        Quit()

def talk_m10_14_7840():
    """Inexorable teacher"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_14_x9(z54=103890, z55=104390, z56=114020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_14_x3(text16=78409200, z41=0, z42=20, z43=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_14_x6(z52=114020102, text24=78409500, text25=78409500, z53=78409500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_14_x7(text27=78409600, z58=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: Immoral Teacher: Conversation_SubState"""
                call = talk_m10_14_x33()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_14_x5(text28=78409400, text29=78409400, text30=78409400, text31=78409400,
                                          z59=114020105, z60=114020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_14_x4(z61=103890, text32=78409100, z62=0, z63=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(114020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(114020105) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_14_x8(text26=78409300, z57=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_14_9000():
    """Trap conversation"""
    """State 0,1: Trap conversation: start"""
    if IsGuest() != 0:
        pass
    elif CompareObjStateId(10145070, 83, 0) and GetEventFlag(203250) != 1:
        """State 2: Trap conversation: Branch"""
        if GetEventFlag(104170) != 1:
            """State 6: When the patch is alive: Treasure chest blast_SubState"""
            # talk:74401600:"Ooh, that'll leave a nice scar!"
            assert talk_m10_14_x1(text1=74401600, z62=203250, z64=30, z65=0)
        elif GetEventFlag(104150) != 1:
            """State 5: Wandering Survival: Treasure Box Explosion_SubState"""
            # talk:74202100:"Ooh, that'll leave a nasty scar!"
            assert talk_m10_14_x1(text1=74202100, z62=203250, z64=30, z65=0)
        """State 4: Trap conversation: Delete character"""
        DeleteEnemyByGeneratorGroup(60, 0)
    """State 3: Trap conversation: System: End"""
    EndMachine()

def talk_m10_14_x0(text20=_, z66=_, z67=0):
    """[Lib] Conversation: General purpose
    text20: Conversation ID
    z66: Conversation flag
    z67: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text20, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z66, 1)
    SetEventFlag(z67, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_14_x1(text1=_, z62=_, z64=_, z65=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z62: Conversation flag
    z64: Display distance
    z65: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z64)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z62, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_14_x2(text26=_, z57=0):
    """[Lib] Conversation: Event end
    text26: Conversation ID
    z57: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text26, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z57, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_14_x3(text16=_, z41=0, z42=20, z43=80):
    """[Lib] Reunion hostility
    text16: Conversation message ID
    z41: Conversation flag ID
    z42: Display distance
    z43: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_14_x22(text16=text16, z41=z41, z42=z42, z43=z43)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_14_x4(z61=_, text32=_, z62=0, z63=_):
    """[Lib] First hostility
    z61: Hostile: Global event flag
    text32: Conversation ID
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
    assert talk_m10_14_x1(text1=text32, z62=z62, z64=-1, z65=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_14_x5(text28=_, text29=_, text30=_, text31=_, z59=_, z60=_):
    """[Lib] Hostile waiting
    text28: Conversation ID: 1 attacked
    text29: Conversation ID: Attacked 2
    text30: Conversation ID: 3 attacked
    text31: Conversation ID: 4 attacked
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
        assert talk_m10_14_x1(text1=text31, z62=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_14_x1(text1=text30, z62=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_14_x1(text1=text29, z62=0, z64=-1, z65=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_14_x1(text1=text28, z62=0, z64=-1, z65=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_14_x6(z52=114020102, text24=78409500, text25=78409500, z53=78409500):
    """[Lib] Hostile state
    z52: Area and other flags: HP decreased
    text24: Conversation ID: HP drop 1
    text25: Conversation ID: HP drop 2
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
            assert talk_m10_14_x10(text11=text24, z30=z52)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_14_x10(text11=text25, z30=z52)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_14_x10(text11=text25, z30=z52)

def talk_m10_14_x7(text27=_, z58=0):
    """[Lib] Death status
    text27: Conversation ID
    z58: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_14_x2(text26=text27, z57=z58)

def talk_m10_14_x8(text26=_, z57=0):
    """[Lib] Murder status
    text26: Conversation ID
    z57: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_14_x2(text26=text26, z57=z57)

def talk_m10_14_x9(z54=_, z55=_, z56=_):
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

def talk_m10_14_x10(text11=_, z30=_):
    """[Lib] Conversation: HP drop
    text11: Conversation ID
    z30: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text11, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z30, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_14_x11(z51=_, text20=_, text21=_, text22=_, text23=_):
    """[Lib] Conversation: Greeting: General
    z51: Area other flag: Contact flag
    text20: Text ID: Talk to_continuous 1
    text21: Text ID: Talk to_continuous 2
    text22: Text ID: Talk to _After a long time 1
    text23: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z51) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_14_x0(text20=text20, z66=0, z67=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_14_x0(text20=text21, z66=0, z67=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_14_x0(text20=text22, z66=0, z67=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_14_x0(text20=text23, z66=0, z67=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(z51, 1)
    """State 10: End state"""
    return 0

def talk_m10_14_x12(action2=_):
    """[Lib] selection dialog
    action2: Dialog: Text ID
    """
    """State 0,1: Selection dialog: Display"""
    DisplayOwnYesNoMenu(action2, 0, -1, 0, 0, 0)
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

def talk_m10_14_x13(z47=0, z48=220, z49=_, z50=0):
    """[Lib] Menu start: General purpose
    z47: Camera parameter ID
    z48: Target Damipoly ID
    z49: NPC event parameter ID
    z50: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z50, z47, z48, z49)
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

def talk_m10_14_x14(text18=77502200, text19=77501100):
    """[Lib] Menu exit: General purpose
    text18: Conversation ID (at the time of purchase)
    text19: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_14_x1(text1=text18, z62=0, z64=-1, z65=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_14_x1(text1=text19, z62=0, z64=-1, z65=0)
    """State 4: End state"""
    return 0

def talk_m10_14_x15(text17=_):
    """[Lib] Menu cancellation: General purpose
    text17: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_14_x1(text1=text17, z62=0, z64=-1, z65=0)
    """State 4: End state"""
    return 0

def talk_m10_14_x16(action1=_):
    """[Lib] OK dialog
    action1: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action1, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_14_x17(z46=8):
    """[Lib] Event action: General purpose
    z46: Event action
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z46)
    assert PlayerIsInEventAction(z46) != 0
    """State 3: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z46) != 1
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z46) != 1
    """State 5: End state"""
    return 0

def talk_m10_14_x18(lot5=_, z24=_, text9=_, text10=_, z25=0, z26=0, z27=0, z28=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot5: Item lottery ID
    z24: Item transfer: Global event flag
    text9: First half: Conversation ID
    text10: Second half: Conversation ID
    z25: Conversation: Global conversation flag
    z26: Trophy acquisition: Area and other flags
    z27: Emigration permission: Global event flag
    z28: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_14_x1(text1=text9, z62=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z24) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z25, 1)
        SetEventFlag(z27, 1)
        SetEventFlag(z28, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_14_x1(text1=text10, z62=0, z64=-1, z65=0)
    elif call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_14_x29(z29=1011, lot1=lot5)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_14_x19(lot1=lot5, z10=z24, z11=z25, z12=z26, z27=z27, z28=z28)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_14_x19(lot1=_, z10=_, z11=_, z12=0, z27=0, z28=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    z10: Item transfer: Global event flag
    z11: Conversation: Global conversation flag
    z12: Trophy acquisition: Area and other flags
    z27: Emigration permission: Global event flag
    z28: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z28, 1)
    SetEventFlag(z27, 1)
    SetEventFlag(z12, 1)
    SetEventFlag(z11, 1)
    SetEventFlag(z10, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_14_x20(lot4=1784000, z21=102900, text7=78406000, text8=78406010, z22=0, z23=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z21: Item transfer: Global event flag
    text7: First half: Conversation ID
    text8: Second half: Conversation ID
    z22: Conversation: Global conversation flag
    z23: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_14_x1(text1=text7, z62=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z21) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z22, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_14_x1(text1=text8, z62=0, z64=-1, z65=0)
    # lot:1784000:Ring of Resistance
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_14_x29(z29=1011, lot1=lot4)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_14_x19(lot1=lot4, z10=z21, z11=z22, z12=z23, z27=0, z28=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_14_x21(z44=103650, z45=103653):
    """[Lib] First hostility _ (without Mes)
    z44: Hostile: Global event flag
    z45: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z44, 1)
    SetEventFlag(z45, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z44) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: First hostility: end"""
    return 0

def talk_m10_14_x22(text16=_, z41=0, z42=20, z43=80):
    """[Lib] Conversation: Hostile display only
    text16: Conversation ID
    z41: Conversation flag
    z42: Display distance
    z43: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text16, GetCommonEventParamDecimal(7), z42)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z41, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_14_x23(text15=_, z38=_, z39=9901, z40=-1):
    """[Lib] Conversation: For unique key guide
    text15: Conversation ID
    z38: Conversation flag
    z39: Key guide parameters
    z40: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z39)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text15, GetCommonEventParamDecimal(7), z40)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z38, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_14_x24():
    """[Lib] Selection Dialog: Immunity"""
    """State 0,1: Selection dialog: Display"""
    # action:1207:"Beg for pardon?\nSouls needed: %d"
    DisplayOwnYesNoMenu(1207, 0, -1, 1, PardonSoulsRequired(), 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO / Cancel"""
        Label('L0')
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        Goto('L0')
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_14_x25(z34=15, z35=0, z36=0, z37=0):
    """[Lib] Event action: Immunity
    z34: Event action
    z35: Pledge type
    z36: Item lottery ID
    z37: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z34)
    assert PlayerIsInEventAction(z34) != 0
    """State 3: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z34) != 1
    """State 5: Event action: Execution"""
    AddSouls(-1 * PardonSoulsRequired())
    SetEventFlagsInRange(3500, 3999, 0)
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z34) != 1
    """State 6: End state"""
    return 0

def talk_m10_14_x26(text13=78400600, text14=78400700, z33=114020107):
    """[Lib] Menu exit: Purchase flag
    text13: Conversation ID (at the time of purchase)
    text14: Conversation ID (when not purchased)
    z33: Purchase flag: Area other flags
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(z33) != 0:
        """State 2: Purchase and leave _SubState"""
        Label('L0')
        assert talk_m10_14_x1(text1=text13, z62=0, z64=-1, z65=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        Goto('L0')
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_14_x1(text1=text14, z62=0, z64=-1, z65=0)
    """State 4: End state"""
    return 0

def talk_m10_14_x27(z30=_, text11=_, text12=_, z31=_, z32=_):
    """[Lib] Hostile state _ (Gerdra)
    z30: Area and other flags: HP decreased
    text11: Conversation ID: HP drop 1
    text12: Conversation ID: HP drop 2
    z31: Conversation ID: HP drop 3
    z32: Hostile formation: Area and other flags
    """
    """State 0,1: Hostile state: Start"""
    while True:
        """State 2: Hostile state: standby"""
        SetEventFlag(z32, 1)
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z30) != 1
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_14_x10(text11=text11, z30=z30)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_14_x10(text11=text12, z30=z30)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_14_x10(text11=text12, z30=z30)

def talk_m10_14_x28(lot3=1742000, z18=102400, text5=74201220, text6=74201230, z19=203221, z20=0, goods3=50930000):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Important items
    lot3: Item lottery ID
    z18: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z19: Conversation: Global conversation flag
    z20: Trophy acquisition: Area and other flags
    goods3: Important items
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_14_x1(text1=text5, z62=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z18) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z19, 1)
    # goods:50930000:Tseldora Den Key
    elif call.Done() and (ItemCount(goods3, 1, 1, 1) > 1) != 0:
        Goto('L0')
    # lot:1742000:Tseldora Den Key
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_14_x29(z29=1011, lot1=lot3)
        Goto('L0')
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_14_x19(lot1=lot3, z10=z18, z11=z19, z12=z20, z27=0, z28=0)
    """State 4: Item transfer: Second half of conversation _SubState"""
    assert talk_m10_14_x1(text1=text6, z62=0, z64=-1, z65=0)
    """State 7: End state"""
    return 0

def talk_m10_14_x29(z29=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z29: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_14_x30(lot2=1742000, z13=102440, text3=74201800, text4=74201830, z14=203241, z15=0, goods2=40530000):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Consumable item
    lot2: Item lottery ID
    z13: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z14: Conversation: Global conversation flag
    z15: Trophy acquisition: Area and other flags
    goods2: Consumption items
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_14_x1(text1=text3, z62=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z13) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z14, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L1')
        assert talk_m10_14_x1(text1=text4, z62=0, z64=-1, z65=0)
    # goods:50930000:Tseldora Den Key
    elif call.Done() and (ItemCount(50930000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # lot:1742000:Tseldora Den Key
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_14_x29(z29=1011, lot1=lot2)
    elif call.Done():
        """State 6: [Lib] Item acquisition dialog: Conversation: Consumed item_SubState"""
        assert talk_m10_14_x31(lot2=lot2, z13=z13, z14=z14, z15=z15, z16=0, z17=0, goods2=goods2)
        Goto('L1')
    """State 7: End state"""
    return 0

def talk_m10_14_x31(lot2=1742000, z13=102440, z14=203241, z15=0, z16=0, z17=0, goods2=40530000):
    """[Lib] Item acquisition dialog: Conversation: Consumed item
    lot2: Item lottery ID
    z13: Item transfer: Global event flag
    z14: Conversation: Global conversation flag
    z15: Trophy acquisition: Area and other flags
    z16: Emigration permission: Global event flag
    z17: White Phantom Appearance: Global Event Flag
    goods2: Consumption items
    """
    """State 0,1: Item acquisition dialog: Display"""
    # goods:40530000:Ring of Thorns
    ConsumeItem(goods2, 1)
    SetEventFlag(z17, 1)
    SetEventFlag(z16, 1)
    SetEventFlag(z15, 1)
    SetEventFlag(z14, 1)
    SetEventFlag(z13, 1)
    # lot:1742000:Tseldora Den Key
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_14_x32(lot1=1742000, z10=102440, text2=74401340, z11=203470, z12=0, goods1=50930000):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Important items
    lot1: Item lottery ID
    z10: Item transfer: Global event flag
    text2: Conversation ID
    z11: Conversation: Global conversation flag
    z12: Trophy acquisition: Area and other flags
    goods1: Important items
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m10_14_x1(text1=text2, z62=0, z64=-1, z65=0)
    if call.Done() and GetEventFlag(z10) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z11, 1)
    # goods:50930000:Tseldora Den Key
    elif call.Done() and (ItemCount(goods1, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # lot:1742000:Tseldora Den Key
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_14_x29(z29=1011, lot1=lot1)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_14_x19(lot1=lot1, z10=z10, z11=z11, z12=z12, z27=0, z28=0)
    """State 6: End state"""
    return 0

def talk_m10_14_x33():
    """Immoral Teacher: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(205701) != 0:
        """State 4: Immoral Teacher: Normal conversation_SubState"""
        assert talk_m10_14_x35()
        """State 5: Immoral Teacher: NPC Menu_SubState"""
        Label('L0')
        assert talk_m10_14_x39()
    else:
        """State 3: Immoral Teacher: First conversation_SubState"""
        call = talk_m10_14_x34()
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_14_x34():
    """Immoral Teacher: First Conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(205700) != 0:
        """State 5: Talk to _part 2: 1_SubState"""
        # talk:78400100:"But now, you are lost, bewildered by your own actions."
        assert talk_m10_14_x0(text20=78400100, z66=0, z67=0)
        """State 6: Talk to Part 2: 2_SubState"""
        # talk:78400140:"Now is the chance.\nDemonstrate your sincerity to me."
        assert talk_m10_14_x1(text1=78400140, z62=205701, z64=-1, z65=0)
        """State 3: First conversation: Talk to _ Part 2: End"""
        SetEventFlag(114020104, 1)
        assert GetEventFlag(114020104) != 0
        """State 8: Menu: Exit state"""
        return 1
    else:
        """State 4: Talk to _ part 1_SubState"""
        # talk:78400000:"Something seems to be bothering you."
        assert talk_m10_14_x0(text20=78400000, z66=205700, z67=0)
        """State 2: Initial conversation: Talk to _Part 1: End"""
        SetEventFlag(114020104, 1)
        assert GetEventFlag(114020104) != 0
        """State 7: Normal: End state"""
        return 0

def talk_m10_14_x35():
    """Immortal Teacher: Regular Conversation"""
    """State 0,1,2: Talk: Greeting_SubState"""
    # talk:78400200:"Ask that your sins be forgiven.", talk:78400300:"I, Cromwell, will pardon your sins.", talk:78400400:"Now, now,\nconfess your sins to me.", talk:78400500:"When you face doubt, you are welcome here."
    assert talk_m10_14_x11(z51=114020104, text20=78400200, text21=78400300, text22=78400400, text23=78400500)
    """State 3: End state"""
    return 0

def talk_m10_14_x36():
    """Immoral Teacher: Menu Conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102900) != 1 and (GetPlayerStat(6, 1) > NpcInfoValue(7840, 3)) != 0 and GetEventFlag(104390)
        != 1):
        """State 4: Equipment transfer (Condition: Belief over a certain level) _SubState"""
        # lot:1784000:Ring of Resistance, talk:78406000:"Forgive this poor soul..."
        assert talk_m10_14_x20(lot4=1784000, z21=102900, text7=78406000, text8=78406010, z22=0, z23=0)
    else:
        """State 3: Menu: Conversation: 1_SubState"""
        assert talk_m10_14_x1(text1=78405600, z62=0, z64=-1, z65=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_14_x37(z1=10000, z2=-10000):
    """Immoral Teacher: Menu Immunity
    z1: Immunity: Seoul
    z2: [Item] Est bottle reinforcement
    """
    """State 0,1: Immunity: Start"""
    if GetEventFlag(106300) != 1 and (GetCommonEventParamInt(15) != 0) != 0 and (GetPlayerSinnerCount() > 1) != 0:
        """State 8: Menu: Immunity_SubState"""
        Label('L0')
        # talk:78405000:"You are a cold beast."
        call = talk_m10_14_x1(text1=78405000, z62=0, z64=-1, z65=0)
        if call.Done() and (GetEventFlag(106300) != 1 and (GetPlayerSinnerCount() > 1) != 0):
            """State 12: Exemption execution selection dialog _sinner ver_SubState"""
            # action:1221:"Beg for pardon?\nSouls needed: 0"
            call = talk_m10_14_x12(action2=1221)
            if call.Get() == 0:
                pass
            elif call.Get() == 1:
                """State 7: Menu: Immunity: YES / NO Dialog: NO_SubState"""
                Label('L1')
                assert talk_m10_14_x1(text1=78405200, z62=0, z64=-1, z65=0)
                Goto('L2')
            elif call.Get() == 2:
                Goto('L1')
        elif call.Done():
            """State 10: Immunity execution selection dialog_SubState"""
            call = talk_m10_14_x24()
            if call.Get() == 0 and (CurrentSouls() > PardonSoulsRequired()) != 1:
                """State 5: Insufficient Seoul amount confirmation dialog_SubState"""
                # action:1016:"Insufficient souls"
                assert talk_m10_14_x16(action1=1016)
                Goto('L2')
            elif call.Get() == 0:
                pass
            elif call.Get() == 1:
                Goto('L1')
        """State 3: Immunity: Purchase flag: Set"""
        SetEventFlag(114020107, 1)
        if GetEventFlag(114020107) != 0 and GetEventFlag(106300) != 1 and (GetPlayerSinnerCount() > 1) != 0:
            """State 13: [Lib] Event action: Immunity ver_SubState"""
            assert talk_m10_14_x52(z3=15, z4=0, z5=0, z6=0)
        elif GetEventFlag(114020107) != 0:
            """State 11: [Lib] Event action: Immunity_SubState"""
            assert talk_m10_14_x25(z34=15, z35=0, z36=0, z37=0)
        """State 9: Completion confirmation dialog_SubState"""
        # action:1208:"Your sin was forgiven"
        assert talk_m10_14_x16(action1=1208)
        """State 6: Menu: Immunity: YES / NO Dialog: YES_SubState"""
        assert talk_m10_14_x1(text1=78405100, z62=0, z64=-1, z65=0)
    elif GetEventFlag(103999) != 1:
        """State 4: Dialog box for confirming the absence of infidelity"""
        # action:1209:"You have not sinned"
        assert talk_m10_14_x16(action1=1209)
    else:
        Goto('L0')
    """State 2: Immunity: Finish"""
    Label('L2')
    ClearNpcMenuSelection()
    """State 14: End state"""
    return 0

def talk_m10_14_x38():
    """Immaculate Teacher: Canceling Menu Pledge"""
    """State 0,1: Pledge cancellation: Start"""
    if (not GetPlayerCovenant()) != 0:
        """State 5: No pledge agreement confirmation dialog_SubState"""
        # action:1304:"No covenant to abandon"
        assert talk_m10_14_x16(action1=1304)
    else:
        """State 9: Menu: Pledge Discard_SubState"""
        assert talk_m10_14_x1(text1=78405300, z62=0, z64=-1, z65=0)
        """State 10: Menu: Discard Pledge: YES / NO Dialog_SubState"""
        # action:1302:"Abandon covenant?"
        call = talk_m10_14_x12(action2=1302)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 12: [Lib] OK dialog_SubState"""
            # action:1315:"Cannot abandon covenant\nwith phantom present"
            assert talk_m10_14_x16(action1=1315)
        elif call.Get() == 0:
            """State 4: Pledge cancellation: Pledge cancellation flag set"""
            SetEventFlag(114020107, 1)
            SetEventFlagIf((GetPlayerCovenant() == 1) != 0, 200900, 0)
            SetEventFlagIf((GetPlayerCovenant() == 2) != 0, 200901, 0)
            SetEventFlagIf((GetPlayerCovenant() == 3) != 0, 200902, 0)
            SetEventFlagIf((GetPlayerCovenant() == 4) != 0, 200903, 0)
            SetEventFlagIf((GetPlayerCovenant() == 5) != 0, 200904, 0)
            SetEventFlagIf((GetPlayerCovenant() == 6) != 0, 200905, 0)
            SetEventFlagIf((GetPlayerCovenant() == 7) != 0, 200906, 0)
            SetEventFlagIf((GetPlayerCovenant() == 8) != 0, 200907, 0)
            SetEventFlagIf((GetPlayerCovenant() == 9) != 0, 200908, 0)
            """State 2: Pledge cancellation: Execute pledge cancellation"""
            ChangePlayerCovenant(0)
            SaveExecution()
            assert (not GetPlayerCovenant()) != 0
            """State 6: Pledge cancellation production (general pledge conclusion motion) _SubState"""
            assert talk_m10_14_x17(z46=8)
            """State 11: Pledge cancellation success confirmation dialog_SubState"""
            # action:1303:"Abandoned covenant"
            assert talk_m10_14_x16(action1=1303)
            """State 8: Menu: Discard Pledge: YES / NO Dialog: YES_SubState"""
            assert talk_m10_14_x1(text1=78405400, z62=0, z64=-1, z65=0)
        elif call.Get() == 2:
            """State 7: Menu: Discard Pledge: YES / NO Dialog: NO_SubState"""
            Label('L0')
            assert talk_m10_14_x1(text1=78405500, z62=0, z64=-1, z65=0)
        elif call.Get() == 1:
            Goto('L0')
    """State 3: Pledge cancellation: End"""
    ClearNpcMenuSelection()
    """State 13: End state"""
    return 0

def talk_m10_14_x39():
    """Immoral Teacher: NPC Menu"""
    """State 0,1: Menu: Start"""
    SetEventFlag(114020107, 0)
    while True:
        """State 2: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_14_x13(z47=0, z48=220, z49=78400000, z50=0)
        if call.Get() == 2:
            """State 3: Immoral Teacher: Menu Conversation_SubState"""
            call = talk_m10_14_x36()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 7:
            """State 4: Immoral Teacher: Menu Immunity_SubState"""
            call = talk_m10_14_x37(z1=10000, z2=-10000)
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 7: [Lib] Menu exit: Purchase flag_SubState"""
            # talk:78400600:"We must never forget our sins.", talk:78400700:"Whenever you are ready."
            assert talk_m10_14_x26(text13=78400600, text14=78400700, z33=114020107)
        """State 8: End state"""
        Label('L0')
        return 0
    """State 6: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:78400800:"You will always find me here."
    assert talk_m10_14_x15(text17=78400800)
    Goto('L0')

def talk_m10_14_x40():
    """Wandering Warrior: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102402) != 0:
        pass
    elif GetEventFlag(104153) != 0:
        pass
    elif (CompareOwnEzStateFlag(7) == 1) != 0:
        pass
    elif (GetStateTime() > 10) != 0:
        pass
    """State 3: Conversation: branch"""
    SetEventFlag(102402, 1)
    if GetEventFlag(114000141) != 0:
        """State 4: Wandering Warrior: PC Addition Conversation_SubState"""
        assert talk_m10_14_x41()
    elif GetEventFlag(114000142) != 0:
        """State 5: Wandering Warrior: Non-PC conversation _SubState"""
        assert talk_m10_14_x42()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_14_x41():
    """Wandering Warrior: PC chat"""
    """State 0,1: Social conversation: Start"""
    if GetEventFlag(203221) != 0 and GetEventFlag(102401) != 1 and GetEventFlag(104150) != 1:
        """State 4: Equipment transfer (condition: wandering to wander) _SubState"""
        # lot:1742010:Creighton's Steel Mask, talk:74206000:"Heh... Rotten bastard..."
        assert (talk_m10_14_x18(lot5=1742010, z24=102401, text9=74206000, text10=74206010, z25=0, z26=0,
                z27=0, z28=0))
    elif GetEventFlag(203221) != 0:
        """State 3: Player support: Talk: Part 3_SubState"""
        # talk:74201300:"You did me well."
        assert talk_m10_14_x0(text20=74201300, z66=0, z67=0)
    elif GetEventFlag(203220) != 0:
        """State 5: Player support: Talk: Part 2: 1_SubState"""
        # talk:74201200:"...I did it...Hah hah!"
        assert talk_m10_14_x0(text20=74201200, z66=0, z67=0)
        """State 6: Player support: Talk: Part 2: 2_SubState"""
        # lot:1742000:Tseldora Den Key, talk:74201220:"Here, take this, and go to my bolt-hole down the way.", talk:74201230:"What's there is yours.", goods:50930000:Tseldora Den Key
        assert (talk_m10_14_x28(lot3=1742000, z18=102400, text5=74201220, text6=74201230, z19=203221,
                z20=0, goods3=50930000))
    else:
        """State 2: Player support: Talk: Part 1_SubState"""
        # talk:74201100:"...Serves you right...Hah hah hah!"
        assert talk_m10_14_x0(text20=74201100, z66=203220, z67=0)
    """State 7: End state"""
    return 0

def talk_m10_14_x42():
    """Wanderer Warrior: Non-PC chat"""
    """State 0,1: Non-energized conversation: start"""
    if GetEventFlag(203230) != 0:
        """State 3: Player non-addition: Talk: Part 2_SubState"""
        # talk:74201500:"...Wait...\n...You weren't friends with that rat, were you?"
        assert talk_m10_14_x0(text20=74201500, z66=0, z67=0)
    else:
        """State 2: Player non-assist: Talk: Part 1_SubState"""
        # talk:74201400:"...Serves you right...Hah hah hah!"
        assert talk_m10_14_x0(text20=74201400, z66=203230, z67=0)
    """State 4: End state"""
    return 0

def talk_m10_14_x43():
    """Wandering Warrior: Conversation: Patch Death"""
    """State 0,1: Patch death conversation: start"""
    if GetEventFlag(203241) != 0:
        """State 5: Patch death: Talk: Part 3 (single loop) _SubState"""
        # talk:74201900:"You did me well."
        assert talk_m10_14_x0(text20=74201900, z66=0, z67=0)
    # goods:40530000:Ring of Thorns
    elif GetEventFlag(203240) != 0 and (ItemCount(40530000, 1, 1, 0) > 1) != 0:
        """State 3: Patch death: Talk: Part 2_SubState"""
        # talk:74201700:"Your ring! That's his ring!"
        assert talk_m10_14_x0(text20=74201700, z66=0, z67=0)
        """State 4: Warrior Band Ring: Transfer Selection Dialog_SubState"""
        # action:1205:"What is your choice?"
        call = talk_m10_14_x12(action2=1205)
        if call.Get() == 0:
            """State 7: Patch death: Talk: Part 2: YES_SubState"""
            # lot:1742000:Tseldora Den Key, talk:74201800:"You killed him, didn't you?", talk:74201830:"What's there is yours.", goods:40530000:Ring of Thorns
            assert (talk_m10_14_x30(lot2=1742000, z13=102440, text3=74201800, text4=74201830, z14=203241,
                    z15=0, goods2=40530000))
        elif call.Get() == 2:
            """State 6: Patch death: Talk: Part 2: NO_SubState"""
            Label('L0')
            # talk:74202000:"I see how it is. You're another slimy toad!"
            call = talk_m10_14_x1(text1=74202000, z62=0, z64=-1, z65=0)
            if call.Done() and GetEventFlag(104150) != 0:
                pass
            elif call.Done():
                """State 9: Hostility: end state"""
                return 1
        elif call.Get() == 1:
            Goto('L0')
    else:
        """State 2: Patch death: Talk: Part 1_SubState"""
        # talk:74201600:"Oh, you. What do you want?"
        assert talk_m10_14_x0(text20=74201600, z66=203240, z67=0)
    """State 8: Normal: End state"""
    return 0

def talk_m10_14_x44():
    """Patch: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102445) != 0:
        pass
    elif GetEventFlag(104173) != 0:
        pass
    elif (CompareOwnEzStateFlag(7) == 1) != 0:
        pass
    elif (GetStateTime() > 10) != 0:
        pass
    """State 3: Conversation: branch"""
    SetEventFlag(102445, 1)
    if GetEventFlag(102441) != 1 and GetEventFlag(102452) != 0 and GetEventFlag(104170) != 1:
        """State 5: Equipment transfer (condition: white phantom summon achievement) _SubState"""
        # lot:1744010:Pate's Spear, talk:74406000:"Heh heh heh..."
        assert (talk_m10_14_x18(lot5=1744010, z24=102441, text9=74406000, text10=74406010, z25=0, z26=0,
                z27=0, z28=0))
    elif GetEventFlag(114000143) != 0 and GetEventFlag(203470) != 0:
        """State 4: Player support: Talk: Part 2_SubState"""
        # talk:74401400:"Be cautious on your travels."
        assert talk_m10_14_x0(text20=74401400, z66=0, z67=0)
    elif GetEventFlag(114000143) != 0:
        """State 7: Player support: Speak: Part 1: 1_SubState"""
        # talk:74401300:"What misunderstanding could have caused this?"
        assert talk_m10_14_x0(text20=74401300, z66=0, z67=0)
        """State 8: Player support: Talk: Part 1: 2_SubState"""
        # lot:1742000:Tseldora Den Key, talk:74401340:"Here, use this key.", goods:50930000:Tseldora Den Key
        assert talk_m10_14_x32(lot1=1742000, z10=102440, text2=74401340, z11=203470, z12=0, goods1=50930000)
    elif GetEventFlag(114000144) != 0:
        """State 6: Player non-addition: Talk: Part 1 (single loop) _SubState"""
        # talk:74401500:"What was he thinking?"
        assert talk_m10_14_x0(text20=74401500, z66=0, z67=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_14_x45():
    """Higher weapon shop: conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Higher weapon shop: First conversation_SubState"""
    assert talk_m10_14_x46()
    """State 4: Higher weapon shop: NPC menu_SubState"""
    assert talk_m10_14_x47()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_14_x46():
    """Upper weapon shop: first conversation"""
    """State 0,1: First conversation: start"""
    if (GetGlobalVariable(224) > 1) != 0:
        """State 5: [Lib] Conversation: Greeting: General purpose_SubState"""
        # talk:77501400:"What do you desire?", talk:77501500:"Do you have a Wondrous Soul?", talk:77501600:"Hello there. Do you have a Wondrous Soul?", talk:77501700:"Hello there. What can I do for you?"
        assert talk_m10_14_x11(z51=114020134, text20=77501400, text21=77501500, text22=77501600, text23=77501700)
    elif GetEventFlag(205410) != 0 and (GetGlobalVariable(224) > 1) != 1:
        """State 4: Talk: Free _SubState"""
        # talk:77500510:"If you provide a Wondrous Soul,\nI will create one thing of your choice."
        call = talk_m10_14_x0(text20=77500510, z66=0, z67=0)
        if call.Done() and GetEventFlag(114020134) != 1:
            """State 2: Conversation: Contact flag: Setting"""
            Label('L0')
            SetEventFlag(114020134, 1)
        elif call.Done():
            pass
    else:
        """State 3: Talk: First_SubState"""
        # talk:77500300:"Oh, we meet again, kind traveller."
        call = talk_m10_14_x0(text20=77500300, z66=205410, z67=0)
        if call.Done() and GetEventFlag(114020134) != 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 6: End state"""
    return 0

def talk_m10_14_x47():
    """Higher weapon shop: NPC menu"""
    """State 0: Start state"""
    while True:
        """State 1: Menu: Start"""
        if (GetGlobalVariable(224) > 1) != 0:
            """State 3: [Lib] Menu start: Paid_SubState"""
            call = talk_m10_14_x13(z47=0, z48=220, z49=77600000, z50=0)
            if call.Get() == 2:
                """State 6: Higher weapon shop: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_14_x48()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 1:
                """State 4: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:77502200:"Come back again if you find another soul.", talk:77501100:"Come again, if it please you."
                assert talk_m10_14_x14(text18=77502200, text19=77501100)
            elif call.Get() == 0:
                break
        else:
            """State 7: [Lib] Menu start: Free_SubState"""
            call = talk_m10_14_x13(z47=0, z48=220, z49=77600001, z50=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 1:
                Goto('L1')
            elif call.Get() == 0:
                break
            elif (GetGlobalVariable(224) > 1) != 0:
                Goto('L1')
        """State 2: Menu: Exit"""
        Label('L2')
        ClearNpcMenuResults()
        """State 8: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:77502300:"Be safe."
    assert talk_m10_14_x15(text17=77502300)
    Goto('L2')

def talk_m10_14_x48():
    """Higher weapon shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(205423) != 0:
        """State 3: Menu conversation: Conversation flag: Initialization"""
        SetEventFlag(205420, 0)
        SetEventFlag(205421, 0)
        SetEventFlag(205422, 0)
        SetEventFlag(205423, 0)
        if GetEventFlag(100904) != 0:
            """State 5: Higher weapon shop: Menu conversation: When obtaining King Seoul_SubState"""
            Label('L0')
            assert talk_m10_14_x50()
        else:
            """State 4: Higher weapon shop: Menu conversation: When king Seoul is not yet available _SubState"""
            Label('L1')
            assert talk_m10_14_x49()
    elif GetEventFlag(100904) != 0:
        Goto('L0')
    else:
        Goto('L1')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 6: End state"""
    return 0

def talk_m10_14_x49():
    """Higher weapon shop: Menu conversation: When king Seoul is not yet available"""
    """State 0,1: Menu conversation: Branch"""
    if GetEventFlag(205422) != 0:
        """State 5: Menu conversation: 4_SubState"""
        # talk:77502600:"Do you find me strange? Skee hee."
        assert talk_m10_14_x1(text1=77502600, z62=205423, z64=-1, z65=0)
    elif GetEventFlag(205421) != 0:
        """State 4: Menu conversation: 3_SubState"""
        # talk:77502500:"It is said that our technique originates\nfrom a strange being that inhabited this land."
        assert talk_m10_14_x1(text1=77502500, z62=205422, z64=-1, z65=0)
    elif GetEventFlag(205420) != 0:
        """State 3: Menu conversation: 2_SubState"""
        # talk:77502400:"It's hard to believe now,\nbut this land was once a flourishing kingdom."
        assert talk_m10_14_x1(text1=77502400, z62=205421, z64=-1, z65=0)
    else:
        """State 2: Menu conversation: Part 1_SubState"""
        # talk:77501300:"The nature of an item is greatly influenced\nby the soul that was used to create it."
        assert talk_m10_14_x1(text1=77501300, z62=205420, z64=-1, z65=0)
    """State 6: End state"""
    return 0

def talk_m10_14_x50():
    """Higher weapon shop: Menu conversation: When obtaining King Seoul"""
    """State 0,1: Menu conversation: Branch"""
    if GetEventFlag(205422) != 0:
        """State 4: Menu conversation: 4_SubState"""
        # talk:77502600:"Do you find me strange? Skee hee."
        assert talk_m10_14_x1(text1=77502600, z62=205423, z64=-1, z65=0)
    elif GetEventFlag(205421) != 0:
        """State 3: Menu conversation: 3_SubState"""
        Label('L0')
        # talk:77502500:"It is said that our technique originates\nfrom a strange being that inhabited this land."
        assert talk_m10_14_x1(text1=77502500, z62=205422, z64=-1, z65=0)
    elif GetEventFlag(205420) != 0:
        Goto('L0')
    else:
        """State 2: Menu conversation: Part 1_SubState"""
        # talk:77501300:"The nature of an item is greatly influenced\nby the soul that was used to create it."
        assert talk_m10_14_x1(text1=77501300, z62=205420, z64=-1, z65=0)
    """State 5: End state"""
    return 0

def talk_m10_14_x51(text1=_, z7=_, z8=_, z9=_):
    """Wandering & Patch: Battle Event
    text1: Conversation ID
    z7: Opponent death: global event flag
    z8: Combat event hostile: area and other flags
    z9: Battle area ID
    """
    """State 0,2: Battle event: Start"""
    if GetEventFlag(z7) != 0:
        pass
    elif GetEventFlag(114000140) != 0:
        pass
    else:
        """State 1: Battle event: Waiting for area entry"""
        if GetEventFlag(114000140) != 0:
            pass
        elif PlayerInPoint(z9) != 0:
            """State 3: Battle event: Area entry waiting: End"""
            if GetEventFlag(114000140) != 0:
                pass
            elif ConversationEnded() != 0:
                """State 4: Battle Event: Conversation_SubState"""
                assert talk_m10_14_x1(text1=text1, z62=0, z64=30, z65=0)
    """State 5: End state"""
    return 0

def talk_m10_14_x52(z3=15, z4=0, z5=0, z6=0):
    """Infidel Teacher: Event Action: Infidel ver
    z3: Event action
    z4: Pledge type
    z5: Item lottery ID
    z6: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z3)
    assert PlayerIsInEventAction(z3) != 0
    """State 3: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z3) != 1
    """State 5: Event action: Execution"""
    ResetSinCounter()
    SetEventFlagsInRange(3500, 3999, 0)
    SetEventFlag(106300, 1)
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z3) != 1
    """State 6: End state"""
    return 0

def talk_m10_14_x53():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(100760) != 0 and GetEventFlag(208001) != 0:
        """State 6: [Lib] Conversation: Talk to 3_SubState"""
        # talk:69200200:"Young Hollow, seek after Vendrick."
        assert talk_m10_14_x23(text15=69200200, z38=0, z39=9901, z40=-1)
        """State 3: End encounter flag"""
        SetEventFlag(100740, 1)
    elif GetEventFlag(100760) != 0 and GetEventFlag(208000) != 0:
        """State 5: [Lib] Conversation: Talk to 2_SubState"""
        # talk:69200100:"Young Hollow, there are but two paths.\nInherit the order of this world, or destroy it."
        assert talk_m10_14_x23(text15=69200100, z38=208001, z39=9901, z40=-1)
    elif GetEventFlag(100760) != 0:
        """State 4: [Lib] Conversation: Talk to 1_SubState"""
        # talk:69200010:"No one has come this far,\nnot for a very long while."
        assert talk_m10_14_x23(text15=69200010, z38=208000, z39=9901, z40=-1)
    """State 2,7: End state"""
    return 0

def talk_m10_14_4100000():
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
            assert talk_m10_14_x53()
    """State 2: Conversation: System termination"""
    EndMachine()

