# -*- coding: utf-8 -*-
def talk_m10_18_7260():
    """Dwarf (Hidden Port)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_18_x9(z32=103631, z33=104131, z34=118020141)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_18_x3(text10=72609200, z20=0, z21=20, z22=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_18_x6(z30=118020142, text21=72609500, text22=72609500, z31=72609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_18_x7(text24=72609600, z36=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: [Lib] Dwarf: Conversation_SubState"""
            while True:
                call = talk_m10_18_x27(z14=118020144, z15=102340, z16=0)
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
                                          z37=118020145, z38=118020146)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_18_x4(z39=103630, text29=72609100, z40=0, z41=103631)
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
        talk_m10_18_x8(text23=72609300, z35=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_18_7520():
    """Woman Knight (Hidden Port)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_18_x9(z32=103691, z33=104191, z34=118020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_18_x3(text10=75209200, z20=0, z21=20, z22=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_18_x6(z30=118020102, text21=75209500, text22=75209500, z31=75209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_18_x7(text24=75209600, z36=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 9: [Lib] Female knight: Before last: Conversation_SubState"""
            while True:
                call = talk_m10_18_x21(z3=102482, z4=102487, z5=102502, z6=118020109)
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
                                          z37=118020105, z38=118020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_18_x4(z39=103690, text29=75209100, z40=0, z41=103691)
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
        talk_m10_18_x8(text23=75209300, z35=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_18_7660():
    """Magician (Hidden Port)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_18_x9(z32=103801, z33=104301, z34=118020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_18_x3(text10=76609200, z20=0, z21=20, z22=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_18_x6(z30=118020122, text21=76609500, text22=76609500, z31=76609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_18_x7(text24=76609600, z36=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Magician: Conversation_SubState"""
            while True:
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
                                          z37=118020125, z38=118020126)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_18_x4(z39=103800, text29=76609100, z40=0, z41=103801)
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
        talk_m10_18_x8(text23=76609300, z35=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_18_x0(text17=_, z44=_, z45=0):
    """[Lib] Conversation: General purpose
    text17: Conversation ID
    z44: Conversation flag
    z45: Global event flag
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
    SetEventFlag(z44, 1)
    SetEventFlag(z45, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_18_x1(text1=_, z2=_, z42=-1, z43=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z2: Conversation flag
    z42: Display distance
    z43: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z42)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z2, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_18_x2(text23=_, z35=0):
    """[Lib] Conversation: Event end
    text23: Conversation ID
    z35: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text23, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z35, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_18_x3(text10=_, z20=0, z21=20, z22=80):
    """[Lib] Reunion hostility
    text10: Conversation message ID
    z20: Conversation flag ID
    z21: Display distance
    z22: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_18_x32(text10=text10, z20=z20, z21=z21, z22=z22)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_18_x4(z39=_, text29=_, z40=0, z41=_):
    """[Lib] First hostility
    z39: Hostile: Global event flag
    text29: Conversation ID
    z40: Conversation flag
    z41: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z39, 1)
    SetEventFlag(z41, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z39) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_18_x1(text1=text29, z2=z40, z42=-1, z43=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_18_x5(text25=_, text26=_, text27=_, text28=_, z37=_, z38=_):
    """[Lib] Hostile waiting
    text25: Conversation ID: 1 attacked
    text26: Conversation ID: Attacked 2
    text27: Conversation ID: 3 attacked
    text28: Conversation ID: 4 attacked
    z37: No use: Area and other flags
    z38: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z38) != 1, z38, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z37) != 1, z37, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_18_x1(text1=text28, z2=0, z42=-1, z43=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_18_x1(text1=text27, z2=0, z42=-1, z43=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_18_x1(text1=text26, z2=0, z42=-1, z43=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_18_x1(text1=text25, z2=0, z42=-1, z43=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_18_x6(z30=_, text21=_, text22=_, z31=_):
    """[Lib] Hostile state
    z30: Area and other flags: HP decreased
    text21: Conversation ID: HP drop 1
    text22: Conversation ID: HP drop 2
    z31: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    """State 2: Hostile state: standby"""
    while True:
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z30) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_18_x10(text21=text21, z30=z30)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_18_x10(text21=text22, z30=z30)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_18_x10(text21=text22, z30=z30)

def talk_m10_18_x7(text24=_, z36=0):
    """[Lib] Death status
    text24: Conversation ID
    z36: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_18_x2(text23=text24, z35=z36)

def talk_m10_18_x8(text23=_, z35=0):
    """[Lib] Murder status
    text23: Conversation ID
    z35: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_18_x2(text23=text23, z35=z35)

def talk_m10_18_x9(z32=_, z33=_, z34=_):
    """[Lib] Event: Branch
    z32: Hostile flag
    z33: death flag
    z34: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z33) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z34) != 0
    elif GetEventFlag(z32) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_18_x10(text21=_, z30=_):
    """[Lib] Conversation: HP drop
    text21: Conversation ID
    z30: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text21, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z30, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_18_x11(z29=118020124, text17=76601000, text18=76601100, text19=76601200, text20=76601300):
    """[Lib] Conversation: Greeting: General
    z29: Area other flag: Contact flag
    text17: Text ID: Talk to_continuous 1
    text18: Text ID: Talk to_continuous 2
    text19: Text ID: Talk to _After a long time 1
    text20: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z29) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_18_x0(text17=text17, z44=0, z45=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_18_x0(text17=text18, z44=0, z45=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_18_x0(text17=text19, z44=0, z45=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_18_x0(text17=text20, z44=0, z45=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(z29, 1)
    """State 10: End state"""
    return 0

def talk_m10_18_x12(z25=0, z26=220, z27=_, z28=0):
    """[Lib] Menu start: General purpose
    z25: Camera parameter ID
    z26: Target Damipoly ID
    z27: NPC event parameter ID
    z28: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z28, z25, z26, z27)
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

