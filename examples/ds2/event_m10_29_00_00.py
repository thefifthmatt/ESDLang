# -*- coding: utf-8 -*-
def event_m10_29_1000():
    """Madura-Forest Shadow Gimmick Door"""
    """State 0,2: [Preset] Madura-The Shadow Shadow Forest Gimmy Door_Lever Operation Judgment-Opening the Gimmick Door_SubState"""
    assert (event_m10_29_x16(z25=10292000, z26=10291000, z27=10291010, z28=10292020, z29=10292010, z30=129010021,
            z31=129010022, z32=129010023))
    """State 3: [Preset] Madura-The Shadow Shadow Forest Gimmick Door_Destination Determination-Gimmick Door Closure_SubState"""
    assert (event_m10_29_x37(z15=105405, z16=10292020, z17=10292010, z18=100001, z19=100002, z20=10292000,
            z21=100000, z22=129010024))
    """State 1: Rerun"""
    RestartMachine()

def event_m10_29_1010():
    """Toggle global flags related to gimmick doors"""
    """State 0,2: [Preset] Switch global flags related to gimmick doors_SubState"""
    assert (event_m10_29_x20(z46=10, z47=20, z48=30, z49=10292020, z50=10292010, z51=10292000, z52=10291000,
            z53=10291010))
    """State 1: Rerun"""
    RestartMachine()

def event_m10_29_1020():
    """Madura-Giant Door in the Shadow Shadow Forest_Initial setting"""
    """State 0,2: [Preset] Madura-The Shadow Shadow Forest Gimmick Door_Initial Settings_SubState"""
    assert (event_m10_29_x29(z36=105405, z37=10292020, z38=10292010, z39=10292000, z40=100001, z41=100002,
            z42=100000, z43=129010020))
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1100():
    """Door 1 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291010, z45=10290401)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1110():
    """Door 2 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291010, z45=10290402)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1120():
    """Door that opens in conjunction with the gimmick door 3"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291010, z45=10290403)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1130():
    """Door 4 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291010, z45=10290404)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1140():
    """Door 5 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291010, z45=10290405)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1150():
    """Door 6 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291010, z45=10290406)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1160():
    """Door 7 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291000, z45=10290407)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1170():
    """Door 8 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291000, z45=10290408)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1180():
    """Door 9 that opens in conjunction with the gimmick door 9"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291000, z45=10290409)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1190():
    """Door 10 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291000, z45=10290410)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1200():
    """Door 11 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291000, z45=10290411)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_1210():
    """Door 12 that opens in conjunction with the gimmick door"""
    """State 0,2: [Preset] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x25(z44=10291000, z45=10290412)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_3000():
    """Navi-mesh changes after unlocking a magician"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_29_x13(z63=300000, z64=0, z65=2, z66=0, z67=102640)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_80000():
    """Rebirth Fire 01_Madura ~ Valent Shadow Forest Connection Path"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_29_x9(z68=1029000, z69=1029099)
    """State 1: Finish"""
    EndMachine()

def event_m10_29_x0(z85=_, z86=_, z87=_, z88=_):
    """[Lib] NPC: Grave Placement: General purpose
    z85: Death map: Global event flag
    z86: Tomb: OBJ instance ID
    z87: Tomb move to: Generator ID
    z88: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z85, 1)
    IsGraveGeneratable(8, z88, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z86, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z86, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_29_x1(z82=_, z83=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z82: Global: death flag
    z83: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z83, 10, 0)
    CompareObjState(1, z83, 20, 0)
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
    IsObjSearched(0, z83)
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

def event_m10_29_x2(z80=_, z81=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z80: Area other flags: Ghost appearance
    z81: Area other flags: Conversation start
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
    SetEventFlag(z80, 1)
    CompareEventFlag(0, z80, 1)
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
    SetEventFlag(z81, 1)
    CompareEventFlag(0, z81, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_29_x3(z80=_, z81=_, z82=_, z83=_, z84=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z80: Ghost Appearance: Area Other Flag
    z81: Conversation start: Area and other flags
    z82: Death: Global event flag
    z83: Tomb: OBJ instance ID
    z84: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z84, 1, 0)
    CompareEventFlag(9, z80, 1)
    CompareObjState(9, z83, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z81, 1)
        CompareEventFlag(0, z81, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_29_x1(z82=z82, z83=z83, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_29_x2(z80=z80, z81=z81, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_29_x4(z78=60, z79=104161):
    """[Lib] NPC: Death determination: General purpose
    z78: Generator ID
    z79: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z79, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z78)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z79, 1)
            CompareEventFlag(0, z79, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_29_x5(z70=115, z71=104270, z72=15, z73=0, z74=102640, z75=1600, z76=15, z77=111356):
    """[Lib] Character: Petrochemical: Key guide
    z70: generator
    z71: Death: Global event flag
    z72: Event action
    z73: Petrified: Area and other flags
    z74: Petrified: Global event flag
    z75: Key guide parameters
    z76: Petrification start state ID
    z77: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z70, z76, 0)
    CompareEventStatus(8, z77, 1, 0)
    CompareEventFlag(2, z73, 1)
    CompareEventFlag(3, z74, 1)
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
    CreateKeyGuideArea(34, z75)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z70)
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
                PlayerActionRequest(z72)
                IsPlayerPlayingMotion(0, z72, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z73, 1)
                CompareEventFlag(0, z73, 1)
                SetEventFlag(z74, 1)
                CompareEventFlag(1, z74, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z72, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_29_x6():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_29_x7(z68=1029000, z69=1029099):
    """[Lib] [execute] Rebirth fire
    z68: Flag start ID
    z69: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z68, z69, 0)
    """State 2: End state"""
    return 0

