# -*- coding: utf-8 -*-
def event_m10_34_3000():
    """Boss: Dog Mouse_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_34_x5(flag2=134000081, z32=300000, z33=300000, z34=101, z35=1034000, z36=134020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_4000():
    """Boss Battle_Death Count"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9000)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4010():
    """Boss Battle_Death Count_2"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9001)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4020():
    """Boss Battle_Death Count_3"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9002)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4030():
    """Boss Battle_Death Count_4"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9003)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4040():
    """Boss Battle_Death Count_5"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9004)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4050():
    """Boss Battle_Death Count_6"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9005)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4060():
    """Boss Battle_Death Count_7"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9006)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4070():
    """Boss Battle_Death Count_8"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9007)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4080():
    """Boss Battle_Death Count_9"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9008)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4090():
    """Boss Battle_Death Count_10"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9009)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4100():
    """Boss Battle_Death Count_11"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9010)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4110():
    """Boss Battle_Death Count_12"""
    """State 0,3: [Preset] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x43(z9=9011)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Done():
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_34_4500():
    """Boss variable reset"""
    """State 0,2: [Preset] Variable reset for boss_SubState"""
    assert event_m10_34_x53()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_5000():
    """Boss Battle_Boss Generation Flag Stand"""
    """State 0,2: [Preset] Boss Battle_Boss Generation Flag Stand_SubState"""
    assert event_m10_34_x48()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_6000():
    """[Insect key interlock] Launch of drawbridge 1"""
    """State 0,2: [Preset] Drawbridge_SubState"""
    assert event_m10_34_x33(z10=10342100, z11=10341010, z12=600000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_6010():
    """Using bug keys_Drawbridge 1"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_34_x19(z26=10342100)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_34_7000():
    """[Insect key interlocking] water dripping _ torches disappear with water"""
    """State 0,2: [Preset] Water dripping_SubState"""
    assert event_m10_34_x35(z7=10342001, z8=700000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_34_7010():
    """Use insect key _ water dripping"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_34_x12(z27=10342001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_8000():
    """[Insect key interlocking] Lights off_Activate"""
    """State 0,2: [Preset] Light Off_SubState"""
    assert event_m10_34_x38(z1=10342101, z2=70, z3=20)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_8010():
    """Using bug keys_Lights off"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_34_x19(z26=10342101)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_34_10000():
    """[Insect key interlocking] Launch of drawbridge 2"""
    """State 0,2: [Preset] Drawbridge_SubState"""
    assert event_m10_34_x33(z10=10342102, z11=10341011, z12=1000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_10010():
    """Using bug keys_Drawbridge 2"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_34_x19(z26=10342102)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_34_11000():
    """[Insect key interlock] Poisonous rat _ In front of insect key _ activation"""
    """State 0,2: [Preset] Poisonous mouse image_SubState"""
    assert event_m10_34_x29(z13=10342103, z14=10341110, z15=10341111, z16=20, z17=240, z18=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_11010():
    """Insect key use_Boss"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_34_x19(z26=10342103)
    """State 1: State"""
    EndMachine()
    Quit()

def event_m10_34_12000():
    """[Insect key interlock] Poisonous rat _ left hand first body _ activation"""
    """State 0,2: [Preset] Poisonous mouse image_SubState"""
    assert event_m10_34_x29(z13=10342004, z14=10341120, z15=10341121, z16=20, z17=241, z18=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_12010():
    """Insect key use_poisonous rat_first left hand"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_34_x12(z27=10342004)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_13000():
    """[Insect key interlock] Poisonous rat _ left eye 2nd body _ activation"""
    """State 0,2: [Preset] Poisonous mouse image_SubState"""
    assert event_m10_34_x29(z13=10342002, z14=10341130, z15=10341131, z16=20, z17=242, z18=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_13010():
    """Using insect keys _ Poisonous mice _ Second left hand"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_34_x12(z27=10342002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_14000():
    """[Insect key interlock] Poisonous rat _ 3rd left hand _ activation"""
    """State 0,2: [Preset] Poisonous mouse image_SubState"""
    assert event_m10_34_x29(z13=10342000, z14=10341140, z15=10341141, z16=20, z17=243, z18=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_14010():
    """Insect key use_Poisoning mouse_Left hand third body"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_34_x12(z27=10342000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_80000():
    """After the fire area 01_ pledge area, in front of the boss room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_34_x23(z24=1034000, z25=1034099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_81000():
    """Regenerative fire 02_in front of the pledge area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_34_x23(z24=1034100, z25=1034199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_34_x0(z44=104421, z45=10344000, z46=286, z47=2262):
    """[Lib] NPC: Grave Placement: General purpose
    z44: Death map: Global event flag
    z45: Tomb: OBJ instance ID
    z46: Tomb move to: Generator ID
    z47: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z44, 1)
    IsGraveGeneratable(8, z47, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z45, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z45, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_34_x1(z41=104420, z42=10344000, npc1=2262):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z41: Global: death flag
    z42: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z42, 10, 0)
    CompareObjState(1, z42, 20, 0)
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
    IsObjSearched(0, z42)
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

def event_m10_34_x2(z39=134010100, z40=134020101, npc1=2262):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z39: Area other flags: Ghost appearance
    z40: Area other flags: Conversation start
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
    SetEventFlag(z39, 1)
    CompareEventFlag(0, z39, 1)
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
    SetEventFlag(z40, 1)
    CompareEventFlag(0, z40, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_34_x3(z39=134010100, z40=134020101, z41=104420, z42=10344000, z43=111512, npc1=2262):
    """[Lib] NPC: Grave: Key guide: General purpose
    z39: Ghost Appearance: Area Other Flag
    z40: Conversation start: Area and other flags
    z41: Death: Global event flag
    z42: Tomb: OBJ instance ID
    z43: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z43, 1, 0)
    CompareEventFlag(9, z39, 1)
    CompareObjState(9, z42, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z40, 1)
        CompareEventFlag(0, z40, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_34_x1(z41=z41, z42=z42, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_34_x2(z39=z39, z40=z40, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_34_x4(z37=285, z38=104421):
    """[Lib] NPC: Death determination: General purpose
    z37: Generator ID
    z38: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z38, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z37)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z38, 1)
            CompareEventFlag(0, z38, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_34_x5(flag2=134000081, z32=300000, z33=300000, z34=101, z35=1034000, z36=134020080, mode2=0):
    """[Lib] [Preset] Boss Battle Start
    flag2: Boss destruction flag
    z32: Start point ID
    z33: End point ID
    z34: Sound ID
    z35: Boss Battle ID
    z36: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_34_x6(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_34_x7(z32=z32, z33=z33)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_34_x8(z34=z34, z35=z35, z36=z36)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_34_x9()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_34_x10(z35=z35)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_34_x11(z34=z34, z35=z35, z36=z36, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_34_x6(flag2=134000081):
    """[Reproduction] Boss Battle_Start
    flag2: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag2) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_34_x7(z32=300000, z33=300000):
    """[Condition] Boss Battle_Start
    z32: Start point ID
    z33: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z32, z33, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z32, z33, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x8(z34=101, z35=1034000, z36=134020080):
    """[Execution] Boss Battle_Start
    z34: Sound ID
    z35: Boss Battle ID
    z36: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z34)
    """State 1: Boss battle start notification"""
    StartBossFight(z35)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z36, 1)
    """State 4: End state"""
    return 0

def event_m10_34_x9():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_34_x10(z35=1034000):
    """[Condition] Boss Battle_End Judgment
    z35: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z35, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x11(z34=101, z35=1034000, z36=134020080, mode2=0):
    """[Execute] Boss Battle_End
    z34: Sound ID
    z35: Boss Battle ID
    z36: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z36, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z35)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z34)
    """State 5: End state"""
    return 0

