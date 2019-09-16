# -*- coding: utf-8 -*-
def talk_m10_04_7000():
    """Dragon Lady (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103520, z78=104020, z79=104020161)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=70009200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 6: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020162, text25=70009500, text26=70009500, z76=70009500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 7: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_04_x7(text28=70009600, z81=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 9: Dragon Miko: Conversation_SubState"""
            while True:
                call = talk_m10_04_x70()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 10) != 0:
                    """State 10: Waiting for hostility: Dragon Miko _SubState"""
                    Label('L2')
                    call = talk_m10_04_x129()
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 10) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103520, text33=70009100, z85=0, z86=0)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(104020136) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(104020179) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(104020178) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(104020177) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(104020176) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(104020168) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(104020167) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020165) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020164) != 1:
                    Goto('L2')
        """State 8: [Lib] Killing state_SubState"""
        talk_m10_04_x8(text27=70009300, z80=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7040():
    """Ladder shop (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103552, z78=104050, z79=104020081)
        if call.Get() == 1:
            """State 10: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=70409200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020082, text25=70409500, text26=70409500, z76=70409500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 4: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_04_x8(text27=70409300, z80=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 8: Ladder shop: Conversation_SubState"""
            while True:
                call = talk_m10_04_x52()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 9: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=70409400, text30=70409410, text31=70409420, text32=70409400,
                                          z82=104020084, z83=104020085)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 6: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103550, text33=70409100, z85=0, z86=103552)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020085) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020084) != 1:
                    Goto('L2')
        """State 5: [Lib] Death state_SubState"""
        talk_m10_04_x7(text28=70409600, z81=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7410():
    """Blue religious warrior"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103640, z78=104140, z79=104020091)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=74109200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020092, text25=74109500, text26=74109500, z76=74109500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 8: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_04_x8(text27=74109300, z80=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 9: Seisho Warrior: Conversation_SubState"""
            while True:
                call = talk_m10_04_x54()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=74109400, text30=74109410, text31=74109420, text32=74109400,
                                          z82=104020094, z83=104020095)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_04_x16(z62=103640, text15=74109100, z63=0, val6=4, z64=200903,
                                               z65=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020095) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020094) != 1:
                    Goto('L2')
        """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
        talk_m10_04_x50(text9=74109600, z33=0, val4=4)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7510():
    """Map writing (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 8: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103682, z78=104180, z79=104020101)
        if call.Get() == 1:
            """State 3: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=75109200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020102, text25=75109500, text26=75109500, z76=75109500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 4: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_04_x8(text27=75109300, z80=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Map writing: Conversation_SubState"""
            while True:
                call = talk_m10_04_x104()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=75109400, text30=75109410, text31=75109420, text32=75109400,
                                          z82=104020104, z83=104020105)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103680, text33=75109100, z85=0, z86=103682)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020105) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020104) != 1:
                    Goto('L2')
        """State 5: [Lib] Death state_SubState"""
        talk_m10_04_x7(text28=75109600, z81=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7540():
    """Yorozu Baba (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 9: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103712, z78=104210, z79=104020171)
        if call.Get() == 1:
            """State 3: [Lib] Reunion hostility_SubState"""
            # talk:75409200:"I'll have your guts for garters! "
            call = talk_m10_04_x3(text14=75409200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:75409500:"That's not very nice, is it?"
                call = talk_m10_04_x6(z75=104020172, text25=75409500, text26=75409500, z76=75409500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 4: [Lib] Killing state_SubState"""
                    Label('L1')
                    # talk:75409300:"Cruel, cruel world, this is... Keh heh heh..."
                    talk_m10_04_x8(text27=75409300, z80=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 8: Yorozu Baba: Conversation_SubState"""
            while True:
                call = talk_m10_04_x59()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    # talk:75409400:"Keh heh heh..."
                    call = talk_m10_04_x5(text29=75409400, text30=75409400, text31=75409410, text32=75409410,
                                          z82=104020174, z83=104020175)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 10: [Lib] First adversification_SubState"""
                        # talk:75409100:"You've no respect! Die, you rotten lout!"
                        call = talk_m10_04_x4(z84=103710, text33=75409100, z85=0, z86=103712)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020175) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020174) != 1:
                    Goto('L2')
        """State 5: [Lib] Death state_SubState"""
        # talk:75409600:"..."
        talk_m10_04_x7(text28=75409600, z81=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7610():
    """Armor shop"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 8: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103750, z78=104250, z79=104020111)
        if call.Get() == 1:
            """State 3: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=76109200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020112, text25=76109500, text26=76109500, z76=76109500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 4: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_04_x8(text27=76109300, z80=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Armor shop: Conversation_SubState"""
            while True:
                call = talk_m10_04_x95()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=76109400, text30=76109410, text31=76109400, text32=76109410,
                                          z82=104020114, z83=104020115)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103750, text33=76109100, z85=0, z86=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020115) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020114) != 1:
                    Goto('L2')
        """State 5: [Lib] Death state_SubState"""
        talk_m10_04_x7(text28=76109600, z81=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7620():
    """Material store (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103762, z78=104260, z79=104020121)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=76209200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020122, text25=76209500, text26=76209500, z76=76209500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_04_x7(text28=76209600, z81=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Material shop: Conversation_SubState"""
            while True:
                call = talk_m10_04_x66()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=76209400, text30=76209410, text31=76209420, text32=76209400,
                                          z82=104020124, z83=104020125)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103760, text33=76209100, z85=0, z86=103762)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020125) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020124) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_04_x8(text27=76209300, z80=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7630():
    """Sorcerer (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103772, z78=104270, z79=104020195)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            # talk:76305010:"I won't let you do this..."
            call = talk_m10_04_x3(text14=76305010, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:76305060:"B-but why?"
                call = talk_m10_04_x6(z75=104020196, text25=76305060, text26=76305060, z76=76305060)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    # talk:76305070:"Eeeek!"
                    talk_m10_04_x7(text28=76305070, z81=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Magician: Conversation_SubState"""
            while True:
                call = talk_m10_04_x110()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    # talk:76305030:"Please, stop this!", talk:76305040:"C-calm...calm yourself!", talk:76305050:"Ouch!"
                    call = talk_m10_04_x5(text29=76305030, text30=76305040, text31=76305050, text32=76305050,
                                          z82=104020198, z83=104020199)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        # talk:76305000:"How could you..."
                        call = talk_m10_04_x4(z84=103770, text33=76305000, z85=0, z86=103772)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020199) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020198) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        # talk:76305020:"Goodness, are you alright?"
        talk_m10_04_x8(text27=76305020, z80=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7640():
    """blacksmith"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 8: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103780, z78=104280, z79=104020131)
        if call.Get() == 1:
            """State 3: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=76409200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020132, text25=76409500, text26=76409500, z76=76409500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 4: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_04_x8(text27=76409300, z80=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Blacksmith: Conversation_SubState"""
            while True:
                call = talk_m10_04_x84()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=76409400, text30=76409410, text31=76409400, text32=76409410,
                                          z82=104020134, z83=104020135)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103780, text33=76409100, z85=0, z86=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020135) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020134) != 1:
                    Goto('L2')
        """State 5: [Lib] Death state_SubState"""
        talk_m10_04_x7(text28=76409600, z81=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7660():
    """Magician (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103802, z78=104300, z79=104020141)
        if call.Get() == 1:
            """State 5: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=76609200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020142, text25=76609500, text26=76609500, z76=76609500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 8: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_04_x7(text28=76609600, z81=0)
                    Quit()
            elif KilledPlayer() != 0:
                pass
            elif (HpValue() > 1) != 1:
                Goto('L1')
        elif call.Get() == 0:
            """State 10: Magician: Conversation_SubState"""
            while True:
                call = talk_m10_04_x75()
                if call.Done():
                    Continue('mainloop')
                elif KilledPlayer() != 0:
                    break
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=76609400, text30=76609410, text31=76609400, text32=76609410,
                                          z82=104020144, z83=104020145)
                    if call.Done():
                        pass
                    elif KilledPlayer() != 0:
                        break
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 4: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103800, text33=76609100, z85=0, z86=103802)
                        if call.Done():
                            Goto('L0')
                        elif KilledPlayer() != 0:
                            break
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020145) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020144) != 1:
                    Goto('L2')
        """State 9: [Lib] Killing state_SubState"""
        talk_m10_04_x8(text27=76609300, z80=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7690():
    """Miracle (Madura)"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_04_x9(z77=103822, z78=104320, z79=104020151)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_04_x3(text14=76909200, z59=0, z60=20, z61=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_04_x6(z75=104020152, text25=76909500, text26=76909500, z76=76909500)
                if KilledPlayer() != 0:
                    pass
                elif (HpValue() > 1) != 1:
                    """State 6: [Lib] Death state_SubState"""
                    Label('L1')
                    talk_m10_04_x7(text28=76909600, z81=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                Goto('L1')
            elif KilledPlayer() != 0:
                pass
        elif call.Get() == 0:
            """State 10: Miracle People: Conversation_SubState"""
            while True:
                call = talk_m10_04_x79()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    Goto('L1')
                elif KilledPlayer() != 0:
                    break
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_04_x5(text29=76909400, text30=76909410, text31=76909420, text32=76909400,
                                          z82=104020154, z83=104020155)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        Goto('L1')
                    elif KilledPlayer() != 0:
                        break
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        call = talk_m10_04_x4(z84=103820, text33=76909100, z85=0, z86=103822)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            Goto('L1')
                        elif KilledPlayer() != 0:
                            break
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020155) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020154) != 1:
                    Goto('L2')
        """State 5: [Lib] Killing state_SubState"""
        talk_m10_04_x8(text27=76909300, z80=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7691():
    """Miracle (combat event)"""
    """State 0,1: Conversation: Start"""
    assert (DistanceFromPlayer() > 6) != 1
    """State 3: [Lib] Conversation: Display only _SubState"""
    # talk:76903100:"Curses... Puzzled me out, have you?"
    assert talk_m10_04_x1(text1=76903100, z63=0, z87=30, z88=0)
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7770():
    """Cat"""
    """State 0,1: Conversation: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        assert talk_m10_04_x9(z77=103870, z78=104370, z79=104020181) == 0
        """State 10: Cat: Conversation_SubState"""
        while True:
            call = talk_m10_04_x106()
            if call.Done():
                Continue('mainloop')
            elif KilledPlayer() != 0:
                """State 9: [Lib] Killing state_SubState"""
                Label('L0')
                talk_m10_04_x8(text27=77709300, z80=0)
                Quit()
            elif (HpValue() > 1) != 1:
                """State 8: [Lib] Death state_SubState"""
                Label('L1')
                talk_m10_04_x7(text28=77709600, z81=0)
                Quit()
            elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020185) != 1:
                """State 6: [Lib] Hostile waiting_SubState"""
                Label('L2')
                call = talk_m10_04_x5(text29=77709400, text30=77709410, text31=77709420, text32=77709400,
                                      z82=104020184, z83=104020185)
                if call.Done():
                    pass
                elif KilledPlayer() != 0:
                    Goto('L0')
                elif (HpValue() > 1) != 1:
                    Goto('L1')
            elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020184) != 1:
                Goto('L2')
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_04_7860():
    """Strong man's stele"""
    """State 0,1: Menu: Start"""
    while Loop('mainloop'):
        if IsGuest() != 0:
            break
        elif GetEventFlag(104020097) != 0:
            pass
        """State 3: Menu: Event action: Playback"""
        PlayerActionRequest(9)
        # lot:2009000:Champion's Tablet, goods:50940000:Champion's Tablet
        if (PlayerIsInEventAction(9) != 0 and (GetPlayerCovenant() == 8) != 0 and GetEventFlag(103100)
            != 1 and CanGetItemLot(2009000, 1) != 1 and (ItemCount(50940000, 1, 1, 1) > 1) != 1):
            """State 10: Menu: Pledge transfer items not available: Insurance_SubState"""
            Label('L0')
            # lot:2009000:Champion's Tablet
            assert talk_m10_04_x22(lot3=2009000, z10=103100)
        # goods:50940000:Champion's Tablet
        elif (PlayerIsInEventAction(9) != 0 and (GetPlayerCovenant() == 8) != 0 and GetEventFlag(103100)
              != 1 and (ItemCount(50940000, 1, 1, 1) > 1) != 1):
            Goto('L0')
        elif PlayerIsInEventAction(9) != 0:
            pass
        """State 7: [Lib] Menu start: General purpose_SubState"""
        while True:
            call = talk_m10_04_x13(z70=0, z71=-1, z72=78601000, z73=0)
            if call.Get() == 0:
                break
            elif call.Get() == 1:
                break
            elif call.Get() == 6:
                """State 11: Menu item: Make a pledge: Strong stone monument_SubState"""
                # lot:2009000:Champion's Tablet, action:1337:"Join the Company of Champions covenant?", action:1347:"Abandon your covenant and\njoin the Company of Champions?"
                assert (talk_m10_04_x127(val1=8, z1=-9999, lot1=2009000, z2=103100, action1=1337, action2=1347,
                        z3=104020031))
            elif call.Get() == 4:
                """State 9: [Lib] Menu item: Dedication: OBJ: Strong man's stone monument_SubState"""
                # goods:62150000:Awestone
                call = talk_m10_04_x46(goods2=62150000, z35=61, z36=217, z37=-9999, val5=8, z38=0, z39=0,
                                       z40=103112)
                if call.Get() == 1:
                    """State 8: [Lib] Menu item: Dedicated: OBJ: Pledge item award_SubState"""
                    # lot:2009011:Great Magic Weapon, lot:2009012:First Dragon Ring, lot:2009013:Vanquisher's Seal
                    assert (talk_m10_04_x40(z11=61, z12=217, lot4=2009011, lot5=2009012, lot6=2009013,
                            z13=103110, z14=103111, z15=103112))
                elif call.Get() == 0:
                    pass
        """State 4: Menu: Event action: End"""
        while True:
            EndPlayerActionRequest()
            if (GetStateTime() > GetRandomValueForStateTime(1, 1)) != 0:
                """State 6: Menu: Event Action: Insurance"""
                pass
            elif PlayerIsInEventAction(9) != 1:
                """State 2: Menu: Exit"""
                SetEventFlag(104020097, 0)
                ClearNpcMenuResults()
                CloseNpcMenu()
                assert (GetEventFlag(104020097) != 1 and (GetStateTime() > GetRandomValueForStateTime(0.1,
                        0.1)) != 0)
                Continue('mainloop')
    """State 5: Menu: System: Exit"""
    EndMachine()

def talk_m10_04_x0(text16=_, z89=_, z90=0):
    """[Lib] Conversation: General purpose
    text16: Conversation ID
    z89: Conversation flag
    z90: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text16, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z89, 1)
    SetEventFlag(z90, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_04_x1(text1=_, z63=_, z87=_, z88=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z63: Conversation flag
    z87: Display distance
    z88: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z87)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z63, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_04_x2(text9=_, z33=0):
    """[Lib] Conversation: Event end
    text9: Conversation ID
    z33: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z33, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_04_x3(text14=_, z59=0, z60=20, z61=80):
    """[Lib] Reunion hostility
    text14: Conversation message ID
    z59: Conversation flag ID
    z60: Display distance
    z61: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_04_x30(text14=text14, z59=z59, z60=z60, z61=z61)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_04_x4(z84=_, text33=_, z85=0, z86=_):
    """[Lib] First hostility
    z84: Hostile: Global event flag
    text33: Conversation ID
    z85: Conversation flag
    z86: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z84, 1)
    SetEventFlag(z86, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z84) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_04_x1(text1=text33, z63=z85, z87=-1, z88=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_04_x5(text29=_, text30=_, text31=_, text32=_, z82=_, z83=_):
    """[Lib] Hostile waiting
    text29: Conversation ID: 1 attacked
    text30: Conversation ID: Attacked 2
    text31: Conversation ID: 3 attacked
    text32: Conversation ID: 4 attacked
    z82: No use: Area and other flags
    z83: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z83) != 1, z83, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z82) != 1, z82, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_04_x1(text1=text32, z63=0, z87=-1, z88=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_04_x1(text1=text31, z63=0, z87=-1, z88=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_04_x1(text1=text30, z63=0, z87=-1, z88=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_04_x1(text1=text29, z63=0, z87=-1, z88=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_04_x6(z75=_, text25=_, text26=_, z76=_):
    """[Lib] Hostile state
    z75: Area and other flags: HP decreased
    text25: Conversation ID: HP drop 1
    text26: Conversation ID: HP drop 2
    z76: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    """State 2: Hostile state: standby"""
    while True:
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z75) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_04_x10(text25=text25, z75=z75)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_04_x10(text25=text26, z75=z75)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_04_x10(text25=text26, z75=z75)

def talk_m10_04_x7(text28=_, z81=0):
    """[Lib] Death status
    text28: Conversation ID
    z81: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_04_x2(text9=text28, z33=z81)

def talk_m10_04_x8(text27=_, z80=0):
    """[Lib] Murder status
    text27: Conversation ID
    z80: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_04_x2(text9=text27, z33=z80)

def talk_m10_04_x9(z77=_, z78=_, z79=_):
    """[Lib] Event: Branch
    z77: Hostile flag
    z78: death flag
    z79: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z78) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z79) != 0
    elif GetEventFlag(z77) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_04_x10(text25=_, z75=_):
    """[Lib] Conversation: HP drop
    text25: Conversation ID
    z75: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text25, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z75, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_04_x11(z74=_, text21=_, text22=_, text23=_, text24=_):
    """[Lib] Conversation: Greeting: General
    z74: Area other flag: Contact flag
    text21: Text ID: Talk to_continuous 1
    text22: Text ID: Talk to_continuous 2
    text23: Text ID: Talk to _After a long time 1
    text24: Text ID: Talk to _After a long time 2
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    """State 2: Continuous or long time: Branch"""
    if GetEventFlag(z74) != 0:
        """State 3: Continuous: Branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 6: Talk to _continuous 1_SubState"""
            assert talk_m10_04_x0(text16=text21, z89=0, z90=0)
        else:
            """State 7: Talk to _continuous 2_SubState"""
            assert talk_m10_04_x0(text16=text22, z89=0, z90=0)
    else:
        """State 4: Long time no see: branch"""
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 8: Talk to me after a long time 1_SubState"""
            assert talk_m10_04_x0(text16=text23, z89=0, z90=0)
        else:
            """State 9: Talk to _After a long time 2_SubState"""
            assert talk_m10_04_x0(text16=text24, z89=0, z90=0)
        """State 5: Long time no see: contact flag set"""
        SetEventFlag(z74, 1)
    """State 10: End state"""
    return 0

