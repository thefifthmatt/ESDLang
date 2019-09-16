# -*- coding: utf-8 -*-
def event_m10_18_1000():
    """Ship movement by bell"""
    """State 0,2: [Preset] Ship movement by bell_SubState"""
    assert event_m10_18_x84(z23=10182000, z24=118000010, z25=10182001, z26=100000, z27=10182002)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_1010():
    """Lever to ring the bell"""
    """State 0,2: [Preset] Lever that rings the bell_SubState"""
    assert event_m10_18_x80(z21=10182001, z22=10181002)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_18_1020():
    """Switching OBJ drawing on board"""
    """State 0,2: [Preset] Onboard OBJ drawing switching_SubState"""
    assert event_m10_18_x99(z8=118000010, z9=10182000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_2000():
    """[Insect key] For starting the lighthouse"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_18_x20(z80=10181050)
    """State 1: Finish"""
    EndMachine()

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

def event_m10_18_4000():
    """Lighting that works with bug keys"""
    """State 0,2: [Preset] Lighting_SubState that lights when the lighthouse starts"""
    assert event_m10_18_x69(z31=10181050)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_6000():
    """Boss battle water level rise"""
    """State 0,2: [Preset] Boss Battle_Water Level Rise_SubState"""
    assert event_m10_18_x61(z36=10182100, z37=118000081)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_7000():
    """Boss: Double Sided Warrior: Snake Head _ Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_18_x7(z85=118000081, z86=700000, z87=700000, z88=101, z89=1018000, z90=118020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_18_8000():
    """Breaking the wooden board brightens (after the insect key lights up)"""
    """State 0,2: [Preset] Breaking the wooden board brightens (after the insect key lights) _SubState"""
    assert event_m10_18_x65(z32=10181200, z33=10180010, z34=10181014, z35=800000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_8010():
    """When the wooden board is broken, it becomes brighter (after the insect key lights up) _2"""
    """State 0,2: [Preset] Breaking the wooden board brightens (after the insect key lights) _SubState"""
    assert event_m10_18_x65(z32=10181201, z33=10180000, z34=10181014, z35=801000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_8020():
    """Breaking the wooden board brightens (after the insect key lights up) _3"""
    """State 0,2: [Preset] Breaking the wooden board brightens (after the insect key lights) _SubState"""
    assert event_m10_18_x65(z32=10181202, z33=10180020, z34=10181014, z35=802000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_9000():
    """Iron fence that can be passed with a hanging leather lever"""
    """State 0,2: [Preset] Iron fence_SubState opened with lever"""
    assert event_m10_18_x90(z18=10181301, z19=10181300, z20=900000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_10000():
    """Connection flag ON"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_18_x30(z66=105415, z67=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_18_11000():
    """Open the door or approach the enemy by approaching"""
    """State 0,2: [Preset] Opening the door or approaching the enemy _SubState"""
    assert event_m10_18_x73(z28=10180402, z29=1100000, z30=118020020)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_12000():
    """Dark Hidden Wall Destruction 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z75=10181020, z76=20, z77=1200000, z78=0, z79=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_12010():
    """Dark Hidden Wall Destruction 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z75=10181021, z76=20, z77=1201000, z78=0, z79=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_12020():
    """Destroy the door when executing Wall Destruction 1"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_18_x95(z10=10181020, z11=10180400)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_12030():
    """Destroy the door when executing Wall Destroy 2"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_18_x95(z10=10181021, z11=10180401)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_13000():
    """Oil bottle_01"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z54=10181400, z55=10181450, z56=40, z57=240, z58=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z49=10181450, z50=40, z51=240, z52=0, z53=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_14000():
    """A ship leaves the compass"""
    """State 0,3: [Preset] The ship leaves the compass _SubState"""
    call = event_m10_18_x89(z5=10182300, z6=101820, z7=100010)
    if call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
    elif call.Get() == 0:
        """State 1: Finish"""
        EndMachine()

def event_m10_18_15000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z75=10181040, z76=20, z77=1500000, z78=0, z79=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_18000():
    """Navi mesh change of destructible wall"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z75=10181022, z76=20, z77=1800000, z78=0, z79=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_19000():
    """Moonlight on the ship"""
    """State 0,2: [Preset] Moonlight _SubState for ships"""
    assert event_m10_18_x94(z12=1900000, z13=1900003, z14=19000, z15=118000010, z16=10182000, z17=19010)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_18_20000():
    """Navimesh changes due to scaffold destruction"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_18_x21(z75=10181230, z76=20, z77=2000000, z78=2, z79=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_80000():
    """Rebirth Fire 01_ Entrance Limestone Cave"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_18_x35(z63=1018000, z64=1018099)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_x0(z6=101820, z110=0, z111=10160000, z7=100010):
    """[Lib] Warp between maps after poly play
    z6: Pre-warp poly play ID
    z110: Poly Play ID after Warp
    z111: Map ID
    z7: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z6, z110, z111, z7, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_18_x1(z106=_, z107=_, z108=_, z109=_):
    """[Lib] NPC: Grave Placement: General purpose
    z106: Death map: Global event flag
    z107: Tomb: OBJ instance ID
    z108: Tomb move to: Generator ID
    z109: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z106, 1)
    IsGraveGeneratable(8, z109, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z107, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z107, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_18_x2(z103=_, z104=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z103: Global: death flag
    z104: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z104, 10, 0)
    CompareObjState(1, z104, 20, 0)
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
    IsObjSearched(0, z104)
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

def event_m10_18_x3(z101=_, z102=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z101: Area other flags: Ghost appearance
    z102: Area other flags: Conversation start
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
    SetEventFlag(z101, 1)
    CompareEventFlag(0, z101, 1)
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
    SetEventFlag(z102, 1)
    CompareEventFlag(0, z102, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_18_x4(z101=_, z102=_, z103=_, z104=_, z105=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z101: Ghost Appearance: Area Other Flag
    z102: Conversation start: Area and other flags
    z103: Death: Global event flag
    z104: Tomb: OBJ instance ID
    z105: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z105, 1, 0)
    CompareEventFlag(9, z101, 1)
    CompareObjState(9, z104, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z102, 1)
        CompareEventFlag(0, z102, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_18_x2(z103=z103, z104=z104, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_18_x3(z101=z101, z102=z102, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_18_x5(z93=102480, z94=102481, z95=102483, z96=102487, z97=102492, z98=102485, z99=102486,
                    z100=102488):
    """[Lib] NPC: Woman Knight: Appearance Judgment
    z93: Sub 1 encountering: Global event flag
    z94: During sub-2 encounter: Global event flag
    z95: Sub 3 encountering: Global event flag
    z96: Generation stop: Global event flag
    z97: Appearance permission: Global event flag
    z98: Sub 1 generation stop: Global event flag
    z99: Sub 2 generation stop: Global event flag
    z100: Sub 3 generation stop: Global event flag
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
            CompareEventFlag(0, z96, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 2: Appearance determination: Judgment while encountering other maps"""
                CompareEventFlag(8, z93, 1)
                CompareEventFlag(8, z98, 0)
                CompareEventFlag(9, z94, 1)
                CompareEventFlag(9, z99, 0)
                CompareEventFlag(10, z95, 1)
                CompareEventFlag(10, z100, 0)
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
                        SetEventFlag(z97, 1)
                        CompareEventFlag(0, z97, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
        """State 3: Appearance judgment: Appearance impossible"""
        SetEventFlag(z97, 0)
        CompareEventFlag(0, z97, 0)
        assert ConditionGroup(0)
    """State 5: Appearance determination: System: Event end"""
    Label('L0')
    EndMachine()

def event_m10_18_x6(z91=_, z92=_):
    """[Lib] NPC: Death determination: General purpose
    z91: Generator ID
    z92: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z92, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z91)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z92, 1)
            CompareEventFlag(0, z92, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_18_x7(z85=118000081, z86=700000, z87=700000, z88=101, z89=1018000, z90=118020080, mode2=0):
    """[Lib] [Preset] Boss Battle Start
    z85: Boss destruction flag
    z86: Start point ID
    z87: End point ID
    z88: Sound ID
    z89: Boss Battle ID
    z90: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_18_x8(z85=z85)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_18_x9(z86=z86, z87=z87)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_18_x10(z88=z88, z89=z89, z90=z90)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_18_x11()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_18_x12(z89=z89)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_18_x13(z88=z88, z89=z89, z90=z90, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_18_x8(z85=118000081):
    """[Reproduction] Boss Battle_Start
    z85: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z85) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_18_x9(z86=700000, z87=700000):
    """[Condition] Boss Battle_Start
    z86: Start point ID
    z87: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z86, z87, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z86, z87, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x10(z88=101, z89=1018000, z90=118020080):
    """[Execution] Boss Battle_Start
    z88: Sound ID
    z89: Boss Battle ID
    z90: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z88)
    """State 1: Boss battle start notification"""
    StartBossFight(z89)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z90, 1)
    """State 4: End state"""
    return 0

def event_m10_18_x11():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x12(z89=1018000):
    """[Condition] Boss Battle_End Judgment
    z89: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z89, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x13(z88=101, z89=1018000, z90=118020080, mode2=0):
    """[Execute] Boss Battle_End
    z88: Sound ID
    z89: Boss Battle ID
    z90: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z90, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z89)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z88)
    """State 5: End state"""
    return 0

def event_m10_18_x14(z80=10181050):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z80: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z80, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z80, 10)
        assert CompareObjStateId(z80, 10, 0)
    elif CompareObjStateId(z80, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z80, 74, 1) and CompareObjStateId(z80, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_18_x15(z80=10181050, mode1=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z80: Object instance ID
    mode1: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z80)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode1) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_18_x16(z80=10181050, z82=38, z83=12, z84=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z80: Object instance ID
    z82: Key guide type
    z83: Event action
    z84: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z80, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z80, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z80, 30)
        assert CompareObjStateId(z80, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z80, z82, z83)
        assert PlayerIsInEventAction(z83) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z83, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z80, 74, 0)
        CompareObjState(1, z80, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z84)
            assert CompareObjStateId(z80, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z80, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_18_x17(z80=10181050, z81=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z80: Object instance ID
    z81: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z80, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_18_x18(z80=10181050):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z80: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z80, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x19():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x20(z80=10181050):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z80: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_18_x14(z80=z80)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_18_x18(z80=z80)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_18_x19()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_18_x15(z80=z80, mode1=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_18_x16(z80=z80, z82=38, z83=12, z84=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_18_x17(z80=z80, z81=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_18_x21(z75=_, z76=20, z77=_, z78=_, z79=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z75: Object instance ID
    z76: OBJ state ID
    z77: Navimesh switching point ID
    z78: Additional attributes
    z79: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_18_x22(z75=z75, z76=z76, z77=z77, z79=z79, z78=z78)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_18_x23(z75=z75, z76=z76, z77=z77)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_18_x24(z75=z75, z76=z76, z77=z77, z78=z78, z79=z79)
    """State 4: End state"""
    return 0

def event_m10_18_x22(z75=_, z76=20, z77=_, z79=_, z78=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z75: Target OBJ instance ID
    z76: Target OBJ state ID
    z77: Navimesh switching point ID
    z79: Additional attributes
    z78: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z75, z76, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z77, z79)
        DeleteNavimeshAttribute(z77, z78)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_18_x23(z75=_, z76=20, z77=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z75: Target OBJ instance ID
    z76: Target OBJ state ID
    z77: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z75, z76, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x24(z75=_, z76=20, z77=_, z78=_, z79=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z75: Target OBJ instance ID
    z76: Target OBJ state ID
    z77: Navimesh switching point ID
    z78: Additional attributes
    z79: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z77, z78)
    DeleteNavimeshAttribute(z77, z79)
    """State 2: End state"""
    return 0

def event_m10_18_x25(z74=102721):
    """[Lib] Appearance determination: Magician
    z74: Appearance permission: Global event flag
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
        SetEventFlag(z74, 1)
        CompareEventFlag(0, z74, 1)
        assert ConditionGroup(0)
    """State 5: Generation stop judgment: System: End"""
    Label('L0')
    EndMachine()

def event_m10_18_x26(z68=102502, z69=566, z70=104190, z71=60, z72=103690, z73=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z68: White Phantom can appear: Global event flag
    z69: White Phantom: Generator ID
    z70: Death: Global event flag
    z71: Body: Generator group ID
    z72: Hostile: Global event flag
    z73: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z69)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z70, 1)
        CompareEventFlag(1, z72, 1)
        CompareEventFlag(2, z68, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z69)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z70, 1)
            CompareEventFlag(1, z72, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z69)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z70, 1)
            CompareEventFlag(1, z72, 1)
            HasNpcPhantomSpawned(2, z69, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z71, 0)
                HasNpcPhantomSpawned(0, z69, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z69)
    """State 4: Appearance: System: End"""
    EndMachine()

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

def event_m10_18_x29(z66=105415, z67=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z66: Global event flag for connection
    z67: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z66, z67)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z66, z67)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_18_x30(z66=105415, z67=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z66: Global event flag for connection
    z67: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_18_x27()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_18_x28()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_18_x29(z66=z66, z67=z67)
    """State 4: End state"""
    return 0

def event_m10_18_x31(z65=567):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z65: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z65)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_18_x32():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x33(z63=1018000, z64=1018099):
    """[Lib] [execute] Rebirth fire
    z63: Flag start ID
    z64: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z63, z64, 0)
    """State 2: End state"""
    return 0

def event_m10_18_x34():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x35(z63=1018000, z64=1018099):
    """[Lib] [Preset] Rebirth
    z63: Flag start ID
    z64: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_18_x32()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_18_x34()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_18_x33(z63=z63, z64=z64)
    """State 4: End state"""
    return 0

def event_m10_18_x36(z59=118000081, z60=102498, z61=204, z62=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z59: Defeat Boss 1: Area and other flags
    z60: Summon Achievement: Global Event Flag
    z61: Summon achievement count: global variable
    z62: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z60, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z59, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z61, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z61, NpcInfoValue(z62, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z60, 1)
                CompareEventFlag(0, z60, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m10_18_x37():
    """[Lib] [Reproduction] Oil 壺 Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x38(z54=_):
    """[Lib] [Conditions]
    z54: Oil bottle OBJ instance ID
    """
    """State 0,1: Was the oil bottle broken?"""
    IsObjBroken(0, z54, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x39(z55=_, z56=_, z57=_, z58=1):
    """[Lib] [execution]
    z55: Tar OBJ instance ID for firewood
    z56: Hit group ID
    z57: Replacement GMID
    z58: Change destination GM slot
    """
    """State 0,1: Oil tar display: 30"""
    ChangeObjState(z55, 30)
    """State 2: Change of material"""
    SetGroundMaterial(z56, z57, z58)
    """State 3: End state"""
    return 0

def event_m10_18_x40(z54=_, z55=_, z56=_, z57=_, z58=1):
    """[Lib] [Preset] Oil bottle
    z54: Oil bottle OBJ instance ID
    z55: Tar OBJ instance ID for firewood
    z56: Hit group ID
    z57: Replacement GMID
    z58: Change destination GM slot
    """
    """State 0,1: [Lib] [Reproduction] Oil bottle_Sky_SubState"""
    assert event_m10_18_x37()
    """State 3: [Lib] [Conditions] Oil 壺 _SubState"""
    assert event_m10_18_x38(z54=z54)
    """State 2: [Lib] [Execution] Oil bottle_SubState"""
    assert event_m10_18_x39(z55=z55, z56=z56, z57=z57, z58=z58)
    """State 4: End state"""
    return 0

def event_m10_18_x41(z50=_, z51=_, z53=1):
    """[Lib] [Reproduction] Tar material change
    z50: Hit group ID
    z51: Replacement GMID
    z53: Change destination GM slot
    """
    """State 0,1: Material change_initialization"""
    SetGroundMaterial(z50, z51, z53)
    """State 2: End state"""
    return 0

def event_m10_18_x42(z49=_):
    """[Lib] [Condition] Tar material change
    z49: OBJ instance ID of tar
    """
    """State 0,1: Did tar burn out?"""
    CompareObjState(0, z49, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x43(z49=_, z50=_, z51=_, z52=0):
    """[Lib] [execution] Tar material change
    z49: OBJ instance ID of tar
    z50: Hit group ID
    z51: Replacement GMID
    z52: Change destination GM slot
    """
    """State 0,1: Change of material"""
    SetGroundMaterial(z50, z51, z52)
    """State 2: End state"""
    return 0

def event_m10_18_x44(z49=_, z50=_, z51=_, z52=0, z53=1):
    """[Lib] [Preset] Tar material change
    z49: OBJ instance ID of tar
    z50: Hit group ID
    z51: Replace_GMID
    z52: After change_GM slot
    z53: Before change_GM slot
    """
    """State 0,1: [Reproduction] Tar material change_SubState"""
    assert event_m10_18_x41(z50=z50, z51=z51, z53=z53)
    """State 3: [Condition] Tar material change_SubState"""
    assert event_m10_18_x42(z49=z49)
    """State 2: [Execution] Tar material change_SubState"""
    assert event_m10_18_x43(z49=z49, z50=z50, z51=z51, z52=z52)
    """State 4: End state"""
    return 0

def event_m10_18_x45(z47=118020109, z48=33):
    """[Lib] [Preset] Get trophy
    z47: Acquisition trigger_other flags
    z48: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z47) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z47, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z48)
    """State 4: End state"""
    return 0

def event_m10_18_x46(z45=9000, z46=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z45: Generator ID
    z46: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z45, z46)
    """State 2: End state"""
    return 0

def event_m10_18_x47(z45=9000, z46=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z45: Generator ID
    z46: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z45, z46, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_18_x48(z45=9000):
    """[Lib] [DC] [Condition] Transparent characters
    z45: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z45)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x49(z45=9000, z46=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z45: Generator ID
    z46: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_18_x47(z45=z45, z46=z46)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_18_x48(z45=z45)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_18_x46(z45=z45, z46=z46)
    """State 4: End state"""
    return 0

def event_m10_18_x50():
    """[Lib] [DC] [Reproduction] Character _ Unlockable management _ Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x51(z41=_, z42=7, z43=1):
    """[Lib] [DC] [Condition] Character _ Unlockable management
    z41: Generator ID
    z42: Share flag
    z43: Comparison value
    """
    """State 0,1: State judgment"""
    CompareChrEzStateValue(0, z41, z42, z43, 1)
    CompareChrEzStateValue(1, z41, z42, z43, 0)
    if ConditionGroup(1):
        """State 3: Can lock"""
        return 1
    elif ConditionGroup(0):
        """State 2: Can't lock"""
        return 0

def event_m10_18_x52(z41=_, z42=7, z43=1, z44=170000000):
    """[Lib] [DC] [Execution] Character _ Unlockable management
    z41: Generator ID
    z42: Share flag
    z43: Comparison value
    z44: Special effect ID
    """
    """State 0,1: Grants a non-locking effect"""
    SetEnemySpEffect(z41, z44, 19, 4)
    """State 2: State judgment or character died?"""
    CompareChrEzStateValue(0, z41, z42, z43, 0)
    IsChrDead(0, z41)
    assert ConditionGroup(0)
    """State 3: Cancel lock disable effect"""
    ClearEnemySpEffect(z41, z44)
    """State 4: Finish"""
    return 0

def event_m10_18_x53(z41=_, z42=7, z43=1, z44=170000000):
    """[Lib] [DC] [Preset] Character _ Unlockable management
    z41: Generator ID
    z42: Share flag
    z43: Comparison value
    z44: Special effect ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Character _ Unlockable management _ Empty _SubState"""
    assert event_m10_18_x50()
    """State 3: [Lib] [DC] [Condition] Character_Unlockable_SubState"""
    call = event_m10_18_x51(z41=z41, z42=z42, z43=z43)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Lib] [DC] [Execution] Chara_Unlockable Management_SubState"""
        assert event_m10_18_x52(z41=z41, z42=z42, z43=z43, z44=z44)
    """State 4: Finish"""
    return 0

def event_m10_18_x54(z38=118000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z38: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z38) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_18_x55(z39=844):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z39: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z39, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x56(z40=118020082):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z40: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z40, 1)
    """State 2: End state"""
    return 0

def event_m10_18_x57(z38=118000081, z39=844, z40=118020082):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z38: Boss destruction flag
    z39: Boss generator ID
    z40: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_18_x54(z38=z38)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_18_x55(z39=z39)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_18_x56(z40=z40)
    """State 4: End state"""
    return 0

def event_m10_18_x58(z36=10182100, z37=118000081):
    """[Reproduction] Reproduction of water level rise
    z36: Instance ID of OBJ performing water level rising animation
    z37: Boss destruction flag
    """
    """State 0,1: Water OBJ: Water level initialization"""
    InitializeObj(z36)
    SetGroundMaterial(3, 240, 0)
    """State 2: Has the boss been destroyed?"""
    if GetEventFlag(z37) != 0:
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

def event_m10_18_x60(z36=10182100):
    """[Execution] Water level rise & Grand material switching
    z36: Instance ID of OBJ performing water level rising animation
    """
    """State 0,1: Water level starts to rise"""
    ChangeObjState(z36, 70)
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

def event_m10_18_x61(z36=10182100, z37=118000081):
    """[Preset] Boss Battle_Water Level Rise
    z36: Instance ID of OBJ performing water level rising animation
    z37: Boss destruction flag
    """
    """State 0,3: [Reproduction] Water level rise state reproduction_SubState"""
    call = event_m10_18_x58(z36=z36, z37=z37)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Water level rise judgment_SubState"""
        assert event_m10_18_x59()
        """State 1: [Execution] Water level rise & Grand material switching_SubState"""
        assert event_m10_18_x60(z36=z36)
    """State 4: End state"""
    return 0

def event_m10_18_x62(z32=_, z33=_, z34=10181014):
    """[Reproduction] When a wooden board is broken, it becomes brighter (after the insect key lights up)
    z32: Wood board instance ID
    z33: Event light ID
    z34: Igniter instance ID
    """
    """State 0,1: Is the insect key lit and the board destroyed?"""
    if CompareObjStateId(z32, 20, 0) and CompareObjStateId(z34, 20, 0):
        """State 4: End of reproduction"""
        return 1
    else:
        """State 2: Event light OFF"""
        SetPointLightEnabled(z33, 0, 0)
        """State 3: Go to the condition phase"""
        return 0

def event_m10_18_x63(z32=_, z34=10181014):
    """[Condition] When the wooden board is broken, it becomes brighter (after the insect key lights up)
    z32: Wood board instance ID
    z34: Igniter instance ID
    """
    """State 0,1: Was the insect key lighthouse turned on and the wooden board destroyed?"""
    IsObjBroken(8, z32, 1)
    CompareObjState(8, z34, 20, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_18_x64(z33=_, z35=_):
    """[Execution] When the wooden board is broken, it becomes brighter (after lighting the insect key)
    z33: Event light ID
    z35: Point ID for changing brightness area
    """
    """State 0,1: Event light ON"""
    SetPointLightEnabled(z33, 1, 1)
    """State 2: Change brightness area"""
    ChangeMapAreaBrightnessSetting(z35, 1)
    """State 3: End state"""
    return 0

def event_m10_18_x65(z32=_, z33=_, z34=10181014, z35=_):
    """[Preset] Brighten up after breaking the wooden board
    z32: Wood board instance ID
    z33: Event light ID
    z34: Igniter instance ID
    z35: Point ID for changing brightness area
    """
    """State 0,1: [Reproduction] Breaking a wooden board makes it brighter (after lighting the insect key) _SubState"""
    call = event_m10_18_x62(z32=z32, z33=z33, z34=z34)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] When the wooden board is broken, it becomes brighter (after lighting the insect key) _SubState"""
        assert event_m10_18_x63(z32=z32, z34=z34)
    """State 3: [Execution] When you break a wooden board, it becomes brighter (after the insect key lights) _SubState"""
    assert event_m10_18_x64(z33=z33, z35=z35)
    """State 4: End state"""
    return 0

def event_m10_18_x66(z18=10181301, z19=10181300, z20=900000):
    """[Reproduction] Iron fence that opens with a lever
    z18: Instance ID of iron fence OBJ
    z19: Lever OBJ instance ID
    z20: Point ID for Navimesh change
    """
    """State 0,1: State judgment of iron fence"""
    if CompareObjStateId(z18, 20, 0):
        """State 3: Disabling the key guide of the lever"""
        DisableObjKeyGuide(z19, 1)
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z20, 2)
        """State 5: Opened"""
        return 1
    else:
        """State 4: Not open"""
        return 0

def event_m10_18_x67(z19=10181300):
    """[Conditions] Iron fence opened with lever
    z19: Lever OBJ object instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z19, 74, 0)
    CompareObjState(0, z19, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x68(z19=10181300, z18=10181301, z20=900000):
    """[Execution] Iron fence opened with lever
    z19: Lever OBJ instance ID
    z18: Instance ID of iron fence OBJ
    z20: Point ID for Navimesh change
    """
    """State 0,3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z19, 1)
    """State 1: Iron fence animation opening with lever"""
    ChangeObjState(z18, 70)
    """State 4: Has the iron fence been opened?"""
    CompareObjState(0, z18, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z20, 2)
    """State 5: End state"""
    return 0

def event_m10_18_x69(z31=10181050):
    """[Preset] Illumination that lights when the lighthouse starts
    z31: Bug ID OBJ instance ID
    """
    """State 0,1: [Reproduction] Lighting_SubState that lights when the lighthouse starts"""
    call = event_m10_18_x70(z31=z31)
    if call.Get() == 0:
        """State 2: [Condition] Lighting_SubState that lights when the lighthouse starts"""
        assert event_m10_18_x71(z31=z31)
        """State 3: [Execution] Lighting_SubState that lights when the lighthouse starts"""
        assert event_m10_18_x72()
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_18_x70(z31=10181050):
    """[Reproduction] Illumination that lights when the lighthouse starts
    z31: Bug ID OBJ instance ID
    """
    """State 0,1: Is the insect key activated?"""
    if True:
        """State 4: Not started"""
        return 0
    elif CompareObjStateId(z31, 20, 0):
        """State 2: Reproduction of brightness area"""
        ChangeHitBrightnessSetting(2, 1)
        ChangeMapAreaBrightnessSetting(400005, 1)
        """State 3: [DC] Faros lighthouse lighting flag ON"""
        SetEventFlag(118000012, 1)
        """State 5: Activated"""
        return 1

def event_m10_18_x71(z31=10181050):
    """[Condition] Illumination that lights when the lighthouse is activated
    z31: Bug ID OBJ instance ID
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z31, 20, 0)
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

def event_m10_18_x73(z28=10180402, z29=1100000, z30=118020020):
    """[Preset] Opening the door or approaching the enemy
    z28: Door instance ID
    z29: Point ID
    z30: Startup flag
    """
    """State 0,1: [Reproduction] Opening a door or approaching an enemy _SubState"""
    assert event_m10_18_x74()
    """State 2: [Conditions] Enemies are activated by opening the door or approaching_SubState"""
    call = event_m10_18_x75(z28=z28, z29=z29)
    if call.Get() == 0:
        pass
    elif call.Done():
        """State 3: [Execution] Opening the door or approaching the enemy by _SubState"""
        assert event_m10_18_x76(z30=z30)
    """State 4: End state"""
    return 0

def event_m10_18_x74():
    """[Reproduction] Opening the door or approaching the enemy _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x75(z28=10180402, z29=1100000):
    """[Condition] Enemy starts when door opens or approaches
    z28: Door instance ID
    z29: Point ID
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
        IsPlayerInsidePoint(0, z29, z29, 1)
        assert ConditionGroup(0)
    else:
        """State 1: Open the door or wait for point intrusion"""
        IsPlayerInsidePoint(0, z29, z29, 1)
        CompareObjState(0, z28, 74, 0)
        CompareObjState(0, z28, 50, 0)
        assert ConditionGroup(0)
    """State 6: Flag stand"""
    return 1

def event_m10_18_x76(z30=118020020):
    """[Execution] Enemy starts when the door opens or approaches
    z30: Enemy activation flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z30, 1)
    """State 2: End state"""
    return 0

def event_m10_18_x77():
    """[Reproduction] Lever that rings the bell"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x78(z22=10181002, z21=10182001):
    """[Condition] Lever that rings the bell
    z22: Lever OBJ instance ID
    z21: Bell OBJ instance ID
    """
    """State 0,1: Lever operation standby or bell standby"""
    CompareObjState(0, z22, 74, 0)
    CompareObjState(0, z22, 84, 0)
    CompareObjState(1, z21, 70, 0)
    if ConditionGroup(1):
        """State 3: Bell rang"""
        return 1
    elif ConditionGroup(0):
        """State 2: Lever activation"""
        return 0

def event_m10_18_x79(z21=10182001, z22=10181002):
    """[Execution] Lever that rings the bell_Lever activation
    z21: Bell OBJ instance ID
    z22: Lever OBJ instance ID
    """
    """State 0,2: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z22, 1)
    """State 1: The bell rings: 70"""
    ChangeObjState(z21, 70)
    """State 3: Waiting for the bell to finish"""
    CompareObjState(0, z21, 10, 0)
    assert ConditionGroup(0)
    """State 4: Enable key guide for lever"""
    DisableObjKeyGuide(z22, 0)
    """State 5: End state"""
    return 0

def event_m10_18_x80(z21=10182001, z22=10181002):
    """[Preset] Lever that rings the bell
    z21: Bell OBJ instance ID
    z22: Lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Lever that rings the bell_SubState"""
    assert event_m10_18_x77()
    """State 3: [Condition] Lever that rings the bell_SubState"""
    call = event_m10_18_x78(z22=z22, z21=z21)
    if call.Get() == 1:
        """State 4: [Execution] Lever that rings the bell_bell activation_SubState"""
        assert event_m10_18_x85(z21=z21, z22=z22)
    elif call.Get() == 0:
        """State 2: [Execution] Lever that rings the bell_Lever activation_SubState"""
        assert event_m10_18_x79(z21=z21, z22=z22)
    """State 5: End state"""
    return 0

def event_m10_18_x81(z23=10182000, z24=118000010, z26=100000, z27=10182002):
    """[Reproduction] Ship movement by bell
    z23: Ship OBJ instance ID
    z24: Ship arrival completion flag
    z26: Point ID for Navimesh change
    z27: Fence OBJ instance ID
    """
    """State 0,8: Attach fence OBJ to ship OBJ"""
    AttachObjToObj(z23, 150, z27)
    """State 1: Has the ship already arrived?"""
    if GetEventFlag(z24) != 0:
        pass
    else:
        Goto('L0')
    """State 9: Is the ship in the initial state?"""
    if CompareObjStateId(z23, 10, 0):
        """State 10: [Relief] The fence opens: 70"""
        ChangeObjState(z27, 70)
        """State 11: Ship map parts display_2"""
        SetMapPartDisplay(1, 1)
        SetHitEnabled(4, 1)
        SetHitEnabled(3, 1)
        """State 12: Hide ship_2"""
        ChangeObjState(z23, 21)
        """State 13: SFX and Light ON_2"""
        SetPointLightEnabled(10180030, 1, 0)
        SetPointLightEnabled(10180040, 1, 0)
        PlaySfxAtPoint(1000)
        PlaySfxAtPoint(1010)
        """State 14: Navi Mesh Change_2"""
        DeleteNavimeshAttribute(z26, 2)
    else:
        """State 3: Ship map parts display"""
        SetMapPartDisplay(1, 1)
        SetHitEnabled(4, 1)
        SetHitEnabled(3, 1)
        """State 4: Hide ship"""
        ChangeObjState(z23, 21)
        """State 6: SFX and Light ON"""
        SetPointLightEnabled(10180030, 1, 0)
        SetPointLightEnabled(10180040, 1, 0)
        PlaySfxAtPoint(1000)
        PlaySfxAtPoint(1010)
        """State 7: Navigation mesh change"""
        DeleteNavimeshAttribute(z26, 2)
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

def event_m10_18_x82(z25=10182001, z23=10182000):
    """[Condition] Ship movement by bell
    z25: Bell OBJ instance ID
    z23: Ship OBJ instance ID
    """
    """State 0,1: Bell ringing standby or ship condition judgment"""
    CompareObjState(0, z25, 70, 0)
    CompareObjState(0, z23, 10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x83(z23=10182000, z24=118000010, z26=100000, z27=10182002):
    """[Execution] Ship movement by bell
    z23: Ship OBJ instance ID
    z24: Ship arrival completion flag
    z26: Point ID for Navimesh change
    z27: Fence OBJ instance ID
    """
    """State 0,1: Ship moves: 70"""
    ChangeObjState(z23, 70)
    """State 2: Immediately after arrival: 23 waits"""
    CompareObjState(0, z23, 23, 0)
    assert ConditionGroup(0)
    """State 3: Ship map parts display"""
    SetMapPartDisplay(1, 1)
    SetHitEnabled(4, 1)
    SetHitEnabled(3, 1)
    """State 8: The fence opens: 70"""
    ChangeObjState(z27, 70)
    """State 9: Wait for the fence to open"""
    CompareObjState(0, z27, 20, 0)
    assert ConditionGroup(0)
    """State 10: Ship arrives: 20"""
    ChangeObjState(z23, 20)
    """State 11: Waiting for ship arrival"""
    CompareObjState(0, z23, 20, 0)
    assert ConditionGroup(0)
    """State 5: Hide ship"""
    ChangeObjState(z23, 21)
    """State 7: SFX and Light ON"""
    SetPointLightEnabled(10180030, 1, 0)
    SetPointLightEnabled(10180040, 1, 0)
    PlaySfxAtPoint(1000)
    PlaySfxAtPoint(1010)
    """State 6: Navigation mesh change"""
    DeleteNavimeshAttribute(z26, 2)
    """State 4: Ship arrival completion flag ON"""
    SetEventFlag(z24, 1)
    """State 12: End state"""
    return 0

def event_m10_18_x84(z23=10182000, z24=118000010, z25=10182001, z26=100000, z27=10182002):
    """[Preset] Ship movement by bell
    z23: Ship OBJ instance ID
    z24: Ship arrival completion flag
    z25: Bell OBJ instance ID
    z26: Point ID for Navimesh change
    z27: Fence OBJ instance ID
    """
    """State 0,1: [Reproduction] Ship movement by bell_SubState"""
    call = event_m10_18_x81(z23=z23, z24=z24, z26=z26, z27=z27)
    if call.Get() == 0:
        """State 3: [Condition] Ship movement by bell_SubState"""
        assert event_m10_18_x82(z25=z25, z23=z23)
        """State 2: [Execution] Ship movement by bell_SubState"""
        assert event_m10_18_x83(z23=z23, z24=z24, z26=z26, z27=z27)
    elif call.Done():
        pass
    """State 4: End state"""
    return 0

def event_m10_18_x85(z21=10182001, z22=10181002):
    """[Execution] Lever that rings the bell
    z21: Bell OBJ instance ID
    z22: Lever OBJ instance ID
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z22, 1)
    """State 2: Waiting for the bell to finish"""
    CompareObjState(0, z21, 10, 0)
    assert ConditionGroup(0)
    """State 3: Enable key guide for lever"""
    DisableObjKeyGuide(z22, 0)
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
    assert event_m10_18_x0(z6=z6, z110=0, z111=10160000, z7=z7)
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

def event_m10_18_x90(z18=10181301, z19=10181300, z20=900000):
    """[Preset] Iron fence opened with lever
    z18: Instance ID of iron fence OBJ
    z19: Lever OBJ instance ID
    z20: Point ID for Navimesh change
    """
    """State 0,1,2: [Reproduction] Iron fence_SubState opened with lever"""
    call = event_m10_18_x66(z18=z18, z19=z19, z20=z20)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Iron fence opened with lever_SubState"""
        assert event_m10_18_x67(z19=z19)
        """State 4: [Execution] Iron fence open with lever_SubState"""
        assert event_m10_18_x68(z19=z19, z18=z18, z20=z20)
    """State 5: End state"""
    return 0

def event_m10_18_x91(z14=19000, z17=19010):
    """[Reproduction] Moonlight on the ship
    z14: Moonlight SFXID
    z17: Indoor SFXID
    """
    """State 0,1: Moonlight SFX stop"""
    StopSfxAtPoint(z14)
    """State 2: Indoor SFX stop"""
    StopSfxAtPoint(z17)
    """State 3: End state"""
    return 0

def event_m10_18_x92(z12=1900000, z13=1900003, z15=118000010, z16=10182000):
    """[Condition] Moonlight on the ship
    z12: Start point ID
    z13: End point ID
    z15: Ship arrival flag
    z16: OBJ instance ID of the ship
    """
    """State 0,3: Has the ship arrived?"""
    CompareEventFlag(8, z15, 1)
    CompareObjState(8, z16, 21, 0)
    SetConditionGroup(0, 8)
    CompareEventFlag(9, z15, 1)
    CompareObjState(9, z16, 22, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Disable ship OBJ synchronization"""
    SetObjSync(z16, 0)
    """State 1: Has the ship arrived and entered the switching point?"""
    IsPlayerInsidePoint(8, z12, z13, 1)
    CompareEventFlag(8, z15, 1)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_18_x93(z12=1900000, z13=1900003, z14=19000, z16=10182000, z17=19010):
    """[Execution] Moonlight on the ship
    z12: Start point ID
    z13: End point ID
    z14: Moonlight SFXID
    z16: OBJ instance ID of the ship
    z17: Indoor SFXID
    """
    """State 0,3: Ship SFX Stop: 22"""
    ChangeObjState(z16, 22)
    """State 2: Moonlight SFX playback"""
    PlaySfxAtPoint(z14)
    """State 5: Indoor SFX playback"""
    PlaySfxAtPoint(z17)
    """State 1: Waiting for next decision: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z12, z13, 0)
    assert ConditionGroup(0)
    """State 4: Ship SFX Stop: 21"""
    ChangeObjState(z16, 21)
    """State 6: End state"""
    return 0

def event_m10_18_x94(z12=1900000, z13=1900003, z14=19000, z15=118000010, z16=10182000, z17=19010):
    """[Preset] Moonlight on the ship
    z12: Start point ID
    z13: End point ID
    z14: Moonlight SFXID
    z15: Ship arrival completion flag
    z16: OBJ instance ID of the ship
    z17: Indoor SFXID
    """
    """State 0,1: [Reproduction] Moonlight _SubState for ships"""
    assert event_m10_18_x91(z14=z14, z17=z17)
    """State 3: [Condition] Moonlight _SubState for ships"""
    assert event_m10_18_x92(z12=z12, z13=z13, z15=z15, z16=z16)
    """State 2: [Execution] Moonlight for the ship_SubState"""
    assert event_m10_18_x93(z12=z12, z13=z13, z14=z14, z16=z16, z17=z17)
    """State 4: End state"""
    return 0

def event_m10_18_x95(z10=_, z11=_):
    """[Preset] Destroy the door when the wall is destroyed
    z10: Wall OBJ instance ID
    z11: Door OBJ instance ID
    """
    """State 0,1: [Reproduction] Destroy the door when the wall is destroyed_Sky_SubState"""
    assert event_m10_18_x96()
    """State 3: [Condition] The door is destroyed when the wall is destroyed."""
    assert event_m10_18_x98(z10=z10)
    """State 2: [Execution] When the wall is destroyed, the door is also destroyed._SubState"""
    assert event_m10_18_x97(z11=z11)
    """State 4: End state"""
    return 0

def event_m10_18_x96():
    """[Reproduction] Destroy the door when the wall is destroyed"""
    """State 0,1: End state"""
    return 0

def event_m10_18_x97(z11=_):
    """[Execution] When the wall is destroyed, the door is also destroyed.
    z11: Door OBJ instance ID
    """
    """State 0,1: Door destruction"""
    DestroyObj(z11, z11, 0)
    """State 2: End state"""
    return 0

def event_m10_18_x98(z10=_):
    """[Condition] When the wall is destroyed, the door is also destroyed.
    z10: Wall OBJ instance ID
    """
    """State 0,1: Wall waiting for destruction"""
    IsObjBroken(0, z10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_18_x99(z8=118000010, z9=10182000):
    """[Preset] Onboard OBJ drawing switching
    z8: Ship arrival flag
    z9: Ship OBJ instance ID
    """
    """State 0,1: [Reproduction] Drawing switching of OBJ on board _SubState"""
    call = event_m10_18_x100(z8=z8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Onboard OBJ drawing switching_SubState"""
        assert event_m10_18_x101(z8=z8, z9=z9)
    """State 3: [Execution] OBJ drawing switching on board _SubState"""
    assert event_m10_18_x102()
    """State 4: End state"""
    return 0

def event_m10_18_x100(z8=118000010):
    """[Reproduction] Onboard OBJ drawing switching
    z8: Ship arrival flag
    """
    """State 0,2: Has the ship already arrived?"""
    if GetEventFlag(z8) != 0:
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

def event_m10_18_x101(z8=118000010, z9=10182000):
    """[Conditions] Onboard OBJ drawing switching
    z8: Ship arrival flag
    z9: Ship OBJ instance ID
    """
    """State 0,1: Has the ship arrived?"""
    CompareEventFlag(0, z8, 1)
    CompareObjState(0, z9, 23, 0)
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
    event_m10_18_x1(z106=104131, z107=10184200, z108=246, z109=7260)

def event_m10_18_111203():
    """OBJ: Dwarf (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7260:Lonesome Gavlan
    event_m10_18_x4(z101=118010140, z102=118020141, z103=104130, z104=10184200, z105=111202, npc1=7260)

def event_m10_18_111204():
    """OBJ: Dwarf (hidden port): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_18_x6(z91=245, z92=104131)

def event_m10_18_111272():
    """OBJ: Female Knight (Hidden Port): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_18_x1(z106=104191, z107=10184000, z108=91, z109=7520)

def event_m10_18_111273():
    """OBJ: Woman Knight (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_18_x4(z101=118010100, z102=118020101, z103=104190, z104=10184000, z105=111272, npc1=7520)

def event_m10_18_111274():
    """OBJ: Woman Knight (Hidden Harbor): Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_18_x6(z91=90, z92=104191)

def event_m10_18_111275():
    """OBJ: Woman Knight (Hidden Port): Appearance Judgment"""
    """State 0,1: [Lib] NPC: Woman Knight: Appearance Judgment_SubState"""
    event_m10_18_x5(z93=102480, z94=102481, z95=102483, z96=102487, z97=102492, z98=102485, z99=102486,
                    z100=102488)

def event_m10_18_111276():
    """OBJ: Woman Knight (Hidden Port): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_18_x26(z68=102502, z69=566, z70=104190, z71=60, z72=103690, z73=-1)

def event_m10_18_111277():
    """OBJ: Female Knight (Hidden Port): White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_18_x36(z59=118000081, z60=102498, z61=204, z62=7520)

def event_m10_18_111392():
    """OBJ: Magician (Hidden Port): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_18_x1(z106=104301, z107=10184100, z108=136, z109=7660)

def event_m10_18_111393():
    """OBJ: Magician (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7660:Carhillion of the Fold
    event_m10_18_x4(z101=118010120, z102=118020121, z103=104300, z104=10184100, z105=111392, npc1=7660)

def event_m10_18_111394():
    """OBJ: Magician (hidden port): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_18_x6(z91=135, z92=104301)

def event_m10_18_111395():
    """OBJ: Magician (Hidden Port): Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Magician_SubState"""
    event_m10_18_x25(z74=102721)

def event_m10_18_111800():
    """Small white spirit 1"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_18_x31(z65=567)

def event_m10_18_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_18_x45(z47=118020109, z48=33)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_18_4001000():
    """[DC] Bridge that can be defeated"""
    """State 0,2: [DC] [Preset] Defeatable Bridge_SubState"""
    assert event_m10_18_x107(z1=6001000, z2=10181080, z3=10181090, val1=0.7, z4=118000014)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4002000():
    """[DC] Oil bottle _02"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z54=10181405, z55=10181455, z56=50, z57=242, z58=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z49=10181455, z50=50, z51=242, z52=0, z53=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4002010():
    """[DC] Oil bottle_03"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z54=10181410, z55=10181460, z56=50, z57=241, z58=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z49=10181460, z50=50, z51=241, z52=0, z53=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4002020():
    """[DC] Oil bottle_04"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z54=10181415, z55=10181465, z56=50, z57=240, z58=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z49=10181465, z50=50, z51=240, z52=0, z53=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4002030():
    """[DC] Oil bottle _05"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m10_18_x40(z54=10181420, z55=10181470, z56=50, z57=243, z58=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m10_18_x44(z49=10181470, z50=50, z51=243, z52=0, z53=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4003000():
    """[DC] Sailor_Unlockable Management_1"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_18_x53(z41=1510, z42=7, z43=1, z44=170000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4003010():
    """[DC] Sailor_Unlockable Management_2"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_18_x53(z41=5040, z42=7, z43=1, z44=170000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4003020():
    """[DC] Sailor_Unlockable Management_3"""
    """State 0,2: [Lib] [DC] [Preset] Character_Unlockable_SubState"""
    assert event_m10_18_x53(z41=5041, z42=7, z43=1, z44=170000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_18_x49(z45=9000, z46=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_18_4031000():
    """[DC] NPC White Spirit_Gesture Management_Double Sided Warrior: Snake Head"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_18_x57(z38=118000081, z39=844, z40=118020082)
    """State 1: Finish"""
    EndMachine()

