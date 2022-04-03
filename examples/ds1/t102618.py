# -*- coding: utf-8 -*-
def t102618_1():
    """State 0"""
    while Loop('mainloop'):
        """State 15"""
        Label('L0')
        DebugEvent('待機')
        SetUpdateDistance(25)
        if CheckSelfDeath() == 1 and not GetEventStatus(1315) and GetDistanceToPlayer() <= 5:
            break
        elif (GetEventStatus(71600051) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf()
              <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1):
            """State 42"""
            # talk:28001400:"Oh, hello."
            TalkToPlayer(28001400, -1, -1)
            DisplayOneLineHelp(-1)
            if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
                """State 14"""
                Label('L1')
                ClearTalkProgressData()
                def ExitPause():
                    RemoveMyAggro()
                if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
                    """State 29"""
                    Label('L2')
                    # talk:28003500:"Ohh...ogghh...How could I allow this..."
                    TalkToPlayer(28003500, -1, -1)
                    DisplayOneLineHelp(-1)
                    ForceCloseMenu()
                    if HasTalkEnded() == 1:
                        continue
                    elif GetDistanceToPlayer() >= 5:
                        pass
                elif (not GetEventStatus(71600039) and IsPlayerAttacking() == 1 and GetDistanceToPlayer()
                      <= 5 and GetSelfHP() <= 90):
                    """State 7"""
                    # talk:28003400:"Sigh..."
                    TalkToPlayer(28003400, -1, -1)
                    SetEventState(71600039, 1)
                    ForceCloseMenu()
                    if CheckSelfDeath() == 1:
                        """State 30"""
                        Label('L3')
                        ClearTalkProgressData()
                        def ExitPause():
                            RemoveMyAggro()
                        assert CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5
                        break
                    elif HasTalkEnded() == 1:
                        """State 6"""
                        SetEventState(71600039, 1)
                        """State 8"""
                        Label('L4')
                        ClearTalkDisabledState()
                        RemoveMyAggro()
                        continue
                    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                          == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                          > 10):
                        pass
                elif GetEventStatus(1314) == 1:
                    """State 9"""
                    Label('L5')
                    ForceEndTalk(3)
                    Goto('L4')
                elif (not GetEventStatus(71600038) and IsPlayerAttacking() == 1 and GetDistanceToPlayer()
                      <= 5 and GetEventStatus(71600037) == 1):
                    """State 53"""
                    # talk:28003330:"Stop that!"
                    TalkToPlayer(28003330, -1, -1)
                    SetEventState(71600038, 1)
                    ForceCloseMenu()
                    if CheckSelfDeath() == 1:
                        Goto('L3')
                    elif HasTalkEnded() == 1:
                        """State 52"""
                        SetEventState(71600038, 1)
                        Goto('L4')
                    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                          == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                          > 5):
                        pass
                elif (not GetEventStatus(71600037) and IsPlayerAttacking() == 1 and GetDistanceToPlayer()
                      <= 5 and GetEventStatus(71600036) == 1):
                    """State 51"""
                    # talk:28003320:"Cease!"
                    TalkToPlayer(28003320, -1, -1)
                    SetEventState(71600037, 1)
                    ForceCloseMenu()
                    if CheckSelfDeath() == 1:
                        Goto('L3')
                    elif HasTalkEnded() == 1:
                        """State 50"""
                        SetEventState(71600037, 1)
                        Goto('L4')
                    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                          == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                          > 5):
                        pass
                elif (not GetEventStatus(71600036) and IsPlayerAttacking() == 1 and GetDistanceToPlayer()
                      <= 5 and GetEventStatus(71600035) == 1):
                    """State 49"""
                    # talk:28003310:"What are you doing!"
                    TalkToPlayer(28003310, -1, -1)
                    SetEventState(71600036, 1)
                    ForceCloseMenu()
                    if CheckSelfDeath() == 1:
                        Goto('L3')
                    elif HasTalkEnded() == 1:
                        """State 48"""
                        SetEventState(71600036, 1)
                        Goto('L4')
                    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                          == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                          > 5):
                        pass
                elif (not GetEventStatus(71600035) and IsPlayerAttacking() == 1 and GetDistanceToPlayer()
                      <= 5):
                    """State 11"""
                    # talk:28003300:"What! No!"
                    TalkToPlayer(28003300, -1, -1)
                    SetEventState(71600035, 1)
                    ForceCloseMenu()
                    if CheckSelfDeath() == 1:
                        Goto('L3')
                    elif HasTalkEnded() == 1:
                        """State 10"""
                        SetEventState(71600035, 1)
                        Goto('L4')
                    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                          == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                          > 5):
                        pass
                elif GetEventStatus(71600038) == 1:
                    Goto('L5')
                else:
                    Goto('L5')
            elif HasTalkEnded() == 1:
                """State 43"""
                SetEventState(71600052, 1)
                """State 22"""
                Label('L6')
                ClearTalkActionState()
                if True:
                    while True:
                        """State 3"""
                        # action:15000240:"Have curse broken"
                        AddTalkListData(2, 15000240, -1)
                        # action:15000010:"Purchase Item"
                        AddTalkListData(1, 15000010, -1)
                        ShowShopMessage(0, 0, 0)
                        # action:15000005:"Leave"
                        AddTalkListData(4, 15000005, -1)
                        def ExitPause():
                            ClearTalkListData()
                        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
                            """State 19"""
                            Label('L7')
                            ForceEndTalk(0)
                            ClearTalkProgressData()
                            CloseShopMessage()
                            if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
                                Goto('L2')
                            elif IsPlayerMovingACertainDistance(1) == 1:
                                """State 5"""
                                Label('L8')
                                if GetDistanceToPlayer() >= 12:
                                    pass
                                else:
                                    """State 26"""
                                    Continue('mainloop')
                            elif not IsPlayerMovingACertainDistance(1):
                                pass
                        elif not GetTalkListEntryResult():
                            break
                        elif GetTalkListEntryResult() == 1:
                            """State 2,1"""
                            OpenRegularShop(2400, 2499)
                            if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
                                """State 18"""
                                Label('L9')
                                CloseMenu()
                                if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
                                    Goto('L2')
                                elif IsPlayerMovingACertainDistance(1) == 1:
                                    Goto('L8')
                                elif not IsPlayerMovingACertainDistance(1):
                                    pass
                                else:
                                    Continue('mainloop')
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 3):
                                Goto('L9')
                            elif not IsMenuOpen(11):
                                continue
                        elif GetTalkListEntryResult() == 4:
                            break
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 3):
                            Goto('L7')
                        elif GetTalkListEntryResult() == 2:
                            """State 61"""
                            if not GetEventStatus(751):
                                """State 63"""
                                # action:10010733:"You are not cursed"
                                OpenGenericDialog(7, 10010733, 1, 0, 2)
                                DebugEvent('呪われていない')
                                DisplayOneLineHelp(-1)
                                if CheckSelfDeath() == 1:
                                    pass
                                elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                      or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                      > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() ==
                                      1):
                                    """State 65"""
                                    ForceCloseGenericDialog()
                                    ForceEndTalk(0)
                                    ClearTalkProgressData()
                                    Continue('mainloop')
                                elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                    """State 64"""
                                    Label('L10')
                                    ClearTalkDisabledState()
                                    DebugEvent('会話タイマークリア　誓約同じ')
                                    """State 13"""
                                    Label('L11')
                                    if True:
                                        continue
                                    elif GetDistanceToPlayer() >= 3:
                                        Continue('mainloop')
                                elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                    Goto('L10')
                            elif ComparePlayerStatus(10, 0, 0) == 1:
                                """State 58"""
                                # action:10010761:"No humanity"
                                OpenGenericDialog(7, 10010761, 1, 0, 2)
                                DebugEvent('人間性が足りない')
                                DisplayOneLineHelp(-1)
                                if CheckSelfDeath() == 1:
                                    pass
                                elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                      or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                      > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() ==
                                      1):
                                    """State 60"""
                                    ForceCloseGenericDialog()
                                    ForceEndTalk(0)
                                    ClearTalkProgressData()
                                    Continue('mainloop')
                                elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                    """State 59"""
                                    Label('L12')
                                    ClearTalkDisabledState()
                                    DebugEvent('会話タイマークリア　誓約同じ')
                                    Goto('L11')
                                elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                    Goto('L12')
                            else:
                                """State 57"""
                                # action:10020060:"Have curse broken in trade for humanity?"
                                OpenGenericDialog(8, 10020060, 3, 4, 2)
                                if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
                                    pass
                                elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                      or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                      > 120 or GetDistanceToPlayer() > 15):
                                    """State 54"""
                                    ForceCloseGenericDialog()
                                    ForceEndTalk(0)
                                    ClearTalkProgressData()
                                    Continue('mainloop')
                                elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                    """State 56"""
                                    Label('L13')
                                    DebugEvent('解呪しない')
                                    Goto('L11')
                                elif GetGenericDialogButtonResult() == 2 and not IsGenericDialogOpen():
                                    Goto('L13')
                                elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                    """State 55"""
                                    DebugEvent('解呪する')
                                    ChangePlayerStats(10, 1, 1)
                                    SetEventState(754, 1)
                                    Goto('L11')
                            """State 62"""
                            ForceCloseGenericDialog()
                            ForceEndTalk(0)
                            ClearTalkProgressData()
                            if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
                                Goto('L2')
                            else:
                                Continue('mainloop')
                        """State 4"""
                        ForceEndTalk(0)
                        Continue('mainloop')
                    """State 24"""
                    continue
                elif GetDistanceToPlayer() >= 3:
                    continue
            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                  == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
                pass
        elif (IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer()
              <= 2 and GetOneLineHelpStatus() == 1 and not GetEventStatus(71600051)):
            """State 38"""
            # talk:28001300:"Oh, hello."
            TalkToPlayer(28001300, -1, -1)
            DisplayOneLineHelp(-1)
            if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
                Goto('L1')
            elif HasTalkEnded() == 1:
                """State 39"""
                SetEventState(71600051, 1)
                Goto('L6')
            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                  == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
                pass
        elif (not GetOneLineHelpStatus() and HasDisableTalkPeriodElapsed() == 1 and not IsTalkingToSomeoneElse()
              and not CheckSelfDeath() and not IsCharacterDisabled() and not IsClientPlayer() and GetRelativeAngleBetweenPlayerAndSelf()
              <= 45 and GetDistanceToPlayer() <= 2 and not GetEventStatus(1314) and not GetEventStatus(1315)):
            """State 16"""
            # action:10010200:"Talk"
            DisplayOneLineHelp(10010200)
            continue
        elif (GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
              or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer()
              > 2)):
            """State 17"""
            DisplayOneLineHelp(-1)
            continue
        elif IsAttackedBySomeone() == 1 and not GetEventStatus(1315):
            """State 23"""
            DisplayOneLineHelp(-1)
            Goto('L1')
        """State 20"""
        Label('L14')
        ClearTalkProgressData()
        """State 21"""
        ForceEndTalk(0)
    """State 27"""
    # talk:28003500:"Ohh...ogghh...How could I allow this..."
    TalkToPlayer(28003500, -1, -1)
    DisplayOneLineHelp(-1)
    ForceCloseMenu()
    if HasTalkEnded() == 1 and HasTalkEnded() == 1:
        Goto('L0')
    elif GetDistanceToPlayer() >= 5:
        Goto('L14')
    """Unused"""
    """State 12"""
    # talk:28000200:"Oh, hello there. How are you?"
    TalkToPlayer(28000200, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 25"""
    # talk:28000400:"Well, hello there. Have you been cursed?"
    TalkToPlayer(28000400, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 28"""
    # talk:28000000:"Well, this is a surprise. I don't get many visitors, except for\nghosts."
    TalkToPlayer(28000000, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 31"""
    # talk:28001540:"The Four Kings slumber in the deepest chamber of the ruins."
    TalkToPlayer(28001540, -1, -1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 32"""
    # talk:28001200:"...Magnificent. You defeated the Four Kings."
    TalkToPlayer(28001200, -1, -1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 33"""
    # talk:28000500:"Hello, there. Cursed again?"
    TalkToPlayer(28000500, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 34"""
    # talk:28000300:"Hello, there. Where have you been? I'm glad to see you well."
    TalkToPlayer(28000300, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 35"""
    # talk:28000100:"Well, this is a surprise. I don't get many visitors, except\nghosts."
    TalkToPlayer(28000100, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 36"""
    # talk:28001520:"Oh, hello. You've acquired the Lordvessel, have you?"
    TalkToPlayer(28001520, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 37"""
    # talk:28001530:"Well, this is a surprise. I get few visitors, save for ghosts."
    TalkToPlayer(28001530, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 40"""
    # talk:28001000:"...You've broken the seal, have you?..."
    TalkToPlayer(28001000, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 41"""
    # talk:28001010:"...You've broken the seal, have you?..."
    TalkToPlayer(28001010, -1, -1)
    DisplayOneLineHelp(-1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 44"""
    # talk:28002000:"I am the Guardian of the Seal."
    TalkToPlayer(28002000, -1, -1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 45"""
    # talk:28002100:"New Londo was sacrificed to contain the Darkwraiths."
    TalkToPlayer(28002100, -1, -1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 46"""
    # talk:28002200:"Long ago, the Four Kings were powerful men. Only, their hearts\nwere weak."
    TalkToPlayer(28002200, -1, -1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')
    """State 47"""
    # talk:28001100:"According to legend, the knight Artorias crossed the Abyss,"
    TalkToPlayer(28001100, -1, -1)
    if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
        Goto('L1')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5):
        Goto('L14')

