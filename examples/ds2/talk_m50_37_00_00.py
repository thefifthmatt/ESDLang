# -*- coding: utf-8 -*-
def talk_m50_37_x0(text2=_, z12=_, z13=_, z14=0):
    """[Lib] Conversation: Display only
    text2: Conversation ID
    z12: Conversation flag
    z13: Display distance
    z14: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text2, GetCommonEventParamDecimal(7), z13)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z12, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m50_37_x1(lot1=_, flag1=_):
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

def talk_m50_37_x2(lot3=1788000, flag3=0, z4=207630, z5=0, z10=0, z11=0):
    """[Lib] Item acquisition dialog: Conversation
    lot3: Item lottery ID
    flag3: Item transfer: Global event flag
    z4: Conversation: Global conversation flag
    z5: Trophy acquisition: Area and other flags
    z10: Emigration permission: Global event flag
    z11: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z11, 1)
    SetEventFlag(z10, 1)
    SetEventFlag(z5, 1)
    SetEventFlag(z4, 1)
    SetEventFlag(flag3, 1)
    # lot:1788000:Loyce Gauntlets
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m50_37_x3(text3=_, z7=_, z8=_, z9=50):
    """[Lib] Conversation: For unique key guide
    text3: Conversation ID
    z7: Conversation flag
    z8: Key guide parameters
    z9: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z8)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text3, GetCommonEventParamDecimal(7), z9)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z7, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m50_37_x4(z6=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z6: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m50_37_x5(lot3=1788000, flag3=0, text2=75810330, z4=207630, z5=0, goods1=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item: Important items
    lot3: Item lottery ID
    flag3: Item transfer: Global event flag
    text2: Conversation ID
    z4: Conversation: Global conversation flag
    z5: Trophy acquisition: Area and other flags
    goods1: Important items
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m50_37_x0(text2=text2, z12=0, z13=-1, z14=0)
    if call.Done() and GetEventFlag(flag3) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z4, 1)
    elif call.Done() and (ItemCount(goods1, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # lot:1788000:Loyce Gauntlets
    elif call.Done() and CanGetItemLot(lot3, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m50_37_x4(z6=1011, lot1=lot3)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m50_37_x2(lot3=lot3, flag3=flag3, z4=z4, z5=z5, z10=0, z11=0)
    """State 6: End state"""
    return 0

def talk_m50_37_x6(lot2=1788030, flag2=103303):
    """[Lib] Conversation: Item transfer: Item: NOKey
    lot2: Item lottery
    flag2: Item transfer: Global event flag
    """
    """State 0,1: Conversation: Start"""
    # lot:1788030:Soul of Alsanna, Silent Oracle
    if CanGetItemLot(lot2, 1) != 1:
        """State 3: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m50_37_x4(z6=1011, lot1=lot2)
    elif GetEventFlag(flag2) != 1:
        """State 2: [Lib] Item acquisition dialog_SubState"""
        assert talk_m50_37_x1(lot1=lot2, flag1=flag2)
    else:
        pass
    """State 4: Conversation: End"""
    return 0

