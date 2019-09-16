# -*- coding: utf-8 -*-
def event_m10_19_1000():
    """Scaffold moving up and down with lever"""
    """State 0,2: [Preset] Scaffolding up and down with lever_SubState"""
    assert event_m10_19_x121(z75=10191100, z76=10191010)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_2000():
    """One-way door from the bonfire room"""
    """State 0,2: [Lib] Area specified door unlocked_SubState"""
    assert event_m10_19_x0(z185=0, z186=200000, z187=19020100)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_3000():
    """[Insect Key] For Recovery Fountain _01"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_19_x13(z163=10191501)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_3010():
    """[Insect Key Activation] Recovery Fountain_01"""
    """State 0,2: [Lib] [Preset] Recovery Fountain_SubState"""
    assert event_m10_19_x23(z159=10191501, z160=20, z161=240, z162=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4000():
    """[Insect Key] For Recovery Fountain _02"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_19_x13(z163=10191502)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4010():
    """[Insect Key Activation] Recovery Fountain_02"""
    """State 0,2: [Lib] [Preset] Recovery Fountain_SubState"""
    assert event_m10_19_x23(z159=10191502, z160=10, z161=240, z162=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_5000():
    """Bridge descending with lever"""
    """State 0,3: [Preset] Bridge descending with lever_SubState"""
    call = event_m10_19_x164(z31=10191300, z32=10191002, z33=10191000)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_19_6000():
    """Burning furnace_shutter opening / closing"""
    """State 0,2: [Preset] Burning furnace_Shutter and damage_SubState"""
    assert (event_m10_19_x129(z65=10191550, z66=10191610, z67=600000, z68=600010, z69=10191615, z70=10191620,
            z71=600020))
    """State 1: Finish"""
    EndMachine()

def event_m10_19_6010():
    """Burning furnace _ flame when opening the door"""
    """State 0,3: [Preset] Burning furnace _ Flame when opening the door _ SubState"""
    call = event_m10_19_x140(z23=10191610, z24=10190402, z25=10191600)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_19_6020():
    """Burning furnace"""
    """State 0,3: [Preset] Burning furnace _ Flame when opening the door _ SubState"""
    call = event_m10_19_x140(z23=10191610, z24=10190400, z25=10191605)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_19_7000():
    """Molten iron pot 01"""
    """State 0,2: [Preset] Floor switch_Fused iron_SubState"""
    assert event_m10_19_x138(z54=10191700, z55=10191050, z56=10191710, z57=30, z58=240)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_7010():
    """Molten iron pot 02"""
    """State 0,2: [Preset] Floor switch_Fused iron_SubState"""
    assert event_m10_19_x138(z54=10191701, z55=10191051, z56=10191711, z57=30, z58=241)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_7020():
    """Molten iron pot 03"""
    """State 0,2: [Preset] Floor switch_Fused iron_SubState"""
    assert event_m10_19_x138(z54=10191702, z55=10191052, z56=10191712, z57=30, z58=242)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_8000():
    """Boss: Demon Knight Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_19_x6(z168=119000081, z169=800000, z170=800000, z171=102, z172=1019000, z173=119020080,
            mode7=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_19_8010():
    """Flames linked to boss actions"""
    """State 0,2: [Preset] Flame _SubState linked to the behavior of the boss"""
    assert event_m10_19_x143(z47=806, z48=71, z49=70, z50=10192200, z51=10192201, z52=93050010, z53=119000081)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_8020():
    """Vegrant generation determination"""
    """State 0,2: [Preset] Vegrant generation determination_SubState"""
    assert event_m10_19_x152(z39=119020010, z40=119020012, z41=119000081)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_8030():
    """Vegrant removal judgment"""
    """State 0,2: [Preset] Vegrant defeat determination_SubState"""
    assert event_m10_19_x172(z26=5000)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_9000():
    """Lever that stops all flame images"""
    """State 0,2: [Reproduction] Lever that stops all flame images _SubState"""
    call = event_m10_19_x130()
    if call.Get() == 0:
        """State 4: [Condition] Lever that stops all flame images _OFF to ON_SubState"""
        assert event_m10_19_x131(z62=10191350, z63=74, z64=30)
        """State 3: [Execute] Lever to stop all flame images"""
        assert event_m10_19_x132(z60=119000040, z61=1)
    elif call.Get() == 1:
        """State 5: [Condition] Lever that stops all flame images _ON to OFF_SubState"""
        assert event_m10_19_x131(z62=10191350, z63=84, z64=10)
        """State 6: [Execute] Lever to stop all flame images_Turn flag OFF_SubState"""
        assert event_m10_19_x132(z60=119000040, z61=0)
    """State 1: End (re-executable)"""
    RestartMachine()

def event_m10_19_10000():
    """Bell guard_bell lever"""
    """State 0,3: [Lib] [Preset] Bell guard_Lever that rings the bell_SubState"""
    call = event_m10_19_x58(z110=10191011, z111=10191200, val2=10191210, z112=10191220, z113=10191230,
                            z114=10191290, z115=10190641, z116=1000000)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()

def event_m10_19_10010():
    """Kanemori_Receiving the bell net"""
    """State 0,2: [Lib] [Preset] Kanemori_Net reception_SubState"""
    assert event_m10_19_x50(z124=10010, mode3=1, mode4=1, mode5=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_10020():
    """Jewel guard"""
    """State 0,2: [Lib] [Preset] Kanemori _ Judgment Spirit Lever Use Decision_SubState"""
    assert event_m10_19_x57(z123=10191011)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_11000():
    """[Insect key] For hidden door 1_01"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_19_x13(z163=10191500)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_11010():
    """[Insect key activation] Hidden door 1_01"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_19_x27(z157=10191500, val3=10190000, z158=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_11020():
    """[Insect key] Hidden door_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z149=10191410, z150=20, z151=1102000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_12000():
    """Falling scaffold 01_ back left"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z72=10191752, z73=10191053, z74=1200000)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_12010():
    """Falling scaffold 02_back right"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z72=10191753, z73=10191054, z74=1201000)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_12020():
    """Falling scaffold 03_ right front"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z72=10191751, z73=10191055, z74=1202000)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_12030():
    """Falling scaffold 04_left front"""
    """State 0,2: [Preset] OBJ action_SubState with floor switch"""
    assert event_m10_19_x125(z72=10191750, z73=10191056, z74=1203000)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_13000():
    """Attaching a flame in two directions_attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_19_x31(z154=10191100, z155=150, z156=10191650)
    """State 3: [Lib] [Preset] OBJ attach_2_SubState"""
    assert event_m10_19_x31(z154=10191100, z155=151, z156=10191651)
    """State 1: Finish"""
    EndMachine()

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
    assert (event_m10_19_x193(z3=119000086, z4=1500000, z5=1500000, z6=101, z7=1019010, z8=119020085,
            mode1=0))
    """State 7: Host? _2"""
    if IsGuest() != 1:
        """State 5: Auto save enabled"""
        DisableAutoSave(0)
    else:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_19_15010():
    """Boss: Molten Iron Demon_Poly Play"""
    """State 0,2: [Preset] Molten Iron Daemon_Poly Play_SubState"""
    assert event_m10_19_x188(z10=10190610, z11=101910, z12=119000087, z13=1501000, z14=1, z15=119000088)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_15020():
    """Boss: Molten Iron Daemon"""
    """State 0,2: Wait for damage invalid event to end"""
    assert EventEnded(14000) != 0
    """State 3: [Preset] Molten iron daemon_Initial location change_SubState"""
    assert event_m10_19_x153(z34=119000087, z35=807, z36=1502000, z37=2, z38=119000086)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_16000():
    """Connection flag ON"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_19_x39(z147=105420, z148=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_17000():
    """Bridges destroyed by enemies_Navigation change"""
    """State 0,2: [Preset] Bridge destroyed by enemies _SubState"""
    assert event_m10_19_x165(z27=10194999, z28=20, z29=1700000, z30=119020030)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_19000():
    """Guillotine door"""
    """State 0,2: [Preset] Guillotine Door_SubState"""
    assert event_m10_19_x148(z43=10191020, z44=10191021, z45=10191110, z46=1900000)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_20000():
    """End bonfire_molten iron"""
    """State 0,2: [Lib] [Preset] End special bonfire_SubState"""
    assert event_m10_19_x67(z121=10190700, z122=100360)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_23000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z149=10191404, z150=20, z151=2300000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_23010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z149=10191406, z150=20, z151=2301000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_24000():
    """Navimesh changes due to varistor destruction"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z149=10192000, z150=20, z151=2400000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_60000():
    """Pledge: Kanemori_Contribution UP"""
    """State 0,2: Has the generation determination event ended?"""
    assert EventEnded(60010) != 0
    """State 3: [Preset] Pledge: Kanemori_Contribution UP_SubState"""
    assert event_m10_19_x183(z16=7007, z17=119020018, z18=119020014)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_60010():
    """Pledge: Kanemori_Contribution UP_Intruder Generation Judgment"""
    """State 0,2: [Preset] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_SubState"""
    assert event_m10_19_x179(z20=119020014, z21=119020016)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_80000():
    """After the fire of rebirth 01_ Boss Demon Knight, a one-way door room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z144=1019000, z145=1019099)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_81000():
    """Regenerative fire 02_Stairs under the entrance bridge"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z144=1019100, z145=1019199)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_82000():
    """Reproduction Fire 03_Head of a Giant Cow"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z144=1019200, z145=1019299)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_82010():
    """Shop lineup expansion_molten iron demon"""
    """State 0,2: [Lib] [Preset] Shop Lineup_SubState"""
    # bonfire:19660:Eygil's Idol
    assert event_m10_19_x72(bonfire2=19660, z117=119000086, z118=101101)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_83000():
    """Reproduction flame 04_ depression in front of Kanemori area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_19_x44(z144=1019300, z145=1019399)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_90000():
    """Trophy_Lost Iron"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_19_x68(z119=100360, z120=7)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_x0(z185=0, z186=200000, z187=19020100):
    """[Lib] Area designated door unlocked
    z185: Text ID when opened
    z186: Point ID
    z187: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z186, 0, z185, 1101, z187, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x1(z183=0, z184=0, z108=_, z109=_):
    """[Lib] Warp between maps after poly play
    z183: Pre-warp poly play ID
    z184: Poly Play ID after Warp
    z108: Map ID
    z109: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z183, z184, z108, z109, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_19_x2(z179=_, z180=_, z181=_, z182=_):
    """[Lib] NPC: Grave Placement: General purpose
    z179: Death map: Global event flag
    z180: Tomb: OBJ instance ID
    z181: Tomb move to: Generator ID
    z182: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z179, 1)
    IsGraveGeneratable(8, z182, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z180, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z180, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_19_x3(z176=_, z177=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z176: Global: death flag
    z177: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z177, 10, 0)
    CompareObjState(1, z177, 20, 0)
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
    IsObjSearched(0, z177)
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

def event_m10_19_x4(z174=_, z175=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z174: Area other flags: Ghost appearance
    z175: Area other flags: Conversation start
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
    SetEventFlag(z174, 1)
    CompareEventFlag(0, z174, 1)
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
    SetEventFlag(z175, 1)
    CompareEventFlag(0, z175, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_19_x5(z174=_, z175=_, z176=_, z177=_, z178=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z174: Ghost Appearance: Area Other Flag
    z175: Conversation start: Area and other flags
    z176: Death: Global event flag
    z177: Tomb: OBJ instance ID
    z178: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z178, 1, 0)
    CompareEventFlag(9, z174, 1)
    CompareObjState(9, z177, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z175, 1)
        CompareEventFlag(0, z175, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_19_x3(z176=z176, z177=z177, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_19_x4(z174=z174, z175=z175, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_19_x6(z168=119000081, z169=800000, z170=800000, z171=102, z172=1019000, z173=119020080,
                    mode7=0):
    """[Lib] [Preset] Boss Battle Start
    z168: Boss destruction flag
    z169: Start point ID
    z170: End point ID
    z171: Sound ID
    z172: Boss Battle ID
    z173: Other flags for logic
    mode7: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_19_x7(z3=z168)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_19_x8(z4=z169, z5=z170)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_19_x9(z171=z171, z172=z172, z173=z173)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_19_x10()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_19_x11(z7=z172)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_19_x12(z6=z171, z7=z172, z8=z173, mode1=mode7)
    """State 7: End state"""
    return 0

def event_m10_19_x7(z3=_):
    """[Reproduction] Boss Battle_Start
    z3: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z3) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_19_x8(z4=_, z5=_):
    """[Condition] Boss Battle_Start
    z4: Start point ID
    z5: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z4, z5, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z4, z5, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x9(z171=102, z172=1019000, z173=119020080):
    """[Execution] Boss Battle_Start
    z171: Sound ID
    z172: Boss Battle ID
    z173: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z171)
    """State 1: Boss battle start notification"""
    StartBossFight(z172)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z173, 1)
    """State 4: End state"""
    return 0

def event_m10_19_x10():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x11(z7=_):
    """[Condition] Boss Battle_End Judgment
    z7: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z7, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x12(z6=_, z7=_, z8=_, mode1=0):
    """[Execute] Boss Battle_End
    z6: Sound ID
    z7: Boss Battle ID
    z8: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z8, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z7)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z6)
    """State 5: End state"""
    return 0

def event_m10_19_x13(z163=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z163: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_19_x14(z163=z163)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_19_x21(z163=z163)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_19_x22()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_19_x15(z163=z163, mode6=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_19_x16(z163=z163, z165=38, z166=3, z167=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_19_x17(z163=z163, z164=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_19_x14(z163=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z163: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z163, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z163, 10)
        assert CompareObjStateId(z163, 10, 0)
    elif CompareObjStateId(z163, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z163, 74, 1) and CompareObjStateId(z163, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_19_x15(z163=_, mode6=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z163: Object instance ID
    mode6: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z163)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode6) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_19_x16(z163=_, z165=38, z166=3, z167=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z163: Object instance ID
    z165: Key guide type
    z166: Event action
    z167: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z163, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z163, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z163, 30)
        assert CompareObjStateId(z163, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z163, z165, z166)
        assert PlayerIsInEventAction(z166) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z166, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z163, 74, 0)
        CompareObjState(1, z163, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z167)
            assert CompareObjStateId(z163, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z163, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_19_x17(z163=_, z164=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z163: Object instance ID
    z164: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z163, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_19_x18(z159=_, z160=_, z161=240, z162=1):
    """[Reproduction] Spring of recovery
    z159: OBJ instance ID of the bug key
    z160: Hit group ID
    z161: Replacement GMID
    z162: Switching GM slot
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z159, 20, 0):
        """State 2: Water OBJ: OBJ state transition: 20"""
        ChangeOwnObjState(20)
        """State 3: Enable recovery"""
        SetGroundMaterial(z160, z161, z162)
        """State 4: Activated"""
        return 0
    else:
        """State 5: Not running"""
        return 1

def event_m10_19_x19(z159=_):
    """[Condition] Spring of recovery
    z159: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z159, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x20(z160=_, z161=240, z162=1):
    """[Execution] Recovery Fountain
    z160: Hit group ID
    z161: Replacement GMID
    z162: Switching GM slot
    """
    """State 0,1: Water OBJ: OBJ state transition: 70"""
    ChangeOwnObjState(70)
    assert (GetStateTime() > 1) != 0
    """State 2: Enable recovery"""
    SetGroundMaterial(z160, z161, z162)
    """State 3: Waiting for the end of anime"""
    assert CompareOwnObjStateId(20, 0)
    """State 4: End state"""
    return 0

def event_m10_19_x21(z163=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z163: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z163, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x22():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x23(z159=_, z160=_, z161=240, z162=1):
    """[Lib] [Preset] Recovery Fountain
    z159: OBJ instance ID of the bug key
    z160: Hit group ID
    z161: Replacement GMID
    z162: Switching GM slot
    """
    """State 0,1: [Reproduction] Recovery Fountain_SubState"""
    call = event_m10_19_x18(z159=z159, z160=z160, z161=z161, z162=z162)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Condition] Recovery Fountain_SubState"""
        assert event_m10_19_x19(z159=z159)
        """State 2: [Execution] Recovery Fountain_SubState"""
        assert event_m10_19_x20(z160=z160, z161=z161, z162=z162)
    """State 4: End state"""
    return 0

def event_m10_19_x24(z157=10191500, val3=10190000):
    """[Reproduction] Hidden door 1_face SFX
    z157: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z157, 20, 0):
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

def event_m10_19_x25(z157=10191500):
    """[Conditions] Hidden door 1_Face SFX
    z157: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z157, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x26(z157=10191500, val3=10190000, z158=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z157: OBJ instance ID of the bug key
    val3: Event light ID
    z158: Light fade time
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
        SetPointLightEnabled(val3, 1, z158)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_19_x27(z157=10191500, val3=10190000, z158=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z157: OBJ instance ID of the bug key
    val3: Event light ID
    z158: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_19_x24(z157=z157, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_19_x25(z157=z157)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_19_x26(z157=z157, val3=val3, z158=z158, val4=val4)
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

def event_m10_19_x30(z154=_, z155=_, z156=_):
    """[Lib] [execute] OBJ attach
    z154: Parent OBJ instance ID
    z155: Parent Damipoli ID
    z156: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z154, z155, z156)
    """State 2: End state"""
    return 0

def event_m10_19_x31(z154=_, z155=_, z156=_):
    """[Lib] [Preset] OBJ attach
    z154: Parent OBJ instance ID
    z155: Parent Damipoli ID
    z156: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m10_19_x28()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m10_19_x29()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m10_19_x30(z154=z154, z155=z155, z156=z156)
    """State 4: End state"""
    return 0

def event_m10_19_x32(z149=_, z150=20, z151=_, z152=0, z153=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z149: Object instance ID
    z150: OBJ state ID
    z151: Navimesh switching point ID
    z152: Additional attributes
    z153: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_19_x33(z149=z149, z150=z150, z151=z151, z153=z153, z152=z152)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_19_x34(z149=z149, z150=z150, z151=z151)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_19_x35(z149=z149, z150=z150, z151=z151, z152=z152, z153=z153)
    """State 4: End state"""
    return 0

def event_m10_19_x33(z149=_, z150=20, z151=_, z153=2, z152=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z149: Target OBJ instance ID
    z150: Target OBJ state ID
    z151: Navimesh switching point ID
    z153: Additional attributes
    z152: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z149, z150, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z151, z153)
        DeleteNavimeshAttribute(z151, z152)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_19_x34(z149=_, z150=20, z151=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z149: Target OBJ instance ID
    z150: Target OBJ state ID
    z151: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z149, z150, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x35(z149=_, z150=20, z151=_, z152=0, z153=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z149: Target OBJ instance ID
    z150: Target OBJ state ID
    z151: Navimesh switching point ID
    z152: Additional attributes
    z153: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z151, z152)
    DeleteNavimeshAttribute(z151, z153)
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

def event_m10_19_x38(z147=105420, z148=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z147: Global event flag for connection
    z148: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z147, z148)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z147, z148)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_19_x39(z147=105420, z148=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z147: Global event flag for connection
    z148: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_19_x36()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_19_x37()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_19_x38(z147=z147, z148=z148)
    """State 4: End state"""
    return 0

def event_m10_19_x40(z146=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z146: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z146)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_19_x41():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x42(z144=_, z145=_):
    """[Lib] [execute] Rebirth fire
    z144: Flag start ID
    z145: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z144, z145, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x43():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x44(z144=_, z145=_):
    """[Lib] [Preset] Rebirth
    z144: Flag start ID
    z145: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_19_x41()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_19_x43()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_19_x42(z144=z144, z145=z145)
    """State 4: End state"""
    return 0

def event_m10_19_x45(z140=119000081, z141=102498, z142=204, z143=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z140: Defeat Boss 1: Area and other flags
    z141: Summon Achievement: Global Event Flag
    z142: Summon achievement count: global variable
    z143: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z141, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z140, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z142, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z142, NpcInfoValue(z143, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z141, 1)
                CompareEventFlag(0, z141, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m10_19_x46(z136=_, z137=_, z138=0, z139=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z136: Summon range
    z137: Generator ID
    z138: Appearance: Minimum time
    z139: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z136, z136, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z138, 3, z139)
        IsPlayerInsidePoint(1, z136, z136, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z137)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_19_x47(z132=10000000, z133=570, z134=0, z135=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z132: Summon range
    z133: Generator ID
    z134: Appearance: Minimum time
    z135: Appearance: Maximum time
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
            DeleteNpcPhantom(z133)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z132, z132, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z134, 3, z135)
                IsPlayerInsidePoint(1, z132, z132, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z133)
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

def event_m10_19_x48(z130=_, z131=_):
    """[Lib] [Preset] Get trophy
    z130: Acquisition trigger_other flags
    z131: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z130) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z130, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z131)
    """State 4: End state"""
    return 0

def event_m10_19_x49(z125=102501, z126=576, z127=104190, z128=103690, z129=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z125: White Phantom can appear: Global event flag
    z126: White Phantom: Generator ID
    z127: Death: Global event flag
    z128: Hostile: Global event flag
    z129: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z126)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z127, 1)
        CompareEventFlag(1, z128, 1)
        CompareEventFlag(2, z125, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z126)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z127, 1)
            CompareEventFlag(1, z128, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z126)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z127, 1)
            CompareEventFlag(1, z128, 1)
            HasNpcPhantomSpawned(2, z126, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z126, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z126)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m10_19_x50(z124=10010, mode3=1, mode4=1, mode5=1):
    """[Lib] [Preset] Kanemori_Net reception
    z124: Event sound ID for bell
    mode3: Wait 1 after SE playback
    mode4: Wait 2 after SE playback
    mode5: Wait 3 after playing SE
    """
    """State 0,1: [Lib] [Reproduction] Kanemori_Net reception_SubState"""
    assert event_m10_19_x51()
    """State 3: [Lib] [Conditions] Kanemori_Net reception_SubState"""
    assert event_m10_19_x52()
    """State 2: [Lib] [Execution] Kanemori_Net reception_SubState"""
    assert event_m10_19_x53(z124=z124, mode3=mode3, mode4=mode4, mode5=mode5)
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