def talk_m10_18_x13(text15=72600700, text16=72600800):
    """[Lib] Menu exit: General purpose
    text15: Conversation ID (at the time of purchase)
    text16: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_18_x1(text1=text15, z2=0, z42=-1, z43=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_18_x1(text1=text16, z2=0, z42=-1, z43=0)
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
    assert talk_m10_18_x1(text1=text14, z2=0, z42=-1, z43=0)
    """State 4: End state"""
    return 0

def talk_m10_18_x15(lot4=1766000, z18=102720, text8=76606000, text9=76606010):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z18: Global event flag
    text8: First half: Conversation ID
    text9: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_18_x1(text1=text8, z2=0, z42=-1, z43=0)
    # lot:1766000:Northern Ritual Band+1
    if call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z19=1011, lot1=lot4)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_18_x16(lot3=lot4, z17=z18)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_18_x1(text1=text9, z2=0, z42=-1, z43=0)
    """State 6: End state"""
    return 0

def talk_m10_18_x16(lot3=_, z17=_):
    """[Lib] Item acquisition dialog
    lot3: Item lottery ID
    z17: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z17, 1)
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_18_x17(lot3=1726000, z17=102355, text7=72606000):
    """[Lib] Equipment transfer: Mes⇒Item
    lot3: Item lottery ID
    z17: Global event flag
    text7: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_18_x1(text1=text7, z2=0, z42=-1, z43=0)
    # lot:1726000:Gyrm Greataxe
    if call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z19=1011, lot1=lot3)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_18_x16(lot3=lot3, z17=z17)
    """State 5: End state"""
    return 0

def talk_m10_18_x18(lot2=_, z10=_, text5=_, text6=_, z11=_, z6=_, z12=0, z13=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot2: Item lottery ID
    z10: Item transfer: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    z11: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
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
    call = talk_m10_18_x1(text1=text5, z2=0, z42=-1, z43=0)
    if call.Done() and GetEventFlag(z10) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z11, 1)
        SetEventFlag(z12, 1)
        SetEventFlag(z13, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_18_x1(text1=text6, z2=0, z42=-1, z43=0)
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z19=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_18_x20(lot1=lot2, z7=z10, z8=z11, z9=z6, z12=z12, z13=z13)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_18_x19(lot1=1752020, z7=102496, text4=75201100, z8=203620, z9=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot1: Item lottery ID
    z7: Item transfer: Global event flag
    text4: Conversation ID
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
    call = talk_m10_18_x1(text1=text4, z2=0, z42=-1, z43=0)
    if call.Done() and GetEventFlag(z7) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z8, 1)
    # lot:1752020:Ring of Steel Protection+1
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_18_x33(z19=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_18_x20(lot1=lot1, z7=z7, z8=z8, z9=z9, z12=0, z13=0)
    """State 9: End state"""
    return 0

def talk_m10_18_x20(lot1=_, z7=_, z8=_, z9=_, z12=0, z13=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Item lottery ID
    z7: Item transfer: Global event flag
    z8: Conversation: Global conversation flag
    z9: Trophy acquisition: Area and other flags
    z12: Emigration permission: Global event flag
    z13: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z13, 1)
    SetEventFlag(z12, 1)
    SetEventFlag(z9, 1)
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_18_x21(z3=102482, z4=102487, z5=102502, z6=118020109):
    """[Lib] Woman Knight: Before Last: Conversation
    z3: Encounter: Global event flag
    z4: Generation establishment: Global event flag
    z5: White Phantom Appearance: Global Event Flag
    z6: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203630) != 0 and GetEventFlag(z3) != 0:
        """State 5: Woman Knight: Encounter 4th: Conversation_SubState"""
        Label('L0')
        assert talk_m10_18_x25(z4=z4, z3=z3, z5=z5)
    elif GetEventFlag(203623) != 0 and GetEventFlag(z3) != 1:
        Goto('L0')
    elif GetEventFlag(203620) != 0 and GetEventFlag(z3) != 0:
        """State 4: Woman Knight: Encounter 3rd: Conversation_SubState"""
        Label('L1')
        assert talk_m10_18_x24(z4=z4, z3=z3, z5=z5)
    elif GetEventFlag(203614) != 0 and GetEventFlag(z3) != 1:
        Goto('L1')
    elif GetEventFlag(203610) != 0 and GetEventFlag(z3) != 0:
        """State 3: Woman Knight: Encounter 2nd: Conversation_SubState"""
        Label('L2')
        assert talk_m10_18_x23(z4=z4, z3=z3, z5=z5)
    elif GetEventFlag(203602) != 0 and GetEventFlag(z3) != 1:
        Goto('L2')
    elif GetEventFlag(203600) != 0 and GetEventFlag(z3) != 0:
        """State 2: Woman Knight: First encounter: Conversation_SubState"""
        Label('L3')
        assert talk_m10_18_x22(z4=z4, z3=z3, z5=z5)
    else:
        Goto('L3')
    """State 7: End state"""
    return 0