def talk_m50_37_x7():
    """White priestess"""
    """State 0,1: Conversation: Start"""
    if GetEventFlag(103303) != 0:
        """State 31: [Lib] Conversation: 4 repeats of knight souls_SubState"""
        # talk:75810396:"Go on, kind visitor."
        assert talk_m50_37_x3(text3=75810396, z7=0, z8=50389010, z9=50)
    elif GetEventFlag(207690) != 0:
        """State 34: [Lib] Conversation: Conversation before Item Transfer 4_SubState"""
        # talk:75810390:"Kind visitor."
        assert talk_m50_37_x3(text3=75810390, z7=207700, z8=50379001, z9=50)
        """State 33: [Lib] Conversation: Item transfer 4_SubState"""
        # lot:1788030:Soul of Alsanna, Silent Oracle
        call = talk_m50_37_x6(lot2=1788030, flag2=103303)
        if call.Done() and GetEventFlag(103303) != 0:
            """State 7: Shop addition flag"""
            SetEventFlag(101220, 1)
        elif call.Done():
            pass
    # goods:64600000:Loyce Soul
    elif (ItemCount(64600000, 1, 1, 1) > 50) != 0 and GetEventFlag(103302) != 0:
        """State 30: [Lib] Conversation: 4_SubState collecting knight souls"""
        # talk:75810500:"I sense a knight's joyous elation."
        assert talk_m50_37_x3(text3=75810500, z7=207690, z8=50379000, z9=50)
        """State 9: Ice seal state change 4"""
        SetEventFlag(537000153, 1)
    elif GetEventFlag(207680) != 0:
        """State 29: [Lib] Conversation: 3 repeats of knight souls_SubState"""
        # talk:75810383:"...man is no different."
        assert talk_m50_37_x3(text3=75810383, z7=0, z8=50379000, z9=50)
    elif GetEventFlag(103302) != 0:
        """State 28: [Lib] Conversation: 3_2_SubState collecting knight souls"""
        # talk:75810380:"My Father, once human, succumbed to Dark..."
        assert talk_m50_37_x3(text3=75810380, z7=207680, z8=50379000, z9=50)
    # goods:64600000:Loyce Soul
    elif (ItemCount(64600000, 1, 1, 1) > 35) != 0 and GetEventFlag(103301) != 0:
        """State 27: [Lib] Conversation: 3_1_SubState collecting knight souls"""
        # talk:75810370:"I sense a knight's joyous elation."
        assert talk_m50_37_x3(text3=75810370, z7=207670, z8=50379000, z9=50)
        """State 6: Ice seal state change 3"""
        SetEventFlag(537000152, 1)
        """State 37: Conversation: Item Transfer: White Miko: Item Transfer 3_SubState"""
        # lot:1788020:Loyce Helm
        assert talk_m50_37_x8(lot1=1788020, flag1=103302)
    elif GetEventFlag(207660) != 0:
        """State 26: [Lib] Conversation: 2 repeats of knight souls_SubState"""
        # talk:75810365:"One day, you may encounter another.\nAnother being, born of Dark."
        assert talk_m50_37_x3(text3=75810365, z7=0, z8=50379000, z9=50)
    elif GetEventFlag(103301) != 0:
        """State 25: [Lib] Conversation: 2_2_SubState collecting knight souls"""
        # talk:75810360:"The beings born from shards of Dark..."
        assert talk_m50_37_x3(text3=75810360, z7=207660, z8=50379000, z9=50)
    # goods:64600000:Loyce Soul
    elif (ItemCount(64600000, 1, 1, 1) > 15) != 0 and GetEventFlag(103300) != 0:
        """State 24: [Lib] Conversation: 2_1_SubState collecting knight souls"""
        # talk:75810350:"I sense a knight's joyous elation."
        assert talk_m50_37_x3(text3=75810350, z7=207650, z8=50379000, z9=50)
        """State 5: Ice seal state change 2"""
        SetEventFlag(537000151, 1)
        """State 36: Conversation: Item Transfer: White Miko: Item Transfer 2_SubState"""
        # lot:1788010:Loyce Armor
        assert talk_m50_37_x8(lot1=1788010, flag1=103301)
    elif GetEventFlag(207640) != 0:
        """State 23: [Lib] Conversation: 1 repeat of knight's souls_SubState"""
        # talk:75810342:"For my dear Lord, and his loyal knights."
        assert talk_m50_37_x3(text3=75810342, z7=0, z8=50379000, z9=50)
    elif GetEventFlag(103300) != 0:
        """State 22: [Lib] Conversation: 1_2_SubState collecting knight souls"""
        # talk:75810340:"My dear Lord has departed."
        assert talk_m50_37_x3(text3=75810340, z7=207640, z8=50379000, z9=50)
    # goods:64600000:Loyce Soul
    elif (ItemCount(64600000, 1, 1, 1) > 5) != 0 and GetEventFlag(207620) != 0:
        """State 21: [Lib] Conversation: 1_1_SubState collecting knight souls"""
        # talk:75810330:"I sense a knight's joyous elation."
        assert talk_m50_37_x3(text3=75810330, z7=207630, z8=50379000, z9=50)
        """State 4: Ice seal state change 1"""
        SetEventFlag(537000150, 1)
        """State 35: Conversation: Item Transfer: White Miko: Item Transfer 1_SubState"""
        # lot:1788000:Loyce Gauntlets
        assert talk_m50_37_x8(lot1=1788000, flag1=103300)
    elif GetEventFlag(207610) != 0 and GetEventFlag(101070) != 0:
        """State 17: [Lib] Conversation: Repeat after defeating the boss_SubState"""
        # talk:75810320:"The knights of Eleum Loyce\nwere swallowed by the Chaos..."
        assert talk_m50_37_x3(text3=75810320, z7=207620, z8=50379000, z9=50)
    elif GetEventFlag(101070) != 0:
        """State 15: [Lib] Conversation: 6_SubState talking"""
        # talk:75810300:"You've granted my one wish..."
        assert talk_m50_37_x3(text3=75810300, z7=207610, z8=50379000, z9=50)
    elif GetEventFlag(537000020) != 0 and GetEventFlag(537000021) != 0 and GetEventFlag(537000022) != 0:
        """State 38: [Lib] Conversation: Repeat 2_SubState"""
        # talk:75810200:"Many of Eleum Loyce's faithful knights\nfollowed their Lord into the Chaos."
        assert talk_m50_37_x3(text3=75810200, z7=207601, z8=50379000, z9=50)
    elif GetEventFlag(207580) != 0:
        """State 16: [Lib] Conversation: Repeat 1_SubState"""
        # talk:75810210:"Many of Eleum Loyce's faithful knights\nfollowed their Lord into the Chaos."
        assert talk_m50_37_x3(text3=75810210, z7=207600, z8=50379000, z9=50)
    elif GetEventFlag(207590) != 0:
        """State 18: [Lib] Conversation: After NO_SubState"""
        # talk:75810190:"Stranger."
        assert talk_m50_37_x3(text3=75810190, z7=0, z8=50379000, z9=50)
        """State 3: YN dialog"""
        Label('L0')
        # action:1220:"What is your choice?"
        DisplayOwnYesNoMenu(1220, 50, -1, 0, 0, 0)
        if (YesNoMenuResult() == 1) != 0:
            """State 19: [Lib] Conversation: YES selection_SubState"""
            # talk:75810170:"Kind visitor, I thank you."
            assert talk_m50_37_x0(text2=75810170, z12=207580, z13=50, z14=0)
            """State 8: Unsealing"""
            SetEventFlag(537000011, 1)
            SetEventFlag(537000001, 1)
            assert GetEventFlag(537020007) != 0
            """State 39: [Lib] Conversation: Repeat 1 display only_SubState"""
            # talk:75810210:"Many of Eleum Loyce's faithful knights\nfollowed their Lord into the Chaos."
            assert talk_m50_37_x0(text2=75810210, z12=0, z13=50, z14=0)
        elif (YesNoMenuResult() == 2) != 0:
            """State 20: [Lib] Conversation: NO selection_SubState"""
            Label('L1')
            # talk:75810180:"Then be gone."
            assert talk_m50_37_x0(text2=75810180, z12=207590, z13=50, z14=0)
        elif YesNoMenuDisplay() != 1:
            Goto('L1')
    elif GetEventFlag(207560) != 0:
        """State 14: [Lib] Conversation: Talk to 5_SubState"""
        # talk:75810160:"I have but one wish."
        assert talk_m50_37_x3(text3=75810160, z7=207570, z8=50379000, z9=50)
        Goto('L0')
    elif GetEventFlag(207550) != 0:
        """State 13: [Lib] Conversation: 4_SubState talking"""
        # talk:75810150:"Inevitably, the King was drained of vigour,\nand plunged into the Chaos' heart."
        assert talk_m50_37_x3(text3=75810150, z7=207560, z8=50379000, z9=50)
    elif GetEventFlag(207540) != 0:
        """State 12: [Lib] Conversation: 3_SubState talking"""
        # talk:75810140:"My dear lord, a most true king."
        assert talk_m50_37_x3(text3=75810140, z7=207550, z8=50379000, z9=50)
    elif GetEventFlag(207530) != 0:
        """State 11: [Lib] Conversation: 2_SubState talking"""
        # talk:75810130:"This land is barren,"
        assert talk_m50_37_x3(text3=75810130, z7=207540, z8=50379000, z9=50)
    elif GetEventFlag(207530) != 1:
        """State 10: [Lib] Conversation: 1_A_SubState to speak"""
        # talk:75810110:"To think Aava could be bested..."
        assert talk_m50_37_x3(text3=75810110, z7=207530, z8=50379000, z9=50)
    """State 2: Conversation: End"""
    Label('L2')
    """State 40: End state"""
    return 0
    """Unused"""
    """State 32: [Lib] Conversation: Item transfer: 1_1_SubState collecting knight souls"""
    # lot:1788000:Loyce Gauntlets, talk:75810330:"I sense a knight's joyous elation."
    assert talk_m50_37_x5(lot3=1788000, flag3=0, text2=75810330, z4=207630, z5=0, goods1=0)
    Goto('L2')

