# -*- coding: utf-8 -*-
def event_m20_11_1000():
    """Connection flag ON"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m20_11_x45(z79=105430, z80=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_11_2000():
    """Treasure corpse branch"""
    """State 0,2: [Preset] Treasure corpse branch _SubState"""
    assert event_m20_11_x86(z41=20111330, z42=20116130, z43=71)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_3000():
    """Boss: Beautiful voice frog battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m20_11_x5(flag10=211000081, z107=300000, z108=300000, z109=101, z110=2011000, z111=211020080,
            mode3=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_3010():
    """Beautiful voice frog singing voice"""
    """State 0,3: [Preset] Voice frog singing voice_SubState"""
    call = event_m20_11_x97(flag3=211000081, z30=201120002, z31=802, z32=301000, z33=301001, z34=301010,
                            z35=301011)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m20_11_3020():
    """Beautiful voice frog singing_flag"""
    """State 0,2: [Preset] Beautiful frog singing voice_flag_SubState"""
    assert event_m20_11_x110(flag1=211000081, z24=802, z25=211020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4000():
    """Elevator"""
    """State 0,2: Has the initialization event ended?"""
    assert EventEnded(4030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m20_11_x12(z74=20111400, z75=400010, z76=400000, z77=20111410, z78=20111420)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_11_4010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_11_x17(z104=20111400, z105=20111410, z106=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_11_4020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_11_x17(z104=20111400, z105=20111420, z106=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_11_4030():
    """Elevator_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m20_11_x25(z101=20111400, z102=40, flag9=211000020, z103=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_5000():
    """Altar of the living"""
    """State 0,2: [Preset] Living Altar_SubState"""
    assert event_m20_11_x82()
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_11_6000():
    """Door of the living"""
    """State 0,2: [Preset] Door of the living person_SubState"""
    assert event_m20_11_x77(z39=20110480, z40=600000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_7000():
    """Door of the dead"""
    """State 0,2: [Preset] Dead Door_SubState"""
    assert event_m20_11_x76(z36=20110485, z37=700000, z38=211000010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_7010():
    """Banshee's Ascension"""
    """State 0,2: [Preset] Banshee's Ascension_SubState"""
    assert event_m20_11_x105(z26=4100, flag2=211000010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_8000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m20_11_x32(z96=20111500)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_8010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m20_11_x36(z94=20111500, val2=20110000, z95=0.6, val3=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_8020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_11_x38(z81=20111510, z82=20, z83=802000, z84=0, z85=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_9000():
    """Get King Soul"""
    """State 0,2: [Preset] _SubState to acquire the king's soul"""
    assert event_m20_11_x101(z27=100904, z28=20115070, z29=20115500)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_14000():
    """Photoworm that reacts to enemy and PC approach_cave_1"""
    """State 0,2: [Preset] Photoworm_Girl_SubState reacts to enemy and PC approach"""
    assert event_m20_11_x120(z5=5, z6=2305, z7=20114728, z8=211000015, z9=16010, z10=104220)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_14010():
    """The photoworm that reacts to the enemy and PC approach_cave_2"""
    """State 0,2: [Preset] Photoworm_Girl_SubState reacts to enemy and PC approach"""
    assert event_m20_11_x120(z5=5, z6=2305, z7=20114729, z8=211000015, z9=16010, z10=104220)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_14020():
    """Photoworm reacts to enemy and PC approach_cave_3"""
    """State 0,2: [Preset] Photoworm_Girl_SubState reacts to enemy and PC approach"""
    assert event_m20_11_x120(z5=5, z6=2305, z7=20114730, z8=211000015, z9=16010, z10=104220)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15000():
    """Photoworm_Plaza_1 reacts to enemy and PC approach"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4250, z15=20114606, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15010():
    """Photoworm _Square_2 reacts to enemy and PC approach"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4250, z15=20114607, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15020():
    """The photoworm that reacts to the enemy and the PC approach_Plaza_3"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4220, z15=20114608, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15030():
    """The photoworm that responds to the enemy and PC approach_Plaza_4"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4250, z15=20114609, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15040():
    """The photoworm that reacts to the enemy and PC approach_Square_5"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4220, z15=20114610, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15050():
    """The photoworm that responds to the enemy and PC approach_Square_6"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4250, z15=20114611, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_15060():
    """The photoworm that reacts to the enemy and PC approach_Plaza_7"""
    """State 0,2: [Preset] Photoworm_Frog_SubState reacts to enemy and PC approach"""
    assert (event_m20_11_x117(z13=5, z14=4220, z15=20114612, z16=211000016, z17=16010, z18=211000081,
            z19=802))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_16000():
    """Lizard extinction judgment_cave"""
    """State 0,2: [Preset] lizard extinction judgment_4 bodies_SubState"""
    assert event_m20_11_x118(z12=211000015)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_16010():
    """Lizard extinction judgment _ open space"""
    """State 0,2: [DC] [Preset] Lizard extinction judgment_3 bodies_SubState"""
    assert event_m20_11_x122(z1=211000016)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_80000():
    """Fireworks for regeneration 01_Upper tower of entrance tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_11_x53(z65=2011000, z66=2011099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_81000():
    """Fireworks for Regeneration 02_ A collapsed building next to aquatic plants"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_11_x53(z65=2011100, z66=2011199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_82000():
    """Rebirth Fire 03_Cave to parent tree"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_11_x53(z65=2011200, z66=2011299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_83000():
    """Rebirth Fire 04_Lower tower in front of the living altar"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_11_x53(z65=2011300, z66=2011399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_x0(z124=_, z125=_, z126=_, z127=_):
    """[Lib] NPC: Grave Placement: General purpose
    z124: Death map: Global event flag
    z125: Tomb: OBJ instance ID
    z126: Tomb move to: Generator ID
    z127: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z124, 1)
    IsGraveGeneratable(8, z127, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z125, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z125, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m20_11_x1(z121=_, z122=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z121: Global: death flag
    z122: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z122, 10, 0)
    CompareObjState(1, z122, 20, 0)
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
    IsObjSearched(0, z122)
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

def event_m20_11_x2(z119=_, z120=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z119: Area other flags: Ghost appearance
    z120: Area other flags: Conversation start
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
    SetEventFlag(z119, 1)
    CompareEventFlag(0, z119, 1)
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
    SetEventFlag(z120, 1)
    CompareEventFlag(0, z120, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m20_11_x3(z119=_, z120=_, z121=_, z122=_, z123=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z119: Ghost Appearance: Area Other Flag
    z120: Conversation start: Area and other flags
    z121: Death: Global event flag
    z122: Tomb: OBJ instance ID
    z123: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z123, 1, 0)
    CompareEventFlag(9, z119, 1)
    CompareObjState(9, z122, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z120, 1)
        CompareEventFlag(0, z120, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m20_11_x1(z121=z121, z122=z122, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m20_11_x2(z119=z119, z120=z120, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m20_11_x4(z112=_, z113=_, z114=_, z115=201110002, z116=_, z117=_, z118=_):
    """[Lib] Bard Girl: Hoarseness
    z112: Death: Global event flag
    z113: Hoarseness: Occurrence: Point ID
    z114: Hoar: Stop: Point ID
    z115: Sound ID
    z116: Hoarseness: Reoccurrence point ID
    z117: Dead behavior: Area and other flags
    z118: Generator ID
    """
    """State 0,1: Hoar: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 8: Hoarseness: Death determination"""
        CompareEventFlag(0, z112, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Hoar: Branch: Wait"""
            CompareEventFlag(0, z112, 1)
            IsPlayerInsidePoint(1, z114, z114, 1)
            IsPlayerInsidePoint(8, z113, z113, 1)
            IsPlayerInsidePoint(8, z114, z114, 0)
            IsPlayerInsidePoint(2, z113, z113, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 7: Hoar: Stopping area intrusion: Stop playback"""
                SetEventFlag(z117, 0)
                StopSoundFollowingGenerator(z118)
                CompareEventFlag(0, z117, 0)
                """State 6: Hoar: Stop area invading: Waiting"""
                IsPlayerInsidePoint(0, z116, z116, 0)
                CompareEventFlag(1, z112, 1)
                if ConditionGroup(1):
                    pass
                elif ConditionGroup(0):
                    """State 4: Hoarseness: System: Rerun"""
                    Label('L0')
                    RestartMachine()
                    Quit()
            elif ConditionGroup(8):
                """State 9: Hoar: Play area intrusion: Play"""
                SetEventFlag(z117, 1)
                CompareEventFlag(0, z117, 1)
                PlaySoundFollowingGenerator(5, z115, z118)
                assert ConditionGroup(0)
                """State 3: Hoar: Play area intrusion: Standby"""
                IsPlayerInsidePoint(0, z114, z114, 1)
                IsPlayerInsidePoint(1, z113, z113, 0)
                CompareEventFlag(2, z112, 1)
                if ConditionGroup(2):
                    pass
                elif ConditionGroup(0):
                    Goto('L0')
                elif ConditionGroup(1):
                    Goto('L0')
            elif ConditionGroup(2):
                """State 10: Hoar: Out of playback area Outside: Stop playback"""
                SetEventFlag(z117, 0)
                StopSoundFollowingGenerator(z118)
                CompareEventFlag(0, z117, 0)
                assert ConditionGroup(0)
                """State 11: Hoar: Playback area intrusion Outside: Standby"""
                IsPlayerInsidePoint(0, z113, z113, 1)
                CompareEventFlag(1, z112, 1)
                if ConditionGroup(1):
                    pass
                elif ConditionGroup(0):
                    Goto('L0')
    """State 5: Hoarseness: System: End"""
    StopSoundFollowingGenerator(z118)
    EndMachine()
    Quit()
    """Unused"""
    """State 12: End state"""
    return 0

def event_m20_11_x5(flag10=211000081, z107=300000, z108=300000, z109=101, z110=2011000, z111=211020080,
                    mode3=0):
    """[Lib] [Preset] Boss Battle Start
    flag10: Boss destruction flag
    z107: Start point ID
    z108: End point ID
    z109: Sound ID
    z110: Boss Battle ID
    z111: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_11_x6(flag10=flag10)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m20_11_x7(z107=z107, z108=z108)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m20_11_x8(z109=z109, z110=z110, z111=z111)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_11_x9()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_11_x10(z110=z110)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m20_11_x11(z109=z109, z110=z110, z111=z111, mode3=mode3)
    """State 7: End state"""
    return 0

def event_m20_11_x6(flag10=211000081):
    """[Reproduction] Boss Battle_Start
    flag10: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag10) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_11_x7(z107=300000, z108=300000):
    """[Condition] Boss Battle_Start
    z107: Start point ID
    z108: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z107, z108, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z107, z108, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x8(z109=101, z110=2011000, z111=211020080):
    """[Execution] Boss Battle_Start
    z109: Sound ID
    z110: Boss Battle ID
    z111: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z109)
    """State 1: Boss battle start notification"""
    StartBossFight(z110)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z111, 1)
    """State 4: End state"""
    return 0

def event_m20_11_x9():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x10(z110=2011000):
    """[Condition] Boss Battle_End Judgment
    z110: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z110, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x11(z109=101, z110=2011000, z111=211020080, mode3=0):
    """[Execute] Boss Battle_End
    z109: Sound ID
    z110: Boss Battle ID
    z111: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z111, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z110)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode3) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z109)
    """State 5: End state"""
    return 0

def event_m20_11_x12(z74=20111400, z75=400010, z76=400000, z77=20111410, z78=20111420):
    """[Lib] [Preset] Elevator
    z74: OBJ instance ID of the elevator
    z75: On elevator point ID_
    z76: Elevator point ID_below
    z77: Upper lever OBJ instance ID
    z78: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m20_11_x13()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m20_11_x14(z74=z74, z75=z75, z76=z76, z77=z77, z78=z78)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m20_11_x47(z74=z74, z76=z76)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m20_11_x46(z74=z74, z75=z75)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m20_11_x15(z74=z74, z75=z75)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m20_11_x16(z74=z74, z76=z76)
    """State 7: End state"""
    return 0

def event_m20_11_x13():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x14(z74=20111400, z75=400010, z76=400000, z77=20111410, z78=20111420):
    """[Condition] Elevator
    z74: Elevator OBJ instance ID
    z75: On elevator point ID_
    z76: Elevator point ID_below
    z77: Upper lever OBJ instance ID
    z78: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z74, 10, 0)
    CompareObjState(1, z74, 40, 0)
    CompareObjState(2, z74, 80, 0)
    CompareObjState(2, z74, 41, 0)
    CompareObjState(3, z74, 70, 0)
    CompareObjState(3, z74, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z76, z76, 1)
        CompareObjState(0, z77, 74, 0)
        CompareObjState(0, z77, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z75, z75, 1)
        CompareObjState(0, z78, 74, 0)
        CompareObjState(0, z78, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m20_11_x15(z74=20111400, z75=400010):
    """[Execution] Elevator_Rise
    z74: Elevator OBJ instance ID
    z75: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z74, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z74, 30, 0)
    IsPlayerInsidePoint(8, z75, z75, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z74, 71)
    assert CompareObjStateId(z74, 40, 0)
    """State 4: End state"""
    return 0

def event_m20_11_x16(z74=20111400, z76=400000):
    """[Execution] Elevator_Descent
    z74: Elevator OBJ instance ID
    z76: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z74, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z74, 41, 0)
    IsPlayerInsidePoint(8, z76, z76, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z74, 81)
    assert CompareObjStateId(z74, 10, 0)
    """State 4: End state"""
    return 0

def event_m20_11_x17(z104=20111400, z105=_, z106=_):
    """[Lib] [Preset] Elevator lever
    z104: OBJ instance ID of the elevator
    z105: Lever OBJ instance ID
    z106: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m20_11_x18()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m20_11_x19(z104=z104, z105=z105, z106=z106)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m20_11_x20(z104=z104, z105=z105, z106=z106)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m20_11_x21(z104=z104, z105=z105, z106=z106)
    """State 5: Rerun"""
    return 0

def event_m20_11_x18():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x19(z104=20111400, z105=_, z106=_):
    """[Condition] Elevator lever_use judgment
    z104: OBJ instance ID of the elevator
    z105: Lever OBJ instance ID
    z106: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z104, z106, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m20_11_x20(z104=20111400, z105=_, z106=_):
    """[Execution] Elevator lever_Key guide valid
    z104: OBJ instance ID of the elevator
    z105: Lever OBJ instance ID
    z106: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z105, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z104, z106, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_11_x21(z104=20111400, z105=_, z106=_):
    """[Execute] Elevator lever_key guide disabled
    z104: OBJ instance ID of the elevator
    z105: Lever OBJ instance ID
    z106: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z105, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z104, z106, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_11_x22(flag9=211000020):
    """[Lib] [Reproduction] Elevator_Initialization
    flag9: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag9) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m20_11_x23():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m20_11_x24(z101=20111400, z102=40, flag9=211000020, z103=40):
    """[Lib] [Execution] Elevator_Initialization
    z101: Elevator OBJ instance ID
    z102: Initial position OBJ state ID
    flag9: Initialization completion flag
    z103: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z101, z102)
    assert CompareObjStateId(z101, z103, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag9, 1)
    """State 3: End state"""
    return 0

def event_m20_11_x25(z101=20111400, z102=40, flag9=211000020, z103=40):
    """[Lib] [Preset] Elevator_Initialization
    z101: Elevator OBJ instance ID
    z102: Initial position OBJ state ID
    flag9: Initialization completion flag
    z103: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m20_11_x22(flag9=flag9)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m20_11_x23()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m20_11_x24(z101=z101, z102=z102, flag9=flag9, z103=z103)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m20_11_x26(z96=20111500):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z96: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z96, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z96, 10)
        assert CompareObjStateId(z96, 10, 0)
    elif CompareObjStateId(z96, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z96, 74, 1) and CompareObjStateId(z96, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m20_11_x27(z96=20111500, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z96: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z96)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m20_11_x28(z96=20111500, z98=38, z99=12, z100=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z96: Object instance ID
    z98: Key guide type
    z99: Event action
    z100: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z96, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z96, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z96, 30)
        assert CompareObjStateId(z96, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z96, z98, z99)
        assert PlayerIsInEventAction(z99) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z99, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z96, 74, 0)
        CompareObjState(1, z96, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z100)
            assert CompareObjStateId(z96, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z96, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m20_11_x29(z96=20111500, z97=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z96: Object instance ID
    z97: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z96, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m20_11_x30(z96=20111500):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z96: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z96, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x31():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x32(z96=20111500):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z96: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m20_11_x26(z96=z96)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m20_11_x30(z96=z96)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m20_11_x31()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m20_11_x27(z96=z96, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m20_11_x28(z96=z96, z98=38, z99=12, z100=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m20_11_x29(z96=z96, z97=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m20_11_x33(z94=20111500, val2=20110000):
    """[Reproduction] Hidden door 1_face SFX
    z94: OBJ instance ID of the bug key
    val2: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z94, 20, 0):
        pass
    else:
        Goto('L0')
    """State 2: Event light reproduction judgment"""
    if (not val2) != 0:
        pass
    else:
        """State 3: Event light ON"""
        SetPointLightEnabled(val2, 1, 0)
    """State 6: Hidden door status judgment"""
    if CompareOwnObjStateId(10, 0):
        """State 7: Hidden door lighting: 30"""
        ChangeOwnObjState(30)
        assert CompareOwnObjStateId(30, 0)
    else:
        pass
    """State 8: Activated"""
    return 0
    """State 5: Event light usage judgment"""
    Label('L0')
    if (not val2) != 0:
        pass
    else:
        """State 4: Event light OFF"""
        SetPointLightEnabled(val2, 0, 0)
    """State 9: Not started"""
    return 1

def event_m20_11_x34(z94=20111500):
    """[Conditions] Hidden door 1_Face SFX
    z94: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z94, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x35(z94=20111500, val2=20110000, z95=0.6, val3=1.5):
    """[Execution] Hidden door 1_Face SFX
    z94: OBJ instance ID of the bug key
    val2: Event light ID
    z95: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,2: Event light usage judgment"""
    if (not val2) != 0:
        """State 5: Wait until face SFX playback"""
        assert (GetStateTime() > val3) != 0
        """State 4: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    else:
        """State 1: Event light ON"""
        SetPointLightEnabled(val2, 1, z95)
        assert (GetStateTime() > val3) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m20_11_x36(z94=20111500, val2=20110000, z95=0.6, val3=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z94: OBJ instance ID of the bug key
    val2: Event light ID
    z95: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m20_11_x33(z94=z94, val2=val2)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m20_11_x34(z94=z94)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m20_11_x35(z94=z94, val2=val2, z95=z95, val3=val3)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m20_11_x37(z86=5300, z87=0, z88=15, z89=211000030, z90=0, z91=1600, z92=6, z93=4000010):
    """[Lib] Character: Petrochemical: Key guide
    z86: generator
    z87: Death: Global event flag
    z88: Event action
    z89: Petrified: Area and other flags
    z90: Petrified: Global event flag
    z91: Key guide parameters
    z92: Petrification start state ID
    z93: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z86, z92, 0)
    CompareEventStatus(8, z93, 1, 0)
    CompareEventFlag(2, z89, 1)
    CompareEventFlag(3, z90, 1)
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
    CreateKeyGuideArea(34, z91)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z86)
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
            DisplayOwnYesNoMenu(1002, 3, 220, 2, 60537000, 0)
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
                PlayerActionRequest(z88)
                IsPlayerPlayingMotion(0, z88, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z89, 1)
                CompareEventFlag(0, z89, 1)
                SetEventFlag(z90, 1)
                CompareEventFlag(1, z90, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z88, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()
    Quit()

def event_m20_11_x38(z81=20111510, z82=20, z83=802000, z84=0, z85=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z81: Object instance ID
    z82: OBJ state ID
    z83: Navimesh switching point ID
    z84: Additional attributes
    z85: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m20_11_x39(z81=z81, z82=z82, z83=z83, z85=z85, z84=z84)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m20_11_x40(z81=z81, z82=z82, z83=z83)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m20_11_x41(z81=z81, z82=z82, z83=z83, z84=z84, z85=z85)
    """State 4: End state"""
    return 0

def event_m20_11_x39(z81=20111510, z82=20, z83=802000, z85=2, z84=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z81: Target OBJ instance ID
    z82: Target OBJ state ID
    z83: Navimesh switching point ID
    z85: Additional attributes
    z84: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z81, z82, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z83, z85)
        DeleteNavimeshAttribute(z83, z84)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m20_11_x40(z81=20111510, z82=20, z83=802000):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z81: Target OBJ instance ID
    z82: Target OBJ state ID
    z83: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z81, z82, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x41(z81=20111510, z82=20, z83=802000, z84=0, z85=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z81: Target OBJ instance ID
    z82: Target OBJ state ID
    z83: Navimesh switching point ID
    z84: Additional attributes
    z85: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z83, z84)
    DeleteNavimeshAttribute(z83, z85)
    """State 2: End state"""
    return 0

def event_m20_11_x42():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x43():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x44(z79=105430, z80=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z79: Global event flag for connection
    z80: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z79, z80)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z79, z80)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_11_x45(z79=105430, z80=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z79: Global event flag for connection
    z80: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m20_11_x42()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m20_11_x43()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m20_11_x44(z79=z79, z80=z80)
    """State 4: End state"""
    return 0

def event_m20_11_x46(z74=20111400, z75=400010):
    """[Execution] Elevator_Return switch after lift
    z74: Elevator OBJ instance ID
    z75: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z74, 30, 0)
    IsPlayerInsidePoint(8, z75, z75, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z74, 71)
    assert CompareObjStateId(z74, 40, 0)
    """State 3: End state"""
    return 0

def event_m20_11_x47(z74=20111400, z76=400000):
    """[Execution] Elevator_Return switch after descending
    z74: Elevator OBJ instance ID
    z76: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z74, 41, 0)
    IsPlayerInsidePoint(8, z76, z76, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z74, 81)
    assert CompareObjStateId(z74, 10, 0)
    """State 3: End state"""
    return 0

def event_m20_11_x48(z68=5300, z69=0, z70=211000030, z71=0, z72=0, z73=4000000):
    """[Lib] Character: Petrified: Appearance setting
    z68: Generator ID
    z69: Death: Global event flag
    z70: Petrified: Area and other flags
    z71: Petrified: Global event flag
    z72: Startup state
    z73: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z68)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z69, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z70, 1)
                CompareEventFlag(1, z71, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z68, z72)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m20_11_x49(z67=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z67: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z67)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m20_11_x50():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x51(z65=_, z66=_):
    """[Lib] [execute] Rebirth fire
    z65: Flag start ID
    z66: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z65, z66, 0)
    """State 2: End state"""
    return 0

def event_m20_11_x52():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x53(z65=_, z66=_):
    """[Lib] [Preset] Rebirth
    z65: Flag start ID
    z66: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m20_11_x50()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m20_11_x52()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m20_11_x51(z65=z65, z66=z66)
    """State 4: End state"""
    return 0

def event_m20_11_x54(flag7=211000030, flag8=0, z64=2, z63=0, z62=6000020):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    flag7: Other flags
    flag8: Global flag
    z64: Additional attributes
    z63: Delete attribute
    z62: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(flag7) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(flag8) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z62, z64)
        DeleteNavimeshAttribute(z62, z63)
        """State 3: Flag OFF"""
        return 0

def event_m20_11_x55(flag7=211000030, flag8=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    flag7: Other flags
    flag8: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, flag7, 1)
    CompareEventFlag(0, flag8, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m20_11_x56(z62=6000020, z63=0, z64=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z62: Navimesh switching point ID
    z63: Additional attributes
    z64: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z62, z63)
    DeleteNavimeshAttribute(z62, z64)
    """State 2: End state"""
    return 0

def event_m20_11_x57(z62=6000020, z63=0, z64=2, flag7=211000030, flag8=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z62: Navimesh switching point ID
    z63: Additional attributes
    z64: Delete attribute
    flag7: Other flags
    flag8: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m20_11_x54(flag7=flag7, flag8=flag8, z64=z64, z63=z63, z62=z62)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m20_11_x55(flag7=flag7, flag8=flag8)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m20_11_x56(z62=z62, z63=z63, z64=z64)
    """State 4: End state"""
    return 0

def event_m20_11_x58(z58=10000000, z59=660, z60=0, z61=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z58: Summon range
    z59: Generator ID
    z60: Appearance: Minimum time
    z61: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z58, z58, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z60, 3, z61)
        IsPlayerInsidePoint(1, z58, z58, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z59)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m20_11_x59(flag4=211020001, flag5=211000002):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag4: Lottery determination flag
    flag5: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag5) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag4) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m20_11_x60(z44=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z44: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z44, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m20_11_x61(flag4=211020001, z45=3, z46=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag4: Lottery determination flag
    z45: Number of appearance judgment points
    z46: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag4, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z45)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z46, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m20_11_x62(flag4=211020001, z44=14, flag5=211000002, z45=3, z46=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag4: Lottery determination flag
    z44: Random number comparison value
    flag5: Defeat flag
    z45: Number of appearance judgment points
    z46: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m20_11_x59(flag4=flag4, flag5=flag5)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m20_11_x60(z44=z44)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m20_11_x61(flag4=flag4, z45=z45, z46=z46)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m20_11_x75(flag4=flag4, z46=z46)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m20_11_x63(val1=_, z55=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z55: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z55) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m20_11_x64(z51=_, z52=0, z53=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z51: Appearance judgment point ID
    z52: Minimum appearance time
    z53: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z51, z51, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z52, 3, z53)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m20_11_x65(z54=965, z56=_, z57=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z54: Generator ID
    z56: Appearance start point ID
    z57: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z54, z56, z57)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z54)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m20_11_x66(flag6=211000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag6: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag6) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m20_11_x67(z51=_, z52=0, z53=5, z54=965, val1=_, z55=10, z56=_, z57=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z51: Intrusion detection point ID
    z52: Minimum appearance time
    z53: Maximum time to appear
    z54: Generator ID
    val1: Appearance judgment number
    z55: Lottery result point variable
    z56: Appearance start point ID
    z57: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m20_11_x63(val1=val1, z55=z55)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m20_11_x64(z51=z51, z52=z52, z53=z53)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m20_11_x65(z54=z54, z56=z56, z57=z57)
    """State 4: Finish"""
    return 0

def event_m20_11_x68(z49=965, mode1=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z49: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z49)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m20_11_x69(flag6=211000002, z50=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag6: Defeat flag
    z50: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag6, 1)
    """State 2: Head flag judgment"""
    CompareEventFlag(0, 102750, 1)
    if ConditionGroup(0):
        """State 4: Hand flag judgment"""
        CompareEventFlag(0, 102752, 1)
        if ConditionGroup(0):
            """State 5: Foot flag judgment"""
            CompareEventFlag(0, 102753, 1)
            if ConditionGroup(0):
                """State 6: Torso flag judgment"""
                CompareEventFlag(0, 102751, 1)
                if ConditionGroup(0):
                    """State 10: Weapon flag ON"""
                    SetEventFlag(z50, 1)
                else:
                    """State 7: Torso flag ON"""
                    SetEventFlag(102751, 1)
            else:
                """State 9: Foot flag ON"""
                SetEventFlag(102753, 1)
        else:
            """State 8: Hand flag ON"""
            SetEventFlag(102752, 1)
    else:
        """State 3: Head flag ON"""
        SetEventFlag(102750, 1)
    """State 11: End state"""
    return 0

def event_m20_11_x70(flag6=211000002, z49=965, mode1=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag6: Defeat flag
    z49: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m20_11_x66(flag6=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m20_11_x68(z49=z49, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m20_11_x69(flag6=flag6, z50=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m20_11_x69(flag6=flag6, z50=102755)
    """State 5: End state"""
    return 0

def event_m20_11_x71(z47=_, z48=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z47: Generator ID
    z48: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z47, z48)
    """State 2: End state"""
    return 0

def event_m20_11_x72(z47=_, z48=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z47: Generator ID
    z48: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z47, z48, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_11_x73(z47=_):
    """[Lib] [DC] [Condition] Transparent characters
    z47: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z47)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x74(z47=_, z48=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z47: Generator ID
    z48: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m20_11_x72(z47=z47, z48=z48)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m20_11_x73(z47=z47)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m20_11_x71(z47=z47, z48=z48)
    """State 4: End state"""
    return 0

def event_m20_11_x75(flag4=211020001, z46=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag4: Lottery determination flag
    z46: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag4, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z46, 0)
    """State 3: End state"""
    return 0

def event_m20_11_x76(z36=20110485, z37=700000, z38=211000010):
    """[Preset] Door of the dead
    z36: OBJ instance ID of the door
    z37: Navimesh change point ID
    z38: Banshee's Ascension Flag
    """
    """State 0,2: [Reproduction] Living / December Door_SubState"""
    call = event_m20_11_x88(z39=z36)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Door of the dead_SubState"""
        call = event_m20_11_x90(z36=z36, z38=z38)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 3: [Execution] Doors of living and dead people_Message display_SubState"""
            assert event_m20_11_x87(z39=z36)
            """State 1: Rerun"""
            RestartMachine()
            Quit()
    """State 5: End state"""
    return 0

def event_m20_11_x77(z39=20110480, z40=600000):
    """[Preset] Door of the living
    z39: OBJ instance ID of the door
    z40: Navimesh change point ID
    """
    """State 0,3: [Reproduction] Living / December Door_SubState"""
    call = event_m20_11_x88(z39=z39)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Door of living person_SubState"""
        call = event_m20_11_x89(z39=z39)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 2: [Execution] Doors of living and dead people_Message display_SubState"""
            assert event_m20_11_x87(z39=z39)
            """State 1: Rerun"""
            RestartMachine()
            Quit()
    """State 5: End state"""
    return 0

def event_m20_11_x78():
    """[Reproduction] The living altar _ Sky"""
    """State 0,1: State"""
    ChangeOwnObjState(30)
    """State 2: End state"""
    return 0

def event_m20_11_x79():
    """[Condition] Altar of the living"""
    """State 0,1: Key guide access standby"""
    IsObjSearched(0, 20111200)
    assert ConditionGroup(0)
    """State 2: Are the conditions met?"""
    IsChrDead(0, 20)
    IsChrDead(0, 25)
    ComparePlayerSinLevel(0, 2, 0)
    IsPlayerHollow(0, 0, 1)
    # goods:60151000:Human Effigy
    DoesPlayerHaveItem(0, 60151000, 1, 3, 1, 1, 1)
    # goods:60151000:Human Effigy
    IsItemLeft(0, 60151000, 1)
    if ConditionGroup(0):
        """State 4: Nothing happens"""
        return 1
    else:
        """State 3: End state"""
        return 0

def event_m20_11_x80():
    """[Execution] Living Altar_Back to Living"""
    """State 0,1: Prayer action"""
    PlayerActionRequest(6)
    assert (GetStateTime() > 4) != 0
    """State 2: Special effects: Return to the living"""
    SetPlayerSpEffect(100000010, 19, 4)
    """State 3: End of prayer action"""
    EndPlayerActionRequest()
    """State 4: End state"""
    return 0

def event_m20_11_x81():
    """[Execution] Living Altar_Nothing happens"""
    """State 0,1: Prayer action"""
    PlayerActionRequest(6)
    assert (GetStateTime() > 4) != 0
    """State 2: Dialog display: Nothing happened"""
    # action:1113:"Alas, nothing happened"
    DisplayOwnOkMenu(1113, 10, 0, 190, 0, 0, 0)
    """State 3: End of prayer action"""
    EndPlayerActionRequest()
    """State 4: End state"""
    return 0

def event_m20_11_x82():
    """[Preset] Living Altar"""
    """State 0,1: [Reproduction] Living Altar_Sky_SubState"""
    assert event_m20_11_x78()
    """State 2: [Conditions] Living Altar_SubState"""
    call = event_m20_11_x79()
    if call.Get() == 1:
        """State 4: [Execution] Living Altar_Nothing happens_SubState"""
        assert event_m20_11_x81()
    elif call.Done():
        """State 3: [Execution] Altar of the living_Return to the living_SubState"""
        assert event_m20_11_x80()
    """State 5: End state"""
    return 0

def event_m20_11_x83():
    """[Reproduction] Treasure corpse branch _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x84(z41=20111330):
    """[Condition] Treasure corpse branch
    z41: Branch instance ID
    """
    """State 0,1: Wait for branch destruction"""
    IsObjBroken(0, z41, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x85(z42=20116130, z43=71):
    """[Execution] Treasure corpse branch
    z42: Instance ID of treasure corpse
    z43: Falling state ID
    """
    """State 0,1: OBJ state transition: treasure corpse"""
    ChangeObjState(z42, z43)
    """State 2: End state"""
    return 0

def event_m20_11_x86(z41=20111330, z42=20116130, z43=71):
    """[Preset] Treasure corpse branch
    z41: Branch instance ID
    z42: Instance ID of treasure corpse
    z43: Falling state ID
    """
    """State 0,1: [Reproduction] Treasure corpse branch_sky_SubState"""
    assert event_m20_11_x83()
    """State 2: [Condition] Treasure corpse branch_SubState"""
    assert event_m20_11_x84(z41=z41)
    """State 3: [Execution] Treasure corpse branch _SubState"""
    assert event_m20_11_x85(z42=z42, z43=z43)
    """State 4: End state"""
    return 0

def event_m20_11_x87(z39=_):
    """[Execution] Doors of living and dead people_Message display
    z39: OBJ instance ID of the door
    """
    """State 0,1: Message display"""
    # action:1100:"Locked"
    DisplayOwnOkMenu(1100, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m20_11_x88(z39=_):
    """[Reproduction] Doors of living and dead
    z39: OBJ instance ID of the door
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z39, 30, 0):
        """State 3: Opened"""
        return 1
    else:
        """State 2: Not open"""
        return 0

def event_m20_11_x89(z39=20110480):
    """[Condition] Door of the living
    z39: OBJ instance ID of the door
    """
    """State 0,6: Did you destroy the king?"""
    CompareEventFlag(0, 100978, 1)
    if ConditionGroup(0):
        """State 1: Is the player living or dead?"""
        IsPlayerHollow(0, 0, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: The door cannot be opened or closed"""
            ChangeObjState(z39, 100)
            """State 4: Have you examined the door? Or did you become a living person?"""
            IsObjSearched(0, z39)
            IsPlayerHollow(1, 0, 1)
            if ConditionGroup(0):
                Goto('L0')
            elif ConditionGroup(1):
                pass
        """State 3: The door can be opened and closed"""
        ChangeObjState(z39, 10)
        """State 5: Did you open the door?"""
        CompareObjState(0, z39, 30, 0)
        assert ConditionGroup(0)
        """State 9: Opened the door"""
        return 0
    else:
        """State 7: Unopenable door_2"""
        ChangeObjState(z39, 100)
        """State 8: Have you examined the door?"""
        IsObjSearched(0, z39)
        assert ConditionGroup(0)
    """State 10: The door does not open"""
    Label('L0')
    return 1

def event_m20_11_x90(z36=20110485, z38=211000010):
    """[Condition] Door of the dead
    z36: OBJ instance ID of the door
    z38: Banshee's Ascension Flag
    """
    """State 0,1: Is the player living or dead?"""
    IsPlayerHollow(0, 0, 1)
    if ConditionGroup(0):
        """State 2: The door cannot be opened or closed"""
        Label('L0')
        ChangeObjState(z36, 100)
        """State 8: Have you examined the door?"""
        IsObjSearched(0, z36)
        assert ConditionGroup(0)
    else:
        """State 6: Have you lifted Banshee?"""
        CompareEventFlag(0, z38, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 7: Unopenable door_2"""
            ChangeObjState(z36, 100)
            """State 5: Have you examined the door? or Did Banshee Ascend?"""
            IsObjSearched(0, z36)
            CompareEventFlag(1, z38, 1)
            if ConditionGroup(0):
                Goto('L1')
            elif ConditionGroup(1):
                pass
        """State 3: The door can be opened and closed"""
        ChangeObjState(z36, 10)
        """State 4: Did you open the door? Or did you become a living person?"""
        CompareObjState(0, z36, 30, 0)
        IsPlayerHollow(1, 0, 1)
        if ConditionGroup(0):
            """State 10: Opened the door"""
            return 1
        elif ConditionGroup(1):
            Goto('L0')
    """State 9: The door does not open"""
    Label('L1')
    return 0

def event_m20_11_x91(flag3=211000081, z31=802):
    """[Reproduction] Voice of a beautiful frog
    flag3: Boss destruction flag
    z31: Generator ID
    """
    """State 0,1: Did you destroy the beautiful frog?"""
    if GetEventFlag(flag3) != 0:
        """State 2: Stop generator following sound"""
        StopSoundFollowingGenerator(z31)
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Not defeated"""
        return 0

def event_m20_11_x92(z32=301000, z33=301001):
    """[Conditions] Voice of a beautiful frog
    z32: Singing voice playback start point ID
    z33: Singing voice end point ID
    """
    """State 0,1: Did you break into the starting point?"""
    IsPlayerInsidePoint(0, z32, z33, 1)
    assert ConditionGroup(0)
    """State 2: Play singing voice"""
    return 0

def event_m20_11_x93(z30=201120002, z31=802):
    """[Execution] Voice frog singing voice
    z30: Sound ID
    z31: Frog generator ID
    """
    """State 0,1: Play generator-following sound"""
    PlaySoundFollowingGenerator(5, z30, z31)
    """State 2: End state"""
    return 0

def event_m20_11_x94():
    """[Reproduction] Voice of a beautiful voice frog_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x95(flag3=211000081, z31=802, z34=301010, z35=301011):
    """[Conditions] Voice frog singing voice_stop judgment
    flag3: Boss destruction flag
    z31: Generator ID
    z34: Singing stop point ID
    z35: Singing stop end point ID
    """
    """State 0,1: The or boss from the stop point destroyed the or boss that was released from the activation state."""
    IsPlayerInsidePoint(0, z34, z35, 0)
    CompareEventFlag(1, flag3, 1)
    CompareChrStartUpState(1, z31, 2, 1)
    if ConditionGroup(0):
        """State 2: Stop singing voice: restart"""
        return 0
    elif ConditionGroup(1):
        """State 3: Stop singing: End"""
        return 1

def event_m20_11_x96(z31=802):
    """[Execution] Voice frog singing voice_stop
    z31: Generator ID
    """
    """State 0,1: Stop generator following sound"""
    StopSoundFollowingGenerator(z31)
    """State 2: End state"""
    return 0

def event_m20_11_x97(flag3=211000081, z30=201120002, z31=802, z32=301000, z33=301001, z34=301010, z35=301011):
    """[Preset] Voice of a beautiful frog
    flag3: Boss destruction flag
    z30: Sound ID
    z31: Generator ID
    z32: Singing voice playback start point ID
    z33: Singing voice playback end point ID
    z34: Singing stop point ID
    z35: Singing stop end point ID
    """
    """State 0,1: [Reproduction] Voice frog singing voice_SubState"""
    call = event_m20_11_x91(flag3=flag3, z31=z31)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Conditions] Voice of a beautiful frog _SubState"""
        assert event_m20_11_x92(z32=z32, z33=z33)
        """State 3: [Execution] Voice frog singing voice_Play_SubState"""
        assert event_m20_11_x93(z30=z30, z31=z31)
        """State 2: [Reproduction] Voice frog singing voice_Sky_SubState"""
        assert event_m20_11_x94()
        """State 6: [Conditions] Voice frog singing voice_Stop judgment_SubState"""
        call = event_m20_11_x95(flag3=flag3, z31=z31, z34=z34, z35=z35)
        if call.Get() == 1:
            """State 7: [Execution] Voice frog singing voice_stop_2_SubState"""
            assert event_m20_11_x96(z31=z31)
        elif call.Get() == 0:
            """State 4: [Execution] Voice frog singing voice_Stop_SubState"""
            assert event_m20_11_x96(z31=z31)
            """State 9: Rerun"""
            return 1
    """State 8: Finish"""
    return 0

def event_m20_11_x98():
    """[Reproduction] Obtaining King's Soul _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x99(z28=20115070, z29=20115500):
    """[Conditions] Obtaining King's Soul
    z28: King Soul OBJ Instance ID
    z29: BEST_Wang Soul OBJ Instance ID
    """
    """State 0,1: Got King Soul?"""
    WasObjItemAcquired(0, z28, 1)
    WasObjItemAcquired(0, z29, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_11_x100(z27=100904):
    """[Run] Get King Soul
    z27: King's Soul Acquisition Global Event Flag
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(z27, 1)
    """State 2: End state"""
    return 0

def event_m20_11_x101(z27=100904, z28=20115070, z29=20115500):
    """[Preset] Acquire King's Soul
    z27: King's Soul Acquisition Global Event Flag
    z28: King Soul OBJ Instance ID
    z29: BEST_Wang Soul OBJ Instance ID
    """
    """State 0,1: [Reproduction] Get the king's soul_Sky_SubState"""
    assert event_m20_11_x98()
    """State 3: [Condition] _SubState to acquire the king's soul"""
    assert event_m20_11_x99(z28=z28, z29=z29)
    """State 2: [Execution] Get the king's soul_SubState"""
    assert event_m20_11_x100(z27=z27)
    """State 4: End state"""
    return 0

def event_m20_11_x102(flag2=211000010):
    """[Reproduction] Banshee's Ascension
    flag2: Ascension flag
    """
    """State 0,3: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you already ascended?"""
    if GetEventFlag(flag2) != 0:
        """State 5: Ascended"""
        return 1
    else:
        """State 1: Key guide creation"""
        CreateKeyGuideArea(34, 20119200)
        """State 4: Wait for decision to check"""
        return 0
    """State 6: Guest: Exit"""
    Label('L0')
    return 2

def event_m20_11_x103(z26=4100):
    """[Condition] Banshee Ascension
    z26: Banshee's generator ID
    """
    """State 0,1: Examined or died"""
    IsChrSearched(0, z26)
    IsChrDead(1, z26)
    if ConditionGroup(1):
        """State 3: Died"""
        return 1
    elif ConditionGroup(0):
        """State 2: Talked"""
        return 0

def event_m20_11_x104(flag2=211000010, z26=4100):
    """[Execution] Banshee's Ascension_Ascension
    flag2: Ascension flag
    z26: Banshee's generator ID
    """
    """State 0,1: Ascension flag ON"""
    SetEventFlag(flag2, 1)
    """State 2: Delete key guide"""
    DeleteKeyGuideArea()
    """State 5: Ascension SFX playback"""
    PlaySfxAtPoint(7010)
    """State 3: Waiting for the ascension to end"""
    CompareChrEzStateValue(0, z26, 7, 1, 0)
    assert ConditionGroup(0)
    """State 4: Delete character"""
    DeleteEnemyByGenerator(z26, 0)
    """State 6: End state"""
    return 0

def event_m20_11_x105(z26=4100, flag2=211000010):
    """[Preset] Banshee's Ascension
    z26: Banshee's generator ID
    flag2: Ascension flag
    """
    """State 0,1: [Reproduction] Banshee's Ascension_SubState"""
    call = event_m20_11_x102(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Banshee's Ascension_SubState"""
        call = event_m20_11_x103(z26=z26)
        if call.Get() == 1:
            """State 4: [Execution] Banshee's Ascension_Death_SubState"""
            assert event_m20_11_x106()
        elif call.Get() == 0:
            """State 2: [Execution] Banshee's Ascension_SubState"""
            assert event_m20_11_x104(flag2=flag2, z26=z26)
    """State 5: End state"""
    return 0

def event_m20_11_x106():
    """[Execution] Banshee's Ascension_Death"""
    """State 0,1: Delete key guide"""
    DeleteKeyGuideArea()
    """State 2: End state"""
    return 0

def event_m20_11_x107(flag1=211000081, z25=211020082, z24=802):
    """[Reproduction] Voice frog singing voice_flag
    flag1: Boss destruction flag
    z25: Frog singing flag
    z24: Generator ID
    """
    """State 0,1: Did you destroy the beautiful frog?"""
    if GetEventFlag(flag1) != 0:
        """State 2: Singing flag OFF"""
        SetEventFlag(z25, 0)
        """State 5: Defeated"""
        return 1
    else:
        """State 3: Singing flag ON"""
        SetEventFlag(z25, 1)
        """State 4: Not defeated"""
        return 0

def event_m20_11_x108(flag1=211000081, z24=802):
    """[Condition] Voice frog singing voice_flag
    flag1: Boss destruction flag
    z24: Generator ID
    """
    """State 0,1: Defeated the boss that the boss released from the activation state or"""
    CompareEventFlag(0, flag1, 1)
    CompareChrStartUpState(0, z24, 2, 1)
    assert ConditionGroup(0)
    """State 2: Stop singing: End"""
    return 0

def event_m20_11_x109(z25=211020082, z24=802):
    """[Execution] Voice frog singing voice_flag
    z25: Frog singing flag
    z24: Generator ID
    """
    """State 0,1: Frog singing voice flag OFF"""
    SetEventFlag(z25, 0)
    """State 2: End state"""
    return 0

def event_m20_11_x110(flag1=211000081, z24=802, z25=211020082):
    """[Preset] Beautiful Voice Frog Singing Voice_Flag
    flag1: Boss destruction flag
    z24: Generator ID
    z25: Frog singing flag
    """
    """State 0,1: [Reproduction] Voice frog singing voice_flag_SubState"""
    call = event_m20_11_x107(flag1=flag1, z25=z25, z24=z24)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Singing voice frog_flag_SubState"""
        assert event_m20_11_x108(flag1=flag1, z24=z24)
        """State 2: [Execution] Voice frog singing voice_flag_SubState"""
        assert event_m20_11_x109(z25=z25, z24=z24)
    """State 4: Finish"""
    return 0

def event_m20_11_x111(z9=16010, z7=_):
    """[Reproduction] Photoworm reacts to enemy and PC approach
    z9: Extinction event ID
    z7: Mitsu insect OBJ instance ID
    """
    """State 0,1: End of extinction event"""
    assert EventEnded(z9) != 0
    """State 2: Is the photoworm in its initial state?"""
    if CompareObjStateId(z7, 10, 1):
        """State 4: Spreading: End"""
        return 1
    else:
        """State 3: Spread waiting"""
        return 0

def event_m20_11_x112():
    """[Reproduction] Lizard extinction judgment_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_11_x113(z20=2302, z21=2303, z22=2304, z23=2305):
    """[Condition] Lizard extinction judgment_4 bodies
    z20: Generator ID ①
    z21: Generator ID ②
    z22: Generator ID ③
    z23: Generator ID ④
    """
    """State 0,1: Upper limit judgment of lizards"""
    IsChrMaxRespawnCount(8, z20, 1, 0)
    IsChrMaxRespawnCount(8, z21, 1, 0)
    IsChrMaxRespawnCount(8, z22, 1, 0)
    IsChrMaxRespawnCount(8, z23, 1, 0)
    if ConditionGroup(8):
        """State 2: extinction"""
        return 0
    else:
        """State 3: Not extinct"""
        return 1

def event_m20_11_x114(z1=_):
    """[Execution] lizard extinction judgment
    z1: Lizard extinction flag
    """
    """State 0,1: Extinction flag ON"""
    SetEventFlag(z1, 1)
    """State 2: End state"""
    return 0

def event_m20_11_x115(z7=_):
    """[Execution] Photoworm reacts to enemy and PC approach
    z7: Mitsu insect OBJ instance ID
    """
    """State 0,1: Flying animation playback"""
    ChangeObjState(z7, 70)
    assert CompareObjStateId(z7, 20, 0)
    """State 2: End state"""
    return 0

def event_m20_11_x116(z13=5, z14=_, z15=_, z16=211000016, z18=211000081, z19=802):
    """[Conditions] Photoworm_frog that reacts to enemy and PC approach
    z13: PC approach distance
    z14: Generator ID
    z15: Mitsu insect OBJ instance ID
    z16: Extinction flag
    z18: Frog Destruction Flag
    z19: Frog generator ID
    """
    """State 0,1: Photoworm spread test"""
    CompareChrEzStateValue(0, z14, 0, 0, 1)
    CompareObjPlayerDistance(0, z15, z13, 5)
    CompareEventFlag(0, z16, 1)
    CompareEventFlag(0, z18, 1)
    CompareChrStartUpState(0, z19, 2, 1)
    assert ConditionGroup(0)
    """State 2: Spread: End"""
    return 0

def event_m20_11_x117(z13=5, z14=_, z15=_, z16=211000016, z17=16010, z18=211000081, z19=802):
    """[Preset] Photoworm frog reacts to enemy and PC approach
    z13: PC approach distance
    z14: Generator ID
    z15: Mitsu insect OBJ instance ID
    z16: Extinction flag
    z17: Extinction event ID
    z18: Frog Destruction Flag
    z19: Frog generator ID
    """
    """State 0,1: [Reproduction] Photoworm_SubState reacts to enemy and PC approach"""
    call = event_m20_11_x111(z9=z17, z7=z15)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Photoworm_Frog_SubState reacts to enemy and PC approach"""
        assert event_m20_11_x116(z13=z13, z14=z14, z15=z15, z16=z16, z18=z18, z19=z19)
        """State 2: [Execution] Photoworm_SubState reacts to enemy and PC approach"""
        assert event_m20_11_x115(z7=z15)
    """State 4: Finish"""
    return 0

def event_m20_11_x118(z12=211000015):
    """[Preset] lizard extinction judgment_4 bodies
    z12: Lizard extinction flag
    """
    """State 0,1: [Reproduction] Lizard extinction judgment_sky_SubState"""
    assert event_m20_11_x112()
    """State 3: [Condition] Lizard extinction judgment_4 bodies_SubState"""
    call = event_m20_11_x113(z20=2302, z21=2303, z22=2304, z23=2305)
    if call.Get() == 0:
        """State 2: [Execution] Lizard extinction judgment_SubState"""
        assert event_m20_11_x114(z1=z12)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_11_x119(z11=5, z6=2305, z7=_, z8=211000015, z10=104220):
    """[Condition] Photoworm_girl reacts to enemy and PC approach
    z11: PC approach distance
    z6: Generator ID
    z7: Mitsu insect OBJ instance ID
    z8: Extinction flag
    z10: Girl death flag
    """
    """State 0,1: Photoworm spread test"""
    CompareChrEzStateValue(0, z6, 0, 0, 1)
    CompareObjPlayerDistance(0, z7, z11, 5)
    CompareEventFlag(0, z8, 1)
    CompareEventFlag(0, z10, 1)
    assert ConditionGroup(0)
    """State 2: Spread: End"""
    return 0

def event_m20_11_x120(z5=5, z6=2305, z7=_, z8=211000015, z9=16010, z10=104220):
    """[Preset] Mitsuguru_Girl reacts to enemy and PC approach
    z5: PC approach distance
    z6: Generator ID
    z7: Mitsu insect OBJ instance ID
    z8: Extinction flag
    z9: Extinction event ID
    z10: Girl death flag
    """
    """State 0,1: [Reproduction] Photoworm_SubState reacts to enemy and PC approach"""
    call = event_m20_11_x111(z9=z9, z7=z7)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Photoworm_Girl_SubState reacts to enemy and PC approach"""
        assert event_m20_11_x119(z11=5, z6=z6, z7=z7, z8=z8, z10=z10)
        """State 2: [Execution] Photoworm_SubState reacts to enemy and PC approach"""
        assert event_m20_11_x115(z7=z7)
    """State 4: Finish"""
    return 0

def event_m20_11_x121(z2=4220, z3=4250, z4=4280):
    """[DC] [Condition] Lizard extinction judgment_3 bodies
    z2: Generator ID ①
    z3: Generator ID ②
    z4: Generator ID ③
    """
    """State 0,1: Upper limit judgment of lizards"""
    IsChrMaxRespawnCount(8, z2, 1, 0)
    IsChrMaxRespawnCount(8, z3, 1, 0)
    IsChrMaxRespawnCount(8, z4, 1, 0)
    if ConditionGroup(8):
        """State 2: extinction"""
        return 0
    else:
        """State 3: Not extinct"""
        return 1

def event_m20_11_x122(z1=211000016):
    """[DC] [Preset] lizard extinction judgment_3 bodies
    z1: Lizard extinction flag
    """
    """State 0,1: [Reproduction] Lizard extinction judgment_sky_SubState"""
    assert event_m20_11_x112()
    """State 3: [DC] [Condition] Lizard extinction judgment_3 bodies_SubState"""
    call = event_m20_11_x121(z2=4220, z3=4250, z4=4280)
    if call.Get() == 0:
        """State 2: [Execution] Lizard extinction judgment_SubState"""
        assert event_m20_11_x114(z1=z1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_11_111302():
    """NPC: Bard Girl 1: Grave"""
    """State 0,1: NPC: Bard Girl 1: Grave Placement_SubState"""
    event_m20_11_x0(z124=104220, z125=20114000, z126=21, z127=7600)
    Quit()

def event_m20_11_111303():
    """NPC: Bard Girl 1: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7600:Milfanito
    event_m20_11_x3(z119=211010100, z120=211020101, z121=104220, z122=20114000, z123=111302, npc1=7600)
    Quit()

def event_m20_11_111304():
    """NPC: Bard Girl 1: Hoarseness"""
    """State 0,1: [Lib] Bard Girl: Hoarse _SubState"""
    event_m20_11_x4(z112=104220, z113=20000000, z114=20000010, z115=201110002, z116=20000020, z117=211020107,
                    z118=20)
    Quit()

def event_m20_11_111312():
    """NPC: Bard Girl 2: Tomb"""
    """State 0,1: NPC: Bard Girl 2: Grave Placement_SubState"""
    event_m20_11_x0(z124=104230, z125=20114100, z126=26, z127=7601)
    Quit()

def event_m20_11_111313():
    """NPC: Bard Girl 2: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7601:Milfanito
    event_m20_11_x3(z119=211010120, z120=211020121, z121=104230, z122=20114100, z123=111312, npc1=7601)
    Quit()

def event_m20_11_111314():
    """NPC: Bard Girl 2: Hoarseness"""
    """State 0,1: [Lib] Bard Girl: Hoarse _SubState"""
    event_m20_11_x4(z112=104230, z113=20000100, z114=20000110, z115=201110002, z116=20000120, z117=211020127,
                    z118=25)
    Quit()

def event_m20_11_118130():
    """Multi-use NPC: Lancer (Female): White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_11_x49(z67=666)
    Quit()

def event_m20_11_118131():
    """Multi-use NPC: Small White Spirit: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_11_x49(z67=667)
    Quit()

def event_m20_11_118220():
    """Multi-use NPC: Magician (Male): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m20_11_x58(z58=10000000, z59=660, z60=0, z61=2)
    Quit()

def event_m20_11_4000000():
    """[DC] Traveler's Dead _ Petrification Stop_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m20_11_x37(z86=5300, z87=0, z88=15, z89=211000030, z90=0, z91=1600, z92=6, z93=4000010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4000010():
    """[DC] Traveler's deceased_Stop petrification_Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m20_11_x48(z68=5300, z69=0, z70=211000030, z71=0, z72=0, z73=4000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4000020():
    """[DC] Traveller's Dead _ Petrochemical Stop _ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m20_11_x57(z62=6000020, z63=0, z64=2, flag7=211000030, flag8=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4001000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m20_11_x62(flag4=211020001, z44=14, flag5=211000002, z45=3, z46=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m20_11_x67(z51=80000000, z52=0, z53=5, z54=965, val1=1, z55=10, z56=80000001, z57=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m20_11_x67(z51=80000100, z52=0, z53=5, z54=965, val1=2, z55=10, z56=80000101, z57=80000199)
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m20_11_x67(z51=80000200, z52=0, z53=5, z54=965, val1=3, z55=10, z56=80000201, z57=80000299)
        """State 2: Start flag ON"""
        SetEventFlag(211020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4001010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m20_11_x70(flag6=211000002, z49=965, mode1=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_11_x74(z47=6600, z48=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_11_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_11_x74(z47=6601, z48=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

