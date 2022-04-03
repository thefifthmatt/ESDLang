# -*- coding: utf-8 -*-
def talk_m50_36_x0(text1=75700010, z1=0, z2=30, z3=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z1: Conversation flag
    z2: Display distance
    z3: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    # talk:75700010:"no text"
    StartConversation(text1, GetCommonEventParamDecimal(7), z2)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z1, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m50_36_110000():
    """Samurai bride acquired Seoul"""
    """State 0,1: Conversation start"""
    if IsGuest() != 0:
        pass
    elif GetEventFlag(536000020) != 0:
        """State 3: [Lib] Conversation: Display only _SubState"""
        # talk:75700010:"no text"
        assert talk_m50_36_x0(text1=75700010, z1=0, z2=30, z3=0)
    """State 2: End of conversation"""
    EndMachine()
    Quit()

