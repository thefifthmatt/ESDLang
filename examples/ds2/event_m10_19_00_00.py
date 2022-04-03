# -*- coding: utf-8 -*-
def event_m10_19_1000():
    """Scaffold moving up and down with lever"""
    """State 0,2: [Preset] Scaffolding up and down with lever_SubState"""
    assert event_m10_19_x121(z68=10191100, z69=10191010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_2000():
    """One-way door from the bonfire room"""
    """State 0,2: [Lib] Area specified door unlocked_SubState"""
    assert event_m10_19_x0(z166=0, z167=200000, z168=19020100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_3000():
    """[Insect Key] For Recovery Fountain _01"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_19_x13(z145=10191501)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_3010():
    """[Insect Key Activation] Recovery Fountain_01"""
    """State 0,2: [Lib] [Preset] Recovery Fountain_SubState"""
    assert event_m10_19_x23(z141=10191501, z142=20, z143=240, z144=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4000():
    """[Insect Key] For Recovery Fountain _02"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_19_x13(z145=10191502)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4010():
    """[Insect Key Activation] Recovery Fountain_02"""
    """State 0,2: [Lib] [Preset] Recovery Fountain_SubState"""
    assert event_m10_19_x23(z141=10191502, z142=10, z143=240, z144=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_5000():
    """Bridge descending with lever"""
    """State 0,3: [Preset] Bridge descending with lever_SubState"""
    call = event_m10_19_x164(z27=10191300, z28=10191002, z29=10191000)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_19_6000():
    """Burning furnace_shutter opening / closing"""
    """State 0,2: [Preset] Burning furnace_Shutter and damage_SubState"""
    assert (event_m10_19_x129(z58=10191550, z59=10191610, z60=600000, z61=600010, z62=10191615, z63=10191620,
            z64=600020))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_6010():
    """Burning furnace _ flame when opening the door"""
    """State 0,3: [Preset] Burning furnace _ Flame when opening the door _ SubState"""
    call = event_m10_19_x140(z19=10191610, z20=10190402, z21=10191600)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_19_6020():
    """Burning furnace"""
    """State 0,3: [Preset] Burning furnace _ Flame when opening the door _ SubState"""
    call = event_m10_19_x140(z19=10191610, z20=10190400, z21=10191605)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_19_7000():
    """Molten iron pot 01"""
    """State 0,2: [Preset] Floor switch_Fused iron_SubState"""
    assert event_m10_19_x138(z47=10191700, z48=10191050, z49=10191710, z50=30, z51=240)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_7010():
    """Molten iron pot 02"""
    """State 0,2: [Preset] Floor switch_Fused iron_SubState"""
    assert event_m10_19_x138(z47=10191701, z48=10191051, z49=10191711, z50=30, z51=241)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_7020():
    """Molten iron pot 03"""
    """State 0,2: [Preset] Floor switch_Fused iron_SubState"""
    assert event_m10_19_x138(z47=10191702, z48=10191052, z49=10191712, z50=30, z51=242)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_8000():
    """Boss: Demon Knight Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_19_x6(flag19=119000081, z150=800000, z151=800000, z152=102, z153=1019000, z154=119020080,
            mode7=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_8010():
    """Flames linked to boss actions"""
    """State 0,2: [Preset] Flame _SubState linked to the behavior of the boss"""
    assert event_m10_19_x143(z41=806, z42=71, z43=70, z44=10192200, z45=10192201, z46=93050010, flag7=119000081)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_8020():
    """Vegrant generation determination"""
    """State 0,2: [Preset] Vegrant generation determination_SubState"""
    assert event_m10_19_x152(z34=119020010, flag6=119020012, z35=119000081)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_8030():
    """Vegrant removal judgment"""
    """State 0,2: [Preset] Vegrant defeat determination_SubState"""
    assert event_m10_19_x172(z22=5000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_9000():
    """Lever that stops all flame images"""
    """State 0,2: [Reproduction] Lever that stops all flame images _SubState"""
    call = event_m10_19_x130()
    if call.Get() == 0:
        """State 4: [Condition] Lever that stops all flame images _OFF to ON_SubState"""
        assert event_m10_19_x131(z55=10191350, z56=74, z57=30)
        """State 3: [Execute] Lever to stop all flame images"""
        assert event_m10_19_x132(z53=119000040, z54=1)
    elif call.Get() == 1:
        """State 5: [Condition] Lever that stops all flame images _ON to OFF_SubState"""
        assert event_m10_19_x131(z55=10191350, z56=84, z57=10)
        """State 6: [Execute] Lever to stop all flame images_Turn flag OFF_SubState"""
        assert event_m10_19_x132(z53=119000040, z54=0)
    """State 1: End (re-executable)"""
    RestartMachine()
    Quit()

def event_m10_19_10000():
    """Bell guard_bell lever"""
    """State 0,3: [Lib] [Preset] Bell guard_Lever that rings the bell_SubState"""
    call = event_m10_19_x58(z96=10191011, z97=10191200, val2=10191210, z98=10191220, z99=10191230, z100=10191290,
                            z101=10190641, z102=1000000)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m10_19_10010():
    """Kanemori_Receiving the bell net"""
    """State 0,2: [Lib] [Preset] Kanemori_Net reception_SubState"""
    assert event_m10_19_x50(z107=10010, mode3=1, mode4=1, mode5=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_10020():
    """Jewel guard"""
    """State 0,2: [Lib] [Preset] Kanemori _ Judgment Spirit Lever Use Decision_SubState"""
    assert event_m10_19_x57(z106=10191011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_11000():
    """[Insect key] For hidden door 1_01"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_19_x13(z145=10191500)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_11010():
    """[Insect key activation] Hidden door 1_01"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_19_x27(z139=10191500, val3=10190000, z140=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_11020():
    """[Insect key] Hidden door_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z131=10191410, z132=20, z133=1102000, z134=0, z135=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_12000():
    """Falling scaffold 01_ back left"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z65=10191752, z66=10191053, z67=1200000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_12010():
    """Falling scaffold 02_back right"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z65=10191753, z66=10191054, z67=1201000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_12020():
    """Falling scaffold 03_ right front"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z65=10191751, z66=10191055, z67=1202000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_12030():
    """Falling scaffold 04_left front"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z65=10191750, z66=10191056, z67=1203000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_13000():
    """Attaching a flame in two directions_attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_19_x31(z136=10191100, z137=150, z138=10191650)
    """State 3: [Lib] [Preset] OBJ attach_2_SubState"""
    assert event_m10_19_x31(z136=10191100, z137=151, z138=10191651)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_14000():
    """Disabling damage"""
    """State 0,1: Disabling the damage floor"""
    SetDamageImmunityByGeneratorId(807, 200016010, 1)
    SetDamageImmunityByGeneratorId(807, 200016020, 1)
    SetDamageImmunityByGeneratorId(807, 200016030, 1)
    SetDamageImmunityByCharacterId(306008, 200016010, 1)
    SetDamageImmunityByCharacterId(306008, 200016020, 1)
    SetDamageImmunityByCharacterId(306008, 200016030, 1)
    SetDamageImmunityByCharacterId(306009, 200016010, 1)
    SetDamageImmunityByCharacterId(306009, 200016020, 1)
    SetDamageImmunityByCharacterId(306009, 200016030, 1)
    SetDamageImmunityByCharacterId(319009, 200016010, 1)
    SetDamageImmunityByCharacterId(319009, 200016020, 1)
    SetDamageImmunityByCharacterId(319009, 200016030, 1)
    SetDamageImmunityByCharacterId(306008, 200011010, 1)
    SetDamageImmunityByCharacterId(306008, 200011020, 1)
    SetDamageImmunityByCharacterId(306008, 200011030, 1)
    SetDamageImmunityByCharacterId(306009, 200011010, 1)
    SetDamageImmunityByCharacterId(306009, 200011020, 1)
    SetDamageImmunityByCharacterId(306009, 200011030, 1)
    SetDamageImmunityByCharacterId(319009, 200011010, 1)
    SetDamageImmunityByCharacterId(319009, 200011020, 1)
    SetDamageImmunityByCharacterId(319009, 200011030, 1)
    SetDamageImmunityByCharacterId(694005, 200011010, 1)
    SetDamageImmunityByCharacterId(897000, 200011010, 1)
    SetDamageImmunityByCharacterId(897501, 200011010, 1)
    SetDamageImmunityByCharacterId(898000, 200011010, 1)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_19_15000():
    """Boss: Molten demon battle"""
    """State 0,3: Waiting for white door"""
    CompareObjState(0, 10190610, 100, 0)
    assert ConditionGroup(0)
    """State 6: Host?"""
    if IsGuest() != 1:
        """State 4: Auto save prohibited"""
        DisableAutoSave(1)
    else:
        pass
    """State 2: Is the poly drama replay event over?"""
    assert EventEnded(15010) != 0
    """State 8: [BEST] [Lib] [Preset] Molten Iron Demon Battle_SubState"""
    assert (event_m10_19_x193(flag1=119000086, z3=1500000, z4=1500000, z5=101, z6=1019010, z7=119020085,
            mode1=0))
    """State 7: Host? _2"""
    if IsGuest() != 1:
        """State 5: Auto save enabled"""
        DisableAutoSave(0)
    else:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_15010():
    """Boss: Molten Iron Demon_Poly Play"""
    """State 0,2: [Preset] Molten Iron Daemon_Poly Play_SubState"""
    assert event_m10_19_x188(z9=10190610, z10=101910, flag2=119000087, z11=1501000, z12=1, z13=119000088)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_15020():
    """Boss: Molten Iron Daemon"""
    """State 0,2: Wait for damage invalid event to end"""
    assert EventEnded(14000) != 0
    """State 3: [Preset] Molten iron daemon_Initial location change_SubState"""
    assert event_m10_19_x153(z30=119000087, z31=807, z32=1502000, z33=2, flag5=119000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_16000():
    """Connection flag ON"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_19_x39(z129=105420, z130=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_17000():
    """Bridges destroyed by enemies_Navigation change"""
    """State 0,2: [Preset] Bridge destroyed by enemies _SubState"""
    assert event_m10_19_x165(z23=10194999, z24=20, z25=1700000, z26=119020030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_19000():
    """Guillotine door"""
    """State 0,2: [Preset] Guillotine Door_SubState"""
    assert event_m10_19_x148(z37=10191020, z38=10191021, z39=10191110, z40=1900000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_20000():
    """End bonfire_molten iron"""
    """State 0,2: [Lib] [Preset] End special bonfire_SubState"""
    assert event_m10_19_x67(z105=10190700, flag17=100360)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_23000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z131=10191404, z132=20, z133=2300000, z134=0, z135=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_23010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z131=10191406, z132=20, z133=2301000, z134=0, z135=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_24000():
    """Navimesh changes due to varistor destruction"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z131=10192000, z132=20, z133=2400000, z134=0, z135=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_60000():
    """Pledge: Kanemori_Contribution UP"""
    """State 0,2: Has the generation determination event ended?"""
    assert EventEnded(60010) != 0
    """State 3: [Preset] Pledge: Kanemori_Contribution UP_SubState"""
    assert event_m10_19_x183(z14=7007, flag3=119020018, z15=119020014)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_60010():
    """Pledge: Kanemori_Contribution UP_Intruder Generation Judgment"""
    """State 0,2: [Preset] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_SubState"""
    assert event_m10_19_x179(z17=119020014, flag4=119020016)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_80000():
    """After the fire of rebirth 01_ Boss Demon Knight, a one-way door room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z126=1019000, z127=1019099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_81000():
    """Regenerative fire 02_Stairs under the entrance bridge"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z126=1019100, z127=1019199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_82000():
    """Reproduction Fire 03_Head of a Giant Cow"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z126=1019200, z127=1019299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_82010():
    """Shop lineup expansion_molten iron demon"""
    """State 0,2: [Lib] [Preset] Shop Lineup_SubState"""
    # bonfire:19660:Eygil's Idol
    assert event_m10_19_x72(bonfire2=19660, z103=119000086, flag15=101101)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_83000():
    """Reproduction flame 04_ depression in front of Kanemori area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z126=1019300, z127=1019399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_90000():
    """Trophy_Lost Iron"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_19_x68(flag16=100360, z104=7)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_x0(z166=0, z167=200000, z168=19020100):
    """[Lib] Area designated door unlocked
    z166: Text ID when opened
    z167: Point ID
    z168: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z167, 0, z166, 1101, z168, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x1(z164=0, z165=0, z94=_, z95=_):
    """[Lib] Warp between maps after poly play
    z164: Pre-warp poly play ID
    z165: Poly Play ID after Warp
    z94: Map ID
    z95: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z164, z165, z94, z95, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_19_x2(z160=_, z161=_, z162=_, z163=_):
    """[Lib] NPC: Grave Placement: General purpose
    z160: Death map: Global event flag
    z161: Tomb: OBJ instance ID
    z162: Tomb move to: Generator ID
    z163: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z160, 1)
    IsGraveGeneratable(8, z163, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z161, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z161, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_19_x3(z157=_, z158=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z157: Global: death flag
    z158: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z158, 10, 0)
    CompareObjState(1, z158, 20, 0)
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
    IsObjSearched(0, z158)
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

def event_m10_19_x4(z155=_, z156=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z155: Area other flags: Ghost appearance
    z156: Area other flags: Conversation start
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
    SetEventFlag(z155, 1)
    CompareEventFlag(0, z155, 1)
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
    SetEventFlag(z156, 1)
    CompareEventFlag(0, z156, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_19_x5(z155=_, z156=_, z157=_, z158=_, z159=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z155: Ghost Appearance: Area Other Flag
    z156: Conversation start: Area and other flags
    z157: Death: Global event flag
    z158: Tomb: OBJ instance ID
    z159: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z159, 1, 0)
    CompareEventFlag(9, z155, 1)
    CompareObjState(9, z158, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z156, 1)
        CompareEventFlag(0, z156, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_19_x3(z157=z157, z158=z158, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_19_x4(z155=z155, z156=z156, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_19_x6(flag19=119000081, z150=800000, z151=800000, z152=102, z153=1019000, z154=119020080,
                    mode7=0):
    """[Lib] [Preset] Boss Battle Start
    flag19: Boss destruction flag
    z150: Start point ID
    z151: End point ID
    z152: Sound ID
    z153: Boss Battle ID
    z154: Other flags for logic
    mode7: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_19_x7(flag1=flag19)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_19_x8(z3=z150, z4=z151)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_19_x9(z152=z152, z153=z153, z154=z154)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_19_x10()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_19_x11(z6=z153)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_19_x12(z5=z152, z6=z153, z7=z154, mode1=mode7)
    """State 7: End state"""
    return 0

def event_m10_19_x7(flag1=_):
    """[Reproduction] Boss Battle_Start
    flag1: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag1) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_19_x8(z3=_, z4=_):
    """[Condition] Boss Battle_Start
    z3: Start point ID
    z4: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z3, z4, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z3, z4, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x9(z152=102, z153=1019000, z154=119020080):
    """[Execution] Boss Battle_Start
    z152: Sound ID
    z153: Boss Battle ID
    z154: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z152)
    """State 1: Boss battle start notification"""
    StartBossFight(z153)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z154, 1)
    """State 4: End state"""
    return 0

def event_m10_19_x10():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x11(z6=_):
    """[Condition] Boss Battle_End Judgment
    z6: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z6, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x12(z5=_, z6=_, z7=_, mode1=0):
    """[Execute] Boss Battle_End
    z5: Sound ID
    z6: Boss Battle ID
    z7: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z7, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z6)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z5)
    """State 5: End state"""
    return 0

def event_m10_19_x13(z145=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z145: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_19_x14(z145=z145)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_19_x21(z145=z145)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_19_x22()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_19_x15(z145=z145, mode6=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_19_x16(z145=z145, z147=38, z148=3, z149=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_19_x17(z145=z145, z146=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_19_x14(z145=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z145: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z145, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z145, 10)
        assert CompareObjStateId(z145, 10, 0)
    elif CompareObjStateId(z145, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z145, 74, 1) and CompareObjStateId(z145, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_19_x15(z145=_, mode6=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z145: Object instance ID
    mode6: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z145)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode6) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_19_x16(z145=_, z147=38, z148=3, z149=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z145: Object instance ID
    z147: Key guide type
    z148: Event action
    z149: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z145, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z145, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z145, 30)
        assert CompareObjStateId(z145, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z145, z147, z148)
        assert PlayerIsInEventAction(z148) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z148, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z145, 74, 0)
        CompareObjState(1, z145, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z149)
            assert CompareObjStateId(z145, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z145, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_x17(z145=_, z146=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z145: Object instance ID
    z146: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z145, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_19_x18(z141=_, z142=_, z143=240, z144=1):
    """[Reproduction] Spring of recovery
    z141: OBJ instance ID of the bug key
    z142: Hit group ID
    z143: Replacement GMID
    z144: Switching GM slot
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z141, 20, 0):
        """State 2: Water OBJ: OBJ state transition: 20"""
        ChangeOwnObjState(20)
        """State 3: Enable recovery"""
        SetGroundMaterial(z142, z143, z144)
        """State 4: Activated"""
        return 0
    else:
        """State 5: Not running"""
        return 1

def event_m10_19_x19(z141=_):
    """[Condition] Spring of recovery
    z141: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z141, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x20(z142=_, z143=240, z144=1):
    """[Execution] Recovery Fountain
    z142: Hit group ID
    z143: Replacement GMID
    z144: Switching GM slot
    """
    """State 0,1: Water OBJ: OBJ state transition: 70"""
    ChangeOwnObjState(70)
    assert (GetStateTime() > 1) != 0
    """State 2: Enable recovery"""
    SetGroundMaterial(z142, z143, z144)
    """State 3: Waiting for the end of anime"""
    assert CompareOwnObjStateId(20, 0)
    """State 4: End state"""
    return 0

def event_m10_19_x21(z145=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z145: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z145, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x22():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x23(z141=_, z142=_, z143=240, z144=1):
    """[Lib] [Preset] Recovery Fountain
    z141: OBJ instance ID of the bug key
    z142: Hit group ID
    z143: Replacement GMID
    z144: Switching GM slot
    """
    """State 0,1: [Reproduction] Recovery Fountain_SubState"""
    call = event_m10_19_x18(z141=z141, z142=z142, z143=z143, z144=z144)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Condition] Recovery Fountain_SubState"""
        assert event_m10_19_x19(z141=z141)
        """State 2: [Execution] Recovery Fountain_SubState"""
        assert event_m10_19_x20(z142=z142, z143=z143, z144=z144)
    """State 4: End state"""
    return 0

def event_m10_19_x24(z139=10191500, val3=10190000):
    """[Reproduction] Hidden door 1_face SFX
    z139: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z139, 20, 0):
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

def event_m10_19_x25(z139=10191500):
    """[Conditions] Hidden door 1_Face SFX
    z139: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z139, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x26(z139=10191500, val3=10190000, z140=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z139: OBJ instance ID of the bug key
    val3: Event light ID
    z140: Light fade time
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
        SetPointLightEnabled(val3, 1, z140)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_19_x27(z139=10191500, val3=10190000, z140=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z139: OBJ instance ID of the bug key
    val3: Event light ID
    z140: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_19_x24(z139=z139, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_19_x25(z139=z139)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_19_x26(z139=z139, val3=val3, z140=z140, val4=val4)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_19_x28():
    """[Lib] [Reproduction] OBJ attach_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x29():
    """[Lib] [Condition] OBJ attach_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x30(z136=_, z137=_, z138=_):
    """[Lib] [execute] OBJ attach
    z136: Parent OBJ instance ID
    z137: Parent Damipoli ID
    z138: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z136, z137, z138)
    """State 2: End state"""
    return 0

def event_m10_19_x31(z136=_, z137=_, z138=_):
    """[Lib] [Preset] OBJ attach
    z136: Parent OBJ instance ID
    z137: Parent Damipoli ID
    z138: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m10_19_x28()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m10_19_x29()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m10_19_x30(z136=z136, z137=z137, z138=z138)
    """State 4: End state"""
    return 0

def event_m10_19_x32(z131=_, z132=20, z133=_, z134=0, z135=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z131: Object instance ID
    z132: OBJ state ID
    z133: Navimesh switching point ID
    z134: Additional attributes
    z135: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_19_x33(z131=z131, z132=z132, z133=z133, z135=z135, z134=z134)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_19_x34(z131=z131, z132=z132, z133=z133)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_19_x35(z131=z131, z132=z132, z133=z133, z134=z134, z135=z135)
    """State 4: End state"""
    return 0

def event_m10_19_x33(z131=_, z132=20, z133=_, z135=2, z134=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z131: Target OBJ instance ID
    z132: Target OBJ state ID
    z133: Navimesh switching point ID
    z135: Additional attributes
    z134: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z131, z132, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z133, z135)
        DeleteNavimeshAttribute(z133, z134)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_19_x34(z131=_, z132=20, z133=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z131: Target OBJ instance ID
    z132: Target OBJ state ID
    z133: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z131, z132, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x35(z131=_, z132=20, z133=_, z134=0, z135=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z131: Target OBJ instance ID
    z132: Target OBJ state ID
    z133: Navimesh switching point ID
    z134: Additional attributes
    z135: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z133, z134)
    DeleteNavimeshAttribute(z133, z135)
    """State 2: End state"""
    return 0

def event_m10_19_x36():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x37():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x38(z129=105420, z130=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z129: Global event flag for connection
    z130: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z129, z130)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z129, z130)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_19_x39(z129=105420, z130=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z129: Global event flag for connection
    z130: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_19_x36()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_19_x37()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_19_x38(z129=z129, z130=z130)
    """State 4: End state"""
    return 0

def event_m10_19_x40(z128=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z128: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z128)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_19_x41():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x42(z126=_, z127=_):
    """[Lib] [execute] Rebirth fire
    z126: Flag start ID
    z127: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z126, z127, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x43():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x44(z126=_, z127=_):
    """[Lib] [Preset] Rebirth
    z126: Flag start ID
    z127: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_19_x41()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_19_x43()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_19_x42(z126=z126, z127=z127)
    """State 4: End state"""
    return 0

def event_m10_19_x45(z122=119000081, z123=102498, z124=204, z125=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z122: Defeat Boss 1: Area and other flags
    z123: Summon Achievement: Global Event Flag
    z124: Summon achievement count: global variable
    z125: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z123, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z122, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z124, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z124, NpcInfoValue(z125, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z123, 1)
                CompareEventFlag(0, z123, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_19_x46(z118=_, z119=_, z120=0, z121=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z118: Summon range
    z119: Generator ID
    z120: Appearance: Minimum time
    z121: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z118, z118, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z120, 3, z121)
        IsPlayerInsidePoint(1, z118, z118, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z119)
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

def event_m10_19_x47(z114=10000000, z115=570, z116=0, z117=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z114: Summon range
    z115: Generator ID
    z116: Appearance: Minimum time
    z117: Appearance: Maximum time
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
            DeleteNpcPhantom(z115)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z114, z114, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z116, 3, z117)
                IsPlayerInsidePoint(1, z114, z114, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z115)
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

def event_m10_19_x48(flag18=_, z113=_):
    """[Lib] [Preset] Get trophy
    flag18: Acquisition trigger_other flags
    z113: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag18) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag18, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z113)
    """State 4: End state"""
    return 0

def event_m10_19_x49(z108=102501, z109=576, z110=104190, z111=103690, z112=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z108: White Phantom can appear: Global event flag
    z109: White Phantom: Generator ID
    z110: Death: Global event flag
    z111: Hostile: Global event flag
    z112: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z109)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z110, 1)
        CompareEventFlag(1, z111, 1)
        CompareEventFlag(2, z108, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z109)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z110, 1)
            CompareEventFlag(1, z111, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z109)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z110, 1)
            CompareEventFlag(1, z111, 1)
            HasNpcPhantomSpawned(2, z109, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z109, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z109)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_19_x50(z107=10010, mode3=1, mode4=1, mode5=1):
    """[Lib] [Preset] Kanemori_Net reception
    z107: Event sound ID for bell
    mode3: Wait 1 after SE playback
    mode4: Wait 2 after SE playback
    mode5: Wait 3 after playing SE
    """
    """State 0,1: [Lib] [Reproduction] Kanemori_Net reception_SubState"""
    assert event_m10_19_x51()
    """State 3: [Lib] [Conditions] Kanemori_Net reception_SubState"""
    assert event_m10_19_x52()
    """State 2: [Lib] [Execution] Kanemori_Net reception_SubState"""
    assert event_m10_19_x53(z107=z107, mode3=mode3, mode4=mode4, mode5=mode5)
    """State 4: End state"""
    return 0

def event_m10_19_x51():
    """[Lib] [Reproduction] Kanemori_Net reception"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x52():
    """[Lib] [Conditions] Kanemori_Net reception"""
    """State 0,1: Waiting for reception: If a host dies in a multiplayer, it will not be played back"""
    IsBellKeeperRingingHistoryCleared(8, 1)
    IsHostDead(8, 0)
    IsBellKeeperRingingHistoryCleared(9, 1)
    IsHostDead(9, 1)
    IsMultiplayer(9, 1, 0)
    if ConditionGroup(9):
        """State 2: Have you finished multiplayer?"""
        IsMultiplayer(0, 0, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        pass
    """State 3: Reception: Bell ringing process"""
    return 0

def event_m10_19_x53(z107=10010, mode3=1, mode4=1, mode5=1):
    """[Lib] [Execution] Kanemori_Net reception_Playback
    z107: Event sound ID for bell
    mode3: Wait 1 after SE playback
    mode4: Wait 2 after SE playback
    mode5: Wait 3 after playing SE
    """
    """State 0,1: Ring the bell: first time"""
    PlaySoundAtPoint(z107)
    assert (GetStateTime() > mode3) != 0
    """State 4: Ring the bell: second time"""
    PlaySoundAtPoint(z107)
    assert (GetStateTime() > mode4) != 0
    """State 5: Ring the bell: 3rd time"""
    PlaySoundAtPoint(z107)
    assert (GetStateTime() > mode5) != 0
    """State 2: Clear reception history"""
    ClearBellKeeperRingingHistory()
    """State 3: Clear confirmation of received history"""
    IsBellKeeperRingingHistoryCleared(0, 0)
    assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_19_x54(z106=10191011):
    """[Lib] [reproduction] Kanemori _ judgment of lever use of Kanemori spirit
    z106: Lever OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 4: Host: Exit"""
        return 1
    else:
        """State 2: Disable key guide"""
        DisableObjKeyGuide(z106, 1)
        """State 3: Guest: Spirit guard"""
        return 0

def event_m10_19_x55():
    """[Lib] [Conditions] Kanemori _ Judgment spirit lever usage judgment"""
    """State 0,1: Has the host died?"""
    IsHostDead(0, 1)
    assert ConditionGroup(0)
    """State 2: Bell guard spirit: lever operation possible"""
    return 0

def event_m10_19_x56(z106=10191011):
    """[Lib] [Execution] Kanemori _ Judgment Spirit use lever judgment
    z106: Lever OBJ instance ID
    """
    """State 0,1: Activate key guide"""
    DisableObjKeyGuide(z106, 0)
    """State 2: Finish"""
    return 0

def event_m10_19_x57(z106=10191011):
    """[Lib] [Preset] Kanemori _ Judgment Spirit's lever usage judgment
    z106: Lever OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] Kanemori _ Jerusalem Spirit Lever Use Judgment_SubState"""
    call = event_m10_19_x54(z106=z106)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Conditions] Kanemori_Bellguard spirit lever usage judgment_SubState"""
        assert event_m10_19_x55()
        """State 2: [Lib] [Execution] Kanemori_Legend of lever guard_SubState"""
        assert event_m10_19_x56(z106=z106)
    """State 4: Finish"""
    return 0

def event_m10_19_x58(z96=10191011, z97=10191200, val2=10191210, z98=10191220, z99=10191230, z100=10191290,
                     z101=10190641, z102=1000000):
    """[Lib] [Preset] Bell guard_bell lever
    z96: Lever_OBJ instance ID
    z97: Bell 1_OBJ instance ID
    val2: Bell 2_OBJ instance ID
    z98: Bell 3_OBJ instance ID
    z99: Bell 4_OBJ instance ID
    z100: Door OBJ instance ID
    z101: White door OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Bell guard_Lever that bell rings_SubState"""
    call = event_m10_19_x59(z100=z100, z101=z101, z102=z102)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        Goto('L0')
    """State 3: [Lib] [Conditions] Bell guard_Lever that rings bell_SubState"""
    call = event_m10_19_x60(z96=z96)
    if call.Get() == 0:
        """State 4: [Lib] [execution] bell guard_bell lever_host_SubState"""
        assert (event_m10_19_x61(z96=z96, z97=z97, val2=val2, z98=z98, z99=z99, z100=z100, z101=z101,
                z102=z102))
    elif call.Get() == 1:
        """State 2: [Lib] [execution] bell guard_bell lever_guest_SubState"""
        assert event_m10_19_x62(z96=z96, z97=z97, val2=val2, z98=z98, z99=z99)
    """State 7: Rerun"""
    return 0
    """State 6: [Lib] [Conditions] Bell guard_Lever that rings bell_Guest_SubState"""
    Label('L0')
    assert event_m10_19_x73(z100=z100)
    """State 5: [Lib] [Execution] Bell guard_Lever that bell rings_Navigation change_SubState"""
    assert event_m10_19_x74(z100=z100, z102=z102)
    """State 8: Guest termination"""
    return 1

def event_m10_19_x59(z100=10191290, z101=10190641, z102=1000000):
    """[Lib] [reproduction] bell guard _ bell ringing lever
    z100: Door OBJ instance ID
    z101: White door OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,3: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is the door open?"""
    if CompareObjStateId(z100, 10, 0):
        """State 2: White door key guide disabled"""
        DisableWhiteDoorKeyGuide(z101, 1)
    else:
        """State 4: Navimesh change: passable"""
        DeleteNavimeshAttribute(z102, 2)
    """State 5: host"""
    return 0
    """State 6: Guest termination"""
    Label('L0')
    return 1

def event_m10_19_x60(z96=10191011):
    """[Lib] [Conditions] Bell guard_bell lever
    z96: OBJ instance ID of the lever
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z96, 74, 0)
    CompareObjState(0, z96, 84, 0)
    SetConditionGroup(8, 0)
    IsHostDead(8, 0)
    CompareObjState(1, z96, 74, 0)
    CompareObjState(1, z96, 84, 0)
    SetConditionGroup(9, 1)
    IsHostDead(9, 1)
    if ConditionGroup(8):
        """State 2: Host is alive: Host processing"""
        return 0
    elif ConditionGroup(9):
        """State 3: Host dies: guest processing"""
        return 1

def event_m10_19_x61(z96=10191011, z97=10191200, val2=10191210, z98=10191220, z99=10191230, z100=10191290,
                     z101=10190641, z102=1000000):
    """[Lib] [Execution] Kanemori_Lever that rings the bell_Host
    z96: Lever_OBJ instance ID
    z97: Bell 1_OBJ instance ID
    val2: Bell 2_OBJ instance ID
    z98: Bell 3_OBJ instance ID
    z99: Bell 4_OBJ instance ID
    z100: Door OBJ instance ID
    z101: White door OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z96, 1)
    """State 9: Ringing bell judgment"""
    if (not val2) != 0:
        """State 10: Ring bell 1"""
        ChangeObjState(z97, 70)
        """State 8: Bell 1 animation playback judgment"""
        CompareObjState(0, z97, 70, 0)
        assert ConditionGroup(0)
        """State 4: Bell 1 animation end"""
        CompareObjState(0, z97, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z97, 70)
        ChangeObjState(val2, 70)
        ChangeObjState(z98, 70)
        ChangeObjState(z99, 70)
        """State 11: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z97, 70, 0)
        CompareObjState(0, val2, 70, 0)
        CompareObjState(0, z98, 70, 0)
        CompareObjState(0, z99, 70, 0)
        assert ConditionGroup(0)
        """State 12: Bell 1 ~ 4 anime end judgment"""
        CompareObjState(8, z97, 10, 0)
        CompareObjState(8, val2, 10, 0)
        CompareObjState(8, z98, 10, 0)
        CompareObjState(8, z99, 10, 0)
        assert ConditionGroup(8)
    """State 5: Judgment of door"""
    CompareObjState(0, z100, 10, 0)
    CompareObjState(1, z100, 10, 1)
    if ConditionGroup(0):
        """State 6: Open the door: 70"""
        ChangeObjState(z100, 70)
        """State 7: Door animation end judgment"""
        CompareObjState(0, z100, 20, 0)
        assert ConditionGroup(0)
        """State 14: Navimesh change: passable"""
        DeleteNavimeshAttribute(z102, 2)
        """State 13: Enable key guide for white door"""
        DisableWhiteDoorKeyGuide(z101, 0)
    elif ConditionGroup(1):
        pass
    """State 3: Lever key guide enabled"""
    DisableObjKeyGuide(z96, 0)
    """State 15: End state"""
    return 0

def event_m10_19_x62(z96=10191011, z97=10191200, val2=10191210, z98=10191220, z99=10191230):
    """[Lib] [execution] Kanemori _ Lever singing bell _ Guest
    z96: Lever_OBJ instance ID
    z97: Bell 1_OBJ instance ID
    val2: Bell 2_OBJ instance ID
    z98: Bell 3_OBJ instance ID
    z99: Bell 4_OBJ instance ID
    """
    """State 0,5: Ringing bell judgment"""
    if (not val2) != 0:
        """State 6: Ring bell 1"""
        ChangeObjState(z97, 70)
        """State 3: Ringing the bell_server information"""
        NotifyServerOfBellKeeperRinging()
        """State 4: Bell 1 animation playback judgment"""
        CompareObjState(0, z97, 70, 0)
        assert ConditionGroup(0)
        """State 2: Bell 1 animation end"""
        CompareObjState(0, z97, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z97, 70)
        ChangeObjState(val2, 70)
        ChangeObjState(z98, 70)
        ChangeObjState(z99, 70)
        """State 8: Bell ringing_server information transmission_2"""
        NotifyServerOfBellKeeperRinging()
        """State 9: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z97, 70, 0)
        CompareObjState(0, val2, 70, 0)
        CompareObjState(0, z98, 70, 0)
        CompareObjState(0, z99, 70, 0)
        assert ConditionGroup(0)
        """State 7: Anime end judgment for bells 1 to 4_2"""
        CompareObjState(8, z97, 10, 0)
        CompareObjState(8, val2, 10, 0)
        CompareObjState(8, z98, 10, 0)
        CompareObjState(8, z99, 10, 0)
        assert ConditionGroup(8)
    """State 10: End state"""
    return 0

def event_m10_19_x63(flag17=100360):
    """[Lib] [Reproduction] Special bonfire at the end
    flag17: Lighting completion flag
    """
    """State 0,1: Is the bonfire already lit?"""
    if GetEventFlag(flag17) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_19_x64(z105=10190700):
    """[Lib] [Condition] Terminal special fire
    z105: Bonfire OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z105)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x65(z105=10190700, flag17=100360):
    """[Lib] [Execution] End special bonfire_ignition
    z105: Bonfire OBJ instance ID
    flag17: Lighting completion flag
    """
    """State 0,6: Bonfire light action"""
    PlayerActionRequest(5)
    assert PlayerIsInEventAction(5) != 0
    """State 7: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 5, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 5: Bonfire ignition"""
        ChangeObjState(z105, 70)
        """State 3: Lighting completion flag ON"""
        SetEventFlag(flag17, 1)
        """State 1: Production FE display"""
        OpenPresentationWindow(20)
        assert PresentationWindowDisplay() != 0
        """State 4: Waiting for non-display of production FE"""
        assert PresentationWindowDisplay() != 1
        """State 2: Event message display"""
        # action:2022:"A primal bonfire was rekindled"
        DisplayEventMessage(2022, 0, 0, 0)
        assert EventMessageDisplay() != 0
    """State 8: End state"""
    return 0

def event_m10_19_x66(z105=10190700, flag17=100360):
    """[Lib] [Execution] End special bonfire_warp
    z105: Bonfire OBJ instance ID
    flag17: Lighting completion flag
    """
    """State 0,1: Warp PC action"""
    PlayerActionRequest(6)
    assert PlayerIsInEventAction(6) != 0
    """State 2: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 6, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Warp SFX playback PC invincible"""
        PlaySfxSelfGenerated(8002, 239, 200)
        SetPlayerInvincible(1)
        assert (GetStateTime() > 2.5) != 0
        """State 5: [Lib] Warp between maps after poly play_SubState"""
        assert event_m10_19_x1(z164=0, z165=0, z94=10040000, z95=200000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m10_19_x67(z105=10190700, flag17=100360):
    """[Lib] [Preset] Special bonfire at the end
    z105: Bonfire OBJ instance ID
    flag17: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] End special bonfire _SubState"""
    call = event_m10_19_x63(flag17=flag17)
    if call.Get() == 1:
        """State 5: [Lib] [Condition] End special bonfire_2_SubState"""
        assert event_m10_19_x64(z105=z105)
        """State 2: [Lib] [Execution] End special bonfire_warp_SubState"""
        assert event_m10_19_x66(z105=z105, flag17=flag17)
    elif call.Get() == 0:
        """State 4: [Lib] [Condition] End special bonfire_SubState"""
        assert event_m10_19_x64(z105=z105)
        """State 3: [Lib] [Execution] End special bonfire_At ignition_SubState"""
        assert event_m10_19_x65(z105=z105, flag17=flag17)
    """State 6: Rerun"""
    return 0

def event_m10_19_x68(flag16=100360, z104=7):
    """[Lib] [Preset] Trophy Acquisition_Global
    flag16: Acquisition trigger_global flag
    z104: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag16) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag16, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z104)
    """State 4: End state"""
    return 0

def event_m10_19_x69(flag15=101101):
    """[Lib] [Reproduction] Shop Lineup
    flag15: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(flag15) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m10_19_x70(bonfire2=19660, z103=119000086):
    """[Lib] [Conditions] Shop lineup
    bonfire2: Bonfire ID
    z103: Boss destruction flag
    """
    """State 0,1: Is the total number of laps 2 or more and is the boss destroyed?"""
    # bonfire:19660:Eygil's Idol
    CompareGameCycleForBonfire(8, bonfire2, 2, 2, 3)
    CompareEventFlag(8, z103, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_19_x71(flag15=101101):
    """[Lib] [execution] shop lineup
    flag15: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(flag15, 1)
    """State 2: End state"""
    return 0

def event_m10_19_x72(bonfire2=19660, z103=119000086, flag15=101101):
    """[Lib] [Preset] Shop Lineup
    bonfire2: Bonfire ID
    z103: Boss destruction flag
    flag15: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_19_x69(flag15=flag15)
    if call.Get() == 0:
        """State 3: [Lib] [Conditions] Shop lineup_SubState"""
        assert event_m10_19_x70(bonfire2=bonfire2, z103=z103)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_19_x71(flag15=flag15)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_19_x73(z100=10191290):
    """[Lib] [Conditions] Kanemori _ Lever that rings the bell _ Guest
    z100: Door OBJ instance ID
    """
    """State 0,1: Waiting for the door to open"""
    CompareObjState(0, z100, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x74(z100=10191290, z102=1000000):
    """[Lib] [execution] bell guard_bell change lever_navigation change
    z100: Door OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,1: Navimesh change: passable"""
    DeleteNavimeshAttribute(z102, 2)
    """State 2: End state"""
    return 0

def event_m10_19_x75(z93=10194900):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z93: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z93)
    """State 2: End state"""
    return 0

def event_m10_19_x76(z93=10194900):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z93: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z93, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z93)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_19_x77(z93=10194900, z94=50360000, z95=5100000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z93: Warp OBJ instance ID
    z94: Map ID
    z95: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z93, 1)
    """State 4: Warp PC action"""
    PlayerActionRequest(6)
    assert PlayerIsInEventAction(6) != 0
    """State 5: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 6, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 6: Warp SFX playback PC invincible"""
        PlaySfxSelfGenerated(8002, 219, 200)
        SetPlayerInvincible(1)
        assert (GetStateTime() > 2.5) != 0
        """State 2: Multiplayer prohibited state: ON"""
        ProhibitMultiplayer(1)
        """State 3: Save execution"""
        SaveExecution()
        """State 9: [Lib] Warp between maps after poly play_SubState"""
        assert event_m10_19_x1(z164=0, z165=0, z94=z94, z95=z95)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m10_19_x78(z93=10194900):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z93: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z93, 1)
    """State 2: End state"""
    return 0

def event_m10_19_x79(z93=10194900, z94=50360000, z95=5100000):
    """[Lib] [Preset] Warp move between main part and DLC
    z93: Warp OBJ instance ID
    z94: Map ID
    z95: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m10_19_x75(z93=z93)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m10_19_x76(z93=z93)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m10_19_x78(z93=z93)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m10_19_x77(z93=z93, z94=z94, z95=z95)
    """State 5: End state"""
    return 0

def event_m10_19_x80(z86=10192600):
    """[Lib] [BEST] [Condition] Andyel_Appearance_Termination
    z86: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z86)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x81(z86=10192600, flag14=100762, flag13=100743):
    """[Lib] [BEST] [Execution] Andyel_Appearance_Termination
    z86: Ander OBJ instance ID
    flag14: Conversation start flag
    flag13: Encounter flag
    """
    """State 0,4: Bonfire light action"""
    PlayerActionRequest(5)
    assert PlayerIsInEventAction(5) != 0
    """State 5: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 5, 0)
    if ConditionGroup(1):
        """State 8: Rerun"""
        return 1
    elif ConditionGroup(0):
        """State 6: Andel encounter flag ON"""
        SetEventFlag(flag13, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z86, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z86, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(flag14, 1)
        """State 7: End state"""
        return 0

def event_m10_19_x82(flag12=100740):
    """[Lib] [BEST] [Conditions] Ander_Destruction_End_Termination
    flag12: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, flag12, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x83(z86=10192600):
    """[Lib] [BEST] [Execution] Andel_Deletion_End
    z86: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z86, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z86, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x84(z86=10192600, flag12=100740, flag14=100762, flag13=100743):
    """[Lib] [BEST] [Reproduction] Anderl_Appearance determination_Termination
    z86: Ander OBJ instance ID
    flag12: Event completion flag
    flag14: Conversation start flag
    flag13: Encounter flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been completed?"""
        if GetEventFlag(flag12) != 0:
            pass
        else:
            """State 3: Was it in conversation?"""
            if GetEventFlag(flag14) != 0:
                pass
            else:
                """State 4: Was it in the middle of appearance?"""
                if CompareObjStateId(z86, 72, 0):
                    pass
                elif CompareObjStateId(z86, 73, 0):
                    pass
                elif CompareObjStateId(z86, 70, 0):
                    pass
                elif CompareObjStateId(z86, 30, 0):
                    pass
                else:
                    """State 7: Was the appearance confirmed?"""
                    if GetEventFlag(flag13) != 0:
                        """State 8: Standby state: 30"""
                        ChangeObjState(z86, 30)
                    else:
                        """State 11: Appearance determination"""
                        return 2
                """State 5: Wait for completion"""
                assert CompareObjStateId(z86, 30, 0)
                """State 6: Conversation start flag ON"""
                SetEventFlag(flag14, 1)
            """State 10: Disappearance judgment"""
            return 1
    """State 9: Finish"""
    return 0

def event_m10_19_x85():
    """[Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x86(z86=10192600, flag12=100740, flag13=100743, flag14=100762, z87=100360, z88=100300,
                     z89=100400, z90=100461):
    """[Lib] [BEST] [Preset] Andyel_Termination
    z86: Ander OBJ instance ID
    flag12: Event completion flag
    flag13: Encounter flag
    flag14: Conversation start flag
    z87: Lighting completion flag
    z88: Bonfire lighting judgment flag ①
    z89: Bonfire lighting judgment flag ②
    z90: Bonfire lighting judgment flag ③
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Ander _ Appearance determination _ Termination _ SubState"""
    call = event_m10_19_x84(z86=z86, flag12=flag12, flag14=flag14, flag13=flag13)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty _ SubState"""
        Label('L0')
        assert event_m10_19_x85()
        """State 9: [Lib] [BEST] [Conditions] Ander_Deletion_Termination_Termination_SubState"""
        assert event_m10_19_x82(flag12=flag12)
        """State 6: [Lib] [BEST] [Execution] Andel_Destruction_End_SubState"""
        assert event_m10_19_x83(z86=z86)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Ander_Appearance determination_Termination_SubState"""
        call = event_m10_19_x93(z86=z86, z87=z87, z88=z88, z89=z89, z90=z90, flag13=flag13)
        if call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Andel_Appearance determination_Termination_SubState"""
            assert event_m10_19_x94(z86=z86)
            """State 1: [Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty_SubState"""
            assert event_m10_19_x92()
            """State 7: [Lib] [BEST] [Condition] Ander_Appearance_Termination_SubState"""
            assert event_m10_19_x80(z86=z86)
            """State 4: [Lib] [BEST] [Execution] Andel_Appearance_Termination_SubState"""
            call = event_m10_19_x81(z86=z86, flag14=flag14, flag13=flag13)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                Goto('L0')
        elif call.Get() == 1:
            pass
        """State 11: Rerun"""
        return 1
    """State 10: Finish"""
    return 0

def event_m10_19_x87(z91=10192600, z92=10190700):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z91, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z92, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_19_x88(z91=10192600):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z91: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z91, 10, 0)
    CompareObjState(0, z91, 31, 0)
    CompareObjState(0, z91, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_19_x89(z91=10192600, z92=10190700):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z92, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z91, 10, 1)
    CompareObjState(8, z91, 31, 1)
    CompareObjState(8, z91, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_19_x90(z91=10192600, z92=10190700):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z92, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z91, 10, 0)
    CompareObjState(0, z91, 31, 0)
    CompareObjState(0, z91, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_19_x91(z91=10192600, z92=10190700):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_19_x87(z91=z91, z92=z92)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_19_x88(z91=z91)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_19_x89(z91=z91, z92=z92)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_19_x90(z91=z91, z92=z92)
    """State 6: Rerun"""
    return 1

def event_m10_19_x92():
    """[Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x93(z86=10192600, z87=100360, z88=100300, z89=100400, z90=100461, flag13=100743):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_Termination
    z86: Ander OBJ instance ID
    z87: Lighting completion flag
    z88: Bonfire lighting judgment flag ①
    z89: Bonfire lighting judgment flag ②
    z90: Bonfire lighting judgment flag ③
    flag13: Andyur encounter flag
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z87, 0)
    CompareEventFlag(8, z88, 1)
    CompareEventFlag(8, z89, 1)
    CompareEventFlag(8, z90, 1)
    CompareEventFlag(8, flag13, 0)
    CompareEventFlag(0, flag13, 1)
    if ConditionGroup(8):
        """State 2: End state"""
        return 0
    elif ConditionGroup(0):
        """State 3: Rerun"""
        return 1

def event_m10_19_x94(z86=10192600):
    """[Lib] [BEST] [Execution] Andel_Appearance determination_Termination
    z86: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z86, 31)
    """State 2: End state"""
    return 0

def event_m10_19_x95(z84=10192600, z85=10190700):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z84: Ander OBJ instance ID
    z85: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z84, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z85, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_19_x96(z84=10192600):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z84: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z84, 10, 0)
    CompareObjState(0, z84, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_19_x97(z84=10192600, z85=10190700):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z84: Ander OBJ instance ID
    z85: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z85, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z84, 10, 1)
    CompareObjState(8, z84, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_19_x98(z84=10192600, z85=10190700):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z84: Ander OBJ instance ID
    z85: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z85, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z84, 10, 0)
    CompareObjState(0, z84, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_19_x99(z84=10192600, z85=10190700):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z84: Ander OBJ instance ID
    z85: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_19_x95(z84=z84, z85=z85)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_19_x96(z84=z84)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_19_x97(z84=z84, z85=z85)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_19_x98(z84=z84, z85=z85)
    """State 5: Rerun"""
    return 0

def event_m10_19_x100(flag9=119020001, flag10=119000002):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag9: Lottery determination flag
    flag10: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag10) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag9) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_19_x101(z72=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z72: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z72, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_19_x102(flag9=119020001, z73=2, z74=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag9: Lottery determination flag
    z73: Number of appearance judgment points
    z74: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag9, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z73)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z74, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_19_x103(flag9=119020001, z72=14, flag10=119000002, z73=2, z74=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag9: Lottery determination flag
    z72: Random number comparison value
    flag10: Defeat flag
    z73: Number of appearance judgment points
    z74: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_19_x100(flag9=flag9, flag10=flag10)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_19_x101(z72=z72)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_19_x102(flag9=flag9, z73=z73, z74=z74)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_19_x112(flag9=flag9, z74=z74)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_19_x104(val1=_, z81=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z81: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z81) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_19_x105(z77=_, z78=0, z79=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z77: Appearance judgment point ID
    z78: Minimum appearance time
    z79: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z77, z77, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z78, 3, z79)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_19_x106(z80=941, z82=_, z83=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z80: Generator ID
    z82: Appearance start point ID
    z83: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z80, z82, z83)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z80)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m10_19_x107(flag11=119000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag11: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag11) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_19_x108(z77=_, z78=0, z79=5, z80=941, val1=_, z81=10, z82=_, z83=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z77: Intrusion detection point ID
    z78: Minimum appearance time
    z79: Maximum time to appear
    z80: Generator ID
    val1: Appearance judgment number
    z81: Lottery result point variable
    z82: Appearance start point ID
    z83: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_19_x104(val1=val1, z81=z81)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_19_x105(z77=z77, z78=z78, z79=z79)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_19_x106(z80=z80, z82=z82, z83=z83)
    """State 4: Finish"""
    return 0

def event_m10_19_x109(z75=941, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z75: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z75)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_19_x110(flag11=119000002, z76=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag11: Defeat flag
    z76: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag11, 1)
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
                    SetEventFlag(z76, 1)
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

def event_m10_19_x111(flag11=119000002, z75=941, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag11: Defeat flag
    z75: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_19_x107(flag11=flag11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_19_x109(z75=z75, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_19_x110(flag11=flag11, z76=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_19_x110(flag11=flag11, z76=102755)
    """State 5: End state"""
    return 0

def event_m10_19_x112(flag9=119020001, z74=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag9: Lottery determination flag
    z74: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag9, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z74, 0)
    """State 3: End state"""
    return 0

def event_m10_19_x113(flag8=_):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag8: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_19_x114(z70=_):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z70: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z70, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x115(z71=_):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z71: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z71, 1)
    """State 2: End state"""
    return 0

def event_m10_19_x116(flag8=_, z70=_, z71=_):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag8: Boss destruction flag
    z70: Boss generator ID
    z71: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_19_x113(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_19_x114(z70=z70)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_19_x115(z71=z71)
    """State 4: End state"""
    return 0

def event_m10_19_x117(z68=10191100):
    """[Reproduction] Scaffold moving up and down with lever
    z68: Scaffold instance ID
    """
    """State 0,4: [SEQ19188 compatible] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 1: Scaffold status determination"""
    if CompareObjStateId(z68, 30, 0):
        """State 2: Navimesh attribute switching_1_Descent"""
        DeleteNavimeshAttribute(100002, 2)
        DeleteNavimeshAttribute(100003, 2)
        DeleteNavimeshAttribute(100005, 2)
        AddNavimeshAttribute(100000, 2)
        AddNavimeshAttribute(100001, 2)
        AddNavimeshAttribute(100004, 2)
    elif CompareObjStateId(z68, 10, 0):
        """State 3: Navimesh attribute switching_2 when rising"""
        DeleteNavimeshAttribute(100000, 2)
        DeleteNavimeshAttribute(100001, 2)
        DeleteNavimeshAttribute(100004, 2)
        DeleteNavimeshAttribute(100005, 2)
        AddNavimeshAttribute(100002, 2)
        AddNavimeshAttribute(100003, 2)
    """State 5: End state"""
    return 0

def event_m10_19_x118(z69=10191010, z68=10191100):
    """[Condition] Scaffold moving up and down with lever
    z69: Lever instance ID
    z68: Scaffold instance ID
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z69, 74, 0)
    CompareObjState(0, z69, 84, 0)
    assert ConditionGroup(0)
    """State 2: Scaffold status determination"""
    CompareObjState(0, z68, 10, 0)
    CompareObjState(1, z68, 30, 0)
    if ConditionGroup(0):
        """State 3: Descent"""
        return 0
    elif ConditionGroup(1):
        """State 4: Rise"""
        return 1

def event_m10_19_x119(z68=10191100, z69=10191010):
    """[Execute] Scaffolding up and down with lever
    z68: Scaffold instance ID
    z69: Lever instance ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z68, 70)
    """State 2: Navigation mesh attribute switching_3_ moving"""
    AddNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100002, 2)
    AddNavimeshAttribute(100003, 2)
    AddNavimeshAttribute(100004, 2)
    AddNavimeshAttribute(100005, 2)
    """State 5: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z69, 1)
    """State 3: Waiting for scaffolding to finish"""
    CompareObjState(0, z68, 30, 0)
    assert ConditionGroup(0)
    """State 6: Enable key guide for lever"""
    DisableObjKeyGuide(z69, 0)
    """State 4: Navimesh attribute switching_1_Descent"""
    DeleteNavimeshAttribute(100002, 2)
    DeleteNavimeshAttribute(100003, 2)
    DeleteNavimeshAttribute(100005, 2)
    AddNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100004, 2)
    """State 7: End state"""
    return 0

def event_m10_19_x120(z68=10191100, z69=10191010):
    """[Execution] Scaffolding up and down with lever
    z68: Scaffold instance ID
    z69: Lever instance ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z68, 80)
    """State 2: Navigation mesh attribute switching_3_ moving"""
    AddNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100002, 2)
    AddNavimeshAttribute(100003, 2)
    AddNavimeshAttribute(100004, 2)
    AddNavimeshAttribute(100005, 2)
    """State 5: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z69, 1)
    """State 3: Waiting for the scaffold to rise"""
    CompareObjState(0, z68, 10, 0)
    assert ConditionGroup(0)
    """State 6: Enable key guide for lever"""
    DisableObjKeyGuide(z69, 0)
    """State 4: Navimesh attribute switching_2 when rising"""
    DeleteNavimeshAttribute(100000, 2)
    DeleteNavimeshAttribute(100001, 2)
    DeleteNavimeshAttribute(100004, 2)
    DeleteNavimeshAttribute(100005, 2)
    AddNavimeshAttribute(100002, 2)
    AddNavimeshAttribute(100003, 2)
    """State 7: End state"""
    return 0

def event_m10_19_x121(z68=10191100, z69=10191010):
    """[Preset] Scaffold moving up and down with lever
    z68: Scaffold instance ID
    z69: Lever instance ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z68, 0)
    """State 2: [Reproduction] Scaffolding up and down with lever _SubState"""
    assert event_m10_19_x117(z68=z68)
    """State 3: [Condition] Scaffolding up and down with lever_SubState"""
    call = event_m10_19_x118(z69=z69, z68=z68)
    if call.Get() == 0:
        """State 4: [Execution] Scaffolding up and down with lever_Descent_SubState"""
        assert event_m10_19_x119(z68=z68, z69=z69)
    elif call.Get() == 1:
        """State 5: [Execution] Scaffolding up and down with lever"""
        assert event_m10_19_x120(z68=z68, z69=z69)
    """State 6: End state"""
    return 0

def event_m10_19_x122(z67=_):
    """[Reproduction] Floor switch_Folding scaffold
    z67: Navigation switching area ID
    """
    """State 0,1: Navigation switching"""
    DeleteNavimeshAttribute(z67, 2)
    """State 2: End state"""
    return 0

def event_m10_19_x123(z66=_):
    """[Condition] Floor switch_Folding scaffold
    z66: Switch instance ID
    """
    """State 0,1: Did you get on the switch?"""
    CompareObjState(0, z66, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x124(z65=_, z67=_):
    """[Execution] Floor switch
    z65: OBJ instance ID to be run
    z67: Navigation switching area ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z65, 70)
    """State 2: Navigation switching"""
    AddNavimeshAttribute(z67, 2)
    """State 3: End state"""
    return 0

def event_m10_19_x125(z65=_, z66=_, z67=_):
    """[Preset] Floor switch
    z65: OBJ instance ID
    z66: Floor switch instance ID
    z67: Navigation switching area ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z65, 0)
    """State 2: [Reproduction] OBJ action _SubState with floor switch"""
    assert event_m10_19_x122(z67=z67)
    """State 3: [Condition] OBJ action _SubState with floor switch"""
    assert event_m10_19_x123(z66=z66)
    """State 4: [Execution] OBJ action with floor switch_Folding scaffolding_SubState"""
    assert event_m10_19_x124(z65=z65, z67=z67)
    """State 5: End state"""
    return 0

def event_m10_19_x126(z59=10191610, z60=600000, z61=600010, z62=10191615, z63=10191620, z64=600020):
    """[Reproduction] Burning furnace_Shutter and damage
    z59: Shutter instance ID
    z60: Damage area ID1
    z61: Damage area ID2
    z62: Damipoli instance ID under shutter
    z63: Damipoli instance ID on the ladder
    z64: Navimesh change point ID
    """
    """State 0,1: Has the shutter already closed?"""
    if CompareObjStateId(z59, 10, 0):
        """State 6: Fire on the ladder"""
        ChangeObjState(z63, 10)
        """State 5: Flame regeneration under the shutter"""
        ChangeObjState(z62, 10)
        """State 3: Burning damage ON"""
        EnableDamageArea(z60, 1)
        EnableDamageArea(z61, 1)
        """State 9: End state"""
        return 0
    else:
        """State 2: Burning damage disabled"""
        EnableDamageArea(z60, 0)
        EnableDamageArea(z61, 0)
        """State 4: Shutter flame stop"""
        ChangeObjState(z62, 20)
        """State 7: Flame stop on ladder"""
        ChangeObjState(z63, 20)
        """State 8: Navigation mesh change"""
        DeleteNavimeshAttribute(z64, 2)
        """State 10: Reproduce and finish"""
        return 1

def event_m10_19_x127(z58=10191550):
    """[Condition] Burning furnace_Shutter and damage
    z58: Valve instance ID
    """
    """State 0,1: Wait for valve operation"""
    CompareObjState(0, z58, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x128(z59=10191610, z60=600000, z61=600010, z62=10191615, z63=10191620, z64=600020):
    """[Execution] Burning furnace_Shutter and damage
    z59: Shutter instance ID
    z60: Damage area ID1
    z61: Damage area ID2
    z62: Damipoli instance ID under shutter
    z63: Damipoli instance ID on the ladder
    z64: Navimesh change point ID
    """
    """State 0,1: Shutter close animation playback"""
    ChangeObjState(z59, 70)
    """State 5: Did the shutter close to a certain level?"""
    CompareObjState(0, z59, 72, 0)
    assert ConditionGroup(0)
    """State 2: Burning damage disabled"""
    EnableDamageArea(z60, 0)
    EnableDamageArea(z61, 0)
    """State 3: Stop flame under shutter"""
    ChangeObjState(z62, 20)
    """State 4: Flame stop on ladder"""
    ChangeObjState(z63, 20)
    """State 6: Is the shutter completely closed?"""
    CompareObjState(0, z59, 20, 0)
    assert ConditionGroup(0)
    """State 7: Navigation mesh change"""
    DeleteNavimeshAttribute(z64, 2)
    """State 8: End state"""
    return 0

def event_m10_19_x129(z58=10191550, z59=10191610, z60=600000, z61=600010, z62=10191615, z63=10191620,
                      z64=600020):
    """[Preset] Burning furnace_Shutter and damage
    z58: Valve instance ID
    z59: Shutter instance ID
    z60: Damage area ID1
    z61: Damage area ID2
    z62: Damipoli instance ID under shutter
    z63: Damipoli instance ID on the ladder
    z64: Navimesh change point ID
    """
    """State 0,1: Disable OBJ synchronization"""
    SetObjSync(z59, 0)
    """State 2: [Reproduction] Burning furnace_Shutter and damage_SubState"""
    call = event_m10_19_x126(z59=z59, z60=z60, z61=z61, z62=z62, z63=z63, z64=z64)
    if call.Get() == 0:
        """State 3: [Condition] Burning furnace_Shutter and damage_SubState"""
        assert event_m10_19_x127(z58=z58)
        """State 4: [Execution] Burning furnace_Shutter and damage_SubState"""
        assert event_m10_19_x128(z59=z59, z60=z60, z61=z61, z62=z62, z63=z63, z64=z64)
    elif call.Get() == 1:
        pass
    """State 5: End state"""
    return 0

def event_m10_19_x130():
    """[Reproduction] Lever that stops all flame images"""
    """State 0,1: Judgment of status of fire flag"""
    if GetEventFlag(119000040) != 0:
        """State 2: Navi Mesh Delete"""
        DeleteNavimeshAttribute(900000, 2)
        """State 5: ON to OFF"""
        return 1
    else:
        """State 3: Navi Mesh added"""
        AddNavimeshAttribute(900000, 2)
        """State 4: OFF to ON"""
        return 0

def event_m10_19_x131(z55=10191350, z56=_, z57=_):
    """[Condition] Lever to stop all flame images
    z55: Lever OBJ object instance ID
    z56: Lever state_Start confirmed
    z57: Lever state_Standby
    """
    """State 0,1: Is the lever ready to start?"""
    CompareObjState(0, z55, z56, 0)
    assert ConditionGroup(0)
    """State 2: Is the lever in standby mode?"""
    CompareObjState(0, z55, z57, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x132(z53=119000040, z54=_):
    """[Execute] Lever that stops all flame images
    z53: Flame statue working flag
    z54: Flag setting
    """
    """State 0,1: Flame flag operation flag switching"""
    SetEventFlag(z53, z54)
    """State 2: End state"""
    return 0

def event_m10_19_x133(flag7=119000081):
    """[Reproduction] Flame linked to boss action
    flag7: Boss destruction flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag7) != 1:
        """State 2: Undefeated"""
        return 0
    else:
        """State 3: Defeated"""
        return 1

def event_m10_19_x134(z43=_, z44=10192200, z45=10192201, z52=_):
    """[Execution] Flames linked to boss actions
    z43: OBJ state ID for ON / OFF
    z44: OBJ instance ID of stone statue 1
    z45: OBJ instance ID of stone statue 2
    z52: ON / OFF completion confirmation OBJ state ID
    """
    """State 0,1: OBJ status change"""
    ChangeObjState(z44, z43)
    ChangeObjState(z45, z43)
    """State 2: Has the OBJ status change been completed?"""
    CompareObjState(8, z44, z52, 0)
    CompareObjState(8, z45, z52, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_19_x135(z47=_, z50=30, z51=_):
    """[Reproduction] Floor switch _ Molten iron pot
    z47: OBJ instance ID to be run
    z50: Hit group ID
    z51: Grand material ID
    """
    """State 0,1: Gimmick already activated?"""
    if CompareObjStateId(z47, 20, 0):
        """State 3: Activate damage"""
        SetGroundMaterial(z50, z51, 1)
        """State 5: Simple end"""
        return 1
    else:
        """State 2: Invalidate damage area"""
        SetGroundMaterial(z50, z51, 0)
        """State 4: End state"""
        return 0

def event_m10_19_x136(z48=_):
    """[Conditions] Floor switch_molten iron pot
    z48: Switch instance ID
    """
    """State 0,1: Did you get on the switch?"""
    CompareObjState(0, z48, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x137(z47=_, z48=_, z49=_, z50=30, z51=_):
    """[Execution] Floor switch _ Molten iron pot
    z47: OBJ instance ID to be run
    z48: Floor switch instance ID
    z49: Display OBJ instance ID
    z50: Hit group ID
    z51: Grand material ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z47, 70)
    assert (GetStateTime() > 4.5) != 0
    """State 3: OBJ display"""
    ChangeObjState(z49, 20)
    """State 2: Activate damage"""
    SetGroundMaterial(z50, z51, 1)
    """State 4: End state"""
    return 0

def event_m10_19_x138(z47=_, z48=_, z49=_, z50=30, z51=_):
    """[Preset] Floor switch _ Molten iron pot
    z47: OBJ instance ID
    z48: Floor switch instance ID
    z49: Display OBJ instance ID
    z50: Hit group ID
    z51: Grand material ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z47, 0)
    """State 2: [Reproduction] Floor switch_molten iron_SubState"""
    call = event_m10_19_x135(z47=z47, z50=z50, z51=z51)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Conditions] Floor switch _ Molten iron _ SubState"""
        assert event_m10_19_x136(z48=z48)
        """State 4: [Execution] Floor switch_molten iron_SubState"""
        assert event_m10_19_x137(z47=z47, z48=z48, z49=z49, z50=z50, z51=z51)
    """State 5: End state"""
    return 0

def event_m10_19_x139(z19=10191610):
    """[Reproduction] Burning furnace _ flame when opening the door
    z19: Shutter OBJ instance ID
    """
    """State 0,1: Is the shutter closed?"""
    if CompareObjStateId(z19, 20, 0):
        """State 3: The shutter is closed"""
        return 1
    else:
        """State 2: The shutter is open"""
        return 0

def event_m10_19_x140(z19=10191610, z20=_, z21=_):
    """[Preset] Burning furnace
    z19: Shutter OBJ instance ID
    z20: Door OBJ instance ID
    z21: Instance ID of OBJ that emits flame
    """
    """State 0,1: [Reproduction] Burning furnace _ SubState"""
    call = event_m10_19_x139(z19=z19)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Burning furnace_Open door and flame_SubState"""
        call = event_m10_19_x173(z19=z19, z20=z20)
        if call.Get() == 2:
            pass
        elif call.Get() == 0:
            """State 4: [Execution] Burning furnace _ Flame when opening the door _ Flame operation _ SubState"""
            call = event_m10_19_x174(z21=z21, z19=z19, z20=z20)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                """State 7: Rerun"""
                Label('L0')
                return 1
        elif call.Get() == 1:
            """State 5: [Execution] Burning furnace _ Flame when opening the door _ Flame stop _ SubState"""
            call = event_m10_19_x175(z21=z21, z19=z19, z20=z20)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                Goto('L0')
    """State 2: [Execution] Burning furnace _ Flame when opening the door _ Flame complete stop _ SubState"""
    assert event_m10_19_x141(z21=z21)
    """State 6: The shutter is closed"""
    return 0

def event_m10_19_x141(z21=_):
    """[Execution] Burning furnace _ Flame when opening the door _ Flame complete stop
    z21: Instance ID of OBJ that emits flame
    """
    """State 0,1: Complete stop of fire from the door"""
    ChangeObjState(z21, 20)
    """State 2: Has the flame stopped completely?"""
    CompareObjState(0, z21, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x142(z41=806, z46=93050010):
    """[Condition] Fire linked to the boss's action
    z41: Boss generator ID
    z46: Boss special state effect ID
    """
    """State 0,1: Boss status judgment"""
    ChrHasSpEffect(0, z41, z46, 1)
    IsChrDead(1, z41)
    if ConditionGroup(0):
        """State 2: Turn off due to status change"""
        return 0
    elif ConditionGroup(1):
        """State 3: Boss death"""
        return 1

def event_m10_19_x143(z41=806, z42=71, z43=70, z44=10192200, z45=10192201, z46=93050010, flag7=119000081):
    """[Preset] Flames linked to boss actions
    z41: Boss generator ID
    z42: State ID with stone statue on
    z43: State ID with stone statue flame OFF
    z44: OBJ instance ID of stone statue 1
    z45: OBJ instance ID of stone statue 2
    z46: Boss special state effect ID
    flag7: Boss destruction flag
    """
    """State 0,1: [Reproduction] Flame_SubState linked to the boss's behavior"""
    call = event_m10_19_x133(flag7=flag7)
    if call.Get() == 0:
        """State 4: [Condition] Fire linked to the boss's behavior_Boss is in anger state_SubState"""
        call = event_m10_19_x142(z41=z41, z46=z46)
        if call.Get() == 0:
            """State 2: [Execution] Flames linked to boss actions"""
            assert event_m10_19_x134(z43=z43, z44=z44, z45=z45, z52=30)
            """State 5: [Conditions] Flames linked to boss actions_Boss dies_SubState"""
            assert event_m10_19_x144(z41=z41)
            """State 3: [Execution] Flames linked to boss actions"""
            assert event_m10_19_x134(z43=z42, z44=z44, z45=z45, z52=10)
        elif call.Get() == 1:
            pass
    elif call.Get() == 1:
        pass
    """State 6: Finish"""
    return 0

def event_m10_19_x144(z41=806):
    """[Condition] Fire linked to the boss's action
    z41: Boss generator ID
    """
    """State 0,1: Boss status judgment"""
    IsChrDead(0, z41)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x145(z39=10191110, z37=10191020, z38=10191021, z40=1900000):
    """[Reproduction] Guillotine door
    z39: Guillotine door OBJ instance ID
    z37: Lever 1_OBJ instance ID
    z38: Lever 2_OBJ instance ID
    z40: Navigation change point ID
    """
    """State 0,1: Is the blade in the initial state?"""
    if CompareObjStateId(z39, 10, 1):
        """State 2: Disabling the key guide of the lever"""
        DisableObjKeyGuide(z37, 1)
        DisableObjKeyGuide(z38, 1)
        """State 3: Navigation mesh switching: Allowed to pass"""
        DeleteNavimeshAttribute(z40, 2)
        """State 4: Blade lowering standby"""
        CompareObjState(0, z39, 10, 0)
        assert CompareObjStateId(z39, 10, 0)
        """State 5: Enable key guide for lever"""
        DisableObjKeyGuide(z37, 0)
        DisableObjKeyGuide(z38, 0)
        """State 6: Navi mesh switching: Not allowed"""
        AddNavimeshAttribute(z40, 2)
    else:
        pass
    """State 7: End state"""
    return 0

def event_m10_19_x146(z37=10191020, z38=10191021):
    """[Conditions] Guillotine door
    z37: Lever 1_OBJ instance ID
    z38: Lever 2_OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z37, 74, 0)
    CompareObjState(0, z37, 84, 0)
    CompareObjState(0, z38, 74, 0)
    CompareObjState(0, z38, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x147(z39=10191110, z37=10191020, z38=10191021, z40=1900000):
    """[Execution] Guillotine door
    z39: Guillotine door OBJ instance ID
    z37: Lever 1_OBJ instance ID
    z38: Lever 2_OBJ instance ID
    z40: Navigation change point ID
    """
    """State 0,1: The door blade rises: 70"""
    ChangeObjState(z39, 70)
    """State 3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z37, 1)
    DisableObjKeyGuide(z38, 1)
    """State 6: Blade rising standby"""
    CompareObjState(0, z39, 30, 0)
    assert ConditionGroup(0)
    """State 5: Navigation mesh switching: Allowed to pass"""
    DeleteNavimeshAttribute(z40, 2)
    """State 2: Blade lowering standby"""
    CompareObjState(0, z39, 10, 0)
    assert ConditionGroup(0)
    """State 4: Enable key guide for lever"""
    DisableObjKeyGuide(z37, 0)
    DisableObjKeyGuide(z38, 0)
    """State 7: Navi mesh switching: Not allowed"""
    AddNavimeshAttribute(z40, 2)
    """State 8: End state"""
    return 0

def event_m10_19_x148(z37=10191020, z38=10191021, z39=10191110, z40=1900000):
    """[Preset] Guillotine door
    z37: Lever 1_OBJ instance ID
    z38: Lever 2_OBJ instance ID
    z39: OBJ instance ID of the guillotine door
    z40: Navigation change point ID
    """
    """State 0,1: [Reproduction] Guillotine door_SubState"""
    assert event_m10_19_x145(z39=z39, z37=z37, z38=z38, z40=z40)
    """State 2: [Condition] Guillotine door_SubState"""
    assert event_m10_19_x146(z37=z37, z38=z38)
    """State 3: [Execution] Guillotine door_SubState"""
    assert event_m10_19_x147(z39=z39, z37=z37, z38=z38, z40=z40)
    """State 4: End state"""
    return 0

def event_m10_19_x149(flag6=119020012):
    """[Reproduction] Vegrant generation determination
    flag6: Vegrant generation flag
    """
    """State 0,1: Has it already been judged?"""
    if GetEventFlag(flag6) != 0:
        """State 3: Judged"""
        return 1
    else:
        """State 2: Undecided"""
        return 0

def event_m10_19_x150(z35=119000081):
    """[Condition] Vegrant generation determination
    z35: Demon Knight Defeat Flag
    """
    """State 0,1: Demon Knight Defeat Determination"""
    CompareEventFlag(0, z35, 1)
    CompareEventFlag(1, z35, 0)
    if ConditionGroup(0):
        """State 2: Defeated"""
        return 0
    elif ConditionGroup(1):
        """State 3: Not defeated"""
        return 1

def event_m10_19_x151(z34=119020010, flag6=119020012, z36=_):
    """[Execution] Vegrant generation determination
    z34: Vagrant creation permission flag
    flag6: Vegrant generation flag
    z36: Generation permission ON / OFF
    """
    """State 0,1: Vagrant creation permission flag"""
    SetEventFlag(z34, z36)
    """State 2: Vagrant generation determination flag ON"""
    SetEventFlag(flag6, 1)
    """State 3: End state"""
    return 0

def event_m10_19_x152(z34=119020010, flag6=119020012, z35=119000081):
    """[Preset] Vegrant generation determination
    z34: Vagrant creation permission flag
    flag6: Vegrant generation flag
    z35: Demon Knight Defeat Flag
    """
    """State 0,1: [Reproduction] Vegrant generation determination_SubState"""
    call = event_m10_19_x149(flag6=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Vegrant generation determination_SubState"""
        call = event_m10_19_x150(z35=z35)
        if call.Get() == 1:
            """State 4: [Execution] Vegrant generation determination_OFF_SubState"""
            assert event_m10_19_x151(z34=z34, flag6=flag6, z36=0)
        elif call.Get() == 0:
            """State 2: [Execution] Vegrant generation determination_ON_SubState"""
            assert event_m10_19_x151(z34=z34, flag6=flag6, z36=1)
    """State 5: End state"""
    return 0

def event_m10_19_x153(z30=119000087, z31=807, z32=1502000, z33=2, flag5=119000086):
    """[Preset] Molten iron daemon
    z30: Flag to perform first battle or rematch determination
    z31: Molten Daemon Generator ID
    z32: Point ID for relocation during rematch
    z33: Activation state ID at the time of rematch
    flag5: Destruction flag of molten iron demon
    """
    """State 0,4: [Reproduction] Molten Iron Daemon_Initial Location Change_SubState"""
    call = event_m10_19_x154(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Molten iron daemon_Initial location change_SubState"""
        call = event_m10_19_x155(z30=z30)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 3: Waiting for white door"""
            CompareObjState(0, 10190610, 100, 0)
            assert ConditionGroup(0)
            """State 2: Wait for save"""
            assert (GetStateTime() > 0.1) != 0
            """State 6: [Execution] Molten iron daemon_Initial location change_SubState"""
            assert event_m10_19_x156(z31=z31, z32=z32, z33=z33)
            """State 1: Wait for battle"""
            CompareEventFlag(0, 119000088, 1)
            assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m10_19_x154(flag5=119000086):
    """[Reproduction] Molten iron daemon
    flag5: Destruction flag of molten iron demon
    """
    """State 0,1: Are you destroying the molten iron demon?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Undefeated"""
        return 0

def event_m10_19_x155(z30=119000087):
    """[Condition] Molten iron daemon_Initial location change
    z30: Flag to perform first battle or rematch determination
    """
    """State 0,1: Is it the first game? Is it a rematch?"""
    CompareEventFlag(0, z30, 0)
    if ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m10_19_x156(z31=807, z32=1502000, z33=2):
    """[Execution] Molten iron daemon
    z31: Molten Daemon Generator ID
    z32: Point ID for relocation during rematch
    z33: Activation state ID at the time of rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z31, z32)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z31, z33)
    """State 3: End state"""
    return 0

def event_m10_19_x157(z27=10191300):
    """[Reproduction] Bridge descending with lever
    z27: OBJ instance ID of the bridge
    """
    """State 0,1: Is the bridge in a finished state"""
    if CompareObjStateId(z27, 20, 0):
        pass
    elif CompareObjStateId(z27, 71, 0):
        pass
    elif CompareObjStateId(z27, 81, 0):
        pass
    else:
        Goto('L0')
    """State 5: Navi mesh switching"""
    AddNavimeshAttribute(500000, 2)
    AddNavimeshAttribute(500001, 2)
    DeleteNavimeshAttribute(500003, 2)
    """State 11: Both fall"""
    return 3
    """State 2: Right is falling"""
    Label('L0')
    if CompareObjStateId(z27, 80, 0):
        pass
    elif CompareObjStateId(z27, 40, 0):
        pass
    else:
        Goto('L1')
    """State 6: Navimesh switching_falling right"""
    AddNavimeshAttribute(500002, 2)
    DeleteNavimeshAttribute(500001, 2)
    """State 10: Right falls"""
    return 2
    """State 3: Is the left falling"""
    Label('L1')
    if CompareObjStateId(z27, 70, 0):
        """State 7: Navi mesh switching_falling left"""
        Label('L2')
        AddNavimeshAttribute(500002, 2)
        DeleteNavimeshAttribute(500000, 2)
        """State 9: The left is falling"""
        return 1
    elif CompareObjStateId(z27, 30, 0):
        Goto('L2')
    else:
        """State 4: Navimesh switching_up"""
        DeleteNavimeshAttribute(500002, 2)
        """State 8: initial state"""
        return 0

def event_m10_19_x158(z28=10191002, z29=10191000):
    """[Condition] Bridge descending with lever_Initial
    z28: Right lever OBJ instance ID
    z29: Left lever OBJ instance ID
    """
    """State 0,1: Waiting for two levers to start"""
    CompareObjState(0, z28, 72, 0)
    CompareObjState(1, z29, 72, 0)
    if ConditionGroup(0):
        """State 2: Right falls"""
        return 0
    elif ConditionGroup(1):
        """State 3: The left is falling"""
        return 1

def event_m10_19_x159(z27=10191300, z28=10191002, z29=10191000):
    """[Execution] Bridge descending with lever_Initial right fall
    z27: OBJ instance ID of the bridge
    z28: Right lever OBJ instance ID
    z29: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z28, 1)
    DisableObjKeyGuide(z29, 1)
    """State 1: Bridge _ right falls: 80"""
    ChangeObjState(z27, 80)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z27, 40, 0)
    """State 4: Navimesh switching_falling right"""
    AddNavimeshAttribute(500002, 2)
    DeleteNavimeshAttribute(500001, 2)
    """State 5: Lever key guide enabled"""
    DisableObjKeyGuide(z28, 0)
    DisableObjKeyGuide(z29, 0)
    """State 6: Waiting for the left to fall"""
    return 0

def event_m10_19_x160(z27=10191300, z28=10191002, z29=10191000):
    """[Execution] Bridge descending with lever _ Initial left fall
    z27: OBJ instance ID of the bridge
    z28: Right lever OBJ instance ID
    z29: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z28, 1)
    DisableObjKeyGuide(z29, 1)
    """State 1: Bridge _ left falls: 70"""
    ChangeObjState(z27, 70)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z27, 30, 0)
    """State 5: Navi mesh switching_falling left"""
    AddNavimeshAttribute(500002, 2)
    DeleteNavimeshAttribute(500000, 2)
    """State 4: Lever key guide enabled"""
    DisableObjKeyGuide(z28, 0)
    DisableObjKeyGuide(z29, 0)
    """State 6: Waiting for the right fall"""
    return 0

