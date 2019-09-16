# -*- coding: utf-8 -*-
def event_m10_02_1000():
    """Text stele_01"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3500:"Bonfires are places of respite\nYou may also light torches on them"
    assert event_m10_02_x34(z40=10021101, action3=3500)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1010():
    """Text stele_02"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3501:"Light sconces with a torch"
    assert event_m10_02_x34(z40=10021102, action3=3501)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1020():
    """Text stone monument_03"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3003:"⑦： Attack (R weapon)"
    assert event_m10_02_x34(z40=10021103, action3=3003)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1040():
    """Text stele_05"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3007:"⑪： Target Lock/Release\n⑰ While target locked： Change Target"
    assert event_m10_02_x34(z40=10021105, action3=3007)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1050():
    """Text stele_06"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3001:"⑱ + Hold ⑳： Dash"
    assert event_m10_02_x34(z40=10021106, action3=3001)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1070():
    """Text stele_08"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3058:"⑦ Behind enemy's back： Critical Hit"
    assert event_m10_02_x34(z40=10021108, action3=3058)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1080():
    """Text stele _09"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3014:"⑱ + ⑳： Roll"
    assert event_m10_02_x34(z40=10021109, action3=3014)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1090():
    """Text stele_010"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3012:"㊧㊨： Switch equipped weapon"
    assert event_m10_02_x34(z40=10021110, action3=3012)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1100():
    """Text stone monument_011"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3013:"⑳： Backstep"
    assert event_m10_02_x34(z40=10021111, action3=3013)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1110():
    """Text stone monument_012"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3016:"②： Use Item"
    assert event_m10_02_x34(z40=10021112, action3=3016)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1120():
    """Text stone monument_013"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3002:"⑰： Move camera"
    assert event_m10_02_x34(z40=10021113, action3=3002)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1130():
    """Text stone monument_014"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3018:"Hold ①： Wield left weapon two-handed"
    assert event_m10_02_x34(z40=10021114, action3=3018)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1140():
    """Text stele_015"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3017:"①： Wield right weapon two-handed"
    assert event_m10_02_x34(z40=10021115, action3=3017)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1150():
    """Text stone monument_016"""
    """State 0,2: [Preset] Text Stele_Dash Jump_SubState"""
    # action:3015:"⑫ While dashing： Dashing Jump", action:3020:"⑳ While dashing： Dashing Jump"
    assert event_m10_02_x66(z17=10021116, action1=3015, action2=3020)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1160():
    """Text stone monument_017"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3050:"⑱＋⑦/⑨： Guard Break"
    assert event_m10_02_x34(z40=10021117, action3=3050)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1170():
    """Text stone monument_018"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3060:"⑩/⑧ With shield equipped： Parry (repel enemy's attack)"
    assert event_m10_02_x34(z40=10021118, action3=3060)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1180():
    """Text stone monument_019"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3057:"⑦/⑨ While falling： Plunging Attack"
    assert event_m10_02_x34(z40=10021119, action3=3057)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1190():
    """Text stone monument_020"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3052:"⑱ + ⑧/⑩： Jumping Attack"
    assert event_m10_02_x34(z40=10021120, action3=3052)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_1200():
    """Text stone monument_021"""
    """State 0,2: [Preset] Text Stone Monument_SubState"""
    # action:3502:"Search your surroundings"
    assert event_m10_02_x34(z40=10021121, action3=3502)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_2000():
    """Falling tree 1"""
    """State 0,2: [Lib] [Preset] Falling tree _SubState"""
    assert event_m10_02_x12(z61=10021200, z62=200000)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_2010():
    """Falling tree 2"""
    """State 0,2: [Lib] [Preset] Falling tree _SubState"""
    assert event_m10_02_x12(z61=10021210, z62=201000)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_5000():
    """Gender change 棺 桶"""
    """State 0,3: [Preset] Gender changes 棺 桶 _SubState"""
    call = event_m10_02_x40(z31=10021400, z32=102000030)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_02_5010():
    """イ ベ ン ト Startup event"""
    """State 0,2: [Preset] 棺 桶 Event at startup_SubState"""
    assert event_m10_02_x44(z29=102000030, z30=10021400)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_6000():
    """Firefighter woman housekeeper tutorial related"""
    """State 0,2: [Preset] Firework Housekeeper tutorial related _SubState"""
    assert event_m10_02_x50(z22=3300, z23=3301, z24=102281)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_7000():
    """Drops of water fall from the waterfall and the torches disappear"""
    """State 0,2: [Lib] [Preset] _SubState that erases torches with point intrusion"""
    assert event_m10_02_x8(z63=700000, z64=700000, z65=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_8000():
    """The reason of the line"""
    """State 0,2: [Preset] Line reason_SubState"""
    assert event_m10_02_x54(z18=102000040, z19=10027000)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_8010():
    """Line drawing process"""
    """State 0,2: [Preset] Line drawing process_SubState"""
    assert event_m10_02_x58(z20=102000040, z21=10027000)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_02_16000():
    """Fire prevention house event"""
    """State 0,2: [Preset] Fireproof House _SubState"""
    assert (event_m10_02_x30(z33=10020400, z34=102000010, z35=102000011, z36=102000012, val1=1600000,
            z37=102000015, z38=105501, z39=106100))
    """State 1: Finish"""
    EndMachine()

def event_m10_02_16010():
    """BGM control of fire prevention house"""
    """State 0,2: [Preset] BGM control of fire prevention house _SubState"""
    assert event_m10_02_x45(z25=10, z26=16010, z27=102000015, z28=10020400)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_80000():
    """Rebirth of Fire 01_ House of Firemen"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_02_x17(z53=1002000, z54=1002099)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_90000():
    """Trophy_lost memory"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_02_x22(z46=105501, z47=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_x0(z75=_, val1=_, z34=_, z76=_, z77=_):
    """[Lib] Normal poly play
    z75: Poly play ID
    val1: Destination point ID after poly play
    z34: Poly drama played flag
    z76: End fade
    z77: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(z34) != 1:
        """State 1: Poly play"""
        PlayCutscene(z75, z76, z77)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((val1 > 1) != 0, val1)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((val1 > 1) != 0, val1)
    SetEventFlag(z34, 1)
    """State 7: End state"""
    return 0

