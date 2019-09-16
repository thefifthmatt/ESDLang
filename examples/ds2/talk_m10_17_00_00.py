# -*- coding: utf-8 -*-
def talk_m10_17_7040():
    """Ladder Shop (Tank Valley)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_17_x9(z50=103551, z51=104050, z52=117020111)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m10_17_x3(text7=70409200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_17_x6(z48=117020112, text18=70409500, text19=70409500, z49=70409500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 9: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_17_x7(text21=70409600, z54=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 4: Ladder shop: Conversation_SubState"""
                call = talk_m10_17_x47()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_17_x5(text22=70409400, text23=70409410, text24=70409420, text25=70409400,
                                          z55=117020115, z56=117020116)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 5: [Lib] First adversification_SubState"""
                        call = talk_m10_17_x4(z57=103550, text26=70409100, z58=0, z59=103551)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(117020116) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(117020115) != 1:
                    Goto('L2')
        """State 10: [Lib] Killing state_SubState"""
        talk_m10_17_x8(text20=70409300, z53=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_17_7260():
    """Dwarf"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_17_x9(z50=103632, z51=104130, z52=117020161)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_17_x3(text7=72609200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_17_x6(z48=117020162, text18=72609500, text19=72609500, z49=72609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_17_x7(text21=72609600, z54=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Dwarf: Conversation_SubState"""
                call = talk_m10_17_x29(z26=117020164, z27=102343, z28=102346)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_17_x5(text22=72609400, text23=72609410, text24=72609420, text25=72609400,
                                          z55=117020165, z56=117020166)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_17_x4(z57=103630, text26=72609100, z58=0, z59=103632)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(117020166) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(117020165) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_17_x8(text20=72609300, z53=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_17_7440():
    """Patch (dwelling valley)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_17_x9(z50=103672, z51=104170, z52=117020141)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_17_x3(text7=74409200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_17_x6(z48=117020142, text18=74409500, text19=74409500, z49=74409500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_17_x7(text21=74409600, z54=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Patch: Conversation_SubState"""
                call = talk_m10_17_x56()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_17_x5(text22=74409400, text23=74409410, text24=74409420, text25=74409400,
                                          z55=117020145, z56=117020146)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_17_x4(z57=103670, text26=74409100, z58=0, z59=103672)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(117020146) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(117020145) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_17_x8(text20=74409300, z53=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_17_7520():
    """Woman Knight (Tank Valley)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_17_x9(z50=103693, z51=104190, z52=117020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_17_x3(text7=75209200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_17_x6(z48=117020122, text18=75209500, text19=75209500, z49=75209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_17_x7(text21=75209600, z54=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: [Lib] Female knight: Before last: Conversation_SubState"""
                call = talk_m10_17_x23(z15=102481, z16=102486, z17=102501, z18=117020129)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_17_x5(text22=75209400, text23=75209410, text24=75209420, text25=75209400,
                                          z55=117020125, z56=117020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_17_x4(z57=103690, text26=75209100, z58=0, z59=103693)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(117020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(117020125) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_17_x8(text20=75209300, z53=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_17_7620():
    """Material shop (Tani no Valley)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_17_x9(z50=103761, z51=104260, z52=117020151)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_17_x3(text7=76209200, z38=0, z39=20, z40=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_17_x6(z48=117020152, text18=76209500, text19=76209500, z49=76209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_17_x7(text21=76209600, z54=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Material shop: Conversation_SubState"""
                call = talk_m10_17_x52()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_17_x5(text22=76209400, text23=76209410, text24=76209420, text25=76209400,
                                          z55=117020155, z56=117020156)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_17_x4(z57=103760, text26=76209100, z58=0, z59=103761)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(117020156) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(117020155) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_17_x8(text20=76209300, z53=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_17_7870():
    """Sun altar"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Menu: Start"""
        if IsGuest() != 0:
            break
        elif GetEventFlag(117020170) != 0:
            pass
        """State 3: Menu: Event action: Playback"""
        PlayerActionRequest(9)
        # lot:2007000:Sun Seal
        if (PlayerIsInEventAction(9) != 0 and (GetPlayerCovenant() == 1) != 0 and GetEventFlag(103120)
            != 1 and CanGetItemLot(2007000, 1) != 1):
            """State 15: [Lib] Inventory full dialog: Item display_SubState"""
            # lot:2007000:Sun Seal
            assert talk_m10_17_x46(z30=1011, lot1=2007000)
        elif PlayerIsInEventAction(9) != 0 and (GetPlayerCovenant() == 1) != 0 and GetEventFlag(103120) != 1:
            """State 14: Pledge item transfer not yet available: Insurance_SubState"""
            # lot:2007000:Sun Seal
            assert talk_m10_17_x17(lot1=2007000, z4=103120)
        elif PlayerIsInEventAction(9) != 0:
            pass
        while True:
            """State 5: Menu: Branch"""
            # goods:63021000:"Praise the Sun" Gesture
            if PlayerIsInEventAction(9) != 0 and (ItemCount(63021000, 1, 1, 0) > 1) != 0:
                """State 12: [Lib] Menu start: No gesture _SubState"""
                call = talk_m10_17_x13(z43=0, z44=-1, z45=78602001, z46=0)
                if call.Get() == 0:
                    break
                elif call.Get() == 1:
                    break
                elif call.Get() == 6:
                    """State 9: [Lib] Menu item: Make a pledge: OBJ_SubState"""
                    Label('L0')
                    # lot:2007000:Sun Seal, action:1330:"Join the Heirs of the Sun covenant?", action:1340:"Abandon your covenant and\njoin the Heirs of the Sun?"
                    assert (talk_m10_17_x42(mode1=1, z7=-9999, lot4=2007000, z8=103120, action1=1330,
                            action2=1340, z9=117020171))
                elif call.Get() == 4:
                    """State 10: [Lib] Menu item: Dedicated: OBJ_SubState"""
                    Label('L1')
                    # goods:62120000:Sunlight Medal, lot:2007000:Sun Seal
                    call = talk_m10_17_x36(goods1=62120000, z33=60, z34=210, z35=-9999, mode2=1, lot9=2007000,
                                           z36=103120, z37=103132)
                    if call.Get() == 1:
                        """State 11: [Lib] Menu item: Dedicated: OBJ: Pledge item award_SubState"""
                        # lot:2007011:Sunlight Parma, lot:2007012:Sun Sword, lot:2007013:Sunlight Spear
                        assert (talk_m10_17_x44(z2=60, z3=210, lot1=2007011, lot2=2007012, lot3=2007013,
                                z4=103130, z5=103131, z6=103132))
                    elif call.Get() == 0:
                        pass
            elif PlayerIsInEventAction(9) != 0:
                """State 8: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_17_x13(z43=0, z44=-1, z45=78602000, z46=0)
                if call.Get() == 6:
                    Goto('L0')
                elif call.Get() == 4:
                    Goto('L1')
                elif call.Get() == 10:
                    """State 13: [Lib] Menu item: Gesture_SubState"""
                    assert talk_m10_17_x38(z31=63021000, z32=0)
                elif call.Get() == 0:
                    break
                elif call.Get() == 1:
                    break
        while True:
            """State 4: Menu: Event action: End"""
            EndPlayerActionRequest()
            if (GetStateTime() > GetRandomValueForStateTime(1, 1)) != 0:
                """State 7: Menu: Event Action: Insurance"""
                pass
            elif PlayerIsInEventAction(9) != 1:
                """State 2: Menu: Exit"""
                SetEventFlag(117020170, 0)
                ClearNpcMenuResults()
                CloseNpcMenu()
                assert (GetEventFlag(117020170) != 1 and (GetStateTime() > GetRandomValueForStateTime(0.1,
                        0.1)) != 0)
                Continue('mainloop')
    """State 6: Menu: System: Exit"""
    EndMachine()

def talk_m10_17_x0(text14=_, z62=_, z63=0):
    """[Lib] Conversation: General purpose
    text14: Conversation ID
    z62: Conversation flag
    z63: Global event flag
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
    SetEventFlag(z62, 1)
    SetEventFlag(z63, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_17_x1(text8=_, z42=_, z60=-1, z61=0):
    """[Lib] Conversation: Display only
    text8: Conversation ID
    z42: Conversation flag
    z60: Display distance
    z61: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), z60)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z42, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_17_x2(text20=_, z53=0):
    """[Lib] Conversation: Event end
    text20: Conversation ID
    z53: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text20, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z53, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_17_x3(text7=_, z38=0, z39=20, z40=80):
    """[Lib] Reunion hostility
    text7: Conversation message ID
    z38: Conversation flag ID
    z39: Display distance
    z40: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_17_x35(text7=text7, z38=z38, z39=z39, z40=z40)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_17_x4(z57=_, text26=_, z58=0, z59=_):
    """[Lib] First hostility
    z57: Hostile: Global event flag
    text26: Conversation ID
    z58: Conversation flag
    z59: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z57, 1)
    SetEventFlag(z59, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z57) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_17_x1(text8=text26, z42=z58, z60=-1, z61=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_17_x5(text22=_, text23=_, text24=_, text25=_, z55=_, z56=_):
    """[Lib] Hostile waiting
    text22: Conversation ID: 1 attacked
    text23: Conversation ID: Attacked 2
    text24: Conversation ID: 3 attacked
    text25: Conversation ID: 4 attacked
    z55: No use: Area and other flags
    z56: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z56) != 1, z56, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z55) != 1, z55, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_17_x1(text8=text25, z42=0, z60=-1, z61=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_17_x1(text8=text24, z42=0, z60=-1, z61=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_17_x1(text8=text23, z42=0, z60=-1, z61=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_17_x1(text8=text22, z42=0, z60=-1, z61=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_17_x6(z48=_, text18=_, text19=_, z49=_):
    """[Lib] Hostile state
    z48: Area and other flags: HP decreased
    text18: Conversation ID: HP drop 1
    text19: Conversation ID: HP drop 2
    z49: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z48) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_17_x10(text18=text18, z48=z48)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_17_x10(text18=text19, z48=z48)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_17_x10(text18=text19, z48=z48)

def talk_m10_17_x7(text21=_, z54=0):
    """[Lib] Death status
    text21: Conversation ID
    z54: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_17_x2(text20=text21, z53=z54)

def talk_m10_17_x8(text20=_, z53=0):
    """[Lib] Murder status
    text20: Conversation ID
    z53: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_17_x2(text20=text20, z53=z53)

def talk_m10_17_x9(z50=_, z51=_, z52=_):
    """[Lib] Event: Branch
    z50: Hostile flag
    z51: death flag
    z52: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z51) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z52) != 0
    elif GetEventFlag(z50) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_17_x10(text18=_, z48=_):
    """[Lib] Conversation: HP drop
    text18: Conversation ID
    z48: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text18, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z48, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_17_x11(z47=117020154, text14=76200200, text15=76200300, text16=76200400, text17=76200400):
    """[Lib] Conversation: Greeting: General
    z47: Area other flag: Contact flag
    text14: Text ID: Talk to_continuous 1
    text15: Text ID: Talk to_continuous 2
    text16: Text ID: Talk to _After a long time 1
    text17: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z47) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_17_x0(text14=text14, z62=0, z63=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_17_x0(text14=text15, z62=0, z63=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_17_x0(text14=text16, z62=0, z63=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_17_x0(text14=text17, z62=0, z63=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(z47, 1)
    """State 10: End state"""
    return 0

def talk_m10_17_x12(action1=_):
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

def talk_m10_17_x13(z43=0, z44=_, z45=_, z46=0):
    """[Lib] Menu start: General purpose
    z43: Camera parameter ID
    z44: Target Damipoly ID
    z45: NPC event parameter ID
    z46: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z46, z43, z44, z45)
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

def talk_m10_17_x14(text12=_, text13=_):
    """[Lib] Menu exit: General purpose
    text12: Conversation ID (at the time of purchase)
    text13: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_17_x1(text8=text12, z42=0, z60=-1, z61=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_17_x1(text8=text13, z42=0, z60=-1, z61=0)
    """State 4: End state"""
    return 0

def talk_m10_17_x15(text11=_):
    """[Lib] Menu cancellation: General purpose
    text11: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_17_x1(text8=text11, z42=0, z60=-1, z61=0)
    """State 4: End state"""
    return 0

def talk_m10_17_x16(action5=_):
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

def talk_m10_17_x17(lot1=_, z4=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    z4: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z4, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_17_x18(lot8=1726000, z29=102355, text6=72606000):
    """[Lib] Equipment transfer: Mes⇒Item
    lot8: Item lottery ID
    z29: Global event flag
    text6: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_17_x1(text8=text6, z42=0, z60=-1, z61=0)
    # lot:1726000:Gyrm Greataxe
    if call.Done() and CanGetItemLot(lot8, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_17_x46(z30=1011, lot1=lot8)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_17_x17(lot1=lot8, z4=z29)
    """State 5: End state"""
    return 0

def talk_m10_17_x19(lot7=_, z22=_, text4=_, text5=_, z23=_, z18=_, z24=0, z25=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot7: Item lottery ID
    z22: Item transfer: Global event flag
    text4: First half: Conversation ID
    text5: Second half: Conversation ID
    z23: Conversation: Global conversation flag
    z18: Trophy acquisition: Area and other flags
    z24: Emigration permission: Global event flag
    z25: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_17_x1(text8=text4, z42=0, z60=-1, z61=0)
    if call.Done() and GetEventFlag(z22) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z23, 1)
        SetEventFlag(z24, 1)
        SetEventFlag(z25, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_17_x1(text8=text5, z42=0, z60=-1, z61=0)
    elif call.Done() and CanGetItemLot(lot7, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_17_x46(z30=1011, lot1=lot7)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_17_x21(lot5=lot7, z12=z22, z13=z23, z14=z18, z24=z24, z25=z25)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_17_x20(lot6=1752020, z19=102496, text3=75201100, z20=203620, z21=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot6: Item lottery ID
    z19: Item transfer: Global event flag
    text3: Conversation ID
    z20: Conversation: Global conversation flag
    z21: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m10_17_x1(text8=text3, z42=0, z60=-1, z61=0)
    if call.Done() and GetEventFlag(z19) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z20, 1)
    # lot:1752020:Ring of Steel Protection+1
    elif call.Done() and CanGetItemLot(lot6, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_17_x46(z30=1011, lot1=lot6)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_17_x21(lot5=lot6, z12=z19, z13=z20, z14=z21, z24=0, z25=0)
    """State 9: End state"""
    return 0

def talk_m10_17_x21(lot5=_, z12=_, z13=_, z14=_, z24=0, z25=0):
    """[Lib] Item acquisition dialog: Conversation
    lot5: Item lottery ID
    z12: Item transfer: Global event flag
    z13: Conversation: Global conversation flag
    z14: Trophy acquisition: Area and other flags
    z24: Emigration permission: Global event flag
    z25: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z25, 1)
    SetEventFlag(z24, 1)
    SetEventFlag(z14, 1)
    SetEventFlag(z13, 1)
    SetEventFlag(z12, 1)
    AwardItem(lot5, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_17_x22(lot5=1762000, z12=102620, text1=76206000, text2=76206010, z13=0, z14=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot5: Item lottery ID
    z12: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z13: Conversation: Global conversation flag
    z14: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_17_x1(text8=text1, z42=0, z60=-1, z61=0)
    if call.Done() and GetEventFlag(z12) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z13, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_17_x1(text8=text2, z42=0, z60=-1, z61=0)
    # lot:1762000:Twinkling Titanite
    elif call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_17_x46(z30=1011, lot1=lot5)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_17_x21(lot5=lot5, z12=z12, z13=z13, z14=z14, z24=0, z25=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_17_x23(z15=102481, z16=102486, z17=102501, z18=117020129):
    """[Lib] Woman Knight: Before Last: Conversation
    z15: Encounter: Global event flag
    z16: Generation establishment: Global event flag
    z17: White Phantom Appearance: Global Event Flag
    z18: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203630) != 0 and GetEventFlag(z15) != 0:
        """State 5: Woman Knight: Encounter 4th: Conversation_SubState"""
        Label('L0')
        assert talk_m10_17_x27(z16=z16, z15=z15, z17=z17)
    elif GetEventFlag(203623) != 0 and GetEventFlag(z15) != 1:
        Goto('L0')
    elif GetEventFlag(203620) != 0 and GetEventFlag(z15) != 0:
        """State 4: Woman Knight: Encounter 3rd: Conversation_SubState"""
        Label('L1')
        assert talk_m10_17_x26(z16=z16, z15=z15, z17=z17)
    elif GetEventFlag(203614) != 0 and GetEventFlag(z15) != 1:
        Goto('L1')
    elif GetEventFlag(203610) != 0 and GetEventFlag(z15) != 0:
        """State 3: Woman Knight: Encounter 2nd: Conversation_SubState"""
        Label('L2')
        assert talk_m10_17_x25(z16=z16, z15=z15, z17=z17)
    elif GetEventFlag(203602) != 0 and GetEventFlag(z15) != 1:
        Goto('L2')
    elif GetEventFlag(203600) != 0 and GetEventFlag(z15) != 0:
        """State 2: Woman Knight: First encounter: Conversation_SubState"""
        Label('L3')
        assert talk_m10_17_x24(z16=z16, z15=z15, z17=z17)
    else:
        Goto('L3')
    """State 7: End state"""
    return 0

def talk_m10_17_x24(z16=102486, z15=102481, z17=102501):
    """Woman Knight: First encounter: Conversation
    z16: Generation stop: Global event flag
    z15: Encounter: Global event flag
    z17: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: First encounter: Start"""
    if GetEventFlag(203601) != 0:
        """State 7: First encounter: Talk: Part 3: 1_SubState"""
        # talk:75200300:"You are an odd one, indeed.\nI've always made a point of avoiding people."
        assert talk_m10_17_x0(text14=75200300, z62=0, z63=0)
        """State 10: First encounter: Talk: Part 3: 2_SubState"""
        # talk:75200310:"While you've made a point of engaging me."
        assert talk_m10_17_x1(text8=75200310, z42=0, z60=-1, z61=0)
        """State 11: First encounter: Talk: Part 3: 3_SubState"""
        # talk:75200320:"I can see that you are mid-journey.\nIf you require assistance, I will help you."
        assert talk_m10_17_x1(text8=75200320, z42=203602, z60=-1, z61=0)
        """State 4: First encounter: White phantom can appear: Set flag"""
        SetEventFlag(z17, 1)
        assert GetEventFlag(z17) != 0
        """State 2: First encounter: stop generation"""
        SetEventFlag(z16, 1)
        assert GetEventFlag(z16) != 0
    elif GetEventFlag(203600) != 0:
        """State 6: First encounter: Talk: Part 2: 1_SubState"""
        # talk:75200100:"Phew..."
        assert talk_m10_17_x0(text14=75200100, z62=0, z63=0)
        """State 8: First encounter: Talk: Part 2: 2_SubState"""
        # talk:75200110:"Heh heh. You are an odd one."
        assert talk_m10_17_x1(text8=75200110, z42=0, z60=-1, z61=0)
        """State 9: First encounter: Talk: Part 2: 3_SubState"""
        # talk:75200120:"Normally, people keep a safe distance\nwhen they see this mask. But you..."
        assert talk_m10_17_x1(text8=75200120, z42=203601, z60=-1, z61=0)
        """State 3: First encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z15, 1)
        assert GetEventFlag(z15) != 0
    else:
        """State 5: First encounter: Talk: Part 1_SubState"""
        # talk:75200000:"What is it?"
        assert talk_m10_17_x0(text14=75200000, z62=203600, z63=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_17_x25(z16=102486, z15=102481, z17=102501):
    """Woman Knight: Second encounter: Conversation
    z16: Generation stop: Global event flag
    z15: Encounter: Global event flag
    z17: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter second time: Start"""
    if GetEventFlag(203614) != 0:
        """State 10: Encounter 2nd time: Speak: Part 5 (Single loop) _SubState"""
        # talk:75201000:"I'm sorry...to burden you with talk of my fate."
        assert talk_m10_17_x0(text14=75201000, z62=0, z63=0)
        """State 3: 2nd encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z15, 1)
        assert GetEventFlag(z15) != 0
    elif GetEventFlag(203613) != 0:
        """State 9: Encounter second time: Talk: Part 5: 1_SubState"""
        # talk:75200900:"Have you heard of the Undead?\nThese poor souls affected by the curse."
        assert talk_m10_17_x0(text14=75200900, z62=0, z63=0)
        """State 13: Encounter second time: Talk: Part 5: 2_SubState"""
        # talk:75200910:"An Undead gradually loses his humanity,\nuntil his wits degrade completely."
        assert talk_m10_17_x1(text8=75200910, z42=0, z60=-1, z61=0)
        """State 14: Encounter second time: Speak: Part 5: 3_SubState"""
        # talk:75200960:"I can only hope...that they are."
        assert talk_m10_17_x1(text8=75200960, z42=203614, z60=-1, z61=0)
        """State 4: Second encounter: White phantom can appear: Set flag"""
        SetEventFlag(z17, 1)
        assert GetEventFlag(z17) != 0
        """State 2: Second encounter: Stop generation"""
        SetEventFlag(z16, 1)
        assert GetEventFlag(z16) != 0
    elif GetEventFlag(203612) != 0:
        """State 8: Encounter 2nd time: Talk: 4_SubState"""
        # talk:75200800:"I was raised to wield a sword from birth."
        assert talk_m10_17_x0(text14=75200800, z62=203613, z63=0)
        Goto('L0')
    elif GetEventFlag(203611) != 0:
        """State 7: Encounter second time: Talk: Part 3_SubState"""
        # talk:75200700:"Our land of Mirrah is surrounded by enemies,\nand constantly at war."
        assert talk_m10_17_x0(text14=75200700, z62=203612, z63=0)
        Goto('L0')
    elif GetEventFlag(203610) != 0:
        """State 6: Encounter second time: Speak: Part 2_SubState"""
        # lot:1752010:Human Effigy, talk:75200600:"Ah, yes, I have not thanked you\nfor humouring me the other day.", talk:75200620:"Of course, I've no idea what it is.\nHeh heh."
        assert (talk_m10_17_x19(lot7=1752010, z22=102495, text4=75200600, text5=75200620, z23=203611,
                z18=0, z24=0, z25=0))
        Goto('L0')
    else:
        """State 5: Encounter second time: Speak: Part 1: 1_SubState"""
        # talk:75200500:"I thought that might be you.\nYou haven't changed a bit, have you? Heh heh."
        assert talk_m10_17_x0(text14=75200500, z62=0, z63=0)
        """State 11: Encounter second time: Talk: Part 1: 2_SubState"""
        # talk:75200520:"A wretched place, indeed, but not \nwithout traces of its former glory."
        assert talk_m10_17_x1(text8=75200520, z42=0, z60=-1, z61=0)
        """State 12: Encounter second time: Talk: Part 1: 3_SubState"""
        # talk:75200530:"What could have caused such degradation?"
        assert talk_m10_17_x1(text8=75200530, z42=203610, z60=-1, z61=0)
        Goto('L0')
    """State 15: End state"""
    return 0

def talk_m10_17_x26(z16=102486, z15=102481, z17=102501):
    """Woman Knight: Encounter 3rd: Conversation
    z16: Generation stop: Global event flag
    z15: Encounter: Global event flag
    z17: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 3rd: Start"""
    if GetEventFlag(203622) != 0:
        """State 8: Encounter 3rd time: Talk: 4_SubState"""
        # talk:75201400:"If only someone would hear my tale..."
        assert talk_m10_17_x0(text14=75201400, z62=203623, z63=0)
        """State 4: 3rd encounter: White phantom can appear: Set flag"""
        SetEventFlag(z17, 1)
        assert GetEventFlag(z17) != 0
        """State 2: Encounter 3rd: Stop generation"""
        SetEventFlag(z16, 1)
        assert GetEventFlag(z16) != 0
    elif GetEventFlag(203621) != 0:
        """State 7: Encounter third time: Speak: Part 3: 1_SubState"""
        # talk:75201300:"I had an older brother. We learned to fence together."
        assert talk_m10_17_x0(text14=75201300, z62=0, z63=0)
        """State 11: Encounter third time: Speak: Part 3: 2_SubState"""
        # talk:75201340:"But then, one day...he was gone,\nlost without a trace."
        assert talk_m10_17_x1(text8=75201340, z42=203622, z60=-1, z61=0)
        """State 3: 3rd encounter: Set flag during encounter"""
        Label('L0')
        SetEventFlag(z15, 1)
        assert GetEventFlag(z15) != 0
    elif GetEventFlag(203620) != 0:
        """State 6: Encounter 3rd time: Speak: Part 2: 1_SubState"""
        # talk:75201200:"I've found my thoughts growing hazy."
        assert talk_m10_17_x0(text14=75201200, z62=0, z63=0)
        """State 9: Encounter third time: Talk: Part 2: 2_SubState"""
        # talk:75201220:"The curse is doing its work upon me."
        assert talk_m10_17_x1(text8=75201220, z42=0, z60=-1, z61=0)
        """State 10: Encounter third time: Speak: Part 2: 3_SubState"""
        # talk:75201230:"I am frightened... Terribly so..."
        assert talk_m10_17_x1(text8=75201230, z42=203621, z60=-1, z61=0)
        Goto('L0')
    else:
        """State 5: Encounter 3rd time: Speak: Part 1_SubState"""
        # lot:1752020:Ring of Steel Protection+1, talk:75201100:"Still on the road, are you?"
        assert talk_m10_17_x20(lot6=1752020, z19=102496, text3=75201100, z20=203620, z21=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_17_x27(z16=102486, z15=102481, z17=102501):
    """Woman Knight: Encounter 4th: Conversation
    z16: Generation stop: Global event flag
    z15: Encounter: Global event flag
    z17: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 4th: Start"""
    if GetEventFlag(203632) != 0:
        """State 8: Encounter 4th: Speak: Part 4_SubState"""
        # talk:75201800:"Sometimes, I feel obsessed...\nwith this insignificant thing called "self"."
        assert talk_m10_17_x0(text14=75201800, z62=203633, z63=0)
        """State 4: 4th encounter: White phantom can appear: Set flag"""
        SetEventFlag(z17, 1)
        assert GetEventFlag(z17) != 0
        """State 2: Encounter 4th: Stop generation"""
        SetEventFlag(z16, 1)
        assert GetEventFlag(z16) != 0
    elif GetEventFlag(203631) != 0:
        """State 7: Encounter 4th: Speak: Part 3_SubState"""
        # talk:75201700:"Loss frightens me no end.\nLoss of memory, loss of self."
        assert talk_m10_17_x0(text14=75201700, z62=203632, z63=0)
        """State 3: 4th encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z15, 1)
        assert GetEventFlag(z15) != 0
    elif GetEventFlag(203630) != 0:
        """State 6: Encounter 4th: Speak: Part 2: 1_SubState"""
        # talk:75201600:"What is this curse?"
        assert talk_m10_17_x0(text14=75201600, z62=0, z63=0)
        """State 9: Encounter 4th: Speak: Part 2: 2_SubState"""
        # talk:75201610:"The question rings in my mind,\nbut I haven't the focus to answer it."
        assert talk_m10_17_x1(text8=75201610, z42=203631, z60=-1, z61=0)
        Goto('L0')
    else:
        """State 5: Encounter 4th: Speak: Part 1_SubState"""
        # talk:75201500:"Oh... You..."
        assert talk_m10_17_x0(text14=75201500, z62=203630, z63=0)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_17_x28(text8=76200600, text9=76200700, text10=76200800, z41=102625, z42=204305):
    """[Lib] Menu Exit: Emigration Mes
    text8: Conversation ID (at the time of purchase)
    text9: Conversation ID (when not purchased)
    text10: Conversation ID (Migration decision)
    z41: Emigration: Global event flag
    z42: Emigration: Global conversation flag
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(z41) != 0 and GetEventFlag(z42) != 1:
        """State 4: Menu: Leaving: Relocation decision_SubState"""
        assert talk_m10_17_x1(text8=text10, z42=z42, z60=-1, z61=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Menu: Leave: At purchase_SubState"""
        assert talk_m10_17_x1(text8=text8, z42=0, z60=-1, z61=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Menu: Leave: Non-Purchase_SubState"""
        assert talk_m10_17_x1(text8=text9, z42=0, z60=-1, z61=0)
    """State 5: End state"""
    return 0

def talk_m10_17_x29(z26=117020164, z27=102343, z28=102346):
    """[Lib] Dwarf: Conversation
    z26: Contact: Area and other flags
    z27: Emigration permission: Global event flag
    z28: Shop list: Global event flag
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    SetEventFlag(z28, 1)
    if GetEventFlag(202900) != 0:
        """State 4: Dwarf: Greetings_SubState"""
        assert talk_m10_17_x31(z26=z26, z27=z27)
    else:
        """State 3: Dwarf: First conversation_SubState"""
        assert talk_m10_17_x30(z26=z26, z27=z27)
    """State 5: Dwarf: NPC menu_SubState"""
    assert talk_m10_17_x32()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_17_x30(z26=117020164, z27=102343):
    """Dwarf: First conversation
    z26: Contact: Area and other flags
    z27: Emigration permission: Global event flag
    """
    """State 0,1,3: Speak: Part 1: 1_SubState"""
    # talk:72600000:"Who you?"
    assert talk_m10_17_x0(text14=72600000, z62=202900, z63=0)
    """State 4: Talk: Part 1: 2_SubState"""
    # talk:72600060:"With Gavlan, you wheel?\nYou deal! Gah hah!"
    assert talk_m10_17_x1(text8=72600060, z42=202900, z60=-1, z61=0)
    """State 2: First conversation: Set contact flag"""
    SetEventFlag(z27, 1)
    SetEventFlag(z26, 1)
    assert GetEventFlag(z26) != 0
    """State 5: End state"""
    return 0

def talk_m10_17_x31(z26=117020164, z27=102343):
    """Dwarf: Greeting
    z26: Contact: Area and other flags
    z27: Emigration permission: Global event flag
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z26) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 7: Talk to _continuous 1_SubState"""
            # talk:72600100:"What? You want?"
            assert talk_m10_17_x0(text14=72600100, z62=0, z63=0)
        else:
            """State 8: Talk to _continuous 2_SubState"""
            # talk:72600200:"Umm...You want? Want what?"
            assert talk_m10_17_x0(text14=72600200, z62=0, z63=0)
    else:
        """State 4: Long time no see: branch"""
        if GetEventFlag(202904) != 0:
            """State 5: Long time no see: Flag initialization"""
            SetEventFlag(202901, 0)
            SetEventFlag(202902, 0)
            SetEventFlag(202903, 0)
            SetEventFlag(202904, 0)
            """State 9: Talk to me after a long time 1_SubState"""
            Label('L0')
            # talk:72600300:"Umm...Gavlan know you."
            assert talk_m10_17_x0(text14=72600300, z62=202901, z63=0)
        elif GetEventFlag(202903) != 0:
            """State 12: Talk to _After a long time 4_SubState"""
            # talk:72600600:"You, again.\nGavlan, meet you again."
            assert talk_m10_17_x0(text14=72600600, z62=202904, z63=0)
        elif GetEventFlag(202902) != 0:
            """State 11: Talk to _After a long time 3_SubState"""
            # talk:72600500:"Oh Gavlan, know you.\nWhat you want?"
            assert talk_m10_17_x0(text14=72600500, z62=202903, z63=0)
        elif GetEventFlag(202901) != 0:
            """State 10: Talk to _After a long time 2_SubState"""
            # talk:72600400:"Make deal with Gavlan?"
            assert talk_m10_17_x0(text14=72600400, z62=202902, z63=0)
        else:
            Goto('L0')
        """State 6: Greeting: Contact flag setting"""
        SetEventFlag(z27, 1)
        SetEventFlag(z26, 1)
        assert GetEventFlag(z26) != 0
    """State 13: End state"""
    return 0

def talk_m10_17_x32():
    """Dwarf: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 6: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_17_x13(z43=0, z44=220, z45=72600000, z46=0)
        if call.Get() == 2:
            """State 5: Dwarf: Menu conversation_SubState"""
            call = talk_m10_17_x33()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3: [Lib] Exit menu: General purpose_SubState"""
            # talk:72600700:"Many deal...many thanks! Gah hah!", talk:72600800:"You? Go home?"
            assert talk_m10_17_x14(text12=72600700, text13=72600800)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuResults()
        """State 7: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:72600900:"Umm..."
    assert talk_m10_17_x15(text11=72600900)
    Goto('L0')

def talk_m10_17_x33():
    """Dwarf: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102355) != 1 and (GetGlobalVariable(200) > NpcInfoValue(7260, 0)) != 0 and GetEventFlag(104130)
        != 1):
        """State 3: Equipment transfer (Condition: Total purchase amount is above a certain level) _SubState"""
        # lot:1726000:Gyrm Greataxe, talk:72606000:"Wheel...deal..."
        assert talk_m10_17_x18(lot8=1726000, z29=102355, text6=72606000)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:72605000:"Umm...You strong."
        assert talk_m10_17_x1(text8=72605000, z42=0, z60=-1, z61=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_17_x34(mode1=1):
    """[Lib] Pledge cancellation: Overwrite
    mode1: Main pledge: pledge type
    """
    """State 0,1: Overwrite: Start"""
    if (not GetPlayerCovenant()) != 0:
        pass
    elif (GetPlayerCovenant() == mode1) != 1:
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

def talk_m10_17_x35(text7=_, z38=0, z39=20, z40=80):
    """[Lib] Conversation: Hostile display only
    text7: Conversation ID
    z38: Conversation flag
    z39: Display distance
    z40: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), z39)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z38, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_17_x36(goods1=62120000, z33=60, z34=210, z35=-9999, mode2=1, lot9=2007000, z36=103120, z37=103132):
    """[Lib] Menu item: Dedicated: OBJ
    goods1: Dedication item ID
    z33: Current pledge rank: Area variable
    z34: Last pledge rank: global variable
    z35: Event action
    mode2: Pledge type
    lot9: Transfer: Item lottery
    z36: Transfer: Global event flag
    z37: Ranking 3 items: Global event flag
    """
    """State 0,1: Votive: Start"""
    if (GetPlayerCovenant() == mode2) != 1:
        """State 8: Votive: Confirmation dialog not signed"""
        # action:1314:"You must belong to this covenant\nto make an offering"
        assert talk_m10_17_x16(action5=1314)
    elif GetEventFlag(z37) != 0 and (GetGlobalVariable(z34) == 3) != 0:
        """State 4: Dedication: No more dedication confirmation dialog_SubState"""
        Label('L0')
        # action:1309:"There is nothing more to offer.\nYou have done fine work."
        assert talk_m10_17_x16(action5=1309)
    elif GetEventFlag(z37) != 0 and (GetPlayerCovenantLevel(mode2) > 3) != 0:
        Goto('L0')
    else:
        """State 6: Dedication: Dedication selection dialog_SubState"""
        # action:1306:"Offer\n%s?"
        call = talk_m10_17_x37(action4=1306, goods1=goods1)
        # goods:62120000:Sunlight Medal
        if call.Get() == 0 and (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 5: Votive: Confirmation of possession of possession _SubState"""
            # action:1310:"You have no offerings"
            assert talk_m10_17_x16(action5=1310)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Dedication: OBJ_SubState"""
            assert talk_m10_17_x43(z35=z35, goods1=goods1, z33=z33, mode2=mode2, lot9=lot9, z36=z36)
            """State 3: Delivery confirmation dialog_SubState"""
            # action:1307:"Your devotion to your\ncovenant has deepened"
            assert talk_m10_17_x16(action5=1307)
            """State 10: Rank up: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 2: Votive: Finish"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_17_x37(action4=1306, goods1=62120000):
    """[Lib] Selection dialog: Item display
    action4: Dialog: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    # action:1306:"Offer\n%s?", goods:62120000:Sunlight Medal
    DisplayOwnYesNoMenu(action4, 0, -1, 2, goods1, 0)
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

def talk_m10_17_x38(z31=_, z32=0):
    """[Lib] Menu item: Gesture
    z31: Gesture: Item ID
    z32: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_17_x45(z31=z31, z32=z32)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_17_x39(action3=1203, val1=2000):
    """[Lib] selection dialog: Soul amount
    action3: Dialog: Text ID
    val1: Soul Amount: Argument
    """
    """State 0,1: Selection dialog: Display"""
    # action:1203:"Pay souls?\nSouls needed: %d"
    DisplayOwnYesNoMenu(action3, 0, -1, 1, val1, 0)
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

def talk_m10_17_x40(z11=-9999, mode1=1, lot4=2007000, z8=103120):
    """[Lib] Event action: Pledge: OBJ
    z11: Event action
    mode1: Pledge type
    lot4: Item lottery ID
    z8: Item transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z11)
    """State 2: IventAction: Motion_Waiting"""
    # lot:2007000:Sun Seal
    if (GetEventFlag(z8) != 1 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0 and CanGetItemLot(lot4,
        1) != 1):
        """State 5: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(mode1)
        # lot:2007000:Sun Seal
        if (GetPlayerCovenant() == mode1) != 0 and CanGetItemLot(lot4, 1) != 1 and GetEventFlag(z8) != 1:
            """State 6: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_17_x46(z30=1011, lot1=lot4)
        elif (GetPlayerCovenant() == mode1) != 0:
            pass
    elif GetEventFlag(z8) != 0 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        Goto('L0')
    elif (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 4: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(mode1)
        SetEventFlag(z8, 1)
        # lot:2007000:Sun Seal
        AwardItem(lot4, 1)
        assert (GetPlayerCovenant() == mode1) != 0
    """State 3,7: End state"""
    return 0

def talk_m10_17_x41(mode1=1, z10=9, lot4=2007000, z8=103120, action1=1330, action2=1340, z9=117020171):
    """[Lib] Pledge conclusion: OBJ
    mode1: Pledge type
    z10: Event action
    lot4: Item lottery ID
    z8: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z9: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z9, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_17_x12(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_17_x16(action5=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge: OBJ_SubState"""
            Label('L1')
            assert talk_m10_17_x40(z11=-9999, mode1=mode1, lot4=lot4, z8=z8) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_17_x16(action5=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_17_x12(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_17_x34(mode1=mode1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_17_x42(mode1=1, z7=-9999, lot4=2007000, z8=103120, action1=1330, action2=1340, z9=117020171):
    """[Lib] Menu item: Make a pledge: OBJ
    mode1: Pledge name
    z7: Event action
    lot4: Item lottery ID
    z8: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z9: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == mode1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_17_x16(action5=1305)
    else:
        """State 4: [Lib] Pledge conclusion: OBJ_SubState"""
        call = talk_m10_17_x41(mode1=mode1, z10=9, lot4=lot4, z8=z8, action1=action1, action2=action2,
                               z9=z9)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_17_x43(z35=-9999, goods1=62120000, z33=60, mode2=1, lot9=2007000, z36=103120):
    """[Lib] Event action: Dedication: OBJ
    z35: Event action
    goods1: Special Offer: Event Item
    z33: Current pledge level: area variable
    mode2: Pledge type
    lot9: Transfer: Item lottery
    z36: Transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z35)
    assert PlayerIsInEventAction(z35) != 0
    """State 2: IventAction: Motion_Waiting"""
    if GetEventFlag(z36) != 0 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 5: Event action: votive delivery"""
        # goods:62120000:Sunlight Medal
        ConsumeItem(goods1, 1)
        AddPlayerCovenantContribution(mode2, 1)
        SetAreaVariable(z33, GetPlayerCovenantLevel(mode2))
        SaveExecution()
    elif (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 6: Event action: Votive delivery: Item transfer"""
        # lot:2007000:Sun Seal
        AwardItem(lot9, 1)
        SetEventFlag(z36, 1)
        # goods:62120000:Sunlight Medal
        ConsumeItem(goods1, 1)
        AddPlayerCovenantContribution(mode2, 1)
        SetAreaVariable(z33, GetPlayerCovenantLevel(mode2))
        SaveExecution()
    """State 4,7: End state"""
    return 0

def talk_m10_17_x44(z2=60, z3=210, lot1=2007011, lot2=2007012, lot3=2007013, z4=103130, z5=103131, z6=103132):
    """[Lib] Menu item: Dedicated: OBJ: Pledge item award
    z2: Current pledge rank: Area variable
    z3: Last pledge rank: global variable
    lot1: Ranking 1: Item lottery
    lot2: Ranking 2: Item lottery
    lot3: Ranking 3: Item lottery
    z4: Ranking 1: Global event flag
    z5: Ranking 2: Global event flag
    z6: Ranking 3: Global event flag
    """
    """State 0,3: Dedication: rank up judgment"""
    if (GetGlobalVariable(z3) > GetAreaVariable(z2)) != 1:
        """State 8: Pledge Rank Up Confirmation Dialog_SubState"""
        Label('L0')
        # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
        assert talk_m10_17_x16(action5=1308)
        """State 2: Pledge ranking judgment"""
        # lot:2007011:Sunlight Parma
        if (GetAreaVariable(z2) > 1) != 0 and GetEventFlag(z4) != 1 and CanGetItemLot(lot1, 1) != 1:
            """State 9: [Lib] Inventory full dialog (ranking 1) _SubState"""
            assert talk_m10_17_x46(z30=1011, lot1=lot1)
        elif (GetAreaVariable(z2) > 1) != 0 and GetEventFlag(z4) != 1:
            """State 5: Pledge ranking 1 item acquisition dialog_SubState"""
            assert talk_m10_17_x17(lot1=lot1, z4=z4)
            """State 1: Pledge ranking: area variable ⇒ global variable"""
            Label('L1')
            SetGlobalVariable(z3, GetAreaVariable(z2))
        # lot:2007012:Sun Sword
        elif (GetAreaVariable(z2) > 2) != 0 and GetEventFlag(z5) != 1 and CanGetItemLot(lot2, 1) != 1:
            """State 10: [Lib] Inventory full dialog (ranking 2) _SubState"""
            assert talk_m10_17_x46(z30=1011, lot1=lot2)
        elif (GetAreaVariable(z2) > 2) != 0 and GetEventFlag(z5) != 1:
            """State 6: Pledge ranking 2 item acquisition dialog_SubState"""
            assert talk_m10_17_x17(lot1=lot2, z4=z5)
            Goto('L1')
        # lot:2007013:Sunlight Spear
        elif (GetAreaVariable(z2) > 3) != 0 and GetEventFlag(z6) != 1 and CanGetItemLot(lot3, 1) != 1:
            """State 11: [Lib] Inventory full dialog (ranking 3) _SubState"""
            assert talk_m10_17_x46(z30=1011, lot1=lot3)
        elif (GetAreaVariable(z2) > 3) != 0 and GetEventFlag(z6) != 1:
            """State 7: Pledge ranking 3 item acquisition dialog_SubState"""
            assert talk_m10_17_x17(lot1=lot3, z4=z6)
            Goto('L1')
        else:
            Goto('L1')
    elif (GetGlobalVariable(z3) > 1) != 0 and GetEventFlag(z4) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z3) > 2) != 0 and GetEventFlag(z5) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z3) > 3) != 0 and GetEventFlag(z6) != 1:
        Goto('L0')
    else:
        Goto('L1')
    """State 4: Pledge Ranking: End"""
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_17_x45(z31=_, z32=0):
    """[Lib] Get gesture dialog
    z31: Item ID
    z32: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(z31, 0, -1)
    SetEventFlag(z32, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_17_x46(z30=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z30: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_17_x47():
    """Ladder shop: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(117010110) != 0:
        """State 4: After ladder installation: Conversation_SubState"""
        Label('L0')
        assert talk_m10_17_x49()
    elif GetEventFlag(102160) != 0:
        Goto('L0')
    else:
        """State 3: Before installing the ladder: Conversation_SubState"""
        assert talk_m10_17_x48(val1=2000, z1=-2000)
    """State 5: End state"""
    return 0

def talk_m10_17_x48(val1=2000, z1=-2000):
    """Before installing the ladder: Conversation
    val1: Ladder price
    z1: Ladder price: Seoul subtraction
    """
    """State 0,1: Before installation: Start"""
    if GetEventFlag(201801) != 0 and GetEventFlag(102160) != 1:
        """State 6: Talk: Part 1: Review _SubState"""
        # talk:70404500:"...What? You don't have a choice, do you!"
        assert talk_m10_17_x0(text14=70404500, z62=0, z63=0)
        """State 9: Ladder installation selection dialog_SubState"""
        Label('L0')
        # action:1203:"Pay souls?\nSouls needed: %d"
        call = talk_m10_17_x39(action3=1203, val1=val1)
        if call.Get() == 0 and (CurrentSouls() > val1) != 0:
            """State 2,8: Before Ladder Shop Installation: Ladder Installation Poly Play_SubState"""
            assert talk_m10_17_x59(z1=z1)
            Goto('L1')
        elif call.Get() == 0:
            """State 7: Ladder installation Seoul shortage confirmation dialog_SubState"""
            # action:1016:"Insufficient souls"
            assert talk_m10_17_x16(action5=1016)
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
        """State 5: Speak: Part 2: NO_SubState"""
        # talk:70400300:"...Hell, of course it's not free!"
        assert talk_m10_17_x1(text8=70400300, z42=0, z60=-1, z61=0)
    elif GetEventFlag(201800) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:70400100:"...You want to climb down here?"
        assert talk_m10_17_x0(text14=70400100, z62=201801, z63=0)
        Goto('L0')
    else:
        """State 3: Talk: Part 1: First Look _SubState"""
        # talk:70400000:"...Shush, you eejit, stay quiet!"
        assert talk_m10_17_x0(text14=70400000, z62=201800, z63=0)
    """State 10: End state"""
    Label('L1')
    return 0

def talk_m10_17_x49():
    """After installing the ladder: Conversation"""
    """State 0,1,2: Talk to: After the ladder: Single loop_SubState"""
    # talk:70400500:"...Oh, what is it? What do you need now?"
    assert talk_m10_17_x0(text14=70400500, z62=0, z63=0)
    """State 3: Ladder shop: NPC menu_SubState"""
    assert talk_m10_17_x50()
    """State 4: End state"""
    return 0

def talk_m10_17_x50():
    """Ladder shop: NPC menu"""
    """State 0: Start state"""
    while True:
        """State 1: Menu: Start"""
        ClearNpcMenuResults()
        """State 3: Menu: Branch"""
        # goods:63016000:"Prostration" Gesture
        if (ItemCount(63016000, 1, 1, 0) > 1) != 0:
            """State 8: [Lib] Menu start: No gesture _SubState"""
            call = talk_m10_17_x13(z43=0, z44=220, z45=70400001, z46=0)
            if call.Get() == 2:
                """State 5: Ladder shop: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_17_x51()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 6: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:70400600:"...No mate, these deals, they won't last forever...", talk:70400700:"...Fine, then, all the best..."
                assert talk_m10_17_x14(text12=70400600, text13=70400700)
        else:
            """State 4: [Lib] Menu start: With gesture_SubState"""
            call = talk_m10_17_x13(z43=0, z44=220, z45=70400000, z46=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 10:
                """State 9: [Lib] Menu item: Gesture_SubState"""
                call = talk_m10_17_x38(z31=63016000, z32=0)
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
        ClearNpcMenuResults()
        """State 10: End state"""
        return 0
    """State 7: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:70400800:"...Oi! Downright rude, really..."
    assert talk_m10_17_x15(text11=70400800)
    Goto('L2')

def talk_m10_17_x51():
    """Ladder shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(201805) != 0:
        """State 7: Menu conversation: 5_SubState"""
        assert talk_m10_17_x1(text8=70405400, z42=0, z60=-1, z61=0)
    elif GetEventFlag(201804) != 0:
        """State 6: Menu conversation: 4_SubState"""
        assert talk_m10_17_x1(text8=70405300, z42=201805, z60=-1, z61=0)
    elif GetEventFlag(201803) != 0:
        """State 5: Menu conversation: 3_SubState"""
        assert talk_m10_17_x1(text8=70405200, z42=201804, z60=-1, z61=0)
    elif GetEventFlag(201802) != 0:
        """State 4: Menu conversation: 2_SubState"""
        assert talk_m10_17_x1(text8=70405100, z42=201803, z60=-1, z61=0)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        # talk:70405000:"You ungrateful little git!"
        assert talk_m10_17_x1(text8=70405000, z42=201802, z60=-1, z61=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m10_17_x52():
    """Material shop: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Material shop: First conversation_SubState"""
    assert talk_m10_17_x53()
    """State 4: Material shop: NPC menu_SubState"""
    assert talk_m10_17_x54()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_17_x53():
    """Material shop: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(204300) != 0:
        """State 4: [Lib] Conversation: Greeting: General purpose_SubState"""
        # talk:76200200:"What? Do you need something?", talk:76200300:"I'll provide whatever service you need.\nFor a fair price, of course!", talk:76200400:"You've been long away. What would you like?"
        assert talk_m10_17_x11(z47=117020154, text14=76200200, text15=76200300, text16=76200400, text17=76200400)
    else:
        """State 3: Talk: First_SubState"""
        # talk:76200000:"Are you a traveller?"
        assert talk_m10_17_x0(text14=76200000, z62=204300, z63=0)
        """State 2: First conversation: contact flag"""
        SetEventFlag(117020154, 1)
    """State 5: End state"""
    return 0

def talk_m10_17_x54():
    """Material shop: NPC menu"""
    """State 0: Start state"""
    while True:
        """State 1,2: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_17_x13(z43=0, z44=220, z45=76200000, z46=0)
        if call.Get() == 2:
            """State 5: Material shop: Menu conversation_SubState"""
            call = talk_m10_17_x55()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Menu exit: Emigration Mes_SubState"""
            # talk:76200600:"Visit me again, whenever you please.", talk:76200700:"No interest? Suit yourself.", talk:76200800:"I suppose it's about time I moved shop..."
            assert talk_m10_17_x28(text8=76200600, text9=76200700, text10=76200800, z41=102625, z42=204305)
        """State 6: End state"""
        Label('L0')
        return 0
    """State 3: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76200900:"Oi! Mind your manners!"
    assert talk_m10_17_x15(text11=76200900)
    Goto('L0')

def talk_m10_17_x55():
    """Material shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102620) != 1 and (GetGlobalVariable(221) > NpcInfoValue(7620, 0)) != 0 and GetEventFlag(104260)
        != 1):
        """State 8: Equipment transfer (Conditions: Shop purchase total is above a certain level) _SubState"""
        # lot:1762000:Twinkling Titanite, talk:76206000:"Bye for now. Heh heh..."
        assert talk_m10_17_x22(lot5=1762000, z12=102620, text1=76206000, text2=76206010, z13=0, z14=0)
    elif GetEventFlag(204304) != 0:
        """State 7: Menu conversation: 5_SubState"""
        call = talk_m10_17_x1(text8=76205400, z42=0, z60=-1, z61=0)
        if call.Done() and GetEventFlag(102625) != 1:
            """State 2: Menu conversation: Set migration permission flag"""
            SetEventFlag(102625, 1)
            assert GetEventFlag(102625) != 0
        elif call.Done():
            pass
    elif GetEventFlag(204302) != 0:
        """State 6: Menu conversation: 4_SubState"""
        assert talk_m10_17_x1(text8=76205300, z42=204304, z60=-1, z61=0)
    elif GetEventFlag(204301) != 0:
        """State 5: Menu conversation: 2_SubState"""
        assert talk_m10_17_x1(text8=76205100, z42=204302, z60=-1, z61=0)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:76205000:"Fine, if that's the way it is..."
        assert talk_m10_17_x1(text8=76205000, z42=204301, z60=-1, z61=0)
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_17_x56():
    """Patch: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    if GetEventFlag(102441) != 1 and GetEventFlag(102452) != 0 and GetEventFlag(104170) != 1:
        """State 3: Equipment transfer (condition: white phantom summon achievement) _SubState"""
        # lot:1744010:Pate's Spear, talk:74406000:"Heh heh heh..."
        assert (talk_m10_17_x19(lot7=1744010, z22=102441, text4=74406000, text5=74406010, z23=0, z18=0,
                z24=0, z25=0))
    elif GetEventFlag(117000148) != 0:
        """State 5: Patch: Get Treasure: Conversation_SubState"""
        assert talk_m10_17_x58()
    else:
        """State 4: Patch: Treasure not available: Conversation_SubState"""
        call = talk_m10_17_x57()
        if call.Done():
            pass
        elif GetEventFlag(117000148) != 0:
            pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_17_x57():
    """Patch: Treasure not available: Conversation"""
    """State 0,1,2: Treasure not available: Talk: Part 1_SubState"""
    # talk:74400800:"Well, we meet again."
    assert talk_m10_17_x0(text14=74400800, z62=0, z63=0)
    """State 3: End state"""
    return 0

def talk_m10_17_x58():
    """Patch: Treasure Acquisition: Conversation"""
    """State 0,1: Treasure acquisition: start"""
    if GetEventFlag(203441) != 0:
        """State 5: Treasure Acquisition: Speak: Part 3_SubState"""
        # talk:74401100:"You be careful, too, my friend.\nFor trust can be a dangerous thing."
        assert talk_m10_17_x0(text14=74401100, z62=0, z63=0)
    elif GetEventFlag(203440) != 0:
        """State 4: Treasure acquisition: Talk: Part 2_SubState"""
        # talk:74401000:"I prefer a more cautious approach.\nIt's hard to know who to even trust these days."
        call = talk_m10_17_x0(text14=74401000, z62=203441, z63=0)
        if call.Done() and GetEventFlag(102451) != 1:
            """State 2: Treasure acquisition: Set migration permission flag"""
            SetEventFlag(102451, 1)
            assert GetEventFlag(102451) != 0
        elif call.Done():
            pass
    else:
        """State 3: Treasure Acquisition: Talk: Part 1_SubState"""
        # talk:74400900:"Well, good to see that you survived."
        assert talk_m10_17_x0(text14=74400900, z62=203440, z63=0)
    """State 6: End state"""
    return 0

def talk_m10_17_x59(z1=-2000):
    """Before installing the ladder shop: Ladder installation poly drama
    z1: Soul subtraction
    """
    """State 0,3,5: Poly play: First half: Message_SubState"""
    # talk:70400200:"...All right, it'll be just a moment..."
    assert talk_m10_17_x1(text8=70400200, z42=0, z60=-1, z61=0)
    """State 1: Conversation: Poly play"""
    SetEventFlag(117020117, 1)
    assert GetEventFlag(117020117) != 0
    """State 2: Conversation: Poly drama playback standby"""
    assert GetEventFlag(117020117) != 1
    """State 4: Before installation: Seoul subtraction"""
    AddSouls(z1)
    SetEventFlag(102165, 1)
    SetEventFlag(102160, 1)
    """State 6: Poly play: Second half: Message_SubState"""
    # talk:70400400:"...Ahhh...Go on ahead, I won't offer this deal twice..."
    assert talk_m10_17_x1(text8=70400400, z42=0, z60=-1, z61=0)
    """State 7: End state"""
    return 0

