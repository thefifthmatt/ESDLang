# -*- coding: utf-8 -*-
def talk_m10_18_7260():
    """Dwarf (Hidden Port)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_18_x9(flag13=103631, flag14=104131, flag15=118020141)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_18_x3(text10=72609200, z12=0, z13=20, z14=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_18_x6(flag12=118020142, text21=72609500, text22=72609500, z19=72609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_18_x7(text24=72609600, z21=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: [Lib] Dwarf: Conversation_SubState"""
                call = talk_m10_18_x27(flag8=118020144, z7=102340, z8=0)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_18_x5(text25=72609400, text26=72609410, text27=72609420, text28=72609400,
                                          flag16=118020145, flag17=118020146)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_18_x4(flag18=103630, text29=72609100, z22=0, z23=103631)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(118020146) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(118020145) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_18_x8(text23=72609300, z20=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_18_7520():
    """Woman Knight (Hidden Port)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_18_x9(flag13=103691, flag14=104191, flag15=118020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_18_x3(text10=75209200, z12=0, z13=20, z14=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_18_x6(flag12=118020102, text21=75209500, text22=75209500, z19=75209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_18_x7(text24=75209600, z21=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: [Lib] Female knight: Before last: Conversation_SubState"""
                call = talk_m10_18_x21(flag3=102482, flag4=102487, flag5=102502, z1=118020109)
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_18_x5(text25=75209400, text26=75209410, text27=75209420, text28=75209400,
                                          flag16=118020105, flag17=118020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_18_x4(flag18=103690, text29=75209100, z22=0, z23=103691)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(118020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(118020105) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_18_x8(text23=75209300, z20=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_18_7660():
    """Magician (Hidden Port)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_18_x9(flag13=103801, flag14=104301, flag15=118020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_18_x3(text10=76609200, z12=0, z13=20, z14=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_18_x6(flag12=118020122, text21=76609500, text22=76609500, z19=76609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_18_x7(text24=76609600, z21=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Magician: Conversation_SubState"""
                call = talk_m10_18_x34()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_18_x5(text25=76609400, text26=76609410, text27=76609400, text28=76609410,
                                          flag16=118020125, flag17=118020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_18_x4(flag18=103800, text29=76609100, z22=0, z23=103801)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(118020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(118020125) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_18_x8(text23=76609300, z20=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_18_x0(text17=_, z26=_, z27=0):
    """[Lib] Conversation: General purpose
    text17: Conversation ID
    z26: Conversation flag
    z27: Global event flag
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
    SetEventFlag(z26, 1)
    SetEventFlag(z27, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_18_x1(text1=_, flag2=_, z24=-1, z25=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    flag2: Conversation flag
    z24: Display distance
    z25: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z24)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(flag2, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_18_x2(text23=_, z20=0):
    """[Lib] Conversation: Event end
    text23: Conversation ID
    z20: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text23, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z20, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_18_x3(text10=_, z12=0, z13=20, z14=80):
    """[Lib] Reunion hostility
    text10: Conversation message ID
    z12: Conversation flag ID
    z13: Display distance
    z14: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_18_x32(text10=text10, z12=z12, z13=z13, z14=z14)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_18_x4(flag18=_, text29=_, z22=0, z23=_):
    """[Lib] First hostility
    flag18: Hostile: Global event flag
    text29: Conversation ID
    z22: Conversation flag
    z23: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag18, 1)
    SetEventFlag(z23, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag18) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_18_x1(text1=text29, flag2=z22, z24=-1, z25=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_18_x5(text25=_, text26=_, text27=_, text28=_, flag16=_, flag17=_):
    """[Lib] Hostile waiting
    text25: Conversation ID: 1 attacked
    text26: Conversation ID: Attacked 2
    text27: Conversation ID: 3 attacked
    text28: Conversation ID: 4 attacked
    flag16: No use: Area and other flags
    flag17: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag17) != 1, flag17, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag16) != 1, flag16, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_18_x1(text1=text28, flag2=0, z24=-1, z25=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_18_x1(text1=text27, flag2=0, z24=-1, z25=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_18_x1(text1=text26, flag2=0, z24=-1, z25=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_18_x1(text1=text25, flag2=0, z24=-1, z25=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_18_x6(flag12=_, text21=_, text22=_, z19=_):
    """[Lib] Hostile state
    flag12: Area and other flags: HP decreased
    text21: Conversation ID: HP drop 1
    text22: Conversation ID: HP drop 2
    z19: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag12) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_18_x10(text21=text21, flag12=flag12)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_18_x10(text21=text22, flag12=flag12)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_18_x10(text21=text22, flag12=flag12)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_18_x7(text24=_, z21=0):
    """[Lib] Death status
    text24: Conversation ID
    z21: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_18_x2(text23=text24, z20=z21)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_18_x8(text23=_, z20=0):
    """[Lib] Murder status
    text23: Conversation ID
    z20: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_18_x2(text23=text23, z20=z20)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_18_x9(flag13=_, flag14=_, flag15=_):
    """[Lib] Event: Branch
    flag13: Hostile flag
    flag14: death flag
    flag15: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag14) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag15) != 0
    elif GetEventFlag(flag13) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_18_x10(text21=_, flag12=_):
    """[Lib] Conversation: HP drop
    text21: Conversation ID
    flag12: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text21, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag12, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_18_x11(flag11=118020124, text17=76601000, text18=76601100, text19=76601200, text20=76601300):
    """[Lib] Conversation: Greeting: General
    flag11: Area other flag: Contact flag
    text17: Text ID: Talk to_continuous 1
    text18: Text ID: Talk to_continuous 2
    text19: Text ID: Talk to _After a long time 1
    text20: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(flag11) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_18_x0(text17=text17, z26=0, z27=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_18_x0(text17=text18, z26=0, z27=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_18_x0(text17=text19, z26=0, z27=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_18_x0(text17=text20, z26=0, z27=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(flag11, 1)
    """State 10: End state"""
    return 0

def talk_m10_18_x12(z15=0, z16=220, z17=_, z18=0):
    """[Lib] Menu start: General purpose
    z15: Camera parameter ID
    z16: Target Damipoly ID
    z17: NPC event parameter ID
    z18: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z18, z15, z16, z17)
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

def talk_m10_18_x13(text15=72600700, text16=72600800):
    """[Lib] Menu exit: General purpose
    text15: Conversation ID (at the time of purchase)
    text16: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_18_x1(text1=text15, flag2=0, z24=-1, z25=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_18_x1(text1=text16, flag2=0, z24=-1, z25=0)
    """State 4: End state"""
    return 0

def talk_m10_18_x14(text14=_):
    """[Lib] Menu cancellation: General purpose
    text14: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_18_x1(text1=text14, flag2=0, z24=-1, z25=0)
    """State 4: End state"""
    return 0

def talk_m10_18_x15(lot4=1766000, z10=102720, text8=76606000, text9=76606010):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z10: Global event flag
    text8: First half: Conversation ID
    text9: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_18_x1(text1=text8, flag2=0, z24=-1, z25=0)
    # lot:1766000:Northern Ritual Band+1
    if call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z11=1011, lot1=lot4)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_18_x16(lot3=lot4, z9=z10)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_18_x1(text1=text9, flag2=0, z24=-1, z25=0)
    """State 6: End state"""
    return 0

def talk_m10_18_x16(lot3=_, z9=_):
    """[Lib] Item acquisition dialog
    lot3: Item lottery ID
    z9: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z9, 1)
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_18_x17(lot3=1726000, z9=102355, text7=72606000):
    """[Lib] Equipment transfer: Mes⇒Item
    lot3: Item lottery ID
    z9: Global event flag
    text7: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_18_x1(text1=text7, flag2=0, z24=-1, z25=0)
    # lot:1726000:Gyrm Greataxe
    if call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z11=1011, lot1=lot3)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_18_x16(lot3=lot3, z9=z9)
    """State 5: End state"""
    return 0

def talk_m10_18_x18(lot2=_, flag7=_, text5=_, text6=_, z4=_, z1=_, z5=0, z6=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot2: Item lottery ID
    flag7: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z4: Conversation: Global conversation flag
    z1: Trophy acquisition: Area and other flags
    z5: Emigration permission: Global event flag
    z6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_18_x1(text1=text5, flag2=0, z24=-1, z25=0)
    if call.Done() and GetEventFlag(flag7) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z4, 1)
        SetEventFlag(z5, 1)
        SetEventFlag(z6, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_18_x1(text1=text6, flag2=0, z24=-1, z25=0)
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z11=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_18_x20(lot1=lot2, flag6=flag7, z2=z4, z3=z1, z5=z5, z6=z6)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_18_x19(lot1=1752020, flag6=102496, text4=75201100, z2=203620, z3=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot1: Item lottery ID
    flag6: Item transfer: Global event flag
    text4: Conversation ID
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: Conversation_SubState"""
    call = talk_m10_18_x1(text1=text4, flag2=0, z24=-1, z25=0)
    if call.Done() and GetEventFlag(flag6) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    # lot:1752020:Ring of Steel Protection+1
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z11=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_18_x20(lot1=lot1, flag6=flag6, z2=z2, z3=z3, z5=0, z6=0)
    """State 9: End state"""
    return 0

def talk_m10_18_x20(lot1=_, flag6=_, z2=_, z3=_, z5=0, z6=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    flag6: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z5: Emigration permission: Global event flag
    z6: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z6, 1)
    SetEventFlag(z5, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(flag6, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_18_x21(flag3=102482, flag4=102487, flag5=102502, z1=118020109):
    """[Lib] Woman Knight: Before Last: Conversation
    flag3: Encounter: Global event flag
    flag4: Generation establishment: Global event flag
    flag5: White Phantom Appearance: Global Event Flag
    z1: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203630) != 0 and GetEventFlag(flag3) != 0:
        """State 5: Woman Knight: Encounter 4th: Conversation_SubState"""
        Label('L0')
        assert talk_m10_18_x25(flag4=flag4, flag3=flag3, flag5=flag5)
    elif GetEventFlag(203623) != 0 and GetEventFlag(flag3) != 1:
        Goto('L0')
    elif GetEventFlag(203620) != 0 and GetEventFlag(flag3) != 0:
        """State 4: Woman Knight: Encounter 3rd: Conversation_SubState"""
        Label('L1')
        assert talk_m10_18_x24(flag4=flag4, flag3=flag3, flag5=flag5)
    elif GetEventFlag(203614) != 0 and GetEventFlag(flag3) != 1:
        Goto('L1')
    elif GetEventFlag(203610) != 0 and GetEventFlag(flag3) != 0:
        """State 3: Woman Knight: Encounter 2nd: Conversation_SubState"""
        Label('L2')
        assert talk_m10_18_x23(flag4=flag4, flag3=flag3, flag5=flag5)
    elif GetEventFlag(203602) != 0 and GetEventFlag(flag3) != 1:
        Goto('L2')
    elif GetEventFlag(203600) != 0 and GetEventFlag(flag3) != 0:
        """State 2: Woman Knight: First encounter: Conversation_SubState"""
        Label('L3')
        assert talk_m10_18_x22(flag4=flag4, flag3=flag3, flag5=flag5)
    else:
        Goto('L3')
    """State 7: End state"""
    Label('L4')
    return 0
    """Unused"""
    """State 6: Woman Knight: Equipment Transfer_SubState"""
    # lot:1752000:Mirrah Greatsword, talk:75206000:"Please...find my brother..."
    assert (talk_m10_18_x18(lot2=1752000, flag7=102497, text5=75206000, text6=75206010, z4=0, z1=z1,
            z5=0, z6=0))
    Goto('L4')

def talk_m10_18_x22(flag4=102487, flag3=102482, flag5=102502):
    """Woman Knight: First encounter: Conversation
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    flag5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: First encounter: Start"""
    if GetEventFlag(203601) != 0:
        """State 7: First encounter: Talk: Part 3: 1_SubState"""
        # talk:75200300:"You are an odd one, indeed.\nI've always made a point of avoiding people."
        assert talk_m10_18_x0(text17=75200300, z26=0, z27=0)
        """State 10: First encounter: Talk: Part 3: 2_SubState"""
        # talk:75200310:"While you've made a point of engaging me."
        assert talk_m10_18_x1(text1=75200310, flag2=0, z24=-1, z25=0)
        """State 11: First encounter: Talk: Part 3: 3_SubState"""
        # talk:75200320:"I can see that you are mid-journey.\nIf you require assistance, I will help you."
        assert talk_m10_18_x1(text1=75200320, flag2=203602, z24=-1, z25=0)
        """State 4: First encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
        """State 2: First encounter: stop generation"""
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203600) != 0:
        """State 6: First encounter: Talk: Part 2: 1_SubState"""
        # talk:75200100:"Phew..."
        assert talk_m10_18_x0(text17=75200100, z26=0, z27=0)
        """State 8: First encounter: Talk: Part 2: 2_SubState"""
        # talk:75200110:"Heh heh. You are an odd one."
        assert talk_m10_18_x1(text1=75200110, flag2=0, z24=-1, z25=0)
        """State 9: First encounter: Talk: Part 2: 3_SubState"""
        # talk:75200120:"Normally, people keep a safe distance\nwhen they see this mask. But you..."
        assert talk_m10_18_x1(text1=75200120, flag2=203601, z24=-1, z25=0)
        """State 3: First encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(flag3, 1)
        assert GetEventFlag(flag3) != 0
    else:
        """State 5: First encounter: Talk: Part 1_SubState"""
        # talk:75200000:"What is it?"
        assert talk_m10_18_x0(text17=75200000, z26=203600, z27=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_18_x23(flag4=102487, flag3=102482, flag5=102502):
    """Woman Knight: Second encounter: Conversation
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    flag5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter second time: Start"""
    if GetEventFlag(203614) != 0:
        """State 10: Encounter 2nd time: Speak: Part 5 (Single loop) _SubState"""
        # talk:75201000:"I'm sorry...to burden you with talk of my fate."
        assert talk_m10_18_x0(text17=75201000, z26=0, z27=0)
        """State 3: 2nd encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(flag3, 1)
        assert GetEventFlag(flag3) != 0
    elif GetEventFlag(203613) != 0:
        """State 9: Encounter second time: Talk: Part 5: 1_SubState"""
        # talk:75200900:"Have you heard of the Undead?\nThese poor souls affected by the curse."
        assert talk_m10_18_x0(text17=75200900, z26=0, z27=0)
        """State 13: Encounter second time: Talk: Part 5: 2_SubState"""
        # talk:75200910:"An Undead gradually loses his humanity,\nuntil his wits degrade completely."
        assert talk_m10_18_x1(text1=75200910, flag2=0, z24=-1, z25=0)
        """State 14: Encounter second time: Speak: Part 5: 3_SubState"""
        # talk:75200960:"I can only hope...that they are."
        assert talk_m10_18_x1(text1=75200960, flag2=203614, z24=-1, z25=0)
        """State 4: Second encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
        """State 2: Second encounter: Stop generation"""
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203612) != 0:
        """State 8: Encounter 2nd time: Talk: 4_SubState"""
        # talk:75200800:"I was raised to wield a sword from birth."
        assert talk_m10_18_x0(text17=75200800, z26=203613, z27=0)
        Goto('L0')
    elif GetEventFlag(203611) != 0:
        """State 7: Encounter second time: Talk: Part 3_SubState"""
        # talk:75200700:"Our land of Mirrah is surrounded by enemies,\nand constantly at war."
        assert talk_m10_18_x0(text17=75200700, z26=203612, z27=0)
        Goto('L0')
    elif GetEventFlag(203610) != 0:
        """State 6: Encounter second time: Speak: Part 2_SubState"""
        # lot:1752010:Human Effigy, talk:75200600:"Ah, yes, I have not thanked you\nfor humouring me the other day.", talk:75200620:"Of course, I've no idea what it is.\nHeh heh."
        assert (talk_m10_18_x18(lot2=1752010, flag7=102495, text5=75200600, text6=75200620, z4=203611,
                z1=0, z5=0, z6=0))
        Goto('L0')
    else:
        """State 5: Encounter second time: Speak: Part 1: 1_SubState"""
        # talk:75200500:"I thought that might be you.\nYou haven't changed a bit, have you? Heh heh."
        assert talk_m10_18_x0(text17=75200500, z26=0, z27=0)
        """State 11: Encounter second time: Talk: Part 1: 2_SubState"""
        # talk:75200520:"A wretched place, indeed, but not \nwithout traces of its former glory."
        assert talk_m10_18_x1(text1=75200520, flag2=0, z24=-1, z25=0)
        """State 12: Encounter second time: Talk: Part 1: 3_SubState"""
        # talk:75200530:"What could have caused such degradation?"
        assert talk_m10_18_x1(text1=75200530, flag2=203610, z24=-1, z25=0)
        Goto('L0')
    """State 15: End state"""
    return 0

def talk_m10_18_x24(flag4=102487, flag3=102482, flag5=102502):
    """Woman Knight: Encounter 3rd: Conversation
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    flag5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 3rd: Start"""
    if GetEventFlag(203622) != 0:
        """State 8: Encounter 3rd time: Talk: 4_SubState"""
        # talk:75201400:"If only someone would hear my tale..."
        assert talk_m10_18_x0(text17=75201400, z26=203623, z27=0)
        """State 4: 3rd encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
        """State 2: Encounter 3rd: Stop generation"""
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203621) != 0:
        """State 7: Encounter third time: Speak: Part 3: 1_SubState"""
        # talk:75201300:"I had an older brother. We learned to fence together."
        assert talk_m10_18_x0(text17=75201300, z26=0, z27=0)
        """State 11: Encounter third time: Speak: Part 3: 2_SubState"""
        # talk:75201340:"But then, one day...he was gone,\nlost without a trace."
        assert talk_m10_18_x1(text1=75201340, flag2=203622, z24=-1, z25=0)
        """State 3: 3rd encounter: Set flag during encounter"""
        Label('L0')
        SetEventFlag(flag3, 1)
        assert GetEventFlag(flag3) != 0
    elif GetEventFlag(203620) != 0:
        """State 6: Encounter 3rd time: Speak: Part 2: 1_SubState"""
        # talk:75201200:"I've found my thoughts growing hazy."
        assert talk_m10_18_x0(text17=75201200, z26=0, z27=0)
        """State 9: Encounter third time: Talk: Part 2: 2_SubState"""
        # talk:75201220:"The curse is doing its work upon me."
        assert talk_m10_18_x1(text1=75201220, flag2=0, z24=-1, z25=0)
        """State 10: Encounter third time: Speak: Part 2: 3_SubState"""
        # talk:75201230:"I am frightened... Terribly so..."
        assert talk_m10_18_x1(text1=75201230, flag2=203621, z24=-1, z25=0)
        Goto('L0')
    else:
        """State 5: Encounter 3rd time: Speak: Part 1_SubState"""
        # lot:1752020:Ring of Steel Protection+1, talk:75201100:"Still on the road, are you?"
        assert talk_m10_18_x19(lot1=1752020, flag6=102496, text4=75201100, z2=203620, z3=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_18_x25(flag4=102487, flag3=102482, flag5=102502):
    """Woman Knight: Encounter 4th: Conversation
    flag4: Generation stop: Global event flag
    flag3: Encounter: Global event flag
    flag5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 4th: Start"""
    if GetEventFlag(203632) != 0:
        """State 8: Encounter 4th: Speak: Part 4_SubState"""
        # talk:75201800:"Sometimes, I feel obsessed...\nwith this insignificant thing called "self"."
        assert talk_m10_18_x0(text17=75201800, z26=203633, z27=0)
        """State 4: 4th encounter: White phantom can appear: Set flag"""
        SetEventFlag(flag5, 1)
        assert GetEventFlag(flag5) != 0
        """State 2: Encounter 4th: Stop generation"""
        SetEventFlag(flag4, 1)
        assert GetEventFlag(flag4) != 0
    elif GetEventFlag(203631) != 0:
        """State 7: Encounter 4th: Speak: Part 3_SubState"""
        # talk:75201700:"Loss frightens me no end.\nLoss of memory, loss of self."
        assert talk_m10_18_x0(text17=75201700, z26=203632, z27=0)
        """State 3: 4th encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(flag3, 1)
        assert GetEventFlag(flag3) != 0
    elif GetEventFlag(203630) != 0:
        """State 6: Encounter 4th: Speak: Part 2: 1_SubState"""
        # talk:75201600:"What is this curse?"
        assert talk_m10_18_x0(text17=75201600, z26=0, z27=0)
        """State 9: Encounter 4th: Speak: Part 2: 2_SubState"""
        # talk:75201610:"The question rings in my mind,\nbut I haven't the focus to answer it."
        assert talk_m10_18_x1(text1=75201610, flag2=203631, z24=-1, z25=0)
        Goto('L0')
    else:
        """State 5: Encounter 4th: Speak: Part 1_SubState"""
        # talk:75201500:"Oh... You..."
        assert talk_m10_18_x0(text17=75201500, z26=203630, z27=0)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_18_x26(text11=76601400, text12=76601500, text13=76601600, flag9=102640, flag10=0):
    """[Lib] Menu Exit: Emigration Mes
    text11: Conversation ID (at the time of purchase)
    text12: Conversation ID (when not purchased)
    text13: Conversation ID (Migration decision)
    flag9: Emigration: Global event flag
    flag10: Emigration: Global conversation flag
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(flag9) != 0 and GetEventFlag(flag10) != 1:
        """State 4: Menu: Leaving: Relocation decision_SubState"""
        assert talk_m10_18_x1(text1=text13, flag2=flag10, z24=-1, z25=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Menu: Leave: At purchase_SubState"""
        assert talk_m10_18_x1(text1=text11, flag2=0, z24=-1, z25=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Menu: Leave: Non-Purchase_SubState"""
        assert talk_m10_18_x1(text1=text12, flag2=0, z24=-1, z25=0)
    """State 5: End state"""
    return 0

def talk_m10_18_x27(flag8=118020144, z7=102340, z8=0):
    """[Lib] Dwarf: Conversation
    flag8: Contact: Area and other flags
    z7: Emigration permission: Global event flag
    z8: Shop list: Global event flag
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    SetEventFlag(z8, 1)
    if GetEventFlag(202900) != 0:
        """State 4: Dwarf: Greetings_SubState"""
        assert talk_m10_18_x29(flag8=flag8, z7=z7)
    else:
        """State 3: Dwarf: First conversation_SubState"""
        assert talk_m10_18_x28(flag8=flag8, z7=z7)
    """State 5: Dwarf: NPC menu_SubState"""
    assert talk_m10_18_x30()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_18_x28(flag8=118020144, z7=102340):
    """Dwarf: First conversation
    flag8: Contact: Area and other flags
    z7: Emigration permission: Global event flag
    """
    """State 0,1,3: Speak: Part 1: 1_SubState"""
    # talk:72600000:"Who you?"
    assert talk_m10_18_x0(text17=72600000, z26=202900, z27=0)
    """State 4: Talk: Part 1: 2_SubState"""
    # talk:72600060:"With Gavlan, you wheel?\nYou deal! Gah hah!"
    assert talk_m10_18_x1(text1=72600060, flag2=202900, z24=-1, z25=0)
    """State 2: First conversation: Set contact flag"""
    SetEventFlag(z7, 1)
    SetEventFlag(flag8, 1)
    assert GetEventFlag(flag8) != 0
    """State 5: End state"""
    return 0

def talk_m10_18_x29(flag8=118020144, z7=102340):
    """Dwarf: Greeting
    flag8: Contact: Area and other flags
    z7: Emigration permission: Global event flag
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(flag8) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 7: Talk to _continuous 1_SubState"""
            # talk:72600100:"What? You want?"
            assert talk_m10_18_x0(text17=72600100, z26=0, z27=0)
        else:
            """State 8: Talk to _continuous 2_SubState"""
            # talk:72600200:"Umm...You want? Want what?"
            assert talk_m10_18_x0(text17=72600200, z26=0, z27=0)
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
            assert talk_m10_18_x0(text17=72600300, z26=202901, z27=0)
        elif GetEventFlag(202903) != 0:
            """State 12: Talk to _After a long time 4_SubState"""
            # talk:72600600:"You, again.\nGavlan, meet you again."
            assert talk_m10_18_x0(text17=72600600, z26=202904, z27=0)
        elif GetEventFlag(202902) != 0:
            """State 11: Talk to _After a long time 3_SubState"""
            # talk:72600500:"Oh Gavlan, know you.\nWhat you want?"
            assert talk_m10_18_x0(text17=72600500, z26=202903, z27=0)
        elif GetEventFlag(202901) != 0:
            """State 10: Talk to _After a long time 2_SubState"""
            # talk:72600400:"Make deal with Gavlan?"
            assert talk_m10_18_x0(text17=72600400, z26=202902, z27=0)
        else:
            Goto('L0')
        """State 6: Greeting: Contact flag setting"""
        SetEventFlag(z7, 1)
        SetEventFlag(flag8, 1)
        assert GetEventFlag(flag8) != 0
    """State 13: End state"""
    return 0

def talk_m10_18_x30():
    """Dwarf: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    while True:
        """State 6: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_18_x12(z15=0, z16=220, z17=72600000, z18=0)
        if call.Get() == 2:
            """State 5: Dwarf: Menu conversation_SubState"""
            call = talk_m10_18_x31()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3: [Lib] Exit menu: General purpose_SubState"""
            # talk:72600700:"Many deal...many thanks! Gah hah!", talk:72600800:"You? Go home?"
            assert talk_m10_18_x13(text15=72600700, text16=72600800)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuResults()
        """State 7: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:72600900:"Umm..."
    assert talk_m10_18_x14(text14=72600900)
    Goto('L0')

def talk_m10_18_x31():
    """Dwarf: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102355) != 1 and (GetGlobalVariable(200) > NpcInfoValue(7260, 0)) != 0 and GetEventFlag(104130)
        != 1):
        """State 3: Equipment transfer (Condition: Total purchase amount is above a certain level) _SubState"""
        # lot:1726000:Gyrm Greataxe, talk:72606000:"Wheel...deal..."
        assert talk_m10_18_x17(lot3=1726000, z9=102355, text7=72606000)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:72605000:"Umm...You strong."
        assert talk_m10_18_x1(text1=72605000, flag2=0, z24=-1, z25=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_18_x32(text10=_, z12=0, z13=20, z14=80):
    """[Lib] Conversation: Hostile display only
    text10: Conversation ID
    z12: Conversation flag
    z13: Display distance
    z14: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text10, GetCommonEventParamDecimal(7), z13)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z12, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_18_x33(z11=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z11: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_18_x34():
    """Magician: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Magician: First conversation_SubState"""
    call = talk_m10_18_x35()
    if call.Get() == 1:
        """State 4: Magician: NPC Menu_SubState"""
        assert talk_m10_18_x36()
    elif call.Get() == 0:
        pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_18_x35():
    """Magician: First conversation"""
    """State 0: Start state"""
    while True:
        """State 1: First conversation: start"""
        if GetEventFlag(204800) != 0:
            """State 5: [Lib] Conversation: Greeting: General purpose_SubState"""
            # talk:76601000:"Do you seek my teachings?\nVery well, very well.", talk:76601100:"Back already?\nYour diligence is commendable.", talk:76601200:"Your visit is welcome.\nI trust you've kept up your studies.", talk:76601300:"Oh, there you are. Do you seek my teachings?"
            assert (talk_m10_18_x11(flag11=118020124, text17=76601000, text18=76601100, text19=76601200,
                    text20=76601300))
        elif (GetPlayerStat(5, 1) > NpcInfoValue(7660, 0)) != 0:
            break
        else:
            """State 4: Speak: Reason less than 10: 1_SubState"""
            # talk:76600100:"Hmm..."
            call = talk_m10_18_x0(text17=76600100, z26=0, z27=0)
            if call.Done():
                """State 6: Talk to: Reason less than 10: 2_SubState"""
                # talk:76600120:"I am Carhillion, and I've no\ninterest in the magic-impaired."
                assert talk_m10_18_x1(text1=76600120, flag2=0, z24=-1, z25=0)
                """State 7: Normal: End state"""
                return 0
            elif (GetPlayerStat(5, 1) > NpcInfoValue(7660, 0)) != 0:
                continue
        """State 8: Menu: Exit state"""
        Label('L0')
        return 1
    """State 3: Talk: Power is over 10_SubState"""
    # talk:76600000:"Hmm...I sense power..."
    assert talk_m10_18_x0(text17=76600000, z26=204800, z27=0)
    """State 2: First conversation: Set contact flag"""
    SetEventFlag(118020124, 1)
    Goto('L0')

def talk_m10_18_x36():
    """Magician: NPC Menu"""
    """State 0,1: Menu: Start"""
    while True:
        """State 3: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_18_x12(z15=0, z16=220, z17=76600000, z18=0)
        if call.Get() == 2:
            """State 6: Magician: Menu conversation_SubState"""
            call = talk_m10_18_x37()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 7: Menu exit: Emigration Mes_SubState"""
            # talk:76601400:"Young pupil, do not take my teachings lightly.", talk:76601500:"One day, my teachings will save you.", talk:76601600:"Young pupil, may we meet again, in Majula."
            assert talk_m10_18_x38(text1=76601400, text2=76601500, text3=76601600, flag1=100961, flag2=204800)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuSelection()
        """State 8: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76601700:"The path is yet long, young pupil."
    assert talk_m10_18_x14(text14=76601700)
    Goto('L0')
    """Unused"""
    """State 4: [Lib] Menu exit: Emigration Mes_SubState"""
    # talk:76601400:"Young pupil, do not take my teachings lightly.", talk:76601500:"One day, my teachings will save you.", talk:76601600:"Young pupil, may we meet again, in Majula."
    assert talk_m10_18_x26(text11=76601400, text12=76601500, text13=76601600, flag9=102640, flag10=0)
    Goto('L0')

def talk_m10_18_x37():
    """Magician: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102720) != 1 and (GetPlayerStat(5, 1) > NpcInfoValue(7660, 2)) != 0 and GetEventFlag(104300)
        != 1):
        """State 6: Equipment transfer (Conditions: Reason is above a certain level) _SubState"""
        # lot:1766000:Northern Ritual Band+1, talk:76606000:"Do not neglect your studies, dear pupil."
        assert talk_m10_18_x15(lot4=1766000, z10=102720, text8=76606000, text9=76606010)
    elif GetEventFlag(204811) != 0:
        """State 3: Menu conversation: Flag initialization"""
        SetEventFlag(204810, 0)
        SetEventFlag(204811, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76602000:"The forces of magic, and souls, \nlie dormant in this land."
        assert talk_m10_18_x1(text1=76602000, flag2=204810, z24=-1, z25=0)
    elif GetEventFlag(204810) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:76602100:"Use scrolls to unleash\nthe power of sorceries."
        assert talk_m10_18_x1(text1=76602100, flag2=204811, z24=-1, z25=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 7: End state"""
    return 0

def talk_m10_18_x38(text1=76601400, text2=76601500, text3=76601600, flag1=100961, flag2=204800):
    """Menu Exit: Emigration Mes
    text1: Conversation ID (at the time of purchase)
    text2: Conversation ID (when not purchased)
    text3: Conversation ID (Migration decision)
    flag1: Emigration: Global event flag
    flag2: Emigration: Global conversation flag
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(flag1) != 0 and GetEventFlag(flag2) != 0:
        """State 4: Menu: Leaving: Relocation decision_SubState"""
        assert talk_m10_18_x1(text1=text3, flag2=flag2, z24=-1, z25=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Menu: Leave: At purchase_SubState"""
        assert talk_m10_18_x1(text1=text1, flag2=0, z24=-1, z25=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Menu: Leave: Non-Purchase_SubState"""
        assert talk_m10_18_x1(text1=text2, flag2=0, z24=-1, z25=0)
    """State 5: End state"""
    return 0

