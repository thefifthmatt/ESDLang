# -*- coding: utf-8 -*-
def event_m50_37_1000():
    """Falling damage disabled_player"""
    """State 0,2: [Preset] Falling damage disabled_player_SubState"""
    assert event_m50_37_x87(z202=100000, z203=100001)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_1010():
    """Fall damage disabled_NPC_1"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z199=100000, z200=100001, z201=770)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_1020():
    """Fall damage invalid_NPC_2"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z199=100000, z200=100001, z201=771)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_1030():
    """Falling damage disabled_White Knight_1"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z199=100000, z200=100001, z201=794)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_1040():
    """Falling damage disabled_White Knight_2"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z199=100000, z200=100001, z201=795)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_1050():
    """Falling damage disabled_White Knight_3"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z199=100000, z200=100001, z201=796)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_1060():
    """Falling damage disabled_White Knight_4"""
    """State 0,2: [Preset] Drop damage invalid_NPC_SubState"""
    assert event_m50_37_x91(z199=100000, z200=100001, z201=797)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_2100():
    """Release of ice seal"""
    """State 0,2: [Preset] Canceling the ice seal_SubState"""
    assert event_m50_37_x129(flag27=537000011, z176=50371200, z177=210000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_2200():
    """A torch disappears in a snowstorm"""
    """State 0,2: [Preset] Torches disappear in a snowstorm_SubState"""
    assert event_m50_37_x99(z191=10, z192=537000001, z193=30)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_2300():
    """Lighthouse under a snowstorm"""
    """State 0,2: [Preset] Lighthouse under the snowstorm_SubState"""
    assert event_m50_37_x133(z175=537000001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_2400():
    """Multi-prohibition up to conversation with a shrine maiden"""
    """State 0,3: [Preset] Multi-prohibition until conversation with a shrine maiden_SubState"""
    call = event_m50_37_x257(z81=503701, flag13=537000011)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_2500():
    """A shrine for a shrine maiden"""
    """State 0,2: [Preset] A maiden for a shrine _1 stage _SubState"""
    assert event_m50_37_x280(z66=537000150, z67=50371400, z68=250000, z69=250001, z70=3)
    """State 3: [Preset] A maiden to the shrine _2 stage _SubState"""
    assert event_m50_37_x280(z66=537000151, z67=50371401, z68=250010, z69=250011, z70=3)
    """State 4: [Preset] Machikazu _3 stages_SubState"""
    assert event_m50_37_x280(z66=537000152, z67=50371402, z68=250020, z69=250021, z70=3)
    """State 5: [Preset] Fallen maiden to the shrine _4 stages_SubState"""
    assert event_m50_37_x280(z66=537000153, z67=50371403, z68=250030, z69=250031, z70=3)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_2600():
    """Seoul won by the death of a shrine maiden"""
    """State 0,2: [Preset] Seoul gained by the death of a shrine maiden_SubState"""
    assert event_m50_37_x314(flag6=537000019, z47=340, flag7=103303)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_2700():
    """Wind speed magnification change by removing snowstorm"""
    """State 0,2: [Preset] Wind speed magnification change by canceling snowstorm_SubState"""
    assert event_m50_37_x370(z13=537000001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_3020():
    """C root key door: Yukihara"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m50_37_x1(z285=1005, z286=1105, z287=52500000, z288=537000047)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_4000():
    """棺 桶 Bobsled"""
    """State 0,3: Is the initialization event complete?"""
    assert EventEnded(4020) != 0
    """State 4: [Preset] 棺 桶 Bobsleigh_SubState"""
    call = event_m50_37_x121(z179=50371010, z180=537000005)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_4010():
    """イ ベ ン ト Startup event"""
    """State 0,2: [Preset] 棺 桶 Event at startup_SubState"""
    assert event_m50_37_x125(flag28=537000005, z178=50371011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_4020():
    """棺 桶 Bobsled_Initialization"""
    """State 0,2: [Preset] 棺 桶 Bobsleigh_Initialization_SubState"""
    assert event_m50_37_x378(z8=50371010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_5000():
    """Snowstorm management in the snowy field area"""
    """State 0,3: [Preset] Snowstorm management in the snowy field_SubState"""
    call = event_m50_37_x165(z154=537010014, z155=537020015)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6000():
    """Enemy _A that appears in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7000, z145=600100, z146=600149, z147=75, z148=11, z149=20, z150=600020,
                             z151=600029)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6010():
    """Enemy _B appearing in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z57=55, z58=600020, z59=600029, flag11=537010130, z60=7001, z61=11, z62=20)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7001, z145=600150, z146=600199, z147=110, z148=11, z149=20, z150=600020,
                             z151=600029)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6040():
    """Enemy _E that appears in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7004, z145=600300, z146=600349, z147=60, z148=12, z149=20, z150=600030,
                             z151=600039)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6050():
    """Enemy _F that appears in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z57=40, z58=600030, z59=600039, flag11=537010131, z60=7005, z61=12, z62=20)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7005, z145=600350, z146=600399, z147=90, z148=12, z149=20, z150=600030,
                             z151=600039)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6080():
    """Enemy _I that appears in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7008, z145=600500, z146=600549, z147=70, z148=13, z149=30, z150=600040,
                             z151=600049)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6090():
    """Enemy _J appearing in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z57=20, z58=600040, z59=600049, flag11=537010133, z60=7009, z61=13, z62=30)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7009, z145=600550, z146=600599, z147=90, z148=13, z149=30, z150=600040,
                             z151=600049)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6100():
    """Enemy _K that appears in a snowstorm"""
    """State 0,4: [Preset] Generation delay at appearance_SubState"""
    assert event_m50_37_x288(z57=50, z58=600040, z59=600049, flag11=537010132, z60=7010, z61=13, z62=30)
    """State 3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7010, z145=600600, z146=600649, z147=135, z148=13, z149=30, z150=600040,
                             z151=600049)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6120():
    """Enemy _M appearing in a snowstorm"""
    """State 0,3: [Preset] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x169(z144=7012, z145=600700, z146=600749, z147=60, z148=10, z149=10, z150=600010,
                             z151=600019)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6500():
    """Snowfield Enemy Defeat Count_A"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7000, z107=11, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6510():
    """Snowfield enemy defeat count _B"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7001, z107=11, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6540():
    """Snowfield enemy defeat count _E"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7004, z107=12, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6550():
    """Snowfield Enemy Defeat Count_F"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7005, z107=12, val1=20)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6580():
    """Snowfield enemy defeat count _I"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7008, z107=13, val1=30)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6590():
    """Snowfield enemy defeat count _J"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7009, z107=13, val1=30)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6600():
    """Snowfield enemy defeat count _K"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7010, z107=13, val1=30)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_6620():
    """Snowfield Enemy Defeat Count_M"""
    """State 0,3: [Preset] Snowfield enemy countdown_SubState"""
    call = event_m50_37_x225(z106=7012, z107=10, val1=10)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_7000():
    """Liberation of White Knight_1"""
    """State 0,2: [Preset] Liberation of White Knight_SubState"""
    assert event_m50_37_x95(z194=790, flag29=537000020, z195=5.5, z196=96880100, z197=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_7010():
    """Liberation of White Knight_2"""
    """State 0,2: [Preset] Liberation of White Knight_SubState"""
    assert event_m50_37_x95(z194=791, flag29=537000021, z195=5.5, z196=96880100, z197=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_7020():
    """Liberation of White Knight_3"""
    """State 0,2: [Preset] Liberation of White Knight_SubState"""
    assert event_m50_37_x95(z194=792, flag29=537000022, z195=5.5, z196=96880100, z197=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_8000():
    """Gate opened with lever_Castle"""
    """State 0,2: [Preset] Gate opened with lever _SubState"""
    assert event_m50_37_x204(z115=50372450, z116=50372550, z117=800000, z118=5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_8010():
    """Gate opened with lever_City B"""
    """State 0,2: [Preset] Gate opened with lever _SubState"""
    assert event_m50_37_x204(z115=50372650, z116=50372651, z117=801000, z118=5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_8020():
    """Gate opened with lever_Under Tiger Bridge"""
    """State 0,2: [Preset] Gate opened with lever _SubState"""
    assert event_m50_37_x204(z115=50372660, z116=50372661, z117=802000, z118=5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_9000():
    """The door opens when the lighthouse is on"""
    """State 0,2: [Preset] _SubState opens when the lighthouse is on"""
    assert (event_m50_37_x106(z185=50370700, z186=50370701, z187=50370702, z188=50370703, z189=50372001,
            z190=900000))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_10000():
    """Elevator_city B entrance"""
    """State 0,2: Has the initialization event been completed?"""
    assert EventEnded(10030) != 0
    """State 3: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_37_x10(z240=50372500, z241=1000000, z242=1000010, z243=50372401, z244=50372400)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_10010():
    """Elevator_city B entrance_on the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z273=50372500, z274=50372401, z275=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_10020():
    """Elevator_city B entrance_under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z273=50372500, z274=50372400, z275=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_10030():
    """Elevator_city B entrance_initialization"""
    """State 0,2: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m50_37_x23(z270=50372500, z271=40, flag36=537000040, z272=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_11000():
    """Elevator_city B exit"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_37_x10(z240=50372501, z241=1100000, z242=1100010, z243=50372403, z244=50372402)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_11010():
    """Elevator_city B exit_on lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z273=50372501, z274=50372403, z275=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_11020():
    """Elevator_city B exit_under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z273=50372501, z274=50372402, z275=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_12000():
    """Elevator_Mikome Altar"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m50_37_x10(z240=50372502, z241=1200000, z242=1200010, z243=50372405, z244=50372404)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_12010():
    """Elevator_Mikome Altar_Lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z273=50372502, z274=50372405, z275=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_12020():
    """Elevator_Mikome Altar_Under the lever"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m50_37_x15(z273=50372502, z274=50372404, z275=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_13000():
    """Return from the snowy field route"""
    """State 0,2: [Preset] Return from Boss Room_Yukihara_SubState"""
    assert event_m50_37_x343(z32=1300000, z33=50371190)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_14000():
    """Snowball"""
    """State 0,2: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371020, z257=150, z258=50371021)
    """State 3: [Preset] Snowball Gorokuro_SubState"""
    assert event_m50_37_x181(z134=50371020, z135=50371021, z136=1400000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15020():
    """Enemy who moves by absorbing Seoul _ Tiger Wall 1F_3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371173, z257=150, z258=50371146)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3011, z142=7, flag23=537020102, z143=50371146)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15030():
    """Enemy who moves by absorbing soul _ Tiger Wall 1F_4"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371172, z257=150, z258=50371145)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3010, z142=7, flag23=537020103, z143=50371145)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15100():
    """Enemy who moves by absorbing Seoul _ 1st half of Tiger Wall 3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371160, z257=150, z258=50371140)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3700, z142=7, flag23=537020104, z143=50371140)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15110():
    """Enemies that move by absorbing Seoul _ Tiger Wall 3F 1st Half_2"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371161, z257=150, z258=50371141)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3701, z142=7, flag23=537020105, z143=50371141)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15120():
    """Enemy who moves by absorbing soul_first half of Tiger Wall 3F_3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371168, z257=150, z258=50371142)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3702, z142=7, flag23=537020106, z143=50371142)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15210():
    """Enemies moving by absorbing Seoul _ Tiger Wall 3F Passage_2"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371170, z257=150, z258=50371143)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3911, z142=7, flag23=537020108, z143=50371143)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15220():
    """Enemy moving by absorbing Seoul _ Tiger Wall 3F Passage _3"""
    """State 0,3: [Lib] [Preset] OBJ attach_SubState"""
    assert event_m50_37_x42(z256=50371171, z257=150, z258=50371144)
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=3912, z142=7, flag23=537020109, z143=50371144)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15300():
    """Enemy moving by absorbing Seoul _ City B Exit_1"""
    """State 0,2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=5500, z142=9.5, flag23=537020110, z143=50371147)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_15310():
    """Enemy moving by absorbing Seoul _ City B Exit_2"""
    """State 0,2: [Preset] Enemy _SubState moving by absorbing soul"""
    assert event_m50_37_x173(z141=5501, z142=9.5, flag23=537020111, z143=50371148)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_16000():
    """Rejected by ice"""
    """State 0,2: [Preset] Rejection effect by ice_SubState"""
    assert event_m50_37_x177(z137=537020016, z138=1600000, z139=50371251, z140=50371252, flag22=537000006)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_17000():
    """To get the eyes of a shrine maiden"""
    """State 0,2: [Preset] _SubState to get Miko's eyes"""
    assert event_m50_37_x185(flag1=537000012, z2=50376550, z3=17000, z4=17000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_18000():
    """Zako's transparent management_A"""
    """State 0,3: [Preset] Zako's transparency management_SubState"""
    call = event_m50_37_x189(flag21=537000012, z128=537010065, z129=2620, z130=5, z131=15, z132=3, z133=5)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_18010():
    """Zako's transparency_A"""
    """State 0,3: [Preset] Transparent Zako_SubState"""
    call = event_m50_37_x194(z122=537000012, z123=537010065, z124=2620, z125=98830010, z126=98830000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_18100():
    """Zako's transparent management_B"""
    """State 0,3: [Preset] Zako's transparency management_SubState"""
    call = event_m50_37_x189(flag21=537000012, z128=537010066, z129=2621, z130=10, z131=20, z132=5, z133=10)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_18110():
    """Zako's transparency_B"""
    """State 0,3: [Preset] Transparent Zako_SubState"""
    call = event_m50_37_x194(z122=537000012, z123=537010066, z124=2621, z125=98830010, z126=98830000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_18200():
    """Zako's transparent management_C"""
    """State 0,3: [Preset] Zako's transparency management_SubState"""
    call = event_m50_37_x189(flag21=537000012, z128=537010067, z129=2700, z130=5, z131=15, z132=3, z133=5)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_18210():
    """Zako's transparency_C"""
    """State 0,3: [Preset] Transparent Zako_SubState"""
    call = event_m50_37_x194(z122=537000012, z123=537010067, z124=2700, z125=98830010, z126=98830000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_19000():
    """One-way door"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z281=0, z282=1101, z283=1900000, z284=537000048)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_19010():
    """One-way door_Ladder room"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z281=0, z282=1101, z283=1901000, z284=537000049)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_19020():
    """One-way door_Elevator room"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z281=0, z282=1101, z283=1902000, z284=537000044)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_19030():
    """One-way door_underpass"""
    """State 0,2: [Lib] Area specified door unlocked (text specified version that does not open) _SubState"""
    assert event_m50_37_x2(z281=0, z282=1101, z283=1903000, z284=537000043)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_20000():
    """Frozen treasure chest"""
    """State 0,2: [Preset] Frozen treasure chest_SubState"""
    assert event_m50_37_x229(z105=537000011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_20500():
    """Frozen mimic"""
    """State 0,2: [Preset] Frozen Mimic_Body_SubState"""
    assert event_m50_37_x261(z78=50373001, z79=537000070, z80=2050000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_20600():
    """Frozen Mimic_No body"""
    """State 0,2: [Preset] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x265(z75=537000071, z76=50375720, z77=50371620)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_21000():
    """NPC mimicry control_map"""
    """State 0,3: [Preset] NPC mimic control_map_SubState"""
    call = event_m50_37_x235(z100=762, z101=537020063, z102=60375000, z103=60375001)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_21010():
    """NPC mimic control_character"""
    """State 0,2: [Preset] NPC Mimicry Control_Character_SubState"""
    assert event_m50_37_x239(z97=537020063, z98=60375001, z99=762)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_22000():
    """[Insect key] For recovery hot spring"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m50_37_x24(z265=50372900)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_22010():
    """[Insect key activation] Recovery hot spring"""
    """State 0,2: [Lib] [Preset] Recovery Fountain_SubState"""
    assert event_m50_37_x34(z261=50372900, z262=30, z263=240, z264=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_23000():
    """[Insect key] Face SFX hidden door"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m50_37_x24(z265=50372800)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_23010():
    """[Insect key activation] Face SFX hidden door"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m50_37_x38(z259=50372800, val3=50370000, z260=0.6, val4=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_23020():
    """Frozen insect key_for face SFX hidden door"""
    """State 0,2: [Preset] Frozen Bug Key_SubState"""
    assert event_m50_37_x269(z73=50372802, z74=50372800)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_23030():
    """Change the navigation mesh of the face SFX hidden door"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50372801, z252=20, z253=2303000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_24000():
    """Lever operated by lever"""
    """State 0,2: [Preset] Transporter operated by lever_SubState"""
    assert event_m50_37_x284(z63=50372600, z64=50372601, z65=2400000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_25000():
    """Boss: Tiger Battle"""
    """State 0,2: [Preset] Tiger Battle_Start_SubState"""
    assert (event_m50_37_x161(flag24=537000081, z156=504, z157=5037030, z158=537020080, z159=5, z160=537020083,
            z161=2500000))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_25020():
    """Tiger cry production"""
    """State 0,2: [Preset] Tiger cry production_SubState"""
    assert event_m50_37_x253(z82=25020, z83=1, z84=2502000, flag14=537000018)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_25050():
    """NPC gesture management"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_37_x217(flag17=537000081, z111=907, z112=537020084)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_26000():
    """Transparent management of tigers"""
    """State 0,3: [Preset] Tiger transparency management_SubState"""
    call = event_m50_37_x146(flag25=537000012, z172=537010013, z173=907, flag26=537000081, z174=537020080)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_26010():
    """Tiger transparency"""
    """State 0,3: [Preset] Tiger transparency_SubState"""
    call = event_m50_37_x147(z165=537000012, z166=537010013, z167=907, z168=96790010, z169=96790000,
                             z170=96790020)
    if call.Get() == 0:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_27000():
    """Broken tiger statue_right 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371370, z252=20, z253=2700000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27010():
    """Broken tiger statue_right 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371371, z252=20, z253=2701000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27020():
    """Broken Tiger Statue_Right 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371372, z252=20, z253=2702000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27030():
    """Broken Tiger Statue_Right 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371373, z252=20, z253=2703000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27040():
    """Broken tiger statue_Right 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371374, z252=20, z253=2704000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27100():
    """A stone statue that breaks a tiger battle_left 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371385, z252=20, z253=2710000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27110():
    """Broken tiger statue_left 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371386, z252=20, z253=2711000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27120():
    """Broken tiger statue_Left 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371387, z252=20, z253=2712000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27130():
    """Broken tiger statue_Left 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371388, z252=20, z253=2713000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_27140():
    """Broken tiger statue_Left 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371389, z252=20, z253=2714000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_30000():
    """Boss: Ice King"""
    """State 0,2: [Preset] Ice King Battle_SubState"""
    assert event_m50_37_x142(flag5=537000086, z29=501, z30=5037000, z31=537020085)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_30020():
    """Production sound when falling"""
    """State 0,2: [Preset] Falling sound_SubState"""
    assert event_m50_37_x249(z85=3002000, z86=30020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_30040():
    """White knight falling with PC following"""
    """State 0,2: [Preset] Falling white knight by PC tracking_SubState"""
    assert event_m50_37_x273(z71=3004000, z72=537020024, flag12=537000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_30050():
    """NPC Gesture Management_Ice King"""
    """State 0,2: [Preset] NPC Gesture Management_SubState"""
    assert event_m50_37_x217(flag17=537000086, z111=908, z112=537020087)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_30070():
    """The crown that appears when you destroy a boss"""
    """State 0,3: [Preset] Crown _SubState that appears when a boss is destroyed"""
    # action:5310:"A faint heat lingers in the ancient crown"
    call = event_m50_37_x350(z23=50371570, flag4=537000002, z24=537000086, z25=5, action1=5310)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_31000():
    """Return from the boss room"""
    """State 0,2: [Preset] Return from Boss Room_SubState"""
    assert event_m50_37_x103(z113=3100010, flag18=537000086, z114=50371001, flag19=537000002) == 0
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_31050():
    """Return from Boss Room_White Knight_1"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z26=794, z27=5037000, z28=537020025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_31060():
    """Return from Boss Room_White Knight_2"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z26=795, z27=5037000, z28=537020025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_31070():
    """Return from Boss Room_White Knight_3"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z26=796, z27=5037000, z28=537020025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_31080():
    """Return from Boss Room_White Knight_4"""
    """State 0,2: [Preset] Return from the White Knight Boss Room_SubState"""
    assert event_m50_37_x328(z26=797, z27=5037000, z28=537020025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_31100():
    """White knight inside ice after boss battle removed"""
    """State 0,2: [Preset] Delete the white knight inside the ice after the boss battle_SubState"""
    assert event_m50_37_x382(z7=537020175)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32000():
    """White Knight: Sealing Order and Sealing Direction"""
    """State 0,3: [Preset] Sealing instruction _SubState"""
    assert event_m50_37_x241(z94=40, z95=10, z96=1)
    """State 2: [Preset] Sealing production_SubState"""
    assert (event_m50_37_x245(z87=794, z88=795, z89=796, z90=797, flag15=537020035, z91=15, z92=50371122,
            z93=50371552))
    """State 5: [Preset] Sealing instruction_2_SubState"""
    assert event_m50_37_x241(z94=90, z95=10, z96=2)
    """State 4: [Preset] Sealing production_2_SubState"""
    assert (event_m50_37_x245(z87=794, z88=795, z89=796, z90=797, flag15=537020036, z91=15, z92=50371120,
            z93=50371550))
    """State 7: [Preset] Sealing instruction_3_SubState"""
    assert event_m50_37_x241(z94=150, z95=10, z96=3)
    """State 6: [Preset] Sealing production_3_SubState"""
    assert (event_m50_37_x245(z87=794, z88=795, z89=796, z90=797, flag15=537020037, z91=0, z92=50371121,
            z93=50371551))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32010():
    """Change generator navigator mesh"""
    """State 0,3: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m50_37_x59(z230=3201000, z231=2, z232=0, flag34=537020035, flag35=0)
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    event_m50_37_x43(z251=50371122, z252=20, z253=3201000, z254=2, z255=0)
    Quit()

def event_m50_37_32020():
    """Change generator navigator mesh"""
    """State 0,3: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m50_37_x59(z230=3202000, z231=2, z232=0, flag34=537020036, flag35=0)
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    event_m50_37_x43(z251=50371120, z252=20, z253=3202000, z254=2, z255=0)
    Quit()

def event_m50_37_32030():
    """Change generator navigator mesh"""
    """State 0,3: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m50_37_x59(z230=3203000, z231=2, z232=0, flag34=537020037, flag35=0)
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    event_m50_37_x43(z251=50371121, z252=20, z253=3203000, z254=2, z255=0)
    Quit()

def event_m50_37_32100():
    """White Knight's profession_1"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z21=794, z22=537000026, flag3=537000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32110():
    """White Knight's profession_2"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z21=795, z22=537000027, flag3=537000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32120():
    """White Knight's profession_3"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z21=796, z22=537000028, flag3=537000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32130():
    """White Knight's profession_4"""
    """State 0,2: [Preset] White Knight's profession_SubState"""
    assert event_m50_37_x364(z21=797, z22=537000029, flag3=537000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32200():
    """Instant death damage inside ice _A"""
    """State 0,2: [Preset] Instant death damage inside ice _SubState"""
    assert event_m50_37_x386(z5=3220000, z6=50371122)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32210():
    """Instant death damage inside ice_B"""
    """State 0,2: [Preset] Instant death damage inside ice _SubState"""
    assert event_m50_37_x386(z5=3221000, z6=50371120)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_32220():
    """Instant death damage inside ice _C"""
    """State 0,2: [Preset] Instant death damage inside ice _SubState"""
    assert event_m50_37_x386(z5=3222000, z6=50371121)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_33030():
    """Black Knight: Defeat count _4"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4110, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33040():
    """Black Knight: Defeat count _5"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4111, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33050():
    """Black Knight: Defeat count _6"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4112, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33060():
    """Black Knight: Defeat count _7"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4113, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33070():
    """Black Knight: Defeat count _8"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4114, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33080():
    """Black Knight: Defeat count _9"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4115, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33090():
    """Black Knight: Defeat count _10"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4116, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33100():
    """Black Knight: Defeat count _11"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4117, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33110():
    """Black Knight: Defeat count _12"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4118, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33120():
    """Black Knight: Defeat Count Count_13"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4119, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33130():
    """Black Knight: Defeat count _14"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4120, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33140():
    """Black Knight: Defeat count _15"""
    """State 0,3: [Preset] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x198(z119=4121, z120=1, flag20=537000086)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_33500():
    """Black Knight: Defeat count reset"""
    """State 0,2: [Preset] Black Knight: Defeat count reset_SubState"""
    assert event_m50_37_x203()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_34000():
    """Black Knight: Generation Generator_A"""
    """State 0,3: [Preset] Black Knight: Generator Generator_SubState"""
    call = event_m50_37_x213(flag2=537020035, z14=12, z15=4110, z16=4111, z17=4112, z18=4113, z19=13,
                             z20=14)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_34010():
    """Black Knight: Generator Generator_B"""
    """State 0,3: [Preset] Black Knight: Generator Generator_SubState"""
    call = event_m50_37_x213(flag2=537020036, z14=13, z15=4114, z16=4115, z17=4116, z18=4117, z19=12,
                             z20=14)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_34020():
    """Black Knight: Generator Generator_C"""
    """State 0,3: [Preset] Black Knight: Generator Generator_SubState"""
    call = event_m50_37_x213(flag2=537020037, z14=14, z15=4118, z16=4119, z17=4120, z18=4121, z19=12,
                             z20=13)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_34050():
    """Black Knight Generator started operation"""
    """State 0,2: [Preset] Black Knight Generator starts operation_SubState"""
    assert event_m50_37_x374(z9=3400000, z10=537020032, z11=0, z12=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_35000():
    """Boss: Black Tiger Battle"""
    """State 0,3: [Preset] Black Tiger Battle_SubState"""
    assert (event_m50_37_x302(flag9=537000091, z49=3500000, z50=3500000, z51=503, z52=5037010, mode1=0,
            z53=537020090, z54=537020093))
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Lib] [Preset] Boss Battle Start_SubState"""
    event_m50_37_x3(flag37=537000091, z276=3500000, z277=3500000, z278=503, z279=5037010, z280=537020090,
                    mode5=0)
    Quit()

def event_m50_37_35010():
    """Boss: Black Tiger Battle _ 2nd Tiger Operation"""
    """State 0,2: [Preset] Second tiger in operation _SubState"""
    assert event_m50_37_x292(flag10=537000091, z55=5037010, z56=537020093)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_35050():
    """NPC Gesture Management_Black Tiger"""
    """State 0,2: [Preset] NPC Gesture Management_2 Body Version_SubState"""
    assert event_m50_37_x219(flag16=537000091, z108=537020092, z109=909, z110=910)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_40000():
    """Hidden door_castle wall_navigation mesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50372851, z252=20, z253=4000000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_40010():
    """Hidden door_Cave_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50372850, z252=20, z253=4001000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41000():
    """Navimesh change of ice seal _ ice tower"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371223, z252=20, z253=4100000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41010():
    """Change the Navimesh of Ice Seal _Barista Crossroads"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371222, z252=20, z253=4101000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41020():
    """Navi mesh change of ice seal"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371224, z252=20, z253=4102000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41030():
    """Change Navimesh of ice seal_alley right"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371210, z252=20, z253=4103000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41040():
    """Change the Navimesh of the ice seal_Left alley"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371211, z252=20, z253=4104000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41050():
    """Navimesh change of ice seal_fountain plaza_1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371204, z252=20, z253=4105000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41060():
    """Navimesh change of ice seal_fountain plaza_2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371203, z252=20, z253=4106000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41070():
    """Changed the Navimesh of the ice seal_Fountain Square_3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371201, z252=20, z253=4107000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41080():
    """Change the Navimesh of Ice Seal_Fountain Square_4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371202, z252=20, z253=4108000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41090():
    """Navimesh change of ice seal _ Cathedral treasure chest"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371700, z252=20, z253=4109000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_41100():
    """Navimesh change of ice seal_golem passage"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50373110, z252=20, z253=4110000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42000():
    """Enemy moving by absorbing soul_Navigation mesh change_Treasure 1A"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371140, z252=20, z253=4200000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42010():
    """Enemy moving by absorbing soul_Navimesh change_Treasure 1B"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371141, z252=20, z253=4201000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42020():
    """Enemy moving with soul absorption_Navimesh change_Treasure 1C"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371142, z252=20, z253=4202000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42100():
    """Enemy moving with soul absorption_Navigation mesh change_Aisle 1A"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371170, z252=20, z253=4210000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42110():
    """Enemy moving with soul absorption_Navimesh change_Aisle 1B"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371171, z252=20, z253=4211000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42200():
    """Enemy moving with soul absorption_Navigation mesh change_Room 1A"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371172, z252=20, z253=4220000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_42210():
    """Enemy moving by absorbing soul_Navigation mesh change_Room 1B"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m50_37_x43(z251=50371173, z252=20, z253=4221000, z254=0, z255=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43020():
    """Enemy who moves by absorbing soul_character_tiger wall 1F_3"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43030():
    """Enemies moving by absorbing soul_character_tiger wall 1F_4"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43100():
    """Enemy who moves by absorbing soul _Chara_Tiger Wall 3F 1st Half_1"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43110():
    """Enemies moving by absorbing soul_Chara_Tiger Wall 3F 1st Half_2"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43120():
    """Enemy who moves by absorbing soul_character_tiger castle wall 3F first half_3"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43210():
    """Enemy who moves by absorbing soul_character_tiger castle wall 3F passage_2"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43220():
    """Enemies that move by absorbing Seoul_Chara_Tiger Wall 3F Passage_3"""
    """State 0,2: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_43300():
    """Enemy who moves by absorbing Seoul _ Character _ City B Exit_1"""
    """State 0,3: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    event_m50_37_x173(z141=5500, z142=4.5, flag23=537020110, z143=0)
    Quit()

def event_m50_37_43310():
    """Enemies moving by absorbing Seoul_Character_Exit B"""
    """State 0,3: [Preset] Enemies that move by absorbing souls_Character_SubState"""
    assert event_m50_37_x310()
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Preset] Enemy _SubState moving by absorbing soul"""
    event_m50_37_x173(z141=5501, z142=4.5, flag23=537020111, z143=0)
    Quit()

def event_m50_37_44000():
    """Bhaksta launch"""
    """State 0,3: [Preset] Samurai Warrior Bakusta Launch_SubState"""
    call = event_m50_37_x318(z44=50372650, z45=537020003, z46=537020004)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_49000():
    """Create filter condition"""
    """State 0,2: [Preset] Filter condition registration_SubState"""
    assert event_m50_37_x341()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_49010():
    """Filter condition judgment_DLC possession"""
    """State 0,2: [Preset] Filter condition judgment_DLC possession_SubState"""
    assert event_m50_37_x332(z41=537020050, z42=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_49020():
    """Filter condition judgment_First Tiger Battle"""
    """State 0,2: [Preset] Filter Condition Judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x336(z38=537020051, z39=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_49030():
    """Filter condition judgment_Rematch tiger battle"""
    """State 0,2: [Preset] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x340(z34=537020052, z35=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_51000():
    """Start from the Forest of the Shadow"""
    """State 0,1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_52000():
    """Return to the Forest of Shadow"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m50_37_x67(z222=50371000, z223=10320000, z224=5200000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_53000():
    """Door that opens with DLC purchase"""
    """State 0,3: [Preset] Door that opens with DLC purchase_SubState"""
    call = event_m50_37_x108(z181=50370400, z182=5300010, z183=5300000, z184=5300001)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m50_37_59000():
    """Inter-DLC event"""
    """State 0,2: [Preset] Inter-DLC event"""
    assert event_m50_37_x306(flag8=103400, z48=5320)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_80000():
    """Regenerative fire 01_Start point_37650"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z237=5037000, z238=5037099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_82000():
    """Regeneration of fire 03_city area A_37660"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z237=5037200, z238=5037299)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_83000():
    """Reproduction of fire 04_city B in the middle_37665"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z237=5037300, z238=5037399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_84000():
    """Rebirth of Fire 05_Cathedral_37670"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z237=5037400, z238=5037499)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_85000():
    """Rebirth of Fire 06_Snowfield_37675"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z237=5037500, z238=5037599)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_87000():
    """Rebirth Fire 08_Tora Hashishita_37685"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m50_37_x54(z237=5037700, z238=5037799)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_89000():
    """Shop lineup expansion_tiger"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_37_x69(z221=101071, flag33=101221)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_89010():
    """Shop lineup expansion_Black Tiger"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_37_x69(z221=101072, flag33=101222)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_89020():
    """Shop Lineup Expansion_Ice King"""
    """State 0,2: [Lib] [DLC] [Preset] Shop lineup_1 lap_SubState"""
    assert event_m50_37_x69(z221=101070, flag33=101223)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_x0(z289=0, z290=0, z223=_, z32=_):
    """[Lib] Warp between maps after poly play
    z289: Pre-warp poly play ID
    z290: Poly Play ID after Warp
    z223: Map ID
    z32: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z289, z290, z223, z32, 0)
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
    event_m50_37_x50(z239=771)
    Quit()

def event_m50_37_x1(z285=1005, z286=1105, z287=52500000, z288=537000047):
    """[Lib] Item specified door unlocking_2
    z285: Text ID when opened
    z286: Text ID when not opened
    z287: item
    z288: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z287, z285, z286, z288, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x2(z281=0, z282=1101, z283=_, z284=_):
    """[Lib] Area specified door unlocked (text specified version not opened) _2
    z281: Text ID when opened
    z282: Text ID when not opened
    z283: Point ID
    z284: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z283, 0, z281, z282, z284, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x3(flag37=537000091, z276=3500000, z277=3500000, z278=503, z279=5037010, z280=537020090,
                    mode5=0):
    """[Lib] [Preset] Boss Battle Start
    flag37: Boss destruction flag
    z276: Start point ID
    z277: End point ID
    z278: Sound ID
    z279: Boss Battle ID
    z280: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m50_37_x4(flag37=flag37)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m50_37_x5(z276=z276, z277=z277)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m50_37_x6(z278=z278, z279=z279, z280=z280)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m50_37_x7()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m50_37_x8(z279=z279)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m50_37_x9(z278=z278, z279=z279, z280=z280, mode5=mode5)
    """State 7: End state"""
    return 0

def event_m50_37_x4(flag37=537000091):
    """[Reproduction] Boss Battle_Start
    flag37: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag37) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_37_x5(z276=3500000, z277=3500000):
    """[Condition] Boss Battle_Start
    z276: Start point ID
    z277: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z276, z277, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z276, z277, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x6(z278=503, z279=5037010, z280=537020090):
    """[Execution] Boss Battle_Start
    z278: Sound ID
    z279: Boss Battle ID
    z280: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z278)
    """State 1: Boss battle start notification"""
    StartBossFight(z279)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z280, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x7():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x8(z279=5037010):
    """[Condition] Boss Battle_End Judgment
    z279: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z279, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x9(z278=503, z279=5037010, z280=537020090, mode5=0):
    """[Execute] Boss Battle_End
    z278: Sound ID
    z279: Boss Battle ID
    z280: Other flags for logic
    mode5: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z280, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z279)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode5) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z278)
    """State 5: End state"""
    return 0

def event_m50_37_100010():
    """White Spirit sign display_White Tiger 01"""
    """State 0,1: Miko's Eye Judgment"""
    assert GetEventFlag(537000012) != 0
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z239=772)
    Quit()

def event_m50_37_x10(z240=_, z241=_, z242=_, z243=_, z244=_):
    """[Lib] [Preset] Elevator
    z240: OBJ instance ID of the elevator
    z241: On elevator point ID_
    z242: Elevator point ID_below
    z243: Upper lever OBJ instance ID
    z244: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m50_37_x11()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m50_37_x12(z240=z240, z241=z241, z242=z242, z243=z243, z244=z244)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m50_37_x49(z240=z240, z242=z242)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m50_37_x48(z240=z240, z241=z241)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m50_37_x13(z240=z240, z241=z241)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m50_37_x14(z240=z240, z242=z242)
    """State 7: End state"""
    return 0

def event_m50_37_100011():
    """White spirit sign display_White Tiger 02"""
    """State 0,1: Miko's Eye Judgment"""
    assert GetEventFlag(537000012) != 0
    """State 2: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z239=773)
    Quit()

def event_m50_37_x11():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x12(z240=_, z241=_, z242=_, z243=_, z244=_):
    """[Condition] Elevator
    z240: Elevator OBJ instance ID
    z241: On elevator point ID_
    z242: Elevator point ID_below
    z243: Upper lever OBJ instance ID
    z244: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z240, 10, 0)
    CompareObjState(1, z240, 40, 0)
    CompareObjState(2, z240, 80, 0)
    CompareObjState(2, z240, 41, 0)
    CompareObjState(3, z240, 70, 0)
    CompareObjState(3, z240, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z242, z242, 1)
        CompareObjState(0, z243, 74, 0)
        CompareObjState(0, z243, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z241, z241, 1)
        CompareObjState(0, z244, 74, 0)
        CompareObjState(0, z244, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m50_37_x13(z240=_, z241=_):
    """[Execution] Elevator_Rise
    z240: Elevator OBJ instance ID
    z241: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z240, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z240, 30, 0)
    IsPlayerInsidePoint(8, z241, z241, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z240, 71)
    assert CompareObjStateId(z240, 40, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x14(z240=_, z242=_):
    """[Execution] Elevator_Descent
    z240: Elevator OBJ instance ID
    z242: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z240, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z240, 41, 0)
    IsPlayerInsidePoint(8, z242, z242, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z240, 81)
    assert CompareObjStateId(z240, 10, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x15(z273=_, z274=_, z275=_):
    """[Lib] [Preset] Elevator lever
    z273: OBJ instance ID of the elevator
    z274: Lever OBJ instance ID
    z275: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m50_37_x16()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m50_37_x17(z273=z273, z274=z274, z275=z275)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m50_37_x18(z273=z273, z274=z274, z275=z275)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m50_37_x19(z273=z273, z274=z274, z275=z275)
    """State 5: Rerun"""
    return 0

def event_m50_37_x16():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x17(z273=_, z274=_, z275=_):
    """[Condition] Elevator lever_use judgment
    z273: OBJ instance ID of the elevator
    z274: Lever OBJ instance ID
    z275: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z273, z275, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m50_37_x18(z273=_, z274=_, z275=_):
    """[Execution] Elevator lever_Key guide valid
    z273: OBJ instance ID of the elevator
    z274: Lever OBJ instance ID
    z275: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z274, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z273, z275, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x19(z273=_, z274=_, z275=_):
    """[Execute] Elevator lever_key guide disabled
    z273: OBJ instance ID of the elevator
    z274: Lever OBJ instance ID
    z275: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z274, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z273, z275, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x20(flag36=537000040):
    """[Lib] [Reproduction] Elevator_Initialization
    flag36: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag36) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m50_37_100021():
    """White spirit sign display_Yukihara 01"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z239=775)
    Quit()

def event_m50_37_x21():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m50_37_x22(z270=50372500, z271=40, flag36=537000040, z272=40):
    """[Lib] [Execution] Elevator_Initialization
    z270: Elevator OBJ instance ID
    z271: Initial position OBJ state ID
    flag36: Initialization completion flag
    z272: [Preset] 棺 桶 Bobsleigh_Initialization_SubState
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z270, z271)
    assert CompareObjStateId(z270, z272, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag36, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x23(z270=50372500, z271=40, flag36=537000040, z272=40):
    """[Lib] [Preset] Elevator_Initialization
    z270: Elevator OBJ instance ID
    z271: Initial position OBJ state ID
    flag36: Initialization completion flag
    z272: [Preset] 棺 桶 Bobsleigh_Initialization_SubState
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m50_37_x20(flag36=flag36)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m50_37_x21()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m50_37_x22(z270=z270, z271=z271, flag36=flag36, z272=z272)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m50_37_x24(z265=_):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z265: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m50_37_x25(z265=z265)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m50_37_x32(z265=z265)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m50_37_x33()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m50_37_x26(z265=z265, mode4=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m50_37_x27(z265=z265, z267=38, z268=3, z269=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m50_37_x28(z265=z265, z266=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m50_37_x25(z265=_):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z265: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z265, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z265, 10)
        assert CompareObjStateId(z265, 10, 0)
    elif CompareObjStateId(z265, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z265, 74, 1) and CompareObjStateId(z265, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m50_37_x26(z265=_, mode4=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z265: Object instance ID
    mode4: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z265)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode4) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m50_37_x27(z265=_, z267=38, z268=3, z269=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z265: Object instance ID
    z267: Key guide type
    z268: Event action
    z269: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z265, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z265, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z265, 30)
        assert CompareObjStateId(z265, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z265, z267, z268)
        assert PlayerIsInEventAction(z268) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z268, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z265, 74, 0)
        CompareObjState(1, z265, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z269)
            assert CompareObjStateId(z265, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z265, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m50_37_x28(z265=_, z266=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z265: Object instance ID
    z266: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z265, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m50_37_x29(z261=50372900, z262=30, z263=240, z264=1):
    """[Reproduction] Spring of recovery
    z261: OBJ instance ID of the bug key
    z262: Hit group ID
    z263: Replacement GMID
    z264: Switching GM slot
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z261, 20, 0):
        """State 2: Water OBJ: OBJ state transition: 20"""
        ChangeOwnObjState(20)
        """State 3: Enable recovery"""
        SetGroundMaterial(z262, z263, z264)
        """State 4: Activated"""
        return 0
    else:
        """State 5: Not running"""
        return 1

def event_m50_37_x30(z261=50372900):
    """[Condition] Spring of recovery
    z261: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z261, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x31(z262=30, z263=240, z264=1):
    """[Execution] Recovery Fountain
    z262: Hit group ID
    z263: Replacement GMID
    z264: Switching GM slot
    """
    """State 0,1: Water OBJ: OBJ state transition: 70"""
    ChangeOwnObjState(70)
    assert (GetStateTime() > 1) != 0
    """State 2: Enable recovery"""
    SetGroundMaterial(z262, z263, z264)
    """State 3: Waiting for the end of anime"""
    assert CompareOwnObjStateId(20, 0)
    """State 4: End state"""
    return 0

def event_m50_37_x32(z265=_):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z265: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z265, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x33():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x34(z261=50372900, z262=30, z263=240, z264=1):
    """[Lib] [Preset] Recovery Fountain
    z261: OBJ instance ID of the bug key
    z262: Hit group ID
    z263: Replacement GMID
    z264: Switching GM slot
    """
    """State 0,1: [Reproduction] Recovery Fountain_SubState"""
    call = event_m50_37_x29(z261=z261, z262=z262, z263=z263, z264=z264)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Condition] Recovery Fountain_SubState"""
        assert event_m50_37_x30(z261=z261)
        """State 2: [Execution] Recovery Fountain_SubState"""
        assert event_m50_37_x31(z262=z262, z263=z263, z264=z264)
    """State 4: End state"""
    return 0

def event_m50_37_x35(z259=50372800, val3=50370000):
    """[Reproduction] Hidden door 1_face SFX
    z259: OBJ instance ID of the bug key
    val3: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z259, 20, 0):
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

def event_m50_37_x36(z259=50372800):
    """[Conditions] Hidden door 1_Face SFX
    z259: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z259, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x37(z259=50372800, val3=50370000, z260=0.6, val4=1.5):
    """[Execution] Hidden door 1_Face SFX
    z259: OBJ instance ID of the bug key
    val3: Event light ID
    z260: Light fade time
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
        SetPointLightEnabled(val3, 1, z260)
        assert (GetStateTime() > val4) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m50_37_x38(z259=50372800, val3=50370000, z260=0.6, val4=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z259: OBJ instance ID of the bug key
    val3: Event light ID
    z260: Light fade time
    val4: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m50_37_x35(z259=z259, val3=val3)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m50_37_x36(z259=z259)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m50_37_x37(z259=z259, val3=val3, z260=z260, val4=val4)
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
    event_m50_37_x55(z233=537000086, z234=102498, z235=204, z236=7520)
    Quit()

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
    event_m50_37_x47(z245=102502, z246=770, z247=104190, z248=61, z249=103690, z250=-1)
    Quit()

def event_m50_37_x41(z256=_, z257=150, z258=_):
    """[Lib] [execute] OBJ attach
    z256: Parent OBJ instance ID
    z257: Parent Damipoli ID
    z258: Child OBJ instance ID
    """
    """State 0,1: OBJ attach"""
    AttachObjToObj(z256, z257, z258)
    """State 2: End state"""
    return 0

def event_m50_37_x42(z256=_, z257=150, z258=_):
    """[Lib] [Preset] OBJ attach
    z256: Parent OBJ instance ID
    z257: Parent Damipoli ID
    z258: Child OBJ instance ID
    """
    """State 0,1: [Lib] [Reproduction] OBJ attach_empty_SubState"""
    assert event_m50_37_x39()
    """State 3: [Lib] [Condition] OBJ attach_empty_SubState"""
    assert event_m50_37_x40()
    """State 2: [Lib] [Execution] OBJ attach_SubState"""
    assert event_m50_37_x41(z256=z256, z257=z257, z258=z258)
    """State 4: End state"""
    return 0

def event_m50_37_x43(z251=_, z252=20, z253=_, z254=_, z255=_):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z251: Object instance ID
    z252: OBJ state ID
    z253: Navimesh switching point ID
    z254: Additional attributes
    z255: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m50_37_x44(z251=z251, z252=z252, z253=z253, z255=z255, z254=z254)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m50_37_x45(z251=z251, z252=z252, z253=z253)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m50_37_x46(z251=z251, z252=z252, z253=z253, z254=z254, z255=z255)
    """State 4: End state"""
    return 0

def event_m50_37_x44(z251=_, z252=20, z253=_, z255=_, z254=_):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z251: Target OBJ instance ID
    z252: Target OBJ state ID
    z253: Navimesh switching point ID
    z255: Additional attributes
    z254: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z251, z252, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z253, z255)
        DeleteNavimeshAttribute(z253, z254)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m50_37_x45(z251=_, z252=20, z253=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z251: Target OBJ instance ID
    z252: Target OBJ state ID
    z253: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z251, z252, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x46(z251=_, z252=20, z253=_, z254=_, z255=_):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z251: Target OBJ instance ID
    z252: Target OBJ state ID
    z253: Navimesh switching point ID
    z254: Additional attributes
    z255: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z253, z254)
    DeleteNavimeshAttribute(z253, z255)
    """State 2: End state"""
    return 0

def event_m50_37_x47(z245=102502, z246=770, z247=104190, z248=61, z249=103690, z250=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z245: White Phantom can appear: Global event flag
    z246: White Phantom: Generator ID
    z247: Death: Global event flag
    z248: Body: Generator group ID
    z249: Hostile: Global event flag
    z250: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z246)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z247, 1)
        CompareEventFlag(1, z249, 1)
        CompareEventFlag(2, z245, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z246)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z247, 1)
            CompareEventFlag(1, z249, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z246)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z247, 1)
            CompareEventFlag(1, z249, 1)
            HasNpcPhantomSpawned(2, z246, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z248, 0)
                HasNpcPhantomSpawned(0, z246, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z246)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m50_37_x48(z240=_, z241=_):
    """[Execution] Elevator_Return switch after lift
    z240: Elevator OBJ instance ID
    z241: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z240, 30, 0)
    IsPlayerInsidePoint(8, z241, z241, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z240, 71)
    assert CompareObjStateId(z240, 40, 0)
    """State 3: End state"""
    return 0

def event_m50_37_x49(z240=_, z242=_):
    """[Execution] Elevator_Return switch after descending
    z240: Elevator OBJ instance ID
    z242: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z240, 41, 0)
    IsPlayerInsidePoint(8, z242, z242, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z240, 81)
    assert CompareObjStateId(z240, 10, 0)
    """State 3: End state"""
    return 0

def event_m50_37_100050():
    """White spirit sign display_Yukihara_Durahan"""
    """State 0,1: [Lib] NPC White Phantom Appearance: General: Single_SubState"""
    event_m50_37_x60(z225=102000, z226=774, z227=104000, z228=103500, z229=-1)
    Quit()

def event_m50_37_x50(z239=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z239: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z239)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m50_37_x51():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x52(z237=_, z238=_):
    """[Lib] [execute] Rebirth fire
    z237: Flag start ID
    z238: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z237, z238, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x53():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x54(z237=_, z238=_):
    """[Lib] [Preset] Rebirth
    z237: Flag start ID
    z238: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m50_37_x51()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m50_37_x53()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m50_37_x52(z237=z237, z238=z238)
    """State 4: End state"""
    return 0

def event_m50_37_x55(z233=537000086, z234=102498, z235=204, z236=7520):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z233: Defeat Boss 1: Area and other flags
    z234: Summon Achievement: Global Event Flag
    z235: Summon achievement count: global variable
    z236: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z234, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z233, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z235, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z235, NpcInfoValue(z236, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z234, 1)
                CompareEventFlag(0, z234, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m50_37_x56(flag34=_, flag35=0, z232=0, z231=2, z230=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    flag34: Other flags
    flag35: Global flag
    z232: Additional attributes
    z231: Delete attribute
    z230: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(flag34) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(flag35) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z230, z232)
        DeleteNavimeshAttribute(z230, z231)
        """State 3: Flag OFF"""
        return 0

def event_m50_37_x57(flag34=_, flag35=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    flag34: Other flags
    flag35: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, flag34, 1)
    CompareEventFlag(0, flag35, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m50_37_x58(z230=_, z231=2, z232=0):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z230: Navimesh switching point ID
    z231: Additional attributes
    z232: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z230, z231)
    DeleteNavimeshAttribute(z230, z232)
    """State 2: End state"""
    return 0

def event_m50_37_x59(z230=_, z231=2, z232=0, flag34=_, flag35=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z230: Navimesh switching point ID
    z231: Additional attributes
    z232: Delete attribute
    flag34: Other flags
    flag35: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m50_37_x56(flag34=flag34, flag35=flag35, z232=z232, z231=z231, z230=z230)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m50_37_x57(flag34=flag34, flag35=flag35)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m50_37_x58(z230=z230, z231=z231, z232=z232)
    """State 4: End state"""
    return 0

def event_m50_37_100060():
    """White spirit sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z239=777)
    Quit()

def event_m50_37_x60(z225=102000, z226=774, z227=104000, z228=103500, z229=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Single
    z225: White Phantom can appear: Global event flag
    z226: White Phantom: Generator ID
    z227: Death: Global event flag
    z228: Hostile: Global event flag
    z229: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z226)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z227, 1)
        CompareEventFlag(1, z228, 1)
        CompareEventFlag(2, z225, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z226)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z227, 1)
            CompareEventFlag(1, z228, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z226)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z227, 1)
            CompareEventFlag(1, z228, 1)
            HasNpcPhantomSpawned(2, z226, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                HasNpcPhantomSpawned(0, z226, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z226)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m50_37_x61(flag33=_):
    """[Lib] [Reproduction] Shop Lineup
    flag33: Global flag for shop
    """
    """State 0,1: Is the shop flag already ON?"""
    if GetEventFlag(flag33) != 1:
        """State 2: OFF: Judgment"""
        return 0
    else:
        """State 3: ON: End"""
        return 1

def event_m50_37_x62(flag33=_):
    """[Lib] [execution] shop lineup
    flag33: Global flag for shop
    """
    """State 0,1: Shop flag ON"""
    SetEventFlag(flag33, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x63(z222=50371000):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z222: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z222)
    """State 2: End state"""
    return 0

def event_m50_37_x64(z222=50371000):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z222: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z222, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z222)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m50_37_x65(z222=50371000, z223=10320000, z224=5200000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z222: Warp OBJ instance ID
    z223: Map ID
    z224: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z222, 1)
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
        assert event_m50_37_x0(z289=0, z290=0, z223=z223, z32=z224)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m50_37_x66(z222=50371000):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z222: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z222, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x67(z222=50371000, z223=10320000, z224=5200000):
    """[Lib] [Preset] Warp move between main part and DLC
    z222: Warp OBJ instance ID
    z223: Map ID
    z224: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m50_37_x63(z222=z222)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m50_37_x64(z222=z222)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m50_37_x66(z222=z222)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m50_37_x65(z222=z222, z223=z223, z224=z224)
    """State 5: End state"""
    return 0

def event_m50_37_x68(z221=_):
    """[Lib] [DLC] [Conditions] Shop Lineup_1 lap
    z221: Boss destruction flag
    """
    """State 0,1: Are you killing the boss?"""
    CompareEventFlag(0, z221, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x69(z221=_, flag33=_):
    """[Lib] [DLC] [Preset] Shop Lineup_1 lap
    z221: Boss destruction flag
    flag33: Global flag for shop
    """
    """State 0,1: [Lib] [Reproduction] Shop Lineup_SubState"""
    call = event_m50_37_x61(flag33=flag33)
    if call.Get() == 0:
        """State 3: [Lib] [DLC] [Conditions] Shop lineup_Only boss destruction_SubState"""
        assert event_m50_37_x68(z221=z221)
        """State 2: [Lib] [Execution] Shop Lineup_SubState"""
        assert event_m50_37_x62(flag33=flag33)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_37_100070():
    """White Spirit Sign Display_Attribute Hunter"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m50_37_x50(z239=776)
    Quit()

def event_m50_37_x70(z216=_, z217=_, z218=0, z219=_, z220=_):
    """[Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON
    z216: Summon range
    z217: Generator ID
    z218: Appearance: Minimum time
    z219: Appearance: Maximum time
    z220: Startup flag
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z216, z216, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z218, 3, z219)
        IsPlayerInsidePoint(1, z216, z216, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z217)
            SetEventFlag(z220, 1)
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

def event_m50_37_x71(flag30=537020055, flag31=537000056):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag30: Lottery determination flag
    flag31: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag31) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag30) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m50_37_x72(z204=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z204: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z204, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m50_37_x73(flag30=537020055, z205=3, z206=40):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag30: Lottery determination flag
    z205: Number of appearance judgment points
    z206: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag30, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z205)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z206, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m50_37_x74(flag30=537020055, z204=14, flag31=537000056, z205=3, z206=40):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag30: Lottery determination flag
    z204: Random number comparison value
    flag31: Defeat flag
    z205: Number of appearance judgment points
    z206: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m50_37_x71(flag30=flag30, flag31=flag31)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m50_37_x72(z204=z204)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m50_37_x73(flag30=flag30, z205=z205, z206=z206)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m50_37_x83(flag30=flag30, z206=z206)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m50_37_x75(val2=_, z213=40):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val2: Appearance judgment number
    z213: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z213) == val2) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m50_37_x76(z209=_, z210=0, z211=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z209: Appearance judgment point ID
    z210: Minimum appearance time
    z211: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z209, z209, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z210, 3, z211)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_37_x77(z212=980, z214=_, z215=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z212: Generator ID
    z214: Appearance start point ID
    z215: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z212, z214, z215)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z212)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m50_37_x78(flag32=537000056):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag32: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag32) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m50_37_x79(z209=_, z210=0, z211=5, z212=980, val2=_, z213=40, z214=_, z215=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z209: Intrusion detection point ID
    z210: Minimum appearance time
    z211: Maximum time to appear
    z212: Generator ID
    val2: Appearance judgment number
    z213: Lottery result point variable
    z214: Appearance start point ID
    z215: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m50_37_x75(val2=val2, z213=z213)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m50_37_x76(z209=z209, z210=z210, z211=z211)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m50_37_x77(z212=z212, z214=z214, z215=z215)
    """State 4: Finish"""
    return 0

def event_m50_37_x80(z207=980, mode3=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z207: Generator ID
    mode3: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z207)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode3) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m50_37_x81(flag32=537000056, z208=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag32: Defeat flag
    z208: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag32, 1)
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
                    SetEventFlag(z208, 1)
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

def event_m50_37_x82(flag32=537000056, z207=980, mode3=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag32: Defeat flag
    z207: Generator ID
    mode3: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m50_37_x78(flag32=flag32)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m50_37_x80(z207=z207, mode3=mode3)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m50_37_x81(flag32=flag32, z208=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m50_37_x81(flag32=flag32, z208=102755)
    """State 5: End state"""
    return 0

def event_m50_37_x83(flag30=537020055, z206=40):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag30: Lottery determination flag
    z206: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag30, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z206, 0)
    """State 3: End state"""
    return 0

def event_m50_37_x84():
    """[Reproduction] Falling damage disabled_player"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x85(z202=100000, z203=100001):
    """[Condition] Fall damage invalid_player
    z202: Start point ID
    z203: End point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z202, z203, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x86(z202=100000, z203=100001):
    """[Execution] Falling damage disabled_player
    z202: Start point ID
    z203: End point ID
    """
    """State 0,1: Drop damage disabled"""
    DisablePlayerFallDamageOnce()
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z202, z203, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m50_37_x87(z202=100000, z203=100001):
    """[Preset] Falling damage disabled_player
    z202: Start point ID
    z203: End point ID
    """
    """State 0,1: [Reproduction] Falling damage invalid_player_SubState"""
    assert event_m50_37_x84()
    """State 3: [Condition] Fall damage invalid_player_SubState"""
    assert event_m50_37_x85(z202=z202, z203=z203)
    """State 2: [Execution] Fall damage invalid_player_SubState"""
    assert event_m50_37_x86(z202=z202, z203=z203)
    """State 4: Rerun"""
    return 0

def event_m50_37_x88():
    """[Reproduction] Invalid fall damage_NPC"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x89(z199=100000, z200=100001, z201=_):
    """[Condition] Fall damage invalid_NPC
    z199: Start point ID
    z200: End point ID
    z201: Generator ID
    """
    """State 0,1: Point judgment"""
    IsChrInsidePoint(0, z201, z199, z200, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x90(z199=100000, z200=100001, z201=_):
    """[Execution] Fall damage invalid_NPC
    z199: Start point ID
    z200: End point ID
    z201: Generator ID
    """
    """State 0,1: Drop damage disabled"""
    DisableEnemyFallDamageOnce(z201)
    """State 2: Did you get out of the point?"""
    IsChrInsidePoint(0, z201, z199, z200, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m50_37_x91(z199=100000, z200=100001, z201=_):
    """[Preset] Fall damage disabled_NPC
    z199: Start point ID
    z200: End point ID
    z201: Generator ID
    """
    """State 0,1: [Reproduction] Invalid fall damage_NPC_SubState"""
    assert event_m50_37_x88()
    """State 3: [Condition] Fall damage invalid_NPC_SubState"""
    assert event_m50_37_x89(z199=z199, z200=z200, z201=z201)
    """State 2: [Execution] Fall damage invalid_NPC_SubState"""
    assert event_m50_37_x90(z199=z199, z200=z200, z201=z201)
    """State 4: Rerun"""
    return 0

def event_m50_37_x92(flag29=_, z194=_):
    """[Reproduction] Release of White Knight
    flag29: Release flag
    z194: Generator ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 1: Is it already released?"""
    if GetEventFlag(flag29) != 0:
        """State 3: Delete character"""
        DeleteEnemyByGenerator(z194, 0)
        """State 5: Released"""
        return 1
    else:
        """State 4: Wait for judgment"""
        return 0
    """State 6: Guest: Exit"""
    Label('L0')
    return 2

def event_m50_37_x93(z194=_, z198=5):
    """[Condition] Release of White Knight
    z194: Generator ID
    z198: Judgment distance
    """
    """State 0,1: Approached or died"""
    CompareChrPlayerDistance(0, z194, z198, 5)
    IsChrDead(1, z194)
    if ConditionGroup(1):
        """State 3: Died"""
        return 1
    elif ConditionGroup(0):
        """State 2: Approached"""
        return 0

def event_m50_37_x94(flag29=_, z194=_, z196=96880100, z197=1):
    """[Execution] Release of White Knight
    flag29: Release flag
    z194: Generator ID
    z196: Feedback special effect ID
    z197: weight
    """
    """State 0,4: Weight until action"""
    CompareStateTime(0, z197, 3, z197)
    assert ConditionGroup(0)
    """State 1: Release flag ON"""
    SetEventFlag(flag29, 1)
    """State 2: Waiting for completion of return action"""
    ChrHasSpEffect(0, z194, z196, 1)
    CompareStateTime(0, 30, 3, 30)
    assert ConditionGroup(0)
    """State 3: Delete character"""
    DeleteEnemyByGenerator(z194, 0)
    """State 5: Message display"""
    # action:5840:"A knight of Eleum Loyce seeks the Chaos..."
    DisplayEventMessage(5840, 0, 0, 0)
    """State 6: End state"""
    return 0

def event_m50_37_x95(z194=_, flag29=_, z195=5.5, z196=96880100, z197=1):
    """[Preset] Release of White Knight
    z194: Generator ID
    flag29: Release flag
    z195: Judgment distance
    z196: Feedback special effect ID
    z197: Wait until startup
    """
    """State 0,1: [Reproduction] Liberation of White Knight_SubState"""
    call = event_m50_37_x92(flag29=flag29, z194=z194)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] White Knight Release_SubState"""
        call = event_m50_37_x93(z194=z194, z198=5)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Release of White Knight_SubState"""
            assert event_m50_37_x94(flag29=flag29, z194=z194, z196=z196, z197=z197)
    elif call.Get() == 2:
        pass
    """State 4: End state"""
    return 0

def event_m50_37_x96():
    """[Reproduction] Torches disappear due to snowstorm"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x97(z191=10, z192=537000001, z193=30):
    """[Condition] Torches disappear due to snowstorm
    z191: Main_Hit group ID
    z192: Snowstorm stop flag
    z193: Yukihara_Hit Group ID
    """
    """State 0,1: Are you wearing a torch under a snowstorm?"""
    SetConditionGroup(0, 8)
    CompareEventFlag(8, z192, 0)
    IsPlayerOnHitGroup(8, z191, 1)
    IsPlayerUsingTorch(8, 1)
    SetConditionGroup(0, 9)
    IsPlayerOnHitGroup(9, z193, 1)
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

def event_m50_37_x99(z191=10, z192=537000001, z193=30):
    """[Preset] Torches disappear with snowstorm
    z191: Main_Hit group ID
    z192: Snowstorm stop flag
    z193: Yukihara_Hit Group ID
    """
    """State 0,1: [Reproduction] A torch disappears in a snowstorm _SubState"""
    assert event_m50_37_x96()
    """State 3: [Condition] A torch disappears in a snowstorm_SubState"""
    assert event_m50_37_x97(z191=z191, z192=z192, z193=z193)
    """State 2: [Execution] Torch disappears due to snowstorm_SubState"""
    assert event_m50_37_x98()
    """State 4: Rerun"""
    return 0

def event_m50_37_x100(flag18=537000086, z114=50371001, flag19=537000002):
    """[Reproduction] Return from the boss room
    flag18: Defeat flag
    z114: Warp OBJ instance ID
    flag19: Crown acquisition flag
    """
    """State 0,1: Did you destroy the boss?"""
    if GetEventFlag(flag18) != 0:
        """State 3: Has the crown been acquired?"""
        if GetEventFlag(flag19) != 0:
            """State 2: Warp OBJ has appeared: 30"""
            ChangeObjState(z114, 30)
            """State 5: Acquired and destroyed"""
            return 1
        else:
            pass
    else:
        pass
    """State 4: Not destroy or get"""
    return 0

def event_m50_37_x101(flag18=537000086, flag19=537000002):
    """[Condition] Return from the boss room _ Defeat the boss
    flag18: Boss destruction flag
    flag19: Crown acquisition flag
    """
    """State 0,1: Destroyed the boss & got the crown?"""
    CompareEventFlag(8, flag18, 1)
    CompareEventFlag(8, flag19, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x102(z32=_):
    """[Execution] Return from Boss Room_Warp
    z32: Warp destination point ID
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
        assert event_m50_37_x0(z289=0, z290=0, z223=50370000, z32=z32)
        """State 3: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
        """State 7: Unbeatable PC"""
        SetPlayerInvincible(0)
    """State 9: End state"""
    return 0

def event_m50_37_x103(z113=3100010, flag18=537000086, z114=50371001, flag19=537000002):
    """[Preset] Return from Boss Room
    z113: Warp destination point ID
    flag18: Boss destruction flag
    z114: Warp OBJ instance ID
    flag19: Crown acquisition flag
    """
    """State 0,1: [Reproduction] Return from the boss room_SubState"""
    call = event_m50_37_x100(flag18=flag18, z114=z114, flag19=flag19)
    if call.Get() == 1:
        """State 5: [Condition] Return from the boss room_Judgment to check_SubState"""
        assert event_m50_37_x209(z33=z114)
        """State 3: [Execution] Return from Boss Room_Warp_SubState"""
        assert event_m50_37_x102(z32=z113)
    elif call.Get() == 0:
        """State 4: [Condition] Return from Boss Room_Boss Defeat_SubState"""
        assert event_m50_37_x101(flag18=flag18, flag19=flag19)
        """State 2: [Execution] Return from Boss Room_OBJ Appearance_SubState"""
        assert event_m50_37_x208(z114=z114)
    """State 6: Rerun"""
    return 0

def event_m50_37_x104(z185=50370700, z186=50370701, z187=50370702, z188=50370703):
    """[Conditions] The door opens when the lighthouse is lit
    z185: Lighthouse ①OBJ instance ID
    z186: Lighthouse ②OBJ instance ID
    z187: Lighthouse ③ OBJ instance ID
    z188: Lighthouse ④ OBJ instance ID
    """
    """State 0,1: Is the light on the lighthouse?"""
    CompareObjState(8, z185, 30, 0)
    CompareObjState(8, z186, 30, 0)
    CompareObjState(8, z187, 30, 0)
    CompareObjState(8, z188, 30, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x105(z189=50372001, z190=900000):
    """[Execution] The door opens when the lighthouse is on
    z189: Door OBJ instance ID
    z190: Navigation change point ID
    """
    """State 0,1: The door opens: 70"""
    ChangeObjState(z189, 70)
    """State 3: Waiting for the door to open"""
    CompareObjState(0, z189, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navimesh change: passable"""
    DeleteNavimeshAttribute(z190, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x106(z185=50370700, z186=50370701, z187=50370702, z188=50370703, z189=50372001, z190=900000):
    """[Preset] The door opens when the lighthouse is on
    z185: Lighthouse ①OBJ instance ID
    z186: Lighthouse ②OBJ instance ID
    z187: Lighthouse ③ OBJ instance ID
    z188: Lighthouse ④ OBJ instance ID
    z189: Door OBJ instance ID
    z190: Navigation change point ID
    """
    """State 0,1: [Reproduction] The door opens when the lighthouse lights up_SubState"""
    call = event_m50_37_x107(z189=z189, z190=z190)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] The door opens when the lighthouse is lit._SubState"""
        assert event_m50_37_x104(z185=z185, z186=z186, z187=z187, z188=z188)
        """State 2: [Execution] The door opens when the lighthouse lights up_SubState"""
        assert event_m50_37_x105(z189=z189, z190=z190)
    """State 4: End state"""
    return 0

def event_m50_37_x107(z189=50372001, z190=900000):
    """[Reproduction] The door opens when the lighthouse is on
    z189: Door OBJ instance ID
    z190: Navigation change point ID
    """
    """State 0,1: Is the door open?"""
    if CompareObjStateId(z189, 10, 1):
        """State 5: Navimesh change: non-passable_2"""
        AddNavimeshAttribute(z190, 2)
        """State 2: Waiting for the door to open"""
        assert CompareObjStateId(z189, 20, 0)
        """State 4: Navimesh change: passable"""
        DeleteNavimeshAttribute(z190, 2)
        """State 7: End state"""
        return 1
    else:
        """State 3: Navimesh change: no traffic"""
        AddNavimeshAttribute(z190, 2)
        """State 6: Not open"""
        return 0

def event_m50_37_x108(z181=50370400, z182=5300010, z183=5300000, z184=5300001):
    """[Preset] Door that opens with DLC purchase
    z181: Door OBJ instance ID
    z182: Navigation switching point ID
    z183: Judgment start point ID
    z184: Judgment end point ID
    """
    """State 0,1: [Reproduction] Doors opened with DLC purchase_SubState"""
    call = event_m50_37_x109(z181=z181, z182=z182)
    if call.Get() == 0:
        """State 3: [Conditions] Doors opened by DLC purchase_SubState"""
        call = event_m50_37_x111(z181=z181, z183=z183, z184=z184)
        if call.Get() == 0:
            """State 6: [Execution] Door opened by DLC purchase_Manual_SubState"""
            assert event_m50_37_x114(z181=z181, z182=z182)
            Goto('L0')
        elif call.Get() == 2:
            """State 5: [Execution] Door opened with DLC purchase_Auto_SubState"""
            assert event_m50_37_x113(z181=z181, z182=z182)
            Goto('L0')
        elif call.Get() == 1:
            """State 7: [Execution] Door that opens with DLC purchase_No access_Front_SubState"""
            assert event_m50_37_x115(z181=z181)
        elif call.Get() == 3:
            """State 8: [Execution] Door opened with DLC purchase_No access_Back_SubState"""
            assert event_m50_37_x116(z181=z181)
        """State 9: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 4: [Conditions] Doors opened by DLC purchase_Guest_SubState"""
        assert event_m50_37_x112(z181=z181)
        """State 2: [Execution] Door opened with DLC purchase_Guest_SubState"""
        assert event_m50_37_x110(z181=z181, z182=z182)
    """State 10: Finish"""
    Label('L0')
    return 1

def event_m50_37_x109(z181=50370400, z182=5300010):
    """[Reproduction] Door opened with DLC purchase
    z181: Door OBJ instance ID
    z182: Navigation switching point ID
    """
    """State 0,2: Navigation switching_initialization"""
    AddNavimeshAttribute(z182, 2)
    """State 1: Host?"""
    if IsGuest() != 1:
        """State 3: Safety: Door initialization"""
        InitializeObj(z181)
        assert CompareObjStateId(z181, 10, 0)
        """State 4: Disable key guide"""
        DisableObjKeyGuide(z181, 1)
        """State 5: Not passed"""
        return 0
    else:
        """State 6: The guests"""
        return 1

def event_m50_37_x110(z181=50370400, z182=5300010):
    """[Execution] Door opened with DLC purchase_Guest
    z181: King's door OBJ instance ID
    z182: Navigation switching point ID
    """
    """State 0,1: Change navigation"""
    DeleteNavimeshAttribute(z182, 2)
    """State 2: End state"""
    return 0

def event_m50_37_x111(z181=50370400, z183=5300000, z184=5300001):
    """[Conditions] Doors opened by DLC purchase
    z181: Door OBJ instance ID
    z183: Judgment start point ID
    z184: Judgment end point ID
    """
    """State 0,2: Distance judgment or point judgment"""
    CompareObjPlayerDistance(0, z181, 4, 5)
    SetConditionGroup(1, 8)
    IsPlayerInsidePoint(8, z183, z184, 1)
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

def event_m50_37_x112(z181=50370400):
    """[Conditions] Doors opened with DLC purchase_Guest
    z181: Door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z181, 20, 0)
    assert ConditionGroup(0)
    """State 2: Mural opened"""
    return 0

def event_m50_37_x113(z181=50370400, z182=5300010):
    """[Execution] Door opened with DLC purchase_Auto
    z181: Door OBJ instance ID
    z182: Navigation switching point ID
    """
    """State 0,1: Door opens"""
    ChangeObjState(z181, 20)
    """State 2: Waiting for the door to finish"""
    CompareObjState(0, z181, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching"""
    DeleteNavimeshAttribute(z182, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x114(z181=50370400, z182=5300010):
    """[Execution] Door opened with DLC purchase_Manual
    z181: Door OBJ instance ID
    z182: Navigation switching point ID
    """
    """State 0,3: Activate key guide"""
    DisableObjKeyGuide(z181, 0)
    """State 1: Waiting for the door to finish"""
    CompareObjState(0, z181, 20, 0)
    assert ConditionGroup(0)
    """State 2: Navigation switching"""
    DeleteNavimeshAttribute(z182, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x115(z181=50370400):
    """[Execution] Door opened with DLC purchase
    z181: Door OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z181, 8, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x116(z181=50370400):
    """[Execution] Door opened with DLC purchase
    z181: Door OBJ instance ID
    """
    """State 0,3: Did you approach the door?"""
    CompareObjPlayerDistance(0, z181, 4, 5)
    assert ConditionGroup(0)
    """State 1: Message display"""
    # action:5000:"Closed"
    DisplayEventMessage(5000, 0, 0, 0)
    """State 2: Did you leave the door?"""
    CompareObjPlayerDistance(0, z181, 8, 3)
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

def event_m50_37_x118(z179=50371010):
    """[Conditions] 棺 桶 Bobsled
    z179: 棺 桶 OBJ instance ID
    """
    """State 0,1: Judgment to check or multiplayer judgment"""
    IsObjSearched(0, z179)
    IsMultiplayer(1, 1, 0)
    if ConditionGroup(1):
        """State 3: During multiplayer"""
        return 1
    elif ConditionGroup(0):
        """State 2: Examined"""
        return 0

def event_m50_37_x119(z179=50371010, z180=537000005):
    """[Execution] 棺 桶 Bobsled
    z179: 棺 桶 OBJ instance ID
    z180: PC start flag
    """
    """State 0,7: Menu auto-save multi-disabled"""
    DisableAutoSave(1)
    ProhibitInGameMenu(1)
    ProhibitMultiplayer(1)
    """State 1: Action request to player"""
    ObjAnimationPlayerControlRequest(z179, 34, 13)
    assert PlayerIsInEventAction(13) != 0
    """State 14: PC invincible ON"""
    SetPlayerInvincible(1)
    """State 6: キ ャ ン セ ル moved or canceled"""
    CompareObjState(0, z179, 30, 0)
    IsPlayerPlayingMotion(1, 13, 0)
    if ConditionGroup(1):
        """State 5: Initialize 棺 桶: 10"""
        ChangeObjState(z179, 10)
        """State 10: 待 ち Waiting for initialization"""
        CompareObjState(0, z179, 10, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(0):
        """State 11: Hide player"""
        SetHidePlayer(1)
        """State 13: Bobsled start: 90"""
        ChangeObjState(z179, 90)
        """State 4: weight"""
        assert (GetStateTime() > 5) != 0
        """State 2: Warp processing"""
        PlayCutsceneAndWarpToMap(0, 0, 50370000, 400000, 2)
        """State 3: Startup motion flag ON"""
        SetEventFlag(z180, 1)
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

def event_m50_37_x120(z179=50371010):
    """[Execution] 棺 桶 Bobsleigh_Multi
    z179: 棺 桶 OBJ instance ID
    """
    """State 0,1: 棺 桶 Disable key guide"""
    DisableObjKeyGuide(z179, 1)
    """State 2: Waiting for multi end"""
    IsMultiplayer(0, 0, 0)
    assert ConditionGroup(0)
    """State 3: 棺 桶 Activating key guide"""
    DisableObjKeyGuide(z179, 0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x121(z179=50371010, z180=537000005):
    """[Preset] 棺 桶 Bobsled
    z179: 棺 桶 OBJ instance ID
    z180: PC start flag
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
    call = event_m50_37_x118(z179=z179)
    if call.Get() == 0:
        """State 2: [Execution] 棺 桶 Bobsleigh_SubState"""
        assert event_m50_37_x119(z179=z179, z180=z180)
    elif call.Get() == 1:
        """State 3: [Execution] 棺 桶 Bobsled_Multi Medium_SubState"""
        assert event_m50_37_x120(z179=z179)
    """State 5: Rerun"""
    return 0

def event_m50_37_x122(flag28=537000005, z178=50371011):
    """[Reproduction] 棺 桶 Startup event
    flag28: PC start flag
    z178: 棺 桶 OBJ instance ID
    """
    """State 0,1: Is the PC start flag ON?"""
    if GetEventFlag(flag28) != 0:
        """State 2: 棺 桶 Closed state: 30"""
        ChangeObjState(z178, 30)
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

def event_m50_37_x124(flag28=537000005, z178=50371011):
    """[Execution] 棺 桶 Startup event
    flag28: PC start flag
    z178: 棺 桶 OBJ instance ID
    """
    """State 0,1: Open the casket: 80"""
    ChangeObjState(z178, 80)
    """State 2: PC start flag OFF"""
    SetEventFlag(flag28, 0)
    """State 3: End state"""
    return 0

def event_m50_37_x125(flag28=537000005, z178=50371011):
    """[Preset] 棺 桶 Startup event
    flag28: PC start flag
    z178: 棺 桶 OBJ instance ID
    """
    """State 0,1: [Reproduction] 棺 桶 Startup event_SubState"""
    call = event_m50_37_x122(flag28=flag28, z178=z178)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] 棺 桶 Startup event_SubState"""
        assert event_m50_37_x123()
        """State 2: [Execution] 棺 桶 Startup event_SubState"""
        assert event_m50_37_x124(flag28=flag28, z178=z178)
    """State 4: End state"""
    return 0

def event_m50_37_x126(flag27=537000011, z176=50371200, z177=210000):
    """[Reproduction] Canceling the ice seal
    flag27: Seal release flag
    z176: Ice Seal OBJ Instance ID
    z177: Navigation change point ID
    """
    """State 0,1: Has the seal been released?"""
    if GetEventFlag(flag27) != 0:
        """State 2: Seal is released"""
        ChangeObjState(z176, 70)
        """State 3: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z177, 2)
        """State 6: Canceled"""
        return 1
    else:
        """State 4: Navigation switch: Passable_2"""
        AddNavimeshAttribute(z177, 2)
        """State 5: Unreleased"""
        return 0

def event_m50_37_x127(flag27=537000011):
    """[Condition] Release of ice seal
    flag27: Seal release flag
    """
    """State 0,1: Was the seal released?"""
    CompareEventFlag(0, flag27, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x128(z176=50371200, z177=210000):
    """[Execution] Release of ice seal
    z176: Ice Seal OBJ Instance ID
    z177: Navigation change point ID
    """
    """State 0,1: Seal is released"""
    ChangeObjState(z176, 70)
    """State 9: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z177, 2)
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

def event_m50_37_x129(flag27=537000011, z176=50371200, z177=210000):
    """[Preset] Canceling the ice seal
    flag27: Seal release flag
    z176: Ice Seal OBJ Instance ID
    z177: Navigation change point ID
    """
    """State 0,1: [Reproduction] Canceling the ice seal_SubState"""
    call = event_m50_37_x126(flag27=flag27, z176=z176, z177=z177)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Canceling the ice seal_SubState"""
        assert event_m50_37_x127(flag27=flag27)
        """State 2: [Execution] Canceling the ice seal_SubState"""
        assert event_m50_37_x128(z176=z176, z177=z177)
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

def event_m50_37_x131(z175=537000001):
    """[Conditions] Lighthouse under snowstorm
    z175: Snowstorm stop flag
    """
    """State 0,1: Has the snowstorm stopped?"""
    CompareEventFlag(0, z175, 1)
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

def event_m50_37_x133(z175=537000001):
    """[Preset] Lighthouse under snowstorm
    z175: Snowstorm stop flag
    """
    """State 0,1: [Reproduction] Lighthouse _SubState under snowstorm"""
    assert event_m50_37_x130()
    """State 3: [Condition] Lighthouse under snowstorm_SubState"""
    assert event_m50_37_x131(z175=z175)
    """State 2: [Execution] Lighthouse under the snowstorm_SubState"""
    assert event_m50_37_x132()
    """State 4: End state"""
    return 0

def event_m50_37_x134(flag5=537000086):
    """[Reproduction] Ice King Battle_Start
    flag5: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag5) != 0:
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

def event_m50_37_x136(z30=5037000):
    """[Execution] Ice King Battle_Start
    z30: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z30)
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

def event_m50_37_x138(z30=5037000):
    """[Condition] Ice King Battle_Phase 3
    z30: Boss Battle ID
    """
    """State 0,1: Did you destroy all bosses?"""
    IsEventBossKill(0, z30, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x139(z29=501, z30=5037000, z31=537020085):
    """[Execution] Ice King Battle Phase 2
    z29: Sound ID
    z30: Boss Battle ID
    z31: Other flags for logic
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
    PlaySoundAtPoint(z29)
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

def event_m50_37_x141(z29=501, z30=5037000, z31=537020085, mode2=0):
    """[Execution] Ice King Battle Phase 3
    z29: Sound ID
    z30: Boss Battle ID
    z31: Other flags for logic
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
    SetEventFlag(z31, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z30)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z29)
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

def event_m50_37_x142(flag5=537000086, z29=501, z30=5037000, z31=537020085):
    """[Preset] Ice King
    flag5: Boss destruction flag
    z29: Sound ID
    z30: Boss Battle ID
    z31: Other flags for logic
    """
    """State 0,5: [Reproduction] Ice King Battle_Start_SubState"""
    call = event_m50_37_x134(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 15: [Condition] Ice King Battle_Start_SubState"""
        assert event_m50_37_x135()
        """State 10: [Execution] Ice King Battle_Start_SubState"""
        assert event_m50_37_x136(z30=z30)
        """State 1: [Reproduction] Ice King Battle_Phase 1_Sky_SubState"""
        assert event_m50_37_x274()
        """State 11: [Condition] Ice King Battle_Phase 1_SubState"""
        assert event_m50_37_x275()
        """State 6: [Execution] Ice King Battle_Phase 1_SubState"""
        assert event_m50_37_x276(z31=z31)
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
        assert event_m50_37_x139(z29=z29, z30=z30, z31=z31)
        """State 3: [Reproduction] Ice King Battle_Phase 3_SubState"""
        assert event_m50_37_x199()
        """State 13: [Condition] Ice King Battle_Phase 3_SubState"""
        assert event_m50_37_x138(z30=z30)
        """State 8: [Execution] Ice King Battle_Phase 3_SubState"""
        assert event_m50_37_x141(z29=z29, z30=z30, z31=z31, mode2=0)
    """State 16: End state"""
    return 0

def event_m50_37_x143(flag25=537000012, z172=537010013, flag26=537000081):
    """[Reproduction] Transparent management of tigers
    flag25: Miko's eyes: possession flag
    z172: Transparency control flag
    flag26: Defeat flag
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
    if GetEventFlag(flag26) != 0:
        pass
    else:
        Goto('L1')
    """State 8: Defeated"""
    return 3
    """State 2: Do you have a shrine maiden eye?"""
    Label('L1')
    if GetEventFlag(flag25) != 0:
        """State 6: Possessing a shrine maiden's eyes"""
        return 1
    else:
        """State 4: Transparent control flag ON"""
        SetEventFlag(z172, 1)
        """State 5: Transparency control"""
        return 0

def event_m50_37_x144(z173=907, flag26=537000081, z174=537020080, flag25=537000012):
    """[Condition] Transparent management of tigers
    z173: Generator ID
    flag26: Defeat flag
    z174: Battle start flag
    flag25: Miko's eyes: possession flag
    """
    """State 0,1: Battle start or shrine maiden possession or destruction determination"""
    CompareChrEzStateValue(0, z173, 7, 1, 0)
    CompareEventFlag(0, z174, 1)
    CompareEventFlag(1, flag26, 1)
    CompareEventFlag(1, flag25, 1)
    if ConditionGroup(1):
        """State 3: Rerun"""
        return 1
    elif ConditionGroup(0):
        """State 2: Transparency control"""
        return 0

def event_m50_37_x145(flag25=537000012, z172=537010013, z173=907, flag26=537000081):
    """[Execution] Transparent management of tigers
    flag25: Miko's eyes: possession flag
    z172: Transparency control flag
    z173: Generator ID
    flag26: Defeat flag
    """
    """State 0,1: Random timer or shrine maiden possession or destruction determination"""
    CompareStateTime(0, 15, 3, 25)
    CompareEventFlag(1, flag26, 1)
    CompareEventFlag(1, flag25, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Transparent control flag OFF"""
        SetEventFlag(z172, 0)
        """State 4: Random timer or shrine maiden eye possession or destruction determination_2"""
        CompareStateTime(0, 1, 3, 3)
        CompareEventFlag(1, flag26, 1)
        CompareEventFlag(1, flag25, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 2: Transparent control flag ON"""
            SetEventFlag(z172, 1)
    """State 5: End state"""
    return 0

def event_m50_37_x146(flag25=537000012, z172=537010013, z173=907, flag26=537000081, z174=537020080):
    """[Preset] Transparent management of tigers
    flag25: Miko's eyes: possession flag
    z172: Transparency control flag
    z173: Generator ID
    flag26: Defeat flag
    z174: Battle start flag
    """
    """State 0,1: [Reproduction] Transparency management of tigers_SubState"""
    call = event_m50_37_x143(flag25=flag25, z172=z172, flag26=flag26)
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
    call = event_m50_37_x144(z173=z173, flag26=flag26, z174=z174, flag25=flag25)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Transparent management of tigers_SubState"""
        assert event_m50_37_x145(flag25=flag25, z172=z172, z173=z173, flag26=flag26)
    """State 5: Rerun"""
    return 1

def event_m50_37_x147(z165=537000012, z166=537010013, z167=907, z168=96790010, z169=96790000, z170=96790020):
    """[Preset] Transparent tiger
    z165: Miko's eyes: possession flag
    z166: Transparency control flag
    z167: Generator ID
    z168: Transparent special effect ID
    z169: Translucent special effect ID
    z170: Normal special effect ID
    """
    """State 0,1: [Reproduction] Transparency of tigers_SubState"""
    assert event_m50_37_x148()
    """State 4: [Condition] Tiger transparency_SubState"""
    call = event_m50_37_x149(z165=z165, z166=z166)
    if call.Get() == 2:
        """State 3: [Execution] Transparency of tiger_Release_SubState"""
        assert event_m50_37_x151(z167=z167, z168=z168, z169=z169, z170=z170)
        """State 6: Finish"""
        return 0
    elif call.Get() == 0:
        """State 5: [Execution] Transparency of tigers_Translucent_SubState"""
        assert event_m50_37_x150(z167=z167, z168=z169, z165=z165, z166=z166, z171=1, z169=z168)
    elif call.Get() == 1:
        """State 2: [Execution] Transparency of tigers_Transparent_SubState"""
        assert event_m50_37_x150(z167=z167, z168=z168, z165=z165, z166=z166, z171=0, z169=z169)
    """State 7: Rerun"""
    return 1

def event_m50_37_x148():
    """[Reproduction] Transparency of tiger"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x149(z165=537000012, z166=537010013):
    """[Condition] Transparency of tiger
    z165: Miko's eyes: possession flag
    z166: Transparency control flag
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z166, 1)
    CompareEventFlag(1, z166, 0)
    CompareEventFlag(2, z165, 1)
    if ConditionGroup(2):
        """State 4: The possession of a shrine maiden"""
        return 2
    elif ConditionGroup(1):
        """State 2: Translucent"""
        return 0
    elif ConditionGroup(0):
        """State 3: Transparency"""
        return 1

def event_m50_37_x150(z167=907, z168=_, z165=537000012, z166=537010013, z171=_, z169=_):
    """[Execution] Transparency of tigers
    z167: Generator ID
    z168: Grant special effect ID
    z165: Miko's eyes: possession flag
    z166: Transparency control flag
    z171: Control flag judgment
    z169: Cancel special effect ID
    """
    """State 0,3: Cancel special effects"""
    ClearEnemySpEffect(z167, z168)
    ClearEnemySpEffect(z167, z169)
    assert (GetStateTime() >= 0) != 0
    """State 1: Giving special effects to tigers"""
    SetEnemySpEffect(z167, z168, 10, 4)
    """State 2: Flag judgment"""
    CompareEventFlag(0, z166, z171)
    CompareEventFlag(0, z165, 1)
    assert ConditionGroup(0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x151(z167=907, z168=96790010, z169=96790000, z170=96790020):
    """[Execution] Make tiger transparent
    z167: Generator ID
    z168: Transparent special effect ID
    z169: Translucent special effect ID
    z170: Normal special effect ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z167, z168)
    ClearEnemySpEffect(z167, z169)
    assert (GetStateTime() >= 0) != 0
    """State 2: Giving special effects to tigers"""
    SetEnemySpEffect(z167, z170, 10, 4)
    """State 3: Finish"""
    return 0

def event_m50_37_x152(flag24=537000081):
    """[Reproduction] Tiger Battle_Start
    flag24: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag24) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_37_x153(z161=2500000, z164=2500000):
    """[Condition] Tiger Battle_Start
    z161: Start point ID
    z164: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z161, z164, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z161, z164, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x154(z157=5037030):
    """[Execution] Tiger Battle_Start
    z157: Boss Battle ID
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z157)
    """State 2: End state"""
    return 0

def event_m50_37_x155():
    """[Reproduction] HP display and BGM playback and boss activation_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x156(z163=907, z158=537020080):
    """[Condition] HP display, BGM playback and boss activation
    z163: Boss generator ID
    z158: Logic flag
    """
    """State 0,1: Damaged or point intrusion or activated"""
    CompareChrHpRatio(0, z163, 100, 4)
    IsPlayerInsidePoint(0, 2500010, 2500010, 1)
    CompareEventFlag(0, z158, 1)
    CompareChrEzStateValue(0, z163, 7, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x157(z156=504, z158=537020080, z159=5, z157=5037030, z160=537020083, z162=907):
    """[Execution] HP display, BGM playback and boss activation
    z156: Sound ID
    z158: Logic flag
    z159: Wait time until display
    z157: Boss Battle ID
    z160: BGM and gauge display flag
    z162: Boss generator ID
    """
    """State 0,3: Logic flag ON"""
    SetEventFlag(z158, 1)
    """State 4: Wait until BGM playback and HP display"""
    CompareStateTime(0, z159, 2, z159)
    CompareEventFlag(0, z160, 1)
    CompareChrEzStateValue(0, z162, 7, 1, 0)
    IsEventBossKill(1, z157, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z156)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 6: Camera parameter switching"""
    ChangeCameraParameters(679100, 3, 3)
    """State 5: BGM and gauge display flag ON"""
    SetEventFlag(z160, 1)
    """State 7: End state"""
    return 0

def event_m50_37_x158():
    """[Reproduction] Tiger Battle_End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x159(z157=5037030):
    """[Condition] Tora Battle_End Judgment
    z157: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z157, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x160(z156=504, z157=5037030, z158=537020080):
    """[Execution] Tiger Battle_End
    z156: Sound ID
    z157: Boss Battle ID
    z158: Other flags for logic
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z158, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z157)
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z156)
    assert (GetStateTime() > 6.5) != 0
    """State 4: Return camera parameters"""
    ResetCameraParameters()
    """State 5: End state"""
    return 0

def event_m50_37_x161(flag24=537000081, z156=504, z157=5037030, z158=537020080, z159=5, z160=537020083,
                      z161=2500000):
    """[Preset] Tiger Battle_Start
    flag24: Boss destruction flag
    z156: Sound ID
    z157: Boss Battle ID
    z158: Other flags for logic
    z159: Wait time
    z160: BGM and gauge display flag
    z161: Point ID
    """
    """State 0,1: [Reproduction] Tiger Battle_Start_SubState"""
    call = event_m50_37_x152(flag24=flag24)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Tiger Battle_Start_SubState"""
        assert event_m50_37_x153(z161=z161, z164=z161)
        """State 3: [Execution] Tiger Battle_Start_SubState"""
        assert event_m50_37_x154(z157=z157)
        """State 7: [Reproduction] HP display and BGM playback and boss activation_empty_SubState"""
        assert event_m50_37_x155()
        """State 9: [Condition] HP display, BGM playback and boss activation_SubState"""
        assert event_m50_37_x156(z163=907, z158=z158)
        """State 8: [Execution] HP display, BGM playback and boss activation_SubState"""
        assert event_m50_37_x157(z156=z156, z158=z158, z159=z159, z157=z157, z160=z160, z162=907)
        """State 2: [Reproduction] Tiger Battle_End_Sky_SubState"""
        assert event_m50_37_x158()
        """State 6: [Condition] Tiger Battle_End Judgment_SubState"""
        assert event_m50_37_x159(z157=z157)
        """State 4: [Execution] Tiger Battle_End_SubState"""
        assert event_m50_37_x160(z156=z156, z157=z157, z158=z158)
    """State 10: End state"""
    return 0

def event_m50_37_x162(z154=537010014, z155=537020015):
    """[Execution] Snowstorm management in the snowfield area
    z154: Snowstorm control flag
    z155: Enemy appearance flag
    """
    """State 0,1: Snowstorm control flag ON"""
    SetEventFlag(z154, 1)
    """State 5: Waiting for enemy appearance"""
    CompareStateTime(0, 3, 3, 3)
    assert ConditionGroup(0)
    """State 6: Enemy appearance flag ON"""
    SetEventFlag(z155, 1)
    """State 2: Has time passed?"""
    CompareStateTime(0, 22, 3, 27)
    assert ConditionGroup(0)
    """State 3: Snowstorm control flag OFF"""
    SetEventFlag(z154, 0)
    """State 7: Enemy appearance flag OFF"""
    SetEventFlag(z155, 0)
    """State 4: Has time passed? _2"""
    CompareStateTime(0, 15, 3, 24)
    assert ConditionGroup(0)
    """State 8: Rerun"""
    return 0

def event_m50_37_x163(z154=537010014):
    """[Reproduction] Snowstorm management in the snowy field area
    z154: Snowstorm control flag
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

def event_m50_37_x165(z154=537010014, z155=537020015):
    """[Preset] Snowstorm management in the snowfield area
    z154: Snowstorm control flag
    z155: Enemy appearance flag
    """
    """State 0,1: [Reproduction] Snowstorm management in the snowy field_SubState"""
    call = event_m50_37_x163(z154=z154)
    if call.Get() == 1:
        """State 5: Finish"""
        return 1
    elif call.Get() == 0:
        """State 3: [Condition] Snowstorm management in the snowfield area_SubState"""
        assert event_m50_37_x164()
        """State 2: [Execution] Snowstorm management in the snowfield area_SubState"""
        assert event_m50_37_x162(z154=z154, z155=z155)
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

def event_m50_37_x167(z144=_, z148=_, z149=_, z153=537020015, z150=_, z151=_):
    """[Condition] Enemy appearing in a snowstorm
    z144: Generator ID
    z148: Defeat count
    z149: Maximum number of generations
    z153: Enemy appearance flag
    z150: Generateable_start point ID
    z151: Generateable_end point ID
    """
    """State 0,1: Generation determination"""
    CompareEventFlag(8, z153, 1)
    IsChrActive(8, z144, 0)
    IsPlayerInsidePoint(8, 600080, 600099, 0)
    IsPlayerInsidePoint(8, z150, z151, 1)
    IsPlayerOnHitGroup(8, 30, 1)
    CompareEventFlagValue(1, 1, z148, z149, 3)
    if ConditionGroup(1):
        """State 3: Maximum number: End"""
        return 1
    elif ConditionGroup(8):
        """State 2: End state"""
        return 0

def event_m50_37_x168(z144=_, z145=_, z146=_, z152=1, z147=_, z148=_, z149=_):
    """[Execution] Enemy that appears in a snowstorm
    z144: Generator ID
    z145: Generation start point ID
    z146: Generation end point ID
    z152: Generation distance order
    z147: Next generation weight
    z148: Defeat count
    z149: Maximum number of generations
    """
    """State 0,1: Enemy generation"""
    ForceGenerationFromPointBasedOnPositionAndCameraOfAllUsers(z144, z145, z146, 20, 50, 1, z152, 1)
    assert (GetStateTime() > 1) != 0
    """State 2: Death determination or upper limit number determination"""
    IsChrDead(0, z144)
    CompareEventFlagValue(1, 1, z148, z149, 3)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Next generation wait or upper limit number judgment"""
        CompareStateTime(0, z147, 3, z147)
        CompareEventFlagValue(1, 1, z148, z149, 3)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 4: Rerun"""
            return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x169(z144=_, z145=_, z146=_, z147=_, z148=_, z149=_, z150=_, z151=_):
    """[Preset] Enemy that appears in snowstorm
    z144: Generator ID
    z145: Generation start point ID
    z146: Generation end point ID
    z147: Next generation weight
    z148: Defeat count
    z149: Maximum number of generations
    z150: Generateable_start point ID
    z151: Generateable_end point ID
    """
    """State 0,1: [Reproduction] Enemy _SubState that appears in a snowstorm"""
    call = event_m50_37_x166()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Enemy _SubState appearing in snowstorm"""
        call = event_m50_37_x167(z144=z144, z148=z148, z149=z149, z153=537020015, z150=z150, z151=z151)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Enemy _SubState that appears in a snowstorm"""
            call = event_m50_37_x168(z144=z144, z145=z145, z146=z146, z152=1, z147=z147, z148=z148, z149=z149)
            if call.Get() == 1:
                pass
            elif call.Get() == 0:
                """State 4: Rerun"""
                return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x170(z141=_, z142=_, flag23=_, z143=_):
    """[Condition] Enemy moving by absorbing soul
    z141: Generator ID
    z142: Absorption distance
    flag23: Absorption flag
    z143: Absorption OBJ instance ID
    """
    """State 0,3: Is the ice already broken?"""
    CompareEventFlag(0, 537000011, 1)
    assert ConditionGroup(0)
    """State 4: Seoul absorption processing: ON"""
    AddSoulAcquisitionTarget(z143, z142, flag23, 1, -1)
    """State 1: Absorption or character determination"""
    CompareEventFlag(0, flag23, 1)
    IsChrDeadOrRespawnOver(1, z141, 1)
    if ConditionGroup(1):
        """State 2: Seoul absorption processing: OFF"""
        AddSoulAcquisitionTarget(z143, z142, flag23, 0, 220)
        """State 5: Absorption OBJ hidden: 20"""
        ChangeObjState(z143, 20)
        """State 7: Absorption character death"""
        return 1
    elif ConditionGroup(0):
        """State 6: Absorption completed"""
        return 0

def event_m50_37_x171(flag23=_, z143=_):
    """[Reproduction] Enemy moving by absorbing soul
    flag23: Absorption flag
    z143: Absorption OBJ instance ID
    """
    """State 0,1: Already absorbed?"""
    if GetEventFlag(flag23) != 0:
        """State 2: Absorption OBJ hidden: 20"""
        ChangeObjState(z143, 20)
        """State 4: Absorbed"""
        return 1
    else:
        """State 3: Not absorbed"""
        return 0

def event_m50_37_x172(z143=_):
    """[Execution] Enemy moving by absorbing soul
    z143: Absorption OBJ instance ID
    """
    """State 0,1,2: Absorption OBJ hidden: 20"""
    ChangeObjState(z143, 20)
    """State 3: End state"""
    return 0

def event_m50_37_x173(z141=_, z142=_, flag23=_, z143=_):
    """[Preset] Enemy who moves by absorbing soul
    z141: Generator ID
    z142: Absorption distance
    flag23: Absorption flag
    z143: Absorption OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemy _SubState moving by absorbing soul"""
    call = event_m50_37_x171(flag23=flag23, z143=z143)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Enemy _SubState moving by absorbing Seoul"""
        call = event_m50_37_x170(z141=z141, z142=z142, flag23=flag23, z143=z143)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Enemies that move by absorbing souls_SubState"""
            assert event_m50_37_x172(z143=z143)
    """State 4: End state"""
    return 0

def event_m50_37_x174(flag22=537000006):
    """[Reproduction] Rejection effect by ice
    flag22: Event completion flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the event been executed?"""
        if GetEventFlag(flag22) != 0:
            pass
        else:
            """State 3: Not executed"""
            return 0
    """State 4: Finish"""
    return 1

def event_m50_37_x175(z138=1600000):
    """[Condition] Rejection effect by ice
    z138: Point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(8, z138, z138, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x176(z137=537020016, z139=50371251, z140=50371252, flag22=537000006):
    """[Execution] Rejection by ice
    z137: Conversation flag
    z139: Door OBJ instance ID
    z140: Vine: Ice OBJ instance ID
    flag22: Event completion flag
    """
    """State 0,2: Cold threat from the door: 70"""
    ChangeObjState(z139, 70)
    assert (GetStateTime() > 2) != 0
    """State 3: Vine ice appears: 70"""
    ChangeObjState(z140, 70)
    assert (GetStateTime() > 0.5) != 0
    """State 1: Conversation flag ON"""
    SetEventFlag(z137, 1)
    """State 4: Event completion flag ON"""
    SetEventFlag(flag22, 1)
    """State 5: End state"""
    return 0

def event_m50_37_x177(z137=537020016, z138=1600000, z139=50371251, z140=50371252, flag22=537000006):
    """[Preset] Rejection effect by ice
    z137: Conversation flag
    z138: Point ID
    z139: Door OBJ instance ID
    z140: Vine: Ice OBJ instance ID
    flag22: Event completion flag
    """
    """State 0,1: [Reproduction] Rejection effect by ice_SubState"""
    call = event_m50_37_x174(flag22=flag22)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Rejection effect by ice_SubState"""
        assert event_m50_37_x175(z138=z138)
        """State 2: [Execution] Rejection with ice_SubState"""
        assert event_m50_37_x176(z137=z137, z139=z139, z140=z140, flag22=flag22)
    """State 4: End state"""
    return 0

def event_m50_37_x178(z136=1400000, z135=50371021, z134=50371020):
    """[Reproduction] Snowball Gorokuro
    z136: Navigation change point ID
    z135: Big Snowball OBJ Instance ID
    z134: Mini Snowball OBJ instance ID
    """
    """State 0,2: Has a big snowball already displayed?"""
    if CompareObjStateId(z135, 20, 0):
        pass
    else:
        """State 4: Mini snowball status judgment"""
        if CompareObjStateId(z134, 10, 1):
            """State 5: Waiting for a mini snowball to roll"""
            if CompareObjStateId(z134, 72, 0):
                pass
            elif CompareObjStateId(z134, 21, 0):
                pass
            """State 6: Deca snowball display: 20"""
            ChangeObjState(z135, 20)
        else:
            """State 1: Navigation switching: Not allowed"""
            AddNavimeshAttribute(z136, 2)
            """State 7: Waiting for rolling"""
            return 0
    """State 3: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z136, 2)
    """State 8: Finish"""
    return 1

def event_m50_37_x179(z134=50371020):
    """[Conditions] Snowball Gorokuro
    z134: Mini Snowball OBJ instance ID
    """
    """State 0,1: Snowball damage judgment"""
    IsObjDamaged(0, z134, -1, -4, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x180(z134=50371020, z135=50371021, z136=1400000):
    """[Execution] Snowball Gorokuro
    z134: Mini Snowball OBJ instance ID
    z135: Big Snowball OBJ Instance ID
    z136: Navigation change point ID
    """
    """State 0,3: Starting rolling mini snowballs: 70"""
    ChangeObjState(z134, 70)
    """State 4: Waiting for rolling"""
    CompareObjState(0, z134, 72, 0)
    assert ConditionGroup(0)
    """State 1: Deca snowball display"""
    ChangeObjState(z135, 20)
    """State 2: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z136, 2)
    """State 5: End state"""
    return 0

def event_m50_37_x181(z134=50371020, z135=50371021, z136=1400000):
    """[Preset] Snowball Gorokuro
    z134: Mini Snowball OBJ instance ID
    z135: Big Snowball OBJ Instance ID
    z136: Navigation change point ID
    """
    """State 0,2: [Reproduction] Snowball Gorokuro_SubState"""
    call = event_m50_37_x178(z136=z136, z135=z135, z134=z134)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Snowball Gorokuro_SubState"""
        assert event_m50_37_x179(z134=z134)
        """State 3: [Execution] Snowball Gorokuro_SubState"""
        assert event_m50_37_x180(z134=z134, z135=z135, z136=z136)
    """State 5: End state"""
    return 0
    """Unused"""
    """State 1: State"""
    Quit()

def event_m50_37_x182(flag1=537000012, z4=17000):
    """[Reproduction] Obtaining the eyes of a shrine maiden
    flag1: Miko eyes possession flag
    z4: Event SFXID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Already acquired?"""
        if GetEventFlag(flag1) != 1:
            """State 3: Generation of SFX"""
            PlaySfxAtPoint(z4)
            """State 5: Unacquired"""
            return 0
        else:
            pass
    else:
        pass
    """State 4: Stop SFX"""
    StopSfxAtPoint(z4)
    """State 6: Finish"""
    return 1

def event_m50_37_x183(z2=50376550):
    """[Conditions] Acquire Miko's eyes
    z2: Miko eyes OBJ instance ID
    """
    """State 0,1: Got Miko's eyes? Are you in the snowy field?"""
    WasObjItemAcquired(0, z2, 1)
    IsPlayerOnHitGroup(1, 30, 1)
    if ConditionGroup(0):
        """State 2: Miko's eyes get"""
        return 0
    elif ConditionGroup(1):
        """State 3: In the snowy field"""
        return 1

def event_m50_37_x184(flag1=537000012, z3=17000, z4=17000):
    """[Execution] Acquire the eyes of a shrine maiden
    flag1: Miko eyes possession flag
    z3: Event sound ID
    z4: Event SFXID
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(flag1, 1)
    """State 2: Atmosphere SE regeneration"""
    PlaySoundAtPoint(z3)
    """State 3: Stop SFX"""
    StopSfxAtPoint(z4)
    """State 4: End state"""
    return 0

def event_m50_37_x185(flag1=537000012, z2=50376550, z3=17000, z4=17000):
    """[Preset] Acquire Miko's eyes
    flag1: Miko eyes possession flag
    z2: Miko eyes OBJ instance ID
    z3: Event sound ID
    z4: Event SFXID
    """
    """State 0,1: [Reproduction] _SubState to get Miko's eyes"""
    call = event_m50_37_x182(flag1=flag1, z4=z4)
    if call.Get() == 0:
        """State 3: [Condition] _SubState to get Miko's eyes"""
        call = event_m50_37_x183(z2=z2)
        if call.Get() == 0:
            """State 2: [Execution] _SubState to get the eyes of the shrine maiden"""
            assert event_m50_37_x184(flag1=flag1, z3=z3, z4=z4)
        elif call.Get() == 1:
            """State 4: [DC] [Execution] Yukihara_SubState to get Miko's eyes"""
            assert event_m50_37_x387(z4=z4)
    elif call.Get() == 1:
        pass
    """State 5: End state"""
    return 0

def event_m50_37_x186(flag21=537000012, z128=_):
    """[Reproduction] Zako's transparency management
    flag21: Miko's eyes: possession flag
    z128: Transparency control flag
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
    if GetEventFlag(flag21) != 0:
        """State 5: Possessing a shrine maiden's eyes"""
        return 1
    else:
        """State 3: Transparent control flag ON"""
        SetEventFlag(z128, 1)
        """State 4: Transparency control"""
        return 0

def event_m50_37_x187():
    """[Condition] Zako's transparency management_empty"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x188(flag21=537000012, z128=_, z129=_, z130=_, z131=_, z132=_, z133=_):
    """[Execution] Transparent management of Zako
    flag21: Miko's eyes: possession flag
    z128: Transparency control flag
    z129: Generator ID
    z130: Minimum time to turn off
    z131: Maximum time to OFF
    z132: Minimum time to ON
    z133: Maximum time to ON
    """
    """State 0,1: Random timer or shrine maiden possession or destruction determination"""
    CompareStateTime(0, z130, 3, z131)
    IsChrDeadOrRespawnOver(1, z129, 1)
    CompareEventFlag(1, flag21, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Transparent control flag OFF"""
        SetEventFlag(z128, 0)
        """State 4: Random timer or shrine maiden eye possession or destruction determination_2"""
        CompareStateTime(0, z132, 3, z133)
        IsChrDeadOrRespawnOver(1, z129, 1)
        CompareEventFlag(1, flag21, 1)
        if ConditionGroup(1):
            pass
        elif ConditionGroup(0):
            """State 2: Transparent control flag ON"""
            SetEventFlag(z128, 1)
            """State 6: Rerun"""
            return 1
    """State 5: Finish"""
    return 0

def event_m50_37_x189(flag21=537000012, z128=_, z129=_, z130=_, z131=_, z132=_, z133=_):
    """[Preset] Zako's transparency management
    flag21: Miko's eyes: possession flag
    z128: Transparency control flag
    z129: Generator ID
    z130: Minimum time to turn off
    z131: Maximum time to OFF
    z132: Minimum time to ON
    z133: Time until ON
    """
    """State 0,1: [Reproduction] Zako's transparency management_SubState"""
    call = event_m50_37_x186(flag21=flag21, z128=z128)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Zako's transparency management_empty_SubState"""
        assert event_m50_37_x187()
        """State 2: [Execution] Zako's transparency management_SubState"""
        call = event_m50_37_x188(flag21=flag21, z128=z128, z129=z129, z130=z130, z131=z131, z132=z132,
                                 z133=z133)
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

def event_m50_37_x191(z122=537000012, z123=_):
    """[Condition] Transparency of Zako
    z122: Miko's eyes: possession flag
    z123: Transparency control flag
    """
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, z123, 1)
    CompareEventFlag(1, z123, 0)
    CompareEventFlag(2, z122, 1)
    if ConditionGroup(2):
        """State 4: The possession of a shrine maiden"""
        return 2
    elif ConditionGroup(1):
        """State 2: Translucent"""
        return 0
    elif ConditionGroup(0):
        """State 3: Transparency"""
        return 1

def event_m50_37_x192(z124=_, z125=_, z122=537000012, z123=_, z127=_, z126=_):
    """[Execution] Transparency of Zako
    z124: Generator ID
    z125: Grant special effect ID
    z122: Miko's eyes: possession flag
    z123: Transparency control flag
    z127: Control flag judgment
    z126: Cancel special effect ID
    """
    """State 0,3: Cancel special effects"""
    ClearEnemySpEffect(z124, z125)
    ClearEnemySpEffect(z124, z126)
    assert (GetStateTime() >= 0) != 0
    """State 1: Giving Zako a special effect"""
    SetEnemySpEffect(z124, z125, 10, 4)
    """State 2: Flag judgment"""
    CompareEventFlag(0, z123, z127)
    CompareEventFlag(0, z122, 1)
    assert ConditionGroup(0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x193(z124=_, z125=98830010, z126=98830000):
    """[Execution] Zako's transparency_release
    z124: Generator ID
    z125: Transparent special effect ID
    z126: Translucent special effect ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z124, z125)
    ClearEnemySpEffect(z124, z126)
    """State 2: Finish"""
    return 0

def event_m50_37_x194(z122=537000012, z123=_, z124=_, z125=98830010, z126=98830000):
    """[Preset] Transparency of Zako
    z122: Miko's eyes: possession flag
    z123: Transparency control flag
    z124: Generator ID
    z125: Transparent special effect ID
    z126: Translucent special effect ID
    """
    """State 0,1: [Reproduction] Transparency of Zako_SubState"""
    assert event_m50_37_x190()
    """State 4: [Condition] Zako's transparency_SubState"""
    call = event_m50_37_x191(z122=z122, z123=z123)
    if call.Get() == 2:
        """State 3: [Execution] Zako's transparency_Release_SubState"""
        assert event_m50_37_x193(z124=z124, z125=z125, z126=z126)
        """State 6: Finish"""
        return 0
    elif call.Get() == 0:
        """State 5: [Execution] Zako's transparency_Translucent_SubState"""
        assert event_m50_37_x192(z124=z124, z125=z126, z122=z122, z123=z123, z127=1, z126=z125)
    elif call.Get() == 1:
        """State 2: [Execution] Zako's transparency_Transparency_SubState"""
        assert event_m50_37_x192(z124=z124, z125=z125, z122=z122, z123=z123, z127=0, z126=z126)
    """State 7: Rerun"""
    return 1

def event_m50_37_x195(flag20=537000086):
    """[Reproduction] Black Knight: Defeat count
    flag20: Defeat count variable
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the boss been destroyed?"""
        if GetEventFlag(flag20) != 0:
            pass
        else:
            """State 3: End state"""
            return 0
    """State 4: Do nothing: Quit"""
    return 1

def event_m50_37_x196(z119=_, z121=0):
    """[Condition] Black Knight: Defeat count
    z119: Generator ID
    z121: Boss destruction flag
    """
    """State 0,1: Wait for character destruction or wait for boss destruction"""
    IsChrDead(0, z119)
    CompareEventFlag(1, z121, 1)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Variable addition"""
        return 0

def event_m50_37_x197(z119=_, z120=1):
    """[Execution] Black Knight: Defeat count
    z119: Generator ID
    z120: Defeat count variable
    """
    """State 0,1: [Condition] Ice King Battle_Start_SubState"""
    AddAreaVariable(z120, 1)
    """State 2: Wait for generator to restart"""
    IsChrActive(0, z119, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x198(z119=_, z120=1, flag20=537000086):
    """[Preset] Black Knight: Defeat count
    z119: Generator ID
    z120: Defeat count variable
    flag20: Boss destruction flag
    """
    """State 0,1: [Reproduction] Black Knight: Defeat count _SubState"""
    call = event_m50_37_x195(flag20=flag20)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Black Knight: Defeat Count Count_SubState"""
        call = event_m50_37_x196(z119=z119, z121=0)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Black Knight: Defeat count _SubState"""
            assert event_m50_37_x197(z119=z119, z120=z120)
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

def event_m50_37_x204(z115=_, z116=_, z117=_, z118=5):
    """[Preset] Gate opened by lever
    z115: Lever OBJ instance ID
    z116: Gate OBJ instance ID
    z117: Navigation change point ID
    z118: Wait until navigation switching
    """
    """State 0,1: [Reproduction] Gate_SubState opened with lever"""
    call = event_m50_37_x205(z116=z116, z117=z117)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Gate_SubState opened with lever"""
        assert event_m50_37_x206(z115=z115)
        """State 2: [Execution] Gate opened with lever _SubState"""
        assert event_m50_37_x207(z116=z116, z117=z117, z118=z118)
    """State 4: End state"""
    return 0

def event_m50_37_x205(z116=_, z117=_):
    """[Reproduction] Gate opened with lever
    z116: Gate OBJ instance ID
    z117: Navigation change point ID
    """
    """State 0,1: Is the gate open?"""
    if CompareObjStateId(z116, 10, 1):
        """State 3: Waiting for opening"""
        assert CompareObjStateId(z116, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z117, 2)
        """State 6: Already in operation"""
        return 1
    else:
        """State 4: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z117, 2)
        """State 5: Not in operation"""
        return 0

def event_m50_37_x206(z115=_):
    """[Condition] Gate opened by lever
    z115: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z115, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x207(z116=_, z117=_, z118=5):
    """[Execution] Gate opened by lever
    z116: Gate OBJ instance ID
    z117: Navigation change point ID
    z118: Wait until navigation switching
    """
    """State 0,2: Gate opens: 70"""
    ChangeObjState(z116, 70)
    """State 4: weight"""
    CompareStateTime(0, z118, 3, z118)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z117, 2)
    """State 3: Waiting for the opening of the iron lattice"""
    CompareObjState(0, z116, 20, 0)
    assert ConditionGroup(0)
    """State 5: End state"""
    return 0

def event_m50_37_x208(z114=50371001):
    """[Execution] Return from boss room_OBJ appearance
    z114: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ has appeared: 30"""
    ChangeObjState(z114, 30)
    """State 2: Rerun"""
    return 0

def event_m50_37_x209(z33=_):
    """[Condition] Return from the boss room
    z33: Warp OBJ instance ID
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z33)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x210(flag2=_):
    """[Reproduction] Black Knight: Generator
    flag2: Sealed flag
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
        if GetEventFlag(flag2) != 0:
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

def event_m50_37_x211(flag2=_, z14=_, z19=_, z20=_):
    """[Condition] Black Knight: Generator
    flag2: Sealed flag
    z14: Event group ID
    z19: Other ① Event group ID
    z20: Other ② Event group ID
    """
    """State 0,1: Generation determination"""
    CompareEventFlag(0, flag2, 1)
    CompareEventFlag(0, 537020175, 1)
    SetConditionGroup(1, 8)
    CompareActiveChrNum(8, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(8, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(8, 2, 3, 6)
    CompareEventFlag(8, 537020170, 1)
    CompareEventFlag(8, 537020172, 0)
    CompareEventFlag(8, 537020032, 1)
    SetConditionGroup(1, 9)
    CompareActiveChrNum(9, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(9, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(9, 30, 3, 45)
    CompareEventFlag(9, 537020170, 1)
    CompareEventFlag(9, 537020172, 0)
    CompareEventFlag(9, 537020032, 1)
    SetConditionGroup(1, 10)
    CompareActiveChrNum(10, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(10, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(10, 35, 3, 45)
    CompareEventFlag(10, 537020174, 1)
    CompareEventFlagValue(10, 1, 2, 6, 4)
    CompareMultiplayerPlayerCount(10, 1, 1, 0, 0)
    CompareEventFlag(10, 537020032, 1)
    SetConditionGroup(1, 11)
    CompareActiveChrNum(11, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(11, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(11, 35, 3, 45)
    CompareEventFlag(11, 537020174, 1)
    CompareEventFlagValue(11, 1, 2, 12, 4)
    CompareMultiplayerPlayerCount(11, 1, 1, 1, 0)
    CompareEventFlag(11, 537020032, 1)
    SetConditionGroup(1, 12)
    CompareActiveChrNum(12, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(12, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(12, 35, 3, 45)
    CompareEventFlag(12, 537020174, 1)
    CompareEventFlagValue(12, 1, 2, 20, 4)
    CompareMultiplayerPlayerCount(12, 1, 1, 2, 3)
    CompareEventFlag(12, 537020032, 1)
    SetConditionGroup(1, 13)
    CompareActiveChrNum(13, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(13, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(13, 60, 3, 75)
    CompareEventFlag(13, 537020174, 1)
    CompareEventFlagValue(13, 1, 2, 6, 4)
    CompareMultiplayerPlayerCount(13, 1, 1, 0, 0)
    CompareEventFlag(13, 537020032, 1)
    SetConditionGroup(1, 14)
    CompareActiveChrNum(14, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(14, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(14, 60, 3, 75)
    CompareEventFlag(14, 537020174, 1)
    CompareEventFlagValue(14, 1, 2, 12, 4)
    CompareMultiplayerPlayerCount(14, 1, 1, 1, 0)
    CompareEventFlag(14, 537020032, 1)
    SetConditionGroup(1, 15)
    CompareActiveChrNum(15, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(15, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(15, 60, 3, 75)
    CompareEventFlag(15, 537020174, 1)
    CompareEventFlagValue(15, 1, 2, 20, 4)
    CompareMultiplayerPlayerCount(15, 1, 1, 2, 3)
    CompareEventFlag(15, 537020032, 1)
    if ConditionGroup(0):
        pass
    elif ConditionGroup(1):
        """State 10: Wait just before generation"""
        CompareEventFlag(0, flag2, 1)
        CompareEventFlag(0, 537020175, 1)
        CompareStateTime(1, 2, 3, 5)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 11: Generation"""
            return 0
    """State 12: Clear and sealed"""
    return 1
    """Unused"""
    """State 2: Phase 1 2 or less"""
    SetConditionGroup(1, 8)
    CompareActiveChrNum(8, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(8, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(8, 4, 3, 8)
    CompareEventFlag(8, 537020170, 1)
    CompareEventFlag(8, 537020172, 0)
    Quit()
    """State 3: Phase 1 3 or more"""
    SetConditionGroup(1, 9)
    CompareActiveChrNum(9, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(9, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(9, 20, 3, 30)
    CompareEventFlag(9, 537020170, 1)
    CompareEventFlag(9, 537020172, 0)
    Quit()
    """State 4: Phase 3 2 or less White 0"""
    SetConditionGroup(1, 10)
    CompareActiveChrNum(10, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(10, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(10, 35, 3, 45)
    CompareEventFlag(10, 537020174, 1)
    CompareEventFlagValue(10, 1, 2, 6, 4)
    CompareMultiplayerPlayerCount(10, 1, 1, 0, 0)
    Quit()
    """State 5: Phase 3 2 or less White 1"""
    SetConditionGroup(1, 11)
    CompareActiveChrNum(11, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(11, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(11, 35, 3, 45)
    CompareEventFlag(11, 537020174, 1)
    CompareEventFlagValue(11, 1, 2, 12, 4)
    CompareMultiplayerPlayerCount(11, 1, 1, 1, 0)
    Quit()
    """State 6: Phase 3 2 or less White 2"""
    SetConditionGroup(1, 12)
    CompareActiveChrNum(12, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(12, z14, z19, z20, 0, 0, 2, 5)
    CompareStateTime(12, 35, 3, 45)
    CompareEventFlag(12, 537020174, 1)
    CompareEventFlagValue(12, 1, 2, 20, 4)
    CompareMultiplayerPlayerCount(12, 1, 1, 2, 3)
    Quit()
    """State 7: Phase 3 3 or more White 0"""
    SetConditionGroup(1, 13)
    CompareActiveChrNum(13, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(13, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(13, 60, 3, 75)
    CompareEventFlag(13, 537020174, 1)
    CompareEventFlagValue(13, 1, 2, 6, 4)
    CompareMultiplayerPlayerCount(13, 1, 1, 0, 0)
    Quit()
    """State 8: Phase 3 3 or more White 1"""
    SetConditionGroup(1, 14)
    CompareActiveChrNum(14, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(14, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(14, 60, 3, 75)
    CompareEventFlag(14, 537020174, 1)
    CompareEventFlagValue(14, 1, 2, 12, 4)
    CompareMultiplayerPlayerCount(14, 1, 1, 1, 0)
    Quit()
    """State 9: Phase 3 3 or more White 2"""
    SetConditionGroup(1, 15)
    CompareActiveChrNum(15, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(15, z14, z19, z20, 0, 0, 3, 3)
    CompareStateTime(15, 60, 3, 75)
    CompareEventFlag(15, 537020174, 1)
    CompareEventFlagValue(15, 1, 2, 20, 4)
    CompareMultiplayerPlayerCount(15, 1, 1, 2, 3)
    Quit()

def event_m50_37_x212(z15=_, z16=_, z17=_, z18=_):
    """[Execution] Black Knight: Generator
    z15: Black Knight ① Generator ID
    z16: Black Knight ② Generator ID
    z17: Black Knight ③ Generator ID
    z18: Disable key guide
    """
    """State 0,3: SFX playback from generator: 70"""
    ChangeOwnObjState(70)
    """State 1: Random generation of black knights"""
    ForceRandomGeneration(1, z15, z16, z17, z18, 0)
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

def event_m50_37_x213(flag2=_, z14=_, z15=_, z16=_, z17=_, z18=_, z19=_, z20=_):
    """[Preset] Black Knight: Generator
    flag2: Sealed flag
    z14: Event group ID
    z15: Black Knight ① Generator ID
    z16: Black Knight ② Generator ID
    z17: Black Knight ③ Generator ID
    z18: Disable key guide
    z19: Other ① Event group ID
    z20: Other ② Event group ID
    """
    """State 0,1: [Reproduction] Black Knight: Generation Generator_SubState"""
    call = event_m50_37_x210(flag2=flag2)
    if call.Get() == 3:
        """State 7: Finish"""
        Label('L0')
        return 1
    elif call.Get() == 1:
        Goto('L0')
    elif call.Get() == 2:
        """State 5: [Condition] Black Knight: Generation Generator_After Defeating Boss_SubState"""
        assert event_m50_37_x365(z14=z14, z19=z19, z20=z20)
        """State 4: [Execution] Black Knight: Generation Generator_After Defeating Boss_SubState"""
        assert event_m50_37_x366(z15=z15, z16=z16, z17=z17, z18=z18, z14=z14, z19=z19, z20=z20)
    elif call.Get() == 0:
        """State 3: [Condition] Black Knight: Generation Generator_SubState"""
        call = event_m50_37_x211(flag2=flag2, z14=z14, z19=z19, z20=z20)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Black Knight: Generation Generator_SubState"""
            assert event_m50_37_x212(z15=z15, z16=z16, z17=z17, z18=z18)
    """State 6: Rerun"""
    return 0

def event_m50_37_x214(flag16=_):
    """[Reproduction] NPC gesture management
    flag16: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag16) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_37_x215(z111=_):
    """[Conditions] NPC gesture management
    z111: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z111, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x216(z108=_):
    """[Execution] NPC gesture management
    z108: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z108, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x217(flag17=_, z111=_, z112=_):
    """[Preset] NPC gesture management
    flag17: Defeat flag
    z111: Boss generator ID
    z112: Gesture flag
    """
    """State 0,1: [Reproduction] NPC Gesture Management_SubState"""
    call = event_m50_37_x214(flag16=flag17)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] NPC Gesture Management_SubState"""
        assert event_m50_37_x215(z111=z111)
        """State 2: [Execution] NPC Gesture Management_SubState"""
        assert event_m50_37_x216(z108=z112)
    """State 4: End state"""
    return 0

def event_m50_37_x218(z109=909, z110=910):
    """[Conditions] NPC Gesture Management_2
    z109: Boss ① Generator ID
    z110: Boss ② Generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(8, z109, 0, 5)
    CompareChrHpValue(8, z110, 0, 5)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x219(flag16=537000091, z108=537020092, z109=909, z110=910):
    """[Preset] NPC Gesture Management_2
    flag16: Defeat flag
    z108: Gesture flag
    z109: Boss ① Generator ID
    z110: Boss ② Generator ID
    """
    """State 0,1: [Reproduction] NPC Gesture Management_SubState"""
    call = event_m50_37_x214(flag16=flag16)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] NPC Gesture Management_2 Body Version_SubState"""
        assert event_m50_37_x218(z109=z109, z110=z110)
        """State 2: [Execution] NPC Gesture Management_SubState"""
        assert event_m50_37_x216(z108=z108)
    """State 4: End state"""
    return 0

def event_m50_37_x220():
    """[Reproduction] Sealing instructions"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x221(z94=_, z95=10, z96=_):
    """[Condition] Sealing order
    z94: Phase 1 and 2_ decision seconds
    z95: Phase 3_ judgment seconds
    z96: Phase 1 and 2_Total Defeat Count
    """
    """State 0,1: Sealing order judgment"""
    CompareEventFlag(0, 537020030, 1)
    SetConditionGroup(0, 8)
    CompareAreaTimer(8, 0, z94, 3)
    CompareEventFlag(8, 537020170, 1)
    CompareEventFlagValue(8, 1, 1, z96, 3)
    SetConditionGroup(0, 9)
    CompareAreaTimer(9, 0, z95, 3)
    CompareEventFlag(9, 537020174, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x222(z107=_, val1=_):
    """[Reproduction] Enemy Snowfield Defeat Count
    z107: Defeat count variable
    val1: Maximum number of generations
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Has the number of defeats reached the upper limit?"""
        if (GetAreaVariable(z107) > val1) != 0:
            pass
        else:
            """State 3: End state"""
            return 0
    """State 4: Do nothing: Quit"""
    return 1

def event_m50_37_x223(z106=_, z107=_, val1=_):
    """[Condition] Enemy Snowfield Defeat Count
    z106: Generator ID
    z107: Defeat count variable
    val1: Maximum number of generations
    """
    """State 0,1: Character destruction waiting or upper limit number judgment"""
    IsChrDead(0, z106)
    CompareEventFlagValue(1, 1, z107, val1, 3)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Variable addition"""
        return 0

def event_m50_37_x224(z106=_, z107=_):
    """[Execution] Enemy Snowfield Defeat Count
    z106: Generator ID
    z107: Defeat count variable
    """
    """State 0,1: [Condition] Ice King Battle_Start_SubState"""
    AddAreaVariable(z107, 1)
    """State 2: Wait for generator to restart"""
    IsChrActive(0, z106, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m50_37_x225(z106=_, z107=_, val1=_):
    """[Preset] Defeat count of snowfield enemies
    z106: Generator ID
    z107: Defeat count variable
    val1: Maximum number of generations
    """
    """State 0,1: [Reproduction] Snowfield enemy defeat count _SubState"""
    call = event_m50_37_x222(z107=z107, val1=val1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Snowfield Enemy Defeat Count_SubState"""
        call = event_m50_37_x223(z106=z106, z107=z107, val1=val1)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Snowfield Enemy Defeat Count_SubState"""
            assert event_m50_37_x224(z106=z106, z107=z107)
            """State 4: Rerun"""
            return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x226(z105=537000011):
    """[Condition] Frozen treasure chest
    z105: Seal release flag
    """
    """State 0,1: Was the shrine maiden sealed?"""
    CompareEventFlag(0, z105, 1)
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

def event_m50_37_x229(z105=537000011):
    """[Preset] Frozen treasure chest
    z105: Seal release flag
    """
    """State 0,1: [Reproduction] Frozen treasure chest_SubState"""
    assert event_m50_37_x228()
    """State 3: [Condition] Frozen treasure chest_SubState"""
    assert event_m50_37_x226(z105=z105)
    """State 2: [Execution] Frozen treasure chest_SubState"""
    assert event_m50_37_x227()
    """State 4: End state"""
    return 0

def event_m50_37_x230(z100=762, z102=60375000):
    """[Condition] NPC mimicry control_map_start judgment
    z100: Generator ID
    z102: Mimicry activation_Special effect ID
    """
    """State 0,1: NPC special effect judgment"""
    ChrHasSpEffect(0, z100, z102, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x231(z101=537020063, z104=_):
    """[Execution] NPC mimic control_map
    z101: Mimicry flag
    z104: ON / OFF
    """
    """State 0,1: Mimic flag switching"""
    SetEventFlag(z101, z104)
    """State 2: End state"""
    return 0

def event_m50_37_x232(z100=762, z103=60375001):
    """[Condition] NPC mimic control_map_end judgment
    z100: Generator ID
    z103: Mimicry lottery_Special effect ID
    """
    """State 0,1: NPC generation judgment and special effect judgment"""
    ChrHasSpEffect(0, z100, z103, 0)
    IsChrActive(0, z100, 0)
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

def event_m50_37_x235(z100=762, z101=537020063, z102=60375000, z103=60375001):
    """[Preset] NPC mimic control_map
    z100: Generator ID
    z101: Mimicry flag
    z102: Mimicry activation_Special effect ID
    z103: Mimicry lottery_Special effect ID
    """
    """State 0,1: [Reproduction] NPC mimic control_map_SubState"""
    call = event_m50_37_x234()
    if call.Get() == 1:
        """State 8: Finish"""
        return 1
    elif call.Get() == 0:
        """State 4: [Condition] NPC mimicry control_Map_Start judgment_SubState"""
        assert event_m50_37_x230(z100=z100, z102=z102)
        """State 3: [Execution] NPC mimic control_map_SubState"""
        assert event_m50_37_x231(z101=z101, z104=1)
        """State 2: [Reproduce] NPC mimic control_map_empty_SubState"""
        assert event_m50_37_x233()
        """State 5: [Condition] NPC mimic control_map_end judgment_SubState"""
        assert event_m50_37_x232(z100=z100, z103=z103)
        """State 6: [Execution] NPC mimic control_map_2_SubState"""
        assert event_m50_37_x231(z101=z101, z104=0)
        """State 7: Rerun"""
        return 0

def event_m50_37_x236():
    """[Reproduction] NPC mimic control _ character"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x237(z97=537020063):
    """[Condition] NPC mimicry control_character
    z97: Mimicry flag
    """
    """State 0,1: Mimicry flag judgment"""
    CompareEventFlag(0, z97, 1)
    assert ConditionGroup(0)
    """State 2: Mimic"""
    return 0

def event_m50_37_x238(z98=60375001, z99=762):
    """[Execution] NPC mimic control _ character
    z98: Mimicry lottery_Special effect ID
    z99: Generator ID
    """
    """State 0,1: Giving special effects of mimicry lottery"""
    SetEnemySpEffect(z99, z98, 19, 4)
    """State 2: End state"""
    return 0

def event_m50_37_x239(z97=537020063, z98=60375001, z99=762):
    """[Preset] NPC mimicry control_character
    z97: Mimicry flag
    z98: Mimicry lottery_Special effect ID
    z99: Generator ID
    """
    """State 0,1: [Reproduction] NPC mimicry control_character_SubState"""
    assert event_m50_37_x236()
    """State 3: [Condition] NPC mimicry control_Character_SubState"""
    assert event_m50_37_x237(z97=z97)
    """State 2: [Map] SFX tracking setting in front of the camera"""
    assert event_m50_37_x238(z98=z98, z99=z99)
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

def event_m50_37_x241(z94=_, z95=10, z96=_):
    """[Preset] Sealing instructions
    z94: Phase 1 and 2_ decision seconds
    z95: Phase 3_ judgment seconds
    z96: Phase 1 and 2_Total Defeat Count
    """
    """State 0,1: [Reproduction] Sealing instruction _SubState"""
    assert event_m50_37_x220()
    """State 3: [Condition] Sealing instruction_SubState"""
    assert event_m50_37_x221(z94=z94, z95=z95, z96=z96)
    """State 2: [Execution] Sealing instruction _SubState"""
    assert event_m50_37_x240()
    """State 4: End state"""
    return 0

def event_m50_37_x242():
    """[Reproduction] Sealing production"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x243(z87=794, z88=795, z89=796, z90=797):
    """[Conditions] Sealing production
    z87: White Knight ① Generator ID
    z88: White Knight ② Generator ID
    z89: White Knight ③ Generator ID
    z90: White Knight ④ Generator ID
    """
    """State 0,1: Has the white knight destroyed the generator?"""
    ChrHasSpEffect(0, z87, 96880200, 1)
    ChrHasSpEffect(0, z88, 96880200, 1)
    ChrHasSpEffect(0, z89, 96880200, 1)
    ChrHasSpEffect(0, z90, 96880200, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x244(flag15=_, z91=_, z92=_, z93=_):
    """[Execution] Sealing production
    flag15: Sealed flag
    z91: Next judgment weight
    z92: Generator OBJ instance ID
    z93: Ice OBJ instance ID
    """
    """State 0,1: Seal flag ON"""
    SetEventFlag(flag15, 1)
    assert GetEventFlag(flag15) != 0
    """State 3: Sealing instruction flag OFF"""
    SetEventFlag(537020030, 0)
    assert GetEventFlag(537020030) != 1
    """State 5: Ice appearance: 70"""
    ChangeObjState(z93, 70)
    """State 6: Waiting for the appearance of ice"""
    CompareObjState(0, z93, 20, 0)
    assert ConditionGroup(0)
    """State 4: Generator seal: 20"""
    ChangeObjState(z92, 20)
    """State 2: Wait for next judgment"""
    CompareStateTime(0, z91, 3, z91)
    assert ConditionGroup(0)
    """State 7: End state"""
    return 0

def event_m50_37_x245(z87=794, z88=795, z89=796, z90=797, flag15=_, z91=_, z92=_, z93=_):
    """[Preset] Sealing production
    z87: White Knight ① Generator ID
    z88: White Knight ② Generator ID
    z89: White Knight ③ Generator ID
    z90: White Knight ④ Generator ID
    flag15: Sealed flag
    z91: Next judgment weight
    z92: Generator OBJ instance ID
    z93: Ice OBJ instance ID
    """
    """State 0,1: [Reproduction] Sealing production_SubState"""
    assert event_m50_37_x242()
    """State 3: [Condition] Sealing production_SubState"""
    assert event_m50_37_x243(z87=z87, z88=z88, z89=z89, z90=z90)
    """State 2: [Execution] Sealing production_SubState"""
    assert event_m50_37_x244(flag15=flag15, z91=z91, z92=z92, z93=z93)
    """State 4: End state"""
    return 0

def event_m50_37_x246():
    """[Reproduction] Production sound when falling"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x247(z85=3002000):
    """[Condition] Production sound when falling
    z85: Playback judgment point ID
    """
    """State 0,1: Playback point judgment"""
    IsPlayerInsidePoint(0, z85, z85, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x248(z86=30020):
    """[Execution] Production sound when falling
    z86: Event sound ID
    """
    """State 0,1: Impact sound playback"""
    PlaySoundAtPoint(z86)
    """State 2: End state"""
    return 0

def event_m50_37_x249(z85=3002000, z86=30020):
    """[Preset] Production sound when falling
    z85: Playback judgment point ID
    z86: Event sound ID
    """
    """State 0,1: [Reproduction] Production sound at fall_SubState"""
    assert event_m50_37_x246()
    """State 3: [Condition] Production sound at fall_SubState"""
    assert event_m50_37_x247(z85=z85)
    """State 2: [Execution] Production sound at fall_SubState"""
    assert event_m50_37_x248(z86=z86)
    """State 4: End state"""
    return 0

def event_m50_37_x250(flag14=537000018):
    """[Reproduction] Tiger cry production
    flag14: Event completion flag
    """
    """State 0,1: Have you ever executed an event?"""
    if GetEventFlag(flag14) != 0:
        """State 3: Executed"""
        return 1
    else:
        """State 2: Not executed"""
        return 0

def event_m50_37_x251(z84=2502000):
    """[Condition] Tiger cry production
    z84: Playback judgment point ID
    """
    """State 0,1: Playback judgment"""
    IsPlayerInsidePoint(8, z84, z84, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x252(z82=25020, z83=1, flag14=537000018):
    """[Execution] Tiger cry production
    z82: Event sound ID
    z83: Wait until playback
    flag14: Event completion flag
    """
    """State 0,3: Event completion flag ON"""
    SetEventFlag(flag14, 1)
    """State 2: Wait until playback"""
    CompareStateTime(0, z83, 3, z83)
    assert ConditionGroup(0)
    """State 1: Play sound"""
    PlaySoundAtPoint(z82)
    """State 4: End state"""
    return 0

def event_m50_37_x253(z82=25020, z83=1, z84=2502000, flag14=537000018):
    """[Preset] Tiger cry production
    z82: Event sound ID
    z83: Wait until playback
    z84: Playback judgment point
    flag14: Event completion flag
    """
    """State 0,1: [Reproduction] Tiger cry production_SubState"""
    call = event_m50_37_x250(flag14=flag14)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Tiger cry production_SubState"""
        assert event_m50_37_x251(z84=z84)
        """State 2: [Execution] Tiger cry production_SubState"""
        assert event_m50_37_x252(z82=z82, z83=z83, flag14=flag14)
    """State 4: End state"""
    return 0

def event_m50_37_x254(z81=503701, flag13=537000011):
    """[Condition] Multi-prohibition until conversation with a shrine maiden
    z81: Multiplayer section ID
    flag13: Judgment flag
    """
    """State 0,1: Are you not talking to a shrine maiden and a tiger?"""
    IsPlayerInMultiplayerSection(8, z81, 1)
    CompareEventFlag(8, flag13, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x255(z81=503701, flag13=537000011):
    """[Execution] Multi-prohibition until conversation with shrine maiden
    z81: Multiplayer section ID
    flag13: Judgment flag
    """
    """State 0,1: Multi prohibited"""
    ProhibitMultiplayer(1)
    """State 2: Wait for next judgment"""
    IsPlayerInMultiplayerSection(0, z81, 0)
    CompareEventFlag(0, flag13, 1)
    assert ConditionGroup(0)
    """State 3: Multi effective"""
    ProhibitMultiplayer(0)
    """State 4: End state"""
    return 0

def event_m50_37_x256(flag13=537000011):
    """[Reproduction] Multi-prohibition until conversation with a shrine maiden
    flag13: Judgment flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 1: Have you already talked?"""
        if GetEventFlag(flag13) != 0:
            pass
        else:
            """State 3: Not talking"""
            return 0
    else:
        pass
    """State 4: Conversation: End"""
    return 1

def event_m50_37_x257(z81=503701, flag13=537000011):
    """[Preset] Multi-prohibition until conversation with a shrine maiden
    z81: Multiplayer section ID
    flag13: Judgment flag
    """
    """State 0,1: [Reproduction] Multi-prohibited until conversation with a shrine maiden_SubState"""
    call = event_m50_37_x256(flag13=flag13)
    if call.Get() == 1:
        """State 4: Finish"""
        return 0
    elif call.Get() == 0:
        """State 3: [Condition] Multi-prohibition until conversation with a shrine maiden_SubState"""
        assert event_m50_37_x254(z81=z81, flag13=flag13)
        """State 2: [Execution] Multi-prohibited until conversation with a shrine maiden_SubState"""
        assert event_m50_37_x255(z81=z81, flag13=flag13)
        """State 5: Rerun"""
        return 1

def event_m50_37_x258(z80=2050000):
    """[Reproduction] Frozen Mimic_with body
    z80: Navigation change point ID
    """
    """State 0,1: Navigation switching: Not allowed"""
    AddNavimeshAttribute(z80, 2)
    """State 2: End state"""
    return 0

def event_m50_37_x259(z78=50373001):
    """[Condition] Frozen Mimic_with body
    z78: Ice OBJ instance ID
    """
    """State 0,1: Did the ice disappear?"""
    CompareObjState(0, z78, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x260(z79=537000070, z80=2050000):
    """[Execution] Frozen Mimic_with body
    z79: Generate flag
    z80: Navigation change point ID
    """
    """State 0,1: Generation flag ON"""
    SetEventFlag(z79, 1)
    """State 2: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z80, 2)
    """State 3: End state"""
    return 0

def event_m50_37_x261(z78=50373001, z79=537000070, z80=2050000):
    """[Preset] Frozen Mimic_with body
    z78: Ice OBJ instance ID
    z79: Generate flag
    z80: Navigation change point ID
    """
    """State 0,1: [Reproduction] Frozen Mimic_Body_SubState"""
    assert event_m50_37_x258(z80=z80)
    """State 3: Is it a hostile spirit?"""
    assert event_m50_37_x259(z78=z78)
    """State 2: [Execution] Frozen Mimic_Body_SubState"""
    assert event_m50_37_x260(z79=z79, z80=z80)
    """State 4: End state"""
    return 0

def event_m50_37_x262(z77=50371620):
    """[Condition] Frozen Mimic_No body
    z77: Ice OBJ instance ID
    """
    """State 0,1: Did the ice disappear?"""
    CompareObjState(0, z77, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x263(z76=50375720):
    """[Reproduction] Frozen Mimic _ No body
    z76: Treasure chest OBJ instance ID
    """
    """State 0,1: Treasure chest key guide OFF"""
    DisableObjKeyGuide(z76, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x264(z75=537000071, z76=50375720):
    """[Execution] Frozen Mimic _ No body
    z75: Generate flag
    z76: Treasure chest OBJ instance ID
    """
    """State 0,2: Hide treasure chest"""
    ChangeDrawHit(z76, 0)
    """State 1: Generation flag ON"""
    SetEventFlag(z75, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x265(z75=537000071, z76=50375720, z77=50371620):
    """[Preset] Frozen Mimic _ No body
    z75: Generate flag
    z76: Treasure chest OBJ instance ID
    z77: Ice OBJ instance ID
    """
    """State 0,1: [Reproduction] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x263(z76=z76)
    """State 3: [Condition] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x262(z77=z77)
    """State 2: [Execution] Frozen Mimic_No Body_SubState"""
    assert event_m50_37_x264(z75=z75, z76=z76)
    """State 4: End state"""
    return 0

def event_m50_37_x266(z74=50372800):
    """[Reproduction] Frozen insect key
    z74: Bug key OBJ instance ID
    """
    """State 0,1: Bug Key Key Guide OFF"""
    DisableObjKeyGuide(z74, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x267(z73=50372802):
    """[Condition] Frozen insect key
    z73: Ice OBJ instance ID
    """
    """State 0,1: Did the ice melt?"""
    CompareObjState(0, z73, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x268(z74=50372800):
    """[Execution] Frozen insect key
    z74: Bug key OBJ instance ID
    """
    """State 0,1: Bug Key Key Guide ON"""
    DisableObjKeyGuide(z74, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x269(z73=50372802, z74=50372800):
    """[Preset] Frozen insect key
    z73: Ice OBJ instance ID
    z74: Bug key OBJ instance ID
    """
    """State 0,1: [Reproduction] Frozen insect key _SubState"""
    assert event_m50_37_x266(z74=z74)
    """State 3: [Condition] Frozen insect key _SubState"""
    assert event_m50_37_x267(z73=z73)
    """State 2: [Execution] Frozen insect key _SubState"""
    assert event_m50_37_x268(z74=z74)
    """State 4: End state"""
    return 0

def event_m50_37_x270(flag12=537000086):
    """[Reproduction] White knight falling with PC following
    flag12: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag12) != 0:
        """State 3: Defeated: No follow-up"""
        return 1
    else:
        """State 2: Before defeat"""
        return 0

def event_m50_37_x271(z71=3004000):
    """[Condition] White knight falling with PC following
    z71: Judgment point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(8, z71, z71, 1)
    IsHost(8, 1, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m50_37_x272(z72=537020024):
    """[Execution] White knight falling with PC following
    z72: Follow flag
    """
    """State 0,1: Follow flag ON"""
    SetEventFlag(z72, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x273(z71=3004000, z72=537020024, flag12=537000086):
    """[Preset] White knight falling with PC following
    z71: Judgment point ID
    z72: Follow flag
    flag12: Defeat flag
    """
    """State 0,1: [Reproduction] White Knight_SubState falling with PC following"""
    call = event_m50_37_x270(flag12=flag12)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] White Knight_SubState falling with PC following"""
        assert event_m50_37_x271(z71=z71)
        """State 2: [Execution] Falling white knight in PC following_SubState"""
        assert event_m50_37_x272(z72=z72)
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

def event_m50_37_x276(z31=537020085):
    """[Execution] Ice King Battle Phase 1
    z31: Other flags for logic
    """
    """State 0,2: Start battle start timer"""
    StartAreaTimer(0)
    """State 3: Phase 1 flag ON"""
    SetEventFlag(537020170, 1)
    """State 1: Boss battle flag notification for logic"""
    SetEventFlag(z31, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x277(z66=_):
    """[Conditions] Ochikage to Miko
    z66: Stage seal release flag
    """
    """State 0,1: Stage seal release flag judgment"""
    CompareEventFlag(0, z66, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x278(z67=_, z68=_, z69=_, z70=3):
    """[Execution] Ochikage to Miko
    z67: Ice OBJ instance ID
    z68: Change navigation ① Point ID
    z69: Change navigation ② Point ID
    z70: weight
    """
    """State 0,4: Weight until destruction"""
    CompareStateTime(0, z70, 3, z70)
    assert ConditionGroup(0)
    """State 1: The disappearance of the ice OBJ: 70"""
    ChangeObjState(z67, 70)
    """State 2: Waiting for ice to disappear"""
    CompareObjState(0, z67, 20, 0)
    assert ConditionGroup(0)
    """State 3: Navigation switching: Traffic is possible"""
    DeleteNavimeshAttribute(z68, 2)
    DeleteNavimeshAttribute(z69, 2)
    """State 5: End state"""
    return 0

def event_m50_37_x279(z67=_, z68=_, z69=_):
    """[Reproduction] Ochikage to Miko
    z67: Ice OBJ instance ID
    z68: Change navigation ① Point ID
    z69: Change navigation ② Point ID
    """
    """State 0,1: Is the ice in its initial state?"""
    if CompareObjStateId(z67, 10, 1):
        """State 3: Waiting for ice to disappear"""
        assert CompareObjStateId(z67, 20, 0)
        """State 4: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z68, 2)
        DeleteNavimeshAttribute(z69, 2)
        """State 6: Executed"""
        return 1
    else:
        """State 2: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z68, 2)
        AddNavimeshAttribute(z69, 2)
        """State 5: Not executed"""
        return 0

def event_m50_37_x280(z66=_, z67=_, z68=_, z69=_, z70=3):
    """[Preset] Ochikage to Miko
    z66: Stage seal release flag
    z67: Ice OBJ instance ID
    z68: Change navigation ① Point ID
    z69: Change navigation ② Point ID
    z70: weight
    """
    """State 0,1: [Reproduction] Ochikazu _SubState to the shrine maiden"""
    call = event_m50_37_x279(z67=z67, z68=z68, z69=z69)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] A Submission to a Maiden_SubState"""
        assert event_m50_37_x277(z66=z66)
        """State 2: [Execution] A maiden to a shrine _SubState"""
        assert event_m50_37_x278(z67=z67, z68=z68, z69=z69, z70=z70)
    """State 4: End state"""
    return 0

def event_m50_37_x281(z64=50372601, z65=2400000):
    """[Reproduction] Transporter operated by lever
    z64: Transporter OBJ instance ID
    z65: Navigation change point ID
    """
    """State 0,1: Is the transporter already in operation?"""
    if CompareObjStateId(z64, 10, 1):
        """State 3: Waiting for operation"""
        assert CompareObjStateId(z64, 20, 0)
        """State 2: Navigation switching: Traffic is possible"""
        DeleteNavimeshAttribute(z65, 2)
        """State 6: Already in operation"""
        return 1
    else:
        """State 4: Navigation switching: Not allowed"""
        AddNavimeshAttribute(z65, 2)
        """State 5: Not in operation"""
        return 0

def event_m50_37_x282(z63=50372600):
    """[Conditions] Transporter operated by lever
    z63: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z63, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x283(z64=50372601, z65=2400000):
    """[Execution] Transporter operated by lever
    z64: Transporter OBJ instance ID
    z65: Navigation change point ID
    """
    """State 0,2: The transporter is in operation: 70"""
    ChangeObjState(z64, 70)
    """State 3: Waiting for completion of operation of transporter"""
    CompareObjState(0, z64, 20, 0)
    assert ConditionGroup(0)
    """State 1: Navigation change: Allowed to pass"""
    DeleteNavimeshAttribute(z65, 2)
    """State 4: End state"""
    return 0

def event_m50_37_x284(z63=50372600, z64=50372601, z65=2400000):
    """[Preset] Transporter operated by lever
    z63: Lever OBJ instance ID
    z64: Transporter OBJ instance ID
    z65: Navigation change point ID
    """
    """State 0,1: [Reproduction] Transporter _SubState operated by lever"""
    call = event_m50_37_x281(z64=z64, z65=z65)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Transporter operated by lever_SubState"""
        assert event_m50_37_x282(z63=z63)
        """State 2: [Execution] Transporter operated by lever_SubState"""
        assert event_m50_37_x283(z64=z64, z65=z65)
    """State 4: End state"""
    return 0

def event_m50_37_x285(z57=_, z58=_, z59=_, flag11=_, z60=_, z61=_, z62=_):
    """[Condition] Generation delay on appearance
    z57: Generation delay time
    z58: Generateable_start point ID
    z59: Generateable_end point ID
    flag11: Delayed completion flag
    z60: Generator ID
    z61: Defeat count
    z62: Maximum number of generations
    """
    """State 0,1: Delay judgment"""
    IsChrActive(8, z60, 0)
    CompareEventFlag(8, 537020015, 1)
    IsPlayerInsidePoint(8, 600080, 600099, 0)
    IsPlayerInsidePoint(8, z58, z59, 1)
    CompareEventFlag(0, flag11, 1)
    CompareEventFlagValue(0, 1, z61, z62, 3)
    if ConditionGroup(0):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(8):
        """State 2: delay"""
        return 0

def event_m50_37_x286(z57=_, flag11=_):
    """[Execution] Generation delay on appearance
    z57: Generation delay time
    flag11: Delayed completion flag
    """
    """State 0,1: During generation delay"""
    CompareStateTime(0, z57, 3, z57)
    CompareEventFlag(0, flag11, 1)
    assert ConditionGroup(0)
    """State 2: Delay completion flag ON"""
    SetEventFlag(flag11, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x287(flag11=_):
    """[Reproduction] Generation delay at the time of appearance
    flag11: Delayed completion flag
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
    if GetEventFlag(flag11) != 0:
        """State 4: Delayed"""
        return 1
    else:
        """State 3: First time"""
        return 0

def event_m50_37_x288(z57=_, z58=_, z59=_, flag11=_, z60=_, z61=_, z62=_):
    """[Preset] Delay in generation
    z57: Generation delay time
    z58: Generateable_start point ID
    z59: Generateable_end point ID
    flag11: Delayed completion flag
    z60: Generator ID
    z61: Defeat count
    z62: Maximum number of generations
    """
    """State 0,1: [Reproduction] Generation delay at appearance_SubState"""
    call = event_m50_37_x287(flag11=flag11)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Generation delay at appearance_SubState"""
        assert event_m50_37_x285(z57=z57, z58=z58, z59=z59, flag11=flag11, z60=z60, z61=z61, z62=z62)
        """State 2: [Execution] Generation delay at appearance_SubState"""
        assert event_m50_37_x286(z57=z57, flag11=flag11)
    """State 4: End state"""
    return 0

def event_m50_37_x289(z55=5037010):
    """[Condition] Operation of the second tiger
    z55: Boss Battle ID
    """
    """State 0,5: Has the boss battle started?"""
    IsEventBossBattle(0, z55, 1)
    assert ConditionGroup(0)
    """State 6: Start battle start timer"""
    StartAreaTimer(0)
    """State 2: Multi-person determination"""
    CompareMultiplayerPlayerCount(0, 1, 1, 2, 3)
    CompareMultiplayerPlayerCount(1, 1, 1, 1, 0)
    CompareMultiplayerPlayerCount(2, 1, 1, 0, 0)
    if ConditionGroup(0):
        """State 4: Start-up judgment_Friend 2"""
        CompareEventBossHpRatio(0, z55, 2, 100, 4)
        CompareEventBossHpRatio(0, z55, 1, 80, 5)
        CompareAreaTimer(0, 0, 30, 3)
        CompareMultiplayerPlayerCount(1, 1, 1, 2, 4)
        if ConditionGroup(1):
            """State 3: Start-up judgment_Friend 1"""
            Label('L0')
            CompareEventBossHpRatio(0, z55, 2, 100, 4)
            CompareEventBossHpRatio(0, z55, 1, 60, 5)
            CompareAreaTimer(0, 0, 60, 3)
            CompareMultiplayerPlayerCount(1, 1, 1, 1, 4)
            if ConditionGroup(1):
                """State 1: Start judgment_host only"""
                Label('L1')
                CompareEventBossHpRatio(0, z55, 2, 100, 4)
                CompareEventBossHpRatio(0, z55, 1, 40, 5)
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

def event_m50_37_x290(z56=537020093):
    """[Execution] Operation of the second tiger
    z56: Startup flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z56, 1)
    """State 2: Battle start timer stop"""
    EndAreaTimer(0)
    """State 3: End state"""
    return 0

def event_m50_37_x291(flag10=537000091):
    """[Reproduction] Operation of the second tiger
    flag10: Defeat flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: Have you already destroyed the boss?"""
        if GetEventFlag(flag10) != 1:
            """State 3: Host: Undefeated"""
            return 0
        else:
            pass
    else:
        pass
    """State 4: Finish"""
    return 1

def event_m50_37_x292(flag10=537000091, z55=5037010, z56=537020093):
    """[Preset] Operation of the second tiger
    flag10: Defeat flag
    z55: Boss Battle ID
    z56: Startup flag
    """
    """State 0,1: [Reproduction] Operation of the second tiger _SubState"""
    call = event_m50_37_x291(flag10=flag10)
    if call.Get() == 0:
        """State 3: [Condition] Second tiger in operation _SubState"""
        assert event_m50_37_x289(z55=z55)
        """State 2: [Execution] Second tiger in operation _SubState"""
        assert event_m50_37_x290(z56=z56)
    elif call.Get() == 1:
        pass
    """State 4: Finish"""
    return 0

def event_m50_37_x293(flag9=537000091):
    """[Reproduction] Black Tiger Battle_Start
    flag9: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag9) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m50_37_x294(z49=3500000, z50=3500000):
    """[Condition] Black Tiger Battle_Start
    z49: Start point ID
    z50: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z49, z50, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z49, z50, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x295(z51=503, z52=5037010, z53=537020090):
    """[Execution] Black Tiger Battle_Start
    z51: Sound ID
    z52: Boss Battle ID
    z53: Tiger first body start flag
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z51)
    """State 1: Boss battle start notification"""
    StartBossFight(z52)
    """State 2: Boss battle flag notification for the first tiger for logic"""
    SetEventFlag(z53, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x296():
    """[Reproduction] Black Tiger Battle_2"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x297(z52=5037010):
    """[Condition] Black Tiger Battle_End
    z52: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z52, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x298(z51=503, z52=5037010, mode1=0, z53=537020090, z54=537020093):
    """[Execution] Black Tiger Battle_End
    z51: Sound ID
    z52: Boss Battle ID
    mode1: BGM stop time
    z53: Tiger first body start flag
    z54: Tiger second body start flag
    """
    """State 0,1: Tiger start flag OFF"""
    SetEventFlag(z53, 0)
    SetEventFlag(z54, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z52)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z51)
    """State 5: End state"""
    return 0

def event_m50_37_x299(z54=537020093):
    """[Condition] Black Tiger Battle_2
    z54: Tiger second body start flag
    """
    """State 0,1: Start-up judgment: 2nd tiger"""
    CompareEventFlag(0, z54, 1)
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

def event_m50_37_x302(flag9=537000091, z49=3500000, z50=3500000, z51=503, z52=5037010, mode1=0, z53=537020090,
                      z54=537020093):
    """[Preset] Black Tiger Battle
    flag9: Boss destruction flag
    z49: Start point ID
    z50: End point ID
    z51: Sound ID
    z52: Boss Battle ID
    mode1: BGM stop time
    z53: Tiger first body start flag
    z54: Tiger second body start flag
    """
    """State 0,2: [Reproduction] Black Tiger Battle_Start_SubState"""
    call = event_m50_37_x293(flag9=flag9)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 8: [Condition] Black Tiger Battle_Start_SubState"""
        assert event_m50_37_x294(z49=z49, z50=z50)
        """State 5: [Execution] Black Tiger Battle_Start_SubState"""
        assert event_m50_37_x295(z51=z51, z52=z52, z53=z53)
        """State 1: [Reproduction] Black Tiger Battle _ 2nd Start_Sky_SubState"""
        assert event_m50_37_x296()
        """State 7: [Condition] Black Tiger Battle_2"""
        assert event_m50_37_x299(z54=z54)
        """State 4: [Execution] Black Tiger Battle_2 Start-up_SubState"""
        assert event_m50_37_x300()
        """State 3: [Reproduction] Black Tiger Battle_End_Sky_SubState"""
        assert event_m50_37_x301()
        """State 9: [Condition] Black Tiger Battle_End_SubState"""
        assert event_m50_37_x297(z52=z52)
        """State 6: [Execution] Black Tiger Battle_End_SubState"""
        assert event_m50_37_x298(z51=z51, z52=z52, mode1=mode1, z53=z53, z54=z54)
    """State 10: End state"""
    return 0

def event_m50_37_x303(flag8=103400):
    """[Reproduction] Event between DLCs
    flag8: Defeat flag
    """
    """State 0,1: Already destroyed?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m50_37_x304(z48=5320):
    """[Condition] Event between DLCs
    z48: Generator ID
    """
    """State 0,1: Waiting for destruction"""
    IsChrDeadOrRespawnOver(0, z48, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x305(flag8=103400):
    """[Execution] Event between DLCs
    flag8: Defeat flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag8, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x306(flag8=103400, z48=5320):
    """[Preset] DLC event
    flag8: Defeat flag
    z48: Generator ID
    """
    """State 0,1: [Reproduction] Inter-DLC event"""
    call = event_m50_37_x303(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Event between DLCs"""
        assert event_m50_37_x304(z48=z48)
        """State 2: [Execution] Event between DLCs"""
        assert event_m50_37_x305(flag8=flag8)
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

def event_m50_37_x311(flag6=537000019, flag7=103303):
    """[Reproduction] Acquired Seoul by the death of a shrine maiden
    flag6: Seoul acquisition other flags
    flag7: Seoul acquisition global flag
    """
    """State 0,3: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Have you acquired the maiden soul in conversation?"""
        if GetEventFlag(flag7) != 0:
            pass
        else:
            """State 2: Have you acquired Seoul in this event?"""
            if GetEventFlag(flag6) != 0:
                pass
            else:
                """State 4: Unacquired"""
                return 0
    """State 5: Finish"""
    return 1

def event_m50_37_x312(z47=340, flag7=103303):
    """[Condition] Seoul won by the death of a shrine maiden
    z47: Generator ID
    flag7: Seoul acquisition global flag
    """
    """State 0,1: Did you kill the shrine maiden?"""
    IsChrDeadOrRespawnOver(0, z47, 1)
    CompareEventFlag(1, flag7, 1)
    if ConditionGroup(1):
        """State 3: Obtained in conversation"""
        return 1
    elif ConditionGroup(0):
        """State 2: Killed"""
        return 0

def event_m50_37_x313(flag6=537000019):
    """[Execution] Seoul won by the death of a shrine maiden
    flag6: Seoul acquisition other flags
    """
    """State 0,1: Item acquisition"""
    # lot:1788030:Soul of Alsanna, Silent Oracle
    AwardItem(1788030, 1)
    """State 2: Acquisition flag ON"""
    SetEventFlag(flag6, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x314(flag6=537000019, z47=340, flag7=103303):
    """[Preset] Seoul won by the death of a shrine maiden
    flag6: Seoul acquisition other flags
    z47: Generator ID
    flag7: Seoul acquisition global flag
    """
    """State 0,1: [Reproduction] Seoul gained by the death of a shrine maiden_SubState"""
    call = event_m50_37_x311(flag6=flag6, flag7=flag7)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Seoul gained due to the death of a shrine maiden_SubState"""
        call = event_m50_37_x312(z47=z47, flag7=flag7)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Acquisition of Seoul by the death of a shrine maiden_SubState"""
            assert event_m50_37_x313(flag6=flag6)
    """State 4: End state"""
    return 0

def event_m50_37_x315(z44=50372650):
    """[Reproduction] Bakusta activation
    z44: Lever OBJ instance ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Has the lever already been activated?"""
        if CompareObjStateId(z44, 20, 0):
            pass
        elif CompareObjStateId(z44, 72, 0):
            pass
        elif CompareObjStateId(z44, 70, 0):
            pass
        else:
            """State 3: Before startup"""
            return 0
    """State 4: Finish"""
    return 1

def event_m50_37_x316(z44=50372650):
    """[Conditions] Bhaksta launching of escort warrior
    z44: Lever OBJ instance ID
    """
    """State 0,1: Did the player touch the lever?"""
    CompareObjState(0, z44, 10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x317(z45=_):
    """[Execution] Bakusta activation
    z45: Startup flag
    """
    """State 0,1: Start flag ON"""
    SetEventFlag(z45, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x318(z44=50372650, z45=537020003, z46=537020004):
    """[Preset] Samurai Warrior Bakusta Launch
    z44: Lever OBJ instance ID
    z45: Start flag
    z46: Completion flag
    """
    """State 0,1: [Reproduction] Bhaksta launch of Submarine Warrior_SubState"""
    call = event_m50_37_x315(z44=z44)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Bhaksta launching of escort warrior"""
        assert event_m50_37_x316(z44=z44)
        """State 2: [Execution] Samurai Warrior Bakusta Start_Start Pull_SubState"""
        assert event_m50_37_x317(z45=z45)
        """State 5: [Reproduction] Bakusta launching of the life warrior_Sky_SubState"""
        assert event_m50_37_x320()
        """State 4: [Conditions] Bhaksta launching of escort warrior _Cancel or confirmed_SubState"""
        call = event_m50_37_x319(z44=z44)
        if call.Get() == 0:
            """State 6: [Execution] Bhaksta launching of the fighter"""
            assert event_m50_37_x317(z45=z46)
        elif call.Get() == 1:
            """State 7: [Execution] Samurai Warrior Bakusta Launch_Cancel_SubState"""
            assert event_m50_37_x324(z45=z45, z44=z44)
            """State 9: Rerun"""
            return 1
    """State 8: Finish"""
    return 0

def event_m50_37_x319(z44=50372650):
    """[Condition] Bakusta activation of escort warrior _ Cancel or confirm
    z44: Lever OBJ instance ID
    """
    """State 0,1: Cancel or lever confirmation"""
    CompareObjState(0, z44, 71, 0)
    CompareObjState(0, z44, 10, 0)
    CompareObjState(1, z44, 72, 0)
    CompareObjState(1, z44, 20, 0)
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

def event_m50_37_x324(z45=537020003, z44=50372650):
    """[Execution] Resident Warrior Bakusta Launch_Cancel
    z45: Startup flag
    z44: Lever OBJ instance ID
    """
    """State 0,1: Startup flag OFF"""
    SetEventFlag(z45, 0)
    """State 2: Initial waiting for lever"""
    CompareObjState(0, z44, 10, 0)
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

def event_m50_37_x326(z27=5037000):
    """[Condition] Return from the boss room of the white knight
    z27: Boss Battle ID
    """
    """State 0,1: Has the boss battle started?"""
    IsEventBossBattle(0, z27, 1)
    assert ConditionGroup(0)
    """State 2: Has the boss battle ended?"""
    IsEventBossBattle(0, z27, 0)
    assert ConditionGroup(0)
    """State 3: Start of return"""
    return 0

def event_m50_37_x327(z26=_):
    """[Execution] Returning from the White Knight Boss Room
    z26: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z26, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x328(z26=_, z27=5037000, z28=537020025):
    """[Preset] Return from the White Knight Boss Room
    z26: Generator ID
    z27: Boss Battle ID
    z28: Return start flag
    """
    """State 0,1: [Reproduction] Return from the White Knight Boss Room_SubState"""
    call = event_m50_37_x325()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Return from White Knight's Boss Room_Start Judgment_SubState"""
        assert event_m50_37_x326(z27=z27)
        """State 3: [Execution] Return from the White Knight Boss Room_Return Start_SubState"""
        assert event_m50_37_x348(z28=z28)
        """State 6: [Reproduction] Return from the White Knight Boss Room_Sky_SubState"""
        assert event_m50_37_x349()
        """State 5: [Condition] Return from White Knight's Boss Room_Return Judgment_SubState"""
        assert event_m50_37_x347(z26=z26)
        """State 2: [Execution] Returning from the White Knight Boss Room_Character Delete_SubState"""
        assert event_m50_37_x327(z26=z26)
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

def event_m50_37_x331(z41=537020050, z43=_):
    """[Execution] Filter condition judgment_DLC possession
    z41: Filter flag
    z43: ON / OFF
    """
    """State 0,1: Filter flag switching"""
    SetEventFlag(z41, z43)
    """State 2: Finish"""
    return 0

def event_m50_37_x332(z41=537020050, z42=1):
    """[Preset] Filter condition judgment_DLC possession
    z41: Filter flag
    z42: ON / OFF
    """
    """State 0,1: [Reproduction] Filter condition judgment_DLC possession_SubState"""
    assert event_m50_37_x329()
    """State 3: [Condition] Filter condition judgment_DLC possession_SubState"""
    call = event_m50_37_x330()
    if call.Get() == 0:
        """State 4: [Execution] Filter condition judgment_DLC possession_ON_SubState"""
        assert event_m50_37_x331(z41=z41, z43=1)
    elif call.Get() == 1:
        """State 2: [Execution] Filter condition judgment_DLC possession_OFF_SubState"""
        assert event_m50_37_x331(z41=z41, z43=0)
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

def event_m50_37_x335(z38=537020051, z40=1):
    """[Execution] Filter Condition Judgment_First Tiger Battle
    z38: Filter flag
    z40: ON / OFF
    """
    """State 0,1: Filter flag switching"""
    SetEventFlag(z38, z40)
    """State 2: Finish"""
    return 0

def event_m50_37_x336(z38=537020051, z39=1):
    """[Preset] Filter Condition Judgment_First Tiger Battle
    z38: Filter flag
    z39: ON / OFF
    """
    """State 0,1: [Reproduction] Filter Condition Judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x333()
    """State 3: [Condition] Filter condition judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x334()
    """State 2: [Execution] Filter Condition Judgment_First Tiger Battle_SubState"""
    assert event_m50_37_x335(z38=z38, z40=1)
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

def event_m50_37_x339(z36=537020052, z37=1):
    """[Execution] Filter condition judgment_Rematch tiger battle
    z36: Filter flag
    z37: ON / OFF
    """
    """State 0,1: Filter flag switching"""
    SetEventFlag(z36, z37)
    """State 2: Finish"""
    return 0

def event_m50_37_x340(z34=537020052, z35=1):
    """[Preset] Filter Condition Judgment_Rematch Tiger Battle
    z34: Filter flag
    z35: ON / OFF
    """
    """State 0,1: [Reproduction] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x337()
    """State 3: [Condition] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x338()
    """State 2: [Execution] Filter condition judgment_Rematch tiger battle_SubState"""
    assert event_m50_37_x339(z36=537020052, z37=1)
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

def event_m50_37_x343(z32=1300000, z33=50371190):
    """[Preset] Return from Boss Room_Yukihara
    z32: Warp destination point ID
    z33: Warp OBJ instance ID
    """
    """State 0,1: [Reproduction] Return from Boss Room_Yukihara_SubState"""
    assert event_m50_37_x342()
    """State 3: [Condition] Return from the boss room_Judgment to check_SubState"""
    assert event_m50_37_x209(z33=z33)
    """State 2: [Execution] Return from Boss Room_Warp_SubState"""
    assert event_m50_37_x102(z32=z32)
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

def event_m50_37_x347(z26=_):
    """[Condition] Return from White Boss Boss Room_Return Judgment
    z26: Generator ID
    """
    """State 0,1: Return judgment"""
    CompareEventFlag(8, 537020087, 1)
    ChrHasSpEffect(8, z26, 96880100, 1)
    assert ConditionGroup(8)
    """State 2: Delete character"""
    return 0

def event_m50_37_x348(z28=537020025):
    """[Execution] Return from the White Knight's Boss Room_Start Return
    z28: Return start flag
    """
    """State 0,1: Return start flag ON"""
    SetEventFlag(z28, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x349():
    """[Reproduction] Return from the White Knight Boss Room _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x350(z23=50371570, flag4=537000002, z24=537000086, z25=5, action1=5310):
    """[Preset] Crown that appears when a boss is destroyed
    z23: 棺 桶 Activating key guide
    flag4: Crown acquisition flag
    z24: Defeat flag
    z25: weight
    action1: Text ID
    """
    """State 0,1: [Reproduction] Crown _SubState that appears when a boss is destroyed"""
    call = event_m50_37_x351(flag4=flag4, z23=z23)
    if call.Get() == 0:
        """State 7: [Condition] Crown that appears when boss is destroyed _ Defeat determination_SubState"""
        call = event_m50_37_x357(z24=z24)
        if call.Get() == 1:
            """State 9: [Execution] Crown_Sky_SubState that appears when a boss is destroyed"""
            assert event_m50_37_x359()
        elif call.Get() == 0:
            """State 5: [Execution] Crown Appearing at Boss Defeat_Display Crown_SubState"""
            assert event_m50_37_x355(z23=z23)
            """State 2: [Reproduction] Crown _ Sky _ SubState that appears by destroying the boss"""
            assert event_m50_37_x352()
            """State 8: [Condition] Crown that appears when boss is destroyed"""
            call = event_m50_37_x358(z23=z23)
            if call.Get() == 1:
                """State 3: [Execution] Crown that appears by destroying the boss_Key guide switching_SubState"""
                assert event_m50_37_x353(z23=z23)
            elif call.Get() == 0:
                """State 4: [Execution] Crown Appearing at Boss Defeat_Get Crown_SubState"""
                assert event_m50_37_x354(z23=z23, flag4=flag4, z25=z25, action1=action1)
                Goto('L0')
            elif call.Get() == 2:
                """State 10: [Execution] Crown that appears after destroying the boss_Unacquired_SubState"""
                assert event_m50_37_x360(z23=z23)
        """State 12: Rerun"""
        return 1
    elif call.Get() == 2:
        """State 6: [Execution] Crown Appearing by Boss Defeat_Hide_SubState"""
        assert event_m50_37_x356(z23=z23)
    elif call.Get() == 1:
        pass
    """State 11: Finish"""
    Label('L0')
    return 0

def event_m50_37_x351(flag4=537000002, z23=50371570):
    """[Reproduction] Crown that appears when a boss is destroyed
    flag4: Crown acquisition flag
    z23: 棺 桶 Activating key guide
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Have you acquired the crown?"""
    if GetEventFlag(flag4) != 1:
        """State 3: Hide crown"""
        ChangeObjState(z23, 10)
        assert CompareObjStateId(z23, 10, 0)
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

def event_m50_37_x353(z23=50371570):
    """[Execution] Crown that appears when the boss is destroyed
    z23: 棺 桶 Activating key guide
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z23, 1)
    """State 2: Is the boss battle over?"""
    IsEventBossBattle(0, 5037000, 0)
    assert ConditionGroup(0)
    """State 3: Enable key guide"""
    DisableObjKeyGuide(z23, 0)
    """State 4: Rerun"""
    return 0

def event_m50_37_x354(z23=50371570, flag4=537000002, z25=5, action1=5310):
    """[Execution] Crowns that appear when the boss is destroyed
    z23: 棺 桶 Activating key guide
    flag4: Crown acquisition flag
    z25: weight
    action1: Text ID
    """
    """State 0,1: Key guide disabled: 10"""
    ChangeObjState(z23, 10)
    """State 2: Wait for transition"""
    CompareObjState(0, z23, 10, 0)
    assert ConditionGroup(0)
    """State 3: Item acquisition"""
    # lot:60031000:Crown of the Ivory King
    AwardItem(60031000, 1)
    """State 4: Turn on the crown acquisition flag"""
    SetEventFlag(flag4, 1)
    """State 5: weight"""
    CompareStateTime(0, z25, 3, z25)
    assert ConditionGroup(0)
    """State 6: Text display"""
    # action:5310:"A faint heat lingers in the ancient crown"
    DisplayEventMessage(action1, 0, 0, 0)
    assert EventMessageDisplay() != 1
    """State 7: End state"""
    return 0

def event_m50_37_x355(z23=50371570):
    """[Execution] Crowns that appear when a boss is destroyed
    z23: 棺 桶 Activating key guide
    """
    """State 0,1: Crown display: 30"""
    ChangeObjState(z23, 30)
    """State 2: End state"""
    return 0

def event_m50_37_x356(z23=50371570):
    """[Execution] Crowns that appear when the boss is destroyed
    z23: 棺 桶 Activating key guide
    """
    """State 0,1: Crown OBJ hidden: 10"""
    ChangeObjState(z23, 10)
    """State 2: End state"""
    return 0

def event_m50_37_x357(z24=537000086):
    """[Condition] Crown that appears when a boss is destroyed
    z24: Defeat flag
    """
    """State 0,1: Did you defeat the king of ice or become multiplayer?"""
    CompareEventFlag(0, z24, 1)
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

def event_m50_37_x358(z23=50371570):
    """[Conditions] Examining the crown that appears when a boss is destroyed
    z23: 棺 桶 Activating key guide
    """
    """State 0,1: Did you check the crown or became a boss battle?"""
    IsObjSearched(0, z23)
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

def event_m50_37_x360(z23=50371570):
    """[Execution] Crown that appears when the boss is destroyed
    z23: 棺 桶 Activating key guide
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z23, 1)
    """State 1: Acquisition failure window display"""
    # lot:60031000:Crown of the Ivory King
    DisplayItemAwardFailure(60031000, 0, 190)
    assert ItemAwardFailureDisplay() != 0
    """State 2: Waiting for acquisition failure window to be hidden"""
    assert ItemAwardFailureDisplay() != 1
    """State 4: Activate key guide"""
    DisableObjKeyGuide(z23, 0)
    """State 5: End state"""
    return 0

def event_m50_37_x361(z21=_):
    """[Condition] White Knight
    z21: Generator ID
    """
    """State 0,1: White Knight starts sealing or died"""
    ChrHasSpEffect(0, z21, 96880200, 1)
    IsChrDead(0, z21)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x362(z22=_):
    """[Execution] White Knight
    z22: Profession flag
    """
    """State 0,1: Vocational occupation flag ON"""
    SetEventFlag(z22, 1)
    """State 2: End state"""
    return 0

def event_m50_37_x363(z22=_, flag3=537000086):
    """[Reproduction] White Knight
    z22: Profession flag
    flag3: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 3: Has the boss been destroyed?"""
        if GetEventFlag(flag3) != 1:
            """State 1: Vocational occupation flag OFF"""
            SetEventFlag(z22, 0)
            """State 4: Undefeated"""
            return 0
        else:
            pass
    """State 5: Finish"""
    return 1

def event_m50_37_x364(z21=_, z22=_, flag3=537000086):
    """[Preset] White Knight
    z21: Generator ID
    z22: Profession flag
    flag3: Defeat flag
    """
    """State 0,1: [Reproduction] White Knight's profession_SubState"""
    call = event_m50_37_x363(z22=z22, flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] White knight's profession_SubState"""
        assert event_m50_37_x361(z21=z21)
        """State 2: [Execution] White Knight's profession_SubState"""
        assert event_m50_37_x362(z22=z22)
    """State 4: End state"""
    return 0

def event_m50_37_x365(z14=_, z19=_, z20=_):
    """[Condition] Black Knight: Generation Generator_After Defeating Boss
    z14: Event group ID
    z19: Other ① Event group ID
    z20: Other ② Event group ID
    """
    """State 0,1: Generation determination"""
    CompareActiveChrNum(8, z14, 0, 0, 0, 0, 1, 5)
    CompareActiveChrNum(8, z14, z19, z20, 0, 0, 5, 5)
    CompareEventFlag(8, 537020032, 1)
    assert ConditionGroup(8)
    """State 2: Wait just before generation"""
    CompareStateTime(0, 2, 3, 5)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m50_37_x366(z15=_, z16=_, z17=_, z18=_, z14=_, z19=_, z20=_):
    """[Execution] Black Knight: Generation Generator
    z15: Black Knight ① Generator ID
    z16: Black Knight ② Generator ID
    z17: Black Knight ③ Generator ID
    z18: Disable key guide
    z14: Event group ID
    z19: Other ① Event group ID
    z20: Other ② Event group ID
    """
    """State 0,3: SFX playback from generator: 70"""
    ChangeOwnObjState(70)
    """State 1: Random generation of black knights"""
    ForceRandomGeneration(1, z15, z16, z17, z18, 0)
    """State 2: Wait for next generation"""
    CompareActiveChrNum(8, z14, z19, z20, 0, 0, 5, 5)
    CompareStateTime(8, 140, 3, 155)
    assert ConditionGroup(8)
    """State 4: Rerun"""
    return 0

def event_m50_37_x367():
    """[Reproduction] Wind speed magnification change by snowstorm cancellation"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x368(z13=537000001):
    """[Conditions] Change in wind speed magnification by canceling snowstorm
    z13: Snowstorm release flag
    """
    """State 0,1: Has the snowstorm been lifted?"""
    CompareEventFlag(0, z13, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x369():
    """[Execution] Wind speed magnification change by canceling snowstorm"""
    """State 0,1: Change in wind speed magnification"""
    SetWindSpeedMultiplier(1, 0.1)
    """State 2: End state"""
    return 0

def event_m50_37_x370(z13=537000001):
    """[Preset] Wind speed magnification change by removing snowstorm
    z13: Snowstorm release flag
    """
    """State 0,1: [Reproduction] Wind speed magnification change by canceling snowstorm_SubState"""
    assert event_m50_37_x367()
    """State 3: [Condition] Change in wind speed magnification by canceling snowstorm_SubState"""
    assert event_m50_37_x368(z13=z13)
    """State 2: [Execution] Wind speed magnification change due to snowstorm cancellation_SubState"""
    assert event_m50_37_x369()
    """State 4: End state"""
    return 0

def event_m50_37_x371():
    """[Reproduction] Start of operation of Black Knight Generator"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x372(z9=3400000):
    """[Condition] Start of operation of Black Knight Generator
    z9: Judgment point ID
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z9, z9, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x373(z10=537020032, z11=0, z12=0):
    """[Execution] Start of operation of Black Knight Generator
    z10: Operation flag
    z11: Minimum weight
    z12: Maximum weight
    """
    """State 0,2: weight"""
    CompareStateTime(0, z11, 3, z12)
    assert ConditionGroup(0)
    """State 1: Operation flag ON"""
    SetEventFlag(z10, 1)
    """State 3: End state"""
    return 0

def event_m50_37_x374(z9=3400000, z10=537020032, z11=0, z12=0):
    """[Preset] Start of Black Knight Generator
    z9: Judgment point ID
    z10: Operation flag
    z11: Minimum weight until operation
    z12: Maximum weight until operation
    """
    """State 0,1: [Reproduction] Black Knight Generator starts operation_SubState"""
    assert event_m50_37_x371()
    """State 3: [Condition] Start of Black Knight Generator_SubState"""
    assert event_m50_37_x372(z9=z9)
    """State 2: [Execution] Start of Black Knight Generator_SubState"""
    assert event_m50_37_x373(z10=z10, z11=z11, z12=z12)
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

def event_m50_37_x377(z8=50371010):
    """[Execution] 棺 桶 Bobsled_Initialization
    z8: 棺 桶 OBJ instance ID
    """
    """State 0,1: 棺 桶 OBJ initialization"""
    InitializeObj(z8)
    assert CompareObjStateId(z8, 10, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x378(z8=50371010):
    """[Preset] 棺 桶 Bobsleigh_Initialization
    z8: 棺 桶 OBJ instance ID
    """
    """State 0,1: [Reproduction] 棺 桶 Bobsleigh_Initialization_SubState"""
    call = event_m50_37_x375()
    if call.Get() == 0:
        """State 3: [Condition] 棺 桶 Bobsleigh_Initialization_Empty_SubState"""
        assert event_m50_37_x376()
        """State 2: [Execution] 棺 桶 Bobsleigh_Initialization_SubState"""
        assert event_m50_37_x377(z8=z8)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m50_37_x379():
    """[Reproduction] White knight deleted inside ice after boss war _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x380(z7=537020175):
    """[Condition] White knight inside ice after boss battle removed
    z7: Judgment flag
    """
    """State 0,1: Boss clear flag judgment"""
    CompareEventFlag(0, z7, 0)
    CompareEventFlag(1, z7, 1)
    if ConditionGroup(1):
        """State 2: OFF standby"""
        CompareEventFlag(0, z7, 0)
        assert ConditionGroup(0)
    elif ConditionGroup(0):
        pass
    """State 3: End state"""
    return 0

def event_m50_37_x381():
    """[Execution] White knight inside ice after boss battle removed"""
    """State 0,1: End state"""
    return 0

def event_m50_37_x382(z7=537020175):
    """[Preset] Delete the white knight inside the ice after the boss battle
    z7: Judgment flag
    """
    """State 0,1: [Reproduction] White knight inside ice after boss battle removed_Sky_SubState"""
    assert event_m50_37_x379()
    """State 3: [Condition] White knight inside ice after boss battle removed_SubState"""
    assert event_m50_37_x380(z7=z7)
    """State 2: [Execution] Delete the white knight inside the ice after the boss battle_Sky_SubState"""
    assert event_m50_37_x381()
    """State 4: End state"""
    return 0

def event_m50_37_x383(z5=_):
    """[Reproduction] Instant death damage inside the ice
    z5: Point ID
    """
    """State 0,1: Disabling the damage range"""
    EnableDamageArea(z5, 0)
    """State 2: End state"""
    return 0

def event_m50_37_x384(z6=_):
    """[Condition] Instant death damage inside the ice
    z6: Ice OBJ instance ID
    """
    """State 0,1: Has ice appeared?"""
    CompareObjState(0, z6, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m50_37_x385(z5=_):
    """[Execution] Instant death damage inside the ice
    z5: Point ID
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
    EnableDamageArea(z5, 1)
    """State 4: End state"""
    return 0

def event_m50_37_x386(z5=_, z6=_):
    """[Preset] Instant death damage inside the ice
    z5: Point ID
    z6: Ice OBJ instance ID
    """
    """State 0,1: [Reproduction] Instant death damage inside ice_SubState"""
    assert event_m50_37_x383(z5=z5)
    """State 3: [Condition] Instant death damage inside ice_SubState"""
    assert event_m50_37_x384(z6=z6)
    """State 2: [Execution] Instant death damage inside the ice_SubState"""
    assert event_m50_37_x385(z5=z5)
    """State 4: End state"""
    return 0

def event_m50_37_x387(z4=17000):
    """[DC] [Execution] Yukihara gets the eyes of a priestess
    z4: Event SFXID
    """
    """State 0,1: Stop SFX"""
    StopSfxAtPoint(z4)
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
    event_m50_37_x70(z216=10000000, z217=760, z218=0, z219=0.2, z220=537020060)
    Quit()

def event_m50_37_101010():
    """Black Spirit Display_Dark Miracle"""
    """State 0,1: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_37_x70(z216=10000100, z217=761, z218=0, z219=0.2, z220=537020061)
    Quit()

def event_m50_37_101020():
    """Black Spirit Display_Holy Knight"""
    """State 0,1: [Lib] [DLC] NPC Black Phantom Appearance: Online: Unconditional_Flag ON_SubState"""
    event_m50_37_x70(z216=10000200, z217=762, z218=0, z219=0, z220=537020062)
    Quit()

def event_m50_37_4000000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m50_37_x74(flag30=537020055, z204=14, flag31=537000056, z205=3, z206=40)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert (event_m50_37_x79(z209=80000000, z210=0, z211=5, z212=980, val2=1, z213=40, z214=80000001,
                z215=80000099))
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert (event_m50_37_x79(z209=80000100, z210=0, z211=5, z212=980, val2=2, z213=40, z214=80000101,
                z215=80000199))
        """State 6: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert (event_m50_37_x79(z209=80000200, z210=0, z211=5, z212=980, val2=3, z213=40, z214=80000201,
                z215=80000299))
        """State 2: Start flag ON"""
        SetEventFlag(537020057, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_4000010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m50_37_x82(flag32=537000056, z207=980, mode3=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m50_37_4001000():
    """[DC] Cannot lock fighter"""
    """State 0,2: [DC] [Preset] Pallet Warrior Unlockable Management_SubState"""
    assert event_m50_37_x391(z1=5320)
    """State 1: Finish"""
    EndMachine()
    Quit()