def event_m10_19_x161(z29=_):
    """[Condition] Bridge descending by lever_2
    z29: Second lever OBJ instance ID
    """
    """State 0,1: Waiting for lever to start"""
    CompareObjState(0, z29, 72, 0)
    assert ConditionGroup(0)
    """State 2: Fall"""
    return 0

def event_m10_19_x162(z27=10191300, z28=10191002, z29=10191000):
    """[Execution] Bridge descending with lever _ 2nd right fall
    z27: OBJ instance ID of the bridge
    z28: Right lever OBJ instance ID
    z29: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z28, 1)
    DisableObjKeyGuide(z29, 1)
    """State 1: Bridge_Right falls: 71"""
    ChangeObjState(z27, 71)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z27, 20, 0)
    """State 5: Navi mesh switching"""
    AddNavimeshAttribute(500000, 2)
    AddNavimeshAttribute(500001, 2)
    DeleteNavimeshAttribute(500003, 2)
    """State 4: Lever key guide enabled"""
    DisableObjKeyGuide(z28, 0)
    DisableObjKeyGuide(z29, 0)
    """State 6: Complete"""
    return 0

def event_m10_19_x163(z27=10191300, z28=10191002, z29=10191000):
    """[Execution] Bridge descending with lever _ 2nd left fall
    z27: OBJ instance ID of the bridge
    z28: Right lever OBJ instance ID
    z29: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z28, 1)
    DisableObjKeyGuide(z29, 1)
    """State 1: Bridge _ left falls: 81"""
    ChangeObjState(z27, 81)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z27, 20, 0)
    """State 5: Navi mesh switching"""
    AddNavimeshAttribute(500000, 2)
    AddNavimeshAttribute(500001, 2)
    DeleteNavimeshAttribute(500003, 2)
    """State 4: Lever key guide enabled"""
    DisableObjKeyGuide(z28, 0)
    DisableObjKeyGuide(z29, 0)
    """State 6: Complete"""
    return 0

