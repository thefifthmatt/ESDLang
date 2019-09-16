# -*- coding: utf-8 -*-
def event_m10_32_1000():
    """Switching the gimmick door related flags on the connection path"""
    """State 0,2: [Lib] [Preset] Switch connection flag when in map_SubState"""
    assert event_m10_32_x23(z88=105405, z89=1)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_32_2000():
    """Generation management of phantom enemies 1"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2000, z33=1, z34=132020020, z35=132020001)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_2010():
    """Generation management of phantom enemies 2"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2001, z33=2, z34=132020021, z35=132020002)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_2020():
    """Generation management of phantom enemies 3"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2002, z33=3, z34=132020022, z35=132020003)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_2030():
    """Generation management of phantom enemies 4"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2003, z33=4, z34=132020023, z35=132020004)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_2040():
    """Generation management of phantom enemies 5"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2006, z33=5, z34=132020024, z35=132020005)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_2050():
    """Generation management of phantom enemies 6"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2007, z33=6, z34=132020025, z35=132020006)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_2060():
    """Generation management of phantom enemies 7"""
    """State 0,3: [Preset] Phantom enemy generation management_SubState"""
    call = event_m10_32_x77(z32=2009, z33=7, z34=132020026, z35=132020007)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_4000():
    """OBJ: Shenzhen Pilgrim: Magic Circle Open"""
    """State 0,1: [Lib] Pilgrim of Shenzhen: Magic Square: Open_SubState"""
    event_m10_32_x4(z133=102327, z134=102330, z135=10323000)

def event_m10_32_4001():
    """OBJ: Shenzhen Pilgrim: Magic Warp"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Key Guide_SubState"""
    event_m10_32_x6(z125=102327, z126=10323000, z127=102330, z128=400010, z129=0)

def event_m10_32_4002():
    """OBJ: Shenzhen Pilgrim: Magic Circle Opening"""
    """State 0,1: [Lib] Pilgrim in Shenzhen: Magic Square: Opening Production_SubState"""
    event_m10_32_x5(z130=10323000, z131=102327, z132=132020107)

