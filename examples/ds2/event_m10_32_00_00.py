# -*- coding: utf-8 -*-
def event_m10_32_1000():
    """Switching the gimmick door related flags on the connection path"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_32_x23(z77=105405, z78=1)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_32_2000():
    """Generation management of phantom enemies 1"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2000, z31=1, flag3=132020020, flag4=132020001)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_2010():
    """Generation management of phantom enemies 2"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2001, z31=2, flag3=132020021, flag4=132020002)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_2020():
    """Generation management of phantom enemies 3"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2002, z31=3, flag3=132020022, flag4=132020003)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_2030():
    """Generation management of phantom enemies 4"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2003, z31=4, flag3=132020023, flag4=132020004)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_2040():
    """Generation management of phantom enemies 5"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2006, z31=5, flag3=132020024, flag4=132020005)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_2050():
    """Generation management of phantom enemies 6"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2007, z31=6, flag3=132020025, flag4=132020006)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_2060():
    """Generation management of phantom enemies 7"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z30=2009, z31=7, flag3=132020026, flag4=132020007)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4000():
    """OBJ: Shenzhen Pilgrim: Magic Circle Open"""
    """State 0,1: [Lib] Pilgrim of Shenzhen: Magic Square: Open_SubState"""
    event_m10_32_x4(z122=102327, z123=102330, z124=10323000)
    Quit()

def event_m10_32_4001():
    """OBJ: Shenzhen Pilgrim: Magic Warp"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Key Guide_SubState"""
    event_m10_32_x6(z114=102327, z115=10323000, z116=102330, z117=400010, z118=0)
    Quit()

def event_m10_32_4002():
    """OBJ: Shenzhen Pilgrim: Magic Circle Opening"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Opening Production_SubState"""
    event_m10_32_x5(z119=10323000, z120=102327, z121=132020107)
    Quit()

