# -*- coding: utf-8 -*-
def event_m10_10_1000():
    """King's door"""
    """State 0,2: [Lib] [Preset] King's Door_SubState"""
    assert event_m10_10_x40(z99=10100417, z100=100000, z101=110000079)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_10_2000():
    """Interlocking elevator_initialization"""
    """State 0,3: [Lib] [Preset] Elevator_Initialization_SubState"""
    assert event_m10_10_x18(z162=10101050, z163=12, z164=110020060, z165=30)
    """State 2: [Lib] [Preset] Elevator_Initialization_2_SubState"""
    assert event_m10_10_x18(z162=10101060, z163=14, z164=110020061, z165=40)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_2010():
    """Interlocking elevator_operation"""
    """State 0,2: [Lib] [Preset] Interlocking Elevator_SubState"""
    assert (event_m10_10_x26(z102=10101050, z103=10101060, z104=2000, z105=201000, z106=201001, z107=201002,
            z108=201003, z109=15))
    """State 1: Rerun"""
    RestartMachine()

def event_m10_10_3000():
    """Navimesh change of the wall that breaks in the flame barrel"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101300, z138=20, z139=300000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_10_x29(z144=10101600)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m10_10_x39(z142=10101600, val2=10100000, z143=0.6, val3=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101610, z138=20, z139=402000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_5000():
    """Key door that opens with "key of fire" """
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z174=1005, z175=1105, z176=50810000, z177=110000070)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_5100():
    """The lock door that opens with the key of the royal soldier"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z174=1005, z175=1105, z176=50600000, z177=110000072)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_5200():
    """The key door that opens with the “Welcome Key” (can be broken)"""
    """State 0,2: [Preset] Key door opened with "Welcome Key" (breakable) _SubState"""
    assert event_m10_10_x102(z65=10100415, z66=520000)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_5210():
    """The key door that opens with the key of the Royal Soldier"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z174=1005, z175=1105, z176=50600000, z177=110000076)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_5211():
    """The key door that opens with the key of the Royal Soldier"""
    """State 0,2: [Lib] Item specified door unlocking_2_SubState"""
    assert event_m10_10_x6(z174=1005, z175=1105, z176=50600000, z177=110000078)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6000():
    """Boss: Vegrant _ Battle"""
    """State 0,2: Is the poly drama replay event over?"""
    assert EventEnded(6010) != 0
    """State 3: [Preset] Boss: Vegrant Battle_Start_SubState"""
    assert (event_m10_10_x146(z30=110000086, z31=600000, z32=600000, z33=102, z34=1010000, z35=110020085,
            mode1=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6010():
    """Boss: Vegrant_Poly Theater"""
    """State 0,2: [Preset] Vegrant_Poly Play_SubState"""
    assert event_m10_10_x139(z36=101030, z37=110000087, z38=601000, z39=1, z40=10100610, z41=110000086)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6020():
    """Boss: Vegrant _ initial placement change"""
    """State 0,2: [Preset] Vagrant_Initial layout change_SubState"""
    assert event_m10_10_x129(z46=853, z47=602000, z48=2, z49=110000087)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6050():
    """Barista 1 destroyed by Vegrant attack"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101450, z138=20, z139=605000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6060():
    """Barista 2 destroyed by Vegrant attack"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101456, z138=20, z139=606000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6500():
    """Boss: New Giant Senior Soldier_Deceased_Battle"""
    """State 0,2: Is the poly drama replay event over?"""
    assert EventEnded(6510) != 0
    """State 3: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_10_x8(z166=110000081, z167=650000, z168=650000, z169=101, z170=1010010, z171=110020080,
            mode4=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6510():
    """Boss: New Giant Senior Soldier_Deceased_Poly Drama"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m10_10_x22(z156=10100600, z157=101020, z158=110000082, z159=651000, z160=1)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_6520():
    """Boss: New Giant Senior Soldier"""
    """State 0,2: [Preset] New Giant Senior Soldier _ Change initial placement_SubState"""
    assert event_m10_10_x147(z27=110000082, z28=857, z29=652000)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_7000():
    """Vegrant hawk taxi"""
    """State 0,2: [Preset] Inter-map warp_SubState by checking OBJ"""
    assert event_m10_10_x90(z73=10101500, z74=101010, z75=101620, z76=10160000, z77=100000)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_8000():
    """One-way door that opens the enemy when attacked _ One-way door control"""
    """State 0,2: [Lib] Area specified door unlocked_SubState"""
    assert event_m10_10_x0(z187=0, z188=800000, z189=10020101)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_8010():
    """Enemy opens when attacking One-way door _ Enemy door opening control"""
    """State 0,2: [Preset] Enemy door opening control_SubState"""
    assert event_m10_10_x110(z58=110010042, z59=10100413)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_9000():
    """Giant nut"""
    """State 0,2: [Preset] Giant Tree Fruit_System Version_SubState"""
    assert event_m10_10_x176(z7=106200, z8=10101120)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_10_9010():
    """Giant tree nut drawing process"""
    """State 0,2: [Preset] Giant tree nut drawing process_SubState"""
    assert event_m10_10_x122(z25=106200, z26=10101120)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_10_9020():
    """Giant Tree Fruit_Message"""
    """State 0,2: [Preset] Giant Tree Fruit_Message_SubState"""
    assert event_m10_10_x170(z5=10101120, z6=106200)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_10_10000():
    """Navi-mesh attribute change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101070, z138=20, z139=1000000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_10010():
    """Navi-mesh attribute change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101071, z138=20, z139=1001000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_10020():
    """Navi-mesh attribute change of inner wall of fracture wall"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101075, z138=20, z139=1002000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_11000():
    """Switch that closes the door"""
    """State 0,2: [Preset] Door close switch _SubState"""
    assert event_m10_10_x106(z60=102443, z61=1100000, z62=1100001, z63=10101160, z64=1100002)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_12000():
    """Oiwa Gorokuro"""
    """State 0,2: [Preset] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x114(z55=1200000, z56=1200000, z57=10101700)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_13000():
    """Waterway one-way door"""
    """State 0,2: [Lib] Area specified door unlocked_SubState"""
    assert event_m10_10_x0(z187=0, z188=1300000, z189=10020103)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_14000():
    """Flame that disappears when Salamander is annihilated"""
    """State 0,2: [Preset] Flame that disappears when Salamander is annihilated _SubState"""
    assert event_m10_10_x118(z50=3100, z51=3110, z52=3150, z53=3160, z54=10101002)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_14010():
    """Disabling the ground flame damage of salamander"""
    """State 0,2: Disabling specific damage"""
    SetDamageImmunityByCharacterId(601000, 210100100, 1)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_15000():
    """Vegrant appeared with a hawk _ character"""
    """State 0,2: [Preset] Vagrant Appears in Hawk_Character_SubState"""
    assert event_m10_10_x156(z22=110000020, z23=10101900, z24=2255)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_15010():
    """Vegrant Appears with a Hawk_Map"""
    """State 0,2: [Preset] Hawk Vegrant Appearance_SubState"""
    assert (event_m10_10_x159(z14=110000020, z15=100968, z16=10101900, z17=2255, z18=1500001, z19=1500001,
            z20=110020022, z21=110000086))
    """State 1: Finish"""
    EndMachine()

def event_m10_10_15020():
    """Hide hawk OBJ"""
    """State 0,2: [Preset] Hide hawk OBJ_SubState"""
    assert event_m10_10_x134(z42=110000020, z43=10101900, z44=100968)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_15030():
    """Vegrant appeared with a hawk_deletion judgment"""
    """State 0,3: [Preset] Vegrant deletion determination_SubState"""
    call = event_m10_10_x162(z13=2255)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_10_15040():
    """Vegrant Appears with a Hawk_Reward"""
    """State 0,2: [Preset] Vagrant Appearance with Hawk_Reward_SubState"""
    # lot:60008000:Soul of the Pursuer
    assert event_m10_10_x166(lot1=60008000, z9=110000086, z10=100968, z11=2255, z12=110000024)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_16000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_10_x45(z137=10101000, z138=20, z139=1600000, z140=0, z141=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_37000():
    """Giant's memory warp boss"""
    """State 0,3: [Preset] Giant's memory intrusion_SubState"""
    call = event_m10_10_x96(z67=10101510, z68=101070, z69=0, z70=20100000, z71=3700000, z72=105300)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_10_37010():
    """Giant's memory warp"""
    """State 0,3: [Preset] Giant's memory intrusion_SubState"""
    call = event_m10_10_x96(z67=10101520, z68=101050, z69=0, z70=20100000, z71=3701000, z72=105301)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_10_37020():
    """Giant's memory warp_chandelier"""
    """State 0,3: [Preset] Giant's memory intrusion_SubState"""
    call = event_m10_10_x96(z67=10101530, z68=101060, z69=0, z70=20100000, z71=3702000, z72=105302)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m10_10_38000():
    """Flame radiation salamander logic event to the cave"""
    """State 0,2: [Preset] Flame emission salamander logic event _SubState"""
    assert event_m10_10_x100()
    """State 1: Finish"""
    EndMachine()

def event_m10_10_80000():
    """Regeneration of fire 01_ main tower"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_10_x54(z128=1010000, z129=1010099)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_81000():
    """Regenerative fire 02"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_10_x54(z128=1010100, z129=1010199)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_83000():
    """Rebirth Fire 04_Riverside after connection with Madura"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_10_x54(z128=1010300, z129=1010399)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_90000():
    """Trophy_The Last Giant"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_10_x60(z112=110000081, z113=5)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_x0(z187=0, z188=_, z189=_):
    """[Lib] Area designated door unlocked
    z187: Text ID when opened
    z188: Point ID
    z189: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(z188, 0, z187, 1101, z189, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x1(z68=_, z69=_, z70=_, z71=_):
    """[Lib] Warp between maps after poly play
    z68: Pre-warp poly play ID
    z69: Poly Play ID after Warp
    z70: Map ID
    z71: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z68, z69, z70, z71, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m10_10_x2(z183=_, z184=_, z185=_, z186=_):
    """[Lib] NPC: Grave Placement: General purpose
    z183: Death map: Global event flag
    z184: Tomb: OBJ instance ID
    z185: Tomb move to: Generator ID
    z186: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z183, 1)
    IsGraveGeneratable(8, z186, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z184, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z184, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_10_x3(z180=_, z181=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z180: Global: death flag
    z181: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z181, 10, 0)
    CompareObjState(1, z181, 20, 0)
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
    IsObjSearched(0, z181)
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

def event_m10_10_x4(z178=_, z179=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z178: Area other flags: Ghost appearance
    z179: Area other flags: Conversation start
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
    SetEventFlag(z178, 1)
    CompareEventFlag(0, z178, 1)
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
    SetEventFlag(z179, 1)
    CompareEventFlag(0, z179, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_10_x5(z178=_, z179=_, z180=_, z181=_, z182=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z178: Ghost Appearance: Area Other Flag
    z179: Conversation start: Area and other flags
    z180: Death: Global event flag
    z181: Tomb: OBJ instance ID
    z182: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z182, 1, 0)
    CompareEventFlag(9, z178, 1)
    CompareObjState(9, z181, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z179, 1)
        CompareEventFlag(0, z179, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_10_x3(z180=z180, z181=z181, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_10_x4(z178=z178, z179=z179, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_10_x6(z174=1005, z175=1105, z176=_, z177=_):
    """[Lib] Item specified door unlocking_2
    z174: Text ID when opened
    z175: Text ID when not opened
    z176: item
    z177: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z176, z174, z175, z177, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x7(z172=_, z173=_):
    """[Lib] NPC: Death determination: General purpose
    z172: Generator ID
    z173: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z173, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z172)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z173, 1)
            CompareEventFlag(0, z173, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_10_x8(z166=110000081, z167=650000, z168=650000, z169=101, z170=1010010, z171=110020080,
                    mode4=0):
    """[Lib] [Preset] Boss Battle Start
    z166: Boss destruction flag
    z167: Start point ID
    z168: End point ID
    z169: Sound ID
    z170: Boss Battle ID
    z171: Other flags for logic
    mode4: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_10_x9(z166=z166)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_10_x10(z167=z167, z168=z168)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_10_x11(z169=z169, z170=z170, z171=z171)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_10_x12()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_10_x13(z170=z170)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_10_x14(z169=z169, z170=z170, z171=z171, mode4=mode4)
    """State 7: End state"""
    return 0

def event_m10_10_x9(z166=110000081):
    """[Reproduction] Boss Battle_Start
    z166: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z166) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_10_x10(z167=650000, z168=650000):
    """[Condition] Boss Battle_Start
    z167: Start point ID
    z168: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z167, z168, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z167, z168, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x11(z169=101, z170=1010010, z171=110020080):
    """[Execution] Boss Battle_Start
    z169: Sound ID
    z170: Boss Battle ID
    z171: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z169)
    """State 1: Boss battle start notification"""
    StartBossFight(z170)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z171, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x12():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x13(z170=1010010):
    """[Condition] Boss Battle_End Judgment
    z170: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z170, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x14(z169=101, z170=1010010, z171=110020080, mode4=0):
    """[Execute] Boss Battle_End
    z169: Sound ID
    z170: Boss Battle ID
    z171: Other flags for logic
    mode4: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z171, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z170)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode4) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z169)
    """State 5: End state"""
    return 0

def event_m10_10_x15(z164=_):
    """[Lib] [Reproduction] Elevator_Initialization
    z164: Initialization completion flag
    """
    """State 0,1: Already initialized?"""
    if GetEventFlag(z164) != 0:
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

def event_m10_10_x17(z162=_, z163=_, z164=_, z165=_):
    """[Lib] [Execution] Elevator_Initialization
    z162: Elevator OBJ instance ID
    z163: Initial position OBJ state ID
    z164: Initialization completion flag
    z165: OBJ state after initialization
    """
    """State 0,1: Elevator initialization"""
    ChangeObjState(z162, z163)
    assert CompareObjStateId(z162, z165, 0)
    """State 2: Initialization completion flag ON"""
    SetEventFlag(z164, 1)
    """State 3: End state"""
    return 0

def event_m10_10_x18(z162=_, z163=_, z164=_, z165=_):
    """[Lib] [Preset] Elevator_Initialization
    z162: Elevator OBJ instance ID
    z163: Initial position OBJ state ID
    z164: Initialization completion flag
    z165: OBJ state after initialization
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Initialization_SubState"""
    call = event_m10_10_x15(z164=z164)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Elevator_Initialization_SubState"""
        call = event_m10_10_x16()
        if call.Get() == 0:
            """State 2: [Lib] [Execution] Elevator_Initialization_SubState"""
            assert event_m10_10_x17(z162=z162, z163=z163, z164=z164, z165=z165)
        elif call.Get() == 1:
            pass
    """State 4: End state"""
    return 0

def event_m10_10_x19(z158=110000082):
    """[Reproduction] Boss Battle_Poly Play Replay
    z158: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z158) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_10_x20(z156=10100600):
    """[Condition] Boss Battle_Poly Play Replay
    z156: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z156, 100, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x21(z157=101020, z158=110000082, z159=651000, z161=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z157: Poly play ID
    z158: Poly drama played flag
    z159: Warp point ID
    z161: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z157, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z158, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z159)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_10_x22(z156=10100600, z157=101020, z158=110000082, z159=651000, z160=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z156: White door instance ID
    z157: Poly play ID
    z158: Poly drama played flag
    z159: Warp point ID
    z160: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m10_10_x19(z158=z158)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m10_10_x20(z156=z156)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m10_10_x21(z157=z157, z158=z158, z159=z159, z161=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_10_x23(z104=2000):
    """[Lib] [Reproduction] Interlocking elevator
    z104: Initialization event ID
    """
    """State 0,1: Has the initialization event been completed?"""
    assert EventEnded(z104) != 0
    """State 2: End state"""
    return 0

def event_m10_10_x24(z102=10101050, z103=10101060, z105=201000, z106=201001, z107=201002, z108=201003):
    """[Lib] [Conditions] Interlocking elevator
    z102: Reference lift_object instance ID
    z103: Mirror lift_object instance ID
    z105: Reference lift point_on
    z106: Reference lift point_below
    z107: Mirror lift point_on
    z108: Mirror lift point_bottom
    """
    """State 0,2: Elevator state judgment"""
    CompareObjState(0, z102, 30, 0)
    CompareObjState(0, z102, 40, 0)
    CompareObjState(1, z102, 70, 0)
    CompareObjState(1, z102, 32, 0)
    CompareObjState(2, z102, 80, 0)
    CompareObjState(2, z102, 42, 0)
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
    CompareObjState(8, z102, 30, 0)
    IsPlayerInsidePoint(8, z106, z106, 1)
    SetConditionGroup(0, 8)
    CompareObjState(9, z103, 40, 0)
    IsPlayerInsidePoint(9, z107, z107, 1)
    SetConditionGroup(0, 9)
    CompareObjState(10, z102, 40, 0)
    IsPlayerInsidePoint(10, z105, z105, 1)
    SetConditionGroup(1, 10)
    CompareObjState(11, z103, 30, 0)
    IsPlayerInsidePoint(11, z108, z108, 1)
    SetConditionGroup(1, 11)
    if ConditionGroup(0):
        """State 6: Standard from bottom to top"""
        return 0
    elif ConditionGroup(1):
        """State 7: Standard is from top to bottom"""
        return 1

def event_m10_10_x25(z102=10101050, z103=10101060, z105=201000, z108=201003, z155=15):
    """[Lib] [execution] interlocking elevator
    z102: Reference lift_object instance ID
    z103: Mirror lift_object instance ID
    z105: Start point ID
    z108: End point ID
    z155: Safety time
    """
    """State 0,2: The elevator starts moving"""
    ChangeObjState(z102, 70)
    ChangeObjState(z103, 80)
    """State 1: Did you get off the switch?"""
    CompareObjState(8, z103, 42, 0)
    CompareObjState(8, z102, 32, 0)
    IsPlayerInsidePoint(8, z105, z108, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z102, 72)
    ChangeObjState(z103, 82)
    """State 4: Wait for switch transition"""
    CompareObjState(8, z102, 40, 0)
    CompareObjState(8, z103, 30, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m10_10_x26(z102=10101050, z103=10101060, z104=2000, z105=201000, z106=201001, z107=201002,
                     z108=201003, z109=15):
    """[Lib] [Preset] Interlocking elevator
    z102: Reference lift_object instance ID
    z103: Mirror lift_object instance ID
    z104: Initialization event ID
    z105: On reference point ID_
    z106: Below reference point ID_
    z107: On mirror point ID_
    z108: Mirror point under
    z109: Safety time
    """
    """State 0,1: [Lib] [Reproduction] Interlocking Elevator_SubState"""
    assert event_m10_10_x23(z104=z104)
    """State 2: [Lib] [Condition] Interlocking elevator_SubState"""
    call = event_m10_10_x24(z102=z102, z103=z103, z105=z105, z106=z106, z107=z107, z108=z108)
    if call.Get() == 2:
        """State 6: [Lib] [Execution] Interlocking elevator_Returning the switch after the reference rise_SubState"""
        assert event_m10_10_x61(z102=z102, z103=z103, z105=z105, z108=z108, z111=15)
    elif call.Get() == 3:
        """State 5: [Lib] [Execution] Interlocking elevator_Returning the switch after the reference descent_SubState"""
        assert event_m10_10_x62(z102=z102, z103=z103, z105=z105, z108=z108, z110=15)
    elif call.Get() == 0:
        """State 4: [Lib] [Execution] Interlocking Elevator_Reference is rising_SubState"""
        assert event_m10_10_x25(z102=z102, z103=z103, z105=z105, z108=z108, z155=15)
    elif call.Get() == 1:
        """State 3: [Lib] [Execution] Interlocking Elevator_Reference is descending_SubState"""
        assert event_m10_10_x27(z102=z102, z103=z103, z105=z105, z108=z108, z154=15)
    """State 7: End state"""
    return 0

def event_m10_10_x27(z102=10101050, z103=10101060, z105=201000, z108=201003, z154=15):
    """[Lib] [execution] interlocking elevator
    z102: Reference lift_object instance ID
    z103: Mirror lift_object instance ID
    z105: Start point ID
    z108: End point ID
    z154: Safety time
    """
    """State 0,2: The elevator starts moving"""
    ChangeObjState(z102, 80)
    ChangeObjState(z103, 70)
    """State 1: Did you get off the switch?"""
    CompareObjState(8, z103, 32, 0)
    CompareObjState(8, z102, 42, 0)
    IsPlayerInsidePoint(8, z105, z108, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z102, 82)
    ChangeObjState(z103, 72)
    """State 4: Wait for switch transition"""
    CompareObjState(8, z102, 30, 0)
    CompareObjState(8, z103, 40, 0)
    assert ConditionGroup(8)
    """State 5: End state"""
    return 0

def event_m10_10_x28(z149=104160, z150=102422, z151=102423, z152=110010107, z153=103662):
    """[Lib] Appearance determination: General purpose
    z149: Death: Global event flag
    z150: Local emigration permission: Global event flag
    z151: Relocation permission after moving: Global event flag
    z152: Appearance determination: Area and other flags
    z153: Pre-movement hostile: Global event flag
    """
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance determination: Death determination"""
        CompareEventFlag(0, z149, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Migration determination"""
            CompareEventFlag(8, z150, 1)
            CompareEventFlag(8, z151, 1)
            if ConditionGroup(8):
                pass
            else:
                """State 7: Appearance determination: Appearance determination"""
                CompareEventFlag(8, z150, 1)
                CompareEventFlag(8, z153, 0)
                if ConditionGroup(8):
                    """State 4: Appearance determination: Appearable"""
                    SetEventFlag(z152, 1)
                    CompareEventFlag(0, z152, 1)
                    assert ConditionGroup(0)
                    Goto('L0')
                else:
                    """State 5: Appearance judgment: Impossible to appear"""
                    SetEventFlag(z152, 0)
                    CompareEventFlag(0, z152, 0)
                    assert ConditionGroup(0)
                    Goto('L0')
        """State 8: Appearance judgment: Appearance stopped"""
        SetEventFlag(z152, 0)
        CompareEventFlag(0, z152, 0)
        assert ConditionGroup(0)
    """State 6: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m10_10_x29(z144=10101600):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z144: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_10_x30(z144=z144)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_10_x34(z144=z144)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_10_x35()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_10_x31(z144=z144, mode3=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_10_x32(z144=z144, z146=38, z147=3, z148=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_10_x33(z144=z144, z145=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_10_x30(z144=10101600):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z144: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z144, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z144, 10)
        assert CompareObjStateId(z144, 10, 0)
    elif CompareObjStateId(z144, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z144, 74, 1) and CompareObjStateId(z144, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_10_x31(z144=10101600, mode3=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z144: Object instance ID
    mode3: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z144)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode3) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_10_x32(z144=10101600, z146=38, z147=3, z148=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z144: Object instance ID
    z146: Key guide type
    z147: Event action
    z148: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z144, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z144, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z144, 30)
        assert CompareObjStateId(z144, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z144, z146, z147)
        assert PlayerIsInEventAction(z147) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z147, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z144, 74, 0)
        CompareObjState(1, z144, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z148)
            assert CompareObjStateId(z144, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z144, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_10_x33(z144=10101600, z145=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z144: Object instance ID
    z145: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z144, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_10_x34(z144=10101600):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z144: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z144, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x35():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x36(z142=10101600, val2=10100000):
    """[Reproduction] Hidden door 1_face SFX
    z142: OBJ instance ID of the bug key
    val2: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z142, 20, 0):
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

def event_m10_10_x37(z142=10101600):
    """[Conditions] Hidden door 1_Face SFX
    z142: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z142, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x38(z142=10101600, val2=10100000, z143=0.6, val3=1.5):
    """[Execution] Hidden door 1_Face SFX
    z142: OBJ instance ID of the bug key
    val2: Event light ID
    z143: Light fade time
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
        SetPointLightEnabled(val2, 1, z143)
        assert (GetStateTime() > val3) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m10_10_x39(z142=10101600, val2=10100000, z143=0.6, val3=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z142: OBJ instance ID of the bug key
    val2: Event light ID
    z143: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m10_10_x36(z142=z142, val2=val2)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m10_10_x37(z142=z142)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m10_10_x38(z142=z142, val2=val2, z143=z143, val3=val3)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m10_10_x40(z99=10100417, z100=100000, z101=110000079):
    """[Lib] [Preset] King's door
    z99: King's door OBJ instance ID
    z100: Navigation change point ID
    z101: Opening flag
    """
    """State 0,1: [Reproduction] King's door_SubState"""
    call = event_m10_10_x41(z99=z99, z100=z100)
    if call.Get() == 0:
        """State 4: [Condition] King's door_SubState"""
        call = event_m10_10_x42(z99=z99, z101=z101)
        if call.Get() == 1:
            """State 3: [Execution] King's Door_Open_SubState"""
            assert event_m10_10_x43(z99=z99, z100=z100, z101=z101)
        elif call.Get() == 0:
            """State 2: [Execution] King's door_Do not open_SubState"""
            assert event_m10_10_x44(z99=z99)
    elif call.Get() == 1:
        """State 5: [Lib] [Condition] King's door_Close_SubState"""
        assert event_m10_10_x55(z99=z99)
        """State 6: [Lib] [Execution] King's door_Close_SubState"""
        assert event_m10_10_x56(z99=z99, z100=z100)
    elif call.Get() == 2:
        """State 7: [Lib] [Condition] King's door_Guest_SubState"""
        call = event_m10_10_x63(z99=z99)
        if call.Get() == 0:
            """State 8: [Lib] [Execution] King's Door_Guest_Passable_SubState"""
            assert event_m10_10_x64(z99=z99, z100=z100)
        elif call.Get() == 1:
            """State 9: [Lib] [Execution] King's door_Guest_No access_SubState"""
            assert event_m10_10_x65(z99=z99, z100=z100)
    """State 10: Rerun"""
    return 0

def event_m10_10_x41(z99=10100417, z100=100000):
    """[Lib] [Reproduction] King's door
    z99: King's door OBJ instance ID
    z100: Navigation change point ID
    """
    """State 0,6: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Is the door closed or closed?"""
    if CompareObjStateId(z99, 10, 0):
        """State 4: Waiting for the door to close"""
        Label('L0')
        assert CompareObjStateId(z99, 10, 0)
        """State 5: Navimesh attribute added"""
        AddNavimeshAttribute(z100, 2)
        """State 7: Closed"""
        return 0
    elif CompareObjStateId(z99, 80, 0):
        Goto('L0')
    else:
        """State 1: Waiting for the door to open"""
        assert CompareObjStateId(z99, 30, 0)
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z100, 2)
        """State 8: is open"""
        return 1
    """State 9: Guest: Exit"""
    Label('L1')
    return 2

def event_m10_10_x42(z99=10100417, z101=110000079):
    """[Lib] [Condition] King's door
    z99: King's door OBJ instance ID
    z101: Opening flag
    """
    """State 0,2: Did you approach the king's door?"""
    CompareObjPlayerDistance(0, z99, 3, 5)
    assert ConditionGroup(0)
    """State 1: Is it equipped with a king's ring? Has it been opened?"""
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    SetConditionGroup(0, 8)
    # goods:40510000:King's Ring
    DoesPlayerHaveItem(8, 40510000, 1, 3, 1, 1, 0)
    CompareEventFlag(8, z101, 1)
    if ConditionGroup(0):
        """State 4: Equipped with a king's ring"""
        return 1
    else:
        """State 3: Not qualified"""
        return 0

def event_m10_10_x43(z99=10100417, z100=100000, z101=110000079):
    """[Lib] [Execution] King's door_Open
    z99: King's door OBJ instance ID
    z100: Navigation change point ID
    z101: Opening flag
    """
    """State 0,1: Opening flag ON King's door opens"""
    SetEventFlag(z101, 1)
    ChangeOwnObjState(70)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z99, 30, 0)
    assert ConditionGroup(0)
    """State 3: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z100, 2)
    """State 4: End state"""
    return 0

def event_m10_10_x44(z99=10100417):
    """[Lib] [execution] King's door _ not open
    z99: King's door OBJ instance ID
    """
    """State 0,1: Event message display"""
    # action:2000:"Produce the symbol of the King"
    DisplayEventMessage(2000, 0, 0, 0)
    """State 2: Equipped with an or ring away from the king's door?"""
    CompareObjPlayerDistance(0, z99, 10, 3)
    # goods:40510000:King's Ring
    IsItemEquipped(0, 40510000, 1, 3)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x45(z137=_, z138=20, z139=_, z140=0, z141=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z137: Object instance ID
    z138: OBJ state ID
    z139: Navimesh switching point ID
    z140: Additional attributes
    z141: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_10_x46(z137=z137, z138=z138, z139=z139, z141=z141, z140=z140)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_10_x47(z137=z137, z138=z138, z139=z139)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_10_x48(z137=z137, z138=z138, z139=z139, z140=z140, z141=z141)
    """State 4: End state"""
    return 0

def event_m10_10_x46(z137=_, z138=20, z139=_, z141=2, z140=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z137: Target OBJ instance ID
    z138: Target OBJ state ID
    z139: Navimesh switching point ID
    z141: Additional attributes
    z140: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z137, z138, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z139, z141)
        DeleteNavimeshAttribute(z139, z140)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_10_x47(z137=_, z138=20, z139=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z137: Target OBJ instance ID
    z138: Target OBJ state ID
    z139: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z137, z138, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x48(z137=_, z138=20, z139=_, z140=0, z141=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z137: Target OBJ instance ID
    z138: Target OBJ state ID
    z139: Navimesh switching point ID
    z140: Additional attributes
    z141: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z139, z140)
    DeleteNavimeshAttribute(z139, z141)
    """State 2: End state"""
    return 0

def event_m10_10_x49(z131=102442, z132=526, z133=104170, z134=60, z135=103670, z136=65):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z131: White Phantom can appear: Global event flag
    z132: White Phantom: Generator ID
    z133: Death: Global event flag
    z134: Body: Generator group ID
    z135: Hostile: Global event flag
    z136: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z132)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z133, 1)
        CompareEventFlag(1, z135, 1)
        CompareEventFlag(2, z131, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z132)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z133, 1)
            CompareEventFlag(1, z135, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z132)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z133, 1)
            CompareEventFlag(1, z135, 1)
            HasNpcPhantomSpawned(2, z132, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z134, 0)
                HasNpcPhantomSpawned(0, z132, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z132)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m10_10_x50(z130=_):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z130: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z130)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_10_x51():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x52(z128=_, z129=_):
    """[Lib] [execute] Rebirth fire
    z128: Flag start ID
    z129: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z128, z129, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x53():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x54(z128=_, z129=_):
    """[Lib] [Preset] Rebirth
    z128: Flag start ID
    z129: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_10_x51()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_10_x53()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_10_x52(z128=z128, z129=z129)
    """State 4: End state"""
    return 0