def event_m10_19_x53(z124=10010, mode3=1, mode4=1, mode5=1):
    """[Lib] [Execution] Kanemori_Net reception_Playback
    z124: Event sound ID for bell
    mode3: Wait 1 after SE playback
    mode4: Wait 2 after SE playback
    mode5: Wait 3 after playing SE
    """
    """State 0,1: Ring the bell: first time"""
    PlaySoundAtPoint(z124)
    assert (GetStateTime() > mode3) != 0
    """State 4: Ring the bell: second time"""
    PlaySoundAtPoint(z124)
    assert (GetStateTime() > mode4) != 0
    """State 5: Ring the bell: 3rd time"""
    PlaySoundAtPoint(z124)
    assert (GetStateTime() > mode5) != 0
    """State 2: Clear reception history"""
    ClearBellKeeperRingingHistory()
    """State 3: Clear confirmation of received history"""
    IsBellKeeperRingingHistoryCleared(0, 0)
    assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m10_19_x54(z123=10191011):
    """[Lib] [reproduction] Kanemori _ judgment of lever use of Kanemori spirit
    z123: Lever OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 4: Host: Exit"""
        return 1
    else:
        """State 2: Disable key guide"""
        DisableObjKeyGuide(z123, 1)
        """State 3: Guest: Spirit guard"""
        return 0

def event_m10_19_x55():
    """[Lib] [Conditions] Kanemori _ Judgment spirit lever usage judgment"""
    """State 0,1: Has the host died?"""
    IsHostDead(0, 1)
    assert ConditionGroup(0)
    """State 2: Bell guard spirit: lever operation possible"""
    return 0

def event_m10_19_x56(z123=10191011):
    """[Lib] [Execution] Kanemori _ Judgment Spirit use lever judgment
    z123: Lever OBJ instance ID
    """
    """State 0,1: Activate key guide"""
    DisableObjKeyGuide(z123, 0)
    """State 2: Finish"""
    return 0

