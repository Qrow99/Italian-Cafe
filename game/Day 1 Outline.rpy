    label DAY1:


# Despite just being the outline, both days 1 and 5 will contain drink making
# sections in them, just a heads up.


    show black box at Position(xalign=0, yalign=0)
    show ed neutral behind black at Position(xalign=0.3, yalign=0.22)

    ED "{color=#EBB134}''Today’s the day, Max. Think you’re ready?''"

    MAX "{color=#34B7EB}''Sure, yeah, I think so!
    But, uh, can you remind me again what today is?''"

    ED "{color=#EBB134}''It’s Monday.''"

    MAX "{color=#34B7EB}''Right... Which means...?''"

    ED "{color=#EBB134}''Your training’s over.''"

    MAX "{color=#34B7EB}''And...?''"

    ED "{color=#EBB134}''It’s your first day alone.
    You’re not my assistant anymore. Today...''"

    hide black box with dissolve

    ED "{color=#EBB134}''You’re La Piovositá’s second official barista.''"

    MAX "{color=#34B7EB}''Right! Of course! Guess it just slipped my mind...''"

    """
    {color=#34B7EB}I hadn’t actually forgotten, but for some reason it didn’t feel right for me to say it. I pretty much spent all weekend working myself up for today: my first official day on the job.

    {color=#34B7EB}I really shouldn’t be this nervous; I mean, I’m just a barista at some nowhere café that popped up last month, but somehow I’ve still managed to make myself anxious about it.

    {color=#34B7EB}Does everyone get this shaken up about their first job?
    """

    ED "{color=#EBB134}''Before you start, how about a test?''"

    show ed inquire

    MAX "{color=#34B7EB}''A test!? What do you mean?''"

    show ed neutral

    ED "{color=#EBB134}''Relax. Just make me a drink. A Deep Breath should be easy.''"

    MAX "{color=#34B7EB}''A Deep Breath? Got it!''"


    "{color=#34B7EB}Alright, a Deep Breath, that shouldn’t be hard. I just gotta look it up in the menu, and then put everything together, just like he taught me..."

    MAX "{color=#34B7EB}''Here you go, sir!''"

    ED "{color=#EBB134}''Don’t call me ‘sir.’ And thanks.''"

    MAX "{color=#34B7EB}''Noted... But how’s the drink? Did I do alright?''"

    show ed think

    if coffee >= 1:
        jump good
    else:
        jump bad

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # (if drink is correct)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label good:

    ED "{color=#EBB134}''Not bad.''"

    MAX "{color=#34B7EB}''Really?! You think so?!''"

    ED "{color=#EBB134}''The proportions are off. There’s too much milk in it. Otherwise, it’s decent.''"

    MAX "{color=#34B7EB}''Is that bad?''"

    show ed neutral

    ED "{color=#EBB134}''It’s not terrible.''"

    "{color=#34B7EB}I’m confused. But ‘decent’ is better than ‘bad’ so hey, I’ll take it."

    ED "{color=#EBB134}''Not the worst first coffee I’ve had.''"

    MAX "{color=#34B7EB}''How often have you even gotten to try someone’s first coffee?''"

    show ed think

    ED "{color=#EBB134}''More than you’d think. Four years of being a barista’s worth.''"

    MAX "{color=#34B7EB}''Four years!? But you don’t even look that much older than me.''"

    show ed neutral

    ED "{color=#EBB134}''I’m nineteen.''"

    MAX "{color=#34B7EB}''Nineteen!?
    You’re younger than me and have four years of job experience!?''"

    "{color=#34B7EB}Thankfully I don’t get much time to ponder on my own insecurities and inadequacies, as me and Ed’s conversation is swiftly interrupted by our boss slinking into the room."

    jump D1I1connect


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # (if drink is incorrect)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label bad:
    ED "{color=#EBB134}''It could use some work.''"

    MAX "{color=#34B7EB}''Oh, I see...''"

    "{color=#34B7EB}Crap. I can’t believe I messed up my first drink..."

    show ed neutral

    ED "{color=#EBB134}''Eh, don’t beat yourself up about it.
    Let’s call it a mulligan.''"

    MAX "{color=#34B7EB}''A mulligan... right.''"

    "{color=#34B7EB}I have no idea what that means.
    Though I don’t get much time to ponder it, as me and Ed’s conversation is swiftly interrupted by our boss slinking into the room."

    jump D1I1connect

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Both results go here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D1I1connect:

    show ed neutral at Position(xalign=0.1, yalign=0.22) with ease

    show laura angry at Position(xalign=0.5, yalign=0.22) with dissolve

    LAURA "{color=#ff3636}''Hey! What’s going on out here?
    ‘Cause it sure doesn’t look like working!''"

    ED "{color=#EBB134}''I’m testing Max before his shift.''"

    LAURA "{color=#ff3636}''Testing, huh? Well that’s funny, because I didn’t think I was paying you to be a teacher!''"

    ED "{color=#EBB134}''You were last week.''"

    show laura neutral

    LAURA "{color=#ff3636}''Well, that was last week, bub. This week, I’m paying you to do your dang job! And since the newbie’s up at the front, that means cleaning duty for you!''"

    ED "{color=#EBB134}''Fine with me.''"

    show laura angry

    LAURA "{color=#ff3636}''It better be! Now that we’re all in agreement, no more dilly dallying you two! This fine establishment isn’t going to run itself, you hear?
    So Edward, get to cleaning!''"

    show ed neutral at Position(xpos=-400, xanchor=0, yalign=0.22) with ease
    show laura angry at Position(xalign=0.3, yalign=0.22) with ease

    LAURA "{color=#ff3636}''And newbie!''"

    MAX "{color=#34B7EB}''Yes ma’am!?''"

    show laura inquire

    LAURA "{color=#ff3636}''You got any questions before I let you off the hook?''"

    MAX "{color=#34B7EB}''No ma’am!
    Actually, just one: Why are we called ‘La Piovositá?’''"

    show laura happy

    LAURA "{color=#ff3636}''An excellent question!
    It’s Italian! It means ‘the falling of the rain,’ isn’t it atmospheric?''"

    show ed neutral at Position(xalign=0, yalign=0.22) with ease

    ED "{color=#EBB134}''That’s not what it means.''"

    show ed neutral at Position(xpos=-400, xanchor=0, yalign=0.22) with ease
    show laura angry

    LAURA "{color=#ff3636}''Ah, whatever! Who’s gonna know the difference, anyway?''"

    MAX "{color=#34B7EB}''Well, you could’ve fooled me! Heheheh...''"

    show laura neutral

    LAURA "{color=#ff3636}''See? It’s great!
    Anyways, if that’s all you wanted, then I’ll let you get started...''"

    show laura neutral at Position(xpos=-400, xanchor=0, yalign=0.22) with ease

    """
    {color=#34B7EB}I don’t know what it is about Laura, but I can’t help but feel on edge when she’s around. It’s probably just because she’s my boss, but it might be something more.

    {color=#34B7EB}The way she walks around is so petite and elegant, and yet the way she talks is always so bold and explosive!

    {color=#34B7EB}I don’t understand how Ed converses so casually with her, even talking back to her on occasion.

    {color=#34B7EB}For me, I always feel like she could sneak up behind me at any moment and blow out my eardrums...
    """

    show laura angry at Position(xalign=0.3, yalign=0.22) with ease

    LAURA "{color=#ff3636}''Oh yeah and one more thing, newbie!''"

    MAX "{color=#34B7EB}''Ah! Y-y-y-yes!? What is it!?''"

    show laura neutral

    LAURA "{color=#ff3636}''Stop being so jumpy, alright? You’re gonna scare away the customers.''"

    MAX "{color=#34B7EB}''I’m sorry, ma’am! I’ll get on that right away!''"

    LAURA "{color=#ff3636}''You’d better.''"

    show laura neutral at Position(xpos=-400, xanchor=0, yalign=0.22) with ease

    """
    {color=#34B7EB}Sheesh...
    I guess I don’t really have much time to worry about it, though.

    {color=#34B7EB}Not when my first real customer could be right around the corner! The last thing I’d want to do is screw up my first day just because of my stupid nerves…
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 2 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D1Break:

    "{color=#34B7EB}As the customer left the building, I could hear the loud footsteps of a familiar body coming out from behind me."

    show ed neutral at Position(xalign=0.3, yalign=0.22) with ease

    ED "{color=#EBB134}''You’re doing good so far.''"

    MAX "{color=#34B7EB}''You really think so? I keep feeling like I have no idea what to say when it’s just me and a customer alone together.''"

    ED "{color=#EBB134}''It happens, don’t sweat it.
    Take a quick break. I’ll cover you.''"

    MAX "{color=#34B7EB}''You sure? I don’t know if Laura would like that...''"

    show ed think

    ED "{color=#EBB134}''If she doesn’t, she can tell me.
    Go take five in the break room.''"

    MAX "{color=#34B7EB}''Well, alright. Thanks Ed!''"

    show black box at Position(xalign=0, yalign=0) with dissolve
    show ed neutral at Position(xpos=-400, xanchor=0, yalign=0.22) with ease

    """
    {color=#34B7EB}As I exited into the back room, Ed only gave a quick grunt and a slight nod.
    Though I’m sure he meant it in the best way possible.

    {color=#34B7EB}It seemed as though Ed had done a pretty good job cleaning up the break room, though I can’t actually remember what it looked like last week well enough to say for certain.
    """

    hide black box with dissolve

    """
    {color=#34B7EB}Sure enough, five minutes had passed relatively quickly. As I stuck my head out of the break room, Ed was making idle chat with a customer and Laura was nowhere to be seen, so I figured returning to my post was the best option.
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 3 here
    jump D1I3
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 4 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D1Outro:

    """
    {color=#34B7EB}Once the final customer left, I took a glance at my phone and noticed that my shift was over.

    {color=#34B7EB}I immediately went toward Laura’s office to inform her I was leaving, but the door swung open seconds before I could reach the handle.
    """

    show laura neutral at Position(xalign=0.3, yalign=0.22) with ease

    LAURA "{color=#ff3636}''How’s the first day going, newbie?
    You manage to not screw up too bad yet?''"

    MAX "{color=#34B7EB}''Heheheh... well, you see...''"

    "{color=#34B7EB}Before I could meekly respond and likely embarrass myself, Ed steps in to my aid."

    show laura neutral at Position(xalign=0.5, yalign=0.22) with ease
    show ed neutral at Position(xalign=0.1, yalign=0.22) with ease

    ED "{color=#EBB134}''He did just fine. Now, he’s going home.''"

    show laura angry

    LAURA "{color=#ff3636}''He is, huh?''"

    MAX "{color=#34B7EB}''I mean I don’t have to!!
    I could always stay in and clean up a little if you need me to!''"

    ED "{color=#EBB134}''I can take care of it. You go home and rest.''"

    LAURA "{color=#ff3636}''Hey, since when are you the boss here, bub?
    Answer: you aren’t!''"

    show laura happy

    LAURA "{color=#ff3636}''So newbie, your boss says: go home and get some rest! Ed can take care of the cleaning up.''"

    MAX "{color=#34B7EB}''I, uh... Thanks! Both of you! Goodbye!''"

    ED "{color=#EBB134}''Safe travels.''"

    show laura neutral

    LAURA "{color=#ff3636}''Yeah, yeah just get out of here. Or else I might have to pay you overtime.''"

    show black box at Position(xalign=0, yalign=0) with dissolve

    """
    {color=#34B7EB}In retrospect, I think the day went relatively well. There may have been a few hiccups, maybe an awkward moment here and there, but I think Ed’s compliment might have actually been genuine, and not just a means to save me from Laura.

    {color=#34B7EB}I decided to keep said thought in my mind as a motivator to do well tomorrow, and to not disappoint Ed or Laura during my next shift.
    """

    jump DAY2