def event_m10_19_x164(z27=10191300, z28=10191002, z29=10191000):
    """[Preset] Bridge descending with lever
    z27: OBJ instance ID of the bridge
    z28: Right lever OBJ instance ID
    z29: Left lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Bridge descending with a lever_SubState"""
    call = event_m10_19_x157(z27=z27)
    if call.Get() == 0:
        """State 7: [Condition] Bridge descending with lever_Initial_SubState"""
        call = event_m10_19_x158(z28=z28, z29=z29)
        if call.Get() == 0:
            """State 4: [Execution] Bridge descending with lever_Initial right fall_SubState"""
            assert event_m10_19_x159(z27=z27, z28=z28, z29=z29)
        elif call.Get() == 1:
            """State 5: [Execute] Bridge descending with lever_Initial left fall_SubState"""
            assert event_m10_19_x160(z27=z27, z28=z28, z29=z29)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 2:
        """State 6: [Condition] Bridge descending with lever _ 2nd_SubState"""
        assert event_m10_19_x161(z29=z29)
        """State 3: [Execution] Bridge descending with lever _ 2nd fall left_SubState"""
        assert event_m10_19_x163(z27=z27, z28=z28, z29=z29)
    elif call.Get() == 1:
        """State 8: [Condition] Bridge descending with lever _ 2nd _ SubState"""
        assert event_m10_19_x161(z29=z28)
        """State 2: [Execution] Bridge descending with lever_2 Falling right_SubState"""
        assert event_m10_19_x162(z27=z27, z28=z28, z29=z29)
    elif call.Get() == 3:
        pass
    """State 10: Finish"""
    return 1