def talk_m10_04_x12(action1=_):
    """[Lib] selection dialog
    action1: Dialog: Text ID
    """
    """State 0,1: Selection dialog: Display"""
    DisplayOwnYesNoMenu(action1, 0, -1, 0, 0, 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO"""
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        """State 5: End state: Cancel"""
        Label('L0')
        return 2
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_04_x13(z70=0, z71=_, z72=_, z73=_):
    """[Lib] Menu start: General purpose
    z70: Camera parameter ID
    z71: Target Damipoly ID
    z72: NPC event parameter ID
    z73: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z73, z70, z71, z72)
    """State 3: Menu start: Standby"""
    if (NpcMenuResult() == 19) != 0:
        """State 6: Cancel: End state"""
        return 0
    elif (NpcMenuResult() == 18) != 0:
        """State 7: Normal: End state"""
        Label('L0')
        return 1
    elif (NpcMenuResult() == 17) != 0:
        Goto('L0')
    elif (NpcMenuResult() == 16) != 0:
        """State 8: Conversation: end state"""
        return 2
    elif (NpcMenuResult() == 5) != 0:
        """State 12: Pledge: End state"""
        return 6
    elif (NpcMenuResult() == 9) != 0:
        """State 13: Immunity: End State"""
        return 7
    elif (NpcMenuResult() == 10) != 0:
        """State 9: Pledge Discard: End State"""
        return 3
    elif (NpcMenuResult() == 6) != 0:
        """State 10: Votive: End State"""
        return 4
    elif (NpcMenuResult() == 12) != 0:
        """State 11: Ladder: End state"""
        return 5
    elif (NpcMenuResult() == 13) != 0:
        """State 15: Route switching: End state"""
        return 9
    elif (NpcMenuResult() == 14) != 0:
        """State 14: Pass XX: End state"""
        return 8
    elif (NpcMenuResult() == 11) != 0:
        """State 16: Gesture: End state"""
        return 10
    elif (NpcMenuResult() == 1) != 0:
        """State 17: Point reassignment: end state"""
        return 11
    elif (NpcMenuResult() == 20) != 0:
        """State 18: Est bottle enhancement: end state"""
        return 12
    elif (NpcMenuResult() == 21) != 0:
        """State 19: Level up: End state"""
        return 13

def talk_m10_04_x14(text19=_, text20=_):
    """[Lib] Menu exit: General purpose
    text19: Conversation ID (at the time of purchase)
    text20: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_04_x1(text1=text19, z63=0, z87=-1, z88=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_04_x1(text1=text20, z63=0, z87=-1, z88=0)
    """State 4: End state"""
    return 0

def talk_m10_04_x15(text18=_):
    """[Lib] Menu cancellation: General purpose
    text18: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_04_x1(text1=text18, z63=0, z87=-1, z88=0)
    """State 4: End state"""
    return 0

def talk_m10_04_x16(z62=103640, text15=74109100, z63=0, val6=4, z64=200903, z65=0):
    """[Lib] First hostility _ (pledge cancellation)
    z62: Hostile: Global event flag
    text15: Conversation ID
    z63: Conversation flag
    val6: Cancellation pledge name
    z64: Pledge cancellation: Global conversation flag
    z65: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z62, 1)
    SetEventFlag(z65, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z62) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_04_x29(val1=val6)
    if call.Done() and (GetPlayerCovenant() == val6) != 0:
        """State 3: First hostility: pledge change"""
        ChangePlayerCovenantIf((GetPlayerCovenant() == val6) != 0, 0)
        assert (GetStateTime() >= 0) != 0
        """State 2: First hostility: save execution"""
        SaveExecution()
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 4: Conversation: First hostilization_SubState"""
    assert talk_m10_04_x1(text1=text15, z63=z63, z87=-1, z88=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_04_x17(text8=74100610, z28=0, lot11=_, z29=_, z30=213, z31=59):
    """[Lib] Conversation: Pledge ranking
    text8: Ranking: Conversation ID
    z28: Ranking: Conversation flag
    lot11: Item lottery
    z29: Ranking transfer: Global event flag
    z30: Previous rank: Global variable
    z31: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_04_x19(action8=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # talk:74100610:"But I've never been out that way.\n...It's far too perilous."
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z28, 1)
    if CanGetItemLot(lot11, 1) != 1 and GetEventFlag(z29) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_04_x51(z32=1011, lot1=lot11)
    elif GetEventFlag(z29) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_04_x22(lot3=lot11, z10=z29)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z30, GetAreaVariable(z31))
    """State 11: End state"""
    return 0

def talk_m10_04_x18(val3=4, z18=8, lot7=2001000, z19=102381, action3=1333, action4=1343, z20=104020030):
    """[Lib] Menu item: Make a pledge
    val3: Pledge name
    z18: Event action
    lot7: Item lottery ID
    z19: Item transfer: Global event flag
    action3: Pledge text
    action4: Overwriting pledge text
    z20: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val3) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_04_x19(action8=1305)
    else:
        """State 4: [Lib] Pledge conclusion: General purpose_SubState"""
        call = talk_m10_04_x35(val3=val3, z18=z18, lot7=lot7, z19=z19, action3=action3, action4=action4,
                               z20=z20)
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_04_x19(action8=_):
    """[Lib] OK dialog
    action8: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action8, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x20(z69=8):
    """[Lib] Event action: General purpose
    z69: Event action
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z69)
    assert PlayerIsInEventAction(z69) != 0
    """State 3: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z69) != 1
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z69) != 1
    """State 5: End state"""
    return 0

def talk_m10_04_x21(lot10=1741000, z27=102380, text6=74106000, text7=74106020):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot10: Item lottery ID
    z27: Global event flag
    text6: First half: Conversation ID
    text7: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_04_x1(text1=text6, z63=0, z87=-1, z88=0)
    # lot:1741000:Ring of Steel Protection
    if call.Done() and CanGetItemLot(lot10, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_04_x51(z32=1011, lot1=lot10)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_04_x22(lot3=lot10, z10=z27)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_04_x1(text1=text7, z63=0, z87=-1, z88=0)
    """State 6: End state"""
    return 0

def talk_m10_04_x22(lot3=_, z10=_):
    """[Lib] Item acquisition dialog
    lot3: Item lottery ID
    z10: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z10, 1)
    AwardItem(lot3, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x23(z68=104020113, text16=_, text17=_):
    """[Lib] Conversation: Greeting: Single
    z68: Area other flag: Contact flag
    text16: Text ID: Talk to_continuous
    text17: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(z68) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m10_04_x0(text16=text16, z89=0, z90=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m10_04_x0(text16=text17, z89=0, z90=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(z68, 1)
    """State 5: End state"""
    return 0

def talk_m10_04_x24(lot2=_, z7=_, z8=_, z9=_, z66=0, z67=0):
    """[Lib] Item acquisition dialog: Conversation
    lot2: Item lottery ID
    z7: Item transfer: Global event flag
    z8: Conversation: Global conversation flag
    z9: Trophy acquisition: Area and other flags
    z66: Emigration permission: Global event flag
    z67: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z67, 1)
    SetEventFlag(z66, 1)
    SetEventFlag(z9, 1)
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    AwardItem(lot2, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x25(lot9=_, z24=_, text4=_, text5=_, z25=_, z26=_):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot9: Item lottery ID
    z24: Item transfer: Global event flag
    text4: First half: Conversation ID
    text5: Second half: Conversation ID
    z25: Conversation: Global conversation flag
    z26: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_04_x1(text1=text4, z63=0, z87=-1, z88=0)
    if call.Done() and GetEventFlag(z24) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z25, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_04_x1(text1=text5, z63=0, z87=-1, z88=0)
    elif call.Done() and CanGetItemLot(lot9, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_04_x51(z32=1011, lot1=lot9)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_04_x24(lot2=lot9, z7=z24, z8=z25, z9=z26, z66=0, z67=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_04_x26(lot8=_, z21=_, text3=_, z22=_, z23=_):
    """[Lib] Conversation: Item transfer: Mes⇒Item
    lot8: Item lottery ID
    z21: Item transfer: Global event flag
    text3: Conversation ID
    z22: Conversation: Global conversation flag
    z23: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: Conversation_SubState"""
    call = talk_m10_04_x1(text1=text3, z63=0, z87=-1, z88=0)
    if call.Done() and GetEventFlag(z21) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z22, 1)
    elif call.Done() and CanGetItemLot(lot8, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_04_x51(z32=1011, lot1=lot8)
    elif call.Done():
        """State 4: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_04_x24(lot2=lot8, z7=z21, z8=z22, z9=z23, z66=0, z67=0)
    """State 6: End state"""
    return 0

def talk_m10_04_x27():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m10_04_x28():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x29(val1=_):
    """[Lib] Pledge cancellation: Overwrite
    val1: Main pledge: pledge type
    """
    """State 0,1: Overwrite: Start"""
    if (not GetPlayerCovenant()) != 0:
        pass
    elif (GetPlayerCovenant() == val1) != 1:
        pass
    else:
        """State 2: Overwrite: Release flag"""
        SetEventFlagIf((GetPlayerCovenant() == 1) != 0, 200900, 1)
        SetEventFlagIf((GetPlayerCovenant() == 2) != 0, 200901, 1)
        SetEventFlagIf((GetPlayerCovenant() == 3) != 0, 200902, 1)
        SetEventFlagIf((GetPlayerCovenant() == 4) != 0, 200903, 1)
        SetEventFlagIf((GetPlayerCovenant() == 5) != 0, 200904, 1)
        SetEventFlagIf((GetPlayerCovenant() == 6) != 0, 200905, 1)
        SetEventFlagIf((GetPlayerCovenant() == 7) != 0, 200906, 1)
        SetEventFlagIf((GetPlayerCovenant() == 8) != 0, 200907, 1)
        SetEventFlagIf((GetPlayerCovenant() == 9) != 0, 200908, 1)
    """State 3: End state"""
    return 0

def talk_m10_04_x30(text14=_, z59=0, z60=20, z61=80):
    """[Lib] Conversation: Hostile display only
    text14: Conversation ID
    z59: Conversation flag
    z60: Display distance
    z61: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text14, GetCommonEventParamDecimal(7), z60)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z59, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_04_x31(action7=_, goods2=_):
    """[Lib] Selection dialog: Item display
    action7: Dialog: Text ID
    goods2: Item name: Event item
    """
    """State 0,1: Selection dialog: Display"""
    DisplayOwnYesNoMenu(action7, 0, -1, 2, goods2, 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO"""
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        """State 5: End state: Cancel"""
        Label('L0')
        return 2
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_04_x32(action6=1206, goods3=60525000):
    """[Lib] OK dialog: Item display
    action6: Text ID
    goods3: Item name: Event item
    """
    """State 0,1: OK dialog: Display"""
    # action:1206:"You do not have\n%s", goods:60525000:Estus Flask Shard
    DisplayOwnOkMenu(action6, 0, 0, -1, 2, goods3, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x33(z43=_, z44=0):
    """[Lib] Menu item: Gesture
    z43: Gesture: Item ID
    z44: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_04_x44(z43=z43, z44=z44)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_04_x34(action5=1203, val2=2000):
    """[Lib] selection dialog: Soul amount
    action5: Dialog: Text ID
    val2: Soul Amount: Argument
    """
    """State 0,1: Selection dialog: Display"""
    # action:1203:"Pay souls?\nSouls needed: %d"
    DisplayOwnYesNoMenu(action5, 0, -1, 1, val2, 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO"""
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        """State 5: End state: Cancel"""
        Label('L0')
        return 2
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_04_x35(val3=4, z18=8, lot7=2001000, z19=102381, action3=1333, action4=1343, z20=104020030):
    """[Lib] Pledge conclusion: General purpose
    val3: Pledge type
    z18: Event action
    lot7: Item lottery ID
    z19: Item transfer: Global event flag
    action3: Pledge text
    action4: Overwriting pledge text
    z20: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z20, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_04_x12(action1=action3)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_04_x19(action8=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_04_x36(z18=z18, val3=val3, lot7=lot7, z19=z19) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_04_x19(action8=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_04_x12(action1=action4)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_04_x29(val1=val3)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_04_x36(z18=8, val3=4, lot7=2001000, z19=102381):
    """[Lib] Event action: Pledge
    z18: Event action
    val3: Pledge type
    lot7: Item lottery ID
    z19: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z18)
    assert PlayerIsInEventAction(z18) != 0
    """State 3: IventAction: Motion_Waiting"""
    # lot:2001000:Blue Seal
    if PlayerIsInEventAction(z18) != 1 and CanGetItemLot(lot7, 1) != 1 and GetEventFlag(z19) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val3)
        # lot:2001000:Blue Seal
        if (GetPlayerCovenant() == val3) != 0 and CanGetItemLot(lot7, 1) != 1 and GetEventFlag(z19) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_04_x51(z32=1011, lot1=lot7)
        elif (GetPlayerCovenant() == val3) != 0:
            pass
    elif PlayerIsInEventAction(z18) != 1 and GetEventFlag(z19) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z18) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val3)
        SetEventFlag(z19, 1)
        # lot:2001000:Blue Seal
        AwardItem(lot7, 1)
        assert (GetPlayerCovenant() == val3) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z18) != 1
    """State 8: End state"""
    return 0

def talk_m10_04_x37(z17=-9999, val1=8, lot1=2009000, z2=103100):
    """[Lib] Event action: Pledge: OBJ
    z17: Event action
    val1: Pledge type
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z17)
    """State 2: IventAction: Motion_Waiting"""
    # lot:2009000:Champion's Tablet
    if (GetEventFlag(z2) != 1 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0 and CanGetItemLot(lot1,
        1) != 1):
        """State 5: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        # lot:2009000:Champion's Tablet
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot1, 1) != 1 and GetEventFlag(z2) != 1:
            """State 6: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_04_x51(z32=1011, lot1=lot1)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif GetEventFlag(z2) != 0 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        Goto('L0')
    elif (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 4: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z2, 1)
        # lot:2009000:Champion's Tablet
        AwardItem(lot1, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 3,7: End state"""
    return 0

def talk_m10_04_x38(val1=8, z16=9, lot1=2009000, z2=103100, action1=1337, action2=1347, z3=104020031):
    """[Lib] Pledge conclusion: OBJ
    val1: Pledge type
    z16: Event action
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z3, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_04_x12(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_04_x19(action8=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge: OBJ_SubState"""
            Label('L1')
            assert talk_m10_04_x37(z17=-9999, val1=val1, lot1=lot1, z2=z2) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_04_x19(action8=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_04_x12(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_04_x29(val1=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_04_x39(z53=4, z54=59, z55=213, z56=102390, z57=102391, z58=102392):
    """[Lib] Pledge: Rank up: Conversation: 1
    z53: Pledge: Pledge type
    z54: Current rank: Area variable
    z55: Previous rank: Global variable
    z56: Ranking 1: Item transfer: Global event flag
    z57: Ranking 2: Item transfer: Global event flag
    z58: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z54, GetPlayerCovenantLevel(z53))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z55) > GetAreaVariable(z54)) != 1 and (GetGlobalVariable(z55) == GetAreaVariable(z54))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z55) > GetAreaVariable(z54)) != 0 and (GetGlobalVariable(z55) == GetAreaVariable(z54))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z55, GetAreaVariable(z54))
    elif GetEventFlag(z56) != 1 and (GetGlobalVariable(z55) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(z57) != 1 and (GetGlobalVariable(z55) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(z58) != 1 and (GetGlobalVariable(z55) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_04_x40(z11=61, z12=217, lot4=2009011, lot5=2009012, lot6=2009013, z13=103110, z14=103111,
                    z15=103112):
    """[Lib] Menu item: Dedicated: OBJ: Pledge item award
    z11: Current pledge rank: Area variable
    z12: Last pledge rank: global variable
    lot4: Ranking 1: Item lottery
    lot5: Ranking 2: Item lottery
    lot6: Ranking 3: Item lottery
    z13: Ranking 1: Global event flag
    z14: Ranking 2: Global event flag
    z15: Ranking 3: Global event flag
    """
    """State 0,3: Dedication: rank up judgment"""
    if (GetGlobalVariable(z12) > GetAreaVariable(z11)) != 1:
        """State 8: Pledge Rank Up Confirmation Dialog_SubState"""
        Label('L0')
        # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
        assert talk_m10_04_x19(action8=1308)
        """State 2: Pledge ranking judgment"""
        # lot:2009011:Great Magic Weapon
        if (GetAreaVariable(z11) > 1) != 0 and GetEventFlag(z13) != 1 and CanGetItemLot(lot4, 1) != 1:
            """State 9: [Lib] Inventory full dialog (ranking 1) _SubState"""
            assert talk_m10_04_x51(z32=1011, lot1=lot4)
        elif (GetAreaVariable(z11) > 1) != 0 and GetEventFlag(z13) != 1:
            """State 5: Pledge ranking 1 item acquisition dialog_SubState"""
            assert talk_m10_04_x22(lot3=lot4, z10=z13)
            """State 1: Pledge ranking: area variable ⇒ global variable"""
            Label('L1')
            SetGlobalVariable(z12, GetAreaVariable(z11))
        # lot:2009012:First Dragon Ring
        elif (GetAreaVariable(z11) > 2) != 0 and GetEventFlag(z14) != 1 and CanGetItemLot(lot5, 1) != 1:
            """State 10: [Lib] Inventory full dialog (ranking 2) _SubState"""
            assert talk_m10_04_x51(z32=1011, lot1=lot5)
        elif (GetAreaVariable(z11) > 2) != 0 and GetEventFlag(z14) != 1:
            """State 6: Pledge ranking 2 item acquisition dialog_SubState"""
            assert talk_m10_04_x22(lot3=lot5, z10=z14)
            Goto('L1')
        # lot:2009013:Vanquisher's Seal
        elif (GetAreaVariable(z11) > 3) != 0 and GetEventFlag(z15) != 1 and CanGetItemLot(lot6, 1) != 1:
            """State 11: [Lib] Inventory full dialog (ranking 3) _SubState"""
            assert talk_m10_04_x51(z32=1011, lot1=lot6)
        elif (GetAreaVariable(z11) > 3) != 0 and GetEventFlag(z15) != 1:
            """State 7: Pledge ranking 3 item acquisition dialog_SubState"""
            assert talk_m10_04_x22(lot3=lot6, z10=z15)
            Goto('L1')
        else:
            Goto('L1')
    elif (GetGlobalVariable(z12) > 1) != 0 and GetEventFlag(z13) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z12) > 2) != 0 and GetEventFlag(z14) != 1:
        Goto('L0')
    elif (GetGlobalVariable(z12) > 3) != 0 and GetEventFlag(z15) != 1:
        Goto('L0')
    else:
        Goto('L1')
    """State 4: Pledge Ranking: End"""
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_04_x41(text13=_, z49=_, z50=104020149, z51=104010159, z52=104010166):
    """[Lib] Conversation: Canceling startup state
    text13: Conversation ID
    z49: Conversation flag
    z50: Activation state release: Area and other flags
    z51: Rock sitting 1: Poke your cheek with your hand
    z52: Extend both hands back
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 10: Conversation: Cancel start state: Branch"""
    if GetEventFlag(z50) != 0:
        """State 8: Conversation: Activation state release: Second time"""
        Label('L0')
        DeleteKeyGuideArea()
        SetEventFlag(z50, 1)
    elif GetEventFlag(z51) != 1 and GetEventFlag(z52) != 1:
        Goto('L0')
    else:
        """State 7: Conversation: Activation state release: First use"""
        DeleteKeyGuideArea()
        SetEventFlag(z50, 1)
        assert GetEventFlag(z50) != 0
        """State 9: Conversation: Release hood: Wait"""
        KeyGuideTemporarilyInvalidIf(GetEventFlag(z51) != 0, 3.5)
        KeyGuideTemporarilyInvalidIf(GetEventFlag(z52) != 0, 3.5)
        assert (GetStateTime() > GetRandomValueForStateTime(3, 3)) != 0
    """State 4: Conversation: Message"""
    StartConversation(text13, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z49, 1)
    """State 11: Conversation: End"""
    return 0

def talk_m10_04_x42(text12=_, z46=_, z47=10049030, z48=5):
    """[Lib] Conversation: For unique key guide
    text12: Conversation ID
    z46: Conversation flag
    z47: Key guide parameters
    z48: Cancel distance
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, z47)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text12, GetCommonEventParamDecimal(7), z48)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z46, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_04_x43(z45=15):
    """[Lib] Event action: Est bottle strengthening
    z45: Event action
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z45)
    assert PlayerIsInEventAction(z45) != 0
    """State 3: IventAction: Motion_Waiting"""
    assert PlayerIsInEventAction(z45) != 1
    """State 5: Event action: Est bottle strengthening"""
    # goods:60525000:Estus Flask Shard
    ConsumeItem(60525000, 1)
    StrengthenEstus()
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z45) != 1
    """State 6: End state"""
    return 0

def talk_m10_04_x44(z43=_, z44=0):
    """[Lib] Get gesture dialog
    z43: Item ID
    z44: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(z43, 0, -1)
    SetEventFlag(z44, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x45(z41=-9999, goods2=62150000, z35=61, val5=8, z42=0, z40=103112):
    """[Lib] Event action: Dedication: OBJ: Strong man's monument
    z41: Event action
    goods2: Special Offer: Event Item
    z35: Current pledge level: area variable
    val5: Pledge type
    z42: Transfer: Item lottery
    z40: Transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z41)
    assert PlayerIsInEventAction(z41) != 0
    """State 2: IventAction: Motion_Waiting"""
    if GetEventFlag(103112) != 0 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 5: Event action: votive delivery"""
        AddAwestoneRankingCount(1)
        # goods:62150000:Awestone
        ConsumeItem(goods2, 1)
        SetAreaVariable(z35, GetPlayerCovenantLevel(val5))
        SaveExecution()
    elif (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 6: Event action: Votive delivery: Item transfer"""
        AddAwestoneRankingCount(1)
        # goods:62150000:Awestone
        ConsumeItem(goods2, 1)
        AddPlayerCovenantContribution(val5, 1)
        SetAreaVariable(z35, GetPlayerCovenantLevel(val5))
        SaveExecution()
    """State 4,7: End state"""
    return 0

