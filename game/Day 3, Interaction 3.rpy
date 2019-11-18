    label D3I3:

    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_enter.ogg"

    "{color=#34B7EB}Looking up, I’m met with a familiar, suspicious scowl. Unlike our previous encounter, though, the mysterious writer wastes no time in giving me her order."

    show june neutral at Position(xalign=0.3, yalign=0.22) with dissolve

    JUNE "{color=#4969de}''Hey you, what on the menu here has the least amount of flavor?''"

    MAX "{color=#34B7EB}''The least...? You mean like nothing but coffee or no flavor at all?''"

    JUNE "{color=#4969de}''The smallest amount of coffee you can reasonably conceive.''"

    MAX "{color=#34B7EB}''Well let’s see, Fly Me to the Moon is just an Americano, so not too much flavor there, and the Dinkles has a lot of milk, so it’s probably got the weakest coffee flavor.
    I could also get you a nice hot cup of tap water, if you’d prefer that.''"

    "{color=#34B7EB}I crack a cheesy smile and strike an inviting pose, but get no reaction. Perhaps this was the wrong customer to test my comedy routine on."

    show june angry

    JUNE "{color=#4969de}''Just the Dinkles or whatever you call it is fine.''"

    MAX "{color=#34B7EB}''Okay, coming right up.''"
    while makingdrink == 0:
        "{color=#34B7EB}Man, that was a terrible joke. Maybe I should just stick to being a normal, non-comedic barista... Regardless, I guess I’d better start making a Dinkles."
        pause
    $ makingdrink = 0

# here's the drink. The order is the Dinkles.
    if coffee == 1 and Milk == 1 and steamedMilk == 1:
        jump d3i3good
    else:
        jump d3i3bad

    MAX "{color=#34B7EB}''Here you go! Enjoy!''"

    show june neutral

    JUNE "{color=#4969de}''I’ll try my best.''"

    show june angry


    # if drink is correct
    label d3i3good:
    """
    {color=#34B7EB}She picks up her cup and takes a large swig, keeping it in her mouth with puffed up cheeks. Her face scrunches up into a painful, red wince as she slowly gulps down the large mouthful she took.

    {color=#34B7EB}She then proceeds to take out her laptop and begin taking notes as she had last time, but the discomfort on her face lasts long after she finishes drinking.
    """
    jump d3i3converge

    # if drink is incorrect
    label d3i3bad:
    """
    {color=#34B7EB}She picks up her cup and takes a large swig, keeping it in her mouth with puffed up cheeks. Her face turns a bright red and she proceeds to spit the whole mouthful back into her cup, wincing and breathing heavily.

    {color=#34B7EB}She then proceeds to take out her laptop and begin taking notes as she had last time, but the discomfort on her face lasts long after she finishes drinking.
    """
    jump d3i3converge

    # both options come back here
    label d3i3converge:
    MAX "{color=#34B7EB}''So... how is it?''"

    show june neutral

    JUNE "{color=#4969de}''It’s fine. I just hate coffee.''"

    MAX "{color=#34B7EB}''You hate coffee? Then why even order it?''"

    JUNE "{color=#4969de}''I had to figure out the taste somehow... Can’t really describe the taste of something I don’t drink.''"
    JUNE "{color=#4969de}''Anyways, can you go throw the rest of this away and make me a Benny Goodman? In the meantime, I’m going to grab my wallet.
    Make it fast, too. We’ve got a long menu to get through.''"

    MAX "{color=#34B7EB}''Hold on, you’re not thinking of ordering everything on the menu, are you?''"

    JUNE "{color=#4969de}''Maybe not today, but if all goes to plan I’ll have notes on the taste of every basic coffee drink by the end of next week.''"

    MAX "{color=#34B7EB}''Next week!? Not to question your methods, but have you considered that maybe there’s a better option?''"

    show june inquire

    JUNE "{color=#4969de}''Why would I need another option?''"

    MAX "{color=#34B7EB}''For the sake of your wallet. Also your heart. Maybe your taste buds too, if the whole ‘hating coffee’ thing hasn’t changed in the past five minutes.''"

    JUNE "{color=#4969de}''You have any better ideas?''"

    MAX "{color=#34B7EB}''At least one. How about this: I’m relatively experienced when it comes to the flavors of coffee, so why don’t I just tell you what different drinks taste like? Probably saves a lot of time and suffering on your part.''"

    show june neutral

    JUNE "{color=#4969de}''If I just wanted to know what it basically tasted like, I could’ve asked anyone. It’s not the same as tasting it for yourself...''"

    MAX "{color=#34B7EB}''I don’t really understand what you mean, but okay.
    What do you have written down so far? Maybe I can at least help verify what you already have.''"

    show june think

    JUNE "{color=#4969de}''Well for pumpkin spice, cappuccinos, and heavily diluted coffee, my notes mark the taste down as... ‘bad.’''"

    MAX "{color=#34B7EB}''I see... Well, if you really want to know what this stuff tastes like for yourself, then maybe this’ll help...''"

    """
    {color=#34B7EB}I take a copy of the menu from the counter and begin to heavily vandalize it. For each item on the menu, I write down next to it a common grocery item that has the same basic flavor.

    {color=#34B7EB}For the Benny Goodman, I write down my favorite chocolate bar. For the One Sweet Day, I just write down the creamer we use in house. So on and so forth. After finishing my destruction of a perfectly good menu, I hand it to her.
    """

    MAX "{color=#34B7EB}''Here. All of these things should have about the sort of flavor you’re looking for, coffee not included. Maybe consider changing your notes from ‘bad’ to ‘bitter’ and you’ve probably got a good enough idea of what to write about.''"

    show june inquire

    JUNE "{color=#4969de}''Wow, thanks. Why are you doing all this for me, anyways? What’s in it for you, huh?''"

    MAX "{color=#34B7EB}''Well you see, uh... I don’t know. Guess I just hate to see someone spend so much time doing something they don’t want to do?''"

    show june neutral

    JUNE "{color=#4969de}''Sounds like a bunch of crap, but whatever. I should probably get going anyways.
    You sure you don’t want anything for this? Not even like a tip or something?''"

    MAX "{color=#34B7EB}''Not having to make everything on the menu is its own reward, but maybe you could show me what you’re writing when it’s done? If I’m going to be helping you this much, I want to at least know what it’s for.''"

    JUNE "{color=#4969de}''You actually want to read it? Alright, it’s a deal then. See you later.''"

    hide june with dissolve
    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_exit.ogg"

    jump D3I4