def event_m10_19_x165(z23=10194999, z24=20, z25=1700000, z26=119020030):
    """[Preset] Bridge destroyed by enemies
    z23: Instance ID of the bridge OBJ
    z24: State ID of the destruction state of the bridge OBJ
    z25: Navimesh change point ID
    z26: Bridge destruction complete flag
    """
    """State 0,1: [Reproduction] Bridge _SubState destroyed by enemies"""
    call = event_m10_19_x166(z23=z23, z24=z24)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Bridge destroyed by enemy _SubState"""
        assert event_m10_19_x167(z23=z23, z24=z24)
    """State 3: [Execution] Bridge _SubState destroyed by enemies"""
    assert event_m10_19_x168(z25=z25, z26=z26)
    """State 4: End state"""
    return 0

def event_m10_19_x166(z23=10194999, z24=20):
    """[Reproduction] Bridge destroyed by enemies
    z23: Instance ID of the bridge OBJ
    z24: State ID of the destruction state of the bridge OBJ
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z23, z24, 0):
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Undestructed"""
        return 0

def event_m10_19_x167(z23=10194999, z24=20):
    """[Condition] Bridge destroyed by enemies
    z23: Instance ID of the bridge OBJ
    z24: State ID of the destruction state of the bridge OBJ
    """
    """State 0,1: OBJ destruction determination"""
    CompareObjState(0, z23, z24, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x168(z25=1700000, z26=119020030):
    """[Execution] Bridge destroyed by enemies
    z25: Navimesh change point ID
    z26: Bridge destruction complete flag
    """
    """State 0,1: Navigation mesh change"""
    AddNavimeshAttribute(z25, 2)
    """State 2: Bridge destruction complete flag: ON"""
    SetEventFlag(z26, 1)
    """State 3: End state"""
    return 0

def event_m10_19_x169():
    """[Reproduction] Vegrant Deletion Determination_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x170(z22=5000):
    """[Condition] Vegrant removal determination
    z22: Generator ID
    """
    """State 0,2: Has a vegrant been generated?"""
    IsChrActive(0, z22, 1)
    assert ConditionGroup(0)
    """State 1: Has Vegrant finished the return action?"""
    CompareChrEzStateValue(0, z22, 7, 1, 0)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m10_19_x171(z22=5000):
    """[Execution] Vegrant removal determination
    z22: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z22, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x172(z22=5000):
    """[Preset] Vegrant removal judgment
    z22: Generator ID
    """
    """State 0,1: [Reproduction] Vegrant deletion judgment_empty_SubState"""
    assert event_m10_19_x169()
    """State 3: [Condition] Vegrant deletion determination_SubState"""
    assert event_m10_19_x170(z22=z22)
    """State 2: [Execution] Vegrant deletion determination_SubState"""
    assert event_m10_19_x171(z22=z22)
    """State 4: End state"""
    return 0

def event_m10_19_x173(z19=10191610, z20=_):
    """[Condition] Burning furnace _ Flame when opening the door
    z19: Shutter OBJ instance ID
    z20: Door OBJ instance ID
    """
    """State 0,1: Shutter and door status judgment"""
    CompareObjState(0, z19, 20, 0)
    CompareObjState(1, z20, 30, 0)
    CompareObjState(2, z20, 84, 0)
    CompareObjState(2, z20, 10, 0)
    if ConditionGroup(0):
        """State 4: The shutter is closed"""
        return 2
    elif ConditionGroup(1):
        """State 2: The door is open"""
        return 0
    elif ConditionGroup(2):
        """State 3: The door is closed"""
        return 1

def event_m10_19_x174(z21=_, z19=10191610, z20=_):
    """[Execution] Burning furnace _ Flame when opening the door _ Flame operation
    z21: Instance ID of OBJ that emits flame
    z19: Shutter OBJ instance ID
    z20: Door OBJ instance ID
    """
    """State 0,1: Flame state transition"""
    ChangeObjState(z21, 30)
    """State 2: Shutter and door status judgment"""
    CompareObjState(0, z19, 20, 0)
    CompareObjState(1, z20, 30, 1)
    if ConditionGroup(0):
        """State 4: The shutter is closed"""
        return 1
    elif ConditionGroup(1):
        """State 3: There was a change in the condition of the door"""
        return 0

def event_m10_19_x175(z21=_, z19=10191610, z20=_):
    """[Execution] Burning furnace _ Flame when opening the door _ Flame stop
    z21: Instance ID of OBJ that emits flame
    z19: Shutter OBJ instance ID
    z20: Door OBJ instance ID
    """
    """State 0,1: Flame state transition"""
    ChangeObjState(z21, 10)
    """State 2: Shutter and door status judgment"""
    CompareObjState(0, z19, 20, 0)
    CompareObjState(8, z20, 10, 1)
    CompareObjState(8, z20, 84, 1)
    if ConditionGroup(0):
        """State 4: The shutter is closed"""
        return 1
    elif ConditionGroup(8):
        """State 3: There was a change in the condition of the door"""
        return 0

def event_m10_19_x176(flag4=119020016):
    """[Reproduction] Pledge: Kanemori_Contribution UP_Intruder generation determination
    flag4: Intruder generation determination flag
    """
    """State 0,1: Has it already been judged?"""
    if GetEventFlag(flag4) != 0:
        pass
    else:
        Goto('L0')
    """State 4: Judged"""
    return 1
    """State 2: Is it a bell defense pledge?"""
    Label('L0')
    if (GetPlayerCovenant() == 6) != 0:
        """State 3: Undecided"""
        return 0
    else:
        """State 5: Not a bell guard"""
        return 2

def event_m10_19_x177():
    """[Condition] Pledge: Kanemori_Contribution UP_Intruder generation determination"""
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment"""
    CompareEventRandValue(0, 0, 19, 5)
    if ConditionGroup(0):
        """State 3: Intruder: Generate"""
        return 0
    else:
        """State 4: Do not generate"""
        return 1

