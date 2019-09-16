# -*- coding: utf-8 -*-
def event_m10_15_1000():
    """[Insect key] For lantern lighting"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_15_x23(z146=10154900)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_1010():
    """[Insect key activation] Lantern lights"""
    """State 0,2: [Preset] Lantern lights_SubState"""
    assert event_m10_15_x75(z81=10154900)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_2000():
    """During the mirror night"""
    """State 0,2: [Preset] Mirror Night _SubState"""
    assert event_m10_15_x127(z50=200000, z51=200000)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_3000():
    """An enemy trapped in the orientation comes out"""
    """State 0,2: [Preset] Enemies start when entering a giant trap or _SubState"""
    assert event_m10_15_x84(z25=300000, z26=300010, z27=300020)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4000():
    """Elevator Guardian Dragon's Nest"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_15_x13(z121=10152000, z122=400010, z123=400000, z124=10152505, z125=10152500)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_4010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_15_x18(z151=10152000, z152=10152505, z153=10)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_4020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_15_x18(z151=10152000, z152=10152500, z153=40)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_4030():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m10_15_x39(z126=403000, z127=10152000, z128=105425, z129=40, z130=50, z131=1, z132=0)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_4050():
    """For connection_Connection flag OFF"""
    """State 0,3: [Lib] [Preset] Switch the connection flag at the point _SubState"""
    call = event_m10_15_x60(z90=405000, z91=405000, z92=105425, z93=0, z94=1)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()