def event_m10_32_5000():
    """Pitfall_Large_Navimesh switching"""
    """State 0,2: [Preset] Pitfall_SubState"""
    assert event_m10_32_x63(z35=10321500, z36=500000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_5010():
    """Pitfall_Small_Navigation mesh switching"""
    """State 0,2: [Preset] Pitfall_SubState"""
    assert event_m10_32_x63(z35=10321505, z36=501000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6000():
    """Boss: Manscorpion ♀ Battle"""
    """State 0,2: [Preset] Manscorpion Battle_Start_SubState"""
    assert event_m10_32_x79(flag2=132000081, z22=101, z23=1032000, z24=132020080, z25=5, mode1=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6010():
    """OBJ Navimesh change destroyed during the Manscorpion battle 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321250, z86=20, z87=601000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6020():
    """OBJ Navimesh change 2 destroyed during Manscorpion battle"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321260, z86=20, z87=602000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6030():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321261, z86=20, z87=603000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6040():
    """OBJ Navimesh change destroyed during the Manscorpion battle 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321304, z86=20, z87=604000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6050():
    """OBJ Navimesh change destroyed during the Manscorpion battle 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321305, z86=20, z87=605000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6060():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 6"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321306, z86=20, z87=606000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6070():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 7"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321307, z86=20, z87=607000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_6080():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 8"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z85=10321301, z86=20, z87=608000, z88=0, z89=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_7000():
    """Treasure corpse stone pillar_01"""
    """State 0,2: [Preset] Stone Pillar_SubState"""
    assert event_m10_32_x64(z32=10321250, z33=10326200, z34=72)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_8000():
    """King's door"""
    """State 0,3: [Preset] King's Door_City of Shadows_SubState"""
    call = event_m10_32_x89(z19=10320400, z20=105310, z21=132000055)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_9000():
    """White door to the royal castle"""
    """State 0,3: [Preset] White door to the Royal Castle_SubState"""
    call = event_m10_32_x68(z13=10320405, z14=900000, z15=100420, z16=10320406, z17=900010)
    if call.Get() == 0:
        """State 1: Door release (end)"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Door not open (re-execution)"""
        RestartMachine()
        Quit()

def event_m10_32_10000():
    """Lion Warrior _ Petrification Stop 1_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z90=2040, z91=0, z92=15, z93=132000010, z94=0, z95=1600, z96=3, z97=10010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_10010():
    """Lion Warrior _ Petrification Stop 1_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z71=2040, z72=0, z73=132000010, z74=0, z75=0, z76=10000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_10020():
    """Lion Warrior _ Petrification Stop 1_ Switching Navigation"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z58=1002000, z59=0, z60=2, flag10=132000010, flag11=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_11000():
    """Lion Warrior _ Petrification Stop 2_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z90=2310, z91=0, z92=15, z93=132000012, z94=0, z95=1600, z96=3, z97=11010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_11010():
    """Lion Warrior _ Petrification Stop 2_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z71=2310, z72=0, z73=132000012, z74=0, z75=0, z76=11000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_11020():
    """Lion Warrior _ Petrification Stop 2_ Switching Navigation"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z58=1102000, z59=0, z60=2, flag10=132000012, flag11=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_12000():
    """Lion Warrior _ Petrochemical Stop 3_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z90=2041, z91=0, z92=15, z93=132000014, z94=0, z95=1600, z96=3, z97=12010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_12010():
    """Lion Warrior _ Petrification Stop 3_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z71=2041, z72=0, z73=132000014, z74=0, z75=0, z76=12000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_12020():
    """Lion Warrior _ Petrochemical Stop 3_ Navigation Switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z58=1202000, z59=0, z60=2, flag10=132000014, flag11=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_12050():
    """Acquire items by destroying petrified characters"""
    """State 0,2: [Preset] Earn items by destroying petrified characters_SubState"""
    # lot:60009000:Fang Key
    assert event_m10_32_x96(lot1=60009000, z18=2041)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_13000():
    """Disabling damage"""
    """State 0,1: Disabling lazy damage"""
    SetDamageImmunityByCharacterId(210000, 200018020, 1)
    SetDamageImmunityByCharacterId(222001, 200018020, 1)
    SetDamageImmunityByCharacterId(308000, 200018020, 1)
    """State 3: [DC] Invalidation character addition"""
    SetDamageImmunityByCharacterId(153000, 200018020, 1)
    SetDamageImmunityByCharacterId(213011, 200018020, 1)
    SetDamageImmunityByCharacterId(307001, 200018020, 1)
    SetDamageImmunityByCharacterId(694007, 200018020, 1)
    SetDamageImmunityByCharacterId(883000, 200018020, 1)
    SetDamageImmunityByCharacterId(883100, 200018020, 1)
    SetDamageImmunityByCharacterId(893000, 200018020, 1)
    SetDamageImmunityByCharacterId(725000, 200018020, 1)
    SetDamageImmunityByCharacterId(742002, 200018020, 1)
    SetDamageImmunityByCharacterId(838200, 200018020, 1)
    SetDamageImmunityByCharacterId(838300, 200018020, 1)
    SetDamageImmunityByCharacterId(153010, 200018020, 1)
    """State 2: Finish"""
    EndMachine()
    Quit()

def event_m10_32_14000():
    """Key door that opens with "Beast Key" """
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_32_x9(z105=1005, z106=1105, z107=50850000, z108=132000050)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_80000():
    """Fireworks for regeneration 01_ in the building of the branch road"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_32_x30(z61=1032000, z62=1032099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_81000():
    """Regeneration of fire 02_in the huge bridge"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_32_x30(z61=1032100, z62=1032199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_x0(z129=0, z130=0, z53=50370000, z54=5100000):
    """[Lib] Warp between maps after poly play
    z129: Pre-warp poly play ID
    z130: Poly Play ID after Warp
    z53: Map ID
    z54: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z129, z130, z53, z54, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_32_x1(z125=_, z126=_, z127=_, z128=_):
    """[Lib] NPC: Grave Placement: General purpose
    z125: Death map: Global event flag
    z126: Tomb: OBJ instance ID
    z127: Tomb move to: Generator ID
    z128: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z125, 1)
    IsGraveGeneratable(8, z128, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z126, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z126, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_32_x2(z111=_, z112=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z111: Global: death flag
    z112: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z112, 10, 0)
    CompareObjState(1, z112, 20, 0)
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
    IsObjSearched(0, z112)
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

def event_m10_32_x3(z109=_, z110=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z109: Area other flags: Ghost appearance
    z110: Area other flags: Conversation start
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
    SetEventFlag(z109, 1)
    CompareEventFlag(0, z109, 1)
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
    SetEventFlag(z110, 1)
    CompareEventFlag(0, z110, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_32_x4(z122=102327, z123=102330, z124=10323000):
    """[Lib] Shenzhen Pilgrim: Magic Square: Open
    z122: Magic Square: Open: Global Event Flag
    z123: Magic Square: Invasion: Global Event Flag
    z124: Magic Square: OBJ instance ID
    """
    """State 0,1: Magic Square: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Magic square: All open judgment"""
        CompareEventFlag(8, 100979, 1)
        CompareEventFlag(8, z122, 1)
        CompareEventFlag(9, 100979, 1)
        CompareEventFlag(8, z122, 0)
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
            CompareObjState(0, z124, 30, 0)
            assert ConditionGroup(0)
        else:
            """State 3: Magic Square: Player Return Judgment"""
            CompareEventFlag(8, z122, 1)
            CompareEventFlag(8, z123, 1)
            if ConditionGroup(8):
                """State 4: Magic square: Flag initialization setting"""
                SetEventFlag(z122, 0)
                SetEventFlag(z123, 0)
                CompareEventFlag(8, z122, 0)
                CompareEventFlag(8, z123, 0)
                assert ConditionGroup(8)
                """State 8: Magic Square: Erasure"""
                ChangeOwnObjState(80)
                CompareObjState(0, z124, 10, 0)
                assert ConditionGroup(0)
            else:
                """State 6: Magic Square: Open Flag Judgment"""
                CompareEventFlag(0, z122, 1)
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

def event_m10_32_x5(z119=10323000, z120=102327, z121=132020107):
    """[Lib] Shenzhen Pilgrims: Magic Square: Opening Production
    z119: Magic Square: OBJ instance ID
    z120: Magic Square: Open: Global Event Flag
    z121: Magic Square: Production Start: Area and Other Flags
    """
    """State 0,4: Appearance production: Start"""
    CompareEventFlag(0, z121, 1)
    assert ConditionGroup(0)
    """State 3: Appearance effect: Open flag setting"""
    SetEventFlag(z120, 1)
    CompareEventFlag(0, z120, 1)
    assert ConditionGroup(0)
    """State 1: Appearance Direction: Magic Square Appearance"""
    ChangeOwnObjState(70)
    CompareObjState(0, z119, 30, 0)
    assert ConditionGroup(0)
    """State 5: Appearance production: End"""
    SetEventFlag(z121, 0)
    CompareEventFlag(0, z121, 0)
    assert ConditionGroup(0)
    """State 2: Appearance production: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_32_x6(z114=102327, z115=10323000, z116=102330, z117=400010, z118=0):
    """[Lib] Shenzhen Pilgrim: Magic Square: Key Guide
    z114: Magic Square: Open: Global Event Flag
    z115: Magic Square: OBJ instance ID
    z116: Magic Square: Invasion: Global Event Flag
    z117: Magic Square: Warp Point
    z118: Magic Square: During Warp: Area Other Flag
    """
    """State 0,1: Key guide: Start"""
    CompareObjState(0, z115, 30, 0)
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
        IsObjSearched(2, z115)
        CompareObjState(3, z115, 10, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(2):
            """State 7: Key guide: Intrusion flag: Setting"""
            ProhibitMultiplayer(1)
            SetEventFlag(z118, 1)
            """State 8: Shenzhen Pilgrim: Magic Square: Warp_SubState"""
            call = event_m10_32_x7(z117=z117, z116=z116)
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

def event_m10_32_x7(z117=400010, z116=102330):
    """Shenzhen Pilgrim: Magic Square: Warp
    z117: Warp point ID
    z116: Intrusion: Global flag
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
            SetEventFlag(z116, 1)
            PlayCutsceneAndWarpToMap(0, 0, 40030000, z117, 0)
            assert CutsceneWarpEnded() != 0
            """State 2: Warp: Wait for completion"""
            CompareEventFlag(0, 0, 1)
            assert ConditionGroup(0)
            """State 6: Normal: End state"""
            return 0
    """State 7: Re-execution: end state"""
    return 1

def event_m10_32_x8(z109=_, z110=_, z111=_, z112=_, z113=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z109: Ghost Appearance: Area Other Flag
    z110: Conversation start: Area and other flags
    z111: Death: Global event flag
    z112: Tomb: OBJ instance ID
    z113: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z113, 1, 0)
    CompareEventFlag(9, z109, 1)
    CompareObjState(9, z112, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z110, 1)
        CompareEventFlag(0, z110, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_32_x2(z111=z111, z112=z112, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_32_x3(z109=z109, z110=z110, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_32_x9(z105=1005, z106=1105, z107=50850000, z108=132000050):
    """[Lib] Item specified door unlocking_2
    z105: Text ID when opened
    z106: Text ID when not opened
    z107: item
    z108: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z107, z105, z106, z108, 0)
    """State 2: End state"""
    return 0

def event_m10_32_x10(z103=_, z104=_):
    """[Lib] NPC: Death determination: General purpose
    z103: Generator ID
    z104: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z104, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z103)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z104, 1)
            CompareEventFlag(0, z104, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_32_x11(z98=104150, z99=102405, z100=102406, z101=132010127, z102=103651):
    """[Lib] Appearance determination: General purpose
    z98: Death: Global event flag
    z99: Local emigration permission: Global event flag
    z100: Relocation permission after moving: Global event flag
    z101: Appearance determination: Area and other flags
    z102: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z98, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z99, 1)
            CompareEventFlag(8, z100, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z99, 1)
                CompareEventFlag(8, z102, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z101, 1)
                    CompareEventFlag(0, z101, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z101, 0)
                    CompareEventFlag(0, z101, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z101, 0)
        CompareEventFlag(0, z101, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_32_x12(z19=10320400, z21=132000055):
    """[Lib] [Condition] King's door
    z19: King's door OBJ instance ID
    z21: Opening flag
    """
    """State 0,2: Did you approach the king's door?"""
    CompareObjPlayerDistance(0, z19, 3, 5)
    assert ConditionGroup(0)
    """State 1: Is it equipped with a king's ring? Has it been opened?"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    SetConditionGroup(0, 8)
    # goods:40510000:King's Ring
    DoesPlayerHaveItem(8, 40510000, 1, 3, 1, 1, 0)
    CompareEventFlag(8, z21, 1)
    if ConditionGroup(0):
        """State 4: Equipped with a king's ring"""
        return 1
    else:
        """State 3: Not qualified"""
        return 0

def event_m10_32_x13(z19=10320400):
    """[Lib] [execution] King's door _ not open
    z19: King's door OBJ instance ID
    """
    """State 0,1: Event message display"""
    # action:2000:"Produce the symbol of the King"
    DisplayEventMessage(2000, 0, 0, 0)
    """State 2: Equipped with an or ring away from the king's door?"""
    CompareObjPlayerDistance(0, z19, 10, 3)
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_32_x14(z90=_, z91=0, z92=15, z93=_, z94=0, z95=1600, z96=3, z97=_):
    """[Lib] Character: Petrochemical: Key guide
    z90: generator
    z91: Death: Global event flag
    z92: Event action
    z93: Petrified: Area and other flags
    z94: Petrified: Global event flag
    z95: Key guide parameters
    z96: Petrification start state ID
    z97: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z90, z96, 0)
    CompareEventStatus(8, z97, 1, 0)
    CompareEventFlag(2, z93, 1)
    CompareEventFlag(3, z94, 1)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(2):
        pass
    elif ConditionGroup(3):
        pass
    elif ConditionGroup(8):
        Goto('L0')
    else:
        pass
    """State 17: End state"""
    return 0
    """State 2: Petrochemical: Key guide: Display"""
    Label('L0')
    CreateKeyGuideArea(34, z95)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z90)
    IsPlayerInTheMap(1, 0, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 5: Petrification: Key guide: Deleted"""
        DeleteKeyGuideArea()
        # goods:60537000:Fragrant Branch of Yore
        if (ItemCount(60537000, 1, 1, 0) > 1) != 1:
            """State 12: Petrification: Item not owned dialog"""
            # action:1017:"A statue blocks your way"
            DisplayOwnOkMenu(1017, 3, 15, 220, 2, 0, 0)
            assert OkMenuDisplay() != 0
            """State 13: Petrochemical: Item not owned dialog: Waiting for input"""
            assert OkMenuDisplay() != 1
        else:
            """State 10: Petrochemical: Item usage selection dialog"""
            # action:1002:"Use %s?", goods:60537000:Fragrant Branch of Yore
            DisplayOwnYesNoMenu(1002, 3, 220, 2, 60537000, 0)
            assert YesNoMenuDisplay() != 0
            """State 11: Petrochemical: Item usage selection dialog: Waiting for input"""
            if (YesNoMenuResult() == 3) != 0:
                pass
            elif (YesNoMenuResult() == 2) != 0:
                pass
            elif (YesNoMenuResult() == 1) != 0:
                """State 15,14: Petrochemical: Event action: Start"""
                DoesPlayerEventAction(0, 1)
                assert ConditionGroup(0)
                """State 6: Petrification: Event action: Regeneration"""
                PlayerActionRequest(z92)
                IsPlayerPlayingMotion(0, z92, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z93, 1)
                CompareEventFlag(0, z93, 1)
                SetEventFlag(z94, 1)
                CompareEventFlag(1, z94, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z92, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()
    Quit()

def event_m10_32_x15(z85=_, z86=20, z87=_, z88=0, z89=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z85: Object instance ID
    z86: OBJ state ID
    z87: Navimesh switching point ID
    z88: Additional attributes
    z89: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_32_x16(z85=z85, z86=z86, z87=z87, z89=z89, z88=z88)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_32_x17(z85=z85, z86=z86, z87=z87)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_32_x18(z85=z85, z86=z86, z87=z87, z88=z88, z89=z89)
    """State 4: End state"""
    return 0

def event_m10_32_x16(z85=_, z86=20, z87=_, z89=2, z88=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z85: Target OBJ instance ID
    z86: Target OBJ state ID
    z87: Navimesh switching point ID
    z89: Additional attributes
    z88: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z85, z86, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z87, z89)
        DeleteNavimeshAttribute(z87, z88)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_32_x17(z85=_, z86=20, z87=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z85: Target OBJ instance ID
    z86: Target OBJ state ID
    z87: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z85, z86, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x18(z85=_, z86=20, z87=_, z88=0, z89=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z85: Target OBJ instance ID
    z86: Target OBJ state ID
    z87: Navimesh switching point ID
    z88: Additional attributes
    z89: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z87, z88)
    DeleteNavimeshAttribute(z87, z89)
    """State 2: End state"""
    return 0

def event_m10_32_x19(z79=102980, z80=626, z81=104430, z82=60, z83=103930, z84=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z79: White Phantom can appear: Global event flag
    z80: White Phantom: Generator ID
    z81: Death: Global event flag
    z82: Body: Generator group ID
    z83: Hostile: Global event flag
    z84: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z80)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z81, 1)
        CompareEventFlag(1, z83, 1)
        CompareEventFlag(2, z79, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z80)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z81, 1)
            CompareEventFlag(1, z83, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z80)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z81, 1)
            CompareEventFlag(1, z83, 1)
            HasNpcPhantomSpawned(2, z80, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z82, 0)
                HasNpcPhantomSpawned(0, z80, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z80)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_32_x20():
    """[Lib] [Reproduction] Switch the connection flag when in the map"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x21():
    """[Lib] [Condition] Switch to connection flag when in map"""
    """State 0,1: Are you in the map?"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x22(z77=105405, z78=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z77: Global event flag for connection
    z78: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z77, z78)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z77, z78)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_32_x23(z77=105405, z78=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z77: Global event flag for connection
    z78: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_32_x20()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_32_x21()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_32_x22(z77=z77, z78=z78)
    """State 4: End state"""
    return 0

def event_m10_32_x24(z71=_, z72=0, z73=_, z74=0, z75=0, z76=_):
    """[Lib] Character: Petrified: Appearance setting
    z71: Generator ID
    z72: Death: Global event flag
    z73: Petrified: Area and other flags
    z74: Petrified: Global event flag
    z75: Startup state
    z76: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z71)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z72, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z73, 1)
                CompareEventFlag(1, z74, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z71, z75)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_32_x25(z64=102317, z65=102324, z66=102331, z67=102332, z68=102315, z69=102316, z70=103622):
    """[Lib] NPC: Shenzhen Pilgrims: Appearance Judgment
    z64: Generation stop: Global event flag
    z65: Appearance permission: Global event flag
    z66: Sub 1 encountering: Global event flag
    z67: During sub-2 encounter: Global event flag
    z68: Sub 1 generation stop: Global event flag
    z69: Sub 2 generation stop: Global event flag
    z70: Hostile map: Global event flag
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
                CompareEventFlag(0, z64, 1)
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
                        CompareEventFlag(8, z66, 1)
                        CompareEventFlag(8, z68, 0)
                        CompareEventFlag(9, z67, 1)
                        CompareEventFlag(9, z69, 0)
                        if ConditionGroup(8):
                            pass
                        elif ConditionGroup(9):
                            pass
                        else:
                            Goto('L1')
                """State 5: Appearance judgment: Appearance impossible"""
                Label('L0')
                SetEventFlag(z65, 0)
                CompareEventFlag(0, z65, 0)
                assert ConditionGroup(0)
                Goto('L2')
            """State 6: Appearance determination: Appearance allowed"""
            Label('L1')
            SetEventFlag(z65, 1)
            CompareEventFlag(0, z65, 1)
            assert ConditionGroup(0)
    """State 3: Appearance determination: System: End"""
    Label('L2')
    EndMachine()
    Quit()
    """Unused"""
    """State 10: Appearance determination: Reappearance setting"""
    CompareEventFlag(8, z64, 0)
    CompareEventFlag(8, z70, 0)
    if ConditionGroup(8):
        Goto('L1')
    else:
        Goto('L0')
    """State 11: End state"""
    return 0

def event_m10_32_x26(z63=627):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z63: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z63)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_32_x27():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x28(z61=_, z62=_):
    """[Lib] [execute] Rebirth fire
    z61: Flag start ID
    z62: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z61, z62, 0)
    """State 2: End state"""
    return 0

def event_m10_32_x29():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x30(z61=_, z62=_):
    """[Lib] [Preset] Rebirth
    z61: Flag start ID
    z62: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_32_x27()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_32_x29()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_32_x28(z61=z61, z62=z62)
    """State 4: End state"""
    return 0

def event_m10_32_x31(z19=10320400):
    """[Lib] [Condition] King's door closed
    z19: King's door OBJ instance ID
    """
    """State 0,1: Did you leave the king's door?"""
    CompareObjPlayerDistance(0, z19, 30, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x32(flag10=_, flag11=0, z60=2, z59=0, z58=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    flag10: Other flags
    flag11: Global flag
    z60: Additional attributes
    z59: Delete attribute
    z58: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(flag10) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(flag11) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z58, z60)
        DeleteNavimeshAttribute(z58, z59)
        """State 3: Flag OFF"""
        return 0

def event_m10_32_x33(flag10=_, flag11=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    flag10: Other flags
    flag11: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, flag10, 1)
    CompareEventFlag(0, flag11, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_32_x34(z58=_, z59=0, z60=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z58: Navimesh switching point ID
    z59: Additional attributes
    z60: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z58, z59)
    DeleteNavimeshAttribute(z58, z60)
    """State 2: End state"""
    return 0

def event_m10_32_x35(z58=_, z59=0, z60=2, flag10=_, flag11=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z58: Navimesh switching point ID
    z59: Additional attributes
    z60: Delete attribute
    flag10: Other flags
    flag11: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_32_x32(flag10=flag10, flag11=flag11, z60=z60, z59=z59, z58=z58)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_32_x33(flag10=flag10, flag11=flag11)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_32_x34(z58=z58, z59=z59, z60=z60)
    """State 4: End state"""
    return 0

def event_m10_32_x36(flag9=_, z57=_):
    """[Lib] [Preset] Get trophy
    flag9: Acquisition trigger_other flags
    z57: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag9) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag9, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z57)
    """State 4: End state"""
    return 0

def event_m10_32_x37(z55=40, z56=104122):
    """[Lib] NPC: Death Determination: Shenzhen Pilgrim
    z55: Generator ID
    z56: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z56, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z55)
            IsChrDead(8, z55)
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
                SetEventFlag(z56, 1)
                CompareEventFlag(0, z56, 1)
                assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_32_x38(z52=10323800):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z52: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z52)
    """State 2: End state"""
    return 0

def event_m10_32_x39(z52=10323800):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z52: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z52, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z52)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_32_x40(z52=10323800, z53=50370000, z54=5100000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z52: Warp OBJ instance ID
    z53: Map ID
    z54: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z52, 1)
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
        assert event_m10_32_x0(z129=0, z130=0, z53=z53, z54=z54)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m10_32_x41(z52=10323800):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z52: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z52, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x42(z52=10323800, z53=50370000, z54=5100000):
    """[Lib] [Preset] Warp move between main part and DLC
    z52: Warp OBJ instance ID
    z53: Map ID
    z54: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m10_32_x38(z52=z52)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m10_32_x39(z52=z52)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m10_32_x41(z52=z52)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m10_32_x40(z52=z52, z53=z53, z54=z54)
    """State 5: End state"""
    return 0

def event_m10_32_x43(flag6=132020043, flag7=132000044):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    flag6: Lottery determination flag
    flag7: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(flag7) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(flag6) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_32_x44(z40=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z40: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z40, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_32_x45(flag6=132020043, z41=2, z42=20):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag6: Lottery determination flag
    z41: Number of appearance judgment points
    z42: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag6, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z41)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z42, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_32_x46(flag6=132020043, z40=14, flag7=132000044, z41=2, z42=20):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    flag6: Lottery determination flag
    z40: Random number comparison value
    flag7: Defeat flag
    z41: Number of appearance judgment points
    z42: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_32_x43(flag6=flag6, flag7=flag7)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_32_x44(z40=z40)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_32_x45(flag6=flag6, z41=z41, z42=z42)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_32_x55(flag6=flag6, z42=z42)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_32_x47(val1=_, z49=20):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z49: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z49) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_32_x48(z45=_, z46=0, z47=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z45: Appearance judgment point ID
    z46: Minimum appearance time
    z47: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z45, z45, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z46, 3, z47)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_32_x49(z48=956, z50=_, z51=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z48: Generator ID
    z50: Appearance start point ID
    z51: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z48, z50, z51)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z48)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m10_32_x50(flag8=132000044):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag8: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag8) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_32_x51(z45=_, z46=0, z47=5, z48=956, val1=_, z49=20, z50=_, z51=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z45: Intrusion detection point ID
    z46: Minimum appearance time
    z47: Maximum time to appear
    z48: Generator ID
    val1: Appearance judgment number
    z49: Lottery result point variable
    z50: Appearance start point ID
    z51: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_32_x47(val1=val1, z49=z49)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_32_x48(z45=z45, z46=z46, z47=z47)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_32_x49(z48=z48, z50=z50, z51=z51)
    """State 4: Finish"""
    return 0

def event_m10_32_x52(z43=956, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z43: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z43)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_32_x53(flag8=132000044, z44=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag8: Defeat flag
    z44: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag8, 1)
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
                    SetEventFlag(z44, 1)
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

def event_m10_32_x54(flag8=132000044, z43=956, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag8: Defeat flag
    z43: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_32_x50(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_32_x52(z43=z43, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_32_x53(flag8=flag8, z44=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_32_x53(flag8=flag8, z44=102755)
    """State 5: End state"""
    return 0

def event_m10_32_x55(flag6=132020043, z42=20):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag6: Lottery determination flag
    z42: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag6, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z42, 0)
    """State 3: End state"""
    return 0

def event_m10_32_x56(flag5=132000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag5: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_32_x57(z38=824):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z38: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z38, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x58(z39=132020082):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z39: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z39, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x59(flag5=132000081, z38=824, z39=132020082):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag5: Boss destruction flag
    z38: Boss generator ID
    z39: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_32_x56(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_32_x57(z38=z38)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_32_x58(z39=z39)
    """State 4: End state"""
    return 0

def event_m10_32_x60():
    """[Reproduction] Reproducing pitfalls"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x61(z35=_):
    """[Conditions] Waiting for pitfalls
    z35: Pitfall OBJ instance ID
    """
    """State 0,1: OBJ collapse waiting"""
    CompareObjState(0, z35, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x62(z36=_, z37=0):
    """[Execution] Pitfall navigator mesh switching
    z36: Navimesh switching area ID
    z37: Pitfall OBJ instance ID
    """
    """State 0,1: Navi mesh switching"""
    AddNavimeshAttribute(z36, 2)
    """State 2: End state"""
    return 0

def event_m10_32_x63(z35=_, z36=_):
    """[Preset] Pitfall
    z35: Pitfall OBJ instance ID
    z36: Navimesh switching area ID
    """
    """State 0,1: [Reproduction] Pitfall state reproduction_SubState"""
    assert event_m10_32_x60()
    """State 2: [Condition] Pitfall collapse waiting_SubState"""
    assert event_m10_32_x61(z35=z35)
    """State 3: [Execution] Pitfall navigator mesh switching_SubState"""
    assert event_m10_32_x62(z36=z36, z37=0)
    """State 4: End state"""
    return 0

def event_m10_32_x64(z32=10321250, z33=10326200, z34=72):
    """[Preset] Stone pillar of treasure corpse
    z32: Stone pillar instance ID
    z33: Instance ID of treasure corpse
    z34: Falling state ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z33, 0)
    """State 2: [Reproduction] Treasure corpse branch_sky_SubState"""
    assert event_m10_32_x65()
    """State 3: [Condition] Treasure corpse branch_SubState"""
    assert event_m10_32_x66(z32=z32)
    """State 4: [Execution] Treasure corpse branch _SubState"""
    assert event_m10_32_x67(z33=z33, z34=z34)
    """State 5: End state"""
    return 0

def event_m10_32_x65():
    """[Reproduction] Stone pillar of treasure corpse _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x66(z32=10321250):
    """[Condition] Stone pillar of treasure corpse
    z32: Branch instance ID
    """
    """State 0,1: Wait for branch destruction"""
    IsObjBroken(0, z32, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x67(z33=10326200, z34=72):
    """[Execution] Stone pillar of treasure corpse
    z33: Instance ID of treasure corpse
    z34: Falling state ID
    """
    """State 0,1: OBJ state transition: treasure corpse"""
    ChangeObjState(z33, z34)
    """State 2: End state"""
    return 0

def event_m10_32_x68(z13=10320405, z14=900000, z15=100420, z16=10320406, z17=900010):
    """[Preset] Special door to the Royal Castle
    z13: Instance ID of door table OBJ
    z14: Point ID for table navigation mesh change
    z15: Special door opening flag
    z16: Instance ID of OBJ behind the door
    z17: Point ID for changing back Navi mesh
    """
    """State 0,3: [Reproduction] White door to the Royal Castle_SubState"""
    call = event_m10_32_x69(z13=z13, z16=z16)
    if call.Get() == 0:
        """State 4: [Condition] White door to the Royal Castle_SubState"""
        call = event_m10_32_x70(z13=z13)
        if call.Get() == 0:
            """State 5: [Execution] White door to the Royal Castle_Defeat specified boss_SubState"""
            assert event_m10_32_x71(z13=z13, z16=z16)
        elif call.Get() == 2:
            """State 6: [Execution] White door to the royal castle _ Acquire Seoul above a certain level _ SubState"""
            assert event_m10_32_x72(z13=z13, z16=z16)
        elif call.Get() == 1:
            """State 7: [Execution] White door to the Royal Castle_No access_SubState"""
            assert event_m10_32_x73(z13=z13)
            """State 10: Door not open"""
            return 1
    elif call.Get() == 2:
        """State 8: [Execution] Special door to the Royal Castle_Relief_SubState"""
        assert event_m10_32_x97(z13=z13, z16=z16)
    elif call.Get() == 1:
        pass
    """State 1: Navigation mesh change"""
    DeleteNavimeshAttribute(z14, 2)
    DeleteNavimeshAttribute(z17, 2)
    """State 2: Flag ON Special door opened"""
    SetEventFlag(z15, 1)
    """State 9: Door release"""
    return 0

def event_m10_32_x69(z13=10320405, z16=10320406):
    """[Reproduction] Special door to the Royal Castle
    z13: Instance ID of door table OBJ
    z16: Instance ID of OBJ behind the door
    """
    """State 0,2: Judgment status of doors"""
    if CompareObjStateId(z13, 10, 0):
        pass
    else:
        Goto('L0')
    """State 1: Hide key guide"""
    DisableObjKeyGuide(z13, 1)
    DisableObjKeyGuide(z16, 1)
    """State 4: Not passed"""
    return 0
    """State 3: Is the back of the door closed?"""
    Label('L0')
    if CompareObjStateId(z16, 10, 0):
        """State 6: Open the door"""
        return 2
    else:
        """State 5: Passed"""
        return 1

def event_m10_32_x70(z13=10320405):
    """[Conditions] Special door to the Royal Castle
    z13: Shirado OBJ instance ID
    """
    """State 0,2: Judging distance from players"""
    CompareObjPlayerDistance(0, z13, 3, 5)
    assert ConditionGroup(0)
    """State 1: Player status determination"""
    CompareEventFlag(8, 100963, 1)
    CompareEventFlag(8, 100952, 1)
    CompareEventFlag(8, 100460, 1)
    CompareEventFlag(8, 100966, 1)
    CompareCumulativeSouls(0, GetCommonEventParamInt(14) * ClampInt(GetGameCycle(), 1, 8), 3, 1)
    if ConditionGroup(8):
        """State 3: Passable (Defeat specified boss)"""
        return 0
    elif ConditionGroup(0):
        """State 5: Passable (obtained above Seoul)"""
        return 2
    else:
        """State 4: Impassable"""
        return 1

def event_m10_32_x71(z13=10320405, z16=10320406):
    """[Execution] Special door to the royal castle
    z13: Instance ID of door table OBJ
    z16: Instance ID of OBJ behind the door
    """
    """State 0,1: Front door release"""
    ChangeObjState(z13, 74)
    """State 2: Waiting for front door"""
    CompareObjState(0, z13, 74, 0)
    assert ConditionGroup(0)
    """State 3: Open the back door"""
    ChangeObjState(z16, 74)
    """State 4: End state"""
    return 0

def event_m10_32_x72(z13=10320405, z16=10320406):
    """[Execution] Special door to Wangcheng
    z13: Instance ID of door table OBJ
    z16: Instance ID of OBJ behind the door
    """
    """State 0,1: Key guide display"""
    DisableObjKeyGuide(z13, 0)
    DisableObjKeyGuide(z16, 0)
    """State 2: Did you open the door?"""
    CompareObjState(0, z13, 74, 0)
    assert ConditionGroup(0)
    """State 3: Open the back door"""
    ChangeObjState(z16, 74)
    """State 4: End state"""
    return 0

def event_m10_32_x73(z13=10320405):
    """[Execution] Special door to the Royal Castle
    z13: Shirado OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:2002:"Seek mightier souls"
    DisplayEventMessage(2002, 0, 0, 0)
    """State 2: Did you leave the white door? or cumulative soul value exceeds a certain value?"""
    CompareObjPlayerDistance(0, z13, 10, 3)
    CompareCumulativeSouls(0, GetCommonEventParamInt(14) * ClampInt(GetGameCycle(), 1, 8), 3, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_32_x74(z31=_, flag3=_, flag4=_):
    """[Reproduction] Generation management of phantom enemies
    z31: Area variable ID
    flag3: Generation stop flag
    flag4: Initialization completion flag
    """
    """State 0,5: host? The guests?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 7: Guest: Exit"""
    return 1
    """State 3: Area variable initialization judgment"""
    Label('L0')
    if GetEventFlag(flag4) != 0:
        pass
    else:
        """State 1: Generation stop flag judgment"""
        if GetEventFlag(flag3) != 0:
            pass
        else:
            """State 2: Reset area variable"""
            SetAreaVariable(z31, 0)
            """State 4: Area variable initialization processing completion flag: ON"""
            SetEventFlag(flag4, 1)
    """State 6: Host: Condition"""
    return 0

def event_m10_32_x75(z30=_, z31=_):
    """[Condition] Generation management of phantom enemies
    z30: Generator ID
    z31: Area variable ID
    """
    """State 0,1: Phantom enemy death waiting or generation number is 2 or more"""
    IsChrDead(0, z30)
    CompareEventFlagValue(1, 1, z31, 2, 3)
    if ConditionGroup(1):
        """State 3: Number of generations is 2 or more"""
        return 1
    elif ConditionGroup(0):
        """State 2: death"""
        return 0

def event_m10_32_x76(z31=_, z30=_):
    """[Execution] Generation management of phantom enemies_Add variable
    z31: Area variable ID
    z30: Generator ID
    """
    """State 0,1: Number of generated area variable addition"""
    AddAreaVariable(z31, 1)
    """State 2: Waiting for generation"""
    assert GeneratorOperationOngoing(z30) != 1
    """State 3: Rerun"""
    return 0

def event_m10_32_x77(z30=_, z31=_, flag3=_, flag4=_):
    """[Preset] Generation management of phantom enemies
    z30: Generator ID
    z31: Area variable ID
    flag3: Generation stop flag
    flag4: Initialization completion flag
    """
    """State 0,1: [Reproduction] Generation management of phantom enemies_SubState"""
    call = event_m10_32_x74(z31=z31, flag3=flag3, flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Phantom enemy generation management_SubState"""
        call = event_m10_32_x75(z30=z30, z31=z31)
        if call.Get() == 0:
            """State 3: [Execution] Generation management of phantom enemies_Variable addition_SubState"""
            assert event_m10_32_x76(z31=z31, z30=z30)
            """State 5: Rerun"""
            return 0
        elif call.Get() == 1:
            """State 2: [Execute] Generation management of phantom enemies_flag_SubState"""
            assert event_m10_32_x78(flag3=flag3)
    """State 6: Finish"""
    return 1

def event_m10_32_x78(flag3=_):
    """[Execute] Phantom enemy generation management flag
    flag3: Generation stop flag
    """
    """State 0,1: Stop flag ON"""
    SetEventFlag(flag3, 1)
    """State 2: Finish"""
    return 0

def event_m10_32_x79(flag2=132000081, z22=101, z23=1032000, z24=132020080, z25=5, mode1=0):
    """[Preset] Manscorpion Battle _Start
    flag2: Boss destruction flag
    z22: Sound ID
    z23: Boss Battle ID
    z24: Other flags for logic
    z25: Wait time
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Manscorpion Battle _Start_SubState"""
    call = event_m10_32_x80(flag2=flag2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Conditions] Manscorpion Battle_Start_SubState"""
        assert event_m10_32_x81(z28=600000, z29=600000)
        """State 3: [Execution] Manscorpion Battle _Start_SubState"""
        assert event_m10_32_x82(z23=z23, z24=z24)
        """State 7: [Reproduction] HP display and BGM playback_empty_SubState"""
        assert event_m10_32_x83()
        """State 9: [Condition] HP display and BGM playback_SubState"""
        assert event_m10_32_x84(z26=824, z27=2)
        """State 8: [Execution] HP display and BGM playback_SubState"""
        assert event_m10_32_x85(z22=z22, z25=z25, z23=z23)
        """State 2: [Reproduction] Manscorpion Battle_End_Sky_SubState"""
        assert event_m10_32_x86()
        """State 6: [Conditions] Manscorpion Battle_End Judgment_SubState"""
        assert event_m10_32_x87(z23=z23)
        """State 4: [Execution] Manscorpion Battle _End_SubState"""
        assert event_m10_32_x88(z22=z22, z23=z23, z24=z24, mode1=mode1)
    """State 10: End state"""
    return 0

def event_m10_32_x80(flag2=132000081):
    """[Reproduction] Manscorpion Battle _Start
    flag2: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag2) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_32_x81(z28=600000, z29=600000):
    """[Condition] Manscorpion Battle _Start
    z28: Start point ID
    z29: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z28, z29, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z28, z29, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x82(z23=1032000, z24=132020080):
    """[Execution] Manscorpion Battle _Start
    z23: Boss Battle ID
    z24: Logic flag
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z23)
    """State 2: Logic flag ON"""
    SetEventFlag(z24, 1)
    """State 3: End state"""
    return 0

def event_m10_32_x83():
    """[Reproduction] HP display and BGM playback_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x84(z26=824, z27=2):
    """[Condition] HP display and BGM playback
    z26: Boss generator ID
    z27: Activation state ID
    """
    """State 0,1: Did the boss jump out of the sand?"""
    CompareChrEzStateValue(0, z26, 7, 1, 0)
    IsEventBossKill(0, z26, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x85(z22=101, z25=5, z23=1032000):
    """[Execution] HP display and BGM playback
    z22: Sound ID
    z25: Wait time until display
    z23: Boss Battle ID
    """
    """State 0,3: Wait until BGM playback and HP display"""
    CompareStateTime(0, z25, 2, z25)
    IsEventBossKill(1, z23, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z22)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 4: End state"""
    return 0

def event_m10_32_x86():
    """[Reproduction] Manscorpion Battle _End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x87(z23=1032000):
    """[Condition] Manscorpion Battle _ End Judgment
    z23: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z23, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x88(z22=101, z23=1032000, z24=132020080, mode1=0):
    """[Execution] Manscorpion Battle _End
    z22: Sound ID
    z23: Boss Battle ID
    z24: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z24, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z23)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z22)
    """State 5: End state"""
    return 0

def event_m10_32_x89(z19=10320400, z20=105310, z21=132000055):
    """[Preset] King's door
    z19: Instance ID of king's door OBJ
    z20: King door opening and closing flag
    z21: Opening flag
    """
    """State 0,1: [Reproduction] King's door _ the forest of shadows_SubState"""
    call = event_m10_32_x90(z19=z19, z20=z20)
    if call.Get() == 1:
        """State 2: [Condition] King's door_SubState"""
        call = event_m10_32_x12(z19=z19, z21=z21)
        if call.Get() == 1:
            """State 3: [Execution] King's Door _ The Shadow Shadow Forest _ Open _ SubState"""
            assert event_m10_32_x91(z19=z19, z20=z20, z21=z21)
        elif call.Get() == 0:
            """State 4: [Execution] King's door_Do not open_SubState"""
            assert event_m10_32_x13(z19=z19)
    elif call.Get() == 2:
        """State 5: [Lib] [Condition] King's door_Close_SubState"""
        assert event_m10_32_x31(z19=z19)
        """State 6: [Execution] King's Door _ The Shadow Shadow Forest _Close_SubState"""
        assert event_m10_32_x92(z19=z19, z20=z20)
    elif call.Get() == 0:
        """State 8: Finish"""
        return 1
    """State 7: Rerun"""
    return 0

def event_m10_32_x90(z19=10320400, z20=105310):
    """[Reproduction] King's door
    z19: Instance ID of king's door OBJ
    z20: King door opening and closing flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 2: Is the door closed or closed?"""
    if CompareObjStateId(z19, 10, 0):
        """State 3: Waiting for the door to close"""
        Label('L0')
        assert CompareObjStateId(z19, 10, 0)
        """State 6: King door open / close flag: OFF"""
        SetEventFlag(z20, 0)
        """State 8: Closed"""
        return 1
    elif CompareObjStateId(z19, 80, 0):
        Goto('L0')
    else:
        """State 4: Waiting for the door to open"""
        assert CompareObjStateId(z19, 30, 0)
        """State 5: King's door open / close flag: ON"""
        SetEventFlag(z20, 1)
        """State 9: is open"""
        return 2
    """State 7: Guest: Exit"""
    Label('L1')
    return 0

def event_m10_32_x91(z19=10320400, z20=105310, z21=132000055):
    """[Execution] King's Door _ Open Shadow Forest _ Open
    z19: Instance ID of king's door OBJ
    z20: King door opening and closing flag
    z21: Opening flag
    """
    """State 0,1: Opening flag ON King's door opens"""
    SetEventFlag(z21, 1)
    ChangeObjState(z19, 70)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z19, 30, 0)
    assert ConditionGroup(0)
    """State 3: King's door open / close flag: ON"""
    SetEventFlag(z20, 1)
    """State 4: End state"""
    return 0

