# -*- coding: utf-8 -*-
def event_m20_24_1000():
    """When the bell rings, enemies are operational_1"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020010, z40=20241040, z41=20241050)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_1010():
    """When the bell rings, enemies are operational_2"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020010, z40=20241050, z41=20241040)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_1020():
    """When the bell rings, the enemy is in operation _3"""
    """State 0,2: [Preset] Enemy operation when ringing bell_bell single_substate"""
    assert event_m20_24_x119(z42=224020011, z43=20241100)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_2000():
    """Shortcut drawbridge"""
    """State 0,1: Disable OBJ sync"""
    SetObjSync(20241010, 0)
    """State 3: [Reproduction] Shortcut drawbridge_SubState"""
    call = event_m20_24_x96(z56=20241010, z57=200000)
    if call.Get() == 0:
        """State 5: [Condition] Shortcut drawbridge_SubState"""
        assert event_m20_24_x97(z55=20241000)
        """State 4: [Execution] Shortcut drawbridge_SubState"""
        assert event_m20_24_x98(z54=200000)
    elif call.Done():
        pass
    """State 2: Finish"""
    EndMachine()

def event_m20_24_3000():
    """A huge candlestick ignites"""
    """State 0,2: [Preset] Fire on a huge candlestick_SubState"""
    assert event_m20_24_x131(z16=20240700, z17=70, z18=224000050)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4000():
    """Boss: Queen Knight B Battle"""
    """State 0,2: Is the poly drama replay event finished?"""
    assert EventEnded(4010) != 0
    """State 3: [Lib] [Preset] Boss Battle Cut Scene No _SubState"""
    assert (event_m20_24_x5(z137=224000081, z138=400000, z139=400000, z140=101, z141=2024000, z142=224020080,
            mode3=0))
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010():
    """Boss: Queen Knight B_ Poly Play"""
    """State 0,2: [Lib] [Preset] Boss Battle_Poly Play Playback_SubState"""
    assert event_m20_24_x15(z131=20240600, z132=202410, z133=224000082, z134=401000, z135=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4100():
    """Navimesh change of pillars destroyed in Queen Knight Battle B 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242303, z120=20, z121=410000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4110():
    """Navimesh change of pillars destroyed in Queen Knight Battle B 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242302, z120=20, z121=411000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4120():
    """Navimesh change of pillars destroyed in Queen Knight Battle B 3"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242300, z120=20, z121=412000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4130():
    """Navimesh change of pillars destroyed in Queen Knight Battle B 4"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242301, z120=20, z121=413000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4140():
    """Navimesh change of pillars destroyed in Queen Knight Battle B 5"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242306, z120=20, z121=414000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4150():
    """Change Navimesh of Pillar destroyed in Queen Knight Battle B 6"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242308, z120=20, z121=415000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4160():
    """Navimesh change of pillars destroyed in Queen Knight Battle B 7"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242307, z120=20, z121=416000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4170():
    """Navimesh change of pillar destroyed in knight knight battle B 8"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20242309, z120=20, z121=417000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_7000():
    """[Insect key] Hidden door ① For activation"""
    """State 0,2: [Lib] [Asynchronous] [Preset] Bug key (wall) _SubState"""
    assert event_m20_24_x16(z126=20241800)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_7010():
    """[Insect key] Hidden door ①"""
    """State 0,2: [Lib] [Preset] Hidden door 1_Face SFX_SubState"""
    assert event_m20_24_x26(z124=20241800, val2=20240010, z125=0.6, val3=1.5)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_7020():
    """[Insect key] Hidden door ①_Navimesh change"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20241500, z120=20, z121=702000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_8000():
    """King whose defense power fluctuates with the number of possessed items"""
    """State 0,2: [Preset] Wang _SubState whose defense power varies with the number of possessed items"""
    assert event_m20_24_x99()
    """State 1: Finish"""
    EndMachine()

def event_m20_24_8010():
    """BGM playback of the king's room"""
    """State 0,2: [Preset] BGM playback of the king's room_SubState"""
    assert event_m20_24_x127(z37=224000081, z38=102)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_8020():
    """Boss battle with the king"""
    """State 0,3: [Preset] King_Boss Battle_SubState"""
    assert event_m20_24_x147(z28=224000086, z29=802010, z30=2024010, z31=224020085, z32=224000088)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_8030():
    """Get the king's ring"""
    """State 0,2: [Preset] Get the king's ring_SubState"""
    assert event_m20_24_x114(z46=100804, z47=20246500)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_8040():
    """King's white door management"""
    """State 0,2: [Preset] King's white door management_SubState"""
    assert event_m20_24_x136()
    """State 1: Finish"""
    EndMachine()

def event_m20_24_8050():
    """King adversity"""
    """State 0,2: [Preset] King's hostility determination_SubState"""
    assert event_m20_24_x140(z33=230, z34=224000088)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_9000():
    """Oil bottle 1"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_24_x40(z105=20242200, z106=20242250, z107=10, z108=240, z109=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_24_x44(z100=20242250, z101=10, z102=240, z103=0, z104=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_9010():
    """Oil bottle 2"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_24_x40(z105=20242201, z106=20242251, z107=20, z108=240, z109=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_24_x44(z100=20242251, z101=20, z102=240, z103=0, z104=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_9020():
    """Oil bottle 3"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_24_x40(z105=20242202, z106=20242252, z107=10, z108=241, z109=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_24_x44(z100=20242252, z101=10, z102=241, z103=0, z104=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_9030():
    """Oil bottle 4"""
    """State 0,2: [Lib] [Preset] Oil 壺 SubState"""
    assert event_m20_24_x40(z105=20242203, z106=20242253, z107=10, z108=242, z109=1)
    """State 3: [Lib] [Preset] Tar material change_SubState"""
    assert event_m20_24_x44(z100=20242253, z101=10, z102=242, z103=0, z104=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12000():
    """Enemy generation stops due to tombstone destruction 1"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242400, z45=224000020)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12010():
    """Enemy generation stops due to tombstone destruction 2"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242401, z45=224000021)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12020():
    """Enemy generation stops due to tombstone destruction 3"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242402, z45=224000022)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12030():
    """Enemy generation stops due to tombstone destruction 4"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242403, z45=224000023)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12040():
    """Enemy generation stops due to tombstone destruction5"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242404, z45=224000024)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12050():
    """Enemy generation stops due to tombstone destruction6"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242405, z45=224000025)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12060():
    """Enemy generation stops due to tombstone destruction7"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242406, z45=224000026)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12070():
    """Enemy generation stops due to tombstone destruction 8"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242407, z45=224000027)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12080():
    """Enemy generation stops due to tombstone destruction 9"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242408, z45=224000028)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_12090():
    """Enemy generation stops due to tombstone destruction 10"""
    """State 0,2: [Preset] Generation of enemies stops due to tombstone destruction_SubState"""
    assert event_m20_24_x122(z44=20242409, z45=224000029)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_13000():
    """Hidden Door Navi Mesh Change 1"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20241550, z120=20, z121=1300000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_13010():
    """Hidden door navigation mesh change 2"""
    """State 0,2: [Lib] [Preset] Switch Navimesh according to OBJ state_SubState"""
    assert event_m20_24_x27(z119=20241560, z120=20, z121=1301000, z122=0, z123=2)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_80000():
    """Regenerative fire 01"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_24_x36(z110=2024000, z111=2024099)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_81000():
    """Regenerative fire 02_Gap under the entrance stairs"""
    """State 0,2: [Lib] [Preset] Reproduction fire _SubState"""
    assert event_m20_24_x36(z110=2024100, z111=2024199)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_90000():
    """Trophy_Vanclad"""
    """State 0,2: [Lib] [Preset] Get Trophy_SubState"""
    assert event_m20_24_x46(z94=224000086, z95=11)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_x0(z152=0, z153=0, z154=50380000, z155=5000000):
    """[Lib] Warp between maps after poly play
    z152: Pre-warp poly play ID
    z153: Poly Play ID after Warp
    z154: Map ID
    z155: Point ID
    """
    """State 0,1: Poly drama warp"""
    PlayCutsceneAndWarpToMap(z152, z153, z154, z155, 0)
    assert CutsceneWarpEnded() != 0
    """State 2: End state"""
    return 0

def event_m20_24_x1(z148=104010, z149=20244000, z150=241, z151=5060):
    """[Lib] NPC: Grave Placement: General purpose
    z148: Death map: Global event flag
    z149: Tomb: OBJ instance ID
    z150: Tomb move to: Generator ID
    z151: NPC information parameter ID
    """
    """State 0,1: Grave Placement: Start"""
    IsPlayerInTheMap(0, 1, 0)
    assert ConditionGroup(0)
    """State 2: Grave placement: branch"""
    CompareEventFlag(8, z148, 1)
    IsGraveGeneratable(8, z151, 1)
    if ConditionGroup(8):
        """State 4: Grave Placement: Death"""
        ChangeOwnObjState(20)
        CompareObjState(0, z149, 20, 0)
        assert ConditionGroup(0)
        """State 6: Grave Placement: Warp Move"""
    else:
        """State 3: Grave Placement: Survival"""
        ChangeOwnObjState(10)
        CompareObjState(0, z149, 10, 0)
        assert ConditionGroup(0)
    """State 5: Grave Placement: System: Finish"""
    EndMachine()

def event_m20_24_x2(z145=104010, z146=20244000, npc1=5060):
    """[Lib] NPC: Grave: Key Guide: Key Guide
    z145: Global: death flag
    z146: Grave OBJ instance ID
    npc1: NPC information parameter ID
    """
    """State 0,1,5: Key guide: Grave display judgment"""
    CompareObjState(0, z146, 10, 0)
    CompareObjState(1, z146, 20, 0)
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
    IsObjSearched(0, z146)
    IsPlayerInTheMap(1, 0, 0)
    if ConditionGroup(0):
        """State 3: Key Guide: Use Soul dialog"""
        # action:1211:"[ChrName]\nOffer souls to grave?\nSouls needed: %d", npc:5060:Grave Warden Agdayne
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

def event_m20_24_x3(z143=224010100, z144=224020101, npc1=5060):
    """[Lib] NPC: Grave: Key Guide: Appearance of Ghosts
    z143: Area other flags: Ghost appearance
    z144: Area other flags: Conversation start
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
    SetEventFlag(z143, 1)
    CompareEventFlag(0, z143, 1)
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
    SetEventFlag(z144, 1)
    CompareEventFlag(0, z144, 1)
    assert ConditionGroup(0)
    """State 10: End state"""
    return 0

def event_m20_24_x4(z143=224010100, z144=224020101, z145=104010, z146=20244000, z147=111022, npc1=5060):
    """[Lib] NPC: Grave: Key guide: General purpose
    z143: Ghost Appearance: Area Other Flag
    z144: Conversation start: Area and other flags
    z145: Death: Global event flag
    z146: Tomb: OBJ instance ID
    z147: Grave event ID
    npc1: NPC information parameter ID
    """
    """State 0,1: Key guide: Start"""
    IsPlayerInTheMap(8, 1, 0)
    CompareEventStatus(8, z147, 1, 0)
    CompareEventFlag(9, z143, 1)
    CompareObjState(9, z146, 20, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(9):
        """State 3: Key guide: Start conversation: Set flag"""
        SetEventFlag(z144, 1)
        CompareEventFlag(0, z144, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        """State 4: [Lib] NPC: Grave: Key Guide: Key Guide_SubState"""
        assert event_m20_24_x2(z145=z145, z146=z146, npc1=npc1)
        """State 5: [Lib] NPC: Grave: Key Guide: Ghost Appearance_SubState"""
        assert event_m20_24_x3(z143=z143, z144=z144, npc1=npc1)
    """State 2: Key Guide: System: Exit"""
    EndMachine()

def event_m20_24_x5(z137=224000081, z138=400000, z139=400000, z140=101, z141=2024000, z142=224020080,
                    mode3=0):
    """[Lib] [Preset] Boss Battle Start
    z137: Boss destruction flag
    z138: Start point ID
    z139: End point ID
    z140: Sound ID
    z141: Boss Battle ID
    z142: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: [Reproduction] Boss Battle_Start_SubState"""
    call = event_m20_24_x6(z137=z137)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] Boss Battle_Start_SubState"""
        assert event_m20_24_x7(z138=z138, z139=z139)
        """State 3: [Execution] Boss Battle_Start_SubState"""
        assert event_m20_24_x8(z140=z140, z141=z141, z142=z142)
        """State 2: [Reproduction] Boss Battle_Sky_SubState"""
        assert event_m20_24_x9()
        """State 6: [Condition] Boss Battle_End Judgment_SubState"""
        assert event_m20_24_x10(z141=z141)
        """State 4: [Execution] Boss Battle_End_SubState"""
        assert event_m20_24_x11(z140=z140, z141=z141, z142=z142, mode3=mode3)
    """State 7: End state"""
    return 0

def event_m20_24_x6(z137=224000081):
    """[Reproduction] Boss Battle_Start
    z137: Boss destruction flag
    """
    """State 0,1: Are you destroying the boss?"""
    if GetEventFlag(z137) != 0:
        """State 3: Defeated the boss"""
        return 1
    else:
        """State 2: Not destroy the boss"""
        return 0

def event_m20_24_x7(z138=400000, z139=400000):
    """[Condition] Boss Battle_Start
    z138: Start point ID
    z139: End point ID
    """
    """State 0,1: Did you enter the boss room point?"""
    IsPlayerInsidePoint(8, z138, z139, 1)
    IsHost(8, 1, 0)
    SetConditionGroup(0, 8)
    IsPlayerInsidePoint(9, z138, z139, 1)
    IsHost(9, 0, 0)
    SetConditionGroup(0, 9)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x8(z140=101, z141=2024000, z142=224020080):
    """[Execution] Boss Battle_Start
    z140: Sound ID
    z141: Boss Battle ID
    z142: Other flags for logic
    """
    """State 0,3: Boss BGM playback"""
    PlaySoundAtPoint(z140)
    """State 1: Boss battle start notification"""
    StartBossFight(z141)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z142, 1)
    """State 4: End state"""
    return 0

def event_m20_24_x9():
    """[Reproduction] Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x10(z141=2024000):
    """[Condition] Boss Battle_End Judgment
    z141: Boss Battle ID
    """
    """State 0,1: Did you beat the boss?"""
    IsEventBossKill(0, z141, 0, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x11(z140=101, z141=2024000, z142=224020080, mode3=0):
    """[Execute] Boss Battle_End
    z140: Sound ID
    z141: Boss Battle ID
    z142: Other flags for logic
    mode3: BGM stop time
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z142, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z141)
    """State 4: BGM stop standby"""
    assert (GetStateTime() > mode3) != 0
    """State 3: Boss BGM stop"""
    StopSoundAtPoint(z140)
    """State 5: End state"""
    return 0

def event_m20_24_x12(z133=224000082):
    """[Reproduction] Boss Battle_Poly Play Replay
    z133: Poly drama played flag
    """
    """State 0,2: Wait for in-game start"""
    assert InGame() != 0
    """State 1: Has the boss been destroyed? Is the poly drama already played?"""
    if GetEventFlag(z133) != 0:
        """State 4: No poly play"""
        Label('L0')
        return 1
    elif (ComparePlayerPhantom(0) != 1 and ComparePlayerPhantom(1) != 1 and ComparePlayerPhantom(3) !=
          1 and ComparePlayerPhantom(2) != 1 and ComparePlayerPhantom(4) != 1):
        Goto('L0')
    else:
        """State 3: Poly play"""
        return 0

def event_m20_24_x13(z131=20240600):
    """[Condition] Boss Battle_Poly Play Replay
    z131: White door OBJ instance ID
    """
    """State 0,1: Did you pass the white door?"""
    assert CompareObjStateId(z131, 100, 0)
    """State 2: End state"""
    return 0

