# -*- coding: utf-8 -*-
def event_m10_15_1000():
    """[Insect key] For lantern lighting"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m10_15_x23(z140=10154900)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_1010():
    """[Insect key activation] Lantern lights"""
    """State 0,2: [Preset] Lantern lights_SubState"""
    assert event_m10_15_x75(z79=10154900)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_2000():
    """During the mirror night"""
    """State 0,2: [Preset] Mirror Night _SubState"""
    assert event_m10_15_x127(z48=200000, z49=200000)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_3000():
    """An enemy trapped in the orientation comes out"""
    """State 0,2: [Preset] Enemies start when entering a giant trap or _SubState"""
    assert event_m10_15_x84(z23=300000, z24=300010, z25=300020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4000():
    """Elevator Guardian Dragon's Nest"""
    """State 0,2: [Lib] [Preset] Elevator_SubState"""
    assert event_m10_15_x13(z115=10152000, z116=400010, z117=400000, z118=10152505, z119=10152500)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_4010():
    """Elevator lever _ top"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_15_x18(z145=10152000, z146=10152505, z147=10)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_4020():
    """Elevator lever_bottom"""
    """State 0,2: [Lib] [Preset] Elevator lever_SubState"""
    assert event_m10_15_x18(z145=10152000, z146=10152500, z147=40)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_4030():
    """Elevator_Connection replacement"""
    """State 0,2: [Lib] [Preset] Elevator_Read Connection_SubState"""
    assert event_m10_15_x39(z120=403000, z121=10152000, z122=105425, z123=40, z124=50, z125=1, z126=0)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_4050():
    """For connection_Connection flag OFF"""
    """State 0,3: [Lib] [Preset] Switch the connection flag at the point _SubState"""
    call = event_m10_15_x60(z87=405000, z88=405000, z89=105425, z90=0, z91=1)
    if call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()
    elif call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()

def event_m10_15_5000():
    """Ogre_ Petrochemical Stop_Key Guide"""
    """State 0,3: Character: Petrified: Key Guide_SubState"""
    assert event_m10_15_x140(z33=2500, z34=0, z35=15, z36=115000050, z37=0, z38=10159000, z39=4, z40=5010)
    """State 1: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 2: [Lib] Character: Petrified: Key Guide_SubState"""
    event_m10_15_x30(z132=2500, z133=0, z134=15, z135=115000050, z136=0, z137=10159000, z138=4, z139=5010)
    Quit()

def event_m10_15_5010():
    """Ogre _ Petrification stop_ Appearance setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_15_x44(z109=2500, z110=0, z111=115000050, z112=0, z113=0, z114=5000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_5020():
    """Auger _ petrification stop _ navigation switching"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_15_x53(z103=502000, z104=0, z105=2, flag5=115000050, flag6=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_6000():
    """Mirror Night Mirror_1"""
    """State 0,2: [Preset] Mirror Night Mirror_SubState"""
    assert event_m10_15_x72(z80=10151615, z81=600000, z82=115020010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_6030():
    """Mirror Knight Mirror_4"""
    """State 0,2: [Preset] Mirror Night Mirror_SubState"""
    assert event_m10_15_x72(z80=10151600, z81=603000, z82=115020013)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_6040():
    """Mirror Night Mirror_5"""
    """State 0,2: [Preset] Mirror Night Mirror_SubState"""
    assert event_m10_15_x72(z80=10151620, z81=604000, z82=115020014)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_7000():
    """Boss: Wyvern _ Battle"""
    """State 0,2: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m10_15_x6(flag7=115000081, z148=700000, z149=700000, z150=101, z151=1015000, z152=115020080,
            mode2=0))
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_8000():
    """Bone Dragon Death Treatment"""
    """State 0,2: [Preset] Bone Dragon's Death Process_SubState"""
    # lot:60050000:Aldia Key
    assert event_m10_15_x80(z76=5000, z77=7, z78=1, lot1=60050000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_9000():
    """Wall destruction auger activation_1"""
    """State 0,2: [Preset] Wall destruction auger start event _SubState"""
    assert event_m10_15_x89(z17=10151001, z18=115020005, z19=900000, z20=900001, z21=6000, z22=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_9010():
    """Wall breaking auger activation_2"""
    """State 0,2: [Preset] Wall destruction auger start event _SubState"""
    assert event_m10_15_x89(z17=10151025, z18=115020006, z19=900010, z20=900011, z21=6010, z22=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_10000():
    """Enemy generation when cart is destroyed_1"""
    """State 0,2: [Preset] Enemy generated when cart is destroyed _SubState"""
    assert event_m10_15_x93(z73=10151050, z74=115000015, z75=1000000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_10010():
    """Enemy generation when cart is destroyed_2"""
    """State 0,2: [Preset] Enemy generated when cart is destroyed _SubState"""
    assert event_m10_15_x93(z73=10151062, z74=115000016, z75=1001000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_10020():
    """Enemy generation when destroying cart _3"""
    """State 0,2: [Preset] Enemy generated when cart is destroyed _SubState"""
    assert event_m10_15_x93(z73=10151061, z74=115000017, z75=1002000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_11000():
    """Gimmick door in the middle of the map"""
    """State 0,2: Wait for initialization event to end"""
    assert EventEnded(11010) != 0
    """State 3: [Preset] Map middle gimmick door_SubState"""
    assert (event_m10_15_x97(z26=10152700, z27=10152705, z28=10152515, z29=10152520, z30=10152510, z31=1100000,
            z32=1100001))
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_11010():
    """Gimmick door in the middle of the map_initialization"""
    """State 0,2: [BEST] Relief event finished?"""
    assert EventEnded(4000000) != 0
    """State 3: [Preset] Map middle door_initialization_SubState"""
    assert event_m10_15_x131(z43=115010020, z44=10152700, z45=10152705, z46=1100000, z47=1100001)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_12000():
    """Switch enemy display with gimmick door"""
    """State 0,2: Is the initialization event finished?"""
    assert EventEnded(12010) != 0
    """State 3: [Preset] Enemy display switching at the gimmick door_SubState"""
    assert event_m10_15_x100(z68=10152700, z69=10152705) == 0
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_12010():
    """Enemy display switching_initialization"""
    """State 0,2: [BEST] Relief event finished?"""
    assert EventEnded(4000000) != 0
    """State 3: [Preset] Enemy display switching_initialization_SubState"""
    assert event_m10_15_x105(z64=10152700, z65=10152705)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_13000():
    """Sealed person"""
    """State 0,2: [Preset] Enclosed Person_SubState"""
    assert event_m10_15_x111(z60=10152710, z61=10152525, z62=1300000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_14000():
    """The door that opens with the key of Anne Deal"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_15_x4(z155=1005, z156=1105, z157=51030000, z158=115000030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_15000():
    """Wall 1 visible on the door"""
    """State 0,2: [Preset] Wall visible through the door_SubState"""
    assert event_m10_15_x107(z63=10151001)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_15010():
    """Wall 2 visible on the door"""
    """State 0,2: [Preset] Wall visible through the door_SubState"""
    assert event_m10_15_x107(z63=10151002)
    """State 1: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_16000():
    """Hidden door navigation mesh changes"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_15_x31(z127=10151700, z128=20, z129=1600000, z130=0, z131=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_17000():
    """Switching the wall to be destroyed by the guided auger"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_15_x31(z127=10151002, z128=20, z129=1700000, z130=0, z131=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_18000():
    """Starting conditions for an auger at the foot of the aisle"""
    """State 0,2: [Preset] Startup condition of the auger and reinforced immortal at the foot of the passage_SubState"""
    assert event_m10_15_x115(z57=10151070, z58=1800000, z59=115020040)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_18010():
    """Activation conditions for reinforced immortals at the foot of the aisle"""
    """State 0,2: [Preset] Startup condition of the auger and reinforced immortal at the foot of the passage_SubState"""
    assert event_m10_15_x115(z57=10151080, z58=1801000, z59=115020041)
    """State 1: Finish"""
    EndMachine()
    Quit()

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
    Quit()

def event_m10_15_21000():
    """Wall and door to be destroyed by guided auger"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m10_15_x31(z127=10151020, z128=20, z129=2100000, z130=0, z131=2)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_21010():
    """The door is destroyed when the wall is destroyed_1"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_15_x122(z55=10151020, z56=10150400)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_22000():
    """The door is destroyed when the wall is destroyed_2"""
    """State 0,2: [Preset] Destroy the door when the wall breaks_SubState"""
    assert event_m10_15_x122(z55=10151025, z56=10150433)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_23000():
    """The enemy behind the painting starts 1"""
    """State 0,2: [Preset] The enemy behind the painting is activated_SubState"""
    assert event_m10_15_x123(z52=10151200, z53=20, z54=115020035)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_23010():
    """The enemy behind the painting starts 2"""
    """State 0,2: [Preset] The enemy behind the painting is activated_SubState"""
    assert event_m10_15_x123(z52=10151203, z53=20, z54=115020036)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_23020():
    """The enemy behind the painting starts 3"""
    """State 0,2: [Preset] The enemy behind the painting is activated_SubState"""
    assert event_m10_15_x123(z52=10151201, z53=20, z54=115020037)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_24000():
    """Navi mesh change of the king's door"""
    """State 0,3: [Preset] Change the king's door navigation mesh_SubState"""
    call = event_m10_15_x135(z41=105310, z42=2400000)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
        Quit()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()
        Quit()

def event_m10_15_80000():
    """Fireworks for Regeneration 01_ Entrance building"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_15_x49(z106=1015000, z107=1015099)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_81000():
    """Rebirth Fire 02_Staircase hidden door room to basement"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m10_15_x49(z106=1015100, z107=1015199)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_x0(z164=_, z165=_, z166=_, z167=_):
    """[Lib] NPC: Grave Placement: General purpose
    z164: Death map: Global event flag
    z165: Tomb: OBJ instance ID
    z166: Tomb move to: Generator ID
    z167: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z164, 1)
    IsGraveGeneratable(8, z167, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z165, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z165, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()
    Quit()
    """Unused"""
    """State 7: End state"""
    return 0

def event_m10_15_x1(z161=_, z162=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z161: Global: death flag
    z162: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z162, 10, 0)
    CompareObjState(1, z162, 20, 0)
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
    IsObjSearched(0, z162)
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

def event_m10_15_x2(z159=_, z160=_, npc1=_):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z159: Area other flags: Ghost appearance
    z160: Area other flags: Conversation start
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
    SetEventFlag(z159, 1)
    CompareEventFlag(0, z159, 1)
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
    SetEventFlag(z160, 1)
    CompareEventFlag(0, z160, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m10_15_x3(z159=_, z160=_, z161=_, z162=_, z163=_, npc1=_):
    """[Lib] NPC: Grave: Key guide: General purpose
    z159: Ghost Appearance: Area Other Flag
    z160: Conversation start: Area and other flags
    z161: Death: Global event flag
    z162: Tomb: OBJ instance ID
    z163: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z163, 1, 0)
    CompareEventFlag(9, z159, 1)
    CompareObjState(9, z162, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z160, 1)
        CompareEventFlag(0, z160, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m10_15_x1(z161=z161, z162=z162, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m10_15_x2(z159=z159, z160=z160, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_15_x4(z155=1005, z156=1105, z157=51030000, z158=_):
    """[Lib] Item specified door unlocking_2
    z155: Text ID when opened
    z156: Text ID when not opened
    z157: item
    z158: Key gimmick flag
    """
    """State 0,1: Setting unlocking information"""
    SetUnlockInfo(0, z157, z155, z156, z158, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x5(z153=90, z154=104195):
    """[Lib] NPC: Death determination: General purpose
    z153: Generator ID
    z154: Death map: Global event flag
    """
    """State 0,1: Death determination: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Death determination: branch"""
        CompareEventFlag(0, z154, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 2: Death determination: Wait"""
            IsChrDead(0, z153)
            assert ConditionGroup(0)
            """State 5: Death determination: death flag setting"""
            SetEventFlag(z154, 1)
            CompareEventFlag(0, z154, 1)
            assert ConditionGroup(0)
    """State 4: Death determination: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 6: End state"""
    return 0

def event_m10_15_x6(flag7=115000081, z148=700000, z149=700000, z150=101, z151=1015000, z152=115020080,
                    mode2=0):
    """[Lib] [Preset] Boss Battle Start
    flag7: Boss destruction flag
    z148: Start point ID
    z149: End point ID
    z150: Sound ID
    z151: Boss Battle ID
    z152: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m10_15_x7(flag7=flag7)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m10_15_x8(z148=z148, z149=z149)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m10_15_x9(z150=z150, z151=z151, z152=z152)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m10_15_x10()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m10_15_x11(z151=z151)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m10_15_x12(z150=z150, z151=z151, z152=z152, mode2=mode2)
    """State 7: End state"""
    return 0

def event_m10_15_x7(flag7=115000081):
    """[Reproduction] Boss Battle_Start
    flag7: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(flag7) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m10_15_x8(z148=700000, z149=700000):
    """[Condition] Boss Battle_Start
    z148: Start point ID
    z149: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z148, z149, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z148, z149, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x9(z150=101, z151=1015000, z152=115020080):
    """[Execution] Boss Battle_Start
    z150: Sound ID
    z151: Boss Battle ID
    z152: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z150)
    """State 1: Boss battle start notification"""
    StartBossFight(z151)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z152, 1)
    """State 4: End state"""
    return 0

def event_m10_15_x10():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x11(z151=1015000):
    """[Condition] Boss Battle_End Judgment
    z151: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z151, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x12(z150=101, z151=1015000, z152=115020080, mode2=0):
    """[Execute] Boss Battle_End
    z150: Sound ID
    z151: Boss Battle ID
    z152: Other flags for logic
    mode2: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z152, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z151)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode2) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z150)
    """State 5: End state"""
    return 0

def event_m10_15_x13(z115=10152000, z116=400010, z117=400000, z118=10152505, z119=10152500):
    """[Lib] [Preset] Elevator
    z115: OBJ instance ID of the elevator
    z116: On elevator point ID_
    z117: Elevator point ID_below
    z118: Upper lever OBJ instance ID
    z119: Lower lever OBJ instance ID
    """
    """State 0,1: [Reproduction] Elevator_SubState"""
    assert event_m10_15_x14()
    """State 2: [Condition] Elevator_SubState"""
    call = event_m10_15_x15(z115=z115, z116=z116, z117=z117, z118=z118, z119=z119)
    if call.Get() == 2:
        """State 5: [Execution] Elevator_Return switch after descending_SubState"""
        assert event_m10_15_x43(z115=z115, z117=z117)
    elif call.Get() == 3:
        """State 6: [Execution] Elevator_Return switch after ascending_SubState"""
        assert event_m10_15_x42(z115=z115, z116=z116)
    elif call.Get() == 0:
        """State 4: [Execution] Elevator_Rise_SubState"""
        assert event_m10_15_x16(z115=z115, z116=z116)
    elif call.Get() == 1:
        """State 3: [Execution] Elevator_Descent_SubState"""
        assert event_m10_15_x17(z115=z115, z117=z117)
    """State 7: End state"""
    return 0

def event_m10_15_x14():
    """[Reproduction] Elevator"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x15(z115=10152000, z116=400010, z117=400000, z118=10152505, z119=10152500):
    """[Condition] Elevator
    z115: Elevator OBJ instance ID
    z116: On elevator point ID_
    z117: Elevator point ID_below
    z118: Upper lever OBJ instance ID
    z119: Lower lever OBJ instance ID
    """
    """State 0,1: Elevator position determination"""
    CompareObjState(0, z115, 10, 0)
    CompareObjState(1, z115, 40, 0)
    CompareObjState(2, z115, 80, 0)
    CompareObjState(2, z115, 41, 0)
    CompareObjState(3, z115, 70, 0)
    CompareObjState(3, z115, 30, 0)
    if ConditionGroup(2):
        """State 6,10: Return the switch after descending"""
        return 2
    elif ConditionGroup(3):
        """State 7,11: Return the switch after rising"""
        return 3
    elif ConditionGroup(0):
        """State 4,2: Point or lever standby"""
        IsPlayerInsidePoint(0, z117, z117, 1)
        CompareObjState(0, z118, 74, 0)
        CompareObjState(0, z118, 84, 0)
        assert ConditionGroup(0)
        """State 8: Lift the elevator"""
        return 0
    elif ConditionGroup(1):
        """State 5,3: Point or lever standby_2"""
        IsPlayerInsidePoint(0, z116, z116, 1)
        CompareObjState(0, z119, 74, 0)
        CompareObjState(0, z119, 84, 0)
        assert ConditionGroup(0)
        """State 9: Lower the elevator"""
        return 1

def event_m10_15_x16(z115=10152000, z116=400010):
    """[Execution] Elevator_Rise
    z115: Elevator OBJ instance ID
    z116: On point ID_
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z115, 70)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z115, 30, 0)
    IsPlayerInsidePoint(8, z116, z116, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z115, 71)
    assert CompareObjStateId(z115, 40, 0)
    """State 4: End state"""
    return 0

def event_m10_15_x17(z115=10152000, z117=400000):
    """[Execution] Elevator_Descent
    z115: Elevator OBJ instance ID
    z117: Point ID_below
    """
    """State 0,1: Start moving elevator"""
    ChangeObjState(z115, 80)
    """State 2: Did you get off the elevator?"""
    CompareObjState(8, z115, 41, 0)
    IsPlayerInsidePoint(8, z117, z117, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 3: Switch returns"""
    ChangeObjState(z115, 81)
    assert CompareObjStateId(z115, 10, 0)
    """State 4: End state"""
    return 0

def event_m10_15_x18(z145=10152000, z146=_, z147=_):
    """[Lib] [Preset] Elevator lever
    z145: OBJ instance ID of the elevator
    z146: Lever OBJ instance ID
    z147: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: [Reproduction] Elevator lever_empty_SubState"""
    assert event_m10_15_x19()
    """State 4: [Conditions] Elevator lever_Use determination_SubState"""
    call = event_m10_15_x20(z145=z145, z146=z146, z147=z147)
    if call.Get() == 1:
        """State 3: [Execution] Elevator lever_Key guide valid_SubState"""
        assert event_m10_15_x21(z145=z145, z146=z146, z147=z147)
    elif call.Get() == 0:
        """State 2: [Execution] Elevator lever_Key guide disabled_SubState"""
        assert event_m10_15_x22(z145=z145, z146=z146, z147=z147)
    """State 5: Rerun"""
    return 0

def event_m10_15_x19():
    """[Reproduction] Elevator lever _ empty"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x20(z145=10152000, z146=_, z147=_):
    """[Condition] Elevator lever_use judgment
    z145: OBJ instance ID of the elevator
    z146: Lever OBJ instance ID
    z147: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Elevator position determination"""
    if CompareObjStateId(z145, z147, 0):
        """State 3: Lever activation"""
        return 1
    else:
        """State 2: Lever disable"""
        return 0

def event_m10_15_x21(z145=10152000, z146=_, z147=_):
    """[Execution] Elevator lever_Key guide valid
    z145: OBJ instance ID of the elevator
    z146: Lever OBJ instance ID
    z147: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Enable key guide for lever"""
    DisableObjKeyGuide(z146, 0)
    """State 2: Wait for next decision"""
    CompareObjState(0, z145, z147, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x22(z145=10152000, z146=_, z147=_):
    """[Execute] Elevator lever_key guide disabled
    z145: OBJ instance ID of the elevator
    z146: Lever OBJ instance ID
    z147: Elevator state ID on the opposite side of the lever
    """
    """State 0,1: Disabling the key guide of the lever"""
    DisableObjKeyGuide(z146, 1)
    """State 2: Wait for next decision"""
    CompareObjState(0, z145, z147, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x23(z140=10154900):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z140: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m10_15_x24(z140=z140)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m10_15_x28(z140=z140)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m10_15_x29()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m10_15_x25(z140=z140, mode1=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m10_15_x26(z140=z140, z142=38, z143=3, z144=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m10_15_x27(z140=z140, z141=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m10_15_x24(z140=10154900):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z140: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z140, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z140, 10)
        assert CompareObjStateId(z140, 10, 0)
    elif CompareObjStateId(z140, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z140, 74, 1) and CompareObjStateId(z140, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m10_15_x25(z140=10154900, mode1=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z140: Object instance ID
    mode1: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z140)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode1) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m10_15_x26(z140=10154900, z142=38, z143=3, z144=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z140: Object instance ID
    z142: Key guide type
    z143: Event action
    z144: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z140, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z140, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z140, 30)
        assert CompareObjStateId(z140, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z140, z142, z143)
        assert PlayerIsInEventAction(z143) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z143, 0)
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z140, 74, 0)
        CompareObjState(1, z140, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z144)
            assert CompareObjStateId(z140, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z140, 10)
    """State 3: Rerun"""
    RestartMachine()
    Quit()

def event_m10_15_x27(z140=10154900, z141=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z140: Object instance ID
    z141: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z140, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()
    Quit()
    """Unused"""
    """State 3: End state"""
    return 0

def event_m10_15_x28(z140=10154900):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z140: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z140, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x29():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x30(z132=_, z133=0, z134=15, z135=_, z136=0, z137=_, z138=_, z139=_):
    """[Lib] Character: Petrochemical: Key guide
    z132: generator
    z133: Death: Global event flag
    z134: Event action
    z135: Petrified: Area and other flags
    z136: Petrified: Global event flag
    z137: Key guide parameters
    z138: Petrification start state ID
    z139: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z132, z138, 0)
    CompareEventStatus(8, z139, 1, 0)
    CompareEventFlag(2, z135, 1)
    CompareEventFlag(3, z136, 1)
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
    CreateKeyGuideArea(34, z137)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z132)
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
                PlayerActionRequest(z134)
                IsPlayerPlayingMotion(0, z134, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z135, 1)
                CompareEventFlag(0, z135, 1)
                SetEventFlag(z136, 1)
                CompareEventFlag(1, z136, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z134, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()
    Quit()

def event_m10_15_x31(z127=_, z128=20, z129=_, z130=0, z131=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z127: Object instance ID
    z128: OBJ state ID
    z129: Navimesh switching point ID
    z130: Additional attributes
    z131: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m10_15_x32(z127=z127, z128=z128, z129=z129, z131=z131, z130=z130)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m10_15_x33(z127=z127, z128=z128, z129=z129)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m10_15_x34(z127=z127, z128=z128, z129=z129, z130=z130, z131=z131)
    """State 4: End state"""
    return 0

def event_m10_15_x32(z127=_, z128=20, z129=_, z131=2, z130=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z127: Target OBJ instance ID
    z128: Target OBJ state ID
    z129: Navimesh switching point ID
    z131: Additional attributes
    z130: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z127, z128, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z129, z131)
        DeleteNavimeshAttribute(z129, z130)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m10_15_x33(z127=_, z128=20, z129=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z127: Target OBJ instance ID
    z128: Target OBJ state ID
    z129: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z127, z128, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x34(z127=_, z128=20, z129=_, z130=0, z131=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z127: Target OBJ instance ID
    z128: Target OBJ state ID
    z129: Navimesh switching point ID
    z130: Additional attributes
    z131: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z129, z130)
    DeleteNavimeshAttribute(z129, z131)
    """State 2: End state"""
    return 0

def event_m10_15_x35():
    """[Lib] [Reproduction] Elevator_Connection replacement"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x36(z120=403000, z121=10152000, z123=40, z124=50):
    """[Lib] [Condition] Elevator_Connection replacement
    z120: Replacement point
    z121: OBJ instance ID of the elevator
    z123: Top_Hit group ID
    z124: Bottom_Hit group ID
    """
    """State 0,1: Waiting for intrusion or hitting or hitting a replacement point"""
    IsPlayerInsidePoint(8, z120, z120, 1)
    CompareObjState(8, z121, 70, 0)
    IsPlayerInsidePoint(9, z120, z120, 1)
    CompareObjState(9, z121, 80, 0)
    IsPlayerOnHitGroup(0, z123, 1)
    IsPlayerOnHitGroup(1, z124, 1)
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

def event_m10_15_x37(z120=403000, z122=105425, z125=1, z123=40, z121=10152000):
    """[Lib] [Execution] Elevator_Connection reading rise_Point
    z120: Replacement point
    z122: Global flag for connection
    z125: ON / OFF of global flag
    z123: Top_Hit group ID
    z121: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z122, z125)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z120, z120, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z123, 1)
    IsPlayerInsidePoint(8, z120, z120, 1)
    CompareObjState(8, z121, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_15_x38(z122=105425, z125=1, z123=40, z120=403000, z121=10152000):
    """[Lib] [Execution] Elevator_Upon connection replacement_Hit
    z122: Global flag for connection
    z125: ON / OFF of global flag
    z123: Hit group ID
    z120: Replacement point ID
    z121: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z122, z125)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z123, 0)
    IsPlayerInsidePoint(8, z120, z120, 1)
    CompareObjState(8, z121, 80, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x39(z120=403000, z121=10152000, z122=105425, z123=40, z124=50, z125=1, z126=0):
    """[Lib] [Preset] Elevator_Connection replacement
    z120: Replacement point
    z121: OBJ instance ID of the elevator
    z122: Global flag for connection
    z123: Top_Hit group ID
    z124: Bottom_Hit group ID
    z125: Up_Global flag when rising
    z126: Global flag transition when down
    """
    """State 0,1: [Lib] [Reproduction] Elevator_Read Connection_SubState"""
    assert event_m10_15_x35()
    """State 2: [Lib] [Condition] Elevator_Connection replacement_SubState"""
    call = event_m10_15_x36(z120=z120, z121=z121, z123=z123, z124=z124)
    if call.Get() == 0:
        """State 6: [Lib] [Execution] Elevator_Connection reading rise_Point_SubState"""
        assert event_m10_15_x37(z120=z120, z122=z122, z125=z125, z123=z123, z121=z121)
    elif call.Get() == 1:
        """State 4: [Lib] [Execution] Elevator_Connection replacement descent_Point_SubState"""
        assert event_m10_15_x41(z120=z120, z122=z122, z126=z126, z124=z124, z121=z121)
    elif call.Get() == 2:
        """State 5: [Lib] [Execution] Elevator_Upon Connection Reading_Hit_SubState"""
        assert event_m10_15_x38(z122=z122, z125=z125, z123=z123, z120=z120, z121=z121)
    elif call.Get() == 3:
        """State 3: [Lib] [Execution] Elevator_Under Connection_Read_Hit_SubState"""
        assert event_m10_15_x40(z122=z122, z126=z126, z124=z124, z120=z120, z121=z121)
    """State 7: End state"""
    return 0

def event_m10_15_x40(z122=105425, z126=0, z124=50, z120=403000, z121=10152000):
    """[Lib] [Execution] Elevator_Replaced connection_Hit
    z122: Global flag for connection
    z126: ON / OFF of global flag
    z124: Hit group ID
    z120: Replacement point ID
    z121: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z122, z126)
    """State 2: Wait for next decision"""
    IsPlayerOnHitGroup(0, z124, 0)
    IsPlayerInsidePoint(8, z120, z120, 1)
    CompareObjState(8, z121, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x41(z120=403000, z122=105425, z126=0, z124=50, z121=10152000):
    """[Lib] [Execution] Elevator_Deletion of connection replacement_Point
    z120: Replacement point
    z122: Global flag for connection
    z126: ON / OFF of global flag
    z124: Bottom_Hit group ID
    z121: OBJ instance ID of the elevator
    """
    """State 0,1: Connect event global event flag"""
    SetEventFlag(z122, z126)
    """State 2: Did you get out of the point?"""
    IsPlayerInsidePoint(0, z120, z120, 0)
    assert ConditionGroup(0)
    """State 3: Wait for next decision"""
    IsPlayerOnHitGroup(0, z124, 1)
    IsPlayerInsidePoint(8, z120, z120, 1)
    CompareObjState(8, z121, 70, 0)
    SetConditionGroup(0, 8)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_15_x42(z115=10152000, z116=400010):
    """[Execution] Elevator_Return switch after lift
    z115: Elevator OBJ instance ID
    z116: On point ID_
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z115, 30, 0)
    IsPlayerInsidePoint(8, z116, z116, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z115, 71)
    assert CompareObjStateId(z115, 40, 0)
    """State 3: End state"""
    return 0

def event_m10_15_x43(z115=10152000, z117=400000):
    """[Execution] Elevator_Return switch after descending
    z115: Elevator OBJ instance ID
    z117: Point ID_below
    """
    """State 0,1: Did you get off the elevator?"""
    CompareObjState(8, z115, 41, 0)
    IsPlayerInsidePoint(8, z117, z117, 0)
    IsPlayerAnActor(0, 1)
    DoesActorExist(0, 0)
    SetConditionGroup(8, 0)
    assert HostConditionGroup(8)
    """State 2: Switch returns"""
    ChangeObjState(z115, 81)
    assert CompareObjStateId(z115, 10, 0)
    """State 3: End state"""
    return 0

def event_m10_15_x44(z109=_, z110=0, z111=_, z112=0, z113=0, z114=_):
    """[Lib] Character: Petrified: Appearance setting
    z109: Generator ID
    z110: Death: Global event flag
    z111: Petrified: Area and other flags
    z112: Petrified: Global event flag
    z113: Startup state
    z114: Key guide: Event ID
    """
    """State 0,1: Petrification appearance setting: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 3: Petrification appearance setting: Death determination: Generator"""
        IsChrDead(0, z109)
        if ConditionGroup(0):
            pass
        else:
            """State 4: Petrification appearance setting: Death determination: Global event flag"""
            CompareEventFlag(0, z110, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 5: Petrification: Judgment cancellation decision"""
                CompareEventFlag(0, z111, 1)
                CompareEventFlag(1, z112, 1)
                if ConditionGroup(0):
                    """State 6: Petrified Appearance Setting: Switching startup state"""
                    Label('L0')
                    OverrideGeneratorStartupState(z109, z113)
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

def event_m10_15_x45(z108=540):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z108: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z108)
    """State 3: Appearance: System: End"""
    EndMachine()
    Quit()
    """Unused"""
    """State 4: End state"""
    return 0

def event_m10_15_x46():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x47(z106=_, z107=_):
    """[Lib] [execute] Rebirth fire
    z106: Flag start ID
    z107: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z106, z107, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x48():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x49(z106=_, z107=_):
    """[Lib] [Preset] Rebirth
    z106: Flag start ID
    z107: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m10_15_x46()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m10_15_x48()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m10_15_x47(z106=z106, z107=z107)
    """State 4: End state"""
    return 0

def event_m10_15_x50(flag5=_, flag6=0, z105=2, z104=0, z103=_):
    """[Lib] [Reproduction] Switch Navimesh with flag judgment
    flag5: Other flags
    flag6: Global flag
    z105: Additional attributes
    z104: Delete attribute
    z103: Navimesh switching point ID
    """
    """State 0,1: Flag judgment"""
    if GetEventFlag(flag5) != 0:
        """State 4: Already flag on"""
        Label('L0')
        return 1
    elif GetEventFlag(flag6) != 0:
        Goto('L0')
    else:
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z103, z105)
        DeleteNavimeshAttribute(z103, z104)
        """State 3: Flag OFF"""
        return 0

def event_m10_15_x51(flag5=_, flag6=0):
    """[Lib] [Condition] Switch to Navimesh by flag judgment
    flag5: Other flags
    flag6: Global flag
    """
    """State 0,1: Flag waiting"""
    CompareEventFlag(0, flag5, 1)
    CompareEventFlag(0, flag6, 1)
    assert ConditionGroup(0)
    """State 2: Flag ON"""
    return 0

def event_m10_15_x52(z103=_, z104=0, z105=2):
    """[Lib] [execution] Navi mesh switching by flag judgment
    z103: Navimesh switching point ID
    z104: Additional attributes
    z105: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z103, z104)
    DeleteNavimeshAttribute(z103, z105)
    """State 2: End state"""
    return 0

def event_m10_15_x53(z103=_, z104=0, z105=2, flag5=_, flag6=0):
    """[Lib] [Preset] Navimesh switching by flag judgment
    z103: Navimesh switching point ID
    z104: Additional attributes
    z105: Delete attribute
    flag5: Other flags
    flag6: Global flag
    """
    """State 0,1: [Lib] [Reproduction] Navimesh switching with flag judgment_SubState"""
    call = event_m10_15_x50(flag5=flag5, flag6=flag6, z105=z105, z104=z104, z103=z103)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [Condition] Navigation mesh switching by flag judgment_SubState"""
        assert event_m10_15_x51(flag5=flag5, flag6=flag6)
    """State 2: [Lib] [execution] Navimesh switching with flag judgment_SubState"""
    assert event_m10_15_x52(z103=z103, z104=z104, z105=z105)
    """State 4: End state"""
    return 0

def event_m10_15_x54(z97=102810, z98=10001000, z99=530, z100=104340, z101=0, z102=2):
    """[Lib] NPC Black Phantom Appearance: Online
    z97: Summoning conditions: Global event flag
    z98: Summon range
    z99: Generator ID
    z100: Death: Global event flag
    z101: Appearance: Minimum time
    z102: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z100, 1)
        CompareEventFlag(8, z97, 1)
        IsPlayerInsidePoint(8, z98, z98, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(8):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z100, 1)
            CompareStateTime(1, z101, 3, z102)
            IsPlayerInsidePoint(2, z98, z98, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z99)
                HasNpcPhantomSpawned(0, z99, 1)
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

def event_m10_15_x55(z93=10000000, z94=531, z95=0, z96=0):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z93: Summon range
    z94: Generator ID
    z95: Appearance: Minimum time
    z96: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z93, z93, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z95, 3, z96)
        IsPlayerInsidePoint(1, z93, z93, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z94)
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

def event_m10_15_x56(flag4=115020107, z92=33):
    """[Lib] [Preset] Get trophy
    flag4: Acquisition trigger_other flags
    z92: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(flag4) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, flag4, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z92)
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

def event_m10_15_x58(z87=405000, z88=405000):
    """[Lib] [Condition] Switch the connection flag at the point
    z87: Start point ID
    z88: End point ID
    """
    """State 0,1: Are you in point?"""
    IsPlayerInsidePoint(0, z87, z88, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x59(z89=105425, z90=0, z91=1):
    """[Lib] [Execution] Switch to the connection flag at the point
    z89: Global event flag for connection
    z90: Flag switching
    z91: Wait for next judgment
    """
    """State 0,1: Switch global event flag for connection"""
    SetEventFlag(z89, z90)
    """State 2: Wait for flag transition"""
    CompareEventFlag(0, z89, z90)
    assert ConditionGroup(0)
    """State 3: For next judgment: Has the flag changed?"""
    CompareEventFlag(0, z89, z91)
    assert ConditionGroup(0)
    """State 4: End state"""
    return 0

def event_m10_15_x60(z87=405000, z88=405000, z89=105425, z90=0, z91=1):
    """[Lib] [Preset] Switch the connection flag at the point
    z87: Start point ID
    z88: End point ID
    z89: Global event flag for connection
    z90: Flag switching
    z91: Wait for next judgment
    """
    """State 0,1: [Lib] [Reproduction] Switch the connection flag at the point _SubState"""
    call = event_m10_15_x57()
    if call.Get() == 0:
        """State 3: [Lib] [Condition] Switch connection flag at point _SubState"""
        assert event_m10_15_x58(z87=z87, z88=z88)
        """State 2: [Lib] [Execution] Switch to the connection flag at the point _SubState"""
        assert event_m10_15_x59(z89=z89, z90=z90, z91=z91)
        """State 4: Rerun"""
        return 0
    elif call.Get() == 1:
        """State 5: Guest: Exit"""
        return 1

def event_m10_15_x61(z85=_, z86=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z85: Generator ID
    z86: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z85, z86)
    """State 2: End state"""
    return 0

def event_m10_15_x62(z85=_, z86=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z85: Generator ID
    z86: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z85, z86, 19, 4)
    """State 2: End state"""
    return 0

def event_m10_15_x63(z85=_):
    """[Lib] [DC] [Condition] Transparent characters
    z85: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z85)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x64(z85=_, z86=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z85: Generator ID
    z86: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m10_15_x62(z85=z85, z86=z86)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m10_15_x63(z85=z85)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m10_15_x61(z85=z85, z86=z86)
    """State 4: End state"""
    return 0

def event_m10_15_x65(flag3=115000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    flag3: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(flag3) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m10_15_x66(z83=800):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z83: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z83, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x67(z84=115020082):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z84: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z84, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x68(flag3=115000081, z83=800, z84=115020082):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    flag3: Boss destruction flag
    z83: Boss generator ID
    z84: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m10_15_x65(flag3=flag3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_15_x66(z83=z83)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m10_15_x67(z84=z84)
    """State 4: End state"""
    return 0

def event_m10_15_x69(z80=_):
    """[Reproduction] Mirror night mirror state reproduction
    z80: Mirror instance ID
    """
    """State 0,2: Spiritual determination"""
    if (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
        1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        """State 4: Enemy spirit: End"""
        return 1
    else:
        """State 1: OBJ initialization"""
        InitializeObj(z80)
        """State 3: End state"""
        return 0

def event_m10_15_x70(z81=_):
    """[Conditions] Point intrusion determination
    z81: Point ID
    """
    """State 0,1: Point intrusion standby"""
    IsPlayerInsidePoint(0, z81, z81, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x71(z80=_, z82=_):
    """[Execute] Mirror Split & Enemy Generation
    z80: Mirror instance ID
    z82: Operation flag
    """
    """State 0,1: Generator operation flag ON"""
    SetEventFlag(z82, 1)
    assert (GetStateTime() > 2.4) != 0
    """State 2: OBJ state transition: mirror split"""
    ChangeObjState(z80, 70)
    """State 3: End state"""
    return 0

def event_m10_15_x72(z80=_, z81=_, z82=_):
    """[Preset] Mirror Night Mirror
    z80: Mirror instance ID
    z81: Point ID
    z82: Operation flag
    """
    """State 0,1: [Reproduction] Mirror night mirror state reproduction_SubState"""
    call = event_m10_15_x69(z80=z80)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Point intrusion determination_SubState"""
        assert event_m10_15_x70(z81=z81)
        """State 3: [Execution] Mirror Split & Enemy Generation_SubState"""
        assert event_m10_15_x71(z80=z80, z82=z82)
    """State 4: End state"""
    return 0

def event_m10_15_x73(z79=10154900):
    """[Reproduction] Lantern lighting
    z79: OBJ instance ID of the bug key
    """
    """State 0,1: Is the insect key activated?"""
    if True:
        """State 3: Not running"""
        return 0
    elif CompareObjStateId(z79, 20, 0):
        """State 2: Keep all lights on: 20"""
        ChangeObjState(10151012, 20)
        ChangeObjState(10151013, 20)
        ChangeObjState(10151014, 20)
        ChangeObjState(10151015, 20)
        ChangeObjState(10151016, 20)
        ChangeObjState(10151017, 20)
        """State 4: Activated"""
        return 1

def event_m10_15_x74(z79=10154900):
    """[Condition] Lantern lighting
    z79: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z79, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x75(z79=10154900):
    """[Preset] Lantern lights
    z79: OBJ instance ID of the bug key
    """
    """State 0,1: [Reproduction] Lantern lighting_SubState"""
    call = event_m10_15_x73(z79=z79)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 2: [Condition] Lantern lighting_SubState"""
        assert event_m10_15_x74(z79=z79)
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

def event_m10_15_x78(z76=5000, z77=7, z78=1):
    """[Condition] Death of bone dragon
    z76: Bone Dragon Generator ID
    z77: Logic flag ID
    z78: Logic flag comparison value
    """
    """State 0,1: Has the bone dragon finished the assault?"""
    CompareChrEzStateValue(0, z76, z77, z78, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x79(z76=5000, lot1=60050000):
    """[Execution] Bone Dragon Death Processing
    z76: Bone Dragon Generator ID
    lot1: Item lottery ID
    """
    """State 0,1: Bone dragon death treatment key item acquisition"""
    EnemyActionRequest(z76, 1)
    # lot:60050000:Aldia Key
    AwardItem(lot1, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x80(z76=5000, z77=7, z78=1, lot1=60050000):
    """[Preset] Bone Dragon Death Treatment
    z76: Bone Dragon Generator ID
    z77: Logic flag ID
    z78: Logic flag comparison value
    lot1: Item lottery ID
    """
    """State 0,1: [Reproduction] Bone Dragon Death Processing_SubState"""
    call = event_m10_15_x77()
    if call.Get() == 0:
        """State 3: [Condition] Death process of bone dragon_SubState"""
        assert event_m10_15_x78(z76=z76, z77=z77, z78=z78)
        """State 2: [Execution] Bone Dragon Death Processing_SubState"""
        assert event_m10_15_x79(z76=z76, lot1=lot1)
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

def event_m10_15_x82(z23=300000):
    """[Condition] Enemies are activated when they enter the ori
    z23: Point ID
    """
    """State 0,1: Did you enter the or 檻 that attacked the trap?"""
    IsObjDamaged(0, 10151040, -1, -3, 0)
    IsPlayerInsidePoint(0, z23, z23, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x83(z25=300020):
    """[Execution] Enemies are activated when they enter a large cage or inside
    z25: Point ID for Navimesh change
    """
    """State 0,1: Enemy activation flag ON"""
    SetEventFlag(115010001, 1)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z25, 2)
    """State 3: End state"""
    return 0

def event_m10_15_x84(z23=300000, z24=300010, z25=300020):
    """[Preset] Enemies are activated when entering or encroaching a giant spear
    z23: Point ID for destruction
    z24: Destroyed point ID
    z25: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Enemies start up when entering a giant eagle or sub_State"""
    call = event_m10_15_x81()
    if call.Get() == 2:
        """State 6: [Condition] Enemy activation determination_Enemy Spirit_SubState"""
        assert event_m10_15_x142()
        """State 5: [Execution] Navi Change_Enemy Spirit_SubState"""
        assert event_m10_15_x143(z25=z25)
    elif call.Get() == 0:
        """State 3: [Condition] Enemies start when entering specified area_SubState"""
        assert event_m10_15_x85(z24=z24)
        """State 4: [Execution] Enemies are activated when they enter a giant trap or _SubState"""
        Label('L0')
        assert event_m10_15_x83(z25=z25)
    elif call.Done():
        """State 2: [Condition] Enemies are activated when they enter a large cage or _SubState"""
        assert event_m10_15_x82(z23=z23)
        Goto('L0')
    """State 7: End state"""
    return 0

def event_m10_15_x85(z24=300010):
    """[Condition] Enemies start when entering the specified area
    z24: Point ID
    """
    """State 0,1: Entered the specified area?"""
    IsPlayerInsidePoint(0, z24, z24, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x86(z17=_, z20=_, z18=_):
    """[Reproduction] Wall destruction auger activation
    z17: Wall instance ID
    z20: Navigation switching point ID
    z18: Auger wall destruction flag
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
    if CompareObjStateId(z17, 20, 0):
        """State 3: Ogre wall destruction flag ON"""
        SetEventFlag(z18, 1)
        """State 2: Navi mesh switching"""
        DeleteNavimeshAttribute(z20, 2)
        """State 5: Destroyed"""
        return 0
    else:
        """State 6: Not destroyed"""
        return 1

def event_m10_15_x87(z19=_, z21=_, z17=_, z22=_):
    """[Condition] Wall breaking auger activation
    z19: Point ID
    z21: Generator ID
    z17: Wall instance ID
    z22: Time until entering the point and the auger reacts
    """
    """State 0,1: Did the auger meet the conditions to destroy the wall?"""
    IsPlayerInsidePoint(0, z19, z19, 1)
    CompareChrHpRatio(1, z21, 100, 4)
    IsObjBroken(2, z17, 1)
    if ConditionGroup(0):
        """State 2: Has a certain time elapsed since entering the point? Or did you damage the auger?"""
        CompareStateTime(0, z22, 2, z22)
        CompareChrHpRatio(1, z21, 100, 4)
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

def event_m10_15_x88(z18=_, z20=_, z17=_):
    """[Execution] Wall destruction auger activation_Wall destruction action flag ON
    z18: Auger wall destruction flag
    z20: Navigation switching point ID
    z17: Wall instance ID
    """
    """State 0,1: Ogre wall destruction flag ON"""
    SetEventFlag(z18, 1)
    """State 2: The wall was broken"""
    IsObjBroken(0, z17, 1)
    assert ConditionGroup(0)
    """State 3: Navi mesh switching"""
    DeleteNavimeshAttribute(z20, 2)
    """State 4: End state"""
    return 0

def event_m10_15_x89(z17=_, z18=_, z19=_, z20=_, z21=_, z22=_):
    """[Preset] Wall destruction auger activation
    z17: Wall instance ID
    z18: Auger wall destruction flag
    z19: Point ID
    z20: Navigation switching point ID
    z21: Generator ID
    z22: Time until entering the point and the auger reacts
    """
    """State 0,1: [Reproduction] Wall destruction auger activation_SubState"""
    call = event_m10_15_x86(z17=z17, z20=z20, z18=z18)
    if call.Get() == 2:
        """State 5: [Condition] Wall destruction auger activation_Enemy Spirit_SubState"""
        assert event_m10_15_x144(z17=z17)
        """State 6: [Execution] Wall destruction auger activation_Navimesh switching only_2_SubState"""
        assert event_m10_15_x106(z20=z20)
    elif call.Get() == 0:
        pass
    elif call.Done():
        """State 2: [Condition] Wall destruction auger activation_SubState"""
        call = event_m10_15_x87(z19=z19, z21=z21, z17=z17, z22=z22)
        if call.Get() == 0:
            """State 3: [Execution] Wall destruction auger activation_Wall destruction action flag ON_SubState"""
            assert event_m10_15_x88(z18=z18, z20=z20, z17=z17)
        elif call.Get() == 1:
            """State 4: [Execution] Wall destruction auger activation_Navimesh switching only_SubState"""
            assert event_m10_15_x106(z20=z20)
    """State 7: End state"""
    return 0

def event_m10_15_x90(z73=_, z74=_, z75=_):
    """[Reproduction] Enemy generation when cart is destroyed
    z73: Cart instance ID
    z74: Enemy generation flag
    z75: Point ID for Navimesh change
    """
    """State 0,1: Is the cart destroyed?"""
    if CompareObjStateId(z73, 20, 0):
        """State 2: Enemy generation flag ON"""
        SetEventFlag(z74, 1)
        """State 3: Navigation mesh change"""
        DeleteNavimeshAttribute(z75, 2)
        """State 4: Destroyed"""
        return 0
    else:
        """State 5: Not destroyed"""
        return 1

def event_m10_15_x91(z73=_):
    """[Condition] Enemy is generated when cart is destroyed
    z73: Cart instance ID
    """
    """State 0,1: Waiting for cart destruction"""
    CompareObjState(0, z73, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x92(z74=_, z75=_):
    """[Execution] Enemy generation when cart is destroyed
    z74: Enemy generation flag
    z75: Point ID for Navimesh change
    """
    """State 0,1: Enemy generation flag ON"""
    SetEventFlag(z74, 1)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z75, 2)
    """State 3: End state"""
    return 0

def event_m10_15_x93(z73=_, z74=_, z75=_):
    """[Preset] Enemy generated when cart is destroyed
    z73: Cart instance ID
    z74: Enemy generation flag
    z75: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Enemy generation at the time of cart destruction_SubState"""
    call = event_m10_15_x90(z73=z73, z74=z74, z75=z75)
    if call.Get() == 0:
        pass
    elif call.Done():
        """State 2: [Condition] Enemy generated at the time of cart destruction_SubState"""
        assert event_m10_15_x91(z73=z73)
        """State 3: [Execution] Enemies generated when the cart is destroyed _SubState"""
        assert event_m10_15_x92(z74=z74, z75=z75)
    """State 4: End state"""
    return 0

def event_m10_15_x94(z26=10152700, z27=10152705, z28=10152515, z29=10152520, z30=10152510):
    """[Reproduction] Gimmick door in the middle of the map
    z26: The instance ID of the lobby door
    z27: Instance ID of the aisle door
    z28: The instance ID of the lobby lever
    z29: Instance ID of the aisle lever
    z30: Center lever instance ID
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z26, 80, 0):
        """State 4: Key guide all OFF: Lobby side closed"""
        DisableObjKeyGuide(z28, 1)
        DisableObjKeyGuide(z29, 1)
        DisableObjKeyGuide(z30, 1)
        """State 8: Closed lobby side"""
        return 2
    elif CompareObjStateId(z27, 80, 0):
        """State 5: Key guide all OFF: Closing passage side"""
        DisableObjKeyGuide(z29, 1)
        DisableObjKeyGuide(z28, 1)
        DisableObjKeyGuide(z30, 1)
        """State 9: Aisle side closed"""
        return 3
    elif CompareObjStateId(z26, 30, 0):
        """State 2: Key guide switching: When the lobby is released"""
        DisableObjKeyGuide(z28, 1)
        DisableObjKeyGuide(z29, 0)
        DisableObjKeyGuide(z30, 0)
        """State 6: When the lobby is open"""
        return 0
    elif CompareObjStateId(z27, 30, 0):
        """State 3: Key guide switching: When aisle is released"""
        DisableObjKeyGuide(z29, 1)
        DisableObjKeyGuide(z28, 0)
        DisableObjKeyGuide(z30, 0)
        """State 7: When the aisle is open"""
        return 1

def event_m10_15_x95(z29=_, z30=10152510):
    """[Condition] Gimmick door in the middle of the map
    z29: Lever instance ID to activate
    z30: Center lever instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z29, 74, 0)
    CompareObjState(0, z29, 84, 0)
    CompareObjState(0, z30, 74, 0)
    CompareObjState(0, z30, 84, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x96(z26=_, z27=_, z28=10152515, z29=10152520, z30=10152510, z31=_, z32=_):
    """[Execution] Gimmick door in the middle of the map
    z26: Instance ID of the door to close
    z27: Instance ID of door to open
    z28: Lobby lever instance ID
    z29: Aisle lever instance ID
    z30: Center lever instance ID
    z31: Point ID to change Navimesh to entry prohibition
    z32: Point ID to change Navimesh to allow entry
    """
    """State 0,1: Close the door"""
    ChangeObjState(z26, 80)
    """State 5: Key guide switching: All invalid"""
    DisableObjKeyGuide(z28, 1)
    DisableObjKeyGuide(z29, 1)
    DisableObjKeyGuide(z30, 1)
    """State 4: Has the door closed?"""
    CompareObjState(0, z26, 10, 0)
    assert ConditionGroup(0)
    """State 6: Navi Mesh Change: No entry on"""
    AddNavimeshAttribute(z31, 2)
    """State 2,3: Open the door"""
    ChangeObjState(z27, 70)
    """State 7: Navi Mesh Change: No entry prohibited"""
    DeleteNavimeshAttribute(z32, 2)
    """State 8: End state"""
    return 0

def event_m10_15_x97(z26=10152700, z27=10152705, z28=10152515, z29=10152520, z30=10152510, z31=1100000,
                     z32=1100001):
    """[Preset] Map middle gimmick door
    z26: The instance ID of the lobby door
    z27: Instance ID of the aisle door
    z28: The instance ID of the lobby lever
    z29: Instance ID of the aisle lever
    z30: Center lever instance ID
    z31: Point ID for changing the navigation mesh of the lobby door
    z32: Point ID for changing the navigation mesh of the door on the aisle side
    """
    """State 0,1: [Reproduction] Gimmick door _SubState in the middle of the map"""
    call = event_m10_15_x94(z26=z26, z27=z27, z28=z28, z29=z29, z30=z30)
    if call.Get() == 2:
        """State 6: [Execution] Gimmick door in the middle of the map_Lobby side closing_SubState"""
        assert event_m10_15_x141(z26=z26, z27=z27, z28=z28, z29=z29, z30=z30, z31=z31, z32=z32)
    elif call.Get() == 3:
        """State 7: [Execution] Gimmick door in the middle of the map_Aisle side closed_SubState"""
        assert event_m10_15_x141(z26=z27, z27=z26, z28=z28, z29=z29, z30=z30, z31=z32, z32=z31)
    elif call.Get() == 0:
        """State 2: [Condition] Gimmick door in the middle of the map: When the lobby side is open_SubState"""
        assert event_m10_15_x95(z29=z29, z30=z30)
        """State 4: [Execution] Gimmick door in the middle of the map: _SubState when the lobby is open"""
        assert event_m10_15_x96(z26=z26, z27=z27, z28=z28, z29=z29, z30=z30, z31=z31, z32=z32)
    elif call.Get() == 1:
        """State 3: [Condition] Gimmick door in the middle of the map: When the aisle side is open_SubState"""
        assert event_m10_15_x95(z29=z28, z30=z30)
        """State 5: [Execute] Gimmick door in the middle of the map: When the aisle side is open_SubState"""
        assert event_m10_15_x96(z26=z27, z27=z26, z28=z28, z29=z29, z30=z30, z31=z32, z32=z31)
    """State 8: End state"""
    return 0

def event_m10_15_x98(z72=_, z68=_):
    """[Condition] Switch enemy display with gimmick door
    z72: Hit group on the side that does not erase the enemy
    z68: Instance ID of the door to close
    """
    """State 0,1: Did the door close while riding the specified hit?"""
    IsPlayerOnHitGroup(0, z72, 1)
    IsPlayerOnHitGroup(0, 30, 1)
    SetConditionGroup(8, 0)
    CompareObjState(8, z68, 10, 0)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m10_15_x99(z70=_, z71=_):
    """[Execution] Switch the enemy display at the gimmick door
    z70: Event group ID to stop
    z71: Event group ID to be canceled
    """
    """State 0,1: Enemy stop"""
    PauseEnemyGroup(z70, 1)
    """State 3,2: Enemy stop release"""
    PauseEnemyGroup(z71, 0)
    """State 4: End state"""
    return 0

def event_m10_15_x100(z68=10152700, z69=10152705):
    """[Preset] Switch enemy display with gimmick door
    z68: The instance ID of the lobby door
    z69: Instance ID of the aisle door
    """
    """State 0,1: [Reproduction] Enemy display switching at the gimmick door_SubState"""
    call = event_m10_15_x101(z68=z68, z69=z69)
    if call.Get() == 0:
        """State 2: [Condition] Enemy display switching with gimmick door: Lobby side closes_SubState"""
        assert event_m10_15_x98(z72=10, z68=z68)
        """State 4: [Execution] Enemy display switching at gimmick door: Lobby side closes_SubState"""
        assert event_m10_15_x99(z70=20, z71=21)
    elif call.Get() == 1:
        """State 3: [Condition] Enemy display switching at gimmick door: Passage side closes_SubState"""
        assert event_m10_15_x98(z72=20, z68=z69)
        """State 5: [Execution] Enemy switching with gimmick door: Aisle side closes_SubState"""
        assert event_m10_15_x99(z70=21, z71=20)
    """State 6: Rerun"""
    return 0

def event_m10_15_x101(z68=10152700, z69=10152705):
    """[Reproduction] Enemy switching with gimmick door
    z68: The instance ID of the lobby door
    z69: Instance ID of the aisle door
    """
    """State 0,1: Judgment of door status"""
    if CompareObjStateId(z68, 30, 0):
        """State 2: When the lobby is open"""
        return 0
    elif CompareObjStateId(z69, 30, 0):
        """State 3: When the aisle is open"""
        return 1

def event_m10_15_x102():
    """[Reproduction] Enemy display switching_initialization"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x103(z64=10152700, z65=10152705):
    """[Condition] Enemy display switching_initialization
    z64: Lobby side door OBJ instance ID
    z65: Aisle side door OBJ instance ID
    """
    """State 0,1: PC position and open door judgment"""
    IsPlayerOnHitGroup(0, 20, 1)
    IsPlayerOnHitGroup(8, 30, 1)
    CompareObjState(8, z64, 30, 0)
    SetConditionGroup(0, 8)
    IsPlayerOnHitGroup(1, 10, 1)
    IsPlayerOnHitGroup(9, 30, 1)
    CompareObjState(9, z65, 30, 0)
    SetConditionGroup(1, 9)
    if ConditionGroup(0):
        """State 2: Lobby side"""
        return 0
    elif ConditionGroup(1):
        """State 3: Ogre passage side"""
        return 1

def event_m10_15_x104(z66=_, z67=_):
    """[Execute] Enemy display switching_initialization
    z66: Event group ID to stop
    z67: Event group ID to be canceled
    """
    """State 0,1: Switch enemy display"""
    PauseEnemyGroup(z66, 1)
    PauseEnemyGroup(z67, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x105(z64=10152700, z65=10152705):
    """[Preset] Enemy display switching_initialization
    z64: Lobby side door OBJ instance ID
    z65: Aisle side door OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemy display switching_initialization_SubState"""
    assert event_m10_15_x102()
    """State 2: [Condition] Enemy display switching_initialization_SubState"""
    call = event_m10_15_x103(z64=z64, z65=z65)
    if call.Get() == 0:
        """State 4: [Execution] Enemy display switching_initialization: Lobby side display_SubState"""
        assert event_m10_15_x104(z66=21, z67=20)
    elif call.Get() == 1:
        """State 3: [Execute] Enemy display switching_initialization: passage side display_SubState"""
        assert event_m10_15_x104(z66=20, z67=21)
    """State 5: End state"""
    return 0

def event_m10_15_x106(z20=_):
    """[Execution] Wall destruction auger activation_Navimesh switching only
    z20: Navigation switching point ID
    """
    """State 0,1: Navi mesh switching"""
    DeleteNavimeshAttribute(z20, 2)
    """State 2: End state"""
    return 0

def event_m10_15_x107(z63=_):
    """[Preset] Wall visible on the door
    z63: Instance ID of the wall OBJ visible on the door
    """
    """State 0,1: [Reproduction] Wall _SubState visible in the door"""
    assert event_m10_15_x108()
    """State 2: [Condition] Wall visible through the door_SubState"""
    assert event_m10_15_x109(z63=z63)
    """State 3: [Execution] Wall that looks like a door_SubState"""
    assert event_m10_15_x110(z63=z63)
    """State 4: End state"""
    return 0

def event_m10_15_x108():
    """[Reproduction] Wall visible on the door"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x109(z63=_):
    """[Conditions] Wall visible on the door
    z63: Instance ID of the wall OBJ visible on the door
    """
    """State 0,1: Have you checked the wall?"""
    IsObjSearched(0, z63)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x110(z63=_):
    """[Execution] Wall visible on the door
    z63: Instance ID of the wall OBJ visible on the door
    """
    """State 0,1: Show message"""
    # action:1100:"Locked"
    DisplayOwnOkMenu(1100, 0, 0, 190, 0, 0, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x111(z60=10152710, z61=10152525, z62=1300000):
    """[Preset] Enclosed people
    z60: Magic barrier OBJ instance ID
    z61: Lever OBJ instance ID
    z62: Point ID for Navimesh change
    """
    """State 0,1: [Reproduction] Enclosed person_SubState"""
    call = event_m10_15_x112(z60=z60, z62=z62)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Enclosed person_SubState"""
        assert event_m10_15_x113(z61=z61)
        """State 3: [Execution] Enclosed Person_SubState"""
        assert event_m10_15_x114(z60=z60, z62=z62)
    """State 4: End state"""
    return 0

def event_m10_15_x112(z60=10152710, z62=1300000):
    """[Reproduction] Enclosed people
    z60: Magic barrier OBJ instance ID
    z62: Point ID for Navimesh change
    """
    """State 0,1: Has the seal already been released?"""
    if GetEventFlag(102810) != 0:
        pass
    else:
        Goto('L0')
    """State 3: Has the magic barrier been initialized?"""
    if IsGuest() != 1 and CompareObjStateId(z60, 10, 0):
        """State 4: [Relief] Canceling the magic barrier: 70"""
        ChangeObjState(z60, 70)
        assert CompareObjStateId(z60, 20, 0)
    else:
        pass
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z62, 2)
    """State 6: Canceled"""
    return 1
    """State 5: Not open"""
    Label('L0')
    return 0

def event_m10_15_x113(z61=10152525):
    """[Condition] Enclosed person
    z61: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z61, 72, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x114(z60=10152710, z62=1300000):
    """[Execution] Enclosed person
    z60: Magic barrier OBJ instance ID
    z62: Point ID for Navimesh change
    """
    """State 0,1: Break the magic barrier: 70"""
    ChangeObjState(z60, 70)
    assert CompareObjStateId(z60, 20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z62, 2)
    """State 3: Sealed Person: Turns on the seal release flag"""
    SetEventFlag(102810, 1)
    """State 4: End state"""
    return 0

def event_m10_15_x115(z57=_, z58=_, z59=_):
    """[Preset] Activation conditions for an auger and a reinforced immortal who are at the foot of the aisle
    z57: 檻 OBJ instance ID
    z58: Point ID for Navimesh change
    z59: An activation flag for enemies in the cage
    """
    """State 0,1: [Reproduction] Starting condition of the auger and reinforced immortal at the foot of the passage_SubState"""
    call = event_m10_15_x116(z57=z57)
    if call.Get() == 0:
        """State 2: [Conditions] Activation conditions for the auger and reinforced immortal at the foot of the aisle_SubState"""
        assert event_m10_15_x117(z57=z57)
    elif call.Get() == 1:
        pass
    """State 3: [Execution] Activation conditions for the auger and reinforced immortal who are at the foot of the passage_SubState"""
    assert event_m10_15_x118(z58=z58, z59=z59)
    """State 4: End state"""
    return 0

def event_m10_15_x116(z57=_):
    """[Reproduction] Starting conditions for an auger and a reinforced immortal man
    z57: 檻 OBJ instance ID
    """
    """State 0,1: 判定 Judgment of OBJ status"""
    if CompareObjStateId(z57, 10, 0):
        """State 2: Undestructed"""
        return 0
    else:
        """State 3: Destroyed"""
        return 1

def event_m10_15_x117(z57=_):
    """[Conditions] Conditions for starting an auger and a reinforced immortal person at the foot of the passage
    z57: 檻 OBJ instance ID
    """
    """State 0,1: 檻 Destruction of OBJ destruction"""
    CompareObjState(0, z57, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x118(z58=_, z59=_):
    """[Execution] Starting conditions for an auger and a reinforced immortal person at the foot of the passage
    z58: Point ID for Navimesh change
    z59: An activation flag for enemies in the cage
    """
    """State 0,1: Navimesh change processing"""
    DeleteNavimeshAttribute(z58, 2)
    """State 2: Turn on the activation flag for enemies in the cage"""
    SetEventFlag(z59, 1)
    """State 3: End state"""
    return 0

def event_m10_15_x119():
    """[Reproduction] Destroy the door when the wall is destroyed"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x120(z55=_):
    """[Condition] When the wall is destroyed, the door is also destroyed.
    z55: Wall OBJ instance ID
    """
    """State 0,1: Wall waiting for destruction"""
    IsObjBroken(0, z55, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x121(z56=_):
    """[Execution] When the wall is destroyed, the door is also destroyed.
    z56: Door OBJ instance ID
    """
    """State 0,1: Door destruction"""
    DestroyObj(z56, z56, 0)
    """State 2: End state"""
    return 0

def event_m10_15_x122(z55=_, z56=_):
    """[Preset] Destroy the door when the wall is destroyed
    z55: Wall OBJ instance ID
    z56: Door OBJ instance ID
    """
    """State 0,1: [Reproduction] Destroy the door when the wall is destroyed_Sky_SubState"""
    assert event_m10_15_x119()
    """State 3: [Condition] The door is destroyed when the wall is destroyed."""
    assert event_m10_15_x120(z55=z55)
    """State 2: [Execution] When the wall is destroyed, the door is also destroyed._SubState"""
    assert event_m10_15_x121(z56=z56)
    """State 4: End state"""
    return 0

def event_m10_15_x123(z52=_, z53=20, z54=_):
    """[Preset] The enemy behind the painting starts
    z52: Instance ID of the painting OBJ
    z53: State ID when the painting OBJ is destroyed
    z54: Enemy action start flag
    """
    """State 0,1: [Reproduction] The enemy behind the painting is activated_SubState"""
    call = event_m10_15_x124(z52=z52, z53=z53, z54=z54)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] The enemy behind the painting is activated_SubState"""
        assert event_m10_15_x125(z52=z52, z53=z53)
        """State 3: [Execution] The enemy behind the painting is activated_SubState"""
        assert event_m10_15_x126(z54=z54)
    """State 4: End state"""
    return 0

def event_m10_15_x124(z52=_, z53=20, z54=_):
    """[Reproduction] The enemy behind the painting starts
    z52: Instance ID of the painting OBJ
    z53: State ID when the painting OBJ is destroyed
    z54: Enemy action start flag
    """
    """State 0,1: State judgment of painting OBJ"""
    if CompareObjStateId(z52, z53, 0):
        """State 2: Turn on enemy action start flag"""
        SetEventFlag(z54, 1)
        """State 4: Destroyed"""
        return 1
    else:
        """State 3: Undestructed"""
        return 0

def event_m10_15_x125(z52=_, z53=20):
    """[Condition] The enemy behind the painting starts
    z52: Instance ID of the painting OBJ
    z53: State ID when the painting OBJ is destroyed
    """
    """State 0,1: Has the painting OBJ been destroyed?"""
    CompareObjState(0, z52, z53, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x126(z54=_):
    """[Execution] The enemy behind the painting starts
    z54: Enemy action start flag
    """
    """State 0,1: Turn on enemy action start flag"""
    SetEventFlag(z54, 1)
    """State 2: End state"""
    return 0

def event_m10_15_x127(z48=200000, z49=200000):
    """[Preset] Mirror Night
    z48: Judgment area start point ID
    z49: End point ID of the judgment area
    """
    """State 0,1: [Reproduction] _SubState during Mirror Knight"""
    assert event_m10_15_x128()
    """State 2: [Condition] Mirror Knight's _ Area_SubState"""
    assert event_m10_15_x129(z51=1, z48=z48, z49=z49)
    """State 3: [Execution] Mirror Knight's _ Area_SubState"""
    assert event_m10_15_x130(z50=1)
    """State 4: [Conditions] Mirror Night Room_Outside Area_SubState"""
    assert event_m10_15_x129(z51=0, z48=z48, z49=z49)
    """State 5: [Execution] During Mirror Knight_Outside Area_SubState"""
    assert event_m10_15_x130(z50=0)
    """State 6: End state"""
    return 0

def event_m10_15_x128():
    """[Reproduction] Mirror Night"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x129(z51=_, z48=200000, z49=200000):
    """[Conditions] Mirror Night
    z51: Area inside / outside judgment
    z48: Judgment area start point ID
    z49: End point ID of the judgment area
    """
    """State 0,1: Area inside / outside judgment"""
    IsPlayerInsidePoint(0, z48, z49, z51)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x130(z50=_):
    """[Execution] Mirror Night
    z50: Special drawing to set
    """
    """State 0,1: Drawing switching"""
    SetSpecialDrawingMode(z50)
    """State 2: End state"""
    return 0

def event_m10_15_x131(z43=115010020, z44=10152700, z45=10152705, z46=1100000, z47=1100001):
    """[Preset] Map middle gimmick door_initialization
    z43: Gimmick door initialization execution determination flag
    z44: The instance ID of the lobby door
    z45: Instance ID of the aisle door
    z46: Point ID for changing the navigation mesh of the lobby door
    z47: Point ID for changing the navigation mesh of the door on the aisle side
    """
    """State 0,1: [Reproduction] Gimmick door in the middle of the map_Initialization_SubState"""
    call = event_m10_15_x132()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [Condition] Gimmick door in the middle of the map_Initialization_SubState"""
        call = event_m10_15_x133(z43=z43)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 3: [Execution] Gimmick door in the middle of the map_Initialization_SubState"""
            assert event_m10_15_x134(z43=z43, z44=z44, z45=z45, z46=z46, z47=z47)
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

def event_m10_15_x133(z43=115010020):
    """[Condition] Gimmick door in the middle of the map_Initialization
    z43: Gimmick door initialization execution determination flag
    """
    """State 0,1: Initialization execution judgment"""
    CompareEventFlag(0, 115010020, 1)
    if ConditionGroup(0):
        """State 3: Finish"""
        return 1
    else:
        """State 2: Initialization execution"""
        return 0

def event_m10_15_x134(z43=115010020, z44=10152700, z45=10152705, z46=1100000, z47=1100001):
    """[Execution] Gimmick door in the middle of the map
    z43: Gimmick door initialization execution determination flag
    z44: The instance ID of the lobby door
    z45: Instance ID of the aisle door
    z46: Point ID for changing the navigation mesh of the lobby door
    z47: Point ID for changing the navigation mesh of the door on the aisle side
    """
    """State 0,1: Set both doors to the initial state"""
    ChangeObjState(z44, 30)
    ChangeObjState(z45, 10)
    """State 4: Wait for transition of both doors"""
    CompareObjState(8, z44, 30, 0)
    CompareObjState(8, z45, 10, 0)
    assert ConditionGroup(8)
    """State 2: Navigation mesh change"""
    DeleteNavimeshAttribute(z46, 2)
    AddNavimeshAttribute(z47, 2)
    """State 3: Gimmick door initialization execution determination flag: ON"""
    SetEventFlag(z43, 1)
    """State 5: End state"""
    return 0

def event_m10_15_x135(z41=105310, z42=2400000):
    """[Preset] Change the navigation mesh of the king's door
    z41: King door opening and closing flag
    z42: Navimesh change point ID
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
    call = event_m10_15_x137(z41=z41)
    if call.Get() == 0:
        """State 3: [Execution] Navi mesh change of the king's door_Closed_SubState"""
        assert event_m10_15_x138(z41=z41, z42=z42)
    elif call.Get() == 1:
        """State 4: [Execution] Change Navimesh of King's Door_Open_SubState"""
        assert event_m10_15_x139(z41=z41, z42=z42)
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

def event_m10_15_x137(z41=105310):
    """[Condition] Change the navigation mesh of the king's door
    z41: King door opening and closing flag
    """
    """State 0,1: Judgment status of king's door open / close flag"""
    CompareEventFlag(0, z41, 0)
    if ConditionGroup(0):
        """State 2: The king's door is closed"""
        return 0
    else:
        """State 3: The king's door is open"""
        return 1

def event_m10_15_x138(z41=105310, z42=2400000):
    """[Execution] Navi mesh change of the king's door_closed
    z41: King door opening and closing flag
    z42: Navimesh change point ID
    """
    """State 0,1: Navimesh disabled"""
    AddNavimeshAttribute(z42, 2)
    """State 2: Has the king's door opened?"""
    CompareEventFlag(0, z41, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x139(z41=105310, z42=2400000):
    """[Execution] Navi mesh change of the king's door_open
    z41: King door opening and closing flag
    z42: Navimesh change point ID
    """
    """State 0,1: Navigation mesh can be passed"""
    DeleteNavimeshAttribute(z42, 2)
    """State 2: Has the king's door closed?"""
    CompareEventFlag(0, z41, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x140(z33=2500, z34=0, z35=15, z36=115000050, z37=0, z38=10159000, z39=4, z40=5010):
    """Character: Petrified: Key guide
    z33: generator
    z34: Death: Global event flag
    z35: Event action
    z36: Petrified: Area and other flags
    z37: Petrified: Global event flag
    z38: Key guide parameters
    z39: Petrification start state ID
    z40: Petrification appearance event
    """
    """State 0,16: Petrochemical: Start"""
    CompareChrStartUpState(8, z33, z39, 0)
    CompareEventStatus(8, z40, 1, 0)
    CompareEventFlag(2, z36, 1)
    CompareEventFlag(3, z37, 1)
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
    CreateKeyGuideArea(34, z38)
    """State 3: Petrochemical: Key guide: Waiting for input"""
    IsChrSearched(0, z33)
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
                PlayerActionRequest(z35)
                IsPlayerPlayingMotion(0, z35, 1)
                assert ConditionGroup(0)
                """State 7: Petrification: Event action: Standby: Elapsed time"""
                CompareStateTime(0, 1.3, 2, 1.3)
                assert ConditionGroup(0)
                """State 8: Petrification: Petrified"""
                # goods:60537000:Fragrant Branch of Yore
                ConsumeItem(60537000, 1)
                SetEventFlag(z36, 1)
                CompareEventFlag(0, z36, 1)
                SetEventFlag(z37, 1)
                CompareEventFlag(1, z37, 1)
                if ConditionGroup(0):
                    pass
                elif ConditionGroup(1):
                    pass
                """State 9: Petrochemical: Event action: Wait"""
                IsPlayerPlayingMotion(0, z35, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 4: Petrochemical: System: Re-execution"""
        RestartMachine()
        Quit()
    """State 1: Petrochemical: System: End"""
    Label('L1')
    EndMachine()
    Quit()

def event_m10_15_x141(z26=_, z27=_, z28=10152515, z29=10152520, z30=10152510, z31=_, z32=_):
    """[Execute] Gimmick door in the middle of the map_Closed
    z26: Instance ID of the door to close
    z27: Instance ID of door to open
    z28: Lobby lever instance ID
    z29: Aisle lever instance ID
    z30: Center lever instance ID
    z31: Point ID to change Navimesh to entry prohibition
    z32: Point ID to change Navimesh to allow entry
    """
    """State 0,3: Has the door closed?"""
    CompareObjState(0, z26, 10, 0)
    assert ConditionGroup(0)
    """State 4: Navi Mesh Change: No entry on"""
    AddNavimeshAttribute(z31, 2)
    """State 1,2: Open the door"""
    ChangeObjState(z27, 70)
    """State 5: Navi Mesh Change: No entry prohibited"""
    DeleteNavimeshAttribute(z32, 2)
    """State 6: End state"""
    return 0

def event_m10_15_x142():
    """[Condition] Enemy activation determination_Enemy Spirit"""
    """State 0,1: Was the startup flag turned ON?"""
    CompareEventFlag(0, 115010001, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x143(z25=300020):
    """[Execution] Navi change _ enemy spirit
    z25: Point ID for Navimesh change
    """
    """State 0,1: Navigation mesh change"""
    DeleteNavimeshAttribute(z25, 2)
    """State 2: End state"""
    return 0

def event_m10_15_x144(z17=_):
    """[Conditions] Wall destruction auger activation _ enemy spirit
    z17: Wall instance ID
    """
    """State 0,1: Was the wall broken?"""
    IsObjBroken(0, z17, 1)
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

def event_m10_15_x146(z15=10152700, z16=10152705):
    """[BEST] [Condition] Gimmick door in the middle of the map_Relief
    z15: Lobby door OBJ instance ID
    z16: Aisle door OBJ instance ID
    """
    """State 0,1: Remedy execution decision: Are both doors closed?"""
    CompareObjState(8, z15, 10, 0)
    CompareObjState(8, z16, 10, 0)
    if ConditionGroup(8):
        """State 2: Initialization execution"""
        return 0
    else:
        """State 3: Finish"""
        return 1

def event_m10_15_x147(flag2=115010020):
    """[BEST] [execution] Gimmick door in the middle of the map _ relief
    flag2: Gimmick door initialization execution determination flag
    """
    """State 0,1: Gimmick door initialization execution determination flag: OFF"""
    SetEventFlag(flag2, 0)
    assert GetEventFlag(flag2) != 1
    """State 2: End state"""
    return 0

def event_m10_15_x148(z15=10152700, z16=10152705, flag2=115010020):
    """[BEST] [Preset] Gimmick door in the middle of the map_Relief
    z15: Lobby door OBJ instance ID
    z16: Aisle door OBJ instance ID
    flag2: Gimmick door initialization execution determination flag
    """
    """State 0,1: [BEST] [Reproduction] Gimmick door in the middle of the map_Relief_SubState"""
    call = event_m10_15_x145()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [BEST] [Condition] Map's middle gimmick door_Relief_SubState"""
        call = event_m10_15_x146(z15=z15, z16=z16)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [BEST] [Execute] Gimmick door in the middle of the map_Relief_SubState"""
            assert event_m10_15_x147(flag2=flag2)
    """State 4: Finish"""
    return 0

def event_m10_15_x149(z13=10152530):
    """[DC] [Condition] When the lever is activated, the heel is completely destroyed.
    z13: Lever OBJ instance ID
    """
    """State 0,1: Lever activation judgment"""
    CompareObjState(0, z13, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m10_15_x150(z14=115020049):
    """[DC] [Execution] Lever is activated to destroy all traps
    z14: All destruction flag
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
    SetEventFlag(z14, 1)
    """State 18: End state"""
    return 0

def event_m10_15_x151():
    """[DC] [Reproduction] Lever is completely destroyed by lever activation"""
    """State 0,1: End state"""
    return 0

def event_m10_15_x152(z13=10152530, z14=115020049):
    """[DC] [Preset] Lever is completely destroyed by lever activation
    z13: Lever OBJ instance ID
    z14: All destruction flag
    """
    """State 0,1: [DC] [Reproduction] Trap is completely destroyed by lever activation_SubState"""
    assert event_m10_15_x151()
    """State 3: [DC] [Condition] When the lever is activated, the heel is completely destroyed_SubState"""
    assert event_m10_15_x149(z13=z13)
    """State 2: [DC] [Execution] When the lever is activated, the trap is completely destroyed_SubState"""
    assert event_m10_15_x150(z14=z14)
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

def event_m10_15_x154(flag1=_):
    """[DC] [execution] Enemies are generated by lighting the lighthouse
    flag1: Enemy generation flag
    """
    """State 0,1: Enemy generation flag ON"""
    SetEventFlag(flag1, 1)
    """State 2: Wait for flag ON"""
    CompareEventFlag(0, flag1, 1)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m10_15_x155(z12=_, flag1=_):
    """[DC] [Reproduction] Enemy generation by lighthouse lighting
    z12: Lighthouse OBJ instance ID
    flag1: Enemy generation flag
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
        SetEventFlag(flag1, 1)
        assert GetEventFlag(flag1) != 0
        """State 5: Already lit"""
        return 1
    else:
        """State 4: Unlit"""
        return 0

def event_m10_15_x156(z12=_, flag1=_):
    """[DC] [Preset] Enemy generated by lighthouse lighting
    z12: Lighthouse OBJ instance ID
    flag1: Enemy generation flag
    """
    """State 0,1: [DC] [Reproduction] Enemies generated by lighthouse lighting_SubState"""
    call = event_m10_15_x155(z12=z12, flag1=flag1)
    if call.Get() == 2:
        pass
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Enemy generated by lighthouse lighting_SubState"""
        assert event_m10_15_x153(z12=z12)
        """State 2: [DC] [Execution] Enemies generated by lighthouse lighting_SubState"""
        assert event_m10_15_x154(flag1=flag1)
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
    event_m10_15_x0(z164=104195, z165=10154000, z166=91, z167=7520)
    Quit()

def event_m10_15_111273():
    """OBJ: Woman Knight (Andiel's Hall): Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7520:Lucatiel of Mirrah
    event_m10_15_x3(z159=115010100, z160=115020101, z161=104190, z162=10154000, z163=111272, npc1=7520)
    Quit()

def event_m10_15_111274():
    """OBJ: Woman Knight (Andyle Hall): Death Determination"""
    """State 0,1: [Lib] NPC: Death determination: General purpose_SubState"""
    event_m10_15_x5(z153=90, z154=104195)
    Quit()

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
    Quit()

def event_m10_15_111432():
    """NPC: Enclosed Person: Tomb"""
    """State 0,1: [Lib] NPC: Grave Placement: General Purpose_SubState"""
    event_m10_15_x0(z164=104340, z165=10154001, z166=161, z167=7710)
    Quit()

def event_m10_15_111433():
    """NPC: Sealed Person: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:7710:Royal Sorcerer Navlaan
    event_m10_15_x3(z159=115010140, z160=115020141, z161=104340, z162=10154001, z163=111432, npc1=7710)
    Quit()

def event_m10_15_111435():
    """NPC: Enclosed Person: Black Phantom Appearance"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online_SubState"""
    event_m10_15_x54(z97=102810, z98=10001000, z99=530, z100=104340, z101=0, z102=2)
    Quit()

def event_m10_15_118100():
    """White spirit sign display"""
    """State 0,1: [Lib] NPC White Phantom Appearance: Unconditional_SubState"""
    event_m10_15_x45(z108=540)
    Quit()

def event_m10_15_118210():
    """Multi-use NPC: Shinigami (Female): Black Phantom Appears"""
    """State 0,1: [Lib] NPC Black Phantom Appearance: Online: Unconditional_SubState"""
    event_m10_15_x55(z93=10000000, z94=531, z95=0, z96=0)
    Quit()

def event_m10_15_120130():
    """Trophy: Akertyra"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m10_15_x56(flag4=115020107, z92=33)
    """State 1: System: Exit"""
    EndMachine()
    Quit()

def event_m10_15_4000000():
    """[BEST] Gimmick door in the middle of the map_Relief"""
    """State 0,2: [BEST] [Preset] Map middle gimmick door_Relief_SubState"""
    assert event_m10_15_x148(z15=10152700, z16=10152705, flag2=115010020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4001000():
    """[DC] Lever is completely destroyed when lever is activated"""
    """State 0,2: [DC] [Preset] Deactivation of lever by lever activation_SubState"""
    assert event_m10_15_x152(z13=10152530, z14=115020049)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4002000():
    """[DC] Enemies linked to lighthouses and lanterns_1"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150700, flag1=115000070)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7002, z11=10150710)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4002010():
    """[DC] Enemies linked to lighthouses and lanterns_2"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150701, flag1=115000071)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7003, z11=10150711)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4002020():
    """[DC] Enemy _3 linked with lighthouse and lantern"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150702, flag1=115000072)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7001, z11=10150712)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4002030():
    """[DC] Enemy _4 linked with lighthouse and lantern"""
    """State 0,3: [DC] [Preset] Enemies generated by lighthouse lighting_SubState"""
    assert event_m10_15_x156(z12=10150703, flag1=115000073)
    """State 2: [DC] [Preset] Lantern lit by destroying enemies linked to the lighthouse_SubState"""
    assert event_m10_15_x157(z10=7000, z11=10150713)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4003000():
    """[DC] All lantern lighting"""
    """State 0,2: [DC] [Preset] All lantern lighting judgment_SubState"""
    assert event_m10_15_x164(z5=10150710, z6=10150711, z7=10150712, z8=10150713, z9=115000079)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4004000():
    """[DC] Lock Door Opened with "Anne Deal Key" _2"""
    """State 0,2: [Lib] Item specified door unlocking_SubState"""
    assert event_m10_15_x4(z155=1005, z156=1105, z157=51030000, z158=115000031)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4005000():
    """[DC] Traveler's Dead _ Petrochemical Stop 1_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_15_x30(z132=8600, z133=0, z134=15, z135=115000051, z136=0, z137=1600, z138=6, z139=4005010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4005010():
    """[DC] Traveller's Dead _ Petrification Stop 1_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_15_x44(z109=8600, z110=0, z111=115000051, z112=0, z113=0, z114=4005000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4005020():
    """[DC] Traveler dead _ petrochemical stop 1_ switch navigation"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_15_x53(z103=6005020, z104=0, z105=2, flag5=115000051, flag6=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4006000():
    """[DC] Traveler's Dead _ Petrochemical Stop 2_ Key Guide"""
    """State 0,2: [Lib] Character: Petrified: Key Guide_SubState"""
    assert event_m10_15_x30(z132=8601, z133=0, z134=15, z135=115000052, z136=0, z137=1600, z138=6, z139=4006010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4006010():
    """[DC] Traveller's Dead _ Petrification Stop 2_ Appearance Setting"""
    """State 0,2: [Lib] Character: Petrified: Appearance setting_SubState"""
    assert event_m10_15_x44(z109=8601, z110=0, z111=115000052, z112=0, z113=0, z114=4006000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4006020():
    """[DC] Traveler's Dead _ Petrochemical Stop 2_ Navigation Switch"""
    """State 0,2: [Lib] [Preset] Navigation mesh switching by flag judgment_SubState"""
    assert event_m10_15_x53(z103=6006020, z104=0, z105=2, flag5=115000052, flag6=0)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4007000():
    """[DC] Can't lock with character invincible until 檻 destruction _ Mimic_1"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151092, z3=170001000, z4=8010)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4007010():
    """[DC] Can't lock with character invincible until 檻 destruction _ Mimic_2"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151093, z3=170001000, z4=8011)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4007100():
    """[DC] Cannot lock with character invincible until destruction"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151090, z3=170001000, z4=4030)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4007200():
    """[DC] Character invincible and cannot be locked until 檻 destruction"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151091, z3=170001000, z4=8020)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4007300():
    """[DC] Cannot lock with character invincible until 檻 destruction_Basilisk_1"""
    """State 0,2: [DC] [Preset] Cannot be locked and invincible until 檻 destruction_SubState"""
    assert event_m10_15_x168(z1=115020049, z2=10151094, z3=170001000, z4=8040)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_15_x64(z85=7100, z86=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_15_x64(z85=7101, z86=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m10_15_x64(z85=7102, z86=96960000)
    """State 1: Finish"""
    EndMachine()
    Quit()

def event_m10_15_4031000():
    """[DC] NPC White Spirit_Gesture Management_Wyvern"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m10_15_x68(flag3=115000081, z83=800, z84=115020082)
    """State 1: Finish"""
    EndMachine()
    Quit()

