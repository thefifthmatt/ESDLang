# -*- coding: utf-8 -*-
def event_m10_14_1000():
    """End_Boss HP setting"""
    """State 0,3: [Preset] Boss HP Setting_SubState"""
    assert event_m10_14_x97(z88=100000)
    """State 2: [BEST] Disabling warmth fire"""
    SetDamageImmunityByGeneratorId(803, 33200000, 1)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_2000():
    """Outpost Battle_Queen Generation Judgment"""
    """State 0,2: [Preset] Prelude Battle_Queen Generation Judgment_SubState"""
    assert event_m10_14_x161(z41=114000081, z42=114000083, z43=114020084)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_2010():
    """Preliminary battle_Time limit setting"""
    """State 0,2: Has the generation determination event ended?"""
    assert EventEnded(2000) != 0
    """State 3: [Preset] Preliminary Battle_Time Limit_SubState"""
    assert event_m10_14_x145(z52=114020084, z53=1000, z54=114000081)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_2020():
    """Preliminary Battle_Preservation and withdrawal of Queen's HP"""
    """State 0,3: Has the generation determination been completed?"""
    assert EventEnded(2000) != 0
    """State 4: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_SubState"""
    call = event_m10_14_x100(z37=95, z38=1000, z39=114000085)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 5: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_2_SubState"""
        call = event_m10_14_x100(z37=90, z38=1000, z39=114000086)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 6: [Preset] Preliminary battle with boss _HP save and withdrawal_3_SubState"""
            call = event_m10_14_x100(z37=85, z38=1000, z39=114000087)
            if call.Get() == 1:
                pass
            elif call.Done():
                """State 7: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_4_SubState"""
                call = event_m10_14_x100(z37=80, z38=1000, z39=114000088)
                if call.Get() == 1:
                    pass
                elif call.Done():
                    """State 8: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_5_SubState"""
                    call = event_m10_14_x100(z37=75, z38=1000, z39=114000089)
                    if call.Get() == 1:
                        pass
                    elif call.Done():
                        """State 9: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_6_SubState"""
                        call = event_m10_14_x100(z37=70, z38=1000, z39=114000090)
                        if call.Get() == 1:
                            pass
                        elif call.Done():
                            """State 10: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_7_SubState"""
                            call = event_m10_14_x100(z37=65, z38=1000, z39=114000091)
                            if call.Get() == 1:
                                pass
                            elif call.Done():
                                """State 11: [Preset] Preliminary battle with boss _HP save and withdrawal_8_SubState"""
                                call = event_m10_14_x100(z37=60, z38=1000, z39=114000092)
                                if call.Get() == 1:
                                    pass
                                elif call.Done():
                                    """State 12: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_9_SubState"""
                                    call = event_m10_14_x100(z37=55, z38=1000, z39=114000093)
                                    if call.Get() == 1:
                                        pass
                                    elif call.Done():
                                        """State 13: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_10_SubState"""
                                        call = event_m10_14_x100(z37=50, z38=1000, z39=114000094)
                                        if call.Get() == 1:
                                            pass
                                        elif call.Get() == 0:
                                            """State 2: Withdrawal flag ON"""
                                            SetEventFlag(114000083, 1)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_2040():
    """Outpost battle_deletion after withdrawal"""
    """State 0,2: Has the generation determination been completed?"""
    assert EventEnded(2000) != 0
    """State 3: [Preset] Delete after withdrawal_SubState"""
    assert event_m10_14_x113(z34=1000, z35=204000, z36=114020084)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_2050():
    """Outpost Battle_Boss HP Gauge Display"""
    """State 0,2: Has the generation determination been completed?"""
    assert EventEnded(2000) != 0
    """State 3: [Preset] Outpost Battle_Boss HP Gauge Display_SubState"""
    assert event_m10_14_x165(z25=114000081, z26=1014001, z27=1000, z28=114020084, z29=114000083)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_3000():
    """Pile destruction in front of rocks"""
    """State 0,2: [Preset] Rock destruction by sub pile_SubState"""
    assert event_m10_14_x89(z90=10143030, z91=10143000, z92=70, z93=300030)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_3010():
    """Rock destruction by pile destruction_back"""
    """State 0,2: [Preset] Rock destruction by sub pile_SubState"""
    assert event_m10_14_x89(z90=10143035, z91=10143005, z92=80, z93=301000)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4000():
    """Boss: Battle of the Queen"""
    """State 0,2: Is the poly drama event finished?"""
    assert EventEnded(4010) != 0
    """State 3: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_14_x8(z167=114000081, z168=400000, z169=400000, z170=101, z171=1014000, z172=114020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010():
    """Boss"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m10_14_x18(z161=10140602, z162=101410, z163=114000082, z164=401000, z165=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4020():
    """Boss: Spider Queen 1"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z10=8010, z11=114000081, z12=120, z13=114020040)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4021():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 2"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z10=8011, z11=114000081, z12=120, z13=114020041)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4022():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 3"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z10=8012, z11=114000081, z12=120, z13=114020042)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4023():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 4"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z10=8013, z11=114000081, z12=120, z13=114020043)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4024():
    """Boss: Spider Queen"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z10=8014, z11=114000081, z12=120, z13=114020044)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4025():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 6"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z10=8015, z11=114000081, z12=120, z13=114020045)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_5000():
    """Treasure chest appears when you pull the switch"""
    """State 0,2: [Preset] Treasure chest appears when switch is pulled_SubState"""
    assert event_m10_14_x164(z30=10143101, z31=10145120, z32=500000, z33=10143100)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_6000():
    """Sand door"""
    """State 0,3: [Preset] Sand Door_SubState"""
    # action:1102:"Too heavy to open"
    call = event_m10_14_x105(z76=10140400, z77=10141020, z78=50, z79=20, z80=20, z81=600000, action1=1102)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_14_7000():
    """Boss: Zakobos_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_14_x8(z167=114000096, z168=700000, z169=700000, z170=102, z171=1014010, z172=114020095,
            mode2=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_14_8000():
    """Bug door"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_14_x5(z178=1005, z179=1105, z180=50830000, z181=114000010)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_8002():
    """Insect key door_3"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_14_x5(z178=1005, z179=1105, z180=50830000, z181=114000014)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_9000():
    """Warp to the memory of the ancient dragon"""
    """State 0,3: [Preset] Inter-map warp_SubState by checking OBJ"""
    call = event_m10_14_x106(z64=10141700, z65=101420, z66=0, z67=20260000, z68=900000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_9010():
    """Red soul and Complicated display"""
    """State 0,3: [Preset] Red Soul and Complicated Display _SubState"""
    call = event_m10_14_x124(z6=10141705, z7=2004, z8=100460, z9=100951)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_10000():
    """The key door that opens with "Patch House Key" """
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_14_x5(z178=1005, z179=1105, z180=50930000, z181=114000060)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_11010():
    """Insect lock door_Spider start_Front"""
    """State 0,2: [Preset] Insect Lock Door_Spider Launch_SubState"""
    assert event_m10_14_x117(z73=10140412, z74=1101000, z75=114020072)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_12000():
    """One door open from the beginning"""
    """State 0,2: Make one door open"""
    ChangeObjState(10140471, 74)
    assert CompareObjStateId(10140471, 30, 0)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_13000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_14_x19(z156=10142500, z157=20, z158=1300000, z159=0, z160=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_14000():
    """Door that opens with a wall lever_Left"""
    """State 0,2: [Preset] Door opened with wall lever_SubState"""
    assert event_m10_14_x129(z59=10141401, z60=10141400, z61=1400000, z62=20, z63=10)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_14010():
    """Door that opens with a wall lever_Right"""
    """State 0,2: [Preset] Door opened with wall lever_SubState"""
    assert event_m10_14_x129(z59=10141406, z60=10141405, z61=1401000, z62=20, z63=10)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_15000():
    """Treasure corpse 1"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141500, z56=10146230)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_15010():
    """Treasure corpse 2"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141501, z56=10146300)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_15020():
    """Treasure corpse 3"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141502, z56=10146310)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_15030():
    """Treasure corpse 4"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141503, z56=10146320)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_15040():
    """Treasure corpse 5"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141504, z56=10146010)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_15050():
    """Treasure corpse 6"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141505, z56=10146330)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_16000():
    """Treasure corpse falls due to tower destruction"""
    """State 0,2: [Preset] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_14_x149(z49=10141550, z50=10146290, z51=70)
    """State 1: Finish"""

