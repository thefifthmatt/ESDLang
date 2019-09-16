# -*- coding: utf-8 -*-
def event_m20_21_1000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_21_x38(z204=20211600, z205=20, z206=100000, z207=0, z208=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_2000():
    """Key door that opens with "Corridor key" """
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m20_21_x9(z235=1005, z236=1105, z237=50610000, z238=221000020)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_3000():
    """Lever door between soldiers"""
    """State 0,2: [Preset] Lever door between soldiers_SubState"""
    assert event_m20_21_x170(z51=20212000, z52=20211520, z53=20210410, z54=300000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4000():
    """OBJ: Shenzhen Pilgrim: Magic Circle Open"""
    """State 0,1: [Lib] Pilgrim of Shenzhen: Magic Square: Open_SubState"""
    event_m20_21_x4(z252=102326, z253=102329, z254=20213000)

def event_m20_21_4001():
    """OBJ: Shenzhen Pilgrim: Magic Warp"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Key Guide_SubState"""
    event_m20_21_x6(z244=102326, z245=20213000, z246=102329, z247=400020, z248=0)

def event_m20_21_4002():
    """OBJ: Shenzhen Pilgrim: Magic Circle Opening"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Opening Production_SubState"""
    event_m20_21_x5(z249=20213000, z250=102326, z251=221020107)

def event_m20_21_5000():
    """Elevator 昇降 Amana Altar"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(5030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m20_21_x18(z186=20213100, z187=500010, z188=500000, z189=20211500, z190=20211510)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_5010():
    """Elevator lever message display_upper"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z224=20213100, z225=20211500, z226=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_5020():
    """Elevator lever message display_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z224=20213100, z225=20211510, z226=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_5030():
    """Elevator_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m20_21_x31(z220=20213100, z221=40, z222=221000015, z223=40)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_5040():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m20_21_x46(z191=504000, z192=20213100, z193=105430, z194=10, z195=20, z196=0, z197=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_5050():
    """_PC forced death for connection"""
    """State 0,2: [Lib] [Preset] [Asynchronous] Player forced fall death_SubState"""
    assert event_m20_21_x65(z146=505000, z147=3)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_5060():
    """For connection_Connection flag OFF"""
    """State 0,3: [Lib] [Preset] Switch the connection flag at the point _SubState"""
    call = event_m20_21_x71(z141=506000, z142=506000, z143=105430, z144=0, z145=1)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()

def event_m20_21_6000():
    """Golem door 01"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z112=20210400, z113=221000033, z114=6.7, z115=600000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6010():
    """Golem door 02"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z112=20210401, z113=221000034, z114=6.7, z115=601000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6020():
    """Golem door 03"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z112=20210402, z113=221000035, z114=6.7, z115=602000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6030():
    """Golem door 04"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z112=20210403, z113=221000036, z114=6.7, z115=603000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6040():
    """Golem door 05"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z112=20210404, z113=221000037, z114=6.7, z115=604000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6050():
    """Golem door 06"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z112=20210405, z113=221000038, z114=6.7, z115=605000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6100():
    """Main gate golem_Right"""
    """State 0,2: [Preset] Golem_Main Gate_SubState"""
    assert event_m20_21_x109(z55=20212500, z56=20212600, z57=221000039, z58=7.5)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6105():
    """Main gate golem_Left"""
    """State 0,2: [Preset] Golem_Main Gate_SubState"""
    assert event_m20_21_x109(z55=20212505, z56=20212605, z57=221000040, z58=7.5)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_6110():
    """The main gate of the golem"""
    """State 0,2: [Preset] Golem Main Gate_SubState"""
    assert (event_m20_21_x160(z65=20210407, z66=20212600, z67=20212605, z68=221000041, z69=20212500,
            z70=20212505))
    """State 1: Finish"""
    EndMachine()

def event_m20_21_7000():
    """Boss: Heavy cavalry: Soldier only 2 battles_battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m20_21_x11(z227=221000081, z228=700000, z229=700000, z230=202, z231=1021000, z232=221020080,
            mode5=0))
    """State 1: Finish"""
    EndMachine()

def event_m20_21_7010():
    """Boss: Heavy cavalry: Soldier only 2 battles_Light switching"""
    """State 0,2: [Preset] Boss: Heavy cavalry: Soldier only 2 battles_Light switch_SubState"""
    assert event_m20_21_x175(z46=20210001, z47=20210002, z48=701000, z49=701002)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_8000():
    """Boss: Mirror Knight_Battle"""
    """State 0,2: [Preset] Mirror Night Battle Start_SubState"""
    assert (event_m20_21_x167(z59=221000086, z60=800000, z61=800000, z62=201, z63=1021010, z64=221020085,
            mode2=0))
    """State 1: Finish"""
    EndMachine()

def event_m20_21_9000():
    """King's door"""
    """State 0,3: [Preset] Door of the King_SubState"""
    call = event_m20_21_x98(z33=20210406, z34=900000, z35=221000021)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m20_21_10000():
    """Acid spitting dragon statue"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z110=20211100, z111=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_10010():
    """Acid spitting dragon statue_2"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z110=20211105, z111=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_10020():
    """Acid spitting dragon statue_3"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z110=20211110, z111=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_10030():
    """Acid spitting dragon statue_4"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z110=20211115, z111=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_11000():
    """Boss Battle: Queen Knight AC, Queen"""
    """State 0,3: [Preset] Boss Battle: Queen's Knight_SubState"""
    call = event_m20_21_x123(z6=1100000, z7=1100000, z8=102, z9=1021020, z10=221020090, z11=100972, z12=221000091,
                             z13=1021021)
    if call.Get() == 7:
        """State 2: White door control flag ON"""
        Label('L0')
        SetEventFlag(221000092, 1)
    elif call.Get() == 4:
        """State 7: [Preset] Boss Battle: Andyel_SubState"""
        assert event_m20_21_x184(z25=1200010, z26=1200011, z27=701, z28=1021040, z29=221020005, z30=221000006)
    elif call.Get() == 6:
        """State 8: [Preset] Boss Battle: Queen_C_2 Series Battle_SubState"""
        assert (event_m20_21_x128(z91=1200000, z92=1200000, z93=101, z94=1021031, z95=221020095, z96=221000096,
                z97=221000097))
        """State 9: [Preset] Boss Battle: Andyel_Sequential Battle_SubState"""
        Label('L1')
        assert event_m20_21_x197(z19=701, z20=1021040, z21=221020005, z22=221000006, z23=1200010, z24=1200011)
    elif call.Get() == 1:
        """State 4: [Preset] Boss Battle: Queen_A_SubState"""
        assert (event_m20_21_x128(z91=1200000, z92=1200000, z93=101, z94=1021030, z95=221020095, z96=221000096,
                z97=221000097))
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 2:
        Goto('L0')
    elif call.Get() == 3:
        """State 5: [Preset] Boss Battle: Queen_B_SubState"""
        assert (event_m20_21_x128(z91=1200001, z92=1200001, z93=101, z94=1021030, z95=221020095, z96=221000096,
                z97=221000098))
    elif call.Get() == 5:
        """State 6: [Preset] Boss Battle: Queen_C_3 Consecutive_SubState"""
        assert (event_m20_21_x128(z91=1200001, z92=1200001, z93=101, z94=1021031, z95=221020095, z96=221000096,
                z97=221000098))
        Goto('L1')
    """State 1: Finish"""
    EndMachine()

def event_m20_21_11010():
    """Queen Knight AC_Destroy"""
    """State 0,2: [Preset] Queen Knight AC_Destroy_SubState"""
    assert event_m20_21_x132(z84=860, z85=862, z86=93320030, z87=93340030, z88=221000091)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_12010():
    """Boss Battle_Poly Drama: Queen Knight, Queen"""
    """State 0,2: [Preset] Poly Play Management: Queen Knight, Queen_SubState"""
    assert event_m20_21_x126()
    """State 1: Finish"""
    EndMachine()

def event_m20_21_13000():
    """Elevator_in front of corridor"""
    """State 0,2: Has the elevator golem event been completed?"""
    assert EventEnded(13030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m20_21_x18(z186=20213110, z187=1300000, z188=1300010, z189=20211540, z190=20211530)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_13010():
    """Elevator_in front of corridor_lever message_up"""
    """State 0,2: Has the elevator golem event been completed?"""
    assert EventEnded(13030) != 0
    """State 3: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z224=20213110, z225=20211540, z226=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_13020():
    """Elevator_in front of corridor_lever message_bottom"""
    """State 0,2: Has the elevator golem event been completed?"""
    assert EventEnded(13030) != 0
    """State 3: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z224=20213110, z225=20211530, z226=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_21_13030():
    """Elevator golem activation"""
    """State 0,2: [Preset] Elevator Golem Activation_SubState"""
    assert (event_m20_21_x113(z101=20212520, z102=20212620, z103=20213110, z104=20211530, z105=20211540,
            z106=7.5, z107=221000010, z108=221000032))
    """State 1: Finish"""
    EndMachine()

def event_m20_21_14000():
    """[Preliminary] Portrait of the Queen"""
    """State 0,1: Finish"""
    EndMachine()

def event_m20_21_15000():
    """White door management during splicing"""
    """State 0,2: [Preset] White door management during sublimation_SubState"""
    assert event_m20_21_x120()
    """State 1: Finish"""
    EndMachine()

def event_m20_21_16000():
    """End roll"""
    """State 0,2: [Preset] End roll_SubState"""
    assert event_m20_21_x136(z79=1600000, z80=221000094, z81=221020002)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_17000():
    """Setting retry points after defeating the Queen"""
    """State 0,2: [Preset] Retry point setting after defeating the Queen_SubState"""
    assert event_m20_21_x140(z78=221000093)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_19000():
    """Golems that move by sucking souls_1"""
    """State 0,2: [Preset] Golem that moves by sucking a soul (lights on) _SubState"""
    assert event_m20_21_x141(z74=20212510, z75=20212700, z76=221000030, z77=6.7)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_19010():
    """Golem that moves by sucking a soul (lights on) _2"""
    """State 0,2: [Preset] Golem that moves by sucking a soul (lights on) _SubState"""
    assert event_m20_21_x141(z74=20212515, z75=20212705, z76=221000031, z77=6.7)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_20000():
    """Statue of Nation 1"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z72=3010, z73=20211001)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_20010():
    """Statue Neck Drop_2"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z72=3020, z73=20211000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_20020():
    """Statue of Neck _3"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z72=3030, z73=20211002)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_20030():
    """Statue Neck Drop_4"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z72=3040, z73=20211003)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_21000():
    """Key person"""
    """State 0,3: [SFX] Stop SFX generated by you"""
    call = event_m20_21_x150(z71=20211700)
    if call.Get() == 2:
        """State 2: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 1: Rerun"""
        RestartMachine()

def event_m20_21_22000():
    """Vegrant Deletion Decision_Left"""
    """State 0,2: [Preset] Vegrant deletion determination_SubState"""
    assert event_m20_21_x174(z50=8000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_22010():
    """Vegrant Deletion Decision_Right"""
    """State 0,2: [Preset] Vegrant deletion determination_SubState"""
    assert event_m20_21_x174(z50=8010)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_80000():
    """Rebirth Fire 01_In front of the King's door to the last boss"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_21_x58(z171=2021000, z172=2021099)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_81000():
    """After the fire of rebirth 02_ boss heavy cavalry"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_21_x58(z171=2021100, z172=2021199)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_82000():
    """Reproduction of fire 03_in the hidden door"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_21_x58(z171=2021200, z172=2021299)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_90000():
    """Trophy_Knight of the Mirror"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_21_x62(z155=221000086, z156=10)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_x0(z82=_, val1=1600010, z259=0, z260=0, z261=1):
    """[Lib] Normal poly play
    z82: Poly play ID
    val1: Destination point ID after poly play
    z259: Poly drama played flag
    z260: End fade
    z261: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(z259) != 1:
        """State 1: Poly play"""
        PlayCutscene(z82, z260, z261)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((val1 > 1) != 0, val1)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((val1 > 1) != 0, val1)
    SetEventFlag(z259, 1)
    """State 7: End state"""
    return 0

def event_m20_21_x1(z255=_, z256=_, z257=_, z258=_):
    """[Lib] NPC: Grave Placement: General purpose
    z255: Death map: Global event flag
    z256: Tomb: OBJ instance ID
    z257: Tomb move to: Generator ID
    z258: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z255, 1)
    IsGraveGeneratable(8, z258, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z256, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z256, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m20_21_x2(z241=_, z242=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z241: Global: death flag
    z242: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z242, 10, 0)
    CompareObjState(1, z242, 20, 0)
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
    IsObjSearched(0, z242)
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

def event_m20_21_x3(z239=_, z240=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z239: Area other flags: Ghost appearance
    z240: Area other flags: Conversation start
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
    SetEventFlag(z239, 1)
    CompareEventFlag(0, z239, 1)
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
    SetEventFlag(z240, 1)
    CompareEventFlag(0, z240, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m20_21_x4(z252=102326, z253=102329, z254=20213000):
    """[Lib] Shenzhen Pilgrim: Magic Square: Open
    z252: Magic Square: Open: Global Event Flag
    z253: Magic Square: Invasion: Global Event Flag
    z254: Magic Square: OBJ instance ID
    """
    """State 0,1: Magic Square: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Magic square: All open judgment"""
        CompareEventFlag(8, 100979, 1)
        CompareEventFlag(8, z252, 1)
        CompareEventFlag(9, 100979, 1)
        CompareEventFlag(8, z252, 0)
        if ConditionGroup(8):
            pass
        elif ConditionGroup(9):
            """State 9: Magic Square: All Invasion Flag: OFF"""
            SetEventFlag(102328, 0)
            SetEventFlag(102329, 0)
            SetEventFlag(102330, 0)
            CompareEventFlag(8, 102328, 0)
            CompareEventFlag(8, 102329, 0)
            CompareEventFlag(8, 102330, 0)
            assert ConditionGroup(8)
            """State 2: Magic Square: Open"""
            Label('L0')
            ChangeOwnObjState(70)
            CompareObjState(0, z254, 30, 0)
            assert ConditionGroup(0)
        else:
            """State 3: Magic Square: Player Return Judgment"""
            CompareEventFlag(8, z252, 1)
            CompareEventFlag(8, z253, 1)
            if ConditionGroup(8):
                """State 4: Magic square: Flag initialization setting"""
                SetEventFlag(z252, 0)
                SetEventFlag(z253, 0)
                CompareEventFlag(8, z252, 0)
                CompareEventFlag(8, z253, 0)
                assert ConditionGroup(8)
                """State 8: Magic Square: Erasure"""
                ChangeOwnObjState(80)
                CompareObjState(0, z254, 10, 0)
                assert ConditionGroup(0)
            else:
                """State 6: Magic Square: Open Flag Judgment"""
                CompareEventFlag(0, z252, 1)
                if ConditionGroup(0):
                    Goto('L0')
                else:
                    pass
    """State 5: Magic Square: System: End"""
    EndMachine()

def event_m20_21_x5(z249=20213000, z250=102326, z251=221020107):
    """[Lib] Shenzhen Pilgrims: Magic Square: Opening Production
    z249: Magic Square: OBJ instance ID
    z250: Magic Square: Open: Global Event Flag
    z251: Magic Square: Production Start: Area and Other Flags
    """
    """State 0,4: Appearance production: Start"""
    CompareEventFlag(0, z251, 1)
    assert ConditionGroup(0)
    """State 3: Appearance effect: Open flag setting"""
    SetEventFlag(z250, 1)
    CompareEventFlag(0, z250, 1)
    assert ConditionGroup(0)
    """State 1: Appearance Direction: Magic Square Appearance"""
    ChangeOwnObjState(70)
    CompareObjState(0, z249, 30, 0)
    assert ConditionGroup(0)
    """State 5: Appearance production: End"""
    SetEventFlag(z251, 0)
    CompareEventFlag(0, z251, 0)
    assert ConditionGroup(0)
    """State 2: Appearance production: System: End"""
    EndMachine()

def event_m20_21_x6(z244=102326, z245=20213000, z246=102329, z247=400020, z248=0):
    """[Lib] Shenzhen Pilgrim: Magic Square: Key Guide
    z244: Magic Square: Open: Global Event Flag
    z245: Magic Square: OBJ instance ID
    z246: Magic Square: Invasion: Global Event Flag
    z247: Magic Square: Warp Point
    z248: Magic Square: During Warp: Area Other Flag
    """
    """State 0,1: Key guide: Start"""
    CompareObjState(0, z245, 30, 0)
    assert ConditionGroup(0)
    """State 4: Key guide: Multiplayer judgment"""
    IsMultiplayer(0, 1, 1)
    IsPlayerInCovenant(1, 9, 0)
    if ConditionGroup(0):
        """State 2: Key guide: Multiplayer judgment: Hidden standby"""
        Label('L0')
        DeleteKeyGuideArea()
        IsMultiplayer(8, 0, 1)
        IsPlayerInCovenant(8, 9, 1)
        assert ConditionGroup(8)
    elif ConditionGroup(1):
        Goto('L0')
    else:
        """State 3: Key Guide: Display standby"""
        CreateKeyGuideArea(34, 630)
        IsPlayerInCovenant(0, 9, 0)
        IsMultiplayer(1, 1, 1)
        IsObjSearched(2, z245)
        CompareObjState(3, z245, 10, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(2):
            """State 7: Key guide: Intrusion flag: Setting"""
            ProhibitMultiplayer(1)
            SetEventFlag(z248, 1)
            """State 8: Shenzhen Pilgrim: Magic Square: Warp_SubState"""
            call = event_m20_21_x7(z247=z247, z246=z246)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                """State 6: Key Guide: System: Exit"""
                EndMachine()
                Quit()
        elif ConditionGroup(3):
            pass
    """State 5: Key Guide: System: Rerun"""
    RestartMachine()

def event_m20_21_x7(z247=400020, z246=102329):
    """Shenzhen Pilgrim: Magic Square: Warp
    z247: Warp point ID
    z246: Intrusion: Global flag
    """
    """State 0,1: Warp: Start"""
    DeleteKeyGuideArea()
    """State 3: Warp: Player motion start"""
    PlayerActionRequest(6)
    IsPlayerPlayingMotion(0, 6, 1)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 4: Warp: Player motion standby"""
        CompareStateTime(0, 2.5, 2, 2.5)
        IsMultiplayer(1, 1, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 5: Warp: execute"""
            SetEventFlag(z246, 1)
            PlayCutsceneAndWarpToMap(0, 0, 40030000, z247, 0)
            assert CutsceneWarpEnded() != 0
            """State 2: Warp: Wait for completion"""
            CompareEventFlag(0, 0, 1)
            assert ConditionGroup(0)
            """State 6: Normal: End state"""
            return 0
    """State 7: Re-execution: end state"""
    return 1

def event_m20_21_x8(z239=_, z240=_, z241=_, z242=_, z243=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z239: Ghost Appearance: Area Other Flag
    z240: Conversation start: Area and other flags
    z241: Death: Global event flag
    z242: Tomb: OBJ instance ID
    z243: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z243, 1, 0)
    CompareEventFlag(9, z239, 1)
    CompareObjState(9, z242, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z240, 1)
        CompareEventFlag(0, z240, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m20_21_x2(z241=z241, z242=z242, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m20_21_x3(z239=z239, z240=z240, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m20_21_x9(z235=1005, z236=1105, z237=50610000, z238=221000020):
    """[Lib] Item specified door unlocking_2
    z235: Text ID when opened
    z236: Text ID when not opened
    z237: item
    z238: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z237, z235, z236, z238, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x10(z233=60, z234=104162):
    """[Lib] NPC: Death determination: General purpose
    z233: Generator ID
    z234: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z234, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z233)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z234, 1)
            CompareEventFlag(0, z234, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m20_21_x11(z227=221000081, z228=700000, z229=700000, z230=202, z231=1021000, z232=221020080,
                     mode5=0):
    """[Lib] [Preset] Boss Battle Start
    z227: Boss destruction flag
    z228: Start point ID
    z229: End point ID
    z230: Sound ID
    z231: Boss Battle ID
    z232: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(z22=z227)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m20_21_x13(z228=z228, z229=z229)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m20_21_x14(z93=z230, z94=z231, z95=z232)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z20=z231)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m20_21_x17(z19=z230, z20=z231, z21=z232, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m20_21_x12(z22=_):
    """[Reproduction] Boss Battle_Start
    z22: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z22) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_21_x13(z228=700000, z229=700000):
    """[Condition] Boss Battle_Start
    z228: Start point ID
    z229: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z228, z229, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z228, z229, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x14(z93=_, z94=_, z95=_):
    """[Execution] Boss Battle_Start
    z93: Sound ID
    z94: Boss Battle ID
    z95: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z93)
    """State 1: Boss battle start notification"""
    StartBossFight(z94)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z95, 1)
    """State 4: End state"""
    return 0

def event_m20_21_x15():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x16(z20=_):
    """[Condition] Boss Battle_End Judgment
    z20: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z20, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x17(z19=_, z20=_, z21=_, mode5=0):
    """[Execute] Boss Battle_End
    z19: Sound ID
    z20: Boss Battle ID
    z21: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z21, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z20)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z19)
    """State 5: End state"""
    return 0

def event_m20_21_x18(z186=_, z187=_, z188=_, z189=_, z190=_):
    """[Lib] [Preset] Elevator
    z186: OBJ instance ID of the elevator
    z187: On elevator point ID_
    z188: Elevator point ID_below
    z189: Upper lever OBJ instance ID
    z190: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m20_21_x19()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m20_21_x20(z186=z186, z187=z187, z188=z188, z189=z189, z190=z190)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m20_21_x51(z186=z186, z188=z188)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m20_21_x50(z186=z186, z187=z187)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m20_21_x21(z186=z186, z187=z187)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m20_21_x22(z186=z186, z188=z188)
    """State 7: End state"""
    return 0

def event_m20_21_x19():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x20(z186=_, z187=_, z188=_, z189=_, z190=_):
    """[Condition] Elevator
    z186: Elevator OBJ instance ID
    z187: On elevator point ID_
    z188: Elevator point ID_below
    z189: Upper lever OBJ instance ID
    z190: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z186, 10, 0)
    CompareObjState(1, z186, 40, 0)
    CompareObjState(2, z186, 80, 0)
    CompareObjState(2, z186, 41, 0)
    CompareObjState(3, z186, 70, 0)
    CompareObjState(3, z186, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z188, z188, 1)
        CompareObjState(0, z189, 74, 0)
        CompareObjState(0, z189, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z187, z187, 1)
        CompareObjState(0, z190, 74, 0)
        CompareObjState(0, z190, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m20_21_x21(z186=_, z187=_):
    """[Execution] Elevator_Rise
    z186: Elevator OBJ instance ID
    z187: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z186, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z186, 30, 0)
    IsPlayerInsidePoint(8, z187, z187, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z186, 71)
    assert CompareObjStateId(z186, 40, 0)
    """State 4: End state"""
    return 0

def event_m20_21_x22(z186=_, z188=_):
    """[Execution] Elevator_Descent
    z186: Elevator OBJ instance ID
    z188: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z186, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z186, 41, 0)
    IsPlayerInsidePoint(8, z188, z188, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z186, 81)
    assert CompareObjStateId(z186, 10, 0)
    """State 4: End state"""
    return 0

def event_m20_21_x23(z224=_, z225=_, z226=_):
    """[Lib] [Preset] Elevator lever
    z224: OBJ instance ID of the elevator
    z225: Lever OBJ instance ID
    z226: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m20_21_x24()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m20_21_x25(z224=z224, z225=z225, z226=z226)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m20_21_x26(z224=z224, z225=z225, z226=z226)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m20_21_x27(z224=z224, z225=z225, z226=z226)
    """State 5: Rerun"""
    return 0

def event_m20_21_x24():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x25(z224=_, z225=_, z226=_):
    """[Condition] Elevator lever_use judgment
    z224: OBJ instance ID of the elevator
    z225: Lever OBJ instance ID
    z226: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z224, z226, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m20_21_x26(z224=_, z225=_, z226=_):
    """[Execution] Elevator lever_Key guide valid
    z224: OBJ instance ID of the elevator
    z225: Lever OBJ instance ID
    z226: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z225, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z224, z226, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x27(z224=_, z225=_, z226=_):
    """[Execute] Elevator lever_key guide disabled
    z224: OBJ instance ID of the elevator
    z225: Lever OBJ instance ID
    z226: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z225, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z224, z226, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x28(z222=221000015):
    """[Lib] [Reproduction] Elevator_Initialization
    z222: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(z222) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m20_21_x29():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m20_21_x30(z220=20213100, z221=40, z222=221000015, z223=40):
    """[Lib] [Execution] Elevator_Initialization
    z220: Elevator OBJ instance ID
    z221: Initial position OBJ state ID
    z222: Initialization completion flag
    z223: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z220, z221)
    assert CompareObjStateId(z220, z223, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z222, 1)
    """State 3: End state"""
    return 0

def event_m20_21_x31(z220=20213100, z221=40, z222=221000015, z223=40):
    """[Lib] [Preset] Elevator_Initialization
    z220: Elevator OBJ instance ID
    z221: Initial position OBJ state ID
    z222: Initialization completion flag
    z223: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m20_21_x28(z222=z222)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m20_21_x29()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m20_21_x30(z220=z220, z221=z221, z222=z222, z223=z223)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m20_21_x32(z99=_):
    """[Reproduction] Boss Battle_Poly Play Replay
    z99: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z99) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m20_21_x33(z214=20210607):
    """[Condition] Boss Battle_Poly Play Replay
    z214: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z214, 100, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x34(z98=_, z99=_, z100=_, z219=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z98: Poly play ID
    z99: Poly drama played flag
    z100: Warp point ID
    z219: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z98, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z99, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z100)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m20_21_x35(z214=20210607, z215=202110, z216=221000097, z217=1201000, z218=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z214: White door instance ID
    z215: Poly play ID
    z216: Poly drama played flag
    z217: Warp point ID
    z218: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m20_21_x32(z99=z216)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m20_21_x33(z214=z214)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m20_21_x34(z98=z215, z99=z216, z100=z217, z219=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_21_x36(z209=104160, z210=102421, z211=102422, z212=221020147, z213=103661):
    """[Lib] Appearance determination: General purpose
    z209: Death: Global event flag
    z210: Local emigration permission: Global event flag
    z211: Relocation permission after moving: Global event flag
    z212: Appearance determination: Area and other flags
    z213: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z209, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z210, 1)
            CompareEventFlag(8, z211, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z210, 1)
                CompareEventFlag(8, z213, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z212, 1)
                    CompareEventFlag(0, z212, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z212, 0)
                    CompareEventFlag(0, z212, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z212, 0)
        CompareEventFlag(0, z212, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m20_21_x37():
    """[Lib] [Reproduction] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x38(z204=20211600, z205=20, z206=100000, z207=0, z208=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z204: Object instance ID
    z205: OBJ state ID
    z206: Navimesh switching point ID
    z207: Additional attributes
    z208: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m20_21_x39(z204=z204, z205=z205, z206=z206, z208=z208, z207=z207)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m20_21_x40(z204=z204, z205=z205, z206=z206)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m20_21_x41(z204=z204, z205=z205, z206=z206, z207=z207, z208=z208)
    """State 4: End state"""
    return 0

def event_m20_21_x39(z204=20211600, z205=20, z206=100000, z208=2, z207=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z204: Target OBJ instance ID
    z205: Target OBJ state ID
    z206: Navimesh switching point ID
    z208: Additional attributes
    z207: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z204, z205, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z206, z208)
        DeleteNavimeshAttribute(z206, z207)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m20_21_x40(z204=20211600, z205=20, z206=100000):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z204: Target OBJ instance ID
    z205: Target OBJ state ID
    z206: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z204, z205, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x41(z204=20211600, z205=20, z206=100000, z207=0, z208=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z204: Target OBJ instance ID
    z205: Target OBJ state ID
    z206: Navimesh switching point ID
    z207: Additional attributes
    z208: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z206, z207)
    DeleteNavimeshAttribute(z206, z208)
    """State 2: End state"""
    return 0

def event_m20_21_x42():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x43(z191=504000, z192=20213100, z194=10, z195=20):
    """[Lib] [Condition] Elevator_Connection replacement
    z191: Replacement point
    z192: OBJ instance ID of the elevator
    z194: Top_Hit group ID
    z195: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z191, z191, 1)
    CompareObjState(8, z192, 70, 0)
    IsPlayerInsidePoint(9, z191, z191, 1)
    CompareObjState(9, z192, 80, 0)
    IsPlayerOnHitGroup(0, z194, 1)
    IsPlayerOnHitGroup(1, z195, 1)
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

def event_m20_21_x44(z191=504000, z193=105430, z196=0, z194=10, z192=20213100):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z191: Replacement point
    z193: Global flag for connection
    z196: ON / OFF of global flag
    z194: Top_Hit group ID
    z192: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z193, z196)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z191, z191, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z194, 1)
    IsPlayerInsidePoint(8, z191, z191, 1)
    CompareObjState(8, z192, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x45(z193=105430, z196=0, z194=10, z191=504000, z192=20213100):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z193: Global flag for connection
    z196: ON / OFF of global flag
    z194: Hit group ID
    z191: Replacement point ID
    z192: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z193, z196)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z194, 0)
    IsPlayerInsidePoint(8, z191, z191, 1)
    CompareObjState(8, z192, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x46(z191=504000, z192=20213100, z193=105430, z194=10, z195=20, z196=0, z197=1):
    """[Lib] [Preset] Elevator_Connection replacement
    z191: Replacement point
    z192: OBJ instance ID of the elevator
    z193: Global flag for connection
    z194: Top_Hit group ID
    z195: Bottom_Hit group ID
    z196: Up_Global flag when rising
    z197: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m20_21_x42()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m20_21_x43(z191=z191, z192=z192, z194=z194, z195=z195)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m20_21_x44(z191=z191, z193=z193, z196=z196, z194=z194, z192=z192)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m20_21_x49(z191=z191, z193=z193, z197=z197, z195=z195, z192=z192)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m20_21_x45(z193=z193, z196=z196, z194=z194, z191=z191, z192=z192)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m20_21_x48(z193=z193, z197=z197, z195=z195, z191=z191, z192=z192)
    """State 7: End state"""
    return 0

def event_m20_21_x47(z198=102431, z199=676, z200=104160, z201=63, z202=103660, z203=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z198: White Phantom can appear: Global event flag
    z199: White Phantom: Generator ID
    z200: Death: Global event flag
    z201: Body: Generator group ID
    z202: Hostile: Global event flag
    z203: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z199)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z200, 1)
        CompareEventFlag(1, z202, 1)
        CompareEventFlag(2, z198, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z199)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z200, 1)
            CompareEventFlag(1, z202, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z199)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z200, 1)
            CompareEventFlag(1, z202, 1)
            HasNpcPhantomSpawned(2, z199, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z201, 0)
                HasNpcPhantomSpawned(0, z199, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z199)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m20_21_x48(z193=105430, z197=1, z195=20, z191=504000, z192=20213100):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z193: Global flag for connection
    z197: ON / OFF of global flag
    z195: Hit group ID
    z191: Replacement point ID
    z192: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z193, z197)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z195, 0)
    IsPlayerInsidePoint(8, z191, z191, 1)
    CompareObjState(8, z192, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x49(z191=504000, z193=105430, z197=1, z195=20, z192=20213100):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z191: Replacement point
    z193: Global flag for connection
    z197: ON / OFF of global flag
    z195: Bottom_Hit group ID
    z192: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z193, z197)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z191, z191, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z195, 1)
    IsPlayerInsidePoint(8, z191, z191, 1)
    CompareObjState(8, z192, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x50(z186=_, z187=_):
    """[Execution] Elevator_Return switch after lift
    z186: Elevator OBJ instance ID
    z187: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z186, 30, 0)
    IsPlayerInsidePoint(8, z187, z187, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z186, 71)
    assert CompareObjStateId(z186, 40, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x51(z186=_, z188=_):
    """[Execution] Elevator_Return switch after descending
    z186: Elevator OBJ instance ID
    z188: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z186, 41, 0)
    IsPlayerInsidePoint(8, z188, z188, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z186, 81)
    assert CompareObjStateId(z186, 10, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x52(z179=102316, z180=102323, z181=102331, z182=102333, z183=102315, z184=102317, z185=103623):
    """[Lib] NPC: Shenzhen Pilgrims: Appearance Judgment
    z179: Generation stop: Global event flag
    z180: Appearance permission: Global event flag
    z181: Sub 1 encountering: Global event flag
    z182: During sub-2 encounter: Global event flag
    z183: Sub 1 generation stop: Global event flag
    z184: Sub 2 generation stop: Global event flag
    z185: Hostile map: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, 104120, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 7: Appearance determination: Pledge determination"""
            CompareEventFlag(8, 102321, 1)
            CompareEventFlag(8, 103621, 0)
            CompareEventFlag(8, 103622, 0)
            CompareEventFlag(8, 103623, 0)
            if ConditionGroup(8):
                pass
            else:
                """State 4: Appearance determination: Generation stop determination"""
                CompareEventFlag(0, z179, 1)
                if ConditionGroup(0):
                    pass
                else:
                    """State 8: Appearance determination: Adversity determination"""
                    CompareEventFlag(0, 103621, 1)
                    CompareEventFlag(1, 103622, 1)
                    CompareEventFlag(2, 103623, 1)
                    if ConditionGroup(0):
                        pass
                    elif ConditionGroup(1):
                        pass
                    elif ConditionGroup(2):
                        pass
                    else:
                        """State 9: Appearance determination: Judgment while encountering other maps"""
                        CompareEventFlag(8, z181, 1)
                        CompareEventFlag(8, z183, 0)
                        CompareEventFlag(9, z182, 1)
                        CompareEventFlag(9, z184, 0)
                        if ConditionGroup(8):
                            pass
                        elif ConditionGroup(9):
                            pass
                        else:
                            Goto('L0')
                """State 5: Appearance judgment: Appearance impossible"""
                SetEventFlag(z180, 0)
                CompareEventFlag(0, z180, 0)
                assert ConditionGroup(0)
                Goto('L1')
            """State 6: Appearance determination: Appearance allowed"""
            Label('L0')
            SetEventFlag(z180, 1)
            CompareEventFlag(0, z180, 1)
            assert ConditionGroup(0)
    """State 3: Appearance determination: System: End"""
    Label('L1')
    EndMachine()

def event_m20_21_x53(z178=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z178: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z178)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m20_21_x54(z173=104160, z174=678, z175=104160, z176=103660, z177=63):
    """[Lib] NPC white phantom appearance: General purpose: OFF
    z173: White Phantom can appear: Global event flag
    z174: White Phantom: Generator ID
    z175: Death: Global event flag
    z176: Hostile: Global event flag
    z177: Body: Generator group ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z174)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z175, 1)
        CompareEventFlag(1, z176, 1)
        CompareEventFlag(2, z173, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z174)
            """State 7: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z175, 1)
            CompareEventFlag(1, z176, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 8: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z174)
            """State 4: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z175, 1)
            CompareEventFlag(1, z176, 1)
            HasNpcPhantomSpawned(2, z174, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 5: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z177, 0)
                HasNpcPhantomSpawned(0, z174, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 9: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z174)
    """State 10: Appearance: System: End"""
    EndMachine()