def event_m10_32_5000():
    """Pitfall_Large_Navimesh switching"""
    """State 0,2: [Preset] Pitfall_SubState"""
    assert event_m10_32_x63(z39=10321500, z40=500000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_5010():
    """Pitfall_Small_Navigation mesh switching"""
    """State 0,2: [Preset] Pitfall_SubState"""
    assert event_m10_32_x63(z39=10321505, z40=501000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6000():
    """Boss: Manscorpion ♀ Battle"""
    """State 0,2: [Preset] Manscorpion Battle_Start_SubState"""
    assert event_m10_32_x79(z23=132000081, z24=101, z25=1032000, z26=132020080, z27=5, mode1=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6010():
    """OBJ Navimesh change destroyed during the Manscorpion battle 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321250, z97=20, z98=601000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6020():
    """OBJ Navimesh change 2 destroyed during Manscorpion battle"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321260, z97=20, z98=602000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6030():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321261, z97=20, z98=603000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6040():
    """OBJ Navimesh change destroyed during the Manscorpion battle 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321304, z97=20, z98=604000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6050():
    """OBJ Navimesh change destroyed during the Manscorpion battle 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321305, z97=20, z98=605000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6060():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 6"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321306, z97=20, z98=606000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6070():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 7"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321307, z97=20, z98=607000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_6080():
    """OBJ Navimesh changes destroyed during the Manscorpion battle 8"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_32_x15(z96=10321301, z97=20, z98=608000, z99=0, z100=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_7000():
    """Treasure corpse stone pillar_01"""
    """State 0,2: [Preset] Stone Pillar_SubState"""
    assert event_m10_32_x64(z36=10321250, z37=10326200, z38=72)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_8000():
    """King's door"""
    """State 0,3: [Preset] King's Door_City of Shadows_SubState"""
    call = event_m10_32_x89(z20=10320400, z21=105310, z22=132000055)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_32_9000():
    """White door to the royal castle"""
    """State 0,3: [Preset] White door to the Royal Castle_SubState"""
    call = event_m10_32_x68(z14=10320405, z15=900000, z16=100420, z17=10320406, z18=900010)
    if call.Get() == 0:
        """State 1: Door release (end)"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Door not open (re-execution)"""
        RestartMachine()

def event_m10_32_10000():
    """Lion Warrior _ Petrification Stop 1_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z101=2040, z102=0, z103=15, z104=132000010, z105=0, z106=1600, z107=3, z108=10010)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_10010():
    """Lion Warrior _ Petrification Stop 1_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z82=2040, z83=0, z84=132000010, z85=0, z86=0, z87=10000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_10020():
    """Lion Warrior _ Petrification Stop 1_ Switching Navigation"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z67=1002000, z68=0, z69=2, z70=132000010, z71=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_11000():
    """Lion Warrior _ Petrification Stop 2_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z101=2310, z102=0, z103=15, z104=132000012, z105=0, z106=1600, z107=3, z108=11010)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_11010():
    """Lion Warrior _ Petrification Stop 2_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z82=2310, z83=0, z84=132000012, z85=0, z86=0, z87=11000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_11020():
    """Lion Warrior _ Petrification Stop 2_ Switching Navigation"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z67=1102000, z68=0, z69=2, z70=132000012, z71=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_12000():
    """Lion Warrior _ Petrochemical Stop 3_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z101=2041, z102=0, z103=15, z104=132000014, z105=0, z106=1600, z107=3, z108=12010)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_12010():
    """Lion Warrior _ Petrification Stop 3_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z82=2041, z83=0, z84=132000014, z85=0, z86=0, z87=12000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_12020():
    """Lion Warrior _ Petrochemical Stop 3_ Navigation Switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z67=1202000, z68=0, z69=2, z70=132000014, z71=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_12050():
    """Acquire items by destroying petrified characters"""
    """State 0,2: [Preset] Earn items by destroying petrified characters_SubState"""
    # lot:60009000:Fang Key
    assert event_m10_32_x96(lot1=60009000, z19=2041)
    """State 1: Finish"""
    EndMachine()

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

def event_m10_32_14000():
    """Key door that opens with "Beast Key" """
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_32_x9(z116=1005, z117=1105, z118=50850000, z119=132000050)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_80000():
    """Fireworks for regeneration 01_ in the building of the branch road"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_32_x30(z72=1032000, z73=1032099)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_81000():
    """Regeneration of fire 02_in the huge bridge"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_32_x30(z72=1032100, z73=1032199)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_x0(z140=0, z141=0, z61=50370000, z62=5100000):
    """[Lib] Warp between maps after poly play
    z140: Pre-warp poly play ID
    z141: Poly Play ID after Warp
    z61: Map ID
    z62: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z140, z141, z61, z62, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_32_x1(z136=_, z137=_, z138=_, z139=_):
    """[Lib] NPC: Grave Placement: General purpose
    z136: Death map: Global event flag
    z137: Tomb: OBJ instance ID
    z138: Tomb move to: Generator ID
    z139: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z136, 1)
    IsGraveGeneratable(8, z139, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z137, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z137, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_32_x2(z122=_, z123=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z122: Global: death flag
    z123: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z123, 10, 0)
    CompareObjState(1, z123, 20, 0)
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
    IsObjSearched(0, z123)
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

def event_m10_32_x3(z120=_, z121=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z120: Area other flags: Ghost appearance
    z121: Area other flags: Conversation start
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
    SetEventFlag(z120, 1)
    CompareEventFlag(0, z120, 1)
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
    SetEventFlag(z121, 1)
    CompareEventFlag(0, z121, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_32_x4(z133=102327, z134=102330, z135=10323000):
    """[Lib] Shenzhen Pilgrim: Magic Square: Open
    z133: Magic Square: Open: Global Event Flag
    z134: Magic Square: Invasion: Global Event Flag
    z135: Magic Square: OBJ instance ID
    """
    """State 0,1: Magic Square: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 7: Magic square: All open judgment"""
        CompareEventFlag(8, 100979, 1)
        CompareEventFlag(8, z133, 1)
        CompareEventFlag(9, 100979, 1)
        CompareEventFlag(8, z133, 0)
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
            CompareObjState(0, z135, 30, 0)
            assert ConditionGroup(0)
        else:
            """State 3: Magic Square: Player Return Judgment"""
            CompareEventFlag(8, z133, 1)
            CompareEventFlag(8, z134, 1)
            if ConditionGroup(8):
                """State 4: Magic square: Flag initialization setting"""
                SetEventFlag(z133, 0)
                SetEventFlag(z134, 0)
                CompareEventFlag(8, z133, 0)
                CompareEventFlag(8, z134, 0)
                assert ConditionGroup(8)
                """State 8: Magic Square: Erasure"""
                ChangeOwnObjState(80)
                CompareObjState(0, z135, 10, 0)
                assert ConditionGroup(0)
            else:
                """State 6: Magic Square: Open Flag Judgment"""
                CompareEventFlag(0, z133, 1)
                if ConditionGroup(0):
                    Goto('L0')
                else:
                    pass
    """State 5: Magic Square: System: End"""
    EndMachine()

def event_m10_32_x5(z130=10323000, z131=102327, z132=132020107):
    """[Lib] Shenzhen Pilgrims: Magic Square: Opening Production
    z130: Magic Square: OBJ instance ID
    z131: Magic Square: Open: Global Event Flag
    z132: Magic Square: Production Start: Area and Other Flags
    """
    """State 0,4: Appearance production: Start"""
    CompareEventFlag(0, z132, 1)
    assert ConditionGroup(0)
    """State 3: Appearance effect: Open flag setting"""
    SetEventFlag(z131, 1)
    CompareEventFlag(0, z131, 1)
    assert ConditionGroup(0)
    """State 1: Appearance Direction: Magic Square Appearance"""
    ChangeOwnObjState(70)
    CompareObjState(0, z130, 30, 0)
    assert ConditionGroup(0)
    """State 5: Appearance production: End"""
    SetEventFlag(z132, 0)
    CompareEventFlag(0, z132, 0)
    assert ConditionGroup(0)
    """State 2: Appearance production: System: End"""
    EndMachine()

def event_m10_32_x6(z125=102327, z126=10323000, z127=102330, z128=400010, z129=0):
    """[Lib] Shenzhen Pilgrim: Magic Square: Key Guide
    z125: Magic Square: Open: Global Event Flag
    z126: Magic Square: OBJ instance ID
    z127: Magic Square: Invasion: Global Event Flag
    z128: Magic Square: Warp Point
    z129: Magic Square: During Warp: Area Other Flag
    """
    """State 0,1: Key guide: Start"""
    CompareObjState(0, z126, 30, 0)
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
        IsObjSearched(2, z126)
        CompareObjState(3, z126, 10, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
        elif ConditionGroup(2):
            """State 7: Key guide: Intrusion flag: Setting"""
            ProhibitMultiplayer(1)
            SetEventFlag(z129, 1)
            """State 8: Shenzhen Pilgrim: Magic Square: Warp_SubState"""
            call = event_m10_32_x7(z128=z128, z127=z127)
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

def event_m10_32_x7(z128=400010, z127=102330):
    """Shenzhen Pilgrim: Magic Square: Warp
    z128: Warp point ID
    z127: Intrusion: Global flag
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
            SetEventFlag(z127, 1)
            PlayCutsceneAndWarpToMap(0, 0, 40030000, z128, 0)
            assert CutsceneWarpEnded() != 0
            """State 2: Warp: Wait for completion"""
            CompareEventFlag(0, 0, 1)
            assert ConditionGroup(0)
            """State 6: Normal: End state"""
            return 0
    """State 7: Re-execution: end state"""
    return 1

def event_m10_32_x8(z120=_, z121=_, z122=_, z123=_, z124=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z120: Ghost Appearance: Area Other Flag
    z121: Conversation start: Area and other flags
    z122: Death: Global event flag
    z123: Tomb: OBJ instance ID
    z124: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z124, 1, 0)
    CompareEventFlag(9, z120, 1)
    CompareObjState(9, z123, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z121, 1)
        CompareEventFlag(0, z121, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_32_x2(z122=z122, z123=z123, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_32_x3(z120=z120, z121=z121, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_32_x9(z116=1005, z117=1105, z118=50850000, z119=132000050):
    """[Lib] Item specified door unlocking_2
    z116: Text ID when opened
    z117: Text ID when not opened
    z118: item
    z119: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z118, z116, z117, z119, 0)
    """State 2: End state"""
    return 0

def event_m10_32_x10(z114=_, z115=_):
    """[Lib] NPC: Death determination: General purpose
    z114: Generator ID
    z115: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z115, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z114)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z115, 1)
            CompareEventFlag(0, z115, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_32_x11(z109=104150, z110=102405, z111=102406, z112=132010127, z113=103651):
    """[Lib] Appearance determination: General purpose
    z109: Death: Global event flag
    z110: Local emigration permission: Global event flag
    z111: Relocation permission after moving: Global event flag
    z112: Appearance determination: Area and other flags
    z113: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z109, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z110, 1)
            CompareEventFlag(8, z111, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z110, 1)
                CompareEventFlag(8, z113, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z112, 1)
                    CompareEventFlag(0, z112, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z112, 0)
                    CompareEventFlag(0, z112, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z112, 0)
        CompareEventFlag(0, z112, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m10_32_x12(z20=10320400, z22=132000055):
    """[Lib] [Condition] King's door
    z20: King's door OBJ instance ID
    z22: Opening flag
    """
    """State 0,2: Did you approach the king's door?"""
    CompareObjPlayerDistance(0, z20, 3, 5)
    assert ConditionGroup(0)
    """State 1: Is it equipped with a king's ring? Has it been opened?"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    SetConditionGroup(0, 8)
    # goods:40510000:King's Ring
    DoesPlayerHaveItem(8, 40510000, 1, 3, 1, 1, 0)
    CompareEventFlag(8, z22, 1)
    if ConditionGroup(0):
        """State 4: Equipped with a king's ring"""
        return 1
    else:
        """State 3: Not qualified"""
        return 0

def event_m10_32_x13(z20=10320400):
    """[Lib] [execution] King's door _ not open
    z20: King's door OBJ instance ID
    """
    """State 0,1: Event message display"""
    # action:2000:"Produce the symbol of the King"
    DisplayEventMessage(2000, 0, 0, 0)
    """State 2: Equipped with an or ring away from the king's door?"""
    CompareObjPlayerDistance(0, z20, 10, 3)
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_32_x14(z101=_, z102=0, z103=15, z104=_, z105=0, z106=1600, z107=3, z108=_):
    """[Lib] Character: Petrochemical: Key guide
    z101: generator
    z102: Death: Global event flag
    z103: Event action
    z104: Petrified: Area and other flags
    z105: Petrified: Global event flag
    z106: Key guide parameters
    z107: Petrification start state ID
    z108: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z101, z107, 0)
    CompareEventStatus(8, z108, 1, 0)
    CompareEventFlag(2, z104, 1)
    CompareEventFlag(3, z105, 1)
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
    CreateKeyGuideArea(34, z106)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z101)
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
                PlayerActionRequest(z103)
                IsPlayerPlayingMotion(0, z103, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z104, 1)
                CompareEventFlag(0, z104, 1)
                SetEventFlag(z105, 1)
                CompareEventFlag(1, z105, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z103, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_32_x15(z96=_, z97=20, z98=_, z99=0, z100=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z96: Object instance ID
    z97: OBJ state ID
    z98: Navimesh switching point ID
    z99: Additional attributes
    z100: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_32_x16(z96=z96, z97=z97, z98=z98, z100=z100, z99=z99)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_32_x17(z96=z96, z97=z97, z98=z98)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_32_x18(z96=z96, z97=z97, z98=z98, z99=z99, z100=z100)
    """State 4: End state"""
    return 0

def event_m10_32_x16(z96=_, z97=20, z98=_, z100=2, z99=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z96: Target OBJ instance ID
    z97: Target OBJ state ID
    z98: Navimesh switching point ID
    z100: Additional attributes
    z99: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z96, z97, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z98, z100)
        DeleteNavimeshAttribute(z98, z99)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_32_x17(z96=_, z97=20, z98=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z96: Target OBJ instance ID
    z97: Target OBJ state ID
    z98: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z96, z97, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x18(z96=_, z97=20, z98=_, z99=0, z100=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z96: Target OBJ instance ID
    z97: Target OBJ state ID
    z98: Navimesh switching point ID
    z99: Additional attributes
    z100: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z98, z99)
    DeleteNavimeshAttribute(z98, z100)
    """State 2: End state"""
    return 0

def event_m10_32_x19(z90=102980, z91=626, z92=104430, z93=60, z94=103930, z95=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z90: White Phantom can appear: Global event flag
    z91: White Phantom: Generator ID
    z92: Death: Global event flag
    z93: Body: Generator group ID
    z94: Hostile: Global event flag
    z95: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z91)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z92, 1)
        CompareEventFlag(1, z94, 1)
        CompareEventFlag(2, z90, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z91)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z92, 1)
            CompareEventFlag(1, z94, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z91)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z92, 1)
            CompareEventFlag(1, z94, 1)
            HasNpcPhantomSpawned(2, z91, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z93, 0)
                HasNpcPhantomSpawned(0, z91, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z91)
    """State 4: Appearance: System: End"""
    EndMachine()

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

def event_m10_32_x22(z88=105405, z89=1):
    """[Lib] [Execution] Switch to connection flag when in map
    z88: Global event flag for connection
    z89: Flag switching
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z88, z89)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z88, z89)
    assert ConditionGroup(0)
    """State 3: For next judgment: Did you get out of the map?"""
    IsPlayerInTheMap(0, 0, 0)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_32_x23(z88=105405, z89=1):
    """[Lib] [Preset] Switch the connection flag when in the map
    z88: Global event flag for connection
    z89: Flag switching
    """
    """State 0,1: [Lib] [Reproduction] Switch connection flag when in map_SubState"""
    assert event_m10_32_x20()
    """State 3: [Lib] [Condition] Switch to the connection flag when in the map_SubState"""
    assert event_m10_32_x21()
    """State 2: [Lib] [Execution] Switch to connection flag when in map _SubState"""
    assert event_m10_32_x22(z88=z88, z89=z89)
    """State 4: End state"""
    return 0

def event_m10_32_x24(z82=_, z83=0, z84=_, z85=0, z86=0, z87=_):
    """[Lib] Character: Petrified: Appearance setting
    z82: Generator ID
    z83: Death: Global event flag
    z84: Petrified: Area and other flags
    z85: Petrified: Global event flag
    z86: Startup state
    z87: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z82)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z83, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z84, 1)
                CompareEventFlag(1, z85, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z82, z86)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()

def event_m10_32_x25(z75=102317, z76=102324, z77=102331, z78=102332, z79=102315, z80=102316, z81=103622):
    """[Lib] NPC: Shenzhen Pilgrims: Appearance Judgment
    z75: Generation stop: Global event flag
    z76: Appearance permission: Global event flag
    z77: Sub 1 encountering: Global event flag
    z78: During sub-2 encounter: Global event flag
    z79: Sub 1 generation stop: Global event flag
    z80: Sub 2 generation stop: Global event flag
    z81: Hostile map: Global event flag
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
                CompareEventFlag(0, z75, 1)
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
                        CompareEventFlag(8, z77, 1)
                        CompareEventFlag(8, z79, 0)
                        CompareEventFlag(9, z78, 1)
                        CompareEventFlag(9, z80, 0)
                        if ConditionGroup(8):
                            pass
                        elif ConditionGroup(9):
                            pass
                        else:
                            Goto('L0')
                """State 5: Appearance judgment: Appearance impossible"""
                SetEventFlag(z76, 0)
                CompareEventFlag(0, z76, 0)
                assert ConditionGroup(0)
                Goto('L1')
            """State 6: Appearance determination: Appearance allowed"""
            Label('L0')
            SetEventFlag(z76, 1)
            CompareEventFlag(0, z76, 1)
            assert ConditionGroup(0)
    """State 3: Appearance determination: System: End"""
    Label('L1')
    EndMachine()

def event_m10_32_x26(z74=627):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z74: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z74)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_32_x27():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x28(z72=_, z73=_):
    """[Lib] [execute] Rebirth fire
    z72: Flag start ID
    z73: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z72, z73, 0)
    """State 2: End state"""
    return 0

def event_m10_32_x29():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x30(z72=_, z73=_):
    """[Lib] [Preset] Rebirth
    z72: Flag start ID
    z73: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_32_x27()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_32_x29()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_32_x28(z72=z72, z73=z73)
    """State 4: End state"""
    return 0

def event_m10_32_x31(z20=10320400):
    """[Lib] [Condition] King's door closed
    z20: King's door OBJ instance ID
    """
    """State 0,1: Did you leave the king's door?"""
    CompareObjPlayerDistance(0, z20, 30, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x32(z70=_, z71=0, z69=2, z68=0, z67=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z70: Other flags
    z71: Global flag
    z69: Additional attributes
    z68: Delete attribute
    z67: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z70) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z71) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z67, z69)
        DeleteNavimeshAttribute(z67, z68)
        """State 3: Flag OFF"""
        return 0