def event_m10_19_x178(z17=119020014, flag4=119020016, z18=_):
    """[Execution] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment
    z17: Intruder generation permission flag
    flag4: Intruder generation determination flag
    z18: Generation permission ON / OFF
    """
    """State 0,1: Intruder generation permission flag"""
    SetEventFlag(z17, z18)
    """State 2: Intruder generation determination flag ON"""
    SetEventFlag(flag4, 1)
    """State 3: End state"""
    return 0

def event_m10_19_x179(z17=119020014, flag4=119020016):
    """[Preset] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment
    z17: Intruder generation permission flag
    flag4: Intruder generation determination flag
    """
    """State 0,1: [Reproduction] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_SubState"""
    call = event_m10_19_x176(flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_SubState"""
        call = event_m10_19_x177()
        if call.Get() == 0:
            """State 4: [Execution] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_ON_SubState"""
            assert event_m10_19_x178(z17=z17, flag4=flag4, z18=1)
        elif call.Get() == 1:
            """State 2: [Execution] Pledge: Kanemori_Contribution UP_Intruder Generation Determination_OFF_SubState"""
            Label('L0')
            assert event_m10_19_x178(z17=z17, flag4=flag4, z18=0)
    elif call.Get() == 2:
        Goto('L0')
    """State 5: End state"""
    return 0

def event_m10_19_x180(flag3=119020018, z16=119020014):
    """[Reproduction] Pledge: Kanemori_Contribution UP
    flag3: Intruder Destruction Flag
    z16: Intruder generation permission flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 3: Has an intruder been generated?"""
        if GetEventFlag(119020014) != 0:
            """State 2: Has the intruder been destroyed?"""
            if GetEventFlag(flag3) != 1:
                """State 4: host"""
                return 0
            else:
                pass
        else:
            pass
    else:
        pass
    """State 5: Finish"""
    return 1

def event_m10_19_x181(z14=7007):
    """[Condition] Pledge: Kanemori_Contribution UP
    z14: Intruder generator ID
    """
    """State 0,1: Pledge and intruder defeat determination"""
    IsChrDead(8, z14)
    IsPlayerInCovenant(8, 6, 1)
    IsChrDead(9, z14)
    IsPlayerInCovenant(9, 6, 0)
    if ConditionGroup(8):
        """State 2: Increased contribution"""
        return 0
    elif ConditionGroup(9):
        """State 3: do nothing"""
        return 1

def event_m10_19_x182(flag3=119020018):
    """[Execution] Pledge: Kanemori_Contribution UP
    flag3: Intruder Destruction Flag
    """
    """State 0,1: Kanemori: Increased contribution"""
    AddPlayerCovenantContribution(6, 1)
    """State 2: Defeat flag ON"""
    SetEventFlag(flag3, 1)
    assert GetEventFlag(flag3) != 0
    """State 3: Finish"""
    return 0

def event_m10_19_x183(z14=7007, flag3=119020018, z15=119020014):
    """[Preset] Pledge: Kanemori_Contribution UP
    z14: Intruder generator ID
    flag3: Intruder Destruction Flag
    z15: Intruder generation permission flag
    """
    """State 0,1: [Reproduction] Pledge: Kanemori_Contribution UP_SubState"""
    call = event_m10_19_x180(flag3=flag3, z16=119020014)
    if call.Get() == 0:
        """State 3: [Condition] Pledge: Kanemori_Contribution UP_SubState"""
        call = event_m10_19_x181(z14=z14)
        if call.Get() == 0:
            """State 2: [Execution] Pledge: Kanemori_Contribution UP_SubState"""
            assert event_m10_19_x182(flag3=flag3)
        elif call.Get() == 1:
            """State 4: [Execution] Pledge: Kanemori_Contribution UP_Destroy only_SubState"""
            assert event_m10_19_x184(flag3=flag3)
    elif call.Get() == 1:
        pass
    """State 5: Finish"""
    return 0

def event_m10_19_x184(flag3=119020018):
    """[Execution] Pledge: Kanemori_Contribution UP_Destroy only
    flag3: Intruder Destruction Flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag3, 1)
    assert GetEventFlag(flag3) != 0
    """State 2: Finish"""
    return 0