def event_m10_19_x57(z123=10191011):
    """[Lib] [Preset] Kanemori _ Judgment Spirit's lever usage judgment
    z123: Lever OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] Kanemori _ Jerusalem Spirit Lever Use Judgment_SubState"""
    call = event_m10_19_x54(z123=z123)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Conditions] Kanemori_Bellguard spirit lever usage judgment_SubState"""
        assert event_m10_19_x55()
        """State 2: [Lib] [Execution] Kanemori_Legend of lever guard_SubState"""
        assert event_m10_19_x56(z123=z123)
    """State 4: Finish"""
    return 0

def event_m10_19_x58(z110=10191011, z111=10191200, val2=10191210, z112=10191220, z113=10191230, z114=10191290,
                     z115=10190641, z116=1000000):
    """[Lib] [Preset] Bell guard_bell lever
    z110: Lever_OBJ instance ID
    z111: Bell 1_OBJ instance ID
    val2: Bell 2_OBJ instance ID
    z112: Bell 3_OBJ instance ID
    z113: Bell 4_OBJ instance ID
    z114: Door OBJ instance ID
    z115: White door OBJ instance ID
    z116: Navigation change point ID
    """
    """State 0,1: [Lib] [Reproduction] Bell guard_Lever that bell rings_SubState"""
    call = event_m10_19_x59(z114=z114, z115=z115, z116=z116)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        Goto('L0')
    """State 3: [Lib] [Conditions] Bell guard_Lever that rings bell_SubState"""
    call = event_m10_19_x60(z110=z110)
    if call.Get() == 0:
        """State 4: [Lib] [execution] bell guard_bell lever_host_SubState"""
        assert (event_m10_19_x61(z110=z110, z111=z111, val2=val2, z112=z112, z113=z113, z114=z114, z115=z115,
                z116=z116))
    elif call.Get() == 1:
        """State 2: [Lib] [execution] bell guard_bell lever_guest_SubState"""
        assert event_m10_19_x62(z110=z110, z111=z111, val2=val2, z112=z112, z113=z113)
    """State 7: Rerun"""
    return 0
    """State 6: [Lib] [Conditions] Bell guard_Lever that rings bell_Guest_SubState"""
    Label('L0')
    assert event_m10_19_x73(z114=z114)
    """State 5: [Lib] [Execution] Bell guard_Lever that bell rings_Navigation change_SubState"""
    assert event_m10_19_x74(z114=z114, z116=z116)
    """State 8: Guest termination"""
    return 1

def event_m10_19_x59(z114=10191290, z115=10190641, z116=1000000):
    """[Lib] [reproduction] bell guard _ bell ringing lever
    z114: Door OBJ instance ID
    z115: White door OBJ instance ID
    z116: Navigation change point ID
    """
    """State 0,3: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is the door open?"""
    if CompareObjStateId(z114, 10, 0):
        """State 2: White door key guide disabled"""
        DisableWhiteDoorKeyGuide(z115, 1)
    else:
        """State 4: Navimesh change: passable"""
        DeleteNavimeshAttribute(z116, 2)
    """State 5: host"""
    return 0
    """State 6: Guest termination"""
    Label('L0')
    return 1

def event_m10_19_x60(z110=10191011):
    """[Lib] [Conditions] Bell guard_bell lever
    z110: OBJ instance ID of the lever
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z110, 74, 0)
    CompareObjState(0, z110, 84, 0)
    SetConditionGroup(8, 0)
    IsHostDead(8, 0)
    CompareObjState(1, z110, 74, 0)
    CompareObjState(1, z110, 84, 0)
    SetConditionGroup(9, 1)
    IsHostDead(9, 1)
    if ConditionGroup(8):
        """State 2: Host is alive: Host processing"""
        return 0
    elif ConditionGroup(9):
        """State 3: Host dies: guest processing"""
        return 1

def event_m10_19_x61(z110=10191011, z111=10191200, val2=10191210, z112=10191220, z113=10191230, z114=10191290,
                     z115=10190641, z116=1000000):
    """[Lib] [Execution] Kanemori_Lever that rings the bell_Host
    z110: Lever_OBJ instance ID
    z111: Bell 1_OBJ instance ID
    val2: Bell 2_OBJ instance ID
    z112: Bell 3_OBJ instance ID
    z113: Bell 4_OBJ instance ID
    z114: Door OBJ instance ID
    z115: White door OBJ instance ID
    z116: Navigation change point ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z110, 1)
    """State 9: Ringing bell judgment"""
    if (not val2) != 0:
        """State 10: Ring bell 1"""
        ChangeObjState(z111, 70)
        """State 8: Bell 1 animation playback judgment"""
        CompareObjState(0, z111, 70, 0)
        assert ConditionGroup(0)
        """State 4: Bell 1 animation end"""
        CompareObjState(0, z111, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z111, 70)
        ChangeObjState(val2, 70)
        ChangeObjState(z112, 70)
        ChangeObjState(z113, 70)
        """State 11: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z111, 70, 0)
        CompareObjState(0, val2, 70, 0)
        CompareObjState(0, z112, 70, 0)
        CompareObjState(0, z113, 70, 0)
        assert ConditionGroup(0)
        """State 12: Bell 1 ~ 4 anime end judgment"""
        CompareObjState(8, z111, 10, 0)
        CompareObjState(8, val2, 10, 0)
        CompareObjState(8, z112, 10, 0)
        CompareObjState(8, z113, 10, 0)
        assert ConditionGroup(8)
    """State 5: Judgment of door"""
    CompareObjState(0, z114, 10, 0)
    CompareObjState(1, z114, 10, 1)
    if ConditionGroup(0):
        """State 6: Open the door: 70"""
        ChangeObjState(z114, 70)
        """State 7: Door animation end judgment"""
        CompareObjState(0, z114, 20, 0)
        assert ConditionGroup(0)
        """State 14: Navimesh change: passable"""
        DeleteNavimeshAttribute(z116, 2)
        """State 13: Enable key guide for white door"""
        DisableWhiteDoorKeyGuide(z115, 0)
    elif ConditionGroup(1):
        pass
    """State 3: Lever key guide enabled"""
    DisableObjKeyGuide(z110, 0)
    """State 15: End state"""
    return 0

def event_m10_19_x62(z110=10191011, z111=10191200, val2=10191210, z112=10191220, z113=10191230):
    """[Lib] [execution] Kanemori _ Lever singing bell _ Guest
    z110: Lever_OBJ instance ID
    z111: Bell 1_OBJ instance ID
    val2: Bell 2_OBJ instance ID
    z112: Bell 3_OBJ instance ID
    z113: Bell 4_OBJ instance ID
    """
    """State 0,5: Ringing bell judgment"""
    if (not val2) != 0:
        """State 6: Ring bell 1"""
        ChangeObjState(z111, 70)
        """State 3: Ringing the bell_server information"""
        NotifyServerOfBellKeeperRinging()
        """State 4: Bell 1 animation playback judgment"""
        CompareObjState(0, z111, 70, 0)
        assert ConditionGroup(0)
        """State 2: Bell 1 animation end"""
        CompareObjState(0, z111, 10, 0)
        assert ConditionGroup(0)
    else:
        """State 1: Ring bell 1-4"""
        ChangeObjState(z111, 70)
        ChangeObjState(val2, 70)
        ChangeObjState(z112, 70)
        ChangeObjState(z113, 70)
        """State 8: Bell ringing_server information transmission_2"""
        NotifyServerOfBellKeeperRinging()
        """State 9: Bell 1-4 animation playback judgment"""
        CompareObjState(0, z111, 70, 0)
        CompareObjState(0, val2, 70, 0)
        CompareObjState(0, z112, 70, 0)
        CompareObjState(0, z113, 70, 0)
        assert ConditionGroup(0)
        """State 7: Anime end judgment for bells 1 to 4_2"""
        CompareObjState(8, z111, 10, 0)
        CompareObjState(8, val2, 10, 0)
        CompareObjState(8, z112, 10, 0)
        CompareObjState(8, z113, 10, 0)
        assert ConditionGroup(8)
    """State 10: End state"""
    return 0

def event_m10_19_x63(z122=100360):
    """[Lib] [Reproduction] Special bonfire at the end
    z122: Lighting completion flag
    """
    """State 0,1: Is the bonfire already lit?"""
    if GetEventFlag(z122) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_19_x64(z121=10190700):
    """[Lib] [Condition] Terminal special fire
    z121: Bonfire OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z121)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x65(z121=10190700, z122=100360):
    """[Lib] [Execution] End special bonfire_ignition
    z121: Bonfire OBJ instance ID
    z122: Lighting completion flag
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
        ChangeObjState(z121, 70)
        """State 3: Lighting completion flag ON"""
        SetEventFlag(z122, 1)
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

def event_m10_19_x66(z121=10190700, z122=100360):
    """[Lib] [Execution] End special bonfire_warp
    z121: Bonfire OBJ instance ID
    z122: Lighting completion flag
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
        assert event_m10_19_x1(z183=0, z184=0, z108=10040000, z109=200000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m10_19_x67(z121=10190700, z122=100360):
    """[Lib] [Preset] Special bonfire at the end
    z121: Bonfire OBJ instance ID
    z122: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] End special bonfire _SubState"""
    call = event_m10_19_x63(z122=z122)
    if call.Get() == 1:
        """State 5: [Lib] [Condition] End special bonfire_2_SubState"""
        assert event_m10_19_x64(z121=z121)
        """State 2: [Lib] [Execution] End special bonfire_warp_SubState"""
        assert event_m10_19_x66(z121=z121, z122=z122)
    elif call.Get() == 0:
        """State 4: [Lib] [Condition] End special bonfire_SubState"""
        assert event_m10_19_x64(z121=z121)
        """State 3: [Lib] [Execution] End special bonfire_At ignition_SubState"""
        assert event_m10_19_x65(z121=z121, z122=z122)
    """State 6: Rerun"""
    return 0

def event_m10_19_x68(z119=100360, z120=7):
    """[Lib] [Preset] Trophy Acquisition_Global
    z119: Acquisition trigger_global flag
    z120: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z119) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z119, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z120)
    """State 4: End state"""
    return 0

def event_m10_19_x69(z118=101101):
    """[Lib] [Reproduction] Shop Lineup
    z118: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(z118) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m10_19_x70(bonfire2=19660, z117=119000086):
    """[Lib] [Conditions] Shop lineup
    bonfire2: Bonfire ID
    z117: Boss destruction flag
    """
    """State 0,1: Is the total number of laps 2 or more and is the boss destroyed?"""
    # bonfire:19660:Eygil's Idol
    CompareGameCycleForBonfire(8, bonfire2, 2, 2, 3)
    CompareEventFlag(8, z117, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_19_x71(z118=101101):
    """[Lib] [execution] shop lineup
    z118: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(z118, 1)
    """State 2: End state"""
    return 0

def event_m10_19_x72(bonfire2=19660, z117=119000086, z118=101101):
    """[Lib] [Preset] Shop Lineup
    bonfire2: Bonfire ID
    z117: Boss destruction flag
    z118: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_19_x69(z118=z118)
    if call.Get() == 0:
        """State 3: [Lib] [Conditions] Shop lineup_SubState"""
        assert event_m10_19_x70(bonfire2=bonfire2, z117=z117)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_19_x71(z118=z118)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_19_x73(z114=10191290):
    """[Lib] [Conditions] Kanemori _ Lever that rings the bell _ Guest
    z114: Door OBJ instance ID
    """
    """State 0,1: Waiting for the door to open"""
    CompareObjState(0, z114, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x74(z114=10191290, z116=1000000):
    """[Lib] [execution] bell guard_bell change lever_navigation change
    z114: Door OBJ instance ID
    z116: Navigation change point ID
    """
    """State 0,1: Navimesh change: passable"""
    DeleteNavimeshAttribute(z116, 2)
    """State 2: End state"""
    return 0

def event_m10_19_x75(z107=10194900):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z107: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z107)
    """State 2: End state"""
    return 0

def event_m10_19_x76(z107=10194900):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z107: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z107, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z107)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_19_x77(z107=10194900, z108=50360000, z109=5100000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z107: Warp OBJ instance ID
    z108: Map ID
    z109: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z107, 1)
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
        assert event_m10_19_x1(z183=0, z184=0, z108=z108, z109=z109)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m10_19_x78(z107=10194900):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z107: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z107, 1)
    """State 2: End state"""
    return 0

def event_m10_19_x79(z107=10194900, z108=50360000, z109=5100000):
    """[Lib] [Preset] Warp move between main part and DLC
    z107: Warp OBJ instance ID
    z108: Map ID
    z109: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m10_19_x75(z107=z107)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m10_19_x76(z107=z107)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m10_19_x78(z107=z107)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m10_19_x77(z107=z107, z108=z108, z109=z109)
    """State 5: End state"""
    return 0

