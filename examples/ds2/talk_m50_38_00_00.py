# -*- coding: utf-8 -*-
def talk_m50_38_6840():
    """Van Clad (birthday)"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            pass
        elif GetEventFlag(103980) != 0:
            break
        else:
            """State 10: Van Clad (birthday): Conversation_SubState"""
            call = talk_m50_38_x5()
            if call.Done() and GetEventFlag(103200) != 0:
                """State 11: [Lib] Conversation: Display only _SubState"""
                Label('L0')
                # talk:51300130:"Foolish..."
                assert talk_m50_38_x0(text2=51300130, z8=0, z9=-1, z10=0)
                """State 2: Hostility: Set damage flag"""
                AddAreaVariable(63, 1)
            elif call.Done():
                continue
            elif (NumberOfTimesDamaged(1) > 1) != 0:
                Goto('L0')
            # goods:25130100:King's Crown
            elif GetEventFlag(538020011) != 0 and (not ItemCount(25130100, 1, 1, 0)) != 0:
                """State 6: King crown check"""
                SetEventFlag(538020011, 0)
                SetAreaVariable(1, 0)
                SetEventFlag(538020010, 0)
                continue
            # goods:21650100:Crown of the Sunken King
            elif GetEventFlag(538020012) != 0 and (not ItemCount(21650100, 1, 1, 0)) != 0:
                """State 7: Underground crown check"""
                SetEventFlag(538020012, 0)
                SetAreaVariable(1, 0)
                SetEventFlag(538020010, 0)
                continue
            # goods:21630100:Crown of the Old Iron King
            elif GetEventFlag(538020013) != 0 and (not ItemCount(21630100, 1, 1, 0)) != 0:
                """State 8: Ash crown check"""
                SetEventFlag(538020013, 0)
                SetAreaVariable(1, 0)
                SetEventFlag(538020010, 0)
                continue
            # goods:21640100:Crown of the Ivory King
            elif GetEventFlag(538020014) != 0 and (not ItemCount(21640100, 1, 1, 0)) != 0:
                """State 9: Ice crown check"""
                SetEventFlag(538020014, 0)
                SetAreaVariable(1, 0)
                SetEventFlag(538020010, 0)
                continue
        """State 4: Conversation: System: End"""
        Label('L1')
        EndMachine()
        Quit()
    """State 3: Hostility: Set flag"""
    DeleteKeyGuideArea()
    SetEventFlag(103980, 1)
    SetEventFlag(103999, 1)
    SaveExecution()
    assert GetEventFlag(103980) != 0
    Goto('L1')

def talk_m50_38_6841():
    """Crown number check"""
    """State 0,1: Check number of possessions"""
    # goods:25130100:King's Crown
    if (ItemCount(25130100, 1, 1, 0) > 1) != 0:
        """State 2: Possession of the crown of the king"""
        SetEventFlag(538020011, 1)
        # goods:21650100:Crown of the Sunken King
        if (ItemCount(21650100, 1, 1, 0) > 1) != 0 and GetEventFlag(101051) != 0:
            """State 4: Underground crown possession"""
            Label('L0')
            SetEventFlag(538020012, 1)
            # goods:21630100:Crown of the Old Iron King
            if (ItemCount(21630100, 1, 1, 0) > 1) != 0 and GetEventFlag(101061) != 0:
                """State 6: Possession of ash crown"""
                Label('L1')
                SetEventFlag(538020013, 1)
                # goods:21640100:Crown of the Ivory King
                if (ItemCount(21640100, 1, 1, 0) > 1) != 0 and GetEventFlag(101070) != 0:
                    """State 8: Possession of a crown of ice"""
                    Label('L2')
                    SetEventFlag(538020014, 1)
                else:
                    """State 9: No possession of ice crown"""
                    Label('L3')
            else:
                """State 7: No possession of ash crown"""
                Label('L4')
                # goods:21640100:Crown of the Ivory King
                if (ItemCount(21640100, 1, 1, 0) > 1) != 0 and GetEventFlag(101070) != 0:
                    Goto('L2')
                else:
                    Goto('L3')
        else:
            """State 5: No underground crown possession"""
            Label('L5')
            # goods:21630100:Crown of the Old Iron King
            if (ItemCount(21630100, 1, 1, 0) > 1) != 0 and GetEventFlag(101061) != 0:
                Goto('L1')
            else:
                Goto('L4')
    # goods:25130100:King's Crown
    elif (ItemCount(25130100, 1, 1, 0) > 1) != 1:
        """State 3: No crown possession"""
        # goods:21650100:Crown of the Sunken King
        if (ItemCount(21650100, 1, 1, 0) > 1) != 0 and GetEventFlag(101051) != 0:
            Goto('L0')
        else:
            Goto('L5')
    """State 10: Conversation: System: End"""
    EndMachine()

def talk_m50_38_x0(text2=_, z8=0, z9=_, z10=0):
    """[Lib] Conversation: Display only
    text2: Conversation ID
    z8: Conversation flag
    z9: Display distance
    z10: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text2, GetCommonEventParamDecimal(7), z9)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z8, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m50_38_x1(action1=1011):
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