def event_m10_32_x33(z70=_, z71=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z70: Other flags
    z71: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z70, 1)
    CompareEventFlag(0, z71, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_32_x34(z67=_, z68=0, z69=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z67: Navimesh switching point ID
    z68: Additional attributes
    z69: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z67, z68)
    DeleteNavimeshAttribute(z67, z69)
    """State 2: End state"""
    return 0

def event_m10_32_x35(z67=_, z68=0, z69=2, z70=_, z71=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z67: Navimesh switching point ID
    z68: Additional attributes
    z69: Delete attribute
    z70: Other flags
    z71: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_32_x32(z70=z70, z71=z71, z69=z69, z68=z68, z67=z67)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_32_x33(z70=z70, z71=z71)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_32_x34(z67=z67, z68=z68, z69=z69)
    """State 4: End state"""
    return 0

def event_m10_32_x36(z65=_, z66=_):
    """[Lib] [Preset] Get trophy
    z65: Acquisition trigger_other flags
    z66: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z65) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z65, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z66)
    """State 4: End state"""
    return 0

def event_m10_32_x37(z63=40, z64=104122):
    """[Lib] NPC: Death Determination: Shenzhen Pilgrim
    z63: Generator ID
    z64: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z64, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z63)
            IsChrDead(8, z63)
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
                SetEventFlag(z64, 1)
                CompareEventFlag(0, z64, 1)
                assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_32_x38(z60=10323800):
    """[Lib] [DLC] [Reproduction] Warp move between main part and DLC
    z60: Warp OBJ instance ID
    """
    """State 0,1: Warp OBJ state initialization"""
    InitializeObj(z60)
    """State 2: End state"""
    return 0

def event_m10_32_x39(z60=10323800):
    """[Lib] [DLC] [Conditions] Warp move between main part and DLC
    z60: Warp OBJ instance ID
    """
    """State 0,2: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z60, 0)
    """State 1: It became waiting to check or multi"""
    IsObjSearched(0, z60)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_32_x40(z60=10323800, z61=50370000, z62=5100000):
    """[Lib] [DLC] [Execution] Warp move between main part and DLC
    z60: Warp OBJ instance ID
    z61: Map ID
    z62: Warp point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z60, 1)
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
        assert event_m10_32_x0(z140=0, z141=0, z61=z61, z62=z62)
        """State 7: Invincible OFF"""
        SetPlayerInvincible(0)
        """State 8: Multiplayer prohibited state: OFF"""
        ProhibitMultiplayer(0)
    """State 10: End state"""
    return 0