def event_m10_19_x80(z97=10192600):
    """[Lib] [BEST] [Condition] Andyel_Appearance_Termination
    z97: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z97)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x81(z97=10192600, z100=100762, z99=100743):
    """[Lib] [BEST] [Execution] Andyel_Appearance_Termination
    z97: Ander OBJ instance ID
    z100: Conversation start flag
    z99: Encounter flag
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
        SetEventFlag(z99, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z97, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z97, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(z100, 1)
        """State 7: End state"""
        return 0

def event_m10_19_x82(z98=100740):
    """[Lib] [BEST] [Conditions] Ander_Destruction_End_Termination
    z98: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, z98, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x83(z97=10192600):
    """[Lib] [BEST] [Execution] Andel_Deletion_End
    z97: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z97, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z97, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x84(z97=10192600, z98=100740, z100=100762, z99=100743):
    """[Lib] [BEST] [Reproduction] Anderl_Appearance determination_Termination
    z97: Ander OBJ instance ID
    z98: Event completion flag
    z100: Conversation start flag
    z99: Encounter flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been completed?"""
        if GetEventFlag(z98) != 0:
            pass
        else:
            """State 3: Was it in conversation?"""
            if GetEventFlag(z100) != 0:
                pass
            else:
                """State 4: Was it in the middle of appearance?"""
                if CompareObjStateId(z97, 72, 0):
                    pass
                elif CompareObjStateId(z97, 73, 0):
                    pass
                elif CompareObjStateId(z97, 70, 0):
                    pass
                elif CompareObjStateId(z97, 30, 0):
                    pass
                else:
                    """State 7: Was the appearance confirmed?"""
                    if GetEventFlag(z99) != 0:
                        """State 8: Standby state: 30"""
                        ChangeObjState(z97, 30)
                    else:
                        """State 11: Appearance determination"""
                        return 2
                """State 5: Wait for completion"""
                assert CompareObjStateId(z97, 30, 0)
                """State 6: Conversation start flag ON"""
                SetEventFlag(z100, 1)
            """State 10: Disappearance judgment"""
            return 1
    """State 9: Finish"""
    return 0

def event_m10_19_x85():
    """[Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x86(z97=10192600, z98=100740, z99=100743, z100=100762, z101=100360, z102=100300, z103=100400,
                     z104=100461):
    """[Lib] [BEST] [Preset] Andyel_Termination
    z97: Ander OBJ instance ID
    z98: Event completion flag
    z99: Encounter flag
    z100: Conversation start flag
    z101: Lighting completion flag
    z102: Bonfire lighting judgment flag ①
    z103: Bonfire lighting judgment flag ②
    z104: Bonfire lighting judgment flag ③
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Ander _ Appearance determination _ Termination _ SubState"""
    call = event_m10_19_x84(z97=z97, z98=z98, z100=z100, z99=z99)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty _ SubState"""
        Label('L0')
        assert event_m10_19_x85()
        """State 9: [Lib] [BEST] [Conditions] Ander_Deletion_Termination_Termination_SubState"""
        assert event_m10_19_x82(z98=z98)
        """State 6: [Lib] [BEST] [Execution] Andel_Destruction_End_SubState"""
        assert event_m10_19_x83(z97=z97)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Ander_Appearance determination_Termination_SubState"""
        call = event_m10_19_x93(z97=z97, z101=z101, z102=z102, z103=z103, z104=z104, z99=z99)
        if call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Andel_Appearance determination_Termination_SubState"""
            assert event_m10_19_x94(z97=z97)
            """State 1: [Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty_SubState"""
            assert event_m10_19_x92()
            """State 7: [Lib] [BEST] [Condition] Ander_Appearance_Termination_SubState"""
            assert event_m10_19_x80(z97=z97)
            """State 4: [Lib] [BEST] [Execution] Andel_Appearance_Termination_SubState"""
            call = event_m10_19_x81(z97=z97, z100=z100, z99=z99)
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

def event_m10_19_x87(z105=10192600, z106=10190700):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z105: Ander OBJ instance ID
    z106: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z105, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z106, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_19_x88(z105=10192600):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z105: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z105, 10, 0)
    CompareObjState(0, z105, 31, 0)
    CompareObjState(0, z105, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_19_x89(z105=10192600, z106=10190700):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z105: Ander OBJ instance ID
    z106: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z106, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z105, 10, 1)
    CompareObjState(8, z105, 31, 1)
    CompareObjState(8, z105, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_19_x90(z105=10192600, z106=10190700):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z105: Ander OBJ instance ID
    z106: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z106, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z105, 10, 0)
    CompareObjState(0, z105, 31, 0)
    CompareObjState(0, z105, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_19_x91(z105=10192600, z106=10190700):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z105: Ander OBJ instance ID
    z106: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_19_x87(z105=z105, z106=z106)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_19_x88(z105=z105)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_19_x89(z105=z105, z106=z106)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_19_x90(z105=z105, z106=z106)
    """State 6: Rerun"""
    return 1

def event_m10_19_x92():
    """[Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x93(z97=10192600, z101=100360, z102=100300, z103=100400, z104=100461, z99=100743):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_Termination
    z97: Ander OBJ instance ID
    z101: Lighting completion flag
    z102: Bonfire lighting judgment flag ①
    z103: Bonfire lighting judgment flag ②
    z104: Bonfire lighting judgment flag ③
    z99: Andyur encounter flag
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z101, 0)
    CompareEventFlag(8, z102, 1)
    CompareEventFlag(8, z103, 1)
    CompareEventFlag(8, z104, 1)
    CompareEventFlag(8, z99, 0)
    CompareEventFlag(0, z99, 1)
    if ConditionGroup(8):
        """State 2: End state"""
        return 0
    elif ConditionGroup(0):
        """State 3: Rerun"""
        return 1

def event_m10_19_x94(z97=10192600):
    """[Lib] [BEST] [Execution] Andel_Appearance determination_Termination
    z97: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z97, 31)
    """State 2: End state"""
    return 0

def event_m10_19_x95(z95=10192600, z96=10190700):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z95, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z96, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_19_x96(z95=10192600):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z95: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z95, 10, 0)
    CompareObjState(0, z95, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_19_x97(z95=10192600, z96=10190700):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z96, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z95, 10, 1)
    CompareObjState(8, z95, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_19_x98(z95=10192600, z96=10190700):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z96, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z95, 10, 0)
    CompareObjState(0, z95, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_19_x99(z95=10192600, z96=10190700):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z95: Ander OBJ instance ID
    z96: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_19_x95(z95=z95, z96=z96)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_19_x96(z95=z95)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_19_x97(z95=z95, z96=z96)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_19_x98(z95=z95, z96=z96)
    """State 5: Rerun"""
    return 0

def event_m10_19_x100(z80=119020001, z82=119000002):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z80: Lottery determination flag
    z82: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z82) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z80) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_19_x101(z81=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z81: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z81, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_19_x102(z80=119020001, z83=2, z84=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z80: Lottery determination flag
    z83: Number of appearance judgment points
    z84: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z80, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z83)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z84, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_19_x103(z80=119020001, z81=14, z82=119000002, z83=2, z84=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z80: Lottery determination flag
    z81: Random number comparison value
    z82: Defeat flag
    z83: Number of appearance judgment points
    z84: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_19_x100(z80=z80, z82=z82)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_19_x101(z81=z81)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_19_x102(z80=z80, z83=z83, z84=z84)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_19_x112(z80=z80, z84=z84)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_19_x104(val1=_, z92=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z92: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z92) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_19_x105(z88=_, z89=0, z90=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z88: Appearance judgment point ID
    z89: Minimum appearance time
    z90: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z88, z88, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z89, 3, z90)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_19_x106(z91=941, z93=_, z94=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z91: Generator ID
    z93: Appearance start point ID
    z94: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z91, z93, z94)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z91)
    """State 4: Finish"""
    return 0

def event_m10_19_x107(z85=119000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z85: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z85) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_19_x108(z88=_, z89=0, z90=5, z91=941, val1=_, z92=10, z93=_, z94=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z88: Intrusion detection point ID
    z89: Minimum appearance time
    z90: Maximum time to appear
    z91: Generator ID
    val1: Appearance judgment number
    z92: Lottery result point variable
    z93: Appearance start point ID
    z94: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_19_x104(val1=val1, z92=z92)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_19_x105(z88=z88, z89=z89, z90=z90)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_19_x106(z91=z91, z93=z93, z94=z94)
    """State 4: Finish"""
    return 0

def event_m10_19_x109(z86=941, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z86: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z86)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_19_x110(z85=119000002, z87=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z85: Defeat flag
    z87: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z85, 1)
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
                    SetEventFlag(z87, 1)
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

def event_m10_19_x111(z85=119000002, z86=941, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z85: Defeat flag
    z86: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_19_x107(z85=z85)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_19_x109(z86=z86, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_19_x110(z85=z85, z87=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_19_x110(z85=z85, z87=102755)
    """State 5: End state"""
    return 0

def event_m10_19_x112(z80=119020001, z84=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z80: Lottery determination flag
    z84: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z80, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z84, 0)
    """State 3: End state"""
    return 0

def event_m10_19_x113(z77=_):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z77: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z77) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_19_x114(z78=_):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z78: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z78, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x115(z79=_):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z79: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z79, 1)
    """State 2: End state"""
    return 0

def event_m10_19_x116(z77=_, z78=_, z79=_):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z77: Boss destruction flag
    z78: Boss generator ID
    z79: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_19_x113(z77=z77)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_19_x114(z78=z78)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_19_x115(z79=z79)
    """State 4: End state"""
    return 0

def event_m10_19_x117(z75=10191100):
    """[Reproduction] Scaffold moving up and down with lever
    z75: Scaffold instance ID
    """
    """State 0,4: [SEQ19188 compatible] Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 1: Scaffold status determination"""
    if CompareObjStateId(z75, 30, 0):
        """State 2: Navimesh attribute switching_1_Descent"""
        DeleteNavimeshAttribute(100002, 2)
        DeleteNavimeshAttribute(100003, 2)
        DeleteNavimeshAttribute(100005, 2)
        AddNavimeshAttribute(100000, 2)
        AddNavimeshAttribute(100001, 2)
        AddNavimeshAttribute(100004, 2)
    elif CompareObjStateId(z75, 10, 0):
        """State 3: Navimesh attribute switching_2 when rising"""
        DeleteNavimeshAttribute(100000, 2)
        DeleteNavimeshAttribute(100001, 2)
        DeleteNavimeshAttribute(100004, 2)
        DeleteNavimeshAttribute(100005, 2)
        AddNavimeshAttribute(100002, 2)
        AddNavimeshAttribute(100003, 2)
    """State 5: End state"""
    return 0

def event_m10_19_x118(z76=10191010, z75=10191100):
    """[Condition] Scaffold moving up and down with lever
    z76: Lever instance ID
    z75: Scaffold instance ID
    """
    """State 0,1: Lever standby"""
    CompareObjState(0, z76, 74, 0)
    CompareObjState(0, z76, 84, 0)
    assert ConditionGroup(0)
    """State 2: Scaffold status determination"""
    CompareObjState(0, z75, 10, 0)
    CompareObjState(1, z75, 30, 0)
    if ConditionGroup(0):
        """State 3: Descent"""
        return 0
    elif ConditionGroup(1):
        """State 4: Rise"""
        return 1

def event_m10_19_x119(z75=10191100, z76=10191010):
    """[Execute] Scaffolding up and down with lever
    z75: Scaffold instance ID
    z76: Lever instance ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z75, 70)
    """State 2: Navigation mesh attribute switching_3_ moving"""
    AddNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100002, 2)
    AddNavimeshAttribute(100003, 2)
    AddNavimeshAttribute(100004, 2)
    AddNavimeshAttribute(100005, 2)
    """State 5: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z76, 1)
    """State 3: Waiting for scaffolding to finish"""
    CompareObjState(0, z75, 30, 0)
    assert ConditionGroup(0)
    """State 6: Enable key guide for lever"""
    DisableObjKeyGuide(z76, 0)
    """State 4: Navimesh attribute switching_1_Descent"""
    DeleteNavimeshAttribute(100002, 2)
    DeleteNavimeshAttribute(100003, 2)
    DeleteNavimeshAttribute(100005, 2)
    AddNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100004, 2)
    """State 7: End state"""
    return 0

def event_m10_19_x120(z75=10191100, z76=10191010):
    """[Execution] Scaffolding up and down with lever
    z75: Scaffold instance ID
    z76: Lever instance ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z75, 80)
    """State 2: Navigation mesh attribute switching_3_ moving"""
    AddNavimeshAttribute(100000, 2)
    AddNavimeshAttribute(100001, 2)
    AddNavimeshAttribute(100002, 2)
    AddNavimeshAttribute(100003, 2)
    AddNavimeshAttribute(100004, 2)
    AddNavimeshAttribute(100005, 2)
    """State 5: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z76, 1)
    """State 3: Waiting for the scaffold to rise"""
    CompareObjState(0, z75, 10, 0)
    assert ConditionGroup(0)
    """State 6: Enable key guide for lever"""
    DisableObjKeyGuide(z76, 0)
    """State 4: Navimesh attribute switching_2 when rising"""
    DeleteNavimeshAttribute(100000, 2)
    DeleteNavimeshAttribute(100001, 2)
    DeleteNavimeshAttribute(100004, 2)
    DeleteNavimeshAttribute(100005, 2)
    AddNavimeshAttribute(100002, 2)
    AddNavimeshAttribute(100003, 2)
    """State 7: End state"""
    return 0