def talk_m10_04_x46(goods2=62150000, z35=61, z36=217, z37=-9999, val5=8, z38=0, z39=0, z40=103112):
    """[Lib] Menu item: Dedicated: OBJ: Strong man's monument
    goods2: Dedication item ID
    z35: Current pledge rank: Area variable
    z36: Last pledge rank: global variable
    z37: Event action
    val5: Pledge type
    z38: Transfer: Item lottery
    z39: Transfer: Global event flag
    z40: Ranking 3 items: Global event flag
    """
    """State 0,1: Votive: Start"""
    if (GetPlayerCovenant() == val5) != 1:
        """State 7: Votive: Confirmation dialog not signed"""
        # action:1314:"You must belong to this covenant\nto make an offering"
        assert talk_m10_04_x19(action8=1314)
    else:
        """State 6: Dedication: Dedication selection dialog_SubState"""
        # action:1306:"Offer\n%s?"
        call = talk_m10_04_x31(action7=1306, goods2=goods2)
        # goods:62150000:Awestone
        if call.Get() == 0 and (ItemCount(goods2, 1, 1, 0) > 1) != 1:
            """State 5: Votive: Confirmation of possession of possession _SubState"""
            # action:1310:"You have no offerings"
            assert talk_m10_04_x19(action8=1310)
        elif call.Get() == 0:
            """State 8: [Lib] Event action: Dedication: OBJ: Strong man's monument_SubState"""
            assert talk_m10_04_x45(z41=-9999, goods2=goods2, z35=z35, val5=val5, z42=0, z40=z40)
            """State 3: Delivery confirmation dialog_SubState"""
            # action:1307:"Your devotion to your\ncovenant has deepened"
            assert talk_m10_04_x19(action8=1307)
            """State 10: Rank up: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 2: Votive: Finish"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_04_x47(lot3=2001000, z10=102381):
    """[Lib] Conversation: Item transfer: Item: Key
    lot3: Item lottery
    z10: Item transfer: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # lot:2001000:Blue Seal
    if CanGetItemLot(lot3, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_04_x51(z32=1011, lot1=lot3)
    elif GetEventFlag(z10) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_04_x22(lot3=lot3, z10=z10)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m10_04_x48(text10=_, text11=_, z34=_):
    """[Lib] Menu exit: Purchase flag
    text10: Conversation ID (at the time of purchase)
    text11: Conversation ID (when not purchased)
    z34: Purchase flag: Area other flags
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and GetEventFlag(z34) != 0:
        """State 2: Purchase and leave _SubState"""
        Label('L0')
        assert talk_m10_04_x1(text1=text10, z63=0, z87=-1, z88=0)
    elif NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        Goto('L0')
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_04_x1(text1=text11, z63=0, z87=-1, z88=0)
    """State 4: End state"""
    return 0

def talk_m10_04_x49(lot2=1700000, z7=102090, text1=70000020, text2=70000050, z8=201100, z9=0, goods1=60155000):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Important items
    lot2: Item lottery ID
    z7: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z8: Conversation: Global conversation flag
    z9: Trophy acquisition: Area and other flags
    goods1: Important items
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_04_x1(text1=text1, z63=0, z87=-1, z88=0)
    if call.Done() and GetEventFlag(z7) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        Label('L0')
        SetEventFlag(z8, 1)
    # goods:60155000:Estus Flask
    elif call.Done() and (ItemCount(goods1, 1, 1, 1) > 1) != 0:
        Goto('L0')
    # lot:1700000:Estus Flask
    elif call.Done() and CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_04_x51(z32=1011, lot1=lot2)
        Goto('L0')
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_04_x24(lot2=lot2, z7=z7, z8=z8, z9=z9, z66=0, z67=0)
    """State 4: Item transfer: Second half of conversation _SubState"""
    assert talk_m10_04_x1(text1=text2, z63=0, z87=-1, z88=0)
    """State 7: End state"""
    return 0

def talk_m10_04_x50(text9=74109600, z33=0, val4=4):
    """[Lib] Death status_ (pledge cancellation)
    text9: Conversation ID
    z33: Global: death flag
    val4: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_04_x29(val1=val4)
    if call.Done() and (GetPlayerCovenant() == val4) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_04_x2(text9=text9, z33=z33)

def talk_m10_04_x51(z32=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z32: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_04_x52():
    """Ladder shop: Conversation"""
    """State 0,2: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Ladder shop: First conversation_SubState"""
    assert talk_m10_04_x53()
    """State 4: Ladder shop: NPC menu_SubState"""
    assert talk_m10_04_x63()
    """State 1: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_04_x53():
    """Ladder shop: first conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(201850) != 0:
        """State 4: Talk: Greeting_SubState"""
        # talk:70402200:"Ah! Back already? Ha.", talk:70402300:"All right, what'd you forget this time?\n", talk:70402400:"Hey, what've you been up to!", talk:70402500:"Come to see auld Gilligan, have you?\nHah!"
        assert talk_m10_04_x11(z74=104020083, text21=70402200, text22=70402300, text23=70402400, text24=70402500)
    elif GetEventFlag(201800) != 0:
        """State 5: Talk to: First time: Review_SubState"""
        # talk:70402100:"Wait, you found your way out, too! Hah!"
        assert talk_m10_04_x0(text16=70402100, z89=201850, z90=0)
        """State 2: First conversation: Set contact flag"""
        Label('L0')
        SetEventFlag(104020083, 1)
        SetEventFlag(201800, 1)
        SetEventFlag(201850, 1)
    else:
        """State 3: Talk: First Time: First Look _SubState"""
        # talk:70402000:"What? Who are you?"
        assert talk_m10_04_x0(text16=70402000, z89=201850, z90=0)
        Goto('L0')
    """State 6: End state"""
    return 0

def talk_m10_04_x54():
    """Seisho Warrior: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    if GetEventFlag(203103) != 0:
        """State 3: Seisho Warrior: Greeting Conversation_SubState"""
        call = talk_m10_04_x56()
        if call.Get() == 1:
            pass
        elif call.Get() == 0:
            """State 5: Seishin Warrior: Menu_SubState"""
            assert talk_m10_04_x57()
    else:
        """State 4: Seisho Warrior: First conversation_SubState"""
        assert talk_m10_04_x55()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_04_x55():
    """Seisho Warrior: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(203102) != 0:
        """State 6: First look: Speak: Pledge contract: First time _SubState"""
        # talk:74100300:"Do you see the way beyond the bonfire?\nThat will take you to the Forest of the Giants."
        call = talk_m10_04_x0(text16=74100300, z89=203103, z90=0)
        if call.Done() and (GetPlayerCovenant() == 4) != 0:
            """State 10: Confirm oath conclusion confirmation dialog_SubState"""
            # action:1305:"You already belong\nto this covenant"
            assert talk_m10_04_x19(action8=1305)
        elif call.Done():
            """State 9: [Lib] Pledge conclusion: General purpose_SubState"""
            # lot:2001000:Blue Seal, action:1333:"Join the Way of Blue covenant?", action:1343:"Abandon your covenant and\njoin the Way of Blue?"
            call = talk_m10_04_x35(val3=4, z18=8, lot7=2001000, z19=102381, action3=1333, action4=1343,
                                   z20=104020030)
            if call.Get() == 0:
                """State 8: First look: Talk: Pledge contract: YES / NO dialog: NO_SubState"""
                # talk:74100500:"Have you seen that pit?\nThat gaping hole in the earth."
                assert talk_m10_04_x1(text1=74100500, z63=0, z87=-1, z88=0)
            elif call.Get() == 1:
                """State 7: First look: Talk: Pledge contract: YES / NO dialog: YES_SubState"""
                # talk:74100400:"Heide's Tower of Flame lies beyond the far gate."
                assert talk_m10_04_x1(text1=74100400, z63=0, z87=-1, z88=0)
    elif GetEventFlag(203101) != 0:
        """State 5: First look: Talk to _part3_SubState"""
        # talk:74100200:"There are four beings in this land with giant souls."
        assert talk_m10_04_x0(text16=74100200, z89=203102, z90=0)
    elif GetEventFlag(203112) != 0:
        """State 4: First look: Talk to _Part 2_SubState"""
        # talk:74100100:"Do you know much about souls?"
        assert talk_m10_04_x0(text16=74100100, z89=203101, z90=0)
    elif GetEventFlag(203100) != 0:
        """State 11: First look: Talk to that 1.5_SubState"""
        # talk:74100050:"I am Saulden.\nAnd like you...I lost everything, and now I'm here."
        assert talk_m10_04_x0(text16=74100050, z89=203112, z90=0)
    else:
        """State 3: First look: Talk to _part 1_SubState"""
        # talk:74100000:"You're Undead...aren't you."
        assert talk_m10_04_x0(text16=74100000, z89=203100, z90=0)
    """State 2: First conversation: End"""
    SetEventFlag(104020093, 1)
    """State 12: End state"""
    return 0

def talk_m10_04_x56():
    """Seishin warrior: greeting conversation"""
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 300)
    if (GetPlayerCovenant() == 4) != 1:
        """State 9: Seisho Warrior: Emigration Count _SubState"""
        Label('L0')
        assert talk_m10_04_x126()
        """State 2: Greeting: Branch"""
        if GetEventFlag(203117) != 1 and (GetAreaVariable(58) > 9) != 0:
            """State 15: Migrant increase message: 3_SubState"""
            # talk:74108200:"Quite a hive of activity we are, these days."
            call = talk_m10_04_x1(text1=74108200, z63=203117, z87=-1, z88=0)
            # lot:1741010:Soul Vessel
            if call.Done() and CanGetItemLot(1741010, 1) != 1:
                """State 17: Inventory full confirmation dialog_SubState"""
                # action:1011:"Your inventory bag is full"
                assert talk_m10_04_x19(action8=1011)
            elif call.Done() and GetEventFlag(102382) != 1:
                """State 16: [Lib] Item acquisition dialog_SubState"""
                # lot:1741010:Soul Vessel
                assert talk_m10_04_x22(lot3=1741010, z10=102382)
            elif call.Done():
                pass
        elif GetEventFlag(203116) != 1 and (GetAreaVariable(58) > 5) != 0:
            """State 14: Migrant increase message: 2_SubState"""
            # talk:74108100:"Look at our new neighbours..."
            assert talk_m10_04_x1(text1=74108100, z63=203116, z87=-1, z88=0)
        elif GetEventFlag(203115) != 1:
            """State 13: Migrant increase message: 1_SubState"""
            # talk:74108000:"Do you feel lonely here?"
            assert talk_m10_04_x1(text1=74108000, z63=203115, z87=-1, z88=0)
        elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 100) != 0:
            """State 10: Review: Talk (Random) 1_SubState"""
            # talk:74100600:"There lies a forest beyond the hills."
            assert talk_m10_04_x1(text1=74100600, z63=0, z87=-1, z88=0)
        elif (GetRandomValue(0) > 0 and GetRandomValue(0) < 200) != 0:
            """State 11: Review: Talk to (random) 2_SubState"""
            # talk:74100610:"But I've never been out that way.\n...It's far too perilous."
            assert talk_m10_04_x1(text1=74100610, z63=0, z87=-1, z88=0)
        else:
            """State 12: Review: Talk (random) 3_SubState"""
            # talk:74100620:"I am told the palace lies beyond the forest."
            assert talk_m10_04_x1(text1=74100620, z63=0, z87=-1, z88=0)
    elif (GetPlayerCovenant() == 4) != 0 and GetEventFlag(102381) != 1:
        """State 8: Pledge item transfer not yet available: Insurance_SubState"""
        # lot:2001000:Blue Seal
        call = talk_m10_04_x47(lot3=2001000, z10=102381)
        if call.Done():
            Goto('L0')
        elif (GetPlayerCovenant() == 4) != 1:
            """State 19: Pledge Discard: End State"""
            Label('L1')
            return 1
    elif (GetStateTime() >= 0) != 0:
        """State 4: [Lib] Pledge: Rank up: Conversation_SubState"""
        call = talk_m10_04_x39(z53=4, z54=59, z55=213, z56=102390, z57=102391, z58=102392)
        if call.Get() == 1:
            """State 3: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(59) > 1) != 0 and GetEventFlag(102390) != 1:
                """State 5: Conversation: Pledge Ranking 1_SubState"""
                # talk:74100610:"But I've never been out that way.\n...It's far too perilous.", lot:2001011:Bloodbite Ring
                call = talk_m10_04_x17(text8=74100610, z28=0, lot11=2001011, z29=102390, z30=213, z31=59)
                if call.Done():
                    pass
                elif (GetPlayerCovenant() == 4) != 1:
                    Goto('L1')
            elif (GetAreaVariable(59) > 2) != 0 and GetEventFlag(102391) != 1:
                """State 6: Conversation: Pledge Ranking 2_SubState"""
                # talk:74100610:"But I've never been out that way.\n...It's far too perilous.", lot:2001012:Hush
                call = talk_m10_04_x17(text8=74100610, z28=0, lot11=2001012, z29=102391, z30=213, z31=59)
                if call.Done():
                    pass
                elif (GetPlayerCovenant() == 4) != 1:
                    Goto('L1')
            elif (GetAreaVariable(59) > 3) != 0 and GetEventFlag(102392) != 1:
                """State 7: Conversation: Pledge Ranking 3_SubState"""
                # talk:74100610:"But I've never been out that way.\n...It's far too perilous.", lot:2001013:Blue Tearstone Ring
                call = talk_m10_04_x17(text8=74100610, z28=0, lot11=2001013, z29=102392, z30=213, z31=59)
                if call.Done():
                    pass
                elif (GetPlayerCovenant() == 4) != 1:
                    Goto('L1')
            else:
                Goto('L0')
        elif call.Get() == 0:
            Goto('L0')
    """State 18: Menu: Exit state"""
    return 0

def talk_m10_04_x57():
    """Seishin Warrior: Menu"""
    """State 0,1: Menu: Start"""
    while True:
        # goods:63004000:"Welcome" Gesture
        if (ItemCount(63004000, 1, 1, 0) > 1) != 0:
            """State 7: [Lib] Menu start: No gesture _SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=74100001, z73=0)
            if call.Get() == 2:
                """State 6: Seisho Warrior: Menu Conversation_SubState"""
                Label('L0')
                call = talk_m10_04_x58()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 6:
                """State 3: [Lib] Menu item: _SubState with a pledge"""
                Label('L1')
                # lot:2001000:Blue Seal, action:1333:"Join the Way of Blue covenant?", action:1343:"Abandon your covenant and\njoin the Way of Blue?"
                call = talk_m10_04_x18(val3=4, z18=8, lot7=2001000, z19=102381, action3=1333, action4=1343,
                                       z20=104020030)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 4: [Lib] Exit menu: General purpose_SubState"""
                Label('L2')
                # talk:74100800:"The flame you see there is a bonfire."
                assert talk_m10_04_x14(text19=74100700, text20=74100800)
        else:
            """State 2: [Lib] Menu start: With gesture_SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=74100000, z73=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 6:
                Goto('L1')
            elif call.Get() == 10:
                """State 8: [Lib] Menu item: Gesture_SubState"""
                call = talk_m10_04_x33(z43=63004000, z44=0)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L2')
        """State 9: End state"""
        Label('L3')
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:74100900:"Long ago, a woman called a Fire Keeper\nwatched over each bonfire."
    assert talk_m10_04_x15(text18=74100900)
    Goto('L3')

