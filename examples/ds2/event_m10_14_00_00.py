# -*- coding: utf-8 -*-
def event_m10_14_1000():
    """End_Boss HP setting"""
    """State 0,3: [Preset] Boss HP Setting_SubState"""
    assert event_m10_14_x97(z81=100000)
    """State 2: [BEST] Disabling warmth fire"""
    SetDamageImmunityByGeneratorId(803, 33200000, 1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_2000():
    """Outpost Battle_Queen Generation Judgment"""
    """State 0,2: [Preset] Prelude Battle_Queen Generation Judgment_SubState"""
    assert event_m10_14_x161(z36=114000081, z37=114000083, z38=114020084)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_2010():
    """Preliminary battle_Time limit setting"""
    """State 0,2: Has the generation determination event ended?"""
    assert EventEnded(2000) != 0
    """State 3: [Preset] Preliminary Battle_Time Limit_SubState"""
    assert event_m10_14_x145(flag6=114020084, z47=1000, z48=114000081)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_2020():
    """Preliminary Battle_Preservation and withdrawal of Queen's HP"""
    """State 0,3: Has the generation determination been completed?"""
    assert EventEnded(2000) != 0
    """State 4: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_SubState"""
    call = event_m10_14_x100(z33=95, z34=1000, z35=114000085)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 5: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_2_SubState"""
        call = event_m10_14_x100(z33=90, z34=1000, z35=114000086)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 6: [Preset] Preliminary battle with boss _HP save and withdrawal_3_SubState"""
            call = event_m10_14_x100(z33=85, z34=1000, z35=114000087)
            if call.Get() == 1:
                pass
            elif call.Done():
                """State 7: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_4_SubState"""
                call = event_m10_14_x100(z33=80, z34=1000, z35=114000088)
                if call.Get() == 1:
                    pass
                elif call.Done():
                    """State 8: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_5_SubState"""
                    call = event_m10_14_x100(z33=75, z34=1000, z35=114000089)
                    if call.Get() == 1:
                        pass
                    elif call.Done():
                        """State 9: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_6_SubState"""
                        call = event_m10_14_x100(z33=70, z34=1000, z35=114000090)
                        if call.Get() == 1:
                            pass
                        elif call.Done():
                            """State 10: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_7_SubState"""
                            call = event_m10_14_x100(z33=65, z34=1000, z35=114000091)
                            if call.Get() == 1:
                                pass
                            elif call.Done():
                                """State 11: [Preset] Preliminary battle with boss _HP save and withdrawal_8_SubState"""
                                call = event_m10_14_x100(z33=60, z34=1000, z35=114000092)
                                if call.Get() == 1:
                                    pass
                                elif call.Done():
                                    """State 12: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_9_SubState"""
                                    call = event_m10_14_x100(z33=55, z34=1000, z35=114000093)
                                    if call.Get() == 1:
                                        pass
                                    elif call.Done():
                                        """State 13: [Preset] Preliminary Battle with Boss_HP Save and Withdrawal_10_SubState"""
                                        call = event_m10_14_x100(z33=50, z34=1000, z35=114000094)
                                        if call.Get() == 1:
                                            pass
                                        elif call.Get() == 0:
                                            """State 2: Withdrawal flag ON"""
                                            SetEventFlag(114000083, 1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_2040():
    """Outpost battle_deletion after withdrawal"""
    """State 0,2: Has the generation determination been completed?"""
    assert EventEnded(2000) != 0
    """State 3: [Preset] Delete after withdrawal_SubState"""
    assert event_m10_14_x113(z31=1000, z32=204000, flag4=114020084)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_2050():
    """Outpost Battle_Boss HP Gauge Display"""
    """State 0,2: Has the generation determination been completed?"""
    assert EventEnded(2000) != 0
    """State 3: [Preset] Outpost Battle_Boss HP Gauge Display_SubState"""
    assert event_m10_14_x165(flag3=114000081, z23=1014001, z24=1000, z25=114020084, z26=114000083)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_3000():
    """Pile destruction in front of rocks"""
    """State 0,2: [Preset] Rock destruction by sub pile_SubState"""
    assert event_m10_14_x89(z83=10143030, z84=10143000, z85=70, z86=300030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_3010():
    """Rock destruction by pile destruction_back"""
    """State 0,2: [Preset] Rock destruction by sub pile_SubState"""
    assert event_m10_14_x89(z83=10143035, z84=10143005, z85=80, z86=301000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4000():
    """Boss: Battle of the Queen"""
    """State 0,2: Is the poly drama event finished?"""
    assert EventEnded(4010) != 0
    """State 3: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_14_x8(flag20=114000081, z148=400000, z149=400000, z150=101, z151=1014000, z152=114020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010():
    """Boss"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m10_14_x18(z143=10140602, z144=101410, flag19=114000082, z145=401000, z146=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4020():
    """Boss: Spider Queen 1"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z9=8010, z10=114000081, z11=120, z12=114020040)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4021():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 2"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z9=8011, z10=114000081, z11=120, z12=114020041)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4022():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 3"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z9=8012, z10=114000081, z11=120, z12=114020042)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4023():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 4"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z9=8013, z10=114000081, z11=120, z12=114020043)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4024():
    """Boss: Spider Queen"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z9=8014, z10=114000081, z11=120, z12=114020044)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4025():
    """Boss: Queen of Akatsuki _ Zakokoku Generation 6"""
    """State 0,2: [Preset] Boss: The Queen of Akatsuki_Zakokoku Generation_SubState"""
    assert event_m10_14_x183(z9=8015, z10=114000081, z11=120, z12=114020045)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_5000():
    """Treasure chest appears when you pull the switch"""
    """State 0,2: [Preset] Treasure chest appears when switch is pulled_SubState"""
    assert event_m10_14_x164(z27=10143101, z28=10145120, z29=500000, z30=10143100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_6000():
    """Sand door"""
    """State 0,3: [Preset] Sand Door_SubState"""
    # action:1102:"Too heavy to open"
    call = event_m10_14_x105(z69=10140400, z70=10141020, z71=50, z72=20, z73=20, z74=600000, action1=1102)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_7000():
    """Boss: Zakobos_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_14_x8(flag20=114000096, z148=700000, z149=700000, z150=102, z151=1014010, z152=114020095,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_8000():
    """Bug door"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_14_x5(z158=1005, z159=1105, z160=50830000, z161=114000010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_8002():
    """Insect key door_3"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_14_x5(z158=1005, z159=1105, z160=50830000, z161=114000014)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_9000():
    """Warp to the memory of the ancient dragon"""
    """State 0,3: [Preset] Inter-map warp_SubState by checking OBJ"""
    call = event_m10_14_x106(z57=10141700, z58=101420, z59=0, z60=20260000, z61=900000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_9010():
    """Red soul and Complicated display"""
    """State 0,3: [Preset] Red Soul and Complicated Display _SubState"""
    call = event_m10_14_x124(z6=10141705, z7=2004, flag1=100460, z8=100951)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_10000():
    """The key door that opens with "Patch House Key" """
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_14_x5(z158=1005, z159=1105, z160=50930000, z161=114000060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_11010():
    """Insect lock door_Spider start_Front"""
    """State 0,2: [Preset] Insect Lock Door_Spider Launch_SubState"""
    assert event_m10_14_x117(z66=10140412, z67=1101000, z68=114020072)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_12000():
    """One door open from the beginning"""
    """State 0,2: Make one door open"""
    ChangeObjState(10140471, 74)
    assert CompareObjStateId(10140471, 30, 0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_13000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_14_x19(z138=10142500, z139=20, z140=1300000, z141=0, z142=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_14000():
    """Door that opens with a wall lever_Left"""
    """State 0,2: [Preset] Door opened with wall lever_SubState"""
    assert event_m10_14_x129(z52=10141401, z53=10141400, z54=1400000, z55=20, z56=10)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_14010():
    """Door that opens with a wall lever_Right"""
    """State 0,2: [Preset] Door opened with wall lever_SubState"""
    assert event_m10_14_x129(z52=10141406, z53=10141405, z54=1401000, z55=20, z56=10)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_15000():
    """Treasure corpse 1"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141500, z50=10146230)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_15010():
    """Treasure corpse 2"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141501, z50=10146300)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_15020():
    """Treasure corpse 3"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141502, z50=10146310)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_15030():
    """Treasure corpse 4"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141503, z50=10146320)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_15040():
    """Treasure corpse 5"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141504, z50=10146010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_15050():
    """Treasure corpse 6"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141505, z50=10146330)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_16000():
    """Treasure corpse falls due to tower destruction"""
    """State 0,2: [Preset] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_14_x149(z44=10141550, z45=10146290, z46=70)
    """State 1: Finish"""
    Quit()

def event_m10_14_17000():
    """Navimesh change due to yagura destruction 1"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x150(z41=10141550, z42=1700000, z43=1700001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_17010():
    """Navimesh change due to yagura destruction 2"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x150(z41=10141555, z42=1701000, z43=1701001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_17020():
    """Navimesh change due to yagura destruction 3"""
    """State 0,2: [Preset] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x150(z41=10141545, z42=1702000, z43=1702001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_20020():
    """One-way door 03 (dust chute room)"""
    """State 0,2: [Lib] Area specified door unlocking_2_SubState"""
    assert event_m10_14_x6(z155=0, z156=2002000, z157=114000020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_21000():
    """Alarm treasure chest"""
    """State 0,2: [Preset] Alarm treasure chest _ Start _ SubState"""
    assert event_m10_14_x137(z51=10145060, flag7=114000070)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_22000():
    """Termination Bonfire_Pyroxene"""
    """State 0,2: [Lib] [Preset] End special bonfire_SubState"""
    assert event_m10_14_x36(z115=10141800, flag18=100461)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_14_23000():
    """Pig eats mushrooms_pig 1"""
    """State 0,3: [Preset] Pig eats mushrooms_SubState"""
    call = event_m10_14_x179(flag2=114000052, z13=10141590, z14=10146500, z15=2300000, z16=10, z17=1120)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_23010():
    """Pig eats mushrooms_pig 2"""
    """State 0,3: [Preset] Pig eats mushrooms_SubState"""
    call = event_m10_14_x179(flag2=114000052, z13=10141590, z14=10146500, z15=2300000, z16=10, z17=1121)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_23020():
    """Pig eats mushrooms"""
    """State 0,3: [Preset] Pig eats mushrooms_SubState"""
    call = event_m10_14_x179(flag2=114000052, z13=10141590, z14=10146500, z15=2300000, z16=10, z17=1122)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_24000():
    """Probability of piglets"""
    """State 0,2: [Preset] Appearance of piglets with probability _SubState"""
    assert event_m10_14_x154(z39=114020050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_25000():
    """Interlocking destruction due to scaffold destruction"""
    """State 0,2: [Preset] Linkage destruction due to scaffold destruction_SubState"""
    assert event_m10_14_x172(z19=10141180, z20=2500000, z21=2500001, z22=10141170)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_25010():
    """Navi mesh change of scaffolding that breaks when riding"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_14_x19(z138=10141170, z139=20, z140=2501000, z141=2, z142=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_80000():
    """Rebirth fire 01_A building next to ant hell"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_14_x27(z135=1014000, z136=1014099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_80010():
    """Shop lineup expansion"""
    """State 0,2: [Lib] [Preset] Shop Lineup_SubState"""
    # bonfire:14650:Lower Brightstone Cove
    assert event_m10_14_x41(bonfire1=14650, z113=114000081, flag16=101100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_81000():
    """Rebirth Fire 02_Map entrance tent"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_14_x27(z135=1014100, z136=1014199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_82000():
    """Rebirth Fire 03_Cave after Church"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_14_x27(z135=1014200, z136=1014299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_90000():
    """Trophy_Pyroxene Light"""
    """State 0,2: [Lib] [Preset] Get Trophy_Global_SubState"""
    assert event_m10_14_x37(flag17=100461, z114=9)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_x0(z58=_, z59=0, z60=_, z61=_):
    """[Lib] Warp between maps after poly play
    z58: Pre-warp poly play ID
    z59: Poly Play ID after Warp
    z60: Map ID
    z61: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z58, z59, z60, z61, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_14_x1(z167=_, z168=_, z169=_, z170=_):
    """[Lib] NPC: Grave Placement: General purpose
    z167: Death map: Global event flag
    z168: Tomb: OBJ instance ID
    z169: Tomb move to: Generator ID
    z170: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z167, 1)
    IsGraveGeneratable(8, z170, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z168, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z168, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_14_x2(z164=_, z165=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z164: Global: death flag
    z165: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z165, 10, 0)
    CompareObjState(1, z165, 20, 0)
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
    IsObjSearched(0, z165)
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

def event_m10_14_x3(z162=_, z163=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z162: Area other flags: Ghost appearance
    z163: Area other flags: Conversation start
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
    SetEventFlag(z162, 1)
    CompareEventFlag(0, z162, 1)
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
    SetEventFlag(z163, 1)
    CompareEventFlag(0, z163, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_14_x4(z162=_, z163=_, z164=_, z165=_, z166=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z162: Ghost Appearance: Area Other Flag
    z163: Conversation start: Area and other flags
    z164: Death: Global event flag
    z165: Tomb: OBJ instance ID
    z166: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z166, 1, 0)
    CompareEventFlag(9, z162, 1)
    CompareObjState(9, z165, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z163, 1)
        CompareEventFlag(0, z163, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_14_x2(z164=z164, z165=z165, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_14_x3(z162=z162, z163=z163, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_14_x5(z158=1005, z159=1105, z160=_, z161=_):
    """[Lib] Item specified door unlocking_2
    z158: Text ID when opened
    z159: Text ID when not opened
    z160: item
    z161: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z160, z158, z159, z161, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x6(z155=0, z156=2002000, z157=114000020):
    """[Lib] Area specified door unlocking_2
    z155: Text ID when opened
    z156: Point ID
    z157: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z156, 0, z155, 1101, z157, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x7(z153=_, z154=_):
    """[Lib] NPC: Death determination: General purpose
    z153: Generator ID
    z154: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z154, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z153)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z154, 1)
            CompareEventFlag(0, z154, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_14_x8(flag20=_, z148=_, z149=_, z150=_, z151=_, z152=_, mode2=0):
    """[Lib] [Preset] Boss Battle Start
    flag20: Boss destruction flag
    z148: Start point ID
    z149: End point ID
    z150: Sound ID
    z151: Boss Battle ID
    z152: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_14_x9(flag20=flag20)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_14_x10(z148=z148, z149=z149)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_14_x11(z150=z150, z151=z151, z152=z152)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_14_x12()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_14_x13(z151=z151)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_14_x14(z150=z150, z151=z151, z152=z152, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_14_x9(flag20=_):
    """[Reproduction] Boss Battle_Start
    flag20: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag20) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_14_x10(z148=_, z149=_):
    """[Condition] Boss Battle_Start
    z148: Start point ID
    z149: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z148, z149, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z148, z149, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x11(z150=_, z151=_, z152=_):
    """[Execution] Boss Battle_Start
    z150: Sound ID
    z151: Boss Battle ID
    z152: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z150)
    """State 1: Boss battle start notification"""
    StartBossFight(z151)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z152, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x12():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x13(z151=_):
    """[Condition] Boss Battle_End Judgment
    z151: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z151, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x14(z150=_, z151=_, z152=_, mode2=0):
    """[Execute] Boss Battle_End
    z150: Sound ID
    z151: Boss Battle ID
    z152: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z152, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z151)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z150)
    """State 5: End state"""
    return 0