def talk_m50_37_x8(lot1=_, flag1=_):
    """Conversation: Item Transfer: White Miko: Item: NOKey
    lot1: Item lottery
    flag1: Item transfer: Global event flag
    """
    """State 0,1: Conversation: Start"""
    if CanGetItemLot(lot1, 1) != 1:
        """State 4: Inventory full dialog: White Miko _SubState"""
        assert talk_m50_37_x9(z3=1011, lot1=lot1)
    elif GetEventFlag(flag1) != 1:
        """State 2: [Lib] Item acquisition dialog_SubState"""
        assert talk_m50_37_x1(lot1=lot1, flag1=flag1)
    else:
        pass
    """State 5: Conversation: End"""
    Label('L0')
    return 0
    """Unused"""
    """State 3: [Lib] Inventory full dialog: Item display_SubState"""
    assert talk_m50_37_x4(z6=1011, lot1=lot1)
    Goto('L0')

def talk_m50_37_x9(z3=1011, lot1=_):
    """Inventory full dialog: White Miko
    z3: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 40, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m50_37_x10(text1=75815020, z1=103310):
    """Death status: white priestess
    text1: Conversation ID
    z1: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Death Message: White Miko _SubState"""
    talk_m50_37_x11(text1=text1, z2=207700)
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def talk_m50_37_x11(text1=75815020, z2=207700):
    """Conversation: Death Message: White Miko
    text1: Conversation ID
    z2: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    # talk:75815020:"Oh...my dear Lord..."
    StartConversation(text1, GetCommonEventParamDecimal(7), 50)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z2, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m50_37_110000():
    """White Miko: Warning ①"""
    """State 0: Start state"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Conversation: Start"""
        assert GetEventFlag(207500) != 1 and GetEventFlag(537020016) != 0
        """State 3: [Lib] Conversation: Initial _SubState"""
        # talk:75810010:"You, approaching Eleum Loyce,"
        assert talk_m50_37_x0(text2=75810010, z12=207500, z13=100, z14=0)
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

