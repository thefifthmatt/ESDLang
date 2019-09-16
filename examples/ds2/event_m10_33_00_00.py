# -*- coding: utf-8 -*-
def event_m10_33_1000():
    """Thorns with switch"""
    """State 0,2: [Preset] Switch with switch_SubState"""
    assert event_m10_33_x38(z53=10331000, z54=10333005, z55=10333010, z56=100000, z57=100010, z58=0)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_2000():
    """Boss: Giant Mouse _ Battle"""
    """State 0,2: [Preset] Giant Mouse Battle_Start_SubState"""
    assert event_m10_33_x51(z26=133000081, z27=101, z28=1033000, z29=133020080, z30=5, mode1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_3000():
    """Bug key A_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331310, z65=10332505, val2=300000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_3100():
    """Bug key A_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331310)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_4000():
    """Bug key B_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331315, z65=10332510, val2=400000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_4100():
    """Bug key B_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331315)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_5000():
    """Bug key C_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331320, z65=10332500, val2=500000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_5100():
    """Bug key C_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331320)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_6000():
    """Bug Key D1_ Strong enemy"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331055, z65=10332620, val2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_6010():
    """Bug Key D2_ Strong enemy"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331130, z65=10332621, val2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_6020():
    """Bug Key D3_ Strong enemy"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331340, z65=10332622, val2=602000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_6100():
    """Bug key D1_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331055)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_6110():
    """Bug key D2_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331130)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_6120():
    """Bug key D3_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331340)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_8000():
    """Bug key F_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331325, z65=10332515, val2=800000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_8100():
    """Bug key F_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331325)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_9000():
    """Bug key G_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331330, z65=10332520, val2=900000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_9100():
    """Bug key G_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331330)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_10000():
    """Bug Key H_Hidden Road"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331085, z65=10332805, val2=1000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_10100():
    """Bug key H_"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331085)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_11000():
    """Bug key I1_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331090, z65=10332570, val2=1100000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_11010():
    """Bug Key I2_Dwarf Statue"""
    """State 0,2: [Preset] Bug key_Dwarf statue_Wall interlocking_SubState"""
    assert event_m10_33_x41(z42=10331090, z43=1101000, z44=10332325, z45=10332570)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_11100():
    """Bug key I1_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331090)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_12000():
    """Bug Key J_Hidden Road"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331095, z65=10332800, val2=1200000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_12100():
    """Bug key J_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331095)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_13000():
    """Bug Key K_Closed"""
    """State 0,2: [Preset] Bug key_Closed, Spike_SubState"""
    assert event_m10_33_x30(z62=10331015, z63=10333000, val1=1300000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_13100():
    """Bug key K_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331015)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_15000():
    """Bug Key M_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z46=10331100, z47=1500000, z48=10332300)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_15100():
    """Bug key M_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331100)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_16000():
    """Bug Key N_ Launch Disc"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z50=10331105, z51=1600000, z52=10332100)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_16100():
    """Bug key N_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331105)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_17000():
    """Bug Key O_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z46=10331300, z47=1700000, z48=10332305)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_17100():
    """Bug key O_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331300)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_18000():
    """Bug Key P_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z46=10331110, z47=1800000, z48=10332310)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_18100():
    """Bug key P_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331110)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_19000():
    """Bug key Q_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331020, z65=10332525, val2=1900000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_19100():
    """Bug key Q_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331020)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_20000():
    """Bug Key R_Hidden Road"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z64=10331335, z65=10332810, val2=2000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_20100():
    """Bug key R_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331335)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_21000():
    """Bug Key S_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z46=10331025, z47=2100000, z48=10332315)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_21100():
    """Bug key S_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331025)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_22000():
    """Bug Key T_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z46=10331345, z47=2200000, z48=10332320)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_22100():
    """Bug key T_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z76=10331345)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_23000():
    """Bug key U1"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z50=10331160, z51=2300000, z52=10332125)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_23010():
    """Bug key U2"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z50=10331160, z51=2301000, z52=10332120)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_23020():
    """Bug key U3"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z50=10331160, z51=2302000, z52=10332115)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_23030():
    """Bug key U4"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z50=10331160, z51=2303000, z52=10332110)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_23040():
    """Bug Key U5_ Launch Disc"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z50=10331160, z51=2304000, z52=10332105)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_23100():
    """Bug key U_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331160)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_24000():
    """Bug Key V1_ Strong enemy"""
    """State 0,2: [Preset] OBJ operation with bug keys, navigation switching_SubState"""
    assert event_m10_33_x27(z64=10331140, z65=10332601, val2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_24010():
    """Bug Key V2_ Strong enemy"""
    """State 0,2: [Preset] OBJ operation with bug keys, navigation switching_SubState"""
    assert event_m10_33_x27(z64=10331145, z65=10332602, val2=2401000)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_24020():
    """Bug Key V3_ Strong enemy"""
    """State 0,2: [Preset] OBJ operation with bug keys, navigation switching_SubState"""
    assert event_m10_33_x27(z64=10331150, z65=10332600, val2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_24100():
    """Bug key V1_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331140)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_24110():
    """Bug key V2_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331145)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_24120():
    """Bug key V3_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z77=10331150)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_30000():
    """Map light switch_overhead_1"""
    """State 0,2: [Preset] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x62(z14=10330000, z15=50, z16=10, z17=60, z18=80)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30010():
    """Map light switch_NPC room"""
    """State 0,2: [Preset] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x59(z19=10330010, z20=50, z21=10, z22=80)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30020():
    """Map light switch_rock surface"""
    """State 0,2: [Preset] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x62(z14=10330020, z15=90, z16=100, z17=110, z18=30)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30030():
    """Map light switch_Wall"""
    """State 0,2: [Preset] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x62(z14=10330030, z15=90, z16=100, z17=110, z18=30)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30040():
    """Map light switch_stairs"""
    """State 0,2: [Preset] Map light switch_5 target hits_SubState"""
    assert event_m10_33_x65(z8=10330040, z9=50, z10=90, z11=100, z12=110, z13=30)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30050():
    """Map light switch_Boss base"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330050, z24=30, z25=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30060():
    """Map light switch_Boss room entrance"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330060, z24=30, z25=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30070():
    """Map light switch_Overhead_2"""
    """State 0,2: [Preset] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x59(z19=10330070, z20=90, z21=110, z22=20)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30080():
    """Map light switch_Overhead_3"""
    """State 0,2: [Preset] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x59(z19=10330080, z20=90, z21=110, z22=20)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30090():
    """Map light switch_Overhead_4"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330090, z24=70, z25=80)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30100():
    """Map light switch_Overhead_5"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330100, z24=70, z25=80)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30110():
    """Map light switch_Torch_1"""
    """State 0,2: [Preset] Map light switch_Target hits 6_SubState"""
    assert event_m10_33_x68(z1=10330110, z2=90, z3=100, z4=110, z5=20, z6=120, z7=30)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30120():
    """Map light switch_Torch_2"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330120, z24=110, z25=20)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_30130():
    """Map light switch_Torch_3"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330130, z24=70, z25=80)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_33_80000():
    """Fireworks for regeneration 01_In front of the pledge area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_33_x17(z74=1033000, z75=1033099)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_81000():
    """After the prayer area 02_ in front of the boss room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_33_x17(z74=1033100, z75=1033199)
    """State 1: Finish"""
    EndMachine()