def event_m10_29_x8():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_29_x9(z68=1029000, z69=1029099):
    """[Lib] [Preset] Rebirth
    z68: Flag start ID
    z69: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_29_x6()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_29_x8()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_29_x7(z68=z68, z69=z69)
    """State 4: End state"""
    return 0

def event_m10_29_x10(z66=0, z67=102640, z65=2, z64=0, z63=300000):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z66: Other flags
    z67: Global flag
    z65: Additional attributes
    z64: Delete attribute
    z63: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z66) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z67) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z63, z65)
        DeleteNavimeshAttribute(z63, z64)
        """State 3: Flag OFF"""
        return 0

def event_m10_29_x11(z66=0, z67=102640):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z66: Other flags
    z67: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z66, 1)
    CompareEventFlag(0, z67, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_29_x12(z63=300000, z64=0, z65=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z63: Navimesh switching point ID
    z64: Additional attributes
    z65: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z63, z64)
    DeleteNavimeshAttribute(z63, z65)
    """State 2: End state"""
    return 0

def event_m10_29_x13(z63=300000, z64=0, z65=2, z66=0, z67=102640):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z63: Navimesh switching point ID
    z64: Additional attributes
    z65: Delete attribute
    z66: Other flags
    z67: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_29_x10(z66=z66, z67=z67, z65=z65, z64=z64, z63=z63)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_29_x11(z66=z66, z67=z67)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_29_x12(z63=z63, z64=z64, z65=z65)
    """State 4: End state"""
    return 0

def event_m10_29_x14(z61=129020107, z62=31):
    """[Lib] [Preset] Get trophy
    z61: Acquisition trigger_other flags
    z62: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z61) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z61, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z62)
    """State 4: End state"""
    return 0

def event_m10_29_x15(z58=115, z59=104271, z60=117):
    """[Lib] NPC: Death determination: For the appearance of the map
    z58: First generator ID
    z59: Death map: Global event flag
    z60: Second generator ID
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z59, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(8, z58)
            IsChrActive(8, z58, 1)
            IsChrDead(9, z60)
            IsChrActive(9, z60, 1)
            if ConditionGroup(8):
                pass
            elif ConditionGroup(9):
                pass
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z59, 1)
            CompareEventFlag(0, z59, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_29_x16(z25=10292000, z26=10291000, z27=10291010, z28=10292020, z29=10292010, z30=129010021,
                     z31=129010022, z32=129010023):
    """[Preset] Madura-empty shadow woods gimmick door_lever operation judgment-opening of gimmick door
    z25: Instance ID of gimmick door OBJ
    z26: Instance ID of the madura lever
    z27: Instance ID of the forest side lever of the imaginary shadow
    z28: Instance ID of Madura side door OBJ
    z29: Instance ID of the door OBJ on the forest side of the imaginary shadow
    z30: Lever operated flag
    z31: Both doors closed flag
    z32: Gimmick door opening completion flag
    """
    """State 0,1: [Reproduction] Madura-Forest Shadow Gimmick Door_Lever Operation Judgment-Gimmick Door Open_SubState"""
    call = event_m10_29_x17(z26=z26, z27=z27, z57=102640, z32=z32, z31=z31, z30=z30)
    if call.Get() == 3:
        pass
    elif call.Get() == 1:
        """State 4: [Execution] Madura-The Shadow Shadow Forest Gimmick Door_Gimmic Door Open_SubState"""
        Label('L0')
        assert event_m10_29_x34(z25=z25, z33=100000, z32=z32)
    elif call.Get() == 2:
        """State 3: [Execution] Madura-The Shadow Shadow Forest Gimmick Door_Both Door Closure_SubState"""
        Label('L1')
        assert event_m10_29_x33(z28=z28, z29=z29, z34=100001, z35=100002, z31=z31)
        Goto('L0')
    elif call.Get() == 0:
        """State 2: [Conditions] Madura-Void Shadow Woods Gimmick Door_Lever Operation Judgment_SubState"""
        assert event_m10_29_x18(z26=z26, z27=z27, z30=z30)
        Goto('L1')
    """State 5: End state"""
    return 0

def event_m10_29_x17(z26=10291000, z27=10291010, z57=102640, z32=129010023, z31=129010022, z30=129010021):
    """[Reproduction] Madura-Forest Shadow Gimmick Door_Lever Operation Judgment-Gimmick Door Open
    z26: Instance ID of the madura lever
    z27: Instance ID of the forest side lever of the imaginary shadow
    z57: [Group condition: Event] Area timer comparison
    z32: Gimmick door opening completion flag
    z31: Both doors closed flag
    z30: Lever operated flag
    """
    """State 0,6: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z26, 1)
    DisableObjKeyGuide(z27, 1)
    """State 2: Did the initial setting event end and unlock the magician's petrification?"""
    assert EventEnded(1020) != 0 and GetEventFlag(z57) != 0
    """State 5: Is the opening of the gimmick door complete?"""
    if GetEventFlag(z32) != 0:
        pass
    else:
        Goto('L0')
    """State 7: Changing the state of the navigation mesh of each door"""
    DeleteNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100002, 2)
    """State 12: Gimmick door opening complete"""
    return 3
    """State 4: Are both doors closed?"""
    Label('L0')
    if GetEventFlag(z31) != 0:
        pass
    else:
        Goto('L1')
    """State 8: Navi mesh on both doors made inaccessible"""
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100002, 2)
    """State 10: Both doors closed"""
    return 1
    """State 3: Has the lever been operated?"""
    Label('L1')
    if GetEventFlag(z30) != 0:
        """State 11: Lever operated"""
        return 2
    else:
        """State 1: Enable key guide for lever"""
        DisableObjKeyGuide(z26, 0)
        DisableObjKeyGuide(z27, 0)
        """State 9: Not executed"""
        return 0