def event_m20_24_x14(z132=202410, z133=224000082, z134=401000, z136=1):
    """[Execution] Boss Battle _ Poly Play Replay
    z132: Poly play ID
    z133: Poly drama played flag
    z134: Warp point ID
    z136: Weight until poly play
    """
    """State 0,1: For time adjustment"""
    assert (GetStateTime() > 1) != 0
    """State 2: Poly drama playback started"""
    PlayCutscene(z132, 1, 1)
    assert (CutscenePlaying() == 1) != 0
    """State 3: Replaying a poly play"""
    assert (not CutscenePlaying()) != 0
    """State 4,6: Remote character sync"""
    WarpAndSyncRemoteCharacters()
    """State 5: Host judgment"""
    if IsGuest() != 1:
        """State 8: Poly drama replayed flag ON"""
        SetEventFlag(z133, 1)
        """State 7: Warp to boss battle start position"""
        WarpPlayersWithinMap(z134)
        """State 9: Save execution"""
        SaveExecution()
    else:
        pass
    """State 10: End state"""
    return 0

def event_m20_24_x15(z131=20240600, z132=202410, z133=224000082, z134=401000, z135=1):
    """[Lib] [Preset] Boss Battle_Poly Play Replay
    z131: White door instance ID
    z132: Poly play ID
    z133: Poly drama played flag
    z134: Warp point ID
    z135: Wait time
    """
    """State 0,1: [Reproduction] Boss Battle_Poly Play Playback_SubState"""
    call = event_m20_24_x12(z133=z133)
    if call.Get() == 0:
        """State 3: [Condition] Boss Battle_Poly Play Playback_SubState"""
        assert event_m20_24_x13(z131=z131)
        """State 2: [Execution] Boss Battle_Poly Play_SubState"""
        assert event_m20_24_x14(z132=z132, z133=z133, z134=z134, z136=1)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_24_x16(z126=20241800):
    """[Lib] [Asynchronous] [Preset] Bug key (wall)
    z126: Object instance ID
    """
    """State 0,1: [Private] [Asynchronous] [Reproduction] Bug key _SubState"""
    call = event_m20_24_x17(z126=z126)
    if call.Get() == 1:
        """State 7: End of reproduction"""
        return 0
    elif call.Get() == 2:
        """State 5: [Private] [Asynchronous] [Condition] Guest Bug Key_SubState"""
        assert event_m20_24_x21(z126=z126)
        """State 6: [Lib] [Execution] Dummy_SubState"""
        assert event_m20_24_x22()
    elif call.Done():
        """State 2: [Private] [Asynchronous] [Condition] Bug key _SubState"""
        # goods:60536000:Pharros' Lockstone
        call = event_m20_24_x18(z126=z126, mode2=1, goods3=60536000)
        if call.Get() == 0:
            """State 3: [Private] [Asynchronous] [Execution] Use bug key _SubState"""
            # goods:60536000:Pharros' Lockstone
            assert event_m20_24_x19(z126=z126, z128=38, z129=3, z130=1, goods2=60536000)
        elif call.Done():
            """State 4: [Private] [Asynchronous] [Execution] Insect key unavailable dialog _SubState"""
            # goods:60536000:Pharros' Lockstone
            event_m20_24_x20(z126=z126, z127=1, goods1=60536000)
            Quit()
    """State 8: End of execution"""
    return 1

def event_m20_24_x17(z126=20241800):
    """[Private] [Asynchronous] [Reproduction] Bug Key
    z126: Object instance ID
    """
    """State 0,1: OBJ status judgment"""
    if IsGuest() != 0:
        """State 5: Guest termination"""
        return 2
    elif CompareObjStateId(z126, 30, 0):
        """State 2: OBJ initialization: 10"""
        Label('L0')
        ChangeObjState(z126, 10)
        assert CompareObjStateId(z126, 10, 0)
    elif CompareObjStateId(z126, 70, 0):
        Goto('L0')
    elif CompareObjStateId(z126, 74, 1) and CompareObjStateId(z126, 20, 1):
        pass
    else:
        """State 4: After execution"""
        return 1
    """State 3: Before execution"""
    return 0

def event_m20_24_x18(z126=20241800, mode2=1, goods3=60536000):
    """[Private] [Asynchronous] [Condition] Host insect key
    z126: Object instance ID
    mode2: Number consumed
    goods3: Consumption items
    """
    """State 0,1: Judgment to examine"""
    IsObjSearched(0, z126)
    assert ConditionGroup(0)
    """State 2: Available branch"""
    # goods:60536000:Pharros' Lockstone
    if (ItemCount(goods3, 1, 1, 0) > mode2) != 0:
        """State 3: Available end"""
        return 0
    else:
        """State 4: Unusable termination"""
        return 1

def event_m20_24_x19(z126=20241800, z128=38, z129=3, z130=1, goods2=60536000):
    """[Private] [Asynchronous] [Execution] Use bug key dialog
    z126: Object instance ID
    z128: Key guide type
    z129: Event action
    z130: Number consumed
    goods2: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:3000:"⑱： Move"
    DisplayYesNoMenu(3000, 1.8, z126, 190, 0, 0, 0)
    # action:1002:"Use %s?", goods:60536000:Pharros' Lockstone
    DisplayYesNoMenu(1002, 1.8, z126, 190, 2, goods2, 0)
    assert YesNoMenuDisplay() != 1
    """State 2: Result judgment"""
    if (YesNoMenuResult() == 1) != 0:
        """State 7: Bug key transition waiting: 30"""
        ChangeObjState(z126, 30)
        assert CompareObjStateId(z126, 30, 0)
        """State 4: Action request to player"""
        ObjAnimationPlayerControlRequest(z126, z128, z129)
        assert PlayerIsInEventAction(z129) != 0
        """State 5: OBJ status judgment"""
        IsPlayerPlayingMotion(0, z129, 0)
        # goods:60536000:Pharros' Lockstone
        DoesPlayerHaveItem(0, goods2, 0, 5, 1, 1, 0)
        CompareObjState(1, z126, 74, 0)
        CompareObjState(1, z126, 20, 0)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 6: Insect key consumption"""
            # goods:60536000:Pharros' Lockstone
            ConsumeItem(goods2, z130)
            assert CompareObjStateId(z126, 20, 0)
            """State 9: End state"""
            return 0
    else:
        pass
    """State 8: Bug key: Initial state: 10"""
    ChangeObjState(z126, 10)
    """State 3: Rerun"""
    RestartMachine()

def event_m20_24_x20(z126=20241800, z127=1, goods1=60536000):
    """[Private] [Asynchronous] [Execution] Unusable key
    z126: Object instance ID
    z127: Number consumed
    goods1: Consumption items
    """
    """State 0,1: Dialog display"""
    # action:1013:"No %s\nin inventory", goods:60536000:Pharros' Lockstone
    DisplayOkMenu(1013, 0, 0, z126, 190, 2, goods1, 0)
    assert OkMenuDisplay() != 1
    """State 2: Rerun"""
    RestartMachine()