def event_m10_19_x121(z75=10191100, z76=10191010):
    """[Preset] Scaffold moving up and down with lever
    z75: Scaffold instance ID
    z76: Lever instance ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z75, 0)
    """State 2: [Reproduction] Scaffolding up and down with lever _SubState"""
    assert event_m10_19_x117(z75=z75)
    """State 3: [Condition] Scaffolding up and down with lever_SubState"""
    call = event_m10_19_x118(z76=z76, z75=z75)
    if call.Get() == 0:
        """State 4: [Execution] Scaffolding up and down with lever_Descent_SubState"""
        assert event_m10_19_x119(z75=z75, z76=z76)
    elif call.Get() == 1:
        """State 5: [Execution] Scaffolding up and down with lever"""
        assert event_m10_19_x120(z75=z75, z76=z76)
    """State 6: End state"""
    return 0

def event_m10_19_x122(z74=_):
    """[Reproduction] Floor switch_Folding scaffold
    z74: Navigation switching area ID
    """
    """State 0,1: Navigation switching"""
    DeleteNavimeshAttribute(z74, 2)
    """State 2: End state"""
    return 0

def event_m10_19_x123(z73=_):
    """[Condition] Floor switch_Folding scaffold
    z73: Switch instance ID
    """
    """State 0,1: Did you get on the switch?"""
    CompareObjState(0, z73, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x124(z72=_, z74=_):
    """[Execution] Floor switch
    z72: OBJ instance ID to be run
    z74: Navigation switching area ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z72, 70)
    """State 2: Navigation switching"""
    AddNavimeshAttribute(z74, 2)
    """State 3: End state"""
    return 0

def event_m10_19_x125(z72=_, z73=_, z74=_):
    """[Preset] Floor switch
    z72: OBJ instance ID
    z73: Floor switch instance ID
    z74: Navigation switching area ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z72, 0)
    """State 2: [Reproduction] OBJ action _SubState with floor switch"""
    assert event_m10_19_x122(z74=z74)
    """State 3: [Condition] OBJ action _SubState with floor switch"""
    assert event_m10_19_x123(z73=z73)
    """State 4: [Execution] OBJ action with floor switch_Folding scaffolding_SubState"""
    assert event_m10_19_x124(z72=z72, z74=z74)
    """State 5: End state"""
    return 0

def event_m10_19_x126(z66=10191610, z67=600000, z68=600010, z69=10191615, z70=10191620, z71=600020):
    """[Reproduction] Burning furnace_Shutter and damage
    z66: Shutter instance ID
    z67: Damage area ID1
    z68: Damage area ID2
    z69: Damipoli instance ID under shutter
    z70: Damipoli instance ID on the ladder
    z71: Navimesh change point ID
    """
    """State 0,1: Has the shutter already closed?"""
    if CompareObjStateId(z66, 10, 0):
        """State 6: Fire on the ladder"""
        ChangeObjState(z70, 10)
        """State 5: Flame regeneration under the shutter"""
        ChangeObjState(z69, 10)
        """State 3: Burning damage ON"""
        EnableDamageArea(z67, 1)
        EnableDamageArea(z68, 1)
        """State 9: End state"""
        return 0
    else:
        """State 2: Burning damage disabled"""
        EnableDamageArea(z67, 0)
        EnableDamageArea(z68, 0)
        """State 4: Shutter flame stop"""
        ChangeObjState(z69, 20)
        """State 7: Flame stop on ladder"""
        ChangeObjState(z70, 20)
        """State 8: Navigation mesh change"""
        DeleteNavimeshAttribute(z71, 2)
        """State 10: Reproduce and finish"""
        return 1

def event_m10_19_x127(z65=10191550):
    """[Condition] Burning furnace_Shutter and damage
    z65: Valve instance ID
    """
    """State 0,1: Wait for valve operation"""
    CompareObjState(0, z65, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x128(z66=10191610, z67=600000, z68=600010, z69=10191615, z70=10191620, z71=600020):
    """[Execution] Burning furnace_Shutter and damage
    z66: Shutter instance ID
    z67: Damage area ID1
    z68: Damage area ID2
    z69: Damipoli instance ID under shutter
    z70: Damipoli instance ID on the ladder
    z71: Navimesh change point ID
    """
    """State 0,1: Shutter close animation playback"""
    ChangeObjState(z66, 70)
    """State 5: Did the shutter close to a certain level?"""
    CompareObjState(0, z66, 72, 0)
    assert ConditionGroup(0)
    """State 2: Burning damage disabled"""
    EnableDamageArea(z67, 0)
    EnableDamageArea(z68, 0)
    """State 3: Stop flame under shutter"""
    ChangeObjState(z69, 20)
    """State 4: Flame stop on ladder"""
    ChangeObjState(z70, 20)
    """State 6: Is the shutter completely closed?"""
    CompareObjState(0, z66, 20, 0)
    assert ConditionGroup(0)
    """State 7: Navigation mesh change"""
    DeleteNavimeshAttribute(z71, 2)
    """State 8: End state"""
    return 0

def event_m10_19_x129(z65=10191550, z66=10191610, z67=600000, z68=600010, z69=10191615, z70=10191620,
                      z71=600020):
    """[Preset] Burning furnace_Shutter and damage
    z65: Valve instance ID
    z66: Shutter instance ID
    z67: Damage area ID1
    z68: Damage area ID2
    z69: Damipoli instance ID under shutter
    z70: Damipoli instance ID on the ladder
    z71: Navimesh change point ID
    """
    """State 0,1: Disable OBJ synchronization"""
    SetObjSync(z66, 0)
    """State 2: [Reproduction] Burning furnace_Shutter and damage_SubState"""
    call = event_m10_19_x126(z66=z66, z67=z67, z68=z68, z69=z69, z70=z70, z71=z71)
    if call.Get() == 0:
        """State 3: [Condition] Burning furnace_Shutter and damage_SubState"""
        assert event_m10_19_x127(z65=z65)
        """State 4: [Execution] Burning furnace_Shutter and damage_SubState"""
        assert event_m10_19_x128(z66=z66, z67=z67, z68=z68, z69=z69, z70=z70, z71=z71)
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

def event_m10_19_x131(z62=10191350, z63=_, z64=_):
    """[Condition] Lever to stop all flame images
    z62: Lever OBJ object instance ID
    z63: Lever state_Start confirmed
    z64: Lever state_Standby
    """
    """State 0,1: Is the lever ready to start?"""
    CompareObjState(0, z62, z63, 0)
    assert ConditionGroup(0)
    """State 2: Is the lever in standby mode?"""
    CompareObjState(0, z62, z64, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x132(z60=119000040, z61=_):
    """[Execute] Lever that stops all flame images
    z60: Flame statue working flag
    z61: Flag setting
    """
    """State 0,1: Flame flag operation flag switching"""
    SetEventFlag(z60, z61)
    """State 2: End state"""
    return 0

def event_m10_19_x133(z53=119000081):
    """[Reproduction] Flame linked to boss action
    z53: Boss destruction flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z53) != 1:
        """State 2: Undefeated"""
        return 0
    else:
        """State 3: Defeated"""
        return 1

def event_m10_19_x134(z49=_, z50=10192200, z51=10192201, z59=_):
    """[Execution] Flames linked to boss actions
    z49: OBJ state ID for ON / OFF
    z50: OBJ instance ID of stone statue 1
    z51: OBJ instance ID of stone statue 2
    z59: ON / OFF completion confirmation OBJ state ID
    """
    """State 0,1: OBJ status change"""
    ChangeObjState(z50, z49)
    ChangeObjState(z51, z49)
    """State 2: Has the OBJ status change been completed?"""
    CompareObjState(8, z50, z59, 0)
    CompareObjState(8, z51, z59, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_19_x135(z54=_, z57=30, z58=_):
    """[Reproduction] Floor switch _ Molten iron pot
    z54: OBJ instance ID to be run
    z57: Hit group ID
    z58: Grand material ID
    """
    """State 0,1: Gimmick already activated?"""
    if CompareObjStateId(z54, 20, 0):
        """State 3: Activate damage"""
        SetGroundMaterial(z57, z58, 1)
        """State 5: Simple end"""
        return 1
    else:
        """State 2: Invalidate damage area"""
        SetGroundMaterial(z57, z58, 0)
        """State 4: End state"""
        return 0

def event_m10_19_x136(z55=_):
    """[Conditions] Floor switch_molten iron pot
    z55: Switch instance ID
    """
    """State 0,1: Did you get on the switch?"""
    CompareObjState(0, z55, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x137(z54=_, z55=_, z56=_, z57=30, z58=_):
    """[Execution] Floor switch _ Molten iron pot
    z54: OBJ instance ID to be run
    z55: Floor switch instance ID
    z56: Display OBJ instance ID
    z57: Hit group ID
    z58: Grand material ID
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z54, 70)
    assert (GetStateTime() > 4.5) != 0
    """State 3: OBJ display"""
    ChangeObjState(z56, 20)
    """State 2: Activate damage"""
    SetGroundMaterial(z57, z58, 1)
    """State 4: End state"""
    return 0

def event_m10_19_x138(z54=_, z55=_, z56=_, z57=30, z58=_):
    """[Preset] Floor switch _ Molten iron pot
    z54: OBJ instance ID
    z55: Floor switch instance ID
    z56: Display OBJ instance ID
    z57: Hit group ID
    z58: Grand material ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z54, 0)
    """State 2: [Reproduction] Floor switch_molten iron_SubState"""
    call = event_m10_19_x135(z54=z54, z57=z57, z58=z58)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Conditions] Floor switch _ Molten iron _ SubState"""
        assert event_m10_19_x136(z55=z55)
        """State 4: [Execution] Floor switch_molten iron_SubState"""
        assert event_m10_19_x137(z54=z54, z55=z55, z56=z56, z57=z57, z58=z58)
    """State 5: End state"""
    return 0

def event_m10_19_x139(z23=10191610):
    """[Reproduction] Burning furnace _ flame when opening the door
    z23: Shutter OBJ instance ID
    """
    """State 0,1: Is the shutter closed?"""
    if CompareObjStateId(z23, 20, 0):
        """State 3: The shutter is closed"""
        return 1
    else:
        """State 2: The shutter is open"""
        return 0

def event_m10_19_x140(z23=10191610, z24=_, z25=_):
    """[Preset] Burning furnace
    z23: Shutter OBJ instance ID
    z24: Door OBJ instance ID
    z25: Instance ID of OBJ that emits flame
    """
    """State 0,1: [Reproduction] Burning furnace _ SubState"""
    call = event_m10_19_x139(z23=z23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Burning furnace_Open door and flame_SubState"""
        call = event_m10_19_x173(z23=z23, z24=z24)
        if call.Get() == 2:
            pass
        elif call.Get() == 0:
            """State 4: [Execution] Burning furnace _ Flame when opening the door _ Flame operation _ SubState"""
            call = event_m10_19_x174(z25=z25, z23=z23, z24=z24)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                """State 7: Rerun"""
                Label('L0')
                return 1
        elif call.Get() == 1:
            """State 5: [Execution] Burning furnace _ Flame when opening the door _ Flame stop _ SubState"""
            call = event_m10_19_x175(z25=z25, z23=z23, z24=z24)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                Goto('L0')
    """State 2: [Execution] Burning furnace _ Flame when opening the door _ Flame complete stop _ SubState"""
    assert event_m10_19_x141(z25=z25)
    """State 6: The shutter is closed"""
    return 0