def event_m10_32_x41(z60=10323800):
    """[Lib] [DLC] [Execution] Warp move of main part and DLC_Key guide disabled
    z60: Warp OBJ instance ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z60, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x42(z60=10323800, z61=50370000, z62=5100000):
    """[Lib] [Preset] Warp move between main part and DLC
    z60: Warp OBJ instance ID
    z61: Map ID
    z62: Warp point ID
    """
    """State 0,1: [Lib] [DLC] [Reproduction] Warp move of the main part and DLC_SubState"""
    assert event_m10_32_x38(z60=z60)
    """State 4: [Lib] [DLC] [Condition] Warp move between main part and DLC_SubState"""
    call = event_m10_32_x39(z60=z60)
    if call.Get() == 1:
        """State 3: [Lib] [DLC] [Execution] Warp move between main volume and DLC_Key guide disabled_SubState"""
        assert event_m10_32_x41(z60=z60)
    elif call.Get() == 0:
        """State 2: [Lib] [DLC] [Execution] Warp move between main part and DLC_SubState"""
        assert event_m10_32_x40(z60=z60, z61=z61, z62=z62)
    """State 5: End state"""
    return 0

def event_m10_32_x43(z45=132020043, z47=132000044):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z45: Lottery determination flag
    z47: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z47) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z45) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_32_x44(z46=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z46: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z46, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_32_x45(z45=132020043, z48=2, z49=20):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z45: Lottery determination flag
    z48: Number of appearance judgment points
    z49: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z45, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z48)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z49, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_32_x46(z45=132020043, z46=14, z47=132000044, z48=2, z49=20):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z45: Lottery determination flag
    z46: Random number comparison value
    z47: Defeat flag
    z48: Number of appearance judgment points
    z49: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m10_32_x43(z45=z45, z47=z47)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_32_x44(z46=z46)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_32_x45(z45=z45, z48=z48, z49=z49)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_32_x55(z45=z45, z49=z49)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_32_x47(val1=_, z57=20):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z57: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z57) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_32_x48(z53=_, z54=0, z55=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z53: Appearance judgment point ID
    z54: Minimum appearance time
    z55: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z53, z53, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z54, 3, z55)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_32_x49(z56=956, z58=_, z59=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z56: Generator ID
    z58: Appearance start point ID
    z59: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z56, z58, z59)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z56)
    """State 4: Finish"""
    return 0

def event_m10_32_x50(z50=132000044):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z50: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z50) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_32_x51(z53=_, z54=0, z55=5, z56=956, val1=_, z57=20, z58=_, z59=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z53: Intrusion detection point ID
    z54: Minimum appearance time
    z55: Maximum time to appear
    z56: Generator ID
    val1: Appearance judgment number
    z57: Lottery result point variable
    z58: Appearance start point ID
    z59: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_32_x47(val1=val1, z57=z57)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_32_x48(z53=z53, z54=z54, z55=z55)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_32_x49(z56=z56, z58=z58, z59=z59)
    """State 4: Finish"""
    return 0

def event_m10_32_x52(z51=956, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z51: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z51)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_32_x53(z50=132000044, z52=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z50: Defeat flag
    z52: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z50, 1)
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
                    SetEventFlag(z52, 1)
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

def event_m10_32_x54(z50=132000044, z51=956, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z50: Defeat flag
    z51: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_32_x50(z50=z50)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_32_x52(z51=z51, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_32_x53(z50=z50, z52=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_32_x53(z50=z50, z52=102755)
    """State 5: End state"""
    return 0

def event_m10_32_x55(z45=132020043, z49=20):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z45: Lottery determination flag
    z49: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z45, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z49, 0)
    """State 3: End state"""
    return 0

def event_m10_32_x56(z42=132000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z42: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z42) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_32_x57(z43=824):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z43: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z43, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x58(z44=132020082):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z44: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z44, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x59(z42=132000081, z43=824, z44=132020082):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z42: Boss destruction flag
    z43: Boss generator ID
    z44: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_32_x56(z42=z42)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_32_x57(z43=z43)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_32_x58(z44=z44)
    """State 4: End state"""
    return 0

def event_m10_32_x60():
    """[Reproduction] Reproducing pitfalls"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x61(z39=_):
    """[Conditions] Waiting for pitfalls
    z39: Pitfall OBJ instance ID
    """
    """State 0,1: OBJ collapse waiting"""
    CompareObjState(0, z39, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x62(z40=_, z41=0):
    """[Execution] Pitfall navigator mesh switching
    z40: Navimesh switching area ID
    z41: Pitfall OBJ instance ID
    """
    """State 0,1: Navi mesh switching"""
    AddNavimeshAttribute(z40, 2)
    """State 2: End state"""
    return 0

def event_m10_32_x63(z39=_, z40=_):
    """[Preset] Pitfall
    z39: Pitfall OBJ instance ID
    z40: Navimesh switching area ID
    """
    """State 0,1: [Reproduction] Pitfall state reproduction_SubState"""
    assert event_m10_32_x60()
    """State 2: [Condition] Pitfall collapse waiting_SubState"""
    assert event_m10_32_x61(z39=z39)
    """State 3: [Execution] Pitfall navigator mesh switching_SubState"""
    assert event_m10_32_x62(z40=z40, z41=0)
    """State 4: End state"""
    return 0

def event_m10_32_x64(z36=10321250, z37=10326200, z38=72):
    """[Preset] Stone pillar of treasure corpse
    z36: Stone pillar instance ID
    z37: Instance ID of treasure corpse
    z38: Falling state ID
    """
    """State 0,1: Disable OBJ sync"""
    SetObjSync(z37, 0)
    """State 2: [Reproduction] Treasure corpse branch_sky_SubState"""
    assert event_m10_32_x65()
    """State 3: [Condition] Treasure corpse branch_SubState"""
    assert event_m10_32_x66(z36=z36)
    """State 4: [Execution] Treasure corpse branch _SubState"""
    assert event_m10_32_x67(z37=z37, z38=z38)
    """State 5: End state"""
    return 0

def event_m10_32_x65():
    """[Reproduction] Stone pillar of treasure corpse _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x66(z36=10321250):
    """[Condition] Stone pillar of treasure corpse
    z36: Branch instance ID
    """
    """State 0,1: Wait for branch destruction"""
    IsObjBroken(0, z36, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x67(z37=10326200, z38=72):
    """[Execution] Stone pillar of treasure corpse
    z37: Instance ID of treasure corpse
    z38: Falling state ID
    """
    """State 0,1: OBJ state transition: treasure corpse"""
    ChangeObjState(z37, z38)
    """State 2: End state"""
    return 0

def event_m10_32_x68(z14=10320405, z15=900000, z16=100420, z17=10320406, z18=900010):
    """[Preset] Special door to the Royal Castle
    z14: Instance ID of door table OBJ
    z15: Point ID for table navigation mesh change
    z16: Special door opening flag
    z17: Instance ID of OBJ behind the door
    z18: Point ID for changing back Navi mesh
    """
    """State 0,3: [Reproduction] White door to the Royal Castle_SubState"""
    call = event_m10_32_x69(z14=z14, z17=z17)
    if call.Get() == 0:
        """State 4: [Condition] White door to the Royal Castle_SubState"""
        call = event_m10_32_x70(z14=z14)
        if call.Get() == 0:
            """State 5: [Execution] White door to the Royal Castle_Defeat specified boss_SubState"""
            assert event_m10_32_x71(z14=z14, z17=z17)
        elif call.Get() == 2:
            """State 6: [Execution] White door to the royal castle _ Acquire Seoul above a certain level _ SubState"""
            assert event_m10_32_x72(z14=z14, z17=z17)
        elif call.Get() == 1:
            """State 7: [Execution] White door to the Royal Castle_No access_SubState"""
            assert event_m10_32_x73(z14=z14)
            """State 10: Door not open"""
            return 1
    elif call.Get() == 2:
        """State 8: [Execution] Special door to the Royal Castle_Relief_SubState"""
        assert event_m10_32_x97(z14=z14, z17=z17)
    elif call.Get() == 1:
        pass
    """State 1: Navigation mesh change"""
    DeleteNavimeshAttribute(z15, 2)
    DeleteNavimeshAttribute(z18, 2)
    """State 2: Flag ON Special door opened"""
    SetEventFlag(z16, 1)
    """State 9: Door release"""
    return 0

def event_m10_32_x69(z14=10320405, z17=10320406):
    """[Reproduction] Special door to the Royal Castle
    z14: Instance ID of door table OBJ
    z17: Instance ID of OBJ behind the door
    """
    """State 0,2: Judgment status of doors"""
    if CompareObjStateId(z14, 10, 0):
        pass
    else:
        Goto('L0')
    """State 1: Hide key guide"""
    DisableObjKeyGuide(z14, 1)
    DisableObjKeyGuide(z17, 1)
    """State 4: Not passed"""
    return 0
    """State 3: Is the back of the door closed?"""
    Label('L0')
    if CompareObjStateId(z17, 10, 0):
        """State 6: Open the door"""
        return 2
    else:
        """State 5: Passed"""
        return 1

def event_m10_32_x70(z14=10320405):
    """[Conditions] Special door to the Royal Castle
    z14: Shirado OBJ instance ID
    """
    """State 0,2: Judging distance from players"""
    CompareObjPlayerDistance(0, z14, 3, 5)
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

def event_m10_32_x71(z14=10320405, z17=10320406):
    """[Execution] Special door to the royal castle
    z14: Instance ID of door table OBJ
    z17: Instance ID of OBJ behind the door
    """
    """State 0,1: Front door release"""
    ChangeObjState(z14, 74)
    """State 2: Waiting for front door"""
    CompareObjState(0, z14, 74, 0)
    assert ConditionGroup(0)
    """State 3: Open the back door"""
    ChangeObjState(z17, 74)
    """State 4: End state"""
    return 0

def event_m10_32_x72(z14=10320405, z17=10320406):
    """[Execution] Special door to Wangcheng
    z14: Instance ID of door table OBJ
    z17: Instance ID of OBJ behind the door
    """
    """State 0,1: Key guide display"""
    DisableObjKeyGuide(z14, 0)
    DisableObjKeyGuide(z17, 0)
    """State 2: Did you open the door?"""
    CompareObjState(0, z14, 74, 0)
    assert ConditionGroup(0)
    """State 3: Open the back door"""
    ChangeObjState(z17, 74)
    """State 4: End state"""
    return 0

def event_m10_32_x73(z14=10320405):
    """[Execution] Special door to the Royal Castle
    z14: Shirado OBJ instance ID
    """
    """State 0,1: Message display"""
    # action:2002:"Seek mightier souls"
    DisplayEventMessage(2002, 0, 0, 0)
    """State 2: Did you leave the white door? or cumulative soul value exceeds a certain value?"""
    CompareObjPlayerDistance(0, z14, 10, 3)
    CompareCumulativeSouls(0, GetCommonEventParamInt(14) * ClampInt(GetGameCycle(), 1, 8), 3, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_32_x74(z33=_, z34=_, z35=_):
    """[Reproduction] Generation management of phantom enemies
    z33: Area variable ID
    z34: Generation stop flag
    z35: Initialization completion flag
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
    if GetEventFlag(z35) != 0:
        pass
    else:
        """State 1: Generation stop flag judgment"""
        if GetEventFlag(z34) != 0:
            pass
        else:
            """State 2: Reset area variable"""
            SetAreaVariable(z33, 0)
            """State 4: Area variable initialization processing completion flag: ON"""
            SetEventFlag(z35, 1)
    """State 6: Host: Condition"""
    return 0

def event_m10_32_x75(z32=_, z33=_):
    """[Condition] Generation management of phantom enemies
    z32: Generator ID
    z33: Area variable ID
    """
    """State 0,1: Phantom enemy death waiting or generation number is 2 or more"""
    IsChrDead(0, z32)
    CompareEventFlagValue(1, 1, z33, 2, 3)
    if ConditionGroup(1):
        """State 3: Number of generations is 2 or more"""
        return 1
    elif ConditionGroup(0):
        """State 2: death"""
        return 0

def event_m10_32_x76(z33=_, z32=_):
    """[Execution] Generation management of phantom enemies_Add variable
    z33: Area variable ID
    z32: Generator ID
    """
    """State 0,1: Number of generated area variable addition"""
    AddAreaVariable(z33, 1)
    """State 2: Waiting for generation"""
    assert GeneratorOperationOngoing(z32) != 1
    """State 3: Rerun"""
    return 0

def event_m10_32_x77(z32=_, z33=_, z34=_, z35=_):
    """[Preset] Generation management of phantom enemies
    z32: Generator ID
    z33: Area variable ID
    z34: Generation stop flag
    z35: Initialization completion flag
    """
    """State 0,1: [Reproduction] Generation management of phantom enemies_SubState"""
    call = event_m10_32_x74(z33=z33, z34=z34, z35=z35)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Phantom enemy generation management_SubState"""
        call = event_m10_32_x75(z32=z32, z33=z33)
        if call.Get() == 0:
            """State 3: [Execution] Generation management of phantom enemies_Variable addition_SubState"""
            assert event_m10_32_x76(z33=z33, z32=z32)
            """State 5: Rerun"""
            return 0
        elif call.Get() == 1:
            """State 2: [Execute] Generation management of phantom enemies_flag_SubState"""
            assert event_m10_32_x78(z34=z34)
    """State 6: Finish"""
    return 1

def event_m10_32_x78(z34=_):
    """[Execute] Phantom enemy generation management flag
    z34: Generation stop flag
    """
    """State 0,1: Stop flag ON"""
    SetEventFlag(z34, 1)
    """State 2: Finish"""
    return 0

def event_m10_32_x79(z23=132000081, z24=101, z25=1032000, z26=132020080, z27=5, mode1=0):
    """[Preset] Manscorpion Battle _Start
    z23: Boss destruction flag
    z24: Sound ID
    z25: Boss Battle ID
    z26: Other flags for logic
    z27: Wait time
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Manscorpion Battle _Start_SubState"""
    call = event_m10_32_x80(z23=z23)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Conditions] Manscorpion Battle_Start_SubState"""
        assert event_m10_32_x81(z30=600000, z31=600000)
        """State 3: [Execution] Manscorpion Battle _Start_SubState"""
        assert event_m10_32_x82(z25=z25, z26=z26)
        """State 7: [Reproduction] HP display and BGM playback_empty_SubState"""
        assert event_m10_32_x83()
        """State 9: [Condition] HP display and BGM playback_SubState"""
        assert event_m10_32_x84(z28=824, z29=2)
        """State 8: [Execution] HP display and BGM playback_SubState"""
        assert event_m10_32_x85(z24=z24, z27=z27, z25=z25)
        """State 2: [Reproduction] Manscorpion Battle_End_Sky_SubState"""
        assert event_m10_32_x86()
        """State 6: [Conditions] Manscorpion Battle_End Judgment_SubState"""
        assert event_m10_32_x87(z25=z25)
        """State 4: [Execution] Manscorpion Battle _End_SubState"""
        assert event_m10_32_x88(z24=z24, z25=z25, z26=z26, mode1=mode1)
    """State 10: End state"""
    return 0

def event_m10_32_x80(z23=132000081):
    """[Reproduction] Manscorpion Battle _Start
    z23: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z23) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_32_x81(z30=600000, z31=600000):
    """[Condition] Manscorpion Battle _Start
    z30: Start point ID
    z31: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z30, z31, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z30, z31, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x82(z25=1032000, z26=132020080):
    """[Execution] Manscorpion Battle _Start
    z25: Boss Battle ID
    z26: Logic flag
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z25)
    """State 2: Logic flag ON"""
    SetEventFlag(z26, 1)
    """State 3: End state"""
    return 0

def event_m10_32_x83():
    """[Reproduction] HP display and BGM playback_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x84(z28=824, z29=2):
    """[Condition] HP display and BGM playback
    z28: Boss generator ID
    z29: Activation state ID
    """
    """State 0,1: Did the boss jump out of the sand?"""
    CompareChrEzStateValue(0, z28, 7, 1, 0)
    IsEventBossKill(0, z28, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x85(z24=101, z27=5, z25=1032000):
    """[Execution] HP display and BGM playback
    z24: Sound ID
    z27: Wait time until display
    z25: Boss Battle ID
    """
    """State 0,3: Wait until BGM playback and HP display"""
    CompareStateTime(0, z27, 2, z27)
    IsEventBossKill(1, z25, 0, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 1: BGM battle BGM playback"""
        PlaySoundAtPoint(z24)
    """State 2: Boss HP gauge display"""
    DisplayBossHpBar(0, 1)
    """State 4: End state"""
    return 0

def event_m10_32_x86():
    """[Reproduction] Manscorpion Battle _End_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x87(z25=1032000):
    """[Condition] Manscorpion Battle _ End Judgment
    z25: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z25, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_32_x88(z24=101, z25=1032000, z26=132020080, mode1=0):
    """[Execution] Manscorpion Battle _End
    z24: Sound ID
    z25: Boss Battle ID
    z26: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z26, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z25)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z24)
    """State 5: End state"""
    return 0

def event_m10_32_x89(z20=10320400, z21=105310, z22=132000055):
    """[Preset] King's door
    z20: Instance ID of king's door OBJ
    z21: King door opening and closing flag
    z22: Opening flag
    """
    """State 0,1: [Reproduction] King's door _ the forest of shadows_SubState"""
    call = event_m10_32_x90(z20=z20, z21=z21)
    if call.Get() == 1:
        """State 2: [Condition] King's door_SubState"""
        call = event_m10_32_x12(z20=z20, z22=z22)
        if call.Get() == 1:
            """State 3: [Execution] King's Door _ The Shadow Shadow Forest _ Open _ SubState"""
            assert event_m10_32_x91(z20=z20, z21=z21, z22=z22)
        elif call.Get() == 0:
            """State 4: [Execution] King's door_Do not open_SubState"""
            assert event_m10_32_x13(z20=z20)
    elif call.Get() == 2:
        """State 5: [Lib] [Condition] King's door_Close_SubState"""
        assert event_m10_32_x31(z20=z20)
        """State 6: [Execution] King's Door _ The Shadow Shadow Forest _Close_SubState"""
        assert event_m10_32_x92(z20=z20, z21=z21)
    elif call.Get() == 0:
        """State 8: Finish"""
        return 1
    """State 7: Rerun"""
    return 0

def event_m10_32_x90(z20=10320400, z21=105310):
    """[Reproduction] King's door
    z20: Instance ID of king's door OBJ
    z21: King door opening and closing flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 2: Is the door closed or closed?"""
    if CompareObjStateId(z20, 10, 0):
        """State 3: Waiting for the door to close"""
        Label('L0')
        assert CompareObjStateId(z20, 10, 0)
        """State 6: King door open / close flag: OFF"""
        SetEventFlag(z21, 0)
        """State 8: Closed"""
        return 1
    elif CompareObjStateId(z20, 80, 0):
        Goto('L0')
    else:
        """State 4: Waiting for the door to open"""
        assert CompareObjStateId(z20, 30, 0)
        """State 5: King's door open / close flag: ON"""
        SetEventFlag(z21, 1)
        """State 9: is open"""
        return 2
    """State 7: Guest: Exit"""
    Label('L1')
    return 0

def event_m10_32_x91(z20=10320400, z21=105310, z22=132000055):
    """[Execution] King's Door _ Open Shadow Forest _ Open
    z20: Instance ID of king's door OBJ
    z21: King door opening and closing flag
    z22: Opening flag
    """
    """State 0,1: Opening flag ON King's door opens"""
    SetEventFlag(z22, 1)
    ChangeObjState(z20, 70)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z20, 30, 0)
    assert ConditionGroup(0)
    """State 3: King's door open / close flag: ON"""
    SetEventFlag(z21, 1)
    """State 4: End state"""
    return 0