def event_m10_32_x92(z19=10320400, z20=105310):
    """[Execution] The door of the king
    z19: Instance ID of king's door OBJ
    z20: King door opening and closing flag
    """
    """State 0,1: The king's door closes"""
    ChangeObjState(z19, 80)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z19, 10, 0)
    assert ConditionGroup(0)
    """State 3: King door open / close flag: OFF"""
    SetEventFlag(z20, 0)
    """State 4: End state"""
    return 0

def event_m10_32_x93():
    """[Reproduction] Item acquisition by destroying petrified characters"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Has the item been acquired?"""
    # goods:50850000:Fang Key
    if (ItemCount(50850000, 1, 1, 1) == 1) != 0:
        """State 5: Item acquired"""
        return 2
    else:
        """State 3: host"""
        return 0
    """State 4: The guests"""
    Label('L0')
    return 1

def event_m10_32_x94(z18=2041):
    """[Condition] Earn items by destroying petrified characters
    z18: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z18)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x95(lot1=60009000):
    """[Execution] Get items by destroying petrified characters
    lot1: Item lottery ID
    """
    """State 0,1: Reward acquisition"""
    # lot:60009000:Fang Key
    AwardItem(lot1, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x96(lot1=60009000, z18=2041):
    """[Preset] Earn items by destroying petrified characters
    lot1: Item lottery ID
    z18: Generator ID
    """
    """State 0,1: [Reproduction] Item acquisition by destroying petrified characters_SubState"""
    call = event_m10_32_x93()
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Acquire items by destroying petrified characters_SubState"""
        assert event_m10_32_x94(z18=z18)
        """State 2: [Execution] Item acquisition by destroying petrified characters_SubState"""
        assert event_m10_32_x95(lot1=lot1)
    """State 4: End state"""
    return 0

