# -*- coding: utf-8 -*-
def event_m10_31_10():
    """Duel start"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel start_SubState"""
    assert (event_m10_31_x19(z39=10310400, z40=10310401, z41=10310402, z42=10310403, z43=10310404, z44=10310405,
            z45=10, z46=16))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_2000():
    """Drawbridge"""
    """State 0,2: [Preset] Working Bridge_SubState"""
    assert event_m10_31_x46(z20=10312000, z21=10311010, z22=200000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_3000():
    """Boss battle_scaffold expansion"""
    """State 0,2: [Preset] Scaffold extension_SubState"""
    assert (event_m10_31_x51(z13=10312010, z14=10311011, z15=10311012, z16=300000, z17=300001, z18=131000025,
            z19=131000026))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_5000():
    """Boss: Heavy cavalry: Soldier only_Battle"""
    """State 0,2: [Preset] Heavy Cavalry: Soldiers only_Boss Battle_SubState"""
    assert (event_m10_31_x62(flag1=131000081, z1=500000, z2=500000, z3=101, z4=1031000, z5=131020080,
            z6=842, mode1=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6000():
    """Boss: Ornstein_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_31_x5(flag5=131000086, z50=600000, z51=600000, z52=102, z53=1031010, z54=131020085,
            mode5=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6010():
    """Pillars and chairs destroyed 1"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313000, z12=601000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6020():
    """Pillar and chair 2 to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313001, z12=602000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6030():
    """Pillars and chairs destroyed 3"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313002, z12=603000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6040():
    """Pillars and chairs 4 destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313003, z12=604000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6090():
    """Pillar and chair 9 destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313008, z12=609000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6100():
    """10 pillars and chairs to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313009, z12=610000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6110():
    """Pillars and chairs to be destroyed 11"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313010, z12=611000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6120():
    """Pillars and chairs destroyed 12"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313011, z12=612000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6170():
    """Pillars and chairs 17 destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313016, z12=617000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6180():
    """Pillars and chairs destroyed 18"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313017, z12=618000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6190():
    """Pillars and chairs destroyed 19"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313018, z12=619000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6200():
    """20 pillars and chairs to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313019, z12=620000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6210():
    """21 pillars and chairs to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313020, z12=621000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6220():
    """Pillars and chairs 22 to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313021, z12=622000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6270():
    """Pillars and chairs destroyed 27"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313026, z12=627000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6280():
    """Pillars and chairs destroyed 28"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313027, z12=628000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6290():
    """Pillars and chairs 29 to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313028, z12=629000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6300():
    """30 pillars and chairs to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313029, z12=630000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6310():
    """Pillar and chair 31 to be destroyed"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313030, z12=631000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_6320():
    """[Group condition: Character] Player special effects"""
    """State 0,2: [Preset] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x57(z11=10313031, z12=632000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_7000():
    """The gimmick door between Madura and Heide Great Fire Tower"""
    """State 0,2: [Preset] Madura-Heide Great Fire Tower Gimmick Door_SubState"""
    assert event_m10_31_x39(z23=10312020, z24=10311020, z25=10311015, z26=700000, z27=700001, z28=700002)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_31_8000():
    """Lever Appearing from the Floor_Boss Battle Scaffold Expansion 1"""
    """State 0,2: [Preset] Lever appearing from the floor_SubState"""
    assert (event_m10_31_x54(z7=10311105, z8=10311011, z9=1020, mode2=0, mode3=0, mode4=0, z10=800000,
            flag2=131000020))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_8010():
    """Lever Appearing from the Floor_Boss Battle Scaffold Expansion 2"""
    """State 0,2: [Preset] Lever appearing from the floor_SubState"""
    assert (event_m10_31_x54(z7=10311110, z8=10311012, z9=1030, mode2=0, mode3=0, mode4=0, z10=801000,
            flag2=131000021))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_8020():
    """Lever emerging from the floor"""
    """State 0,2: [Preset] Lever appearing from the floor_SubState"""
    assert (event_m10_31_x54(z7=10311100, z8=10311010, z9=1080, mode2=0, mode3=0, mode4=0, z10=802000,
            flag2=131000022))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_9000():
    """Switching of Madura's revolving door related flags"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_31_x17(z48=105400, z49=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_31_10000():
    """Connection flag OFF"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_31_x17(z48=105415, z49=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_31_70000():
    """Duel request"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62100000:Token of Fidelity
    assert event_m10_31_x31(z31=0, z32=10319000, z33=10319001, z34=10312100, z35=30, val1=2, goods1=62100000)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_31_70010():
    """Duel Request_2"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62100000:Token of Fidelity
    assert event_m10_31_x31(z31=1, z32=10319000, z33=10319001, z34=10312101, z35=30, val1=2, goods1=62100000)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_31_70020():
    """Duel Request_3"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Duel Request_Training_SubState"""
    # goods:62100000:Token of Fidelity
    assert event_m10_31_x31(z31=2, z32=10319000, z33=10319001, z34=10312102, z35=30, val1=2, goods1=62100000)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_31_80000():
    """Rebirth Fire 01_ Lighthouse after Boss Heavy Cavalry"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_31_x28(z37=1031000, z38=1031099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_81000():
    """Regenerative fire 02_The rocks beside the starting point"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_31_x28(z37=1031100, z38=1031199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_82000():
    """After the rebirth of fire 03_Boss Öhnstein"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_31_x28(z37=1031200, z38=1031299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_x0(z62=_, z63=_, z64=_, z65=_):
    """[Lib] NPC: Grave Placement: General purpose
    z62: Death map: Global event flag
    z63: Tomb: OBJ instance ID
    z64: Tomb move to: Generator ID
    z65: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z62, 1)
    IsGraveGeneratable(8, z65, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z63, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z63, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_31_x1(z59=_, z60=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z59: Global: death flag
    z60: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z60, 10, 0)
    CompareObjState(1, z60, 20, 0)
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
    IsObjSearched(0, z60)
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

def event_m10_31_x2(z57=_, z58=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z57: Area other flags: Ghost appearance
    z58: Area other flags: Conversation start
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
    SetEventFlag(z57, 1)
    CompareEventFlag(0, z57, 1)
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
    SetEventFlag(z58, 1)
    CompareEventFlag(0, z58, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_31_x3(z57=_, z58=_, z59=_, z60=_, z61=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z57: Ghost Appearance: Area Other Flag
    z58: Conversation start: Area and other flags
    z59: Death: Global event flag
    z60: Tomb: OBJ instance ID
    z61: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z61, 1, 0)
    CompareEventFlag(9, z57, 1)
    CompareObjState(9, z60, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z58, 1)
        CompareEventFlag(0, z58, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_31_x1(z59=z59, z60=z60, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_31_x2(z57=z57, z58=z58, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_31_x4(z55=150, z56=104321):
    """[Lib] NPC: Death determination: General purpose
    z55: Generator ID
    z56: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z56, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z55)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z56, 1)
            CompareEventFlag(0, z56, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_31_x5(flag5=131000086, z50=600000, z51=600000, z52=102, z53=1031010, z54=131020085, mode5=0):
    """[Lib] [Preset] Boss Battle Start
    flag5: Boss destruction flag
    z50: Start point ID
    z51: End point ID
    z52: Sound ID
    z53: Boss Battle ID
    z54: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_31_x6(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_31_x7(z50=z50, z51=z51)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_31_x8(z52=z52, z53=z53, z54=z54)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_31_x9()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_31_x10(z53=z53)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_31_x11(z52=z52, z53=z53, z54=z54, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m10_31_x6(flag5=131000086):
    """[Reproduction] Boss Battle_Start
    flag5: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_31_x7(z50=600000, z51=600000):
    """[Condition] Boss Battle_Start
    z50: Start point ID
    z51: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z50, z51, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z50, z51, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x8(z52=102, z53=1031010, z54=131020085):
    """[Execution] Boss Battle_Start
    z52: Sound ID
    z53: Boss Battle ID
    z54: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z52)
    """State 1: Boss battle start notification"""
    StartBossFight(z53)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z54, 1)
    """State 4: End state"""
    return 0

def event_m10_31_x9():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x10(z53=1031010):
    """[Condition] Boss Battle_End Judgment
    z53: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z53, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x11(z52=102, z53=1031010, z54=131020085, mode5=0):
    """[Execute] Boss Battle_End
    z52: Sound ID
    z53: Boss Battle ID
    z54: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z54, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z53)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z52)
    """State 5: End state"""
    return 0

def event_m10_31_x12():
    """[Lib] [Reproduction] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x13():
    """[Lib] [Condition] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x14():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x15():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x16(z48=_, z49=0):
    """[Lib] [Execution] Switch to connection flag when in map
    z48: Global event flag for connection
    z49: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z48, z49)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z48, z49)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_31_x17(z48=_, z49=0):
    """[Lib] [Preset] Switch the connection flag when in the map
    z48: Global event flag for connection
    z49: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_31_x14()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_31_x15()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_31_x16(z48=z48, z49=z49)
    """State 4: End state"""
    return 0

def event_m10_31_x18(z47=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z47: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z47)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_31_x19(z39=10310400, z40=10310401, z41=10310402, z42=10310403, z43=10310404, z44=10310405,
                     z45=10, z46=16):
    """[Lib] [Asynchronous] [Preset] Duel start
    z39: Door instance IDA
    z40: Door instance IDB
    z41: Door instance IDC
    z42: Door instance IDD
    z43: Door instance IDE
    z44: Door instance IDF
    z45: Event sound ID
    z46: Production FE type
    """
    """State 0,1: [Lib] [Reproduction] Dummy_SubState"""
    assert event_m10_31_x12()
    """State 2: [Lib] [Condition] Dummy_SubState"""
    assert event_m10_31_x13()
    """State 3: [Lib] [Execution] Duel Start_SubState"""
    assert event_m10_31_x20(z39=z39, z40=z40, z41=z41, z42=z42, z43=z43, z44=z44, z45=z45, z46=z46)
    """State 4: End state"""
    return 0

def event_m10_31_x20(z39=10310400, z40=10310401, z41=10310402, z42=10310403, z43=10310404, z44=10310405,
                     z45=10, z46=16):
    """[Private] [Asynchronous] [Execution] Start of duel
    z39: Door instance IDA
    z40: Door instance IDB
    z41: Door instance IDC
    z42: Door instance IDD
    z43: Door instance IDE
    z44: Door instance IDF
    z45: Event sound ID
    z46: Production FE type
    """
    """State 0,1: Jingle sound playback"""
    PlaySoundAtPoint(z45)
    """State 4: Preparation time"""
    assert (GetStateTime() > 5) != 0
    """State 2: Start: open the door"""
    ChangeObjState(z39, 70)
    ChangeObjState(z40, 70)
    ChangeObjState(z41, 70)
    ChangeObjState(z42, 70)
    ChangeObjState(z43, 70)
    ChangeObjState(z44, 70)
    """State 3: Production FE display"""
    OpenPresentationWindow(z46)
    """State 5: End state"""
    return 0

def event_m10_31_x21(z31=_):
    """[Private] [Asynchronous] [Execution] Duel Request_Start
    z31: Duel type
    """
    """State 0,1: Motion start"""
    PlayerActionRequest(14)
    ProhibitInGameMenu(1)
    """State 2: Matching start"""
    StartDuelMatch(z31)
    """State 3: End state"""
    return 0

def event_m10_31_x22(z34=_, z35=30):
    """[Private] [Asynchronous] [Condition] Duel request_wait
    z34: Object instance ID
    z35: Hit group
    """
    """State 0,2: A little wait"""
    assert (GetStateTime() >= 0) != 0
    """State 1: Wait to examine"""
    IsObjSearched(0, z34)
    IsDuelStartPossible(0, 0)
    IsPlayerDamaged(0)
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(0, z35, 0, 0, 2)
    IsPlayerPlayingMotion(0, 14, 0)
    IsDuelMatching(0, 0)
    HasDuelMatched(1, 1)
    if ConditionGroup(0):
        """State 4: Cancel"""
        return 0
    elif ConditionGroup(1):
        """State 3,5: Duel-matched"""
        return 1

def event_m10_31_x23():
    """[Private] [Asynchronous] [Execution] Duel request_wait_cancel"""
    """State 0,1: Motion cancellation"""
    EndPlayerActionRequest()
    """State 2: Duel cancellation"""
    CancelDuelMatch()
    ProhibitInGameMenu(0)
    """State 3: End state"""
    return 0

def event_m10_31_x24(z35=30, z33=10319001):
    """[Private] [Asynchronous] [Reproduction] Duel request_wait
    z35: Hit group
    z33: Key guide parameters
    """
    """State 0,1: Key guide creation"""
    CreateKeyGuideArea(34, z33)
    """State 2: Finish"""
    return 0

def event_m10_31_x25():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x26(z37=_, z38=_):
    """[Lib] [execute] Rebirth fire
    z37: Flag start ID
    z38: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z37, z38, 0)
    """State 2: End state"""
    return 0

def event_m10_31_x27():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x28(z37=_, z38=_):
    """[Lib] [Preset] Rebirth
    z37: Flag start ID
    z38: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_31_x25()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_31_x27()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_31_x26(z37=z37, z38=z38)
    """State 4: End state"""
    return 0

def event_m10_31_x29(flag4=131020017, z36=19):
    """[Lib] [Preset] Get trophy
    flag4: Acquisition trigger_other flags
    z36: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag4) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag4, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z36)
    """State 4: End state"""
    return 0

def event_m10_31_x30():
    """[Private] [Asynchronous] [Execution] Duel request_wait_matched"""
    """State 0,3: Cannot cancel motion"""
    ForceDisablePlayerAnimationCancelling(1)
    DeleteKeyGuideArea()
    IsDuelMatching(0, 0)
    assert ConditionGroup(0)
    """State 1: Motion cancellation"""
    EndPlayerActionRequest()
    ForceDisablePlayerAnimationCancelling(0)
    """State 2: Duel cancellation"""
    CancelDuelMatch()
    ProhibitInGameMenu(0)
    """State 4: End state"""
    return 0

def event_m10_31_x31(z31=_, z32=10319000, z33=10319001, z34=_, z35=30, val1=2, goods1=62100000):
    """[Lib] [Asynchronous] [Preset] Duel Request
    z31: Duel type
    z32: Start key guide parameter
    z33: Cancel key guide parameter
    z34: Object instance ID
    z35: Hit group
    val1: Pledge
    goods1: item
    """
    """State 0,8: [Private] [Asynchronous] [Reproduction] Duel Request_Start_Training_SubState"""
    call = event_m10_31_x33(z35=z35, z32=z32, val1=val1)
    if call.Get() == 1:
        """State 10: [Private] [Asynchronous] [Condition] Duel request_Start_Key guide wait_Training_SubState"""
        call = event_m10_31_x32(z34=z34, z35=z35, val1=val1, goods1=goods1)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 3: [Private] [Asynchronous] [Execution] Duel Request_Start_SubState"""
            assert event_m10_31_x21(z31=z31)
            """State 4: [Private] [Asynchronous] [Reproduction] Duel Request_Standby_SubState"""
            assert event_m10_31_x24(z35=z35, z33=z33)
            """State 5: [Private] [Asynchronous] [Condition] Duel Request_Standby_SubState"""
            call = event_m10_31_x22(z34=z34, z35=z35)
            if call.Get() == 0:
                """State 6: [Private] [Asynchronous] [Execution] Duel Request_Wait_Cancel_SubState"""
                assert event_m10_31_x23()
            elif call.Get() == 1:
                """State 7: [Private] [Asynchronous] [Execution] Duel Request_Waiting_Matched_SubState"""
                assert event_m10_31_x30()
            """State 2: Rerun_2"""
            RestartMachine()
            Quit()
    elif call.Done():
        """State 9: [Private] [Asynchronous] [Condition] Duel Request_Start_Key Guide Invalidation Wait_Training_SubState"""
        assert event_m10_31_x34(z35=z35, val1=val1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_31_x32(z34=_, z35=30, val1=2, goods1=62100000):
    """[Private] [Asynchronous] [Condition] Duel request_Start_Key guide wait
    z34: Object instance ID
    z35: Hit group
    val1: Pledge
    goods1: item
    """
    """State 0,1: Wait to examine"""
    IsObjSearched(0, z34)
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(1, z35, 0, 0, 2)
    IsPlayerInCovenant(1, val1, 0)
    IsOffline(1, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Item confirmation"""
        # goods:62100000:Token of Fidelity
        if (ItemCount(goods1, 1, 1, 0) > 1) != 1:
            """State 2: Don't have display"""
            # action:1013:"No %s\nin inventory", goods:62100000:Token of Fidelity
            DisplayOwnOkMenu(1013, 0, 0, 190, 2, goods1, 0)
            assert OkMenuDisplay() != 1
            Goto('L0')
        elif (GetPlayerCovenant() == 2) != 0:
            """State 4: Usage confirmation"""
            # action:1002:"Use %s?", goods:62100000:Token of Fidelity
            DisplayOwnYesNoMenu(1002, 0, 190, 2, goods1, 0)
            assert YesNoMenuDisplay() != 1
            """State 5: Result branch"""
            if (YesNoMenuResult() == 1) != 1:
                Goto('L0')
            else:
                pass
        else:
            pass
        """State 6: Establishment"""
        return 0
    """State 7: Not established"""
    Label('L0')
    return 1

def event_m10_31_x33(z35=30, z32=10319000, val1=2):
    """[Private] [Asynchronous] [Reproduction] Duel Request_Start
    z35: Hit group
    z32: Key guide parameters
    val1: Pledge
    """
    """State 0,1: Branch"""
    if (CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(z35, 0, 1) != 1 and (GetPlayerCovenant()
        == val1) != 0 and IsOffline() != 1):
        """State 2: Key guide creation"""
        CreateKeyGuideArea(34, z32)
        """State 5: There are no enemies around"""
        return 1
    else:
        """State 3: Delete key guide"""
        DeleteKeyGuideArea()
        """State 4: There are enemies around"""
        return 0

def event_m10_31_x34(z35=30, val1=2):
    """[Private] [Asynchronous] [Condition] Duel request_Start_Key guide invalidation waiting
    z35: Hit group
    val1: Pledge
    """
    """State 0,1: Wait"""
    CompareHowManyCharactersOnHitGroupAreHostileOrFriendly(8, z35, 0, 0, 5)
    IsPlayerInCovenant(8, val1, 1)
    IsOffline(8, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_31_x35(flag3=_):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag3: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag3) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_31_x36(z29=_):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z29: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z29, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x37(z30=_):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z30: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z30, 1)
    """State 2: End state"""
    return 0

def event_m10_31_x38(flag3=_, z29=_, z30=_):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag3: Boss destruction flag
    z29: Boss generator ID
    z30: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_31_x35(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_31_x36(z29=z29)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_31_x37(z30=z30)
    """State 4: End state"""
    return 0

def event_m10_31_x39(z23=10312020, z24=10311020, z25=10311015, z26=700000, z27=700001, z28=700002):
    """[Preset] Giudal door between Madura and Heide Great Fire Tower
    z23: Door instance ID
    z24: Instance ID of the madura lever
    z25: Heide Great Fire Tower lever instance ID
    z26: Point ID for Navimesh change
    z27: Point ID for door closing judgment_Start
    z28: Door closing judgment point ID_End
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z23, 0)
    """State 2: [Reproduction] Giudal door between Madura and Heide Great Fire Tower_SubState"""
    call = event_m10_31_x40(z23=z23, z24=z24, z25=z25, z26=z26)
    if call.Done():
        """State 3: [Condition] Giudal door between Madura and Heide Great Fire Tower_SubState"""
        assert event_m10_31_x41(z24=z24, z25=z25)
        """State 4: [Execution] Madura-Heide Great Fire Tower Gimmick Door_SubState"""
        assert event_m10_31_x42(z23=z23, z24=z24, z25=z25, z26=z26, z27=z27, z28=z28)
    elif call.Get() == 1:
        pass
    """State 5: End state"""
    return 0

def event_m10_31_x40(z23=10312020, z24=10311020, z25=10311015, z26=700000):
    """[Reproduction] Giudal door between Madura and Heide Great Fire Tower
    z23: Door instance ID
    z24: Instance ID of the madura lever
    z25: Heide Great Fire Tower lever instance ID
    z26: Point ID for Navimesh change
    """
    """State 0,2: Event ends for guests"""
    if IsGuest() != 0:
        """State 6: Simple end"""
        return 1
    else:
        """State 1: Initialize the OBJ state of the door"""
        InitializeObj(z23)
        """State 4: Navi Mesh Change: No entry"""
        AddNavimeshAttribute(z26, 2)
        """State 3: Enable key guide for lever"""
        DisableObjKeyGuide(z24, 0)
        DisableObjKeyGuide(z25, 0)
        """State 5: End state"""
        return 0

def event_m10_31_x41(z24=10311020, z25=10311015):
    """[Conditions] Gimmick door between Madura and Heide Great Fire Tower
    z24: Instance ID of the madura lever
    z25: Heide Great Fire Tower lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z24, 74, 0)
    CompareObjState(0, z25, 74, 0)
    CompareObjState(0, z24, 84, 0)
    CompareObjState(0, z25, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x42(z23=10312020, z24=10311020, z25=10311015, z26=700000, z27=700001, z28=700002):
    """[Execute] Gimmick door between Madura and Heide Great Fire Tower
    z23: Door instance ID
    z24: Instance ID of the madura lever
    z25: Heide Great Fire Tower lever instance ID
    z26: Point ID for Navimesh change
    z27: Point ID for door closing judgment_Start
    z28: Door closing judgment point ID_End
    """
    """State 0,1: OBJ state transition: Door: 70"""
    ChangeObjState(z23, 70)
    """State 2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z24, 1)
    DisableObjKeyGuide(z25, 1)
    """State 3: Has the door opened?"""
    CompareObjState(0, z23, 30, 0)
    assert ConditionGroup(0)
    """State 7: Navi Mesh Change: Enterable"""
    DeleteNavimeshAttribute(z26, 2)
    """State 4: Judgment of conditions for closing the door"""
    CompareStateTime(0, 15, 2, 15)
    IsPlayerInsidePoint(1, z27, z28, 1)
    if ConditionGroup(0):
        """State 5: OBJ state transition: Door: 80"""
        ChangeObjState(z23, 80)
        """State 6: Has the door closed?"""
        CompareObjState(0, z23, 10, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(1):
        pass
    """State 8: End state"""
    return 0

def event_m10_31_x43(z20=10312000, z22=200000):
    """[Reproduction] Working bridge
    z20: Bridge instance ID
    z22: Navimesh switching point ID
    """
    """State 0,1: Already in operation?"""
    if CompareObjStateId(z20, 10, 1):
        """State 3: Waiting for the bridge anime to end"""
        assert CompareObjStateId(z20, 20, 0)
        """State 2: Navigation switching"""
        DeleteNavimeshAttribute(z22, 2)
        """State 5: Finish"""
        return 1
    else:
        """State 4: Not in operation"""
        return 0

def event_m10_31_x44(z21=10311010):
    """[Conditions] Working bridge
    z21: Lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z21, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x45(z20=10312000, z22=200000):
    """[Execution] Operation Bridge
    z20: Bridge instance ID
    z22: Navigation switching point ID
    """
    """State 0,1: OBJ state transition request: Bridge: 70"""
    ChangeObjState(z20, 70)
    """State 2: OBJ state transition completion wait: 20"""
    CompareObjState(0, z20, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z22, 2)
    """State 4: End state"""
    return 0

def event_m10_31_x46(z20=10312000, z21=10311010, z22=200000):
    """[Preset] Working bridge
    z20: Bridge instance ID
    z21: Lever instance ID
    z22: Navigation switching point ID
    """
    """State 0,1: [Reproduction] Operation Bridge_SubState"""
    call = event_m10_31_x43(z20=z20, z22=z22)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Working bridge_SubState"""
        assert event_m10_31_x44(z21=z21)
        """State 3: [Execution] Operation Bridge_SubState"""
        assert event_m10_31_x45(z20=z20, z22=z22)
    """State 4: End state"""
    return 0

def event_m10_31_x47(z13=10312010, z16=300000, z17=300001, z18=131000025, z19=131000026):
    """[Reproduction] Scaffolding expansion
    z13: Scaffold instance ID
    z16: Navi switching point ID_small
    z17: Navigation switching point ID_Large
    z18: Scaffold expansion flag ①
    z19: Scaffold expansion flag ②
    """
    """State 0,1: Is the scaffold fully expanded?"""
    if CompareObjStateId(z13, 20, 0):
        """State 3: Navigation switching: 2-stage expansion"""
        DeleteNavimeshAttribute(z16, 2)
        DeleteNavimeshAttribute(z17, 2)
    else:
        """State 9: Is it in the second stage of expansion?"""
        if CompareObjStateId(z13, 71, 0):
            """State 8: Hit invalidation: outside _2"""
            SetHitEnabled(20, 0)
            """State 10: Navigation switching: 1 stage expansion_2"""
            DeleteNavimeshAttribute(z16, 2)
            """State 7: Waiting for expansion: 2nd stage"""
            assert CompareObjStateId(z13, 20, 0)
            """State 11: Hit activation: outside"""
            SetHitEnabled(20, 1)
            """State 12: Navigation switching: 2-stage expansion_2"""
            DeleteNavimeshAttribute(z17, 2)
            """State 18: Scaffold expansion flag ② ON"""
            SetEventFlag(z19, 1)
        else:
            """State 5: Hit invalidation: outside"""
            SetHitEnabled(20, 0)
            """State 2: Is the scaffold expanded by one step?"""
            if CompareObjStateId(z13, 30, 0):
                """State 4: Navigation switching: 1 level expansion"""
                DeleteNavimeshAttribute(z16, 2)
            else:
                """State 13: Is it in the first stage of expansion?"""
                if CompareObjStateId(z13, 70, 0):
                    """State 17: Hit invalidation: inside_3"""
                    SetHitEnabled(10, 0)
                    """State 14: Waiting for expansion: Stage 1"""
                    assert CompareObjStateId(z13, 30, 0)
                    """State 15: Hit activation: inside"""
                    SetHitEnabled(10, 1)
                    """State 16: Navigation switching: 1 stage expansion_3"""
                    DeleteNavimeshAttribute(z16, 2)
                    """State 19: Scaffold expansion flag ① ON"""
                    SetEventFlag(z18, 1)
                else:
                    """State 6: Hit invalidation: inside"""
                    SetHitEnabled(10, 0)
                    """State 20: Not in operation"""
                    return 0
            """State 22: Expanded_1 stage"""
            return 2
    """State 21: Finish"""
    return 1

def event_m10_31_x48(z14=10311011, z15=10311012):
    """[Conditions] Scaffold expansion_1 stage
    z14: Lever instance ID_1
    z15: Lever instance ID_2
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z14, 20, 0)
    CompareObjState(0, z15, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x49(z13=10312010, z16=300000, z18=131000025):
    """[Execution] Scaffold extension_1 stage
    z13: Scaffold instance ID
    z16: Navigation switching point ID
    z18: Scaffold expansion flag ①
    """
    """State 0,1: OBJ state transition request: Scaffolding: 70"""
    ChangeObjState(z13, 70)
    """State 2: OBJ state transition completion wait: 30"""
    CompareObjState(0, z13, 30, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z16, 2)
    """State 4: Hit activation: inside"""
    SetHitEnabled(10, 1)
    """State 5: Scaffold expansion flag ON"""
    SetEventFlag(z18, 1)
    """State 6: End state"""
    return 0

def event_m10_31_x50(z13=10312010, z17=300001, z19=131000026):
    """[Execution] Scaffold extension_2 stage
    z13: Scaffold instance ID
    z17: Navigation switching point ID
    z19: Scaffold expansion flag ②
    """
    """State 0,1: OBJ state transition request: Scaffolding: 71"""
    ChangeObjState(z13, 71)
    """State 2: OBJ state transition completion wait: 20"""
    CompareObjState(0, z13, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z17, 2)
    """State 4: Hit invalidation: outside"""
    SetHitEnabled(20, 1)
    """State 5: Scaffold expansion flag ON"""
    SetEventFlag(z19, 1)
    """State 6: End state"""
    return 0

def event_m10_31_x51(z13=10312010, z14=10311011, z15=10311012, z16=300000, z17=300001, z18=131000025,
                     z19=131000026):
    """[Preset] Scaffolding expansion
    z13: Scaffold instance ID
    z14: Lever instance ID_1
    z15: Lever instance ID_2
    z16: Navi switching point ID_small
    z17: Navigation switching point ID_Large
    z18: Scaffold expansion flag ①
    z19: Scaffold expansion flag ②
    """
    """State 0,1: [Reproduction] Scaffold extension_SubState"""
    call = event_m10_31_x47(z13=z13, z16=z16, z17=z17, z18=z18, z19=z19)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 5: [Condition] Scaffolding extension_2 stage_SubState"""
        Label('L0')
        assert event_m10_31_x52(z14=z14, z15=z15)
        """State 4: [Execution] Scaffold extension_2 stage_SubState"""
        assert event_m10_31_x50(z13=z13, z17=z17, z19=z19)
    elif call.Get() == 0:
        """State 2: [Condition] Scaffold extension_1 stage_SubState"""
        assert event_m10_31_x48(z14=z14, z15=z15)
        """State 3: [Execution] Scaffold extension_1 stage_SubState"""
        assert event_m10_31_x49(z13=z13, z16=z16, z18=z18)
        Goto('L0')
    """State 6: End state"""
    return 0

def event_m10_31_x52(z14=10311011, z15=10311012):
    """[Condition] Scaffolding extension_2 stage
    z14: Lever instance ID_1
    z15: Lever instance ID_2
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(8, z14, 20, 0)
    CompareObjState(8, z15, 20, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_31_x53(z7=_, z8=_, flag2=_):
    """[Reproduction] Lever appearing from the floor
    z7: Object instance ID of the storage hole
    z8: Lever object instance ID
    flag2: Enemy flag for enemies
    """
    """State 0,1: Attach lever OBJ to storage hole OBJ"""
    AttachObjToObj(z7, 150, z8)
    DisableObjKeyGuide(z8, 1)
    """State 2: Determining the status of the storage hole OBJ"""
    if CompareObjStateId(z7, 10, 0):
        pass
    else:
        Goto('L0')
    """State 3: Defeat all enemy targets"""
    if GetEventFlag(flag2) != 0:
        """State 5: Annihilated"""
        return 1
    else:
        """State 4: Not annihilated"""
        return 0
    """State 6: End immediately"""
    Label('L0')
    return 2

def event_m10_31_x54(z7=_, z8=_, z9=_, mode2=0, mode3=0, mode4=0, z10=_, flag2=_):
    """[Preset] Lever that emerges from the floor
    z7: Object instance ID of the storage hole
    z8: Lever object instance ID
    z9: Enemy 1 generator ID
    mode2: Enemy 2 Generator ID
    mode3: Enemy 3 generator ID
    mode4: Enemy 4 generator ID
    z10: Point ID for Navimesh change
    flag2: Enemy flag for enemies
    """
    """State 0,1: [Reproduction] Lever _SubState emerging from the floor"""
    call = event_m10_31_x53(z7=z7, z8=z8, flag2=flag2)
    if call.Get() == 2:
        """State 4: [Execution] Lever appearing from the floor_End immediately_SubState"""
        assert event_m10_31_x61(z7=z7, z8=z8, z10=z10)
    elif call.Get() == 1:
        """State 3: [Execution] Lever _SubState emerging from the floor"""
        Label('L0')
        assert event_m10_31_x56(z7=z7, z8=z8, z10=z10, flag2=flag2)
    elif call.Get() == 0:
        """State 2: [Condition] Lever appearing from the floor_SubState"""
        assert event_m10_31_x55(z9=z9, mode2=mode2, mode3=mode3, mode4=mode4)
        Goto('L0')
    """State 5: End state"""
    return 0

def event_m10_31_x55(z9=_, mode2=0, mode3=0, mode4=0):
    """[Conditions] Lever emerging from the floor
    z9: Enemy 1 generator ID
    mode2: Enemy 2 Generator ID
    mode3: Enemy 3 generator ID
    mode4: Enemy 4 generator ID
    """
    """State 0,1: Enemy 1 death check"""
    IsChrDeadOrRespawnOver(0, z9, 1)
    assert ConditionGroup(0)
    """State 6: Enemy 2 presence determination"""
    if (not mode2) != 0:
        """State 5: There are no more enemies"""
        Label('L0')
    else:
        """State 2: Enemy 2 death check"""
        IsChrDeadOrRespawnOver(0, mode2, 1)
        assert ConditionGroup(0)
        """State 7: Enemy 3 presence check"""
        if (not mode3) != 0:
            Goto('L0')
        else:
            """State 3: Enemy 3 death determination"""
            IsChrDeadOrRespawnOver(0, mode3, 1)
            assert ConditionGroup(0)
            """State 8: Enemy 4 presence check"""
            if (not mode4) != 0:
                Goto('L0')
            else:
                """State 4: Enemy 4 death determination"""
                IsChrDeadOrRespawnOver(0, mode4, 1)
                assert ConditionGroup(0)
    """State 9: End state"""
    return 0

def event_m10_31_x56(z7=_, z8=_, z10=_, flag2=_):
    """[Execution] Lever emerging from the floor
    z7: Object instance ID of the storage hole
    z8: Lever object instance ID
    z10: Point ID for Navimesh change
    flag2: Enemy flag for enemies
    """
    """State 0,4: Enemy flag for enemies to be subjugated: ON"""
    SetEventFlag(flag2, 1)
    """State 5: Waiting for enemy death to end"""
    CompareStateTime(0, 5, 2, 5)
    assert ConditionGroup(0)
    """State 2: Run live animation"""
    ChangeObjState(z7, 70)
    """State 6: End judgment of animation"""
    CompareObjState(0, z7, 20, 0)
    assert ConditionGroup(0)
    """State 1: Enable lever key guide"""
    DisableObjKeyGuide(z8, 0)
    """State 3: Navigation mesh change"""
    AddNavimeshAttribute(z10, 2)
    """State 7: End state"""
    return 0

def event_m10_31_x57(z11=_, z12=_):
    """[Preset] Pillars and chairs to be destroyed
    z11: OBJ instance ID to be destroyed
    z12: Point ID to change Navimesh
    """
    """State 0,1: [Reproduction] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x58(z12=z12)
    """State 2: [Condition] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x59(z11=z11)
    """State 3: [Execution] Pillars and chairs to be destroyed _SubState"""
    assert event_m10_31_x60(z12=z12)
    """State 4: End state"""
    return 0

def event_m10_31_x58(z12=_):
    """[Reproduction] Pillars and chairs destroyed
    z12: Point ID to change Navimesh
    """
    """State 0,1: Navimesh change: no traffic"""
    AddNavimeshAttribute(z12, 2)
    """State 2: End state"""
    return 0

def event_m10_31_x59(z11=_):
    """[Condition] Pillars and chairs to be destroyed
    z11: OBJ instance ID to be destroyed
    """
    """State 0,1: Was OBJ destroyed?"""
    CompareObjState(0, z11, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x60(z12=_):
    """[Execution] Pillars and chairs destroyed
    z12: Point ID to change Navimesh
    """
    """State 0,1: Change of Navimesh: Passable"""
    DeleteNavimeshAttribute(z12, 2)
    """State 2: End state"""
    return 0

def event_m10_31_x61(z7=_, z8=_, z10=_):
    """[Execution] Lever appearing from the floor
    z7: Object instance ID of the storage hole
    z8: Lever object instance ID
    z10: Point ID for Navimesh change
    """
    """State 0,3: End judgment of animation"""
    CompareObjState(0, z7, 20, 0)
    assert ConditionGroup(0)
    """State 1: Enable lever key guide"""
    DisableObjKeyGuide(z8, 0)
    """State 2: Navigation mesh change"""
    AddNavimeshAttribute(z10, 2)
    """State 4: End state"""
    return 0

def event_m10_31_x62(flag1=131000081, z1=500000, z2=500000, z3=101, z4=1031000, z5=131020080, z6=842,
                     mode1=0):
    """[Preset] Heavy cavalry soldiers only _ boss battle
    flag1: Boss destruction flag
    z1: Start point ID
    z2: End point ID
    z3: Sound ID
    z4: Boss Battle ID
    z5: Other flags for logic
    z6: Generator ID
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Heavy Cavalry: Soldiers only_Boss Battle_Start_SubState"""
    call = event_m10_31_x63(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Conditions] Heavy Cavalry: Soldiers only_Boss Battle_Start_SubState"""
        assert event_m10_31_x64(z1=z1, z2=z2)
        """State 4: [Execution] Heavy cavalry: Soldier only _ Boss battle _ Immortal release_SubState"""
        assert event_m10_31_x65(z3=z3, z4=z4, z5=z5, z6=z6)
        """State 2: [Reproduction] Heavy Cavalry: Soldier only _ Boss Battle _ Sky _ SubState"""
        assert event_m10_31_x66()
        """State 6: [Conditions] Heavy Cavalry: Soldiers only_Boss Battle_End Judgment_SubState"""
        assert event_m10_31_x67(z4=z4)
        """State 3: [Execution] Heavy Cavalry: Soldiers only_Boss Battle_End_SubState"""
        assert event_m10_31_x68(z3=z3, z4=z4, z5=z5, mode1=mode1)
    """State 7: End state"""
    return 0

def event_m10_31_x63(flag1=131000081):
    """[Reproduction] Heavy Cavalry: Soldiers only_Boss Battle_Start
    flag1: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag1) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_31_x64(z1=500000, z2=500000):
    """[Conditions] Heavy cavalry: Soldier only_Boss Battle_Start
    z1: Start point ID
    z2: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z1, z2, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z1, z2, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x65(z3=101, z4=1031000, z5=131020080, z6=842):
    """[Execution] Heavy cavalry: Soldier only
    z3: Sound ID
    z4: Boss Battle ID
    z5: Other flags for logic
    z6: Generator ID
    """
    """State 0,4: Immortalization"""
    SetEnemySpEffect(z6, 91320030, 19, 4)
    """State 3: Boss BGM playback"""
    PlaySoundAtPoint(z3)
    """State 1: Boss battle start notification"""
    StartBossFight(z4)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z5, 1)
    """State 5: End state"""
    return 0

def event_m10_31_x66():
    """[Reproduction] Heavy Cavalry: Soldiers only_Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_31_x67(z4=1031000):
    """[Conditions] Heavy cavalry: Soldier only_Boss battle_End determination
    z4: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z4, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_31_x68(z3=101, z4=1031000, z5=131020080, mode1=0):
    """[Execution] Heavy Cavalry: Soldiers only_Boss Battle_End
    z3: Sound ID
    z4: Boss Battle ID
    z5: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z5, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z4)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z3)
    """State 5: End state"""
    return 0

def event_m10_31_111412():
    """OBJ: Miracle Person: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_31_x0(z62=104321, z63=10314100, z64=150, z65=7690)
    Quit()

def event_m10_31_111413():
    """OBJ: Miracle Person: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7690:Licia of Lindeldt
    event_m10_31_x3(z57=131010110, z58=131020111, z59=104320, z60=10314100, z61=111412, npc1=7690)
    Quit()

def event_m10_31_111414():
    """OBJ: Miracle: Death decision"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_31_x4(z55=150, z56=104321)
    Quit()

def event_m10_31_111492():
    """OBJ: Guardian Knight: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_31_x0(z62=104400, z63=10314000, z64=315, z65=7850)
    Quit()

def event_m10_31_111493():
    """OBJ: Guardian Knight: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7850:Blue Sentinel Targray
    event_m10_31_x3(z57=131010010, z58=131020011, z59=104400, z60=10314000, z61=111492, npc1=7850)
    Quit()

def event_m10_31_118100():
    """Multi-use NPC: Swordsman (Male): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_31_x18(z47=616)
    Quit()

def event_m10_31_118110():
    """Multi-use NPC: Induction white spirit: Koshiro phantom sign display"""
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, 100790, 1)
    CompareEventFlag(0, 100952, 1)
    assert ConditionGroup(0)
    """State 2: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_31_x18(z47=617)
    Quit()

def event_m10_31_120010():
    """Trophy: Guardian Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_31_x29(flag4=131020017, z36=19)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_31_4031000():
    """[DC] NPC White Spirit_Gesture Management_Heavy Cavalry: Soldiers only"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_31_x38(flag3=131000081, z29=842, z30=131020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_31_4031010():
    """[DC] NPC White Spirit_Gesture Management_Onstein"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_31_x38(flag3=131000086, z29=843, z30=131020087)
    """State 1: Finish"""
    EndMachine()
    Quit()

