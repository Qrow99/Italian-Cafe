    label D2I2:

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"

    "{color=#34B7EB}The energetic redhead is back, looking less energetic and more worse for wear. Yikes."

    play sound "sfx_room_footsteps_enter.ogg"
    show amecie angry at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''How are you doing today?''"

    if chichi == 0:
        jump chichisad

    #Got previous order right:
    AMC "{color=#ff7566}''Really tired. Work sucks, am I right?''"
    "{color=#34B7EB}She opens her jacket to reveal a parking attendant badge. My boss looks over and locks eyes with me."
    MAX "{color=#34B7EB}''I am legally obligated to say I'm having a good time.''"

    show amecie happy

    "{color=#34B7EB}Amnesty laughs her hyena laugh."
    AMC "{color=#ff7566}''Glad to hear it. Can I have a Song of Seasons with one espresso shot?''"
    MAX "{color=#34B7EB}''Just the one? You sure?''"

    show amecie neutral

    AMC "{color=#ff7566}''Yeah, I already did my midterm, which I think I did pretty good on, so just the one is good enough.''"
    MAX "{color=#34B7EB}''Congrats! One Song of Seasons coming right up!''"

    $ order = 1

    "{color=#34B7EB}I make the drink. Song of Seasons isn't too complicated."
    #(No change in interaction if you get it wrong.)
    while makingdrink == 0:
        "{color=#34B7EB}I make the drink. Song of Seasons isn't too complicated."
        #pause

    $ makingdrink = 0
    $ order = 0
    if chichi == 1:
        jump chichihappy
    else:
        jump chichisad
    MAX "{color=#34B7EB}''Amnesty, I have your Song of Seasons with one espresso shot!''"
    label chichihappy:
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
    show amecie happy

    AMC "{color=#ff7566}''Thanks! Hey I forgot to tell you! My audition went really well, and my friends and I are in the dance show tomorrow night! Do you want to come?''"
    MAX "{color=#34B7EB}''I'd love to, but I'm working tomorrow.''"
    AMC "{color=#ff7566}''Awww that's ok, I'll come visit after!''"
    MAX "{color=#34B7EB}''Can't wait! See you then!''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide amecie with dissolve
    play sound2 "sfx_room_door_main_close.ogg"
    jump D2Break

    #If you got the last drink wrong

    label chichisad:
    AMC "{color=#ff7566}''Life sucks. I did bad on my midterm, didn't get in to the dance show, and worst of all, I have work right now! I just need a pick me up.''"
    "{color=#34B7EB}My guilty conscience weighs me down."
    MAX "{color=#34B7EB}''I'm sorry to hear that. Can I get you anything?''"

    show amecie neutral

    AMC "{color=#ff7566}''Yeah, I'll have a Song of Seasons with 5 espresso shots.''"
    "{color=#34B7EB}Now that's what I call life threatening. As the barista of this establishment, I do not want to be responsible for the caffeine shock induced death of the nice redhead in front of you."
    MAX "{color=#34B7EB}''I'm afraid I can't give you five shots.''"

    show amecie angry

    AMC "{color=#ff7566}''C'mon!! Please???''"
    MAX "{color=#34B7EB}''Cafe policy. Sorry, it's too dangerous.''"
    AMC "{color=#ff7566}''Ugh, fine.''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide amecie with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    "{color=#34B7EB}Amnesty storms off. I feel really bad. Maybe I should have listened to her the first time, huh?"


    jump D2Break