def event_m10_14_17000():
    """Navimesh change due to yagura destruction 1"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x150(z46=10141550, z47=1700000, z48=1700001)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_17010():
    """Navimesh change due to yagura destruction 2"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x150(z46=10141555, z47=1701000, z48=1701001)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_17020():
    """Navimesh change due to yagura destruction 3"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x150(z46=10141545, z47=1702000, z48=1702001)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_20020():
    """One-way door 03 (dust chute room)"""
    """State 0,2: [Lib] Area specified door unlocking_2_SubState"""
    assert event_m10_14_x6(z175=0, z176=2002000, z177=114000020)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_21000():
    """Alarm treasure chest"""
    """State 0,2: [Preset] Alarm treasure chest _ Start _ SubState"""
    assert event_m10_14_x137(z57=10145060, z58=114000070)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_22000():
    """Termination Bonfire_Pyroxene"""
    """State 0,2: [Lib] [Preset] End special bonfire_SubState"""
    assert event_m10_14_x36(z132=10141800, z133=100461)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_14_23000():
    """Pig eats mushrooms_pig 1"""
    """State 0,3: [Preset] Pig eats mushrooms_SubState"""
    call = event_m10_14_x179(z14=114000052, z15=10141590, z16=10146500, z17=2300000, z18=10, z19=1120)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_23010():
    """Pig eats mushrooms_pig 2"""
    """State 0,3: [Preset] Pig eats mushrooms_SubState"""
    call = event_m10_14_x179(z14=114000052, z15=10141590, z16=10146500, z17=2300000, z18=10, z19=1121)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_23020():
    """Pig eats mushrooms"""
    """State 0,3: [Preset] Pig eats mushrooms_SubState"""
    call = event_m10_14_x179(z14=114000052, z15=10141590, z16=10146500, z17=2300000, z18=10, z19=1122)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_24000():
    """Probability of piglets"""
    """State 0,2: [Preset] Appearance of piglets with probability _SubState"""
    assert event_m10_14_x154(z44=114020050)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_25000():
    """Interlocking destruction due to scaffold destruction"""
    """State 0,2: [Preset] Linkage destruction due to scaffold destruction_SubState"""
    assert event_m10_14_x172(z21=10141180, z22=2500000, z23=2500001, z24=10141170)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_25010():
    """Navi mesh change of scaffolding that breaks when riding"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_14_x19(z156=10141170, z157=20, z158=2501000, z159=2, z160=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_80000():
    """Rebirth fire 01_A building next to ant hell"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_14_x27(z153=1014000, z154=1014099)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_80010():
    """Shop lineup expansion"""
    """State 0,2: [Lib] [Preset] Shop Lineup_SubState"""
    # bonfire:14650:Lower Brightstone Cove
    assert event_m10_14_x41(bonfire1=14650, z128=114000081, z129=101100)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_81000():
    """Rebirth Fire 02_Map entrance tent"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_14_x27(z153=1014100, z154=1014199)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_82000():
    """Rebirth Fire 03_Cave after Church"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_14_x27(z153=1014200, z154=1014299)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_90000():
    """Trophy_Pyroxene Light"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_14_x37(z130=100461, z131=9)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_x0(z65=_, z66=0, z67=_, z68=_):
    """[Lib] Warp between maps after poly play
    z65: Pre-warp poly play ID
    z66: Poly Play ID after Warp
    z67: Map ID
    z68: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z65, z66, z67, z68, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_14_x1(z187=_, z188=_, z189=_, z190=_):
    """[Lib] NPC: Grave Placement: General purpose
    z187: Death map: Global event flag
    z188: Tomb: OBJ instance ID
    z189: Tomb move to: Generator ID
    z190: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z187, 1)
    IsGraveGeneratable(8, z190, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z188, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z188, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_14_x2(z184=_, z185=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z184: Global: death flag
    z185: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z185, 10, 0)
    CompareObjState(1, z185, 20, 0)
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
    IsObjSearched(0, z185)
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

def event_m10_14_x3(z182=_, z183=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z182: Area other flags: Ghost appearance
    z183: Area other flags: Conversation start
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
    SetEventFlag(z182, 1)
    CompareEventFlag(0, z182, 1)
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
    SetEventFlag(z183, 1)
    CompareEventFlag(0, z183, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_14_x4(z182=_, z183=_, z184=_, z185=_, z186=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z182: Ghost Appearance: Area Other Flag
    z183: Conversation start: Area and other flags
    z184: Death: Global event flag
    z185: Tomb: OBJ instance ID
    z186: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z186, 1, 0)
    CompareEventFlag(9, z182, 1)
    CompareObjState(9, z185, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z183, 1)
        CompareEventFlag(0, z183, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_14_x2(z184=z184, z185=z185, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_14_x3(z182=z182, z183=z183, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_14_x5(z178=1005, z179=1105, z180=_, z181=_):
    """[Lib] Item specified door unlocking_2
    z178: Text ID when opened
    z179: Text ID when not opened
    z180: item
    z181: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z180, z178, z179, z181, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x6(z175=0, z176=2002000, z177=114000020):
    """[Lib] Area specified door unlocking_2
    z175: Text ID when opened
    z176: Point ID
    z177: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z176, 0, z175, 1101, z177, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x7(z173=_, z174=_):
    """[Lib] NPC: Death determination: General purpose
    z173: Generator ID
    z174: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z174, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z173)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z174, 1)
            CompareEventFlag(0, z174, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_14_x8(z167=_, z168=_, z169=_, z170=_, z171=_, z172=_, mode2=0):
    """[Lib] [Preset] Boss Battle Start
    z167: Boss destruction flag
    z168: Start point ID
    z169: End point ID
    z170: Sound ID
    z171: Boss Battle ID
    z172: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_14_x9(z167=z167)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_14_x10(z168=z168, z169=z169)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_14_x11(z170=z170, z171=z171, z172=z172)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_14_x12()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_14_x13(z171=z171)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_14_x14(z170=z170, z171=z171, z172=z172, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_14_x9(z167=_):
    """[Reproduction] Boss Battle_Start
    z167: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z167) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_14_x10(z168=_, z169=_):
    """[Condition] Boss Battle_Start
    z168: Start point ID
    z169: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z168, z169, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z168, z169, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x11(z170=_, z171=_, z172=_):
    """[Execution] Boss Battle_Start
    z170: Sound ID
    z171: Boss Battle ID
    z172: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z170)
    """State 1: Boss battle start notification"""
    StartBossFight(z171)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z172, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x12():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x13(z171=_):
    """[Condition] Boss Battle_End Judgment
    z171: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z171, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x14(z170=_, z171=_, z172=_, mode2=0):
    """[Execute] Boss Battle_End
    z170: Sound ID
    z171: Boss Battle ID
    z172: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z172, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z171)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z170)
    """State 5: End state"""
    return 0

def event_m10_14_x15(z163=114000082):
    """[Reproduction] Boss Battle_Poly Play Replay
    z163: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z163) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_14_x16(z161=10140602):
    """[Condition] Boss Battle_Poly Play Replay
    z161: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z161, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x17(z162=101410, z163=114000082, z164=401000, z166=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z162: Poly play ID
    z163: Poly drama played flag
    z164: Warp point ID
    z166: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z162, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z163, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z164)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_14_x18(z161=10140602, z162=101410, z163=114000082, z164=401000, z165=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z161: White door instance ID
    z162: Poly play ID
    z163: Poly drama played flag
    z164: Warp point ID
    z165: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m10_14_x15(z163=z163)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m10_14_x16(z161=z161)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m10_14_x17(z162=z162, z163=z163, z164=z164, z166=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_14_x19(z156=_, z157=20, z158=_, z159=_, z160=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z156: Object instance ID
    z157: OBJ state ID
    z158: Navimesh switching point ID
    z159: Additional attributes
    z160: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_14_x20(z156=z156, z157=z157, z158=z158, z160=z160, z159=z159)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_14_x21(z156=z156, z157=z157, z158=z158)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_14_x22(z156=z156, z157=z157, z158=z158, z159=z159, z160=z160)
    """State 4: End state"""
    return 0

def event_m10_14_x20(z156=_, z157=20, z158=_, z160=_, z159=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z156: Target OBJ instance ID
    z157: Target OBJ state ID
    z158: Navimesh switching point ID
    z160: Additional attributes
    z159: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z156, z157, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z158, z160)
        DeleteNavimeshAttribute(z158, z159)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_14_x21(z156=_, z157=20, z158=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z156: Target OBJ instance ID
    z157: Target OBJ state ID
    z158: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z156, z157, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x22(z156=_, z157=20, z158=_, z159=_, z160=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z156: Target OBJ instance ID
    z157: Target OBJ state ID
    z158: Navimesh switching point ID
    z159: Additional attributes
    z160: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z158, z159)
    DeleteNavimeshAttribute(z158, z160)
    """State 2: End state"""
    return 0

def event_m10_14_x23(z155=_):
    """[DC] [execution] Lighthouse lighting management
    z155: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z155)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_14_x24():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x25(z153=_, z154=_):
    """[Lib] [execute] Rebirth fire
    z153: Flag start ID
    z154: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z153, z154, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x26():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x27(z153=_, z154=_):
    """[Lib] [Preset] Rebirth
    z153: Flag start ID
    z154: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_14_x24()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_14_x26()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_14_x25(z153=z153, z154=z154)
    """State 4: End state"""
    return 0

def event_m10_14_x28(z149=114000096, z150=102436, z151=205, z152=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z149: Defeat Boss 1: Area and other flags
    z150: Summon Achievement: Global Event Flag
    z151: Summon achievement count: global variable
    z152: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z150, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z149, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z151, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z151, NpcInfoValue(z152, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z150, 1)
                CompareEventFlag(0, z150, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m10_14_x29(z143=102810, z144=10001000, z145=521, z146=104340, z147=0, z148=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z143: Summoning conditions: Global event flag
    z144: Summon range
    z145: Generator ID
    z146: Death: Global event flag
    z147: Appearance: Minimum time
    z148: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z146, 1)
        CompareEventFlag(8, z143, 1)
        IsPlayerInsidePoint(8, z144, z144, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z146, 1)
            CompareStateTime(1, z147, 3, z148)
            IsPlayerInsidePoint(2, z144, z144, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z145)
                HasNpcPhantomSpawned(0, z145, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_14_x30(z139=10002000, z140=520, z141=0, z142=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z139: Summon range
    z140: Generator ID
    z141: Appearance: Minimum time
    z142: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z139, z139, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z141, 3, z142)
        IsPlayerInsidePoint(1, z139, z139, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z140)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_14_x31(z134=102430, z135=526, z136=104160, z137=103660, z138=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z134: White Phantom can appear: Global event flag
    z135: White Phantom: Generator ID
    z136: Death: Global event flag
    z137: Hostile: Global event flag
    z138: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z135)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z136, 1)
        CompareEventFlag(1, z137, 1)
        CompareEventFlag(2, z134, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z135)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z136, 1)
            CompareEventFlag(1, z137, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z135)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z136, 1)
            CompareEventFlag(1, z137, 1)
            HasNpcPhantomSpawned(2, z135, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z135, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z135)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m10_14_x32(z133=100461):
    """[Lib] [Reproduction] Special bonfire at the end
    z133: Lighting completion flag
    """
    """State 0,1: Is the bonfire already lit?"""
    if GetEventFlag(z133) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_14_x33(z132=10141800):
    """[Lib] [Condition] Terminal special fire
    z132: Bonfire OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z132)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x34(z132=10141800, z133=100461):
    """[Lib] [Execution] End special bonfire_ignition
    z132: Bonfire OBJ instance ID
    z133: Lighting completion flag
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
        ChangeObjState(z132, 70)
        """State 3: Lighting completion flag ON"""
        SetEventFlag(z133, 1)
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

def event_m10_14_x35(z132=10141800, z133=100461):
    """[Lib] [Execution] End special bonfire_warp
    z132: Bonfire OBJ instance ID
    z133: Lighting completion flag
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
        assert event_m10_14_x0(z65=0, z66=0, z67=10040000, z68=200000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m10_14_x36(z132=10141800, z133=100461):
    """[Lib] [Preset] Special bonfire at the end
    z132: Bonfire OBJ instance ID
    z133: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] End special bonfire _SubState"""
    call = event_m10_14_x32(z133=z133)
    if call.Get() == 1:
        """State 5: [Lib] [Condition] End special bonfire_2_SubState"""
        assert event_m10_14_x33(z132=z132)
        """State 2: [Lib] [Execution] End special bonfire_warp_SubState"""
        assert event_m10_14_x35(z132=z132, z133=z133)
    elif call.Get() == 0:
        """State 4: [Lib] [Condition] End special bonfire_SubState"""
        assert event_m10_14_x33(z132=z132)
        """State 3: [Lib] [Execution] End special bonfire_At ignition_SubState"""
        assert event_m10_14_x34(z132=z132, z133=z133)
    """State 6: Rerun"""
    return 0

def event_m10_14_x37(z130=100461, z131=9):
    """[Lib] [Preset] Trophy Acquisition_Global
    z130: Acquisition trigger_global flag
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

def event_m10_14_x38(z127=_):
    """[Lib] [Reproduction] Shop Lineup
    z127: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(z127) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m10_14_x39(bonfire1=14650, z128=114000081):
    """[Lib] [Conditions] Shop lineup
    bonfire1: Bonfire ID
    z128: Boss destruction flag
    """
    """State 0,1: Is the total number of laps 2 or more and is the boss destroyed?"""
    # bonfire:14650:Lower Brightstone Cove
    CompareGameCycleForBonfire(8, bonfire1, 2, 2, 3)
    CompareEventFlag(8, z128, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_14_x40(z127=_):
    """[Lib] [execution] shop lineup
    z127: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(z127, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x41(bonfire1=14650, z128=114000081, z129=101100):
    """[Lib] [Preset] Shop Lineup
    bonfire1: Bonfire ID
    z128: Boss destruction flag
    z129: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_14_x38(z127=z129)
    if call.Get() == 0:
        """State 3: [Lib] [Conditions] Shop lineup_SubState"""
        assert event_m10_14_x39(bonfire1=bonfire1, z128=z128)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_14_x40(z127=z129)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_14_x42(z126=101063):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z126: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z126, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x43(z126=101063, z127=101213):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z126: Boss destruction flag
    z127: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_14_x38(z127=z127)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m10_14_x42(z126=z126)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_14_x40(z127=z127)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_14_x44(z116=10141810):
    """[Lib] [BEST] [Condition] Andyel_Appearance_Termination
    z116: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z116)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x45(z116=10141810, z119=100760, z118=100741):
    """[Lib] [BEST] [Execution] Andyel_Appearance_Termination
    z116: Ander OBJ instance ID
    z119: Conversation start flag
    z118: Encounter flag
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
        SetEventFlag(z118, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z116, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z116, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(z119, 1)
        """State 7: End state"""
        return 0

def event_m10_14_x46(z117=100740):
    """[Lib] [BEST] [Conditions] Ander_Destruction_End_Termination
    z117: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, z117, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x47(z116=10141810):
    """[Lib] [BEST] [Execution] Andel_Deletion_End
    z116: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z116, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z116, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_14_x48(z116=10141810, z117=100740, z119=100760, z118=100741):
    """[Lib] [BEST] [Reproduction] Anderl_Appearance determination_Termination
    z116: Ander OBJ instance ID
    z117: Event completion flag
    z119: Conversation start flag
    z118: Encounter flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been completed?"""
        if GetEventFlag(z117) != 0:
            pass
        else:
            """State 3: Was it in conversation?"""
            if GetEventFlag(z119) != 0:
                pass
            else:
                """State 4: Was it in the middle of appearance?"""
                if CompareObjStateId(z116, 72, 0):
                    pass
                elif CompareObjStateId(z116, 73, 0):
                    pass
                elif CompareObjStateId(z116, 70, 0):
                    pass
                elif CompareObjStateId(z116, 30, 0):
                    pass
                else:
                    """State 7: Was the appearance confirmed?"""
                    if GetEventFlag(z118) != 0:
                        """State 8: Standby state: 30"""
                        ChangeObjState(z116, 30)
                    else:
                        """State 11: Appearance determination"""
                        return 2
                """State 5: Wait for completion"""
                assert CompareObjStateId(z116, 30, 0)
                """State 6: Conversation start flag ON"""
                SetEventFlag(z119, 1)
            """State 10: Disappearance judgment"""
            return 1
    """State 9: Finish"""
    return 0

def event_m10_14_x49():
    """[Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x50(z116=10141810, z117=100740, z118=100741, z119=100760, z120=100461, z121=100300,
                     z122=100360, z123=100400):
    """[Lib] [BEST] [Preset] Andyel_Termination
    z116: Ander OBJ instance ID
    z117: Event completion flag
    z118: Encounter flag
    z119: Conversation start flag
    z120: Lighting completion flag
    z121: Bonfire lighting judgment flag ①
    z122: Bonfire lighting judgment flag ②
    z123: Bonfire lighting judgment flag ③
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Ander _ Appearance determination _ Termination _ SubState"""
    call = event_m10_14_x48(z116=z116, z117=z117, z119=z119, z118=z118)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty _ SubState"""
        Label('L0')
        assert event_m10_14_x49()
        """State 9: [Lib] [BEST] [Conditions] Ander_Deletion_Termination_Termination_SubState"""
        assert event_m10_14_x46(z117=z117)
        """State 6: [Lib] [BEST] [Execution] Andel_Destruction_End_SubState"""
        assert event_m10_14_x47(z116=z116)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Ander_Appearance determination_Termination_SubState"""
        call = event_m10_14_x57(z116=z116, z120=z120, z121=z121, z122=z122, z123=z123, z118=z118)
        if call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Andel_Appearance determination_Termination_SubState"""
            assert event_m10_14_x58(z116=z116)
            """State 1: [Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty_SubState"""
            assert event_m10_14_x56()
            """State 7: [Lib] [BEST] [Condition] Ander_Appearance_Termination_SubState"""
            assert event_m10_14_x44(z116=z116)
            """State 4: [Lib] [BEST] [Execution] Andel_Appearance_Termination_SubState"""
            call = event_m10_14_x45(z116=z116, z119=z119, z118=z118)
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

def event_m10_14_x51(z124=10141810, z125=10141800):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z124: Ander OBJ instance ID
    z125: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z124, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z125, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_14_x52(z124=10141810):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z124: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z124, 10, 0)
    CompareObjState(0, z124, 31, 0)
    CompareObjState(0, z124, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_14_x53(z124=10141810, z125=10141800):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z124: Ander OBJ instance ID
    z125: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z125, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z124, 10, 1)
    CompareObjState(8, z124, 31, 1)
    CompareObjState(8, z124, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_14_x54(z124=10141810, z125=10141800):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z124: Ander OBJ instance ID
    z125: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z125, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z124, 10, 0)
    CompareObjState(0, z124, 31, 0)
    CompareObjState(0, z124, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_14_x55(z124=10141810, z125=10141800):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z124: Ander OBJ instance ID
    z125: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_14_x51(z124=z124, z125=z125)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_14_x52(z124=z124)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_14_x53(z124=z124, z125=z125)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_14_x54(z124=z124, z125=z125)
    """State 6: Rerun"""
    return 1

def event_m10_14_x56():
    """[Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x57(z116=10141810, z120=100461, z121=100300, z122=100360, z123=100400, z118=100741):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_Termination
    z116: Ander OBJ instance ID
    z120: Lighting completion flag
    z121: Bonfire lighting judgment flag ①
    z122: Bonfire lighting judgment flag ②
    z123: Bonfire lighting judgment flag ③
    z118: Andyur encounter flag
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z120, 0)
    CompareEventFlag(8, z121, 1)
    CompareEventFlag(8, z122, 1)
    CompareEventFlag(8, z123, 1)
    CompareEventFlag(8, z118, 0)
    CompareEventFlag(0, z118, 1)
    if ConditionGroup(8):
        """State 2: End state"""
        return 0
    elif ConditionGroup(0):
        """State 3: Rerun"""
        return 1

def event_m10_14_x58(z116=10141810):
    """[Lib] [BEST] [Execution] Andel_Appearance determination_Termination
    z116: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z116, 31)
    """State 2: End state"""
    return 0

def event_m10_14_x59(z114=10141810, z115=10141800):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z114: Ander OBJ instance ID
    z115: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z114, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z115, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_14_x60(z114=10141810):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z114: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z114, 10, 0)
    CompareObjState(0, z114, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_14_x61(z114=10141810, z115=10141800):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z114: Ander OBJ instance ID
    z115: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z115, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z114, 10, 1)
    CompareObjState(8, z114, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_14_x62(z114=10141810, z115=10141800):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z114: Ander OBJ instance ID
    z115: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z115, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z114, 10, 0)
    CompareObjState(0, z114, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_14_x63(z114=10141810, z115=10141800):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z114: Ander OBJ instance ID
    z115: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_14_x59(z114=z114, z115=z115)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_14_x60(z114=z114)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_14_x61(z114=z114, z115=z115)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_14_x62(z114=z114, z115=z115)
    """State 5: Rerun"""
    return 0

def event_m10_14_x64(z112=10141810):
    """[Lib] [BEST] [Conditions] Switching the Andy navig mesh
    z112: Ander OBJ instance ID
    """
    """State 0,1: Judgment of under deal status"""
    CompareObjState(0, z112, 10, 0)
    CompareObjState(0, z112, 31, 0)
    CompareObjState(0, z112, 20, 0)
    if ConditionGroup(0):
        """State 2: I'm stuck"""
        return 0
    else:
        """State 3: Appearing"""
        return 1

def event_m10_14_x65(z112=10141810, z113=6003000):
    """[Lib] [BEST] [Execution] Anderu's navigation mesh switching_passable
    z112: Ander OBJ instance ID
    z113: Navigation change point ID
    """
    """State 0,2: Navimesh switching: Allowed to pass"""
    DeleteNavimeshAttribute(z113, 2)
    """State 1: Next judgment"""
    CompareObjState(8, z112, 10, 1)
    CompareObjState(8, z112, 31, 1)
    CompareObjState(8, z112, 20, 1)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_14_x66(z112=10141810, z113=6003000):
    """[Lib] [BEST] [Execution] Anderu navigesh mesh switching_No traffic
    z112: Ander OBJ instance ID
    z113: Navigation change point ID
    """
    """State 0,2: Navi mesh switching: no traffic"""
    AddNavimeshAttribute(z113, 2)
    """State 1: Next judgment"""
    CompareObjState(0, z112, 10, 0)
    CompareObjState(0, z112, 31, 0)
    CompareObjState(0, z112, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_14_x67(z112=10141810, z113=6003000):
    """[Lib] [BEST] [Reproduction] Switching the Andy navig mesh
    z112: Ander OBJ instance ID
    z113: Navigation change point ID
    """
    """State 0,1: Is the Andyal finished?"""
    if CompareObjStateId(z112, 20, 0):
        """State 2: Navimesh switching: Allowed to pass"""
        DeleteNavimeshAttribute(z113, 2)
        """State 4: Finished"""
        return 1
    else:
        """State 3: Waiting"""
        return 0

def event_m10_14_x68(z112=10141810, z113=6003000):
    """[Lib] [BEST] [Preset] Anderu navigator mesh switching_
    z112: Ander OBJ instance ID
    z113: Navigation change point ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Anderu's navigation mesh switching _SubState"""
    call = event_m10_14_x67(z112=z112, z113=z113)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Conditions] Switching the Andy's Navimesh_SubState"""
    Label('L0')
    call = event_m10_14_x64(z112=z112)
    if call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Switching the Andy's Navigation Mesh_Passable_SubState"""
        assert event_m10_14_x65(z112=z112, z113=z113)
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Navigation mesh switching of the deal _ Traffic prohibited _SubState"""
        assert event_m10_14_x66(z112=z112, z113=z113)
    """State 5: Rerun"""
    return 0

def event_m10_14_x69(z97=114020001, z99=114000002):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z97: Lottery determination flag
    z99: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z99) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z97) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_14_x70(z98=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z98: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z98, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_14_x71(z97=114020001, z100=4, z101=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z97: Lottery determination flag
    z100: Number of appearance judgment points
    z101: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z97, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z100)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z101, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_14_x72(z97=114020001, z98=14, z99=114000002, z100=4, z101=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z97: Lottery determination flag
    z98: Random number comparison value
    z99: Defeat flag
    z100: Number of appearance judgment points
    z101: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_14_x69(z97=z97, z99=z99)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_14_x70(z98=z98)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_14_x71(z97=z97, z100=z100, z101=z101)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_14_x81(z97=z97, z101=z101)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_14_x73(val1=_, z109=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z109: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z109) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_14_x74(z105=_, z106=0, z107=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z105: Appearance judgment point ID
    z106: Minimum appearance time
    z107: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z105, z105, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z106, 3, z107)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_14_x75(z108=926, z110=_, z111=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z108: Generator ID
    z110: Appearance start point ID
    z111: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z108, z110, z111)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z108)
    """State 4: Finish"""
    return 0

def event_m10_14_x76(z102=114000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z102: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z102) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_14_x77(z105=_, z106=0, z107=5, z108=926, val1=_, z109=10, z110=_, z111=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z105: Intrusion detection point ID
    z106: Minimum appearance time
    z107: Maximum time to appear
    z108: Generator ID
    val1: Appearance judgment number
    z109: Lottery result point variable
    z110: Appearance start point ID
    z111: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_14_x73(val1=val1, z109=z109)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_14_x74(z105=z105, z106=z106, z107=z107)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_14_x75(z108=z108, z110=z110, z111=z111)
    """State 4: Finish"""
    return 0

def event_m10_14_x78(z103=926, mode1=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z103: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z103)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_14_x79(z102=114000002, z104=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z102: Defeat flag
    z104: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z102, 1)
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
                    SetEventFlag(z104, 1)
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

def event_m10_14_x80(z102=114000002, z103=926, mode1=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z102: Defeat flag
    z103: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_14_x76(z102=z102)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_14_x78(z103=z103, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_14_x79(z102=z102, z104=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_14_x79(z102=z102, z104=102755)
    """State 5: End state"""
    return 0

def event_m10_14_x81(z97=114020001, z101=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z97: Lottery determination flag
    z101: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z97, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z101, 0)
    """State 3: End state"""
    return 0

def event_m10_14_x82(z94=114000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z94: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z94) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_14_x83(z95=803):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z95: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z95, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x84(z96=114020079):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z96: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z96, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x85(z94=114000081, z95=803, z96=114020079):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z94: Boss destruction flag
    z95: Boss generator ID
    z96: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_14_x82(z94=z94)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_14_x83(z95=z95)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_14_x84(z96=z96)
    """State 4: End state"""
    return 0

def event_m10_14_x86(z91=_, z93=_):
    """[Reproduction] Reproduction of rocky rocky state
    z91: Rock instance ID
    z93: Point ID for Navimesh change
    """
    """State 0,1: State determination of rock OBJ"""
    if CompareObjStateId(z91, 10, 1):
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z93, 2)
        """State 5: Executed"""
        return 1
    else:
        """State 3: Navimesh attribute added"""
        AddNavimeshAttribute(z93, 2)
        """State 4: Not executed"""
        return 0

def event_m10_14_x87(z90=_):
    """[Conditions] Pile failure judgment
    z90: Pile instance ID
    """
    """State 0,1: Group condition: Pile breaking standby"""
    CompareObjState(0, z90, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x88(z91=_, z92=_, z93=_):
    """[Execution] Iwa Gorogoro
    z91: Rock instance ID
    z92: Rolling state ID
    z93: Point ID for Navimesh change
    """
    """State 0,2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z93, 2)
    """State 1: OBJ State Transition: Rock Gorogoro"""
    ChangeObjState(z91, z92)
    assert CompareObjStateId(z91, 20, 0)
    """State 3: End state"""
    return 0

def event_m10_14_x89(z90=_, z91=_, z92=_, z93=_):
    """[Preset] Pile destruction and rocks
    z90: Pile instance ID
    z91: Rock instance ID
    z92: Rolling state ID
    z93: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Rock rocking state reproduction_SubState"""
    call = event_m10_14_x86(z91=z91, z93=z93)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Pile failure judgment_SubState"""
        assert event_m10_14_x87(z90=z90)
        """State 3: [Execution] Iwa Gorogoro_SubState"""
        assert event_m10_14_x88(z91=z91, z92=z92, z93=z93)
    """State 4: End state"""
    return 0

def event_m10_14_x90(z30=10143101, z31=10145120, z32=500000, z33=10143100):
    """[Reproduction] Treasure chest appears when you pull the switch
    z30: Scaffolding OBJ instance ID
    z31: Treasure chest OBJ instance ID
    z32: Point ID for Navimesh change
    z33: Switch OBJ instance ID
    """
    """State 0,1: Attach a treasure chest to the scaffold"""
    AttachObjToObj(z30, 150, z31)
    """State 2,3: Scaffold OBJ status determination"""
    if CompareObjStateId(z30, 20, 0):
        """State 5: Disable key guide for switch"""
        DisableObjKeyGuide(z33, 1)
        """State 4,7: Already in operation"""
        return 1
    else:
        """State 6: Not in operation"""
        return 0

def event_m10_14_x91(z33=10143100):
    """[Condition] Treasure chest appears when switch is pulled
    z33: Switch OBJ instance ID
    """
    """State 0,1: Switch operation standby"""
    CompareObjState(0, z33, 74, 0)
    CompareObjState(0, z33, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x92(z30=10143101, z32=500000, z33=10143100):
    """[Execution] Treasure chest appears when switch is pulled
    z30: Scaffolding OBJ instance ID
    z32: Point ID for Navimesh change
    z33: Switch OBJ instance ID
    """
    """State 0,4: Disable key guide for switch"""
    DisableObjKeyGuide(z33, 1)
    """State 1: Scaffold animation playback descending with a switch"""
    ChangeObjState(z30, 70)
    """State 3: Has the animation of the scaffold finished playing?"""
    CompareObjState(0, z30, 20, 0)
    assert ConditionGroup(0)
    """State 2,5: End state"""
    return 0

def event_m10_14_x93():
    """[Execution] Preliminary Battle with Boss"""
    """State 0,1: Withdrawal flag ON"""
    SetEventFlag(114000083, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x94():
    """[Reproduction] HP setting of boss"""
    """State 0,1: Destroyed the boss?"""
    if GetEventFlag(114000081) != 0:
        """State 3: Simple end"""
        return 1
    else:
        """State 2: End state"""
        return 0

def event_m10_14_x95(z88=100000):
    """[Condition] HP setting of boss_Termination
    z88: Point ID
    """
    """State 0,1: Did you enter the point before the boss?"""
    IsPlayerInsidePoint(8, z88, z88, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: Flag judgment"""
    CompareEventFlag(0, 114000085, 1)
    CompareEventFlag(1, 114000086, 1)
    CompareEventFlag(2, 114000087, 1)
    CompareEventFlag(3, 114000088, 1)
    CompareEventFlag(4, 114000089, 1)
    CompareEventFlag(5, 114000090, 1)
    CompareEventFlag(6, 114000091, 1)
    CompareEventFlag(7, 114000092, 1)
    CompareEventFlag(8, 114000093, 1)
    CompareEventFlag(9, 114000094, 1)
    if ConditionGroup(9):
        """State 12: HP setting 10"""
        return 9
    elif ConditionGroup(8):
        """State 11: HP setting 9"""
        return 8
    elif ConditionGroup(7):
        """State 10: HP setting 8"""
        return 7
    elif ConditionGroup(6):
        """State 9: HP setting 7"""
        return 6
    elif ConditionGroup(5):
        """State 8: HP setting 6"""
        return 5
    elif ConditionGroup(4):
        """State 7: HP setting 5"""
        return 4
    elif ConditionGroup(3):
        """State 6: HP setting 4"""
        return 3
    elif ConditionGroup(2):
        """State 5: HP setting 3"""
        return 2
    elif ConditionGroup(1):
        """State 4: HP setting 2"""
        return 1
    elif ConditionGroup(0):
        """State 3: HP setting 1"""
        return 0
    else:
        """State 13: No corresponding HP setting flag"""
        return 10

def event_m10_14_x96(z89=_):
    """[Execution] HP setting of boss
    z89: HP ratio to be set
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Boss HP settings"""
        SetHpRatioFromGenerator(803, z89)
    else:
        pass
    """State 3: End state"""
    return 0

def event_m10_14_x97(z88=100000):
    """[Preset] Boss HP Setting_Termination
    z88: HP set point ID
    """
    """State 0,1: [Reproduction] HP setting of boss_SubState"""
    call = event_m10_14_x94()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] HP setting of boss_SubState"""
        call = event_m10_14_x95(z88=z88)
        if call.Get() == 0:
            """State 3: [Execution] HP setting of boss_SubState"""
            assert event_m10_14_x96(z89=95)
        elif call.Get() == 1:
            """State 4: [Execution] HP setting of boss_2_SubState"""
            assert event_m10_14_x96(z89=90)
        elif call.Get() == 2:
            """State 5: [Execute] HP setting of boss_3_SubState"""
            assert event_m10_14_x96(z89=85)
        elif call.Get() == 3:
            """State 6: [Execute] HP setting of boss_4_SubState"""
            assert event_m10_14_x96(z89=80)
        elif call.Get() == 4:
            """State 7: [Execute] HP setting of boss_5_SubState"""
            assert event_m10_14_x96(z89=75)
        elif call.Get() == 5:
            """State 8: [Execution] HP setting of boss_6_SubState"""
            assert event_m10_14_x96(z89=70)
        elif call.Get() == 6:
            """State 9: [Execute] HP setting of boss_7_SubState"""
            assert event_m10_14_x96(z89=65)
        elif call.Get() == 7:
            """State 10: [Execution] HP setting of boss_8_SubState"""
            assert event_m10_14_x96(z89=60)
        elif call.Get() == 8:
            """State 11: [Execution] HP setting of boss_9_SubState"""
            assert event_m10_14_x96(z89=55)
        elif call.Get() == 9:
            """State 12: [Execute] HP setting of boss_10_SubState"""
            assert event_m10_14_x96(z89=50)
        elif call.Get() == 10:
            pass
    """State 13: End state"""
    return 0

def event_m10_14_x98(z37=_, z38=1000, z85=202000, z86=202001, z87=30):
    """[Condition] Preliminary Battle with Boss
    z37: HP reduction rate (%)
    z38: Enemy generator ID
    z85: Start point ID
    z86: End point ID
    z87: Time limit
    """
    """State 0,2: Generating the start battle boss and canceling the activation state"""
    CompareChrStartUpState(8, z38, 2, 1)
    CompareEventFlag(8, 114020084, 1)
    CompareEventFlag(0, 114000081, 1)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(8):
        Goto('L0')
    """State 5: Destroyed"""
    return 2
    """State 1: HP is below a certain level or passes through the gate or a certain time elapses"""
    Label('L0')
    CompareChrHpRatio(1, z38, z37, 5)
    IsPlayerInsidePoint(8, z85, z86, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    CompareAreaTimer(0, 0, z87, 3)
    if ConditionGroup(0):
        """State 4: Boss withdrawal"""
        return 1
    elif ConditionGroup(1):
        """State 3: Save HP reduction"""
        return 0

def event_m10_14_x99(z39=_):
    """[Execution] Preliminary Battle with Boss_Save HP
    z39: HP save flag
    """
    """State 0,1: HP save flag ON"""
    SetEventFlag(z39, 1)
    """State 2: A large number of transition prevention empty states"""
    assert (GetStateTime() > 0.1) != 0
    """State 3: End state"""
    return 0

def event_m10_14_x100(z37=_, z38=1000, z39=_):
    """[Preset] Preliminary Battle with Boss
    z37: HP reduction rate (%)
    z38: Enemy generator ID
    z39: HP save flag
    """
    """State 0,4: [Reproduction] Preliminary battle with boss _HP save and withdrawal_SubState"""
    call = event_m10_14_x162(z40=114020084)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] Preliminary Battle with Boss_HP Save and Withdrawal_SubState"""
        call = event_m10_14_x98(z37=z37, z38=z38, z85=202000, z86=202001, z87=30)
        if call.Get() == 2:
            pass
        elif call.Get() == 1:
            """State 3: [Execution] Preliminary Battle with Boss_Withdrawal_SubState"""
            assert event_m10_14_x93()
        elif call.Get() == 0:
            """State 2: [Execution] Preliminary Battle with Boss_HP Save_SubState"""
            assert event_m10_14_x99(z39=z39)
            """State 5: End state"""
            return 0
    """State 6: Withdrawal and destruction completed"""
    return 1

def event_m10_14_x101(z76=10140400, z83=50, z84=20, z81=600000):
    """[Reproduction] Sand door
    z76: OBJ instance ID of the sand door
    z83: OBJ state ID being destroyed
    z84: OBJ state ID after destruction
    z81: Navigation change point ID
    """
    """State 0,1: Has the sand door been destroyed?"""
    if CompareOwnObjStateId(z83, 0):
        """State 2: Navigation mesh change"""
        Label('L0')
        DeleteNavimeshAttribute(z81, 2)
        """State 3: Destroyed"""
        return 0
    elif CompareOwnObjStateId(z84, 0):
        Goto('L0')
    else:
        """State 4: Not destroyed"""
        return 1

def event_m10_14_x102(z76=10140400):
    """[Condition] Sand door
    z76: OBJ instance ID of the sand door
    """
    """State 0,1: PC behavior judgment"""
    IsObjSearched(0, z76)
    IsObjBroken(1, z76, 1)
    if ConditionGroup(0):
        """State 2: Access key guide"""
        return 0
    elif ConditionGroup(1):
        """State 3: Destroy the sand door"""
        return 1

def event_m10_14_x103(action1=1102):
    """[Execute] Sand door_dialog display
    action1: Text ID
    """
    """State 0,1: Dialog display: heavy and not open"""
    # action:1102:"Too heavy to open"
    DisplayOwnOkMenu(action1, 0, 0, 190, 0, 0, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x104(z76=10140400, z77=10141020, z82=20, z81=600000):
    """[Execution] Sand door_Sand display
    z76: OBJ instance ID of the sand door
    z77: OBJ instance ID of the ground
    z82: Ground display OBJ state ID
    z81: Navigation change point ID
    """
    """State 0,1: Ground OBJ display"""
    ChangeObjState(z77, z82)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z81, 2)
    """State 3: End state"""
    return 0

def event_m10_14_x105(z76=10140400, z77=10141020, z78=50, z79=20, z80=20, z81=600000, action1=1102):
    """[Preset] Sand door
    z76: OBJ instance ID of the sand door
    z77: OBJ instance ID of the ground
    z78: OBJ State ID during destruction of the sand door
    z79: OBJ State ID after destruction of the sand door
    z80: Ground display OBJ state ID
    z81: Navigation change point ID
    action1: Dialog text ID
    """
    """State 0,1: [Reproduction] Sand door_SubState"""
    call = event_m10_14_x101(z76=z76, z83=50, z84=20, z81=z81)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Condition] Sand door_SubState"""
        call = event_m10_14_x102(z76=z76)
        if call.Get() == 0:
            """State 2: [Execute] Sand door_Display dialog_SubState"""
            assert event_m10_14_x103(action1=action1)
            """State 5: Dialog display"""
            return 0
        elif call.Get() == 1:
            """State 3: [Execution] Sand door_Sand display_SubState"""
            assert event_m10_14_x104(z76=z76, z77=z77, z82=20, z81=z81)
    """State 6: Destroyed"""
    return 1

def event_m10_14_x106(z64=10141700, z65=101420, z66=0, z67=20260000, z68=900000):
    """[Preset] Check OBJ and warp between maps
    z64: OBJ instance ID to check
    z65: Pre-warp poly play ID
    z66: Poly Play ID after Warp
    z67: Map ID
    z68: Point ID
    """
    """State 0,1: [Reproduction] OBJ is examined and warp between maps_SubState"""
    call = event_m10_14_x107(z64=z64)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Inter-map warp_SubState by checking OBJ"""
        call = event_m10_14_x108(z64=z64)
        if call.Get() == 0:
            """State 3: [Execution] Inter-map warp_warp execution_SubState by checking OBJ"""
            assert event_m10_14_x109(z64=z64, z65=z65, z66=z66, z67=z67, z68=z68)
            Goto('L0')
        elif call.Get() == 1:
            """State 4: [Execution] Check OBJ, warp between maps_Key guide invalidation only_SubState"""
            assert event_m10_14_x110(z64=z64)
        elif call.Get() == 2:
            """State 5: [Execution] Giant's memory intrusion_Nothing happens_SubState"""
            assert event_m10_14_x120()
        """State 7: Rerun"""
        return 1
    """State 6: Finish"""
    Label('L0')
    return 0

def event_m10_14_x107(z64=10141700):
    """[Net] Duel matching cancellation
    z64: OBJ instance ID to check
    """
    """State 0,2: Did you get the Old Dragon Soul?"""
    if GetEventFlag(100460) != 0:
        """State 3: Display of crystal OBJ: 30"""
        ChangeObjState(z64, 30)
        """State 1: Disable key guide"""
        DisableObjKeyGuide(z64, 1)
        """State 4: End state"""
        return 0
    else:
        """State 5: Old dragon not acquired in Seoul"""
        return 1

def event_m10_14_x108(z64=10141700):
    """[Condition] Check OBJ and warp between maps
    z64: OBJ instance ID to check
    """
    """State 0,1: Single play and queen defeated?"""
    IsMultiplayer(8, 0, 1)
    CompareEventFlag(8, 114000081, 1)
    assert ConditionGroup(8)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z64, 0)
    """State 2: Was OBJ checked or multi?"""
    IsObjSearched(0, z64)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 6: Key guide disabled"""
    return 1
    """State 4: Do you have an ash mist core?"""
    Label('L0')
    # goods:50910000:Ashen Mist Heart
    DoesPlayerHaveItem(0, 50910000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 5: Warp execution"""
        return 0
    else:
        """State 7: Nothing happens"""
        return 2

def event_m10_14_x109(z64=10141700, z65=101420, z66=0, z67=20260000, z68=900000):
    """[Execution] Inter-map warp_warp execution after checking OBJ
    z64: OBJ instance ID to check
    z65: Pre-warp poly play ID
    z66: Poly Play ID after Warp
    z67: Map ID
    z68: Point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z64, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_14_x0(z65=z65, z66=z66, z67=z67, z68=z68)
    """State 4: End state"""
    return 0

def event_m10_14_x110(z64=10141700):
    """[Execution] Checking OBJ and only warping between maps_key guide invalidation
    z64: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z64, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x111(z34=1000, z35=204000):
    """[Condition] Deletion after withdrawal
    z34: Enemy generator ID
    z35: Deletion point ID
    """
    """State 0,1: Has the withdrawn character entered the withdrawal point? Or did you destroy it?"""
    IsChrInsidePoint(8, z34, z35, z35, 1)
    CompareEventFlag(8, 114000083, 1)
    CompareEventFlag(0, 114000081, 1)
    if ConditionGroup(0):
        """State 4: Destroyed"""
        return 1
    elif ConditionGroup(8):
        """State 2: Safety time"""
        assert (GetStateTime() > 5) != 0
        """State 3: End state"""
        return 0

def event_m10_14_x112(z34=1000):
    """[Execution] Deletion after withdrawal
    z34: Enemy generator ID
    """
    """State 0,1: Enemy deleted"""
    PauseEnemy(z34, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x113(z34=1000, z35=204000, z36=114020084):
    """[Preset] Deletion after withdrawal
    z34: Enemy generator ID
    z35: Deletion point ID
    z36: Generation determination flag
    """
    """State 0,3: [Reproduction] Delete after withdrawal_SubState"""
    call = event_m10_14_x163(z36=z36)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Delete after withdrawal_SubState"""
        call = event_m10_14_x111(z34=z34, z35=z35)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Delete after withdrawal_SubState"""
            assert event_m10_14_x112(z34=z34)
    """State 4: End state"""
    return 0

def event_m10_14_x114(z73=10140412):
    """[Reproduction] Insect key door _ Spider activation
    z73: Door instance ID
    """
    """State 0,1: Is the door unlocked?"""
    if CompareObjStateId(z73, 30, 0):
        """State 3: Unlocked"""
        return 1
    else:
        """State 2: Unlocked"""
        return 0

def event_m10_14_x115(z73=10140412):
    """[Conditions] Bug lock door_Spider activation: Unlocking judgment
    z73: Door instance ID
    """
    """State 0,1: Did you open the door?"""
    CompareObjState(0, z73, 10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x116(z75=114020072):
    """[Execution] Bug lock door_Spider start
    z75: Startup flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z75, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x117(z73=10140412, z74=1101000, z75=114020072):
    """[Preset] Insect Lock Door_Spider Launch
    z73: Door instance ID
    z74: Point ID
    z75: Startup flag
    """
    """State 0,1: [Reproduction] Bug's key door_Spider start_SubState"""
    call = event_m10_14_x114(z73=z73)
    if call.Get() == 0:
        """State 2: [Condition] Insect key door_Spider activation: Unlocking determination_SubState"""
        assert event_m10_14_x115(z73=z73)
    elif call.Get() == 1:
        """State 3: [Condition] Bug's key door_Spider start: Point judgment_SubState"""
        assert event_m10_14_x118(z74=z74)
    """State 4: [Execution] Bug's key door_Spider start_SubState"""
    assert event_m10_14_x116(z75=z75)
    """State 5: End state"""
    return 0

def event_m10_14_x118(z74=1101000):
    """[Condition] Insect lock door_Spider activation: Point judgment
    z74: Point ID
    """
    """State 0,1: Entered the specified area?"""
    IsPlayerInsidePoint(0, z74, z74, 1)
    IsPlayerInsidePoint(0, 1102000, 1102000, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x119(z69=_, z70=_, z71=_, z72=_):
    """Wandering & Patch: Death Determination
    z69: Death: Global event flag
    z70: Generator ID
    z71: For encounter: Global event flag
    z72: For opponent encounter: Global event flag
    """
    """State 0,1: Death determination: Start"""
    CompareEventStatus(8, 111255, 1, 0)
    CompareEventFlag(0, z71, 1)
    CompareEventFlag(0, z71, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 2: Death determination: Death determination"""
        CompareEventFlag(0, z69, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Death determination: Wait"""
            IsChrDead(0, z70)
            IsPlayerInTheMap(1, 0, 0)
            if ConditionGroup(0):
                """State 4: Death determination: death flag setting"""
                SetEventFlag(z69, 1)
                CompareEventFlag(0, z69, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(1):
                pass
    """State 5: Death determination: System: End"""
    EndMachine()

def event_m10_14_x120():
    """[Execution] Giant's memory intrusion_Nothing happens"""
    """State 0,1: Message display"""
    # action:1113:"Alas, nothing happened"
    DisplayOwnOkMenu(1113, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m10_14_x121(z8=100460):
    """[Reproduction] Red Soul and Complicated Display
    z8: Old Dragon's Soul Acquisition Flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Has an old dragon acquired Seoul?"""
    if GetEventFlag(z8) != 1:
        """State 3: Waiting for display"""
        return 0
    else:
        """State 5: End: Hide"""
        return 2
    """State 4: Guest user"""
    Label('L0')
    return 1

def event_m10_14_x122(z9=100951):
    """[Condition] Red Soul and Complicated Display
    z9: Defeated queen flag
    """
    """State 0,1: Did you destroy the queen of nieces?"""
    CompareEventFlag(0, z9, 1)
    assert ConditionGroup(0)
    """State 2: Red soul display"""
    return 0

def event_m10_14_x123(z6=10141705, z7=2004, z8=100460):
    """[Execution] Red Soul and Complicated Display _Acquisition and Complicated Display
    z6: Damipoli OBJ instance ID
    z7: Text ID
    z8: Old Dragon's Soul Acquisition Flag
    """
    """State 0,2: Display of haze: 32"""
    ChangeObjState(z6, 32)
    """State 1: Old Dragon Soul Acquisition Flag ON"""
    SetEventFlag(z8, 1)
    """State 3: Production FE display"""
    OpenPresentationWindow(22)
    assert PresentationWindowDisplay() != 0
    """State 4: End state"""
    return 0

def event_m10_14_x124(z6=10141705, z7=2004, z8=100460, z9=100951):
    """[Preset] Red Soul and Complicated Display
    z6: Damipoli OBJ instance ID
    z7: Text ID
    z8: Old Dragon's Soul Acquisition Flag
    z9: Defeated queen flag
    """
    """State 0,1: [Reproduction] Red Soul and Complicated Display _SubState"""
    call = event_m10_14_x121(z8=z8)
    if call.Get() == 0:
        """State 4: [Condition] Red Soul and Complicated Display _Defeat Judgment_SubState"""
        assert event_m10_14_x122(z9=z9) == 0
        """State 3: [Run] Red Soul and Complicated Display_Red Soul Display_SubState"""
        assert event_m10_14_x126(z6=z6)
        """State 6: [Reproduction] Red Soul and Complicated Display_Sky_SubState"""
        assert event_m10_14_x127()
        """State 5: [Condition] Red Soul and Complicated Display_Judgment to Check_SubState"""
        call = event_m10_14_x125(z6=z6)
        if call.Get() == 1:
            """State 8: [Execution] Red Soul and Complicated Display_Key Guide Switch_SubState"""
            assert event_m10_14_x184(z6=z6)
            """State 10: Rerun"""
            return 1
        elif call.Get() == 0:
            """State 2: [Execution] Red Soul and Complicated Display_Acquisition and Complicated Display_SubState"""
            assert event_m10_14_x123(z6=z6, z7=z7, z8=z8)
    elif call.Get() == 2:
        """State 7: [Run] Red Soul and Complicated Display_Hide_SubState"""
        assert event_m10_14_x128(z6=z6)
    elif call.Get() == 1:
        pass
    """State 9: Finish"""
    return 0

def event_m10_14_x125(z6=10141705):
    """[Condition] Red Soul and Complicated Display
    z6: Damipoli OBJ instance ID
    """
    """State 0,1: Did you check the red soul or became a boss battle?"""
    IsObjSearched(0, z6)
    IsEventBossBattle(1, 1014000, 1)
    if ConditionGroup(1):
        """State 3: During the boss battle"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m10_14_x126(z6=10141705):
    """[Execution] Red Soul and Complicated Display_Red Soul Display
    z6: Damipoli OBJ instance ID
    """
    """State 0,1: Red Soul Display: 30"""
    ChangeObjState(z6, 30)
    """State 2: End state"""
    return 0

def event_m10_14_x127():
    """[Reproduction] Red Soul and Complicated Display_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x128(z6=10141705):
    """[Run] Red Soul and Complicated Display_Hide
    z6: Damipoli OBJ instance ID
    """
    """State 0,1: Damipoli OBJ hidden: 10"""
    ChangeObjState(z6, 10)
    """State 2: End state"""
    return 0

def event_m10_14_x129(z59=_, z60=_, z61=_, z62=20, z63=10):
    """[Preset] Door that opens with a wall lever
    z59: Lever OBJ instance ID
    z60: Door OBJ instance ID
    z61: Point ID for Navimesh change
    z62: Door OBJ open state ID
    z63: Initial state of door OBJ
    """
    """State 0,1: [Reproduction] Door opened with wall lever _SubState"""
    call = event_m10_14_x130(z60=z60, z62=z62, z63=z63)
    if call.Get() == 0:
        """State 2: [Condition] Door that opens with a wall lever_SubState"""
        assert event_m10_14_x131(z59=z59)
        """State 3: [Execution] Door opened with a wall lever_Unopened_SubState"""
        assert event_m10_14_x132(z60=z60, z61=z61, z62=z62, z59=z59)
    elif call.Get() == 1:
        """State 4: [Execution] Door opened with a wall lever_Opened_SubState"""
        assert event_m10_14_x133(z61=z61, z59=z59, z60=z60)
    """State 5: End state"""
    return 0

def event_m10_14_x130(z60=_, z62=20, z63=10):
    """[Reproduction] Door that opens with wall lever
    z60: Door OBJ instance ID
    z62: Door OBJ open state ID
    z63: Initial state of door OBJ
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z60, z63, 1):
        """State 3: Opened"""
        return 1
    else:
        """State 2: Not open"""
        return 0

def event_m10_14_x131(z59=_):
    """[Conditions] Door opened with wall lever
    z59: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z59, 74, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x132(z60=_, z61=_, z62=20, z59=_):
    """[Execution] Door opened with a wall lever_not open
    z60: Door OBJ instance ID
    z61: Point ID for Navimesh change
    z62: Door OBJ open state ID
    z59: Lever OBJ instance ID
    """
    """State 0,1: Door that opens with lever"""
    ChangeObjState(z60, 70)
    assert CompareObjStateId(z60, z62, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z61, 2)
    """State 3: Disable key guide of lever"""
    DisableObjKeyGuide(z59, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x133(z61=_, z59=_, z60=_):
    """[Execution] Door that opens with wall lever_Opened
    z61: Point ID for Navimesh change
    z59: Lever OBJ instance ID
    z60: Door OBJ instance ID
    """
    """State 0,3: Waiting for the door to open"""
    assert CompareObjStateId(z60, 20, 0)
    """State 1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z61, 2)
    """State 2: Disable key guide of lever"""
    DisableObjKeyGuide(z59, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x134(z58=114000070):
    """[Reproduction] Alarm treasure chest
    z58: Spider start flag
    """
    """State 0,1: Has the trap been activated?"""
    if GetEventFlag(z58) != 0:
        """State 3: Trap executed"""
        return 1
    else:
        """State 2: Trap not executed"""
        return 0

def event_m10_14_x135(z57=10145060):
    """[Condition] Alarm treasure chest
    z57: OBJ instance ID of treasure chest
    """
    """State 0,1: Did the treasure box be confirmed or broken?"""
    CompareObjState(0, z57, 75, 0)
    CompareObjState(0, z57, 100, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x136(z58=114000070):
    """[Execute] Alarm treasure chest
    z58: Spider start flag
    """
    """State 0,1: Spider start flag ON"""
    SetEventFlag(z58, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x137(z57=10145060, z58=114000070):
    """[Preset] Alarm treasure chest
    z57: OBJ instance ID of treasure chest
    z58: Spider start flag
    """
    """State 0,1: [Reproduction] Alarm treasure chest _ Start _ SubState"""
    call = event_m10_14_x134(z58=z58)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Alarm treasure chest"""
        assert event_m10_14_x135(z57=z57)
        """State 2: [Execution] Alarm treasure chest _ Start _ SubState"""
        assert event_m10_14_x136(z58=z58)
    """State 4: End state"""
    return 0

def event_m10_14_x138(z55=_, z56=_):
    """[Preset] Treasure corpse
    z55: 壺 OBJ instance ID
    z56: Instance ID of treasure corpse OBJ
    """
    """State 0,1: [Reproduction] Treasure corpse _SubState"""
    call = event_m10_14_x139(z55=z55, z56=z56)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] If you break the trap, the treasure corpse_SubState"""
        assert event_m10_14_x140(z55=z55)
        """State 3: [Execution] If you break the trap, the treasure corpse_SubState"""
        assert event_m10_14_x141(z56=z56)
    """State 4: End state"""
    return 0

def event_m10_14_x139(z55=_, z56=_):
    """[Reproduction] Treasure corpse
    z55: 壺 OBJ instance ID
    z56: Instance ID of treasure corpse OBJ
    """
    """State 0,1: 判定 Judgment of OBJ status"""
    if CompareObjStateId(z55, 20, 0):
        """State 2: Anime execution of treasure corpse OBJ"""
        ChangeObjState(z56, 73)
        """State 5: 壺: Destroyed"""
        return 1
    else:
        """State 3: Hidden body hidden"""
        ChangeDrawHit(z56, 0)
        """State 4: 壺: Undestructed"""
        return 0

def event_m10_14_x140(z55=_):
    """[Condition] If you break a spear,
    z55: 壺 OBJ instance ID
    """
    """State 0,1: Did you destroy 壺 OBJ?"""
    CompareObjState(0, z55, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x141(z56=_):
    """[Execution] Treasure corpse
    z56: Instance ID of treasure corpse OBJ
    """
    """State 0,2: Treasure corpse display"""
    ChangeDrawHit(z56, 1)
    """State 1: Anime execution of treasure corpse OBJ"""
    ChangeObjState(z56, 73)
    """State 3: End state"""
    return 0

def event_m10_14_x142(z52=114020084):
    """[Reproduction] Preliminary battle _ time limit setting
    z52: Pre-battle boss generation determination flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Queen generation flag determination"""
        if GetEventFlag(z52) != 1:
            pass
        else:
            """State 3: Not destroyed or withdrawn"""
            return 0
    """State 4: Simple end"""
    return 1

def event_m10_14_x143(z52=114020084, z53=1000, z54=114000081):
    """[Condition] Preliminary Battle_Time limit setting
    z52: Front boss boss generation flag
    z53: Generator ID
    z54: Defeat flag
    """
    """State 0,1: Generation of start battle boss & activation state release or destruction flag ON"""
    CompareChrStartUpState(8, z53, 2, 1)
    CompareEventFlag(8, z52, 1)
    CompareEventFlag(0, z54, 1)
    if ConditionGroup(0):
        """State 3: Defeated the boss"""
        return 1
    elif ConditionGroup(8):
        """State 2: Pre-time battle time limit start"""
        return 0

def event_m10_14_x144():
    """[Execution] Preliminary Battle_Set time limit"""
    """State 0,1: Start timer for time limit"""
    StartAreaTimer(0)
    """State 2: End state"""
    return 0

def event_m10_14_x145(z52=114020084, z53=1000, z54=114000081):
    """[Preset] Preliminary Battle_Time limit setting
    z52: Outpost Battle Boss Generation Flag
    z53: Generator ID
    z54: Defeat flag
    """
    """State 0,1: [Reproduction] Preliminary Battle_Time Limit_SubState"""
    call = event_m10_14_x142(z52=z52)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Front battle_Time limit setting_SubState"""
        call = event_m10_14_x143(z52=z52, z53=z53, z54=z54)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Preliminary Battle_Time Limit Setting_SubState"""
            assert event_m10_14_x144()
    """State 4: End state"""
    return 0

def event_m10_14_x146():
    """[Reproduction] Treasure corpse fall _ sky with yagura destruction"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x147(z50=10146290, z51=70):
    """[Execution] Treasure corpse falls due to yagura destruction
    z50: Instance ID of treasure corpse
    z51: Falling state ID
    """
    """State 0,1: Treasure corpse fall"""
    ChangeObjState(z50, z51)
    """State 2: End state"""
    return 0

def event_m10_14_x148(z49=10141550):
    """[Condition] Treasure corpse falls due to yagura destruction
    z49: Yagura instance ID
    """
    """State 0,1: Waiting for destruction of the tower"""
    IsObjBroken(0, z49, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x149(z49=10141550, z50=10146290, z51=70):
    """[Preset] Treasure corpse falls due to yagura destruction
    z49: Yagura instance ID
    z50: Instance ID of treasure corpse
    z51: Falling state ID
    """
    """State 0,1: [Reproduction] Treasure corpse fall due to yagura destruction_Sky_SubState"""
    assert event_m10_14_x146()
    """State 2: [Condition] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_14_x148(z49=z49)
    """State 3: [Execution] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_14_x147(z50=z50, z51=z51)
    """State 4: End state"""
    return 0

def event_m10_14_x150(z46=_, z47=_, z48=_):
    """[Preset] Navimesh change due to yagura destruction
    z46: YAGURA OBJ instance ID
    z47: Point ID for changing Navimesh at the top of the tower
    z48: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: [Reproduction] Navi mesh change due to yagura destruction_SubState"""
    call = event_m10_14_x151(z46=z46)
    if call.Get() == 0:
        """State 2: [Condition] Navi mesh change due to yagura destruction_SubState"""
        assert event_m10_14_x152(z46=z46)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x153(z47=z47, z48=z48)
    """State 4: End state"""
    return 0

def event_m10_14_x151(z46=_):
    """[Reproduction] Navi mesh change due to yagura destruction
    z46: YAGURA OBJ instance ID
    """
    """State 0,1: State determination of yagura OBJ"""
    if CompareObjStateId(z46, 20, 1):
        """State 2: Undestructed"""
        return 0
    else:
        """State 3: Destroyed"""
        return 1

def event_m10_14_x152(z46=_):
    """[Condition] Navi mesh change due to yagura destruction
    z46: YAGURA OBJ instance ID
    """
    """State 0,1: Yagura OBJ transition waiting"""
    CompareObjState(0, z46, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x153(z47=_, z48=_):
    """[Execution] Navi mesh change due to yagura destruction
    z47: Point ID for changing Navimesh at the top of the tower
    z48: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: Added navigating mesh attributes at the top of the tower"""
    AddNavimeshAttribute(z47, 2)
    """State 2: Navimesh attribute deletion at the bottom of the tower"""
    DeleteNavimeshAttribute(z48, 2)
    """State 3: End state"""
    return 0

def event_m10_14_x154(z44=114020050):
    """[Preset] Probability of piglet appearance
    z44: Piglet generation flag
    """
    """State 0,1: [Reproduction] Appearance of piglets with probability _SubState"""
    assert event_m10_14_x155()
    """State 2: [Condition] Appearance of piglet with probability_SubState"""
    call = event_m10_14_x156()
    if call.Get() == 0:
        """State 3: [Execution] Probability of piglet appearance"""
        assert event_m10_14_x157(z44=z44, z45=1)
    elif call.Get() == 1:
        """State 4: [Execution] Appearance of piglet with probability_No piglet appearance_SubState"""
        assert event_m10_14_x157(z44=z44, z45=0)
    """State 5: End state"""
    return 0

def event_m10_14_x155():
    """[Reproduction] Appearance of piglets with probability"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x156():
    """[Condition] Appearance of piglets with probability"""
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 999)
    """State 2: Random number judgment"""
    CompareEventRandValue(0, 0, 0, 0)
    if ConditionGroup(0):
        """State 3: Piglet appearance"""
        return 0
    else:
        """State 4: No piglet appeared"""
        return 1

def event_m10_14_x157(z44=114020050, z45=_):
    """[Execution] Appearance of piglets with probability
    z44: Piglet generation flag
    z45: ON / OFF of piglet generation flag
    """
    """State 0,1: Change the flag state based on the random number result"""
    SetEventFlag(z44, z45)
    """State 2: End state"""
    return 0

def event_m10_14_x158(z41=114000081, z42=114000083):
    """[Conditions] Prelude Battle_Queen Generation Judgment
    z41: Boss destruction flag
    z42: Withdrawal flag
    """
    """State 0,3: Is the number of game laps 2 or more?"""
    CompareGameCycleForBonfire(0, 0, 0, 1, 0)
    if ConditionGroup(0):
        pass
    else:
        Goto('L0')
    """State 7: Number of laps 1"""
    return 3
    """State 1: Are you killing the boss?"""
    Label('L0')
    CompareEventFlag(0, z41, 1)
    if ConditionGroup(0):
        pass
    else:
        Goto('L1')
    """State 5: Boss killed"""
    return 1
    """State 2: Has it been withdrawn?"""
    Label('L1')
    CompareEventFlag(0, z42, 1)
    if ConditionGroup(0):
        """State 6: Withdrawn"""
        return 2
    else:
        """State 4: Pre-battle starts"""
        return 0

def event_m10_14_x159():
    """[Reproduction] Prelude Battle_Queen Generation Judgment"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m10_14_x160(z43=114020084):
    """[Execution] Prelude Battle_Generation of Queen
    z43: Queen generation flag
    """
    """State 0,1: Former Samurai Battle_Two Queen Generation Flag ON"""
    SetEventFlag(z43, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x161(z41=114000081, z42=114000083, z43=114020084):
    """[Preset] Prelude Battle_Queen Generation Judgment
    z41: Boss destruction flag
    z42: Withdrawal flag
    z43: Queen generation flag
    """
    """State 0,1: [Reproduction] Prelude Battle_Queen Generation Determination_SubState"""
    call = event_m10_14_x159()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Preliminary Battle_Queen Generation Judgment_SubState"""
        call = event_m10_14_x158(z41=z41, z42=z42)
        if call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
        elif call.Get() == 3:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Prelude Battle_Queen Generation Judgment_SubState"""
            assert event_m10_14_x160(z43=z43)
    """State 4: End state"""
    return 0

def event_m10_14_x162(z40=114020084):
    """[Reproduction] Preliminary Battle with Boss
    z40: Pre-battle boss generation determination flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Queen generation flag determination"""
        if GetEventFlag(z40) != 1:
            pass
        else:
            """State 3: Not destroyed or withdrawn"""
            return 0
    """State 4: Simple end"""
    return 1

def event_m10_14_x163(z36=114020084):
    """[Reproduction] Deletion after withdrawal
    z36: Pre-battle boss generation determination flag
    """
    """State 0,1: Queen generation flag determination"""
    if GetEventFlag(z36) != 1:
        """State 3: Simple end"""
        return 1
    else:
        """State 2: Not destroyed or withdrawn"""
        return 0

def event_m10_14_x164(z30=10143101, z31=10145120, z32=500000, z33=10143100):
    """[Preset] Treasure chest appears when switch is pulled
    z30: Scaffolding OBJ instance ID
    z31: Treasure chest OBJ instance ID
    z32: Point ID for Navimesh change
    z33: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Treasure chest appears when switch is pulled_SubState"""
    call = event_m10_14_x90(z30=z30, z31=z31, z32=z32, z33=z33)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] When you pull the switch, a treasure box appears._SubState"""
        assert event_m10_14_x91(z33=z33)
        """State 3: [Execution] Treasure chest appears when switch is pulled_SubState"""
        assert event_m10_14_x92(z30=z30, z32=z32, z33=z33)
    """State 4: End state"""
    return 0

def event_m10_14_x165(z25=114000081, z26=1014001, z27=1000, z28=114020084, z29=114000083):
    """[Preset] Outpost Battle_Boss HP Gauge Display
    z25: Boss destruction flag
    z26: Boss Battle ID
    z27: Generator ID
    z28: Generation determination flag
    z29: Withdrawal flag
    """
    """State 0,1: [Reproduction] Prelude Battle_Boss HP Gauge Display_SubState"""
    call = event_m10_14_x166(z25=z25)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Conditions] Preliminary Battle_Boss HP Gauge Display_SubState"""
        assert event_m10_14_x167(z27=z27, z28=z28)
        """State 3: [Execution] Prelude Battle_Boss HP Gauge Display_SubState"""
        assert event_m10_14_x168(z26=z26)
        """State 2: [Reproduction] Prelude Battle_Boss HP Gauge Display_Sky_SubState"""
        assert event_m10_14_x169()
        """State 6: [Condition] Preliminary Battle_Boss HP Gauge Display_End Judgment_SubState"""
        assert event_m10_14_x170(z29=z29)
        """State 4: [Execution] Prelude Battle_Boss HP Gauge Display_End_SubState"""
        assert event_m10_14_x171(z26=z26)
    """State 7: End state"""
    return 0

def event_m10_14_x166(z25=114000081):
    """[Reproduction] Front battle _ boss HP gauge display
    z25: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z25) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_14_x167(z27=1000, z28=114020084):
    """[Conditions] Front battle_Boss HP gauge display
    z27: Generator ID
    z28: Generation determination flag
    """
    """State 0,1: Generating the start battle boss and canceling the activation state"""
    CompareChrStartUpState(8, z27, 2, 1)
    IsChrActive(8, z27, 1)
    CompareEventFlag(8, z28, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_14_x168(z26=1014001):
    """[Execution] Prelude Battle_Boss HP Gauge Display
    z26: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z26)
    """State 2: End state"""
    return 0

def event_m10_14_x169():
    """[Reproduction] Prelude Battle_Boss HP Gauge Display_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x170(z29=114000083):
    """[Condition] Prelude Battle_Boss HP Gauge Display_End Judgment
    z29: Withdrawal flag
    """
    """State 0,1: Has the withdrawal started?"""
    CompareEventFlag(0, z29, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x171(z26=1014001):
    """[Execution] Prelude Battle_Boss HP Gauge Display_End
    z26: Boss Battle ID
    """
    """State 0,1: Boss battle end notification"""
    CancelBossFight(z26)
    """State 2: End state"""
    return 0

def event_m10_14_x172(z21=10141180, z22=2500000, z23=2500001, z24=10141170):
    """[Preset] Interlocking destruction due to scaffold destruction
    z21: Scaffolding OBJ instance ID
    z22: Point ID for changing the navigation mesh at the top of the scaffold
    z23: Point ID for changing the navigation mesh at the bottom of the scaffold
    z24: Instance ID of scaffolding OBJ to be interlocked
    """
    """State 0,1: [Reproduction] Interlocking destruction due to scaffold destruction_SubState"""
    call = event_m10_14_x173(z21=z21, z22=z22, z23=z23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Interlocking destruction due to scaffold destruction_SubState"""
        assert event_m10_14_x174(z21=z21)
    """State 3: [Execution] Linkage destruction due to scaffold destruction_SubState"""
    assert event_m10_14_x175(z22=z22, z23=z23, z24=z24)
    """State 4: End state"""
    return 0

def event_m10_14_x173(z21=10141180, z22=2500000, z23=2500001):
    """[Reproduction] Interlocking destruction due to scaffold destruction
    z21: Scaffolding OBJ instance ID
    z22: Point ID for changing the navigation mesh at the top of the scaffold
    z23: Point ID for changing the navigation mesh at the bottom of the scaffold
    """
    """State 0,1: Scaffold OBJ status determination"""
    if CompareObjStateId(z21, 20, 0):
        """State 5: Destroyed"""
        return 1
    else:
        """State 2: Navi-mesh attribute deletion at the top of the scaffold"""
        DeleteNavimeshAttribute(z22, 2)
        """State 3: Added navigation mesh attributes at the bottom of the scaffolding"""
        AddNavimeshAttribute(z23, 2)
        """State 4: Undestructed"""
        return 0

def event_m10_14_x174(z21=10141180):
    """[Condition] Interlocking destruction due to scaffold destruction
    z21: Scaffolding OBJ instance ID
    """
    """State 0,1: Has the scaffold OBJ been destroyed?"""
    CompareObjState(0, z21, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x175(z22=2500000, z23=2500001, z24=10141170):
    """[Execution] Interlocking destruction due to scaffold destruction
    z22: Point ID for changing the navigation mesh at the top of the scaffold
    z23: Point ID for changing the navigation mesh at the bottom of the scaffold
    z24: Instance ID of scaffolding OBJ to be interlocked
    """
    """State 0,1: Added navigation mesh attributes at the top of the scaffold"""
    AddNavimeshAttribute(z22, 2)
    """State 2: Navimesh attribute deletion at the bottom of the scaffold"""
    DeleteNavimeshAttribute(z23, 2)
    """State 3: Judgment of the state of the scaffold where interlocking destruction occurs"""
    CompareObjState(0, z24, 10, 0)
    if ConditionGroup(0):
        """State 4: Destroying the scaffold where interlocking destruction occurs"""
        ChangeObjState(z24, 20)
    else:
        pass
    """State 5: End state"""
    return 0

def event_m10_14_x176(z14=114000052, z16=10146500):
    """[Reproduction] Pig eats mushrooms
    z14: Mushroom complete eating flag
    z16: Item OBJ instance ID
    """
    """State 0,1: Have you already eaten mushrooms?"""
    if GetEventFlag(z14) != 0:
        """State 4: Meal"""
        return 1
    else:
        """State 2: Hide item"""
        ChangeDrawHit(z16, 0)
        """State 3: Before meal"""
        return 0

def event_m10_14_x177(z19=_, z17=2300000, z20=2300000, z18=10, z14=114000052):
    """[Condition] Pigs eat mushrooms
    z19: Pig generator ID
    z17: Start point ID
    z20: End point ID
    z18: Time to complete meal
    z14: Meal completion flag
    """
    """State 0,1: Has the pig started to eat mushrooms?"""
    CompareChrEzStateValue(0, z19, 7, 1, 0)
    assert ConditionGroup(0)
    """State 2: Meal success or failure"""
    CompareEventFlag(0, z14, 1)
    CompareChrEzStateValue(8, z19, 7, 1, 0)
    CompareStateTime(8, z18, 3, z18)
    CompareChrEzStateValue(1, z19, 7, 1, 1)
    if ConditionGroup(0):
        """State 5: Other pigs successfully eat: finished"""
        return 2
    elif ConditionGroup(8):
        """State 3: Meal success: item display"""
        return 0
    elif ConditionGroup(1):
        """State 4: Meal failure: re-execution"""
        return 1

def event_m10_14_x178(z14=114000052, z15=10141590, z16=10146500):
    """[Execution] Pigs eat mushrooms
    z14: Mushroom complete eating flag
    z15: Mushroom OBJ instance ID
    z16: Item OBJ instance ID
    """
    """State 0,1: Mushroom OBJ complete meal: 10"""
    ChangeObjState(z15, 10)
    """State 2: Item appearance"""
    ChangeDrawHit(z16, 1)
    """State 3: Mushroom complete meal flag ON"""
    SetEventFlag(z14, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x179(z14=114000052, z15=10141590, z16=10146500, z17=2300000, z18=10, z19=_):
    """[Preset] Pigs eat mushrooms
    z14: Mushroom complete eating flag
    z15: Mushroom OBJ instance ID
    z16: Item OBJ instance ID
    z17: Point ID
    z18: Time to complete meal
    z19: Pig generator ID
    """
    """State 0,2: [Reproduction] Pig eats mushrooms_SubState"""
    call = event_m10_14_x176(z14=z14, z16=z16)
    if call.Get() == 1:
        """State 1: Item display"""
        Label('L0')
        ChangeDrawHit(z16, 1)
    elif call.Get() == 0:
        """State 4: [Condition] Pig eats mushrooms_SubState"""
        call = event_m10_14_x177(z19=z19, z17=z17, z20=z17, z18=z18, z14=z14)
        if call.Get() == 2:
            Goto('L0')
        elif call.Get() == 0:
            """State 3: [Execution] Pig eats mushrooms_SubState"""
            assert event_m10_14_x178(z14=z14, z15=z15, z16=z16)
        elif call.Get() == 1:
            """State 6: Rerun"""
            return 1
    """State 5: End state"""
    return 0

def event_m10_14_x180():
    """[Reproduction] Boss: The queen of fox"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x181(z10=_, z11=114000081, z12=120):
    """[Conditions] Boss: Queen of Akatsuki _ Zakokoku generation
    z10: Zako Generator ID
    z11: Boss destruction flag
    z12: Time to flag ON
    """
    """State 0,1: Corresponding spider died or destroyed boss"""
    IsChrDead(0, z10)
    CompareEventFlag(1, z11, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 2: Generation waiting or boss destruction"""
        CompareStateTime(0, z12, 3, z12)
        CompareEventFlag(1, z11, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 3: Zako death: flag ON"""
            return 0
    """State 4: Defeat Boss: Finish"""
    return 1

def event_m10_14_x182(z13=_):
    """[Execution] Boss: Spider Queen
    z13: Zako spider generation flag
    """
    """State 0,1: Generation flag ON"""
    SetEventFlag(z13, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x183(z10=_, z11=114000081, z12=120, z13=_):
    """[Preset] Boss
    z10: Zako Generator ID
    z11: Boss destruction flag
    z12: Time to flag ON
    z13: Zako spider generation flag
    """
    """State 0,1: [Reproduction] Boss: Saddle Queen_Zako Spider Generation_Sky_SubState"""
    assert event_m10_14_x180()
    """State 3: [Conditions] Boss: The queen of fox"""
    call = event_m10_14_x181(z10=z10, z11=z11, z12=z12)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Boss: Spider Queen"""
        assert event_m10_14_x182(z13=z13)
    """State 4: End state"""
    return 0

def event_m10_14_x184(z6=10141705):
    """[Execution] Red Soul and Complicated Display_Key Guide Change
    z6: Damipoli OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z6, 1)
    """State 2: Is the boss battle over?"""
    IsEventBossBattle(0, 1014000, 0)
    assert ConditionGroup(0)
    """State 3: Enable key guide"""
    DisableObjKeyGuide(z6, 0)
    """State 4: Rerun"""
    return 0

def event_m10_14_x185(z4=_, z5=_):
    """[DC] [Reproduction] Lighthouse lighting management
    z4: Lighthouse instance ID
    z5: Lighting flag
    """
    """State 0,1: Is it already lit?"""
    if CompareObjStateId(z4, 30, 0):
        """State 2: Lighting flag ON"""
        SetEventFlag(z5, 1)
        """State 4: Already lit"""
        return 1
    else:
        """State 3: Unlit"""
        return 0

def event_m10_14_x186(z4=_):
    """[DC] [Condition] Lighthouse lighting management
    z4: Lighthouse instance ID
    """
    """State 0,1: Waiting for lighting"""
    CompareObjState(0, z4, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x187(z5=_):
    """[DC] [execution] Lighthouse lighting management
    z5: Lighting flag
    """
    """State 0,1: Lighting flag ON"""
    SetEventFlag(z5, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x188(z4=_, z5=_):
    """[DC] [Preset] Lighthouse lighting management
    z4: Lighthouse instance ID
    z5: Lighting flag
    """
    """State 0,1: [DC] [Reproduction] Lighthouse lighting management_SubState"""
    call = event_m10_14_x185(z4=z4, z5=z5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Lighthouse lighting management_SubState"""
        assert event_m10_14_x186(z4=z4)
        """State 2: [DC] [execution] Lighthouse lighting management_SubState"""
        assert event_m10_14_x187(z5=z5)
    """State 4: Finish"""
    return 0

def event_m10_14_x189(z2=_):
    """[DC] [Conditions] Switching thorn damage of farmers
    z2: Generator ID
    """
    """State 0,1: Mining action is finished or died?"""
    IsChrDeadOrRespawnOver(0, z2, 1)
    CompareChrEzStateValue(1, z2, 7, 2, 0)
    if ConditionGroup(0):
        """State 3: death"""
        return 1
    elif ConditionGroup(1):
        """State 2: End of action"""
        return 0

def event_m10_14_x190(z2=_, z3=200014060):
    """[DC] [Execution] Thorn damage switching of peasant deceased
    z2: Generator ID
    z3: Damage ID
    """
    """State 0,1: Activate damage"""
    SetDamageImmunityByGeneratorId(z2, z3, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x191(z2=_, z3=200014060):
    """[DC] [reproduction] Thorn damage switching of peasant deceased
    z2: Generator ID
    z3: Damage ID
    """
    """State 0,1: Damage invalidation"""
    SetDamageImmunityByGeneratorId(z2, z3, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x192(z2=_, z3=200014060):
    """[DC] [Preset] Thorn damage switching for farmers
    z2: Generator ID
    z3: Damage ID
    """
    """State 0,1: [DC] [Reproduction] Thorn damage switching of a peasant deceased_SubState"""
    assert event_m10_14_x191(z2=z2, z3=z3)
    """State 3: [DC] [Condition] Switching thorn damage of peasant_substate_SubState"""
    call = event_m10_14_x189(z2=z2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [DC] [execution] Thorn damage switching of a farmer deceased_SubState"""
        assert event_m10_14_x190(z2=z2, z3=z3)
    """State 4: End state"""
    return 0

def event_m10_14_x193():
    """[DC] [Reproduction] Unlockable management of the peasant _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x194(z1=_):
    """[DC] [Conditions] Unlockable management of peasant deceased
    z1: Generator ID
    """
    """State 0,1: Mining behavior judgment"""
    CompareChrEzStateValue(0, z1, 7, 2, 1)
    CompareChrEzStateValue(1, z1, 7, 2, 0)
    if ConditionGroup(1):
        """State 3: In combat"""
        return 1
    elif ConditionGroup(0):
        """State 2: Mining"""
        return 0

def event_m10_14_x195(z1=_):
    """[DC] [execution] Unlockable management of peasant deceased
    z1: Generator ID
    """
    """State 0,1: Grants a non-locking effect"""
    SetEnemySpEffect(z1, 170000000, 19, 4)
    """State 2: Did you start battle or died?"""
    CompareChrEzStateValue(0, z1, 7, 2, 0)
    IsChrDead(0, z1)
    assert ConditionGroup(0)
    """State 3: Cancel lock disable effect"""
    ClearEnemySpEffect(z1, 170000000)
    """State 4: Finish"""
    return 0

def event_m10_14_x196(z1=_):
    """[DC] [Preset] Farmer deceased locked management
    z1: Generator ID
    """
    """State 0,1: [DC] [Reproduction] Farmer deceased locked lock_empty_SubState"""
    assert event_m10_14_x193()
    """State 3: [DC] [Conditions] Unlockable management of farmer deceased_SubState"""
    call = event_m10_14_x194(z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [DC] [execution] Farmer deceased lock disabled management_SubState"""
        assert event_m10_14_x195(z1=z1)
    """State 4: Finish"""
    return 0

def event_m10_14_111232():
    """OBJ: Wandering Warrior: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_14_x1(z187=104153, z188=10144300, z189=56, z190=7420)

def event_m10_14_111233():
    """OBJ: Wandering Warrior: Key Guide"""
    """State 0,1: Death map flag judgment"""
    CompareEventFlag(0, 104153, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_14_x4(z182=114010110, z183=114020111, z184=104150, z185=10144300, z186=111232, npc1=7420)

def event_m10_14_111234():
    """OBJ: Wandering Warrior: Death Judgment"""
    """State 0,1: Wandering & Patch: Death Determination_SubState"""
    event_m10_14_x119(z69=104153, z70=55, z71=102402, z72=102445)

def event_m10_14_111235():
    """OBJ: Wandering Warrior: Battle Event: Appearance Judgment"""
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, 104150, 1)
        CompareEventFlag(1, 104171, 1)
        CompareEventFlag(2, 104172, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(2):
            pass
        else:
            """State 3: Appearance Judgment: Wandering & Patch: Emigration Judgment"""
            CompareEventFlag(8, 102406, 1)
            CompareEventFlag(8, 103652, 0)
            CompareEventFlag(8, 102451, 1)
            CompareEventFlag(8, 103672, 0)
            if ConditionGroup(8):
                """State 4: Appearance determination: Appearable"""
                SetEventFlag(114000118, 1)
                CompareEventFlag(0, 114000118, 1)
                assert ConditionGroup(0)
                Goto('L0')
            else:
                pass
        """State 5: Appearance judgment: Impossible to appear"""
        SetEventFlag(114000118, 0)
        CompareEventFlag(0, 114000118, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m10_14_111246():
    """OBJ: Satoshi Tsutsumi: White phantom sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m10_14_x31(z134=102430, z135=526, z136=104160, z137=103660, z138=-1)

def event_m10_14_111247():
    """OBJ: Satoshi Tsutsumi: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_14_x28(z149=114000096, z150=102436, z151=205, z152=7430)

def event_m10_14_111252():
    """OBJ: Patch: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_14_x1(z187=104173, z188=10144200, z189=66, z190=7440)

def event_m10_14_111253():
    """OBJ: Patch: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7440:Mild-mannered Pate
    event_m10_14_x4(z182=114010120, z183=114020121, z184=104170, z185=10144200, z186=111252, npc1=7440)

def event_m10_14_111254():
    """OBJ: Patch: Death determination"""
    """State 0,1: Wandering & Patch: Death Determination_SubState"""
    event_m10_14_x119(z69=104173, z70=65, z71=102445, z72=102402)

def event_m10_14_111255():
    """OBJ: Patch & Wanderer: Win / Lose Judgment"""
    """State 0,13: Win / Lose Judgment: Event End Judgment"""
    CompareEventStatus(8, 111235, 1, 0)
    CompareEventStatus(8, 111256, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(8):
        """State 15: Win / Loss Judgment: Player Escape Judgment"""
        CompareEventFlag(8, 104170, 1)
        CompareEventFlag(8, 114000114, 1)
        CompareEventFlag(8, 114000124, 1)
        if ConditionGroup(8):
            """State 7: Win / Lose Judgment: Patch Death: Branch"""
            Label('L0')
            CompareEventFlag(0, 114020127, 1)
            if ConditionGroup(0):
                """State 3: Win / Loss Judgment: Wandering: Supportive: Patch Dead"""
                SetEventFlag(114000141, 1)
            else:
                """State 4: Win / Lose Judgment: Wandering: No support: Patch death"""
                SetEventFlag(114000142, 1)
        else:
            """State 11: Win / Loss Judgment: Death Judgment"""
            CompareEventFlag(0, 104151, 1)
            CompareEventFlag(1, 104171, 1)
            CompareEventFlag(2, 104172, 1)
            CompareEventFlag(3, 104173, 1)
            CompareEventFlag(4, 104152, 1)
            CompareEventFlag(4, 104153, 1)
            if ConditionGroup(0):
                Goto('L1')
            elif ConditionGroup(1):
                Goto('L1')
            elif ConditionGroup(2):
                Goto('L1')
            elif ConditionGroup(3):
                Goto('L1')
            elif ConditionGroup(4):
                Goto('L1')
            else:
                """State 16: Victory / Loss Judgment: Wandering and Player Death"""
                CompareEventFlag(8, 104150, 1)
                CompareEventFlag(8, 114000141, 0)
                CompareEventFlag(8, 114000142, 0)
                CompareEventFlag(8, 114000143, 0)
                CompareEventFlag(8, 114000144, 0)
                if ConditionGroup(8):
                    pass
                else:
                    """State 17: Win / Loss Judgment: When a patch and player die"""
                    CompareEventFlag(8, 104170, 1)
                    CompareEventFlag(8, 114000141, 0)
                    CompareEventFlag(8, 114000142, 0)
                    CompareEventFlag(8, 114000143, 0)
                    CompareEventFlag(8, 114000144, 0)
                    if ConditionGroup(8):
                        Goto('L0')
                    else:
                        """State 14: Win / Loss Judgment: Emigration Judgment"""
                        CompareEventFlag(0, 114000118, 0)
                        CompareEventFlag(1, 114000128, 0)
                        if ConditionGroup(0):
                            Goto('L1')
                        elif ConditionGroup(1):
                            Goto('L1')
                        else:
                            """State 12: Win / Loss Judgment: Player Intrusion Judgment"""
                            IsPlayerInsidePoint(0, 10000000, 10000000, 1)
                            assert ConditionGroup(0)
                            """State 2: Win / Loss Judgment: Encounter Setting"""
                            SetEventFlag(114000114, 1)
                            SetEventFlag(114000124, 1)
                            CompareEventFlag(8, 114000114, 1)
                            CompareEventFlag(8, 114000124, 1)
                            assert ConditionGroup(8)
                            """State 1: Win / Lose Judgment: Final Judgment"""
                            IsChrDead(0, 55)
                            IsChrDead(1, 65)
                            if ConditionGroup(0):
                                pass
                            elif ConditionGroup(1):
                                Goto('L0')
                """State 8: Win / Lose Judgment: Wandering Death: Branch"""
                CompareEventFlag(0, 114020117, 1)
                if ConditionGroup(0):
                    """State 5: Win / Lose Judgment: Patch: With Support: Wandering Death"""
                    SetEventFlag(114000143, 1)
                else:
                    """State 6: Win / Lose Judgment: Patch: No support: Wandering death"""
                    SetEventFlag(114000144, 1)
        """State 10: Win / Loss Judgment: Battle Event: End"""
        SetEventFlag(114000140, 1)
    """State 9: Win / Lose Judgment: System: End"""
    Label('L1')
    EndMachine()

def event_m10_14_111256():
    """OBJ: Patch: Appearance determination"""
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, 104151, 1)
        CompareEventFlag(1, 104152, 1)
        CompareEventFlag(2, 104170, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(2):
            pass
        else:
            """State 9: Appearance determination: Patch victory determination"""
            CompareEventFlag(8, 114000140, 1)
            CompareEventFlag(8, 114000143, 1)
            CompareEventFlag(9, 114000140, 1)
            CompareEventFlag(9, 114000144, 1)
            if ConditionGroup(8):
                pass
            elif ConditionGroup(9):
                pass
            else:
                """State 7: Appearance determination: Draw determination"""
                CompareEventFlag(8, 114000140, 1)
                CompareEventFlag(8, 114000114, 1)
                CompareEventFlag(8, 114000124, 1)
                if ConditionGroup(8):
                    """State 8: Appearance determination: draw setting"""
                    SetEventFlag(104170, 1)
                    CompareEventFlag(0, 104170, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 3: Appearance Judgment: Wandering & Patch: Emigration Judgment"""
                    CompareEventFlag(8, 102406, 1)
                    CompareEventFlag(8, 103652, 0)
                    CompareEventFlag(8, 102451, 1)
                    CompareEventFlag(8, 103672, 0)
                    if ConditionGroup(8):
                        pass
                    else:
                        Goto('L0')
            """State 4: Appearance determination: Appearable"""
            SetEventFlag(114000128, 1)
            CompareEventFlag(0, 114000128, 1)
            assert ConditionGroup(0)
            Goto('L1')
        """State 5: Appearance judgment: Impossible to appear"""
        Label('L0')
        SetEventFlag(114000128, 0)
        CompareEventFlag(0, 114000128, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L1')
    EndMachine()

def event_m10_14_111332():
    """OBJ: Wandering Warrior (Patch Death): Grave"""
    """State 0: Start state"""
    assert EventEnded(111232) != 0
    """State 2: Grave generation judgment"""
    CompareEventFlag(0, 104153, 1)
    if ConditionGroup(0):
        """State 1: System: Exit"""
        EndMachine()
    else:
        """State 3: [Lib] NPC: Grave Placement: General Purpose_SubState"""
        event_m10_14_x1(z187=104154, z188=10144300, z189=58, z190=7420)

def event_m10_14_111333():
    """OBJ: Wandering Warrior (Patch Death): Key Guide"""
    """State 0,1: Death map flag judgment"""
    CompareEventFlag(0, 104154, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_14_x4(z182=114010109, z183=114020111, z184=104150, z185=10144300, z186=111332, npc1=7420)

def event_m10_14_111334():
    """OBJ: Wandering Warrior (Patch Death): Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_14_x7(z173=57, z174=104154)

def event_m10_14_111335():
    """OBJ: Wandering Warrior (Patch Death): Appearance Judgment"""
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, 111235, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(8):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, 104150, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 8: Appearance determination: Migration determination"""
            CompareEventFlag(8, 102406, 1)
            CompareEventFlag(8, 103652, 0)
            if ConditionGroup(8):
                """State 7: Appearance determination: Battle event determination"""
                CompareEventFlag(0, 114000140, 1)
                if ConditionGroup(0):
                    pass
                else:
                    """State 3: Appearance determination: Patch: Death determination"""
                    CompareEventFlag(0, 104171, 1)
                    CompareEventFlag(1, 104172, 1)
                    if ConditionGroup(0):
                        """State 4: Appearance determination: Appearable"""
                        Label('L0')
                        SetEventFlag(114000119, 1)
                        CompareEventFlag(0, 114000119, 1)
                        assert ConditionGroup(0)
                        Goto('L1')
                    elif ConditionGroup(1):
                        Goto('L0')
                    else:
                        pass
            else:
                pass
        """State 5: Appearance judgment: Impossible to appear"""
        SetEventFlag(114000119, 0)
        CompareEventFlag(0, 114000119, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L1')
    EndMachine()

def event_m10_14_111435():
    """OBJ: Sealed Person: Black Phantom Sign Display"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_14_x29(z143=102810, z144=10001000, z145=521, z146=104340, z147=0, z148=2)

def event_m10_14_111452():
    """OBJ: Upper weapon shop: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_14_x1(z187=104362, z188=10144100, z189=266, z190=7760)

def event_m10_14_111453():
    """OBJ: Upper weapon shop: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7760:Weaponsmith Ornifex
    event_m10_14_x4(z182=114010130, z183=114020131, z184=104360, z185=10144100, z186=111452, npc1=7760)

def event_m10_14_111454():
    """OBJ: Upper weapon shop: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_14_x7(z173=265, z174=104362)

def event_m10_14_111482():
    """NPC: Immoral Teacher: Grave"""
    """State 0,1: NPC: Immoral Teacher: Grave Placement_SubState"""
    event_m10_14_x1(z187=104390, z188=10144000, z189=311, z190=7840)

def event_m10_14_111483():
    """NPC: Immoral Teacher: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7840:Cromwell the Pardoner
    event_m10_14_x4(z182=114010100, z183=114020101, z184=104390, z185=10144000, z186=111482, npc1=7840)

def event_m10_14_111484():
    """NPC: Immoral Teacher: Shop List"""
    """State 0,1: Shop list: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    else:
        """State 3: Shop list: Fire lap: Judgment"""
        # bonfire:14655:Royal Army Campsite
        CompareGameCycleForBonfire(0, 14655, 1, 2, 3)
        if ConditionGroup(0):
            """State 4: Shop list: Fire lap: Flag setting"""
            SetEventFlag(102404, 1)
            CompareEventFlag(0, 102404, 1)
            assert ConditionGroup(0)
        else:
            pass
    """State 2: Shop list: System: End"""
    EndMachine()

def event_m10_14_118100():
    """Multi NPC: Test 1_ Boss Long Distance: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_14_x23(z155=528)

def event_m10_14_118110():
    """Multi-use NPC: Test 2_ Tavern: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_14_x23(z155=529)

def event_m10_14_118120():
    """Multi-use NPC: Leroy: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_14_x23(z155=527)

def event_m10_14_118210():
    """Multi NPC: Dark Spirit Test: Black Phantom Appearance"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_14_x30(z139=10002000, z140=520, z141=0, z142=2)

def event_m10_14_3000000():
    """[DLC] Shop lineup expansion_Demon Knight Kai"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m10_14_x43(z126=101063, z127=101213)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4000000():
    """[BEST] Appearance of Andyel"""
    """State 0,3: [Lib] [BEST] [Preset] Ander_Termination_SubState"""
    call = event_m10_14_x50(z116=10141810, z117=100740, z118=100741, z119=100760, z120=100461, z121=100300,
                            z122=100360, z123=100400)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_4001000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_14_x63(z114=10141810, z115=10141800)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_4002000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_14_x55(z124=10141810, z125=10141800)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_4003000():
    """[BEST] Anderu Navimesh switching"""
    """State 0,3: [Lib] [BEST] [Preset] Anderu's navigation mesh switching_SubState"""
    call = event_m10_14_x68(z112=10141810, z113=6003000)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_14_4010000():
    """[DC] Lighthouse lighting management_01"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140700, z5=114020180)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010010():
    """[DC] Lighthouse lighting management_02"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140701, z5=114020181)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010020():
    """[DC] Lighthouse lighting management_03"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140702, z5=114020182)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010030():
    """[DC] Lighthouse lighting management_04"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140703, z5=114020183)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010040():
    """[DC] Lighthouse lighting management_05"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140704, z5=114020184)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010050():
    """[DC] Lighthouse lighting management_06"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140705, z5=114020185)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010060():
    """[DC] Lighthouse lighting management_07"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140706, z5=114020186)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4010080():
    """[DC] Lighthouse lighting management_09"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140708, z5=114020188)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011000():
    """[DC] Thorn damage switch for peasant_1"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5251, z3=200014060)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011010():
    """[DC] Thorn damage switching of peasant deceased_2"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5252, z3=200014060)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011020():
    """[DC] Thorn damage switching of peasant deceased_3"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5253, z3=200014060)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011030():
    """[DC] Thorn damage switching of farmer deceased_4"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5254, z3=200014060)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011500():
    """[DC] Farmer deceased locked lock_1"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5251)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011510():
    """[DC] Unlockable management of peasant deceased_2"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5252)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011520():
    """[DC] Farmer deceased locked lock_3"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5253)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4011530():
    """[DC] Farmer deceased locked lock_4"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5254)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4012000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_14_x72(z97=114020001, z98=14, z99=114000002, z100=4, z101=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m10_14_x77(z105=80000000, z106=0, z107=5, z108=926, val1=1, z109=10, z110=80000001,
                z111=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m10_14_x77(z105=80000100, z106=0, z107=5, z108=926, val1=2, z109=10, z110=80000101,
                z111=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m10_14_x77(z105=80000200, z106=0, z107=5, z108=926, val1=3, z109=10, z110=80000201,
                z111=80000299))
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert (event_m10_14_x77(z105=80000300, z106=0, z107=5, z108=926, val1=4, z109=10, z110=80000301,
                z111=80000399))
        """State 2: Start flag ON"""
        SetEventFlag(114020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4012010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_14_x80(z102=114000002, z103=926, mode1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4013000():
    """[DC] Treasure corpse 7"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141506, z56=10146480)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4013010():
    """[DC] Treasure corpse 8"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141507, z56=10146490)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4013020():
    """[DC] Treasure corpse 9"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141508, z56=10146510)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4013030():
    """[DC] Treasure corpse 10"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z55=10141509, z56=10146520)
    """State 1: Finish"""
    EndMachine()

def event_m10_14_4031000():
    """[DC] NPC White Spirit_Gesture Management_The Queen"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_14_x85(z94=114000081, z95=803, z96=114020079)
    """State 1: Finish"""
    EndMachine()

