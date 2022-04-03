# -*- coding: utf-8 -*-
def event_m10_10_1000():
    """King's door"""
    """State 0,2: [Lib] [Preset] King's Door_SubState"""
    assert event_m10_10_x40(z81=10100417, z82=100000, z83=110000079)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_10_2000():
    """Interlocking elevator_initialization"""
    """State 0,3: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m10_10_x18(z142=10101050, z143=12, flag21=110020060, z144=30)
    """State 2: [Lib] [Preset] Elevator_Initialization_2_SubState"""
    assert event_m10_10_x18(z142=10101060, z143=14, flag21=110020061, z144=40)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_2010():
    """Interlocking elevator_operation"""
    """State 0,2: [Lib] [Preset] Interlocking Elevator_SubState"""
    assert (event_m10_10_x26(z84=10101050, z85=10101060, z86=2000, z87=201000, z88=201001, z89=201002,
            z90=201003, z91=15))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_10_3000():
    """Navimesh change of the wall that breaks in the flame barrel"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101300, z119=20, z120=300000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_10_x29(z125=10101600)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_10_x39(z123=10101600, val2=10100000, z124=0.6, val3=1.5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101610, z119=20, z120=402000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_5000():
    """Key door that opens with "key of fire" """
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z152=1005, z153=1105, z154=50810000, z155=110000070)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_5100():
    """The lock door that opens with the key of the royal soldier"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z152=1005, z153=1105, z154=50600000, z155=110000072)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_5200():
    """The key door that opens with the “Welcome Key” (can be broken)"""
    """State 0,2: [Preset] Key door opened with "Welcome Key" (breakable) _SubState"""
    assert event_m10_10_x102(z52=10100415, z53=520000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_5210():
    """The key door that opens with the key of the Royal Soldier"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z152=1005, z153=1105, z154=50600000, z155=110000076)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_5211():
    """The key door that opens with the key of the Royal Soldier"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z152=1005, z153=1105, z154=50600000, z155=110000078)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6000():
    """Boss: Vegrant _ Battle"""
    """State 0,2: Is the poly drama replay event over?"""
    assert EventEnded(6010) != 0
    """State 3: [Preset] Boss: Vegrant Battle_Start_SubState"""
    assert (event_m10_10_x146(flag8=110000086, z23=600000, z24=600000, z25=102, z26=1010000, z27=110020085,
            mode1=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6010():
    """Boss: Vegrant_Poly Theater"""
    """State 0,2: [Preset] Vegrant_Poly Play_SubState"""
    assert event_m10_10_x139(z28=101030, flag9=110000087, z29=601000, z30=1, z31=10100610, flag10=110000086)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6020():
    """Boss: Vegrant _ initial placement change"""
    """State 0,2: [Preset] Vagrant_Initial layout change_SubState"""
    assert event_m10_10_x129(z34=853, z35=602000, z36=2, z37=110000087)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6050():
    """Barista 1 destroyed by Vegrant attack"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101450, z119=20, z120=605000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6060():
    """Barista 2 destroyed by Vegrant attack"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101456, z119=20, z120=606000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6500():
    """Boss: New Giant Senior Soldier_Deceased_Battle"""
    """State 0,2: Is the poly drama replay event over?"""
    assert EventEnded(6510) != 0
    """State 3: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_10_x8(flag22=110000081, z145=650000, z146=650000, z147=101, z148=1010010, z149=110020080,
            mode4=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6510():
    """Boss: New Giant Senior Soldier_Deceased_Poly Drama"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m10_10_x22(z137=10100600, z138=101020, flag20=110000082, z139=651000, z140=1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_6520():
    """Boss: New Giant Senior Soldier"""
    """State 0,2: [Preset] New Giant Senior Soldier _ Change initial placement_SubState"""
    assert event_m10_10_x147(z20=110000082, z21=857, z22=652000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_7000():
    """Vegrant hawk taxi"""
    """State 0,2: [Preset] Inter-map warp_SubState by checking OBJ"""
    assert event_m10_10_x90(z60=10101500, z61=101010, z62=101620, z63=10160000, z64=100000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_8000():
    """One-way door that opens the enemy when attacked _ One-way door control"""
    """State 0,2: [Lib] Area specified door unlocked_SubState"""
    assert event_m10_10_x0(z165=0, z166=800000, z167=10020101)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_8010():
    """Enemy opens when attacking One-way door _ Enemy door opening control"""
    """State 0,2: [Preset] Enemy door opening control_SubState"""
    assert event_m10_10_x110(z46=110010042, z47=10100413)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_9000():
    """Giant nut"""
    """State 0,2: [Preset] Giant Tree Fruit_System Version_SubState"""
    assert event_m10_10_x176(flag3=106200, z5=10101120)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_10_9010():
    """Giant tree nut drawing process"""
    """State 0,2: [Preset] Giant tree nut drawing process_SubState"""
    assert event_m10_10_x122(flag7=106200, z19=10101120)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_10_9020():
    """Giant Tree Fruit_Message"""
    """State 0,2: [Preset] Giant Tree Fruit_Message_SubState"""
    assert event_m10_10_x170(z4=10101120, flag2=106200)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_10_10000():
    """Navi-mesh attribute change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101070, z119=20, z120=1000000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_10010():
    """Navi-mesh attribute change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101071, z119=20, z120=1001000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_10020():
    """Navi-mesh attribute change of inner wall of fracture wall"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101075, z119=20, z120=1002000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_11000():
    """Switch that closes the door"""
    """State 0,2: [Preset] Door close switch _SubState"""
    assert event_m10_10_x106(flag13=102443, z48=1100000, z49=1100001, z50=10101160, z51=1100002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_12000():
    """Oiwa Gorokuro"""
    """State 0,2: [Preset] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x114(z43=1200000, z44=1200000, z45=10101700)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_13000():
    """Waterway one-way door"""
    """State 0,2: [Lib] Area specified door unlocked_SubState"""
    assert event_m10_10_x0(z165=0, z166=1300000, z167=10020103)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_14000():
    """Flame that disappears when Salamander is annihilated"""
    """State 0,2: [Preset] Flame that disappears when Salamander is annihilated _SubState"""
    assert event_m10_10_x118(z38=3100, z39=3110, z40=3150, z41=3160, z42=10101002)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_14010():
    """Disabling the ground flame damage of salamander"""
    """State 0,2: Disabling specific damage"""
    SetDamageImmunityByCharacterId(601000, 210100100, 1)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_15000():
    """Vegrant appeared with a hawk _ character"""
    """State 0,2: [Preset] Vagrant Appears in Hawk_Character_SubState"""
    assert event_m10_10_x156(flag6=110000020, z17=10101900, z18=2255)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_15010():
    """Vegrant Appears with a Hawk_Map"""
    """State 0,2: [Preset] Hawk Vegrant Appearance_SubState"""
    assert (event_m10_10_x159(flag5=110000020, z10=100968, z11=10101900, z12=2255, z13=1500001, z14=1500001,
            z15=110020022, z16=110000086))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_15020():
    """Hide hawk OBJ"""
    """State 0,2: [Preset] Hide hawk OBJ_SubState"""
    assert event_m10_10_x134(flag11=110000020, z32=10101900, flag12=100968)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_15030():
    """Vegrant appeared with a hawk_deletion judgment"""
    """State 0,3: [Preset] Vegrant deletion determination_SubState"""
    call = event_m10_10_x162(z9=2255)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_10_15040():
    """Vegrant Appears with a Hawk_Reward"""
    """State 0,2: [Preset] Vagrant Appearance with Hawk_Reward_SubState"""
    # lot:60008000:Soul of the Pursuer
    assert event_m10_10_x166(lot1=60008000, z6=110000086, z7=100968, z8=2255, flag4=110000024)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_16000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z118=10101000, z119=20, z120=1600000, z121=0, z122=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_37000():
    """Giant's memory warp boss"""
    """State 0,3: [Preset] Giant's memory intrusion_SubState"""
    call = event_m10_10_x96(z54=10101510, z55=101070, z56=0, z57=20100000, z58=3700000, z59=105300)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_10_37010():
    """Giant's memory warp"""
    """State 0,3: [Preset] Giant's memory intrusion_SubState"""
    call = event_m10_10_x96(z54=10101520, z55=101050, z56=0, z57=20100000, z58=3701000, z59=105301)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_10_37020():
    """Giant's memory warp_chandelier"""
    """State 0,3: [Preset] Giant's memory intrusion_SubState"""
    call = event_m10_10_x96(z54=10101530, z55=101060, z56=0, z57=20100000, z58=3702000, z59=105302)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()
        Quit()

def event_m10_10_38000():
    """Flame radiation salamander logic event to the cave"""
    """State 0,2: [Preset] Flame emission salamander logic event _SubState"""
    assert event_m10_10_x100()
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_80000():
    """Regeneration of fire 01_ main tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_10_x54(z109=1010000, z110=1010099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_81000():
    """Regenerative fire 02"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_10_x54(z109=1010100, z110=1010199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_83000():
    """Rebirth Fire 04_Riverside after connection with Madura"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_10_x54(z109=1010300, z110=1010399)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_90000():
    """Trophy_The Last Giant"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_10_x60(flag19=110000081, z94=5)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_x0(z165=0, z166=_, z167=_):
    """[Lib] Area designated door unlocked
    z165: Text ID when opened
    z166: Point ID
    z167: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z166, 0, z165, 1101, z167, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x1(z55=_, z56=_, z57=_, z58=_):
    """[Lib] Warp between maps after poly play
    z55: Pre-warp poly play ID
    z56: Poly Play ID after Warp
    z57: Map ID
    z58: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z55, z56, z57, z58, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_10_x2(z161=_, z162=_, z163=_, z164=_):
    """[Lib] NPC: Grave Placement: General purpose
    z161: Death map: Global event flag
    z162: Tomb: OBJ instance ID
    z163: Tomb move to: Generator ID
    z164: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z161, 1)
    IsGraveGeneratable(8, z164, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z162, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z162, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_10_x3(z158=_, z159=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z158: Global: death flag
    z159: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z159, 10, 0)
    CompareObjState(1, z159, 20, 0)
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
    IsObjSearched(0, z159)
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

def event_m10_10_x4(z156=_, z157=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z156: Area other flags: Ghost appearance
    z157: Area other flags: Conversation start
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
    SetEventFlag(z156, 1)
    CompareEventFlag(0, z156, 1)
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
    SetEventFlag(z157, 1)
    CompareEventFlag(0, z157, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_10_x5(z156=_, z157=_, z158=_, z159=_, z160=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z156: Ghost Appearance: Area Other Flag
    z157: Conversation start: Area and other flags
    z158: Death: Global event flag
    z159: Tomb: OBJ instance ID
    z160: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z160, 1, 0)
    CompareEventFlag(9, z156, 1)
    CompareObjState(9, z159, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z157, 1)
        CompareEventFlag(0, z157, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_10_x3(z158=z158, z159=z159, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_10_x4(z156=z156, z157=z157, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_10_x6(z152=1005, z153=1105, z154=_, z155=_):
    """[Lib] Item specified door unlocking_2
    z152: Text ID when opened
    z153: Text ID when not opened
    z154: item
    z155: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z154, z152, z153, z155, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x7(z150=_, z151=_):
    """[Lib] NPC: Death determination: General purpose
    z150: Generator ID
    z151: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z151, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z150)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z151, 1)
            CompareEventFlag(0, z151, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_10_x8(flag22=110000081, z145=650000, z146=650000, z147=101, z148=1010010, z149=110020080,
                    mode4=0):
    """[Lib] [Preset] Boss Battle Start
    flag22: Boss destruction flag
    z145: Start point ID
    z146: End point ID
    z147: Sound ID
    z148: Boss Battle ID
    z149: Other flags for logic
    mode4: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_10_x9(flag22=flag22)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_10_x10(z145=z145, z146=z146)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_10_x11(z147=z147, z148=z148, z149=z149)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_10_x12()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_10_x13(z148=z148)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_10_x14(z147=z147, z148=z148, z149=z149, mode4=mode4)
    """State 7: End state"""
    return 0

def event_m10_10_x9(flag22=110000081):
    """[Reproduction] Boss Battle_Start
    flag22: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag22) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_10_x10(z145=650000, z146=650000):
    """[Condition] Boss Battle_Start
    z145: Start point ID
    z146: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z145, z146, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z145, z146, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x11(z147=101, z148=1010010, z149=110020080):
    """[Execution] Boss Battle_Start
    z147: Sound ID
    z148: Boss Battle ID
    z149: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z147)
    """State 1: Boss battle start notification"""
    StartBossFight(z148)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z149, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x12():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x13(z148=1010010):
    """[Condition] Boss Battle_End Judgment
    z148: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z148, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x14(z147=101, z148=1010010, z149=110020080, mode4=0):
    """[Execute] Boss Battle_End
    z147: Sound ID
    z148: Boss Battle ID
    z149: Other flags for logic
    mode4: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z149, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z148)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode4) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z147)
    """State 5: End state"""
    return 0

def event_m10_10_x15(flag21=_):
    """[Lib] [Reproduction] Elevator_Initialization
    flag21: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(flag21) != 0:
        """State 3: Initialized"""
        return 1
    else:
        """State 2: Uninitialized"""
        return 0

def event_m10_10_x16():
    """[Lib] [Condition] Elevator_Initialization"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_10_x17(z142=_, z143=_, flag21=_, z144=_):
    """[Lib] [Execution] Elevator_Initialization
    z142: Elevator OBJ instance ID
    z143: Initial position OBJ state ID
    flag21: Initialization completion flag
    z144: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z142, z143)
    assert CompareObjStateId(z142, z144, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(flag21, 1)
    """State 3: End state"""
    return 0

def event_m10_10_x18(z142=_, z143=_, flag21=_, z144=_):
    """[Lib] [Preset] Elevator_Initialization
    z142: Elevator OBJ instance ID
    z143: Initial position OBJ state ID
    flag21: Initialization completion flag
    z144: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m10_10_x15(flag21=flag21)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m10_10_x16()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m10_10_x17(z142=z142, z143=z143, flag21=flag21, z144=z144)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m10_10_x19(flag20=110000082):
    """[Reproduction] Boss Battle_Poly Play Replay
    flag20: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(flag20) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_10_x20(z137=10100600):
    """[Condition] Boss Battle_Poly Play Replay
    z137: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z137, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x21(z138=101020, flag20=110000082, z139=651000, z141=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z138: Poly play ID
    flag20: Poly drama played flag
    z139: Warp point ID
    z141: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z138, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(flag20, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z139)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_10_x22(z137=10100600, z138=101020, flag20=110000082, z139=651000, z140=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z137: White door instance ID
    z138: Poly play ID
    flag20: Poly drama played flag
    z139: Warp point ID
    z140: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m10_10_x19(flag20=flag20)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m10_10_x20(z137=z137)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m10_10_x21(z138=z138, flag20=flag20, z139=z139, z141=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_10_x23(z86=2000):
    """[Lib] [Reproduction] Interlocking elevator
    z86: Initialization event ID
    """
    """State 0,1: Has the initialization event been completed?"""
    assert EventEnded(z86) != 0
    """State 2: End state"""
    return 0

def event_m10_10_x24(z84=10101050, z85=10101060, z87=201000, z88=201001, z89=201002, z90=201003):
    """[Lib] [Conditions] Interlocking elevator
    z84: Reference lift_object instance ID
    z85: Mirror lift_object instance ID
    z87: Reference lift point_on
    z88: Reference lift point_below
    z89: Mirror lift point_on
    z90: Mirror lift point_bottom
    """
    """State 0,2: Elevator state judgment"""
    CompareObjState(0, z84, 30, 0)
    CompareObjState(0, z84, 40, 0)
    CompareObjState(1, z84, 70, 0)
    CompareObjState(1, z84, 32, 0)
    CompareObjState(2, z84, 80, 0)
    CompareObjState(2, z84, 42, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(2):
        Goto('L0')
    elif ConditionGroup(0):
        Goto('L1')
    """State 5,8: Switch back after raising the standard"""
    return 2
    """State 4: While the standard is descending or waiting for the descent to finish"""
    Label('L0')
    """State 9: Switch back after descent"""
    return 3
    """State 3: Standard is below or above"""
    Label('L1')
    """State 1: Point waiting"""
    CompareObjState(8, z84, 30, 0)
    IsPlayerInsidePoint(8, z88, z88, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z85, 40, 0)
    IsPlayerInsidePoint(9, z89, z89, 1)
    SetConditionGroup(0, 9)
    CompareObjState(10, z84, 40, 0)
    IsPlayerInsidePoint(10, z87, z87, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z85, 30, 0)
    IsPlayerInsidePoint(11, z90, z90, 1)
    SetConditionGroup(1, 11)
    if ConditionGroup(0):
        """State 6: Standard from bottom to top"""
        return 0
    elif ConditionGroup(1):
        """State 7: Standard is from top to bottom"""
        return 1

def event_m10_10_x25(z84=10101050, z85=10101060, z87=201000, z90=201003, z136=15):
    """[Lib] [execution] interlocking elevator
    z84: Reference lift_object instance ID
    z85: Mirror lift_object instance ID
    z87: Start point ID
    z90: End point ID
    z136: Safety time
    """
    """State 0,2: The elevator starts moving"""
    ChangeObjState(z84, 70)
    ChangeObjState(z85, 80)
    """State 1: Did you get off the switch?"""
    CompareObjState(8, z85, 42, 0)
    CompareObjState(8, z84, 32, 0)
    IsPlayerInsidePoint(8, z87, z90, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z84, 72)
    ChangeObjState(z85, 82)
    """State 4: Wait for switch transition"""
    CompareObjState(8, z84, 40, 0)
    CompareObjState(8, z85, 30, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m10_10_x26(z84=10101050, z85=10101060, z86=2000, z87=201000, z88=201001, z89=201002, z90=201003,
                     z91=15):
    """[Lib] [Preset] Interlocking elevator
    z84: Reference lift_object instance ID
    z85: Mirror lift_object instance ID
    z86: Initialization event ID
    z87: On reference point ID_
    z88: Below reference point ID_
    z89: On mirror point ID_
    z90: Mirror point under
    z91: Safety time
    """
    """State 0,1: [Lib] [Reproduction] Interlocking Elevator_SubState"""
    assert event_m10_10_x23(z86=z86)
    """State 2: [Lib] [Condition] Interlocking elevator_SubState"""
    call = event_m10_10_x24(z84=z84, z85=z85, z87=z87, z88=z88, z89=z89, z90=z90)
    if call.Get() == 2:
        """State 6: [Lib] [Execution] Interlocking elevator_Returning the switch after the reference rise_SubState"""
        assert event_m10_10_x61(z84=z84, z85=z85, z87=z87, z90=z90, z93=15)
    elif call.Get() == 3:
        """State 5: [Lib] [Execution] Interlocking elevator_Returning the switch after the reference descent_SubState"""
        assert event_m10_10_x62(z84=z84, z85=z85, z87=z87, z90=z90, z92=15)
    elif call.Get() == 0:
        """State 4: [Lib] [Execution] Interlocking Elevator_Reference is rising_SubState"""
        assert event_m10_10_x25(z84=z84, z85=z85, z87=z87, z90=z90, z136=15)
    elif call.Get() == 1:
        """State 3: [Lib] [Execution] Interlocking Elevator_Reference is descending_SubState"""
        assert event_m10_10_x27(z84=z84, z85=z85, z87=z87, z90=z90, z135=15)
    """State 7: End state"""
    return 0

def event_m10_10_x27(z84=10101050, z85=10101060, z87=201000, z90=201003, z135=15):
    """[Lib] [execution] interlocking elevator
    z84: Reference lift_object instance ID
    z85: Mirror lift_object instance ID
    z87: Start point ID
    z90: End point ID
    z135: Safety time
    """
    """State 0,2: The elevator starts moving"""
    ChangeObjState(z84, 80)
    ChangeObjState(z85, 70)
    """State 1: Did you get off the switch?"""
    CompareObjState(8, z85, 32, 0)
    CompareObjState(8, z84, 42, 0)
    IsPlayerInsidePoint(8, z87, z90, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z84, 82)
    ChangeObjState(z85, 72)
    """State 4: Wait for switch transition"""
    CompareObjState(8, z84, 30, 0)
    CompareObjState(8, z85, 40, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m10_10_x28(z130=104160, z131=102422, z132=102423, z133=110010107, z134=103662):
    """[Lib] Appearance determination: General purpose
    z130: Death: Global event flag
    z131: Local emigration permission: Global event flag
    z132: Relocation permission after moving: Global event flag
    z133: Appearance determination: Area and other flags
    z134: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z130, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z131, 1)
            CompareEventFlag(8, z132, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z131, 1)
                CompareEventFlag(8, z134, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z133, 1)
                    CompareEventFlag(0, z133, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z133, 0)
                    CompareEventFlag(0, z133, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z133, 0)
        CompareEventFlag(0, z133, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()
    Quit()
    """Unused"""
    """State 9: End state"""
    return 0

def event_m10_10_x29(z125=10101600):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z125: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_10_x30(z125=z125)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_10_x34(z125=z125)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_10_x35()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_10_x31(z125=z125, mode3=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_10_x32(z125=z125, z127=38, z128=3, z129=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_10_x33(z125=z125, z126=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_10_x30(z125=10101600):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z125: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z125, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z125, 10)
        assert CompareObjStateId(z125, 10, 0)
    elif CompareObjStateId(z125, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z125, 74, 1) and CompareObjStateId(z125, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_10_x31(z125=10101600, mode3=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z125: Object instance ID
    mode3: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z125)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode3) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_10_x32(z125=10101600, z127=38, z128=3, z129=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z125: Object instance ID
    z127: Key guide type
    z128: Event action
    z129: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z125, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z125, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z125, 30)
        assert CompareObjStateId(z125, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z125, z127, z128)
        assert PlayerIsInEventAction(z128) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z128, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z125, 74, 0)
        CompareObjState(1, z125, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z129)
            assert CompareObjStateId(z125, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z125, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_10_x33(z125=10101600, z126=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z125: Object instance ID
    z126: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z125, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_10_x34(z125=10101600):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z125: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z125, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x35():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x36(z123=10101600, val2=10100000):
    """[Reproduction] Hidden door 1_face SFX
    z123: OBJ instance ID of the bug key
    val2: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z123, 20, 0):
        pass
    else:
        Goto('L0')
    """State 2: Event light reproduction judgment"""
    if (not val2) != 0:
        pass
    else:
        """State 3: Event light ON"""
        SetPointLightEnabled(val2, 1, 0)
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
    if (not val2) != 0:
        pass
    else:
        """State 4: Event light OFF"""
        SetPointLightEnabled(val2, 0, 0)
    """State 9: Not started"""
    return 1

def event_m10_10_x37(z123=10101600):
    """[Conditions] Hidden door 1_Face SFX
    z123: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z123, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x38(z123=10101600, val2=10100000, z124=0.6, val3=1.5):
    """[Execution] Hidden door 1_Face SFX
    z123: OBJ instance ID of the bug key
    val2: Event light ID
    z124: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,2: Event light usage judgment"""
    if (not val2) != 0:
        """State 5: Wait until face SFX playback"""
        assert (GetStateTime() > val3) != 0
        """State 4: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    else:
        """State 1: Event light ON"""
        SetPointLightEnabled(val2, 1, z124)
        assert (GetStateTime() > val3) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_10_x39(z123=10101600, val2=10100000, z124=0.6, val3=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z123: OBJ instance ID of the bug key
    val2: Event light ID
    z124: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_10_x36(z123=z123, val2=val2)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_10_x37(z123=z123)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_10_x38(z123=z123, val2=val2, z124=z124, val3=val3)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_10_x40(z81=10100417, z82=100000, z83=110000079):
    """[Lib] [Preset] King's door
    z81: King's door OBJ instance ID
    z82: Navigation change point ID
    z83: Opening flag
    """
    """State 0,1: [Reproduction] King's door_SubState"""
    call = event_m10_10_x41(z81=z81, z82=z82)
    if call.Get() == 0:
        """State 4: [Condition] King's door_SubState"""
        call = event_m10_10_x42(z81=z81, z83=z83)
        if call.Get() == 1:
            """State 3: [Execution] King's Door_Open_SubState"""
            assert event_m10_10_x43(z81=z81, z82=z82, z83=z83)
        elif call.Get() == 0:
            """State 2: [Execution] King's door_Do not open_SubState"""
            assert event_m10_10_x44(z81=z81)
    elif call.Get() == 1:
        """State 5: [Lib] [Condition] King's door_Close_SubState"""
        assert event_m10_10_x55(z81=z81)
        """State 6: [Lib] [Execution] King's door_Close_SubState"""
        assert event_m10_10_x56(z81=z81, z82=z82)
    elif call.Get() == 2:
        """State 7: [Lib] [Condition] King's door_Guest_SubState"""
        call = event_m10_10_x63(z81=z81)
        if call.Get() == 0:
            """State 8: [Lib] [Execution] King's Door_Guest_Passable_SubState"""
            assert event_m10_10_x64(z81=z81, z82=z82)
        elif call.Get() == 1:
            """State 9: [Lib] [Execution] King's door_Guest_No access_SubState"""
            assert event_m10_10_x65(z81=z81, z82=z82)
    """State 10: Rerun"""
    return 0

def event_m10_10_x41(z81=10100417, z82=100000):
    """[Lib] [Reproduction] King's door
    z81: King's door OBJ instance ID
    z82: Navigation change point ID
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Is the door closed or closed?"""
    if CompareObjStateId(z81, 10, 0):
        """State 4: Waiting for the door to close"""
        Label('L0')
        assert CompareObjStateId(z81, 10, 0)
        """State 5: Navimesh attribute added"""
        AddNavimeshAttribute(z82, 2)
        """State 7: Closed"""
        return 0
    elif CompareObjStateId(z81, 80, 0):
        Goto('L0')
    else:
        """State 1: Waiting for the door to open"""
        assert CompareObjStateId(z81, 30, 0)
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z82, 2)
        """State 8: is open"""
        return 1
    """State 9: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_10_x42(z81=10100417, z83=110000079):
    """[Lib] [Condition] King's door
    z81: King's door OBJ instance ID
    z83: Opening flag
    """
    """State 0,2: Did you approach the king's door?"""
    CompareObjPlayerDistance(0, z81, 3, 5)
    assert ConditionGroup(0)
    """State 1: Is it equipped with a king's ring? Has it been opened?"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    SetConditionGroup(0, 8)
    # goods:40510000:King's Ring
    DoesPlayerHaveItem(8, 40510000, 1, 3, 1, 1, 0)
    CompareEventFlag(8, z83, 1)
    if ConditionGroup(0):
        """State 4: Equipped with a king's ring"""
        return 1
    else:
        """State 3: Not qualified"""
        return 0

def event_m10_10_x43(z81=10100417, z82=100000, z83=110000079):
    """[Lib] [Execution] King's door_Open
    z81: King's door OBJ instance ID
    z82: Navigation change point ID
    z83: Opening flag
    """
    """State 0,1: Opening flag ON King's door opens"""
    SetEventFlag(z83, 1)
    ChangeOwnObjState(70)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z81, 30, 0)
    assert ConditionGroup(0)
    """State 3: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z82, 2)
    """State 4: End state"""
    return 0

def event_m10_10_x44(z81=10100417):
    """[Lib] [execution] King's door _ not open
    z81: King's door OBJ instance ID
    """
    """State 0,1: Event message display"""
    # action:2000:"Produce the symbol of the King"
    DisplayEventMessage(2000, 0, 0, 0)
    """State 2: Equipped with an or ring away from the king's door?"""
    CompareObjPlayerDistance(0, z81, 10, 3)
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x45(z118=_, z119=20, z120=_, z121=0, z122=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z118: Object instance ID
    z119: OBJ state ID
    z120: Navimesh switching point ID
    z121: Additional attributes
    z122: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_10_x46(z118=z118, z119=z119, z120=z120, z122=z122, z121=z121)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_10_x47(z118=z118, z119=z119, z120=z120)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_10_x48(z118=z118, z119=z119, z120=z120, z121=z121, z122=z122)
    """State 4: End state"""
    return 0

def event_m10_10_x46(z118=_, z119=20, z120=_, z122=2, z121=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z118: Target OBJ instance ID
    z119: Target OBJ state ID
    z120: Navimesh switching point ID
    z122: Additional attributes
    z121: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z118, z119, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z120, z122)
        DeleteNavimeshAttribute(z120, z121)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_10_x47(z118=_, z119=20, z120=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z118: Target OBJ instance ID
    z119: Target OBJ state ID
    z120: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z118, z119, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x48(z118=_, z119=20, z120=_, z121=0, z122=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z118: Target OBJ instance ID
    z119: Target OBJ state ID
    z120: Navimesh switching point ID
    z121: Additional attributes
    z122: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z120, z121)
    DeleteNavimeshAttribute(z120, z122)
    """State 2: End state"""
    return 0

def event_m10_10_x49(z112=102442, z113=526, z114=104170, z115=60, z116=103670, z117=65):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z112: White Phantom can appear: Global event flag
    z113: White Phantom: Generator ID
    z114: Death: Global event flag
    z115: Body: Generator group ID
    z116: Hostile: Global event flag
    z117: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z113)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z114, 1)
        CompareEventFlag(1, z116, 1)
        CompareEventFlag(2, z112, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z113)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z114, 1)
            CompareEventFlag(1, z116, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z113)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z114, 1)
            CompareEventFlag(1, z116, 1)
            HasNpcPhantomSpawned(2, z113, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z115, 0)
                HasNpcPhantomSpawned(0, z113, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z113)
    """State 4: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 11: End state"""
    return 0

def event_m10_10_x50(z111=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z111: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z111)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_10_x51():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x52(z109=_, z110=_):
    """[Lib] [execute] Rebirth fire
    z109: Flag start ID
    z110: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z109, z110, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x53():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x54(z109=_, z110=_):
    """[Lib] [Preset] Rebirth
    z109: Flag start ID
    z110: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_10_x51()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_10_x53()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_10_x52(z109=z109, z110=z110)
    """State 4: End state"""
    return 0

def event_m10_10_x55(z81=10100417):
    """[Lib] [Condition] King's door closed
    z81: King's door OBJ instance ID
    """
    """State 0,1: Did you leave the king's door?"""
    CompareObjPlayerDistance(0, z81, 30, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x56(z81=10100417, z82=100000):
    """[Lib] [Execution] King's door closes
    z81: King's door OBJ instance ID
    z82: Navigation change point ID
    """
    """State 0,1: The king's door closes"""
    ChangeOwnObjState(80)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z81, 10, 0)
    assert ConditionGroup(0)
    """State 3: Navimesh attribute deletion"""
    AddNavimeshAttribute(z82, 2)
    """State 4: End state"""
    return 0

def event_m10_10_x57(z105=110000081, z106=102452, z107=206, z108=7440):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z105: Defeat Boss 1: Area and other flags
    z106: Summon Achievement: Global Event Flag
    z107: Summon achievement count: global variable
    z108: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z106, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z105, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z107, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z107, NpcInfoValue(z108, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z106, 1)
                CompareEventFlag(0, z106, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 8: End state"""
    return 0

def event_m10_10_x58(z99=102810, z100=10000010, z101=520, z102=104340, z103=0, z104=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z99: Summoning conditions: Global event flag
    z100: Summon range
    z101: Generator ID
    z102: Death: Global event flag
    z103: Appearance: Minimum time
    z104: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z102, 1)
        CompareEventFlag(8, z99, 1)
        IsPlayerInsidePoint(8, z100, z100, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z102, 1)
            CompareStateTime(1, z103, 3, z104)
            IsPlayerInsidePoint(2, z100, z100, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z101)
                HasNpcPhantomSpawned(0, z101, 1)
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

def event_m10_10_x59(z95=10000020, z96=521, z97=0, z98=0):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z95: Summon range
    z96: Generator ID
    z97: Appearance: Minimum time
    z98: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z95, z95, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z97, 3, z98)
        IsPlayerInsidePoint(1, z95, z95, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z96)
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

def event_m10_10_x60(flag19=_, z94=_):
    """[Lib] [Preset] Get trophy
    flag19: Acquisition trigger_other flags
    z94: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag19) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag19, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z94)
    """State 4: End state"""
    return 0