def event_m10_32_x92(z20=10320400, z21=105310):
    """[Execution] The door of the king
    z20: Instance ID of king's door OBJ
    z21: King door opening and closing flag
    """
    """State 0,1: The king's door closes"""
    ChangeObjState(z20, 80)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z20, 10, 0)
    assert ConditionGroup(0)
    """State 3: King door open / close flag: OFF"""
    SetEventFlag(z21, 0)
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

def event_m10_32_x94(z19=2041):
    """[Condition] Earn items by destroying petrified characters
    z19: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z19)
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

def event_m10_32_x96(lot1=60009000, z19=2041):
    """[Preset] Earn items by destroying petrified characters
    lot1: Item lottery ID
    z19: Generator ID
    """
    """State 0,1: [Reproduction] Item acquisition by destroying petrified characters_SubState"""
    call = event_m10_32_x93()
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Acquire items by destroying petrified characters_SubState"""
        assert event_m10_32_x94(z19=z19)
        """State 2: [Execution] Item acquisition by destroying petrified characters_SubState"""
        assert event_m10_32_x95(lot1=lot1)
    """State 4: End state"""
    return 0

def event_m10_32_x97(z14=10320405, z17=10320406):
    """[Execution] Special door to the royal castle for relief
    z14: Instance ID of door table OBJ
    z17: Instance ID of OBJ behind the door
    """
    """State 0,1: Key guide display"""
    DisableObjKeyGuide(z14, 0)
    DisableObjKeyGuide(z17, 0)
    """State 2: Open the front and back doors"""
    ChangeObjState(z14, 74)
    ChangeObjState(z17, 74)
    """State 3: End state"""
    return 0

