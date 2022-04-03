# -*- coding: utf-8 -*-
def event_m20_10_1000():
    """Fireball fireball launch_1"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103700, val3=8)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1010():
    """Lively fireball launch_2"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103701, val3=10)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1020():
    """Lively fireball fire _3"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103702, val3=6)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1030():
    """Lively fireball fire _4"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103703, val3=7.5)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1040():
    """Lively fireball fire _5"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103704, val3=12)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1050():
    """Lively fireball fire _6"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103705, val3=9)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1060():
    """Lively fireball fire _7"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103706, val3=11)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_1070():
    """Lively fireball fire _8"""
    """State 0,2: Area judgment"""
    if GetEventFlag(105300) != 0:
        """State 3: Finish"""
        EndMachine()
        Quit()
    else:
        """State 4: [Preset] Fireball generation_Automatic launch_SubState"""
        assert event_m20_10_x70(z33=20103707, val3=8)
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m20_10_2000():
    """Front fireball _ launch management"""
    """State 0,2: [Preset] Front fireball_Launch management_SubState"""
    assert (event_m20_10_x94(z21=200000, z22=200000, z23=210020080, z24=2012, z25=2013, flag3=210020040,
            flag4=210020050))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_2012():
    """Front fireball fire _ Normal"""
    """State 0,3: [Preset] Front fireball launch_SubState"""
    assert event_m20_10_x90(z26=20103608, z27=1, z28=2)
    """State 4: [Preset] Front fireball fire_4_SubState"""
    assert event_m20_10_x90(z26=20103667, z27=0, z28=2)
    """State 2: Launch control flag ON"""
    SetEventFlag(210020040, 1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_2013():
    """Front fireball fire boss"""
    """State 0,3: [Preset] Front fireball launch_SubState"""
    assert event_m20_10_x90(z26=20103652, z27=0, z28=1.5)
    """State 6: [Preset] Front fireball fire_4_SubState"""
    assert event_m20_10_x90(z26=20103667, z27=0, z28=1.5)
    """State 5: [Preset] Front fireball firing_2_SubState"""
    assert event_m20_10_x90(z26=20103608, z27=0, z28=1.5)
    """State 4: [Preset] Front fireball fire_3_SubState"""
    assert event_m20_10_x90(z26=20103612, z27=0, z28=1.5)
    """State 2: Launch control flag ON"""
    SetEventFlag(210020050, 1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_3000():
    """Fireball launch _"""
    """State 0,2: [Preset] Stone Head Gorokuro_SubState"""
    assert event_m20_10_x86(z29=20103680, mode2=0, z30=300000, z31=300000, z32=20101050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_3010():
    """Navimesh change due to stone statue destruction"""
    """State 0,2: Waiting for the end of the event"""
    assert EventEnded(3000) != 0
    """State 3: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20101050, z75=20, z76=301000, z77=2, z78=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_4000():
    """Shaking Cantera_1"""
    """State 0,2: [Preset] Vibration in the cave_Lantern shaking_SubState"""
    assert event_m20_10_x66(flag5=210020010, z34=400000, z35=10, z36=201000002, z37=20101000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_4010():
    """Shaking Cantera_2"""
    """State 0,2: [Preset] Vibration in the cave_Lantern shaking_SubState"""
    assert event_m20_10_x66(flag5=210020011, z34=401000, z35=10, z36=201000002, z37=20101001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_5000():
    """Shaking chandelier"""
    """State 0,2: [Preset] Shaking Chandelier_Parent_SubState"""
    assert event_m20_10_x61(z40=500000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_5010():
    """Swinging chandelier_for OBJ01_Stair side"""
    """State 0,2: [Preset] Shaking Chandelier_OBJ_SubState"""
    assert event_m20_10_x62(z38=500000, val4=0.1, z39=20101350)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_5020():
    """Swing chandelier_OBJ 02"""
    """State 0,2: [Preset] Shaking Chandelier_OBJ_SubState"""
    assert event_m20_10_x62(z38=500000, val4=0.6, z39=20101351)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_5030():
    """Swinging chandelier_03 for OBJ"""
    """State 0,2: [Preset] Shaking Chandelier_OBJ_SubState"""
    assert event_m20_10_x62(z38=500000, val4=0, z39=20101352)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_5040():
    """Shaking chandelier for OBJ 04"""
    """State 0,2: [Preset] Shaking Chandelier_OBJ_SubState"""
    assert event_m20_10_x62(z38=500000, val4=0.2, z39=20101354)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_5050():
    """Shaking chandelier _ for OBJ 05_ wooden bridge side"""
    """State 0,2: [Preset] Shaking Chandelier_OBJ_SubState"""
    assert event_m20_10_x62(z38=500000, val4=0.8, z39=20101356)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_6000():
    """Giant soldier destroyed wall"""
    """State 0,2: [Preset] Giant breaks wall_SubState"""
    assert event_m20_10_x56(z41=20102700, z42=20100404, z43=600000, z44=210000070, z45=600020, z46=210000072)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_7000():
    """Wheel crane_1"""
    """State 0,2: [Preset] Wheel crane_SubState"""
    assert event_m20_10_x40(z49=20103050, z50=20103000, z51=700000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_7010():
    """Wheel crane_2"""
    """State 0,2: [Preset] Wheel crane_SubState"""
    assert event_m20_10_x40(z49=20103055, z50=20103005, z51=701000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_8000():
    """Boss: New Giant Senior Soldier (Living) _Battle"""
    """State 0,2: [Preset] New Giant Senior Soldier (Living) _Boss Battle_SubState"""
    assert (event_m20_10_x98(flag2=210000081, z14=30, z15=101, z16=2010000, z17=210020080, z18=800, z19=800000,
            mode1=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_9000():
    """Oil bottle 1"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_10_x30(z63=20102400, z64=20102450, z65=10, z66=240, z67=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_10_x34(z58=20102450, z59=10, z60=240, z61=0, z62=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_9020():
    """Oil bottle 3"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_10_x30(z63=20102402, z64=20102452, z65=20, z66=241, z67=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_10_x34(z58=20102452, z59=20, z60=241, z61=0, z62=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_9030():
    """Oil bottle 4"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_10_x30(z63=20102403, z64=20102453, z65=20, z66=242, z67=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_10_x34(z58=20102453, z59=20, z60=242, z61=0, z62=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_9040():
    """Oil bottle 5"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_10_x30(z63=20102404, z64=20102454, z65=20, z66=240, z67=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_10_x34(z58=20102454, z59=20, z60=240, z61=0, z62=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_10000():
    """Gained Seoul with Barista 1"""
    """State 0,2: [Preset] Obtaining Soul with Barista_SubState"""
    assert event_m20_10_x41(z47=20102302, z48=1000000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_10010():
    """Gained Seoul with Barista 2"""
    """State 0,2: [Preset] Obtaining Soul with Barista_SubState"""
    assert event_m20_10_x41(z47=20102306, z48=1001000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_10020():
    """Gained Seoul with Barista 3"""
    """State 0,2: [Preset] Obtaining Soul with Barista_SubState"""
    assert event_m20_10_x41(z47=20102317, z48=1002000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_10030():
    """Gained Seoul with Barista 4"""
    """State 0,2: [Preset] Obtaining Soul with Barista_SubState"""
    assert event_m20_10_x41(z47=20102303, z48=1003000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_11000():
    """[Insect Key] For trap activation with flying blade"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m20_10_x7(z81=20101100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_11010():
    """[Insect Key] Trap with flying blade"""
    """State 0,2: [Preset] Trap with flying blades_SubState"""
    assert event_m20_10_x45(z10=20101200, z11=20101100, z12=1101000, z13=1101000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_11100():
    """[Insect key] For hidden doors"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m20_10_x7(z81=20101110)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_11110():
    """[Insect key] Hidden door"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m20_10_x17(z79=20101110, val5=20100010, z80=0.6, val6=1.5)
    """State 3: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20101220, z75=20, z76=1111000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_12000():
    """Giant's memory time limit_after the king's door"""
    """State 0,2: Intrusion source determination"""
    if GetEventFlag(105300) != 0:
        """State 3: [Preset] Giant's memory time limit_SubState"""
        # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
        assert (event_m20_10_x78(z5=0, z6=210010001, val1=270, val2=290, z7=300, action1=2012, action2=2013,
                z8=3700000))
    else:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_12010():
    """Giant's memory time limit"""
    """State 0,1: Intrusion source determination"""
    if GetEventFlag(105301) != 0:
        """State 3: [Preset] Giant's memory time limit_SubState"""
        # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
        assert (event_m20_10_x78(z5=0, z6=210010001, val1=270, val2=290, z7=300, action1=2012, action2=2013,
                z8=3701000))
    else:
        pass
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m20_10_12020():
    """Giant's memory time limit_Vegrant"""
    """State 0,1: Intrusion source determination"""
    if GetEventFlag(105302) != 0:
        """State 3: [Preset] Giant's memory time limit_SubState"""
        # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
        assert (event_m20_10_x78(z5=0, z6=210010001, val1=270, val2=290, z7=300, action1=2012, action2=2013,
                z8=3702000))
    else:
        pass
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m20_10_13000():
    """Return from the dead body of the giant_after the king's door"""
    """State 0,2: [Preset] Return from Giant's corpse_SubState"""
    # lot:60004000:Soul of a Giant, goods:50920000:Soul of a Giant
    assert event_m20_10_x52(z1=20103520, z2=0, z3=0, z4=3700000, lot1=60004000, flag1=210000020, goods1=50920000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_13010():
    """Return from the dead body of the giant"""
    """State 0,2: [Preset] Return from Giant's corpse_SubState"""
    # lot:60004000:Soul of a Giant, goods:50920000:Soul of a Giant
    assert event_m20_10_x52(z1=20103500, z2=0, z3=0, z4=3701000, lot1=60004000, flag1=210000021, goods1=50920000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_13020():
    """Return from Giant's Corpse_Vegrant"""
    """State 0,2: [Preset] Return from Giant's corpse_SubState"""
    # lot:60004000:Soul of a Giant, goods:50920000:Soul of a Giant
    assert event_m20_10_x52(z1=20103510, z2=0, z3=0, z4=3702000, lot1=60004000, flag1=210000022, goods1=50920000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_15000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20101210, z75=20, z76=1500000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_16000():
    """Navigation mesh change due to fence destruction"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102500, z75=20, z76=1600000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18000():
    """Navimesh change due to half-breaking varistor destruction"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102350, z75=20, z76=1800000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18010():
    """Navimesh change due to half-breaking varistor destruction 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102351, z75=20, z76=1801000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18020():
    """Navimesh change due to half-breaking varistor destruction 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102352, z75=20, z76=1802000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18030():
    """Navimesh change due to half-breaking varistor destruction 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102353, z75=20, z76=1803000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18040():
    """Navimesh change due to half-breaking varistor destruction 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102354, z75=20, z76=1804000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18050():
    """Navimesh change due to half-breaking varistor destruction 6"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102355, z75=20, z76=1805000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18060():
    """Navimesh change due to half-breaking varistor destruction 7"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102356, z75=20, z76=1806000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18070():
    """Navi mesh change due to half-breaking varistor destruction 8"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102357, z75=20, z76=1807000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_18080():
    """Navimesh change due to half-breaking varistor destruction 9"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102358, z75=20, z76=1808000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19000():
    """Navimesh change due to varistor destruction 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102303, z75=20, z76=1900000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19010():
    """Navimesh change due to varistor destruction 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102302, z75=20, z76=1901000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19020():
    """Navimesh change due to varistor destruction 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102313, z75=20, z76=1902000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19030():
    """Navimesh change due to varistor destruction 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102306, z75=20, z76=1903000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19040():
    """Navimesh change due to varistor destruction 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102317, z75=20, z76=1904000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19050():
    """Navimesh change due to varistor destruction 6"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102320, z75=20, z76=1905000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19060():
    """Navimesh change due to varistor destruction 7"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102321, z75=20, z76=1906000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19070():
    """Navimesh change due to varistor destruction 8"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102322, z75=20, z76=1907000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19080():
    """Navimesh change due to varistor destruction 9"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102323, z75=20, z76=1908000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19090():
    """Navimesh change due to varistor destruction 10_1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102328, z75=20, z76=1909000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_19100():
    """Navimesh change due to varistor destruction 10_2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_10_x18(z74=20102329, z75=20, z76=1910000, z77=0, z78=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_20000():
    """Disabling damage"""
    """State 0,1: Giant King: Disabling instant death damage"""
    SetDamageImmunityByGeneratorId(800, 220100000, 1)
    """State 5: Giant King: Disabling Fireball Damage"""
    SetDamageImmunityByGeneratorId(800, 220100700, 1)
    """State 4: Kingdom Captain: Disabling Gorokuro Instant Death Damage"""
    SetDamageImmunityByGeneratorId(657, 220100000, 1)
    """State 6: Tsukimitsu: Disabling instant death damage"""
    SetDamageImmunityByGeneratorId(656, 220100000, 1)
    """State 3: PC: Disabling damage to giant kings"""
    SetDamageImmunityByCharacterId(100, 220100001, 1)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m20_10_80000():
    """Rebirth Fire 01_After the fallen giant's forest_King's door"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_10_x25(z72=2010000, z73=2010099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m20_10_x0(z2=0, z3=0, z102=10100000, z4=_):
    """[Lib] Warp between maps after poly play
    z2: Pre-warp poly play ID
    z3: Poly Play ID after Warp
    z102: Map ID
    z4: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z2, z3, z102, z4, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m20_10_x1(z98=_, z99=_, z100=_, z101=_):
    """[Lib] NPC: Grave Placement: General purpose
    z98: Death map: Global event flag
    z99: Tomb: OBJ instance ID
    z100: Tomb move to: Generator ID
    z101: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z98, 1)
    IsGraveGeneratable(8, z101, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z99, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z99, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m20_10_x2(z95=_, z96=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z95: Global: death flag
    z96: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z96, 10, 0)
    CompareObjState(1, z96, 20, 0)
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
    IsObjSearched(0, z96)
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

def event_m20_10_x3(z93=_, z94=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z93: Area other flags: Ghost appearance
    z94: Area other flags: Conversation start
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
    SetEventFlag(z93, 1)
    CompareEventFlag(0, z93, 1)
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
    SetEventFlag(z94, 1)
    CompareEventFlag(0, z94, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m20_10_x4(z93=_, z94=_, z95=_, z96=_, z97=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z93: Ghost Appearance: Area Other Flag
    z94: Conversation start: Area and other flags
    z95: Death: Global event flag
    z96: Tomb: OBJ instance ID
    z97: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z97, 1, 0)
    CompareEventFlag(9, z93, 1)
    CompareObjState(9, z96, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z94, 1)
        CompareEventFlag(0, z94, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m20_10_x2(z95=z95, z96=z96, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m20_10_x3(z93=z93, z94=z94, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m20_10_x5(z91=60, z92=104164):
    """[Lib] NPC: Death determination: General purpose
    z91: Generator ID
    z92: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z92, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z91)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z92, 1)
            CompareEventFlag(0, z92, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m20_10_x6(z86=104160, z87=102423, z88=0, z89=210020107, z90=103663):
    """[Lib] Appearance determination: General purpose
    z86: Death: Global event flag
    z87: Local emigration permission: Global event flag
    z88: Relocation permission after moving: Global event flag
    z89: Appearance determination: Area and other flags
    z90: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z86, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z87, 1)
            CompareEventFlag(8, z88, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z87, 1)
                CompareEventFlag(8, z90, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z89, 1)
                    CompareEventFlag(0, z89, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z89, 0)
                    CompareEventFlag(0, z89, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z89, 0)
        CompareEventFlag(0, z89, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m20_10_x7(z81=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z81: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m20_10_x8(z81=z81)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m20_10_x12(z81=z81)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m20_10_x13()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m20_10_x9(z81=z81, mode3=1, goods4=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m20_10_x10(z81=z81, z83=38, z84=3, z85=1, goods3=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m20_10_x11(z81=z81, z82=1, goods2=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m20_10_x8(z81=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z81: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z81, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z81, 10)
        assert CompareObjStateId(z81, 10, 0)
    elif CompareObjStateId(z81, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z81, 74, 1) and CompareObjStateId(z81, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m20_10_x9(z81=_, mode3=1, goods4=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z81: Object instance ID
    mode3: Number consumed
    goods4: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z81)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods4, 1, 1, 0) > mode3) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m20_10_x10(z81=_, z83=38, z84=3, z85=1, goods3=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z81: Object instance ID
    z83: Key guide type
    z84: Event action
    z85: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z81, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z81, 190, 2, goods3, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z81, 30)
        assert CompareObjStateId(z81, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z81, z83, z84)
        assert PlayerIsInEventAction(z84) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z84, 0)
        DoesPlayerHaveItem(0, goods3, 0, 5, 1, 1, 0)
        CompareObjState(1, z81, 74, 0)
        CompareObjState(1, z81, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods3, z85)
            assert CompareObjStateId(z81, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z81, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_x11(z81=_, z82=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z81: Object instance ID
    z82: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z81, 190, 2, goods2, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m20_10_x12(z81=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z81: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z81, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x13():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x14(z79=20101110, val5=20100010):
    """[Reproduction] Hidden door 1_face SFX
    z79: OBJ instance ID of the bug key
    val5: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z79, 20, 0):
        pass
    else:
        Goto('L0')
    """State 2: Event light reproduction judgment"""
    if (not val5) != 0:
        pass
    else:
        """State 3: Event light ON"""
        SetPointLightEnabled(val5, 1, 0)
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
    if (not val5) != 0:
        pass
    else:
        """State 4: Event light OFF"""
        SetPointLightEnabled(val5, 0, 0)
    """State 9: Not started"""
    return 1

def event_m20_10_x15(z79=20101110):
    """[Conditions] Hidden door 1_Face SFX
    z79: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z79, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x16(z79=20101110, val5=20100010, z80=0.6, val6=1.5):
    """[Execution] Hidden door 1_Face SFX
    z79: OBJ instance ID of the bug key
    val5: Event light ID
    z80: Light fade time
    val6: Wait until face SFX playback
    """
    """State 0,2: Event light usage judgment"""
    if (not val5) != 0:
        """State 5: Wait until face SFX playback"""
        assert (GetStateTime() > val6) != 0
        """State 4: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    else:
        """State 1: Event light ON"""
        SetPointLightEnabled(val5, 1, z80)
        assert (GetStateTime() > val6) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m20_10_x17(z79=20101110, val5=20100010, z80=0.6, val6=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z79: OBJ instance ID of the bug key
    val5: Event light ID
    z80: Light fade time
    val6: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m20_10_x14(z79=z79, val5=val5)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m20_10_x15(z79=z79)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m20_10_x16(z79=z79, val5=val5, z80=z80, val6=val6)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m20_10_x18(z74=_, z75=20, z76=_, z77=_, z78=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z74: Object instance ID
    z75: OBJ state ID
    z76: Navimesh switching point ID
    z77: Additional attributes
    z78: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m20_10_x19(z74=z74, z75=z75, z76=z76, z78=z78, z77=z77)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m20_10_x20(z74=z74, z75=z75, z76=z76)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m20_10_x21(z74=z74, z75=z75, z76=z76, z77=z77, z78=z78)
    """State 4: End state"""
    return 0

def event_m20_10_x19(z74=_, z75=20, z76=_, z78=_, z77=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z74: Target OBJ instance ID
    z75: Target OBJ state ID
    z76: Navimesh switching point ID
    z78: Additional attributes
    z77: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z74, z75, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z76, z78)
        DeleteNavimeshAttribute(z76, z77)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m20_10_x20(z74=_, z75=20, z76=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z74: Target OBJ instance ID
    z75: Target OBJ state ID
    z76: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z74, z75, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x21(z74=_, z75=20, z76=_, z77=_, z78=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z74: Target OBJ instance ID
    z75: Target OBJ state ID
    z76: Navimesh switching point ID
    z77: Additional attributes
    z78: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z76, z77)
    DeleteNavimeshAttribute(z76, z78)
    """State 2: End state"""
    return 0

def event_m20_10_x22():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x23(z72=2010000, z73=2010099):
    """[Lib] [execute] Rebirth fire
    z72: Flag start ID
    z73: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z72, z73, 0)
    """State 2: End state"""
    return 0

def event_m20_10_x24():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x25(z72=2010000, z73=2010099):
    """[Lib] [Preset] Rebirth
    z72: Flag start ID
    z73: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m20_10_x22()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m20_10_x24()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m20_10_x23(z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m20_10_x26(z68=210000081, z69=102436, z70=205, z71=7430):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z68: Defeat Boss 1: Area and other flags
    z69: Summon Achievement: Global Event Flag
    z70: Summon achievement count: global variable
    z71: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z69, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z68, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z70, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z70, NpcInfoValue(z71, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z69, 1)
                CompareEventFlag(0, z69, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m20_10_x27():
    """[Lib] [Reproduction] Oil 壺 Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x28(z63=_):
    """[Lib] [Conditions]
    z63: Oil bottle OBJ instance ID
    """
    """State 0,1: Was the oil bottle broken?"""
    IsObjBroken(0, z63, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x29(z64=_, z65=_, z66=_, z67=1):
    """[Lib] [execution]
    z64: Tar OBJ instance ID for firewood
    z65: Hit group ID
    z66: Replacement GMID
    z67: Change destination GM slot
    """
    """State 0,1: Oil tar display: 30"""
    ChangeObjState(z64, 30)
    """State 2: Change of material"""
    SetGroundMaterial(z65, z66, z67)
    """State 3: End state"""
    return 0

def event_m20_10_x30(z63=_, z64=_, z65=_, z66=_, z67=1):
    """[Lib] [Preset] Oil bottle
    z63: Oil bottle OBJ instance ID
    z64: Tar OBJ instance ID for firewood
    z65: Hit group ID
    z66: Replacement GMID
    z67: Change destination GM slot
    """
    """State 0,1: [Lib] [Reproduction] Oil bottle_Sky_SubState"""
    assert event_m20_10_x27()
    """State 3: [Lib] [Conditions] Oil 壺 _SubState"""
    assert event_m20_10_x28(z63=z63)
    """State 2: [Lib] [Execution] Oil bottle_SubState"""
    assert event_m20_10_x29(z64=z64, z65=z65, z66=z66, z67=z67)
    """State 4: End state"""
    return 0

def event_m20_10_x31(z59=_, z60=_, z62=1):
    """[Lib] [Reproduction] Tar material change
    z59: Hit group ID
    z60: Replacement GMID
    z62: Change destination GM slot
    """
    """State 0,1: Material change_initialization"""
    SetGroundMaterial(z59, z60, z62)
    """State 2: End state"""
    return 0

def event_m20_10_x32(z58=_):
    """[Lib] [Condition] Tar material change
    z58: OBJ instance ID of tar
    """
    """State 0,1: Did tar burn out?"""
    CompareObjState(0, z58, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x33(z58=_, z59=_, z60=_, z61=0):
    """[Lib] [execution] Tar material change
    z58: OBJ instance ID of tar
    z59: Hit group ID
    z60: Replacement GMID
    z61: Change destination GM slot
    """
    """State 0,1: Change of material"""
    SetGroundMaterial(z59, z60, z61)
    """State 2: End state"""
    return 0

def event_m20_10_x34(z58=_, z59=_, z60=_, z61=0, z62=1):
    """[Lib] [Preset] Tar material change
    z58: OBJ instance ID of tar
    z59: Hit group ID
    z60: Replace_GMID
    z61: After change_GM slot
    z62: Before change_GM slot
    """
    """State 0,1: [Reproduction] Tar material change_SubState"""
    assert event_m20_10_x31(z59=z59, z60=z60, z62=z62)
    """State 3: [Condition] Tar material change_SubState"""
    assert event_m20_10_x32(z58=z58)
    """State 2: [Execution] Tar material change_SubState"""
    assert event_m20_10_x33(z58=z58, z59=z59, z60=z60, z61=z61)
    """State 4: End state"""
    return 0

def event_m20_10_x35(flag6=_, z57=_):
    """[Lib] [Preset] Get trophy
    flag6: Acquisition trigger_other flags
    z57: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag6) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag6, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z57)
    """State 4: End state"""
    return 0

def event_m20_10_x36(z52=_, z53=_, z54=_, z55=_, z56=_):
    """[Lib] NPC White Phantom Appearance: General: Stops generation
    z52: White Phantom can appear: Global event flag
    z53: Person: Generator ID
    z54: Opponent: Generator
    z55: Death: Global event flag
    z56: Hostile: Global event flag
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Sign display: Judgment: Standby"""
        CompareEventFlag(0, z55, 1)
        CompareEventFlag(1, z56, 1)
        HasNpcPhantomSpawned(2, z54, 1)
        CompareEventFlag(3, z52, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Appearance: Phantom Appearance: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z53)
            """State 9: Appearance: Phantom Appearance: Not allowed: Wait"""
            CompareEventFlag(0, z55, 1)
            CompareEventFlag(8, z56, 0)
            HasNpcPhantomSpawned(8, z54, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(8):
                """State 8: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            Goto('L0')
        elif ConditionGroup(3):
            """State 3: Appearance: Sign display: Permission"""
            GenerateNpcPhantom(z53)
            """State 5: Appearance: Sign display: Wait"""
            CompareEventFlag(0, z55, 1)
            CompareEventFlag(1, z56, 1)
            HasNpcPhantomSpawned(2, z54, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                Goto('L0')
        """State 7: Appearance: Sign deletion: Stop generation"""
        Label('L2')
        DeleteNpcPhantom(z53)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 10: Appearance: Phantom is appearing: Waiting"""
    CompareEventFlag(0, z55, 1)
    CompareEventFlag(1, z56, 1)
    HasNpcPhantomSpawned(2, z53, 0)
    if ConditionGroup(0):
        Goto('L2')
    elif ConditionGroup(1):
        Goto('L0')
    elif ConditionGroup(3):
        Goto('L1')
    """State 11: End state"""
    return 0

def event_m20_10_x37():
    """[Reproduction] Wheel crane state reproduction"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x38(z49=_):
    """[Conditions] Judgment destruction determination
    z49: Fastener instance ID
    """
    """State 0,1: Group condition: Waiting for fastener breakage"""
    CompareObjState(0, z49, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x39(z50=_, z51=_):
    """[Execution] Wheel crane operation
    z50: Wheel crane instance ID
    z51: Point ID for Navimesh change
    """
    """State 0,1: OBJ state transition: crane down"""
    ChangeObjState(z50, 70)
    assert CompareObjStateId(z50, 20, 0)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z51, 2)
    """State 3: End state"""
    return 0

def event_m20_10_x40(z49=_, z50=_, z51=_):
    """[Preset] Wheel crane
    z49: Fastener instance ID
    z50: Wheel crane instance ID
    z51: Point ID for Navimesh change
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z50, 0)
    """State 2: [Reproduction] Reproducing wheel crane state_SubState"""
    assert event_m20_10_x37()
    """State 3: [Condition] Fastener destruction judgment_SubState"""
    assert event_m20_10_x38(z49=z49)
    """State 4: [Execution] Wheel crane operation_SubState"""
    assert event_m20_10_x39(z50=z50, z51=z51)
    """State 5: End state"""
    return 0

def event_m20_10_x41(z47=_, z48=_):
    """[Preset] Gained Seoul with Barista
    z47: Varistor OBJ instance ID
    z48: Seoul launcher point ID
    """
    """State 0,1: [Reproduction] Obtaining Soul with Barista_SubState"""
    assert event_m20_10_x42()
    """State 2: [Conditions] Obtaining Seoul with Barista_SubState"""
    call = event_m20_10_x43(z47=z47)
    if call.Get() == 0:
        """State 3: [Execution] Obtaining Soul with Barista_SubState"""
        assert event_m20_10_x44(z47=z47, z48=z48)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_10_x42():
    """[Reproduction] Obtaining Seoul with Barista"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x43(z47=_):
    """[Condition] Seoul gained with Barista
    z47: Varistor OBJ instance ID
    """
    """State 0,1: Was a bullet fired from a barista?"""
    CompareObjState(0, z47, 72, 0)
    assert ConditionGroup(0)
    """State 3: Random number generation"""
    GenerateRandomNumber(0, 0, 999)
    """State 2: Random number judgment"""
    CompareEventRandValue(0, 0, 0, 0)
    if ConditionGroup(0):
        """State 5: Get Seoul"""
        return 0
    else:
        """State 4: Varistor status judgment"""
        CompareObjState(0, z47, 10, 0)
        assert ConditionGroup(0)
        """State 6: Not available"""
        return 1

def event_m20_10_x44(z47=_, z48=_):
    """[Execution] Obtaining Seoul with Barista
    z47: Varistor OBJ instance ID
    z48: Seoul launcher point ID
    """
    """State 0,2: Seoul acquisition waiting time"""
    assert (GetStateTime() > 2) != 0
    """State 1: Get Seoul"""
    ObtainSoulsFromPoint(7777, 290000130, z48)
    """State 3: Varistor status judgment"""
    CompareObjState(0, z47, 10, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_10_x45(z10=20101200, z11=20101100, z12=1101000, z13=1101000):
    """[Preset] Trap with flying blade
    z10: Launcher OBJ instance ID
    z11: Bug ID OBJ instance ID
    z12: Trap start area_start point ID
    z13: Trap start area_end point ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z10, 0)
    """State 2: [Reproduction] Trap _SubState with flying blade"""
    call = event_m20_10_x46(z11=z11)
    if call.Get() == 0:
        """State 3: [Condition] Trap with flying blades_SubState"""
        assert event_m20_10_x47(z12=z12, z13=z13)
        """State 4: [Execution] Trap with flying blades_SubState"""
        assert event_m20_10_x48(z10=z10, z12=z12, z13=z13)
    elif call.Get() == 1:
        """State 5: [Condition] Trap with flying blades_Waiting for insect keys_SubState"""
        assert event_m20_10_x99(z11=z11)
    """State 6: End state"""
    return 0

def event_m20_10_x46(z11=20101100):
    """[Reproduction] Trap with flying blade
    z11: Bug ID OBJ instance ID
    """
    """State 0,1: Insect key status judgment"""
    if CompareObjStateId(z11, 20, 0):
        """State 2: Activated"""
        return 0
    else:
        """State 3: Not started"""
        return 1

def event_m20_10_x47(z12=1101000, z13=1101000):
    """[Condition] Trap with flying blade
    z12: Trap start area_start point ID
    z13: Trap start area_end point ID
    """
    """State 0,1: Did you enter the trap activation area?"""
    IsPlayerInsidePoint(0, z12, z13, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x48(z10=20101200, z12=1101000, z13=1101000):
    """[Execution] Trap with flying blade
    z10: Launcher OBJ instance ID
    z12: Trap start area_start point ID
    z13: Trap start area_end point ID
    """
    """State 0,1: Trap activation"""
    ChangeObjState(z10, 70)
    """State 2: Cool time"""
    CompareStateTime(0, 5, 3, 5)
    IsPlayerInsidePoint(0, z13, z13, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_10_x49(z1=_, flag1=_):
    """[Reproduction] Return from the dead body of the giant
    z1: Giant corpse OBJ instance ID
    flag1: Item acquisition confirmation flag
    """
    """State 0,2: Key guide activation: 30"""
    ChangeObjState(z1, 30)
    """State 3: Wait for transition"""
    assert CompareObjStateId(z1, 30, 0)
    """State 1: Did you get the item?"""
    if GetEventFlag(flag1) != 0:
        """State 5: It has been acquired"""
        return 1
    else:
        """State 4: Unacquired"""
        return 0

def event_m20_10_x50(z1=_, goods1=_):
    """[Condition] Return from the dead body of the giant
    z1: Giant corpse OBJ instance ID
    goods1: Acquisition judgment item ID
    """
    """State 0,1: Wait for decision to check"""
    IsObjSearched(0, z1)
    assert ConditionGroup(0)
    """State 2: Can you get the souls of giants?"""
    if CanGetItem(goods1, 1) != 0:
        """State 3: Available"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m20_10_x51(z1=_, z2=0, z3=0, z4=_):
    """[Execution] Return from the dead body of the giant
    z1: Giant corpse OBJ instance ID
    z2: Pre-warp poly play ID
    z3: Poly Play ID after Warp
    z4: Warp destination point ID
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: [Lib] Warp between maps after poly play_SubState"""
    assert event_m20_10_x0(z2=z2, z3=z3, z102=10100000, z4=z4)
    """State 4: End state"""
    return 0

def event_m20_10_x52(z1=_, z2=0, z3=0, z4=_, lot1=60004000, flag1=_, goods1=50920000):
    """[Preset] Return from the dead body of the giant
    z1: Giant corpse OBJ instance ID
    z2: Pre-warp poly play ID
    z3: Poly Play ID after Warp
    z4: Warp destination point ID
    lot1: Lottery ID for item acquisition
    flag1: Item acquisition confirmation flag
    goods1: Acquisition judgment item ID
    """
    """State 0,2: [Reproduction] Return from the dead body of the giant_SubState"""
    call = event_m20_10_x49(z1=z1, flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 4: [Condition] Return from the dead body of the giant_SubState"""
    assert event_m20_10_x50(z1=z1, goods1=0)
    """State 3: [Execution] Return from the dead body of the giant_SubState"""
    assert event_m20_10_x51(z1=z1, z2=z2, z3=z3, z4=z4)
    """State 8: End state"""
    return 0
    """State 5: [Condition] Return from Giant's corpse_Item acquisition_SubState"""
    Label('L0')
    call = event_m20_10_x50(z1=z1, goods1=goods1)
    if call.Get() == 0:
        """State 6: [Execute] Return from Giant's corpse_Item acquisition_SubState"""
        assert event_m20_10_x69(z1=z1, lot1=lot1, flag1=flag1)
    elif call.Get() == 1:
        """State 7: [Execution] Return from the dead body of the giant"""
        assert event_m20_10_x101(z1=z1, lot1=lot1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m20_10_x53(z41=20102700, z42=20100404, z43=600000):
    """[Reproduction] Giant destroyed wall
    z41: OBJ instance ID of the wall
    z42: OBJ instance ID of the door
    z43: Navigation change point ID
    """
    """State 0,1: Has the wall already broken?"""
    if CompareObjStateId(z41, 20, 0):
        """State 2: Navigation mesh change"""
        DeleteNavimeshAttribute(z43, 2)
        """State 4: Destroyed"""
        return 1
    else:
        """State 3: Undestructed"""
        return 0

def event_m20_10_x54(z45=600020):
    """[Condition] Giant destroyed wall
    z45: Point ID
    """
    """State 0,1: Open or wait after destruction"""
    IsPlayerInsidePoint(0, z45, z45, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x55(z41=20102700, z42=20100404, z43=600000, z44=210000070, z46=210000072):
    """[Execution] Giant destroyed wall
    z41: OBJ instance ID of the wall
    z42: OBJ instance ID of the door
    z43: Navigation change point ID
    z44: Giant Logic Flag
    z46: Wall destruction complete flag
    """
    """State 0,1: Giant Logic Flag ON"""
    SetEventFlag(z44, 1)
    """State 2: Was the wall broken? Or did a certain time have passed since the giant began to move?"""
    CompareObjState(0, z41, 20, 0)
    CompareStateTime(1, 30, 3, 30)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        """State 4: Destroy the wall (safety process)"""
        ChangeObjState(z41, 20)
    """State 5: Wall destruction complete flag ON"""
    SetEventFlag(z46, 1)
    """State 3: Navigation mesh change"""
    DeleteNavimeshAttribute(z43, 2)
    """State 6: End state"""
    return 0

def event_m20_10_x56(z41=20102700, z42=20100404, z43=600000, z44=210000070, z45=600020, z46=210000072):
    """[Preset] Giant destroyed wall
    z41: OBJ instance ID of the wall
    z42: OBJ instance ID of the door
    z43: Navigation change point ID
    z44: Giant Logic Flag
    z45: Point ID
    z46: Wall destruction complete flag
    """
    """State 0,1: [Reproduction] Giant destroyed wall_SubState"""
    call = event_m20_10_x53(z41=z41, z42=z42, z43=z43)
    if call.Done():
        """State 3: [Conditions] Giant destroyed wall_SubState"""
        assert event_m20_10_x54(z45=z45)
        """State 2: [Execution] Giant breaks wall_SubState"""
        assert event_m20_10_x55(z41=z41, z42=z42, z43=z43, z44=z44, z46=z46)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_10_x57():
    """[Reproduction] Shaking chandelier"""
    """State 0,1: The event ends if the chandelier shakes"""
    if GetEventFlag(210020016) != 0:
        """State 3: Event end"""
        return 1
    else:
        """State 2: End state"""
        return 0

def event_m20_10_x58(z38=500000):
    """[Condition] Shaking chandelier
    z38: Point ID
    """
    """State 0,1: Did you enter the specified area?"""
    IsPlayerInsidePoint(0, z38, z38, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x59():
    """[Execution] Shaking Chandelier _ Parent"""
    """State 0,1: Camera vibration, SE playback, flag ON"""
    ShakeCameraGlobal(10202000, 1)
    PlayOneShotSoundFollowingListener(201000002)
    SetEventFlag(210020016, 1)
    """State 2: End state"""
    return 0

def event_m20_10_x60(val4=_, z39=_):
    """[Execution] Shaking Chandelier_OBJ
    val4: Waiting time
    z39: Chandelier instance ID
    """
    """State 0,1: Time adjustment state"""
    assert (GetStateTime() > val4) != 0
    """State 2: Chandelier shaking: 70"""
    ChangeObjState(z39, 70)
    assert (GetStateTime() > 4) != 0
    """State 3: End state"""
    return 0

def event_m20_10_x61(z40=500000):
    """[Preset] Shaking chandelier_parent
    z40: Point ID
    """
    """State 0,1: [Reproduction] Shaking Chandelier_SubState"""
    call = event_m20_10_x57()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Shaking chandelier_SubState"""
        assert event_m20_10_x58(z38=z40)
        """State 3: [Execution] Shaking Chandelier_Parent_SubState"""
        assert event_m20_10_x59()
    """State 4: End state"""
    return 0

def event_m20_10_x62(z38=500000, val4=_, z39=_):
    """[Preset] Shaking Chandelier_OBJ
    z38: Point ID
    val4: Waiting time
    z39: Chandelier instance ID
    """
    """State 0,1: [Reproduction] Shaking Chandelier_SubState"""
    call = event_m20_10_x57()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Shaking chandelier_SubState"""
        assert event_m20_10_x58(z38=z38)
        """State 3: [Execution] swaying chandelier_OBJ_SubState"""
        assert event_m20_10_x60(val4=val4, z39=z39)
    """State 4: End state"""
    return 0

def event_m20_10_x63(flag5=_):
    """[Reproduction] Vibration in the cave _ Lantern shaking
    flag5: Activated flag
    """
    """State 0,1: Has the event ended?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Event end"""
        return 1
    else:
        """State 2: End state"""
        return 0

def event_m20_10_x64(z34=_):
    """[Condition] Vibration in the cave_Lantern shaking
    z34: Point ID
    """
    """State 0,1: Did you enter the specified area?"""
    IsPlayerInsidePoint(0, z34, z34, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x65(flag5=_, z35=10, z36=201000002, z37=_):
    """[Execution] Vibration in the cave_Lantern shaking
    flag5: Activated flag
    z35: SFXID
    z36: SEID
    z37: Canterra Impala ID
    """
    """State 0,1: Vibrate camera + SE"""
    ShakeCameraGlobal(10102000, 1)
    PlayOneShotSfxAtPoint(z35)
    PlayOneShotSoundFollowingListener(z36)
    """State 2: OBJ state transition: 70"""
    ChangeObjState(z37, 70)
    """State 3: Turn on the end flag"""
    SetEventFlag(flag5, 1)
    """State 4: End state"""
    return 0

def event_m20_10_x66(flag5=_, z34=_, z35=10, z36=201000002, z37=_):
    """[Preset] Vibration in the cave _ Lantern shaking
    flag5: Activated flag
    z34: Point ID
    z35: SFXID
    z36: SEID
    z37: Canterra Impala ID
    """
    """State 0,1: [Reproduction] Vibration in the cave_Lantern shaking_SubState"""
    call = event_m20_10_x63(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Cave vibration_Lantern shaking_SubState"""
        assert event_m20_10_x64(z34=z34)
        """State 3: [Execution] Vibration in the cave_Lantern shaking_SubState"""
        assert event_m20_10_x65(flag5=flag5, z35=z35, z36=z36, z37=z37)
    """State 4: End state"""
    return 0

def event_m20_10_x67(z33=_):
    """[Reproduction] Fireball generation
    z33: Damipoli OBJ instance ID for fireball
    """
    """State 0,1: OBJ initialization"""
    InitializeObj(z33)
    """State 2: End state"""
    return 0

def event_m20_10_x68(z33=_, val3=_):
    """[Execution] Fireball generation
    z33: Fireball Damipoli OBJ instance ID
    val3: Cool time
    """
    """State 0,2: Cool time state"""
    assert (GetStateTime() > val3) != 0
    """State 1: Fireball fire"""
    ChangeObjState(z33, 70)
    """State 3: End state"""
    return 0

def event_m20_10_x69(z1=_, lot1=60004000, flag1=_):
    """[Execution] Return from Giant's corpse_Item acquisition
    z1: Giant corpse OBJ instance ID
    lot1: Lottery ID for item acquisition
    flag1: Item acquisition confirmation flag
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60004000:Soul of a Giant
    AwardItem(lot1, 1)
    """State 4: Turn on the item acquisition flag"""
    SetEventFlag(flag1, 1)
    """State 5: End state"""
    return 0

def event_m20_10_x70(z33=_, val3=_):
    """[Preset] Fireball generation_Automatic launch
    z33: Damipoli OBJ instance ID for fireball
    val3: Cool time
    """
    """State 0,1: [Reproduction] Distant fireball generation_SubState"""
    assert event_m20_10_x67(z33=z33)
    """State 3: [Condition] Fireball generation_sky_SubState"""
    assert event_m20_10_x71()
    """State 2: [Execution] Distant fireball generation_SubState"""
    assert event_m20_10_x68(z33=z33, val3=val3)
    """State 4: End state"""
    return 0

def event_m20_10_x71():
    """[Condition] Fireball generation_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x72(flag2=210000081):
    """[Reproduction] Giant King Battle_Start
    flag2: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag2) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_10_x73(z14=30, z18=800):
    """[Condition] HP display, BGM playback and boss activation
    z14: Boss gauge display start distance
    z18: Generator ID
    """
    """State 0,1: Did you approach the boss? Or did you give damage?"""
    CompareChrPlayerDistance(0, 800, z14, 5)
    CompareChrHpRatio(0, z18, 100, 4)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x74(z16=2010000):
    """[Execution] Giant King Battle_Start
    z16: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z16)
    """State 2: End state"""
    return 0

def event_m20_10_x75():
    """[Reproduction] Giant King Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x76(z16=2010000):
    """[Condition] Giant King Battle_End Judgment
    z16: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z16, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x77(z15=101, z16=2010000, z17=210020080, mode1=0):
    """[Execution] Giant King Battle End
    z15: Sound ID
    z16: Boss Battle ID
    z17: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,5: Pausing the global timer"""
    SuspendGlobalTimer(0)
    """State 1: Logic flag OFF"""
    SetEventFlag(z17, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z16)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z15)
    """State 6: Waiting for global timer to resume"""
    assert (GetStateTime() > 9) != 0
    """State 7: Restart the global timer"""
    RestartGlobalTimer(0)
    """State 8: End state"""
    return 0

def event_m20_10_x78(z5=0, z6=210010001, val1=270, val2=290, z7=300, action1=2012, action2=2013, z8=_):
    """[Preset] Giant's memory time limit
    z5: Global timer ID
    z6: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    z7: Execution start time of the third phase process
    action1: Text ID to display in the first phase
    action2: Text ID to display in the third phase
    z8: Return Warp Point ID
    """
    """State 0,1: [Reproduction] Giant's memory time limit_SubState"""
    call = event_m20_10_x79(z5=z5, z6=z6, val1=val1, val2=val2)
    if call.Get() == 3:
        """State 8: [Conditions & Execution] Giant's Memory Time Limit_0th Phase_SubState"""
        # action:2011:"One cannot reside within memory for long"
        assert event_m20_10_x100(z5=z5, z9=5, action3=2011)
        """State 2: [Conditions & Execution] Giant's Memory Time Limit_First Phase_SubState"""
        assert event_m20_10_x80(z5=z5, val1=val1, action1=action1)
        """State 3: [Conditions & Execution] Giant's Memory Time Limit_Second Phase_SubState"""
        assert event_m20_10_x81(z5=z5, val2=val2, z6=z6)
        """State 4: [Conditions & Execution] Giant's Memory Time Limit_3rd Phase_SubState"""
        assert event_m20_10_x82(z5=z5, z7=z7, action2=action2, z8=z8)
    elif call.Get() == 0:
        """State 9: [Conditions & Execution] Giant's Memory Time Limit_First Phase_2_SubState"""
        assert event_m20_10_x80(z5=z5, val1=val1, action1=action1)
        """State 5: [Conditions & Execution] Giant's Memory Time Limit_Second Phase_2_SubState"""
        assert event_m20_10_x81(z5=z5, val2=val2, z6=z6)
        """State 6: [Conditions & Execution] Giant's Memory Time Limit_3rd Phase_2_SubState"""
        assert event_m20_10_x82(z5=z5, z7=z7, action2=action2, z8=z8)
    elif call.Get() == 1:
        """State 10: [Conditions & Execution] Giant's Memory Time Limit_Second Phase_3_SubState"""
        assert event_m20_10_x81(z5=z5, val2=val2, z6=z6)
        """State 7: [Conditions & Execution] Giant's Memory Time Limit_3rd Phase_3_SubState"""
        assert event_m20_10_x82(z5=z5, z7=z7, action2=action2, z8=z8)
    elif call.Get() == 2:
        """State 11: [Conditions & Execution] Giant's Memory Time Limit_3rd Phase_4_SubState"""
        assert event_m20_10_x82(z5=z5, z7=z7, action2=action2, z8=z8)
    """State 12: End state"""
    return 0

def event_m20_10_x79(z5=0, z6=210010001, val1=270, val2=290):
    """[Reproduction] Giant's memory time limit
    z5: Global timer ID
    z6: Time limit notification flag
    val1: Execution start time of the first phase process
    val2: Execution start time of the second phase process
    """
    """State 0,1: Timer start judgment"""
    if (GetGlobalTimerTime(z5) > val2) != 0:
        """State 5: Restart global timer_3"""
        RestartGlobalTimer(z5)
        """State 6: Time limit notification flag ON"""
        SetEventFlag(z6, 1)
        """State 9: From the third phase"""
        return 2
    elif (GetGlobalTimerTime(z5) > val1) != 0:
        """State 4: Restart global timer_2"""
        RestartGlobalTimer(z5)
        """State 8: From the second phase"""
        return 1
    elif (GetGlobalTimerTime(z5) > 1) != 0:
        """State 3: Restart global timer"""
        RestartGlobalTimer(z5)
        """State 7: From the first phase"""
        return 0
    else:
        """State 2: Starting the global timer"""
        StartGlobalTimer(z5)
        """State 10: From the 0th phase"""
        return 3

def event_m20_10_x80(z5=0, val1=270, action1=2012):
    """[Conditions & Execution] Giant's Memory Time Limit_First Phase
    z5: Global timer ID
    val1: Execution start time of the first phase process
    action1: Text ID to display in the first phase
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z5, val1, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2012:"The ashen mist has thinned..."
    DisplayEventMessage(action1, 0, 0, 0)
    """State 3: End state"""
    return 0

def event_m20_10_x81(z5=0, val2=290, z6=210010001):
    """[Conditions & Execution] Giant's Memory Time Limit _ Second Phase
    z5: Global timer ID
    val2: Execution start time of the second phase process
    z6: Time limit notification flag
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z5, val2, 3)
    assert ConditionGroup(0)
    """State 2: Time limit notification flag ON"""
    SetEventFlag(z6, 1)
    """State 3: End state"""
    return 0

def event_m20_10_x82(z5=0, z7=300, action2=2013, z8=_):
    """[Conditions & Execution] Giant's Memory Time Limit_3rd Phase
    z5: Global timer ID
    z7: Execution start time of the third phase process
    action2: Text ID to display in the third phase
    z8: Return Warp Point ID
    """
    """State 0,1: Wait for time limit"""
    CompareGlobalTimer(0, z5, z7, 3)
    assert ConditionGroup(0)
    """State 2: Event message display"""
    # action:2013:"The ashen mist fades..."
    DisplayEventMessage(action2, 0, 0, 0)
    """State 3: Return to Giant Tree"""
    PlayCutsceneAndWarpToMap(0, 0, 10100000, z8, 0)
    """State 4: End state"""
    return 0

def event_m20_10_x83(z32=20101050):
    """[Reproduction] Stone statue
    z32: Gorokuro head OBJ instance ID
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(210000081) != 0:
        """State 5: Defeated"""
        return 1
    else:
        """State 2: Initialize related OBJ"""
        InitializeObj(z32)
        InitializeObj(20102352)
        InitializeObj(20102359)
        InitializeObj(20102313)
        assert (CompareObjStateId(20102352, 10, 0) and CompareObjStateId(20102313, 10, 0) and CompareObjStateId(z32,
                10, 0))
        """State 3: Navimesh attribute added"""
        AddNavimeshAttribute(1802000, 2)
        AddNavimeshAttribute(1902000, 2)
        """State 4: Not defeated"""
        return 0

def event_m20_10_x84(z30=300000, z31=300000):
    """[Condition] Head of stone statue
    z30: Start point ID
    z31: End point ID
    """
    """State 0,1: Are you within the specified area?"""
    IsPlayerInsidePoint(0, z30, z31, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x85(z29=20103680, mode2=0, z32=20101050):
    """[Execution] Stone statue
    z29: Fireball Damipoli OBJ instance ID
    mode2: Cool time
    z32: Gorokuro head OBJ instance ID
    """
    """State 0,2: Cool time state"""
    assert (GetStateTime() > mode2) != 0
    """State 1: Fireball fire"""
    ChangeObjState(z29, 70)
    """State 3: Fire ball landing waiting time"""
    assert (GetStateTime() > 5.6) != 0
    """State 4: Is the stone statue in its initial state?"""
    if CompareObjStateId(z32, 10, 0):
        """State 5: Gorogoro start: 70"""
        ChangeObjState(z32, 70)
    else:
        pass
    """State 6: End state"""
    return 0

def event_m20_10_x86(z29=20103680, mode2=0, z30=300000, z31=300000, z32=20101050):
    """[Preset] Stone statue
    z29: Damipoli OBJ instance ID for fireball
    mode2: Cool time
    z30: Launch start point ID
    z31: Firing end point ID
    z32: Gorokuro head OBJ instance ID
    """
    """State 0,1: [Reproduction] Head of stone statue _SubState"""
    call = event_m20_10_x83(z32=z32)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Stone Statue Head Gorokuro_SubState"""
        assert event_m20_10_x84(z30=z30, z31=z31)
        """State 2: [Execution] Head of stone statue _SubState"""
        assert event_m20_10_x85(z29=z29, mode2=mode2, z32=z32)
    """State 4: End state"""
    return 0

def event_m20_10_x87():
    """[Reproduction] Front fireball launch _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x88():
    """[Condition] Front fireball fire _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x89(z26=_, z27=_, z28=_):
    """[Execution] Front fireball launch
    z26: Fireball Damipoli OBJ instance ID
    z27: Wait time
    z28: Cool time
    """
    """State 0,2: Wait time"""
    CompareStateTime(0, z27, 2, z27)
    assert ConditionGroup(0)
    """State 1: Fireball fire"""
    ChangeObjState(z26, 75)
    """State 3: Cool time"""
    CompareStateTime(0, z28, 2, z28)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_10_x90(z26=_, z27=_, z28=_):
    """[Preset] Front fireball launch
    z26: Fireball Damipoli OBJ instance ID
    z27: Wait time
    z28: Cool time
    """
    """State 0,1: [Reproduction] Front fireball fire_sky_SubState"""
    assert event_m20_10_x87()
    """State 3: [Condition] Front fireball fire_Sky_SubState"""
    assert event_m20_10_x88()
    """State 2: [Execution] Fireball fire front_SubState"""
    assert event_m20_10_x89(z26=z26, z27=z27, z28=z28)
    """State 4: End state"""
    return 0

def event_m20_10_x91():
    """[Reproduction] Front fireball _ Launch management _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x92(z21=200000, z22=200000, z23=210020080):
    """[Condition] Front fireball_Launch management
    z21: Front_start point ID
    z22: Near_end point ID
    z23: Fireball launch switch flag
    """
    """State 0,1: Branch judgment"""
    IsPlayerInsidePoint(0, z21, z22, 1)
    CompareEventFlag(1, z23, 1)
    if ConditionGroup(1):
        """State 3: Boss battle started"""
        return 1
    elif ConditionGroup(0):
        """State 2: This point"""
        return 0

def event_m20_10_x93(z24=_, flag3=_):
    """[Execution] Front fireball_Launch management
    z24: External event ID
    flag3: Fireball management flag
    """
    """State 0,1: External event execution"""
    ExecuteEvent(z24)
    """State 3: Fireball management flag OFF"""
    SetEventFlag(flag3, 0)
    assert GetEventFlag(flag3) != 1
    """State 2: Wait for re-judgment"""
    CompareEventFlag(0, flag3, 1)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m20_10_x94(z21=200000, z22=200000, z23=210020080, z24=2012, z25=2013, flag3=210020040, flag4=210020050):
    """[Preset] Front fireball _ Launch management
    z21: Start point ID
    z22: End point ID
    z23: Fireball launch switch flag
    z24: External event ID_initial
    z25: External event ID_boss
    flag3: Fireball management flag_initial
    flag4: Fireball management flag_Boss
    """
    """State 0,1: [Reproduction] Front fireball_Launch management_Sky_SubState"""
    assert event_m20_10_x91()
    """State 3: [Condition] Front fireball_Launch management_SubState"""
    call = event_m20_10_x92(z21=z21, z22=z22, z23=z23)
    if call.Get() == 1:
        """State 4: [Execution] Front fireball_Launch management_2_SubState"""
        assert event_m20_10_x93(z24=z25, flag3=flag4)
    elif call.Get() == 0:
        """State 2: [Execution] Front fireball_Launch management_SubState"""
        assert event_m20_10_x93(z24=z24, flag3=flag3)
    """State 5: End state"""
    return 0

def event_m20_10_x95(z19=800000, z20=800000):
    """[Condition] Giant King Battle_Start
    z19: Start point ID
    z20: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z19, z20, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z19, z20, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_10_x96(z15=101, z17=210020080, z16=2010000):
    """[Execution] HP display, BGM playback and boss activation
    z15: Sound ID
    z17: Logic flag
    z16: Boss Battle ID
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z17, 1)
    """State 4: Did the boss die before showing?"""
    IsEventBossKill(0, z16, 0, 1)
    if ConditionGroup(0):
        pass
    else:
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z15)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 5: End state"""
    return 0

def event_m20_10_x97():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m20_10_x98(flag2=210000081, z14=30, z15=101, z16=2010000, z17=210020080, z18=800, z19=800000,
                     mode1=0):
    """[Preset] New Giant Senior Soldier (Living) _Boss Battle
    flag2: Boss destruction flag
    z14: Boss gauge display start distance
    z15: Sound ID
    z16: Boss Battle ID
    z17: Other flags for logic
    z18: Generator ID
    z19: Point ID
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Giant King Battle_Start_SubState"""
    call = event_m20_10_x72(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Battle of Giant Kings_Start_SubState"""
        assert event_m20_10_x95(z19=z19, z20=z19)
        """State 3: [Execution] Giant King Battle_Start_SubState"""
        assert event_m20_10_x74(z16=z16)
        """State 7: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
        assert event_m20_10_x97()
        """State 9: [Condition] HP display, BGM playback and boss activation_SubState"""
        assert event_m20_10_x73(z14=z14, z18=z18)
        """State 8: [Execution] HP display, BGM playback and boss activation_SubState"""
        assert event_m20_10_x96(z15=z15, z17=z17, z16=z16)
        """State 2: [Reproduction] Giant King Battle_End_Sky_SubState"""
        assert event_m20_10_x75()
        """State 6: [Condition] Giant King Battle_End Judgment_SubState"""
        assert event_m20_10_x76(z16=z16)
        """State 4: [Execution] Giant King Battle_End_SubState"""
        assert event_m20_10_x77(z15=z15, z16=z16, z17=z17, mode1=mode1)
    """State 10: End state"""
    return 0

def event_m20_10_x99(z11=20101100):
    """[Condition] Trap with flying blades
    z11: Bug ID OBJ instance ID
    """
    """State 0,1: Waiting for activation of insect key"""
    CompareObjState(0, z11, 20, 0)
    assert ConditionGroup(0)
    """State 2: Bug key activation"""
    return 0

def event_m20_10_x100(z5=0, z9=5, action3=2011):
    """[Conditions & Execution] Giant's Memory Time Limit_0th Phase
    z5: Global timer ID
    z9: Execution start time of the 0th phase process
    action3: Text ID displayed in the 0th phase
    """
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 3: Wait for a certain time"""
    CompareStateTime(0, z9, 3, z9)
    assert ConditionGroup(0)
    """State 1: Event message display"""
    # action:2011:"One cannot reside within memory for long"
    DisplayEventMessage(action3, 0, 0, 0)
    """State 4: End state"""
    return 0

def event_m20_10_x101(z1=_, lot1=60004000):
    """[Execution] Return from Giant's dead body
    z1: Giant corpse OBJ instance ID
    lot1: Lottery ID for item acquisition
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z1, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z1, 10, 0)
    assert ConditionGroup(0)
    """State 3: Acquisition failure window display"""
    # lot:60004000:Soul of a Giant
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 4: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 5: End state"""
    return 0

def event_m20_10_111162():
    """NPC: Kingdom Captain: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_10_x1(z98=104110, z99=20104000, z100=32, z101=7240)
    Quit()

def event_m20_10_111163():
    """NPC: Kingdom Captain: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7240:Captain Drummond
    event_m20_10_x4(z93=210010160, z94=210020161, z95=104110, z96=20104000, z97=111162, npc1=7240)
    Quit()

def event_m20_10_111164():
    """NPC: Kingdom Captain: White Phantom Sign Display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General Purpose: Generation Stop_SubState"""
    event_m20_10_x36(z52=102302, z53=657, z54=656, z55=104110, z56=103610)
    Quit()

def event_m20_10_111242():
    """NPC: Moonlight Jun: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m20_10_x1(z98=104164, z99=20104100, z100=61, z101=7430)
    Quit()

def event_m20_10_111243():
    """NPC: Moonlight Jun: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7430:Benhart of Jugo
    event_m20_10_x4(z93=210010100, z94=210020101, z95=104160, z96=20104100, z97=111242, npc1=7430)
    Quit()

def event_m20_10_111244():
    """NPC: Moonlight Jun: Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m20_10_x5(z91=60, z92=104164)
    Quit()

def event_m20_10_111245():
    """NPC: Moonlight Jun: Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m20_10_x6(z86=104160, z87=102423, z88=0, z89=210020107, z90=103663)
    Quit()

def event_m20_10_111246():
    """NPC: Satoshi Tsutsumi: White phantom sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General Purpose: Generation Stop_SubState"""
    event_m20_10_x36(z52=102432, z53=656, z54=657, z55=104160, z56=103660)
    Quit()

def event_m20_10_111247():
    """NPC: Satoshi Tsutsumi: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m20_10_x26(z68=210000081, z69=102436, z70=205, z71=7430)
    Quit()

def event_m20_10_120110():
    """Trophy: Moonlight Sword"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_10_x35(flag6=210020108, z57=31)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m20_10_120120():
    """Trophy: Fort Guardian"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_10_x35(flag6=210020167, z57=32)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

