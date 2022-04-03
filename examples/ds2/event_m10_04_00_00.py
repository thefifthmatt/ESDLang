# -*- coding: utf-8 -*-
def event_m10_04_3010():
    """Invade the world of miracles"""
    """State 0,3: [Preset] Intrusion item usage determination_SubState"""
    call = event_m10_04_x59(z32=2)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_04_3020():
    """Invade the world of miraculous people_return from the destination"""
    """State 0,2: [Preset] Return from intrusion_SubState"""
    # lot:60006000:Rotunda Lockstone
    assert event_m10_04_x63(z27=152, z28=50, lot1=60006000, z29=2103, z30=300010, z31=104322)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_4000():
    """The key door that opens with the key of Mr. A's house"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_04_x6(z90=1005, z91=1105, z92=50860000, z93=104000050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_4100():
    """The key door that opens with the key of Mr. B's house"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_04_x6(z90=1005, z91=1105, z92=50870000, z93=104000051)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_4200():
    """The key door that opens with the key of death"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_04_x6(z90=1005, z91=1105, z92=50820000, z93=104000052)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_5000():
    """NPC Ladder Shop Small Ladder_Navigation Mesh Change"""
    """State 0,1: Navigation mesh traffic is possible"""
    DeleteNavimeshAttribute(500000, 2)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_04_5010():
    """NPC ladder shop middle ladder_Navimesh change"""
    """State 0,1: Navigation mesh traffic is possible"""
    DeleteNavimeshAttribute(501000, 2)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_04_5020():
    """NPC Ladder Shop Large Ladder_Navigation Mesh Change"""
    """State 0,1: Navigation mesh traffic is possible"""
    DeleteNavimeshAttribute(502000, 2)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_04_6000():
    """Treasure corpse from well"""
    """State 0,2: [Preset] OBJ animation playback by attacking OBJ_SubState"""
    assert event_m10_04_x22(z73=10042105, z74=-1, z75=10046000, z76=70, z77=20)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_8000():
    """Madura-Giant Morima Gimmick Door"""
    """State 0,2: [Preset] Madura-Giant Morima Gimmick Door_SubState"""
    assert (event_m10_04_x35(z53=10043010, z54=10041015, z55=10041020, z56=800001, z57=800002, z58=800010,
            z59=800011))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_9000():
    """Revolving door switch"""
    """State 0,2: [Preset] Revolving door switch_SubState"""
    # goods:50890000:Rotunda Lockstone
    assert event_m10_04_x41(z33=10043020, z34=10043000, flag3=104020156, item1=50890000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_9010():
    """Toggles global flags related to revolving doors"""
    """State 0,2: [Preset] Switching global flags related to revolving doors_SubState"""
    assert event_m10_04_x42(z46=10043000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_9020():
    """Changing the navigation mesh of the revolving door"""
    """State 0,2: [Preset] Navimesh change of the revolving door_SubState"""
    assert event_m10_04_x51(z35=10043000, z36=30, z37=40, z38=902000, z39=902001)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_10000():
    """Switching the gimmick door related flags on the connection path"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_04_x17(z83=105405, z84=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_11000():
    """Flame 1 on the updated world map"""
    """State 0,2: [Preset] World map to be updated_SubState"""
    # bonfire:10655:Cardinal Tower
    assert event_m10_04_x47(z40=10043600, z41=150, z42=10043610, z43=100971, bonfire3=10655, z44=104010070)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11010():
    """Flame 2 on the updated world map"""
    """State 0,2: Has the Flame 1 event ended?"""
    assert EventEnded(11000) != 0
    """State 3: [Preset] World map to be updated_SubState"""
    # bonfire:16685:The Saltfort
    assert event_m10_04_x47(z40=10043600, z41=151, z42=10043620, z43=100963, bonfire3=16685, z44=104010071)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11020():
    """Flame 3 on the updated world map 3"""
    """State 0,2: Was the Flame 2 event finished?"""
    assert EventEnded(11010) != 0
    """State 3: [Preset] World map to be updated_SubState"""
    # bonfire:19660:Eygil's Idol
    assert event_m10_04_x47(z40=10043600, z41=152, z42=10043630, z43=100952, bonfire3=19660, z44=104010072)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11030():
    """Flame 4 on the updated world map"""
    """State 0,2: Was the Flame 3 event finished?"""
    assert EventEnded(11020) != 0
    """State 3: [Preset] World map to be updated_SubState"""
    # bonfire:25660:Hidden Chamber
    assert event_m10_04_x47(z40=10043600, z41=153, z42=10043640, z43=100966, bonfire3=25660, z44=104010073)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11040():
    """Flame 5 on the updated world map"""
    """State 0,2: Was the Flame 4 event finished?"""
    assert EventEnded(11030) != 0
    """State 3: [Preset] World map to be updated_SubState"""
    # bonfire:14650:Lower Brightstone Cove
    assert event_m10_04_x47(z40=10043600, z41=154, z42=10043650, z43=100951, bonfire3=14650, z44=104010074)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11050():
    """Flame 6 on the updated world map"""
    """State 0,2: Was the Flame 5 event finished?"""
    assert EventEnded(11040) != 0
    """State 3: [Preset] World map to be updated_SubState"""
    # bonfire:24650:Undead Ditch
    assert event_m10_04_x47(z40=10043600, z41=155, z42=10043660, z43=100804, bonfire3=24650, z44=104010075)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11060():
    """Fire 7 on the updated world map"""
    """State 0,2: Was the Flame 6 event finished?"""
    assert EventEnded(11050) != 0
    """State 3: [Preset] Updated World Map_Old Dragon_SubState"""
    # bonfire:27655:Shrine Entrance
    assert (event_m10_04_x81(z9=10043600, z10=156, z11=10043670, z12=103140, bonfire2=27655, z13=104010076,
            z14=100977))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_11070():
    """Fire 8 on the updated world map"""
    """State 0,2: Has the Fire 7 event ended?"""
    assert EventEnded(11060) != 0
    """State 3: [Preset] World map to be updated_SubState"""
    # bonfire:21650:King's Gate
    assert event_m10_04_x47(z40=10043600, z41=157, z42=10043680, z43=100974, bonfire3=21650, z44=104010077)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_12000():
    """Obelisk _ front side"""
    """State 0,2: [Preset] Obelisk_Front Side_SubState"""
    assert event_m10_04_x65(z23=10041000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_12010():
    """Obelisk_Backside"""
    """State 0,2: [Preset] Obelisk_Backside_SubState"""
    assert event_m10_04_x66(z22=10041010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_04_14000():
    """SFX linked to miraculous migration"""
    """State 0,2: [Preset] SFX_SubState linked to miraculous migration"""
    assert event_m10_04_x79()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_15000():
    """Miracles emigrated by clearing the hidden port"""
    """State 0,2: [Preset] Miracles migrated by clearing the hidden port_SubState"""
    assert event_m10_04_x85(z7=100961, z8=102765)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_20000():
    """Defeat Skeleton: Round 1"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1100, z25=0, z26=104000060)
    Quit()

def event_m10_04_20001():
    """Defeat Skeleton: Round 2"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1101, z25=1, z26=104000061)
    Quit()

def event_m10_04_20002():
    """Defeat Skeleton: Round 3"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1102, z25=2, z26=104000062)
    Quit()

def event_m10_04_20003():
    """Defeat Skeleton: Round 4"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1103, z25=3, z26=104000063)
    Quit()

def event_m10_04_20004():
    """Defeat Skeleton: Round 5"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1104, z25=4, z26=104000064)
    Quit()

def event_m10_04_20005():
    """Defeat Skeleton: Orbit 6"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1105, z25=5, z26=104000065)
    Quit()

def event_m10_04_20006():
    """Defeat Skeleton: Orbit 7"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1106, z25=6, z26=104000066)
    Quit()

def event_m10_04_20007():
    """Defeat Skeleton: 8 laps"""
    """State 0,1: Zako death determination_SubState"""
    event_m10_04_x64(z24=1107, z25=7, z26=104000067)
    Quit()

def event_m10_04_50000():
    """[DLC] Cheat item purchase flag management"""
    """State 0,2: [DLC] [Preset] Cheat item sales flag management_SubState"""
    assert event_m10_04_x89()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_80000():
    """Rebirth Fire 01_Main bonfire in the middle of the village"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_04_x26(z71=1004000, z72=1004099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_x0(z79=_, mode1=0, flag11=0, z106=1, z107=1):
    """[Lib] Normal poly play
    z79: Poly play ID
    mode1: Destination point ID after poly play
    flag11: Poly drama played flag
    z106: End fade
    z107: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(flag11) != 1:
        """State 1: Poly play"""
        PlayCutscene(z79, z106, z107)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((mode1 > 1) != 0, mode1)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((mode1 > 1) != 0, mode1)
    SetEventFlag(flag11, 1)
    """State 7: End state"""
    return 0

def event_m10_04_x1(z103=0, z104=0, z105=10040000, z30=300010):
    """[Lib] Warp between maps after poly play
    z103: Pre-warp poly play ID
    z104: Poly Play ID after Warp
    z105: Map ID
    z30: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z103, z104, z105, z30, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_04_x2(z99=_, z100=_, z101=_, z102=_):
    """[Lib] NPC: Grave Placement: General purpose
    z99: Death map: Global event flag
    z100: Tomb: OBJ instance ID
    z101: Tomb move to: Generator ID
    z102: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z99, 1)
    IsGraveGeneratable(8, z102, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z100, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z100, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_04_x3(z96=_, z97=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z96: Global: death flag
    z97: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z97, 10, 0)
    CompareObjState(1, z97, 20, 0)
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
    IsObjSearched(0, z97)
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
    Quit()

def event_m10_04_x4(z94=_, z95=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z94: Area other flags: Ghost appearance
    z95: Area other flags: Conversation start
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
    SetEventFlag(z94, 1)
    CompareEventFlag(0, z94, 1)
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
    SetEventFlag(z95, 1)
    CompareEventFlag(0, z95, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_04_x5(z94=_, z95=_, z96=_, z97=_, z98=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z94: Ghost Appearance: Area Other Flag
    z95: Conversation start: Area and other flags
    z96: Death: Global event flag
    z97: Tomb: OBJ instance ID
    z98: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z98, 1, 0)
    CompareEventFlag(9, z94, 1)
    CompareObjState(9, z97, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z95, 1)
        CompareEventFlag(0, z95, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_04_x3(z96=z96, z97=z97, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_04_x4(z94=z94, z95=z95, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_04_x6(z90=1005, z91=1105, z92=_, z93=_):
    """[Lib] Item specified door unlocking_2
    z90: Text ID when opened
    z91: Text ID when not opened
    z92: item
    z93: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z92, z90, z91, z93, 0)
    """State 2: End state"""
    return 0

def event_m10_04_x7(z88=_, z89=_):
    """[Lib] NPC: Death determination: General purpose
    z88: Generator ID
    z89: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z89, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z88)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z89, 1)
            CompareEventFlag(0, z89, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_04_x8(z86=10041100, z87=104020097):
    """[Lib] OBJ Pledge: First move
    z86: OBJ instance ID
    z87: During menu operation: Area and other flags
    """
    """State 0,10: OBJ: Pledge: Initialization"""
    SetEventFlag(z87, 0)
    """State 1: OBJ: Pledge: Start"""
    SetObjSync(z86, 0)
    IsPlayerInTheMap(8, 1, 0)
    CompareEventFlag(8, z87, 0)
    assert ConditionGroup(8)
    """State 2: OBJ: Pledge: Net multiplayer judgment"""
    if IsGuest() != 0:
        """State 3: OBJ: Pledge: Hide"""
        ChangeOwnObjState(10)
        CompareObjState(0, z86, 10, 0)
        assert ConditionGroup(0)
        """State 9: OBJ: Pledge: System: End"""
        EndMachine()
        Quit()
    else:
        """State 4: OBJ: Pledge: Display"""
        ChangeOwnObjState(30)
        CompareObjState(0, z86, 30, 0)
        assert ConditionGroup(0)
        """State 5: OBJ: Pledge: Start: Wait"""
        IsObjSearched(0, z86)
        assert ConditionGroup(0)
        """State 7: OBJ: Pledge: Launch"""
        SetEventFlag(z87, 1)
        CompareEventFlag(0, z87, 1)
        assert ConditionGroup(0)
        """State 8: OBJ: Pledge: Menu running: Wait"""
        CompareEventFlag(0, z87, 0)
        assert ConditionGroup(0)
        """State 11: OBJ: Pledge: Timer"""
        KeyGuideTemporarilyInvalid(1)
        CompareStateTime(0, 1, 3, 1)
        assert ConditionGroup(0)
        """State 6: OBJ: Pledge: System: Re-execution"""
        RestartMachine()
        Quit()
    """Unused"""
    """State 12: End state"""
    return 0

def event_m10_04_x9():
    """[Lib] [Reproduction] OBJ attach_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x10():
    """[Lib] [Condition] OBJ attach_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x11(z9=10043600, z10=_, z11=_):
    """[Lib] [execute] OBJ attach
    z9: Parent OBJ instance ID
    z10: Parent Damipoli ID
    z11: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z9, z10, z11)
    """State 2: End state"""
    return 0

def event_m10_04_x12(z9=10043600, z10=_, z11=_):
    """[Lib] [Preset] OBJ attach
    z9: Parent OBJ instance ID
    z10: Parent Damipoli ID
    z11: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m10_04_x9()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m10_04_x10()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m10_04_x11(z9=z9, z10=z10, z11=z11)
    """State 4: End state"""
    return 0

def event_m10_04_x13(z85=102722):
    """[Lib] Appearance determination: Magician
    z85: Appearance permission: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, 104300, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Appearance determination"""
            CompareEventFlag(8, 100961, 1)
            CompareEventFlag(8, 204800, 1)
            CompareEventFlag(8, 103801, 0)
            if ConditionGroup(8):
                pass
            else:
                Goto('L0')
        """State 4: Appearance judgment: Appearance permission"""
        SetEventFlag(z85, 1)
        CompareEventFlag(0, z85, 1)
        assert ConditionGroup(0)
    """State 5: Generation stop judgment: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_04_x14():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x15():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_04_x16(z83=105405, z84=0):
    """[Lib] [Execution] Switch to connection flag when in map
    z83: Global event flag for connection
    z84: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z83, z84)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z83, z84)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_04_x17(z83=105405, z84=0):
    """[Lib] [Preset] Switch the connection flag when in the map
    z83: Global event flag for connection
    z84: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_04_x14()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_04_x15()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_04_x16(z83=z83, z84=z84)
    """State 4: End state"""
    return 0

