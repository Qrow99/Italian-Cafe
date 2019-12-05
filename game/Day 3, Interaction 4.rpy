    label D3I4:

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"

    "{color=#34B7EB}Amnesty, everyone's favorite dancing chemist parking attendant, dances her way into the cafe and up to the counter. I can see her impeccable eyeshadow."

    play music "mus_main_loop_cafejazz9.ogg" fadein 3.0
    play sound "sfx_room_footsteps_enter.ogg"
    show amecie happy at Position(xalign=0.3, yalign=0.205) with dissolve

    AMC "{color=#ff7566}''How's it going Coffee Queen!''"
    MAX "{color=#34B7EB}''Not too bad, what about you?''"
    AMC "{color=#ff7566}''We just performed the best dance routine, choreographed by yours truly, of course!''"
    "{color=#34B7EB}She does a pirouette. I applaud."
    MAX "{color=#34B7EB}''Looks like you did a great job! Can I get you anything?''"
    AMC "{color=#ff7566}''We ALL did great! I'd like to order four Song of Seasons! Can you put espresso shots in mine though? Surprise me!''"

    $ order = 1

    "{color=#34B7EB}She winks. Well, no way to mess this one up. Time to make some coffee!"

    #here's where the coffee's made

    while makingdrink == 0:
        "{color=#34B7EB}She winks. Well, no way to mess this one up. Time to make some coffee!"
        #pause

    $ makingdrink = 0
    $ order = 0

    if coffee == 1 and Pumpkin == 1 and foam == 1 and ExtraShot == 1 :
        "{color=#34B7EB}Ok! Four seasons, sounds about right."
    elif Espresso == 1 or Milk == 1 or Cinnamon == 1 or Chocolate == 1 or creamer == 1 or whip_cream == 1 or steam == 1:
        "{color=#34B7EB}Ok I think thats right? Only one way to find out..."

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

    MAX "{color=#34B7EB}''Amnesty, I have your four coffees!''"

    show amecie neutral

    AMC "{color=#ff7566}''Thank you so much!!''"
    MAX "{color=#34B7EB}''This one has the shots.''"

    show amecie happy

    AMC "{color=#ff7566}''Ooo thanks! Hey, did you want to see part of my performance?''"
    "{color=#34B7EB}I look at the few customers behind her in line."
    MAX "{color=#34B7EB}''Sorry, but I have to take these orders.''"

    show amecie neutral

    AMC "{color=#ff7566}''That's ok, maybe next time. Thanks for the drinks! And remember to follow my MUA Instagram @red.ysetbeauty #ad #sponsored ;)''"
    "{color=#34B7EB}I wonder why she said 'semicolon, close parenthesis.' Must be an influencer thing."

    play sound "sfx_room_footsteps_exit.ogg"
    hide amecie with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    "{color=#34B7EB}I prepare to take the orders of the small line that was forming behind her, but they all leave the building along with her. Guess I could've seen her performance after all."


    jump D3Outro