def talk_m10_04_x58():
    """Seisho Warrior: Menu conversation"""
    """State 0,1,3: Menu conversation: Branch"""
    while True:
        if (GetEventFlag(102380) != 1 and (GetPlayerDeathCountByPhantomType(0) > 100) != 0 and GetEventFlag(104140)
            != 1):
            break
        elif GetEventFlag(203111) != 0:
            """State 2: Menu conversation: Flag initialization"""
            SetEventFlag(203104, 0)
            SetEventFlag(203105, 0)
            SetEventFlag(203106, 0)
            SetEventFlag(203108, 0)
            SetEventFlag(203109, 0)
            SetEventFlag(203110, 0)
            SetEventFlag(203111, 0)
            continue
        elif GetEventFlag(203110) != 0:
            """State 12: Menu conversation: 8_SubState"""
            assert talk_m10_04_x1(text1=74105700, z63=203111, z87=-1, z88=0)
        elif GetEventFlag(203109) != 0:
            """State 11: Menu conversation: 7_SubState"""
            assert talk_m10_04_x1(text1=74105600, z63=203110, z87=-1, z88=0)
        elif GetEventFlag(203108) != 0:
            """State 10: Menu conversation: 6_SubState"""
            assert talk_m10_04_x1(text1=74105500, z63=203109, z87=-1, z88=0)
        elif GetEventFlag(203106) != 0:
            """State 9: Menu conversation: 5_SubState"""
            assert talk_m10_04_x1(text1=74105400, z63=203108, z87=-1, z88=0)
        elif GetEventFlag(203105) != 0:
            """State 7: Menu conversation: 3_SubState"""
            assert talk_m10_04_x1(text1=74105200, z63=203106, z87=-1, z88=0)
        elif GetEventFlag(203104) != 0:
            """State 6: Menu conversation: 2_SubState"""
            assert talk_m10_04_x1(text1=74105100, z63=203105, z87=-1, z88=0)
        else:
            """State 5: Menu conversation: Part 1_SubState"""
            # talk:74105000:"Have you come unhinged?"
            assert talk_m10_04_x1(text1=74105000, z63=203104, z87=-1, z88=0)
        """State 4: Menu conversation: End"""
        Label('L0')
        ClearNpcMenuSelection()
        """State 14: End state"""
        return 0
    """State 13: Equipment transfer (Conditions: ○ dead) _SubState"""
    # lot:1741000:Ring of Steel Protection, talk:74106000:"I'll be moving on... I suppose..."
    assert talk_m10_04_x21(lot10=1741000, z27=102380, text6=74106000, text7=74106020)
    Goto('L0')

def talk_m10_04_x59():
    """Yorozu Baba: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Yorozu Baba: First conversation_SubState"""
    assert talk_m10_04_x60()
    """State 4: Yorozu Baba: NPC Menu_SubState"""
    assert talk_m10_04_x61()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_04_x60():
    """Yorozu Baba: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(203850) != 0:
        """State 4: Talk: Greeting_SubState"""
        # talk:75400200:"Buy something, anything...", talk:75400300:"Thank you kindly. Keh heh heh...", talk:75400400:"Keh heh heh...", talk:75400500:"You again? Keh heh heh..."
        assert talk_m10_04_x11(z74=104020173, text21=75400200, text22=75400300, text23=75400400, text24=75400500)
    else:
        """State 3: Talk to (first time) _SubState"""
        # talk:75400100:"Oh, you again. "
        assert talk_m10_04_x0(text16=75400100, z89=203850, z90=0)
        """State 2: First conversation: Set contact flag"""
        SetEventFlag(104020173, 1)
    """State 5: End state"""
    return 0

def talk_m10_04_x61():
    """Yorozu Baba: NPC Menu"""
    """State 0,1: Menu: Start"""
    while True:
        """State 4: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_04_x13(z70=0, z71=220, z72=75400000, z73=0)
        if call.Get() == 2:
            """State 5: Yorozu Baba: Menu conversation_SubState"""
            call = talk_m10_04_x62()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3: [Lib] Exit menu: General purpose_SubState"""
            # talk:75400600:"Thank you kindly. Keh heh heh...", talk:75400700:"Lowly times, these are..."
            assert talk_m10_04_x14(text19=75400600, text20=75400700)
        """State 6: End state"""
        Label('L0')
        return 0
    """State 2: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:75400800:"Keh heh heh..."
    assert talk_m10_04_x15(text18=75400800)
    Goto('L0')

def talk_m10_04_x62():
    """Yorozu Baba: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102520) != 1 and (GetGlobalVariable(220) > NpcInfoValue(7540, 0)) != 0 and GetEventFlag(104210)
        != 1):
        """State 6: Equipment transfer (Conditions: Shop purchase total is above a certain level) _SubState"""
        # lot:1754000:Covetous Silver Serpent Ring+1, talk:75406000:"Everyone's so stingy around here. ", talk:75406010:"Everyone's so stingy everywhere!"
        assert talk_m10_04_x25(lot9=1754000, z24=102520, text4=75406000, text5=75406010, z25=0, z26=0)
    elif GetEventFlag(203852) != 0:
        """State 2: Menu conversation: Flag initialization"""
        SetEventFlag(203851, 0)
        SetEventFlag(203852, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:75405000:"My name is Melentia."
        assert talk_m10_04_x1(text1=75405000, z63=203851, z87=-1, z88=0)
    elif GetEventFlag(203851) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:75405100:"Seemed like the battles would never end."
        assert talk_m10_04_x1(text1=75405100, z63=203852, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 7: End state"""
    return 0

