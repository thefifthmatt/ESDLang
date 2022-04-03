# -*- coding: utf-8 -*-
def talk_m10_19_7530():
    """Kanemori: Vane"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_19_x7(flag17=103700, flag18=104200, flag19=119020101)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_19_x3(text9=75309200, z27=0, z28=20, z29=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_19_x5(flag16=119020102, text18=75309500, text19=75309500, z37=75309500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 7: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_19_x6(text20=75309300, z38=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 9: [Lib] Kanemori: Conversation_SubState"""
                # action:1335:"Join the Bell Keeper covenant?", action:1345:"Abandon your covenant and\njoin the Bell Keeper covenant?"
                call = talk_m10_19_x24(z3=60, action1=1335, action2=1345, z4=119020107)
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_19_x4(text21=75309400, text22=75309410, text23=75309420, text24=75309400,
                                          flag20=119020105, flag21=119020106)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 8: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_19_x14(flag14=103700, text10=75309100, z30=0, val4=6, z31=200905,
                                               z32=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(119020106) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(119020105) != 1:
                    Goto('L2')
        """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
        talk_m10_19_x38(text7=75309600, z17=0, val2=6)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_19_7720():
    """Curio shop"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_19_x7(flag17=103850, flag18=104350, flag19=119020111)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_19_x3(text9=77209200, z27=0, z28=20, z29=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_19_x5(flag16=119020112, text18=77209500, text19=77209500, z37=77209500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 7: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_19_x6(text20=77209300, z38=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 8: Rare goods store: Conversation_SubState"""
                call = talk_m10_19_x40()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 5: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_19_x4(text21=77209400, text22=77209410, text23=77209420, text24=77209400,
                                          flag20=119020115, flag21=119020116)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_19_x14(flag14=103850, text10=77209100, z30=0, val4=7, z31=200906,
                                               z32=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(119020116) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(119020115) != 1:
                    Goto('L2')
        """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
        talk_m10_19_x38(text7=77209600, z17=0, val2=7)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()
    Quit()

def talk_m10_19_x0(text14=_, z41=_, z42=0):
    """[Lib] Conversation: General purpose
    text14: Conversation ID
    z41: Conversation flag
    z42: Global event flag
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
    SetEventFlag(z41, 1)
    SetEventFlag(z42, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_19_x1(text1=_, z30=_, z39=-1, z40=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z30: Conversation flag
    z39: Display distance
    z40: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z39)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z30, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_19_x2(text7=_, z17=0):
    """[Lib] Conversation: Event end
    text7: Conversation ID
    z17: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z17, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_19_x3(text9=_, z27=0, z28=20, z29=80):
    """[Lib] Reunion hostility
    text9: Conversation message ID
    z27: Conversation flag ID
    z28: Display distance
    z29: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_19_x29(text9=text9, z27=z27, z28=z28, z29=z29)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_19_x4(text21=_, text22=_, text23=_, text24=_, flag20=_, flag21=_):
    """[Lib] Hostile waiting
    text21: Conversation ID: 1 attacked
    text22: Conversation ID: Attacked 2
    text23: Conversation ID: 3 attacked
    text24: Conversation ID: 4 attacked
    flag20: No use: Area and other flags
    flag21: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(flag21) != 1, flag21, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(flag20) != 1, flag20, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_19_x1(text1=text24, z30=0, z39=-1, z40=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_19_x1(text1=text23, z30=0, z39=-1, z40=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_19_x1(text1=text22, z30=0, z39=-1, z40=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_19_x1(text1=text21, z30=0, z39=-1, z40=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_19_x5(flag16=_, text18=_, text19=_, z37=_):
    """[Lib] Hostile state
    flag16: Area and other flags: HP decreased
    text18: Conversation ID: HP drop 1
    text19: Conversation ID: HP drop 2
    z37: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(flag16) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_19_x8(text18=text18, flag16=flag16)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_19_x8(text18=text19, flag16=flag16)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_19_x8(text18=text19, flag16=flag16)
    """Unused"""
    """State 7: End state"""
    return 0

def talk_m10_19_x6(text20=_, z38=0):
    """[Lib] Murder status
    text20: Conversation ID
    z38: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_19_x2(text7=text20, z17=z38)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m10_19_x7(flag17=_, flag18=_, flag19=_):
    """[Lib] Event: Branch
    flag17: Hostile flag
    flag18: death flag
    flag19: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(flag18) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(flag19) != 0
    elif GetEventFlag(flag17) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_19_x8(text18=_, flag16=_):
    """[Lib] Conversation: HP drop
    text18: Conversation ID
    flag16: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text18, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(flag16, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_19_x9(flag15=119020114, text14=77200200, text15=77200300, text16=77200400, text17=77200500):
    """[Lib] Conversation: Greeting: General
    flag15: Area other flag: Contact flag
    text14: Text ID: Talk to_continuous 1
    text15: Text ID: Talk to_continuous 2
    text16: Text ID: Talk to _After a long time 1
    text17: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(flag15) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_19_x0(text14=text14, z41=0, z42=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_19_x0(text14=text15, z41=0, z42=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_19_x0(text14=text16, z41=0, z42=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_19_x0(text14=text17, z41=0, z42=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(flag15, 1)
    """State 10: End state"""
    return 0

def talk_m10_19_x10(action1=_):
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

def talk_m10_19_x11(z33=0, z34=220, z35=_, z36=0):
    """[Lib] Menu start: General purpose
    z33: Camera parameter ID
    z34: Target Damipoly ID
    z35: NPC event parameter ID
    z36: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z36, z33, z34, z35)
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

def talk_m10_19_x12(text12=77200600, text13=77200700):
    """[Lib] Menu exit: General purpose
    text12: Conversation ID (at the time of purchase)
    text13: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_19_x1(text1=text12, z30=0, z39=-1, z40=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_19_x1(text1=text13, z30=0, z39=-1, z40=0)
    """State 4: End state"""
    return 0

def talk_m10_19_x13(text11=77200900):
    """[Lib] Menu cancellation: General purpose
    text11: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_19_x1(text1=text11, z30=0, z39=-1, z40=0)
    """State 4: End state"""
    return 0

def talk_m10_19_x14(flag14=_, text10=_, z30=0, val4=_, z31=_, z32=0):
    """[Lib] First hostility _ (pledge cancellation)
    flag14: Hostile: Global event flag
    text10: Conversation ID
    z30: Conversation flag
    val4: Cancellation pledge name
    z31: Pledge cancellation: Global conversation flag
    z32: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(flag14, 1)
    SetEventFlag(z32, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(flag14) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_19_x28(val2=val4)
    if call.Done() and (GetPlayerCovenant() == val4) != 0:
        """State 3: First hostility: pledge change"""
        ChangePlayerCovenantIf((GetPlayerCovenant() == val4) != 0, 0)
        assert (GetStateTime() >= 0) != 0
        """State 2: First hostility: save execution"""
        SaveExecution()
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 4: Conversation: First hostilization_SubState"""
    assert talk_m10_19_x1(text1=text10, z30=z30, z39=-1, z40=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_19_x15(text6=_, z14=0, lot9=_, flag8=_, z15=215, z3=60):
    """[Lib] Conversation: Pledge ranking
    text6: Ranking: Conversation ID
    z14: Ranking: Conversation flag
    lot9: Item lottery
    flag8: Ranking transfer: Global event flag
    z15: Previous rank: Global variable
    z3: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_19_x17(action6=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text6, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z14, 1)
    if CanGetItemLot(lot9, 1) != 1 and GetEventFlag(flag8) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_19_x39(z16=1011, lot1=lot9)
    elif GetEventFlag(flag8) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_19_x19(lot1=lot9, flag1=flag8)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z15, GetAreaVariable(z3))
    """State 11: End state"""
    return 0

def talk_m10_19_x16(val1=7, z5=8, lot5=2008000, flag5=102830, action3=1336, action4=1346, z6=119020117):
    """[Lib] Menu item: Make a pledge
    val1: Pledge name
    z5: Event action
    lot5: Item lottery ID
    flag5: Item transfer: Global event flag
    action3: Pledge text
    action4: Overwriting pledge text
    z6: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_19_x17(action6=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m10_19_x31(val1=val1, z5=z5, lot5=lot5, flag5=flag5, action1=action3, action2=action4,
                               z4=z6)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_19_x17(action6=_):
    """[Lib] OK dialog
    action6: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action6, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_19_x18(goods1=62130000, val3=7, z23=61, z24=216, z25=15, lot10=0, flag12=0, flag13=102833):
    """[Lib] Menu item: Dedicated
    goods1: Special Offer: Event Item
    val3: Pledge name
    z23: Current pledge rank: Area variable
    z24: Last pledge rank: global variable
    z25: Event action
    lot10: Transfer: Item lottery
    flag12: Transfer: Global event flag
    flag13: Ranking 3 items: Global event flag
    """
    """State 0,1: Votive: Start"""
    if (GetPlayerCovenant() == val3) != 1:
        """State 8: Votive: Confirmation dialog not signed"""
        # action:1314:"You must belong to this covenant\nto make an offering"
        assert talk_m10_19_x17(action6=1314)
    elif GetEventFlag(flag13) != 0 and (GetGlobalVariable(z24) == 3) != 0:
        """State 4: Dedication: No more dedication confirmation dialog_SubState"""
        Label('L0')
        # action:1309:"There is nothing more to offer.\nYou have done fine work."
        assert talk_m10_19_x17(action6=1309)
    elif GetEventFlag(flag13) != 0 and (GetPlayerCovenantLevel(val3) > 3) != 0:
        Goto('L0')
    else:
        """State 6: Dedication: Dedication selection dialog_SubState"""
        # action:1306:"Offer\n%s?"
        call = talk_m10_19_x30(action5=1306, goods1=goods1)
        # goods:62130000:Dragon Scale
        if call.Get() == 0 and (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 5: Votive: Confirmation of possession of possession _SubState"""
            # action:1310:"You have no offerings"
            assert talk_m10_19_x17(action6=1310)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Dedication_SubState"""
            assert talk_m10_19_x33(z26=15, goods1=goods1, z23=z23, val3=val3, lot10=lot10, flag12=flag12)
            """State 3: Delivery confirmation dialog_SubState"""
            # action:1307:"Your devotion to your\ncovenant has deepened"
            assert talk_m10_19_x17(action6=1307)
            """State 9: Rank up: End state"""
            return 0
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 2: Votive: Finish"""
    ClearNpcMenuSelection()
    """State 10: End state"""
    return 1

def talk_m10_19_x19(lot1=_, flag1=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    flag1: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(flag1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_19_x20(lot8=1772000, z13=102820, text5=77206000):
    """[Lib] Equipment transfer: Mes⇒Item
    lot8: Item lottery ID
    z13: Global event flag
    text5: Conversation ID
    """
    """State 0,1,2: Equipment transfer: Conversation_SubState"""
    call = talk_m10_19_x1(text1=text5, z30=0, z39=-1, z40=0)
    # lot:1772000:Covetous Gold Serpent Ring+1
    if call.Done() and CanGetItemLot(lot8, 1) != 1:
        """State 4: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_19_x39(z16=1011, lot1=lot8)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_19_x19(lot1=lot8, flag1=z13)
    """State 5: End state"""
    return 0

def talk_m10_19_x21(lot7=_, flag7=_, text3=_, text4=_, z9=0, z10=0, z11=0, z12=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot7: Item lottery ID
    flag7: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z9: Conversation: Global conversation flag
    z10: Trophy acquisition: Area and other flags
    z11: Emigration permission: Global event flag
    z12: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_19_x1(text1=text3, z30=0, z39=-1, z40=0)
    if call.Done() and GetEventFlag(flag7) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z9, 1)
        SetEventFlag(z11, 1)
        SetEventFlag(z12, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_19_x1(text1=text4, z30=0, z39=-1, z40=0)
    elif call.Done() and CanGetItemLot(lot7, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_19_x39(z16=1011, lot1=lot7)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_19_x22(lot6=lot7, flag6=flag7, z7=z9, z8=z10, z11=z11, z12=z12)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_19_x22(lot6=_, flag6=_, z7=0, z8=0, z11=0, z12=0):
    """[Lib] Item acquisition dialog: Conversation
    lot6: Item lottery ID
    flag6: Item transfer: Global event flag
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    z11: Emigration permission: Global event flag
    z12: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z12, 1)
    SetEventFlag(z11, 1)
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(flag6, 1)
    AwardItem(lot6, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_19_x23(lot6=1753020, flag6=102511, text1=75300300, text2=75300310, z7=0, z8=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot6: Item lottery ID
    flag6: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_19_x1(text1=text1, z30=0, z39=-1, z40=0)
    if call.Done() and GetEventFlag(flag6) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z7, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_19_x1(text1=text2, z30=0, z39=-1, z40=0)
    # lot:1753020:Bell Keeper's Seal
    elif call.Done() and CanGetItemLot(lot6, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_19_x39(z16=1011, lot1=lot6)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_19_x22(lot6=lot6, flag6=flag6, z7=z7, z8=z8, z11=0, z12=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_19_x24(z3=60, action1=1335, action2=1345, z4=119020107):
    """[Lib] Kanemori: Conversation
    z3: Current pledge rank: Area variable
    action1: Pledge text
    action2: Overwriting pledge text
    z4: For trophies: Area and other flags
    """
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetPlayerCovenant() == 6) != 0:
        """State 4: Kanemori: Pledge conversation_SubState"""
        assert talk_m10_19_x26(z3=z3)
    elif GetEventFlag(200905) != 0:
        """State 5: Kanemori: Re-pledge conversation_SubState"""
        assert talk_m10_19_x27(action1=action1, action2=action2, z4=z4)
    else:
        """State 3: Kanemori: Unpowed conversation_SubState"""
        assert talk_m10_19_x25(action1=action1, action2=action2, z4=z4)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_19_x25(action1=1335, action2=1345, z4=119020107):
    """Kanemori: Unpowed conversation
    action1: Pledge text
    action2: Overwriting pledge text
    z4: For trophies: Area and other flags
    """
    """State 0,1: Unpowed conversation: Start"""
    if GetEventFlag(203701) != 0:
        """State 4: Speak: Part 3_SubState"""
        # talk:75300200:"Hah hah hah, ooh hoo hoo!"
        assert talk_m10_19_x0(text14=75300200, z41=0, z42=0)
        """State 6: [Lib] Pledge conclusion: General purpose_SubState"""
        # lot:0:No Item
        call = talk_m10_19_x31(val1=6, z5=8, lot5=0, flag5=0, action1=action1, action2=action2, z4=z4)
        if call.Get() == 1:
            """State 7: Speak: Part 3: YES_SubState"""
            # lot:1753020:Bell Keeper's Seal, talk:75300300:"Hah hah, heh! Here, for you!", talk:75300310:"When you're 'round the bell,\nyou'll be brought near!"
            assert (talk_m10_19_x23(lot6=1753020, flag6=102511, text1=75300300, text2=75300310, z7=0,
                    z8=0))
        elif call.Get() == 0:
            """State 5: Speak: Part 3: NO_SubState"""
            # talk:75300400:"Gah hah hah hah hah!"
            assert talk_m10_19_x1(text1=75300400, z30=0, z39=-1, z40=0)
    elif GetEventFlag(203700) != 0:
        """State 3: Talk to: 2_SubState"""
        # talk:75300100:"A long, long, long time ago,\nthe Princess, she made me, yes, just like so!"
        assert talk_m10_19_x0(text14=75300100, z41=203701, z42=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:75300000:"Undead! Undead!"
        assert talk_m10_19_x0(text14=75300000, z41=203700, z42=0)
    """State 8: End state"""
    return 0

def talk_m10_19_x26(z3=60):
    """Kanemori: Pledge conversation
    z3: Current pledge rank: Area variable
    """
    """State 0,1: Pledge conversation: start"""
    SetAreaVariable(z3, GetPlayerCovenantLevel(6))
    if GetEventFlag(102511) != 1:
        """State 10: When ring is not transferred: Insurance_SubState"""
        # lot:1753020:Bell Keeper's Seal, talk:75300300:"Hah hah, heh! Here, for you!", talk:75300310:"When you're 'round the bell,\nyou'll be brought near!"
        assert (talk_m10_19_x21(lot7=1753020, flag7=102511, text3=75300300, text4=75300310, z9=0, z10=0,
                z11=0, z12=0))
    elif (GetEventFlag(102510) != 1 and (PhantomMultiplayerCount(11) > NpcInfoValue(7530, 0)) != 0 and
          GetEventFlag(104200) != 1):
        """State 4: Equipment transfer (Condition: Achieved Summon Phantom Summon) _SubState"""
        # lot:1753000:Rusted Coin, talk:75306000:"Forever...for true!"
        assert (talk_m10_19_x21(lot7=1753000, flag7=102510, text3=75306000, text4=75306020, z9=0, z10=0,
                z11=0, z12=0))
    else:
        """State 6: [Lib] Pledge: Rank up: Conversation_SubState"""
        call = talk_m10_19_x34(z21=6, z3=z3, z22=215, flag9=102512, flag10=102513, flag11=102514)
        if call.Get() == 1:
            """State 3: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(z3) > 1) != 0 and GetEventFlag(102512) != 1:
                """State 7: Conversation: Pledge Ranking 1_SubState"""
                # talk:75300700:"Gah hah! Hah hah hah!", lot:2004011:Titanite Slab
                assert talk_m10_19_x15(text6=75300700, z14=0, lot9=2004011, flag8=102512, z15=215, z3=z3)
                Goto('L0')
            elif (GetAreaVariable(z3) > 2) != 0 and GetEventFlag(102513) != 1:
                """State 8: Conversation: Pledge Ranking 2_SubState"""
                # talk:75300800:"Bravo, my friend, look how they've bled!", lot:2004012:Hidden Weapon
                assert talk_m10_19_x15(text6=75300800, z14=0, lot9=2004012, flag8=102513, z15=215, z3=z3)
                Goto('L0')
            elif (GetAreaVariable(z3) > 3) != 0 and GetEventFlag(102514) != 1:
                """State 9: Conversation: Pledge Ranking 3_SubState"""
                # talk:75300900:"Hah! Haaaah!", lot:2004013:Bell Keeper Helmet
                assert talk_m10_19_x15(text6=75300900, z14=0, lot9=2004013, flag8=102514, z15=215, z3=z3)
                Goto('L0')
            else:
                pass
        elif call.Get() == 0:
            pass
        """State 5: When pledged: Talk: Part 1_SubState"""
        # talk:75300600:"Ah hah hah! The Princess made me!\nTo guard the Bell of Alken!"
        assert talk_m10_19_x0(text14=75300600, z41=0, z42=0)
    """State 2: Pledge conversation: End"""
    Label('L0')
    ClearNpcMenuSelection()
    """State 11: End state"""
    return 0

def talk_m10_19_x27(action1=1335, action2=1345, z4=119020107):
    """Kanemori: Re-pledge conversation
    action1: Pledge text
    action2: Overwriting pledge text
    z4: For trophies: Area and other flags
    """
    """State 0,1,3: Re-pledge: Talk: Part 1_SubState"""
    # talk:75300500:"You want to guard the bell, do you?"
    assert talk_m10_19_x0(text14=75300500, z41=0, z42=0)
    """State 6: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item
    call = talk_m10_19_x31(val1=6, z5=8, lot5=0, flag5=0, action1=action1, action2=action2, z4=z4)
    if call.Get() == 0:
        """State 5: Speak: Part 3: NO_SubState"""
        # talk:75300400:"Gah hah hah hah hah!"
        assert talk_m10_19_x1(text1=75300400, z30=0, z39=-1, z40=0)
    elif call.Get() == 1 and GetEventFlag(102511) != 1:
        """State 7: When ring is not transferred: Insurance_SubState"""
        # lot:1753020:Bell Keeper's Seal, talk:75300300:"Hah hah, heh! Here, for you!", talk:75300310:"When you're 'round the bell,\nyou'll be brought near!"
        assert (talk_m10_19_x21(lot7=1753020, flag7=102511, text3=75300300, text4=75300310, z9=0, z10=0,
                z11=0, z12=0))
    elif call.Get() == 1:
        """State 4: Laughter_SubState"""
        assert talk_m10_19_x1(text1=75306020, z30=0, z39=-1, z40=0)
    """State 2: Re-pow conversation: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m10_19_x28(val2=_):
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

def talk_m10_19_x29(text9=_, z27=0, z28=20, z29=80):
    """[Lib] Conversation: Hostile display only
    text9: Conversation ID
    z27: Conversation flag
    z28: Display distance
    z29: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), z28)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z27, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_19_x30(action5=_, goods1=_):
    """[Lib] Selection dialog: Item display
    action5: Dialog: Text ID
    goods1: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    DisplayOwnYesNoMenu(action5, 0, -1, 2, goods1, 0)
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

def talk_m10_19_x31(val1=_, z5=8, lot5=_, flag5=_, action1=_, action2=_, z4=_):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z5: Event action
    lot5: Item lottery ID
    flag5: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z4: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z4, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_19_x10(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_19_x17(action6=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_19_x32(z5=z5, val1=val1, lot5=lot5, flag5=flag5) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_19_x17(action6=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_19_x10(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_19_x28(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_19_x32(z5=8, val1=_, lot5=_, flag5=_):
    """[Lib] Event action: Pledge
    z5: Event action
    val1: Pledge type
    lot5: Item lottery ID
    flag5: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z5)
    assert PlayerIsInEventAction(z5) != 0
    """State 3: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z5) != 1 and CanGetItemLot(lot5, 1) != 1 and GetEventFlag(flag5) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot5, 1) != 1 and GetEventFlag(flag5) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_19_x39(z16=1011, lot1=lot5)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z5) != 1 and GetEventFlag(flag5) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z5) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(flag5, 1)
        AwardItem(lot5, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z5) != 1
    """State 8: End state"""
    return 0

def talk_m10_19_x33(z26=15, goods1=62130000, z23=61, val3=7, lot10=0, flag12=0):
    """[Lib] Event action: Dedication
    z26: Event action
    goods1: Special Offer: Event Item
    z23: Current pledge level: area variable
    val3: Pledge type
    lot10: Transfer: Item lottery
    flag12: Transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z26)
    assert PlayerIsInEventAction(z26) != 0
    """State 2: IventAction: Motion_Waiting"""
    if PlayerIsInEventAction(z26) != 1 and GetEventFlag(flag12) != 0:
        """State 4: Event action: votive delivery"""
        # goods:62130000:Dragon Scale
        ConsumeItem(goods1, 1)
        AddPlayerCovenantContribution(val3, 1)
        SetAreaVariable(z23, GetPlayerCovenantLevel(val3))
        SaveExecution()
    elif PlayerIsInEventAction(z26) != 1:
        """State 5: Event action: Votive delivery: Item transfer"""
        # lot:0:No Item
        AwardItem(lot10, 1)
        SetEventFlag(flag12, 1)
        # goods:62130000:Dragon Scale
        ConsumeItem(goods1, 1)
        AddPlayerCovenantContribution(val3, 1)
        SetAreaVariable(z23, GetPlayerCovenantLevel(val3))
        SaveExecution()
    """State 3: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z26) != 1
    """State 6: End state"""
    return 0

def talk_m10_19_x34(z21=6, z3=60, z22=215, flag9=102512, flag10=102513, flag11=102514):
    """[Lib] Pledge: Rank up: Conversation: 1
    z21: Pledge: Pledge type
    z3: Current rank: Area variable
    z22: Previous rank: Global variable
    flag9: Ranking 1: Item transfer: Global event flag
    flag10: Ranking 2: Item transfer: Global event flag
    flag11: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z3, GetPlayerCovenantLevel(z21))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z22) > GetAreaVariable(z3)) != 1 and (GetGlobalVariable(z22) == GetAreaVariable(z3))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z22) > GetAreaVariable(z3)) != 0 and (GetGlobalVariable(z22) == GetAreaVariable(z3))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z22, GetAreaVariable(z3))
    elif GetEventFlag(flag9) != 1 and (GetGlobalVariable(z22) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(flag10) != 1 and (GetGlobalVariable(z22) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(flag11) != 1 and (GetGlobalVariable(z22) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_19_x35(z1=61, z2=216, lot2=2008011, lot3=2008012, lot4=2008013, flag2=102831, flag3=102832,
                    flag4=102833):
    """[Lib] Menu item: Dedicated: OBJ: Pledge item award
    z1: Current pledge rank: Area variable
    z2: Last pledge rank: global variable
    lot2: Ranking 1: Item lottery
    lot3: Ranking 2: Item lottery
    lot4: Ranking 3: Item lottery
    flag2: Ranking 1: Global event flag
    flag3: Ranking 2: Global event flag
    flag4: Ranking 3: Global event flag
    """
    """State 0,3: Dedication: rank up judgment"""
    if (GetGlobalVariable(z2) > GetAreaVariable(z1)) != 1:
        """State 8: Pledge Rank Up Confirmation Dialog_SubState"""
        Label('L0')
        # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
        assert talk_m10_19_x17(action6=1308)
        """State 2: Pledge ranking judgment"""
        # lot:2008011:Dragon Head Stone
        if (GetAreaVariable(z1) > 1) != 0 and GetEventFlag(flag2) != 1 and CanGetItemLot(lot2, 1) != 1:
            """State 9: [Lib] Inventory full dialog (ranking 1) _SubState"""
            assert talk_m10_19_x39(z16=1011, lot1=lot2)
        elif (GetAreaVariable(z1) > 1) != 0 and GetEventFlag(flag2) != 1:
            """State 5: Pledge ranking 1 item acquisition dialog_SubState"""
            assert talk_m10_19_x19(lot1=lot2, flag1=flag2)
            """State 1: Pledge ranking: area variable ⇒ global variable"""
            Label('L1')
            SetGlobalVariable(z2, GetAreaVariable(z1))
        # lot:2008012:Dragon Torso Stone
        elif (GetAreaVariable(z1) > 2) != 0 and GetEventFlag(flag3) != 1 and CanGetItemLot(lot3, 1) != 1:
            """State 10: [Lib] Inventory full dialog (ranking 2) _SubState"""
            assert talk_m10_19_x39(z16=1011, lot1=lot3)
        elif (GetAreaVariable(z1) > 2) != 0 and GetEventFlag(flag3) != 1:
            """State 6: Pledge ranking 2 item acquisition dialog_SubState"""
            assert talk_m10_19_x19(lot1=lot3, flag1=flag3)
            Goto('L1')
        # lot:2008013:Black Dragon Greatsword
        elif (GetAreaVariable(z1) > 3) != 0 and GetEventFlag(flag4) != 1 and CanGetItemLot(lot4, 1) != 1:
            """State 11: [Lib] Inventory full dialog (ranking 3) _SubState"""
            assert talk_m10_19_x39(z16=1011, lot1=lot4)
        elif (GetAreaVariable(z1) > 3) != 0 and GetEventFlag(flag4) != 1:
            """State 7: Pledge ranking 3 item acquisition dialog_SubState"""
            assert talk_m10_19_x19(lot1=lot4, flag1=flag4)
            Goto('L1')
        else:
            Goto('L1')
    elif (GetGlobalVariable(z2) > 1) != 0 and GetEventFlag(flag2) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z2) > 2) != 0 and GetEventFlag(flag3) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z2) > 3) != 0 and GetEventFlag(flag4) != 1:
        Goto('L0')
    else:
        Goto('L1')
    """State 4: Pledge Ranking: End"""
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_19_x36(text8=_, z18=_, z19=9901, z20=-1):
    """[Lib] Conversation: For unique key guide
    text8: Conversation ID
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
    StartConversation(text8, GetCommonEventParamDecimal(7), z20)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z18, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_19_x37(lot1=2008000, flag1=102830):
    """[Lib] Conversation: Item transfer: Item: Key
    lot1: Item lottery
    flag1: Item transfer: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # lot:2008000:Ancient Dragon Seal
    if CanGetItemLot(lot1, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_19_x39(z16=1011, lot1=lot1)
    elif GetEventFlag(flag1) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_19_x19(lot1=lot1, flag1=flag1)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m10_19_x38(text7=_, z17=0, val2=_):
    """[Lib] Death status_ (pledge cancellation)
    text7: Conversation ID
    z17: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_19_x28(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_19_x2(text7=text7, z17=z17)
    Quit()
    """Unused"""
    """State 5: End state"""
    return 0

def talk_m10_19_x39(z16=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z16: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_19_x40():
    """Rare goods store: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    # goods:62190000:Petrified Egg
    if GetEventFlag(205300) != 0 and (ItemCount(62190000, 1, 1, 0) > 1) != 0 and GetEventFlag(102821) != 1:
        """State 5: Curio store: Dragon egg: Conversation_SubState"""
        assert talk_m10_19_x41()
    elif GetEventFlag(102821) != 0 and (GetPlayerCovenant() == 7) != 0 and GetEventFlag(102830) != 1:
        """State 9: Pledge item transfer not yet available: Insurance_SubState"""
        # lot:2008000:Ancient Dragon Seal
        assert talk_m10_19_x37(lot1=2008000, flag1=102830)
        """State 6: [Lib] Conversation: Greeting: General purpose_SubState"""
        Label('L0')
        # talk:77200200:"What? You again?", talk:77200300:"You've quite unusual taste, don't you?", talk:77200400:"Well? Where've you been?", talk:77200500:"Finally decided to come and visit?"
        assert talk_m10_19_x9(flag15=119020114, text14=77200200, text15=77200300, text16=77200400, text17=77200500)
        """State 7: Curio store: NPC menu_SubState"""
        Label('L1')
        assert talk_m10_19_x42()
    elif GetEventFlag(205300) != 0:
        Goto('L0')
    else:
        """State 4: Talk: First time: 1_SubState"""
        # talk:77200000:"What? Who're you?"
        assert talk_m10_19_x0(text14=77200000, z41=0, z42=0)
        """State 8: Talk: First time: 2_SubState"""
        # talk:77200020:"What? Have a look at my wares."
        assert talk_m10_19_x1(text1=77200020, z30=205300, z39=-1, z40=0)
        """State 3: Contact flag setting"""
        SetEventFlag(119020114, 1)
        Goto('L1')
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 10: End state"""
    return 0

def talk_m10_19_x41():
    """Curio store: Dragon egg: Conversation"""
    """State 0,1: Conversation: Start"""
    if GetEventFlag(205320) != 0:
        """State 5: If you have a dragon egg: 2nd time_SubState"""
        # talk:77208400:"Oh, change your mind?"
        assert talk_m10_19_x0(text14=77208400, z41=0, z42=0)
    else:
        """State 4: If you have a dragon egg _SubState"""
        # talk:77208100:"What is that? A petrified egg?"
        assert talk_m10_19_x0(text14=77208100, z41=205320, z42=0)
    """State 9: Egg fossil transfer selection dialog_SubState"""
    # action:1200:"Give\n%s?", goods:62190000:Petrified Egg
    call = talk_m10_19_x30(action5=1200, goods1=62190000)
    if call.Get() == 1:
        """State 7: If you have a dragon egg: NO_SubState"""
        Label('L0')
        # talk:77208300:"Oh no, no, no, no, no, don't say that.\nGive a bloke a chance."
        assert talk_m10_19_x1(text1=77208300, z30=0, z39=-1, z40=0)
    elif call.Get() == 2:
        Goto('L0')
    elif call.Get() == 0:
        """State 2: Subtract dragon eggs"""
        # goods:62190000:Petrified Egg
        ConsumeItem(62190000, 1)
        SetEventFlag(102821, 1)
        assert GetEventFlag(102821) != 0
        """State 6: If you have a dragon egg: YES_SubState"""
        # talk:77208200:"How very kind of you."
        assert talk_m10_19_x1(text1=77208200, z30=0, z39=-1, z40=0)
        """State 8: [Lib] OK dialog_SubState"""
        # action:1320:"You can now join\nthe Dragon Remnants covenant"
        assert talk_m10_19_x17(action6=1320)
    """State 3: Dragon Egg Conversation: End"""
    SetEventFlag(119020114, 1)
    """State 10: End state"""
    return 0

def talk_m10_19_x42():
    """Curio store: NPC menu"""
    """State 0: Start state"""
    while True:
        """State 1: Menu: Start"""
        if GetEventFlag(102821) != 0:
            """State 7: [Lib] Menu start: Pledge / Dedication available_SubState"""
            call = talk_m10_19_x11(z33=0, z34=220, z35=77200001, z36=0)
            if call.Get() == 2:
                """State 6: Curio store: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_19_x43()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 6:
                """State 8: [Lib] Menu item: _SubState with a pledge"""
                # lot:2008000:Ancient Dragon Seal, action:1336:"Join the Dragon Remnants covenant?", action:1346:"Abandon your covenant and\njoin the Dragon Remnants covenant?"
                call = talk_m10_19_x16(val1=7, z5=8, lot5=2008000, flag5=102830, action3=1336, action4=1346,
                                       z6=119020117)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 4:
                """State 9: [Lib] Menu item: Dedicated _SubState"""
                # goods:62130000:Dragon Scale, lot:0:No Item
                call = talk_m10_19_x18(goods1=62130000, val3=7, z23=61, z24=216, z25=15, lot10=0, flag12=0,
                                       flag13=102833)
                if call.Get() == 0:
                    """State 10: [Lib] Menu item: Dedicated: OBJ: Pledge item award_SubState"""
                    # lot:2008011:Dragon Head Stone, lot:2008012:Dragon Torso Stone, lot:2008013:Black Dragon Greatsword
                    call = talk_m10_19_x35(z1=61, z2=216, lot2=2008011, lot3=2008012, lot4=2008013, flag2=102831,
                                           flag3=102832, flag4=102833)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        break
                elif call.Get() == 1:
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 4: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:77200600:"Cheers!", talk:77200700:"Very well, no pressure."
                assert talk_m10_19_x12(text12=77200600, text13=77200700)
        else:
            """State 3: [Lib] Menu start: Pledge / No dedication_SubState"""
            call = talk_m10_19_x11(z33=0, z34=220, z35=77200000, z36=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L1')
        """State 2: Menu: Exit"""
        Label('L2')
        ClearNpcMenuSelection()
        """State 11: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:77200900:"Hey? Where you off to?"
    assert talk_m10_19_x13(text11=77200900)
    Goto('L2')

def talk_m10_19_x43():
    """Curio store: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102820) != 1 and (GetGlobalVariable(222) > 10000) != 0 and GetEventFlag(104350) != 1:
        """State 4: Equipment transfer (Conditions: Shop purchase total is above a certain level) _SubState"""
        # lot:1772000:Covetous Gold Serpent Ring+1, talk:77206000:"So...guess I'll be moving along."
        assert talk_m10_19_x20(lot8=1772000, z13=102820, text5=77206000)
    elif GetEventFlag(205313) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(205310, 0)
        SetEventFlag(205311, 0)
        SetEventFlag(205312, 0)
        SetEventFlag(205313, 0)
        """State 5: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:77201000:"I'm mainly a treasure hunter, you see.\nI'm only a merchant on the side."
        assert talk_m10_19_x1(text1=77201000, z30=205310, z39=-1, z40=0)
    elif GetEventFlag(205312) != 0:
        """State 8: Menu conversation: 4_SubState"""
        # talk:77208000:"Have you heard of the shrine\non the eastern edge of Drangleic?"
        assert talk_m10_19_x1(text1=77208000, z30=205313, z39=-1, z40=0)
    elif GetEventFlag(205311) != 0:
        """State 7: Menu conversation: 3_SubState"""
        # talk:77201800:"Hey, You know that odd fellow?\nWith the hulking blue sword."
        assert talk_m10_19_x1(text1=77201800, z30=205312, z39=-1, z40=0)
    elif GetEventFlag(205310) != 0:
        """State 6: Menu conversation: 2_SubState"""
        # talk:77201600:"There's good iron in these parts.\nAn old king even used it to build a castle."
        assert talk_m10_19_x1(text1=77201600, z30=205311, z39=-1, z40=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_19_x44():
    """Andyel: Conversation"""
    """State 0,1: Conversation start"""
    if GetEventFlag(100762) != 0 and GetEventFlag(208001) != 0:
        """State 6: [Lib] Conversation: Talk to 3_SubState"""
        # talk:69200200:"Young Hollow, seek after Vendrick."
        assert talk_m10_19_x36(text8=69200200, z18=0, z19=9901, z20=-1)
        """State 3: End encounter flag"""
        SetEventFlag(100740, 1)
    elif GetEventFlag(100762) != 0 and GetEventFlag(208000) != 0:
        """State 5: [Lib] Conversation: Talk to 2_SubState"""
        # talk:69200100:"Young Hollow, there are but two paths.\nInherit the order of this world, or destroy it."
        assert talk_m10_19_x36(text8=69200100, z18=208001, z19=9901, z20=-1)
    elif GetEventFlag(100762) != 0:
        """State 4: [Lib] Conversation: Talk to 1_SubState"""
        # talk:69200010:"No one has come this far,\nnot for a very long while."
        assert talk_m10_19_x36(text8=69200010, z18=208000, z19=9901, z20=-1)
    """State 2,7: End state"""
    return 0

def talk_m10_19_4100000():
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
            assert talk_m10_19_x44()
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

