# -*- coding: utf-8 -*-
def event_m50_36_1000():
    """Operate the facility"""
    """State 0,3: [Preset] _SubState to operate the facility"""
    call = event_m50_36_x116(z159=50363040)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_1020():
    """Facility operation direction"""
    """State 0,2: [Preset] Facility Operation Direction_SubState"""
    assert event_m50_36_x232(z67=50363040, z68=50361500, z69=50361510, z70=50363100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_2000():
    """Lattice opening with lever_1"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z176=50361021, z177=50362000, z178=200000, z179=9)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_2010():
    """Lattice opening with lever_2"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z176=50361022, z177=50362010, z178=201000, z179=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_2020():
    """Lattice opening with lever_3"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z176=50361023, z177=50362020, z178=202000, z179=8.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_2030():
    """Opening with a lever_4"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z176=50361028, z177=50362040, z178=203000, z179=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_2040():
    """Opening with a lever_5"""
    """State 0,2: [Preset] Opened with a lever"""
    assert event_m50_36_x94(z176=50361026, z177=50362030, z178=204000, z179=7.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_3000():
    """Get a firestick"""
    """State 0,3: [Preset] _SubState to get a sashimi stick"""
    # lot:60014000:Scorching Iron Scepter, goods:53100000:Scorching Iron Scepter
    call = event_m50_36_x220(z74=50367900, lot1=60014000, flag15=536000024, goods1=53100000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_3020():
    """The fire of the other tower disappears"""
    """State 0,2: [Preset] The fire of another tower disappears_SubState"""
    assert event_m50_36_x268(flag10=536000024, z36=3020, z37=50360060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_3030():
    """The furnace in the other tower stops"""
    """State 0,2: [Preset] Furnace in another tower stops_SubState"""
    assert event_m50_36_x276(flag9=536000024, z31=50361530, z32=50360040, z33=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_3040():
    """The light of the other tower disappears"""
    """State 0,2: [Preset] The light of the other tower disappears_SubState"""
    assert event_m50_36_x280(flag8=536000024, z29=1, z30=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_3050():
    """Debate start of another tower"""
    """State 0,2: [Preset] Debut activation of another tower_SubState"""
    assert event_m50_36_x295(flag3=536020023, flag4=536000024, z11=305000, z12=305002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_3060():
    """Change the filter of another tower"""
    """State 0,2: [Preset] Change filter of another tower_SubState"""
    assert event_m50_36_x306(z2=306000, z3=306000, val1=14)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_4000():
    """A treasure when the mountain of ash is destroyed_1"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362800, z185=50368000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4010():
    """Treasure when the mountain of ash is destroyed_2"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362801, z185=50368010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4020():
    """Treasure _3"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362802, z185=50368020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4030():
    """Treasure _4"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362803, z185=50368030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4040():
    """Treasure _5"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362804, z185=50368040)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4050():
    """Treasure _6"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362805, z185=50368050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4060():
    """Treasure _7"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362806, z185=50368060)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4070():
    """Treasure _8"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362807, z185=50368070)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4080():
    """Treasure _9"""
    """State 0,2: [Preset] Treasure _SubState when breaking the mountain of ash"""
    assert event_m50_36_x72(z184=50362808, z185=50368080)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5000():
    """Destroying a spider statue"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361109, z127=536000049, z128=50368590, z129=33, z130=93, z131=43,
                             z132=33, z133=500000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_5010():
    """Smoke damage caused by a spear image_Isolated island"""
    """State 0,2: [Preset] Smoke damage caused by a spear image_Isolated Island_SubState"""
    assert event_m50_36_x128(flag30=536000049)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5200():
    """煤 Wet Strengthening_Isolated Island_Ax A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2811, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5210():
    """煤 Wet Strengthening_Isolated Island_Ax B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2820, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5220():
    """煤 Wet Strengthening_Isolated Island_Ax C"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2821, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5230():
    """煤 Wet Strengthening_Isolated Island_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2800, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5240():
    """煤 Wet Strengthening_Isolated Island_Ax E"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2801, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5250():
    """煤 Wet Strengthening_Isolated Island_Ax F"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2810, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5280():
    """煤 Wet Strengthening_Isolated Island_Ax I"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2822, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5300():
    """煤 Wet Strengthening_Isolated Island_Smoke Spirit A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2830, z104=96560310, z105=96560210, z106=96560410,
            z107=96560000, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_5310():
    """煤 Wet Strengthening_Isolated Island_Smoke Spirit B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000049, z103=2805, z104=96560310, z105=96560210, z106=96560410,
            z107=96560000, z108=50361109))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_6000():
    """Destroying a spear statue_Lobby"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361108, z127=536000048, z128=50368580, z129=34, z130=94, z131=44,
                             z132=34, z133=600000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_6010():
    """Smoke damage caused by a spear statue_Lobby"""
    """State 0,2: Operate the facility"""
    assert event_m50_36_x131(flag29=536000048)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_6020():
    """Smoke filter change by sculpture"""
    """State 0,3: [Preset] Smoke filter change by Subaru image_SubState"""
    call = event_m50_36_x135(flag27=536000049, flag28=536000048, z147=20, z148=30, val9=14, val10=15,
                             z149=22, z150=32)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_6030():
    """Smoke fog and light changes by the eagle statue"""
    """State 0,3: [Preset] Smoke fog and light change by the image of a spider _SubState"""
    call = event_m50_36_x228(flag13=536000049, flag14=536000048, z71=22, z72=32, val2=14, val3=15)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_6100():
    """煤 Wet Strengthening_Lobby_Ax A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000048, z103=2900, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361108))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_6110():
    """煤 Wet Strengthening_Lobby_Ax B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000048, z103=2901, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361108))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_6130():
    """煤 Wet Strengthening_Lobby_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000048, z103=2911, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361108))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_6140():
    """煤 Wet Strengthening_Lobby_Ax E"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000048, z103=2912, z104=96560300, z105=96560200, z106=96560400,
            z107=96560100, z108=50361108))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_6210():
    """煤 Wet Strengthening_Lobby_Smoke Spirit B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=0, z102=536000048, z103=2920, z104=96560310, z105=96560210, z106=96560410,
            z107=96560000, z108=50361108))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_7000():
    """Large door opened by lever_upper layer"""
    """State 0,2: [Preset] Large door opened by lever_Enemy activation_SubState"""
    assert event_m50_36_x253(z49=50361024, z50=50360410, z51=700000, z52=536000027)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_7010():
    """Large door opened with lever_Multiple tower"""
    """State 0,2: [Preset] Large door opened with lever_SubState"""
    assert event_m50_36_x98(z173=50361025, z174=50360411, z175=701000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_7020():
    """Large door opened with lever_Paka floor area"""
    """State 0,2: [Preset] Large door opened with lever_SubState"""
    assert event_m50_36_x98(z173=50361027, z174=50360412, z175=702000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_8000():
    """One-way door_Beside the fire room"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _2_SubState"""
    assert event_m50_36_x2(z260=0, z261=1101, z262=800000, z263=536000030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_8010():
    """One-way door_Paka floor area"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_36_x2(z260=0, z261=1101, z262=801000, z263=536000032)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_8011():
    """OBJ blocking a one-way door"""
    """State 0,2: [Preset] OBJ_SubState that blocks a one-way door"""
    assert event_m50_36_x177(z114=50363090, z115=536000032)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_9010():
    """Change navigation with Salamander Defeat_2"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z34=7500, z35=901000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_9020():
    """Change navigation with Salamander Defeat_3"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z34=7502, z35=902000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_9030():
    """Change navigation by destroying salamander_4"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z34=7503, z35=903000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_9070():
    """Change navigation with Salamander Defeat_8"""
    """State 0,2: [Preset] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x272(z34=7603, z35=907000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_10000():
    """Elevator_in front of boss"""
    """State 0,1: Has the initialization event been completed?"""
    assert EventEnded(10030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z236=50361300, z237=1000000, z238=1000010, z239=50361040, z240=50361041)
    """State 2: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_10010():
    """Elevator_Before boss_Lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361300, z253=50361040, z254=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_10020():
    """Elevator_Before boss_Lever bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361300, z253=50361041, z254=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_10030():
    """Elevator_Before Boss_Initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m50_36_x23(z249=50361300, z250=40, flag38=536000012, z251=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_12000():
    """Elevator_Start"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z236=50361320, z237=1200000, z238=1200010, z239=50361050, z240=50361051)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_12010():
    """Elevator_Start_Lever top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361320, z253=50361050, z254=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_12020():
    """Elevator_Start_Lever bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361320, z253=50361051, z254=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_13000():
    """Elevator_Termination of break route"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z236=50361019, z237=1300000, z238=1300010, z239=50361060, z240=50361061)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_13010():
    """Elevator_Termination of split route_Lever top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361019, z253=50361060, z254=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_13020():
    """Elevator_Termination of dividing route_Under lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361019, z253=50361061, z254=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_14000():
    """Elevator_Separate tower"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(14030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_36_x10(z236=50361330, z237=1400000, z238=1400010, z239=50361081, z240=50361080)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_14010():
    """Elevator_Another tower_Lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361330, z253=50361081, z254=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_14020():
    """Elevator_Another tower_Under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_36_x15(z252=50361330, z253=50361080, z254=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_14030():
    """Elevator_separate tower_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m50_36_x23(z249=50361330, z250=40, flag38=536000013, z251=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_14040():
    """Elevator_Another tower_Navigation switching"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(14030) != 0
    """State 3: [Navigation switching of preset elevators_SubState"""
    assert event_m50_36_x284(z25=50361330, z26=1404000, z27=1404010)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_15010():
    """Unraveling the curse of the bride ’s soul"""
    """State 0,2: [Preset] _SubState to unlock the curse of the bride ’s soul"""
    assert event_m50_36_x176(flag18=536000026, z116=5, z117=5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_16000():
    """Hidden door navigation mesh change_outer wall"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z241=50362210, z242=20, z243=1600000, z244=0, z245=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_16010():
    """Hidden door navigation mesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z241=50362211, z242=20, z243=1601000, z244=0, z245=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_17000():
    """C root key: memory"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_36_x1(z264=1005, z265=1105, z266=52400000, z267=536000036)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_17010():
    """C root key door: Split"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_36_x1(z264=1005, z265=1105, z266=52400000, z267=536000038)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_17020():
    """Lobby key door"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_36_x1(z264=1005, z265=1105, z266=52400000, z267=536000034)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_18000():
    """Enemy jumping out of Haishan_1"""
    """State 0,2: [Preset] Enemy _SubState jumping out of Ashyama"""
    assert event_m50_36_x310(flag1=536020065, z1=1800000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_18010():
    """Enemy jumping out of Haizan_2"""
    """State 0,2: [Preset] Enemy _SubState jumping out of Ashyama"""
    assert event_m50_36_x310(flag1=536020066, z1=1801000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_19000():
    """Continuous intrusion"""
    """State 0,2: [Preset] Continuous intrusion_SubState"""
    assert event_m50_36_x141(z41=536020004, z42=536020005, z43=536020006, z44=536020007, z45=536020008)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_19010():
    """Continuous intrusion_termination"""
    """State 0,2: [Preset] Continuous intrusion_End_SubState"""
    assert event_m50_36_x145(z135=7000, z136=7001, z137=7002, z138=7003, z139=7004, flag23=536000001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_20000():
    """Boss: Black Smoke Knight"""
    """State 0,2: [Preset] Black Smoke Knight Battle_Start_SubState"""
    assert (event_m50_36_x206(flag16=536000081, z75=501, z76=5036000, z77=536020080, z78=6.3, z79=10,
            z80=5036001, z81=536020083))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_20010():
    """The crown that appears when you destroy a boss"""
    """State 0,3: [Preset] Crown _SubState that appears when a boss is destroyed"""
    # action:5310:"A faint heat lingers in the ancient crown"
    call = event_m50_36_x181(z20=50363080, flag6=536000020, z21=5, action1=5310, z22=50360080)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_20050():
    """NPC Gesture Management_Black Smoke Knight"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_36_x299(flag2=536000081, z9=903, z10=536020084)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_21000():
    """Boss behavior change with Verstad equipment"""
    """State 0,3: [Preset] Boss behavior change with Verstad equipment_SubState"""
    call = event_m50_36_x157(z123=536020082, flag22=536000081)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_22000():
    """Destroyed sculpture _ left boss room _ front"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361101, z127=536000041, z128=50368510, z129=33, z130=93, z131=43,
                             z132=33, z133=2200000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_22010():
    """Destroying a spear statue_Boss room left_Back"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361102, z127=536000042, z128=50368520, z129=34, z130=94, z131=44,
                             z132=34, z133=2201000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_22020():
    """Destroying a spider statue"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361103, z127=536000043, z128=50368530, z129=33, z130=93, z131=43,
                             z132=33, z133=2202000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_22030():
    """Destroying a spider statue_Boss room right_Back"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361104, z127=536000044, z128=50368540, z129=34, z130=94, z131=44,
                             z132=34, z133=2203000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_22100():
    """煤 Wet Strengthening_Multiple Versions_Ax A"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z4=4610, z5=96560300, z6=96560200, z7=96560400, z8=96560100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_22110():
    """煤 Wet strengthening_Multiple images_Ax B"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z4=4611, z5=96560300, z6=96560200, z7=96560400, z8=96560100)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_22200():
    """煤 Wet enhancement_Multiple images_Cow A"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z4=4700, z5=96560320, z6=96560220, z7=96560420, z8=96560110)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_22210():
    """煤 Wet strengthening_Multiple images_Cow B"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z4=4800, z5=96560320, z6=96560220, z7=96560420, z8=96560110)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_22300():
    """煤 Wet Enhancement_Multiple Images_Smoke Spirit A"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z4=4600, z5=96560310, z6=96560210, z7=96560410, z8=96560000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_22310():
    """煤 Wet Enhancement_Multiple Images_Smoke Spirit B"""
    """State 0,2: [Preset] Dampening enhancement_Multiple images_SubState"""
    assert event_m50_36_x302(mode1=0, z4=4601, z5=96560310, z6=96560210, z7=96560410, z8=96560000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_23000():
    """Recovery sphere with spear image _ Boss room left _ front"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361101, z247=150, z248=50361453)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(flag19=536000041, z118=50361453)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_23010():
    """Recovery sphere with a spear image _ Boss room left _ back"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361102, z247=150, z248=50361454)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(flag19=536000042, z118=50361454)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_23020():
    """Recovery sphere with sculpture statue _ boss room right _ front"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361103, z247=150, z248=50361452)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(flag19=536000043, z118=50361452)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_23030():
    """Recovery sphere with a spear image _ Boss room right _ back"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361104, z247=150, z248=50361451)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(flag19=536000044, z118=50361451)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_25000():
    """Boss: Demon Knight Kai_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m50_36_x3(flag39=536000091, z255=2500000, z256=2500000, z257=503, z258=5036020, z259=536020090,
            mode5=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_25010():
    """Flame linked to the Demon Knight Kai action"""
    """State 0,2: [Preset] Flame_SubState linked to Demon Knight Kai action"""
    assert (event_m50_36_x99(z166=905, z167=71, z168=70, z169=50362200, z170=50362201, z171=93050011,
            flag32=536000091))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_25050():
    """NPC Gesture Management_Demon Knight Kai"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_36_x299(flag2=536000091, z9=905, z10=536020094)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_28000():
    """Boss: Oriental Knight_Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Start_SubState"""
    assert (event_m50_36_x3(flag39=536000086, z255=2800000, z256=2800000, z257=502, z258=5036010, z259=536020085,
            mode5=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_28010():
    """Toyo knight's hunger judgment"""
    """State 0,2: [Preset] Toyo knight's gut determination_SubState"""
    assert event_m50_36_x288(flag7=536000086, z23=536020087, z24=5036010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_28050():
    """NPC Gesture Management_Toyo Knight"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_36_x299(flag2=536000086, z9=904, z10=536020089)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_30000():
    """Two pairs of spinning fire bulls"""
    """State 0,2: [Preset] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m50_36_x79(z183=50361200)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_30010():
    """Two pairs of rotating fire-blowing cows_attach_1"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361200, z247=150, z248=50361210)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_30020():
    """Two pairs of rotating fire-blowing cows_attach_2"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361200, z247=151, z248=50361211)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_31000():
    """Sliding fire-blowing cattle"""
    """State 0,2: [Preset] sliding fire-blowing cow_initialized version_SubState"""
    assert (event_m50_36_x123(z151=50361220, z152=30, z153=32, z154=70, z155=72, z156=3100000, z157=3100010,
            z158=3100020))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_31010():
    """Sliding fire-blowing cow _ Thorn wall side A_ attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361220, z247=150, z248=50361230)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_32000():
    """Sliding fire-sprayed cow_Kenzawayama 1F"""
    """State 0,2: [Preset] Sliding fire-blowing cow_Initialized version_Kenzawayama 1F_SubState"""
    assert event_m50_36_x197(z95=50361221, z96=30, z97=32, z98=70, z99=72, z100=3200000, z101=3200020)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_32010():
    """Sliding fire beef_Kenzawayama 1F_Attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361221, z247=150, z248=50361231)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_33000():
    """Sliding fire-sprayed cow_Kenzawa 2F"""
    """State 0,2: [Preset] sliding fire-blowing cow_initialized version_Kenzawa 2F_SubState"""
    assert event_m50_36_x198(z88=50361222, z89=40, z90=42, z91=80, z92=82, z93=3300020, z94=3300000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_33010():
    """Sliding fire beef_Kenzawa 2F_Attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361222, z247=150, z248=50361232)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_34000():
    """Sliding fire-blowing cow _ thorn wall side B"""
    """State 0,2: [Preset] sliding fire-blowing cow_initialized version_SubState"""
    assert (event_m50_36_x123(z151=50361260, z152=40, z153=42, z154=80, z155=82, z156=3400000, z157=3400010,
            z158=3400020))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_34010():
    """Sliding fire-blowing cow _ Thorn wall side B_ attach"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361260, z247=150, z248=50361250)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_37000():
    """The image of a half-broken spear collapses"""
    """State 0,2: [Preset] The image of a half-broken spear collapses"""
    assert event_m50_36_x264(z38=50368800, z39=50361130, z40=3700000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38000():
    """Destruction variable reset of eagle statue"""
    """State 0,2: [Preset] Destruction variable reset of the spider image_SubState"""
    assert event_m50_36_x240(z62=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38010():
    """Judgment of the number of spears"""
    """State 0,2: [Preset] Judgment of the number of spears_SubState"""
    assert event_m50_36_x248(z53=1, z54=10, z55=536000039, z56=11, z57=536000059, z58=100710)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38100():
    """Addition of destructive variables for sculpture _Zakobos ①"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000040, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38110():
    """Addition of destructive variable for sculpture statue"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000041, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38120():
    """Addition of destructive variable of sculpture statue_Boss room left_Back"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000042, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38130():
    """Addition of destructive variable for sculpture statue"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000043, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38140():
    """Addition of destruction variable of sculpture statue_Boss room right_Back"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000044, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38160():
    """Addition of destructive variable of sculpture statue_Boss room_Zakobos ②"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000046, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38170():
    """Addition of destructive variable of sculpture statue_Boss room_Throne"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000047, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38180():
    """Addition of destructive variable of sculpture statue_Boss room_Lobby"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000048, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38190():
    """Addition of destruction variable of sculpture statue_Boss room_Isolated island"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000049, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38200():
    """Addition of destructive variables for sculpture _ Boss Room _ Airy"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000050, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_38210():
    """Addition of destructive variable of sculpture statue_boss room_top"""
    """State 0,2: [Preset] Destructive variable addition of the frog image_SubState"""
    assert event_m50_36_x244(z59=38000, z60=536000051, z61=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_39000():
    """Destroy the spider statue_top"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361111, z127=536000051, z128=50368610, z129=30, z130=91, z131=41,
                             z132=31, z133=3900000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_39010():
    """Dark storm from the statue of a spider"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361111, z247=150, z248=50361611)
    """State 2: [Preset] Dark storm _SubState"""
    assert event_m50_36_x236(flag12=536000051, z63=50361611, z64=50361111, z65=91, z66=31)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_40000():
    """Opened with a lever"""
    """State 0,2: [Preset] Continuous iron grids open with lever _7 versions_SubState"""
    assert event_m50_36_x163(z122=50361075, mode3=0, flag21=536020016, val6=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_40010():
    """7 continuous iron grid version changes"""
    """State 0,2: [Preset] 7 continuous iron grid editions_Navigation change_SubState"""
    assert event_m50_36_x204(z87=536020017)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_41000():
    """Opened with a lever"""
    """State 0,2: [Preset] Continuous iron grids open with levers_9 versions_SubState"""
    assert event_m50_36_x164(z121=50361076, mode2=0, flag20=536020018, val5=3.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_41010():
    """Nine continuous bar grid version change"""
    """State 0,2: [Preset] Nine continuous iron grid version_Navigation change_SubState"""
    assert event_m50_36_x205(z86=536020019)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_42000():
    """After the 7th edition of the spitting salamander statue"""
    """State 0,3: [Preset] Salamander image _SubState spitting fire"""
    call = event_m50_36_x168(z119=50362050, z120=50362250)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_42010():
    """After the 9th edition of the spitting salamander statue"""
    """State 0,3: [Preset] Salamander image _SubState spitting fire"""
    call = event_m50_36_x168(z119=50362060, z120=50362251)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_43000():
    """Destroying the statue of the fox"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361100, z127=536000040, z128=50368500, z129=33, z130=93, z131=43,
                             z132=33, z133=4300000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_43010():
    """Activating the Samurai Statue_Zakobos ①"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361100, z247=150, z248=50361150)
    """State 2: [Preset] Activating the frog image_SubState"""
    assert event_m50_36_x188(flag17=536000040, z109=50361100, z110=5, z111=50361150, z112=4301000, z113=4301000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_43100():
    """煤 Wet Strengthening_Zakobos ①_Ax A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z102=536000040, z103=1300, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361100))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_43110():
    """煤 Wet Strengthening_Zakobos ①_Ax B"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z102=536000040, z103=1310, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361100))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_43120():
    """煤 Wet Strengthening_Zakobos ①_Ax C"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z102=536000040, z103=1330, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361100))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_43130():
    """煤 Wet Strengthening_Zakobos ①_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z102=536000040, z103=1331, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361100))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_43140():
    """煤 Wet Strengthening_Zakobos ①_Ax E"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z102=536000040, z103=1332, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361100))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_43150():
    """煤 Wet Strengthening_Zakobos ①_Ax F"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361150, z102=536000040, z103=1301, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361100))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_44000():
    """Destroying a spider image_Zakobos ②"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361106, z127=536000046, z128=50368560, z129=34, z130=94, z131=44,
                             z132=34, z133=4400000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_44010():
    """Activating the Samurai Statue_Zakobos ②"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361106, z247=150, z248=50361156)
    """State 2: [Preset] Activating the frog image_SubState"""
    assert event_m50_36_x188(flag17=536000046, z109=50361106, z110=5, z111=50361156, z112=4401000, z113=4401000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_44020():
    """Dark storm from the statue of a spider Zakobos ②"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361106, z247=150, z248=50361606)
    """State 3: [Preset] Dark storm caused by the image of a spider _Zakobos ②_SubState"""
    assert (event_m50_36_x291(flag5=536000046, z13=50361606, z14=50361106, z15=94, z16=34, z17=2121,
            z18=2124, z19=2130))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_44130():
    """煤 Wet Strengthening_Zakobos②_Ax D"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z102=536000046, z103=2121, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361106))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_44160():
    """煤 Wet Strengthening_Zakobos②_AxG"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z102=536000046, z103=2124, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361106))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_44170():
    """煤 Wet Strengthening_Zakobos②_Ax H"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z102=536000046, z103=2120, z104=96560300, z105=96560200,
            z106=96560400, z107=96560100, z108=50361106))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_44200():
    """煤 Wet Strengthening_Zakobos②_Cow A"""
    """State 0,2: [Preset] Wetting enhancement_SubState"""
    assert (event_m50_36_x192(val4=50361156, z102=536000046, z103=2130, z104=96560320, z105=96560220,
            z106=96560420, z107=96560110, z108=50361106))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_45000():
    """Destroy the eagle statue in front of the throne"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361107, z127=536000047, z128=50368570, z129=33, z130=93, z131=43,
                             z132=33, z133=4500000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_45010():
    """Healing sphere with a spear image_in front of the throne"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361107, z247=150, z248=50361456)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(flag19=536000047, z118=50361456)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_46000():
    """Destroy the eagle statue_Eiley"""
    """State 0,3: [Preset] Destroying a spear image_SubState"""
    call = event_m50_36_x147(z126=50361110, z127=536000050, z128=50368600, z129=34, z130=94, z131=44,
                             z132=34, z133=4600000)
    if call.Get() == 2:
        """State 1: Finish"""
        Label('L0')
        EndMachine()
        Quit()
    elif call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 3:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_46020():
    """Healing sphere with a spear image_Irie"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_36_x27(z246=50361110, z247=150, z248=50361455)
    """State 2: [Preset] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x172(flag19=536000050, z118=50361455)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_47000():
    """Wall broken by explosion_Thorn wall side A_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z241=50362125, z242=20, z243=4700000, z244=0, z245=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_47010():
    """Wall broken by explosion_Thorn wall side B_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z241=50362126, z242=20, z243=4701000, z244=0, z245=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_47020():
    """Wall broken by explosion_swords"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_36_x28(z241=50362127, z242=20, z243=4702000, z244=0, z245=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_48010():
    """_B"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z73=50362401)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_48020():
    """_C"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z73=50362402)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_48030():
    """Ignite the corpse_D"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z73=50362403)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_48040():
    """_E"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z73=50362404)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_48050():
    """Fire a corpse_F"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z73=50362405)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_48060():
    """_G"""
    """State 0,3: [Preset] _SubState to ignite the corpse"""
    call = event_m50_36_x221(z73=50362406)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

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
    Quit()

def event_m50_36_50000():
    """Door that opens with DLC purchase"""
    """State 0,3: [Preset] Door that opens with DLC purchase_SubState"""
    call = event_m50_36_x82(z180=50360400, z181=5000000, z182=5000010)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_51000():
    """Start from molten iron castle"""
    """State 0,1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_52000():
    """Return to molten iron castle"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m50_36_x48(z215=50363010, z216=10190000, z217=5200000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_36_53000():
    """Invade the memory of the ancient king"""
    """State 0,3: [Preset] Invade the memory of the old king_SubState"""
    call = event_m50_36_x109(z161=50363060, z162=503610, z163=0, z164=50360000, z165=5300000, flag31=101061)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_54000():
    """Return from the memory of the ancient king"""
    """State 0,3: [Preset] Return from the Memory of the Old King_Item Available_SubState"""
    # lot:60013000:Smelter Wedge, goods:53200000:Smelter Wedge
    call = event_m50_36_x66(z186=50363030, lot2=60013000, flag33=536000022, goods2=53200000, z187=0,
                            z188=0, z189=5400000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_36_55000():
    """Time limit of memory of the ancient king"""
    """State 0,2: [Preset] Old King's memory time limit_SubState"""
    # action:2012:"The ashen mist has thinned...", action:2013:"The ashen mist fades..."
    assert (event_m50_36_x110(z143=4, z144=0, val7=1050, val8=1070, z145=1080, action2=2012, action3=2013,
            z146=5400000))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_59000():
    """Clear inter-DLC event_C route division"""
    """State 0,2: [Preset] Inter-DLC event_C route clear_SubState"""
    assert event_m50_36_x257(z48=101063, flag11=100711)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_59010():
    """Clear DLC event_C route memory"""
    """State 0,2: [Preset] Inter-DLC event_C route clear_SubState"""
    assert event_m50_36_x257(z48=101062, flag11=100712)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_80000():
    """Fireworks for regeneration 01_Start point_36650"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z233=5036000, z234=5036099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_81000():
    """Regenerative fire 02_Facility operation OBJ Square_36655"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z233=5036100, z234=5036199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_82000():
    """Rebirth Fire 03_Midroom Room_36660"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z233=5036200, z234=5036299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_83000():
    """Reproduction of fire 04_divided route_36665"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z233=5036300, z234=5036399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_84000():
    """Rebirth Fire 05_Before Boss Route_36670"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z233=5036400, z234=5036499)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_85000():
    """Rebirth Fire 06_Before the Flame (Memory) Route_36675"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_36_x38(z233=5036500, z234=5036599)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_89000():
    """Shop lineup expansion_Knight of black smoke"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_36_x50(z214=101061, flag37=101211)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_89010():
    """Shop lineup expansion_Toyo Knight"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_36_x50(z214=101062, flag37=101212)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_100000():
    """White Spirit 01: Carion"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m50_36_x41(z218=102722, z219=740, z220=104300, z221=103800, z222=-1)
    Quit()

def event_m50_36_x0(z162=_, z163=0, z164=_, z146=_):
    """[Lib] Warp between maps after poly play
    z162: Pre-warp poly play ID
    z163: Poly Play ID after Warp
    z164: Map ID
    z146: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z162, z163, z164, z146, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m50_36_x1(z264=1005, z265=1105, z266=52400000, z267=_):
    """[Lib] Item specified door unlocking_2
    z264: Text ID when opened
    z265: Text ID when not opened
    z266: item
    z267: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z266, z264, z265, z267, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x2(z260=0, z261=1101, z262=_, z263=_):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z260: Text ID when opened
    z261: Text ID when not opened
    z262: Point ID
    z263: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z262, 0, z260, z261, z263, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x3(flag39=_, z255=_, z256=_, z257=_, z258=_, z259=_, mode5=0):
    """[Lib] [Preset] Boss Battle Start
    flag39: Boss destruction flag
    z255: Start point ID
    z256: End point ID
    z257: Sound ID
    z258: Boss Battle ID
    z259: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m50_36_x4(flag39=flag39)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m50_36_x5(z255=z255, z256=z256)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m50_36_x6(z257=z257, z258=z258, z259=z259)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m50_36_x7()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m50_36_x8(z258=z258)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m50_36_x9(z257=z257, z258=z258, z259=z259, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m50_36_x4(flag39=_):
    """[Reproduction] Boss Battle_Start
    flag39: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag39) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_36_x5(z255=_, z256=_):
    """[Condition] Boss Battle_Start
    z255: Start point ID
    z256: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z255, z256, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z255, z256, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x6(z257=_, z258=_, z259=_):
    """[Execution] Boss Battle_Start
    z257: Sound ID
    z258: Boss Battle ID
    z259: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z257)
    """State 1: Boss battle start notification"""
    StartBossFight(z258)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z259, 1)
    """State 4: End state"""
    return 0

def event_m50_36_x7():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x8(z258=_):
    """[Condition] Boss Battle_End Judgment
    z258: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z258, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x9(z257=_, z258=_, z259=_, mode5=0):
    """[Execute] Boss Battle_End
    z257: Sound ID
    z258: Boss Battle ID
    z259: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z259, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z258)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z257)
    """State 5: End state"""
    return 0

def event_m50_36_100010():
    """White Spirit 02"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z235=741)
    Quit()

def event_m50_36_x10(z236=_, z237=_, z238=_, z239=_, z240=_):
    """[Lib] [Preset] Elevator
    z236: OBJ instance ID of the elevator
    z237: On elevator point ID_
    z238: Elevator point ID_below
    z239: Upper lever OBJ instance ID
    z240: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m50_36_x11()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m50_36_x12(z236=z236, z237=z237, z238=z238, z239=z239, z240=z240)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m50_36_x33(z236=z236, z238=z238)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m50_36_x32(z236=z236, z237=z237)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m50_36_x13(z236=z236, z237=z237)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m50_36_x14(z236=z236, z238=z238)
    """State 7: End state"""
    return 0

def event_m50_36_x11():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x12(z236=_, z237=_, z238=_, z239=_, z240=_):
    """[Condition] Elevator
    z236: Elevator OBJ instance ID
    z237: On elevator point ID_
    z238: Elevator point ID_below
    z239: Upper lever OBJ instance ID
    z240: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z236, 10, 0)
    CompareObjState(1, z236, 40, 0)
    CompareObjState(2, z236, 80, 0)
    CompareObjState(2, z236, 41, 0)
    CompareObjState(3, z236, 70, 0)
    CompareObjState(3, z236, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z238, z238, 1)
        CompareObjState(0, z239, 74, 0)
        CompareObjState(0, z239, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z237, z237, 1)
        CompareObjState(0, z240, 74, 0)
        CompareObjState(0, z240, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m50_36_x13(z236=_, z237=_):
    """[Execution] Elevator_Rise
    z236: Elevator OBJ instance ID
    z237: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z236, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z236, 30, 0)
    IsPlayerInsidePoint(8, z237, z237, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z236, 71)
    assert CompareObjStateId(z236, 40, 0)
    """State 4: End state"""
    return 0

def event_m50_36_x14(z236=_, z238=_):
    """[Execution] Elevator_Descent
    z236: Elevator OBJ instance ID
    z238: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z236, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z236, 41, 0)
    IsPlayerInsidePoint(8, z238, z238, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z236, 81)
    assert CompareObjStateId(z236, 10, 0)
    """State 4: End state"""
    return 0

def event_m50_36_x15(z252=_, z253=_, z254=_):
    """[Lib] [Preset] Elevator lever
    z252: OBJ instance ID of the elevator
    z253: Lever OBJ instance ID
    z254: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m50_36_x16()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m50_36_x17(z252=z252, z253=z253, z254=z254)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m50_36_x18(z252=z252, z253=z253, z254=z254)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m50_36_x19(z252=z252, z253=z253, z254=z254)
    """State 5: Rerun"""
    return 0

def event_m50_36_x16():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x17(z252=_, z253=_, z254=_):
    """[Condition] Elevator lever_use judgment
    z252: OBJ instance ID of the elevator
    z253: Lever OBJ instance ID
    z254: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z252, z254, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m50_36_x18(z252=_, z253=_, z254=_):
    """[Execution] Elevator lever_Key guide valid
    z252: OBJ instance ID of the elevator
    z253: Lever OBJ instance ID
    z254: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z253, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z252, z254, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x19(z252=_, z253=_, z254=_):
    """[Execute] Elevator lever_key guide disabled
    z252: OBJ instance ID of the elevator
    z253: Lever OBJ instance ID
    z254: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z253, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z252, z254, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_100020():
    """White Spirit 03"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z235=742)
    Quit()

def event_m50_36_x20(flag38=_):
    """[Lib] [Reproduction] Elevator_Initialization
    flag38: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag38) != 0:
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

def event_m50_36_x22(z249=_, z250=40, flag38=_, z251=40):
    """[Lib] [Execution] Elevator_Initialization
    z249: Elevator OBJ instance ID
    z250: Initial position OBJ state ID
    flag38: Initialization completion flag
    z251: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z249, z250)
    assert CompareObjStateId(z249, z251, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag38, 1)
    """State 3: End state"""
    return 0

def event_m50_36_x23(z249=_, z250=40, flag38=_, z251=40):
    """[Lib] [Preset] Elevator_Initialization
    z249: Elevator OBJ instance ID
    z250: Initial position OBJ state ID
    flag38: Initialization completion flag
    z251: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m50_36_x20(flag38=flag38)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m50_36_x21()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m50_36_x22(z249=z249, z250=z250, flag38=flag38, z251=z251)
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

def event_m50_36_x26(z246=_, z247=_, z248=_):
    """[Lib] [execute] OBJ attach
    z246: Parent OBJ instance ID
    z247: Parent Damipoli ID
    z248: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z246, z247, z248)
    """State 2: End state"""
    return 0

def event_m50_36_x27(z246=_, z247=_, z248=_):
    """[Lib] [Preset] OBJ attach
    z246: Parent OBJ instance ID
    z247: Parent Damipoli ID
    z248: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m50_36_x24()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m50_36_x25()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m50_36_x26(z246=z246, z247=z247, z248=z248)
    """State 4: End state"""
    return 0

def event_m50_36_x28(z241=_, z242=20, z243=_, z244=0, z245=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z241: Object instance ID
    z242: OBJ state ID
    z243: Navimesh switching point ID
    z244: Additional attributes
    z245: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m50_36_x29(z241=z241, z242=z242, z243=z243, z245=z245, z244=z244)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m50_36_x30(z241=z241, z242=z242, z243=z243)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m50_36_x31(z241=z241, z242=z242, z243=z243, z244=z244, z245=z245)
    """State 4: End state"""
    return 0

def event_m50_36_x29(z241=_, z242=20, z243=_, z245=2, z244=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z241: Target OBJ instance ID
    z242: Target OBJ state ID
    z243: Navimesh switching point ID
    z245: Additional attributes
    z244: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z241, z242, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z243, z245)
        DeleteNavimeshAttribute(z243, z244)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m50_36_100030():
    """White Spirit 04"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z235=743)
    Quit()

def event_m50_36_x30(z241=_, z242=20, z243=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z241: Target OBJ instance ID
    z242: Target OBJ state ID
    z243: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z241, z242, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x31(z241=_, z242=20, z243=_, z244=0, z245=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z241: Target OBJ instance ID
    z242: Target OBJ state ID
    z243: Navimesh switching point ID
    z244: Additional attributes
    z245: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z243, z244)
    DeleteNavimeshAttribute(z243, z245)
    """State 2: End state"""
    return 0

def event_m50_36_x32(z236=_, z237=_):
    """[Execution] Elevator_Return switch after lift
    z236: Elevator OBJ instance ID
    z237: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z236, 30, 0)
    IsPlayerInsidePoint(8, z237, z237, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z236, 71)
    assert CompareObjStateId(z236, 40, 0)
    """State 3: End state"""
    return 0

def event_m50_36_x33(z236=_, z238=_):
    """[Execution] Elevator_Return switch after descending
    z236: Elevator OBJ instance ID
    z238: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z236, 41, 0)
    IsPlayerInsidePoint(8, z238, z238, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z236, 81)
    assert CompareObjStateId(z236, 10, 0)
    """State 3: End state"""
    return 0

def event_m50_36_x34(z235=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z235: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z235)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m50_36_x35():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x36(z233=_, z234=_):
    """[Lib] [execute] Rebirth fire
    z233: Flag start ID
    z234: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z233, z234, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x37():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x38(z233=_, z234=_):
    """[Lib] [Preset] Rebirth
    z233: Flag start ID
    z234: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m50_36_x35()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m50_36_x37()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m50_36_x36(z233=z233, z234=z234)
    """State 4: End state"""
    return 0

def event_m50_36_x39(z227=100601, z228=10000010, z229=731, z230=104480, z231=0, z232=0):
    """[Lib] NPC Black Phantom Appearance: Online
    z227: Summoning conditions: Global event flag
    z228: Summon range
    z229: Generator ID
    z230: Death: Global event flag
    z231: Appearance: Minimum time
    z232: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z230, 1)
        CompareEventFlag(8, z227, 1)
        IsPlayerInsidePoint(8, z228, z228, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z230, 1)
            CompareStateTime(1, z231, 3, z232)
            IsPlayerInsidePoint(2, z228, z228, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z229)
                HasNpcPhantomSpawned(0, z229, 1)
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

def event_m50_36_100040():
    """White Spirit 05"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z235=744)
    Quit()

def event_m50_36_x40(z223=10000000, z224=730, z225=0, z226=0.2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z223: Summon range
    z224: Generator ID
    z225: Appearance: Minimum time
    z226: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z223, z223, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z225, 3, z226)
        IsPlayerInsidePoint(1, z223, z223, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z224)
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

def event_m50_36_x41(z218=102722, z219=740, z220=104300, z221=103800, z222=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z218: White Phantom can appear: Global event flag
    z219: White Phantom: Generator ID
    z220: Death: Global event flag
    z221: Hostile: Global event flag
    z222: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z219)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z220, 1)
        CompareEventFlag(1, z221, 1)
        CompareEventFlag(2, z218, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z219)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z220, 1)
            CompareEventFlag(1, z221, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z219)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z220, 1)
            CompareEventFlag(1, z221, 1)
            HasNpcPhantomSpawned(2, z219, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z219, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z219)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m50_36_x42(flag37=_):
    """[Lib] [Reproduction] Shop Lineup
    flag37: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(flag37) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m50_36_x43(flag37=_):
    """[Lib] [execution] shop lineup
    flag37: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(flag37, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x44(z215=50363010):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z215: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z215)
    """State 2: End state"""
    return 0

def event_m50_36_x45(z215=50363010):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z215: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z215, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z215)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m50_36_x46(z215=50363010, z216=10190000, z217=5200000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z215: Warp OBJ instance ID
    z216: Map ID
    z217: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z215, 1)
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
        assert event_m50_36_x0(z162=0, z163=0, z164=z216, z146=z217)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m50_36_x47(z215=50363010):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z215: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z215, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x48(z215=50363010, z216=10190000, z217=5200000):
    """[Lib] [Preset] Warp move between main part and DLC
    z215: Warp OBJ instance ID
    z216: Map ID
    z217: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m50_36_x44(z215=z215)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m50_36_x45(z215=z215)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m50_36_x47(z215=z215)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m50_36_x46(z215=z215, z216=z216, z217=z217)
    """State 5: End state"""
    return 0

def event_m50_36_x49(z214=_):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z214: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z214, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_100050():
    """White Spirit 06"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_36_x34(z235=745)
    Quit()

def event_m50_36_x50(z214=_, flag37=_):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z214: Boss destruction flag
    flag37: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m50_36_x42(flag37=flag37)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m50_36_x49(z214=z214)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m50_36_x43(flag37=flag37)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x51(z209=10000000, z210=730, z211=0, z212=0.2, z213=536020060):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON
    z209: Summon range
    z210: Generator ID
    z211: Appearance: Minimum time
    z212: Appearance: Maximum time
    z213: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z209, z209, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z211, 3, z212)
        IsPlayerInsidePoint(1, z209, z209, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z210)
            SetEventFlag(z213, 1)
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

def event_m50_36_x52(z202=100601, z203=10000010, z204=731, z205=104480, z206=0, z207=0, z208=536020061):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online
    z202: Summoning conditions: Global event flag
    z203: Summon range
    z204: Generator ID
    z205: Death: Global event flag
    z206: Appearance: Minimum time
    z207: Appearance: Maximum time
    z208: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z205, 1)
        CompareEventFlag(8, z202, 1)
        IsPlayerInsidePoint(8, z203, z203, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z205, 1)
            CompareStateTime(1, z206, 3, z207)
            IsPlayerInsidePoint(2, z203, z203, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z204)
                SetEventFlag(z208, 1)
                HasNpcPhantomSpawned(0, z204, 1)
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

def event_m50_36_x53(flag34=536020067, flag35=536000068):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag34: Lottery determination flag
    flag35: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag35) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag34) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m50_36_x54(z190=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z190: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z190, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m50_36_x55(flag34=536020067, z191=3, z192=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag34: Lottery determination flag
    z191: Number of appearance judgment points
    z192: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag34, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z191)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z192, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m50_36_x56(flag34=536020067, z190=14, flag35=536000068, z191=3, z192=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag34: Lottery determination flag
    z190: Random number comparison value
    flag35: Defeat flag
    z191: Number of appearance judgment points
    z192: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m50_36_x53(flag34=flag34, flag35=flag35)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m50_36_x54(z190=z190)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m50_36_x55(flag34=flag34, z191=z191, z192=z192)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m50_36_x65(flag34=flag34, z192=z192)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m50_36_x57(val11=_, z199=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val11: Appearance judgment number
    z199: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z199) == val11) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_36_x58(z195=_, z196=0, z197=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z195: Appearance judgment point ID
    z196: Minimum appearance time
    z197: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z195, z195, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z196, 3, z197)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_36_x59(z198=977, z200=_, z201=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z198: Generator ID
    z200: Appearance start point ID
    z201: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z198, z200, z201)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z198)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m50_36_x60(flag36=536000068):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag36: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag36) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m50_36_x61(z195=_, z196=0, z197=5, z198=977, val11=_, z199=10, z200=_, z201=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z195: Intrusion detection point ID
    z196: Minimum appearance time
    z197: Maximum time to appear
    z198: Generator ID
    val11: Appearance judgment number
    z199: Lottery result point variable
    z200: Appearance start point ID
    z201: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m50_36_x57(val11=val11, z199=z199)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m50_36_x58(z195=z195, z196=z196, z197=z197)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m50_36_x59(z198=z198, z200=z200, z201=z201)
    """State 4: Finish"""
    return 0

def event_m50_36_x62(z193=977, mode4=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z193: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z193)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode4) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m50_36_x63(flag36=536000068, z194=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag36: Defeat flag
    z194: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag36, 1)
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
                    SetEventFlag(z194, 1)
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

def event_m50_36_x64(flag36=536000068, z193=977, mode4=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag36: Defeat flag
    z193: Generator ID
    mode4: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m50_36_x60(flag36=flag36)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m50_36_x62(z193=z193, mode4=mode4)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m50_36_x63(flag36=flag36, z194=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m50_36_x63(flag36=flag36, z194=102755)
    """State 5: End state"""
    return 0

def event_m50_36_x65(flag34=536020067, z192=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag34: Lottery determination flag
    z192: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag34, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z192, 0)
    """State 3: End state"""
    return 0

def event_m50_36_x66(z186=50363030, lot2=60013000, flag33=536000022, goods2=53200000, z187=0, z188=0,
                     z189=5400000):
    """[Preset] Return from the memory of the old king
    z186: OBJ instance ID
    lot2: Lottery ID for item acquisition
    flag33: Item acquisition confirmation flag
    goods2: Acquisition judgment item ID
    z187: Pre-warp poly play ID
    z188: Poly Play ID after Warp
    z189: Point ID
    """
    """State 0,3: [Reproduction] Return from the memory of the ancient king_SubState"""
    call = event_m50_36_x69(z186=z186, flag33=flag33)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 4: [Condition] Return from old king's memory_SubState"""
    assert event_m50_36_x67(z186=z186, goods2=0)
    """State 2: [Execution] Return from the memory of the old king_SubState"""
    assert event_m50_36_x68(z186=z186, z187=z187, z188=z188, z189=z189)
    """State 7: End state"""
    return 0
    """State 1: [Condition] Return from the memory of the old king_Item acquisition_SubState"""
    Label('L0')
    call = event_m50_36_x67(z186=z186, goods2=goods2)
    if call.Get() == 0:
        """State 5: [Execution] Return from the memory of the old king_Item acquisition_SubState"""
        assert event_m50_36_x70(z186=z186, lot2=lot2, flag33=flag33)
    elif call.Get() == 1:
        """State 6: [Execution] Return from the memory of the old king_Item acquisition impossible_SubState"""
        assert event_m50_36_x71(z186=z186, lot2=lot2)
    """State 8: Rerun"""
    return 1

def event_m50_36_x67(z186=50363030, goods2=_):
    """[Condition] Warp to the memory of the ancient king
    z186: OBJ instance ID
    goods2: Item ID
    """
    """State 0,1: Have you examined OBJ?"""
    IsObjSearched(0, z186)
    assert ConditionGroup(0)
    """State 2: Can items be acquired?"""
    if CanGetItem(goods2, 1) != 0:
        """State 3: Available"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m50_36_x68(z186=50363030, z187=0, z188=0, z189=5400000):
    """[Execution] Warp to the memory of the ancient king
    z186: OBJ instance ID
    z187: Pre-warp poly play ID
    z188: Poly Play ID after Warp
    z189: Point ID
    """
    """State 0,4: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 1: Key guide disabled: 10"""
    ChangeObjState(z186, 10)
    """State 2: Wait for transition completion"""
    CompareObjState(0, z186, 10, 0)
    assert ConditionGroup(0)
    """State 3: End of global timer"""
    EndGlobalTimer(4)
    """State 6: [Lib] Warp between maps after poly play_SubState"""
    assert event_m50_36_x0(z162=z187, z163=z188, z164=50360000, z146=z189)
    """State 5: Multiplayer prohibited state: OFF"""
    ProhibitMultiplayer(0)
    """State 7: End state"""
    return 0

def event_m50_36_x69(z186=50363030, flag33=536000022):
    """[Reproduction] Warp to the memory of the ancient king
    z186: OBJ instance ID
    flag33: Item acquisition confirmation flag
    """
    """State 0,2: Key guide activation: 30"""
    ChangeObjState(z186, 30)
    """State 3: Wait for transition"""
    assert CompareObjStateId(z186, 30, 0)
    """State 1: Did you get the item?"""
    if GetEventFlag(flag33) != 0:
        """State 5: It has been acquired"""
        return 1
    else:
        """State 4: Unacquired"""
        return 0

def event_m50_36_x70(z186=50363030, lot2=60013000, flag33=536000022):
    """[Execution] Warp _ item acquisition to the memory of the ancient king
    z186: OBJ instance ID
    lot2: Lottery ID for item acquisition
    flag33: Item acquisition confirmation flag
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z186, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z186, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60013000:Smelter Wedge
    AwardItem(lot2, 1)
    """State 4: Turn on the item acquisition flag"""
    SetEventFlag(flag33, 1)
    SetEventFlag(100905, 1)
    """State 5: End state"""
    return 0

def event_m50_36_x71(z186=50363030, lot2=60013000):
    """[Execution] Warp to old king's memory
    z186: OBJ instance ID
    lot2: Lottery ID for item acquisition
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z186, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z186, 10, 0)
    assert ConditionGroup(0)
    """State 3: Acquisition failure window display"""
    # lot:60013000:Smelter Wedge
    DisplayItemAwardFailure(lot2, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 4: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 5: End state"""
    return 0

def event_m50_36_x72(z184=_, z185=_):
    """[Preset] Break the ash mountain and treasure
    z184: Instance ID of Haiyama OBJ
    z185: Treasure OBJ instance ID
    """
    """State 0,1: [Reproduction] Treasure _SubState when breaking the ash mountain"""
    call = event_m50_36_x73(z184=z184, z185=z185)
    if call.Get() == 0:
        """State 3: [Condition] Treasure _SubState when the ash mountain is destroyed"""
        assert event_m50_36_x74(z184=z184)
        """State 2: [Execution] Breaking the pile of ash treasure _SubState"""
        assert event_m50_36_x75(z185=z185)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x73(z184=_, z185=_):
    """[Reproduction] Treasure when the mountain of ash is broken
    z184: Instance ID of Haiyama OBJ
    z185: Treasure OBJ instance ID
    """
    """State 0,1: State determination of Haiyama OBJ"""
    if CompareObjStateId(z184, 20, 0):
        """State 4: Haiyama: destroyed"""
        return 1
    else:
        """State 2: Hide treasure"""
        ChangeDrawHit(z185, 0)
        """State 3: Haeyama: Undestructed"""
        return 0

def event_m50_36_x74(z184=_):
    """[Condition] Treasure when the mountain of ash is broken
    z184: Instance ID of Haiyama OBJ
    """
    """State 0,1: Did you destroy Haiyama OBJ?"""
    CompareObjState(0, z184, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x75(z185=_):
    """[Execution] Break the ash mountain and treasure
    z185: Treasure OBJ instance ID
    """
    """State 0,1: Treasure display"""
    ChangeDrawHit(z185, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x76(z183=50361200):
    """[Reproduction] Two pairs of rotating fire-blowing cows
    z183: Cow OBJ instance ID
    """
    """State 0,1: Judgment of fire-blown cow"""
    if CompareObjStateId(z183, 10, 1):
        """State 3,4: Waiting for stop"""
        assert CompareObjStateId(z183, 10, 0)
    else:
        pass
    """State 2,5: End state"""
    return 0

def event_m50_36_x77(z183=50361200):
    """[Conditions] Two pairs of rotating fired cows
    z183: Cow OBJ instance ID
    """
    """State 0,1: Damage judgment"""
    IsObjDamaged(0, z183, -1, -1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x78(z183=50361200):
    """[Execution] 2 pairs of fire-blowing cows rotating
    z183: Cow OBJ instance ID
    """
    """State 0,1: Rotating fire bull"""
    ChangeObjState(z183, 30)
    """State 2: Wait for rotation to end"""
    CompareObjState(0, z183, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x79(z183=50361200):
    """[Preset] Two pairs of fire-blowing cows that rotate
    z183: Cow OBJ instance ID
    """
    """State 0,1: [Reproduction] Two pairs of fire-blowing cows _SubState rotating"""
    assert event_m50_36_x76(z183=z183)
    """State 3: [Condition] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m50_36_x77(z183=z183)
    """State 2: [Execution] Two pairs of rotating fire-blowing cows_SubState"""
    assert event_m50_36_x78(z183=z183)
    """State 4: Rerun"""
    return 0

def event_m50_36_x80(z151=_, z154=_, z153=_, z156=_, z157=_, z158=_):
    """[Execution] A fire-blowing cow that slides
    z151: Cow OBJ instance ID
    z154: Mobile OBJ state ID
    z153: Movement end OBJ state ID
    z156: Before operation_Navigation change point ID
    z157: Active_Navigation change point ID
    z158: After operation_navi change point ID
    """
    """State 0,3: Navigation mesh change"""
    AddNavimeshAttribute(z156, 2)
    AddNavimeshAttribute(z157, 2)
    AddNavimeshAttribute(z158, 2)
    """State 1: Slide movement of fire-blown cow"""
    ChangeObjState(z151, z154)
    """State 2: Waiting for movement to end"""
    CompareObjState(0, z151, z153, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change_2"""
    DeleteNavimeshAttribute(z156, 2)
    DeleteNavimeshAttribute(z157, 2)
    AddNavimeshAttribute(z158, 2)
    """State 5: End state"""
    return 0

def event_m50_36_x81(z88=_):
    """[Conditions] Sliding fire-blown cow
    z88: Cow OBJ instance ID
    """
    """State 0,1: Damage judgment"""
    IsObjDamaged(0, z88, -1, -3, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x82(z180=50360400, z181=5000000, z182=5000010):
    """[Preset] Door that opens with DLC purchase
    z180: Door OBJ instance ID
    z181: Navigation switching point ID
    z182: Judgment point ID
    """
    """State 0,1: [Reproduction] Doors opened with DLC purchase_SubState"""
    call = event_m50_36_x83(z180=z180, z181=z181)
    if call.Get() == 0:
        """State 3: [Conditions] Doors opened by DLC purchase_SubState"""
        call = event_m50_36_x85(z180=z180, z182=z182)
        if call.Get() == 0:
            """State 6: [Execution] Door opened by DLC purchase_Manual_SubState"""
            assert event_m50_36_x88(z180=z180, z181=z181)
            Goto('L0')
        elif call.Get() == 2:
            """State 5: [Execution] Door opened with DLC purchase_Auto_SubState"""
            assert event_m50_36_x87(z180=z180, z181=z181)
            Goto('L0')
        elif call.Get() == 1:
            """State 7: [Execution] Door that opens with DLC purchase_No access_Front_SubState"""
            assert event_m50_36_x89(z180=z180)
        elif call.Get() == 3:
            """State 8: [Execution] Door opened with DLC purchase_No access_Back_SubState"""
            assert event_m50_36_x90(z180=z180)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Conditions] Doors opened by DLC purchase_Guest_SubState"""
        assert event_m50_36_x86(z180=z180)
        """State 2: [Execution] Door opened with DLC purchase_Guest_SubState"""
        assert event_m50_36_x84(z180=z180, z181=z181)
    """State 10: Finish"""
    Label('L0')
    return 1

def event_m50_36_x83(z180=50360400, z181=5000000):
    """[Reproduction] Door opened with DLC purchase
    z180: Door OBJ instance ID
    z181: Navigation switching point ID
    """
    """State 0,2: Navigation switching_initialization"""
    AddNavimeshAttribute(z181, 2)
    """State 1: Host?"""
    if IsGuest() != 1:
        """State 3: Safety: Door initialization"""
        InitializeObj(z180)
        assert CompareObjStateId(z180, 10, 0)
        """State 4: Disable key guide"""
        DisableObjKeyGuide(z180, 1)
        """State 5: Not passed"""
        return 0
    else:
        """State 6: The guests"""
        return 1

def event_m50_36_x84(z180=50360400, z181=5000000):
    """[Execution] Door opened with DLC purchase_Guest
    z180: King's door OBJ instance ID
    z181: Navigation switching point ID
    """
    """State 0,1: Change navigation"""
    DeleteNavimeshAttribute(z181, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x85(z180=50360400, z182=5000010):
    """[Conditions] Doors opened by DLC purchase
    z180: Door OBJ instance ID
    z182: Judgment point ID
    """
    """State 0,2: Distance judgment or point judgment"""
    CompareObjPlayerDistance(0, z180, 4, 5)
    SetConditionGroup(1, 8)
    IsPlayerInsidePoint(8, z182, z182, 1)
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

def event_m50_36_x86(z180=50360400):
    """[Conditions] Doors opened with DLC purchase_Guest
    z180: Door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z180, 20, 0)
    assert ConditionGroup(0)
    """State 2: Mural opened"""
    return 0

def event_m50_36_x87(z180=50360400, z181=5000000):
    """[Execution] Door opened with DLC purchase_Auto
    z180: Door OBJ instance ID
    z181: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z180, 20)
    """State 2: Waiting for the door to finish"""
    CompareObjState(0, z180, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z181, 2)
    """State 4: End state"""
    return 0

def event_m50_36_x88(z180=50360400, z181=5000000):
    """[Execution] Door opened with DLC purchase_Manual
    z180: Door OBJ instance ID
    z181: Navigation switching point ID
    """
    """State 0,3: Activate key guide"""
    DisableObjKeyGuide(z180, 0)
    """State 1: Waiting for the door to finish"""
    CompareObjState(0, z180, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation switching"""
    DeleteNavimeshAttribute(z181, 2)
    """State 4: End state"""
    return 0

def event_m50_36_x89(z180=50360400):
    """[Execution] Door opened with DLC purchase
    z180: Door OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z180, 8, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x90(z180=50360400):
    """[Execution] Door opened with DLC purchase
    z180: Door OBJ instance ID
    """
    """State 0,3: Did you approach the door?"""
    CompareObjPlayerDistance(0, z180, 4, 5)
    assert ConditionGroup(0)
    """State 1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z180, 8, 3)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_36_x91(z177=_, z178=_):
    """[Reproduction] Iron lattice that opens with a lever
    z177: Iron lattice OBJ instance ID
    z178: Navigation change point ID
    """
    """State 0,1: Is the iron grid open?"""
    if CompareObjStateId(z177, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z177, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z178, 2)
        """State 6: Already in operation"""
        return 1
    else:
        """State 4: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z178, 2)
        """State 5: Not in operation"""
        return 0

def event_m50_36_x92(z176=_):
    """[Conditions] Iron grid that opens with lever
    z176: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z176, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x93(z177=_, z178=_, z179=_):
    """[Execution] Iron grid that opens with lever
    z177: Iron lattice OBJ instance ID
    z178: Navigation change point ID
    z179: Wait until navigation switching
    """
    """State 0,2: The iron bar opens: 70"""
    ChangeObjState(z177, 70)
    """State 4: weight"""
    CompareStateTime(0, z179, 3, z179)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z178, 2)
    """State 3: Waiting for the opening of the iron lattice"""
    CompareObjState(0, z177, 20, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m50_36_x94(z176=_, z177=_, z178=_, z179=_):
    """[Preset] Opening with a lever
    z176: Lever OBJ instance ID
    z177: Iron lattice OBJ instance ID
    z178: Navigation change point ID
    z179: Wait until navigation switching
    """
    """State 0,1: [Reproduction] Iron lattice _SubState opened with lever"""
    call = event_m50_36_x91(z177=z177, z178=z178)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Iron lattice that opens with lever_SubState"""
        assert event_m50_36_x92(z176=z176)
        """State 2: [Execution] Iron lattices opened by lever_SubState"""
        assert event_m50_36_x93(z177=z177, z178=z178, z179=z179)
    """State 4: End state"""
    return 0

def event_m50_36_x95(z174=_, z175=_):
    """[Reproduction] Large door opened by lever
    z174: Door OBJ instance ID
    z175: Navigation change point ID
    """
    """State 0,1: Is the big door open?"""
    if CompareObjStateId(z174, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z174, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z175, 2)
        """State 5: Already in operation"""
        return 1
    else:
        """State 4: Not in operation"""
        return 0

def event_m50_36_x96(z49=_):
    """[Conditions] Large door opened with lever
    z49: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z49, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x97(z174=_, z175=_):
    """[Execution] Large door opened by lever
    z174: Door OBJ instance ID
    z175: Navigation change point ID
    """
    """State 0,2: The big door opens: 70"""
    ChangeObjState(z174, 70)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z174, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z175, 2)
    """State 4: End state"""
    return 0

def event_m50_36_x98(z173=_, z174=_, z175=_):
    """[Preset] Large door opened by lever
    z173: Lever OBJ instance ID
    z174: Door OBJ instance ID
    z175: Navigation change point ID
    """
    """State 0,1: [Reproduction] Large door opened with lever_SubState"""
    call = event_m50_36_x95(z174=z174, z175=z175)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Large door opened with lever_SubState"""
        assert event_m50_36_x96(z49=z173)
        """State 2: [Execution] Large door opened with lever_SubState"""
        assert event_m50_36_x97(z174=z174, z175=z175)
    """State 4: End state"""
    return 0

def event_m50_36_x99(z166=905, z167=71, z168=70, z169=50362200, z170=50362201, z171=93050011, flag32=536000091):
    """[Preset] Flame linked to the Demon Knight Kai action
    z166: Boss generator ID
    z167: State ID with stone statue on
    z168: State ID with stone statue flame OFF
    z169: OBJ instance ID of stone statue 1
    z170: OBJ instance ID of stone statue 2
    z171: Boss special state effect ID
    flag32: Boss destruction flag
    """
    """State 0,1: [Reproduction] Flame _SubState linked to Demon Knight Kai action"""
    call = event_m50_36_x100(flag32=flag32)
    if call.Get() == 0:
        """State 3: [Condition] Flame linked to the Demon Knight Kai action_Boss goes to "anger" state_SubState"""
        call = event_m50_36_x101(z166=z166, z171=z171)
        if call.Get() == 0:
            """State 2: [Execution] Flame linked to Demon Knight Kai action_Lights off_SubState"""
            assert event_m50_36_x103(z168=z168, z169=z169, z170=z170, z172=30)
            """State 4: [Condition] Flame linked to Demon Knight Kai action_Boss dies_SubState"""
            assert event_m50_36_x102(z166=z166)
            """State 5: [Execution] Flame_Lit_SubState linked to Demon Knight Kai action"""
            assert event_m50_36_x103(z168=z167, z169=z169, z170=z170, z172=10)
        elif call.Get() == 1:
            pass
    elif call.Get() == 1:
        pass
    """State 6: Finish"""
    return 0

def event_m50_36_100100():
    """Dark Spirit 01"""
    """State 0,2: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_36_x51(z209=10000000, z210=730, z211=0, z212=0.2, z213=536020060)
    Quit()
    """Unused"""
    """State 1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m50_36_x40(z223=10000000, z224=730, z225=0, z226=0.2)
    Quit()

def event_m50_36_x100(flag32=536000091):
    """[Reproduction] Flame linked to Demon Knight Kai action
    flag32: Boss destruction flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag32) != 1:
        """State 2: Undefeated"""
        return 0
    else:
        """State 3: Defeated"""
        return 1

def event_m50_36_x101(z166=905, z171=93050011):
    """[Conditions] Flame_Boss linked to Demon Knight Kai's action is in "anger" state
    z166: Boss generator ID
    z171: Boss special state effect ID
    """
    """State 0,1: Boss status judgment"""
    ChrHasSpEffect(0, z166, z171, 1)
    IsChrDead(1, z166)
    if ConditionGroup(0):
        """State 2: Turn off due to status change"""
        return 0
    elif ConditionGroup(1):
        """State 3: Boss death"""
        return 1

def event_m50_36_x102(z166=905):
    """[Condition] Flame boss dies in conjunction with Demon Knight Kai action
    z166: Boss generator ID
    """
    """State 0,1: Boss status judgment"""
    IsChrDead(0, z166)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x103(z168=_, z169=50362200, z170=50362201, z172=_):
    """[Execution] Flame linked to Demon Knight Kai action
    z168: OBJ state ID for ON / OFF
    z169: OBJ instance ID of stone statue 1
    z170: OBJ instance ID of stone statue 2
    z172: ON / OFF completion confirmation OBJ state ID
    """
    """State 0,1: OBJ status change"""
    ChangeObjState(z169, z168)
    ChangeObjState(z170, z168)
    """State 2: Has the OBJ status change been completed?"""
    CompareObjState(8, z169, z172, 0)
    CompareObjState(8, z170, z172, 0)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m50_36_x104(z161=50363060, flag31=101061):
    """[Reproduction] Invading the memory of the ancient king
    z161: OBJ instance ID to check
    flag31: Boss destruction flag
    """
    """State 0,4: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Are you destroying a smoke knight?"""
    if GetEventFlag(flag31) != 0:
        """State 3: SFX generation: 40"""
        ChangeObjState(z161, 40)
    else:
        pass
    """State 1: Disable key guide"""
    DisableObjKeyGuide(z161, 1)
    """State 5: End state"""
    return 0
    """State 6: The guests"""
    Label('L0')
    return 1

def event_m50_36_x105(z161=50363060, flag31=101061):
    """[Condition] Invade the memory of the ancient king
    z161: OBJ instance ID to check
    flag31: Boss destruction flag
    """
    """State 0,1: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z161, 0)
    """State 2: Did you investigate OBJ or became multi or destroyed boss?"""
    IsObjSearched(0, z161)
    IsMultiplayer(1, 1, 1)
    CompareEventFlag(2, flag31, 1)
    if ConditionGroup(2):
        """State 5: SFX generation: 40"""
        ChangeObjState(z161, 40)
        """State 6: Was OBJ checked or multi?"""
        IsObjSearched(0, z161)
        IsMultiplayer(1, 1, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 4: Do you have an ash mist core? Are you destroying a smoke knight?"""
            Label('L0')
            # goods:50910000:Ashen Mist Heart
            DoesPlayerHaveItem(8, 50910000, 1, 3, 1, 1, 0)
            CompareEventFlag(8, flag31, 1)
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

def event_m50_36_x106(z161=50363060, z162=503610, z163=0, z164=50360000, z165=5300000):
    """[Execution] Invade the memory of the ancient king
    z161: OBJ instance ID to check
    z162: Pre-warp poly play ID
    z163: Poly Play ID after Warp
    z164: Map ID
    z165: Point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z161, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: Timer reset for time limit"""
    EndGlobalTimer(4)
    """State 5: [Lib] Warp between maps after poly play_SubState"""
    assert event_m50_36_x0(z162=z162, z163=z163, z164=z164, z146=z165)
    """State 4: Multiplayer prohibited state: OFF"""
    ProhibitMultiplayer(0)
    """State 6: End state"""
    return 0

def event_m50_36_x107(z161=50363060):
    """[Execution] Invasion of old king's memory
    z161: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z161, 1)
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

def event_m50_36_x109(z161=50363060, z162=503610, z163=0, z164=50360000, z165=5300000, flag31=101061):
    """[Preset] Invade the memory of the ancient king
    z161: OBJ instance ID to check
    z162: Pre-warp poly play ID
    z163: Poly Play ID after Warp
    z164: Map ID
    z165: Point ID
    flag31: Boss destruction flag
    """
    """State 0,1: [Reproduction] Intrusion into the memory of the ancient king_SubState"""
    call = event_m50_36_x104(z161=z161, flag31=flag31)
    if call.Get() == 0:
        """State 5: [Condition] Invade the memory of the old king_SubState"""
        call = event_m50_36_x105(z161=z161, flag31=flag31)
        if call.Get() == 1:
            """State 3: [Execution] Intrusion into the memory of the old king_Disable Key Guide_SubState"""
            assert event_m50_36_x107(z161=z161)
        elif call.Get() == 2:
            """State 4: [Execution] Intrusion into the memory of the old king _Nothing happens_SubState"""
            assert event_m50_36_x108()
        elif call.Get() == 0:
            """State 2: [Execution] Intrusion into the memory of the ancient king_SubState"""
            assert event_m50_36_x106(z161=z161, z162=z162, z163=z163, z164=z164, z165=z165)
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
    event_m50_36_x52(z202=100601, z203=10000010, z204=731, z205=104480, z206=0, z207=0, z208=536020061)
    Quit()
    """Unused"""
    """State 1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m50_36_x39(z227=100601, z228=10000010, z229=731, z230=104480, z231=0, z232=0)
    Quit()

def event_m50_36_x110(z143=4, z144=0, val7=1050, val8=1070, z145=1080, action2=2012, action3=2013, z146=5400000):
    """[Preset] Memory time limit of the ancient king
    z143: Global timer ID
    z144: Time limit notification flag
    val7: Execution start time of the first phase process
    val8: Execution start time of the second phase process
    z145: Execution start time of the third phase process
    action2: Text ID to display in the first phase
    action3: Text ID to display in the third phase
    z146: Return Warp Point ID
    """
    """State 0,12: [Reproduction] Time limit of memory of the old king_Start judgment_SubState"""
    call = event_m50_36_x136()
    if call.Get() == 0:
        """State 14: [Condition] Memory time limit_start judgment_SubState"""
        assert event_m50_36_x137()
        """State 13: [Execution] Memory time limit of old king_Start judgment_Empty_SubState"""
        assert event_m50_36_x138()
        """State 1: [Reproduction] Memory time limit of the ancient king_SubState"""
        call = event_m50_36_x111(z143=z143, z144=z144, val7=val7, val8=val8)
        if call.Get() == 3:
            """State 8: [Conditions & Execution] Memory time limit of old king_0th phase_SubState"""
            # action:2011:"One cannot reside within memory for long"
            assert event_m50_36_x112(z143=z143, z160=5, action4=2011)
            """State 2: [Conditions & Execution] Memory time limit of the old king_First Phase_SubState"""
            assert event_m50_36_x113(z143=z143, val7=val7, action2=action2)
            """State 3: [Conditions & Execution] Memory time limit of old king_Second Phase_SubState"""
            assert event_m50_36_x114(z143=z143, val8=val8, z144=z144)
            """State 4: [Conditions & Execution] Memory time limit of the ancient king_3rd phase_SubState"""
            assert event_m50_36_x115(z143=z143, z145=z145, action3=action3, z146=z146)
        elif call.Get() == 0:
            """State 9: [Conditions & Execution] Memory time limit of the ancient king_First Phase_2_SubState"""
            assert event_m50_36_x113(z143=z143, val7=val7, action2=action2)
            """State 5: [Conditions & Execution] Memory time limit of old king_Second Phase_2_SubState"""
            assert event_m50_36_x114(z143=z143, val8=val8, z144=z144)
            """State 6: [Conditions & Execution] Memory time limit of the ancient king_3rd phase_2_SubState"""
            assert event_m50_36_x115(z143=z143, z145=z145, action3=action3, z146=z146)
        elif call.Get() == 1:
            """State 10: [Conditions & Execution] Memory time limit of the ancient king_Second Phase_3_SubState"""
            assert event_m50_36_x114(z143=z143, val8=val8, z144=z144)
            """State 7: [Conditions & Execution] Memory time limit of the ancient king_3rd phase_3_SubState"""
            assert event_m50_36_x115(z143=z143, z145=z145, action3=action3, z146=z146)
        elif call.Get() == 2:
            """State 11: [Conditions & Execution] Memory time limit of old king_3rd phase_4_SubState"""
            assert event_m50_36_x115(z143=z143, z145=z145, action3=action3, z146=z146)
    elif call.Get() == 1:
        pass
    """State 15: End state"""
    return 0

def event_m50_36_x111(z143=4, z144=0, val7=1050, val8=1070):
    """[Reproduction] Time limit of memory of the ancient king
    z143: Global timer ID
    z144: Time limit notification flag
    val7: Execution start time of the first phase process
    val8: Execution start time of the second phase process
    """
    """State 0,1: Timer start judgment"""
    if (GetGlobalTimerTime(z143) > val8) != 0:
        """State 5: Restart global timer_3"""
        RestartGlobalTimer(z143)
        """State 6: Time limit notification flag ON"""
        SetEventFlag(z144, 1)
        """State 9: From the third phase"""
        return 2
    elif (GetGlobalTimerTime(z143) > val7) != 0:
        """State 4: Restart global timer_2"""
        RestartGlobalTimer(z143)
        """State 8: From the second phase"""
        return 1
    elif (GetGlobalTimerTime(z143) > 1) != 0:
        """State 3: Restart global timer"""
        RestartGlobalTimer(z143)
        """State 7: From the first phase"""
        return 0
    else:
        """State 2: Starting the global timer"""
        StartGlobalTimer(z143)
        """State 10: From the 0th phase"""
        return 3

def event_m50_36_x112(z143=4, z160=5, action4=2011):
    """[Conditions & Execution] Time limit of memory of the ancient king_0th phase
    z143: Global timer ID
    z160: Execution start time of the 0th phase process
    action4: Text ID displayed in the 0th phase
    """
    """State 0,2: Is it in game?"""
    assert InGame() != 0
    """State 3: Wait for a fixed time or multi judgment or judgment within point"""
    CompareStateTime(0, z160, 3, z160)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 5: Pause timer"""
        SuspendGlobalTimer(z143)
        """State 4: Rerun"""
        RestartMachine()
        Quit()
    elif ConditionGroup(0):
        """State 1: Event message display"""
        # action:2011:"One cannot reside within memory for long"
        DisplayEventMessage(action4, 0, 0, 0)
        """State 6: End state"""
        return 0

def event_m50_36_x113(z143=4, val7=1050, action2=2012):
    """[Conditions & Execution] Time limit of memory of old king _First phase
    z143: Global timer ID
    val7: Execution start time of the first phase process
    action2: Text ID to display in the first phase
    """
    """State 0,1: Time limit waiting or multi judgment or judgment within point"""
    CompareGlobalTimer(0, z143, val7, 3)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 4: Pause timer"""
        SuspendGlobalTimer(z143)
        """State 3: Rerun"""
        RestartMachine()
        Quit()
    elif ConditionGroup(0):
        """State 2: Event message display"""
        # action:2012:"The ashen mist has thinned..."
        DisplayEventMessage(action2, 0, 0, 0)
        """State 5: End state"""
        return 0

def event_m50_36_x114(z143=4, val8=1070, z144=0):
    """[Conditions & Execution] Memory time limit of the ancient king _ 2nd phase
    z143: Global timer ID
    val8: Execution start time of the second phase process
    z144: Time limit notification flag
    """
    """State 0,1: Time limit waiting or multi judgment or judgment within point"""
    CompareGlobalTimer(0, z143, val8, 3)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 4: Pause timer"""
        SuspendGlobalTimer(z143)
        """State 3: Rerun"""
        RestartMachine()
        Quit()
    elif ConditionGroup(0):
        """State 2: Time limit notification flag ON"""
        SetEventFlag(z144, 1)
        """State 5: End state"""
        return 0

def event_m50_36_x115(z143=4, z145=1080, action3=2013, z146=5400000):
    """[Conditions & Execution] Time limit of memory of the ancient king_3rd phase
    z143: Global timer ID
    z145: Execution start time of the third phase process
    action3: Text ID to display in the third phase
    z146: Return Warp Point ID
    """
    """State 0,1: Time limit waiting or multi judgment or judgment within point"""
    CompareGlobalTimer(0, z143, z145, 3)
    IsMultiplayer(1, 1, 1)
    IsPlayerInsidePoint(1, 5500000, 5500001, 1)
    if ConditionGroup(1):
        """State 5: Pause timer"""
        SuspendGlobalTimer(z143)
        """State 4: Rerun"""
        RestartMachine()
        Quit()
    elif ConditionGroup(0):
        """State 6: Multiplayer prohibited state: ON"""
        ProhibitMultiplayer(1)
        """State 2: Event message display"""
        # action:2013:"The ashen mist fades..."
        DisplayEventMessage(action3, 0, 0, 0)
        """State 3: Timer reset"""
        EndGlobalTimer(z143)
        """State 8: [Lib] Warp between maps after poly play_SubState"""
        assert event_m50_36_x0(z162=0, z163=0, z164=50360000, z146=z146)
        """State 7: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
        """State 9: End state"""
        return 0

def event_m50_36_x116(z159=50363040):
    """[Preset] Run the facility
    z159: Launch OBJ instance ID
    """
    """State 0,1: [Reproduction] _SubState to operate the facility"""
    call = event_m50_36_x117(z159=z159)
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
    call = event_m50_36_x122(z159=z159)
    if call.Get() == 0:
        """State 3: [Execution] Operate the facility_Host_Available_SubState"""
        call = event_m50_36_x119(z159=z159)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: End of operation"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Run the facility_Host_Unlockable_SubState"""
        assert event_m50_36_x120(z159=z159)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Operating the facility_Guest_SubState"""
    Label('L1')
    assert event_m50_36_x121(z159=z159)
    """State 2: [Execution] Run the facility_Guest_Empty_SubState"""
    assert event_m50_36_x118()
    """State 9: Guest termination"""
    return 2

def event_m50_36_x117(z159=50363040):
    """[Reproduction] Operate the facility
    z159: Launch OBJ instance ID
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
    if CompareObjStateId(z159, 20, 0):
        pass
    elif CompareObjStateId(z159, 76, 0):
        pass
    elif CompareObjStateId(z159, 74, 0):
        pass
    elif CompareObjStateId(z159, 70, 0):
        pass
    else:
        Goto('L1')
    """State 7: After execution"""
    return 2
    """State 3: Safety: Still waiting for operation?"""
    Label('L1')
    if CompareObjStateId(z159, 30, 1):
        pass
    else:
        """State 4: Returning to the initial state: 10"""
        ChangeObjState(z159, 10)
        assert CompareObjStateId(z159, 10, 0)
    """State 6: Before execution"""
    return 1

def event_m50_36_x118():
    """[Execution] Operate the facility_Guest_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x119(z159=50363040):
    """[Execution] Operate the facility_Host_Available
    z159: Active OBJ instance ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:53100000:Scorching Iron Scepter
    DisplayYesNoMenu(1002, 1.8, z159, 190, 2, 53100000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 6: Wait for operation transition: 30"""
        ChangeObjState(z159, 30)
        assert CompareObjStateId(z159, 30, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z159, 38, 16)
        assert PlayerIsInEventAction(16) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 16, 0)
        # goods:53100000:Scorching Iron Scepter
        DoesPlayerHaveItem(0, 53100000, 0, 5, 1, 1, 0)
        CompareObjState(1, z159, 74, 0)
        CompareObjState(1, z159, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Fire sashimi stick consumption"""
            # goods:53100000:Scorching Iron Scepter
            ConsumeItem(53100000, 1)
            assert CompareObjStateId(z159, 20, 0)
            """State 8: End of operation"""
            return 0
    else:
        pass
    """State 7: Returning to the initial state: 10"""
    ChangeObjState(z159, 10)
    """State 9: Rerun"""
    return 1

def event_m50_36_x120(z159=50363040):
    """[Execution] Operate the facility_Host_Unlockable
    z159: Launch OBJ instance ID
    """
    """State 0,2: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:53100000:Scorching Iron Scepter
    DisplayOkMenu(1013, 0, 0, z159, 190, 2, 53100000, 0)
    assert OkMenuDisplay() != 1
    """State 1: Wait for initial state"""
    CompareObjState(0, z159, 10, 0)
    assert ConditionGroup(0)
    """State 3: Unsuccessful unlocking_rerun"""
    return 0

def event_m50_36_x121(z159=50363040):
    """[Condition] _Guest to operate the facility
    z159: Launch OBJ instance ID
    """
    """State 0,1: Wait for completion"""
    CompareObjState(0, z159, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x122(z159=50363040):
    """[Condition] _Host to operate the facility
    z159: Launch OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z159)
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

def event_m50_36_x123(z151=_, z152=_, z153=_, z154=_, z155=_, z156=_, z157=_, z158=_):
    """[Preset] Fire-blowing cow that slides
    z151: Cow OBJ instance ID
    z152: OBJ state ID before operation
    z153: OBJ state ID after operation
    z154: OBJ state ID in operation from before operation
    z155: OBJ state ID that has been in operation since operation
    z156: Before operation_Navigation change point ID
    z157: Active_Navigation change point ID
    z158: After operation_navi change point ID
    """
    """State 0,5: [Reproduction] Sliding fire-blowing cow_Initialized version_SubState"""
    call = event_m50_36_x124(z151=z151, z152=z152, z153=z153, z154=z154, z155=z155, z156=z156, z157=z157,
                             z158=z158)
    if call.Get() == 0:
        """State 2: [Conditions] Sliding fire-blowing cow_SubState"""
        assert event_m50_36_x81(z88=z151)
        """State 1: [Execution] Sliding fire bull_SubState"""
        assert event_m50_36_x80(z151=z151, z154=z154, z153=z153, z156=z156, z157=z157, z158=z158)
    elif call.Get() == 1:
        """State 3: [Condition] Sliding fire-blowing cow_2_SubState"""
        assert event_m50_36_x81(z88=z151)
        """State 4: [Execution] Sliding fire-blown cow_2_SubState"""
        assert event_m50_36_x80(z151=z151, z154=z155, z153=z152, z156=z158, z157=z157, z158=z156)
    """State 6: Rerun"""
    return 0

def event_m50_36_x124(z151=_, z152=_, z153=_, z154=_, z155=_, z156=_, z157=_, z158=_):
    """[Reproduction] Sliding fire-blowing cow_initialization version
    z151: Cow OBJ instance ID
    z152: OBJ state ID before operation
    z153: OBJ state ID after operation
    z154: OBJ state ID in operation from before operation
    z155: OBJ state ID that has been in operation since operation
    z156: Before operation_Navigation change point ID
    z157: Active_Navigation change point ID
    z158: After operation_navi change point ID
    """
    """State 0,16: Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 8: Is the fire-blown cow before initialization?"""
    if CompareObjStateId(z151, 10, 0):
        """State 9: Initialize"""
        ChangeObjState(z151, z152)
        assert CompareObjStateId(z151, z152, 0)
    else:
        pass
    """State 1: Judgment of fire-blown cow"""
    if CompareObjStateId(z151, z154, 0):
        """State 4,14: Navi Mesh Change_5"""
        AddNavimeshAttribute(z156, 2)
        AddNavimeshAttribute(z157, 2)
        AddNavimeshAttribute(z158, 2)
        """State 7: Waiting for completion of operation"""
        assert CompareObjStateId(z151, z153, 0)
        """State 15: Navi Mesh Change_6"""
        DeleteNavimeshAttribute(z157, 2)
        DeleteNavimeshAttribute(z156, 2)
        AddNavimeshAttribute(z158, 2)
    elif CompareObjStateId(z151, z155, 0):
        """State 5,12: Navi Mesh Change_2"""
        AddNavimeshAttribute(z156, 2)
        AddNavimeshAttribute(z157, 2)
        AddNavimeshAttribute(z158, 2)
        """State 6: Wait for initial state"""
        assert CompareObjStateId(z151, z152, 0)
        """State 11: Navi Mesh Change_3"""
        DeleteNavimeshAttribute(z157, 2)
        DeleteNavimeshAttribute(z158, 2)
        AddNavimeshAttribute(z156, 2)
        """State 17: Fire-blown cow: initial state"""
        Label('L0')
        return 0
    elif CompareObjStateId(z151, z152, 0):
        """State 2,10: Navigation mesh change"""
        DeleteNavimeshAttribute(z157, 2)
        DeleteNavimeshAttribute(z158, 2)
        AddNavimeshAttribute(z156, 2)
        Goto('L0')
    elif CompareObjStateId(z151, z153, 0):
        """State 3,13: Navi Mesh Change_4"""
        DeleteNavimeshAttribute(z157, 2)
        DeleteNavimeshAttribute(z156, 2)
        AddNavimeshAttribute(z158, 2)
    """State 18: Fire-blown cow: End of operation"""
    return 1

def event_m50_36_x125(flag30=536000049):
    """[Reproduction] Smoke damage caused by a spear image
    flag30: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(flag30) != 0:
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

def event_m50_36_x126(flag29=_):
    """[Condition] Smoke damage caused by the image of a spider
    flag29: Destruction flag
    """
    """State 0,1: Waiting for destruction of eagle statue"""
    CompareEventFlag(0, flag29, 1)
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

def event_m50_36_x128(flag30=536000049):
    """[Preset] Smoke damage caused by a spear image
    flag30: Destruction flag
    """
    """State 0,1: [Reproduction] Smoke damage caused by a spear image_Isolated Island_SubState"""
    call = event_m50_36_x125(flag30=flag30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Smoke damage due to the image of a spider _SubState"""
        assert event_m50_36_x126(flag29=flag30)
        """State 2: [Execution] Smoke damage caused by a spider image_Isolated Island_SubState"""
        assert event_m50_36_x127()
    """State 4: End state"""
    return 0

def event_m50_36_x129(flag29=536000048):
    """[Reproduction] Smoke damage caused by a spider image_Lobby
    flag29: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(flag29) != 0:
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

def event_m50_36_x131(flag29=536000048):
    """[Preset] Smoke damage caused by a spear image_Lobby
    flag29: Destruction flag
    """
    """State 0,2: [Reproduction] Smoke damage caused by a spear image_Lobby_SubState"""
    call = event_m50_36_x129(flag29=flag29)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Smoke damage due to the image of a spider _SubState"""
        assert event_m50_36_x126(flag29=flag29)
        """State 3: [Execution] Smoke damage caused by a spear image_Lobby_SubState"""
        assert event_m50_36_x130()
    """State 4: End state"""
    return 0

def event_m50_36_x132(flag27=536000049, flag28=536000048):
    """[Reproduction] Smoke filter change by the image of the frog
    flag27: Isolated island_destruction flag
    flag28: Lobby_Destroy flag
    """
    """State 0,1: Are both eagle statues destroyed?"""
    if GetEventFlag(flag27) != 0 and GetEventFlag(flag28) != 0:
        """State 2: Destroyed"""
        return 0
    else:
        """State 3: Not destroyed"""
        return 1

def event_m50_36_x133(z147=20, z148=30, flag27=536000049, flag28=536000048, z149=22, z150=32):
    """[Condition] Smoke filter change by sculpture
    z147: Isolated island_hit group ID
    z148: Lobby_Hit Group ID
    flag27: Isolated island_destruction flag
    flag28: Lobby_Destroy flag
    z149: Isolated island_internal hit group ID
    z150: Lobby_Internal hit group ID
    """
    """State 0,1: Can you see the smoke area?"""
    SetConditionGroup(0, 8)
    IsPlayerOnHitGroup(8, z147, 1)
    CompareEventFlag(8, flag27, 0)
    SetConditionGroup(0, 9)
    IsPlayerOnHitGroup(9, z149, 1)
    CompareEventFlag(9, flag27, 0)
    SetConditionGroup(1, 10)
    IsPlayerOnHitGroup(10, z148, 1)
    CompareEventFlag(10, flag28, 0)
    SetConditionGroup(1, 11)
    IsPlayerOnHitGroup(11, z150, 1)
    CompareEventFlag(11, flag28, 0)
    CompareEventFlag(12, flag27, 1)
    CompareEventFlag(12, flag28, 1)
    if ConditionGroup(0):
        """State 2: Isolated island: Smoke area is visible"""
        return 0
    elif ConditionGroup(1):
        """State 3: Lobby: Smoke area is visible"""
        return 1
    elif ConditionGroup(10):
        """State 4: Both eagle statues broke"""
        return 2

def event_m50_36_x134(val9=_, z147=_, flag27=_, z149=_):
    """[Execution] Smoke filter change by the image of the frog
    val9: Volume fog filter ID
    z147: Hit group ID
    flag27: Destruction flag
    z149: Internal hit group ID
    """
    """State 0,2: Filter status judgment"""
    if (GetVolumeFogFilterOverride() == val9) != 1:
        """State 1: Push filter"""
        PushVolumeFogFilter(val9, 0)
        assert (GetVolumeFogFilterOverride() == val9) != 0
    else:
        pass
    """State 3: Can you see the smoke area? Did you destroy the eagle statue?"""
    IsPlayerOnHitGroup(8, z147, 0)
    IsPlayerOnHitGroup(8, z149, 0)
    CompareEventFlag(1, flag27, 1)
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

def event_m50_36_x135(flag27=536000049, flag28=536000048, z147=20, z148=30, val9=14, val10=15, z149=22,
                      z150=32):
    """[Preset] Smoke filter change by haze image
    flag27: Isolated island_destruction flag
    flag28: Lobby_Destroy flag
    z147: Isolated island_hit group ID
    z148: Lobby_Hit Group ID
    val9: Solitary island_volume fog filter ID
    val10: Lobby_volume fog filter ID
    z149: Isolated island_internal hit group ID
    z150: Lobby_Internal hit group ID
    """
    """State 0,1: [Reproduction] Smoke filter change by Subaru image_SubState"""
    call = event_m50_36_x132(flag27=flag27, flag28=flag28)
    if call.Get() == 1:
        """State 3: [Condition] Smoke filter change by sculpture image_SubState"""
        call = event_m50_36_x133(z147=z147, z148=z148, flag27=flag27, flag28=flag28, z149=z149, z150=z150)
        if call.Get() == 0:
            """State 2: [Execution] Smoke filter change by sculpture image_SubState"""
            assert event_m50_36_x134(val9=val9, z147=z147, flag27=flag27, z149=z149)
            """State 6: Rerun"""
            Label('L0')
            return 1
        elif call.Get() == 1:
            """State 4: [Execution] Smoke filter change by sculpture image_2_SubState"""
            assert event_m50_36_x134(val9=val10, z147=z148, flag27=flag28, z149=z150)
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

def event_m50_36_x139(flag24=536000001, flag25=536020002, flag26=536020003):
    """[Reproduction] Continuous intrusion
    flag24: Event completion flag
    flag25: Event execution flag_1
    flag26: Event execution flag_2 or later
    """
    """State 0,1: Has the event already been completed?"""
    if GetEventFlag(flag24) != 0:
        pass
    else:
        Goto('L0')
    """State 6: Event completed"""
    return 2
    """State 3: Was it in the middle of the second and subsequent events?"""
    Label('L0')
    if GetEventFlag(flag26) != 0:
        pass
    else:
        Goto('L1')
    """State 7: During generation: 2nd and subsequent bodies"""
    return 3
    """State 2: Was it in the middle of the first event?"""
    Label('L1')
    if GetEventFlag(flag25) != 0:
        """State 5: During generation: 1st body"""
        return 1
    else:
        """State 4: Not executed"""
        return 0

def event_m50_36_x140(z140=_, z141=_, z142=_):
    """[Condition] Continuous intrusion
    z140: Start point ID
    z141: End point ID
    z142: Event execution flag
    """
    """State 0,1: Have you entered the dark spirit generation point? Has it already been done?"""
    SetConditionGroup(0, 8)
    IsHost(8, 1, 0)
    IsPlayerInsidePoint(8, z140, z141, 1)
    CompareEventFlag(0, z142, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x141(z41=536020004, z42=536020005, z43=536020006, z44=536020007, z45=536020008):
    """[Preset] Continuous intrusion
    z41: Generation flag ①
    z42: Generation flag ②
    z43: Generation flag ③
    z44: Generation flag (4)
    z45: Generation flag ⑤
    """
    """State 0,1: [Reproduction] Continuous intrusion_SubState"""
    call = event_m50_36_x139(flag24=536000001, flag25=536020002, flag26=536020003)
    if call.Get() == 2:
        pass
    elif call.Get() == 3:
        """State 7: [Execution] Continuous intrusion _2 Subsequent generation_SubState"""
        Label('L0')
        assert event_m50_36_x260(z42=z42, z43=z43, z44=z44, z45=z45, z46=536020003)
    elif call.Get() == 1:
        """State 3: [Execution] Consecutive intrusion _1 body only generated_SubState"""
        assert event_m50_36_x146(z41=z41, z134=536020002)
        """State 5: [Reproduction] Continuous intrusion_empty_SubState"""
        Label('L1')
        assert event_m50_36_x259()
        """State 4: [Condition] Continuous intrusion_2_SubState"""
        assert event_m50_36_x140(z140=1900010, z141=1900010, z142=536020003)
        Goto('L0')
    elif call.Get() == 0:
        """State 2: [Condition] Continuous intrusion_SubState"""
        assert event_m50_36_x140(z140=1900000, z141=1900001, z142=536020002)
        """State 6: [Execution] Continuous intrusion_1 body_SubState"""
        assert event_m50_36_x258(z41=z41, z47=536020002)
        Goto('L1')
    """State 8: End state"""
    return 0

def event_m50_36_x142(flag23=536000001):
    """[Reproduction] Continuous intrusion_end
    flag23: Event completion flag
    """
    """State 0,1: Has the event already been completed?"""
    if GetEventFlag(flag23) != 0:
        """State 3: Finish"""
        return 1
    else:
        """State 2: Not executed"""
        return 0

def event_m50_36_x143(z135=7000, z136=7001, z137=7002, z138=7003, z139=7004):
    """[Condition] Continuous intrusion_termination
    z135: Generator ID ①
    z136: Generator ID ②
    z137: Generator ID ③
    z138: Generator ID ④
    z139: Generator ID ⑤
    """
    """State 0,1: Did you destroy all the dark spirits?"""
    IsChrDeadOrRespawnOver(8, z135, 1)
    IsChrDeadOrRespawnOver(8, z136, 1)
    IsChrDeadOrRespawnOver(8, z137, 1)
    IsChrDeadOrRespawnOver(8, z138, 1)
    IsChrDeadOrRespawnOver(8, z139, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_36_x144(flag23=536000001):
    """[Execute] Continuous intrusion_end
    flag23: Event completion flag
    """
    """State 0,1: Network FE display"""
    OpenNetworkMessageMenu(9010, 0, 0, 0)
    OpenPresentationWindow(14)
    """State 2: Event completion flag ON"""
    SetEventFlag(flag23, 1)
    """State 3: End state"""
    return 0

def event_m50_36_x145(z135=7000, z136=7001, z137=7002, z138=7003, z139=7004, flag23=536000001):
    """[Preset] Continuous intrusion_end
    z135: Generator ID ①
    z136: Generator ID ②
    z137: Generator ID ③
    z138: Generator ID ④
    z139: Generator ID ⑤
    flag23: Event completion flag
    """
    """State 0,1: [Reproduction] Continuous intrusion_end_SubState"""
    call = event_m50_36_x142(flag23=flag23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Continuous intrusion_End_SubState"""
        assert event_m50_36_x143(z135=z135, z136=z136, z137=z137, z138=z138, z139=z139)
        """State 2: [Execution] Continuous intrusion_End_SubState"""
        assert event_m50_36_x144(flag23=flag23)
    """State 4: End state"""
    return 0

def event_m50_36_x146(z41=536020004, z134=536020002):
    """[Execution] Continuous intrusion_1
    z41: Generation flag ①
    z134: Event executed flag_1 body
    """
    """State 0,3: Execution flag ON"""
    SetEventFlag(z134, 1)
    """State 2: Generate weight 1"""
    CompareStateTime(0, 0, 3, 0)
    assert ConditionGroup(0)
    """State 1: Generation flag 1 ON"""
    SetEventFlag(z41, 1)
    """State 4: End state"""
    return 0

def event_m50_36_x147(z126=_, z127=_, z128=_, z129=_, z130=_, z131=_, z132=_, z133=_):
    """[Preset] Destroy the statue
    z126: 像 image OBJ instance ID
    z127: Destruction flag
    z128: Treasure OBJ instance ID
    z129: Initial state OBJ state ID
    z130: Activation confirmed OBJ state ID
    z131: OBJ state ID during alignment
    z132: OBJ state ID after cancellation
    z133: Navigation change point ID
    """
    """State 0,1: [Reproduction] Destroying a spider image_SubState"""
    call = event_m50_36_x148(z126=z126, z127=z127, z128=z128, z129=z129, z130=z130, z131=z131, z132=z132,
                             z133=z133)
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
    call = event_m50_36_x149(z126=z126)
    if call.Get() == 0:
        """State 3: [Execution] Destroying the image of the spider_Host_Destroyable_SubState"""
        call = event_m50_36_x150(z126=z126, z127=z127, z128=z128, z131=z131, z130=z130, z132=z132, z133=z133)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 7: End of destruction"""
            return 0
    elif call.Get() == 1:
        """State 4: [Execution] Destroying the image of the spider_Host_Unbreakable_SubState"""
        assert event_m50_36_x151(z126=z126, z132=z132)
    """State 10: Rerun"""
    return 3
    """State 5: [Condition] Destroying the image of a spider_Guest_SubState"""
    Label('L1')
    assert event_m50_36_x152(z126=z126)
    """State 2: [Execution] Destroying the image of a spider _Guest_SubState"""
    assert event_m50_36_x153(z133=z133)
    """State 9: Guest termination"""
    return 2

def event_m50_36_x148(z126=_, z127=_, z128=_, z129=_, z130=_, z131=_, z132=_, z133=_):
    """[Reproduction] Destroying a spear image
    z126: 像 image OBJ instance ID
    z127: Destruction flag
    z128: Treasure OBJ instance ID
    z129: Initial state OBJ state ID
    z130: Activation confirmed OBJ state ID
    z131: OBJ state ID during alignment
    z132: OBJ state ID after cancellation
    z133: Navigation change point ID
    """
    """State 0,2: Host judgment"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 11: Navigation change: No traffic_2"""
    AddNavimeshAttribute(z133, 2)
    """State 12: Guest termination"""
    return 0
    """State 5: Initialization judgment"""
    Label('L0')
    if CompareObjStateId(z126, 10, 1):
        pass
    else:
        """State 6: Transition to initial state"""
        ChangeObjState(z126, z129)
        assert CompareObjStateId(z126, z129, 0)
    """State 7: Safety: staying in alignment?"""
    if CompareObjStateId(z126, z131, 1):
        pass
    else:
        """State 8: Transition to the state after cancellation"""
        ChangeObjState(z126, z132)
        assert CompareObjStateId(z126, z132, 0)
    """State 1: OBJ status judgment"""
    if CompareObjStateId(z126, 20, 0):
        """State 3: Destruction flag ON"""
        Label('L1')
        SetEventFlag(z127, 1)
        """State 10: Navigation change: Allowed to pass"""
        DeleteNavimeshAttribute(z133, 2)
        """State 14: After execution"""
        return 2
    elif CompareObjStateId(z126, z130, 0):
        Goto('L1')
    elif CompareObjStateId(z126, 50, 0):
        Goto('L1')
    elif CompareObjStateId(z126, 51, 0):
        Goto('L1')
    elif CompareObjStateId(z126, 60, 0):
        Goto('L1')
    else:
        """State 4: Hide treasure"""
        ChangeDrawHit(z128, 0)
        """State 9: Navigation change: No traffic"""
        AddNavimeshAttribute(z133, 2)
        """State 13: Before execution"""
        return 1

def event_m50_36_x149(z126=_):
    """[Conditions] Destroying a spider image_Host
    z126: 像 image OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z126)
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

def event_m50_36_x150(z126=_, z127=_, z128=_, z131=_, z130=_, z132=_, z133=_):
    """[Execution] Destroying the image of a spider
    z126: 像 image OBJ instance ID
    z127: Destruction flag
    z128: Treasure OBJ instance ID
    z131: OBJ state ID during alignment
    z130: Activation confirmed OBJ state ID
    z132: OBJ state ID after cancellation
    z133: Navigation change point ID
    """
    """State 0,1: Dialog display"""
    # action:1002:"Use %s?", goods:53200000:Smelter Wedge
    DisplayYesNoMenu(1002, 2.2, z126, 190, 2, 53200000, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 6: Waiting for alignment"""
        ChangeObjState(z126, z131)
        assert CompareObjStateId(z126, z131, 0)
        """State 3: Action request to player"""
        ObjAnimationPlayerControlRequest(z126, 38, 16)
        assert PlayerIsInEventAction(11) != 0
        """State 4: OBJ status judgment"""
        IsPlayerPlayingMotion(0, 16, 0)
        # goods:53200000:Smelter Wedge
        DoesPlayerHaveItem(0, 53200000, 0, 5, 1, 1, 0)
        CompareObjState(1, z126, z130, 0)
        CompareObjState(1, z126, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 5: Destruction item consumption"""
            # goods:53200000:Smelter Wedge
            ConsumeItem(53200000, 1)
            if CompareObjStateId(z126, 50, 0):
                pass
            elif CompareObjStateId(z126, 51, 0):
                pass
            """State 9: Treasure display"""
            ChangeDrawHit(z128, 1)
            assert CompareObjStateId(z126, 20, 0)
            """State 8: Destruction flag ON"""
            SetEventFlag(z127, 1)
            """State 10: Navigation change: Allowed to pass"""
            DeleteNavimeshAttribute(z133, 2)
            """State 11: End of destruction"""
            return 0
    else:
        pass
    """State 7: Return to the state after cancellation"""
    ChangeObjState(z126, z132)
    """State 12: Rerun"""
    return 1

def event_m50_36_x151(z126=_, z132=_):
    """[Execution] Destroying a spider image
    z126: 像 image OBJ instance ID
    z132: OBJ state ID after cancellation
    """
    """State 0,2: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:53200000:Smelter Wedge
    DisplayOkMenu(1013, 0, 0, z126, 190, 2, 53200000, 0)
    assert OkMenuDisplay() != 1
    """State 1: Waiting after cancellation"""
    CompareObjState(0, z126, z132, 0)
    assert ConditionGroup(0)
    """State 3: Unsuccessful unlocking_rerun"""
    return 0

def event_m50_36_x152(z126=_):
    """[Condition] Destroying the statue of a spider _Guest
    z126: 像 image OBJ instance ID
    """
    """State 0,1: Wait for completion"""
    CompareObjState(0, z126, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x153(z133=_):
    """[Execution] Destroy the statue of a spider _Guest
    z133: Navigation change point ID
    """
    """State 0,1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z133, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x154(z123=536020082, flag22=536000081):
    """[Reproduction] Boss behavior change with Verstad equipment
    z123: Logic flag
    flag22: Boss destruction flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 5: Has the boss been destroyed?"""
        if GetEventFlag(flag22) != 0:
            pass
        else:
            """State 2: Equipment judgment"""
            # goods:23330100:Velstadt's Helm
            if (EquippedItemCount(23330100) >= 0) != 0:
                """State 3: Logic flag ON"""
                SetEventFlag(z123, 1)
                """State 6: Equipped"""
                return 0
            else:
                """State 4: Logic flag OFF"""
                SetEventFlag(z123, 0)
                """State 8: Not equipped"""
                return 2
    else:
        pass
    """State 7: Finish"""
    return 1

def event_m50_36_x155(z125=_):
    """[Condition] Boss behavior changes with Verstud equipment
    z125: Comparison value
    """
    """State 0,1: Equipment judgment"""
    # goods:23330100:Velstadt's Helm
    IsItemEquipped(0, 23330100, z125, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x156(z123=536020082, z124=_):
    """[Execution] Boss behavior change with Verstad equipment
    z123: Logic flag
    z124: ON or OFF
    """
    """State 0,1: Logic flag switching"""
    SetEventFlag(z123, z124)
    """State 2: End state"""
    return 0

def event_m50_36_x157(z123=536020082, flag22=536000081):
    """[Preset] Boss behavior change with Verstud equipment
    z123: Logic flag
    flag22: Boss destruction flag
    """
    """State 0,1: [Reproduction] Boss behavior change with Verstad equipment_SubState"""
    call = event_m50_36_x154(z123=z123, flag22=flag22)
    if call.Get() == 1:
        """State 7: Finish"""
        return 1
    elif call.Get() == 0:
        """State 3: [Condition] Boss behavior change with Verstad equipment_SubState"""
        assert event_m50_36_x155(z125=0)
        """State 2: [Execution] Boss behavior change with Verstad equipment_SubState"""
        assert event_m50_36_x156(z123=z123, z124=0)
    elif call.Get() == 2:
        """State 4: [Conditions] Boss behavior change with Verstad equipment_2_SubState"""
        assert event_m50_36_x155(z125=1)
        """State 5: [Execution] Boss behavior change with Verstad equipment_2_SubState"""
        assert event_m50_36_x156(z123=z123, z124=1)
    """State 6: Rerun"""
    return 0

def event_m50_36_x158(z122=50361075, mode3=0, flag21=536020016, val6=2):
    """[Reproduction] Continuous iron lattice _7 version opened with lever
    z122: Lever OBJ instance ID
    mode3: weight
    flag21: Event completion flag
    val6: Large weight closes
    """
    """State 0,10: Event completion judgment"""
    if GetEventFlag(flag21) != 0:
        pass
    else:
        """State 1: Judgment of lever status"""
        if CompareObjStateId(z122, 70, 0):
            """State 9: Lever end waiting"""
            Label('L0')
            assert CompareObjStateId(z122, 20, 0)
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
            SetEventFlag(flag21, 1)
        elif CompareObjStateId(z122, 72, 0):
            Goto('L0')
        elif CompareObjStateId(z122, 20, 0):
            Goto('L0')
        else:
            """State 21: Not in operation"""
            return 0
    """State 22: Already in operation"""
    return 1

def event_m50_36_x159(z121=_):
    """[Conditions] Continuous iron grid that opens with lever
    z121: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z121, 72, 0)
    CompareObjState(0, z121, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x160(mode3=0, flag21=536020016, val6=2):
    """[Execution] Continuous iron lattice _7 versions opened with lever
    mode3: weight
    flag21: Event completion flag
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
    SetEventFlag(flag21, 1)
    """State 15: End state"""
    return 0

def event_m50_36_x161(mode2=0, flag20=536020018, val5=3.5):
    """[Execution] Continuous iron lattice _9 versions opened with lever
    mode2: weight
    flag20: Event completion flag
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
    SetEventFlag(flag20, 1)
    """State 17: End state"""
    return 0

def event_m50_36_x162(z121=50361076, mode2=0, flag20=536020018, val5=3.5):
    """[Reproduction] Opening with a lever
    z121: Lever OBJ instance ID
    mode2: weight
    flag20: Event completion flag
    val5: Large weight closes
    """
    """State 0,10: Event completion judgment"""
    if GetEventFlag(flag20) != 0:
        pass
    else:
        """State 1: Judgment of lever status"""
        if CompareObjStateId(z121, 70, 0):
            """State 9: Lever end waiting"""
            Label('L0')
            assert CompareObjStateId(z121, 20, 0)
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
            SetEventFlag(flag20, 1)
        elif CompareObjStateId(z121, 72, 0):
            Goto('L0')
        elif CompareObjStateId(z121, 20, 0):
            Goto('L0')
        else:
            """State 23: Not in operation"""
            return 0
    """State 24: Already in operation"""
    return 1

def event_m50_36_x163(z122=50361075, mode3=0, flag21=536020016, val6=2):
    """[Preset] Continuous iron lattice _7 version opened with lever
    z122: Lever OBJ instance ID
    mode3: weight
    flag21: Event completion flag
    val6: Large weight closes
    """
    """State 0,1: [Reproduction] Continuous iron lattice _7 version _SubState opened with lever"""
    call = event_m50_36_x158(z122=z122, mode3=mode3, flag21=flag21, val6=val6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Continuous iron grids opened by lever_SubState"""
        assert event_m50_36_x159(z121=z122)
        """State 2: [Execution] Continuous Lattice Opening with Lever_7 Versions_SubState"""
        assert event_m50_36_x160(mode3=mode3, flag21=flag21, val6=val6)
    """State 4: Finish"""
    return 0

def event_m50_36_x164(z121=50361076, mode2=0, flag20=536020018, val5=3.5):
    """[Preset] Continuous iron lattice _ 9 versions opened with lever
    z121: Lever OBJ instance ID
    mode2: weight
    flag20: Event completion flag
    val5: Large weight closes
    """
    """State 0,2: [Reproduction] Continuous iron lattice _9 versions_SubState opened with lever"""
    call = event_m50_36_x162(z121=z121, mode2=mode2, flag20=flag20, val5=val5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Continuous iron grids opened by lever_SubState"""
        assert event_m50_36_x159(z121=z121)
        """State 3: [Execution] Continuous iron grids open with levers_9 versions_SubState"""
        assert event_m50_36_x161(mode2=mode2, flag20=flag20, val5=val5)
    """State 4: Finish"""
    return 0

def event_m50_36_x165():
    """[Reproduction] Salamander statue spitting fire"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x166(z119=_):
    """[Condition] Salamander statue spitting fire
    z119: Iron lattice OBJ instance ID
    """
    """State 0,1: The iron lattice is open or the iron lattice is closed"""
    CompareObjState(0, z119, 30, 0)
    CompareObjState(0, z119, 80, 0)
    CompareObjState(1, z119, 20, 0)
    if ConditionGroup(1):
        """State 3: Closed"""
        return 1
    elif ConditionGroup(0):
        """State 2: Open"""
        return 0

def event_m50_36_x167(z119=_, z120=_):
    """[Execution] Salamander statue spitting fire
    z119: Iron lattice OBJ instance ID
    z120: Salamander OBJ instance ID
    """
    """State 0,1: Fireball fire"""
    ChangeObjState(z120, 70)
    """State 2: Random weight"""
    CompareStateTime(0, 1, 3, 2)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_36_x168(z119=_, z120=_):
    """[Preset] Salamander statue spitting fire
    z119: Iron lattice OBJ instance ID
    z120: Salamander OBJ instance ID
    """
    """State 0,1: [Reproduction] Salamander image _SubState spitting fire"""
    assert event_m50_36_x165()
    """State 3: [Condition] Salamander statue spit fire_SubState"""
    call = event_m50_36_x166(z119=z119)
    if call.Get() == 1:
        """State 5: Finish"""
        return 1
    elif call.Get() == 0:
        """State 2: [Execution] Salamander statue _SubState spitting fire"""
        assert event_m50_36_x167(z119=z119, z120=z120)
        """State 4: Rerun"""
        return 0

def event_m50_36_x169(flag19=_):
    """[Reproduction] Recovery sphere with a spear image
    flag19: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(flag19) != 0:
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Not destroyed"""
        return 0

def event_m50_36_x170(flag19=_):
    """[Conditions] Recovery sphere with a spear image
    flag19: Destruction flag
    """
    """State 0,1: Waiting for destruction of eagle statue"""
    CompareEventFlag(0, flag19, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x171(z118=_):
    """[Execution] Recovery sphere with spear image
    z118: Recovery ball OBJ instance ID
    """
    """State 0,1: Disappearance of recovery ball: 20"""
    ChangeObjState(z118, 20)
    """State 2: End state"""
    return 0

def event_m50_36_x172(flag19=_, z118=_):
    """[Preset] Recovery sphere with spear image
    flag19: Destruction flag
    z118: Recovery ball OBJ instance ID
    """
    """State 0,1: [Reproduction] Recovery sphere with a spear image_SubState"""
    call = event_m50_36_x169(flag19=flag19)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Recovery sphere by the image of a spider _SubState"""
        assert event_m50_36_x170(flag19=flag19)
    """State 2: [Execution] Recovery sphere with a spear image_SubState"""
    assert event_m50_36_x171(z118=z118)
    """State 4: End state"""
    return 0

def event_m50_36_x173(flag18=536000026):
    """[Reproduction] Unraveling the curse of the bride ’s soul
    flag18: Event completion flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Has Seoul already changed?"""
    if GetEventFlag(flag18) != 0:
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

def event_m50_36_x175(z116=5, z117=5):
    """[Execution] Unravel the curse of the bride ’s soul
    z116: Weight until item acquisition
    z117: Weight until info display
    """
    """State 0,2: weight"""
    CompareStateTime(8, z116, 3, z116)
    # goods:53300000:Soul of Nadalia, Bride of Ash
    DoesPlayerHaveItem(8, 53300000, 12, 3, 1, 1, 0)
    CompareStateTime(0, z116, 3, z116)
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
    CompareStateTime(0, z117, 3, z117)
    assert ConditionGroup(0)
    """State 3: Event message display"""
    # action:5710:"Nadalia is no more. True Soul of Nadalia acquired."
    DisplayEventMessage(5710, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 8: End state"""
    return 0

def event_m50_36_x176(flag18=536000026, z116=5, z117=5):
    """[Preset] Unravel the curse of the bride ’s soul
    flag18: Event completion flag
    z116: Weight until item acquisition
    z117: Weight until info display
    """
    """State 0,2: [Reproduction] _SubState to unravel the curse of the bride ’s soul"""
    call = event_m50_36_x173(flag18=flag18)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] The bride's soul curse can be solved _SubState"""
        assert event_m50_36_x174()
        """State 3: [Execution] _SubState to unravel the curse of the bride ’s soul"""
        call = event_m50_36_x175(z116=z116, z117=z117)
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

def event_m50_36_x177(z114=50363090, z115=536000032):
    """[Preset] OBJ blocking the one-way door
    z114: OBJ instance ID to be destroyed
    z115: One-way door flag
    """
    """State 0,1: [Reproduction] OBJ_Sky_SubState that blocks a one-way door"""
    assert event_m50_36_x178()
    """State 3: [Condition] OBJ_SubState that blocks a one-way door"""
    assert event_m50_36_x180(z114=z114)
    """State 2: [Execution] OBJ_SubState to block the one-way door"""
    assert event_m50_36_x179(z115=z115)
    """State 4: End state"""
    return 0

def event_m50_36_x178():
    """[Reproduction] OBJ_sky blocking one-way door"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x179(z115=536000032):
    """[Execution] OBJ blocking one-way door
    z115: One-way door flag
    """
    """State 0,1: One-way flag ON"""
    SetEventFlag(z115, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x180(z114=50363090):
    """[Conditions] OBJ blocking a one-way door
    z114: OBJ instance ID to be destroyed
    """
    """State 0,1: Is the target OBJ broken?"""
    IsObjBroken(0, z114, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x181(z20=50363080, flag6=536000020, z21=5, action1=5310, z22=50360080):
    """[Preset] Crown that appears when a boss is destroyed
    z20: Crown OBJ instance ID
    flag6: Crown acquisition flag
    z21: weight
    action1: Text ID
    z22: Event light ID
    """
    """State 0,1: [Reproduction] Crown _SubState that appears when a boss is destroyed"""
    call = event_m50_36_x182(flag6=flag6, z20=z20, z22=z22)
    if call.Get() == 0:
        """State 3: [Condition] Crown _SubState that appears when a boss is destroyed"""
        call = event_m50_36_x184(z20=z20)
        if call.Get() == 0:
            """State 2: [Execution] Crown _SubState that appears when a boss is destroyed"""
            assert event_m50_36_x183(z20=z20, flag6=flag6, z21=z21, action1=action1, z22=z22)
        elif call.Get() == 1:
            """State 4: [Execution] Crown that appears after destroying the boss_Unacquired_SubState"""
            assert event_m50_36_x289(z20=z20)
            """State 6: Rerun"""
            return 1
    elif call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    """State 5: Finish"""
    return 0

def event_m50_36_x182(flag6=536000020, z20=50363080, z22=50360080):
    """[Reproduction] Crown that appears when a boss is destroyed
    flag6: Crown acquisition flag
    z20: Crown OBJ instance ID
    z22: Event light ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you acquired the crown?"""
    if GetEventFlag(flag6) != 1:
        """State 4: Key guide enabled"""
        DisableObjKeyGuide(z20, 0)
        """State 5: Event light ON"""
        SetPointLightEnabled(z22, 1, 0)
        """State 7: Unacquired"""
        return 0
    else:
        """State 3: Hidden: 10"""
        ChangeObjState(z20, 10)
        """State 6: Event light OFF"""
        SetPointLightEnabled(z22, 0, 0)
        """State 9: Finish"""
        return 2
    """State 8: Guest user"""
    Label('L0')
    return 1

def event_m50_36_x183(z20=50363080, flag6=536000020, z21=5, action1=5310, z22=50360080):
    """[Execution] The crown that appears when the boss is defeated
    z20: Crown OBJ instance ID
    flag6: Crown acquisition flag
    z21: weight
    action1: Text ID
    z22: Event light ID
    """
    """State 0,7: Event light OFF"""
    SetPointLightEnabled(z22, 0, 0.5)
    """State 1: Hidden: 10"""
    ChangeObjState(z20, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z20, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60016000:Crown of the Old Iron King
    AwardItem(60016000, 1)
    """State 4: Turn on the crown acquisition flag"""
    SetEventFlag(flag6, 1)
    """State 5: weight"""
    CompareStateTime(0, z21, 3, z21)
    assert ConditionGroup(0)
    """State 6: Text display"""
    # action:5310:"A faint heat lingers in the ancient crown"
    DisplayEventMessage(action1, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 8: End state"""
    return 0

def event_m50_36_x184(z20=50363080):
    """[Condition] Crown that appears when the boss is defeated
    z20: Crown OBJ instance ID
    """
    """State 0,1: Judging the crown"""
    IsObjSearched(0, z20)
    assert ConditionGroup(0)
    """State 2: Can items be acquired?"""
    # goods:21630100:Crown of the Old Iron King
    if CanGetItem(21630100, 1) != 0:
        """State 3: Item acquisition"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m50_36_x185(flag17=_, z111=_):
    """[Reproduction] Activating the spider image
    flag17: Destruction flag
    z111: Damipoli OBJ instance ID for production
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
    if GetEventFlag(flag17) != 0:
        pass
    else:
        """State 2: Has the production been activated?"""
        if CompareObjStateId(z111, 10, 0):
            """State 4: Not executed"""
            return 0
        else:
            pass
    """State 5: Executed"""
    return 1

def event_m50_36_x186(flag17=_, z109=_, z110=5, z112=_, z113=_):
    """[Conditions] Activating the image of the frog
    flag17: Destruction flag
    z109: 像 image OBJ instance ID
    z110: Comparison distance
    z112: Start point ID
    z113: End point ID
    """
    """State 0,1: Did you invade the or point that approached the sculpture statue?"""
    CompareObjPlayerDistance(0, z109, z110, 5)
    IsPlayerInsidePoint(0, z112, z113, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x187(z111=_):
    """[Execution] Activating the image of the frog
    z111: Damipoli OBJ instance ID for production
    """
    """State 0,1: Production activation: 70"""
    ChangeObjState(z111, 70)
    """State 2: End state"""
    return 0

def event_m50_36_x188(flag17=_, z109=_, z110=5, z111=_, z112=_, z113=_):
    """[Preset] Activating the frog image
    flag17: Destruction flag
    z109: 像 image OBJ instance ID
    z110: Comparison distance
    z111: Damipoli OBJ instance ID for production
    z112: Start point ID
    z113: End point ID
    """
    """State 0,1: [Reproduction] Activating the frog image_SubState"""
    call = event_m50_36_x185(flag17=flag17, z111=z111)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Activating the image of the frog_SubState"""
        assert event_m50_36_x186(flag17=flag17, z109=z109, z110=z110, z112=z112, z113=z113)
        """State 2: [Execution] Activating the image of the frog_SubState"""
        assert event_m50_36_x187(z111=z111)
    """State 4: End state"""
    return 0

def event_m50_36_x189(val4=_, z102=_, z103=_, z108=_):
    """[Conditions] Wetting enhancement
    val4: OBJ instance ID for production
    z102: Destruction flag
    z103: Generator ID
    z108: 像 image OBJ instance ID
    """
    """State 0,2: Always activated"""
    if (not val4) != 0:
        pass
    else:
        """State 1: Judgment judgment or destruction judgment"""
        CompareObjState(0, val4, 20, 0)
        CompareObjState(0, val4, 70, 0)
        CompareEventFlag(1, z102, 1)
        IsChrDead(1, z103)
        CompareObjState(1, z108, 50, 0)
        CompareObjState(1, z108, 51, 0)
        if ConditionGroup(1):
            """State 3: Cancel: Do nothing"""
            return 0
        elif ConditionGroup(0):
            pass
    """State 4: Strengthen"""
    return 1

def event_m50_36_x190(z103=_, z104=_, z102=_, z105=_, z106=_, z107=_, z108=_):
    """[Execution] Wetting enhancement
    z103: Generator ID
    z104: Special effect ID during effect
    z102: Destruction flag
    z105: Special effect ID for release effect
    z106: Special effect ID for activation
    z107: Enhanced Special Effect ID
    z108: 像 image OBJ instance ID
    """
    """State 0,1: For strengthening, during effect, for triggering effect 3 special effects are given"""
    SetEnemySpEffect(z103, z104, 19, 4)
    SetEnemySpEffect(z103, z106, 19, 4)
    SetEnemySpEffect(z103, z107, 19, 4)
    """State 2: Destruction determination"""
    CompareEventFlag(0, z102, 1)
    IsChrDead(0, z103)
    CompareObjState(0, z108, 50, 0)
    CompareObjState(0, z108, 51, 0)
    assert ConditionGroup(0)
    """State 3: Cancel special effects"""
    ClearEnemySpEffect(z103, z104)
    ClearEnemySpEffect(z103, z106)
    ClearEnemySpEffect(z103, z107)
    """State 4: Special effects for release effects"""
    SetEnemySpEffect(z103, z105, 19, 4)
    """State 5: End state"""
    return 0

def event_m50_36_x191():
    """[Reproduction] Strengthening of wetness"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x192(val4=_, z102=_, z103=_, z104=_, z105=_, z106=_, z107=_, z108=_):
    """[Preset] Strengthening wetness
    val4: OBJ instance ID for production
    z102: Destruction flag
    z103: Generator ID
    z104: Special effect ID during effect
    z105: Special effect ID for release effect
    z106: Special effect ID for activation
    z107: Enhanced Special Effect ID
    z108: 像 image OBJ instance ID
    """
    """State 0,1: [Reproduction] Wetting enhancement_SubState"""
    assert event_m50_36_x191()
    """State 3: [Condition] Wetting enhancement_SubState"""
    call = event_m50_36_x189(val4=val4, z102=z102, z103=z103, z108=z108)
    if call.Get() == 1:
        """State 2: [Execution] Wetting enhancement_SubState"""
        assert event_m50_36_x190(z103=z103, z104=z104, z102=z102, z105=z105, z106=z106, z107=z107, z108=z108)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m50_36_x193(z95=50361221, z96=30, z97=32, z98=70, z99=72, z100=3200000, z101=3200020):
    """[Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawa 1F
    z95: Cow OBJ instance ID
    z96: OBJ state ID before operation
    z97: OBJ state ID after operation
    z98: OBJ state ID in operation from before operation
    z99: OBJ state ID that has been in operation since operation
    z100: Before operation_Navigation change point ID
    z101: After operation_navi change point ID
    """
    """State 0,16: Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 8: Is the fire-blown cow before initialization?"""
    if CompareObjStateId(z95, 10, 0):
        """State 9: Initialize"""
        ChangeObjState(z95, z96)
        assert CompareObjStateId(z95, z96, 0)
    else:
        pass
    """State 1: Judgment of fire-blown cow"""
    if CompareObjStateId(z95, z98, 0):
        """State 4,15: Navi Mesh Change_5"""
        AddNavimeshAttribute(z100, 2)
        AddNavimeshAttribute(3200010, 2)
        AddNavimeshAttribute(3200011, 2)
        AddNavimeshAttribute(3200012, 2)
        AddNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z101, 2)
        """State 7: Waiting for completion of operation"""
        assert CompareObjStateId(z95, z97, 0)
        """State 14: Navi Mesh Change_6"""
        DeleteNavimeshAttribute(z100, 2)
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z101, 2)
    elif CompareObjStateId(z95, z99, 0):
        """State 5,11: Navi Mesh Change_2"""
        AddNavimeshAttribute(z100, 2)
        AddNavimeshAttribute(3200010, 2)
        AddNavimeshAttribute(3200011, 2)
        AddNavimeshAttribute(3200012, 2)
        AddNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z101, 2)
        """State 6: Wait for initial state"""
        assert CompareObjStateId(z95, z96, 0)
        """State 13: Navi Mesh Change_3"""
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        DeleteNavimeshAttribute(z101, 2)
        AddNavimeshAttribute(z100, 2)
        """State 17: Fire-blown cow: initial state"""
        Label('L0')
        return 0
    elif CompareObjStateId(z95, z96, 0):
        """State 2,10: Navigation mesh change"""
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        DeleteNavimeshAttribute(z101, 2)
        AddNavimeshAttribute(z100, 2)
        Goto('L0')
    elif CompareObjStateId(z95, z97, 0):
        """State 3,12: Navi Mesh Change_4"""
        DeleteNavimeshAttribute(z100, 2)
        DeleteNavimeshAttribute(3200010, 2)
        DeleteNavimeshAttribute(3200011, 2)
        DeleteNavimeshAttribute(3200012, 2)
        DeleteNavimeshAttribute(3200013, 2)
        AddNavimeshAttribute(z101, 2)
    """State 18: Fire-blown cow: End of operation"""
    return 1

def event_m50_36_x194(z88=50361222, z89=40, z90=42, z91=80, z92=82, z93=3300020, z94=3300000):
    """[Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawa 2F
    z88: Cow OBJ instance ID
    z89: OBJ state ID before operation
    z90: OBJ state ID after operation
    z91: OBJ state ID in operation from before operation
    z92: OBJ state ID that has been in operation since operation
    z93: Before operation_Navigation change point ID
    z94: After operation_navi change point ID
    """
    """State 0,16: Loop count adjustment with dummy synchronization"""
    SetConditionGroupTrue(0)
    assert ConditionGroup(0)
    """State 8: Is the fire-blown cow before initialization?"""
    if CompareObjStateId(z88, 10, 0):
        """State 9: Initialize"""
        ChangeObjState(z88, z89)
        assert CompareObjStateId(z88, z89, 0)
    else:
        pass
    """State 1: Judgment of fire-blown cow"""
    if CompareObjStateId(z88, z91, 0):
        """State 4,15: Navi Mesh Change_5"""
        AddNavimeshAttribute(z93, 2)
        AddNavimeshAttribute(3300010, 2)
        AddNavimeshAttribute(3300011, 2)
        AddNavimeshAttribute(3300012, 2)
        AddNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z94, 2)
        """State 7: Waiting for completion of operation"""
        assert CompareObjStateId(z88, z90, 0)
        """State 14: Navi Mesh Change_6"""
        DeleteNavimeshAttribute(z93, 2)
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z94, 2)
    elif CompareObjStateId(z88, z92, 0):
        """State 5,11: Navi Mesh Change_2"""
        AddNavimeshAttribute(z93, 2)
        AddNavimeshAttribute(3300010, 2)
        AddNavimeshAttribute(3300011, 2)
        AddNavimeshAttribute(3300012, 2)
        AddNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z94, 2)
        """State 6: Wait for initial state"""
        assert CompareObjStateId(z88, z89, 0)
        """State 13: Navi Mesh Change_3"""
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        DeleteNavimeshAttribute(z94, 2)
        AddNavimeshAttribute(z93, 2)
        """State 17: Fire-blown cow: initial state"""
        Label('L0')
        return 0
    elif CompareObjStateId(z88, z89, 0):
        """State 2,10: Navigation mesh change"""
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        DeleteNavimeshAttribute(z94, 2)
        AddNavimeshAttribute(z93, 2)
        Goto('L0')
    elif CompareObjStateId(z88, z90, 0):
        """State 3,12: Navi Mesh Change_4"""
        DeleteNavimeshAttribute(z93, 2)
        DeleteNavimeshAttribute(3300010, 2)
        DeleteNavimeshAttribute(3300011, 2)
        DeleteNavimeshAttribute(3300012, 2)
        DeleteNavimeshAttribute(3300013, 2)
        AddNavimeshAttribute(z94, 2)
    """State 18: Fire-blown cow: End of operation"""
    return 1

def event_m50_36_x195(z95=50361221, z98=_, z97=_, z100=_, z101=_):
    """[Execution] sliding fire-blowing cow_Kenzawa 1F
    z95: Cow OBJ instance ID
    z98: Mobile OBJ state ID
    z97: Movement end OBJ state ID
    z100: Before operation_Navigation change point ID
    z101: After operation_navi change point ID
    """
    """State 0,3: Navigation mesh change"""
    AddNavimeshAttribute(z100, 2)
    AddNavimeshAttribute(3200010, 2)
    AddNavimeshAttribute(3200011, 2)
    AddNavimeshAttribute(3200012, 2)
    AddNavimeshAttribute(3200013, 2)
    AddNavimeshAttribute(z101, 2)
    """State 1: Slide movement of fire-blown cow"""
    ChangeObjState(z95, z98)
    """State 2: Waiting for movement to end"""
    CompareObjState(0, z95, z97, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change_2"""
    DeleteNavimeshAttribute(3200010, 2)
    DeleteNavimeshAttribute(3200011, 2)
    DeleteNavimeshAttribute(3200012, 2)
    DeleteNavimeshAttribute(3200013, 2)
    DeleteNavimeshAttribute(z100, 2)
    AddNavimeshAttribute(z101, 2)
    """State 5: End state"""
    return 0

def event_m50_36_x196(z88=50361222, z91=_, z90=_, z93=_, z94=_):
    """[Execution] Sliding fire-blowing _Kenzawa 2F
    z88: Cow OBJ instance ID
    z91: Mobile OBJ state ID
    z90: Movement end OBJ state ID
    z93: Before operation_Navigation change point ID
    z94: After operation_navi change point ID
    """
    """State 0,3: Navigation mesh change"""
    AddNavimeshAttribute(z93, 2)
    AddNavimeshAttribute(3300010, 2)
    AddNavimeshAttribute(3300011, 2)
    AddNavimeshAttribute(3300012, 2)
    AddNavimeshAttribute(3300013, 2)
    AddNavimeshAttribute(z94, 2)
    """State 1: Slide movement of fire-blown cow"""
    ChangeObjState(z88, z91)
    """State 2: Waiting for movement to end"""
    CompareObjState(0, z88, z90, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change_2"""
    DeleteNavimeshAttribute(3300010, 2)
    DeleteNavimeshAttribute(3300011, 2)
    DeleteNavimeshAttribute(3300012, 2)
    DeleteNavimeshAttribute(3300013, 2)
    DeleteNavimeshAttribute(z93, 2)
    AddNavimeshAttribute(z94, 2)
    """State 5: End state"""
    return 0

def event_m50_36_x197(z95=50361221, z96=30, z97=32, z98=70, z99=72, z100=3200000, z101=3200020):
    """[Preset] sliding fire-blowing cow_initialized version_Kenzawayama 1F
    z95: Cow OBJ instance ID
    z96: OBJ state ID before operation
    z97: OBJ state ID after operation
    z98: OBJ state ID in operation from before operation
    z99: OBJ state ID that has been in operation since operation
    z100: Before operation_Navigation change point ID
    z101: After operation_navi change point ID
    """
    """State 0,3: [Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawa 1F_SubState"""
    call = event_m50_36_x193(z95=z95, z96=z96, z97=z97, z98=z98, z99=z99, z100=z100, z101=z101)
    if call.Get() == 0:
        """State 1: [Conditions] Sliding fire-blowing cow_SubState"""
        assert event_m50_36_x81(z88=z95)
        """State 4: [Execution] Sliding fired cow _Kenzawa 1F_SubState"""
        assert event_m50_36_x195(z95=z95, z98=z98, z97=z97, z100=z100, z101=z101)
    elif call.Get() == 1:
        """State 2: [Condition] Sliding fire-blowing cow_2_SubState"""
        assert event_m50_36_x81(z88=z95)
        """State 5: [Execution] Sliding fire-blowing cow_Kenzawa 1F_2_SubState"""
        assert event_m50_36_x195(z95=z95, z98=z99, z97=z96, z100=z101, z101=z100)
    """State 6: Rerun"""
    return 0

def event_m50_36_x198(z88=50361222, z89=40, z90=42, z91=80, z92=82, z93=3300020, z94=3300000):
    """[Preset] sliding fire-blowing cows_initialization version_Kenzawa 2F
    z88: Cow OBJ instance ID
    z89: OBJ state ID before operation
    z90: OBJ state ID after operation
    z91: OBJ state ID in operation from before operation
    z92: OBJ state ID that has been in operation since operation
    z93: Before operation_Navigation change point ID
    z94: After operation_navi change point ID
    """
    """State 0,3: [Reproduction] Sliding fire-blowing cow_Initialized version_Kenzawayama 2F_SubState"""
    call = event_m50_36_x194(z88=z88, z89=z89, z90=z90, z91=z91, z92=z92, z93=z93, z94=z94)
    if call.Get() == 0:
        """State 1: [Conditions] Sliding fire-blowing cow_SubState"""
        assert event_m50_36_x81(z88=z88)
        """State 4: [Execution] Sliding fire-blowing cow_Kenzawa 2F_SubState"""
        assert event_m50_36_x196(z88=z88, z91=z91, z90=z90, z93=z93, z94=z94)
    elif call.Get() == 1:
        """State 2: [Condition] Sliding fire-blowing cow_2_SubState"""
        assert event_m50_36_x81(z88=z88)
        """State 5: [Execution] Sliding fired cow _Kenzawa 2F_2_SubState"""
        assert event_m50_36_x196(z88=z88, z91=z92, z90=z89, z93=z94, z94=z93)
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

def event_m50_36_x201(z87=536020017):
    """[Execution] 7 continuous iron grid version changes
    z87: Enemy activation flag
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
    SetEventFlag(z87, 1)
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

def event_m50_36_x203(z86=536020019):
    """[Execution] Nine continuous iron grid version change
    z86: Enemy activation flag
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
    SetEventFlag(z86, 1)
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

def event_m50_36_x204(z87=536020017):
    """[Preset] 7 continuous iron grid version changes
    z87: Enemy activation flag
    """
    """State 0,1: [Reproduction] 7 continuous iron lattice versions_Navigation change_SubState"""
    assert event_m50_36_x200()
    """State 3: [Condition] Continuous iron grid_Navigation change_Empty_SubState"""
    assert event_m50_36_x199()
    """State 2: [Execution] 7 continuous iron grid versions_Navigation change_SubState"""
    assert event_m50_36_x201(z87=z87)
    """State 4: End state"""
    return 0

def event_m50_36_x205(z86=536020019):
    """[Preset] Nine continuous iron grid versions
    z86: Enemy activation flag
    """
    """State 0,1: [Reproduction] Nine continuous iron lattice versions_Navigation change_SubState"""
    assert event_m50_36_x202()
    """State 3: [Condition] Continuous iron grid_Navigation change_Empty_SubState"""
    assert event_m50_36_x199()
    """State 2: [Execution] Nine continuous iron grid version_Navigation change_SubState"""
    assert event_m50_36_x203(z86=z86)
    """State 4: End state"""
    return 0

def event_m50_36_x206(flag16=536000081, z75=501, z76=5036000, z77=536020080, z78=6.3, z79=10, z80=5036001,
                      z81=536020083):
    """[Preset] knight battle of black smoke _ start
    flag16: Boss destruction flag
    z75: Sound ID
    z76: First boss battle ID
    z77: Other flags for logic
    z78: Wait time
    z79: Boss starting distance
    z80: Rematch boss battle ID
    z81: BGM and gauge display flag
    """
    """State 0,1: [Reproduction] Black Smoke Knight Battle_Start_SubState"""
    call = event_m50_36_x207(flag16=flag16)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Knight of Black Smoke_Start_SubState"""
        call = event_m50_36_x208(z84=2000000, z85=2000000)
        if call.Get() == 0:
            """State 3: [Execution] Knight of Black Smoke_Start_SubState"""
            assert event_m50_36_x209(z76=z76)
            """State 7: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
            assert event_m50_36_x210()
            """State 9: [Condition] HP display, BGM playback and boss activation_SubState"""
            assert event_m50_36_x211(z82=903, z79=z79, z77=z77, z83=2000010)
            """State 8: [Execution] HP display, BGM playback and boss activation_SubState"""
            assert event_m50_36_x212(z75=z75, z77=z77, z78=z78, z76=z76, z81=z81)
            """State 2: [Reproduction] Knight of Black Smoke_End_Sky_SubState"""
            assert event_m50_36_x213()
            """State 6: [Condition] Knight of Black Smoke_End Judgment_SubState"""
            assert event_m50_36_x214(z76=z76)
            """State 4: [Execution] Knight of Black Smoke_End_SubState"""
            assert event_m50_36_x215(z75=z75, z76=z76, z77=z77)
        elif call.Get() == 1:
            """State 11: [Execution] Knight of Black Smoke_Start_2_SubState"""
            assert event_m50_36_x209(z76=z80)
            """State 14: [Reproduction] HP display and BGM playback and boss activation_empty_2_SubState"""
            assert event_m50_36_x210()
            """State 16: [Condition] HP display, BGM playback and boss activation_2_SubState"""
            assert event_m50_36_x211(z82=903, z79=z79, z77=z77, z83=2000010)
            """State 15: [Execution] HP display, BGM playback and boss activation_2_SubState"""
            assert event_m50_36_x212(z75=z75, z77=z77, z78=z78, z76=z80, z81=z81)
            """State 10: [Reproduction] Knight of Black Smoke_End_Sky_2_SubState"""
            assert event_m50_36_x213()
            """State 13: [Condition] Knight of Black Smoke_End Judgment_2_SubState"""
            assert event_m50_36_x214(z76=z80)
            """State 12: [Execution] Knight of Black Smoke_End_2_SubState"""
            assert event_m50_36_x215(z75=z75, z76=z80, z77=z77)
    """State 17: End state"""
    return 0

def event_m50_36_x207(flag16=536000081):
    """[Reproduction] Black Smoke Knight Battle_Start
    flag16: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag16) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_36_x208(z84=2000000, z85=2000000):
    """[Conditions] Black Smoke Knight Battle_Start
    z84: Start point ID
    z85: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z84, z85, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z84, z85, 1)
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

def event_m50_36_x209(z76=_):
    """[Execution] Knight of Black Smoke _Start
    z76: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z76)
    """State 2: End state"""
    return 0

def event_m50_36_x210():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x211(z82=903, z79=10, z77=536020080, z83=2000010):
    """[Condition] HP display, BGM playback and boss activation
    z82: Boss generator ID
    z79: Boss starting distance
    z77: Logic flag
    z83: Boss launch point
    """
    """State 0,1: Approach or damage at a certain distance or point intrusion or activated"""
    CompareChrPlayerDistance(0, z82, z79, 5)
    CompareChrHpRatio(0, z82, 100, 4)
    IsPlayerInsidePoint(0, z83, z83, 1)
    CompareEventFlag(0, z77, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x212(z75=501, z77=536020080, z78=6.3, z76=_, z81=536020083):
    """[Execution] HP display, BGM playback and boss activation
    z75: Sound ID
    z77: Logic flag
    z78: Wait time until display
    z76: Boss Battle ID
    z81: BGM and gauge display flag
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z77, 1)
    """State 4: Wait until BGM playback and HP display"""
    CompareStateTime(0, z78, 2, z78)
    CompareEventFlag(0, z81, 1)
    IsEventBossKill(1, z76, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z75)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 6: Camera parameter switching"""
    ChangeCameraParameters(675000, 3, 3)
    """State 5: BGM and gauge display flag ON"""
    SetEventFlag(z81, 1)
    """State 7: End state"""
    return 0

def event_m50_36_x213():
    """[Reproduction] Black smoke knight battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x214(z76=_):
    """[Condition] Black smoke knight battle_End judgment
    z76: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z76, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x215(z75=501, z76=_, z77=536020080):
    """[Execution] Black Smoke Knight Battle
    z75: Sound ID
    z76: Boss Battle ID
    z77: Other flags for logic
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z77, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z76)
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z75)
    assert (GetStateTime() > 6.5) != 0
    """State 4: Return camera parameters"""
    ResetCameraParameters()
    """State 5: End state"""
    return 0

def event_m50_36_x216(flag15=536000024, z74=50367900):
    """[Reproduction] Obtaining a firestick
    flag15: Item acquisition confirmation flag
    z74: Firestick OBJ instance ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Did you get the item?"""
    if GetEventFlag(flag15) != 0:
        """State 4: It has been acquired"""
        return 1
    else:
        """State 3: Unacquired"""
        return 0
    """State 5: The guests"""
    Label('L0')
    return 2

def event_m50_36_x217(z74=50367900, goods1=53100000):
    """[Condition] Get a firestick
    z74: Firestick OBJ instance ID
    goods1: Item ID
    """
    """State 0,1: Have you checked out the sashimi?"""
    IsObjSearched(0, z74)
    assert ConditionGroup(0)
    """State 2: Can items be acquired?"""
    # goods:53100000:Scorching Iron Scepter
    if CanGetItem(goods1, 1) != 0:
        """State 3: Available"""
        return 0
    else:
        """State 4: Not available"""
        return 1

def event_m50_36_x218(z74=50367900, lot1=60014000, flag15=536000024):
    """[Execution] Acquire a sashimi stick_Item acquisition
    z74: Firestick OBJ instance ID
    lot1: Lottery ID for item acquisition
    flag15: Item acquisition confirmation flag
    """
    """State 0,4: Item acquisition PC action"""
    PlayerActionRequest(2)
    assert PlayerIsInEventAction(6) != 0
    """State 2: Item acquisition"""
    # lot:60014000:Scorching Iron Scepter
    AwardItem(lot1, 1)
    """State 3: Turn on the item acquisition flag"""
    SetEventFlag(flag15, 1)
    """State 1: Get a stick: 70"""
    ChangeObjState(z74, 70)
    """State 5: End state"""
    return 0

def event_m50_36_x219(z74=50367900, lot1=60014000):
    """[Execution] Acquire a sashimi stick_Item acquisition not possible
    z74: Firestick OBJ instance ID
    lot1: Lottery ID for item acquisition
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z74, 1)
    """State 2: Acquisition failure window display"""
    # lot:60014000:Scorching Iron Scepter
    DisplayItemAwardFailure(lot1, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 3: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z74, 0)
    """State 5: End state"""
    return 0

def event_m50_36_x220(z74=50367900, lot1=60014000, flag15=536000024, goods1=53100000):
    """[Preset] Get a firestick
    z74: Firestick OBJ instance ID
    lot1: Lottery ID for item acquisition
    flag15: Item acquisition confirmation flag
    goods1: Acquisition judgment item ID
    """
    """State 0,1: [Reproduction] _SubState to obtain a sashimi stick"""
    call = event_m50_36_x216(flag15=flag15, z74=z74)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] _SubState to get a sashimi stick"""
        call = event_m50_36_x217(z74=z74, goods1=goods1)
        if call.Done():
            """State 2: [Execution] Get a sashimi stick_Item acquisition_SubState"""
            assert event_m50_36_x218(z74=z74, lot1=lot1, flag15=flag15)
        elif call.Done():
            """State 3: [Execution] Obtaining a firestick_Item not available_SubState"""
            assert event_m50_36_x219(z74=z74, lot1=lot1)
            """State 6: Rerun"""
            return 1
    elif call.Get() == 2:
        pass
    """State 5: Finish"""
    return 0

def event_m50_36_x221(z73=_):
    """[Preset] Fire the corpse
    z73: Corpse OBJ instance ID
    """
    """State 0,1: [Reproduction] _SubState to ignite the corpse"""
    call = event_m50_36_x222(z73=z73)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] _SubState to ignite the corpse"""
        call = event_m50_36_x223(z73=z73)
        if call.Get() == 0:
            """State 2: [Execution] _SubState to ignite the corpse"""
            assert event_m50_36_x224(z73=z73)
        elif call.Get() == 1:
            """State 5: Rerun"""
            return 1
    """State 4: End state"""
    return 0

def event_m50_36_x222(z73=_):
    """[Reproduction] Fire the corpse
    z73: Corpse OBJ instance ID
    """
    """State 0,1: Ignition judgment of corpse"""
    if CompareObjStateId(z73, 40, 0):
        """State 3: Ignited"""
        Label('L0')
        return 1
    elif CompareObjStateId(z73, 42, 0):
        Goto('L0')
    else:
        """State 2: Unignited"""
        return 0

def event_m50_36_x223(z73=_):
    """[Condition] Light the corpse
    z73: Corpse OBJ instance ID
    """
    """State 0,1: Determining corpse status"""
    if CompareObjStateId(z73, 30, 0):
        """State 2: With key guide"""
        Label('L0')
        CompareObjState(0, z73, 70, 0)
        CompareObjState(0, z73, 40, 0)
        CompareObjState(0, z73, 42, 0)
        IsPlayerUsingTorch(8, 0)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 4: Transition to no key guide: 10"""
            ChangeObjState(z73, 10)
            CompareObjState(0, z73, 30, 1)
            assert ConditionGroup(0)
            """State 7: Rerun"""
            return 1
    else:
        """State 3: Without key guide"""
        CompareObjState(0, z73, 40, 0)
        CompareObjState(0, z73, 42, 0)
        CompareObjState(0, z73, 70, 0)
        IsPlayerUsingTorch(8, 1)
        IsHost(8, 1, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 5: Transition to key guide existence: 30"""
            ChangeObjState(z73, 30)
            Goto('L0')
    """State 6: Dead body: Lit"""
    return 0

def event_m50_36_x224(z73=_):
    """[Execution] Ignite the corpse
    z73: Corpse OBJ instance ID
    """
    """State 0,1: Lights up: 70"""
    ChangeObjState(z73, 70)
    """State 2: Waiting for lighting"""
    CompareObjState(0, z73, 40, 0)
    CompareObjState(0, z73, 42, 0)
    assert ConditionGroup(0)
    """State 3,4: End state"""
    return 0

def event_m50_36_x225(flag13=536000049, flag14=536000048):
    """[Reproduction] Smoke fog and light change by the image of a spider
    flag13: Isolated island_destruction flag
    flag14: Lobby_Destroy flag
    """
    """State 0,1: Are both eagle statues destroyed?"""
    if GetEventFlag(flag13) != 0 and GetEventFlag(flag14) != 0:
        """State 2: Destroyed"""
        return 0
    else:
        """State 3: Not destroyed"""
        return 1

def event_m50_36_x226(z71=22, z72=32, flag13=536000049, flag14=536000048):
    """[Condition] Smoke fog and light change by the image of the frog
    z71: Isolated island_internal hit group ID
    z72: Lobby_Internal hit group ID
    flag13: Isolated island_destruction flag
    flag14: Lobby_Destroy flag
    """
    """State 0,1: Can you see the smoke area?"""
    IsPlayerOnHitGroup(8, z71, 1)
    CompareEventFlag(8, flag13, 0)
    IsPlayerOnHitGroup(9, z72, 1)
    CompareEventFlag(9, flag14, 0)
    CompareEventFlag(10, flag13, 1)
    CompareEventFlag(10, flag14, 1)
    if ConditionGroup(8):
        """State 2: Isolated island: Inside the smoke area"""
        return 0
    elif ConditionGroup(9):
        """State 3: Lobby: Inside the smoke area"""
        return 1
    elif ConditionGroup(10):
        """State 4: Both eagle statues broke"""
        return 2

def event_m50_36_x227(val2=_, z71=_, flag13=_):
    """[Execution] Smoke fog and light change by the image of the frog
    val2: Fog filter ID
    z71: Internal hit group ID
    flag13: Destruction flag
    """
    """State 0,2: Filter status judgment"""
    if (GetFogFilterOverride() == val2) != 1:
        """State 1: Push filter"""
        PushFogFilter(val2, 0.5)
        assert (GetFogFilterOverride() == val2) != 0
    else:
        pass
    """State 3: Can you see the smoke area? Did you destroy the eagle statue?"""
    IsPlayerOnHitGroup(0, z71, 0)
    CompareEventFlag(1, flag13, 1)
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

def event_m50_36_x228(flag13=536000049, flag14=536000048, z71=22, z72=32, val2=14, val3=15):
    """[Preset] Smoke fog and light change by the image of a spider
    flag13: Isolated island_destruction flag
    flag14: Lobby_Destroy flag
    z71: Isolated island_internal hit group ID
    z72: Lobby_Internal hit group ID
    val2: Isolated island_Fog filter ID
    val3: Lobby_Fog Filter ID
    """
    """State 0,1: [Reproduction] Smoke fog and light change due to the image of a spider _SubState"""
    call = event_m50_36_x225(flag13=flag13, flag14=flag14)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 3: [Condition] Smoke fog and light change by the image of a spider _SubState"""
    call = event_m50_36_x226(z71=z71, z72=z72, flag13=flag13, flag14=flag14)
    if call.Get() == 0:
        """State 2: [Execution] Smoke fog and light change by the image of a spider _SubState"""
        assert event_m50_36_x227(val2=val2, z71=z71, flag13=flag13)
    elif call.Get() == 1:
        """State 4: [Execution] Smoke fog and light change by sculpture image_2_SubState"""
        assert event_m50_36_x227(val2=val3, z71=z72, flag13=flag14)
    """State 6: Rerun"""
    return 1
    """State 5: Finish"""
    Label('L0')
    return 0

def event_m50_36_x229(z67=50363040, z68=50361500, z69=50361510, z70=50363100):
    """[Reproduction] Facility operation direction
    z67: Active OBJ instance ID
    z68: Cow OBJ instance ID
    z69: Steam OBJ instance ID
    z70: Armor OBJ instance ID
    """
    """State 0,9: Has the event been executed?"""
    if GetEventFlag(536000010) != 0:
        """State 20: Changed central pillar steam to permanent: 20"""
        ChangeObjState(z69, 20)
        """State 3: Event light switching 2"""
        SetPointLightEnabled(50360000, 1, 0)
        SetPointLightEnabled(50360020, 1, 0)
        SetPointLightEnabled(50360100, 0, 0)
    else:
        """State 1: Is there a stab stick?"""
        if CompareObjStateId(z67, 20, 0):
            """State 10: Cattle initial state judgment"""
            if CompareObjStateId(z68, 10, 0):
                """State 4: The cow starts to fire: 70"""
                ChangeObjState(z68, 70)
                """State 12: weight"""
                Label('L0')
                assert (GetStateTime() > 3) != 0
                """State 5: Light on steam on central pillar: 70"""
                Label('L1')
                ChangeObjState(z69, 70)
                SetPointLightEnabled(50360000, 1, 0.5)
                SetPointLightEnabled(50360020, 1, 0.5)
                """State 15: Weight 2"""
                Label('L2')
                assert (GetStateTime() > 2) != 0
                """State 7: Cattle stop: 20"""
                ChangeObjState(z68, 20)
                """State 8: Armor OBJ launch: 70"""
                Label('L3')
                ChangeObjState(z70, 70)
                CompareStateTime(0, 10, 3, 10)
                """State 17: Weight 3"""
                Label('L4')
                assert (GetStateTime() > 10) != 0
            else:
                """State 13: Cattle action state judgment"""
                if CompareObjStateId(z68, 70, 0):
                    Goto('L0')
                else:
                    """State 11: Central column initial state judgment"""
                    if CompareObjStateId(z69, 10, 0):
                        Goto('L1')
                    else:
                        """State 19: Light reproduction"""
                        SetPointLightEnabled(50360000, 1, 0.5)
                        SetPointLightEnabled(50360020, 1, 0.5)
                        SetPointLightEnabled(50360100, 0, 1)
                        """State 14: Cattle end determination"""
                        if CompareObjStateId(z68, 20, 1):
                            Goto('L2')
                        else:
                            """State 16: Armor initial state judgment"""
                            if CompareObjStateId(z70, 10, 0):
                                Goto('L3')
                            else:
                                """State 18: Armor action state judgment"""
                                if CompareObjStateId(z70, 70, 0):
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

def event_m50_36_x230(z67=50363040):
    """[Condition] Facility operation direction
    z67: Active OBJ instance ID
    """
    """State 0,1: Fire stab stick insertion judgment"""
    CompareObjState(0, z67, 20, 0)
    assert ConditionGroup(0)
    """State 2: Elevator operation"""
    return 0

def event_m50_36_x231(z67=50363040, z68=50361500, z69=50361510, z70=50363100):
    """[Execution] Facility operation direction
    z67: Active OBJ instance ID
    z68: Cattle ①_OBJ instance ID
    z69: Steam OBJ instance ID
    z70: Armor OBJ instance ID
    """
    """State 0,1: Cow 1 starts to fire: 70"""
    ChangeObjState(z68, 70)
    CompareStateTime(0, 3, 3, 3)
    assert ConditionGroup(0)
    """State 2: Light switching Steam on central pillar: 70"""
    ChangeObjState(z69, 70)
    CompareStateTime(0, 2, 3, 2)
    SetPointLightEnabled(50360000, 1, 0.5)
    SetPointLightEnabled(50360020, 1, 0.5)
    SetPointLightEnabled(50360100, 0, 1)
    assert ConditionGroup(0)
    """State 4: Cattle stop: 20"""
    ChangeObjState(z68, 20)
    """State 5: Armor OBJ launch: 70"""
    ChangeObjState(z70, 70)
    CompareStateTime(0, 10, 3, 10)
    assert ConditionGroup(0)
    """State 3: All elevator operating flag ON"""
    SetEventFlag(536000010, 1)
    """State 6: End state"""
    return 0

def event_m50_36_x232(z67=50363040, z68=50361500, z69=50361510, z70=50363100):
    """[Preset] Facility operation direction
    z67: Active OBJ instance ID
    z68: Cattle ①_OBJ instance ID
    z69: Steam OBJ instance ID
    z70: Armor OBJ instance ID
    """
    """State 0,1: [Reproduction] Facility operation production_SubState"""
    call = event_m50_36_x229(z67=z67, z68=z68, z69=z69, z70=z70)
    if call.Get() == 0:
        """State 3: [Condition] Facility operation direction_SubState"""
        assert event_m50_36_x230(z67=z67)
        """State 2: [Execution] Facility Operation Direction_SubState"""
        assert event_m50_36_x231(z67=z67, z68=z68, z69=z69, z70=z70)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x233(flag5=_):
    """[Reproduction] Storm of darkness by the image of a spear
    flag5: Destruction flag
    """
    """State 0,1: Is the samurai statue broken?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Not destroyed"""
        return 0

def event_m50_36_x234(flag12=536000051, z64=50361111, z65=91, z66=31, z63=50361611):
    """[Condition] Storm of darkness caused by a statue of a spear
    flag12: Destruction flag
    z64: 像 image OBJ instance ID
    z65: Samurai Statue_Activation Confirmed OBJ State ID
    z66: Saddle Statue_OBJ State ID after cancellation
    z63: Dark Storm OBJ Instance ID
    """
    """State 0,1: Waiting for the spear statue to appear or waiting for destruction"""
    CompareObjState(0, z64, z66, 0)
    CompareEventFlag(1, flag12, 1)
    CompareObjState(1, z64, z65, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 2: Dark Storm Activated: 30"""
        ChangeObjState(z63, 30)
        """State 3: Waiting for destruction of eagle statue"""
        CompareEventFlag(0, flag12, 1)
        CompareObjState(0, z64, z65, 0)
        assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_36_x235(z13=_):
    """[Execution] Storm of darkness caused by a spear image
    z13: Dark Storm OBJ Instance ID
    """
    """State 0,1: End of Dark Storm: 20"""
    ChangeObjState(z13, 20)
    """State 2: End state"""
    return 0

def event_m50_36_x236(flag12=536000051, z63=50361611, z64=50361111, z65=91, z66=31):
    """[Preset] Storm of darkness by the image of a spear
    flag12: Destruction flag
    z63: Dark Storm OBJ Instance ID
    z64: 像 image OBJ instance ID
    z65: Samurai Statue_Activation Confirmed OBJ State ID
    z66: Saddle Statue_OBJ State ID after cancellation
    """
    """State 0,1: [Reproduction] Dark storm _SubState by a spear image"""
    call = event_m50_36_x233(flag5=flag12)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Dark storm _SubState"""
        assert event_m50_36_x234(flag12=flag12, z64=z64, z65=z65, z66=z66, z63=z63)
    """State 2: [Execution] Storm of Darkness by Subaru Statue_SubState"""
    assert event_m50_36_x235(z13=z63)
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

def event_m50_36_x239(z62=1):
    """[Execution] Destruction variable reset of eagle statue
    z62: The number of destruction
    """
    """State 0,1: Initializing area variables"""
    SetAreaVariable(z62, 0)
    """State 2: End state"""
    return 0

def event_m50_36_x240(z62=1):
    """[Preset] Destruction variable reset
    z62: The number of destruction
    """
    """State 0,1: [Reproduction] Destruction variable reset of the spider image_SubState"""
    call = event_m50_36_x237()
    if call.Get() == 0:
        """State 3: [Condition] Destruction variable reset of moth image_empty_SubState"""
        assert event_m50_36_x238()
        """State 2: [Execution] Destruction variable reset of the eagle image_SubState"""
        assert event_m50_36_x239(z62=z62)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_36_x241(z59=38000):
    """[Reproduction] Addition of destructive variables for the eagle image
    z59: Reset event ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Has the reset event ended?"""
        assert EventEnded(z59) != 0
        """State 3: host"""
        return 0
    else:
        """State 4: The guests"""
        return 1

def event_m50_36_x242(z60=_):
    """[Conditions] Addition of destruction variables for the statue
    z60: Destruction flag
    """
    """State 0,1: Waiting for destruction of eagle statue"""
    CompareEventFlag(0, z60, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x243(z61=1):
    """[Execution] Addition of destructive variables for the statue
    z61: Number of destruction
    """
    """State 0,1: Number of spear statue destruction +1"""
    AddAreaVariable(z61, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x244(z59=38000, z60=_, z61=1):
    """[Preset] Addition of destruction variable of eagle image
    z59: Reset event ID
    z60: Destruction flag
    z61: Number of destruction
    """
    """State 0,1: [Reproduction] Destructive variable addition of eagle image_SubState"""
    call = event_m50_36_x241(z59=z59)
    if call.Get() == 0:
        """State 3: [Condition] Destructive variable addition of sculpture image_SubState"""
        assert event_m50_36_x242(z60=z60)
        """State 2: [Execution] Addition of destructive variables for the image of the spider"""
        assert event_m50_36_x243(z61=z61)
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

def event_m50_36_x246(z53=1, z54=_):
    """[Conditions] Judgment of number of destruction
    z53: Number of destruction
    z54: Comparison number of destruction
    """
    """State 0,1: Destruction count"""
    CompareEventFlagValue(0, 1, z53, z54, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x247(z55=536000039):
    """[Execution] Judgment of the number of spear images
    z55: 1 remaining flag
    """
    """State 0,1: 1 remaining flag ON"""
    SetEventFlag(z55, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x248(z53=1, z54=10, z55=536000039, z56=11, z57=536000059, z58=100710):
    """[Preset] Judgment of the number of spears
    z53: Number of destruction
    z54: Comparison number of destruction
    z55: 1 remaining flag
    z56: Total destruction comparison number
    z57: All destruction flag
    z58: All destruction global flag
    """
    """State 0,1: [Reproduction] Judgment of the number of spears"""
    call = event_m50_36_x245()
    if call.Get() == 0:
        """State 3: [Condition] Judgment of the number of spears"""
        assert event_m50_36_x246(z53=z53, z54=z54)
        """State 2: [Execution] Judgment of the number of spears"""
        assert event_m50_36_x247(z55=z55)
        """State 5: [Reproduction] Judgment of the number of spears_empty_SubState"""
        assert event_m50_36_x249()
        """State 4: [Condition] Judgment of the number of spears"""
        assert event_m50_36_x246(z53=z53, z54=z56)
        """State 6: [Execution] Judgment of the number of spears"""
        assert event_m50_36_x250(z57=z57, z58=z58)
    elif call.Get() == 1:
        pass
    """State 7: End state"""
    return 0

def event_m50_36_x249():
    """[Reproduction] Judgment image destruction number determination_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x250(z57=536000059, z58=100710):
    """[Execution] Judgment of the number of spears
    z57: All destruction flag
    z58: All destruction global flag
    """
    """State 0,1: All destruction flag ON"""
    SetEventFlag(z57, 1)
    SetEventFlag(z58, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x251(z50=50360410, z51=700000, z52=536000027):
    """[Execution] Large door opened by lever_Enemy activation
    z50: Door OBJ instance ID
    z51: Navigation change point ID
    z52: Enemy activation flag
    """
    """State 0,2: The big door opens: 70"""
    ChangeObjState(z50, 70)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z50, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z51, 2)
    """State 4: Enemy activation flag ON"""
    SetEventFlag(z52, 1)
    """State 5: End state"""
    return 0

def event_m50_36_x252(z50=50360410, z51=700000, z52=536000027):
    """[Reproduction] Large door opened by lever_Enemy activation
    z50: Door OBJ instance ID
    z51: Navigation change point ID
    z52: Enemy activation flag
    """
    """State 0,1: Is the big door open?"""
    if CompareObjStateId(z50, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z50, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z51, 2)
        """State 4: Enemy activation flag ON"""
        SetEventFlag(z52, 1)
        """State 6: Already in operation"""
        return 1
    else:
        """State 5: Not in operation"""
        return 0

def event_m50_36_x253(z49=50361024, z50=50360410, z51=700000, z52=536000027):
    """[Preset] Large door opened by lever_Enemy activation
    z49: Lever OBJ instance ID
    z50: Door OBJ instance ID
    z51: Navigation change point ID
    z52: Enemy activation flag
    """
    """State 0,2: [Reproduction] Large door opened by lever_Enemy activation_SubState"""
    call = event_m50_36_x252(z50=z50, z51=z51, z52=z52)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 1: [Condition] Large door opened with lever_SubState"""
        assert event_m50_36_x96(z49=z49)
        """State 3: [Execution] Large door opened by lever_Enemy activation_SubState"""
        assert event_m50_36_x251(z50=z50, z51=z51, z52=z52)
    """State 4: End state"""
    return 0

def event_m50_36_x254(flag11=_):
    """[Reproduction] Inter-DLC event_C route clear
    flag11: Achievement flag
    """
    """State 0,1: Already cleared?"""
    if GetEventFlag(flag11) != 0:
        """State 3: Cleared"""
        return 1
    else:
        """State 2: Not cleared"""
        return 0

def event_m50_36_x255(z48=_):
    """[Conditions] Inter-DLC event_C route clear
    z48: Boss destruction flag
    """
    """State 0,1: Boss destruction waiting"""
    CompareEventFlag(0, z48, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x256(flag11=_):
    """[Execution] Inter-DLC event_C route clear
    flag11: Achievement flag
    """
    """State 0,1: Clear flag ON"""
    SetEventFlag(flag11, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x257(z48=_, flag11=_):
    """[Preset] Inter-DLC event_C route clear
    z48: Boss destruction flag
    flag11: Achievement flag
    """
    """State 0,1: [Reproduction] Inter-DLC event_C route clear_SubState"""
    call = event_m50_36_x254(flag11=flag11)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Inter-DLC event_C route clear_SubState"""
        assert event_m50_36_x255(z48=z48)
        """State 2: [Execution] Inter-DLC event_C route clear_SubState"""
        assert event_m50_36_x256(flag11=flag11)
    """State 4: End state"""
    return 0

def event_m50_36_x258(z41=536020004, z47=536020002):
    """[Execution] Continuous intrusion_1 body
    z41: Generation flag ①
    z47: Event execution flag_1
    """
    """State 0,4: Execution flag ON"""
    SetEventFlag(z47, 1)
    """State 1: Network FE display"""
    OpenNetworkMessageMenu(9000, 0, 0, 0)
    """State 3: Generate weight 1"""
    CompareStateTime(0, 0, 3, 0)
    assert ConditionGroup(0)
    """State 2: Generation flag 1 ON"""
    SetEventFlag(z41, 1)
    """State 5: End state"""
    return 0

def event_m50_36_x259():
    """[Reproduction] Continuous intrusion_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x260(z42=536020005, z43=536020006, z44=536020007, z45=536020008, z46=536020003):
    """[Execution] Continuous intrusion_2
    z42: Generation flag ②
    z43: Generation flag ③
    z44: Generation flag (4)
    z45: Generation flag ⑤
    z46: Event executed flag_2
    """
    """State 0,9: Execution flag ON"""
    SetEventFlag(z46, 1)
    """State 5: Generation weight 2"""
    CompareStateTime(0, 0.5, 3, 0.5)
    assert ConditionGroup(0)
    """State 1: Generation flag 2 ON"""
    SetEventFlag(z42, 1)
    """State 6: Generate weight 3"""
    CompareStateTime(0, 1, 3, 1)
    assert ConditionGroup(0)
    """State 2: Generation flag 3 ON"""
    SetEventFlag(z43, 1)
    """State 7: Generation weight 4"""
    CompareStateTime(0, 1.5, 3, 1.5)
    assert ConditionGroup(0)
    """State 3: Generation flag 4 ON"""
    SetEventFlag(z44, 1)
    """State 8: Generate weight 5"""
    CompareStateTime(0, 0.8, 3, 0.8)
    assert ConditionGroup(0)
    """State 4: Generation flag 5 ON"""
    SetEventFlag(z45, 1)
    """State 10: End state"""
    return 0

def event_m50_36_x261(z39=50361130, z40=3700000):
    """[Reproduction] The image of a half-broken coral collapses
    z39: Half gangrene statue OBJ instance ID
    z40: Navigation change point ID
    """
    """State 0,1: Is it already broken?"""
    if CompareObjStateId(z39, 20, 0):
        """State 3: Navigation change: Allowed to pass"""
        DeleteNavimeshAttribute(z40, 2)
        """State 5: Destroyed"""
        return 1
    else:
        """State 2: Navigation change: No traffic"""
        AddNavimeshAttribute(z40, 2)
        """State 4: Undestructed"""
        return 0

def event_m50_36_x262(z38=50368800):
    """[Condition] The image of the half-broken coral collapses
    z38: Item OBJ instance ID
    """
    """State 0,1: Did you get the item?"""
    WasObjItemAcquired(0, z38, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x263(z39=50361130, z40=3700000):
    """[Execution] The image of the half-broken cocoon collapses
    z39: Half gangrene statue OBJ instance ID
    z40: Navigation change point ID
    """
    """State 0,1: The image of a spider collapses"""
    DestroyObj(z39, z39, 0)
    """State 2: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z40, 2)
    """State 3: End state"""
    return 0

def event_m50_36_x264(z38=50368800, z39=50361130, z40=3700000):
    """[Preset] The image of a half-broken spear collapses
    z38: Item OBJ instance ID
    z39: Half gangrene statue OBJ instance ID
    z40: Navigation change point ID
    """
    """State 0,1: [Reproduction] _SubState where the image of a half-broken spear collapses"""
    call = event_m50_36_x261(z39=z39, z40=z40)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] _SubState where the image of the half-broken spear collapses"""
        assert event_m50_36_x262(z38=z38)
        """State 2: [Execution] The image of the half-broken cocoon collapses"""
        assert event_m50_36_x263(z39=z39, z40=z40)
    """State 4: End state"""
    return 0

def event_m50_36_x265(flag10=536000024):
    """[Condition] The fire in the other tower disappears
    flag10: Firestick acquisition flag
    """
    """State 0,1: Did you get a firestick?"""
    CompareEventFlag(0, flag10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x266(flag10=536000024, z36=3020, z37=50360060):
    """[Execution] The fire of another tower disappears
    flag10: Firestick acquisition flag
    z36: Event SFXID
    z37: Event light ID
    """
    """State 0,1: Event SFX OFF"""
    StopSfxAtPoint(z36)
    """State 2: Event light OFF"""
    SetPointLightEnabled(z37, 0, 0.5)
    """State 3: End state"""
    return 0

def event_m50_36_x267(flag10=536000024, z36=3020, z37=50360060):
    """[Reproduction] The fire of another tower disappears
    flag10: Firestick acquisition flag
    z36: Event SFXID
    z37: Event light ID
    """
    """State 0,1: Have you got a firestick?"""
    if GetEventFlag(flag10) != 0:
        """State 3: Event SFX OFF"""
        StopSfxAtPoint(z36)
        """State 5: Event light OFF"""
        SetPointLightEnabled(z37, 0, 0)
        """State 7: Obtained"""
        return 1
    else:
        """State 2: Event SFX ON"""
        PlaySfxAtPoint(z36)
        """State 4: Event light ON"""
        SetPointLightEnabled(z37, 1, 0)
        """State 6: I have not obtained"""
        return 0

def event_m50_36_x268(flag10=536000024, z36=3020, z37=50360060):
    """[Preset] The fire of another tower disappears
    flag10: Firestick acquisition flag
    z36: Event SFXID
    z37: Event light ID
    """
    """State 0,1: [Reproduction] The fire of another tower disappears_SubState"""
    call = event_m50_36_x267(flag10=flag10, z36=z36, z37=z37)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] The fire of another tower disappears_SubState"""
        assert event_m50_36_x265(flag10=flag10)
        """State 2: [Execution] The fire of another tower disappears_SubState"""
        assert event_m50_36_x266(flag10=flag10, z36=z36, z37=z37)
    """State 4: End state"""
    return 0

def event_m50_36_x269(z35=_):
    """[Reproduction] Navi change by destroying salamander
    z35: Navigation change point ID
    """
    """State 0,1: Navimesh not allowed"""
    AddNavimeshAttribute(z35, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x270(z34=_):
    """[Condition] Change navigation by destroying salamander
    z34: Generator ID
    """
    """State 0,1: Salamander defeat judgment"""
    IsChrDeadOrRespawnOver(0, z34, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x271(z35=_):
    """[Execution] Change navigation by destroying salamander
    z35: Navigation change point ID
    """
    """State 0,1: Navigation mesh traffic is possible"""
    DeleteNavimeshAttribute(z35, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x272(z34=_, z35=_):
    """[Preset] Change navigation by destroying salamander
    z34: Generator ID
    z35: Navigation change point ID
    """
    """State 0,1: [Reproduction] Navi change by destroying Salamander_SubState"""
    assert event_m50_36_x269(z35=z35)
    """State 3: [Condition] Change navigation by destroying Salamander_SubState"""
    assert event_m50_36_x270(z34=z34)
    """State 2: [Execution] Navi change by destroying Salamander_SubState"""
    assert event_m50_36_x271(z35=z35)
    """State 4: End state"""
    return 0

def event_m50_36_x273(flag9=536000024, z31=50361530, z32=50360040):
    """[Reproduction] Furnace in another tower stops
    flag9: Sashimi get flag
    z31: Reactor OBJ instance ID
    z32: Event light ID
    """
    """State 0,1: Have you already obtained a firestick?"""
    if GetEventFlag(flag9) != 0:
        """State 4: Furnace flame extinguished: 20"""
        ChangeObjState(z31, 20)
        """State 5: Event light OFF"""
        SetPointLightEnabled(z32, 0, 0)
        """State 7: Item acquired"""
        return 1
    else:
        """State 2: Furnace flames lit: 10"""
        ChangeObjState(z31, 10)
        """State 3: Event light ON"""
        SetPointLightEnabled(z32, 1, 0)
        """State 6: Waiting for item acquisition"""
        return 0

def event_m50_36_x274(flag9=536000024):
    """[Condition] Furnace in another tower stops
    flag9: Sashimi get flag
    """
    """State 0,1: Did you get a firestick?"""
    CompareEventFlag(0, flag9, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x275(z31=50361530, z32=50360040, z33=1.5):
    """[Execution] The furnace in the other tower stops
    z31: Reactor OBJ instance ID
    z32: Event light ID
    z33: Unlit weight
    """
    """State 0,3: weight"""
    CompareStateTime(0, z33, 3, z33)
    assert ConditionGroup(0)
    """State 1: Furnace flame extinguished: 20"""
    ChangeObjState(z31, 20)
    """State 2: Event light OFF"""
    SetPointLightEnabled(z32, 0, 0.5)
    """State 4: End state"""
    return 0

def event_m50_36_x276(flag9=536000024, z31=50361530, z32=50360040, z33=1.5):
    """[Preset] Furnace in another tower stops
    flag9: Sashimi get flag
    z31: Reactor OBJ instance ID
    z32: Event light ID
    z33: Unlit weight
    """
    """State 0,1: [Reproduction] Furnace in another tower stops_SubState"""
    call = event_m50_36_x273(flag9=flag9, z31=z31, z32=z32)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Furnace in another tower stops_SubState"""
        assert event_m50_36_x274(flag9=flag9)
        """State 2: [Execution] Furnace in another tower stops_SubState"""
        assert event_m50_36_x275(z31=z31, z32=z32, z33=z33)
    """State 4: Finish"""
    return 0

def event_m50_36_x277(flag8=536000024, z29=1, z30=2):
    """[Reproduction] The light of another tower disappears
    flag8: Firestick acquisition flag
    z29: Light _part group ID
    z30: No light_Parts group ID
    """
    """State 0,1: Have you got a firestick?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Map parts switching: no light"""
        SetMapPartDisplay(z29, 0)
        SetMapPartDisplay(z30, 1)
        """State 5: Obtained"""
        return 1
    else:
        """State 2: Map parts change: There is light"""
        SetMapPartDisplay(z29, 1)
        SetMapPartDisplay(z30, 0)
        """State 4: I have not obtained"""
        return 0

def event_m50_36_x278(flag8=536000024):
    """[Conditions] The light of the other tower disappears
    flag8: Firestick acquisition flag
    """
    """State 0,1: Did you get a firestick?"""
    CompareEventFlag(0, flag8, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x279(flag8=536000024, z29=1, z30=2):
    """[Execution] The light of the other tower disappears
    flag8: Firestick acquisition flag
    z29: Light _part group ID
    z30: No light_Parts group ID
    """
    """State 0,1: Map parts switching: no light"""
    SetMapPartDisplay(z29, 0)
    SetMapPartDisplay(z30, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x280(flag8=536000024, z29=1, z30=2):
    """[Preset] The light of the other tower disappears
    flag8: Firestick acquisition flag
    z29: Light _part group ID
    z30: No light_Parts group ID
    """
    """State 0,1: [Reproduction] The light of another tower disappears _SubState"""
    call = event_m50_36_x277(flag8=flag8, z29=z29, z30=z30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] The light of another tower disappears_SubState"""
        assert event_m50_36_x278(flag8=flag8)
        """State 2: [Execution] Light of the other tower disappears_SubState"""
        assert event_m50_36_x279(flag8=flag8, z29=z29, z30=z30)
    """State 4: End state"""
    return 0

def event_m50_36_x281(z26=1404000, z27=1404010):
    """[Reproduction] Elevator navigation switching
    z26: Navigation change point_on
    z27: Navigation change point under
    """
    """State 0,1: Navi mesh switching: Not allowed"""
    AddNavimeshAttribute(z26, 2)
    AddNavimeshAttribute(z27, 2)
    """State 2: End state"""
    return 0

def event_m50_36_x282(z25=50361330):
    """[Condition] Elevator navigation switching
    z25: Elevator OBJ instance ID
    """
    """State 0,1: Elevator state judgment"""
    CompareObjState(0, z25, 40, 0)
    CompareObjState(1, z25, 10, 0)
    if ConditionGroup(0):
        """State 3: The elevator is on top"""
        return 1
    elif ConditionGroup(1):
        """State 2: The elevator is below"""
        return 0

def event_m50_36_x283(z25=50361330, z26=_, z27=_, z28=_):
    """[Execution] Elevator navigation switching
    z25: Elevator OBJ instance ID
    z26: Passable point
    z27: Impassable points
    z28: Elevator stop OBJ state ID
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z26, 2)
    AddNavimeshAttribute(z27, 2)
    """State 2: Building operation standby"""
    CompareObjState(0, z25, z28, 1)
    assert ConditionGroup(0)
    """State 3: Finish"""
    return 0

def event_m50_36_x284(z25=50361330, z26=1404000, z27=1404010):
    """[Preset elevator navigation switching
    z25: Elevator OBJ instance ID
    z26: Navigation change point_on
    z27: Navigation change point under
    """
    """State 0,1: [Reproduction] Elevator navigation switching_SubState"""
    assert event_m50_36_x281(z26=z26, z27=z27)
    """State 3: [Condition] Elevator navigation switching_SubState"""
    call = event_m50_36_x282(z25=z25)
    if call.Get() == 1:
        """State 2: [Execute] Elevator navigation switching_SubState"""
        assert event_m50_36_x283(z25=z25, z26=z26, z27=z27, z28=40)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator navigation switching_2_SubState"""
        assert event_m50_36_x283(z25=z25, z26=z27, z27=z26, z28=10)
    """State 5: Rerun"""
    return 0

def event_m50_36_x285(flag7=536000086, z23=536020087):
    """[Reproduction] Oriental knight's gut determination
    flag7: Boss destruction flag
    z23: Gag stop flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: Has the boss been destroyed?"""
        if GetEventFlag(flag7) != 0:
            pass
        else:
            """State 3: Canceled suffocation flag OFF"""
            SetEventFlag(z23, 0)
            """State 4: host"""
            return 0
    else:
        pass
    """State 5: Finish"""
    return 1

def event_m50_36_x286(flag7=536000086, z23=536020087, z24=5036010):
    """[Conditions] Toyo knight's gut determination
    flag7: Boss destruction flag
    z23: Gag stop flag
    z24: Boss Battle ID
    """
    """State 0,1: Has the boss battle started?"""
    IsEventBossBattle(0, z24, 1)
    assert ConditionGroup(0)
    """State 2: Player HP decrease judgment"""
    ComparePlayerHpDecrease(0)
    IsEventBossKill(1, z24, 0, 1)
    if ConditionGroup(1):
        """State 4: Sealed:"""
        return 1
    elif ConditionGroup(0):
        """State 3: HP reduction: Canceled hunger"""
        return 0

def event_m50_36_x287(flag7=536000086, z23=536020087, z24=5036010):
    """[Execution] Judgment of Toyo Knight
    flag7: Boss destruction flag
    z23: Gag stop flag
    z24: Boss Battle ID
    """
    """State 0,1: The hunger stop flag ON"""
    SetEventFlag(z23, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x288(flag7=536000086, z23=536020087, z24=5036010):
    """[Preset] Oriental knight's gut determination
    flag7: Boss destruction flag
    z23: Gag stop flag
    z24: Boss Battle ID
    """
    """State 0,1: [Reproduction] Oriental knight's gut determination_SubState"""
    call = event_m50_36_x285(flag7=flag7, z23=z23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Toyo knight's gut determination_SubState"""
        call = event_m50_36_x286(flag7=flag7, z23=z23, z24=z24)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Oriental knight's hunger determination_SubState"""
            assert event_m50_36_x287(flag7=flag7, z23=z23, z24=z24)
    """State 4: End state"""
    return 0

def event_m50_36_x289(z20=50363080):
    """[Execution] Crown that appears when the boss is destroyed
    z20: Crown OBJ instance ID
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z20, 1)
    """State 1: Acquisition failure window display"""
    # lot:60016000:Crown of the Old Iron King
    DisplayItemAwardFailure(60016000, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 2: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z20, 0)
    """State 5: End state"""
    return 0

def event_m50_36_x290(flag5=536000046, z14=50361106, z15=94, z16=34, z13=50361606, z17=2121, z18=2124,
                      z19=2130):
    """[Condition] Storm of Darkness by Zhao Statue _ Zakobos ②
    flag5: Destruction flag
    z14: 像 image OBJ instance ID
    z15: Samurai Statue_Activation Confirmed OBJ State ID
    z16: Saddle Statue_OBJ State ID after cancellation
    z13: Dark Storm OBJ Instance ID
    z17: Generator ID ①
    z18: Generator ID ②
    z19: Generator ID ③
    """
    """State 0,1: Waiting for the spear statue to appear or waiting for destruction"""
    CompareObjState(8, z14, z16, 0)
    IsChrDeadOrRespawnOver(8, z17, 1)
    IsChrDeadOrRespawnOver(8, z19, 1)
    IsChrDeadOrRespawnOver(8, z18, 1)
    IsChrDeadOrRespawnOver(8, 2120, 1)
    CompareEventFlag(1, flag5, 1)
    CompareObjState(1, z14, z15, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(8):
        """State 2: Dark Storm Activated: 30"""
        ChangeObjState(z13, 30)
        """State 3: Waiting for destruction of eagle statue"""
        CompareEventFlag(0, flag5, 1)
        CompareObjState(0, z14, z15, 0)
        assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_36_x291(flag5=536000046, z13=50361606, z14=50361106, z15=94, z16=34, z17=2121, z18=2124,
                      z19=2130):
    """[Preset] Storm of Darkness by Zodiac Statue _ Zakobos ②
    flag5: Destruction flag
    z13: Dark Storm OBJ Instance ID
    z14: 像 image OBJ instance ID
    z15: Samurai Statue_Activation Confirmed OBJ State ID
    z16: Saddle Statue_OBJ State ID after cancellation
    z17: Generator ID ①
    z18: Generator ID ②
    z19: Generator ID ③
    """
    """State 0,1: [Reproduction] Dark storm _SubState by a spear image"""
    call = event_m50_36_x233(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Storm of darkness by the statue of a spider _Zakobos ②_SubState"""
        assert (event_m50_36_x290(flag5=flag5, z14=z14, z15=z15, z16=z16, z13=z13, z17=z17, z18=z18,
                z19=z19))
    """State 2: [Execution] Storm of Darkness by Subaru Statue_SubState"""
    assert event_m50_36_x235(z13=z13)
    """State 4: End state"""
    return 0

def event_m50_36_x292(flag3=536020023, flag4=536000024):
    """[Reproduction] Debut activation of another tower
    flag3: Fat start flag
    flag4: Sashimi get flag
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
    if GetEventFlag(flag4) != 0:
        """State 4: Activated"""
        Label('L1')
        return 1
    elif GetEventFlag(flag3) != 0:
        Goto('L1')
    else:
        """State 3: Not started"""
        return 0

def event_m50_36_x293(z11=305000, z12=305002, flag4=536000024):
    """[Condition] Debate start of another tower
    z11: Start point ID
    z12: End point ID
    flag4: Sashimi get flag
    """
    """State 0,1: Point determination or firestick acquisition determination"""
    IsPlayerInsidePoint(0, z11, z12, 1)
    CompareEventFlag(0, flag4, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x294(flag3=536020023):
    """[Execution] Debate start of another tower
    flag3: Fat start flag
    """
    """State 0,1: Fat start flag ON"""
    SetEventFlag(flag3, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x295(flag3=536020023, flag4=536000024, z11=305000, z12=305002):
    """[Preset] Debut of another tower
    flag3: Fat start flag
    flag4: Sashimi get flag
    z11: Start point ID
    z12: End point ID
    """
    """State 0,1: [Reproduction] Debut activation of another tower_SubState"""
    call = event_m50_36_x292(flag3=flag3, flag4=flag4)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        """State 2: [Execution] Debut activation of another tower_SubState"""
        Label('L0')
        assert event_m50_36_x294(flag3=flag3)
    elif call.Get() == 0:
        """State 3: [Condition] Debut activation of another tower_SubState"""
        assert event_m50_36_x293(z11=z11, z12=z12, flag4=flag4)
        Goto('L0')
    """State 4: End state"""
    return 0

def event_m50_36_x296(flag2=_):
    """[Reproduction] NPC gesture management
    flag2: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag2) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_36_x297(z9=_):
    """[Conditions] NPC gesture management
    z9: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z9, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x298(z10=_):
    """[Execution] NPC gesture management
    z10: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z10, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x299(flag2=_, z9=_, z10=_):
    """[Preset] NPC gesture management
    flag2: Defeat flag
    z9: Boss generator ID
    z10: Gesture flag
    """
    """State 0,1: [Reproduction] NPC Gesture Management_SubState"""
    call = event_m50_36_x296(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] NPC Gesture Management_SubState"""
        assert event_m50_36_x297(z9=z9)
        """State 2: [Execution] NPC Gesture Management_SubState"""
        assert event_m50_36_x298(z10=z10)
    """State 4: End state"""
    return 0

def event_m50_36_x300(mode1=0, z4=_):
    """[Conditions] Wetting enhancement_Multiple images
    mode1: OBJ instance ID for production
    z4: Generator ID
    """
    """State 0,2: Always activated"""
    if (not mode1) != 0:
        pass
    else:
        """State 1: Judgment judgment or destruction judgment"""
        CompareObjState(0, mode1, 20, 0)
        CompareObjState(0, mode1, 70, 0)
        IsChrDead(1, z4)
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

def event_m50_36_x301(z4=_, z5=_, z6=_, z7=_, z8=_):
    """[Execution] Wetting enhancement_Multiple images
    z4: Generator ID
    z5: Special effect ID during effect
    z6: Special effect ID for release effect
    z7: Special effect ID for activation
    z8: Enhanced Special Effect ID
    """
    """State 0,1: For strengthening, during effect, for triggering effect 3 special effects are given"""
    SetEnemySpEffect(z4, z5, 19, 4)
    SetEnemySpEffect(z4, z7, 19, 4)
    SetEnemySpEffect(z4, z8, 19, 4)
    """State 2: Destruction determination"""
    IsChrDead(0, z4)
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
    ClearEnemySpEffect(z4, z5)
    ClearEnemySpEffect(z4, z7)
    ClearEnemySpEffect(z4, z8)
    """State 4: Special effects for release effects"""
    SetEnemySpEffect(z4, z6, 19, 4)
    """State 5: End state"""
    return 0

def event_m50_36_x302(mode1=0, z4=_, z5=_, z6=_, z7=_, z8=_):
    """[Preset] 煤 Wet Enhancement_Multiple Images
    mode1: OBJ instance ID for production
    z4: Generator ID
    z5: Special effect ID during effect
    z6: Special effect ID for release effect
    z7: Special effect ID for activation
    z8: Enhanced Special Effect ID
    """
    """State 0,1: [Reproduction] Wetting enhancement_SubState"""
    assert event_m50_36_x191()
    """State 3: [Condition] Wetting enhancement_Multiple images_SubState"""
    call = event_m50_36_x300(mode1=mode1, z4=z4)
    if call.Get() == 1:
        """State 2: [Execution] Wetting enhancement_Multiple images_SubState"""
        assert event_m50_36_x301(z4=z4, z5=z5, z6=z6, z7=z7, z8=z8)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m50_36_x303():
    """[Reproduction] Change the filter of another tower"""
    """State 0,1: End state"""
    return 0

def event_m50_36_x304(z2=306000, z3=306000):
    """[Condition] Change the filter of another tower
    z2: Start point ID
    z3: End point ID
    """
    """State 0,1: Did you enter a switching point?"""
    IsPlayerInsidePoint(0, z2, z3, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x305(z2=306000, z3=306000, val1=14):
    """[Execution] Change the filter of another tower
    z2: Start point ID
    z3: End point ID
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
    IsPlayerInsidePoint(0, z2, z3, 0)
    assert ConditionGroup(0)
    """State 4: Outside area: Pop filter"""
    PopVolumeFogFilter(0)
    """State 5: Waiting for pop"""
    assert (GetVolumeFogFilterOverride() == val1) != 1
    """State 6: Rerun"""
    return 0

def event_m50_36_x306(z2=306000, z3=306000, val1=14):
    """[Preset] Change the filter of another tower
    z2: Start point ID
    z3: End point ID
    val1: Volume fog filter ID
    """
    """State 0,1: [Reproduction] Change the filter of another tower_SubState"""
    assert event_m50_36_x303()
    """State 3: [Condition] Filter change of another tower_SubState"""
    assert event_m50_36_x304(z2=z2, z3=z3)
    """State 2: [Execution] Change filter of another tower_SubState"""
    assert event_m50_36_x305(z2=z2, z3=z3, val1=val1)
    """State 4: Rerun"""
    return 0

def event_m50_36_x307(flag1=_):
    """[Reproduction] Enemy jumping out of Haikuyama
    flag1: Pop out flag
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
    if GetEventFlag(flag1) != 0:
        """State 4: Popped out"""
        return 1
    else:
        """State 3: Not jumping out"""
        return 0

def event_m50_36_x308(flag1=_, z1=_):
    """[Condition] Enemy jumping out of Haizan
    flag1: Pop out flag
    z1: Pop-up point ID
    """
    """State 0,1: State invincibility: Release judgment"""
    BecomeInvincibleInCurrentState()
    IsPlayerInsidePoint(0, z1, z1, 1)
    CompareEventFlag(0, flag1, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_36_x309(flag1=_):
    """[Execution] Enemy jumping out of Haiyama
    flag1: Pop out flag
    """
    """State 0,1: Pop-out flag ON"""
    SetEventFlag(flag1, 1)
    """State 2: End state"""
    return 0

def event_m50_36_x310(flag1=_, z1=_):
    """[Preset] Enemy jumping out of Haeyama
    flag1: Pop out flag
    z1: Pop-up point ID
    """
    """State 0,1: [Reproduction] Enemy _SubState jumping out of Haeyama"""
    call = event_m50_36_x307(flag1=flag1)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Enemy _SubState jumping out of Haizan"""
        assert event_m50_36_x308(flag1=flag1, z1=z1)
        """State 2: [Execution] Enemy _SubState jumping out of Haizan"""
        assert event_m50_36_x309(flag1=flag1)
    """State 4: End state"""
    return 0

def event_m50_36_4000000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m50_36_x56(flag34=536020067, z190=14, flag35=536000068, z191=3, z192=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m50_36_x61(z195=80000000, z196=0, z197=5, z198=977, val11=1, z199=10, z200=80000001,
                z201=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m50_36_x61(z195=80000100, z196=0, z197=5, z198=977, val11=2, z199=10, z200=80000101,
                z201=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m50_36_x61(z195=80000200, z196=0, z197=5, z198=977, val11=3, z199=10, z200=80000201,
                z201=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(536020069, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_36_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m50_36_x64(flag36=536000068, z193=977, mode4=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