def talk_m50_37_110010():
    """White Miko: Warning ②"""
    """State 0: Start state"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Conversation: Start"""
        if PlayerInPoint(20000010) != 0 and GetEventFlag(207510) != 1:
            """State 3: [Lib] Conversation: Initial _SubState"""
            # talk:75810030:"Go back."
            assert talk_m50_37_x0(text2=75810030, z12=207510, z13=100, z14=0)
        elif GetEventFlag(101071) != 0:
            pass
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

def talk_m50_37_110011():
    """White Miko: Warning ②_1"""
    """State 0: Start state"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Conversation: Start"""
        if (GetEventFlag(101071) != 1 and GetEventFlag(537000012) != 1 and GetEventFlag(537020080) !=
            1 and GetEventFlag(207511) != 1 and PlayerInPoint(2500000) != 0):
            """State 3: Wait"""
            SetEventFlag(537020017, 1)
            assert (GetStateTime() > 3) != 0
            """State 4: [Lib] Conversation: Initial _SubState"""
            # talk:75810040:"Poor Aava, do you miss your king?"
            assert talk_m50_37_x0(text2=75810040, z12=207511, z13=100, z14=0)
        elif GetEventFlag(101071) != 0:
            pass
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

def talk_m50_37_110020():
    """White Miko: Warning ③"""
    """State 0: Start state"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Conversation: Start"""
        if PlayerInPoint(20000020) != 0 and GetEventFlag(207520) != 1:
            """State 3: [Lib] Conversation: Initial _SubState"""
            # talk:75810050:"Turn away."
            assert talk_m50_37_x0(text2=75810050, z12=207520, z13=100, z14=0)
        elif GetEventFlag(101071) != 0:
            pass
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

def talk_m50_37_110021():
    """White Miko: Warning ④"""
    """State 0: Start state"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Conversation: Start"""
        if GetEventFlag(207521) != 1 and GetEventFlag(537000012) != 0 and PlayerInPoint(2500000) != 0:
            """State 3: Wait"""
            SetEventFlag(537020017, 1)
            assert (GetStateTime() > 3) != 0
            """State 4: [Lib] Conversation: Initial _SubState"""
            # talk:75810013:"This dead city has nothing to offer."
            assert talk_m50_37_x0(text2=75810013, z12=207521, z13=100, z14=0)
        elif GetEventFlag(101071) != 0:
            pass
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

def talk_m50_37_110030():
    """White Miko: Conversation"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            while True:
                """State 5: White shrine maiden_SubState"""
                call = talk_m50_37_x7()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    """State 4: Flag setting"""
                    SetEventFlag(537000011, 1)
                    SetEventFlag(537000001, 1)
                    SetEventFlag(537000150, 1)
                    SetEventFlag(537000151, 1)
                    SetEventFlag(537000152, 1)
                    SetEventFlag(537000153, 1)
                    SetEventFlag(101220, 1)
                    """State 6: Death state: white priest _SubState"""
                    # talk:75815020:"Oh...my dear Lord..."
                    assert talk_m50_37_x10(text1=75815020, z1=103310)
                    Break('mainloop')
                elif (NumberOfTimesDamaged(0) > 1) != 0:
                    """State 3: Attacked: White Miko"""
                    ResetDamageTakenCount()
                    CancelConversation()
    """State 2: Conversation: System termination"""
    EndMachine()
    Quit()