def event_m20_24_x21(z126=20241800):
    """[Private] [Asynchronous] [Condition] Guest Bug Key
    z126: Object instance ID
    """
    """State 0,1: OBJ standby"""
    CompareObjState(0, z126, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x22():
    """[Lib] [execution] dummy"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x23(z124=20241800, val2=20240010):
    """[Reproduction] Hidden door 1_face SFX
    z124: OBJ instance ID of the bug key
    val2: Event light ID
    """
    """State 0,1: Is the insect key activated?"""
    if CompareObjStateId(z124, 20, 0):
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

def event_m20_24_x24(z124=20241800):
    """[Conditions] Hidden door 1_Face SFX
    z124: OBJ instance ID of the bug key
    """
    """State 0,1: Waiting for insect key activation"""
    CompareObjState(0, z124, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x25(z124=20241800, val2=20240010, z125=0.6, val3=1.5):
    """[Execution] Hidden door 1_Face SFX
    z124: OBJ instance ID of the bug key
    val2: Event light ID
    z125: Light fade time
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
        SetPointLightEnabled(val2, 1, z125)
        assert (GetStateTime() > val3) != 0
        """State 3: Hidden door OBJ state transition: 30"""
        ChangeOwnObjState(30)
    """State 6: Finish"""
    return 0

def event_m20_24_x26(z124=20241800, val2=20240010, z125=0.6, val3=1.5):
    """[Lib] [Preset] Hidden door 1_Face SFX
    z124: OBJ instance ID of the bug key
    val2: Event light ID
    z125: Light fade time
    val3: Wait until face SFX playback
    """
    """State 0,1: [Reproduction] Hidden door 1_face SFX_SubState"""
    call = event_m20_24_x23(z124=z124, val2=val2)
    if call.Get() == 1:
        """State 3: [Condition] Hidden door 1_face SFX_SubState"""
        assert event_m20_24_x24(z124=z124)
        """State 2: [Execution] Hidden door 1_face SFX_SubState"""
        assert event_m20_24_x25(z124=z124, val2=val2, z125=z125, val3=val3)
    elif call.Get() == 0:
        pass
    """State 4: Finish"""
    return 0

def event_m20_24_x27(z119=_, z120=20, z121=_, z122=0, z123=2):
    """[Lib] [Preset] Switch Navimesh according to OBJ status
    z119: Object instance ID
    z120: OBJ state ID
    z121: Navimesh switching point ID
    z122: Additional attributes
    z123: Delete attribute
    """
    """State 0,1: [Lib] [Reproduction] Navi mesh switching according to OBJ state_SubState"""
    call = event_m20_24_x28(z119=z119, z120=z120, z121=z121, z123=z123, z122=z122)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [Conditions] Switching the navigation mesh according to the OBJ state_SubState"""
        assert event_m20_24_x29(z119=z119, z120=z120, z121=z121)
    """State 2: [Lib] [Execution] Navigation mesh switching according to OBJ state_SubState"""
    assert event_m20_24_x30(z119=z119, z120=z120, z121=z121, z122=z122, z123=z123)
    """State 4: End state"""
    return 0

def event_m20_24_x28(z119=_, z120=20, z121=_, z123=2, z122=0):
    """[Lib] [Reproduction] Navi mesh switching according to OBJ status
    z119: Target OBJ instance ID
    z120: Target OBJ state ID
    z121: Navimesh switching point ID
    z123: Additional attributes
    z122: Delete attribute
    """
    """State 0,1: OBJ status judgment"""
    if CompareObjStateId(z119, z120, 1):
        """State 2: Navimesh attribute change"""
        AddNavimeshAttribute(z121, z123)
        DeleteNavimeshAttribute(z121, z122)
        """State 4: Not running"""
        return 1
    else:
        """State 3: Already started"""
        return 0

def event_m20_24_x29(z119=_, z120=20, z121=_):
    """[Lib] [Condition] Switch to Navimesh according to OBJ status
    z119: Target OBJ instance ID
    z120: Target OBJ state ID
    z121: Navimesh switching point ID
    """
    """State 0,1: OBJ transition wait"""
    CompareObjState(0, z119, z120, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x30(z119=_, z120=20, z121=_, z122=0, z123=2):
    """[Lib] [Execution] Switch Navimesh according to OBJ status
    z119: Target OBJ instance ID
    z120: Target OBJ state ID
    z121: Navimesh switching point ID
    z122: Additional attributes
    z123: Delete attribute
    """
    """State 0,1: Navimesh attribute change"""
    AddNavimeshAttribute(z121, z122)
    DeleteNavimeshAttribute(z121, z123)
    """State 2: End state"""
    return 0

def event_m20_24_x31(z113=102030, z114=686, z115=104010, z116=60, z117=103510, z118=-1):
    """[Lib] NPC White Phantom Appearance: General-purpose: Body coexistence
    z113: White Phantom can appear: Global event flag
    z114: White Phantom: Generator ID
    z115: Death: Global event flag
    z116: Body: Generator group ID
    z117: Hostile: Global event flag
    z118: Body: Generator ID
    """
    """State 0,1: Appearance: Start"""
    DeleteNpcPhantom(z114)
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom sign Appearance: Judgment"""
        CompareEventFlag(0, z115, 1)
        CompareEventFlag(1, z117, 1)
        CompareEventFlag(2, z113, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 9: Appearance: Sign & Phantom: Not allowed"""
            Label('L0')
            DeleteNpcPhantom(z114)
            """State 10: Appearance: Hostile: Standby"""
            CompareEventFlag(0, z115, 1)
            CompareEventFlag(1, z117, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Appearance: System: Rerun"""
                Label('L1')
                RestartMachine()
                Quit()
        elif ConditionGroup(2):
            """State 3: Appearance: Phantom sign display: Permission"""
            GenerateNpcPhantom(z114)
            """State 8: Appearance: Phantom sign displayed: Waiting"""
            CompareEventFlag(0, z115, 1)
            CompareEventFlag(1, z117, 1)
            HasNpcPhantomSpawned(2, z114, 1)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                Goto('L0')
            elif ConditionGroup(2):
                """State 6: Appearance: Phantom is appearing: Waiting"""
                DeleteEnemyByGeneratorGroup(z116, 0)
                HasNpcPhantomSpawned(0, z114, 0)
                assert ConditionGroup(0)
                Goto('L1')
        """State 7: Appearance: Sign & Phantom: Stop generation"""
        DeleteNpcPhantom(z114)
    """State 4: Appearance: System: End"""
    EndMachine()

def event_m20_24_x32(z112=690):
    """[Lib] NPC White Phantom Appearance: Unconditional
    z112: Generator ID
    """
    """State 0,1: Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Appearance: Phantom appearance permission"""
        GenerateNpcPhantom(z112)
    """State 3: Appearance: System: End"""
    EndMachine()

def event_m20_24_x33():
    """[Lib] [Reproduction] Rebirth fire _ sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x34(z110=_, z111=_):
    """[Lib] [execute] Rebirth fire
    z110: Flag start ID
    z111: Flag end ID
    """
    """State 0,1: Flag reset"""
    SetEventFlagsInRange(z110, z111, 0)
    """State 2: End state"""
    return 0

def event_m20_24_x35():
    """[Lib] [Condition] Rebirth fire_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x36(z110=_, z111=_):
    """[Lib] [Preset] Rebirth
    z110: Flag start ID
    z111: Flag end ID
    """
    """State 0,1: [Lib] [Reproduction] Reproduction of fire_sky_SubState"""
    assert event_m20_24_x33()
    """State 3: [Lib] [Condition] Reproduction fire_Sky_SubState"""
    assert event_m20_24_x35()
    """State 2: [Lib] [Execution] Regenerative fire _SubState"""
    assert event_m20_24_x34(z110=z110, z111=z111)
    """State 4: End state"""
    return 0

def event_m20_24_x37():
    """[Lib] [Reproduction] Oil 壺 Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x38(z105=_):
    """[Lib] [Conditions]
    z105: Oil bottle OBJ instance ID
    """
    """State 0,1: Was the oil bottle broken?"""
    IsObjBroken(0, z105, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x39(z106=_, z107=_, z108=_, z109=1):
    """[Lib] [execution]
    z106: Tar OBJ instance ID for firewood
    z107: Hit group ID
    z108: Replacement GMID
    z109: Change destination GM slot
    """
    """State 0,1: Oil tar display: 30"""
    ChangeObjState(z106, 30)
    """State 2: Change of material"""
    SetGroundMaterial(z107, z108, z109)
    """State 3: End state"""
    return 0

def event_m20_24_x40(z105=_, z106=_, z107=_, z108=_, z109=1):
    """[Lib] [Preset] Oil bottle
    z105: Oil bottle OBJ instance ID
    z106: Tar OBJ instance ID for firewood
    z107: Hit group ID
    z108: Replacement GMID
    z109: Change destination GM slot
    """
    """State 0,1: [Lib] [Reproduction] Oil bottle_Sky_SubState"""
    assert event_m20_24_x37()
    """State 3: [Lib] [Conditions] Oil 壺 _SubState"""
    assert event_m20_24_x38(z105=z105)
    """State 2: [Lib] [Execution] Oil bottle_SubState"""
    assert event_m20_24_x39(z106=z106, z107=z107, z108=z108, z109=z109)
    """State 4: End state"""
    return 0

def event_m20_24_x41(z101=_, z102=_, z104=1):
    """[Lib] [Reproduction] Tar material change
    z101: Hit group ID
    z102: Replacement GMID
    z104: Change destination GM slot
    """
    """State 0,1: Material change_initialization"""
    SetGroundMaterial(z101, z102, z104)
    """State 2: End state"""
    return 0

def event_m20_24_x42(z100=_):
    """[Lib] [Condition] Tar material change
    z100: OBJ instance ID of tar
    """
    """State 0,1: Did tar burn out?"""
    CompareObjState(0, z100, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x43(z100=_, z101=_, z102=_, z103=0):
    """[Lib] [execution] Tar material change
    z100: OBJ instance ID of tar
    z101: Hit group ID
    z102: Replacement GMID
    z103: Change destination GM slot
    """
    """State 0,1: Change of material"""
    SetGroundMaterial(z101, z102, z103)
    """State 2: End state"""
    return 0

def event_m20_24_x44(z100=_, z101=_, z102=_, z103=0, z104=1):
    """[Lib] [Preset] Tar material change
    z100: OBJ instance ID of tar
    z101: Hit group ID
    z102: Replace_GMID
    z103: After change_GM slot
    z104: Before change_GM slot
    """
    """State 0,1: [Reproduction] Tar material change_SubState"""
    assert event_m20_24_x41(z101=z101, z102=z102, z104=z104)
    """State 3: [Condition] Tar material change_SubState"""
    assert event_m20_24_x42(z100=z100)
    """State 2: [Execution] Tar material change_SubState"""
    assert event_m20_24_x43(z100=z100, z101=z101, z102=z102, z103=z103)
    """State 4: End state"""
    return 0

def event_m20_24_x45(z96=10000000, z97=680, z98=0, z99=2):
    """[Lib] NPC Black Phantom Appearance: Online: Unconditional
    z96: Summon range
    z97: Generator ID
    z98: Appearance: Minimum time
    z99: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        IsPlayerInsidePoint(0, z96, z96, 1)
        assert ConditionGroup(0)
        """State 3: Black Phantom Appearance: Timer: Start"""
        CompareStateTime(0, z98, 3, z99)
        IsPlayerInsidePoint(1, z96, z96, 0)
        if ConditionGroup(0):
            """State 5: Black phantom appearance: Black phantom generation"""
            GenerateNpcPhantom(z97)
        elif ConditionGroup(1):
            """State 6: Black Phantom Appearance: System: Re-execution"""
            RestartMachine()
            Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m20_24_x46(z94=224000086, z95=11):
    """[Lib] [Preset] Get trophy
    z94: Acquisition trigger_other flags
    z95: Trophy type
    """
    """State 0,1: Have you acquired a trophy?"""
    if GetEventFlag(z94) != 0:
        pass
    else:
        """State 2: Wait for specified flag"""
        CompareEventFlag(0, z94, 1)
        assert ConditionGroup(0)
        """State 3: Trophy acquisition"""
        AwardTrophy(z95)
    """State 4: End state"""
    return 0

def event_m20_24_x47(z93=20243000):
    """[Lib] [BEST] [Reproduction] Phantom management of Andyel
    z93: Ander OBJ instance ID
    """
    """State 0,1: Are you a guest?"""
    if IsGuest() != 1:
        pass
    else:
        """State 2: Has the Andyir appeared?"""
        if CompareObjStateId(z93, 20, 0):
            pass
        else:
            """State 3: The guests"""
            return 0
    """State 4: Finish"""
    return 1

def event_m20_24_x48(z93=20243000):
    """[Lib] [BEST] [Condition] Phantom management of Andyel
    z93: Ander OBJ instance ID
    """
    """State 0,1: OBJ active judgment"""
    IsObjActive(0, z93, 1)
    CompareObjState(1, z93, 20, 0)
    if ConditionGroup(1):
        """State 3: Finish"""
        return 1
    elif ConditionGroup(0):
        """State 2: Illusion"""
        return 0

def event_m20_24_x49(z93=20243000):
    """[Lib] [BEST] [Execution] Phantom management of Andyel
    z93: Ander OBJ instance ID
    """
    """State 0,2: Phantom processing"""
    SetObjPhantomParameters(z93, 15)
    """State 1: Next judgment"""
    IsObjActive(0, z93, 0)
    CompareObjState(0, z93, 20, 0)
    assert ConditionGroup(0)
    """State 3: Illusion"""
    return 0

def event_m20_24_x50(z93=20243000):
    """[Lib] [BEST] [Preset] Phantom management of Andyel
    z93: Ander OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Phantom management of Andy _SubState"""
    call = event_m20_24_x47(z93=z93)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [BEST] [Condition] Phantom management of Andy_SubState"""
        call = event_m20_24_x48(z93=z93)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 2: [Lib] [BEST] [Execution] Phantom management of Andy_SubState"""
            assert event_m20_24_x49(z93=z93)
            """State 5: Rerun"""
            return 1
    """State 4: Finish"""
    return 0

def event_m20_24_x51(z91=20243000, z92=20240651):
    """[Lib] [BEST] [Reproduction] SFX management of bonfire
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z91, 20, 0):
        """State 2: Turn on SFX"""
        DisableObjSfx(z92, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m20_24_x52(z91=20243000):
    """[Lib] [BEST] [Condition] SFX management of bonfire
    z91: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z91, 10, 0)
    CompareObjState(0, z91, 31, 0)
    CompareObjState(0, z91, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on SFX"""
        return 1
    else:
        """State 2: SFX off"""
        return 0

def event_m20_24_x53(z91=20243000, z92=20240651):
    """[Lib] [BEST] [Execution] Bonfire SFX Management_ON
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,2: Enable SFX"""
    DisableObjSfx(z92, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z91, 10, 1)
    CompareObjState(8, z91, 31, 1)
    CompareObjState(8, z91, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m20_24_x54(z91=20243000, z92=20240651):
    """[Lib] [BEST] [execution] Bonfire SFX management_OFF
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,2: Disable SFX"""
    DisableObjSfx(z92, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z91, 10, 0)
    CompareObjState(0, z91, 31, 0)
    CompareObjState(0, z91, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m20_24_x55(z91=20243000, z92=20240651):
    """[Lib] [BEST] [Preset] Bonfire SFX Management
    z91: Ander OBJ instance ID
    z92: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire SFX Management_SubState"""
    call = event_m20_24_x51(z91=z91, z92=z92)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 5: Finish"""
    return 0
    """State 4: [Lib] [BEST] [Conditions] Bonfire SFX Management_SubState"""
    Label('L0')
    call = event_m20_24_x52(z91=z91)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execute] Bonfire SFX Management_ON_SubState"""
        assert event_m20_24_x53(z91=z91, z92=z92)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] SFX management of bonfire _OFF_SubState"""
        assert event_m20_24_x54(z91=z91, z92=z92)
    """State 6: Rerun"""
    return 1

def event_m20_24_x56(z89=20243000, z90=20240651):
    """[Lib] [BEST] [Reproduction] Bonfire Key Guide Management
    z89: Ander OBJ instance ID
    z90: Bonfire OBJ instance ID
    """
    """State 0,1: Has the Andyir appeared?"""
    if CompareObjStateId(z89, 20, 0):
        """State 2: Activate key guide for bonfire"""
        DisableObjKeyGuide(z90, 0)
        """State 4: Finish"""
        return 1
    else:
        """State 3: Incomplete"""
        return 0

def event_m20_24_x57(z89=20243000):
    """[Lib] [BEST] [Conditions] Key guide management for bonfire
    z89: Ander OBJ instance ID
    """
    """State 0,1: Determining the status of the deal"""
    CompareObjState(0, z89, 10, 0)
    CompareObjState(0, z89, 20, 0)
    if ConditionGroup(0):
        """State 3: Turn on key guide"""
        return 1
    else:
        """State 2: OFF key guide"""
        return 0

def event_m20_24_x58(z89=20243000, z90=20240651):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_ON
    z89: Ander OBJ instance ID
    z90: Bonfire OBJ instance ID
    """
    """State 0,2: Activate key guide for bonfire"""
    DisableObjKeyGuide(z90, 0)
    """State 1: Next judgment"""
    CompareObjState(8, z89, 10, 1)
    CompareObjState(8, z89, 20, 1)
    assert ConditionGroup(8)
    """State 3: Rerun"""
    return 0

def event_m20_24_x59(z89=20243000, z90=20240651):
    """[Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF
    z89: Ander OBJ instance ID
    z90: Bonfire OBJ instance ID
    """
    """State 0,2: Disabling bonfire key guide"""
    DisableObjKeyGuide(z90, 1)
    """State 1: Next judgment"""
    CompareObjState(0, z89, 10, 0)
    CompareObjState(0, z89, 20, 0)
    assert ConditionGroup(0)
    """State 3: Rerun"""
    return 0

def event_m20_24_x60(z89=20243000, z90=20240651):
    """[Lib] [BEST] [Preset] Bonfire Key Guide Management
    z89: Ander OBJ instance ID
    z90: Bonfire OBJ instance ID
    """
    """State 0,1: [Lib] [BEST] [Reproduction] Bonfire Key Guide Management_SubState"""
    call = event_m20_24_x56(z89=z89, z90=z90)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 6: Finish"""
    return 1
    """State 4: [Lib] [BEST] [Condition] Key guide management of bonfire _SubState"""
    Label('L0')
    call = event_m20_24_x57(z89=z89)
    if call.Get() == 1:
        """State 3: [Lib] [BEST] [Execution] Bonfire Key Guide Management_ON_SubState"""
        assert event_m20_24_x58(z89=z89, z90=z90)
    elif call.Get() == 0:
        """State 2: [Lib] [BEST] [Execution] Bonfire Key Guide Management_OFF_SubState"""
        assert event_m20_24_x59(z89=z89, z90=z90)
    """State 5: Rerun"""
    return 0

def event_m20_24_x61(z83=20243000, z84=100745, z86=100764, z85=100746, z87=100740, z88=20240651):
    """[Lib] [BEST] [Reproduction] Andyel_Appearance Judgment_2
    z83: Ander OBJ instance ID
    z84: Event completion flag
    z86: Conversation start flag
    z85: Encounter flag
    z87: Last encounter determination flag
    z88: Bonfire OBJ instance ID
    """
    """State 0,1: Has the event been completed?"""
    if GetEventFlag(z84) != 0:
        pass
    else:
        Goto('L0')
    """State 7: Finish"""
    return 0
    """State 2: Was it in conversation?"""
    Label('L0')
    if GetEventFlag(z86) != 0:
        pass
    else:
        """State 3: Was it in the middle of appearance?"""
        if CompareObjStateId(z83, 72, 0):
            """State 4: Wait for completion"""
            Label('L1')
            assert CompareObjStateId(z83, 30, 0)
            """State 5: Conversation start flag ON"""
            SetEventFlag(z86, 1)
        elif CompareObjStateId(z83, 73, 0):
            Goto('L1')
        elif CompareObjStateId(z83, 70, 0):
            Goto('L1')
        elif CompareObjStateId(z83, 30, 0):
            Goto('L1')
        else:
            """State 6: Is it in game?"""
            assert InGame() != 0
            """State 9: Appearance determination"""
            return 2
    """State 8: Disappearance judgment"""
    return 1

def event_m20_24_x62(z87=100740, z88=20240651):
    """[Lib] [BEST] [Conditions] Andyel_Appearance determination_2
    z87: Last encounter determination flag
    z88: Bonfire OBJ instance ID
    """
    """State 0,1: Andel appearance determination"""
    CompareEventFlag(8, z87, 1)
    IsObjActive(8, z88, 1)
    CompareEventFlag(9, z87, 1)
    IsObjActive(9, z88, 1)
    CompareObjState(9, z88, 30, 0)
    if ConditionGroup(9):
        """State 3: Ignited"""
        return 1
    elif ConditionGroup(8):
        """State 2: Waiting for ignition"""
        return 0

def event_m20_24_x63(z83=20243000):
    """[Lib] [BEST] [Execution] Andyel_Appearance determination_2
    z83: Ander OBJ instance ID
    """
    """State 0,1: Andy key guide activation: 31"""
    ChangeObjState(z83, 31)
    """State 2: End state"""
    return 0

def event_m20_24_x64():
    """[Lib] [BEST] [Reproduction] Andiel_Appearance_2"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x65(z83=20243000):
    """[Lib] [BEST] [Condition] Andyel_Appearance_2
    z83: Ander OBJ instance ID
    """
    """State 0,1: Judgment to examine the deal"""
    IsObjSearched(0, z83)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x66(z83=20243000, z86=100764, z85=100746):
    """[Lib] [BEST] [Execution] Andyel_Appearance_2
    z83: Ander OBJ instance ID
    z86: Conversation start flag
    z85: Encounter flag
    """
    """State 0,7: Host?"""
    if IsGuest() != 1:
        """State 4: Bonfire light action"""
        PlayerActionRequest(5)
        assert PlayerIsInEventAction(5) != 0
    else:
        pass
    """State 5: Wait for action to finish"""
    CompareStateTime(8, 1.5, 2, 1.5)
    IsHost(8, 1, 0)
    IsPlayerPlayingMotion(9, 5, 0)
    IsHost(9, 1, 0)
    if ConditionGroup(9):
        """State 9: Rerun"""
        return 1
    elif ConditionGroup(8):
        """State 6: Andel encounter flag ON"""
        SetEventFlag(z85, 1)
        """State 1: Andyir Appearance: 72"""
        ChangeObjState(z83, 72)
        """State 2: Waiting for Andyur to appear"""
        CompareObjState(0, z83, 30, 0)
        assert ConditionGroup(0)
        """State 3: Conversation start flag ON"""
        SetEventFlag(z86, 1)
        """State 8: End state"""
        return 0

def event_m20_24_x67():
    """[Lib] [BEST] [Reproduction] Anderel_Deletion Judgment_2"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x68(z84=100745):
    """[Lib] [BEST] [Conditions] Anderel_Deletion Judgment_2 or later
    z84: Event completion flag
    """
    """State 0,1: Completion flag judgment"""
    CompareEventFlag(0, z84, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x69(z83=20243000):
    """[Lib] [BEST] [Execution] Andel_Deletion Judgment_2 or later
    z83: Ander OBJ instance ID
    """
    """State 0,1: Andyel disappearance: 71"""
    ChangeObjState(z83, 71)
    """State 2: Waiting for Andyel disappearance"""
    CompareObjState(0, z83, 20, 0)
    assert ConditionGroup(0)
    """State 3: End state"""
    return 0

def event_m20_24_x70(z83=20243000, z84=100745, z85=100746, z86=100764, z87=100740, z88=20240651):
    """[Lib] [BEST] [Preset] Andyel_2 or later
    z83: Ander OBJ instance ID
    z84: Event completion flag
    z85: Encounter flag
    z86: Conversation start flag
    z87: Last encounter determination flag
    z88: Bonfire OBJ instance ID
    """
    """State 0,2: [Lib] [BEST] [Reproduction] Andiel_Appearance determination_2 and subsequent times_SubState"""
    call = event_m20_24_x61(z83=z83, z84=z84, z86=z86, z85=z85, z87=z87, z88=z88)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [BEST] [Reproduction] Ander _ annihilation determination _ 2nd and later _SubState"""
        Label('L0')
        assert event_m20_24_x67()
        """State 9: [Lib] [BEST] [Condition] Ander _ annihilation judgment _ 2nd and later _SubState"""
        assert event_m20_24_x68(z84=z84)
        """State 6: [Lib] [BEST] [Execution] Ander _ disappearance determination _ 2nd and later _SubState"""
        assert event_m20_24_x69(z83=z83)
    elif call.Get() == 2:
        """State 8: [Lib] [BEST] [Condition] Andyel_Appearance determination_2 and subsequent times_SubState"""
        call = event_m20_24_x62(z87=z87, z88=z88)
        if call.Get() == 1:
            """State 10: [Lib] [BEST] [Execution] Andel _ Appearance determination _ 2nd or later _ Ignition completed _SubState"""
            assert event_m20_24_x71(z83=z83, z86=z86)
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] [BEST] [Execution] Anderl_Appearance determination_2 and subsequent times_SubState"""
            assert event_m20_24_x63(z83=z83)
            """State 1: [Lib] [BEST] [Reproduction] Andiel _ Appearance _ 2nd and later _SubState"""
            assert event_m20_24_x64()
            """State 7: [Lib] [BEST] [Conditions] Andyel_Appearance_2 and later _SubState"""
            assert event_m20_24_x65(z83=z83)
            """State 4: [Lib] [BEST] [Execution] Andyel_Appearance_2 and subsequent times_SubState"""
            call = event_m20_24_x66(z83=z83, z86=z86, z85=z85)
            if call.Get() == 1:
                """State 12: Rerun"""
                return 1
            elif call.Get() == 0:
                Goto('L0')
    """State 11: Finish"""
    return 0

def event_m20_24_x71(z83=20243000, z86=100764):
    """[Lib] [BEST] [Execution] Andiel _ Appearance determination _ 2nd and later _ Ignited
    z83: Ander OBJ instance ID
    z86: Conversation start flag
    """
    """State 0,1: Andyle waiting state: 30"""
    ChangeObjState(z83, 30)
    """State 3: Waiting for waiting"""
    CompareObjState(0, z83, 30, 0)
    assert ConditionGroup(0)
    """State 2: Host?"""
    if IsGuest() != 1:
        """State 4: Conversation start flag ON"""
        SetEventFlag(z86, 1)
    else:
        pass
    """State 5: Guest waiting"""
    SetConditionGroupTrue(0)
    assert HostConditionGroup(0)
    """State 6: End state"""
    return 0

def event_m20_24_x72(z78=10000000, z79=680, z80=104320, z81=0, z82=2):
    """[Lib] [BEST] NPC Black Phantom Appearance: Online: Miracle Person _ When Living
    z78: Summon range
    z79: Generator ID
    z80: Death: Global event flag
    z81: Appearance: Minimum time
    z82: Appearance: Maximum time
    """
    """State 0,7: [DC] Is it in game?"""
    assert InGame() != 0
    """State 1: Black Phantom Appearance: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 2: Black Phantom Appearance: Summoning Conditions: Standby"""
        CompareEventFlag(0, z80, 1)
        IsPlayerInsidePoint(1, z78, z78, 1)
        if ConditionGroup(0):
            pass
        elif ConditionGroup(1):
            """State 3: Black Phantom Appearance: Timer: Start"""
            CompareEventFlag(0, z80, 1)
            CompareStateTime(1, z81, 3, z82)
            IsPlayerInsidePoint(2, z78, z78, 0)
            if ConditionGroup(0):
                pass
            elif ConditionGroup(1):
                """State 5: Black phantom appearance: Black phantom generation"""
                GenerateNpcPhantom(z79)
                HasNpcPhantomSpawned(0, z79, 1)
                assert ConditionGroup(0)
            elif ConditionGroup(2):
                """State 6: Black Phantom Appearance: System: Re-execution"""
                RestartMachine()
                Quit()
    """State 4: Black Phantom Appearance: System: End"""
    EndMachine()

def event_m20_24_x73(z61=224020004, z63=224000005):
    """[Lib] [DC] [Reproduction] Wanderer _ random lottery
    z61: Lottery determination flag
    z63: Defeat flag
    """
    """State 0,4: Is it in game?"""
    assert InGame() != 0
    """State 2: Host?"""
    if IsGuest() != 1:
        pass
    else:
        Goto('L1')
    """State 3: Already destroyed?"""
    if GetEventFlag(z63) != 0:
        pass
    else:
        Goto('L0')
    """State 8: Defeated"""
    return 3
    """State 1: Have you already drawn?"""
    Label('L0')
    if GetEventFlag(z61) != 0:
        """State 6: Lottery completed"""
        return 1
    else:
        """State 5: Not drawn"""
        return 0
    """State 7: Guest: Exit"""
    Label('L1')
    return 2

def event_m20_24_x74(z62=14):
    """[Lib] [DC] [Condition] Wanderer_Random lottery
    z62: Random number comparison value
    """
    """State 0,1: Random number generation"""
    GenerateRandomNumber(0, 0, 99)
    """State 2: Random number judgment [[DEBUG]] flag 109990 ON can be reliably attached"""
    CompareEventRandValue(0, 0, z62, 5)
    CompareEventFlag(0, 109990, 1)
    if ConditionGroup(0):
        """State 3: Atari: Can be generated"""
        return 0
    else:
        """State 4: Lost: Cannot be generated"""
        return 1

def event_m20_24_x75(z61=224020004, z64=2, z65=10):
    """[Lib] [DC] [execution] wanderer_random lottery_atari
    z61: Lottery determination flag
    z64: Number of appearance judgment points
    z65: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z61, 1)
    """State 2: Appearance judging point lottery: random number generation"""
    GenerateRandomNumber(1, 1, z64)
    """State 3: Lottery result point variable: random number substitution"""
    SetAreaVariable(z65, GetRandomValue(1))
    """State 4: End state"""
    return 0

def event_m20_24_x76(z61=224020004, z62=14, z63=224000005, z64=2, z65=10):
    """[Lib] [DC] [Preset] Wanderer_Random lottery
    z61: Lottery determination flag
    z62: Random number comparison value
    z63: Defeat flag
    z64: Number of appearance judgment points
    z65: Lottery result point variable
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Random Drawing_SubState"""
    call = event_m20_24_x73(z61=z61, z63=z63)
    if call.Get() == 3:
        """State 5: Defeated: Finished"""
        return 0
    elif call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Random lottery_SubState"""
        call = event_m20_24_x74(z62=z62)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [Execution] Wanderer_Random lottery_Atari_SubState"""
            assert event_m20_24_x75(z61=z61, z64=z64, z65=z65)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Random Lottery_Loose_SubState"""
            assert event_m20_24_x89(z61=z61, z65=z65)
    elif call.Get() == 2:
        """State 7: Guest: Exit"""
        return 2
    """State 6: End of lottery"""
    return 1

def event_m20_24_x77(val1=_, z75=10):
    """[Lib] [DC] [Reproduction] Wanderer_Generation
    val1: Appearance judgment number
    z75: Lottery result point variable
    """
    """State 0,3: Is it in game?"""
    assert InGame() != 0
    """State 1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Is the appearance judgment point here?"""
        if (GetAreaVariable(z75) == val1) != 1:
            pass
        else:
            """State 5: Waiting for generation"""
            return 1
    """State 4: Finish"""
    return 0

def event_m20_24_x78(z71=_, z72=0, z73=5):
    """[Lib] [DC] [Condition] Wanderer_Generation
    z71: Appearance judgment point ID
    z72: Minimum appearance time
    z73: Maximum time to appear
    """
    """State 0,1: Point judgment"""
    IsPlayerInsidePoint(0, z71, z71, 1)
    assert ConditionGroup(0)
    """State 2: Random weight"""
    CompareStateTime(0, z72, 3, z73)
    assert ConditionGroup(0)
    """State 3: Generation"""
    return 0

def event_m20_24_x79(z74=971, z76=_, z77=_):
    """[Lib] [DC] [Execution] Wanderer_Generation
    z74: Generator ID
    z76: Appearance start point ID
    z77: Appearance end point ID
    """
    """State 0,3: Randomly overwrite the initial position"""
    OverrideGeneratorStartPositionRandom(z74, z76, z77)
    assert (GetStateTime() > 0.1) != 0
    """State 1: Wanderer: Generation"""
    GenerateNpcPhantom(z74)
    """State 4: Finish"""
    return 0

def event_m20_24_x80(z68=224000005):
    """[Lib] [DC] [Reproduction] Wanderer_Destroy
    z68: Defeat flag
    """
    """State 0,2: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 1: Already destroyed?"""
        if GetEventFlag(z68) != 0:
            pass
        else:
            """State 3: Not defeated"""
            return 0
    """State 4: Defeated"""
    return 1

def event_m20_24_x81(z71=_, z72=0, z73=5, z74=971, val1=_, z75=10, z76=_, z77=_):
    """[Lib] [DC] [Preset] Wanderer_Generation
    z71: Intrusion detection point ID
    z72: Minimum appearance time
    z73: Maximum time to appear
    z74: Generator ID
    val1: Appearance judgment number
    z75: Lottery result point variable
    z76: Appearance start point ID
    z77: Appearance end point ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Generation_SubState"""
    call = event_m20_24_x77(val1=val1, z75=z75)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 3: [Lib] [DC] [Condition] Wanderer_Generation_SubState"""
        assert event_m20_24_x78(z71=z71, z72=z72, z73=z73)
        """State 2: [Lib] [DC] [Execution] Wanderer_Generation_SubState"""
        assert event_m20_24_x79(z74=z74, z76=z76, z77=z77)
    """State 4: Finish"""
    return 0

def event_m20_24_x82(z69=971, mode1=1):
    """[Lib] [DC] [Condition] Wanderer_Destroy
    z69: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z69)
    assert ConditionGroup(0)
    """State 2: Wanderer equipment check"""
    if (not mode1) != 0:
        """State 3: Large sword"""
        return 0
    else:
        """State 4: Kama"""
        return 1

def event_m20_24_x83(z68=224000005, z70=_):
    """[Lib] [DC] [Execution] Wanderer_Destroy
    z68: Defeat flag
    z70: Weapon flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z68, 1)
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
                    SetEventFlag(z70, 1)
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

def event_m20_24_x84(z68=224000005, z69=971, mode1=1):
    """[Lib] [DC] [Preset] Wanderer_Destroy
    z68: Defeat flag
    z69: Generator ID
    mode1: Wanderer equipment
    """
    """State 0,1: [Lib] [DC] [Reproduction] Wanderer_Destroy_SubState"""
    call = event_m20_24_x80(z68=z68)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] Wanderer_Destroy_SubState"""
        call = event_m20_24_x82(z69=z69, mode1=mode1)
        if call.Get() == 0:
            """State 2: [Lib] [DC] [execution] wanderer_defeat determination_sword ver_SubState"""
            assert event_m20_24_x83(z68=z68, z70=102754)
        elif call.Get() == 1:
            """State 4: [Lib] [DC] [Execution] Wanderer_Destroy_Kama ver_SubState"""
            assert event_m20_24_x83(z68=z68, z70=102755)
    """State 5: End state"""
    return 0

def event_m20_24_x85(z66=_, z67=96960000):
    """[Lib] [DC] [Execute] Transparent characters
    z66: Generator ID
    z67: Parameter ID
    """
    """State 0,1: Cancel special effects"""
    ClearEnemySpEffect(z66, z67)
    """State 2: End state"""
    return 0

def event_m20_24_x86(z66=_, z67=96960000):
    """[Lib] [DC] [Reproduction] Transparent characters
    z66: Generator ID
    z67: Parameter ID
    """
    """State 0,1: Special effects: draw only shadows"""
    SetEnemySpEffect(z66, z67, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_24_x87(z66=_):
    """[Lib] [DC] [Condition] Transparent characters
    z66: Generator ID
    """
    """State 0,1: Defeat determination"""
    IsChrDead(0, z66)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x88(z66=_, z67=96960000):
    """[Lib] [DC] [Preset] Transparent characters
    z66: Generator ID
    z67: Parameter ID
    """
    """State 0,1: [Lib] [DC] [Reproduction] Transparent character _SubState"""
    assert event_m20_24_x86(z66=z66, z67=z67)
    """State 3: [Lib] [DC] [Condition] Transparent character _SubState"""
    assert event_m20_24_x87(z66=z66)
    """State 2: [Lib] [DC] [Execution] Transparent character _SubState"""
    assert event_m20_24_x85(z66=z66, z67=z67)
    """State 4: End state"""
    return 0

def event_m20_24_x89(z61=224020004, z65=10):
    """[Lib] [DC] [Execution] Wanderer_Random lottery_Loose
    z61: Lottery determination flag
    z65: Lottery result point variable
    """
    """State 0,1: Lottery determination flag ON"""
    SetEventFlag(z61, 1)
    """State 2: Lottery result point variable: Substitute 0"""
    SetAreaVariable(z65, 0)
    """State 3: End state"""
    return 0

def event_m20_24_x90(z58=224000081):
    """[Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management
    z58: Defeat flag
    """
    """State 0,1: Has the boss been destroyed?"""
    if GetEventFlag(z58) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_24_x91(z59=800):
    """[Lib] [DC] [Condition] NPC White Spirit_Gesture Management
    z59: Boss generator ID
    """
    """State 0,1: Has the boss's HP dropped below 0?"""
    CompareChrHpValue(0, z59, 0, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x92(z60=224020083):
    """[Lib] [DC] [execution] NPC white spirit _ gesture management
    z60: Gesture flag
    """
    """State 0,1: Gesture flag ON"""
    SetEventFlag(z60, 1)
    """State 2: End state"""
    return 0

def event_m20_24_x93(z58=224000081, z59=800, z60=224020083):
    """[Lib] [DC] [Preset] NPC White Spirit_Gesture Management
    z58: Boss destruction flag
    z59: Boss generator ID
    z60: Gesture flag
    """
    """State 0,1: [Lib] [DC] [Reproduction] NPC White Spirit_Gesture Management_SubState"""
    call = event_m20_24_x90(z58=z58)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Lib] [DC] [Condition] NPC White Spirit_Gesture Management_SubState"""
        assert event_m20_24_x91(z59=z59)
        """State 2: [Lib] [DC] [Execution] NPC White Spirit_Gesture Management_SubState"""
        assert event_m20_24_x92(z60=z60)
    """State 4: End state"""
    return 0

def event_m20_24_x94(z18=224000050):
    """[Reproduction] Reproduction of the state of a huge candlestick
    z18: All lighting complete flag
    """
    """State 0,12: Is it all lit?"""
    if GetEventFlag(z18) != 0:
        pass
    else:
        """State 13: Host?"""
        if IsGuest() != 0:
            """State 26: The guests"""
            return 12
        else:
            """State 1: Judgment status of candlestick 1"""
            if CompareObjStateId(20242050, 10, 1):
                """State 2: State determination of candlestick 2"""
                if CompareObjStateId(20242000, 10, 1):
                    """State 3: State determination of candlestick 3"""
                    if CompareObjStateId(20242030, 10, 1):
                        """State 4: State determination of candlestick 4"""
                        if CompareObjStateId(20242035, 10, 1):
                            """State 5: State determination of candlestick 5"""
                            if CompareObjStateId(20242040, 10, 1):
                                """State 6: State determination of candlestick 6"""
                                if CompareObjStateId(20242025, 10, 1):
                                    """State 7: State determination of candlestick 7"""
                                    if CompareObjStateId(20242045, 10, 1):
                                        """State 8: State determination of candlestick 8"""
                                        if CompareObjStateId(20242055, 10, 1):
                                            """State 9: State determination of candlestick 9"""
                                            if CompareObjStateId(20242060, 10, 1):
                                                """State 10: State determination of candlestick 10"""
                                                if CompareObjStateId(20242010, 10, 1):
                                                    """State 11: State determination of candlestick 11"""
                                                    if CompareObjStateId(20242005, 10, 1):
                                                        pass
                                                    else:
                                                        """State 24: From candlestick 11"""
                                                        return 10
                                                else:
                                                    """State 23: From candlestick 10"""
                                                    return 9
                                            else:
                                                """State 22: From candlestick 9"""
                                                return 8
                                        else:
                                            """State 21: From candlestick 8"""
                                            return 7
                                    else:
                                        """State 20: From candlestick 7"""
                                        return 6
                                else:
                                    """State 19: From candlestick 6"""
                                    return 5
                            else:
                                """State 18: From candlestick 5"""
                                return 4
                        else:
                            """State 17: From candlestick 4"""
                            return 3
                    else:
                        """State 16: From candlestick 3"""
                        return 2
                else:
                    """State 15: From candlestick 2"""
                    return 1
            else:
                """State 14: Unlit"""
                return 0
    """State 25: Finish"""
    return 11

def event_m20_24_x95(z16=20240700):
    """[Conditions] Judgment state determination for a huge candlestick
    z16: Igniter instance ID
    """
    """State 0,1: Was it ignited?"""
    CompareObjState(0, z16, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x96(z56=20241010, z57=200000):
    """[Reproduction] Shortcut drawbridge
    z56: Drawbridge OBJ instance ID
    z57: Navigation change point ID
    """
    """State 0,1: Check the state of the drawbridge"""
    if CompareObjStateId(z56, 10, 0):
        """State 3: Not started"""
        return 0
    else:
        """State 2: Navimesh attribute deletion"""
        DeleteNavimeshAttribute(z57, 2)
        """State 4: Activated"""
        return 1

def event_m20_24_x97(z55=20241000):
    """[Condition] Shortcut drawbridge
    z55: Lever OBJ instance ID
    """
    """State 0,1: Lever operation standby"""
    CompareObjState(0, z55, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x98(z54=200000):
    """[Run] Shortcut drawbridge
    z54: Navigation change point ID
    """
    """State 0,1: Drawbridge animation playback"""
    ChangeOwnObjState(70)
    assert CompareOwnObjStateId(20, 0)
    """State 2: Navimesh attribute deletion"""
    DeleteNavimeshAttribute(z54, 2)
    """State 3: End state"""
    return 0

def event_m20_24_x99():
    """[Preset] King whose defense power fluctuates according to the number of possessed items"""
    """State 0,1: [Reproduction] King_SubState whose defense power fluctuates depending on the number of possessed items"""
    call = event_m20_24_x100()
    if call.Get() == 1:
        pass
    elif call.Done():
        Goto('L0')
    """State 10: Guest ends immediately"""
    return 1
    """State 2: [Condition] King_SubState whose defense power varies with the number of possessed items"""
    Label('L0')
    call = event_m20_24_x101()
    if call.Get() == 0:
        """State 3: [Execution] King whose defense power varies depending on the number of possessed items_Number of possessions: 0_SubState"""
        assert event_m20_24_x102(z53=95146010)
    elif call.Get() == 1:
        """State 4: [Execution] King whose defense power varies depending on the number of possessed items_Number of possessions: 1_SubState"""
        assert event_m20_24_x102(z53=95146020)
    elif call.Get() == 2:
        """State 5: [Execution] King whose defense power varies depending on the number of possessed items_Number of possessions: 2_SubState"""
        assert event_m20_24_x102(z53=95146030)
    elif call.Get() == 3:
        """State 6: [Execution] King whose defense power varies depending on the number of possessed items_Number of possessions: 3_SubState"""
        assert event_m20_24_x102(z53=95146040)
    elif call.Get() == 4:
        """State 7: [Execution] King whose defense power varies depending on the number of possessed items_Number of possessions: 4_SubState"""
        assert event_m20_24_x102(z53=95146050)
    elif call.Get() == 5:
        """State 8: [Execution] King whose defense power varies depending on the number of possessed items_Number of possessions: 5 to _SubState"""
        assert event_m20_24_x102(z53=95146060)
    """State 9: End state"""
    return 0

def event_m20_24_x100():
    """[Reproduction] King whose defense power fluctuates depending on the number of possessed items"""
    """State 0,1: Guest judgment"""
    if IsGuest() != 0:
        """State 3: The guests"""
        return 1
    else:
        """State 2: host"""
        return 0

def event_m20_24_x101():
    """[Conditions] King whose defense power varies depending on the number of possessed items"""
    """State 0,1: Giant Soul Counting"""
    # goods:50920000:Soul of a Giant
    DoesPlayerHaveItem(0, 50920000, 0, 0, 1, 1, 1)
    # goods:50920000:Soul of a Giant
    DoesPlayerHaveItem(1, 50920000, 1, 0, 1, 1, 1)
    # goods:50920000:Soul of a Giant
    DoesPlayerHaveItem(2, 50920000, 2, 0, 1, 1, 1)
    # goods:50920000:Soul of a Giant
    DoesPlayerHaveItem(3, 50920000, 3, 0, 1, 1, 1)
    # goods:50920000:Soul of a Giant
    DoesPlayerHaveItem(4, 50920000, 4, 0, 1, 1, 1)
    # goods:50920000:Soul of a Giant
    DoesPlayerHaveItem(5, 50920000, 5, 3, 1, 1, 1)
    if ConditionGroup(0):
        """State 2: Number of possessions: 0"""
        return 0
    elif ConditionGroup(1):
        """State 3: Number of possessions: 1"""
        return 1
    elif ConditionGroup(2):
        """State 4: Number of possessions: 2"""
        return 2
    elif ConditionGroup(3):
        """State 5: Number of possessions: 3"""
        return 3
    elif ConditionGroup(4):
        """State 6: Number of possessions: 4"""
        return 4
    elif ConditionGroup(5):
        """State 7: Number of possessions: 5"""
        return 5

def event_m20_24_x102(z53=_):
    """[Execution] King whose defense power fluctuates according to the number of possessed items
    z53: ID of special effect to be granted
    """
    """State 0,1: Giving special effects to an old king"""
    SetEnemySpEffect(230, z53, 19, 4)
    """State 2: End state"""
    return 0

def event_m20_24_x103(z48=224000086):
    """[Reproduction] Boss battle with the king
    z48: King defeat flag
    """
    """State 0,1: Are you destroying the king?"""
    if GetEventFlag(z48) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_24_x104(z49=802000):
    """[Condition] Boss Battle with King_Start Judgment
    z49: Start judgment point ID
    """
    """State 0,1: Did you attack the king within the points?"""
    CompareChrHpRatio(8, 230, 100, 4)
    IsPlayerInsidePoint(8, z49, 802000, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_24_x105(z51=2024010, z52=224020085):
    """[Execution] Boss battle with the King_Start
    z51: Boss Battle ID
    z52: Logic flag
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z51)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z52, 1)
    """State 3: End state"""
    return 0

def event_m20_24_x106(z50=802001, z51=2024010):
    """[Condition] Boss Battle with King_End Judgment
    z50: End judgment point ID
    z51: Boss Battle ID
    """
    """State 0,1: Did you defeat or kill from the end point?"""
    IsPlayerInsidePoint(0, z50, z50, 0)
    IsEventBossKill(1, z51, 0, 1)
    if ConditionGroup(1):
        """State 3: End of boss destruction"""
        return 1
    elif ConditionGroup(0):
        """State 2: Cancel boss battle"""
        return 0

def event_m20_24_x107(z51=2024010):
    """[Execution] Boss Battle with King_Cancel
    z51: Boss Battle ID
    """
    """State 0,1: Boss battle cancellation notice"""
    CancelBossFight(z51)
    """State 2: Rerun"""
    return 0

def event_m20_24_x108(z48=224000086, z49=802000, z50=802001, z51=2024010, z52=224020085):
    """[Preset] Boss battle with the king
    z48: King defeat flag
    z49: Start judgment point ID
    z50: End judgment point ID
    z51: Boss Battle ID
    z52: Logic flag
    """
    """State 0,1: [Reproduction] Boss Battle with the King_SubState"""
    call = event_m20_24_x103(z48=z48)
    if call.Get() == 0:
        """State 6: [Condition] Boss battle with the king_Start judgment_SubState"""
        assert event_m20_24_x104(z49=z49)
        """State 4: [Execution] Boss Battle with King_Start_SubState"""
        assert event_m20_24_x105(z51=z51, z52=z52)
        """State 2: [Reproduction] Boss Battle with King_Sky_SubState"""
        assert event_m20_24_x109()
        """State 7: [Condition] Boss Battle with King_End Judgment_SubState"""
        call = event_m20_24_x106(z50=z50, z51=z51)
        if call.Get() == 0:
            """State 3: [Execution] Boss Battle with King_Cancel_SubState"""
            assert event_m20_24_x107(z51=z51)
            """State 9: Rerun"""
            return 1
        elif call.Get() == 1:
            """State 5: [Execution] Boss Battle with King_End_SubState"""
            assert event_m20_24_x110(z51=z51, z52=z52)
    elif call.Get() == 1:
        pass
    """State 8: Finish"""
    return 0

def event_m20_24_x109():
    """[Reproduction] Boss battle with the king _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x110(z51=2024010, z52=224020085):
    """[Execution] Boss Battle with King_End
    z51: Boss Battle ID
    z52: Logic flag
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z52, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z51)
    """State 3: End state"""
    return 0