def event_m10_19_x185(flag2=119000087):
    """[Reproduction] Molten iron demon
    flag2: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(flag2) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_19_x186(z9=10190610):
    """[Condition] Molten iron demon
    z9: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z9, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x187(z10=101910, flag2=119000087, z11=1501000, z12=1, z13=119000088):
    """[Execution] Molten Iron Daemon
    z10: Poly play ID
    flag2: Poly drama played flag
    z11: Warp point ID
    z12: Weight until poly play
    z13: Boss generation flag
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z10, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: During poly play: Generation flag ON"""
    SetEventFlag(z13, 1)
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(flag2, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z11)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_19_x188(z9=10190610, z10=101910, flag2=119000087, z11=1501000, z12=1, z13=119000088):
    """[Preset] Molten Iron Demon_Poly Play
    z9: White door instance ID
    z10: Poly play ID
    flag2: Poly drama played flag
    z11: Warp point ID
    z12: Wait time
    z13: Boss generation flag
    """
    """State 0,1: [Reproduction] Molten Iron Daemon_Poly Play_SubState"""
    call = event_m10_19_x185(flag2=flag2)
    if call.Get() == 0:
        """State 3: [Condition] Molten iron daemon_Poly play_SubState"""
        assert event_m10_19_x186(z9=z9)
        """State 2: [Execution] Molten Iron Daemon_Poly Play_SubState"""
        assert event_m10_19_x187(z10=z10, flag2=flag2, z11=z11, z12=z12, z13=z13)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_19_x189():
    """[DLC] [Reproduction] Stone monument displayed in text"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x190(z8=_):
    """[DLC] [Condition] Stone monument displayed in text
    z8: Stele OBJ instance ID
    """
    """State 0,1: Wait for decision to check"""
    IsObjSearched(0, z8)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x191(action1=_, z8=_):
    """[DLC] [execution] Stone monument displayed as text
    action1: Text ID
    z8: Stele OBJ instance ID
    """
    """State 0,2: Disable key guide"""
    DisableObjKeyGuide(z8, 1)
    """State 1: Text display"""
    DisplayEventMessage(action1, 0, 0, 0)
    assert (GetStateTime() > 1.5) != 0
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z8, 0)
    """State 4: End state"""
    return 0

def event_m10_19_x192(z8=_, action1=_):
    """[DLC] [Preset] Stone monument displayed as text
    z8: Stele OBJ instance ID
    action1: Text ID
    """
    """State 0,1: [DLC] [Reproduction] Stone monument_SubState displayed in text"""
    assert event_m10_19_x189()
    """State 3: [DLC] [Condition] Stone monument_SubState displayed in text"""
    assert event_m10_19_x190(z8=z8)
    """State 2: [DLC] [Execution] Stone monument_SubState displayed in text"""
    assert event_m10_19_x191(action1=action1, z8=z8)
    """State 4: End state"""
    return 0

def event_m10_19_x193(flag1=119000086, z3=1500000, z4=1500000, z5=101, z6=1019010, z7=119020085, mode1=0):
    """[BEST] [Lib] [Preset] Molten Iron Demon Battle
    flag1: Boss destruction flag
    z3: Start point ID
    z4: End point ID
    z5: Sound ID
    z6: Boss Battle ID
    z7: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_19_x7(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_19_x8(z3=z3, z4=z4)
        """State 6: [BEST] [Execute] Molten Iron Daemon Battle_Start_SubState"""
        assert event_m10_19_x194(z5=z5, z6=z6, z7=z7)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_19_x10()
        """State 5: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_19_x11(z6=z6)
        """State 3: [Execution] Boss Battle_End_SubState"""
        assert event_m10_19_x12(z5=z5, z6=z6, z7=z7, mode1=mode1)
    """State 7: End state"""
    return 0

def event_m10_19_x194(z5=101, z6=1019010, z7=119020085):
    """[BEST] [Execution] Molten Iron Demon Battle_Start
    z5: Sound ID
    z6: Boss Battle ID
    z7: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z5)
    """State 1: Boss battle start notification"""
    StartBossFight(z6)
    """State 5: Host?"""
    if IsGuest() != 1:
        """State 4: Enable auto save"""
        DisableAutoSave(0)
    else:
        pass
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z7, 1)
    """State 6: End state"""
    return 0