def talk_m50_38_x2(lot1=1787000, z7=103140):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    z7: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z7, 1)
    # lot:1787000:Ashen Mist Heart
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m50_38_x3(text2=51300120, text3=51300127, z4=538010110, z5=0, z6=0):
    """[Lib] Conversation: Poly Play: Mes⇒Poly⇒Mes
    text2: First half conversation: conversation ID
    text3: Second half conversation: conversation ID
    z4: Poly drama play start: area and other flags
    z5: Global event flag 1
    z6: Global event flag 2
    """
    """State 0,4: Poly play: First half: Message_SubState"""
    assert talk_m50_38_x0(text2=text2, z8=0, z9=-1, z10=0)
    """State 1: Conversation: Poly play"""
    SetEventFlag(z4, 1)
    assert GetEventFlag(z4) != 0
    """State 2: Conversation: Poly drama playback standby"""
    assert GetEventFlag(z4) != 1
    """State 3: Conversation: Global event flag setting"""
    SetEventFlag(z5, 1)
    SetEventFlag(z6, 1)
    """State 5: Poly play: Second half: Message_SubState"""
    assert talk_m50_38_x0(text2=text3, z8=0, z9=-1, z10=0)
    """State 6: End state"""
    return 0

def talk_m50_38_x4(text1=_, z1=_, z2=50389010, z3=20):
    """[Lib] Conversation: For unique key guide
    text1: Conversation ID
    z1: Conversation flag
    z2: Key guide parameters
    z3: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z2)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text1, GetCommonEventParamDecimal(7), z3)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z1, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m50_38_x5():
    """Van Clad (Life): Conversation"""
    """State 0: Start state"""
    if (GetAreaVariable(63) > 1) != 0:
        pass
    elif GetEventFlag(538020010) != 0:
        """State 1: Conversation: Start"""
        Label('L0')
        if GetEventFlag(207040) != 0 and (GetAreaVariable(1) > 4) != 0:
            """State 35: [Lib] Conversation: Vanclad conversation only: possessing 4 crowns 1_SubState"""
            # talk:51300120:"One day, fire will fade,\nand Dark will become a curse."
            assert talk_m50_38_x4(text1=51300120, z1=207050, z2=50389010, z3=20)
            """State 16: Conversation: Poly play"""
            SetEventFlag(538010110, 1)
            assert GetEventFlag(538010110) != 0
            """State 17: Conversation: Poly drama playback standby"""
            assert GetEventFlag(538010110) != 1
            """State 18: No deaths flag"""
            SetEventFlag(100730, 1)
            SetEventFlag(100731, 1)
            SetEventFlag(103201, 1)
            assert GetEventFlag(100730) != 0
            """State 19: Wait ①"""
            assert (GetStateTime() > 1.5) != 0
            """State 37: [Lib] Conversation: Van Clad Conversation: Four Crowns 1_1: Display only_SubState"""
            # talk:51300127:"The rest will follow..."
            assert talk_m50_38_x0(text2=51300127, z8=0, z9=20, z10=0)
            """State 20: Wait ②"""
            assert (GetStateTime() > 1.5) != 0
            """State 13: Forced return flag"""
            SetEventFlag(103200, 1)
            Quit()
        elif GetEventFlag(207041) != 0:
            """State 34: [Lib] Conversation: Vanclad conversation only: 3 crown possession 3_SubState"""
            # talk:51300110:"Dark was seen as a curse."
            assert talk_m50_38_x4(text1=51300110, z1=0, z2=50389010, z3=20)
        elif GetEventFlag(207040) != 0:
            """State 33: [Lib] Conversation: Vanclad conversation only: 3 crown possession 2_SubState"""
            # talk:51300100:"Fire came to be,\nand with it, Disparity."
            assert talk_m50_38_x4(text1=51300100, z1=207041, z2=50389010, z3=20)
        elif GetEventFlag(207030) != 0 and (GetAreaVariable(1) > 3) != 0:
            """State 32: [Lib] Conversation: Vanclad conversation only: 3 crown possession 1_SubState"""
            # talk:51300090:"Seeker of fire, I see you've\nsubdued another foul creature."
            assert talk_m50_38_x4(text1=51300090, z1=207040, z2=50389010, z3=20)
        elif GetEventFlag(207031) != 0:
            """State 31: [Lib] Conversation: Vanclad Conversation only: 2 crown possession 3_SubState"""
            # talk:51300080:"Drangleic will fall, the fire will fade,\nand the souls of old will reemerge."
            assert talk_m50_38_x4(text1=51300080, z1=0, z2=50389010, z3=20)
        elif GetEventFlag(207030) != 0:
            """State 30: [Lib] Conversation: Van Clad Conversation Only: 2 Crowns 2_SubState"""
            # talk:51300070:"I am king of this\nwretched, unravelled kingdom."
            assert talk_m50_38_x4(text1=51300070, z1=207031, z2=50389010, z3=20)
        elif GetEventFlag(207020) != 0 and (GetAreaVariable(1) > 2) != 0:
            """State 29: [Lib] Conversation: Vanclad conversation only: 2 crown possession 1_SubState"""
            # talk:51300060:"Seeker of fire,\nconqueror of Dark."
            assert talk_m50_38_x4(text1=51300060, z1=207030, z2=50389010, z3=20)
        elif GetEventFlag(207021) != 0:
            """State 28: [Lib] Conversation: Vanclad conversation only: possessing one crown 3_SubState"""
            # talk:51300050:"I fail to see your design,\nyoung moth."
            assert talk_m50_38_x4(text1=51300050, z1=0, z2=50389010, z3=20)
        elif GetEventFlag(207020) != 0:
            """State 27: [Lib] Conversation: Vanclad conversation only: 1 crown possession 2_SubState"""
            # talk:51300040:"I am no king. \nI am more fit to be a jester... "
            assert talk_m50_38_x4(text1=51300040, z1=207021, z2=50389010, z3=20)
        elif GetEventFlag(207000) != 0 and (GetAreaVariable(1) > 1) != 0:
            """State 26: [Lib] Conversation: Van Clad Conversation: One crown possession 1_SubState"""
            # talk:51300030:"Seeker of fire,\ndeliverer of crowns."
            assert talk_m50_38_x4(text1=51300030, z1=207020, z2=50389010, z3=20)
        elif GetEventFlag(207010) != 0:
            """State 25: [Lib] Conversation: Vanclad Conversation Only: Non-owned 2_SubState"""
            # talk:51200025:"And your wishes, granted."
            assert talk_m50_38_x4(text1=51200025, z1=0, z2=50389010, z3=20)
        elif GetEventFlag(207000) != 0:
            """State 24: [Lib] Conversation: Vanclad Conversation Only: Non-owned 1_SubState"""
            # talk:51200020:"As flame rises, so does it fade.\nSuch is the way of things."
            assert talk_m50_38_x4(text1=51200020, z1=207010, z2=50389010, z3=20)
        else:
            """State 22: [Lib] Conversation: Dedicated to Van Clad Conversation _SubState"""
            SetEventFlag(100500, 1)
            # talk:51300010:"Seeker of fire,\ncoveter of the throne."
            assert (talk_m50_38_x4(text1=51300010, z1=207000, z2=50389010, z3=20) and GetEventFlag(100500)
                    != 0)
    else:
        """State 3: Check number of possessions"""
        # goods:25130100:King's Crown
        if (ItemCount(25130100, 1, 1, 0) > 1) != 0:
            """State 4: Possession of the crown of the king"""
            AddAreaVariable(1, 1)
            # goods:21650100:Crown of the Sunken King
            if (ItemCount(21650100, 1, 1, 0) > 1) != 0 and GetEventFlag(101051) != 0:
                """State 6: Underground crown possession"""
                Label('L1')
                AddAreaVariable(1, 1)
                # goods:21630100:Crown of the Old Iron King
                if (ItemCount(21630100, 1, 1, 0) > 1) != 0 and GetEventFlag(101061) != 0:
                    """State 9: Possession of ash crown"""
                    Label('L2')
                    AddAreaVariable(1, 1)
                    # goods:21640100:Crown of the Ivory King
                    if (ItemCount(21640100, 1, 1, 0) > 1) != 0 and GetEventFlag(101070) != 0:
                        """State 11: Possession of a crown of ice"""
                        Label('L3')
                        AddAreaVariable(1, 1)
                    else:
                        """State 12: No possession of ice crown"""
                        Label('L4')
                else:
                    """State 10: No possession of ash crown"""
                    Label('L5')
                    # goods:21640100:Crown of the Ivory King
                    if (ItemCount(21640100, 1, 1, 0) > 1) != 0 and GetEventFlag(101070) != 0:
                        Goto('L3')
                    else:
                        Goto('L4')
            else:
                """State 7: No underground crown possession"""
                Label('L6')
                # goods:21630100:Crown of the Old Iron King
                if (ItemCount(21630100, 1, 1, 0) > 1) != 0 and GetEventFlag(101061) != 0:
                    Goto('L2')
                else:
                    Goto('L5')
        # goods:25130100:King's Crown
        elif (ItemCount(25130100, 1, 1, 0) > 1) != 1:
            """State 5: No crown possession"""
            # goods:21650100:Crown of the Sunken King
            if (ItemCount(21650100, 1, 1, 0) > 1) != 0 and GetEventFlag(101051) != 0:
                Goto('L1')
            else:
                Goto('L6')
        """State 8: Crown number check flag"""
        SetEventFlag(538020010, 1)
        Goto('L0')
    """State 2,38: End state"""
    return 0