def event_m10_29_x18(z26=10291000, z27=10291010, z30=129010021):
    """[Conditions] Madura-hollow shadow woods gimmick door_lever operation judgment
    z26: Instance ID of the madura lever
    z27: Instance ID of the forest side lever of the imaginary shadow
    z30: Lever operated flag
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z26, 74, 0)
    CompareObjState(0, z27, 74, 0)
    CompareObjState(0, z26, 84, 0)
    CompareObjState(0, z27, 84, 0)
    assert ConditionGroup(0)
    """State 2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z26, 1)
    DisableObjKeyGuide(z27, 1)
    """State 3: Lever operated flag: ON"""
    SetEventFlag(z30, 1)
    """State 4: End state"""
    return 0

def event_m10_29_x19(z17=_, z19=_, z56=_, z22=129010024):
    """[Execution] Madura-empty shadow of the forest gimmick door _ opening the destination door
    z17: Instance ID of moving side door OBJ
    z19: Point ID for navigation mesh change of moving side door
    z56: Destination MAPID
    z22: Destination door opening completion flag
    """
    """State 0,4: Wait for completion of reading destination MAP"""
    IsMapReadAndBackreadStable(0, z56, 1)
    assert ConditionGroup(0)
    """State 1: Open the moving door"""
    ChangeObjState(z17, 70)
    """State 2: Has the moving door fully opened?"""
    CompareObjState(0, z17, 30, 0)
    assert ConditionGroup(0)
    """State 3: Make the navigation mesh of the moving door accessible"""
    DeleteNavimeshAttribute(z19, 2)
    """State 5: Destination door opening completion flag: ON"""
    SetEventFlag(z22, 1)
    """State 6: End state"""
    return 0

def event_m10_29_x20(z46=10, z47=20, z48=30, z49=10292020, z50=10292010, z51=10292000, z52=10291000,
                     z53=10291010):
    """[Preset] Switch global flags related to gimmick doors
    z46: Hit group ID on the Madura side
    z47: Hit group ID on the forest side
    z48: Hit group ID of the gimmick door room
    z49: Instance ID of Madura side door OBJ
    z50: Instance ID of the door OBJ on the forest side of the imaginary shadow
    z51: Instance ID of gimmick door OBJ
    z52: Instance ID of the madura lever
    z53: Instance ID of the forest side lever of the imaginary shadow
    """
    """State 0,1: [Reproduction] Switching global flags related to gimmick doors_SubState"""
    assert event_m10_29_x21()
    """State 2: [Condition] Switch global flags related to gimmick doors_SubState"""
    call = event_m10_29_x22(z46=z46, z47=z47, z48=z48, z49=z49, z50=z50, z52=z52, z53=z53)
    if call.Get() == 0:
        """State 3: [Execution] Switch global flags related to gimmick doors_Madura_SubState"""
        assert event_m10_29_x23(z55=0, z46=z46)
    elif call.Get() == 1:
        """State 4: [Execution] Switching global flags related to gimmick doors_Valve Shadow Forest_SubState"""
        assert event_m10_29_x23(z55=1, z46=z47)
    elif call.Get() == 3:
        """State 5: [Execution] Switching global flags related to gimmick doors_In the room (Destination: Forest of Shadow of Shadows) _SubState"""
        assert event_m10_29_x24(z48=z48, z54=1, z51=z51)
    elif call.Get() == 2:
        """State 6: [Execution] Switching global flags related to gimmick doors_In the room (Destination: Madura) _SubState"""
        assert event_m10_29_x24(z48=z48, z54=0, z51=z51)
    elif call.Get() == 4:
        pass
    """State 7: End state"""
    return 0

def event_m10_29_x21():
    """[Reproduction] Switching global flags related to gimmick doors"""
    """State 0,1: End state"""
    return 0