def event_m10_04_x18(z78=_, z79=_, z80=_, z81=_, z82=104020089):
    """[Lib] Ladder shop: Ladder installation
    z78: OBJ instance ID
    z79: Poly play ID
    z80: Size ladder installation: Global event flag
    z81: Size ladder installation: Area and other flags
    z82: Conversation standby: Area and other flags
    """
    """State 0,5: Ladder setting: Area Other flags: Setting"""
    SetEventFlag(z81, 1)
    CompareEventFlag(0, z81, 1)
    assert ConditionGroup(0)
    """State 6: Ladder setting: conversation waiting"""
    CompareEventFlag(0, z82, 1)
    assert ConditionGroup(0)
    """State 1,7: [Lib] Normal poly play_SubState"""
    assert event_m10_04_x0(z79=z79, mode1=0, flag11=0, z106=1, z107=1)
    """State 2: Ladder installation: Ladder display"""
    Label('L0')
    SetEventFlag(z80, 1)
    ChangeObjState(z78, 10)
    CompareObjState(8, z78, 10, 0)
    CompareEventFlag(8, z80, 1)
    assert ConditionGroup(8)
    """State 3: Ladder installation: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: Erasing all ladders: Erasing"""
    ChangeObjState(10041310, 30)
    ChangeObjState(10041305, 30)
    ChangeObjState(10041300, 30)
    CompareObjState(8, 10041310, 30, 0)
    CompareObjState(8, 10041305, 30, 0)
    CompareObjState(8, 10041300, 30, 0)
    SetEventFlag(102170, 0)
    SetEventFlag(102171, 0)
    SetEventFlag(102172, 0)
    assert ConditionGroup(8)
    Goto('L0')
    """State 8: End state"""
    return 0

def event_m10_04_x19():
    """[Reproduction] OBJ animation playback by attacking OBJ"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x20(z73=10042105, z74=-1):
    """[Condition] OBJ animation playback by attacking OBJ
    z73: Trigger OBJ instance ID
    z74: Damage attribute
    """
    """State 0,1: Was OBJ attacked?"""
    IsObjDamaged(0, z73, z74, -1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_04_x21(z75=10046000, z76=70, z73=10042105, z77=20):
    """[Execution] OBJ animation playback by attacking OBJ
    z75: Target OBJ instance ID
    z76: Anime OBJ State ID
    z73: Trigger OBJ instance ID
    z77: Trigger animation OBJ state ID
    """
    """State 0,1: Animation playback of trigger OBJ and target OBJ"""
    ChangeObjState(z75, z76)
    ChangeObjState(z73, z77)
    assert CompareObjStateId(z75, z76, 0) and CompareObjStateId(z73, z77, 0)
    """State 2: End state"""
    return 0

def event_m10_04_x22(z73=10042105, z74=-1, z75=10046000, z76=70, z77=20):
    """[Preset] OBJ animation playback by attacking OBJ
    z73: Trigger OBJ instance ID
    z74: Damage attribute
    z75: Target OBJ instance ID
    z76: Anime OBJ State ID
    z77: Trigger animation OBJ state ID
    """
    """State 0,1: [Reproduction] OBJ animation playback by attacking OBJ_SubState"""
    assert event_m10_04_x19()
    """State 3: [Condition] OBJ animation playback by attacking OBJ_SubState"""
    assert event_m10_04_x20(z73=z73, z74=z74)
    """State 2: [Execution] OBJ animation playback by attacking OBJ_SubState"""
    assert event_m10_04_x21(z75=z75, z76=z76, z73=z73, z77=z77)
    """State 4: End state"""
    return 0

def event_m10_04_x23():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x24(z71=1004000, z72=1004099):
    """[Lib] [execute] Rebirth fire
    z71: Flag start ID
    z72: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z71, z72, 0)
    """State 2: End state"""
    return 0

def event_m10_04_x25():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x26(z71=1004000, z72=1004099):
    """[Lib] [Preset] Rebirth
    z71: Flag start ID
    z72: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_04_x23()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_04_x25()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_04_x24(z71=z71, z72=z72)
    """State 4: End state"""
    return 0

def event_m10_04_x27(flag10=_, z70=_):
    """[Lib] [Preset] Get trophy
    flag10: Acquisition trigger_other flags
    z70: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag10) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag10, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z70)
    """State 4: End state"""
    return 0

def event_m10_04_x28(z69=_, flag7=_, flag8=_, flag9=_):
    """Dragon Miko: Boss Defeat Counter
    z69: Main Boss: Global event flag
    flag7: Sub 1 boss: Global event flag
    flag8: Sub 2 boss: Global event flag
    flag9: Sub 3 boss: Global event flag
    """
    """State 0,1: Defeat Boss"""
    if GetEventFlag(flag7) != 0:
        """State 3: Boss Defeat: Main + Sub 1 branch"""
        if GetEventFlag(flag8) != 0:
            """State 6: Defeat Boss: Defeat 3"""
            Label('L0')
            SetEventFlag(102082, 1)
            CompareEventFlag(0, 102082, 1)
            assert ConditionGroup(0)
        elif GetEventFlag(flag9) != 0:
            Goto('L0')
        else:
            """State 5: Defeat Boss: Defeat 2"""
            Label('L1')
            SetEventFlag(102081, 1)
            CompareEventFlag(0, 102081, 1)
            assert ConditionGroup(0)
    elif GetEventFlag(flag8) != 0:
        """State 4: Boss Defeated: Main + Sub 2 branch"""
        if GetEventFlag(flag9) != 0:
            Goto('L0')
        else:
            Goto('L1')
    elif GetEventFlag(flag9) != 0:
        Goto('L1')
    else:
        """State 2: Defeat Boss: Defeat 1"""
        SetEventFlag(102080, 1)
        CompareEventFlag(0, 102080, 1)
        assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m10_04_x29(z68=_, flag4=_, flag5=_, flag6=_):
    """Miracle: Boss Defeat Counter
    z68: Main Boss: Global event flag
    flag4: Sub 1 boss: Global event flag
    flag5: Sub 2 boss: Global event flag
    flag6: Sub 3 boss: Global event flag
    """
    """State 0,1: Defeat Boss"""
    if GetEventFlag(flag4) != 0:
        """State 3: Boss Defeat: Main + Sub 1 branch"""
        if GetEventFlag(flag5) != 0:
            """State 6: Defeat Boss: Defeat 3"""
            Label('L0')
            SetEventFlag(102761, 1)
            CompareEventFlag(0, 102761, 1)
            assert ConditionGroup(0)
        elif GetEventFlag(flag6) != 0:
            Goto('L0')
        else:
            """State 5: Defeat Boss: Defeat 2"""
            Label('L1')
    elif GetEventFlag(flag5) != 0:
        """State 4: Boss Defeated: Main + Sub 2 branch"""
        if GetEventFlag(flag6) != 0:
            Goto('L0')
        else:
            Goto('L1')
    elif GetEventFlag(flag6) != 0:
        Goto('L1')
    else:
        """State 2: Defeat Boss: Defeat 1"""
        pass
    """State 7: End state"""
    return 0

def event_m10_04_x30(z60=_, z61=_):
    """Miracle Person: Revolving Door: Single Anime Play
    z60: Animation playback: OBJ State ID
    z61: Target state: OBJ state ID
    """
    """State 0,1: Animation playback: Playback request"""
    ChangeOwnObjState(z60)
    CompareObjState(0, 10043000, z60, 0)
    assert ConditionGroup(0)
    """State 2: Animation playback: Playback standby"""
    CompareObjState(0, 10043000, z61, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_04_x31(z60=_, z61=_, z62=_, z63=_, z64=_, z65=_, z66=_, z67=0):
    """Miracle Person: Revolving Door: Whole Anime Play
    z60: Close: Anime State: OBJ State
    z61: Close: Target state: OBJ state
    z62: Move: Anime State: OBJ State
    z63: Movement: Target state: OBJ state
    z64: Open: Anime State: OBJ State
    z65: Open: Target state: OBJ state
    z66: Reading map ID
    z67: Animation start waiting time
    """
    """State 0,5: Judgment during OBJ operation"""
    SetEventFlag(104020156, 1)
    CompareObjState(0, 10043000, 70, 0)
    CompareObjState(0, 10043000, 71, 0)
    CompareObjState(0, 10043000, 72, 0)
    CompareObjState(0, 10043000, 80, 0)
    CompareObjState(0, 10043000, 81, 0)
    CompareObjState(0, 10043000, 82, 0)
    if ConditionGroup(0):
        """State 4: OBJ active standby"""
        CompareObjState(0, 10043000, z61, 0)
        CompareObjState(1, 10043000, z63, 0)
        CompareObjState(2, 10043000, z65, 0)
        if ConditionGroup(0):
            """State 1: Reserve standby time setting"""
            Label('L0')
            CompareStateTime(0, z67, 2, z67)
            assert ConditionGroup(0)
            """State 9: Revolving door: Door movement_SubState"""
            assert event_m10_04_x30(z60=z62, z61=z63)
            """State 2: [DC] Loading completion confirmation and chunk comparison"""
            Label('L1')
            IsMapReadAndBackreadStable(0, z66, 1)
            CompareChunkPhase(0, 2, 4)
            assert ConditionGroup(0)
            """State 10: Revolving door: lattice closed ⇒ open _SubState"""
            assert event_m10_04_x30(z60=z64, z61=z65)
        elif ConditionGroup(1):
            Goto('L1')
        elif ConditionGroup(2):
            """State 7: Waiting to open the lattice"""
            CompareObjState(0, 10043000, z65, 0)
            assert ConditionGroup(0)
    else:
        """State 6: OBJ state judgment"""
        CompareObjState(0, 10043000, z61, 0)
        CompareObjState(1, 10043000, z63, 0)
        if ConditionGroup(0):
            Goto('L0')
        elif ConditionGroup(1):
            Goto('L1')
        else:
            """State 8: Revolving door: Lattice open⇒Close_SubState"""
            assert event_m10_04_x30(z60=z60, z61=z61)
            Goto('L0')
    """State 3: Animation playback start flag OFF setting"""
    SetEventFlag(104020156, 0)
    CompareEventFlag(0, 104020156, 0)
    assert ConditionGroup(0)
    """State 11: End state"""
    return 0

def event_m10_04_x32(z53=10043010, z54=10041015, z55=10041020):
    """[Reproduction] Madura-Giant Morima Gimmick Door
    z53: Door instance ID
    z54: Instance ID of the madura lever
    z55: Giant forest lever instance ID
    """
    """State 0,2: Event ends for guests"""
    if IsGuest() != 0:
        """State 6: Simple end"""
        return 1
    else:
        """State 1: Initialize the OBJ state of the door"""
        InitializeObj(z53)
        """State 4: Navi Mesh Change: Unable to progress"""
        AddNavimeshAttribute(800000, 2)
        """State 3: Enable key guide for lever"""
        DisableObjKeyGuide(z54, 0)
        DisableObjKeyGuide(z55, 0)
        """State 5: End state"""
        return 0

def event_m10_04_x33(z54=10041015, z55=10041020):
    """[Conditions] Madura-Giant Morima Gimmick Door
    z54: Instance ID of the madura lever
    z55: Giant forest lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z54, 74, 0)
    CompareObjState(0, z55, 74, 0)
    CompareObjState(0, z54, 84, 0)
    CompareObjState(0, z55, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_04_x34(z53=10043010, z54=10041015, z55=10041020, z56=800001, z57=800002, z58=800010, z59=800011):
    """[Execution] Madura-Giant Morima Gimmick Door
    z53: Door instance ID
    z54: Instance ID of the madura lever
    z55: Giant forest lever instance ID
    z56: Point ID for door closing judgment_Start
    z57: Door closing judgment point ID_End
    z58: Forced door closing point ID_start
    z59: Forced door closing point ID_End
    """
    """State 0,1: OBJ state transition: Door: 70"""
    ChangeObjState(z53, 70)
    """State 2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z54, 1)
    DisableObjKeyGuide(z55, 1)
    """State 3: Has the door opened?"""
    CompareObjState(0, z53, 30, 0)
    IsPlayerInsidePoint(1, z58, z59, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 7: Navigation mesh change: Progress possible"""
        DeleteNavimeshAttribute(800000, 2)
        """State 4: Judgment of conditions for closing the door"""
        CompareStateTime(0, 0.7, 2, 0.7)
        IsPlayerInsidePoint(0, z56, z57, 1)
        IsPlayerInsidePoint(1, z58, z59, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 5: OBJ state transition: Door: 80"""
            ChangeObjState(z53, 80)
            """State 6: Has the door closed or entered the forced door closing point?"""
            CompareObjState(0, z53, 10, 0)
            IsPlayerInsidePoint(0, z58, z59, 1)
            assert ConditionGroup(0)
    """State 8: End state"""
    return 0

def event_m10_04_x35(z53=10043010, z54=10041015, z55=10041020, z56=800001, z57=800002, z58=800010, z59=800011):
    """[Preset] Madura-Giant Morima Gimmick Door
    z53: Door instance ID
    z54: Instance ID of the madura lever
    z55: Giant forest lever instance ID
    z56: Point ID for door closing judgment_Start
    z57: Door closing judgment point ID_End
    z58: Forced door closing point ID_start
    z59: Forced door closing point ID_End
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z53, 0)
    """State 2: [Reproduction] Madura-Giant Morima Gimmick Door_SubState"""
    call = event_m10_04_x32(z53=z53, z54=z54, z55=z55)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Conditions] Madura-Giant Morima Gimmick Door_SubState"""
        assert event_m10_04_x33(z54=z54, z55=z55)
        """State 4: [Execution] Madura-Giant Morima Gimmick Door_SubState"""
        assert event_m10_04_x34(z53=z53, z54=z54, z55=z55, z56=z56, z57=z57, z58=z58, z59=z59)
    """State 5: End state"""
    return 0

def event_m10_04_x36():
    """Armor shop: Arrangement armor selection"""
    """State 0,1: Placement armor selection: random number generation"""
    Label('L0')
    GenerateRandomNumber(1, 0, 19)
    if (GetRandomValue(0) > 0 and GetRandomValue(0) < 1) != 0:
        """State 3: Armor_on the desk on the wall_SubState"""
        Label('L1')
        call = event_m10_04_x37(z52=10043500)
        if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
            pass
        elif call.Get() == 0:
            """State 2: Arrangement armor selection: Area: Counter: Addition"""
            Label('L2')
            AddAreaVariable(63, 1)
            Goto('L0')
        elif call.Get() == 1:
            """State 4: Armor_in the box_SubState"""
            Label('L3')
            call = event_m10_04_x37(z52=10043501)
            if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
                pass
            elif call.Get() == 0:
                Goto('L2')
            elif call.Get() == 1:
                """State 5: Armor_on the desk in front_SubState"""
                Label('L4')
                call = event_m10_04_x37(z52=10043502)
                if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
                    pass
                elif call.Get() == 0:
                    Goto('L2')
                elif call.Get() == 1:
                    """State 6: 籠 Hand_on the desk on the wall_SubState"""
                    Label('L5')
                    call = event_m10_04_x37(z52=10043520)
                    if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
                        pass
                    elif call.Get() == 0:
                        Goto('L2')
                    elif call.Get() == 1:
                        """State 7: The right side of the front desk _SubState"""
                        Label('L6')
                        call = event_m10_04_x37(z52=10043521)
                        if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
                            pass
                        elif call.Get() == 0:
                            Goto('L2')
                        elif call.Get() == 1:
                            """State 8: 籠 手 _in the box_SubState"""
                            Label('L7')
                            call = event_m10_04_x37(z52=10043522)
                            if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
                                pass
                            elif call.Get() == 0:
                                Goto('L2')
                            elif call.Get() == 1:
                                """State 9: 籠 Hand_Center on the front desk_SubState"""
                                Label('L8')
                                call = event_m10_04_x37(z52=10043523)
                                if call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63)) != 0:
                                    pass
                                elif call.Get() == 0:
                                    Goto('L2')
                                elif call.Get() == 1:
                                    """State 10: 籠 手 _The right side of the wall shelf_SubState"""
                                    Label('L9')
                                    call = event_m10_04_x37(z52=10043524)
                                    if (call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63))
                                        != 0):
                                        pass
                                    elif call.Get() == 0:
                                        Goto('L2')
                                    elif call.Get() == 1:
                                        """State 11: 籠 手 _Left side of wall shelf_SubState"""
                                        Label('L10')
                                        call = event_m10_04_x37(z52=10043525)
                                        if (call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63))
                                            != 0):
                                            pass
                                        elif call.Get() == 0:
                                            Goto('L2')
                                        elif call.Get() == 1:
                                            """State 12: On the desk on the wall side_SubState"""
                                            Label('L11')
                                            call = event_m10_04_x37(z52=10043540)
                                            if (call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63))
                                                != 0):
                                                pass
                                            elif call.Get() == 0:
                                                Goto('L2')
                                            elif call.Get() == 1:
                                                """State 13: Ingredients_Bottom right side of the desk on the wall_SubState"""
                                                Label('L12')
                                                call = event_m10_04_x37(z52=10043541)
                                                if (call.Get() == 0 and (GetGlobalVariable(202) == GetAreaVariable(63))
                                                    != 0):
                                                    pass
                                                elif call.Get() == 0:
                                                    Goto('L2')
                                                elif call.Get() == 1:
                                                    """State 14: Ingredients_Left side under the desk on the wall side_SubState"""
                                                    Label('L13')
                                                    call = event_m10_04_x37(z52=10043542)
                                                    if (call.Get() == 0 and (GetGlobalVariable(202) ==
                                                        GetAreaVariable(63)) != 0):
                                                        pass
                                                    elif call.Get() == 0:
                                                        Goto('L2')
                                                    elif call.Get() == 1:
                                                        """State 15: Ingredients_in the box_SubState"""
                                                        Label('L14')
                                                        call = event_m10_04_x37(z52=10043543)
                                                        if (call.Get() == 0 and (GetGlobalVariable(202)
                                                            == GetAreaVariable(63)) != 0):
                                                            pass
                                                        elif call.Get() == 0:
                                                            Goto('L2')
                                                        elif call.Get() == 1:
                                                            """State 16: 兜 _On the right side of the desk on the wall_SubState"""
                                                            Label('L15')
                                                            call = event_m10_04_x37(z52=10043560)
                                                            if (call.Get() == 0 and (GetGlobalVariable(202)
                                                                == GetAreaVariable(63)) != 0):
                                                                pass
                                                            elif call.Get() == 0:
                                                                Goto('L2')
                                                            elif call.Get() == 1:
                                                                """State 17: 兜 _On the front desk_SubState"""
                                                                Label('L16')
                                                                call = event_m10_04_x37(z52=10043561)
                                                                if (call.Get() == 0 and (GetGlobalVariable(202)
                                                                    == GetAreaVariable(63)) != 0):
                                                                    pass
                                                                elif call.Get() == 0:
                                                                    Goto('L2')
                                                                elif call.Get() == 1:
                                                                    """State 18: 兜 _You are on the armor of the desk on the wall_SubState"""
                                                                    Label('L17')
                                                                    call = event_m10_04_x37(z52=10043562)
                                                                    if (call.Get() == 0 and (GetGlobalVariable(202)
                                                                        == GetAreaVariable(63)) != 0):
                                                                        pass
                                                                    elif call.Get() == 0:
                                                                        Goto('L2')
                                                                    elif call.Get() == 1:
                                                                        """State 19: 兜 _Left side of wall shelf_SubState"""
                                                                        Label('L18')
                                                                        call = event_m10_04_x37(z52=10043563)
                                                                        if (call.Get() == 0 and (GetGlobalVariable(202)
                                                                            == GetAreaVariable(63)) != 0):
                                                                            pass
                                                                        elif call.Get() == 0:
                                                                            Goto('L2')
                                                                        elif call.Get() == 1:
                                                                            """State 20: 兜 _Center on wall shelf_SubState"""
                                                                            Label('L19')
                                                                            call = event_m10_04_x37(z52=10043564)
                                                                            if (call.Get() == 0 and (GetGlobalVariable(202)
                                                                                == GetAreaVariable(63)) != 0):
                                                                                pass
                                                                            elif call.Get() == 0:
                                                                                Goto('L2')
                                                                            elif call.Get() == 1:
                                                                                """State 21: 兜 _Right side of the wall shelf_SubState"""
                                                                                Label('L20')
                                                                                call = event_m10_04_x37(z52=10043565)
                                                                                if (call.Get() == 0 and (GetGlobalVariable(202)
                                                                                    == GetAreaVariable(63)) != 0):
                                                                                    pass
                                                                                elif call.Get() == 0:
                                                                                    Goto('L2')
                                                                                elif call.Get() == 1:
                                                                                    Goto('L1')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 2) != 0:
        Goto('L3')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 3) != 0:
        Goto('L4')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 4) != 0:
        Goto('L6')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 5) != 0:
        Goto('L8')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 6) != 0:
        Goto('L7')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 7) != 0:
        Goto('L9')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 8) != 0:
        Goto('L10')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 9) != 0:
        Goto('L5')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
        Goto('L14')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 11) != 0:
        Goto('L12')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 12) != 0:
        Goto('L13')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 13) != 0:
        Goto('L11')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 14) != 0:
        Goto('L16')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 15) != 0:
        Goto('L20')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 16) != 0:
        Goto('L18')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 17) != 0:
        Goto('L19')
    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 18) != 0:
        Goto('L17')
    else:
        Goto('L15')
    """State 22: End state"""
    return 0