def event_m10_10_x55(z99=10100417):
    """[Lib] [Condition] King's door closed
    z99: King's door OBJ instance ID
    """
    """State 0,1: Did you leave the king's door?"""
    CompareObjPlayerDistance(0, z99, 30, 3)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x56(z99=10100417, z100=100000):
    """[Lib] [Execution] King's door closes
    z99: King's door OBJ instance ID
    z100: Navigation change point ID
    """
    """State 0,1: The king's door closes"""
    ChangeOwnObjState(80)
    """State 2: OBJ transition wait"""
    CompareObjState(0, z99, 10, 0)
    assert ConditionGroup(0)
    """State 3: Navimesh attribute deletion"""
    AddNavimeshAttribute(z100, 2)
    """State 4: End state"""
    return 0

def event_m10_10_x57(z124=110000081, z125=102452, z126=206, z127=7440):
    """[Lib] NPC: White Phantom: Summoning Count: General
    z124: Defeat Boss 1: Area and other flags
    z125: Summon Achievement: Global Event Flag
    z126: Summon achievement count: global variable
    z127: NPC information parameter ID
    """
    """State 0,1: Summon: Start"""
    if IsGuest() != 0:
        pass
    else:
        """State 4: Summon: Achievement Judgment"""
        CompareEventFlag(0, z125, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Summon: Defeat Boss: Wait"""
            CompareEventFlag(0, z124, 1)
            assert ConditionGroup(0)
            """State 6: Summon: Count of summons"""
            AddGlobalVariable(z126, 1)
            """State 7: Summon: Achievement Judgment"""
            CompareEventFlagValue(0, 0, z126, NpcInfoValue(z127, 0), 3)
            if ConditionGroup(0):
                """State 3: Summon: Achievement setting"""
                SetEventFlag(z125, 1)
                CompareEventFlag(0, z125, 1)
                assert ConditionGroup(0)
            else:
                pass
    """State 5: Summon: System: End"""
    EndMachine()

def event_m10_10_x58(z118=102810, z119=10000010, z120=520, z121=104340, z122=0, z123=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z118: Summoning conditions: Global event flag
    z119: Summon range
    z120: Generator ID
    z121: Death: Global event flag
    z122: Appearance: Minimum time
    z123: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z121, 1)
        CompareEventFlag(8, z118, 1)
        IsPlayerInsidePoint(8, z119, z119, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z121, 1)
            CompareStateTime(1, z122, 3, z123)
            IsPlayerInsidePoint(2, z119, z119, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z120)
                HasNpcPhantomSpawned(0, z120, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_10_x59(z114=10000020, z115=521, z116=0, z117=0):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z114: Summon range
    z115: Generator ID
    z116: Appearance: Minimum time
    z117: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z114, z114, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z116, 3, z117)
        IsPlayerInsidePoint(1, z114, z114, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z115)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_10_x60(z112=_, z113=_):
    """[Lib] [Preset] Get trophy
    z112: Acquisition trigger_other flags
    z113: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z112) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z112, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z113)
    """State 4: End state"""
    return 0