def event_m10_02_x1(z71=_, z72=_, z73=_, z74=_):
    """[Lib] NPC: Grave Placement: General purpose
    z71: Death map: Global event flag
    z72: Tomb: OBJ instance ID
    z73: Tomb move to: Generator ID
    z74: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z71, 1)
    IsGraveGeneratable(8, z74, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z72, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z72, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_02_x2(z68=_, z69=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z68: Global: death flag
    z69: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z69, 10, 0)
    CompareObjState(1, z69, 20, 0)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        Goto('L0')
    """State 10: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """State 2: Key guide: Key guide display"""
    Label('L0')
    CreateKeyGuideArea(34, 610)
    """State 11: Key guide: Waiting for input"""
    IsObjSearched(0, z69)
    IsPlayerInTheMap(1, 0, 0)
    if ConditionGroup(0):
        """State 3: Key Guide: Use Soul dialog"""
        # action:1211:"[ChrName]\nOffer souls to grave?\nSouls needed: %d"
        DisplayOwnYesNoMenu(1211, 0, 190, 1, GraveSoulsRequired(npc1), NpcParamTextId(npc1))
        assert YesNoMenuDisplay() != 0
        """State 7: Key Guide: Use Soul dialog: Wait for input"""
        if (YesNoMenuResult() == 1) != 0 and (CurrentSouls() > GraveSoulsRequired(npc1)) != 1:
            """State 4: Key guide: Soul shortage dialog"""
            # action:1016:"Insufficient souls"
            DisplayOwnOkMenu(1016, 3, 15, 190, 0, 0, 0)
            assert OkMenuDisplay() != 0
            """State 8: Key guide: Soul shortage dialog: Waiting for input"""
            assert OkMenuDisplay() != 1
        elif (YesNoMenuResult() == 1) != 0:
            """State 9: Key guide: Delete key guide"""
            DeleteKeyGuideArea()
            """State 12: End state"""
            return 0
        elif (YesNoMenuResult() == 2) != 0:
            pass
        elif (YesNoMenuResult() == 3) != 0:
            pass
    elif ConditionGroup(1):
        pass
    """State 6: Key guide: Reset"""
    DeleteKeyGuideArea()
    RestartMachine()

def event_m10_02_x3(z66=_, z67=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z66: Area other flags: Ghost appearance
    z67: Area other flags: Conversation start
    npc1: NPC information parameter ID
    """
    """State 0,5: Appearance of ghost: Player action starts"""
    PlayerActionRequest(6)
    IsPlayerPlayingMotion(0, 6, 1)
    assert ConditionGroup(0)
    """State 6: Ghost appearance: Seoul consumption"""
    AddSouls(-1 * GraveSoulsRequired(npc1))
    """State 7: Appearance of ghost: Waiting for player action"""
    CompareStateTime(0, 4, 2, 4)
    assert ConditionGroup(0)
    """State 1: Ghost appearance: Appearance"""
    SetEventFlag(z66, 1)
    CompareEventFlag(0, z66, 1)
    assert ConditionGroup(0)
    """State 8: Ghost appearance: waiting for completion"""
    CompareStateTime(0, 4, 2, 4)
    assert ConditionGroup(0)
    """State 3: Appearance of ghost: End of player action"""
    EndPlayerActionRequest()
    """State 2: Ghost appearance: Character action waiting"""
    IsPlayerPlayingMotion(0, 6, 0)
    assert ConditionGroup(0)
    """State 9: Ghost appearance: Waiting for conversation"""
    CompareStateTime(0, 2.1, 2, 2.1)
    assert ConditionGroup(0)
    """State 4: Ghost appearance: Conversation start flag"""
    SetEventFlag(z67, 1)
    CompareEventFlag(0, z67, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_02_x4(z66=_, z67=_, z68=_, z69=_, z70=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z66: Ghost Appearance: Area Other Flag
    z67: Conversation start: Area and other flags
    z68: Death: Global event flag
    z69: Tomb: OBJ instance ID
    z70: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z70, 1, 0)
    CompareEventFlag(9, z66, 1)
    CompareObjState(9, z69, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z67, 1)
        CompareEventFlag(0, z67, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_02_x2(z68=z68, z69=z69, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_02_x3(z66=z66, z67=z67, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_02_x5():
    """[Lib] [Reproduction] Erase torches with point intrusion"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x6(z63=700000, z64=700000):
    """[Lib] [Condition] The torch is erased by point intrusion.
    z63: Start point ID
    z64: End point ID
    """
    """State 0,1: Did you enter the point with a torch on?"""
    IsPlayerInsidePoint(8, z63, z64, 1)
    IsPlayerUsingTorch(8, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_02_x7(z65=10, z63=700000, z64=700000):
    """[Lib] [Execution] erase torches with point intrusion
    z65: Torches digestion parameter ID
    z63: Start point ID
    z64: End point ID
    """
    """State 0,1: Turn off torches"""
    RemovePlayerTorches(z65)
    """State 2: Has the torch disappeared?"""
    IsPlayerUsingTorch(0, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_02_x8(z63=700000, z64=700000, z65=10):
    """[Lib] [Preset] Erase torches with point intrusion
    z63: Start point ID
    z64: End point ID
    z65: Torches digestion parameter ID
    """
    """State 0,1: [Lib] [Reproduction] _SubState that erases torches with point intrusion"""
    assert event_m10_02_x5()
    """State 3: [Lib] [Condition] _SubState that erases torches with point intrusion"""
    assert event_m10_02_x6(z63=z63, z64=z64)
    """State 2: [Lib] [Execution] _SubState that erases torches with point intrusion"""
    assert event_m10_02_x7(z65=z65, z63=z63, z64=z64)
    """State 4: End state"""
    return 0

def event_m10_02_x9():
    """[Lib] [Reproduction] Falling Tree"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x10(z61=_):
    """[Lib] [Condition] Falling tree
    z61: OBJ instance ID of the tree
    """
    """State 0,1: Wait for tree to fall"""
    CompareObjState(0, z61, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x11(z62=_):
    """[Lib] [execution] fallen tree
    z62: Navigation change point ID
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z62, 2)
    """State 2: End state"""
    return 0

def event_m10_02_x12(z61=_, z62=_):
    """[Lib] [Preset] Falling Tree
    z61: OBJ instance ID of the tree
    z62: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Falling tree _SubState"""
    assert event_m10_02_x9()
    """State 3: [Lib] [Condition] Falling tree _SubState"""
    assert event_m10_02_x10(z61=z61)
    """State 2: [Lib] [Execution] Falling tree _SubState"""
    assert event_m10_02_x11(z62=z62)
    """State 4: End state"""
    return 0

def event_m10_02_x13(z55=3500, z56=0, z57=102000050, z58=0, z59=0, z60=4000000):
    """[Lib] Character: Petrified: Appearance setting
    z55: Generator ID
    z56: Death: Global event flag
    z57: Petrified: Area and other flags
    z58: Petrified: Global event flag
    z59: Startup state
    z60: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z55)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z56, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z57, 1)
                CompareEventFlag(1, z58, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z55, z59)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()

def event_m10_02_x14():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x15(z53=1002000, z54=1002099):
    """[Lib] [execute] Rebirth fire
    z53: Flag start ID
    z54: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z53, z54, 0)
    """State 2: End state"""
    return 0

def event_m10_02_x16():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x17(z53=1002000, z54=1002099):
    """[Lib] [Preset] Rebirth
    z53: Flag start ID
    z54: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_02_x14()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_02_x16()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_02_x15(z53=z53, z54=z54)
    """State 4: End state"""
    return 0

def event_m10_02_x18(z51=102000050, z52=0, z50=2, z49=0, z48=6000020):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z51: Other flags
    z52: Global flag
    z50: Additional attributes
    z49: Delete attribute
    z48: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z51) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z52) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z48, z50)
        DeleteNavimeshAttribute(z48, z49)
        """State 3: Flag OFF"""
        return 0

def event_m10_02_x19(z51=102000050, z52=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z51: Other flags
    z52: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z51, 1)
    CompareEventFlag(0, z52, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_02_x20(z48=6000020, z49=0, z50=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z48: Navimesh switching point ID
    z49: Additional attributes
    z50: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z48, z49)
    DeleteNavimeshAttribute(z48, z50)
    """State 2: End state"""
    return 0

def event_m10_02_x21(z48=6000020, z49=0, z50=2, z51=102000050, z52=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z48: Navimesh switching point ID
    z49: Additional attributes
    z50: Delete attribute
    z51: Other flags
    z52: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_02_x18(z51=z51, z52=z52, z50=z50, z49=z49, z48=z48)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_02_x19(z51=z51, z52=z52)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_02_x20(z48=z48, z49=z49, z50=z50)
    """State 4: End state"""
    return 0

def event_m10_02_x22(z46=105501, z47=1):
    """[Lib] [Preset] Trophy Acquisition_Global
    z46: Acquisition trigger_global flag
    z47: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z46) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z46, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z47)
    """State 4: End state"""
    return 0