def event_m10_29_x22(z46=10, z47=20, z48=30, z49=10292020, z50=10292010, z52=10291000, z53=10291010):
    """[Conditions] Switching global flags related to gimmick doors
    z46: Hit group ID on the Madura side
    z47: Hit group ID on the forest side
    z48: Hit group ID of the gimmick door room
    z49: Instance ID of Madura side door OBJ
    z50: Instance ID of the door OBJ on the forest side of the imaginary shadow
    z52: Instance ID of the madura lever
    z53: Instance ID of the forest side lever of the imaginary shadow
    """
    """State 0,1: Which hit group are you on?"""
    IsPlayerOnHitGroup(0, z46, 1)
    IsPlayerOnHitGroup(1, z47, 1)
    IsPlayerOnHitGroup(2, z48, 1)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        Goto('L0')
    elif ConditionGroup(2):
        Goto('L1')
    """State 4: Madura side"""
    return 0
    """State 5: Forest side of the shadow of emptiness"""
    Label('L0')
    return 1
    """State 3: Was the gimmick door lever pulled?"""
    Label('L1')
    CompareObjState(0, z52, 74, 0)
    CompareObjState(0, z53, 74, 0)
    CompareObjState(0, z52, 84, 0)
    CompareObjState(0, z53, 84, 0)
    IsPlayerOnHitGroup(1, z48, 0)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        Goto('L2')
    """State 2: Which door started to close?"""
    CompareObjState(0, z49, 80, 0)
    CompareObjState(1, z50, 80, 0)
    if ConditionGroup(0):
        """State 7: Inside the room (Destination: Forest of Shadow)"""
        return 3
    elif ConditionGroup(1):
        """State 6: Inside the room (destination: Madura)"""
        return 2
    """State 8: Rerun"""
    Label('L2')
    return 4