def event_m10_32_x98(z13=_, action1=_):
    """[DLC] [Preset] Stone monument displayed as text
    z13: Stele OBJ instance ID
    action1: Text ID
    """
    """State 0,1: [DLC] [Reproduction] Stone monument_SubState displayed in text"""
    assert event_m10_32_x99()
    """State 3: [DLC] [Condition] Stone monument_SubState displayed in text"""
    assert event_m10_32_x101(z13=z13)
    """State 2: [DLC] [Execution] Stone monument_SubState displayed in text"""
    assert event_m10_32_x100(action1=action1, z13=z13)
    """State 4: End state"""
    return 0

def event_m10_32_x99():
    """[DLC] [Reproduction] Stone monument displayed in text"""
    """State 0,1: End state"""
    return 0

def event_m10_32_x100(action1=_, z13=_):
    """[DLC] [execution] Stone monument displayed as text
    action1: Text ID
    z13: Stele OBJ instance ID
    """
    """State 0,2: Disable key guide"""
    DisableObjKeyGuide(z13, 1)
    """State 1: Text display"""
    DisplayEventMessage(action1, 0, 0, 0)
    assert (GetStateTime() > 1.5) != 0
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z13, 0)
    """State 4: End state"""
    return 0

def event_m10_32_x101(z13=_):
    """[DLC] [Condition] Stone monument displayed in text
    z13: Stele OBJ instance ID
    """
    """State 0,1: Wait for decision to check"""
    IsObjSearched(0, z13)
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