def talk_m10_18_x22(z4=102487, z3=102482, z5=102502):
    """Woman Knight: First encounter: Conversation
    z4: Generation stop: Global event flag
    z3: Encounter: Global event flag
    z5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: First encounter: Start"""
    if GetEventFlag(203601) != 0:
        """State 7: First encounter: Talk: Part 3: 1_SubState"""
        # talk:75200300:"You are an odd one, indeed.\nI've always made a point of avoiding people."
        assert talk_m10_18_x0(text17=75200300, z44=0, z45=0)
        """State 10: First encounter: Talk: Part 3: 2_SubState"""
        # talk:75200310:"While you've made a point of engaging me."
        assert talk_m10_18_x1(text1=75200310, z2=0, z42=-1, z43=0)
        """State 11: First encounter: Talk: Part 3: 3_SubState"""
        # talk:75200320:"I can see that you are mid-journey.\nIf you require assistance, I will help you."
        assert talk_m10_18_x1(text1=75200320, z2=203602, z42=-1, z43=0)
        """State 4: First encounter: White phantom can appear: Set flag"""
        SetEventFlag(z5, 1)
        assert GetEventFlag(z5) != 0
        """State 2: First encounter: stop generation"""
        SetEventFlag(z4, 1)
        assert GetEventFlag(z4) != 0
    elif GetEventFlag(203600) != 0:
        """State 6: First encounter: Talk: Part 2: 1_SubState"""
        # talk:75200100:"Phew..."
        assert talk_m10_18_x0(text17=75200100, z44=0, z45=0)
        """State 8: First encounter: Talk: Part 2: 2_SubState"""
        # talk:75200110:"Heh heh. You are an odd one."
        assert talk_m10_18_x1(text1=75200110, z2=0, z42=-1, z43=0)
        """State 9: First encounter: Talk: Part 2: 3_SubState"""
        # talk:75200120:"Normally, people keep a safe distance\nwhen they see this mask. But you..."
        assert talk_m10_18_x1(text1=75200120, z2=203601, z42=-1, z43=0)
        """State 3: First encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z3, 1)
        assert GetEventFlag(z3) != 0
    else:
        """State 5: First encounter: Talk: Part 1_SubState"""
        # talk:75200000:"What is it?"
        assert talk_m10_18_x0(text17=75200000, z44=203600, z45=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_18_x23(z4=102487, z3=102482, z5=102502):
    """Woman Knight: Second encounter: Conversation
    z4: Generation stop: Global event flag
    z3: Encounter: Global event flag
    z5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter second time: Start"""
    if GetEventFlag(203614) != 0:
        """State 10: Encounter 2nd time: Speak: Part 5 (Single loop) _SubState"""
        # talk:75201000:"I'm sorry...to burden you with talk of my fate."
        assert talk_m10_18_x0(text17=75201000, z44=0, z45=0)
        """State 3: 2nd encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z3, 1)
        assert GetEventFlag(z3) != 0
    elif GetEventFlag(203613) != 0:
        """State 9: Encounter second time: Talk: Part 5: 1_SubState"""
        # talk:75200900:"Have you heard of the Undead?\nThese poor souls affected by the curse."
        assert talk_m10_18_x0(text17=75200900, z44=0, z45=0)
        """State 13: Encounter second time: Talk: Part 5: 2_SubState"""
        # talk:75200910:"An Undead gradually loses his humanity,\nuntil his wits degrade completely."
        assert talk_m10_18_x1(text1=75200910, z2=0, z42=-1, z43=0)
        """State 14: Encounter second time: Speak: Part 5: 3_SubState"""
        # talk:75200960:"I can only hope...that they are."
        assert talk_m10_18_x1(text1=75200960, z2=203614, z42=-1, z43=0)
        """State 4: Second encounter: White phantom can appear: Set flag"""
        SetEventFlag(z5, 1)
        assert GetEventFlag(z5) != 0
        """State 2: Second encounter: Stop generation"""
        SetEventFlag(z4, 1)
        assert GetEventFlag(z4) != 0
    elif GetEventFlag(203612) != 0:
        """State 8: Encounter 2nd time: Talk: 4_SubState"""
        # talk:75200800:"I was raised to wield a sword from birth."
        assert talk_m10_18_x0(text17=75200800, z44=203613, z45=0)
        Goto('L0')
    elif GetEventFlag(203611) != 0:
        """State 7: Encounter second time: Talk: Part 3_SubState"""
        # talk:75200700:"Our land of Mirrah is surrounded by enemies,\nand constantly at war."
        assert talk_m10_18_x0(text17=75200700, z44=203612, z45=0)
        Goto('L0')
    elif GetEventFlag(203610) != 0:
        """State 6: Encounter second time: Speak: Part 2_SubState"""
        # lot:1752010:Human Effigy, talk:75200600:"Ah, yes, I have not thanked you\nfor humouring me the other day.", talk:75200620:"Of course, I've no idea what it is.\nHeh heh."
        assert (talk_m10_18_x18(lot2=1752010, z10=102495, text5=75200600, text6=75200620, z11=203611,
                z6=0, z12=0, z13=0))
        Goto('L0')
    else:
        """State 5: Encounter second time: Speak: Part 1: 1_SubState"""
        # talk:75200500:"I thought that might be you.\nYou haven't changed a bit, have you? Heh heh."
        assert talk_m10_18_x0(text17=75200500, z44=0, z45=0)
        """State 11: Encounter second time: Talk: Part 1: 2_SubState"""
        # talk:75200520:"A wretched place, indeed, but not \nwithout traces of its former glory."
        assert talk_m10_18_x1(text1=75200520, z2=0, z42=-1, z43=0)
        """State 12: Encounter second time: Talk: Part 1: 3_SubState"""
        # talk:75200530:"What could have caused such degradation?"
        assert talk_m10_18_x1(text1=75200530, z2=203610, z42=-1, z43=0)
        Goto('L0')
    """State 15: End state"""
    return 0