def event_m10_33_x0(z94=_, z95=_, z96=_, z97=_):
    """[Lib] NPC: Grave Placement: General purpose
    z94: Death map: Global event flag
    z95: Tomb: OBJ instance ID
    z96: Tomb move to: Generator ID
    z97: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z94, 1)
    IsGraveGeneratable(8, z97, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z95, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z95, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_33_x1(z91=_, z92=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z91: Global: death flag
    z92: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z92, 10, 0)
    CompareObjState(1, z92, 20, 0)
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
    IsObjSearched(0, z92)
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

def event_m10_33_x2(z89=_, z90=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z89: Area other flags: Ghost appearance
    z90: Area other flags: Conversation start
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
    SetEventFlag(z89, 1)
    CompareEventFlag(0, z89, 1)
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
    SetEventFlag(z90, 1)
    CompareEventFlag(0, z90, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_33_x3(z89=_, z90=_, z91=_, z92=_, z93=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z89: Ghost Appearance: Area Other Flag
    z90: Conversation start: Area and other flags
    z91: Death: Global event flag
    z92: Tomb: OBJ instance ID
    z93: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z93, 1, 0)
    CompareEventFlag(9, z89, 1)
    CompareObjState(9, z92, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z90, 1)
        CompareEventFlag(0, z90, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_33_x1(z91=z91, z92=z92, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_33_x2(z89=z89, z90=z90, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_33_x4(z87=_, z88=_):
    """[Lib] NPC: Death determination: General purpose
    z87: Generator ID
    z88: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z88, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z87)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z88, 1)
            CompareEventFlag(0, z88, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_33_x5(z82=104130, z83=102343, z84=0, z85=133020116, z86=103632):
    """[Lib] Appearance determination: General purpose
    z82: Death: Global event flag
    z83: Local emigration permission: Global event flag
    z84: Relocation permission after moving: Global event flag
    z85: Appearance determination: Area and other flags
    z86: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z82, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z83, 1)
            CompareEventFlag(8, z84, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z83, 1)
                CompareEventFlag(8, z86, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z85, 1)
                    CompareEventFlag(0, z85, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z85, 0)
                    CompareEventFlag(0, z85, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z85, 0)
        CompareEventFlag(0, z85, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m10_33_x6(z77=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z77: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_33_x7(z76=z77)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_33_x11(z76=z77)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_33_x12()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_33_x8(z76=z77, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_33_x9(z76=z77, z79=38, z80=3, z81=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_33_x10(z76=z77, z78=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_33_x7(z76=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z76: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z76, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z76, 10)
        assert CompareObjStateId(z76, 10, 0)
    elif CompareObjStateId(z76, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z76, 74, 1) and CompareObjStateId(z76, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_33_x8(z76=_, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z76: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z76)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_33_x9(z76=_, z79=38, z80=_, z81=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z76: Object instance ID
    z79: Key guide type
    z80: Event action
    z81: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z76, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z76, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z76, 30)
        assert CompareObjStateId(z76, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z76, z79, z80)
        assert PlayerIsInEventAction(z80) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z80, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z76, 74, 0)
        CompareObjState(1, z76, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z81)
            assert CompareObjStateId(z76, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z76, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_33_x10(z76=_, z78=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z76: Object instance ID
    z78: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z76, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_33_x11(z76=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z76: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z76, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x12():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x13(z76=_):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z76: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_33_x7(z76=z76)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_33_x11(z76=z76)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_33_x12()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_33_x8(z76=z76, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_33_x9(z76=z76, z79=38, z80=12, z81=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_33_x10(z76=z76, z78=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_33_x14():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x15(z74=_, z75=_):
    """[Lib] [execute] Rebirth fire
    z74: Flag start ID
    z75: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z74, z75, 0)
    """State 2: End state"""
    return 0

