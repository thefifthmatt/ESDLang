# -*- coding: utf-8 -*-
def event_m20_21_1000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_21_x38(z183=20211600, z184=20, z185=100000, z186=0, z187=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_2000():
    """Key door that opens with "Corridor key" """
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m20_21_x9(z211=1005, z212=1105, z213=50610000, z214=221000020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_3000():
    """Lever door between soldiers"""
    """State 0,2: [Preset] Lever door between soldiers_SubState"""
    assert event_m20_21_x170(z43=20212000, z44=20211520, z45=20210410, z46=300000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4000():
    """OBJ: Shenzhen Pilgrim: Magic Circle Open"""
    """State 0,1: [Lib] Pilgrim of Shenzhen: Magic Square: Open_SubState"""
    event_m20_21_x4(z228=102326, z229=102329, z230=20213000)
    Quit()

def event_m20_21_4001():
    """OBJ: Shenzhen Pilgrim: Magic Warp"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Key Guide_SubState"""
    event_m20_21_x6(z220=102326, z221=20213000, z222=102329, z223=400020, z224=0)
    Quit()

def event_m20_21_4002():
    """OBJ: Shenzhen Pilgrim: Magic Circle Opening"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Opening Production_SubState"""
    event_m20_21_x5(z225=20213000, z226=102326, z227=221020107)
    Quit()

def event_m20_21_5000():
    """Elevator 昇降 Amana Altar"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(5030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m20_21_x18(z165=20213100, z166=500010, z167=500000, z168=20211500, z169=20211510)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_5010():
    """Elevator lever message display_upper"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z201=20213100, z202=20211500, z203=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_5020():
    """Elevator lever message display_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z201=20213100, z202=20211510, z203=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_5030():
    """Elevator_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m20_21_x31(z198=20213100, z199=40, flag23=221000015, z200=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_5040():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m20_21_x46(z170=504000, z171=20213100, z172=105430, z173=10, z174=20, z175=0, z176=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_5050():
    """_PC forced death for connection"""
    """State 0,2: [Lib] [Preset] [Asynchronous] Player forced fall death_SubState"""
    assert event_m20_21_x65(z126=505000, z127=3)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_5060():
    """For connection_Connection flag OFF"""
    """State 0,3: [Lib] [Preset] Switch the connection flag at the point _SubState"""
    call = event_m20_21_x71(z121=506000, z122=506000, z123=105430, z124=0, z125=1)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m20_21_6000():
    """Golem door 01"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z96=20210400, z97=221000033, z98=6.7, z99=600000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6010():
    """Golem door 02"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z96=20210401, z97=221000034, z98=6.7, z99=601000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6020():
    """Golem door 03"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z96=20210402, z97=221000035, z98=6.7, z99=602000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6030():
    """Golem door 04"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z96=20210403, z97=221000036, z98=6.7, z99=603000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6040():
    """Golem door 05"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z96=20210404, z97=221000037, z98=6.7, z99=604000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6050():
    """Golem door 06"""
    """State 0,2: [Preset] Golem Door_SubState"""
    assert event_m20_21_x97(z96=20210405, z97=221000038, z98=6.7, z99=605000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6100():
    """Main gate golem_Right"""
    """State 0,2: [Preset] Golem_Main Gate_SubState"""
    assert event_m20_21_x109(z47=20212500, z48=20212600, z49=221000039, z50=7.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6105():
    """Main gate golem_Left"""
    """State 0,2: [Preset] Golem_Main Gate_SubState"""
    assert event_m20_21_x109(z47=20212505, z48=20212605, z49=221000040, z50=7.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_6110():
    """The main gate of the golem"""
    """State 0,2: [Preset] Golem Main Gate_SubState"""
    assert (event_m20_21_x160(z56=20210407, z57=20212600, z58=20212605, z59=221000041, z60=20212500,
            z61=20212505))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_7000():
    """Boss: Heavy cavalry: Soldier only 2 battles_battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m20_21_x11(flag24=221000081, z204=700000, z205=700000, z206=202, z207=1021000, z208=221020080,
            mode5=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_7010():
    """Boss: Heavy cavalry: Soldier only 2 battles_Light switching"""
    """State 0,2: [Preset] Boss: Heavy cavalry: Soldier only 2 battles_Light switch_SubState"""
    assert event_m20_21_x175(z38=20210001, z39=20210002, z40=701000, z41=701002)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_8000():
    """Boss: Mirror Knight_Battle"""
    """State 0,2: [Preset] Mirror Night Battle Start_SubState"""
    assert (event_m20_21_x167(flag9=221000086, z51=800000, z52=800000, z53=201, z54=1021010, z55=221020085,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_9000():
    """King's door"""
    """State 0,3: [Preset] Door of the King_SubState"""
    call = event_m20_21_x98(z27=20210406, z28=900000, z29=221000021)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_21_10000():
    """Acid spitting dragon statue"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z94=20211100, z95=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_10010():
    """Acid spitting dragon statue_2"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z94=20211105, z95=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_10020():
    """Acid spitting dragon statue_3"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z94=20211110, z95=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_10030():
    """Acid spitting dragon statue_4"""
    """State 0,2: [Preset] Acid spitting dragon statue_SubState"""
    assert event_m20_21_x106(z94=20211115, z95=4, mode3=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_11000():
    """Boss Battle: Queen Knight AC, Queen"""
    """State 0,3: [Preset] Boss Battle: Queen's Knight_SubState"""
    call = event_m20_21_x123(z5=1100000, z6=1100000, z7=102, z8=1021020, z9=221020090, flag2=100972,
                             flag3=221000091, z10=1021021)
    if call.Get() == 7:
        """State 2: White door control flag ON"""
        Label('L0')
        SetEventFlag(221000092, 1)
    elif call.Get() == 4:
        """State 7: [Preset] Boss Battle: Andyel_SubState"""
        assert event_m20_21_x184(z20=1200010, z21=1200011, z22=701, z23=1021040, z24=221020005, flag6=221000006)
    elif call.Get() == 6:
        """State 8: [Preset] Boss Battle: Queen_C_2 Series Battle_SubState"""
        assert (event_m20_21_x128(z79=1200000, z80=1200000, z81=101, z82=1021031, z83=221020095, flag13=221000096,
                z84=221000097))
        """State 9: [Preset] Boss Battle: Andyel_Sequential Battle_SubState"""
        Label('L1')
        assert (event_m20_21_x197(z15=701, z16=1021040, z17=221020005, flag5=221000006, z18=1200010,
                z19=1200011))
    elif call.Get() == 1:
        """State 4: [Preset] Boss Battle: Queen_A_SubState"""
        assert (event_m20_21_x128(z79=1200000, z80=1200000, z81=101, z82=1021030, z83=221020095, flag13=221000096,
                z84=221000097))
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 2:
        Goto('L0')
    elif call.Get() == 3:
        """State 5: [Preset] Boss Battle: Queen_B_SubState"""
        assert (event_m20_21_x128(z79=1200001, z80=1200001, z81=101, z82=1021030, z83=221020095, flag13=221000096,
                z84=221000098))
    elif call.Get() == 5:
        """State 6: [Preset] Boss Battle: Queen_C_3 Consecutive_SubState"""
        assert (event_m20_21_x128(z79=1200001, z80=1200001, z81=101, z82=1021031, z83=221020095, flag13=221000096,
                z84=221000098))
        Goto('L1')
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_11010():
    """Queen Knight AC_Destroy"""
    """State 0,2: [Preset] Queen Knight AC_Destroy_SubState"""
    assert event_m20_21_x132(z73=860, z74=862, z75=93320030, z76=93340030, flag12=221000091)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_12010():
    """Boss Battle_Poly Drama: Queen Knight, Queen"""
    """State 0,2: [Preset] Poly Play Management: Queen Knight, Queen_SubState"""
    assert event_m20_21_x126()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_13000():
    """Elevator_in front of corridor"""
    """State 0,2: Has the elevator golem event been completed?"""
    assert EventEnded(13030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m20_21_x18(z165=20213110, z166=1300000, z167=1300010, z168=20211540, z169=20211530)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_13010():
    """Elevator_in front of corridor_lever message_up"""
    """State 0,2: Has the elevator golem event been completed?"""
    assert EventEnded(13030) != 0
    """State 3: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z201=20213110, z202=20211540, z203=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_13020():
    """Elevator_in front of corridor_lever message_bottom"""
    """State 0,2: Has the elevator golem event been completed?"""
    assert EventEnded(13030) != 0
    """State 3: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m20_21_x23(z201=20213110, z202=20211530, z203=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_21_13030():
    """Elevator golem activation"""
    """State 0,2: [Preset] Elevator Golem Activation_SubState"""
    assert (event_m20_21_x113(z87=20212520, z88=20212620, z89=20213110, z90=20211530, z91=20211540, z92=7.5,
            flag15=221000010, flag16=221000032))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_14000():
    """[Preliminary] Portrait of the Queen"""
    """State 0,1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_15000():
    """White door management during splicing"""
    """State 0,2: [Preset] White door management during sublimation_SubState"""
    assert event_m20_21_x120()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_16000():
    """End roll"""
    """State 0,2: [Preset] End roll_SubState"""
    assert event_m20_21_x136(z69=1600000, flag11=221000094, z70=221020002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_17000():
    """Setting retry points after defeating the Queen"""
    """State 0,2: [Preset] Retry point setting after defeating the Queen_SubState"""
    assert event_m20_21_x140(flag10=221000093)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_19000():
    """Golems that move by sucking souls_1"""
    """State 0,2: [Preset] Golem that moves by sucking a soul (lights on) _SubState"""
    assert event_m20_21_x141(z65=20212510, z66=20212700, z67=221000030, z68=6.7)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_19010():
    """Golem that moves by sucking a soul (lights on) _2"""
    """State 0,2: [Preset] Golem that moves by sucking a soul (lights on) _SubState"""
    assert event_m20_21_x141(z65=20212515, z66=20212705, z67=221000031, z68=6.7)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_20000():
    """Statue of Nation 1"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z63=3010, z64=20211001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_20010():
    """Statue Neck Drop_2"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z63=3020, z64=20211000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_20020():
    """Statue of Neck _3"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z63=3030, z64=20211002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_20030():
    """Statue Neck Drop_4"""
    """State 0,2: [Preset] Drop of Statue Night_SubState"""
    assert event_m20_21_x148(z63=3040, z64=20211003)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_21000():
    """Key person"""
    """State 0,3: [SFX] Stop SFX generated by you"""
    call = event_m20_21_x150(z62=20211700)
    if call.Get() == 2:
        """State 2: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_21_22000():
    """Vegrant Deletion Decision_Left"""
    """State 0,2: [Preset] Vegrant deletion determination_SubState"""
    assert event_m20_21_x174(z42=8000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_22010():
    """Vegrant Deletion Decision_Right"""
    """State 0,2: [Preset] Vegrant deletion determination_SubState"""
    assert event_m20_21_x174(z42=8010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_80000():
    """Rebirth Fire 01_In front of the King's door to the last boss"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_21_x58(z150=2021000, z151=2021099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_81000():
    """After the fire of rebirth 02_ boss heavy cavalry"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_21_x58(z150=2021100, z151=2021199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_82000():
    """Reproduction of fire 03_in the hidden door"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_21_x58(z150=2021200, z151=2021299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_90000():
    """Trophy_Knight of the Mirror"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_21_x62(flag21=221000086, z135=10)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_x0(z71=_, val1=1600010, flag25=0, z235=0, z236=1):
    """[Lib] Normal poly play
    z71: Poly play ID
    val1: Destination point ID after poly play
    flag25: Poly drama played flag
    z235: End fade
    z236: Start fade
    """
    """State 0,6: Wait for in-game start"""
    assert InGame() != 0
    """State 5: Played judgment"""
    if GetEventFlag(flag25) != 1:
        """State 1: Poly play"""
        PlayCutscene(z71, z235, z236)
        assert (CutscenePlaying() == 1) != 0
        """State 4: Poly Play Pre Warp"""
        WarpPlayersWithinMapIf((val1 > 1) != 0, val1)
        """State 3: During the poly play"""
        assert (not CutscenePlaying()) != 0
    else:
        pass
    """State 2: Warp after the poly drama"""
    WarpPlayersWithinMapIf((val1 > 1) != 0, val1)
    SetEventFlag(flag25, 1)
    """State 7: End state"""
    return 0

def event_m20_21_x1(z231=_, z232=_, z233=_, z234=_):
    """[Lib] NPC: Grave Placement: General purpose
    z231: Death map: Global event flag
    z232: Tomb: OBJ instance ID
    z233: Tomb move to: Generator ID
    z234: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z231, 1)
    IsGraveGeneratable(8, z234, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z232, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z232, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m20_21_x2(z217=_, z218=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z217: Global: death flag
    z218: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z218, 10, 0)
    CompareObjState(1, z218, 20, 0)
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
    IsObjSearched(0, z218)
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

def event_m20_21_x3(z215=_, z216=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z215: Area other flags: Ghost appearance
    z216: Area other flags: Conversation start
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
    SetEventFlag(z215, 1)
    CompareEventFlag(0, z215, 1)
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
    SetEventFlag(z216, 1)
    CompareEventFlag(0, z216, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m20_21_x4(z228=102326, z229=102329, z230=20213000):
    """[Lib] Shenzhen Pilgrim: Magic Square: Open
    z228: Magic Square: Open: Global Event Flag
    z229: Magic Square: Invasion: Global Event Flag
    z230: Magic Square: OBJ instance ID
    """
    """State 0,1: Magic Square: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Magic square: All open judgment"""
        CompareEventFlag(8, 100979, 1)
        CompareEventFlag(8, z228, 1)
        CompareEventFlag(9, 100979, 1)
        CompareEventFlag(8, z228, 0)
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
            CompareObjState(0, z230, 30, 0)
            assert ConditionGroup(0)
        else:
            """State 3: Magic Square: Player Return Judgment"""
            CompareEventFlag(8, z228, 1)
            CompareEventFlag(8, z229, 1)
            if ConditionGroup(8):
                """State 4: Magic square: Flag initialization setting"""
                SetEventFlag(z228, 0)
                SetEventFlag(z229, 0)
                CompareEventFlag(8, z228, 0)
                CompareEventFlag(8, z229, 0)
                assert ConditionGroup(8)
                """State 8: Magic Square: Erasure"""
                ChangeOwnObjState(80)
                CompareObjState(0, z230, 10, 0)
                assert ConditionGroup(0)
            else:
                """State 6: Magic Square: Open Flag Judgment"""
                CompareEventFlag(0, z228, 1)
                if ConditionGroup(0):
                    Goto('L0')
                else:
                    pass
    """State 5: Magic Square: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 10: End state"""
    return 0

def event_m20_21_x5(z225=20213000, z226=102326, z227=221020107):
    """[Lib] Shenzhen Pilgrims: Magic Square: Opening Production
    z225: Magic Square: OBJ instance ID
    z226: Magic Square: Open: Global Event Flag
    z227: Magic Square: Production Start: Area and Other Flags
    """
    """State 0,4: Appearance production: Start"""
    CompareEventFlag(0, z227, 1)
    assert ConditionGroup(0)
    """State 3: Appearance effect: Open flag setting"""
    SetEventFlag(z226, 1)
    CompareEventFlag(0, z226, 1)
    assert ConditionGroup(0)
    """State 1: Appearance Direction: Magic Square Appearance"""
    ChangeOwnObjState(70)
    CompareObjState(0, z225, 30, 0)
    assert ConditionGroup(0)
    """State 5: Appearance production: End"""
    SetEventFlag(z227, 0)
    CompareEventFlag(0, z227, 0)
    assert ConditionGroup(0)
    """State 2: Appearance production: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m20_21_x6(z220=102326, z221=20213000, z222=102329, z223=400020, z224=0):
    """[Lib] Shenzhen Pilgrim: Magic Square: Key Guide
    z220: Magic Square: Open: Global Event Flag
    z221: Magic Square: OBJ instance ID
    z222: Magic Square: Invasion: Global Event Flag
    z223: Magic Square: Warp Point
    z224: Magic Square: During Warp: Area Other Flag
    """
    """State 0,1: Key guide: Start"""
    CompareObjState(0, z221, 30, 0)
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
        IsObjSearched(2, z221)
        CompareObjState(3, z221, 10, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(2):
            """State 7: Key guide: Intrusion flag: Setting"""
            ProhibitMultiplayer(1)
            SetEventFlag(z224, 1)
            """State 8: Shenzhen Pilgrim: Magic Square: Warp_SubState"""
            call = event_m20_21_x7(z223=z223, z222=z222)
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
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m20_21_x7(z223=400020, z222=102329):
    """Shenzhen Pilgrim: Magic Square: Warp
    z223: Warp point ID
    z222: Intrusion: Global flag
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
            SetEventFlag(z222, 1)
            PlayCutsceneAndWarpToMap(0, 0, 40030000, z223, 0)
            assert CutsceneWarpEnded() != 0
            """State 2: Warp: Wait for completion"""
            CompareEventFlag(0, 0, 1)
            assert ConditionGroup(0)
            """State 6: Normal: End state"""
            return 0
    """State 7: Re-execution: end state"""
    return 1

def event_m20_21_x8(z215=_, z216=_, z217=_, z218=_, z219=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z215: Ghost Appearance: Area Other Flag
    z216: Conversation start: Area and other flags
    z217: Death: Global event flag
    z218: Tomb: OBJ instance ID
    z219: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z219, 1, 0)
    CompareEventFlag(9, z215, 1)
    CompareObjState(9, z218, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z216, 1)
        CompareEventFlag(0, z216, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m20_21_x2(z217=z217, z218=z218, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m20_21_x3(z215=z215, z216=z216, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m20_21_x9(z211=1005, z212=1105, z213=50610000, z214=221000020):
    """[Lib] Item specified door unlocking_2
    z211: Text ID when opened
    z212: Text ID when not opened
    z213: item
    z214: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z213, z211, z212, z214, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x10(z209=60, z210=104162):
    """[Lib] NPC: Death determination: General purpose
    z209: Generator ID
    z210: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z210, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z209)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z210, 1)
            CompareEventFlag(0, z210, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m20_21_x11(flag24=221000081, z204=700000, z205=700000, z206=202, z207=1021000, z208=221020080,
                     mode5=0):
    """[Lib] [Preset] Boss Battle Start
    flag24: Boss destruction flag
    z204: Start point ID
    z205: End point ID
    z206: Sound ID
    z207: Boss Battle ID
    z208: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(flag5=flag24)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m20_21_x13(z204=z204, z205=z205)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m20_21_x14(z81=z206, z82=z207, z83=z208)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z16=z207)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m20_21_x17(z15=z206, z16=z207, z17=z208, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m20_21_x12(flag5=_):
    """[Reproduction] Boss Battle_Start
    flag5: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_21_x13(z204=700000, z205=700000):
    """[Condition] Boss Battle_Start
    z204: Start point ID
    z205: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z204, z205, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z204, z205, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x14(z81=_, z82=_, z83=_):
    """[Execution] Boss Battle_Start
    z81: Sound ID
    z82: Boss Battle ID
    z83: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z81)
    """State 1: Boss battle start notification"""
    StartBossFight(z82)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z83, 1)
    """State 4: End state"""
    return 0

def event_m20_21_x15():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x16(z16=_):
    """[Condition] Boss Battle_End Judgment
    z16: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z16, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x17(z15=_, z16=_, z17=_, mode5=0):
    """[Execute] Boss Battle_End
    z15: Sound ID
    z16: Boss Battle ID
    z17: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z17, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z16)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z15)
    """State 5: End state"""
    return 0

def event_m20_21_x18(z165=_, z166=_, z167=_, z168=_, z169=_):
    """[Lib] [Preset] Elevator
    z165: OBJ instance ID of the elevator
    z166: On elevator point ID_
    z167: Elevator point ID_below
    z168: Upper lever OBJ instance ID
    z169: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m20_21_x19()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m20_21_x20(z165=z165, z166=z166, z167=z167, z168=z168, z169=z169)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m20_21_x51(z165=z165, z167=z167)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m20_21_x50(z165=z165, z166=z166)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m20_21_x21(z165=z165, z166=z166)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m20_21_x22(z165=z165, z167=z167)
    """State 7: End state"""
    return 0

def event_m20_21_x19():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x20(z165=_, z166=_, z167=_, z168=_, z169=_):
    """[Condition] Elevator
    z165: Elevator OBJ instance ID
    z166: On elevator point ID_
    z167: Elevator point ID_below
    z168: Upper lever OBJ instance ID
    z169: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z165, 10, 0)
    CompareObjState(1, z165, 40, 0)
    CompareObjState(2, z165, 80, 0)
    CompareObjState(2, z165, 41, 0)
    CompareObjState(3, z165, 70, 0)
    CompareObjState(3, z165, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z167, z167, 1)
        CompareObjState(0, z168, 74, 0)
        CompareObjState(0, z168, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z166, z166, 1)
        CompareObjState(0, z169, 74, 0)
        CompareObjState(0, z169, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m20_21_x21(z165=_, z166=_):
    """[Execution] Elevator_Rise
    z165: Elevator OBJ instance ID
    z166: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z165, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z165, 30, 0)
    IsPlayerInsidePoint(8, z166, z166, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z165, 71)
    assert CompareObjStateId(z165, 40, 0)
    """State 4: End state"""
    return 0

def event_m20_21_x22(z165=_, z167=_):
    """[Execution] Elevator_Descent
    z165: Elevator OBJ instance ID
    z167: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z165, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z165, 41, 0)
    IsPlayerInsidePoint(8, z167, z167, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z165, 81)
    assert CompareObjStateId(z165, 10, 0)
    """State 4: End state"""
    return 0

def event_m20_21_x23(z201=_, z202=_, z203=_):
    """[Lib] [Preset] Elevator lever
    z201: OBJ instance ID of the elevator
    z202: Lever OBJ instance ID
    z203: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m20_21_x24()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m20_21_x25(z201=z201, z202=z202, z203=z203)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m20_21_x26(z201=z201, z202=z202, z203=z203)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m20_21_x27(z201=z201, z202=z202, z203=z203)
    """State 5: Rerun"""
    return 0

def event_m20_21_x24():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x25(z201=_, z202=_, z203=_):
    """[Condition] Elevator lever_use judgment
    z201: OBJ instance ID of the elevator
    z202: Lever OBJ instance ID
    z203: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z201, z203, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m20_21_x26(z201=_, z202=_, z203=_):
    """[Execution] Elevator lever_Key guide valid
    z201: OBJ instance ID of the elevator
    z202: Lever OBJ instance ID
    z203: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z202, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z201, z203, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x27(z201=_, z202=_, z203=_):
    """[Execute] Elevator lever_key guide disabled
    z201: OBJ instance ID of the elevator
    z202: Lever OBJ instance ID
    z203: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z202, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z201, z203, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x28(flag23=221000015):
    """[Lib] [Reproduction] Elevator_Initialization
    flag23: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag23) != 0:
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

def event_m20_21_x30(z198=20213100, z199=40, flag23=221000015, z200=40):
    """[Lib] [Execution] Elevator_Initialization
    z198: Elevator OBJ instance ID
    z199: Initial position OBJ state ID
    flag23: Initialization completion flag
    z200: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z198, z199)
    assert CompareObjStateId(z198, z200, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag23, 1)
    """State 3: End state"""
    return 0

def event_m20_21_x31(z198=20213100, z199=40, flag23=221000015, z200=40):
    """[Lib] [Preset] Elevator_Initialization
    z198: Elevator OBJ instance ID
    z199: Initial position OBJ state ID
    flag23: Initialization completion flag
    z200: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m20_21_x28(flag23=flag23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m20_21_x29()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m20_21_x30(z198=z198, z199=z199, flag23=flag23, z200=z200)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m20_21_x32(flag14=_):
    """[Reproduction] Boss Battle_Poly Play Replay
    flag14: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(flag14) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m20_21_x33(z193=20210607):
    """[Condition] Boss Battle_Poly Play Replay
    z193: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z193, 100, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x34(z85=_, flag14=_, z86=_, z197=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z85: Poly play ID
    flag14: Poly drama played flag
    z86: Warp point ID
    z197: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z85, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(flag14, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z86)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m20_21_x35(z193=20210607, z194=202110, flag22=221000097, z195=1201000, z196=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z193: White door instance ID
    z194: Poly play ID
    flag22: Poly drama played flag
    z195: Warp point ID
    z196: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m20_21_x32(flag14=flag22)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m20_21_x33(z193=z193)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m20_21_x34(z85=z194, flag14=flag22, z86=z195, z197=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_21_x36(z188=104160, z189=102421, z190=102422, z191=221020147, z192=103661):
    """[Lib] Appearance determination: General purpose
    z188: Death: Global event flag
    z189: Local emigration permission: Global event flag
    z190: Relocation permission after moving: Global event flag
    z191: Appearance determination: Area and other flags
    z192: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z188, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z189, 1)
            CompareEventFlag(8, z190, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z189, 1)
                CompareEventFlag(8, z192, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z191, 1)
                    CompareEventFlag(0, z191, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z191, 0)
                    CompareEventFlag(0, z191, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z191, 0)
        CompareEventFlag(0, z191, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m20_21_x37():
    """[Lib] [Reproduction] Dummy"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x38(z183=20211600, z184=20, z185=100000, z186=0, z187=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z183: Object instance ID
    z184: OBJ state ID
    z185: Navimesh switching point ID
    z186: Additional attributes
    z187: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m20_21_x39(z183=z183, z184=z184, z185=z185, z187=z187, z186=z186)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m20_21_x40(z183=z183, z184=z184, z185=z185)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m20_21_x41(z183=z183, z184=z184, z185=z185, z186=z186, z187=z187)
    """State 4: End state"""
    return 0

def event_m20_21_x39(z183=20211600, z184=20, z185=100000, z187=2, z186=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z183: Target OBJ instance ID
    z184: Target OBJ state ID
    z185: Navimesh switching point ID
    z187: Additional attributes
    z186: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z183, z184, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z185, z187)
        DeleteNavimeshAttribute(z185, z186)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m20_21_x40(z183=20211600, z184=20, z185=100000):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z183: Target OBJ instance ID
    z184: Target OBJ state ID
    z185: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z183, z184, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x41(z183=20211600, z184=20, z185=100000, z186=0, z187=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z183: Target OBJ instance ID
    z184: Target OBJ state ID
    z185: Navimesh switching point ID
    z186: Additional attributes
    z187: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z185, z186)
    DeleteNavimeshAttribute(z185, z187)
    """State 2: End state"""
    return 0

def event_m20_21_x42():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x43(z170=504000, z171=20213100, z173=10, z174=20):
    """[Lib] [Condition] Elevator_Connection replacement
    z170: Replacement point
    z171: OBJ instance ID of the elevator
    z173: Top_Hit group ID
    z174: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z170, z170, 1)
    CompareObjState(8, z171, 70, 0)
    IsPlayerInsidePoint(9, z170, z170, 1)
    CompareObjState(9, z171, 80, 0)
    IsPlayerOnHitGroup(0, z173, 1)
    IsPlayerOnHitGroup(1, z174, 1)
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

def event_m20_21_x44(z170=504000, z172=105430, z175=0, z173=10, z171=20213100):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z170: Replacement point
    z172: Global flag for connection
    z175: ON / OFF of global flag
    z173: Top_Hit group ID
    z171: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z172, z175)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z170, z170, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z173, 1)
    IsPlayerInsidePoint(8, z170, z170, 1)
    CompareObjState(8, z171, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x45(z172=105430, z175=0, z173=10, z170=504000, z171=20213100):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z172: Global flag for connection
    z175: ON / OFF of global flag
    z173: Hit group ID
    z170: Replacement point ID
    z171: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z172, z175)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z173, 0)
    IsPlayerInsidePoint(8, z170, z170, 1)
    CompareObjState(8, z171, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x46(z170=504000, z171=20213100, z172=105430, z173=10, z174=20, z175=0, z176=1):
    """[Lib] [Preset] Elevator_Connection replacement
    z170: Replacement point
    z171: OBJ instance ID of the elevator
    z172: Global flag for connection
    z173: Top_Hit group ID
    z174: Bottom_Hit group ID
    z175: Up_Global flag when rising
    z176: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m20_21_x42()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m20_21_x43(z170=z170, z171=z171, z173=z173, z174=z174)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m20_21_x44(z170=z170, z172=z172, z175=z175, z173=z173, z171=z171)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m20_21_x49(z170=z170, z172=z172, z176=z176, z174=z174, z171=z171)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m20_21_x45(z172=z172, z175=z175, z173=z173, z170=z170, z171=z171)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m20_21_x48(z172=z172, z176=z176, z174=z174, z170=z170, z171=z171)
    """State 7: End state"""
    return 0

def event_m20_21_x47(z177=102431, z178=676, z179=104160, z180=63, z181=103660, z182=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z177: White Phantom can appear: Global event flag
    z178: White Phantom: Generator ID
    z179: Death: Global event flag
    z180: Body: Generator group ID
    z181: Hostile: Global event flag
    z182: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z178)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z179, 1)
        CompareEventFlag(1, z181, 1)
        CompareEventFlag(2, z177, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z178)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z179, 1)
            CompareEventFlag(1, z181, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z178)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z179, 1)
            CompareEventFlag(1, z181, 1)
            HasNpcPhantomSpawned(2, z178, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z180, 0)
                HasNpcPhantomSpawned(0, z178, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z178)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m20_21_x48(z172=105430, z176=1, z174=20, z170=504000, z171=20213100):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z172: Global flag for connection
    z176: ON / OFF of global flag
    z174: Hit group ID
    z170: Replacement point ID
    z171: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z172, z176)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z174, 0)
    IsPlayerInsidePoint(8, z170, z170, 1)
    CompareObjState(8, z171, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x49(z170=504000, z172=105430, z176=1, z174=20, z171=20213100):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z170: Replacement point
    z172: Global flag for connection
    z176: ON / OFF of global flag
    z174: Bottom_Hit group ID
    z171: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z172, z176)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z170, z170, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z174, 1)
    IsPlayerInsidePoint(8, z170, z170, 1)
    CompareObjState(8, z171, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x50(z165=_, z166=_):
    """[Execution] Elevator_Return switch after lift
    z165: Elevator OBJ instance ID
    z166: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z165, 30, 0)
    IsPlayerInsidePoint(8, z166, z166, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z165, 71)
    assert CompareObjStateId(z165, 40, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x51(z165=_, z167=_):
    """[Execution] Elevator_Return switch after descending
    z165: Elevator OBJ instance ID
    z167: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z165, 41, 0)
    IsPlayerInsidePoint(8, z167, z167, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z165, 81)
    assert CompareObjStateId(z165, 10, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x52(z158=102316, z159=102323, z160=102331, z161=102333, z162=102315, z163=102317, z164=103623):
    """[Lib] NPC: Shenzhen Pilgrims: Appearance Judgment
    z158: Generation stop: Global event flag
    z159: Appearance permission: Global event flag
    z160: Sub 1 encountering: Global event flag
    z161: During sub-2 encounter: Global event flag
    z162: Sub 1 generation stop: Global event flag
    z163: Sub 2 generation stop: Global event flag
    z164: Hostile map: Global event flag
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
                CompareEventFlag(0, z158, 1)
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
                        CompareEventFlag(8, z160, 1)
                        CompareEventFlag(8, z162, 0)
                        CompareEventFlag(9, z161, 1)
                        CompareEventFlag(9, z163, 0)
                        if ConditionGroup(8):
                            pass
                        elif ConditionGroup(9):
                            pass
                        else:
                            Goto('L1')
                """State 5: Appearance judgment: Appearance impossible"""
                Label('L0')
                SetEventFlag(z159, 0)
                CompareEventFlag(0, z159, 0)
                assert ConditionGroup(0)
                Goto('L2')
            """State 6: Appearance determination: Appearance allowed"""
            Label('L1')
            SetEventFlag(z159, 1)
            CompareEventFlag(0, z159, 1)
            assert ConditionGroup(0)
    """State 3: Appearance determination: System: End"""
    Label('L2')
    EndMachine()
    Quit()
    """Unused"""
    """State 10: Appearance determination: Reappearance setting"""
    CompareEventFlag(8, z158, 0)
    CompareEventFlag(8, z164, 0)
    if ConditionGroup(8):
        Goto('L1')
    else:
        Goto('L0')
    """State 11: End state"""
    return 0

def event_m20_21_x53(z157=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z157: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z157)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m20_21_x54(z152=104160, z153=678, z154=104160, z155=103660, z156=63):
    """[Lib] NPC white phantom appearance: General purpose: OFF
    z152: White Phantom can appear: Global event flag
    z153: White Phantom: Generator ID
    z154: Death: Global event flag
    z155: Hostile: Global event flag
    z156: Body: Generator group ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z153)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z154, 1)
        CompareEventFlag(1, z155, 1)
        CompareEventFlag(2, z152, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z153)
            """State 7: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z154, 1)
            CompareEventFlag(1, z155, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 8: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z153)
            """State 4: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z154, 1)
            CompareEventFlag(1, z155, 1)
            HasNpcPhantomSpawned(2, z153, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 5: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z156, 0)
                HasNpcPhantomSpawned(0, z153, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 9: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z153)
    """State 10: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m20_21_x55():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x56(z150=_, z151=_):
    """[Lib] [execute] Rebirth fire
    z150: Flag start ID
    z151: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z150, z151, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x57():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x58(z150=_, z151=_):
    """[Lib] [Preset] Rebirth
    z150: Flag start ID
    z151: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m20_21_x55()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m20_21_x57()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m20_21_x56(z150=z150, z151=z151)
    """State 4: End state"""
    return 0

def event_m20_21_x59(z146=_, z147=102436, z148=205, z149=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z146: Defeat Boss 1: Area and other flags
    z147: Summon Achievement: Global Event Flag
    z148: Summon achievement count: global variable
    z149: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z147, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z146, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z148, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z148, NpcInfoValue(z149, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z147, 1)
                CompareEventFlag(0, z147, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m20_21_x60(z140=102810, z141=10002000, z142=670, z143=104340, z144=0, z145=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z140: Summoning conditions: Global event flag
    z141: Summon range
    z142: Generator ID
    z143: Death: Global event flag
    z144: Appearance: Minimum time
    z145: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z143, 1)
        CompareEventFlag(8, z140, 1)
        IsPlayerInsidePoint(8, z141, z141, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z143, 1)
            CompareStateTime(1, z144, 3, z145)
            IsPlayerInsidePoint(2, z141, z141, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z142)
                HasNpcPhantomSpawned(0, z142, 1)
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

def event_m20_21_x61(z136=10001000, z137=671, z138=0, z139=1):
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
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m20_21_x62(flag21=_, z135=_):
    """[Lib] [Preset] Get trophy
    flag21: Acquisition trigger_other flags
    z135: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag21) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag21, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z135)
    """State 4: End state"""
    return 0

def event_m20_21_x63(z130=102010, z131=677, z132=104000, z133=103500, z134=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z130: White Phantom can appear: Global event flag
    z131: White Phantom: Generator ID
    z132: Death: Global event flag
    z133: Hostile: Global event flag
    z134: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z131)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z132, 1)
        CompareEventFlag(1, z133, 1)
        CompareEventFlag(2, z130, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z131)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z132, 1)
            CompareEventFlag(1, z133, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z131)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z132, 1)
            CompareEventFlag(1, z133, 1)
            HasNpcPhantomSpawned(2, z131, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z131, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z131)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m20_21_x64(z128=40, z129=104123):
    """[Lib] NPC: Death Determination: Shenzhen Pilgrim
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
            IsChrDead(8, z128)
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
                SetEventFlag(z129, 1)
                CompareEventFlag(0, z129, 1)
                assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m20_21_x65(z126=505000, z127=3):
    """[Lib] [Preset] [Asynchronous] Player forced fall death
    z126: Point ID
    z127: Fall time
    """
    """State 0,1: [Lib] [Reproduction] Dummy_SubState"""
    assert event_m20_21_x37()
    """State 2: [Lib] [Condition] [Asynchronous] Player forced fall death_SubState"""
    assert event_m20_21_x66(z126=z126, z127=z127)
    """State 3: [Lib] [Execution] [Asynchronous] Player forced fall death_SubState"""
    assert event_m20_21_x67()
    """State 4: End state"""
    return 0

def event_m20_21_x66(z126=505000, z127=3):
    """[Lib] [Condition] [Asynchronous] Player forced fall death
    z126: Point ID
    z127: Fall time
    """
    """State 0,1: Judgment"""
    IsPlayerInsidePoint(8, z126, z126, 1)
    ComparePlayerFallTime(8, z127, 3)
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

def event_m20_21_x69(z121=506000, z122=506000):
    """[Lib] [Condition] Switch the connection flag at the point
    z121: Start point ID
    z122: End point ID
    """
    """State 0,1: Are you in point?"""
    IsPlayerInsidePoint(0, z121, z122, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x70(z123=105430, z124=0, z125=1):
    """[Lib] [Execution] Switch to the connection flag at the point
    z123: Global event flag for connection
    z124: Flag switching
    z125: Wait for next judgment
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z123, z124)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z123, z124)
    assert ConditionGroup(0)
    """State 3: For next judgment: Has the flag changed?"""
    CompareEventFlag(0, z123, z125)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x71(z121=506000, z122=506000, z123=105430, z124=0, z125=1):
    """[Lib] [Preset] Switch the connection flag at the point
    z121: Start point ID
    z122: End point ID
    z123: Global event flag for connection
    z124: Flag switching
    z125: Wait for next judgment
    """
    """State 0,1: [Lib] [Reproduction] Switch the connection flag at the point _SubState"""
    call = event_m20_21_x68()
    if call.Get() == 0:
        """State 3: [Lib] [Condition] Switch connection flag at point _SubState"""
        assert event_m20_21_x69(z121=z121, z122=z122)
        """State 2: [Lib] [Execution] Switch to the connection flag at the point _SubState"""
        assert event_m20_21_x70(z123=z123, z124=z124, z125=z125)
        """State 4: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 5: Guest: Exit"""
        return 1

def event_m20_21_x72(z116=10001000, z117=671, z118=104320, z119=0, z120=1):
    """[Lib] [BEST] NPC Black Phantom Appearance: Online: Miracle Person _ When Living
    z116: Summon range
    z117: Generator ID
    z118: Death: Global event flag
    z119: Appearance: Minimum time
    z120: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z118, 1)
        IsPlayerInsidePoint(1, z116, z116, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z118, 1)
            CompareStateTime(1, z119, 3, z120)
            IsPlayerInsidePoint(2, z116, z116, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z117)
                HasNpcPhantomSpawned(0, z117, 1)
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

def event_m20_21_x73(flag18=221020043, flag19=221000044):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag18: Lottery determination flag
    flag19: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag19) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag18) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m20_21_x74(z102=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z102: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z102, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m20_21_x75(flag18=221020043, z103=3, z104=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag18: Lottery determination flag
    z103: Number of appearance judgment points
    z104: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag18, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z103)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z104, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m20_21_x76(flag18=221020043, z102=14, flag19=221000044, z103=3, z104=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag18: Lottery determination flag
    z102: Random number comparison value
    flag19: Defeat flag
    z103: Number of appearance judgment points
    z104: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m20_21_x73(flag18=flag18, flag19=flag19)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m20_21_x74(z102=z102)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m20_21_x75(flag18=flag18, z103=z103, z104=z104)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m20_21_x89(flag18=flag18, z104=z104)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m20_21_x77(val2=_, z113=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z113: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z113) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m20_21_x78(z109=_, z110=0, z111=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z109: Appearance judgment point ID
    z110: Minimum appearance time
    z111: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z109, z109, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z110, 3, z111)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m20_21_x79(z112=968, z114=_, z115=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z112: Generator ID
    z114: Appearance start point ID
    z115: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z112, z114, z115)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z112)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m20_21_x80(flag20=221000044):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag20: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag20) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m20_21_x81(z109=_, z110=0, z111=5, z112=968, val2=_, z113=10, z114=_, z115=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z109: Intrusion detection point ID
    z110: Minimum appearance time
    z111: Maximum time to appear
    z112: Generator ID
    val2: Appearance judgment number
    z113: Lottery result point variable
    z114: Appearance start point ID
    z115: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m20_21_x77(val2=val2, z113=z113)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m20_21_x78(z109=z109, z110=z110, z111=z111)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m20_21_x79(z112=z112, z114=z114, z115=z115)
    """State 4: Finish"""
    return 0

def event_m20_21_x82(z107=968, mode4=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z107: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z107)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode4) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m20_21_x83(flag20=221000044, z108=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag20: Defeat flag
    z108: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag20, 1)
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
                    SetEventFlag(z108, 1)
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

def event_m20_21_x84(flag20=221000044, z107=968, mode4=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag20: Defeat flag
    z107: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m20_21_x80(flag20=flag20)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m20_21_x82(z107=z107, mode4=mode4)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m20_21_x83(flag20=flag20, z108=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m20_21_x83(flag20=flag20, z108=102755)
    """State 5: End state"""
    return 0

def event_m20_21_x85(z105=_, z106=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z105: Generator ID
    z106: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z105, z106)
    """State 2: End state"""
    return 0

def event_m20_21_x86(z105=_, z106=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z105: Generator ID
    z106: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z105, z106, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_21_x87(z105=_):
    """[Lib] [DC] [Condition] Transparent characters
    z105: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z105)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x88(z105=_, z106=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z105: Generator ID
    z106: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m20_21_x86(z105=z105, z106=z106)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m20_21_x87(z105=z105)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m20_21_x85(z105=z105, z106=z106)
    """State 4: End state"""
    return 0

def event_m20_21_x89(flag18=221020043, z104=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag18: Lottery determination flag
    z104: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag18, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z104, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x90(flag17=221000086):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag17: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag17) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_21_x91(z100=825):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z100: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z100, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x92(z101=221020088):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z101: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z101, 1)
    """State 2: End state"""
    return 0

def event_m20_21_x93(flag17=221000086, z100=825, z101=221020088):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag17: Boss destruction flag
    z100: Boss generator ID
    z101: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m20_21_x90(flag17=flag17)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m20_21_x91(z100=z100)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m20_21_x92(z101=z101)
    """State 4: End state"""
    return 0

def event_m20_21_x94(z96=_, z97=_, z98=6.7, z99=_):
    """[Reproduction] Golem door
    z96: Golem door instance ID
    z97: A flag to determine if the golem door has absorbed soul
    z98: Distance that golem door absorbs soul
    z99: Point ID for Navimesh change
    """
    """State 0,1: Is the door OBJ open?"""
    if CompareObjStateId(z96, 20, 0):
        """State 3: Navigation mesh change"""
        DeleteNavimeshAttribute(z99, 2)
        """State 5: Opened"""
        return 1
    else:
        """State 2: Absorption processing in Seoul"""
        AddSoulAcquisitionTarget(z96, z98, z97, 1, -1)
        """State 4: Not open"""
        return 0

def event_m20_21_x95(z97=_):
    """[Condition] Golem door
    z97: A flag to determine if the golem door has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z97, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x96(z96=_, z99=_):
    """[Execution] Golem door
    z96: Golem door instance ID
    z99: Point ID for Navimesh change
    """
    """State 0,1: OBJ state transition: door"""
    ChangeObjState(z96, 70)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z99, 2)
    """State 3: End state"""
    return 0

def event_m20_21_x97(z96=_, z97=_, z98=6.7, z99=_):
    """[Preset] Golem door
    z96: Golem door instance ID
    z97: A flag to determine if the golem door has absorbed soul
    z98: Distance that golem door absorbs soul
    z99: Point ID for Navimesh change
    """
    """State 0,1: Disable OBJ synchronization"""
    SetObjSync(z96, 0)
    """State 2: [Reproduction] Golem door_SubState"""
    call = event_m20_21_x94(z96=z96, z97=z97, z98=z98, z99=z99)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Condition] Golem door_SubState"""
        assert event_m20_21_x95(z97=z97)
        """State 4: [Execution] Golem door_SubState"""
        assert event_m20_21_x96(z96=z96, z99=z99)
    """State 5: End state"""
    return 0

def event_m20_21_x98(z27=20210406, z28=900000, z29=221000021):
    """[Preset] King's door
    z27: Instance ID of king's door OBJ
    z28: Point ID for changing navigation
    z29: Opening flag
    """
    """State 0,1: [Reproduction] King's door_SubState"""
    call = event_m20_21_x99(z27=z27, z28=z28)
    if call.Get() == 1:
        """State 4: [Condition] King's door_SubState"""
        call = event_m20_21_x102(z27=z27, z29=z29)
        if call.Get() == 1:
            """State 3: [Execution] King's Door_Open_SubState"""
            assert event_m20_21_x101(z27=z27, z28=z28, z29=z29)
        elif call.Get() == 0:
            """State 2: [Execution] King's door_Do not open_SubState"""
            assert event_m20_21_x100(z27=z27)
            """State 7: Rerun"""
            return 0
    elif call.Get() == 0:
        pass
    elif call.Get() == 2:
        """State 6: [Condition] King's door_Guest_SubState"""
        assert event_m20_21_x181(z27=z27)
        """State 5: [Execution] King's Door_Guest_SubState"""
        assert event_m20_21_x182(z28=z28)
    """State 8: Finish"""
    return 1

def event_m20_21_x99(z27=20210406, z28=900000):
    """[Reproduction] King's door
    z27: Instance ID of king's door OBJ
    z28: Point ID for changing navigation
    """
    """State 0,1: Determining the state of the king's door"""
    if CompareObjStateId(z27, 30, 0):
        pass
    elif CompareObjStateId(z27, 70, 0):
        """State 2: Waiting for the door to open"""
        assert CompareObjStateId(z27, 30, 0)
    else:
        """State 4: Host?"""
        if IsGuest() != 1:
            """State 6: host"""
            return 1
        else:
            """State 7: The guests"""
            return 2
    """State 3: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z28, 2)
    """State 5: Finish"""
    return 0

def event_m20_21_x100(z27=20210406):
    """[Execution] King's door_Do not open
    z27: Instance ID of king's door OBJ
    """
    """State 0,1: Event message display"""
    # action:2000:"Produce the symbol of the King"
    DisplayEventMessage(2000, 0, 0, 0)
    """State 2: Equipped with an or ring away from the king's door?"""
    CompareObjPlayerDistance(0, z27, 10, 3)
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x101(z27=20210406, z28=900000, z29=221000021):
    """[Execution] King's door_Open
    z27: Instance ID of king's door OBJ
    z28: Point ID for changing navigation
    z29: Opening flag
    """
    """State 0,1: Opening flag ON King's door opens"""
    SetEventFlag(z29, 1)
    ChangeObjState(z27, 70)
    """State 2: Waiting for the door to open"""
    CompareObjState(0, z27, 30, 0)
    assert ConditionGroup(0)
    """State 3: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z28, 2)
    """State 4: End state"""
    return 0

def event_m20_21_x102(z27=20210406, z29=221000021):
    """[Condition] King's door
    z27: Instance ID of king's door OBJ
    z29: Opening flag
    """
    """State 0,2: Did you approach the king's door?"""
    CompareObjPlayerDistance(0, z27, 3, 5)
    assert ConditionGroup(0)
    """State 1: Is it equipped with a king's ring? Has it been opened?"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    SetConditionGroup(0, 8)
    # goods:40510000:King's Ring
    DoesPlayerHaveItem(8, 40510000, 1, 3, 1, 1, 0)
    CompareEventFlag(8, z29, 1)
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

def event_m20_21_x104(z94=_, z95=4):
    """[Condition] Statue of a dragon that spits acid
    z94: Statue instance ID
    z95: Reaction sound level
    """
    """State 0,1: Did you hear a sound nearby?"""
    CheckObjHeardSound(0, z94, z95, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x105(z94=_, mode3=1):
    """[Execution] Statue of dragon spitting acid
    z94: Statue instance ID
    mode3: Cool time
    """
    """State 0,1: OBJ state transition request: Statue: 70"""
    ChangeObjState(z94, 70)
    """State 3: Waiting for the end of firing"""
    assert CompareObjStateId(z94, 10, 0)
    """State 2: Cool time"""
    assert (GetStateTime() > mode3) != 0
    """State 4: End state"""
    return 0

def event_m20_21_x106(z94=_, z95=4, mode3=1):
    """[Preset] Acid spitting dragon statue
    z94: Statue instance ID
    z95: Reaction sound level
    mode3: Cool time
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z94, 0)
    """State 2: [Reproduction] Statue of dragon spitting acid_Sky_SubState"""
    assert event_m20_21_x103()
    """State 3: [Condition] Dragon _SubState that spits acid"""
    assert event_m20_21_x104(z94=z94, z95=z95)
    """State 4: [Execution] Statue of dragon spitting acid _SubState"""
    assert event_m20_21_x105(z94=z94, mode3=mode3)
    """State 5: End state"""
    return 0

def event_m20_21_x107(z47=_, z93=30, z49=_, z50=7.5):
    """[Reproduction] Golem_Main Gate
    z47: Golem instance ID
    z93: State ID to be initialized
    z49: Flag that determines if the golem has absorbed soul
    z50: The distance a golem absorbs soul
    """
    """State 0,1: Golem already activated?"""
    if CompareObjStateId(z47, 20, 0):
        """State 5: Activated"""
        return 1
    elif CompareObjStateId(z47, 72, 0):
        """State 6: Seoul absorbed"""
        Label('L0')
        return 2
    elif CompareObjStateId(z47, 70, 0):
        Goto('L0')
    else:
        """State 2: Golem OBJ state initialization"""
        ChangeObjState(z47, z93)
        assert CompareObjStateId(z47, z93, 0)
        """State 3: Absorption processing in Seoul"""
        AddSoulAcquisitionTarget(z47, z50, z49, 1, -1)
        """State 4: Not started"""
        return 0

def event_m20_21_x108(z47=_, z48=_):
    """[Execution] Golem_Main Gate
    z47: Golem instance ID
    z48: Lever instance ID
    """
    """State 0,3: OBJ state transition: Golem operation"""
    ChangeObjState(z47, 70)
    """State 4: Has Golem's Soul Absorption Anime finished?"""
    CompareObjState(0, z47, 72, 0)
    assert ConditionGroup(0)
    """State 1: OBJ state transition: lever operation"""
    ChangeObjState(z48, 70)
    """State 2: Lever OBJ transition standby"""
    CompareObjState(0, z48, 20, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m20_21_x109(z47=_, z48=_, z49=_, z50=7.5):
    """[Preset] Golem_Main Gate
    z47: Golem instance ID
    z48: Lever instance ID
    z49: Flag that determines if the golem has absorbed soul
    z50: The distance a golem absorbs soul
    """
    """State 0,1: Disable OBJ synchronization"""
    SetObjSync(z47, 0)
    SetObjSync(z48, 0)
    """State 2: [Reproduction] Golem_Main Gate_SubState"""
    call = event_m20_21_x107(z47=z47, z93=30, z49=z49, z50=z50)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 5: [Execution] Golem_Main Gate_Seoul Absorbed_SubState"""
        assert event_m20_21_x169(z47=z47, z48=z48)
    elif call.Done():
        """State 4: [Condition] Golem_Main Gate_SubState"""
        assert event_m20_21_x168(z49=z49)
        """State 3: [Execution] Golem_Main Gate_SubState"""
        assert event_m20_21_x108(z47=z47, z48=z48)
    """State 6: End state"""
    return 0

def event_m20_21_x110(z90=20211530, z91=20211540, z87=20212520, z92=7.5, flag15=221000010, flag16=221000032):
    """[Reproduction] Golem for elevator
    z90: Elevator lower lever_OBJ instance ID
    z91: Elevator upper lever_OBJ instance ID
    z87: Golem instance ID
    z92: The distance a golem absorbs soul
    flag15: Elevator start flag
    flag16: Flag that determines if the golem has absorbed soul
    """
    """State 0,2: Invalid lever for elevator"""
    DisableObjKeyGuide(z90, 1)
    DisableObjKeyGuide(z91, 1)
    """State 1: Is the elevator started?"""
    if GetEventFlag(flag15) != 0:
        """State 7: [Rescue] Is the golem in the initial state? _2"""
        if CompareObjStateId(z87, 10, 0):
            pass
        else:
            """State 9: Activated"""
            return 1
    else:
        """State 5: Has Golem absorbed Seoul?"""
        if GetEventFlag(flag16) != 0:
            """State 6: [Rescue] Is the golem in the initial state?"""
            if CompareObjStateId(z87, 10, 0):
                pass
            else:
                """State 10: Seoul absorbed"""
                return 2
        else:
            pass
    """State 3: Golem OBJ state initialization"""
    ChangeObjState(z87, 30)
    assert CompareObjStateId(z87, 30, 0)
    """State 4: Absorption processing in Seoul"""
    AddSoulAcquisitionTarget(z87, z92, flag16, 1, -1)
    """State 8: End state"""
    return 0

def event_m20_21_x111(z87=20212520, flag16=221000032):
    """[Condition] Elevator golem activation
    z87: Golem instance ID
    flag16: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, flag16, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x112(z87=20212520, z88=20212620, z89=20213110, z90=20211530, z91=20211540, flag15=221000010):
    """[Execution] Golem for elevator
    z87: Golem OBJ instance ID
    z88: OBJ instance ID of the lever
    z89: OBJ instance ID of the elevator
    z90: Elevator bottom_lever OBJ instance ID
    z91: Elevator top_lever OBJ instance ID
    flag15: Elevator start flag
    """
    """State 0,5: Golem state determination"""
    if CompareObjStateId(z87, 30, 0):
        """State 6: OBJ state transition: Golem operation"""
        ChangeObjState(z87, 70)
        assert CompareObjStateId(z87, 30, 1)
    else:
        pass
    """State 7: Has Golem's Soul Absorption Anime finished?"""
    CompareObjState(0, z87, 70, 1)
    assert ConditionGroup(0)
    """State 12: Judgment of lever status"""
    if CompareObjStateId(z88, 20, 1):
        """State 13: Lever initialization"""
        InitializeObj(z88)
        assert (GetStateTime() >= 0) != 0
        """State 8: OBJ state transition: lever operation"""
        ChangeObjState(z88, 70)
    else:
        pass
    """State 2: Golem lever OBJ transition waiting"""
    CompareObjState(0, z88, 20, 0)
    assert ConditionGroup(0)
    """State 11: Elevator state judgment"""
    if CompareObjStateId(z89, 40, 0):
        """State 3: Move the elevator down"""
        ChangeObjState(z89, 80)
    else:
        pass
    """State 9: Elevator OBJ transition standby"""
    CompareObjState(0, z89, 41, 0)
    assert ConditionGroup(0)
    """State 10: Return the elevator switch"""
    ChangeObjState(z89, 81)
    """State 4: Elevator lever activation"""
    DisableObjKeyGuide(z91, 0)
    """State 1: Flag ON"""
    SetEventFlag(flag15, 1)
    """State 14: End state"""
    return 0

def event_m20_21_x113(z87=20212520, z88=20212620, z89=20213110, z90=20211530, z91=20211540, z92=7.5,
                      flag15=221000010, flag16=221000032):
    """[Preset] Golem for elevator
    z87: Golem OBJ instance ID
    z88: OBJ instance ID of the lever
    z89: OBJ instance ID of the elevator
    z90: Elevator lower lever_OBJ instance ID
    z91: Elevator upper lever_OBJ instance ID
    z92: The distance a golem absorbs soul
    flag15: Elevator start flag
    flag16: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: [Reproduction] Elevator Golem Activation_SubState"""
    call = event_m20_21_x110(z90=z90, z91=z91, z87=z87, z92=z92, flag15=flag15, flag16=flag16)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        """State 3: [Execution] Golem activation for elevators_SubState"""
        Label('L0')
        assert event_m20_21_x112(z87=z87, z88=z88, z89=z89, z90=z90, z91=z91, flag15=flag15)
    elif call.Done():
        """State 2: [Condition] Elevator golem activation_SubState"""
        assert event_m20_21_x111(z87=z87, flag16=flag16)
        Goto('L0')
    """State 4: End state"""
    return 0

def event_m20_21_x114(z43=20212000, z44=20211520, z45=20210410, z46=300000):
    """[Reproduction] Lever door between soldiers
    z43: Instance ID of the iron lattice OBJ
    z44: Lever OBJ instance ID
    z45: Door OBJ instance ID
    z46: Navimesh change point ID
    """
    """State 0,1: Disable key guide of door OBJ"""
    DisableObjKeyGuide(z45, 1)
    """State 2: Judgment of lever OBJ status"""
    if CompareObjStateId(z44, 20, 0):
        pass
    else:
        Goto('L0')
    """State 3: State determination of iron lattice OBJ"""
    if CompareObjStateId(z43, 20, 0):
        """State 4: Enable key guide for door OBJ"""
        DisableObjKeyGuide(z45, 0)
        """State 5: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z46, 2)
        """State 7: Activated"""
        return 1
    else:
        """State 8: Only lever is activated"""
        return 2
    """State 6: Not started"""
    Label('L0')
    return 0

def event_m20_21_x115(z44=20211520):
    """[Condition] Lever door between soldiers
    z44: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z44, 72, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x116(z43=20212000, z45=20210410, z46=300000):
    """[Execution] Lever door between soldiers
    z43: Instance ID of the iron lattice OBJ
    z45: Door OBJ instance ID
    z46: Navimesh change point ID
    """
    """State 0,1: Animation reproduction of iron lattice OBJ"""
    ChangeObjState(z43, 70)
    """State 3: Has the iron bar opened?"""
    CompareObjState(0, z43, 20, 0)
    assert ConditionGroup(0)
    """State 4: Enable key guide for door OBJ"""
    DisableObjKeyGuide(z45, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z46, 2)
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

def event_m20_21_x122(flag2=100972, flag3=221000091):
    """[Reproduction] Boss Battle Start_Queen Knight
    flag2: Global flag for determining the destruction of giants
    flag3: Other flags for queen knight AC destruction determination
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
        GetEventFlag(flag2) != 0 and GetEventFlag(flag3) != 0):
        pass
    else:
        Goto('L2')
    """State 10: To the second battle of Andyel"""
    return 4
    """State 1: Queen single battle?"""
    Label('L2')
    if GetEventFlag(flag2) != 0 and GetEventFlag(flag3) != 0:
        pass
    else:
        Goto('L3')
    """State 6: To Queen A"""
    return 0
    """State 2: Destroyed Knight AC?"""
    Label('L3')
    if GetEventFlag(flag3) != 0:
        """State 7: Simple end"""
        return 1
    else:
        """State 8: End state"""
        return 2

def event_m20_21_x123(z5=1100000, z6=1100000, z7=102, z8=1021020, z9=221020090, flag2=100972, flag3=221000091,
                      z10=1021021):
    """[Preset] Boss Battle: Queen Knight
    z5: Start point ID
    z6: End point ID
    z7: Sound ID
    z8: Boss Battle ID
    z9: Other flags for logic
    flag2: Global flag for determining the destruction of giants
    flag3: Other flags for queen knight AC destruction determination
    z10: Boss Battle ID (for consecutive battles)
    """
    """State 0,1: [Reproduction] Boss Battle Start_Queen's Knight_SubState"""
    call = event_m20_21_x122(flag2=flag2, flag3=flag3)
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
    call = event_m20_21_x149(z5=z5, z6=z6, flag2=flag2)
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
        assert event_m20_21_x14(z81=z7, z82=z8, z83=z9)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 4: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z16=z8)
        """State 12: [Execution] Boss Battle_End_Queen Knight_SubState"""
        assert event_m20_21_x202(z7=z7, z8=z8, z9=z9, mode1=0)
    elif call.Get() == 1:
        """State 5: [Execution] Boss Battle_Start (Consecutive Battle) _SubState"""
        assert event_m20_21_x14(z81=z7, z82=z10, z83=z9)
        """State 6: [Reproduction] Boss Battle_Sky (Sequential Battle) _SubState"""
        assert event_m20_21_x15()
        """State 7: [Condition] Boss Battle_End Judgment (Consecutive Battle) _SubState"""
        assert event_m20_21_x16(z16=z10)
        """State 13: [Execution] Boss Battle_End_Queen's Knight (Continuous Battle) _SubState"""
        assert event_m20_21_x202(z7=z7, z8=z10, z9=z9, mode1=0)
        Goto('L5')
    elif call.Get() == 2:
        """State 9: [Execution] Boss Battle_Start (Consecutive Battle) _2_SubState"""
        assert event_m20_21_x14(z81=z7, z82=z10, z83=z9)
        """State 10: [Reproduction] Boss Battle_Sky (Sequence) _2_SubState"""
        assert event_m20_21_x15()
        """State 11: [Condition] Boss Battle_End Judgment (Consecutive Battle) _2_SubState"""
        assert event_m20_21_x16(z16=z10)
        """State 14: [Execution] Boss Battle_End_Queen Knight (Consecutive Battle) _2_SubState"""
        assert event_m20_21_x202(z7=z7, z8=z10, z9=z9, mode1=0)
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

def event_m20_21_x125(z85=202120, flag14=221000098, z86=1201001):
    """[Preset] Poly Play_Queen Battle B
    z85: Poly play ID
    flag14: Poly drama played flag
    z86: Warp point ID
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m20_21_x32(flag14=flag14)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Poly Play_Queen Battle B_SubState"""
        call = event_m20_21_x124()
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 2: [Execution] Boss Battle_Poly Play_SubState"""
            assert event_m20_21_x34(z85=z85, flag14=flag14, z86=z86, z197=1)
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
        assert event_m20_21_x35(z193=20210607, z194=202110, flag22=221000097, z195=1201000, z196=1)
    else:
        """State 3: [Preset] Poly Play_Queen Battle B_SubState"""
        assert event_m20_21_x125(z85=202120, flag14=221000098, z86=1201001)
    """State 4: End state"""
    return 0

def event_m20_21_x127(z84=_, z79=_, z80=_):
    """[Condition] Boss Battle_Start: Queen
    z84: Poly drama played flag
    z79: Start point ID
    z80: End point ID
    """
    """State 0,1: Did you enter the point after the poly play? Has the queen been destroyed?"""
    CompareEventFlag(8, z84, 1)
    IsPlayerInsidePoint(8, z79, z80, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    CompareEventFlag(9, z84, 1)
    IsPlayerInsidePoint(9, z79, z80, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(1, 221000096, 1)
    if ConditionGroup(1):
        """State 3: Guest: Defeat the Queen"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m20_21_x128(z79=_, z80=_, z81=101, z82=_, z83=221020095, flag13=221000096, z84=_):
    """[Preset] Boss Battle: Queen
    z79: Start point ID
    z80: End point ID
    z81: Sound ID
    z82: Boss Battle ID
    z83: Other flags for logic
    flag13: Boss destruction flag
    z84: Poly drama played flag
    """
    """State 0,5: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(flag5=flag13)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 6: [Condition] Boss Battle_Start: Queen_SubState"""
        call = event_m20_21_x127(z84=z84, z79=z79, z80=z80)
        if call.Get() == 1:
            pass
        elif call.Done():
            """State 2: [Execution] Boss Battle_Start_SubState"""
            assert event_m20_21_x14(z81=z81, z82=z82, z83=z83)
            """State 1: [Reproduction] Boss Battle_Sky_SubState"""
            assert event_m20_21_x15()
            """State 4: [Condition] Boss Battle_End Judgment_SubState"""
            assert event_m20_21_x16(z16=z82)
            """State 3: [Execution] Boss Battle_End_SubState"""
            assert event_m20_21_x17(z15=z81, z16=z82, z17=z83, mode5=0)
    """State 7: End state"""
    return 0

def event_m20_21_x129(flag12=221000091):
    """[Reproduction] Queen Knight AC_ Defeat Determination
    flag12: Queen Knight AC Defeat Flag
    """
    """State 0,1: Are the queens A and C defeated?"""
    if GetEventFlag(flag12) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_21_x130(z77=860, z78=862):
    """[Condition] Queen Knight AC_ Defeat Determination
    z77: Knight A generator ID
    z78: Knight C generator ID
    """
    """State 0,1: Are A and C pseudo-dead?"""
    CompareChrHpValue(8, z77, 1, 5)
    CompareChrHpValue(8, z78, 1, 5)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_21_x131(z73=860, z74=862, z75=93320030, z76=93340030):
    """[Execution] Queen Knight AC_ Defeat Determination
    z73: Knight A generator ID
    z74: Knight C generator ID
    z75: A's immortal release special effect ID
    z76: C immortal release special effect ID
    """
    """State 0,1: Canceled and killed immortality of A and C"""
    SetEnemySpEffect(z73, z75, 19, 4)
    SetEnemySpEffect(z74, z76, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_21_x132(z73=860, z74=862, z75=93320030, z76=93340030, flag12=221000091):
    """[Preset] Queen Knight AC_Destroy
    z73: Knight A generator ID
    z74: Knight C generator ID
    z75: A's immortal release special effect ID
    z76: C immortal release special effect ID
    flag12: Queen Knight AC Defeat Flag
    """
    """State 0,1: [Reproduction] Queen Knight AC_Destroy_SubState"""
    call = event_m20_21_x129(flag12=flag12)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Queen Knight AC_Destroy_SubState"""
        assert event_m20_21_x130(z77=860, z78=862)
        """State 2: [Execution] Queen Knight AC_Destroy_SubState"""
        assert event_m20_21_x131(z73=z73, z74=z74, z75=z75, z76=z76)
    """State 4: End state"""
    return 0

def event_m20_21_x133(flag11=221000094):
    """[Reproduction] End roll
    flag11: End roll execution judgment flag
    """
    """State 0,3: Event light ON"""
    SetPointLightEnabled(20210010, 1, 0)
    """State 1: End roll execution judgment"""
    if GetEventFlag(flag11) != 0:
        """State 5: Executed"""
        return 1
    else:
        """State 2: End OBJ key guide valid"""
        DisableObjKeyGuide(20211800, 0)
        DisableObjKeyGuide(20211810, 0)
        """State 4: Not executed"""
        return 0

def event_m20_21_x134(z69=1600000):
    """[Condition] End roll
    z69: Point ID
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

def event_m20_21_x135(flag11=221000094, z71=_, val1=1600010, z70=221020002, z72=_):
    """[Execution] End role
    flag11: End roll execution judgment flag
    z71: Poly play ID
    val1: Destination point ID after poly play
    z70: Staff roll branch flag
    z72: ON / OFF
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
    SetEventFlag(z70, z72)
    CompareEventFlag(0, z70, z72)
    assert ConditionGroup(0)
    """State 10: [Lib] Normal poly play_SubState"""
    assert event_m20_21_x0(z71=z71, val1=val1, flag25=0, z235=0, z236=1)
    """State 1: End roll"""
    RollCredits()
    """State 2,7: In-game menu and PC operation enable, PC invincibility release"""
    ProhibitInGameMenu(0)
    ProhibitPlayerOperation(0)
    SetPlayerInvincible(0)
    """State 11: End state"""
    return 0

def event_m20_21_x136(z69=1600000, flag11=221000094, z70=221020002):
    """[Preset] End roll
    z69: Point ID
    flag11: End roll execution judgment flag
    z70: Staff roll branch flag
    """
    """State 0,1: [Reproduction] End role_SubState"""
    call = event_m20_21_x133(flag11=flag11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] End role_SubState"""
        call = event_m20_21_x134(z69=z69)
        if call.Get() == 0:
            """State 3: [Execution] End roll_Conventional version_SubState"""
            assert event_m20_21_x135(flag11=flag11, z71=202130, val1=1600010, z70=z70, z72=0)
        elif call.Get() == 1:
            """State 4: [Execution] End role_BEST version_SubState"""
            assert event_m20_21_x135(flag11=flag11, z71=202150, val1=1600010, z70=z70, z72=1)
    """State 5: End state"""
    return 0

def event_m20_21_x137(flag10=221000093):
    """[Reproduction] Retry point setting after queen defeat
    flag10: Retry point setting completion flag
    """
    """State 0,1: Retry point setting completion flag judgment"""
    if GetEventFlag(flag10) != 0:
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

def event_m20_21_x139(flag10=221000093):
    """[Execution] Retry point setting after queen defeat
    flag10: Retry point setting completion flag
    """
    """State 0,1: Retry point setting"""
    SetRespawnPoint(1700000)
    """State 2: Retry point setting completion flag ON"""
    SetEventFlag(flag10, 1)
    """State 3: End state"""
    return 0

def event_m20_21_x140(flag10=221000093):
    """[Preset] Retry point setting after defeating the Queen
    flag10: Retry point setting completion flag
    """
    """State 0,1: [Reproduction] Retry point setting after defeating the Queen_SubState"""
    call = event_m20_21_x137(flag10=flag10)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Retry point setting after defeating the Queen_SubState"""
        assert event_m20_21_x138()
        """State 3: [Execution] Retry point setting after defeating the queen_SubState"""
        assert event_m20_21_x139(flag10=flag10)
    """State 4: End state"""
    return 0

def event_m20_21_x141(z65=_, z66=_, z67=_, z68=6.7):
    """[Preset] Golem that moves by sucking soul (lights on)
    z65: Golem OBJ instance ID
    z66: Torch OBJ instance ID
    z67: Flag that determines if Golem OBJ has absorbed soul
    z68: Distance that Golem OBJ absorbs Seoul
    """
    """State 0,1: [Reproduction] Golem that moves by sucking soul (lights on) _SubState"""
    call = event_m20_21_x142(z65=z65, z66=z66, z67=z67, z68=z68)
    if call.Get() == 0:
        """State 2: [Conditions] Golem that moves by sucking soul (lights on) _SubState"""
        assert event_m20_21_x143(z67=z67)
        """State 3: [Execution] Golem that moves by sucking soul (lights on) _SubState"""
        assert event_m20_21_x144(z65=z65, z66=z66)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_21_x142(z65=_, z66=_, z67=_, z68=6.7):
    """[Reproduction] Golem that moves by sucking soul (lights on)
    z65: Golem OBJ instance ID
    z66: Torch OBJ instance ID
    z67: Flag that determines if Golem OBJ has absorbed soul
    z68: Distance that Golem OBJ absorbs Seoul
    """
    """State 0,1: Attach torches to golem"""
    AttachObjToObj(z65, 150, z66)
    """State 2: Golem already activated?"""
    if CompareObjStateId(z65, 22, 0):
        """State 5: Safety: lighting torches"""
        ChangeObjState(z66, 20)
        """State 7: Activated"""
        return 1
    else:
        """State 3: Golem OBJ state initialization"""
        ChangeObjState(z65, 40)
        assert CompareObjStateId(z65, 40, 0)
        """State 4: Absorption processing in Seoul"""
        AddSoulAcquisitionTarget(z65, z68, z67, 1, -1)
        """State 6: Not started"""
        return 0

def event_m20_21_x143(z67=_):
    """[Conditions] Golem that moves by sucking soul (lights on)
    z67: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z67, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x144(z65=_, z66=_):
    """[Execution] Golem that moves by sucking soul (lights up)
    z65: Golem OBJ instance ID
    z66: Torch OBJ instance ID
    """
    """State 0,2: Bring a torch to the golem"""
    ChangeObjState(z65, 80)
    assert CompareObjStateId(z65, 22, 0)
    """State 1: Light a torch"""
    ChangeObjState(z66, 20)
    """State 3: End state"""
    return 0

def event_m20_21_x145(z63=_, z64=_):
    """[Reproduction] Drop of Statue Night
    z63: Generator ID
    z64: Impala ID of the neck
    """
    """State 0,1: Is your neck already broken?"""
    if IsBodyPartDestroyed(z63, 1) != 0:
        """State 2: Cut: Do nothing"""
        pass
    else:
        """State 3: Not cut: Initialization"""
        InitializeObj(z64)
    """State 4: Host termination"""
    return 0

def event_m20_21_x146():
    """[Condition] The fall of statue night_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x147(z63=_, z64=_):
    """[Execution] The fall of Statue Knight
    z63: Generator ID
    z64: Neck instance ID
    """
    """State 0,1: Link OBJ to the generator"""
    GenerateObjFromCharacter(z63, z64, 7)
    """State 2: End state"""
    return 0

def event_m20_21_x148(z63=_, z64=_):
    """[Preset] Drop of Statue Night
    z63: Generator ID
    z64: Neck instance ID
    """
    """State 0,1: [Reproduction] Drop of Statue Night_SubState"""
    assert event_m20_21_x145(z63=z63, z64=z64) == 0
    """State 3: [Condition] The fall of the statue night_Sky_SubState"""
    assert event_m20_21_x146()
    """State 2: [Execution] Drop of Statue Knight_SubState"""
    assert event_m20_21_x147(z63=z63, z64=z64)
    """State 4: End state"""
    return 0

def event_m20_21_x149(z5=1100000, z6=1100000, flag2=100972):
    """[Condition] Boss Battle Start_Queen Knight
    z5: Start point ID
    z6: End point ID
    flag2: Global flag for determining the destruction of giants
    """
    """State 0,1: Did you enter the boss room point? Has the AC been defeated?"""
    IsPlayerInsidePoint(8, z5, z6, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z5, z6, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(1, 221000091, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4: Guest: Destroyed Giant King?"""
    CompareEventFlag(0, flag2, 0)
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
    CompareEventFlag(0, flag2, 0)
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

def event_m20_21_x150(z62=20211700):
    """[Preset] Key person
    z62: Key person OBJ instance ID
    """
    """State 0,1: [Reproduction] Key person_SubState"""
    call = event_m20_21_x151(z62=z62)
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
    call = event_m20_21_x156(z62=z62)
    if call.Get() == 0:
        """State 3: [Execution] Key person_Host_Unlockable_SubState"""
        call = event_m20_21_x153(z62=z62)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: Unlocked"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Key person_Host_Unlockable_SubState"""
        assert event_m20_21_x154(z62=z62)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Key person_Guest_SubState"""
    Label('L1')
    assert event_m20_21_x155(z62=z62)
    """State 2: [Execution] Key person_Guest_Empty_SubState"""
    assert event_m20_21_x152()
    """State 9: Guest termination"""
    return 2

def event_m20_21_x151(z62=20211700):
    """[Reproduction] Key person
    z62: Key person OBJ instance ID
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
    elif (CompareObjStateId(z62, 20, 0) and CompareObjStateId(z62, 74, 0) and CompareObjStateId(z62,
          76, 0) and CompareObjStateId(z62, 70, 0) and CompareObjStateId(z62, 78, 0)):
        """State 5: After execution"""
        return 2

def event_m20_21_x152():
    """[Execution] Key person_Guest_Empty"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x153(z62=20211700):
    """[Execution] Key person_Host_Unlockable
    z62: Key person OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:1980000:Key to the Embedded
    DisplayYesNoMenu(1002, 1.8, z62, 190, 2, 1980000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 9: Key person transition waiting: 30"""
        ChangeObjState(z62, 30)
        assert CompareObjStateId(z62, 30, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z62, 38, 11)
        assert PlayerIsInEventAction(11) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 11, 0)
        # goods:1980000:Key to the Embedded
        DoesPlayerHaveItem(0, 1980000, 0, 5, 1, 1, 0)
        CompareObjState(1, z62, 74, 0)
        CompareObjState(1, z62, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Key person sword consumption"""
            # goods:1980000:Key to the Embedded
            ConsumeItem(1980000, 1)
            assert CompareObjStateId(z62, 20, 0)
            """State 11: Unlocked"""
            return 0
    else:
        """State 8: Key person: Waiting for transition: 30"""
        ChangeObjState(z62, 30)
        assert CompareObjStateId(z62, 30, 0)
        """State 6: Key person: Unsuccessful unlocking: 80"""
        ChangeObjState(z62, 80)
        assert CompareObjStateId(z62, 80, 0)
        """State 7: Key person: Initial state standby"""
        CompareObjState(0, z62, 10, 0)
        CompareObjState(0, z62, 10, 0)
        assert ConditionGroup(0)
    """State 10: Key person: Initial state: 10"""
    ChangeObjState(z62, 10)
    """State 12: Rerun"""
    return 1

def event_m20_21_x154(z62=20211700):
    """[Execution] Key person_Host_Unlockable
    z62: Key person OBJ instance ID
    """
    """State 0,4: Key person: Waiting for transition: 30"""
    ChangeObjState(z62, 30)
    assert CompareObjStateId(z62, 30, 0)
    """State 1: Key person: Unsuccessful unlocking: 80"""
    ChangeObjState(z62, 80)
    assert CompareObjStateId(z62, 80, 0)
    """State 3: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:1980000:Key to the Embedded
    DisplayOkMenu(1013, 0, 0, z62, 190, 2, 1980000, 0)
    assert OkMenuDisplay() != 1
    """State 2: Key person: Initial state standby"""
    CompareObjState(0, z62, 10, 0)
    assert ConditionGroup(0)
    """State 5: Unsuccessful unlocking_rerun"""
    return 0

def event_m20_21_x155(z62=20211700):
    """[Condition] Key person_Guest
    z62: Key person OBJ instance ID
    """
    """State 0,1: Wait for key person to finish"""
    CompareObjState(0, z62, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x156(z62=20211700):
    """[Condition] Key person_host
    z62: Key person OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z62)
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

def event_m20_21_x157(z56=20210407):
    """[Reproduction] Main gate of Golem
    z56: Door instance ID
    """
    """State 0,1: Is the gate already open or on the way to open?"""
    if CompareObjStateId(z56, 20, 0):
        """State 2: Navigation mesh change"""
        Label('L0')
        DeleteNavimeshAttribute(610000, 2)
        """State 4: End of reproduction"""
        return 1
    elif CompareObjStateId(z56, 70, 0):
        Goto('L0')
    else:
        """State 3: End state"""
        return 0

def event_m20_21_x158(z57=20212600, z58=20212605, z60=20212500, z61=20212505):
    """[Condition] Main gate of Golem
    z57: Right lever instance ID
    z58: Instance ID of the left lever
    z60: Right golem instance ID
    z61: Left golem instance ID
    """
    """State 0,1: Standby for left and right golems"""
    CompareObjState(8, z60, 20, 0)
    CompareObjState(8, z61, 20, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_21_x159(z56=20210407, z59=221000041):
    """[Execution] The main gate of the Golem
    z56: Door instance ID Instance ID
    z59: Main gate liberation flag
    """
    """State 0,1: OBJ state transition: door"""
    ChangeObjState(z56, 70)
    """State 4: Main gate release flag ON"""
    SetEventFlag(z59, 1)
    """State 3: Has the door opened?"""
    CompareObjState(0, z56, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(610000, 2)
    """State 5: End state"""
    return 0

def event_m20_21_x160(z56=20210407, z57=20212600, z58=20212605, z59=221000041, z60=20212500, z61=20212505):
    """[Preset] Golem front gate
    z56: Door instance ID
    z57: Right lever instance ID
    z58: Instance ID of the left lever
    z59: Main gate liberation flag
    z60: Right golem instance ID
    z61: Left golem instance ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z56, 0)
    """State 2: [Reproduction] Golem Main Gate_SubState"""
    call = event_m20_21_x157(z56=z56)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [Condition] Golem Main Gate_SubState"""
        assert event_m20_21_x158(z57=z57, z58=z58, z60=z60, z61=z61)
        """State 4: [Execution] Golem Main Gate_SubState"""
        assert event_m20_21_x159(z56=z56, z59=z59)
    """State 5: End state"""
    return 0

def event_m20_21_x161(flag9=221000086):
    """[Reproduction] Mirror Night Battle_Start
    flag9: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag9) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_21_x162(z51=800000, z52=800000):
    """[Condition] Mirror Night Battle_Start
    z51: Start point ID
    z52: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z51, z52, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z51, z52, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Is it in game?"""
    assert InGame() != 0
    """State 3: End state"""
    return 0

def event_m20_21_x163(z53=201, z54=1021010, z55=221020085):
    """[Execution] Mirror Night Battle_Start
    z53: Sound ID
    z54: Boss Battle ID
    z55: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z53)
    """State 1: Boss battle start notification"""
    StartBossFight(z54)
    """State 4: Drawing mode switching: Mirror night mode"""
    SetSpecialDrawingMode(1)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z55, 1)
    """State 5: End state"""
    return 0

def event_m20_21_x164():
    """[Reproduction] Mirror Night Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_21_x165(z54=1021010):
    """[Condition] Mirror Knight Battle_End Judgment
    z54: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z54, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x166(z53=201, z54=1021010, z55=221020085, mode2=0):
    """[Execution] Mirror Night Battle_End
    z53: Sound ID
    z54: Boss Battle ID
    z55: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z55, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z54)
    """State 4: Drawing mode switching: Standard"""
    SetSpecialDrawingMode(0)
    """State 5: My death under Mirror Knight"""
    EnemyActionRequest(5000, 1)
    EnemyActionRequest(5001, 1)
    """State 6: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z53)
    """State 7: End state"""
    return 0

def event_m20_21_x167(flag9=221000086, z51=800000, z52=800000, z53=201, z54=1021010, z55=221020085, mode2=0):
    """[Preset] Mirror Night Battle starts
    flag9: Boss destruction flag
    z51: Start point ID
    z52: End point ID
    z53: Sound ID
    z54: Boss Battle ID
    z55: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Mirror Night Battle_Start_SubState"""
    call = event_m20_21_x161(flag9=flag9)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Mirror Knight Battle_Start_SubState"""
        assert event_m20_21_x162(z51=z51, z52=z52)
        """State 3: [Execution] Mirror Knight Battle_Start_SubState"""
        assert event_m20_21_x163(z53=z53, z54=z54, z55=z55)
        """State 2: [Reproduction] Mirror Knight Battle_Sky_SubState"""
        assert event_m20_21_x164()
        """State 6: [Condition] Mirror Knight Battle_End Judgment_SubState"""
        assert event_m20_21_x165(z54=z54)
        """State 4: [Execution] Mirror Knight Battle_End_SubState"""
        assert event_m20_21_x166(z53=z53, z54=z54, z55=z55, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m20_21_x168(z49=_):
    """[Condition] Golem_Main Gate
    z49: Flag that determines if the golem has absorbed soul
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z49, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x169(z47=_, z48=_):
    """[Execution] Golem_Main Gate_Soul Absorbed
    z47: Golem instance ID
    z48: Lever instance ID
    """
    """State 0,3: Has Golem's Soul Absorption Anime finished?"""
    CompareObjState(0, z47, 72, 0)
    assert ConditionGroup(0)
    """State 1: OBJ state transition: lever operation"""
    ChangeObjState(z48, 70)
    """State 2: Lever OBJ transition standby"""
    CompareObjState(0, z48, 20, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_21_x170(z43=20212000, z44=20211520, z45=20210410, z46=300000):
    """[Preset] Lever door between soldiers
    z43: Instance ID of the iron lattice OBJ
    z44: Lever OBJ instance ID
    z45: Door OBJ instance ID
    z46: Navimesh change point ID
    """
    """State 0,1: [Reproduction] Lever door between soldiers_SubState"""
    call = event_m20_21_x114(z43=z43, z44=z44, z45=z45, z46=z46)
    if call.Get() == 0:
        """State 2: [Condition] Lever door between soldiers_SubState"""
        assert event_m20_21_x115(z44=z44)
        """State 3: [Execution] Lever door between soldiers_SubState"""
        Label('L0')
        assert event_m20_21_x116(z43=z43, z45=z45, z46=z46)
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

def event_m20_21_x172(z42=_):
    """[Condition] Vegrant removal determination
    z42: Generator ID
    """
    """State 0,2: Has a vegrant been generated?"""
    IsChrActive(0, z42, 1)
    assert ConditionGroup(0)
    """State 1: Has Vegrant finished the return action?"""
    CompareChrEzStateValue(0, z42, 7, 1, 0)
    assert ConditionGroup(0)
    """State 3: Returned"""
    return 0

def event_m20_21_x173(z42=_):
    """[Execution] Vegrant removal determination
    z42: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z42, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x174(z42=_):
    """[Preset] Vegrant removal judgment
    z42: Generator ID
    """
    """State 0,1: [Reproduction] Vegrant deletion judgment_empty_SubState"""
    assert event_m20_21_x171()
    """State 3: [Condition] Vegrant deletion determination_SubState"""
    assert event_m20_21_x172(z42=z42)
    """State 2: [Execution] Vegrant deletion determination_SubState"""
    assert event_m20_21_x173(z42=z42)
    """State 4: End state"""
    return 0

def event_m20_21_x175(z38=20210001, z39=20210002, z40=701000, z41=701002):
    """[Preset] Boss: Heavy cavalry: Soldier only 2 battles_Light switching
    z38: Boss Battle Area Treasure Light 1
    z39: Boss Battle Area Treasure Light 2
    z40: Boss battle area light switch point_start
    z41: Boss battle area light switch point _ end
    """
    """State 0,1: [Reproduction] Boss: Heavy cavalry: Soldier only 2 battles_Light switching_SubState"""
    assert event_m20_21_x176(z38=z38, z39=z39)
    """State 2: [Conditions] Boss: Heavy cavalry: Soldier only 2 battles_Light switching_SubState"""
    assert event_m20_21_x177(z40=z40, z41=z41)
    """State 3: [Execution] Boss: Heavy cavalry: Soldier only 2 battles_Light switch_SubState"""
    assert event_m20_21_x178(z38=z38, z39=z39, z40=z40, z41=z41)
    """State 4: End state"""
    return 0

def event_m20_21_x176(z38=20210001, z39=20210002):
    """[Reproduction] Boss: Heavy cavalry: Soldier only 2 battles_light switching
    z38: Boss Battle Area Treasure Light 1
    z39: Boss Battle Area Treasure Light 2
    """
    """State 0,1: Lights off"""
    SetPointLightEnabled(z38, 0, 0)
    SetPointLightEnabled(z39, 0, 0)
    """State 2: End state"""
    return 0

def event_m20_21_x177(z40=701000, z41=701002):
    """[Conditions] Boss: Heavy cavalry: Soldier only 2 battles_light switching
    z40: Boss battle area light switch point_start
    z41: Boss battle area light switch point _ end
    """
    """State 0,1: Did you enter the lighting point?"""
    IsPlayerInsidePoint(0, z40, z41, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x178(z38=20210001, z39=20210002, z40=701000, z41=701002):
    """[Execution] Boss: Heavy cavalry: Soldier only 2 battles_Light switching
    z38: Boss Battle Area Treasure Light 1
    z39: Boss Battle Area Treasure Light 2
    z40: Boss battle area light switch point_start
    z41: Boss battle area light switch point _ end
    """
    """State 0,1: Light on"""
    SetPointLightEnabled(z38, 1, 0)
    SetPointLightEnabled(z39, 1, 0)
    """State 2: Did you get out of the lighting point?"""
    IsPlayerInsidePoint(0, z40, z41, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_21_x179(z34=104160, z35=678, z36=104160, flag8=103660, z37=63):
    """NPC White Phantom Appearance: General Purpose
    z34: White Phantom can appear: Global event flag
    z35: White Phantom: Generator ID
    z36: Death: Global event flag
    flag8: Hostile: Global event flag
    z37: Body: Generator group ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z35)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z36, 1)
        CompareEventFlag(1, flag8, 1)
        CompareEventFlag(2, z34, 0)
        CompareEventFlag(8, 100974, 1)
        CompareEventFlag(8, 100972, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z35)
            if GetEventFlag(221000006) != 0:
                """State 12: Appearance: Hostile: Waiting: After the Queen"""
                Label('L1')
                CompareEventFlag(0, z36, 1)
                if ConditionGroup(0):
                    pass
                elif (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747)
                      != 0 and GetEventFlag(221000001) != 0 and GetEventFlag(221000006) != 1 and GetEventFlag(flag8)
                      != 1):
                    """State 8: Appearance: System: Rerun"""
                    Label('L2')
                    RestartMachine()
                    Quit()
            elif GetEventFlag(221000096) != 0:
                Goto('L1')
            else:
                """State 7: Appearance: Hostile: Standby"""
                CompareEventFlag(0, z36, 1)
                CompareEventFlag(8, flag8, 0)
                CompareEventFlag(8, 100974, 1)
                CompareEventFlag(8, 100972, 1)
                CompareEventFlag(9, flag8, 0)
                CompareEventFlag(9, 100974, 0)
                CompareEventFlag(9, 100972, 0)
                CompareEventFlag(10, flag8, 0)
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
            GenerateNpcPhantom(z35)
            if (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747) !=
                0 and GetEventFlag(221000001) != 0):
                """State 11: Appearance: Phantom sign showing: Waiting: After the queen"""
                CompareEventFlag(0, z36, 1)
                CompareEventFlag(1, flag8, 1)
                HasNpcPhantomSpawned(2, z35, 1)
                if ConditionGroup(0):
                    Goto('L4')
                elif ConditionGroup(1):
                    Goto('L0')
                elif ConditionGroup(2):
                    pass
            else:
                """State 4: Appearance: Phantom sign displayed: Waiting"""
                CompareEventFlag(0, z36, 1)
                CompareEventFlag(1, flag8, 1)
                HasNpcPhantomSpawned(2, z35, 1)
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
            DeleteEnemyByGeneratorGroup(z37, 0)
            HasNpcPhantomSpawned(0, z35, 0)
            assert ConditionGroup(0)
            Goto('L2')
        elif GetEventFlag(221000096) != 0:
            Goto('L0')
        elif ConditionGroup(2):
            Goto('L3')
        """State 9: Appearance: Sign & Phantom: Stop generation"""
        Label('L4')
        DeleteNpcPhantom(z35)
    """State 10: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 13: End state"""
    return 0

def event_m20_21_x180(z30=_, z31=_, z32=_, flag7=_, z33=-1):
    """NPC White Phantom Appearance: General Purpose: Durahan
    z30: White Phantom can appear: Global event flag
    z31: White Phantom: Generator ID
    z32: Death: Global event flag
    flag7: Hostile: Global event flag
    z33: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z31)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z32, 1)
        CompareEventFlag(1, flag7, 1)
        CompareEventFlag(2, z30, 1)
        CompareEventFlag(8, 100974, 1)
        CompareEventFlag(8, 100972, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z31)
            if GetEventFlag(221000006) != 0:
                """State 12: Appearance: Hostile: Waiting: After the Queen"""
                Label('L1')
                CompareEventFlag(0, z32, 1)
                if ConditionGroup(0):
                    pass
                elif (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747)
                      != 0 and GetEventFlag(221000001) != 0 and GetEventFlag(221000006) != 1 and GetEventFlag(flag7)
                      != 1):
                    """State 5: Appearance: System: Rerun"""
                    Label('L2')
                    RestartMachine()
                    Quit()
            elif GetEventFlag(221000096) != 0:
                Goto('L1')
            else:
                """State 10: Appearance: Hostile: Standby"""
                CompareEventFlag(0, z32, 1)
                CompareEventFlag(8, flag7, 0)
                CompareEventFlag(8, 100974, 0)
                CompareEventFlag(8, 100972, 0)
                CompareEventFlag(9, flag7, 0)
                CompareEventFlag(9, 100974, 1)
                CompareEventFlag(9, 100972, 1)
                CompareEventFlag(10, flag7, 0)
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
            GenerateNpcPhantom(z31)
            if (GetEventFlag(221000096) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100747) !=
                0 and GetEventFlag(221000001) != 0):
                """State 11: Appearance: Phantom sign showing: Waiting: After the queen"""
                CompareEventFlag(0, z32, 1)
                CompareEventFlag(1, flag7, 1)
                HasNpcPhantomSpawned(2, z31, 1)
                if ConditionGroup(2):
                    pass
                elif ConditionGroup(1):
                    Goto('L0')
                elif ConditionGroup(0):
                    Goto('L4')
            else:
                """State 8: Appearance: Phantom sign displayed: Waiting"""
                CompareEventFlag(0, z32, 1)
                CompareEventFlag(1, flag7, 1)
                HasNpcPhantomSpawned(2, z31, 1)
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
            HasNpcPhantomSpawned(0, z31, 0)
            assert ConditionGroup(0)
            Goto('L2')
        elif GetEventFlag(221000096) != 0:
            Goto('L0')
        elif ConditionGroup(2):
            Goto('L3')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        Label('L4')
        DeleteNpcPhantom(z31)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 13: End state"""
    return 0

def event_m20_21_x181(z27=20210406):
    """[Condition] King's door_Guest
    z27: Instance ID of king's door OBJ
    """
    """State 0,1: Has the door opened?"""
    CompareObjState(0, z27, 30, 0)
    assert ConditionGroup(0)
    """State 2: Door opened"""
    return 0

def event_m20_21_x182(z28=900000):
    """[Execution] King's Door_Guest
    z28: Point ID for changing navigation
    """
    """State 0,1: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z28, 2)
    """State 2: End state"""
    return 0

def event_m20_21_x183(z20=1200010, z21=1200011):
    """[Conditions] Boss Battle_Start: Anderu
    z20: Start point ID
    z21: End point ID
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
    IsPlayerInsidePoint(8, z20, z21, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 9)
    IsPlayerInsidePoint(9, z20, z21, 1)
    IsHost(9, 0, 0)
    assert ConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m20_21_x184(z20=1200010, z21=1200011, z22=701, z23=1021040, z24=221020005, flag6=221000006):
    """[Preset] Boss Battle: Andyel
    z20: Start point ID
    z21: End point ID
    z22: Sound ID
    z23: Boss Battle ID
    z24: Other flags for logic
    flag6: Boss destruction flag
    """
    """State 0,4: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(flag5=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start: Andyel_SubState"""
        assert event_m20_21_x183(z20=z20, z21=z21)
        """State 6: [Execution] Boss Battle_Start: Andyel_SubState"""
        assert event_m20_21_x198(z15=z22, z16=z23, z17=z24)
        """State 7: [Reproduction] Boss Battle_Sky_2_SubState"""
        assert event_m20_21_x15()
        """State 9: [Condition] Boss Battle_HP Gauge Display: Andyel_SubState"""
        assert event_m20_21_x199()
        """State 8: [Execution] Boss Battle_HP Gauge Display: Andiel_SubState"""
        assert event_m20_21_x200()
        """State 1: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 3: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z16=z23)
        """State 2: [Execution] Boss Battle_End_SubState"""
        assert event_m20_21_x17(z15=z22, z16=z23, z17=z24, mode5=0)
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

def event_m20_21_x187(z25=20211800, z26=20211810):
    """[BEST] [Execution] End OBJ management_After end
    z25: Conventional end OBJ instance ID
    z26: EX end OBJ instance ID
    """
    """State 0,1: Disable end OBJ: 10"""
    ChangeObjState(z25, 10)
    ChangeObjState(z26, 10)
    """State 2: End state"""
    return 0

def event_m20_21_x188(z25=20211800, z26=20211810):
    """[BEST] [Execution] End OBJ management_After the deal
    z25: Conventional end OBJ instance ID
    z26: EX end OBJ instance ID
    """
    """State 0,1: Enable end OBJ: 20"""
    ChangeObjState(z25, 20)
    ChangeObjState(z26, 20)
    """State 2: End state"""
    return 0

def event_m20_21_x189(z25=20211800, z26=20211810):
    """[BEST] [execution] End OBJ management_after the queen
    z25: Conventional end OBJ instance ID
    z26: EX end OBJ instance ID
    """
    """State 0,2: weight"""
    CompareStateTime(0, 8, 3, 8)
    assert ConditionGroup(0)
    """State 1: Enable only conventional OBJ"""
    ChangeObjState(z25, 20)
    ChangeObjState(z26, 10)
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

def event_m20_21_x191(z25=20211800, z26=20211810):
    """[BEST] [Preset] End OBJ management
    z25: Conventional end OBJ instance ID
    z26: EX end OBJ instance ID
    """
    """State 0,1: [BEST] [Reproduction] End OBJ management_SubState"""
    assert event_m20_21_x185()
    """State 6: [BEST] [Condition] End OBJ management_SubState"""
    call = event_m20_21_x186()
    if call.Get() == 1:
        """State 3: [BEST] [Execution] End OBJ management_After end_SubState"""
        assert event_m20_21_x187(z25=z25, z26=z26)
    elif call.Get() == 2:
        """State 2: [BEST] [Execution] End OBJ management_After deal_SubState"""
        assert event_m20_21_x188(z25=z25, z26=z26)
    elif call.Get() == 0:
        """State 4: [BEST] [Execution] End OBJ Management_After the Queen_SubState"""
        assert event_m20_21_x189(z25=z25, z26=z26)
    elif call.Get() == 3:
        """State 5: [BEST] [Execution] End OBJ management_Waiting for next judgment_SubState"""
        assert event_m20_21_x190()
        """State 8: Rerun"""
        return 1
    """State 7: Finish"""
    return 0

def event_m20_21_x192(z11=910, z12=1105000, z13=221000007, flag4=221000006, z14=221000001):
    """[BEST] [Preset] Anderel_Initial layout change
    z11: Generator ID
    z12: Point ID for rematch
    z13: Flag for judging first battle or rematch
    flag4: Boss destruction flag
    z14: Memory read flag
    """
    """State 0,1: [BEST] [Reproduction] Andel_Initial layout change_SubState"""
    call = event_m20_21_x193(flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [BEST] [Condition] Anderel_Initial layout change_SubState"""
        call = event_m20_21_x194(z13=z13, z14=z14)
        if call.Get() == 2:
            """State 4: [BEST] [Execution] Andele_Initial location change_When conversation is dead_SubState"""
            assert event_m20_21_x201(z11=z11, z12=z12)
        elif call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 2: [BEST] [Execution] Undeal_Initial location change_SubState"""
            assert event_m20_21_x195(z11=z11, z12=z12)
    """State 5: End state"""
    return 0

def event_m20_21_x193(flag4=221000006):
    """[BEST] [Reproduction] Andel _ initial placement change
    flag4: Boss destruction flag
    """
    """State 0,1: Destroyed?"""
    if GetEventFlag(flag4) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Undefeated"""
        return 0

def event_m20_21_x194(z13=221000007, z14=221000001):
    """[BEST] [Condition] Andyel_Initial layout change
    z13: Flag to perform first battle or rematch determination
    z14: Memory read flag
    """
    """State 0,1: Is it the first game? Is it a rematch? Did you die during the conversation?"""
    CompareEventFlag(0, z13, 0)
    CompareEventFlag(8, z13, 0)
    CompareEventFlag(8, z14, 1)
    if ConditionGroup(8):
        """State 4: Died during conversation"""
        return 2
    elif ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m20_21_x195(z11=910, z12=1105000):
    """[BEST] [Execution] Andele_Initial placement change
    z11: Generator ID
    z12: Point ID for rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z11, z12)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z11, 0)
    """State 3: End state"""
    return 0

def event_m20_21_x196(z18=1200010, z19=1200011):
    """[Condition] Boss Battle_Start: Andyel_Sequential Battle
    z18: Start point ID
    z19: End point ID
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
    IsPlayerInsidePoint(8, z18, z19, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 9)
    IsPlayerInsidePoint(9, z18, z19, 1)
    IsHost(9, 0, 0)
    assert ConditionGroup(0)
    """State 11: End state"""
    return 0

def event_m20_21_x197(z15=701, z16=1021040, z17=221020005, flag5=221000006, z18=1200010, z19=1200011):
    """[Preset] Boss Battle: Andyel
    z15: Sound ID
    z16: Boss Battle ID
    z17: Other flags for logic
    flag5: Boss destruction flag
    z18: Start point ID
    z19: End point ID
    """
    """State 0,4: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_21_x12(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start: Andyel_Sequential Battle_SubState"""
        assert event_m20_21_x196(z18=z18, z19=z19)
        """State 6: [Execution] Boss Battle_Start: Andyel_SubState"""
        assert event_m20_21_x198(z15=z15, z16=z16, z17=z17)
        """State 7: [Reproduction] Boss Battle_Sky_2_SubState"""
        assert event_m20_21_x15()
        """State 9: [Condition] Boss Battle_HP Gauge Display: Andyel_SubState"""
        assert event_m20_21_x199()
        """State 8: [Execution] Boss Battle_HP Gauge Display: Andiel_SubState"""
        assert event_m20_21_x200()
        """State 1: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_21_x15()
        """State 3: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_21_x16(z16=z16)
        """State 2: [Execution] Boss Battle_End_SubState"""
        assert event_m20_21_x17(z15=z15, z16=z16, z17=z17, mode5=0)
    """State 10: End state"""
    return 0

def event_m20_21_x198(z15=701, z16=1021040, z17=221020005):
    """[Execution] Boss Battle_Start: Andyel
    z15: Sound ID
    z16: Boss Battle ID
    z17: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z15)
    """State 1: Boss battle start notification"""
    StartBossFight(z16)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z17, 1)
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

def event_m20_21_x201(z11=910, z12=1105000):
    """[BEST] [Execution] Andele_Initial location change_When conversation is dead
    z11: Generator ID
    z12: Point ID for rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPositionAndWarpGenerated(z11, z12)
    """State 2: End state"""
    return 0

def event_m20_21_x202(z7=102, z8=_, z9=221020090, mode1=0):
    """[Execution] Boss Battle_End_Queen Knight
    z7: Sound ID
    z8: Boss Battle ID
    z9: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z9, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z8)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z7)
    """State 7: Has the boss battle been finalized?"""
    IsEventBossBattle(0, z8, 0)
    assert ConditionGroup(0)
    """State 6: Isn't auto saving in progress?"""
    IsGameSaving(0, 0)
    assert ConditionGroup(0)
    """State 5: Save execution"""
    SaveExecution()
    """State 8: End state"""
    return 0

def event_m20_21_x203(z2=221020042):
    """[DC] [Reproduction] Flag switching with king's ring equipment
    z2: Logic flag
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
        SetEventFlag(z2, 1)
        """State 5: Equipped"""
        return 0
    else:
        """State 4: Logic flag OFF"""
        SetEventFlag(z2, 0)
        """State 7: Not equipped"""
        return 2
    """State 6: Finish"""
    Label('L0')
    return 1

def event_m20_21_x204(z4=_):
    """[DC] [Condition] Flag switch with king's ring equipment
    z4: Comparison value
    """
    """State 0,1: Equipment judgment"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, z4, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_21_x205(z2=221020042, z3=_):
    """[DC] [execution] Flag switch with king's ring equipment
    z2: Logic flag
    z3: ON or OFF
    """
    """State 0,1: Logic flag switching"""
    SetEventFlag(z2, z3)
    """State 2: End state"""
    return 0

def event_m20_21_x206(z2=221020042):
    """[DC] [Preset] Flag switch with king's ring equipment
    z2: Logic flag
    """
    """State 0,1: [DC] [Reproduction] Flag switch with king's ring equipment_SubState"""
    call = event_m20_21_x203(z2=z2)
    if call.Get() == 0:
        """State 3: [DC] [Condition] Flag switching with king's ring equipment_SubState"""
        assert event_m20_21_x204(z4=0)
        """State 2: [DC] [execution] Flag switch with king's ring equipment_SubState"""
        assert event_m20_21_x205(z2=z2, z3=0)
    elif call.Get() == 2:
        """State 5: [DC] [Condition] Flag switch with king's ring equipment_2_SubState"""
        assert event_m20_21_x204(z4=1)
        """State 4: [DC] [execution] Flag switch with king's ring equipment_2_SubState"""
        assert event_m20_21_x205(z2=z2, z3=1)
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

def event_m20_21_x208(flag1=221000025):
    """[DC] [execution] Kamen starts in treasure chest
    flag1: Masked start flag
    """
    """State 0,1: Masked activation flag ON"""
    SetEventFlag(flag1, 1)
    """State 2: End state"""
    return 0

def event_m20_21_x209(flag1=221000025):
    """[DC] [Reproduction] Mask starts in treasure chest
    flag1: Masked start flag
    """
    """State 0,1: Already started?"""
    if GetEventFlag(flag1) != 0:
        """State 3: Started: End"""
        return 1
    else:
        """State 2: Not running"""
        return 0

def event_m20_21_x210(z1=20215170, flag1=221000025):
    """[DC] [Preset] Mask is activated in treasure chest
    z1: Treasure chest OBJ instance ID
    flag1: Masked start flag
    """
    """State 0,1: [DC] [Reproduction] Mask is activated in the treasure box_SubState"""
    call = event_m20_21_x209(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Mask is activated in treasure box_SubState"""
        assert event_m20_21_x207(z1=z1)
        """State 2: [DC] [execution] The mask is activated in the treasure box_SubState"""
        assert event_m20_21_x208(flag1=flag1)
    """State 4: End state"""
    return 0

def event_m20_21_111015():
    """OBJ: Durahan: White phantom sign display"""
    """State 0,2: NPC White Phantom Appearance: General Purpose: Durahan_SubState"""
    event_m20_21_x180(z30=102010, z31=677, z32=104000, flag7=103500, z33=-1)
    Quit()
    """Unused"""
    """State 1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m20_21_x63(z130=102010, z131=677, z132=104000, z133=103500, z134=-1)
    Quit()

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
    Quit()

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
    Quit()

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
    Quit()

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
    Quit()

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
    Quit()

def event_m20_21_111182():
    """OBJ: Shenzhen Pilgrim: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_21_x1(z231=104123, z232=20214000, z233=41, z234=7250)
    Quit()

def event_m20_21_111183():
    """OBJ: Shenzhen Pilgrims: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7250:Darkdiver Grandahl
    event_m20_21_x8(z215=221010100, z216=221020101, z217=104120, z218=20214000, z219=111182, npc1=7250)
    Quit()

def event_m20_21_111184():
    """OBJ: Shenzhen Pilgrim: Death Determination"""
    """State 0,1: [Lib] NPC: Death Judgment: Shenzhen Pilgrim_SubState"""
    event_m20_21_x64(z128=40, z129=104123)
    Quit()

def event_m20_21_111185():
    """OBJ: Shenzhen Pilgrim: Appearance Judgment"""
    """State 0,1: [Lib] NPC: Shenzhen Pilgrim: Appearance Judgment_SubState"""
    event_m20_21_x52(z158=102316, z159=102323, z160=102331, z161=102333, z162=102315, z163=102317, z164=103623)
    Quit()

def event_m20_21_111242():
    """OBJ: Moonlight Jun: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_21_x1(z231=104162, z232=20214200, z233=61, z234=7430)
    Quit()

def event_m20_21_111243():
    """OBJ: Satoshi Moonlight: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7430:Benhart of Jugo
    event_m20_21_x8(z215=221010140, z216=221020141, z217=104160, z218=20214200, z219=111242, npc1=7430)
    Quit()

def event_m20_21_111244():
    """OBJ: Satoshi Moonlight: Judgment of death"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m20_21_x10(z209=60, z210=104162)
    Quit()

def event_m20_21_111245():
    """OBJ: Tsukimitsu: Appearance judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m20_21_x36(z188=104160, z189=102421, z190=102422, z191=221020147, z192=103661)
    Quit()

def event_m20_21_111246():
    """OBJ: Satoshi Moonlight: Defeat Queen Armor: White Phantom Sign Display"""
    """State 0,2: [Lib] NPC White Phantom Appearance: General Purpose: Akira Moonlight_SubState"""
    event_m20_21_x179(z34=104160, z35=678, z36=104160, flag8=103660, z37=63)
    Quit()
    """Unused"""
    """State 1: NPC White Phantom Appearance: General: OFF_SubState"""
    event_m20_21_x54(z152=104160, z153=678, z154=104160, z155=103660, z156=63)
    Quit()

def event_m20_21_111247():
    """OBJ: Satoshi Tsutsumi: Defeated Queen Armor: White Phantom"""
    """State 0: Start state"""
    assert GetEventFlag(221000001) != 1
    """State 1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m20_21_x59(z146=221000096, z147=102436, z148=205, z149=7430)
    Quit()

def event_m20_21_111248():
    """OBJ: Satoshi Tsutsumi: Defeat Mirror Knight: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m20_21_x47(z177=102431, z178=676, z179=104160, z180=63, z181=103660, z182=-1)
    Quit()

def event_m20_21_111249():
    """OBJ: Satoshi Tsutsumi: Defeat Mirror Knight: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m20_21_x59(z146=221000086, z147=102436, z148=205, z149=7430)
    Quit()

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
    Quit()
    """Unused"""
    """State 7: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_21_x1(z231=104240, z232=20214300, z233=306, z234=7602)
    Quit()

def event_m20_21_111323():
    """OBJ: Captive Girl: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7602:Imprisoned Milfanito
    event_m20_21_x8(z215=221010150, z216=221020151, z217=104240, z218=20214300, z219=111322, npc1=7602)
    Quit()

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
    Quit()

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
    Quit()

def event_m20_21_111435():
    """OBJ: Enclosed Person: Black Phantom Appearance"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m20_21_x60(z140=102810, z141=10002000, z142=670, z143=104340, z144=0, z145=2)
    Quit()

def event_m20_21_111800():
    """White Spirit: Mirror Night"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z157=679)
    Quit()

def event_m20_21_111801():
    """White phantom sign display for Anderu"""
    """State 0,1: Confirm the deal flag"""
    assert GetEventFlag(100747) != 0 and GetEventFlag(100978) != 0 and GetEventFlag(100972) != 0
    """State 2: NPC White Phantom Appearance: General Purpose: Andyel_SubState"""
    event_m20_21_x180(z30=100972, z31=680, z32=0, flag7=0, z33=-1)
    Quit()

def event_m20_21_111802():
    """Small White Spirit: Lobby"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z157=681)
    Quit()

def event_m20_21_111803():
    """Kobaku Rei: Warrior in the Mirror"""
    """State 0,1: Golem lighthouse confirmation"""
    assert GetEventFlag(221000030) != 0 and GetEventFlag(221000031) != 0
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z157=682)
    Quit()

def event_m20_21_111804():
    """Small white spirit: key route"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_21_x53(z157=683)
    Quit()

def event_m20_21_118140():
    """Multi-use NPC: Meat Cut (Female): Black Phantom Appears"""
    """State 0,2: [Lib] [BEST] NPC Black Phantom Appearance: Online: Miracles"""
    event_m20_21_x72(z116=10001000, z117=671, z118=104320, z119=0, z120=1)
    Quit()
    """Unused"""
    """State 1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m20_21_x61(z136=10001000, z137=671, z138=0, z139=1)
    Quit()

def event_m20_21_120080():
    """Trophy: Deep Darkness Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_21_x62(flag21=221020109, z135=26)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m20_21_120110():
    """Trophy: Moonlight Sword"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_21_x62(flag21=221020148, z135=31)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m20_21_4000000():
    """[BEST] End OBJ management"""
    """State 0,3: [BEST] [Preset] End OBJ Management_SubState"""
    call = event_m20_21_x191(z25=20211800, z26=20211810)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m20_21_4001000():
    """[BEST] Andyel_initial placement change"""
    """State 0,2: [BEST] [Preset] Anderel_Initial layout change_SubState"""
    assert event_m20_21_x192(z11=910, z12=1105000, z13=221000007, flag4=221000006, z14=221000001)
    """State 1: Finish"""
    EndMachine()
    Quit()

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
    Quit()

def event_m20_21_4011000():
    """[DC] Flag switching with king's ring equipment"""
    """State 0,3: [DC] [Preset] Flag switch with king's ring equipment_SubState"""
    call = event_m20_21_x206(z2=221020042)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m20_21_4012000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m20_21_x76(flag18=221020043, z102=14, flag19=221000044, z103=3, z104=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m20_21_x81(z109=80000000, z110=0, z111=5, z112=968, val2=1, z113=10, z114=80000001,
                z115=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m20_21_x81(z109=80000100, z110=0, z111=5, z112=968, val2=2, z113=10, z114=80000101,
                z115=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m20_21_x81(z109=80000200, z110=0, z111=5, z112=968, val2=3, z113=10, z114=80000201,
                z115=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(221020045, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4012010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m20_21_x84(flag20=221000044, z107=968, mode4=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4013000():
    """[DC] Mask is activated in treasure chest"""
    """State 0,2: [DC] [Preset] Mask is activated in the treasure box_SubState"""
    assert event_m20_21_x210(z1=20215170, flag1=221000025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_21_x88(z105=9200, z106=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_21_x88(z105=9201, z106=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_21_x88(z105=9202, z106=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_21_4031000():
    """[DC] NPC White Spirit_Gesture Management_Mirror Night"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m20_21_x93(flag17=221000086, z100=825, z101=221020088)
    """State 1: Finish"""
    EndMachine()
    Quit()

