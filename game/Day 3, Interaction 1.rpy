label D3I1:

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"
    stop music fadeout 5.0

    """
    {color=#34B7EB}As I shuffle around the coffee shop, I hear a faint sound of bongos, snapping, and synchronized steps.

    {color=#34B7EB}It seems like they're crescendoing? What's going on? Suddenly a group of three people smoothly waltz in, snapping and walking in perfect step.
    """

    play music "mus_main_loop_cafejazz3.ogg" fadein 3.0
    play sound "sfx_room_footsteps_enter.ogg"
    show roberto neutral at Position(xalign=0.3, yalign=0.205) with dissolve
    show cynthia neutral at Position(xalign=0.0, yalign=0.205) with dissolve
    show bridget neutral at Position(xalign=0.6, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Hello there! Welcome to La Piovosita! What can I get for you?''"

    "{color=#34B7EB}The main leader of the fancily dressed possy speaks, while the other two continuously snap in tempo."

    URTO "{color=#e0e0e0}''Hey there Cool Cat. I really dig that name. Rolls off the tongue. Anyways, is this the best coffee shop in town?''"

    """
    {color=#34B7EB}The snapping intensifies and the bongos—where is that coming from—pick up the tempo.

    {color=#34B7EB}I feel like I'm being interrogated. I mean... what's the worst that can happen to me? But I feel as though I must answer carefully.
    """

    MAX "{color=#34B7EB}''Errrr.... it's the best it can be? I think the coffee here is splendid!''"

    "{color=#34B7EB}Gosh, I hope Laura doesn't kill me if I lose these customers. They lean forward and squint their eyes at me. The leader casually puts his arm on the counter."

    #The Beatniks speak one by one:

    show roberto inquire

    URTO "{color=#e0e0e0}''Good for lounging?''"

    show cynthia inquire

    UCYN "{color=#d4d4d4}''Atmospheric for some slam poetry?''"

    show bridget inquire

    UBGT "{color=#d4d4d4}''Groovy enough to boogie down?''"

    "{color=#34B7EB}I feel overwhelmed...I'll try to answer as best as I can."

    MAX "{color=#34B7EB}''Yes, yes, and maybe? I'll have to ask my manager—''"

    "{color=#34B7EB}The leader leans a little more and his glasses scoot down so I can see his steel gray eyes. They pierce through my soul."

    show roberto sans

    URTO "{color=#e0e0e0}''Focus your radio, man. If you make us some slammin coffee, we'll become your Gin mill cowboys and give you some of our good dollars. Capiche?''"

    "{color=#34B7EB}I'm stunned for a moment."
    "{color=#34B7EB}Is that slang he's using? And is he... is he making an ultimatum with me? I'll still appease them because well ...it's my job."

    MAX "{color=#34B7EB}''Okay... so um... what drink would you like?''"

    show roberto neutral

    URTO "{color=#e0e0e0}''Dark Sun.''"

    show cynthia neutral

    UCYN "{color=#d4d4d4}''Fly me to the Moon.''"

    show bridget neutral

    UBGT "{color=#d4d4d4}''Benny Goodman.''"

    "{color=#34B7EB}They walk back in step and shimmy their shoulders as they sit down to wait."
    "{color=#34B7EB}I'm a little perplexed if they'll like them or not. Guess I'll find out in a bit...maybe an intense bongo solo will play?"
    #*Coffee gameplay ensues*

    $ order = 1

    while makingdrink == 0:
        "{color=#34B7EB}Bongos aside, what did they want again? I think one was a Dark Sun..."
        #pause
    $ makingdrink = 0

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

    while makingdrink == 0:
        "{color=#34B7EB}Ok one down, next one was a Goodmoon? Wait, crap we dont serve that! Then what was it...?"
        #pause

    $ makingdrink = 0

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

    while makingdrink == 0:
        "{color=#34B7EB}Ok, then the last one was a Jhonny Moonman... or was it a fly me to Benny?"
        #pause

    $ makingdrink = 0
    $ order = 0

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

    MAX "{color=#34B7EB}''Here you go!''"

    """
    {color=#34B7EB}They eye me carefully and take their first sip.

    {color=#34B7EB}All three of them slip down their glasses and grin at me like I passed a test or something. All of them have steel gray eyes. The bongos tap at a rapid motion, creating tension in the air.
    """

    show roberto happy
    show cynthia happy
    show bridget happy

    URTO "{color=#e0e0e0}''These drinks threw babies out of the balcony, man. You've made us your official gin mill cowboys. We'll come back soon.''"

    "{color=#34B7EB}The two other girls wink at me in agreement and I feel a little pride. Should I be worried that my drinks can throw babies off balconies?"

    play sound "sfx_room_footsteps_exit.ogg"
    hide bridget with dissolve
    hide cynthia with dissolve
    hide roberto with dissolve
    play sound2 "sfx_room_door_main_close.ogg"
    stop music fadeout 3.0

    "{color=#34B7EB}They slide the money on the counter in union—change and extra tips—and smoothly walk and snap out of the café. The sound of the bongos get fainter as they disappear from my line of vision."

    jump D3I2