def event_m10_33_x16():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x17(z74=_, z75=_):
    """[Lib] [Preset] Rebirth
    z74: Flag start ID
    z75: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_33_x14()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_33_x16()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_33_x15(z74=z74, z75=z75)
    """State 4: End state"""
    return 0

def event_m10_33_x18(z70=10000000, z71=_, z72=0, z73=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z70: Summon range
    z71: Generator ID
    z72: Appearance: Minimum time
    z73: Appearance: Maximum time
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
            DeleteNpcPhantom(z71)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z70, z70, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z72, 3, z73)
                IsPlayerInsidePoint(1, z70, z70, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z71)
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

def event_m10_33_x19(z68=133020107, z69=22):
    """[Lib] [Preset] Get trophy
    z68: Acquisition trigger_other flags
    z69: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z68) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z68, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z69)
    """State 4: End state"""
    return 0

def event_m10_33_x20(z66=9000, z67=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z66: Generator ID
    z67: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z66, z67)
    """State 2: End state"""
    return 0

def event_m10_33_x21(z66=9000, z67=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z66: Generator ID
    z67: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z66, z67, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_33_x22(z66=9000):
    """[Lib] [DC] [Condition] Transparent characters
    z66: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z66)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x23(z66=9000, z67=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z66: Generator ID
    z67: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_33_x21(z66=z66, z67=z67)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_33_x22(z66=z66)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_33_x20(z66=z66, z67=z67)
    """State 4: End state"""
    return 0

def event_m10_33_x24(z64=_, val2=_, z65=_):
    """[Reproduction] Bug key _ 檻, hidden road
    z64: Bug key instance ID
    val2: Navimesh switching point ID
    z65: Instance ID of operation OBJ
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z64, 20, 0):
        pass
    else:
        Goto('L0')
    """State 4: Navigation switch_2"""
    DeleteNavimeshAttribute(val2, 2)
    if CompareObjStateId(z65, 20, 0):
        pass
    else:
        """State 5: OBJ status change"""
        ChangeObjState(z65, 70)
    """State 7: Simple end"""
    return 1
    """State 3: Skip without navigation switching"""
    Label('L0')
    if (not val2) != 0:
        pass
    else:
        """State 2: Navigation switching"""
        AddNavimeshAttribute(val2, 2)
    """State 6: End state"""
    return 0

def event_m10_33_x25(z62=_):
    """[Condition] OBJ operation with bug keys, navigation switching
    z62: Bug key instance ID
    """
    """State 0,1: Did you use an insect key?"""
    CompareObjState(0, z62, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x26(z65=_, val2=_):
    """[Execution] Bug key _, hidden road
    z65: イ ン ス タ ン ス Instance ID
    val2: Navi Mesh Switching Point Id
    """
    """State 0,1: OBJ state transition: 檻"""
    ChangeObjState(z65, 70)
    """State 2: Skip without navigation switching"""
    if (not val2) != 0:
        pass
    else:
        """State 4: Did the coffin open?"""
        CompareObjState(0, z65, 20, 0)
        assert ConditionGroup(0)
        """State 3: Navigation switching"""
        DeleteNavimeshAttribute(val2, 2)
    """State 5: End state"""
    return 0

def event_m10_33_x27(z64=_, z65=_, val2=_):
    """[Preset] Bug key _ 檻, hidden road
    z64: Bug key instance ID
    z65: Instance ID of operation OBJ
    val2: Navimesh switching point ID
    """
    """State 0,2: [Reproduction] Bug key _ 檻, hidden road _SubState"""
    call = event_m10_33_x24(z64=z64, val2=val2, z65=z65)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] OBJ operation with bug keys, navigation switching_SubState"""
        assert event_m10_33_x25(z62=z64)
        """State 3: [Execution] Bug key _ 檻, hidden road _SubState"""
        assert event_m10_33_x26(z65=z65, val2=val2)
    """State 4: End state"""
    return 0

def event_m10_33_x28(z63=10333000, val1=1300000):
    """[Execution] Insect key
    z63: イ ン ス タ ン ス Instance ID
    val1: Navi Mesh Switching Point Id
    """
    """State 0,1: OBJ state transition: 檻"""
    ChangeObjState(z63, 70)
    """State 2: Skip without navigation switching"""
    if (not val1) != 0:
        pass
    else:
        """State 3: Navigation switching"""
        AddNavimeshAttribute(val1, 2)
    """State 4: End state"""
    return 0

def event_m10_33_x29(z62=10331015, val1=1300000, z63=10333000):
    """[Reproduction] Bug key
    z62: Bug key instance ID
    val1: Navimesh switching point ID
    z63: Instance ID of operation OBJ
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z62, 20, 0):
        pass
    else:
        Goto('L0')
    """State 4: Navigation switch_2"""
    DeleteNavimeshAttribute(val1, 2)
    if CompareObjStateId(z63, 20, 0):
        pass
    else:
        """State 5: OBJ status change"""
        ChangeObjState(z63, 70)
    """State 7: Simple end"""
    return 1
    """State 3: Skip without navigation switching"""
    Label('L0')
    if (not val1) != 0:
        pass
    else:
        """State 2: Navigation switching"""
        DeleteNavimeshAttribute(val1, 2)
    """State 6: End state"""
    return 0

