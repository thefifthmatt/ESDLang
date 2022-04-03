# -*- coding: utf-8 -*-
def event_m10_17_1000():
    """Gate opened with lever"""
    """State 0,2,3: [Reproduction] Gate_SubState opened with lever"""
    assert event_m10_17_x78()
    """State 4: [Condition] Gate_SubState opened with lever"""
    assert event_m10_17_x79(z57=10172013)
    """State 5: [Execution] Gate opened with lever _SubState"""
    assert event_m10_17_x80(z56=100000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_2000():
    """Hanging poison 01_attach"""
    """State 0,1: Attach a poison to the chain"""
    AttachObjToObj(10173500, 150, 10173550)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_17_2010():
    """Suspended poison 01_operation"""
    """State 0,2: [Preset] Suspended Poison _ Operation _ SubState"""
    assert event_m10_17_x91(z50=10172120)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_3000():
    """OBJ attach of giant windmill"""
    """State 0,1: Attach wings to shaft"""
    AttachObjToObj(10171500, 150, 10171501)
    AttachObjToObj(10171500, 151, 10171502)
    AttachObjToObj(10171500, 152, 10171503)
    AttachObjToObj(10171500, 153, 10171504)
    AttachObjToObj(10171500, 154, 10171505)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4000():
    """Elevator ⇔ Molten Fortress"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_17_x15(z81=10173100, z82=400010, z83=400000, z84=10172030, z85=10172020)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_4010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_17_x20(z112=10173100, z113=10172030, z114=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_4020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_17_x20(z112=10173100, z113=10172020, z114=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_4030():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m10_17_x46(z86=403000, z87=10173100, z88=105420, z89=70, z90=80, z91=1, z92=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_4050():
    """For connection_Connection flag OFF"""
    """State 0,3: [Lib] [Preset] Switch the connection flag at the point _SubState"""
    call = event_m10_17_x60(z72=405000, z73=405000, z74=105420, z75=0, z76=1)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m10_17_5000():
    """Iron lattice that can be opened and closed by levers"""
    """State 0,2: [Preset] Iron lattice that can be opened and closed by lever"""
    assert event_m10_17_x114(z14=500000, z15=10172110, z16=10171540, z17=10172900)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_6000():
    """Suspended poison 02_ attach"""
    """State 0,1: Attach a poison to the chain"""
    AttachObjToObj(10173510, 150, 10173560)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_17_6010():
    """Suspended poison 02_operation"""
    """State 0,2: [Preset] Suspended Poison _ Operation _ SubState"""
    assert event_m10_17_x91(z50=10172100)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_7000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_17_x26(z102=10171200)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_7010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_17_x36(z100=10171200, val3=10170010, z101=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_7020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10171300, z94=20, z95=702000, z96=0, z97=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_7100():
    """[Insect Key] Recovery Fountain_Poisonous_Startup"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_17_x26(z102=10171205)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_7110():
    """[Insect Key] Recovery Fountain _ Poisonous"""
    """State 0,2: [Preset] [Insect Key] Recovery Fountain_Poisonous_SubState"""
    assert (event_m10_17_x99(z28=10171205, z29=10171310, z30=10171315, z31=90, z32=240, z33=1, z34=2,
            z35=117000055))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_8000():
    """Boss: Shabazahat_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_17_x8(flag8=117000081, z115=800000, z116=800000, z117=102, z118=1017000, z119=117020080,
            mode3=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_8010():
    """Liberation of dead workers in cages 1"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173300, z37=117020085)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_8020():
    """Liberation of dead workers in cages 2"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173301, z37=117020086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_8030():
    """Liberation of dead workers in cages 3"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173302, z37=117020087)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_8040():
    """Liberation of dead workers in cages 4"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173303, z37=117020088)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_8500():
    """Boss: Naga_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_17_x8(flag8=117000091, z115=850000, z116=850000, z117=101, z118=1017010, z119=117020090,
            mode3=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_9000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10171355, z94=20, z95=900000, z96=0, z97=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_9010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10171360, z94=20, z95=901000, z96=0, z97=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_9020():
    """Hidden Door Navi Mesh Change 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10171350, z94=20, z95=902000, z96=0, z97=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_10000():
    """Disabling poison fog damage of enemy characters"""
    """State 0,2: [Preset] Enemy character's poison fog damage disabled_SubState"""
    assert (event_m10_17_x105(z20=147005, z21=311000, z22=200010010, z23=200010020, z24=200010030, z25=200010011,
            z26=200010021, z27=200010031))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_11000():
    """Wooden wall 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10173600, z94=20, z95=1100000, z96=0, z97=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_11010():
    """The wooden wall 2 where the enemy destroys"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10173605, z94=20, z95=1101000, z96=0, z97=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_12000():
    """Floor switch treadle _ in front of iron bar"""
    """State 0,2: [Preset] Floor switch tread arrow _SubState"""
    assert event_m10_17_x112(z18=10171131, z19=10171011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_12010():
    """Floor switch treadle _ crossroad"""
    """State 0,2: [Preset] Floor switch tread arrow _SubState"""
    assert event_m10_17_x112(z18=10171130, z19=10171012)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_14000():
    """Navi mesh change for destructible scaffold"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z93=10173800, z94=20, z95=1400000, z96=2, z97=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_15000():
    """Hunting Forest MAP loading and discarding"""
    """State 0,2: [Preset] Hunting Forest MAP loading discard_SubState"""
    assert event_m10_17_x119(z5=100, z6=105440)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_27000():
    """One-way door (destination jumped off)"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _2_SubState"""
    assert event_m10_17_x5(z130=0, z131=1101, z132=2700000, z133=117000180)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_31100():
    """[Asynchronous] Giant windmill"""
    """State 0,3: [Reproduction] Giant windmill_SubState"""
    call = event_m10_17_x92(z47=10171500, z48=117000055, z49=117000056)
    if call.Get() == 0:
        """State 4: [Condition] Giant windmill_SubState"""
        call = event_m10_17_x93(z46=10171500)
        if call.Get() == 1:
            """State 5: [Execution] Giant windmill_SubState"""
            assert (event_m10_17_x94(z38=10171500, z39=10171501, z40=10171502, z41=10171503, z42=10171504,
                    z43=117000055, z44=10171505, z45=117000056))
        elif call.Get() == 0:
            """State 2: Rerun"""
            RestartMachine()
            Quit()
    elif call.Get() == 1:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_32010():
    """Suspended ceiling: Ceiling"""
    """State 0,2: [Preset] Suspended ceiling_SubState"""
    assert event_m10_17_x84(z53=10172130, z54=10171530, z55=3201000, val1=7)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_42000():
    """Poison water drop"""
    """State 0,2: [Preset] Poison water drop_SubState"""
    assert event_m10_17_x118(z9=10173000, z10=10173001, z11=10173002, z12=10173003, z13=10173004, flag2=117000055)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_80000():
    """Reproduction Fire 01_Cave in front of village mining square"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z78=1017000, z79=1017099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_81000():
    """Rebirth Fire 02_After the Boss Java Hat, Lower Tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z78=1017100, z79=1017199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_82000():
    """Rebirth Fire 03_ Entrance Poison Destination Cave"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z78=1017200, z79=1017299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_83000():
    """After the huge windmill, the fireworks 04_"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z78=1017300, z79=1017399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_84000():
    """Hidden door in front of the boss room, tower top layer"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z78=1017400, z79=1017499)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_x0(z143=101710, mode4=0, flag9=117000118, z144=1, z145=1):
    """[Lib] Normal poly play
    z143: Poly play ID
    mode4: Destination point ID after poly play
    flag9: Poly drama played flag
    z144: End fade
    z145: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(flag9) != 1:
        """State 1: Poly play"""
        PlayCutscene(z143, z144, z145)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((mode4 > 1) != 0, mode4)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((mode4 > 1) != 0, mode4)
    SetEventFlag(flag9, 1)
    """State 7: End state"""
    return 0

def event_m10_17_x1(z139=_, z140=_, z141=_, z142=_):
    """[Lib] NPC: Grave Placement: General purpose
    z139: Death map: Global event flag
    z140: Tomb: OBJ instance ID
    z141: Tomb move to: Generator ID
    z142: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z139, 1)
    IsGraveGeneratable(8, z142, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z140, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z140, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_17_x2(z136=_, z137=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z136: Global: death flag
    z137: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z137, 10, 0)
    CompareObjState(1, z137, 20, 0)
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
    IsObjSearched(0, z137)
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

def event_m10_17_x3(z134=_, z135=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z134: Area other flags: Ghost appearance
    z135: Area other flags: Conversation start
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
    SetEventFlag(z134, 1)
    CompareEventFlag(0, z134, 1)
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
    SetEventFlag(z135, 1)
    CompareEventFlag(0, z135, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_17_x4(z134=_, z135=_, z136=_, z137=_, z138=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z134: Ghost Appearance: Area Other Flag
    z135: Conversation start: Area and other flags
    z136: Death: Global event flag
    z137: Tomb: OBJ instance ID
    z138: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z138, 1, 0)
    CompareEventFlag(9, z134, 1)
    CompareObjState(9, z137, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z135, 1)
        CompareEventFlag(0, z135, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_17_x2(z136=z136, z137=z137, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_17_x3(z134=z134, z135=z135, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_17_x5(z130=0, z131=1101, z132=2700000, z133=117000180):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z130: Text ID when opened
    z131: Text ID when not opened
    z132: Point ID
    z133: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z132, 0, z130, z131, z133, 0)
    """State 2: End state"""
    return 0

def event_m10_17_x6(z122=102480, z123=102482, z124=102483, z125=102486, z126=102491, z127=102485, z128=102487,
                    z129=102488):
    """[Lib] NPC: Woman Knight: Appearance Judgment
    z122: Sub 1 encountering: Global event flag
    z123: During sub-2 encounter: Global event flag
    z124: Sub 3 encountering: Global event flag
    z125: Generation stop: Global event flag
    z126: Appearance permission: Global event flag
    z127: Sub 1 generation stop: Global event flag
    z128: Sub 2 generation stop: Global event flag
    z129: Sub 3 generation stop: Global event flag
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
            CompareEventFlag(0, z125, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 2: Appearance determination: Judgment while encountering other maps"""
                CompareEventFlag(8, z122, 1)
                CompareEventFlag(8, z127, 0)
                CompareEventFlag(9, z123, 1)
                CompareEventFlag(9, z128, 0)
                CompareEventFlag(10, z124, 1)
                CompareEventFlag(10, z129, 0)
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
                        SetEventFlag(z126, 1)
                        CompareEventFlag(0, z126, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
        """State 3: Appearance judgment: Appearance impossible"""
        SetEventFlag(z126, 0)
        CompareEventFlag(0, z126, 0)
        assert ConditionGroup(0)
    """State 5: Appearance determination: System: Event end"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_17_x7(z120=_, z121=_):
    """[Lib] NPC: Death determination: General purpose
    z120: Generator ID
    z121: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z121, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z120)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z121, 1)
            CompareEventFlag(0, z121, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_17_x8(flag8=_, z115=_, z116=_, z117=_, z118=_, z119=_, mode3=0):
    """[Lib] [Preset] Boss Battle Start
    flag8: Boss destruction flag
    z115: Start point ID
    z116: End point ID
    z117: Sound ID
    z118: Boss Battle ID
    z119: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_17_x9(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_17_x10(z115=z115, z116=z116)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_17_x11(z117=z117, z118=z118, z119=z119)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_17_x12()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_17_x13(z118=z118)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_17_x14(z117=z117, z118=z118, z119=z119, mode3=mode3)
    """State 7: End state"""
    return 0

def event_m10_17_x9(flag8=_):
    """[Reproduction] Boss Battle_Start
    flag8: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_17_x10(z115=_, z116=_):
    """[Condition] Boss Battle_Start
    z115: Start point ID
    z116: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z115, z116, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z115, z116, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x11(z117=_, z118=_, z119=_):
    """[Execution] Boss Battle_Start
    z117: Sound ID
    z118: Boss Battle ID
    z119: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z117)
    """State 1: Boss battle start notification"""
    StartBossFight(z118)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z119, 1)
    """State 4: End state"""
    return 0

def event_m10_17_x12():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x13(z118=_):
    """[Condition] Boss Battle_End Judgment
    z118: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z118, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x14(z117=_, z118=_, z119=_, mode3=0):
    """[Execute] Boss Battle_End
    z117: Sound ID
    z118: Boss Battle ID
    z119: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z119, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z118)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode3) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z117)
    """State 5: End state"""
    return 0

def event_m10_17_x15(z81=10173100, z82=400010, z83=400000, z84=10172030, z85=10172020):
    """[Lib] [Preset] Elevator
    z81: OBJ instance ID of the elevator
    z82: On elevator point ID_
    z83: Elevator point ID_below
    z84: Upper lever OBJ instance ID
    z85: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_17_x16()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_17_x17(z81=z81, z82=z82, z83=z83, z84=z84, z85=z85)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_17_x50(z81=z81, z83=z83)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_17_x49(z81=z81, z82=z82)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_17_x18(z81=z81, z82=z82)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_17_x19(z81=z81, z83=z83)
    """State 7: End state"""
    return 0

def event_m10_17_x16():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x17(z81=10173100, z82=400010, z83=400000, z84=10172030, z85=10172020):
    """[Condition] Elevator
    z81: Elevator OBJ instance ID
    z82: On elevator point ID_
    z83: Elevator point ID_below
    z84: Upper lever OBJ instance ID
    z85: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z81, 10, 0)
    CompareObjState(1, z81, 40, 0)
    CompareObjState(2, z81, 80, 0)
    CompareObjState(2, z81, 41, 0)
    CompareObjState(3, z81, 70, 0)
    CompareObjState(3, z81, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z83, z83, 1)
        CompareObjState(0, z84, 74, 0)
        CompareObjState(0, z84, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z82, z82, 1)
        CompareObjState(0, z85, 74, 0)
        CompareObjState(0, z85, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_17_x18(z81=10173100, z82=400010):
    """[Execution] Elevator_Rise
    z81: Elevator OBJ instance ID
    z82: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z81, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z81, 30, 0)
    IsPlayerInsidePoint(8, z82, z82, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z81, 71)
    assert CompareObjStateId(z81, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x19(z81=10173100, z83=400000):
    """[Execution] Elevator_Descent
    z81: Elevator OBJ instance ID
    z83: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z81, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z81, 41, 0)
    IsPlayerInsidePoint(8, z83, z83, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z81, 81)
    assert CompareObjStateId(z81, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x20(z112=10173100, z113=_, z114=_):
    """[Lib] [Preset] Elevator lever
    z112: OBJ instance ID of the elevator
    z113: Lever OBJ instance ID
    z114: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_17_x21()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_17_x22(z112=z112, z113=z113, z114=z114)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_17_x23(z112=z112, z113=z113, z114=z114)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_17_x24(z112=z112, z113=z113, z114=z114)
    """State 5: Rerun"""
    return 0

def event_m10_17_x21():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x22(z112=10173100, z113=_, z114=_):
    """[Condition] Elevator lever_use judgment
    z112: OBJ instance ID of the elevator
    z113: Lever OBJ instance ID
    z114: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z112, z114, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_17_x23(z112=10173100, z113=_, z114=_):
    """[Execution] Elevator lever_Key guide valid
    z112: OBJ instance ID of the elevator
    z113: Lever OBJ instance ID
    z114: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z113, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z112, z114, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x24(z112=10173100, z113=_, z114=_):
    """[Execute] Elevator lever_key guide disabled
    z112: OBJ instance ID of the elevator
    z113: Lever OBJ instance ID
    z114: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z113, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z112, z114, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x25(z107=_, z108=_, z109=_, z110=_, z111=_):
    """[Lib] Appearance determination: General purpose
    z107: Death: Global event flag
    z108: Local emigration permission: Global event flag
    z109: Relocation permission after moving: Global event flag
    z110: Appearance determination: Area and other flags
    z111: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z107, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z108, 1)
            CompareEventFlag(8, z109, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z108, 1)
                CompareEventFlag(8, z111, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z110, 1)
                    CompareEventFlag(0, z110, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z110, 0)
                    CompareEventFlag(0, z110, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z110, 0)
        CompareEventFlag(0, z110, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_17_x26(z102=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z102: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_17_x27(z102=z102)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_17_x31(z102=z102)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_17_x32()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_17_x28(z102=z102, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_17_x29(z102=z102, z104=38, z105=3, z106=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_17_x30(z102=z102, z103=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_17_x27(z102=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z102: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z102, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z102, 10)
        assert CompareObjStateId(z102, 10, 0)
    elif CompareObjStateId(z102, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z102, 74, 1) and CompareObjStateId(z102, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_17_x28(z102=_, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z102: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z102)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_17_x29(z102=_, z104=38, z105=3, z106=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z102: Object instance ID
    z104: Key guide type
    z105: Event action
    z106: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z102, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z102, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z102, 30)
        assert CompareObjStateId(z102, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z102, z104, z105)
        assert PlayerIsInEventAction(z105) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z105, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z102, 74, 0)
        CompareObjState(1, z102, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z106)
            assert CompareObjStateId(z102, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z102, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_17_x30(z102=_, z103=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z102: Object instance ID
    z103: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z102, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_17_x31(z102=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z102: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z102, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x32():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x33(z100=10171200, val3=10170010):
    """[Reproduction] Hidden door 1_face SFX
    z100: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z100, 20, 0):
        pass
    else:
        Goto('L0')
    """State 2: Event light reproduction judgment"""
    if (not val3) != 0:
        pass
    else:
        """State 3: Event light ON"""
        SetPointLightEnabled(val3, 1, 0)
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
    if (not val3) != 0:
        pass
    else:
        """State 4: Event light OFF"""
        SetPointLightEnabled(val3, 0, 0)
    """State 9: Not started"""
    return 1

def event_m10_17_x34(z100=10171200):
    """[Conditions] Hidden door 1_Face SFX
    z100: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z100, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x35(z100=10171200, val3=10170010, z101=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z100: OBJ instance ID of the bug key
    val3: Event light ID
    z101: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,2: Event light usage judgment"""
    if (not val3) != 0:
        """State 5: Wait until face SFX playback"""
        assert (GetStateTime() > val4) != 0
        """State 4: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    else:
        """State 1: Event light ON"""
        SetPointLightEnabled(val3, 1, z101)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_17_x36(z100=10171200, val3=10170010, z101=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z100: OBJ instance ID of the bug key
    val3: Event light ID
    z101: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_17_x33(z100=z100, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_17_x34(z100=z100)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_17_x35(z100=z100, val3=val3, z101=z101, val4=val4)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_17_x37(z98=10173250, z99=117020170):
    """[Lib] OBJ Pledge: First move
    z98: OBJ instance ID
    z99: During menu operation: Area and other flags
    """
    """State 0,10: OBJ: Pledge: Initialization"""
    SetEventFlag(z99, 0)
    """State 1: OBJ: Pledge: Start"""
    SetObjSync(z98, 0)
    IsPlayerInTheMap(8, 1, 0)
    CompareEventFlag(8, z99, 0)
    assert ConditionGroup(8)
    """State 2: OBJ: Pledge: Net multiplayer judgment"""
    if IsGuest() != 0:
        """State 3: OBJ: Pledge: Hide"""
        ChangeOwnObjState(10)
        CompareObjState(0, z98, 10, 0)
        assert ConditionGroup(0)
        """State 9: OBJ: Pledge: System: End"""
        EndMachine()
        Quit()
    else:
        """State 4: OBJ: Pledge: Display"""
        ChangeOwnObjState(30)
        CompareObjState(0, z98, 30, 0)
        assert ConditionGroup(0)
        """State 5: OBJ: Pledge: Start: Wait"""
        IsObjSearched(0, z98)
        assert ConditionGroup(0)
        """State 7: OBJ: Pledge: Launch"""
        SetEventFlag(z99, 1)
        CompareEventFlag(0, z99, 1)
        assert ConditionGroup(0)
        """State 8: OBJ: Pledge: Menu running: Wait"""
        CompareEventFlag(0, z99, 0)
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

def event_m10_17_x38(z93=_, z94=20, z95=_, z96=_, z97=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z93: Object instance ID
    z94: OBJ state ID
    z95: Navimesh switching point ID
    z96: Additional attributes
    z97: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_17_x39(z93=z93, z94=z94, z95=z95, z97=z97, z96=z96)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_17_x40(z93=z93, z94=z94, z95=z95)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_17_x41(z93=z93, z94=z94, z95=z95, z96=z96, z97=z97)
    """State 4: End state"""
    return 0

def event_m10_17_x39(z93=_, z94=20, z95=_, z97=_, z96=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z93: Target OBJ instance ID
    z94: Target OBJ state ID
    z95: Navimesh switching point ID
    z97: Additional attributes
    z96: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z93, z94, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z95, z97)
        DeleteNavimeshAttribute(z95, z96)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_17_x40(z93=_, z94=20, z95=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z93: Target OBJ instance ID
    z94: Target OBJ state ID
    z95: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z93, z94, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x41(z93=_, z94=20, z95=_, z96=_, z97=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z93: Target OBJ instance ID
    z94: Target OBJ state ID
    z95: Navimesh switching point ID
    z96: Additional attributes
    z97: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z95, z96)
    DeleteNavimeshAttribute(z95, z97)
    """State 2: End state"""
    return 0

def event_m10_17_x42():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x43(z86=403000, z87=10173100, z89=70, z90=80):
    """[Lib] [Condition] Elevator_Connection replacement
    z86: Replacement point
    z87: OBJ instance ID of the elevator
    z89: Top_Hit group ID
    z90: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z86, z86, 1)
    CompareObjState(8, z87, 70, 0)
    IsPlayerInsidePoint(9, z86, z86, 1)
    CompareObjState(9, z87, 80, 0)
    IsPlayerOnHitGroup(0, z89, 1)
    IsPlayerOnHitGroup(1, z90, 1)
    if ConditionGroup(8):
        """State 2: Ascent point intrusion"""
        return 0
    elif ConditionGroup(9):
        """State 3: Point entry while descending"""
        return 1
    elif ConditionGroup(0):
        """State 4: Be on top"""
        return 2
    elif ConditionGroup(1):
        """State 5: Be down"""
        return 3

def event_m10_17_x44(z86=403000, z88=105420, z91=1, z89=70, z87=10173100):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z86: Replacement point
    z88: Global flag for connection
    z91: ON / OFF of global flag
    z89: Top_Hit group ID
    z87: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z88, z91)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z86, z86, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z89, 1)
    IsPlayerInsidePoint(8, z86, z86, 1)
    CompareObjState(8, z87, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_17_x45(z88=105420, z91=1, z89=70, z86=403000, z87=10173100):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z88: Global flag for connection
    z91: ON / OFF of global flag
    z89: Hit group ID
    z86: Replacement point ID
    z87: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z88, z91)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z89, 0)
    IsPlayerInsidePoint(8, z86, z86, 1)
    CompareObjState(8, z87, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x46(z86=403000, z87=10173100, z88=105420, z89=70, z90=80, z91=1, z92=0):
    """[Lib] [Preset] Elevator_Connection replacement
    z86: Replacement point
    z87: OBJ instance ID of the elevator
    z88: Global flag for connection
    z89: Top_Hit group ID
    z90: Bottom_Hit group ID
    z91: Up_Global flag when rising
    z92: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m10_17_x42()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m10_17_x43(z86=z86, z87=z87, z89=z89, z90=z90)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m10_17_x44(z86=z86, z88=z88, z91=z91, z89=z89, z87=z87)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m10_17_x48(z86=z86, z88=z88, z92=z92, z90=z90, z87=z87)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m10_17_x45(z88=z88, z91=z91, z89=z89, z86=z86, z87=z87)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m10_17_x47(z88=z88, z92=z92, z90=z90, z86=z86, z87=z87)
    """State 7: End state"""
    return 0

def event_m10_17_x47(z88=105420, z92=0, z90=80, z86=403000, z87=10173100):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z88: Global flag for connection
    z92: ON / OFF of global flag
    z90: Hit group ID
    z86: Replacement point ID
    z87: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z88, z92)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z90, 0)
    IsPlayerInsidePoint(8, z86, z86, 1)
    CompareObjState(8, z87, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x48(z86=403000, z88=105420, z92=0, z90=80, z87=10173100):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z86: Replacement point
    z88: Global flag for connection
    z92: ON / OFF of global flag
    z90: Bottom_Hit group ID
    z87: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z88, z92)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z86, z86, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z90, 1)
    IsPlayerInsidePoint(8, z86, z86, 1)
    CompareObjState(8, z87, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_17_x49(z81=10173100, z82=400010):
    """[Execution] Elevator_Return switch after lift
    z81: Elevator OBJ instance ID
    z82: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z81, 30, 0)
    IsPlayerInsidePoint(8, z82, z82, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z81, 71)
    assert CompareObjStateId(z81, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_17_x50(z81=10173100, z83=400000):
    """[Execution] Elevator_Return switch after descending
    z81: Elevator OBJ instance ID
    z83: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z81, 41, 0)
    IsPlayerInsidePoint(8, z83, z83, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z81, 81)
    assert CompareObjStateId(z81, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_17_x51(z80=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z80: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z80)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_17_x52():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x53(z78=_, z79=_):
    """[Lib] [execute] Rebirth fire
    z78: Flag start ID
    z79: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z78, z79, 0)
    """State 2: End state"""
    return 0

def event_m10_17_x54():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x55(z78=_, z79=_):
    """[Lib] [Preset] Rebirth
    z78: Flag start ID
    z79: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_17_x52()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_17_x54()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_17_x53(z78=z78, z79=z79)
    """State 4: End state"""
    return 0

def event_m10_17_x56(flag7=_, z77=_):
    """[Lib] [Preset] Get trophy
    flag7: Acquisition trigger_other flags
    z77: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag7) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag7, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z77)
    """State 4: End state"""
    return 0

def event_m10_17_x57():
    """[Lib] [Reproduction] Switch the connection flag at the point"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_17_x58(z72=405000, z73=405000):
    """[Lib] [Condition] Switch the connection flag at the point
    z72: Start point ID
    z73: End point ID
    """
    """State 0,1: Are you in point?"""
    IsPlayerInsidePoint(0, z72, z73, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x59(z74=105420, z75=0, z76=1):
    """[Lib] [Execution] Switch to the connection flag at the point
    z74: Global event flag for connection
    z75: Flag switching
    z76: Wait for next judgment
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z74, z75)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z74, z75)
    assert ConditionGroup(0)
    """State 3: For next judgment: Has the flag changed?"""
    CompareEventFlag(0, z74, z76)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_17_x60(z72=405000, z73=405000, z74=105420, z75=0, z76=1):
    """[Lib] [Preset] Switch the connection flag at the point
    z72: Start point ID
    z73: End point ID
    z74: Global event flag for connection
    z75: Flag switching
    z76: Wait for next judgment
    """
    """State 0,1: [Lib] [Reproduction] Switch the connection flag at the point _SubState"""
    call = event_m10_17_x57()
    if call.Get() == 0:
        """State 3: [Lib] [Condition] Switch connection flag at point _SubState"""
        assert event_m10_17_x58(z72=z72, z73=z73)
        """State 2: [Lib] [Execution] Switch to the connection flag at the point _SubState"""
        assert event_m10_17_x59(z74=z74, z75=z75, z76=z76)
        """State 4: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 5: Guest: Exit"""
        return 1

def event_m10_17_x61(flag4=117020001, flag5=117000002):
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

def event_m10_17_x62(z60=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z60: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z60, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_17_x63(flag4=117020001, z61=6, z62=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag4: Lottery determination flag
    z61: Number of appearance judgment points
    z62: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag4, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z61)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z62, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_17_x64(flag4=117020001, z60=14, flag5=117000002, z61=6, z62=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag4: Lottery determination flag
    z60: Random number comparison value
    flag5: Defeat flag
    z61: Number of appearance judgment points
    z62: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_17_x61(flag4=flag4, flag5=flag5)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_17_x62(z60=z60)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_17_x63(flag4=flag4, z61=z61, z62=z62)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_17_x73(flag4=flag4, z62=z62)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_17_x65(val2=_, z69=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z69: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z69) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_17_x66(z65=_, z66=0, z67=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z65: Appearance judgment point ID
    z66: Minimum appearance time
    z67: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z65, z65, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z66, 3, z67)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_17_x67(z68=935, z70=_, z71=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z68: Generator ID
    z70: Appearance start point ID
    z71: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z68, z70, z71)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z68)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m10_17_x68(flag6=117000002):
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

def event_m10_17_x69(z65=_, z66=0, z67=5, z68=935, val2=_, z69=10, z70=_, z71=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z65: Intrusion detection point ID
    z66: Minimum appearance time
    z67: Maximum time to appear
    z68: Generator ID
    val2: Appearance judgment number
    z69: Lottery result point variable
    z70: Appearance start point ID
    z71: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_17_x65(val2=val2, z69=z69)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_17_x66(z65=z65, z66=z66, z67=z67)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_17_x67(z68=z68, z70=z70, z71=z71)
    """State 4: Finish"""
    return 0

def event_m10_17_x70(z63=935, mode1=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z63: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z63)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_17_x71(flag6=117000002, z64=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag6: Defeat flag
    z64: Weapon flag
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
                    SetEventFlag(z64, 1)
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

def event_m10_17_x72(flag6=117000002, z63=935, mode1=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag6: Defeat flag
    z63: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_17_x68(flag6=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_17_x70(z63=z63, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_17_x71(flag6=flag6, z64=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_17_x71(flag6=flag6, z64=102755)
    """State 5: End state"""
    return 0

def event_m10_17_x73(flag4=117020001, z62=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag4: Lottery determination flag
    z62: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag4, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z62, 0)
    """State 3: End state"""
    return 0

def event_m10_17_x74(flag3=117000091):
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

def event_m10_17_x75(z58=801):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z58: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z58, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x76(z59=117020092):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z59: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z59, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x77(flag3=117000091, z58=801, z59=117020092):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag3: Boss destruction flag
    z58: Boss generator ID
    z59: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_17_x74(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_17_x75(z58=z58)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_17_x76(z59=z59)
    """State 4: End state"""
    return 0

def event_m10_17_x78():
    """[Reproduction] Gate opened with lever"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x79(z57=10172013):
    """[Condition] Gate opened by lever
    z57: Lever OBJ object instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z57, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x80(z56=100000):
    """[Execution] Gate opened by lever
    z56: Navigation mesh change
    """
    """State 0,1: Gate animation opening with lever"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(30, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z56, 2)
    """State 3: End state"""
    return 0

def event_m10_17_x81(z53=10172130, z54=10171530, z55=3201000):
    """[Reproduction] Suspended ceiling
    z53: Lever instance ID
    z54: Ceiling instance ID
    z55: Damage area ID
    """
    """State 0,5: [SEQ26778] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 3: Is the ceiling in the initial state?"""
    if CompareObjStateId(z54, 10, 1):
        """State 4: Initializing the ceiling"""
        InitializeObj(z54)
    else:
        pass
    """State 2: Damage invalid"""
    EnableDamageArea(z55, 0)
    """State 1: Activate key guide"""
    DisableObjKeyGuide(z53, 0)
    """State 6: End state"""
    return 0

def event_m10_17_x82(z53=10172130):
    """[Conditions] Suspended ceiling
    z53: Lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z53, 74, 0)
    CompareObjState(0, z53, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x83(z54=10171530, z55=3201000, val1=7, z53=10172130):
    """[Execution] suspended ceiling
    z54: Suspended ceiling instance ID
    z55: Damage area ID
    val1: Fall waiting time
    z53: Lever instance ID
    """
    """State 0,6: Disable key guide"""
    DisableObjKeyGuide(z53, 1)
    """State 1: OBJ state transition: suspended ceiling"""
    ChangeObjState(z54, 70)
    """State 2: Wait for descent start"""
    CompareObjState(0, z54, 71, 0)
    assert ConditionGroup(0)
    """State 5: Time lapse state"""
    assert (GetStateTime() > val1) != 0
    """State 3: Activate damage"""
    EnableDamageArea(z55, 1)
    """State 4: Wait for descent completion"""
    CompareObjState(0, z54, 10, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m10_17_x84(z53=10172130, z54=10171530, z55=3201000, val1=7):
    """[Preset] Suspended ceiling
    z53: Lever instance ID
    z54: Suspended ceiling instance ID
    z55: Damage area ID
    val1: Fall waiting time
    """
    """State 0,1: [Reproduction] Suspended ceiling_SubState"""
    assert event_m10_17_x81(z53=z53, z54=z54, z55=z55)
    """State 2: [Condition] Suspended ceiling_SubState"""
    assert event_m10_17_x82(z53=z53)
    """State 3: [Execution] Suspended ceiling_SubState"""
    assert event_m10_17_x83(z54=z54, z55=z55, val1=val1, z53=z53)
    """State 4: End state"""
    return 0

def event_m10_17_x85(z16=10171540, z15=10172110, z14=500000):
    """[Reproduction] Iron lattice that can be opened and closed by levers
    z16: OBJ instance ID of the bar
    z15: OBJ instance ID of the lever
    z14: Navigation change point ID
    """
    """State 0,1: Is the iron lattice in anime?"""
    if CompareObjStateId(z16, 70, 0):
        """State 2: Disabling the key guide of the lever"""
        DisableObjKeyGuide(z15, 1)
        """State 4: Waiting for the rise of the iron lattice"""
        assert CompareObjStateId(z16, 30, 0)
        """State 3: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z14, 2)
        """State 5: Enable key guide for lever"""
        DisableObjKeyGuide(z15, 0)
    elif CompareObjStateId(z16, 80, 0):
        """State 6: Disabling the key guide for the lever_2"""
        DisableObjKeyGuide(z15, 1)
        """State 8: Waiting for the descent of the iron grid"""
        assert CompareObjStateId(z16, 10, 0)
        """State 7: Navimesh attribute added"""
        AddNavimeshAttribute(z14, 2)
        """State 9: Lever key guide activation_2"""
        DisableObjKeyGuide(z15, 0)
    else:
        """State 10: State determination of iron grid"""
        if CompareObjStateId(z16, 30, 0):
            """State 11: Navimesh attribute deletion_2"""
            DeleteNavimeshAttribute(z14, 2)
        elif CompareObjStateId(z16, 10, 0):
            """State 12: Navimesh attribute added_2"""
            AddNavimeshAttribute(z14, 2)
    """State 13: End state"""
    return 0

def event_m10_17_x86(z15=10172110, z17=10172900, z16=10171540):
    """[Conditions] Iron lattice that can be opened and closed by levers
    z15: Wall hole lever OBJ instance ID
    z17: OBJ instance ID for enemy judgment
    z16: Iron lattice OBJ instance ID
    """
    """State 0,1: Lever operation or enemy starts"""
    CompareObjState(0, z15, 74, 0)
    CompareObjState(0, z15, 84, 0)
    IsObjDamaged(0, z17, -1, 4000, 112400010)
    IsObjDamaged(0, z17, -1, 4000, 112401010)
    IsObjDamaged(0, z17, -1, 4000, 112402010)
    assert ConditionGroup(0)
    """State 2: State determination of iron grid"""
    CompareObjState(0, z16, 10, 0)
    CompareObjState(1, z16, 30, 0)
    if ConditionGroup(0):
        """State 3: The iron grid is down"""
        return 0
    elif ConditionGroup(1):
        """State 4: The iron grid is up"""
        return 1

def event_m10_17_x87(z14=500000, z15=10172110, z16=10171540):
    """[Execution] Iron lattice that can be opened and closed with a lever
    z14: Navigation change point ID
    z15: Lever OBJ instance ID
    z16: Iron lattice OBJ instance ID
    """
    """State 0,3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z15, 1)
    """State 1: Iron lattice rise animation playback: 70"""
    ChangeObjState(z16, 70)
    """State 4: Waiting for the rise of the iron lattice"""
    CompareObjState(0, z16, 30, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z14, 2)
    """State 5: Enable key guide for lever"""
    DisableObjKeyGuide(z15, 0)
    """State 6: End state"""
    return 0

def event_m10_17_x88():
    """[Reproduction] Suspended poisonous _ operation"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x89(z50=_):
    """[Conditions] Hanging poisonous jars in operation
    z50: OBJ instance ID of the lever
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z50, 74, 0)
    CompareObjState(0, z50, 84, 0)
    assert ConditionGroup(0)
    """State 3: Disable key guide"""
    DisableObjKeyGuide(z50, 1)
    """State 2: Chain status judgment"""
    if CompareOwnObjStateId(10, 0):
        """State 4: Under"""
        return 0
    elif CompareOwnObjStateId(30, 0):
        """State 5: It is above"""
        return 1

def event_m10_17_x90(z51=_, z52=_, z50=_):
    """[Execution] Hanging Poisonous _ Operation
    z51: OBJ state ID in operation
    z52: OBJ state ID after operation
    z50: OBJ instance ID of the lever
    """
    """State 0,1: Chain OBJ animation playback"""
    ChangeOwnObjState(z51)
    assert CompareOwnObjStateId(z52, 0)
    """State 2: End of lever animation"""
    CompareObjState(0, z50, 10, 0)
    CompareObjState(0, z50, 30, 0)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z50, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x91(z50=_):
    """[Preset] Suspended poisonous _ operation
    z50: OBJ instance ID of the lever
    """
    """State 0,1: [Reproduction] Hanging poisonous lever _SubState"""
    assert event_m10_17_x88()
    """State 3: [Condition] Lung poison lever _SubState"""
    call = event_m10_17_x89(z50=z50)
    if call.Get() == 0:
        """State 2: [Execution] Hung poison poison lever _SubState"""
        assert event_m10_17_x90(z51=70, z52=30, z50=z50)
    elif call.Get() == 1:
        """State 4: [Execution] Lung Poison Lever_2_SubState"""
        assert event_m10_17_x90(z51=80, z52=10, z50=z50)
    """State 5: End state"""
    return 0

def event_m10_17_x92(z47=10171500, z48=117000055, z49=117000056):
    """[Reproduction] Giant windmill
    z47: Huge windmill instance ID
    z48: Windmill burned flag
    z49: Windmill burning start flag
    """
    """State 0,1: Wind turbine OBJ status judgment"""
    if CompareObjStateId(z47, 20, 0):
        """State 3: [DC] Windmill burning start flag ON"""
        Label('L0')
        SetEventFlag(z49, 1)
        """State 2: Burned flag set"""
        SetEventFlag(z48, 1)
        """State 5: End state"""
        return 1
    elif CompareObjStateId(z47, 51, 0):
        Goto('L0')
    else:
        """State 4: [Condition] To giant windmill"""
        return 0

def event_m10_17_x93(z46=10171500):
    """[Condition] Giant windmill
    z46: Huge windmill instance ID
    """
    """State 0,5: Judgment of state of giant windmill"""
    if CompareObjStateId(z46, 30, 0):
        """State 1: With key guide"""
        Label('L0')
        CompareObjState(0, z46, 20, 0)
        CompareObjState(0, z46, 50, 0)
        IsPlayerUsingTorch(8, 0)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Transition to no key guide: 10"""
            ChangeObjState(z46, 10)
            CompareObjState(0, z46, 30, 1)
            assert ConditionGroup(0)
            """State 6: To redo"""
            return 0
    else:
        """State 2: Without key guide"""
        CompareObjState(0, z46, 20, 0)
        CompareObjState(0, z46, 50, 0)
        IsPlayerUsingTorch(8, 1)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 4: Transition to key guide existence: 30"""
            ChangeObjState(z46, 30)
            Goto('L0')
    """State 7: [Execution] To giant windmill"""
    return 1

def event_m10_17_x94(z38=10171500, z39=10171501, z40=10171502, z41=10171503, z42=10171504, z43=117000055,
                     z44=10171505, z45=117000056):
    """[Execution] Giant windmill
    z38: Huge windmill instance ID
    z39: Instance ID of giant windmill wing 1
    z40: Instance ID of giant windmill wing 2
    z41: Instance ID of giant windmill wing 3
    z42: Instance ID of Giant Windmill Wing 4
    z43: Windmill burned flag
    z44: OBJ instance ID of center feather
    z45: Windmill burning start flag
    """
    """State 0,3: [DC] Windmill burning start flag ON"""
    SetEventFlag(z45, 1)
    """State 1: on fire"""
    ChangeObjState(z39, 70)
    ChangeObjState(z40, 70)
    ChangeObjState(z41, 70)
    ChangeObjState(z42, 70)
    ChangeObjState(z44, 70)
    assert CompareObjStateId(z38, 51, 0)
    """State 2: Windmill burning flag ON"""
    SetEventFlag(z43, 1)
    """State 4: End state"""
    return 0

def event_m10_17_x95(z36=_, z37=_):
    """[Preset] Workers released from dead dead
    z36: The instance ID of the bag containing the worker
    z37: Worker release flag of dead dead in cage
    """
    """State 0,1: [Reproduction] Liberation of dead workers in cages_SubState"""
    assert event_m10_17_x96()
    """State 2: [Conditions] Liberation of dead workers in cages_SubState"""
    assert event_m10_17_x97(z36=z36)
    """State 3: [Execution] Liberation of dead workers in cages_SubState"""
    assert event_m10_17_x98(z37=z37)
    """State 4: End state"""
    return 0

def event_m10_17_x96():
    """[Reproduction] Liberation of dead workers in cages"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x97(z36=_):
    """[Conditions] Liberation of dead workers in cages
    z36: The instance ID of the bag containing the worker
    """
    """State 0,1: Was the cage containing the workers destroyed?"""
    assert CompareObjStateId(z36, 20, 0)
    """State 2: End state"""
    return 0

def event_m10_17_x98(z37=_):
    """[Execution] Liberation of dead workers in cages
    z37: Worker release flag of dead dead in cage
    """
    """State 0,1: Raise a worker release flag for the dead dead"""
    SetEventFlag(z37, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x99(z28=10171205, z29=10171310, z30=10171315, z31=90, z32=240, z33=1, z34=2, z35=117000055):
    """[Preset] [Insect Key] Recovery Fountain _ Poisonous
    z28: Bug ID OBJ instance ID
    z29: Instance ID of Recovery OBJ
    z30: Poison water OBJ instance ID
    z31: Hit group ID
    z32: Grand material ID
    z33: Grand material slot_poisonous water
    z34: Grand Material Slot_Recovery
    z35: Windmill burned flag
    """
    """State 0,1: [Reproduction] [Insect Key] Recovery Fountain_Poisonous_SubState"""
    call = event_m10_17_x100(z28=z28, z29=z29, z30=z30, z31=z31, z32=z32, z33=z33, z34=z34, z35=z35)
    if call.Get() == 0:
        """State 2: [Condition] [Insect Key] Recovery Fountain_Poisonous_SubState"""
        call = event_m10_17_x101(z28=z28, z35=z35)
        if call.Get() == 0:
            """State 3: [Execute] [Insect Key] Recovery Fountain_Poisonous_Recovery_SubState"""
            Label('L0')
            assert event_m10_17_x102(z29=z29, z31=z31, z32=z32, z34=z34)
        elif call.Get() == 1:
            """State 4: [Execute] [Insect Key] Recovery Fountain _ Poisonous _ Poison water not activated _SubState"""
            assert event_m10_17_x103(z30=z30, z31=z31, z32=z32, z33=z33, z35=z35)
            Goto('L0')
    elif call.Get() == 2:
        """State 5: [Execution] [Insect Key] Recovery Fountain_Poisonous_Poison Water Activated_SubState"""
        assert event_m10_17_x104(z30=z30, z31=z31, z32=z32, z33=z33, z35=z35)
        Goto('L0')
    elif call.Get() == 1:
        pass
    """State 6: End state"""
    return 0

def event_m10_17_x100(z28=10171205, z29=10171310, z30=10171315, z31=90, z32=240, z33=1, z34=2, z35=117000055):
    """[Reproduction] [Insect Key] Recovery Fountain _ Poisonous
    z28: Bug ID OBJ instance ID
    z29: Instance ID of Recovery OBJ
    z30: Poison water OBJ instance ID
    z31: Hit group ID
    z32: Grand material ID
    z33: Grand material slot_poisonous water
    z34: Grand Material Slot_Recovery
    z35: Windmill burned flag
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z28, 20, 0):
        pass
    else:
        Goto('L1')
    """State 2: Did you remove the poison?"""
    if CompareObjStateId(z30, 20, 0):
        pass
    elif CompareObjStateId(z30, 71, 0):
        pass
    else:
        Goto('L0')
    """State 7: Has water already accumulated?"""
    if CompareObjStateId(z29, 20, 0):
        pass
    else:
        """State 4: Reserving water: 70"""
        ChangeObjState(z29, 70)
        """State 8: Waiting for accumulation"""
        assert CompareObjStateId(z29, 20, 0)
    """State 6: Enable grand material recovery"""
    SetGroundMaterial(z31, z32, z34)
    """State 12: Started: Recovery"""
    return 1
    """State 9: Has poison water already accumulated?"""
    Label('L0')
    if CompareObjStateId(z30, 30, 0):
        pass
    else:
        """State 3: Accumulate poisonous water: 70"""
        ChangeObjState(z30, 70)
        """State 10: Puddle waiting_2"""
        assert CompareObjStateId(z30, 30, 0)
    """State 5: Activate poison water of Grand Material"""
    SetGroundMaterial(z31, z32, z33)
    """State 13: Activated: Poison water"""
    return 2
    """State 11: Not started"""
    Label('L1')
    return 0

def event_m10_17_x101(z28=10171205, z35=117000055):
    """[Condition] [Insect Key] Recovery Fountain _ Poisonous
    z28: Bug ID OBJ instance ID
    z35: Windmill burned flag
    """
    """State 0,2: Waiting for insect key activation"""
    CompareObjState(0, z28, 20, 0)
    assert ConditionGroup(0)
    """State 1: Did you remove the poison?"""
    CompareEventFlag(0, z35, 1)
    if ConditionGroup(0):
        """State 3: Bug key activation: recovery"""
        return 0
    else:
        """State 4: Bug key activation: poisonous water"""
        return 1

def event_m10_17_x102(z29=10171310, z31=90, z32=240, z34=2):
    """[Execute] [Insect Key] Recovery Fountain_Poisoned_Recovery
    z29: Instance ID of Recovery OBJ
    z31: Hit group ID
    z32: Grand material ID
    z34: Grand material slot
    """
    """State 0,1: Recovery fountain launch"""
    ChangeObjState(z29, 70)
    assert (GetStateTime() > 1) != 0
    """State 2: Enable grand material recovery"""
    SetGroundMaterial(z31, z32, z34)
    """State 3: Waiting for the end of anime"""
    assert CompareObjStateId(z29, 20, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x103(z30=10171315, z31=90, z32=240, z33=1, z35=117000055):
    """[Execute] [Insect Key] Recovery Fountain _ Poisonous _ Poison water not activated
    z30: Poison water OBJ instance ID
    z31: Hit group ID
    z32: Grand material ID
    z33: Grand material slot
    z35: Windmill burned flag
    """
    """State 0,1: Poison water fountain start"""
    ChangeObjState(z30, 70)
    assert (GetStateTime() > 1) != 0
    """State 2: Activate poison water of Grand Material"""
    SetGroundMaterial(z31, z32, z33)
    """State 3: Wait for poison removal"""
    CompareEventFlag(0, z35, 1)
    assert ConditionGroup(0)
    """State 4: Poison water fountain stop"""
    ChangeObjState(z30, 71)
    assert (GetStateTime() > 1) != 0
    """State 5: Disable ground material poison water"""
    SetGroundMaterial(z31, z32, z33)
    """State 6: Waiting for the end of the poisonous water anime"""
    assert CompareObjStateId(z30, 20, 0)
    """State 7: End state"""
    return 0

def event_m10_17_x104(z30=10171315, z31=90, z32=240, z33=1, z35=117000055):
    """[Execution] [Insect Key] Recovery Fountain _ Poisonous _ Poison water activated
    z30: Poison water OBJ instance ID
    z31: Hit group ID
    z32: Grand material ID
    z33: Grand material slot
    z35: Windmill burned flag
    """
    """State 0,1: Wait for poison removal"""
    CompareEventFlag(0, z35, 1)
    assert ConditionGroup(0)
    """State 2: Poison water fountain stop"""
    ChangeObjState(z30, 71)
    assert (GetStateTime() > 1) != 0
    """State 3: Disable ground material poison water"""
    SetGroundMaterial(z31, z32, z33)
    """State 4: Waiting for the end of the poisonous water anime"""
    assert CompareObjStateId(z30, 20, 0)
    """State 5: End state"""
    return 0

def event_m10_17_x105(z20=147005, z21=311000, z22=200010010, z23=200010020, z24=200010030, z25=200010011,
                      z26=200010021, z27=200010031):
    """[Preset] Enemy character's poison fog damage disabled
    z20: Character ID of sick person
    z21: Knight soldier: Character ID of a riding soldier
    z22: Poison fog (weak) damage ID
    z23: Poison fog (medium) damage ID
    z24: Poison fog (strong) damage ID
    z25: Poison fog (weak) production damage ID
    z26: Poison fog (medium) production damage ID
    z27: Poison fog (strong) production damage ID
    """
    """State 0,1: [Reproduce] Enemy character's poison fog damage disabled_SubState"""
    assert event_m10_17_x106()
    """State 2: [Condition] Enemy character's poison fog damage disabled_SubState"""
    assert event_m10_17_x107()
    """State 3: [Execute] Enemy character's poison fog damage disabled_SubState"""
    assert event_m10_17_x108(z20=z20, z21=z21, z22=z22, z23=z23, z24=z24, z25=z25, z26=z26, z27=z27)
    """State 4: End state"""
    return 0

def event_m10_17_x106():
    """[Reproduction] Enemy character's poison fog damage invalidation"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x107():
    """[Condition] Invalidate poison fog damage of enemy characters"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x108(z20=147005, z21=311000, z22=200010010, z23=200010020, z24=200010030, z25=200010011,
                      z26=200010021, z27=200010031):
    """[Execution] Disabling poison mist damage of enemy characters
    z20: Character ID of sick person
    z21: Knight soldier: Character ID of a riding soldier
    z22: Poison fog (weak) damage ID
    z23: Poison fog (medium) damage ID
    z24: Poison fog (strong) damage ID
    z25: Poison fog (weak) production damage ID
    z26: Poison fog (medium) production damage ID
    z27: Poison fog (strong) production damage ID
    """
    """State 0,1: Disabling poison fog damage"""
    SetDamageImmunityByCharacterId(z20, z22, 1)
    SetDamageImmunityByCharacterId(z20, z23, 1)
    SetDamageImmunityByCharacterId(z20, z24, 1)
    SetDamageImmunityByCharacterId(z21, z22, 1)
    SetDamageImmunityByCharacterId(z21, z23, 1)
    SetDamageImmunityByCharacterId(z21, z24, 1)
    SetDamageImmunityByCharacterId(z20, z25, 1)
    SetDamageImmunityByCharacterId(z20, z26, 1)
    SetDamageImmunityByCharacterId(z20, z27, 1)
    SetDamageImmunityByCharacterId(z21, z25, 1)
    SetDamageImmunityByCharacterId(z21, z26, 1)
    SetDamageImmunityByCharacterId(z21, z27, 1)
    SetDamageImmunityByGeneratorId(5110, 200014020, 1)
    SetDamageImmunityByGeneratorId(5110, 200014030, 1)
    SetDamageImmunityByCharacterId(z20, 200014020, 1)
    SetDamageImmunityByCharacterId(z20, 200014030, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x109():
    """[Reproduction] Floor switch arrow"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x110(z19=_):
    """[Condition] Floor switch tapping arrow
    z19: Switch instance ID
    """
    """State 0,1: Did you get on the switch?"""
    CompareObjState(0, z19, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x111(z18=_):
    """[Execution] Floor switch treadle
    z18: OBJ instance ID to be run
    """
    """State 0,1: Arrow firing: 70"""
    ChangeObjState(z18, 70)
    """State 2: End state"""
    return 0

def event_m10_17_x112(z18=_, z19=_):
    """[Preset] Floor switch arrow
    z18: OBJ instance ID to be run
    z19: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Floor switch treadle _SubState"""
    assert event_m10_17_x109()
    """State 3: [Condition] Floor switch tread arrow _SubState"""
    assert event_m10_17_x110(z19=z19)
    """State 2: [Execution] Floor switch treadle_SubState"""
    assert event_m10_17_x111(z18=z18)
    """State 4: End state"""
    return 0

def event_m10_17_x113(z14=500000, z15=10172110, z16=10171540):
    """[Execution] Iron lattice that can be opened and closed by lever
    z14: Navigation change point ID
    z15: Lever OBJ instance ID
    z16: Iron lattice OBJ instance ID
    """
    """State 0,3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z15, 1)
    """State 1: Iron lattice descending animation playback: 80"""
    ChangeObjState(z16, 80)
    """State 4: Waiting for the descent of the iron grid"""
    CompareObjState(0, z16, 10, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute added"""
    AddNavimeshAttribute(z14, 2)
    """State 5: Enable key guide for lever"""
    DisableObjKeyGuide(z15, 0)
    """State 6: End state"""
    return 0

def event_m10_17_x114(z14=500000, z15=10172110, z16=10171540, z17=10172900):
    """[Preset] Iron lattice that can be opened and closed by levers
    z14: Navigation change point ID
    z15: Lever OBJ instance ID
    z16: Iron lattice OBJ instance ID
    z17: OBJ instance ID for enemy judgment
    """
    """State 0,1: [Reproduction] Iron lattice _SubState that can open and close the enemy with a lever"""
    assert event_m10_17_x85(z16=z16, z15=z15, z14=z14)
    """State 4: [Condition] Iron lattice that can be opened and closed by lever"""
    call = event_m10_17_x86(z15=z15, z17=z17, z16=z16)
    if call.Get() == 0:
        """State 3: [Execution] Iron lattice that can be opened and closed by lever"""
        assert event_m10_17_x87(z14=z14, z15=z15, z16=z16)
    elif call.Get() == 1:
        """State 2: [Execution] Iron lattice that can be opened and closed with a lever_Descent_SubState"""
        assert event_m10_17_x113(z14=z14, z15=z15, z16=z16)
    """State 5: Rerun"""
    return 0

def event_m10_17_x115(z9=10173000, z10=10173001, z11=10173002, z12=10173003, z13=10173004, flag2=117000055):
    """[Reproduction] Poison water drop
    z9: Poison water OBJ instance ID_1
    z10: Poison water OBJ instance ID_2
    z11: Poison water OBJ instance ID_3
    z12: Poison water OBJ instance ID_4
    z13: Poison water OBJ instance ID_5
    flag2: Windmill burned flag
    """
    """State 0,1: Is the windmill burning and valve operated?"""
    if GetEventFlag(flag2) != 0:
        """State 2: Poison water status switching"""
        SetGroundMaterial(20, 240, 1)
        SetGroundMaterial(30, 240, 1)
        SetGroundMaterial(40, 240, 1)
        SetGroundMaterial(50, 240, 1)
        SetGroundMaterial(60, 240, 1)
        SetGroundMaterial(21, 240, 1)
        ChangeObjState(z9, 20)
        ChangeObjState(z10, 20)
        ChangeObjState(z11, 20)
        ChangeObjState(z12, 20)
        ChangeObjState(z13, 20)
        """State 4: End of reproduction"""
        return 1
    else:
        """State 3: End state"""
        return 0

def event_m10_17_x116(flag2=117000055):
    """[Condition] Poisonous water drop
    flag2: Windmill burned flag
    """
    """State 0,1: Did the windmill burn?"""
    CompareEventFlag(0, flag2, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x117(z9=10173000, z10=10173001, z11=10173002, z12=10173003, z13=10173004):
    """[Execution] Poison water drop
    z9: Poison water OBJ instance ID_1
    z10: Poison water OBJ instance ID_2
    z11: Poison water OBJ instance ID_3
    z12: Poison water OBJ instance ID_4
    z13: Poison water OBJ instance ID_5
    """
    """State 0,1: OBJ state transition: poison water"""
    ChangeObjState(z9, 70)
    ChangeObjState(z10, 70)
    ChangeObjState(z11, 70)
    ChangeObjState(z12, 70)
    ChangeObjState(z13, 70)
    """State 12: Time elapsed: 2.5 seconds"""
    CompareStateTime(0, 2.5, 2, 2.5)
    assert ConditionGroup(0)
    """State 11: Changed the ground material for Poison Water 5"""
    SetGroundMaterial(40, 240, 1)
    """State 14: Time elapsed: 1 second"""
    CompareStateTime(0, 1, 2, 1)
    assert ConditionGroup(0)
    """State 13: Changed the ground material for Poison Water 2"""
    SetGroundMaterial(30, 240, 1)
    """State 17: Changed the ground material for poisonous water 4 (slope)"""
    SetGroundMaterial(21, 240, 1)
    """State 16: Time elapsed: 1 second_2"""
    CompareStateTime(0, 1, 2, 1)
    assert ConditionGroup(0)
    """State 15: Changed the ground material of Poison Water 1"""
    SetGroundMaterial(60, 240, 1)
    """State 10: Time elapsed: 1/2 second"""
    CompareStateTime(0, 0.5, 2, 0.5)
    assert ConditionGroup(0)
    """State 9: Changed the ground material for Poison Water 4"""
    SetGroundMaterial(20, 240, 1)
    """State 4: Change the state of poison water 1, 2 and 5"""
    ChangeObjState(z9, 20)
    ChangeObjState(z10, 20)
    ChangeObjState(z13, 20)
    """State 8: Time elapsed: 2 seconds and a half_2"""
    CompareStateTime(0, 2.5, 2, 2.5)
    assert ConditionGroup(0)
    """State 7: Changed the ground material for poisonous water 3"""
    SetGroundMaterial(50, 240, 1)
    """State 2: Time elapsed: 2 seconds"""
    CompareStateTime(0, 2, 2, 2)
    assert ConditionGroup(0)
    """State 3: Change the state of poison water 4"""
    ChangeObjState(z12, 20)
    """State 5: Time elapsed: 5 seconds and a half"""
    CompareStateTime(0, 5.5, 2, 5.5)
    assert ConditionGroup(0)
    """State 6: Change the state of Poison Water 3"""
    ChangeObjState(z11, 20)
    """State 18: End state"""
    return 0

def event_m10_17_x118(z9=10173000, z10=10173001, z11=10173002, z12=10173003, z13=10173004, flag2=117000055):
    """[Preset] Poison water drop
    z9: Poison water OBJ instance ID_1
    z10: Poison water OBJ instance ID_2
    z11: Poison water OBJ instance ID_3
    z12: Poison water OBJ instance ID_4
    z13: Poison water OBJ instance ID_5
    flag2: Windmill burned flag
    """
    """State 0,1: [Reproduction] Poison water drop_SubState"""
    call = event_m10_17_x115(z9=z9, z10=z10, z11=z11, z12=z12, z13=z13, flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Poisonous water reduction_SubState"""
        assert event_m10_17_x116(flag2=flag2)
        """State 2: [Execution] Poison water drop_SubState"""
        assert event_m10_17_x117(z9=z9, z10=z10, z11=z11, z12=z12, z13=z13)
    """State 4: End state"""
    return 0

def event_m10_17_x119(z5=100, z6=105440):
    """[Preset] Hunting Forest MAP loading discard
    z5: Judgment hit group ID
    z6: Hunting Forest MAP discard flag
    """
    """State 0,1: [Reproduction] Loading and discarding Hunting Forest MAP_SubState"""
    assert event_m10_17_x120()
    """State 2: [Condition] Reading and discarding Hunting Forest MAP_SubState"""
    call = event_m10_17_x121(z5=z5)
    if call.Get() == 0:
        """State 3: [Execution] Hunting Forest MAP loading discard_flag OFF_SubState"""
        assert event_m10_17_x122(z6=z6, z7=0, z5=z5, z8=0)
    elif call.Get() == 1:
        """State 4: [Execution] Hunting Forest MAP loading discard_flag ON_SubState"""
        assert event_m10_17_x122(z6=z6, z7=1, z5=z5, z8=1)
    """State 5: End state"""
    return 0

def event_m10_17_x120():
    """[Reproduction] Reading and discarding Hunting Forest MAP"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x121(z5=100):
    """[Condition] Reading and discarding Hunting Forest MAP
    z5: Judgment hit group ID
    """
    """State 0,2: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 1: Are you on a hit for judgment?"""
    IsPlayerOnHitGroup(0, z5, 1)
    if ConditionGroup(0):
        """State 3: Flag off"""
        return 0
    else:
        """State 4: Turn on the flag"""
        return 1

def event_m10_17_x122(z6=105440, z7=_, z5=100, z8=_):
    """[Execution] Reading and discarding Hunting Forest MAP
    z6: Hunting Forest MAP discard flag
    z7: Flag ON / OFF
    z5: Judgment hit group ID
    z8: YES / NO for hit judgment
    """
    """State 0,1: Switched flag for discarding hunting forest MAP"""
    SetEventFlag(z6, z7)
    """State 2: Did the condition change condition be met?"""
    IsPlayerInTheMap(0, 0, 0)
    IsPlayerOnHitGroup(0, z5, z8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x123(z2=_, z3=_, z4=_):
    """[BEST] [Preset] Suspended Poison Poison _ Destruction
    z2: Poisonous OBJ instance ID
    z3: Chain OBJ instance ID
    z4: Destruction judgment point ID
    """
    """State 0,1: [BEST] [Reproduction] Hanging Poison _ Destruction _ SubState"""
    call = event_m10_17_x124(z2=z2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [BEST] [Condition] Suspended poison spider_Destruction_SubState"""
        call = event_m10_17_x126(z2=z2, z3=z3, z4=z4)
        if call.Get() == 1:
            pass
        elif call.Get() == 2:
            """State 5: Rerun"""
            return 1
        elif call.Get() == 0:
            """State 3: [BEST] [Execution] Suspended Poison Spider_Destruction_SubState"""
            assert event_m10_17_x125(z2=z2)
    """State 4: Finish"""
    return 0

def event_m10_17_x124(z2=_):
    """[BEST] [Reproduction] Suspended poison _ destruction
    z2: Poisonous OBJ instance ID
    """
    """State 0,1: Is the cocoon already broken?"""
    if CompareObjStateId(z2, 10, 1):
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Before destruction"""
        return 0

def event_m10_17_x125(z2=_):
    """[BEST] [Execution] Hanging Poison 壺 Destruction
    z2: Poisonous OBJ instance ID
    """
    """State 0,1: Hail destruction"""
    DestroyObj(z2, z2, 0)
    """State 2: Finish"""
    return 0

def event_m10_17_x126(z2=_, z3=_, z4=_):
    """[BEST] [Condition] Suspended poison spider _ destruction
    z2: Poisonous OBJ instance ID
    z3: Chain OBJ instance ID
    z4: Destruction judgment point ID
    """
    """State 0,1: Is the chain descending?"""
    CompareObjState(0, z3, 80, 0)
    CompareObjState(0, z2, 10, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4: Destroyed"""
    return 1
    """State 2: Is the player down while descending?"""
    Label('L0')
    CompareStateTime(8, 1.5, 3, 1.5)
    IsPlayerInsidePoint(8, z4, z4, 1)
    CompareObjState(0, z3, 10, 0)
    if ConditionGroup(0):
        """State 5: Rerun"""
        return 2
    elif ConditionGroup(8):
        """State 3: Destroy the spear"""
        return 0

def event_m10_17_x127(flag1=100790):
    """[DC] [Execution] Judgment White Spirit Summon Achievement Judgment
    flag1: Summon achievement flag
    """
    """State 0,1: Summon achievement flag ON"""
    SetEventFlag(flag1, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x128(z1=600):
    """[DC] [Conditions] Judgment achievement of guided white spirit
    z1: White Spirit Generator ID
    """
    """State 0,1: Was the white spirit summoned?"""
    IsChrActive(0, z1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x129(flag1=100790):
    """[DC] [Reproduction] Judgment White Spirit Summoning Achievement Judgment
    flag1: Summon achievement flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Have you already summoned?"""
        if GetEventFlag(flag1) != 0:
            pass
        else:
            """State 3: Waiting for summon"""
            return 0
    """State 4: Finish"""
    return 1

def event_m10_17_x130(z1=600, flag1=100790):
    """[DC] [Preset] Guided White Spirit Summoning Achievement Judgment
    z1: White Spirit Generator ID
    flag1: Summon achievement flag
    """
    """State 0,1: [DC] [Reproduction] Guidance White Spirit Summon Achievement Judgment_SubState"""
    call = event_m10_17_x129(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Judgment white spirit summon achievement determination_SubState"""
        assert event_m10_17_x128(z1=z1)
        """State 2: [DC] [Execute] Guidance White Spirit Summon Achievement Judgment_SubState"""
        assert event_m10_17_x127(flag1=flag1)
    """State 4: Finish"""
    return 0

def event_m10_17_111092():
    """OBJ: Ladder Shop (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z139=104051, z140=10174000, z141=46, z142=7040)
    Quit()

def event_m10_17_111093():
    """OBJ: Ladder Shop (Tank Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7040:Laddersmith Gilligan
    event_m10_17_x4(z134=117010110, z135=117020111, z136=104050, z137=10174000, z138=111092, npc1=7040)
    Quit()

def event_m10_17_111094():
    """OBJ: Ladder shop (Tankoku valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z120=45, z121=104051)
    Quit()

def event_m10_17_111095():
    """OBJ: Ladder Shop (Tank Valley): Ladder"""
    """State 0,4: Ladder installation: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 1: Ladder installation: Branch"""
    CompareEventFlag(0, 102160, 0)
    if ConditionGroup(0):
        """State 2: Ladder installation: Hide"""
        ChangeObjState(10170500, 30)
        CompareObjState(0, 10170500, 30, 0)
        assert ConditionGroup(0)
        """State 3: Ladder installation: Hidden standby"""
        CompareEventFlag(0, 102160, 1)
        IsPlayerInTheMap(1, 0, 0)
        if ConditionGroup(0):
            """State 5: Ladder installation: re-execution"""
            RestartMachine()
            Quit()
        elif ConditionGroup(1):
            pass
    else:
        """State 6: Ladder installation: Display"""
        ChangeObjState(10170500, 10)
        CompareObjState(0, 10170500, 10, 0)
        assert ConditionGroup(0)
    """State 7: Ladder installation: Event end"""
    EndMachine()
    Quit()

def event_m10_17_111096():
    """OBJ: Ladder Shop (Tank Valley): Ladder Poly Play"""
    """State 0,4: Ladder installation: Poly drama start: Standby"""
    CompareEventFlag(0, 117020117, 1)
    assert ConditionGroup(0)
    """State 1,6: [Lib] Normal poly play_SubState"""
    assert event_m10_17_x0(z143=101710, mode4=0, flag9=117000118, z144=1, z145=1)
    """State 2: Ladder installation: Ladder display"""
    ChangeObjState(10170500, 10)
    CompareObjState(0, 10170500, 10, 0)
    assert ConditionGroup(0)
    """State 5: Ladder installation: Poly play: End"""
    SetEventFlag(117020117, 0)
    CompareEventFlag(0, 117020117, 0)
    assert ConditionGroup(0)
    """State 3: Ladder installation: System: End"""
    EndMachine()
    Quit()

def event_m10_17_111202():
    """OBJ: Dwarf: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z139=104132, z140=10174004, z141=246, z142=7260)
    Quit()

def event_m10_17_111203():
    """OBJ: Dwarf: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7260:Lonesome Gavlan
    event_m10_17_x4(z134=117010160, z135=117020161, z136=104130, z137=10174004, z138=111202, npc1=7260)
    Quit()

def event_m10_17_111204():
    """OBJ: Dwarf (Dwelling Valley): Death Determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z120=245, z121=104132)
    Quit()

def event_m10_17_111205():
    """OBJ: Dwarf (Dwelling Valley): Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_17_x25(z107=104130, z108=102340, z109=102343, z110=117020167, z111=103631)
    Quit()

def event_m10_17_111252():
    """OBJ: Patch (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z139=104172, z140=10174003, z141=66, z142=7440)
    Quit()

def event_m10_17_111253():
    """OBJ: Patch (Pump Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7440:Mild-mannered Pate
    event_m10_17_x4(z134=117010140, z135=117020141, z136=104170, z137=10174003, z138=111252, npc1=7440)
    Quit()

def event_m10_17_111254():
    """OBJ: Patch (dwelling valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z120=65, z121=104172)
    Quit()

def event_m10_17_111255():
    """OBJ: Patch (valley): Appearance determination"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_17_x25(z107=104170, z108=102450, z109=102451, z110=117020147, z111=103671)
    Quit()

def event_m10_17_111256():
    """OBJ: Patch (Tani no Valley): Treasure acquisition decision"""
    """State 0,1: Treasure acquisition decision: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Treasure acquisition decision: standby"""
        WasObjItemAcquired(0, 10175140, 1)
        assert ConditionGroup(0)
        """State 3: Treasure acquisition determination: flag setting"""
        SetEventFlag(117000148, 1)
        CompareEventFlag(0, 117000148, 1)
        assert ConditionGroup(0)
    """State 4: Treasure acquisition decision: System: End"""
    EndMachine()
    Quit()

def event_m10_17_111272():
    """OBJ: Woman Knight (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z139=104193, z140=10174001, z141=91, z142=7520)
    Quit()

def event_m10_17_111273():
    """OBJ: Woman Knight (Tank Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_17_x4(z134=117010120, z135=117020121, z136=104190, z137=10174001, z138=111272, npc1=7520)
    Quit()

def event_m10_17_111274():
    """OBJ: Woman Knight (Tank Valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z120=90, z121=104193)
    Quit()

def event_m10_17_111275():
    """OBJ: Woman Knight (Tank Valley): Appearance Judgment"""
    """State 0,1: [Lib] NPC: Woman Knight: Appearance Judgment_SubState"""
    event_m10_17_x6(z122=102480, z123=102482, z124=102483, z125=102486, z126=102491, z127=102485, z128=102487,
                    z129=102488)
    Quit()

def event_m10_17_111342():
    """OBJ: Material Store (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z139=104261, z140=10174002, z141=196, z142=7620)
    Quit()

def event_m10_17_111343():
    """OBJ: Material Store (Dwelling Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7620:Stone Trader Chloanne
    event_m10_17_x4(z134=117010150, z135=117020151, z136=104260, z137=10174002, z138=111342, npc1=7620)
    Quit()

def event_m10_17_111344():
    """OBJ: Material shop (Tank valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z120=195, z121=104261)
    Quit()

def event_m10_17_112010():
    """OBJ: Sun altar (pledge event)"""
    """State 0,1: [Lib] OBJ Pledge: Initial _SubState"""
    event_m10_17_x37(z98=10173250, z99=117020170)
    Quit()

def event_m10_17_118100():
    """Multi-use NPC: Swordsman (Male): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_17_x51(z80=556)
    Quit()

def event_m10_17_118110():
    """Multi-use NPC: Hint NPC: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_17_x51(z80=600)
    Quit()

def event_m10_17_118120():
    """Multi-use NPC: Test: Koshiro phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_17_x51(z80=605)
    Quit()

def event_m10_17_120000():
    """Trophy: A brilliant pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_17_x56(flag7=117020171, z77=18)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_17_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_17_x56(flag7=117020129, z77=33)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_17_4000000():
    """[BEST] Hanging poison trap 01_ destruction"""
    """State 0,3: [BEST] [Preset] Suspended Poison _ Destruction _ SubState"""
    call = event_m10_17_x123(z2=10173550, z3=10173500, z4=6000000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_17_4001000():
    """[BEST] Suspended Poison 02_Destruction"""
    """State 0,3: [BEST] [Preset] Suspended Poison _ Destruction _ SubState"""
    call = event_m10_17_x123(z2=10173560, z3=10173510, z4=6001000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_17_4002000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_17_x64(flag4=117020001, z60=14, flag5=117000002, z61=6, z62=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_17_x69(z65=80000000, z66=0, z67=5, z68=935, val2=1, z69=10, z70=80000001, z71=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_17_x69(z65=80000100, z66=0, z67=5, z68=935, val2=2, z69=10, z70=80000101, z71=80000199)
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m10_17_x69(z65=80000200, z66=0, z67=5, z68=935, val2=3, z69=10, z70=80000201, z71=80000299)
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert event_m10_17_x69(z65=80000300, z66=0, z67=5, z68=935, val2=4, z69=10, z70=80000301, z71=80000399)
        """State 8: [Lib] [DC] [Preset] Wanderer_Generation_5_SubState"""
        assert event_m10_17_x69(z65=80000400, z66=0, z67=5, z68=935, val2=5, z69=10, z70=80000401, z71=80000499)
        """State 9: [Lib] [DC] [Preset] Wanderer_Generation_6_SubState"""
        assert event_m10_17_x69(z65=80000500, z66=0, z67=5, z68=935, val2=6, z69=10, z70=80000501, z71=80000599)
        """State 2: Start flag ON"""
        SetEventFlag(117020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4002010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_17_x72(flag6=117000002, z63=935, mode1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4003000():
    """[DC] Liberation of dead workers in cages_way 1"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173310, z37=117010020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4003010():
    """[DC] Liberation of dead workers in cages_way 2"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173311, z37=117010021)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4003020():
    """[DC] Liberation of dead workers in cages 3"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173312, z37=117010022)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4003030():
    """[DC] Liberation of dead workers in cages 4"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z36=10173313, z37=117010023)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4004000():
    """[DC] Guided white spirit summon achievement achievement judgment"""
    """State 0,2: [DC] [Preset] Guidance White Spirit Summon Achievement Judgment_SubState"""
    assert event_m10_17_x130(z1=600, flag1=100790)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_17_4031000():
    """[DC] NPC White Spirit_Gesture Management_Naga"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_17_x77(flag3=117000091, z58=801, z59=117020092)
    """State 1: Finish"""
    EndMachine()
    Quit()