def event_m10_15_5000():
    """Ogre_ Petrochemical Stop_Key Guide"""
    """State 0,3: Character: Petrified: Key Guide_SubState"""
    assert event_m10_15_x140(z35=2500, z36=0, z37=15, z38=115000050, z39=0, z40=10159000, z41=4, z42=5010)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_5010():
    """Ogre _ Petrification stop_ Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_15_x44(z115=2500, z116=0, z117=115000050, z118=0, z119=0, z120=5000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_5020():
    """Auger _ petrification stop _ navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_15_x53(z107=502000, z108=0, z109=2, z110=115000050, z111=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_6000():
    """Mirror Night Mirror_1"""
    """State 0,2: [Preset] Mirror Night Mirror_SubState"""
    assert event_m10_15_x72(z82=10151615, z83=600000, z84=115020010)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_6030():
    """Mirror Knight Mirror_4"""
    """State 0,2: [Preset] Mirror Night Mirror_SubState"""
    assert event_m10_15_x72(z82=10151600, z83=603000, z84=115020013)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_6040():
    """Mirror Night Mirror_5"""
    """State 0,2: [Preset] Mirror Night Mirror_SubState"""
    assert event_m10_15_x72(z82=10151620, z83=604000, z84=115020014)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_7000():
    """Boss: Wyvern _ Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_15_x6(z154=115000081, z155=700000, z156=700000, z157=101, z158=1015000, z159=115020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()

def event_m10_15_8000():
    """Bone Dragon Death Treatment"""
    """State 0,2: [Preset] Bone Dragon's Death Process_SubState"""
    # lot:60050000:Aldia Key
    assert event_m10_15_x80(z78=5000, z79=7, z80=1, lot1=60050000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_9000():
    """Wall destruction auger activation_1"""
    """State 0,2: [Preset] Wall destruction auger start event _SubState"""
    assert event_m10_15_x89(z19=10151001, z20=115020005, z21=900000, z22=900001, z23=6000, z24=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_9010():
    """Wall breaking auger activation_2"""
    """State 0,2: [Preset] Wall destruction auger start event _SubState"""
    assert event_m10_15_x89(z19=10151025, z20=115020006, z21=900010, z22=900011, z23=6010, z24=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_10000():
    """Enemy generation when cart is destroyed_1"""
    """State 0,2: [Preset] Enemy generated when cart is destroyed _SubState"""
    assert event_m10_15_x93(z75=10151050, z76=115000015, z77=1000000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_10010():
    """Enemy generation when cart is destroyed_2"""
    """State 0,2: [Preset] Enemy generated when cart is destroyed _SubState"""
    assert event_m10_15_x93(z75=10151062, z76=115000016, z77=1001000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_10020():
    """Enemy generation when destroying cart _3"""
    """State 0,2: [Preset] Enemy generated when cart is destroyed _SubState"""
    assert event_m10_15_x93(z75=10151061, z76=115000017, z77=1002000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_11000():
    """Gimmick door in the middle of the map"""
    """State 0,2: Wait for initialization event to end"""
    assert EventEnded(11010) != 0
    """State 3: [Preset] Map middle gimmick door_SubState"""
    assert (event_m10_15_x97(z28=10152700, z29=10152705, z30=10152515, z31=10152520, z32=10152510, z33=1100000,
            z34=1100001))
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_11010():
    """Gimmick door in the middle of the map_initialization"""
    """State 0,2: [BEST] Relief event finished?"""
    assert EventEnded(4000000) != 0
    """State 3: [Preset] Map middle door_initialization_SubState"""
    assert event_m10_15_x131(z45=115010020, z46=10152700, z47=10152705, z48=1100000, z49=1100001)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_12000():
    """Switch enemy display with gimmick door"""
    """State 0,2: Is the initialization event finished?"""
    assert EventEnded(12010) != 0
    """State 3: [Preset] Enemy display switching at the gimmick door_SubState"""
    assert event_m10_15_x100(z70=10152700, z71=10152705) == 0
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_12010():
    """Enemy display switching_initialization"""
    """State 0,2: [BEST] Relief event finished?"""
    assert EventEnded(4000000) != 0
    """State 3: [Preset] Enemy display switching_initialization_SubState"""
    assert event_m10_15_x105(z66=10152700, z67=10152705)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_13000():
    """Sealed person"""
    """State 0,2: [Preset] Enclosed Person_SubState"""
    assert event_m10_15_x111(z62=10152710, z63=10152525, z64=1300000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_14000():
    """The door that opens with the key of Anne Deal"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_15_x4(z162=1005, z163=1105, z164=51030000, z165=115000030)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_15000():
    """Wall 1 visible on the door"""
    """State 0,2: [Preset] Wall visible through the door_SubState"""
    assert event_m10_15_x107(z65=10151001)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_15010():
    """Wall 2 visible on the door"""
    """State 0,2: [Preset] Wall visible through the door_SubState"""
    assert event_m10_15_x107(z65=10151002)
    """State 1: Rerun"""
    RestartMachine()

def event_m10_15_16000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_15_x31(z133=10151700, z134=20, z135=1600000, z136=0, z137=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_17000():
    """Switching the wall to be destroyed by the guided auger"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_15_x31(z133=10151002, z134=20, z135=1700000, z136=0, z137=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_18000():
    """Starting conditions for an auger at the foot of the aisle"""
    """State 0,2: [Preset] Startup condition of the auger and reinforced immortal at the foot of the passage_SubState"""
    assert event_m10_15_x115(z59=10151070, z60=1800000, z61=115020040)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_18010():
    """Activation conditions for reinforced immortals at the foot of the aisle"""
    """State 0,2: [Preset] Startup condition of the auger and reinforced immortal at the foot of the passage_SubState"""
    assert event_m10_15_x115(z59=10151080, z60=1801000, z61=115020041)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_20000():
    """Disabling damage"""
    """State 0,2: Disabling the damage floor"""
    SetDamageImmunityByGeneratorId(9100, 200014040, 1)
    SetDamageImmunityByGeneratorId(9101, 200014040, 1)
    SetDamageImmunityByGeneratorId(4200, 200014040, 1)
    """State 3: [DC] Large shield warrior petrified"""
    SetDamageImmunityByGeneratorId(540, 121000310, 1)
    SetDamageImmunityByGeneratorId(540, 122200410, 1)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_21000():
    """Wall and door to be destroyed by guided auger"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_15_x31(z133=10151020, z134=20, z135=2100000, z136=0, z137=2)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_21010():
    """The door is destroyed when the wall is destroyed_1"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_15_x122(z57=10151020, z58=10150400)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_22000():
    """The door is destroyed when the wall is destroyed_2"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_15_x122(z57=10151025, z58=10150433)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_23000():
    """The enemy behind the painting starts 1"""
    """State 0,2: [Preset] The enemy behind the painting is activated_SubState"""
    assert event_m10_15_x123(z54=10151200, z55=20, z56=115020035)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_23010():
    """The enemy behind the painting starts 2"""
    """State 0,2: [Preset] The enemy behind the painting is activated_SubState"""
    assert event_m10_15_x123(z54=10151203, z55=20, z56=115020036)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_23020():
    """The enemy behind the painting starts 3"""
    """State 0,2: [Preset] The enemy behind the painting is activated_SubState"""
    assert event_m10_15_x123(z54=10151201, z55=20, z56=115020037)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_24000():
    """Navi mesh change of the king's door"""
    """State 0,3: [Preset] Change the king's door navigation mesh_SubState"""
    call = event_m10_15_x135(z43=105310, z44=2400000)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m10_15_80000():
    """Fireworks for Regeneration 01_ Entrance building"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_15_x49(z112=1015000, z113=1015099)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_81000():
    """Rebirth Fire 02_Staircase hidden door room to basement"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_15_x49(z112=1015100, z113=1015199)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_x0(z171=_, z172=_, z173=_, z174=_):
    """[Lib] NPC: Grave Placement: General purpose
    z171: Death map: Global event flag
    z172: Tomb: OBJ instance ID
    z173: Tomb move to: Generator ID
    z174: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z171, 1)
    IsGraveGeneratable(8, z174, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z172, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z172, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m10_15_x1(z168=_, z169=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z168: Global: death flag
    z169: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z169, 10, 0)
    CompareObjState(1, z169, 20, 0)
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
    IsObjSearched(0, z169)
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

def event_m10_15_x2(z166=_, z167=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z166: Area other flags: Ghost appearance
    z167: Area other flags: Conversation start
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
    SetEventFlag(z166, 1)
    CompareEventFlag(0, z166, 1)
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
    SetEventFlag(z167, 1)
    CompareEventFlag(0, z167, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_15_x3(z166=_, z167=_, z168=_, z169=_, z170=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z166: Ghost Appearance: Area Other Flag
    z167: Conversation start: Area and other flags
    z168: Death: Global event flag
    z169: Tomb: OBJ instance ID
    z170: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z170, 1, 0)
    CompareEventFlag(9, z166, 1)
    CompareObjState(9, z169, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z167, 1)
        CompareEventFlag(0, z167, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_15_x1(z168=z168, z169=z169, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_15_x2(z166=z166, z167=z167, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m10_15_x4(z162=1005, z163=1105, z164=51030000, z165=_):
    """[Lib] Item specified door unlocking_2
    z162: Text ID when opened
    z163: Text ID when not opened
    z164: item
    z165: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z164, z162, z163, z165, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x5(z160=90, z161=104195):
    """[Lib] NPC: Death determination: General purpose
    z160: Generator ID
    z161: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z161, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z160)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z161, 1)
            CompareEventFlag(0, z161, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()

def event_m10_15_x6(z154=115000081, z155=700000, z156=700000, z157=101, z158=1015000, z159=115020080,
                    mode2=0):
    """[Lib] [Preset] Boss Battle Start
    z154: Boss destruction flag
    z155: Start point ID
    z156: End point ID
    z157: Sound ID
    z158: Boss Battle ID
    z159: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_15_x7(z154=z154)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_15_x8(z155=z155, z156=z156)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_15_x9(z157=z157, z158=z158, z159=z159)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_15_x10()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_15_x11(z158=z158)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_15_x12(z157=z157, z158=z158, z159=z159, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_15_x7(z154=115000081):
    """[Reproduction] Boss Battle_Start
    z154: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z154) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_15_x8(z155=700000, z156=700000):
    """[Condition] Boss Battle_Start
    z155: Start point ID
    z156: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z155, z156, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z155, z156, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x9(z157=101, z158=1015000, z159=115020080):
    """[Execution] Boss Battle_Start
    z157: Sound ID
    z158: Boss Battle ID
    z159: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z157)
    """State 1: Boss battle start notification"""
    StartBossFight(z158)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z159, 1)
    """State 4: End state"""
    return 0

def event_m10_15_x10():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x11(z158=1015000):
    """[Condition] Boss Battle_End Judgment
    z158: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z158, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x12(z157=101, z158=1015000, z159=115020080, mode2=0):
    """[Execute] Boss Battle_End
    z157: Sound ID
    z158: Boss Battle ID
    z159: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z159, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z158)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z157)
    """State 5: End state"""
    return 0

def event_m10_15_x13(z121=10152000, z122=400010, z123=400000, z124=10152505, z125=10152500):
    """[Lib] [Preset] Elevator
    z121: OBJ instance ID of the elevator
    z122: On elevator point ID_
    z123: Elevator point ID_below
    z124: Upper lever OBJ instance ID
    z125: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_15_x14()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_15_x15(z121=z121, z122=z122, z123=z123, z124=z124, z125=z125)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_15_x43(z121=z121, z123=z123)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_15_x42(z121=z121, z122=z122)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_15_x16(z121=z121, z122=z122)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_15_x17(z121=z121, z123=z123)
    """State 7: End state"""
    return 0

def event_m10_15_x14():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x15(z121=10152000, z122=400010, z123=400000, z124=10152505, z125=10152500):
    """[Condition] Elevator
    z121: Elevator OBJ instance ID
    z122: On elevator point ID_
    z123: Elevator point ID_below
    z124: Upper lever OBJ instance ID
    z125: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z121, 10, 0)
    CompareObjState(1, z121, 40, 0)
    CompareObjState(2, z121, 80, 0)
    CompareObjState(2, z121, 41, 0)
    CompareObjState(3, z121, 70, 0)
    CompareObjState(3, z121, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z123, z123, 1)
        CompareObjState(0, z124, 74, 0)
        CompareObjState(0, z124, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z122, z122, 1)
        CompareObjState(0, z125, 74, 0)
        CompareObjState(0, z125, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_15_x16(z121=10152000, z122=400010):
    """[Execution] Elevator_Rise
    z121: Elevator OBJ instance ID
    z122: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z121, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z121, 30, 0)
    IsPlayerInsidePoint(8, z122, z122, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z121, 71)
    assert CompareObjStateId(z121, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_15_x17(z121=10152000, z123=400000):
    """[Execution] Elevator_Descent
    z121: Elevator OBJ instance ID
    z123: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z121, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z121, 41, 0)
    IsPlayerInsidePoint(8, z123, z123, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z121, 81)
    assert CompareObjStateId(z121, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_15_x18(z151=10152000, z152=_, z153=_):
    """[Lib] [Preset] Elevator lever
    z151: OBJ instance ID of the elevator
    z152: Lever OBJ instance ID
    z153: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_15_x19()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_15_x20(z151=z151, z152=z152, z153=z153)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_15_x21(z151=z151, z152=z152, z153=z153)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_15_x22(z151=z151, z152=z152, z153=z153)
    """State 5: Rerun"""
    return 0

def event_m10_15_x19():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x20(z151=10152000, z152=_, z153=_):
    """[Condition] Elevator lever_use judgment
    z151: OBJ instance ID of the elevator
    z152: Lever OBJ instance ID
    z153: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z151, z153, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_15_x21(z151=10152000, z152=_, z153=_):
    """[Execution] Elevator lever_Key guide valid
    z151: OBJ instance ID of the elevator
    z152: Lever OBJ instance ID
    z153: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z152, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z151, z153, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x22(z151=10152000, z152=_, z153=_):
    """[Execute] Elevator lever_key guide disabled
    z151: OBJ instance ID of the elevator
    z152: Lever OBJ instance ID
    z153: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z152, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z151, z153, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x23(z146=10154900):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z146: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_15_x24(z146=z146)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_15_x28(z146=z146)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_15_x29()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_15_x25(z146=z146, mode1=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_15_x26(z146=z146, z148=38, z149=3, z150=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_15_x27(z146=z146, z147=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_15_x24(z146=10154900):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z146: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z146, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z146, 10)
        assert CompareObjStateId(z146, 10, 0)
    elif CompareObjStateId(z146, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z146, 74, 1) and CompareObjStateId(z146, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_15_x25(z146=10154900, mode1=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z146: Object instance ID
    mode1: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z146)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode1) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_15_x26(z146=10154900, z148=38, z149=3, z150=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z146: Object instance ID
    z148: Key guide type
    z149: Event action
    z150: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z146, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z146, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z146, 30)
        assert CompareObjStateId(z146, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z146, z148, z149)
        assert PlayerIsInEventAction(z149) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z149, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z146, 74, 0)
        CompareObjState(1, z146, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z150)
            assert CompareObjStateId(z146, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z146, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m10_15_x27(z146=10154900, z147=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z146: Object instance ID
    z147: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z146, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m10_15_x28(z146=10154900):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z146: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z146, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x29():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x30(z138=_, z139=0, z140=15, z141=_, z142=0, z143=_, z144=_, z145=_):
    """[Lib] Character: Petrochemical: Key guide
    z138: generator
    z139: Death: Global event flag
    z140: Event action
    z141: Petrified: Area and other flags
    z142: Petrified: Global event flag
    z143: Key guide parameters
    z144: Petrification start state ID
    z145: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z138, z144, 0)
    CompareEventStatus(8, z145, 1, 0)
    CompareEventFlag(2, z141, 1)
    CompareEventFlag(3, z142, 1)
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
    CreateKeyGuideArea(34, z143)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z138)
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
                PlayerActionRequest(z140)
                IsPlayerPlayingMotion(0, z140, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z141, 1)
                CompareEventFlag(0, z141, 1)
                SetEventFlag(z142, 1)
                CompareEventFlag(1, z142, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z140, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_15_x31(z133=_, z134=20, z135=_, z136=0, z137=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z133: Object instance ID
    z134: OBJ state ID
    z135: Navimesh switching point ID
    z136: Additional attributes
    z137: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_15_x32(z133=z133, z134=z134, z135=z135, z137=z137, z136=z136)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_15_x33(z133=z133, z134=z134, z135=z135)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_15_x34(z133=z133, z134=z134, z135=z135, z136=z136, z137=z137)
    """State 4: End state"""
    return 0

def event_m10_15_x32(z133=_, z134=20, z135=_, z137=2, z136=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z133: Target OBJ instance ID
    z134: Target OBJ state ID
    z135: Navimesh switching point ID
    z137: Additional attributes
    z136: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z133, z134, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z135, z137)
        DeleteNavimeshAttribute(z135, z136)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_15_x33(z133=_, z134=20, z135=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z133: Target OBJ instance ID
    z134: Target OBJ state ID
    z135: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z133, z134, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x34(z133=_, z134=20, z135=_, z136=0, z137=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z133: Target OBJ instance ID
    z134: Target OBJ state ID
    z135: Navimesh switching point ID
    z136: Additional attributes
    z137: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z135, z136)
    DeleteNavimeshAttribute(z135, z137)
    """State 2: End state"""
    return 0

def event_m10_15_x35():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x36(z126=403000, z127=10152000, z129=40, z130=50):
    """[Lib] [Condition] Elevator_Connection replacement
    z126: Replacement point
    z127: OBJ instance ID of the elevator
    z129: Top_Hit group ID
    z130: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z126, z126, 1)
    CompareObjState(8, z127, 70, 0)
    IsPlayerInsidePoint(9, z126, z126, 1)
    CompareObjState(9, z127, 80, 0)
    IsPlayerOnHitGroup(0, z129, 1)
    IsPlayerOnHitGroup(1, z130, 1)
    if ConditionGroup(8):
        """State 2: Ascent point intrusion"""
        return 0
    elif ConditionGroup(9):
        """State 3: Point entry while descending"""
        return 1
    elif ConditionGroup(0):
        """State 4: Be on top"""
        return 2
    elif ConditionGroup(1):
        """State 5: Be down"""
        return 3

def event_m10_15_x37(z126=403000, z128=105425, z131=1, z129=40, z127=10152000):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z126: Replacement point
    z128: Global flag for connection
    z131: ON / OFF of global flag
    z129: Top_Hit group ID
    z127: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z128, z131)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z126, z126, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z129, 1)
    IsPlayerInsidePoint(8, z126, z126, 1)
    CompareObjState(8, z127, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_15_x38(z128=105425, z131=1, z129=40, z126=403000, z127=10152000):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z128: Global flag for connection
    z131: ON / OFF of global flag
    z129: Hit group ID
    z126: Replacement point ID
    z127: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z128, z131)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z129, 0)
    IsPlayerInsidePoint(8, z126, z126, 1)
    CompareObjState(8, z127, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x39(z126=403000, z127=10152000, z128=105425, z129=40, z130=50, z131=1, z132=0):
    """[Lib] [Preset] Elevator_Connection replacement
    z126: Replacement point
    z127: OBJ instance ID of the elevator
    z128: Global flag for connection
    z129: Top_Hit group ID
    z130: Bottom_Hit group ID
    z131: Up_Global flag when rising
    z132: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m10_15_x35()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m10_15_x36(z126=z126, z127=z127, z129=z129, z130=z130)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m10_15_x37(z126=z126, z128=z128, z131=z131, z129=z129, z127=z127)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m10_15_x41(z126=z126, z128=z128, z132=z132, z130=z130, z127=z127)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m10_15_x38(z128=z128, z131=z131, z129=z129, z126=z126, z127=z127)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m10_15_x40(z128=z128, z132=z132, z130=z130, z126=z126, z127=z127)
    """State 7: End state"""
    return 0

def event_m10_15_x40(z128=105425, z132=0, z130=50, z126=403000, z127=10152000):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z128: Global flag for connection
    z132: ON / OFF of global flag
    z130: Hit group ID
    z126: Replacement point ID
    z127: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z128, z132)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z130, 0)
    IsPlayerInsidePoint(8, z126, z126, 1)
    CompareObjState(8, z127, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x41(z126=403000, z128=105425, z132=0, z130=50, z127=10152000):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z126: Replacement point
    z128: Global flag for connection
    z132: ON / OFF of global flag
    z130: Bottom_Hit group ID
    z127: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z128, z132)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z126, z126, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z130, 1)
    IsPlayerInsidePoint(8, z126, z126, 1)
    CompareObjState(8, z127, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_15_x42(z121=10152000, z122=400010):
    """[Execution] Elevator_Return switch after lift
    z121: Elevator OBJ instance ID
    z122: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z121, 30, 0)
    IsPlayerInsidePoint(8, z122, z122, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z121, 71)
    assert CompareObjStateId(z121, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_15_x43(z121=10152000, z123=400000):
    """[Execution] Elevator_Return switch after descending
    z121: Elevator OBJ instance ID
    z123: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z121, 41, 0)
    IsPlayerInsidePoint(8, z123, z123, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z121, 81)
    assert CompareObjStateId(z121, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_15_x44(z115=_, z116=0, z117=_, z118=0, z119=0, z120=_):
    """[Lib] Character: Petrified: Appearance setting
    z115: Generator ID
    z116: Death: Global event flag
    z117: Petrified: Area and other flags
    z118: Petrified: Global event flag
    z119: Startup state
    z120: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z115)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z116, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z117, 1)
                CompareEventFlag(1, z118, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z115, z119)
                elif ConditionGroup(1):
                    Goto('L0')
                else:
                    """State 7: Petrification appearance: Petrified state appearance"""
                    pass
    """State 2: Petrification appearance setting: System: End"""
    EndMachine()

def event_m10_15_x45(z114=540):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z114: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z114)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m10_15_x46():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x47(z112=_, z113=_):
    """[Lib] [execute] Rebirth fire
    z112: Flag start ID
    z113: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z112, z113, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x48():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x49(z112=_, z113=_):
    """[Lib] [Preset] Rebirth
    z112: Flag start ID
    z113: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_15_x46()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_15_x48()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_15_x47(z112=z112, z113=z113)
    """State 4: End state"""
    return 0

def event_m10_15_x50(z110=_, z111=0, z109=2, z108=0, z107=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    z110: Other flags
    z111: Global flag
    z109: Additional attributes
    z108: Delete attribute
    z107: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(z110) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(z111) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z107, z109)
        DeleteNavimeshAttribute(z107, z108)
        """State 3: Flag OFF"""
        return 0

def event_m10_15_x51(z110=_, z111=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    z110: Other flags
    z111: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, z110, 1)
    CompareEventFlag(0, z111, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_15_x52(z107=_, z108=0, z109=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z107: Navimesh switching point ID
    z108: Additional attributes
    z109: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z107, z108)
    DeleteNavimeshAttribute(z107, z109)
    """State 2: End state"""
    return 0

def event_m10_15_x53(z107=_, z108=0, z109=2, z110=_, z111=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z107: Navimesh switching point ID
    z108: Additional attributes
    z109: Delete attribute
    z110: Other flags
    z111: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_15_x50(z110=z110, z111=z111, z109=z109, z108=z108, z107=z107)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_15_x51(z110=z110, z111=z111)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_15_x52(z107=z107, z108=z108, z109=z109)
    """State 4: End state"""
    return 0

def event_m10_15_x54(z101=102810, z102=10001000, z103=530, z104=104340, z105=0, z106=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z101: Summoning conditions: Global event flag
    z102: Summon range
    z103: Generator ID
    z104: Death: Global event flag
    z105: Appearance: Minimum time
    z106: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z104, 1)
        CompareEventFlag(8, z101, 1)
        IsPlayerInsidePoint(8, z102, z102, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z104, 1)
            CompareStateTime(1, z105, 3, z106)
            IsPlayerInsidePoint(2, z102, z102, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z103)
                HasNpcPhantomSpawned(0, z103, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_15_x55(z97=10000000, z98=531, z99=0, z100=0):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z97: Summon range
    z98: Generator ID
    z99: Appearance: Minimum time
    z100: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z97, z97, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z99, 3, z100)
        IsPlayerInsidePoint(1, z97, z97, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z98)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m10_15_x56(z95=115020107, z96=33):
    """[Lib] [Preset] Get trophy
    z95: Acquisition trigger_other flags
    z96: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z95) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z95, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z96)
    """State 4: End state"""
    return 0

def event_m10_15_x57():
    """[Lib] [Reproduction] Switch the connection flag at the point"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_15_x58(z90=405000, z91=405000):
    """[Lib] [Condition] Switch the connection flag at the point
    z90: Start point ID
    z91: End point ID
    """
    """State 0,1: Are you in point?"""
    IsPlayerInsidePoint(0, z90, z91, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x59(z92=105425, z93=0, z94=1):
    """[Lib] [Execution] Switch to the connection flag at the point
    z92: Global event flag for connection
    z93: Flag switching
    z94: Wait for next judgment
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z92, z93)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z92, z93)
    assert ConditionGroup(0)
    """State 3: For next judgment: Has the flag changed?"""
    CompareEventFlag(0, z92, z94)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_15_x60(z90=405000, z91=405000, z92=105425, z93=0, z94=1):
    """[Lib] [Preset] Switch the connection flag at the point
    z90: Start point ID
    z91: End point ID
    z92: Global event flag for connection
    z93: Flag switching
    z94: Wait for next judgment
    """
    """State 0,1: [Lib] [Reproduction] Switch the connection flag at the point _SubState"""
    call = event_m10_15_x57()
    if call.Get() == 0:
        """State 3: [Lib] [Condition] Switch connection flag at point _SubState"""
        assert event_m10_15_x58(z90=z90, z91=z91)
        """State 2: [Lib] [Execution] Switch to the connection flag at the point _SubState"""
        assert event_m10_15_x59(z92=z92, z93=z93, z94=z94)
        """State 4: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 5: Guest: Exit"""
        return 1

def event_m10_15_x61(z88=_, z89=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z88: Generator ID
    z89: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z88, z89)
    """State 2: End state"""
    return 0

def event_m10_15_x62(z88=_, z89=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z88: Generator ID
    z89: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z88, z89, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_15_x63(z88=_):
    """[Lib] [DC] [Condition] Transparent characters
    z88: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z88)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x64(z88=_, z89=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z88: Generator ID
    z89: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_15_x62(z88=z88, z89=z89)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_15_x63(z88=z88)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_15_x61(z88=z88, z89=z89)
    """State 4: End state"""
    return 0

def event_m10_15_x65(z85=115000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z85: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z85) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_15_x66(z86=800):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z86: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z86, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x67(z87=115020082):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z87: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z87, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x68(z85=115000081, z86=800, z87=115020082):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z85: Boss destruction flag
    z86: Boss generator ID
    z87: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_15_x65(z85=z85)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_15_x66(z86=z86)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_15_x67(z87=z87)
    """State 4: End state"""
    return 0

def event_m10_15_x69(z82=_):
    """[Reproduction] Mirror night mirror state reproduction
    z82: Mirror instance ID
    """
    """State 0,2: Spiritual determination"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        """State 4: Enemy spirit: End"""
        return 1
    else:
        """State 1: OBJ initialization"""
        InitializeObj(z82)
        """State 3: End state"""
        return 0

def event_m10_15_x70(z83=_):
    """[Conditions] Point intrusion determination
    z83: Point ID
    """
    """State 0,1: Point intrusion standby"""
    IsPlayerInsidePoint(0, z83, z83, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x71(z82=_, z84=_):
    """[Execute] Mirror Split & Enemy Generation
    z82: Mirror instance ID
    z84: Operation flag
    """
    """State 0,1: Generator operation flag ON"""
    SetEventFlag(z84, 1)
    assert (GetStateTime() > 2.4) != 0
    """State 2: OBJ state transition: mirror split"""
    ChangeObjState(z82, 70)
    """State 3: End state"""
    return 0

def event_m10_15_x72(z82=_, z83=_, z84=_):
    """[Preset] Mirror Night Mirror
    z82: Mirror instance ID
    z83: Point ID
    z84: Operation flag
    """
    """State 0,1: [Reproduction] Mirror night mirror state reproduction_SubState"""
    call = event_m10_15_x69(z82=z82)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Point intrusion determination_SubState"""
        assert event_m10_15_x70(z83=z83)
        """State 3: [Execution] Mirror Split & Enemy Generation_SubState"""
        assert event_m10_15_x71(z82=z82, z84=z84)
    """State 4: End state"""
    return 0

def event_m10_15_x73(z81=10154900):
    """[Reproduction] Lantern lighting
    z81: OBJ instance ID of the bug key
    """
    """State 0,1: Is the insect key activated?"""
    if True:
        """State 3: Not running"""
        return 0
    elif CompareObjStateId(z81, 20, 0):
        """State 2: Keep all lights on: 20"""
        ChangeObjState(10151012, 20)
        ChangeObjState(10151013, 20)
        ChangeObjState(10151014, 20)
        ChangeObjState(10151015, 20)
        ChangeObjState(10151016, 20)
        ChangeObjState(10151017, 20)
        """State 4: Activated"""
        return 1

def event_m10_15_x74(z81=10154900):
    """[Condition] Lantern lighting
    z81: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z81, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x75(z81=10154900):
    """[Preset] Lantern lights
    z81: OBJ instance ID of the bug key
    """
    """State 0,1: [Reproduction] Lantern lighting_SubState"""
    call = event_m10_15_x73(z81=z81)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Lantern lighting_SubState"""
        assert event_m10_15_x74(z81=z81)
        """State 3: [Execution] Turning on the lantern_SubState"""
        assert event_m10_15_x76()
    """State 4: End state"""
    return 0

def event_m10_15_x76():
    """[Execution] Lighting the lantern"""
    """State 0,1: Lantern 1 lighting: 70"""
    ChangeObjState(10151012, 70)
    assert (GetStateTime() > 0.3) != 0
    """State 2: Lantern 2 lighting: 70"""
    ChangeObjState(10151013, 70)
    assert (GetStateTime() > 0.5) != 0
    """State 3: Lantern 3 lights: 70"""
    ChangeObjState(10151014, 70)
    assert (GetStateTime() > 1) != 0
    """State 4: Lantern 4 lighting: 70"""
    ChangeObjState(10151015, 70)
    assert (GetStateTime() > 2.5) != 0
    """State 5: Lantern 5 lights: 70"""
    ChangeObjState(10151016, 70)
    assert (GetStateTime() > 2.8) != 0
    """State 6: Lantern 6 lights: 70"""
    ChangeObjState(10151017, 70)
    """State 7: End state"""
    return 0

def event_m10_15_x77():
    """[Reproduction] Bone Dragon Death Processing"""
    """State 0,1: Host?"""
    if IsGuest() != 1:
        """State 2: host"""
        return 0
    else:
        """State 3: The guests"""
        return 1

def event_m10_15_x78(z78=5000, z79=7, z80=1):
    """[Condition] Death of bone dragon
    z78: Bone Dragon Generator ID
    z79: Logic flag ID
    z80: Logic flag comparison value
    """
    """State 0,1: Has the bone dragon finished the assault?"""
    CompareChrEzStateValue(0, z78, z79, z80, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x79(z78=5000, lot1=60050000):
    """[Execution] Bone Dragon Death Processing
    z78: Bone Dragon Generator ID
    lot1: Item lottery ID
    """
    """State 0,1: Bone dragon death treatment key item acquisition"""
    EnemyActionRequest(z78, 1)
    # lot:60050000:Aldia Key
    AwardItem(lot1, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x80(z78=5000, z79=7, z80=1, lot1=60050000):
    """[Preset] Bone Dragon Death Treatment
    z78: Bone Dragon Generator ID
    z79: Logic flag ID
    z80: Logic flag comparison value
    lot1: Item lottery ID
    """
    """State 0,1: [Reproduction] Bone Dragon Death Processing_SubState"""
    call = event_m10_15_x77()
    if call.Get() == 0:
        """State 3: [Condition] Death process of bone dragon_SubState"""
        assert event_m10_15_x78(z78=z78, z79=z79, z80=z80)
        """State 2: [Execution] Bone Dragon Death Processing_SubState"""
        assert event_m10_15_x79(z78=z78, lot1=lot1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m10_15_x81():
    """[Reproduction] Enemies are activated when they enter a large cage"""
    """State 0,2: Spiritual determination"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    else:
        Goto('L0')
    """State 5: Enemy's unreactive spirit"""
    return 2
    """State 1: Has the cocoon already broken?"""
    Label('L0')
    if CompareObjStateId(10151040, 20, 0):
        """State 3: Destroyed"""
        return 0
    else:
        """State 4: Not destroyed"""
        return 1

def event_m10_15_x82(z25=300000):
    """[Condition] Enemies are activated when they enter the ori
    z25: Point ID
    """
    """State 0,1: Did you enter the or 檻 that attacked the trap?"""
    IsObjDamaged(0, 10151040, -1, -3, 0)
    IsPlayerInsidePoint(0, z25, z25, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x83(z27=300020):
    """[Execution] Enemies are activated when they enter a large cage or inside
    z27: Point ID for Navimesh change
    """
    """State 0,1: Enemy activation flag ON"""
    SetEventFlag(115010001, 1)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z27, 2)
    """State 3: End state"""
    return 0

def event_m10_15_x84(z25=300000, z26=300010, z27=300020):
    """[Preset] Enemies are activated when entering or encroaching a giant spear
    z25: Point ID for destruction
    z26: Destroyed point ID
    z27: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Enemies start up when entering a giant eagle or sub_State"""
    call = event_m10_15_x81()
    if call.Get() == 2:
        """State 6: [Condition] Enemy activation determination_Enemy Spirit_SubState"""
        assert event_m10_15_x142()
        """State 5: [Execution] Navi Change_Enemy Spirit_SubState"""
        assert event_m10_15_x143(z27=z27)
    elif call.Get() == 0:
        """State 3: [Condition] Enemies start when entering specified area_SubState"""
        assert event_m10_15_x85(z26=z26)
        """State 4: [Execution] Enemies are activated when they enter a giant trap or _SubState"""
        Label('L0')
        assert event_m10_15_x83(z27=z27)
    elif call.Done():
        """State 2: [Condition] Enemies are activated when they enter a large cage or _SubState"""
        assert event_m10_15_x82(z25=z25)
        Goto('L0')
    """State 7: End state"""
    return 0

def event_m10_15_x85(z26=300010):
    """[Condition] Enemies start when entering the specified area
    z26: Point ID
    """
    """State 0,1: Entered the specified area?"""
    IsPlayerInsidePoint(0, z26, z26, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x86(z19=_, z22=_, z20=_):
    """[Reproduction] Wall destruction auger activation
    z19: Wall instance ID
    z22: Navigation switching point ID
    z20: Auger wall destruction flag
    """
    """State 0,4: Spiritual determination"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        pass
    else:
        Goto('L0')
    """State 7: Enemy's unreactive spirit"""
    return 2
    """State 1: Has the wall been destroyed?"""
    Label('L0')
    if CompareObjStateId(z19, 20, 0):
        """State 3: Ogre wall destruction flag ON"""
        SetEventFlag(z20, 1)
        """State 2: Navi mesh switching"""
        DeleteNavimeshAttribute(z22, 2)
        """State 5: Destroyed"""
        return 0
    else:
        """State 6: Not destroyed"""
        return 1

def event_m10_15_x87(z21=_, z23=_, z19=_, z24=_):
    """[Condition] Wall breaking auger activation
    z21: Point ID
    z23: Generator ID
    z19: Wall instance ID
    z24: Time until entering the point and the auger reacts
    """
    """State 0,1: Did the auger meet the conditions to destroy the wall?"""
    IsPlayerInsidePoint(0, z21, z21, 1)
    CompareChrHpRatio(1, z23, 100, 4)
    IsObjBroken(2, z19, 1)
    if ConditionGroup(0):
        """State 2: Has a certain time elapsed since entering the point? Or did you damage the auger?"""
        CompareStateTime(0, z24, 2, z24)
        CompareChrHpRatio(1, z23, 100, 4)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            pass
    elif ConditionGroup(1):
        pass
    elif ConditionGroup(2):
        """State 4: Wall destruction by normal action"""
        return 1
    """State 3: End state"""
    return 0

def event_m10_15_x88(z20=_, z22=_, z19=_):
    """[Execution] Wall destruction auger activation_Wall destruction action flag ON
    z20: Auger wall destruction flag
    z22: Navigation switching point ID
    z19: Wall instance ID
    """
    """State 0,1: Ogre wall destruction flag ON"""
    SetEventFlag(z20, 1)
    """State 2: The wall was broken"""
    IsObjBroken(0, z19, 1)
    assert ConditionGroup(0)
    """State 3: Navi mesh switching"""
    DeleteNavimeshAttribute(z22, 2)
    """State 4: End state"""
    return 0

def event_m10_15_x89(z19=_, z20=_, z21=_, z22=_, z23=_, z24=_):
    """[Preset] Wall destruction auger activation
    z19: Wall instance ID
    z20: Auger wall destruction flag
    z21: Point ID
    z22: Navigation switching point ID
    z23: Generator ID
    z24: Time until entering the point and the auger reacts
    """
    """State 0,1: [Reproduction] Wall destruction auger activation_SubState"""
    call = event_m10_15_x86(z19=z19, z22=z22, z20=z20)
    if call.Get() == 2:
        """State 5: [Condition] Wall destruction auger activation_Enemy Spirit_SubState"""
        assert event_m10_15_x144(z19=z19)
        """State 6: [Execution] Wall destruction auger activation_Navimesh switching only_2_SubState"""
        assert event_m10_15_x106(z22=z22)
    elif call.Get() == 0:
        pass
    elif call.Done():
        """State 2: [Condition] Wall destruction auger activation_SubState"""
        call = event_m10_15_x87(z21=z21, z23=z23, z19=z19, z24=z24)
        if call.Get() == 0:
            """State 3: [Execution] Wall destruction auger activation_Wall destruction action flag ON_SubState"""
            assert event_m10_15_x88(z20=z20, z22=z22, z19=z19)
        elif call.Get() == 1:
            """State 4: [Execution] Wall destruction auger activation_Navimesh switching only_SubState"""
            assert event_m10_15_x106(z22=z22)
    """State 7: End state"""
    return 0

def event_m10_15_x90(z75=_, z76=_, z77=_):
    """[Reproduction] Enemy generation when cart is destroyed
    z75: Cart instance ID
    z76: Enemy generation flag
    z77: Point ID for Navimesh change
    """
    """State 0,1: Is the cart destroyed?"""
    if CompareObjStateId(z75, 20, 0):
        """State 2: Enemy generation flag ON"""
        SetEventFlag(z76, 1)
        """State 3: Navigation mesh change"""
        DeleteNavimeshAttribute(z77, 2)
        """State 4: Destroyed"""
        return 0
    else:
        """State 5: Not destroyed"""
        return 1

def event_m10_15_x91(z75=_):
    """[Condition] Enemy is generated when cart is destroyed
    z75: Cart instance ID
    """
    """State 0,1: Waiting for cart destruction"""
    CompareObjState(0, z75, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x92(z76=_, z77=_):
    """[Execution] Enemy generation when cart is destroyed
    z76: Enemy generation flag
    z77: Point ID for Navimesh change
    """
    """State 0,1: Enemy generation flag ON"""
    SetEventFlag(z76, 1)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z77, 2)
    """State 3: End state"""
    return 0

def event_m10_15_x93(z75=_, z76=_, z77=_):
    """[Preset] Enemy generated when cart is destroyed
    z75: Cart instance ID
    z76: Enemy generation flag
    z77: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Enemy generation at the time of cart destruction_SubState"""
    call = event_m10_15_x90(z75=z75, z76=z76, z77=z77)
    if call.Get() == 0:
        pass
    elif call.Done():
        """State 2: [Condition] Enemy generated at the time of cart destruction_SubState"""
        assert event_m10_15_x91(z75=z75)
        """State 3: [Execution] Enemies generated when the cart is destroyed _SubState"""
        assert event_m10_15_x92(z76=z76, z77=z77)
    """State 4: End state"""
    return 0

def event_m10_15_x94(z28=10152700, z29=10152705, z30=10152515, z31=10152520, z32=10152510):
    """[Reproduction] Gimmick door in the middle of the map
    z28: The instance ID of the lobby door
    z29: Instance ID of the aisle door
    z30: The instance ID of the lobby lever
    z31: Instance ID of the aisle lever
    z32: Center lever instance ID
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z28, 80, 0):
        """State 4: Key guide all OFF: Lobby side closed"""
        DisableObjKeyGuide(z30, 1)
        DisableObjKeyGuide(z31, 1)
        DisableObjKeyGuide(z32, 1)
        """State 8: Closed lobby side"""
        return 2
    elif CompareObjStateId(z29, 80, 0):
        """State 5: Key guide all OFF: Closing passage side"""
        DisableObjKeyGuide(z31, 1)
        DisableObjKeyGuide(z30, 1)
        DisableObjKeyGuide(z32, 1)
        """State 9: Aisle side closed"""
        return 3
    elif CompareObjStateId(z28, 30, 0):
        """State 2: Key guide switching: When the lobby is released"""
        DisableObjKeyGuide(z30, 1)
        DisableObjKeyGuide(z31, 0)
        DisableObjKeyGuide(z32, 0)
        """State 6: When the lobby is open"""
        return 0
    elif CompareObjStateId(z29, 30, 0):
        """State 3: Key guide switching: When aisle is released"""
        DisableObjKeyGuide(z31, 1)
        DisableObjKeyGuide(z30, 0)
        DisableObjKeyGuide(z32, 0)
        """State 7: When the aisle is open"""
        return 1

def event_m10_15_x95(z31=_, z32=10152510):
    """[Condition] Gimmick door in the middle of the map
    z31: Lever instance ID to activate
    z32: Center lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z31, 74, 0)
    CompareObjState(0, z31, 84, 0)
    CompareObjState(0, z32, 74, 0)
    CompareObjState(0, z32, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x96(z28=_, z29=_, z30=10152515, z31=10152520, z32=10152510, z33=_, z34=_):
    """[Execution] Gimmick door in the middle of the map
    z28: Instance ID of the door to close
    z29: Instance ID of door to open
    z30: Lobby lever instance ID
    z31: Aisle lever instance ID
    z32: Center lever instance ID
    z33: Point ID to change Navimesh to entry prohibition
    z34: Point ID to change Navimesh to allow entry
    """
    """State 0,1: Close the door"""
    ChangeObjState(z28, 80)
    """State 5: Key guide switching: All invalid"""
    DisableObjKeyGuide(z30, 1)
    DisableObjKeyGuide(z31, 1)
    DisableObjKeyGuide(z32, 1)
    """State 4: Has the door closed?"""
    CompareObjState(0, z28, 10, 0)
    assert ConditionGroup(0)
    """State 6: Navi Mesh Change: No entry on"""
    AddNavimeshAttribute(z33, 2)
    """State 2,3: Open the door"""
    ChangeObjState(z29, 70)
    """State 7: Navi Mesh Change: No entry prohibited"""
    DeleteNavimeshAttribute(z34, 2)
    """State 8: End state"""
    return 0

def event_m10_15_x97(z28=10152700, z29=10152705, z30=10152515, z31=10152520, z32=10152510, z33=1100000,
                     z34=1100001):
    """[Preset] Map middle gimmick door
    z28: The instance ID of the lobby door
    z29: Instance ID of the aisle door
    z30: The instance ID of the lobby lever
    z31: Instance ID of the aisle lever
    z32: Center lever instance ID
    z33: Point ID for changing the navigation mesh of the lobby door
    z34: Point ID for changing the navigation mesh of the door on the aisle side
    """
    """State 0,1: [Reproduction] Gimmick door _SubState in the middle of the map"""
    call = event_m10_15_x94(z28=z28, z29=z29, z30=z30, z31=z31, z32=z32)
    if call.Get() == 2:
        """State 6: [Execution] Gimmick door in the middle of the map_Lobby side closing_SubState"""
        assert event_m10_15_x141(z28=z28, z29=z29, z30=z30, z31=z31, z32=z32, z33=z33, z34=z34)
    elif call.Get() == 3:
        """State 7: [Execution] Gimmick door in the middle of the map_Aisle side closed_SubState"""
        assert event_m10_15_x141(z28=z29, z29=z28, z30=z30, z31=z31, z32=z32, z33=z34, z34=z33)
    elif call.Get() == 0:
        """State 2: [Condition] Gimmick door in the middle of the map: When the lobby side is open_SubState"""
        assert event_m10_15_x95(z31=z31, z32=z32)
        """State 4: [Execution] Gimmick door in the middle of the map: _SubState when the lobby is open"""
        assert event_m10_15_x96(z28=z28, z29=z29, z30=z30, z31=z31, z32=z32, z33=z33, z34=z34)
    elif call.Get() == 1:
        """State 3: [Condition] Gimmick door in the middle of the map: When the aisle side is open_SubState"""
        assert event_m10_15_x95(z31=z30, z32=z32)
        """State 5: [Execute] Gimmick door in the middle of the map: When the aisle side is open_SubState"""
        assert event_m10_15_x96(z28=z29, z29=z28, z30=z30, z31=z31, z32=z32, z33=z34, z34=z33)
    """State 8: End state"""
    return 0

def event_m10_15_x98(z74=_, z70=_):
    """[Condition] Switch enemy display with gimmick door
    z74: Hit group on the side that does not erase the enemy
    z70: Instance ID of the door to close
    """
    """State 0,1: Did the door close while riding the specified hit?"""
    IsPlayerOnHitGroup(0, z74, 1)
    IsPlayerOnHitGroup(0, 30, 1)
    SetConditionGroup(8, 0)
    CompareObjState(8, z70, 10, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_15_x99(z72=_, z73=_):
    """[Execution] Switch the enemy display at the gimmick door
    z72: Event group ID to stop
    z73: Event group ID to be canceled
    """
    """State 0,1: Enemy stop"""
    PauseEnemyGroup(z72, 1)
    """State 3,2: Enemy stop release"""
    PauseEnemyGroup(z73, 0)
    """State 4: End state"""
    return 0

def event_m10_15_x100(z70=10152700, z71=10152705):
    """[Preset] Switch enemy display with gimmick door
    z70: The instance ID of the lobby door
    z71: Instance ID of the aisle door
    """
    """State 0,1: [Reproduction] Enemy display switching at the gimmick door_SubState"""
    call = event_m10_15_x101(z70=z70, z71=z71)
    if call.Get() == 0:
        """State 2: [Condition] Enemy display switching with gimmick door: Lobby side closes_SubState"""
        assert event_m10_15_x98(z74=10, z70=z70)
        """State 4: [Execution] Enemy display switching at gimmick door: Lobby side closes_SubState"""
        assert event_m10_15_x99(z72=20, z73=21)
    elif call.Get() == 1:
        """State 3: [Condition] Enemy display switching at gimmick door: Passage side closes_SubState"""
        assert event_m10_15_x98(z74=20, z70=z71)
        """State 5: [Execution] Enemy switching with gimmick door: Aisle side closes_SubState"""
        assert event_m10_15_x99(z72=21, z73=20)
    """State 6: Rerun"""
    return 0

def event_m10_15_x101(z70=10152700, z71=10152705):
    """[Reproduction] Enemy switching with gimmick door
    z70: The instance ID of the lobby door
    z71: Instance ID of the aisle door
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z70, 30, 0):
        """State 2: When the lobby is open"""
        return 0
    elif CompareObjStateId(z71, 30, 0):
        """State 3: When the aisle is open"""
        return 1

def event_m10_15_x102():
    """[Reproduction] Enemy display switching_initialization"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x103(z66=10152700, z67=10152705):
    """[Condition] Enemy display switching_initialization
    z66: Lobby side door OBJ instance ID
    z67: Aisle side door OBJ instance ID
    """
    """State 0,1: PC position and open door judgment"""
    IsPlayerOnHitGroup(0, 20, 1)
    IsPlayerOnHitGroup(8, 30, 1)
    CompareObjState(8, z66, 30, 0)
    SetConditionGroup(0, 8)
    IsPlayerOnHitGroup(1, 10, 1)
    IsPlayerOnHitGroup(9, 30, 1)
    CompareObjState(9, z67, 30, 0)
    SetConditionGroup(1, 9)
    if ConditionGroup(0):
        """State 2: Lobby side"""
        return 0
    elif ConditionGroup(1):
        """State 3: Ogre passage side"""
        return 1

def event_m10_15_x104(z68=_, z69=_):
    """[Execute] Enemy display switching_initialization
    z68: Event group ID to stop
    z69: Event group ID to be canceled
    """
    """State 0,1: Switch enemy display"""
    PauseEnemyGroup(z68, 1)
    PauseEnemyGroup(z69, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x105(z66=10152700, z67=10152705):
    """[Preset] Enemy display switching_initialization
    z66: Lobby side door OBJ instance ID
    z67: Aisle side door OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemy display switching_initialization_SubState"""
    assert event_m10_15_x102()
    """State 2: [Condition] Enemy display switching_initialization_SubState"""
    call = event_m10_15_x103(z66=z66, z67=z67)
    if call.Get() == 0:
        """State 4: [Execution] Enemy display switching_initialization: Lobby side display_SubState"""
        assert event_m10_15_x104(z68=21, z69=20)
    elif call.Get() == 1:
        """State 3: [Execute] Enemy display switching_initialization: passage side display_SubState"""
        assert event_m10_15_x104(z68=20, z69=21)
    """State 5: End state"""
    return 0

def event_m10_15_x106(z22=_):
    """[Execution] Wall destruction auger activation_Navimesh switching only
    z22: Navigation switching point ID
    """
    """State 0,1: Navi mesh switching"""
    DeleteNavimeshAttribute(z22, 2)
    """State 2: End state"""
    return 0

def event_m10_15_x107(z65=_):
    """[Preset] Wall visible on the door
    z65: Instance ID of the wall OBJ visible on the door
    """
    """State 0,1: [Reproduction] Wall _SubState visible in the door"""
    assert event_m10_15_x108()
    """State 2: [Condition] Wall visible through the door_SubState"""
    assert event_m10_15_x109(z65=z65)
    """State 3: [Execution] Wall that looks like a door_SubState"""
    assert event_m10_15_x110(z65=z65)
    """State 4: End state"""
    return 0

def event_m10_15_x108():
    """[Reproduction] Wall visible on the door"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x109(z65=_):
    """[Conditions] Wall visible on the door
    z65: Instance ID of the wall OBJ visible on the door
    """
    """State 0,1: Have you checked the wall?"""
    IsObjSearched(0, z65)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x110(z65=_):
    """[Execution] Wall visible on the door
    z65: Instance ID of the wall OBJ visible on the door
    """
    """State 0,1: Show message"""
    # action:1100:"Locked"
    DisplayOwnOkMenu(1100, 0, 0, 190, 0, 0, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x111(z62=10152710, z63=10152525, z64=1300000):
    """[Preset] Enclosed people
    z62: Magic barrier OBJ instance ID
    z63: Lever OBJ instance ID
    z64: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Enclosed person_SubState"""
    call = event_m10_15_x112(z62=z62, z64=z64)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Enclosed person_SubState"""
        assert event_m10_15_x113(z63=z63)
        """State 3: [Execution] Enclosed Person_SubState"""
        assert event_m10_15_x114(z62=z62, z64=z64)
    """State 4: End state"""
    return 0

def event_m10_15_x112(z62=10152710, z64=1300000):
    """[Reproduction] Enclosed people
    z62: Magic barrier OBJ instance ID
    z64: Point ID for Navimesh change
    """
    """State 0,1: Has the seal already been released?"""
    if GetEventFlag(102810) != 0:
        pass
    else:
        Goto('L0')
    """State 3: Has the magic barrier been initialized?"""
    if IsGuest() != 1 and CompareObjStateId(z62, 10, 0):
        """State 4: [Relief] Canceling the magic barrier: 70"""
        ChangeObjState(z62, 70)
        assert CompareObjStateId(z62, 20, 0)
    else:
        pass
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z64, 2)
    """State 6: Canceled"""
    return 1
    """State 5: Not open"""
    Label('L0')
    return 0

def event_m10_15_x113(z63=10152525):
    """[Condition] Enclosed person
    z63: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z63, 72, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x114(z62=10152710, z64=1300000):
    """[Execution] Enclosed person
    z62: Magic barrier OBJ instance ID
    z64: Point ID for Navimesh change
    """
    """State 0,1: Break the magic barrier: 70"""
    ChangeObjState(z62, 70)
    assert CompareObjStateId(z62, 20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z64, 2)
    """State 3: Sealed Person: Turns on the seal release flag"""
    SetEventFlag(102810, 1)
    """State 4: End state"""
    return 0

def event_m10_15_x115(z59=_, z60=_, z61=_):
    """[Preset] Activation conditions for an auger and a reinforced immortal who are at the foot of the aisle
    z59: 檻 OBJ instance ID
    z60: Point ID for Navimesh change
    z61: An activation flag for enemies in the cage
    """
    """State 0,1: [Reproduction] Starting condition of the auger and reinforced immortal at the foot of the passage_SubState"""
    call = event_m10_15_x116(z59=z59)
    if call.Get() == 0:
        """State 2: [Conditions] Activation conditions for the auger and reinforced immortal at the foot of the aisle_SubState"""
        assert event_m10_15_x117(z59=z59)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Activation conditions for the auger and reinforced immortal who are at the foot of the passage_SubState"""
    assert event_m10_15_x118(z60=z60, z61=z61)
    """State 4: End state"""
    return 0

def event_m10_15_x116(z59=_):
    """[Reproduction] Starting conditions for an auger and a reinforced immortal man
    z59: 檻 OBJ instance ID
    """
    """State 0,1: 判定 Judgment of OBJ status"""
    if CompareObjStateId(z59, 10, 0):
        """State 2: Undestructed"""
        return 0
    else:
        """State 3: Destroyed"""
        return 1

def event_m10_15_x117(z59=_):
    """[Conditions] Conditions for starting an auger and a reinforced immortal person at the foot of the passage
    z59: 檻 OBJ instance ID
    """
    """State 0,1: 檻 Destruction of OBJ destruction"""
    CompareObjState(0, z59, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x118(z60=_, z61=_):
    """[Execution] Starting conditions for an auger and a reinforced immortal person at the foot of the passage
    z60: Point ID for Navimesh change
    z61: An activation flag for enemies in the cage
    """
    """State 0,1: Navimesh change processing"""
    DeleteNavimeshAttribute(z60, 2)
    """State 2: Turn on the activation flag for enemies in the cage"""
    SetEventFlag(z61, 1)
    """State 3: End state"""
    return 0

def event_m10_15_x119():
    """[Reproduction] Destroy the door when the wall is destroyed"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x120(z57=_):
    """[Condition] When the wall is destroyed, the door is also destroyed.
    z57: Wall OBJ instance ID
    """
    """State 0,1: Wall waiting for destruction"""
    IsObjBroken(0, z57, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x121(z58=_):
    """[Execution] When the wall is destroyed, the door is also destroyed.
    z58: Door OBJ instance ID
    """
    """State 0,1: Door destruction"""
    DestroyObj(z58, z58, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x122(z57=_, z58=_):
    """[Preset] Destroy the door when the wall is destroyed
    z57: Wall OBJ instance ID
    z58: Door OBJ instance ID
    """
    """State 0,1: [Reproduction] Destroy the door when the wall is destroyed_Sky_SubState"""
    assert event_m10_15_x119()
    """State 3: [Condition] The door is destroyed when the wall is destroyed."""
    assert event_m10_15_x120(z57=z57)
    """State 2: [Execution] When the wall is destroyed, the door is also destroyed._SubState"""
    assert event_m10_15_x121(z58=z58)
    """State 4: End state"""
    return 0

def event_m10_15_x123(z54=_, z55=20, z56=_):
    """[Preset] The enemy behind the painting starts
    z54: Instance ID of the painting OBJ
    z55: State ID when the painting OBJ is destroyed
    z56: Enemy action start flag
    """
    """State 0,1: [Reproduction] The enemy behind the painting is activated_SubState"""
    call = event_m10_15_x124(z54=z54, z55=z55, z56=z56)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] The enemy behind the painting is activated_SubState"""
        assert event_m10_15_x125(z54=z54, z55=z55)
        """State 3: [Execution] The enemy behind the painting is activated_SubState"""
        assert event_m10_15_x126(z56=z56)
    """State 4: End state"""
    return 0

def event_m10_15_x124(z54=_, z55=20, z56=_):
    """[Reproduction] The enemy behind the painting starts
    z54: Instance ID of the painting OBJ
    z55: State ID when the painting OBJ is destroyed
    z56: Enemy action start flag
    """
    """State 0,1: State judgment of painting OBJ"""
    if CompareObjStateId(z54, z55, 0):
        """State 2: Turn on enemy action start flag"""
        SetEventFlag(z56, 1)
        """State 4: Destroyed"""
        return 1
    else:
        """State 3: Undestructed"""
        return 0

def event_m10_15_x125(z54=_, z55=20):
    """[Condition] The enemy behind the painting starts
    z54: Instance ID of the painting OBJ
    z55: State ID when the painting OBJ is destroyed
    """
    """State 0,1: Has the painting OBJ been destroyed?"""
    CompareObjState(0, z54, z55, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x126(z56=_):
    """[Execution] The enemy behind the painting starts
    z56: Enemy action start flag
    """
    """State 0,1: Turn on enemy action start flag"""
    SetEventFlag(z56, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x127(z50=200000, z51=200000):
    """[Preset] Mirror Night
    z50: Judgment area start point ID
    z51: End point ID of the judgment area
    """
    """State 0,1: [Reproduction] _SubState during Mirror Knight"""
    assert event_m10_15_x128()
    """State 2: [Condition] Mirror Knight's _ Area_SubState"""
    assert event_m10_15_x129(z53=1, z50=z50, z51=z51)
    """State 3: [Execution] Mirror Knight's _ Area_SubState"""
    assert event_m10_15_x130(z52=1)
    """State 4: [Conditions] Mirror Night Room_Outside Area_SubState"""
    assert event_m10_15_x129(z53=0, z50=z50, z51=z51)
    """State 5: [Execution] During Mirror Knight_Outside Area_SubState"""
    assert event_m10_15_x130(z52=0)
    """State 6: End state"""
    return 0

def event_m10_15_x128():
    """[Reproduction] Mirror Night"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x129(z53=_, z50=200000, z51=200000):
    """[Conditions] Mirror Night
    z53: Area inside / outside judgment
    z50: Judgment area start point ID
    z51: End point ID of the judgment area
    """
    """State 0,1: Area inside / outside judgment"""
    IsPlayerInsidePoint(0, z50, z51, z53)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x130(z52=_):
    """[Execution] Mirror Night
    z52: Special drawing to set
    """
    """State 0,1: Drawing switching"""
    SetSpecialDrawingMode(z52)
    """State 2: End state"""
    return 0

def event_m10_15_x131(z45=115010020, z46=10152700, z47=10152705, z48=1100000, z49=1100001):
    """[Preset] Map middle gimmick door_initialization
    z45: Gimmick door initialization execution determination flag
    z46: The instance ID of the lobby door
    z47: Instance ID of the aisle door
    z48: Point ID for changing the navigation mesh of the lobby door
    z49: Point ID for changing the navigation mesh of the door on the aisle side
    """
    """State 0,1: [Reproduction] Gimmick door in the middle of the map_Initialization_SubState"""
    call = event_m10_15_x132()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Gimmick door in the middle of the map_Initialization_SubState"""
        call = event_m10_15_x133(z45=z45)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 3: [Execution] Gimmick door in the middle of the map_Initialization_SubState"""
            assert event_m10_15_x134(z45=z45, z46=z46, z47=z47, z48=z48, z49=z49)
    """State 4: End state"""
    return 0

def event_m10_15_x132():
    """[Reproduction] Gimmick door in the middle of the map_initialization"""
    """State 0,1: Exit if guest"""
    if IsGuest() != 0:
        """State 3: Finish"""
        return 1
    else:
        """State 2: Execution conditions"""
        return 0

def event_m10_15_x133(z45=115010020):
    """[Condition] Gimmick door in the middle of the map_Initialization
    z45: Gimmick door initialization execution determination flag
    """
    """State 0,1: Initialization execution judgment"""
    CompareEventFlag(0, 115010020, 1)
    if ConditionGroup(0):
        """State 3: Finish"""
        return 1
    else:
        """State 2: Initialization execution"""
        return 0

def event_m10_15_x134(z45=115010020, z46=10152700, z47=10152705, z48=1100000, z49=1100001):
    """[Execution] Gimmick door in the middle of the map
    z45: Gimmick door initialization execution determination flag
    z46: The instance ID of the lobby door
    z47: Instance ID of the aisle door
    z48: Point ID for changing the navigation mesh of the lobby door
    z49: Point ID for changing the navigation mesh of the door on the aisle side
    """
    """State 0,1: Set both doors to the initial state"""
    ChangeObjState(z46, 30)
    ChangeObjState(z47, 10)
    """State 4: Wait for transition of both doors"""
    CompareObjState(8, z46, 30, 0)
    CompareObjState(8, z47, 10, 0)
    assert ConditionGroup(8)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z48, 2)
    AddNavimeshAttribute(z49, 2)
    """State 3: Gimmick door initialization execution determination flag: ON"""
    SetEventFlag(z45, 1)
    """State 5: End state"""
    return 0

def event_m10_15_x135(z43=105310, z44=2400000):
    """[Preset] Change the navigation mesh of the king's door
    z43: King door opening and closing flag
    z44: Navimesh change point ID
    """
    """State 0,1: [Reproduction] Navi mesh change of the king's door_SubState"""
    call = event_m10_15_x136()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 2: [Condition] Change the navigation mesh of the king's door_SubState"""
    Label('L0')
    call = event_m10_15_x137(z43=z43)
    if call.Get() == 0:
        """State 3: [Execution] Navi mesh change of the king's door_Closed_SubState"""
        assert event_m10_15_x138(z43=z43, z44=z44)
    elif call.Get() == 1:
        """State 4: [Execution] Change Navimesh of King's Door_Open_SubState"""
        assert event_m10_15_x139(z43=z43, z44=z44)
    """State 5: Rerun"""
    return 0

def event_m10_15_x136():
    """[Reproduction] Navi mesh change of the king's door"""
    """State 0,1: Host? Are you a guest?"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m10_15_x137(z43=105310):
    """[Condition] Change the navigation mesh of the king's door
    z43: King door opening and closing flag
    """
    """State 0,1: Judgment status of king's door open / close flag"""
    CompareEventFlag(0, z43, 0)
    if ConditionGroup(0):
        """State 2: The king's door is closed"""
        return 0
    else:
        """State 3: The king's door is open"""
        return 1

def event_m10_15_x138(z43=105310, z44=2400000):
    """[Execution] Navi mesh change of the king's door_closed
    z43: King door opening and closing flag
    z44: Navimesh change point ID
    """
    """State 0,1: Navimesh disabled"""
    AddNavimeshAttribute(z44, 2)
    """State 2: Has the king's door opened?"""
    CompareEventFlag(0, z43, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x139(z43=105310, z44=2400000):
    """[Execution] Navi mesh change of the king's door_open
    z43: King door opening and closing flag
    z44: Navimesh change point ID
    """
    """State 0,1: Navigation mesh can be passed"""
    DeleteNavimeshAttribute(z44, 2)
    """State 2: Has the king's door closed?"""
    CompareEventFlag(0, z43, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x140(z35=2500, z36=0, z37=15, z38=115000050, z39=0, z40=10159000, z41=4, z42=5010):
    """Character: Petrified: Key guide
    z35: generator
    z36: Death: Global event flag
    z37: Event action
    z38: Petrified: Area and other flags
    z39: Petrified: Global event flag
    z40: Key guide parameters
    z41: Petrification start state ID
    z42: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z35, z41, 0)
    CompareEventStatus(8, z42, 1, 0)
    CompareEventFlag(2, z38, 1)
    CompareEventFlag(3, z39, 1)
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
    CreateKeyGuideArea(34, z40)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z35)
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
            DisplayOwnYesNoMenu(1002, 4, 220, 2, 60537000, 0)
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
                PlayerActionRequest(z37)
                IsPlayerPlayingMotion(0, z37, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z38, 1)
                CompareEventFlag(0, z38, 1)
                SetEventFlag(z39, 1)
                CompareEventFlag(1, z39, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z37, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()

def event_m10_15_x141(z28=_, z29=_, z30=10152515, z31=10152520, z32=10152510, z33=_, z34=_):
    """[Execute] Gimmick door in the middle of the map_Closed
    z28: Instance ID of the door to close
    z29: Instance ID of door to open
    z30: Lobby lever instance ID
    z31: Aisle lever instance ID
    z32: Center lever instance ID
    z33: Point ID to change Navimesh to entry prohibition
    z34: Point ID to change Navimesh to allow entry
    """
    """State 0,3: Has the door closed?"""
    CompareObjState(0, z28, 10, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change: No entry on"""
    AddNavimeshAttribute(z33, 2)
    """State 1,2: Open the door"""
    ChangeObjState(z29, 70)
    """State 5: Navi Mesh Change: No entry prohibited"""
    DeleteNavimeshAttribute(z34, 2)
    """State 6: End state"""
    return 0

def event_m10_15_x142():
    """[Condition] Enemy activation determination_Enemy Spirit"""
    """State 0,1: Was the startup flag turned ON?"""
    CompareEventFlag(0, 115010001, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x143(z27=300020):
    """[Execution] Navi change _ enemy spirit
    z27: Point ID for Navimesh change
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z27, 2)
    """State 2: End state"""
    return 0

def event_m10_15_x144(z19=_):
    """[Conditions] Wall destruction auger activation _ enemy spirit
    z19: Wall instance ID
    """
    """State 0,1: Was the wall broken?"""
    IsObjBroken(0, z19, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x145():
    """[BEST] [Reproduction] Gimmick door in the middle of the map_Relief"""
    """State 0,1: Exit if guest"""
    if IsGuest() != 0:
        """State 3: Finish"""
        return 1
    else:
        """State 2: Execution conditions"""
        return 0

def event_m10_15_x146(z16=10152700, z17=10152705):
    """[BEST] [Condition] Gimmick door in the middle of the map_Relief
    z16: Lobby door OBJ instance ID
    z17: Aisle door OBJ instance ID
    """
    """State 0,1: Remedy execution decision: Are both doors closed?"""
    CompareObjState(8, z16, 10, 0)
    CompareObjState(8, z17, 10, 0)
    if ConditionGroup(8):
        """State 2: Initialization execution"""
        return 0
    else:
        """State 3: Finish"""
        return 1

def event_m10_15_x147(z18=115010020):
    """[BEST] [execution] Gimmick door in the middle of the map _ relief
    z18: Gimmick door initialization execution determination flag
    """
    """State 0,1: Gimmick door initialization execution determination flag: OFF"""
    SetEventFlag(z18, 0)
    assert GetEventFlag(z18) != 1
    """State 2: End state"""
    return 0

def event_m10_15_x148(z16=10152700, z17=10152705, z18=115010020):
    """[BEST] [Preset] Gimmick door in the middle of the map_Relief
    z16: Lobby door OBJ instance ID
    z17: Aisle door OBJ instance ID
    z18: Gimmick door initialization execution determination flag
    """
    """State 0,1: [BEST] [Reproduction] Gimmick door in the middle of the map_Relief_SubState"""
    call = event_m10_15_x145()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [BEST] [Condition] Map's middle gimmick door_Relief_SubState"""
        call = event_m10_15_x146(z16=z16, z17=z17)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [BEST] [Execute] Gimmick door in the middle of the map_Relief_SubState"""
            assert event_m10_15_x147(z18=z18)
    """State 4: Finish"""
    return 0

def event_m10_15_x149(z14=10152530):
    """[DC] [Condition] When the lever is activated, the heel is completely destroyed.
    z14: Lever OBJ instance ID
    """
    """State 0,1: Lever activation judgment"""
    CompareObjState(0, z14, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x150(z15=115020049):
    """[DC] [Execution] Lever is activated to destroy all traps
    z15: All destruction flag
    """
    """State 0,2: Ori A destruction judgment"""
    CompareObjState(0, 10151090, 10, 0)
    if ConditionGroup(0):
        """State 3: Destruction of Ori A"""
        DestroyObj(10151090, 10151090, 0)
    else:
        pass
    """State 4: Ori-B destruction judgment"""
    CompareObjState(0, 10151091, 10, 0)
    if ConditionGroup(0):
        """State 5: Destruction of Ori B"""
        DestroyObj(10151091, 10151091, 0)
    else:
        pass
    """State 6: Ori-C destruction determination"""
    CompareObjState(0, 10151092, 10, 0)
    if ConditionGroup(0):
        """State 7: Destruction of Ori C"""
        DestroyObj(10151092, 10151092, 0)
    else:
        pass
    """State 8: Ori-D destruction judgment"""
    CompareObjState(0, 10151093, 10, 0)
    if ConditionGroup(0):
        """State 9: Destruction of Ori D"""
        DestroyObj(10151093, 10151093, 0)
    else:
        pass
    """State 10: Ori E destruction judgment"""
    CompareObjState(0, 10151094, 10, 0)
    if ConditionGroup(0):
        """State 11: Destruction of Ori E"""
        DestroyObj(10151094, 10151094, 0)
    else:
        pass
    """State 12: Ori-F destruction judgment"""
    CompareObjState(0, 10151041, 10, 0)
    if ConditionGroup(0):
        """State 13: Destruction of Orient F"""
        DestroyObj(10151041, 10151041, 0)
    else:
        pass
    """State 14: Ori-G destruction judgment"""
    CompareObjState(0, 10151070, 10, 0)
    if ConditionGroup(0):
        """State 15: Destruction of Ori G"""
        DestroyObj(10151070, 10151070, 0)
    else:
        pass
    """State 16: Ori-H destruction determination"""
    CompareObjState(0, 10151080, 10, 0)
    if ConditionGroup(0):
        """State 17: Destruction of Ori H"""
        DestroyObj(10151080, 10151080, 0)
    else:
        pass
    """State 1: All destruction flag ON"""
    SetEventFlag(z15, 1)
    """State 18: End state"""
    return 0

def event_m10_15_x151():
    """[DC] [Reproduction] Lever is completely destroyed by lever activation"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x152(z14=10152530, z15=115020049):
    """[DC] [Preset] Lever is completely destroyed by lever activation
    z14: Lever OBJ instance ID
    z15: All destruction flag
    """
    """State 0,1: [DC] [Reproduction] Trap is completely destroyed by lever activation_SubState"""
    assert event_m10_15_x151()
    """State 3: [DC] [Condition] When the lever is activated, the heel is completely destroyed_SubState"""
    assert event_m10_15_x149(z14=z14)
    """State 2: [DC] [Execution] When the lever is activated, the trap is completely destroyed_SubState"""
    assert event_m10_15_x150(z15=z15)
    """State 4: End state"""
    return 0

def event_m10_15_x153(z12=_):
    """[DC] [Condition] Enemy generated by lighthouse lighting
    z12: Lighthouse OBJ instance ID
    """
    """State 0,1: Lighthouse lighting judgment"""
    CompareObjState(0, z12, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x154(z13=_):
    """[DC] [execution] Enemies are generated by lighting the lighthouse
    z13: Enemy generation flag
    """
    """State 0,1: Enemy generation flag ON"""
    SetEventFlag(z13, 1)
    """State 2: Wait for flag ON"""
    CompareEventFlag(0, z13, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x155(z12=_, z13=_):
    """[DC] [Reproduction] Enemy generation by lighthouse lighting
    z12: Lighthouse OBJ instance ID
    z13: Enemy generation flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 6: The guests"""
    return 2
    """State 1: Is the lighthouse already lit?"""
    Label('L0')
    if CompareObjStateId(z12, 30, 0):
        """State 3: Enemy generation flag ON"""
        SetEventFlag(z13, 1)
        assert GetEventFlag(z13) != 0
        """State 5: Already lit"""
        return 1
    else:
        """State 4: Unlit"""
        return 0

def event_m10_15_x156(z12=_, z13=_):
    """[DC] [Preset] Enemy generated by lighthouse lighting
    z12: Lighthouse OBJ instance ID
    z13: Enemy generation flag
    """
    """State 0,1: [DC] [Reproduction] Enemies generated by lighthouse lighting_SubState"""
    call = event_m10_15_x155(z12=z12, z13=z13)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Enemy generated by lighthouse lighting_SubState"""
        assert event_m10_15_x153(z12=z12)
        """State 2: [DC] [Execution] Enemies generated by lighthouse lighting_SubState"""
        assert event_m10_15_x154(z13=z13)
    """State 4: Finish"""
    return 0

def event_m10_15_x157(z10=_, z11=_):
    """[DC] [Preset] Lantern lights by destroying enemies linked to the lighthouse
    z10: Generator ID
    z11: Lantern OBJ instance ID
    """
    """State 0,1: [DC] [Reproduction] Lanterns lit by lighthouse-linked enemy destruction_SubState"""
    call = event_m10_15_x158(z11=z11)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Lantern lights when the lighthouse-linked enemy is destroyed _SubState"""
        assert event_m10_15_x159(z10=z10)
        """State 2: [DC] [Execution] Lantern lights when the lighthouse-linked enemy is destroyed_SubState"""
        assert event_m10_15_x160(z11=z11)
    """State 4: End state"""
    return 0

def event_m10_15_x158(z11=_):
    """[DC] [Reproduction] Lantern lights by destroying the lighthouse-linked enemy
    z11: Lantern OBJ instance ID
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        Goto('L0')
    """State 5: The guests"""
    return 2
    """State 2: Is the lantern already lit?"""
    Label('L0')
    if CompareObjStateId(z11, 70, 0):
        """State 4: Already lit"""
        return 1
    else:
        """State 3: Unlit"""
        return 0

def event_m10_15_x159(z10=_):
    """[DC] [Condition] Lantern lights when lighthouse-linked enemy defeats
    z10: Generator ID
    """
    """State 0,1: Destroyed enemies that appeared in tandem?"""
    IsChrDeadOrRespawnOver(0, z10, 1)
    assert ConditionGroup(0)
    """State 2: Defeat"""
    return 0

def event_m10_15_x160(z11=_):
    """[DC] [Execution] Lantern lights by destroying enemies linked to the lighthouse
    z11: Lantern OBJ instance ID
    """
    """State 0,1: Lantern lighting: 70"""
    ChangeObjState(z11, 70)
    """State 2: End state"""
    return 0

def event_m10_15_x161(z5=10150710, z6=10150711, z7=10150712, z8=10150713):
    """[DC] [Condition] All lantern lighting
    z5: Lantern ①OBJ instance ID
    z6: Lantern ② OBJ instance ID
    z7: Lantern ③ OBJ instance ID
    z8: Lantern ④ OBJ instance ID
    """
    """State 0,1: Did all the lanterns light up?"""
    CompareObjState(8, z5, 20, 0)
    CompareObjState(8, z6, 20, 0)
    CompareObjState(8, z7, 20, 0)
    CompareObjState(8, z8, 20, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_15_x162(z9=115000079):
    """[DC] [Execution] All lantern lighting judgment
    z9: All lighting flag
    """
    """State 0,1: All lighting flag ON"""
    SetEventFlag(z9, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x163():
    """[DC] [Reproduction] All lantern lighting judgment_empty"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x164(z5=10150710, z6=10150711, z7=10150712, z8=10150713, z9=115000079):
    """[DC] [Preset] All lantern lighting judgment
    z5: Lantern ①OBJ instance ID
    z6: Lantern ② OBJ instance ID
    z7: Lantern ③ OBJ instance ID
    z8: Lantern ④ OBJ instance ID
    z9: All lighting flag
    """
    """State 0,1: [DC] [Reproduction] All lantern lighting determination_empty_SubState"""
    assert event_m10_15_x163()
    """State 3: [DC] [Condition] Judgment of all lantern lighting_SubState"""
    assert event_m10_15_x161(z5=z5, z6=z6, z7=z7, z8=z8)
    """State 2: [DC] [Execution] All lantern lighting judgment_SubState"""
    assert event_m10_15_x162(z9=z9)
    """State 4: End state"""
    return 0

def event_m10_15_x165():
    """[DC] [Reproduction] Character invincible until lock destruction"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x166(z1=115020049, z2=_, z3=170001000, z4=_):
    """[DC] [Condition] Characters are invincible and cannot be locked until destruction
    z1: 檻 Destruction flag
    z2: 檻 OBJ instance ID
    z3: Special effect ID
    z4: Generator ID
    """
    """State 0,1: State Invincible and Unlockable: Samurai Destruction Judgment"""
    BecomeInvincibleInCurrentState()
    SetEnemySpEffect(z4, z3, 19, 4)
    CompareEventFlag(0, z1, 1)
    CompareObjState(0, z2, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x167(z3=170001000, z4=_):
    """[DC] [Execution] Cannot lock with character invincible until destruction
    z3: Special effect ID
    z4: Generator ID
    """
    """State 0,1: Unlock disabled"""
    ClearEnemySpEffect(z4, z3)
    """State 2: End state"""
    return 0

def event_m10_15_x168(z1=115020049, z2=_, z3=170001000, z4=_):
    """[DC] [Preset] Character invincible and cannot be locked until destruction
    z1: 檻 Destruction flag
    z2: 檻 OBJ instance ID
    z3: Special effect ID
    z4: Generator ID
    """
    """State 0,1: [DC] [Reproduction] Character invincible and cannot be locked until 檻 destruction_Sky_SubState"""
    assert event_m10_15_x165()
    """State 3: [DC] [Condition] Character invincible and cannot be locked until 檻 destruction_SubState"""
    assert event_m10_15_x166(z1=z1, z2=z2, z3=z3, z4=z4)
    """State 2: [DC] [Execute] Character invincible and cannot be locked until destruction _SubState"""
    assert event_m10_15_x167(z3=z3, z4=z4)
    """State 4: End state"""
    return 0

def event_m10_15_111272():
    """OBJ: Woman Knight (Andiel's Hall): Grave"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_15_x0(z171=104195, z172=10154000, z173=91, z174=7520)

def event_m10_15_111273():
    """OBJ: Woman Knight (Andiel's Hall): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_15_x3(z166=115010100, z167=115020101, z168=104190, z169=10154000, z170=111272, npc1=7520)

def event_m10_15_111274():
    """OBJ: Woman Knight (Andyle Hall): Death Determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_15_x5(z160=90, z161=104195)

def event_m10_15_111276():
    """OBJ: Woman Knight (Andiel's Hall): Appearance Judgment"""
    """State 0,1: Appearance determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 8: Appearance determination: Death determination"""
        CompareEventFlag(0, 104190, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 3: Appearance determination: Generation stop determination"""
            CompareEventFlag(0, 102489, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 4: Appearance determination: Adversity determination"""
                CompareEventFlag(0, 103691, 1)
                CompareEventFlag(1, 103692, 1)
                CompareEventFlag(2, 103693, 1)
                CompareEventFlag(3, 103694, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                elif ConditionGroup(2):
                    pass
                elif ConditionGroup(3):
                    pass
                else:
                    """State 5: Appearance determination: Other map generation stop determination"""
                    CompareEventFlag(8, 102485, 1)
                    CompareEventFlag(8, 102486, 1)
                    CompareEventFlag(8, 102487, 1)
                    CompareEventFlag(8, 102488, 1)
                    if ConditionGroup(8):
                        """State 7: Appearance determination: Appearance allowed"""
                        SetEventFlag(102494, 1)
                        CompareEventFlag(0, 102494, 1)
                        assert ConditionGroup(0)
                        Goto('L0')
                    else:
                        pass
        """State 6: Appearance judgment: Appearance impossible"""
        SetEventFlag(102494, 0)
        CompareEventFlag(0, 102494, 0)
        assert ConditionGroup(0)
    """State 2: Appearance determination: System: End"""
    Label('L0')
    EndMachine()

def event_m10_15_111432():
    """NPC: Enclosed Person: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_15_x0(z171=104340, z172=10154001, z173=161, z174=7710)

def event_m10_15_111433():
    """NPC: Sealed Person: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7710:Royal Sorcerer Navlaan
    event_m10_15_x3(z166=115010140, z167=115020141, z168=104340, z169=10154001, z170=111432, npc1=7710)

def event_m10_15_111435():
    """NPC: Enclosed Person: Black Phantom Appearance"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_15_x54(z101=102810, z102=10001000, z103=530, z104=104340, z105=0, z106=2)

def event_m10_15_118100():
    """White spirit sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_15_x45(z114=540)

def event_m10_15_118210():
    """Multi-use NPC: Shinigami (Female): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_15_x55(z97=10000000, z98=531, z99=0, z100=0)

def event_m10_15_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_15_x56(z95=115020107, z96=33)
    """State 1: System: Exit"""
    EndMachine()

def event_m10_15_4000000():
    """[BEST] Gimmick door in the middle of the map_Relief"""
    """State 0,2: [BEST] [Preset] Map middle gimmick door_Relief_SubState"""
    assert event_m10_15_x148(z16=10152700, z17=10152705, z18=115010020)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4001000():
    """[DC] Lever is completely destroyed when lever is activated"""
    """State 0,2: [DC] [Preset] Deactivation of lever by lever activation_SubState"""
    assert event_m10_15_x152(z14=10152530, z15=115020049)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4002000():
    """[DC] Enemies linked to lighthouses and lanterns_1"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150700, z13=115000070)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7002, z11=10150710)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4002010():
    """[DC] Enemies linked to lighthouses and lanterns_2"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150701, z13=115000071)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7003, z11=10150711)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4002020():
    """[DC] Enemy _3 linked with lighthouse and lantern"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150702, z13=115000072)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7001, z11=10150712)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4002030():
    """[DC] Enemy _4 linked with lighthouse and lantern"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150703, z13=115000073)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7000, z11=10150713)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4003000():
    """[DC] All lantern lighting"""
    """State 0,2: [DC] [Preset] All lantern lighting judgment_SubState"""
    assert event_m10_15_x164(z5=10150710, z6=10150711, z7=10150712, z8=10150713, z9=115000079)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4004000():
    """[DC] Lock Door Opened with "Anne Deal Key" _2"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_15_x4(z162=1005, z163=1105, z164=51030000, z165=115000031)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4005000():
    """[DC] Traveler's Dead _ Petrochemical Stop 1_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_15_x30(z138=8600, z139=0, z140=15, z141=115000051, z142=0, z143=1600, z144=6, z145=4005010)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4005010():
    """[DC] Traveller's Dead _ Petrification Stop 1_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_15_x44(z115=8600, z116=0, z117=115000051, z118=0, z119=0, z120=4005000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4005020():
    """[DC] Traveler dead _ petrochemical stop 1_ switch navigation"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_15_x53(z107=6005020, z108=0, z109=2, z110=115000051, z111=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4006000():
    """[DC] Traveler's Dead _ Petrochemical Stop 2_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_15_x30(z138=8601, z139=0, z140=15, z141=115000052, z142=0, z143=1600, z144=6, z145=4006010)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4006010():
    """[DC] Traveller's Dead _ Petrification Stop 2_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_15_x44(z115=8601, z116=0, z117=115000052, z118=0, z119=0, z120=4006000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4006020():
    """[DC] Traveler's Dead _ Petrochemical Stop 2_ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_15_x53(z107=6006020, z108=0, z109=2, z110=115000052, z111=0)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4007000():
    """[DC] Can't lock with character invincible until 檻 destruction _ Mimic_1"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151092, z3=170001000, z4=8010)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4007010():
    """[DC] Can't lock with character invincible until 檻 destruction _ Mimic_2"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151093, z3=170001000, z4=8011)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4007100():
    """[DC] Cannot lock with character invincible until destruction"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151090, z3=170001000, z4=4030)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4007200():
    """[DC] Character invincible and cannot be locked until 檻 destruction"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151091, z3=170001000, z4=8020)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4007300():
    """[DC] Cannot lock with character invincible until 檻 destruction_Basilisk_1"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151094, z3=170001000, z4=8040)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_15_x64(z88=7100, z89=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_15_x64(z88=7101, z89=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_15_x64(z88=7102, z89=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m10_15_4031000():
    """[DC] NPC White Spirit_Gesture Management_Wyvern"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_15_x68(z85=115000081, z86=800, z87=115020082)
    """State 1: Finish"""
    EndMachine()

