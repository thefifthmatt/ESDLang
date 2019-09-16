# -*- coding: utf-8 -*-
def talk_m50_35_6820():
    """Underground queen"""
    """State 0: Start state"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Conversation: Start"""
        if GetEventFlag(535000083) != 0 and GetEventFlag(535020082) != 0:
            """State 4: [Lib] Conversation: 2nd and later _SubState"""
            # talk:75900410:"You...forever you shall rot... "
            assert talk_m50_35_x0(text1=75900410, z1=0, z2=35, z3=0)
        elif GetEventFlag(535020082) != 0:
            """State 3: [Lib] Conversation: Initial _SubState"""
            SetEventFlag(535000083, 1)
            # talk:75900500:"Huh! You were not deserving of the mire…"
            assert talk_m50_35_x0(text1=75900500, z1=0, z2=35, z3=0)
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m50_35_x0(text1=_, z1=0, z2=35, z3=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z1: Conversation flag
    z2: Display distance
    z3: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z2)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z1, 1)
    """State 5: Conversation: End"""
    return 0