def talk_m10_18_x24(z4=102487, z3=102482, z5=102502):
    """Woman Knight: Encounter 3rd: Conversation
    z4: Generation stop: Global event flag
    z3: Encounter: Global event flag
    z5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 3rd: Start"""
    if GetEventFlag(203622) != 0:
        """State 8: Encounter 3rd time: Talk: 4_SubState"""
        # talk:75201400:"If only someone would hear my tale..."
        assert talk_m10_18_x0(text17=75201400, z44=203623, z45=0)
        """State 4: 3rd encounter: White phantom can appear: Set flag"""
        SetEventFlag(z5, 1)
        assert GetEventFlag(z5) != 0
        """State 2: Encounter 3rd: Stop generation"""
        SetEventFlag(z4, 1)
        assert GetEventFlag(z4) != 0
    elif GetEventFlag(203621) != 0:
        """State 7: Encounter third time: Speak: Part 3: 1_SubState"""
        # talk:75201300:"I had an older brother. We learned to fence together."
        assert talk_m10_18_x0(text17=75201300, z44=0, z45=0)
        """State 11: Encounter third time: Speak: Part 3: 2_SubState"""
        # talk:75201340:"But then, one day...he was gone,\nlost without a trace."
        assert talk_m10_18_x1(text1=75201340, z2=203622, z42=-1, z43=0)
        """State 3: 3rd encounter: Set flag during encounter"""
        Label('L0')
        SetEventFlag(z3, 1)
        assert GetEventFlag(z3) != 0
    elif GetEventFlag(203620) != 0:
        """State 6: Encounter 3rd time: Speak: Part 2: 1_SubState"""
        # talk:75201200:"I've found my thoughts growing hazy."
        assert talk_m10_18_x0(text17=75201200, z44=0, z45=0)
        """State 9: Encounter third time: Talk: Part 2: 2_SubState"""
        # talk:75201220:"The curse is doing its work upon me."
        assert talk_m10_18_x1(text1=75201220, z2=0, z42=-1, z43=0)
        """State 10: Encounter third time: Speak: Part 2: 3_SubState"""
        # talk:75201230:"I am frightened... Terribly so..."
        assert talk_m10_18_x1(text1=75201230, z2=203621, z42=-1, z43=0)
        Goto('L0')
    else:
        """State 5: Encounter 3rd time: Speak: Part 1_SubState"""
        # lot:1752020:Ring of Steel Protection+1, talk:75201100:"Still on the road, are you?"
        assert talk_m10_18_x19(lot1=1752020, z7=102496, text4=75201100, z8=203620, z9=0)
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_18_x25(z4=102487, z3=102482, z5=102502):
    """Woman Knight: Encounter 4th: Conversation
    z4: Generation stop: Global event flag
    z3: Encounter: Global event flag
    z5: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Encounter 4th: Start"""
    if GetEventFlag(203632) != 0:
        """State 8: Encounter 4th: Speak: Part 4_SubState"""
        # talk:75201800:"Sometimes, I feel obsessed...\nwith this insignificant thing called "self"."
        assert talk_m10_18_x0(text17=75201800, z44=203633, z45=0)
        """State 4: 4th encounter: White phantom can appear: Set flag"""
        SetEventFlag(z5, 1)
        assert GetEventFlag(z5) != 0
        """State 2: Encounter 4th: Stop generation"""
        SetEventFlag(z4, 1)
        assert GetEventFlag(z4) != 0
    elif GetEventFlag(203631) != 0:
        """State 7: Encounter 4th: Speak: Part 3_SubState"""
        # talk:75201700:"Loss frightens me no end.\nLoss of memory, loss of self."
        assert talk_m10_18_x0(text17=75201700, z44=203632, z45=0)
        """State 3: 4th encounter: Set encounter flag"""
        Label('L0')
        SetEventFlag(z3, 1)
        assert GetEventFlag(z3) != 0
    elif GetEventFlag(203630) != 0:
        """State 6: Encounter 4th: Speak: Part 2: 1_SubState"""
        # talk:75201600:"What is this curse?"
        assert talk_m10_18_x0(text17=75201600, z44=0, z45=0)
        """State 9: Encounter 4th: Speak: Part 2: 2_SubState"""
        # talk:75201610:"The question rings in my mind,\nbut I haven't the focus to answer it."
        assert talk_m10_18_x1(text1=75201610, z2=203631, z42=-1, z43=0)
        Goto('L0')
    else:
        """State 5: Encounter 4th: Speak: Part 1_SubState"""
        # talk:75201500:"Oh... You..."
        assert talk_m10_18_x0(text17=75201500, z44=203630, z45=0)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_18_x26(text11=76601400, text12=76601500, text13=76601600, z23=102640, z24=0):
    """[Lib] Menu Exit: Emigration Mes
    text11: Conversation ID (at the time of purchase)
    text12: Conversation ID (when not purchased)
    text13: Conversation ID (Migration decision)
    z23: Emigration: Global event flag
    z24: Emigration: Global conversation flag
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(z23) != 0 and GetEventFlag(z24) != 1:
        """State 4: Menu: Leaving: Relocation decision_SubState"""
        assert talk_m10_18_x1(text1=text13, z2=z24, z42=-1, z43=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Menu: Leave: At purchase_SubState"""
        assert talk_m10_18_x1(text1=text11, z2=0, z42=-1, z43=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Menu: Leave: Non-Purchase_SubState"""
        assert talk_m10_18_x1(text1=text12, z2=0, z42=-1, z43=0)
    """State 5: End state"""
    return 0

def talk_m10_18_x27(z14=118020144, z15=102340, z16=0):
    """[Lib] Dwarf: Conversation
    z14: Contact: Area and other flags
    z15: Emigration permission: Global event flag
    z16: Shop list: Global event flag
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    SetEventFlag(z16, 1)
    if GetEventFlag(202900) != 0:
        """State 4: Dwarf: Greetings_SubState"""
        assert talk_m10_18_x29(z14=z14, z15=z15)
    else:
        """State 3: Dwarf: First conversation_SubState"""
        assert talk_m10_18_x28(z14=z14, z15=z15)
    """State 5: Dwarf: NPC menu_SubState"""
    assert talk_m10_18_x30()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_18_x28(z14=118020144, z15=102340):
    """Dwarf: First conversation
    z14: Contact: Area and other flags
    z15: Emigration permission: Global event flag
    """
    """State 0,1,3: Speak: Part 1: 1_SubState"""
    # talk:72600000:"Who you?"
    assert talk_m10_18_x0(text17=72600000, z44=202900, z45=0)
    """State 4: Talk: Part 1: 2_SubState"""
    # talk:72600060:"With Gavlan, you wheel?\nYou deal! Gah hah!"
    assert talk_m10_18_x1(text1=72600060, z2=202900, z42=-1, z43=0)
    """State 2: First conversation: Set contact flag"""
    SetEventFlag(z15, 1)
    SetEventFlag(z14, 1)
    assert GetEventFlag(z14) != 0
    """State 5: End state"""
    return 0

def talk_m10_18_x29(z14=118020144, z15=102340):
    """Dwarf: Greeting
    z14: Contact: Area and other flags
    z15: Emigration permission: Global event flag
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z14) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 7: Talk to _continuous 1_SubState"""
            # talk:72600100:"What? You want?"
            assert talk_m10_18_x0(text17=72600100, z44=0, z45=0)
        else:
            """State 8: Talk to _continuous 2_SubState"""
            # talk:72600200:"Umm...You want? Want what?"
            assert talk_m10_18_x0(text17=72600200, z44=0, z45=0)
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
            assert talk_m10_18_x0(text17=72600300, z44=202901, z45=0)
        elif GetEventFlag(202903) != 0:
            """State 12: Talk to _After a long time 4_SubState"""
            # talk:72600600:"You, again.\nGavlan, meet you again."
            assert talk_m10_18_x0(text17=72600600, z44=202904, z45=0)
        elif GetEventFlag(202902) != 0:
            """State 11: Talk to _After a long time 3_SubState"""
            # talk:72600500:"Oh Gavlan, know you.\nWhat you want?"
            assert talk_m10_18_x0(text17=72600500, z44=202903, z45=0)
        elif GetEventFlag(202901) != 0:
            """State 10: Talk to _After a long time 2_SubState"""
            # talk:72600400:"Make deal with Gavlan?"
            assert talk_m10_18_x0(text17=72600400, z44=202902, z45=0)
        else:
            Goto('L0')
        """State 6: Greeting: Contact flag setting"""
        SetEventFlag(z15, 1)
        SetEventFlag(z14, 1)
        assert GetEventFlag(z14) != 0
    """State 13: End state"""
    return 0

def talk_m10_18_x30():
    """Dwarf: NPC menu"""
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    """State 6: [Lib] Menu start: General purpose_SubState"""
    while True:
        call = talk_m10_18_x12(z25=0, z26=220, z27=72600000, z28=0)
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
        assert talk_m10_18_x17(lot3=1726000, z17=102355, text7=72606000)
    else:
        """State 4: Menu conversation: Part 1_SubState"""
        # talk:72605000:"Umm...You strong."
        assert talk_m10_18_x1(text1=72605000, z2=0, z42=-1, z43=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_18_x32(text10=_, z20=0, z21=20, z22=80):
    """[Lib] Conversation: Hostile display only
    text10: Conversation ID
    z20: Conversation flag
    z21: Display distance
    z22: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text10, GetCommonEventParamDecimal(7), z21)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z20, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_18_x33(z19=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z19: Text ID
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
    """State 0,1: First conversation: start"""
    while True:
        if GetEventFlag(204800) != 0:
            """State 5: [Lib] Conversation: Greeting: General purpose_SubState"""
            # talk:76601000:"Do you seek my teachings?\nVery well, very well.", talk:76601100:"Back already?\nYour diligence is commendable.", talk:76601200:"Your visit is welcome.\nI trust you've kept up your studies.", talk:76601300:"Oh, there you are. Do you seek my teachings?"
            assert (talk_m10_18_x11(z29=118020124, text17=76601000, text18=76601100, text19=76601200,
                    text20=76601300))
        elif (GetPlayerStat(5, 1) > NpcInfoValue(7660, 0)) != 0:
            break
        else:
            """State 4: Speak: Reason less than 10: 1_SubState"""
            # talk:76600100:"Hmm..."
            call = talk_m10_18_x0(text17=76600100, z44=0, z45=0)
            if call.Done():
                """State 6: Talk to: Reason less than 10: 2_SubState"""
                # talk:76600120:"I am Carhillion, and I've no\ninterest in the magic-impaired."
                assert talk_m10_18_x1(text1=76600120, z2=0, z42=-1, z43=0)
                """State 7: Normal: End state"""
                return 0
            elif (GetPlayerStat(5, 1) > NpcInfoValue(7660, 0)) != 0:
                continue
        """State 8: Menu: Exit state"""
        Label('L0')
        return 1
    """State 3: Talk: Power is over 10_SubState"""
    # talk:76600000:"Hmm...I sense power..."
    assert talk_m10_18_x0(text17=76600000, z44=204800, z45=0)
    """State 2: First conversation: Set contact flag"""
    SetEventFlag(118020124, 1)
    Goto('L0')

def talk_m10_18_x36():
    """Magician: NPC Menu"""
    """State 0,1,3: [Lib] Menu start: General purpose_SubState"""
    while True:
        call = talk_m10_18_x12(z25=0, z26=220, z27=76600000, z28=0)
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
            assert talk_m10_18_x38(text1=76601400, text2=76601500, text3=76601600, z1=100961, z2=204800)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuSelection()
        """State 8: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76601700:"The path is yet long, young pupil."
    assert talk_m10_18_x14(text14=76601700)
    Goto('L0')

def talk_m10_18_x37():
    """Magician: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102720) != 1 and (GetPlayerStat(5, 1) > NpcInfoValue(7660, 2)) != 0 and GetEventFlag(104300)
        != 1):
        """State 6: Equipment transfer (Conditions: Reason is above a certain level) _SubState"""
        # lot:1766000:Northern Ritual Band+1, talk:76606000:"Do not neglect your studies, dear pupil."
        assert talk_m10_18_x15(lot4=1766000, z18=102720, text8=76606000, text9=76606010)
    elif GetEventFlag(204811) != 0:
        """State 3: Menu conversation: Flag initialization"""
        SetEventFlag(204810, 0)
        SetEventFlag(204811, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76602000:"The forces of magic, and souls, \nlie dormant in this land."
        assert talk_m10_18_x1(text1=76602000, z2=204810, z42=-1, z43=0)
    elif GetEventFlag(204810) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:76602100:"Use scrolls to unleash\nthe power of sorceries."
        assert talk_m10_18_x1(text1=76602100, z2=204811, z42=-1, z43=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 7: End state"""
    return 0

def talk_m10_18_x38(text1=76601400, text2=76601500, text3=76601600, z1=100961, z2=204800):
    """Menu Exit: Emigration Mes
    text1: Conversation ID (at the time of purchase)
    text2: Conversation ID (when not purchased)
    text3: Conversation ID (Migration decision)
    z1: Emigration: Global event flag
    z2: Emigration: Global conversation flag
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(z1) != 0 and GetEventFlag(z2) != 0:
        """State 4: Menu: Leaving: Relocation decision_SubState"""
        assert talk_m10_18_x1(text1=text3, z2=z2, z42=-1, z43=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Menu: Leave: At purchase_SubState"""
        assert talk_m10_18_x1(text1=text1, z2=0, z42=-1, z43=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Menu: Leave: Non-Purchase_SubState"""
        assert talk_m10_18_x1(text1=text2, z2=0, z42=-1, z43=0)
    """State 5: End state"""
    return 0