def event_m10_10_x61(z102=10101050, z103=10101060, z105=201000, z108=201003, z111=15):
    """[Lib] [Execution] Interlocking elevator_Return the switch after the reference rises
    z102: Reference lift_object instance ID
    z103: Mirror lift_object instance ID
    z105: Start point ID
    z108: End point ID
    z111: Safety time
    """
    """State 0,1: Did you get off the switch?"""
    CompareObjState(8, z103, 42, 0)
    CompareObjState(8, z102, 32, 0)
    IsPlayerInsidePoint(8, z105, z108, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z102, 72)
    ChangeObjState(z103, 82)
    """State 3: Wait for switch transition"""
    CompareObjState(8, z102, 40, 0)
    CompareObjState(8, z103, 30, 0)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_10_x62(z102=10101050, z103=10101060, z105=201000, z108=201003, z110=15):
    """[Lib] [Execution] Interlocking elevator_Returns the switch after the descent
    z102: Reference lift_object instance ID
    z103: Mirror lift_object instance ID
    z105: Start point ID
    z108: End point ID
    z110: Safety time
    """
    """State 0,1: Did you get off the switch?"""
    CompareObjState(8, z103, 32, 0)
    CompareObjState(8, z102, 42, 0)
    IsPlayerInsidePoint(8, z105, z108, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z102, 82)
    ChangeObjState(z103, 72)
    """State 3: Wait for switch transition"""
    CompareObjState(8, z102, 30, 0)
    CompareObjState(8, z103, 40, 0)
    assert ConditionGroup(8)
    """State 4: End state"""
    return 0