def event_m10_32_x97(z13=10320405, z16=10320406):
    """[Execution] Special door to the royal castle for relief
    z13: Instance ID of door table OBJ
    z16: Instance ID of OBJ behind the door
    """
    """State 0,1: Key guide display"""
    DisableObjKeyGuide(z13, 0)
    DisableObjKeyGuide(z16, 0)
    """State 2: Open the front and back doors"""
    ChangeObjState(z13, 74)
    ChangeObjState(z16, 74)
    """State 3: End state"""
    return 0

def event_m10_32_x98(z12=_, action1=_):
    """[DLC] [Preset] Stone monument displayed as text
    z12: Stele OBJ instance ID
    action1: Text ID
    """
    """State 0,1: [DLC] [Reproduction] Stone monument_SubState displayed in text"""
    assert event_m10_32_x99()
    """State 3: [DLC] [Condition] Stone monument_SubState displayed in text"""
    assert event_m10_32_x101(z12=z12)
    """State 2: [DLC] [Execution] Stone monument_SubState displayed in text"""
    assert event_m10_32_x100(action1=action1, z12=z12)
    """State 4: End state"""
    return 0

def event_m10_32_x99():
    """[DLC] [Reproduction] Stone monument displayed in text"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x100(action1=_, z12=_):
    """[DLC] [execution] Stone monument displayed as text
    action1: Text ID
    z12: Stele OBJ instance ID
    """
    """State 0,2: Disable key guide"""
    DisableObjKeyGuide(z12, 1)
    """State 1: Text display"""
    DisplayEventMessage(action1, 0, 0, 0)
    assert (GetStateTime() > 1.5) != 0
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z12, 0)
    """State 4: End state"""
    return 0

def event_m10_32_x101(z12=_):
    """[DLC] [Condition] Stone monument displayed in text
    z12: Stele OBJ instance ID
    """
    """State 0,1: Wait for decision to check"""
    IsObjSearched(0, z12)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x102(z3=132000051):
    """[DC] [Condition] Zako's transparency and materialization
    z3: Miko's pupil _ possession flag
    """
    """State 0,1: Miko's pupil possession flag judgment"""
    CompareEventFlag(0, z3, 1)
    CompareEventFlag(1, z3, 0)
    if ConditionGroup(0):
        """State 3: Materialization"""
        return 1
    elif ConditionGroup(1):
        """State 2: Transparency"""
        return 0

