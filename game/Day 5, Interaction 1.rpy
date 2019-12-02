    label D5I1:

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"
    stop music fadeout 5.0

    "{color=#34B7EB}What are the odds I can just happen upon something that could help me in this very specific situation?"

    play music "mus_main_loop_cafejazz10.ogg" fadein 3.0
    play sound "sfx_room_footsteps_enter.ogg"
    show june neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    JUNE "{color=#4969de}''Hey, get me a Cinna-monster would you? I went around and tried all the stuff you told me to. Turns out, cinnamon doesn’t taste all that bad.''"

    MAX "{color=#34B7EB}''Really? Well, I’m happy to hear it! One Cinna-monster coming right up!''"
    while makingdrink == 0:
        "{color=#34B7EB}I sure hope she isn’t expecting the cinnamon to cancel out the coffee completely, but I guess we’ll find out. One Cinna-monster it is!"
        #pause

    $ makingdrink = 0

    # Drink making goes here.
    # Doesn't matter what drink.

    MAX "{color=#34B7EB}''Here you go! Hope you actually like it!''"

    show june think

    JUNE "{color=#4969de}''Me too.''"

    MAX "{color=#34B7EB}''So, seeing as you’ve gone and done your research, have you gotten much farther in your writing?''"

    show june happy

    JUNE "{color=#4969de}''Yes I have. In fact, I’ve got the first few chapters already published online.''"

    MAX "{color=#34B7EB}''Chapters, huh? That reminds me, I never actually asked what you were writing about.''"

    show june think

    JUNE "{color=#4969de}''Well it’s, uh... just something I write online for fun. It’s a story about a game I like...''"

    MAX "{color=#34B7EB}''Oh, so like a fanfiction?''"

    show june inquire

    JUNE "{color=#4969de}''...Yes, actually. You seem pretty unfazed by it. Don’t you think it’s, I don’t know, weird?''"

    MAX "{color=#34B7EB}''I’ve got a couple of friends who are into that kind of stuff, so it’s pretty normal territory for me. I’d still like to give it a look, if you wouldn’t mind.''"

    JUNE "{color=#4969de}''You really want to know about my fanfic?''"

    MAX "{color=#34B7EB}''Yeah, sure! Actually, now that I think about it, you owe it to me! Said so yourself.''"

    show june think

    JUNE "{color=#4969de}''Well yeah, but I didn’t think you’d actually care...''"

    MAX "{color=#34B7EB}''Guess you thought wrong, then.''"

    show june happy

    JUNE "{color=#4969de}''Hmph. Fine. If you insist, I’ll give you a little summary and then give you the link.
    Gimme your phone for a second.''"

    play sound "sfx_room_typing_soft_single.ogg"

    "{color=#34B7EB}I unlock my phone and hand it to her. Her fingernails make a satisfying clicking sound as she stares at the screen, plinking away at it."

    show june think
    stop sound

    JUNE "{color=#4969de}''So it’s like... uh... how do I put it? Well, here’s a start; have you ever heard of 'Water Crest?'''"

    MAX "{color=#34B7EB}''You said it’s a video game, right? I think my brother might’ve talked about it once or twice.''"

    show june neutral

    JUNE "{color=#4969de}''Well, that’s what I’m writing about.''"

    MAX "{color=#34B7EB}''Does it have anything to do with working in a café?''"

    JUNE "{color=#4969de}''No, it’s actually a medieval strategy game... but it’s not meant to connect to the source material. It’s an alternate universe narrative.''"
    JUNE "{color=#4969de}''Like, all the characters and their personalities and relationships are pretty much the same, but it’s in modern times.''"
    JUNE "{color=#4969de}''And instead of fighting for the honor of their respective countries, the characters are fighting over who has to pay the tab.''"
    JUNE "{color=#4969de}''I’m mostly writing it because there are these two characters I really like, but they didn’t interact nearly enough in the game, so... yeah.''"

    MAX "{color=#34B7EB}''Ah, I see.''"

    """
    {color=#34B7EB}I don’t see, but honestly that really doesn’t matter. Taking my phone back from her, I find that the description she uses on the webpage doesn’t quite match up to the one she’s giving in front of me.

    {color=#34B7EB}I was expecting more of a comedy, slice of life sort of ordeal, but upon further inspection the contents of her story appear to be a bit more... saucy.
    """

    MAX "{color=#34B7EB}''Oh, is this a romance?''"

    show june think

    JUNE "{color=#4969de}''Yeah, sort of...
    It might be a little more, uh, intense...''"

    """
    {color=#34B7EB}Suddenly she blushes and stops talking altogether. I decide to ignore the implications of her actions in favor of pondering another possibility maybe this girl could be my ticket to getting some advice on how to help Ed!

    {color=#34B7EB}Not that I really think this strange, awkward girl has much experience in the realm of legitimate romance, but hey neither do I, so what’s the worst that could happen?
    """

    MAX "{color=#34B7EB}''A romance in a coffee shop, huh? There doesn’t happen to be a relationship between a barista and a customer, does there?''"

    show june neutral

    JUNE "{color=#4969de}''Well yeah, of course there is. It’s a staple of the subgenre.''"

    show june angry

    JUNE "{color=#4969de}''I hope you’re not implying anything.''"

    MAX "{color=#34B7EB}''What!? No, I didn’t mean anything like that!
    I’m just so curious, you know? How do two characters with seemingly completely different personalities and places in life end up interacting, even blossoming into close friends?''"

    show june neutral

    "{color=#34B7EB}She takes a moment to squint at me suspiciously, but nevertheless still indulges my admittedly easily misunderstandable question."

    JUNE "{color=#4969de}''Well, the customer just kind of talks to the barista, and over time they get to know each other. It’s not like one just up and immediately confesses their love for the other. That’d be really weird.''"

    MAX "{color=#34B7EB}''Just getting up and talking to each other? Nothing fancy or extravagant?''"

    JUNE "{color=#4969de}''I don’t know how you usually talk to people, but yeah. It’s pretty mundane.''"

    MAX "{color=#34B7EB}''I see. Well, I’ll look forward to reading about it, then!''"

    show june happy

    JUNE "{color=#4969de}''I’m glad someone does...
    Hey, I should get going here, but thanks for helping me out with my fanfic. You’re a weird barista, but I’ve enjoyed coming in here.''"

    MAX "{color=#34B7EB}''Of course! I’m always happy to help!''"

    show june neutral

    JUNE "{color=#4969de}''Yup, you really are weird.
    Oh, one last thing; if you really do intend on reading what I wrote, maybe consider not doing it in a public place. See you.''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide june with dissolve
    play sound2 "sfx_room_door_main_close.ogg"
    stop music fadeout 3.0
    
    "{color=#34B7EB}I’m not going to think too hard about what that might mean."

    jump D5I2
