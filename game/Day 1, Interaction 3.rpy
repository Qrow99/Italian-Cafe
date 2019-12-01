    label D1I3:

    # here is where the sound effects will go when they are made
    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_enter.ogg"

    "{color=#34B7EB}Soon, another figure enters the building. Her shifty eyes scan the room briefly before landing on a table near the counter. She moves in a slow, deliberate way, as though she were trying to avoid being seen, but her clothing does anything but blend in."

    show june neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Hello there! Welcome to La Piovositá!''"

    JUNE "{color=#4969de}''...''"

    """
    {color=#34B7EB}The girl hardly so much as shoots me a glance in response. I try to think of something to say, but come up with nothing.

    {color=#34B7EB}I never actually thought of what to do in a situation like this. Is it weird to have expected every customer who came in to actually order something?

    {color=#34B7EB}I guess the best thing I can do is keep up the good old service industry smile and hope she’ll give me something to work with.
    """

    MAX "{color=#34B7EB}''Can I get you anything, miss...?''"

    JUNE "{color=#4969de}''No.''"

    MAX "{color=#34B7EB}''Um, okay then.''"

    """
    {color=#34B7EB}Well, ‘no’ is technically something, but not really what I was hoping for.

    {color=#34B7EB}The girl then proceeds to take out a slim laptop and begin typing furiously. Between bouts of loud, mechanical clacking on her keyboard, she takes a few moments to look up and stare directly at me.

    {color=#34B7EB}I have no idea what to make of this. She goes through the pattern of typing, staring, and back to typing again enough times to make me so uncomfortable that I have to say literally anything just to break the tension.
    """

    MAX "{color=#34B7EB}''Are you sure you don’t want a drink?''"

    show june think

    "{color=#34B7EB}The girl continues to look down at her laptop, as if deaf to my question, but then after a few seconds she finally decides to respond."

    JUNE "{color=#4969de}''I want the Song of Seasons, and I want you to tell me how you made it.''"

    MAX "{color=#34B7EB}''Uh, sure thing? You want like directions, or...?''"

    show june neutral

    JUNE "{color=#4969de}''That would be nice, yes.''"

    "{color=#34B7EB}Alright, Song of Seasons. That should be pretty easy, but why ask for directions...?"

    while makingdrink == 0:
        "{color=#34B7EB}Alright, Song of Seasons. That should be pretty easy, but why ask for directions...?"
        pause

    $ makingdrink = 0

# here's where the drink making minigame is. Customer asks for Song of Seasons, but it doesn't matter what's made.
    if Pumpkin == 1 and foam == 1:
        jump interaction3good
    else:
        jump interaction3good

    label interaction3good:
    MAX "{color=#34B7EB}''Here’s your drink! Enjoy!''"

    show june angry

    "{color=#34B7EB}She walks up to the counter, snatches the drink, takes a meager sip, and then grimaces. It doesn’t look like she likes it, but she doesn’t complain, so I guess I can’t either?"

    show june neutral

    JUNE "{color=#4969de}''Alright, now how’d you make it?''"

    MAX "{color=#34B7EB}''Right, the directions!''"
    MAX "{color=#34B7EB}''Well, it’s honestly not too difficult; I just put some ground coffee into the machine and start heating up some milk. Then, once the coffee is done, I mix it with some pumpkin flavored creamer and top it off with the foam that forms at the top of the milk.''"

    show june inquire

    JUNE "{color=#4969de}''Okay... I see. What do you do with the rest of the milk?''"

    MAX "{color=#34B7EB}''Just save it for later. Not much else to do with it until someone else comes in.''"

    show june think

    JUNE "{color=#4969de}''Hm...''"

    """
    {color=#34B7EB}The girl resumes clacking on her keyboard silently, now spending the rare moments she looks up to inspect the coffee machine or her drink instead of myself, which gives me some relief.

    {color=#34B7EB}I wonder if Laura would get mad that I just nonchalantly gave away a recipe to a customer. Not like it’s a particularly complex or unorthodox way of making a drink, but still...

    {color=#34B7EB}It’s not like this random girl would be trying to gather trade secrets or special recipes or anything, right? That’s completely ludacris.

    {color=#34B7EB}There’s absolutely no way my actions could possibly cause the rise of a competitor that would rival our business just by showing some politeness, right!?
    """

    MAX "{color=#34B7EB}''Hey, you mind if I ask why you wanted to know how I made your drink?''"

    "{color=#34B7EB}For at least a solid ten seconds she didn’t respond, again appearing as if she hadn’t heard me. Though, once again, she eventually manages to get some words out."

    show june neutral

    JUNE "{color=#4969de}''It’s for a project.''"

    MAX "{color=#34B7EB}''What kind of project?''"

    show june angry

    JUNE "{color=#4969de}''You’re real pushy, you know that?''"

    MAX "{color=#34B7EB}''Oh, I’m sorry! I can back off, if you want me to.''"

    show june think

    JUNE "{color=#4969de}''...''"

    show june neutral

    JUNE "{color=#4969de}''I’m writing something. The main character is a barista at a coffee shop, but I don’t have a single clue what being a barista is actually like. So there.''"

    MAX "{color=#34B7EB}''Oh, that makes sense.
    Well hey, if you ever want to know anything about working in a café, I’d be happy to help! I mean, I’m pretty new at the whole barista thing, but I’d totally be willing to answer any questions you might have!''"

    show june inquire

    JUNE "{color=#4969de}''You would, huh? I might just take you up on that.''"

    MAX "{color=#34B7EB}''Anytime!''"

    show june neutral

    JUNE "{color=#4969de}''For now, though, I think I’m going to head home.''"

    MAX "{color=#34B7EB}''Alright then. Hope to see you back here soon!''"

    JUNE "{color=#4969de}''Yeah, alright.''"

    hide june with dissolve
    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_exit.ogg"
    python:
        coffee = 0
        Espresso = 0
        milk = 0
        Cinnamon = 0
        Chocolate = 0
        Pumpkin = 0
        pagenum = 0
        foam = 0
        espresso = 0
        creamer = 0
        whip_cream = 0
        steam = 0
    jump D1I4