def event_m10_32_x103(z1=_, z2=98382000, z3=132000051):
    """[DC] [execution] Zako's transparency and materialization_transparency
    z1: Generator ID
    z2: Translucent effect ID
    z3: Miko's pupil _ possession flag
    """
    """State 0,1: Giving Zako a special effect"""
    SetEnemySpEffect(z1, z2, 10, 4)
    """State 2: Possession flag judgment"""
    CompareEventFlag(0, z3, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_32_x104():
    """[DC] [Reproduction] Zako's transparency and materialization_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x105(z1=_, z2=98382000, z3=132000051):
    """[DC] [Preset] Zako transparency and materialization
    z1: Generator ID
    z2: Translucent effect ID
    z3: Miko's pupil _ possession flag
    """
    """State 0,1: [DC] [Reproduction] Transparency and materialization of Zako_empty_SubState"""
    assert event_m10_32_x104()
    """State 4: [DC] [Condition] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x102(z3=z3)
    if call.Get() == 1:
        """State 2: [DC] [execution] Zako's transparency and materialization_substance_SubState"""
        assert event_m10_32_x118(z1=z1, z2=z2)
        """State 5: Finish"""
        return 0
    elif call.Get() == 0:
        """State 3: [DC] [execution] Zako transparency and materialization_transparency_SubState"""
        assert event_m10_32_x103(z1=z1, z2=z2, z3=z3)
        """State 6: Rerun"""
        return 1

def event_m10_32_x106(flag1=_):
    """[DC] [Reproduction] Illusion enemy of ruins _ Defeat count
    flag1: Judgment flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Have you counted it before saving?"""
        if GetEventFlag(flag1) != 0:
            pass
        else:
            """State 3: Defeat determination"""
            return 0
    """State 4: Do nothing: Quit"""
    return 1

def event_m10_32_x107(z9=_, z10=4, z11=8):
    """[DC] [Condition] Illusionary enemies of ruins _ Defeat count
    z9: Generator ID
    z10: Defeat count variable
    z11: Necessary number of destruction
    """
    """State 0,1: Character destruction waiting or upper limit number judgment or destruction number judgment"""
    IsChrDead(0, z9)
    IsChrMaxRespawnCount(1, z9, 1, 0)
    CompareEventFlagValue(1, 0, 4, z11, 3)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Variable addition"""
        return 0

def event_m10_32_x108(z10=4, flag1=_):
    """[DC] [Execution] Illusionary enemy of ruins _ Defeat count
    z10: Defeat count variable
    flag1: Judgment flag
    """
    """State 0,1: Defeat count + 1 judgment flag ON"""
    SetEventFlag(flag1, 1)
    AddGlobalVariable(z10, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x109(flag1=_, z9=_, z10=4, z11=8):
    """[DC] [Preset] Illusionary enemies of ruins _ Defeat count
    flag1: Judgment flag
    z9: Generator ID
    z10: Defeat count variable
    z11: Necessary number of destruction
    """
    """State 0,1: [DC] [Reproduction] Illusionary enemy of ruins _ Defeat count _ SubState"""
    call = event_m10_32_x106(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Phantom enemies of ruins_Countdown count_SubState"""
        call = event_m10_32_x107(z9=z9, z10=z10, z11=z11)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [DC] [Execution] Illusionary enemy of ruins _ Defeat count _ SubState"""
            assert event_m10_32_x108(z10=z10, flag1=flag1)
    """State 4: End state"""
    return 0

def event_m10_32_x110(z6=4, z7=8):
    """[DC] [Condition] White spirit sign appears by destroying phantom enemies in ruins
    z6: Defeat count variable
    z7: Necessary number of destruction
    """
    """State 0,1: Did you destroy a certain number of phantom enemies?"""
    CompareEventFlagValue(0, 0, z6, z7, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x111(z8=132000075):
    """[DC] [Execution] White spirit sign appears by destroying phantom enemies in ruins
    z8: White spirit sign appearance flag
    """
    """State 0,1: White spirit sign appearance flag ON"""
    SetEventFlag(z8, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x112():
    """[DC] [Reproduction] White spirit sign appears by destroying phantom enemies in ruins"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: Finish"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m10_32_x113(z6=4, z7=8, z8=132000075):
    """[DC] [Preset] Defeat the phantom enemies of the ruins.
    z6: Defeat count variable
    z7: Necessary number of destruction
    z8: White spirit sign appearance flag
    """
    """State 0,1: [DC] [Reproduction] White spirit sign appears by destroying the phantom enemy of the ruins_SubState"""
    call = event_m10_32_x112()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] White spirit sign appears by destroying phantom enemies in the ruins_SubState"""
        assert event_m10_32_x110(z6=z6, z7=z7)
        """State 2: [DC] [Execution] Defeat the phantom enemy of the ruins."""
        assert event_m10_32_x111(z8=z8)
    """State 4: End state"""
    return 0

def event_m10_32_x114():
    """[DC] [Reproduction] Judgment of possession of Miko's eyes"""
    """State 0,1: Host?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: Possession judgment"""
        return 0

