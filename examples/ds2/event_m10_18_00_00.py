# -*- coding: utf-8 -*-
def event_m10_18_1000():
    """Ship movement by bell"""
    """State 0,2: [Preset] Ship movement by bell_SubState"""
    assert event_m10_18_x84(z22=10182000, flag2=118000010, z23=10182001, z24=100000, z25=10182002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_1010():
    """Lever to ring the bell"""
    """State 0,2: [Preset] Lever that rings the bell_SubState"""
    assert event_m10_18_x80(z20=10182001, z21=10181002)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_18_1020():
    """Switching OBJ drawing on board"""
    """State 0,2: [Preset] Onboard OBJ drawing switching_SubState"""
    assert event_m10_18_x99(flag1=118000010, z8=10182000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_2000():
    """[Insect key] For starting the lighthouse"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_18_x20(z75=10181050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_3000():
    """Bright area from the start"""
    """State 0,1: Bright area ON"""
    ChangeMapAreaBrightnessSetting(300000, 1)
    ChangeMapAreaBrightnessSetting(300001, 1)
    ChangeMapAreaBrightnessSetting(300002, 1)
    ChangeMapAreaBrightnessSetting(300003, 1)
    ChangeMapAreaBrightnessSetting(300004, 1)
    ChangeMapAreaBrightnessSetting(300005, 1)
    ChangeMapAreaBrightnessSetting(300006, 1)
    ChangeMapAreaBrightnessSetting(300007, 1)
    ChangeMapAreaBrightnessSetting(300008, 1)
    ChangeMapAreaBrightnessSetting(300009, 1)
    ChangeMapAreaBrightnessSetting(300010, 1)
    ChangeMapAreaBrightnessSetting(300011, 1)
    ChangeMapAreaBrightnessSetting(300013, 1)
    ChangeMapAreaBrightnessSetting(300014, 1)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4000():
    """Lighting that works with bug keys"""
    """State 0,2: [Preset] Lighting_SubState that lights when the lighthouse starts"""
    assert event_m10_18_x69(z29=10181050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_6000():
    """Boss battle water level rise"""
    """State 0,2: [Preset] Boss Battle_Water Level Rise_SubState"""
    assert event_m10_18_x61(z34=10182100, flag3=118000081)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_7000():
    """Boss: Double Sided Warrior: Snake Head _ Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_18_x7(flag6=118000081, z80=700000, z81=700000, z82=101, z83=1018000, z84=118020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_8000():
    """Breaking the wooden board brightens (after the insect key lights up)"""
    """State 0,2: [Preset] Breaking the wooden board brightens (after the insect key lights) _SubState"""
    assert event_m10_18_x65(z30=10181200, z31=10180010, z32=10181014, z33=800000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_8010():
    """When the wooden board is broken, it becomes brighter (after the insect key lights up) _2"""
    """State 0,2: [Preset] Breaking the wooden board brightens (after the insect key lights) _SubState"""
    assert event_m10_18_x65(z30=10181201, z31=10180000, z32=10181014, z33=801000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_8020():
    """Breaking the wooden board brightens (after the insect key lights up) _3"""
    """State 0,2: [Preset] Breaking the wooden board brightens (after the insect key lights) _SubState"""
    assert event_m10_18_x65(z30=10181202, z31=10180020, z32=10181014, z33=802000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_9000():
    """Iron fence that can be passed with a hanging leather lever"""
    """State 0,2: [Preset] Iron fence_SubState opened with lever"""
    assert event_m10_18_x90(z17=10181301, z18=10181300, z19=900000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_10000():
    """Connection flag ON"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_18_x30(z61=105415, z62=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_18_11000():
    """Open the door or approach the enemy by approaching"""
    """State 0,2: [Preset] Opening the door or approaching the enemy _SubState"""
    assert event_m10_18_x73(z26=10180402, z27=1100000, z28=118020020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_12000():
    """Dark Hidden Wall Destruction 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z70=10181020, z71=20, z72=1200000, z73=0, z74=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_12010():
    """Dark Hidden Wall Destruction 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z70=10181021, z71=20, z72=1201000, z73=0, z74=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_12020():
    """Destroy the door when executing Wall Destruction 1"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_18_x95(z9=10181020, z10=10180400)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_12030():
    """Destroy the door when executing Wall Destroy 2"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_18_x95(z9=10181021, z10=10180401)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_13000():
    """Oil bottle_01"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z49=10181400, z50=10181450, z51=40, z52=240, z53=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z44=10181450, z45=40, z46=240, z47=0, z48=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_14000():
    """A ship leaves the compass"""
    """State 0,3: [Preset] The ship leaves the compass _SubState"""
    call = event_m10_18_x89(z5=10182300, z6=101820, z7=100010)
    if call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()

def event_m10_18_15000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z70=10181040, z71=20, z72=1500000, z73=0, z74=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_18000():
    """Navi mesh change of destructible wall"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z70=10181022, z71=20, z72=1800000, z73=0, z74=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_19000():
    """Moonlight on the ship"""
    """State 0,2: [Preset] Moonlight _SubState for ships"""
    assert event_m10_18_x94(z11=1900000, z12=1900003, z13=19000, z14=118000010, z15=10182000, z16=19010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_18_20000():
    """Navimesh changes due to scaffold destruction"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z70=10181230, z71=20, z72=2000000, z73=2, z74=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_80000():
    """Rebirth Fire 01_ Entrance Limestone Cave"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_18_x35(z58=1018000, z59=1018099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_x0(z6=101820, z104=0, z105=10160000, z7=100010):
    """[Lib] Warp between maps after poly play
    z6: Pre-warp poly play ID
    z104: Poly Play ID after Warp
    z105: Map ID
    z7: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z6, z104, z105, z7, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_18_x1(z100=_, z101=_, z102=_, z103=_):
    """[Lib] NPC: Grave Placement: General purpose
    z100: Death map: Global event flag
    z101: Tomb: OBJ instance ID
    z102: Tomb move to: Generator ID
    z103: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z100, 1)
    IsGraveGeneratable(8, z103, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z101, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z101, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_18_x2(z97=_, z98=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z97: Global: death flag
    z98: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z98, 10, 0)
    CompareObjState(1, z98, 20, 0)
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
    IsObjSearched(0, z98)
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

def event_m10_18_x3(z95=_, z96=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z95: Area other flags: Ghost appearance
    z96: Area other flags: Conversation start
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
    SetEventFlag(z95, 1)
    CompareEventFlag(0, z95, 1)
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
    SetEventFlag(z96, 1)
    CompareEventFlag(0, z96, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_18_x4(z95=_, z96=_, z97=_, z98=_, z99=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z95: Ghost Appearance: Area Other Flag
    z96: Conversation start: Area and other flags
    z97: Death: Global event flag
    z98: Tomb: OBJ instance ID
    z99: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z99, 1, 0)
    CompareEventFlag(9, z95, 1)
    CompareObjState(9, z98, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z96, 1)
        CompareEventFlag(0, z96, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_18_x2(z97=z97, z98=z98, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_18_x3(z95=z95, z96=z96, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_18_x5(z87=102480, z88=102481, z89=102483, z90=102487, z91=102492, z92=102485, z93=102486,
                    z94=102488):
    """[Lib] NPC: Woman Knight: Appearance Judgment
    z87: Sub 1 encountering: Global event flag
    z88: During sub-2 encounter: Global event flag
    z89: Sub 3 encountering: Global event flag
    z90: Generation stop: Global event flag
    z91: Appearance permission: Global event flag
    z92: Sub 1 generation stop: Global event flag
    z93: Sub 2 generation stop: Global event flag
    z94: Sub 3 generation stop: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    CompareEventFlag(1, 104190, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Appearance determination: Death determination"""
        CompareEventFlag(0, 104190, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 6: Appearance determination: Generation stop determination"""
            CompareEventFlag(0, z90, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 2: Appearance determination: Judgment while encountering other maps"""
                CompareEventFlag(8, z87, 1)
                CompareEventFlag(8, z92, 0)
                CompareEventFlag(9, z88, 1)
                CompareEventFlag(9, z93, 0)
                CompareEventFlag(10, z89, 1)
                CompareEventFlag(10, z94, 0)
                if ConditionGroup(8):
                    pass
                elif ConditionGroup(9):
                    pass
                elif ConditionGroup(10):
                    pass
                else:
                    """State 8: Appearance determination: Adversity determination"""
                    CompareEventFlag(0, 103692, 1)
                    CompareEventFlag(1, 103693, 1)
                    CompareEventFlag(2, 103691, 1)
                    CompareEventFlag(3, 103694, 1)
                    if ConditionGroup(0):
                        pass
                    elif ConditionGroup(1):
                        pass
                    elif ConditionGroup(2):
                        pass
                    elif ConditionGroup(3):
                        pass
                    else:
                        """State 4: Appearance determination: Appearance allowed"""
                        SetEventFlag(z91, 1)
                        CompareEventFlag(0, z91, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
        """State 3: Appearance judgment: Appearance impossible"""
        SetEventFlag(z91, 0)
        CompareEventFlag(0, z91, 0)
        assert ConditionGroup(0)
    """State 5: Appearance determination: System: Event end"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_18_x6(z85=_, z86=_):
    """[Lib] NPC: Death determination: General purpose
    z85: Generator ID
    z86: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z86, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z85)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z86, 1)
            CompareEventFlag(0, z86, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_18_x7(flag6=118000081, z80=700000, z81=700000, z82=101, z83=1018000, z84=118020080, mode2=0):
    """[Lib] [Preset] Boss Battle Start
    flag6: Boss destruction flag
    z80: Start point ID
    z81: End point ID
    z82: Sound ID
    z83: Boss Battle ID
    z84: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_18_x8(flag6=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_18_x9(z80=z80, z81=z81)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_18_x10(z82=z82, z83=z83, z84=z84)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_18_x11()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_18_x12(z83=z83)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_18_x13(z82=z82, z83=z83, z84=z84, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_18_x8(flag6=118000081):
    """[Reproduction] Boss Battle_Start
    flag6: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag6) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_18_x9(z80=700000, z81=700000):
    """[Condition] Boss Battle_Start
    z80: Start point ID
    z81: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z80, z81, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z80, z81, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x10(z82=101, z83=1018000, z84=118020080):
    """[Execution] Boss Battle_Start
    z82: Sound ID
    z83: Boss Battle ID
    z84: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z82)
    """State 1: Boss battle start notification"""
    StartBossFight(z83)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z84, 1)
    """State 4: End state"""
    return 0

def event_m10_18_x11():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x12(z83=1018000):
    """[Condition] Boss Battle_End Judgment
    z83: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z83, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x13(z82=101, z83=1018000, z84=118020080, mode2=0):
    """[Execute] Boss Battle_End
    z82: Sound ID
    z83: Boss Battle ID
    z84: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z84, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z83)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z82)
    """State 5: End state"""
    return 0

def event_m10_18_x14(z75=10181050):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z75: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z75, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z75, 10)
        assert CompareObjStateId(z75, 10, 0)
    elif CompareObjStateId(z75, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z75, 74, 1) and CompareObjStateId(z75, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_18_x15(z75=10181050, mode1=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z75: Object instance ID
    mode1: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z75)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode1) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_18_x16(z75=10181050, z77=38, z78=12, z79=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z75: Object instance ID
    z77: Key guide type
    z78: Event action
    z79: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z75, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z75, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z75, 30)
        assert CompareObjStateId(z75, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z75, z77, z78)
        assert PlayerIsInEventAction(z78) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z78, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z75, 74, 0)
        CompareObjState(1, z75, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z79)
            assert CompareObjStateId(z75, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z75, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_18_x17(z75=10181050, z76=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z75: Object instance ID
    z76: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z75, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_18_x18(z75=10181050):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z75: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z75, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x19():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x20(z75=10181050):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z75: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_18_x14(z75=z75)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_18_x18(z75=z75)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_18_x19()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_18_x15(z75=z75, mode1=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_18_x16(z75=z75, z77=38, z78=12, z79=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_18_x17(z75=z75, z76=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_18_x21(z70=_, z71=20, z72=_, z73=_, z74=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z70: Object instance ID
    z71: OBJ state ID
    z72: Navimesh switching point ID
    z73: Additional attributes
    z74: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_18_x22(z70=z70, z71=z71, z72=z72, z74=z74, z73=z73)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_18_x23(z70=z70, z71=z71, z72=z72)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_18_x24(z70=z70, z71=z71, z72=z72, z73=z73, z74=z74)
    """State 4: End state"""
    return 0

def event_m10_18_x22(z70=_, z71=20, z72=_, z74=_, z73=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z70: Target OBJ instance ID
    z71: Target OBJ state ID
    z72: Navimesh switching point ID
    z74: Additional attributes
    z73: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z70, z71, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z72, z74)
        DeleteNavimeshAttribute(z72, z73)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_18_x23(z70=_, z71=20, z72=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z70: Target OBJ instance ID
    z71: Target OBJ state ID
    z72: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z70, z71, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x24(z70=_, z71=20, z72=_, z73=_, z74=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z70: Target OBJ instance ID
    z71: Target OBJ state ID
    z72: Navimesh switching point ID
    z73: Additional attributes
    z74: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z72, z73)
    DeleteNavimeshAttribute(z72, z74)
    """State 2: End state"""
    return 0

def event_m10_18_x25(z69=102721):
    """[Lib] Appearance determination: Magician
    z69: Appearance permission: Global event flag
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
        SetEventFlag(z69, 1)
        CompareEventFlag(0, z69, 1)
        assert ConditionGroup(0)
    """State 5: Generation stop judgment: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_18_x26(z63=102502, z64=566, z65=104190, z66=60, z67=103690, z68=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z63: White Phantom can appear: Global event flag
    z64: White Phantom: Generator ID
    z65: Death: Global event flag
    z66: Body: Generator group ID
    z67: Hostile: Global event flag
    z68: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z64)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z65, 1)
        CompareEventFlag(1, z67, 1)
        CompareEventFlag(2, z63, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z64)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z65, 1)
            CompareEventFlag(1, z67, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z64)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z65, 1)
            CompareEventFlag(1, z67, 1)
            HasNpcPhantomSpawned(2, z64, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z66, 0)
                HasNpcPhantomSpawned(0, z64, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z64)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_18_x27():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x28():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x29(z61=105415, z62=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z61: Global event flag for connection
    z62: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z61, z62)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z61, z62)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_18_x30(z61=105415, z62=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z61: Global event flag for connection
    z62: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_18_x27()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_18_x28()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_18_x29(z61=z61, z62=z62)
    """State 4: End state"""
    return 0

def event_m10_18_x31(z60=567):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z60: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z60)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_18_x32():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x33(z58=1018000, z59=1018099):
    """[Lib] [execute] Rebirth fire
    z58: Flag start ID
    z59: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z58, z59, 0)
    """State 2: End state"""
    return 0

def event_m10_18_x34():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x35(z58=1018000, z59=1018099):
    """[Lib] [Preset] Rebirth
    z58: Flag start ID
    z59: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_18_x32()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_18_x34()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_18_x33(z58=z58, z59=z59)
    """State 4: End state"""
    return 0

def event_m10_18_x36(z54=118000081, z55=102498, z56=204, z57=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z54: Defeat Boss 1: Area and other flags
    z55: Summon Achievement: Global Event Flag
    z56: Summon achievement count: global variable
    z57: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z55, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z54, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z56, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z56, NpcInfoValue(z57, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z55, 1)
                CompareEventFlag(0, z55, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_18_x37():
    """[Lib] [Reproduction] Oil 壺 Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x38(z49=_):
    """[Lib] [Conditions]
    z49: Oil bottle OBJ instance ID
    """
    """State 0,1: Was the oil bottle broken?"""
    IsObjBroken(0, z49, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x39(z50=_, z51=_, z52=_, z53=1):
    """[Lib] [execution]
    z50: Tar OBJ instance ID for firewood
    z51: Hit group ID
    z52: Replacement GMID
    z53: Change destination GM slot
    """
    """State 0,1: Oil tar display: 30"""
    ChangeObjState(z50, 30)
    """State 2: Change of material"""
    SetGroundMaterial(z51, z52, z53)
    """State 3: End state"""
    return 0

def event_m10_18_x40(z49=_, z50=_, z51=_, z52=_, z53=1):
    """[Lib] [Preset] Oil bottle
    z49: Oil bottle OBJ instance ID
    z50: Tar OBJ instance ID for firewood
    z51: Hit group ID
    z52: Replacement GMID
    z53: Change destination GM slot
    """
    """State 0,1: [Lib] [Reproduction] Oil bottle_Sky_SubState"""
    assert event_m10_18_x37()
    """State 3: [Lib] [Conditions] Oil 壺 _SubState"""
    assert event_m10_18_x38(z49=z49)
    """State 2: [Lib] [Execution] Oil bottle_SubState"""
    assert event_m10_18_x39(z50=z50, z51=z51, z52=z52, z53=z53)
    """State 4: End state"""
    return 0

def event_m10_18_x41(z45=_, z46=_, z48=1):
    """[Lib] [Reproduction] Tar material change
    z45: Hit group ID
    z46: Replacement GMID
    z48: Change destination GM slot
    """
    """State 0,1: Material change_initialization"""
    SetGroundMaterial(z45, z46, z48)
    """State 2: End state"""
    return 0

def event_m10_18_x42(z44=_):
    """[Lib] [Condition] Tar material change
    z44: OBJ instance ID of tar
    """
    """State 0,1: Did tar burn out?"""
    CompareObjState(0, z44, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x43(z44=_, z45=_, z46=_, z47=0):
    """[Lib] [execution] Tar material change
    z44: OBJ instance ID of tar
    z45: Hit group ID
    z46: Replacement GMID
    z47: Change destination GM slot
    """
    """State 0,1: Change of material"""
    SetGroundMaterial(z45, z46, z47)
    """State 2: End state"""
    return 0

def event_m10_18_x44(z44=_, z45=_, z46=_, z47=0, z48=1):
    """[Lib] [Preset] Tar material change
    z44: OBJ instance ID of tar
    z45: Hit group ID
    z46: Replace_GMID
    z47: After change_GM slot
    z48: Before change_GM slot
    """
    """State 0,1: [Reproduction] Tar material change_SubState"""
    assert event_m10_18_x41(z45=z45, z46=z46, z48=z48)
    """State 3: [Condition] Tar material change_SubState"""
    assert event_m10_18_x42(z44=z44)
    """State 2: [Execution] Tar material change_SubState"""
    assert event_m10_18_x43(z44=z44, z45=z45, z46=z46, z47=z47)
    """State 4: End state"""
    return 0

def event_m10_18_x45(flag5=118020109, z43=33):
    """[Lib] [Preset] Get trophy
    flag5: Acquisition trigger_other flags
    z43: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag5) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag5, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z43)
    """State 4: End state"""
    return 0

def event_m10_18_x46(z41=9000, z42=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z41: Generator ID
    z42: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z41, z42)
    """State 2: End state"""
    return 0

def event_m10_18_x47(z41=9000, z42=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z41: Generator ID
    z42: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z41, z42, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_18_x48(z41=9000):
    """[Lib] [DC] [Condition] Transparent characters
    z41: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z41)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x49(z41=9000, z42=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z41: Generator ID
    z42: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_18_x47(z41=z41, z42=z42)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_18_x48(z41=z41)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_18_x46(z41=z41, z42=z42)
    """State 4: End state"""
    return 0

def event_m10_18_x50():
    """[Lib] [DC] [Reproduction] Character _ Unlockable management _ Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x51(z37=_, z38=7, z39=1):
    """[Lib] [DC] [Condition] Character _ Unlockable management
    z37: Generator ID
    z38: Share flag
    z39: Comparison value
    """
    """State 0,1: State judgment"""
    CompareChrEzStateValue(0, z37, z38, z39, 1)
    CompareChrEzStateValue(1, z37, z38, z39, 0)
    if ConditionGroup(1):
        """State 3: Can lock"""
        return 1
    elif ConditionGroup(0):
        """State 2: Can't lock"""
        return 0

def event_m10_18_x52(z37=_, z38=7, z39=1, z40=170000000):
    """[Lib] [DC] [Execution] Character _ Unlockable management
    z37: Generator ID
    z38: Share flag
    z39: Comparison value
    z40: Special effect ID
    """
    """State 0,1: Grants a non-locking effect"""
    SetEnemySpEffect(z37, z40, 19, 4)
    """State 2: State judgment or character died?"""
    CompareChrEzStateValue(0, z37, z38, z39, 0)
    IsChrDead(0, z37)
    assert ConditionGroup(0)
    """State 3: Cancel lock disable effect"""
    ClearEnemySpEffect(z37, z40)
    """State 4: Finish"""
    return 0

def event_m10_18_x53(z37=_, z38=7, z39=1, z40=170000000):
    """[Lib] [DC] [Preset] Character _ Unlockable management
    z37: Generator ID
    z38: Share flag
    z39: Comparison value
    z40: Special effect ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Character _ Unlockable management _ Empty _SubState"""
    assert event_m10_18_x50()
    """State 3: [Lib] [DC] [Condition] Character_Unlockable_SubState"""
    call = event_m10_18_x51(z37=z37, z38=z38, z39=z39)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Lib] [DC] [Execution] Chara_Unlockable Management_SubState"""
        assert event_m10_18_x52(z37=z37, z38=z38, z39=z39, z40=z40)
    """State 4: Finish"""
    return 0

def event_m10_18_x54(flag4=118000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag4: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag4) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_18_x55(z35=844):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z35: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z35, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x56(z36=118020082):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z36: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z36, 1)
    """State 2: End state"""
    return 0

def event_m10_18_x57(flag4=118000081, z35=844, z36=118020082):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag4: Boss destruction flag
    z35: Boss generator ID
    z36: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_18_x54(flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_18_x55(z35=z35)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_18_x56(z36=z36)
    """State 4: End state"""
    return 0

def event_m10_18_x58(z34=10182100, flag3=118000081):
    """[Reproduction] Reproduction of water level rise
    z34: Instance ID of OBJ performing water level rising animation
    flag3: Boss destruction flag
    """
    """State 0,1: Water OBJ: Water level initialization"""
    InitializeObj(z34)
    SetGroundMaterial(3, 240, 0)
    """State 2: Has the boss been destroyed?"""
    if GetEventFlag(flag3) != 0:
        """State 4: Boss killed"""
        return 1
    else:
        """State 3: Not rising"""
        return 0

def event_m10_18_x59():
    """[Conditions] Water level rise judgment"""
    """State 0,1: Point intrusion standby"""
    IsPlayerInsidePoint(8, 600000, 600000, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_18_x60(z34=10182100):
    """[Execution] Water level rise & Grand material switching
    z34: Instance ID of OBJ performing water level rising animation
    """
    """State 0,1: Water level starts to rise"""
    ChangeObjState(z34, 70)
    """State 4: Waiting for water depth change time 1"""
    CompareStateTime(0, 55, 2, 55)
    assert ConditionGroup(0)
    """State 2: Switching ground material due to water level change 1"""
    SetGroundMaterial(3, 240, 1)
    """State 5: Waiting for water depth change time 2"""
    CompareStateTime(0, 70, 2, 70)
    assert ConditionGroup(0)
    """State 3: Switching ground material due to water level change 2"""
    SetGroundMaterial(3, 240, 2)
    """State 6: End state"""
    return 0

def event_m10_18_x61(z34=10182100, flag3=118000081):
    """[Preset] Boss Battle_Water Level Rise
    z34: Instance ID of OBJ performing water level rising animation
    flag3: Boss destruction flag
    """
    """State 0,3: [Reproduction] Water level rise state reproduction_SubState"""
    call = event_m10_18_x58(z34=z34, flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Water level rise judgment_SubState"""
        assert event_m10_18_x59()
        """State 1: [Execution] Water level rise & Grand material switching_SubState"""
        assert event_m10_18_x60(z34=z34)
    """State 4: End state"""
    return 0

def event_m10_18_x62(z30=_, z31=_, z32=10181014):
    """[Reproduction] When a wooden board is broken, it becomes brighter (after the insect key lights up)
    z30: Wood board instance ID
    z31: Event light ID
    z32: Igniter instance ID
    """
    """State 0,1: Is the insect key lit and the board destroyed?"""
    if CompareObjStateId(z30, 20, 0) and CompareObjStateId(z32, 20, 0):
        """State 4: End of reproduction"""
        return 1
    else:
        """State 2: Event light OFF"""
        SetPointLightEnabled(z31, 0, 0)
        """State 3: Go to the condition phase"""
        return 0

def event_m10_18_x63(z30=_, z32=10181014):
    """[Condition] When the wooden board is broken, it becomes brighter (after the insect key lights up)
    z30: Wood board instance ID
    z32: Igniter instance ID
    """
    """State 0,1: Was the insect key lighthouse turned on and the wooden board destroyed?"""
    IsObjBroken(8, z30, 1)
    CompareObjState(8, z32, 20, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_18_x64(z31=_, z33=_):
    """[Execution] When the wooden board is broken, it becomes brighter (after lighting the insect key)
    z31: Event light ID
    z33: Point ID for changing brightness area
    """
    """State 0,1: Event light ON"""
    SetPointLightEnabled(z31, 1, 1)
    """State 2: Change brightness area"""
    ChangeMapAreaBrightnessSetting(z33, 1)
    """State 3: End state"""
    return 0

def event_m10_18_x65(z30=_, z31=_, z32=10181014, z33=_):
    """[Preset] Brighten up after breaking the wooden board
    z30: Wood board instance ID
    z31: Event light ID
    z32: Igniter instance ID
    z33: Point ID for changing brightness area
    """
    """State 0,1: [Reproduction] Breaking a wooden board makes it brighter (after lighting the insect key) _SubState"""
    call = event_m10_18_x62(z30=z30, z31=z31, z32=z32)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] When the wooden board is broken, it becomes brighter (after lighting the insect key) _SubState"""
        assert event_m10_18_x63(z30=z30, z32=z32)
    """State 3: [Execution] When you break a wooden board, it becomes brighter (after the insect key lights) _SubState"""
    assert event_m10_18_x64(z31=z31, z33=z33)
    """State 4: End state"""
    return 0

def event_m10_18_x66(z17=10181301, z18=10181300, z19=900000):
    """[Reproduction] Iron fence that opens with a lever
    z17: Instance ID of iron fence OBJ
    z18: Lever OBJ instance ID
    z19: Point ID for Navimesh change
    """
    """State 0,1: State judgment of iron fence"""
    if CompareObjStateId(z17, 20, 0):
        """State 3: Disabling the key guide of the lever"""
        DisableObjKeyGuide(z18, 1)
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z19, 2)
        """State 5: Opened"""
        return 1
    else:
        """State 4: Not open"""
        return 0

def event_m10_18_x67(z18=10181300):
    """[Conditions] Iron fence opened with lever
    z18: Lever OBJ object instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z18, 74, 0)
    CompareObjState(0, z18, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x68(z18=10181300, z17=10181301, z19=900000):
    """[Execution] Iron fence opened with lever
    z18: Lever OBJ instance ID
    z17: Instance ID of iron fence OBJ
    z19: Point ID for Navimesh change
    """
    """State 0,3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z18, 1)
    """State 1: Iron fence animation opening with lever"""
    ChangeObjState(z17, 70)
    """State 4: Has the iron fence been opened?"""
    CompareObjState(0, z17, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z19, 2)
    """State 5: End state"""
    return 0

def event_m10_18_x69(z29=10181050):
    """[Preset] Illumination that lights when the lighthouse starts
    z29: Bug ID OBJ instance ID
    """
    """State 0,1: [Reproduction] Lighting_SubState that lights when the lighthouse starts"""
    call = event_m10_18_x70(z29=z29)
    if call.Get() == 0:
        """State 2: [Condition] Lighting_SubState that lights when the lighthouse starts"""
        assert event_m10_18_x71(z29=z29)
        """State 3: [Execution] Lighting_SubState that lights when the lighthouse starts"""
        assert event_m10_18_x72()
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_18_x70(z29=10181050):
    """[Reproduction] Illumination that lights when the lighthouse starts
    z29: Bug ID OBJ instance ID
    """
    """State 0,1: Is the insect key activated?"""
    if True:
        """State 4: Not started"""
        return 0
    elif CompareObjStateId(z29, 20, 0):
        """State 2: Reproduction of brightness area"""
        ChangeHitBrightnessSetting(2, 1)
        ChangeMapAreaBrightnessSetting(400005, 1)
        """State 3: [DC] Faros lighthouse lighting flag ON"""
        SetEventFlag(118000012, 1)
        """State 5: Activated"""
        return 1

def event_m10_18_x71(z29=10181050):
    """[Condition] Illumination that lights when the lighthouse is activated
    z29: Bug ID OBJ instance ID
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z29, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x72():
    """[Execution] Illumination that lights when the lighthouse starts"""
    """State 0,2: Time lapse state"""
    assert (GetStateTime() > 1) != 0
    """State 1: Lighthouse lighting and brightness area switching"""
    ChangeHitBrightnessSetting(40, 1)
    ChangeHitBrightnessSetting(2, 1)
    ChangeMapAreaBrightnessSetting(400005, 1)
    ChangeOwnObjState(20)
    """State 3: [DC] Faros lighthouse lighting flag ON"""
    SetEventFlag(118000012, 1)
    """State 4: End state"""
    return 0

def event_m10_18_x73(z26=10180402, z27=1100000, z28=118020020):
    """[Preset] Opening the door or approaching the enemy
    z26: Door instance ID
    z27: Point ID
    z28: Startup flag
    """
    """State 0,1: [Reproduction] Opening a door or approaching an enemy _SubState"""
    assert event_m10_18_x74()
    """State 2: [Conditions] Enemies are activated by opening the door or approaching_SubState"""
    call = event_m10_18_x75(z26=z26, z27=z27)
    if call.Get() == 0:
        pass
    elif call.Done():
        """State 3: [Execution] Opening the door or approaching the enemy by _SubState"""
        assert event_m10_18_x76(z28=z28)
    """State 4: End state"""
    return 0

def event_m10_18_x74():
    """[Reproduction] Opening the door or approaching the enemy _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x75(z26=10180402, z27=1100000):
    """[Condition] Enemy starts when door opens or approaches
    z26: Door instance ID
    z27: Point ID
    """
    """State 0,2: Black or red spirit?"""
    if ComparePlayerPhantom(7) != 0:
        pass
    elif ComparePlayerPhantom(8) != 0:
        pass
    elif ComparePlayerPhantom(10) != 0:
        pass
    elif ComparePlayerPhantom(9) != 0:
        pass
    else:
        Goto('L0')
    """State 5: Simple end"""
    return 0
    """State 3: Is the door broken or open?"""
    Label('L0')
    if DoorOpen(0) != 1:
        """State 4: Point intrusion standby"""
        IsPlayerInsidePoint(0, z27, z27, 1)
        assert ConditionGroup(0)
    else:
        """State 1: Open the door or wait for point intrusion"""
        IsPlayerInsidePoint(0, z27, z27, 1)
        CompareObjState(0, z26, 74, 0)
        CompareObjState(0, z26, 50, 0)
        assert ConditionGroup(0)
    """State 6: Flag stand"""
    return 1

def event_m10_18_x76(z28=118020020):
    """[Execution] Enemy starts when the door opens or approaches
    z28: Enemy activation flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z28, 1)
    """State 2: End state"""
    return 0

def event_m10_18_x77():
    """[Reproduction] Lever that rings the bell"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x78(z21=10181002, z20=10182001):
    """[Condition] Lever that rings the bell
    z21: Lever OBJ instance ID
    z20: Bell OBJ instance ID
    """
    """State 0,1: Lever operation standby or bell standby"""
    CompareObjState(0, z21, 74, 0)
    CompareObjState(0, z21, 84, 0)
    CompareObjState(1, z20, 70, 0)
    if ConditionGroup(1):
        """State 3: Bell rang"""
        return 1
    elif ConditionGroup(0):
        """State 2: Lever activation"""
        return 0

def event_m10_18_x79(z20=10182001, z21=10181002):
    """[Execution] Lever that rings the bell_Lever activation
    z20: Bell OBJ instance ID
    z21: Lever OBJ instance ID
    """
    """State 0,2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z21, 1)
    """State 1: The bell rings: 70"""
    ChangeObjState(z20, 70)
    """State 3: Waiting for the bell to finish"""
    CompareObjState(0, z20, 10, 0)
    assert ConditionGroup(0)
    """State 4: Enable key guide for lever"""
    DisableObjKeyGuide(z21, 0)
    """State 5: End state"""
    return 0

def event_m10_18_x80(z20=10182001, z21=10181002):
    """[Preset] Lever that rings the bell
    z20: Bell OBJ instance ID
    z21: Lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Lever that rings the bell_SubState"""
    assert event_m10_18_x77()
    """State 3: [Condition] Lever that rings the bell_SubState"""
    call = event_m10_18_x78(z21=z21, z20=z20)
    if call.Get() == 1:
        """State 4: [Execution] Lever that rings the bell_bell activation_SubState"""
        assert event_m10_18_x85(z20=z20, z21=z21)
    elif call.Get() == 0:
        """State 2: [Execution] Lever that rings the bell_Lever activation_SubState"""
        assert event_m10_18_x79(z20=z20, z21=z21)
    """State 5: End state"""
    return 0

def event_m10_18_x81(z22=10182000, flag2=118000010, z24=100000, z25=10182002):
    """[Reproduction] Ship movement by bell
    z22: Ship OBJ instance ID
    flag2: Ship arrival completion flag
    z24: Point ID for Navimesh change
    z25: Fence OBJ instance ID
    """
    """State 0,8: Attach fence OBJ to ship OBJ"""
    AttachObjToObj(z22, 150, z25)
    """State 1: Has the ship already arrived?"""
    if GetEventFlag(flag2) != 0:
        pass
    else:
        Goto('L0')
    """State 9: Is the ship in the initial state?"""
    if CompareObjStateId(z22, 10, 0):
        """State 10: [Relief] The fence opens: 70"""
        ChangeObjState(z25, 70)
        """State 11: Ship map parts display_2"""
        SetMapPartDisplay(1, 1)
        SetHitEnabled(4, 1)
        SetHitEnabled(3, 1)
        """State 12: Hide ship_2"""
        ChangeObjState(z22, 21)
        """State 13: SFX and Light ON_2"""
        SetPointLightEnabled(10180030, 1, 0)
        SetPointLightEnabled(10180040, 1, 0)
        PlaySfxAtPoint(1000)
        PlaySfxAtPoint(1010)
        """State 14: Navi Mesh Change_2"""
        DeleteNavimeshAttribute(z24, 2)
    else:
        """State 3: Ship map parts display"""
        SetMapPartDisplay(1, 1)
        SetHitEnabled(4, 1)
        SetHitEnabled(3, 1)
        """State 4: Hide ship"""
        ChangeObjState(z22, 21)
        """State 6: SFX and Light ON"""
        SetPointLightEnabled(10180030, 1, 0)
        SetPointLightEnabled(10180040, 1, 0)
        PlaySfxAtPoint(1000)
        PlaySfxAtPoint(1010)
        """State 7: Navigation mesh change"""
        DeleteNavimeshAttribute(z24, 2)
    """State 16: Operated"""
    return 1
    """State 5: SFX and light OFF"""
    Label('L0')
    SetPointLightEnabled(10180030, 0, 0)
    SetPointLightEnabled(10180040, 0, 0)
    StopSfxAtPoint(1000)
    StopSfxAtPoint(1010)
    """State 2: Remove ship map parts and hits"""
    SetMapPartDisplay(1, 0)
    SetHitEnabled(3, 0)
    SetHitEnabled(4, 0)
    """State 15: No operation"""
    return 0

def event_m10_18_x82(z23=10182001, z22=10182000):
    """[Condition] Ship movement by bell
    z23: Bell OBJ instance ID
    z22: Ship OBJ instance ID
    """
    """State 0,1: Bell ringing standby or ship condition judgment"""
    CompareObjState(0, z23, 70, 0)
    CompareObjState(0, z22, 10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x83(z22=10182000, flag2=118000010, z24=100000, z25=10182002):
    """[Execution] Ship movement by bell
    z22: Ship OBJ instance ID
    flag2: Ship arrival completion flag
    z24: Point ID for Navimesh change
    z25: Fence OBJ instance ID
    """
    """State 0,1: Ship moves: 70"""
    ChangeObjState(z22, 70)
    """State 2: Immediately after arrival: 23 waits"""
    CompareObjState(0, z22, 23, 0)
    assert ConditionGroup(0)
    """State 3: Ship map parts display"""
    SetMapPartDisplay(1, 1)
    SetHitEnabled(4, 1)
    SetHitEnabled(3, 1)
    """State 8: The fence opens: 70"""
    ChangeObjState(z25, 70)
    """State 9: Wait for the fence to open"""
    CompareObjState(0, z25, 20, 0)
    assert ConditionGroup(0)
    """State 10: Ship arrives: 20"""
    ChangeObjState(z22, 20)
    """State 11: Waiting for ship arrival"""
    CompareObjState(0, z22, 20, 0)
    assert ConditionGroup(0)
    """State 5: Hide ship"""
    ChangeObjState(z22, 21)
    """State 7: SFX and Light ON"""
    SetPointLightEnabled(10180030, 1, 0)
    SetPointLightEnabled(10180040, 1, 0)
    PlaySfxAtPoint(1000)
    PlaySfxAtPoint(1010)
    """State 6: Navigation mesh change"""
    DeleteNavimeshAttribute(z24, 2)
    """State 4: Ship arrival completion flag ON"""
    SetEventFlag(flag2, 1)
    """State 12: End state"""
    return 0

def event_m10_18_x84(z22=10182000, flag2=118000010, z23=10182001, z24=100000, z25=10182002):
    """[Preset] Ship movement by bell
    z22: Ship OBJ instance ID
    flag2: Ship arrival completion flag
    z23: Bell OBJ instance ID
    z24: Point ID for Navimesh change
    z25: Fence OBJ instance ID
    """
    """State 0,1: [Reproduction] Ship movement by bell_SubState"""
    call = event_m10_18_x81(z22=z22, flag2=flag2, z24=z24, z25=z25)
    if call.Get() == 0:
        """State 3: [Condition] Ship movement by bell_SubState"""
        assert event_m10_18_x82(z23=z23, z22=z22)
        """State 2: [Execution] Ship movement by bell_SubState"""
        assert event_m10_18_x83(z22=z22, flag2=flag2, z24=z24, z25=z25)
    elif call.Done():
        pass
    """State 4: End state"""
    return 0

def event_m10_18_x85(z20=10182001, z21=10181002):
    """[Execution] Lever that rings the bell
    z20: Bell OBJ instance ID
    z21: Lever OBJ instance ID
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z21, 1)
    """State 2: Waiting for the bell to finish"""
    CompareObjState(0, z20, 10, 0)
    assert ConditionGroup(0)
    """State 3: Enable key guide for lever"""
    DisableObjKeyGuide(z21, 0)
    """State 4: End state"""
    return 0

def event_m10_18_x86(z5=10182300):
    """[Reproduction] Ship leaves port with compass
    z5: Compass OBJ instance ID
    """
    """State 0,1: Compass state initialization"""
    InitializeObj(z5)
    """State 2: End state"""
    return 0

def event_m10_18_x87(z5=10182300):
    """[Conditions] Ships leave the compass
    z5: Compass OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z5, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z5)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_18_x88(z6=101820, z7=100010, z5=10182300):
    """[Execution] Ship leaves port on compass
    z6: Pre-warp poly play ID
    z7: Warp point ID
    z5: Compass OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z5, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_18_x0(z6=z6, z104=0, z105=10160000, z7=z7)
    """State 4: End state"""
    return 0

def event_m10_18_x89(z5=10182300, z6=101820, z7=100010):
    """[Preset] The ship leaves the compass
    z5: Compass OBJ instance ID
    z6: Poly play ID
    z7: Warp point ID
    """
    """State 0,1: [Reproduction] The ship leaves the compass _SubState"""
    assert event_m10_18_x86(z5=z5)
    """State 3: [Condition] Ship leaves port on compass_SubState"""
    call = event_m10_18_x87(z5=z5)
    if call.Get() == 1:
        """State 4: [Execution] Ship leaves port on compass_Key guide disabled_SubState"""
        assert event_m10_18_x103(z5=z5)
        """State 6: Rerun"""
        return 1
    elif call.Get() == 0:
        """State 2: [Execution] The ship leaves the compass _SubState"""
        assert event_m10_18_x88(z6=z6, z7=z7, z5=z5)
        """State 5: End state"""
        return 0

def event_m10_18_x90(z17=10181301, z18=10181300, z19=900000):
    """[Preset] Iron fence opened with lever
    z17: Instance ID of iron fence OBJ
    z18: Lever OBJ instance ID
    z19: Point ID for Navimesh change
    """
    """State 0,1,2: [Reproduction] Iron fence_SubState opened with lever"""
    call = event_m10_18_x66(z17=z17, z18=z18, z19=z19)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Iron fence opened with lever_SubState"""
        assert event_m10_18_x67(z18=z18)
        """State 4: [Execution] Iron fence open with lever_SubState"""
        assert event_m10_18_x68(z18=z18, z17=z17, z19=z19)
    """State 5: End state"""
    return 0

def event_m10_18_x91(z13=19000, z16=19010):
    """[Reproduction] Moonlight on the ship
    z13: Moonlight SFXID
    z16: Indoor SFXID
    """
    """State 0,1: Moonlight SFX stop"""
    StopSfxAtPoint(z13)
    """State 2: Indoor SFX stop"""
    StopSfxAtPoint(z16)
    """State 3: End state"""
    return 0

def event_m10_18_x92(z11=1900000, z12=1900003, z14=118000010, z15=10182000):
    """[Condition] Moonlight on the ship
    z11: Start point ID
    z12: End point ID
    z14: Ship arrival flag
    z15: OBJ instance ID of the ship
    """
    """State 0,3: Has the ship arrived?"""
    CompareEventFlag(8, z14, 1)
    CompareObjState(8, z15, 21, 0)
    SetConditionGroup(0, 8)
    CompareEventFlag(9, z14, 1)
    CompareObjState(9, z15, 22, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Disable ship OBJ synchronization"""
    SetObjSync(z15, 0)
    """State 1: Has the ship arrived and entered the switching point?"""
    IsPlayerInsidePoint(8, z11, z12, 1)
    CompareEventFlag(8, z14, 1)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_18_x93(z11=1900000, z12=1900003, z13=19000, z15=10182000, z16=19010):
    """[Execution] Moonlight on the ship
    z11: Start point ID
    z12: End point ID
    z13: Moonlight SFXID
    z15: OBJ instance ID of the ship
    z16: Indoor SFXID
    """
    """State 0,3: Ship SFX Stop: 22"""
    ChangeObjState(z15, 22)
    """State 2: Moonlight SFX playback"""
    PlaySfxAtPoint(z13)
    """State 5: Indoor SFX playback"""
    PlaySfxAtPoint(z16)
    """State 1: Waiting for next decision: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z11, z12, 0)
    assert ConditionGroup(0)
    """State 4: Ship SFX Stop: 21"""
    ChangeObjState(z15, 21)
    """State 6: End state"""
    return 0

def event_m10_18_x94(z11=1900000, z12=1900003, z13=19000, z14=118000010, z15=10182000, z16=19010):
    """[Preset] Moonlight on the ship
    z11: Start point ID
    z12: End point ID
    z13: Moonlight SFXID
    z14: Ship arrival completion flag
    z15: OBJ instance ID of the ship
    z16: Indoor SFXID
    """
    """State 0,1: [Reproduction] Moonlight _SubState for ships"""
    assert event_m10_18_x91(z13=z13, z16=z16)
    """State 3: [Condition] Moonlight _SubState for ships"""
    assert event_m10_18_x92(z11=z11, z12=z12, z14=z14, z15=z15)
    """State 2: [Execution] Moonlight for the ship_SubState"""
    assert event_m10_18_x93(z11=z11, z12=z12, z13=z13, z15=z15, z16=z16)
    """State 4: End state"""
    return 0

def event_m10_18_x95(z9=_, z10=_):
    """[Preset] Destroy the door when the wall is destroyed
    z9: Wall OBJ instance ID
    z10: Door OBJ instance ID
    """
    """State 0,1: [Reproduction] Destroy the door when the wall is destroyed_Sky_SubState"""
    assert event_m10_18_x96()
    """State 3: [Condition] The door is destroyed when the wall is destroyed."""
    assert event_m10_18_x98(z9=z9)
    """State 2: [Execution] When the wall is destroyed, the door is also destroyed._SubState"""
    assert event_m10_18_x97(z10=z10)
    """State 4: End state"""
    return 0

def event_m10_18_x96():
    """[Reproduction] Destroy the door when the wall is destroyed"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x97(z10=_):
    """[Execution] When the wall is destroyed, the door is also destroyed.
    z10: Door OBJ instance ID
    """
    """State 0,1: Door destruction"""
    DestroyObj(z10, z10, 0)
    """State 2: End state"""
    return 0

def event_m10_18_x98(z9=_):
    """[Condition] When the wall is destroyed, the door is also destroyed.
    z9: Wall OBJ instance ID
    """
    """State 0,1: Wall waiting for destruction"""
    IsObjBroken(0, z9, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x99(flag1=118000010, z8=10182000):
    """[Preset] Onboard OBJ drawing switching
    flag1: Ship arrival flag
    z8: Ship OBJ instance ID
    """
    """State 0,1: [Reproduction] Drawing switching of OBJ on board _SubState"""
    call = event_m10_18_x100(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Onboard OBJ drawing switching_SubState"""
        assert event_m10_18_x101(flag1=flag1, z8=z8)
    """State 3: [Execution] OBJ drawing switching on board _SubState"""
    assert event_m10_18_x102()
    """State 4: End state"""
    return 0

def event_m10_18_x100(flag1=118000010):
    """[Reproduction] Onboard OBJ drawing switching
    flag1: Ship arrival flag
    """
    """State 0,2: Has the ship already arrived?"""
    if GetEventFlag(flag1) != 0:
        """State 4: Arrived"""
        return 1
    else:
        """State 1: Hide OBJ on board"""
        ChangeObjState(10182200, 30)
        ChangeObjState(10182201, 30)
        ChangeObjState(10182202, 30)
        ChangeObjState(10182203, 30)
        ChangeObjState(10182204, 30)
        ChangeObjState(10182205, 30)
        ChangeObjState(10182206, 30)
        ChangeObjState(10182207, 30)
        ChangeObjState(10182208, 30)
        """State 3: Not arrived yet"""
        return 0

def event_m10_18_x101(flag1=118000010, z8=10182000):
    """[Conditions] Onboard OBJ drawing switching
    flag1: Ship arrival flag
    z8: Ship OBJ instance ID
    """
    """State 0,1: Has the ship arrived?"""
    CompareEventFlag(0, flag1, 1)
    CompareObjState(0, z8, 23, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x102():
    """[Execution] Onboard OBJ drawing switching"""
    """State 0,1: Display OBJ on board"""
    ChangeObjState(10182200, 10)
    ChangeObjState(10182201, 10)
    ChangeObjState(10182202, 10)
    ChangeObjState(10182203, 10)
    ChangeObjState(10182204, 10)
    ChangeObjState(10182205, 10)
    ChangeObjState(10182206, 10)
    ChangeObjState(10182207, 10)
    ChangeObjState(10182208, 10)
    """State 2: End state"""
    return 0

def event_m10_18_x103(z5=10182300):
    """[Execution] The ship leaves the compass with the key guide disabled
    z5: Compass OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z5, 1)
    """State 2: End state"""
    return 0

def event_m10_18_x104():
    """[DC] [Reproduction] Defeatable bridge"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x105(z2=10181080):
    """[DC] [Condition] Defeatable bridge
    z2: Bridge OBJ instance ID
    """
    """State 0,1: Waiting for the fall of the bridge"""
    CompareObjState(0, z2, 20, 0)
    CompareObjState(0, z2, 70, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x106(z1=6001000, z2=10181080, z3=10181090, val1=0.7, z4=118000014):
    """[DC] [execution] Defeatable bridge
    z1: Navigation change point ID
    z2: Bridge OBJ instance ID
    z3: Stopper OBJ instance ID
    val1: Weight until destruction
    z4: Opening flag
    """
    """State 0,2: Is the stopper broken?"""
    CompareObjState(0, z3, 10, 0)
    if ConditionGroup(0):
        """State 5: weight"""
        assert (GetStateTime() > val1) != 0
        """State 3: Destruction of stopper"""
        DestroyObj(z3, z3, 0)
    else:
        pass
    """State 4: Did the bridge fall over?"""
    CompareObjState(0, z2, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z1, 2)
    """State 6: Opening flag ON"""
    SetEventFlag(z4, 1)
    """State 7: End state"""
    return 0

def event_m10_18_x107(z1=6001000, z2=10181080, z3=10181090, val1=0.7, z4=118000014):
    """[DC] [Preset] Defeatable bridge
    z1: Navigation change point ID
    z2: Bridge OBJ instance ID
    z3: Stopper OBJ instance ID
    val1: Weight until destruction
    z4: Opening flag
    """
    """State 0,1: [DC] [Reproduction] Defeatable Bridge_SubState"""
    assert event_m10_18_x104()
    """State 3: [DC] [Condition] Defeatable Bridge_SubState"""
    assert event_m10_18_x105(z2=z2)
    """State 2: [DC] [Execution] Defeatable Bridge_SubState"""
    assert event_m10_18_x106(z1=z1, z2=z2, z3=z3, val1=val1, z4=z4)
    """State 4: End state"""
    return 0

def event_m10_18_111202():
    """OBJ: Dwarf (Hidden Port): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_18_x1(z100=104131, z101=10184200, z102=246, z103=7260)
    Quit()

def event_m10_18_111203():
    """OBJ: Dwarf (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7260:Lonesome Gavlan
    event_m10_18_x4(z95=118010140, z96=118020141, z97=104130, z98=10184200, z99=111202, npc1=7260)
    Quit()

def event_m10_18_111204():
    """OBJ: Dwarf (hidden port): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_18_x6(z85=245, z86=104131)
    Quit()

def event_m10_18_111272():
    """OBJ: Female Knight (Hidden Port): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_18_x1(z100=104191, z101=10184000, z102=91, z103=7520)
    Quit()

def event_m10_18_111273():
    """OBJ: Woman Knight (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_18_x4(z95=118010100, z96=118020101, z97=104190, z98=10184000, z99=111272, npc1=7520)
    Quit()

def event_m10_18_111274():
    """OBJ: Woman Knight (Hidden Harbor): Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_18_x6(z85=90, z86=104191)
    Quit()

def event_m10_18_111275():
    """OBJ: Woman Knight (Hidden Port): Appearance Judgment"""
    """State 0,1: [Lib] NPC: Woman Knight: Appearance Judgment_SubState"""
    event_m10_18_x5(z87=102480, z88=102481, z89=102483, z90=102487, z91=102492, z92=102485, z93=102486,
                    z94=102488)
    Quit()

def event_m10_18_111276():
    """OBJ: Woman Knight (Hidden Port): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_18_x26(z63=102502, z64=566, z65=104190, z66=60, z67=103690, z68=-1)
    Quit()

def event_m10_18_111277():
    """OBJ: Female Knight (Hidden Port): White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_18_x36(z54=118000081, z55=102498, z56=204, z57=7520)
    Quit()

def event_m10_18_111392():
    """OBJ: Magician (Hidden Port): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_18_x1(z100=104301, z101=10184100, z102=136, z103=7660)
    Quit()

def event_m10_18_111393():
    """OBJ: Magician (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7660:Carhillion of the Fold
    event_m10_18_x4(z95=118010120, z96=118020121, z97=104300, z98=10184100, z99=111392, npc1=7660)
    Quit()

def event_m10_18_111394():
    """OBJ: Magician (hidden port): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_18_x6(z85=135, z86=104301)
    Quit()

def event_m10_18_111395():
    """OBJ: Magician (Hidden Port): Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Magician_SubState"""
    event_m10_18_x25(z69=102721)
    Quit()

def event_m10_18_111800():
    """Small white spirit 1"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_18_x31(z60=567)
    Quit()

def event_m10_18_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_18_x45(flag5=118020109, z43=33)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_18_4001000():
    """[DC] Bridge that can be defeated"""
    """State 0,2: [DC] [Preset] Defeatable Bridge_SubState"""
    assert event_m10_18_x107(z1=6001000, z2=10181080, z3=10181090, val1=0.7, z4=118000014)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4002000():
    """[DC] Oil bottle _02"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z49=10181405, z50=10181455, z51=50, z52=242, z53=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z44=10181455, z45=50, z46=242, z47=0, z48=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4002010():
    """[DC] Oil bottle_03"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z49=10181410, z50=10181460, z51=50, z52=241, z53=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z44=10181460, z45=50, z46=241, z47=0, z48=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4002020():
    """[DC] Oil bottle_04"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z49=10181415, z50=10181465, z51=50, z52=240, z53=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z44=10181465, z45=50, z46=240, z47=0, z48=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4002030():
    """[DC] Oil bottle _05"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z49=10181420, z50=10181470, z51=50, z52=243, z53=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z44=10181470, z45=50, z46=243, z47=0, z48=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4003000():
    """[DC] Sailor_Unlockable Management_1"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_18_x53(z37=1510, z38=7, z39=1, z40=170000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4003010():
    """[DC] Sailor_Unlockable Management_2"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_18_x53(z37=5040, z38=7, z39=1, z40=170000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4003020():
    """[DC] Sailor_Unlockable Management_3"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_18_x53(z37=5041, z38=7, z39=1, z40=170000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_18_x49(z41=9000, z42=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_18_4031000():
    """[DC] NPC White Spirit_Gesture Management_Double Sided Warrior: Snake Head"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_18_x57(flag4=118000081, z35=844, z36=118020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

