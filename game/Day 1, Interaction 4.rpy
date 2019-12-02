    label D1I4:

    """
    {color=#34B7EB}I patiently wait at the counter and I suddenly hear a loud clanging outside.
    """
    play music "mus_main_loop_cafejazz5.ogg" fadein 3.0
    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"

    """
    {color=#34B7EB}A blonde girl carrying a large metal water bottle and wearing a bright, purple backpack that looks like it was meant especially for Swedish kindergarteners bursts into the coffee shop.

    {color=#34B7EB}She walks in there with purpose like she was on a mission. She's glued on to her phone, almost running into a chair and table, and says 'and I Oop' in response.
    """

    play sound "sfx_room_footsteps_enter.ogg"
    show sahbreena neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    """
    {color=#34B7EB}As she gets to me, she slams her gigantic bottle onto the counter. I practically flinch in fear. She shines me a bright smile, showing off her colorful braces.

    {color=#34B7EB}As she begins to talk, I feel myself begin to shake and stutter my speech.
    """

    MAX "{color=#34B7EB}''H-hi, h-how are you? What would you like to order today?''"

    show sahbreena happy

    SBNA "{color=#fa9def}''Hiiiiiiiiii, first of all, I'm doing great, I just made new scrunchies with my girlies and I just got a new holographic metal straw that I can't wait to uuseeeeee.''"

    show sahbreena angry

    SBNA "{color=#fa9def}''Does your shop sell metal straws? If you don't, I'm going to call my girlies and we're gonna blast you on social mediaaaa—''"

    MAX "{color=#34B7EB}''Ma'am—''"

    show sahbreena happy

    SBNA "{color=#fa9def}''What? Oh, sorry, I just get so passionate about the turtles. Because they're dying and all that. Anyways, can I get the Dinkles with creamer and loaadsksksk of whipped cream? And put in my reusable coffee cup, pretty pleaseee?''"

    "{color=#34B7EB}She takes out a giant glass reusable coffee cup covered in stickers and puka shells. I'm overwhelmed with the situation, but I appreciate her passionate effort to help out the environment."

    MAX "{color=#34B7EB}''Oh sure thing, can I get a name for the order?''"

    SBNA "{color=#fa9def}''Sure thingggg, Sahbreena. S-A-H-B-R-E-E-N-A. You got it?''"

    "{color=#34B7EB}She speaks in lightning speed; I try to spell it as best as I can and wonder why her name is so weirdly spelled."

    MAX "{color=#34B7EB}''Yeah, I got it. Your order will be ready in a few minutes.''"

    "{color=#34B7EB}She's immediately on her phone, typing away and updating her friends about getting coffee on every social media she has, and responds without even looking at me."

    show sahbreena neutral

    SBNA "{color=#fa9def}''Thanksksksksks a bunchhhh.''"

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_exit.ogg"
    hide sahbreena with dissolve

    "{color=#34B7EB}She walks away, almost tripping on a discarded paper straw in the process."

    $ order = 1

    "{color=#34B7EB}Anyways, she said the Dinkles with whipped cream, right? That shouldn't be too hard..."
    while makingdrink == 0:
        "{color=#34B7EB}Anyways, she said the Dinkles with whipped cream, right? That shouldn't be too hard..."
        #pause

    $ makingdrink = 0
    $ order = 0

    # Coffee gameplay ensues. Correct drink is the Dinkles.

    if coffee == 1 and Milk == 1 and whip_cream == 1 and steam == 1:
        jump D1I4GOOD
    elif Espresso == 1 or Cinnamon == 1 or Chocolate == 1 or Pumpkin == 1 or foam == 1 or ExtraShot == 1 or creamer == 1:
        jump D1I4BAD

    # Bad outcome:
    label D1I4BAD:
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

    MAX "{color=#34B7EB}''Order for Sahbreena? Your drink is ready!''"

    "{color=#34B7EB}She bolts upright from her chair like an excited puppy and lets out the phrase 'AnD I OoP!' before walking over to the counter and getting her drink."

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_enter.ogg"
    show sahbreena happy at Position(xalign=0.3, yalign=0.205) with dissolve

    SBNA "{color=#fa9def}''Wooowwww, Thanksksksksk a bunch! You didn't damage any of my stickers and shells, and you put a lot of whipped cream just like I asked you too!''"

    MAX "{color=#34B7EB}''It's practically bursting out of your cup.''"

    SBNA "{color=#fa9def}''Just the way I like it!''"

    "{color=#34B7EB}The whipped cream is overflowing out of the straw hole. Sahbreena is licking at it like a feral animal. But after a moment, she stops. She squints down at her cup, and then back at me, and then she bursts into a frenzy."

    show sahbreena angry

    SBNA "{color=#fa9def}''Hey! This isn't right! You messed up my drinksksksksksk!''"

    MAX "{color=#34B7EB}''I did!? I'm so sorry! Do you want me to get you another one...?''"

    """
    {color=#34B7EB}I begin to offer her a replacement drink, but I am not allowed such a luxury.

    {color=#34B7EB}Before I can get the offer out of my mouth, Sahbreena starts making some weird hissing noise, like that of a caffeinated snake.
    """

    SBNA "{color=#fa9def}''Sksksksksksks!
    Do you just hate the environment!? Is that it!? You skskskskskscum!?''"

    MAX "{color=#34B7EB}''What? No! Is that even relevant...?''"

    SBNA "{color=#fa9def}''Sksksksksksksksksksk!''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide sahbreena with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    """
    {color=#34B7EB}From the looks of it, she doesn't hear me. In fact, it doesn't seem like she notices much at all. Drink in hand, Sahbreena walks out the door in a fuss, nearly tripping on a a misaligned floor tile on her way out.

    {color=#34B7EB}All the while, that weird tongue clicking noise refuses to stop emitting itself from her mouth.
    """

    jump D1Outro

    # Good outcome:
    label D1I4GOOD:

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

    MAX "{color=#34B7EB}''Order for Sahbreena? Your drink is ready!''"

    "{color=#34B7EB}She bolts upright from her chair like an excited puppy and lets out the phrase 'AnD I OoP!' before walking over to the counter and getting her drink."

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_enter.ogg"
    show sahbreena happy at Position(xalign=0.3, yalign=0.205) with dissolve

    SBNA "{color=#fa9def}''Wooowwww, Thanksksksksk a bunch! You didn't damage any of my stickers and shells, and you put a lot of whipped cream just like I asked you too!''"

    MAX "{color=#34B7EB}''It's practically bursting out of your cup.''"

    SBNA "{color=#fa9def}''Just the way I like it!''"

    "{color=#34B7EB}The whipped cream is overflowing out of the straw hole. Sahbreena is licking at it like a feral animal. Suddenly she stops, and begins staring at my name tag."

    show sahbreena neutral

    SBNA "{color=#fa9def}''...Max, huh?'' *gasps* ''O.M.G. You have the same name as one of my girlfriend's—her name is Bhriteney, btw—dog, Max!''"

    MAX "{color=#34B7EB}''...Cool. It's a common name.''"

    "{color=#34B7EB}From the sound of her tone, I should feel special but I don't."

    show sahbreena happy

    SBNA "{color=#fa9def}''So, as thanks for giving me the perfect drinkieeee, I'll give you a scrunchie with 'Max' embroidered on it!''"

    show sahbreena angry

    SBNA "{color=#fa9def}''It was supposed to be for Bhriteney's dog, but I never liked her anyways, her name is spelled all weird and she doesn't have a real hydro flasksksks.''"

    show sahbreena neutral

    SBNA "{color=#fa9def}''It's fake. Like her. You didn't hear that from me though. Anywaysksks, Byeeeee! Toodles!''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide sahbreena with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    "{color=#34B7EB}With lightning speed, she's gone, almost tripping on nothing whatsoever. I think the scrunchie is a good omen, and I wear it on my wrist. It radiates with chaotic energy."

    jump D1Outro
