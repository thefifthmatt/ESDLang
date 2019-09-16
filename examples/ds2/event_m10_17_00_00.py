# -*- coding: utf-8 -*-
def event_m10_17_1000():
    """Gate opened with lever"""
    """State 0,2,3: [Reproduction] Gate_SubState opened with lever"""
    assert event_m10_17_x78()
    """State 4: [Condition] Gate_SubState opened with lever"""
    assert event_m10_17_x79(z59=10172013)
    """State 5: [Execution] Gate opened with lever _SubState"""
    assert event_m10_17_x80(z58=100000)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_2000():
    """Hanging poison 01_attach"""
    """State 0,1: Attach a poison to the chain"""
    AttachObjToObj(10173500, 150, 10173550)
    """State 2: Finish"""
    EndMachine()

def event_m10_17_2010():
    """Suspended poison 01_operation"""
    """State 0,2: [Preset] Suspended Poison _ Operation _ SubState"""
    assert event_m10_17_x91(z52=10172120)
    """State 1: Rerun"""
    RestartMachine()

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

def event_m10_17_4000():
    """Elevator ⇔ Molten Fortress"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_17_x15(z88=10173100, z89=400010, z90=400000, z91=10172030, z92=10172020)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_4010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_17_x20(z119=10173100, z120=10172030, z121=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_4020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_17_x20(z119=10173100, z120=10172020, z121=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_4030():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m10_17_x46(z93=403000, z94=10173100, z95=105420, z96=70, z97=80, z98=1, z99=0)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_4050():
    """For connection_Connection flag OFF"""
    """State 0,3: [Lib] [Preset] Switch the connection flag at the point _SubState"""
    call = event_m10_17_x60(z78=405000, z79=405000, z80=105420, z81=0, z82=1)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()

def event_m10_17_5000():
    """Iron lattice that can be opened and closed by levers"""
    """State 0,2: [Preset] Iron lattice that can be opened and closed by lever"""
    assert event_m10_17_x114(z16=500000, z17=10172110, z18=10171540, z19=10172900)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_6000():
    """Suspended poison 02_ attach"""
    """State 0,1: Attach a poison to the chain"""
    AttachObjToObj(10173510, 150, 10173560)
    """State 2: Finish"""
    EndMachine()

def event_m10_17_6010():
    """Suspended poison 02_operation"""
    """State 0,2: [Preset] Suspended Poison _ Operation _ SubState"""
    assert event_m10_17_x91(z52=10172100)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_7000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_17_x26(z109=10171200)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_7010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_17_x36(z107=10171200, val3=10170010, z108=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_7020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10171300, z101=20, z102=702000, z103=0, z104=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_7100():
    """[Insect Key] Recovery Fountain_Poisonous_Startup"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_17_x26(z109=10171205)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_7110():
    """[Insect Key] Recovery Fountain _ Poisonous"""
    """State 0,2: [Preset] [Insect Key] Recovery Fountain_Poisonous_SubState"""
    assert (event_m10_17_x99(z30=10171205, z31=10171310, z32=10171315, z33=90, z34=240, z35=1, z36=2,
            z37=117000055))
    """State 1: Finish"""
    EndMachine()

def event_m10_17_8000():
    """Boss: Shabazahat_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_17_x8(z122=117000081, z123=800000, z124=800000, z125=102, z126=1017000, z127=117020080,
            mode3=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_17_8010():
    """Liberation of dead workers in cages 1"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173300, z39=117020085)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_8020():
    """Liberation of dead workers in cages 2"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173301, z39=117020086)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_8030():
    """Liberation of dead workers in cages 3"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173302, z39=117020087)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_8040():
    """Liberation of dead workers in cages 4"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173303, z39=117020088)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_8500():
    """Boss: Naga_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_17_x8(z122=117000091, z123=850000, z124=850000, z125=101, z126=1017010, z127=117020090,
            mode3=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_17_9000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10171355, z101=20, z102=900000, z103=0, z104=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_9010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10171360, z101=20, z102=901000, z103=0, z104=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_9020():
    """Hidden Door Navi Mesh Change 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10171350, z101=20, z102=902000, z103=0, z104=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_10000():
    """Disabling poison fog damage of enemy characters"""
    """State 0,2: [Preset] Enemy character's poison fog damage disabled_SubState"""
    assert (event_m10_17_x105(z22=147005, z23=311000, z24=200010010, z25=200010020, z26=200010030, z27=200010011,
            z28=200010021, z29=200010031))
    """State 1: Finish"""
    EndMachine()

def event_m10_17_11000():
    """Wooden wall 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10173600, z101=20, z102=1100000, z103=0, z104=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_11010():
    """The wooden wall 2 where the enemy destroys"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10173605, z101=20, z102=1101000, z103=0, z104=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_12000():
    """Floor switch treadle _ in front of iron bar"""
    """State 0,2: [Preset] Floor switch tread arrow _SubState"""
    assert event_m10_17_x112(z20=10171131, z21=10171011)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_12010():
    """Floor switch treadle _ crossroad"""
    """State 0,2: [Preset] Floor switch tread arrow _SubState"""
    assert event_m10_17_x112(z20=10171130, z21=10171012)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_14000():
    """Navi mesh change for destructible scaffold"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_17_x38(z100=10173800, z101=20, z102=1400000, z103=2, z104=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_15000():
    """Hunting Forest MAP loading and discarding"""
    """State 0,2: [Preset] Hunting Forest MAP loading discard_SubState"""
    assert event_m10_17_x119(z6=100, z7=105440)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_27000():
    """One-way door (destination jumped off)"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _2_SubState"""
    assert event_m10_17_x5(z138=0, z139=1101, z140=2700000, z141=117000180)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_31100():
    """[Asynchronous] Giant windmill"""
    """State 0,3: [Reproduction] Giant windmill_SubState"""
    call = event_m10_17_x92(z49=10171500, z50=117000055, z51=117000056)
    if call.Get() == 0:
        """State 4: [Condition] Giant windmill_SubState"""
        call = event_m10_17_x93(z48=10171500)
        if call.Get() == 1:
            """State 5: [Execution] Giant windmill_SubState"""
            assert (event_m10_17_x94(z40=10171500, z41=10171501, z42=10171502, z43=10171503, z44=10171504,
                    z45=117000055, z46=10171505, z47=117000056))
        elif call.Get() == 0:
            """State 2: Rerun"""
            RestartMachine()
            Quit()
    elif call.Get() == 1:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_17_32010():
    """Suspended ceiling: Ceiling"""
    """State 0,2: [Preset] Suspended ceiling_SubState"""
    assert event_m10_17_x84(z55=10172130, z56=10171530, z57=3201000, val1=7)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_17_42000():
    """Poison water drop"""
    """State 0,2: [Preset] Poison water drop_SubState"""
    assert event_m10_17_x118(z10=10173000, z11=10173001, z12=10173002, z13=10173003, z14=10173004, z15=117000055)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_80000():
    """Reproduction Fire 01_Cave in front of village mining square"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z85=1017000, z86=1017099)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_81000():
    """Rebirth Fire 02_After the Boss Java Hat, Lower Tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z85=1017100, z86=1017199)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_82000():
    """Rebirth Fire 03_ Entrance Poison Destination Cave"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z85=1017200, z86=1017299)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_83000():
    """After the huge windmill, the fireworks 04_"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z85=1017300, z86=1017399)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_84000():
    """Hidden door in front of the boss room, tower top layer"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_17_x55(z85=1017400, z86=1017499)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_x0(z151=101710, mode4=0, z152=117000118, z153=1, z154=1):
    """[Lib] Normal poly play
    z151: Poly play ID
    mode4: Destination point ID after poly play
    z152: Poly drama played flag
    z153: End fade
    z154: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(z152) != 1:
        """State 1: Poly play"""
        PlayCutscene(z151, z153, z154)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((mode4 > 1) != 0, mode4)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((mode4 > 1) != 0, mode4)
    SetEventFlag(z152, 1)
    """State 7: End state"""
    return 0