def event_m10_32_x115():
    """[DC] [Condition] Judgment of possession of Miko's eyes"""
    """State 0,1: Do you have a shrine maiden's eyes?"""
    # goods:53600000:Eye of the Priestess
    DoesPlayerHaveItem(0, 53600000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 2: In possession"""
        return 0
    else:
        """State 3: Not possess"""
        return 1

def event_m10_32_x116(z4=132000051, z5=_):
    """[DC] [Execution] Judgment of possession of Miko's eyes
    z4: Miko's Eye: Possession Flag
    z5: ON or OFF
    """
    """State 0,1: Possession flag switching"""
    SetEventFlag(z4, z5)
    """State 2: Finish"""
    return 0

def event_m10_32_x117(z4=132000051):
    """[DC] [Preset] Judgment of possession of Miko's eyes
    z4: Miko's Eye: Possession Flag
    """
    """State 0,1: [DC] [Reproduction] Judgment of possession of a shrine maiden_SubState"""
    call = event_m10_32_x114()
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 3: [DC] [Condition] Judgment of possession of a shrine maiden_SubState"""
        call = event_m10_32_x115()
        if call.Get() == 0:
            """State 2: [DC] [Execution] Judgment of possession of a shrine maiden_SubState"""
            assert event_m10_32_x116(z4=z4, z5=1)
        elif call.Get() == 1:
            """State 4: [DC] [Execution] Judgment of possession of a shrine maiden_2_SubState"""
            assert event_m10_32_x116(z4=z4, z5=0)
    """State 5: Finish"""
    return 0

def event_m10_32_x118(z1=_, z2=98382000):
    """[DC] [execution] Zako's transparency and materialization_materialization
    z1: Generator ID
    z2: Translucent effect ID
    """
    """State 0,1: Release special effects of Zako"""
    ClearEnemySpEffect(z1, z2)
    """State 2: End state"""
    return 0

def event_m10_32_111012():
    """OBJ: Durahan: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z125=104000, z126=10324200, z127=257, z128=3070)
    Quit()

def event_m10_32_111013():
    """OBJ: Durahan: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:3070:Head of Vengarl
    event_m10_32_x8(z109=132010170, z110=132020171, z111=104000, z112=10324200, z113=111012, npc1=3070)
    Quit()

def event_m10_32_111014():
    """OBJ: Neckless Durahan: Death determination"""
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Death determination: branch"""
        CompareEventFlag(0, 102010, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Death determination: Wait"""
            IsChrDead(0, 2220)
            assert ConditionGroup(0)
            """State 4: Death determination: death flag setting"""
            SetEventFlag(102010, 1)
            SetEventFlag(102000, 1)
            CompareEventFlag(8, 102010, 1)
            CompareEventFlag(8, 102000, 1)
            assert ConditionGroup(8)
    """State 5: Death determination: System: End"""
    EndMachine()
    Quit()

def event_m10_32_111182():
    """OBJ: Shenzhen Pilgrim: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z125=104122, z126=10324000, z127=41, z128=7250)
    Quit()

def event_m10_32_111183():
    """OBJ: Shenzhen Pilgrims: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7250:Darkdiver Grandahl
    event_m10_32_x8(z109=132010100, z110=132020101, z111=104120, z112=10324000, z113=111182, npc1=7250)
    Quit()

def event_m10_32_111184():
    """OBJ: Shenzhen Pilgrim: Death Determination"""
    """State 0,1: [Lib] NPC: Death Judgment: Shenzhen Pilgrim_SubState"""
    event_m10_32_x37(z55=40, z56=104122)
    Quit()

def event_m10_32_111185():
    """OBJ: Shenzhen Pilgrim: Appearance Judgment"""
    """State 0,1: [Lib] NPC: Shenzhen Pilgrim: Appearance Judgment_SubState"""
    event_m10_32_x25(z64=102317, z65=102324, z66=102331, z67=102332, z68=102315, z69=102316, z70=103622)
    Quit()

def event_m10_32_111232():
    """OBJ: Wandering Warrior: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z125=104152, z126=10324300, z127=56, z128=7420)
    Quit()

def event_m10_32_111233():
    """OBJ: Wandering Warrior: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_32_x8(z109=132010120, z110=132020121, z111=104150, z112=10324300, z113=111232, npc1=7420)
    Quit()

def event_m10_32_111234():
    """OBJ: Wandering Warrior: Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_32_x10(z103=55, z104=104152)
    Quit()

def event_m10_32_111235():
    """OBJ: Wandering Warrior: Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_32_x11(z98=104150, z99=102405, z100=102406, z101=132010127, z102=103651)
    Quit()

def event_m10_32_111452():
    """OBJ: Upper weapon shop: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z125=104361, z126=10324100, z127=266, z128=7760)
    Quit()

def event_m10_32_111453():
    """OBJ: Upper weapon shop: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7760:Weaponsmith Ornifex
    event_m10_32_x8(z109=132010190, z110=132020191, z111=104360, z112=10324100, z113=111452, npc1=7760)
    Quit()

def event_m10_32_111454():
    """OBJ: Upper weapon shop: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_32_x10(z103=265, z104=104361)
    Quit()

def event_m10_32_111522():
    """OBJ: Manscorpion ♂: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z125=104430, z126=10324600, z127=326, z128=5020)
    Quit()