def event_m20_21_x55():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x56(z171=_, z172=_):
    """[Lib] [execute] Rebirth fire
    z171: Flag start ID
    z172: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z171, z172, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x57():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x58(z171=_, z172=_):
    """[Lib] [Preset] Rebirth
    z171: Flag start ID
    z172: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m20_21_x55()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m20_21_x57()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m20_21_x56(z171=z171, z172=z172)
    """State 4: End state"""
    return 0

def event_m20_21_x59(z167=_, z168=102436, z169=205, z170=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z167: Defeat Boss 1: Area and other flags
    z168: Summon Achievement: Global Event Flag
    z169: Summon achievement count: global variable
    z170: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z168, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z167, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z169, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z169, NpcInfoValue(z170, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z168, 1)
                CompareEventFlag(0, z168, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m20_21_x60(z161=102810, z162=10002000, z163=670, z164=104340, z165=0, z166=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z161: Summoning conditions: Global event flag
    z162: Summon range
    z163: Generator ID
    z164: Death: Global event flag
    z165: Appearance: Minimum time
    z166: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z164, 1)
        CompareEventFlag(8, z161, 1)
        IsPlayerInsidePoint(8, z162, z162, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z164, 1)
            CompareStateTime(1, z165, 3, z166)
            IsPlayerInsidePoint(2, z162, z162, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z163)
                HasNpcPhantomSpawned(0, z163, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m20_21_x61(z157=10001000, z158=671, z159=0, z160=1):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z157: Summon range
    z158: Generator ID
    z159: Appearance: Minimum time
    z160: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z157, z157, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z159, 3, z160)
        IsPlayerInsidePoint(1, z157, z157, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z158)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m20_21_x62(z155=_, z156=_):
    """[Lib] [Preset] Get trophy
    z155: Acquisition trigger_other flags
    z156: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z155) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z155, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z156)
    """State 4: End state"""
    return 0

def event_m20_21_x63(z150=102010, z151=677, z152=104000, z153=103500, z154=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z150: White Phantom can appear: Global event flag
    z151: White Phantom: Generator ID
    z152: Death: Global event flag
    z153: Hostile: Global event flag
    z154: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z151)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z152, 1)
        CompareEventFlag(1, z153, 1)
        CompareEventFlag(2, z150, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z151)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z152, 1)
            CompareEventFlag(1, z153, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z151)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z152, 1)
            CompareEventFlag(1, z153, 1)
            HasNpcPhantomSpawned(2, z151, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z151, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z151)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m20_21_x64(z148=40, z149=104123):
    """[Lib] NPC: Death Determination: Shenzhen Pilgrim
    z148: Generator ID
    z149: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z149, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z148)
            IsChrDead(8, z148)
            CompareEventFlag(8, 102321, 1)
            if ConditionGroup(8):
                """State 6: Death determination: All death flag set"""
                SetEventFlag(104121, 1)
                SetEventFlag(104122, 1)
                SetEventFlag(104123, 1)
                CompareEventFlag(8, 104121, 1)
                CompareEventFlag(8, 104122, 1)
                CompareEventFlag(8, 103623, 1)
                assert ConditionGroup(8)
            elif ConditionGroup(0):
                """State 5: Death determination: death flag setting"""
                SetEventFlag(z149, 1)
                CompareEventFlag(0, z149, 1)
                assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m20_21_x65(z146=505000, z147=3):
    """[Lib] [Preset] [Asynchronous] Player forced fall death
    z146: Point ID
    z147: Fall time
    """
    """State 0,1: [Lib] [Reproduction] Dummy_SubState"""
    assert event_m20_21_x37()
    """State 2: [Lib] [Condition] [Asynchronous] Player forced fall death_SubState"""
    assert event_m20_21_x66(z146=z146, z147=z147)
    """State 3: [Lib] [Execution] [Asynchronous] Player forced fall death_SubState"""
    assert event_m20_21_x67()
    """State 4: End state"""
    return 0

def event_m20_21_x66(z146=505000, z147=3):
    """[Lib] [Condition] [Asynchronous] Player forced fall death
    z146: Point ID
    z147: Fall time
    """
    """State 0,1: Judgment"""
    IsPlayerInsidePoint(8, z146, z146, 1)
    ComparePlayerFallTime(8, z147, 3)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_21_x67():
    """[Lib] [execution] [asynchronous] Player forced fall death"""
    """State 0,1: Fall death request"""
    PlayerDeathRequest(0)
    """State 2: End state"""
    return 0

def event_m20_21_x68():
    """[Lib] [Reproduction] Switch the connection flag at the point"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m20_21_x69(z141=506000, z142=506000):
    """[Lib] [Condition] Switch the connection flag at the point
    z141: Start point ID
    z142: End point ID
    """
    """State 0,1: Are you in point?"""
    IsPlayerInsidePoint(0, z141, z142, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x70(z143=105430, z144=0, z145=1):
    """[Lib] [Execution] Switch to the connection flag at the point
    z143: Global event flag for connection
    z144: Flag switching
    z145: Wait for next judgment
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z143, z144)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z143, z144)
    assert ConditionGroup(0)
    """State 3: For next judgment: Has the flag changed?"""
    CompareEventFlag(0, z143, z145)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x71(z141=506000, z142=506000, z143=105430, z144=0, z145=1):
    """[Lib] [Preset] Switch the connection flag at the point
    z141: Start point ID
    z142: End point ID
    z143: Global event flag for connection
    z144: Flag switching
    z145: Wait for next judgment
    """
    """State 0,1: [Lib] [Reproduction] Switch the connection flag at the point _SubState"""
    call = event_m20_21_x68()
    if call.Get() == 0:
        """State 3: [Lib] [Condition] Switch connection flag at point _SubState"""
        assert event_m20_21_x69(z141=z141, z142=z142)
        """State 2: [Lib] [Execution] Switch to the connection flag at the point _SubState"""
        assert event_m20_21_x70(z143=z143, z144=z144, z145=z145)
        """State 4: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 5: Guest: Exit"""
        return 1