def event_m10_04_x37(z52=_):
    """Armor shop: Single armor selection
    z52: OBJ instance ID
    """
    """State 0,1: Single armor selection: Start"""
    CompareObjState(0, z52, 20, 0)
    if ConditionGroup(0):
        """State 4: Not set: End state"""
        return 1
    else:
        """State 2: Single armor selection: Setting"""
        ChangeObjStateIf(CompareObjStateId(z52, 10, 0), z52, 20)
        CompareObjState(0, z52, 20, 0)
        assert ConditionGroup(0)
        """State 3: Setting: End state"""
        return 0

def event_m10_04_x38(z33=10043020, item1=50890000):
    """[Reproduction] Revolving door switch
    z33: OBJ instance ID of the switch
    item1: Launch item
    """
    """State 0,1: Key guide enabled"""
    ChangeObjState(z33, 30)
    """State 2: End state"""
    return 0

def event_m10_04_x39(z33=10043020, item1=50890000):
    """[Conditions] Revolving door switch
    z33: OBJ instance ID of the switch
    item1: Launch item
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z33)
    assert ConditionGroup(0)
    """State 2: Do you have a launch item?"""
    DoesPlayerHaveItem(0, item1, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 3: Rotate the door"""
        return 0
    else:
        """State 4: Show message"""
        return 1

def event_m10_04_x40(z33=10043020, z34=10043000, flag3=104020156):
    """[Execution] Revolving door switch_Revolving door execution
    z33: OBJ instance ID of the switch
    z34: OBJ instance ID of the revolving door
    flag3: Rotation flag
    """
    """State 0,1: Rotation flag ON"""
    SetEventFlag(flag3, 1)
    assert GetEventFlag(flag3) != 0
    """State 3: Key guide disabled"""
    ChangeObjState(z33, 10)
    """State 5: Wait for flag OFF"""
    CompareEventFlag(0, flag3, 0)
    assert ConditionGroup(0)
    """State 2: Waiting for next start"""
    CompareObjState(0, z34, 30, 0)
    CompareObjState(0, z34, 40, 0)
    assert ConditionGroup(0)
    """State 4: Key guide enabled"""
    ChangeObjState(z33, 30)
    """State 6: End of rotation"""
    return 0

def event_m10_04_x41(z33=10043020, z34=10043000, flag3=104020156, item1=50890000):
    """[Preset] Revolving door switch
    z33: OBJ instance ID of the switch
    z34: OBJ instance ID of the revolving door
    flag3: Rotation start flag
    item1: Launch item
    """
    """State 0,1: [Reproduction] Revolving door switch_SubState"""
    assert event_m10_04_x38(z33=z33, item1=item1)
    """State 3: [Condition] Revolving door switch_SubState"""
    call = event_m10_04_x39(z33=z33, item1=item1)
    if call.Get() == 0:
        """State 2: [Execution] Revolving door switch_Revolving door execution_SubState"""
        assert event_m10_04_x40(z33=z33, z34=z34, flag3=flag3)
    elif call.Get() == 1:
        """State 4: [Execute] Revolving door switch_Message display_SubState"""
        assert event_m10_04_x55()
    """State 5: Rerun"""
    return 0

def event_m10_04_x42(z46=10043000):
    """[Preset] Switch the global flags related to revolving doors
    z46: Instance ID of revolving door OBJ
    """
    """State 0,1: [Reproduction] Switching global flags related to revolving doors_SubState"""
    assert event_m10_04_x43()
    """State 2: [Conditions] Switch global flags related to revolving doors_SubState"""
    call = event_m10_04_x44(z46=z46)
    if call.Get() == 0:
        """State 3: [Execution] Switching global flags related to revolving doors_Heide Great Fire Tower_SubState"""
        assert event_m10_04_x45(z50=0, z51=3)
    elif call.Get() == 1:
        """State 4: [Execution] Switching global flags related to revolving doors_Hunting Forest_SubState"""
        assert event_m10_04_x45(z50=1, z51=4)
    elif call.Get() == 2:
        """State 5: [Execution] Toggling global flags related to revolving doors_Operation area (Heide large fire tower side door open) _SubState"""
        assert event_m10_04_x46(z47=0, z48=2, z46=z46, z49=40)
    elif call.Get() == 3:
        """State 6: [Execution] Switching global flags related to revolving doors_Operation area (hunting forest door open) _SubState"""
        assert event_m10_04_x46(z47=1, z48=2, z46=z46, z49=30)
    """State 7: End state"""
    return 0

def event_m10_04_x43():
    """[Reproduction] Switching global flags related to revolving doors"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x44(z46=10043000):
    """[Condition] Switching global flags related to revolving doors
    z46: Instance ID of revolving door OBJ
    """
    """State 0,1: Which hit group are you on?"""
    IsPlayerOnHitGroup(0, 3, 1)
    IsPlayerOnHitGroup(1, 4, 1)
    IsPlayerOnHitGroup(8, 2, 1)
    CompareObjState(2, 10043000, 72, 0)
    CompareObjState(2, 10043000, 71, 0)
    CompareObjState(2, 10043000, 32, 0)
    CompareObjState(2, 10043000, 31, 0)
    SetConditionGroup(8, 2)
    IsPlayerOnHitGroup(9, 2, 1)
    CompareObjState(3, 10043000, 41, 0)
    CompareObjState(3, 10043000, 42, 0)
    CompareObjState(3, 10043000, 81, 0)
    CompareObjState(3, 10043000, 82, 0)
    SetConditionGroup(9, 3)
    if ConditionGroup(0):
        """State 2: You are in the passage on the side of the Great Fire Tower in Heide"""
        return 0
    elif ConditionGroup(1):
        """State 3: In the hunting forest side passage"""
        return 1
    elif ConditionGroup(8):
        """State 4: Operation area_Heide large fire tower side door opens"""
        return 2
    elif ConditionGroup(9):
        """State 5: Operation area_Hunting forest side door is open"""
        return 3

def event_m10_04_x45(z50=_, z51=_):
    """[Execute] Switch global flags related to revolving doors_Aisle area
    z50: ON / OFF of global flag
    z51: Hit group ID
    """
    """State 0,1: Change global event flag"""
    SetEventFlag(105400, z50)
    """State 2: Did you disappear from the hit group you were riding on?"""
    IsPlayerOnHitGroup(0, z51, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_04_x46(z47=_, z48=2, z46=10043000, z49=_):
    """[Execute] Switch global flags related to revolving doors_Operation area
    z47: ON / OFF of global flag
    z48: Hit group ID
    z46: Instance ID of revolving door OBJ
    z49: Revolving door OBJ state ID
    """
    """State 0,1: Change global event flag"""
    SetEventFlag(105400, z47)
    """State 2: Did you leave the operating area? Or has the open door changed?"""
    IsPlayerOnHitGroup(0, z48, 0)
    CompareObjState(0, z46, z49, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_04_x47(z40=10043600, z41=_, z42=_, z43=_, bonfire3=_, z44=_):
    """[Preset] Updated world map
    z40: World map OBJ instance ID
    z41: World map OBJ Damipoli ID
    z42: Instance ID of the flame OBJ on the world map
    z43: Global event flag ID for MAP clear determination
    bonfire3: Bonfire ID for lap level determination
    z44: NPC flag setting
    """
    """State 0,1: [Reproduction] Updated world map _SubState"""
    assert event_m10_04_x48(z9=z40, z10=z41, z11=z42)
    """State 2: [Condition] World map to be updated_SubState"""
    call = event_m10_04_x49(z43=z43, bonfire3=bonfire3, z44=z44)
    if call.Get() == 2:
        """State 3: [Execute] World map to be updated _ Blue flame _ SubState"""
        assert event_m10_04_x50(z11=z42, z45=20)
    elif call.Get() == 1:
        """State 4: [Execution] World map to be updated_Red Flame_SubState"""
        assert event_m10_04_x50(z11=z42, z45=30)
    elif call.Done():
        pass
    """State 5: End state"""
    return 0

def event_m10_04_x48(z9=10043600, z10=_, z11=_):
    """[Reproduction] Updated world map
    z9: World map OBJ instance ID
    z10: World map OBJ Damipoli ID
    z11: Instance ID of the flame OBJ on the world map
    """
    """State 0,1: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_04_x12(z9=z9, z10=z10, z11=z11)
    """State 2: End state"""
    return 0