def event_m10_33_x30(z62=10331015, z63=10333000, val1=1300000):
    """[Preset] Bug key _ traffic stop, thorn
    z62: Bug key instance ID
    z63: Instance ID of operation OBJ
    val1: Navimesh switching point ID
    """
    """State 0,2: [Reproduction] Insect Key_Closed_Spotted_SubState"""
    call = event_m10_33_x29(z62=z62, val1=val1, z63=z63)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] OBJ operation with bug keys, navigation switching_SubState"""
        assert event_m10_33_x25(z62=z62)
        """State 3: [Execution] Insect Key_Closed, Spike_SubState"""
        assert event_m10_33_x28(z63=z63, val1=val1)
    """State 4: End state"""
    return 0

def event_m10_33_x31(z46=_, z47=_):
    """[Condition] Bug key_Dwarf statue, Launch disk
    z46: Bug key instance ID
    z47: Shooting start point ID
    """
    """State 0,1: Did you enter the point after using the bug key?"""
    CompareObjState(8, z46, 20, 0)
    IsPlayerInsidePoint(8, z47, z47, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_33_x32(z52=_, z61=5, z51=_):
    """[Execution] Bug key _ launch disk
    z52: Instance ID of operation OBJ
    z61: Cool time
    z51: Shooting start point
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z52, 70)
    """State 2: Cool time state"""
    CompareStateTime(8, z61, 3, z61)
    IsPlayerAnActor(1, 1)
    DoesActorExist(1, 0)
    SetConditionGroup(8, 1)
    assert HostConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x33(z50=_, z51=_, z52=_):
    """[Preset] Bug Key _ Launch Disc
    z50: Bug key instance ID
    z51: Shooting start point ID
    z52: OBJ instance ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z52, 0)
    """State 4: [Reproduction] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x39()
    """State 2: [Condition] Bug key_Dwarf statue, Launch disk_SubState"""
    assert event_m10_33_x31(z46=z50, z47=z51)
    """State 3: [Execution] Bug key_Dwarf statue, Launch disk_SubState"""
    assert event_m10_33_x32(z52=z52, z61=5, z51=z51)
    """State 5: End state"""
    return 0