def event_m20_21_x72(z136=10001000, z137=671, z138=104320, z139=0, z140=1):
    """[Lib] [BEST] NPC Black Phantom Appearance: Online: Miracle Person _ When Living
    z136: Summon range
    z137: Generator ID
    z138: Death: Global event flag
    z139: Appearance: Minimum time
    z140: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z138, 1)
        IsPlayerInsidePoint(1, z136, z136, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z138, 1)
            CompareStateTime(1, z139, 3, z140)
            IsPlayerInsidePoint(2, z136, z136, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z137)
                HasNpcPhantomSpawned(0, z137, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m20_21_x73(z119=221020043, z121=221000044):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z119: Lottery determination flag
    z121: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z121) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z119) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m20_21_x74(z120=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z120: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z120, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m20_21_x75(z119=221020043, z122=3, z123=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z119: Lottery determination flag
    z122: Number of appearance judgment points
    z123: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z119, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z122)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z123, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m20_21_x76(z119=221020043, z120=14, z121=221000044, z122=3, z123=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z119: Lottery determination flag
    z120: Random number comparison value
    z121: Defeat flag
    z122: Number of appearance judgment points
    z123: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m20_21_x73(z119=z119, z121=z121)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m20_21_x74(z120=z120)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m20_21_x75(z119=z119, z122=z122, z123=z123)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m20_21_x89(z119=z119, z123=z123)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m20_21_x77(val2=_, z133=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z133: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z133) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m20_21_x78(z129=_, z130=0, z131=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z129: Appearance judgment point ID
    z130: Minimum appearance time
    z131: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z129, z129, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z130, 3, z131)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m20_21_x79(z132=968, z134=_, z135=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z132: Generator ID
    z134: Appearance start point ID
    z135: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z132, z134, z135)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z132)
    """State 4: Finish"""
    return 0

def event_m20_21_x80(z126=221000044):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z126: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z126) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m20_21_x81(z129=_, z130=0, z131=5, z132=968, val2=_, z133=10, z134=_, z135=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z129: Intrusion detection point ID
    z130: Minimum appearance time
    z131: Maximum time to appear
    z132: Generator ID
    val2: Appearance judgment number
    z133: Lottery result point variable
    z134: Appearance start point ID
    z135: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m20_21_x77(val2=val2, z133=z133)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m20_21_x78(z129=z129, z130=z130, z131=z131)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m20_21_x79(z132=z132, z134=z134, z135=z135)
    """State 4: Finish"""
    return 0

def event_m20_21_x82(z127=968, mode4=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z127: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z127)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode4) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m20_21_x83(z126=221000044, z128=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z126: Defeat flag
    z128: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z126, 1)
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
                    SetEventFlag(z128, 1)
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

def event_m20_21_x84(z126=221000044, z127=968, mode4=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z126: Defeat flag
    z127: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m20_21_x80(z126=z126)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m20_21_x82(z127=z127, mode4=mode4)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m20_21_x83(z126=z126, z128=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m20_21_x83(z126=z126, z128=102755)
    """State 5: End state"""
    return 0

def event_m20_21_x85(z124=_, z125=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z124: Generator ID
    z125: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z124, z125)
    """State 2: End state"""
    return 0

def event_m20_21_x86(z124=_, z125=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z124: Generator ID
    z125: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z124, z125, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_21_x87(z124=_):
    """[Lib] [DC] [Condition] Transparent characters
    z124: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z124)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x88(z124=_, z125=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z124: Generator ID
    z125: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m20_21_x86(z124=z124, z125=z125)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m20_21_x87(z124=z124)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m20_21_x85(z124=z124, z125=z125)
    """State 4: End state"""
    return 0

def event_m20_21_x89(z119=221020043, z123=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z119: Lottery determination flag
    z123: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z119, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z123, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x90(z116=221000086):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z116: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z116) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_21_x91(z117=825):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z117: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z117, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x92(z118=221020088):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z118: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z118, 1)
    """State 2: End state"""
    return 0

def event_m20_21_x93(z116=221000086, z117=825, z118=221020088):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z116: Boss destruction flag
    z117: Boss generator ID
    z118: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m20_21_x90(z116=z116)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m20_21_x91(z117=z117)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m20_21_x92(z118=z118)
    """State 4: End state"""
    return 0

def event_m20_21_x94(z112=_, z113=_, z114=6.7, z115=_):
    """[Reproduction] Golem door
    z112: Golem door instance ID
    z113: A flag to determine if the golem door has absorbed soul
    z114: Distance that golem door absorbs soul
    z115: Point ID for Navimesh change
    """
    """State 0,1: Is the door OBJ open?"""
    if CompareObjStateId(z112, 20, 0):
        """State 3: Navigation mesh change"""
        DeleteNavimeshAttribute(z115, 2)
        """State 5: Opened"""
        return 1
    else:
        """State 2: Absorption processing in Seoul"""
        AddSoulAcquisitionTarget(z112, z114, z113, 1, -1)
        """State 4: Not open"""
        return 0

def event_m20_21_x95(z113=_):
    """[Condition] Golem door
    z113: A flag to determine if the golem door has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z113, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x96(z112=_, z115=_):
    """[Execution] Golem door
    z112: Golem door instance ID
    z115: Point ID for Navimesh change
    """
    """State 0,1: OBJ state transition: door"""
    ChangeObjState(z112, 70)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z115, 2)
    """State 3: End state"""
    return 0

def event_m20_21_x97(z112=_, z113=_, z114=6.7, z115=_):
    """[Preset] Golem door
    z112: Golem door instance ID
    z113: A flag to determine if the golem door has absorbed soul
    z114: Distance that golem door absorbs soul
    z115: Point ID for Navimesh change
    """
    """State 0,1: Disable OBJ synchronization"""
    SetObjSync(z112, 0)
    """State 2: [Reproduction] Golem door_SubState"""
    call = event_m20_21_x94(z112=z112, z113=z113, z114=z114, z115=z115)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Condition] Golem door_SubState"""
        assert event_m20_21_x95(z113=z113)
        """State 4: [Execution] Golem door_SubState"""
        assert event_m20_21_x96(z112=z112, z115=z115)
    """State 5: End state"""
    return 0

def event_m20_21_x98(z33=20210406, z34=900000, z35=221000021):
    """[Preset] King's door
    z33: Instance ID of king's door OBJ
    z34: Point ID for changing navigation
    z35: Opening flag
    """
    """State 0,1: [Reproduction] King's door_SubState"""
    call = event_m20_21_x99(z33=z33, z34=z34)
    if call.Get() == 1:
        """State 4: [Condition] King's door_SubState"""
        call = event_m20_21_x102(z33=z33, z35=z35)
        if call.Get() == 1:
            """State 3: [Execution] King's Door_Open_SubState"""
            assert event_m20_21_x101(z33=z33, z34=z34, z35=z35)
        elif call.Get() == 0:
            """State 2: [Execution] King's door_Do not open_SubState"""
            assert event_m20_21_x100(z33=z33)
            """State 7: Rerun"""
            return 0
    elif call.Get() == 0:
        pass
    elif call.Get() == 2:
        """State 6: [Condition] King's door_Guest_SubState"""
        assert event_m20_21_x181(z33=z33)
        """State 5: [Execution] King's Door_Guest_SubState"""
        assert event_m20_21_x182(z34=z34)
    """State 8: Finish"""
    return 1

def event_m20_21_x99(z33=20210406, z34=900000):
    """[Reproduction] King's door
    z33: Instance ID of king's door OBJ
    z34: Point ID for changing navigation
    """
    """State 0,1: Determining the state of the king's door"""
    if CompareObjStateId(z33, 30, 0):
        pass
    elif CompareObjStateId(z33, 70, 0):
        """State 2: Waiting for the door to open"""
        assert CompareObjStateId(z33, 30, 0)
    else:
        """State 4: Host?"""
        if IsGuest() != 1:
            """State 6: host"""
            return 1
        else:
            """State 7: The guests"""
            return 2
    """State 3: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z34, 2)
    """State 5: Finish"""
    return 0

def event_m20_21_x100(z33=20210406):
    """[Execution] King's door_Do not open
    z33: Instance ID of king's door OBJ
    """
    """State 0,1: Event message display"""
    # action:2000:"Produce the symbol of the King"
    DisplayEventMessage(2000, 0, 0, 0)
    """State 2: Equipped with an or ring away from the king's door?"""
    CompareObjPlayerDistance(0, z33, 10, 3)
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x101(z33=20210406, z34=900000, z35=221000021):
    """[Execution] King's door_Open
    z33: Instance ID of king's door OBJ
    z34: Point ID for changing navigation
    z35: Opening flag
    """
    """State 0,1: Opening flag ON King's door opens"""
    SetEventFlag(z35, 1)
    ChangeObjState(z33, 70)
    """State 2: Waiting for the door to open"""
    CompareObjState(0, z33, 30, 0)
    assert ConditionGroup(0)
    """State 3: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z34, 2)
    """State 4: End state"""
    return 0

def event_m20_21_x102(z33=20210406, z35=221000021):
    """[Condition] King's door
    z33: Instance ID of king's door OBJ
    z35: Opening flag
    """
    """State 0,2: Did you approach the king's door?"""
    CompareObjPlayerDistance(0, z33, 3, 5)
    assert ConditionGroup(0)
    """State 1: Is it equipped with a king's ring? Has it been opened?"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    SetConditionGroup(0, 8)
    # goods:40510000:King's Ring
    DoesPlayerHaveItem(8, 40510000, 1, 3, 1, 1, 0)
    CompareEventFlag(8, z35, 1)
    if ConditionGroup(0):
        """State 4: Equipped with a king's ring"""
        return 1
    else:
        """State 3: Not qualified"""
        return 0