def talk_m10_04_x63():
    """Ladder shop: NPC menu"""
    """State 0,1: Menu: Start"""
    SetEventFlag(104020096, 0)
    """State 2: Menu: Branch"""
    while True:
        # goods:63016000:"Prostration" Gesture
        if GetEventFlag(104010080) != 0 and (ItemCount(63016000, 1, 1, 0) > 1) != 0:
            """State 10: Menu start: [Death] No gestures_SubState"""
            Label('L0')
            call = talk_m10_04_x13(z70=0, z71=220, z72=70401003, z73=0)
            if call.Get() == 2:
                """State 5: Ladder shop: Menu conversation_SubState"""
                Label('L1')
                call = talk_m10_04_x64()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 11: [Lib] Menu exit: Purchase flag_SubState"""
                Label('L2')
                # talk:70402600:"Cheers for that! Hah hah! ", talk:70402700:"What? Don't waste my time."
                assert talk_m10_04_x48(text10=70402600, text11=70402700, z34=104020096)
        elif GetEventFlag(104010080) != 0:
            """State 9: Menu start: [Death] Gesture exists_SubState"""
            Label('L3')
            call = talk_m10_04_x13(z70=0, z71=220, z72=70401002, z73=0)
            if call.Get() == 2:
                Goto('L1')
            elif call.Get() == 10:
                """State 8: [Lib] Menu item: Gesture_SubState"""
                Label('L4')
                call = talk_m10_04_x33(z43=63016000, z44=0)
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L2')
        # goods:63016000:"Prostration" Gesture
        elif ((ItemCount(63016000, 1, 1, 0) > 1) != 0 and GetEventFlag(102170) != 0 and GetEventFlag(102171)
              != 0 and GetEventFlag(102172) != 0):
            Goto('L0')
        elif GetEventFlag(102172) != 0 and GetEventFlag(102171) != 0 and GetEventFlag(102170) != 0:
            Goto('L3')
        # goods:63016000:"Prostration" Gesture
        elif (ItemCount(63016000, 1, 1, 0) > 1) != 0:
            """State 7: Menu start: No gesture _SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=70401001, z73=0)
            if call.Get() == 2:
                Goto('L1')
            elif call.Get() == 5:
                """State 6: Ladder shop: Menu item: Ladder_SubState"""
                Label('L5')
                call = talk_m10_04_x65()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L2')
        else:
            """State 3: Menu start: Gesture exists_SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=70401000, z73=0)
            if call.Get() == 2:
                Goto('L1')
            elif call.Get() == 5:
                Goto('L5')
            elif call.Get() == 10:
                Goto('L4')
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L2')
        """State 12: End state"""
        Label('L6')
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:70402800:"Oi! Where're you off to now!"
    assert talk_m10_04_x15(text18=70402800)
    Goto('L6')

def talk_m10_04_x64():
    """Ladder shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102174) != 0 and GetEventFlag(102173) != 1 and GetEventFlag(104050) != 1:
        """State 8: Equipment transfer (condition: choose the highest ladder) _SubState"""
        # lot:1704000:Melu Scimitar, talk:70407000:"Here you are my friend, you can have these, eh!\nIt's a little bonus, you know, for your big purchase.", talk:70407010:"Ah come on, don't look so glum!\nI'm trying to be nice here!"
        assert talk_m10_04_x25(lot9=1704000, z24=102173, text4=70407000, text5=70407010, z25=0, z26=104020034)
    elif GetEventFlag(201854) != 0:
        """State 2: Menu conversation: Flag initialization"""
        SetEventFlag(201851, 0)
        SetEventFlag(201852, 0)
        SetEventFlag(201853, 0)
        SetEventFlag(201854, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:70405000:"You ungrateful little git!"
        assert talk_m10_04_x1(text1=70405000, z63=201851, z87=-1, z88=0)
    elif GetEventFlag(201853) != 0:
        """State 7: Menu conversation: 4_SubState"""
        assert talk_m10_04_x1(text1=70405300, z63=201854, z87=-1, z88=0)
    elif GetEventFlag(201852) != 0:
        """State 6: Menu conversation: 3_SubState"""
        assert talk_m10_04_x1(text1=70405200, z63=201853, z87=-1, z88=0)
    elif GetEventFlag(201851) != 0:
        """State 5: Menu conversation: 2_SubState"""
        assert talk_m10_04_x1(text1=70405100, z63=201852, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_04_x65():
    """Ladder shop: Menu item: Ladder"""
    """State 0,1: Ladder: Start"""
    if GetEventFlag(201855) != 0 and GetEventFlag(102172) != 0:
        """State 15: Ladder menu: First conversation (Single loop 2) _SubState"""
        Label('L0')
        assert talk_m10_04_x1(text1=70405610, z63=0, z87=-1, z88=0)
    elif GetEventFlag(201855) != 0 and GetEventFlag(102171) != 0:
        Goto('L0')
    elif GetEventFlag(201855) != 0 and GetEventFlag(102170) != 0:
        Goto('L0')
    elif GetEventFlag(201855) != 0:
        """State 9: Ladder menu: First conversation (Single loop) _SubState"""
        assert talk_m10_04_x1(text1=70405600, z63=0, z87=-1, z88=0)
    else:
        """State 8: Ladder menu: First conversation_SubState"""
        assert talk_m10_04_x1(text1=70405400, z63=201855, z87=-1, z88=0)
    """State 3: Ladder menu: N choice menu: Open"""
    DisplayMultiOptionMenu(10, 12, 0, 80000, 89901)
    if (MultiOptionMenuResult() == 3) != 0:
        """State 7: Ladder: End (End of cancellation)"""
        ClearNpcMenuSelection()
        SetEventFlag(104020086, 0)
        SetEventFlag(104020087, 0)
        SetEventFlag(104020088, 0)
        SetEventFlag(104020089, 0)
        """State 14: Ladder menu: After N selection is finished (Cancel) _SubState"""
        assert talk_m10_04_x1(text1=70406300, z63=0, z87=-1, z88=0)
    elif GetEventFlag(104020086) != 0:
        """State 10: Ladder menu: N selection: Short ladder selection_SubState"""
        CloseMultiOptionMenu()
        # talk:70406000:"Ohhh, I've had enough of this place..."
        assert talk_m10_04_x1(text1=70406000, z63=0, z87=-1, z88=0)
        """State 4: Ladder menu: N-choice menu: Short: Standby"""
        SetEventFlag(104020089, 1)
        SetEventFlag(104020096, 1)
        assert EventEnded(111095) != 0
        """State 2: Ladder: Finish"""
        Label('L1')
        ClearNpcMenuSelection()
        SetEventFlag(104020086, 0)
        SetEventFlag(104020087, 0)
        SetEventFlag(104020088, 0)
        SetEventFlag(104020089, 0)
        """State 13: Ladder menu: After selecting N_SubState"""
        assert talk_m10_04_x1(text1=70406400, z63=0, z87=-1, z88=0)
    elif GetEventFlag(104020087) != 0:
        """State 11: Ladder menu: N selection: Normal ladder selection_SubState"""
        CloseMultiOptionMenu()
        assert talk_m10_04_x1(text1=70406100, z63=0, z87=-1, z88=0)
        """State 5: Ladder menu: N-choice menu: Normal: Standby"""
        SetEventFlag(104020089, 1)
        SetEventFlag(104020096, 1)
        assert EventEnded(111096) != 0
        Goto('L1')
    elif GetEventFlag(104020088) != 0:
        """State 12: Ladder menu: N selection: Long ladder selection_SubState"""
        CloseMultiOptionMenu()
        assert talk_m10_04_x1(text1=70406200, z63=0, z87=-1, z88=0)
        """State 6: Ladder menu: N-choice menu: Long: Standby"""
        SetEventFlag(104020089, 1)
        SetEventFlag(104020096, 1)
        SetEventFlag(102174, 1)
        assert EventEnded(111097) != 0
        Goto('L1')
    """State 16: End state"""
    return 0

def talk_m10_04_x66():
    """Material shop: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Material shop: First conversation_SubState"""
    assert talk_m10_04_x67()
    """State 4: Material shop: NPC menu_SubState"""
    assert talk_m10_04_x68()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_04_x67():
    """Material shop: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(204350) != 0:
        """State 4: [Lib] Conversation: Greeting: General purpose_SubState"""
        # talk:76200200:"What? Do you need something?", talk:76200300:"I'll provide whatever service you need.\nFor a fair price, of course!", talk:76200400:"You've been long away. What would you like?"
        assert talk_m10_04_x11(z74=104020123, text21=76200200, text22=76200300, text23=76200400, text24=76200400)
    else:
        """State 3: Talk: First_SubState"""
        # talk:76200000:"Are you a traveller?"
        assert talk_m10_04_x0(text16=76200000, z89=204350, z90=0)
        """State 2: First conversation: contact flag"""
        SetEventFlag(104020123, 1)
    """State 5: End state"""
    return 0

def talk_m10_04_x68():
    """Material shop: NPC menu"""
    """State 0,1: Menu: Start"""
    while True:
        """State 5: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_04_x13(z70=0, z71=220, z72=76200000, z73=0)
        if call.Get() == 2:
            """State 3: Material shop: Menu conversation_SubState"""
            call = talk_m10_04_x69()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Exit menu: General purpose_SubState"""
            # talk:76200600:"Visit me again, whenever you please.", talk:76200700:"No interest? Suit yourself."
            assert talk_m10_04_x14(text19=76200600, text20=76200700)
        """State 6: End state"""
        Label('L0')
        return 0
    """State 2: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76200900:"Oi! Mind your manners!"
    assert talk_m10_04_x15(text18=76200900)
    Goto('L0')

def talk_m10_04_x69():
    """Material shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102620) != 1 and (GetGlobalVariable(221) > NpcInfoValue(7620, 0)) != 0 and GetEventFlag(104260)
        != 1):
        """State 3: Equipment transfer (Conditions: Shop purchase total is above a certain level) _SubState"""
        # lot:1762000:Twinkling Titanite, talk:76206000:"Bye for now. Heh heh..."
        assert talk_m10_04_x25(lot9=1762000, z24=102620, text4=76206000, text5=76206010, z25=0, z26=0)
    elif GetEventFlag(104280) != 0:
        """State 5: Material shop: Menu conversation (blacksmith death) _SubState"""
        assert talk_m10_04_x121()
    else:
        """State 4: Material shop: Menu conversation (Blacksmith survival) _SubState"""
        assert talk_m10_04_x120()
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 6: End state"""
    return 0

def talk_m10_04_x70():
    """Dragon Miko: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(201102) != 0:
        """State 4: Dragon Miko: Normal conversation_SubState"""
        assert talk_m10_04_x72()
        """State 5: Dragon Miko: NPC Menu_SubState"""
        assert talk_m10_04_x73()
    else:
        """State 3: Dragon Miko: First Conversation_SubState"""
        assert talk_m10_04_x71()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_04_x71():
    """Dragon Miko: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(201101) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:70000200:"Bearer of the curse..."
        assert talk_m10_04_x41(text13=70000200, z49=201102, z50=104020149, z51=104010159, z52=104010166)
    elif GetEventFlag(201100) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:70000100:"Bearer of the curse, seek misery."
        assert talk_m10_04_x41(text13=70000100, z49=201101, z50=104020149, z51=104010159, z52=104010166)
    else:
        """State 3: Speak: Part 1: 1_SubState"""
        # talk:70000000:"Are you...the next monarch?"
        assert talk_m10_04_x41(text13=70000000, z49=0, z50=104020149, z51=104010159, z52=104010166)
        """State 7: [Lib] Conversation: Item Transfer: Mes⇒Item⇒Mes: Important Item_SubState"""
        # lot:1700000:Estus Flask, talk:70000020:"Bearer of the curse...", talk:70000050:"Go on, and see the King.", goods:60155000:Estus Flask
        assert (talk_m10_04_x49(lot2=1700000, z7=102090, text1=70000020, text2=70000050, z8=201100, z9=0,
                goods1=60155000))
        """State 2: Initial conversation: Information display"""
        # action:2020:"You may level up by the power of the Emerald Herald"
        DisplayEventMessage(2020, 0, 0, 0)
    """State 8: End state"""
    return 0

def talk_m10_04_x72():
    """Dragon Miko: normal conversation"""
    """State 0,1: Normal conversation: Start"""
    if GetEventFlag(102080) != 0 and GetEventFlag(201110) != 1:
        """State 6: Talking 4: 4 boss after defeating the first _SubState"""
        # talk:70000500:"Beyond the bonfire lies the Forest of the Giants,\nwhere a great battle precipitated the kingdom's downfall."
        assert talk_m10_04_x41(text13=70000500, z49=201110, z50=104020149, z51=104010159, z52=104010166)
    elif GetEventFlag(102081) != 0 and GetEventFlag(201111) != 1:
        """State 7: Talk to 4: 4 boss after defeating the second _SubState"""
        # talk:70000600:"The far gate is the entrance to Heide's Tower of Flame."
        assert talk_m10_04_x41(text13=70000600, z49=201111, z50=104020149, z51=104010159, z52=104010166)
    elif GetEventFlag(102082) != 0 and GetEventFlag(201112) != 1:
        """State 8: Talk to 4: 4 boss after defeating the third _SubState"""
        # talk:70000700:"Inside the giant pit..."
        assert talk_m10_04_x41(text13=70000700, z49=201112, z50=104020149, z51=104010159, z52=104010166)
    elif GetEventFlag(102083) != 0 and GetEventFlag(201113) != 1:
        """State 9: Talking 4: 4 bosses after defeating 4th _SubState"""
        # talk:70000800:"Over the hill and past the forest is the King's castle."
        assert talk_m10_04_x41(text13=70000800, z49=201113, z50=104020149, z51=104010159, z52=104010166)
    # goods:60525000:Estus Flask Shard
    elif GetEventFlag(104020163) != 1 and (ItemCount(60525000, 1, 1, 0) > 1) != 0 and EstusAtMaxStrength() != 1:
        """State 3: Talk 4: Ess Fragment: 1_SubState"""
        assert talk_m10_04_x41(text13=70000900, z49=0, z50=104020149, z51=104010159, z52=104010166)
        """State 10: Speak 4: Est fragment: 2_SubState"""
        assert talk_m10_04_x1(text1=70000910, z63=0, z87=-1, z88=0)
        """State 2: Normal conversation: Contact flag setting"""
        SetEventFlag(104020163, 1)
    elif GetEventFlag(100958) != 0:
        """State 5: Talk 4: There is a castle clear flag_SubState"""
        # talk:70000400:"Bearer of the curse. I will always be at your side."
        assert talk_m10_04_x41(text13=70000400, z49=0, z50=104020149, z51=104010159, z52=104010166)
    else:
        """State 4: Talk 4: No Royal Castle clear flag_SubState"""
        # talk:70000300:"Bearer of the curse..."
        assert talk_m10_04_x41(text13=70000300, z49=0, z50=104020149, z51=104010159, z52=104010166)
    """State 11: End state"""
    return 0

def talk_m10_04_x73():
    """Dragon Miko: NPC Menu"""
    """State 0,1: Menu: Start"""
    while True:
        """State 2: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_04_x13(z70=0, z71=220, z72=70000000, z73=0)
        if call.Get() == 2:
            """State 3: Dragon Miko: Menu Conversation_SubState"""
            call = talk_m10_04_x74()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 12:
            """State 6: Dragon Miko: Menu: Est Bottle Strengthening_SubState"""
            call = talk_m10_04_x113()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 13:
            """State 7: Dragon Miko: Menu: Level Up _SubState"""
            call = talk_m10_04_x114()
            if call.Done():
                continue
            elif ((NpcMenuResult() == 19) != 0 and PlayerIsInEventAction(1) != 1 and PlayerIsInEventAction(-9999)
                  != 1):
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Menu exit: No Mes_SubState"""
            assert talk_m10_04_x27()
        """State 8: End state"""
        Label('L0')
        return 0
    """State 5: [Lib] Menu canceled: No Mes_SubState"""
    assert talk_m10_04_x28()
    Goto('L0')

def talk_m10_04_x74():
    """Dragon Miko: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(201128) != 0:
        """State 2: Menu conversation: Flag initialization"""
        SetEventFlag(201123, 0)
        SetEventFlag(201124, 0)
        SetEventFlag(201125, 0)
        SetEventFlag(201126, 0)
        SetEventFlag(201127, 0)
        SetEventFlag(201128, 0)
        """State 7: Menu conversation: 4_SubState"""
        Label('L0')
        assert talk_m10_04_x1(text1=70005300, z63=201123, z87=-1, z88=0)
    elif GetEventFlag(201127) != 0:
        """State 12: Menu conversation: 9_SubState"""
        assert talk_m10_04_x1(text1=70005800, z63=201128, z87=-1, z88=0)
    elif GetEventFlag(201126) != 0:
        """State 11: Menu conversation: 8_SubState"""
        assert talk_m10_04_x1(text1=70005700, z63=201127, z87=-1, z88=0)
    elif GetEventFlag(201125) != 0:
        """State 10: Menu conversation: 7_SubState"""
        assert talk_m10_04_x1(text1=70005600, z63=201126, z87=-1, z88=0)
    elif GetEventFlag(201124) != 0:
        """State 9: Menu conversation: 6_SubState"""
        assert talk_m10_04_x1(text1=70005500, z63=201125, z87=-1, z88=0)
    elif GetEventFlag(201123) != 0:
        """State 8: Menu conversation: 5_SubState"""
        assert talk_m10_04_x1(text1=70005400, z63=201124, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 13: End state"""
    return 0

def talk_m10_04_x75():
    """Magician: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    """State 3: Magician: First conversation_SubState"""
    call = talk_m10_04_x76()
    if call.Get() == 1:
        """State 4: Magician: NPC Menu_SubState"""
        assert talk_m10_04_x77()
    elif call.Get() == 0:
        pass
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_04_x76():
    """Magician: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(204820) != 0:
        """State 4: [Lib] Conversation: Greeting: General purpose_SubState"""
        # talk:76601000:"Do you seek my teachings?\nVery well, very well.", talk:76601100:"Back already?\nYour diligence is commendable.", talk:76601200:"Your visit is welcome.\nI trust you've kept up your studies.", talk:76601300:"Oh, there you are. Do you seek my teachings?"
        assert talk_m10_04_x11(z74=104020143, text21=76601000, text22=76601100, text23=76601200, text24=76601300)
    else:
        """State 3: Talk: First_SubState"""
        # talk:76603000:"Oh, so you've finally decided to join us?"
        assert talk_m10_04_x0(text16=76603000, z89=204820, z90=0)
        """State 2: First conversation: Set contact flag"""
        SetEventFlag(104020143, 1)
    """State 6: Menu: Exit state"""
    return 1

def talk_m10_04_x77():
    """Magician: NPC Menu"""
    """State 0,1,3: [Lib] Menu start: General purpose_SubState"""
    while True:
        call = talk_m10_04_x13(z70=0, z71=220, z72=76600000, z73=0)
        if call.Get() == 2:
            """State 5: Magician: Menu conversation_SubState"""
            call = talk_m10_04_x78()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 6: [Lib] Exit menu: General purpose_SubState"""
            # talk:76601400:"Young pupil, do not take my teachings lightly.", talk:76601500:"One day, my teachings will save you."
            assert talk_m10_04_x14(text19=76601400, text20=76601500)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuSelection()
        """State 7: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76601700:"The path is yet long, young pupil."
    assert talk_m10_04_x15(text18=76601700)
    Goto('L0')

def talk_m10_04_x78():
    """Magician: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102720) != 1 and (GetPlayerStat(5, 1) > NpcInfoValue(7660, 2)) != 0 and GetEventFlag(104300)
        != 1):
        """State 3: Equipment transfer (Conditions: Reason is above a certain level) _SubState"""
        # lot:1766000:Northern Ritual Band+1, talk:76606000:"Do not neglect your studies, dear pupil."
        assert talk_m10_04_x25(lot9=1766000, z24=102720, text4=76606000, text5=76606010, z25=0, z26=0)
    elif GetEventFlag(104272) != 0:
        """State 6: Magician: Menu Conversation: Death after moving to a magician_SubState"""
        assert talk_m10_04_x117()
    elif GetEventFlag(102640) != 0 and GetEventFlag(102650) != 0 and GetEventFlag(103771) != 1:
        """State 5: Magician: Menu Conversation: Magician Emigration_SubState"""
        assert talk_m10_04_x116()
    else:
        """State 4: Magician: Menu Conversation: Magician not migrated or died _SubState"""
        assert talk_m10_04_x115()
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 7: End state"""
    return 0

def talk_m10_04_x79():
    """Miracle: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    assert GetEventFlag(104020156) != 1
    """State 3: Miracle: First conversation_SubState"""
    assert talk_m10_04_x80()
    """State 4: Miracle: NPC Menu_SubState"""
    assert talk_m10_04_x81()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 5: End state"""
    return 0

def talk_m10_04_x80():
    """Miracle: First conversation"""
    """State 0,1: First conversation: start"""
    if GetEventFlag(205050) != 0 and GetEventFlag(102761) != 0:
        """State 4: Menu conversation: Defeat 3 bosses_SubState"""
        # talk:76903000:"You've had quite a journey, I can see..."
        assert talk_m10_04_x0(text16=76903000, z89=0, z90=0)
    elif GetEventFlag(205050) != 0:
        """State 3: Talk: Part 1: Second time _SubState"""
        # talk:76901100:"Just speak up if you're in need of miracles."
        assert talk_m10_04_x0(text16=76901100, z89=0, z90=0)
    else:
        """State 2: Talk: Part 1_SubState"""
        # talk:76901000:"Oh, hello there...\nAn honour to see you again."
        assert talk_m10_04_x0(text16=76901000, z89=205050, z90=0)
    """State 5: End state"""
    return 0

def talk_m10_04_x81():
    """Miracles: NPC menu"""
    """State 0,2: Menu: Start"""
    ClearNpcMenuResults()
    SetEventFlag(104020098, 0)
    """State 3: Menu: Branch"""
    while True:
        if GetEventFlag(104320) != 0:
            """State 9: [Lib] Menu start: At death_SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=76900001, z73=0)
            if call.Get() == 2:
                """State 6: Miracle: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_04_x82()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                """State 8: [Lib] Menu exit: Purchase flag_SubState"""
                Label('L1')
                # talk:76901300:"May the power of miracles be with you.", talk:76901400:"No need for miracles?"
                assert talk_m10_04_x48(text10=76901300, text11=76901400, z34=104020098)
        else:
            """State 5: [Lib] Menu start: When living, _SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=76900000, z73=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 9:
                """State 7: Miracle Person: Menu Item: Route Change_SubState"""
                call = talk_m10_04_x83(val2=2000, z6=-2000)
                if call.Done():
                    continue
                elif ((NpcMenuResult() == 19) != 0 and (GetAreaVariable(57) == 200) != 1 and PlayerIsInEventAction(9)
                      != 1):
                    break
            elif call.Get() == 0:
                break
            elif call.Get() == 1:
                Goto('L1')
        """State 1: Menu: Exit"""
        Label('L2')
        ClearNpcMenuResults()
        """State 10: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76901500:"Oh? Done so soon?"
    assert talk_m10_04_x15(text18=76901500)
    Goto('L2')

def talk_m10_04_x82():
    """Miracle: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102760) != 1 and (GetPlayerStat(6, 1) > NpcInfoValue(7690, 3)) != 0 and GetEventFlag(104320)
        != 1):
        """State 8: Equipment transfer (Condition: Belief over a certain level) _SubState"""
        # lot:1769000:Idol's Chime, talk:76906000:"Seek...miracles..."
        assert talk_m10_04_x25(lot9=1769000, z24=102760, text4=76906000, text5=76906010, z25=0, z26=0)
    elif GetEventFlag(205062) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(205060, 0)
        SetEventFlag(205061, 0)
        SetEventFlag(205062, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76901600:"To cast miracles,\nyou must have strong faith in the gods."
        assert talk_m10_04_x1(text1=76901600, z63=205060, z87=-1, z88=0)
    elif GetEventFlag(205061) != 0:
        """State 6: Menu conversation: 3_SubState"""
        # talk:76901800:"What is the First Flame?"
        assert talk_m10_04_x1(text1=76901800, z63=205062, z87=-1, z88=0)
    elif GetEventFlag(205060) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:76901700:"Miracles have been passed down\nthrough us since the First Flame."
        assert talk_m10_04_x1(text1=76901700, z63=205061, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_04_x83(val2=2000, z6=-2000):
    """Miracle Person: Menu Item: Route Change
    val2: Seoul amount
    z6: Subtract soul amount
    """
    """State 0,1: Route change: Start"""
    ClearNpcMenuAction()
    """State 10: Seoul payment selection dialog_SubState"""
    # action:1203:"Pay souls?\nSouls needed: %d"
    call = talk_m10_04_x34(action5=1203, val2=val2)
    if call.Get() == 1:
        pass
    elif call.Get() == 0 and (CurrentSouls() > val2) != 1:
        """State 9: Soul shortage confirmation dialog_SubState"""
        # action:1016:"Insufficient souls"
        assert talk_m10_04_x19(action8=1016)
    elif call.Get() == 0:
        """State 8: Route change: Event action: Start"""
        PlayerActionRequest(9)
        assert PlayerIsInEventAction(9) != 0
        """State 3: Route change: Seoul subtraction"""
        AddSouls(z6)
        SetEventFlag(104020098, 1)
        """State 4: Route change: OBJ animation started"""
        SetAreaVariable(57, 200)
        assert (GetStateTime() > GetRandomValueForStateTime(2, 2)) != 0
        """State 7: Route change: Timer"""
        SetEventFlag(104020156, 1)
        assert GetEventFlag(104020156) != 0
        """State 5: Route change: OBJ anime: Waiting"""
        assert GetEventFlag(104020156) != 1
        """State 6: Route change: Area variable: Setting"""
        SetAreaVariable(57, 1)
        EndPlayerActionRequest()
        """State 11: Menu: Route change_SubState"""
        # talk:76901200:"Go ahead, then."
        assert talk_m10_04_x1(text1=76901200, z63=0, z87=-1, z88=0)
    elif call.Get() == 2:
        pass
    """State 2: Route change: End"""
    ClearNpcMenuSelection()
    """State 12: End state"""
    return 0

def talk_m10_04_x84():
    """Blacksmith: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102661) != 0:
        """State 4: Blacksmith: Inside: Conversation_SubState"""
        assert talk_m10_04_x86()
        """State 5: Blacksmith: NPC Menu_SubState"""
        assert talk_m10_04_x87()
    else:
        """State 3: Blacksmith: Locking: Conversation_SubState"""
        assert talk_m10_04_x85()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_04_x85():
    """Blacksmith: Locked: Conversation"""
    """State 0,1: Locking: Start"""
    if GetEventFlag(102660) != 0:
        """State 5: Outdoors: Unlocking: Talking to: 1_SubState"""
        Label('L0')
        # talk:76400200:"Ah, yes, very good."
        assert talk_m10_04_x0(text16=76400200, z89=0, z90=0)
    elif GetEventFlag(204500) != 0:
        """State 4: Outdoors: Locking: Talking to: 2_SubState"""
        # talk:76400100:"I'm a blacksmith.\nI'm nothing without my tools."
        call = talk_m10_04_x0(text16=76400100, z89=0, z90=0)
        if call.Done():
            pass
        elif GetEventFlag(102660) != 0:
            """State 2: Locking: Door unlocking: Key guide removed"""
            Label('L1')
            DeleteKeyGuideArea()
            Goto('L0')
    else:
        """State 3: Outdoors: Locking: Talking to: 1_SubState"""
        # talk:76400000:"Who are you?"
        call = talk_m10_04_x0(text16=76400000, z89=204500, z90=0)
        if call.Done():
            pass
        elif GetEventFlag(102660) != 0:
            Goto('L1')
    """State 6: End state"""
    return 0

def talk_m10_04_x86():
    """Blacksmith: Room: Conversation"""
    """State 0,1: Indoor conversation: Start"""
    if GetEventFlag(204510) != 0:
        """State 4: [Lib] Conversation: Greeting: General purpose_SubState"""
        # talk:76400400:"What? You again?", talk:76400500:"You again?\nCan't you see that I'm busy?", talk:76400600:"Hmph, I'd given you up for dead.\nAlmost had me worried, really...", talk:76400700:"I knew you'd be around soon.\nGo on, show me what you've got."
        assert talk_m10_04_x11(z74=104020133, text21=76400400, text22=76400500, text23=76400600, text24=76400700)
    else:
        """State 3: Talk: First_SubState"""
        # talk:76400300:"You, stand back.\nThis is dangerous work."
        assert talk_m10_04_x0(text16=76400300, z89=204510, z90=0)
        """State 2: Indoor conversation: contact flag setting"""
        SetEventFlag(104020133, 1)
        assert GetEventFlag(104020133) != 0
    """State 5: End state"""
    return 0

def talk_m10_04_x87():
    """Blacksmith: NPC menu"""
    """State 0,1: Menu: Start"""
    while True:
        """State 4: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_04_x13(z70=0, z71=220, z72=76400000, z73=0)
        if call.Get() == 2:
            """State 5: Blacksmith: Menu conversation_SubState"""
            call = talk_m10_04_x88()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3: [Lib] Exit menu: General purpose_SubState"""
            # talk:76400800:"I'll be around, if you make it back.", talk:76400900:"Hmph. Don't waste my time."
            assert talk_m10_04_x14(text19=76400800, text20=76400900)
        """State 6: End state"""
        Label('L0')
        return 0
    """State 2: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76401000:"People these days..."
    assert talk_m10_04_x15(text18=76401000)
    Goto('L0')

def talk_m10_04_x88():
    """Blacksmith: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102662) != 1 and (GetGlobalVariable(225) > NpcInfoValue(7640, 1)) != 0 and GetEventFlag(104280)
        != 1):
        """State 10: Equipment transfer (Condition: Blacksmith: Equipment strengthening / Attribute change usage total) _SubState"""
        # lot:1764000:Blacksmith's Hammer, talk:76406000:"Chloanne...I..."
        assert talk_m10_04_x26(lot8=1764000, z21=102662, text3=76406000, z22=0, z23=0)
    # goods:50990000:Dull Ember
    elif (ItemCount(50990000, 1, 1, 0) > 1) != 0 and GetEventFlag(204530) != 1:
        """State 3: Menu conversation: seed fire: when possession of seed fire _SubState"""
        # talk:76401500:"I see that you have an ember.\nWhere did you get it?"
        assert talk_m10_04_x1(text1=76401500, z63=204530, z87=-1, z88=0)
    elif GetEventFlag(104260) != 0 and GetEventFlag(104050) != 0:
        """State 4: Blacksmith: Menu Conversation: Elemental (Death) & Ladder (Death) / Ladder (Not) _SubState"""
        Label('L0')
        assert talk_m10_04_x89()
    elif GetEventFlag(104260) != 0 and GetEventFlag(102165) != 0 and GetEventFlag(103551) != 0:
        Goto('L0')
    elif GetEventFlag(104260) != 0 and GetEventFlag(102165) != 0 and GetEventFlag(103551) != 1:
        """State 5: Blacksmith: Menu Conversation: Elemental (Death) & Ladder (Trans) _SubState"""
        assert talk_m10_04_x92()
    elif GetEventFlag(104260) != 0 and GetEventFlag(102165) != 1:
        Goto('L0')
    elif GetEventFlag(103761) != 1 and GetEventFlag(102625) != 0 and GetEventFlag(102165) != 1:
        """State 8: Blacksmith: Menu Conversation: Elementary (Transfer) & Ladder (Not) / Ladder (Death) _SubState"""
        Label('L1')
        assert talk_m10_04_x93()
    elif (GetEventFlag(103761) != 1 and GetEventFlag(102625) != 0 and GetEventFlag(103551) != 0 and GetEventFlag(102165)
          != 0):
        Goto('L1')
    elif GetEventFlag(103761) != 1 and GetEventFlag(102625) != 0 and GetEventFlag(104050) != 0:
        Goto('L1')
    elif (GetEventFlag(103761) != 1 and GetEventFlag(102625) != 0 and GetEventFlag(103551) != 1 and GetEventFlag(102165)
          != 0):
        """State 9: Blacksmith: Menu Conversation: Elementary (Move) & Ladder (Move) _SubState"""
        assert talk_m10_04_x94()
    elif GetEventFlag(102625) != 1 and GetEventFlag(104050) != 0:
        """State 6: Blacksmith: Menu conversation: Elementary (not yet) & ladder (not yet) _SubState"""
        Label('L2')
        assert talk_m10_04_x90()
    elif GetEventFlag(102625) != 0 and GetEventFlag(104050) != 0 and GetEventFlag(103761) != 0:
        Goto('L2')
    elif GetEventFlag(102625) != 1 and GetEventFlag(102165) != 1:
        Goto('L2')
    elif GetEventFlag(102625) != 1 and GetEventFlag(103551) != 0 and GetEventFlag(102165) != 0:
        Goto('L2')
    elif GetEventFlag(103761) != 0 and GetEventFlag(102625) != 0 and GetEventFlag(102165) != 1:
        Goto('L2')
    elif (GetEventFlag(103761) != 0 and GetEventFlag(102625) != 0 and GetEventFlag(103551) != 0 and GetEventFlag(102165)
          != 0):
        Goto('L2')
    elif GetEventFlag(102625) != 1 and GetEventFlag(102165) != 0 and GetEventFlag(103551) != 1:
        """State 7: Blacksmith: Menu conversation: Elementary (not yet) & ladder (transfer) _SubState"""
        Label('L3')
        assert talk_m10_04_x91()
    elif (GetEventFlag(103761) != 0 and GetEventFlag(102625) != 0 and GetEventFlag(102165) != 0 and GetEventFlag(103551)
          != 1):
        Goto('L3')
    else:
        Goto('L2')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 11: End state"""
    return 0

def talk_m10_04_x89():
    """Blacksmith: Menu Conversation: Elemental (Death) & Ladder (Death) / Ladder (Not)"""
    """State 0,1: Both deaths: Start"""
    if GetEventFlag(204521) != 0:
        """State 2: Both deaths: initialization settings"""
        SetEventFlag(204520, 0)
        SetEventFlag(204521, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76401100:"Drat, you're worse than my reckless daughter."
        assert talk_m10_04_x1(text1=76401100, z63=204520, z87=-1, z88=0)
    elif GetEventFlag(204520) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76401300:"You'll need souls\nto repair and improve equipment."
        assert talk_m10_04_x1(text1=76401300, z63=204521, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 5: End state"""
    return 0