def event_m10_17_x1(z147=_, z148=_, z149=_, z150=_):
    """[Lib] NPC: Grave Placement: General purpose
    z147: Death map: Global event flag
    z148: Tomb: OBJ instance ID
    z149: Tomb move to: Generator ID
    z150: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z147, 1)
    IsGraveGeneratable(8, z150, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z148, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z148, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_17_x2(z144=_, z145=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z144: Global: death flag
    z145: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z145, 10, 0)
    CompareObjState(1, z145, 20, 0)
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
    IsObjSearched(0, z145)
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

def event_m10_17_x3(z142=_, z143=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z142: Area other flags: Ghost appearance
    z143: Area other flags: Conversation start
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
    SetEventFlag(z142, 1)
    CompareEventFlag(0, z142, 1)
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
    SetEventFlag(z143, 1)
    CompareEventFlag(0, z143, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_17_x4(z142=_, z143=_, z144=_, z145=_, z146=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z142: Ghost Appearance: Area Other Flag
    z143: Conversation start: Area and other flags
    z144: Death: Global event flag
    z145: Tomb: OBJ instance ID
    z146: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z146, 1, 0)
    CompareEventFlag(9, z142, 1)
    CompareObjState(9, z145, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z143, 1)
        CompareEventFlag(0, z143, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_17_x2(z144=z144, z145=z145, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_17_x3(z142=z142, z143=z143, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_17_x5(z138=0, z139=1101, z140=2700000, z141=117000180):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z138: Text ID when opened
    z139: Text ID when not opened
    z140: Point ID
    z141: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z140, 0, z138, z139, z141, 0)
    """State 2: End state"""
    return 0

def event_m10_17_x6(z130=102480, z131=102482, z132=102483, z133=102486, z134=102491, z135=102485, z136=102487,
                    z137=102488):
    """[Lib] NPC: Woman Knight: Appearance Judgment
    z130: Sub 1 encountering: Global event flag
    z131: During sub-2 encounter: Global event flag
    z132: Sub 3 encountering: Global event flag
    z133: Generation stop: Global event flag
    z134: Appearance permission: Global event flag
    z135: Sub 1 generation stop: Global event flag
    z136: Sub 2 generation stop: Global event flag
    z137: Sub 3 generation stop: Global event flag
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
            CompareEventFlag(0, z133, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 2: Appearance determination: Judgment while encountering other maps"""
                CompareEventFlag(8, z130, 1)
                CompareEventFlag(8, z135, 0)
                CompareEventFlag(9, z131, 1)
                CompareEventFlag(9, z136, 0)
                CompareEventFlag(10, z132, 1)
                CompareEventFlag(10, z137, 0)
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
                        SetEventFlag(z134, 1)
                        CompareEventFlag(0, z134, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
        """State 3: Appearance judgment: Appearance impossible"""
        SetEventFlag(z134, 0)
        CompareEventFlag(0, z134, 0)
        assert ConditionGroup(0)
    """State 5: Appearance determination: System: Event end"""
    Label('L0')
    EndMachine()

def event_m10_17_x7(z128=_, z129=_):
    """[Lib] NPC: Death determination: General purpose
    z128: Generator ID
    z129: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z129, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z128)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z129, 1)
            CompareEventFlag(0, z129, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_17_x8(z122=_, z123=_, z124=_, z125=_, z126=_, z127=_, mode3=0):
    """[Lib] [Preset] Boss Battle Start
    z122: Boss destruction flag
    z123: Start point ID
    z124: End point ID
    z125: Sound ID
    z126: Boss Battle ID
    z127: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_17_x9(z122=z122)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_17_x10(z123=z123, z124=z124)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_17_x11(z125=z125, z126=z126, z127=z127)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_17_x12()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_17_x13(z126=z126)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_17_x14(z125=z125, z126=z126, z127=z127, mode3=mode3)
    """State 7: End state"""
    return 0

def event_m10_17_x9(z122=_):
    """[Reproduction] Boss Battle_Start
    z122: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z122) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_17_x10(z123=_, z124=_):
    """[Condition] Boss Battle_Start
    z123: Start point ID
    z124: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z123, z124, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z123, z124, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x11(z125=_, z126=_, z127=_):
    """[Execution] Boss Battle_Start
    z125: Sound ID
    z126: Boss Battle ID
    z127: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z125)
    """State 1: Boss battle start notification"""
    StartBossFight(z126)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z127, 1)
    """State 4: End state"""
    return 0

def event_m10_17_x12():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x13(z126=_):
    """[Condition] Boss Battle_End Judgment
    z126: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z126, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x14(z125=_, z126=_, z127=_, mode3=0):
    """[Execute] Boss Battle_End
    z125: Sound ID
    z126: Boss Battle ID
    z127: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z127, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z126)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode3) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z125)
    """State 5: End state"""
    return 0

def event_m10_17_x15(z88=10173100, z89=400010, z90=400000, z91=10172030, z92=10172020):
    """[Lib] [Preset] Elevator
    z88: OBJ instance ID of the elevator
    z89: On elevator point ID_
    z90: Elevator point ID_below
    z91: Upper lever OBJ instance ID
    z92: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_17_x16()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_17_x17(z88=z88, z89=z89, z90=z90, z91=z91, z92=z92)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_17_x50(z88=z88, z90=z90)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_17_x49(z88=z88, z89=z89)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_17_x18(z88=z88, z89=z89)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_17_x19(z88=z88, z90=z90)
    """State 7: End state"""
    return 0

def event_m10_17_x16():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x17(z88=10173100, z89=400010, z90=400000, z91=10172030, z92=10172020):
    """[Condition] Elevator
    z88: Elevator OBJ instance ID
    z89: On elevator point ID_
    z90: Elevator point ID_below
    z91: Upper lever OBJ instance ID
    z92: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z88, 10, 0)
    CompareObjState(1, z88, 40, 0)
    CompareObjState(2, z88, 80, 0)
    CompareObjState(2, z88, 41, 0)
    CompareObjState(3, z88, 70, 0)
    CompareObjState(3, z88, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z90, z90, 1)
        CompareObjState(0, z91, 74, 0)
        CompareObjState(0, z91, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z89, z89, 1)
        CompareObjState(0, z92, 74, 0)
        CompareObjState(0, z92, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_17_x18(z88=10173100, z89=400010):
    """[Execution] Elevator_Rise
    z88: Elevator OBJ instance ID
    z89: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z88, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z88, 30, 0)
    IsPlayerInsidePoint(8, z89, z89, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z88, 71)
    assert CompareObjStateId(z88, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x19(z88=10173100, z90=400000):
    """[Execution] Elevator_Descent
    z88: Elevator OBJ instance ID
    z90: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z88, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z88, 41, 0)
    IsPlayerInsidePoint(8, z90, z90, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z88, 81)
    assert CompareObjStateId(z88, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x20(z119=10173100, z120=_, z121=_):
    """[Lib] [Preset] Elevator lever
    z119: OBJ instance ID of the elevator
    z120: Lever OBJ instance ID
    z121: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_17_x21()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_17_x22(z119=z119, z120=z120, z121=z121)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_17_x23(z119=z119, z120=z120, z121=z121)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_17_x24(z119=z119, z120=z120, z121=z121)
    """State 5: Rerun"""
    return 0

def event_m10_17_x21():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x22(z119=10173100, z120=_, z121=_):
    """[Condition] Elevator lever_use judgment
    z119: OBJ instance ID of the elevator
    z120: Lever OBJ instance ID
    z121: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z119, z121, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_17_x23(z119=10173100, z120=_, z121=_):
    """[Execution] Elevator lever_Key guide valid
    z119: OBJ instance ID of the elevator
    z120: Lever OBJ instance ID
    z121: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z120, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z119, z121, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x24(z119=10173100, z120=_, z121=_):
    """[Execute] Elevator lever_key guide disabled
    z119: OBJ instance ID of the elevator
    z120: Lever OBJ instance ID
    z121: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z120, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z119, z121, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x25(z114=_, z115=_, z116=_, z117=_, z118=_):
    """[Lib] Appearance determination: General purpose
    z114: Death: Global event flag
    z115: Local emigration permission: Global event flag
    z116: Relocation permission after moving: Global event flag
    z117: Appearance determination: Area and other flags
    z118: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z114, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z115, 1)
            CompareEventFlag(8, z116, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z115, 1)
                CompareEventFlag(8, z118, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z117, 1)
                    CompareEventFlag(0, z117, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z117, 0)
                    CompareEventFlag(0, z117, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z117, 0)
        CompareEventFlag(0, z117, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m10_17_x26(z109=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z109: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_17_x27(z109=z109)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_17_x31(z109=z109)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_17_x32()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_17_x28(z109=z109, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_17_x29(z109=z109, z111=38, z112=3, z113=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_17_x30(z109=z109, z110=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_17_x27(z109=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z109: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z109, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z109, 10)
        assert CompareObjStateId(z109, 10, 0)
    elif CompareObjStateId(z109, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z109, 74, 1) and CompareObjStateId(z109, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_17_x28(z109=_, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z109: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z109)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_17_x29(z109=_, z111=38, z112=3, z113=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z109: Object instance ID
    z111: Key guide type
    z112: Event action
    z113: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z109, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z109, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z109, 30)
        assert CompareObjStateId(z109, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z109, z111, z112)
        assert PlayerIsInEventAction(z112) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z112, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z109, 74, 0)
        CompareObjState(1, z109, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z113)
            assert CompareObjStateId(z109, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z109, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_17_x30(z109=_, z110=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z109: Object instance ID
    z110: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z109, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_17_x31(z109=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z109: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z109, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x32():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x33(z107=10171200, val3=10170010):
    """[Reproduction] Hidden door 1_face SFX
    z107: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z107, 20, 0):
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