def event_m20_21_x103():
    """[Reproduction] Acid spitting dragon statue _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x104(z110=_, z111=4):
    """[Condition] Statue of a dragon that spits acid
    z110: Statue instance ID
    z111: Reaction sound level
    """
    """State 0,1: Did you hear a sound nearby?"""
    CheckObjHeardSound(0, z110, z111, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x105(z110=_, mode3=1):
    """[Execution] Statue of dragon spitting acid
    z110: Statue instance ID
    mode3: Cool time
    """
    """State 0,1: OBJ state transition request: Statue: 70"""
    ChangeObjState(z110, 70)
    """State 3: Waiting for the end of firing"""
    assert CompareObjStateId(z110, 10, 0)
    """State 2: Cool time"""
    assert (GetStateTime() > mode3) != 0
    """State 4: End state"""
    return 0

def event_m20_21_x106(z110=_, z111=4, mode3=1):
    """[Preset] Acid spitting dragon statue
    z110: Statue instance ID
    z111: Reaction sound level
    mode3: Cool time
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z110, 0)
    """State 2: [Reproduction] Statue of dragon spitting acid_Sky_SubState"""
    assert event_m20_21_x103()
    """State 3: [Condition] Dragon _SubState that spits acid"""
    assert event_m20_21_x104(z110=z110, z111=z111)
    """State 4: [Execution] Statue of dragon spitting acid _SubState"""
    assert event_m20_21_x105(z110=z110, mode3=mode3)
    """State 5: End state"""
    return 0

def event_m20_21_x107(z55=_, z109=30, z57=_, z58=7.5):
    """[Reproduction] Golem_Main Gate
    z55: Golem instance ID
    z109: State ID to be initialized
    z57: Flag that determines if the golem has absorbed soul
    z58: The distance a golem absorbs soul
    """
    """State 0,1: Golem already activated?"""
    if CompareObjStateId(z55, 20, 0):
        """State 5: Activated"""
        return 1
    elif CompareObjStateId(z55, 72, 0):
        """State 6: Seoul absorbed"""
        Label('L0')
        return 2
    elif CompareObjStateId(z55, 70, 0):
        Goto('L0')
    else:
        """State 2: Golem OBJ state initialization"""
        ChangeObjState(z55, z109)
        assert CompareObjStateId(z55, z109, 0)
        """State 3: Absorption processing in Seoul"""
        AddSoulAcquisitionTarget(z55, z58, z57, 1, -1)
        """State 4: Not started"""
        return 0

def event_m20_21_x108(z55=_, z56=_):
    """[Execution] Golem_Main Gate
    z55: Golem instance ID
    z56: Lever instance ID
    """
    """State 0,3: OBJ state transition: Golem operation"""
    ChangeObjState(z55, 70)
    """State 4: Has Golem's Soul Absorption Anime finished?"""
    CompareObjState(0, z55, 72, 0)
    assert ConditionGroup(0)
    """State 1: OBJ state transition: lever operation"""
    ChangeObjState(z56, 70)
    """State 2: Lever OBJ transition standby"""
    CompareObjState(0, z56, 20, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m20_21_x109(z55=_, z56=_, z57=_, z58=7.5):
    """[Preset] Golem_Main Gate
    z55: Golem instance ID
    z56: Lever instance ID
    z57: Flag that determines if the golem has absorbed soul
    z58: The distance a golem absorbs soul
    """
    """State 0,1: Disable OBJ synchronization"""
    SetObjSync(z55, 0)
    SetObjSync(z56, 0)
    """State 2: [Reproduction] Golem_Main Gate_SubState"""
    call = event_m20_21_x107(z55=z55, z109=30, z57=z57, z58=z58)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 5: [Execution] Golem_Main Gate_Seoul Absorbed_SubState"""
        assert event_m20_21_x169(z55=z55, z56=z56)
    elif call.Done():
        """State 4: [Condition] Golem_Main Gate_SubState"""
        assert event_m20_21_x168(z57=z57)
        """State 3: [Execution] Golem_Main Gate_SubState"""
        assert event_m20_21_x108(z55=z55, z56=z56)
    """State 6: End state"""
    return 0

def event_m20_21_x110(z104=20211530, z105=20211540, z101=20212520, z106=7.5, z107=221000010, z108=221000032):
    """[Reproduction] Golem for elevator
    z104: Elevator lower lever_OBJ instance ID
    z105: Elevator upper lever_OBJ instance ID
    z101: Golem instance ID
    z106: The distance a golem absorbs soul
    z107: Elevator start flag
    z108: Flag that determines if the golem has absorbed soul
    """
    """State 0,2: Invalid lever for elevator"""
    DisableObjKeyGuide(z104, 1)
    DisableObjKeyGuide(z105, 1)
    """State 1: Is the elevator started?"""
    if GetEventFlag(z107) != 0:
        """State 7: [Rescue] Is the golem in the initial state? _2"""
        if CompareObjStateId(z101, 10, 0):
            pass
        else:
            """State 9: Activated"""
            return 1
    else:
        """State 5: Has Golem absorbed Seoul?"""
        if GetEventFlag(z108) != 0:
            """State 6: [Rescue] Is the golem in the initial state?"""
            if CompareObjStateId(z101, 10, 0):
                pass
            else:
                """State 10: Seoul absorbed"""
                return 2
        else:
            pass
    """State 3: Golem OBJ state initialization"""
    ChangeObjState(z101, 30)
    assert CompareObjStateId(z101, 30, 0)
    """State 4: Absorption processing in Seoul"""
    AddSoulAcquisitionTarget(z101, z106, z108, 1, -1)
    """State 8: End state"""
    return 0

def event_m20_21_x111(z101=20212520, z108=221000032):
    """[Condition] Elevator golem activation
    z101: Golem instance ID
    z108: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z108, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x112(z101=20212520, z102=20212620, z103=20213110, z104=20211530, z105=20211540, z107=221000010):
    """[Execution] Golem for elevator
    z101: Golem OBJ instance ID
    z102: OBJ instance ID of the lever
    z103: OBJ instance ID of the elevator
    z104: Elevator bottom_lever OBJ instance ID
    z105: Elevator top_lever OBJ instance ID
    z107: Elevator start flag
    """
    """State 0,5: Golem state determination"""
    if CompareObjStateId(z101, 30, 0):
        """State 6: OBJ state transition: Golem operation"""
        ChangeObjState(z101, 70)
        assert CompareObjStateId(z101, 30, 1)
    else:
        pass
    """State 7: Has Golem's Soul Absorption Anime finished?"""
    CompareObjState(0, z101, 70, 1)
    assert ConditionGroup(0)
    """State 12: Judgment of lever status"""
    if CompareObjStateId(z102, 20, 1):
        """State 13: Lever initialization"""
        InitializeObj(z102)
        assert (GetStateTime() >= 0) != 0
        """State 8: OBJ state transition: lever operation"""
        ChangeObjState(z102, 70)
    else:
        pass
    """State 2: Golem lever OBJ transition waiting"""
    CompareObjState(0, z102, 20, 0)
    assert ConditionGroup(0)
    """State 11: Elevator state judgment"""
    if CompareObjStateId(z103, 40, 0):
        """State 3: Move the elevator down"""
        ChangeObjState(z103, 80)
    else:
        pass
    """State 9: Elevator OBJ transition standby"""
    CompareObjState(0, z103, 41, 0)
    assert ConditionGroup(0)
    """State 10: Return the elevator switch"""
    ChangeObjState(z103, 81)
    """State 4: Elevator lever activation"""
    DisableObjKeyGuide(z105, 0)
    """State 1: Flag ON"""
    SetEventFlag(z107, 1)
    """State 14: End state"""
    return 0

def event_m20_21_x113(z101=20212520, z102=20212620, z103=20213110, z104=20211530, z105=20211540, z106=7.5,
                      z107=221000010, z108=221000032):
    """[Preset] Golem for elevator
    z101: Golem OBJ instance ID
    z102: OBJ instance ID of the lever
    z103: OBJ instance ID of the elevator
    z104: Elevator lower lever_OBJ instance ID
    z105: Elevator upper lever_OBJ instance ID
    z106: The distance a golem absorbs soul
    z107: Elevator start flag
    z108: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: [Reproduction] Elevator Golem Activation_SubState"""
    call = event_m20_21_x110(z104=z104, z105=z105, z101=z101, z106=z106, z107=z107, z108=z108)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 3: [Execution] Golem activation for elevators_SubState"""
        Label('L0')
        assert event_m20_21_x112(z101=z101, z102=z102, z103=z103, z104=z104, z105=z105, z107=z107)
    elif call.Done():
        """State 2: [Condition] Elevator golem activation_SubState"""
        assert event_m20_21_x111(z101=z101, z108=z108)
        Goto('L0')
    """State 4: End state"""
    return 0

def event_m20_21_x114(z51=20212000, z52=20211520, z53=20210410, z54=300000):
    """[Reproduction] Lever door between soldiers
    z51: Instance ID of the iron lattice OBJ
    z52: Lever OBJ instance ID
    z53: Door OBJ instance ID
    z54: Navimesh change point ID
    """
    """State 0,1: Disable key guide of door OBJ"""
    DisableObjKeyGuide(z53, 1)
    """State 2: Judgment of lever OBJ status"""
    if CompareObjStateId(z52, 20, 0):
        pass
    else:
        Goto('L0')
    """State 3: State determination of iron lattice OBJ"""
    if CompareObjStateId(z51, 20, 0):
        """State 4: Enable key guide for door OBJ"""
        DisableObjKeyGuide(z53, 0)
        """State 5: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z54, 2)
        """State 7: Activated"""
        return 1
    else:
        """State 8: Only lever is activated"""
        return 2
    """State 6: Not started"""
    Label('L0')
    return 0

def event_m20_21_x115(z52=20211520):
    """[Condition] Lever door between soldiers
    z52: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z52, 72, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x116(z51=20212000, z53=20210410, z54=300000):
    """[Execution] Lever door between soldiers
    z51: Instance ID of the iron lattice OBJ
    z53: Door OBJ instance ID
    z54: Navimesh change point ID
    """
    """State 0,1: Animation reproduction of iron lattice OBJ"""
    ChangeObjState(z51, 70)
    """State 3: Has the iron bar opened?"""
    CompareObjState(0, z51, 20, 0)
    assert ConditionGroup(0)
    """State 4: Enable key guide for door OBJ"""
    DisableObjKeyGuide(z53, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z54, 2)
    """State 5: End state"""
    return 0

def event_m20_21_x117():
    """[Reproduction] White door management during fire-joining"""
    """State 0,1: Event ends for guests"""
    if IsGuest() != 0:
        """State 3: Simple end"""
        return 1
    else:
        """State 2: Event start"""
        return 0

def event_m20_21_x118():
    """[Condition] White door management during fire-joining"""
    """State 0,4: Did you defeat Andyel?"""
    if GetEventFlag(221000006) != 0 and GetEventFlag(221000094) != 0:
        pass
    elif GetEventFlag(221000006) != 0:
        """State 6: White door display"""
        Label('L0')
        return 1
    else:
        """State 3: Did you defeat the queen?"""
        if GetEventFlag(221000096) != 0 and GetEventFlag(221000094) != 0:
            pass
        elif GetEventFlag(221000096) != 0:
            Goto('L0')
        else:
            """State 1: Did you defeat the Giant King?"""
            if GetEventFlag(100972) != 0:
                Goto('L0')
            else:
                """State 2: Did you defeat the Queen Knight AC?"""
                if GetEventFlag(221000091) != 1:
                    Goto('L0')
                else:
                    pass
    """State 5: White door hidden"""
    return 0

def event_m20_21_x119():
    """[Execution] White door management during display"""
    """State 0,1: White door control flag switching"""
    SetEventFlag(221000092, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x120():
    """[Preset] White door management during fire-joining"""
    """State 0,1: [Reproduction] White door management during fire-joining_SubState"""
    call = event_m20_21_x117()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] White door management during fire-joining_SubState"""
        call = event_m20_21_x118()
        if call.Get() == 1:
            """State 3: [Execution] White door management during firefighting_Display_SubState"""
            assert event_m20_21_x119()
        elif call.Get() == 0:
            """State 4: [Execution] White door management during fire-joining_hidden_SubState"""
            assert event_m20_21_x121()
    """State 5: End state"""
    return 0

def event_m20_21_x121():
    """[Execution] White door management during fire brigade_hidden"""
    """State 0,1: White door control flag switching"""
    SetEventFlag(221000092, 1)
    """State 2: End state"""
    return 0

def event_m20_21_x122(z11=100972, z12=221000091):
    """[Reproduction] Boss Battle Start_Queen Knight
    z11: Global flag for determining the destruction of giants
    z12: Other flags for queen knight AC destruction determination
    """
    """State 0,5: Already finished?"""
    if GetEventFlag(221000094) != 0:
        pass
    else:
        Goto('L0')
    """State 11: Ended"""
    return 5
    """State 3: Andyel single battle?"""
    Label('L0')
    if GetEventFlag(100747) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(221000096) != 0:
        pass
    else:
        Goto('L1')
    """State 9: To the Anderel single battle"""
    return 3
    """State 4: Queen and Andyel?"""
    Label('L1')
    if (GetEventFlag(100747) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(221000096) != 1 and
        GetEventFlag(z11) != 0 and GetEventFlag(z12) != 0):
        pass
    else:
        Goto('L2')
    """State 10: To the second battle of Andyel"""
    return 4
    """State 1: Queen single battle?"""
    Label('L2')
    if GetEventFlag(z11) != 0 and GetEventFlag(z12) != 0:
        pass
    else:
        Goto('L3')
    """State 6: To Queen A"""
    return 0
    """State 2: Destroyed Knight AC?"""
    Label('L3')
    if GetEventFlag(z12) != 0:
        """State 7: Simple end"""
        return 1
    else:
        """State 8: End state"""
        return 2

def event_m20_21_x123(z6=1100000, z7=1100000, z8=102, z9=1021020, z10=221020090, z11=100972, z12=221000091,
                      z13=1021021):
    """[Preset] Boss Battle: Queen Knight
    z6: Start point ID
    z7: End point ID
    z8: Sound ID
    z9: Boss Battle ID
    z10: Other flags for logic
    z11: Global flag for determining the destruction of giants
    z12: Other flags for queen knight AC destruction determination
    z13: Boss Battle ID (for consecutive battles)
    """
    """State 0,1: [Reproduction] Boss Battle Start_Queen's Knight_SubState"""
    call = event_m20_21_x122(z11=z11, z12=z12)
    if call.Get() == 5:
        pass
    elif call.Get() == 3:
        Goto('L0')
    elif call.Get() == 4:
        Goto('L1')
    elif call.Get() == 0:
        Goto('L2')
    elif call.Get() == 1:
        Goto('L3')
    elif call.Done():
        Goto('L4')
    """State 22: Ended: Finished"""
    return 7
    """State 19: To Andyel"""
    Label('L0')
    return 4
    """State 21: To the second battle of Andyel"""
    Label('L1')
    return 6
    """State 16: To Queen A"""
    Label('L2')
    return 1
    """State 15: Simple end"""
    Label('L3')
    return 0
    """State 8: [Condition] Boss Battle Start_Queen's Knight_SubState"""
    Label('L4')
    call = event_m20_21_x149(z6=z6, z7=z7, z11=z11)
    if call.Get() == 3:
        pass
    elif call.Get() == 4:
        """State 18: To battle with the queen"""
        Label('L5')
        return 3
    elif call.Get() == 5:
        """State 20: Three consecutive battles until Andel"""
        Label('L6')
        return 5
    elif call.Get() == 0:
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m20_21_x14(z93=z8, z94=z9, z95=z10)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 4: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z20=z9)
        """State 12: [Execution] Boss Battle_End_Queen Knight_SubState"""
        assert event_m20_21_x202(z8=z8, z9=z9, z10=z10, mode1=0)
    elif call.Get() == 1:
        """State 5: [Execution] Boss Battle_Start (Consecutive Battle) _SubState"""
        assert event_m20_21_x14(z93=z8, z94=z13, z95=z10)
        """State 6: [Reproduction] Boss Battle_Sky (Sequential Battle) _SubState"""
        assert event_m20_21_x15()
        """State 7: [Condition] Boss Battle_End Judgment (Consecutive Battle) _SubState"""
        assert event_m20_21_x16(z20=z13)
        """State 13: [Execution] Boss Battle_End_Queen's Knight (Continuous Battle) _SubState"""
        assert event_m20_21_x202(z8=z8, z9=z13, z10=z10, mode1=0)
        Goto('L5')
    elif call.Get() == 2:
        """State 9: [Execution] Boss Battle_Start (Consecutive Battle) _2_SubState"""
        assert event_m20_21_x14(z93=z8, z94=z13, z95=z10)
        """State 10: [Reproduction] Boss Battle_Sky (Sequence) _2_SubState"""
        assert event_m20_21_x15()
        """State 11: [Condition] Boss Battle_End Judgment (Consecutive Battle) _2_SubState"""
        assert event_m20_21_x16(z20=z13)
        """State 14: [Execution] Boss Battle_End_Queen Knight (Consecutive Battle) _2_SubState"""
        assert event_m20_21_x202(z8=z8, z9=z13, z10=z10, mode1=0)
        Goto('L6')
    """State 17: Single battle ended"""
    return 2