def event_m10_14_x15(flag19=114000082):
    """[Reproduction] Boss Battle_Poly Play Replay
    flag19: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(flag19) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_14_x16(z143=10140602):
    """[Condition] Boss Battle_Poly Play Replay
    z143: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z143, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x17(z144=101410, flag19=114000082, z145=401000, z147=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z144: Poly play ID
    flag19: Poly drama played flag
    z145: Warp point ID
    z147: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z144, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(flag19, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z145)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_14_x18(z143=10140602, z144=101410, flag19=114000082, z145=401000, z146=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z143: White door instance ID
    z144: Poly play ID
    flag19: Poly drama played flag
    z145: Warp point ID
    z146: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m10_14_x15(flag19=flag19)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m10_14_x16(z143=z143)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m10_14_x17(z144=z144, flag19=flag19, z145=z145, z147=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_14_x19(z138=_, z139=20, z140=_, z141=_, z142=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z138: Object instance ID
    z139: OBJ state ID
    z140: Navimesh switching point ID
    z141: Additional attributes
    z142: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_14_x20(z138=z138, z139=z139, z140=z140, z142=z142, z141=z141)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_14_x21(z138=z138, z139=z139, z140=z140)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_14_x22(z138=z138, z139=z139, z140=z140, z141=z141, z142=z142)
    """State 4: End state"""
    return 0

def event_m10_14_x20(z138=_, z139=20, z140=_, z142=_, z141=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z138: Target OBJ instance ID
    z139: Target OBJ state ID
    z140: Navimesh switching point ID
    z142: Additional attributes
    z141: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z138, z139, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z140, z142)
        DeleteNavimeshAttribute(z140, z141)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_14_x21(z138=_, z139=20, z140=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z138: Target OBJ instance ID
    z139: Target OBJ state ID
    z140: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z138, z139, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x22(z138=_, z139=20, z140=_, z141=_, z142=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z138: Target OBJ instance ID
    z139: Target OBJ state ID
    z140: Navimesh switching point ID
    z141: Additional attributes
    z142: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z140, z141)
    DeleteNavimeshAttribute(z140, z142)
    """State 2: End state"""
    return 0

def event_m10_14_x23(z137=_):
    """[DC] [execution] Lighthouse lighting management
    z137: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z137)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_14_x24():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x25(z135=_, z136=_):
    """[Lib] [execute] Rebirth fire
    z135: Flag start ID
    z136: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z135, z136, 0)
    """State 2: End state"""
    return 0

def event_m10_14_x26():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x27(z135=_, z136=_):
    """[Lib] [Preset] Rebirth
    z135: Flag start ID
    z136: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_14_x24()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_14_x26()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_14_x25(z135=z135, z136=z136)
    """State 4: End state"""
    return 0

def event_m10_14_x28(z131=114000096, z132=102436, z133=205, z134=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z131: Defeat Boss 1: Area and other flags
    z132: Summon Achievement: Global Event Flag
    z133: Summon achievement count: global variable
    z134: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z132, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z131, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z133, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z133, NpcInfoValue(z134, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z132, 1)
                CompareEventFlag(0, z132, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_14_x29(z125=102810, z126=10001000, z127=521, z128=104340, z129=0, z130=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z125: Summoning conditions: Global event flag
    z126: Summon range
    z127: Generator ID
    z128: Death: Global event flag
    z129: Appearance: Minimum time
    z130: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z128, 1)
        CompareEventFlag(8, z125, 1)
        IsPlayerInsidePoint(8, z126, z126, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z128, 1)
            CompareStateTime(1, z129, 3, z130)
            IsPlayerInsidePoint(2, z126, z126, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z127)
                HasNpcPhantomSpawned(0, z127, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_14_x30(z121=10002000, z122=520, z123=0, z124=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z121: Summon range
    z122: Generator ID
    z123: Appearance: Minimum time
    z124: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z121, z121, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z123, 3, z124)
        IsPlayerInsidePoint(1, z121, z121, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z122)
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

def event_m10_14_x31(z116=102430, z117=526, z118=104160, z119=103660, z120=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z116: White Phantom can appear: Global event flag
    z117: White Phantom: Generator ID
    z118: Death: Global event flag
    z119: Hostile: Global event flag
    z120: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z117)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z118, 1)
        CompareEventFlag(1, z119, 1)
        CompareEventFlag(2, z116, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z117)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z118, 1)
            CompareEventFlag(1, z119, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z117)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z118, 1)
            CompareEventFlag(1, z119, 1)
            HasNpcPhantomSpawned(2, z117, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z117, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z117)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_14_x32(flag18=100461):
    """[Lib] [Reproduction] Special bonfire at the end
    flag18: Lighting completion flag
    """
    """State 0,1: Is the bonfire already lit?"""
    if GetEventFlag(flag18) != 0:
        """State 3: Already lit"""
        return 1
    else:
        """State 2: Unlit"""
        return 0

def event_m10_14_x33(z115=10141800):
    """[Lib] [Condition] Terminal special fire
    z115: Bonfire OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z115)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x34(z115=10141800, flag18=100461):
    """[Lib] [Execution] End special bonfire_ignition
    z115: Bonfire OBJ instance ID
    flag18: Lighting completion flag
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
        ChangeObjState(z115, 70)
        """State 3: Lighting completion flag ON"""
        SetEventFlag(flag18, 1)
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

def event_m10_14_x35(z115=10141800, flag18=100461):
    """[Lib] [Execution] End special bonfire_warp
    z115: Bonfire OBJ instance ID
    flag18: Lighting completion flag
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
        assert event_m10_14_x0(z58=0, z59=0, z60=10040000, z61=200000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m10_14_x36(z115=10141800, flag18=100461):
    """[Lib] [Preset] Special bonfire at the end
    z115: Bonfire OBJ instance ID
    flag18: Lighting completion flag
    """
    """State 0,1: [Lib] [Reproduction] End special bonfire _SubState"""
    call = event_m10_14_x32(flag18=flag18)
    if call.Get() == 1:
        """State 5: [Lib] [Condition] End special bonfire_2_SubState"""
        assert event_m10_14_x33(z115=z115)
        """State 2: [Lib] [Execution] End special bonfire_warp_SubState"""
        assert event_m10_14_x35(z115=z115, flag18=flag18)
    elif call.Get() == 0:
        """State 4: [Lib] [Condition] End special bonfire_SubState"""
        assert event_m10_14_x33(z115=z115)
        """State 3: [Lib] [Execution] End special bonfire_At ignition_SubState"""
        assert event_m10_14_x34(z115=z115, flag18=flag18)
    """State 6: Rerun"""
    return 0

def event_m10_14_x37(flag17=100461, z114=9):
    """[Lib] [Preset] Trophy Acquisition_Global
    flag17: Acquisition trigger_global flag
    z114: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag17) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag17, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z114)
    """State 4: End state"""
    return 0

def event_m10_14_x38(flag15=_):
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

def event_m10_14_x39(bonfire1=14650, z113=114000081):
    """[Lib] [Conditions] Shop lineup
    bonfire1: Bonfire ID
    z113: Boss destruction flag
    """
    """State 0,1: Is the total number of laps 2 or more and is the boss destroyed?"""
    # bonfire:14650:Lower Brightstone Cove
    CompareGameCycleForBonfire(8, bonfire1, 2, 2, 3)
    CompareEventFlag(8, z113, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_14_x40(flag15=_):
    """[Lib] [execution] shop lineup
    flag15: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(flag15, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x41(bonfire1=14650, z113=114000081, flag16=101100):
    """[Lib] [Preset] Shop Lineup
    bonfire1: Bonfire ID
    z113: Boss destruction flag
    flag16: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_14_x38(flag15=flag16)
    if call.Get() == 0:
        """State 3: [Lib] [Conditions] Shop lineup_SubState"""
        assert event_m10_14_x39(bonfire1=bonfire1, z113=z113)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_14_x40(flag15=flag16)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_14_x42(z112=101063):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z112: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z112, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x43(z112=101063, flag15=101213):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z112: Boss destruction flag
    flag15: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m10_14_x38(flag15=flag15)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m10_14_x42(z112=z112)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m10_14_x40(flag15=flag15)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_14_x44(z105=10141810):
    """[Lib] [BEST] [Condition] Andyel_Appearance_Termination
    z105: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z105)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x45(z105=10141810, flag14=100760, flag13=100741):
    """[Lib] [BEST] [Execution] Andyel_Appearance_Termination
    z105: Ander OBJ instance ID
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
        ChangeObjState(z105, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z105, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(flag14, 1)
        """State 7: End state"""
        return 0

def event_m10_14_x46(flag12=100740):
    """[Lib] [BEST] [Conditions] Ander_Destruction_End_Termination
    flag12: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, flag12, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x47(z105=10141810):
    """[Lib] [BEST] [Execution] Andel_Deletion_End
    z105: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z105, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z105, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_14_x48(z105=10141810, flag12=100740, flag14=100760, flag13=100741):
    """[Lib] [BEST] [Reproduction] Anderl_Appearance determination_Termination
    z105: Ander OBJ instance ID
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
                if CompareObjStateId(z105, 72, 0):
                    pass
                elif CompareObjStateId(z105, 73, 0):
                    pass
                elif CompareObjStateId(z105, 70, 0):
                    pass
                elif CompareObjStateId(z105, 30, 0):
                    pass
                else:
                    """State 7: Was the appearance confirmed?"""
                    if GetEventFlag(flag13) != 0:
                        """State 8: Standby state: 30"""
                        ChangeObjState(z105, 30)
                    else:
                        """State 11: Appearance determination"""
                        return 2
                """State 5: Wait for completion"""
                assert CompareObjStateId(z105, 30, 0)
                """State 6: Conversation start flag ON"""
                SetEventFlag(flag14, 1)
            """State 10: Disappearance judgment"""
            return 1
    """State 9: Finish"""
    return 0

def event_m10_14_x49():
    """[Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x50(z105=10141810, flag12=100740, flag13=100741, flag14=100760, z106=100461, z107=100300,
                     z108=100360, z109=100400):
    """[Lib] [BEST] [Preset] Andyel_Termination
    z105: Ander OBJ instance ID
    flag12: Event completion flag
    flag13: Encounter flag
    flag14: Conversation start flag
    z106: Lighting completion flag
    z107: Bonfire lighting judgment flag ①
    z108: Bonfire lighting judgment flag ②
    z109: Bonfire lighting judgment flag ③
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Ander _ Appearance determination _ Termination _ SubState"""
    call = event_m10_14_x48(z105=z105, flag12=flag12, flag14=flag14, flag13=flag13)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation judgment _ terminal _ empty _ SubState"""
        Label('L0')
        assert event_m10_14_x49()
        """State 9: [Lib] [BEST] [Conditions] Ander_Deletion_Termination_Termination_SubState"""
        assert event_m10_14_x46(flag12=flag12)
        """State 6: [Lib] [BEST] [Execution] Andel_Destruction_End_SubState"""
        assert event_m10_14_x47(z105=z105)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Ander_Appearance determination_Termination_SubState"""
        call = event_m10_14_x57(z105=z105, z106=z106, z107=z107, z108=z108, z109=z109, flag13=flag13)
        if call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Andel_Appearance determination_Termination_SubState"""
            assert event_m10_14_x58(z105=z105)
            """State 1: [Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty_SubState"""
            assert event_m10_14_x56()
            """State 7: [Lib] [BEST] [Condition] Ander_Appearance_Termination_SubState"""
            assert event_m10_14_x44(z105=z105)
            """State 4: [Lib] [BEST] [Execution] Andel_Appearance_Termination_SubState"""
            call = event_m10_14_x45(z105=z105, flag14=flag14, flag13=flag13)
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

def event_m10_14_x51(z110=10141810, z111=10141800):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z110: Ander OBJ instance ID
    z111: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z110, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z111, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_14_x52(z110=10141810):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z110: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z110, 10, 0)
    CompareObjState(0, z110, 31, 0)
    CompareObjState(0, z110, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m10_14_x53(z110=10141810, z111=10141800):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z110: Ander OBJ instance ID
    z111: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z111, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z110, 10, 1)
    CompareObjState(8, z110, 31, 1)
    CompareObjState(8, z110, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_14_x54(z110=10141810, z111=10141800):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z110: Ander OBJ instance ID
    z111: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z111, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z110, 10, 0)
    CompareObjState(0, z110, 31, 0)
    CompareObjState(0, z110, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_14_x55(z110=10141810, z111=10141800):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z110: Ander OBJ instance ID
    z111: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m10_14_x51(z110=z110, z111=z111)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m10_14_x52(z110=z110)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m10_14_x53(z110=z110, z111=z111)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m10_14_x54(z110=z110, z111=z111)
    """State 6: Rerun"""
    return 1

def event_m10_14_x56():
    """[Lib] [BEST] [Reproduction] Ander_Appearance_Termination_Empty"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x57(z105=10141810, z106=100461, z107=100300, z108=100360, z109=100400, flag13=100741):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_Termination
    z105: Ander OBJ instance ID
    z106: Lighting completion flag
    z107: Bonfire lighting judgment flag ①
    z108: Bonfire lighting judgment flag ②
    z109: Bonfire lighting judgment flag ③
    flag13: Andyur encounter flag
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z106, 0)
    CompareEventFlag(8, z107, 1)
    CompareEventFlag(8, z108, 1)
    CompareEventFlag(8, z109, 1)
    CompareEventFlag(8, flag13, 0)
    CompareEventFlag(0, flag13, 1)
    if ConditionGroup(8):
        """State 2: End state"""
        return 0
    elif ConditionGroup(0):
        """State 3: Rerun"""
        return 1

def event_m10_14_x58(z105=10141810):
    """[Lib] [BEST] [Execution] Andel_Appearance determination_Termination
    z105: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z105, 31)
    """State 2: End state"""
    return 0

def event_m10_14_x59(z103=10141810, z104=10141800):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z103: Ander OBJ instance ID
    z104: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z103, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z104, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m10_14_x60(z103=10141810):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z103: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z103, 10, 0)
    CompareObjState(0, z103, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m10_14_x61(z103=10141810, z104=10141800):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z103: Ander OBJ instance ID
    z104: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z104, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z103, 10, 1)
    CompareObjState(8, z103, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m10_14_x62(z103=10141810, z104=10141800):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z103: Ander OBJ instance ID
    z104: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z104, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z103, 10, 0)
    CompareObjState(0, z103, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m10_14_x63(z103=10141810, z104=10141800):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z103: Ander OBJ instance ID
    z104: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m10_14_x59(z103=z103, z104=z104)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m10_14_x60(z103=z103)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m10_14_x61(z103=z103, z104=z104)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m10_14_x62(z103=z103, z104=z104)
    """State 5: Rerun"""
    return 0

def event_m10_14_x64(z101=10141810):
    """[Lib] [BEST] [Conditions] Switching the Andy navig mesh
    z101: Ander OBJ instance ID
    """
    """State 0,1: Judgment of under deal status"""
    CompareObjState(0, z101, 10, 0)
    CompareObjState(0, z101, 31, 0)
    CompareObjState(0, z101, 20, 0)
    if ConditionGroup(0):
        """State 2: I'm stuck"""
        return 0
    else:
        """State 3: Appearing"""
        return 1

def event_m10_14_x65(z101=10141810, z102=6003000):
    """[Lib] [BEST] [Execution] Anderu's navigation mesh switching_passable
    z101: Ander OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,2: Navimesh switching: Allowed to pass"""
    DeleteNavimeshAttribute(z102, 2)
    """State 1: Next judgment"""
    CompareObjState(8, z101, 10, 1)
    CompareObjState(8, z101, 31, 1)
    CompareObjState(8, z101, 20, 1)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_14_x66(z101=10141810, z102=6003000):
    """[Lib] [BEST] [Execution] Anderu navigesh mesh switching_No traffic
    z101: Ander OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,2: Navi mesh switching: no traffic"""
    AddNavimeshAttribute(z102, 2)
    """State 1: Next judgment"""
    CompareObjState(0, z101, 10, 0)
    CompareObjState(0, z101, 31, 0)
    CompareObjState(0, z101, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_14_x67(z101=10141810, z102=6003000):
    """[Lib] [BEST] [Reproduction] Switching the Andy navig mesh
    z101: Ander OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,1: Is the Andyal finished?"""
    if CompareObjStateId(z101, 20, 0):
        """State 2: Navimesh switching: Allowed to pass"""
        DeleteNavimeshAttribute(z102, 2)
        """State 4: Finished"""
        return 1
    else:
        """State 3: Waiting"""
        return 0

def event_m10_14_x68(z101=10141810, z102=6003000):
    """[Lib] [BEST] [Preset] Anderu navigator mesh switching_
    z101: Ander OBJ instance ID
    z102: Navigation change point ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Anderu's navigation mesh switching _SubState"""
    call = event_m10_14_x67(z101=z101, z102=z102)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Conditions] Switching the Andy's Navimesh_SubState"""
    Label('L0')
    call = event_m10_14_x64(z101=z101)
    if call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Switching the Andy's Navigation Mesh_Passable_SubState"""
        assert event_m10_14_x65(z101=z101, z102=z102)
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Navigation mesh switching of the deal _ Traffic prohibited _SubState"""
        assert event_m10_14_x66(z101=z101, z102=z102)
    """State 5: Rerun"""
    return 0

def event_m10_14_x69(flag9=114020001, flag10=114000002):
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

def event_m10_14_x70(z89=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z89: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z89, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_14_x71(flag9=114020001, z90=4, z91=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag9: Lottery determination flag
    z90: Number of appearance judgment points
    z91: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag9, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z90)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z91, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_14_x72(flag9=114020001, z89=14, flag10=114000002, z90=4, z91=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag9: Lottery determination flag
    z89: Random number comparison value
    flag10: Defeat flag
    z90: Number of appearance judgment points
    z91: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_14_x69(flag9=flag9, flag10=flag10)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_14_x70(z89=z89)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_14_x71(flag9=flag9, z90=z90, z91=z91)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_14_x81(flag9=flag9, z91=z91)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_14_x73(val1=_, z98=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z98: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z98) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_14_x74(z94=_, z95=0, z96=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z94: Appearance judgment point ID
    z95: Minimum appearance time
    z96: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z94, z94, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z95, 3, z96)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_14_x75(z97=926, z99=_, z100=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z97: Generator ID
    z99: Appearance start point ID
    z100: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z97, z99, z100)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z97)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m10_14_x76(flag11=114000002):
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

def event_m10_14_x77(z94=_, z95=0, z96=5, z97=926, val1=_, z98=10, z99=_, z100=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z94: Intrusion detection point ID
    z95: Minimum appearance time
    z96: Maximum time to appear
    z97: Generator ID
    val1: Appearance judgment number
    z98: Lottery result point variable
    z99: Appearance start point ID
    z100: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_14_x73(val1=val1, z98=z98)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_14_x74(z94=z94, z95=z95, z96=z96)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_14_x75(z97=z97, z99=z99, z100=z100)
    """State 4: Finish"""
    return 0

def event_m10_14_x78(z92=926, mode1=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z92: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z92)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_14_x79(flag11=114000002, z93=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag11: Defeat flag
    z93: Weapon flag
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
                    SetEventFlag(z93, 1)
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

def event_m10_14_x80(flag11=114000002, z92=926, mode1=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag11: Defeat flag
    z92: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_14_x76(flag11=flag11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_14_x78(z92=z92, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_14_x79(flag11=flag11, z93=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_14_x79(flag11=flag11, z93=102755)
    """State 5: End state"""
    return 0

def event_m10_14_x81(flag9=114020001, z91=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag9: Lottery determination flag
    z91: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag9, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z91, 0)
    """State 3: End state"""
    return 0

def event_m10_14_x82(flag8=114000081):
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

def event_m10_14_x83(z87=803):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z87: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z87, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x84(z88=114020079):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z88: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z88, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x85(flag8=114000081, z87=803, z88=114020079):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag8: Boss destruction flag
    z87: Boss generator ID
    z88: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_14_x82(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_14_x83(z87=z87)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_14_x84(z88=z88)
    """State 4: End state"""
    return 0

def event_m10_14_x86(z84=_, z86=_):
    """[Reproduction] Reproduction of rocky rocky state
    z84: Rock instance ID
    z86: Point ID for Navimesh change
    """
    """State 0,1: State determination of rock OBJ"""
    if CompareObjStateId(z84, 10, 1):
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z86, 2)
        """State 5: Executed"""
        return 1
    else:
        """State 3: Navimesh attribute added"""
        AddNavimeshAttribute(z86, 2)
        """State 4: Not executed"""
        return 0

def event_m10_14_x87(z83=_):
    """[Conditions] Pile failure judgment
    z83: Pile instance ID
    """
    """State 0,1: Group condition: Pile breaking standby"""
    CompareObjState(0, z83, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x88(z84=_, z85=_, z86=_):
    """[Execution] Iwa Gorogoro
    z84: Rock instance ID
    z85: Rolling state ID
    z86: Point ID for Navimesh change
    """
    """State 0,2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z86, 2)
    """State 1: OBJ State Transition: Rock Gorogoro"""
    ChangeObjState(z84, z85)
    assert CompareObjStateId(z84, 20, 0)
    """State 3: End state"""
    return 0

def event_m10_14_x89(z83=_, z84=_, z85=_, z86=_):
    """[Preset] Pile destruction and rocks
    z83: Pile instance ID
    z84: Rock instance ID
    z85: Rolling state ID
    z86: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Rock rocking state reproduction_SubState"""
    call = event_m10_14_x86(z84=z84, z86=z86)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Pile failure judgment_SubState"""
        assert event_m10_14_x87(z83=z83)
        """State 3: [Execution] Iwa Gorogoro_SubState"""
        assert event_m10_14_x88(z84=z84, z85=z85, z86=z86)
    """State 4: End state"""
    return 0

def event_m10_14_x90(z27=10143101, z28=10145120, z29=500000, z30=10143100):
    """[Reproduction] Treasure chest appears when you pull the switch
    z27: Scaffolding OBJ instance ID
    z28: Treasure chest OBJ instance ID
    z29: Point ID for Navimesh change
    z30: Switch OBJ instance ID
    """
    """State 0,1: Attach a treasure chest to the scaffold"""
    AttachObjToObj(z27, 150, z28)
    """State 2,3: Scaffold OBJ status determination"""
    if CompareObjStateId(z27, 20, 0):
        """State 5: Disable key guide for switch"""
        DisableObjKeyGuide(z30, 1)
        """State 4,7: Already in operation"""
        return 1
    else:
        """State 6: Not in operation"""
        return 0

def event_m10_14_x91(z30=10143100):
    """[Condition] Treasure chest appears when switch is pulled
    z30: Switch OBJ instance ID
    """
    """State 0,1: Switch operation standby"""
    CompareObjState(0, z30, 74, 0)
    CompareObjState(0, z30, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x92(z27=10143101, z29=500000, z30=10143100):
    """[Execution] Treasure chest appears when switch is pulled
    z27: Scaffolding OBJ instance ID
    z29: Point ID for Navimesh change
    z30: Switch OBJ instance ID
    """
    """State 0,4: Disable key guide for switch"""
    DisableObjKeyGuide(z30, 1)
    """State 1: Scaffold animation playback descending with a switch"""
    ChangeObjState(z27, 70)
    """State 3: Has the animation of the scaffold finished playing?"""
    CompareObjState(0, z27, 20, 0)
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

def event_m10_14_x95(z81=100000):
    """[Condition] HP setting of boss_Termination
    z81: Point ID
    """
    """State 0,1: Did you enter the point before the boss?"""
    IsPlayerInsidePoint(8, z81, z81, 1)
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

def event_m10_14_x96(z82=_):
    """[Execution] HP setting of boss
    z82: HP ratio to be set
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Boss HP settings"""
        SetHpRatioFromGenerator(803, z82)
    else:
        pass
    """State 3: End state"""
    return 0

def event_m10_14_x97(z81=100000):
    """[Preset] Boss HP Setting_Termination
    z81: HP set point ID
    """
    """State 0,1: [Reproduction] HP setting of boss_SubState"""
    call = event_m10_14_x94()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] HP setting of boss_SubState"""
        call = event_m10_14_x95(z81=z81)
        if call.Get() == 0:
            """State 3: [Execution] HP setting of boss_SubState"""
            assert event_m10_14_x96(z82=95)
        elif call.Get() == 1:
            """State 4: [Execution] HP setting of boss_2_SubState"""
            assert event_m10_14_x96(z82=90)
        elif call.Get() == 2:
            """State 5: [Execute] HP setting of boss_3_SubState"""
            assert event_m10_14_x96(z82=85)
        elif call.Get() == 3:
            """State 6: [Execute] HP setting of boss_4_SubState"""
            assert event_m10_14_x96(z82=80)
        elif call.Get() == 4:
            """State 7: [Execute] HP setting of boss_5_SubState"""
            assert event_m10_14_x96(z82=75)
        elif call.Get() == 5:
            """State 8: [Execution] HP setting of boss_6_SubState"""
            assert event_m10_14_x96(z82=70)
        elif call.Get() == 6:
            """State 9: [Execute] HP setting of boss_7_SubState"""
            assert event_m10_14_x96(z82=65)
        elif call.Get() == 7:
            """State 10: [Execution] HP setting of boss_8_SubState"""
            assert event_m10_14_x96(z82=60)
        elif call.Get() == 8:
            """State 11: [Execution] HP setting of boss_9_SubState"""
            assert event_m10_14_x96(z82=55)
        elif call.Get() == 9:
            """State 12: [Execute] HP setting of boss_10_SubState"""
            assert event_m10_14_x96(z82=50)
        elif call.Get() == 10:
            pass
    """State 13: End state"""
    return 0

def event_m10_14_x98(z33=_, z34=1000, z78=202000, z79=202001, z80=30):
    """[Condition] Preliminary Battle with Boss
    z33: HP reduction rate (%)
    z34: Enemy generator ID
    z78: Start point ID
    z79: End point ID
    z80: Time limit
    """
    """State 0,2: Generating the start battle boss and canceling the activation state"""
    CompareChrStartUpState(8, z34, 2, 1)
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
    CompareChrHpRatio(1, z34, z33, 5)
    IsPlayerInsidePoint(8, z78, z79, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    CompareAreaTimer(0, 0, z80, 3)
    if ConditionGroup(0):
        """State 4: Boss withdrawal"""
        return 1
    elif ConditionGroup(1):
        """State 3: Save HP reduction"""
        return 0

def event_m10_14_x99(z35=_):
    """[Execution] Preliminary Battle with Boss_Save HP
    z35: HP save flag
    """
    """State 0,1: HP save flag ON"""
    SetEventFlag(z35, 1)
    """State 2: A large number of transition prevention empty states"""
    assert (GetStateTime() > 0.1) != 0
    """State 3: End state"""
    return 0

def event_m10_14_x100(z33=_, z34=1000, z35=_):
    """[Preset] Preliminary Battle with Boss
    z33: HP reduction rate (%)
    z34: Enemy generator ID
    z35: HP save flag
    """
    """State 0,4: [Reproduction] Preliminary battle with boss _HP save and withdrawal_SubState"""
    call = event_m10_14_x162(flag5=114020084)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] Preliminary Battle with Boss_HP Save and Withdrawal_SubState"""
        call = event_m10_14_x98(z33=z33, z34=z34, z78=202000, z79=202001, z80=30)
        if call.Get() == 2:
            pass
        elif call.Get() == 1:
            """State 3: [Execution] Preliminary Battle with Boss_Withdrawal_SubState"""
            assert event_m10_14_x93()
        elif call.Get() == 0:
            """State 2: [Execution] Preliminary Battle with Boss_HP Save_SubState"""
            assert event_m10_14_x99(z35=z35)
            """State 5: End state"""
            return 0
    """State 6: Withdrawal and destruction completed"""
    return 1

def event_m10_14_x101(z69=10140400, z76=50, z77=20, z74=600000):
    """[Reproduction] Sand door
    z69: OBJ instance ID of the sand door
    z76: OBJ state ID being destroyed
    z77: OBJ state ID after destruction
    z74: Navigation change point ID
    """
    """State 0,1: Has the sand door been destroyed?"""
    if CompareOwnObjStateId(z76, 0):
        """State 2: Navigation mesh change"""
        Label('L0')
        DeleteNavimeshAttribute(z74, 2)
        """State 3: Destroyed"""
        return 0
    elif CompareOwnObjStateId(z77, 0):
        Goto('L0')
    else:
        """State 4: Not destroyed"""
        return 1

def event_m10_14_x102(z69=10140400):
    """[Condition] Sand door
    z69: OBJ instance ID of the sand door
    """
    """State 0,1: PC behavior judgment"""
    IsObjSearched(0, z69)
    IsObjBroken(1, z69, 1)
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

def event_m10_14_x104(z69=10140400, z70=10141020, z75=20, z74=600000):
    """[Execution] Sand door_Sand display
    z69: OBJ instance ID of the sand door
    z70: OBJ instance ID of the ground
    z75: Ground display OBJ state ID
    z74: Navigation change point ID
    """
    """State 0,1: Ground OBJ display"""
    ChangeObjState(z70, z75)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z74, 2)
    """State 3: End state"""
    return 0

def event_m10_14_x105(z69=10140400, z70=10141020, z71=50, z72=20, z73=20, z74=600000, action1=1102):
    """[Preset] Sand door
    z69: OBJ instance ID of the sand door
    z70: OBJ instance ID of the ground
    z71: OBJ State ID during destruction of the sand door
    z72: OBJ State ID after destruction of the sand door
    z73: Ground display OBJ state ID
    z74: Navigation change point ID
    action1: Dialog text ID
    """
    """State 0,1: [Reproduction] Sand door_SubState"""
    call = event_m10_14_x101(z69=z69, z76=50, z77=20, z74=z74)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Condition] Sand door_SubState"""
        call = event_m10_14_x102(z69=z69)
        if call.Get() == 0:
            """State 2: [Execute] Sand door_Display dialog_SubState"""
            assert event_m10_14_x103(action1=action1)
            """State 5: Dialog display"""
            return 0
        elif call.Get() == 1:
            """State 3: [Execution] Sand door_Sand display_SubState"""
            assert event_m10_14_x104(z69=z69, z70=z70, z75=20, z74=z74)
    """State 6: Destroyed"""
    return 1

def event_m10_14_x106(z57=10141700, z58=101420, z59=0, z60=20260000, z61=900000):
    """[Preset] Check OBJ and warp between maps
    z57: OBJ instance ID to check
    z58: Pre-warp poly play ID
    z59: Poly Play ID after Warp
    z60: Map ID
    z61: Point ID
    """
    """State 0,1: [Reproduction] OBJ is examined and warp between maps_SubState"""
    call = event_m10_14_x107(z57=z57)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Inter-map warp_SubState by checking OBJ"""
        call = event_m10_14_x108(z57=z57)
        if call.Get() == 0:
            """State 3: [Execution] Inter-map warp_warp execution_SubState by checking OBJ"""
            assert event_m10_14_x109(z57=z57, z58=z58, z59=z59, z60=z60, z61=z61)
            Goto('L0')
        elif call.Get() == 1:
            """State 4: [Execution] Check OBJ, warp between maps_Key guide invalidation only_SubState"""
            assert event_m10_14_x110(z57=z57)
        elif call.Get() == 2:
            """State 5: [Execution] Giant's memory intrusion_Nothing happens_SubState"""
            assert event_m10_14_x120()
        """State 7: Rerun"""
        return 1
    """State 6: Finish"""
    Label('L0')
    return 0

def event_m10_14_x107(z57=10141700):
    """[Net] Duel matching cancellation
    z57: OBJ instance ID to check
    """
    """State 0,2: Did you get the Old Dragon Soul?"""
    if GetEventFlag(100460) != 0:
        """State 3: Display of crystal OBJ: 30"""
        ChangeObjState(z57, 30)
        """State 1: Disable key guide"""
        DisableObjKeyGuide(z57, 1)
        """State 4: End state"""
        return 0
    else:
        """State 5: Old dragon not acquired in Seoul"""
        return 1

def event_m10_14_x108(z57=10141700):
    """[Condition] Check OBJ and warp between maps
    z57: OBJ instance ID to check
    """
    """State 0,1: Single play and queen defeated?"""
    IsMultiplayer(8, 0, 1)
    CompareEventFlag(8, 114000081, 1)
    assert ConditionGroup(8)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z57, 0)
    """State 2: Was OBJ checked or multi?"""
    IsObjSearched(0, z57)
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

def event_m10_14_x109(z57=10141700, z58=101420, z59=0, z60=20260000, z61=900000):
    """[Execution] Inter-map warp_warp execution after checking OBJ
    z57: OBJ instance ID to check
    z58: Pre-warp poly play ID
    z59: Poly Play ID after Warp
    z60: Map ID
    z61: Point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z57, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_14_x0(z58=z58, z59=z59, z60=z60, z61=z61)
    """State 4: End state"""
    return 0

def event_m10_14_x110(z57=10141700):
    """[Execution] Checking OBJ and only warping between maps_key guide invalidation
    z57: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z57, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x111(z31=1000, z32=204000):
    """[Condition] Deletion after withdrawal
    z31: Enemy generator ID
    z32: Deletion point ID
    """
    """State 0,1: Has the withdrawn character entered the withdrawal point? Or did you destroy it?"""
    IsChrInsidePoint(8, z31, z32, z32, 1)
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

def event_m10_14_x112(z31=1000):
    """[Execution] Deletion after withdrawal
    z31: Enemy generator ID
    """
    """State 0,1: Enemy deleted"""
    PauseEnemy(z31, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x113(z31=1000, z32=204000, flag4=114020084):
    """[Preset] Deletion after withdrawal
    z31: Enemy generator ID
    z32: Deletion point ID
    flag4: Generation determination flag
    """
    """State 0,3: [Reproduction] Delete after withdrawal_SubState"""
    call = event_m10_14_x163(flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Delete after withdrawal_SubState"""
        call = event_m10_14_x111(z31=z31, z32=z32)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Delete after withdrawal_SubState"""
            assert event_m10_14_x112(z31=z31)
    """State 4: End state"""
    return 0

def event_m10_14_x114(z66=10140412):
    """[Reproduction] Insect key door _ Spider activation
    z66: Door instance ID
    """
    """State 0,1: Is the door unlocked?"""
    if CompareObjStateId(z66, 30, 0):
        """State 3: Unlocked"""
        return 1
    else:
        """State 2: Unlocked"""
        return 0

def event_m10_14_x115(z66=10140412):
    """[Conditions] Bug lock door_Spider activation: Unlocking judgment
    z66: Door instance ID
    """
    """State 0,1: Did you open the door?"""
    CompareObjState(0, z66, 10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x116(z68=114020072):
    """[Execution] Bug lock door_Spider start
    z68: Startup flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z68, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x117(z66=10140412, z67=1101000, z68=114020072):
    """[Preset] Insect Lock Door_Spider Launch
    z66: Door instance ID
    z67: Point ID
    z68: Startup flag
    """
    """State 0,1: [Reproduction] Bug's key door_Spider start_SubState"""
    call = event_m10_14_x114(z66=z66)
    if call.Get() == 0:
        """State 2: [Condition] Insect key door_Spider activation: Unlocking determination_SubState"""
        assert event_m10_14_x115(z66=z66)
    elif call.Get() == 1:
        """State 3: [Condition] Bug's key door_Spider start: Point judgment_SubState"""
        assert event_m10_14_x118(z67=z67)
    """State 4: [Execution] Bug's key door_Spider start_SubState"""
    assert event_m10_14_x116(z68=z68)
    """State 5: End state"""
    return 0

def event_m10_14_x118(z67=1101000):
    """[Condition] Insect lock door_Spider activation: Point judgment
    z67: Point ID
    """
    """State 0,1: Entered the specified area?"""
    IsPlayerInsidePoint(0, z67, z67, 1)
    IsPlayerInsidePoint(0, 1102000, 1102000, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x119(z62=_, z63=_, z64=_, z65=_):
    """Wandering & Patch: Death Determination
    z62: Death: Global event flag
    z63: Generator ID
    z64: For encounter: Global event flag
    z65: For opponent encounter: Global event flag
    """
    """State 0,1: Death determination: Start"""
    CompareEventStatus(8, 111255, 1, 0)
    CompareEventFlag(0, z64, 1)
    CompareEventFlag(0, z64, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 2: Death determination: Death determination"""
        CompareEventFlag(0, z62, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Death determination: Wait"""
            IsChrDead(0, z63)
            IsPlayerInTheMap(1, 0, 0)
            if ConditionGroup(0):
                """State 4: Death determination: death flag setting"""
                SetEventFlag(z62, 1)
                CompareEventFlag(0, z62, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(1):
                pass
    """State 5: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_14_x120():
    """[Execution] Giant's memory intrusion_Nothing happens"""
    """State 0,1: Message display"""
    # action:1113:"Alas, nothing happened"
    DisplayOwnOkMenu(1113, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m10_14_x121(flag1=100460):
    """[Reproduction] Red Soul and Complicated Display
    flag1: Old Dragon's Soul Acquisition Flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Has an old dragon acquired Seoul?"""
    if GetEventFlag(flag1) != 1:
        """State 3: Waiting for display"""
        return 0
    else:
        """State 5: End: Hide"""
        return 2
    """State 4: Guest user"""
    Label('L0')
    return 1

def event_m10_14_x122(z8=100951):
    """[Condition] Red Soul and Complicated Display
    z8: Defeated queen flag
    """
    """State 0,1: Did you destroy the queen of nieces?"""
    CompareEventFlag(0, z8, 1)
    assert ConditionGroup(0)
    """State 2: Red soul display"""
    return 0

def event_m10_14_x123(z6=10141705, z7=2004, flag1=100460):
    """[Execution] Red Soul and Complicated Display _Acquisition and Complicated Display
    z6: Damipoli OBJ instance ID
    z7: Text ID
    flag1: Old Dragon's Soul Acquisition Flag
    """
    """State 0,2: Display of haze: 32"""
    ChangeObjState(z6, 32)
    """State 1: Old Dragon Soul Acquisition Flag ON"""
    SetEventFlag(flag1, 1)
    """State 3: Production FE display"""
    OpenPresentationWindow(22)
    assert PresentationWindowDisplay() != 0
    """State 4: End state"""
    return 0

def event_m10_14_x124(z6=10141705, z7=2004, flag1=100460, z8=100951):
    """[Preset] Red Soul and Complicated Display
    z6: Damipoli OBJ instance ID
    z7: Text ID
    flag1: Old Dragon's Soul Acquisition Flag
    z8: Defeated queen flag
    """
    """State 0,1: [Reproduction] Red Soul and Complicated Display _SubState"""
    call = event_m10_14_x121(flag1=flag1)
    if call.Get() == 0:
        """State 4: [Condition] Red Soul and Complicated Display _Defeat Judgment_SubState"""
        assert event_m10_14_x122(z8=z8) == 0
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
            assert event_m10_14_x123(z6=z6, z7=z7, flag1=flag1)
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

def event_m10_14_x129(z52=_, z53=_, z54=_, z55=20, z56=10):
    """[Preset] Door that opens with a wall lever
    z52: Lever OBJ instance ID
    z53: Door OBJ instance ID
    z54: Point ID for Navimesh change
    z55: Door OBJ open state ID
    z56: Initial state of door OBJ
    """
    """State 0,1: [Reproduction] Door opened with wall lever _SubState"""
    call = event_m10_14_x130(z53=z53, z55=z55, z56=z56)
    if call.Get() == 0:
        """State 2: [Condition] Door that opens with a wall lever_SubState"""
        assert event_m10_14_x131(z52=z52)
        """State 3: [Execution] Door opened with a wall lever_Unopened_SubState"""
        assert event_m10_14_x132(z53=z53, z54=z54, z55=z55, z52=z52)
    elif call.Get() == 1:
        """State 4: [Execution] Door opened with a wall lever_Opened_SubState"""
        assert event_m10_14_x133(z54=z54, z52=z52, z53=z53)
    """State 5: End state"""
    return 0

def event_m10_14_x130(z53=_, z55=20, z56=10):
    """[Reproduction] Door that opens with wall lever
    z53: Door OBJ instance ID
    z55: Door OBJ open state ID
    z56: Initial state of door OBJ
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z53, z56, 1):
        """State 3: Opened"""
        return 1
    else:
        """State 2: Not open"""
        return 0

def event_m10_14_x131(z52=_):
    """[Conditions] Door opened with wall lever
    z52: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z52, 74, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x132(z53=_, z54=_, z55=20, z52=_):
    """[Execution] Door opened with a wall lever_not open
    z53: Door OBJ instance ID
    z54: Point ID for Navimesh change
    z55: Door OBJ open state ID
    z52: Lever OBJ instance ID
    """
    """State 0,1: Door that opens with lever"""
    ChangeObjState(z53, 70)
    assert CompareObjStateId(z53, z55, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z54, 2)
    """State 3: Disable key guide of lever"""
    DisableObjKeyGuide(z52, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x133(z54=_, z52=_, z53=_):
    """[Execution] Door that opens with wall lever_Opened
    z54: Point ID for Navimesh change
    z52: Lever OBJ instance ID
    z53: Door OBJ instance ID
    """
    """State 0,3: Waiting for the door to open"""
    assert CompareObjStateId(z53, 20, 0)
    """State 1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z54, 2)
    """State 2: Disable key guide of lever"""
    DisableObjKeyGuide(z52, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x134(flag7=114000070):
    """[Reproduction] Alarm treasure chest
    flag7: Spider start flag
    """
    """State 0,1: Has the trap been activated?"""
    if GetEventFlag(flag7) != 0:
        """State 3: Trap executed"""
        return 1
    else:
        """State 2: Trap not executed"""
        return 0

def event_m10_14_x135(z51=10145060):
    """[Condition] Alarm treasure chest
    z51: OBJ instance ID of treasure chest
    """
    """State 0,1: Did the treasure box be confirmed or broken?"""
    CompareObjState(0, z51, 75, 0)
    CompareObjState(0, z51, 100, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x136(flag7=114000070):
    """[Execute] Alarm treasure chest
    flag7: Spider start flag
    """
    """State 0,1: Spider start flag ON"""
    SetEventFlag(flag7, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x137(z51=10145060, flag7=114000070):
    """[Preset] Alarm treasure chest
    z51: OBJ instance ID of treasure chest
    flag7: Spider start flag
    """
    """State 0,1: [Reproduction] Alarm treasure chest _ Start _ SubState"""
    call = event_m10_14_x134(flag7=flag7)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Alarm treasure chest"""
        assert event_m10_14_x135(z51=z51)
        """State 2: [Execution] Alarm treasure chest _ Start _ SubState"""
        assert event_m10_14_x136(flag7=flag7)
    """State 4: End state"""
    return 0

def event_m10_14_x138(z49=_, z50=_):
    """[Preset] Treasure corpse
    z49: 壺 OBJ instance ID
    z50: Instance ID of treasure corpse OBJ
    """
    """State 0,1: [Reproduction] Treasure corpse _SubState"""
    call = event_m10_14_x139(z49=z49, z50=z50)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] If you break the trap, the treasure corpse_SubState"""
        assert event_m10_14_x140(z49=z49)
        """State 3: [Execution] If you break the trap, the treasure corpse_SubState"""
        assert event_m10_14_x141(z50=z50)
    """State 4: End state"""
    return 0

def event_m10_14_x139(z49=_, z50=_):
    """[Reproduction] Treasure corpse
    z49: 壺 OBJ instance ID
    z50: Instance ID of treasure corpse OBJ
    """
    """State 0,1: 判定 Judgment of OBJ status"""
    if CompareObjStateId(z49, 20, 0):
        """State 2: Anime execution of treasure corpse OBJ"""
        ChangeObjState(z50, 73)
        """State 5: 壺: Destroyed"""
        return 1
    else:
        """State 3: Hidden body hidden"""
        ChangeDrawHit(z50, 0)
        """State 4: 壺: Undestructed"""
        return 0

def event_m10_14_x140(z49=_):
    """[Condition] If you break a spear,
    z49: 壺 OBJ instance ID
    """
    """State 0,1: Did you destroy 壺 OBJ?"""
    CompareObjState(0, z49, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x141(z50=_):
    """[Execution] Treasure corpse
    z50: Instance ID of treasure corpse OBJ
    """
    """State 0,2: Treasure corpse display"""
    ChangeDrawHit(z50, 1)
    """State 1: Anime execution of treasure corpse OBJ"""
    ChangeObjState(z50, 73)
    """State 3: End state"""
    return 0

def event_m10_14_x142(flag6=114020084):
    """[Reproduction] Preliminary battle _ time limit setting
    flag6: Pre-battle boss generation determination flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Queen generation flag determination"""
        if GetEventFlag(flag6) != 1:
            pass
        else:
            """State 3: Not destroyed or withdrawn"""
            return 0
    """State 4: Simple end"""
    return 1

def event_m10_14_x143(flag6=114020084, z47=1000, z48=114000081):
    """[Condition] Preliminary Battle_Time limit setting
    flag6: Front boss boss generation flag
    z47: Generator ID
    z48: Defeat flag
    """
    """State 0,1: Generation of start battle boss & activation state release or destruction flag ON"""
    CompareChrStartUpState(8, z47, 2, 1)
    CompareEventFlag(8, flag6, 1)
    CompareEventFlag(0, z48, 1)
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

def event_m10_14_x145(flag6=114020084, z47=1000, z48=114000081):
    """[Preset] Preliminary Battle_Time limit setting
    flag6: Outpost Battle Boss Generation Flag
    z47: Generator ID
    z48: Defeat flag
    """
    """State 0,1: [Reproduction] Preliminary Battle_Time Limit_SubState"""
    call = event_m10_14_x142(flag6=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Front battle_Time limit setting_SubState"""
        call = event_m10_14_x143(flag6=flag6, z47=z47, z48=z48)
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

def event_m10_14_x147(z45=10146290, z46=70):
    """[Execution] Treasure corpse falls due to yagura destruction
    z45: Instance ID of treasure corpse
    z46: Falling state ID
    """
    """State 0,1: Treasure corpse fall"""
    ChangeObjState(z45, z46)
    """State 2: End state"""
    return 0

def event_m10_14_x148(z44=10141550):
    """[Condition] Treasure corpse falls due to yagura destruction
    z44: Yagura instance ID
    """
    """State 0,1: Waiting for destruction of the tower"""
    IsObjBroken(0, z44, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x149(z44=10141550, z45=10146290, z46=70):
    """[Preset] Treasure corpse falls due to yagura destruction
    z44: Yagura instance ID
    z45: Instance ID of treasure corpse
    z46: Falling state ID
    """
    """State 0,1: [Reproduction] Treasure corpse fall due to yagura destruction_Sky_SubState"""
    assert event_m10_14_x146()
    """State 2: [Condition] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_14_x148(z44=z44)
    """State 3: [Execution] Treasure corpse fall due to yagura destruction_SubState"""
    assert event_m10_14_x147(z45=z45, z46=z46)
    """State 4: End state"""
    return 0

def event_m10_14_x150(z41=_, z42=_, z43=_):
    """[Preset] Navimesh change due to yagura destruction
    z41: YAGURA OBJ instance ID
    z42: Point ID for changing Navimesh at the top of the tower
    z43: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: [Reproduction] Navi mesh change due to yagura destruction_SubState"""
    call = event_m10_14_x151(z41=z41)
    if call.Get() == 0:
        """State 2: [Condition] Navi mesh change due to yagura destruction_SubState"""
        assert event_m10_14_x152(z41=z41)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Navi mesh change due to yagura destruction_SubState"""
    assert event_m10_14_x153(z42=z42, z43=z43)
    """State 4: End state"""
    return 0

def event_m10_14_x151(z41=_):
    """[Reproduction] Navi mesh change due to yagura destruction
    z41: YAGURA OBJ instance ID
    """
    """State 0,1: State determination of yagura OBJ"""
    if CompareObjStateId(z41, 20, 1):
        """State 2: Undestructed"""
        return 0
    else:
        """State 3: Destroyed"""
        return 1

def event_m10_14_x152(z41=_):
    """[Condition] Navi mesh change due to yagura destruction
    z41: YAGURA OBJ instance ID
    """
    """State 0,1: Yagura OBJ transition waiting"""
    CompareObjState(0, z41, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x153(z42=_, z43=_):
    """[Execution] Navi mesh change due to yagura destruction
    z42: Point ID for changing Navimesh at the top of the tower
    z43: Point ID for navigating mesh change at the bottom of the tower
    """
    """State 0,1: Added navigating mesh attributes at the top of the tower"""
    AddNavimeshAttribute(z42, 2)
    """State 2: Navimesh attribute deletion at the bottom of the tower"""
    DeleteNavimeshAttribute(z43, 2)
    """State 3: End state"""
    return 0

def event_m10_14_x154(z39=114020050):
    """[Preset] Probability of piglet appearance
    z39: Piglet generation flag
    """
    """State 0,1: [Reproduction] Appearance of piglets with probability _SubState"""
    assert event_m10_14_x155()
    """State 2: [Condition] Appearance of piglet with probability_SubState"""
    call = event_m10_14_x156()
    if call.Get() == 0:
        """State 3: [Execution] Probability of piglet appearance"""
        assert event_m10_14_x157(z39=z39, z40=1)
    elif call.Get() == 1:
        """State 4: [Execution] Appearance of piglet with probability_No piglet appearance_SubState"""
        assert event_m10_14_x157(z39=z39, z40=0)
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

def event_m10_14_x157(z39=114020050, z40=_):
    """[Execution] Appearance of piglets with probability
    z39: Piglet generation flag
    z40: ON / OFF of piglet generation flag
    """
    """State 0,1: Change the flag state based on the random number result"""
    SetEventFlag(z39, z40)
    """State 2: End state"""
    return 0

def event_m10_14_x158(z36=114000081, z37=114000083):
    """[Conditions] Prelude Battle_Queen Generation Judgment
    z36: Boss destruction flag
    z37: Withdrawal flag
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
    CompareEventFlag(0, z36, 1)
    if ConditionGroup(0):
        pass
    else:
        Goto('L1')
    """State 5: Boss killed"""
    return 1
    """State 2: Has it been withdrawn?"""
    Label('L1')
    CompareEventFlag(0, z37, 1)
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

def event_m10_14_x160(z38=114020084):
    """[Execution] Prelude Battle_Generation of Queen
    z38: Queen generation flag
    """
    """State 0,1: Former Samurai Battle_Two Queen Generation Flag ON"""
    SetEventFlag(z38, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x161(z36=114000081, z37=114000083, z38=114020084):
    """[Preset] Prelude Battle_Queen Generation Judgment
    z36: Boss destruction flag
    z37: Withdrawal flag
    z38: Queen generation flag
    """
    """State 0,1: [Reproduction] Prelude Battle_Queen Generation Determination_SubState"""
    call = event_m10_14_x159()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Preliminary Battle_Queen Generation Judgment_SubState"""
        call = event_m10_14_x158(z36=z36, z37=z37)
        if call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
        elif call.Get() == 3:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Prelude Battle_Queen Generation Judgment_SubState"""
            assert event_m10_14_x160(z38=z38)
    """State 4: End state"""
    return 0

def event_m10_14_x162(flag5=114020084):
    """[Reproduction] Preliminary Battle with Boss
    flag5: Pre-battle boss generation determination flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Queen generation flag determination"""
        if GetEventFlag(flag5) != 1:
            pass
        else:
            """State 3: Not destroyed or withdrawn"""
            return 0
    """State 4: Simple end"""
    return 1

def event_m10_14_x163(flag4=114020084):
    """[Reproduction] Deletion after withdrawal
    flag4: Pre-battle boss generation determination flag
    """
    """State 0,1: Queen generation flag determination"""
    if GetEventFlag(flag4) != 1:
        """State 3: Simple end"""
        return 1
    else:
        """State 2: Not destroyed or withdrawn"""
        return 0

def event_m10_14_x164(z27=10143101, z28=10145120, z29=500000, z30=10143100):
    """[Preset] Treasure chest appears when switch is pulled
    z27: Scaffolding OBJ instance ID
    z28: Treasure chest OBJ instance ID
    z29: Point ID for Navimesh change
    z30: Switch OBJ instance ID
    """
    """State 0,1: [Reproduction] Treasure chest appears when switch is pulled_SubState"""
    call = event_m10_14_x90(z27=z27, z28=z28, z29=z29, z30=z30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] When you pull the switch, a treasure box appears._SubState"""
        assert event_m10_14_x91(z30=z30)
        """State 3: [Execution] Treasure chest appears when switch is pulled_SubState"""
        assert event_m10_14_x92(z27=z27, z29=z29, z30=z30)
    """State 4: End state"""
    return 0

def event_m10_14_x165(flag3=114000081, z23=1014001, z24=1000, z25=114020084, z26=114000083):
    """[Preset] Outpost Battle_Boss HP Gauge Display
    flag3: Boss destruction flag
    z23: Boss Battle ID
    z24: Generator ID
    z25: Generation determination flag
    z26: Withdrawal flag
    """
    """State 0,1: [Reproduction] Prelude Battle_Boss HP Gauge Display_SubState"""
    call = event_m10_14_x166(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Conditions] Preliminary Battle_Boss HP Gauge Display_SubState"""
        assert event_m10_14_x167(z24=z24, z25=z25)
        """State 3: [Execution] Prelude Battle_Boss HP Gauge Display_SubState"""
        assert event_m10_14_x168(z23=z23)
        """State 2: [Reproduction] Prelude Battle_Boss HP Gauge Display_Sky_SubState"""
        assert event_m10_14_x169()
        """State 6: [Condition] Preliminary Battle_Boss HP Gauge Display_End Judgment_SubState"""
        assert event_m10_14_x170(z26=z26)
        """State 4: [Execution] Prelude Battle_Boss HP Gauge Display_End_SubState"""
        assert event_m10_14_x171(z23=z23)
    """State 7: End state"""
    return 0

def event_m10_14_x166(flag3=114000081):
    """[Reproduction] Front battle _ boss HP gauge display
    flag3: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag3) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_14_x167(z24=1000, z25=114020084):
    """[Conditions] Front battle_Boss HP gauge display
    z24: Generator ID
    z25: Generation determination flag
    """
    """State 0,1: Generating the start battle boss and canceling the activation state"""
    CompareChrStartUpState(8, z24, 2, 1)
    IsChrActive(8, z24, 1)
    CompareEventFlag(8, z25, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_14_x168(z23=1014001):
    """[Execution] Prelude Battle_Boss HP Gauge Display
    z23: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z23)
    """State 2: End state"""
    return 0

def event_m10_14_x169():
    """[Reproduction] Prelude Battle_Boss HP Gauge Display_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x170(z26=114000083):
    """[Condition] Prelude Battle_Boss HP Gauge Display_End Judgment
    z26: Withdrawal flag
    """
    """State 0,1: Has the withdrawal started?"""
    CompareEventFlag(0, z26, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x171(z23=1014001):
    """[Execution] Prelude Battle_Boss HP Gauge Display_End
    z23: Boss Battle ID
    """
    """State 0,1: Boss battle end notification"""
    CancelBossFight(z23)
    """State 2: End state"""
    return 0

def event_m10_14_x172(z19=10141180, z20=2500000, z21=2500001, z22=10141170):
    """[Preset] Interlocking destruction due to scaffold destruction
    z19: Scaffolding OBJ instance ID
    z20: Point ID for changing the navigation mesh at the top of the scaffold
    z21: Point ID for changing the navigation mesh at the bottom of the scaffold
    z22: Instance ID of scaffolding OBJ to be interlocked
    """
    """State 0,1: [Reproduction] Interlocking destruction due to scaffold destruction_SubState"""
    call = event_m10_14_x173(z19=z19, z20=z20, z21=z21)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Interlocking destruction due to scaffold destruction_SubState"""
        assert event_m10_14_x174(z19=z19)
    """State 3: [Execution] Linkage destruction due to scaffold destruction_SubState"""
    assert event_m10_14_x175(z20=z20, z21=z21, z22=z22)
    """State 4: End state"""
    return 0

def event_m10_14_x173(z19=10141180, z20=2500000, z21=2500001):
    """[Reproduction] Interlocking destruction due to scaffold destruction
    z19: Scaffolding OBJ instance ID
    z20: Point ID for changing the navigation mesh at the top of the scaffold
    z21: Point ID for changing the navigation mesh at the bottom of the scaffold
    """
    """State 0,1: Scaffold OBJ status determination"""
    if CompareObjStateId(z19, 20, 0):
        """State 5: Destroyed"""
        return 1
    else:
        """State 2: Navi-mesh attribute deletion at the top of the scaffold"""
        DeleteNavimeshAttribute(z20, 2)
        """State 3: Added navigation mesh attributes at the bottom of the scaffolding"""
        AddNavimeshAttribute(z21, 2)
        """State 4: Undestructed"""
        return 0

def event_m10_14_x174(z19=10141180):
    """[Condition] Interlocking destruction due to scaffold destruction
    z19: Scaffolding OBJ instance ID
    """
    """State 0,1: Has the scaffold OBJ been destroyed?"""
    CompareObjState(0, z19, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_14_x175(z20=2500000, z21=2500001, z22=10141170):
    """[Execution] Interlocking destruction due to scaffold destruction
    z20: Point ID for changing the navigation mesh at the top of the scaffold
    z21: Point ID for changing the navigation mesh at the bottom of the scaffold
    z22: Instance ID of scaffolding OBJ to be interlocked
    """
    """State 0,1: Added navigation mesh attributes at the top of the scaffold"""
    AddNavimeshAttribute(z20, 2)
    """State 2: Navimesh attribute deletion at the bottom of the scaffold"""
    DeleteNavimeshAttribute(z21, 2)
    """State 3: Judgment of the state of the scaffold where interlocking destruction occurs"""
    CompareObjState(0, z22, 10, 0)
    if ConditionGroup(0):
        """State 4: Destroying the scaffold where interlocking destruction occurs"""
        ChangeObjState(z22, 20)
    else:
        pass
    """State 5: End state"""
    return 0

def event_m10_14_x176(flag2=114000052, z14=10146500):
    """[Reproduction] Pig eats mushrooms
    flag2: Mushroom complete eating flag
    z14: Item OBJ instance ID
    """
    """State 0,1: Have you already eaten mushrooms?"""
    if GetEventFlag(flag2) != 0:
        """State 4: Meal"""
        return 1
    else:
        """State 2: Hide item"""
        ChangeDrawHit(z14, 0)
        """State 3: Before meal"""
        return 0

def event_m10_14_x177(z17=_, z15=2300000, z18=2300000, z16=10, flag2=114000052):
    """[Condition] Pigs eat mushrooms
    z17: Pig generator ID
    z15: Start point ID
    z18: End point ID
    z16: Time to complete meal
    flag2: Meal completion flag
    """
    """State 0,1: Has the pig started to eat mushrooms?"""
    CompareChrEzStateValue(0, z17, 7, 1, 0)
    assert ConditionGroup(0)
    """State 2: Meal success or failure"""
    CompareEventFlag(0, flag2, 1)
    CompareChrEzStateValue(8, z17, 7, 1, 0)
    CompareStateTime(8, z16, 3, z16)
    CompareChrEzStateValue(1, z17, 7, 1, 1)
    if ConditionGroup(0):
        """State 5: Other pigs successfully eat: finished"""
        return 2
    elif ConditionGroup(8):
        """State 3: Meal success: item display"""
        return 0
    elif ConditionGroup(1):
        """State 4: Meal failure: re-execution"""
        return 1

def event_m10_14_x178(flag2=114000052, z13=10141590, z14=10146500):
    """[Execution] Pigs eat mushrooms
    flag2: Mushroom complete eating flag
    z13: Mushroom OBJ instance ID
    z14: Item OBJ instance ID
    """
    """State 0,1: Mushroom OBJ complete meal: 10"""
    ChangeObjState(z13, 10)
    """State 2: Item appearance"""
    ChangeDrawHit(z14, 1)
    """State 3: Mushroom complete meal flag ON"""
    SetEventFlag(flag2, 1)
    """State 4: End state"""
    return 0

def event_m10_14_x179(flag2=114000052, z13=10141590, z14=10146500, z15=2300000, z16=10, z17=_):
    """[Preset] Pigs eat mushrooms
    flag2: Mushroom complete eating flag
    z13: Mushroom OBJ instance ID
    z14: Item OBJ instance ID
    z15: Point ID
    z16: Time to complete meal
    z17: Pig generator ID
    """
    """State 0,2: [Reproduction] Pig eats mushrooms_SubState"""
    call = event_m10_14_x176(flag2=flag2, z14=z14)
    if call.Get() == 1:
        """State 1: Item display"""
        Label('L0')
        ChangeDrawHit(z14, 1)
    elif call.Get() == 0:
        """State 4: [Condition] Pig eats mushrooms_SubState"""
        call = event_m10_14_x177(z17=z17, z15=z15, z18=z15, z16=z16, flag2=flag2)
        if call.Get() == 2:
            Goto('L0')
        elif call.Get() == 0:
            """State 3: [Execution] Pig eats mushrooms_SubState"""
            assert event_m10_14_x178(flag2=flag2, z13=z13, z14=z14)
        elif call.Get() == 1:
            """State 6: Rerun"""
            return 1
    """State 5: End state"""
    return 0

def event_m10_14_x180():
    """[Reproduction] Boss: The queen of fox"""
    """State 0,1: End state"""
    return 0

def event_m10_14_x181(z9=_, z10=114000081, z11=120):
    """[Conditions] Boss: Queen of Akatsuki _ Zakokoku generation
    z9: Zako Generator ID
    z10: Boss destruction flag
    z11: Time to flag ON
    """
    """State 0,1: Corresponding spider died or destroyed boss"""
    IsChrDead(0, z9)
    CompareEventFlag(1, z10, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 2: Generation waiting or boss destruction"""
        CompareStateTime(0, z11, 3, z11)
        CompareEventFlag(1, z10, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 3: Zako death: flag ON"""
            return 0
    """State 4: Defeat Boss: Finish"""
    return 1

def event_m10_14_x182(z12=_):
    """[Execution] Boss: Spider Queen
    z12: Zako spider generation flag
    """
    """State 0,1: Generation flag ON"""
    SetEventFlag(z12, 1)
    """State 2: End state"""
    return 0

def event_m10_14_x183(z9=_, z10=114000081, z11=120, z12=_):
    """[Preset] Boss
    z9: Zako Generator ID
    z10: Boss destruction flag
    z11: Time to flag ON
    z12: Zako spider generation flag
    """
    """State 0,1: [Reproduction] Boss: Saddle Queen_Zako Spider Generation_Sky_SubState"""
    assert event_m10_14_x180()
    """State 3: [Conditions] Boss: The queen of fox"""
    call = event_m10_14_x181(z9=z9, z10=z10, z11=z11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Boss: Spider Queen"""
        assert event_m10_14_x182(z12=z12)
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
    event_m10_14_x1(z167=104153, z168=10144300, z169=56, z170=7420)
    Quit()

def event_m10_14_111233():
    """OBJ: Wandering Warrior: Key Guide"""
    """State 0,1: Death map flag judgment"""
    CompareEventFlag(0, 104153, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_14_x4(z162=114010110, z163=114020111, z164=104150, z165=10144300, z166=111232, npc1=7420)
    Quit()

def event_m10_14_111234():
    """OBJ: Wandering Warrior: Death Judgment"""
    """State 0,1: Wandering & Patch: Death Determination_SubState"""
    event_m10_14_x119(z62=104153, z63=55, z64=102402, z65=102445)
    Quit()

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
    Quit()

def event_m10_14_111246():
    """OBJ: Satoshi Tsutsumi: White phantom sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m10_14_x31(z116=102430, z117=526, z118=104160, z119=103660, z120=-1)
    Quit()

def event_m10_14_111247():
    """OBJ: Satoshi Tsutsumi: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_14_x28(z131=114000096, z132=102436, z133=205, z134=7430)
    Quit()

def event_m10_14_111252():
    """OBJ: Patch: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_14_x1(z167=104173, z168=10144200, z169=66, z170=7440)
    Quit()

def event_m10_14_111253():
    """OBJ: Patch: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7440:Mild-mannered Pate
    event_m10_14_x4(z162=114010120, z163=114020121, z164=104170, z165=10144200, z166=111252, npc1=7440)
    Quit()

def event_m10_14_111254():
    """OBJ: Patch: Death determination"""
    """State 0,1: Wandering & Patch: Death Determination_SubState"""
    event_m10_14_x119(z62=104173, z63=65, z64=102445, z65=102402)
    Quit()

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
    Quit()

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
    Quit()

def event_m10_14_111332():
    """OBJ: Wandering Warrior (Patch Death): Grave"""
    """State 0: Start state"""
    assert EventEnded(111232) != 0
    """State 2: Grave generation judgment"""
    CompareEventFlag(0, 104153, 1)
    if ConditionGroup(0):
        """State 1: System: Exit"""
        EndMachine()
        Quit()
    else:
        """State 3: [Lib] NPC: Grave Placement: General Purpose_SubState"""
        event_m10_14_x1(z167=104154, z168=10144300, z169=58, z170=7420)
        Quit()

def event_m10_14_111333():
    """OBJ: Wandering Warrior (Patch Death): Key Guide"""
    """State 0,1: Death map flag judgment"""
    CompareEventFlag(0, 104154, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_14_x4(z162=114010109, z163=114020111, z164=104150, z165=10144300, z166=111332, npc1=7420)
    Quit()

def event_m10_14_111334():
    """OBJ: Wandering Warrior (Patch Death): Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_14_x7(z153=57, z154=104154)
    Quit()

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
    Quit()

def event_m10_14_111435():
    """OBJ: Sealed Person: Black Phantom Sign Display"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_14_x29(z125=102810, z126=10001000, z127=521, z128=104340, z129=0, z130=2)
    Quit()

def event_m10_14_111452():
    """OBJ: Upper weapon shop: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_14_x1(z167=104362, z168=10144100, z169=266, z170=7760)
    Quit()

def event_m10_14_111453():
    """OBJ: Upper weapon shop: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7760:Weaponsmith Ornifex
    event_m10_14_x4(z162=114010130, z163=114020131, z164=104360, z165=10144100, z166=111452, npc1=7760)
    Quit()

def event_m10_14_111454():
    """OBJ: Upper weapon shop: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_14_x7(z153=265, z154=104362)
    Quit()

def event_m10_14_111482():
    """NPC: Immoral Teacher: Grave"""
    """State 0,1: NPC: Immoral Teacher: Grave Placement_SubState"""
    event_m10_14_x1(z167=104390, z168=10144000, z169=311, z170=7840)
    Quit()

def event_m10_14_111483():
    """NPC: Immoral Teacher: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7840:Cromwell the Pardoner
    event_m10_14_x4(z162=114010100, z163=114020101, z164=104390, z165=10144000, z166=111482, npc1=7840)
    Quit()

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
    Quit()

def event_m10_14_118100():
    """Multi NPC: Test 1_ Boss Long Distance: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_14_x23(z137=528)
    Quit()

def event_m10_14_118110():
    """Multi-use NPC: Test 2_ Tavern: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_14_x23(z137=529)
    Quit()

def event_m10_14_118120():
    """Multi-use NPC: Leroy: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_14_x23(z137=527)
    Quit()

def event_m10_14_118210():
    """Multi NPC: Dark Spirit Test: Black Phantom Appearance"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_14_x30(z121=10002000, z122=520, z123=0, z124=2)
    Quit()

def event_m10_14_3000000():
    """[DLC] Shop lineup expansion_Demon Knight Kai"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m10_14_x43(z112=101063, flag15=101213)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4000000():
    """[BEST] Appearance of Andyel"""
    """State 0,3: [Lib] [BEST] [Preset] Ander_Termination_SubState"""
    call = event_m10_14_x50(z105=10141810, flag12=100740, flag13=100741, flag14=100760, z106=100461,
                            z107=100300, z108=100360, z109=100400)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_4001000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m10_14_x63(z103=10141810, z104=10141800)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_4002000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m10_14_x55(z110=10141810, z111=10141800)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_4003000():
    """[BEST] Anderu Navimesh switching"""
    """State 0,3: [Lib] [BEST] [Preset] Anderu's navigation mesh switching_SubState"""
    call = event_m10_14_x68(z101=10141810, z102=6003000)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_14_4010000():
    """[DC] Lighthouse lighting management_01"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140700, z5=114020180)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010010():
    """[DC] Lighthouse lighting management_02"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140701, z5=114020181)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010020():
    """[DC] Lighthouse lighting management_03"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140702, z5=114020182)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010030():
    """[DC] Lighthouse lighting management_04"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140703, z5=114020183)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010040():
    """[DC] Lighthouse lighting management_05"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140704, z5=114020184)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010050():
    """[DC] Lighthouse lighting management_06"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140705, z5=114020185)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010060():
    """[DC] Lighthouse lighting management_07"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140706, z5=114020186)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4010080():
    """[DC] Lighthouse lighting management_09"""
    """State 0,2: [DC] [Preset] Lighthouse lighting management_SubState"""
    assert event_m10_14_x188(z4=10140708, z5=114020188)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011000():
    """[DC] Thorn damage switch for peasant_1"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5251, z3=200014060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011010():
    """[DC] Thorn damage switching of peasant deceased_2"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5252, z3=200014060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011020():
    """[DC] Thorn damage switching of peasant deceased_3"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5253, z3=200014060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011030():
    """[DC] Thorn damage switching of farmer deceased_4"""
    """State 0,2: [DC] [Preset] Farmer deceased thorn damage switch_SubState"""
    assert event_m10_14_x192(z2=5254, z3=200014060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011500():
    """[DC] Farmer deceased locked lock_1"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5251)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011510():
    """[DC] Unlockable management of peasant deceased_2"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5252)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011520():
    """[DC] Farmer deceased locked lock_3"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5253)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4011530():
    """[DC] Farmer deceased locked lock_4"""
    """State 0,2: [DC] [Preset] Farmer deceased lock disabled management_SubState"""
    assert event_m10_14_x196(z1=5254)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4012000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_14_x72(flag9=114020001, z89=14, flag10=114000002, z90=4, z91=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_14_x77(z94=80000000, z95=0, z96=5, z97=926, val1=1, z98=10, z99=80000001, z100=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_14_x77(z94=80000100, z95=0, z96=5, z97=926, val1=2, z98=10, z99=80000101, z100=80000199)
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m10_14_x77(z94=80000200, z95=0, z96=5, z97=926, val1=3, z98=10, z99=80000201, z100=80000299)
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert event_m10_14_x77(z94=80000300, z95=0, z96=5, z97=926, val1=4, z98=10, z99=80000301, z100=80000399)
        """State 2: Start flag ON"""
        SetEventFlag(114020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4012010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_14_x80(flag11=114000002, z92=926, mode1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4013000():
    """[DC] Treasure corpse 7"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141506, z50=10146480)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4013010():
    """[DC] Treasure corpse 8"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141507, z50=10146490)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4013020():
    """[DC] Treasure corpse 9"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141508, z50=10146510)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4013030():
    """[DC] Treasure corpse 10"""
    """State 0,2: [Preset] Treasure corpse _SubState"""
    assert event_m10_14_x138(z49=10141509, z50=10146520)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_14_4031000():
    """[DC] NPC White Spirit_Gesture Management_The Queen"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_14_x85(flag8=114000081, z87=803, z88=114020079)
    """State 1: Finish"""
    EndMachine()
    Quit()