def event_m20_24_x111():
    """[Reproduction] Get the king's ring_sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x112(z47=20246500):
    """[Condition] Get the king's ring
    z47: King Ring OBJ Instance ID
    """
    """State 0,1: Got the king's ring?"""
    WasObjItemAcquired(0, z47, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x113(z46=100804):
    """[Execution] Get the king's ring
    z46: Ring acquisition global event flag
    """
    """State 0,1: Acquisition flag ON"""
    SetEventFlag(z46, 1)
    """State 2: End state"""
    return 0

def event_m20_24_x114(z46=100804, z47=20246500):
    """[Preset] Get the king's ring
    z46: Ring acquisition global event flag
    z47: King Ring OBJ Instance ID
    """
    """State 0,1: [Reproduction] Get the king's ring_Sky_SubState"""
    assert event_m20_24_x111()
    """State 3: [Condition] _SubState to get the king's ring"""
    assert event_m20_24_x112(z47=z47)
    """State 2: [Execution] Get the king's ring_SubState"""
    assert event_m20_24_x113(z46=z46)
    """State 4: End state"""
    return 0

def event_m20_24_x115():
    """[Reproduction] Enemy operation when the bell rings"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x116(z7=_, z6=_):
    """[Execution] Enemies start when ringing bells_Loop_Flag ON
    z7: Bell OBJ instance ID
    z6: Enemy operation flag
    """
    """State 0,1: Anime playback with bells ringing: 100"""
    ChangeObjState(z7, 100)
    """State 3: Bell ringing waiting"""
    if CompareObjStateId(z7, 80, 0):
        """State 2: Enemy operation flag ON"""
        SetEventFlag(z6, 1)
    elif CompareObjStateId(z7, 10, 0):
        """State 4,5: Enemy operation flag OFF"""
        SetEventFlag(z6, 0)
    """State 6: Rerun"""
    return 0

def event_m20_24_x117(z7=_):
    """[Condition] Enemies start when the bell rings
    z7: Bell OBJ instance ID
    """
    """State 0,1: Was the attack or the bell already ringing?"""
    IsObjDamaged(0, z7, -1, -1, 0)
    CompareObjState(1, z7, 10, 1)
    if ConditionGroup(1):
        """State 2: Are you under attack or ending the ringing?"""
        IsObjDamaged(0, z7, -1, -1, 0)
        CompareObjState(1, z7, 90, 0)
        if ConditionGroup(1):
            """State 3: Have you been attacked or finished ringing?"""
            IsObjDamaged(0, z7, -1, -1, 0)
            CompareObjState(1, z7, 10, 0)
            if ConditionGroup(1):
                """State 5: Stop: It has finished ringing"""
                return 1
            elif ConditionGroup(0):
                pass
        elif ConditionGroup(0):
            """State 4: On the way: under attack"""
            return 0
    elif ConditionGroup(0):
        pass
    """State 6: Initial action: attacked"""
    return 2

def event_m20_24_x118(z43=20241100, z42=224020011):
    """[Execution] When the bell rings, the enemy is in operation_flag OFF
    z43: Bell OBJ instance ID
    z42: Enemy operation flag
    """
    """State 0,1: Enemy operation flag OFF"""
    SetEventFlag(z42, 0)
    """State 2: Rerun"""
    return 0

def event_m20_24_x119(z42=224020011, z43=20241100):
    """[Preset] Enemy operation when the bell rings
    z42: Enemy operation flag
    z43: Bell OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemies operation when ringing bell_Sky_SubState"""
    assert event_m20_24_x115()
    """State 4: [Condition] When the bell rings, the enemy is in operation _SubState"""
    call = event_m20_24_x117(z7=z43)
    if call.Get() == 2:
        """State 5: [Execution] Enemies start when ringing bell_Initial action_Flag ON_SubState"""
        assert event_m20_24_x126(z7=z43, z6=z42)
    elif call.Get() == 0:
        """State 3: [Execution] Enemies start when ringing bell_Loop_Flag ON_SubState"""
        assert event_m20_24_x116(z7=z43, z6=z42)
    elif call.Get() == 1:
        """State 2: [Execution] When the bell rings, the enemy is operating_flag OFF_SubState"""
        assert event_m20_24_x118(z43=z43, z42=z42)
    """State 6: End state"""
    return 0

def event_m20_24_x120(z40=_, z39=_, z41=_):
    """[Execution] Enemies start when ringing bells_flag OFF_bells
    z40: Bell OBJ instance ID
    z39: Enemy operation flag
    z41: Other bell OBJ instance ID
    """
    """State 0,2: Are other bells ringing?"""
    if CompareObjStateId(z41, 10, 1):
        """State 3: Operation flag remains"""
        pass
    else:
        """State 1: Enemy operation flag OFF"""
        SetEventFlag(z39, 0)
    """State 4: Rerun"""
    return 0

def event_m20_24_x121(z39=_, z40=_, z41=_):
    """[Preset] Enemies working when ringing bells
    z39: Enemy operation flag
    z40: Bell OBJ instance ID
    z41: Other bell OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemies operation when ringing bell_Sky_SubState"""
    assert event_m20_24_x115()
    """State 3: [Condition] When the bell rings, the enemy is in operation _SubState"""
    call = event_m20_24_x117(z7=z40)
    if call.Get() == 2:
        """State 5: [Execution] Enemies start when ringing bell_Initial action_Flag ON_SubState"""
        assert event_m20_24_x126(z7=z40, z6=z39)
    elif call.Get() == 0:
        """State 2: [Execution] Enemies start when ringing bell_Loop_Flag ON_SubState"""
        assert event_m20_24_x116(z7=z40, z6=z39)
    elif call.Get() == 1:
        """State 4: [Execution] When the bell rings, enemies are operating_flag OFF_bell multiple_SubState"""
        assert event_m20_24_x120(z40=z40, z39=z39, z41=z41)
    """State 6: End state"""
    return 0

def event_m20_24_x122(z44=_, z45=_):
    """[Preset] Enemy generation stops due to tombstone destruction
    z44: Tombstone OBJ instance ID
    z45: Tombstone destruction flag
    """
    """State 0,1: [Reproduction] Generation of enemies stops due to tombstone destruction_SubState"""
    call = event_m20_24_x123(z44=z44)
    if call.Get() == 0:
        """State 2: [Condition] Due to tombstone destruction, enemy generation stops_SubState"""
        assert event_m20_24_x124(z44=z44)
        """State 3: [Execution] Due to tombstone destruction, enemy generation stops_SubState"""
        assert event_m20_24_x125(z45=z45)
    elif call.Get() == 1:
        pass
    """State 4: End state"""
    return 0

def event_m20_24_x123(z44=_):
    """[Reproduction] Generation of enemies stops due to destruction of tombstones
    z44: Tombstone OBJ instance ID
    """
    """State 0,1: Judgment of state of destruction stone"""
    if CompareObjStateId(z44, 20, 0):
        """State 3: Destroyed"""
        return 1
    else:
        """State 2: Undestructed"""
        return 0

def event_m20_24_x124(z44=_):
    """[Condition] Enemy generation stops due to tombstone destruction
    z44: Tombstone OBJ instance ID
    """
    """State 0,1: Was the gravestone OBJ destroyed?"""
    CompareObjState(0, z44, 20, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x125(z45=_):
    """[Execution] Due to the tombstone destruction, enemy generation stops
    z45: Tombstone destruction flag
    """
    """State 0,1: Turn on the tombstone destruction flag"""
    SetEventFlag(z45, 1)
    """State 2: End state"""
    return 0

def event_m20_24_x126(z7=_, z6=_):
    """[Execution] When the bell rings, enemies are activated.
    z7: Bell OBJ instance ID
    z6: Enemy operation flag
    """
    """State 0,1: Anime playback with bells ringing: 70"""
    ChangeObjState(z7, 70)
    """State 3: Bell ringing waiting"""
    assert CompareObjStateId(z7, 10, 1)
    """State 2: Enemy operation flag ON"""
    SetEventFlag(z6, 1)
    """State 4: Rerun"""
    return 0

def event_m20_24_x127(z37=224000081, z38=102):
    """[Preset] BGM playback in the king's room
    z37: Queen's Knight B Defeat Flag
    z38: Sound ID to ring in the king's room
    """
    """State 0,1: [Reproduction] BGM playback of the king's room_SubState"""
    assert event_m20_24_x128()
    """State 2: [Condition] BGM playback of the king's room_SubState"""
    assert event_m20_24_x129(z37=z37)
    """State 3: [Execution] BGM playback of the king's room_SubState"""
    assert event_m20_24_x130(z38=z38)
    """State 4: End state"""
    return 0

def event_m20_24_x128():
    """[Reproduction] BGM playback of the king's room"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x129(z37=224000081):
    """[Condition] BGM playback in the king's room
    z37: Queen's Knight B Defeat Flag
    """
    """State 0,1: Did you destroy Queen Knight B?"""
    CompareEventFlag(0, z37, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x130(z38=102):
    """[Execution] BGM playback of the king's room
    z38: Sound ID to ring in the king's room
    """
    """State 0,1: BGM playback"""
    PlaySoundAtPoint(z38)
    """State 2: End state"""
    return 0

def event_m20_24_x131(z16=20240700, z17=70, z18=224000050):
    """[Preset] A huge candlestick is lit
    z16: Igniter instance ID
    z17: OBJ state ID for SFX lighting
    z18: All lighting complete flag
    """
    """State 0,2: [Reproduction] Giant candlestick state reproduction_SubState"""
    call = event_m20_24_x94(z18=z18)
    if call.Get() == 11:
        pass
    elif call.Get() == 12:
        """State 16: [Conditions] Huge candlestick lights_Guest_SubState"""
        assert event_m20_24_x166(z18=z18)
        """State 15: [Execute] Huge candlestick lights_Guest_SubState"""
        assert event_m20_24_x165()
        """State 1: Guest waiting"""
        Label('L0')
        SetConditionGroupTrue(0)
        assert HostConditionGroup(0)
    elif call.Get() == 10:
        """State 14: [Execute] Huge candlestick lighting_Last_SubState"""
        Label('L1')
        assert event_m20_24_x164(z17=z17, z19=20242005, z18=z18)
        Goto('L0')
    elif call.Get() == 9:
        """State 13: [Execute] Huge candlestick lighting_10_SubState"""
        Label('L2')
        assert event_m20_24_x132(z35=1.1, z17=z17, z36=20242010)
        Goto('L1')
    elif call.Get() == 8:
        """State 12: [Execution] Huge candlestick lighting_9_SubState"""
        Label('L3')
        assert event_m20_24_x132(z35=1.5, z17=z17, z36=20242060)
        Goto('L2')
    elif call.Get() == 7:
        """State 11: [Execution] Huge candlestick lighting_8_SubState"""
        Label('L4')
        assert event_m20_24_x132(z35=0.7, z17=z17, z36=20242055)
        Goto('L3')
    elif call.Get() == 6:
        """State 10: [Execute] Huge candlestick lighting_7_SubState"""
        Label('L5')
        assert event_m20_24_x132(z35=0.2, z17=z17, z36=20242045)
        Goto('L4')
    elif call.Get() == 5:
        """State 9: [Execution] Huge candlestick lighting_6_SubState"""
        Label('L6')
        assert event_m20_24_x132(z35=0.9, z17=z17, z36=20242025)
        Goto('L5')
    elif call.Get() == 4:
        """State 8: [Execute] Huge candlestick lighting_5_SubState"""
        Label('L7')
        assert event_m20_24_x132(z35=1.4, z17=z17, z36=20242040)
        Goto('L6')
    elif call.Get() == 3:
        """State 7: [Execute] Huge candlestick lighting_4_SubState"""
        Label('L8')
        assert event_m20_24_x132(z35=0.7, z17=z17, z36=20242035)
        Goto('L7')
    elif call.Get() == 2:
        """State 6: [Execution] Huge candlestick lighting_3_SubState"""
        Label('L9')
        assert event_m20_24_x132(z35=0.5, z17=z17, z36=20242030)
        Goto('L8')
    elif call.Get() == 1:
        """State 5: [Execute] Huge candlestick lighting_2_SubState"""
        Label('L10')
        assert event_m20_24_x132(z35=1.3, z17=z17, z36=20242000)
        Goto('L9')
    elif call.Get() == 0:
        """State 3: [Conditions] Ignition stand state determination for huge candlesticks_SubState"""
        assert event_m20_24_x95(z16=z16)
        """State 4: [Execute] Huge candlestick lighting_SubState"""
        assert event_m20_24_x132(z35=0.7, z17=z17, z36=20242050)
        Goto('L10')
    """State 17: End state"""
    return 0

def event_m20_24_x132(z35=_, z17=70, z36=_):
    """[Execute] Huge candlestick lights
    z35: State elapsed time
    z17: OBJ state ID for SFX lighting
    z36: Instance ID of giant candlestick OBJ
    """
    """State 0,1: Giant candlestick SFX generation"""
    ChangeObjState(z36, z17)
    """State 2: A certain amount of time has elapsed"""
    CompareStateTime(8, z35, 2, z35)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m20_24_x133():
    """[Reproduction] King's white door management"""
    """State 0,2: Turn on the white door control flag"""
    SetEventFlag(224000087, 1)
    """State 1: Has the king been destroyed?"""
    if GetEventFlag(224000086) != 0:
        """State 4: Simple end"""
        return 1
    else:
        """State 3: End state"""
        return 0

def event_m20_24_x134():
    """[Conditions] King's white door management"""
    """State 0,1: Did you hostile with the king?"""
    CompareEventFlag(0, 224000088, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x135():
    """[Execution] King's white door management"""
    """State 0,2: Set the white door control flag to OFF"""
    SetEventFlag(224000087, 0)
    """State 1: Did you destroy the king?"""
    CompareEventFlag(0, 224000086, 1)
    assert ConditionGroup(0)
    """State 3: Turn on the white door control flag"""
    SetEventFlag(224000087, 1)
    """State 4: End state"""
    return 0

def event_m20_24_x136():
    """[Preset] King's white door management"""
    """State 0,1: [Reproduction] King's white door management_SubState"""
    call = event_m20_24_x133()
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [Condition] King's white door management_SubState"""
        assert event_m20_24_x134()
        """State 2: [Execution] King's White Door Management_SubState"""
        assert event_m20_24_x135()
    """State 4: End state"""
    return 0

def event_m20_24_x137():
    """[Reproduction] Adversity judgment of king"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x138(z33=230):
    """[Condition] King's hostility judgment
    z33: King's generator ID
    """
    """State 0,1: Have you reduced your HP to a certain level?"""
    CompareChrHpRatio(0, z33, 95, 5)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x139(z34=224000088):
    """[Execution] King's Adversity Judgment
    z34: King's hostile flag
    """
    """State 0,1: Hostile flag ON"""
    SetEventFlag(z34, 1)
    SaveExecution()
    """State 2: End state"""
    return 0

def event_m20_24_x140(z33=230, z34=224000088):
    """[Preset] King's Adversity Judgment
    z33: King's generator ID
    z34: King's hostile flag
    """
    """State 0,1: [Reproduction] King's hostility determination_SubState"""
    assert event_m20_24_x137()
    """State 3: [Condition] King's hostility determination_SubState"""
    assert event_m20_24_x138(z33=z33)
    """State 2: [Execution] King's hostility determination_SubState"""
    assert event_m20_24_x139(z34=z34)
    """State 4: End state"""
    return 0

def event_m20_24_x141(z28=224000086):
    """[Reproduction] King_Boss Battle
    z28: King defeat flag
    """
    """State 0,1: Are you destroying the king?"""
    if GetEventFlag(z28) != 0:
        """State 3: Defeated"""
        return 1
    else:
        """State 2: Not defeated"""
        return 0

def event_m20_24_x142():
    """[Reproduction] King_Boss Battle_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x143(z29=802010, z32=224000088):
    """[Conditions] King_Boss Battle_Start Judgment
    z29: Start judgment point ID
    z32: Hostile flag
    """
    """State 0,1: Are you in point with hostility?"""
    CompareEventFlag(8, z32, 1)
    IsPlayerInsidePoint(8, z29, z29, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_24_x144(z30=2024010):
    """[Conditions] King_Boss Battle_End Judgment
    z30: Boss Battle ID
    """
    """State 0,1: Destroy the king?"""
    IsEventBossKill(0, z30, 0, 1)
    assert ConditionGroup(0)
    """State 2: End of boss destruction"""
    return 0

def event_m20_24_x145(z30=2024010, z31=224020085):
    """[Execution] King_Boss Battle_Start
    z30: Boss Battle ID
    z31: Logic flag
    """
    """State 0,1: Boss battle start notification"""
    StartBossFight(z30)
    """State 2: Boss battle flag notification for logic"""
    SetEventFlag(z31, 1)
    """State 3: End state"""
    return 0

def event_m20_24_x146(z30=2024010, z31=224020085):
    """[Execution] King_Boss Battle_End
    z30: Boss Battle ID
    z31: Logic flag
    """
    """State 0,1: Logic flag OFF"""
    SetEventFlag(z31, 0)
    """State 2: Boss battle end notification"""
    EndBossFight(z30)
    """State 3: End state"""
    return 0

def event_m20_24_x147(z28=224000086, z29=802010, z30=2024010, z31=224020085, z32=224000088):
    """[Preset] King_Boss Battle
    z28: King defeat flag
    z29: Start judgment point ID
    z30: Boss Battle ID
    z31: Logic flag
    z32: Hostile flag
    """
    """State 0,1: [Reproduction] King_Boss Battle_SubState"""
    call = event_m20_24_x141(z28=z28)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 5: [Condition] King_Boss Battle_Start Judgment_SubState"""
        assert event_m20_24_x143(z29=z29, z32=z32)
        """State 3: [Execution] King_Boss Battle_Start_SubState"""
        assert event_m20_24_x145(z30=z30, z31=z31)
        """State 2: [Reproduction] King_Boss Battle_Sky_SubState"""
        assert event_m20_24_x142()
        """State 6: [Condition] King_Boss Battle_End Judgment_SubState"""
        assert event_m20_24_x144(z30=z30)
        """State 4: [Execution] King_Boss Battle_End_SubState"""
        assert event_m20_24_x146(z30=z30, z31=z31)
    """State 7: Finish"""
    return 0

def event_m20_24_x148(z27=20246500):
    """[DLC] [Reproduction] Warp to memory of Van Clad
    z27: King Ring OBJ Instance ID
    """
    """State 0,2: Host?"""
    if IsGuest() != 1:
        """State 3: Have you finished the quest?"""
        if GetEventFlag(103201) != 0:
            """State 5: Hide OBJ: 31"""
            ChangeObjState(z27, 31)
        else:
            """State 1: OBJ state initialization"""
            ChangeObjState(z27, 10)
            assert CompareObjStateId(z27, 10, 0)
            """State 4: End of event if DLC is not purchased"""
            CompareEventFlag(0, 100610, 1)
            CompareEventFlag(0, 100611, 1)
            CompareEventFlag(0, 100612, 1)
            CompareEventFlag(0, 100613, 1)
            if ConditionGroup(0):
                """State 6: End state"""
                return 0
            else:
                pass
    else:
        pass
    """State 7: Guest or not purchased or finished"""
    return 1

def event_m20_24_x149(z27=20246500):
    """[DLC] [Condition] Warp to memory of Van Clad
    z27: King Ring OBJ Instance ID
    """
    """State 0,3: Is it single play?"""
    IsMultiplayer(0, 0, 1)
    assert ConditionGroup(0)
    """State 2: Get a king's ring and not fighting with the king?"""
    CompareEventFlag(8, 100804, 1)
    CompareEventFlag(8, 100603, 1)
    CompareEventFlag(8, 224020085, 0)
    CompareEventFlag(1, 224020085, 1)
    if ConditionGroup(1):
        """State 6: Did you destroy the king?"""
        CompareEventFlag(0, 224000086, 1)
        assert ConditionGroup(0)
    elif ConditionGroup(8):
        pass
    """State 4: Activate key guide"""
    ChangeObjState(20246500, 30)
    """State 5: Have you been fighting with the king or king who investigated OBJ?"""
    IsObjSearched(0, z27)
    IsMultiplayer(1, 1, 1)
    CompareEventFlag(1, 224020085, 1)
    if ConditionGroup(1):
        """State 7: Key guide disabled"""
        return 0
    elif ConditionGroup(0):
        """State 1: Do you have an ash mist core?"""
        # goods:50910000:Ashen Mist Heart
        DoesPlayerHaveItem(0, 50910000, 1, 3, 1, 1, 0)
        if ConditionGroup(0):
            """State 9: Warp execution"""
            return 2
        else:
            """State 8: Nothing happens"""
            return 1

def event_m20_24_x150():
    """[DLC] [execution] Warp to warp memory"""
    """State 0,1: Warp PC action"""
    PlayerActionRequest(6)
    assert PlayerIsInEventAction(6) != 0
    """State 2: Wait for action to finish"""
    CompareStateTime(0, 1.5, 2, 1.5)
    IsPlayerPlayingMotion(1, 6, 0)
    if ConditionGroup(1):
        pass
    elif ConditionGroup(0):
        """State 3: Warp SFX playback PC invincible"""
        PlaySfxSelfGenerated(8002, 239, 190)
        SetPlayerInvincible(1)
        assert (GetStateTime() > 2.5) != 0
        """State 5: [Lib] Warp between maps after poly play_SubState"""
        assert event_m20_24_x0(z152=0, z153=0, z154=50380000, z155=5000000)
        """State 4: Invincible OFF"""
        SetPlayerInvincible(0)
    """State 6: End state"""
    return 0

def event_m20_24_x151(z27=20246500):
    """[DLC] [Execution] Warp to memory of Van Clad_Key guide invalid
    z27: King Ring OBJ Instance ID
    """
    """State 0,1: OBJ state initialization"""
    ChangeObjState(z27, 10)
    assert CompareObjStateId(z27, 10, 0)
    """State 2: End state"""
    return 0

def event_m20_24_x152():
    """[DLC] [execution] Warp to memory of Van Clad_Nothing happens"""
    """State 0,1: Message display"""
    # action:1113:"Alas, nothing happened"
    DisplayOwnOkMenu(1113, 0, 0, 190, 0, 0, 0)
    """State 2: End state"""
    return 0

def event_m20_24_x153(z27=20246500):
    """[DLC] [Preset] Warp to memory of Van Clad
    z27: King Ring OBJ Instance ID
    """
    """State 0,1: [DLC] [Reproduction] Warp_SubState to Van Clad Memory"""
    call = event_m20_24_x148(z27=z27)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        Goto('L0')
    """State 7: Finish"""
    return 1
    """State 3: [DLC] [Conditions] Warp_SubState to Van Clad Memory"""
    Label('L0')
    call = event_m20_24_x149(z27=z27)
    if call.Get() == 2:
        """State 5: [DLC] [Execution] Warp Warm Execution_SubState to Vanclad Memory"""
        assert event_m20_24_x150()
    elif call.Get() == 0:
        """State 4: [DLC] [Execution] Warp to Van Clad Memory_Key Guide Invalid_SubState"""
        assert event_m20_24_x151(z27=z27)
    elif call.Get() == 1:
        """State 2: [DLC] [execution] Warp to Vanclad's memory_Nothing happens_SubState"""
        assert event_m20_24_x152()
    """State 6: Rerun"""
    return 0

def event_m20_24_x154():
    """[DLC] [Reproduction] Sound reproduction of the king's armor"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x155(z22=5100000, z26=5100000, z24=103201):
    """[DLC] [Condition] Sound reproduction of the light insect of the king's armor
    z22: Sound playback start point ID
    z26: Sound end start point ID
    z24: Quest end flag
    """
    """State 0,1: Did you get into the point? Have you finished the quest?"""
    IsPlayerInsidePoint(0, z22, z26, 1)
    CompareEventFlag(1, z24, 1)
    if ConditionGroup(1):
        """State 3: Quest finished"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m20_24_x156():
    """[DLC] [execution] Sound reproduction of king armor's light insect"""
    """State 0,1: Play sound"""
    PlaySoundFollowingSelf(4, 5034, 190)
    """State 2: End state"""
    return 0

def event_m20_24_x157(z22=5100000, z23=5100010, z24=103201):
    """[DLC] [Preset] Sound reproduction of king armor's light insect
    z22: Sound playback start point ID
    z23: Sound stop start point ID
    z24: Quest end flag
    """
    """State 0,1: [DLC] [Reproduction] Sound playback of the king's armor _SubState"""
    assert event_m20_24_x154()
    """State 2: [DLC] [Condition] Reproduction of the sound of the worm's armor _SubState"""
    call = event_m20_24_x155(z22=z22, z26=z22, z24=z24)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DLC] [Execution] Sound reproduction of the worm armor _SubState"""
        assert event_m20_24_x156()
        """State 4: [DLC] [Condition] Sound playback of king's armor _Stop judgment_SubState"""
        call = event_m20_24_x158(z23=z23, z25=z23, z24=z24)
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 5: [DLC] [execution] Sound playback of king's armor _stop_SubState"""
            assert event_m20_24_x159()
            """State 6: Rerun"""
            return 0
    """State 7: Finish"""
    return 1

def event_m20_24_x158(z23=5100010, z25=5100010, z24=103201):
    """[DLC] [Condition] Sound playback of king's armor
    z23: Sound playback start point ID
    z25: Sound end start point ID
    z24: Quest end flag
    """
    """State 0,1: Did you get out of the point? Have you finished the quest?"""
    IsPlayerInsidePoint(0, z23, z25, 0)
    CompareEventFlag(1, z24, 1)
    if ConditionGroup(1):
        """State 3: Quest finished"""
        return 1
    elif ConditionGroup(0):
        """State 2: End state"""
        return 0

def event_m20_24_x159():
    """[DLC] [Execution] Sound playback of king's armor _ Stop"""
    """State 0,1: Sound stop"""
    StopSoundFollowingSelf()
    """State 2: End state"""
    return 0

def event_m20_24_x160(z20=224000001, z21=100730):
    """[DLC] [Reproduction] Message display when crown function is released
    z20: Message display flag
    z21: Crown function release flag
    """
    """State 0,2: Has the function of the crown been released?"""
    if GetEventFlag(z21) != 1:
        pass
    else:
        """State 1: Is the message already displayed?"""
        if GetEventFlag(z20) != 0:
            pass
        else:
            """State 3: Not showing"""
            return 0
    """State 4: Finish"""
    return 1

def event_m20_24_x161(z21=100730):
    """[DLC] [Condition] Message display when crown function is released
    z21: Crown function release flag
    """
    """State 0,1: Has the crown function been released?"""
    CompareEventFlag(0, z21, 1)
    assert ConditionGroup(0)
    """State 2: Message display"""
    return 0

def event_m20_24_x162(z20=224000001, action1=5900):
    """[DLC] [execution] Message display when crown function is released
    z20: Message display flag
    action1: Text ID
    """
    """State 0,3: weight"""
    assert (GetStateTime() > 8) != 0
    """State 2: Message display flag ON"""
    SetEventFlag(z20, 1)
    """State 1: Message display"""
    # action:5900:"Heat radiates from the ancient crowns"
    DisplayEventMessage(action1, 0, 0, 0)
    """State 4: Finish"""
    return 0

def event_m20_24_x163(z20=224000001, z21=100730, action1=5900):
    """[DLC] [Preset] Message display when crown function is released
    z20: Message display flag
    z21: Crown function release flag
    action1: Text ID
    """
    """State 0,1: [DLC] [Reproduction] Message display when crown function is released_SubState"""
    call = event_m20_24_x160(z20=z20, z21=z21)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DLC] [Condition] Message display when crown function is released_SubState"""
        assert event_m20_24_x161(z21=z21)
        """State 2: [DLC] [Execution] Message display when crown function is released_SubState"""
        assert event_m20_24_x162(z20=z20, action1=action1)
    """State 4: Finish"""
    return 0

def event_m20_24_x164(z17=70, z19=20242005, z18=224000050):
    """[Execution] Huge candlestick lighting_Last
    z17: OBJ state ID for SFX lighting
    z19: Instance ID of giant candlestick OBJ
    z18: All lighting complete flag
    """
    """State 0,1: Giant candlestick SFX generation Enemy generation flag and all lighting flag ON message display"""
    ChangeObjState(z19, z17)
    # action:9100:"When light is revealed, the shadows rise..."
    DisplayEventMessage(9100, 0, 0, 0)
    SetEventFlag(z18, 1)
    SetEventFlag(224000051, 1)
    SetEventFlag(224000052, 1)
    SetEventFlag(224000053, 1)
    SetEventFlag(224000054, 1)
    SetEventFlag(224000055, 1)
    SetEventFlag(224000056, 1)
    SetEventFlag(224000057, 1)
    SetEventFlag(224000058, 1)
    SetEventFlag(224000059, 1)
    SetEventFlag(224000060, 1)
    SetEventFlag(224000061, 1)
    """State 2: Wait for flag"""
    CompareEventFlag(8, z18, 1)
    CompareEventFlag(8, 224000051, 1)
    CompareEventFlag(8, 224000052, 1)
    CompareEventFlag(8, 224000053, 1)
    CompareEventFlag(8, 224000054, 1)
    CompareEventFlag(8, 224000055, 1)
    CompareEventFlag(8, 224000056, 1)
    CompareEventFlag(8, 224000057, 1)
    CompareEventFlag(8, 224000058, 1)
    CompareEventFlag(8, 224000059, 1)
    CompareEventFlag(8, 224000060, 1)
    CompareEventFlag(8, 224000061, 1)
    assert ConditionGroup(8)
    """State 3: End state"""
    return 0

def event_m20_24_x165():
    """[Execution] Lighting a huge candlestick_Guest"""
    """State 0,1: Message display"""
    # action:9100:"When light is revealed, the shadows rise..."
    DisplayEventMessage(9100, 0, 0, 0)
    """State 2: End state"""
    return 0

def event_m20_24_x166(z18=224000050):
    """[Conditions] Large candlestick lights_guest
    z18: All lighting complete flag
    """
    """State 0,1: Wait for flag"""
    CompareEventFlag(8, z18, 1)
    CompareEventFlag(8, 224000051, 1)
    CompareEventFlag(8, 224000052, 1)
    CompareEventFlag(8, 224000053, 1)
    CompareEventFlag(8, 224000054, 1)
    CompareEventFlag(8, 224000055, 1)
    CompareEventFlag(8, 224000056, 1)
    CompareEventFlag(8, 224000057, 1)
    CompareEventFlag(8, 224000058, 1)
    CompareEventFlag(8, 224000059, 1)
    CompareEventFlag(8, 224000060, 1)
    CompareEventFlag(8, 224000061, 1)
    assert ConditionGroup(8)
    """State 2: End state"""
    return 0

def event_m20_24_x167(z12=3000, z13=_):
    """[DC] [Reproduction] Defeat enemies linked to candlesticks to extinguish
    z12: Lighting event ID
    z13: Enemy generation flag
    """
    """State 0,1: Has the candlestick lighting event ended?"""
    assert EventEnded(z12) != 0
    """State 2: Destroyed?"""
    if GetEventFlag(z13) != 1:
        """State 4: Defeated"""
        return 1
    else:
        """State 3: Waiting for destruction"""
        return 0

def event_m20_24_x168(z14=_):
    """[DC] [Condition] Defeat enemies linked to candlesticks and turn off
    z14: Generator ID
    """
    """State 0,1: Destroyed enemies that appeared in tandem?"""
    IsChrDeadOrRespawnOver(0, z14, 1)
    assert ConditionGroup(0)
    """State 2: Defeat"""
    return 0

def event_m20_24_x169(z13=_, z15=_):
    """[DC] [Execution] Defeat enemies linked to candlesticks to extinguish
    z13: Enemy generation flag
    z15: Candlestick OBJ instance ID
    """
    """State 0,1: Turn off the candlestick. Enemy generation flag OFF"""
    SetEventFlag(z13, 0)
    InitializeObj(z15)
    """State 2: End state"""
    return 0

def event_m20_24_x170(z12=3000, z13=_, z14=_, z15=_):
    """[DC] [Preset] Defeat enemies linked to candlesticks and turn off
    z12: Lighting event ID
    z13: Enemy generation flag
    z14: Generator ID
    z15: Candlestick OBJ instance ID
    """
    """State 0,1: [DC] [Reproduction] Defeating enemies linked to candlesticks to extinguish _SubState"""
    call = event_m20_24_x167(z12=z12, z13=z13)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Defeating enemies linked to candlesticks to extinguish _SubState"""
        assert event_m20_24_x168(z14=z14)
    """State 2: [DC] [Execution] Defeat enemies linked to candlesticks and turn off _SubState"""
    assert event_m20_24_x169(z13=z13, z15=z15)
    """State 4: End state"""
    return 0