def event_m10_32_111523():
    """OBJ: Manscorpion ♂: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:5020:Manscorpion Tark
    event_m10_32_x8(z109=132010150, z110=132020151, z111=104430, z112=10324600, z113=111522, npc1=5020)
    Quit()

def event_m10_32_111524():
    """OBJ: Manscorpion ♂: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_32_x19(z79=102980, z80=626, z81=104430, z82=60, z83=103930, z84=-1)
    Quit()

def event_m10_32_118100():
    """Multi-use NPC: White Spirit Test 1: White Phantom Sign Display"""
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, 132000075, 1)
    assert ConditionGroup(0)
    """State 2: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_32_x26(z63=627)
    Quit()

def event_m10_32_120080():
    """Trophy: Deep Darkness Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_32_x36(flag9=132020109, z57=26)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_32_120160():
    """Trophy: Thinking neck"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_32_x36(flag9=132020177, z57=36)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_32_3000000():
    """[DLC] Warp move to ice map"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m10_32_x42(z52=10323800, z53=50370000, z54=5100000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_32_3001000():
    """[DLC] Stone monument displayed in text_1"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5400:"Forbidden is the path\nto the ancient king's domain"
    assert event_m10_32_x98(z12=10323810, action1=5400)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_32_3001010():
    """[DLC] Stone monument displayed in text_2"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5420:"With water dry, and path amiss,\nwoeful temptation is dismissed"
    assert event_m10_32_x98(z12=10323811, action1=5420)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_32_3001020():
    """[DLC] Stone monument displayed in text_3"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5430:"Trespassers will face\nadversity befitting a monarch"
    assert event_m10_32_x98(z12=10323812, action1=5430)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_32_3001030():
    """[DLC] Stone monument displayed as text_4"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5610:"Eleum Loyce, land of the Ivory King, lies cold as death,\nnary a hint of warmth remaining"
    assert event_m10_32_x98(z12=10323813, action1=5610)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_32_4000000():
    """[DC] Lion Warrior _ Petrification Stop 4_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z90=2210, z91=0, z92=15, z93=132000016, z94=0, z95=1600, z96=3, z97=4000010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4000010():
    """[DC] Lion Warrior _ Petrification Stop 4_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z71=2210, z72=0, z73=132000016, z74=0, z75=0, z76=4000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4000020():
    """[DC] Lion Warrior _ Petrification Stop 4_ Navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z58=6000020, z59=0, z60=2, flag10=132000016, flag11=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4001000():
    """[DC] Lion Warrior _ Petrification Stop 5_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z90=2103, z91=0, z92=15, z93=132000017, z94=0, z95=1600, z96=3, z97=4001010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4001010():
    """[DC] Lion Warrior _ Petrification Stop 5_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z71=2103, z72=0, z73=132000017, z74=0, z75=0, z76=4001000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4001020():
    """[DC] Lion Warrior _ Petrochemical stop 5_ Navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z58=6001020, z59=0, z60=2, flag10=132000017, flag11=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4002000():
    """[DC] Lion Warrior _ Petrification Stop 6_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z90=2500, z91=0, z92=15, z93=132000018, z94=0, z95=1600, z96=3, z97=4002010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4002010():
    """[DC] Lion Warrior _ Petrification Stop 6_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z71=2500, z72=0, z73=132000018, z74=0, z75=0, z76=4002000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4002020():
    """[DC] Lion Warrior _ Petrification Stop 6_ Navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z58=6002020, z59=0, z60=2, flag10=132000018, flag11=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4003000():
    """[DC] Transparency and materialization of Zako_Winter Deep 1"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=1300, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003010():
    """[DC] Transparency and materialization of Zako_Winter 2"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=1310, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003100():
    """[DC] Zako's transparency and materialization_Fog Forest 1"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2000, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003110():
    """[DC] Transparency and materialization of Zako_Fog Forest 2"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2001, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003120():
    """[DC] Transparency and materialization of Zako_Fog Forest 3"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2002, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003130():
    """[DC] Transparency and materialization of Zako_Fog Forest 4"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2003, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003140():
    """[DC] Zako's transparency and materialization_Fog Forest 5"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2006, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003150():
    """[DC] Transparency and materialization of Zako_Fog Forest 6"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2007, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003160():
    """[DC] Transparency and materialization of Zako_Fog Forest 7"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2009, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003200():
    """[DC] Transparency and materialization of Zako_Ruins 1"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2400, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003210():
    """[DC] Transparency and materialization of Zako_Ruins 2"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2410, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003220():
    """[DC] Transparency and materialization of Zako_Ruins 3"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2420, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003230():
    """[DC] Transparency and materialization of Zako _ Ruins 4"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2430, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003240():
    """[DC] Transparency and materialization of Zako _ Ruins 5"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2421, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003250():
    """[DC] Transparency and materialization of Zako_Ruins 6"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2440, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003260():
    """[DC] Transparency and materialization of Zako _ Ruins 7"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2450, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003270():
    """[DC] Transparency and materialization of Zako_Ruins 8"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2460, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003300():
    """[DC] Zako's transparency and materialization"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=1250, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_32_4003900():
    """[DC] Determination of possession of Miko's eyes"""
    """State 0,2: [DC] [Preset] Judgment of possession of a shrine maiden_SubState"""
    assert event_m10_32_x117(z4=132000051)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004000():
    """[DC] Illusionary enemy of ruins _ Defeat count 1"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020056, z9=2400, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004010():
    """[DC] Illusionary enemy of ruins _ Defeat count 2"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020057, z9=2410, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004020():
    """[DC] Illusionary enemy of ruins _ Defeat count 3"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020058, z9=2420, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004030():
    """[DC] Illusionary enemy of ruins _ Defeat count 4"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020059, z9=2430, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004040():
    """[DC] Illusionary enemy of ruins _ Defeat count 5"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020060, z9=2421, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004050():
    """[DC] Illusionary enemy of ruins _ Defeat count 6"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020061, z9=2440, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004060():
    """[DC] Illusionary enemy of ruins _ Defeat count 7"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020062, z9=2450, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4004070():
    """[DC] Illusionary enemy of ruins _ Defeat count 8"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(flag1=132020063, z9=2460, z10=4, z11=8)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4005000():
    """[DC] White spirit sign appears by destroying phantom enemies in ruins"""
    """State 0,2: [DC] [Preset] Defeat the phantom enemy of the ruins."""
    assert event_m10_32_x113(z6=4, z7=8, z8=132000075)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4011000():
    """[DC] Wanderer B_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_32_x46(flag6=132020043, z40=14, flag7=132000044, z41=2, z42=20)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_32_x51(z45=80000000, z46=0, z47=5, z48=956, val1=1, z49=20, z50=80000001, z51=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_32_x51(z45=80000100, z46=0, z47=5, z48=956, val1=2, z49=20, z50=80000101, z51=80000199)
        """State 2: Start flag ON"""
        SetEventFlag(132020045, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4011010():
    """[DC] Wanderer B_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_32_x54(flag8=132000044, z43=956, mode2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_32_4031000():
    """[DC] NPC White Spirit_Gesture Management_Manscorpion♀"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_32_x59(flag5=132000081, z38=824, z39=132020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