def event_m10_34_x12(z27=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z27: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_34_x13(z26=z27)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_34_x17(z26=z27)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_34_x18()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_34_x14(z26=z27, mode1=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_34_x15(z26=z27, z29=38, z30=3, z31=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_34_x16(z26=z27, z28=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_34_x13(z26=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z26: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z26, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z26, 10)
        assert CompareObjStateId(z26, 10, 0)
    elif CompareObjStateId(z26, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z26, 74, 1) and CompareObjStateId(z26, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_34_x14(z26=_, mode1=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z26: Object instance ID
    mode1: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z26)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode1) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_34_x15(z26=_, z29=38, z30=_, z31=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z26: Object instance ID
    z29: Key guide type
    z30: Event action
    z31: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z26, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z26, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z26, 30)
        assert CompareObjStateId(z26, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z26, z29, z30)
        assert PlayerIsInEventAction(z30) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z30, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z26, 74, 0)
        CompareObjState(1, z26, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z31)
            assert CompareObjStateId(z26, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z26, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_34_x16(z26=_, z28=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z26: Object instance ID
    z28: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z26, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_34_x17(z26=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z26: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z26, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x18():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_34_x19(z26=_):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z26: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_34_x13(z26=z26)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_34_x17(z26=z26)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_34_x18()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_34_x14(z26=z26, mode1=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_34_x15(z26=z26, z29=38, z30=12, z31=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_34_x16(z26=z26, z28=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_34_x20():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_34_x21(z24=_, z25=_):
    """[Lib] [execute] Rebirth fire
    z24: Flag start ID
    z25: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z24, z25, 0)
    """State 2: End state"""
    return 0

def event_m10_34_x22():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_34_x23(z24=_, z25=_):
    """[Lib] [Preset] Rebirth
    z24: Flag start ID
    z25: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_34_x20()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_34_x22()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_34_x21(z24=z24, z25=z25)
    """State 4: End state"""
    return 0

def event_m10_34_x24(z20=10000000, z21=_, z22=0, z23=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z20: Summon range
    z21: Generator ID
    z22: Appearance: Minimum time
    z23: Appearance: Maximum time
    """
    """State 0,10: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Black Phantom Appearance: Online"""
        IsOffline(0, 0)
        if ConditionGroup(0):
            """State 9: Black Phantom Appearance: Sign removed"""
            DeleteNpcPhantom(z21)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z20, z20, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z22, 3, z23)
                IsPlayerInsidePoint(1, z20, z20, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z21)
                    Goto('L0')
                elif ConditionGroup(1):
                    pass
                elif ConditionGroup(2):
                    pass
            elif ConditionGroup(0):
                pass
        """State 6: Black Phantom Appearance: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 4: Black Phantom Appearance: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_34_x25(flag1=134020107, z19=22):
    """[Lib] [Preset] Get trophy
    flag1: Acquisition trigger_other flags
    z19: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag1) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag1, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z19)
    """State 4: End state"""
    return 0

def event_m10_34_x26(z15=_, z13=_, z16=20, z17=_, z18=1):
    """[Reproduction] Reproduction of vomiting mouse state
    z15: Poison swamp instance ID
    z13: Bug key instance ID
    z16: Hit group ID
    z17: Grand material ID
    z18: Grand material slot ID
    """
    """State 0,1: Has the insect key been activated?"""
    if CompareObjStateId(z13, 20, 0):
        """State 2: Poison swamp OBJ display, damage ON"""
        SetGroundMaterial(z16, z17, z18)
        ChangeObjState(z15, 70)
        """State 5: Activated"""
        return 1
    else:
        """State 3: Damage off"""
        SetGroundMaterial(z16, z17, 0)
        """State 4: Not started"""
        return 0

def event_m10_34_x27(z13=_):
    """[Conditions] Poisonous rat image
    z13: Bug key instance ID
    """
    """State 0,1: Bug key waiting"""
    CompareObjState(0, z13, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x28(z14=_, z15=_, z16=20, z17=_, z18=1):
    """[Execution] Poisonous mouse image
    z14: Statue instance ID
    z15: Poison swamp instance ID
    z16: Hit group ID
    z17: Grand material ID
    z18: Grand material slot ID
    """
    """State 0,1: OBJ State Transition: Mouse Image: 70"""
    ChangeObjState(z14, 70)
    assert (GetStateTime() > 4.5) != 0
    """State 2: OBJ State Transition: Poison Swamp: 70"""
    ChangeObjState(z15, 70)
    """State 3: Damage ON"""
    SetGroundMaterial(z16, z17, z18)
    """State 4: End state"""
    return 0

def event_m10_34_x29(z13=_, z14=_, z15=_, z16=20, z17=_, z18=1):
    """[Preset] Poisonous rat image
    z13: Bug key instance ID
    z14: Statue instance ID
    z15: Poison swamp instance ID
    z16: Hit group ID
    z17: Grand material ID
    z18: Grand material slot ID
    """
    """State 0,1: [Reproduction] Reproduction of poisoned mouse state_SubState"""
    call = event_m10_34_x26(z15=z15, z13=z13, z16=z16, z17=z17, z18=z18)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Insect key activation determination_SubState"""
        assert event_m10_34_x27(z13=z13)
        """State 3: [Execution] Poisonous mouse image_SubState"""
        assert event_m10_34_x28(z14=z14, z15=z15, z16=z16, z17=z17, z18=z18)
    """State 4: End state"""
    return 0

def event_m10_34_x30(z10=_, z12=_):
    """[Reproduction] Drawbridge
    z10: Bug key instance ID
    z12: Navimesh switching point ID
    """
    """State 0,1: Has the insect key been activated?"""
    if CompareObjStateId(z10, 20, 0):
        """State 2: Navi mesh switching"""
        DeleteNavimeshAttribute(z12, 2)
        """State 4: Activated"""
        return 1
    else:
        """State 3: Not started"""
        return 0

def event_m10_34_x31(z1=_):
    """[Conditions] Lights off
    z1: Bug key instance ID
    """
    """State 0,1: Bug key waiting"""
    CompareObjState(0, z1, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x32(z11=_, z12=_):
    """[Execution] drawbridge
    z11: Bridge instance ID
    z12: Navimesh switching point ID
    """
    """State 0,1: OBJ state transition: 70"""
    ChangeObjState(z11, 70)
    """State 2: OBJ state transition completion wait: 20"""
    CompareObjState(0, z11, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navi mesh switching"""
    DeleteNavimeshAttribute(z12, 2)
    """State 4: End state"""
    return 0

def event_m10_34_x33(z10=_, z11=_, z12=_):
    """[Preset] Drawbridge
    z10: Bug key instance ID
    z11: Bridge instance ID
    z12: Navimesh switching point ID
    """
    """State 0,2: [Reproduction] Drawbridge_SubState"""
    call = event_m10_34_x30(z10=z10, z12=z12)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] Insect key activation_SubState"""
        assert event_m10_34_x31(z1=z10)
        """State 3: [Execution] Drawbridge_SubState"""
        assert event_m10_34_x32(z11=z11, z12=z12)
    """State 4: End state"""
    return 0

def event_m10_34_x34():
    """[Execution] water dripping"""
    """State 0,1: Torches disappear (water)"""
    RemovePlayerTorches(10)
    """State 2: End state"""
    return 0

def event_m10_34_x35(z7=10342001, z8=700000):
    """[Preset] Water dripping
    z7: Bug key instance ID
    z8: Water dripping point ID
    """
    """State 0,1: [Reproduction] Water dripping_SubState"""
    call = event_m10_34_x36(z7=z7)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Water dripping_Insect key activation judgment_SubState"""
        assert event_m10_34_x37(z7=z7)
        """State 5: [Execution] Water dripping_Waterfall activation_SubState"""
        assert event_m10_34_x55()
    """State 4: [Condition] Water dripping_Point intrusion judgment_SubState"""
    assert event_m10_34_x54(z8=z8)
    """State 3: [Execution] Water dripping_SubState"""
    assert event_m10_34_x34()
    """State 6: End state"""
    return 0

def event_m10_34_x36(z7=10342001):
    """[Reproduction] Water dripping
    z7: Bug key instance ID
    """
    """State 0,1: Has the insect key been activated?"""
    if CompareObjStateId(z7, 20, 0):
        """State 2: Enable Grand Material Falls"""
        SetGroundMaterial(10, 240, 1)
        """State 4: Activated"""
        return 1
    else:
        """State 3: Not started"""
        return 0

def event_m10_34_x37(z7=10342001):
    """[Condition] Water dripping
    z7: Bug key instance ID
    """
    """State 0,1: Bug key waiting"""
    CompareObjState(0, z7, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x38(z1=10342101, z2=70, z3=20):
    """[Preset] Lights off
    z1: Bug key instance ID
    z2: Lighting off state ID
    z3: Illuminated state ID
    """
    """State 0,1: [Reproduction] Light off_SubState"""
    call = event_m10_34_x39(z1=z1, z3=z3)
    if call.Get() == 0:
        """State 2: [Condition] Light off_SubState"""
        assert event_m10_34_x31(z1=z1)
        """State 3: [Execution] Light off_SubState"""
        Label('L0')
        assert event_m10_34_x56(z4=10342200, z2=z2, z5=0.7, z6=10340000, z3=z3)
        """State 4: [Execution] Light extinguished_2_SubState"""
        Label('L1')
        assert event_m10_34_x56(z4=10342205, z2=z2, z5=0.7, z6=10340010, z3=z3)
        """State 5: [Execution] Light off_3_SubState"""
        Label('L2')
        assert event_m10_34_x56(z4=10342210, z2=z2, z5=0.7, z6=10340020, z3=z3)
        """State 6: [Execution] Light extinction_4_SubState"""
        Label('L3')
        assert event_m10_34_x56(z4=10342215, z2=z2, z5=0.7, z6=10340030, z3=z3)
        """State 7: [Execution] Lights off_5_SubState"""
        Label('L4')
        assert event_m10_34_x56(z4=10342225, z2=z2, z5=0.7, z6=10340040, z3=z3)
        """State 8: [Execution] Light extinguished_6_SubState"""
        Label('L5')
        assert event_m10_34_x56(z4=10342230, z2=z2, z5=0.7, z6=10340050, z3=z3)
    elif call.Get() == 2:
        Goto('L0')
    elif call.Get() == 3:
        Goto('L1')
    elif call.Get() == 4:
        Goto('L2')
    elif call.Get() == 5:
        Goto('L3')
    elif call.Get() == 6:
        Goto('L4')
    elif call.Get() == 7:
        Goto('L5')
    elif call.Get() == 1:
        pass
    """State 9: End state"""
    return 0

def event_m10_34_x39(z1=10342101, z3=20):
    """[Reproduction] Lights off
    z1: Bug key instance ID
    z3: Illuminated state ID
    """
    """State 0,1: Has the insect key been activated?"""
    if CompareObjStateId(z1, 20, 0):
        pass
    else:
        Goto('L5')
    """State 3: Lighting 1 status judgment"""
    if CompareObjStateId(10342200, z3, 0):
        pass
    else:
        Goto('L4')
    """State 9: Turn off point light 1"""
    SetPointLightEnabled(10340000, 0, 0)
    """State 4: Lighting 2 status judgment"""
    if CompareObjStateId(10342205, z3, 0):
        pass
    else:
        Goto('L3')
    """State 10: Turn off point light 2"""
    SetPointLightEnabled(10340010, 0, 0)
    """State 5: Lighting 3 status judgment"""
    if CompareObjStateId(10342210, z3, 0):
        pass
    else:
        Goto('L2')
    """State 11: Turn off point light 3"""
    SetPointLightEnabled(10340020, 0, 0)
    """State 6: Lighting 4 status judgment"""
    if CompareObjStateId(10342215, z3, 0):
        pass
    else:
        Goto('L1')
    """State 12: Turn off point light 4"""
    SetPointLightEnabled(10340030, 0, 0)
    """State 7: Lighting 5 status judgment"""
    if CompareObjStateId(10342225, z3, 0):
        pass
    else:
        Goto('L0')
    """State 13: Turn off point light 5"""
    SetPointLightEnabled(10340040, 0, 0)
    """State 8: Lighting 6 status judgment"""
    if CompareObjStateId(10342230, z3, 0):
        """State 14: Turn off point light 6"""
        SetPointLightEnabled(10340050, 0, 0)
        """State 16: Finish"""
        return 1
    else:
        """State 22: From lighting 6"""
        return 7
    """State 21: From lighting 5"""
    Label('L0')
    return 6
    """State 20: From lighting 4"""
    Label('L1')
    return 5
    """State 19: From lighting 3"""
    Label('L2')
    return 4
    """State 18: From lighting 2"""
    Label('L3')
    return 3
    """State 17: From lighting 1"""
    Label('L4')
    return 2
    """State 2: Light up"""
    Label('L5')
    ChangeObjState(10342200, 10)
    ChangeObjState(10342205, 10)
    ChangeObjState(10342210, 10)
    ChangeObjState(10342215, 10)
    ChangeObjState(10342225, 10)
    ChangeObjState(10342230, 10)
    SetPointLightEnabled(10340000, 1, 0)
    SetPointLightEnabled(10340010, 1, 0)
    SetPointLightEnabled(10340020, 1, 0)
    SetPointLightEnabled(10340030, 1, 0)
    SetPointLightEnabled(10340040, 1, 0)
    SetPointLightEnabled(10340050, 1, 0)
    """State 15: Not started"""
    return 0

def event_m10_34_x40():
    """[Reproduction] Boss Battle_Death Count"""
    """State 0,1: Boss destroyed or guest?"""
    if GetEventFlag(134000081) != 0:
        """State 3: Simple end"""
        Label('L0')
        return 1
    elif IsGuest() != 0:
        Goto('L0')
    else:
        """State 2: End state"""
        return 0

def event_m10_34_x41(z9=_):
    """[Condition] Boss Battle_Death Count
    z9: Generator ID
    """
    """State 0,1: Character death waiting"""
    CompareEventFlagValue(0, 1, 10, 100, 3)
    IsChrDead(1, z9)
    IsChrInsidePoint(8, z9, 400000, 400003, 1)
    CompareEventFlag(8, 134000081, 1)
    if ConditionGroup(0):
        """State 3: Generator stop"""
        return 1
    elif ConditionGroup(1):
        """State 2: End state"""
        return 0
    elif ConditionGroup(8):
        """State 4: Enemy deleted"""
        return 2

def event_m10_34_x42(z9=_):
    """[Execution] Boss Battle_Death Count
    z9: Generator ID
    """
    """State 0,1: Death count +1"""
    AddAreaVariable(10, 1)
    """State 2: Generator restart waiting"""
    IsChrActive(0, z9, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_34_x43(z9=_):
    """[Preset] Boss Battle_Death Count
    z9: Generator ID
    """
    """State 0,1: [Reproduction] Boss Battle_Death Count_SubState"""
    call = event_m10_34_x40()
    if call.Done():
        """State 2: [Condition] Boss Battle_Death Count_SubState"""
        call = event_m10_34_x41(z9=z9)
        if call.Get() == 1:
            """State 4: [Execution] Boss Battle_Generator Stop Flag ON_SubState"""
            assert event_m10_34_x44()
        elif call.Get() == 2:
            """State 5: [Execute] Enemy Delete_SubState"""
            assert event_m10_34_x49(z9=z9)
        elif call.Done():
            """State 3: [Execution] Boss Battle_Death Count_SubState"""
            assert event_m10_34_x42(z9=z9)
            """State 6: Rerun"""
            return 0
    elif call.Get() == 1:
        pass
    """State 7: Finish"""
    return 1

def event_m10_34_x44():
    """[Execution] Boss Battle_Generator Stop Flag ON"""
    """State 0,1: Generator stop flag ON"""
    SetEventFlag(134020086, 1)
    """State 2: End state"""
    return 0

def event_m10_34_x45():
    """[Reproduction] Boss Battle_Boss Generation Flag Stand"""
    """State 0,1: Boss destroyed or guest?"""
    if GetEventFlag(134000081) != 0:
        """State 3: Simple end"""
        Label('L0')
        return 1
    elif IsGuest() != 0:
        Goto('L0')
    else:
        """State 2: End state"""
        return 0

def event_m10_34_x46():
    """[Condition] Boss Battle_Boss Generation Flag Stand"""
    """State 0,1: Did you destroy a certain number of Zako?"""
    CompareEventFlagValue(0, 1, 10, 10, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_34_x47():
    """[Execution] Boss Battle_Boss Generation Flag Stand"""
    """State 0,1: Boss generation flag ON"""
    SetEventFlag(134020083, 1)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 3: End state"""
    return 0

def event_m10_34_x48():
    """[Preset] Boss Battle_Boss Generation Flag Stand"""
    """State 0,1: [Reproduction] Boss Battle_Boss Generation Flag Stand_SubState"""
    call = event_m10_34_x45()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Boss Battle_Boss Generation Flag Stand_SubState"""
        assert event_m10_34_x46()
        """State 3: [Execution] Boss Battle_Boss Generation Flag Stand_SubState"""
        assert event_m10_34_x47()
    """State 4: End state"""
    return 0

def event_m10_34_x49(z9=_):
    """[Execute] Enemy Delete
    z9: Generator ID
    """
    """State 0,1: Enemy deleted"""
    PauseEnemy(z9, 1)
    """State 2: End state"""
    return 0

def event_m10_34_x50():
    """[Reproduction] Boss variable reset_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_34_x51():
    """[Condition] Boss variable reset_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_34_x52():
    """[Execute] Reset variable for boss"""
    """State 0,1: Initializing area variables"""
    SetAreaVariable(10, 0)
    """State 2: End state"""
    return 0

def event_m10_34_x53():
    """[Preset] Boss variable reset"""
    """State 0,1: [Reproduce] Boss variable reset_empty_SubState"""
    assert event_m10_34_x50()
    """State 3: [Condition] Boss variable reset_empty_SubState"""
    assert event_m10_34_x51()
    """State 2: [Execution] Boss variable reset_SubState"""
    assert event_m10_34_x52()
    """State 4: End state"""
    return 0

def event_m10_34_x54(z8=700000):
    """[Condition] Water dripping_Point intrusion judgment
    z8: Water dripping point ID
    """
    """State 0,1: Got a point with a torch?"""
    IsPlayerInsidePoint(8, z8, z8, 1)
    IsPlayerUsingTorch(8, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_34_x55():
    """[Execution] waterfall _ waterfall start"""
    """State 0,1: OBJ State Transition: Waterfall Damipoli: 20"""
    ChangeObjState(10341030, 20)
    """State 2: Enable Grand Material Falls"""
    SetGroundMaterial(10, 240, 1)
    """State 3: End state"""
    return 0

def event_m10_34_x56(z4=_, z2=70, z5=0.7, z6=_, z3=20):
    """[Execution] Lights off
    z4: Instance ID of lighting OBJ
    z2: Lighting off state ID
    z5: State elapsed time
    z6: Point light ID
    z3: Illuminated state ID
    """
    """State 0,1: Turn off the lights"""
    ChangeObjState(z4, z2)
    """State 4: Is the light turned off?"""
    CompareObjState(0, z4, z3, 0)
    assert ConditionGroup(0)
    """State 3: Point light off"""
    SetPointLightEnabled(z6, 0, 0)
    """State 2: A certain amount of time has elapsed"""
    CompareStateTime(0, z5, 2, z5)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m10_34_111512():
    """OBJ: Mouse king (Saint Cemetery): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_34_x0(z44=104421, z45=10344000, z46=286, z47=2262)
    Quit()

def event_m10_34_111513():
    """OBJ: Mouse King (Saint Cemetery): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    event_m10_34_x3(z39=134010100, z40=134020101, z41=104420, z42=10344000, z43=111512, npc1=2262)
    Quit()

def event_m10_34_111514():
    """OBJ: Mouse King (Saint Cemetery): Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_34_x4(z37=285, z38=104421)
    Quit()

def event_m10_34_118220():
    """Multi-use NPC: Mage (male): Black Phantom Appearance: Offline"""
    """State 0,1: [DC] Total lap count judgment"""
    if (GetGameCycleForBonfire(34655) > 2) != 0:
        """State 3: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_2_SubState"""
        event_m10_34_x24(z20=10000000, z21=641, z22=0, z23=2)
        Quit()
    else:
        """State 2: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
        event_m10_34_x24(z20=10000000, z21=640, z22=0, z23=2)
        Quit()

def event_m10_34_120040():
    """Trophy: Mouse Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_34_x25(flag1=134020107, z19=22)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