def event_m10_19_x141(z25=_):
    """[Execution] Burning furnace _ Flame when opening the door _ Flame complete stop
    z25: Instance ID of OBJ that emits flame
    """
    """State 0,1: Complete stop of fire from the door"""
    ChangeObjState(z25, 20)
    """State 2: Has the flame stopped completely?"""
    CompareObjState(0, z25, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_19_x142(z47=806, z52=93050010):
    """[Condition] Fire linked to the boss's action
    z47: Boss generator ID
    z52: Boss special state effect ID
    """
    """State 0,1: Boss status judgment"""
    ChrHasSpEffect(0, z47, z52, 1)
    IsChrDead(1, z47)
    if ConditionGroup(0):
        """State 2: Turn off due to status change"""
        return 0
    elif ConditionGroup(1):
        """State 3: Boss death"""
        return 1

def event_m10_19_x143(z47=806, z48=71, z49=70, z50=10192200, z51=10192201, z52=93050010, z53=119000081):
    """[Preset] Flames linked to boss actions
    z47: Boss generator ID
    z48: State ID with stone statue on
    z49: State ID with stone statue flame OFF
    z50: OBJ instance ID of stone statue 1
    z51: OBJ instance ID of stone statue 2
    z52: Boss special state effect ID
    z53: Boss destruction flag
    """
    """State 0,1: [Reproduction] Flame_SubState linked to the boss's behavior"""
    call = event_m10_19_x133(z53=z53)
    if call.Get() == 0:
        """State 4: [Condition] Fire linked to the boss's behavior_Boss is in anger state_SubState"""
        call = event_m10_19_x142(z47=z47, z52=z52)
        if call.Get() == 0:
            """State 2: [Execution] Flames linked to boss actions"""
            assert event_m10_19_x134(z49=z49, z50=z50, z51=z51, z59=30)
            """State 5: [Conditions] Flames linked to boss actions_Boss dies_SubState"""
            assert event_m10_19_x144(z47=z47)
            """State 3: [Execution] Flames linked to boss actions"""
            assert event_m10_19_x134(z49=z48, z50=z50, z51=z51, z59=10)
        elif call.Get() == 1:
            pass
    elif call.Get() == 1:
        pass
    """State 6: Finish"""
    return 0

def event_m10_19_x144(z47=806):
    """[Condition] Fire linked to the boss's action
    z47: Boss generator ID
    """
    """State 0,1: Boss status judgment"""
    IsChrDead(0, z47)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x145(z45=10191110, z43=10191020, z44=10191021, z46=1900000):
    """[Reproduction] Guillotine door
    z45: Guillotine door OBJ instance ID
    z43: Lever 1_OBJ instance ID
    z44: Lever 2_OBJ instance ID
    z46: Navigation change point ID
    """
    """State 0,1: Is the blade in the initial state?"""
    if CompareObjStateId(z45, 10, 1):
        """State 2: Disabling the key guide of the lever"""
        DisableObjKeyGuide(z43, 1)
        DisableObjKeyGuide(z44, 1)
        """State 3: Navigation mesh switching: Allowed to pass"""
        DeleteNavimeshAttribute(z46, 2)
        """State 4: Blade lowering standby"""
        CompareObjState(0, z45, 10, 0)
        assert CompareObjStateId(z45, 10, 0)
        """State 5: Enable key guide for lever"""
        DisableObjKeyGuide(z43, 0)
        DisableObjKeyGuide(z44, 0)
        """State 6: Navi mesh switching: Not allowed"""
        AddNavimeshAttribute(z46, 2)
    else:
        pass
    """State 7: End state"""
    return 0

def event_m10_19_x146(z43=10191020, z44=10191021):
    """[Conditions] Guillotine door
    z43: Lever 1_OBJ instance ID
    z44: Lever 2_OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z43, 74, 0)
    CompareObjState(0, z43, 84, 0)
    CompareObjState(0, z44, 74, 0)
    CompareObjState(0, z44, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x147(z45=10191110, z43=10191020, z44=10191021, z46=1900000):
    """[Execution] Guillotine door
    z45: Guillotine door OBJ instance ID
    z43: Lever 1_OBJ instance ID
    z44: Lever 2_OBJ instance ID
    z46: Navigation change point ID
    """
    """State 0,1: The door blade rises: 70"""
    ChangeObjState(z45, 70)
    """State 3: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z43, 1)
    DisableObjKeyGuide(z44, 1)
    """State 6: Blade rising standby"""
    CompareObjState(0, z45, 30, 0)
    assert ConditionGroup(0)
    """State 5: Navigation mesh switching: Allowed to pass"""
    DeleteNavimeshAttribute(z46, 2)
    """State 2: Blade lowering standby"""
    CompareObjState(0, z45, 10, 0)
    assert ConditionGroup(0)
    """State 4: Enable key guide for lever"""
    DisableObjKeyGuide(z43, 0)
    DisableObjKeyGuide(z44, 0)
    """State 7: Navi mesh switching: Not allowed"""
    AddNavimeshAttribute(z46, 2)
    """State 8: End state"""
    return 0

def event_m10_19_x148(z43=10191020, z44=10191021, z45=10191110, z46=1900000):
    """[Preset] Guillotine door
    z43: Lever 1_OBJ instance ID
    z44: Lever 2_OBJ instance ID
    z45: OBJ instance ID of the guillotine door
    z46: Navigation change point ID
    """
    """State 0,1: [Reproduction] Guillotine door_SubState"""
    assert event_m10_19_x145(z45=z45, z43=z43, z44=z44, z46=z46)
    """State 2: [Condition] Guillotine door_SubState"""
    assert event_m10_19_x146(z43=z43, z44=z44)
    """State 3: [Execution] Guillotine door_SubState"""
    assert event_m10_19_x147(z45=z45, z43=z43, z44=z44, z46=z46)
    """State 4: End state"""
    return 0

def event_m10_19_x149(z40=119020012):
    """[Reproduction] Vegrant generation determination
    z40: Vegrant generation flag
    """
    """State 0,1: Has it already been judged?"""
    if GetEventFlag(z40) != 0:
        """State 3: Judged"""
        return 1
    else:
        """State 2: Undecided"""
        return 0

def event_m10_19_x150(z41=119000081):
    """[Condition] Vegrant generation determination
    z41: Demon Knight Defeat Flag
    """
    """State 0,1: Demon Knight Defeat Determination"""
    CompareEventFlag(0, z41, 1)
    CompareEventFlag(1, z41, 0)
    if ConditionGroup(0):
        """State 2: Defeated"""
        return 0
    elif ConditionGroup(1):
        """State 3: Not defeated"""
        return 1

def event_m10_19_x151(z39=119020010, z40=119020012, z42=_):
    """[Execution] Vegrant generation determination
    z39: Vagrant creation permission flag
    z40: Vegrant generation flag
    z42: Generation permission ON / OFF
    """
    """State 0,1: Vagrant creation permission flag"""
    SetEventFlag(z39, z42)
    """State 2: Vagrant generation determination flag ON"""
    SetEventFlag(z40, 1)
    """State 3: End state"""
    return 0

def event_m10_19_x152(z39=119020010, z40=119020012, z41=119000081):
    """[Preset] Vegrant generation determination
    z39: Vagrant creation permission flag
    z40: Vegrant generation flag
    z41: Demon Knight Defeat Flag
    """
    """State 0,1: [Reproduction] Vegrant generation determination_SubState"""
    call = event_m10_19_x149(z40=z40)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Vegrant generation determination_SubState"""
        call = event_m10_19_x150(z41=z41)
        if call.Get() == 1:
            """State 4: [Execution] Vegrant generation determination_OFF_SubState"""
            assert event_m10_19_x151(z39=z39, z40=z40, z42=0)
        elif call.Get() == 0:
            """State 2: [Execution] Vegrant generation determination_ON_SubState"""
            assert event_m10_19_x151(z39=z39, z40=z40, z42=1)
    """State 5: End state"""
    return 0

def event_m10_19_x153(z34=119000087, z35=807, z36=1502000, z37=2, z38=119000086):
    """[Preset] Molten iron daemon
    z34: Flag to perform first battle or rematch determination
    z35: Molten Daemon Generator ID
    z36: Point ID for relocation during rematch
    z37: Activation state ID at the time of rematch
    z38: Destruction flag of molten iron demon
    """
    """State 0,4: [Reproduction] Molten Iron Daemon_Initial Location Change_SubState"""
    call = event_m10_19_x154(z38=z38)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Molten iron daemon_Initial location change_SubState"""
        call = event_m10_19_x155(z34=z34)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 3: Waiting for white door"""
            CompareObjState(0, 10190610, 100, 0)
            assert ConditionGroup(0)
            """State 2: Wait for save"""
            assert (GetStateTime() > 0.1) != 0
            """State 6: [Execution] Molten iron daemon_Initial location change_SubState"""
            assert event_m10_19_x156(z35=z35, z36=z36, z37=z37)
            """State 1: Wait for battle"""
            CompareEventFlag(0, 119000088, 1)
            assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m10_19_x154(z38=119000086):
    """[Reproduction] Molten iron daemon
    z38: Destruction flag of molten iron demon
    """
    """State 0,1: Are you destroying the molten iron demon?"""
    if GetEventFlag(z38) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Undefeated"""
        return 0

def event_m10_19_x155(z34=119000087):
    """[Condition] Molten iron daemon_Initial location change
    z34: Flag to perform first battle or rematch determination
    """
    """State 0,1: Is it the first game? Is it a rematch?"""
    CompareEventFlag(0, z34, 0)
    if ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m10_19_x156(z35=807, z36=1502000, z37=2):
    """[Execution] Molten iron daemon
    z35: Molten Daemon Generator ID
    z36: Point ID for relocation during rematch
    z37: Activation state ID at the time of rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z35, z36)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z35, z37)
    """State 3: End state"""
    return 0

def event_m10_19_x157(z31=10191300):
    """[Reproduction] Bridge descending with lever
    z31: OBJ instance ID of the bridge
    """
    """State 0,1: Is the bridge in a finished state"""
    if CompareObjStateId(z31, 20, 0):
        pass
    elif CompareObjStateId(z31, 71, 0):
        pass
    elif CompareObjStateId(z31, 81, 0):
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
    if CompareObjStateId(z31, 80, 0):
        pass
    elif CompareObjStateId(z31, 40, 0):
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
    if CompareObjStateId(z31, 70, 0):
        """State 7: Navi mesh switching_falling left"""
        Label('L2')
        AddNavimeshAttribute(500002, 2)
        DeleteNavimeshAttribute(500000, 2)
        """State 9: The left is falling"""
        return 1
    elif CompareObjStateId(z31, 30, 0):
        Goto('L2')
    else:
        """State 4: Navimesh switching_up"""
        DeleteNavimeshAttribute(500002, 2)
        """State 8: initial state"""
        return 0

def event_m10_19_x158(z32=10191002, z33=10191000):
    """[Condition] Bridge descending with lever_Initial
    z32: Right lever OBJ instance ID
    z33: Left lever OBJ instance ID
    """
    """State 0,1: Waiting for two levers to start"""
    CompareObjState(0, z32, 72, 0)
    CompareObjState(1, z33, 72, 0)
    if ConditionGroup(0):
        """State 2: Right falls"""
        return 0
    elif ConditionGroup(1):
        """State 3: The left is falling"""
        return 1

def event_m10_19_x159(z31=10191300, z32=10191002, z33=10191000):
    """[Execution] Bridge descending with lever_Initial right fall
    z31: OBJ instance ID of the bridge
    z32: Right lever OBJ instance ID
    z33: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z32, 1)
    DisableObjKeyGuide(z33, 1)
    """State 1: Bridge _ right falls: 80"""
    ChangeObjState(z31, 80)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z31, 40, 0)
    """State 4: Navimesh switching_falling right"""
    AddNavimeshAttribute(500002, 2)
    DeleteNavimeshAttribute(500001, 2)
    """State 5: Lever key guide enabled"""
    DisableObjKeyGuide(z32, 0)
    DisableObjKeyGuide(z33, 0)
    """State 6: Waiting for the left to fall"""
    return 0