def event_m10_17_x34(z107=10171200):
    """[Conditions] Hidden door 1_Face SFX
    z107: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z107, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x35(z107=10171200, val3=10170010, z108=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z107: OBJ instance ID of the bug key
    val3: Event light ID
    z108: Light fade time
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
        SetPointLightEnabled(val3, 1, z108)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_17_x36(z107=10171200, val3=10170010, z108=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z107: OBJ instance ID of the bug key
    val3: Event light ID
    z108: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_17_x33(z107=z107, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_17_x34(z107=z107)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_17_x35(z107=z107, val3=val3, z108=z108, val4=val4)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_17_x37(z105=10173250, z106=117020170):
    """[Lib] OBJ Pledge: First move
    z105: OBJ instance ID
    z106: During menu operation: Area and other flags
    """
    """State 0,10: OBJ: Pledge: Initialization"""
    SetEventFlag(z106, 0)
    """State 1: OBJ: Pledge: Start"""
    SetObjSync(z105, 0)
    IsPlayerInTheMap(8, 1, 0)
    CompareEventFlag(8, z106, 0)
    assert ConditionGroup(8)
    """State 2: OBJ: Pledge: Net multiplayer judgment"""
    if IsGuest() != 0:
        """State 3: OBJ: Pledge: Hide"""
        ChangeOwnObjState(10)
        CompareObjState(0, z105, 10, 0)
        assert ConditionGroup(0)
        """State 9: OBJ: Pledge: System: End"""
        EndMachine()
    else:
        """State 4: OBJ: Pledge: Display"""
        ChangeOwnObjState(30)
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 5: OBJ: Pledge: Start: Wait"""
        IsObjSearched(0, z105)
        assert ConditionGroup(0)
        """State 7: OBJ: Pledge: Launch"""
        SetEventFlag(z106, 1)
        CompareEventFlag(0, z106, 1)
        assert ConditionGroup(0)
        """State 8: OBJ: Pledge: Menu running: Wait"""
        CompareEventFlag(0, z106, 0)
        assert ConditionGroup(0)
        """State 11: OBJ: Pledge: Timer"""
        KeyGuideTemporarilyInvalid(1)
        CompareStateTime(0, 1, 3, 1)
        assert ConditionGroup(0)
        """State 6: OBJ: Pledge: System: Re-execution"""
        RestartMachine()

def event_m10_17_x38(z100=_, z101=20, z102=_, z103=_, z104=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z100: Object instance ID
    z101: OBJ state ID
    z102: Navimesh switching point ID
    z103: Additional attributes
    z104: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_17_x39(z100=z100, z101=z101, z102=z102, z104=z104, z103=z103)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_17_x40(z100=z100, z101=z101, z102=z102)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_17_x41(z100=z100, z101=z101, z102=z102, z103=z103, z104=z104)
    """State 4: End state"""
    return 0

def event_m10_17_x39(z100=_, z101=20, z102=_, z104=_, z103=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z100: Target OBJ instance ID
    z101: Target OBJ state ID
    z102: Navimesh switching point ID
    z104: Additional attributes
    z103: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z100, z101, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z102, z104)
        DeleteNavimeshAttribute(z102, z103)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_17_x40(z100=_, z101=20, z102=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z100: Target OBJ instance ID
    z101: Target OBJ state ID
    z102: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z100, z101, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x41(z100=_, z101=20, z102=_, z103=_, z104=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z100: Target OBJ instance ID
    z101: Target OBJ state ID
    z102: Navimesh switching point ID
    z103: Additional attributes
    z104: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z102, z103)
    DeleteNavimeshAttribute(z102, z104)
    """State 2: End state"""
    return 0

def event_m10_17_x42():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x43(z93=403000, z94=10173100, z96=70, z97=80):
    """[Lib] [Condition] Elevator_Connection replacement
    z93: Replacement point
    z94: OBJ instance ID of the elevator
    z96: Top_Hit group ID
    z97: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z93, z93, 1)
    CompareObjState(8, z94, 70, 0)
    IsPlayerInsidePoint(9, z93, z93, 1)
    CompareObjState(9, z94, 80, 0)
    IsPlayerOnHitGroup(0, z96, 1)
    IsPlayerOnHitGroup(1, z97, 1)
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

def event_m10_17_x44(z93=403000, z95=105420, z98=1, z96=70, z94=10173100):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z93: Replacement point
    z95: Global flag for connection
    z98: ON / OFF of global flag
    z96: Top_Hit group ID
    z94: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z95, z98)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z93, z93, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z96, 1)
    IsPlayerInsidePoint(8, z93, z93, 1)
    CompareObjState(8, z94, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_17_x45(z95=105420, z98=1, z96=70, z93=403000, z94=10173100):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z95: Global flag for connection
    z98: ON / OFF of global flag
    z96: Hit group ID
    z93: Replacement point ID
    z94: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z95, z98)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z96, 0)
    IsPlayerInsidePoint(8, z93, z93, 1)
    CompareObjState(8, z94, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x46(z93=403000, z94=10173100, z95=105420, z96=70, z97=80, z98=1, z99=0):
    """[Lib] [Preset] Elevator_Connection replacement
    z93: Replacement point
    z94: OBJ instance ID of the elevator
    z95: Global flag for connection
    z96: Top_Hit group ID
    z97: Bottom_Hit group ID
    z98: Up_Global flag when rising
    z99: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m10_17_x42()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m10_17_x43(z93=z93, z94=z94, z96=z96, z97=z97)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m10_17_x44(z93=z93, z95=z95, z98=z98, z96=z96, z94=z94)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m10_17_x48(z93=z93, z95=z95, z99=z99, z97=z97, z94=z94)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m10_17_x45(z95=z95, z98=z98, z96=z96, z93=z93, z94=z94)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m10_17_x47(z95=z95, z99=z99, z97=z97, z93=z93, z94=z94)
    """State 7: End state"""
    return 0

def event_m10_17_x47(z95=105420, z99=0, z97=80, z93=403000, z94=10173100):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z95: Global flag for connection
    z99: ON / OFF of global flag
    z97: Hit group ID
    z93: Replacement point ID
    z94: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z95, z99)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z97, 0)
    IsPlayerInsidePoint(8, z93, z93, 1)
    CompareObjState(8, z94, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x48(z93=403000, z95=105420, z99=0, z97=80, z94=10173100):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z93: Replacement point
    z95: Global flag for connection
    z99: ON / OFF of global flag
    z97: Bottom_Hit group ID
    z94: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z95, z99)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z93, z93, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z97, 1)
    IsPlayerInsidePoint(8, z93, z93, 1)
    CompareObjState(8, z94, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_17_x49(z88=10173100, z89=400010):
    """[Execution] Elevator_Return switch after lift
    z88: Elevator OBJ instance ID
    z89: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z88, 30, 0)
    IsPlayerInsidePoint(8, z89, z89, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z88, 71)
    assert CompareObjStateId(z88, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_17_x50(z88=10173100, z90=400000):
    """[Execution] Elevator_Return switch after descending
    z88: Elevator OBJ instance ID
    z90: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z88, 41, 0)
    IsPlayerInsidePoint(8, z90, z90, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z88, 81)
    assert CompareObjStateId(z88, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_17_x51(z87=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z87: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z87)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_17_x52():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x53(z85=_, z86=_):
    """[Lib] [execute] Rebirth fire
    z85: Flag start ID
    z86: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z85, z86, 0)
    """State 2: End state"""
    return 0

def event_m10_17_x54():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x55(z85=_, z86=_):
    """[Lib] [Preset] Rebirth
    z85: Flag start ID
    z86: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_17_x52()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_17_x54()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_17_x53(z85=z85, z86=z86)
    """State 4: End state"""
    return 0

def event_m10_17_x56(z83=_, z84=_):
    """[Lib] [Preset] Get trophy
    z83: Acquisition trigger_other flags
    z84: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z83) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z83, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z84)
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

def event_m10_17_x58(z78=405000, z79=405000):
    """[Lib] [Condition] Switch the connection flag at the point
    z78: Start point ID
    z79: End point ID
    """
    """State 0,1: Are you in point?"""
    IsPlayerInsidePoint(0, z78, z79, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x59(z80=105420, z81=0, z82=1):
    """[Lib] [Execution] Switch to the connection flag at the point
    z80: Global event flag for connection
    z81: Flag switching
    z82: Wait for next judgment
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z80, z81)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z80, z81)
    assert ConditionGroup(0)
    """State 3: For next judgment: Has the flag changed?"""
    CompareEventFlag(0, z80, z82)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_17_x60(z78=405000, z79=405000, z80=105420, z81=0, z82=1):
    """[Lib] [Preset] Switch the connection flag at the point
    z78: Start point ID
    z79: End point ID
    z80: Global event flag for connection
    z81: Flag switching
    z82: Wait for next judgment
    """
    """State 0,1: [Lib] [Reproduction] Switch the connection flag at the point _SubState"""
    call = event_m10_17_x57()
    if call.Get() == 0:
        """State 3: [Lib] [Condition] Switch connection flag at point _SubState"""
        assert event_m10_17_x58(z78=z78, z79=z79)
        """State 2: [Lib] [Execution] Switch to the connection flag at the point _SubState"""
        assert event_m10_17_x59(z80=z80, z81=z81, z82=z82)
        """State 4: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 5: Guest: Exit"""
        return 1