def event_m10_33_x34(z46=_, z47=_, z48=_):
    """[Preset] Bug key_Dwarf statue
    z46: Bug key instance ID
    z47: Shooting start point ID
    z48: OBJ instance ID
    """
    """State 0,2: [Reproduction] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x39()
    """State 1: [Condition] Bug key_Dwarf statue, Launch disk_SubState"""
    assert event_m10_33_x31(z46=z46, z47=z47)
    """State 3: [Execution] Bug key_Dwarf statue_SubState"""
    assert event_m10_33_x40(z44=z48, z49=5, z43=z47)
    """State 4: End state"""
    return 0

def event_m10_33_x35(z53=10331000, z54=10333005, z55=10333010, z56=100000, z57=100010, z60=133020010):
    """[Reproduction] Switch with thorns
    z53: Switch OBJ instance ID
    z54: Thorn 1_OBJ instance ID
    z55: Thorn 2_OBJ instance ID
    z56: Navigation change point ID_1
    z57: Navigation change point ID_2
    z60: Switch status flag
    """
    """State 0,6: Are thorns in the initial state?"""
    if CompareObjStateId(z54, 10, 1) and CompareObjStateId(z55, 10, 1):
        """State 7: Switch status flag ON"""
        SetEventFlag(z60, 1)
        """State 4,1: Waiting for thorn withdrawal"""
        assert CompareObjStateId(z54, 10, 0) and CompareObjStateId(z55, 10, 0)
        """State 5,2: Undo switch: 80"""
        ChangeObjState(z53, 80)
        """State 3: Wait for switch to return"""
        assert CompareObjStateId(z53, 10, 0)
        """State 8: Switch status flag OFF"""
        SetEventFlag(z60, 0)
    else:
        pass
    """State 9: End state"""
    return 0

def event_m10_33_x36(z53=10331000):
    """[Condition] With a switch
    z53: Switch OBJ instance ID
    """
    """State 0,1: Was the switch pressed?"""
    CompareObjState(0, z53, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x37(z53=10331000, z54=10333005, z55=10333010, z56=100000, z57=100010, z59=133020010):
    """[Execute]
    z53: Switch OBJ instance ID
    z54: Thorn 1_OBJ instance ID
    z55: Thorn 2_OBJ instance ID
    z56: Navigation change point ID_1
    z57: Navigation change point ID_2
    z59: Switch status flag
    """
    """State 0,8: Switch status flag ON"""
    SetEventFlag(z59, 1)
    """State 1: Spike popping out: 70"""
    ChangeObjState(z54, 70)
    ChangeObjState(z55, 70)
    """State 3: Waiting for splinter"""
    CompareObjState(8, z54, 70, 0)
    CompareObjState(8, z55, 70, 0)
    assert ConditionGroup(8)
    """State 6,2: Waiting for thorn withdrawal"""
    CompareObjState(8, z54, 10, 0)
    CompareObjState(8, z55, 10, 0)
    assert ConditionGroup(8)
    """State 7,4: Undo switch: 80"""
    ChangeObjState(z53, 80)
    """State 5: Wait for switch to return"""
    CompareObjState(0, z53, 10, 0)
    assert ConditionGroup(0)
    """State 9: Switch status flag OFF"""
    SetEventFlag(z59, 0)
    """State 10: End state"""
    return 0

def event_m10_33_x38(z53=10331000, z54=10333005, z55=10333010, z56=100000, z57=100010, z58=0):
    """[Preset] Switch
    z53: Switch OBJ instance ID
    z54: Thorn 1_OBJ instance ID
    z55: Thorn 2_OBJ instance ID
    z56: Navigation change point ID_1
    z57: Navigation change point ID_2
    z58: Switch status flag
    """
    """State 0,1: [Reproduction] Thornet_SubState with a switch"""
    assert event_m10_33_x35(z53=z53, z54=z54, z55=z55, z56=z56, z57=z57, z60=133020010)
    """State 3: [Condition] With a switch"""
    assert event_m10_33_x36(z53=z53)
    """State 2: [Execution] Switch with the switch_SubState"""
    assert event_m10_33_x37(z53=z53, z54=z54, z55=z55, z56=z56, z57=z57, z59=133020010)
    """State 4: End state"""
    return 0

def event_m10_33_x39():
    """[Reproduction] Bug key _ dwarf statue, launch disk"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x40(z44=_, z49=5, z43=_):
    """[Execution] Bug key_Dwarf statue
    z44: Instance ID of operation OBJ
    z49: Cool time
    z43: Shooting start point ID
    """
    """State 0,4: Random lottery"""
    GenerateRandomNumber(0, 0, 999)
    """State 5: Random number judgment"""
    CompareEventRandValue(0, 0, 0, 0)
    if ConditionGroup(0):
        """State 3: OBJ state transition_2"""
        ChangeObjState(z44, 80)
    else:
        """State 1: OBJ state transition"""
        ChangeObjState(z44, 70)
    """State 2: Cool time state"""
    CompareStateTime(8, z49, 3, z49)
    IsPlayerAnActor(1, 1)
    DoesActorExist(1, 0)
    SetConditionGroup(8, 1)
    if HostConditionGroup(0):
        pass
    elif HostConditionGroup(8):
        pass
    """State 6: End state"""
    return 0

def event_m10_33_x41(z42=10331090, z43=1101000, z44=10332325, z45=10332570):
    """[Preset] Bug key_Dwarf statue_Wall interlocking
    z42: Bug key instance ID
    z43: Shooting start point ID
    z44: OBJ instance ID
    z45: Linked wall OBJ instance ID
    """
    """State 0,1: [Reproduction] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x39()
    """State 3: [Condition] Bug key _ Dwarf image, Launch disk _ Wall interlock _ SubState"""
    assert event_m10_33_x42(z42=z42, z43=z43, z45=z45)
    """State 2: [Execution] Bug key_Dwarf statue_SubState"""
    assert event_m10_33_x40(z44=z44, z49=5, z43=z43)
    """State 4: End state"""
    return 0

def event_m10_33_x42(z42=10331090, z43=1101000, z45=10332570):
    """[Condition] Bug key_Dwarf image, Launch disk_Wall interlock
    z42: Bug key instance ID
    z43: Shooting start point ID
    z45: Linked wall OBJ instance ID
    """
    """State 0,1: Did you enter the point with the wall open after using the insect key?"""
    CompareObjState(8, z42, 20, 0)
    CompareObjState(8, z45, 20, 0)
    IsPlayerInsidePoint(8, z43, z43, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_33_x43(z26=133000081):
    """[Reproduction] Giant mouse battle_start
    z26: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z26) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_33_x44(z28=1033000):
    """[Execution] Giant Mouse Battle_Start
    z28: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z28)
    """State 2: End state"""
    return 0

def event_m10_33_x45():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x46(z28=1033000):
    """[Condition] Giant mouse battle_end judgment
    z28: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z28, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x47(z27=101, z28=1033000, z41=133020080, mode1=0):
    """[Execution] Giant Mouse Battle_End
    z27: Sound ID
    z28: Boss Battle ID
    z41: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z41, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z28)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z27)
    """State 5: End state"""
    return 0

def event_m10_33_x48(z39=200000, z40=200000):
    """[Condition] Giant Mouse Battle_Start
    z39: Start point ID
    z40: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z39, z40, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z39, z40, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x49(z32=200010, z33=200010, z34=852, z35=2800, z36=2810, z37=2820, z38=2830):
    """[Condition] HP display, BGM playback and boss activation
    z32: Start point ID
    z33: End point ID
    z34: Boss generator ID
    z35: Zako ① Generator ID
    z36: Zako ② Generator ID
    z37: Zako ③ Generator ID
    z38: Zako ④ Generator ID
    """
    """State 0,1: Invaded or damaged the starting point"""
    IsPlayerInsidePoint(0, z32, z33, 1)
    CompareChrHpRatio(0, z34, 100, 4)
    CompareChrHpRatio(0, z35, 100, 4)
    CompareChrHpRatio(0, z36, 100, 4)
    CompareChrHpRatio(0, z37, 100, 4)
    CompareChrHpRatio(0, z38, 100, 4)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x50(z27=101, z31=133020080, z30=5, z28=1033000):
    """[Execution] HP display, BGM playback and boss activation
    z27: Sound ID
    z31: Logic flag
    z30: Wait time until display
    z28: Boss Battle ID
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z31, 1)
    """State 4: Wait until BGM playback and HP display"""
    CompareStateTime(0, z30, 2, z30)
    IsEventBossKill(1, z28, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z27)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 5: End state"""
    return 0