def event_m10_02_x23():
    """[Lib] [DC] [Reproduction] Character deletion judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x24(z41=3350, z42=7, z43=1, z44=0):
    """[Lib] [DC] [Condition] Character deletion judgment
    z41: Generator ID
    z42: Shared flag ID
    z43: Comparison value
    z44: Judgment comparison type
    """
    """State 0,2: Has the target character been generated?"""
    IsChrActive(0, z41, 1)
    assert ConditionGroup(0)
    """State 1: Has the target character completed the return action?"""
    CompareChrEzStateValue(0, z41, z42, z43, z44)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m10_02_x25(z41=3350, z45=0):
    """[Lib] [DC] [Execution] Character deletion judgment
    z41: Generator ID
    z45: Whether to treat it as death
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z41, z45)
    """State 2: End state"""
    return 0

def event_m10_02_x26(z41=3350, z42=7, z43=1, z44=0, z45=0):
    """[Lib] [DC] [Preset] Character deletion judgment
    z41: Generator ID
    z42: Shared flag ID
    z43: Comparison value
    z44: Judgment comparison type
    z45: Whether to treat it as death
    """
    """State 0,1: [Lib] [DC] [Reproduction] Character deletion judgment_empty_SubState"""
    assert event_m10_02_x23()
    """State 3: [Lib] [DC] [Condition] Character deletion judgment_SubState"""
    assert event_m10_02_x24(z41=z41, z42=z42, z43=z43, z44=z44)
    """State 2: [Lib] [DC] [Execution] Character deletion judgment_SubState"""
    assert event_m10_02_x25(z41=z41, z45=z45)
    """State 4: End state"""
    return 0

def event_m10_02_x27(z37=102000015):
    """[Reproduction] Fireproof House
    z37: Event end flag
    """
    """State 0,1: Has the event ended already?"""
    if GetEventFlag(z37) != 0:
        pass
    else:
        Goto('L0')
    """State 4: Executed"""
    return 1
    """State 2: Is it over the second lap of the game?"""
    Label('L0')
    if (GetGameCycle() > 2) != 0:
        """State 5: During lap play"""
        return 2
    else:
        """State 3: First play"""
        return 0

