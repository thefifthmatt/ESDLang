# -*- coding: utf-8 -*-
def event_m50_36_1000():
    """Operate the facility"""
    """State 0,3: [Preset] _SubState to operate the facility"""
    call = event_m50_36_x116(z189=50363040)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_1020():
    """Facility operation direction"""
    """State 0,2: [Preset] Facility Operation Direction_SubState"""
    assert event_m50_36_x232(z79=50363040, z80=50361500, z81=50361510, z82=50363100)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_2000():
    """Lattice opening with lever_1"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z208=50361021, z209=50362000, z210=200000, z211=9)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_2010():
    """Lattice opening with lever_2"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z208=50361022, z209=50362010, z210=201000, z211=8)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_2020():
    """Lattice opening with lever_3"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z208=50361023, z209=50362020, z210=202000, z211=8.5)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_2030():
    """Opening with a lever_4"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z208=50361028, z209=50362040, z210=203000, z211=8)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_2040():
    """Opening with a lever_5"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z208=50361026, z209=50362030, z210=204000, z211=7.5)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_3000():
    """Get a firestick"""
    """State 0,3: [Preset] _SubState to get a sashimi stick"""
    # lot:60014000:Scorching Iron Scepter, goods:53100000:Scorching Iron Scepter
    call = event_m50_36_x220(z88=50367900, lot1=60014000, z89=536000024, goods1=53100000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_3020():
    """The fire of the other tower disappears"""
    """State 0,2: [Preset] The fire of another tower disappears_SubState"""
    assert event_m50_36_x268(z45=536000024, z46=3020, z47=50360060)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_3030():
    """The furnace in the other tower stops"""
    """State 0,2: [Preset] Furnace in another tower stops_SubState"""
    assert event_m50_36_x276(z39=536000024, z40=50361530, z41=50360040, z42=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_3040():
    """The light of the other tower disappears"""
    """State 0,2: [Preset] The light of the other tower disappears_SubState"""
    assert event_m50_36_x280(z36=536000024, z37=1, z38=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_3050():
    """Debate start of another tower"""
    """State 0,2: [Preset] Debut activation of another tower_SubState"""
    assert event_m50_36_x295(z13=536020023, z14=536000024, z15=305000, z16=305002)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_3060():
    """Change the filter of another tower"""
    """State 0,2: [Preset] Change filter of another tower_SubState"""
    assert event_m50_36_x306(z3=306000, z4=306000, val1=14)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_4000():
    """A treasure when the mountain of ash is destroyed_1"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362800, z217=50368000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4010():
    """Treasure when the mountain of ash is destroyed_2"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362801, z217=50368010)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4020():
    """Treasure _3"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362802, z217=50368020)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4030():
    """Treasure _4"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362803, z217=50368030)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4040():
    """Treasure _5"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362804, z217=50368040)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4050():
    """Treasure _6"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362805, z217=50368050)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4060():
    """Treasure _7"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362806, z217=50368060)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4070():
    """Treasure _8"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362807, z217=50368070)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4080():
    """Treasure _9"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z216=50362808, z217=50368080)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5000():
    """Destroying a spider statue"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361109, z149=536000049, z150=50368590, z151=33, z152=93, z153=43,
                             z154=33, z155=500000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_5010():
    """Smoke damage caused by a spear image_Isolated island"""
    """State 0,2: [Preset] Smoke damage caused by a spear image_Isolated Island_SubState"""
    assert event_m50_36_x128(z180=536000049)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5200():
    """煤 Wet Strengthening_Isolated Island_Ax A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2811, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5210():
    """煤 Wet Strengthening_Isolated Island_Ax B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2820, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5220():
    """煤 Wet Strengthening_Isolated Island_Ax C"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2821, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5230():
    """煤 Wet Strengthening_Isolated Island_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2800, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5240():
    """煤 Wet Strengthening_Isolated Island_Ax E"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2801, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5250():
    """煤 Wet Strengthening_Isolated Island_Ax F"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2810, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5280():
    """煤 Wet Strengthening_Isolated Island_Ax I"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2822, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5300():
    """煤 Wet Strengthening_Isolated Island_Smoke Spirit A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2830, z120=96560310, z121=96560210, z122=96560410,
            z123=96560000, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_5310():
    """煤 Wet Strengthening_Isolated Island_Smoke Spirit B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000049, z119=2805, z120=96560310, z121=96560210, z122=96560410,
            z123=96560000, z124=50361109))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_6000():
    """Destroying a spear statue_Lobby"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361108, z149=536000048, z150=50368580, z151=34, z152=94, z153=44,
                             z154=34, z155=600000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_6010():
    """Smoke damage caused by a spear statue_Lobby"""
    """State 0,2: Operate the facility"""
    assert event_m50_36_x131(z179=536000048)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_6020():
    """Smoke filter change by sculpture"""
    """State 0,3: [Preset] Smoke filter change by Subaru image_SubState"""
    call = event_m50_36_x135(z173=536000049, z174=536000048, z175=20, z176=30, val9=14, val10=15, z177=22,
                             z178=32)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_6030():
    """Smoke fog and light changes by the eagle statue"""
    """State 0,3: [Preset] Smoke fog and light change by the image of a spider _SubState"""
    call = event_m50_36_x228(z83=536000049, z84=536000048, z85=22, z86=32, val2=14, val3=15)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_6100():
    """煤 Wet Strengthening_Lobby_Ax A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000048, z119=2900, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361108))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_6110():
    """煤 Wet Strengthening_Lobby_Ax B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000048, z119=2901, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361108))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_6130():
    """煤 Wet Strengthening_Lobby_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000048, z119=2911, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361108))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_6140():
    """煤 Wet Strengthening_Lobby_Ax E"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000048, z119=2912, z120=96560300, z121=96560200, z122=96560400,
            z123=96560100, z124=50361108))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_6210():
    """煤 Wet Strengthening_Lobby_Smoke Spirit B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z118=536000048, z119=2920, z120=96560310, z121=96560210, z122=96560410,
            z123=96560000, z124=50361108))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_7000():
    """Large door opened by lever_upper layer"""
    """State 0,2: [Preset] Large door opened by lever_Enemy activation_SubState"""
    assert event_m50_36_x253(z60=50361024, z61=50360410, z62=700000, z63=536000027)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_7010():
    """Large door opened with lever_Multiple tower"""
    """State 0,2: [Preset] Large door opened with lever_SubState"""
    assert event_m50_36_x98(z205=50361025, z206=50360411, z207=701000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_7020():
    """Large door opened with lever_Paka floor area"""
    """State 0,2: [Preset] Large door opened with lever_SubState"""
    assert event_m50_36_x98(z205=50361027, z206=50360412, z207=702000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_8000():
    """One-way door_Beside the fire room"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _2_SubState"""
    assert event_m50_36_x2(z299=0, z300=1101, z301=800000, z302=536000030)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_8010():
    """One-way door_Paka floor area"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_36_x2(z299=0, z300=1101, z301=801000, z302=536000032)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_8011():
    """OBJ blocking a one-way door"""
    """State 0,2: [Preset] OBJ_SubState that blocks a one-way door"""
    assert event_m50_36_x177(z131=50363090, z132=536000032)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_9010():
    """Change navigation with Salamander Defeat_2"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z43=7500, z44=901000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_9020():
    """Change navigation with Salamander Defeat_3"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z43=7502, z44=902000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_9030():
    """Change navigation by destroying salamander_4"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z43=7503, z44=903000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_9070():
    """Change navigation with Salamander Defeat_8"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z43=7603, z44=907000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_10000():
    """Elevator_in front of boss"""
    """State 0,1: Has the initialization event been completed?"""
    assert EventEnded(10030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z273=50361300, z274=1000000, z275=1000010, z276=50361040, z277=50361041)
    """State 2: Rerun"""
    RestartMachine()

def event_m50_36_10010():
    """Elevator_Before boss_Lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361300, z291=50361040, z292=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_10020():
    """Elevator_Before boss_Lever bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361300, z291=50361041, z292=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_10030():
    """Elevator_Before Boss_Initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m50_36_x23(z286=50361300, z287=40, z288=536000012, z289=40)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_12000():
    """Elevator_Start"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z273=50361320, z274=1200000, z275=1200010, z276=50361050, z277=50361051)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_12010():
    """Elevator_Start_Lever top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361320, z291=50361050, z292=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_12020():
    """Elevator_Start_Lever bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361320, z291=50361051, z292=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_13000():
    """Elevator_Termination of break route"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z273=50361019, z274=1300000, z275=1300010, z276=50361060, z277=50361061)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_13010():
    """Elevator_Termination of split route_Lever top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361019, z291=50361060, z292=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_13020():
    """Elevator_Termination of dividing route_Under lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361019, z291=50361061, z292=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_14000():
    """Elevator_Separate tower"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(14030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z273=50361330, z274=1400000, z275=1400010, z276=50361081, z277=50361080)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_14010():
    """Elevator_Another tower_Lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361330, z291=50361081, z292=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_14020():
    """Elevator_Another tower_Under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z290=50361330, z291=50361080, z292=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_14030():
    """Elevator_separate tower_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m50_36_x23(z286=50361330, z287=40, z288=536000013, z289=40)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_14040():
    """Elevator_Another tower_Navigation switching"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(14030) != 0
    """State 3: [Navigation switching of preset elevators_SubState"""
    assert event_m50_36_x284(z32=50361330, z33=1404000, z34=1404010)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_15010():
    """Unraveling the curse of the bride ’s soul"""
    """State 0,2: [Preset] _SubState to unlock the curse of the bride ’s soul"""
    assert event_m50_36_x176(z133=536000026, z134=5, z135=5)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_16000():
    """Hidden door navigation mesh change_outer wall"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z278=50362210, z279=20, z280=1600000, z281=0, z282=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_16010():
    """Hidden door navigation mesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z278=50362211, z279=20, z280=1601000, z281=0, z282=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_17000():
    """C root key: memory"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_36_x1(z303=1005, z304=1105, z305=52400000, z306=536000036)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_17010():
    """C root key door: Split"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_36_x1(z303=1005, z304=1105, z305=52400000, z306=536000038)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_17020():
    """Lobby key door"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_36_x1(z303=1005, z304=1105, z305=52400000, z306=536000034)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_18000():
    """Enemy jumping out of Haishan_1"""
    """State 0,2: [Preset] Enemy _SubState jumping out of Ashyama"""
    assert event_m50_36_x310(z1=536020065, z2=1800000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_18010():
    """Enemy jumping out of Haizan_2"""
    """State 0,2: [Preset] Enemy _SubState jumping out of Ashyama"""
    assert event_m50_36_x310(z1=536020066, z2=1801000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_19000():
    """Continuous intrusion"""
    """State 0,2: [Preset] Continuous intrusion_SubState"""
    assert event_m50_36_x141(z51=536020004, z52=536020005, z53=536020006, z54=536020007, z55=536020008)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_19010():
    """Continuous intrusion_termination"""
    """State 0,2: [Preset] Continuous intrusion_End_SubState"""
    assert event_m50_36_x145(z157=7000, z158=7001, z159=7002, z160=7003, z161=7004, z162=536000001)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_20000():
    """Boss: Black Smoke Knight"""
    """State 0,2: [Preset] Black Smoke Knight Battle_Start_SubState"""
    assert (event_m50_36_x206(z90=536000081, z91=501, z92=5036000, z93=536020080, z94=6.3, z95=10, z96=5036001,
            z97=536020083))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_20010():
    """The crown that appears when you destroy a boss"""
    """State 0,3: [Preset] Crown _SubState that appears when a boss is destroyed"""
    # action:5310:"A faint heat lingers in the ancient crown"
    call = event_m50_36_x181(z25=50363080, z26=536000020, z27=5, action1=5310, z28=50360080)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_20050():
    """NPC Gesture Management_Black Smoke Knight"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_36_x299(z10=536000081, z11=903, z12=536020084)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_21000():
    """Boss behavior change with Verstad equipment"""
    """State 0,3: [Preset] Boss behavior change with Verstad equipment_SubState"""
    call = event_m50_36_x157(z144=536020082, z145=536000081)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_22000():
    """Destroyed sculpture _ left boss room _ front"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361101, z149=536000041, z150=50368510, z151=33, z152=93, z153=43,
                             z154=33, z155=2200000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_22010():
    """Destroying a spear statue_Boss room left_Back"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361102, z149=536000042, z150=50368520, z151=34, z152=94, z153=44,
                             z154=34, z155=2201000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_22020():
    """Destroying a spider statue"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361103, z149=536000043, z150=50368530, z151=33, z152=93, z153=43,
                             z154=33, z155=2202000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_22030():
    """Destroying a spider statue_Boss room right_Back"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361104, z149=536000044, z150=50368540, z151=34, z152=94, z153=44,
                             z154=34, z155=2203000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_22100():
    """煤 Wet Strengthening_Multiple Versions_Ax A"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z5=4610, z6=96560300, z7=96560200, z8=96560400, z9=96560100)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_22110():
    """煤 Wet strengthening_Multiple images_Ax B"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z5=4611, z6=96560300, z7=96560200, z8=96560400, z9=96560100)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_22200():
    """煤 Wet enhancement_Multiple images_Cow A"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z5=4700, z6=96560320, z7=96560220, z8=96560420, z9=96560110)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_22210():
    """煤 Wet strengthening_Multiple images_Cow B"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z5=4800, z6=96560320, z7=96560220, z8=96560420, z9=96560110)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_22300():
    """煤 Wet Enhancement_Multiple Images_Smoke Spirit A"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z5=4600, z6=96560310, z7=96560210, z8=96560410, z9=96560000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_22310():
    """煤 Wet Enhancement_Multiple Images_Smoke Spirit B"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z5=4601, z6=96560310, z7=96560210, z8=96560410, z9=96560000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_23000():
    """Recovery sphere with spear image _ Boss room left _ front"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361101, z284=150, z285=50361453)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(z136=536000041, z137=50361453)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_23010():
    """Recovery sphere with a spear image _ Boss room left _ back"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361102, z284=150, z285=50361454)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(z136=536000042, z137=50361454)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_23020():
    """Recovery sphere with sculpture statue _ boss room right _ front"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361103, z284=150, z285=50361452)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(z136=536000043, z137=50361452)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_23030():
    """Recovery sphere with a spear image _ Boss room right _ back"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361104, z284=150, z285=50361451)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(z136=536000044, z137=50361451)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_25000():
    """Boss: Demon Knight Kai_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m50_36_x3(z293=536000091, z294=2500000, z295=2500000, z296=503, z297=5036020, z298=536020090,
            mode5=0))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_25010():
    """Flame linked to the Demon Knight Kai action"""
    """State 0,2: [Preset] Flame_SubState linked to Demon Knight Kai action"""
    assert (event_m50_36_x99(z197=905, z198=71, z199=70, z200=50362200, z201=50362201, z202=93050011,
            z203=536000091))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_25050():
    """NPC Gesture Management_Demon Knight Kai"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_36_x299(z10=536000091, z11=905, z12=536020094)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_28000():
    """Boss: Oriental Knight_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m50_36_x3(z293=536000086, z294=2800000, z295=2800000, z296=502, z297=5036010, z298=536020085,
            mode5=0))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_28010():
    """Toyo knight's hunger judgment"""
    """State 0,2: [Preset] Toyo knight's gut determination_SubState"""
    assert event_m50_36_x288(z29=536000086, z30=536020087, z31=5036010)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_28050():
    """NPC Gesture Management_Toyo Knight"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_36_x299(z10=536000086, z11=904, z12=536020089)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_30000():
    """Two pairs of spinning fire bulls"""
    """State 0,2: [Preset] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m50_36_x79(z215=50361200)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_30010():
    """Two pairs of rotating fire-blowing cows_attach_1"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361200, z284=150, z285=50361210)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_30020():
    """Two pairs of rotating fire-blowing cows_attach_2"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361200, z284=151, z285=50361211)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_31000():
    """Sliding fire-blowing cattle"""
    """State 0,2: [Preset] sliding fire-blowing cow_initialized version_SubState"""
    assert (event_m50_36_x123(z181=50361220, z182=30, z183=32, z184=70, z185=72, z186=3100000, z187=3100010,
            z188=3100020))
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_31010():
    """Sliding fire-blowing cow _ Thorn wall side A_ attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361220, z284=150, z285=50361230)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_32000():
    """Sliding fire-sprayed cow_Kenzawayama 1F"""
    """State 0,2: [Preset] Sliding fire-blowing cow_Initialized version_Kenzawayama 1F_SubState"""
    assert event_m50_36_x197(z111=50361221, z112=30, z113=32, z114=70, z115=72, z116=3200000, z117=3200020)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_32010():
    """Sliding fire beef_Kenzawayama 1F_Attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361221, z284=150, z285=50361231)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_33000():
    """Sliding fire-sprayed cow_Kenzawa 2F"""
    """State 0,2: [Preset] sliding fire-blowing cow_initialized version_Kenzawa 2F_SubState"""
    assert event_m50_36_x198(z104=50361222, z105=40, z106=42, z107=80, z108=82, z109=3300020, z110=3300000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_33010():
    """Sliding fire beef_Kenzawa 2F_Attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361222, z284=150, z285=50361232)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_34000():
    """Sliding fire-blowing cow _ thorn wall side B"""
    """State 0,2: [Preset] sliding fire-blowing cow_initialized version_SubState"""
    assert (event_m50_36_x123(z181=50361260, z182=40, z183=42, z184=80, z185=82, z186=3400000, z187=3400010,
            z188=3400020))
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_34010():
    """Sliding fire-blowing cow _ Thorn wall side B_ attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361260, z284=150, z285=50361250)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_37000():
    """The image of a half-broken spear collapses"""
    """State 0,2: [Preset] The image of a half-broken spear collapses"""
    assert event_m50_36_x264(z48=50368800, z49=50361130, z50=3700000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38000():
    """Destruction variable reset of eagle statue"""
    """State 0,2: [Preset] Destruction variable reset of the spider image_SubState"""
    assert event_m50_36_x240(z73=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38010():
    """Judgment of the number of spears"""
    """State 0,2: [Preset] Judgment of the number of spears_SubState"""
    assert event_m50_36_x248(z64=1, z65=10, z66=536000039, z67=11, z68=536000059, z69=100710)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38100():
    """Addition of destructive variables for sculpture _Zakobos ①"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000040, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38110():
    """Addition of destructive variable for sculpture statue"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000041, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38120():
    """Addition of destructive variable of sculpture statue_Boss room left_Back"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000042, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38130():
    """Addition of destructive variable for sculpture statue"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000043, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38140():
    """Addition of destruction variable of sculpture statue_Boss room right_Back"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000044, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38160():
    """Addition of destructive variable of sculpture statue_Boss room_Zakobos ②"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000046, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38170():
    """Addition of destructive variable of sculpture statue_Boss room_Throne"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000047, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38180():
    """Addition of destructive variable of sculpture statue_Boss room_Lobby"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000048, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38190():
    """Addition of destruction variable of sculpture statue_Boss room_Isolated island"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000049, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38200():
    """Addition of destructive variables for sculpture _ Boss Room _ Airy"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000050, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_38210():
    """Addition of destructive variable of sculpture statue_boss room_top"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z70=38000, z71=536000051, z72=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_39000():
    """Destroy the spider statue_top"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361111, z149=536000051, z150=50368610, z151=30, z152=91, z153=41,
                             z154=31, z155=3900000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_39010():
    """Dark storm from the statue of a spider"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361111, z284=150, z285=50361611)
    """State 2: [Preset] Dark storm _SubState"""
    assert event_m50_36_x236(z74=536000051, z75=50361611, z76=50361111, z77=91, z78=31)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_40000():
    """Opened with a lever"""
    """State 0,2: [Preset] Continuous iron grids open with lever _7 versions_SubState"""
    assert event_m50_36_x163(z142=50361075, mode3=0, z143=536020016, val6=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_40010():
    """7 continuous iron grid version changes"""
    """State 0,2: [Preset] 7 continuous iron grid editions_Navigation change_SubState"""
    assert event_m50_36_x204(z103=536020017)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_41000():
    """Opened with a lever"""
    """State 0,2: [Preset] Continuous iron grids open with levers_9 versions_SubState"""
    assert event_m50_36_x164(z140=50361076, mode2=0, z141=536020018, val5=3.5)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_41010():
    """Nine continuous bar grid version change"""
    """State 0,2: [Preset] Nine continuous iron grid version_Navigation change_SubState"""
    assert event_m50_36_x205(z102=536020019)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_42000():
    """After the 7th edition of the spitting salamander statue"""
    """State 0,3: [Preset] Salamander image _SubState spitting fire"""
    call = event_m50_36_x168(z138=50362050, z139=50362250)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_42010():
    """After the 9th edition of the spitting salamander statue"""
    """State 0,3: [Preset] Salamander image _SubState spitting fire"""
    call = event_m50_36_x168(z138=50362060, z139=50362251)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_43000():
    """Destroying the statue of the fox"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361100, z149=536000040, z150=50368500, z151=33, z152=93, z153=43,
                             z154=33, z155=4300000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_43010():
    """Activating the Samurai Statue_Zakobos ①"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361100, z284=150, z285=50361150)
    """State 2: [Preset] Activating the frog image_SubState"""
    assert event_m50_36_x188(z125=536000040, z126=50361100, z127=5, z128=50361150, z129=4301000, z130=4301000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_43100():
    """煤 Wet Strengthening_Zakobos ①_Ax A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z118=536000040, z119=1300, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361100))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_43110():
    """煤 Wet Strengthening_Zakobos ①_Ax B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z118=536000040, z119=1310, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361100))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_43120():
    """煤 Wet Strengthening_Zakobos ①_Ax C"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z118=536000040, z119=1330, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361100))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_43130():
    """煤 Wet Strengthening_Zakobos ①_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z118=536000040, z119=1331, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361100))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_43140():
    """煤 Wet Strengthening_Zakobos ①_Ax E"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z118=536000040, z119=1332, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361100))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_43150():
    """煤 Wet Strengthening_Zakobos ①_Ax F"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z118=536000040, z119=1301, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361100))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_44000():
    """Destroying a spider image_Zakobos ②"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361106, z149=536000046, z150=50368560, z151=34, z152=94, z153=44,
                             z154=34, z155=4400000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_44010():
    """Activating the Samurai Statue_Zakobos ②"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361106, z284=150, z285=50361156)
    """State 2: [Preset] Activating the frog image_SubState"""
    assert event_m50_36_x188(z125=536000046, z126=50361106, z127=5, z128=50361156, z129=4401000, z130=4401000)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_44020():
    """Dark storm from the statue of a spider Zakobos ②"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361106, z284=150, z285=50361606)
    """State 3: [Preset] Dark storm caused by the image of a spider _Zakobos ②_SubState"""
    assert (event_m50_36_x291(z17=536000046, z18=50361606, z19=50361106, z20=94, z21=34, z22=2121, z23=2124,
            z24=2130))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_44130():
    """煤 Wet Strengthening_Zakobos②_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z118=536000046, z119=2121, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361106))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_44160():
    """煤 Wet Strengthening_Zakobos②_AxG"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z118=536000046, z119=2124, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361106))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_44170():
    """煤 Wet Strengthening_Zakobos②_Ax H"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z118=536000046, z119=2120, z120=96560300, z121=96560200,
            z122=96560400, z123=96560100, z124=50361106))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_44200():
    """煤 Wet Strengthening_Zakobos②_Cow A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z118=536000046, z119=2130, z120=96560320, z121=96560220,
            z122=96560420, z123=96560110, z124=50361106))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_45000():
    """Destroy the eagle statue in front of the throne"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361107, z149=536000047, z150=50368570, z151=33, z152=93, z153=43,
                             z154=33, z155=4500000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_45010():
    """Healing sphere with a spear image_in front of the throne"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361107, z284=150, z285=50361456)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(z136=536000047, z137=50361456)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_46000():
    """Destroy the eagle statue_Eiley"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z148=50361110, z149=536000050, z150=50368600, z151=34, z152=94, z153=44,
                             z154=34, z155=4600000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_46020():
    """Healing sphere with a spear image_Irie"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z283=50361110, z284=150, z285=50361455)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(z136=536000050, z137=50361455)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_47000():
    """Wall broken by explosion_Thorn wall side A_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z278=50362125, z279=20, z280=4700000, z281=0, z282=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_47010():
    """Wall broken by explosion_Thorn wall side B_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z278=50362126, z279=20, z280=4701000, z281=0, z282=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_47020():
    """Wall broken by explosion_swords"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z278=50362127, z279=20, z280=4702000, z281=0, z282=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_48010():
    """_B"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z87=50362401)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_48020():
    """_C"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z87=50362402)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_48030():
    """Ignite the corpse_D"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z87=50362403)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_48040():
    """_E"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z87=50362404)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_48050():
    """Fire a corpse_F"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z87=50362405)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_48060():
    """_G"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z87=50362406)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_49000():
    """Disabling damage"""
    """State 0,1: PC: Disabling enemy recovery effect with spear image"""
    SetDamageImmunityByCharacterId(100, 320050000, 1)
    SetDamageImmunityByCharacterId(100, 320050100, 1)
    SetDamageImmunityByCharacterId(100, 320050200, 1)
    """State 3: White Spirit: Invalidate enemy recovery effect with spear image"""
    SetDamageImmunityByGeneratorId(740, 320050000, 1)
    SetDamageImmunityByGeneratorId(740, 320050100, 1)
    SetDamageImmunityByGeneratorId(740, 320050200, 1)
    SetDamageImmunityByGeneratorId(741, 320050000, 1)
    SetDamageImmunityByGeneratorId(741, 320050100, 1)
    SetDamageImmunityByGeneratorId(741, 320050200, 1)
    """State 4: Zako: Disabling dark storms caused by spider statues"""
    SetDamageImmunityByCharacterId(650000, 320080030, 1)
    SetDamageImmunityByCharacterId(650000, 320080031, 1)
    SetDamageImmunityByCharacterId(650000, 320080040, 1)
    SetDamageImmunityByCharacterId(653000, 320080030, 1)
    SetDamageImmunityByCharacterId(653000, 320080031, 1)
    SetDamageImmunityByCharacterId(653000, 320080040, 1)
    SetDamageImmunityByCharacterId(653006, 320080030, 1)
    SetDamageImmunityByCharacterId(653006, 320080031, 1)
    SetDamageImmunityByCharacterId(653006, 320080040, 1)
    SetDamageImmunityByCharacterId(653010, 320080030, 1)
    SetDamageImmunityByCharacterId(653010, 320080031, 1)
    SetDamageImmunityByCharacterId(653010, 320080040, 1)
    SetDamageImmunityByCharacterId(653020, 320080030, 1)
    SetDamageImmunityByCharacterId(653020, 320080031, 1)
    SetDamageImmunityByCharacterId(653020, 320080040, 1)
    SetDamageImmunityByCharacterId(653029, 320080030, 1)
    SetDamageImmunityByCharacterId(653029, 320080031, 1)
    SetDamageImmunityByCharacterId(653029, 320080040, 1)
    SetDamageImmunityByCharacterId(656000, 320080030, 1)
    SetDamageImmunityByCharacterId(656000, 320080031, 1)
    SetDamageImmunityByCharacterId(656000, 320080040, 1)
    SetDamageImmunityByCharacterId(873000, 320080030, 1)
    SetDamageImmunityByCharacterId(873000, 320080031, 1)
    SetDamageImmunityByCharacterId(873000, 320080040, 1)
    SetDamageImmunityByGeneratorId(977, 320080030, 1)
    SetDamageImmunityByGeneratorId(977, 320080031, 1)
    SetDamageImmunityByGeneratorId(977, 320080040, 1)
    """State 5: Zako: Disable cursed smoke damage"""
    SetDamageImmunityByCharacterId(653000, 320030000, 1)
    SetDamageImmunityByCharacterId(653002, 320030000, 1)
    SetDamageImmunityByCharacterId(653010, 320030000, 1)
    SetDamageImmunityByCharacterId(653011, 320030000, 1)
    SetDamageImmunityByCharacterId(653020, 320030000, 1)
    SetDamageImmunityByCharacterId(653021, 320030000, 1)
    SetDamageImmunityByCharacterId(656000, 320030000, 1)
    SetDamageImmunityByCharacterId(871000, 320030000, 1)
    SetDamageImmunityByCharacterId(873000, 320030000, 1)
    SetDamageImmunityByGeneratorId(977, 320030000, 1)
    """State 2: Finish"""
    EndMachine()

def event_m50_36_50000():
    """Door that opens with DLC purchase"""
    """State 0,3: [Preset] Door that opens with DLC purchase_SubState"""
    call = event_m50_36_x82(z212=50360400, z213=5000000, z214=5000010)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_36_51000():
    """Start from molten iron castle"""
    """State 0,1: Finish"""
    EndMachine()

def event_m50_36_52000():
    """Return to molten iron castle"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m50_36_x48(z252=50363010, z253=10190000, z254=5200000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_36_53000():
    """Invade the memory of the ancient king"""
    """State 0,3: [Preset] Invade the memory of the old king_SubState"""
    call = event_m50_36_x109(z191=50363060, z192=503610, z193=0, z194=50360000, z195=5300000, z196=101061)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_54000():
    """Return from the memory of the ancient king"""
    """State 0,3: [Preset] Return from the Memory of the Old King_Item Available_SubState"""
    # lot:60013000:Smelter Wedge, goods:53200000:Smelter Wedge
    call = event_m50_36_x66(z218=50363030, lot2=60013000, z219=536000022, goods2=53200000, z220=0, z221=0,
                            z222=5400000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_36_55000():
    """Time limit of memory of the ancient king"""
    """State 0,2: [Preset] Old King's memory time limit_SubState"""
    # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
    assert (event_m50_36_x110(z169=4, z170=0, val7=1050, val8=1070, z171=1080, action2=2012, action3=2013,
            z172=5400000))
    """State 1: Finish"""
    EndMachine()

def event_m50_36_59000():
    """Clear inter-DLC event_C route division"""
    """State 0,2: [Preset] Inter-DLC event_C route clear_SubState"""
    assert event_m50_36_x257(z58=101063, z59=100711)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_59010():
    """Clear DLC event_C route memory"""
    """State 0,2: [Preset] Inter-DLC event_C route clear_SubState"""
    assert event_m50_36_x257(z58=101062, z59=100712)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_80000():
    """Fireworks for regeneration 01_Start point_36650"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z270=5036000, z271=5036099)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_81000():
    """Regenerative fire 02_Facility operation OBJ Square_36655"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z270=5036100, z271=5036199)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_82000():
    """Rebirth Fire 03_Midroom Room_36660"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z270=5036200, z271=5036299)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_83000():
    """Reproduction of fire 04_divided route_36665"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z270=5036300, z271=5036399)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_84000():
    """Rebirth Fire 05_Before Boss Route_36670"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z270=5036400, z271=5036499)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_85000():
    """Rebirth Fire 06_Before the Flame (Memory) Route_36675"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z270=5036500, z271=5036599)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_89000():
    """Shop lineup expansion_Knight of black smoke"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_36_x50(z250=101061, z251=101211)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_89010():
    """Shop lineup expansion_Toyo Knight"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_36_x50(z250=101062, z251=101212)
    """State 1: Finish"""
    EndMachine()

def event_m50_36_100000():
    """White Spirit 01: Carion"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m50_36_x41(z255=102722, z256=740, z257=104300, z258=103800, z259=-1)

def event_m50_36_x0(z192=_, z193=0, z194=_, z172=_):
    """[Lib] Warp between maps after poly play
    z192: Pre-warp poly play ID
    z193: Poly Play ID after Warp
    z194: Map ID
    z172: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z192, z193, z194, z172, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m50_36_x1(z303=1005, z304=1105, z305=52400000, z306=_):
    """[Lib] Item specified door unlocking_2
    z303: Text ID when opened
    z304: Text ID when not opened
    z305: item
    z306: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z305, z303, z304, z306, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x2(z299=0, z300=1101, z301=_, z302=_):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z299: Text ID when opened
    z300: Text ID when not opened
    z301: Point ID
    z302: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z301, 0, z299, z300, z302, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x3(z293=_, z294=_, z295=_, z296=_, z297=_, z298=_, mode5=0):
    """[Lib] [Preset] Boss Battle Start
    z293: Boss destruction flag
    z294: Start point ID
    z295: End point ID
    z296: Sound ID
    z297: Boss Battle ID
    z298: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m50_36_x4(z293=z293)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m50_36_x5(z294=z294, z295=z295)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m50_36_x6(z296=z296, z297=z297, z298=z298)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m50_36_x7()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m50_36_x8(z297=z297)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m50_36_x9(z296=z296, z297=z297, z298=z298, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m50_36_x4(z293=_):
    """[Reproduction] Boss Battle_Start
    z293: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z293) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_36_x5(z294=_, z295=_):
    """[Condition] Boss Battle_Start
    z294: Start point ID
    z295: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z294, z295, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z294, z295, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x6(z296=_, z297=_, z298=_):
    """[Execution] Boss Battle_Start
    z296: Sound ID
    z297: Boss Battle ID
    z298: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z296)
    """State 1: Boss battle start notification"""
    StartBossFight(z297)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z298, 1)
    """State 4: End state"""
    return 0

def event_m50_36_x7():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x8(z297=_):
    """[Condition] Boss Battle_End Judgment
    z297: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z297, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x9(z296=_, z297=_, z298=_, mode5=0):
    """[Execute] Boss Battle_End
    z296: Sound ID
    z297: Boss Battle ID
    z298: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z298, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z297)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z296)
    """State 5: End state"""
    return 0

def event_m50_36_100010():
    """White Spirit 02"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z272=741)

def event_m50_36_x10(z273=_, z274=_, z275=_, z276=_, z277=_):
    """[Lib] [Preset] Elevator
    z273: OBJ instance ID of the elevator
    z274: On elevator point ID_
    z275: Elevator point ID_below
    z276: Upper lever OBJ instance ID
    z277: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m50_36_x11()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m50_36_x12(z273=z273, z274=z274, z275=z275, z276=z276, z277=z277)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m50_36_x33(z273=z273, z275=z275)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m50_36_x32(z273=z273, z274=z274)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m50_36_x13(z273=z273, z274=z274)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m50_36_x14(z273=z273, z275=z275)
    """State 7: End state"""
    return 0

def event_m50_36_x11():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x12(z273=_, z274=_, z275=_, z276=_, z277=_):
    """[Condition] Elevator
    z273: Elevator OBJ instance ID
    z274: On elevator point ID_
    z275: Elevator point ID_below
    z276: Upper lever OBJ instance ID
    z277: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z273, 10, 0)
    CompareObjState(1, z273, 40, 0)
    CompareObjState(2, z273, 80, 0)
    CompareObjState(2, z273, 41, 0)
    CompareObjState(3, z273, 70, 0)
    CompareObjState(3, z273, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z275, z275, 1)
        CompareObjState(0, z276, 74, 0)
        CompareObjState(0, z276, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z274, z274, 1)
        CompareObjState(0, z277, 74, 0)
        CompareObjState(0, z277, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m50_36_x13(z273=_, z274=_):
    """[Execution] Elevator_Rise
    z273: Elevator OBJ instance ID
    z274: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z273, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z273, 30, 0)
    IsPlayerInsidePoint(8, z274, z274, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z273, 71)
    assert CompareObjStateId(z273, 40, 0)
    """State 4: End state"""
    return 0

def event_m50_36_x14(z273=_, z275=_):
    """[Execution] Elevator_Descent
    z273: Elevator OBJ instance ID
    z275: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z273, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z273, 41, 0)
    IsPlayerInsidePoint(8, z275, z275, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z273, 81)
    assert CompareObjStateId(z273, 10, 0)
    """State 4: End state"""
    return 0

def event_m50_36_x15(z290=_, z291=_, z292=_):
    """[Lib] [Preset] Elevator lever
    z290: OBJ instance ID of the elevator
    z291: Lever OBJ instance ID
    z292: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m50_36_x16()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m50_36_x17(z290=z290, z291=z291, z292=z292)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m50_36_x18(z290=z290, z291=z291, z292=z292)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m50_36_x19(z290=z290, z291=z291, z292=z292)
    """State 5: Rerun"""
    return 0

def event_m50_36_x16():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x17(z290=_, z291=_, z292=_):
    """[Condition] Elevator lever_use judgment
    z290: OBJ instance ID of the elevator
    z291: Lever OBJ instance ID
    z292: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z290, z292, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m50_36_x18(z290=_, z291=_, z292=_):
    """[Execution] Elevator lever_Key guide valid
    z290: OBJ instance ID of the elevator
    z291: Lever OBJ instance ID
    z292: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z291, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z290, z292, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x19(z290=_, z291=_, z292=_):
    """[Execute] Elevator lever_key guide disabled
    z290: OBJ instance ID of the elevator
    z291: Lever OBJ instance ID
    z292: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z291, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z290, z292, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_100020():
    """White Spirit 03"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z272=742)

def event_m50_36_x20(z288=_):
    """[Lib] [Reproduction] Elevator_Initialization
    z288: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(z288) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m50_36_x21():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_36_x22(z286=_, z287=40, z288=_, z289=40):
    """[Lib] [Execution] Elevator_Initialization
    z286: Elevator OBJ instance ID
    z287: Initial position OBJ state ID
    z288: Initialization completion flag
    z289: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z286, z287)
    assert CompareObjStateId(z286, z289, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z288, 1)
    """State 3: End state"""
    return 0

def event_m50_36_x23(z286=_, z287=40, z288=_, z289=40):
    """[Lib] [Preset] Elevator_Initialization
    z286: Elevator OBJ instance ID
    z287: Initial position OBJ state ID
    z288: Initialization completion flag
    z289: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m50_36_x20(z288=z288)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m50_36_x21()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m50_36_x22(z286=z286, z287=z287, z288=z288, z289=z289)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m50_36_x24():
    """[Lib] [Reproduction] OBJ attach_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x25():
    """[Lib] [Condition] OBJ attach_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x26(z283=_, z284=_, z285=_):
    """[Lib] [execute] OBJ attach
    z283: Parent OBJ instance ID
    z284: Parent Damipoli ID
    z285: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z283, z284, z285)
    """State 2: End state"""
    return 0

def event_m50_36_x27(z283=_, z284=_, z285=_):
    """[Lib] [Preset] OBJ attach
    z283: Parent OBJ instance ID
    z284: Parent Damipoli ID
    z285: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m50_36_x24()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m50_36_x25()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m50_36_x26(z283=z283, z284=z284, z285=z285)
    """State 4: End state"""
    return 0

def event_m50_36_x28(z278=_, z279=20, z280=_, z281=0, z282=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z278: Object instance ID
    z279: OBJ state ID
    z280: Navimesh switching point ID
    z281: Additional attributes
    z282: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m50_36_x29(z278=z278, z279=z279, z280=z280, z282=z282, z281=z281)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m50_36_x30(z278=z278, z279=z279, z280=z280)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m50_36_x31(z278=z278, z279=z279, z280=z280, z281=z281, z282=z282)
    """State 4: End state"""
    return 0

def event_m50_36_x29(z278=_, z279=20, z280=_, z282=2, z281=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z278: Target OBJ instance ID
    z279: Target OBJ state ID
    z280: Navimesh switching point ID
    z282: Additional attributes
    z281: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z278, z279, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z280, z282)
        DeleteNavimeshAttribute(z280, z281)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m50_36_100030():
    """White Spirit 04"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z272=743)

def event_m50_36_x30(z278=_, z279=20, z280=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z278: Target OBJ instance ID
    z279: Target OBJ state ID
    z280: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z278, z279, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x31(z278=_, z279=20, z280=_, z281=0, z282=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z278: Target OBJ instance ID
    z279: Target OBJ state ID
    z280: Navimesh switching point ID
    z281: Additional attributes
    z282: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z280, z281)
    DeleteNavimeshAttribute(z280, z282)
    """State 2: End state"""
    return 0

def event_m50_36_x32(z273=_, z274=_):
    """[Execution] Elevator_Return switch after lift
    z273: Elevator OBJ instance ID
    z274: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z273, 30, 0)
    IsPlayerInsidePoint(8, z274, z274, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z273, 71)
    assert CompareObjStateId(z273, 40, 0)
    """State 3: End state"""
    return 0

def event_m50_36_x33(z273=_, z275=_):
    """[Execution] Elevator_Return switch after descending
    z273: Elevator OBJ instance ID
    z275: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z273, 41, 0)
    IsPlayerInsidePoint(8, z275, z275, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z273, 81)
    assert CompareObjStateId(z273, 10, 0)
    """State 3: End state"""
    return 0

def event_m50_36_x34(z272=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z272: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z272)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m50_36_x35():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x36(z270=_, z271=_):
    """[Lib] [execute] Rebirth fire
    z270: Flag start ID
    z271: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z270, z271, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x37():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x38(z270=_, z271=_):
    """[Lib] [Preset] Rebirth
    z270: Flag start ID
    z271: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m50_36_x35()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m50_36_x37()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m50_36_x36(z270=z270, z271=z271)
    """State 4: End state"""
    return 0

def event_m50_36_x39(z264=100601, z265=10000010, z266=731, z267=104480, z268=0, z269=0):
    """[Lib] NPC Black Phantom Appearance: Online
    z264: Summoning conditions: Global event flag
    z265: Summon range
    z266: Generator ID
    z267: Death: Global event flag
    z268: Appearance: Minimum time
    z269: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z267, 1)
        CompareEventFlag(8, z264, 1)
        IsPlayerInsidePoint(8, z265, z265, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z267, 1)
            CompareStateTime(1, z268, 3, z269)
            IsPlayerInsidePoint(2, z265, z265, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z266)
                HasNpcPhantomSpawned(0, z266, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_36_100040():
    """White Spirit 05"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z272=744)

def event_m50_36_x40(z260=10000000, z261=730, z262=0, z263=0.2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z260: Summon range
    z261: Generator ID
    z262: Appearance: Minimum time
    z263: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z260, z260, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z262, 3, z263)
        IsPlayerInsidePoint(1, z260, z260, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z261)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_36_x41(z255=102722, z256=740, z257=104300, z258=103800, z259=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z255: White Phantom can appear: Global event flag
    z256: White Phantom: Generator ID
    z257: Death: Global event flag
    z258: Hostile: Global event flag
    z259: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z256)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z257, 1)
        CompareEventFlag(1, z258, 1)
        CompareEventFlag(2, z255, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z256)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z257, 1)
            CompareEventFlag(1, z258, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z256)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z257, 1)
            CompareEventFlag(1, z258, 1)
            HasNpcPhantomSpawned(2, z256, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z256, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z256)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m50_36_x42(z251=_):
    """[Lib] [Reproduction] Shop Lineup
    z251: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(z251) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m50_36_x43(z251=_):
    """[Lib] [execution] shop lineup
    z251: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(z251, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x44(z252=50363010):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z252)
    """State 2: End state"""
    return 0

def event_m50_36_x45(z252=50363010):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z252, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z252)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m50_36_x46(z252=50363010, z253=10190000, z254=5200000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    z253: Map ID
    z254: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z252, 1)
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
        assert event_m50_36_x0(z192=0, z193=0, z194=z253, z172=z254)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m50_36_x47(z252=50363010):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z252: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z252, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x48(z252=50363010, z253=10190000, z254=5200000):
    """[Lib] [Preset] Warp move between main part and DLC
    z252: Warp OBJ instance ID
    z253: Map ID
    z254: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m50_36_x44(z252=z252)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m50_36_x45(z252=z252)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m50_36_x47(z252=z252)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m50_36_x46(z252=z252, z253=z253, z254=z254)
    """State 5: End state"""
    return 0

def event_m50_36_x49(z250=_):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z250: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z250, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_100050():
    """White Spirit 06"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z272=745)

def event_m50_36_x50(z250=_, z251=_):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z250: Boss destruction flag
    z251: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m50_36_x42(z251=z251)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m50_36_x49(z250=z250)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m50_36_x43(z251=z251)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x51(z245=10000000, z246=730, z247=0, z248=0.2, z249=536020060):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON
    z245: Summon range
    z246: Generator ID
    z247: Appearance: Minimum time
    z248: Appearance: Maximum time
    z249: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z245, z245, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z247, 3, z248)
        IsPlayerInsidePoint(1, z245, z245, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z246)
            SetEventFlag(z249, 1)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_36_x52(z238=100601, z239=10000010, z240=731, z241=104480, z242=0, z243=0, z244=536020061):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online
    z238: Summoning conditions: Global event flag
    z239: Summon range
    z240: Generator ID
    z241: Death: Global event flag
    z242: Appearance: Minimum time
    z243: Appearance: Maximum time
    z244: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z241, 1)
        CompareEventFlag(8, z238, 1)
        IsPlayerInsidePoint(8, z239, z239, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z241, 1)
            CompareStateTime(1, z242, 3, z243)
            IsPlayerInsidePoint(2, z239, z239, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z240)
                SetEventFlag(z244, 1)
                HasNpcPhantomSpawned(0, z240, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_36_x53(z223=536020067, z225=536000068):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z223: Lottery determination flag
    z225: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z225) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z223) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m50_36_x54(z224=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z224: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z224, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m50_36_x55(z223=536020067, z226=3, z227=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z223: Lottery determination flag
    z226: Number of appearance judgment points
    z227: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z223, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z226)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z227, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m50_36_x56(z223=536020067, z224=14, z225=536000068, z226=3, z227=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z223: Lottery determination flag
    z224: Random number comparison value
    z225: Defeat flag
    z226: Number of appearance judgment points
    z227: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m50_36_x53(z223=z223, z225=z225)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m50_36_x54(z224=z224)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m50_36_x55(z223=z223, z226=z226, z227=z227)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m50_36_x65(z223=z223, z227=z227)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m50_36_x57(val11=_, z235=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val11: Appearance judgment number
    z235: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z235) == val11) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_36_x58(z231=_, z232=0, z233=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z231: Appearance judgment point ID
    z232: Minimum appearance time
    z233: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z231, z231, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z232, 3, z233)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_36_x59(z234=977, z236=_, z237=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z234: Generator ID
    z236: Appearance start point ID
    z237: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z234, z236, z237)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z234)
    """State 4: Finish"""
    return 0

def event_m50_36_x60(z228=536000068):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z228: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z228) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m50_36_x61(z231=_, z232=0, z233=5, z234=977, val11=_, z235=10, z236=_, z237=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z231: Intrusion detection point ID
    z232: Minimum appearance time
    z233: Maximum time to appear
    z234: Generator ID
    val11: Appearance judgment number
    z235: Lottery result point variable
    z236: Appearance start point ID
    z237: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m50_36_x57(val11=val11, z235=z235)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m50_36_x58(z231=z231, z232=z232, z233=z233)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m50_36_x59(z234=z234, z236=z236, z237=z237)
    """State 4: Finish"""
    return 0

def event_m50_36_x62(z229=977, mode4=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z229: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z229)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode4) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m50_36_x63(z228=536000068, z230=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z228: Defeat flag
    z230: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z228, 1)
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
                    SetEventFlag(z230, 1)
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

def event_m50_36_x64(z228=536000068, z229=977, mode4=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z228: Defeat flag
    z229: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m50_36_x60(z228=z228)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m50_36_x62(z229=z229, mode4=mode4)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m50_36_x63(z228=z228, z230=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m50_36_x63(z228=z228, z230=102755)
    """State 5: End state"""
    return 0

def event_m50_36_x65(z223=536020067, z227=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z223: Lottery determination flag
    z227: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z223, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z227, 0)
    """State 3: End state"""
    return 0

def event_m50_36_x66(z218=50363030, lot2=60013000, z219=536000022, goods2=53200000, z220=0, z221=0, z222=5400000):
    """[Preset] Return from the memory of the old king
    z218: OBJ instance ID
    lot2: Lottery ID for item acquisition
    z219: Item acquisition confirmation flag
    goods2: Acquisition judgment item ID
    z220: Pre-warp poly play ID
    z221: Poly Play ID after Warp
    z222: Point ID
    """
    """State 0,3: [Reproduction] Return from the memory of the ancient king_SubState"""
    call = event_m50_36_x69(z218=z218, z219=z219)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 4: [Condition] Return from old king's memory_SubState"""
    assert event_m50_36_x67(z218=z218, goods2=0)
    """State 2: [Execution] Return from the memory of the old king_SubState"""
    assert event_m50_36_x68(z218=z218, z220=z220, z221=z221, z222=z222)
    """State 7: End state"""
    return 0
    """State 1: [Condition] Return from the memory of the old king_Item acquisition_SubState"""
    Label('L0')
    call = event_m50_36_x67(z218=z218, goods2=goods2)
    if call.Get() == 0:
        """State 5: [Execution] Return from the memory of the old king_Item acquisition_SubState"""
        assert event_m50_36_x70(z218=z218, lot2=lot2, z219=z219)
    elif call.Get() == 1:
        """State 6: [Execution] Return from the memory of the old king_Item acquisition impossible_SubState"""
        assert event_m50_36_x71(z218=z218, lot2=lot2)
    """State 8: Rerun"""
    return 1

def event_m50_36_x67(z218=50363030, goods2=_):
    """[Condition] Warp to the memory of the ancient king
    z218: OBJ instance ID
    goods2: Item ID
    """
    """State 0,1: Have you examined OBJ?"""
    IsObjSearched(0, z218)
    assert ConditionGroup(0)
    """State 2: Can items be acquired?"""
    if CanGetItem(goods2, 1) != 0:
        """State 3: Available"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m50_36_x68(z218=50363030, z220=0, z221=0, z222=5400000):
    """[Execution] Warp to the memory of the ancient king
    z218: OBJ instance ID
    z220: Pre-warp poly play ID
    z221: Poly Play ID after Warp
    z222: Point ID
    """
    """State 0,4: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 1: Key guide disabled: 10"""
    ChangeObjState(z218, 10)
    """State 2: Wait for transition completion"""
    CompareObjState(0, z218, 10, 0)
    assert ConditionGroup(0)
    """State 3: End of global timer"""
    EndGlobalTimer(4)
    """State 6: [Lib] Warp between maps after poly play_SubState"""
    assert event_m50_36_x0(z192=z220, z193=z221, z194=50360000, z172=z222)
    """State 5: Multiplayer prohibited state: OFF"""
    ProhibitMultiplayer(0)
    """State 7: End state"""
    return 0

def event_m50_36_x69(z218=50363030, z219=536000022):
    """[Reproduction] Warp to the memory of the ancient king
    z218: OBJ instance ID
    z219: Item acquisition confirmation flag
    """
    """State 0,2: Key guide activation: 30"""
    ChangeObjState(z218, 30)
    """State 3: Wait for transition"""
    assert CompareObjStateId(z218, 30, 0)
    """State 1: Did you get the item?"""
    if GetEventFlag(z219) != 0:
        """State 5: It has been acquired"""
        return 1
    else:
        """State 4: Unacquired"""
        return 0

def event_m50_36_x70(z218=50363030, lot2=60013000, z219=536000022):
    """[Execution] Warp _ item acquisition to the memory of the ancient king
    z218: OBJ instance ID
    lot2: Lottery ID for item acquisition
    z219: Item acquisition confirmation flag
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z218, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z218, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60013000:Smelter Wedge
    AwardItem(lot2, 1)
    """State 4: Turn on the item acquisition flag"""
    SetEventFlag(z219, 1)
    SetEventFlag(100905, 1)
    """State 5: End state"""
    return 0

def event_m50_36_x71(z218=50363030, lot2=60013000):
    """[Execution] Warp to old king's memory
    z218: OBJ instance ID
    lot2: Lottery ID for item acquisition
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z218, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z218, 10, 0)
    assert ConditionGroup(0)
    """State 3: Acquisition failure window display"""
    # lot:60013000:Smelter Wedge
    DisplayItemAwardFailure(lot2, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 4: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 5: End state"""
    return 0

def event_m50_36_x72(z216=_, z217=_):
    """[Preset] Break the ash mountain and treasure
    z216: Instance ID of Haiyama OBJ
    z217: Treasure OBJ instance ID
    """
    """State 0,1: [Reproduction] Treasure _SubState when breaking the ash mountain"""
    call = event_m50_36_x73(z216=z216, z217=z217)
    if call.Get() == 0:
        """State 3: [Condition] Treasure _SubState when the ash mountain is destroyed"""
        assert event_m50_36_x74(z216=z216)
        """State 2: [Execution] Breaking the pile of ash treasure _SubState"""
        assert event_m50_36_x75(z217=z217)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x73(z216=_, z217=_):
    """[Reproduction] Treasure when the mountain of ash is broken
    z216: Instance ID of Haiyama OBJ
    z217: Treasure OBJ instance ID
    """
    """State 0,1: State determination of Haiyama OBJ"""
    if CompareObjStateId(z216, 20, 0):
        """State 4: Haiyama: destroyed"""
        return 1
    else:
        """State 2: Hide treasure"""
        ChangeDrawHit(z217, 0)
        """State 3: Haeyama: Undestructed"""
        return 0

def event_m50_36_x74(z216=_):
    """[Condition] Treasure when the mountain of ash is broken
    z216: Instance ID of Haiyama OBJ
    """
    """State 0,1: Did you destroy Haiyama OBJ?"""
    CompareObjState(0, z216, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x75(z217=_):
    """[Execution] Break the ash mountain and treasure
    z217: Treasure OBJ instance ID
    """
    """State 0,1: Treasure display"""
    ChangeDrawHit(z217, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x76(z215=50361200):
    """[Reproduction] Two pairs of rotating fire-blowing cows
    z215: Cow OBJ instance ID
    """
    """State 0,1: Judgment of fire-blown cow"""
    if CompareObjStateId(z215, 10, 1):
        """State 3,4: Waiting for stop"""
        assert CompareObjStateId(z215, 10, 0)
    else:
        pass
    """State 2,5: End state"""
    return 0

def event_m50_36_x77(z215=50361200):
    """[Conditions] Two pairs of rotating fired cows
    z215: Cow OBJ instance ID
    """
    """State 0,1: Damage judgment"""
    IsObjDamaged(0, z215, -1, -1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x78(z215=50361200):
    """[Execution] 2 pairs of fire-blowing cows rotating
    z215: Cow OBJ instance ID
    """
    """State 0,1: Rotating fire bull"""
    ChangeObjState(z215, 30)
    """State 2: Wait for rotation to end"""
    CompareObjState(0, z215, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x79(z215=50361200):
    """[Preset] Two pairs of fire-blowing cows that rotate
    z215: Cow OBJ instance ID
    """
    """State 0,1: [Reproduction] Two pairs of fire-blowing cows _SubState rotating"""
    assert event_m50_36_x76(z215=z215)
    """State 3: [Condition] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m50_36_x77(z215=z215)
    """State 2: [Execution] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m50_36_x78(z215=z215)
    """State 4: Rerun"""
    return 0

def event_m50_36_x80(z181=_, z184=_, z183=_, z186=_, z187=_, z188=_):
    """[Execution] A fire-blowing cow that slides
    z181: Cow OBJ instance ID
    z184: Mobile OBJ state ID
    z183: Movement end OBJ state ID
    z186: Before operation_Navigation change point ID
    z187: Active_Navigation change point ID
    z188: After operation_navi change point ID
    """
    """State 0,3: Navigation mesh change"""
    AddNavimeshAttribute(z186, 2)
    AddNavimeshAttribute(z187, 2)
    AddNavimeshAttribute(z188, 2)
    """State 1: Slide movement of fire-blown cow"""
    ChangeObjState(z181, z184)
    """State 2: Waiting for movement to end"""
    CompareObjState(0, z181, z183, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change_2"""
    DeleteNavimeshAttribute(z186, 2)
    DeleteNavimeshAttribute(z187, 2)
    AddNavimeshAttribute(z188, 2)
    """State 5: End state"""
    return 0

def event_m50_36_x81(z104=_):
    """[Conditions] Sliding fire-blown cow
    z104: Cow OBJ instance ID
    """
    """State 0,1: Damage judgment"""
    IsObjDamaged(0, z104, -1, -3, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x82(z212=50360400, z213=5000000, z214=5000010):
    """[Preset] Door that opens with DLC purchase
    z212: Door OBJ instance ID
    z213: Navigation switching point ID
    z214: Judgment point ID
    """
    """State 0,1: [Reproduction] Doors opened with DLC purchase_SubState"""
    call = event_m50_36_x83(z212=z212, z213=z213)
    if call.Get() == 0:
        """State 3: [Conditions] Doors opened by DLC purchase_SubState"""
        call = event_m50_36_x85(z212=z212, z214=z214)
        if call.Get() == 0:
            """State 6: [Execution] Door opened by DLC purchase_Manual_SubState"""
            assert event_m50_36_x88(z212=z212, z213=z213)
            Goto('L0')
        elif call.Get() == 2:
            """State 5: [Execution] Door opened with DLC purchase_Auto_SubState"""
            assert event_m50_36_x87(z212=z212, z213=z213)
            Goto('L0')
        elif call.Get() == 1:
            """State 7: [Execution] Door that opens with DLC purchase_No access_Front_SubState"""
            assert event_m50_36_x89(z212=z212)
        elif call.Get() == 3:
            """State 8: [Execution] Door opened with DLC purchase_No access_Back_SubState"""
            assert event_m50_36_x90(z212=z212)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Conditions] Doors opened by DLC purchase_Guest_SubState"""
        assert event_m50_36_x86(z212=z212)
        """State 2: [Execution] Door opened with DLC purchase_Guest_SubState"""
        assert event_m50_36_x84(z212=z212, z213=z213)
    """State 10: Finish"""
    Label('L0')
    return 1

def event_m50_36_x83(z212=50360400, z213=5000000):
    """[Reproduction] Door opened with DLC purchase
    z212: Door OBJ instance ID
    z213: Navigation switching point ID
    """
    """State 0,2: Navigation switching_initialization"""
    AddNavimeshAttribute(z213, 2)
    """State 1: Host?"""
    if IsGuest() != 1:
        """State 3: Safety: Door initialization"""
        InitializeObj(z212)
        assert CompareObjStateId(z212, 10, 0)
        """State 4: Disable key guide"""
        DisableObjKeyGuide(z212, 1)
        """State 5: Not passed"""
        return 0
    else:
        """State 6: The guests"""
        return 1

def event_m50_36_x84(z212=50360400, z213=5000000):
    """[Execution] Door opened with DLC purchase_Guest
    z212: King's door OBJ instance ID
    z213: Navigation switching point ID
    """
    """State 0,1: Change navigation"""
    DeleteNavimeshAttribute(z213, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x85(z212=50360400, z214=5000010):
    """[Conditions] Doors opened by DLC purchase
    z212: Door OBJ instance ID
    z214: Judgment point ID
    """
    """State 0,2: Distance judgment or point judgment"""
    CompareObjPlayerDistance(0, z212, 4, 5)
    SetConditionGroup(1, 8)
    IsPlayerInsidePoint(8, z214, z214, 1)
    IsHost(8, 1, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4,5: Player status determination_2"""
    CompareEventFlag(8, 100601, 1)
    CompareEventFlag(8, 100611, 1)
    # goods:52100000:Heavy Iron Key
    DoesPlayerHaveItem(8, 52100000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 8: Back: Allowed"""
        return 2
    else:
        """State 9: Back: No traffic"""
        return 3
    """State 3: Approach from the front"""
    Label('L0')
    """State 1: Player status determination"""
    CompareEventFlag(8, 100601, 1)
    CompareEventFlag(8, 100611, 1)
    # goods:52100000:Heavy Iron Key
    DoesPlayerHaveItem(8, 52100000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 6: Front: Allowed"""
        return 0
    else:
        """State 7: Front: No traffic"""
        return 1

def event_m50_36_x86(z212=50360400):
    """[Conditions] Doors opened with DLC purchase_Guest
    z212: Door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z212, 20, 0)
    assert ConditionGroup(0)
    """State 2: Mural opened"""
    return 0

def event_m50_36_x87(z212=50360400, z213=5000000):
    """[Execution] Door opened with DLC purchase_Auto
    z212: Door OBJ instance ID
    z213: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z212, 20)
    """State 2: Waiting for the door to finish"""
    CompareObjState(0, z212, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z213, 2)
    """State 4: End state"""
    return 0

def event_m50_36_x88(z212=50360400, z213=5000000):
    """[Execution] Door opened with DLC purchase_Manual
    z212: Door OBJ instance ID
    z213: Navigation switching point ID
    """
    """State 0,3: Activate key guide"""
    DisableObjKeyGuide(z212, 0)
    """State 1: Waiting for the door to finish"""
    CompareObjState(0, z212, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation switching"""
    DeleteNavimeshAttribute(z213, 2)
    """State 4: End state"""
    return 0

def event_m50_36_x89(z212=50360400):
    """[Execution] Door opened with DLC purchase
    z212: Door OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z212, 8, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x90(z212=50360400):
    """[Execution] Door opened with DLC purchase
    z212: Door OBJ instance ID
    """
    """State 0,3: Did you approach the door?"""
    CompareObjPlayerDistance(0, z212, 4, 5)
    assert ConditionGroup(0)
    """State 1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z212, 8, 3)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_36_x91(z209=_, z210=_):
    """[Reproduction] Iron lattice that opens with a lever
    z209: Iron lattice OBJ instance ID
    z210: Navigation change point ID
    """
    """State 0,1: Is the iron grid open?"""
    if CompareObjStateId(z209, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z209, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z210, 2)
        """State 6: Already in operation"""
        return 1
    else:
        """State 4: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z210, 2)
        """State 5: Not in operation"""
        return 0

def event_m50_36_x92(z208=_):
    """[Conditions] Iron grid that opens with lever
    z208: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z208, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x93(z209=_, z210=_, z211=_):
    """[Execution] Iron grid that opens with lever
    z209: Iron lattice OBJ instance ID
    z210: Navigation change point ID
    z211: Wait until navigation switching
    """
    """State 0,2: The iron bar opens: 70"""
    ChangeObjState(z209, 70)
    """State 4: weight"""
    CompareStateTime(0, z211, 3, z211)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z210, 2)
    """State 3: Waiting for the opening of the iron lattice"""
    CompareObjState(0, z209, 20, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m50_36_x94(z208=_, z209=_, z210=_, z211=_):
    """[Preset] Opening with a lever
    z208: Lever OBJ instance ID
    z209: Iron lattice OBJ instance ID
    z210: Navigation change point ID
    z211: Wait until navigation switching
    """
    """State 0,1: [Reproduction] Iron lattice _SubState opened with lever"""
    call = event_m50_36_x91(z209=z209, z210=z210)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Iron lattice that opens with lever_SubState"""
        assert event_m50_36_x92(z208=z208)
        """State 2: [Execution] Iron lattices opened by lever_SubState"""
        assert event_m50_36_x93(z209=z209, z210=z210, z211=z211)
    """State 4: End state"""
    return 0

def event_m50_36_x95(z206=_, z207=_):
    """[Reproduction] Large door opened by lever
    z206: Door OBJ instance ID
    z207: Navigation change point ID
    """
    """State 0,1: Is the big door open?"""
    if CompareObjStateId(z206, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z206, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z207, 2)
        """State 5: Already in operation"""
        return 1
    else:
        """State 4: Not in operation"""
        return 0

def event_m50_36_x96(z60=_):
    """[Conditions] Large door opened with lever
    z60: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z60, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x97(z206=_, z207=_):
    """[Execution] Large door opened by lever
    z206: Door OBJ instance ID
    z207: Navigation change point ID
    """
    """State 0,2: The big door opens: 70"""
    ChangeObjState(z206, 70)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z206, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z207, 2)
    """State 4: End state"""
    return 0

def event_m50_36_x98(z205=_, z206=_, z207=_):
    """[Preset] Large door opened by lever
    z205: Lever OBJ instance ID
    z206: Door OBJ instance ID
    z207: Navigation change point ID
    """
    """State 0,1: [Reproduction] Large door opened with lever_SubState"""
    call = event_m50_36_x95(z206=z206, z207=z207)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Large door opened with lever_SubState"""
        assert event_m50_36_x96(z60=z205)
        """State 2: [Execution] Large door opened with lever_SubState"""
        assert event_m50_36_x97(z206=z206, z207=z207)
    """State 4: End state"""
    return 0

def event_m50_36_x99(z197=905, z198=71, z199=70, z200=50362200, z201=50362201, z202=93050011, z203=536000091):
    """[Preset] Flame linked to the Demon Knight Kai action
    z197: Boss generator ID
    z198: State ID with stone statue on
    z199: State ID with stone statue flame OFF
    z200: OBJ instance ID of stone statue 1
    z201: OBJ instance ID of stone statue 2
    z202: Boss special state effect ID
    z203: Boss destruction flag
    """
    """State 0,1: [Reproduction] Flame _SubState linked to Demon Knight Kai action"""
    call = event_m50_36_x100(z203=z203)
    if call.Get() == 0:
        """State 3: [Condition] Flame linked to the Demon Knight Kai action_Boss goes to "anger" state_SubState"""
        call = event_m50_36_x101(z197=z197, z202=z202)
        if call.Get() == 0:
            """State 2: [Execution] Flame linked to Demon Knight Kai action_Lights off_SubState"""
            assert event_m50_36_x103(z199=z199, z200=z200, z201=z201, z204=30)
            """State 4: [Condition] Flame linked to Demon Knight Kai action_Boss dies_SubState"""
            assert event_m50_36_x102(z197=z197)
            """State 5: [Execution] Flame_Lit_SubState linked to Demon Knight Kai action"""
            assert event_m50_36_x103(z199=z198, z200=z200, z201=z201, z204=10)
        elif call.Get() == 1:
            pass
    elif call.Get() == 1:
        pass
    """State 6: Finish"""
    return 0

def event_m50_36_100100():
    """Dark Spirit 01"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_36_x51(z245=10000000, z246=730, z247=0, z248=0.2, z249=536020060)

def event_m50_36_x100(z203=536000091):
    """[Reproduction] Flame linked to Demon Knight Kai action
    z203: Boss destruction flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z203) != 1:
        """State 2: Undefeated"""
        return 0
    else:
        """State 3: Defeated"""
        return 1

def event_m50_36_x101(z197=905, z202=93050011):
    """[Conditions] Flame_Boss linked to Demon Knight Kai's action is in "anger" state
    z197: Boss generator ID
    z202: Boss special state effect ID
    """
    """State 0,1: Boss status judgment"""
    ChrHasSpEffect(0, z197, z202, 1)
    IsChrDead(1, z197)
    if ConditionGroup(0):
        """State 2: Turn off due to status change"""
        return 0
    elif ConditionGroup(1):
        """State 3: Boss death"""
        return 1

def event_m50_36_x102(z197=905):
    """[Condition] Flame boss dies in conjunction with Demon Knight Kai action
    z197: Boss generator ID
    """
    """State 0,1: Boss status judgment"""
    IsChrDead(0, z197)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x103(z199=_, z200=50362200, z201=50362201, z204=_):
    """[Execution] Flame linked to Demon Knight Kai action
    z199: OBJ state ID for ON / OFF
    z200: OBJ instance ID of stone statue 1
    z201: OBJ instance ID of stone statue 2
    z204: ON / OFF completion confirmation OBJ state ID
    """
    """State 0,1: OBJ status change"""
    ChangeObjState(z200, z199)
    ChangeObjState(z201, z199)
    """State 2: Has the OBJ status change been completed?"""
    CompareObjState(8, z200, z204, 0)
    CompareObjState(8, z201, z204, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m50_36_x104(z191=50363060, z196=101061):
    """[Reproduction] Invading the memory of the ancient king
    z191: OBJ instance ID to check
    z196: Boss destruction flag
    """
    """State 0,4: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Are you destroying a smoke knight?"""
    if GetEventFlag(z196) != 0:
        """State 3: SFX generation: 40"""
        ChangeObjState(z191, 40)
    else:
        pass
    """State 1: Disable key guide"""
    DisableObjKeyGuide(z191, 1)
    """State 5: End state"""
    return 0
    """State 6: The guests"""
    Label('L0')
    return 1

def event_m50_36_x105(z191=50363060, z196=101061):
    """[Condition] Invade the memory of the ancient king
    z191: OBJ instance ID to check
    z196: Boss destruction flag
    """
    """State 0,1: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z191, 0)
    """State 2: Did you investigate OBJ or became multi or destroyed boss?"""
    IsObjSearched(0, z191)
    IsMultiplayer(1, 1, 1)
    CompareEventFlag(2, z196, 1)
    if ConditionGroup(2):
        """State 5: SFX generation: 40"""
        ChangeObjState(z191, 40)
        """State 6: Was OBJ checked or multi?"""
        IsObjSearched(0, z191)
        IsMultiplayer(1, 1, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 4: Do you have an ash mist core? Are you destroying a smoke knight?"""
            Label('L0')
            # goods:50910000:Ashen Mist Heart
            DoesPlayerHaveItem(8, 50910000, 1, 3, 1, 1, 0)
            CompareEventFlag(8, z196, 1)
            if ConditionGroup(8):
                """State 7: Warp execution"""
                return 0
            else:
                """State 9: Nothing happens"""
                return 2
    elif ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 8: Key guide disabled"""
    return 1

def event_m50_36_x106(z191=50363060, z192=503610, z193=0, z194=50360000, z195=5300000):
    """[Execution] Invade the memory of the ancient king
    z191: OBJ instance ID to check
    z192: Pre-warp poly play ID
    z193: Poly Play ID after Warp
    z194: Map ID
    z195: Point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z191, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: Timer reset for time limit"""
    EndGlobalTimer(4)
    """State 5: [Lib] Warp between maps after poly play_SubState"""
    assert event_m50_36_x0(z192=z192, z193=z193, z194=z194, z172=z195)
    """State 4: Multiplayer prohibited state: OFF"""
    ProhibitMultiplayer(0)
    """State 6: End state"""
    return 0

def event_m50_36_x107(z191=50363060):
    """[Execution] Invasion of old king's memory
    z191: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z191, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x108():
    """[Execution] Intrusion into the memory of the ancient king _ Nothing happens"""
    """State 0,1: Message display"""
    # action:1113:"Alas, nothing happened"
    DisplayOwnOkMenu(1113, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m50_36_x109(z191=50363060, z192=503610, z193=0, z194=50360000, z195=5300000, z196=101061):
    """[Preset] Invade the memory of the ancient king
    z191: OBJ instance ID to check
    z192: Pre-warp poly play ID
    z193: Poly Play ID after Warp
    z194: Map ID
    z195: Point ID
    z196: Boss destruction flag
    """
    """State 0,1: [Reproduction] Intrusion into the memory of the ancient king_SubState"""
    call = event_m50_36_x104(z191=z191, z196=z196)
    if call.Get() == 0:
        """State 5: [Condition] Invade the memory of the old king_SubState"""
        call = event_m50_36_x105(z191=z191, z196=z196)
        if call.Get() == 1:
            """State 3: [Execution] Intrusion into the memory of the old king_Disable Key Guide_SubState"""
            assert event_m50_36_x107(z191=z191)
        elif call.Get() == 2:
            """State 4: [Execution] Intrusion into the memory of the old king _Nothing happens_SubState"""
            assert event_m50_36_x108()
        elif call.Get() == 0:
            """State 2: [Execution] Intrusion into the memory of the ancient king_SubState"""
            assert event_m50_36_x106(z191=z191, z192=z192, z193=z193, z194=z194, z195=z195)
            Goto('L0')
        """State 6: Rerun"""
        return 0
    elif call.Get() == 1:
        pass
    """State 7: Finish"""
    Label('L0')
    return 1

def event_m50_36_100110():
    """Dark Spirit 02: Poverty Warrior"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online_SubState"""
    event_m50_36_x52(z238=100601, z239=10000010, z240=731, z241=104480, z242=0, z243=0, z244=536020061)

def event_m50_36_x110(z169=4, z170=0, val7=1050, val8=1070, z171=1080, action2=2012, action3=2013, z172=5400000):
    """[Preset] Memory time limit of the ancient king
    z169: Global timer ID
    z170: Time limit notification flag
    val7: Execution start time of the first phase process
    val8: Execution start time of the second phase process
    z171: Execution start time of the third phase process
    action2: Text ID to display in the first phase
    action3: Text ID to display in the third phase
    z172: Return Warp Point ID
    """
    """State 0,12: [Reproduction] Time limit of memory of the old king_Start judgment_SubState"""
    call = event_m50_36_x136()
    if call.Get() == 0:
        """State 14: [Condition] Memory time limit_start judgment_SubState"""
        assert event_m50_36_x137()
        """State 13: [Execution] Memory time limit of old king_Start judgment_Empty_SubState"""
        assert event_m50_36_x138()
        """State 1: [Reproduction] Memory time limit of the ancient king_SubState"""
        call = event_m50_36_x111(z169=z169, z170=z170, val7=val7, val8=val8)
        if call.Get() == 3:
            """State 8: [Conditions & Execution] Memory time limit of old king_0th phase_SubState"""
            # action:2011:"One cannot reside within memory for long"
            assert event_m50_36_x112(z169=z169, z190=5, action4=2011)
            """State 2: [Conditions & Execution] Memory time limit of the old king_First Phase_SubState"""
            assert event_m50_36_x113(z169=z169, val7=val7, action2=action2)
            """State 3: [Conditions & Execution] Memory time limit of old king_Second Phase_SubState"""
            assert event_m50_36_x114(z169=z169, val8=val8, z170=z170)
            """State 4: [Conditions & Execution] Memory time limit of the ancient king_3rd phase_SubState"""
            assert event_m50_36_x115(z169=z169, z171=z171, action3=action3, z172=z172)
        elif call.Get() == 0:
            """State 9: [Conditions & Execution] Memory time limit of the ancient king_First Phase_2_SubState"""
            assert event_m50_36_x113(z169=z169, val7=val7, action2=action2)
            """State 5: [Conditions & Execution] Memory time limit of old king_Second Phase_2_SubState"""
            assert event_m50_36_x114(z169=z169, val8=val8, z170=z170)
            """State 6: [Conditions & Execution] Memory time limit of the ancient king_3rd phase_2_SubState"""
            assert event_m50_36_x115(z169=z169, z171=z171, action3=action3, z172=z172)
        elif call.Get() == 1:
            """State 10: [Conditions & Execution] Memory time limit of the ancient king_Second Phase_3_SubState"""
            assert event_m50_36_x114(z169=z169, val8=val8, z170=z170)
            """State 7: [Conditions & Execution] Memory time limit of the ancient king_3rd phase_3_SubState"""
            assert event_m50_36_x115(z169=z169, z171=z171, action3=action3, z172=z172)
        elif call.Get() == 2:
            """State 11: [Conditions & Execution] Memory time limit of old king_3rd phase_4_SubState"""
            assert event_m50_36_x115(z169=z169, z171=z171, action3=action3, z172=z172)
    elif call.Get() == 1:
        pass
    """State 15: End state"""
    return 0

def event_m50_36_x111(z169=4, z170=0, val7=1050, val8=1070):
    """[Reproduction] Time limit of memory of the ancient king
    z169: Global timer ID
    z170: Time limit notification flag
    val7: Execution start time of the first phase process
    val8: Execution start time of the second phase process
    """
    """State 0,1: Timer start judgment"""
    if (GetGlobalTimerTime(z169) > val8) != 0:
        """State 5: Restart global timer_3"""
        RestartGlobalTimer(z169)
        """State 6: Time limit notification flag ON"""
        SetEventFlag(z170, 1)
        """State 9: From the third phase"""
        return 2
    elif (GetGlobalTimerTime(z169) > val7) != 0:
        """State 4: Restart global timer_2"""
        RestartGlobalTimer(z169)
        """State 8: From the second phase"""
        return 1
    elif (GetGlobalTimerTime(z169) > 1) != 0:
        """State 3: Restart global timer"""
        RestartGlobalTimer(z169)
        """State 7: From the first phase"""
        return 0
    else:
        """State 2: Starting the global timer"""
        StartGlobalTimer(z169)
        """State 10: From the 0th phase"""
        return 3

def event_m50_36_x112(z169=4, z190=5, action4=2011):
    """[Conditions & Execution] Time limit of memory of the ancient king_0th phase
    z169: Global timer ID
    z190: Execution start time of the 0th phase process
    action4: Text ID displayed in the 0th phase
    """
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 3: Wait for a fixed time or multi judgment or judgment within point"""
    CompareStateTime(0, z190, 3, z190)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 5: Pause timer"""
        SuspendGlobalTimer(z169)
        """State 4: Rerun"""
        RestartMachine()
    elif ConditionGroup(0):
        """State 1: Event message display"""
        # action:2011:"One cannot reside within memory for long"
        DisplayEventMessage(action4, 0, 0, 0)
        """State 6: End state"""
        return 0

def event_m50_36_x113(z169=4, val7=1050, action2=2012):
    """[Conditions & Execution] Time limit of memory of old king _First phase
    z169: Global timer ID
    val7: Execution start time of the first phase process
    action2: Text ID to display in the first phase
    """
    """State 0,1: Time limit waiting or multi judgment or judgment within point"""
    CompareGlobalTimer(0, z169, val7, 3)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 4: Pause timer"""
        SuspendGlobalTimer(z169)
        """State 3: Rerun"""
        RestartMachine()
    elif ConditionGroup(0):
        """State 2: Event message display"""
        # action:2012:"The ashen mist has thinned..."
        DisplayEventMessage(action2, 0, 0, 0)
        """State 5: End state"""
        return 0

def event_m50_36_x114(z169=4, val8=1070, z170=0):
    """[Conditions & Execution] Memory time limit of the ancient king _ 2nd phase
    z169: Global timer ID
    val8: Execution start time of the second phase process
    z170: Time limit notification flag
    """
    """State 0,1: Time limit waiting or multi judgment or judgment within point"""
    CompareGlobalTimer(0, z169, val8, 3)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 4: Pause timer"""
        SuspendGlobalTimer(z169)
        """State 3: Rerun"""
        RestartMachine()
    elif ConditionGroup(0):
        """State 2: Time limit notification flag ON"""
        SetEventFlag(z170, 1)
        """State 5: End state"""
        return 0

def event_m50_36_x115(z169=4, z171=1080, action3=2013, z172=5400000):
    """[Conditions & Execution] Time limit of memory of the ancient king_3rd phase
    z169: Global timer ID
    z171: Execution start time of the third phase process
    action3: Text ID to display in the third phase
    z172: Return Warp Point ID
    """
    """State 0,1: Time limit waiting or multi judgment or judgment within point"""
    CompareGlobalTimer(0, z169, z171, 3)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 5: Pause timer"""
        SuspendGlobalTimer(z169)
        """State 4: Rerun"""
        RestartMachine()
    elif ConditionGroup(0):
        """State 6: Multiplayer prohibited state: ON"""
        ProhibitMultiplayer(1)
        """State 2: Event message display"""
        # action:2013:"The ashen mist fades..."
        DisplayEventMessage(action3, 0, 0, 0)
        """State 3: Timer reset"""
        EndGlobalTimer(z169)
        """State 8: [Lib] Warp between maps after poly play_SubState"""
        assert event_m50_36_x0(z192=0, z193=0, z194=50360000, z172=z172)
        """State 7: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
        """State 9: End state"""
        return 0

def event_m50_36_x116(z189=50363040):
    """[Preset] Run the facility
    z189: Launch OBJ instance ID
    """
    """State 0,1: [Reproduction] _SubState to operate the facility"""
    call = event_m50_36_x117(z189=z189)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L1')
    """State 8: End of reproduction"""
    return 1
    """State 6: [Condition] _Host_SubState for operating the facility"""
    Label('L0')
    call = event_m50_36_x122(z189=z189)
    if call.Get() == 0:
        """State 3: [Execution] Operate the facility_Host_Available_SubState"""
        call = event_m50_36_x119(z189=z189)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: End of operation"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Run the facility_Host_Unlockable_SubState"""
        assert event_m50_36_x120(z189=z189)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Operating the facility_Guest_SubState"""
    Label('L1')
    assert event_m50_36_x121(z189=z189)
    """State 2: [Execution] Run the facility_Guest_Empty_SubState"""
    assert event_m50_36_x118()
    """State 9: Guest termination"""
    return 2

def event_m50_36_x117(z189=50363040):
    """[Reproduction] Operate the facility
    z189: Launch OBJ instance ID
    """
    """State 0,2: Host judgment"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 5: Guest termination"""
    return 0
    """State 1: Start OBJ status judgment"""
    Label('L0')
    if CompareObjStateId(z189, 20, 0):
        pass
    elif CompareObjStateId(z189, 76, 0):
        pass
    elif CompareObjStateId(z189, 74, 0):
        pass
    elif CompareObjStateId(z189, 70, 0):
        pass
    else:
        Goto('L1')
    """State 7: After execution"""
    return 2
    """State 3: Safety: Still waiting for operation?"""
    Label('L1')
    if CompareObjStateId(z189, 30, 1):
        pass
    else:
        """State 4: Returning to the initial state: 10"""
        ChangeObjState(z189, 10)
        assert CompareObjStateId(z189, 10, 0)
    """State 6: Before execution"""
    return 1

def event_m50_36_x118():
    """[Execution] Operate the facility_Guest_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x119(z189=50363040):
    """[Execution] Operate the facility_Host_Available
    z189: Active OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:53100000:Scorching Iron Scepter
    DisplayYesNoMenu(1002, 1.8, z189, 190, 2, 53100000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 6: Wait for operation transition: 30"""
        ChangeObjState(z189, 30)
        assert CompareObjStateId(z189, 30, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z189, 38, 16)
        assert PlayerIsInEventAction(16) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 16, 0)
        # goods:53100000:Scorching Iron Scepter
        DoesPlayerHaveItem(0, 53100000, 0, 5, 1, 1, 0)
        CompareObjState(1, z189, 74, 0)
        CompareObjState(1, z189, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Fire sashimi stick consumption"""
            # goods:53100000:Scorching Iron Scepter
            ConsumeItem(53100000, 1)
            assert CompareObjStateId(z189, 20, 0)
            """State 8: End of operation"""
            return 0
    else:
        pass
    """State 7: Returning to the initial state: 10"""
    ChangeObjState(z189, 10)
    """State 9: Rerun"""
    return 1

def event_m50_36_x120(z189=50363040):
    """[Execution] Operate the facility_Host_Unlockable
    z189: Launch OBJ instance ID
    """
    """State 0,2: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:53100000:Scorching Iron Scepter
    DisplayOkMenu(1013, 0, 0, z189, 190, 2, 53100000, 0)
    assert OkMenuDisplay() != 1
    """State 1: Wait for initial state"""
    CompareObjState(0, z189, 10, 0)
    assert ConditionGroup(0)
    """State 3: Unsuccessful unlocking_rerun"""
    return 0

def event_m50_36_x121(z189=50363040):
    """[Condition] _Guest to operate the facility
    z189: Launch OBJ instance ID
    """
    """State 0,1: Wait for completion"""
    CompareObjState(0, z189, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x122(z189=50363040):
    """[Condition] _Host to operate the facility
    z189: Launch OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z189)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:53100000:Scorching Iron Scepter
    DoesPlayerHaveItem(0, 53100000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 3: Ready for operation"""
        return 0
    else:
        """State 4: Not operational"""
        return 1

def event_m50_36_x123(z181=_, z182=_, z183=_, z184=_, z185=_, z186=_, z187=_, z188=_):
    """[Preset] Fire-blowing cow that slides
    z181: Cow OBJ instance ID
    z182: OBJ state ID before operation
    z183: OBJ state ID after operation
    z184: OBJ state ID in operation from before operation
    z185: OBJ state ID that has been in operation since operation
    z186: Before operation_Navigation change point ID
    z187: Active_Navigation change point ID
    z188: After operation_navi change point ID
    """
    """State 0,5: [Reproduction] Sliding fire-blowing cow_Initialized version_SubState"""
    call = event_m50_36_x124(z181=z181, z182=z182, z183=z183, z184=z184, z185=z185, z186=z186, z187=z187,
                             z188=z188)
    if call.Get() == 0:
        """State 2: [Conditions] Sliding fire-blowing cow_SubState"""
        assert event_m50_36_x81(z104=z181)
        """State 1: [Execution] Sliding fire bull_SubState"""
        assert event_m50_36_x80(z181=z181, z184=z184, z183=z183, z186=z186, z187=z187, z188=z188)
    elif call.Get() == 1:
        """State 3: [Condition] Sliding fire-blowing cow_2_SubState"""
        assert event_m50_36_x81(z104=z181)
        """State 4: [Execution] Sliding fire-blown cow_2_SubState"""
        assert event_m50_36_x80(z181=z181, z184=z185, z183=z182, z186=z188, z187=z187, z188=z186)
    """State 6: Rerun"""
    return 0

def event_m50_36_x124(z181=_, z182=_, z183=_, z184=_, z185=_, z186=_, z187=_, z188=_):
    """[Reproduction] Sliding fire-blowing cow_initialization version
    z181: Cow OBJ instance ID
    z182: OBJ state ID before operation
    z183: OBJ state ID after operation
    z184: OBJ state ID in operation from before operation
    z185: OBJ state ID that has been in operation since operation
    z186: Before operation_Navigation change point ID
    z187: Active_Navigation change point ID
    z188: After operation_navi change point ID
    """
    """State 0,16: Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 8: Is the fire-blown cow before initialization?"""
    if CompareObjStateId(z181, 10, 0):
        """State 9: Initialize"""
        ChangeObjState(z181, z182)
        assert CompareObjStateId(z181, z182, 0)
    else:
        pass
    """State 1: Judgment of fire-blown cow"""
    if CompareObjStateId(z181, z184, 0):
        """State 4,14: Navi Mesh Change_5"""
        AddNavimeshAttribute(z186, 2)
        AddNavimeshAttribute(z187, 2)
        AddNavimeshAttribute(z188, 2)
        """State 7: Waiting for completion of operation"""
        assert CompareObjStateId(z181, z183, 0)
        """State 15: Navi Mesh Change_6"""
        DeleteNavimeshAttribute(z187, 2)
        DeleteNavimeshAttribute(z186, 2)
        AddNavimeshAttribute(z188, 2)
    elif CompareObjStateId(z181, z185, 0):
        """State 5,12: Navi Mesh Change_2"""
        AddNavimeshAttribute(z186, 2)
        AddNavimeshAttribute(z187, 2)
        AddNavimeshAttribute(z188, 2)
        """State 6: Wait for initial state"""
        assert CompareObjStateId(z181, z182, 0)
        """State 11: Navi Mesh Change_3"""
        DeleteNavimeshAttribute(z187, 2)
        DeleteNavimeshAttribute(z188, 2)
        AddNavimeshAttribute(z186, 2)
        """State 17: Fire-blown cow: initial state"""
        Label('L0')
        return 0
    elif CompareObjStateId(z181, z182, 0):
        """State 2,10: Navigation mesh change"""
        DeleteNavimeshAttribute(z187, 2)
        DeleteNavimeshAttribute(z188, 2)
        AddNavimeshAttribute(z186, 2)
        Goto('L0')
    elif CompareObjStateId(z181, z183, 0):
        """State 3,13: Navi Mesh Change_4"""
        DeleteNavimeshAttribute(z187, 2)
        DeleteNavimeshAttribute(z186, 2)
        AddNavimeshAttribute(z188, 2)
    """State 18: Fire-blown cow: End of operation"""
    return 1

def event_m50_36_x125(z180=536000049):
    """[Reproduction] Smoke damage caused by a spear image
    z180: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(z180) != 0:
        """State 2: Release smoke damage"""
        EnableDamageArea(501000, 0)
        EnableDamageArea(501001, 0)
        EnableDamageArea(501002, 0)
        """State 5: Destroyed"""
        return 1
    else:
        """State 3: Smoke damage effective"""
        EnableDamageArea(501000, 1)
        EnableDamageArea(501001, 1)
        EnableDamageArea(501002, 1)
        """State 4: Not destroyed"""
        return 0

def event_m50_36_x126(z179=_):
    """[Condition] Smoke damage caused by the image of a spider
    z179: Destruction flag
    """
    """State 0,1: Waiting for destruction of eagle statue"""
    CompareEventFlag(0, z179, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x127():
    """[Execution] Smoke damage caused by a spear image"""
    """State 0,1: Release smoke damage"""
    EnableDamageArea(501000, 0)
    EnableDamageArea(501001, 0)
    EnableDamageArea(501002, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x128(z180=536000049):
    """[Preset] Smoke damage caused by a spear image
    z180: Destruction flag
    """
    """State 0,1: [Reproduction] Smoke damage caused by a spear image_Isolated Island_SubState"""
    call = event_m50_36_x125(z180=z180)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Smoke damage due to the image of a spider _SubState"""
        assert event_m50_36_x126(z179=z180)
        """State 2: [Execution] Smoke damage caused by a spider image_Isolated Island_SubState"""
        assert event_m50_36_x127()
    """State 4: End state"""
    return 0

def event_m50_36_x129(z179=536000048):
    """[Reproduction] Smoke damage caused by a spider image_Lobby
    z179: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(z179) != 0:
        """State 2: Release smoke damage"""
        EnableDamageArea(601000, 0)
        EnableDamageArea(601001, 0)
        EnableDamageArea(601002, 0)
        EnableDamageArea(601003, 0)
        EnableDamageArea(601004, 0)
        """State 5: Destroyed"""
        return 1
    else:
        """State 3: Smoke damage effective"""
        EnableDamageArea(601000, 1)
        EnableDamageArea(601001, 1)
        EnableDamageArea(601002, 1)
        EnableDamageArea(601003, 1)
        EnableDamageArea(601004, 1)
        """State 4: Not destroyed"""
        return 0

def event_m50_36_x130():
    """[Execution] Smoke damage caused by a spider image_Lobby"""
    """State 0,1: Release smoke damage"""
    EnableDamageArea(601000, 0)
    EnableDamageArea(601001, 0)
    EnableDamageArea(601002, 0)
    EnableDamageArea(601003, 0)
    EnableDamageArea(601004, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x131(z179=536000048):
    """[Preset] Smoke damage caused by a spear image_Lobby
    z179: Destruction flag
    """
    """State 0,2: [Reproduction] Smoke damage caused by a spear image_Lobby_SubState"""
    call = event_m50_36_x129(z179=z179)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Smoke damage due to the image of a spider _SubState"""
        assert event_m50_36_x126(z179=z179)
        """State 3: [Execution] Smoke damage caused by a spear image_Lobby_SubState"""
        assert event_m50_36_x130()
    """State 4: End state"""
    return 0

def event_m50_36_x132(z173=536000049, z174=536000048):
    """[Reproduction] Smoke filter change by the image of the frog
    z173: Isolated island_destruction flag
    z174: Lobby_Destroy flag
    """
    """State 0,1: Are both eagle statues destroyed?"""
    if GetEventFlag(z173) != 0 and GetEventFlag(z174) != 0:
        """State 2: Destroyed"""
        return 0
    else:
        """State 3: Not destroyed"""
        return 1

def event_m50_36_x133(z175=20, z176=30, z173=536000049, z174=536000048, z177=22, z178=32):
    """[Condition] Smoke filter change by sculpture
    z175: Isolated island_hit group ID
    z176: Lobby_Hit Group ID
    z173: Isolated island_destruction flag
    z174: Lobby_Destroy flag
    z177: Isolated island_internal hit group ID
    z178: Lobby_Internal hit group ID
    """
    """State 0,1: Can you see the smoke area?"""
    SetConditionGroup(0, 8)
    IsPlayerOnHitGroup(8, z175, 1)
    CompareEventFlag(8, z173, 0)
    SetConditionGroup(0, 9)
    IsPlayerOnHitGroup(9, z177, 1)
    CompareEventFlag(9, z173, 0)
    SetConditionGroup(1, 10)
    IsPlayerOnHitGroup(10, z176, 1)
    CompareEventFlag(10, z174, 0)
    SetConditionGroup(1, 11)
    IsPlayerOnHitGroup(11, z178, 1)
    CompareEventFlag(11, z174, 0)
    CompareEventFlag(12, z173, 1)
    CompareEventFlag(12, z174, 1)
    if ConditionGroup(0):
        """State 2: Isolated island: Smoke area is visible"""
        return 0
    elif ConditionGroup(1):
        """State 3: Lobby: Smoke area is visible"""
        return 1
    elif ConditionGroup(10):
        """State 4: Both eagle statues broke"""
        return 2

def event_m50_36_x134(val9=_, z175=_, z173=_, z177=_):
    """[Execution] Smoke filter change by the image of the frog
    val9: Volume fog filter ID
    z175: Hit group ID
    z173: Destruction flag
    z177: Internal hit group ID
    """
    """State 0,2: Filter status judgment"""
    if (GetVolumeFogFilterOverride() == val9) != 1:
        """State 1: Push filter"""
        PushVolumeFogFilter(val9, 0)
        assert (GetVolumeFogFilterOverride() == val9) != 0
    else:
        pass
    """State 3: Can you see the smoke area? Did you destroy the eagle statue?"""
    IsPlayerOnHitGroup(8, z175, 0)
    IsPlayerOnHitGroup(8, z177, 0)
    CompareEventFlag(1, z173, 1)
    if ConditionGroup(8):
        """State 4: Outside area: Pop filter"""
        PopVolumeFogFilter(0)
        """State 5: Waiting for pop"""
        assert (GetVolumeFogFilterOverride() == val9) != 1
    elif ConditionGroup(1):
        """State 6: Destroy statue: pop filter"""
        PopVolumeFogFilter(5)
        """State 7: Waiting for pop_2"""
        assert (GetVolumeFogFilterOverride() == val9) != 1
    """State 8: Rerun"""
    return 0

def event_m50_36_x135(z173=536000049, z174=536000048, z175=20, z176=30, val9=14, val10=15, z177=22, z178=32):
    """[Preset] Smoke filter change by haze image
    z173: Isolated island_destruction flag
    z174: Lobby_Destroy flag
    z175: Isolated island_hit group ID
    z176: Lobby_Hit Group ID
    val9: Solitary island_volume fog filter ID
    val10: Lobby_volume fog filter ID
    z177: Isolated island_internal hit group ID
    z178: Lobby_Internal hit group ID
    """
    """State 0,1: [Reproduction] Smoke filter change by Subaru image_SubState"""
    call = event_m50_36_x132(z173=z173, z174=z174)
    if call.Get() == 1:
        """State 3: [Condition] Smoke filter change by sculpture image_SubState"""
        call = event_m50_36_x133(z175=z175, z176=z176, z173=z173, z174=z174, z177=z177, z178=z178)
        if call.Get() == 0:
            """State 2: [Execution] Smoke filter change by sculpture image_SubState"""
            assert event_m50_36_x134(val9=val9, z175=z175, z173=z173, z177=z177)
            """State 6: Rerun"""
            Label('L0')
            return 1
        elif call.Get() == 1:
            """State 4: [Execution] Smoke filter change by sculpture image_2_SubState"""
            assert event_m50_36_x134(val9=val10, z175=z176, z173=z174, z177=z178)
            Goto('L0')
        elif call.Get() == 2:
            pass
    elif call.Get() == 0:
        pass
    """State 5: End state"""
    return 0

def event_m50_36_x136():
    """[Reproduction] Time limit of memory of the ancient king"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_36_x137():
    """[Condition] Memory time limit of old king_start judgment"""
    """State 0,1: Riding the old king's hit during single play and out of point"""
    IsPlayerOnHitGroup(8, 10, 1)
    IsPlayerInsidePoint(8, 5500000, 5500011, 0)
    IsMultiplayer(8, 0, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_36_x138():
    """[Execution] Memory time limit of old king_Start judgment_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x139(z166=536000001, z167=536020002, z168=536020003):
    """[Reproduction] Continuous intrusion
    z166: Event completion flag
    z167: Event execution flag_1
    z168: Event execution flag_2 or later
    """
    """State 0,1: Has the event already been completed?"""
    if GetEventFlag(z166) != 0:
        pass
    else:
        Goto('L0')
    """State 6: Event completed"""
    return 2
    """State 3: Was it in the middle of the second and subsequent events?"""
    Label('L0')
    if GetEventFlag(z168) != 0:
        pass
    else:
        Goto('L1')
    """State 7: During generation: 2nd and subsequent bodies"""
    return 3
    """State 2: Was it in the middle of the first event?"""
    Label('L1')
    if GetEventFlag(z167) != 0:
        """State 5: During generation: 1st body"""
        return 1
    else:
        """State 4: Not executed"""
        return 0

def event_m50_36_x140(z163=_, z164=_, z165=_):
    """[Condition] Continuous intrusion
    z163: Start point ID
    z164: End point ID
    z165: Event execution flag
    """
    """State 0,1: Have you entered the dark spirit generation point? Has it already been done?"""
    SetConditionGroup(0, 8)
    IsHost(8, 1, 0)
    IsPlayerInsidePoint(8, z163, z164, 1)
    CompareEventFlag(0, z165, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x141(z51=536020004, z52=536020005, z53=536020006, z54=536020007, z55=536020008):
    """[Preset] Continuous intrusion
    z51: Generation flag ①
    z52: Generation flag ②
    z53: Generation flag ③
    z54: Generation flag (4)
    z55: Generation flag ⑤
    """
    """State 0,1: [Reproduction] Continuous intrusion_SubState"""
    call = event_m50_36_x139(z166=536000001, z167=536020002, z168=536020003)
    if call.Get() == 2:
        pass
    elif call.Get() == 3:
        """State 7: [Execution] Continuous intrusion _2 Subsequent generation_SubState"""
        Label('L0')
        assert event_m50_36_x260(z52=z52, z53=z53, z54=z54, z55=z55, z56=536020003)
    elif call.Get() == 1:
        """State 3: [Execution] Consecutive intrusion _1 body only generated_SubState"""
        assert event_m50_36_x146(z51=z51, z156=536020002)
        """State 5: [Reproduction] Continuous intrusion_empty_SubState"""
        Label('L1')
        assert event_m50_36_x259()
        """State 4: [Condition] Continuous intrusion_2_SubState"""
        assert event_m50_36_x140(z163=1900010, z164=1900010, z165=536020003)
        Goto('L0')
    elif call.Get() == 0:
        """State 2: [Condition] Continuous intrusion_SubState"""
        assert event_m50_36_x140(z163=1900000, z164=1900001, z165=536020002)
        """State 6: [Execution] Continuous intrusion_1 body_SubState"""
        assert event_m50_36_x258(z51=z51, z57=536020002)
        Goto('L1')
    """State 8: End state"""
    return 0

def event_m50_36_x142(z162=536000001):
    """[Reproduction] Continuous intrusion_end
    z162: Event completion flag
    """
    """State 0,1: Has the event already been completed?"""
    if GetEventFlag(z162) != 0:
        """State 3: Finish"""
        return 1
    else:
        """State 2: Not executed"""
        return 0

def event_m50_36_x143(z157=7000, z158=7001, z159=7002, z160=7003, z161=7004):
    """[Condition] Continuous intrusion_termination
    z157: Generator ID ①
    z158: Generator ID ②
    z159: Generator ID ③
    z160: Generator ID ④
    z161: Generator ID ⑤
    """
    """State 0,1: Did you destroy all the dark spirits?"""
    IsChrDeadOrRespawnOver(8, z157, 1)
    IsChrDeadOrRespawnOver(8, z158, 1)
    IsChrDeadOrRespawnOver(8, z159, 1)
    IsChrDeadOrRespawnOver(8, z160, 1)
    IsChrDeadOrRespawnOver(8, z161, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_36_x144(z162=536000001):
    """[Execute] Continuous intrusion_end
    z162: Event completion flag
    """
    """State 0,1: Network FE display"""
    OpenNetworkMessageMenu(9010, 0, 0, 0)
    OpenPresentationWindow(14)
    """State 2: Event completion flag ON"""
    SetEventFlag(z162, 1)
    """State 3: End state"""
    return 0

def event_m50_36_x145(z157=7000, z158=7001, z159=7002, z160=7003, z161=7004, z162=536000001):
    """[Preset] Continuous intrusion_end
    z157: Generator ID ①
    z158: Generator ID ②
    z159: Generator ID ③
    z160: Generator ID ④
    z161: Generator ID ⑤
    z162: Event completion flag
    """
    """State 0,1: [Reproduction] Continuous intrusion_end_SubState"""
    call = event_m50_36_x142(z162=z162)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Continuous intrusion_End_SubState"""
        assert event_m50_36_x143(z157=z157, z158=z158, z159=z159, z160=z160, z161=z161)
        """State 2: [Execution] Continuous intrusion_End_SubState"""
        assert event_m50_36_x144(z162=z162)
    """State 4: End state"""
    return 0

def event_m50_36_x146(z51=536020004, z156=536020002):
    """[Execution] Continuous intrusion_1
    z51: Generation flag ①
    z156: Event executed flag_1 body
    """
    """State 0,3: Execution flag ON"""
    SetEventFlag(z156, 1)
    """State 2: Generate weight 1"""
    CompareStateTime(0, 0, 3, 0)
    assert ConditionGroup(0)
    """State 1: Generation flag 1 ON"""
    SetEventFlag(z51, 1)
    """State 4: End state"""
    return 0

def event_m50_36_x147(z148=_, z149=_, z150=_, z151=_, z152=_, z153=_, z154=_, z155=_):
    """[Preset] Destroy the statue
    z148: 像 image OBJ instance ID
    z149: Destruction flag
    z150: Treasure OBJ instance ID
    z151: Initial state OBJ state ID
    z152: Activation confirmed OBJ state ID
    z153: OBJ state ID during alignment
    z154: OBJ state ID after cancellation
    z155: Navigation change point ID
    """
    """State 0,1: [Reproduction] Destroying a spider image_SubState"""
    call = event_m50_36_x148(z148=z148, z149=z149, z150=z150, z151=z151, z152=z152, z153=z153, z154=z154,
                             z155=z155)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L1')
    """State 8: End of reproduction"""
    return 1
    """State 6: [Condition] Destroying the statue of a spider_host_SubState"""
    Label('L0')
    call = event_m50_36_x149(z148=z148)
    if call.Get() == 0:
        """State 3: [Execution] Destroying the image of the spider_Host_Destroyable_SubState"""
        call = event_m50_36_x150(z148=z148, z149=z149, z150=z150, z153=z153, z152=z152, z154=z154, z155=z155)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: End of destruction"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Destroying the image of the spider_Host_Unbreakable_SubState"""
        assert event_m50_36_x151(z148=z148, z154=z154)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Destroying the image of a spider_Guest_SubState"""
    Label('L1')
    assert event_m50_36_x152(z148=z148)
    """State 2: [Execution] Destroying the image of a spider _Guest_SubState"""
    assert event_m50_36_x153(z155=z155)
    """State 9: Guest termination"""
    return 2

def event_m50_36_x148(z148=_, z149=_, z150=_, z151=_, z152=_, z153=_, z154=_, z155=_):
    """[Reproduction] Destroying a spear image
    z148: 像 image OBJ instance ID
    z149: Destruction flag
    z150: Treasure OBJ instance ID
    z151: Initial state OBJ state ID
    z152: Activation confirmed OBJ state ID
    z153: OBJ state ID during alignment
    z154: OBJ state ID after cancellation
    z155: Navigation change point ID
    """
    """State 0,2: Host judgment"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 11: Navigation change: No traffic_2"""
    AddNavimeshAttribute(z155, 2)
    """State 12: Guest termination"""
    return 0
    """State 5: Initialization judgment"""
    Label('L0')
    if CompareObjStateId(z148, 10, 1):
        pass
    else:
        """State 6: Transition to initial state"""
        ChangeObjState(z148, z151)
        assert CompareObjStateId(z148, z151, 0)
    """State 7: Safety: staying in alignment?"""
    if CompareObjStateId(z148, z153, 1):
        pass
    else:
        """State 8: Transition to the state after cancellation"""
        ChangeObjState(z148, z154)
        assert CompareObjStateId(z148, z154, 0)
    """State 1: OBJ status judgment"""
    if CompareObjStateId(z148, 20, 0):
        """State 3: Destruction flag ON"""
        Label('L1')
        SetEventFlag(z149, 1)
        """State 10: Navigation change: Allowed to pass"""
        DeleteNavimeshAttribute(z155, 2)
        """State 14: After execution"""
        return 2
    elif CompareObjStateId(z148, z152, 0):
        Goto('L1')
    elif CompareObjStateId(z148, 50, 0):
        Goto('L1')
    elif CompareObjStateId(z148, 51, 0):
        Goto('L1')
    elif CompareObjStateId(z148, 60, 0):
        Goto('L1')
    else:
        """State 4: Hide treasure"""
        ChangeDrawHit(z150, 0)
        """State 9: Navigation change: No traffic"""
        AddNavimeshAttribute(z155, 2)
        """State 13: Before execution"""
        return 1

def event_m50_36_x149(z148=_):
    """[Conditions] Destroying a spider image_Host
    z148: 像 image OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z148)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:53200000:Smelter Wedge
    DoesPlayerHaveItem(0, 53200000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 3: Destructible"""
        return 0
    else:
        """State 4: Indestructible"""
        return 1

def event_m50_36_x150(z148=_, z149=_, z150=_, z153=_, z152=_, z154=_, z155=_):
    """[Execution] Destroying the image of a spider
    z148: 像 image OBJ instance ID
    z149: Destruction flag
    z150: Treasure OBJ instance ID
    z153: OBJ state ID during alignment
    z152: Activation confirmed OBJ state ID
    z154: OBJ state ID after cancellation
    z155: Navigation change point ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:53200000:Smelter Wedge
    DisplayYesNoMenu(1002, 2.2, z148, 190, 2, 53200000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 6: Waiting for alignment"""
        ChangeObjState(z148, z153)
        assert CompareObjStateId(z148, z153, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z148, 38, 16)
        assert PlayerIsInEventAction(11) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 16, 0)
        # goods:53200000:Smelter Wedge
        DoesPlayerHaveItem(0, 53200000, 0, 5, 1, 1, 0)
        CompareObjState(1, z148, z152, 0)
        CompareObjState(1, z148, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Destruction item consumption"""
            # goods:53200000:Smelter Wedge
            ConsumeItem(53200000, 1)
            if CompareObjStateId(z148, 50, 0):
                pass
            elif CompareObjStateId(z148, 51, 0):
                pass
            """State 9: Treasure display"""
            ChangeDrawHit(z150, 1)
            assert CompareObjStateId(z148, 20, 0)
            """State 8: Destruction flag ON"""
            SetEventFlag(z149, 1)
            """State 10: Navigation change: Allowed to pass"""
            DeleteNavimeshAttribute(z155, 2)
            """State 11: End of destruction"""
            return 0
    else:
        pass
    """State 7: Return to the state after cancellation"""
    ChangeObjState(z148, z154)
    """State 12: Rerun"""
    return 1

def event_m50_36_x151(z148=_, z154=_):
    """[Execution] Destroying a spider image
    z148: 像 image OBJ instance ID
    z154: OBJ state ID after cancellation
    """
    """State 0,2: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:53200000:Smelter Wedge
    DisplayOkMenu(1013, 0, 0, z148, 190, 2, 53200000, 0)
    assert OkMenuDisplay() != 1
    """State 1: Waiting after cancellation"""
    CompareObjState(0, z148, z154, 0)
    assert ConditionGroup(0)
    """State 3: Unsuccessful unlocking_rerun"""
    return 0

def event_m50_36_x152(z148=_):
    """[Condition] Destroying the statue of a spider _Guest
    z148: 像 image OBJ instance ID
    """
    """State 0,1: Wait for completion"""
    CompareObjState(0, z148, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x153(z155=_):
    """[Execution] Destroy the statue of a spider _Guest
    z155: Navigation change point ID
    """
    """State 0,1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z155, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x154(z144=536020082, z145=536000081):
    """[Reproduction] Boss behavior change with Verstad equipment
    z144: Logic flag
    z145: Boss destruction flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 5: Has the boss been destroyed?"""
        if GetEventFlag(z145) != 0:
            pass
        else:
            """State 2: Equipment judgment"""
            # goods:23330100:Velstadt's Helm
            if (EquippedItemCount(23330100) >= 0) != 0:
                """State 3: Logic flag ON"""
                SetEventFlag(z144, 1)
                """State 6: Equipped"""
                return 0
            else:
                """State 4: Logic flag OFF"""
                SetEventFlag(z144, 0)
                """State 8: Not equipped"""
                return 2
    else:
        pass
    """State 7: Finish"""
    return 1

def event_m50_36_x155(z147=_):
    """[Condition] Boss behavior changes with Verstud equipment
    z147: Comparison value
    """
    """State 0,1: Equipment judgment"""
    # goods:23330100:Velstadt's Helm
    IsItemEquipped(0, 23330100, z147, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x156(z144=536020082, z146=_):
    """[Execution] Boss behavior change with Verstad equipment
    z144: Logic flag
    z146: ON or OFF
    """
    """State 0,1: Logic flag switching"""
    SetEventFlag(z144, z146)
    """State 2: End state"""
    return 0

def event_m50_36_x157(z144=536020082, z145=536000081):
    """[Preset] Boss behavior change with Verstud equipment
    z144: Logic flag
    z145: Boss destruction flag
    """
    """State 0,1: [Reproduction] Boss behavior change with Verstad equipment_SubState"""
    call = event_m50_36_x154(z144=z144, z145=z145)
    if call.Get() == 1:
        """State 7: Finish"""
        return 1
    elif call.Get() == 0:
        """State 3: [Condition] Boss behavior change with Verstad equipment_SubState"""
        assert event_m50_36_x155(z147=0)
        """State 2: [Execution] Boss behavior change with Verstad equipment_SubState"""
        assert event_m50_36_x156(z144=z144, z146=0)
    elif call.Get() == 2:
        """State 4: [Conditions] Boss behavior change with Verstad equipment_2_SubState"""
        assert event_m50_36_x155(z147=1)
        """State 5: [Execution] Boss behavior change with Verstad equipment_2_SubState"""
        assert event_m50_36_x156(z144=z144, z146=1)
    """State 6: Rerun"""
    return 0

def event_m50_36_x158(z142=50361075, mode3=0, z143=536020016, val6=2):
    """[Reproduction] Continuous iron lattice _7 version opened with lever
    z142: Lever OBJ instance ID
    mode3: weight
    z143: Event completion flag
    val6: Large weight closes
    """
    """State 0,10: Event completion judgment"""
    if GetEventFlag(z143) != 0:
        pass
    else:
        """State 1: Judgment of lever status"""
        if CompareObjStateId(z142, 70, 0):
            """State 9: Lever end waiting"""
            Label('L0')
            assert CompareObjStateId(z142, 20, 0)
            """State 6: Front grid check"""
            if CompareObjStateId(50362051, 10, 1) and CompareObjStateId(50362052, 10, 1):
                """State 7: State determination of iron grid in front of center"""
                assert CompareObjStateId(50362053, 10, 1) and CompareObjStateId(50362054, 10, 1)
                """State 8: State determination of iron grid at the center back"""
                if CompareObjStateId(50362055, 10, 1) and CompareObjStateId(50362056, 10, 1):
                    """State 13: The state of the innermost iron grid"""
                    if CompareObjStateId(50362057, 10, 1) and CompareObjStateId(50362058, 10, 1):
                        """State 14: Large iron grid state judgment"""
                        if CompareObjStateId(50362050, 10, 0):
                            """State 5: Large iron bar opens: 70"""
                            Label('L1')
                            ChangeObjState(50362050, 70)
                            """State 18: Opening the large iron grid"""
                            Label('L2')
                            assert CompareObjStateId(50362050, 30, 0)
                            """State 19: Weight until closing"""
                            Label('L3')
                            assert (GetStateTime() > val6) != 0
                            """State 16: Large iron grid closes: 80"""
                            ChangeObjState(50362050, 80)
                        else:
                            """State 17: Large iron grid condition judgment_2"""
                            if CompareObjStateId(50362050, 70, 0):
                                Goto('L2')
                            else:
                                """State 20: Large iron grid state determination_3"""
                                if CompareObjStateId(50362050, 30, 0):
                                    Goto('L3')
                                else:
                                    pass
                    else:
                        """State 12: The innermost iron bar opens: 70"""
                        Label('L4')
                        ChangeObjState(50362057, 70)
                        ChangeObjState(50362058, 70)
                        assert (GetStateTime() > 0.5) != 0
                        Goto('L1')
                else:
                    """State 4: The iron bar in the center back opens: 70"""
                    Label('L5')
                    ChangeObjState(50362055, 70)
                    ChangeObjState(50362056, 70)
                    assert (GetStateTime() > mode3) != 0
                    Goto('L4')
            else:
                """State 2: The front iron grid opens: 70"""
                ChangeObjState(50362051, 70)
                ChangeObjState(50362052, 70)
                assert (GetStateTime() > mode3) != 0
                """State 3: The front iron bar opens: 70"""
                ChangeObjState(50362053, 70)
                ChangeObjState(50362054, 70)
                assert (GetStateTime() > mode3) != 0
                Goto('L5')
            """State 15: Waiting for large iron grid to close"""
            assert CompareObjStateId(50362050, 20, 0)
            """State 11: Continuous bar event completion flag ON"""
            SetEventFlag(z143, 1)
        elif CompareObjStateId(z142, 72, 0):
            Goto('L0')
        elif CompareObjStateId(z142, 20, 0):
            Goto('L0')
        else:
            """State 21: Not in operation"""
            return 0
    """State 22: Already in operation"""
    return 1

def event_m50_36_x159(z140=_):
    """[Conditions] Continuous iron grid that opens with lever
    z140: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z140, 72, 0)
    CompareObjState(0, z140, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x160(mode3=0, z143=536020016, val6=2):
    """[Execution] Continuous iron lattice _7 versions opened with lever
    mode3: weight
    z143: Event completion flag
    val6: Large weight closes
    """
    """State 0,1: The front iron grid opens: 70"""
    ChangeObjState(50362051, 70)
    ChangeObjState(50362052, 70)
    """State 4: weight"""
    CompareStateTime(0, mode3, 3, mode3)
    assert ConditionGroup(0)
    """State 2: The front iron bar opens: 70"""
    ChangeObjState(50362053, 70)
    ChangeObjState(50362054, 70)
    """State 6: Weight_2"""
    CompareStateTime(0, mode3, 3, mode3)
    assert ConditionGroup(0)
    """State 3: The iron bar in the center back opens: 70"""
    ChangeObjState(50362055, 70)
    ChangeObjState(50362056, 70)
    """State 7: Weight_3"""
    CompareStateTime(0, mode3, 3, mode3)
    assert ConditionGroup(0)
    """State 9: The innermost iron bar opens: 70"""
    ChangeObjState(50362057, 70)
    ChangeObjState(50362058, 70)
    """State 10: Weight_4"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 5: Large iron bar opens: 70"""
    ChangeObjState(50362050, 70)
    """State 14: Large iron grid waiting to open"""
    CompareObjState(0, 50362050, 30, 0)
    assert ConditionGroup(0)
    """State 12: Weight_5"""
    CompareStateTime(0, val6, 3, val6)
    assert ConditionGroup(0)
    """State 13: Large iron grid closes: 80"""
    ChangeObjState(50362050, 80)
    """State 11: Large iron grid waiting to close"""
    CompareObjState(0, 50362050, 20, 0)
    assert ConditionGroup(0)
    """State 8: Continuous bar event completion flag ON"""
    SetEventFlag(z143, 1)
    """State 15: End state"""
    return 0

def event_m50_36_x161(mode2=0, z141=536020018, val5=3.5):
    """[Execution] Continuous iron lattice _9 versions opened with lever
    mode2: weight
    z141: Event completion flag
    val5: Large weight closes
    """
    """State 0,1: The front iron grid opens: 70"""
    ChangeObjState(50362061, 70)
    ChangeObjState(50362062, 70)
    """State 4: weight"""
    CompareStateTime(0, mode2, 3, mode2)
    assert ConditionGroup(0)
    """State 2: The front iron bar opens: 70"""
    ChangeObjState(50362063, 70)
    ChangeObjState(50362064, 70)
    """State 6: Weight_2"""
    CompareStateTime(0, mode2, 3, mode2)
    assert ConditionGroup(0)
    """State 3: Center bar opens: 70"""
    ChangeObjState(50362065, 70)
    ChangeObjState(50362066, 70)
    """State 7: Weight_3"""
    CompareStateTime(0, mode2, 3, mode2)
    assert ConditionGroup(0)
    """State 8: The iron bar in the center back opens: 70"""
    ChangeObjState(50362067, 70)
    ChangeObjState(50362068, 70)
    """State 9: Weight_4"""
    CompareStateTime(0, mode2, 3, mode2)
    assert ConditionGroup(0)
    """State 11: The innermost iron bar opens: 70"""
    ChangeObjState(50362069, 70)
    ChangeObjState(50362070, 70)
    """State 12: Weight_5"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 5: Large iron bar opens: 70"""
    ChangeObjState(50362060, 70)
    """State 16: Large iron grid waiting to open"""
    CompareObjState(0, 50362060, 30, 0)
    assert ConditionGroup(0)
    """State 14: Weight_6"""
    CompareStateTime(0, val5, 3, val5)
    assert ConditionGroup(0)
    """State 15: Large iron grid closes: 80"""
    ChangeObjState(50362060, 80)
    """State 13: Large iron grid waiting to close"""
    CompareObjState(0, 50362060, 20, 0)
    assert ConditionGroup(0)
    """State 10: Continuous bar event completion flag ON"""
    SetEventFlag(z141, 1)
    """State 17: End state"""
    return 0

def event_m50_36_x162(z140=50361076, mode2=0, z141=536020018, val5=3.5):
    """[Reproduction] Opening with a lever
    z140: Lever OBJ instance ID
    mode2: weight
    z141: Event completion flag
    val5: Large weight closes
    """
    """State 0,10: Event completion judgment"""
    if GetEventFlag(z141) != 0:
        pass
    else:
        """State 1: Judgment of lever status"""
        if CompareObjStateId(z140, 70, 0):
            """State 9: Lever end waiting"""
            Label('L0')
            assert CompareObjStateId(z140, 20, 0)
            """State 6: Front grid check"""
            if CompareObjStateId(50362061, 10, 1) and CompareObjStateId(50362062, 10, 1):
                """State 7: State determination of iron grid in front of center"""
                assert CompareObjStateId(50362063, 10, 1) and CompareObjStateId(50362064, 10, 1)
                """State 8: Central grid check"""
                if CompareObjStateId(50362065, 10, 1) and CompareObjStateId(50362066, 10, 1):
                    """State 12: State determination of iron grid at the center back"""
                    if CompareObjStateId(50362067, 10, 1) and CompareObjStateId(50362068, 10, 1):
                        """State 15: The state of the innermost iron grid"""
                        if CompareObjStateId(50362069, 10, 1) and CompareObjStateId(50362070, 10, 1):
                            """State 17: Large iron grid state judgment"""
                            if CompareObjStateId(50362060, 10, 0):
                                """State 5: Large iron bar opens: 70"""
                                Label('L1')
                                ChangeObjState(50362060, 70)
                                """State 18: Opening the large iron grid"""
                                Label('L2')
                                assert CompareObjStateId(50362060, 30, 0)
                                """State 19: Weight until closing"""
                                Label('L3')
                                assert (GetStateTime() > val5) != 0
                                """State 20: Large iron grid closes: 80"""
                                ChangeObjState(50362060, 80)
                            else:
                                """State 21: Large iron grid condition judgment_2"""
                                if CompareObjStateId(50362060, 70, 0):
                                    Goto('L2')
                                else:
                                    """State 22: Large iron grid state determination_3"""
                                    if CompareObjStateId(50362060, 30, 0):
                                        Goto('L3')
                                    else:
                                        pass
                        else:
                            """State 14: The innermost iron bar opens: 70"""
                            Label('L4')
                            ChangeObjState(50362069, 70)
                            ChangeObjState(50362070, 70)
                            assert (GetStateTime() > 0.5) != 0
                            Goto('L1')
                    else:
                        """State 13: The iron bar in the center back opens: 70"""
                        Label('L5')
                        ChangeObjState(50362067, 70)
                        ChangeObjState(50362068, 70)
                        assert (GetStateTime() > mode2) != 0
                        Goto('L4')
                else:
                    """State 4: Center bar opens: 70"""
                    Label('L6')
                    ChangeObjState(50362065, 70)
                    ChangeObjState(50362066, 70)
                    assert (GetStateTime() > mode2) != 0
                    Goto('L5')
            else:
                """State 2: The front iron grid opens: 70"""
                ChangeObjState(50362061, 70)
                ChangeObjState(50362062, 70)
                assert (GetStateTime() > mode2) != 0
                """State 3: The front iron bar opens: 70"""
                ChangeObjState(50362063, 70)
                ChangeObjState(50362064, 70)
                assert (GetStateTime() > mode2) != 0
                Goto('L6')
            """State 16: Waiting for large iron grid to close"""
            assert CompareObjStateId(50362060, 20, 0)
            """State 11: Continuous bar event completion flag ON"""
            SetEventFlag(z141, 1)
        elif CompareObjStateId(z140, 72, 0):
            Goto('L0')
        elif CompareObjStateId(z140, 20, 0):
            Goto('L0')
        else:
            """State 23: Not in operation"""
            return 0
    """State 24: Already in operation"""
    return 1

def event_m50_36_x163(z142=50361075, mode3=0, z143=536020016, val6=2):
    """[Preset] Continuous iron lattice _7 version opened with lever
    z142: Lever OBJ instance ID
    mode3: weight
    z143: Event completion flag
    val6: Large weight closes
    """
    """State 0,1: [Reproduction] Continuous iron lattice _7 version _SubState opened with lever"""
    call = event_m50_36_x158(z142=z142, mode3=mode3, z143=z143, val6=val6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Continuous iron grids opened by lever_SubState"""
        assert event_m50_36_x159(z140=z142)
        """State 2: [Execution] Continuous Lattice Opening with Lever_7 Versions_SubState"""
        assert event_m50_36_x160(mode3=mode3, z143=z143, val6=val6)
    """State 4: Finish"""
    return 0

def event_m50_36_x164(z140=50361076, mode2=0, z141=536020018, val5=3.5):
    """[Preset] Continuous iron lattice _ 9 versions opened with lever
    z140: Lever OBJ instance ID
    mode2: weight
    z141: Event completion flag
    val5: Large weight closes
    """
    """State 0,2: [Reproduction] Continuous iron lattice _9 versions_SubState opened with lever"""
    call = event_m50_36_x162(z140=z140, mode2=mode2, z141=z141, val5=val5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Continuous iron grids opened by lever_SubState"""
        assert event_m50_36_x159(z140=z140)
        """State 3: [Execution] Continuous iron grids open with levers_9 versions_SubState"""
        assert event_m50_36_x161(mode2=mode2, z141=z141, val5=val5)
    """State 4: Finish"""
    return 0

def event_m50_36_x165():
    """[Reproduction] Salamander statue spitting fire"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x166(z138=_):
    """[Condition] Salamander statue spitting fire
    z138: Iron lattice OBJ instance ID
    """
    """State 0,1: The iron lattice is open or the iron lattice is closed"""
    CompareObjState(0, z138, 30, 0)
    CompareObjState(0, z138, 80, 0)
    CompareObjState(1, z138, 20, 0)
    if ConditionGroup(1):
        """State 3: Closed"""
        return 1
    elif ConditionGroup(0):
        """State 2: Open"""
        return 0

def event_m50_36_x167(z138=_, z139=_):
    """[Execution] Salamander statue spitting fire
    z138: Iron lattice OBJ instance ID
    z139: Salamander OBJ instance ID
    """
    """State 0,1: Fireball fire"""
    ChangeObjState(z139, 70)
    """State 2: Random weight"""
    CompareStateTime(0, 1, 3, 2)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x168(z138=_, z139=_):
    """[Preset] Salamander statue spitting fire
    z138: Iron lattice OBJ instance ID
    z139: Salamander OBJ instance ID
    """
    """State 0,1: [Reproduction] Salamander image _SubState spitting fire"""
    assert event_m50_36_x165()
    """State 3: [Condition] Salamander statue spit fire_SubState"""
    call = event_m50_36_x166(z138=z138)
    if call.Get() == 1:
        """State 5: Finish"""
        return 1
    elif call.Get() == 0:
        """State 2: [Execution] Salamander statue _SubState spitting fire"""
        assert event_m50_36_x167(z138=z138, z139=z139)
        """State 4: Rerun"""
        return 0

def event_m50_36_x169(z136=_):
    """[Reproduction] Recovery sphere with a spear image
    z136: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(z136) != 0:
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Not destroyed"""
        return 0

def event_m50_36_x170(z136=_):
    """[Conditions] Recovery sphere with a spear image
    z136: Destruction flag
    """
    """State 0,1: Waiting for destruction of eagle statue"""
    CompareEventFlag(0, z136, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x171(z137=_):
    """[Execution] Recovery sphere with spear image
    z137: Recovery ball OBJ instance ID
    """
    """State 0,1: Disappearance of recovery ball: 20"""
    ChangeObjState(z137, 20)
    """State 2: End state"""
    return 0

def event_m50_36_x172(z136=_, z137=_):
    """[Preset] Recovery sphere with spear image
    z136: Destruction flag
    z137: Recovery ball OBJ instance ID
    """
    """State 0,1: [Reproduction] Recovery sphere with a spear image_SubState"""
    call = event_m50_36_x169(z136=z136)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Recovery sphere by the image of a spider _SubState"""
        assert event_m50_36_x170(z136=z136)
    """State 2: [Execution] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x171(z137=z137)
    """State 4: End state"""
    return 0

def event_m50_36_x173(z133=536000026):
    """[Reproduction] Unraveling the curse of the bride ’s soul
    z133: Event completion flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Has Seoul already changed?"""
    if GetEventFlag(z133) != 0:
        """State 4: Changed: finished"""
        return 1
    else:
        """State 3: Not executed"""
        return 0
    """State 5: The guests"""
    Label('L0')
    return 2

def event_m50_36_x174():
    """[Condition] The curse of the bride ’s soul can be solved."""
    """State 0,1: Did all the statues of the samurai break? Do you have all fake souls?"""
    CompareEventFlag(8, 536000059, 1)
    # goods:53300000:Soul of Nadalia, Bride of Ash
    DoesPlayerHaveItem(8, 53300000, 12, 3, 1, 1, 0)
    CompareEventFlag(9, 101061, 1)
    WasObjItemAcquired(9, 50368500, 1)
    WasObjItemAcquired(9, 50368510, 1)
    WasObjItemAcquired(9, 50368520, 1)
    WasObjItemAcquired(9, 50368530, 1)
    WasObjItemAcquired(9, 50368540, 1)
    WasObjItemAcquired(9, 50368560, 1)
    WasObjItemAcquired(9, 50368570, 1)
    WasObjItemAcquired(9, 50368580, 1)
    WasObjItemAcquired(9, 50368590, 1)
    WasObjItemAcquired(9, 50368600, 1)
    WasObjItemAcquired(9, 50368610, 1)
    # goods:53300000:Soul of Nadalia, Bride of Ash
    DoesPlayerHaveItem(9, 53300000, 11, 3, 1, 1, 0)
    SetConditionGroup(0, 8)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x175(z134=5, z135=5):
    """[Execution] Unravel the curse of the bride ’s soul
    z134: Weight until item acquisition
    z135: Weight until info display
    """
    """State 0,2: weight"""
    CompareStateTime(8, z134, 3, z134)
    # goods:53300000:Soul of Nadalia, Bride of Ash
    DoesPlayerHaveItem(8, 53300000, 12, 3, 1, 1, 0)
    CompareStateTime(0, z134, 3, z134)
    if ConditionGroup(8):
        """State 6: Redetermination"""
        # goods:53300000:Soul of Nadalia, Bride of Ash
        DoesPlayerHaveItem(8, 53300000, 12, 3, 1, 1, 0)
        if ConditionGroup(8):
            """State 1: Change to true Seoul & expand shop lineup"""
            # goods:53300000:Soul of Nadalia, Bride of Ash
            ConsumeItem(53300000, 12)
            # lot:60015000:Soul of Nadalia, Bride of Ash
            AwardItem(60015000, 1)
            SetEventFlag(101210, 1)
        else:
            """State 9: Rerun"""
            Label('L0')
            return 1
    elif ConditionGroup(0):
        """State 7: Redetermination_2"""
        # goods:53300000:Soul of Nadalia, Bride of Ash
        DoesPlayerHaveItem(8, 53300000, 11, 3, 1, 1, 0)
        if ConditionGroup(8):
            """State 5: Change to true Seoul & expand shop lineup_2"""
            # goods:53300000:Soul of Nadalia, Bride of Ash
            ConsumeItem(53300000, 11)
            # lot:60015000:Soul of Nadalia, Bride of Ash
            AwardItem(60015000, 1)
            SetEventFlag(101210, 1)
        else:
            Goto('L0')
    """State 4: Weight_2"""
    CompareStateTime(0, z135, 3, z135)
    assert ConditionGroup(0)
    """State 3: Event message display"""
    # action:5710:"Nadalia is no more. True Soul of Nadalia acquired."
    DisplayEventMessage(5710, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 8: End state"""
    return 0

def event_m50_36_x176(z133=536000026, z134=5, z135=5):
    """[Preset] Unravel the curse of the bride ’s soul
    z133: Event completion flag
    z134: Weight until item acquisition
    z135: Weight until info display
    """
    """State 0,2: [Reproduction] _SubState to unravel the curse of the bride ’s soul"""
    call = event_m50_36_x173(z133=z133)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] The bride's soul curse can be solved _SubState"""
        assert event_m50_36_x174()
        """State 3: [Execution] _SubState to unravel the curse of the bride ’s soul"""
        call = event_m50_36_x175(z134=z134, z135=z135)
        if call.Get() == 0:
            pass
        elif call.Done():
            """State 1: Rerun"""
            RestartMachine()
            Quit()
    elif call.Get() == 2:
        pass
    """State 5: End state"""
    return 0

def event_m50_36_x177(z131=50363090, z132=536000032):
    """[Preset] OBJ blocking the one-way door
    z131: OBJ instance ID to be destroyed
    z132: One-way door flag
    """
    """State 0,1: [Reproduction] OBJ_Sky_SubState that blocks a one-way door"""
    assert event_m50_36_x178()
    """State 3: [Condition] OBJ_SubState that blocks a one-way door"""
    assert event_m50_36_x180(z131=z131)
    """State 2: [Execution] OBJ_SubState to block the one-way door"""
    assert event_m50_36_x179(z132=z132)
    """State 4: End state"""
    return 0

def event_m50_36_x178():
    """[Reproduction] OBJ_sky blocking one-way door"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x179(z132=536000032):
    """[Execution] OBJ blocking one-way door
    z132: One-way door flag
    """
    """State 0,1: One-way flag ON"""
    SetEventFlag(z132, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x180(z131=50363090):
    """[Conditions] OBJ blocking a one-way door
    z131: OBJ instance ID to be destroyed
    """
    """State 0,1: Is the target OBJ broken?"""
    IsObjBroken(0, z131, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x181(z25=50363080, z26=536000020, z27=5, action1=5310, z28=50360080):
    """[Preset] Crown that appears when a boss is destroyed
    z25: Crown OBJ instance ID
    z26: Crown acquisition flag
    z27: weight
    action1: Text ID
    z28: Event light ID
    """
    """State 0,1: [Reproduction] Crown _SubState that appears when a boss is destroyed"""
    call = event_m50_36_x182(z26=z26, z25=z25, z28=z28)
    if call.Get() == 0:
        """State 3: [Condition] Crown _SubState that appears when a boss is destroyed"""
        call = event_m50_36_x184(z25=z25)
        if call.Get() == 0:
            """State 2: [Execution] Crown _SubState that appears when a boss is destroyed"""
            assert event_m50_36_x183(z25=z25, z26=z26, z27=z27, action1=action1, z28=z28)
        elif call.Get() == 1:
            """State 4: [Execution] Crown that appears after destroying the boss_Unacquired_SubState"""
            assert event_m50_36_x289(z25=z25)
            """State 6: Rerun"""
            return 1
    elif call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    """State 5: Finish"""
    return 0

def event_m50_36_x182(z26=536000020, z25=50363080, z28=50360080):
    """[Reproduction] Crown that appears when a boss is destroyed
    z26: Crown acquisition flag
    z25: Crown OBJ instance ID
    z28: Event light ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you acquired the crown?"""
    if GetEventFlag(z26) != 1:
        """State 4: Key guide enabled"""
        DisableObjKeyGuide(z25, 0)
        """State 5: Event light ON"""
        SetPointLightEnabled(z28, 1, 0)
        """State 7: Unacquired"""
        return 0
    else:
        """State 3: Hidden: 10"""
        ChangeObjState(z25, 10)
        """State 6: Event light OFF"""
        SetPointLightEnabled(z28, 0, 0)
        """State 9: Finish"""
        return 2
    """State 8: Guest user"""
    Label('L0')
    return 1

def event_m50_36_x183(z25=50363080, z26=536000020, z27=5, action1=5310, z28=50360080):
    """[Execution] The crown that appears when the boss is defeated
    z25: Crown OBJ instance ID
    z26: Crown acquisition flag
    z27: weight
    action1: Text ID
    z28: Event light ID
    """
    """State 0,7: Event light OFF"""
    SetPointLightEnabled(z28, 0, 0.5)
    """State 1: Hidden: 10"""
    ChangeObjState(z25, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z25, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60016000:Crown of the Old Iron King
    AwardItem(60016000, 1)
    """State 4: Turn on the crown acquisition flag"""
    SetEventFlag(z26, 1)
    """State 5: weight"""
    CompareStateTime(0, z27, 3, z27)
    assert ConditionGroup(0)
    """State 6: Text display"""
    # action:5310:"A faint heat lingers in the ancient crown"
    DisplayEventMessage(action1, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 8: End state"""
    return 0

def event_m50_36_x184(z25=50363080):
    """[Condition] Crown that appears when the boss is defeated
    z25: Crown OBJ instance ID
    """
    """State 0,1: Judging the crown"""
    IsObjSearched(0, z25)
    assert ConditionGroup(0)
    """State 2: Can items be acquired?"""
    # goods:21630100:Crown of the Old Iron King
    if CanGetItem(21630100, 1) != 0:
        """State 3: Item acquisition"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m50_36_x185(z125=_, z128=_):
    """[Reproduction] Activating the spider image
    z125: Destruction flag
    z128: Damipoli OBJ instance ID for production
    """
    """State 0,3: Is it a hostile spirit?"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    else:
        Goto('L0')
    """State 6: Hostile spirit: no reaction"""
    return 2
    """State 1: Is the samurai statue broken?"""
    Label('L0')
    if GetEventFlag(z125) != 0:
        pass
    else:
        """State 2: Has the production been activated?"""
        if CompareObjStateId(z128, 10, 0):
            """State 4: Not executed"""
            return 0
        else:
            pass
    """State 5: Executed"""
    return 1

def event_m50_36_x186(z125=_, z126=_, z127=5, z129=_, z130=_):
    """[Conditions] Activating the image of the frog
    z125: Destruction flag
    z126: 像 image OBJ instance ID
    z127: Comparison distance
    z129: Start point ID
    z130: End point ID
    """
    """State 0,1: Did you invade the or point that approached the sculpture statue?"""
    CompareObjPlayerDistance(0, z126, z127, 5)
    IsPlayerInsidePoint(0, z129, z130, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x187(z128=_):
    """[Execution] Activating the image of the frog
    z128: Damipoli OBJ instance ID for production
    """
    """State 0,1: Production activation: 70"""
    ChangeObjState(z128, 70)
    """State 2: End state"""
    return 0

def event_m50_36_x188(z125=_, z126=_, z127=5, z128=_, z129=_, z130=_):
    """[Preset] Activating the frog image
    z125: Destruction flag
    z126: 像 image OBJ instance ID
    z127: Comparison distance
    z128: Damipoli OBJ instance ID for production
    z129: Start point ID
    z130: End point ID
    """
    """State 0,1: [Reproduction] Activating the frog image_SubState"""
    call = event_m50_36_x185(z125=z125, z128=z128)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Activating the image of the frog_SubState"""
        assert event_m50_36_x186(z125=z125, z126=z126, z127=z127, z129=z129, z130=z130)
        """State 2: [Execution] Activating the image of the frog_SubState"""
        assert event_m50_36_x187(z128=z128)
    """State 4: End state"""
    return 0

def event_m50_36_x189(val4=_, z118=_, z119=_, z124=_):
    """[Conditions] Wetting enhancement
    val4: OBJ instance ID for production
    z118: Destruction flag
    z119: Generator ID
    z124: 像 image OBJ instance ID
    """
    """State 0,2: Always activated"""
    if (not val4) != 0:
        pass
    else:
        """State 1: Judgment judgment or destruction judgment"""
        CompareObjState(0, val4, 20, 0)
        CompareObjState(0, val4, 70, 0)
        CompareEventFlag(1, z118, 1)
        IsChrDead(1, z119)
        CompareObjState(1, z124, 50, 0)
        CompareObjState(1, z124, 51, 0)
        if ConditionGroup(1):
            """State 3: Cancel: Do nothing"""
            return 0
        elif ConditionGroup(0):
            pass
    """State 4: Strengthen"""
    return 1

def event_m50_36_x190(z119=_, z120=_, z118=_, z121=_, z122=_, z123=_, z124=_):
    """[Execution] Wetting enhancement
    z119: Generator ID
    z120: Special effect ID during effect
    z118: Destruction flag
    z121: Special effect ID for release effect
    z122: Special effect ID for activation
    z123: Enhanced Special Effect ID
    z124: 像 image OBJ instance ID
    """
    """State 0,1: For strengthening, during effect, for triggering effect 3 special effects are given"""
    SetEnemySpEffect(z119, z120, 19, 4)
    SetEnemySpEffect(z119, z122, 19, 4)
    SetEnemySpEffect(z119, z123, 19, 4)
    """State 2: Destruction determination"""
    CompareEventFlag(0, z118, 1)
    IsChrDead(0, z119)
    CompareObjState(0, z124, 50, 0)
    CompareObjState(0, z124, 51, 0)
    assert ConditionGroup(0)
    """State 3: Cancel special effects"""
    ClearEnemySpEffect(z119, z120)
    ClearEnemySpEffect(z119, z122)
    ClearEnemySpEffect(z119, z123)
    """State 4: Special effects for release effects"""
    SetEnemySpEffect(z119, z121, 19, 4)
    """State 5: End state"""
    return 0

def event_m50_36_x191():
    """[Reproduction] Strengthening of wetness"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x192(val4=_, z118=_, z119=_, z120=_, z121=_, z122=_, z123=_, z124=_):
    """[Preset] Strengthening wetness
    val4: OBJ instance ID for production
    z118: Destruction flag
    z119: Generator ID
    z120: Special effect ID during effect
    z121: Special effect ID for release effect
    z122: Special effect ID for activation
    z123: Enhanced Special Effect ID
    z124: 像 image OBJ instance ID
    """
    """State 0,1: [Reproduction] Wetting enhancement_SubState"""
    assert event_m50_36_x191()
    """State 3: [Condition] Wetting enhancement_SubState"""
    call = event_m50_36_x189(val4=val4, z118=z118, z119=z119, z124=z124)
    if call.Get() == 1:
        """State 2: [Execution] Wetting enhancement_SubState"""
        assert event_m50_36_x190(z119=z119, z120=z120, z118=z118, z121=z121, z122=z122, z123=z123, z124=z124)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m50_36_x193(z111=50361221, z112=30, z113=32, z114=70, z115=72, z116=3200000, z117=3200020):
    """[Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawa 1F
    z111: Cow OBJ instance ID
    z112: OBJ state ID before operation
    z113: OBJ state ID after operation
    z114: OBJ state ID in operation from before operation
    z115: OBJ state ID that has been in operation since operation
    z116: Before operation_Navigation change point ID
    z117: After operation_navi change point ID
    """
    """State 0,16: Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 8: Is the fire-blown cow before initialization?"""
    if CompareObjStateId(z111, 10, 0):
        """State 9: Initialize"""
        ChangeObjState(z111, z112)
        assert CompareObjStateId(z111, z112, 0)
    else:
        pass
    """State 1: Judgment of fire-blown cow"""
    if CompareObjStateId(z111, z114, 0):
        """State 4,15: Navi Mesh Change_5"""
        AddNavimeshAttribute(z116, 2)
        AddNavimeshAttribute(3200010, 2)
        AddNavimeshAttribute(3200011, 2)
        AddNavimeshAttribute(3200012, 2)
        AddNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z117, 2)
        """State 7: Waiting for completion of operation"""
        assert CompareObjStateId(z111, z113, 0)
        """State 14: Navi Mesh Change_6"""
        DeleteNavimeshAttribute(z116, 2)
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z117, 2)
    elif CompareObjStateId(z111, z115, 0):
        """State 5,11: Navi Mesh Change_2"""
        AddNavimeshAttribute(z116, 2)
        AddNavimeshAttribute(3200010, 2)
        AddNavimeshAttribute(3200011, 2)
        AddNavimeshAttribute(3200012, 2)
        AddNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z117, 2)
        """State 6: Wait for initial state"""
        assert CompareObjStateId(z111, z112, 0)
        """State 13: Navi Mesh Change_3"""
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        DeleteNavimeshAttribute(z117, 2)
        AddNavimeshAttribute(z116, 2)
        """State 17: Fire-blown cow: initial state"""
        Label('L0')
        return 0
    elif CompareObjStateId(z111, z112, 0):
        """State 2,10: Navigation mesh change"""
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        DeleteNavimeshAttribute(z117, 2)
        AddNavimeshAttribute(z116, 2)
        Goto('L0')
    elif CompareObjStateId(z111, z113, 0):
        """State 3,12: Navi Mesh Change_4"""
        DeleteNavimeshAttribute(z116, 2)
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z117, 2)
    """State 18: Fire-blown cow: End of operation"""
    return 1

def event_m50_36_x194(z104=50361222, z105=40, z106=42, z107=80, z108=82, z109=3300020, z110=3300000):
    """[Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawa 2F
    z104: Cow OBJ instance ID
    z105: OBJ state ID before operation
    z106: OBJ state ID after operation
    z107: OBJ state ID in operation from before operation
    z108: OBJ state ID that has been in operation since operation
    z109: Before operation_Navigation change point ID
    z110: After operation_navi change point ID
    """
    """State 0,16: Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 8: Is the fire-blown cow before initialization?"""
    if CompareObjStateId(z104, 10, 0):
        """State 9: Initialize"""
        ChangeObjState(z104, z105)
        assert CompareObjStateId(z104, z105, 0)
    else:
        pass
    """State 1: Judgment of fire-blown cow"""
    if CompareObjStateId(z104, z107, 0):
        """State 4,15: Navi Mesh Change_5"""
        AddNavimeshAttribute(z109, 2)
        AddNavimeshAttribute(3300010, 2)
        AddNavimeshAttribute(3300011, 2)
        AddNavimeshAttribute(3300012, 2)
        AddNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z110, 2)
        """State 7: Waiting for completion of operation"""
        assert CompareObjStateId(z104, z106, 0)
        """State 14: Navi Mesh Change_6"""
        DeleteNavimeshAttribute(z109, 2)
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z110, 2)
    elif CompareObjStateId(z104, z108, 0):
        """State 5,11: Navi Mesh Change_2"""
        AddNavimeshAttribute(z109, 2)
        AddNavimeshAttribute(3300010, 2)
        AddNavimeshAttribute(3300011, 2)
        AddNavimeshAttribute(3300012, 2)
        AddNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z110, 2)
        """State 6: Wait for initial state"""
        assert CompareObjStateId(z104, z105, 0)
        """State 13: Navi Mesh Change_3"""
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        DeleteNavimeshAttribute(z110, 2)
        AddNavimeshAttribute(z109, 2)
        """State 17: Fire-blown cow: initial state"""
        Label('L0')
        return 0
    elif CompareObjStateId(z104, z105, 0):
        """State 2,10: Navigation mesh change"""
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        DeleteNavimeshAttribute(z110, 2)
        AddNavimeshAttribute(z109, 2)
        Goto('L0')
    elif CompareObjStateId(z104, z106, 0):
        """State 3,12: Navi Mesh Change_4"""
        DeleteNavimeshAttribute(z109, 2)
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z110, 2)
    """State 18: Fire-blown cow: End of operation"""
    return 1

def event_m50_36_x195(z111=50361221, z114=_, z113=_, z116=_, z117=_):
    """[Execution] sliding fire-blowing cow_Kenzawa 1F
    z111: Cow OBJ instance ID
    z114: Mobile OBJ state ID
    z113: Movement end OBJ state ID
    z116: Before operation_Navigation change point ID
    z117: After operation_navi change point ID
    """
    """State 0,3: Navigation mesh change"""
    AddNavimeshAttribute(z116, 2)
    AddNavimeshAttribute(3200010, 2)
    AddNavimeshAttribute(3200011, 2)
    AddNavimeshAttribute(3200012, 2)
    AddNavimeshAttribute(3200013, 2)
    AddNavimeshAttribute(z117, 2)
    """State 1: Slide movement of fire-blown cow"""
    ChangeObjState(z111, z114)
    """State 2: Waiting for movement to end"""
    CompareObjState(0, z111, z113, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change_2"""
    DeleteNavimeshAttribute(3200010, 2)
    DeleteNavimeshAttribute(3200011, 2)
    DeleteNavimeshAttribute(3200012, 2)
    DeleteNavimeshAttribute(3200013, 2)
    DeleteNavimeshAttribute(z116, 2)
    AddNavimeshAttribute(z117, 2)
    """State 5: End state"""
    return 0

def event_m50_36_x196(z104=50361222, z107=_, z106=_, z109=_, z110=_):
    """[Execution] Sliding fire-blowing _Kenzawa 2F
    z104: Cow OBJ instance ID
    z107: Mobile OBJ state ID
    z106: Movement end OBJ state ID
    z109: Before operation_Navigation change point ID
    z110: After operation_navi change point ID
    """
    """State 0,3: Navigation mesh change"""
    AddNavimeshAttribute(z109, 2)
    AddNavimeshAttribute(3300010, 2)
    AddNavimeshAttribute(3300011, 2)
    AddNavimeshAttribute(3300012, 2)
    AddNavimeshAttribute(3300013, 2)
    AddNavimeshAttribute(z110, 2)
    """State 1: Slide movement of fire-blown cow"""
    ChangeObjState(z104, z107)
    """State 2: Waiting for movement to end"""
    CompareObjState(0, z104, z106, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change_2"""
    DeleteNavimeshAttribute(3300010, 2)
    DeleteNavimeshAttribute(3300011, 2)
    DeleteNavimeshAttribute(3300012, 2)
    DeleteNavimeshAttribute(3300013, 2)
    DeleteNavimeshAttribute(z109, 2)
    AddNavimeshAttribute(z110, 2)
    """State 5: End state"""
    return 0

def event_m50_36_x197(z111=50361221, z112=30, z113=32, z114=70, z115=72, z116=3200000, z117=3200020):
    """[Preset] sliding fire-blowing cow_initialized version_Kenzawayama 1F
    z111: Cow OBJ instance ID
    z112: OBJ state ID before operation
    z113: OBJ state ID after operation
    z114: OBJ state ID in operation from before operation
    z115: OBJ state ID that has been in operation since operation
    z116: Before operation_Navigation change point ID
    z117: After operation_navi change point ID
    """
    """State 0,3: [Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawa 1F_SubState"""
    call = event_m50_36_x193(z111=z111, z112=z112, z113=z113, z114=z114, z115=z115, z116=z116, z117=z117)
    if call.Get() == 0:
        """State 1: [Conditions] Sliding fire-blowing cow_SubState"""
        assert event_m50_36_x81(z104=z111)
        """State 4: [Execution] Sliding fired cow _Kenzawa 1F_SubState"""
        assert event_m50_36_x195(z111=z111, z114=z114, z113=z113, z116=z116, z117=z117)
    elif call.Get() == 1:
        """State 2: [Condition] Sliding fire-blowing cow_2_SubState"""
        assert event_m50_36_x81(z104=z111)
        """State 5: [Execution] Sliding fire-blowing cow_Kenzawa 1F_2_SubState"""
        assert event_m50_36_x195(z111=z111, z114=z115, z113=z112, z116=z117, z117=z116)
    """State 6: Rerun"""
    return 0

def event_m50_36_x198(z104=50361222, z105=40, z106=42, z107=80, z108=82, z109=3300020, z110=3300000):
    """[Preset] sliding fire-blowing cows_initialization version_Kenzawa 2F
    z104: Cow OBJ instance ID
    z105: OBJ state ID before operation
    z106: OBJ state ID after operation
    z107: OBJ state ID in operation from before operation
    z108: OBJ state ID that has been in operation since operation
    z109: Before operation_Navigation change point ID
    z110: After operation_navi change point ID
    """
    """State 0,3: [Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawayama 2F_SubState"""
    call = event_m50_36_x194(z104=z104, z105=z105, z106=z106, z107=z107, z108=z108, z109=z109, z110=z110)
    if call.Get() == 0:
        """State 1: [Conditions] Sliding fire-blowing cow_SubState"""
        assert event_m50_36_x81(z104=z104)
        """State 4: [Execution] Sliding fire-blowing cow_Kenzawa 2F_SubState"""
        assert event_m50_36_x196(z104=z104, z107=z107, z106=z106, z109=z109, z110=z110)
    elif call.Get() == 1:
        """State 2: [Condition] Sliding fire-blowing cow_2_SubState"""
        assert event_m50_36_x81(z104=z104)
        """State 5: [Execution] Sliding fired cow _Kenzawa 2F_2_SubState"""
        assert event_m50_36_x196(z104=z104, z107=z108, z106=z105, z109=z110, z110=z109)
    """State 6: Rerun"""
    return 0

def event_m50_36_x199():
    """[Condition] Continuous iron grid_Navigation change_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x200():
    """[Reproduction] 7 continuous iron grid versions"""
    """State 0,1: Navimesh: No traffic"""
    AddNavimeshAttribute(4001010, 2)
    AddNavimeshAttribute(4001020, 2)
    AddNavimeshAttribute(4001030, 2)
    AddNavimeshAttribute(4001040, 2)
    AddNavimeshAttribute(4001050, 2)
    AddNavimeshAttribute(4001060, 2)
    AddNavimeshAttribute(4001070, 2)
    AddNavimeshAttribute(4001080, 2)
    AddNavimeshAttribute(4001090, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x201(z103=536020017):
    """[Execution] 7 continuous iron grid version changes
    z103: Enemy activation flag
    """
    """State 0,1: Wait for the front bar to open"""
    CompareObjState(8, 50362051, 10, 1)
    CompareObjState(8, 50362052, 10, 1)
    assert ConditionGroup(8)
    """State 5: Navimesh switching: Allowed to pass"""
    DeleteNavimeshAttribute(4001010, 2)
    DeleteNavimeshAttribute(4001020, 2)
    """State 2: Wait for the front iron bar to open"""
    CompareObjState(8, 50362053, 10, 1)
    CompareObjState(8, 50362054, 10, 1)
    assert ConditionGroup(8)
    """State 6: Navi Mesh Switching: Allowed to pass_2"""
    DeleteNavimeshAttribute(4001030, 2)
    DeleteNavimeshAttribute(4001040, 2)
    """State 3: Wait for the iron grid in the center to open"""
    CompareObjState(8, 50362055, 10, 1)
    CompareObjState(8, 50362056, 10, 1)
    assert ConditionGroup(8)
    """State 7: Navi Mesh Switching: Passable_3"""
    DeleteNavimeshAttribute(4001050, 2)
    DeleteNavimeshAttribute(4001060, 2)
    """State 11: Wait for the innermost iron bar to open"""
    CompareObjState(8, 50362057, 10, 1)
    CompareObjState(8, 50362058, 10, 1)
    assert ConditionGroup(8)
    """State 12: Navi Mesh Switching: Passable_5"""
    DeleteNavimeshAttribute(4001070, 2)
    DeleteNavimeshAttribute(4001080, 2)
    """State 13: Enemy activation flag ON"""
    SetEventFlag(z103, 1)
    """State 4: Wait for the large bar to open"""
    CompareObjState(0, 50362050, 30, 0)
    CompareObjState(1, 50362050, 20, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 8: Navi Mesh Switching: Passable_4"""
        DeleteNavimeshAttribute(4001090, 2)
        """State 9: Wait for the large bar to close"""
        CompareObjState(0, 50362050, 20, 0)
        assert ConditionGroup(0)
    """State 10: Navi mesh switching: no traffic"""
    AddNavimeshAttribute(4001090, 2)
    """State 14: End state"""
    return 0

def event_m50_36_x202():
    """[Reproduction] Nine continuous iron grid versions"""
    """State 0,1: Navimesh: No traffic"""
    AddNavimeshAttribute(4101010, 2)
    AddNavimeshAttribute(4101020, 2)
    AddNavimeshAttribute(4101030, 2)
    AddNavimeshAttribute(4101040, 2)
    AddNavimeshAttribute(4101050, 2)
    AddNavimeshAttribute(4101060, 2)
    AddNavimeshAttribute(4101070, 2)
    AddNavimeshAttribute(4101080, 2)
    AddNavimeshAttribute(4101090, 2)
    AddNavimeshAttribute(4101100, 2)
    AddNavimeshAttribute(4101110, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x203(z102=536020019):
    """[Execution] Nine continuous iron grid version change
    z102: Enemy activation flag
    """
    """State 0,1: Wait for the front bar to open"""
    CompareObjState(8, 50362061, 10, 1)
    CompareObjState(8, 50362062, 10, 1)
    assert ConditionGroup(8)
    """State 5: Navimesh switching: Allowed to pass"""
    DeleteNavimeshAttribute(4101010, 2)
    DeleteNavimeshAttribute(4101020, 2)
    """State 2: Wait for the front iron bar to open"""
    CompareObjState(8, 50362063, 10, 1)
    CompareObjState(8, 50362064, 10, 1)
    assert ConditionGroup(8)
    """State 6: Navi Mesh Switching: Allowed to pass_2"""
    DeleteNavimeshAttribute(4101030, 2)
    DeleteNavimeshAttribute(4101040, 2)
    """State 11: Wait for the center bar to open"""
    CompareObjState(8, 50362065, 10, 1)
    CompareObjState(8, 50362066, 10, 1)
    assert ConditionGroup(8)
    """State 12: Navi Mesh Switching: Passable_3"""
    DeleteNavimeshAttribute(4101050, 2)
    DeleteNavimeshAttribute(4101060, 2)
    """State 3: Wait for the iron grid in the center to open"""
    CompareObjState(8, 50362067, 10, 1)
    CompareObjState(8, 50362068, 10, 1)
    assert ConditionGroup(8)
    """State 7: Navi Mesh Switching: Passable_4"""
    DeleteNavimeshAttribute(4101070, 2)
    DeleteNavimeshAttribute(4101080, 2)
    """State 13: Wait for the innermost iron bar to open"""
    CompareObjState(8, 50362069, 10, 1)
    CompareObjState(8, 50362070, 10, 1)
    assert ConditionGroup(8)
    """State 14: Navi Mesh Switching: Passable_6"""
    DeleteNavimeshAttribute(4101090, 2)
    DeleteNavimeshAttribute(4101100, 2)
    """State 15: Enemy activation flag ON"""
    SetEventFlag(z102, 1)
    """State 4: Wait for the large bar to open"""
    CompareObjState(0, 50362060, 30, 0)
    CompareObjState(1, 50362060, 20, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 8: Navi Mesh Switching: Passable_5"""
        DeleteNavimeshAttribute(4101110, 2)
        """State 9: Wait for the large bar to close"""
        CompareObjState(0, 50362060, 20, 0)
        assert ConditionGroup(0)
    """State 10: Navi mesh switching: no traffic"""
    AddNavimeshAttribute(4101110, 2)
    """State 16: End state"""
    return 0

def event_m50_36_x204(z103=536020017):
    """[Preset] 7 continuous iron grid version changes
    z103: Enemy activation flag
    """
    """State 0,1: [Reproduction] 7 continuous iron lattice versions_Navigation change_SubState"""
    assert event_m50_36_x200()
    """State 3: [Condition] Continuous iron grid_Navigation change_Empty_SubState"""
    assert event_m50_36_x199()
    """State 2: [Execution] 7 continuous iron grid versions_Navigation change_SubState"""
    assert event_m50_36_x201(z103=z103)
    """State 4: End state"""
    return 0

def event_m50_36_x205(z102=536020019):
    """[Preset] Nine continuous iron grid versions
    z102: Enemy activation flag
    """
    """State 0,1: [Reproduction] Nine continuous iron lattice versions_Navigation change_SubState"""
    assert event_m50_36_x202()
    """State 3: [Condition] Continuous iron grid_Navigation change_Empty_SubState"""
    assert event_m50_36_x199()
    """State 2: [Execution] Nine continuous iron grid version_Navigation change_SubState"""
    assert event_m50_36_x203(z102=z102)
    """State 4: End state"""
    return 0

def event_m50_36_x206(z90=536000081, z91=501, z92=5036000, z93=536020080, z94=6.3, z95=10, z96=5036001,
                      z97=536020083):
    """[Preset] knight battle of black smoke _ start
    z90: Boss destruction flag
    z91: Sound ID
    z92: First boss battle ID
    z93: Other flags for logic
    z94: Wait time
    z95: Boss starting distance
    z96: Rematch boss battle ID
    z97: BGM and gauge display flag
    """
    """State 0,1: [Reproduction] Black Smoke Knight Battle_Start_SubState"""
    call = event_m50_36_x207(z90=z90)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Knight of Black Smoke_Start_SubState"""
        call = event_m50_36_x208(z100=2000000, z101=2000000)
        if call.Get() == 0:
            """State 3: [Execution] Knight of Black Smoke_Start_SubState"""
            assert event_m50_36_x209(z92=z92)
            """State 7: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
            assert event_m50_36_x210()
            """State 9: [Condition] HP display, BGM playback and boss activation_SubState"""
            assert event_m50_36_x211(z98=903, z95=z95, z93=z93, z99=2000010)
            """State 8: [Execution] HP display, BGM playback and boss activation_SubState"""
            assert event_m50_36_x212(z91=z91, z93=z93, z94=z94, z92=z92, z97=z97)
            """State 2: [Reproduction] Knight of Black Smoke_End_Sky_SubState"""
            assert event_m50_36_x213()
            """State 6: [Condition] Knight of Black Smoke_End Judgment_SubState"""
            assert event_m50_36_x214(z92=z92)
            """State 4: [Execution] Knight of Black Smoke_End_SubState"""
            assert event_m50_36_x215(z91=z91, z92=z92, z93=z93)
        elif call.Get() == 1:
            """State 11: [Execution] Knight of Black Smoke_Start_2_SubState"""
            assert event_m50_36_x209(z92=z96)
            """State 14: [Reproduction] HP display and BGM playback and boss activation_empty_2_SubState"""
            assert event_m50_36_x210()
            """State 16: [Condition] HP display, BGM playback and boss activation_2_SubState"""
            assert event_m50_36_x211(z98=903, z95=z95, z93=z93, z99=2000010)
            """State 15: [Execution] HP display, BGM playback and boss activation_2_SubState"""
            assert event_m50_36_x212(z91=z91, z93=z93, z94=z94, z92=z96, z97=z97)
            """State 10: [Reproduction] Knight of Black Smoke_End_Sky_2_SubState"""
            assert event_m50_36_x213()
            """State 13: [Condition] Knight of Black Smoke_End Judgment_2_SubState"""
            assert event_m50_36_x214(z92=z96)
            """State 12: [Execution] Knight of Black Smoke_End_2_SubState"""
            assert event_m50_36_x215(z91=z91, z92=z96, z93=z93)
    """State 17: End state"""
    return 0

def event_m50_36_x207(z90=536000081):
    """[Reproduction] Black Smoke Knight Battle_Start
    z90: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z90) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_36_x208(z100=2000000, z101=2000000):
    """[Conditions] Black Smoke Knight Battle_Start
    z100: Start point ID
    z101: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z100, z101, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z100, z101, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: Has the black smoke knight been destroyed?"""
    CompareEventFlag(0, 101061, 0)
    if ConditionGroup(0):
        """State 3: Undefeated"""
        return 0
    else:
        """State 4: Defeated"""
        return 1

def event_m50_36_x209(z92=_):
    """[Execution] Knight of Black Smoke _Start
    z92: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z92)
    """State 2: End state"""
    return 0

def event_m50_36_x210():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x211(z98=903, z95=10, z93=536020080, z99=2000010):
    """[Condition] HP display, BGM playback and boss activation
    z98: Boss generator ID
    z95: Boss starting distance
    z93: Logic flag
    z99: Boss launch point
    """
    """State 0,1: Approach or damage at a certain distance or point intrusion or activated"""
    CompareChrPlayerDistance(0, z98, z95, 5)
    CompareChrHpRatio(0, z98, 100, 4)
    IsPlayerInsidePoint(0, z99, z99, 1)
    CompareEventFlag(0, z93, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x212(z91=501, z93=536020080, z94=6.3, z92=_, z97=536020083):
    """[Execution] HP display, BGM playback and boss activation
    z91: Sound ID
    z93: Logic flag
    z94: Wait time until display
    z92: Boss Battle ID
    z97: BGM and gauge display flag
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z93, 1)
    """State 4: Wait until BGM playback and HP display"""
    CompareStateTime(0, z94, 2, z94)
    CompareEventFlag(0, z97, 1)
    IsEventBossKill(1, z92, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z91)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 6: Camera parameter switching"""
    ChangeCameraParameters(675000, 3, 3)
    """State 5: BGM and gauge display flag ON"""
    SetEventFlag(z97, 1)
    """State 7: End state"""
    return 0

def event_m50_36_x213():
    """[Reproduction] Black smoke knight battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x214(z92=_):
    """[Condition] Black smoke knight battle_End judgment
    z92: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z92, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x215(z91=501, z92=_, z93=536020080):
    """[Execution] Black Smoke Knight Battle
    z91: Sound ID
    z92: Boss Battle ID
    z93: Other flags for logic
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z93, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z92)
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z91)
    assert (GetStateTime() > 6.5) != 0
    """State 4: Return camera parameters"""
    ResetCameraParameters()
    """State 5: End state"""
    return 0

def event_m50_36_x216(z89=536000024, z88=50367900):
    """[Reproduction] Obtaining a firestick
    z89: Item acquisition confirmation flag
    z88: Firestick OBJ instance ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Did you get the item?"""
    if GetEventFlag(z89) != 0:
        """State 4: It has been acquired"""
        return 1
    else:
        """State 3: Unacquired"""
        return 0
    """State 5: The guests"""
    Label('L0')
    return 2

def event_m50_36_x217(z88=50367900, goods1=53100000):
    """[Condition] Get a firestick
    z88: Firestick OBJ instance ID
    goods1: Item ID
    """
    """State 0,1: Have you checked out the sashimi?"""
    IsObjSearched(0, z88)
    assert ConditionGroup(0)
    """State 2: Can items be acquired?"""
    # goods:53100000:Scorching Iron Scepter
    if CanGetItem(goods1, 1) != 0:
        """State 3: Available"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m50_36_x218(z88=50367900, lot1=60014000, z89=536000024):
    """[Execution] Acquire a sashimi stick_Item acquisition
    z88: Firestick OBJ instance ID
    lot1: Lottery ID for item acquisition
    z89: Item acquisition confirmation flag
    """
    """State 0,4: Item acquisition PC action"""
    PlayerActionRequest(2)
    assert PlayerIsInEventAction(6) != 0
    """State 2: Item acquisition"""
    # lot:60014000:Scorching Iron Scepter
    AwardItem(lot1, 1)
    """State 3: Turn on the item acquisition flag"""
    SetEventFlag(z89, 1)
    """State 1: Get a stick: 70"""
    ChangeObjState(z88, 70)
    """State 5: End state"""
    return 0

def event_m50_36_x219(z88=50367900, lot1=60014000):
    """[Execution] Acquire a sashimi stick_Item acquisition not possible
    z88: Firestick OBJ instance ID
    lot1: Lottery ID for item acquisition
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z88, 1)
    """State 2: Acquisition failure window display"""
    # lot:60014000:Scorching Iron Scepter
    DisplayItemAwardFailure(lot1, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 3: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z88, 0)
    """State 5: End state"""
    return 0

def event_m50_36_x220(z88=50367900, lot1=60014000, z89=536000024, goods1=53100000):
    """[Preset] Get a firestick
    z88: Firestick OBJ instance ID
    lot1: Lottery ID for item acquisition
    z89: Item acquisition confirmation flag
    goods1: Acquisition judgment item ID
    """
    """State 0,1: [Reproduction] _SubState to obtain a sashimi stick"""
    call = event_m50_36_x216(z89=z89, z88=z88)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] _SubState to get a sashimi stick"""
        call = event_m50_36_x217(z88=z88, goods1=goods1)
        if call.Done():
            """State 2: [Execution] Get a sashimi stick_Item acquisition_SubState"""
            assert event_m50_36_x218(z88=z88, lot1=lot1, z89=z89)
        elif call.Done():
            """State 3: [Execution] Obtaining a firestick_Item not available_SubState"""
            assert event_m50_36_x219(z88=z88, lot1=lot1)
            """State 6: Rerun"""
            return 1
    elif call.Get() == 2:
        pass
    """State 5: Finish"""
    return 0

def event_m50_36_x221(z87=_):
    """[Preset] Fire the corpse
    z87: Corpse OBJ instance ID
    """
    """State 0,1: [Reproduction] _SubState to ignite the corpse"""
    call = event_m50_36_x222(z87=z87)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] _SubState to ignite the corpse"""
        call = event_m50_36_x223(z87=z87)
        if call.Get() == 0:
            """State 2: [Execution] _SubState to ignite the corpse"""
            assert event_m50_36_x224(z87=z87)
        elif call.Get() == 1:
            """State 5: Rerun"""
            return 1
    """State 4: End state"""
    return 0

def event_m50_36_x222(z87=_):
    """[Reproduction] Fire the corpse
    z87: Corpse OBJ instance ID
    """
    """State 0,1: Ignition judgment of corpse"""
    if CompareObjStateId(z87, 40, 0):
        """State 3: Ignited"""
        Label('L0')
        return 1
    elif CompareObjStateId(z87, 42, 0):
        Goto('L0')
    else:
        """State 2: Unignited"""
        return 0

def event_m50_36_x223(z87=_):
    """[Condition] Light the corpse
    z87: Corpse OBJ instance ID
    """
    """State 0,1: Determining corpse status"""
    if CompareObjStateId(z87, 30, 0):
        """State 2: With key guide"""
        Label('L0')
        CompareObjState(0, z87, 70, 0)
        CompareObjState(0, z87, 40, 0)
        CompareObjState(0, z87, 42, 0)
        IsPlayerUsingTorch(8, 0)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 4: Transition to no key guide: 10"""
            ChangeObjState(z87, 10)
            CompareObjState(0, z87, 30, 1)
            assert ConditionGroup(0)
            """State 7: Rerun"""
            return 1
    else:
        """State 3: Without key guide"""
        CompareObjState(0, z87, 40, 0)
        CompareObjState(0, z87, 42, 0)
        CompareObjState(0, z87, 70, 0)
        IsPlayerUsingTorch(8, 1)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 5: Transition to key guide existence: 30"""
            ChangeObjState(z87, 30)
            Goto('L0')
    """State 6: Dead body: Lit"""
    return 0

def event_m50_36_x224(z87=_):
    """[Execution] Ignite the corpse
    z87: Corpse OBJ instance ID
    """
    """State 0,1: Lights up: 70"""
    ChangeObjState(z87, 70)
    """State 2: Waiting for lighting"""
    CompareObjState(0, z87, 40, 0)
    CompareObjState(0, z87, 42, 0)
    assert ConditionGroup(0)
    """State 3,4: End state"""
    return 0

def event_m50_36_x225(z83=536000049, z84=536000048):
    """[Reproduction] Smoke fog and light change by the image of a spider
    z83: Isolated island_destruction flag
    z84: Lobby_Destroy flag
    """
    """State 0,1: Are both eagle statues destroyed?"""
    if GetEventFlag(z83) != 0 and GetEventFlag(z84) != 0:
        """State 2: Destroyed"""
        return 0
    else:
        """State 3: Not destroyed"""
        return 1

def event_m50_36_x226(z85=22, z86=32, z83=536000049, z84=536000048):
    """[Condition] Smoke fog and light change by the image of the frog
    z85: Isolated island_internal hit group ID
    z86: Lobby_Internal hit group ID
    z83: Isolated island_destruction flag
    z84: Lobby_Destroy flag
    """
    """State 0,1: Can you see the smoke area?"""
    IsPlayerOnHitGroup(8, z85, 1)
    CompareEventFlag(8, z83, 0)
    IsPlayerOnHitGroup(9, z86, 1)
    CompareEventFlag(9, z84, 0)
    CompareEventFlag(10, z83, 1)
    CompareEventFlag(10, z84, 1)
    if ConditionGroup(8):
        """State 2: Isolated island: Inside the smoke area"""
        return 0
    elif ConditionGroup(9):
        """State 3: Lobby: Inside the smoke area"""
        return 1
    elif ConditionGroup(10):
        """State 4: Both eagle statues broke"""
        return 2

def event_m50_36_x227(val2=_, z85=_, z83=_):
    """[Execution] Smoke fog and light change by the image of the frog
    val2: Fog filter ID
    z85: Internal hit group ID
    z83: Destruction flag
    """
    """State 0,2: Filter status judgment"""
    if (GetFogFilterOverride() == val2) != 1:
        """State 1: Push filter"""
        PushFogFilter(val2, 0.5)
        assert (GetFogFilterOverride() == val2) != 0
    else:
        pass
    """State 3: Can you see the smoke area? Did you destroy the eagle statue?"""
    IsPlayerOnHitGroup(0, z85, 0)
    CompareEventFlag(1, z83, 1)
    if ConditionGroup(0):
        """State 4: Outside area: Pop filter"""
        PopFogFilter(0.5)
        """State 5: Waiting for pop"""
        assert (GetFogFilterOverride() == val2) != 1
    elif ConditionGroup(1):
        """State 6: Destroy statue: pop filter"""
        PopFogFilter(5)
        """State 7: Waiting for pop_2"""
        assert (GetFogFilterOverride() == val2) != 1
    """State 8: Rerun"""
    return 0

def event_m50_36_x228(z83=536000049, z84=536000048, z85=22, z86=32, val2=14, val3=15):
    """[Preset] Smoke fog and light change by the image of a spider
    z83: Isolated island_destruction flag
    z84: Lobby_Destroy flag
    z85: Isolated island_internal hit group ID
    z86: Lobby_Internal hit group ID
    val2: Isolated island_Fog filter ID
    val3: Lobby_Fog Filter ID
    """
    """State 0,1: [Reproduction] Smoke fog and light change due to the image of a spider _SubState"""
    call = event_m50_36_x225(z83=z83, z84=z84)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 3: [Condition] Smoke fog and light change by the image of a spider _SubState"""
    call = event_m50_36_x226(z85=z85, z86=z86, z83=z83, z84=z84)
    if call.Get() == 0:
        """State 2: [Execution] Smoke fog and light change by the image of a spider _SubState"""
        assert event_m50_36_x227(val2=val2, z85=z85, z83=z83)
    elif call.Get() == 1:
        """State 4: [Execution] Smoke fog and light change by sculpture image_2_SubState"""
        assert event_m50_36_x227(val2=val3, z85=z86, z83=z84)
    """State 6: Rerun"""
    return 1
    """State 5: Finish"""
    Label('L0')
    return 0

def event_m50_36_x229(z79=50363040, z80=50361500, z81=50361510, z82=50363100):
    """[Reproduction] Facility operation direction
    z79: Active OBJ instance ID
    z80: Cow OBJ instance ID
    z81: Steam OBJ instance ID
    z82: Armor OBJ instance ID
    """
    """State 0,9: Has the event been executed?"""
    if GetEventFlag(536000010) != 0:
        """State 20: Changed central pillar steam to permanent: 20"""
        ChangeObjState(z81, 20)
        """State 3: Event light switching 2"""
        SetPointLightEnabled(50360000, 1, 0)
        SetPointLightEnabled(50360020, 1, 0)
        SetPointLightEnabled(50360100, 0, 0)
    else:
        """State 1: Is there a stab stick?"""
        if CompareObjStateId(z79, 20, 0):
            """State 10: Cattle initial state judgment"""
            if CompareObjStateId(z80, 10, 0):
                """State 4: The cow starts to fire: 70"""
                ChangeObjState(z80, 70)
                """State 12: weight"""
                Label('L0')
                assert (GetStateTime() > 3) != 0
                """State 5: Light on steam on central pillar: 70"""
                Label('L1')
                ChangeObjState(z81, 70)
                SetPointLightEnabled(50360000, 1, 0.5)
                SetPointLightEnabled(50360020, 1, 0.5)
                """State 15: Weight 2"""
                Label('L2')
                assert (GetStateTime() > 2) != 0
                """State 7: Cattle stop: 20"""
                ChangeObjState(z80, 20)
                """State 8: Armor OBJ launch: 70"""
                Label('L3')
                ChangeObjState(z82, 70)
                CompareStateTime(0, 10, 3, 10)
                """State 17: Weight 3"""
                Label('L4')
                assert (GetStateTime() > 10) != 0
            else:
                """State 13: Cattle action state judgment"""
                if CompareObjStateId(z80, 70, 0):
                    Goto('L0')
                else:
                    """State 11: Central column initial state judgment"""
                    if CompareObjStateId(z81, 10, 0):
                        Goto('L1')
                    else:
                        """State 19: Light reproduction"""
                        SetPointLightEnabled(50360000, 1, 0.5)
                        SetPointLightEnabled(50360020, 1, 0.5)
                        SetPointLightEnabled(50360100, 0, 1)
                        """State 14: Cattle end determination"""
                        if CompareObjStateId(z80, 20, 1):
                            Goto('L2')
                        else:
                            """State 16: Armor initial state judgment"""
                            if CompareObjStateId(z82, 10, 0):
                                Goto('L3')
                            else:
                                """State 18: Armor action state judgment"""
                                if CompareObjStateId(z82, 70, 0):
                                    Goto('L4')
                                else:
                                    pass
            """State 6: All elevator operating flag ON"""
            SetEventFlag(536000010, 1)
        else:
            """State 2: Event light switching"""
            SetPointLightEnabled(50360000, 0, 0)
            SetPointLightEnabled(50360020, 0, 0)
            SetPointLightEnabled(50360100, 1, 0)
            """State 21: Not executed"""
            return 0
    """State 22: Already in operation"""
    return 1

def event_m50_36_x230(z79=50363040):
    """[Condition] Facility operation direction
    z79: Active OBJ instance ID
    """
    """State 0,1: Fire stab stick insertion judgment"""
    CompareObjState(0, z79, 20, 0)
    assert ConditionGroup(0)
    """State 2: Elevator operation"""
    return 0

def event_m50_36_x231(z79=50363040, z80=50361500, z81=50361510, z82=50363100):
    """[Execution] Facility operation direction
    z79: Active OBJ instance ID
    z80: Cattle ①_OBJ instance ID
    z81: Steam OBJ instance ID
    z82: Armor OBJ instance ID
    """
    """State 0,1: Cow 1 starts to fire: 70"""
    ChangeObjState(z80, 70)
    CompareStateTime(0, 3, 3, 3)
    assert ConditionGroup(0)
    """State 2: Light switching Steam on central pillar: 70"""
    ChangeObjState(z81, 70)
    CompareStateTime(0, 2, 3, 2)
    SetPointLightEnabled(50360000, 1, 0.5)
    SetPointLightEnabled(50360020, 1, 0.5)
    SetPointLightEnabled(50360100, 0, 1)
    assert ConditionGroup(0)
    """State 4: Cattle stop: 20"""
    ChangeObjState(z80, 20)
    """State 5: Armor OBJ launch: 70"""
    ChangeObjState(z82, 70)
    CompareStateTime(0, 10, 3, 10)
    assert ConditionGroup(0)
    """State 3: All elevator operating flag ON"""
    SetEventFlag(536000010, 1)
    """State 6: End state"""
    return 0

def event_m50_36_x232(z79=50363040, z80=50361500, z81=50361510, z82=50363100):
    """[Preset] Facility operation direction
    z79: Active OBJ instance ID
    z80: Cattle ①_OBJ instance ID
    z81: Steam OBJ instance ID
    z82: Armor OBJ instance ID
    """
    """State 0,1: [Reproduction] Facility operation production_SubState"""
    call = event_m50_36_x229(z79=z79, z80=z80, z81=z81, z82=z82)
    if call.Get() == 0:
        """State 3: [Condition] Facility operation direction_SubState"""
        assert event_m50_36_x230(z79=z79)
        """State 2: [Execution] Facility Operation Direction_SubState"""
        assert event_m50_36_x231(z79=z79, z80=z80, z81=z81, z82=z82)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x233(z17=_):
    """[Reproduction] Storm of darkness by the image of a spear
    z17: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(z17) != 0:
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Not destroyed"""
        return 0

def event_m50_36_x234(z74=536000051, z76=50361111, z77=91, z78=31, z75=50361611):
    """[Condition] Storm of darkness caused by a statue of a spear
    z74: Destruction flag
    z76: 像 image OBJ instance ID
    z77: Samurai Statue_Activation Confirmed OBJ State ID
    z78: Saddle Statue_OBJ State ID after cancellation
    z75: Dark Storm OBJ Instance ID
    """
    """State 0,1: Waiting for the spear statue to appear or waiting for destruction"""
    CompareObjState(0, z76, z78, 0)
    CompareEventFlag(1, z74, 1)
    CompareObjState(1, z76, z77, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 2: Dark Storm Activated: 30"""
        ChangeObjState(z75, 30)
        """State 3: Waiting for destruction of eagle statue"""
        CompareEventFlag(0, z74, 1)
        CompareObjState(0, z76, z77, 0)
        assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_36_x235(z18=_):
    """[Execution] Storm of darkness caused by a spear image
    z18: Dark Storm OBJ Instance ID
    """
    """State 0,1: End of Dark Storm: 20"""
    ChangeObjState(z18, 20)
    """State 2: End state"""
    return 0

def event_m50_36_x236(z74=536000051, z75=50361611, z76=50361111, z77=91, z78=31):
    """[Preset] Storm of darkness by the image of a spear
    z74: Destruction flag
    z75: Dark Storm OBJ Instance ID
    z76: 像 image OBJ instance ID
    z77: Samurai Statue_Activation Confirmed OBJ State ID
    z78: Saddle Statue_OBJ State ID after cancellation
    """
    """State 0,1: [Reproduction] Dark storm _SubState by a spear image"""
    call = event_m50_36_x233(z17=z74)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Dark storm _SubState"""
        assert event_m50_36_x234(z74=z74, z76=z76, z77=z77, z78=z78, z75=z75)
    """State 2: [Execution] Storm of Darkness by Subaru Statue_SubState"""
    assert event_m50_36_x235(z18=z75)
    """State 4: End state"""
    return 0

def event_m50_36_x237():
    """[Reproduction] Destructive variable reset of eagle image"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_36_x238():
    """[Condition] Destruction variable reset of the eagle image_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x239(z73=1):
    """[Execution] Destruction variable reset of eagle statue
    z73: The number of destruction
    """
    """State 0,1: Initializing area variables"""
    SetAreaVariable(z73, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x240(z73=1):
    """[Preset] Destruction variable reset
    z73: The number of destruction
    """
    """State 0,1: [Reproduction] Destruction variable reset of the spider image_SubState"""
    call = event_m50_36_x237()
    if call.Get() == 0:
        """State 3: [Condition] Destruction variable reset of moth image_empty_SubState"""
        assert event_m50_36_x238()
        """State 2: [Execution] Destruction variable reset of the eagle image_SubState"""
        assert event_m50_36_x239(z73=z73)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x241(z70=38000):
    """[Reproduction] Addition of destructive variables for the eagle image
    z70: Reset event ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Has the reset event ended?"""
        assert EventEnded(z70) != 0
        """State 3: host"""
        return 0
    else:
        """State 4: The guests"""
        return 1

def event_m50_36_x242(z71=_):
    """[Conditions] Addition of destruction variables for the statue
    z71: Destruction flag
    """
    """State 0,1: Waiting for destruction of eagle statue"""
    CompareEventFlag(0, z71, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x243(z72=1):
    """[Execution] Addition of destructive variables for the statue
    z72: Number of destruction
    """
    """State 0,1: Number of spear statue destruction +1"""
    AddAreaVariable(z72, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x244(z70=38000, z71=_, z72=1):
    """[Preset] Addition of destruction variable of eagle image
    z70: Reset event ID
    z71: Destruction flag
    z72: Number of destruction
    """
    """State 0,1: [Reproduction] Destructive variable addition of eagle image_SubState"""
    call = event_m50_36_x241(z70=z70)
    if call.Get() == 0:
        """State 3: [Condition] Destructive variable addition of sculpture image_SubState"""
        assert event_m50_36_x242(z71=z71)
        """State 2: [Execution] Addition of destructive variables for the image of the spider"""
        assert event_m50_36_x243(z72=z72)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x245():
    """[Reproduction] Judgment of the number of spear images"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_36_x246(z64=1, z65=_):
    """[Conditions] Judgment of number of destruction
    z64: Number of destruction
    z65: Comparison number of destruction
    """
    """State 0,1: Destruction count"""
    CompareEventFlagValue(0, 1, z64, z65, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x247(z66=536000039):
    """[Execution] Judgment of the number of spear images
    z66: 1 remaining flag
    """
    """State 0,1: 1 remaining flag ON"""
    SetEventFlag(z66, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x248(z64=1, z65=10, z66=536000039, z67=11, z68=536000059, z69=100710):
    """[Preset] Judgment of the number of spears
    z64: Number of destruction
    z65: Comparison number of destruction
    z66: 1 remaining flag
    z67: Total destruction comparison number
    z68: All destruction flag
    z69: All destruction global flag
    """
    """State 0,1: [Reproduction] Judgment of the number of spears"""
    call = event_m50_36_x245()
    if call.Get() == 0:
        """State 3: [Condition] Judgment of the number of spears"""
        assert event_m50_36_x246(z64=z64, z65=z65)
        """State 2: [Execution] Judgment of the number of spears"""
        assert event_m50_36_x247(z66=z66)
        """State 5: [Reproduction] Judgment of the number of spears_empty_SubState"""
        assert event_m50_36_x249()
        """State 4: [Condition] Judgment of the number of spears"""
        assert event_m50_36_x246(z64=z64, z65=z67)
        """State 6: [Execution] Judgment of the number of spears"""
        assert event_m50_36_x250(z68=z68, z69=z69)
    elif call.Get() == 1:
        pass
    """State 7: End state"""
    return 0

def event_m50_36_x249():
    """[Reproduction] Judgment image destruction number determination_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x250(z68=536000059, z69=100710):
    """[Execution] Judgment of the number of spears
    z68: All destruction flag
    z69: All destruction global flag
    """
    """State 0,1: All destruction flag ON"""
    SetEventFlag(z68, 1)
    SetEventFlag(z69, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x251(z61=50360410, z62=700000, z63=536000027):
    """[Execution] Large door opened by lever_Enemy activation
    z61: Door OBJ instance ID
    z62: Navigation change point ID
    z63: Enemy activation flag
    """
    """State 0,2: The big door opens: 70"""
    ChangeObjState(z61, 70)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z61, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z62, 2)
    """State 4: Enemy activation flag ON"""
    SetEventFlag(z63, 1)
    """State 5: End state"""
    return 0

def event_m50_36_x252(z61=50360410, z62=700000, z63=536000027):
    """[Reproduction] Large door opened by lever_Enemy activation
    z61: Door OBJ instance ID
    z62: Navigation change point ID
    z63: Enemy activation flag
    """
    """State 0,1: Is the big door open?"""
    if CompareObjStateId(z61, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z61, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z62, 2)
        """State 4: Enemy activation flag ON"""
        SetEventFlag(z63, 1)
        """State 6: Already in operation"""
        return 1
    else:
        """State 5: Not in operation"""
        return 0

def event_m50_36_x253(z60=50361024, z61=50360410, z62=700000, z63=536000027):
    """[Preset] Large door opened by lever_Enemy activation
    z60: Lever OBJ instance ID
    z61: Door OBJ instance ID
    z62: Navigation change point ID
    z63: Enemy activation flag
    """
    """State 0,2: [Reproduction] Large door opened by lever_Enemy activation_SubState"""
    call = event_m50_36_x252(z61=z61, z62=z62, z63=z63)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Large door opened with lever_SubState"""
        assert event_m50_36_x96(z60=z60)
        """State 3: [Execution] Large door opened by lever_Enemy activation_SubState"""
        assert event_m50_36_x251(z61=z61, z62=z62, z63=z63)
    """State 4: End state"""
    return 0

def event_m50_36_x254(z59=_):
    """[Reproduction] Inter-DLC event_C route clear
    z59: Achievement flag
    """
    """State 0,1: Already cleared?"""
    if GetEventFlag(z59) != 0:
        """State 3: Cleared"""
        return 1
    else:
        """State 2: Not cleared"""
        return 0

def event_m50_36_x255(z58=_):
    """[Conditions] Inter-DLC event_C route clear
    z58: Boss destruction flag
    """
    """State 0,1: Boss destruction waiting"""
    CompareEventFlag(0, z58, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x256(z59=_):
    """[Execution] Inter-DLC event_C route clear
    z59: Achievement flag
    """
    """State 0,1: Clear flag ON"""
    SetEventFlag(z59, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x257(z58=_, z59=_):
    """[Preset] Inter-DLC event_C route clear
    z58: Boss destruction flag
    z59: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_C route clear_SubState"""
    call = event_m50_36_x254(z59=z59)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Inter-DLC event_C route clear_SubState"""
        assert event_m50_36_x255(z58=z58)
        """State 2: [Execution] Inter-DLC event_C route clear_SubState"""
        assert event_m50_36_x256(z59=z59)
    """State 4: End state"""
    return 0

def event_m50_36_x258(z51=536020004, z57=536020002):
    """[Execution] Continuous intrusion_1 body
    z51: Generation flag ①
    z57: Event execution flag_1
    """
    """State 0,4: Execution flag ON"""
    SetEventFlag(z57, 1)
    """State 1: Network FE display"""
    OpenNetworkMessageMenu(9000, 0, 0, 0)
    """State 3: Generate weight 1"""
    CompareStateTime(0, 0, 3, 0)
    assert ConditionGroup(0)
    """State 2: Generation flag 1 ON"""
    SetEventFlag(z51, 1)
    """State 5: End state"""
    return 0

def event_m50_36_x259():
    """[Reproduction] Continuous intrusion_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x260(z52=536020005, z53=536020006, z54=536020007, z55=536020008, z56=536020003):
    """[Execution] Continuous intrusion_2
    z52: Generation flag ②
    z53: Generation flag ③
    z54: Generation flag (4)
    z55: Generation flag ⑤
    z56: Event executed flag_2
    """
    """State 0,9: Execution flag ON"""
    SetEventFlag(z56, 1)
    """State 5: Generation weight 2"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 1: Generation flag 2 ON"""
    SetEventFlag(z52, 1)
    """State 6: Generate weight 3"""
    CompareStateTime(0, 1, 3, 1)
    assert ConditionGroup(0)
    """State 2: Generation flag 3 ON"""
    SetEventFlag(z53, 1)
    """State 7: Generation weight 4"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 3: Generation flag 4 ON"""
    SetEventFlag(z54, 1)
    """State 8: Generate weight 5"""
    CompareStateTime(0, 0.8, 3, 0.8)
    assert ConditionGroup(0)
    """State 4: Generation flag 5 ON"""
    SetEventFlag(z55, 1)
    """State 10: End state"""
    return 0

def event_m50_36_x261(z49=50361130, z50=3700000):
    """[Reproduction] The image of a half-broken coral collapses
    z49: Half gangrene statue OBJ instance ID
    z50: Navigation change point ID
    """
    """State 0,1: Is it already broken?"""
    if CompareObjStateId(z49, 20, 0):
        """State 3: Navigation change: Allowed to pass"""
        DeleteNavimeshAttribute(z50, 2)
        """State 5: Destroyed"""
        return 1
    else:
        """State 2: Navigation change: No traffic"""
        AddNavimeshAttribute(z50, 2)
        """State 4: Undestructed"""
        return 0

def event_m50_36_x262(z48=50368800):
    """[Condition] The image of the half-broken coral collapses
    z48: Item OBJ instance ID
    """
    """State 0,1: Did you get the item?"""
    WasObjItemAcquired(0, z48, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x263(z49=50361130, z50=3700000):
    """[Execution] The image of the half-broken cocoon collapses
    z49: Half gangrene statue OBJ instance ID
    z50: Navigation change point ID
    """
    """State 0,1: The image of a spider collapses"""
    DestroyObj(z49, z49, 0)
    """State 2: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z50, 2)
    """State 3: End state"""
    return 0

def event_m50_36_x264(z48=50368800, z49=50361130, z50=3700000):
    """[Preset] The image of a half-broken spear collapses
    z48: Item OBJ instance ID
    z49: Half gangrene statue OBJ instance ID
    z50: Navigation change point ID
    """
    """State 0,1: [Reproduction] _SubState where the image of a half-broken spear collapses"""
    call = event_m50_36_x261(z49=z49, z50=z50)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] _SubState where the image of the half-broken spear collapses"""
        assert event_m50_36_x262(z48=z48)
        """State 2: [Execution] The image of the half-broken cocoon collapses"""
        assert event_m50_36_x263(z49=z49, z50=z50)
    """State 4: End state"""
    return 0

def event_m50_36_x265(z45=536000024):
    """[Condition] The fire in the other tower disappears
    z45: Firestick acquisition flag
    """
    """State 0,1: Did you get a firestick?"""
    CompareEventFlag(0, z45, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x266(z45=536000024, z46=3020, z47=50360060):
    """[Execution] The fire of another tower disappears
    z45: Firestick acquisition flag
    z46: Event SFXID
    z47: Event light ID
    """
    """State 0,1: Event SFX OFF"""
    StopSfxAtPoint(z46)
    """State 2: Event light OFF"""
    SetPointLightEnabled(z47, 0, 0.5)
    """State 3: End state"""
    return 0

def event_m50_36_x267(z45=536000024, z46=3020, z47=50360060):
    """[Reproduction] The fire of another tower disappears
    z45: Firestick acquisition flag
    z46: Event SFXID
    z47: Event light ID
    """
    """State 0,1: Have you got a firestick?"""
    if GetEventFlag(z45) != 0:
        """State 3: Event SFX OFF"""
        StopSfxAtPoint(z46)
        """State 5: Event light OFF"""
        SetPointLightEnabled(z47, 0, 0)
        """State 7: Obtained"""
        return 1
    else:
        """State 2: Event SFX ON"""
        PlaySfxAtPoint(z46)
        """State 4: Event light ON"""
        SetPointLightEnabled(z47, 1, 0)
        """State 6: I have not obtained"""
        return 0

def event_m50_36_x268(z45=536000024, z46=3020, z47=50360060):
    """[Preset] The fire of another tower disappears
    z45: Firestick acquisition flag
    z46: Event SFXID
    z47: Event light ID
    """
    """State 0,1: [Reproduction] The fire of another tower disappears_SubState"""
    call = event_m50_36_x267(z45=z45, z46=z46, z47=z47)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] The fire of another tower disappears_SubState"""
        assert event_m50_36_x265(z45=z45)
        """State 2: [Execution] The fire of another tower disappears_SubState"""
        assert event_m50_36_x266(z45=z45, z46=z46, z47=z47)
    """State 4: End state"""
    return 0

def event_m50_36_x269(z44=_):
    """[Reproduction] Navi change by destroying salamander
    z44: Navigation change point ID
    """
    """State 0,1: Navimesh not allowed"""
    AddNavimeshAttribute(z44, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x270(z43=_):
    """[Condition] Change navigation by destroying salamander
    z43: Generator ID
    """
    """State 0,1: Salamander defeat judgment"""
    IsChrDeadOrRespawnOver(0, z43, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x271(z44=_):
    """[Execution] Change navigation by destroying salamander
    z44: Navigation change point ID
    """
    """State 0,1: Navigation mesh traffic is possible"""
    DeleteNavimeshAttribute(z44, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x272(z43=_, z44=_):
    """[Preset] Change navigation by destroying salamander
    z43: Generator ID
    z44: Navigation change point ID
    """
    """State 0,1: [Reproduction] Navi change by destroying Salamander_SubState"""
    assert event_m50_36_x269(z44=z44)
    """State 3: [Condition] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x270(z43=z43)
    """State 2: [Execution] Navi change by destroying Salamander_SubState"""
    assert event_m50_36_x271(z44=z44)
    """State 4: End state"""
    return 0

def event_m50_36_x273(z39=536000024, z40=50361530, z41=50360040):
    """[Reproduction] Furnace in another tower stops
    z39: Sashimi get flag
    z40: Reactor OBJ instance ID
    z41: Event light ID
    """
    """State 0,1: Have you already obtained a firestick?"""
    if GetEventFlag(z39) != 0:
        """State 4: Furnace flame extinguished: 20"""
        ChangeObjState(z40, 20)
        """State 5: Event light OFF"""
        SetPointLightEnabled(z41, 0, 0)
        """State 7: Item acquired"""
        return 1
    else:
        """State 2: Furnace flames lit: 10"""
        ChangeObjState(z40, 10)
        """State 3: Event light ON"""
        SetPointLightEnabled(z41, 1, 0)
        """State 6: Waiting for item acquisition"""
        return 0

def event_m50_36_x274(z39=536000024):
    """[Condition] Furnace in another tower stops
    z39: Sashimi get flag
    """
    """State 0,1: Did you get a firestick?"""
    CompareEventFlag(0, z39, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x275(z40=50361530, z41=50360040, z42=1.5):
    """[Execution] The furnace in the other tower stops
    z40: Reactor OBJ instance ID
    z41: Event light ID
    z42: Unlit weight
    """
    """State 0,3: weight"""
    CompareStateTime(0, z42, 3, z42)
    assert ConditionGroup(0)
    """State 1: Furnace flame extinguished: 20"""
    ChangeObjState(z40, 20)
    """State 2: Event light OFF"""
    SetPointLightEnabled(z41, 0, 0.5)
    """State 4: End state"""
    return 0

def event_m50_36_x276(z39=536000024, z40=50361530, z41=50360040, z42=1.5):
    """[Preset] Furnace in another tower stops
    z39: Sashimi get flag
    z40: Reactor OBJ instance ID
    z41: Event light ID
    z42: Unlit weight
    """
    """State 0,1: [Reproduction] Furnace in another tower stops_SubState"""
    call = event_m50_36_x273(z39=z39, z40=z40, z41=z41)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Furnace in another tower stops_SubState"""
        assert event_m50_36_x274(z39=z39)
        """State 2: [Execution] Furnace in another tower stops_SubState"""
        assert event_m50_36_x275(z40=z40, z41=z41, z42=z42)
    """State 4: Finish"""
    return 0

def event_m50_36_x277(z36=536000024, z37=1, z38=2):
    """[Reproduction] The light of another tower disappears
    z36: Firestick acquisition flag
    z37: Light _part group ID
    z38: No light_Parts group ID
    """
    """State 0,1: Have you got a firestick?"""
    if GetEventFlag(z36) != 0:
        """State 3: Map parts switching: no light"""
        SetMapPartDisplay(z37, 0)
        SetMapPartDisplay(z38, 1)
        """State 5: Obtained"""
        return 1
    else:
        """State 2: Map parts change: There is light"""
        SetMapPartDisplay(z37, 1)
        SetMapPartDisplay(z38, 0)
        """State 4: I have not obtained"""
        return 0

def event_m50_36_x278(z36=536000024):
    """[Conditions] The light of the other tower disappears
    z36: Firestick acquisition flag
    """
    """State 0,1: Did you get a firestick?"""
    CompareEventFlag(0, z36, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x279(z36=536000024, z37=1, z38=2):
    """[Execution] The light of the other tower disappears
    z36: Firestick acquisition flag
    z37: Light _part group ID
    z38: No light_Parts group ID
    """
    """State 0,1: Map parts switching: no light"""
    SetMapPartDisplay(z37, 0)
    SetMapPartDisplay(z38, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x280(z36=536000024, z37=1, z38=2):
    """[Preset] The light of the other tower disappears
    z36: Firestick acquisition flag
    z37: Light _part group ID
    z38: No light_Parts group ID
    """
    """State 0,1: [Reproduction] The light of another tower disappears _SubState"""
    call = event_m50_36_x277(z36=z36, z37=z37, z38=z38)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] The light of another tower disappears_SubState"""
        assert event_m50_36_x278(z36=z36)
        """State 2: [Execution] Light of the other tower disappears_SubState"""
        assert event_m50_36_x279(z36=z36, z37=z37, z38=z38)
    """State 4: End state"""
    return 0

def event_m50_36_x281(z33=1404000, z34=1404010):
    """[Reproduction] Elevator navigation switching
    z33: Navigation change point_on
    z34: Navigation change point under
    """
    """State 0,1: Navi mesh switching: Not allowed"""
    AddNavimeshAttribute(z33, 2)
    AddNavimeshAttribute(z34, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x282(z32=50361330):
    """[Condition] Elevator navigation switching
    z32: Elevator OBJ instance ID
    """
    """State 0,1: Elevator state judgment"""
    CompareObjState(0, z32, 40, 0)
    CompareObjState(1, z32, 10, 0)
    if ConditionGroup(0):
        """State 3: The elevator is on top"""
        return 1
    elif ConditionGroup(1):
        """State 2: The elevator is below"""
        return 0

def event_m50_36_x283(z32=50361330, z33=_, z34=_, z35=_):
    """[Execution] Elevator navigation switching
    z32: Elevator OBJ instance ID
    z33: Passable point
    z34: Impassable points
    z35: Elevator stop OBJ state ID
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z33, 2)
    AddNavimeshAttribute(z34, 2)
    """State 2: Building operation standby"""
    CompareObjState(0, z32, z35, 1)
    assert ConditionGroup(0)
    """State 3: Finish"""
    return 0

def event_m50_36_x284(z32=50361330, z33=1404000, z34=1404010):
    """[Preset elevator navigation switching
    z32: Elevator OBJ instance ID
    z33: Navigation change point_on
    z34: Navigation change point under
    """
    """State 0,1: [Reproduction] Elevator navigation switching_SubState"""
    assert event_m50_36_x281(z33=z33, z34=z34)
    """State 3: [Condition] Elevator navigation switching_SubState"""
    call = event_m50_36_x282(z32=z32)
    if call.Get() == 1:
        """State 2: [Execute] Elevator navigation switching_SubState"""
        assert event_m50_36_x283(z32=z32, z33=z33, z34=z34, z35=40)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator navigation switching_2_SubState"""
        assert event_m50_36_x283(z32=z32, z33=z34, z34=z33, z35=10)
    """State 5: Rerun"""
    return 0

def event_m50_36_x285(z29=536000086, z30=536020087):
    """[Reproduction] Oriental knight's gut determination
    z29: Boss destruction flag
    z30: Gag stop flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: Has the boss been destroyed?"""
        if GetEventFlag(z29) != 0:
            pass
        else:
            """State 3: Canceled suffocation flag OFF"""
            SetEventFlag(z30, 0)
            """State 4: host"""
            return 0
    else:
        pass
    """State 5: Finish"""
    return 1

def event_m50_36_x286(z29=536000086, z30=536020087, z31=5036010):
    """[Conditions] Toyo knight's gut determination
    z29: Boss destruction flag
    z30: Gag stop flag
    z31: Boss Battle ID
    """
    """State 0,1: Has the boss battle started?"""
    IsEventBossBattle(0, z31, 1)
    assert ConditionGroup(0)
    """State 2: Player HP decrease judgment"""
    ComparePlayerHpDecrease(0)
    IsEventBossKill(1, z31, 0, 1)
    if ConditionGroup(1):
        """State 4: Sealed:"""
        return 1
    elif ConditionGroup(0):
        """State 3: HP reduction: Canceled hunger"""
        return 0

def event_m50_36_x287(z29=536000086, z30=536020087, z31=5036010):
    """[Execution] Judgment of Toyo Knight
    z29: Boss destruction flag
    z30: Gag stop flag
    z31: Boss Battle ID
    """
    """State 0,1: The hunger stop flag ON"""
    SetEventFlag(z30, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x288(z29=536000086, z30=536020087, z31=5036010):
    """[Preset] Oriental knight's gut determination
    z29: Boss destruction flag
    z30: Gag stop flag
    z31: Boss Battle ID
    """
    """State 0,1: [Reproduction] Oriental knight's gut determination_SubState"""
    call = event_m50_36_x285(z29=z29, z30=z30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Toyo knight's gut determination_SubState"""
        call = event_m50_36_x286(z29=z29, z30=z30, z31=z31)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Oriental knight's hunger determination_SubState"""
            assert event_m50_36_x287(z29=z29, z30=z30, z31=z31)
    """State 4: End state"""
    return 0

def event_m50_36_x289(z25=50363080):
    """[Execution] Crown that appears when the boss is destroyed
    z25: Crown OBJ instance ID
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z25, 1)
    """State 1: Acquisition failure window display"""
    # lot:60016000:Crown of the Old Iron King
    DisplayItemAwardFailure(60016000, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 2: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z25, 0)
    """State 5: End state"""
    return 0

def event_m50_36_x290(z17=536000046, z19=50361106, z20=94, z21=34, z18=50361606, z22=2121, z23=2124,
                      z24=2130):
    """[Condition] Storm of Darkness by Zhao Statue _ Zakobos ②
    z17: Destruction flag
    z19: 像 image OBJ instance ID
    z20: Samurai Statue_Activation Confirmed OBJ State ID
    z21: Saddle Statue_OBJ State ID after cancellation
    z18: Dark Storm OBJ Instance ID
    z22: Generator ID ①
    z23: Generator ID ②
    z24: Generator ID ③
    """
    """State 0,1: Waiting for the spear statue to appear or waiting for destruction"""
    CompareObjState(8, z19, z21, 0)
    IsChrDeadOrRespawnOver(8, z22, 1)
    IsChrDeadOrRespawnOver(8, z24, 1)
    IsChrDeadOrRespawnOver(8, z23, 1)
    IsChrDeadOrRespawnOver(8, 2120, 1)
    CompareEventFlag(1, z17, 1)
    CompareObjState(1, z19, z20, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(8):
        """State 2: Dark Storm Activated: 30"""
        ChangeObjState(z18, 30)
        """State 3: Waiting for destruction of eagle statue"""
        CompareEventFlag(0, z17, 1)
        CompareObjState(0, z19, z20, 0)
        assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_36_x291(z17=536000046, z18=50361606, z19=50361106, z20=94, z21=34, z22=2121, z23=2124,
                      z24=2130):
    """[Preset] Storm of Darkness by Zodiac Statue _ Zakobos ②
    z17: Destruction flag
    z18: Dark Storm OBJ Instance ID
    z19: 像 image OBJ instance ID
    z20: Samurai Statue_Activation Confirmed OBJ State ID
    z21: Saddle Statue_OBJ State ID after cancellation
    z22: Generator ID ①
    z23: Generator ID ②
    z24: Generator ID ③
    """
    """State 0,1: [Reproduction] Dark storm _SubState by a spear image"""
    call = event_m50_36_x233(z17=z17)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Storm of darkness by the statue of a spider _Zakobos ②_SubState"""
        assert event_m50_36_x290(z17=z17, z19=z19, z20=z20, z21=z21, z18=z18, z22=z22, z23=z23, z24=z24)
    """State 2: [Execution] Storm of Darkness by Subaru Statue_SubState"""
    assert event_m50_36_x235(z18=z18)
    """State 4: End state"""
    return 0

def event_m50_36_x292(z13=536020023, z14=536000024):
    """[Reproduction] Debut activation of another tower
    z13: Fat start flag
    z14: Sashimi get flag
    """
    """State 0,1: Is it a hostile spirit?"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    else:
        Goto('L0')
    """State 5: Hostile spirit"""
    return 2
    """State 2: Already started?"""
    Label('L0')
    if GetEventFlag(z14) != 0:
        """State 4: Activated"""
        Label('L1')
        return 1
    elif GetEventFlag(z13) != 0:
        Goto('L1')
    else:
        """State 3: Not started"""
        return 0

def event_m50_36_x293(z15=305000, z16=305002, z14=536000024):
    """[Condition] Debate start of another tower
    z15: Start point ID
    z16: End point ID
    z14: Sashimi get flag
    """
    """State 0,1: Point determination or firestick acquisition determination"""
    IsPlayerInsidePoint(0, z15, z16, 1)
    CompareEventFlag(0, z14, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x294(z13=536020023):
    """[Execution] Debate start of another tower
    z13: Fat start flag
    """
    """State 0,1: Fat start flag ON"""
    SetEventFlag(z13, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x295(z13=536020023, z14=536000024, z15=305000, z16=305002):
    """[Preset] Debut of another tower
    z13: Fat start flag
    z14: Sashimi get flag
    z15: Start point ID
    z16: End point ID
    """
    """State 0,1: [Reproduction] Debut activation of another tower_SubState"""
    call = event_m50_36_x292(z13=z13, z14=z14)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        """State 2: [Execution] Debut activation of another tower_SubState"""
        Label('L0')
        assert event_m50_36_x294(z13=z13)
    elif call.Get() == 0:
        """State 3: [Condition] Debut activation of another tower_SubState"""
        assert event_m50_36_x293(z15=z15, z16=z16, z14=z14)
        Goto('L0')
    """State 4: End state"""
    return 0

def event_m50_36_x296(z10=_):
    """[Reproduction] NPC gesture management
    z10: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z10) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_36_x297(z11=_):
    """[Conditions] NPC gesture management
    z11: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z11, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x298(z12=_):
    """[Execution] NPC gesture management
    z12: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z12, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x299(z10=_, z11=_, z12=_):
    """[Preset] NPC gesture management
    z10: Defeat flag
    z11: Boss generator ID
    z12: Gesture flag
    """
    """State 0,1: [Reproduction] NPC Gesture Management_SubState"""
    call = event_m50_36_x296(z10=z10)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] NPC Gesture Management_SubState"""
        assert event_m50_36_x297(z11=z11)
        """State 2: [Execution] NPC Gesture Management_SubState"""
        assert event_m50_36_x298(z12=z12)
    """State 4: End state"""
    return 0

def event_m50_36_x300(mode1=0, z5=_):
    """[Conditions] Wetting enhancement_Multiple images
    mode1: OBJ instance ID for production
    z5: Generator ID
    """
    """State 0,2: Always activated"""
    if (not mode1) != 0:
        pass
    else:
        """State 1: Judgment judgment or destruction judgment"""
        CompareObjState(0, mode1, 20, 0)
        CompareObjState(0, mode1, 70, 0)
        IsChrDead(1, z5)
        CompareEventFlag(1, 536000041, 1)
        CompareEventFlag(1, 536000042, 1)
        CompareEventFlag(1, 536000043, 1)
        CompareEventFlag(1, 536000044, 1)
        CompareObjState(1, 50361101, 50, 0)
        CompareObjState(1, 50361101, 51, 0)
        CompareObjState(1, 50361102, 50, 0)
        CompareObjState(1, 50361102, 51, 0)
        CompareObjState(1, 50361103, 50, 0)
        CompareObjState(1, 50361103, 51, 0)
        CompareObjState(1, 50361104, 50, 0)
        CompareObjState(1, 50361104, 51, 0)
        if ConditionGroup(1):
            """State 3: Cancel: Do nothing"""
            return 0
        elif ConditionGroup(0):
            pass
    """State 4: Strengthen"""
    return 1

def event_m50_36_x301(z5=_, z6=_, z7=_, z8=_, z9=_):
    """[Execution] Wetting enhancement_Multiple images
    z5: Generator ID
    z6: Special effect ID during effect
    z7: Special effect ID for release effect
    z8: Special effect ID for activation
    z9: Enhanced Special Effect ID
    """
    """State 0,1: For strengthening, during effect, for triggering effect 3 special effects are given"""
    SetEnemySpEffect(z5, z6, 19, 4)
    SetEnemySpEffect(z5, z8, 19, 4)
    SetEnemySpEffect(z5, z9, 19, 4)
    """State 2: Destruction determination"""
    IsChrDead(0, z5)
    CompareEventFlag(0, 536000041, 1)
    CompareEventFlag(0, 536000042, 1)
    CompareEventFlag(0, 536000043, 1)
    CompareEventFlag(0, 536000044, 1)
    CompareObjState(0, 50361101, 50, 0)
    CompareObjState(0, 50361101, 51, 0)
    CompareObjState(0, 50361102, 50, 0)
    CompareObjState(0, 50361102, 51, 0)
    CompareObjState(0, 50361103, 50, 0)
    CompareObjState(0, 50361103, 51, 0)
    CompareObjState(0, 50361104, 50, 0)
    CompareObjState(0, 50361104, 51, 0)
    assert ConditionGroup(0)
    """State 3: Cancel special effects"""
    ClearEnemySpEffect(z5, z6)
    ClearEnemySpEffect(z5, z8)
    ClearEnemySpEffect(z5, z9)
    """State 4: Special effects for release effects"""
    SetEnemySpEffect(z5, z7, 19, 4)
    """State 5: End state"""
    return 0

def event_m50_36_x302(mode1=0, z5=_, z6=_, z7=_, z8=_, z9=_):
    """[Preset] 煤 Wet Enhancement_Multiple Images
    mode1: OBJ instance ID for production
    z5: Generator ID
    z6: Special effect ID during effect
    z7: Special effect ID for release effect
    z8: Special effect ID for activation
    z9: Enhanced Special Effect ID
    """
    """State 0,1: [Reproduction] Wetting enhancement_SubState"""
    assert event_m50_36_x191()
    """State 3: [Condition] Wetting enhancement_Multiple images_SubState"""
    call = event_m50_36_x300(mode1=mode1, z5=z5)
    if call.Get() == 1:
        """State 2: [Execution] Wetting enhancement_Multiple images_SubState"""
        assert event_m50_36_x301(z5=z5, z6=z6, z7=z7, z8=z8, z9=z9)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m50_36_x303():
    """[Reproduction] Change the filter of another tower"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x304(z3=306000, z4=306000):
    """[Condition] Change the filter of another tower
    z3: Start point ID
    z4: End point ID
    """
    """State 0,1: Did you enter a switching point?"""
    IsPlayerInsidePoint(0, z3, z4, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x305(z3=306000, z4=306000, val1=14):
    """[Execution] Change the filter of another tower
    z3: Start point ID
    z4: End point ID
    val1: Volume fog filter ID
    """
    """State 0,2: Filter status judgment"""
    if (GetVolumeFogFilterOverride() == val1) != 1:
        """State 1: Push filter"""
        PushVolumeFogFilter(val1, 0)
        assert (GetVolumeFogFilterOverride() == val1) != 0
    else:
        pass
    """State 3: Did you get out of the switching point?"""
    IsPlayerInsidePoint(0, z3, z4, 0)
    assert ConditionGroup(0)
    """State 4: Outside area: Pop filter"""
    PopVolumeFogFilter(0)
    """State 5: Waiting for pop"""
    assert (GetVolumeFogFilterOverride() == val1) != 1
    """State 6: Rerun"""
    return 0

def event_m50_36_x306(z3=306000, z4=306000, val1=14):
    """[Preset] Change the filter of another tower
    z3: Start point ID
    z4: End point ID
    val1: Volume fog filter ID
    """
    """State 0,1: [Reproduction] Change the filter of another tower_SubState"""
    assert event_m50_36_x303()
    """State 3: [Condition] Filter change of another tower_SubState"""
    assert event_m50_36_x304(z3=z3, z4=z4)
    """State 2: [Execution] Change filter of another tower_SubState"""
    assert event_m50_36_x305(z3=z3, z4=z4, val1=val1)
    """State 4: Rerun"""
    return 0

def event_m50_36_x307(z1=_):
    """[Reproduction] Enemy jumping out of Haikuyama
    z1: Pop out flag
    """
    """State 0,2: Is it a hostile spirit?"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    else:
        Goto('L0')
    """State 5: Hostile spirit"""
    return 2
    """State 1: Have you already jumped out?"""
    Label('L0')
    if GetEventFlag(z1) != 0:
        """State 4: Popped out"""
        return 1
    else:
        """State 3: Not jumping out"""
        return 0

def event_m50_36_x308(z1=_, z2=_):
    """[Condition] Enemy jumping out of Haizan
    z1: Pop out flag
    z2: Pop-up point ID
    """
    """State 0,1: State invincibility: Release judgment"""
    BecomeInvincibleInCurrentState()
    IsPlayerInsidePoint(0, z2, z2, 1)
    CompareEventFlag(0, z1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x309(z1=_):
    """[Execution] Enemy jumping out of Haiyama
    z1: Pop out flag
    """
    """State 0,1: Pop-out flag ON"""
    SetEventFlag(z1, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x310(z1=_, z2=_):
    """[Preset] Enemy jumping out of Haeyama
    z1: Pop out flag
    z2: Pop-up point ID
    """
    """State 0,1: [Reproduction] Enemy _SubState jumping out of Haeyama"""
    call = event_m50_36_x307(z1=z1)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Enemy _SubState jumping out of Haizan"""
        assert event_m50_36_x308(z1=z1, z2=z2)
        """State 2: [Execution] Enemy _SubState jumping out of Haizan"""
        assert event_m50_36_x309(z1=z1)
    """State 4: End state"""
    return 0

def event_m50_36_4000000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m50_36_x56(z223=536020067, z224=14, z225=536000068, z226=3, z227=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m50_36_x61(z231=80000000, z232=0, z233=5, z234=977, val11=1, z235=10, z236=80000001,
                z237=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m50_36_x61(z231=80000100, z232=0, z233=5, z234=977, val11=2, z235=10, z236=80000101,
                z237=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m50_36_x61(z231=80000200, z232=0, z233=5, z234=977, val11=3, z235=10, z236=80000201,
                z237=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(536020069, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m50_36_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m50_36_x64(z228=536000068, z229=977, mode4=1)
    """State 1: Finish"""
    EndMachine()