def event_m10_04_x49(z43=_, bonfire3=_, z44=_):
    """[Condition] World map to be updated
    z43: Global event flag ID for MAP clear determination
    bonfire3: Bonfire ID for lap level determination
    z44: NPC flag
    """
    """State 0,1: Has the MAP strategy been completed?"""
    CompareEventFlag(8, z44, 1)
    CompareEventFlag(8, z43, 1)
    CompareEventFlag(0, z43, 1)
    if ConditionGroup(8):
        pass
    elif ConditionGroup(0):
        """State 3: Set NPC flag and add variable"""
        AddAreaVariable(60, 1)
        SetEventFlag(z44, 1)
        CompareEventFlag(0, z44, 1)
        assert ConditionGroup(0)
    else:
        """State 4: End state"""
        return 0
    """State 2: Is the MAP lap level 8 or higher?"""
    CompareGameCycleForBonfire(0, bonfire3, 1, 8, 3)
    if ConditionGroup(0):
        """State 6: Lit blue flame"""
        return 2
    else:
        """State 5: Lit red flame"""
        return 1

def event_m10_04_x50(z11=_, z45=_):
    """[Execution] Updated world map
    z11: Instance ID of the flame OBJ on the world map
    z45: State ID of the flame lit on the world map OBJ
    """
    """State 0,1: Lighting the flame"""
    ChangeObjState(z11, z45)
    """State 2: End state"""
    return 0

def event_m10_04_x51(z35=10043000, z36=30, z37=40, z38=902000, z39=902001):
    """[Preset] Revolving door navigation mesh change
    z35: Instance ID of revolving door OBJ
    z36: Hunting forest door open
    z37: Heide large fire tower side door open
    z38: Navimesh change ID for hunting forest
    z39: Navimesh change ID on Heide Great Fire Tower side
    """
    """State 0,1: [Reproduction] Navi mesh change of the revolving door_SubState"""
    assert event_m10_04_x52()
    """State 4: [Condition] Change navigation mesh of the revolving door_SubState"""
    call = event_m10_04_x53(z35=z35, z36=z36, z37=z37)
    if call.Get() == 0:
        """State 2: [Execution] Revolving door navigation mesh change_Hunting forest side door opening_SubState"""
        assert event_m10_04_x54(z38=z38, z39=z39, z35=z35, z37=z37)
    elif call.Get() == 1:
        """State 3: [Execution] Navimesh change of revolving door _ Heide large fire tower side door opening _ SubState"""
        assert event_m10_04_x54(z38=z39, z39=z38, z35=z35, z37=z36)
    """State 5: End state"""
    return 0