def event_m10_02_x28(z33=10020400):
    """[Conditions] Fireproof House
    z33: OBJ instance ID of the door
    """
    """State 0,1: Did you try to open the door?"""
    CompareObjState(0, z33, 70, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x29(z34=102000010, z35=102000011, z36=102000012, val1=1600000, z37=102000015, z38=105501):
    """[Execution] House of fire prevention woman _ 1st lap
    z34: Poly drama replayed flag ①
    z35: Poly drama replayed flag ②
    z36: Poly drama replayed flag ③
    val1: Destination point ID after poly play
    z37: Event end flag
    z38: Trophy flags
    """
    """State 0,8: Disable auto save and prohibit operation"""
    DisableAutoSave(1)
    ProhibitPlayerOperation(1)
    """State 9: [Lib] Normal poly play_SubState"""
    assert event_m10_02_x0(z75=100211, val1=val1, z34=z34, z76=0, z77=1)
    """State 1: Name setting window display"""
    OpenNameSettingMenu()
    assert NameSettingMenuDisplay() != 0
    """State 2: Wait for completion of name setting"""
    assert NameSettingMenuDisplay() != 1
    """State 10: [Lib] Normal poly play_2_SubState"""
    assert event_m10_02_x0(z75=100221, val1=0, z34=z35, z76=0, z77=0)
    """State 6: Return the player to the living"""
    SetPlayerSpEffect(100000020, 19, 4)
    """State 3: Character makeup window display"""
    OpenCharacterCreationMenu()
    assert CharacterCreationMenuDisplay() != 0
    """State 4: Waiting for character makeup to finish"""
    assert CharacterCreationMenuDisplay() != 1
    """State 11: [Lib] Normal poly play_3_SubState"""
    assert event_m10_02_x0(z75=100231, val1=0, z34=z36, z76=1, z77=0)
    """State 7: Trophy flag ON"""
    SetEventFlag(z38, 1)
    """State 5: Event end flag ON"""
    SetEventFlag(z37, 1)
    """State 12: End state"""
    return 0

def event_m10_02_x30(z33=10020400, z34=102000010, z35=102000011, z36=102000012, val1=1600000, z37=102000015,
                     z38=105501, z39=106100):
    """[Preset] Fireproof House
    z33: OBJ instance ID of the door
    z34: Poly drama replayed flag ①
    z35: Poly drama replayed flag ②
    z36: Poly drama replayed flag ③
    val1: End point ID
    z37: Event end flag
    z38: Trophy flags
    z39: DLC flag
    """
    """State 0,2: [Reproduction] Fireproof House _SubState"""
    call = event_m10_02_x27(z37=z37)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] House of Fire Prevention Women_1 lap_SubState"""
        assert event_m10_02_x28(z33=z33)
        """State 3: [Execution] House of Fire Defense _1 lap_SubState"""
        assert event_m10_02_x29(z34=z34, z35=z35, z36=z36, val1=val1, z37=z37, z38=z38)
    elif call.Get() == 2:
        """State 5: [Condition] House of fire prevention woman _ after lap_SubState"""
        assert event_m10_02_x28(z33=z33)
        """State 6: [Execution] Fire girl's house _ after lap_SubState"""
        assert event_m10_02_x35(z34=z34, z35=z35, z36=z36, val1=val1, z37=z37, z38=z38)
    """State 1: DLC flag ON Auto save enabled Operation enabled"""
    SetEventFlag(z39, 1)
    DisableAutoSave(0)
    ProhibitPlayerOperation(0)
    """State 7: End state"""
    return 0

def event_m10_02_x31():
    """[Reproduction] Text monument"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x32(z17=_):
    """[Conditions] Text stone monument
    z17: Stele OBJ instance ID
    """
    """State 0,1: Wait for decision to check"""
    IsObjSearched(0, z17)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x33(action3=_, z40=_):
    """[Execution] Text stele
    action3: Text ID
    z40: Stele OBJ instance ID
    """
    """State 0,2: Disable key guide"""
    DisableObjKeyGuide(z40, 1)
    """State 1: Text display"""
    DisplayEventMessage(action3, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z40, 0)
    """State 4: End state"""
    return 0

def event_m10_02_x34(z40=_, action3=_):
    """[Preset] Text Stone Monument
    z40: Stele OBJ instance ID
    action3: Text ID
    """
    """State 0,1: [Reproduction] Text stone monument_SubState"""
    assert event_m10_02_x31()
    """State 3: [Condition] Text stone monument_SubState"""
    assert event_m10_02_x32(z17=z40)
    """State 2: [Execution] Text stone monument_SubState"""
    assert event_m10_02_x33(action3=action3, z40=z40)
    """State 4: End state"""
    return 0

def event_m10_02_x35(z34=102000010, z35=102000011, z36=102000012, val1=1600000, z37=102000015, z38=105501):
    """[Execution] Firefighter's House # 2 and after
    z34: Poly drama replayed flag ①
    z35: Poly drama replayed flag ②
    z36: Poly drama replayed flag ③
    val1: Destination point ID after poly play
    z37: Event end flag
    z38: Trophy flags
    """
    """State 0,3: Disable auto save and prohibit operation"""
    DisableAutoSave(1)
    ProhibitPlayerOperation(1)
    """State 4: [Lib] Normal poly play_SubState"""
    assert event_m10_02_x0(z75=100210, val1=val1, z34=z34, z76=0, z77=1)
    """State 5: [Lib] Normal poly play_2_SubState"""
    assert event_m10_02_x0(z75=100220, val1=0, z34=z35, z76=0, z77=0)
    """State 6: [Lib] Normal poly play_3_SubState"""
    assert event_m10_02_x0(z75=100230, val1=0, z34=z36, z76=1, z77=0)
    """State 2: Trophy flag ON"""
    SetEventFlag(z38, 1)
    """State 1: Event end flag ON"""
    SetEventFlag(z37, 1)
    """State 7: End state"""
    return 0

def event_m10_02_x36():
    """[Reproduction] Changing gender"""
    """State 0,1: Host judgment"""
    if IsGuest() != 0:
        """State 3: Guest termination"""
        return 1
    else:
        """State 2: End state"""
        return 0

def event_m10_02_x37(z31=10021400):
    """[Condition] Gender changes
    z31: 棺 桶 OBJ instance ID
    """
    """State 0,1: Judgment to check or multiplayer judgment"""
    IsObjSearched(0, z31)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 3: During multiplayer"""
        return 1
    elif ConditionGroup(0):
        """State 2: Examined"""
        return 0