def event_m20_21_x124():
    """[Condition] Poly drama _ Princess Battle B"""
    """State 0,2: Defeated Knight AC?"""
    CompareEventFlag(0, 221000091, 1)
    assert ConditionGroup(0)
    """State 3: Has the giant king been defeated?"""
    CompareEventFlag(0, 100972, 0)
    if ConditionGroup(0):
        """State 7: Simple end"""
        return 1
    else:
        """State 1: For time"""
        assert (GetStateTime() > 5) != 0
        """State 4: Wait for one-shot BGM stop"""
        assert LastOneShotBgmIsPlaying(60, not 1)
        """State 5: Host arbitration"""
        IsHost(0, 1, 0)
        assert HostConditionGroup(0)
        """State 6: End state"""
        return 0

def event_m20_21_x125(z98=202120, z99=221000098, z100=1201001):
    """[Preset] Poly Play_Queen Battle B
    z98: Poly play ID
    z99: Poly drama played flag
    z100: Warp point ID
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m20_21_x32(z99=z99)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Poly Play_Queen Battle B_SubState"""
        call = event_m20_21_x124()
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 2: [Execution] Boss Battle_Poly Play_SubState"""
            assert event_m20_21_x34(z98=z98, z99=z99, z100=z100, z219=1)
    """State 4: End state"""
    return 0

def event_m20_21_x126():
    """[Preset] Poly drama management: queen queen, queen"""
    """State 0,1: Judgment of poly play to play"""
    if GetEventFlag(221000006) != 0:
        pass
    elif GetEventFlag(221000096) != 0:
        pass
    elif GetEventFlag(100972) != 1 and GetEventFlag(221000091) != 0:
        pass
    elif GetEventFlag(100972) != 0 and GetEventFlag(221000091) != 0:
        """State 2: [Lib] [Preset] Boss Battle_Poly Play Replay_Queen Battle A_SubState"""
        assert event_m20_21_x35(z214=20210607, z215=202110, z216=221000097, z217=1201000, z218=1)
    else:
        """State 3: [Preset] Poly Play_Queen Battle B_SubState"""
        assert event_m20_21_x125(z98=202120, z99=221000098, z100=1201001)
    """State 4: End state"""
    return 0

def event_m20_21_x127(z97=_, z91=_, z92=_):
    """[Condition] Boss Battle_Start: Queen
    z97: Poly drama played flag
    z91: Start point ID
    z92: End point ID
    """
    """State 0,1: Did you enter the point after the poly play? Has the queen been destroyed?"""
    CompareEventFlag(8, z97, 1)
    IsPlayerInsidePoint(8, z91, z92, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    CompareEventFlag(9, z97, 1)
    IsPlayerInsidePoint(9, z91, z92, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(1, 221000096, 1)
    if ConditionGroup(1):
        """State 3: Guest: Defeat the Queen"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m20_21_x128(z91=_, z92=_, z93=101, z94=_, z95=221020095, z96=221000096, z97=_):
    """[Preset] Boss Battle: Queen
    z91: Start point ID
    z92: End point ID
    z93: Sound ID
    z94: Boss Battle ID
    z95: Other flags for logic
    z96: Boss destruction flag
    z97: Poly drama played flag
    """
    """State 0,5: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(z22=z96)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 6: [Condition] Boss Battle_Start: Queen_SubState"""
        call = event_m20_21_x127(z97=z97, z91=z91, z92=z92)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 2: [Execution] Boss Battle_Start_SubState"""
            assert event_m20_21_x14(z93=z93, z94=z94, z95=z95)
            """State 1: [Reproduction] Boss Battle_Sky_SubState"""
            assert event_m20_21_x15()
            """State 4: [Condition] Boss Battle_End Judgment_SubState"""
            assert event_m20_21_x16(z20=z94)
            """State 3: [Execution] Boss Battle_End_SubState"""
            assert event_m20_21_x17(z19=z93, z20=z94, z21=z95, mode5=0)
    """State 7: End state"""
    return 0

def event_m20_21_x129(z88=221000091):
    """[Reproduction] Queen Knight AC_ Defeat Determination
    z88: Queen Knight AC Defeat Flag
    """
    """State 0,1: Are the queens A and C defeated?"""
    if GetEventFlag(z88) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_21_x130(z89=860, z90=862):
    """[Condition] Queen Knight AC_ Defeat Determination
    z89: Knight A generator ID
    z90: Knight C generator ID
    """
    """State 0,1: Are A and C pseudo-dead?"""
    CompareChrHpValue(8, z89, 1, 5)
    CompareChrHpValue(8, z90, 1, 5)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_21_x131(z84=860, z85=862, z86=93320030, z87=93340030):
    """[Execution] Queen Knight AC_ Defeat Determination
    z84: Knight A generator ID
    z85: Knight C generator ID
    z86: A's immortal release special effect ID
    z87: C immortal release special effect ID
    """
    """State 0,1: Canceled and killed immortality of A and C"""
    SetEnemySpEffect(z84, z86, 19, 4)
    SetEnemySpEffect(z85, z87, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_21_x132(z84=860, z85=862, z86=93320030, z87=93340030, z88=221000091):
    """[Preset] Queen Knight AC_Destroy
    z84: Knight A generator ID
    z85: Knight C generator ID
    z86: A's immortal release special effect ID
    z87: C immortal release special effect ID
    z88: Queen Knight AC Defeat Flag
    """
    """State 0,1: [Reproduction] Queen Knight AC_Destroy_SubState"""
    call = event_m20_21_x129(z88=z88)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Queen Knight AC_Destroy_SubState"""
        assert event_m20_21_x130(z89=860, z90=862)
        """State 2: [Execution] Queen Knight AC_Destroy_SubState"""
        assert event_m20_21_x131(z84=z84, z85=z85, z86=z86, z87=z87)
    """State 4: End state"""
    return 0

def event_m20_21_x133(z80=221000094):
    """[Reproduction] End roll
    z80: End roll execution judgment flag
    """
    """State 0,3: Event light ON"""
    SetPointLightEnabled(20210010, 1, 0)
    """State 1: End roll execution judgment"""
    if GetEventFlag(z80) != 0:
        """State 5: Executed"""
        return 1
    else:
        """State 2: End OBJ key guide valid"""
        DisableObjKeyGuide(20211800, 0)
        DisableObjKeyGuide(20211810, 0)
        """State 4: Not executed"""
        return 0

def event_m20_21_x134(z79=1600000):
    """[Condition] End roll
    z79: Point ID
    """
    """State 0,1: Multi-end judgment"""
    CompareEventFlag(8, 221000096, 1)
    IsEventBossBattle(8, 1021030, 0)
    IsMultiplayer(8, 0, 1)
    IsObjSearched(8, 20211800)
    CompareEventFlag(9, 221000006, 1)
    IsEventBossBattle(9, 1021040, 0)
    IsMultiplayer(9, 0, 1)
    IsObjSearched(9, 20211810)
    if ConditionGroup(8) and ItemAwardDisplay() != 1:
        """State 2: Previous version: To throne"""
        return 0
    elif ConditionGroup(9):
        """State 3: BEST version: Andel end"""
        return 1

def event_m20_21_x135(z80=221000094, z82=_, val1=1600010, z81=221020002, z83=_):
    """[Execution] End role
    z80: End roll execution judgment flag
    z82: Poly play ID
    val1: Destination point ID after poly play
    z81: Staff roll branch flag
    z83: ON / OFF
    """
    """State 0,6: In-game menu and PC operation prohibited, PC invincible"""
    ProhibitInGameMenu(1)
    ProhibitPlayerOperation(1)
    SetPlayerInvincible(1)
    """State 4: End OBJ key guide disabled"""
    DisableObjKeyGuide(20211800, 1)
    DisableObjKeyGuide(20211810, 1)
    assert (GetStateTime() >= 0) != 0
    """State 3: Wait for one-shot BGM stop"""
    assert LastOneShotBgmIsPlaying(60, not 1)
    """State 8: Host death determination"""
    IsHostDead(0, 0)
    assert ConditionGroup(0)
    """State 9: Abnormal condition recovery"""
    SetPlayerSpEffect(150300000, 19, 4)
    """State 5: Staff roll branch flag setting"""
    SetEventFlag(z81, z83)
    CompareEventFlag(0, z81, z83)
    assert ConditionGroup(0)
    """State 10: [Lib] Normal poly play_SubState"""
    assert event_m20_21_x0(z82=z82, val1=val1, z259=0, z260=0, z261=1)
    """State 1: End roll"""
    RollCredits()
    """State 2,7: In-game menu and PC operation enable, PC invincibility release"""
    ProhibitInGameMenu(0)
    ProhibitPlayerOperation(0)
    SetPlayerInvincible(0)
    """State 11: End state"""
    return 0

def event_m20_21_x136(z79=1600000, z80=221000094, z81=221020002):
    """[Preset] End roll
    z79: Point ID
    z80: End roll execution judgment flag
    z81: Staff roll branch flag
    """
    """State 0,1: [Reproduction] End role_SubState"""
    call = event_m20_21_x133(z80=z80)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] End role_SubState"""
        call = event_m20_21_x134(z79=z79)
        if call.Get() == 0:
            """State 3: [Execution] End roll_Conventional version_SubState"""
            assert event_m20_21_x135(z80=z80, z82=202130, val1=1600010, z81=z81, z83=0)
        elif call.Get() == 1:
            """State 4: [Execution] End role_BEST version_SubState"""
            assert event_m20_21_x135(z80=z80, z82=202150, val1=1600010, z81=z81, z83=1)
    """State 5: End state"""
    return 0

def event_m20_21_x137(z78=221000093):
    """[Reproduction] Retry point setting after queen defeat
    z78: Retry point setting completion flag
    """
    """State 0,1: Retry point setting completion flag judgment"""
    if GetEventFlag(z78) != 0:
        """State 3: Completed"""
        return 1
    else:
        """State 2: Incomplete"""
        return 0

def event_m20_21_x138():
    """[Conditions] Setting retry points after defeating the queen"""
    """State 0,1: Retry setting judgment"""
    SetConditionGroup(0, 8)
    CompareEventFlag(8, 221000096, 1)
    CompareEventFlag(8, 221000093, 0)
    SetConditionGroup(8, 1)
    CompareEventFlag(1, 100978, 0)
    CompareEventFlag(1, 100747, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(9, 221000006, 1)
    CompareEventFlag(9, 221000093, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x139(z78=221000093):
    """[Execution] Retry point setting after queen defeat
    z78: Retry point setting completion flag
    """
    """State 0,1: Retry point setting"""
    SetRespawnPoint(1700000)
    """State 2: Retry point setting completion flag ON"""
    SetEventFlag(z78, 1)
    """State 3: End state"""
    return 0

def event_m20_21_x140(z78=221000093):
    """[Preset] Retry point setting after defeating the Queen
    z78: Retry point setting completion flag
    """
    """State 0,1: [Reproduction] Retry point setting after defeating the Queen_SubState"""
    call = event_m20_21_x137(z78=z78)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Retry point setting after defeating the Queen_SubState"""
        assert event_m20_21_x138()
        """State 3: [Execution] Retry point setting after defeating the queen_SubState"""
        assert event_m20_21_x139(z78=z78)
    """State 4: End state"""
    return 0

def event_m20_21_x141(z74=_, z75=_, z76=_, z77=6.7):
    """[Preset] Golem that moves by sucking soul (lights on)
    z74: Golem OBJ instance ID
    z75: Torch OBJ instance ID
    z76: Flag that determines if Golem OBJ has absorbed soul
    z77: Distance that Golem OBJ absorbs Seoul
    """
    """State 0,1: [Reproduction] Golem that moves by sucking soul (lights on) _SubState"""
    call = event_m20_21_x142(z74=z74, z75=z75, z76=z76, z77=z77)
    if call.Get() == 0:
        """State 2: [Conditions] Golem that moves by sucking soul (lights on) _SubState"""
        assert event_m20_21_x143(z76=z76)
        """State 3: [Execution] Golem that moves by sucking soul (lights on) _SubState"""
        assert event_m20_21_x144(z74=z74, z75=z75)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_21_x142(z74=_, z75=_, z76=_, z77=6.7):
    """[Reproduction] Golem that moves by sucking soul (lights on)
    z74: Golem OBJ instance ID
    z75: Torch OBJ instance ID
    z76: Flag that determines if Golem OBJ has absorbed soul
    z77: Distance that Golem OBJ absorbs Seoul
    """
    """State 0,1: Attach torches to golem"""
    AttachObjToObj(z74, 150, z75)
    """State 2: Golem already activated?"""
    if CompareObjStateId(z74, 22, 0):
        """State 5: Safety: lighting torches"""
        ChangeObjState(z75, 20)
        """State 7: Activated"""
        return 1
    else:
        """State 3: Golem OBJ state initialization"""
        ChangeObjState(z74, 40)
        assert CompareObjStateId(z74, 40, 0)
        """State 4: Absorption processing in Seoul"""
        AddSoulAcquisitionTarget(z74, z77, z76, 1, -1)
        """State 6: Not started"""
        return 0

def event_m20_21_x143(z76=_):
    """[Conditions] Golem that moves by sucking soul (lights on)
    z76: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z76, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x144(z74=_, z75=_):
    """[Execution] Golem that moves by sucking soul (lights up)
    z74: Golem OBJ instance ID
    z75: Torch OBJ instance ID
    """
    """State 0,2: Bring a torch to the golem"""
    ChangeObjState(z74, 80)
    assert CompareObjStateId(z74, 22, 0)
    """State 1: Light a torch"""
    ChangeObjState(z75, 20)
    """State 3: End state"""
    return 0

def event_m20_21_x145(z72=_, z73=_):
    """[Reproduction] Drop of Statue Night
    z72: Generator ID
    z73: Impala ID of the neck
    """
    """State 0,1: Is your neck already broken?"""
    if IsBodyPartDestroyed(z72, 1) != 0:
        """State 2: Cut: Do nothing"""
        pass
    else:
        """State 3: Not cut: Initialization"""
        InitializeObj(z73)
    """State 4: Host termination"""
    return 0

def event_m20_21_x146():
    """[Condition] The fall of statue night_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x147(z72=_, z73=_):
    """[Execution] The fall of Statue Knight
    z72: Generator ID
    z73: Neck instance ID
    """
    """State 0,1: Link OBJ to the generator"""
    GenerateObjFromCharacter(z72, z73, 7)
    """State 2: End state"""
    return 0

