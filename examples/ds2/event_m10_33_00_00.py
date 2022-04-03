# -*- coding: utf-8 -*-
def event_m10_33_1000():
    """Thorns with switch"""
    """State 0,2: [Preset] Switch with switch_SubState"""
    assert event_m10_33_x38(z52=10331000, z53=10333005, z54=10333010, z55=100000, z56=100010, z57=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_2000():
    """Boss: Giant Mouse _ Battle"""
    """State 0,2: [Preset] Giant Mouse Battle_Start_SubState"""
    assert event_m10_33_x51(flag1=133000081, z26=101, z27=1033000, z28=133020080, z29=5, mode1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_3000():
    """Bug key A_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331310, z64=10332505, val2=300000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_3100():
    """Bug key A_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331310)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_4000():
    """Bug key B_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331315, z64=10332510, val2=400000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_4100():
    """Bug key B_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331315)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_5000():
    """Bug key C_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331320, z64=10332500, val2=500000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_5100():
    """Bug key C_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331320)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_6000():
    """Bug Key D1_ Strong enemy"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331055, z64=10332620, val2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_6010():
    """Bug Key D2_ Strong enemy"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331130, z64=10332621, val2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_6020():
    """Bug Key D3_ Strong enemy"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331340, z64=10332622, val2=602000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_6100():
    """Bug key D1_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331055)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_6110():
    """Bug key D2_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331130)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_6120():
    """Bug key D3_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331340)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_8000():
    """Bug key F_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331325, z64=10332515, val2=800000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_8100():
    """Bug key F_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331325)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_9000():
    """Bug key G_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331330, z64=10332520, val2=900000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_9100():
    """Bug key G_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331330)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_10000():
    """Bug Key H_Hidden Road"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331085, z64=10332805, val2=1000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_10100():
    """Bug key H_"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331085)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_11000():
    """Bug key I1_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331090, z64=10332570, val2=1100000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_11010():
    """Bug Key I2_Dwarf Statue"""
    """State 0,2: [Preset] Bug key_Dwarf statue_Wall interlocking_SubState"""
    assert event_m10_33_x41(z41=10331090, z42=1101000, z43=10332325, z44=10332570)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_11100():
    """Bug key I1_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331090)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_12000():
    """Bug Key J_Hidden Road"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331095, z64=10332800, val2=1200000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_12100():
    """Bug key J_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331095)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_13000():
    """Bug Key K_Closed"""
    """State 0,2: [Preset] Bug key_Closed, Spike_SubState"""
    assert event_m10_33_x30(z61=10331015, z62=10333000, val1=1300000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_13100():
    """Bug key K_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331015)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_15000():
    """Bug Key M_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z45=10331100, z46=1500000, z47=10332300)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_15100():
    """Bug key M_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_16000():
    """Bug Key N_ Launch Disc"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z49=10331105, z50=1600000, z51=10332100)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_16100():
    """Bug key N_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331105)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_17000():
    """Bug Key O_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z45=10331300, z46=1700000, z47=10332305)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_17100():
    """Bug key O_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331300)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_18000():
    """Bug Key P_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z45=10331110, z46=1800000, z47=10332310)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_18100():
    """Bug key P_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331110)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_19000():
    """Bug key Q_ 檻"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331020, z64=10332525, val2=1900000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_19100():
    """Bug key Q_Use bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_20000():
    """Bug Key R_Hidden Road"""
    """State 0,2: [Preset] Bug key _ 檻, hidden road _SubState"""
    assert event_m10_33_x27(z63=10331335, z64=10332810, val2=2000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_20100():
    """Bug key R_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331335)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_21000():
    """Bug Key S_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z45=10331025, z46=2100000, z47=10332315)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_21100():
    """Bug key S_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_22000():
    """Bug Key T_Dwarf Statue"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue_SubState"""
    assert event_m10_33_x34(z45=10331345, z46=2200000, z47=10332320)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_22100():
    """Bug key T_ Bug key use"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (floor) _SubState"""
    assert event_m10_33_x13(z74=10331345)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_23000():
    """Bug key U1"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z49=10331160, z50=2300000, z51=10332125)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_23010():
    """Bug key U2"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z49=10331160, z50=2301000, z51=10332120)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_23020():
    """Bug key U3"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z49=10331160, z50=2302000, z51=10332115)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_23030():
    """Bug key U4"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z49=10331160, z50=2303000, z51=10332110)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_23040():
    """Bug Key U5_ Launch Disc"""
    """State 0,2: [Preset] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x33(z49=10331160, z50=2304000, z51=10332105)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_23100():
    """Bug key U_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331160)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_24000():
    """Bug Key V1_ Strong enemy"""
    """State 0,2: [Preset] OBJ operation with bug keys, navigation switching_SubState"""
    assert event_m10_33_x27(z63=10331140, z64=10332601, val2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_24010():
    """Bug Key V2_ Strong enemy"""
    """State 0,2: [Preset] OBJ operation with bug keys, navigation switching_SubState"""
    assert event_m10_33_x27(z63=10331145, z64=10332602, val2=2401000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_24020():
    """Bug Key V3_ Strong enemy"""
    """State 0,2: [Preset] OBJ operation with bug keys, navigation switching_SubState"""
    assert event_m10_33_x27(z63=10331150, z64=10332600, val2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_24100():
    """Bug key V1_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331140)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_24110():
    """Bug key V2_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331145)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_24120():
    """Bug key V3_ using bug key"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_33_x6(z75=10331150)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_30000():
    """Map light switch_overhead_1"""
    """State 0,2: [Preset] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x62(z14=10330000, z15=50, z16=10, z17=60, z18=80)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30010():
    """Map light switch_NPC room"""
    """State 0,2: [Preset] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x59(z19=10330010, z20=50, z21=10, z22=80)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30020():
    """Map light switch_rock surface"""
    """State 0,2: [Preset] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x62(z14=10330020, z15=90, z16=100, z17=110, z18=30)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30030():
    """Map light switch_Wall"""
    """State 0,2: [Preset] Map light switching_Target hits 4_SubState"""
    assert event_m10_33_x62(z14=10330030, z15=90, z16=100, z17=110, z18=30)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30040():
    """Map light switch_stairs"""
    """State 0,2: [Preset] Map light switch_5 target hits_SubState"""
    assert event_m10_33_x65(z8=10330040, z9=50, z10=90, z11=100, z12=110, z13=30)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30050():
    """Map light switch_Boss base"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330050, z24=30, z25=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30060():
    """Map light switch_Boss room entrance"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330060, z24=30, z25=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30070():
    """Map light switch_Overhead_2"""
    """State 0,2: [Preset] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x59(z19=10330070, z20=90, z21=110, z22=20)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30080():
    """Map light switch_Overhead_3"""
    """State 0,2: [Preset] Map light switch_Target hits 3_SubState"""
    assert event_m10_33_x59(z19=10330080, z20=90, z21=110, z22=20)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30090():
    """Map light switch_Overhead_4"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330090, z24=70, z25=80)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30100():
    """Map light switch_Overhead_5"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330100, z24=70, z25=80)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30110():
    """Map light switch_Torch_1"""
    """State 0,2: [Preset] Map light switch_Target hits 6_SubState"""
    assert event_m10_33_x68(z1=10330110, z2=90, z3=100, z4=110, z5=20, z6=120, z7=30)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30120():
    """Map light switch_Torch_2"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330120, z24=110, z25=20)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_30130():
    """Map light switch_Torch_3"""
    """State 0,2: [Preset] Map light switch_Subject hits 2_SubState"""
    assert event_m10_33_x56(z23=10330130, z24=70, z25=80)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_80000():
    """Fireworks for regeneration 01_In front of the pledge area"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_33_x17(z72=1033000, z73=1033099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_81000():
    """After the prayer area 02_ in front of the boss room"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_33_x17(z72=1033100, z73=1033199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_33_x0(z92=_, z93=_, z94=_, z95=_):
    """[Lib] NPC: Grave Placement: General purpose
    z92: Death map: Global event flag
    z93: Tomb: OBJ instance ID
    z94: Tomb move to: Generator ID
    z95: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z92, 1)
    IsGraveGeneratable(8, z95, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z93, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z93, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_33_x1(z89=_, z90=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z89: Global: death flag
    z90: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z90, 10, 0)
    CompareObjState(1, z90, 20, 0)
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
    IsObjSearched(0, z90)
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

def event_m10_33_x2(z87=_, z88=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z87: Area other flags: Ghost appearance
    z88: Area other flags: Conversation start
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
    SetEventFlag(z87, 1)
    CompareEventFlag(0, z87, 1)
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
    SetEventFlag(z88, 1)
    CompareEventFlag(0, z88, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_33_x3(z87=_, z88=_, z89=_, z90=_, z91=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z87: Ghost Appearance: Area Other Flag
    z88: Conversation start: Area and other flags
    z89: Death: Global event flag
    z90: Tomb: OBJ instance ID
    z91: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z91, 1, 0)
    CompareEventFlag(9, z87, 1)
    CompareObjState(9, z90, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z88, 1)
        CompareEventFlag(0, z88, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_33_x1(z89=z89, z90=z90, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_33_x2(z87=z87, z88=z88, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_33_x4(z85=_, z86=_):
    """[Lib] NPC: Death determination: General purpose
    z85: Generator ID
    z86: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z86, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z85)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z86, 1)
            CompareEventFlag(0, z86, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_33_x5(z80=104130, z81=102343, z82=0, z83=133020116, z84=103632):
    """[Lib] Appearance determination: General purpose
    z80: Death: Global event flag
    z81: Local emigration permission: Global event flag
    z82: Relocation permission after moving: Global event flag
    z83: Appearance determination: Area and other flags
    z84: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z80, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z81, 1)
            CompareEventFlag(8, z82, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z81, 1)
                CompareEventFlag(8, z84, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z83, 1)
                    CompareEventFlag(0, z83, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z83, 0)
                    CompareEventFlag(0, z83, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z83, 0)
        CompareEventFlag(0, z83, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_33_x6(z75=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z75: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_33_x7(z74=z75)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_33_x11(z74=z75)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_33_x12()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_33_x8(z74=z75, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_33_x9(z74=z75, z77=38, z78=3, z79=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_33_x10(z74=z75, z76=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_33_x7(z74=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z74: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z74, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z74, 10)
        assert CompareObjStateId(z74, 10, 0)
    elif CompareObjStateId(z74, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z74, 74, 1) and CompareObjStateId(z74, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_33_x8(z74=_, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z74: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z74)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_33_x9(z74=_, z77=38, z78=_, z79=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z74: Object instance ID
    z77: Key guide type
    z78: Event action
    z79: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z74, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z74, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z74, 30)
        assert CompareObjStateId(z74, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z74, z77, z78)
        assert PlayerIsInEventAction(z78) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z78, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z74, 74, 0)
        CompareObjState(1, z74, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z79)
            assert CompareObjStateId(z74, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z74, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_33_x10(z74=_, z76=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z74: Object instance ID
    z76: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z74, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_33_x11(z74=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z74: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z74, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x12():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x13(z74=_):
    """[Lib] [Asynchronous] [Preset] Bug key (floor)
    z74: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_33_x7(z74=z74)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_33_x11(z74=z74)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_33_x12()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_33_x8(z74=z74, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_33_x9(z74=z74, z77=38, z78=12, z79=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_33_x10(z74=z74, z76=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_33_x14():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x15(z72=_, z73=_):
    """[Lib] [execute] Rebirth fire
    z72: Flag start ID
    z73: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z72, z73, 0)
    """State 2: End state"""
    return 0

def event_m10_33_x16():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x17(z72=_, z73=_):
    """[Lib] [Preset] Rebirth
    z72: Flag start ID
    z73: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_33_x14()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_33_x16()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_33_x15(z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m10_33_x18(z68=10000000, z69=_, z70=0, z71=2):
    """[Lib] NPC Black Phantom Appearance: Offline: Unconditional
    z68: Summon range
    z69: Generator ID
    z70: Appearance: Minimum time
    z71: Appearance: Maximum time
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
            DeleteNpcPhantom(z69)
            """State 8: Black Phantom Appearance: Online"""
            IsOffline(0, 1)
            assert ConditionGroup(0)
        else:
            """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
            IsPlayerInsidePoint(1, z68, z68, 1)
            IsOffline(0, 0)
            if ConditionGroup(1):
                """State 3: Black Phantom Appearance: Timer: Start"""
                CompareStateTime(0, z70, 3, z71)
                IsPlayerInsidePoint(1, z68, z68, 0)
                IsOffline(0, 0)
                if ConditionGroup(0):
                    """State 5: Black phantom appearance: Black phantom generation"""
                    GenerateNpcPhantom(z69)
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

def event_m10_33_x19(flag2=133020107, z67=22):
    """[Lib] [Preset] Get trophy
    flag2: Acquisition trigger_other flags
    z67: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag2) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag2, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z67)
    """State 4: End state"""
    return 0

def event_m10_33_x20(z65=9000, z66=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z65: Generator ID
    z66: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z65, z66)
    """State 2: End state"""
    return 0

def event_m10_33_x21(z65=9000, z66=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z65: Generator ID
    z66: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z65, z66, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_33_x22(z65=9000):
    """[Lib] [DC] [Condition] Transparent characters
    z65: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z65)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x23(z65=9000, z66=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z65: Generator ID
    z66: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_33_x21(z65=z65, z66=z66)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_33_x22(z65=z65)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_33_x20(z65=z65, z66=z66)
    """State 4: End state"""
    return 0

def event_m10_33_x24(z63=_, val2=_, z64=_):
    """[Reproduction] Bug key _ 檻, hidden road
    z63: Bug key instance ID
    val2: Navimesh switching point ID
    z64: Instance ID of operation OBJ
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z63, 20, 0):
        pass
    else:
        Goto('L0')
    """State 4: Navigation switch_2"""
    DeleteNavimeshAttribute(val2, 2)
    if CompareObjStateId(z64, 20, 0):
        pass
    else:
        """State 5: OBJ status change"""
        ChangeObjState(z64, 70)
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

def event_m10_33_x25(z61=_):
    """[Condition] OBJ operation with bug keys, navigation switching
    z61: Bug key instance ID
    """
    """State 0,1: Did you use an insect key?"""
    CompareObjState(0, z61, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x26(z64=_, val2=_):
    """[Execution] Bug key _, hidden road
    z64: イ ン ス タ ン ス Instance ID
    val2: Navi Mesh Switching Point Id
    """
    """State 0,1: OBJ state transition: 檻"""
    ChangeObjState(z64, 70)
    """State 2: Skip without navigation switching"""
    if (not val2) != 0:
        pass
    else:
        """State 4: Did the coffin open?"""
        CompareObjState(0, z64, 20, 0)
        assert ConditionGroup(0)
        """State 3: Navigation switching"""
        DeleteNavimeshAttribute(val2, 2)
    """State 5: End state"""
    return 0

def event_m10_33_x27(z63=_, z64=_, val2=_):
    """[Preset] Bug key _ 檻, hidden road
    z63: Bug key instance ID
    z64: Instance ID of operation OBJ
    val2: Navimesh switching point ID
    """
    """State 0,2: [Reproduction] Bug key _ 檻, hidden road _SubState"""
    call = event_m10_33_x24(z63=z63, val2=val2, z64=z64)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] OBJ operation with bug keys, navigation switching_SubState"""
        assert event_m10_33_x25(z61=z63)
        """State 3: [Execution] Bug key _ 檻, hidden road _SubState"""
        assert event_m10_33_x26(z64=z64, val2=val2)
    """State 4: End state"""
    return 0

def event_m10_33_x28(z62=10333000, val1=1300000):
    """[Execution] Insect key
    z62: イ ン ス タ ン ス Instance ID
    val1: Navi Mesh Switching Point Id
    """
    """State 0,1: OBJ state transition: 檻"""
    ChangeObjState(z62, 70)
    """State 2: Skip without navigation switching"""
    if (not val1) != 0:
        pass
    else:
        """State 3: Navigation switching"""
        AddNavimeshAttribute(val1, 2)
    """State 4: End state"""
    return 0

def event_m10_33_x29(z61=10331015, val1=1300000, z62=10333000):
    """[Reproduction] Bug key
    z61: Bug key instance ID
    val1: Navimesh switching point ID
    z62: Instance ID of operation OBJ
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z61, 20, 0):
        pass
    else:
        Goto('L0')
    """State 4: Navigation switch_2"""
    DeleteNavimeshAttribute(val1, 2)
    if CompareObjStateId(z62, 20, 0):
        pass
    else:
        """State 5: OBJ status change"""
        ChangeObjState(z62, 70)
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

def event_m10_33_x30(z61=10331015, z62=10333000, val1=1300000):
    """[Preset] Bug key _ traffic stop, thorn
    z61: Bug key instance ID
    z62: Instance ID of operation OBJ
    val1: Navimesh switching point ID
    """
    """State 0,2: [Reproduction] Insect Key_Closed_Spotted_SubState"""
    call = event_m10_33_x29(z61=z61, val1=val1, z62=z62)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 1: [Condition] OBJ operation with bug keys, navigation switching_SubState"""
        assert event_m10_33_x25(z61=z61)
        """State 3: [Execution] Insect Key_Closed, Spike_SubState"""
        assert event_m10_33_x28(z62=z62, val1=val1)
    """State 4: End state"""
    return 0

def event_m10_33_x31(z45=_, z46=_):
    """[Condition] Bug key_Dwarf statue, Launch disk
    z45: Bug key instance ID
    z46: Shooting start point ID
    """
    """State 0,1: Did you enter the point after using the bug key?"""
    CompareObjState(8, z45, 20, 0)
    IsPlayerInsidePoint(8, z46, z46, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_33_x32(z51=_, z60=5, z50=_):
    """[Execution] Bug key _ launch disk
    z51: Instance ID of operation OBJ
    z60: Cool time
    z50: Shooting start point
    """
    """State 0,1: OBJ state transition"""
    ChangeObjState(z51, 70)
    """State 2: Cool time state"""
    CompareStateTime(8, z60, 3, z60)
    IsPlayerAnActor(1, 1)
    DoesActorExist(1, 0)
    SetConditionGroup(8, 1)
    assert HostConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m10_33_x33(z49=_, z50=_, z51=_):
    """[Preset] Bug Key _ Launch Disc
    z49: Bug key instance ID
    z50: Shooting start point ID
    z51: OBJ instance ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z51, 0)
    """State 4: [Reproduction] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x39()
    """State 2: [Condition] Bug key_Dwarf statue, Launch disk_SubState"""
    assert event_m10_33_x31(z45=z49, z46=z50)
    """State 3: [Execution] Bug key_Dwarf statue, Launch disk_SubState"""
    assert event_m10_33_x32(z51=z51, z60=5, z50=z50)
    """State 5: End state"""
    return 0

def event_m10_33_x34(z45=_, z46=_, z47=_):
    """[Preset] Bug key_Dwarf statue
    z45: Bug key instance ID
    z46: Shooting start point ID
    z47: OBJ instance ID
    """
    """State 0,2: [Reproduction] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x39()
    """State 1: [Condition] Bug key_Dwarf statue, Launch disk_SubState"""
    assert event_m10_33_x31(z45=z45, z46=z46)
    """State 3: [Execution] Bug key_Dwarf statue_SubState"""
    assert event_m10_33_x40(z43=z47, z48=5, z42=z46)
    """State 4: End state"""
    return 0

def event_m10_33_x35(z52=10331000, z53=10333005, z54=10333010, z55=100000, z56=100010, z59=133020010):
    """[Reproduction] Switch with thorns
    z52: Switch OBJ instance ID
    z53: Thorn 1_OBJ instance ID
    z54: Thorn 2_OBJ instance ID
    z55: Navigation change point ID_1
    z56: Navigation change point ID_2
    z59: Switch status flag
    """
    """State 0,6: Are thorns in the initial state?"""
    if CompareObjStateId(z53, 10, 1) and CompareObjStateId(z54, 10, 1):
        """State 7: Switch status flag ON"""
        SetEventFlag(z59, 1)
        """State 4,1: Waiting for thorn withdrawal"""
        assert CompareObjStateId(z53, 10, 0) and CompareObjStateId(z54, 10, 0)
        """State 5,2: Undo switch: 80"""
        ChangeObjState(z52, 80)
        """State 3: Wait for switch to return"""
        assert CompareObjStateId(z52, 10, 0)
        """State 8: Switch status flag OFF"""
        SetEventFlag(z59, 0)
    else:
        pass
    """State 9: End state"""
    return 0

def event_m10_33_x36(z52=10331000):
    """[Condition] With a switch
    z52: Switch OBJ instance ID
    """
    """State 0,1: Was the switch pressed?"""
    CompareObjState(0, z52, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x37(z52=10331000, z53=10333005, z54=10333010, z55=100000, z56=100010, z58=133020010):
    """[Execute]
    z52: Switch OBJ instance ID
    z53: Thorn 1_OBJ instance ID
    z54: Thorn 2_OBJ instance ID
    z55: Navigation change point ID_1
    z56: Navigation change point ID_2
    z58: Switch status flag
    """
    """State 0,8: Switch status flag ON"""
    SetEventFlag(z58, 1)
    """State 1: Spike popping out: 70"""
    ChangeObjState(z53, 70)
    ChangeObjState(z54, 70)
    """State 3: Waiting for splinter"""
    CompareObjState(8, z53, 70, 0)
    CompareObjState(8, z54, 70, 0)
    assert ConditionGroup(8)
    """State 6,2: Waiting for thorn withdrawal"""
    CompareObjState(8, z53, 10, 0)
    CompareObjState(8, z54, 10, 0)
    assert ConditionGroup(8)
    """State 7,4: Undo switch: 80"""
    ChangeObjState(z52, 80)
    """State 5: Wait for switch to return"""
    CompareObjState(0, z52, 10, 0)
    assert ConditionGroup(0)
    """State 9: Switch status flag OFF"""
    SetEventFlag(z58, 0)
    """State 10: End state"""
    return 0

def event_m10_33_x38(z52=10331000, z53=10333005, z54=10333010, z55=100000, z56=100010, z57=0):
    """[Preset] Switch
    z52: Switch OBJ instance ID
    z53: Thorn 1_OBJ instance ID
    z54: Thorn 2_OBJ instance ID
    z55: Navigation change point ID_1
    z56: Navigation change point ID_2
    z57: Switch status flag
    """
    """State 0,1: [Reproduction] Thornet_SubState with a switch"""
    assert event_m10_33_x35(z52=z52, z53=z53, z54=z54, z55=z55, z56=z56, z59=133020010)
    """State 3: [Condition] With a switch"""
    assert event_m10_33_x36(z52=z52)
    """State 2: [Execution] Switch with the switch_SubState"""
    assert event_m10_33_x37(z52=z52, z53=z53, z54=z54, z55=z55, z56=z56, z58=133020010)
    """State 4: End state"""
    return 0

def event_m10_33_x39():
    """[Reproduction] Bug key _ dwarf statue, launch disk"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x40(z43=_, z48=5, z42=_):
    """[Execution] Bug key_Dwarf statue
    z43: Instance ID of operation OBJ
    z48: Cool time
    z42: Shooting start point ID
    """
    """State 0,4: Random lottery"""
    GenerateRandomNumber(0, 0, 999)
    """State 5: Random number judgment"""
    CompareEventRandValue(0, 0, 0, 0)
    if ConditionGroup(0):
        """State 3: OBJ state transition_2"""
        ChangeObjState(z43, 80)
    else:
        """State 1: OBJ state transition"""
        ChangeObjState(z43, 70)
    """State 2: Cool time state"""
    CompareStateTime(8, z48, 3, z48)
    IsPlayerAnActor(1, 1)
    DoesActorExist(1, 0)
    SetConditionGroup(8, 1)
    if HostConditionGroup(0):
        pass
    elif HostConditionGroup(8):
        pass
    """State 6: End state"""
    return 0

def event_m10_33_x41(z41=10331090, z42=1101000, z43=10332325, z44=10332570):
    """[Preset] Bug key_Dwarf statue_Wall interlocking
    z41: Bug key instance ID
    z42: Shooting start point ID
    z43: OBJ instance ID
    z44: Linked wall OBJ instance ID
    """
    """State 0,1: [Reproduction] Bug Key_Dwarf Statue, Launch Disc_SubState"""
    assert event_m10_33_x39()
    """State 3: [Condition] Bug key _ Dwarf image, Launch disk _ Wall interlock _ SubState"""
    assert event_m10_33_x42(z41=z41, z42=z42, z44=z44)
    """State 2: [Execution] Bug key_Dwarf statue_SubState"""
    assert event_m10_33_x40(z43=z43, z48=5, z42=z42)
    """State 4: End state"""
    return 0

def event_m10_33_x42(z41=10331090, z42=1101000, z44=10332570):
    """[Condition] Bug key_Dwarf image, Launch disk_Wall interlock
    z41: Bug key instance ID
    z42: Shooting start point ID
    z44: Linked wall OBJ instance ID
    """
    """State 0,1: Did you enter the point with the wall open after using the insect key?"""
    CompareObjState(8, z41, 20, 0)
    CompareObjState(8, z44, 20, 0)
    IsPlayerInsidePoint(8, z42, z42, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_33_x43(flag1=133000081):
    """[Reproduction] Giant mouse battle_start
    flag1: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag1) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_33_x44(z27=1033000):
    """[Execution] Giant Mouse Battle_Start
    z27: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z27)
    """State 2: End state"""
    return 0

def event_m10_33_x45():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_33_x46(z27=1033000):
    """[Condition] Giant mouse battle_end judgment
    z27: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z27, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x47(z26=101, z27=1033000, z40=133020080, mode1=0):
    """[Execution] Giant Mouse Battle_End
    z26: Sound ID
    z27: Boss Battle ID
    z40: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z40, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z27)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z26)
    """State 5: End state"""
    return 0

def event_m10_33_x48(z38=200000, z39=200000):
    """[Condition] Giant Mouse Battle_Start
    z38: Start point ID
    z39: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z38, z39, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z38, z39, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x49(z31=200010, z32=200010, z33=852, z34=2800, z35=2810, z36=2820, z37=2830):
    """[Condition] HP display, BGM playback and boss activation
    z31: Start point ID
    z32: End point ID
    z33: Boss generator ID
    z34: Zako ① Generator ID
    z35: Zako ② Generator ID
    z36: Zako ③ Generator ID
    z37: Zako ④ Generator ID
    """
    """State 0,1: Invaded or damaged the starting point"""
    IsPlayerInsidePoint(0, z31, z32, 1)
    CompareChrHpRatio(0, z33, 100, 4)
    CompareChrHpRatio(0, z34, 100, 4)
    CompareChrHpRatio(0, z35, 100, 4)
    CompareChrHpRatio(0, z36, 100, 4)
    CompareChrHpRatio(0, z37, 100, 4)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_33_x50(z26=101, z30=133020080, z29=5, z27=1033000):
    """[Execution] HP display, BGM playback and boss activation
    z26: Sound ID
    z30: Logic flag
    z29: Wait time until display
    z27: Boss Battle ID
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z30, 1)
    """State 4: Wait until BGM playback and HP display"""
    CompareStateTime(0, z29, 2, z29)
    IsEventBossKill(1, z27, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z26)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 5: End state"""
    return 0

def event_m10_33_x51(flag1=133000081, z26=101, z27=1033000, z28=133020080, z29=5, mode1=0):
    """[Preset] Giant Mouse Battle_Start
    flag1: Boss destruction flag
    z26: Sound ID
    z27: Boss Battle ID
    z28: Other flags for logic
    z29: Wait time
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Giant Mouse Battle_Start_SubState"""
    call = event_m10_33_x43(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Giant Mouse Battle_Start_SubState"""
        assert event_m10_33_x48(z38=200000, z39=200000)
        """State 2: [Execution] Giant Mouse Battle_Start_SubState"""
        assert event_m10_33_x44(z27=z27)
        """State 4: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
        assert event_m10_33_x45()
        """State 6: [Condition] HP display, BGM playback and boss activation_SubState"""
        assert event_m10_33_x49(z31=200010, z32=200010, z33=852, z34=2800, z35=2810, z36=2820, z37=2830)
        """State 5: [Execution] HP display, BGM playback and boss activation_SubState"""
        assert event_m10_33_x50(z26=z26, z30=133020080, z29=z29, z27=z27)
        """State 7: [Reproduction] Giant Mouse Battle_End_Sky_SubState"""
        assert event_m10_33_x52()
        """State 9: [Condition] Giant Mouse Battle_End Judgment_SubState"""
        assert event_m10_33_x46(z27=z27)
        """State 8: [Execution] Giant Mouse Battle_End_SubState"""
        assert event_m10_33_x47(z26=z26, z27=z27, z40=133020080, mode1=mode1)
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
    event_m10_33_x0(z92=104134, z93=10334100, z94=246, z95=7260)
    Quit()

def event_m10_33_111203():
    """OBJ: Dwarf (Hidden Port): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7260:Lonesome Gavlan
    event_m10_33_x3(z87=133010110, z88=133020111, z89=104130, z90=10334100, z91=111202, npc1=7260)
    Quit()

def event_m10_33_111204():
    """OBJ: Dwarf (hidden port): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_33_x4(z85=245, z86=104134)
    Quit()

def event_m10_33_111205():
    """OBJ: Dwarf (Hidden Port): Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_33_x5(z80=104130, z81=102343, z82=0, z83=133020116, z84=103632)
    Quit()

def event_m10_33_111512():
    """OBJ: King of the mouse (Faros door): Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_33_x0(z92=104422, z93=10334000, z94=286, z95=2262)
    Quit()

def event_m10_33_111513():
    """OBJ: Mouse king (Faros door): Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    event_m10_33_x3(z87=133010100, z88=133020101, z89=104420, z90=10334000, z91=111512, npc1=2262)
    Quit()

def event_m10_33_111514():
    """OBJ: Mouse king (Faros door): Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_33_x4(z85=285, z86=104422)
    Quit()

def event_m10_33_118220():
    """Multi-use NPC: Mage (male): Black Phantom Appearance: Offline"""
    """State 0,1: [DC] Total lap count judgment"""
    if (GetGameCycleForBonfire(33660) > 2) != 0:
        """State 3: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_2_SubState"""
        event_m10_33_x18(z68=10000000, z69=631, z70=0, z71=2)
        Quit()
    else:
        """State 2: [Lib] NPC Black Phantom Appearance: Offline: Unconditional_SubState"""
        event_m10_33_x18(z68=10000000, z69=630, z70=0, z71=2)
        Quit()

def event_m10_33_120040():
    """Trophy: Mouse Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_33_x19(flag2=133020107, z67=22)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_33_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_33_x23(z65=9000, z66=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