def event_m20_24_x171(z10=_):
    """[DC] [Condition] Replenishing bell-ringing characters
    z10: Generator ID
    """
    """State 0,1: Was the target enemy destroyed or depleted?"""
    IsChrDeadOrRespawnOver(0, z10, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x172(z11=_):
    """[DC] [execution] Replenishment of bell-ringing characters
    z11: Defeat flag
    """
    """State 0,1: Defeat flag ON"""
    SetEventFlag(z11, 1)
    """State 2: End state"""
    return 0

def event_m20_24_x173():
    """[DC] [Reproduction] Refilling the bell-ringing character _ Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x174(z10=_, z11=_):
    """[DC] [Preset] Refilling the bell-ringing character
    z10: Generator ID
    z11: Defeat flag
    """
    """State 0,1: [DC] [Reproduction] Refilling the bell-ringing character_Sky_SubState"""
    assert event_m20_24_x173()
    """State 3: [DC] [Condition] Refilling the bell-ringing character_SubState"""
    assert event_m20_24_x171(z10=z10)
    """State 2: [DC] [execution] Replenishing bell-ringing characters_SubState"""
    assert event_m20_24_x172(z11=z11)
    """State 4: End state"""
    return 0

def event_m20_24_x175(z7=_, z6=224020016, z8=_, z9=_):
    """[DC] [Execution] When the bell rings, the enemy is in operation _ flag OFF_ 3 bells
    z7: Bell OBJ instance ID
    z6: Enemy operation flag
    z8: Other bell ① OBJ instance ID
    z9: Other bell ② OBJ instance ID
    """
    """State 0,2: Are other bells ringing?"""
    if CompareObjStateId(z8, 10, 1):
        """State 3: Operation flag remains"""
        Label('L0')
    elif CompareObjStateId(z9, 10, 1):
        Goto('L0')
    else:
        """State 1: Enemy operation flag OFF"""
        SetEventFlag(z6, 0)
    """State 4: Rerun"""
    return 0

def event_m20_24_x176(z6=224020016, z7=_, z8=_, z9=_):
    """[DC] [Preset] When the bell rings, 3 enemies are in operation.
    z6: Enemy operation flag
    z7: Bell OBJ instance ID
    z8: Other bell ① OBJ instance ID
    z9: Other bell ② OBJ instance ID
    """
    """State 0,1: [Reproduction] Enemies operation when ringing bell_Sky_SubState"""
    assert event_m20_24_x115()
    """State 3: [Condition] When the bell rings, the enemy is in operation _SubState"""
    call = event_m20_24_x117(z7=z7)
    if call.Get() == 2:
        """State 4: [Execution] Enemies start when ringing bell_Initial action_Flag ON_SubState"""
        assert event_m20_24_x126(z7=z7, z6=z6)
    elif call.Get() == 0:
        """State 2: [Execution] Enemies start when ringing bell_Loop_Flag ON_SubState"""
        assert event_m20_24_x116(z7=z7, z6=z6)
    elif call.Get() == 1:
        """State 5: [DC] [Execution] When the bell rings, enemies are in operation_flag OFF_3 bells_SubState"""
        assert event_m20_24_x175(z7=z7, z6=z6, z8=z8, z9=z9)
    """State 6: End state"""
    return 0

def event_m20_24_x177(z4=20240710, z5=224000065):
    """[DC] [Reproduction] Enemy appears when the lighthouse is on
    z4: Lighthouse instance ID
    z5: Ignition flag
    """
    """State 0,1: Is it ignited?"""
    if CompareObjStateId(z4, 30, 0):
        """State 2: Ignition flag ON"""
        SetEventFlag(z5, 1)
        """State 4: Ignited"""
        return 1
    else:
        """State 3: Unlit"""
        return 0

def event_m20_24_x178(z4=20240710):
    """[DC] [Condition] Enemy appears when lighthouse is on
    z4: Lighthouse instance ID
    """
    """State 0,1: Ignition standby"""
    CompareObjState(0, z4, 30, 0)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x179(z5=224000065):
    """[DC] [execution] Enemy appears when lighthouse is on
    z5: Ignition flag
    """
    """State 0,1: Ignition flag ON"""
    SetEventFlag(z5, 1)
    """State 2: End state"""
    return 0

def event_m20_24_x180(z4=20240710, z5=224000065):
    """[DC] [Preset] Enemy appears when the lighthouse is on
    z4: Lighthouse instance ID
    z5: Ignition flag
    """
    """State 0,1: [DC] [Reproduction] Appearance of enemies with lighthouse lighting_SubState"""
    call = event_m20_24_x177(z4=z4, z5=z5)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Enemy appears when the lighthouse is lit_SubState"""
        assert event_m20_24_x178(z4=z4)
        """State 2: [DC] [Execution] Appearance of enemies when the lighthouse is lit_SubState"""
        assert event_m20_24_x179(z5=z5)
    """State 4: End state"""
    return 0

def event_m20_24_x181(z2=690, z3=100790):
    """[DC] [Preset] Guided White Spirit Summoning Achievement Judgment
    z2: White Spirit Generator ID
    z3: Summon achievement flag
    """
    """State 0,1: [DC] [Reproduction] Guidance White Spirit Summon Achievement Judgment_SubState"""
    call = event_m20_24_x182(z3=z3)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 3: [DC] [Condition] Judgment white spirit summon achievement determination_SubState"""
        assert event_m20_24_x184(z2=z2)
        """State 2: [DC] [Execute] Guidance White Spirit Summon Achievement Judgment_SubState"""
        assert event_m20_24_x183(z3=z3)
    """State 4: Finish"""
    return 0

def event_m20_24_x182(z3=100790):
    """[DC] [Reproduction] Judgment White Spirit Summoning Achievement Judgment
    z3: Summon achievement flag
    """
    """State 0,1: Host?"""
    if IsGuest() != 0:
        pass
    else:
        """State 2: Have you already summoned?"""
        if GetEventFlag(z3) != 0:
            pass
        else:
            """State 3: Waiting for summon"""
            return 0
    """State 4: Finish"""
    return 1

def event_m20_24_x183(z3=100790):
    """[DC] [Execution] Judgment White Spirit Summon Achievement Judgment
    z3: Summon achievement flag
    """
    """State 0,1: Summon achievement flag ON"""
    SetEventFlag(z3, 1)
    """State 2: End state"""
    return 0

def event_m20_24_x184(z2=690):
    """[DC] [Conditions] Judgment achievement of guided white spirit
    z2: White Spirit Generator ID
    """
    """State 0,1: Was the white spirit summoned?"""
    IsChrActive(0, z2, 1)
    assert ConditionGroup(0)
    """State 2: End state"""
    return 0

def event_m20_24_x185(z1=_):
    """[DC] [Conditions] Immortal senior soldiers unable to lock
    z1: Generator ID
    """
    """State 0,1: Character state judgment"""
    CompareChrEzStateValue(0, z1, 7, 1, 1)
    CompareChrEzStateValue(1, z1, 7, 1, 0)
    if ConditionGroup(1):
        """State 3: In combat"""
        return 1
    elif ConditionGroup(0):
        """State 2: Waiting"""
        return 0

def event_m20_24_x186(z1=_):
    """[DC] [execution] Immortal senior soldiers unable to lock
    z1: Generator ID
    """
    """State 0,1: Grants a non-locking effect"""
    SetEnemySpEffect(z1, 170000000, 19, 4)
    """State 2: Did you start battle or died?"""
    CompareChrEzStateValue(0, z1, 7, 1, 0)
    IsChrDead(0, z1)
    assert ConditionGroup(0)
    """State 3: Cancel lock disable effect"""
    ClearEnemySpEffect(z1, 170000000)
    """State 4: Finish"""
    return 0

def event_m20_24_x187():
    """[DC] [Reproduction] Immortal Senior Soldier Unlockable Management_Sky"""
    """State 0,1: End state"""
    return 0

def event_m20_24_x188(z1=_):
    """[DC] [Preset] Immortal senior soldiers unable to lock
    z1: Generator ID
    """
    """State 0,1: [DC] [Reproduction] Immortal Senior Soldier Unlockable Management_Sky_SubState"""
    assert event_m20_24_x187()
    """State 3: [DC] [Conditions] Immortal senior soldiers unable to lock_SubState"""
    call = event_m20_24_x185(z1=z1)
    if call.Get() == 1:
        pass
    elif call.Get() == 0:
        """State 2: [DC] [Execution] Immortal Senior Soldier Unlockable Management_SubState"""
        assert event_m20_24_x186(z1=z1)
    """State 4: Finish"""
    return 0

def event_m20_24_111022():
    """NPC: Tomb Guard: Grave"""
    """State 0,1: NPC: Tomb Guard: Grave Placement_SubState"""
    event_m20_24_x1(z148=104010, z149=20244000, z150=241, z151=5060)

def event_m20_24_111023():
    """NPC: Tomb Guard: Key Guide"""
    """State 0,1: [Lib] NPC: Grave: Key Guide: General Purpose_SubState"""
    # npc:5060:Grave Warden Agdayne
    event_m20_24_x4(z143=224010100, z144=224020101, z145=104010, z146=20244000, z147=111022, npc1=5060)

def event_m20_24_111024():
    """NPC: Gravekeeper: State change"""
    """State 0,1: State change: Start"""
    IsPlayerInTheMap(0, 1, 0)
    if IsGuest() != 0:
        pass
    elif ConditionGroup(0):
        """State 11: State change: Death judgment"""
        CompareEventFlag(0, 104010, 1)
        if ConditionGroup(0):
            pass
        else:
            """State 12: State change: Approaching conversation judgment"""
            CompareEventFlag(0, 102020, 1)
            if ConditionGroup(0):
                pass
            else:
                """State 3: State change: first standby"""
                IsPlayerInsidePoint(0, 20000000, 20000000, 1)
                IsPlayerInTheMap(1, 0, 0)
                CompareEventFlag(2, 102020, 1)
                IsChrInsidePoint(3, 1000, 20000010, 20000010, 1)
                IsChrActive(4, 240, 0)
                if ConditionGroup(2):
                    pass
                elif ConditionGroup(1):
                    """State 4: State change: System: Re-execution"""
                    Label('L0')
                    RestartMachine()
                    Quit()
                elif ConditionGroup(3):
                    """State 9: State change: hostile state"""
                    Label('L1')
                    SetEventFlag(103510, 1)
                    CompareEventFlag(0, 103510, 1)
                    assert ConditionGroup(0)
                elif ConditionGroup(0):
                    """State 6: State change: State branch"""
                    IsPlayerUsingTorch(0, 1)
                    if ConditionGroup(0):
                        """State 5: State change: light source possession state"""
                        SetEventFlag(224020107, 1)
                        SetEventFlag(224020108, 0)
                        CompareEventFlag(0, 224020107, 1)
                        assert ConditionGroup(0)
                    else:
                        """State 7: State change: light source not owned"""
                        SetEventFlag(224020108, 1)
                        SetEventFlag(224020107, 0)
                        CompareEventFlag(0, 224020108, 1)
                        assert ConditionGroup(0)
                    """State 8: State change: Hostile waiting"""
                    IsPlayerInsidePoint(0, 20000000, 20000000, 0)
                    CompareStateTime(1, 300, 2, 300)
                    IsPlayerInsidePoint(2, 20000010, 20000010, 1)
                    IsChrInsidePoint(3, 1000, 20000010, 20000010, 1)
                    IsChrActive(4, 240, 0)
                    if ConditionGroup(0):
                        Goto('L0')
                    elif ConditionGroup(1):
                        Goto('L0')
                    elif ConditionGroup(3):
                        Goto('L1')
                    elif ConditionGroup(2):
                        """State 10: State change: Within the hostile area"""
                        IsPlayerInsidePoint(0, 20000010, 20000010, 0)
                        IsPlayerUsingTorch(1, 1)
                        CompareEventFlag(2, 102020, 1)
                        IsChrInsidePoint(3, 1000, 20000010, 20000010, 1)
                        IsChrActive(4, 240, 0)
                        if ConditionGroup(2):
                            pass
                        elif ConditionGroup(0):
                            Goto('L0')
                        elif ConditionGroup(1):
                            Goto('L1')
                        elif ConditionGroup(3):
                            Goto('L1')
                        elif ConditionGroup(4):
                            """State 13: Status change: Erase standby"""
                            Label('L2')
                            IsChrActive(0, 240, 1)
                            assert ConditionGroup(0)
                            Goto('L0')
                    elif ConditionGroup(4):
                        Goto('L2')
                elif ConditionGroup(4):
                    Goto('L2')
    """State 2: State change: System: Exit"""
    EndMachine()

def event_m20_24_111025():
    """NPC: Tomb Guard: White Phantom Sign Display"""
    """State 0,1: NPC White Phantom Appearance: General Purpose_SubState"""
    event_m20_24_x31(z113=102030, z114=686, z115=104010, z116=60, z117=103510, z118=-1)

def event_m20_24_118100():
    """Multi-use NPC: White Spirit Test"""
    """State 0,1: NPC White Phantom Appearance: Unconditional_SubState"""
    event_m20_24_x32(z112=690)

def event_m20_24_118220():
    """Multi-use NPC: Magician (Male): Black Phantom Appears"""
    """State 0,2: [Lib] [BEST] NPC Black Phantom Appearance: Online: Miracles"""
    event_m20_24_x72(z78=10000000, z79=680, z80=104320, z81=0, z82=2)

def event_m20_24_1000000():
    """[DLC] Van Clad's memory warp"""
    """State 0,3: [DLC] [Preset] Warp to Memory of Van Clad_SubState"""
    call = event_m20_24_x153(z27=20246500)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m20_24_1001000():
    """[DLC] Reproduction of the light insect of the king's armor"""
    """State 0,3: [DLC] [Preset] Reproduction of sound of worm armor _SubState"""
    call = event_m20_24_x157(z22=5100000, z23=5100010, z24=103201)
    if call.Get() == 1:
        """State 2: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 1: Rerun"""
        RestartMachine()

def event_m20_24_3000000():
    """[DLC] Message display when crown function is released"""
    """State 0,2: [DLC] [Preset] Message display when crown function is released_SubState"""
    # action:5900:"Heat radiates from the ancient crowns"
    assert event_m20_24_x163(z20=224000001, z21=100730, action1=5900)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4000000():
    """[BEST] Andel appearance"""
    """State 0,3: [Lib] [BEST] [Preset] Andiel _ 2nd and later _SubState"""
    call = event_m20_24_x70(z83=20243000, z84=100745, z85=100746, z86=100764, z87=100740, z88=20240651)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m20_24_4001000():
    """[BEST] Phantom management of Andiel"""
    """State 0,3: [Lib] [BEST] [Preset] Phantom management of Andy_SubState"""
    call = event_m20_24_x50(z93=20243000)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m20_24_4002000():
    """[BEST] Bonfire key guide management"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire Key Guide Management_SubState"""
    call = event_m20_24_x60(z89=20243000, z90=20240651)
    if call.Get() == 1:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 0:
        """State 2: Rerun"""
        RestartMachine()

def event_m20_24_4003000():
    """[BEST] SFX management of bonfire"""
    """State 0,3: [Lib] [BEST] [Preset] Bonfire SFX Management_SubState"""
    call = event_m20_24_x55(z91=20243000, z92=20240651)
    if call.Get() == 0:
        """State 1: Finish"""
        EndMachine()
    elif call.Get() == 1:
        """State 2: Rerun"""
        RestartMachine()

def event_m20_24_4010000():
    """[DC] Defeat enemies linked to candlesticks to turn them off_1"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000051, z14=7000, z15=20242050)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010010():
    """[DC] Defeat enemies linked to candlesticks by turning them off_2"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000052, z14=7001, z15=20242000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010020():
    """[DC] Defeat enemies linked to candlesticks_3"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000053, z14=7002, z15=20242030)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010030():
    """[DC] Defeat enemies linked to candlesticks_4"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000054, z14=7003, z15=20242035)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010040():
    """[DC] Defeat enemies linked with candlesticks_5"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000055, z14=7004, z15=20242040)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010050():
    """[DC] Defeat enemies linked to candlesticks_6"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000056, z14=7005, z15=20242025)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010060():
    """[DC] Defeat enemies linked to candlesticks_7"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000057, z14=7006, z15=20242045)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010070():
    """[DC] Defeat enemies linked to candlesticks_8"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000058, z14=7007, z15=20242055)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010080():
    """[DC] Defeat enemies linked to candlesticks_9"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000059, z14=7008, z15=20242060)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010090():
    """[DC] Defeat enemies linked to candlesticks_10"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000060, z14=7009, z15=20242010)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4010100():
    """[DC] Defeat enemies linked to candlesticks_11"""
    """State 0,2: [DC] [Preset] Turn off the enemies linked to the candlestick_SubState"""
    assert event_m20_24_x170(z12=3000, z13=224000061, z14=7010, z15=20242005)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4011000():
    """[DC] Replenishing bell-ringing characters_1"""
    """State 0,2: [DC] [Preset] Refilling bell-ringing characters_SubState"""
    assert event_m20_24_x174(z10=3700, z11=224020040)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4011010():
    """[DC] Replenishing bell-ringing characters_2"""
    """State 0,2: [DC] [Preset] Refilling bell-ringing characters_SubState"""
    assert event_m20_24_x174(z10=3701, z11=224020041)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4012000():
    """[DC] Enemy appears when the lighthouse is turned on_1"""
    """State 0,2: [DC] [Preset] Appearance of enemies with lighthouse lighting_SubState"""
    assert event_m20_24_x180(z4=20240710, z5=224000065)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4015000():
    """[DC] When the bell rings, the enemy is in operation_entrance_A"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020012, z40=20241210, z41=20241215)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4015010():
    """[DC] When the bell rings, the enemy is in operation_entrance_B"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020012, z40=20241215, z41=20241210)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4016000():
    """[DC] Enemies start when ringing bells"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020013, z40=20241200, z41=20241205)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4016010():
    """[DC] Enemies start when ringing bells"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020013, z40=20241205, z41=20241200)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4017000():
    """[DC] When the bell rings, enemies start _room border_A"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020014, z40=20241220, z41=20241225)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4017010():
    """[DC] When the bell rings, enemies start _room border_B"""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020014, z40=20241225, z41=20241220)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4018000():
    """[DC] When the bell rings, the enemy is in operation."""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020015, z40=20241230, z41=20241235)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4018010():
    """[DC] When the bell rings, the enemy is in operation."""
    """State 0,2: [Preset] Enemies working when ringing bell_bells_SubState"""
    assert event_m20_24_x121(z39=224020015, z40=20241235, z41=20241230)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4019000():
    """[DC] When the bell rings, the enemy is in operation."""
    """State 0,2: [DC] [Preset] When the bell rings, enemies are in operation _ Three bells _ SubState"""
    assert event_m20_24_x176(z6=224020016, z7=20241240, z8=20241245, z9=20241250)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4019010():
    """[DC] When the bell rings, the enemy is in operation."""
    """State 0,2: [DC] [Preset] When the bell rings, enemies are in operation _ Three bells _ SubState"""
    assert event_m20_24_x176(z6=224020016, z7=20241245, z8=20241240, z9=20241250)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4019020():
    """[DC] When the bell rings, the enemy is in operation."""
    """State 0,2: [DC] [Preset] When the bell rings, enemies are in operation _ Three bells _ SubState"""
    assert event_m20_24_x176(z6=224020016, z7=20241250, z8=20241245, z9=20241240)
    """State 1: Rerun"""
    RestartMachine()

def event_m20_24_4020000():
    """[DC] Wanderer A_Random lottery and generation"""
    """State 0,3: [Lib] [DC] [Preset] Wanderer_Random Drawing_SubState"""
    call = event_m20_24_x76(z61=224020004, z62=14, z63=224000005, z64=2, z65=10)
    if call.Get() == 0:
        pass
    elif call.Get() == 1:
        """State 4: [Lib] [DC] [Preset] Wanderer_Generation_SubState"""
        assert event_m20_24_x81(z71=80000000, z72=0, z73=5, z74=971, val1=1, z75=10, z76=80000001, z77=80000099)
        """State 5: [Lib] [DC] [Preset] Wanderer_Generation_2_SubState"""
        assert event_m20_24_x81(z71=80000100, z72=0, z73=5, z74=971, val1=2, z75=10, z76=80000101, z77=80000199)
        """State 2: Start flag ON"""
        SetEventFlag(224020006, 1)
    elif call.Get() == 2:
        pass
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4020010():
    """[DC] Wanderer A_Destroy"""
    """State 0,2: [Lib] [DC] [Preset] Wanderer_Destroy_SubState"""
    assert event_m20_24_x84(z68=224000005, z69=971, mode1=1)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4021000():
    """[DC] Guided white spirit summon achievement achievement judgment"""
    """State 0,2: [DC] [Preset] Guidance White Spirit Summon Achievement Judgment_SubState"""
    assert event_m20_24_x181(z2=690, z3=100790)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4022000():
    """[DC] Immortal Senior Soldier Unlockable Management_1"""
    """State 0,2: [DC] [Preset] Immortal Senior Soldier Unlockable Management_SubState"""
    assert event_m20_24_x188(z1=1101)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4022010():
    """[DC] Immortal senior soldiers unable to lock_2"""
    """State 0,2: [DC] [Preset] Immortal Senior Soldier Unlockable Management_SubState"""
    assert event_m20_24_x188(z1=1102)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4022020():
    """[DC] Immortal senior soldiers unable to lock_3"""
    """State 0,2: [DC] [Preset] Immortal Senior Soldier Unlockable Management_SubState"""
    assert event_m20_24_x188(z1=1103)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030000():
    """[DC] Transparent character_1"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9000, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030010():
    """[DC] Transparent character_2"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9001, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030020():
    """[DC] Transparent character_3"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9002, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030040():
    """[DC] Transparent character_5"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9004, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030050():
    """[DC] Transparent character_6"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9005, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030060():
    """[DC] Transparent character _7"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9006, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030070():
    """[DC] Transparent character _8"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9007, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030080():
    """[DC] Transparent character _9"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9008, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030090():
    """[DC] Transparent character_10"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9009, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030110():
    """[DC] Transparent character _12"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9011, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030120():
    """[DC] Transparent character _13"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9012, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030130():
    """[DC] Transparent character _14"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9013, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4030140():
    """[DC] Transparent character _15"""
    """State 0,2: [Lib] [DC] [Preset] Transparent character_SubState"""
    assert event_m20_24_x88(z66=9014, z67=96960000)
    """State 1: Finish"""
    EndMachine()

def event_m20_24_4031000():
    """[DC] NPC White Spirit_Gesture Management_Queen Knight B"""
    """State 0,2: [Lib] [DC] [Preset] NPC White Spirit_Gesture Management_SubState"""
    assert event_m20_24_x93(z58=224000081, z59=800, z60=224020083)
    """State 1: Finish"""
    EndMachine()