def event_m20_21_x148(z72=_, z73=_):
    """[Preset] Drop of Statue Night
    z72: Generator ID
    z73: Neck instance ID
    """
    """State 0,1: [Reproduction] Drop of Statue Night_SubState"""
    assert event_m20_21_x145(z72=z72, z73=z73) == 0
    """State 3: [Condition] The fall of the statue night_Sky_SubState"""
    assert event_m20_21_x146()
    """State 2: [Execution] Drop of Statue Knight_SubState"""
    assert event_m20_21_x147(z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m20_21_x149(z6=1100000, z7=1100000, z11=100972):
    """[Condition] Boss Battle Start_Queen Knight
    z6: Start point ID
    z7: End point ID
    z11: Global flag for determining the destruction of giants
    """
    """State 0,1: Did you enter the boss room point? Has the AC been defeated?"""
    IsPlayerInsidePoint(8, z6, z7, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z6, z7, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(1, 221000091, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4: Guest: Destroyed Giant King?"""
    CompareEventFlag(0, z11, 0)
    if ConditionGroup(0):
        """State 9: Guest: No battle with the queen"""
        return 3
    else:
        """State 5: Guest: Judgment of appearance of Ander"""
        CompareEventFlag(0, 100978, 0)
        CompareEventFlag(0, 100747, 0)
        if ConditionGroup(0):
            """State 10: Guest: Consecutive battle with the Queen"""
            return 4
        else:
            """State 11: Guest: 3 consecutive battles to Ander"""
            return 5
    """State 2: Has the giant king been defeated?"""
    Label('L0')
    CompareEventFlag(0, z11, 0)
    if ConditionGroup(0):
        pass
    else:
        Goto('L1')
    """State 6: No battle with the queen"""
    return 0
    """State 3: Andel appearance determination"""
    Label('L1')
    CompareEventFlag(0, 100978, 0)
    CompareEventFlag(0, 100747, 0)
    if ConditionGroup(0):
        """State 7: There are battles with the Queen"""
        return 1
    else:
        """State 8: Three consecutive battles until Andel"""
        return 2

def event_m20_21_x150(z71=20211700):
    """[Preset] Key person
    z71: Key person OBJ instance ID
    """
    """State 0,1: [Reproduction] Key person_SubState"""
    call = event_m20_21_x151(z71=z71)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L1')
    """State 8: End of reproduction"""
    return 1
    """State 6: [Condition] Key person_Host_SubState"""
    Label('L0')
    call = event_m20_21_x156(z71=z71)
    if call.Get() == 0:
        """State 3: [Execution] Key person_Host_Unlockable_SubState"""
        call = event_m20_21_x153(z71=z71)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: Unlocked"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Key person_Host_Unlockable_SubState"""
        assert event_m20_21_x154(z71=z71)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Key person_Guest_SubState"""
    Label('L1')
    assert event_m20_21_x155(z71=z71)
    """State 2: [Execution] Key person_Guest_Empty_SubState"""
    assert event_m20_21_x152()
    """State 9: Guest termination"""
    return 2

def event_m20_21_x151(z71=20211700):
    """[Reproduction] Key person
    z71: Key person OBJ instance ID
    """
    """State 0,2: Host judgment"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 3: Guest termination"""
    return 0
    """State 1: Key person OBJ status judgment"""
    Label('L0')
    if True:
        """State 4: Before execution"""
        return 1
    elif (CompareObjStateId(z71, 20, 0) and CompareObjStateId(z71, 74, 0) and CompareObjStateId(z71,
          76, 0) and CompareObjStateId(z71, 70, 0) and CompareObjStateId(z71, 78, 0)):
        """State 5: After execution"""
        return 2

def event_m20_21_x152():
    """[Execution] Key person_Guest_Empty"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x153(z71=20211700):
    """[Execution] Key person_Host_Unlockable
    z71: Key person OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:1980000:Key to the Embedded
    DisplayYesNoMenu(1002, 1.8, z71, 190, 2, 1980000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 9: Key person transition waiting: 30"""
        ChangeObjState(z71, 30)
        assert CompareObjStateId(z71, 30, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z71, 38, 11)
        assert PlayerIsInEventAction(11) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 11, 0)
        # goods:1980000:Key to the Embedded
        DoesPlayerHaveItem(0, 1980000, 0, 5, 1, 1, 0)
        CompareObjState(1, z71, 74, 0)
        CompareObjState(1, z71, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Key person sword consumption"""
            # goods:1980000:Key to the Embedded
            ConsumeItem(1980000, 1)
            assert CompareObjStateId(z71, 20, 0)
            """State 11: Unlocked"""
            return 0
    else:
        """State 8: Key person: Waiting for transition: 30"""
        ChangeObjState(z71, 30)
        assert CompareObjStateId(z71, 30, 0)
        """State 6: Key person: Unsuccessful unlocking: 80"""
        ChangeObjState(z71, 80)
        assert CompareObjStateId(z71, 80, 0)
        """State 7: Key person: Initial state standby"""
        CompareObjState(0, z71, 10, 0)
        CompareObjState(0, z71, 10, 0)
        assert ConditionGroup(0)
    """State 10: Key person: Initial state: 10"""
    ChangeObjState(z71, 10)
    """State 12: Rerun"""
    return 1

def event_m20_21_x154(z71=20211700):
    """[Execution] Key person_Host_Unlockable
    z71: Key person OBJ instance ID
    """
    """State 0,4: Key person: Waiting for transition: 30"""
    ChangeObjState(z71, 30)
    assert CompareObjStateId(z71, 30, 0)
    """State 1: Key person: Unsuccessful unlocking: 80"""
    ChangeObjState(z71, 80)
    assert CompareObjStateId(z71, 80, 0)
    """State 3: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:1980000:Key to the Embedded
    DisplayOkMenu(1013, 0, 0, z71, 190, 2, 1980000, 0)
    assert OkMenuDisplay() != 1
    """State 2: Key person: Initial state standby"""
    CompareObjState(0, z71, 10, 0)
    assert ConditionGroup(0)
    """State 5: Unsuccessful unlocking_rerun"""
    return 0

def event_m20_21_x155(z71=20211700):
    """[Condition] Key person_Guest
    z71: Key person OBJ instance ID
    """
    """State 0,1: Wait for key person to finish"""
    CompareObjState(0, z71, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x156(z71=20211700):
    """[Condition] Key person_host
    z71: Key person OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z71)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:1980000:Key to the Embedded
    DoesPlayerHaveItem(0, 1980000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 3: Unlockable"""
        return 0
    else:
        """State 4: Unlockable"""
        return 1

def event_m20_21_x157(z65=20210407):
    """[Reproduction] Main gate of Golem
    z65: Door instance ID
    """
    """State 0,1: Is the gate already open or on the way to open?"""
    if CompareObjStateId(z65, 20, 0):
        """State 2: Navigation mesh change"""
        Label('L0')
        DeleteNavimeshAttribute(610000, 2)
        """State 4: End of reproduction"""
        return 1
    elif CompareObjStateId(z65, 70, 0):
        Goto('L0')
    else:
        """State 3: End state"""
        return 0

def event_m20_21_x158(z66=20212600, z67=20212605, z69=20212500, z70=20212505):
    """[Condition] Main gate of Golem
    z66: Right lever instance ID
    z67: Instance ID of the left lever
    z69: Right golem instance ID
    z70: Left golem instance ID
    """
    """State 0,1: Standby for left and right golems"""
    CompareObjState(8, z69, 20, 0)
    CompareObjState(8, z70, 20, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_21_x159(z65=20210407, z68=221000041):
    """[Execution] The main gate of the Golem
    z65: Door instance ID Instance ID
    z68: Main gate liberation flag
    """
    """State 0,1: OBJ state transition: door"""
    ChangeObjState(z65, 70)
    """State 4: Main gate release flag ON"""
    SetEventFlag(z68, 1)
    """State 3: Has the door opened?"""
    CompareObjState(0, z65, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(610000, 2)
    """State 5: End state"""
    return 0

def event_m20_21_x160(z65=20210407, z66=20212600, z67=20212605, z68=221000041, z69=20212500, z70=20212505):
    """[Preset] Golem front gate
    z65: Door instance ID
    z66: Right lever instance ID
    z67: Instance ID of the left lever
    z68: Main gate liberation flag
    z69: Right golem instance ID
    z70: Left golem instance ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z65, 0)
    """State 2: [Reproduction] Golem Main Gate_SubState"""
    call = event_m20_21_x157(z65=z65)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Condition] Golem Main Gate_SubState"""
        assert event_m20_21_x158(z66=z66, z67=z67, z69=z69, z70=z70)
        """State 4: [Execution] Golem Main Gate_SubState"""
        assert event_m20_21_x159(z65=z65, z68=z68)
    """State 5: End state"""
    return 0

def event_m20_21_x161(z59=221000086):
    """[Reproduction] Mirror Night Battle_Start
    z59: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z59) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_21_x162(z60=800000, z61=800000):
    """[Condition] Mirror Night Battle_Start
    z60: Start point ID
    z61: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z60, z61, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z60, z61, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Is it in game?"""
    assert InGame() != 0
    """State 3: End state"""
    return 0

def event_m20_21_x163(z62=201, z63=1021010, z64=221020085):
    """[Execution] Mirror Night Battle_Start
    z62: Sound ID
    z63: Boss Battle ID
    z64: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z62)
    """State 1: Boss battle start notification"""
    StartBossFight(z63)
    """State 4: Drawing mode switching: Mirror night mode"""
    SetSpecialDrawingMode(1)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z64, 1)
    """State 5: End state"""
    return 0

def event_m20_21_x164():
    """[Reproduction] Mirror Night Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x165(z63=1021010):
    """[Condition] Mirror Knight Battle_End Judgment
    z63: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z63, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x166(z62=201, z63=1021010, z64=221020085, mode2=0):
    """[Execution] Mirror Night Battle_End
    z62: Sound ID
    z63: Boss Battle ID
    z64: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z64, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z63)
    """State 4: Drawing mode switching: Standard"""
    SetSpecialDrawingMode(0)
    """State 5: My death under Mirror Knight"""
    EnemyActionRequest(5000, 1)
    EnemyActionRequest(5001, 1)
    """State 6: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z62)
    """State 7: End state"""
    return 0

def event_m20_21_x167(z59=221000086, z60=800000, z61=800000, z62=201, z63=1021010, z64=221020085, mode2=0):
    """[Preset] Mirror Night Battle starts
    z59: Boss destruction flag
    z60: Start point ID
    z61: End point ID
    z62: Sound ID
    z63: Boss Battle ID
    z64: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Mirror Night Battle_Start_SubState"""
    call = event_m20_21_x161(z59=z59)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Mirror Knight Battle_Start_SubState"""
        assert event_m20_21_x162(z60=z60, z61=z61)
        """State 3: [Execution] Mirror Knight Battle_Start_SubState"""
        assert event_m20_21_x163(z62=z62, z63=z63, z64=z64)
        """State 2: [Reproduction] Mirror Knight Battle_Sky_SubState"""
        assert event_m20_21_x164()
        """State 6: [Condition] Mirror Knight Battle_End Judgment_SubState"""
        assert event_m20_21_x165(z63=z63)
        """State 4: [Execution] Mirror Knight Battle_End_SubState"""
        assert event_m20_21_x166(z62=z62, z63=z63, z64=z64, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m20_21_x168(z57=_):
    """[Condition] Golem_Main Gate
    z57: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z57, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x169(z55=_, z56=_):
    """[Execution] Golem_Main Gate_Soul Absorbed
    z55: Golem instance ID
    z56: Lever instance ID
    """
    """State 0,3: Has Golem's Soul Absorption Anime finished?"""
    CompareObjState(0, z55, 72, 0)
    assert ConditionGroup(0)
    """State 1: OBJ state transition: lever operation"""
    ChangeObjState(z56, 70)
    """State 2: Lever OBJ transition standby"""
    CompareObjState(0, z56, 20, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x170(z51=20212000, z52=20211520, z53=20210410, z54=300000):
    """[Preset] Lever door between soldiers
    z51: Instance ID of the iron lattice OBJ
    z52: Lever OBJ instance ID
    z53: Door OBJ instance ID
    z54: Navimesh change point ID
    """
    """State 0,1: [Reproduction] Lever door between soldiers_SubState"""
    call = event_m20_21_x114(z51=z51, z52=z52, z53=z53, z54=z54)
    if call.Get() == 0:
        """State 2: [Condition] Lever door between soldiers_SubState"""
        assert event_m20_21_x115(z52=z52)
        """State 3: [Execution] Lever door between soldiers_SubState"""
        Label('L0')
        assert event_m20_21_x116(z51=z51, z53=z53, z54=z54)
    elif call.Get() == 2:
        Goto('L0')
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_21_x171():
    """[Reproduction] Vegrant Deletion Determination_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x172(z50=_):
    """[Condition] Vegrant removal determination
    z50: Generator ID
    """
    """State 0,2: Has a vegrant been generated?"""
    IsChrActive(0, z50, 1)
    assert ConditionGroup(0)
    """State 1: Has Vegrant finished the return action?"""
    CompareChrEzStateValue(0, z50, 7, 1, 0)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m20_21_x173(z50=_):
    """[Execution] Vegrant removal determination
    z50: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z50, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x174(z50=_):
    """[Preset] Vegrant removal judgment
    z50: Generator ID
    """
    """State 0,1: [Reproduction] Vegrant deletion judgment_empty_SubState"""
    assert event_m20_21_x171()
    """State 3: [Condition] Vegrant deletion determination_SubState"""
    assert event_m20_21_x172(z50=z50)
    """State 2: [Execution] Vegrant deletion determination_SubState"""
    assert event_m20_21_x173(z50=z50)
    """State 4: End state"""
    return 0

def event_m20_21_x175(z46=20210001, z47=20210002, z48=701000, z49=701002):
    """[Preset] Boss: Heavy cavalry: Soldier only 2 battles_Light switching
    z46: Boss Battle Area Treasure Light 1
    z47: Boss Battle Area Treasure Light 2
    z48: Boss battle area light switch point_start
    z49: Boss battle area light switch point _ end
    """
    """State 0,1: [Reproduction] Boss: Heavy cavalry: Soldier only 2 battles_Light switching_SubState"""
    assert event_m20_21_x176(z46=z46, z47=z47)
    """State 2: [Conditions] Boss: Heavy cavalry: Soldier only 2 battles_Light switching_SubState"""
    assert event_m20_21_x177(z48=z48, z49=z49)
    """State 3: [Execution] Boss: Heavy cavalry: Soldier only 2 battles_Light switch_SubState"""
    assert event_m20_21_x178(z46=z46, z47=z47, z48=z48, z49=z49)
    """State 4: End state"""
    return 0

def event_m20_21_x176(z46=20210001, z47=20210002):
    """[Reproduction] Boss: Heavy cavalry: Soldier only 2 battles_light switching
    z46: Boss Battle Area Treasure Light 1
    z47: Boss Battle Area Treasure Light 2
    """
    """State 0,1: Lights off"""
    SetPointLightEnabled(z46, 0, 0)
    SetPointLightEnabled(z47, 0, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x177(z48=701000, z49=701002):
    """[Conditions] Boss: Heavy cavalry: Soldier only 2 battles_light switching
    z48: Boss battle area light switch point_start
    z49: Boss battle area light switch point _ end
    """
    """State 0,1: Did you enter the lighting point?"""
    IsPlayerInsidePoint(0, z48, z49, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x178(z46=20210001, z47=20210002, z48=701000, z49=701002):
    """[Execution] Boss: Heavy cavalry: Soldier only 2 battles_Light switching
    z46: Boss Battle Area Treasure Light 1
    z47: Boss Battle Area Treasure Light 2
    z48: Boss battle area light switch point_start
    z49: Boss battle area light switch point _ end
    """
    """State 0,1: Light on"""
    SetPointLightEnabled(z46, 1, 0)
    SetPointLightEnabled(z47, 1, 0)
    """State 2: Did you get out of the lighting point?"""
    IsPlayerInsidePoint(0, z48, z49, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x179(z41=104160, z42=678, z43=104160, z44=103660, z45=63):
    """NPC White Phantom Appearance: General Purpose
    z41: White Phantom can appear: Global event flag
    z42: White Phantom: Generator ID
    z43: Death: Global event flag
    z44: Hostile: Global event flag
    z45: Body: Generator group ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z42)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z43, 1)
        CompareEventFlag(1, z44, 1)
        CompareEventFlag(2, z41, 0)
        CompareEventFlag(8, 100974, 1)
        CompareEventFlag(8, 100972, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z42)
            if GetEventFlag(221000006) != 0:
                """State 12: Appearance: Hostile: Waiting: After the Queen"""
                Label('L1')
                CompareEventFlag(0, z43, 1)
                if ConditionGroup(0):
                    pass
                elif (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747)
                      != 0 and GetEventFlag(221000001) != 0 and GetEventFlag(221000006) != 1 and GetEventFlag(z44)
                      != 1):
                    """State 8: Appearance: System: Rerun"""
                    Label('L2')
                    RestartMachine()
                    Quit()
            elif GetEventFlag(221000096) != 0:
                Goto('L1')
            else:
                """State 7: Appearance: Hostile: Standby"""
                CompareEventFlag(0, z43, 1)
                CompareEventFlag(8, z44, 0)
                CompareEventFlag(8, 100974, 1)
                CompareEventFlag(8, 100972, 1)
                CompareEventFlag(9, z44, 0)
                CompareEventFlag(9, 100974, 0)
                CompareEventFlag(9, 100972, 0)
                CompareEventFlag(10, z44, 0)
                CompareEventFlag(10, 100974, 0)
                CompareEventFlag(10, 100972, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(8):
                    Goto('L2')
                elif ConditionGroup(9):
                    Goto('L2')
                elif ConditionGroup(10):
                    Goto('L2')
        elif ConditionGroup(8):
            Goto('L0')
        elif GetEventFlag(221000006) != 0:
            Goto('L0')
        elif (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747) !=
              0 and GetEventFlag(221000001) != 0):
            """State 3: Appearance: Phantom sign display: Permission"""
            Label('L3')
            GenerateNpcPhantom(z42)
            if (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747) !=
                0 and GetEventFlag(221000001) != 0):
                """State 11: Appearance: Phantom sign showing: Waiting: After the queen"""
                CompareEventFlag(0, z43, 1)
                CompareEventFlag(1, z44, 1)
                HasNpcPhantomSpawned(2, z42, 1)
                if ConditionGroup(0):
                    Goto('L4')
                elif ConditionGroup(1):
                    Goto('L0')
                elif ConditionGroup(2):
                    pass
            else:
                """State 4: Appearance: Phantom sign displayed: Waiting"""
                CompareEventFlag(0, z43, 1)
                CompareEventFlag(1, z44, 1)
                HasNpcPhantomSpawned(2, z42, 1)
                CompareEventFlag(8, 100974, 1)
                CompareEventFlag(8, 100972, 0)
                if ConditionGroup(0):
                    Goto('L4')
                elif ConditionGroup(1):
                    Goto('L0')
                elif ConditionGroup(2):
                    pass
                elif ConditionGroup(8):
                    Goto('L0')
            """State 5: Appearance: Phantom is appearing: Waiting"""
            DeleteEnemyByGeneratorGroup(z45, 0)
            HasNpcPhantomSpawned(0, z42, 0)
            assert ConditionGroup(0)
            Goto('L2')
        elif GetEventFlag(221000096) != 0:
            Goto('L0')
        elif ConditionGroup(2):
            Goto('L3')
        """State 9: Appearance: Sign & Phantom: Stop generation"""
        Label('L4')
        DeleteNpcPhantom(z42)
    """State 10: Appearance: System: End"""
    EndMachine()

def event_m20_21_x180(z36=_, z37=_, z38=_, z39=_, z40=-1):
    """NPC White Phantom Appearance: General Purpose: Durahan
    z36: White Phantom can appear: Global event flag
    z37: White Phantom: Generator ID
    z38: Death: Global event flag
    z39: Hostile: Global event flag
    z40: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z37)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z38, 1)
        CompareEventFlag(1, z39, 1)
        CompareEventFlag(2, z36, 1)
        CompareEventFlag(8, 100974, 1)
        CompareEventFlag(8, 100972, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z37)
            if GetEventFlag(221000006) != 0:
                """State 12: Appearance: Hostile: Waiting: After the Queen"""
                Label('L1')
                CompareEventFlag(0, z38, 1)
                if ConditionGroup(0):
                    pass
                elif (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747)
                      != 0 and GetEventFlag(221000001) != 0 and GetEventFlag(221000006) != 1 and GetEventFlag(z39)
                      != 1):
                    """State 5: Appearance: System: Rerun"""
                    Label('L2')
                    RestartMachine()
                    Quit()
            elif GetEventFlag(221000096) != 0:
                Goto('L1')
            else:
                """State 10: Appearance: Hostile: Standby"""
                CompareEventFlag(0, z38, 1)
                CompareEventFlag(8, z39, 0)
                CompareEventFlag(8, 100974, 0)
                CompareEventFlag(8, 100972, 0)
                CompareEventFlag(9, z39, 0)
                CompareEventFlag(9, 100974, 1)
                CompareEventFlag(9, 100972, 1)
                CompareEventFlag(10, z39, 0)
                CompareEventFlag(10, 100974, 0)
                CompareEventFlag(10, 100972, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(8):
                    Goto('L2')
                elif ConditionGroup(9):
                    Goto('L2')
                elif ConditionGroup(10):
                    Goto('L2')
        elif ConditionGroup(8):
            Goto('L0')
        elif GetEventFlag(221000006) != 0:
            Goto('L0')
        elif (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747) !=
              0 and GetEventFlag(221000001) != 0):
            """State 3: Appearance: Phantom sign display: Permission"""
            Label('L3')
            GenerateNpcPhantom(z37)
            if (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747) !=
                0 and GetEventFlag(221000001) != 0):
                """State 11: Appearance: Phantom sign showing: Waiting: After the queen"""
                CompareEventFlag(0, z38, 1)
                CompareEventFlag(1, z39, 1)
                HasNpcPhantomSpawned(2, z37, 1)
                if ConditionGroup(2):
                    pass
                elif ConditionGroup(1):
                    Goto('L0')
                elif ConditionGroup(0):
                    Goto('L4')
            else:
                """State 8: Appearance: Phantom sign displayed: Waiting"""
                CompareEventFlag(0, z38, 1)
                CompareEventFlag(1, z39, 1)
                HasNpcPhantomSpawned(2, z37, 1)
                CompareEventFlag(8, 100974, 1)
                CompareEventFlag(8, 100972, 0)
                if ConditionGroup(0):
                    Goto('L4')
                elif ConditionGroup(1):
                    Goto('L0')
                elif ConditionGroup(2):
                    pass
                elif ConditionGroup(8):
                    Goto('L0')
            """State 6: Appearance: Phantom is appearing: Waiting"""
            HasNpcPhantomSpawned(0, z37, 0)
            assert ConditionGroup(0)
            Goto('L2')
        elif GetEventFlag(221000096) != 0:
            Goto('L0')
        elif ConditionGroup(2):
            Goto('L3')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        Label('L4')
        DeleteNpcPhantom(z37)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m20_21_x181(z33=20210406):
    """[Condition] King's door_Guest
    z33: Instance ID of king's door OBJ
    """
    """State 0,1: Has the door opened?"""
    CompareObjState(0, z33, 30, 0)
    assert ConditionGroup(0)
    """State 2: Door opened"""
    return 0

def event_m20_21_x182(z34=900000):
    """[Execution] King's Door_Guest
    z34: Point ID for changing navigation
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z34, 2)
    """State 2: End state"""
    return 0

def event_m20_21_x183(z25=1200010, z26=1200011):
    """[Conditions] Boss Battle_Start: Anderu
    z25: Start point ID
    z26: End point ID
    """
    """State 0,2: Did you defeat the queen?"""
    CompareEventFlag(0, 221000096, 1)
    assert ConditionGroup(0)
    """State 5: Host?"""
    if IsGuest() != 1:
        """State 3: Memory read flag ON"""
        SetEventFlag(221000001, 1)
    else:
        pass
    """State 4: Wait for Anderu conversation"""
    CompareEventFlag(0, 208031, 1)
    assert ConditionGroup(0)
    """State 1: Have you entered the starting point?"""
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(8, z25, z26, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 9)
    IsPlayerInsidePoint(9, z25, z26, 1)
    IsHost(9, 0, 0)
    assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m20_21_x184(z25=1200010, z26=1200011, z27=701, z28=1021040, z29=221020005, z30=221000006):
    """[Preset] Boss Battle: Andyel
    z25: Start point ID
    z26: End point ID
    z27: Sound ID
    z28: Boss Battle ID
    z29: Other flags for logic
    z30: Boss destruction flag
    """
    """State 0,4: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(z22=z30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start: Andyel_SubState"""
        assert event_m20_21_x183(z25=z25, z26=z26)
        """State 6: [Execution] Boss Battle_Start: Andyel_SubState"""
        assert event_m20_21_x198(z19=z27, z20=z28, z21=z29)
        """State 7: [Reproduction] Boss Battle_Sky_2_SubState"""
        assert event_m20_21_x15()
        """State 9: [Condition] Boss Battle_HP Gauge Display: Andyel_SubState"""
        assert event_m20_21_x199()
        """State 8: [Execution] Boss Battle_HP Gauge Display: Andiel_SubState"""
        assert event_m20_21_x200()
        """State 1: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 3: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z20=z28)
        """State 2: [Execution] Boss Battle_End_SubState"""
        assert event_m20_21_x17(z19=z27, z20=z28, z21=z29, mode5=0)
    """State 10: End state"""
    return 0

def event_m20_21_x185():
    """[BEST] [Reproduction] End OBJ management"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: End state"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m20_21_x186():
    """[BEST] [Conditions] End OBJ management"""
    """State 0,1: End OBJ switching judgment"""
    CompareEventFlag(0, 221000094, 1)
    CompareEventFlag(8, 221000006, 1)
    CompareEventFlag(8, 221000094, 0)
    CompareEventFlag(8, 208030, 1)
    CompareEventFlag(9, 221000096, 1)
    CompareEventFlag(9, 221000094, 0)
    SetConditionGroup(9, 1)
    CompareEventFlag(1, 100978, 0)
    CompareEventFlag(1, 100747, 0)
    if ConditionGroup(0):
        """State 3: End roll executed"""
        return 1
    elif ConditionGroup(8):
        """State 4: After defeating Andeel"""
        return 2
    elif ConditionGroup(9):
        """State 2: After defeating the queen"""
        return 0
    else:
        """State 5: Wait for next decision"""
        return 3

def event_m20_21_x187(z31=20211800, z32=20211810):
    """[BEST] [Execution] End OBJ management_After end
    z31: Conventional end OBJ instance ID
    z32: EX end OBJ instance ID
    """
    """State 0,1: Disable end OBJ: 10"""
    ChangeObjState(z31, 10)
    ChangeObjState(z32, 10)
    """State 2: End state"""
    return 0

def event_m20_21_x188(z31=20211800, z32=20211810):
    """[BEST] [Execution] End OBJ management_After the deal
    z31: Conventional end OBJ instance ID
    z32: EX end OBJ instance ID
    """
    """State 0,1: Enable end OBJ: 20"""
    ChangeObjState(z31, 20)
    ChangeObjState(z32, 20)
    """State 2: End state"""
    return 0

def event_m20_21_x189(z31=20211800, z32=20211810):
    """[BEST] [execution] End OBJ management_after the queen
    z31: Conventional end OBJ instance ID
    z32: EX end OBJ instance ID
    """
    """State 0,2: weight"""
    CompareStateTime(0, 8, 3, 8)
    assert ConditionGroup(0)
    """State 1: Enable only conventional OBJ"""
    ChangeObjState(z31, 20)
    ChangeObjState(z32, 10)
    """State 3: End state"""
    return 0

def event_m20_21_x190():
    """[BEST] [Execution] End OBJ management_Waiting for next decision"""
    """State 0,1: Wait for next judgment"""
    SetConditionGroup(0, 8)
    CompareEventFlag(8, 221000006, 1)
    CompareEventFlag(8, 221000094, 0)
    CompareEventFlag(8, 208030, 1)
    SetConditionGroup(0, 9)
    CompareEventFlag(9, 221000096, 1)
    CompareEventFlag(9, 221000094, 0)
    SetConditionGroup(9, 1)
    CompareEventFlag(1, 100978, 0)
    CompareEventFlag(1, 100747, 0)
    assert ConditionGroup(0)
    """State 2: Rerun"""
    return 0

def event_m20_21_x191(z31=20211800, z32=20211810):
    """[BEST] [Preset] End OBJ management
    z31: Conventional end OBJ instance ID
    z32: EX end OBJ instance ID
    """
    """State 0,1: [BEST] [Reproduction] End OBJ management_SubState"""
    assert event_m20_21_x185()
    """State 6: [BEST] [Condition] End OBJ management_SubState"""
    call = event_m20_21_x186()
    if call.Get() == 1:
        """State 3: [BEST] [Execution] End OBJ management_After end_SubState"""
        assert event_m20_21_x187(z31=z31, z32=z32)
    elif call.Get() == 2:
        """State 2: [BEST] [Execution] End OBJ management_After deal_SubState"""
        assert event_m20_21_x188(z31=z31, z32=z32)
    elif call.Get() == 0:
        """State 4: [BEST] [Execution] End OBJ Management_After the Queen_SubState"""
        assert event_m20_21_x189(z31=z31, z32=z32)
    elif call.Get() == 3:
        """State 5: [BEST] [Execution] End OBJ management_Waiting for next judgment_SubState"""
        assert event_m20_21_x190()
        """State 8: Rerun"""
        return 1
    """State 7: Finish"""
    return 0

def event_m20_21_x192(z14=910, z15=1105000, z16=221000007, z17=221000006, z18=221000001):
    """[BEST] [Preset] Anderel_Initial layout change
    z14: Generator ID
    z15: Point ID for rematch
    z16: Flag for judging first battle or rematch
    z17: Boss destruction flag
    z18: Memory read flag
    """
    """State 0,1: [BEST] [Reproduction] Andel_Initial layout change_SubState"""
    call = event_m20_21_x193(z17=z17)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [BEST] [Condition] Anderel_Initial layout change_SubState"""
        call = event_m20_21_x194(z16=z16, z18=z18)
        if call.Get() == 2:
            """State 4: [BEST] [Execution] Andele_Initial location change_When conversation is dead_SubState"""
            assert event_m20_21_x201(z14=z14, z15=z15)
        elif call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 2: [BEST] [Execution] Undeal_Initial location change_SubState"""
            assert event_m20_21_x195(z14=z14, z15=z15)
    """State 5: End state"""
    return 0

def event_m20_21_x193(z17=221000006):
    """[BEST] [Reproduction] Andel _ initial placement change
    z17: Boss destruction flag
    """
    """State 0,1: Destroyed?"""
    if GetEventFlag(z17) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Undefeated"""
        return 0

def event_m20_21_x194(z16=221000007, z18=221000001):
    """[BEST] [Condition] Andyel_Initial layout change
    z16: Flag to perform first battle or rematch determination
    z18: Memory read flag
    """
    """State 0,1: Is it the first game? Is it a rematch? Did you die during the conversation?"""
    CompareEventFlag(0, z16, 0)
    CompareEventFlag(8, z16, 0)
    CompareEventFlag(8, z18, 1)
    if ConditionGroup(8):
        """State 4: Died during conversation"""
        return 2
    elif ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m20_21_x195(z14=910, z15=1105000):
    """[BEST] [Execution] Andele_Initial placement change
    z14: Generator ID
    z15: Point ID for rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z14, z15)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z14, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x196(z23=1200010, z24=1200011):
    """[Condition] Boss Battle_Start: Andyel_Sequential Battle
    z23: Start point ID
    z24: End point ID
    """
    """State 0,1: Did you defeat the queen?"""
    CompareEventFlag(0, 221000096, 1)
    assert ConditionGroup(0)
    """State 8: Host?"""
    if IsGuest() != 1:
        """State 2: Memory read flag ON"""
        SetEventFlag(221000001, 1)
    else:
        pass
    """State 10: Has the boss battle been finalized?"""
    IsEventBossBattle(0, 1021031, 0)
    assert ConditionGroup(0)
    """State 3: Wait for Anderu conversation"""
    CompareEventFlag(0, 208031, 1)
    IsGameSaving(1, 0)
    if ConditionGroup(0):
        """State 5: Isn't auto saving in progress?"""
        IsGameSaving(0, 0)
        assert ConditionGroup(0)
        """State 4: Save execution"""
        SaveExecution()
    elif ConditionGroup(1):
        """State 6: Save execution_2"""
        SaveExecution()
        """State 7: Wait for Anderu conversation end_2"""
        CompareEventFlag(0, 208031, 1)
        assert ConditionGroup(0)
    """State 9: Have you entered the starting point?"""
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(8, z23, z24, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 9)
    IsPlayerInsidePoint(9, z23, z24, 1)
    IsHost(9, 0, 0)
    assert ConditionGroup(0)
    """State 11: End state"""
    return 0

def event_m20_21_x197(z19=701, z20=1021040, z21=221020005, z22=221000006, z23=1200010, z24=1200011):
    """[Preset] Boss Battle: Andyel
    z19: Sound ID
    z20: Boss Battle ID
    z21: Other flags for logic
    z22: Boss destruction flag
    z23: Start point ID
    z24: End point ID
    """
    """State 0,4: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(z22=z22)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start: Andyel_Sequential Battle_SubState"""
        assert event_m20_21_x196(z23=z23, z24=z24)
        """State 6: [Execution] Boss Battle_Start: Andyel_SubState"""
        assert event_m20_21_x198(z19=z19, z20=z20, z21=z21)
        """State 7: [Reproduction] Boss Battle_Sky_2_SubState"""
        assert event_m20_21_x15()
        """State 9: [Condition] Boss Battle_HP Gauge Display: Andyel_SubState"""
        assert event_m20_21_x199()
        """State 8: [Execution] Boss Battle_HP Gauge Display: Andiel_SubState"""
        assert event_m20_21_x200()
        """State 1: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 3: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z20=z20)
        """State 2: [Execution] Boss Battle_End_SubState"""
        assert event_m20_21_x17(z19=z19, z20=z20, z21=z21, mode5=0)
    """State 10: End state"""
    return 0

def event_m20_21_x198(z19=701, z20=1021040, z21=221020005):
    """[Execution] Boss Battle_Start: Andyel
    z19: Sound ID
    z20: Boss Battle ID
    z21: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z19)
    """State 1: Boss battle start notification"""
    StartBossFight(z20)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z21, 1)
    """State 4: First battle flag ON"""
    SetEventFlag(221000007, 1)
    """State 5: End state"""
    return 0

