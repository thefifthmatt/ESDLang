# -*- coding: utf-8 -*-
def event_m50_37_1000():
    """Falling damage disabled_player"""
    """State 0,2: [Preset] Falling damage disabled_player_SubState"""
    assert event_m50_37_x87(z231=100000, z232=100001)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_1010():
    """Fall damage disabled_NPC_1"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z228=100000, z229=100001, z230=770)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_1020():
    """Fall damage invalid_NPC_2"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z228=100000, z229=100001, z230=771)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_1030():
    """Falling damage disabled_White Knight_1"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z228=100000, z229=100001, z230=794)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_1040():
    """Falling damage disabled_White Knight_2"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z228=100000, z229=100001, z230=795)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_1050():
    """Falling damage disabled_White Knight_3"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z228=100000, z229=100001, z230=796)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_1060():
    """Falling damage disabled_White Knight_4"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z228=100000, z229=100001, z230=797)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_2100():
    """Release of ice seal"""
    """State 0,2: [Preset] Canceling the ice seal_SubState"""
    assert event_m50_37_x129(z202=537000011, z203=50371200, z204=210000)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_2200():
    """A torch disappears in a snowstorm"""
    """State 0,2: [Preset] Torches disappear in a snowstorm_SubState"""
    assert event_m50_37_x99(z219=10, z220=537000001, z221=30)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_2300():
    """Lighthouse under a snowstorm"""
    """State 0,2: [Preset] Lighthouse under the snowstorm_SubState"""
    assert event_m50_37_x133(z201=537000001)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_2400():
    """Multi-prohibition up to conversation with a shrine maiden"""
    """State 0,3: [Preset] Multi-prohibition until conversation with a shrine maiden_SubState"""
    call = event_m50_37_x257(z93=503701, z94=537000011)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_2500():
    """A shrine for a shrine maiden"""
    """State 0,2: [Preset] A maiden for a shrine _1 stage _SubState"""
    assert event_m50_37_x280(z77=537000150, z78=50371400, z79=250000, z80=250001, z81=3)
    """State 3: [Preset] A maiden to the shrine _2 stage _SubState"""
    assert event_m50_37_x280(z77=537000151, z78=50371401, z79=250010, z80=250011, z81=3)
    """State 4: [Preset] Machikazu _3 stages_SubState"""
    assert event_m50_37_x280(z77=537000152, z78=50371402, z79=250020, z80=250021, z81=3)
    """State 5: [Preset] Fallen maiden to the shrine _4 stages_SubState"""
    assert event_m50_37_x280(z77=537000153, z78=50371403, z79=250030, z80=250031, z81=3)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_2600():
    """Seoul won by the death of a shrine maiden"""
    """State 0,2: [Preset] Seoul gained by the death of a shrine maiden_SubState"""
    assert event_m50_37_x314(z52=537000019, z53=340, z54=103303)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_2700():
    """Wind speed magnification change by removing snowstorm"""
    """State 0,2: [Preset] Wind speed magnification change by canceling snowstorm_SubState"""
    assert event_m50_37_x370(z14=537000001)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_3020():
    """C root key door: Yukihara"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_37_x1(z322=1005, z323=1105, z324=52500000, z325=537000047)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_4000():
    """棺 桶 Bobsled"""
    """State 0,3: Is the initialization event complete?"""
    assert EventEnded(4020) != 0
    """State 4: [Preset] 棺 桶 Bobsleigh_SubState"""
    call = event_m50_37_x121(z207=50371010, z208=537000005)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_4010():
    """イ ベ ン ト Startup event"""
    """State 0,2: [Preset] 棺 桶 Event at startup_SubState"""
    assert event_m50_37_x125(z205=537000005, z206=50371011)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_4020():
    """棺 桶 Bobsled_Initialization"""
    """State 0,2: [Preset] 棺 桶 Bobsleigh_Initialization_SubState"""
    assert event_m50_37_x378(z9=50371010)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_5000():
    """Snowstorm management in the snowy field area"""
    """State 0,3: [Preset] Snowstorm management in the snowy field_SubState"""
    call = event_m50_37_x165(z177=537010014, z178=537020015)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6000():
    """Enemy _A that appears in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7000, z168=600100, z169=600149, z170=75, z171=11, z172=20, z173=600020,
                             z174=600029)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6010():
    """Enemy _B appearing in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z67=55, z68=600020, z69=600029, z70=537010130, z71=7001, z72=11, z73=20)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7001, z168=600150, z169=600199, z170=110, z171=11, z172=20, z173=600020,
                             z174=600029)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6040():
    """Enemy _E that appears in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7004, z168=600300, z169=600349, z170=60, z171=12, z172=20, z173=600030,
                             z174=600039)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6050():
    """Enemy _F that appears in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z67=40, z68=600030, z69=600039, z70=537010131, z71=7005, z72=12, z73=20)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7005, z168=600350, z169=600399, z170=90, z171=12, z172=20, z173=600030,
                             z174=600039)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6080():
    """Enemy _I that appears in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7008, z168=600500, z169=600549, z170=70, z171=13, z172=30, z173=600040,
                             z174=600049)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6090():
    """Enemy _J appearing in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z67=20, z68=600040, z69=600049, z70=537010133, z71=7009, z72=13, z73=30)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7009, z168=600550, z169=600599, z170=90, z171=13, z172=30, z173=600040,
                             z174=600049)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6100():
    """Enemy _K that appears in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z67=50, z68=600040, z69=600049, z70=537010132, z71=7010, z72=13, z73=30)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7010, z168=600600, z169=600649, z170=135, z171=13, z172=30, z173=600040,
                             z174=600049)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6120():
    """Enemy _M appearing in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z167=7012, z168=600700, z169=600749, z170=60, z171=10, z172=10, z173=600010,
                             z174=600019)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_6500():
    """Snowfield Enemy Defeat Count_A"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7000, z122=11, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6510():
    """Snowfield enemy defeat count _B"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7001, z122=11, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6540():
    """Snowfield enemy defeat count _E"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7004, z122=12, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6550():
    """Snowfield Enemy Defeat Count_F"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7005, z122=12, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6580():
    """Snowfield enemy defeat count _I"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7008, z122=13, val1=30)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6590():
    """Snowfield enemy defeat count _J"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7009, z122=13, val1=30)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6600():
    """Snowfield enemy defeat count _K"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7010, z122=13, val1=30)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_6620():
    """Snowfield Enemy Defeat Count_M"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z121=7012, z122=10, val1=10)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_7000():
    """Liberation of White Knight_1"""
    """State 0,2: [Preset] Liberation of White Knight_SubState"""
    assert event_m50_37_x95(z222=790, z223=537000020, z224=5.5, z225=96880100, z226=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_7010():
    """Liberation of White Knight_2"""
    """State 0,2: [Preset] Liberation of White Knight_SubState"""
    assert event_m50_37_x95(z222=791, z223=537000021, z224=5.5, z225=96880100, z226=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_7020():
    """Liberation of White Knight_3"""
    """State 0,2: [Preset] Liberation of White Knight_SubState"""
    assert event_m50_37_x95(z222=792, z223=537000022, z224=5.5, z225=96880100, z226=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_8000():
    """Gate opened with lever_Castle"""
    """State 0,2: [Preset] Gate opened with lever _SubState"""
    assert event_m50_37_x204(z134=50372450, z135=50372550, z136=800000, z137=5)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_8010():
    """Gate opened with lever_City B"""
    """State 0,2: [Preset] Gate opened with lever _SubState"""
    assert event_m50_37_x204(z134=50372650, z135=50372651, z136=801000, z137=5)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_8020():
    """Gate opened with lever_Under Tiger Bridge"""
    """State 0,2: [Preset] Gate opened with lever _SubState"""
    assert event_m50_37_x204(z134=50372660, z135=50372661, z136=802000, z137=5)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_9000():
    """The door opens when the lighthouse is on"""
    """State 0,2: [Preset] _SubState opens when the lighthouse is on"""
    assert (event_m50_37_x106(z213=50370700, z214=50370701, z215=50370702, z216=50370703, z217=50372001,
            z218=900000))
    """State 1: Finish"""
    EndMachine()

def event_m50_37_10000():
    """Elevator_city B entrance"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(10030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_37_x10(z275=50372500, z276=1000000, z277=1000010, z278=50372401, z279=50372400)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_10010():
    """Elevator_city B entrance_on the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z309=50372500, z310=50372401, z311=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_10020():
    """Elevator_city B entrance_under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z309=50372500, z310=50372400, z311=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_10030():
    """Elevator_city B entrance_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m50_37_x23(z305=50372500, z306=40, z307=537000040, z308=40)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_11000():
    """Elevator_city B exit"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_37_x10(z275=50372501, z276=1100000, z277=1100010, z278=50372403, z279=50372402)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_11010():
    """Elevator_city B exit_on lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z309=50372501, z310=50372403, z311=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_11020():
    """Elevator_city B exit_under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z309=50372501, z310=50372402, z311=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_12000():
    """Elevator_Mikome Altar"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_37_x10(z275=50372502, z276=1200000, z277=1200010, z278=50372405, z279=50372404)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_12010():
    """Elevator_Mikome Altar_Lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z309=50372502, z310=50372405, z311=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_12020():
    """Elevator_Mikome Altar_Under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z309=50372502, z310=50372404, z311=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_13000():
    """Return from the snowy field route"""
    """State 0,2: [Preset] Return from Boss Room_Yukihara_SubState"""
    assert event_m50_37_x343(z37=1300000, z38=50371190)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_14000():
    """Snowball"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371020, z292=150, z293=50371021)
    """State 3: [Preset] Snowball Gorokuro_SubState"""
    assert event_m50_37_x181(z155=50371020, z156=50371021, z157=1400000)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15020():
    """Enemy who moves by absorbing Seoul _ Tiger Wall 1F_3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371173, z292=150, z293=50371146)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3011, z164=7, z165=537020102, z166=50371146)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15030():
    """Enemy who moves by absorbing soul _ Tiger Wall 1F_4"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371172, z292=150, z293=50371145)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3010, z164=7, z165=537020103, z166=50371145)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15100():
    """Enemy who moves by absorbing Seoul _ 1st half of Tiger Wall 3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371160, z292=150, z293=50371140)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3700, z164=7, z165=537020104, z166=50371140)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15110():
    """Enemies that move by absorbing Seoul _ Tiger Wall 3F 1st Half_2"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371161, z292=150, z293=50371141)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3701, z164=7, z165=537020105, z166=50371141)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15120():
    """Enemy who moves by absorbing soul_first half of Tiger Wall 3F_3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371168, z292=150, z293=50371142)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3702, z164=7, z165=537020106, z166=50371142)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15210():
    """Enemies moving by absorbing Seoul _ Tiger Wall 3F Passage_2"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371170, z292=150, z293=50371143)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3911, z164=7, z165=537020108, z166=50371143)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15220():
    """Enemy moving by absorbing Seoul _ Tiger Wall 3F Passage _3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z291=50371171, z292=150, z293=50371144)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=3912, z164=7, z165=537020109, z166=50371144)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15300():
    """Enemy moving by absorbing Seoul _ City B Exit_1"""
    """State 0,2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=5500, z164=9.5, z165=537020110, z166=50371147)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_15310():
    """Enemy moving by absorbing Seoul _ City B Exit_2"""
    """State 0,2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z163=5501, z164=9.5, z165=537020111, z166=50371148)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_16000():
    """Rejected by ice"""
    """State 0,2: [Preset] Rejection effect by ice_SubState"""
    assert event_m50_37_x177(z158=537020016, z159=1600000, z160=50371251, z161=50371252, z162=537000006)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_17000():
    """To get the eyes of a shrine maiden"""
    """State 0,2: [Preset] _SubState to get Miko's eyes"""
    assert event_m50_37_x185(z2=537000012, z3=50376550, z4=17000, z5=17000)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_18000():
    """Zako's transparent management_A"""
    """State 0,3: [Preset] Zako's transparency management_SubState"""
    call = event_m50_37_x189(z148=537000012, z149=537010065, z150=2620, z151=5, z152=15, z153=3, z154=5)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_18010():
    """Zako's transparency_A"""
    """State 0,3: [Preset] Transparent Zako_SubState"""
    call = event_m50_37_x194(z142=537000012, z143=537010065, z144=2620, z145=98830010, z146=98830000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_18100():
    """Zako's transparent management_B"""
    """State 0,3: [Preset] Zako's transparency management_SubState"""
    call = event_m50_37_x189(z148=537000012, z149=537010066, z150=2621, z151=10, z152=20, z153=5, z154=10)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_18110():
    """Zako's transparency_B"""
    """State 0,3: [Preset] Transparent Zako_SubState"""
    call = event_m50_37_x194(z142=537000012, z143=537010066, z144=2621, z145=98830010, z146=98830000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_18200():
    """Zako's transparent management_C"""
    """State 0,3: [Preset] Zako's transparency management_SubState"""
    call = event_m50_37_x189(z148=537000012, z149=537010067, z150=2700, z151=5, z152=15, z153=3, z154=5)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_18210():
    """Zako's transparency_C"""
    """State 0,3: [Preset] Transparent Zako_SubState"""
    call = event_m50_37_x194(z142=537000012, z143=537010067, z144=2700, z145=98830010, z146=98830000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_19000():
    """One-way door"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z318=0, z319=1101, z320=1900000, z321=537000048)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_19010():
    """One-way door_Ladder room"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z318=0, z319=1101, z320=1901000, z321=537000049)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_19020():
    """One-way door_Elevator room"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z318=0, z319=1101, z320=1902000, z321=537000044)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_19030():
    """One-way door_underpass"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z318=0, z319=1101, z320=1903000, z321=537000043)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_20000():
    """Frozen treasure chest"""
    """State 0,2: [Preset] Frozen treasure chest_SubState"""
    assert event_m50_37_x229(z120=537000011)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_20500():
    """Frozen mimic"""
    """State 0,2: [Preset] Frozen Mimic_Body_SubState"""
    assert event_m50_37_x261(z90=50373001, z91=537000070, z92=2050000)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_20600():
    """Frozen Mimic_No body"""
    """State 0,2: [Preset] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x265(z87=537000071, z88=50375720, z89=50371620)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_21000():
    """NPC mimicry control_map"""
    """State 0,3: [Preset] NPC mimic control_map_SubState"""
    call = event_m50_37_x235(z115=762, z116=537020063, z117=60375000, z118=60375001)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_21010():
    """NPC mimic control_character"""
    """State 0,2: [Preset] NPC Mimicry Control_Character_SubState"""
    assert event_m50_37_x239(z112=537020063, z113=60375001, z114=762)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_22000():
    """[Insect key] For recovery hot spring"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m50_37_x24(z300=50372900)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_22010():
    """[Insect key activation] Recovery hot spring"""
    """State 0,2: [Lib] [Preset] Recovery Fountain_SubState"""
    assert event_m50_37_x34(z296=50372900, z297=30, z298=240, z299=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_23000():
    """[Insect key] Face SFX hidden door"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m50_37_x24(z300=50372800)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_23010():
    """[Insect key activation] Face SFX hidden door"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m50_37_x38(z294=50372800, val3=50370000, z295=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_23020():
    """Frozen insect key_for face SFX hidden door"""
    """State 0,2: [Preset] Frozen Bug Key_SubState"""
    assert event_m50_37_x269(z85=50372802, z86=50372800)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_23030():
    """Change the navigation mesh of the face SFX hidden door"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50372801, z287=20, z288=2303000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_24000():
    """Lever operated by lever"""
    """State 0,2: [Preset] Transporter operated by lever_SubState"""
    assert event_m50_37_x284(z74=50372600, z75=50372601, z76=2400000)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_25000():
    """Boss: Tiger Battle"""
    """State 0,2: [Preset] Tiger Battle_Start_SubState"""
    assert (event_m50_37_x161(z179=537000081, z180=504, z181=5037030, z182=537020080, z183=5, z184=537020083,
            z185=2500000))
    """State 1: Finish"""
    EndMachine()

def event_m50_37_25020():
    """Tiger cry production"""
    """State 0,2: [Preset] Tiger cry production_SubState"""
    assert event_m50_37_x253(z95=25020, z96=1, z97=2502000, z98=537000018)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_25050():
    """NPC gesture management"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_37_x217(z127=537000081, z128=907, z129=537020084)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_26000():
    """Transparent management of tigers"""
    """State 0,3: [Preset] Tiger transparency management_SubState"""
    call = event_m50_37_x146(z196=537000012, z197=537010013, z198=907, z199=537000081, z200=537020080)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_26010():
    """Tiger transparency"""
    """State 0,3: [Preset] Tiger transparency_SubState"""
    call = event_m50_37_x147(z189=537000012, z190=537010013, z191=907, z192=96790010, z193=96790000,
                             z194=96790020)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_27000():
    """Broken tiger statue_right 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371370, z287=20, z288=2700000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27010():
    """Broken tiger statue_right 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371371, z287=20, z288=2701000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27020():
    """Broken Tiger Statue_Right 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371372, z287=20, z288=2702000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27030():
    """Broken Tiger Statue_Right 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371373, z287=20, z288=2703000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27040():
    """Broken tiger statue_Right 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371374, z287=20, z288=2704000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27100():
    """A stone statue that breaks a tiger battle_left 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371385, z287=20, z288=2710000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27110():
    """Broken tiger statue_left 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371386, z287=20, z288=2711000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27120():
    """Broken tiger statue_Left 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371387, z287=20, z288=2712000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27130():
    """Broken tiger statue_Left 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371388, z287=20, z288=2713000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_27140():
    """Broken tiger statue_Left 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371389, z287=20, z288=2714000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_30000():
    """Boss: Ice King"""
    """State 0,2: [Preset] Ice King Battle_SubState"""
    assert event_m50_37_x142(z33=537000086, z34=501, z35=5037000, z36=537020085)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_30020():
    """Production sound when falling"""
    """State 0,2: [Preset] Falling sound_SubState"""
    assert event_m50_37_x249(z99=3002000, z100=30020)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_30040():
    """White knight falling with PC following"""
    """State 0,2: [Preset] Falling white knight by PC tracking_SubState"""
    assert event_m50_37_x273(z82=3004000, z83=537020024, z84=537000086)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_30050():
    """NPC Gesture Management_Ice King"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_37_x217(z127=537000086, z128=908, z129=537020087)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_30070():
    """The crown that appears when you destroy a boss"""
    """State 0,3: [Preset] Crown _SubState that appears when a boss is destroyed"""
    # action:5310:"A faint heat lingers in the ancient crown"
    call = event_m50_37_x350(z26=50371570, z27=537000002, z28=537000086, z29=5, action1=5310)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_31000():
    """Return from the boss room"""
    """State 0,2: [Preset] Return from Boss Room_SubState"""
    assert event_m50_37_x103(z130=3100010, z131=537000086, z132=50371001, z133=537000002) == 0
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_31050():
    """Return from Boss Room_White Knight_1"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z30=794, z31=5037000, z32=537020025)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_31060():
    """Return from Boss Room_White Knight_2"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z30=795, z31=5037000, z32=537020025)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_31070():
    """Return from Boss Room_White Knight_3"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z30=796, z31=5037000, z32=537020025)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_31080():
    """Return from Boss Room_White Knight_4"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z30=797, z31=5037000, z32=537020025)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_31100():
    """White knight inside ice after boss battle removed"""
    """State 0,2: [Preset] Delete the white knight inside the ice after the boss battle_SubState"""
    assert event_m50_37_x382(z8=537020175)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32000():
    """White Knight: Sealing Order and Sealing Direction"""
    """State 0,3: [Preset] Sealing instruction _SubState"""
    assert event_m50_37_x241(z109=40, z110=10, z111=1)
    """State 2: [Preset] Sealing production_SubState"""
    assert (event_m50_37_x245(z101=794, z102=795, z103=796, z104=797, z105=537020035, z106=15, z107=50371122,
            z108=50371552))
    """State 5: [Preset] Sealing instruction_2_SubState"""
    assert event_m50_37_x241(z109=90, z110=10, z111=2)
    """State 4: [Preset] Sealing production_2_SubState"""
    assert (event_m50_37_x245(z101=794, z102=795, z103=796, z104=797, z105=537020036, z106=15, z107=50371120,
            z108=50371550))
    """State 7: [Preset] Sealing instruction_3_SubState"""
    assert event_m50_37_x241(z109=150, z110=10, z111=3)
    """State 6: [Preset] Sealing production_3_SubState"""
    assert (event_m50_37_x245(z101=794, z102=795, z103=796, z104=797, z105=537020037, z106=0, z107=50371121,
            z108=50371551))
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32010():
    """Change generator navigator mesh"""
    """State 0,3: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m50_37_x59(z263=3201000, z264=2, z265=0, z266=537020035, z267=0)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32020():
    """Change generator navigator mesh"""
    """State 0,3: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m50_37_x59(z263=3202000, z264=2, z265=0, z266=537020036, z267=0)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32030():
    """Change generator navigator mesh"""
    """State 0,3: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m50_37_x59(z263=3203000, z264=2, z265=0, z266=537020037, z267=0)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32100():
    """White Knight's profession_1"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z23=794, z24=537000026, z25=537000086)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32110():
    """White Knight's profession_2"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z23=795, z24=537000027, z25=537000086)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32120():
    """White Knight's profession_3"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z23=796, z24=537000028, z25=537000086)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32130():
    """White Knight's profession_4"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z23=797, z24=537000029, z25=537000086)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32200():
    """Instant death damage inside ice _A"""
    """State 0,2: [Preset] Instant death damage inside ice _SubState"""
    assert event_m50_37_x386(z6=3220000, z7=50371122)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32210():
    """Instant death damage inside ice_B"""
    """State 0,2: [Preset] Instant death damage inside ice _SubState"""
    assert event_m50_37_x386(z6=3221000, z7=50371120)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_32220():
    """Instant death damage inside ice _C"""
    """State 0,2: [Preset] Instant death damage inside ice _SubState"""
    assert event_m50_37_x386(z6=3222000, z7=50371121)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_33030():
    """Black Knight: Defeat count _4"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4110, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33040():
    """Black Knight: Defeat count _5"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4111, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33050():
    """Black Knight: Defeat count _6"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4112, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33060():
    """Black Knight: Defeat count _7"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4113, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33070():
    """Black Knight: Defeat count _8"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4114, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33080():
    """Black Knight: Defeat count _9"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4115, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33090():
    """Black Knight: Defeat count _10"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4116, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33100():
    """Black Knight: Defeat count _11"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4117, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33110():
    """Black Knight: Defeat count _12"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4118, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33120():
    """Black Knight: Defeat Count Count_13"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4119, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33130():
    """Black Knight: Defeat count _14"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4120, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33140():
    """Black Knight: Defeat count _15"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z138=4121, z139=1, z140=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_33500():
    """Black Knight: Defeat count reset"""
    """State 0,2: [Preset] Black Knight: Defeat count reset_SubState"""
    assert event_m50_37_x203()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_34000():
    """Black Knight: Generation Generator_A"""
    """State 0,3: [Preset] Black Knight: Generator Generator_SubState"""
    call = event_m50_37_x213(z15=537020035, z16=12, z17=4110, z18=4111, z19=4112, z20=4113, z21=13, z22=14)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_34010():
    """Black Knight: Generator Generator_B"""
    """State 0,3: [Preset] Black Knight: Generator Generator_SubState"""
    call = event_m50_37_x213(z15=537020036, z16=13, z17=4114, z18=4115, z19=4116, z20=4117, z21=12, z22=14)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_34020():
    """Black Knight: Generator Generator_C"""
    """State 0,3: [Preset] Black Knight: Generator Generator_SubState"""
    call = event_m50_37_x213(z15=537020037, z16=14, z17=4118, z18=4119, z19=4120, z20=4121, z21=12, z22=13)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_34050():
    """Black Knight Generator started operation"""
    """State 0,2: [Preset] Black Knight Generator starts operation_SubState"""
    assert event_m50_37_x374(z10=3400000, z11=537020032, z12=0, z13=0)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_35000():
    """Boss: Black Tiger Battle"""
    """State 0,3: [Preset] Black Tiger Battle_SubState"""
    assert (event_m50_37_x302(z57=537000091, z58=3500000, z59=3500000, z60=503, z61=5037010, mode1=0,
            z62=537020090, z63=537020093))
    """State 1: Finish"""
    EndMachine()

def event_m50_37_35010():
    """Boss: Black Tiger Battle _ 2nd Tiger Operation"""
    """State 0,2: [Preset] Second tiger in operation _SubState"""
    assert event_m50_37_x292(z64=537000091, z65=5037010, z66=537020093)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_35050():
    """NPC Gesture Management_Black Tiger"""
    """State 0,2: [Preset] NPC Gesture Management_2 Body Version_SubState"""
    assert event_m50_37_x219(z123=537000091, z124=537020092, z125=909, z126=910)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_40000():
    """Hidden door_castle wall_navigation mesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50372851, z287=20, z288=4000000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_40010():
    """Hidden door_Cave_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50372850, z287=20, z288=4001000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41000():
    """Navimesh change of ice seal _ ice tower"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371223, z287=20, z288=4100000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41010():
    """Change the Navimesh of Ice Seal _Barista Crossroads"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371222, z287=20, z288=4101000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41020():
    """Navi mesh change of ice seal"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371224, z287=20, z288=4102000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41030():
    """Change Navimesh of ice seal_alley right"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371210, z287=20, z288=4103000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41040():
    """Change the Navimesh of the ice seal_Left alley"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371211, z287=20, z288=4104000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41050():
    """Navimesh change of ice seal_fountain plaza_1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371204, z287=20, z288=4105000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41060():
    """Navimesh change of ice seal_fountain plaza_2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371203, z287=20, z288=4106000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41070():
    """Changed the Navimesh of the ice seal_Fountain Square_3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371201, z287=20, z288=4107000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41080():
    """Change the Navimesh of Ice Seal_Fountain Square_4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371202, z287=20, z288=4108000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41090():
    """Navimesh change of ice seal _ Cathedral treasure chest"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371700, z287=20, z288=4109000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_41100():
    """Navimesh change of ice seal_golem passage"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50373110, z287=20, z288=4110000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42000():
    """Enemy moving by absorbing soul_Navigation mesh change_Treasure 1A"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371140, z287=20, z288=4200000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42010():
    """Enemy moving by absorbing soul_Navimesh change_Treasure 1B"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371141, z287=20, z288=4201000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42020():
    """Enemy moving with soul absorption_Navimesh change_Treasure 1C"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371142, z287=20, z288=4202000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42100():
    """Enemy moving with soul absorption_Navigation mesh change_Aisle 1A"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371170, z287=20, z288=4210000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42110():
    """Enemy moving with soul absorption_Navimesh change_Aisle 1B"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371171, z287=20, z288=4211000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42200():
    """Enemy moving with soul absorption_Navigation mesh change_Room 1A"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371172, z287=20, z288=4220000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_42210():
    """Enemy moving by absorbing soul_Navigation mesh change_Room 1B"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z286=50371173, z287=20, z288=4221000, z289=0, z290=2)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43020():
    """Enemy who moves by absorbing soul_character_tiger wall 1F_3"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43030():
    """Enemies moving by absorbing soul_character_tiger wall 1F_4"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43100():
    """Enemy who moves by absorbing soul _Chara_Tiger Wall 3F 1st Half_1"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43110():
    """Enemies moving by absorbing soul_Chara_Tiger Wall 3F 1st Half_2"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43120():
    """Enemy who moves by absorbing soul_character_tiger castle wall 3F first half_3"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43210():
    """Enemy who moves by absorbing soul_character_tiger castle wall 3F passage_2"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43220():
    """Enemies that move by absorbing Seoul_Chara_Tiger Wall 3F Passage_3"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43300():
    """Enemy who moves by absorbing Seoul _ Character _ City B Exit_1"""
    """State 0,3: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_43310():
    """Enemies moving by absorbing Seoul_Character_Exit B"""
    """State 0,3: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_44000():
    """Bhaksta launch"""
    """State 0,3: [Preset] Samurai Warrior Bakusta Launch_SubState"""
    call = event_m50_37_x318(z49=50372650, z50=537020003, z51=537020004)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m50_37_49000():
    """Create filter condition"""
    """State 0,2: [Preset] Filter condition registration_SubState"""
    assert event_m50_37_x341()
    """State 1: Finish"""
    EndMachine()

def event_m50_37_49010():
    """Filter condition judgment_DLC possession"""
    """State 0,2: [Preset] Filter condition judgment_DLC possession_SubState"""
    assert event_m50_37_x332(z46=537020050, z47=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_49020():
    """Filter condition judgment_First Tiger Battle"""
    """State 0,2: [Preset] Filter Condition Judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x336(z43=537020051, z44=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_49030():
    """Filter condition judgment_Rematch tiger battle"""
    """State 0,2: [Preset] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x340(z39=537020052, z40=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_51000():
    """Start from the Forest of the Shadow"""
    """State 0,1: Finish"""
    EndMachine()

def event_m50_37_52000():
    """Return to the Forest of Shadow"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m50_37_x67(z255=50371000, z256=10320000, z257=5200000)
    """State 1: Rerun"""
    RestartMachine()

def event_m50_37_53000():
    """Door that opens with DLC purchase"""
    """State 0,3: [Preset] Door that opens with DLC purchase_SubState"""
    call = event_m50_37_x108(z209=50370400, z210=5300010, z211=5300000, z212=5300001)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m50_37_59000():
    """Inter-DLC event"""
    """State 0,2: [Preset] Inter-DLC event"""
    assert event_m50_37_x306(z55=103400, z56=5320)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_80000():
    """Regenerative fire 01_Start point_37650"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z272=5037000, z273=5037099)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_82000():
    """Regeneration of fire 03_city area A_37660"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z272=5037200, z273=5037299)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_83000():
    """Reproduction of fire 04_city B in the middle_37665"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z272=5037300, z273=5037399)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_84000():
    """Rebirth of Fire 05_Cathedral_37670"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z272=5037400, z273=5037499)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_85000():
    """Rebirth of Fire 06_Snowfield_37675"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z272=5037500, z273=5037599)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_87000():
    """Rebirth Fire 08_Tora Hashishita_37685"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z272=5037700, z273=5037799)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_89000():
    """Shop lineup expansion_tiger"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_37_x69(z253=101071, z254=101221)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_89010():
    """Shop lineup expansion_Black Tiger"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_37_x69(z253=101072, z254=101222)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_89020():
    """Shop Lineup Expansion_Ice King"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_37_x69(z253=101070, z254=101223)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_x0(z326=0, z327=0, z256=_, z37=_):
    """[Lib] Warp between maps after poly play
    z326: Pre-warp poly play ID
    z327: Poly Play ID after Warp
    z256: Map ID
    z37: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z326, z327, z256, z37, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m50_37_100001():
    """White Spirit Sign Display_Ice King 02"""
    """State 0,1: White knight flag watch"""
    if GetEventFlag(537000020) != 0:
        pass
    elif GetEventFlag(537000021) != 0:
        pass
    elif GetEventFlag(537000022) != 0:
        pass
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z274=771)

def event_m50_37_x1(z322=1005, z323=1105, z324=52500000, z325=537000047):
    """[Lib] Item specified door unlocking_2
    z322: Text ID when opened
    z323: Text ID when not opened
    z324: item
    z325: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z324, z322, z323, z325, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x2(z318=0, z319=1101, z320=_, z321=_):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z318: Text ID when opened
    z319: Text ID when not opened
    z320: Point ID
    z321: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z320, 0, z318, z319, z321, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x3(z312=537000091, z313=3500000, z314=3500000, z315=503, z316=5037010, z317=537020090,
                    mode5=0):
    """[Lib] [Preset] Boss Battle Start
    z312: Boss destruction flag
    z313: Start point ID
    z314: End point ID
    z315: Sound ID
    z316: Boss Battle ID
    z317: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m50_37_x4(z312=z312)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m50_37_x5(z313=z313, z314=z314)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m50_37_x6(z315=z315, z316=z316, z317=z317)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m50_37_x7()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m50_37_x8(z316=z316)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m50_37_x9(z315=z315, z316=z316, z317=z317, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m50_37_x4(z312=537000091):
    """[Reproduction] Boss Battle_Start
    z312: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z312) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_37_x5(z313=3500000, z314=3500000):
    """[Condition] Boss Battle_Start
    z313: Start point ID
    z314: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z313, z314, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z313, z314, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x6(z315=503, z316=5037010, z317=537020090):
    """[Execution] Boss Battle_Start
    z315: Sound ID
    z316: Boss Battle ID
    z317: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z315)
    """State 1: Boss battle start notification"""
    StartBossFight(z316)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z317, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x7():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x8(z316=5037010):
    """[Condition] Boss Battle_End Judgment
    z316: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z316, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x9(z315=503, z316=5037010, z317=537020090, mode5=0):
    """[Execute] Boss Battle_End
    z315: Sound ID
    z316: Boss Battle ID
    z317: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z317, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z316)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z315)
    """State 5: End state"""
    return 0

def event_m50_37_100010():
    """White Spirit sign display_White Tiger 01"""
    """State 0,1: Miko's Eye Judgment"""
    assert GetEventFlag(537000012) != 0
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z274=772)

def event_m50_37_x10(z275=_, z276=_, z277=_, z278=_, z279=_):
    """[Lib] [Preset] Elevator
    z275: OBJ instance ID of the elevator
    z276: On elevator point ID_
    z277: Elevator point ID_below
    z278: Upper lever OBJ instance ID
    z279: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m50_37_x11()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m50_37_x12(z275=z275, z276=z276, z277=z277, z278=z278, z279=z279)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m50_37_x49(z275=z275, z277=z277)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m50_37_x48(z275=z275, z276=z276)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m50_37_x13(z275=z275, z276=z276)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m50_37_x14(z275=z275, z277=z277)
    """State 7: End state"""
    return 0

def event_m50_37_100011():
    """White spirit sign display_White Tiger 02"""
    """State 0,1: Miko's Eye Judgment"""
    assert GetEventFlag(537000012) != 0
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z274=773)

def event_m50_37_x11():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x12(z275=_, z276=_, z277=_, z278=_, z279=_):
    """[Condition] Elevator
    z275: Elevator OBJ instance ID
    z276: On elevator point ID_
    z277: Elevator point ID_below
    z278: Upper lever OBJ instance ID
    z279: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z275, 10, 0)
    CompareObjState(1, z275, 40, 0)
    CompareObjState(2, z275, 80, 0)
    CompareObjState(2, z275, 41, 0)
    CompareObjState(3, z275, 70, 0)
    CompareObjState(3, z275, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z277, z277, 1)
        CompareObjState(0, z278, 74, 0)
        CompareObjState(0, z278, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z276, z276, 1)
        CompareObjState(0, z279, 74, 0)
        CompareObjState(0, z279, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m50_37_x13(z275=_, z276=_):
    """[Execution] Elevator_Rise
    z275: Elevator OBJ instance ID
    z276: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z275, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z275, 30, 0)
    IsPlayerInsidePoint(8, z276, z276, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z275, 71)
    assert CompareObjStateId(z275, 40, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x14(z275=_, z277=_):
    """[Execution] Elevator_Descent
    z275: Elevator OBJ instance ID
    z277: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z275, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z275, 41, 0)
    IsPlayerInsidePoint(8, z277, z277, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z275, 81)
    assert CompareObjStateId(z275, 10, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x15(z309=_, z310=_, z311=_):
    """[Lib] [Preset] Elevator lever
    z309: OBJ instance ID of the elevator
    z310: Lever OBJ instance ID
    z311: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m50_37_x16()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m50_37_x17(z309=z309, z310=z310, z311=z311)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m50_37_x18(z309=z309, z310=z310, z311=z311)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m50_37_x19(z309=z309, z310=z310, z311=z311)
    """State 5: Rerun"""
    return 0

def event_m50_37_x16():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x17(z309=_, z310=_, z311=_):
    """[Condition] Elevator lever_use judgment
    z309: OBJ instance ID of the elevator
    z310: Lever OBJ instance ID
    z311: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z309, z311, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m50_37_x18(z309=_, z310=_, z311=_):
    """[Execution] Elevator lever_Key guide valid
    z309: OBJ instance ID of the elevator
    z310: Lever OBJ instance ID
    z311: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z310, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z309, z311, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x19(z309=_, z310=_, z311=_):
    """[Execute] Elevator lever_key guide disabled
    z309: OBJ instance ID of the elevator
    z310: Lever OBJ instance ID
    z311: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z310, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z309, z311, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x20(z307=537000040):
    """[Lib] [Reproduction] Elevator_Initialization
    z307: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(z307) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m50_37_100021():
    """White spirit sign display_Yukihara 01"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z274=775)

def event_m50_37_x21():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_37_x22(z305=50372500, z306=40, z307=537000040, z308=40):
    """[Lib] [Execution] Elevator_Initialization
    z305: Elevator OBJ instance ID
    z306: Initial position OBJ state ID
    z307: Initialization completion flag
    z308: [Preset] 棺 桶 Bobsleigh_Initialization_SubState
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z305, z306)
    assert CompareObjStateId(z305, z308, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z307, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x23(z305=50372500, z306=40, z307=537000040, z308=40):
    """[Lib] [Preset] Elevator_Initialization
    z305: Elevator OBJ instance ID
    z306: Initial position OBJ state ID
    z307: Initialization completion flag
    z308: [Preset] 棺 桶 Bobsleigh_Initialization_SubState
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m50_37_x20(z307=z307)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m50_37_x21()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m50_37_x22(z305=z305, z306=z306, z307=z307, z308=z308)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m50_37_x24(z300=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z300: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m50_37_x25(z300=z300)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m50_37_x32(z300=z300)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m50_37_x33()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m50_37_x26(z300=z300, mode4=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m50_37_x27(z300=z300, z302=38, z303=3, z304=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m50_37_x28(z300=z300, z301=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m50_37_x25(z300=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z300: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z300, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z300, 10)
        assert CompareObjStateId(z300, 10, 0)
    elif CompareObjStateId(z300, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z300, 74, 1) and CompareObjStateId(z300, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m50_37_x26(z300=_, mode4=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z300: Object instance ID
    mode4: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z300)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode4) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m50_37_x27(z300=_, z302=38, z303=3, z304=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z300: Object instance ID
    z302: Key guide type
    z303: Event action
    z304: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z300, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z300, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z300, 30)
        assert CompareObjStateId(z300, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z300, z302, z303)
        assert PlayerIsInEventAction(z303) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z303, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z300, 74, 0)
        CompareObjState(1, z300, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z304)
            assert CompareObjStateId(z300, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z300, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m50_37_x28(z300=_, z301=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z300: Object instance ID
    z301: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z300, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m50_37_x29(z296=50372900, z297=30, z298=240, z299=1):
    """[Reproduction] Spring of recovery
    z296: OBJ instance ID of the bug key
    z297: Hit group ID
    z298: Replacement GMID
    z299: Switching GM slot
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z296, 20, 0):
        """State 2: Water OBJ: OBJ state transition: 20"""
        ChangeOwnObjState(20)
        """State 3: Enable recovery"""
        SetGroundMaterial(z297, z298, z299)
        """State 4: Activated"""
        return 0
    else:
        """State 5: Not running"""
        return 1

def event_m50_37_x30(z296=50372900):
    """[Condition] Spring of recovery
    z296: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z296, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x31(z297=30, z298=240, z299=1):
    """[Execution] Recovery Fountain
    z297: Hit group ID
    z298: Replacement GMID
    z299: Switching GM slot
    """
    """State 0,1: Water OBJ: OBJ state transition: 70"""
    ChangeOwnObjState(70)
    assert (GetStateTime() > 1) != 0
    """State 2: Enable recovery"""
    SetGroundMaterial(z297, z298, z299)
    """State 3: Waiting for the end of anime"""
    assert CompareOwnObjStateId(20, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x32(z300=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z300: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z300, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x33():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x34(z296=50372900, z297=30, z298=240, z299=1):
    """[Lib] [Preset] Recovery Fountain
    z296: OBJ instance ID of the bug key
    z297: Hit group ID
    z298: Replacement GMID
    z299: Switching GM slot
    """
    """State 0,1: [Reproduction] Recovery Fountain_SubState"""
    call = event_m50_37_x29(z296=z296, z297=z297, z298=z298, z299=z299)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Condition] Recovery Fountain_SubState"""
        assert event_m50_37_x30(z296=z296)
        """State 2: [Execution] Recovery Fountain_SubState"""
        assert event_m50_37_x31(z297=z297, z298=z298, z299=z299)
    """State 4: End state"""
    return 0

def event_m50_37_x35(z294=50372800, val3=50370000):
    """[Reproduction] Hidden door 1_face SFX
    z294: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z294, 20, 0):
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

def event_m50_37_x36(z294=50372800):
    """[Conditions] Hidden door 1_Face SFX
    z294: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z294, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x37(z294=50372800, val3=50370000, z295=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z294: OBJ instance ID of the bug key
    val3: Event light ID
    z295: Light fade time
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
        SetPointLightEnabled(val3, 1, z295)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m50_37_x38(z294=50372800, val3=50370000, z295=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z294: OBJ instance ID of the bug key
    val3: Event light ID
    z295: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m50_37_x35(z294=z294, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m50_37_x36(z294=z294)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m50_37_x37(z294=z294, val3=val3, z295=z295, val4=val4)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m50_37_x39():
    """[Lib] [Reproduction] OBJ attach_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_100040():
    """White Spirit Sign Display_Ice King_Female Knight"""
    """State 0,1: White knight flag watch"""
    if GetEventFlag(537000020) != 0:
        pass
    elif GetEventFlag(537000021) != 0:
        pass
    elif GetEventFlag(537000022) != 0:
        pass
    """State 2: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m50_37_x55(z268=537000086, z269=102498, z270=204, z271=7520)

def event_m50_37_x40():
    """[Lib] [Condition] OBJ attach_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_100041():
    """White Spirit Sign Display_Ice King_Female Knight_Summoning Conditions"""
    """State 0,1: White knight flag watch"""
    if GetEventFlag(537000020) != 0:
        pass
    elif GetEventFlag(537000021) != 0:
        pass
    elif GetEventFlag(537000022) != 0:
        pass
    """State 2: [Lib] NPC White Phantom Appearance: General Purpose: Body Coexistence_SubState"""
    event_m50_37_x47(z280=102502, z281=770, z282=104190, z283=61, z284=103690, z285=-1)

def event_m50_37_x41(z291=_, z292=150, z293=_):
    """[Lib] [execute] OBJ attach
    z291: Parent OBJ instance ID
    z292: Parent Damipoli ID
    z293: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z291, z292, z293)
    """State 2: End state"""
    return 0

def event_m50_37_x42(z291=_, z292=150, z293=_):
    """[Lib] [Preset] OBJ attach
    z291: Parent OBJ instance ID
    z292: Parent Damipoli ID
    z293: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m50_37_x39()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m50_37_x40()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m50_37_x41(z291=z291, z292=z292, z293=z293)
    """State 4: End state"""
    return 0

def event_m50_37_x43(z286=_, z287=20, z288=_, z289=_, z290=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z286: Object instance ID
    z287: OBJ state ID
    z288: Navimesh switching point ID
    z289: Additional attributes
    z290: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m50_37_x44(z286=z286, z287=z287, z288=z288, z290=z290, z289=z289)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m50_37_x45(z286=z286, z287=z287, z288=z288)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m50_37_x46(z286=z286, z287=z287, z288=z288, z289=z289, z290=z290)
    """State 4: End state"""
    return 0

def event_m50_37_x44(z286=_, z287=20, z288=_, z290=_, z289=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z286: Target OBJ instance ID
    z287: Target OBJ state ID
    z288: Navimesh switching point ID
    z290: Additional attributes
    z289: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z286, z287, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z288, z290)
        DeleteNavimeshAttribute(z288, z289)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m50_37_x45(z286=_, z287=20, z288=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z286: Target OBJ instance ID
    z287: Target OBJ state ID
    z288: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z286, z287, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x46(z286=_, z287=20, z288=_, z289=_, z290=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z286: Target OBJ instance ID
    z287: Target OBJ state ID
    z288: Navimesh switching point ID
    z289: Additional attributes
    z290: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z288, z289)
    DeleteNavimeshAttribute(z288, z290)
    """State 2: End state"""
    return 0

def event_m50_37_x47(z280=102502, z281=770, z282=104190, z283=61, z284=103690, z285=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z280: White Phantom can appear: Global event flag
    z281: White Phantom: Generator ID
    z282: Death: Global event flag
    z283: Body: Generator group ID
    z284: Hostile: Global event flag
    z285: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z281)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z282, 1)
        CompareEventFlag(1, z284, 1)
        CompareEventFlag(2, z280, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z281)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z282, 1)
            CompareEventFlag(1, z284, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z281)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z282, 1)
            CompareEventFlag(1, z284, 1)
            HasNpcPhantomSpawned(2, z281, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z283, 0)
                HasNpcPhantomSpawned(0, z281, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z281)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m50_37_x48(z275=_, z276=_):
    """[Execution] Elevator_Return switch after lift
    z275: Elevator OBJ instance ID
    z276: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z275, 30, 0)
    IsPlayerInsidePoint(8, z276, z276, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z275, 71)
    assert CompareObjStateId(z275, 40, 0)
    """State 3: End state"""
    return 0

def event_m50_37_x49(z275=_, z277=_):
    """[Execution] Elevator_Return switch after descending
    z275: Elevator OBJ instance ID
    z277: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z275, 41, 0)
    IsPlayerInsidePoint(8, z277, z277, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z275, 81)
    assert CompareObjStateId(z275, 10, 0)
    """State 3: End state"""
    return 0

def event_m50_37_100050():
    """White spirit sign display_Yukihara_Durahan"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m50_37_x60(z258=102000, z259=774, z260=104000, z261=103500, z262=-1)

def event_m50_37_x50(z274=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z274: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z274)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m50_37_x51():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x52(z272=_, z273=_):
    """[Lib] [execute] Rebirth fire
    z272: Flag start ID
    z273: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z272, z273, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x53():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x54(z272=_, z273=_):
    """[Lib] [Preset] Rebirth
    z272: Flag start ID
    z273: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m50_37_x51()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m50_37_x53()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m50_37_x52(z272=z272, z273=z273)
    """State 4: End state"""
    return 0

def event_m50_37_x55(z268=537000086, z269=102498, z270=204, z271=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z268: Defeat Boss 1: Area and other flags
    z269: Summon Achievement: Global Event Flag
    z270: Summon achievement count: global variable
    z271: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z269, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z268, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z270, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z270, NpcInfoValue(z271, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z269, 1)
                CompareEventFlag(0, z269, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m50_37_x56(z266=_, z267=0, z265=0, z264=2, z263=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z266: Other flags
    z267: Global flag
    z265: Additional attributes
    z264: Delete attribute
    z263: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z266) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z267) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z263, z265)
        DeleteNavimeshAttribute(z263, z264)
        """State 3: Flag OFF"""
        return 0

def event_m50_37_x57(z266=_, z267=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z266: Other flags
    z267: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z266, 1)
    CompareEventFlag(0, z267, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m50_37_x58(z263=_, z264=2, z265=0):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z263: Navimesh switching point ID
    z264: Additional attributes
    z265: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z263, z264)
    DeleteNavimeshAttribute(z263, z265)
    """State 2: End state"""
    return 0

def event_m50_37_x59(z263=_, z264=2, z265=0, z266=_, z267=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z263: Navimesh switching point ID
    z264: Additional attributes
    z265: Delete attribute
    z266: Other flags
    z267: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m50_37_x56(z266=z266, z267=z267, z265=z265, z264=z264, z263=z263)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m50_37_x57(z266=z266, z267=z267)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m50_37_x58(z263=z263, z264=z264, z265=z265)
    """State 4: End state"""
    return 0

def event_m50_37_100060():
    """White spirit sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z274=777)

def event_m50_37_x60(z258=102000, z259=774, z260=104000, z261=103500, z262=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z258: White Phantom can appear: Global event flag
    z259: White Phantom: Generator ID
    z260: Death: Global event flag
    z261: Hostile: Global event flag
    z262: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z259)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z260, 1)
        CompareEventFlag(1, z261, 1)
        CompareEventFlag(2, z258, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z259)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z260, 1)
            CompareEventFlag(1, z261, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z259)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z260, 1)
            CompareEventFlag(1, z261, 1)
            HasNpcPhantomSpawned(2, z259, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z259, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z259)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m50_37_x61(z254=_):
    """[Lib] [Reproduction] Shop Lineup
    z254: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(z254) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m50_37_x62(z254=_):
    """[Lib] [execution] shop lineup
    z254: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(z254, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x63(z255=50371000):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z255: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z255)
    """State 2: End state"""
    return 0

def event_m50_37_x64(z255=50371000):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z255: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z255, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z255)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m50_37_x65(z255=50371000, z256=10320000, z257=5200000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z255: Warp OBJ instance ID
    z256: Map ID
    z257: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z255, 1)
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
        assert event_m50_37_x0(z326=0, z327=0, z256=z256, z37=z257)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m50_37_x66(z255=50371000):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z255: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z255, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x67(z255=50371000, z256=10320000, z257=5200000):
    """[Lib] [Preset] Warp move between main part and DLC
    z255: Warp OBJ instance ID
    z256: Map ID
    z257: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m50_37_x63(z255=z255)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m50_37_x64(z255=z255)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m50_37_x66(z255=z255)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m50_37_x65(z255=z255, z256=z256, z257=z257)
    """State 5: End state"""
    return 0

def event_m50_37_x68(z253=_):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z253: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z253, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x69(z253=_, z254=_):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z253: Boss destruction flag
    z254: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m50_37_x61(z254=z254)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m50_37_x68(z253=z253)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m50_37_x62(z254=z254)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_37_100070():
    """White Spirit Sign Display_Attribute Hunter"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z274=776)

def event_m50_37_x70(z248=_, z249=_, z250=0, z251=_, z252=_):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON
    z248: Summon range
    z249: Generator ID
    z250: Appearance: Minimum time
    z251: Appearance: Maximum time
    z252: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z248, z248, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z250, 3, z251)
        IsPlayerInsidePoint(1, z248, z248, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z249)
            SetEventFlag(z252, 1)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m50_37_x71(z233=537020055, z235=537000056):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z233: Lottery determination flag
    z235: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z235) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z233) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m50_37_x72(z234=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z234: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z234, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m50_37_x73(z233=537020055, z236=3, z237=40):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z233: Lottery determination flag
    z236: Number of appearance judgment points
    z237: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z233, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z236)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z237, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m50_37_x74(z233=537020055, z234=14, z235=537000056, z236=3, z237=40):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z233: Lottery determination flag
    z234: Random number comparison value
    z235: Defeat flag
    z236: Number of appearance judgment points
    z237: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m50_37_x71(z233=z233, z235=z235)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m50_37_x72(z234=z234)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m50_37_x73(z233=z233, z236=z236, z237=z237)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m50_37_x83(z233=z233, z237=z237)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m50_37_x75(val2=_, z245=40):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z245: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z245) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_37_x76(z241=_, z242=0, z243=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z241: Appearance judgment point ID
    z242: Minimum appearance time
    z243: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z241, z241, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z242, 3, z243)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_37_x77(z244=980, z246=_, z247=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z244: Generator ID
    z246: Appearance start point ID
    z247: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z244, z246, z247)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z244)
    """State 4: Finish"""
    return 0

def event_m50_37_x78(z238=537000056):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z238: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z238) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m50_37_x79(z241=_, z242=0, z243=5, z244=980, val2=_, z245=40, z246=_, z247=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z241: Intrusion detection point ID
    z242: Minimum appearance time
    z243: Maximum time to appear
    z244: Generator ID
    val2: Appearance judgment number
    z245: Lottery result point variable
    z246: Appearance start point ID
    z247: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m50_37_x75(val2=val2, z245=z245)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m50_37_x76(z241=z241, z242=z242, z243=z243)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m50_37_x77(z244=z244, z246=z246, z247=z247)
    """State 4: Finish"""
    return 0

def event_m50_37_x80(z239=980, mode3=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z239: Generator ID
    mode3: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z239)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode3) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m50_37_x81(z238=537000056, z240=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z238: Defeat flag
    z240: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z238, 1)
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
                    SetEventFlag(z240, 1)
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

def event_m50_37_x82(z238=537000056, z239=980, mode3=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z238: Defeat flag
    z239: Generator ID
    mode3: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m50_37_x78(z238=z238)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m50_37_x80(z239=z239, mode3=mode3)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m50_37_x81(z238=z238, z240=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m50_37_x81(z238=z238, z240=102755)
    """State 5: End state"""
    return 0

def event_m50_37_x83(z233=537020055, z237=40):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z233: Lottery determination flag
    z237: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z233, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z237, 0)
    """State 3: End state"""
    return 0

def event_m50_37_x84():
    """[Reproduction] Falling damage disabled_player"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x85(z231=100000, z232=100001):
    """[Condition] Fall damage invalid_player
    z231: Start point ID
    z232: End point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z231, z232, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x86(z231=100000, z232=100001):
    """[Execution] Falling damage disabled_player
    z231: Start point ID
    z232: End point ID
    """
    """State 0,1: Drop damage disabled"""
    DisablePlayerFallDamageOnce()
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z231, z232, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m50_37_x87(z231=100000, z232=100001):
    """[Preset] Falling damage disabled_player
    z231: Start point ID
    z232: End point ID
    """
    """State 0,1: [Reproduction] Falling damage invalid_player_SubState"""
    assert event_m50_37_x84()
    """State 3: [Condition] Fall damage invalid_player_SubState"""
    assert event_m50_37_x85(z231=z231, z232=z232)
    """State 2: [Execution] Fall damage invalid_player_SubState"""
    assert event_m50_37_x86(z231=z231, z232=z232)
    """State 4: Rerun"""
    return 0

def event_m50_37_x88():
    """[Reproduction] Invalid fall damage_NPC"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x89(z228=100000, z229=100001, z230=_):
    """[Condition] Fall damage invalid_NPC
    z228: Start point ID
    z229: End point ID
    z230: Generator ID
    """
    """State 0,1: Point judgment"""
    IsChrInsidePoint(0, z230, z228, z229, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x90(z228=100000, z229=100001, z230=_):
    """[Execution] Fall damage invalid_NPC
    z228: Start point ID
    z229: End point ID
    z230: Generator ID
    """
    """State 0,1: Drop damage disabled"""
    DisableEnemyFallDamageOnce(z230)
    """State 2: Did you get out of the point?"""
    IsChrInsidePoint(0, z230, z228, z229, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m50_37_x91(z228=100000, z229=100001, z230=_):
    """[Preset] Fall damage disabled_NPC
    z228: Start point ID
    z229: End point ID
    z230: Generator ID
    """
    """State 0,1: [Reproduction] Invalid fall damage_NPC_SubState"""
    assert event_m50_37_x88()
    """State 3: [Condition] Fall damage invalid_NPC_SubState"""
    assert event_m50_37_x89(z228=z228, z229=z229, z230=z230)
    """State 2: [Execution] Fall damage invalid_NPC_SubState"""
    assert event_m50_37_x90(z228=z228, z229=z229, z230=z230)
    """State 4: Rerun"""
    return 0

def event_m50_37_x92(z223=_, z222=_):
    """[Reproduction] Release of White Knight
    z223: Release flag
    z222: Generator ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is it already released?"""
    if GetEventFlag(z223) != 0:
        """State 3: Delete character"""
        DeleteEnemyByGenerator(z222, 0)
        """State 5: Released"""
        return 1
    else:
        """State 4: Wait for judgment"""
        return 0
    """State 6: Guest: Exit"""
    Label('L0')
    return 2

def event_m50_37_x93(z222=_, z227=5):
    """[Condition] Release of White Knight
    z222: Generator ID
    z227: Judgment distance
    """
    """State 0,1: Approached or died"""
    CompareChrPlayerDistance(0, z222, z227, 5)
    IsChrDead(1, z222)
    if ConditionGroup(1):
        """State 3: Died"""
        return 1
    elif ConditionGroup(0):
        """State 2: Approached"""
        return 0

def event_m50_37_x94(z223=_, z222=_, z225=96880100, z226=1):
    """[Execution] Release of White Knight
    z223: Release flag
    z222: Generator ID
    z225: Feedback special effect ID
    z226: weight
    """
    """State 0,4: Weight until action"""
    CompareStateTime(0, z226, 3, z226)
    assert ConditionGroup(0)
    """State 1: Release flag ON"""
    SetEventFlag(z223, 1)
    """State 2: Waiting for completion of return action"""
    ChrHasSpEffect(0, z222, z225, 1)
    CompareStateTime(0, 30, 3, 30)
    assert ConditionGroup(0)
    """State 3: Delete character"""
    DeleteEnemyByGenerator(z222, 0)
    """State 5: Message display"""
    # action:5840:"A knight of Eleum Loyce seeks the Chaos..."
    DisplayEventMessage(5840, 0, 0, 0)
    """State 6: End state"""
    return 0

def event_m50_37_x95(z222=_, z223=_, z224=5.5, z225=96880100, z226=1):
    """[Preset] Release of White Knight
    z222: Generator ID
    z223: Release flag
    z224: Judgment distance
    z225: Feedback special effect ID
    z226: Wait until startup
    """
    """State 0,1: [Reproduction] Liberation of White Knight_SubState"""
    call = event_m50_37_x92(z223=z223, z222=z222)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] White Knight Release_SubState"""
        call = event_m50_37_x93(z222=z222, z227=5)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Release of White Knight_SubState"""
            assert event_m50_37_x94(z223=z223, z222=z222, z225=z225, z226=z226)
    elif call.Get() == 2:
        pass
    """State 4: End state"""
    return 0

def event_m50_37_x96():
    """[Reproduction] Torches disappear due to snowstorm"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x97(z219=10, z220=537000001, z221=30):
    """[Condition] Torches disappear due to snowstorm
    z219: Main_Hit group ID
    z220: Snowstorm stop flag
    z221: Yukihara_Hit Group ID
    """
    """State 0,1: Are you wearing a torch under a snowstorm?"""
    SetConditionGroup(0, 8)
    CompareEventFlag(8, z220, 0)
    IsPlayerOnHitGroup(8, z219, 1)
    IsPlayerUsingTorch(8, 1)
    SetConditionGroup(0, 9)
    IsPlayerOnHitGroup(9, z221, 1)
    IsPlayerUsingTorch(9, 1)
    assert ConditionGroup(0)
    """State 2: Erase torches"""
    return 0

def event_m50_37_x98():
    """[Execution] A torch disappears in a snowstorm"""
    """State 0,1: Turn off torches"""
    RemovePlayerTorches(10)
    """State 2: Has the torch disappeared?"""
    IsPlayerUsingTorch(0, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x99(z219=10, z220=537000001, z221=30):
    """[Preset] Torches disappear with snowstorm
    z219: Main_Hit group ID
    z220: Snowstorm stop flag
    z221: Yukihara_Hit Group ID
    """
    """State 0,1: [Reproduction] A torch disappears in a snowstorm _SubState"""
    assert event_m50_37_x96()
    """State 3: [Condition] A torch disappears in a snowstorm_SubState"""
    assert event_m50_37_x97(z219=z219, z220=z220, z221=z221)
    """State 2: [Execution] Torch disappears due to snowstorm_SubState"""
    assert event_m50_37_x98()
    """State 4: Rerun"""
    return 0

def event_m50_37_x100(z131=537000086, z132=50371001, z133=537000002):
    """[Reproduction] Return from the boss room
    z131: Defeat flag
    z132: Warp OBJ instance ID
    z133: Crown acquisition flag
    """
    """State 0,1: Did you destroy the boss?"""
    if GetEventFlag(z131) != 0:
        """State 3: Has the crown been acquired?"""
        if GetEventFlag(z133) != 0:
            """State 2: Warp OBJ has appeared: 30"""
            ChangeObjState(z132, 30)
            """State 5: Acquired and destroyed"""
            return 1
        else:
            pass
    else:
        pass
    """State 4: Not destroy or get"""
    return 0

def event_m50_37_x101(z131=537000086, z133=537000002):
    """[Condition] Return from the boss room _ Defeat the boss
    z131: Boss destruction flag
    z133: Crown acquisition flag
    """
    """State 0,1: Destroyed the boss & got the crown?"""
    CompareEventFlag(8, z131, 1)
    CompareEventFlag(8, z133, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x102(z37=_):
    """[Execution] Return from Boss Room_Warp
    z37: Warp destination point ID
    """
    """State 0,4: Warp PC action"""
    PlayerActionRequest(6)
    assert PlayerIsInEventAction(6) != 0
    """State 5: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 6, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 6: PC invincibility"""
        SetPlayerInvincible(1)
        assert (GetStateTime() > 2.5) != 0
        """State 1: Multiplayer prohibited state: ON"""
        ProhibitMultiplayer(1)
        """State 2: Save execution"""
        SaveExecution()
        """State 8: [Lib] Warp between maps after poly play_SubState"""
        assert event_m50_37_x0(z326=0, z327=0, z256=50370000, z37=z37)
        """State 3: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
        """State 7: Unbeatable PC"""
        SetPlayerInvincible(0)
    """State 9: End state"""
    return 0

def event_m50_37_x103(z130=3100010, z131=537000086, z132=50371001, z133=537000002):
    """[Preset] Return from Boss Room
    z130: Warp destination point ID
    z131: Boss destruction flag
    z132: Warp OBJ instance ID
    z133: Crown acquisition flag
    """
    """State 0,1: [Reproduction] Return from the boss room_SubState"""
    call = event_m50_37_x100(z131=z131, z132=z132, z133=z133)
    if call.Get() == 1:
        """State 5: [Condition] Return from the boss room_Judgment to check_SubState"""
        assert event_m50_37_x209(z38=z132)
        """State 3: [Execution] Return from Boss Room_Warp_SubState"""
        assert event_m50_37_x102(z37=z130)
    elif call.Get() == 0:
        """State 4: [Condition] Return from Boss Room_Boss Defeat_SubState"""
        assert event_m50_37_x101(z131=z131, z133=z133)
        """State 2: [Execution] Return from Boss Room_OBJ Appearance_SubState"""
        assert event_m50_37_x208(z132=z132)
    """State 6: Rerun"""
    return 0

def event_m50_37_x104(z213=50370700, z214=50370701, z215=50370702, z216=50370703):
    """[Conditions] The door opens when the lighthouse is lit
    z213: Lighthouse ①OBJ instance ID
    z214: Lighthouse ②OBJ instance ID
    z215: Lighthouse ③ OBJ instance ID
    z216: Lighthouse ④ OBJ instance ID
    """
    """State 0,1: Is the light on the lighthouse?"""
    CompareObjState(8, z213, 30, 0)
    CompareObjState(8, z214, 30, 0)
    CompareObjState(8, z215, 30, 0)
    CompareObjState(8, z216, 30, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x105(z217=50372001, z218=900000):
    """[Execution] The door opens when the lighthouse is on
    z217: Door OBJ instance ID
    z218: Navigation change point ID
    """
    """State 0,1: The door opens: 70"""
    ChangeObjState(z217, 70)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z217, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh change: passable"""
    DeleteNavimeshAttribute(z218, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x106(z213=50370700, z214=50370701, z215=50370702, z216=50370703, z217=50372001, z218=900000):
    """[Preset] The door opens when the lighthouse is on
    z213: Lighthouse ①OBJ instance ID
    z214: Lighthouse ②OBJ instance ID
    z215: Lighthouse ③ OBJ instance ID
    z216: Lighthouse ④ OBJ instance ID
    z217: Door OBJ instance ID
    z218: Navigation change point ID
    """
    """State 0,1: [Reproduction] The door opens when the lighthouse lights up_SubState"""
    call = event_m50_37_x107(z217=z217, z218=z218)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] The door opens when the lighthouse is lit._SubState"""
        assert event_m50_37_x104(z213=z213, z214=z214, z215=z215, z216=z216)
        """State 2: [Execution] The door opens when the lighthouse lights up_SubState"""
        assert event_m50_37_x105(z217=z217, z218=z218)
    """State 4: End state"""
    return 0

def event_m50_37_x107(z217=50372001, z218=900000):
    """[Reproduction] The door opens when the lighthouse is on
    z217: Door OBJ instance ID
    z218: Navigation change point ID
    """
    """State 0,1: Is the door open?"""
    if CompareObjStateId(z217, 10, 1):
        """State 5: Navimesh change: non-passable_2"""
        AddNavimeshAttribute(z218, 2)
        """State 2: Waiting for the door to open"""
        assert CompareObjStateId(z217, 20, 0)
        """State 4: Navimesh change: passable"""
        DeleteNavimeshAttribute(z218, 2)
        """State 7: End state"""
        return 1
    else:
        """State 3: Navimesh change: no traffic"""
        AddNavimeshAttribute(z218, 2)
        """State 6: Not open"""
        return 0

def event_m50_37_x108(z209=50370400, z210=5300010, z211=5300000, z212=5300001):
    """[Preset] Door that opens with DLC purchase
    z209: Door OBJ instance ID
    z210: Navigation switching point ID
    z211: Judgment start point ID
    z212: Judgment end point ID
    """
    """State 0,1: [Reproduction] Doors opened with DLC purchase_SubState"""
    call = event_m50_37_x109(z209=z209, z210=z210)
    if call.Get() == 0:
        """State 3: [Conditions] Doors opened by DLC purchase_SubState"""
        call = event_m50_37_x111(z209=z209, z211=z211, z212=z212)
        if call.Get() == 0:
            """State 6: [Execution] Door opened by DLC purchase_Manual_SubState"""
            assert event_m50_37_x114(z209=z209, z210=z210)
            Goto('L0')
        elif call.Get() == 2:
            """State 5: [Execution] Door opened with DLC purchase_Auto_SubState"""
            assert event_m50_37_x113(z209=z209, z210=z210)
            Goto('L0')
        elif call.Get() == 1:
            """State 7: [Execution] Door that opens with DLC purchase_No access_Front_SubState"""
            assert event_m50_37_x115(z209=z209)
        elif call.Get() == 3:
            """State 8: [Execution] Door opened with DLC purchase_No access_Back_SubState"""
            assert event_m50_37_x116(z209=z209)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Conditions] Doors opened by DLC purchase_Guest_SubState"""
        assert event_m50_37_x112(z209=z209)
        """State 2: [Execution] Door opened with DLC purchase_Guest_SubState"""
        assert event_m50_37_x110(z209=z209, z210=z210)
    """State 10: Finish"""
    Label('L0')
    return 1

def event_m50_37_x109(z209=50370400, z210=5300010):
    """[Reproduction] Door opened with DLC purchase
    z209: Door OBJ instance ID
    z210: Navigation switching point ID
    """
    """State 0,2: Navigation switching_initialization"""
    AddNavimeshAttribute(z210, 2)
    """State 1: Host?"""
    if IsGuest() != 1:
        """State 3: Safety: Door initialization"""
        InitializeObj(z209)
        assert CompareObjStateId(z209, 10, 0)
        """State 4: Disable key guide"""
        DisableObjKeyGuide(z209, 1)
        """State 5: Not passed"""
        return 0
    else:
        """State 6: The guests"""
        return 1

def event_m50_37_x110(z209=50370400, z210=5300010):
    """[Execution] Door opened with DLC purchase_Guest
    z209: King's door OBJ instance ID
    z210: Navigation switching point ID
    """
    """State 0,1: Change navigation"""
    DeleteNavimeshAttribute(z210, 2)
    """State 2: End state"""
    return 0

def event_m50_37_x111(z209=50370400, z211=5300000, z212=5300001):
    """[Conditions] Doors opened by DLC purchase
    z209: Door OBJ instance ID
    z211: Judgment start point ID
    z212: Judgment end point ID
    """
    """State 0,2: Distance judgment or point judgment"""
    CompareObjPlayerDistance(0, z209, 4, 5)
    SetConditionGroup(1, 8)
    IsPlayerInsidePoint(8, z211, z212, 1)
    IsHost(8, 1, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4,5: Player status determination_2"""
    CompareEventFlag(8, 100602, 1)
    CompareEventFlag(8, 100612, 1)
    # goods:52200000:Frozen Flower
    DoesPlayerHaveItem(8, 52200000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 8: Back: Allowed"""
        return 2
    else:
        """State 9: Back: No traffic"""
        return 3
    """State 3: Approach from the front"""
    Label('L0')
    """State 1: Player status determination"""
    CompareEventFlag(8, 100602, 1)
    CompareEventFlag(8, 100612, 1)
    # goods:52200000:Frozen Flower
    DoesPlayerHaveItem(8, 52200000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 6: Front: Allowed"""
        return 0
    else:
        """State 7: Front: No traffic"""
        return 1

def event_m50_37_x112(z209=50370400):
    """[Conditions] Doors opened with DLC purchase_Guest
    z209: Door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z209, 20, 0)
    assert ConditionGroup(0)
    """State 2: Mural opened"""
    return 0

def event_m50_37_x113(z209=50370400, z210=5300010):
    """[Execution] Door opened with DLC purchase_Auto
    z209: Door OBJ instance ID
    z210: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z209, 20)
    """State 2: Waiting for the door to finish"""
    CompareObjState(0, z209, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z210, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x114(z209=50370400, z210=5300010):
    """[Execution] Door opened with DLC purchase_Manual
    z209: Door OBJ instance ID
    z210: Navigation switching point ID
    """
    """State 0,3: Activate key guide"""
    DisableObjKeyGuide(z209, 0)
    """State 1: Waiting for the door to finish"""
    CompareObjState(0, z209, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation switching"""
    DeleteNavimeshAttribute(z210, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x115(z209=50370400):
    """[Execution] Door opened with DLC purchase
    z209: Door OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z209, 8, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x116(z209=50370400):
    """[Execution] Door opened with DLC purchase
    z209: Door OBJ instance ID
    """
    """State 0,3: Did you approach the door?"""
    CompareObjPlayerDistance(0, z209, 4, 5)
    assert ConditionGroup(0)
    """State 1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z209, 8, 3)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m50_37_x117():
    """[Reproduction] 棺 桶 Bobsleigh"""
    """State 0,1: Host judgment"""
    if IsGuest() != 0:
        """State 3: Guest termination"""
        return 1
    else:
        """State 2: End state"""
        return 0

def event_m50_37_x118(z207=50371010):
    """[Conditions] 棺 桶 Bobsled
    z207: 棺 桶 OBJ instance ID
    """
    """State 0,1: Judgment to check or multiplayer judgment"""
    IsObjSearched(0, z207)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 3: During multiplayer"""
        return 1
    elif ConditionGroup(0):
        """State 2: Examined"""
        return 0

def event_m50_37_x119(z207=50371010, z208=537000005):
    """[Execution] 棺 桶 Bobsled
    z207: 棺 桶 OBJ instance ID
    z208: PC start flag
    """
    """State 0,7: Menu auto-save multi-disabled"""
    DisableAutoSave(1)
    ProhibitInGameMenu(1)
    ProhibitMultiplayer(1)
    """State 1: Action request to player"""
    ObjAnimationPlayerControlRequest(z207, 34, 13)
    assert PlayerIsInEventAction(13) != 0
    """State 14: PC invincible ON"""
    SetPlayerInvincible(1)
    """State 6: キ ャ ン セ ル moved or canceled"""
    CompareObjState(0, z207, 30, 0)
    IsPlayerPlayingMotion(1, 13, 0)
    if ConditionGroup(1):
        """State 5: Initialize 棺 桶: 10"""
        ChangeObjState(z207, 10)
        """State 10: 待 ち Waiting for initialization"""
        CompareObjState(0, z207, 10, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(0):
        """State 11: Hide player"""
        SetHidePlayer(1)
        """State 13: Bobsled start: 90"""
        ChangeObjState(z207, 90)
        """State 4: weight"""
        assert (GetStateTime() > 5) != 0
        """State 2: Warp processing"""
        PlayCutsceneAndWarpToMap(0, 0, 50370000, 400000, 2)
        """State 3: Startup motion flag ON"""
        SetEventFlag(z208, 1)
        """State 9: Is it gone in game?"""
        assert InGame() != 1
        """State 12: Player display"""
        SetHidePlayer(0)
    """State 15: PC invincible OFF"""
    SetPlayerInvincible(0)
    """State 8: Menu auto save multi enable"""
    DisableAutoSave(0)
    ProhibitInGameMenu(0)
    ProhibitMultiplayer(0)
    """State 16: Rerun"""
    return 0

def event_m50_37_x120(z207=50371010):
    """[Execution] 棺 桶 Bobsleigh_Multi
    z207: 棺 桶 OBJ instance ID
    """
    """State 0,1: 棺 桶 Disable key guide"""
    DisableObjKeyGuide(z207, 1)
    """State 2: Waiting for multi end"""
    IsMultiplayer(0, 0, 0)
    assert ConditionGroup(0)
    """State 3: 棺 桶 Activating key guide"""
    DisableObjKeyGuide(z207, 0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x121(z207=50371010, z208=537000005):
    """[Preset] 棺 桶 Bobsled
    z207: 棺 桶 OBJ instance ID
    z208: PC start flag
    """
    """State 0,1: [Reproduction] 棺 桶 Bobsleigh_SubState"""
    call = event_m50_37_x117()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Guest termination"""
    return 1
    """State 4: [Condition] 棺 桶 Bobsleigh_SubState"""
    Label('L0')
    call = event_m50_37_x118(z207=z207)
    if call.Get() == 0:
        """State 2: [Execution] 棺 桶 Bobsleigh_SubState"""
        assert event_m50_37_x119(z207=z207, z208=z208)
    elif call.Get() == 1:
        """State 3: [Execution] 棺 桶 Bobsled_Multi Medium_SubState"""
        assert event_m50_37_x120(z207=z207)
    """State 5: Rerun"""
    return 0

def event_m50_37_x122(z205=537000005, z206=50371011):
    """[Reproduction] 棺 桶 Startup event
    z205: PC start flag
    z206: 棺 桶 OBJ instance ID
    """
    """State 0,1: Is the PC start flag ON?"""
    if GetEventFlag(z205) != 0:
        """State 2: 棺 桶 Closed state: 30"""
        ChangeObjState(z206, 30)
        """State 3: Motion playback"""
        return 0
    else:
        """State 4: do nothing"""
        return 1

def event_m50_37_x123():
    """[Condition] 棺 桶 Startup event"""
    """State 0,1: Is it in game?"""
    assert InGame() != 0
    """State 2: End state"""
    return 0

def event_m50_37_x124(z205=537000005, z206=50371011):
    """[Execution] 棺 桶 Startup event
    z205: PC start flag
    z206: 棺 桶 OBJ instance ID
    """
    """State 0,1: Open the casket: 80"""
    ChangeObjState(z206, 80)
    """State 2: PC start flag OFF"""
    SetEventFlag(z205, 0)
    """State 3: End state"""
    return 0

def event_m50_37_x125(z205=537000005, z206=50371011):
    """[Preset] 棺 桶 Startup event
    z205: PC start flag
    z206: 棺 桶 OBJ instance ID
    """
    """State 0,1: [Reproduction] 棺 桶 Startup event_SubState"""
    call = event_m50_37_x122(z205=z205, z206=z206)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] 棺 桶 Startup event_SubState"""
        assert event_m50_37_x123()
        """State 2: [Execution] 棺 桶 Startup event_SubState"""
        assert event_m50_37_x124(z205=z205, z206=z206)
    """State 4: End state"""
    return 0

def event_m50_37_x126(z202=537000011, z203=50371200, z204=210000):
    """[Reproduction] Canceling the ice seal
    z202: Seal release flag
    z203: Ice Seal OBJ Instance ID
    z204: Navigation change point ID
    """
    """State 0,1: Has the seal been released?"""
    if GetEventFlag(z202) != 0:
        """State 2: Seal is released"""
        ChangeObjState(z203, 70)
        """State 3: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z204, 2)
        """State 6: Canceled"""
        return 1
    else:
        """State 4: Navigation switch: Passable_2"""
        AddNavimeshAttribute(z204, 2)
        """State 5: Unreleased"""
        return 0

def event_m50_37_x127(z202=537000011):
    """[Condition] Release of ice seal
    z202: Seal release flag
    """
    """State 0,1: Was the seal released?"""
    CompareEventFlag(0, z202, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x128(z203=50371200, z204=210000):
    """[Execution] Release of ice seal
    z203: Ice Seal OBJ Instance ID
    z204: Navigation change point ID
    """
    """State 0,1: Seal is released"""
    ChangeObjState(z203, 70)
    """State 9: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z204, 2)
    assert (GetStateTime() > 4) != 0
    """State 2: Destructive SE Regeneration: 2100"""
    PlaySoundAtPoint(2100)
    assert (GetStateTime() > 0.8) != 0
    """State 3: Destructive SE Regeneration: 2110"""
    PlaySoundAtPoint(2110)
    """State 8: Event message display"""
    # action:5830:"Alsanna's seal is undone, and the winds of Eleum Loyce are ceased"
    DisplayEventMessage(5830, 0, 0, 0)
    assert (GetStateTime() > 1.2) != 0
    """State 4: Destructive SE Regeneration: 2120"""
    PlaySoundAtPoint(2120)
    assert (GetStateTime() > 1.4) != 0
    """State 5: Destructive SE Regeneration: 2130"""
    PlaySoundAtPoint(2130)
    assert (GetStateTime() > 0.8) != 0
    """State 10: Destructive SE Regeneration: 2160"""
    PlaySoundAtPoint(2160)
    assert (GetStateTime() > 1.9) != 0
    """State 6: Destructive SE Regeneration: 2140"""
    PlaySoundAtPoint(2140)
    assert (GetStateTime() > 2.7) != 0
    """State 11: Destructive SE Regeneration: 2170"""
    PlaySoundAtPoint(2170)
    assert (GetStateTime() > 1.7) != 0
    """State 7: Destructive SE Regeneration: 2150"""
    PlaySoundAtPoint(2150)
    """State 12: Conversation flag ON"""
    SetEventFlag(537020007, 1)
    """State 13: End state"""
    return 0

def event_m50_37_x129(z202=537000011, z203=50371200, z204=210000):
    """[Preset] Canceling the ice seal
    z202: Seal release flag
    z203: Ice Seal OBJ Instance ID
    z204: Navigation change point ID
    """
    """State 0,1: [Reproduction] Canceling the ice seal_SubState"""
    call = event_m50_37_x126(z202=z202, z203=z203, z204=z204)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Canceling the ice seal_SubState"""
        assert event_m50_37_x127(z202=z202)
        """State 2: [Execution] Canceling the ice seal_SubState"""
        assert event_m50_37_x128(z203=z203, z204=z204)
    """State 4: End state"""
    return 0

def event_m50_37_x130():
    """[Reproduction] Lighthouse under snowstorm"""
    """State 0,1: Key guide disabled"""
    DisableObjKeyGuide(50370700, 1)
    DisableObjKeyGuide(50370701, 1)
    DisableObjKeyGuide(50370702, 1)
    DisableObjKeyGuide(50370703, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x131(z201=537000001):
    """[Conditions] Lighthouse under snowstorm
    z201: Snowstorm stop flag
    """
    """State 0,1: Has the snowstorm stopped?"""
    CompareEventFlag(0, z201, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x132():
    """[Execution] Lighthouse under snowstorm"""
    """State 0,1: Key guide enabled"""
    DisableObjKeyGuide(50370700, 0)
    DisableObjKeyGuide(50370701, 0)
    DisableObjKeyGuide(50370702, 0)
    DisableObjKeyGuide(50370703, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x133(z201=537000001):
    """[Preset] Lighthouse under snowstorm
    z201: Snowstorm stop flag
    """
    """State 0,1: [Reproduction] Lighthouse _SubState under snowstorm"""
    assert event_m50_37_x130()
    """State 3: [Condition] Lighthouse under snowstorm_SubState"""
    assert event_m50_37_x131(z201=z201)
    """State 2: [Execution] Lighthouse under the snowstorm_SubState"""
    assert event_m50_37_x132()
    """State 4: End state"""
    return 0

def event_m50_37_x134(z33=537000086):
    """[Reproduction] Ice King Battle_Start
    z33: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z33) != 0:
        """State 3: Boss gate initialization"""
        InitializeObj(50371560)
        assert CompareObjStateId(50371560, 10, 0)
        """State 2: Boss gate state reproduction: 20"""
        ChangeObjState(50371560, 20)
        """State 5: Defeated the boss"""
        return 1
    else:
        """State 4: Not destroy the boss"""
        return 0

def event_m50_37_x135():
    """[Condition] Ice King Battle_Start"""
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, 3000000, 3000000, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, 3000000, 3000000, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x136(z35=5037000):
    """[Execution] Ice King Battle_Start
    z35: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z35)
    """State 2: Atmosphere sound playback"""
    PlaySoundAtPoint(30000)
    """State 3: End state"""
    return 0

def event_m50_37_x137():
    """[Reproduction] Ice King Battle Phase 2"""
    """State 0,1: Phase 2 flag ON"""
    SetEventFlag(537020172, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x138(z35=5037000):
    """[Condition] Ice King Battle_Phase 3
    z35: Boss Battle ID
    """
    """State 0,1: Did you destroy all bosses?"""
    IsEventBossKill(0, z35, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x139(z34=501, z35=5037000, z36=537020085):
    """[Execution] Ice King Battle Phase 2
    z34: Sound ID
    z35: Boss Battle ID
    z36: Other flags for logic
    """
    """State 0,5: King Appearance Phase Flag ON"""
    SetEventFlag(537020173, 1)
    """State 16: Are you a guest?"""
    if IsGuest() != 0:
        """State 17: Wait before arrival_Guest"""
        CompareStateTime(0, 5, 3, 5)
        CompareEventFlag(0, 537020089, 1)
        assert ConditionGroup(0)
        """State 20: Is the gate OBJ shaking?"""
        if CompareObjStateId(50371560, 70, 0):
            """State 19: Shake SE Playback: 30001_Guest"""
            PlaySoundAtPoint(30001)
        else:
            pass
        """State 18: Wait_Guest"""
        CompareEventFlag(0, 537020089, 1)
        assert ConditionGroup(0)
    else:
        """State 7: Weight before appearance"""
        CompareStateTime(0, 5, 3, 5)
        assert ConditionGroup(0)
        """State 3: Gate OBJ shakes: 70"""
        ChangeObjState(50371560, 70)
        """State 14: Shake SE playback: 30001"""
        PlaySoundAtPoint(30001)
        """State 12: weight"""
        CompareStateTime(0, 2, 3, 2)
        assert ConditionGroup(0)
        """State 11: Operation of gate OBJ: 71"""
        ChangeObjState(50371560, 71)
        """State 4: Gate end waiting"""
        CompareObjState(0, 50371560, 72, 0)
        assert ConditionGroup(0)
        """State 8: Point judgment or waiting time"""
        IsPlayerInsidePoint(0, 3000020, 3000020, 1)
        CompareStateTime(0, 7, 3, 7)
        assert ConditionGroup(0)
        """State 10: Weight before operation"""
        CompareStateTime(0, 3, 3, 3)
        assert ConditionGroup(0)
        """State 9: Flame from the gate OBJ: 73"""
        ChangeObjState(50371560, 73)
        """State 13: Weight until boss appearance"""
        CompareStateTime(0, 2, 3, 2)
        assert ConditionGroup(0)
        """State 2: Boss appearance flag ON"""
        SetEventFlag(537020089, 1)
    """State 1: Ice King: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 15: Wait until BGM playback"""
    CompareStateTime(0, 6, 3, 6)
    CompareEventFlag(0, 537020174, 1)
    assert ConditionGroup(0)
    """State 6: Boss BGM playback"""
    PlaySoundAtPoint(z34)
    """State 21: End state"""
    return 0

def event_m50_37_x140():
    """[Condition] Ice King Battle Phase 2"""
    """State 0,1: Judgment condition of boss appearance"""
    CompareActiveChrNum(0, 12, 13, 14, 0, 0, 0, 0)
    CompareEventFlag(0, 537020173, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x141(z34=501, z35=5037000, z36=537020085, mode2=0):
    """[Execution] Ice King Battle Phase 3
    z34: Sound ID
    z35: Boss Battle ID
    z36: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,8: Phase clear flag ON"""
    SetEventFlag(537020175, 1)
    """State 11: Remaining black knight death process"""
    EnemyActionRequest(4100, 1)
    EnemyActionRequest(4101, 1)
    EnemyActionRequest(4102, 1)
    EnemyActionRequest(4110, 1)
    EnemyActionRequest(4111, 1)
    EnemyActionRequest(4112, 1)
    EnemyActionRequest(4113, 1)
    EnemyActionRequest(4114, 1)
    EnemyActionRequest(4115, 1)
    EnemyActionRequest(4116, 1)
    EnemyActionRequest(4117, 1)
    EnemyActionRequest(4118, 1)
    EnemyActionRequest(4119, 1)
    EnemyActionRequest(4120, 1)
    EnemyActionRequest(4121, 1)
    """State 7: Timer stop"""
    EndAreaTimer(0)
    EndAreaTimer(0)
    """State 1: Logic flag OFF"""
    SetEventFlag(z36, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z35)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z34)
    """State 6: Atmosphere sound stop"""
    StopSoundAtPoint(30000)
    """State 10: Waiting for boss to disappear"""
    IsChrActive(0, 908, 0)
    assert ConditionGroup(0)
    """State 9: The fire of the gate OBJ is extinguished: 20"""
    ChangeObjState(50371560, 20)
    """State 5: Remaining Black Knight's Death Process: Safety"""
    EnemyActionRequest(4100, 1)
    EnemyActionRequest(4101, 1)
    EnemyActionRequest(4102, 1)
    EnemyActionRequest(4110, 1)
    EnemyActionRequest(4111, 1)
    EnemyActionRequest(4112, 1)
    EnemyActionRequest(4113, 1)
    EnemyActionRequest(4114, 1)
    EnemyActionRequest(4115, 1)
    EnemyActionRequest(4116, 1)
    EnemyActionRequest(4117, 1)
    EnemyActionRequest(4118, 1)
    EnemyActionRequest(4119, 1)
    EnemyActionRequest(4120, 1)
    EnemyActionRequest(4121, 1)
    """State 12: End state"""
    return 0

def event_m50_37_x142(z33=537000086, z34=501, z35=5037000, z36=537020085):
    """[Preset] Ice King
    z33: Boss destruction flag
    z34: Sound ID
    z35: Boss Battle ID
    z36: Other flags for logic
    """
    """State 0,5: [Reproduction] Ice King Battle_Start_SubState"""
    call = event_m50_37_x134(z33=z33)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 15: [Condition] Ice King Battle_Start_SubState"""
        assert event_m50_37_x135()
        """State 10: [Execution] Ice King Battle_Start_SubState"""
        assert event_m50_37_x136(z35=z35)
        """State 1: [Reproduction] Ice King Battle_Phase 1_Sky_SubState"""
        assert event_m50_37_x274()
        """State 11: [Condition] Ice King Battle_Phase 1_SubState"""
        assert event_m50_37_x275()
        """State 6: [Execution] Ice King Battle_Phase 1_SubState"""
        assert event_m50_37_x276(z36=z36)
        """State 4: [Reproduction] Ice King Battle_Rush_Sky_SubState"""
        assert event_m50_37_x344()
        """State 14: [Condition] Ice King Battle_Rush_SubState"""
        assert event_m50_37_x345()
        """State 9: [Execution] Ice King_Rush_SubState"""
        assert event_m50_37_x346()
        """State 2: [Reproduction] Ice King Battle_Phase 2_SubState"""
        assert event_m50_37_x137()
        """State 12: [Condition] Ice King Battle_Phase 2_SubState"""
        assert event_m50_37_x140()
        """State 7: [Execution] Ice King Battle_Phase 2_SubState"""
        assert event_m50_37_x139(z34=z34, z35=z35, z36=z36)
        """State 3: [Reproduction] Ice King Battle_Phase 3_SubState"""
        assert event_m50_37_x199()
        """State 13: [Condition] Ice King Battle_Phase 3_SubState"""
        assert event_m50_37_x138(z35=z35)
        """State 8: [Execution] Ice King Battle_Phase 3_SubState"""
        assert event_m50_37_x141(z34=z34, z35=z35, z36=z36, mode2=0)
    """State 16: End state"""
    return 0

def event_m50_37_x143(z196=537000012, z197=537010013, z199=537000081):
    """[Reproduction] Transparent management of tigers
    z196: Miko's eyes: possession flag
    z197: Transparency control flag
    z199: Defeat flag
    """
    """State 0,3: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 7: The guests"""
    return 2
    """State 1: Is the tiger already destroyed?"""
    Label('L0')
    if GetEventFlag(z199) != 0:
        pass
    else:
        Goto('L1')
    """State 8: Defeated"""
    return 3
    """State 2: Do you have a shrine maiden eye?"""
    Label('L1')
    if GetEventFlag(z196) != 0:
        """State 6: Possessing a shrine maiden's eyes"""
        return 1
    else:
        """State 4: Transparent control flag ON"""
        SetEventFlag(z197, 1)
        """State 5: Transparency control"""
        return 0

def event_m50_37_x144(z198=907, z199=537000081, z200=537020080, z196=537000012):
    """[Condition] Transparent management of tigers
    z198: Generator ID
    z199: Defeat flag
    z200: Battle start flag
    z196: Miko's eyes: possession flag
    """
    """State 0,1: Battle start or shrine maiden possession or destruction determination"""
    CompareChrEzStateValue(0, z198, 7, 1, 0)
    CompareEventFlag(0, z200, 1)
    CompareEventFlag(1, z199, 1)
    CompareEventFlag(1, z196, 1)
    if ConditionGroup(1):
        """State 3: Rerun"""
        return 1
    elif ConditionGroup(0):
        """State 2: Transparency control"""
        return 0

def event_m50_37_x145(z196=537000012, z197=537010013, z198=907, z199=537000081):
    """[Execution] Transparent management of tigers
    z196: Miko's eyes: possession flag
    z197: Transparency control flag
    z198: Generator ID
    z199: Defeat flag
    """
    """State 0,1: Random timer or shrine maiden possession or destruction determination"""
    CompareStateTime(0, 15, 3, 25)
    CompareEventFlag(1, z199, 1)
    CompareEventFlag(1, z196, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Transparent control flag OFF"""
        SetEventFlag(z197, 0)
        """State 4: Random timer or shrine maiden eye possession or destruction determination_2"""
        CompareStateTime(0, 1, 3, 3)
        CompareEventFlag(1, z199, 1)
        CompareEventFlag(1, z196, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 2: Transparent control flag ON"""
            SetEventFlag(z197, 1)
    """State 5: End state"""
    return 0

def event_m50_37_x146(z196=537000012, z197=537010013, z198=907, z199=537000081, z200=537020080):
    """[Preset] Transparent management of tigers
    z196: Miko's eyes: possession flag
    z197: Transparency control flag
    z198: Generator ID
    z199: Defeat flag
    z200: Battle start flag
    """
    """State 0,1: [Reproduction] Transparency management of tigers_SubState"""
    call = event_m50_37_x143(z196=z196, z197=z197, z199=z199)
    if call.Get() == 2:
        pass
    elif call.Get() == 3:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 4: Finish"""
    return 0
    """State 3: [Condition] Transparent management of tigers_SubState"""
    Label('L0')
    call = event_m50_37_x144(z198=z198, z199=z199, z200=z200, z196=z196)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Transparent management of tigers_SubState"""
        assert event_m50_37_x145(z196=z196, z197=z197, z198=z198, z199=z199)
    """State 5: Rerun"""
    return 1

def event_m50_37_x147(z189=537000012, z190=537010013, z191=907, z192=96790010, z193=96790000, z194=96790020):
    """[Preset] Transparent tiger
    z189: Miko's eyes: possession flag
    z190: Transparency control flag
    z191: Generator ID
    z192: Transparent special effect ID
    z193: Translucent special effect ID
    z194: Normal special effect ID
    """
    """State 0,1: [Reproduction] Transparency of tigers_SubState"""
    assert event_m50_37_x148()
    """State 4: [Condition] Tiger transparency_SubState"""
    call = event_m50_37_x149(z189=z189, z190=z190)
    if call.Get() == 2:
        """State 3: [Execution] Transparency of tiger_Release_SubState"""
        assert event_m50_37_x151(z191=z191, z192=z192, z193=z193, z194=z194)
        """State 6: Finish"""
        return 0
    elif call.Get() == 0:
        """State 5: [Execution] Transparency of tigers_Translucent_SubState"""
        assert event_m50_37_x150(z191=z191, z192=z193, z189=z189, z190=z190, z195=1, z193=z192)
    elif call.Get() == 1:
        """State 2: [Execution] Transparency of tigers_Transparent_SubState"""
        assert event_m50_37_x150(z191=z191, z192=z192, z189=z189, z190=z190, z195=0, z193=z193)
    """State 7: Rerun"""
    return 1

def event_m50_37_x148():
    """[Reproduction] Transparency of tiger"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x149(z189=537000012, z190=537010013):
    """[Condition] Transparency of tiger
    z189: Miko's eyes: possession flag
    z190: Transparency control flag
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z190, 1)
    CompareEventFlag(1, z190, 0)
    CompareEventFlag(2, z189, 1)
    if ConditionGroup(2):
        """State 4: The possession of a shrine maiden"""
        return 2
    elif ConditionGroup(1):
        """State 2: Translucent"""
        return 0
    elif ConditionGroup(0):
        """State 3: Transparency"""
        return 1

def event_m50_37_x150(z191=907, z192=_, z189=537000012, z190=537010013, z195=_, z193=_):
    """[Execution] Transparency of tigers
    z191: Generator ID
    z192: Grant special effect ID
    z189: Miko's eyes: possession flag
    z190: Transparency control flag
    z195: Control flag judgment
    z193: Cancel special effect ID
    """
    """State 0,3: Cancel special effects"""
    ClearEnemySpEffect(z191, z192)
    ClearEnemySpEffect(z191, z193)
    assert (GetStateTime() >= 0) != 0
    """State 1: Giving special effects to tigers"""
    SetEnemySpEffect(z191, z192, 10, 4)
    """State 2: Flag judgment"""
    CompareEventFlag(0, z190, z195)
    CompareEventFlag(0, z189, 1)
    assert ConditionGroup(0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x151(z191=907, z192=96790010, z193=96790000, z194=96790020):
    """[Execution] Make tiger transparent
    z191: Generator ID
    z192: Transparent special effect ID
    z193: Translucent special effect ID
    z194: Normal special effect ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z191, z192)
    ClearEnemySpEffect(z191, z193)
    assert (GetStateTime() >= 0) != 0
    """State 2: Giving special effects to tigers"""
    SetEnemySpEffect(z191, z194, 10, 4)
    """State 3: Finish"""
    return 0

def event_m50_37_x152(z179=537000081):
    """[Reproduction] Tiger Battle_Start
    z179: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z179) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_37_x153(z185=2500000, z188=2500000):
    """[Condition] Tiger Battle_Start
    z185: Start point ID
    z188: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z185, z188, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z185, z188, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x154(z181=5037030):
    """[Execution] Tiger Battle_Start
    z181: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z181)
    """State 2: End state"""
    return 0

def event_m50_37_x155():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x156(z187=907, z182=537020080):
    """[Condition] HP display, BGM playback and boss activation
    z187: Boss generator ID
    z182: Logic flag
    """
    """State 0,1: Damaged or point intrusion or activated"""
    CompareChrHpRatio(0, z187, 100, 4)
    IsPlayerInsidePoint(0, 2500010, 2500010, 1)
    CompareEventFlag(0, z182, 1)
    CompareChrEzStateValue(0, z187, 7, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x157(z180=504, z182=537020080, z183=5, z181=5037030, z184=537020083, z186=907):
    """[Execution] HP display, BGM playback and boss activation
    z180: Sound ID
    z182: Logic flag
    z183: Wait time until display
    z181: Boss Battle ID
    z184: BGM and gauge display flag
    z186: Boss generator ID
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z182, 1)
    """State 4: Wait until BGM playback and HP display"""
    CompareStateTime(0, z183, 2, z183)
    CompareEventFlag(0, z184, 1)
    CompareChrEzStateValue(0, z186, 7, 1, 0)
    IsEventBossKill(1, z181, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z180)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 6: Camera parameter switching"""
    ChangeCameraParameters(679100, 3, 3)
    """State 5: BGM and gauge display flag ON"""
    SetEventFlag(z184, 1)
    """State 7: End state"""
    return 0

def event_m50_37_x158():
    """[Reproduction] Tiger Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x159(z181=5037030):
    """[Condition] Tora Battle_End Judgment
    z181: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z181, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x160(z180=504, z181=5037030, z182=537020080):
    """[Execution] Tiger Battle_End
    z180: Sound ID
    z181: Boss Battle ID
    z182: Other flags for logic
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z182, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z181)
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z180)
    assert (GetStateTime() > 6.5) != 0
    """State 4: Return camera parameters"""
    ResetCameraParameters()
    """State 5: End state"""
    return 0

def event_m50_37_x161(z179=537000081, z180=504, z181=5037030, z182=537020080, z183=5, z184=537020083,
                      z185=2500000):
    """[Preset] Tiger Battle_Start
    z179: Boss destruction flag
    z180: Sound ID
    z181: Boss Battle ID
    z182: Other flags for logic
    z183: Wait time
    z184: BGM and gauge display flag
    z185: Point ID
    """
    """State 0,1: [Reproduction] Tiger Battle_Start_SubState"""
    call = event_m50_37_x152(z179=z179)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Tiger Battle_Start_SubState"""
        assert event_m50_37_x153(z185=z185, z188=z185)
        """State 3: [Execution] Tiger Battle_Start_SubState"""
        assert event_m50_37_x154(z181=z181)
        """State 7: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
        assert event_m50_37_x155()
        """State 9: [Condition] HP display, BGM playback and boss activation_SubState"""
        assert event_m50_37_x156(z187=907, z182=z182)
        """State 8: [Execution] HP display, BGM playback and boss activation_SubState"""
        assert event_m50_37_x157(z180=z180, z182=z182, z183=z183, z181=z181, z184=z184, z186=907)
        """State 2: [Reproduction] Tiger Battle_End_Sky_SubState"""
        assert event_m50_37_x158()
        """State 6: [Condition] Tiger Battle_End Judgment_SubState"""
        assert event_m50_37_x159(z181=z181)
        """State 4: [Execution] Tiger Battle_End_SubState"""
        assert event_m50_37_x160(z180=z180, z181=z181, z182=z182)
    """State 10: End state"""
    return 0

def event_m50_37_x162(z177=537010014, z178=537020015):
    """[Execution] Snowstorm management in the snowfield area
    z177: Snowstorm control flag
    z178: Enemy appearance flag
    """
    """State 0,1: Snowstorm control flag ON"""
    SetEventFlag(z177, 1)
    """State 5: Waiting for enemy appearance"""
    CompareStateTime(0, 3, 3, 3)
    assert ConditionGroup(0)
    """State 6: Enemy appearance flag ON"""
    SetEventFlag(z178, 1)
    """State 2: Has time passed?"""
    CompareStateTime(0, 22, 3, 27)
    assert ConditionGroup(0)
    """State 3: Snowstorm control flag OFF"""
    SetEventFlag(z177, 0)
    """State 7: Enemy appearance flag OFF"""
    SetEventFlag(z178, 0)
    """State 4: Has time passed? _2"""
    CompareStateTime(0, 15, 3, 24)
    assert ConditionGroup(0)
    """State 8: Rerun"""
    return 0

def event_m50_37_x163(z177=537010014):
    """[Reproduction] Snowstorm management in the snowy field area
    z177: Snowstorm control flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: Snowstorm control"""
        return 0

def event_m50_37_x164():
    """[Condition] Snowstorm management in the snowfield area"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x165(z177=537010014, z178=537020015):
    """[Preset] Snowstorm management in the snowfield area
    z177: Snowstorm control flag
    z178: Enemy appearance flag
    """
    """State 0,1: [Reproduction] Snowstorm management in the snowy field_SubState"""
    call = event_m50_37_x163(z177=z177)
    if call.Get() == 1:
        """State 5: Finish"""
        return 1
    elif call.Get() == 0:
        """State 3: [Condition] Snowstorm management in the snowfield area_SubState"""
        assert event_m50_37_x164()
        """State 2: [Execution] Snowstorm management in the snowfield area_SubState"""
        assert event_m50_37_x162(z177=z177, z178=z178)
        """State 4: Rerun"""
        return 0

def event_m50_37_x166():
    """[Reproduction] Enemy that appears in snowstorm"""
    """State 0,1: Is it a hostile spirit?"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        """State 3: Hostile spirit: no reaction"""
        return 1
    else:
        """State 2: End state"""
        return 0

def event_m50_37_x167(z167=_, z171=_, z172=_, z176=537020015, z173=_, z174=_):
    """[Condition] Enemy appearing in a snowstorm
    z167: Generator ID
    z171: Defeat count
    z172: Maximum number of generations
    z176: Enemy appearance flag
    z173: Generateable_start point ID
    z174: Generateable_end point ID
    """
    """State 0,1: Generation determination"""
    CompareEventFlag(8, z176, 1)
    IsChrActive(8, z167, 0)
    IsPlayerInsidePoint(8, 600080, 600099, 0)
    IsPlayerInsidePoint(8, z173, z174, 1)
    IsPlayerOnHitGroup(8, 30, 1)
    CompareEventFlagValue(1, 1, z171, z172, 3)
    if ConditionGroup(1):
        """State 3: Maximum number: End"""
        return 1
    elif ConditionGroup(8):
        """State 2: End state"""
        return 0

def event_m50_37_x168(z167=_, z168=_, z169=_, z175=1, z170=_, z171=_, z172=_):
    """[Execution] Enemy that appears in a snowstorm
    z167: Generator ID
    z168: Generation start point ID
    z169: Generation end point ID
    z175: Generation distance order
    z170: Next generation weight
    z171: Defeat count
    z172: Maximum number of generations
    """
    """State 0,1: Enemy generation"""
    ForceGenerationFromPointBasedOnPositionAndCameraOfAllUsers(z167, z168, z169, 20, 50, 1, z175, 1)
    assert (GetStateTime() > 1) != 0
    """State 2: Death determination or upper limit number determination"""
    IsChrDead(0, z167)
    CompareEventFlagValue(1, 1, z171, z172, 3)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Next generation wait or upper limit number judgment"""
        CompareStateTime(0, z170, 3, z170)
        CompareEventFlagValue(1, 1, z171, z172, 3)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 4: Rerun"""
            return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x169(z167=_, z168=_, z169=_, z170=_, z171=_, z172=_, z173=_, z174=_):
    """[Preset] Enemy that appears in snowstorm
    z167: Generator ID
    z168: Generation start point ID
    z169: Generation end point ID
    z170: Next generation weight
    z171: Defeat count
    z172: Maximum number of generations
    z173: Generateable_start point ID
    z174: Generateable_end point ID
    """
    """State 0,1: [Reproduction] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x166()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Enemy _SubState appearing in snowstorm"""
        call = event_m50_37_x167(z167=z167, z171=z171, z172=z172, z176=537020015, z173=z173, z174=z174)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Enemy _SubState that appears in a snowstorm"""
            call = event_m50_37_x168(z167=z167, z168=z168, z169=z169, z175=1, z170=z170, z171=z171, z172=z172)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                """State 4: Rerun"""
                return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x170(z163=_, z164=_, z165=_, z166=_):
    """[Condition] Enemy moving by absorbing soul
    z163: Generator ID
    z164: Absorption distance
    z165: Absorption flag
    z166: Absorption OBJ instance ID
    """
    """State 0,3: Is the ice already broken?"""
    CompareEventFlag(0, 537000011, 1)
    assert ConditionGroup(0)
    """State 4: Seoul absorption processing: ON"""
    AddSoulAcquisitionTarget(z166, z164, z165, 1, -1)
    """State 1: Absorption or character determination"""
    CompareEventFlag(0, z165, 1)
    IsChrDeadOrRespawnOver(1, z163, 1)
    if ConditionGroup(1):
        """State 2: Seoul absorption processing: OFF"""
        AddSoulAcquisitionTarget(z166, z164, z165, 0, 220)
        """State 5: Absorption OBJ hidden: 20"""
        ChangeObjState(z166, 20)
        """State 7: Absorption character death"""
        return 1
    elif ConditionGroup(0):
        """State 6: Absorption completed"""
        return 0

def event_m50_37_x171(z165=_, z166=_):
    """[Reproduction] Enemy moving by absorbing soul
    z165: Absorption flag
    z166: Absorption OBJ instance ID
    """
    """State 0,1: Already absorbed?"""
    if GetEventFlag(z165) != 0:
        """State 2: Absorption OBJ hidden: 20"""
        ChangeObjState(z166, 20)
        """State 4: Absorbed"""
        return 1
    else:
        """State 3: Not absorbed"""
        return 0

def event_m50_37_x172(z166=_):
    """[Execution] Enemy moving by absorbing soul
    z166: Absorption OBJ instance ID
    """
    """State 0,1,2: Absorption OBJ hidden: 20"""
    ChangeObjState(z166, 20)
    """State 3: End state"""
    return 0

def event_m50_37_x173(z163=_, z164=_, z165=_, z166=_):
    """[Preset] Enemy who moves by absorbing soul
    z163: Generator ID
    z164: Absorption distance
    z165: Absorption flag
    z166: Absorption OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemy _SubState moving by absorbing soul"""
    call = event_m50_37_x171(z165=z165, z166=z166)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Enemy _SubState moving by absorbing Seoul"""
        call = event_m50_37_x170(z163=z163, z164=z164, z165=z165, z166=z166)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Enemies that move by absorbing souls_SubState"""
            assert event_m50_37_x172(z166=z166)
    """State 4: End state"""
    return 0

def event_m50_37_x174(z162=537000006):
    """[Reproduction] Rejection effect by ice
    z162: Event completion flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been executed?"""
        if GetEventFlag(z162) != 0:
            pass
        else:
            """State 3: Not executed"""
            return 0
    """State 4: Finish"""
    return 1

def event_m50_37_x175(z159=1600000):
    """[Condition] Rejection effect by ice
    z159: Point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(8, z159, z159, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x176(z158=537020016, z160=50371251, z161=50371252, z162=537000006):
    """[Execution] Rejection by ice
    z158: Conversation flag
    z160: Door OBJ instance ID
    z161: Vine: Ice OBJ instance ID
    z162: Event completion flag
    """
    """State 0,2: Cold threat from the door: 70"""
    ChangeObjState(z160, 70)
    assert (GetStateTime() > 2) != 0
    """State 3: Vine ice appears: 70"""
    ChangeObjState(z161, 70)
    assert (GetStateTime() > 0.5) != 0
    """State 1: Conversation flag ON"""
    SetEventFlag(z158, 1)
    """State 4: Event completion flag ON"""
    SetEventFlag(z162, 1)
    """State 5: End state"""
    return 0

def event_m50_37_x177(z158=537020016, z159=1600000, z160=50371251, z161=50371252, z162=537000006):
    """[Preset] Rejection effect by ice
    z158: Conversation flag
    z159: Point ID
    z160: Door OBJ instance ID
    z161: Vine: Ice OBJ instance ID
    z162: Event completion flag
    """
    """State 0,1: [Reproduction] Rejection effect by ice_SubState"""
    call = event_m50_37_x174(z162=z162)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Rejection effect by ice_SubState"""
        assert event_m50_37_x175(z159=z159)
        """State 2: [Execution] Rejection with ice_SubState"""
        assert event_m50_37_x176(z158=z158, z160=z160, z161=z161, z162=z162)
    """State 4: End state"""
    return 0

def event_m50_37_x178(z157=1400000, z156=50371021, z155=50371020):
    """[Reproduction] Snowball Gorokuro
    z157: Navigation change point ID
    z156: Big Snowball OBJ Instance ID
    z155: Mini Snowball OBJ instance ID
    """
    """State 0,2: Has a big snowball already displayed?"""
    if CompareObjStateId(z156, 20, 0):
        pass
    else:
        """State 4: Mini snowball status judgment"""
        if CompareObjStateId(z155, 10, 1):
            """State 5: Waiting for a mini snowball to roll"""
            if CompareObjStateId(z155, 72, 0):
                pass
            elif CompareObjStateId(z155, 21, 0):
                pass
            """State 6: Deca snowball display: 20"""
            ChangeObjState(z156, 20)
        else:
            """State 1: Navigation switching: Not allowed"""
            AddNavimeshAttribute(z157, 2)
            """State 7: Waiting for rolling"""
            return 0
    """State 3: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z157, 2)
    """State 8: Finish"""
    return 1

def event_m50_37_x179(z155=50371020):
    """[Conditions] Snowball Gorokuro
    z155: Mini Snowball OBJ instance ID
    """
    """State 0,1: Snowball damage judgment"""
    IsObjDamaged(0, z155, -1, -4, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x180(z155=50371020, z156=50371021, z157=1400000):
    """[Execution] Snowball Gorokuro
    z155: Mini Snowball OBJ instance ID
    z156: Big Snowball OBJ Instance ID
    z157: Navigation change point ID
    """
    """State 0,3: Starting rolling mini snowballs: 70"""
    ChangeObjState(z155, 70)
    """State 4: Waiting for rolling"""
    CompareObjState(0, z155, 72, 0)
    assert ConditionGroup(0)
    """State 1: Deca snowball display"""
    ChangeObjState(z156, 20)
    """State 2: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z157, 2)
    """State 5: End state"""
    return 0

def event_m50_37_x181(z155=50371020, z156=50371021, z157=1400000):
    """[Preset] Snowball Gorokuro
    z155: Mini Snowball OBJ instance ID
    z156: Big Snowball OBJ Instance ID
    z157: Navigation change point ID
    """
    """State 0,2: [Reproduction] Snowball Gorokuro_SubState"""
    call = event_m50_37_x178(z157=z157, z156=z156, z155=z155)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Snowball Gorokuro_SubState"""
        assert event_m50_37_x179(z155=z155)
        """State 3: [Execution] Snowball Gorokuro_SubState"""
        assert event_m50_37_x180(z155=z155, z156=z156, z157=z157)
    """State 5: End state"""
    return 0

def event_m50_37_x182(z2=537000012, z5=17000):
    """[Reproduction] Obtaining the eyes of a shrine maiden
    z2: Miko eyes possession flag
    z5: Event SFXID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Already acquired?"""
        if GetEventFlag(z2) != 1:
            """State 3: Generation of SFX"""
            PlaySfxAtPoint(z5)
            """State 5: Unacquired"""
            return 0
        else:
            pass
    else:
        pass
    """State 4: Stop SFX"""
    StopSfxAtPoint(z5)
    """State 6: Finish"""
    return 1

def event_m50_37_x183(z3=50376550):
    """[Conditions] Acquire Miko's eyes
    z3: Miko eyes OBJ instance ID
    """
    """State 0,1: Got Miko's eyes? Are you in the snowy field?"""
    WasObjItemAcquired(0, z3, 1)
    IsPlayerOnHitGroup(1, 30, 1)
    if ConditionGroup(0):
        """State 2: Miko's eyes get"""
        return 0
    elif ConditionGroup(1):
        """State 3: In the snowy field"""
        return 1

def event_m50_37_x184(z2=537000012, z4=17000, z5=17000):
    """[Execution] Acquire the eyes of a shrine maiden
    z2: Miko eyes possession flag
    z4: Event sound ID
    z5: Event SFXID
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(z2, 1)
    """State 2: Atmosphere SE regeneration"""
    PlaySoundAtPoint(z4)
    """State 3: Stop SFX"""
    StopSfxAtPoint(z5)
    """State 4: End state"""
    return 0

def event_m50_37_x185(z2=537000012, z3=50376550, z4=17000, z5=17000):
    """[Preset] Acquire Miko's eyes
    z2: Miko eyes possession flag
    z3: Miko eyes OBJ instance ID
    z4: Event sound ID
    z5: Event SFXID
    """
    """State 0,1: [Reproduction] _SubState to get Miko's eyes"""
    call = event_m50_37_x182(z2=z2, z5=z5)
    if call.Get() == 0:
        """State 3: [Condition] _SubState to get Miko's eyes"""
        call = event_m50_37_x183(z3=z3)
        if call.Get() == 0:
            """State 2: [Execution] _SubState to get the eyes of the shrine maiden"""
            assert event_m50_37_x184(z2=z2, z4=z4, z5=z5)
        elif call.Get() == 1:
            """State 4: [DC] [Execution] Yukihara_SubState to get Miko's eyes"""
            assert event_m50_37_x387(z5=z5)
    elif call.Get() == 1:
        pass
    """State 5: End state"""
    return 0

def event_m50_37_x186(z148=537000012, z149=_):
    """[Reproduction] Zako's transparency management
    z148: Miko's eyes: possession flag
    z149: Transparency control flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 6: The guests"""
    return 2
    """State 1: Do you have a shrine maiden eye?"""
    Label('L0')
    if GetEventFlag(z148) != 0:
        """State 5: Possessing a shrine maiden's eyes"""
        return 1
    else:
        """State 3: Transparent control flag ON"""
        SetEventFlag(z149, 1)
        """State 4: Transparency control"""
        return 0

def event_m50_37_x187():
    """[Condition] Zako's transparency management_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x188(z148=537000012, z149=_, z150=_, z151=_, z152=_, z153=_, z154=_):
    """[Execution] Transparent management of Zako
    z148: Miko's eyes: possession flag
    z149: Transparency control flag
    z150: Generator ID
    z151: Minimum time to turn off
    z152: Maximum time to OFF
    z153: Minimum time to ON
    z154: Maximum time to ON
    """
    """State 0,1: Random timer or shrine maiden possession or destruction determination"""
    CompareStateTime(0, z151, 3, z152)
    IsChrDeadOrRespawnOver(1, z150, 1)
    CompareEventFlag(1, z148, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Transparent control flag OFF"""
        SetEventFlag(z149, 0)
        """State 4: Random timer or shrine maiden eye possession or destruction determination_2"""
        CompareStateTime(0, z153, 3, z154)
        IsChrDeadOrRespawnOver(1, z150, 1)
        CompareEventFlag(1, z148, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 2: Transparent control flag ON"""
            SetEventFlag(z149, 1)
            """State 6: Rerun"""
            return 1
    """State 5: Finish"""
    return 0

def event_m50_37_x189(z148=537000012, z149=_, z150=_, z151=_, z152=_, z153=_, z154=_):
    """[Preset] Zako's transparency management
    z148: Miko's eyes: possession flag
    z149: Transparency control flag
    z150: Generator ID
    z151: Minimum time to turn off
    z152: Maximum time to OFF
    z153: Minimum time to ON
    z154: Time until ON
    """
    """State 0,1: [Reproduction] Zako's transparency management_SubState"""
    call = event_m50_37_x186(z148=z148, z149=z149)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Zako's transparency management_empty_SubState"""
        assert event_m50_37_x187()
        """State 2: [Execution] Zako's transparency management_SubState"""
        call = event_m50_37_x188(z148=z148, z149=z149, z150=z150, z151=z151, z152=z152, z153=z153, z154=z154)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 5: Rerun"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_37_x190():
    """[Reproduction] Transparency of Zako"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x191(z142=537000012, z143=_):
    """[Condition] Transparency of Zako
    z142: Miko's eyes: possession flag
    z143: Transparency control flag
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z143, 1)
    CompareEventFlag(1, z143, 0)
    CompareEventFlag(2, z142, 1)
    if ConditionGroup(2):
        """State 4: The possession of a shrine maiden"""
        return 2
    elif ConditionGroup(1):
        """State 2: Translucent"""
        return 0
    elif ConditionGroup(0):
        """State 3: Transparency"""
        return 1

def event_m50_37_x192(z144=_, z145=_, z142=537000012, z143=_, z147=_, z146=_):
    """[Execution] Transparency of Zako
    z144: Generator ID
    z145: Grant special effect ID
    z142: Miko's eyes: possession flag
    z143: Transparency control flag
    z147: Control flag judgment
    z146: Cancel special effect ID
    """
    """State 0,3: Cancel special effects"""
    ClearEnemySpEffect(z144, z145)
    ClearEnemySpEffect(z144, z146)
    assert (GetStateTime() >= 0) != 0
    """State 1: Giving Zako a special effect"""
    SetEnemySpEffect(z144, z145, 10, 4)
    """State 2: Flag judgment"""
    CompareEventFlag(0, z143, z147)
    CompareEventFlag(0, z142, 1)
    assert ConditionGroup(0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x193(z144=_, z145=98830010, z146=98830000):
    """[Execution] Zako's transparency_release
    z144: Generator ID
    z145: Transparent special effect ID
    z146: Translucent special effect ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z144, z145)
    ClearEnemySpEffect(z144, z146)
    """State 2: Finish"""
    return 0

def event_m50_37_x194(z142=537000012, z143=_, z144=_, z145=98830010, z146=98830000):
    """[Preset] Transparency of Zako
    z142: Miko's eyes: possession flag
    z143: Transparency control flag
    z144: Generator ID
    z145: Transparent special effect ID
    z146: Translucent special effect ID
    """
    """State 0,1: [Reproduction] Transparency of Zako_SubState"""
    assert event_m50_37_x190()
    """State 4: [Condition] Zako's transparency_SubState"""
    call = event_m50_37_x191(z142=z142, z143=z143)
    if call.Get() == 2:
        """State 3: [Execution] Zako's transparency_Release_SubState"""
        assert event_m50_37_x193(z144=z144, z145=z145, z146=z146)
        """State 6: Finish"""
        return 0
    elif call.Get() == 0:
        """State 5: [Execution] Zako's transparency_Translucent_SubState"""
        assert event_m50_37_x192(z144=z144, z145=z146, z142=z142, z143=z143, z147=1, z146=z145)
    elif call.Get() == 1:
        """State 2: [Execution] Zako's transparency_Transparency_SubState"""
        assert event_m50_37_x192(z144=z144, z145=z145, z142=z142, z143=z143, z147=0, z146=z146)
    """State 7: Rerun"""
    return 1

def event_m50_37_x195(z140=537000086):
    """[Reproduction] Black Knight: Defeat count
    z140: Defeat count variable
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the boss been destroyed?"""
        if GetEventFlag(z140) != 0:
            pass
        else:
            """State 3: End state"""
            return 0
    """State 4: Do nothing: Quit"""
    return 1

def event_m50_37_x196(z138=_, z141=0):
    """[Condition] Black Knight: Defeat count
    z138: Generator ID
    z141: Boss destruction flag
    """
    """State 0,1: Wait for character destruction or wait for boss destruction"""
    IsChrDead(0, z138)
    CompareEventFlag(1, z141, 1)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Variable addition"""
        return 0

def event_m50_37_x197(z138=_, z139=1):
    """[Execution] Black Knight: Defeat count
    z138: Generator ID
    z139: Defeat count variable
    """
    """State 0,1: [Condition] Ice King Battle_Start_SubState"""
    AddAreaVariable(z139, 1)
    """State 2: Wait for generator to restart"""
    IsChrActive(0, z138, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x198(z138=_, z139=1, z140=537000086):
    """[Preset] Black Knight: Defeat count
    z138: Generator ID
    z139: Defeat count variable
    z140: Boss destruction flag
    """
    """State 0,1: [Reproduction] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x195(z140=z140)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Black Knight: Defeat Count Count_SubState"""
        call = event_m50_37_x196(z138=z138, z141=0)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Black Knight: Defeat count _SubState"""
            assert event_m50_37_x197(z138=z138, z139=z139)
            """State 4: Rerun"""
            return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x199():
    """[Reproduction] Ice King Battle Phase 3"""
    """State 0,1: Phase 3 flag ON"""
    SetEventFlag(537020174, 1)
    """State 2: Start phase 3 start timer"""
    StartAreaTimer(0)
    """State 3: End state"""
    return 0

def event_m50_37_x200():
    """[Reproduction] Black Knight: Defeat count reset"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m50_37_x201():
    """[Condition] Black knight: Defeat count reset_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x202():
    """[Execution] Black Knight: Defeat count reset"""
    """State 0,1: Initializing area variables"""
    SetAreaVariable(1, 0)
    SetAreaVariable(2, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x203():
    """[Preset] Black Knight: Defeat count reset"""
    """State 0,1: [Reproduction] Black knight: Defeat count reset_SubState"""
    call = event_m50_37_x200()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Black knight: Defeat count reset_sky_SubState"""
        assert event_m50_37_x201()
        """State 2: [Execute] Black Knight: Defeat count reset_SubState"""
        assert event_m50_37_x202()
    """State 4: End state"""
    return 0

def event_m50_37_x204(z134=_, z135=_, z136=_, z137=5):
    """[Preset] Gate opened by lever
    z134: Lever OBJ instance ID
    z135: Gate OBJ instance ID
    z136: Navigation change point ID
    z137: Wait until navigation switching
    """
    """State 0,1: [Reproduction] Gate_SubState opened with lever"""
    call = event_m50_37_x205(z135=z135, z136=z136)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Gate_SubState opened with lever"""
        assert event_m50_37_x206(z134=z134)
        """State 2: [Execution] Gate opened with lever _SubState"""
        assert event_m50_37_x207(z135=z135, z136=z136, z137=z137)
    """State 4: End state"""
    return 0

def event_m50_37_x205(z135=_, z136=_):
    """[Reproduction] Gate opened with lever
    z135: Gate OBJ instance ID
    z136: Navigation change point ID
    """
    """State 0,1: Is the gate open?"""
    if CompareObjStateId(z135, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z135, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z136, 2)
        """State 6: Already in operation"""
        return 1
    else:
        """State 4: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z136, 2)
        """State 5: Not in operation"""
        return 0

def event_m50_37_x206(z134=_):
    """[Condition] Gate opened by lever
    z134: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z134, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x207(z135=_, z136=_, z137=5):
    """[Execution] Gate opened by lever
    z135: Gate OBJ instance ID
    z136: Navigation change point ID
    z137: Wait until navigation switching
    """
    """State 0,2: Gate opens: 70"""
    ChangeObjState(z135, 70)
    """State 4: weight"""
    CompareStateTime(0, z137, 3, z137)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z136, 2)
    """State 3: Waiting for the opening of the iron lattice"""
    CompareObjState(0, z135, 20, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m50_37_x208(z132=50371001):
    """[Execution] Return from boss room_OBJ appearance
    z132: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ has appeared: 30"""
    ChangeObjState(z132, 30)
    """State 2: Rerun"""
    return 0

def event_m50_37_x209(z38=_):
    """[Condition] Return from the boss room
    z38: Warp OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z38)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x210(z15=_):
    """[Reproduction] Black Knight: Generator
    z15: Sealed flag
    """
    """State 0,4: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 9: The guests"""
    return 3
    """State 2: Did you clear it?"""
    Label('L0')
    if GetEventFlag(537020175) != 0:
        pass
    else:
        """State 1: Is the generator sealed?"""
        if GetEventFlag(z15) != 0:
            pass
        else:
            """State 5: Is it in game?"""
            assert InGame() != 0
            """State 3: Has the boss been destroyed?"""
            if GetEventFlag(537000086) != 0:
                """State 8: After destroying the boss"""
                return 2
            else:
                """State 6: In operation"""
                return 0
    """State 7: Defeated and sealed"""
    return 1

def event_m50_37_x211(z15=_, z16=_, z21=_, z22=_):
    """[Condition] Black Knight: Generator
    z15: Sealed flag
    z16: Event group ID
    z21: Other ① Event group ID
    z22: Other ② Event group ID
    """
    """State 0,1: Generation determination"""
    CompareEventFlag(0, z15, 1)
    CompareEventFlag(0, 537020175, 1)
    SetConditionGroup(1, 8)
    CompareActiveChrNum(8, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(8, z16, z21, z22, 0, 0, 2, 5)
    CompareStateTime(8, 2, 3, 6)
    CompareEventFlag(8, 537020170, 1)
    CompareEventFlag(8, 537020172, 0)
    CompareEventFlag(8, 537020032, 1)
    SetConditionGroup(1, 9)
    CompareActiveChrNum(9, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(9, z16, z21, z22, 0, 0, 3, 3)
    CompareStateTime(9, 30, 3, 45)
    CompareEventFlag(9, 537020170, 1)
    CompareEventFlag(9, 537020172, 0)
    CompareEventFlag(9, 537020032, 1)
    SetConditionGroup(1, 10)
    CompareActiveChrNum(10, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(10, z16, z21, z22, 0, 0, 2, 5)
    CompareStateTime(10, 35, 3, 45)
    CompareEventFlag(10, 537020174, 1)
    CompareEventFlagValue(10, 1, 2, 6, 4)
    CompareMultiplayerPlayerCount(10, 1, 1, 0, 0)
    CompareEventFlag(10, 537020032, 1)
    SetConditionGroup(1, 11)
    CompareActiveChrNum(11, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(11, z16, z21, z22, 0, 0, 2, 5)
    CompareStateTime(11, 35, 3, 45)
    CompareEventFlag(11, 537020174, 1)
    CompareEventFlagValue(11, 1, 2, 12, 4)
    CompareMultiplayerPlayerCount(11, 1, 1, 1, 0)
    CompareEventFlag(11, 537020032, 1)
    SetConditionGroup(1, 12)
    CompareActiveChrNum(12, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(12, z16, z21, z22, 0, 0, 2, 5)
    CompareStateTime(12, 35, 3, 45)
    CompareEventFlag(12, 537020174, 1)
    CompareEventFlagValue(12, 1, 2, 20, 4)
    CompareMultiplayerPlayerCount(12, 1, 1, 2, 3)
    CompareEventFlag(12, 537020032, 1)
    SetConditionGroup(1, 13)
    CompareActiveChrNum(13, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(13, z16, z21, z22, 0, 0, 3, 3)
    CompareStateTime(13, 60, 3, 75)
    CompareEventFlag(13, 537020174, 1)
    CompareEventFlagValue(13, 1, 2, 6, 4)
    CompareMultiplayerPlayerCount(13, 1, 1, 0, 0)
    CompareEventFlag(13, 537020032, 1)
    SetConditionGroup(1, 14)
    CompareActiveChrNum(14, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(14, z16, z21, z22, 0, 0, 3, 3)
    CompareStateTime(14, 60, 3, 75)
    CompareEventFlag(14, 537020174, 1)
    CompareEventFlagValue(14, 1, 2, 12, 4)
    CompareMultiplayerPlayerCount(14, 1, 1, 1, 0)
    CompareEventFlag(14, 537020032, 1)
    SetConditionGroup(1, 15)
    CompareActiveChrNum(15, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(15, z16, z21, z22, 0, 0, 3, 3)
    CompareStateTime(15, 60, 3, 75)
    CompareEventFlag(15, 537020174, 1)
    CompareEventFlagValue(15, 1, 2, 20, 4)
    CompareMultiplayerPlayerCount(15, 1, 1, 2, 3)
    CompareEventFlag(15, 537020032, 1)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        """State 10: Wait just before generation"""
        CompareEventFlag(0, z15, 1)
        CompareEventFlag(0, 537020175, 1)
        CompareStateTime(1, 2, 3, 5)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 11: Generation"""
            return 0
    """State 12: Clear and sealed"""
    return 1

def event_m50_37_x212(z17=_, z18=_, z19=_, z20=_):
    """[Execution] Black Knight: Generator
    z17: Black Knight ① Generator ID
    z18: Black Knight ② Generator ID
    z19: Black Knight ③ Generator ID
    z20: Disable key guide
    """
    """State 0,3: SFX playback from generator: 70"""
    ChangeOwnObjState(70)
    """State 1: Random generation of black knights"""
    ForceRandomGeneration(1, z17, z18, z19, z20, 0)
    """State 4: Phase 3?"""
    CompareEventFlag(0, 537020174, 1)
    if ConditionGroup(0):
        """State 5: Generation count + 1"""
        AddAreaVariable(2, 1)
    else:
        pass
    """State 2: Wait for next generation"""
    CompareStateTime(0, 1, 3, 1)
    assert ConditionGroup(0)
    """State 6: Rerun"""
    return 0

def event_m50_37_x213(z15=_, z16=_, z17=_, z18=_, z19=_, z20=_, z21=_, z22=_):
    """[Preset] Black Knight: Generator
    z15: Sealed flag
    z16: Event group ID
    z17: Black Knight ① Generator ID
    z18: Black Knight ② Generator ID
    z19: Black Knight ③ Generator ID
    z20: Disable key guide
    z21: Other ① Event group ID
    z22: Other ② Event group ID
    """
    """State 0,1: [Reproduction] Black Knight: Generation Generator_SubState"""
    call = event_m50_37_x210(z15=z15)
    if call.Get() == 3:
        """State 7: Finish"""
        Label('L0')
        return 1
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 2:
        """State 5: [Condition] Black Knight: Generation Generator_After Defeating Boss_SubState"""
        assert event_m50_37_x365(z16=z16, z21=z21, z22=z22)
        """State 4: [Execution] Black Knight: Generation Generator_After Defeating Boss_SubState"""
        assert event_m50_37_x366(z17=z17, z18=z18, z19=z19, z20=z20, z16=z16, z21=z21, z22=z22)
    elif call.Get() == 0:
        """State 3: [Condition] Black Knight: Generation Generator_SubState"""
        call = event_m50_37_x211(z15=z15, z16=z16, z21=z21, z22=z22)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Black Knight: Generation Generator_SubState"""
            assert event_m50_37_x212(z17=z17, z18=z18, z19=z19, z20=z20)
    """State 6: Rerun"""
    return 0

def event_m50_37_x214(z123=_):
    """[Reproduction] NPC gesture management
    z123: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z123) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_37_x215(z128=_):
    """[Conditions] NPC gesture management
    z128: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z128, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x216(z124=_):
    """[Execution] NPC gesture management
    z124: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z124, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x217(z127=_, z128=_, z129=_):
    """[Preset] NPC gesture management
    z127: Defeat flag
    z128: Boss generator ID
    z129: Gesture flag
    """
    """State 0,1: [Reproduction] NPC Gesture Management_SubState"""
    call = event_m50_37_x214(z123=z127)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] NPC Gesture Management_SubState"""
        assert event_m50_37_x215(z128=z128)
        """State 2: [Execution] NPC Gesture Management_SubState"""
        assert event_m50_37_x216(z124=z129)
    """State 4: End state"""
    return 0

def event_m50_37_x218(z125=909, z126=910):
    """[Conditions] NPC Gesture Management_2
    z125: Boss ① Generator ID
    z126: Boss ② Generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(8, z125, 0, 5)
    CompareChrHpValue(8, z126, 0, 5)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x219(z123=537000091, z124=537020092, z125=909, z126=910):
    """[Preset] NPC Gesture Management_2
    z123: Defeat flag
    z124: Gesture flag
    z125: Boss ① Generator ID
    z126: Boss ② Generator ID
    """
    """State 0,1: [Reproduction] NPC Gesture Management_SubState"""
    call = event_m50_37_x214(z123=z123)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] NPC Gesture Management_2 Body Version_SubState"""
        assert event_m50_37_x218(z125=z125, z126=z126)
        """State 2: [Execution] NPC Gesture Management_SubState"""
        assert event_m50_37_x216(z124=z124)
    """State 4: End state"""
    return 0

def event_m50_37_x220():
    """[Reproduction] Sealing instructions"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x221(z109=_, z110=10, z111=_):
    """[Condition] Sealing order
    z109: Phase 1 and 2_ decision seconds
    z110: Phase 3_ judgment seconds
    z111: Phase 1 and 2_Total Defeat Count
    """
    """State 0,1: Sealing order judgment"""
    CompareEventFlag(0, 537020030, 1)
    SetConditionGroup(0, 8)
    CompareAreaTimer(8, 0, z109, 3)
    CompareEventFlag(8, 537020170, 1)
    CompareEventFlagValue(8, 1, 1, z111, 3)
    SetConditionGroup(0, 9)
    CompareAreaTimer(9, 0, z110, 3)
    CompareEventFlag(9, 537020174, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x222(z122=_, val1=_):
    """[Reproduction] Enemy Snowfield Defeat Count
    z122: Defeat count variable
    val1: Maximum number of generations
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the number of defeats reached the upper limit?"""
        if (GetAreaVariable(z122) > val1) != 0:
            pass
        else:
            """State 3: End state"""
            return 0
    """State 4: Do nothing: Quit"""
    return 1

def event_m50_37_x223(z121=_, z122=_, val1=_):
    """[Condition] Enemy Snowfield Defeat Count
    z121: Generator ID
    z122: Defeat count variable
    val1: Maximum number of generations
    """
    """State 0,1: Character destruction waiting or upper limit number judgment"""
    IsChrDead(0, z121)
    CompareEventFlagValue(1, 1, z122, val1, 3)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Variable addition"""
        return 0

def event_m50_37_x224(z121=_, z122=_):
    """[Execution] Enemy Snowfield Defeat Count
    z121: Generator ID
    z122: Defeat count variable
    """
    """State 0,1: [Condition] Ice King Battle_Start_SubState"""
    AddAreaVariable(z122, 1)
    """State 2: Wait for generator to restart"""
    IsChrActive(0, z121, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x225(z121=_, z122=_, val1=_):
    """[Preset] Defeat count of snowfield enemies
    z121: Generator ID
    z122: Defeat count variable
    val1: Maximum number of generations
    """
    """State 0,1: [Reproduction] Snowfield enemy defeat count _SubState"""
    call = event_m50_37_x222(z122=z122, val1=val1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Snowfield Enemy Defeat Count_SubState"""
        call = event_m50_37_x223(z121=z121, z122=z122, val1=val1)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Snowfield Enemy Defeat Count_SubState"""
            assert event_m50_37_x224(z121=z121, z122=z122)
            """State 4: Rerun"""
            return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x226(z120=537000011):
    """[Condition] Frozen treasure chest
    z120: Seal release flag
    """
    """State 0,1: Was the shrine maiden sealed?"""
    CompareEventFlag(0, z120, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x227():
    """[Execution] Frozen treasure chest"""
    """State 0,1: Treasure chest key guide ON"""
    DisableObjKeyGuide(50375580, 0)
    DisableObjKeyGuide(50375590, 0)
    DisableObjKeyGuide(50375600, 0)
    DisableObjKeyGuide(50375610, 0)
    DisableObjKeyGuide(50375510, 0)
    DisableObjKeyGuide(50375520, 0)
    DisableObjKeyGuide(50375540, 0)
    DisableObjKeyGuide(50375550, 0)
    DisableObjKeyGuide(50375690, 0)
    DisableObjKeyGuide(50375700, 0)
    DisableObjKeyGuide(50375710, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x228():
    """[Reproduction] Frozen treasure chest"""
    """State 0,1: Treasure chest key guide OFF"""
    DisableObjKeyGuide(50375580, 1)
    DisableObjKeyGuide(50375590, 1)
    DisableObjKeyGuide(50375600, 1)
    DisableObjKeyGuide(50375610, 1)
    DisableObjKeyGuide(50375510, 1)
    DisableObjKeyGuide(50375520, 1)
    DisableObjKeyGuide(50375540, 1)
    DisableObjKeyGuide(50375550, 1)
    DisableObjKeyGuide(50375690, 1)
    DisableObjKeyGuide(50375700, 1)
    DisableObjKeyGuide(50375710, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x229(z120=537000011):
    """[Preset] Frozen treasure chest
    z120: Seal release flag
    """
    """State 0,1: [Reproduction] Frozen treasure chest_SubState"""
    assert event_m50_37_x228()
    """State 3: [Condition] Frozen treasure chest_SubState"""
    assert event_m50_37_x226(z120=z120)
    """State 2: [Execution] Frozen treasure chest_SubState"""
    assert event_m50_37_x227()
    """State 4: End state"""
    return 0

def event_m50_37_x230(z115=762, z117=60375000):
    """[Condition] NPC mimicry control_map_start judgment
    z115: Generator ID
    z117: Mimicry activation_Special effect ID
    """
    """State 0,1: NPC special effect judgment"""
    ChrHasSpEffect(0, z115, z117, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x231(z116=537020063, z119=_):
    """[Execution] NPC mimic control_map
    z116: Mimicry flag
    z119: ON / OFF
    """
    """State 0,1: Mimic flag switching"""
    SetEventFlag(z116, z119)
    """State 2: End state"""
    return 0

def event_m50_37_x232(z115=762, z118=60375001):
    """[Condition] NPC mimic control_map_end judgment
    z115: Generator ID
    z118: Mimicry lottery_Special effect ID
    """
    """State 0,1: NPC generation judgment and special effect judgment"""
    ChrHasSpEffect(0, z115, z118, 0)
    IsChrActive(0, z115, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x233():
    """[Reproduction] NPC mimicry control_map_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x234():
    """[Reproduction] NPC mimic control_map"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m50_37_x235(z115=762, z116=537020063, z117=60375000, z118=60375001):
    """[Preset] NPC mimic control_map
    z115: Generator ID
    z116: Mimicry flag
    z117: Mimicry activation_Special effect ID
    z118: Mimicry lottery_Special effect ID
    """
    """State 0,1: [Reproduction] NPC mimic control_map_SubState"""
    call = event_m50_37_x234()
    if call.Get() == 1:
        """State 8: Finish"""
        return 1
    elif call.Get() == 0:
        """State 4: [Condition] NPC mimicry control_Map_Start judgment_SubState"""
        assert event_m50_37_x230(z115=z115, z117=z117)
        """State 3: [Execution] NPC mimic control_map_SubState"""
        assert event_m50_37_x231(z116=z116, z119=1)
        """State 2: [Reproduce] NPC mimic control_map_empty_SubState"""
        assert event_m50_37_x233()
        """State 5: [Condition] NPC mimic control_map_end judgment_SubState"""
        assert event_m50_37_x232(z115=z115, z118=z118)
        """State 6: [Execution] NPC mimic control_map_2_SubState"""
        assert event_m50_37_x231(z116=z116, z119=0)
        """State 7: Rerun"""
        return 0

def event_m50_37_x236():
    """[Reproduction] NPC mimic control _ character"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x237(z112=537020063):
    """[Condition] NPC mimicry control_character
    z112: Mimicry flag
    """
    """State 0,1: Mimicry flag judgment"""
    CompareEventFlag(0, z112, 1)
    assert ConditionGroup(0)
    """State 2: Mimic"""
    return 0

def event_m50_37_x238(z113=60375001, z114=762):
    """[Execution] NPC mimic control _ character
    z113: Mimicry lottery_Special effect ID
    z114: Generator ID
    """
    """State 0,1: Giving special effects of mimicry lottery"""
    SetEnemySpEffect(z114, z113, 19, 4)
    """State 2: End state"""
    return 0

def event_m50_37_x239(z112=537020063, z113=60375001, z114=762):
    """[Preset] NPC mimicry control_character
    z112: Mimicry flag
    z113: Mimicry lottery_Special effect ID
    z114: Generator ID
    """
    """State 0,1: [Reproduction] NPC mimicry control_character_SubState"""
    assert event_m50_37_x236()
    """State 3: [Condition] NPC mimicry control_Character_SubState"""
    assert event_m50_37_x237(z112=z112)
    """State 2: [Map] SFX tracking setting in front of the camera"""
    assert event_m50_37_x238(z113=z113, z114=z114)
    """State 4: End state"""
    return 0

def event_m50_37_x240():
    """[Execute] Sealing instruction"""
    """State 0,1: Sealing instruction flag ON"""
    SetEventFlag(537020030, 1)
    assert GetEventFlag(537020030) != 0
    """State 2: Re-search enemy flag ON"""
    SetEventFlag(537020031, 1)
    assert (GetStateTime() > 0.1) != 0
    """State 3: Re-search enemy flag OFF"""
    SetEventFlag(537020031, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x241(z109=_, z110=10, z111=_):
    """[Preset] Sealing instructions
    z109: Phase 1 and 2_ decision seconds
    z110: Phase 3_ judgment seconds
    z111: Phase 1 and 2_Total Defeat Count
    """
    """State 0,1: [Reproduction] Sealing instruction _SubState"""
    assert event_m50_37_x220()
    """State 3: [Condition] Sealing instruction_SubState"""
    assert event_m50_37_x221(z109=z109, z110=z110, z111=z111)
    """State 2: [Execution] Sealing instruction _SubState"""
    assert event_m50_37_x240()
    """State 4: End state"""
    return 0

def event_m50_37_x242():
    """[Reproduction] Sealing production"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x243(z101=794, z102=795, z103=796, z104=797):
    """[Conditions] Sealing production
    z101: White Knight ① Generator ID
    z102: White Knight ② Generator ID
    z103: White Knight ③ Generator ID
    z104: White Knight ④ Generator ID
    """
    """State 0,1: Has the white knight destroyed the generator?"""
    ChrHasSpEffect(0, z101, 96880200, 1)
    ChrHasSpEffect(0, z102, 96880200, 1)
    ChrHasSpEffect(0, z103, 96880200, 1)
    ChrHasSpEffect(0, z104, 96880200, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x244(z105=_, z106=_, z107=_, z108=_):
    """[Execution] Sealing production
    z105: Sealed flag
    z106: Next judgment weight
    z107: Generator OBJ instance ID
    z108: Ice OBJ instance ID
    """
    """State 0,1: Seal flag ON"""
    SetEventFlag(z105, 1)
    assert GetEventFlag(z105) != 0
    """State 3: Sealing instruction flag OFF"""
    SetEventFlag(537020030, 0)
    assert GetEventFlag(537020030) != 1
    """State 5: Ice appearance: 70"""
    ChangeObjState(z108, 70)
    """State 6: Waiting for the appearance of ice"""
    CompareObjState(0, z108, 20, 0)
    assert ConditionGroup(0)
    """State 4: Generator seal: 20"""
    ChangeObjState(z107, 20)
    """State 2: Wait for next judgment"""
    CompareStateTime(0, z106, 3, z106)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_37_x245(z101=794, z102=795, z103=796, z104=797, z105=_, z106=_, z107=_, z108=_):
    """[Preset] Sealing production
    z101: White Knight ① Generator ID
    z102: White Knight ② Generator ID
    z103: White Knight ③ Generator ID
    z104: White Knight ④ Generator ID
    z105: Sealed flag
    z106: Next judgment weight
    z107: Generator OBJ instance ID
    z108: Ice OBJ instance ID
    """
    """State 0,1: [Reproduction] Sealing production_SubState"""
    assert event_m50_37_x242()
    """State 3: [Condition] Sealing production_SubState"""
    assert event_m50_37_x243(z101=z101, z102=z102, z103=z103, z104=z104)
    """State 2: [Execution] Sealing production_SubState"""
    assert event_m50_37_x244(z105=z105, z106=z106, z107=z107, z108=z108)
    """State 4: End state"""
    return 0

def event_m50_37_x246():
    """[Reproduction] Production sound when falling"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x247(z99=3002000):
    """[Condition] Production sound when falling
    z99: Playback judgment point ID
    """
    """State 0,1: Playback point judgment"""
    IsPlayerInsidePoint(0, z99, z99, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x248(z100=30020):
    """[Execution] Production sound when falling
    z100: Event sound ID
    """
    """State 0,1: Impact sound playback"""
    PlaySoundAtPoint(z100)
    """State 2: End state"""
    return 0

def event_m50_37_x249(z99=3002000, z100=30020):
    """[Preset] Production sound when falling
    z99: Playback judgment point ID
    z100: Event sound ID
    """
    """State 0,1: [Reproduction] Production sound at fall_SubState"""
    assert event_m50_37_x246()
    """State 3: [Condition] Production sound at fall_SubState"""
    assert event_m50_37_x247(z99=z99)
    """State 2: [Execution] Production sound at fall_SubState"""
    assert event_m50_37_x248(z100=z100)
    """State 4: End state"""
    return 0

def event_m50_37_x250(z98=537000018):
    """[Reproduction] Tiger cry production
    z98: Event completion flag
    """
    """State 0,1: Have you ever executed an event?"""
    if GetEventFlag(z98) != 0:
        """State 3: Executed"""
        return 1
    else:
        """State 2: Not executed"""
        return 0

def event_m50_37_x251(z97=2502000):
    """[Condition] Tiger cry production
    z97: Playback judgment point ID
    """
    """State 0,1: Playback judgment"""
    IsPlayerInsidePoint(8, z97, z97, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x252(z95=25020, z96=1, z98=537000018):
    """[Execution] Tiger cry production
    z95: Event sound ID
    z96: Wait until playback
    z98: Event completion flag
    """
    """State 0,3: Event completion flag ON"""
    SetEventFlag(z98, 1)
    """State 2: Wait until playback"""
    CompareStateTime(0, z96, 3, z96)
    assert ConditionGroup(0)
    """State 1: Play sound"""
    PlaySoundAtPoint(z95)
    """State 4: End state"""
    return 0

def event_m50_37_x253(z95=25020, z96=1, z97=2502000, z98=537000018):
    """[Preset] Tiger cry production
    z95: Event sound ID
    z96: Wait until playback
    z97: Playback judgment point
    z98: Event completion flag
    """
    """State 0,1: [Reproduction] Tiger cry production_SubState"""
    call = event_m50_37_x250(z98=z98)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Tiger cry production_SubState"""
        assert event_m50_37_x251(z97=z97)
        """State 2: [Execution] Tiger cry production_SubState"""
        assert event_m50_37_x252(z95=z95, z96=z96, z98=z98)
    """State 4: End state"""
    return 0

def event_m50_37_x254(z93=503701, z94=537000011):
    """[Condition] Multi-prohibition until conversation with a shrine maiden
    z93: Multiplayer section ID
    z94: Judgment flag
    """
    """State 0,1: Are you not talking to a shrine maiden and a tiger?"""
    IsPlayerInMultiplayerSection(8, z93, 1)
    CompareEventFlag(8, z94, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x255(z93=503701, z94=537000011):
    """[Execution] Multi-prohibition until conversation with shrine maiden
    z93: Multiplayer section ID
    z94: Judgment flag
    """
    """State 0,1: Multi prohibited"""
    ProhibitMultiplayer(1)
    """State 2: Wait for next judgment"""
    IsPlayerInMultiplayerSection(0, z93, 0)
    CompareEventFlag(0, z94, 1)
    assert ConditionGroup(0)
    """State 3: Multi effective"""
    ProhibitMultiplayer(0)
    """State 4: End state"""
    return 0

def event_m50_37_x256(z94=537000011):
    """[Reproduction] Multi-prohibition until conversation with a shrine maiden
    z94: Judgment flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Have you already talked?"""
        if GetEventFlag(z94) != 0:
            pass
        else:
            """State 3: Not talking"""
            return 0
    else:
        pass
    """State 4: Conversation: End"""
    return 1

def event_m50_37_x257(z93=503701, z94=537000011):
    """[Preset] Multi-prohibition until conversation with a shrine maiden
    z93: Multiplayer section ID
    z94: Judgment flag
    """
    """State 0,1: [Reproduction] Multi-prohibited until conversation with a shrine maiden_SubState"""
    call = event_m50_37_x256(z94=z94)
    if call.Get() == 1:
        """State 4: Finish"""
        return 0
    elif call.Get() == 0:
        """State 3: [Condition] Multi-prohibition until conversation with a shrine maiden_SubState"""
        assert event_m50_37_x254(z93=z93, z94=z94)
        """State 2: [Execution] Multi-prohibited until conversation with a shrine maiden_SubState"""
        assert event_m50_37_x255(z93=z93, z94=z94)
        """State 5: Rerun"""
        return 1

def event_m50_37_x258(z92=2050000):
    """[Reproduction] Frozen Mimic_with body
    z92: Navigation change point ID
    """
    """State 0,1: Navigation switching: Not allowed"""
    AddNavimeshAttribute(z92, 2)
    """State 2: End state"""
    return 0

def event_m50_37_x259(z90=50373001):
    """[Condition] Frozen Mimic_with body
    z90: Ice OBJ instance ID
    """
    """State 0,1: Did the ice disappear?"""
    CompareObjState(0, z90, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x260(z91=537000070, z92=2050000):
    """[Execution] Frozen Mimic_with body
    z91: Generate flag
    z92: Navigation change point ID
    """
    """State 0,1: Generation flag ON"""
    SetEventFlag(z91, 1)
    """State 2: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z92, 2)
    """State 3: End state"""
    return 0

def event_m50_37_x261(z90=50373001, z91=537000070, z92=2050000):
    """[Preset] Frozen Mimic_with body
    z90: Ice OBJ instance ID
    z91: Generate flag
    z92: Navigation change point ID
    """
    """State 0,1: [Reproduction] Frozen Mimic_Body_SubState"""
    assert event_m50_37_x258(z92=z92)
    """State 3: Is it a hostile spirit?"""
    assert event_m50_37_x259(z90=z90)
    """State 2: [Execution] Frozen Mimic_Body_SubState"""
    assert event_m50_37_x260(z91=z91, z92=z92)
    """State 4: End state"""
    return 0

def event_m50_37_x262(z89=50371620):
    """[Condition] Frozen Mimic_No body
    z89: Ice OBJ instance ID
    """
    """State 0,1: Did the ice disappear?"""
    CompareObjState(0, z89, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x263(z88=50375720):
    """[Reproduction] Frozen Mimic _ No body
    z88: Treasure chest OBJ instance ID
    """
    """State 0,1: Treasure chest key guide OFF"""
    DisableObjKeyGuide(z88, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x264(z87=537000071, z88=50375720):
    """[Execution] Frozen Mimic _ No body
    z87: Generate flag
    z88: Treasure chest OBJ instance ID
    """
    """State 0,2: Hide treasure chest"""
    ChangeDrawHit(z88, 0)
    """State 1: Generation flag ON"""
    SetEventFlag(z87, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x265(z87=537000071, z88=50375720, z89=50371620):
    """[Preset] Frozen Mimic _ No body
    z87: Generate flag
    z88: Treasure chest OBJ instance ID
    z89: Ice OBJ instance ID
    """
    """State 0,1: [Reproduction] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x263(z88=z88)
    """State 3: [Condition] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x262(z89=z89)
    """State 2: [Execution] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x264(z87=z87, z88=z88)
    """State 4: End state"""
    return 0

def event_m50_37_x266(z86=50372800):
    """[Reproduction] Frozen insect key
    z86: Bug key OBJ instance ID
    """
    """State 0,1: Bug Key Key Guide OFF"""
    DisableObjKeyGuide(z86, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x267(z85=50372802):
    """[Condition] Frozen insect key
    z85: Ice OBJ instance ID
    """
    """State 0,1: Did the ice melt?"""
    CompareObjState(0, z85, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x268(z86=50372800):
    """[Execution] Frozen insect key
    z86: Bug key OBJ instance ID
    """
    """State 0,1: Bug Key Key Guide ON"""
    DisableObjKeyGuide(z86, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x269(z85=50372802, z86=50372800):
    """[Preset] Frozen insect key
    z85: Ice OBJ instance ID
    z86: Bug key OBJ instance ID
    """
    """State 0,1: [Reproduction] Frozen insect key _SubState"""
    assert event_m50_37_x266(z86=z86)
    """State 3: [Condition] Frozen insect key _SubState"""
    assert event_m50_37_x267(z85=z85)
    """State 2: [Execution] Frozen insect key _SubState"""
    assert event_m50_37_x268(z86=z86)
    """State 4: End state"""
    return 0

def event_m50_37_x270(z84=537000086):
    """[Reproduction] White knight falling with PC following
    z84: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z84) != 0:
        """State 3: Defeated: No follow-up"""
        return 1
    else:
        """State 2: Before defeat"""
        return 0

def event_m50_37_x271(z82=3004000):
    """[Condition] White knight falling with PC following
    z82: Judgment point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(8, z82, z82, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x272(z83=537020024):
    """[Execution] White knight falling with PC following
    z83: Follow flag
    """
    """State 0,1: Follow flag ON"""
    SetEventFlag(z83, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x273(z82=3004000, z83=537020024, z84=537000086):
    """[Preset] White knight falling with PC following
    z82: Judgment point ID
    z83: Follow flag
    z84: Defeat flag
    """
    """State 0,1: [Reproduction] White Knight_SubState falling with PC following"""
    call = event_m50_37_x270(z84=z84)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] White Knight_SubState falling with PC following"""
        assert event_m50_37_x271(z82=z82)
        """State 2: [Execution] Falling white knight in PC following_SubState"""
        assert event_m50_37_x272(z83=z83)
    """State 4: End state"""
    return 0

def event_m50_37_x274():
    """[Reproduction] Ice King Battle Phase 1_ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x275():
    """[Condition] Ice King Battle Phase 1"""
    """State 0,1: Have you entered the launch point?"""
    IsPlayerInsidePoint(8, 3000010, 3000010, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, 3000010, 3000010, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x276(z36=537020085):
    """[Execution] Ice King Battle Phase 1
    z36: Other flags for logic
    """
    """State 0,2: Start battle start timer"""
    StartAreaTimer(0)
    """State 3: Phase 1 flag ON"""
    SetEventFlag(537020170, 1)
    """State 1: Boss battle flag notification for logic"""
    SetEventFlag(z36, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x277(z77=_):
    """[Conditions] Ochikage to Miko
    z77: Stage seal release flag
    """
    """State 0,1: Stage seal release flag judgment"""
    CompareEventFlag(0, z77, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x278(z78=_, z79=_, z80=_, z81=3):
    """[Execution] Ochikage to Miko
    z78: Ice OBJ instance ID
    z79: Change navigation ① Point ID
    z80: Change navigation ② Point ID
    z81: weight
    """
    """State 0,4: Weight until destruction"""
    CompareStateTime(0, z81, 3, z81)
    assert ConditionGroup(0)
    """State 1: The disappearance of the ice OBJ: 70"""
    ChangeObjState(z78, 70)
    """State 2: Waiting for ice to disappear"""
    CompareObjState(0, z78, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z79, 2)
    DeleteNavimeshAttribute(z80, 2)
    """State 5: End state"""
    return 0

def event_m50_37_x279(z78=_, z79=_, z80=_):
    """[Reproduction] Ochikage to Miko
    z78: Ice OBJ instance ID
    z79: Change navigation ① Point ID
    z80: Change navigation ② Point ID
    """
    """State 0,1: Is the ice in its initial state?"""
    if CompareObjStateId(z78, 10, 1):
        """State 3: Waiting for ice to disappear"""
        assert CompareObjStateId(z78, 20, 0)
        """State 4: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z79, 2)
        DeleteNavimeshAttribute(z80, 2)
        """State 6: Executed"""
        return 1
    else:
        """State 2: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z79, 2)
        AddNavimeshAttribute(z80, 2)
        """State 5: Not executed"""
        return 0

def event_m50_37_x280(z77=_, z78=_, z79=_, z80=_, z81=3):
    """[Preset] Ochikage to Miko
    z77: Stage seal release flag
    z78: Ice OBJ instance ID
    z79: Change navigation ① Point ID
    z80: Change navigation ② Point ID
    z81: weight
    """
    """State 0,1: [Reproduction] Ochikazu _SubState to the shrine maiden"""
    call = event_m50_37_x279(z78=z78, z79=z79, z80=z80)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] A Submission to a Maiden_SubState"""
        assert event_m50_37_x277(z77=z77)
        """State 2: [Execution] A maiden to a shrine _SubState"""
        assert event_m50_37_x278(z78=z78, z79=z79, z80=z80, z81=z81)
    """State 4: End state"""
    return 0

def event_m50_37_x281(z75=50372601, z76=2400000):
    """[Reproduction] Transporter operated by lever
    z75: Transporter OBJ instance ID
    z76: Navigation change point ID
    """
    """State 0,1: Is the transporter already in operation?"""
    if CompareObjStateId(z75, 10, 1):
        """State 3: Waiting for operation"""
        assert CompareObjStateId(z75, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z76, 2)
        """State 6: Already in operation"""
        return 1
    else:
        """State 4: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z76, 2)
        """State 5: Not in operation"""
        return 0

def event_m50_37_x282(z74=50372600):
    """[Conditions] Transporter operated by lever
    z74: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z74, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x283(z75=50372601, z76=2400000):
    """[Execution] Transporter operated by lever
    z75: Transporter OBJ instance ID
    z76: Navigation change point ID
    """
    """State 0,2: The transporter is in operation: 70"""
    ChangeObjState(z75, 70)
    """State 3: Waiting for completion of operation of transporter"""
    CompareObjState(0, z75, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z76, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x284(z74=50372600, z75=50372601, z76=2400000):
    """[Preset] Transporter operated by lever
    z74: Lever OBJ instance ID
    z75: Transporter OBJ instance ID
    z76: Navigation change point ID
    """
    """State 0,1: [Reproduction] Transporter _SubState operated by lever"""
    call = event_m50_37_x281(z75=z75, z76=z76)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Transporter operated by lever_SubState"""
        assert event_m50_37_x282(z74=z74)
        """State 2: [Execution] Transporter operated by lever_SubState"""
        assert event_m50_37_x283(z75=z75, z76=z76)
    """State 4: End state"""
    return 0

def event_m50_37_x285(z67=_, z68=_, z69=_, z70=_, z71=_, z72=_, z73=_):
    """[Condition] Generation delay on appearance
    z67: Generation delay time
    z68: Generateable_start point ID
    z69: Generateable_end point ID
    z70: Delayed completion flag
    z71: Generator ID
    z72: Defeat count
    z73: Maximum number of generations
    """
    """State 0,1: Delay judgment"""
    IsChrActive(8, z71, 0)
    CompareEventFlag(8, 537020015, 1)
    IsPlayerInsidePoint(8, 600080, 600099, 0)
    IsPlayerInsidePoint(8, z68, z69, 1)
    CompareEventFlag(0, z70, 1)
    CompareEventFlagValue(0, 1, z72, z73, 3)
    if ConditionGroup(0):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(8):
        """State 2: delay"""
        return 0

def event_m50_37_x286(z67=_, z70=_):
    """[Execution] Generation delay on appearance
    z67: Generation delay time
    z70: Delayed completion flag
    """
    """State 0,1: During generation delay"""
    CompareStateTime(0, z67, 3, z67)
    CompareEventFlag(0, z70, 1)
    assert ConditionGroup(0)
    """State 2: Delay completion flag ON"""
    SetEventFlag(z70, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x287(z70=_):
    """[Reproduction] Generation delay at the time of appearance
    z70: Delayed completion flag
    """
    """State 0,2: Is it a hostile spirit?"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    else:
        Goto('L0')
    """State 5: Hostile spirit: no reaction"""
    return 2
    """State 1: Is it late?"""
    Label('L0')
    if GetEventFlag(z70) != 0:
        """State 4: Delayed"""
        return 1
    else:
        """State 3: First time"""
        return 0

def event_m50_37_x288(z67=_, z68=_, z69=_, z70=_, z71=_, z72=_, z73=_):
    """[Preset] Delay in generation
    z67: Generation delay time
    z68: Generateable_start point ID
    z69: Generateable_end point ID
    z70: Delayed completion flag
    z71: Generator ID
    z72: Defeat count
    z73: Maximum number of generations
    """
    """State 0,1: [Reproduction] Generation delay at appearance_SubState"""
    call = event_m50_37_x287(z70=z70)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Generation delay at appearance_SubState"""
        assert event_m50_37_x285(z67=z67, z68=z68, z69=z69, z70=z70, z71=z71, z72=z72, z73=z73)
        """State 2: [Execution] Generation delay at appearance_SubState"""
        assert event_m50_37_x286(z67=z67, z70=z70)
    """State 4: End state"""
    return 0

def event_m50_37_x289(z65=5037010):
    """[Condition] Operation of the second tiger
    z65: Boss Battle ID
    """
    """State 0,5: Has the boss battle started?"""
    IsEventBossBattle(0, z65, 1)
    assert ConditionGroup(0)
    """State 6: Start battle start timer"""
    StartAreaTimer(0)
    """State 2: Multi-person determination"""
    CompareMultiplayerPlayerCount(0, 1, 1, 2, 3)
    CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
    CompareMultiplayerPlayerCount(2, 1, 1, 0, 0)
    if ConditionGroup(0):
        """State 4: Start-up judgment_Friend 2"""
        CompareEventBossHpRatio(0, z65, 2, 100, 4)
        CompareEventBossHpRatio(0, z65, 1, 80, 5)
        CompareAreaTimer(0, 0, 30, 3)
        CompareMultiplayerPlayerCount(1, 1, 1, 2, 4)
        if ConditionGroup(1):
            """State 3: Start-up judgment_Friend 1"""
            Label('L0')
            CompareEventBossHpRatio(0, z65, 2, 100, 4)
            CompareEventBossHpRatio(0, z65, 1, 60, 5)
            CompareAreaTimer(0, 0, 60, 3)
            CompareMultiplayerPlayerCount(1, 1, 1, 1, 4)
            if ConditionGroup(1):
                """State 1: Start judgment_host only"""
                Label('L1')
                CompareEventBossHpRatio(0, z65, 2, 100, 4)
                CompareEventBossHpRatio(0, z65, 1, 40, 5)
                assert ConditionGroup(0)
            elif ConditionGroup(0):
                pass
        elif ConditionGroup(0):
            pass
    elif ConditionGroup(1):
        Goto('L0')
    elif ConditionGroup(2):
        Goto('L1')
    """State 7: End state"""
    return 0

def event_m50_37_x290(z66=537020093):
    """[Execution] Operation of the second tiger
    z66: Startup flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z66, 1)
    """State 2: Battle start timer stop"""
    EndAreaTimer(0)
    """State 3: End state"""
    return 0

def event_m50_37_x291(z64=537000091):
    """[Reproduction] Operation of the second tiger
    z64: Defeat flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: Have you already destroyed the boss?"""
        if GetEventFlag(z64) != 1:
            """State 3: Host: Undefeated"""
            return 0
        else:
            pass
    else:
        pass
    """State 4: Finish"""
    return 1

def event_m50_37_x292(z64=537000091, z65=5037010, z66=537020093):
    """[Preset] Operation of the second tiger
    z64: Defeat flag
    z65: Boss Battle ID
    z66: Startup flag
    """
    """State 0,1: [Reproduction] Operation of the second tiger _SubState"""
    call = event_m50_37_x291(z64=z64)
    if call.Get() == 0:
        """State 3: [Condition] Second tiger in operation _SubState"""
        assert event_m50_37_x289(z65=z65)
        """State 2: [Execution] Second tiger in operation _SubState"""
        assert event_m50_37_x290(z66=z66)
    elif call.Get() == 1:
        pass
    """State 4: Finish"""
    return 0

def event_m50_37_x293(z57=537000091):
    """[Reproduction] Black Tiger Battle_Start
    z57: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z57) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_37_x294(z58=3500000, z59=3500000):
    """[Condition] Black Tiger Battle_Start
    z58: Start point ID
    z59: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z58, z59, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z58, z59, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x295(z60=503, z61=5037010, z62=537020090):
    """[Execution] Black Tiger Battle_Start
    z60: Sound ID
    z61: Boss Battle ID
    z62: Tiger first body start flag
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z60)
    """State 1: Boss battle start notification"""
    StartBossFight(z61)
    """State 2: Boss battle flag notification for the first tiger for logic"""
    SetEventFlag(z62, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x296():
    """[Reproduction] Black Tiger Battle_2"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x297(z61=5037010):
    """[Condition] Black Tiger Battle_End
    z61: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z61, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x298(z60=503, z61=5037010, mode1=0, z62=537020090, z63=537020093):
    """[Execution] Black Tiger Battle_End
    z60: Sound ID
    z61: Boss Battle ID
    mode1: BGM stop time
    z62: Tiger first body start flag
    z63: Tiger second body start flag
    """
    """State 0,1: Tiger start flag OFF"""
    SetEventFlag(z62, 0)
    SetEventFlag(z63, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z61)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z60)
    """State 5: End state"""
    return 0

def event_m50_37_x299(z63=537020093):
    """[Condition] Black Tiger Battle_2
    z63: Tiger second body start flag
    """
    """State 0,1: Start-up judgment: 2nd tiger"""
    CompareEventFlag(0, z63, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x300():
    """[Execution] Black Tiger Battle_2 Launch"""
    """State 0,1: 2nd tiger: Boss HP gauge display"""
    DisplayBossHpBar(1, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x301():
    """[Reproduction] Black Tiger Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x302(z57=537000091, z58=3500000, z59=3500000, z60=503, z61=5037010, mode1=0, z62=537020090,
                      z63=537020093):
    """[Preset] Black Tiger Battle
    z57: Boss destruction flag
    z58: Start point ID
    z59: End point ID
    z60: Sound ID
    z61: Boss Battle ID
    mode1: BGM stop time
    z62: Tiger first body start flag
    z63: Tiger second body start flag
    """
    """State 0,2: [Reproduction] Black Tiger Battle_Start_SubState"""
    call = event_m50_37_x293(z57=z57)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 8: [Condition] Black Tiger Battle_Start_SubState"""
        assert event_m50_37_x294(z58=z58, z59=z59)
        """State 5: [Execution] Black Tiger Battle_Start_SubState"""
        assert event_m50_37_x295(z60=z60, z61=z61, z62=z62)
        """State 1: [Reproduction] Black Tiger Battle _ 2nd Start_Sky_SubState"""
        assert event_m50_37_x296()
        """State 7: [Condition] Black Tiger Battle_2"""
        assert event_m50_37_x299(z63=z63)
        """State 4: [Execution] Black Tiger Battle_2 Start-up_SubState"""
        assert event_m50_37_x300()
        """State 3: [Reproduction] Black Tiger Battle_End_Sky_SubState"""
        assert event_m50_37_x301()
        """State 9: [Condition] Black Tiger Battle_End_SubState"""
        assert event_m50_37_x297(z61=z61)
        """State 6: [Execution] Black Tiger Battle_End_SubState"""
        assert event_m50_37_x298(z60=z60, z61=z61, mode1=mode1, z62=z62, z63=z63)
    """State 10: End state"""
    return 0

def event_m50_37_x303(z55=103400):
    """[Reproduction] Event between DLCs
    z55: Defeat flag
    """
    """State 0,1: Already destroyed?"""
    if GetEventFlag(z55) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_37_x304(z56=5320):
    """[Condition] Event between DLCs
    z56: Generator ID
    """
    """State 0,1: Waiting for destruction"""
    IsChrDeadOrRespawnOver(0, z56, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x305(z55=103400):
    """[Execution] Event between DLCs
    z55: Defeat flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z55, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x306(z55=103400, z56=5320):
    """[Preset] DLC event
    z55: Defeat flag
    z56: Generator ID
    """
    """State 0,1: [Reproduction] Inter-DLC event"""
    call = event_m50_37_x303(z55=z55)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Event between DLCs"""
        assert event_m50_37_x304(z56=z56)
        """State 2: [Execution] Event between DLCs"""
        assert event_m50_37_x305(z55=z55)
    """State 4: End state"""
    return 0

def event_m50_37_x307():
    """[Reproduction] Enemy _ character _ sky moving by absorbing soul"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x308():
    """[Condition] Enemies that move by absorbing Seoul"""
    """State 0,1: Invincible treatment: Is the ice already broken?"""
    BecomeInvincibleInCurrentState()
    CompareEventFlag(0, 537000011, 1)
    assert ConditionGroup(0)
    """State 2: Endless"""
    return 0

def event_m50_37_x309():
    """[Execution] Enemies that move by absorbing Seoul_Character_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x310():
    """[Preset] Enemies that move by absorbing soul"""
    """State 0,1: [Reproduction] Enemy _ character _ sky _ SubState moving by absorbing soul"""
    assert event_m50_37_x307()
    """State 3: [Conditions] Enemies that move by absorbing Seoul_Character_SubState"""
    assert event_m50_37_x308()
    """State 2: [Execution] Enemies that move by absorbing soul_Character_Sky_SubState"""
    assert event_m50_37_x309()
    """State 4: End state"""
    return 0

def event_m50_37_x311(z52=537000019, z54=103303):
    """[Reproduction] Acquired Seoul by the death of a shrine maiden
    z52: Seoul acquisition other flags
    z54: Seoul acquisition global flag
    """
    """State 0,3: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Have you acquired the maiden soul in conversation?"""
        if GetEventFlag(z54) != 0:
            pass
        else:
            """State 2: Have you acquired Seoul in this event?"""
            if GetEventFlag(z52) != 0:
                pass
            else:
                """State 4: Unacquired"""
                return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x312(z53=340, z54=103303):
    """[Condition] Seoul won by the death of a shrine maiden
    z53: Generator ID
    z54: Seoul acquisition global flag
    """
    """State 0,1: Did you kill the shrine maiden?"""
    IsChrDeadOrRespawnOver(0, z53, 1)
    CompareEventFlag(1, z54, 1)
    if ConditionGroup(1):
        """State 3: Obtained in conversation"""
        return 1
    elif ConditionGroup(0):
        """State 2: Killed"""
        return 0

def event_m50_37_x313(z52=537000019):
    """[Execution] Seoul won by the death of a shrine maiden
    z52: Seoul acquisition other flags
    """
    """State 0,1: Item acquisition"""
    # lot:1788030:Soul of Alsanna, Silent Oracle
    AwardItem(1788030, 1)
    """State 2: Acquisition flag ON"""
    SetEventFlag(z52, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x314(z52=537000019, z53=340, z54=103303):
    """[Preset] Seoul won by the death of a shrine maiden
    z52: Seoul acquisition other flags
    z53: Generator ID
    z54: Seoul acquisition global flag
    """
    """State 0,1: [Reproduction] Seoul gained by the death of a shrine maiden_SubState"""
    call = event_m50_37_x311(z52=z52, z54=z54)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Seoul gained due to the death of a shrine maiden_SubState"""
        call = event_m50_37_x312(z53=z53, z54=z54)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Acquisition of Seoul by the death of a shrine maiden_SubState"""
            assert event_m50_37_x313(z52=z52)
    """State 4: End state"""
    return 0

def event_m50_37_x315(z49=50372650):
    """[Reproduction] Bakusta activation
    z49: Lever OBJ instance ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Has the lever already been activated?"""
        if CompareObjStateId(z49, 20, 0):
            pass
        elif CompareObjStateId(z49, 72, 0):
            pass
        elif CompareObjStateId(z49, 70, 0):
            pass
        else:
            """State 3: Before startup"""
            return 0
    """State 4: Finish"""
    return 1

def event_m50_37_x316(z49=50372650):
    """[Conditions] Bhaksta launching of escort warrior
    z49: Lever OBJ instance ID
    """
    """State 0,1: Did the player touch the lever?"""
    CompareObjState(0, z49, 10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x317(z50=_):
    """[Execution] Bakusta activation
    z50: Startup flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z50, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x318(z49=50372650, z50=537020003, z51=537020004):
    """[Preset] Samurai Warrior Bakusta Launch
    z49: Lever OBJ instance ID
    z50: Start flag
    z51: Completion flag
    """
    """State 0,1: [Reproduction] Bhaksta launch of Submarine Warrior_SubState"""
    call = event_m50_37_x315(z49=z49)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Bhaksta launching of escort warrior"""
        assert event_m50_37_x316(z49=z49)
        """State 2: [Execution] Samurai Warrior Bakusta Start_Start Pull_SubState"""
        assert event_m50_37_x317(z50=z50)
        """State 5: [Reproduction] Bakusta launching of the life warrior_Sky_SubState"""
        assert event_m50_37_x320()
        """State 4: [Conditions] Bhaksta launching of escort warrior _Cancel or confirmed_SubState"""
        call = event_m50_37_x319(z49=z49)
        if call.Get() == 0:
            """State 6: [Execution] Bhaksta launching of the fighter"""
            assert event_m50_37_x317(z50=z51)
        elif call.Get() == 1:
            """State 7: [Execution] Samurai Warrior Bakusta Launch_Cancel_SubState"""
            assert event_m50_37_x324(z50=z50, z49=z49)
            """State 9: Rerun"""
            return 1
    """State 8: Finish"""
    return 0

def event_m50_37_x319(z49=50372650):
    """[Condition] Bakusta activation of escort warrior _ Cancel or confirm
    z49: Lever OBJ instance ID
    """
    """State 0,1: Cancel or lever confirmation"""
    CompareObjState(0, z49, 71, 0)
    CompareObjState(0, z49, 10, 0)
    CompareObjState(1, z49, 72, 0)
    CompareObjState(1, z49, 20, 0)
    if ConditionGroup(1):
        """State 2: Confirm"""
        return 0
    elif ConditionGroup(0):
        """State 3: Cancel"""
        return 1

def event_m50_37_x320():
    """[Reproduction] Bhaksta launching of a suspicious warrior _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x321():
    """[Reproduce] Filter condition registration_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x322():
    """[Condition] Filter condition registration_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x323():
    """[Execute] Register filter condition"""
    """State 0,1: Create filter"""
    FilterConditionRegistration(110, 1, 15, 0, 8501, 1, 2010, 0, 1, 537020050, 0, 20, 1, 0, 0, 15)
    FilterConditionRegistration(100, 1, 0, 0, 8502, 1, 0, 0, 0, 537020050, 1, 20, 1, 0, 0, 0)
    FilterConditionRegistration(95, 1, 0, 0, 8502, 1, 2010, 0, 0.2, 537000001, 1, 10, 1, 0, 0, 0)
    FilterConditionRegistration(90, 1, 2, 3, 0, 1, 2010, 0, 1, 537020051, 1, 10, 1, 5037030, 1, 2)
    FilterConditionRegistration(80, 1, 3, 3, 0, 1, 2010, 0, 1, 537020051, 0, 10, 1, 5037030, 1, 3)
    FilterConditionRegistration(70, 1, 2, 3, 0, 1, 2010, 0, 1, 537020052, 1, 10, 1, 5037030, 1, 2)
    FilterConditionRegistration(60, 1, 3, 3, 0, 1, 2010, 0, 1, 537020052, 0, 10, 1, 5037030, 1, 3)
    FilterConditionRegistration(40, 1, 2, 2, 8501, 1, 2010, 0, 0.7, 537000001, 0, 10, 1, 0, 0, 2)
    FilterConditionRegistration(30, 1, 0, 0, 8502, 1, 0, 0, 0, 0, 0, 15, 1, 0, 0, 0)
    FilterConditionRegistration(20, 1, 9, 0, 0, 1, 5010, 0, 1, 537010014, 1, 30, 1, 0, 0, 9)
    FilterConditionRegistration(10, 1, 0, 0, 0, 1, 5010, 0, 0.2, 537010014, 0, 30, 1, 0, 0, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x324(z50=537020003, z49=50372650):
    """[Execution] Resident Warrior Bakusta Launch_Cancel
    z50: Startup flag
    z49: Lever OBJ instance ID
    """
    """State 0,1: Startup flag OFF"""
    SetEventFlag(z50, 0)
    """State 2: Initial waiting for lever"""
    CompareObjState(0, z49, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x325():
    """[Reproduction] Return from the White Knight Boss Room"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: Wait for judgment"""
        return 0
    else:
        """State 3: Guest: Exit"""
        return 1

def event_m50_37_x326(z31=5037000):
    """[Condition] Return from the boss room of the white knight
    z31: Boss Battle ID
    """
    """State 0,1: Has the boss battle started?"""
    IsEventBossBattle(0, z31, 1)
    assert ConditionGroup(0)
    """State 2: Has the boss battle ended?"""
    IsEventBossBattle(0, z31, 0)
    assert ConditionGroup(0)
    """State 3: Start of return"""
    return 0

def event_m50_37_x327(z30=_):
    """[Execution] Returning from the White Knight Boss Room
    z30: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z30, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x328(z30=_, z31=5037000, z32=537020025):
    """[Preset] Return from the White Knight Boss Room
    z30: Generator ID
    z31: Boss Battle ID
    z32: Return start flag
    """
    """State 0,1: [Reproduction] Return from the White Knight Boss Room_SubState"""
    call = event_m50_37_x325()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Return from White Knight's Boss Room_Start Judgment_SubState"""
        assert event_m50_37_x326(z31=z31)
        """State 3: [Execution] Return from the White Knight Boss Room_Return Start_SubState"""
        assert event_m50_37_x348(z32=z32)
        """State 6: [Reproduction] Return from the White Knight Boss Room_Sky_SubState"""
        assert event_m50_37_x349()
        """State 5: [Condition] Return from White Knight's Boss Room_Return Judgment_SubState"""
        assert event_m50_37_x347(z30=z30)
        """State 2: [Execution] Returning from the White Knight Boss Room_Character Delete_SubState"""
        assert event_m50_37_x327(z30=z30)
    """State 7: End state"""
    return 0

def event_m50_37_x329():
    """[Reproduction] Filter condition judgment_DLC possession"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x330():
    """[Condition] Filter condition judgment_DLC possession"""
    """State 0,1: DLC purchase status judgment"""
    CompareEventFlag(8, 100602, 1)
    CompareEventFlag(8, 100612, 1)
    # goods:52200000:Frozen Flower
    DoesPlayerHaveItem(8, 52200000, 1, 3, 1, 1, 0)
    if ConditionGroup(8):
        """State 2: Purchased"""
        return 0
    else:
        """State 3: Not purchased"""
        return 1

def event_m50_37_x331(z46=537020050, z48=_):
    """[Execution] Filter condition judgment_DLC possession
    z46: Filter flag
    z48: ON / OFF
    """
    """State 0,1: Filter flag switching"""
    SetEventFlag(z46, z48)
    """State 2: Finish"""
    return 0

def event_m50_37_x332(z46=537020050, z47=1):
    """[Preset] Filter condition judgment_DLC possession
    z46: Filter flag
    z47: ON / OFF
    """
    """State 0,1: [Reproduction] Filter condition judgment_DLC possession_SubState"""
    assert event_m50_37_x329()
    """State 3: [Condition] Filter condition judgment_DLC possession_SubState"""
    call = event_m50_37_x330()
    if call.Get() == 0:
        """State 4: [Execution] Filter condition judgment_DLC possession_ON_SubState"""
        assert event_m50_37_x331(z46=z46, z48=1)
    elif call.Get() == 1:
        """State 2: [Execution] Filter condition judgment_DLC possession_OFF_SubState"""
        assert event_m50_37_x331(z46=z46, z48=0)
    """State 5: Finish"""
    return 0

def event_m50_37_x333():
    """[Reproduction] Filter condition judgment_First Tiger Battle"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x334():
    """[Condition] Filter condition judgment_First Tiger Battle"""
    """State 0,1: Conversation and Judgment Eye Acquisition"""
    CompareEventFlag(8, 537020017, 1)
    CompareEventFlag(8, 537000012, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x335(z43=537020051, z45=1):
    """[Execution] Filter Condition Judgment_First Tiger Battle
    z43: Filter flag
    z45: ON / OFF
    """
    """State 0,1: Filter flag switching"""
    SetEventFlag(z43, z45)
    """State 2: Finish"""
    return 0

def event_m50_37_x336(z43=537020051, z44=1):
    """[Preset] Filter Condition Judgment_First Tiger Battle
    z43: Filter flag
    z44: ON / OFF
    """
    """State 0,1: [Reproduction] Filter Condition Judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x333()
    """State 3: [Condition] Filter condition judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x334()
    """State 2: [Execution] Filter Condition Judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x335(z43=z43, z45=1)
    """State 4: Finish"""
    return 0

def event_m50_37_x337():
    """[Reproduction] Filter condition judgment_Rematch tiger battle"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x338():
    """[Condition] Filter condition judgment_Rematch tiger battle"""
    """State 0,1: Judgment of battle start and shrine maiden acquisition"""
    CompareEventFlag(8, 537020080, 1)
    CompareEventFlag(8, 537000012, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x339(z41=537020052, z42=1):
    """[Execution] Filter condition judgment_Rematch tiger battle
    z41: Filter flag
    z42: ON / OFF
    """
    """State 0,1: Filter flag switching"""
    SetEventFlag(z41, z42)
    """State 2: Finish"""
    return 0

def event_m50_37_x340(z39=537020052, z40=1):
    """[Preset] Filter Condition Judgment_Rematch Tiger Battle
    z39: Filter flag
    z40: ON / OFF
    """
    """State 0,1: [Reproduction] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x337()
    """State 3: [Condition] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x338()
    """State 2: [Execution] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x339(z41=537020052, z42=1)
    """State 4: Finish"""
    return 0

def event_m50_37_x341():
    """[Preset] Filter condition registration"""
    """State 0,1: [Reproduce] Filter condition registration_empty_SubState"""
    assert event_m50_37_x321()
    """State 3: [Condition] Filter condition registration_empty_SubState"""
    assert event_m50_37_x322()
    """State 2: [Execution] Filter condition registration_SubState"""
    assert event_m50_37_x323()
    """State 4: End state"""
    return 0

def event_m50_37_x342():
    """[Reproduction] Return from the boss room_Yukihara"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x343(z37=1300000, z38=50371190):
    """[Preset] Return from Boss Room_Yukihara
    z37: Warp destination point ID
    z38: Warp OBJ instance ID
    """
    """State 0,1: [Reproduction] Return from Boss Room_Yukihara_SubState"""
    assert event_m50_37_x342()
    """State 3: [Condition] Return from the boss room_Judgment to check_SubState"""
    assert event_m50_37_x209(z38=z38)
    """State 2: [Execution] Return from Boss Room_Warp_SubState"""
    assert event_m50_37_x102(z37=z37)
    """State 4: Rerun"""
    return 0

def event_m50_37_x344():
    """[Reproduction] Ice King Battle_Rush_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x345():
    """[Condition] Ice King Battle_Rush"""
    """State 0,1: Judgment of conditions for the rush phase"""
    CompareEventFlag(0, 537020171, 1)
    SetConditionGroup(0, 8)
    CompareEventFlagValue(8, 1, 1, 6, 3)
    CompareEventFlag(8, 537020035, 0)
    CompareEventFlag(8, 537020036, 0)
    CompareEventFlag(8, 537020037, 0)
    SetConditionGroup(0, 9)
    CompareEventFlagValue(9, 1, 1, 6, 3)
    CompareEventFlag(9, 537020035, 1)
    SetConditionGroup(0, 10)
    SetConditionGroup(10, 1)
    CompareEventFlagValue(1, 1, 1, 6, 3)
    CompareActiveChrNum(1, 12, 13, 14, 0, 0, 1, 0)
    CompareEventFlag(10, 537020036, 1)
    SetConditionGroup(0, 11)
    CompareActiveChrNum(11, 12, 13, 14, 0, 0, 0, 0)
    CompareEventFlag(11, 537020037, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x346():
    """[Execution] Ice King Battle Rush"""
    """State 0,1: Phase rush flag ON"""
    SetEventFlag(537020171, 1)
    assert (GetStateTime() >= 0) != 0
    """State 2: End state"""
    return 0

def event_m50_37_x347(z30=_):
    """[Condition] Return from White Boss Boss Room_Return Judgment
    z30: Generator ID
    """
    """State 0,1: Return judgment"""
    CompareEventFlag(8, 537020087, 1)
    ChrHasSpEffect(8, z30, 96880100, 1)
    assert ConditionGroup(8)
    """State 2: Delete character"""
    return 0

def event_m50_37_x348(z32=537020025):
    """[Execution] Return from the White Knight's Boss Room_Start Return
    z32: Return start flag
    """
    """State 0,1: Return start flag ON"""
    SetEventFlag(z32, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x349():
    """[Reproduction] Return from the White Knight Boss Room _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x350(z26=50371570, z27=537000002, z28=537000086, z29=5, action1=5310):
    """[Preset] Crown that appears when a boss is destroyed
    z26: 棺 桶 Activating key guide
    z27: Crown acquisition flag
    z28: Defeat flag
    z29: weight
    action1: Text ID
    """
    """State 0,1: [Reproduction] Crown _SubState that appears when a boss is destroyed"""
    call = event_m50_37_x351(z27=z27, z26=z26)
    if call.Get() == 0:
        """State 7: [Condition] Crown that appears when boss is destroyed _ Defeat determination_SubState"""
        call = event_m50_37_x357(z28=z28)
        if call.Get() == 1:
            """State 9: [Execution] Crown_Sky_SubState that appears when a boss is destroyed"""
            assert event_m50_37_x359()
        elif call.Get() == 0:
            """State 5: [Execution] Crown Appearing at Boss Defeat_Display Crown_SubState"""
            assert event_m50_37_x355(z26=z26)
            """State 2: [Reproduction] Crown _ Sky _ SubState that appears by destroying the boss"""
            assert event_m50_37_x352()
            """State 8: [Condition] Crown that appears when boss is destroyed"""
            call = event_m50_37_x358(z26=z26)
            if call.Get() == 1:
                """State 3: [Execution] Crown that appears by destroying the boss_Key guide switching_SubState"""
                assert event_m50_37_x353(z26=z26)
            elif call.Get() == 0:
                """State 4: [Execution] Crown Appearing at Boss Defeat_Get Crown_SubState"""
                assert event_m50_37_x354(z26=z26, z27=z27, z29=z29, action1=action1)
                Goto('L0')
            elif call.Get() == 2:
                """State 10: [Execution] Crown that appears after destroying the boss_Unacquired_SubState"""
                assert event_m50_37_x360(z26=z26)
        """State 12: Rerun"""
        return 1
    elif call.Get() == 2:
        """State 6: [Execution] Crown Appearing by Boss Defeat_Hide_SubState"""
        assert event_m50_37_x356(z26=z26)
    elif call.Get() == 1:
        pass
    """State 11: Finish"""
    Label('L0')
    return 0

def event_m50_37_x351(z27=537000002, z26=50371570):
    """[Reproduction] Crown that appears when a boss is destroyed
    z27: Crown acquisition flag
    z26: 棺 桶 Activating key guide
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you acquired the crown?"""
    if GetEventFlag(z27) != 1:
        """State 3: Hide crown"""
        ChangeObjState(z26, 10)
        assert CompareObjStateId(z26, 10, 0)
        """State 4: Waiting for appearance"""
        return 0
    else:
        """State 6: End: Hide"""
        return 2
    """State 5: Guest user"""
    Label('L0')
    return 1

def event_m50_37_x352():
    """[Reproduction] Crown that appears by destroying boss _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x353(z26=50371570):
    """[Execution] Crown that appears when the boss is destroyed
    z26: 棺 桶 Activating key guide
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z26, 1)
    """State 2: Is the boss battle over?"""
    IsEventBossBattle(0, 5037000, 0)
    assert ConditionGroup(0)
    """State 3: Enable key guide"""
    DisableObjKeyGuide(z26, 0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x354(z26=50371570, z27=537000002, z29=5, action1=5310):
    """[Execution] Crowns that appear when the boss is destroyed
    z26: 棺 桶 Activating key guide
    z27: Crown acquisition flag
    z29: weight
    action1: Text ID
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z26, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z26, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60031000:Crown of the Ivory King
    AwardItem(60031000, 1)
    """State 4: Turn on the crown acquisition flag"""
    SetEventFlag(z27, 1)
    """State 5: weight"""
    CompareStateTime(0, z29, 3, z29)
    assert ConditionGroup(0)
    """State 6: Text display"""
    # action:5310:"A faint heat lingers in the ancient crown"
    DisplayEventMessage(action1, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 7: End state"""
    return 0

def event_m50_37_x355(z26=50371570):
    """[Execution] Crowns that appear when a boss is destroyed
    z26: 棺 桶 Activating key guide
    """
    """State 0,1: Crown display: 30"""
    ChangeObjState(z26, 30)
    """State 2: End state"""
    return 0

def event_m50_37_x356(z26=50371570):
    """[Execution] Crowns that appear when the boss is destroyed
    z26: 棺 桶 Activating key guide
    """
    """State 0,1: Crown OBJ hidden: 10"""
    ChangeObjState(z26, 10)
    """State 2: End state"""
    return 0

def event_m50_37_x357(z28=537000086):
    """[Condition] Crown that appears when a boss is destroyed
    z28: Defeat flag
    """
    """State 0,1: Did you defeat the king of ice or become multiplayer?"""
    CompareEventFlag(0, z28, 1)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 2: Multi start: Waiting for end"""
        IsMultiplayer(0, 0, 0)
        assert ConditionGroup(0)
        """State 4: Multi-end: Re-execute"""
        return 1
    elif ConditionGroup(0):
        """State 3: Crown display"""
        return 0

def event_m50_37_x358(z26=50371570):
    """[Conditions] Examining the crown that appears when a boss is destroyed
    z26: 棺 桶 Activating key guide
    """
    """State 0,1: Did you check the crown or became a boss battle?"""
    IsObjSearched(0, z26)
    IsEventBossBattle(1, 5037000, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 4: During the boss battle"""
    return 1
    """State 2: Can items be acquired?"""
    Label('L0')
    # goods:21640100:Crown of the Ivory King
    if CanGetItem(21640100, 1) != 0:
        """State 3: Item acquisition"""
        return 0
    else:
        """State 5: Not available"""
        return 2

def event_m50_37_x359():
    """[Execution] Crown that appears after destroying the boss_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x360(z26=50371570):
    """[Execution] Crown that appears when the boss is destroyed
    z26: 棺 桶 Activating key guide
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z26, 1)
    """State 1: Acquisition failure window display"""
    # lot:60031000:Crown of the Ivory King
    DisplayItemAwardFailure(60031000, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 2: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z26, 0)
    """State 5: End state"""
    return 0

def event_m50_37_x361(z23=_):
    """[Condition] White Knight
    z23: Generator ID
    """
    """State 0,1: White Knight starts sealing or died"""
    ChrHasSpEffect(0, z23, 96880200, 1)
    IsChrDead(0, z23)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x362(z24=_):
    """[Execution] White Knight
    z24: Profession flag
    """
    """State 0,1: Vocational occupation flag ON"""
    SetEventFlag(z24, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x363(z24=_, z25=537000086):
    """[Reproduction] White Knight
    z24: Profession flag
    z25: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 3: Has the boss been destroyed?"""
        if GetEventFlag(z25) != 1:
            """State 1: Vocational occupation flag OFF"""
            SetEventFlag(z24, 0)
            """State 4: Undefeated"""
            return 0
        else:
            pass
    """State 5: Finish"""
    return 1

def event_m50_37_x364(z23=_, z24=_, z25=537000086):
    """[Preset] White Knight
    z23: Generator ID
    z24: Profession flag
    z25: Defeat flag
    """
    """State 0,1: [Reproduction] White Knight's profession_SubState"""
    call = event_m50_37_x363(z24=z24, z25=z25)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] White knight's profession_SubState"""
        assert event_m50_37_x361(z23=z23)
        """State 2: [Execution] White Knight's profession_SubState"""
        assert event_m50_37_x362(z24=z24)
    """State 4: End state"""
    return 0

def event_m50_37_x365(z16=_, z21=_, z22=_):
    """[Condition] Black Knight: Generation Generator_After Defeating Boss
    z16: Event group ID
    z21: Other ① Event group ID
    z22: Other ② Event group ID
    """
    """State 0,1: Generation determination"""
    CompareActiveChrNum(8, z16, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(8, z16, z21, z22, 0, 0, 5, 5)
    CompareEventFlag(8, 537020032, 1)
    assert ConditionGroup(8)
    """State 2: Wait just before generation"""
    CompareStateTime(0, 2, 3, 5)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_37_x366(z17=_, z18=_, z19=_, z20=_, z16=_, z21=_, z22=_):
    """[Execution] Black Knight: Generation Generator
    z17: Black Knight ① Generator ID
    z18: Black Knight ② Generator ID
    z19: Black Knight ③ Generator ID
    z20: Disable key guide
    z16: Event group ID
    z21: Other ① Event group ID
    z22: Other ② Event group ID
    """
    """State 0,3: SFX playback from generator: 70"""
    ChangeOwnObjState(70)
    """State 1: Random generation of black knights"""
    ForceRandomGeneration(1, z17, z18, z19, z20, 0)
    """State 2: Wait for next generation"""
    CompareActiveChrNum(8, z16, z21, z22, 0, 0, 5, 5)
    CompareStateTime(8, 140, 3, 155)
    assert ConditionGroup(8)
    """State 4: Rerun"""
    return 0

def event_m50_37_x367():
    """[Reproduction] Wind speed magnification change by snowstorm cancellation"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x368(z14=537000001):
    """[Conditions] Change in wind speed magnification by canceling snowstorm
    z14: Snowstorm release flag
    """
    """State 0,1: Has the snowstorm been lifted?"""
    CompareEventFlag(0, z14, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x369():
    """[Execution] Wind speed magnification change by canceling snowstorm"""
    """State 0,1: Change in wind speed magnification"""
    SetWindSpeedMultiplier(1, 0.1)
    """State 2: End state"""
    return 0

def event_m50_37_x370(z14=537000001):
    """[Preset] Wind speed magnification change by removing snowstorm
    z14: Snowstorm release flag
    """
    """State 0,1: [Reproduction] Wind speed magnification change by canceling snowstorm_SubState"""
    assert event_m50_37_x367()
    """State 3: [Condition] Change in wind speed magnification by canceling snowstorm_SubState"""
    assert event_m50_37_x368(z14=z14)
    """State 2: [Execution] Wind speed magnification change due to snowstorm cancellation_SubState"""
    assert event_m50_37_x369()
    """State 4: End state"""
    return 0

def event_m50_37_x371():
    """[Reproduction] Start of operation of Black Knight Generator"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x372(z10=3400000):
    """[Condition] Start of operation of Black Knight Generator
    z10: Judgment point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z10, z10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x373(z11=537020032, z12=0, z13=0):
    """[Execution] Start of operation of Black Knight Generator
    z11: Operation flag
    z12: Minimum weight
    z13: Maximum weight
    """
    """State 0,2: weight"""
    CompareStateTime(0, z12, 3, z13)
    assert ConditionGroup(0)
    """State 1: Operation flag ON"""
    SetEventFlag(z11, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x374(z10=3400000, z11=537020032, z12=0, z13=0):
    """[Preset] Start of Black Knight Generator
    z10: Judgment point ID
    z11: Operation flag
    z12: Minimum weight until operation
    z13: Maximum weight until operation
    """
    """State 0,1: [Reproduction] Black Knight Generator starts operation_SubState"""
    assert event_m50_37_x371()
    """State 3: [Condition] Start of Black Knight Generator_SubState"""
    assert event_m50_37_x372(z10=z10)
    """State 2: [Execution] Start of Black Knight Generator_SubState"""
    assert event_m50_37_x373(z11=z11, z12=z12, z13=z13)
    """State 4: End state"""
    return 0

def event_m50_37_x375():
    """[Reproduction] 棺 桶 Bobsleigh _ initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_37_x376():
    """[Condition] 棺 桶 Bobsleigh_Initialization_Empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x377(z9=50371010):
    """[Execution] 棺 桶 Bobsled_Initialization
    z9: 棺 桶 OBJ instance ID
    """
    """State 0,1: 棺 桶 OBJ initialization"""
    InitializeObj(z9)
    assert CompareObjStateId(z9, 10, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x378(z9=50371010):
    """[Preset] 棺 桶 Bobsleigh_Initialization
    z9: 棺 桶 OBJ instance ID
    """
    """State 0,1: [Reproduction] 棺 桶 Bobsleigh_Initialization_SubState"""
    call = event_m50_37_x375()
    if call.Get() == 0:
        """State 3: [Condition] 棺 桶 Bobsleigh_Initialization_Empty_SubState"""
        assert event_m50_37_x376()
        """State 2: [Execution] 棺 桶 Bobsleigh_Initialization_SubState"""
        assert event_m50_37_x377(z9=z9)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_37_x379():
    """[Reproduction] White knight deleted inside ice after boss war _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x380(z8=537020175):
    """[Condition] White knight inside ice after boss battle removed
    z8: Judgment flag
    """
    """State 0,1: Boss clear flag judgment"""
    CompareEventFlag(0, z8, 0)
    CompareEventFlag(1, z8, 1)
    if ConditionGroup(1):
        """State 2: OFF standby"""
        CompareEventFlag(0, z8, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(0):
        pass
    """State 3: End state"""
    return 0

def event_m50_37_x381():
    """[Execution] White knight inside ice after boss battle removed"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x382(z8=537020175):
    """[Preset] Delete the white knight inside the ice after the boss battle
    z8: Judgment flag
    """
    """State 0,1: [Reproduction] White knight inside ice after boss battle removed_Sky_SubState"""
    assert event_m50_37_x379()
    """State 3: [Condition] White knight inside ice after boss battle removed_SubState"""
    assert event_m50_37_x380(z8=z8)
    """State 2: [Execution] Delete the white knight inside the ice after the boss battle_Sky_SubState"""
    assert event_m50_37_x381()
    """State 4: End state"""
    return 0

def event_m50_37_x383(z6=_):
    """[Reproduction] Instant death damage inside the ice
    z6: Point ID
    """
    """State 0,1: Disabling the damage range"""
    EnableDamageArea(z6, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x384(z7=_):
    """[Condition] Instant death damage inside the ice
    z7: Ice OBJ instance ID
    """
    """State 0,1: Has ice appeared?"""
    CompareObjState(0, z7, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x385(z6=_):
    """[Execution] Instant death damage inside the ice
    z6: Point ID
    """
    """State 0,3: Disabling damage"""
    SetDamageImmunityByGeneratorId(794, 330040000, 1)
    SetDamageImmunityByGeneratorId(795, 330040000, 1)
    SetDamageImmunityByGeneratorId(796, 330040000, 1)
    SetDamageImmunityByGeneratorId(797, 330040000, 1)
    """State 2: weight"""
    CompareStateTime(0, 1, 3, 1)
    assert ConditionGroup(0)
    """State 1: Enable damage range"""
    EnableDamageArea(z6, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x386(z6=_, z7=_):
    """[Preset] Instant death damage inside the ice
    z6: Point ID
    z7: Ice OBJ instance ID
    """
    """State 0,1: [Reproduction] Instant death damage inside ice_SubState"""
    assert event_m50_37_x383(z6=z6)
    """State 3: [Condition] Instant death damage inside ice_SubState"""
    assert event_m50_37_x384(z7=z7)
    """State 2: [Execution] Instant death damage inside the ice_SubState"""
    assert event_m50_37_x385(z6=z6)
    """State 4: End state"""
    return 0

def event_m50_37_x387(z5=17000):
    """[DC] [Execution] Yukihara gets the eyes of a priestess
    z5: Event SFXID
    """
    """State 0,1: Stop SFX"""
    StopSfxAtPoint(z5)
    """State 2: End state"""
    return 0

def event_m50_37_x388():
    """[DC] [Reproduction] Cannot lock fighter"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x389(z1=5320):
    """[DC] [Condition] Management of non-lockable fighter
    z1: Generator ID
    """
    """State 0,1: Battle state judgment"""
    CompareChrEzStateValue(0, z1, 1, 1, 1)
    CompareChrEzStateValue(1, z1, 1, 1, 0)
    if ConditionGroup(1):
        """State 3: In combat"""
        return 1
    elif ConditionGroup(0):
        """State 2: Inside the friend"""
        return 0

def event_m50_37_x390(z1=5320):
    """[DC] [Execution] Management of non-lockable warriors
    z1: Generator ID
    """
    """State 0,1: Grants a non-locking effect"""
    SetEnemySpEffect(z1, 170000000, 19, 4)
    """State 2: Did you start battle or died?"""
    CompareChrEzStateValue(0, z1, 1, 1, 0)
    IsChrDead(0, z1)
    assert ConditionGroup(0)
    """State 3: Cancel lock disable effect"""
    ClearEnemySpEffect(z1, 170000000)
    """State 4: Finish"""
    return 0

def event_m50_37_x391(z1=5320):
    """[DC] [Preset] Management of non-lockable warriors
    z1: Generator ID
    """
    """State 0,1: [DC] [Reproduction] Pallet warrior cannot be locked _Sky_SubState"""
    assert event_m50_37_x388()
    """State 3: [DC] [Conditions] Uncontrollable management of esoteric warriors_SubState"""
    call = event_m50_37_x389(z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [DC] [Execution] Cannot lock fighter soldiers_SubState"""
        assert event_m50_37_x390(z1=z1)
    """State 4: Finish"""
    return 0

def event_m50_37_101000():
    """Black Spirit Display_Witch"""
    """State 0,1: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_37_x70(z248=10000000, z249=760, z250=0, z251=0.2, z252=537020060)

def event_m50_37_101010():
    """Black Spirit Display_Dark Miracle"""
    """State 0,1: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_37_x70(z248=10000100, z249=761, z250=0, z251=0.2, z252=537020061)

def event_m50_37_101020():
    """Black Spirit Display_Holy Knight"""
    """State 0,1: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_37_x70(z248=10000200, z249=762, z250=0, z251=0, z252=537020062)

def event_m50_37_4000000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m50_37_x74(z233=537020055, z234=14, z235=537000056, z236=3, z237=40)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m50_37_x79(z241=80000000, z242=0, z243=5, z244=980, val2=1, z245=40, z246=80000001,
                z247=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m50_37_x79(z241=80000100, z242=0, z243=5, z244=980, val2=2, z245=40, z246=80000101,
                z247=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m50_37_x79(z241=80000200, z242=0, z243=5, z244=980, val2=3, z245=40, z246=80000201,
                z247=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(537020057, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m50_37_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m50_37_x82(z238=537000056, z239=980, mode3=1)
    """State 1: Finish"""
    EndMachine()

def event_m50_37_4001000():
    """[DC] Cannot lock fighter"""
    """State 0,2: [DC] [Preset] Pallet Warrior Unlockable Management_SubState"""
    assert event_m50_37_x391(z1=5320)
    """State 1: Finish"""
    EndMachine()