def event_m10_19_x160(z31=10191300, z32=10191002, z33=10191000):
    """[Execution] Bridge descending with lever _ Initial left fall
    z31: OBJ instance ID of the bridge
    z32: Right lever OBJ instance ID
    z33: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z32, 1)
    DisableObjKeyGuide(z33, 1)
    """State 1: Bridge _ left falls: 70"""
    ChangeObjState(z31, 70)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z31, 30, 0)
    """State 5: Navi mesh switching_falling left"""
    AddNavimeshAttribute(500002, 2)
    DeleteNavimeshAttribute(500000, 2)
    """State 4: Lever key guide enabled"""
    DisableObjKeyGuide(z32, 0)
    DisableObjKeyGuide(z33, 0)
    """State 6: Waiting for the right fall"""
    return 0

def event_m10_19_x161(z33=_):
    """[Condition] Bridge descending by lever_2
    z33: Second lever OBJ instance ID
    """
    """State 0,1: Waiting for lever to start"""
    CompareObjState(0, z33, 72, 0)
    assert ConditionGroup(0)
    """State 2: Fall"""
    return 0

def event_m10_19_x162(z31=10191300, z32=10191002, z33=10191000):
    """[Execution] Bridge descending with lever _ 2nd right fall
    z31: OBJ instance ID of the bridge
    z32: Right lever OBJ instance ID
    z33: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z32, 1)
    DisableObjKeyGuide(z33, 1)
    """State 1: Bridge_Right falls: 71"""
    ChangeObjState(z31, 71)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z31, 20, 0)
    """State 5: Navi mesh switching"""
    AddNavimeshAttribute(500000, 2)
    AddNavimeshAttribute(500001, 2)
    DeleteNavimeshAttribute(500003, 2)
    """State 4: Lever key guide enabled"""
    DisableObjKeyGuide(z32, 0)
    DisableObjKeyGuide(z33, 0)
    """State 6: Complete"""
    return 0

def event_m10_19_x163(z31=10191300, z32=10191002, z33=10191000):
    """[Execution] Bridge descending with lever _ 2nd left fall
    z31: OBJ instance ID of the bridge
    z32: Right lever OBJ instance ID
    z33: Left lever OBJ instance ID
    """
    """State 0,2: Lever key guide disabled"""
    DisableObjKeyGuide(z32, 1)
    DisableObjKeyGuide(z33, 1)
    """State 1: Bridge _ left falls: 81"""
    ChangeObjState(z31, 81)
    """State 3: Waiting for falling anime"""
    assert CompareObjStateId(z31, 20, 0)
    """State 5: Navi mesh switching"""
    AddNavimeshAttribute(500000, 2)
    AddNavimeshAttribute(500001, 2)
    DeleteNavimeshAttribute(500003, 2)
    """State 4: Lever key guide enabled"""
    DisableObjKeyGuide(z32, 0)
    DisableObjKeyGuide(z33, 0)
    """State 6: Complete"""
    return 0

def event_m10_19_x164(z31=10191300, z32=10191002, z33=10191000):
    """[Preset] Bridge descending with lever
    z31: OBJ instance ID of the bridge
    z32: Right lever OBJ instance ID
    z33: Left lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Bridge descending with a lever_SubState"""
    call = event_m10_19_x157(z31=z31)
    if call.Get() == 0:
        """State 7: [Condition] Bridge descending with lever_Initial_SubState"""
        call = event_m10_19_x158(z32=z32, z33=z33)
        if call.Get() == 0:
            """State 4: [Execution] Bridge descending with lever_Initial right fall_SubState"""
            assert event_m10_19_x159(z31=z31, z32=z32, z33=z33)
        elif call.Get() == 1:
            """State 5: [Execute] Bridge descending with lever_Initial left fall_SubState"""
            assert event_m10_19_x160(z31=z31, z32=z32, z33=z33)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 2:
        """State 6: [Condition] Bridge descending with lever _ 2nd_SubState"""
        assert event_m10_19_x161(z33=z33)
        """State 3: [Execution] Bridge descending with lever _ 2nd fall left_SubState"""
        assert event_m10_19_x163(z31=z31, z32=z32, z33=z33)
    elif call.Get() == 1:
        """State 8: [Condition] Bridge descending with lever _ 2nd _ SubState"""
        assert event_m10_19_x161(z33=z32)
        """State 2: [Execution] Bridge descending with lever_2 Falling right_SubState"""
        assert event_m10_19_x162(z31=z31, z32=z32, z33=z33)
    elif call.Get() == 3:
        pass
    """State 10: Finish"""
    return 1

def event_m10_19_x165(z27=10194999, z28=20, z29=1700000, z30=119020030):
    """[Preset] Bridge destroyed by enemies
    z27: Instance ID of the bridge OBJ
    z28: State ID of the destruction state of the bridge OBJ
    z29: Navimesh change point ID
    z30: Bridge destruction complete flag
    """
    """State 0,1: [Reproduction] Bridge _SubState destroyed by enemies"""
    call = event_m10_19_x166(z27=z27, z28=z28)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Bridge destroyed by enemy _SubState"""
        assert event_m10_19_x167(z27=z27, z28=z28)
    """State 3: [Execution] Bridge _SubState destroyed by enemies"""
    assert event_m10_19_x168(z29=z29, z30=z30)
    """State 4: End state"""
    return 0

def event_m10_19_x166(z27=10194999, z28=20):
    """[Reproduction] Bridge destroyed by enemies
    z27: Instance ID of the bridge OBJ
    z28: State ID of the destruction state of the bridge OBJ
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z27, z28, 0):
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Undestructed"""
        return 0

def event_m10_19_x167(z27=10194999, z28=20):
    """[Condition] Bridge destroyed by enemies
    z27: Instance ID of the bridge OBJ
    z28: State ID of the destruction state of the bridge OBJ
    """
    """State 0,1: OBJ destruction determination"""
    CompareObjState(0, z27, z28, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x168(z29=1700000, z30=119020030):
    """[Execution] Bridge destroyed by enemies
    z29: Navimesh change point ID
    z30: Bridge destruction complete flag
    """
    """State 0,1: Navigation mesh change"""
    AddNavimeshAttribute(z29, 2)
    """State 2: Bridge destruction complete flag: ON"""
    SetEventFlag(z30, 1)
    """State 3: End state"""
    return 0

def event_m10_19_x169():
    """[Reproduction] Vegrant Deletion Determination_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x170(z26=5000):
    """[Condition] Vegrant removal determination
    z26: Generator ID
    """
    """State 0,2: Has a vegrant been generated?"""
    IsChrActive(0, z26, 1)
    assert ConditionGroup(0)
    """State 1: Has Vegrant finished the return action?"""
    CompareChrEzStateValue(0, z26, 7, 1, 0)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m10_19_x171(z26=5000):
    """[Execution] Vegrant removal determination
    z26: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z26, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x172(z26=5000):
    """[Preset] Vegrant removal judgment
    z26: Generator ID
    """
    """State 0,1: [Reproduction] Vegrant deletion judgment_empty_SubState"""
    assert event_m10_19_x169()
    """State 3: [Condition] Vegrant deletion determination_SubState"""
    assert event_m10_19_x170(z26=z26)
    """State 2: [Execution] Vegrant deletion determination_SubState"""
    assert event_m10_19_x171(z26=z26)
    """State 4: End state"""
    return 0

def event_m10_19_x173(z23=10191610, z24=_):
    """[Condition] Burning furnace _ Flame when opening the door
    z23: Shutter OBJ instance ID
    z24: Door OBJ instance ID
    """
    """State 0,1: Shutter and door status judgment"""
    CompareObjState(0, z23, 20, 0)
    CompareObjState(1, z24, 30, 0)
    CompareObjState(2, z24, 84, 0)
    CompareObjState(2, z24, 10, 0)
    if ConditionGroup(0):
        """State 4: The shutter is closed"""
        return 2
    elif ConditionGroup(1):
        """State 2: The door is open"""
        return 0
    elif ConditionGroup(2):
        """State 3: The door is closed"""
        return 1

def event_m10_19_x174(z25=_, z23=10191610, z24=_):
    """[Execution] Burning furnace _ Flame when opening the door _ Flame operation
    z25: Instance ID of OBJ that emits flame
    z23: Shutter OBJ instance ID
    z24: Door OBJ instance ID
    """
    """State 0,1: Flame state transition"""
    ChangeObjState(z25, 30)
    """State 2: Shutter and door status judgment"""
    CompareObjState(0, z23, 20, 0)
    CompareObjState(1, z24, 30, 1)
    if ConditionGroup(0):
        """State 4: The shutter is closed"""
        return 1
    elif ConditionGroup(1):
        """State 3: There was a change in the condition of the door"""
        return 0

def event_m10_19_x175(z25=_, z23=10191610, z24=_):
    """[Execution] Burning furnace _ Flame when opening the door _ Flame stop
    z25: Instance ID of OBJ that emits flame
    z23: Shutter OBJ instance ID
    z24: Door OBJ instance ID
    """
    """State 0,1: Flame state transition"""
    ChangeObjState(z25, 10)
    """State 2: Shutter and door status judgment"""
    CompareObjState(0, z23, 20, 0)
    CompareObjState(8, z24, 10, 1)
    CompareObjState(8, z24, 84, 1)
    if ConditionGroup(0):
        """State 4: The shutter is closed"""
        return 1
    elif ConditionGroup(8):
        """State 3: There was a change in the condition of the door"""
        return 0

def event_m10_19_x176(z21=119020016):
    """[Reproduction] Pledge: Kanemori_Contribution UP_Intruder generation determination
    z21: Intruder generation determination flag
    """
    """State 0,1: Has it already been judged?"""
    if GetEventFlag(z21) != 0:
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

def event_m10_19_x178(z20=119020014, z21=119020016, z22=_):
    """[Execution] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment
    z20: Intruder generation permission flag
    z21: Intruder generation determination flag
    z22: Generation permission ON / OFF
    """
    """State 0,1: Intruder generation permission flag"""
    SetEventFlag(z20, z22)
    """State 2: Intruder generation determination flag ON"""
    SetEventFlag(z21, 1)
    """State 3: End state"""
    return 0

def event_m10_19_x179(z20=119020014, z21=119020016):
    """[Preset] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment
    z20: Intruder generation permission flag
    z21: Intruder generation determination flag
    """
    """State 0,1: [Reproduction] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_SubState"""
    call = event_m10_19_x176(z21=z21)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_SubState"""
        call = event_m10_19_x177()
        if call.Get() == 0:
            """State 4: [Execution] Pledge: Kanemori_Contribution UP_Intruder Generation Judgment_ON_SubState"""
            assert event_m10_19_x178(z20=z20, z21=z21, z22=1)
        elif call.Get() == 1:
            """State 2: [Execution] Pledge: Kanemori_Contribution UP_Intruder Generation Determination_OFF_SubState"""
            Label('L0')
            assert event_m10_19_x178(z20=z20, z21=z21, z22=0)
    elif call.Get() == 2:
        Goto('L0')
    """State 5: End state"""
    return 0

