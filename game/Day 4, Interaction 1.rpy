label D4I1:

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"
    stop music fadeout 5.0

    """
    {color=#34B7EB}A piano plays from a distance, playing a jazzy tune that makes me tap my foot in tempo.

    {color=#34B7EB}Who could be playing an instrument outside? Are they street performers? A thought popped in my head on the only people who could achieve the feat.

    {color=#34B7EB}The Beatniks.

    {color=#34B7EB}I see them walk in the café shimmying their shoulders and the leader does a spin and finalizes his move with an arm on the counter. He winks at me. Why is my heart beating so fast?
    """
    play music "mus_main_loop_cafejazz3.ogg" fadein 3.0
    play sound "sfx_room_footsteps_enter.ogg"
    show roberto neutral at Position(xalign=0.3, yalign=0.205) with dissolve
    show cynthia neutral at Position(xalign=0.0, yalign=0.205) with dissolve
    show bridget neutral at Position(xalign=0.6, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Welcome back! I see you've kept your promise, so what can I get for you?''"

    URTO "{color=#e0e0e0}''Hey there again good fellow, you sure are a shape in a drape. My crew and I wanna try some new drinks to freshen up our palettes. Gotta keep your mind open, ya dig? We don't want to stay in the cube ya know?''"

    "{color=#34B7EB}The two other girls in his possy nod in agreement. Did he just compliment me on my clothes? I mean, I wear the same attire every time I work. Is it my new deodorant? Do I smell different?"

    MAX "{color=#34B7EB}''Oh, sure thing! What kind of drink would you like? Sweet? Anything you would like to add?''"

    ALL "{color=#cccccc}''Surprise us.''"

    """
    {color=#34B7EB}They swiftly pay and turn around; they wait at a nearby table.

    {color=#34B7EB}Oh gosh, this is a predicament. I don't have much confidence in my skills like Ed, I'm still a trainee after all... I say a silent prayer to him, hoping for a boost.

    {color=#34B7EB}I pick three drinks from the coffee menu because, if I remember correctly, they all picked espressos last time. Hmmm ...I'll choose Deep Breath, The Entertainer, and The Dinkles—two simple drinks and one with a shot of energy.
    """
    $ order = 1
    while makingdrink == 0:
        "{color=#34B7EB}Alright, another big order, just need to take a deep breath and... make a Deep Breath."
        #pause

    $ makingdrink = 0

    if coffee == 1 and Milk == 1 and whip_cream == 1:
        $ thirdguy = 1
    elif Espresso == 1 or steam == 1 or Cinnamon == 1 or Chocolate == 1 or Pumpkin == 1 or foam == 1 or ExtraShot == 1 or creamer == 1 :
        $ thirdguy = 0

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
        "{color=#34B7EB}Thats one, next up, I should try making an Entertainer."
        #pause

    $ makingdrink = 0


    if coffee == 1 and Chocolate == 1 and ExtraShot == 1:
        $ secondguy = 1
    elif Espresso == 1 or Milk == 1 or Cinnamon == 1 or Pumpkin == 1 or foam == 1 or creamer == 0 or whip_cream == 1 or steam == 1:
        $ secondguy = 0

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
        "{color=#34B7EB}Two down, one dinkle to go. Is it still 'Dinkles' if there's just one?"
        #pause

    $ makingdrink = 0

    if coffee == 1 and Milk == 1 and whip_cream == 1:
        $ firstguy = 1
    elif Espresso == 1 or Cinnamon == 1 or Chocolate == 1 or Pumpkin == 1 or foam == 1 or ExtraShot == 1 or creamer == 1:
        $ firstguy = 0

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

    "{color=#34B7EB}I stand there and admiring my work, hoping they like it or tolerate it at least."
    if firstguy == 1 and secondguy == 1 and thirdguy == 1:
        "{color=#34B7EB}I hand Deep Breath and The Dinkles to the two girls, and I hand The Entertainer to the main leader. I wonder how it'll affect him?"


    show roberto happy

    URTO "{color=#e0e0e0}*takes a sip* ''Hot Damn! Isn't this the bees knees, this can throw a hundred babies out of the window! I feel alive!''"

    show roberto energy

    """
    {color=#34B7EB}He stands on a table and starts dancing to an upbeat piano tune. The girls stand in shock and they snap in support of him.

    {color=#34B7EB}They look back at me and give me a nonchalant thumbs up. Does that mean they like their drinks?

    {color=#34B7EB}But wow, I didn't expect that...I need to clean that table immediately.

    {color=#34B7EB}He hops from the table and bursts through the door; the girls follow suit, trying to catch up with him.
    """

    play sound "sfx_room_footsteps_exit.ogg"
    hide roberto with dissolve
    hide cynthia with dissolve
    hide bridget with dissolve
    play sound2 "sfx_room_door_main_close.ogg"
    stop music fadeout 3.0

    """
    {color=#34B7EB}He starts dancing with a random stranger to the beat of the music that's still coming from who knows where. The girls try to pry him off.

    {color=#34B7EB}That Espresso shot must've given him a hell of a boost.
    """


    jump D4I2