def event_m10_02_x38(z31=10021400, z32=102000030):
    """[Execution] Changing gender
    z31: 棺 桶 OBJ instance ID
    z32: PC start flag
    """
    """State 0,8: Menu auto save disabled"""
    DisableAutoSave(1)
    ProhibitInGameMenu(1)
    """State 1: Action request to player"""
    ObjAnimationPlayerControlRequest(z31, 34, 13)
    assert PlayerIsInEventAction(13) != 0
    """State 7: キ ャ ン セ ル moved or canceled"""
    CompareObjState(0, z31, 30, 0)
    IsPlayerPlayingMotion(1, 13, 0)
    if ConditionGroup(1):
        """State 6: Initialize 棺 桶"""
        InitializeObj(z31)
        """State 11: 待 ち Waiting for initialization"""
        CompareObjState(0, z31, 10, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(0):
        """State 4: weight"""
        assert (GetStateTime() > 1.5) != 0
        """State 2: Processing to change gender * Scheduled"""
        PlayCutsceneAndWarpToMap(0, 0, 10020000, 500000, 1)
        """State 3: Startup motion flag ON"""
        SetEventFlag(z32, 1)
        """State 10: Is it gone in game?"""
        assert InGame() != 1
    """State 9: Enable menu auto save"""
    DisableAutoSave(0)
    ProhibitInGameMenu(0)
    """State 12: Rerun"""
    return 0

def event_m10_02_x39(z31=10021400):
    """[Execution] Gender changes
    z31: 棺 桶 OBJ instance ID
    """
    """State 0,1: 棺 桶 Disable key guide"""
    DisableObjKeyGuide(z31, 1)
    """State 2: Waiting for multi end"""
    IsMultiplayer(0, 0, 0)
    assert ConditionGroup(0)
    """State 3: 棺 桶 Activating key guide"""
    DisableObjKeyGuide(z31, 0)
    """State 4: Rerun"""
    return 0

def event_m10_02_x40(z31=10021400, z32=102000030):
    """[Preset] Gender changes
    z31: 棺 桶 OBJ instance ID
    z32: PC start flag
    """
    """State 0,1: [Reproduction] 棺 桶 _SubState whose gender changes"""
    call = event_m10_02_x36()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Guest termination"""
    return 1
    """State 4: [Condition] 棺 桶 _SubState whose gender changes"""
    Label('L0')
    call = event_m10_02_x37(z31=z31)
    if call.Get() == 0:
        """State 2: [Execution] Gender changes 棺 桶 _SubState"""
        assert event_m10_02_x38(z31=z31, z32=z32)
    elif call.Get() == 1:
        """State 3: [Execution] Gender changes マ ル チ Multi-sub_State"""
        assert event_m10_02_x39(z31=z31)
    """State 5: Rerun"""
    return 0

def event_m10_02_x41(z29=102000030, z30=10021400):
    """[Reproduction] 棺 桶 Startup event
    z29: PC start flag
    z30: 棺 桶 OBJ instance ID
    """
    """State 0,1: Is the PC start flag ON?"""
    if GetEventFlag(z29) != 0:
        """State 2: 棺 桶 Closed state: 30"""
        ChangeObjState(z30, 30)
        """State 3: Motion playback"""
        return 0
    else:
        """State 4: do nothing"""
        return 1

def event_m10_02_x42():
    """[Condition] 棺 桶 Startup event"""
    """State 0,1: Is it in game?"""
    assert InGame() != 0
    """State 2: End state"""
    return 0

def event_m10_02_x43(z29=102000030, z30=10021400):
    """[Execution] 棺 桶 Startup event
    z29: PC start flag
    z30: 棺 桶 OBJ instance ID
    """
    """State 0,1: Open the casket: 80"""
    ChangeObjState(z30, 80)
    """State 2: PC start flag OFF"""
    SetEventFlag(z29, 0)
    assert (GetStateTime() > 1.5) != 0
    """State 3: Gender change message display"""
    # action:4040:"The nature of your being has changed"
    DisplayEventMessage(4040, 0, 0, 0)
    """State 4: End state"""
    return 0

def event_m10_02_x44(z29=102000030, z30=10021400):
    """[Preset] 棺 桶 Startup event
    z29: PC start flag
    z30: 棺 桶 OBJ instance ID
    """
    """State 0,1: [Reproduction] 棺 桶 Startup event_SubState"""
    call = event_m10_02_x41(z29=z29, z30=z30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] 棺 桶 Startup event_SubState"""
        assert event_m10_02_x42()
        """State 2: [Execution] 棺 桶 Startup event_SubState"""
        assert event_m10_02_x43(z29=z29, z30=z30)
    """State 4: End state"""
    return 0

def event_m10_02_x45(z25=10, z26=16010, z27=102000015, z28=10020400):
    """[Preset] BGM control of fire prevention house
    z25: Fire group house floor hit group ID
    z26: Sound ID of the BGM to play
    z27: Fire prevention house event end judgment flag
    z28: Instance ID of OBJ of fire prevention house
    """
    """State 0,1: [Reproduction] BGM control of fire prevention house _SubState"""
    assert event_m10_02_x46()
    """State 2: [Condition] BGM control of fire prevention house _SubState"""
    call = event_m10_02_x47(z25=z25, z27=z27, z28=z28)
    if call.Get() == 1:
        """State 3: [Execution] BGM control of fire prevention woman's house_First event_SubState"""
        assert event_m10_02_x49(z25=z25, z26=z26, z27=z27)
    elif call.Get() == 0:
        """State 4: [Execution] BGM Control of Fireproof House _After First Event_SubState"""
        assert event_m10_02_x48(z25=z25, z26=z26)
    """State 5: End state"""
    return 0

def event_m10_02_x46():
    """[Reproduction] BGM control of fire prevention house"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x47(z25=10, z27=102000015, z28=10020400):
    """[Conditions] BGM control for fire prevention house
    z25: Fire group house floor hit group ID
    z27: Fire prevention house event end judgment flag
    z28: Instance ID of OBJ of fire prevention house
    """
    """State 0,1: Have you seen the fire prevention house event?"""
    CompareEventFlag(0, z27, 0)
    if ConditionGroup(0):
        """State 2: Did you open the door of the fire prevention woman's house?"""
        CompareObjState(0, z28, 70, 0)
        assert ConditionGroup(0)
        """State 4: At the first event"""
        return 1
    else:
        """State 3: After the first event"""
        return 0

def event_m10_02_x48(z25=10, z26=16010):
    """[Execution] BGM control of fire prevention woman's house after the first event
    z25: Fire group house floor hit group ID
    z26: Sound ID of the BGM to play
    """
    """State 0,1: BGM playback"""
    PlaySoundAtPoint(z26)
    """State 4: End state"""
    return 0

def event_m10_02_x49(z25=10, z26=16010, z27=102000015):
    """[Execution] BGM control of fire prevention woman's house at the first event
    z25: Fire group house floor hit group ID
    z26: Sound ID of the BGM to play
    z27: Fire prevention house event end judgment flag
    """
    """State 0,1: BGM playback"""
    PlaySoundAtPoint(z26)
    """State 4: End state"""
    return 0

def event_m10_02_x50(z22=3300, z23=3301, z24=102281):
    """[Preset] Firework housekeeper tutorial related
    z22: Enemy 1 generator ID to subdue
    z23: Enemy 2 generator ID to subdue
    z24: Tutorial clear flag
    """
    """State 0,1: [Reproduction] Firework housekeeper tutorial related _SubState"""
    assert event_m10_02_x51()
    """State 2: [Conditions] Firework Housekeeper tutorial related _SubState"""
    assert event_m10_02_x52(z22=z22, z23=z23)
    """State 3: [Execution] Firefighter's Housekeeper Tutorial Related _SubState"""
    assert event_m10_02_x53(z24=z24)
    """State 4: End state"""
    return 0

def event_m10_02_x51():
    """[Reproduction] Firefighter housekeeper tutorial related"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x52(z22=3300, z23=3301):
    """[Conditions] Firework Housekeeper tutorial related
    z22: Enemy 1 generator ID to subdue
    z23: Enemy 2 generator ID to subdue
    """
    """State 0,1: Defeat the designated enemy"""
    IsChrDeadOrRespawnOver(8, z22, 1)
    IsChrDeadOrRespawnOver(8, z23, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_02_x53(z24=102281):
    """[Execution] Tutorial related to fire prevention housekeeper
    z24: Tutorial clear flag
    """
    """State 0,1: Turn on the flag"""
    SetEventFlag(z24, 1)
    """State 2: End state"""
    return 0

def event_m10_02_x54(z18=102000040, z19=10027000):
    """[Preset] Line theory
    z18: Flag for generation determination of line theory
    z19: OBJ instance ID for rational display of lines
    """
    """State 0,1: [Reproduction] Line reason_SubState"""
    call = event_m10_02_x55(z18=z18)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 2: [Condition] Line reason_SubState"""
        assert event_m10_02_x56()
        """State 4: [Execution] Line reason_SubState"""
        assert event_m10_02_x57(z18=z18, z19=z19)
    """State 3: [Condition] Line theory_Generation_SubState"""
    assert event_m10_02_x64(z19=z19)
    """State 5: [Execution] Line theory_At generation_SubState"""
    assert event_m10_02_x65(z18=z18, z19=z19)
    """State 6: End state"""
    return 0

def event_m10_02_x55(z18=102000040):
    """[Reproduction] Line reason
    z18: Flag for generation determination of line theory
    """
    """State 0,1: Judgment of state by flag for generation determination of line theory"""
    if GetEventFlag(z18) != 0:
        """State 2: Acquisition judgment"""
        return 0
    else:
        """State 3: Generation determination"""
        return 1

def event_m10_02_x56():
    """[Conditions] Line theory"""
    """State 0,1: Judging the reasoning of the line"""
    IsBoneOfOrderAvailable(8, 1)
    # goods:62020000:Bone of Order
    DoesPlayerHaveItem(8, 62020000, 0, 0, 1, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_02_x57(z18=102000040, z19=10027000):
    """[Execution] Line theory
    z18: Flag for generation determination of line theory
    z19: OBJ instance ID for rational display of lines
    """
    """State 0,1: Generating lines"""
    SetEventFlag(z18, 1)
    ActivateObjItem(z19, 1)
    """State 2: End state"""
    return 0

def event_m10_02_x58(z20=102000040, z21=10027000):
    """[Preset] Line drawing process
    z20: Flag for generation determination of line theory
    z21: OBJ instance ID for rational display of lines
    """
    """State 0,1: [Reproduction] Line drawing process_SubState"""
    call = event_m10_02_x59(z20=z20, z21=z21)
    if call.Get() == 1:
        """State 4: [Conditions] Line drawing process_Generation_SubState"""
        assert event_m10_02_x62(z20=z20)
        """State 5: [Execution] Line drawing process_Generation_SubState"""
        assert event_m10_02_x63(z21=z21)
    elif call.Get() == 0:
        """State 2: [Condition] Line drawing process_SubState"""
        assert event_m10_02_x60(z21=z21)
        """State 3: [Execution] Line drawing process_SubState"""
        assert event_m10_02_x61(z21=z21)
    """State 6: End state"""
    return 0

def event_m10_02_x59(z20=102000040, z21=10027000):
    """[Reproduce] Line drawing process
    z20: Flag for generation determination of line theory
    z21: OBJ instance ID for rational display of lines
    """
    """State 0,1: [DC] [Preset] Lighthouse all lighting judgment_SubState"""
    if GetEventFlag(z20) != 0:
        """State 3: To generation judgment processing"""
        return 1
    else:
        """State 2: To drawing stop processing"""
        return 0

def event_m10_02_x60(z21=10027000):
    """[Conditions] Line drawing process
    z21: OBJ instance ID for rational display of lines
    """
    """State 0,1: Is OBJ active?"""
    IsObjActive(0, z21, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x61(z21=10027000):
    """[Execution] Line drawing process
    z21: OBJ instance ID for rational display of lines
    """
    """State 0,1: Stop generating line theory"""
    ActivateObjItem(z21, 0)
    """State 2: Is OBJ no longer active?"""
    IsObjActive(0, z21, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_02_x62(z20=102000040):
    """[Condition] Line drawing process_Generation
    z20: Flag for generation determination of line theory
    """
    """State 0,1: [DC] [Preset] Lighthouse all lighting judgment_SubState"""
    CompareEventFlag(0, z20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x63(z21=10027000):
    """[Execution] Line drawing process_Generation
    z21: OBJ instance ID for rational display of lines
    """
    """State 0,1: Stop generating line theory"""
    ActivateObjItem(z21, 0)
    """State 2: End state"""
    return 0

def event_m10_02_x64(z19=10027000):
    """[Condition] When creating a line
    z19: OBJ instance ID for rational display of lines
    """
    """State 0,1: Was the reason for the line obtained?"""
    WasObjItemAcquired(0, z19, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x65(z18=102000040, z19=10027000):
    """[Execution] When generating lines
    z18: Flag for generation determination of line theory
    z19: OBJ instance ID for rational display of lines
    """
    """State 0,1: Turn off the generation judgment flag"""
    SetEventFlag(z18, 0)
    """State 2: Reset acquired information"""
    ResetObjItem(z19)
    """State 3: End state"""
    return 0

def event_m10_02_x66(z17=10021116, action1=3015, action2=3020):
    """[Preset] Text Stone Monument_Dash Jump
    z17: Stele OBJ instance ID
    action1: Text ID at L3
    action2: Text ID for A ・ ○
    """
    """State 0,1: [Reproduction] Text stone monument_SubState"""
    assert event_m10_02_x31()
    """State 2: [Condition] Text stone monument_SubState"""
    assert event_m10_02_x32(z17=z17)
    """State 3: [Execution] Text Stele_Dash Jump_SubState"""
    assert event_m10_02_x67(z17=z17, action1=action1, action2=action2)
    """State 4: End state"""
    return 0

def event_m10_02_x67(z17=10021116, action1=3015, action2=3020):
    """[Execution] Text stone monument _ dash jump
    z17: Stele OBJ instance ID
    action1: Text ID at L3
    action2: Text ID for A ・ ○
    """
    """State 0,2: Disable key guide"""
    DisableObjKeyGuide(z17, 1)
    """State 4: Button setting judgment"""
    if JumpButtonL3Enabled() != 0:
        """State 1: Text display at L3"""
        # action:3015:"⑫ While dashing： Dashing Jump"
        DisplayEventMessage(action1, 0, 0, 0)
        assert EventMessageDisplay() != 1
    else:
        """State 5: Text display at A / ○"""
        # action:3020:"⑳ While dashing： Dashing Jump"
        DisplayEventMessage(action2, 0, 0, 0)
        assert EventMessageDisplay() != 1
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z17, 0)
    """State 6: End state"""
    return 0

def event_m10_02_x68(z9=3500, z10=0, z11=15, z12=102000050, z13=0, z14=1600, z15=6, z16=4000010):
    """Character: Petrified: Key guide
    z9: generator
    z10: Death: Global event flag
    z11: Event action
    z12: Petrified: Area and other flags
    z13: Petrified: Global event flag
    z14: Key guide parameters
    z15: Petrification start state ID
    z16: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z9, z15, 0)
    CompareEventStatus(8, z16, 1, 0)
    CompareEventFlag(2, z12, 1)
    CompareEventFlag(3, z13, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(2):
        pass
    elif ConditionGroup(3):
        pass
    elif ConditionGroup(8):
        Goto('L0')
    else:
        pass
    """State 17: End state"""
    return 0
    """State 2: Petrochemical: Key guide: Display"""
    Label('L0')
    CreateKeyGuideArea(34, z14)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z9)
    IsPlayerInTheMap(1, 0, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 5: Petrification: Key guide: Deleted"""
        DeleteKeyGuideArea()
        # goods:60537000:Fragrant Branch of Yore
        if (ItemCount(60537000, 1, 1, 0) > 1) != 1:
            """State 12: Petrification: Item not owned dialog"""
            # action:1017:"A statue blocks your way"
            DisplayOwnOkMenu(1017, 3, 15, 220, 2, 0, 0)
            assert OkMenuDisplay() != 0
            """State 13: Petrochemical: Item not owned dialog: Waiting for input"""
            assert OkMenuDisplay() != 1
        else:
            """State 10: Petrochemical: Item usage selection dialog"""
            # action:1002:"Use %s?", goods:60537000:Fragrant Branch of Yore
            DisplayOwnYesNoMenu(1002, 4, 220, 2, 60537000, 0)
            assert YesNoMenuDisplay() != 0
            """State 11: Petrochemical: Item usage selection dialog: Waiting for input"""
            if (YesNoMenuResult() == 3) != 0:
                pass
            elif (YesNoMenuResult() == 2) != 0:
                pass
            elif (YesNoMenuResult() == 1) != 0:
                """State 15,14: Petrochemical: Event action: Start"""
                DoesPlayerEventAction(0, 1)
                assert ConditionGroup(0)
                """State 6: Petrification: Event action: Regeneration"""
                PlayerActionRequest(z11)
                IsPlayerPlayingMotion(0, z11, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z12, 1)
                CompareEventFlag(0, z12, 1)
                SetEventFlag(z13, 1)
                CompareEventFlag(1, z13, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z11, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_02_x69():
    """[DC] [Reproduction] Vegrant generation determination_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x70(z6=3300, z7=3301):
    """[DC] [Condition] Vegrant generation determination
    z6: Judgment ① Generator ID
    z7: Judgment ② Generator ID
    """
    """State 0,1: Ogre defeat determination"""
    IsChrDeadOrRespawnOver(0, z6, 1)
    IsChrDeadOrRespawnOver(0, z7, 1)
    assert ConditionGroup(0)
    """State 2: Defeated"""
    return 0

def event_m10_02_x71(z5=102020060, z8=15):
    """[DC] [execution] Vegrant generation determination
    z5: Vagrant creation permission flag
    z8: Weight until generation
    """
    """State 0,2: Weight until generation"""
    CompareStateTime(0, z8, 3, z8)
    assert ConditionGroup(0)
    """State 1: Vagrant generation permission flag ON"""
    SetEventFlag(z5, 1)
    """State 3: End state"""
    return 0

def event_m10_02_x72(z5=102020060, z6=3300, z7=3301, z8=15):
    """[DC] [Preset] Vegrant generation determination
    z5: Vagrant creation permission flag
    z6: Judgment ① Generator ID
    z7: Judgment ② Generator ID
    z8: Weight until generation
    """
    """State 0,1: [DC] [Reproduction] Vegrant generation determination_empty_SubState"""
    assert event_m10_02_x69()
    """State 3: [DC] [Condition] Vegrant generation determination_SubState"""
    assert event_m10_02_x70(z6=z6, z7=z7)
    """State 2: [DC] [execution] Vegrant generation determination_SubState"""
    assert event_m10_02_x71(z5=z5, z8=z8)
    """State 4: End state"""
    return 0

def event_m10_02_x73():
    """[DC] [Condition] All lighting judgment of lighthouse"""
    """State 0,1: Did all the lighthouses light up?"""
    CompareObjState(8, 10020700, 30, 0)
    CompareObjState(8, 10020701, 30, 0)
    CompareObjState(8, 10020702, 30, 0)
    CompareObjState(8, 10020703, 30, 0)
    CompareObjState(8, 10020704, 30, 0)
    CompareObjState(8, 10020705, 30, 0)
    CompareObjState(8, 10020706, 30, 0)
    CompareObjState(8, 10020707, 30, 0)
    CompareObjState(8, 10020708, 30, 0)
    CompareObjState(8, 10020709, 30, 0)
    CompareObjState(8, 10020710, 30, 0)
    CompareObjState(8, 10020711, 30, 0)
    CompareObjState(8, 10020712, 30, 0)
    CompareObjState(8, 10020713, 30, 0)
    CompareObjState(8, 10020714, 30, 0)
    CompareObjState(8, 10020715, 30, 0)
    CompareObjState(8, 10020716, 30, 0)
    CompareObjState(8, 10020717, 30, 0)
    CompareObjState(8, 10020718, 30, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_02_x74(z4=102000065):
    """[DC] [execution] All lighting judgment of lighthouse
    z4: All lighting flag
    """
    """State 0,1: All lighting flag ON"""
    SetEventFlag(z4, 1)
    """State 2: End state"""
    return 0

def event_m10_02_x75():
    """[DC] [Reproduction] Lighthouse all lighting judgment_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_02_x76(z4=102000065):
    """[DC] [Preset] All lighting judgment of the lighthouse
    z4: All lighting flag
    """
    """State 0,1: [DC] [Reproduction] Lighthouse all lighting judgment_sky_SubState"""
    assert event_m10_02_x75()
    """State 3: [DC] [Condition] Lighthouse all lighting judgment_SubState"""
    assert event_m10_02_x73()
    """State 2: [DC] [Execution] Lighthouse all lighting judgment_SubState"""
    assert event_m10_02_x74(z4=z4)
    """State 4: End state"""
    return 0

def event_m10_02_x77(z2=102000061, z3=102000062):
    """[DC] [Reproduction] Item acquisition by destroying Vegrant
    z2: Initial item acquisition flag
    z3: Next item acquisition flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 3: Has the item been acquired? : Second and later"""
        if GetEventFlag(z3) != 0:
            pass
        else:
            """State 2: Has the item been acquired? : First time"""
            if GetEventFlag(z2) != 0:
                """State 5: Defeat determination: 2nd or later"""
                return 1
            else:
                """State 4: Defeat determination: First time"""
                return 0
    """State 6: Finish"""
    return 2

def event_m10_02_x78(z1=3350):
    """[DC] [Condition] Acquire items by destroying Vegrant
    z1: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_02_x79(lot1=_, z2=_):
    """[DC] [Execution] Item acquisition by destroying Vegrant
    lot1: Item lottery ID
    z2: Item acquisition flag
    """
    """State 0,1: Reward acquisition acquisition flag ON"""
    SetEventFlag(z2, 1)
    AwardItem(lot1, 1)
    """State 2: End state"""
    return 0

def event_m10_02_x80(z1=3350, lot1=60008100, lot2=60008110, z2=102000061, z3=102000062):
    """[DC] [Preset] Item acquisition by destroying Vegrant
    z1: Generator ID
    lot1: First item lottery ID
    lot2: Next item lottery ID
    z2: Initial item acquisition flag
    z3: Next item acquisition flag
    """
    """State 0,1: [DC] [Reproduction] Item acquisition by destroying Vegrant_SubState"""
    call = event_m10_02_x77(z2=z2, z3=z3)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        """State 4: [DC] [Condition] Acquire items by destroying Vegrant_2_SubState"""
        assert event_m10_02_x78(z1=z1)
        """State 5: [DC] [Execution] Acquire items by destroying Vegrant_2_SubState"""
        assert event_m10_02_x79(lot1=lot2, z2=z3)
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Acquire items by destroying Vegrant_SubState"""
        assert event_m10_02_x78(z1=z1)
        """State 2: [DC] [Execution] Item acquisition by destroying Vegrant_SubState"""
        assert event_m10_02_x79(lot1=lot1, z2=z2)
    """State 6: End state"""
    return 0

def event_m10_02_111102():
    """NPC: Retired Fire Defense 1: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_02_x1(z71=104060, z72=10024000, z73=211, z74=7050)

def event_m10_02_111103():
    """NPC: Retired Fire Defense 1: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7050:Strowen
    event_m10_02_x4(z66=102010105, z67=102020106, z68=104060, z69=10024000, z70=111102, npc1=7050)

def event_m10_02_111112():
    """NPC: Retired Fire Protection Woman 2: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_02_x1(z71=104070, z72=10024100, z73=216, z74=7051)

def event_m10_02_111113():
    """NPC: Retired fire prevention woman 2: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7051:Griant
    event_m10_02_x4(z66=102010110, z67=102020111, z68=104070, z69=10024100, z70=111112, npc1=7051)

def event_m10_02_111122():
    """NPC: Retired Firefighter 3: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_02_x1(z71=104080, z72=10024200, z73=221, z74=7053)

def event_m10_02_111123():
    """NPC: Retired Firefighter 3: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7053:Morrel
    event_m10_02_x4(z66=102010115, z67=102020116, z68=104080, z69=10024200, z70=111122, npc1=7053)

def event_m10_02_111152():
    """NPC: Firefighter Housekeeper: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_02_x1(z71=104100, z72=10024300, z73=16, z74=7230)

def event_m10_02_111153():
    """NPC: Firekeeper's Housekeeper: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7230:Milibeth
    event_m10_02_x4(z66=102010100, z67=102020101, z68=104100, z69=10024300, z70=111152, npc1=7230)

def event_m10_02_4000000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: Character: Petrified: Key Guide_SubState"""
    assert event_m10_02_x68(z9=3500, z10=0, z11=15, z12=102000050, z13=0, z14=1600, z15=6, z16=4000010)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_4000010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_02_x13(z55=3500, z56=0, z57=102000050, z58=0, z59=0, z60=4000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_4000020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_02_x21(z48=6000020, z49=0, z50=2, z51=102000050, z52=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_4001000():
    """[DC] Vegrant generation determination"""
    """State 0,2: [DC] [Preset] Vegrant generation determination_SubState"""
    assert event_m10_02_x72(z5=102020060, z6=3300, z7=3301, z8=15)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_4001010():
    """[DC] Vegrant removal decision"""
    """State 0,2: [Lib] [DC] [Preset] Character deletion judgment_SubState"""
    assert event_m10_02_x26(z41=3350, z42=7, z43=1, z44=0, z45=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_4001020():
    """[DC] Get items by destroying Vegrant"""
    """State 0,2: [DC] [Preset] Item acquisition by destroying Vegrant_SubState"""
    # lot:60008100:Twinkling Titanite, lot:60008110:Twinkling Titanite
    assert event_m10_02_x80(z1=3350, lot1=60008100, lot2=60008110, z2=102000061, z3=102000062)
    """State 1: Finish"""
    EndMachine()

def event_m10_02_4002000():
    """[DC] Lighthouse all lighting judgment"""
    """State 0,2: [DC] [Preset] Lighthouse all lighting judgment_SubState"""
    assert event_m10_02_x76(z4=102000065)
    """State 1: Finish"""
    EndMachine()