def event_m10_19_x180(z17=119020018, z19=119020014):
    """[Reproduction] Pledge: Kanemori_Contribution UP
    z17: Intruder Destruction Flag
    z19: Intruder generation permission flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 3: Has an intruder been generated?"""
        if GetEventFlag(119020014) != 0:
            """State 2: Has the intruder been destroyed?"""
            if GetEventFlag(z17) != 1:
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

def event_m10_19_x181(z16=7007):
    """[Condition] Pledge: Kanemori_Contribution UP
    z16: Intruder generator ID
    """
    """State 0,1: Pledge and intruder defeat determination"""
    IsChrDead(8, z16)
    IsPlayerInCovenant(8, 6, 1)
    IsChrDead(9, z16)
    IsPlayerInCovenant(9, 6, 0)
    if ConditionGroup(8):
        """State 2: Increased contribution"""
        return 0
    elif ConditionGroup(9):
        """State 3: do nothing"""
        return 1

def event_m10_19_x182(z17=119020018):
    """[Execution] Pledge: Kanemori_Contribution UP
    z17: Intruder Destruction Flag
    """
    """State 0,1: Kanemori: Increased contribution"""
    AddPlayerCovenantContribution(6, 1)
    """State 2: Defeat flag ON"""
    SetEventFlag(z17, 1)
    assert GetEventFlag(z17) != 0
    """State 3: Finish"""
    return 0

def event_m10_19_x183(z16=7007, z17=119020018, z18=119020014):
    """[Preset] Pledge: Kanemori_Contribution UP
    z16: Intruder generator ID
    z17: Intruder Destruction Flag
    z18: Intruder generation permission flag
    """
    """State 0,1: [Reproduction] Pledge: Kanemori_Contribution UP_SubState"""
    call = event_m10_19_x180(z17=z17, z19=119020014)
    if call.Get() == 0:
        """State 3: [Condition] Pledge: Kanemori_Contribution UP_SubState"""
        call = event_m10_19_x181(z16=z16)
        if call.Get() == 0:
            """State 2: [Execution] Pledge: Kanemori_Contribution UP_SubState"""
            assert event_m10_19_x182(z17=z17)
        elif call.Get() == 1:
            """State 4: [Execution] Pledge: Kanemori_Contribution UP_Destroy only_SubState"""
            assert event_m10_19_x184(z17=z17)
    elif call.Get() == 1:
        pass
    """State 5: Finish"""
    return 0

def event_m10_19_x184(z17=119020018):
    """[Execution] Pledge: Kanemori_Contribution UP_Destroy only
    z17: Intruder Destruction Flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z17, 1)
    assert GetEventFlag(z17) != 0
    """State 2: Finish"""
    return 0

def event_m10_19_x185(z12=119000087):
    """[Reproduction] Molten iron demon
    z12: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z12) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_19_x186(z10=10190610):
    """[Condition] Molten iron demon
    z10: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z10, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_19_x187(z11=101910, z12=119000087, z13=1501000, z14=1, z15=119000088):
    """[Execution] Molten Iron Daemon
    z11: Poly play ID
    z12: Poly drama played flag
    z13: Warp point ID
    z14: Weight until poly play
    z15: Boss generation flag
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z11, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: During poly play: Generation flag ON"""
    SetEventFlag(z15, 1)
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z12, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z13)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_19_x188(z10=10190610, z11=101910, z12=119000087, z13=1501000, z14=1, z15=119000088):
    """[Preset] Molten Iron Demon_Poly Play
    z10: White door instance ID
    z11: Poly play ID
    z12: Poly drama played flag
    z13: Warp point ID
    z14: Wait time
    z15: Boss generation flag
    """
    """State 0,1: [Reproduction] Molten Iron Daemon_Poly Play_SubState"""
    call = event_m10_19_x185(z12=z12)
    if call.Get() == 0:
        """State 3: [Condition] Molten iron daemon_Poly play_SubState"""
        assert event_m10_19_x186(z10=z10)
        """State 2: [Execution] Molten Iron Daemon_Poly Play_SubState"""
        assert event_m10_19_x187(z11=z11, z12=z12, z13=z13, z14=z14, z15=z15)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_19_x189():
    """[DLC] [Reproduction] Stone monument displayed in text"""
    """State 0,1: End state"""
    return 0

def event_m10_19_x190(z9=_):
    """[DLC] [Condition] Stone monument displayed in text
    z9: Stele OBJ instance ID
    """
    """State 0,1: Wait for decision to check"""
    IsObjSearched(0, z9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_19_x191(action1=_, z9=_):
    """[DLC] [execution] Stone monument displayed as text
    action1: Text ID
    z9: Stele OBJ instance ID
    """
    """State 0,2: Disable key guide"""
    DisableObjKeyGuide(z9, 1)
    """State 1: Text display"""
    DisplayEventMessage(action1, 0, 0, 0)
    assert (GetStateTime() > 1.5) != 0
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z9, 0)
    """State 4: End state"""
    return 0

def event_m10_19_x192(z9=_, action1=_):
    """[DLC] [Preset] Stone monument displayed as text
    z9: Stele OBJ instance ID
    action1: Text ID
    """
    """State 0,1: [DLC] [Reproduction] Stone monument_SubState displayed in text"""
    assert event_m10_19_x189()
    """State 3: [DLC] [Condition] Stone monument_SubState displayed in text"""
    assert event_m10_19_x190(z9=z9)
    """State 2: [DLC] [Execution] Stone monument_SubState displayed in text"""
    assert event_m10_19_x191(action1=action1, z9=z9)
    """State 4: End state"""
    return 0

def event_m10_19_x193(z3=119000086, z4=1500000, z5=1500000, z6=101, z7=1019010, z8=119020085, mode1=0):
    """[BEST] [Lib] [Preset] Molten Iron Demon Battle
    z3: Boss destruction flag
    z4: Start point ID
    z5: End point ID
    z6: Sound ID
    z7: Boss Battle ID
    z8: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_19_x7(z3=z3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_19_x8(z4=z4, z5=z5)
        """State 6: [BEST] [Execute] Molten Iron Daemon Battle_Start_SubState"""
        assert event_m10_19_x194(z6=z6, z7=z7, z8=z8)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_19_x10()
        """State 5: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_19_x11(z7=z7)
        """State 3: [Execution] Boss Battle_End_SubState"""
        assert event_m10_19_x12(z6=z6, z7=z7, z8=z8, mode1=mode1)
    """State 7: End state"""
    return 0

def event_m10_19_x194(z6=101, z7=1019010, z8=119020085):
    """[BEST] [Execution] Molten Iron Demon Battle_Start
    z6: Sound ID
    z7: Boss Battle ID
    z8: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z6)
    """State 1: Boss battle start notification"""
    StartBossFight(z7)
    """State 5: Host?"""
    if IsGuest() != 1:
        """State 4: Enable auto save"""
        DisableAutoSave(0)
    else:
        pass
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z8, 1)
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
    event_m10_19_x49(z125=102501, z126=576, z127=104190, z128=103690, z129=-1)

def event_m10_19_111277():
    """Multi NPC: Female Knight: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_19_x45(z140=119000081, z141=102498, z142=204, z143=7520)

def event_m10_19_111282():
    """NPC: Kanemori: Vane: Tomb"""
    """State 0,1: NPC: Kanemori: Vane: Grave Placement_SubState"""
    event_m10_19_x2(z179=104200, z180=10194100, z181=96, z182=7530)

def event_m10_19_111283():
    """NPC: Kanemori: Vain: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7530:Bell Keeper
    event_m10_19_x5(z174=119010100, z175=119020101, z176=104200, z177=10194100, z178=111282, npc1=7530)

def event_m10_19_111284():
    """NPC: Kanemori: Vane: Black Phantom Appearance: Offline"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
    event_m10_19_x47(z132=10000000, z133=570, z134=0, z135=2)

def event_m10_19_111442():
    """NPC: Curiosity Shop: Grave"""
    """State 0,1: NPC: Curiosity Shop: Grave Placement_SubState"""
    event_m10_19_x2(z179=104350, z180=10194000, z181=176, z182=7720)

def event_m10_19_111443():
    """NPC: Curio Shop: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7720:Magerold of Lanafir
    event_m10_19_x5(z174=119010110, z175=119020111, z176=104350, z177=10194000, z178=111442, npc1=7720)

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

def event_m10_19_118100():
    """Multi-use NPC: White Spirit Test: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_19_x40(z146=577)

def event_m10_19_118110():
    """Multi NPC: White Spirit Test 2: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_19_x40(z146=578)

def event_m10_19_118210():
    """Multi NPC: Dark Spirit Test 1: Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_19_x46(z136=10001000, z137=571, z138=0, z139=2)

def event_m10_19_118220():
    """Multi NPC: Dark Spirit Test 2: Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_19_x46(z136=10002000, z137=572, z138=0, z139=2)

def event_m10_19_118230():
    """Multi NPC: Dark Spirit Test 3: Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_19_x46(z136=10002010, z137=573, z138=0, z139=2)

def event_m10_19_120050():
    """Trophy: Bell Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_19_x48(z130=119020107, z131=23)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_19_120060():
    """Trophy: Old Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_19_x48(z130=119020117, z131=24)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_19_2000000():
    """[DLC] Warp to ash map"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m10_19_x79(z107=10194900, z108=50360000, z109=5100000)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_2001000():
    """[DLC] Stone monument displayed in text"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5430:"Trespassers will face\nadversity befitting a monarch"
    assert event_m10_19_x192(z9=10192500, action1=5430)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_2001010():
    """[DLC] Stone monument displayed in text_2"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5510:"In the tower of the Old Iron King\nresides a Child of Dark"
    assert event_m10_19_x192(z9=10192501, action1=5510)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_2001020():
    """[DLC] Stone monument displayed in text_3"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5420:"With water dry, and path amiss,\nwoeful temptation is dismissed"
    assert event_m10_19_x192(z9=10192502, action1=5420)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_2001030():
    """[DLC] Stone monument displayed as text_4"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5400:"Forbidden is the path\nto the ancient king's domain"
    assert event_m10_19_x192(z9=10192503, action1=5400)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_4000000():
    """[BEST] Andyur appearance _ molten iron castle"""
    """State 0,3: [Lib] [BEST] [Preset] Ander_Termination_SubState"""
    call = event_m10_19_x86(z97=10192600, z98=100740, z99=100743, z100=100762, z101=100360, z102=100300,
                            z103=100400, z104=100461)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_19_4001000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_19_x99(z95=10192600, z96=10190700)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_19_4002000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_19_x91(z105=10192600, z106=10190700)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_19_4010000():
    """[BEST] Hidden door navigation mesh change 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_19_x32(z149=10191400, z150=20, z151=6010000, z152=0, z153=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4020000():
    """[DC] Treasure box changes mimic"""
    """State 0,2: [DC] [Preset] Treasure box changes mimic_SubState"""
    # bonfire:19665:Belfry Sol Approach
    assert event_m10_19_x195(bonfire1=19665, z2=10195130)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4021000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_19_x103(z80=119020001, z81=14, z82=119000002, z83=2, z84=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m10_19_x108(z88=80000000, z89=0, z90=5, z91=941, val1=1, z92=10, z93=80000001,
                z94=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m10_19_x108(z88=80000100, z89=0, z90=5, z91=941, val1=2, z92=10, z93=80000101,
                z94=80000199))
        """State 2: Start flag ON"""
        SetEventFlag(119020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4021010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_19_x111(z85=119000002, z86=941, mode2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4022000():
    """[DC] Two pairs of fire-blowing cows rotating"""
    """State 0,2: [Preset] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m10_19_x199(z1=10191900)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_19_4022010():
    """[DC] Two pairs of rotating fire-blowing cows_attach_1"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_19_x31(z154=10191900, z155=150, z156=10191910)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4022020():
    """[DC] Two pairs of rotating fire-blowing cows_attach_2"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m10_19_x31(z154=10191900, z155=151, z156=10191911)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4031000():
    """[DC] NPC White Spirit_Gesture Management_Demon Knight"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_19_x116(z77=119000081, z78=806, z79=119020082)
    """State 1: Finish"""
    EndMachine()

def event_m10_19_4031010():
    """[DC] NPC White Spirit _ Gesture Management _ Molten Iron Daemon"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_19_x116(z77=119000086, z78=807, z79=119020089)
    """State 1: Finish"""
    EndMachine()