def event_m10_10_x63(z99=10100417):
    """[Lib] [Condition] King's door_Guest
    z99: King's door OBJ instance ID
    """
    """State 0,1: Judgment of door status"""
    CompareObjState(0, z99, 30, 0)
    CompareObjState(1, z99, 10, 0)
    if ConditionGroup(0):
        """State 2: The door is open"""
        return 0
    elif ConditionGroup(1):
        """State 3: The door is closed"""
        return 1

def event_m10_10_x64(z99=10100417, z100=100000):
    """[Lib] [execution] King's door_guest_passable
    z99: King's door OBJ instance ID
    z100: Navigation change point ID
    """
    """State 0,2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z100, 2)
    """State 1: OBJ transition wait"""
    CompareObjState(0, z99, 10, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x65(z99=10100417, z100=100000):
    """[Lib] [Execution] King's door_Guest_No traffic
    z99: King's door OBJ instance ID
    z100: Navigation change point ID
    """
    """State 0,2: Navimesh attribute added"""
    AddNavimeshAttribute(z100, 2)
    """State 1: OBJ transition wait"""
    CompareObjState(0, z99, 30, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x66(z82=39):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z82: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z82, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m10_10_x67(z81=110020001, z84=4, z85=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z81: Lottery determination flag
    z84: Number of appearance judgment points
    z85: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z81, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z84)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z85, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m10_10_x68(val1=_, z96=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z96: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z96) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m10_10_x69(z92=_, z93=0, z94=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z92: Appearance judgment point ID
    z93: Minimum appearance time
    z94: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z92, z92, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z93, 3, z94)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m10_10_x70(z95=923, z97=_, z98=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z95: Generator ID
    z97: Appearance start point ID
    z98: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z95, z97, z98)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z95)
    """State 4: Finish"""
    return 0

def event_m10_10_x71(z89=110000002):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z89: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z89) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m10_10_x72(z92=_, z93=0, z94=5, z95=923, val1=_, z96=10, z97=_, z98=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z92: Intrusion detection point ID
    z93: Minimum appearance time
    z94: Maximum time to appear
    z95: Generator ID
    val1: Appearance judgment number
    z96: Lottery result point variable
    z97: Appearance start point ID
    z98: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m10_10_x68(val1=val1, z96=z96)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m10_10_x69(z92=z92, z93=z93, z94=z94)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m10_10_x70(z95=z95, z97=z97, z98=z98)
    """State 4: Finish"""
    return 0

def event_m10_10_x73(z90=923, mode2=0):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z90: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z90)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode2) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m10_10_x74(z89=110000002, z91=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z89: Defeat flag
    z91: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z89, 1)
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
                    SetEventFlag(z91, 1)
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

def event_m10_10_x75(z89=110000002, z90=923, mode2=0):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z89: Defeat flag
    z90: Generator ID
    mode2: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m10_10_x71(z89=z89)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m10_10_x73(z90=z90, mode2=mode2)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m10_10_x74(z89=z89, z91=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m10_10_x74(z89=z89, z91=102755)
    """State 5: End state"""
    return 0

def event_m10_10_x76(z87=9100, z88=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z87: Generator ID
    z88: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z87, z88)
    """State 2: End state"""
    return 0

def event_m10_10_x77(z87=9100, z88=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z87: Generator ID
    z88: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z87, z88, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_10_x78(z87=9100):
    """[Lib] [DC] [Condition] Transparent characters
    z87: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z87)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x79(z87=9100, z88=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z87: Generator ID
    z88: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_10_x77(z87=z87, z88=z88)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_10_x78(z87=z87)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_10_x76(z87=z87, z88=z88)
    """State 4: End state"""
    return 0

def event_m10_10_x80(z81=110020001, z85=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z81: Lottery determination flag
    z85: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z81, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z85, 0)
    """State 3: End state"""
    return 0

def event_m10_10_x81(z81=110020001, z83=110000002, z86=100804):
    """[Lib] [DC] [Reproduction] Wanderer_Random lottery_Global flag version
    z81: Lottery determination flag
    z83: Defeat flag
    z86: Condition judgment flag
    """
    """State 0,5: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L2')
    """State 4: Are the appearance conditions satisfied?"""
    if GetEventFlag(z86) != 1:
        pass
    else:
        Goto('L0')
    """State 10: Condition not achieved: Cannot appear"""
    return 4
    """State 3: Already destroyed?"""
    Label('L0')
    if GetEventFlag(z83) != 0:
        pass
    else:
        Goto('L1')
    """State 9: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L1')
    if GetEventFlag(z81) != 0:
        """State 7: Lottery completed"""
        return 1
    else:
        """State 6: Not drawn"""
        return 0
    """State 8: Guest: Exit"""
    Label('L2')
    return 2

def event_m10_10_x82(z81=110020001, z82=39, z83=110000002, z84=4, z85=10, z86=100804):
    """[Lib] [DC] [Preset] Wanderer_Random lottery_Global flag version
    z81: Lottery determination flag
    z82: Random number comparison value
    z83: Defeat flag
    z84: Number of appearance judgment points
    z85: Lottery result point variable
    z86: Condition judgment flag
    """
    """State 0,4: [Lib] [DC] [Reproduction] Wanderer_Random lottery_Global flag version_SubState"""
    call = event_m10_10_x81(z81=z81, z83=z83, z86=z86)
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
        call = event_m10_10_x66(z82=z82)
        if call.Get() == 0:
            """State 1: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m10_10_x67(z81=z81, z84=z84, z85=z85)
        elif call.Get() == 1:
            """State 3: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m10_10_x80(z81=z81, z85=z85)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m10_10_x83(z78=110000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z78: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z78) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_10_x84(z79=857):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z79: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z79, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x85(z80=110020084):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z80: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z80, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x86(z78=110000081, z79=857, z80=110020084):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z78: Boss destruction flag
    z79: Boss generator ID
    z80: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_10_x83(z78=z78)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_10_x84(z79=z79)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_10_x85(z80=z80)
    """State 4: End state"""
    return 0

def event_m10_10_x87():
    """[Net] Duel matching cancellation"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x88(z73=10101500):
    """[Condition] Check OBJ and warp between maps
    z73: OBJ instance ID to check
    """
    """State 0,1: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z73, 0)
    """State 2: Was OBJ checked or multi?"""
    IsObjSearched(0, z73)
    IsMultiplayer(1, 1, 1)
    if ConditionGroup(1):
        """State 5: Key guide disabled"""
        return 1
    elif ConditionGroup(0):
        """State 4: Warp execution"""
        return 0

def event_m10_10_x89(z73=10101500, z74=101010, z75=101620, z76=10160000, z77=100000):
    """[Execution] Inter-map warp_warp execution after checking OBJ
    z73: OBJ instance ID to check
    z74: Pre-warp poly play ID
    z75: Poly Play ID after Warp
    z76: Map ID
    z77: Point ID
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z73, 1)
    """State 2: Multiplayer prohibited state: ON"""
    ProhibitMultiplayer(1)
    """State 3: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_10_x1(z68=z74, z69=z75, z70=z76, z71=z77)
    """State 4: End state"""
    return 0