def event_m20_21_x199():
    """[Condition] Boss Battle_HP Gauge Display: Anderu"""
    """State 0,1: Was the startup state released?"""
    CompareChrStartUpState(0, 910, 3, 1)
    CompareStateTime(0, 15, 3, 15)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x200():
    """[Execution] Boss Battle_HP Gauge Display: Andeel"""
    """State 0,1: HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 2: White spirit start flag ON"""
    SetEventFlag(221020008, 1)
    """State 3: End state"""
    return 0

def event_m20_21_x201(z14=910, z15=1105000):
    """[BEST] [Execution] Andele_Initial location change_When conversation is dead
    z14: Generator ID
    z15: Point ID for rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPositionAndWarpGenerated(z14, z15)
    """State 2: End state"""
    return 0

def event_m20_21_x202(z8=102, z9=_, z10=221020090, mode1=0):
    """[Execution] Boss Battle_End_Queen Knight
    z8: Sound ID
    z9: Boss Battle ID
    z10: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z10, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z9)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z8)
    """State 7: Has the boss battle been finalized?"""
    IsEventBossBattle(0, z9, 0)
    assert ConditionGroup(0)
    """State 6: Isn't auto saving in progress?"""
    IsGameSaving(0, 0)
    assert ConditionGroup(0)
    """State 5: Save execution"""
    SaveExecution()
    """State 8: End state"""
    return 0

def event_m20_21_x203(z3=221020042):
    """[DC] [Reproduction] Flag switching with king's ring equipment
    z3: Logic flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Equipment judgment"""
    # goods:40510000:King's Ring
    if (EquippedItemCount(40510000) >= 0) != 0:
        """State 3: Logic flag ON"""
        SetEventFlag(z3, 1)
        """State 5: Equipped"""
        return 0
    else:
        """State 4: Logic flag OFF"""
        SetEventFlag(z3, 0)
        """State 7: Not equipped"""
        return 2
    """State 6: Finish"""
    Label('L0')
    return 1