def event_m10_32_x106(z9=_):
    """[DC] [Reproduction] Illusion enemy of ruins _ Defeat count
    z9: Judgment flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Have you counted it before saving?"""
        if GetEventFlag(z9) != 0:
            pass
        else:
            """State 3: Defeat determination"""
            return 0
    """State 4: Do nothing: Quit"""
    return 1

def event_m10_32_x107(z10=_, z11=4, z12=8):
    """[DC] [Condition] Illusionary enemies of ruins _ Defeat count
    z10: Generator ID
    z11: Defeat count variable
    z12: Necessary number of destruction
    """
    """State 0,1: Character destruction waiting or upper limit number judgment or destruction number judgment"""
    IsChrDead(0, z10)
    IsChrMaxRespawnCount(1, z10, 1, 0)
    CompareEventFlagValue(1, 0, 4, z12, 3)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Variable addition"""
        return 0

def event_m10_32_x108(z11=4, z9=_):
    """[DC] [Execution] Illusionary enemy of ruins _ Defeat count
    z11: Defeat count variable
    z9: Judgment flag
    """
    """State 0,1: Defeat count + 1 judgment flag ON"""
    SetEventFlag(z9, 1)
    AddGlobalVariable(z11, 1)
    """State 2: End state"""
    return 0

def event_m10_32_x109(z9=_, z10=_, z11=4, z12=8):
    """[DC] [Preset] Illusionary enemies of ruins _ Defeat count
    z9: Judgment flag
    z10: Generator ID
    z11: Defeat count variable
    z12: Necessary number of destruction
    """
    """State 0,1: [DC] [Reproduction] Illusionary enemy of ruins _ Defeat count _ SubState"""
    call = event_m10_32_x106(z9=z9)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Phantom enemies of ruins_Countdown count_SubState"""
        call = event_m10_32_x107(z10=z10, z11=z11, z12=z12)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [DC] [Execution] Illusionary enemy of ruins _ Defeat count _ SubState"""
            assert event_m10_32_x108(z11=z11, z9=z9)
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
    event_m10_32_x1(z136=104000, z137=10324200, z138=257, z139=3070)

def event_m10_32_111013():
    """OBJ: Durahan: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:3070:Head of Vengarl
    event_m10_32_x8(z120=132010170, z121=132020171, z122=104000, z123=10324200, z124=111012, npc1=3070)

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

def event_m10_32_111182():
    """OBJ: Shenzhen Pilgrim: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z136=104122, z137=10324000, z138=41, z139=7250)

def event_m10_32_111183():
    """OBJ: Shenzhen Pilgrims: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7250:Darkdiver Grandahl
    event_m10_32_x8(z120=132010100, z121=132020101, z122=104120, z123=10324000, z124=111182, npc1=7250)

def event_m10_32_111184():
    """OBJ: Shenzhen Pilgrim: Death Determination"""
    """State 0,1: [Lib] NPC: Death Judgment: Shenzhen Pilgrim_SubState"""
    event_m10_32_x37(z63=40, z64=104122)

def event_m10_32_111185():
    """OBJ: Shenzhen Pilgrim: Appearance Judgment"""
    """State 0,1: [Lib] NPC: Shenzhen Pilgrim: Appearance Judgment_SubState"""
    event_m10_32_x25(z75=102317, z76=102324, z77=102331, z78=102332, z79=102315, z80=102316, z81=103622)

def event_m10_32_111232():
    """OBJ: Wandering Warrior: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z136=104152, z137=10324300, z138=56, z139=7420)

def event_m10_32_111233():
    """OBJ: Wandering Warrior: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7420:Creighton the Wanderer
    event_m10_32_x8(z120=132010120, z121=132020121, z122=104150, z123=10324300, z124=111232, npc1=7420)

def event_m10_32_111234():
    """OBJ: Wandering Warrior: Death Judgment"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_32_x10(z114=55, z115=104152)

def event_m10_32_111235():
    """OBJ: Wandering Warrior: Appearance Judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_32_x11(z109=104150, z110=102405, z111=102406, z112=132010127, z113=103651)

def event_m10_32_111452():
    """OBJ: Upper weapon shop: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z136=104361, z137=10324100, z138=266, z139=7760)

def event_m10_32_111453():
    """OBJ: Upper weapon shop: Key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7760:Weaponsmith Ornifex
    event_m10_32_x8(z120=132010190, z121=132020191, z122=104360, z123=10324100, z124=111452, npc1=7760)

def event_m10_32_111454():
    """OBJ: Upper weapon shop: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_32_x10(z114=265, z115=104361)

def event_m10_32_111522():
    """OBJ: Manscorpion ♂: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_32_x1(z136=104430, z137=10324600, z138=326, z139=5020)

def event_m10_32_111523():
    """OBJ: Manscorpion ♂: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:5020:Manscorpion Tark
    event_m10_32_x8(z120=132010150, z121=132020151, z122=104430, z123=10324600, z124=111522, npc1=5020)

def event_m10_32_111524():
    """OBJ: Manscorpion ♂: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_32_x19(z90=102980, z91=626, z92=104430, z93=60, z94=103930, z95=-1)