def event_m10_19_x195(bonfire1=19665, z2=10195130):
    """[DC] [Preset] Treasure chest changes mimic
    bonfire1: Bonfire ID
    z2: Treasure chest OBJ instance ID
    """
    """State 0,1: [DC] [Reproduction] Treasure box changes mimic_SubState"""
    assert event_m10_19_x196()
    """State 3: [DC] [Condition] Treasure box changes mimic_SubState"""
    assert event_m10_19_x198(bonfire1=bonfire1)
    """State 2: [DC] [execution] treasure box changes mimic_SubState"""
    assert event_m10_19_x197(z2=z2)
    """State 4: End state"""
    return 0

def event_m10_19_x196():
    """[DC] [Reproduction] Treasure box changes mimic"""
    """State 0,1: Is it in game?"""
    assert InGame() != 0
    """State 2: End state"""
    return 0

def event_m10_19_x197(z2=10195130):
    """[DC] [execution] treasure chest changes mimic
    z2: Treasure chest OBJ instance ID
    """
    """State 0,1: Hidden treasure box and key guide disabled"""
    ChangeDrawHit(z2, 0)
    DisableObjKeyGuide(z2, 1)
    assert (GetStateTime() > 0.1) != 0
    """State 2: End state"""
    return 0

def event_m10_19_x198(bonfire1=19665):
    """[DC] [Condition] Treasure chest changes mimic
    bonfire1: Bonfire ID
    """
    """State 0,1: Is the total number of laps more than the second lap?"""
    # bonfire:19665:Belfry Sol Approach
    CompareGameCycleForBonfire(0, bonfire1, 2, 2, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x199(z1=10191900):
    """[Preset] Two pairs of fire-blowing cows that rotate
    z1: Cow OBJ instance ID
    """
    """State 0,1: [Reproduction] Two pairs of fire-blowing cows _SubState rotating"""
    assert event_m10_19_x200(z1=z1)
    """State 3: [Condition] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m10_19_x202(z1=z1)
    """State 2: [Execution] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m10_19_x201(z1=z1)
    """State 4: Rerun"""
    return 0

def event_m10_19_x200(z1=10191900):
    """[Reproduction] Two pairs of rotating fire-blowing cows
    z1: Cow OBJ instance ID
    """
    """State 0,1: Judgment of fire-blown cow"""
    if CompareObjStateId(z1, 10, 1):
        """State 3,4: Waiting for stop"""
        assert CompareObjStateId(z1, 10, 0)
    else:
        pass
    """State 2,5: End state"""
    return 0

def event_m10_19_x201(z1=10191900):
    """[Execution] 2 pairs of fire-blowing cows rotating
    z1: Cow OBJ instance ID
    """
    """State 0,1: Rotating fire bull"""
    ChangeObjState(z1, 30)
    """State 2: Wait for rotation to end"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x202(z1=10191900):
    """[Conditions] Two pairs of rotating fired cows
    z1: Cow OBJ instance ID
    """
    """State 0,1: Damage judgment"""
    IsObjDamaged(0, z1, -1, -1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_111276():
    """Multi NPC: Woman Knight: White Phantom Sign Display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m10_19_x49(z108=102501, z109=576, z110=104190, z111=103690, z112=-1)
    Quit()

def event_m10_19_111277():
    """Multi NPC: Female Knight: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_19_x45(z122=119000081, z123=102498, z124=204, z125=7520)
    Quit()

def event_m10_19_111282():
    """NPC: Kanemori: Vane: Tomb"""
    """State 0,1: NPC: Kanemori: Vane: Grave Placement_SubState"""
    event_m10_19_x2(z160=104200, z161=10194100, z162=96, z163=7530)
    Quit()

def event_m10_19_111283():
    """NPC: Kanemori: Vain: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7530:Bell Keeper
    event_m10_19_x5(z155=119010100, z156=119020101, z157=104200, z158=10194100, z159=111282, npc1=7530)
    Quit()

def event_m10_19_111284():
    """NPC: Kanemori: Vane: Black Phantom Appearance: Offline"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
    event_m10_19_x47(z114=10000000, z115=570, z116=0, z117=2)
    Quit()

def event_m10_19_111442():
    """NPC: Curiosity Shop: Grave"""
    """State 0,1: NPC: Curiosity Shop: Grave Placement_SubState"""
    event_m10_19_x2(z160=104350, z161=10194000, z162=176, z163=7720)
    Quit()

def event_m10_19_111443():
    """NPC: Curio Shop: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7720:Magerold of Lanafir
    event_m10_19_x5(z155=119010110, z156=119020111, z157=104350, z158=10194000, z159=111442, npc1=7720)
    Quit()

def event_m10_19_111444():
    """NPC: Curio Shop: Shop List"""
    """State 0,1: Shop list: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Shop List: Defeating the King's Heavy Cavalry Boss: Judgment"""
        CompareEventFlag(0, 100980, 1)
        if ConditionGroup(0):
            """State 3: Shop list: Fire lap: Judgment"""
            # bonfire:19655:Threshold Bridge
            CompareGameCycleForBonfire(0, 19655, 2, 2, 3)
            if ConditionGroup(0):
                """State 5: Shop list: Flag update"""
                SetEventFlag(102822, 1)
                CompareEventFlag(0, 102822, 1)
                assert ConditionGroup(0)
            else:
                pass
        else:
            pass
    """State 4: Shop list: System: End"""
    EndMachine()
    Quit()

def event_m10_19_118100():
    """Multi-use NPC: White Spirit Test: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_19_x40(z128=577)
    Quit()

def event_m10_19_118110():
    """Multi NPC: White Spirit Test 2: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_19_x40(z128=578)
    Quit()

def event_m10_19_118210():
    """Multi NPC: Dark Spirit Test 1: Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_19_x46(z118=10001000, z119=571, z120=0, z121=2)
    Quit()

def event_m10_19_118220():
    """Multi NPC: Dark Spirit Test 2: Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_19_x46(z118=10002000, z119=572, z120=0, z121=2)
    Quit()

def event_m10_19_118230():
    """Multi NPC: Dark Spirit Test 3: Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_19_x46(z118=10002010, z119=573, z120=0, z121=2)
    Quit()

def event_m10_19_120050():
    """Trophy: Bell Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_19_x48(flag18=119020107, z113=23)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_19_120060():
    """Trophy: Old Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_19_x48(flag18=119020117, z113=24)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_19_2000000():
    """[DLC] Warp to ash map"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m10_19_x79(z93=10194900, z94=50360000, z95=5100000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_2001000():
    """[DLC] Stone monument displayed in text"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5430:"Trespassers will face\nadversity befitting a monarch"
    assert event_m10_19_x192(z8=10192500, action1=5430)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_2001010():
    """[DLC] Stone monument displayed in text_2"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5510:"In the tower of the Old Iron King\nresides a Child of Dark"
    assert event_m10_19_x192(z8=10192501, action1=5510)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_2001020():
    """[DLC] Stone monument displayed in text_3"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5420:"With water dry, and path amiss,\nwoeful temptation is dismissed"
    assert event_m10_19_x192(z8=10192502, action1=5420)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_2001030():
    """[DLC] Stone monument displayed as text_4"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5400:"Forbidden is the path\nto the ancient king's domain"
    assert event_m10_19_x192(z8=10192503, action1=5400)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_4000000():
    """[BEST] Andyur appearance _ molten iron castle"""
    """State 0,3: [Lib] [BEST] [Preset] Ander_Termination_SubState"""
    call = event_m10_19_x86(z86=10192600, flag12=100740, flag13=100743, flag14=100762, z87=100360, z88=100300,
                            z89=100400, z90=100461)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_19_4001000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_19_x99(z84=10192600, z85=10190700)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_19_4002000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_19_x91(z91=10192600, z92=10190700)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_19_4010000():
    """[BEST] Hidden door navigation mesh change 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z131=10191400, z132=20, z133=6010000, z134=0, z135=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4020000():
    """[DC] Treasure box changes mimic"""
    """State 0,2: [DC] [Preset] Treasure box changes mimic_SubState"""
    # bonfire:19665:Belfry Sol Approach
    assert event_m10_19_x195(bonfire1=19665, z2=10195130)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4021000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_19_x103(flag9=119020001, z72=14, flag10=119000002, z73=2, z74=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m10_19_x108(z77=80000000, z78=0, z79=5, z80=941, val1=1, z81=10, z82=80000001,
                z83=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m10_19_x108(z77=80000100, z78=0, z79=5, z80=941, val1=2, z81=10, z82=80000101,
                z83=80000199))
        """State 2: Start flag ON"""
        SetEventFlag(119020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4021010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_19_x111(flag11=119000002, z75=941, mode2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4022000():
    """[DC] Two pairs of fire-blowing cows rotating"""
    """State 0,2: [Preset] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m10_19_x199(z1=10191900)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_19_4022010():
    """[DC] Two pairs of rotating fire-blowing cows_attach_1"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_19_x31(z136=10191900, z137=150, z138=10191910)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4022020():
    """[DC] Two pairs of rotating fire-blowing cows_attach_2"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_19_x31(z136=10191900, z137=151, z138=10191911)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4031000():
    """[DC] NPC White Spirit_Gesture Management_Demon Knight"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_19_x116(flag8=119000081, z70=806, z71=119020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_19_4031010():
    """[DC] NPC White Spirit _ Gesture Management _ Molten Iron Daemon"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_19_x116(flag8=119000086, z70=807, z71=119020089)
    """State 1: Finish"""
    EndMachine()
    Quit()