def event_m10_10_x61(z84=10101050, z85=10101060, z87=201000, z90=201003, z93=15):
    """[Lib] [Execution] Interlocking elevator_Return the switch after the reference rises
    z84: Reference lift_object instance ID
    z85: Mirror lift_object instance ID
    z87: Start point ID
    z90: End point ID
    z93: Safety time
    """
    """State 0,1: Did you get off the switch?"""
    CompareObjState(8, z85, 42, 0)
    CompareObjState(8, z84, 32, 0)
    IsPlayerInsidePoint(8, z87, z90, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z84, 72)
    ChangeObjState(z85, 82)
    """State 3: Wait for switch transition"""
    CompareObjState(8, z84, 40, 0)
    CompareObjState(8, z85, 30, 0)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_10_x62(z84=10101050, z85=10101060, z87=201000, z90=201003, z92=15):
    """[Lib] [Execution] Interlocking elevator_Returns the switch after the descent
    z84: Reference lift_object instance ID
    z85: Mirror lift_object instance ID
    z87: Start point ID
    z90: End point ID
    z92: Safety time
    """
    """State 0,1: Did you get off the switch?"""
    CompareObjState(8, z85, 32, 0)
    CompareObjState(8, z84, 42, 0)
    IsPlayerInsidePoint(8, z87, z90, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z84, 82)
    ChangeObjState(z85, 72)
    """State 3: Wait for switch transition"""
    CompareObjState(8, z84, 30, 0)
    CompareObjState(8, z85, 40, 0)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_10_x63(z81=10100417):
    """[Lib] [Condition] King's door_Guest
    z81: King's door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z81, 30, 0)
    CompareObjState(1, z81, 10, 0)
    if ConditionGroup(0):
        """State 2: The door is open"""
        return 0
    elif ConditionGroup(1):
        """State 3: The door is closed"""
        return 1

def event_m10_10_x64(z81=10100417, z82=100000):
    """[Lib] [execution] King's door_guest_passable
    z81: King's door OBJ instance ID
    z82: Navigation change point ID
    """
    """State 0,2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z82, 2)
    """State 1: OBJ transition wait"""
    CompareObjState(0, z81, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x65(z81=10100417, z82=100000):
    """[Lib] [Execution] King's door_Guest_No traffic
    z81: King's door OBJ instance ID
    z82: Navigation change point ID
    """
    """State 0,2: Navimesh attribute added"""
    AddNavimeshAttribute(z82, 2)
    """State 1: OBJ transition wait"""
    CompareObjState(0, z81, 30, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x66(z67=39):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z67: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z67, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_10_x67(flag15=110020001, z68=4, z69=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    flag15: Lottery determination flag
    z68: Number of appearance judgment points
    z69: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag15, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z68)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z69, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_10_x68(val1=_, z78=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z78: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z78) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_10_x69(z74=_, z75=0, z76=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z74: Appearance judgment point ID
    z75: Minimum appearance time
    z76: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z74, z74, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z75, 3, z76)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_10_x70(z77=923, z79=_, z80=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z77: Generator ID
    z79: Appearance start point ID
    z80: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z77, z79, z80)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z77)
    """State 4: Finish"""
    return 0
    """Unused"""
    """State 2: Hostile / Friendship Judgment and Random Weight"""
    Quit()

def event_m10_10_x71(flag18=110000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    flag18: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(flag18) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_10_x72(z74=_, z75=0, z76=5, z77=923, val1=_, z78=10, z79=_, z80=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z74: Intrusion detection point ID
    z75: Minimum appearance time
    z76: Maximum time to appear
    z77: Generator ID
    val1: Appearance judgment number
    z78: Lottery result point variable
    z79: Appearance start point ID
    z80: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_10_x68(val1=val1, z78=z78)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_10_x69(z74=z74, z75=z75, z76=z76)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_10_x70(z77=z77, z79=z79, z80=z80)
    """State 4: Finish"""
    return 0

def event_m10_10_x73(z72=923, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z72: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z72)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_10_x74(flag18=110000002, z73=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    flag18: Defeat flag
    z73: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(flag18, 1)
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
                    SetEventFlag(z73, 1)
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

def event_m10_10_x75(flag18=110000002, z72=923, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    flag18: Defeat flag
    z72: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_10_x71(flag18=flag18)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_10_x73(z72=z72, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_10_x74(flag18=flag18, z73=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_10_x74(flag18=flag18, z73=102755)
    """State 5: End state"""
    return 0

def event_m10_10_x76(z70=9100, z71=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z70: Generator ID
    z71: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z70, z71)
    """State 2: End state"""
    return 0

def event_m10_10_x77(z70=9100, z71=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z70: Generator ID
    z71: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z70, z71, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_10_x78(z70=9100):
    """[Lib] [DC] [Condition] Transparent characters
    z70: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z70)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x79(z70=9100, z71=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z70: Generator ID
    z71: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_10_x77(z70=z70, z71=z71)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_10_x78(z70=z70)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_10_x76(z70=z70, z71=z71)
    """State 4: End state"""
    return 0

def event_m10_10_x80(flag15=110020001, z69=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    flag15: Lottery determination flag
    z69: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(flag15, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z69, 0)
    """State 3: End state"""
    return 0

def event_m10_10_x81(flag15=110020001, flag16=110000002, flag17=100804):
    """[Lib] [DC] [Reproduction] Wanderer_Random lottery_Global flag version
    flag15: Lottery determination flag
    flag16: Defeat flag
    flag17: Condition judgment flag
    """
    """State 0,5: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L2')
    """State 4: Are the appearance conditions satisfied?"""
    if GetEventFlag(flag17) != 1:
        pass
    else:
        Goto('L0')
    """State 10: Condition not achieved: Cannot appear"""
    return 4
    """State 3: Already destroyed?"""
    Label('L0')
    if GetEventFlag(flag16) != 0:
        pass
    else:
        Goto('L1')
    """State 9: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L1')
    if GetEventFlag(flag15) != 0:
        """State 7: Lottery completed"""
        return 1
    else:
        """State 6: Not drawn"""
        return 0
    """State 8: Guest: Exit"""
    Label('L2')
    return 2

def event_m10_10_x82(flag15=110020001, z67=39, flag16=110000002, z68=4, z69=10, flag17=100804):
    """[Lib] [DC] [Preset] Wanderer_Random lottery_Global flag version
    flag15: Lottery determination flag
    z67: Random number comparison value
    flag16: Defeat flag
    z68: Number of appearance judgment points
    z69: Lottery result point variable
    flag17: Condition judgment flag
    """
    """State 0,4: [Lib] [DC] [Reproduction] Wanderer_Random lottery_Global flag version_SubState"""
    call = event_m10_10_x81(flag15=flag15, flag16=flag16, flag17=flag17)
    if call.Get() == 4:
        """State 8: Condition unachieved_No appearance: End"""
        return 3
    elif call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m10_10_x66(z67=z67)
        if call.Get() == 0:
            """State 1: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_10_x67(flag15=flag15, z68=z68, z69=z69)
        elif call.Get() == 1:
            """State 3: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_10_x80(flag15=flag15, z69=z69)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_10_x83(flag14=110000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag14: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag14) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_10_x84(z65=857):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z65: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z65, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x85(z66=110020084):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z66: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z66, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x86(flag14=110000081, z65=857, z66=110020084):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag14: Boss destruction flag
    z65: Boss generator ID
    z66: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_10_x83(flag14=flag14)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_10_x84(z65=z65)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_10_x85(z66=z66)
    """State 4: End state"""
    return 0

def event_m10_10_x87():
    """[Net] Duel matching cancellation"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x88(z60=10101500):
    """[Condition] Check OBJ and warp between maps
    z60: OBJ instance ID to check
    """
    """State 0,1: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z60, 0)
    """State 2: Was OBJ checked or multi?"""
    IsObjSearched(0, z60)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_10_x89(z60=10101500, z61=101010, z62=101620, z63=10160000, z64=100000):
    """[Execution] Inter-map warp_warp execution after checking OBJ
    z60: OBJ instance ID to check
    z61: Pre-warp poly play ID
    z62: Poly Play ID after Warp
    z63: Map ID
    z64: Point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z60, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_10_x1(z55=z61, z56=z62, z57=z63, z58=z64)
    """State 4: End state"""
    return 0

def event_m10_10_x90(z60=10101500, z61=101010, z62=101620, z63=10160000, z64=100000):
    """[Preset] Check OBJ and warp between maps
    z60: OBJ instance ID to check
    z61: Pre-warp poly play ID
    z62: Poly Play ID after Warp
    z63: Map ID
    z64: Point ID
    """
    """State 0,2: [Reproduction] Inter-map warp_empty_SubState by examining OBJ"""
    assert event_m10_10_x87()
    """State 3: [Condition] Inter-map warp_SubState by checking OBJ"""
    call = event_m10_10_x88(z60=z60)
    if call.Get() == 1:
        """State 5: [Execution] Check OBJ, warp between maps_Key guide invalidation only_SubState"""
        assert event_m10_10_x91(z60=z60)
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Done():
        """State 4: [Execution] Inter-map warp_warp execution_SubState by checking OBJ"""
        assert event_m10_10_x89(z60=z60, z61=z61, z62=z62, z63=z63, z64=z64)
        """State 6: End state"""
        return 0

def event_m10_10_x91(z60=10101500):
    """[Execution] Checking OBJ and only warping between maps_key guide invalidation
    z60: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z60, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x92(z54=_):
    """[Reproduction] Memory invasion of giants
    z54: OBJ instance ID to check
    """
    """State 0,1: OBJ state initialization"""
    InitializeObj(z54)
    """State 2: End state"""
    return 0

def event_m10_10_x93(z54=_):
    """[Condition] Memory invasion of giant
    z54: OBJ instance ID to check
    """
    """State 0,1: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z54, 0)
    """State 2: Was OBJ checked or multi?"""
    IsObjSearched(0, z54)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        Goto('L0')
    """State 6: Key guide disabled"""
    return 1
    """State 4: Do you have an ash mist core?"""
    Label('L0')
    # goods:50910000:Ashen Mist Heart
    DoesPlayerHaveItem(0, 50910000, 1, 3, 1, 1, 0)
    if ConditionGroup(0):
        """State 5: Warp execution"""
        return 0
    else:
        """State 7: Nothing happens"""
        return 2

def event_m10_10_x94(z54=_, z55=_, z56=0, z57=20100000, z58=_, z59=_):
    """[Execution] Giant's memory intrusion
    z54: OBJ instance ID to check
    z55: Pre-warp poly play ID
    z56: Poly Play ID after Warp
    z57: Map ID
    z58: Point ID
    z59: Global flag for warp
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z54, 1)
    """State 3: Reset flag for judgment"""
    SetEventFlag(105300, 0)
    SetEventFlag(105301, 0)
    SetEventFlag(105302, 0)
    """State 4: Wait for flag reset"""
    CompareEventFlag(8, 105300, 0)
    CompareEventFlag(8, 105301, 0)
    CompareEventFlag(8, 105302, 0)
    assert ConditionGroup(8)
    """State 5: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 2: Judgment flag ON"""
    SetEventFlag(z59, 1)
    """State 6: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_10_x1(z55=z55, z56=z56, z57=z57, z58=z58)
    """State 7: End state"""
    return 0

def event_m10_10_x95(z54=_):
    """[Execution] Giant's memory intrusion_Key guide invalidation
    z54: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z54, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x96(z54=_, z55=_, z56=0, z57=20100000, z58=_, z59=_):
    """[Preset] Memory invasion of giants
    z54: OBJ instance ID to check
    z55: Pre-warp poly play ID
    z56: Poly Play ID after Warp
    z57: Map ID
    z58: Point ID
    z59: Global flag for warp
    """
    """State 0,1: [Reproduction] Giant's memory intrusion_SubState"""
    assert event_m10_10_x92(z54=z54)
    """State 4: [Condition] Memory intrusion of giants_SubState"""
    call = event_m10_10_x93(z54=z54)
    if call.Get() == 1:
        """State 3: [Execution] Giant's memory intrusion_Key guide invalidation_SubState"""
        assert event_m10_10_x95(z54=z54)
    elif call.Get() == 0:
        """State 2: [Execution] Giant's memory intrusion_SubState"""
        assert event_m10_10_x94(z54=z54, z55=z55, z56=z56, z57=z57, z58=z58, z59=z59)
        """State 7: Finish"""
        return 1
    elif call.Get() == 2:
        """State 5: [Execution] Giant's memory intrusion_Nothing happens_SubState"""
        assert event_m10_10_x101()
    """State 6: Rerun"""
    return 0

def event_m10_10_x97():
    """[Reproduction] Event for Flame Radiation Salamander Logic"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x98():
    """[Condition] Event for Flame Radiation Salamander Logic"""
    """State 0,1: Did the normal battle salamander die?"""
    IsChrDead(0, 3150)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x99():
    """[Execution] Event for Flame Radiation Salamander Logic"""
    """State 0,1: Flag ON"""
    SetEventFlag(110020043, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x100():
    """[Preset] Event for Flame Radiation Salamander Logic"""
    """State 0,1: [Reproduction] Event _SubState for flame emission salamander logic"""
    assert event_m10_10_x97()
    """State 2: [Condition] Event_SubState for Flame Radiation Salamander Logic"""
    assert event_m10_10_x98()
    """State 3: [Execution] Event_SubState for Flame Radiation Salamander Logic"""
    assert event_m10_10_x99()
    """State 4: End state"""
    return 0

def event_m10_10_x101():
    """[Execution] Giant's memory intrusion_Nothing happens"""
    """State 0,1: Message display"""
    # action:1113:"Alas, nothing happened"
    DisplayOwnOkMenu(1113, 0, 0, 190, 0, 0, 0)
    assert OkMenuDisplay() != 1
    """State 2: End state"""
    return 0

def event_m10_10_x102(z52=10100415, z53=520000):
    """[Preset] Key door that opens with "Welcome Key" (can be broken)
    z52: Door OBJ instance ID
    z53: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Lock door opened with "Welcome Key" (breakable) _SubState"""
    call = event_m10_10_x103(z52=z52)
    if call.Get() == 0:
        """State 2: [Condition] The key door that opens with "Welcome Key" (can be broken) _SubState"""
        assert event_m10_10_x104(z52=z52)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Key door opened with "Welcome Key" (breakable) _SubState"""
    assert event_m10_10_x105(z53=z53)
    """State 4: End state"""
    return 0

def event_m10_10_x103(z52=10100415):
    """[Reproduction] The key door that opens with the “Welcome Key” (can be broken)
    z52: Door OBJ instance ID
    """
    """State 0,1: Check the status of the door OBJ"""
    if CompareObjStateId(z52, 21, 1):
        """State 2: [Lib] Item specified door unlocking_SubState"""
        assert event_m10_10_x6(z152=1005, z153=1105, z154=50600000, z155=110000074)
        """State 3: Undestructed"""
        return 0
    else:
        """State 4: Destroyed"""
        return 1

def event_m10_10_x104(z52=10100415):
    """[Conditions] Lock door opened with "Welcome Key" (breakable)
    z52: Door OBJ instance ID
    """
    """State 0,1: Was the door destroyed?"""
    CompareObjState(0, z52, 21, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x105(z53=520000):
    """[Execution] Key door opened with "Welcome Key" (breakable)
    z53: Point ID for Navimesh change
    """
    """State 0,1,2: End state"""
    return 0

def event_m10_10_x106(flag13=102443, z48=1100000, z49=1100001, z50=10101160, z51=1100002):
    """[Preset] Switch that closes the door
    flag13: Closed area intrusion detection flag
    z48: Start point ID for closure
    z49: Closing end point ID
    z50: Instance ID of the iron lattice OBJ
    z51: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Switch that closes the door_SubState"""
    call = event_m10_10_x107(flag13=flag13, z51=z51)
    if call.Get() == 0:
        """State 2: [Condition] Switch that closes the door_SubState"""
        assert event_m10_10_x108(z48=z48, z49=z49)
        """State 3: [Execution] Switch that closes the door_SubState"""
        assert event_m10_10_x109(z50=z50, z51=z51, flag13=flag13)
    elif call.Done():
        pass
    """State 4: End state"""
    return 0

def event_m10_10_x107(flag13=102443, z51=1100002):
    """[Reproduction] Switch that closes the door
    flag13: Closed area intrusion detection flag
    z51: Point ID for Navimesh change
    """
    """State 0,2: Guest judgment"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 6: End for guest"""
    return 2
    """State 1: Flag status determination"""
    Label('L0')
    if GetEventFlag(flag13) != 0:
        """State 3: Navigation mesh change"""
        AddNavimeshAttribute(z51, 2)
        """State 5: Closed"""
        return 1
    else:
        """State 4: is open"""
        return 0

def event_m10_10_x108(z48=1100000, z49=1100001):
    """[Condition] Switch that closes the door
    z48: Start point ID for closure
    z49: Closing end point ID
    """
    """State 0,1: Did you enter the area?"""
    IsPlayerInsidePoint(0, z48, z49, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x109(z50=10101160, z51=1100002, flag13=102443):
    """[Execution] Switch that closes the door
    z50: Instance ID of the iron lattice OBJ
    z51: Point ID for Navimesh change
    flag13: Closed area intrusion detection flag
    """
    """State 0,2: Close the bar"""
    ChangeObjState(z50, 70)
    CompareObjState(0, z50, 30, 0)
    assert ConditionGroup(0)
    """State 1: Navigation mesh change"""
    AddNavimeshAttribute(z51, 2)
    """State 3: Turn on the flag"""
    SetEventFlag(flag13, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x110(z46=110010042, z47=10100413):
    """[Preset] Enemy door opening control
    z46: Opening flag for soldiers who open doors
    z47: Door OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemy door opening control_SubState"""
    call = event_m10_10_x111()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Enemy door opening control_SubState"""
        call = event_m10_10_x112(z47=z47)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
        """State 3: [Execution] Enemy door opening control_SubState"""
        assert event_m10_10_x113(z46=z46)
    """State 4: End state"""
    return 0

def event_m10_10_x111():
    """[Reproduction] Enemy door opening control"""
    """State 0,1: Guest judgment"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m10_10_x112(z47=10100413):
    """[Condition] Enemy door opening control
    z47: Door OBJ instance ID
    """
    """State 0,1: Is the door closed?"""
    CompareObjState(0, z47, 10, 0)
    if ConditionGroup(0):
        """State 2: Is the door OBJ damaged?"""
        IsObjDamaged(0, z47, -1, -4, 0)
        assert ConditionGroup(0)
        """State 3: Door not open"""
        return 0
    else:
        """State 4: Door open"""
        return 1

def event_m10_10_x113(z46=110010042):
    """[Execution] Enemy door opening control
    z46: Opening flag for soldiers who open doors
    """
    """State 0,1: Door open soldier activation flag ON"""
    SetEventFlag(z46, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x114(z43=1200000, z44=1200000, z45=10101700):
    """[Preset] Oiwa Gorokuro
    z43: Start point ID
    z44: End point ID
    z45: Instance ID of rock OBJ
    """
    """State 0,1: [Reproduction] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x115()
    """State 2: [Condition] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x116(z43=z43, z44=z44)
    """State 3: [Execution] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x117(z45=z45)
    """State 4: End state"""
    return 0

def event_m10_10_x115():
    """[Reproduction] Oiwa Gorokuro"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x116(z43=1200000, z44=1200000):
    """[Conditions] Oiwa Gorokuro
    z43: Start point ID
    z44: End point ID
    """
    """State 0,1: Entered the specified area"""
    IsPlayerInsidePoint(0, z43, z44, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x117(z45=10101700):
    """[Execution] Oiwa Gorokuro
    z45: Instance ID of rock OBJ
    """
    """State 0,1: Rocky run"""
    ChangeObjState(z45, 70)
    assert CompareObjStateId(z45, 20, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x118(z38=3100, z39=3110, z40=3150, z41=3160, z42=10101002):
    """[Preset] Flame that disappears when salamander is annihilated
    z38: Generator ID of salamander 1 that performs death determination
    z39: Salamander 2 generator ID for mortality determination
    z40: Salamander 3 generator ID for mortality determination
    z41: Generator ID of salamander 4 that performs death determination
    z42: OBJ instance ID of the flame blowing out from the ground
    """
    """State 0,1: [Reproduction] Flame that disappears when Salamander annihilates _SubState"""
    assert event_m10_10_x119()
    """State 2: [Condition] Flame that disappears when Salamander annihilates _SubState"""
    assert event_m10_10_x120(z38=z38, z39=z39, z40=z40, z41=z41)
    """State 3: [Execution] Flame that disappears when Salamander annihilates _SubState"""
    assert event_m10_10_x121(z42=z42)
    """State 4: End state"""
    return 0

def event_m10_10_x119():
    """[Reproduction] Flame that disappears when Salamander annihilates"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x120(z38=3100, z39=3110, z40=3150, z41=3160):
    """[Condition] Flame that disappears when salamander is annihilated
    z38: Generator ID of salamander 1 that performs death determination
    z39: Salamander 2 generator ID for mortality determination
    z40: Salamander 3 generator ID for mortality determination
    z41: Generator ID of salamander 4 that performs death determination
    """
    """State 0,1: Salamander death determination"""
    IsChrDeadOrRespawnOver(8, z38, 1)
    IsChrDeadOrRespawnOver(8, z39, 1)
    IsChrDeadOrRespawnOver(8, z40, 1)
    IsChrDeadOrRespawnOver(8, z41, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_10_x121(z42=10101002):
    """[Execution] Flame that disappears when Salamander is annihilated
    z42: OBJ instance ID of the flame blowing out from the ground
    """
    """State 0,1: Stop the flame blowing from the ground"""
    ChangeObjState(z42, 30)
    """State 2: End state"""
    return 0

def event_m10_10_x122(flag7=106200, z19=10101120):
    """[Preset] Giant tree nut drawing process
    flag7: Giant tree nut generation flag
    z19: Giant Tree OBJ Instance ID
    """
    """State 0,1: [Reproduction] Giant tree nut drawing process_SubState"""
    call = event_m10_10_x123(flag7=flag7, z19=z19)
    if call.Get() == 1:
        """State 4: [Condition] Giant tree nut drawing process_Generation_SubState"""
        assert event_m10_10_x151(flag7=flag7)
        """State 5: [Execution] Giant tree nut drawing process_Generation_SubState"""
        assert event_m10_10_x152(z19=z19)
    elif call.Get() == 0:
        """State 2: [Condition] Giant tree nut drawing process_SubState"""
        assert event_m10_10_x124(z19=z19)
        """State 3: [Execution] Giant tree nut drawing process_SubState"""
        assert event_m10_10_x125(z19=z19)
    """State 6: End state"""
    return 0

def event_m10_10_x123(flag7=106200, z19=10101120):
    """[Reproduction] Giant tree nut drawing process
    flag7: Giant tree nut generation flag
    z19: Giant Tree OBJ Instance ID
    """
    """State 0,1: Judgment status of giant tree nuts"""
    if GetEventFlag(flag7) != 0:
        """State 3: To generation judgment processing"""
        return 1
    else:
        """State 2: To drawing stop processing"""
        return 0

def event_m10_10_x124(z19=10101120):
    """[Condition] Giant tree nut drawing process
    z19: Giant Tree OBJ Instance ID
    """
    """State 0,1: Is OBJ active?"""
    IsObjActive(0, z19, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x125(z19=10101120):
    """[Execution] Giant tree nut drawing process
    z19: Giant Tree OBJ Instance ID
    """
    """State 0,1: Stop producing nuts"""
    ActivateObjItem(z19, 0)
    """State 2: Is OBJ no longer active?"""
    IsObjActive(0, z19, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x126():
    """[Reproduction] Vegrant_Initial layout change"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x127(z37=110000087):
    """[Condition] Vagrant_Initial location change
    z37: Flag to perform first battle or rematch determination
    """
    """State 0,1: Is it the first game? Is it a rematch?"""
    CompareEventFlag(0, z37, 0)
    if ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m10_10_x128(z34=853, z35=602000, z36=2):
    """[Execution] Vagrant_Initial location change
    z34: Vagrant generator ID
    z35: Point ID for relocation during rematch
    z36: Activation state ID at the time of rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z34, z35)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z34, z36)
    """State 3: End state"""
    return 0

def event_m10_10_x129(z34=853, z35=602000, z36=2, z37=110000087):
    """[Preset] Vagrant_Initial location change
    z34: Vagrant generator ID
    z35: Point ID for relocation during rematch
    z36: Activation state ID at the time of rematch
    z37: Flag for judging first battle or rematch
    """
    """State 0,1: [Reproduction] Vagrant_Initial layout change_SubState"""
    assert event_m10_10_x126()
    """State 3: [Condition] Vagrant_Initial location change_SubState"""
    call = event_m10_10_x127(z37=z37)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 2: [Execution] Vagrant_Initial placement change_SubState"""
        assert event_m10_10_x128(z34=z34, z35=z35, z36=z36)
    """State 4: End state"""
    return 0

def event_m10_10_x130(flag5=110000020, z11=10101900, z12=2255):
    """[Execution] Vegrant appeared with hawk
    flag5: Vegrant event executed flag
    z11: Hawk OBJ instance ID
    z12: Generator ID
    """
    """State 0,1: Starting approach of hawk: 70"""
    ChangeObjState(z11, 70)
    """State 3: Waiting for release of startup state"""
    CompareChrStartUpState(0, z12, 3, 1)
    assert ConditionGroup(0)
    """State 2: Event executed flag ON"""
    SetEventFlag(flag5, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x131(flag11=110000020, flag12=100968):
    """[Condition] Hide hawk OBJ
    flag11: Vegrant event executed flag
    flag12: Vagrant Defeat Flag
    """
    """State 0,1: Has the event occurred?"""
    if GetEventFlag(flag11) != 0:
        pass
    else:
        Goto('L0')
    """State 4: Event has occurred"""
    return 1
    """State 2: Is the Vegrant defeated?"""
    Label('L0')
    if GetEventFlag(flag12) != 0:
        """State 5: Vegrant defeated"""
        return 2
    else:
        """State 3: No event occurred"""
        return 0

def event_m10_10_x132():
    """[Reproduction] Hidden hawk OBJ_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x133(z32=10101900, z33=_):
    """[Execution] Hide hawk OBJ
    z32: Hawk OBJ instance ID
    z33: Hawk OBJ State
    """
    """State 0,1: State transition of hawk OBJ"""
    ChangeObjState(z32, z33)
    """State 2: End state"""
    return 0

def event_m10_10_x134(flag11=110000020, z32=10101900, flag12=100968):
    """[Preset] Hide hawk OBJ
    flag11: Vegrant event executed flag
    z32: Hawk OBJ instance ID
    flag12: Vagrant Defeat Flag
    """
    """State 0,1: [Reproduction] Hidden hawk OBJ_Sky_SubState"""
    assert event_m10_10_x132()
    """State 3: [Condition] Hide hawk OBJ_SubState"""
    call = event_m10_10_x131(flag11=flag11, flag12=flag12)
    if call.Get() == 1:
        """State 4: [Execution] Hide hawk OBJ_2_SubState"""
        assert event_m10_10_x133(z32=z32, z33=20)
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Hidden OBJ_SubState"""
        assert event_m10_10_x133(z32=z32, z33=30)
    """State 5: End state"""
    return 0

def event_m10_10_x135():
    """[Reproduction] Vagrant appearance with hawk_deletion judgment"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_10_x136(flag9=110000087):
    """[Reproduction] Vegrant _ poly play reproduction
    flag9: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(flag9) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_10_x137(z31=10100610, flag10=110000086):
    """[Conditions] Vegrant_Poly play
    z31: White door OBJ instance ID
    flag10: Boss destroy other flags
    """
    """State 0,1: Defeated Vegrant on the way through the white door"""
    if GetEventFlag(flag10) != 0:
        """State 3: Defeating Vagrant on the way: No poly play"""
        return 1
    elif CompareObjStateId(z31, 100, 0):
        """State 2: White door passing"""
        return 0

def event_m10_10_x138(z28=101030, flag9=110000087, z29=601000, z30=1):
    """[Execution] Vegrant _ poly play
    z28: Poly play ID
    flag9: Poly drama played flag
    z29: Warp point ID
    z30: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z28, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(flag9, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z29)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_10_x139(z28=101030, flag9=110000087, z29=601000, z30=1, z31=10100610, flag10=110000086):
    """[Preset] Vegrant_Poly Play
    z28: Poly play ID
    flag9: Poly drama played flag
    z29: Warp point ID
    z30: Weight until poly play
    z31: White door OBJ instance ID
    flag10: Boss destroy other flags
    """
    """State 0,1: [Reproduction] Vegrant_Poly Play_SubState"""
    call = event_m10_10_x136(flag9=flag9)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Vegrant_Poly Play_SubState"""
        call = event_m10_10_x137(z31=z31, flag10=flag10)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Vegrant_Poly Play_SubState"""
            assert event_m10_10_x138(z28=z28, flag9=flag9, z29=z29, z30=z30)
    """State 4: End state"""
    return 0

def event_m10_10_x140(flag8=110000086):
    """[Reproduction] Boss: Battle of Vegrant_Start
    flag8: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag8) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_10_x141(z23=600000, z24=600000, flag8=110000086):
    """[Conditions] Boss: Battle of Vegrant_Start
    z23: Start point ID
    z24: End point ID
    flag8: Defeat other flags
    """
    """State 0,1: Did you enter the boss room point? or Destroyed Vagrant on the way?"""
    IsPlayerInsidePoint(8, z23, z24, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z23, z24, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(1, flag8, 1)
    if ConditionGroup(0):
        """State 2: Entered the point"""
        return 0
    elif ConditionGroup(1):
        """State 3: Defeat Vegrant on the way"""
        return 1

def event_m10_10_x142(z25=102, z26=1010000, z27=110020085):
    """[Execution] Boss: Battle against Vegrant _Start
    z25: Sound ID
    z26: Boss Battle ID
    z27: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z25)
    """State 1: Boss battle start notification"""
    StartBossFight(z26)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z27, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x143():
    """[Reproduction] Boss: Vegrant Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x144(z26=1010000):
    """[Conditions] Boss: Vegrant Battle_End Judgment
    z26: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z26, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x145(z25=102, z26=1010000, z27=110020085, mode1=0):
    """[Execution] Boss: Battle of Vegrant _End
    z25: Sound ID
    z26: Boss Battle ID
    z27: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z27, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z26)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z25)
    """State 5: End state"""
    return 0

def event_m10_10_x146(flag8=110000086, z23=600000, z24=600000, z25=102, z26=1010000, z27=110020085, mode1=0):
    """[Preset] Boss: Battle against Vegrant _Start
    flag8: Boss destruction flag
    z23: Start point ID
    z24: End point ID
    z25: Sound ID
    z26: Boss Battle ID
    z27: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Boss: Vegrant Battle_Start_SubState"""
    call = event_m10_10_x140(flag8=flag8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss: Vegrant Battle_Start_SubState"""
        call = event_m10_10_x141(z23=z23, z24=z24, flag8=flag8)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 3: [Execution] Boss: Vegrant Battle_Start_SubState"""
            assert event_m10_10_x142(z25=z25, z26=z26, z27=z27)
            """State 2: [Reproduction] Boss: Vegrant Battle_Sky_SubState"""
            assert event_m10_10_x143()
            """State 6: [Condition] Boss: Vegrant Battle_End Judgment_SubState"""
            assert event_m10_10_x144(z26=z26)
            """State 4: [Execution] Boss: Vegrant Battle_End_SubState"""
            assert event_m10_10_x145(z25=z25, z26=z26, z27=z27, mode1=mode1)
    """State 7: End state"""
    return 0

def event_m10_10_x147(z20=110000082, z21=857, z22=652000):
    """[Preset] New Giant Senior Soldier
    z20: Flag to perform first battle or rematch determination
    z21: New Giant Senior Soldier Generator ID
    z22: Point ID for relocation during rematch
    """
    """State 0,1: [Reproduction] New Giant Senior Soldier_Initial Location Change_SubState"""
    assert event_m10_10_x148()
    """State 2: [Conditions] New Giant Senior Soldier_Initial Location Change_SubState"""
    call = event_m10_10_x149(z20=z20)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Execution] New Giant Senior Soldier_Initial Location Change_Rematch_SubState"""
        assert event_m10_10_x150(z21=z21, z22=z22)
    """State 4: End state"""
    return 0

def event_m10_10_x148():
    """[Reproduction] New Giant Senior Soldier"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x149(z20=110000082):
    """[Conditions] New Giant Senior Soldier
    z20: Flag to perform first battle or rematch determination
    """
    """State 0,1: Is it the first game? Is it a rematch?"""
    CompareEventFlag(0, z20, 0)
    if ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m10_10_x150(z21=857, z22=652000):
    """[Execution] New Giant Senior Soldier
    z21: New Giant Senior Soldier Generator ID
    z22: Point ID for relocation during rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z21, z22)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z21, 0)
    """State 3: End state"""
    return 0

def event_m10_10_x151(flag7=106200):
    """[Condition] Giant tree fruit drawing process
    flag7: Giant tree nut generation flag
    """
    """State 0,1: Judgment status of giant tree nuts"""
    CompareEventFlag(0, flag7, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x152(z19=10101120):
    """[Execution] Giant tree fruit drawing process
    z19: Giant Tree OBJ Instance ID
    """
    """State 0,1: Stop producing nuts"""
    ActivateObjItem(z19, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x153(flag6=110000020):
    """[Reproduction] Vegrant appeared with a hawk _ Character
    flag6: Vegrant event executed flag
    """
    """State 0,1: Has the event occurred?"""
    if GetEventFlag(flag6) != 0:
        """State 3: Event has occurred"""
        return 1
    else:
        """State 2: No event occurred"""
        return 0

def event_m10_10_x154(z18=2255):
    """[Condition] Vegrant appeared with a hawk _ Character
    z18: Generator ID
    """
    """State 0,1: Is it in startup state?"""
    CompareChrStartUpState(0, z18, 3, 0)
    CompareChrStartUpState(1, z18, 3, 1)
    if ConditionGroup(0):
        """State 2: During startup state: Attach"""
        return 0
    elif ConditionGroup(1):
        """State 3: Normal state: Do nothing"""
        return 1

def event_m10_10_x155(z17=10101900):
    """[Execution] Vagrant Appearance with Hawk _ Character
    z17: Hawk OBJ instance ID
    """
    """State 0,1: Character attach to hawk OBJ"""
    AttachCharacterToObj(z17, 6, 2)
    """State 2: Finish"""
    return 0

def event_m10_10_x156(flag6=110000020, z17=10101900, z18=2255):
    """[Preset] hawk bay grant appearance _ character
    flag6: Vegrant event executed flag
    z17: Hawk OBJ instance ID
    z18: Generator ID
    """
    """State 0,3: [Reproduction] Vegrant Appears with Hawk _ Character _ SubState"""
    call = event_m10_10_x153(flag6=flag6)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Vegrant appeared with hawks_Character_SubState"""
        call = event_m10_10_x154(z18=z18)
        if call.Get() == 0:
            """State 4: [Execution] Vagrant Appears in Hawk_Character_SubState"""
            assert event_m10_10_x155(z17=z17)
        elif call.Get() == 1:
            pass
    """State 1: Waiting for release of startup state"""
    CompareChrStartUpState(0, z18, 3, 1)
    assert ConditionGroup(0)
    """State 2: Forced detach"""
    DetachCharacterFromObj()
    """State 6: End state"""
    return 0

def event_m10_10_x157(flag5=110000020):
    """[Reproduction] Vegrant appeared with hawk
    flag5: Vegrant event executed flag
    """
    """State 0,1: Has the event occurred?"""
    if GetEventFlag(flag5) != 0:
        """State 3: Event has occurred"""
        return 1
    else:
        """State 2: No event occurred"""
        return 0

def event_m10_10_x158(z12=2255):
    """[Condition] Vegrant appearance with hawk _ generation determination
    z12: Generator ID
    """
    """State 0,1: Has a character been generated?"""
    IsChrActive(0, z12, 1)
    assert ConditionGroup(0)
    """State 2: Finish"""
    return 0

def event_m10_10_x159(flag5=110000020, z10=100968, z11=10101900, z12=2255, z13=1500001, z14=1500001,
                      z15=110020022, z16=110000086):
    """[Preset] Vagrant appears with hawk
    flag5: Vegrant event executed flag
    z10: Defeat global flag
    z11: Hawk OBJ instance ID
    z12: Generator ID
    z13: Start point ID
    z14: End point ID
    z15: Vagrant return flag
    z16: Defeat other flags
    """
    """State 0,1: [Reproduction] Vegrant Appears in the Hawk_SubState"""
    call = event_m10_10_x157(flag5=flag5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Vagrant Appearance with Hawk_Generation Determination_SubState"""
        assert event_m10_10_x158(z12=z12)
        """State 2: [Execution] Vagrant Appears in Hawk_SubState"""
        assert event_m10_10_x130(flag5=flag5, z11=z11, z12=z12)
    """State 4: End state"""
    return 0

def event_m10_10_x160(z9=2255):
    """[Condition] Vegrant appeared with hawk_deletion judgment
    z9: Generator ID
    """
    """State 0,2: Has a vegrant been generated?"""
    IsChrActive(0, z9, 1)
    assert ConditionGroup(0)
    """State 1: Has Vegrant finished the return action?"""
    CompareChrEzStateValue(0, z9, 7, 1, 0)
    IsChrActive(1, z9, 0)
    if ConditionGroup(0):
        """State 3: Returned"""
        return 0
    elif ConditionGroup(1):
        """State 4: Out of drawing"""
        return 1

def event_m10_10_x161(z9=2255):
    """[Execution] Vagrant Appearance with Hawk
    z9: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z9, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x162(z9=2255):
    """[Preset] Vegrant removal judgment
    z9: Generator ID
    """
    """State 0,3: [Reproduction] Vegrant deletion judgment_SubState"""
    call = event_m10_10_x135()
    if call.Get() == 0:
        """State 2: [Condition] Vegrant deletion determination_SubState"""
        call = event_m10_10_x160(z9=z9)
        if call.Get() == 0:
            """State 1: [Execution] Vegrant deletion determination_SubState"""
            assert event_m10_10_x161(z9=z9)
        elif call.Get() == 1:
            """State 5: Rerun"""
            return 1
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_10_x163(lot1=60008000, z6=110000086, z7=100968, flag4=110000024):
    """[Execution] Vagrant Appearance with a Hawk_Reward
    lot1: Item lottery ID
    z6: Defeat other flags
    z7: Defeat global flag
    flag4: Destroying flag of the appearance event
    """
    """State 0,1: Reward acquisition"""
    # lot:60008000:Soul of the Pursuer
    AwardItem(lot1, 1)
    """State 2: Boss Defeat Flag ON and Defeat Count +1"""
    SetEventFlag(z6, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(flag4, 1)
    # bonfire:10655:Cardinal Tower
    SetGlobalVariable(28, GetBonfireAsceticCount(10655) + 1)
    """State 3: End state"""
    return 0

def event_m10_10_x164(flag4=110000024):
    """[Reproduction] Vegrant Appearance with a Hawk_Reward
    flag4: Destroying flag of the appearance event
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Has it been defeated by the hawk appearance event?"""
    if GetEventFlag(flag4) != 0:
        """State 5: Defeated"""
        return 2
    else:
        """State 3: host"""
        return 0
    """State 4: The guests"""
    Label('L0')
    return 1

def event_m10_10_x165(z8=2255):
    """[Condition] Vegrant Appears with a Hawk_Reward
    z8: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z8)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x166(lot1=60008000, z6=110000086, z7=100968, z8=2255, flag4=110000024):
    """[Preset] Vagrant Appearance with a Hawk_Reward
    lot1: Item lottery ID
    z6: Defeat other flags
    z7: Defeat global flag
    z8: Generator ID
    flag4: Destroying flag of the appearance event
    """
    """State 0,1: [Reproduction] Vegrant Appears with Hawk_Reward_SubState"""
    call = event_m10_10_x164(flag4=flag4)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Vegrant Appears in Hawk_Reward_SubState"""
        assert event_m10_10_x165(z8=z8)
        """State 2: [Execution] Vagrant Appearance with Hawk_Reward_SubState"""
        assert event_m10_10_x163(lot1=lot1, z6=z6, z7=z7, flag4=flag4)
    """State 4: End state"""
    return 0

def event_m10_10_x167(z4=10101120, flag2=106200):
    """[Reproduction] Giant tree fruit_message
    z4: Giant Tree OBJ Instance ID
    flag2: Generation determination flag
    """
    """State 0,3: Giant Tree Initialization: 10"""
    ChangeObjState(z4, 10)
    DisableObjKeyGuide(z4, 1)
    assert CompareObjStateId(z4, 10, 0)
    """State 1: Judgment status of giant tree nuts"""
    if GetEventFlag(flag2) != 0:
        """State 4: Generating"""
        return 0
    else:
        """State 2: Giant Tree Key Guide Valid: 31"""
        ChangeObjState(z4, 31)
        DisableObjKeyGuide(z4, 0)
        assert CompareObjStateId(z4, 31, 0)
        """State 5: Not generated"""
        return 1

def event_m10_10_x168(z4=10101120, flag2=106200):
    """[Condition] Giant Tree Fruit_Message
    z4: Giant Tree OBJ Instance ID
    flag2: Generation determination flag
    """
    """State 0,1: Wait to examine"""
    IsObjSearched(0, z4)
    CompareEventFlag(1, flag2, 1)
    if ConditionGroup(1):
        """State 3: Generated"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m10_10_x169(z4=10101120):
    """[Execution] Giant Tree Fruit_Message
    z4: Giant Tree OBJ Instance ID
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z4, 1)
    """State 1: Message display"""
    # action:2007:"A Giant rests in peace"
    DisplayEventMessage(2007, 0, 0, 0)
    assert EventMessageDisplay() != 0
    """State 2: Message waiting waiting"""
    assert EventMessageDisplay() != 1
    """State 4: End state"""
    return 0

def event_m10_10_x170(z4=10101120, flag2=106200):
    """[Preset] Giant Tree Fruit_Message
    z4: Giant Tree OBJ Instance ID
    flag2: Generation determination flag
    """
    """State 0,1: [Reproduction] Giant Tree Fruit_Message_SubState"""
    call = event_m10_10_x167(z4=z4, flag2=flag2)
    if call.Get() == 0:
        """State 4: [Condition] Giant tree fruit_Message_Waiting_SubState"""
        assert event_m10_10_x177(flag2=flag2)
    elif call.Get() == 1:
        """State 3: [Condition] Giant tree fruit_Message_SubState"""
        call = event_m10_10_x168(z4=z4, flag2=flag2)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Giant Tree Fruit_Message_SubState"""
            assert event_m10_10_x169(z4=z4)
    """State 5: End state"""
    return 0

def event_m10_10_x171(flag3=106200, z5=10101120):
    """[Reproduction] Giant tree fruit_system version
    flag3: Giant tree nut generation flag
    z5: Giant Tree OBJ Instance ID
    """
    """State 0,1: Judgment status of giant tree nuts"""
    if GetEventFlag(flag3) != 0:
        """State 3: Acquisition judgment"""
        return 1
    else:
        """State 2: Generation determination"""
        return 0

def event_m10_10_x172(z5=10101120):
    """[Execution] Giant Tree Fruit_System Version
    z5: Giant Tree OBJ Instance ID
    """
    """State 0,1: Tree fruit generation"""
    ActivateObjItem(z5, 1)
    """State 2: Save intrusion count"""
    SetGlobalVariable(1, TotalInvasionCount())
    """State 3: End state"""
    return 0

def event_m10_10_x173(flag3=106200):
    """[Condition] Giant Tree Fruit_System Version
    flag3: Tree fruit generation judgment flag
    """
    """State 0,1: Generation determination"""
    CompareEventFlag(0, flag3, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x174(z5=10101120):
    """[Conditions] Giant tree fruit_system version_generation time
    z5: Giant Tree OBJ Instance ID
    """
    """State 0,1: Have you got the nuts?"""
    WasObjItemAcquired(0, z5, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x175(flag3=106200, z5=10101120):
    """[Execution] Giant tree fruit_system version_when generating
    flag3: Giant tree nut generation flag
    z5: Giant Tree OBJ Instance ID
    """
    """State 0,1: Turn off the generation judgment flag"""
    SetEventFlag(flag3, 0)
    """State 2: Reset item acquisition information"""
    ResetObjItem(z5)
    """State 3: End state"""
    return 0

def event_m10_10_x176(flag3=106200, z5=10101120):
    """[Preset] Giant Tree Fruit_System Version
    flag3: Giant tree nut generation flag
    z5: Giant Tree OBJ Instance ID
    """
    """State 0,1: [Reproduction] Giant Tree Fruit_System Version_SubState"""
    call = event_m10_10_x171(flag3=flag3, z5=z5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Giant Tree Fruit_System Version_SubState"""
        assert event_m10_10_x173(flag3=flag3)
        """State 2: [Execution] Giant Tree Fruit_System Version_SubState"""
        assert event_m10_10_x172(z5=z5)
    """State 5: [Condition] Giant tree fruit_System version_Generation_SubState"""
    assert event_m10_10_x174(z5=z5)
    """State 3: [Execution] Giant Tree Fruit_System Version_When Generated_SubState"""
    assert event_m10_10_x175(flag3=flag3, z5=z5)
    """State 6: End state"""
    return 0

def event_m10_10_x177(flag2=106200):
    """[Condition] Giant tree fruit_Message_Waiting for acquisition
    flag2: Generate flag
    """
    """State 0,1: Have you got the nuts?"""
    CompareEventFlag(0, flag2, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x178(z1=110000024, z2=2255, z3=110000020):
    """[DC] [Condition] Vegrant appeared with hawks
    z1: Destruction flag
    z2: Generator ID
    z3: Appearance event executed flag
    """
    """State 0,1: Destroyed or withdrawn?"""
    CompareEventFlag(0, z1, 1)
    CompareChrEzStateValue(0, z2, 7, 1, 0)
    SetConditionGroup(0, 8)
    CompareEventFlag(8, z3, 1)
    IsChrActive(8, z2, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x179(flag1=110000025):
    """[DC] [Execution] Vagrant appears with hawks
    flag1: Zako start flag
    """
    """State 0,1: Zako start flag ON"""
    SetEventFlag(flag1, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x180(flag1=110000025):
    """[DC] [Reproduction] Vagrant appeared with hawks
    flag1: Zako start flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is Zako started?"""
        if GetEventFlag(flag1) != 0:
            pass
        else:
            """State 3: Not executed"""
            return 0
    """State 4: Finish"""
    return 1

def event_m10_10_x181(z1=110000024, z2=2255, z3=110000020, flag1=110000025):
    """[DC] [Preset] Vagrant appears with hawks
    z1: Destruction flag
    z2: Generator ID
    z3: Appearance event executed flag
    flag1: Zako start flag
    """
    """State 0,1: [DC] [Reproduction] Vagrant Appears in Hawk_Zako Launch_SubState"""
    call = event_m10_10_x180(flag1=flag1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Vagrant appears with hawks_Zako start_SubState"""
        assert event_m10_10_x178(z1=z1, z2=z2, z3=z3)
        """State 2: [DC] [Execution] Vagrant Appears in Hawk_Zako Launch_SubState"""
        assert event_m10_10_x179(flag1=flag1)
    """State 4: End state"""
    return 0

def event_m10_10_111242():
    """OBJ: Moonlight Jun: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_10_x2(z161=104163, z162=10104300, z163=61, z164=7430)
    Quit()

def event_m10_10_111243():
    """OBJ: Satoshi Moonlight: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7430:Benhart of Jugo
    event_m10_10_x5(z156=110010100, z157=110020101, z158=104160, z159=10104300, z160=111242, npc1=7430)
    Quit()

def event_m10_10_111244():
    """OBJ: Satoshi Moonlight: Judgment of death"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z150=60, z151=104163)
    Quit()

def event_m10_10_111245():
    """OBJ: Tsukimitsu: Appearance judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_10_x28(z130=104160, z131=102422, z132=102423, z133=110010107, z134=103662)
    Quit()

def event_m10_10_111252():
    """OBJ: Patch: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_10_x2(z161=104171, z162=10104200, z163=66, z164=7440)
    Quit()

def event_m10_10_111253():
    """OBJ: Patch: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7440:Mild-mannered Pate
    event_m10_10_x5(z156=110010110, z157=110020111, z158=104170, z159=10104200, z160=111252, npc1=7440)
    Quit()

def event_m10_10_111254():
    """OBJ: Patch: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z150=65, z151=104171)
    Quit()

def event_m10_10_111255():
    """OBJ: Patch: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_10_x49(z112=102442, z113=526, z114=104170, z115=60, z116=103670, z117=65)
    Quit()

def event_m10_10_111256():
    """OBJ: Patch: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_10_x57(z105=110000081, z106=102452, z107=206, z108=7440)
    Quit()

def event_m10_10_111262():
    """OBJ: Mapping: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_10_x2(z161=104181, z162=10104100, z163=86, z164=7510)
    Quit()

def event_m10_10_111263():
    """OBJ: cartography: key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7510:Cartographer Cale
    event_m10_10_x5(z156=110010120, z157=110020121, z158=104180, z159=10104100, z160=111262, npc1=7510)
    Quit()

def event_m10_10_111264():
    """OBJ: Mapping: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z150=85, z151=104181)
    Quit()

def event_m10_10_111292():
    """OBJ: Yorozu Baba: Tomb"""
    """State 0,1: NPC: Yorozu Baba: Grave Placement_SubState"""
    event_m10_10_x2(z161=104211, z162=10104000, z163=261, z164=7540)
    Quit()

def event_m10_10_111293():
    """OBJ: Yorozu Baba: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7540:Merchant Hag Melentia
    event_m10_10_x5(z156=110010130, z157=110020131, z158=104210, z159=10104000, z160=111292, npc1=7540)
    Quit()

def event_m10_10_111294():
    """OBJ: Yorozu Baba: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z150=260, z151=104211)
    Quit()

def event_m10_10_111435():
    """OBJ: Enclosed Person: Black Phantom Summon"""
    """State 0,1: Black Phantom Summon: Start"""
    CompareEventFlag(0, 100972, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_10_x58(z99=102810, z100=10000010, z101=520, z102=104340, z103=0, z104=2)
    Quit()

def event_m10_10_120110():
    """Trophy: Moonlight Sword (Giant Forest)"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_10_x60(flag19=110020108, z94=31)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_10_130000():
    """White spirit test"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_10_x50(z111=527)
    Quit()

def event_m10_10_130001():
    """White Spirit Test_2"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_10_x50(z111=528)
    Quit()

def event_m10_10_140000():
    """Black spirit test"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_10_x59(z95=10000020, z96=521, z97=0, z98=0)
    Quit()

def event_m10_10_4000000():
    """[DC] Vagrant appears with hawks"""
    """State 0,2: [DC] [Preset] Vagrant Appears in Hawk_Zako Launch_SubState"""
    assert event_m10_10_x181(z1=110000024, z2=2255, z3=110000020, flag1=110000025)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4001000():
    """[DC] Wanderer A_Random lottery and generation_Global flag version"""
    """State 0,6: [Lib] [DC] [Preset] Wanderer_Random lottery_Global flag version_SubState"""
    call = event_m10_10_x82(flag15=110020001, z67=39, flag16=110000002, z68=4, z69=10, flag17=100804)
    if call.Get() == 3:
        pass
    elif call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_10_x72(z74=81000000, z75=0, z76=5, z77=923, val1=1, z78=10, z79=81000001, z80=81000099)
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_10_x72(z74=81000100, z75=0, z76=5, z77=923, val1=2, z78=10, z79=81000101, z80=81000199)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m10_10_x72(z74=81000200, z75=0, z76=5, z77=923, val1=3, z78=10, z79=81000201, z80=81000299)
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert event_m10_10_x72(z74=81000300, z75=0, z76=5, z77=923, val1=4, z78=10, z79=81000300, z80=81000301)
        """State 2: Start flag ON"""
        SetEventFlag(110020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4001010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_10_x75(flag18=110000002, z72=923, mode2=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_10_x79(z70=9100, z71=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_10_4031000():
    """[DC] NPC White Spirit _ Gesture Management _ New Giant Senior Soldier _ Dead"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_10_x86(flag14=110000081, z65=857, z66=110020084)
    """State 1: Finish"""
    EndMachine()
    Quit()