def event_m10_32_118100():
    """Multi-use NPC: White Spirit Test 1: White Phantom Sign Display"""
    """State 0,1: Flag judgment"""
    CompareEventFlag(0, 132000075, 1)
    assert ConditionGroup(0)
    """State 2: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_32_x26(z74=627)

def event_m10_32_120080():
    """Trophy: Deep Darkness Pledge"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_32_x36(z65=132020109, z66=26)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_32_120160():
    """Trophy: Thinking neck"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_32_x36(z65=132020177, z66=36)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_32_3000000():
    """[DLC] Warp move to ice map"""
    """State 0,2: [Lib] [Preset] Warp move of main part and DLC_SubState"""
    assert event_m10_32_x42(z60=10323800, z61=50370000, z62=5100000)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_32_3001000():
    """[DLC] Stone monument displayed in text_1"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5400:"Forbidden is the path\nto the ancient king's domain"
    assert event_m10_32_x98(z13=10323810, action1=5400)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_32_3001010():
    """[DLC] Stone monument displayed in text_2"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5420:"With water dry, and path amiss,\nwoeful temptation is dismissed"
    assert event_m10_32_x98(z13=10323811, action1=5420)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_32_3001020():
    """[DLC] Stone monument displayed in text_3"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5430:"Trespassers will face\nadversity befitting a monarch"
    assert event_m10_32_x98(z13=10323812, action1=5430)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_32_3001030():
    """[DLC] Stone monument displayed as text_4"""
    """State 0,2: [DLC] [Preset] Stone monument_SubState displayed in text"""
    # action:5610:"Eleum Loyce, land of the Ivory King, lies cold as death,\nnary a hint of warmth remaining"
    assert event_m10_32_x98(z13=10323813, action1=5610)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_32_4000000():
    """[DC] Lion Warrior _ Petrification Stop 4_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z101=2210, z102=0, z103=15, z104=132000016, z105=0, z106=1600, z107=3, z108=4000010)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4000010():
    """[DC] Lion Warrior _ Petrification Stop 4_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z82=2210, z83=0, z84=132000016, z85=0, z86=0, z87=4000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4000020():
    """[DC] Lion Warrior _ Petrification Stop 4_ Navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z67=6000020, z68=0, z69=2, z70=132000016, z71=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4001000():
    """[DC] Lion Warrior _ Petrification Stop 5_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z101=2103, z102=0, z103=15, z104=132000017, z105=0, z106=1600, z107=3, z108=4001010)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4001010():
    """[DC] Lion Warrior _ Petrification Stop 5_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z82=2103, z83=0, z84=132000017, z85=0, z86=0, z87=4001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4001020():
    """[DC] Lion Warrior _ Petrochemical stop 5_ Navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z67=6001020, z68=0, z69=2, z70=132000017, z71=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4002000():
    """[DC] Lion Warrior _ Petrification Stop 6_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_32_x14(z101=2500, z102=0, z103=15, z104=132000018, z105=0, z106=1600, z107=3, z108=4002010)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4002010():
    """[DC] Lion Warrior _ Petrification Stop 6_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_32_x24(z82=2500, z83=0, z84=132000018, z85=0, z86=0, z87=4002000)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4002020():
    """[DC] Lion Warrior _ Petrification Stop 6_ Navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_32_x35(z67=6002020, z68=0, z69=2, z70=132000018, z71=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4003000():
    """[DC] Transparency and materialization of Zako_Winter Deep 1"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=1300, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003010():
    """[DC] Transparency and materialization of Zako_Winter 2"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=1310, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003100():
    """[DC] Zako's transparency and materialization_Fog Forest 1"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2000, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003110():
    """[DC] Transparency and materialization of Zako_Fog Forest 2"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2001, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003120():
    """[DC] Transparency and materialization of Zako_Fog Forest 3"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2002, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003130():
    """[DC] Transparency and materialization of Zako_Fog Forest 4"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2003, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003140():
    """[DC] Zako's transparency and materialization_Fog Forest 5"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2006, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003150():
    """[DC] Transparency and materialization of Zako_Fog Forest 6"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2007, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003160():
    """[DC] Transparency and materialization of Zako_Fog Forest 7"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2009, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003200():
    """[DC] Transparency and materialization of Zako_Ruins 1"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2400, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003210():
    """[DC] Transparency and materialization of Zako_Ruins 2"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2410, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003220():
    """[DC] Transparency and materialization of Zako_Ruins 3"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2420, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003230():
    """[DC] Transparency and materialization of Zako _ Ruins 4"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2430, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003240():
    """[DC] Transparency and materialization of Zako _ Ruins 5"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2421, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003250():
    """[DC] Transparency and materialization of Zako_Ruins 6"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2440, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003260():
    """[DC] Transparency and materialization of Zako _ Ruins 7"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2450, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003270():
    """[DC] Transparency and materialization of Zako_Ruins 8"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=2460, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003300():
    """[DC] Zako's transparency and materialization"""
    """State 0,3: [DC] [Preset] Zako's transparency and materialization_SubState"""
    call = event_m10_32_x105(z1=1250, z2=98382000, z3=132000051)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_32_4003900():
    """[DC] Determination of possession of Miko's eyes"""
    """State 0,2: [DC] [Preset] Judgment of possession of a shrine maiden_SubState"""
    assert event_m10_32_x117(z4=132000051)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004000():
    """[DC] Illusionary enemy of ruins _ Defeat count 1"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020056, z10=2400, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004010():
    """[DC] Illusionary enemy of ruins _ Defeat count 2"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020057, z10=2410, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004020():
    """[DC] Illusionary enemy of ruins _ Defeat count 3"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020058, z10=2420, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004030():
    """[DC] Illusionary enemy of ruins _ Defeat count 4"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020059, z10=2430, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004040():
    """[DC] Illusionary enemy of ruins _ Defeat count 5"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020060, z10=2421, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004050():
    """[DC] Illusionary enemy of ruins _ Defeat count 6"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020061, z10=2440, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004060():
    """[DC] Illusionary enemy of ruins _ Defeat count 7"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020062, z10=2450, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4004070():
    """[DC] Illusionary enemy of ruins _ Defeat count 8"""
    """State 0,2: [DC] [Preset] Illusionary enemy of ruins _ Defeat count _SubState"""
    assert event_m10_32_x109(z9=132020063, z10=2460, z11=4, z12=8)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4005000():
    """[DC] White spirit sign appears by destroying phantom enemies in ruins"""
    """State 0,2: [DC] [Preset] Defeat the phantom enemy of the ruins."""
    assert event_m10_32_x113(z6=4, z7=8, z8=132000075)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4011000():
    """[DC] Wanderer B_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m10_32_x46(z45=132020043, z46=14, z47=132000044, z48=2, z49=20)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_32_x51(z53=80000000, z54=0, z55=5, z56=956, val1=1, z57=20, z58=80000001, z59=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_32_x51(z53=80000100, z54=0, z55=5, z56=956, val1=2, z57=20, z58=80000101, z59=80000199)
        """State 2: Start flag ON"""
        SetEventFlag(132020045, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4011010():
    """[DC] Wanderer B_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_32_x54(z50=132000044, z51=956, mode2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_32_4031000():
    """[DC] NPC White Spirit_Gesture Management_Manscorpion♀"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_32_x59(z42=132000081, z43=824, z44=132020082)
    """State 1: Finish"""
    EndMachine()