def talk_m10_04_x90():
    """Blacksmith: Menu conversation: Elementary (not yet) & ladder (not yet)"""
    """State 0,1: Both immigrants: Start"""
    if GetEventFlag(204522) != 0:
        """State 2: Both have not migrated: Initialization settings"""
        SetEventFlag(204520, 0)
        SetEventFlag(204521, 0)
        SetEventFlag(204522, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76401100:"Drat, you're worse than my reckless daughter."
        assert talk_m10_04_x1(text1=76401100, z63=204520, z87=-1, z88=0)
    elif GetEventFlag(204521) != 0:
        """State 5: Menu conversation: Part 3: Material shop not moving and survival_SubState"""
        # talk:76401400:"Equipment can be strengthened with rare orestone.\nBut such orestone won't come easily."
        assert talk_m10_04_x1(text1=76401400, z63=204522, z87=-1, z88=0)
    elif GetEventFlag(204520) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76401300:"You'll need souls\nto repair and improve equipment."
        assert talk_m10_04_x1(text1=76401300, z63=204521, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 6: End state"""
    return 0

def talk_m10_04_x91():
    """Blacksmith: Menu conversation: Elementary (not yet) & ladder (transfer)"""
    """State 0,1: Ladder shop migration: Start"""
    if GetEventFlag(204526) != 0:
        """State 2: Ladder-house migration: initialization settings"""
        SetEventFlag(204520, 0)
        SetEventFlag(204521, 0)
        SetEventFlag(204522, 0)
        SetEventFlag(204525, 0)
        SetEventFlag(204526, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76401100:"Drat, you're worse than my reckless daughter."
        assert talk_m10_04_x1(text1=76401100, z63=204520, z87=-1, z88=0)
    elif GetEventFlag(204525) != 0:
        """State 7: Menu conversation: Part 7: Ladder-house migration & survival_SubState"""
        # talk:76401900:"Gilligan can certainly be helpful at times,\nbut he's a real conniver when it comes to money."
        assert talk_m10_04_x1(text1=76401900, z63=204526, z87=-1, z88=0)
    elif GetEventFlag(204522) != 0:
        """State 6: Menu conversation: Part 6: Ladder-house migration & survival_SubState"""
        # talk:76401800:"Now, don't go near that scum\nnear the pit."
        assert talk_m10_04_x1(text1=76401800, z63=204525, z87=-1, z88=0)
    elif GetEventFlag(204521) != 0:
        """State 5: Menu conversation: Part 3: Material shop not moving and survival_SubState"""
        # talk:76401400:"Equipment can be strengthened with rare orestone.\nBut such orestone won't come easily."
        assert talk_m10_04_x1(text1=76401400, z63=204522, z87=-1, z88=0)
    elif GetEventFlag(204520) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76401300:"You'll need souls\nto repair and improve equipment."
        assert talk_m10_04_x1(text1=76401300, z63=204521, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 8: End state"""
    return 0

def talk_m10_04_x92():
    """Blacksmith: Menu conversation: Elementary (death) & ladder (transfer)"""
    """State 0,1: Material Death Ladder Shop Emigration: Start"""
    if GetEventFlag(204526) != 0:
        """State 2: Material death ladder house emigration: initialization setting"""
        SetEventFlag(204520, 0)
        SetEventFlag(204521, 0)
        SetEventFlag(204525, 0)
        SetEventFlag(204526, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76401100:"Drat, you're worse than my reckless daughter."
        assert talk_m10_04_x1(text1=76401100, z63=204520, z87=-1, z88=0)
    elif GetEventFlag(204525) != 0:
        """State 6: Menu conversation: Part 7: Ladder-house migration & survival_SubState"""
        # talk:76401900:"Gilligan can certainly be helpful at times,\nbut he's a real conniver when it comes to money."
        assert talk_m10_04_x1(text1=76401900, z63=204526, z87=-1, z88=0)
    elif GetEventFlag(204521) != 0:
        """State 5: Menu conversation: Part 6: Ladder-house migration & survival_SubState"""
        # talk:76401800:"Now, don't go near that scum\nnear the pit."
        assert talk_m10_04_x1(text1=76401800, z63=204525, z87=-1, z88=0)
    elif GetEventFlag(204520) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76401300:"You'll need souls\nto repair and improve equipment."
        assert talk_m10_04_x1(text1=76401300, z63=204521, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_04_x93():
    """Blacksmith: Menu Conversation: Elementary (Transfer) & Ladder (Not) / Ladder (Death)"""
    """State 0,1: Material migration ladder not dead: start"""
    if GetEventFlag(204524) != 0:
        """State 2: Material migration ladder not dead: initialization setting"""
        SetEventFlag(204520, 0)
        SetEventFlag(204521, 0)
        SetEventFlag(204523, 0)
        SetEventFlag(204524, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76401100:"Drat, you're worse than my reckless daughter."
        assert talk_m10_04_x1(text1=76401100, z63=204520, z87=-1, z88=0)
    elif GetEventFlag(204523) != 0:
        """State 6: Menu conversation: Part 5: Material shop migration & survival_SubState"""
        # talk:76401700:"Stones? Try asking my daughter."
        assert talk_m10_04_x1(text1=76401700, z63=204524, z87=-1, z88=0)
    elif GetEventFlag(204521) != 0:
        """State 5: Menu conversation: Part 4: Material shop migration & survival_SubState"""
        # talk:76401600:"My witless daughter finally came home."
        assert talk_m10_04_x1(text1=76401600, z63=204523, z87=-1, z88=0)
    elif GetEventFlag(204520) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76401300:"You'll need souls\nto repair and improve equipment."
        assert talk_m10_04_x1(text1=76401300, z63=204521, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_04_x94():
    """Blacksmith: Menu conversation: Elementary (moving) & ladder (moving)"""
    """State 0,1: Material transfer ladder transfer: Start"""
    if GetEventFlag(204526) != 0:
        """State 2: Material transfer ladder: initialization setting"""
        SetEventFlag(204520, 0)
        SetEventFlag(204521, 0)
        SetEventFlag(204523, 0)
        SetEventFlag(204524, 0)
        SetEventFlag(204525, 0)
        SetEventFlag(204526, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76401100:"Drat, you're worse than my reckless daughter."
        assert talk_m10_04_x1(text1=76401100, z63=204520, z87=-1, z88=0)
    elif GetEventFlag(204525) != 0:
        """State 8: Menu conversation: Part 7: Ladder-house migration & survival_SubState"""
        # talk:76401900:"Gilligan can certainly be helpful at times,\nbut he's a real conniver when it comes to money."
        assert talk_m10_04_x1(text1=76401900, z63=204526, z87=-1, z88=0)
    elif GetEventFlag(204524) != 0:
        """State 7: Menu conversation: Part 6: Ladder-house migration & survival_SubState"""
        # talk:76401800:"Now, don't go near that scum\nnear the pit."
        assert talk_m10_04_x1(text1=76401800, z63=204525, z87=-1, z88=0)
    elif GetEventFlag(204523) != 0:
        """State 6: Menu conversation: Part 5: Material shop migration & survival_SubState"""
        # talk:76401700:"Stones? Try asking my daughter."
        assert talk_m10_04_x1(text1=76401700, z63=204524, z87=-1, z88=0)
    elif GetEventFlag(204521) != 0:
        """State 5: Menu conversation: Part 4: Material shop migration & survival_SubState"""
        # talk:76401600:"My witless daughter finally came home."
        assert talk_m10_04_x1(text1=76401600, z63=204523, z87=-1, z88=0)
    elif GetEventFlag(204520) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76401300:"You'll need souls\nto repair and improve equipment."
        assert talk_m10_04_x1(text1=76401300, z63=204521, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 9: End state"""
    return 0

def talk_m10_04_x95():
    """Armor store: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(102610) != 1 and GetEventFlag(102611) != 1 and GetEventFlag(102612) != 1:
        """State 3: Armor shop: Conversation: Flag initial setting"""
        SetEventFlag(102610, 1)
        assert GetEventFlag(102610) != 0
        """State 4: Armor store: Bearish: First conversation_SubState"""
        Label('L0')
        assert talk_m10_04_x96()
    elif GetEventFlag(102612) != 0:
        """State 6: Armor store: Bullish: First conversation_SubState"""
        assert talk_m10_04_x98()
    elif GetEventFlag(102611) != 0:
        """State 5: Armor shop: Normal: First conversation_SubState"""
        assert talk_m10_04_x97()
    elif GetEventFlag(102610) != 0:
        Goto('L0')
    """State 7: Armor shop: NPC menu_SubState"""
    assert talk_m10_04_x99()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 8: End state"""
    return 0

def talk_m10_04_x96():
    """Armor store: Bearish: First conversation"""
    """State 0,1: Bearish: First conversation: Start"""
    if GetEventFlag(204200) != 0:
        """State 4: Bearish: Greeting_SubState"""
        # talk:76100100:"Well, thank you, for coming back!\nDo take a look at my wares.", talk:76100200:"Oh, hello again.\nI-I hope you find something of use."
        assert talk_m10_04_x23(z68=104020113, text16=76100100, text17=76100200)
    else:
        """State 3: Bearish: Talk: Initial _SubState"""
        # talk:76100000:"Err, oh, hello there!"
        assert talk_m10_04_x0(text16=76100000, z89=204200, z90=0)
        """State 2: Bearish: First conversation: Set contact flag"""
        SetEventFlag(104020113, 1)
        assert GetEventFlag(104020113) != 0
    """State 5: End state"""
    return 0

def talk_m10_04_x97():
    """Armor shop: Normal: First conversation"""
    """State 0,1: Normal: First conversation: Start"""
    if GetEventFlag(204220) != 0:
        """State 4: Normal: Greeting_SubState"""
        # talk:76101700:"Forget to buy something?\nGo ahead, take your time.", talk:76101800:"I'm glad to see you safe.\nTake...take a look at my wares."
        assert talk_m10_04_x23(z68=104020113, text16=76101700, text17=76101800)
    else:
        """State 3: Normal: Talk: First time _SubState"""
        # talk:76101600:"Oh, I was hoping that you would come."
        assert talk_m10_04_x0(text16=76101600, z89=204220, z90=0)
        """State 2: Normal: First conversation: Set contact flag"""
        SetEventFlag(104020113, 1)
        assert GetEventFlag(104020113) != 0
    """State 5: End state"""
    return 0

def talk_m10_04_x98():
    """Armor shop: Bullish: First conversation"""
    """State 0,1: Bull: First conversation: Start"""
    if GetEventFlag(204240) != 0:
        """State 4: Bull: Greeting_SubState"""
        # talk:76103200:"Looking for armour?\nEverything I offer is quite dependable.", talk:76103300:"You need armour? Go ahead, see what I'm offering."
        assert talk_m10_04_x23(z68=104020113, text16=76103200, text17=76103300)
    else:
        """State 3: Bull: Talk to: First_SubState"""
        # talk:76103100:"Um, sorry, have we met?\nOh sorry, it's just I've been awfully busy lately."
        assert talk_m10_04_x0(text16=76103100, z89=204240, z90=0)
        """State 2: Bull: First conversation: Set contact flag"""
        SetEventFlag(104020113, 1)
        assert GetEventFlag(104020113) != 0
    """State 5: End state"""
    return 0

def talk_m10_04_x99():
    """Armor shop: NPC menu"""
    """State 0,1: Menu: Start"""
    while True:
        """State 4: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_04_x13(z70=0, z71=220, z72=76100000, z73=0)
        if call.Get() == 2:
            """State 9: Armor shop: Menu conversation_SubState"""
            call = talk_m10_04_x100()
            if call.Done():
                continue
            elif GetEventFlag(102612) != 0 and (NpcMenuResult() == 19) != 0:
                """State 6: Bull: [Lib] Menu Cancel: General Purpose_SubState"""
                Label('L0')
                # talk:76103700:"Now, have some patience!"
                assert talk_m10_04_x15(text18=76103700)
            elif GetEventFlag(102611) != 0 and (NpcMenuResult() == 19) != 0:
                """State 5: Normal: [Lib] Menu canceled: General purpose _SubState"""
                Label('L1')
                # talk:76102200:"Finished already?"
                assert talk_m10_04_x15(text18=76102200)
            elif GetEventFlag(102610) != 0 and (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0 and GetEventFlag(102612) != 0:
            Goto('L0')
        elif call.Get() == 0 and GetEventFlag(102611) != 0:
            Goto('L1')
        elif call.Get() == 0 and GetEventFlag(102610) != 0:
            break
        elif call.Get() == 1 and GetEventFlag(102612) != 0:
            """State 8: Bull: [Lib] Menu Exit: General Purpose_SubState"""
            # talk:76103500:"Thanks for the purchase. Do come again.", talk:76103600:"Are you sure?\nWell...I may sell out while you're away."
            assert talk_m10_04_x14(text19=76103500, text20=76103600)
        elif call.Get() == 1 and GetEventFlag(102611) != 0:
            """State 7: Normal: [Lib] Menu exit: General purpose_SubState"""
            # talk:76102000:"Thanks very much.\nDo come again!", talk:76102100:"Always open for business."
            assert talk_m10_04_x14(text19=76102000, text20=76102100)
        elif call.Get() == 1 and GetEventFlag(102610) != 0:
            """State 3: Bearish: [Lib] Menu Exit: General Purpose_SubState"""
            # talk:76100400:"Thanks very much.\nAnd, do please come again.", talk:76100500:"Well, I, I do hope I see you again."
            assert talk_m10_04_x14(text19=76100400, text20=76100500)
        """State 10: End state"""
        Label('L2')
        return 0
    """State 2: Bearish: [Lib] Menu canceled: General purpose _SubState"""
    # talk:76100600:"Oh, is something wrong?"
    assert talk_m10_04_x15(text18=76100600)
    Goto('L2')

def talk_m10_04_x100():
    """Armor shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102612) != 0:
        """State 5: Armor shop: Menu conversation: Bull_SubState"""
        assert talk_m10_04_x103()
    elif GetEventFlag(102611) != 0:
        """State 4: Armor shop: Menu conversation: Normal _SubState"""
        assert talk_m10_04_x102()
    elif GetEventFlag(102610) != 0:
        """State 3: Armor shop: Menu conversation: Bearish_SubState"""
        assert talk_m10_04_x101()
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 6: End state"""
    return 0

def talk_m10_04_x101():
    """Armor shop: Menu conversation: Bearish"""
    """State 0,1: Menu conversation: Bearish: Start"""
    if GetEventFlag(204211) != 0:
        """State 4: Bearish: Menu conversation: 3_SubState"""
        # talk:76101100:"Hmm..."
        assert talk_m10_04_x1(text1=76101100, z63=0, z87=-1, z88=0)
    elif GetEventFlag(204210) != 0:
        """State 3: Bearish: Menu conversation: 2_SubState"""
        # talk:76101000:"A group calling themselves the Blue Sentinels\nhave gained much power in Volgen."
        assert talk_m10_04_x1(text1=76101000, z63=204211, z87=-1, z88=0)
    else:
        """State 2: Bearish: Menu conversation: Part 1_SubState"""
        # talk:76100900:"I came from the west, from Volgen."
        assert talk_m10_04_x1(text1=76100900, z63=204210, z87=-1, z88=0)
    """State 5: End state"""
    return 0

def talk_m10_04_x102():
    """Armor shop: Menu conversation: Normal"""
    """State 0,1: Menu conversation: Normal: Start"""
    # goods:1870000:Bluemoon Greatsword
    if GetEventFlag(204230) != 0 and GetEventFlag(204232) != 1 and (ItemCount(1870000, 1, 1, 0) > 1) != 0:
        """State 5: Normal: Menu conversation: Yuzuki's sword possession_SubState"""
        # talk:76102600:"That sword that you've got...\nMay I, um, have a look at it?"
        assert talk_m10_04_x1(text1=76102600, z63=204232, z87=-1, z88=0)
    elif GetEventFlag(204231) != 0:
        """State 4: Normal: Menu conversation: 3_SubState"""
        Label('L0')
        # talk:76102700:"I considered returning to my homeland,\nbut I've decided to stay a while longer."
        assert talk_m10_04_x1(text1=76102700, z63=0, z87=-1, z88=0)
    # goods:1870000:Bluemoon Greatsword
    elif GetEventFlag(204230) != 0 and (ItemCount(1870000, 1, 1, 0) > 1) != 0:
        Goto('L0')
    # goods:1870000:Bluemoon Greatsword
    elif GetEventFlag(204230) != 0 and (ItemCount(1870000, 1, 1, 0) > 1) != 1:
        """State 3: Normal: Menu conversation: Part 2: Satsuki's possession of swords_SubState"""
        # talk:76102500:"Have you seen that warrior\nlugging that giant blue sword about?"
        assert talk_m10_04_x1(text1=76102500, z63=204231, z87=-1, z88=0)
    else:
        """State 2: Normal: Menu conversation: Part 1_SubState"""
        # talk:76102400:"Did I mention before that\nI'm not from these parts?"
        assert talk_m10_04_x1(text1=76102400, z63=204230, z87=-1, z88=0)
    """State 6: End state"""
    return 0

def talk_m10_04_x103():
    """Armor shop: Menu conversation: Bullish"""
    """State 0,1: Menu conversation: Bullish: Start"""
    if GetEventFlag(102600) != 1 and (CurrentSouls() > 1) != 1 and GetEventFlag(104250) != 1:
        """State 3: Equipment transfer (condition: bullish and possession of soul is 0) _SubState"""
        # lot:1761000:Helm of Aurous, talk:76106000:"Did I mention I was...rich?"
        assert talk_m10_04_x26(lot8=1761000, z21=102600, text3=76106000, z22=0, z23=0)
    else:
        """State 2: Bull: Menu conversation: Part 1_SubState"""
        # talk:76103800:"I'm rich, I'm rich... Mwa hah hah!"
        assert talk_m10_04_x1(text1=76103800, z63=0, z87=-1, z88=0)
    """State 4: End state"""
    return 0

def talk_m10_04_x104():
    """Map writing: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203550) != 1:
        """State 6: Talk: First_SubState"""
        # talk:75100700:"Oh! Hello again!"
        assert talk_m10_04_x0(text16=75100700, z89=203550, z90=0)
    else:
        """State 4: Conversation: bonfire variable judgment"""
        if GetEventFlag(102405) != 0 and GetEventFlag(103651) != 1 and GetEventFlag(203551) != 1:
            """State 9: Talk to: Wandering Warrior: After moving to the empty forest: 1_SubState"""
            # talk:75101300:"Ah yes, there is something I wanted to tell you."
            assert talk_m10_04_x0(text16=75101300, z89=203551, z90=0)
            """State 10: Talk to: Wanderer Warrior: After moving to the empty forest: 2_SubState"""
            # talk:75101340:"And the other day...\nI saw a fellow with a striking likeness! And then!"
            assert talk_m10_04_x1(text1=75101340, z63=0, z87=-1, z88=0)
            """State 11: Talk to: Wandering Warrior: After moving to the empty forest: 3_SubState"""
            # talk:75101350:"And then... Wait..."
            assert talk_m10_04_x1(text1=75101350, z63=0, z87=-1, z88=0)
        elif (GetEventFlag(102470) != 1 and GetEventFlag(203570) != 0 and (GetGlobalVariable(201) > 8)
              != 0 and GetEventFlag(104180) != 1):
            """State 13: Equipment transfer (Condition: All fires are lit: 8): 1_SubState"""
            # talk:75106000:"That map...It's spellbinding..."
            assert talk_m10_04_x0(text16=75106000, z89=0, z90=0)
            """State 12: Equipment transfer (Condition: All fires lighted: 8): 2_SubState"""
            # lot:1751010:Cale's Helm
            assert talk_m10_04_x26(lot8=1751010, z21=102470, text3=75106010, z22=203571, z23=104020032)
        elif (GetGlobalVariable(201) > 8) != 0:
            """State 5: Conversation: Trophy acquisition: Flag setting"""
            SetEventFlag(105528, 1)
            assert GetEventFlag(105528) != 0
            """State 14: Talk: bonfire all lights: 1_SubState"""
            # talk:75101200:"It seems that all the flames have been lit."
            assert talk_m10_04_x0(text16=75101200, z89=203570, z90=0)
        elif (GetGlobalVariable(201) > GetAreaVariable(60)) != 1:
            """State 8: Talk to: The number of bonfires is increasing _SubState"""
            # talk:75101100:"Even more flames have appeared."
            assert talk_m10_04_x0(text16=75101100, z89=0, z90=0)
            """State 3: Conversation: Bonfire variable setting"""
            SetGlobalVariable(201, GetAreaVariable(60))
        else:
            """State 7: Map writing: Loop conversation_SubState"""
            assert talk_m10_04_x105()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 15: End state"""
    return 0

def talk_m10_04_x105():
    """Map writing: Loop conversation"""
    """State 0,1: Loop conversation: start"""
    if GetEventFlag(203562) != 0:
        """State 2: Loop conversation: Flag initialization"""
        SetEventFlag(203560, 0)
        SetEventFlag(203561, 0)
        SetEventFlag(203562, 0)
        """State 3: Talk: Part 1_SubState"""
        Label('L0')
        # talk:75100800:"Did you see the flame on the map?"
        assert talk_m10_04_x0(text16=75100800, z89=203560, z90=0)
    elif GetEventFlag(203561) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:75101000:"I would not venture far into that hole."
        assert talk_m10_04_x0(text16=75101000, z89=203562, z90=0)
    elif GetEventFlag(203560) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:75100900:"But there is something\ngreatly comforting about that flame."
        assert talk_m10_04_x0(text16=75100900, z89=203561, z90=0)
    else:
        Goto('L0')
    """State 6: End state"""
    return 0

def talk_m10_04_x106():
    """Cat: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if (GetPlayerHollowState() == 2) != 0 and GetEventFlag(205501) != 1 and GetEventFlag(205500) != 0:
        """State 5: Talk: Strong dead level_SubState"""
        # talk:77702700:"Hoh hoh! What's happened to you?"
        assert talk_m10_04_x42(text12=77702700, z46=205501, z47=10049030, z48=5)
    elif GetEventFlag(205500) != 0:
        """State 6: Cat: First conversation_SubState"""
        assert talk_m10_04_x125()
    else:
        """State 4: Talk: First_SubState"""
        # talk:77700000:"Oh...Undead, are we?"
        assert talk_m10_04_x42(text12=77700000, z46=205500, z47=10049030, z48=5)
    """State 3: Cat: NPC menu_SubState"""
    assert talk_m10_04_x107()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 7: End state"""
    return 0

def talk_m10_04_x107():
    """Cat: NPC menu"""
    """State 0,1,3: [Lib] Menu start: General purpose_SubState"""
    while True:
        call = talk_m10_04_x13(z70=0, z71=220, z72=77700000, z73=5)
        if call.Get() == 2:
            """State 5: Cat: Menu conversation_SubState"""
            call = talk_m10_04_x108()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 3:
            """State 6: Immoral Teacher: Cancel Menu Pledge_SubState"""
            call = talk_m10_04_x128()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0 and GetEventFlag(102083) != 0:
            pass
        elif call.Get() == 0:
            break
        elif call.Get() == 1 and GetEventFlag(102083) != 0:
            pass
        elif call.Get() == 1:
            """State 7: [Lib] Menu exit: Purchase flag_SubState"""
            # talk:77700100:"Satisfied?", talk:77700200:"Nothing suited you, I presume?"
            assert talk_m10_04_x48(text10=77700100, text11=77700200, z34=104020193)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuSelection()
        """State 8: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:77700300:"Oh my, haste makes waste. Hee hee hee..."
    assert talk_m10_04_x15(text18=77700300)
    Goto('L0')

def talk_m10_04_x108():
    """Cat: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(100972) != 0:
        """State 4: Menu conversation: Giant ’s Soul possession (single loop) _SubState"""
        # talk:77702330:"Honourable Sovereign, take your throne."
        assert talk_m10_04_x1(text1=77702330, z63=0, z87=3, z88=0)
    # goods:40510000:King's Ring
    elif (ItemCount(40510000, 1, 1, 0) > 1) != 0:
        """State 8: Cat: When holding a king's ring: Loop conversation_SubState"""
        assert talk_m10_04_x124()
    elif GetEventFlag(201700) != 0:
        """State 7: Cat: Menu conversation: Queen [Talking: Part 1] is ON: Loop conversation_SubState"""
        assert talk_m10_04_x123()
    elif GetEventFlag(102083) != 0:
        """State 6: Cat: Defeat 4 bosses: Loop conversation_SubState"""
        assert talk_m10_04_x122()
    else:
        """State 3: Cat: Menu conversation: Loop conversation_SubState"""
        assert talk_m10_04_x109()
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

def talk_m10_04_x109():
    """Cat: Menu conversation: Loop conversation"""
    """State 0,1: Loop conversation: start"""
    if GetEventFlag(205518) != 0:
        """State 2: Loop conversation: Flag initialization"""
        SetEventFlag(205510, 0)
        SetEventFlag(205511, 0)
        SetEventFlag(205512, 0)
        SetEventFlag(205517, 0)
        SetEventFlag(205518, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:77701000:"This place is already dead."
        assert talk_m10_04_x1(text1=77701000, z63=205510, z87=3, z88=0)
    elif GetEventFlag(205517) != 0:
        """State 11: Menu conversation: 9_SubState"""
        # talk:77701900:"Did you see that oddly-formed rock behind here?"
        assert talk_m10_04_x1(text1=77701900, z63=205518, z87=3, z88=0)
    elif GetEventFlag(205512) != 0:
        """State 10: Menu conversation: 8_SubState"""
        # talk:77701800:"Have you made friends with the man by the sea?"
        assert talk_m10_04_x1(text1=77701800, z63=205517, z87=3, z88=0)
    elif GetEventFlag(205511) != 0:
        """State 5: Menu conversation: 3_SubState"""
        # talk:77701200:"Are you going to see the Old Ones?"
        assert talk_m10_04_x1(text1=77701200, z63=205512, z87=3, z88=0)
    elif GetEventFlag(205510) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:77701100:"This place is fascinating."
        assert talk_m10_04_x1(text1=77701100, z63=205511, z87=3, z88=0)
    else:
        Goto('L0')
    """State 12: End state"""
    return 0

def talk_m10_04_x110():
    """Magician: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(204450) != 0:
        """State 5: [Lib] Conversation: Greeting: General purpose_SubState"""
        # talk:76302700:"Yes! How may I help you?", talk:76302800:"Hello! Do you require pyromancy?", talk:76302900:"Hello again! How have you been?", talk:76303000:"I'm glad to see you're well!"
        assert talk_m10_04_x11(z74=104020197, text21=76302700, text22=76302800, text23=76302900, text24=76303000)
    else:
        """State 4: Talk: First conversation: 1_SubState"""
        # talk:76302000:"Oh! There you are!"
        assert talk_m10_04_x0(text16=76302000, z89=0, z90=0)
        """State 7: Talk: First conversation: 2_SubState"""
        # talk:76302020:"You even were kind enough to clothe me.\nThank you so very much."
        assert talk_m10_04_x1(text1=76302020, z63=0, z87=-1, z88=0)
        """State 8: Talk: First conversation: 3_SubState"""
        # talk:76302030:"The only thing I can offer is pyromancy,\nbut if that might help you, come to me."
        assert talk_m10_04_x1(text1=76302030, z63=204450, z87=-1, z88=0)
        """State 3: Conversation: Set contact flag"""
        SetEventFlag(104020197, 1)
        assert GetEventFlag(104020197) != 0
    """State 6: Magician: NPC Menu_SubState"""
    assert talk_m10_04_x111()
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_04_x111():
    """Magician: NPC menu"""
    """State 0,1: Menu: Start"""
    while True:
        if GetEventFlag(104270) != 0:
            """State 7: [Lib] Menu start: Death_SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=76300001, z73=0)
            if call.Get() == 2:
                """State 6: Sorcerer: Menu conversation_SubState"""
                Label('L0')
                call = talk_m10_04_x112()
                if call.Done():
                    continue
                elif (NpcMenuResult() == 19) != 0:
                    break
            elif call.Get() == 1:
                """State 4: [Lib] Exit menu: General purpose_SubState"""
                Label('L1')
                # talk:76303100:"I'm always here,\nso come and see me when you're in town!", talk:76303200:"Be safe."
                assert talk_m10_04_x14(text19=76303100, text20=76303200)
            elif call.Get() == 0:
                break
        else:
            """State 3: [Lib] Menu start: General purpose_SubState"""
            call = talk_m10_04_x13(z70=0, z71=220, z72=76300000, z73=0)
            if call.Get() == 2:
                Goto('L0')
            elif call.Get() == 1:
                Goto('L1')
            elif call.Get() == 0:
                break
        """State 2: Menu: Exit"""
        Label('L2')
        """State 8: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:76303300:"Wait! Where are you...cough..."
    assert talk_m10_04_x15(text18=76303300)
    Goto('L2')

def talk_m10_04_x112():
    """Magician: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102722) != 0 and GetEventFlag(204800) != 0 and GetEventFlag(103801) != 1 and GetEventFlag(104302)
        != 1):
        """State 4: Sorcerer: Menu Conversation: Sorcerer Survival_SubState"""
        assert talk_m10_04_x119()
    else:
        """State 3: Sorcerer: Menu conversation: Sorcerer died _SubState"""
        assert talk_m10_04_x118()
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 5: End state"""
    return 0

def talk_m10_04_x113():
    """Dragon Miko: Menu: Est Bottle Strengthening"""
    """State 0,1: Est bottle reinforcement: start"""
    if EstusAtMaxStrength() != 0:
        """State 3: Est Bottle Strengthening Limit Dialog_SubState"""
        # action:1120:"Estus Flask at maximum strength"
        assert talk_m10_04_x19(action8=1120)
    elif (GetStateTime() > GetRandomValueForStateTime(0.1, 0.1)) != 0:
        """State 4: Est fragment transfer selection dialog_SubState"""
        # action:1200:"Give\n%s?", goods:60525000:Estus Flask Shard
        call = talk_m10_04_x31(action7=1200, goods2=60525000)
        # goods:60525000:Estus Flask Shard
        if call.Get() == 0 and (ItemCount(60525000, 1, 1, 0) > 1) != 1:
            """State 5: Est fragment shortage confirmation dialog_SubState"""
            # action:1206:"You do not have\n%s", goods:60525000:Estus Flask Shard
            assert talk_m10_04_x32(action6=1206, goods3=60525000)
        elif call.Get() == 0:
            """State 6: [Lib] Event action: Est bottle strengthening_SubState"""
            assert talk_m10_04_x43(z45=15)
            """State 7: Est bottle strengthening confirmation dialog_SubState"""
            # action:1119:"Estus Flask strengthened"
            assert talk_m10_04_x19(action8=1119)
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 2: Est bottle reinforcement: finished"""
    ClearNpcMenuSelection()
    assert (GetStateTime() > GetRandomValueForStateTime(0.1, 0.1)) != 0
    """State 8: End state"""
    return 0

def talk_m10_04_x114():
    """Dragon Miko: Menu: Level Up"""
    """State 0,1,3: Level up: Motion playback"""
    PlayerActionRequest(1)
    assert PlayerIsInEventAction(1) != 0 and (GetStateTime() > GetRandomValueForStateTime(2, 2)) != 0
    """State 4: Level up: Menu open"""
    OpenRespecMenu(0, 220, 1)
    assert (GetStateTime() >= 0) != 0
    """State 5: Level up: Menu: Waiting for input"""
    if RespecMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 7: Level up: Established"""
        SetEventFlag(104020148, 1)
        SetEventFlag(102181, 1)
        if GetEventFlag(104020) != 0:
            """State 10: Level Up: Dragon Miko: Death Anime: Wait"""
            PlayerActionRequest(-9999)
            assert (GetStateTime() > GetRandomValueForStateTime(2, 2)) != 0
        else:
            """State 8: Level up: Dragon Miko: Anime: Waiting"""
            PlayerActionRequest(-9999)
            assert ((CompareOwnEzStateFlag(6) == 19) != 0 and (GetStateTime() > GetRandomValueForStateTime(2,
                    2)) != 0)
        """State 9: Level Up: Dragon Miko: Anime: End"""
        SetEventFlag(104020148, 0)
    elif RespecMenuDisplay() != 1:
        pass
    """State 6: Level up: End of motion"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(1) != 1
    """State 2: Level up: Finish"""
    ClearNpcMenuSelection()
    """State 11: End state"""
    return 0

def talk_m10_04_x115():
    """Magician: Menu conversation: Magician not moved or died"""
    """State 0,1: Immortality: Start"""
    if GetEventFlag(204834) != 0:
        """State 2: Immortality: Initialization"""
        SetEventFlag(204830, 0)
        SetEventFlag(204831, 0)
        SetEventFlag(204832, 0)
        SetEventFlag(204833, 0)
        SetEventFlag(204834, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76602000:"The forces of magic, and souls, \nlie dormant in this land."
        assert talk_m10_04_x1(text1=76602000, z63=204830, z87=-1, z88=0)
    elif GetEventFlag(204833) != 0:
        """State 7: Menu conversation: No magician: 1_SubState"""
        # talk:76603200:"On my trip here, I met a strange\ngirl once or twice."
        assert talk_m10_04_x1(text1=76603200, z63=204834, z87=-1, z88=0)
    elif GetEventFlag(204832) != 0:
        """State 6: Menu conversation: 4_SubState"""
        # talk:76603500:"Sorcery was created long, long ago."
        assert talk_m10_04_x1(text1=76603500, z63=204833, z87=-1, z88=0)
    elif GetEventFlag(204831) != 0:
        """State 5: Menu conversation: 3_SubState"""
        # talk:76603400:"I sense a dark power here."
        assert talk_m10_04_x1(text1=76603400, z63=204832, z87=-1, z88=0)
    elif GetEventFlag(204830) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76602100:"Use scrolls to unleash\nthe power of sorceries."
        assert talk_m10_04_x1(text1=76602100, z63=204831, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 8: End state"""
    return 0

def talk_m10_04_x116():
    """Magician: Menu Conversation: Magician Emigration"""
    """State 0,1: Emigration: Start"""
    if GetEventFlag(204865) != 0:
        """State 2: Emigration: initialization"""
        SetEventFlag(204860, 0)
        SetEventFlag(204861, 0)
        SetEventFlag(204862, 0)
        SetEventFlag(204863, 0)
        SetEventFlag(204864, 0)
        SetEventFlag(204865, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76602000:"The forces of magic, and souls, \nlie dormant in this land."
        assert talk_m10_04_x1(text1=76602000, z63=204860, z87=-1, z88=0)
    elif GetEventFlag(204864) != 0:
        """State 8: [Group condition: Character] Judgment within player points"""
        # talk:76603600:"So, the girl's been here too."
        assert talk_m10_04_x1(text1=76603600, z63=204865, z87=-1, z88=0)
    elif GetEventFlag(204863) != 0:
        """State 7: Menu conversation: There is a magician: Part 1_SubState"""
        # talk:76603100:"Sorcery and pyromancy thrive in Melfia.\nI've spent much time there, trying to perfect my art."
        assert talk_m10_04_x1(text1=76603100, z63=204864, z87=-1, z88=0)
    elif GetEventFlag(204862) != 0:
        """State 6: Menu conversation: 4_SubState"""
        # talk:76603500:"Sorcery was created long, long ago."
        assert talk_m10_04_x1(text1=76603500, z63=204863, z87=-1, z88=0)
    elif GetEventFlag(204861) != 0:
        """State 5: Menu conversation: 3_SubState"""
        # talk:76603400:"I sense a dark power here."
        assert talk_m10_04_x1(text1=76603400, z63=204862, z87=-1, z88=0)
    elif GetEventFlag(204860) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76602100:"Use scrolls to unleash\nthe power of sorceries."
        assert talk_m10_04_x1(text1=76602100, z63=204861, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 9: End state"""
    return 0

def talk_m10_04_x117():
    """Magician: Menu Conversation: Death after moving to a magician"""
    """State 0,1: Death after migration: Start"""
    if GetEventFlag(204833) != 0:
        """State 2: Death after migration: initialization"""
        SetEventFlag(204830, 0)
        SetEventFlag(204831, 0)
        SetEventFlag(204832, 0)
        SetEventFlag(204833, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76602000:"The forces of magic, and souls, \nlie dormant in this land."
        assert talk_m10_04_x1(text1=76602000, z63=204830, z87=-1, z88=0)
    elif GetEventFlag(204832) != 0:
        """State 6: Menu conversation: 4_SubState"""
        # talk:76603500:"Sorcery was created long, long ago."
        assert talk_m10_04_x1(text1=76603500, z63=204833, z87=-1, z88=0)
    elif GetEventFlag(204831) != 0:
        """State 5: Menu conversation: 3_SubState"""
        # talk:76603400:"I sense a dark power here."
        assert talk_m10_04_x1(text1=76603400, z63=204832, z87=-1, z88=0)
    elif GetEventFlag(204830) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76602100:"Use scrolls to unleash\nthe power of sorceries."
        assert talk_m10_04_x1(text1=76602100, z63=204831, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_04_x118():
    """Sorcerer: Menu conversation: Sorcerer died"""
    """State 0,1,2: Menu conversation: 4_SubState"""
    # talk:76303600:"It was a perilous trek across the mountains."
    assert talk_m10_04_x1(text1=76303600, z63=0, z87=-1, z88=0)
    """State 3: End state"""
    return 0

def talk_m10_04_x119():
    """Sorcerer: Menu conversation: Sorcerer survival"""
    """State 0,1: Magician Survival: Start"""
    if GetEventFlag(204463) != 0:
        """State 2: Magician survival: initialization"""
        SetEventFlag(204460, 0)
        SetEventFlag(204461, 0)
        SetEventFlag(204462, 0)
        SetEventFlag(204463, 0)
        """State 3: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:76302200:"I finally tracked down my teacher."
        assert talk_m10_04_x1(text1=76302200, z63=204460, z87=-1, z88=0)
    elif GetEventFlag(204462) != 0:
        """State 6: Menu conversation: 4_SubState"""
        # talk:76303600:"It was a perilous trek across the mountains."
        assert talk_m10_04_x1(text1=76303600, z63=204463, z87=-1, z88=0)
    elif GetEventFlag(204461) != 0:
        """State 5: Menu conversation: 3_SubState"""
        # talk:76303500:"Once, Master Carhillion spoke\nexcitedly of this land."
        assert talk_m10_04_x1(text1=76303500, z63=204462, z87=-1, z88=0)
    elif GetEventFlag(204460) != 0:
        """State 4: Menu conversation: 2_SubState"""
        # talk:76303400:"Master Carhillion and I are from Melfia, to the south.\nA land lush with sorcery and pyromancy."
        assert talk_m10_04_x1(text1=76303400, z63=204461, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_04_x120():
    """Material shop: Menu conversation (blacksmith survival)"""
    """State 0,1: Menu conversation (blacksmith survival): Start"""
    if GetEventFlag(204355) != 0:
        """State 2: Menu conversation (blacksmith survival): initialization"""
        SetEventFlag(204351, 0)
        SetEventFlag(204353, 0)
        SetEventFlag(204354, 0)
        SetEventFlag(204355, 0)
        """State 7: Menu conversation (blacksmith survival): Part 1_SubState"""
        Label('L0')
        # talk:76201100:"These stones may look all the same,\nbut to the trained eye, each is unique."
        assert talk_m10_04_x1(text1=76201100, z63=204351, z87=-1, z88=0)
    elif GetEventFlag(204354) != 0:
        """State 6: Menu conversation (blacksmith survival): Part 5_SubState"""
        assert talk_m10_04_x1(text1=76205200, z63=204355, z87=-1, z88=0)
    elif GetEventFlag(204353) != 0:
        """State 4: Menu conversation (blacksmith survival): 4: 1_SubState"""
        assert talk_m10_04_x1(text1=76205100, z63=0, z87=-1, z88=0)
        """State 5: Menu conversation (blacksmith survival): Part 4: 2_SubState"""
        assert talk_m10_04_x1(text1=76205140, z63=204354, z87=-1, z88=0)
    elif GetEventFlag(204351) != 0:
        """State 3: Menu conversation (blacksmith survival): 3_SubState"""
        # talk:76205000:"Fine, if that's the way it is..."
        assert talk_m10_04_x1(text1=76205000, z63=204353, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 9: End state"""
    return 0

def talk_m10_04_x121():
    """Material shop: Menu conversation (blacksmith death)"""
    """State 0,1: Menu conversation (blacksmith survival): Start"""
    if GetEventFlag(204353) != 0:
        """State 2: Menu conversation (blacksmith survival): initialization"""
        SetEventFlag(204351, 0)
        SetEventFlag(204353, 0)
        """State 4: Menu conversation (blacksmith death): Part 1_SubState"""
        Label('L0')
        # talk:76201100:"These stones may look all the same,\nbut to the trained eye, each is unique."
        assert talk_m10_04_x1(text1=76201100, z63=204351, z87=-1, z88=0)
    elif GetEventFlag(204351) != 0:
        """State 3: Menu conversation (blacksmith death): Part 3_SubState"""
        # talk:76205000:"Fine, if that's the way it is..."
        assert talk_m10_04_x1(text1=76205000, z63=204353, z87=-1, z88=0)
    else:
        Goto('L0')
    """State 6: End state"""
    return 0

def talk_m10_04_x122():
    """Cat: Defeat 4 bosses: Loop conversation"""
    """State 0,1: Menu conversation: Defeat 4 bosses: Start"""
    if GetEventFlag(205524) != 0:
        """State 2: Menu conversation: When 4 bosses are defeated: Initialization"""
        SetEventFlag(205521, 0)
        SetEventFlag(205522, 0)
        SetEventFlag(205523, 0)
        SetEventFlag(205524, 0)
        """State 4: Menu conversation: When 4 bosses are destroyed: 2_SubState"""
        Label('L0')
        # talk:77701300:"Once, people tried to round up the Undead\nand hide them away from the world."
        assert talk_m10_04_x1(text1=77701300, z63=205521, z87=3, z88=0)
    elif GetEventFlag(205523) != 0:
        """State 7: Menu conversation: When 4 bosses are defeated: 5_SubState"""
        # talk:77701600:"Men develop the most peculiar fascinations."
        assert talk_m10_04_x1(text1=77701600, z63=205524, z87=3, z88=0)
    elif GetEventFlag(205522) != 0:
        """State 6: Menu conversation: When 4 bosses are destroyed: 4_SubState"""
        # talk:77701500:"You've seen that gaping hole here?"
        assert talk_m10_04_x1(text1=77701500, z63=205523, z87=3, z88=0)
    elif GetEventFlag(205521) != 0:
        """State 5: Menu conversation: When 4 bosses are destroyed: 3_SubState"""
        # talk:77701400:"Why do people try so hard to be beautiful?"
        assert talk_m10_04_x1(text1=77701400, z63=205522, z87=3, z88=0)
    else:
        Goto('L0')
    """State 8: End state"""
    return 0

def talk_m10_04_x123():
    """Cat: Queen [Talk: Part 1] is ON: Loop conversation"""
    """State 0,1: Menu conversation: Queen [Talk to: Part 1] is ON: Start"""
    if GetEventFlag(205534) != 0:
        """State 2: Menu conversation: Queen [Talking: Part 1] is ON: Initialization"""
        SetEventFlag(205531, 0)
        SetEventFlag(205532, 0)
        SetEventFlag(205533, 0)
        SetEventFlag(205534, 0)
        """State 3: Menu conversation: Queen [Talking: Part 1] is ON: Part 2_SubState"""
        Label('L0')
        # talk:77701300:"Once, people tried to round up the Undead\nand hide them away from the world."
        assert talk_m10_04_x1(text1=77701300, z63=205531, z87=3, z88=0)
    elif GetEventFlag(205533) != 0:
        """State 6: Menu conversation: Queen [Talking to: Part 1] is ON: Part 5_SubState"""
        # talk:77701600:"Men develop the most peculiar fascinations."
        assert talk_m10_04_x1(text1=77701600, z63=205534, z87=3, z88=0)
    elif GetEventFlag(205532) != 0:
        """State 5: Menu conversation: Queen [Talk to: 1] is ON: 4_SubState"""
        # talk:77701500:"You've seen that gaping hole here?"
        assert talk_m10_04_x1(text1=77701500, z63=205533, z87=3, z88=0)
    elif GetEventFlag(205531) != 0:
        """State 4: Menu conversation: Queen [Talking to: Part 1] is ON: Part 3_SubState"""
        # talk:77701400:"Why do people try so hard to be beautiful?"
        assert talk_m10_04_x1(text1=77701400, z63=205532, z87=3, z88=0)
    else:
        Goto('L0')
    """State 8: End state"""
    return 0

def talk_m10_04_x124():
    """Cat: When holding a king's ring: Loop conversation"""
    """State 0,1: Menu conversation: Defeat 4 bosses: Start"""
    if GetEventFlag(205544) != 0:
        """State 2: Menu conversation: When 4 bosses are defeated: Initialization"""
        SetEventFlag(205541, 0)
        SetEventFlag(205542, 0)
        SetEventFlag(205543, 0)
        SetEventFlag(205544, 0)
        """State 3: Menu conversation: When you have a king's ring: Part 2_SubState"""
        Label('L0')
        # talk:77701300:"Once, people tried to round up the Undead\nand hide them away from the world."
        assert talk_m10_04_x1(text1=77701300, z63=205541, z87=3, z88=0)
    elif GetEventFlag(205543) != 0:
        """State 6: Menu conversation: When you have a king's ring: Part 5_SubState"""
        # talk:77701600:"Men develop the most peculiar fascinations."
        assert talk_m10_04_x1(text1=77701600, z63=205544, z87=3, z88=0)
    elif GetEventFlag(205542) != 0:
        """State 5: Menu conversation: When you have a king's ring: Part 4_SubState"""
        # talk:77701500:"You've seen that gaping hole here?"
        assert talk_m10_04_x1(text1=77701500, z63=205543, z87=3, z88=0)
    elif GetEventFlag(205541) != 0:
        """State 4: Menu conversation: When holding a king's ring: Part 3_SubState"""
        # talk:77701400:"Why do people try so hard to be beautiful?"
        assert talk_m10_04_x1(text1=77701400, z63=205542, z87=3, z88=0)
    else:
        Goto('L0')
    """State 8: End state"""
    return 0

def talk_m10_04_x125():
    """Cat: First conversation"""
    """State 0,1: First conversation: branch"""
    if GetEventFlag(100972) != 0:
        """State 7: Before the last? About Throne_SubState"""
        # talk:77702300:"It seems that we must now part."
        assert talk_m10_04_x42(text12=77702300, z46=0, z47=10049030, z48=5)
    # goods:50910000:Ashen Mist Heart
    elif (ItemCount(50910000, 1, 1, 1) > 1) != 0:
        """State 6: After talking to the dragon, about the giant_SubState"""
        # talk:77702200:"Trespassing into their dreams?"
        assert talk_m10_04_x42(text12=77702200, z46=0, z47=10049030, z48=5)
    # goods:40510000:King's Ring
    elif (ItemCount(40510000, 1, 1, 1) > 1) != 0:
        """State 5: After obtaining the king's ring, _SubState"""
        # talk:77702100:"You'll find a great creature far to the east."
        assert talk_m10_04_x42(text12=77702100, z46=0, z47=10049030, z48=5)
    elif GetEventFlag(201700) != 0:
        """State 4: About the king's whereabouts_SubState"""
        # talk:77702000:"Oh, it's you."
        assert talk_m10_04_x42(text12=77702000, z46=0, z47=10049030, z48=5)
    elif GetEventFlag(102083) != 0:
        """State 3: Speak: After defeating 4 bosses (about the king) _SubState"""
        # talk:77701700:"Well, you've grown quite a bit, haven't you?"
        assert talk_m10_04_x42(text12=77701700, z46=0, z47=10049030, z48=5)
    else:
        """State 2: Talk: First time 2_SubState"""
        # talk:77700400:"Oh...Who were you again?"
        assert talk_m10_04_x42(text12=77700400, z46=0, z47=10049030, z48=5)
    """State 8: End state"""
    return 0

def talk_m10_04_x126():
    """Seisho Warrior: Emigration Count"""
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    if ConversationRequest() != 0 and GetEventFlag(203117) != 0:
        pass
    elif ConversationRequest() != 0:
        """State 5: Conversation: Immigration count: Start"""
        SetEventFlag(104020099, 1)
        """State 6: Conversation: Emigration count: Wait"""
        assert GetEventFlag(104020099) != 1
    """State 4: Conversation: Delete key guide"""
    DeleteKeyGuideArea()
    """State 7: Conversation: End"""
    return 0

def talk_m10_04_x127(val1=8, z1=-9999, lot1=2009000, z2=103100, action1=1337, action2=1347, z3=104020031):
    """Menu item: Make a pledge: Stone monument of strong man
    val1: Pledge name
    z1: Event action
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1: Menu pledge: start"""
    if (GetPlayerCovenant() == val1) != 0:
        """State 3: Confirm oath conclusion confirmation dialog_SubState"""
        # action:1305:"You already belong\nto this covenant"
        assert talk_m10_04_x19(action8=1305)
    else:
        """State 5: First choice_SubState"""
        # action:1360:"This will set you upon an arduous path.\nOkay to join this covenant?"
        call = talk_m10_04_x12(action1=1360)
        if call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
        elif call.Get() == 0:
            """State 6: Next choice_SubState"""
            # action:1361:"Are you prepared to join this covenant?"
            call = talk_m10_04_x12(action1=1361)
            if call.Get() == 1:
                pass
            elif call.Get() == 2:
                pass
            elif call.Get() == 0:
                """State 7: Pledge Conclusion: OBJ: Valuables_SubState"""
                call = talk_m10_04_x131(val1=val1, z4=9, lot1=lot1, z2=z2, action1=action1, action2=action2,
                                        z3=z3)
                if call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    pass
    """State 2: Menu pledge: End"""
    ClearNpcMenuSelection()
    """State 8: End state"""
    return 0

def talk_m10_04_x128():
    """Immaculate Teacher: Canceling Menu Pledge"""
    """State 0,1: Pledge cancellation: Start"""
    if (not GetPlayerCovenant()) != 0:
        """State 5: No pledge agreement confirmation dialog_SubState"""
        # action:1304:"No covenant to abandon"
        assert talk_m10_04_x19(action8=1304)
    elif (GetStateTime() > GetRandomValueForStateTime(0.1, 0.1)) != 0:
        """State 10: Menu: Discard Pledge: YES / NO Dialog_SubState"""
        # action:1302:"Abandon covenant?"
        call = talk_m10_04_x12(action1=1302)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 12: [Lib] OK dialog_SubState"""
            # action:1315:"Cannot abandon covenant\nwith phantom present"
            assert talk_m10_04_x19(action8=1315)
        elif call.Get() == 0:
            """State 4: Pledge cancellation: Pledge cancellation flag set"""
            SetEventFlag(104020193, 1)
            SetEventFlagIf((GetPlayerCovenant() == 1) != 0, 200900, 0)
            SetEventFlagIf((GetPlayerCovenant() == 2) != 0, 200901, 0)
            SetEventFlagIf((GetPlayerCovenant() == 3) != 0, 200902, 0)
            SetEventFlagIf((GetPlayerCovenant() == 4) != 0, 200903, 0)
            SetEventFlagIf((GetPlayerCovenant() == 5) != 0, 200904, 0)
            SetEventFlagIf((GetPlayerCovenant() == 6) != 0, 200905, 0)
            SetEventFlagIf((GetPlayerCovenant() == 7) != 0, 200906, 0)
            SetEventFlagIf((GetPlayerCovenant() == 8) != 0, 200907, 0)
            SetEventFlagIf((GetPlayerCovenant() == 9) != 0, 200908, 0)
            """State 2: Pledge cancellation: Execute pledge cancellation"""
            ChangePlayerCovenant(0)
            SaveExecution()
            assert (not GetPlayerCovenant()) != 0
            """State 6: Pledge cancellation production (general pledge conclusion motion) _SubState"""
            assert talk_m10_04_x20(z69=8)
            """State 11: Pledge cancellation success confirmation dialog_SubState"""
            # action:1303:"Abandoned covenant"
            assert talk_m10_04_x19(action8=1303)
        elif call.Get() == 2:
            pass
        elif call.Get() == 1:
            pass
    """State 3: Pledge cancellation: End"""
    ClearNpcMenuSelection()
    assert (GetStateTime() > GetRandomValueForStateTime(0.1, 0.1)) != 0
    """State 13: End state"""
    return 0

def talk_m10_04_x129():
    """Waiting for hostility: Dragon Miko"""
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 40)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 9) != 0 and GetEventFlag(104020136) != 1, 104020136, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 8) != 0 and GetEventFlag(104020179) != 1, 104020179, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 7) != 0 and GetEventFlag(104020178) != 1, 104020178, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 6) != 0 and GetEventFlag(104020177) != 1, 104020177, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 5) != 0 and GetEventFlag(104020176) != 1, 104020176, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 4) != 0 and GetEventFlag(104020168) != 1, 104020168, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 3) != 0 and GetEventFlag(104020167) != 1, 104020167, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(104020165) != 1, 104020165, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(104020164) != 1, 104020164, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 30 and GetRandomValue(0) < 40) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_04_x1(text1=70009420, z63=0, z87=-1, z88=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 30) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_04_x1(text1=70009410, z63=0, z87=-1, z88=0)
    elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_04_x1(text1=70009400, z63=0, z87=-1, z88=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_04_x130(z5=-9999, val1=8, lot1=2009000, z2=103100):
    """Event Action: Pledge: OBJ: Valuables
    z5: Event action
    val1: Pledge type
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    """
    """State 0,1: IventAction: Motion_Play"""
    PlayerActionRequest(z5)
    """State 2: IventAction: Motion_Waiting"""
    # goods:50940000:Champion's Tablet
    if (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0 and (ItemCount(50940000, 1, 1, 1) > 1) != 0:
        """State 5: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        # goods:50940000:Champion's Tablet
        if (ItemCount(50940000, 1, 1, 1) > 1) != 0:
            pass
        # lot:2009000:Champion's Tablet
        elif (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot1, 1) != 1 and GetEventFlag(z2) != 1:
            """State 6: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_04_x51(z32=1011, lot1=lot1)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    # lot:2009000:Champion's Tablet
    elif (GetEventFlag(z2) != 1 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0 and CanGetItemLot(lot1,
          1) != 1):
        Goto('L0')
    elif GetEventFlag(z2) != 0 and (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        Goto('L0')
    elif (GetStateTime() > GetRandomValueForStateTime(5, 5)) != 0:
        """State 4: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z2, 1)
        # lot:2009000:Champion's Tablet
        AwardItem(lot1, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 3,7: End state"""
    return 0

def talk_m10_04_x131(val1=8, z4=9, lot1=2009000, z2=103100, action1=1337, action2=1347, z3=104020031):
    """Pledge: OBJ: Valuables
    val1: Pledge type
    z4: Event action
    lot1: Item lottery ID
    z2: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z3: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z3, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_04_x12(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_04_x19(action8=1311)
        elif call.Get() == 0:
            """State 9: Event Action: Pledge: OBJ: Valuables_SubState"""
            Label('L1')
            assert talk_m10_04_x130(z5=-9999, val1=val1, lot1=lot1, z2=z2) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_04_x19(action8=1301)
            """State 11: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_04_x12(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_04_x29(val1=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 10: Suspended: End state"""
    return 0

