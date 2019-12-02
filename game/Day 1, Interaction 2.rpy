label D1I2:

    "{color=#34B7EB}My first customer bounds up to the coun-"

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"

    UAMC "{color=#ff7566}''HEEELLLLLOOOOOO''"
    """
    {color=#34B7EB}Her guttural greeting booms through the cafe, turning the heads of all the other patrons. The redhead in front of me is already vibrating with energy, despite the early morning hour. I brace yourself for whatever comes next.
    """
    play sound "sfx_room_footsteps_enter.ogg"
    show amecie happy at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Good morning! What can I get for yo-''"

    show amecie neutral

    UAMC "{color=#ff7566}''It IS a good morning! I just finished my first dance class and my teacher actually acknowledged me today!''"
    MAX "{color=#34B7EB}''That's good!''"

    show amecie happy

    UAMC "{color=#ff7566}''Yeah! She hit me!''"
    MAX "{color=#34B7EB}''Oh.''"
    "{color=#34B7EB}Your eyes follow the redhead's foot as she stretches her leg over her head, perpendicular to the ground."
    MAX "{color=#34B7EB}''Very impressive.''"
    "{color=#34B7EB}She gives an endearing smile and giggles."
    UAMC "{color=#ff7566}''Thank you! I'm practicing for my ballet class!''"
    MAX "{color=#34B7EB}''Did you want coffee or...?''"

    show amecie neutral

    UAMC "{color=#ff7566}''OH yeah can I have a Song of Seasons pretty please?''"
    MAX "{color=#34B7EB}''Of course, can I get a name?''"
    UAMC "{color=#ff7566}''Amnesty! But you can call me Nesty.''"
    "{color=#34B7EB}She winks and sticks her tongue out."
    MAX "{color=#34B7EB}''....Ok. Coming right up-''"
    AMC "{color=#ff7566}''I ALMOST FORGOT can you please add three espresso shots to that?''"
    "{color=#34B7EB}I blink, wondering if I heard her right."
    MAX "{color=#34B7EB}''Three... Espresso.... Shots...?''"

    show amecie happy

    """
    {color=#34B7EB}Amnesty laughs like a hyena, not answering my rhetorical question. Three shots might be too much considering her current energy level...
    """
    $ order = 1
    """
    {color=#34B7EB}Then again she probably knows her limits right? Right?? Time to make a Song of Seasons... with extra espresso.
    """
    while makingdrink == 0:
        "{color=#34B7EB}Then again she probably knows her limits right? Right?? Time to make a Song of Seasons... with extra espresso."
        #pause

    $ makingdrink = 0
    $ order = 0
    #Make it as she asks it, with extra shots
    if coffee == 1 and Pumpkin == 1 and foam == 1 and ExtraShot == 1:
        $ chichi = 1
        jump godwhy
    else:
        jump missingshot

    label godwhy:
    python:
        coffee = 0
        Espresso = 0
        Milk = 0
        Cinnamon = 0
        Chocolate = 0
        Pumpkin = 0
        foam = 0
        ExtraShot = 0
        creamer = 0
        whip_cream = 0
        steam = 0
        reset = 1
    "{color=#34B7EB}Against my better judgement, I make the drink – with as much espresso as I put in it."
    MAX "{color=#34B7EB}''Amnesty, I have your Song of Seasons with three espresso shots!''"
    AMC "{color=#ff7566}''Thank you so much!!''"
    "{color=#34B7EB}She takes a sip. Her pupils dilate. Vibration factor up to 11. I brace myself at the counter."
    AMC "{color=#ff7566}''OH YEAH. This is definitely enough to get me through my four hour chem lab!''"

    show amecie neutral

    AMC "{color=#ff7566} *GASP* ''I can even study for the midterm today!! AND IM READY FOR MY AUDITION!!! THANK YOU SO MUCH COFFEE QUEEN!!''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide amecie with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    "{color=#34B7EB}I accept her complement with a small wave. She bounces out of the cafe, leaving only a fiery red blur on her way out."
    jump D1I2END


    label missingshot:
    python:
        coffee = 0
        Espresso = 0
        Milk = 0
        Cinnamon = 0
        Chocolate = 0
        Pumpkin = 0
        foam = 0
        espresso = 0
        creamer = 0
        whip_cream = 0
        steam = 0
        reset = 1
    #Make it without an extra shot
    "{color=#34B7EB}I decide it's probably for the best not to fuel this fire."
    MAX "{color=#34B7EB}''Amnesty, I have your Song of Seasons with three espresso shots!''"
    AMC "{color=#ff7566}''Thank you so much!!''"

    show amecie angry

    "{color=#34B7EB}She takes a sip. And frowns."

    show amecie neutral

    AMC "{color=#ff7566}''Hmm maybe three just isn't enough. Guess I'll have to order more next time. See you later!''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide amecie with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    "{color=#34B7EB}She walks out of the cafe, a little more sluggish than before."
    jump D1I2END

    label D1I2END:

    jump D1Break