def event_m10_29_x23(z55=_, z46=_):
    """[Execution] Switching global flags related to gimmick doors
    z55: ON / OFF of global flag
    z46: ID of the hit group you are riding on
    """
    """State 0,1: Change global event flag"""
    SetEventFlag(105405, z55)
    """State 2: Did you disappear from the hit group you were riding on?"""
    IsPlayerOnHitGroup(0, z46, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_29_x24(z48=30, z54=_, z51=10292000):
    """[Execution] Switch global flags related to gimmick doors_in the room
    z48: ID of the hit group you are riding on
    z54: ON / OFF of global flag
    z51: Instance ID of gimmick door OBJ
    """
    """State 0,2: Change global event flag"""
    SetEventFlag(105405, z54)
    """State 1: Was the condition for exiting execution processing satisfied?"""
    CompareObjState(0, z51, 70, 0)
    IsPlayerOnHitGroup(0, z48, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_29_x25(z44=_, z45=_):
    """[Preset] Door that opens in conjunction with the gimmick door
    z44: Linked lever OBJ instance ID
    z45: Instance ID of door OBJ to open
    """
    """State 0,2: [Reproduction] Door that opens in conjunction with the gimmick door_SubState"""
    assert event_m10_29_x27()
    """State 3: [Condition] Door that opens in conjunction with the gimmick door_SubState"""
    call = event_m10_29_x26(z44=z44, z45=z45)
    if call.Get() == 1:
        """State 1: [Execution] Door that opens in conjunction with the gimmick door_SubState"""
        assert event_m10_29_x28(z45=z45)
    elif call.Get() == 0:
        pass
    """State 4: End state"""
    return 0

def event_m10_29_x26(z44=_, z45=_):
    """[Condition] Door that opens in conjunction with gimmick door
    z44: Linked lever OBJ instance ID
    z45: Instance ID of door OBJ to open
    """
    """State 0,2: Has the linked lever been operated?"""
    CompareObjState(0, z44, 74, 0)
    CompareObjState(0, z44, 84, 0)
    assert ConditionGroup(0)
    """State 1: Check the status of the door to be opened"""
    CompareObjState(0, z45, 10, 0)
    if ConditionGroup(0):
        """State 4: Open the door"""
        return 1
    else:
        """State 3: End state"""
        return 0

def event_m10_29_x27():
    """[Reproduction] Door that opens in conjunction with gimmick door"""
    """State 0,1: End state"""
    return 0

def event_m10_29_x28(z45=_):
    """[Execution] Door that opens in conjunction with the gimmick door
    z45: Instance ID of door OBJ to open
    """
    """State 0,1: Open the door"""
    ChangeObjState(z45, 74)
    """State 2: End state"""
    return 0

def event_m10_29_x29(z36=105405, z37=10292020, z38=10292010, z39=10292000, z40=100001, z41=100002, z42=100000,
                     z43=129010020):
    """[Preset] Madura to the shadow of the forest gimmick door _ initial setting
    z36: Intrusion MAP determination flag
    z37: Instance ID of Madura side door OBJ
    z38: Instance ID of OBJ
    z39: OBJ instance ID of the gimmick door
    z40: Point ID for changing the navigation mesh of the Madura side door
    z41: Point ID for navigating mesh change of the forest door
    z42: Point ID for changing the navigation mesh of the gimmick door
    z43: Initialization execution flag
    """
    """State 0,1: [Reproduction] Madura-hollow shadow forest mamic door_initial setting_SubState"""
    call = event_m10_29_x30(z37=z37, z38=z38, z39=z39, z40=z40, z41=z41, z42=z42, z43=z43)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Conditions] Madura-City Shadow Forest Gimmick Door_Initial Settings_SubState"""
        call = event_m10_29_x31(z36=z36)
        if call.Get() == 1:
            """State 4: [Execution] Madura to the Shadow Shadow Forest Gimmick Door_Initial Settings_Madura_SubState"""
            assert event_m10_29_x32(z38=z37, z41=z40, z43=z43)
        elif call.Get() == 0:
            """State 3: [Execution] Madura-The Shadow Shadow Forest Gimmy Door_Initial Setting_The Shadow Shadow Forest_SubState"""
            assert event_m10_29_x32(z38=z38, z41=z41, z43=z43)
    """State 5: End state"""
    return 0

def event_m10_29_x30(z37=10292020, z38=10292010, z39=10292000, z40=100001, z41=100002, z42=100000, z43=129010020):
    """[Reproduction] Madura-empty shadow of the forest gimmick door _ initial setting
    z37: Instance ID of Madura side door OBJ
    z38: Instance ID of OBJ
    z39: OBJ instance ID of the gimmick door
    z40: Point ID for changing the navigation mesh of the Madura side door
    z41: Point ID for navigating mesh change of the forest door
    z42: Point ID for changing the navigation mesh of the gimmick door
    z43: Initialization execution flag
    """
    """State 0,2: Has initialization been performed?"""
    if GetEventFlag(z43) != 0:
        """State 4: Executed"""
        return 1
    else:
        """State 1: Initialize the state of each door and Navimesh"""
        InitializeObj(z37)
        InitializeObj(z38)
        InitializeObj(z39)
        AddNavimeshAttribute(z40, 2)
        AddNavimeshAttribute(z41, 2)
        AddNavimeshAttribute(z42, 2)
        """State 3: Not executed"""
        return 0

def event_m10_29_x31(z36=105405):
    """[Conditions] Madura-Void Shadow Woods Gimmick Door_Initial setting
    z36: Intrusion MAP determination flag
    """
    """State 0,1: Global event flag judgment"""
    CompareEventFlag(0, z36, 0)
    if ConditionGroup(0):
        """State 3: Madura"""
        return 1
    else:
        """State 2: Forest of the shadow of emptiness"""
        return 0

def event_m10_29_x32(z38=_, z41=_, z43=129010020):
    """[Execution] Madura-empty shadow of forest gimmick door _ initial setting
    z38: Intrusion MAP side door instance ID
    z41: Point ID for changing the navigation mesh on the intrusion MAP side door
    z43: Initialization execution flag
    """
    """State 0,1: Set initial state of intrusion MAP side door"""
    ChangeObjState(z38, 30)
    DeleteNavimeshAttribute(z41, 2)
    """State 2: Initialization execution flag: ON"""
    SetEventFlag(z43, 1)
    """State 3: End state"""
    return 0

def event_m10_29_x33(z28=10292020, z29=10292010, z34=100001, z35=100002, z31=129010022):
    """[Execution] Madura-empty shadow of the forest gimmick door_close both doors
    z28: Instance ID of Madura side door OBJ
    z29: Instance ID of the door OBJ on the forest side of the imaginary shadow
    z34: Point ID for changing the navigation mesh of the Madura side door
    z35: Point ID for navigating mesh doors of the Forest of Shadows
    z31: Both doors closed flag
    """
    """State 0,1: Close both doors"""
    ChangeObjState(z28, 80)
    ChangeObjState(z29, 80)
    """State 2: Have both doors been closed?"""
    CompareObjState(8, z28, 10, 0)
    CompareObjState(8, z29, 10, 0)
    assert ConditionGroup(8)
    """State 4: Navi mesh on both doors made inaccessible"""
    AddNavimeshAttribute(z34, 2)
    AddNavimeshAttribute(z35, 2)
    """State 3: Both doors closed flag: ON"""
    SetEventFlag(z31, 1)
    """State 5: End state"""
    return 0

def event_m10_29_x34(z25=10292000, z33=100000, z32=129010023):
    """[Execution] Madura-empty shadow forest forest gimmick door _ gimmick door opening
    z25: Instance ID of gimmick door OBJ
    z33: Point ID for changing the navigation mesh of the gimmick door
    z32: Gimmick door opening completion flag
    """
    """State 0,1: Open the gimmick door"""
    ChangeObjState(z25, 70)
    """State 2: Has the gimmick door fully opened?"""
    CompareObjState(0, z25, 30, 0)
    assert ConditionGroup(0)
    """State 3: Make the gimmick door navigation mesh ready to enter"""
    DeleteNavimeshAttribute(z33, 2)
    """State 4: Gimmick door opening completion flag: ON"""
    SetEventFlag(z32, 1)
    """State 5: End state"""
    return 0

def event_m10_29_x35():
    """[Conditions] Madura-empty shadow forest forest gimmick door _ Gimmick door closure waiting"""
    """State 0,2: Timer start judgment"""
    CompareAreaTimer(0, 0, 0, 0)
    CompareAreaTimer(1, 0, 0, 2)
    if ConditionGroup(0):
        """State 3: Start area timer"""
        StartAreaTimer(0)
    elif ConditionGroup(1):
        """State 4: Restart area timer"""
        RestartAreaTimer(0)
    """State 1: Has the waiting time been exceeded?"""
    CompareAreaTimer(0, 0, 300, 2)
    assert ConditionGroup(0)
    """State 5: Stop area timer"""
    PauseAreaTimer(0)
    """State 6: End state"""
    return 0

def event_m10_29_x36(z20=10292000, z21=100000):
    """[Execution] Madura to the Shadow Shadow Forest Gimmick Door_Closed Gimmick Door
    z20: Instance ID of gimmick door OBJ
    z21: Point ID for changing the navigation mesh of the gimmick door
    """
    """State 0,1: Close the gimmick door"""
    ChangeObjState(z20, 80)
    """State 2: Has the gimmick door been closed?"""
    CompareObjState(0, z20, 10, 0)
    assert ConditionGroup(0)
    """State 3: Unable to enter the gimmick door navigation mesh"""
    AddNavimeshAttribute(z21, 2)
    """State 4: Reset gimmick door operation determination flag"""
    SetEventFlag(129010021, 0)
    SetEventFlag(129010022, 0)
    SetEventFlag(129010023, 0)
    SetEventFlag(129010024, 0)
    """State 5: Reset area timer"""
    EndAreaTimer(0)
    """State 6: End state"""
    return 0

def event_m10_29_x37(z15=105405, z16=10292020, z17=10292010, z18=100001, z19=100002, z20=10292000, z21=100000,
                     z22=129010024):
    """[Preset] Madura-Gimmick Shadow Forest Forest Gimmick Door_Destination Determination-Gimmick Door Closure
    z15: Global scenario flag ID for intrusion MAP determination
    z16: Instance ID of Madura side door OBJ
    z17: Instance ID of the door OBJ on the forest side of the imaginary shadow
    z18: Point ID for changing the navigation mesh of the Madura side door
    z19: Point ID for navigating mesh doors of the Forest of Shadows
    z20: Instance ID of gimmick door OBJ
    z21: Point ID for changing the navigation mesh of the gimmick door
    z22: Destination door opening completion flag
    """
    """State 0,2: [Reproduction] Madura-Forest Shadow Gimmick Door_Destination Determination-Gimmick Door Closure_SubState"""
    call = event_m10_29_x39(z15=z15, z16=z16, z17=z17, z18=z18, z19=z19, z23=10040000, z24=10320000,
                            z22=z22)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 1: [Conditions] Madura-Void Shadow Forest Gimmick Door_Destination Determination_SubState"""
        call = event_m10_29_x38(z15=z15)
        if call.Get() == 0:
            """State 6: [Execution] Madura-The Shadow Shadow Forest Gimmick Door_Opening the Destination Door (Madura) _SubState"""
            assert event_m10_29_x19(z17=z16, z19=z18, z56=10040000, z22=z22)
        elif call.Get() == 1:
            """State 5: [Execution] Madura-The Shadow Shadow Forest Gimmick Door_Opening the Destination Door (The Shadow Shadow Forest) _SubState"""
            assert event_m10_29_x19(z17=z17, z19=z19, z56=10320000, z22=z22)
    """State 4: [Conditions] Madura to the Shadow Shadow Forest Gimmick Door_Gimmick Door Closed Waiting_SubState"""
    assert event_m10_29_x35()
    """State 3: [Execution] Madura-The Shadow Shadow Forest Gimmick Door_Gimmic Door Closure_SubState"""
    assert event_m10_29_x36(z20=z20, z21=z21)
    """State 7: End state"""
    return 0

def event_m10_29_x38(z15=105405):
    """[Conditions] Madura to the empty shadow of the forest gimmick door_destination judgment
    z15: Global scenario flag ID for intrusion MAP determination
    """
    """State 0,1: Intrusion MAP determination"""
    CompareEventFlag(0, z15, 0)
    if ConditionGroup(0):
        """State 2: Move to: Madura side"""
        return 0
    else:
        """State 3: Move to: Forest side of the imaginary shadow"""
        return 1

def event_m10_29_x39(z15=105405, z16=10292020, z17=10292010, z18=100001, z19=100002, z23=10040000, z24=10320000,
                     z22=129010024):
    """[Reproduction] Madura-empty shadow forest forest gimmick_moving destination judgment-gimmick door closure
    z15: Global scenario flag ID for intrusion MAP determination
    z16: Instance ID of Madura side door OBJ
    z17: Instance ID of the door OBJ on the forest side of the imaginary shadow
    z18: Point ID for changing the navigation mesh of the Madura side door
    z19: Point ID for navigating mesh doors of the Forest of Shadows
    z23: Madura MAPID
    z24: MAPID of the Forest of Shadow
    z22: Destination door opening completion flag
    """
    """State 0,1: Is the destination door open?"""
    if GetEventFlag(z22) != 0:
        pass
    else:
        Goto('L0')
    """State 2: Intrusion MAP determination"""
    CompareEventFlag(0, z16, 1)
    if GetEventFlag(z15) != 1:
        """State 4: Wait for completion of reading Madura MAP"""
        IsMapReadAndBackreadStable(0, z23, 1)
        assert ConditionGroup(0)
        """State 5: Open the Madura side door"""
        ChangeObjState(z16, 30)
        """State 7: Made the Madura side door mesh mesh accessible"""
        DeleteNavimeshAttribute(z18, 2)
    else:
        """State 3: Waiting for completion of reading of the Shadow Shadow Forest MAP"""
        IsMapReadAndBackreadStable(0, z24, 1)
        assert ConditionGroup(0)
        """State 6: Open the door on the forest side of the hollow shadow"""
        ChangeObjState(z17, 30)
        """State 8: Navimesh of the door on the forest side of the empty shadow is ready to enter"""
        DeleteNavimeshAttribute(z19, 2)
    """State 9: Destination door opening complete"""
    return 0
    """State 10: Destination door opening not completed"""
    Label('L0')
    return 1

def event_m10_29_x40():
    """[DC] [Reproduction] Activating enemy in conjunction with OBJ_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_29_x41(z7=10291000, z8=10290407, z9=10290408, z10=10290410, z11=10290411, z12=10291900,
                     z13=10291910):
    """[DC] [Condition] Enemies start in conjunction with OBJ_Madura side
    z7: Linked lever OBJ instance ID
    z8: Door ①OBJ instance ID
    z9: Door ② OBJ instance ID
    z10: Door ③ OBJ instance ID
    z11: Door ④ OBJ instance ID
    z12: Flame barrel ①OBJ instance ID
    z13: Flame barrel ② OBJ instance ID
    """
    """State 0,1: The interlocked lever is operated or the door is destroyed or the flame barrel is destroyed"""
    CompareObjState(0, z7, 74, 0)
    CompareObjState(0, z7, 84, 0)
    CompareObjState(0, z8, 50, 0)
    CompareObjState(0, z9, 50, 0)
    CompareObjState(0, z10, 50, 0)
    CompareObjState(0, z11, 50, 0)
    CompareObjState(0, z12, 50, 0)
    CompareObjState(0, z13, 50, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_29_x42(z6=_):
    """[DC] [execution] Enemy starts in conjunction with OBJ
    z6: Enemy activation flag
    """
    """State 0,1: Flag ON"""
    SetEventFlag(z6, 1)
    """State 2: End state"""
    return 0

def event_m10_29_x43(z1=10291010, z2=10290403, z3=10290404, z4=10290405, z5=10290406):
    """[DC] [Conditions] Enemies are activated in conjunction with OBJ.
    z1: Linked lever OBJ instance ID
    z2: Door ①OBJ instance ID
    z3: Door ② OBJ instance ID
    z4: Door ③ OBJ instance ID
    z5: Door ④ OBJ instance ID
    """
    """State 0,1: The door with the linked lever operated or the door is destroyed"""
    CompareObjState(0, z1, 74, 0)
    CompareObjState(0, z1, 84, 0)
    CompareObjState(0, z2, 50, 0)
    CompareObjState(0, z3, 50, 0)
    CompareObjState(0, z4, 50, 0)
    CompareObjState(0, z5, 50, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_29_x44(z7=10291000, z8=10290407, z9=10290408, z10=10290410, z11=10290411, z12=10291900,
                     z13=10291910, z14=129020010):
    """[DC] [Preset] Enemy activation linked to OBJ_Madura side
    z7: Linked lever OBJ instance ID
    z8: Door ①OBJ instance ID
    z9: Door ② OBJ instance ID
    z10: Door ③ OBJ instance ID
    z11: Door ④ OBJ instance ID
    z12: Flame barrel ①OBJ instance ID
    z13: Flame barrel ② OBJ instance ID
    z14: Enemy activation flag
    """
    """State 0,1: [DC] [Reproduction] Activating enemy in conjunction with OBJ_Sky_SubState"""
    assert event_m10_29_x40()
    """State 3: [DC] [Condition] Enemies start in conjunction with OBJ_Madura side_SubState"""
    assert event_m10_29_x41(z7=z7, z8=z8, z9=z9, z10=z10, z11=z11, z12=z12, z13=z13)
    """State 2: [DC] [execution] Enemy activation linked to OBJ_SubState"""
    assert event_m10_29_x42(z6=z14)
    """State 4: End state"""
    return 0

def event_m10_29_x45(z1=10291010, z2=10290403, z3=10290404, z4=10290405, z5=10290406, z6=129020011):
    """[DC] [Preset] Enemies are activated in conjunction with OBJ.
    z1: Linked lever OBJ instance ID
    z2: Door ①OBJ instance ID
    z3: Door ② OBJ instance ID
    z4: Door ③ OBJ instance ID
    z5: Door ④ OBJ instance ID
    z6: Enemy activation flag
    """
    """State 0,1: [DC] [Reproduction] Activating enemy in conjunction with OBJ_Sky_SubState"""
    assert event_m10_29_x40()
    """State 3: [DC] [Condition] Enemies start in conjunction with OBJ"""
    assert event_m10_29_x43(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5)
    """State 2: [DC] [execution] Enemy activation linked to OBJ_SubState"""
    assert event_m10_29_x42(z6=z6)
    """State 4: End state"""
    return 0

def event_m10_29_111242():
    """OBJ: Moonlight Jun: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_29_x0(z85=104161, z86=10294000, z87=61, z88=7430)

def event_m10_29_111243():
    """OBJ: Satoshi Moonlight: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7430:Benhart of Jugo
    event_m10_29_x3(z80=129010100, z81=129020101, z82=104160, z83=10294000, z84=111242, npc1=7430)

def event_m10_29_111244():
    """OBJ: Satoshi Moonlight: Judgment of death"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_29_x4(z78=60, z79=104161)

def event_m10_29_111352():
    """OBJ: Magician: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_29_x0(z85=104271, z86=10294100, z87=116, z88=7630)

def event_m10_29_111353():
    """OBJ: Magician: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7630:Rosabeth of Melfia
    event_m10_29_x3(z80=129010110, z81=129020111, z82=104270, z83=10294100, z84=111352, npc1=7630)

def event_m10_29_111354():
    """OBJ: Magician: Death check"""
    """State 0,1: [Lib] NPC: Death decision: _SubState for the map appearance"""
    event_m10_29_x15(z58=115, z59=104271, z60=117)

def event_m10_29_111355():
    """OBJ: Magician: Petrification setting"""
    """State 0,1: [Lib] Character: Petrified: Key Guide_SubState"""
    event_m10_29_x5(z70=115, z71=104270, z72=15, z73=0, z74=102640, z75=1600, z76=15, z77=111356)

def event_m10_29_111356():
    """OBJ: Magician: Appearance setting"""
    """State 0,1: Appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Appearance setting: Death determination"""
    CompareEventFlag(0, 104270, 1)
    if ConditionGroup(0):
        """State 6: Appearance setting: Madura connection: Impossible to appear"""
        Label('L0')
        SetEventFlag(102651, 0)
        CompareEventFlag(0, 102651, 0)
        assert ConditionGroup(0)
    else:
        """State 4: Appearance setting: Migration determination"""
        CompareEventFlag(8, 102650, 1)
        CompareEventFlag(8, 103771, 0)
        if ConditionGroup(8):
            Goto('L0')
        else:
            """State 5: Appearance setting: Petrification judgment"""
            CompareEventFlag(0, 102640, 1)
            if ConditionGroup(0):
                Goto('L0')
            else:
                """State 7: Appearance setting: Madura connection: Appearance allowed"""
                SetEventFlag(102651, 1)
                ExecuteEvent(111355)
                CompareEventFlag(0, 102651, 1)
                assert ConditionGroup(0)
    """State 3: Appearance setting: System: Exit"""
    EndMachine()

def event_m10_29_111357():
    """OBJ: Magician: Move setting"""
    """State 0,1: Move setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 5: Appearance setting: Death determination"""
        CompareEventFlag(0, 104270, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 6: Appearance setting: Migration determination"""
            CompareEventFlag(8, 102650, 1)
            CompareEventFlag(8, 103771, 0)
            if ConditionGroup(8):
                pass
            else:
                """State 3: Movement setting: Judgment release judgment"""
                CompareEventFlag(0, 102640, 0)
                CompareEventFlag(8, 102652, 1)
                CompareEventFlag(8, 102653, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(8):
                    pass
                else:
                    """State 4: Move setting: Move permission"""
                    SetEventFlag(102641, 1)
                    CompareEventFlag(0, 102641, 1)
                    assert ConditionGroup(0)
                    """State 8: Move setting: Previous generator: Erase"""
                    DeleteEnemyByGeneratorGroup(60, 0)
                    Goto('L0')
        """State 7: Move setting: Stop generation"""
        SetEventFlag(102641, 0)
        CompareEventFlag(0, 102641, 0)
        assert ConditionGroup(0)
    """State 2: Move setting: System: Exit"""
    Label('L0')
    EndMachine()

def event_m10_29_111358():
    """OBJ: Magician: Character Erasure"""
    """State 0,1: Character erase: Start"""
    CompareEventStatus(0, 111358, 1, 0)
    assert ConditionGroup(0)
    """State 2: Character erase: Erase judgment"""
    CompareEventFlag(0, 102641, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 4: Character erase: Erase: Standby"""
        CompareEventFlag(8, 102640, 1)
        CompareEventFlag(8, 102641, 0)
        IsChrActive(8, 115, 0)
        assert ConditionGroup(8)
        """State 5: Move setting: Previous generator: Erase"""
        SetEventFlag(102641, 1)
        DeleteEnemyByGeneratorGroup(60, 0)
        CompareEventFlag(0, 102641, 1)
        assert ConditionGroup(0)
    """State 3: Character erasure: System: Exit"""
    EndMachine()

def event_m10_29_111359():
    """OBJ: Magician: Character Erasure 2"""
    """State 0,1,3: Character erase: Erase: Standby"""
    CompareEventFlag(8, 102640, 1)
    CompareEventFlag(8, 102641, 1)
    CompareEventFlag(8, 102652, 1)
    CompareEventFlag(8, 102653, 1)
    IsChrActive(8, 117, 0)
    CompareEventFlag(8, 103771, 0)
    assert ConditionGroup(8)
    """State 4: Move setting: Previous generator: Erase"""
    DeleteEnemyByGeneratorGroup(61, 0)
    assert ConditionGroup(0)
    """State 2: Character erasure: System: Exit"""
    EndMachine()

def event_m10_29_120110():
    """Trophy: Moonlight Sword"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_29_x14(z61=129020107, z62=31)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_29_4000000():
    """[DC] Activating enemy linked to OBJ_Madura side"""
    """State 0,2: [DC] [Preset] Enemy activation linked to OBJ_Madura side_SubState"""
    assert (event_m10_29_x44(z7=10291000, z8=10290407, z9=10290408, z10=10290410, z11=10290411, z12=10291900,
            z13=10291910, z14=129020010))
    """State 1: Finish"""
    EndMachine()

def event_m10_29_4000010():
    """[DC] Enemies start in conjunction with OBJ."""
    """State 0,2: [DC] [Preset] Enemies start in conjunction with OBJ"""
    assert event_m10_29_x45(z1=10291010, z2=10290403, z3=10290404, z4=10290405, z5=10290406, z6=129020011)
    """State 1: Finish"""
    EndMachine()