def event_m10_33_x51(z26=133000081, z27=101, z28=1033000, z29=133020080, z30=5, mode1=0):
    """[Preset] Giant Mouse Battle_Start
    z26: Boss destruction flag
    z27: Sound ID
    z28: Boss Battle ID
    z29: Other flags for logic
    z30: Wait time
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Giant Mouse Battle_Start_SubState"""
    call = event_m10_33_x43(z26=z26)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Giant Mouse Battle_Start_SubState"""
        assert event_m10_33_x48(z39=200000, z40=200000)
        """State 2: [Execution] Giant Mouse Battle_Start_SubState"""
        assert event_m10_33_x44(z28=z28)
        """State 4: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
        assert event_m10_33_x45()
        """State 6: [Condition] HP display, BGM playback and boss activation_SubState"""
        assert event_m10_33_x49(z32=200010, z33=200010, z34=852, z35=2800, z36=2810, z37=2820, z38=2830)
        """State 5: [Execution] HP display, BGM playback and boss activation_SubState"""
        assert event_m10_33_x50(z27=z27, z31=133020080, z30=z30, z28=z28)
        """State 7: [Reproduction] Giant Mouse Battle_End_Sky_SubState"""
        assert event_m10_33_x52()
        """State 9: [Condition] Giant Mouse Battle_End Judgment_SubState"""
        assert event_m10_33_x46(z28=z28)
        """State 8: [Execution] Giant Mouse Battle_End_SubState"""
        assert event_m10_33_x47(z27=z27, z28=z28, z41=133020080, mode1=mode1)
    """State 10: End state"""
    return 0

def event_m10_33_x52():
    """[Reproduction] Giant Mouse Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x53(z1=_):
    """[Reproduction] Map light switching
    z1: Event light ID
    """
    """State 0,1: Change light to default settings"""
    SetPointLightEnabled(z1, 0, 0)
    """State 2: End state"""
    return 0

def event_m10_33_x54(z24=_, z25=_):
    """[Condition] Map light switching_Target 2 hits
    z24: Light switching hit group ID ①
    z25: Light switching hit group ID ②
    """
    """State 0,1: Did you get a lighting hit?"""
    IsPlayerOnHitGroup(0, z24, 1)
    IsPlayerOnHitGroup(0, z25, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x55(z23=_, z24=_, z25=_):
    """[Execution] Map light switch_Target hits 2
    z23: Event light ID
    z24: Light switching hit group ID ①
    z25: Light switching hit group ID ②
    """
    """State 0,1: Switch light"""
    SetPointLightEnabled(z23, 1, 0)
    """State 2: Did you get out of the lighting hit?"""
    IsPlayerOnHitGroup(8, z24, 0)
    IsPlayerOnHitGroup(8, z25, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x56(z23=_, z24=_, z25=_):
    """[Preset] Map light switch_Target two hits
    z23: Event light ID
    z24: Light switching hit group ID ①
    z25: Light switching hit group ID ②
    """
    """State 0,1: [Reproduction] Map light switch_SubState"""
    assert event_m10_33_x53(z1=z23)
    """State 3: [Condition] Map light switch_Subject hits_SubState"""
    assert event_m10_33_x54(z24=z24, z25=z25)
    """State 2: [Execution] Map light switching_Target hits 2_SubState"""
    assert event_m10_33_x55(z23=z23, z24=z24, z25=z25)
    """State 4: End state"""
    return 0

def event_m10_33_x57(z20=_, z21=_, z22=_):
    """[Condition] Map light switching_Target 3 hits
    z20: Light switching hit group ID ①
    z21: Light switching hit group ID ②
    z22: Light switching hit group ID ③
    """
    """State 0,1: Did you get a lighting hit?"""
    IsPlayerOnHitGroup(0, z20, 1)
    IsPlayerOnHitGroup(0, z21, 1)
    IsPlayerOnHitGroup(0, z22, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x58(z19=_, z20=_, z21=_, z22=_):
    """[Execution] Map light switch_3 target hits
    z19: Event light ID
    z20: Light switching hit group ID ①
    z21: Light switching hit group ID ②
    z22: Light switching hit group ID ③
    """
    """State 0,1: Switch light"""
    SetPointLightEnabled(z19, 1, 0)
    """State 2: Did you get out of the lighting hit?"""
    IsPlayerOnHitGroup(8, z20, 0)
    IsPlayerOnHitGroup(8, z21, 0)
    IsPlayerOnHitGroup(8, z22, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x59(z19=_, z20=_, z21=_, z22=_):
    """[Preset] Map light switch_Target 3 hits
    z19: Event light ID
    z20: Light switching hit group ID ①
    z21: Light switching hit group ID ②
    z22: Light switching hit group ID ③
    """
    """State 0,1: [Reproduction] Map light switch_SubState"""
    assert event_m10_33_x53(z1=z19)
    """State 3: [Conditions] Map light switching_Target hits 3_SubState"""
    assert event_m10_33_x57(z20=z20, z21=z21, z22=z22)
    """State 2: [Execution] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x58(z19=z19, z20=z20, z21=z21, z22=z22)
    """State 4: End state"""
    return 0