def event_m10_10_x90(z73=10101500, z74=101010, z75=101620, z76=10160000, z77=100000):
    """[Preset] Check OBJ and warp between maps
    z73: OBJ instance ID to check
    z74: Pre-warp poly play ID
    z75: Poly Play ID after Warp
    z76: Map ID
    z77: Point ID
    """
    """State 0,2: [Reproduction] Inter-map warp_empty_SubState by examining OBJ"""
    assert event_m10_10_x87()
    """State 3: [Condition] Inter-map warp_SubState by checking OBJ"""
    call = event_m10_10_x88(z73=z73)
    if call.Get() == 1:
        """State 5: [Execution] Check OBJ, warp between maps_Key guide invalidation only_SubState"""
        assert event_m10_10_x91(z73=z73)
        """State 1: Rerun"""
        RestartMachine()
    elif call.Done():
        """State 4: [Execution] Inter-map warp_warp execution_SubState by checking OBJ"""
        assert event_m10_10_x89(z73=z73, z74=z74, z75=z75, z76=z76, z77=z77)
        """State 6: End state"""
        return 0

def event_m10_10_x91(z73=10101500):
    """[Execution] Checking OBJ and only warping between maps_key guide invalidation
    z73: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z73, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x92(z67=_):
    """[Reproduction] Memory invasion of giants
    z67: OBJ instance ID to check
    """
    """State 0,1: OBJ state initialization"""
    InitializeObj(z67)
    """State 2: End state"""
    return 0

def event_m10_10_x93(z67=_):
    """[Condition] Memory invasion of giant
    z67: OBJ instance ID to check
    """
    """State 0,1: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 3: Activate key guide"""
    DisableObjKeyGuide(z67, 0)
    """State 2: Was OBJ checked or multi?"""
    IsObjSearched(0, z67)
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

def event_m10_10_x94(z67=_, z68=_, z69=0, z70=20100000, z71=_, z72=_):
    """[Execution] Giant's memory intrusion
    z67: OBJ instance ID to check
    z68: Pre-warp poly play ID
    z69: Poly Play ID after Warp
    z70: Map ID
    z71: Point ID
    z72: Global flag for warp
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z67, 1)
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
    SetEventFlag(z72, 1)
    """State 6: [Lib] Warp between maps after poly play_SubState"""
    assert event_m10_10_x1(z68=z68, z69=z69, z70=z70, z71=z71)
    """State 7: End state"""
    return 0