def event_m10_17_x61(z63=117020001, z65=117000002):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z63: Lottery determination flag
    z65: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z65) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z63) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_17_x62(z64=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z64: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z64, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_17_x63(z63=117020001, z66=6, z67=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z63: Lottery determination flag
    z66: Number of appearance judgment points
    z67: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z63, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z66)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z67, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_17_x64(z63=117020001, z64=14, z65=117000002, z66=6, z67=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z63: Lottery determination flag
    z64: Random number comparison value
    z65: Defeat flag
    z66: Number of appearance judgment points
    z67: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_17_x61(z63=z63, z65=z65)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_17_x62(z64=z64)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_17_x63(z63=z63, z66=z66, z67=z67)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_17_x73(z63=z63, z67=z67)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_17_x65(val2=_, z75=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z75: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z75) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_17_x66(z71=_, z72=0, z73=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z71: Appearance judgment point ID
    z72: Minimum appearance time
    z73: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z71, z71, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z72, 3, z73)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_17_x67(z74=935, z76=_, z77=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z74: Generator ID
    z76: Appearance start point ID
    z77: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z74, z76, z77)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z74)
    """State 4: Finish"""
    return 0

def event_m10_17_x68(z68=117000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z68: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z68) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_17_x69(z71=_, z72=0, z73=5, z74=935, val2=_, z75=10, z76=_, z77=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z71: Intrusion detection point ID
    z72: Minimum appearance time
    z73: Maximum time to appear
    z74: Generator ID
    val2: Appearance judgment number
    z75: Lottery result point variable
    z76: Appearance start point ID
    z77: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_17_x65(val2=val2, z75=z75)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_17_x66(z71=z71, z72=z72, z73=z73)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_17_x67(z74=z74, z76=z76, z77=z77)
    """State 4: Finish"""
    return 0

def event_m10_17_x70(z69=935, mode1=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z69: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z69)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_17_x71(z68=117000002, z70=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z68: Defeat flag
    z70: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z68, 1)
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
                    SetEventFlag(z70, 1)
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

def event_m10_17_x72(z68=117000002, z69=935, mode1=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z68: Defeat flag
    z69: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_17_x68(z68=z68)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_17_x70(z69=z69, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_17_x71(z68=z68, z70=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_17_x71(z68=z68, z70=102755)
    """State 5: End state"""
    return 0

def event_m10_17_x73(z63=117020001, z67=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z63: Lottery determination flag
    z67: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z63, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z67, 0)
    """State 3: End state"""
    return 0

def event_m10_17_x74(z60=117000091):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z60: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z60) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_17_x75(z61=801):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z61: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z61, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x76(z62=117020092):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z62: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z62, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x77(z60=117000091, z61=801, z62=117020092):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z60: Boss destruction flag
    z61: Boss generator ID
    z62: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_17_x74(z60=z60)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_17_x75(z61=z61)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_17_x76(z62=z62)
    """State 4: End state"""
    return 0

def event_m10_17_x78():
    """[Reproduction] Gate opened with lever"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x79(z59=10172013):
    """[Condition] Gate opened by lever
    z59: Lever OBJ object instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z59, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x80(z58=100000):
    """[Execution] Gate opened by lever
    z58: Navigation mesh change
    """
    """State 0,1: Gate animation opening with lever"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(30, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z58, 2)
    """State 3: End state"""
    return 0

def event_m10_17_x81(z55=10172130, z56=10171530, z57=3201000):
    """[Reproduction] Suspended ceiling
    z55: Lever instance ID
    z56: Ceiling instance ID
    z57: Damage area ID
    """
    """State 0,5: [SEQ26778] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 3: Is the ceiling in the initial state?"""
    if CompareObjStateId(z56, 10, 1):
        """State 4: Initializing the ceiling"""
        InitializeObj(z56)
    else:
        pass
    """State 2: Damage invalid"""
    EnableDamageArea(z57, 0)
    """State 1: Activate key guide"""
    DisableObjKeyGuide(z55, 0)
    """State 6: End state"""
    return 0

def event_m10_17_x82(z55=10172130):
    """[Conditions] Suspended ceiling
    z55: Lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z55, 74, 0)
    CompareObjState(0, z55, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x83(z56=10171530, z57=3201000, val1=7, z55=10172130):
    """[Execution] suspended ceiling
    z56: Suspended ceiling instance ID
    z57: Damage area ID
    val1: Fall waiting time
    z55: Lever instance ID
    """
    """State 0,6: Disable key guide"""
    DisableObjKeyGuide(z55, 1)
    """State 1: OBJ state transition: suspended ceiling"""
    ChangeObjState(z56, 70)
    """State 2: Wait for descent start"""
    CompareObjState(0, z56, 71, 0)
    assert ConditionGroup(0)
    """State 5: Time lapse state"""
    assert (GetStateTime() > val1) != 0
    """State 3: Activate damage"""
    EnableDamageArea(z57, 1)
    """State 4: Wait for descent completion"""
    CompareObjState(0, z56, 10, 0)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m10_17_x84(z55=10172130, z56=10171530, z57=3201000, val1=7):
    """[Preset] Suspended ceiling
    z55: Lever instance ID
    z56: Suspended ceiling instance ID
    z57: Damage area ID
    val1: Fall waiting time
    """
    """State 0,1: [Reproduction] Suspended ceiling_SubState"""
    assert event_m10_17_x81(z55=z55, z56=z56, z57=z57)
    """State 2: [Condition] Suspended ceiling_SubState"""
    assert event_m10_17_x82(z55=z55)
    """State 3: [Execution] Suspended ceiling_SubState"""
    assert event_m10_17_x83(z56=z56, z57=z57, val1=val1, z55=z55)
    """State 4: End state"""
    return 0

def event_m10_17_x85(z18=10171540, z17=10172110, z16=500000):
    """[Reproduction] Iron lattice that can be opened and closed by levers
    z18: OBJ instance ID of the bar
    z17: OBJ instance ID of the lever
    z16: Navigation change point ID
    """
    """State 0,1: Is the iron lattice in anime?"""
    if CompareObjStateId(z18, 70, 0):
        """State 2: Disabling the key guide of the lever"""
        DisableObjKeyGuide(z17, 1)
        """State 4: Waiting for the rise of the iron lattice"""
        assert CompareObjStateId(z18, 30, 0)
        """State 3: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z16, 2)
        """State 5: Enable key guide for lever"""
        DisableObjKeyGuide(z17, 0)
    elif CompareObjStateId(z18, 80, 0):
        """State 6: Disabling the key guide for the lever_2"""
        DisableObjKeyGuide(z17, 1)
        """State 8: Waiting for the descent of the iron grid"""
        assert CompareObjStateId(z18, 10, 0)
        """State 7: Navimesh attribute added"""
        AddNavimeshAttribute(z16, 2)
        """State 9: Lever key guide activation_2"""
        DisableObjKeyGuide(z17, 0)
    else:
        """State 10: State determination of iron grid"""
        if CompareObjStateId(z18, 30, 0):
            """State 11: Navimesh attribute deletion_2"""
            DeleteNavimeshAttribute(z16, 2)
        elif CompareObjStateId(z18, 10, 0):
            """State 12: Navimesh attribute added_2"""
            AddNavimeshAttribute(z16, 2)
    """State 13: End state"""
    return 0

def event_m10_17_x86(z17=10172110, z19=10172900, z18=10171540):
    """[Conditions] Iron lattice that can be opened and closed by levers
    z17: Wall hole lever OBJ instance ID
    z19: OBJ instance ID for enemy judgment
    z18: Iron lattice OBJ instance ID
    """
    """State 0,1: Lever operation or enemy starts"""
    CompareObjState(0, z17, 74, 0)
    CompareObjState(0, z17, 84, 0)
    IsObjDamaged(0, z19, -1, 4000, 112400010)
    IsObjDamaged(0, z19, -1, 4000, 112401010)
    IsObjDamaged(0, z19, -1, 4000, 112402010)
    assert ConditionGroup(0)
    """State 2: State determination of iron grid"""
    CompareObjState(0, z18, 10, 0)
    CompareObjState(1, z18, 30, 0)
    if ConditionGroup(0):
        """State 3: The iron grid is down"""
        return 0
    elif ConditionGroup(1):
        """State 4: The iron grid is up"""
        return 1

def event_m10_17_x87(z16=500000, z17=10172110, z18=10171540):
    """[Execution] Iron lattice that can be opened and closed with a lever
    z16: Navigation change point ID
    z17: Lever OBJ instance ID
    z18: Iron lattice OBJ instance ID
    """
    """State 0,3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z17, 1)
    """State 1: Iron lattice rise animation playback: 70"""
    ChangeObjState(z18, 70)
    """State 4: Waiting for the rise of the iron lattice"""
    CompareObjState(0, z18, 30, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z16, 2)
    """State 5: Enable key guide for lever"""
    DisableObjKeyGuide(z17, 0)
    """State 6: End state"""
    return 0

def event_m10_17_x88():
    """[Reproduction] Suspended poisonous _ operation"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x89(z52=_):
    """[Conditions] Hanging poisonous jars in operation
    z52: OBJ instance ID of the lever
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z52, 74, 0)
    CompareObjState(0, z52, 84, 0)
    assert ConditionGroup(0)
    """State 3: Disable key guide"""
    DisableObjKeyGuide(z52, 1)
    """State 2: Chain status judgment"""
    if CompareOwnObjStateId(10, 0):
        """State 4: Under"""
        return 0
    elif CompareOwnObjStateId(30, 0):
        """State 5: It is above"""
        return 1

def event_m10_17_x90(z53=_, z54=_, z52=_):
    """[Execution] Hanging Poisonous _ Operation
    z53: OBJ state ID in operation
    z54: OBJ state ID after operation
    z52: OBJ instance ID of the lever
    """
    """State 0,1: Chain OBJ animation playback"""
    ChangeOwnObjState(z53)
    assert CompareOwnObjStateId(z54, 0)
    """State 2: End of lever animation"""
    CompareObjState(0, z52, 10, 0)
    CompareObjState(0, z52, 30, 0)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z52, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x91(z52=_):
    """[Preset] Suspended poisonous _ operation
    z52: OBJ instance ID of the lever
    """
    """State 0,1: [Reproduction] Hanging poisonous lever _SubState"""
    assert event_m10_17_x88()
    """State 3: [Condition] Lung poison lever _SubState"""
    call = event_m10_17_x89(z52=z52)
    if call.Get() == 0:
        """State 2: [Execution] Hung poison poison lever _SubState"""
        assert event_m10_17_x90(z53=70, z54=30, z52=z52)
    elif call.Get() == 1:
        """State 4: [Execution] Lung Poison Lever_2_SubState"""
        assert event_m10_17_x90(z53=80, z54=10, z52=z52)
    """State 5: End state"""
    return 0

def event_m10_17_x92(z49=10171500, z50=117000055, z51=117000056):
    """[Reproduction] Giant windmill
    z49: Huge windmill instance ID
    z50: Windmill burned flag
    z51: Windmill burning start flag
    """
    """State 0,1: Wind turbine OBJ status judgment"""
    if CompareObjStateId(z49, 20, 0):
        """State 3: [DC] Windmill burning start flag ON"""
        Label('L0')
        SetEventFlag(z51, 1)
        """State 2: Burned flag set"""
        SetEventFlag(z50, 1)
        """State 5: End state"""
        return 1
    elif CompareObjStateId(z49, 51, 0):
        Goto('L0')
    else:
        """State 4: [Condition] To giant windmill"""
        return 0

def event_m10_17_x93(z48=10171500):
    """[Condition] Giant windmill
    z48: Huge windmill instance ID
    """
    """State 0,5: Judgment of state of giant windmill"""
    if CompareObjStateId(z48, 30, 0):
        """State 1: With key guide"""
        Label('L0')
        CompareObjState(0, z48, 20, 0)
        CompareObjState(0, z48, 50, 0)
        IsPlayerUsingTorch(8, 0)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Transition to no key guide: 10"""
            ChangeObjState(z48, 10)
            CompareObjState(0, z48, 30, 1)
            assert ConditionGroup(0)
            """State 6: To redo"""
            return 0
    else:
        """State 2: Without key guide"""
        CompareObjState(0, z48, 20, 0)
        CompareObjState(0, z48, 50, 0)
        IsPlayerUsingTorch(8, 1)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 4: Transition to key guide existence: 30"""
            ChangeObjState(z48, 30)
            Goto('L0')
    """State 7: [Execution] To giant windmill"""
    return 1

def event_m10_17_x94(z40=10171500, z41=10171501, z42=10171502, z43=10171503, z44=10171504, z45=117000055,
                     z46=10171505, z47=117000056):
    """[Execution] Giant windmill
    z40: Huge windmill instance ID
    z41: Instance ID of giant windmill wing 1
    z42: Instance ID of giant windmill wing 2
    z43: Instance ID of giant windmill wing 3
    z44: Instance ID of Giant Windmill Wing 4
    z45: Windmill burned flag
    z46: OBJ instance ID of center feather
    z47: Windmill burning start flag
    """
    """State 0,3: [DC] Windmill burning start flag ON"""
    SetEventFlag(z47, 1)
    """State 1: on fire"""
    ChangeObjState(z41, 70)
    ChangeObjState(z42, 70)
    ChangeObjState(z43, 70)
    ChangeObjState(z44, 70)
    ChangeObjState(z46, 70)
    assert CompareObjStateId(z40, 51, 0)
    """State 2: Windmill burning flag ON"""
    SetEventFlag(z45, 1)
    """State 4: End state"""
    return 0

def event_m10_17_x95(z38=_, z39=_):
    """[Preset] Workers released from dead dead
    z38: The instance ID of the bag containing the worker
    z39: Worker release flag of dead dead in cage
    """
    """State 0,1: [Reproduction] Liberation of dead workers in cages_SubState"""
    assert event_m10_17_x96()
    """State 2: [Conditions] Liberation of dead workers in cages_SubState"""
    assert event_m10_17_x97(z38=z38)
    """State 3: [Execution] Liberation of dead workers in cages_SubState"""
    assert event_m10_17_x98(z39=z39)
    """State 4: End state"""
    return 0

def event_m10_17_x96():
    """[Reproduction] Liberation of dead workers in cages"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x97(z38=_):
    """[Conditions] Liberation of dead workers in cages
    z38: The instance ID of the bag containing the worker
    """
    """State 0,1: Was the cage containing the workers destroyed?"""
    assert CompareObjStateId(z38, 20, 0)
    """State 2: End state"""
    return 0

def event_m10_17_x98(z39=_):
    """[Execution] Liberation of dead workers in cages
    z39: Worker release flag of dead dead in cage
    """
    """State 0,1: Raise a worker release flag for the dead dead"""
    SetEventFlag(z39, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x99(z30=10171205, z31=10171310, z32=10171315, z33=90, z34=240, z35=1, z36=2, z37=117000055):
    """[Preset] [Insect Key] Recovery Fountain _ Poisonous
    z30: Bug ID OBJ instance ID
    z31: Instance ID of Recovery OBJ
    z32: Poison water OBJ instance ID
    z33: Hit group ID
    z34: Grand material ID
    z35: Grand material slot_poisonous water
    z36: Grand Material Slot_Recovery
    z37: Windmill burned flag
    """
    """State 0,1: [Reproduction] [Insect Key] Recovery Fountain_Poisonous_SubState"""
    call = event_m10_17_x100(z30=z30, z31=z31, z32=z32, z33=z33, z34=z34, z35=z35, z36=z36, z37=z37)
    if call.Get() == 0:
        """State 2: [Condition] [Insect Key] Recovery Fountain_Poisonous_SubState"""
        call = event_m10_17_x101(z30=z30, z37=z37)
        if call.Get() == 0:
            """State 3: [Execute] [Insect Key] Recovery Fountain_Poisonous_Recovery_SubState"""
            Label('L0')
            assert event_m10_17_x102(z31=z31, z33=z33, z34=z34, z36=z36)
        elif call.Get() == 1:
            """State 4: [Execute] [Insect Key] Recovery Fountain _ Poisonous _ Poison water not activated _SubState"""
            assert event_m10_17_x103(z32=z32, z33=z33, z34=z34, z35=z35, z37=z37)
            Goto('L0')
    elif call.Get() == 2:
        """State 5: [Execution] [Insect Key] Recovery Fountain_Poisonous_Poison Water Activated_SubState"""
        assert event_m10_17_x104(z32=z32, z33=z33, z34=z34, z35=z35, z37=z37)
        Goto('L0')
    elif call.Get() == 1:
        pass
    """State 6: End state"""
    return 0

def event_m10_17_x100(z30=10171205, z31=10171310, z32=10171315, z33=90, z34=240, z35=1, z36=2, z37=117000055):
    """[Reproduction] [Insect Key] Recovery Fountain _ Poisonous
    z30: Bug ID OBJ instance ID
    z31: Instance ID of Recovery OBJ
    z32: Poison water OBJ instance ID
    z33: Hit group ID
    z34: Grand material ID
    z35: Grand material slot_poisonous water
    z36: Grand Material Slot_Recovery
    z37: Windmill burned flag
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z30, 20, 0):
        pass
    else:
        Goto('L1')
    """State 2: Did you remove the poison?"""
    if CompareObjStateId(z32, 20, 0):
        pass
    elif CompareObjStateId(z32, 71, 0):
        pass
    else:
        Goto('L0')
    """State 7: Has water already accumulated?"""
    if CompareObjStateId(z31, 20, 0):
        pass
    else:
        """State 4: Reserving water: 70"""
        ChangeObjState(z31, 70)
        """State 8: Waiting for accumulation"""
        assert CompareObjStateId(z31, 20, 0)
    """State 6: Enable grand material recovery"""
    SetGroundMaterial(z33, z34, z36)
    """State 12: Started: Recovery"""
    return 1
    """State 9: Has poison water already accumulated?"""
    Label('L0')
    if CompareObjStateId(z32, 30, 0):
        pass
    else:
        """State 3: Accumulate poisonous water: 70"""
        ChangeObjState(z32, 70)
        """State 10: Puddle waiting_2"""
        assert CompareObjStateId(z32, 30, 0)
    """State 5: Activate poison water of Grand Material"""
    SetGroundMaterial(z33, z34, z35)
    """State 13: Activated: Poison water"""
    return 2
    """State 11: Not started"""
    Label('L1')
    return 0

def event_m10_17_x101(z30=10171205, z37=117000055):
    """[Condition] [Insect Key] Recovery Fountain _ Poisonous
    z30: Bug ID OBJ instance ID
    z37: Windmill burned flag
    """
    """State 0,2: Waiting for insect key activation"""
    CompareObjState(0, z30, 20, 0)
    assert ConditionGroup(0)
    """State 1: Did you remove the poison?"""
    CompareEventFlag(0, z37, 1)
    if ConditionGroup(0):
        """State 3: Bug key activation: recovery"""
        return 0
    else:
        """State 4: Bug key activation: poisonous water"""
        return 1

def event_m10_17_x102(z31=10171310, z33=90, z34=240, z36=2):
    """[Execute] [Insect Key] Recovery Fountain_Poisoned_Recovery
    z31: Instance ID of Recovery OBJ
    z33: Hit group ID
    z34: Grand material ID
    z36: Grand material slot
    """
    """State 0,1: Recovery fountain launch"""
    ChangeObjState(z31, 70)
    assert (GetStateTime() > 1) != 0
    """State 2: Enable grand material recovery"""
    SetGroundMaterial(z33, z34, z36)
    """State 3: Waiting for the end of anime"""
    assert CompareObjStateId(z31, 20, 0)
    """State 4: End state"""
    return 0

def event_m10_17_x103(z32=10171315, z33=90, z34=240, z35=1, z37=117000055):
    """[Execute] [Insect Key] Recovery Fountain _ Poisonous _ Poison water not activated
    z32: Poison water OBJ instance ID
    z33: Hit group ID
    z34: Grand material ID
    z35: Grand material slot
    z37: Windmill burned flag
    """
    """State 0,1: Poison water fountain start"""
    ChangeObjState(z32, 70)
    assert (GetStateTime() > 1) != 0
    """State 2: Activate poison water of Grand Material"""
    SetGroundMaterial(z33, z34, z35)
    """State 3: Wait for poison removal"""
    CompareEventFlag(0, z37, 1)
    assert ConditionGroup(0)
    """State 4: Poison water fountain stop"""
    ChangeObjState(z32, 71)
    assert (GetStateTime() > 1) != 0
    """State 5: Disable ground material poison water"""
    SetGroundMaterial(z33, z34, z35)
    """State 6: Waiting for the end of the poisonous water anime"""
    assert CompareObjStateId(z32, 20, 0)
    """State 7: End state"""
    return 0

def event_m10_17_x104(z32=10171315, z33=90, z34=240, z35=1, z37=117000055):
    """[Execution] [Insect Key] Recovery Fountain _ Poisonous _ Poison water activated
    z32: Poison water OBJ instance ID
    z33: Hit group ID
    z34: Grand material ID
    z35: Grand material slot
    z37: Windmill burned flag
    """
    """State 0,1: Wait for poison removal"""
    CompareEventFlag(0, z37, 1)
    assert ConditionGroup(0)
    """State 2: Poison water fountain stop"""
    ChangeObjState(z32, 71)
    assert (GetStateTime() > 1) != 0
    """State 3: Disable ground material poison water"""
    SetGroundMaterial(z33, z34, z35)
    """State 4: Waiting for the end of the poisonous water anime"""
    assert CompareObjStateId(z32, 20, 0)
    """State 5: End state"""
    return 0

def event_m10_17_x105(z22=147005, z23=311000, z24=200010010, z25=200010020, z26=200010030, z27=200010011,
                      z28=200010021, z29=200010031):
    """[Preset] Enemy character's poison fog damage disabled
    z22: Character ID of sick person
    z23: Knight soldier: Character ID of a riding soldier
    z24: Poison fog (weak) damage ID
    z25: Poison fog (medium) damage ID
    z26: Poison fog (strong) damage ID
    z27: Poison fog (weak) production damage ID
    z28: Poison fog (medium) production damage ID
    z29: Poison fog (strong) production damage ID
    """
    """State 0,1: [Reproduce] Enemy character's poison fog damage disabled_SubState"""
    assert event_m10_17_x106()
    """State 2: [Condition] Enemy character's poison fog damage disabled_SubState"""
    assert event_m10_17_x107()
    """State 3: [Execute] Enemy character's poison fog damage disabled_SubState"""
    assert event_m10_17_x108(z22=z22, z23=z23, z24=z24, z25=z25, z26=z26, z27=z27, z28=z28, z29=z29)
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

def event_m10_17_x108(z22=147005, z23=311000, z24=200010010, z25=200010020, z26=200010030, z27=200010011,
                      z28=200010021, z29=200010031):
    """[Execution] Disabling poison mist damage of enemy characters
    z22: Character ID of sick person
    z23: Knight soldier: Character ID of a riding soldier
    z24: Poison fog (weak) damage ID
    z25: Poison fog (medium) damage ID
    z26: Poison fog (strong) damage ID
    z27: Poison fog (weak) production damage ID
    z28: Poison fog (medium) production damage ID
    z29: Poison fog (strong) production damage ID
    """
    """State 0,1: Disabling poison fog damage"""
    SetDamageImmunityByCharacterId(z22, z24, 1)
    SetDamageImmunityByCharacterId(z22, z25, 1)
    SetDamageImmunityByCharacterId(z22, z26, 1)
    SetDamageImmunityByCharacterId(z23, z24, 1)
    SetDamageImmunityByCharacterId(z23, z25, 1)
    SetDamageImmunityByCharacterId(z23, z26, 1)
    SetDamageImmunityByCharacterId(z22, z27, 1)
    SetDamageImmunityByCharacterId(z22, z28, 1)
    SetDamageImmunityByCharacterId(z22, z29, 1)
    SetDamageImmunityByCharacterId(z23, z27, 1)
    SetDamageImmunityByCharacterId(z23, z28, 1)
    SetDamageImmunityByCharacterId(z23, z29, 1)
    SetDamageImmunityByGeneratorId(5110, 200014020, 1)
    SetDamageImmunityByGeneratorId(5110, 200014030, 1)
    SetDamageImmunityByCharacterId(z22, 200014020, 1)
    SetDamageImmunityByCharacterId(z22, 200014030, 1)
    """State 2: End state"""
    return 0

def event_m10_17_x109():
    """[Reproduction] Floor switch arrow"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x110(z21=_):
    """[Condition] Floor switch tapping arrow
    z21: Switch instance ID
    """
    """State 0,1: Did you get on the switch?"""
    CompareObjState(0, z21, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x111(z20=_):
    """[Execution] Floor switch treadle
    z20: OBJ instance ID to be run
    """
    """State 0,1: Arrow firing: 70"""
    ChangeObjState(z20, 70)
    """State 2: End state"""
    return 0

def event_m10_17_x112(z20=_, z21=_):
    """[Preset] Floor switch arrow
    z20: OBJ instance ID to be run
    z21: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Floor switch treadle _SubState"""
    assert event_m10_17_x109()
    """State 3: [Condition] Floor switch tread arrow _SubState"""
    assert event_m10_17_x110(z21=z21)
    """State 2: [Execution] Floor switch treadle_SubState"""
    assert event_m10_17_x111(z20=z20)
    """State 4: End state"""
    return 0

def event_m10_17_x113(z16=500000, z17=10172110, z18=10171540):
    """[Execution] Iron lattice that can be opened and closed by lever
    z16: Navigation change point ID
    z17: Lever OBJ instance ID
    z18: Iron lattice OBJ instance ID
    """
    """State 0,3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z17, 1)
    """State 1: Iron lattice descending animation playback: 80"""
    ChangeObjState(z18, 80)
    """State 4: Waiting for the descent of the iron grid"""
    CompareObjState(0, z18, 10, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh attribute added"""
    AddNavimeshAttribute(z16, 2)
    """State 5: Enable key guide for lever"""
    DisableObjKeyGuide(z17, 0)
    """State 6: End state"""
    return 0

def event_m10_17_x114(z16=500000, z17=10172110, z18=10171540, z19=10172900):
    """[Preset] Iron lattice that can be opened and closed by levers
    z16: Navigation change point ID
    z17: Lever OBJ instance ID
    z18: Iron lattice OBJ instance ID
    z19: OBJ instance ID for enemy judgment
    """
    """State 0,1: [Reproduction] Iron lattice _SubState that can open and close the enemy with a lever"""
    assert event_m10_17_x85(z18=z18, z17=z17, z16=z16)
    """State 4: [Condition] Iron lattice that can be opened and closed by lever"""
    call = event_m10_17_x86(z17=z17, z19=z19, z18=z18)
    if call.Get() == 0:
        """State 3: [Execution] Iron lattice that can be opened and closed by lever"""
        assert event_m10_17_x87(z16=z16, z17=z17, z18=z18)
    elif call.Get() == 1:
        """State 2: [Execution] Iron lattice that can be opened and closed with a lever_Descent_SubState"""
        assert event_m10_17_x113(z16=z16, z17=z17, z18=z18)
    """State 5: Rerun"""
    return 0

def event_m10_17_x115(z10=10173000, z11=10173001, z12=10173002, z13=10173003, z14=10173004, z15=117000055):
    """[Reproduction] Poison water drop
    z10: Poison water OBJ instance ID_1
    z11: Poison water OBJ instance ID_2
    z12: Poison water OBJ instance ID_3
    z13: Poison water OBJ instance ID_4
    z14: Poison water OBJ instance ID_5
    z15: Windmill burned flag
    """
    """State 0,1: Is the windmill burning and valve operated?"""
    if GetEventFlag(z15) != 0:
        """State 2: Poison water status switching"""
        SetGroundMaterial(20, 240, 1)
        SetGroundMaterial(30, 240, 1)
        SetGroundMaterial(40, 240, 1)
        SetGroundMaterial(50, 240, 1)
        SetGroundMaterial(60, 240, 1)
        SetGroundMaterial(21, 240, 1)
        ChangeObjState(z10, 20)
        ChangeObjState(z11, 20)
        ChangeObjState(z12, 20)
        ChangeObjState(z13, 20)
        ChangeObjState(z14, 20)
        """State 4: End of reproduction"""
        return 1
    else:
        """State 3: End state"""
        return 0

def event_m10_17_x116(z15=117000055):
    """[Condition] Poisonous water drop
    z15: Windmill burned flag
    """
    """State 0,1: Did the windmill burn?"""
    CompareEventFlag(0, z15, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_17_x117(z10=10173000, z11=10173001, z12=10173002, z13=10173003, z14=10173004):
    """[Execution] Poison water drop
    z10: Poison water OBJ instance ID_1
    z11: Poison water OBJ instance ID_2
    z12: Poison water OBJ instance ID_3
    z13: Poison water OBJ instance ID_4
    z14: Poison water OBJ instance ID_5
    """
    """State 0,1: OBJ state transition: poison water"""
    ChangeObjState(z10, 70)
    ChangeObjState(z11, 70)
    ChangeObjState(z12, 70)
    ChangeObjState(z13, 70)
    ChangeObjState(z14, 70)
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
    ChangeObjState(z10, 20)
    ChangeObjState(z11, 20)
    ChangeObjState(z14, 20)
    """State 8: Time elapsed: 2 seconds and a half_2"""
    CompareStateTime(0, 2.5, 2, 2.5)
    assert ConditionGroup(0)
    """State 7: Changed the ground material for poisonous water 3"""
    SetGroundMaterial(50, 240, 1)
    """State 2: Time elapsed: 2 seconds"""
    CompareStateTime(0, 2, 2, 2)
    assert ConditionGroup(0)
    """State 3: Change the state of poison water 4"""
    ChangeObjState(z13, 20)
    """State 5: Time elapsed: 5 seconds and a half"""
    CompareStateTime(0, 5.5, 2, 5.5)
    assert ConditionGroup(0)
    """State 6: Change the state of Poison Water 3"""
    ChangeObjState(z12, 20)
    """State 18: End state"""
    return 0

def event_m10_17_x118(z10=10173000, z11=10173001, z12=10173002, z13=10173003, z14=10173004, z15=117000055):
    """[Preset] Poison water drop
    z10: Poison water OBJ instance ID_1
    z11: Poison water OBJ instance ID_2
    z12: Poison water OBJ instance ID_3
    z13: Poison water OBJ instance ID_4
    z14: Poison water OBJ instance ID_5
    z15: Windmill burned flag
    """
    """State 0,1: [Reproduction] Poison water drop_SubState"""
    call = event_m10_17_x115(z10=z10, z11=z11, z12=z12, z13=z13, z14=z14, z15=z15)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Poisonous water reduction_SubState"""
        assert event_m10_17_x116(z15=z15)
        """State 2: [Execution] Poison water drop_SubState"""
        assert event_m10_17_x117(z10=z10, z11=z11, z12=z12, z13=z13, z14=z14)
    """State 4: End state"""
    return 0

def event_m10_17_x119(z6=100, z7=105440):
    """[Preset] Hunting Forest MAP loading discard
    z6: Judgment hit group ID
    z7: Hunting Forest MAP discard flag
    """
    """State 0,1: [Reproduction] Loading and discarding Hunting Forest MAP_SubState"""
    assert event_m10_17_x120()
    """State 2: [Condition] Reading and discarding Hunting Forest MAP_SubState"""
    call = event_m10_17_x121(z6=z6)
    if call.Get() == 0:
        """State 3: [Execution] Hunting Forest MAP loading discard_flag OFF_SubState"""
        assert event_m10_17_x122(z7=z7, z8=0, z6=z6, z9=0)
    elif call.Get() == 1:
        """State 4: [Execution] Hunting Forest MAP loading discard_flag ON_SubState"""
        assert event_m10_17_x122(z7=z7, z8=1, z6=z6, z9=1)
    """State 5: End state"""
    return 0

def event_m10_17_x120():
    """[Reproduction] Reading and discarding Hunting Forest MAP"""
    """State 0,1: End state"""
    return 0

def event_m10_17_x121(z6=100):
    """[Condition] Reading and discarding Hunting Forest MAP
    z6: Judgment hit group ID
    """
    """State 0,2: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 1: Are you on a hit for judgment?"""
    IsPlayerOnHitGroup(0, z6, 1)
    if ConditionGroup(0):
        """State 3: Flag off"""
        return 0
    else:
        """State 4: Turn on the flag"""
        return 1

def event_m10_17_x122(z7=105440, z8=_, z6=100, z9=_):
    """[Execution] Reading and discarding Hunting Forest MAP
    z7: Hunting Forest MAP discard flag
    z8: Flag ON / OFF
    z6: Judgment hit group ID
    z9: YES / NO for hit judgment
    """
    """State 0,1: Switched flag for discarding hunting forest MAP"""
    SetEventFlag(z7, z8)
    """State 2: Did the condition change condition be met?"""
    IsPlayerInTheMap(0, 0, 0)
    IsPlayerOnHitGroup(0, z6, z9)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_17_x123(z3=_, z4=_, z5=_):
    """[BEST] [Preset] Suspended Poison Poison _ Destruction
    z3: Poisonous OBJ instance ID
    z4: Chain OBJ instance ID
    z5: Destruction judgment point ID
    """
    """State 0,1: [BEST] [Reproduction] Hanging Poison _ Destruction _ SubState"""
    call = event_m10_17_x124(z3=z3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [BEST] [Condition] Suspended poison spider_Destruction_SubState"""
        call = event_m10_17_x126(z3=z3, z4=z4, z5=z5)
        if call.Get() == 1:
            pass
        elif call.Get() == 2:
            """State 5: Rerun"""
            return 1
        elif call.Get() == 0:
            """State 3: [BEST] [Execution] Suspended Poison Spider_Destruction_SubState"""
            assert event_m10_17_x125(z3=z3)
    """State 4: Finish"""
    return 0

def event_m10_17_x124(z3=_):
    """[BEST] [Reproduction] Suspended poison _ destruction
    z3: Poisonous OBJ instance ID
    """
    """State 0,1: Is the cocoon already broken?"""
    if CompareObjStateId(z3, 10, 1):
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Before destruction"""
        return 0

def event_m10_17_x125(z3=_):
    """[BEST] [Execution] Hanging Poison 壺 Destruction
    z3: Poisonous OBJ instance ID
    """
    """State 0,1: Hail destruction"""
    DestroyObj(z3, z3, 0)
    """State 2: Finish"""
    return 0

def event_m10_17_x126(z3=_, z4=_, z5=_):
    """[BEST] [Condition] Suspended poison spider _ destruction
    z3: Poisonous OBJ instance ID
    z4: Chain OBJ instance ID
    z5: Destruction judgment point ID
    """
    """State 0,1: Is the chain descending?"""
    CompareObjState(0, z4, 80, 0)
    CompareObjState(0, z3, 10, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4: Destroyed"""
    return 1
    """State 2: Is the player down while descending?"""
    Label('L0')
    CompareStateTime(8, 1.5, 3, 1.5)
    IsPlayerInsidePoint(8, z5, z5, 1)
    CompareObjState(0, z4, 10, 0)
    if ConditionGroup(0):
        """State 5: Rerun"""
        return 2
    elif ConditionGroup(8):
        """State 3: Destroy the spear"""
        return 0

def event_m10_17_x127(z2=100790):
    """[DC] [Execution] Judgment White Spirit Summon Achievement Judgment
    z2: Summon achievement flag
    """
    """State 0,1: Summon achievement flag ON"""
    SetEventFlag(z2, 1)
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

def event_m10_17_x129(z2=100790):
    """[DC] [Reproduction] Judgment White Spirit Summoning Achievement Judgment
    z2: Summon achievement flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Have you already summoned?"""
        if GetEventFlag(z2) != 0:
            pass
        else:
            """State 3: Waiting for summon"""
            return 0
    """State 4: Finish"""
    return 1

def event_m10_17_x130(z1=600, z2=100790):
    """[DC] [Preset] Guided White Spirit Summoning Achievement Judgment
    z1: White Spirit Generator ID
    z2: Summon achievement flag
    """
    """State 0,1: [DC] [Reproduction] Guidance White Spirit Summon Achievement Judgment_SubState"""
    call = event_m10_17_x129(z2=z2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Judgment white spirit summon achievement determination_SubState"""
        assert event_m10_17_x128(z1=z1)
        """State 2: [DC] [Execute] Guidance White Spirit Summon Achievement Judgment_SubState"""
        assert event_m10_17_x127(z2=z2)
    """State 4: Finish"""
    return 0

def event_m10_17_111092():
    """OBJ: Ladder Shop (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z147=104051, z148=10174000, z149=46, z150=7040)

def event_m10_17_111093():
    """OBJ: Ladder Shop (Tank Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7040:Laddersmith Gilligan
    event_m10_17_x4(z142=117010110, z143=117020111, z144=104050, z145=10174000, z146=111092, npc1=7040)

def event_m10_17_111094():
    """OBJ: Ladder shop (Tankoku valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z128=45, z129=104051)

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

def event_m10_17_111096():
    """OBJ: Ladder Shop (Tank Valley): Ladder Poly Play"""
    """State 0,4: Ladder installation: Poly drama start: Standby"""
    CompareEventFlag(0, 117020117, 1)
    assert ConditionGroup(0)
    """State 1,6: [Lib] Normal poly play_SubState"""
    assert event_m10_17_x0(z151=101710, mode4=0, z152=117000118, z153=1, z154=1)
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

def event_m10_17_111202():
    """OBJ: Dwarf: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z147=104132, z148=10174004, z149=246, z150=7260)

def event_m10_17_111203():
    """OBJ: Dwarf: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7260:Lonesome Gavlan
    event_m10_17_x4(z142=117010160, z143=117020161, z144=104130, z145=10174004, z146=111202, npc1=7260)

def event_m10_17_111204():
    """OBJ: Dwarf (Dwelling Valley): Death Determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z128=245, z129=104132)

def event_m10_17_111205():
    """OBJ: Dwarf (Dwelling Valley): Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_17_x25(z114=104130, z115=102340, z116=102343, z117=117020167, z118=103631)

def event_m10_17_111252():
    """OBJ: Patch (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z147=104172, z148=10174003, z149=66, z150=7440)

def event_m10_17_111253():
    """OBJ: Patch (Pump Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7440:Mild-mannered Pate
    event_m10_17_x4(z142=117010140, z143=117020141, z144=104170, z145=10174003, z146=111252, npc1=7440)

def event_m10_17_111254():
    """OBJ: Patch (dwelling valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z128=65, z129=104172)

def event_m10_17_111255():
    """OBJ: Patch (valley): Appearance determination"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_17_x25(z114=104170, z115=102450, z116=102451, z117=117020147, z118=103671)

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

def event_m10_17_111272():
    """OBJ: Woman Knight (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z147=104193, z148=10174001, z149=91, z150=7520)

def event_m10_17_111273():
    """OBJ: Woman Knight (Tank Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_17_x4(z142=117010120, z143=117020121, z144=104190, z145=10174001, z146=111272, npc1=7520)

def event_m10_17_111274():
    """OBJ: Woman Knight (Tank Valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z128=90, z129=104193)

def event_m10_17_111275():
    """OBJ: Woman Knight (Tank Valley): Appearance Judgment"""
    """State 0,1: [Lib] NPC: Woman Knight: Appearance Judgment_SubState"""
    event_m10_17_x6(z130=102480, z131=102482, z132=102483, z133=102486, z134=102491, z135=102485, z136=102487,
                    z137=102488)

def event_m10_17_111342():
    """OBJ: Material Store (Tank Valley): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_17_x1(z147=104261, z148=10174002, z149=196, z150=7620)

def event_m10_17_111343():
    """OBJ: Material Store (Dwelling Valley): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7620:Stone Trader Chloanne
    event_m10_17_x4(z142=117010150, z143=117020151, z144=104260, z145=10174002, z146=111342, npc1=7620)

def event_m10_17_111344():
    """OBJ: Material shop (Tank valley): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_17_x7(z128=195, z129=104261)

def event_m10_17_112010():
    """OBJ: Sun altar (pledge event)"""
    """State 0,1: [Lib] OBJ Pledge: Initial _SubState"""
    event_m10_17_x37(z105=10173250, z106=117020170)

def event_m10_17_118100():
    """Multi-use NPC: Swordsman (Male): White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_17_x51(z87=556)

def event_m10_17_118110():
    """Multi-use NPC: Hint NPC: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_17_x51(z87=600)

def event_m10_17_118120():
    """Multi-use NPC: Test: Koshiro phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_17_x51(z87=605)

def event_m10_17_120000():
    """Trophy: A brilliant pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_17_x56(z83=117020171, z84=18)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_17_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_17_x56(z83=117020129, z84=33)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_17_4000000():
    """[BEST] Hanging poison trap 01_ destruction"""
    """State 0,3: [BEST] [Preset] Suspended Poison _ Destruction _ SubState"""
    call = event_m10_17_x123(z3=10173550, z4=10173500, z5=6000000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_17_4001000():
    """[BEST] Suspended Poison 02_Destruction"""
    """State 0,3: [BEST] [Preset] Suspended Poison _ Destruction _ SubState"""
    call = event_m10_17_x123(z3=10173560, z4=10173510, z5=6001000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_17_4002000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_17_x64(z63=117020001, z64=14, z65=117000002, z66=6, z67=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_17_x69(z71=80000000, z72=0, z73=5, z74=935, val2=1, z75=10, z76=80000001, z77=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_17_x69(z71=80000100, z72=0, z73=5, z74=935, val2=2, z75=10, z76=80000101, z77=80000199)
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m10_17_x69(z71=80000200, z72=0, z73=5, z74=935, val2=3, z75=10, z76=80000201, z77=80000299)
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert event_m10_17_x69(z71=80000300, z72=0, z73=5, z74=935, val2=4, z75=10, z76=80000301, z77=80000399)
        """State 8: [Lib] [DC] [Preset] Wanderer_Generation_5_SubState"""
        assert event_m10_17_x69(z71=80000400, z72=0, z73=5, z74=935, val2=5, z75=10, z76=80000401, z77=80000499)
        """State 9: [Lib] [DC] [Preset] Wanderer_Generation_6_SubState"""
        assert event_m10_17_x69(z71=80000500, z72=0, z73=5, z74=935, val2=6, z75=10, z76=80000501, z77=80000599)
        """State 2: Start flag ON"""
        SetEventFlag(117020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4002010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_17_x72(z68=117000002, z69=935, mode1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4003000():
    """[DC] Liberation of dead workers in cages_way 1"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173310, z39=117010020)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4003010():
    """[DC] Liberation of dead workers in cages_way 2"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173311, z39=117010021)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4003020():
    """[DC] Liberation of dead workers in cages 3"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173312, z39=117010022)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4003030():
    """[DC] Liberation of dead workers in cages 4"""
    """State 0,2: [Preset] Worker release of dead dead in cage_SubState"""
    assert event_m10_17_x95(z38=10173313, z39=117010023)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4004000():
    """[DC] Guided white spirit summon achievement achievement judgment"""
    """State 0,2: [DC] [Preset] Guidance White Spirit Summon Achievement Judgment_SubState"""
    assert event_m10_17_x130(z1=600, z2=100790)
    """State 1: Finish"""
    EndMachine()

def event_m10_17_4031000():
    """[DC] NPC White Spirit_Gesture Management_Naga"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_17_x77(z60=117000091, z61=801, z62=117020092)
    """State 1: Finish"""
    EndMachine()

