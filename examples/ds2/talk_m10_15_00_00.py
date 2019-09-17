# -*- coding: utf-8 -*-
def talk_m10_15_7520():
    """Woman Knight (Andiel's Hall)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_15_x9(z21=103695, z22=104190, z23=115020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_15_x3(text6=75209200, z11=0, z12=20, z13=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_15_x6(z19=115020102, text11=75209500, text12=75209500, z20=75209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_15_x7(text14=75209600, z25=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: Woman Knight: Final: Conversation_SubState"""
                call = talk_m10_15_x25()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_15_x5(text15=75209400, text16=75209410, text17=75209420, text18=75209400,
                                          z26=115020105, z27=115020106)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        call = talk_m10_15_x4(z28=103690, text19=75209100, z29=0, z30=103695)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(115020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(115020105) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_15_x8(text13=75209300, z24=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_15_7710():
    """Sealed person"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 4: [Lib] Event: Branch_SubState"""
        call = talk_m10_15_x9(z21=103840, z22=104340, z23=115020141)
        if call.Get() == 1:
            """State 6: [Lib] Reunion hostility_SubState"""
            call = talk_m10_15_x3(text6=77109200, z11=0, z12=20, z13=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_15_x6(z19=115020142, text11=77109500, text12=77109500, z20=77109500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 9: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_15_x7(text14=77109600, z25=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0 and GetEventFlag(102810) != 1:
            """State 13: Sealed Person: Sealed: Conversation_SubState"""
            call = talk_m10_15_x38()
            if call.Done():
                continue
            elif GetEventFlag(102810) != 0 and ConversationEnded() != 0:
                """State 2: Conversation: damage reset"""
                ResetDamageTakenCount()
                while True:
                    """State 12: Sealed Person: Unsealed: Conversation_SubState"""
                    Label('L2')
                    call = talk_m10_15_x26()
                    if call.Done():
                        Continue('mainloop')
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0 and (not GetPlayerHollowState()) != 0:
                        """State 7: [Lib] Waiting for hostility (living person) _SubState"""
                        Label('L3')
                        call = talk_m10_15_x5(text15=77109450, text16=77109460, text17=77109470, text18=77109450,
                                              z26=115020145, z27=115020146)
                        if call.Done():
                            pass
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                        elif (NumberOfTimesDamaged(1) > 3) != 0:
                            """State 5: [Lib] First adversification_SubState"""
                            Label('L4')
                            call = talk_m10_15_x4(z28=103840, text19=77109100, z29=0, z30=0)
                            if call.Done():
                                Goto('L0')
                            elif KilledPlayer() != 0:
                                break
                            elif (HpValue() > 1) != 1:
                                Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 11: [Lib] Hostile waiting (dead) _SubState"""
                        Label('L5')
                        call = talk_m10_15_x5(text15=77109400, text16=77109410, text17=77109420, text18=77109400,
                                              z26=115020145, z27=115020146)
                        if call.Done():
                            pass
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                        elif (NumberOfTimesDamaged(1) > 3) != 0:
                            Goto('L4')
                    elif ((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(115020146) != 1 and (not
                          GetPlayerHollowState()) != 0):
                        Goto('L3')
                    elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(115020146) != 1:
                        Goto('L5')
                    elif ((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(115020145) != 1 and (not
                          GetPlayerHollowState()) != 0):
                        Goto('L3')
                    elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(115020145) != 1:
                        Goto('L5')
        elif call.Get() == 0:
            Goto('L2')
        """State 10: [Lib] Killing state_SubState"""
        talk_m10_15_x8(text13=77109300, z24=0)
        Quit()
    """State 3: Conversation: System: End"""
    EndMachine()

def talk_m10_15_x0(text20=_, z33=_, z34=0):
    """[Lib] Conversation: General purpose
    text20: Conversation ID
    z33: Conversation flag
    z34: Global event flag
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
    SetEventFlag(z33, 1)
    SetEventFlag(z34, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_15_x1(text1=_, z29=_, z31=-1, z32=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z29: Conversation flag
    z31: Display distance
    z32: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z31)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z29, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_15_x2(text13=_, z24=0):
    """[Lib] Conversation: Event end
    text13: Conversation ID
    z24: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text13, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z24, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_15_x3(text6=_, z11=0, z12=20, z13=80):
    """[Lib] Reunion hostility
    text6: Conversation message ID
    z11: Conversation flag ID
    z12: Display distance
    z13: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_15_x23(text6=text6, z11=z11, z12=z12, z13=z13)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_15_x4(z28=_, text19=_, z29=0, z30=_):
    """[Lib] First hostility
    z28: Hostile: Global event flag
    text19: Conversation ID
    z29: Conversation flag
    z30: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z28, 1)
    SetEventFlag(z30, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z28) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_15_x1(text1=text19, z29=z29, z31=-1, z32=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_15_x5(text15=_, text16=_, text17=_, text18=_, z26=_, z27=_):
    """[Lib] Hostile waiting
    text15: Conversation ID: 1 attacked
    text16: Conversation ID: Attacked 2
    text17: Conversation ID: 3 attacked
    text18: Conversation ID: 4 attacked
    z26: No use: Area and other flags
    z27: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z27) != 1, z27, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z26) != 1, z26, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_15_x1(text1=text18, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_15_x1(text1=text17, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_15_x1(text1=text16, z29=0, z31=-1, z32=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_15_x1(text1=text15, z29=0, z31=-1, z32=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_15_x6(z19=_, text11=_, text12=_, z20=_):
    """[Lib] Hostile state
    z19: Area and other flags: HP decreased
    text11: Conversation ID: HP drop 1
    text12: Conversation ID: HP drop 2
    z20: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z19) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_15_x10(text11=text11, z19=z19)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_15_x10(text11=text12, z19=z19)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_15_x10(text11=text12, z19=z19)

def talk_m10_15_x7(text14=_, z25=0):
    """[Lib] Death status
    text14: Conversation ID
    z25: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_15_x2(text13=text14, z24=z25)

def talk_m10_15_x8(text13=_, z24=0):
    """[Lib] Murder status
    text13: Conversation ID
    z24: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_15_x2(text13=text13, z24=z24)

def talk_m10_15_x9(z21=_, z22=_, z23=_):
    """[Lib] Event: Branch
    z21: Hostile flag
    z22: death flag
    z23: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z22) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z23) != 0
    elif GetEventFlag(z21) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_15_x10(text11=_, z19=_):
    """[Lib] Conversation: HP drop
    text11: Conversation ID
    z19: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text11, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z19, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_15_x11(text10=_, z18=0, action2=_):
    """[Lib] Choice conversation: Mes⇒Choice
    text10: Conversation ID
    z18: Global conversation flag
    action2: Selected conversation ID
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text10, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 7: Conversation: Select message"""
    ShowYesNoSelection(action2, GetCommonEventParamDecimal(7), -1)
    """State 8: Conversation: Selection message input waiting"""
    if CompareConversationResult(3) != 0:
        """State 11: End state: NO"""
        return 2
    elif CompareConversationResult(1) != 0:
        """State 9: End state: Cancel"""
        Label('L0')
        return 0
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif CompareConversationResult(2) != 0:
        """State 10: End state: YES"""
        return 1

def talk_m10_15_x12(action1=1205):
    """[Lib] selection dialog
    action1: Dialog: Text ID
    """
    """State 0,1: Selection dialog: Display"""
    # action:1205:"What is your choice?"
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

def talk_m10_15_x13(z14=0, z15=220, z16=_, z17=0):
    """[Lib] Menu start: General purpose
    z14: Camera parameter ID
    z15: Target Damipoly ID
    z16: NPC event parameter ID
    z17: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z17, z14, z15, z16)
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

def talk_m10_15_x14(text8=77102600, text9=77102700):
    """[Lib] Menu exit: General purpose
    text8: Conversation ID (at the time of purchase)
    text9: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_15_x1(text1=text8, z29=0, z31=-1, z32=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_15_x1(text1=text9, z29=0, z31=-1, z32=0)
    """State 4: End state"""
    return 0

def talk_m10_15_x15(text7=77102800):
    """[Lib] Menu cancellation: General purpose
    text7: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_15_x1(text1=text7, z29=0, z31=-1, z32=0)
    """State 4: End state"""
    return 0

def talk_m10_15_x16(lot3=1771000, z9=102800, text4=77106000, text5=77106010):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot3: Release seal: NPC menu
    z9: Global event flag
    text4: First half: Conversation ID
    text5: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_15_x1(text1=text4, z29=0, z31=-1, z32=0)
    # lot:1771000:Chaos Hood
    if call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_15_x24(z10=1011, lot1=lot3)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_15_x17(lot3=lot3, z9=z9)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_15_x1(text1=text5, z29=0, z31=-1, z32=0)
    """State 6: End state"""
    return 0

def talk_m10_15_x17(lot3=1771000, z9=102800):
    """[Lib] Item acquisition dialog
    lot3: Release seal: NPC menu
    z9: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z9, 1)
    # lot:1771000:Chaos Hood
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_15_x18(lot2=_, z4=_, text2=_, text3=_, z5=_, z6=_, z7=0, z8=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot2: Release seal: NPC menu
    z4: Item transfer: Global event flag
    text2: First half: Conversation ID
    text3: Second half: Conversation ID
    z5: Conversation: Global conversation flag
    z6: Trophy acquisition: Area and other flags
    z7: Emigration permission: Global event flag
    z8: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_15_x1(text1=text2, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z4) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z5, 1)
        SetEventFlag(z7, 1)
        SetEventFlag(z8, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_15_x1(text1=text3, z29=0, z31=-1, z32=0)
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_15_x24(z10=1011, lot1=lot2)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_15_x20(lot1=lot2, z1=z4, z2=z5, z3=z6, z7=z7, z8=z8)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_15_x19(lot1=1771040, z1=102804, text1=77102300, z2=205230, z3=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Key
    lot1: Release seal: NPC menu
    z1: Item transfer: Global event flag
    text1: Conversation ID
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
    call = talk_m10_15_x1(text1=text1, z29=0, z31=-1, z32=0)
    if call.Done() and GetEventFlag(z1) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z2, 1)
    # lot:1771040:Unleash Magic
    elif call.Done() and CanGetItemLot(lot1, 1) != 1:
        """State 8: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_15_x24(z10=1011, lot1=lot1)
    elif call.Done():
        """State 7: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_15_x20(lot1=lot1, z1=z1, z2=z2, z3=z3, z7=0, z8=0)
    """State 9: End state"""
    return 0

def talk_m10_15_x20(lot1=_, z1=_, z2=_, z3=_, z7=0, z8=0):
    """[Lib] Item acquisition dialog: Conversation
    lot1: Release seal: NPC menu
    z1: Item transfer: Global event flag
    z2: Conversation: Global conversation flag
    z3: Trophy acquisition: Area and other flags
    z7: Emigration permission: Global event flag
    z8: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(z3, 1)
    SetEventFlag(z2, 1)
    SetEventFlag(z1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_15_x21():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m10_15_x22():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_15_x23(text6=_, z11=0, z12=20, z13=80):
    """[Lib] Conversation: Hostile display only
    text6: Conversation ID
    z11: Conversation flag
    z12: Display distance
    z13: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text6, GetCommonEventParamDecimal(7), z12)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z11, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_15_x24(z10=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z10: Text ID
    lot1: Release seal: NPC menu
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_15_x25():
    """Woman Knight: Final: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetEventFlag(102497) != 1 and GetEventFlag(102498) != 0 and GetEventFlag(104190) != 1 and GetEventFlag(203651)
        != 0):
        """State 6: Equipment item transfer_SubState"""
        # lot:1752000:Mirrah Greatsword, talk:75206000:"Please...find my brother..."
        assert (talk_m10_15_x18(lot2=1752000, z4=102497, text2=75206000, text3=75206010, z5=0, z6=115020107,
                z7=0, z8=0))
    elif GetEventFlag(203651) != 0:
        """State 5: Encounter 5th: Speak: Part 3_SubState"""
        # talk:75202100:"My name is Lucatiel."
        call = talk_m10_15_x0(text20=75202100, z33=0, z34=0)
        if call.Done() and GetEventFlag(102489) != 1:
            """State 2: Encounter 5th: Stop generation"""
            SetEventFlag(102489, 1)
            assert GetEventFlag(102489) != 0
        elif call.Done():
            pass
    elif GetEventFlag(203650) != 0:
        """State 4: Encounter 5th: Speak: Part 2_SubState"""
        # talk:75202000:"How goes your journey?"
        assert talk_m10_15_x0(text20=75202000, z33=203651, z34=0)
    else:
        """State 3: Encounter 5th: Speak: Part 1_SubState"""
        # talk:75201900:"Who are you..."
        assert talk_m10_15_x0(text20=75201900, z33=203650, z34=0)
    """State 7: End state"""
    return 0

def talk_m10_15_x26():
    """Sealed Person: Unsealed: Conversation"""
    """State 0,1: Conversation: Start"""
    DeleteKeyGuideArea()
    ClearNpcMenuResults()
    """State 3: Unsealing: Conversation_SubState"""
    call = talk_m10_15_x28()
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: Release seal: NPC menu_SubState"""
        assert talk_m10_15_x39()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_15_x27():
    """Sealed: Conversation"""
    """State 0: Start state"""
    while True:
        """State 1: Sealing: Conversation: Start"""
        DeleteKeyGuideArea()
        if (not GetPlayerHollowState()) != 0:
            """State 3: Sealing: Conversation: Living_SubState"""
            call = talk_m10_15_x36()
            if call.Done():
                break
            elif (GetPlayerHollowState() == 1) != 0 and ConversationEnded() != 0:
                pass
            elif (GetPlayerHollowState() == 2) != 0 and ConversationEnded() != 0:
                pass
        else:
            """State 2: Sealed: Conversation: Dead_SubState"""
            call = talk_m10_15_x29()
            if call.Done():
                break
            elif (not GetPlayerHollowState()) != 0 and ConversationEnded() != 0:
                pass
    """State 4: End state"""
    return 0

def talk_m10_15_x28():
    """Unsealing: Conversation"""
    """State 0: Start state"""
    while True:
        """State 1: Release seal: Conversation: Start"""
        DeleteKeyGuideArea()
        if (not GetPlayerHollowState()) != 0:
            """State 4: Release seal: Raw person: Talk to 1 (loop) _SubState"""
            # talk:77103100:"By the very gods... What have you done..."
            call = talk_m10_15_x0(text20=77103100, z33=0, z34=0)
            if call.Done():
                break
            elif (GetPlayerHollowState() == 1) != 0 and ConversationEnded() != 0:
                continue
            elif (GetPlayerHollowState() == 2) != 0 and ConversationEnded() != 0:
                continue
        elif GetEventFlag(205240) != 0:
            """State 3: Unsealing: Dead: Talking 2 (single loop) _SubState"""
            # talk:77103000:"I'll spend some time travelling the lands..."
            call = talk_m10_15_x0(text20=77103000, z33=205240, z34=0)
            if call.Done():
                pass
            elif (not GetPlayerHollowState()) != 0 and ConversationEnded() != 0:
                continue
        else:
            """State 2: Unseal: Dead: Talk to 1_SubState"""
            # talk:77102900:"Hmgh..."
            call = talk_m10_15_x0(text20=77102900, z33=205240, z34=0)
            if call.Done():
                pass
            elif (not GetPlayerHollowState()) != 0 and ConversationEnded() != 0:
                continue
        """State 5: Normal: End state"""
        return 0
    """State 6: Menu: Exit state"""
    return 1

def talk_m10_15_x29():
    """Sealed: Conversation: Dead"""
    """State 0,1: Sealing: Conversation: Dead: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(205230) != 0:
        """State 7: Enclosed person: NPC menu_SubState"""
        assert talk_m10_15_x35()
    elif GetEventFlag(205229) != 0:
        """State 6: Sealed: Conversation: Dead: Final Request_SubState"""
        assert talk_m10_15_x34()
    elif GetEventFlag(205225) != 0:
        """State 5: Sealing: Conversation: Dead: 4th request_SubState"""
        assert talk_m10_15_x33()
    elif GetEventFlag(205224) != 0:
        """State 4: Sealing: Conversation: Dead: Third Request_SubState"""
        assert talk_m10_15_x32()
    elif GetEventFlag(205223) != 0:
        """State 3: Sealing: Conversation: Dead: Second person request_SubState"""
        assert talk_m10_15_x31()
    else:
        """State 2: Sealing: Conversation: Dead: 1st request_SubState"""
        assert talk_m10_15_x30()
    """State 8: End state"""
    return 0

def talk_m10_15_x30():
    """Sealing: Conversation: Dead: 1st request"""
    """State 0,1: Sealing: Dead: 1st request: Start"""
    if GetEventFlag(205221) != 0:
        """State 7: Sealed: Dead: Talk to 3_SubState"""
        # talk:77100800:"Now, I don't have anything against humans,\nbut how is it that you go about defining good and evil?"
        assert talk_m10_15_x0(text20=77100800, z33=205222, z34=0)
        """State 6: Sealing: Dead: Talking 3: 1st person request dialog_SubState"""
        # action:1205:"What is your choice?"
        call = talk_m10_15_x12(action1=1205)
        if call.Get() == 0:
            """State 4: Sealed: Dead: 1st request: YES_SubState"""
            # talk:77100900:"Yes, I see, how very kind of you."
            assert talk_m10_15_x1(text1=77100900, z29=205223, z31=-1, z32=0)
        elif call.Get() == 1:
            """State 5: Sealing: Dead: 1st request: NO_SubState"""
            Label('L0')
            # talk:77101100:"Yes, yes, of course.\nForget that I asked."
            assert talk_m10_15_x1(text1=77101100, z29=0, z31=-1, z32=0)
        elif call.Get() == 2:
            Goto('L0')
    elif GetEventFlag(205220) != 0:
        """State 3: Sealing: Dead: Talk to 2_SubState"""
        # talk:77100500:"This? This contains my power."
        assert talk_m10_15_x0(text20=77100500, z33=205221, z34=0)
    else:
        """State 2: Sealed: Dead: Talk to 1_SubState"""
        # talk:77100400:"Well, you're nicely hollowed, aren't you..."
        assert talk_m10_15_x0(text20=77100400, z33=205220, z34=0)
    """State 8: End state"""
    return 0

def talk_m10_15_x31():
    """Sealing: Conversation: Dead: Request for second person"""
    """State 0,1: Sealing: Dead: Second person Request: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(205226) != 0:
        """State 8: Sealing: Dead: Second person request: Second person request conversation_SubState"""
        # talk:77101300:"I want you to kill one more."
        assert talk_m10_15_x0(text20=77101300, z33=0, z34=0)
        """State 7: Sealing: Dead: Second person request: Second person request dialog_SubState"""
        # action:1205:"What is your choice?"
        call = talk_m10_15_x12(action1=1205)
        if call.Get() == 0:
            """State 5: Sealing: Dead: Second person request: Second person request: YES_SubState"""
            Label('L0')
            # talk:77101400:"Yes, I knew I could count on you."
            assert talk_m10_15_x1(text1=77101400, z29=205224, z31=-1, z32=0)
        elif call.Get() == 1:
            """State 6: Sealing: Dead: Second person request: Second person request: NO_SubState"""
            Label('L1')
            # talk:77101100:"Yes, yes, of course.\nForget that I asked."
            assert talk_m10_15_x1(text1=77101100, z29=0, z31=-1, z32=0)
        elif call.Get() == 2:
            Goto('L1')
    elif GetEventFlag(205226) != 0:
        """State 4: Sealed: Dead: Second person request: Second person request_SubState"""
        # talk:77101300:"I want you to kill one more."
        call = talk_m10_15_x11(text10=77101300, z18=0, action2=77101330)
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            Goto('L1')
        elif call.Get() == 2:
            Goto('L1')
    # goods:50950000:Ladder Miniature
    elif (ItemCount(50950000, 1, 1, 0) > 1) != 0:
        """State 3: Sealed: Dead: Second Request: First Request Achieved_SubState"""
        # lot:1771010:Dispelling Ring, talk:77101200:"Heh heh heh... Fine work.", talk:77101202:""
        assert (talk_m10_15_x18(lot2=1771010, z4=102801, text2=77101200, text3=77101202, z5=205226, z6=0,
                z7=0, z8=0))
    else:
        """State 2: Sealed: Dead: Second person request: First person not achieved_SubState"""
        # talk:77101000:"I want you to kill a merchant named Gilligan."
        call = talk_m10_15_x0(text20=77101000, z33=0, z34=0)
        if call.Done():
            pass
        # goods:50950000:Ladder Miniature
        elif (ItemCount(50950000, 1, 1, 0) > 1) != 0:
            pass
    """State 9: End state"""
    return 0

def talk_m10_15_x32():
    """Sealing: Conversation: Dead: Request for 3rd person"""
    """State 0,1: Sealing: Dead: Third person Request: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(205227) != 0:
        """State 6: Sealed: Dead: 3rd person request: 3rd person request conversation_SubState"""
        # talk:77101600:"I want you to kill one more."
        assert talk_m10_15_x0(text20=77101600, z33=0, z34=0)
        """State 7: Sealed: Dead: Third person request: Third person request dialog_SubState"""
        # action:1205:"What is your choice?"
        call = talk_m10_15_x12(action1=1205)
        if call.Get() == 0:
            """State 4: Sealing: Dead: Third person request: Third person request: YES_SubState"""
            # talk:77101700:"Yes, very good."
            assert talk_m10_15_x1(text1=77101700, z29=205225, z31=-1, z32=0)
        elif call.Get() == 1:
            """State 5: Sealing: Dead: Third person request: Third person request: NO_SubState"""
            Label('L0')
            # talk:77101100:"Yes, yes, of course.\nForget that I asked."
            assert talk_m10_15_x1(text1=77101100, z29=0, z31=-1, z32=0)
        elif call.Get() == 2:
            Goto('L0')
    # goods:27510100:Cale's Helm
    elif (ItemCount(27510100, 1, 1, 0) > 1) != 0:
        """State 3: Sealed: Dead: 3rd request: 2nd request achieved_SubState"""
        # lot:1771020:Simpleton's Spice, talk:77101200:"Heh heh heh... Fine work.", talk:77101202:""
        assert (talk_m10_15_x18(lot2=1771020, z4=102802, text2=77101200, text3=77101202, z5=205227, z6=0,
                z7=0, z8=0))
    else:
        """State 2: Sealing: Dead: 3rd person Request: 2nd person unachieved_SubState"""
        # talk:77101500:"I want you to kill Cale,\nthe cartographer."
        assert talk_m10_15_x0(text20=77101500, z33=0, z34=0)
    """State 8: End state"""
    return 0

def talk_m10_15_x33():
    """Sealing: Conversation: Dead: Request for 4th person"""
    """State 0,1: Sealing: Dead: 4th request: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(205228) != 0:
        """State 7: Sealed: Dead: 4th person request: 4th person request conversation_SubState"""
        # talk:77102000:"You could kill a dozen like that, and it wouldn't matter.\nI want you to kill someone of import."
        assert talk_m10_15_x0(text20=77102000, z33=0, z34=0)
        """State 8: Sealing: Dead: 4th request: 4th request dialog_SubState"""
        # action:1205:"What is your choice?"
        call = talk_m10_15_x12(action1=1205)
        if call.Get() == 0:
            """State 2: Sealed: Dead: 4th request: 4th request: YES"""
            Label('L0')
            SetEventFlag(205229, 1)
        elif call.Get() == 1:
            """State 6: Sealed: Dead: 4th request: 4th request: NO_SubState"""
            Label('L1')
            # talk:77102100:"Having second thoughts?"
            assert talk_m10_15_x1(text1=77102100, z29=0, z31=-1, z32=0)
        elif call.Get() == 2:
            Goto('L1')
    elif GetEventFlag(205228) != 0:
        """State 5: Sealed: Dead: 4th request: 4th request_SubState"""
        # talk:77102000:"You could kill a dozen like that, and it wouldn't matter.\nI want you to kill someone of import."
        call = talk_m10_15_x11(text10=77102000, z18=0, action2=77102070)
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            Goto('L1')
        elif call.Get() == 2:
            Goto('L1')
    # goods:3900000:Sunset Staff
    elif (ItemCount(3900000, 1, 1, 0) > 1) != 0:
        """State 4: Sealed: Dead: 4th request: 3rd request achieved_SubState"""
        # lot:1771030:Forbidden Sun
        assert (talk_m10_15_x18(lot2=1771030, z4=102803, text2=77101250, text3=77101252, z5=205228, z6=0,
                z7=0, z8=0))
    else:
        """State 3: Sealed: Dead: 4th Request: 3rd unachieved_SubState"""
        # talk:77101800:"I want you to kill Felkin.\nThat's Felkin, the hexer."
        assert talk_m10_15_x0(text20=77101800, z33=0, z34=0)
    """State 9: End state"""
    return 0

def talk_m10_15_x34():
    """Sealing: Conversation: Dead: Final request"""
    """State 0,1: Sealing: Dead: Final request: Start"""
    DeleteKeyGuideArea()
    # goods:60355000:Aged Feather
    if (ItemCount(60355000, 1, 1, 0) > 1) != 0:
        """State 4: Sealing: Dead: Final request: 4th person achieved_SubState"""
        # lot:1771040:Unleash Magic, talk:77102300:"Yes, that's the feather."
        assert talk_m10_15_x19(lot1=1771040, z1=102804, text1=77102300, z2=205230, z3=0)
        """State 2: Sealed: Dead: Final Request: White Phantom Appearance: Set Flag"""
        SetEventFlag(102811, 1)
        assert GetEventFlag(102811) != 0
    else:
        """State 3: Sealed: Dead: Final request: 4th unachieved_SubState"""
        # talk:77102200:"Your mark is the girl in Majula known as the muse."
        assert talk_m10_15_x0(text20=77102200, z33=0, z34=0)
    """State 5: End state"""
    return 0

def talk_m10_15_x35():
    """Enclosed person: NPC menu"""
    """State 0,1,2: Menu: First conversation_SubState"""
    # talk:77102500:"What do you require?"
    assert talk_m10_15_x0(text20=77102500, z33=0, z34=0)
    while True:
        """State 3: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_15_x13(z14=0, z15=220, z16=77100000, z17=0)
        if call.Get() == 2:
            """State 6: Enclosed person: Menu conversation_SubState"""
            call = talk_m10_15_x37()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Exit menu: General purpose_SubState"""
            # talk:77102600:"Find what you wanted? Hah hah hah hah...", talk:77102700:"Well, as you wish. Heh heh..."
            assert talk_m10_15_x14(text8=77102600, text9=77102700)
        """State 7: End state"""
        Label('L0')
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:77102800:"Oh, no?"
    assert talk_m10_15_x15(text7=77102800)
    Goto('L0')

def talk_m10_15_x36():
    """Sealing: Conversation: Living"""
    """State 0,1: Sealing: Conversation: Living: Start"""
    DeleteKeyGuideArea()
    if GetEventFlag(205220) != 0 and GetEventFlag(205202) != 1:
        """State 5: Sealed: Living: After deceased conversation _SubState"""
        # talk:77100300:"I haven't said anything strange, have I?"
        assert talk_m10_15_x0(text20=77100300, z33=205202, z34=0)
    elif GetEventFlag(205201) != 0:
        """State 4: Sealing: Living: Talking 3 (single loop) _SubState"""
        # talk:77100200:"Please, just leave me alone."
        assert talk_m10_15_x0(text20=77100200, z33=0, z34=0)
    elif GetEventFlag(205200) != 0:
        """State 3: Sealing: Living: Talk to 2_SubState"""
        # talk:77100100:"Just leave me alone, please."
        assert talk_m10_15_x0(text20=77100100, z33=205201, z34=0)
    else:
        """State 2: Sealed: Living: Talk to 1_SubState"""
        # talk:77100000:"P-please, just stay away."
        assert talk_m10_15_x0(text20=77100000, z33=205200, z34=0)
    """State 6: End state"""
    return 0

def talk_m10_15_x37():
    """Enclosed person: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(205230) != 0 and GetEventFlag(102800) != 1 and GetEventFlag(104340) != 1:
        """State 4: Equipment transfer (condition: all requests achieved) _SubState"""
        # lot:1771000:Chaos Hood, talk:77106000:"Heh heh heh heh heh..."
        assert talk_m10_15_x16(lot3=1771000, z9=102800, text4=77106000, text5=77106010)
    else:
        """State 3: Menu conversation: Part 1_SubState"""
        # talk:77102400:"Now I am at peace."
        assert talk_m10_15_x1(text1=77102400, z29=0, z31=-1, z32=0)
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_15_x38():
    """Sealed: Sealed: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Sealing: Conversation_SubState"""
    assert talk_m10_15_x27()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 4: End state"""
    return 0

def talk_m10_15_x39():
    """Release seal: NPC menu"""
    """State 0,1,2: [Lib] Menu start: General purpose_SubState"""
    call = talk_m10_15_x13(z14=0, z15=220, z16=77101000, z17=0)
    if call.Get() == 0:
        """State 4: [Lib] Menu canceled: No Mes_SubState"""
        assert talk_m10_15_x22()
    elif call.Get() == 1:
        """State 3: [Lib] Menu exit: No Mes_SubState"""
        assert talk_m10_15_x21()
    """State 5: End state"""
    return 0