def event_m10_10_x95(z67=_):
    """[Execution] Giant's memory intrusion_Key guide invalidation
    z67: OBJ instance ID to check
    """
    """State 0,1: Disable key guide"""
    DisableObjKeyGuide(z67, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x96(z67=_, z68=_, z69=0, z70=20100000, z71=_, z72=_):
    """[Preset] Memory invasion of giants
    z67: OBJ instance ID to check
    z68: Pre-warp poly play ID
    z69: Poly Play ID after Warp
    z70: Map ID
    z71: Point ID
    z72: Global flag for warp
    """
    """State 0,1: [Reproduction] Giant's memory intrusion_SubState"""
    assert event_m10_10_x92(z67=z67)
    """State 4: [Condition] Memory intrusion of giants_SubState"""
    call = event_m10_10_x93(z67=z67)
    if call.Get() == 1:
        """State 3: [Execution] Giant's memory intrusion_Key guide invalidation_SubState"""
        assert event_m10_10_x95(z67=z67)
    elif call.Get() == 0:
        """State 2: [Execution] Giant's memory intrusion_SubState"""
        assert event_m10_10_x94(z67=z67, z68=z68, z69=z69, z70=z70, z71=z71, z72=z72)
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

def event_m10_10_x102(z65=10100415, z66=520000):
    """[Preset] Key door that opens with "Welcome Key" (can be broken)
    z65: Door OBJ instance ID
    z66: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Lock door opened with "Welcome Key" (breakable) _SubState"""
    call = event_m10_10_x103(z65=z65)
    if call.Get() == 0:
        """State 2: [Condition] The key door that opens with "Welcome Key" (can be broken) _SubState"""
        assert event_m10_10_x104(z65=z65)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Key door opened with "Welcome Key" (breakable) _SubState"""
    assert event_m10_10_x105(z66=z66)
    """State 4: End state"""
    return 0

def event_m10_10_x103(z65=10100415):
    """[Reproduction] The key door that opens with the “Welcome Key” (can be broken)
    z65: Door OBJ instance ID
    """
    """State 0,1: Check the status of the door OBJ"""
    if CompareObjStateId(z65, 21, 1):
        """State 2: [Lib] Item specified door unlocking_SubState"""
        assert event_m10_10_x6(z174=1005, z175=1105, z176=50600000, z177=110000074)
        """State 3: Undestructed"""
        return 0
    else:
        """State 4: Destroyed"""
        return 1

def event_m10_10_x104(z65=10100415):
    """[Conditions] Lock door opened with "Welcome Key" (breakable)
    z65: Door OBJ instance ID
    """
    """State 0,1: Was the door destroyed?"""
    CompareObjState(0, z65, 21, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x105(z66=520000):
    """[Execution] Key door opened with "Welcome Key" (breakable)
    z66: Point ID for Navimesh change
    """
    """State 0,1,2: End state"""
    return 0

def event_m10_10_x106(z60=102443, z61=1100000, z62=1100001, z63=10101160, z64=1100002):
    """[Preset] Switch that closes the door
    z60: Closed area intrusion detection flag
    z61: Start point ID for closure
    z62: Closing end point ID
    z63: Instance ID of the iron lattice OBJ
    z64: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Switch that closes the door_SubState"""
    call = event_m10_10_x107(z60=z60, z64=z64)
    if call.Get() == 0:
        """State 2: [Condition] Switch that closes the door_SubState"""
        assert event_m10_10_x108(z61=z61, z62=z62)
        """State 3: [Execution] Switch that closes the door_SubState"""
        assert event_m10_10_x109(z63=z63, z64=z64, z60=z60)
    elif call.Done():
        pass
    """State 4: End state"""
    return 0

def event_m10_10_x107(z60=102443, z64=1100002):
    """[Reproduction] Switch that closes the door
    z60: Closed area intrusion detection flag
    z64: Point ID for Navimesh change
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
    if GetEventFlag(z60) != 0:
        """State 3: Navigation mesh change"""
        AddNavimeshAttribute(z64, 2)
        """State 5: Closed"""
        return 1
    else:
        """State 4: is open"""
        return 0

def event_m10_10_x108(z61=1100000, z62=1100001):
    """[Condition] Switch that closes the door
    z61: Start point ID for closure
    z62: Closing end point ID
    """
    """State 0,1: Did you enter the area?"""
    IsPlayerInsidePoint(0, z61, z62, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x109(z63=10101160, z64=1100002, z60=102443):
    """[Execution] Switch that closes the door
    z63: Instance ID of the iron lattice OBJ
    z64: Point ID for Navimesh change
    z60: Closed area intrusion detection flag
    """
    """State 0,2: Close the bar"""
    ChangeObjState(z63, 70)
    CompareObjState(0, z63, 30, 0)
    assert ConditionGroup(0)
    """State 1: Navigation mesh change"""
    AddNavimeshAttribute(z64, 2)
    """State 3: Turn on the flag"""
    SetEventFlag(z60, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x110(z58=110010042, z59=10100413):
    """[Preset] Enemy door opening control
    z58: Opening flag for soldiers who open doors
    z59: Door OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemy door opening control_SubState"""
    call = event_m10_10_x111()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Enemy door opening control_SubState"""
        call = event_m10_10_x112(z59=z59)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
        """State 3: [Execution] Enemy door opening control_SubState"""
        assert event_m10_10_x113(z58=z58)
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

def event_m10_10_x112(z59=10100413):
    """[Condition] Enemy door opening control
    z59: Door OBJ instance ID
    """
    """State 0,1: Is the door closed?"""
    CompareObjState(0, z59, 10, 0)
    if ConditionGroup(0):
        """State 2: Is the door OBJ damaged?"""
        IsObjDamaged(0, z59, -1, -4, 0)
        assert ConditionGroup(0)
        """State 3: Door not open"""
        return 0
    else:
        """State 4: Door open"""
        return 1

def event_m10_10_x113(z58=110010042):
    """[Execution] Enemy door opening control
    z58: Opening flag for soldiers who open doors
    """
    """State 0,1: Door open soldier activation flag ON"""
    SetEventFlag(z58, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x114(z55=1200000, z56=1200000, z57=10101700):
    """[Preset] Oiwa Gorokuro
    z55: Start point ID
    z56: End point ID
    z57: Instance ID of rock OBJ
    """
    """State 0,1: [Reproduction] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x115()
    """State 2: [Condition] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x116(z55=z55, z56=z56)
    """State 3: [Execution] Oiwa Gorokuro_SubState"""
    assert event_m10_10_x117(z57=z57)
    """State 4: End state"""
    return 0

def event_m10_10_x115():
    """[Reproduction] Oiwa Gorokuro"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x116(z55=1200000, z56=1200000):
    """[Conditions] Oiwa Gorokuro
    z55: Start point ID
    z56: End point ID
    """
    """State 0,1: Entered the specified area"""
    IsPlayerInsidePoint(0, z55, z56, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x117(z57=10101700):
    """[Execution] Oiwa Gorokuro
    z57: Instance ID of rock OBJ
    """
    """State 0,1: Rocky run"""
    ChangeObjState(z57, 70)
    assert CompareObjStateId(z57, 20, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x118(z50=3100, z51=3110, z52=3150, z53=3160, z54=10101002):
    """[Preset] Flame that disappears when salamander is annihilated
    z50: Generator ID of salamander 1 that performs death determination
    z51: Salamander 2 generator ID for mortality determination
    z52: Salamander 3 generator ID for mortality determination
    z53: Generator ID of salamander 4 that performs death determination
    z54: OBJ instance ID of the flame blowing out from the ground
    """
    """State 0,1: [Reproduction] Flame that disappears when Salamander annihilates _SubState"""
    assert event_m10_10_x119()
    """State 2: [Condition] Flame that disappears when Salamander annihilates _SubState"""
    assert event_m10_10_x120(z50=z50, z51=z51, z52=z52, z53=z53)
    """State 3: [Execution] Flame that disappears when Salamander annihilates _SubState"""
    assert event_m10_10_x121(z54=z54)
    """State 4: End state"""
    return 0

def event_m10_10_x119():
    """[Reproduction] Flame that disappears when Salamander annihilates"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x120(z50=3100, z51=3110, z52=3150, z53=3160):
    """[Condition] Flame that disappears when salamander is annihilated
    z50: Generator ID of salamander 1 that performs death determination
    z51: Salamander 2 generator ID for mortality determination
    z52: Salamander 3 generator ID for mortality determination
    z53: Generator ID of salamander 4 that performs death determination
    """
    """State 0,1: Salamander death determination"""
    IsChrDeadOrRespawnOver(8, z50, 1)
    IsChrDeadOrRespawnOver(8, z51, 1)
    IsChrDeadOrRespawnOver(8, z52, 1)
    IsChrDeadOrRespawnOver(8, z53, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_10_x121(z54=10101002):
    """[Execution] Flame that disappears when Salamander is annihilated
    z54: OBJ instance ID of the flame blowing out from the ground
    """
    """State 0,1: Stop the flame blowing from the ground"""
    ChangeObjState(z54, 30)
    """State 2: End state"""
    return 0

def event_m10_10_x122(z25=106200, z26=10101120):
    """[Preset] Giant tree nut drawing process
    z25: Giant tree nut generation flag
    z26: Giant Tree OBJ Instance ID
    """
    """State 0,1: [Reproduction] Giant tree nut drawing process_SubState"""
    call = event_m10_10_x123(z25=z25, z26=z26)
    if call.Get() == 1:
        """State 4: [Condition] Giant tree nut drawing process_Generation_SubState"""
        assert event_m10_10_x151(z25=z25)
        """State 5: [Execution] Giant tree nut drawing process_Generation_SubState"""
        assert event_m10_10_x152(z26=z26)
    elif call.Get() == 0:
        """State 2: [Condition] Giant tree nut drawing process_SubState"""
        assert event_m10_10_x124(z26=z26)
        """State 3: [Execution] Giant tree nut drawing process_SubState"""
        assert event_m10_10_x125(z26=z26)
    """State 6: End state"""
    return 0

def event_m10_10_x123(z25=106200, z26=10101120):
    """[Reproduction] Giant tree nut drawing process
    z25: Giant tree nut generation flag
    z26: Giant Tree OBJ Instance ID
    """
    """State 0,1: Judgment status of giant tree nuts"""
    if GetEventFlag(z25) != 0:
        """State 3: To generation judgment processing"""
        return 1
    else:
        """State 2: To drawing stop processing"""
        return 0

def event_m10_10_x124(z26=10101120):
    """[Condition] Giant tree nut drawing process
    z26: Giant Tree OBJ Instance ID
    """
    """State 0,1: Is OBJ active?"""
    IsObjActive(0, z26, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x125(z26=10101120):
    """[Execution] Giant tree nut drawing process
    z26: Giant Tree OBJ Instance ID
    """
    """State 0,1: Stop producing nuts"""
    ActivateObjItem(z26, 0)
    """State 2: Is OBJ no longer active?"""
    IsObjActive(0, z26, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_10_x126():
    """[Reproduction] Vegrant_Initial layout change"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x127(z49=110000087):
    """[Condition] Vagrant_Initial location change
    z49: Flag to perform first battle or rematch determination
    """
    """State 0,1: Is it the first game? Is it a rematch?"""
    CompareEventFlag(0, z49, 0)
    if ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m10_10_x128(z46=853, z47=602000, z48=2):
    """[Execution] Vagrant_Initial location change
    z46: Vagrant generator ID
    z47: Point ID for relocation during rematch
    z48: Activation state ID at the time of rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z46, z47)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z46, z48)
    """State 3: End state"""
    return 0

def event_m10_10_x129(z46=853, z47=602000, z48=2, z49=110000087):
    """[Preset] Vagrant_Initial location change
    z46: Vagrant generator ID
    z47: Point ID for relocation during rematch
    z48: Activation state ID at the time of rematch
    z49: Flag for judging first battle or rematch
    """
    """State 0,1: [Reproduction] Vagrant_Initial layout change_SubState"""
    assert event_m10_10_x126()
    """State 3: [Condition] Vagrant_Initial location change_SubState"""
    call = event_m10_10_x127(z49=z49)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 2: [Execution] Vagrant_Initial placement change_SubState"""
        assert event_m10_10_x128(z46=z46, z47=z47, z48=z48)
    """State 4: End state"""
    return 0

def event_m10_10_x130(z14=110000020, z16=10101900, z17=2255):
    """[Execution] Vegrant appeared with hawk
    z14: Vegrant event executed flag
    z16: Hawk OBJ instance ID
    z17: Generator ID
    """
    """State 0,1: Starting approach of hawk: 70"""
    ChangeObjState(z16, 70)
    """State 3: Waiting for release of startup state"""
    CompareChrStartUpState(0, z17, 3, 1)
    assert ConditionGroup(0)
    """State 2: Event executed flag ON"""
    SetEventFlag(z14, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x131(z42=110000020, z44=100968):
    """[Condition] Hide hawk OBJ
    z42: Vegrant event executed flag
    z44: Vagrant Defeat Flag
    """
    """State 0,1: Has the event occurred?"""
    if GetEventFlag(z42) != 0:
        pass
    else:
        Goto('L0')
    """State 4: Event has occurred"""
    return 1
    """State 2: Is the Vegrant defeated?"""
    Label('L0')
    if GetEventFlag(z44) != 0:
        """State 5: Vegrant defeated"""
        return 2
    else:
        """State 3: No event occurred"""
        return 0

def event_m10_10_x132():
    """[Reproduction] Hidden hawk OBJ_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x133(z43=10101900, z45=_):
    """[Execution] Hide hawk OBJ
    z43: Hawk OBJ instance ID
    z45: Hawk OBJ State
    """
    """State 0,1: State transition of hawk OBJ"""
    ChangeObjState(z43, z45)
    """State 2: End state"""
    return 0

def event_m10_10_x134(z42=110000020, z43=10101900, z44=100968):
    """[Preset] Hide hawk OBJ
    z42: Vegrant event executed flag
    z43: Hawk OBJ instance ID
    z44: Vagrant Defeat Flag
    """
    """State 0,1: [Reproduction] Hidden hawk OBJ_Sky_SubState"""
    assert event_m10_10_x132()
    """State 3: [Condition] Hide hawk OBJ_SubState"""
    call = event_m10_10_x131(z42=z42, z44=z44)
    if call.Get() == 1:
        """State 4: [Execution] Hide hawk OBJ_2_SubState"""
        assert event_m10_10_x133(z43=z43, z45=20)
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 2: [Execution] Hidden OBJ_SubState"""
        assert event_m10_10_x133(z43=z43, z45=30)
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

def event_m10_10_x136(z37=110000087):
    """[Reproduction] Vegrant _ poly play reproduction
    z37: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z37) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m10_10_x137(z40=10100610, z41=110000086):
    """[Conditions] Vegrant_Poly play
    z40: White door OBJ instance ID
    z41: Boss destroy other flags
    """
    """State 0,1: Defeated Vegrant on the way through the white door"""
    if GetEventFlag(z41) != 0:
        """State 3: Defeating Vagrant on the way: No poly play"""
        return 1
    elif CompareObjStateId(z40, 100, 0):
        """State 2: White door passing"""
        return 0

def event_m10_10_x138(z36=101030, z37=110000087, z38=601000, z39=1):
    """[Execution] Vegrant _ poly play
    z36: Poly play ID
    z37: Poly drama played flag
    z38: Warp point ID
    z39: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z36, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z37, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z38)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m10_10_x139(z36=101030, z37=110000087, z38=601000, z39=1, z40=10100610, z41=110000086):
    """[Preset] Vegrant_Poly Play
    z36: Poly play ID
    z37: Poly drama played flag
    z38: Warp point ID
    z39: Weight until poly play
    z40: White door OBJ instance ID
    z41: Boss destroy other flags
    """
    """State 0,1: [Reproduction] Vegrant_Poly Play_SubState"""
    call = event_m10_10_x136(z37=z37)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Conditions] Vegrant_Poly Play_SubState"""
        call = event_m10_10_x137(z40=z40, z41=z41)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Vegrant_Poly Play_SubState"""
            assert event_m10_10_x138(z36=z36, z37=z37, z38=z38, z39=z39)
    """State 4: End state"""
    return 0

def event_m10_10_x140(z30=110000086):
    """[Reproduction] Boss: Battle of Vegrant_Start
    z30: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z30) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_10_x141(z31=600000, z32=600000, z30=110000086):
    """[Conditions] Boss: Battle of Vegrant_Start
    z31: Start point ID
    z32: End point ID
    z30: Defeat other flags
    """
    """State 0,1: Did you enter the boss room point? or Destroyed Vagrant on the way?"""
    IsPlayerInsidePoint(8, z31, z32, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z31, z32, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    CompareEventFlag(1, z30, 1)
    if ConditionGroup(0):
        """State 2: Entered the point"""
        return 0
    elif ConditionGroup(1):
        """State 3: Defeat Vegrant on the way"""
        return 1

def event_m10_10_x142(z33=102, z34=1010000, z35=110020085):
    """[Execution] Boss: Battle against Vegrant _Start
    z33: Sound ID
    z34: Boss Battle ID
    z35: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z33)
    """State 1: Boss battle start notification"""
    StartBossFight(z34)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z35, 1)
    """State 4: End state"""
    return 0

def event_m10_10_x143():
    """[Reproduction] Boss: Vegrant Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x144(z34=1010000):
    """[Conditions] Boss: Vegrant Battle_End Judgment
    z34: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z34, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x145(z33=102, z34=1010000, z35=110020085, mode1=0):
    """[Execution] Boss: Battle of Vegrant _End
    z33: Sound ID
    z34: Boss Battle ID
    z35: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z35, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z34)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode1) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z33)
    """State 5: End state"""
    return 0

def event_m10_10_x146(z30=110000086, z31=600000, z32=600000, z33=102, z34=1010000, z35=110020085, mode1=0):
    """[Preset] Boss: Battle against Vegrant _Start
    z30: Boss destruction flag
    z31: Start point ID
    z32: End point ID
    z33: Sound ID
    z34: Boss Battle ID
    z35: Other flags for logic
    mode1: BGM stop time
    """
    """State 0,1: [Reproduction] Boss: Vegrant Battle_Start_SubState"""
    call = event_m10_10_x140(z30=z30)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss: Vegrant Battle_Start_SubState"""
        call = event_m10_10_x141(z31=z31, z32=z32, z30=z30)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 3: [Execution] Boss: Vegrant Battle_Start_SubState"""
            assert event_m10_10_x142(z33=z33, z34=z34, z35=z35)
            """State 2: [Reproduction] Boss: Vegrant Battle_Sky_SubState"""
            assert event_m10_10_x143()
            """State 6: [Condition] Boss: Vegrant Battle_End Judgment_SubState"""
            assert event_m10_10_x144(z34=z34)
            """State 4: [Execution] Boss: Vegrant Battle_End_SubState"""
            assert event_m10_10_x145(z33=z33, z34=z34, z35=z35, mode1=mode1)
    """State 7: End state"""
    return 0

def event_m10_10_x147(z27=110000082, z28=857, z29=652000):
    """[Preset] New Giant Senior Soldier
    z27: Flag to perform first battle or rematch determination
    z28: New Giant Senior Soldier Generator ID
    z29: Point ID for relocation during rematch
    """
    """State 0,1: [Reproduction] New Giant Senior Soldier_Initial Location Change_SubState"""
    assert event_m10_10_x148()
    """State 2: [Conditions] New Giant Senior Soldier_Initial Location Change_SubState"""
    call = event_m10_10_x149(z27=z27)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Execution] New Giant Senior Soldier_Initial Location Change_Rematch_SubState"""
        assert event_m10_10_x150(z28=z28, z29=z29)
    """State 4: End state"""
    return 0

def event_m10_10_x148():
    """[Reproduction] New Giant Senior Soldier"""
    """State 0,1: End state"""
    return 0

def event_m10_10_x149(z27=110000082):
    """[Conditions] New Giant Senior Soldier
    z27: Flag to perform first battle or rematch determination
    """
    """State 0,1: Is it the first game? Is it a rematch?"""
    CompareEventFlag(0, z27, 0)
    if ConditionGroup(0):
        """State 2: First match"""
        return 0
    else:
        """State 3: rematch"""
        return 1

def event_m10_10_x150(z28=857, z29=652000):
    """[Execution] New Giant Senior Soldier
    z28: New Giant Senior Soldier Generator ID
    z29: Point ID for relocation during rematch
    """
    """State 0,1: Boss placement during rematch"""
    OverrideGeneratorStartPosition(z28, z29)
    """State 2: Start state change"""
    OverrideGeneratorStartupState(z28, 0)
    """State 3: End state"""
    return 0

def event_m10_10_x151(z25=106200):
    """[Condition] Giant tree fruit drawing process
    z25: Giant tree nut generation flag
    """
    """State 0,1: Judgment status of giant tree nuts"""
    CompareEventFlag(0, z25, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x152(z26=10101120):
    """[Execution] Giant tree fruit drawing process
    z26: Giant Tree OBJ Instance ID
    """
    """State 0,1: Stop producing nuts"""
    ActivateObjItem(z26, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x153(z22=110000020):
    """[Reproduction] Vegrant appeared with a hawk _ Character
    z22: Vegrant event executed flag
    """
    """State 0,1: Has the event occurred?"""
    if GetEventFlag(z22) != 0:
        """State 3: Event has occurred"""
        return 1
    else:
        """State 2: No event occurred"""
        return 0

def event_m10_10_x154(z24=2255):
    """[Condition] Vegrant appeared with a hawk _ Character
    z24: Generator ID
    """
    """State 0,1: Is it in startup state?"""
    CompareChrStartUpState(0, z24, 3, 0)
    CompareChrStartUpState(1, z24, 3, 1)
    if ConditionGroup(0):
        """State 2: During startup state: Attach"""
        return 0
    elif ConditionGroup(1):
        """State 3: Normal state: Do nothing"""
        return 1

def event_m10_10_x155(z23=10101900):
    """[Execution] Vagrant Appearance with Hawk _ Character
    z23: Hawk OBJ instance ID
    """
    """State 0,1: Character attach to hawk OBJ"""
    AttachCharacterToObj(z23, 6, 2)
    """State 2: Finish"""
    return 0

def event_m10_10_x156(z22=110000020, z23=10101900, z24=2255):
    """[Preset] hawk bay grant appearance _ character
    z22: Vegrant event executed flag
    z23: Hawk OBJ instance ID
    z24: Generator ID
    """
    """State 0,3: [Reproduction] Vegrant Appears with Hawk _ Character _ SubState"""
    call = event_m10_10_x153(z22=z22)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Vegrant appeared with hawks_Character_SubState"""
        call = event_m10_10_x154(z24=z24)
        if call.Get() == 0:
            """State 4: [Execution] Vagrant Appears in Hawk_Character_SubState"""
            assert event_m10_10_x155(z23=z23)
        elif call.Get() == 1:
            pass
    """State 1: Waiting for release of startup state"""
    CompareChrStartUpState(0, z24, 3, 1)
    assert ConditionGroup(0)
    """State 2: Forced detach"""
    DetachCharacterFromObj()
    """State 6: End state"""
    return 0

def event_m10_10_x157(z14=110000020):
    """[Reproduction] Vegrant appeared with hawk
    z14: Vegrant event executed flag
    """
    """State 0,1: Has the event occurred?"""
    if GetEventFlag(z14) != 0:
        """State 3: Event has occurred"""
        return 1
    else:
        """State 2: No event occurred"""
        return 0

def event_m10_10_x158(z17=2255):
    """[Condition] Vegrant appearance with hawk _ generation determination
    z17: Generator ID
    """
    """State 0,1: Has a character been generated?"""
    IsChrActive(0, z17, 1)
    assert ConditionGroup(0)
    """State 2: Finish"""
    return 0

def event_m10_10_x159(z14=110000020, z15=100968, z16=10101900, z17=2255, z18=1500001, z19=1500001, z20=110020022,
                      z21=110000086):
    """[Preset] Vagrant appears with hawk
    z14: Vegrant event executed flag
    z15: Defeat global flag
    z16: Hawk OBJ instance ID
    z17: Generator ID
    z18: Start point ID
    z19: End point ID
    z20: Vagrant return flag
    z21: Defeat other flags
    """
    """State 0,1: [Reproduction] Vegrant Appears in the Hawk_SubState"""
    call = event_m10_10_x157(z14=z14)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Vagrant Appearance with Hawk_Generation Determination_SubState"""
        assert event_m10_10_x158(z17=z17)
        """State 2: [Execution] Vagrant Appears in Hawk_SubState"""
        assert event_m10_10_x130(z14=z14, z16=z16, z17=z17)
    """State 4: End state"""
    return 0

def event_m10_10_x160(z13=2255):
    """[Condition] Vegrant appeared with hawk_deletion judgment
    z13: Generator ID
    """
    """State 0,2: Has a vegrant been generated?"""
    IsChrActive(0, z13, 1)
    assert ConditionGroup(0)
    """State 1: Has Vegrant finished the return action?"""
    CompareChrEzStateValue(0, z13, 7, 1, 0)
    IsChrActive(1, z13, 0)
    if ConditionGroup(0):
        """State 3: Returned"""
        return 0
    elif ConditionGroup(1):
        """State 4: Out of drawing"""
        return 1

def event_m10_10_x161(z13=2255):
    """[Execution] Vagrant Appearance with Hawk
    z13: Generator ID
    """
    """State 0,1: Delete character"""
    DeleteEnemyByGenerator(z13, 0)
    """State 2: End state"""
    return 0

def event_m10_10_x162(z13=2255):
    """[Preset] Vegrant removal judgment
    z13: Generator ID
    """
    """State 0,3: [Reproduction] Vegrant deletion judgment_SubState"""
    call = event_m10_10_x135()
    if call.Get() == 0:
        """State 2: [Condition] Vegrant deletion determination_SubState"""
        call = event_m10_10_x160(z13=z13)
        if call.Get() == 0:
            """State 1: [Execution] Vegrant deletion determination_SubState"""
            assert event_m10_10_x161(z13=z13)
        elif call.Get() == 1:
            """State 5: Rerun"""
            return 1
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_10_x163(lot1=60008000, z9=110000086, z10=100968, z12=110000024):
    """[Execution] Vagrant Appearance with a Hawk_Reward
    lot1: Item lottery ID
    z9: Defeat other flags
    z10: Defeat global flag
    z12: Destroying flag of the appearance event
    """
    """State 0,1: Reward acquisition"""
    # lot:60008000:Soul of the Pursuer
    AwardItem(lot1, 1)
    """State 2: Boss Defeat Flag ON and Defeat Count +1"""
    SetEventFlag(z9, 1)
    SetEventFlag(z10, 1)
    SetEventFlag(z12, 1)
    # bonfire:10655:Cardinal Tower
    SetGlobalVariable(28, GetBonfireAsceticCount(10655) + 1)
    """State 3: End state"""
    return 0

def event_m10_10_x164(z12=110000024):
    """[Reproduction] Vegrant Appearance with a Hawk_Reward
    z12: Destroying flag of the appearance event
    """
    """State 0,1: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L0')
    """State 2: Has it been defeated by the hawk appearance event?"""
    if GetEventFlag(z12) != 0:
        """State 5: Defeated"""
        return 2
    else:
        """State 3: host"""
        return 0
    """State 4: The guests"""
    Label('L0')
    return 1

def event_m10_10_x165(z11=2255):
    """[Condition] Vegrant Appears with a Hawk_Reward
    z11: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z11)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x166(lot1=60008000, z9=110000086, z10=100968, z11=2255, z12=110000024):
    """[Preset] Vagrant Appearance with a Hawk_Reward
    lot1: Item lottery ID
    z9: Defeat other flags
    z10: Defeat global flag
    z11: Generator ID
    z12: Destroying flag of the appearance event
    """
    """State 0,1: [Reproduction] Vegrant Appears with Hawk_Reward_SubState"""
    call = event_m10_10_x164(z12=z12)
    if call.Get() == 1:
        pass
    elif call.Get() == 2:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] Vegrant Appears in Hawk_Reward_SubState"""
        assert event_m10_10_x165(z11=z11)
        """State 2: [Execution] Vagrant Appearance with Hawk_Reward_SubState"""
        assert event_m10_10_x163(lot1=lot1, z9=z9, z10=z10, z12=z12)
    """State 4: End state"""
    return 0

def event_m10_10_x167(z5=10101120, z6=106200):
    """[Reproduction] Giant tree fruit_message
    z5: Giant Tree OBJ Instance ID
    z6: Generation determination flag
    """
    """State 0,3: Giant Tree Initialization: 10"""
    ChangeObjState(z5, 10)
    DisableObjKeyGuide(z5, 1)
    assert CompareObjStateId(z5, 10, 0)
    """State 1: Judgment status of giant tree nuts"""
    if GetEventFlag(z6) != 0:
        """State 4: Generating"""
        return 0
    else:
        """State 2: Giant Tree Key Guide Valid: 31"""
        ChangeObjState(z5, 31)
        DisableObjKeyGuide(z5, 0)
        assert CompareObjStateId(z5, 31, 0)
        """State 5: Not generated"""
        return 1

def event_m10_10_x168(z5=10101120, z6=106200):
    """[Condition] Giant Tree Fruit_Message
    z5: Giant Tree OBJ Instance ID
    z6: Generation determination flag
    """
    """State 0,1: Wait to examine"""
    IsObjSearched(0, z5)
    CompareEventFlag(1, z6, 1)
    if ConditionGroup(1):
        """State 3: Generated"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m10_10_x169(z5=10101120):
    """[Execution] Giant Tree Fruit_Message
    z5: Giant Tree OBJ Instance ID
    """
    """State 0,3: Disable key guide"""
    DisableObjKeyGuide(z5, 1)
    """State 1: Message display"""
    # action:2007:"A Giant rests in peace"
    DisplayEventMessage(2007, 0, 0, 0)
    assert EventMessageDisplay() != 0
    """State 2: Message waiting waiting"""
    assert EventMessageDisplay() != 1
    """State 4: End state"""
    return 0

def event_m10_10_x170(z5=10101120, z6=106200):
    """[Preset] Giant Tree Fruit_Message
    z5: Giant Tree OBJ Instance ID
    z6: Generation determination flag
    """
    """State 0,1: [Reproduction] Giant Tree Fruit_Message_SubState"""
    call = event_m10_10_x167(z5=z5, z6=z6)
    if call.Get() == 0:
        """State 4: [Condition] Giant tree fruit_Message_Waiting_SubState"""
        assert event_m10_10_x177(z6=z6)
    elif call.Get() == 1:
        """State 3: [Condition] Giant tree fruit_Message_SubState"""
        call = event_m10_10_x168(z5=z5, z6=z6)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Execution] Giant Tree Fruit_Message_SubState"""
            assert event_m10_10_x169(z5=z5)
    """State 5: End state"""
    return 0

def event_m10_10_x171(z7=106200, z8=10101120):
    """[Reproduction] Giant tree fruit_system version
    z7: Giant tree nut generation flag
    z8: Giant Tree OBJ Instance ID
    """
    """State 0,1: Judgment status of giant tree nuts"""
    if GetEventFlag(z7) != 0:
        """State 3: Acquisition judgment"""
        return 1
    else:
        """State 2: Generation determination"""
        return 0

def event_m10_10_x172(z8=10101120):
    """[Execution] Giant Tree Fruit_System Version
    z8: Giant Tree OBJ Instance ID
    """
    """State 0,1: Tree fruit generation"""
    ActivateObjItem(z8, 1)
    """State 2: Save intrusion count"""
    SetGlobalVariable(1, TotalInvasionCount())
    """State 3: End state"""
    return 0

def event_m10_10_x173(z7=106200):
    """[Condition] Giant Tree Fruit_System Version
    z7: Tree fruit generation judgment flag
    """
    """State 0,1: Generation determination"""
    CompareEventFlag(0, z7, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x174(z8=10101120):
    """[Conditions] Giant tree fruit_system version_generation time
    z8: Giant Tree OBJ Instance ID
    """
    """State 0,1: Have you got the nuts?"""
    WasObjItemAcquired(0, z8, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_10_x175(z7=106200, z8=10101120):
    """[Execution] Giant tree fruit_system version_when generating
    z7: Giant tree nut generation flag
    z8: Giant Tree OBJ Instance ID
    """
    """State 0,1: Turn off the generation judgment flag"""
    SetEventFlag(z7, 0)
    """State 2: Reset item acquisition information"""
    ResetObjItem(z8)
    """State 3: End state"""
    return 0

def event_m10_10_x176(z7=106200, z8=10101120):
    """[Preset] Giant Tree Fruit_System Version
    z7: Giant tree nut generation flag
    z8: Giant Tree OBJ Instance ID
    """
    """State 0,1: [Reproduction] Giant Tree Fruit_System Version_SubState"""
    call = event_m10_10_x171(z7=z7, z8=z8)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 4: [Condition] Giant Tree Fruit_System Version_SubState"""
        assert event_m10_10_x173(z7=z7)
        """State 2: [Execution] Giant Tree Fruit_System Version_SubState"""
        assert event_m10_10_x172(z8=z8)
    """State 5: [Condition] Giant tree fruit_System version_Generation_SubState"""
    assert event_m10_10_x174(z8=z8)
    """State 3: [Execution] Giant Tree Fruit_System Version_When Generated_SubState"""
    assert event_m10_10_x175(z7=z7, z8=z8)
    """State 6: End state"""
    return 0

def event_m10_10_x177(z6=106200):
    """[Condition] Giant tree fruit_Message_Waiting for acquisition
    z6: Generate flag
    """
    """State 0,1: Have you got the nuts?"""
    CompareEventFlag(0, z6, 0)
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

def event_m10_10_x179(z4=110000025):
    """[DC] [Execution] Vagrant appears with hawks
    z4: Zako start flag
    """
    """State 0,1: Zako start flag ON"""
    SetEventFlag(z4, 1)
    """State 2: End state"""
    return 0

def event_m10_10_x180(z4=110000025):
    """[DC] [Reproduction] Vagrant appeared with hawks
    z4: Zako start flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is Zako started?"""
        if GetEventFlag(z4) != 0:
            pass
        else:
            """State 3: Not executed"""
            return 0
    """State 4: Finish"""
    return 1

def event_m10_10_x181(z1=110000024, z2=2255, z3=110000020, z4=110000025):
    """[DC] [Preset] Vagrant appears with hawks
    z1: Destruction flag
    z2: Generator ID
    z3: Appearance event executed flag
    z4: Zako start flag
    """
    """State 0,1: [DC] [Reproduction] Vagrant Appears in Hawk_Zako Launch_SubState"""
    call = event_m10_10_x180(z4=z4)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Vagrant appears with hawks_Zako start_SubState"""
        assert event_m10_10_x178(z1=z1, z2=z2, z3=z3)
        """State 2: [DC] [Execution] Vagrant Appears in Hawk_Zako Launch_SubState"""
        assert event_m10_10_x179(z4=z4)
    """State 4: End state"""
    return 0

def event_m10_10_111242():
    """OBJ: Moonlight Jun: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_10_x2(z183=104163, z184=10104300, z185=61, z186=7430)

def event_m10_10_111243():
    """OBJ: Satoshi Moonlight: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7430:Benhart of Jugo
    event_m10_10_x5(z178=110010100, z179=110020101, z180=104160, z181=10104300, z182=111242, npc1=7430)

def event_m10_10_111244():
    """OBJ: Satoshi Moonlight: Judgment of death"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z172=60, z173=104163)

def event_m10_10_111245():
    """OBJ: Tsukimitsu: Appearance judgment"""
    """State 0,1: [Lib] Appearance determination: Generic _SubState"""
    event_m10_10_x28(z149=104160, z150=102422, z151=102423, z152=110010107, z153=103662)

def event_m10_10_111252():
    """OBJ: Patch: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_10_x2(z183=104171, z184=10104200, z185=66, z186=7440)

def event_m10_10_111253():
    """OBJ: Patch: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7440:Mild-mannered Pate
    event_m10_10_x5(z178=110010110, z179=110020111, z180=104170, z181=10104200, z182=111252, npc1=7440)

def event_m10_10_111254():
    """OBJ: Patch: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z172=65, z173=104171)

def event_m10_10_111255():
    """OBJ: Patch: White phantom sign display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m10_10_x49(z131=102442, z132=526, z133=104170, z134=60, z135=103670, z136=65)

def event_m10_10_111256():
    """OBJ: Patch: White Phantom"""
    """State 0,1: [Lib] NPC: White Phantom: Summoning Count: General Purpose_SubState"""
    event_m10_10_x57(z124=110000081, z125=102452, z126=206, z127=7440)

def event_m10_10_111262():
    """OBJ: Mapping: Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_10_x2(z183=104181, z184=10104100, z185=86, z186=7510)

def event_m10_10_111263():
    """OBJ: cartography: key guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7510:Cartographer Cale
    event_m10_10_x5(z178=110010120, z179=110020121, z180=104180, z181=10104100, z182=111262, npc1=7510)

def event_m10_10_111264():
    """OBJ: Mapping: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z172=85, z173=104181)

def event_m10_10_111292():
    """OBJ: Yorozu Baba: Tomb"""
    """State 0,1: NPC: Yorozu Baba: Grave Placement_SubState"""
    event_m10_10_x2(z183=104211, z184=10104000, z185=261, z186=7540)

def event_m10_10_111293():
    """OBJ: Yorozu Baba: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7540:Merchant Hag Melentia
    event_m10_10_x5(z178=110010130, z179=110020131, z180=104210, z181=10104000, z182=111292, npc1=7540)

def event_m10_10_111294():
    """OBJ: Yorozu Baba: Death determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_10_x7(z172=260, z173=104211)

def event_m10_10_111435():
    """OBJ: Enclosed Person: Black Phantom Summon"""
    """State 0,1: Black Phantom Summon: Start"""
    CompareEventFlag(0, 100972, 1)
    assert ConditionGroup(0)
    """State 2: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_10_x58(z118=102810, z119=10000010, z120=520, z121=104340, z122=0, z123=2)

def event_m10_10_120110():
    """Trophy: Moonlight Sword (Giant Forest)"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_10_x60(z112=110020108, z113=31)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_10_130000():
    """White spirit test"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_10_x50(z130=527)

def event_m10_10_130001():
    """White Spirit Test_2"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_10_x50(z130=528)

def event_m10_10_140000():
    """Black spirit test"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_10_x59(z114=10000020, z115=521, z116=0, z117=0)

def event_m10_10_4000000():
    """[DC] Vagrant appears with hawks"""
    """State 0,2: [DC] [Preset] Vagrant Appears in Hawk_Zako Launch_SubState"""
    assert event_m10_10_x181(z1=110000024, z2=2255, z3=110000020, z4=110000025)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4001000():
    """[DC] Wanderer A_Random lottery and generation_Global flag version"""
    """State 0,6: [Lib] [DC] [Preset] Wanderer_Random lottery_Global flag version_SubState"""
    call = event_m10_10_x82(z81=110020001, z82=39, z83=110000002, z84=4, z85=10, z86=100804)
    if call.Get() == 3:
        pass
    elif call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m10_10_x72(z92=81000000, z93=0, z94=5, z95=923, val1=1, z96=10, z97=81000001, z98=81000099)
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m10_10_x72(z92=81000100, z93=0, z94=5, z95=923, val1=2, z96=10, z97=81000101, z98=81000199)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_3_SubState"""
        assert event_m10_10_x72(z92=81000200, z93=0, z94=5, z95=923, val1=3, z96=10, z97=81000201, z98=81000299)
        """State 7: [Lib] [DC] [Preset] Wanderer_Generation_4_SubState"""
        assert event_m10_10_x72(z92=81000300, z93=0, z94=5, z95=923, val1=4, z96=10, z97=81000300, z98=81000301)
        """State 2: Start flag ON"""
        SetEventFlag(110020003, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4001010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m10_10_x75(z89=110000002, z90=923, mode2=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_10_x79(z87=9100, z88=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_10_4031000():
    """[DC] NPC White Spirit _ Gesture Management _ New Giant Senior Soldier _ Dead"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_10_x86(z78=110000081, z79=857, z80=110020084)
    """State 1: Finish"""
    EndMachine()