def event_m10_04_x52():
    """[Reproduction] Navi mesh change of revolving door"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x53(z35=10043000, z36=30, z37=40):
    """[Conditions] Changing the navigation mesh of the revolving door
    z35: Instance ID of revolving door OBJ
    z36: Hunting forest door open
    z37: Heide large fire tower side door open
    """
    """State 0,1: Judgment of revolving door status"""
    CompareObjState(0, z35, z36, 0)
    CompareObjState(1, z35, z37, 0)
    if ConditionGroup(0):
        """State 2: Hunting forest door is open"""
        return 0
    elif ConditionGroup(1):
        """State 3: Heide Fire Tower side door is open"""
        return 1

def event_m10_04_x54(z38=_, z39=_, z35=10043000, z37=_):
    """[Execution] Changing the navigation mesh of the revolving door
    z38: Navimesh change ID for open door
    z39: Navimesh change ID for closed door
    z35: Instance ID of revolving door OBJ
    z37: Reverse door open state
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z38, 2)
    AddNavimeshAttribute(z39, 2)
    """State 2: Was the opposite door open?"""
    CompareObjState(0, z35, z37, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_04_x55():
    """[Execution] Revolving door switch_message display"""
    """State 0,1: Message display"""
    # action:1104:"Contraption does not move"
    DisplayOwnOkMenu(1104, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m10_04_x56():
    """[Reproduction] Intrusion item usage judgment"""
    """State 0,2: Item availability flag OFF"""
    SetEventFlag(102770, 0)
    """State 5: Do you have a collapsed pupil orb?"""
    # goods:51000000:Crushed Eye Orb
    if (not ItemCount(51000000, 1, 1, 0)) != 0:
        pass
    else:
        """State 1: Survival judgment of miraculous person"""
        if GetEventFlag(104320) != 1:
            """State 3: Are miraculous people in Madura"""
            if GetEventFlag(102765) != 0 and GetEventFlag(103821) != 1:
                """State 4: Are you destroying three root bosses?"""
                if GetEventFlag(102761) != 0:
                    """State 6: Intrusion possible"""
                    return 0
                else:
                    pass
            else:
                pass
        else:
            pass
    """State 7: No intrusion"""
    return 1

def event_m10_04_x57(z32=2):
    """[Condition] Intrusion item usage judgment
    z32: Hit group ID
    """
    """State 0,1: Waiting for entry into revolving door room"""
    IsPlayerOnHitGroup(0, z32, 1)
    assert ConditionGroup(0)
    """State 2: Item available"""
    return 0

def event_m10_04_x58(z32=2):
    """[Execution] Intrusion item usage judgment
    z32: Hit group ID
    """
    """State 0,1: Item availability flag ON"""
    SetEventFlag(102770, 1)
    """State 3: Network text FE display"""
    OpenNetworkMessageMenu(2100, 0, 0, 0)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z32, 0)
    CompareEventFlag(0, 104320, 1)
    assert ConditionGroup(0)
    """State 4: Rerun"""
    return 0

def event_m10_04_x59(z32=2):
    """[Preset] Intrusion item usage judgment
    z32: Hit group ID
    """
    """State 0,1: [Reproduction] Intrusion item use determination_SubState"""
    call = event_m10_04_x56()
    if call.Get() == 1:
        """State 5: Finish"""
        return 1
    elif call.Get() == 0:
        """State 3: [Condition] Intrusion item use determination_SubState"""
        assert event_m10_04_x57(z32=z32)
        """State 2: [Execution] Intrusion item use determination_SubState"""
        assert event_m10_04_x58(z32=z32)
        """State 4: Rerun"""
        return 0

def event_m10_04_x60():
    """[Reproduction] Return from the destination"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x61(z27=152, z28=50):
    """[Condition] Return from the intruder
    z27: Generator ID
    z28: Hit group ID
    """
    """State 0,2: Did you enter the invasion destination?"""
    IsPlayerOnHitGroup(0, z28, 1)
    assert ConditionGroup(0)
    """State 1: Did you defeat the miraculous black spirit?"""
    IsChrDead(0, z27)
    assert ConditionGroup(0)
    """State 3: [BEST] Item acquisition judgment"""
    # lot:60006000:Rotunda Lockstone
    if CanGetItemLot(60006000, 1) != 0:
        """State 4: All available"""
        return 0
    else:
        """State 5: Get key items only"""
        return 1

def event_m10_04_x62(lot1=_, z29=2103, z30=300010, z31=104322):
    """[Execution] Return from intrusion
    lot1: Item lottery
    z29: Network text ID
    z30: Return point ID
    z31: Miracle person_map death flag
    """
    """State 0,5: Miracle map death flag ON"""
    SetEventFlag(z31, 1)
    """State 6: Weight after defeat"""
    assert (GetStateTime() > 1.5) != 0
    """State 1: Reward acquisition"""
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Waiting for hidden item acquisition FE"""
    assert ItemAwardDisplay() != 1
    """State 3: Network FE display"""
    OpenNetworkMessageMenu(z29, 0, 0, 0)
    """State 4: Network FE hidden waiting"""
    assert (GetStateTime() > 8) != 0
    """State 7: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_04_x1(z103=0, z104=0, z105=10040000, z30=z30)
    """State 8: End state"""
    return 0

def event_m10_04_x63(z27=152, z28=50, lot1=60006000, z29=2103, z30=300010, z31=104322):
    """[Preset] Return from intrusion
    z27: Generator ID
    z28: Hit group ID
    lot1: Item lottery
    z29: Network text ID
    z30: Return point ID
    z31: Miracle person_map death flag
    """
    """State 0,1: [Reproduction] Return from the intrusion_SubState"""
    assert event_m10_04_x60()
    """State 3: [Condition] Return from the intrusion_SubState"""
    call = event_m10_04_x61(z27=z27, z28=z28)
    if call.Get() == 0:
        """State 2: [Execution] Return from the intrusion_SubState"""
        assert event_m10_04_x62(lot1=lot1, z29=z29, z30=z30, z31=z31)
    elif call.Get() == 1:
        """State 4: [BEST] [Execution] Return from intrusion_Key item only_SubState"""
        # lot:60045000:Rotunda Lockstone
        assert event_m10_04_x62(lot1=60045000, z29=z29, z30=z30, z31=z31)
    """State 5: End state"""
    return 0

def event_m10_04_x64(z24=_, z25=_, z26=_):
    """Zako death determination
    z24: Generator ID
    z25: Lap level
    z26: Defeat: Area and other flags
    """
    """State 0,4: Death determination: Judgment level determination"""
    Label('L0')
    # bonfire:4650:The Far Fire
    CompareGameCycleForBonfire(0, 4650, 2, z25, 4)
    if ConditionGroup(0):
        pass
    else:
        """State 1: Death determination: Death determination"""
        IsChrDead(0, z24)
        assert ConditionGroup(0)
        """State 2: Death determination: Count"""
        SetEventFlag(z26, 1)
    """State 3: Death determination: System: End"""
    Label('L1')
    EndMachine()
    Quit()
    """Unused"""
    """State 5: Death determination: cartography: death"""
    CompareEventFlag(0, 104180, 1)
    if ConditionGroup(0):
        Goto('L1')
    else:
        pass
    """State 6: Death determination: Map writing: Emigration"""
    CompareEventFlag(0, 102462, 1)
    assert ConditionGroup(0)
    Goto('L0')
    """State 7: End state"""
    return 0

def event_m10_04_x65(z23=10041000):
    """[Preset] Obelisk _ front side
    z23: Obelisk OBJ instance ID to check
    """
    """State 0,1: [Reproduction] Obelisk_SubState"""
    assert event_m10_04_x67()
    """State 2: [Condition] Obelisk_SubState"""
    assert event_m10_04_x68(z22=z23)
    """State 3: [Execution] Obelisk_Front_SubState"""
    assert event_m10_04_x69()
    """State 4: End state"""
    return 0

def event_m10_04_x66(z22=10041010):
    """[Preset] Obelisk _ reverse side
    z22: Obelisk OBJ instance ID to check
    """
    """State 0,1: [Reproduction] Obelisk_SubState"""
    assert event_m10_04_x67()
    """State 2: [Condition] Obelisk_SubState"""
    assert event_m10_04_x68(z22=z22)
    """State 3: [Execution] Obelisk_Backside_SubState"""
    assert event_m10_04_x70()
    """State 4: End state"""
    return 0

def event_m10_04_x67():
    """[Reproduction] Obelisk"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x68(z22=_):
    """[Condition] Obelisk
    z22: Obelisk OBJ instance ID to check
    """
    """State 0,1: Have you examined OBJ?"""
    IsObjSearched(0, z22)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_04_x69():
    """[Execution] Obelisk _ front side"""
    """State 0,1: Death number display"""
    DisplayObeliskDeathNumber(0, 190)
    """State 2: End state"""
    return 0

def event_m10_04_x70():
    """[Execution] Obelisk _ reverse side"""
    """State 0,1: Message display"""
    DisplayObeliskMessage(0, 190)
    """State 2: End state"""
    return 0

def event_m10_04_x71(z21=_):
    """Trophy: Single survival
    z21: Death: Global event flag
    """
    """State 0,1: Death determination"""
    CompareEventFlag(0, z21, 1)
    if ConditionGroup(0):
        """State 3: Failure: Exit state"""
        return 1
    else:
        """State 2: Success: Exit state"""
        return 0

def event_m10_04_x72(z18=_, z19=_, z20=_):
    """Trophy: Migration survival
    z18: Death: Global event flag
    z19: Previous map hostile: Global event flag
    z20: Emigration permission: Global event flag
    """
    """State 0,1: Death determination"""
    CompareEventFlag(0, z18, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 2: Hostility"""
        CompareEventFlag(0, z19, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Emigration permission judgment"""
            CompareEventFlag(0, z20, 0)
            if ConditionGroup(0):
                pass
            else:
                """State 4: Success: Exit state"""
                return 0
    """State 5: Failure: Exit state"""
    return 1

def event_m10_04_x73(z15=104300, z16=103801, z17=102722):
    """Trophy: Surviving the Magician
    z15: Death: Global event flag
    z16: Previous map hostile: Global event flag
    z17: Emigration permission: Global event flag
    """
    """State 0,1: Death determination"""
    CompareEventFlag(0, z15, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 2: Hostility"""
        CompareEventFlag(0, z16, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Emigration permission judgment"""
            CompareEventFlag(0, z17, 0)
            if ConditionGroup(0):
                pass
            else:
                """State 4: Conversation judgment"""
                CompareEventFlag(0, 204800, 0)
                if ConditionGroup(0):
                    pass
                else:
                    """State 5: Judgment unlocking decision"""
                    CompareEventFlag(0, 100961, 0)
                    if ConditionGroup(0):
                        pass
                    else:
                        """State 6: Success: Exit state"""
                        return 0
    """State 7: Failure: Exit state"""
    return 1

def event_m10_04_x74():
    """Armor shop: Normal: Shop list"""
    """State 0,1: For Demon Knight Armor: Judgment"""
    CompareEventFlag(0, 100964, 1)
    if ConditionGroup(0):
        """State 2: For Demon Knight Armor: Set Flag"""
        SetEventFlag(102601, 1)
        CompareEventFlag(0, 102601, 1)
    else:
        pass
    """State 3: For Mirror Knight Armor: Judgment"""
    CompareEventFlag(0, 100958, 1)
    if ConditionGroup(0):
        """State 4: For Mirror Knight Armor: Set flag"""
        SetEventFlag(102602, 1)
        CompareEventFlag(0, 102602, 1)
    else:
        pass
    """State 5: Forgotten Sinner Armor: Judgment"""
    CompareEventFlag(0, 100963, 1)
    if ConditionGroup(0):
        """State 6: Forgotten Sinner Armor: Flag Setting"""
        SetEventFlag(102603, 1)
        CompareEventFlag(0, 102603, 1)
    else:
        pass
    """State 7: End state"""
    return 0

def event_m10_04_x75():
    """Armor shop: Bullish: Shop list"""
    """State 0,1: For Princess Knight A & C Armor: Judgment"""
    CompareEventFlag(0, 100974, 1)
    if ConditionGroup(0):
        """State 2: For Princess Knight A & C Armor: Set Flag"""
        SetEventFlag(102604, 1)
        CompareEventFlag(0, 102604, 1)
    else:
        pass
    """State 3: For Princess Knight B Armor: Judgment"""
    CompareEventFlag(0, 100975, 1)
    if ConditionGroup(0):
        """State 4: For Princess Knight B Armor: Set Flag"""
        SetEventFlag(102605, 1)
        CompareEventFlag(0, 102605, 1)
    else:
        pass
    """State 7: For butterfly armor:"""
    # bonfire:4650:The Far Fire
    CompareGameCycleForBonfire(0, 4650, 2, 2, 3)
    if ConditionGroup(0):
        """State 8: For butterfly armor: Set flag"""
        SetEventFlag(102606, 1)
        CompareEventFlag(0, 102606, 1)
    else:
        pass
    """State 5: For butterfly head equipment: Judgment"""
    # bonfire:4650:The Far Fire
    CompareGameCycleForBonfire(0, 4650, 2, 3, 3)
    if ConditionGroup(0):
        """State 6: For butterfly head equipment: Set flag"""
        SetEventFlag(102607, 1)
        CompareEventFlag(0, 102607, 1)
    else:
        pass
    """State 9: End state"""
    return 0

def event_m10_04_x76():
    """[Conditions] SFX linked to miraculous migration"""
    """State 0,1: Migration determination"""
    CompareEventFlag(0, 102765, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_04_x77():
    """[Reproduction] SFX_sky linked with miraculous people's migration"""
    """State 0,1: End state"""
    return 0

def event_m10_04_x78():
    """[Execution] SFX linked with miraculous migration"""
    """State 0,1: SFX playback"""
    PlaySfxAtPoint(14000)
    """State 2: End state"""
    return 0

def event_m10_04_x79():
    """[Preset] SFX linked with miraculous migration"""
    """State 0,1: [Reproduction] SFX_sky_SubState linked to miraculous people's migration"""
    assert event_m10_04_x77()
    """State 3: [Condition] SFX_SubState linked with miraculous people's migration"""
    assert event_m10_04_x76()
    """State 2: [Execution] SFX_SubState linked to miraculous migration"""
    assert event_m10_04_x78()
    """State 4: End state"""
    return 0

def event_m10_04_x80(z12=103140, bonfire2=27655, z13=104010076, z14=100977):
    """[Condition] World map to be updated
    z12: Global event flag ID for MAP clear determination
    bonfire2: Bonfire ID for lap level determination
    z13: NPC flag
    z14: Global flag for MAP clear determination ②
    """
    """State 0,1: Has the MAP strategy been completed?"""
    CompareEventFlag(8, z13, 1)
    CompareEventFlag(1, z12, 1)
    CompareEventFlag(1, z14, 1)
    SetConditionGroup(8, 1)
    CompareEventFlag(0, z12, 1)
    CompareEventFlag(0, z14, 1)
    if ConditionGroup(8):
        pass
    elif ConditionGroup(0):
        """State 3: Set NPC flag and add variable"""
        AddAreaVariable(60, 1)
        SetEventFlag(z13, 1)
        CompareEventFlag(0, z13, 1)
        assert ConditionGroup(0)
    else:
        """State 4: End state"""
        return 0
    """State 2: Is the MAP lap level 8 or higher?"""
    # bonfire:27655:Shrine Entrance
    CompareGameCycleForBonfire(0, bonfire2, 1, 8, 3)
    if ConditionGroup(0):
        """State 6: Lit blue flame"""
        return 2
    else:
        """State 5: Lit red flame"""
        return 1

def event_m10_04_x81(z9=10043600, z10=156, z11=10043670, z12=103140, bonfire2=27655, z13=104010076, z14=100977):
    """[Preset] World map to be updated
    z9: World map OBJ instance ID
    z10: World map OBJ Damipoli ID
    z11: Instance ID of the flame OBJ on the world map
    z12: Global event flag ID for MAP clear determination
    bonfire2: Bonfire ID for lap level determination
    z13: NPC flag setting
    z14: Global event flag ID for MAP clear determination ②
    """
    """State 0,1: [Reproduction] Updated world map _SubState"""
    assert event_m10_04_x48(z9=z9, z10=z10, z11=z11)
    """State 4: [Conditions] World map to be updated_Old Dragon_SubState"""
    call = event_m10_04_x80(z12=z12, bonfire2=bonfire2, z13=z13, z14=z14)
    if call.Get() == 2:
        """State 2: [Execute] World map to be updated _ Blue flame _ SubState"""
        assert event_m10_04_x50(z11=z11, z45=20)
    elif call.Get() == 1:
        """State 3: [Execution] World map to be updated_Red Flame_SubState"""
        assert event_m10_04_x50(z11=z11, z45=30)
    elif call.Done():
        pass
    """State 5: End state"""
    return 0

def event_m10_04_x82():
    """[Reproduction] Miracles migrated by clearing the hidden port"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_04_x83(z7=100961):
    """[Conditions] Miracles emigrated by clearing the hidden port
    z7: Boss Defeat Global Flag
    """
    """State 0,1: Did you destroy the boss?"""
    CompareEventFlag(0, z7, 1)
    if ConditionGroup(0):
        """State 2: Defeated"""
        return 0
    else:
        """State 3: Undefeated"""
        return 1

def event_m10_04_x84(z8=102765):
    """[Execution] The miraculous people migrated by clearing the hidden port
    z8: Miracle Person: Emigration Flag
    """
    """State 0,1: Miracle Person: Immigration Flag ON"""
    SetEventFlag(z8, 1)
    """State 2: End state"""
    return 0

def event_m10_04_x85(z7=100961, z8=102765):
    """[Preset] Miracles emigrated by clearing the hidden port
    z7: Boss Defeat Global Flag
    z8: Miracle Person: Emigration Flag
    """
    """State 0,1: [Reproduction] Miracles migrated by clearing the hidden port_SubState"""
    call = event_m10_04_x82()
    if call.Get() == 0:
        """State 3: [Conditions] Miracles emigrated by clearing the hidden port_SubState"""
        call = event_m10_04_x83(z7=z7)
        if call.Get() == 0:
            """State 2: [Execution] The miraculous people migrated by clearing the hidden port_SubState"""
            assert event_m10_04_x84(z8=z8)
        elif call.Get() == 1:
            pass
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_04_x86():
    """[DLC] [Reproduction] Cheat item sales flag management"""
    """State 0,1: Event ends for guests"""
    if IsGuest() != 0:
        """State 4: Guest termination"""
        return 1
    else:
        """State 2: Initialize variables for judgment"""
        SetAreaVariable(40, 0)
        """State 3: End state"""
        return 0

def event_m10_04_x87():
    """[DLC] [Condition] Cheat item sales flag management"""
    """State 0,1: Have you purchased DLC?"""
    CompareEventFlag(0, 100610, 1)
    CompareEventFlag(0, 100611, 1)
    CompareEventFlag(0, 100612, 1)
    if ConditionGroup(0):
        pass
    else:
        Goto('L0')
    """State 2: Has the castle been cleared?"""
    CompareEventFlag(0, 100958, 1)
    if ConditionGroup(0):
        """State 7: Add variable for judgment"""
        AddAreaVariable(40, 5)
    else:
        """State 3: Has Freyadia been defeated?"""
        CompareEventFlag(0, 100951, 1)
        if ConditionGroup(0):
            """State 8: Add variable for judgment_2"""
            AddAreaVariable(40, 1)
        else:
            pass
        """State 4: Has the iron king been destroyed?"""
        CompareEventFlag(0, 100952, 1)
        if ConditionGroup(0):
            """State 9: Add variable for judgment_3"""
            AddAreaVariable(40, 1)
        else:
            pass
        """State 6: Was the forgotten sinner defeated?"""
        CompareEventFlag(0, 100963, 1)
        if ConditionGroup(0):
            """State 10: Add variable for judgment_4"""
            AddAreaVariable(40, 1)
        else:
            pass
        """State 5: Have you been killed?"""
        CompareEventFlag(0, 100966, 1)
        if ConditionGroup(0):
            """State 11: Add variable for judgment_5"""
            AddAreaVariable(40, 1)
        else:
            pass
    """State 12: End state"""
    return 0
    """State 13: DLC not purchased"""
    Label('L0')
    return 1

def event_m10_04_x88():
    """[DLC] [execute] Cheat item sales flag management"""
    """State 0,1: Variable judgment"""
    if (GetAreaVariable(40) == 5) != 0:
        """State 2: Completed the Royal Castle"""
        SetEventFlag(100620, 1)
        SetEventFlag(100621, 1)
        SetEventFlag(100622, 1)
        SetEventFlag(100623, 1)
        SetEventFlag(100624, 1)
        SetEventFlag(100625, 1)
    elif (GetAreaVariable(40) == 4) != 0:
        """State 3: Four route clear"""
        SetEventFlag(100620, 1)
        SetEventFlag(100621, 1)
        SetEventFlag(100622, 1)
        SetEventFlag(100623, 1)
        SetEventFlag(100624, 1)
    elif (GetAreaVariable(40) == 3) != 0:
        """State 4: Three route clear"""
        SetEventFlag(100620, 1)
        SetEventFlag(100621, 1)
        SetEventFlag(100622, 1)
        SetEventFlag(100623, 1)
    elif (GetAreaVariable(40) == 2) != 0:
        """State 5: Two route clear"""
        SetEventFlag(100620, 1)
        SetEventFlag(100621, 1)
        SetEventFlag(100622, 1)
    elif (GetAreaVariable(40) == 1) != 0:
        """State 6: One route clear"""
        SetEventFlag(100620, 1)
        SetEventFlag(100621, 1)
    else:
        """State 7: initial state"""
        SetEventFlag(100620, 1)
    """State 8: End state"""
    return 0

def event_m10_04_x89():
    """[DLC] [Preset] Cheat item sales flag management"""
    """State 0,1: [DLC] [Reproduction] Cheat item sales flag management_SubState"""
    call = event_m10_04_x86()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [DLC] [Condition] Cheat item sales flag management_SubState"""
        call = event_m10_04_x87()
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 3: [DLC] [execution] Cheat item sales flag management_SubState"""
            assert event_m10_04_x88()
    """State 4: End state"""
    return 0

def event_m10_04_x90(flag1=104000002, flag2=104000001):
    """[DC] [Reproduction] Reincarnation of Pig
    flag1: Fate generation flag
    flag2: Parent pig generation flag
    """
    """State 0,1: Has a fang beast appeared?"""
    if GetEventFlag(flag1) != 0:
        pass
    else:
        Goto('L0')
    """State 5: Fang beast generating"""
    return 2
    """State 2: Has a parent pig appeared?"""
    Label('L0')
    if GetEventFlag(flag2) != 0:
        """State 4: During parent pig production"""
        return 1
    else:
        """State 3: During piglet production"""
        return 0

def event_m10_04_x91(z2=1000, z3=1001, z4=1002):
    """[DC] [Condition] Reincarnation of pigs_pigs
    z2: Piglet generator ID
    z3: Piglet ② generator ID
    z4: Piglet ③ Generator ID
    """
    """State 0,1: Have all the piglets been depleted?"""
    IsChrMaxRespawnCount(8, z2, 1, 0)
    IsChrMaxRespawnCount(8, z3, 1, 0)
    IsChrMaxRespawnCount(8, z4, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_04_x92(flag2=_):
    """[DC] [execution] pig reincarnation
    flag2: Generate flag
    """
    """State 0,1: Generation flag ON"""
    SetEventFlag(flag2, 1)
    """State 2: End state"""
    return 0

def event_m10_04_x93(z5=1010, z6=1011):
    """[DC] [Condition] Reincarnation of pigs_parent pig
    z5: Parent pig ① generator ID
    z6: Parent pig ② generator ID
    """
    """State 0,1: Has all the parent pigs been exhausted?"""
    IsChrMaxRespawnCount(8, z5, 1, 0)
    IsChrMaxRespawnCount(8, z6, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_04_x94(flag1=104000002, flag2=104000001, z2=1000, z3=1001, z4=1002, z5=1010, z6=1011):
    """[DC] [Preset] Pig reincarnation
    flag1: Fate generation flag
    flag2: Parent pig generation flag
    z2: Piglet generator ID
    z3: Piglet ② generator ID
    z4: Piglet ③ Generator ID
    z5: Parent pig ① generator ID
    z6: Parent pig ② generator ID
    """
    """State 0,1: [DC] [Reproduction] Reincarnation of pigs_SubState"""
    call = event_m10_04_x90(flag1=flag1, flag2=flag2)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        """State 4: [DC] [Condition] Reincarnation of pigs_Parent pigs_SubState"""
        assert event_m10_04_x93(z5=z5, z6=z6)
        """State 5: [DC] [Execution] Pig reincarnation_2_SubState"""
        assert event_m10_04_x92(flag2=flag1)
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Reincarnation of pig"""
        assert event_m10_04_x91(z2=z2, z3=z3, z4=z4)
        """State 2: [DC] [execution] Reincarnation of pigs_SubState"""
        assert event_m10_04_x92(flag2=flag2)
    """State 6: Finish"""
    return 0

def event_m10_04_x95(bonfire1=4650):
    """[DC] [Condition] Treasure chest changes mimic
    bonfire1: Bonfire ID
    """
    """State 0,1: Is the total number of laps more than the second lap?"""
    # bonfire:4650:The Far Fire
    CompareGameCycleForBonfire(0, bonfire1, 2, 2, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_04_x96(z1=10045060):
    """[DC] [execution] treasure chest changes mimic
    z1: Treasure chest OBJ instance ID
    """
    """State 0,1: Hidden treasure box and key guide disabled"""
    ChangeDrawHit(z1, 0)
    DisableObjKeyGuide(z1, 1)
    assert (GetStateTime() > 0.1) != 0
    """State 2: End state"""
    return 0

def event_m10_04_x97():
    """[DC] [Reproduction] Treasure box changes mimic"""
    """State 0,1: Is it in game?"""
    assert InGame() != 0
    """State 2: End state"""
    return 0

def event_m10_04_x98(bonfire1=4650, z1=10045060):
    """[DC] [Preset] Treasure chest changes mimic
    bonfire1: Bonfire ID
    z1: Treasure chest OBJ instance ID
    """
    """State 0,1: [DC] [Reproduction] Treasure box changes mimic_SubState"""
    assert event_m10_04_x97()
    """State 3: [DC] [Condition] Treasure box changes mimic_SubState"""
    assert event_m10_04_x95(bonfire1=bonfire1)
    """State 2: [DC] [execution] treasure box changes mimic_SubState"""
    assert event_m10_04_x96(z1=z1)
    """State 4: End state"""
    return 0

def event_m10_04_111052():
    """OBJ: Dragon Maiden: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104020, z100=10044500, z101=207, z102=7000)
    Quit()

def event_m10_04_111053():
    """OBJ: Dragon Maiden: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7000:Emerald Herald
    event_m10_04_x5(z94=104010160, z95=104020161, z96=104020, z97=10044500, z98=111052, npc1=7000)
    Quit()

def event_m10_04_111054():
    """OBJ: Dragon Lady: Boss Defeat Counter"""
    """State 0,1: Boss Defeat: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 4: Boss Defeat: Branch"""
        CompareEventFlag(1, 100963, 1)
        CompareEventFlag(2, 100952, 1)
        CompareEventFlag(3, 100966, 1)
        CompareEventFlag(4, 100951, 1)
        CompareEventFlag(8, 100963, 1)
        CompareEventFlag(8, 100952, 1)
        CompareEventFlag(8, 100966, 1)
        CompareEventFlag(8, 100951, 1)
        if ConditionGroup(8):
            """State 2: Defeat Boss: Defeat 4"""
            SetEventFlag(102083, 1)
            CompareEventFlag(0, 102083, 1)
            assert ConditionGroup(0)
        elif ConditionGroup(1):
            """State 5: Dragon Miko: Boss Defeat Counter (Forgotten Sinner) _SubState"""
            assert event_m10_04_x28(z69=100963, flag7=100952, flag8=100966, flag9=100951)
        elif ConditionGroup(2):
            """State 6: Dragon Miko: Boss Defeat Counter (Fused Iron Demon) _SubState"""
            assert event_m10_04_x28(z69=100952, flag7=100963, flag8=100966, flag9=100951)
        elif ConditionGroup(3):
            """State 7: Dragon Miko: Boss Defeat Counter (Butcher) _SubState"""
            assert event_m10_04_x28(z69=100966, flag7=100963, flag8=100952, flag9=100951)
        elif ConditionGroup(4):
            """State 8: Dragon Miko: Boss Defeat Counter (Queen Queen) _SubState"""
            assert event_m10_04_x28(z69=100951, flag7=100963, flag8=100952, flag9=100966)
        else:
            pass
    """State 3: Boss Defeat: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111055():
    """OBJ: Dragon Lady: Random generation"""
    """State 0,1: Random generation: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Random generation: Death determination"""
        CompareEventFlag(0, 104020, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Random generation: initial placement determination"""
            CompareEventFlag(0, 201100, 0)
            if ConditionGroup(0):
                """State 5: Random generation: initial placement setting"""
                SetEventFlag(104010157, 1)
                CompareEventFlag(0, 104010157, 1)
                assert ConditionGroup(0)
            else:
                """State 6: Random generation: Relocation determination"""
                CompareEventFlag(0, 104010157, 1)
                CompareEventFlag(1, 104010158, 1)
                CompareEventFlag(2, 104010159, 1)
                CompareEventFlag(3, 104010166, 1)
                CompareEventFlag(6, 104010169, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                elif ConditionGroup(2):
                    pass
                elif ConditionGroup(3):
                    pass
                elif ConditionGroup(6):
                    pass
                else:
                    """State 7: Random generation: random number generation"""
                    GenerateRandomNumber(0, 0, 100)
                    CompareStateTime(0, 1, 3, 1)
                    assert ConditionGroup(0)
                    """State 8: Random generation: generation branch"""
                    if (GetRandomValue(0) > 0 and GetRandomValue(0) < 1) != 0:
                        """State 11: Random generation: Rock sitting 2: Extend both hands back"""
                        DeleteEnemyByGeneratorGroup(51, 0)
                        DeleteEnemyByGeneratorGroup(52, 0)
                        DeleteEnemyByGeneratorGroup(56, 0)
                        SetEventFlag(104010166, 1)
                        CompareEventFlag(0, 104010166, 1)
                        assert ConditionGroup(0)
                    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
                        """State 10: Random generation: Rock seat 1: Poke your cheek with your hand"""
                        DeleteEnemyByGeneratorGroup(51, 0)
                        DeleteEnemyByGeneratorGroup(53, 0)
                        DeleteEnemyByGeneratorGroup(56, 0)
                        SetEventFlag(104010159, 1)
                        CompareEventFlag(0, 104010159, 1)
                        assert ConditionGroup(0)
                    elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 30) != 0:
                        """State 12: Random generation: Standing 2: Kicking the ground"""
                        DeleteEnemyByGeneratorGroup(52, 0)
                        DeleteEnemyByGeneratorGroup(51, 0)
                        DeleteEnemyByGeneratorGroup(53, 0)
                        SetEventFlag(104010169, 1)
                        CompareEventFlag(0, 104010169, 1)
                        assert ConditionGroup(0)
                    else:
                        """State 9: Random generation: Standing 1: Looking at the sky"""
                        DeleteEnemyByGeneratorGroup(52, 0)
                        DeleteEnemyByGeneratorGroup(53, 0)
                        DeleteEnemyByGeneratorGroup(56, 0)
                        SetEventFlag(104010158, 1)
                        CompareEventFlag(0, 104010158, 1)
                        assert ConditionGroup(0)
    """State 3: Random generation: System: Exit"""
    EndMachine()
    Quit()

def event_m10_04_111092():
    """OBJ: Ladder Shop: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104052, z100=10044000, z101=46, z102=7040)
    Quit()

def event_m10_04_111093():
    """OBJ: Ladder Shop: Tomb Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7040:Laddersmith Gilligan
    event_m10_04_x5(z94=104010080, z95=104020081, z96=104050, z97=10044000, z98=111092, npc1=7040)
    Quit()

def event_m10_04_111094():
    """OBJ: Ladder shop: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=45, z89=104052)
    Quit()

def event_m10_04_111095():
    """OBJ: Ladder shop: Small ladder installation"""
    """State 0,1: [Lib] Ladder shop: Ladder installation_SubState"""
    event_m10_04_x18(z78=10041310, z79=100450, z80=102170, z81=104020086, z82=104020089)
    Quit()

def event_m10_04_111096():
    """OBJ ： Ladder shop ： Installation of middle ladder"""
    """State 0,1: [Lib] Ladder shop: Ladder installation_SubState"""
    event_m10_04_x18(z78=10041305, z79=100451, z80=102171, z81=104020087, z82=104020089)
    Quit()

def event_m10_04_111097():
    """OBJ: Ladder shop: Large ladder installation"""
    """State 0,1: [Lib] Ladder shop: Ladder installation_SubState"""
    event_m10_04_x18(z78=10041300, z79=100452, z80=102172, z81=104020088, z82=104020089)
    Quit()

def event_m10_04_111098():
    """OBJ: Ladder shop: Eliminate all ladders"""
    """State 0,1: Complete ladder elimination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: All ladder elimination: End judgment"""
    CompareEventFlag(8, 102170, 1)
    CompareEventFlag(8, 102171, 1)
    CompareEventFlag(8, 102172, 1)
    if ConditionGroup(8):
        pass
    else:
        """State 5: Short ladder: Erase judgment"""
        CompareEventFlag(0, 102170, 0)
        if ConditionGroup(0):
            """State 8: Short ladder: erasure"""
            ChangeObjState(10041310, 30)
            CompareObjState(8, 10041310, 30, 0)
        else:
            pass
        """State 6: Normal ladder: Erase judgment"""
        CompareEventFlag(0, 102171, 0)
        if ConditionGroup(0):
            """State 9: Normal ladder: Elimination"""
            ChangeObjState(10041305, 30)
            CompareObjState(8, 10041305, 30, 0)
        else:
            pass
        """State 7: Long ladder: Erase judgment"""
        CompareEventFlag(0, 102172, 0)
        if ConditionGroup(0):
            """State 10: Long ladder: erasure"""
            CompareObjState(8, 10041300, 30, 0)
            ChangeObjState(10041300, 30)
        else:
            pass
    """State 4: Complete ladder elimination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 3: Erasing all ladders: Erasing"""
    ChangeObjState(10041310, 30)
    ChangeObjState(10041305, 30)
    ChangeObjState(10041300, 30)
    CompareObjState(8, 10041310, 30, 0)
    CompareObjState(8, 10041305, 30, 0)
    CompareObjState(8, 10041300, 30, 0)
    assert ConditionGroup(8)
    Goto('L0')

def event_m10_04_111099():
    """OBJ: Ladder shop: Appearance judgment"""
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Appearance determination: Death determination"""
    CompareEventFlag(0, 104050, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 4: Appearance judgment: Naga defeat judgment"""
        CompareEventFlag(0, 100956, 1)
        if ConditionGroup(0):
            """State 5: Appearance determination: Appearance determination"""
            SetEventFlag(102165, 1)
            CompareEventFlag(0, 102165, 1)
            assert ConditionGroup(0)
        else:
            pass
    """State 3: Appearance determination: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111222():
    """OBJ: Broken Blue Warrior: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104140, z100=10044100, z101=101, z102=7410)
    Quit()

def event_m10_04_111223():
    """OBJ: Broken blue warrior: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7410:Crestfallen Saulden
    event_m10_04_x5(z94=104010090, z95=104020091, z96=104140, z97=10044100, z98=111222, npc1=7410)
    Quit()

def event_m10_04_111224():
    """OBJ: Broken warrior: The migrants count"""
    """State 0,1: Migrant count: start"""
    CompareEventFlag(0, 104020099, 1)
    assert ConditionGroup(0)
    """State 15: Emigration count: initialization"""
    SetAreaVariable(58, 0)
    """State 16: Dragon Miko: Single Survival_SubState"""
    call = event_m10_04_x71(z21=104020)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: Dragon Miko: Count Up"""
        AddAreaVariable(58, 1)
    """State 17: Ladder Shop: Emigration survival_SubState"""
    call = event_m10_04_x72(z18=104050, z19=103551, z20=102165)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: Ladder shop: Count up"""
        AddAreaVariable(58, 1)
    """State 18: Broken spirited warrior: Single survival _SubState"""
    call = event_m10_04_x71(z21=104140)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 6: Broken hearted blue warrior: Count up"""
        AddAreaVariable(58, 1)
    """State 19: Map writing: Emigration survival_SubState"""
    call = event_m10_04_x72(z18=104180, z19=103681, z20=102460)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 7: Map writing: Count up"""
        AddAreaVariable(58, 1)
    """State 20: Yorozu Baba: Emigration Survival_SubState"""
    call = event_m10_04_x72(z18=104210, z19=103711, z20=102521)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 8: Yorozu Baba: Count up"""
        AddAreaVariable(58, 1)
    """State 21: Armor Shop: Single Survival_SubState"""
    call = event_m10_04_x71(z21=104250)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 9: Armor shop: Count up"""
        AddAreaVariable(58, 1)
    """State 22: Material shop: Emigration survival_SubState"""
    call = event_m10_04_x72(z18=104260, z19=103761, z20=102625)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 10: Material shop: Count up"""
        AddAreaVariable(58, 1)
    """State 23: Magician: Immigration Survival_SubState"""
    call = event_m10_04_x72(z18=104270, z19=103771, z20=102650)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 11: Magician: Count Up"""
        AddAreaVariable(58, 1)
    """State 24: Blacksmith: Single Survival_SubState"""
    call = event_m10_04_x71(z21=104280)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 12: Blacksmith: Count Up"""
        AddAreaVariable(58, 1)
    """State 25: Trophy: Survival of Magician Migration_SubState"""
    call = event_m10_04_x73(z15=104300, z16=103801, z17=102722)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 13: Magician: Count up"""
        AddAreaVariable(58, 1)
    """State 26: Miracle People: Emigration Survival_SubState"""
    call = event_m10_04_x72(z18=104320, z19=103821, z20=102765)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 14: Miracle: Count up"""
        AddAreaVariable(58, 1)
    """State 3: Emigration count: Set end flag"""
    SetEventFlag(104020099, 0)
    CompareEventFlag(0, 104020099, 0)
    assert ConditionGroup(0)
    """State 2: Emigration count: System: Re-execution"""
    RestartMachine()
    Quit()

def event_m10_04_111262():
    """OBJ: Mapping: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104182, z100=10044200, z101=86, z102=7510)
    Quit()

def event_m10_04_111263():
    """OBJ: cartography: key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7510:Cartographer Cale
    event_m10_04_x5(z94=104010100, z95=104020101, z96=104180, z97=10044200, z98=111262, npc1=7510)
    Quit()

def event_m10_04_111264():
    """OBJ: Mapping: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=85, z89=104182)
    Quit()

def event_m10_04_111265():
    """OBJ: Map writing: Migration decision"""
    """State 0,1: Migration determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Migration decision: death decision"""
        CompareEventFlag(0, 104180, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Migration decision: Migration decision"""
            CompareEventFlag(8, 102460, 1)
            CompareEventFlag(8, 103681, 0)
            CompareEventFlag(8, 100971, 1)
            assert ConditionGroup(8)
            """State 5: Migration decision: Migration decision"""
            SetEventFlag(102462, 1)
            CompareEventFlag(0, 102462, 1)
            assert ConditionGroup(0)
    """State 3: Migration determination: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111266():
    """OBJ: Mapping: Skeleton Defeat Count"""
    """State 0,1: Defeat count: death judgment"""
    CompareEventFlag(0, 104180, 1)
    CompareEventFlag(1, 104000060, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        """State 3: Defeat count: lap level branch"""
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(0, 4650, 2, 1, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(1, 4650, 2, 2, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(2, 4650, 2, 3, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(3, 4650, 2, 4, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(4, 4650, 2, 5, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(5, 4650, 2, 6, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(6, 4650, 2, 7, 0)
        # bonfire:4650:The Far Fire
        CompareGameCycleForBonfire(7, 4650, 2, 8, 3)
        if ConditionGroup(0):
            """State 4: Defeat count: lap level 1: standby"""
            CompareEventFlag(0, 104000060, 1)
            assert ConditionGroup(0)
        elif ConditionGroup(1):
            """State 5: Defeat count: lap level 2: standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            assert ConditionGroup(8)
        elif ConditionGroup(2):
            """State 7: Defeat count: lap level 3: standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            CompareEventFlag(8, 104000062, 1)
            assert ConditionGroup(8)
        elif ConditionGroup(3):
            """State 8: Defeat count: Circulation level 4: Standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            CompareEventFlag(8, 104000062, 1)
            CompareEventFlag(8, 104000063, 1)
            assert ConditionGroup(8)
        elif ConditionGroup(4):
            """State 9: Defeat count: lap level 5: standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            CompareEventFlag(8, 104000062, 1)
            CompareEventFlag(8, 104000063, 1)
            CompareEventFlag(8, 104000064, 1)
            assert ConditionGroup(8)
        elif ConditionGroup(5):
            """State 10: Defeat count: lap level 6: standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            CompareEventFlag(8, 104000062, 1)
            CompareEventFlag(8, 104000063, 1)
            CompareEventFlag(8, 104000064, 1)
            CompareEventFlag(8, 104000065, 1)
            assert ConditionGroup(8)
        elif ConditionGroup(6):
            """State 11: Defeat count: lap level 7: standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            CompareEventFlag(8, 104000062, 1)
            CompareEventFlag(8, 104000063, 1)
            CompareEventFlag(8, 104000064, 1)
            CompareEventFlag(8, 104000065, 1)
            CompareEventFlag(8, 104000066, 1)
            assert ConditionGroup(8)
        elif ConditionGroup(7):
            """State 12: Defeat count: lap level 8: standby"""
            CompareEventFlag(8, 104000060, 1)
            CompareEventFlag(8, 104000061, 1)
            CompareEventFlag(8, 104000062, 1)
            CompareEventFlag(8, 104000063, 1)
            CompareEventFlag(8, 104000064, 1)
            CompareEventFlag(8, 104000065, 1)
            CompareEventFlag(8, 104000066, 1)
            CompareEventFlag(8, 104000067, 1)
            assert ConditionGroup(8)
        """State 6: Defeat count: Defeat all skeletons"""
        SetEventFlag(104000107, 1)
        CompareEventFlag(0, 104000107, 1)
        assert ConditionGroup(0)
    """State 2: Defeat Count: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111267():
    """OBJ: Map writing: Appearance determination"""
    """State 0,4: Appearance judgment: Appearance disapproval: Setting"""
    SetEventFlag(104020106, 0)
    CompareEventFlag(0, 104020106, 0)
    assert ConditionGroup(0)
    """State 5: Appearance determination: Start"""
    CompareEventStatus(8, 111265, 1, 0)
    CompareEventStatus(8, 111266, 1, 0)
    IsPlayerInsidePoint(8, 10000000, 10000000, 0)
    CompareEventFlag(8, 104000107, 1)
    CompareEventStatus(9, 111265, 1, 0)
    CompareEventStatus(9, 111266, 1, 0)
    CompareEventFlag(9, 104000107, 1)
    CompareEventFlag(9, 104020108, 1)
    if ConditionGroup(8):
        pass
    elif ConditionGroup(9):
        pass
    """State 6: Appearance judgment: Appearance permission"""
    SetGlobalVariable(207, 0)
    CompareEventFlagValue(8, 0, 207, 0, 0)
    SetEventFlag(104020106, 1)
    CompareEventFlag(8, 104020106, 1)
    SetEventFlag(104020108, 1)
    CompareEventFlag(8, 104020108, 1)
    assert ConditionGroup(8)
    """State 2: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 1: Appearance determination: Start old"""
    CompareEventStatus(8, 111265, 1, 0)
    CompareEventStatus(8, 111266, 1, 0)
    IsPlayerInsidePoint(8, 10000000, 10000000, 0)
    CompareEventFlag(0, 104000107, 1)
    assert ConditionGroup(8)
    """State 3: Appearance determination: Appearance permission old"""
    SetGlobalVariable(207, 0)
    CompareEventFlagValue(8, 0, 207, 0, 0)
    SetEventFlag(104020106, 1)
    CompareEventFlag(8, 104020106, 1)
    assert ConditionGroup(8)
    Goto('L0')

def event_m10_04_111292():
    """OBJ: Yorozu Baba: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104212, z100=10044150, z101=261, z102=7540)
    Quit()

def event_m10_04_111293():
    """OBJ: Yorozu Baba: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7540:Merchant Hag Melentia
    event_m10_04_x5(z94=104010170, z95=104020171, z96=104210, z97=10044150, z98=111292, npc1=7540)
    Quit()

def event_m10_04_111294():
    """OBJ: Yorozu Baba: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=260, z89=104212)
    Quit()

def event_m10_04_111332():
    """OBJ: Armor shop: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104250, z100=10044250, z101=106, z102=7610)
    Quit()

def event_m10_04_111333():
    """OBJ: Armor shop: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7610:Maughlin the Armourer
    event_m10_04_x5(z94=104010110, z95=104020111, z96=104250, z97=10044250, z98=111332, npc1=7610)
    Quit()

def event_m10_04_111334():
    """OBJ: Armor shop: State transition"""
    """State 0,1: State transition: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: State transition: death judgment"""
        CompareEventFlag(0, 104250, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 4: State transition: bullish judgment"""
            CompareEventFlagValue(0, 0, 227, NpcInfoValue(7610, 5), 3)
            if ConditionGroup(0):
                """State 8: State transition: bullish setting"""
                SetEventFlag(102612, 1)
                SetEventFlag(102610, 0)
                SetEventFlag(102611, 0)
                DeleteEnemyByGeneratorGroup(31, 0)
                DeleteEnemyByGeneratorGroup(30, 0)
                CompareEventFlag(8, 102612, 1)
                CompareEventFlag(8, 102610, 0)
                CompareEventFlag(8, 102611, 0)
                assert ConditionGroup(8)
            else:
                """State 5: State transition: Normal judgment"""
                CompareEventFlagValue(0, 0, 227, NpcInfoValue(7610, 4), 3)
                if ConditionGroup(0):
                    """State 7: State transition: Normal setting"""
                    SetEventFlag(102611, 1)
                    SetEventFlag(102610, 0)
                    SetEventFlag(102612, 0)
                    DeleteEnemyByGeneratorGroup(30, 0)
                    CompareEventFlag(8, 102611, 1)
                    CompareEventFlag(8, 102610, 0)
                    CompareEventFlag(8, 102612, 0)
                    assert ConditionGroup(8)
                else:
                    """State 6: State transition: bearish setting"""
                    SetEventFlag(102610, 1)
                    SetEventFlag(102611, 0)
                    SetEventFlag(102612, 0)
                    CompareEventFlag(8, 102610, 1)
                    CompareEventFlag(8, 102611, 0)
                    CompareEventFlag(8, 102612, 0)
                    assert ConditionGroup(8)
    """State 3: State transition: System: Exit"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: State transition: Shop list update: Standby"""
    CompareEventStatus(0, 111338, 1, 0)
    assert ConditionGroup(0)
    Goto('L0')

def event_m10_04_111335():
    """OBJ: Armor shop: Armor arrangement"""
    """State 0,1: Armor placement: Start"""
    SetGlobalVariableIf((not GetGlobalVariable(202)) != 0, 202, 1)
    IsPlayerInTheMap(8, 1, 0)
    CompareEventFlag(8, 102610, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(8):
        """State 10: Armor placement: Level judgment"""
        CompareEventFlagValue(8, 0, 203, 1, 0)
        CompareEventFlag(8, 102610, 1)
        CompareEventFlag(8, 102611, 0)
        CompareEventFlagValue(9, 0, 203, 2, 0)
        CompareEventFlag(9, 102610, 1)
        CompareEventFlag(9, 102611, 1)
        if ConditionGroup(8):
            pass
        elif ConditionGroup(9):
            pass
        else:
            """State 2: Armor placement: All placement judgment"""
            CompareObjState(8, 10043500, 20, 0)
            CompareObjState(8, 10043501, 20, 0)
            CompareObjState(8, 10043502, 20, 0)
            CompareObjState(8, 10043520, 20, 0)
            CompareObjState(8, 10043521, 20, 0)
            CompareObjState(8, 10043522, 20, 0)
            CompareObjState(8, 10043523, 20, 0)
            CompareObjState(8, 10043524, 20, 0)
            CompareObjState(8, 10043525, 20, 0)
            CompareObjState(8, 10043540, 20, 0)
            CompareObjState(8, 10043541, 20, 0)
            CompareObjState(8, 10043542, 20, 0)
            CompareObjState(8, 10043543, 20, 0)
            CompareObjState(8, 10043560, 20, 0)
            CompareObjState(8, 10043561, 20, 0)
            CompareObjState(8, 10043562, 20, 0)
            CompareObjState(8, 10043563, 20, 0)
            CompareObjState(8, 10043564, 20, 0)
            CompareObjState(8, 10043565, 20, 0)
            if ConditionGroup(8):
                pass
            else:
                """State 5: Armor placement: Global ⇒ Area: Counter"""
                SetAreaVariable(63, GetGlobalVariable(202))
                """State 4: Armor placement: Number of placement settings"""
                GenerateRandomNumberIf(GetEventFlag(102610) != 0 and GetEventFlag(102611) != 1 and GetEventFlag(102612) != 1,
                                       0, 1, 5)
                GenerateRandomNumberIf(GetEventFlag(102610) != 0 and GetEventFlag(102611) != 0 and GetEventFlag(102612) != 1,
                                       0, 6, 12)
                assert (GetStateTime() >= 0) != 0
                """State 7: Armor arrangement: Number of arrangements ⇒ Area: Number of arrangements"""
                SetAreaVariableIf(GetEventFlag(102610) != 0 and GetEventFlag(102611) != 1 and GetEventFlag(102612) != 1,
                                  62, GetRandomValue(0))
                SetAreaVariableIf(GetEventFlag(102610) != 0 and GetEventFlag(102611) != 0 and GetEventFlag(102612) != 1,
                                  62, GetRandomValue(0))
                SetAreaVariableIf(GetEventFlag(102610) != 0 and GetEventFlag(102611) != 0 and GetEventFlag(102612) != 0,
                                  62, 19)
                assert (GetStateTime() >= 0) != 0
                """State 6: Armor Arrangement: Area: Number of Arrangements ⇒ Global"""
                SetGlobalVariable(202, GetAreaVariable(62))
                """State 12: Armor shop: Arrangement armor selection_SubState"""
                assert event_m10_04_x36()
                """State 11: Armor placement: Global: Level setting"""
                SetGlobalVariableIf((GetGlobalVariable(203) == 2) != 0, 203, 3)
                SetGlobalVariableIf((GetGlobalVariable(203) == 1) != 0, 203, 2)
                SetGlobalVariableIf((not GetGlobalVariable(203)) != 0, 203, 1)
    """State 3: Armor placement: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: Armor placement: System: Re-execution"""
    Label('L0')
    RestartMachine()
    Quit()
    """State 9: Armor placement: Re-execution: Standby"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    Goto('L0')

def event_m10_04_111336():
    """OBJ: Armor shop: Shop list"""
    """State 0,1: Shop list: Start"""
    CompareEventStatus(0, 111334, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Shop list: State transition judgment"""
        CompareEventFlag(0, 102610, 1)
        CompareEventFlag(1, 102611, 1)
        CompareEventFlag(2, 102612, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Armor shop: Normal: Shop list_SubState"""
            Label('L0')
            assert event_m10_04_x74()
            """State 4: Shop list: bullish state transition judgment"""
            CompareEventFlag(2, 102612, 1)
            if ConditionGroup(2):
                """State 6: Armor Store: Bullish: Shop List_SubState"""
                assert event_m10_04_x75()
            else:
                pass
        elif ConditionGroup(2):
            Goto('L0')
    """State 2: Shop list: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111342():
    """OBJ: Material shop: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104262, z100=10044350, z101=111, z102=7620)
    Quit()

def event_m10_04_111343():
    """OBJ: Material shop: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7620:Stone Trader Chloanne
    event_m10_04_x5(z94=104010120, z95=104020121, z96=104260, z97=10044350, z98=111342, npc1=7620)
    Quit()

def event_m10_04_111344():
    """OBJ: Material shop: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=110, z89=104262)
    Quit()

def event_m10_04_111352():
    """OBJ: Magician: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104272, z100=10044450, z101=116, z102=7630)
    Quit()

def event_m10_04_111353():
    """OBJ: Magician: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7630:Rosabeth of Melfia
    event_m10_04_x5(z94=104010194, z95=104020195, z96=104270, z97=10044450, z98=111352, npc1=7630)
    Quit()

def event_m10_04_111354():
    """OBJ: Magician: Death check"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=115, z89=104272)
    Quit()

def event_m10_04_111355():
    """OBJ: Magician: Appearance determination"""
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, 104270, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Appearance determination: Timer start flag determination"""
            CompareEventFlag(8, 102652, 1)
            CompareEventFlag(8, 102653, 0)
            CompareEventFlag(9, 102652, 1)
            CompareEventFlag(9, 102653, 1)
            if ConditionGroup(9):
                """State 5: Appearance determination: Appearable"""
                SetEventFlag(102650, 1)
                CompareEventFlag(0, 102650, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(8):
                """State 6: Appearance determination: Intrusion setting"""
                SetEventFlag(102653, 1)
                CompareEventFlag(0, 102653, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 3: Appearance determination: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111362():
    """OBJ: Blacksmith: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104280, z100=10044300, z101=121, z102=7640)
    Quit()

def event_m10_04_111363():
    """OBJ: Blacksmith: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7640:Blacksmith Lenigrast
    event_m10_04_x5(z94=104010130, z95=104020131, z96=104280, z97=10044300, z98=111362, npc1=7640)
    Quit()

def event_m10_04_111365():
    """OBJ: Blacksmith: Judgment of movement"""
    """State 0,1: Judgment: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 5: Movement judgment: Door unlocked judgment"""
        Label('L0')
        CompareEventFlag(0, 102661, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Movement judgment: Door unlocking judgment"""
            CompareEventFlag(0, 102660, 1)
            if ConditionGroup(0):
                """State 3: Movement judgment: Character movement"""
                SetEventFlag(102661, 1)
                CompareEventFlag(0, 102661, 1)
                assert ConditionGroup(0)
            else:
                Goto('L1')
        """State 7: Judgment: Previous generator: Delete"""
        DeleteEnemyByGeneratorGroup(60, 0)
    """State 4: Movement judgment: System: End"""
    Label('L1')
    EndMachine()
    Quit()
    """Unused"""
    """State 6: Movement judgment: Death judgment"""
    CompareEventFlag(0, 104280, 1)
    if ConditionGroup(0):
        Goto('L1')
    else:
        Goto('L0')

def event_m10_04_111366():
    """OBJ: Blacksmith: Door unlocking judgment"""
    """State 0,1: Door unlocking determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 6: Door unlocking determination: Unlocking determination"""
        Label('L0')
        CompareEventFlag(0, 102660, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Door unlocking determination: Unlocking: Standby"""
            IsPlayerInTheMap(0, 0, 0)
            CompareObjState(1, 10040450, 30, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 4: Door unlocking judgment: unlocking setting"""
                SetEventFlag(102660, 1)
                CompareEventFlag(0, 102660, 1)
                assert ConditionGroup(0)
    """State 3: Door unlocking determination: System: End"""
    Label('L1')
    EndMachine()
    Quit()
    """Unused"""
    """State 5: Door unlocking judgment: Death judgment"""
    CompareEventFlag(0, 104280, 1)
    if ConditionGroup(0):
        Goto('L1')
    else:
        Goto('L0')

def event_m10_04_111392():
    """OBJ: Magician: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104302, z100=10044400, z101=136, z102=7660)
    Quit()

def event_m10_04_111393():
    """OBJ: Magician: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7660:Carhillion of the Fold
    event_m10_04_x5(z94=104010140, z95=104020141, z96=104300, z97=10044400, z98=111392, npc1=7660)
    Quit()

def event_m10_04_111394():
    """OBJ: Magician: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=135, z89=104302)
    Quit()

def event_m10_04_111395():
    """OBJ: Magician: Appearance judgment"""
    """State 0,1: [Lib] Appearance determination: Magician_SubState"""
    event_m10_04_x13(z85=102722)
    Quit()

def event_m10_04_111412():
    """OBJ: Miracle Person: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_04_x2(z99=104322, z100=10044050, z101=151, z102=7690)
    Quit()

def event_m10_04_111413():
    """OBJ: Miracle Person: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7690:Licia of Lindeldt
    event_m10_04_x5(z94=104010150, z95=104020151, z96=104320, z97=10044050, z98=111412, npc1=7690)
    Quit()

def event_m10_04_111414():
    """OBJ: Miracle: Death decision"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_04_x7(z88=150, z89=104322)
    Quit()

def event_m10_04_111415():
    """OBJ: Miracle Person: Boss Defeat Counter"""
    """State 0,1: Boss Defeat: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Boss Defeat: Branch"""
        CompareEventFlag(0, 102761, 1)
        CompareEventFlag(1, 100963, 1)
        CompareEventFlag(2, 100952, 1)
        CompareEventFlag(3, 100966, 1)
        CompareEventFlag(4, 100951, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 4: Miracle: Boss Defeat Counter (Forgotten Sinner) _SubState"""
            assert event_m10_04_x29(z68=100963, flag4=100952, flag5=100966, flag6=100951)
        elif ConditionGroup(2):
            """State 5: Miracle: Boss Defeat Counter (Demon Iron) _SubState"""
            assert event_m10_04_x29(z68=100952, flag4=100963, flag5=100966, flag6=100951)
        elif ConditionGroup(3):
            """State 6: Miracle: Boss Defeat Counter (Butcher) _SubState"""
            assert event_m10_04_x29(z68=100966, flag4=100963, flag5=100952, flag6=100951)
        elif ConditionGroup(4):
            """State 7: Miracle Person: Boss Defeat Counter (Queen of Amber) _SubState"""
            assert event_m10_04_x29(z68=100951, flag4=100963, flag5=100952, flag6=100966)
        else:
            pass
    """State 2: Boss Defeat: System: End"""
    EndMachine()
    Quit()

def event_m10_04_111416():
    """OBJ: Miracle Person: Revolving Door"""
    """State 0,1: Revolving door: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 3: Revolving door: System: End"""
    EndMachine()
    Quit()
    """State 6: Revolving door: Animation playback: Initialization"""
    Label('L0')
    CompareObjState(0, 10043000, 31, 0)
    CompareObjState(0, 10043000, 32, 0)
    CompareObjState(0, 10043000, 70, 0)
    CompareObjState(0, 10043000, 71, 0)
    CompareObjState(0, 10043000, 72, 0)
    CompareObjState(1, 10043000, 41, 0)
    CompareObjState(1, 10043000, 42, 0)
    CompareObjState(1, 10043000, 80, 0)
    CompareObjState(1, 10043000, 81, 0)
    CompareObjState(1, 10043000, 82, 0)
    IsObjActive(8, 10043000, 1)
    if ConditionGroup(0):
        """State 7: Revolving door: Left lattice start_SubState"""
        Label('L1')
        assert event_m10_04_x31(z60=70, z61=31, z62=71, z63=32, z64=72, z65=40, z66=10310000, z67=0)
    elif ConditionGroup(1):
        """State 8: Revolving door: Right lattice start_SubState"""
        Label('L2')
        assert event_m10_04_x31(z60=80, z61=41, z62=81, z63=42, z64=82, z65=30, z66=10230000, z67=0)
    else:
        """State 2: Revolving door: Start standby"""
        CompareEventFlag(0, 104020156, 1)
        IsPlayerInTheMap(1, 0, 0)
        if ConditionGroup(0):
            """State 5: Revolving door: Playback animation branch"""
            CompareObjState(0, 10043000, 30, 0)
            CompareObjState(1, 10043000, 40, 0)
            CompareObjState(0, 10043000, 31, 0)
            CompareObjState(0, 10043000, 32, 0)
            CompareObjState(0, 10043000, 70, 0)
            CompareObjState(0, 10043000, 71, 0)
            CompareObjState(0, 10043000, 72, 0)
            CompareObjState(1, 10043000, 41, 0)
            CompareObjState(1, 10043000, 42, 0)
            CompareObjState(1, 10043000, 80, 0)
            CompareObjState(1, 10043000, 81, 0)
            CompareObjState(1, 10043000, 82, 0)
            if ConditionGroup(0):
                Goto('L1')
            elif ConditionGroup(1):
                Goto('L2')
        elif ConditionGroup(1):
            pass
    """State 4: Revolving door: System: Re-execution"""
    RestartMachine()
    Quit()

def event_m10_04_111467():
    """OBJ: Cat: Random generation"""
    """State 0,1: Random generation: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Random generation: Flag initialization setting"""
        CompareEventFlag(0, 104010186, 1)
        CompareEventFlag(1, 104010187, 1)
        CompareEventFlag(4, 104010190, 1)
        CompareEventFlag(5, 104010191, 1)
        CompareEventFlag(6, 104010192, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(4):
            pass
        elif ConditionGroup(5):
            pass
        elif ConditionGroup(6):
            pass
        else:
            """State 2: Random generation: random number generation"""
            GenerateRandomNumber(0, 0, 50)
            CompareStateTime(0, 1, 3, 1)
            assert ConditionGroup(0)
            """State 4: Random generation: generation branch"""
            if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
                """State 5: Random generation: Cat: Sitting"""
                DeleteEnemyByGeneratorGroup(41, 0)
                DeleteEnemyByGeneratorGroup(44, 0)
                DeleteEnemyByGeneratorGroup(45, 0)
                DeleteEnemyByGeneratorGroup(46, 0)
                SetEventFlag(104010186, 1)
                CompareEventFlag(0, 104010186, 1)
                assert ConditionGroup(0)
            elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 20) != 0:
                """State 6: Random generation: Cat: sitting in a box"""
                DeleteEnemyByGeneratorGroup(40, 0)
                DeleteEnemyByGeneratorGroup(44, 0)
                DeleteEnemyByGeneratorGroup(45, 0)
                DeleteEnemyByGeneratorGroup(46, 0)
                SetEventFlag(104010187, 1)
                CompareEventFlag(0, 104010187, 1)
                assert ConditionGroup(0)
            elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 30) != 0:
                """State 9: Random generation: Cat: Sharpening nails"""
                DeleteEnemyByGeneratorGroup(40, 0)
                DeleteEnemyByGeneratorGroup(41, 0)
                DeleteEnemyByGeneratorGroup(45, 0)
                DeleteEnemyByGeneratorGroup(46, 0)
                SetEventFlag(104010190, 1)
                CompareEventFlag(0, 104010190, 1)
                assert ConditionGroup(0)
            elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 40) != 0:
                """State 10: Random generation: Cat: Leaning on chair back"""
                DeleteEnemyByGeneratorGroup(40, 0)
                DeleteEnemyByGeneratorGroup(41, 0)
                DeleteEnemyByGeneratorGroup(44, 0)
                DeleteEnemyByGeneratorGroup(46, 0)
                SetEventFlag(104010191, 1)
                CompareEventFlag(0, 104010191, 1)
                assert ConditionGroup(0)
            elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 50) != 0:
                """State 11: Random generation: Cat: sleeping on the edge of the table"""
                DeleteEnemyByGeneratorGroup(40, 0)
                DeleteEnemyByGeneratorGroup(41, 0)
                DeleteEnemyByGeneratorGroup(44, 0)
                DeleteEnemyByGeneratorGroup(45, 0)
                SetEventFlag(104010192, 1)
                CompareEventFlag(0, 104010192, 1)
                assert ConditionGroup(0)
        """State 12: Random generation: System termination: Wait"""
        Label('L0')
        CompareEventStatus(0, 111468, 1, 0)
        assert ConditionGroup(0)
    """State 13: Random generation: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: Random generation: Cat: Fits on railing"""
    DeleteEnemyByGeneratorGroup(40, 0)
    DeleteEnemyByGeneratorGroup(41, 0)
    DeleteEnemyByGeneratorGroup(43, 0)
    DeleteEnemyByGeneratorGroup(44, 0)
    DeleteEnemyByGeneratorGroup(45, 0)
    DeleteEnemyByGeneratorGroup(46, 0)
    SetEventFlag(104010188, 1)
    CompareEventFlag(0, 104010188, 1)
    assert ConditionGroup(0)
    Goto('L0')
    """State 8: Random generation: Cat: Curled in a pot"""
    DeleteEnemyByGeneratorGroup(40, 0)
    DeleteEnemyByGeneratorGroup(41, 0)
    DeleteEnemyByGeneratorGroup(42, 0)
    DeleteEnemyByGeneratorGroup(44, 0)
    DeleteEnemyByGeneratorGroup(45, 0)
    DeleteEnemyByGeneratorGroup(46, 0)
    SetEventFlag(104010189, 1)
    CompareEventFlag(0, 104010189, 1)
    assert ConditionGroup(0)
    Goto('L0')

def event_m10_04_111468():
    """OBJ: Cat: Shop list"""
    """State 0,1: Shop list: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Shop List: Boss Defeat: Judgment"""
    CompareEventFlag(8, 100967, 1)
    CompareEventFlag(8, 100965, 1)
    if ConditionGroup(8):
        """State 4: Shop List: Defeat Boss: Set Flag"""
        SetEventFlag(102860, 1)
        CompareEventFlag(0, 102860, 1)
        assert ConditionGroup(0)
    else:
        pass
    """State 3: Shop list: End"""
    EndMachine()
    Quit()

def event_m10_04_112000():
    """OBJ: Strong man's monument (pledge event)"""
    """State 0,1: [Lib] OBJ Pledge: Initial _SubState"""
    event_m10_04_x8(z86=10041100, z87=104020097)
    Quit()

def event_m10_04_120030():
    """Trophy: The Weak Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_04_x27(flag10=104020030, z70=21)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_04_120070():
    """Trophy: The Pledge of the Strong"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_04_x27(flag10=104020031, z70=25)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_04_120090():
    """Trophy: Strange map completion"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_04_x27(flag10=104020032, z70=28)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_04_120100():
    """Trophy: Abandoned people"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_04_x27(flag10=104020033, z70=30)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_04_120101():
    """Trophy: Abandoned people: Survival judgment"""
    """State 0,1: Trophy acquisition: Start"""
    IsPlayerInsidePoint(8, 20000000, 20000000, 1)
    CompareEventStatus(8, 111265, 1, 0)
    CompareEventStatus(8, 111355, 1, 0)
    CompareEventStatus(8, 111395, 1, 0)
    CompareEventStatus(8, 111099, 1, 0)
    assert ConditionGroup(8)
    """State 4: Dragon Miko: Single Survival_SubState"""
    call = event_m10_04_x71(z21=104020)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: Ladder Shop: Emigration survival_SubState"""
        call = event_m10_04_x72(z18=104050, z19=103551, z20=102165)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 6: Broken spirited warrior: Single survival _SubState"""
            call = event_m10_04_x71(z21=104140)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                """State 7: Map writing: Emigration survival_SubState"""
                call = event_m10_04_x72(z18=104180, z19=103681, z20=102460)
                if call.Get() == 1:
                    pass
                elif call.Get() == 0:
                    """State 8: Yorozu Baba: Emigration Survival_SubState"""
                    call = event_m10_04_x72(z18=104210, z19=103711, z20=102521)
                    if call.Get() == 1:
                        pass
                    elif call.Get() == 0:
                        """State 9: Armor Shop: Single Survival_SubState"""
                        call = event_m10_04_x71(z21=104250)
                        if call.Get() == 1:
                            pass
                        elif call.Get() == 0:
                            """State 10: Material shop: Emigration survival_SubState"""
                            call = event_m10_04_x72(z18=104260, z19=103761, z20=102625)
                            if call.Get() == 1:
                                pass
                            elif call.Get() == 0:
                                """State 11: Magician: Immigration Survival_SubState"""
                                call = event_m10_04_x72(z18=104270, z19=103771, z20=102650)
                                if call.Get() == 1:
                                    pass
                                elif call.Get() == 0:
                                    """State 12: Blacksmith: Single Survival_SubState"""
                                    call = event_m10_04_x71(z21=104280)
                                    if call.Get() == 1:
                                        pass
                                    elif call.Get() == 0:
                                        """State 13: Trophy: Survival of Magician Migration_SubState"""
                                        call = event_m10_04_x73(z15=104300, z16=103801, z17=102722)
                                        if call.Get() == 1:
                                            pass
                                        elif call.Get() == 0:
                                            """State 14: Miracle People: Emigration Survival_SubState"""
                                            call = event_m10_04_x72(z18=104320, z19=103821, z20=102765)
                                            if call.Get() == 1:
                                                pass
                                            elif call.Get() == 0:
                                                """State 3: Trophy acquisition: flag setting"""
                                                SetEventFlag(104020033, 1)
                                                CompareEventFlag(0, 104020033, 1)
                                                assert ConditionGroup(0)
    """State 2: Trophy acquisition: System: End"""
    EndMachine()
    Quit()

def event_m10_04_120150():
    """Trophy: Miser"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_04_x27(flag10=104020034, z70=35)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_04_4000000():
    """[DC] Pig reincarnation"""
    """State 0,2: [DC] [Preset] Pig Reincarnation_SubState"""
    assert event_m10_04_x94(flag1=104000002, flag2=104000001, z2=1000, z3=1001, z4=1002, z5=1010, z6=1011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_04_4001000():
    """[DC] Treasure box changes mimic"""
    """State 0,2: [DC] [Preset] Treasure box changes mimic_SubState"""
    # bonfire:4650:The Far Fire
    assert event_m10_04_x98(bonfire1=4650, z1=10045060)
    """State 1: Finish"""
    EndMachine()
    Quit()