def event_m10_33_x60(z15=_, z16=_, z17=_, z18=_):
    """[Condition] Map light switch_Target 4 hits
    z15: Light switching hit group ID ①
    z16: Light switching hit group ID ②
    z17: Light switching hit group ID ③
    z18: Light switching hit group ID ④
    """
    """State 0,1: Did you get a lighting hit?"""
    IsPlayerOnHitGroup(0, z15, 1)
    IsPlayerOnHitGroup(0, z16, 1)
    IsPlayerOnHitGroup(0, z17, 1)
    IsPlayerOnHitGroup(0, z18, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x61(z14=_, z15=_, z16=_, z17=_, z18=_):
    """[Execution] Map light switch_Target hit 4
    z14: Event light ID
    z15: Light switching hit group ID ①
    z16: Light switching hit group ID ②
    z17: Light switching hit group ID ③
    z18: Light switching hit group ID ④
    """
    """State 0,1: Switch light"""
    SetPointLightEnabled(z14, 1, 0)
    """State 2: Did you get out of the lighting hit?"""
    IsPlayerOnHitGroup(8, z15, 0)
    IsPlayerOnHitGroup(8, z16, 0)
    IsPlayerOnHitGroup(8, z17, 0)
    IsPlayerOnHitGroup(8, z18, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x62(z14=_, z15=_, z16=_, z17=_, z18=_):
    """[Preset] Map light switching_Target 4 hits
    z14: Event light ID
    z15: Light switching hit group ID ①
    z16: Light switching hit group ID ②
    z17: Light switching hit group ID ③
    z18: Light switching hit group ID ④
    """
    """State 0,1: [Reproduction] Map light switch_SubState"""
    assert event_m10_33_x53(z1=z14)
    """State 3: [Condition] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x60(z15=z15, z16=z16, z17=z17, z18=z18)
    """State 2: [Execution] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x61(z14=z14, z15=z15, z16=z16, z17=z17, z18=z18)
    """State 4: End state"""
    return 0

def event_m10_33_x63(z9=50, z10=90, z11=100, z12=110, z13=30):
    """[Condition] Map light switch_Target 5 hits
    z9: Light switching hit group ID ①
    z10: Light switching hit group ID ②
    z11: Light switching hit group ID ③
    z12: Light switching hit group ID ④
    z13: Light switching hit group ID ⑤
    """
    """State 0,1: Did you get a lighting hit?"""
    IsPlayerOnHitGroup(0, z9, 1)
    IsPlayerOnHitGroup(0, z10, 1)
    IsPlayerOnHitGroup(0, z11, 1)
    IsPlayerOnHitGroup(0, z12, 1)
    IsPlayerOnHitGroup(0, z13, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x64(z8=10330040, z9=50, z10=90, z11=100, z12=110, z13=30):
    """[Execution] Map light switch_5 target hits
    z8: Event light ID
    z9: Light switching hit group ID ①
    z10: Light switching hit group ID ②
    z11: Light switching hit group ID ③
    z12: Light switching hit group ID ④
    z13: Light switching hit group ID ⑤
    """
    """State 0,1: Switch light"""
    SetPointLightEnabled(z8, 1, 0)
    """State 2: Did you get out of the lighting hit?"""
    IsPlayerOnHitGroup(8, z9, 0)
    IsPlayerOnHitGroup(8, z10, 0)
    IsPlayerOnHitGroup(8, z11, 0)
    IsPlayerOnHitGroup(8, z12, 0)
    IsPlayerOnHitGroup(8, z13, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x65(z8=10330040, z9=50, z10=90, z11=100, z12=110, z13=30):
    """[Preset] Map light switch_5 target hits
    z8: Event light ID
    z9: Light switching hit group ID ①
    z10: Light switching hit group ID ②
    z11: Light switching hit group ID ③
    z12: Light switching hit group ID ④
    z13: Light switching hit group ID ⑤
    """
    """State 0,1: [Reproduction] Map light switch_SubState"""
    assert event_m10_33_x53(z1=z8)
    """State 3: [Conditions] Map light switching_5 target hits_SubState"""
    assert event_m10_33_x63(z9=z9, z10=z10, z11=z11, z12=z12, z13=z13)
    """State 2: [Execution] Map light switch_5 target hits_SubState"""
    assert event_m10_33_x64(z8=z8, z9=z9, z10=z10, z11=z11, z12=z12, z13=z13)
    """State 4: End state"""
    return 0

def event_m10_33_x66(z2=90, z3=100, z4=110, z5=20, z6=120, z7=30):
    """[Condition] Map light switching_Target 6 hits
    z2: Light switching hit group ID ①
    z3: Light switching hit group ID ②
    z4: Light switching hit group ID ③
    z5: Light switching hit group ID ④
    z6: Light switching hit group ID ⑤
    z7: Light switching hit group ID ⑥
    """
    """State 0,1: Did you get a lighting hit?"""
    IsPlayerOnHitGroup(0, z2, 1)
    IsPlayerOnHitGroup(0, z3, 1)
    IsPlayerOnHitGroup(0, z4, 1)
    IsPlayerOnHitGroup(0, z5, 1)
    IsPlayerOnHitGroup(0, z6, 1)
    IsPlayerOnHitGroup(0, z7, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x67(z1=10330110, z2=90, z3=100, z4=110, z5=20, z6=120, z7=30):
    """[Execution] Map light switch_Target 6 hits
    z1: Event light ID
    z2: Light switching hit group ID ①
    z3: Light switching hit group ID ②
    z4: Light switching hit group ID ③
    z5: Light switching hit group ID ④
    z6: Light switching hit group ID ⑤
    z7: Light switching hit group ID ⑥
    """
    """State 0,1: Switch light"""
    SetPointLightEnabled(z1, 1, 0)
    """State 2: Did you get out of the lighting hit?"""
    IsPlayerOnHitGroup(8, z2, 0)
    IsPlayerOnHitGroup(8, z3, 0)
    IsPlayerOnHitGroup(8, z4, 0)
    IsPlayerOnHitGroup(8, z5, 0)
    IsPlayerOnHitGroup(8, z6, 0)
    IsPlayerOnHitGroup(8, z7, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x68(z1=10330110, z2=90, z3=100, z4=110, z5=20, z6=120, z7=30):
    """[Preset] Map light switch_Target 6 hits
    z1: Event light ID
    z2: Light switching hit group ID ①
    z3: Light switching hit group ID ②
    z4: Light switching hit group ID ③
    z5: Light switching hit group ID ④
    z6: Light switching hit group ID ⑤
    z7: Light switching hit group ID ⑥
    """
    """State 0,1: [Reproduction] Map light switch_SubState"""
    assert event_m10_33_x53(z1=z1)
    """State 3: [Condition] Map light switch_Target hits 6_SubState"""
    assert event_m10_33_x66(z2=z2, z3=z3, z4=z4, z5=z5, z6=z6, z7=z7)
    """State 2: [Execution] Map light switch_Target hits 6_SubState"""
    assert event_m10_33_x67(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, z6=z6, z7=z7)
    """State 4: End state"""
    return 0

def event_m10_33_111202():
    """OBJ: Dwarf (Faros Door): Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_33_x0(z94=104134, z95=10334100, z96=246, z97=7260)

def event_m10_33_111203():
    """OBJ: Dwarf (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7260:Lonesome Gavlan
    event_m10_33_x3(z89=133010110, z90=133020111, z91=104130, z92=10334100, z93=111202, npc1=7260)

def event_m10_33_111204():
    """OBJ: Dwarf (hidden port): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_33_x4(z87=245, z88=104134)

def event_m10_33_111205():
    """OBJ: Dwarf (Hidden Port): Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_33_x5(z82=104130, z83=102343, z84=0, z85=133020116, z86=103632)

def event_m10_33_111512():
    """OBJ: King of the mouse (Faros door): Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_33_x0(z94=104422, z95=10334000, z96=286, z97=2262)

def event_m10_33_111513():
    """OBJ: Mouse king (Faros door): Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    event_m10_33_x3(z89=133010100, z90=133020101, z91=104420, z92=10334000, z93=111512, npc1=2262)

def event_m10_33_111514():
    """OBJ: Mouse king (Faros door): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_33_x4(z87=285, z88=104422)

def event_m10_33_118220():
    """Multi-use NPC: Mage (male): Black Phantom Appearance: Offline"""
    """State 0,1: [DC] Total lap count judgment"""
    if (GetGameCycleForBonfire(33660) > 2) != 0:
        """State 3: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_2_SubState"""
        event_m10_33_x18(z70=10000000, z71=631, z72=0, z73=2)
    else:
        """State 2: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
        event_m10_33_x18(z70=10000000, z71=630, z72=0, z73=2)

def event_m10_33_120040():
    """Trophy: Mouse Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_33_x19(z68=133020107, z69=22)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_33_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_33_x23(z66=9000, z67=96960000)
    """State 1: Finish"""
    EndMachine()