def event_m20_21_x204(z5=_):
    """[DC] [Condition] Flag switch with king's ring equipment
    z5: Comparison value
    """
    """State 0,1: Equipment judgment"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, z5, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x205(z3=221020042, z4=_):
    """[DC] [execution] Flag switch with king's ring equipment
    z3: Logic flag
    z4: ON or OFF
    """
    """State 0,1: Logic flag switching"""
    SetEventFlag(z3, z4)
    """State 2: End state"""
    return 0

def event_m20_21_x206(z3=221020042):
    """[DC] [Preset] Flag switch with king's ring equipment
    z3: Logic flag
    """
    """State 0,1: [DC] [Reproduction] Flag switch with king's ring equipment_SubState"""
    call = event_m20_21_x203(z3=z3)
    if call.Get() == 0:
        """State 3: [DC] [Condition] Flag switching with king's ring equipment_SubState"""
        assert event_m20_21_x204(z5=0)
        """State 2: [DC] [execution] Flag switch with king's ring equipment_SubState"""
        assert event_m20_21_x205(z3=z3, z4=0)
    elif call.Get() == 2:
        """State 5: [DC] [Condition] Flag switch with king's ring equipment_2_SubState"""
        assert event_m20_21_x204(z5=1)
        """State 4: [DC] [execution] Flag switch with king's ring equipment_2_SubState"""
        assert event_m20_21_x205(z3=z3, z4=1)
    elif call.Get() == 1:
        """State 7: Finish"""
        return 1
    """State 6: Rerun"""
    return 0

def event_m20_21_x207(z1=20215170):
    """[DC] [Condition] Mask is activated in treasure chest
    z1: Treasure chest OBJ instance ID
    """
    """State 0,1: Did you open the treasure chest or destroyed it?"""
    CompareObjState(0, z1, 80, 0)
    CompareObjState(0, z1, 100, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x208(z2=221000025):
    """[DC] [execution] Kamen starts in treasure chest
    z2: Masked start flag
    """
    """State 0,1: Masked activation flag ON"""
    SetEventFlag(z2, 1)
    """State 2: End state"""
    return 0

def event_m20_21_x209(z2=221000025):
    """[DC] [Reproduction] Mask starts in treasure chest
    z2: Masked start flag
    """
    """State 0,1: Already started?"""
    if GetEventFlag(z2) != 0:
        """State 3: Started: End"""
        return 1
    else:
        """State 2: Not running"""
        return 0

def event_m20_21_x210(z1=20215170, z2=221000025):
    """[DC] [Preset] Mask is activated in treasure chest
    z1: Treasure chest OBJ instance ID
    z2: Masked start flag
    """
    """State 0,1: [DC] [Reproduction] Mask is activated in the treasure box_SubState"""
    call = event_m20_21_x209(z2=z2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Mask is activated in treasure box_SubState"""
        assert event_m20_21_x207(z1=z1)
        """State 2: [DC] [execution] The mask is activated in the treasure box_SubState"""
        assert event_m20_21_x208(z2=z2)
    """State 4: End state"""
    return 0

def event_m20_21_111015():
    """OBJ: Durahan: White phantom sign display"""
    """State 0,2: NPC White Phantom Appearance: General Purpose: Durahan_SubState"""
    event_m20_21_x180(z36=102010, z37=677, z38=104000, z39=103500, z40=-1)

def event_m20_21_111052():
    """OBJ: Dragon Maiden (in the Royal Castle): Approval for appearance"""
    """State 0,1: Appearance permission: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 3: Appearance permission: Death determination"""
    CompareEventFlag(0, 104020, 1)
    if ConditionGroup(0):
        """State 4: Appearance permission: Generation stop"""
        Label('L0')
        SetEventFlag(102086, 1)
        CompareEventFlag(0, 102086, 1)
        assert ConditionGroup(0)
    else:
        """State 5: Appearance permission: Judgment of generation stop"""
        CompareEventFlag(0, 102086, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 6: Appearance permission: Judgment of defeating Mirror Knight"""
            CompareEventFlag(0, 100958, 1)
            if ConditionGroup(0):
                Goto('L0')
            else:
                pass
    """State 2: Appearance permission: System: End"""
    EndMachine()

def event_m20_21_111053():
    """OBJ: Dragon Maiden (before clear): Approval for appearance"""
    """State 0,1: Appearance permission: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 3: Appearance permission: Death determination"""
    CompareEventFlag(0, 104020, 1)
    if ConditionGroup(0):
        """State 4: Appearance permission: Generation stop: ON"""
        Label('L0')
        SetEventFlag(102089, 1)
        CompareEventFlag(0, 102089, 1)
        assert ConditionGroup(0)
    else:
        """State 8: Appearance permission: Judgment of generation stop"""
        CompareEventFlag(0, 201150, 1)
        if ConditionGroup(0):
            Goto('L0')
        else:
            """State 5: Approval for appearance: Judgment of destroying queen's armor"""
            CompareEventFlag(0, 100973, 1)
            if ConditionGroup(0):
                Goto('L0')
            else:
                """State 6: Appearance permission: Giant defeat determination"""
                CompareEventFlag(0, 100972, 1)
                if ConditionGroup(0):
                    """State 7: Appearance permission: Generation stop: OFF"""
                    SetEventFlag(102089, 0)
                    CompareEventFlag(0, 102089, 0)
                    assert ConditionGroup(0)
                else:
                    Goto('L0')
    """State 2: Appearance permission: System: End"""
    EndMachine()

def event_m20_21_111054():
    """NPC: Dragon Miko (within the castle): Character erasure"""
    """State 0,1: Character erase: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Character erasure: Erase judgment: Standby"""
        CompareEventFlag(0, 100958, 1)
        assert ConditionGroup(0)
        """State 3: Character erase: Erase"""
        DeleteEnemyByGeneratorGroup(60, 0)
        SetEventFlag(102086, 1)
        CompareEventFlag(8, 102086, 1)
        SetEventFlag(221020167, 1)
        CompareEventFlag(8, 221020167, 1)
        assert ConditionGroup(8)
    """State 4: Character erasure: System: Exit"""
    EndMachine()

def event_m20_21_111055():
    """NPC: Dragon Miko (Before Clear): Character Erasure"""
    """State 0,1: Character erase: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Character erasure: Erase judgment: Standby"""
        CompareEventFlag(0, 100973, 1)
        assert ConditionGroup(0)
        """State 3: Character erase: Erase"""
        DeleteEnemyByGeneratorGroup(62, 0)
        SetEventFlag(102089, 1)
        CompareEventFlag(8, 102089, 1)
        SetEventFlag(221020177, 1)
        CompareEventFlag(8, 221020177, 1)
        assert ConditionGroup(8)
    """State 4: Character erasure: System: Exit"""
    EndMachine()

def event_m20_21_111082():
    """NPC: Queen: Character Erasure"""
    """State 0,1: Character erase: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Character erasure: Erase judgment: Standby"""
        CompareEventFlag(1, 100972, 1)
        assert ConditionGroup(1)
        """State 3: Character erase: Erase"""
        DeleteEnemyByGeneratorGroup(61, 0)
        SetEventFlag(102140, 1)
        CompareEventFlag(0, 102140, 1)
        assert ConditionGroup(0)
    """State 4: Character erasure: System: Exit"""
    EndMachine()

def event_m20_21_111182():
    """OBJ: Shenzhen Pilgrim: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_21_x1(z255=104123, z256=20214000, z257=41, z258=7250)

def event_m20_21_111183():
    """OBJ: Shenzhen Pilgrims: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7250:Darkdiver Grandahl
    event_m20_21_x8(z239=221010100, z240=221020101, z241=104120, z242=20214000, z243=111182, npc1=7250)

def event_m20_21_111184():
    """OBJ: Shenzhen Pilgrim: Death Determination"""
    """State 0,1: [Lib] NPC: Death Judgment: Shenzhen Pilgrim_SubState"""
    event_m20_21_x64(z148=40, z149=104123)

def event_m20_21_111185():
    """OBJ: Shenzhen Pilgrim: Appearance Judgment"""
    """State 0,1: [Lib] NPC: Shenzhen Pilgrim: Appearance Judgment_SubState"""
    event_m20_21_x52(z179=102316, z180=102323, z181=102331, z182=102333, z183=102315, z184=102317, z185=103623)

def event_m20_21_111242():
    """OBJ: Moonlight Jun: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_21_x1(z255=104162, z256=20214200, z257=61, z258=7430)

def event_m20_21_111243():
    """OBJ: Satoshi Moonlight: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7430:Benhart of Jugo
    event_m20_21_x8(z239=221010140, z240=221020141, z241=104160, z242=20214200, z243=111242, npc1=7430)

def event_m20_21_111244():
    """OBJ: Satoshi Moonlight: Judgment of death"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m20_21_x10(z233=60, z234=104162)

def event_m20_21_111245():
    """OBJ: Tsukimitsu: Appearance judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m20_21_x36(z209=104160, z210=102421, z211=102422, z212=221020147, z213=103661)

def event_m20_21_111246():
    """OBJ: Satoshi Moonlight: Defeat Queen Armor: White Phantom Sign Display"""
    """State 0,2: [Lib] NPC White Phantom Appearance: General Purpose: Akira Moonlight_SubState"""
    event_m20_21_x179(z41=104160, z42=678, z43=104160, z44=103660, z45=63)

def event_m20_21_111247():
    """OBJ: Satoshi Tsutsumi: Defeated Queen Armor: White Phantom"""
    """State 0: Start state"""
    assert GetEventFlag(221000001) != 1
    """State 1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m20_21_x59(z167=221000096, z168=102436, z169=205, z170=7430)

def event_m20_21_111248():
    """OBJ: Satoshi Tsutsumi: Defeat Mirror Knight: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m20_21_x47(z198=102431, z199=676, z200=104160, z201=63, z202=103660, z203=-1)

def event_m20_21_111249():
    """OBJ: Satoshi Tsutsumi: Defeat Mirror Knight: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m20_21_x59(z167=221000086, z168=102436, z169=205, z170=7430)

def event_m20_21_111322():
    """OBJ: Captive Girl: Grave"""
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Grave placement: branch"""
        CompareEventFlag(8, 104240, 1)
        CompareEventFlag(8, 102582, 0)
        IsGraveGeneratable(8, 7602, 1)
        if ConditionGroup(8):
            """State 4: Grave Placement: Death"""
            ChangeOwnObjState(20)
            CompareObjState(0, 20214300, 20, 0)
            assert ConditionGroup(0)
            """State 5: Grave Placement: Warp Move"""
            WarpObjToGeneratorPosition(20214300, 306)
        else:
            """State 3: Grave Placement: Survival"""
            ChangeOwnObjState(10)
            CompareObjState(0, 20214300, 10, 0)
            assert ConditionGroup(0)
    """State 6: Grave Placement: System: Finish"""
    EndMachine()

def event_m20_21_111323():
    """OBJ: Captive Girl: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7602:Imprisoned Milfanito
    event_m20_21_x8(z239=221010150, z240=221020151, z241=104240, z242=20214300, z243=111322, npc1=7602)

def event_m20_21_111325():
    """OBJ: Captive Girl: The Last Roar"""
    """State 0,4: Last voice: start"""
    CompareEventFlag(8, 221020157, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        pass
    else:
        Goto('L0')
    """State 5: Last hoarseness: System: End"""
    EndMachine()
    Quit()
    """State 3: Last voice: branch"""
    Label('L0')
    SetEventFlag(221020156, 1)
    CompareEventFlag(8, 221020156, 1)
    PlaySfxAtPoint(23000)
    CompareStateTime(8, 4.5, 3, 4.5)
    CompareEventFlag(8, 102581, 0)
    CompareStateTime(9, 4.5, 3, 4.5)
    CompareEventFlag(9, 221020156, 1)
    if ConditionGroup(8):
        """State 2: Last Hoar: Forced item acquisition"""
        # lot:1760200:Ring of the Dead
        AwardItem(1760200, 1)
        DeleteEnemyByGeneratorGroup(59, 0)
        SetEventFlag(102581, 1)
        CompareEventFlag(0, 102581, 1)
        assert ConditionGroup(0)
        """State 6: Last voice: Playback: Standby"""
        CompareEventFlag(8, 102582, 1)
        CompareObjState(8, 20213110, 80, 0)
        IsPlayerInsidePoint(8, 10000000, 10000000, 1)
        CompareEventFlag(8, 221020157, 0)
        assert ConditionGroup(8)
    elif ConditionGroup(9):
        pass
    """State 1: Last hoarseness: playback"""
    PlaySoundFollowingGenerator(6, 760203000, 305)

def event_m20_21_111326():
    """OBJ: Captive Girl: Last Hoar: For Stop"""
    """State 0,1: Stop judgment: Start"""
    CompareEventFlag(0, 102582, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Stop judgment: Standby"""
        IsPlayerInsidePoint(0, 10000010, 10000010, 1)
        assert ConditionGroup(0)
        """State 3: Stop judgment: Stop flag setting"""
        SetEventFlag(221020157, 1)
        CompareEventFlag(0, 221020157, 1)
        assert ConditionGroup(0)
    """State 4: Stop judgment: System: End"""
    EndMachine()

def event_m20_21_111435():
    """OBJ: Enclosed Person: Black Phantom Appearance"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m20_21_x60(z161=102810, z162=10002000, z163=670, z164=104340, z165=0, z166=2)

def event_m20_21_111800():
    """White Spirit: Mirror Night"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z178=679)

def event_m20_21_111801():
    """White phantom sign display for Anderu"""
    """State 0,1: Confirm the deal flag"""
    assert GetEventFlag(100747) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100972) != 0
    """State 2: NPC White Phantom Appearance: General Purpose: Andyel_SubState"""
    event_m20_21_x180(z36=100972, z37=680, z38=0, z39=0, z40=-1)

def event_m20_21_111802():
    """Small White Spirit: Lobby"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z178=681)

def event_m20_21_111803():
    """Kobaku Rei: Warrior in the Mirror"""
    """State 0,1: Golem lighthouse confirmation"""
    assert GetEventFlag(221000030) != 0 and GetEventFlag(221000031) != 0
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z178=682)

def event_m20_21_111804():
    """Small white spirit: key route"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z178=683)

def event_m20_21_118140():
    """Multi-use NPC: Meat Cut (Female): Black Phantom Appears"""
    """State 0,2: [Lib] [BEST] NPC Black Phantom Appearance: Online: Miracles"""
    event_m20_21_x72(z136=10001000, z137=671, z138=104320, z139=0, z140=1)

def event_m20_21_120080():
    """Trophy: Deep Darkness Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_21_x62(z155=221020109, z156=26)
    """State 1: System: Exit"""
    EndMachine()

def event_m20_21_120110():
    """Trophy: Moonlight Sword"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_21_x62(z155=221020148, z156=31)
    """State 1: System: Exit"""
    EndMachine()

def event_m20_21_4000000():
    """[BEST] End OBJ management"""
    """State 0,3: [BEST] [Preset] End OBJ Management_SubState"""
    call = event_m20_21_x191(z31=20211800, z32=20211810)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m20_21_4001000():
    """[BEST] Andyel_initial placement change"""
    """State 0,2: [BEST] [Preset] Anderel_Initial layout change_SubState"""
    assert event_m20_21_x192(z14=910, z15=1105000, z16=221000007, z17=221000006, z18=221000001)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4010000():
    """[BEST] Disabling damage"""
    """State 0,2: White Spirit Vangal: Disabling Andiel's Fire Sled"""
    SetDamageImmunityByGeneratorId(677, 169200501, 1)
    SetDamageImmunityByGeneratorId(677, 169200511, 1)
    """State 1: White Spirit Banholt: Disabling Andiel's Fire Sled"""
    SetDamageImmunityByGeneratorId(678, 169200501, 1)
    SetDamageImmunityByGeneratorId(678, 169200511, 1)
    """State 3: Finish"""
    EndMachine()

def event_m20_21_4011000():
    """[DC] Flag switching with king's ring equipment"""
    """State 0,3: [DC] [Preset] Flag switch with king's ring equipment_SubState"""
    call = event_m20_21_x206(z3=221020042)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()

def event_m20_21_4012000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m20_21_x76(z119=221020043, z120=14, z121=221000044, z122=3, z123=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m20_21_x81(z129=80000000, z130=0, z131=5, z132=968, val2=1, z133=10, z134=80000001,
                z135=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m20_21_x81(z129=80000100, z130=0, z131=5, z132=968, val2=2, z133=10, z134=80000101,
                z135=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m20_21_x81(z129=80000200, z130=0, z131=5, z132=968, val2=3, z133=10, z134=80000201,
                z135=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(221020045, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4012010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m20_21_x84(z126=221000044, z127=968, mode4=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4013000():
    """[DC] Mask is activated in treasure chest"""
    """State 0,2: [DC] [Preset] Mask is activated in the treasure box_SubState"""
    assert event_m20_21_x210(z1=20215170, z2=221000025)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_21_x88(z124=9200, z125=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_21_x88(z124=9201, z125=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_21_x88(z124=9202, z125=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_21_4031000():
    """[DC] NPC White Spirit_Gesture Management_Mirror Night"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m20_21_x93(z116=221000086, z117=825, z118=221020088)
    """State 1: Finish"""
    EndMachine()

