    label DAY4:

    "{color=#34B7EB}{b}The next day..."

    pause

    """
    {color=#34B7EB}As it turned out, I had completely forgotten whatever questions I wanted to ask Ed overnight. I’m sure they weren’t that important, right?

    {color=#34B7EB}Regardless, walking into work feels like it’s starting to become routine to me; entering the big glass doors no longer gives me as much of a wave of uncertainty as it used to, and in its place I can feel a growing sense of comfort and, almost, happiness.
    """

    hide black box with dissolve
    play music "mus_main_loop_cafejazz7.ogg"

    LAURA "{color=#ff3636}''It’s about time you showed up, newbie! Get over here, chop chop!!''"

    "{color=#34B7EB}Though the feelings Laura gives me remain about the same."

    MAX "{color=#34B7EB}''Yes ma’am!!''"

    show laura tired

    LAURA "{color=#ff3636}''Thank Jesus, Gandhi, and the buddha you’re here newbie! I’ve had to manage this whole hecking place by myself all day!''"

    MAX "{color=#34B7EB}''You have? What about Ed?''"

    show laura angry

    LAURA "{color=#ff3636}''The lazy lard is sick at home! He said he couldn’t make his shift today, and without him I’m the only one that’s left!''"

    MAX "{color=#34B7EB}''Wait, are Ed and I the only people working at this café?''"

    show laura tired

    LAURA "{color=#ff3636}''Employees are expensive, alright? Get off my case!
    Anyways, it doesn’t matter! I’m sure tubby’s just faking it all so he can come in extra late today...''"

    play sound "sfx_room_textmessage_receive.ogg"
    "{color=#34B7EB}Before Laura could continue her rant, a generic ringtone sounded from her pocket, accompanied by the sound of a vibrating mechanical device."

    show laura angry

    LAURA "{color=#ff3636}''It’s a text! From Edward! He says he needs to talk to me!''"
    LAURA "{color=#ff3636}''He’d better say his sickness miraculously disappeared, or else!''"

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_exit.ogg"
    show laura angry at Position(xpos=-400, xanchor=0, yalign=0.205) with ease
    play sound "sfx_room_door_wood_close.ogg"

    """
    {color=#34B7EB}Laura leaves in a huff into her office and begins wildly screaming at her cell phone.

    {color=#34B7EB}I’m not sure if the conversation is supposed to be private, but I’m holding out the hope that it’s not, considering Laura’s inability to keep her voice down...
    """

    LAURA """
    {color=#ff3636}''I don’t believe you! The stomach flu can’t be that bad!''

    {color=#ff3636}''Just down a couple bottles of aspirin or something, that’s what I do!''

    {color=#ff3636}''What do you mean that’s unhealthy? IT’S MEDICINE!''

    {color=#ff3636}''Ah, whatever! Newbie’s here anyways, so I’ll live, I guess.''

    {color=#ff3636}''Extra espresso? What’s that supposed to mean? Okay, sure, I’ll tell him.''

    {color=#ff3636}''But you’ll be here tomorrow right...?''

    {color=#ff3636}''That’s not a no, so I’ll take it as a yes! See you tomorrow, bub!''
    """

    play sound "sfx_room_door_wood_open.ogg"
    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_enter.ogg"
    show laura tired at Position(xalign=0.3, yalign=0.205) with ease

    LAURA "{color=#ff3636}''Well, newbie, looks like it’s just me and you this afternoon.''"
    LAURA "{color=#ff3636}''But don’t fret, I know that you and Edward have been getting all chummy as of late, so in his absence, I shall be your replacement Edward!''"

    "{color=#34B7EB}Laura jolts into an upright position and puffs out her cheeks, putting on a face that looks like someone trying their absolute hardest to be apathetic."

    show laura impersonation

    LAURA "{color=#ff3636}''So, what do you think?''"

    MAX "{color=#34B7EB}''It’s, uh... it’s perfect! It’s like Ed never left!''"

    show laura neutral

    LAURA "{color=#ff3636}''Jeez, no need to butter me up, kid. I can tell you aren’t convinced.''"

    show laura happy

    LAURA "{color=#ff3636}''Oh, I get it! It must be the phrasing! I’m using too many words in each sentence, huh?''"

    MAX "{color=#34B7EB}''I mean, he does tend to not use a whole lot of those.''"

    LAURA "{color=#ff3636}''Of course, that’s what I’m missing!
    Tell you what, I’m going to go in my office and practice my Edward impression, and you stay here and work!''"

    MAX "{color=#34B7EB}''Sounds great!''"

    LAURA "{color=#ff3636}''I thought so! You just wait, newbie! When I’m done, it’ll be like Edward never left!''"

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_exit.ogg"
    show laura happy at Position(xpos=-400, xanchor=0, yalign=0.205) with ease
    play sound "sfx_room_door_wood_close.ogg"

    """
    {color=#34B7EB}Laura takes a jaunty strut to her office, leaving me completely alone.

    {color=#34B7EB}Not that it’s really all that different from what usually happens during my shift, but without Ed it feels a little bit emptier...

    {color=#34B7EB}I guess I shouldn't dwell on it too much, though. Not while I have a job to do! Especially since Ed isn’t here! I need to be on the top of my game today! Now if only I really knew what that meant...
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 1 here
    jump D4I1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 2 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D4Break:

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_enter.ogg"
    show laura neutral at Position(xalign=0.3, yalign=0.205) with ease

    LAURA "{color=#ff3636}''How goes it, newbie?''"

    MAX "{color=#34B7EB}''Pretty good! I was just about to take my...''"
    MAX "{color=#34B7EB}''Actually, nevermind! Nothing! Everything’s going perfect! Hahahah...''"

    "{color=#34B7EB}This would usually be the time of day that Ed gives me a break, but I wouldn’t dare ask Laura for one. I feel like she’d more likely kill me than let me off work, even for a few minutes."

    show laura inquire

    LAURA "{color=#ff3636}''What? Were you going to...''"

    show laura impersonation

    LAURA "{color=#ff3636}''I mean, uh... You gonna ask for break?''"

    MAX "{color=#34B7EB}''What!? No! Not at all, I wouldn’t...''"

    show laura neutral

    LAURA "{color=#ff3636}''Oh come on, I know Edward gives you breaks every day. I’m not stupid.''"

    show laura angry

    LAURA "{color=#ff3636}''Nor am I a monster! Look newbie, if you ever need to take five or something... I mean, you need anything just ask.''"

    MAX "{color=#34B7EB}''Wow, that’s... thanks, ma’am! I really appreciate it!''"

    show laura neutral

    LAURA "{color=#ff3636}''Yeah, anytime.
    Anytime, except today! Not while we’re understaffed!''"

    MAX "{color=#34B7EB}''Uh, okay! So that’s a no on the break, then?''"

    show laura tired

    LAURA "{color=#ff3636}''Yeah, the break is a no can do, bud. Being boss is already a workload, but doing that PLUS imitating your coworker is a full time job.''"

    LAURA "{color=#ff3636}''I’m sure you understand, I can’t do all that AND work the counter!
    Tomorrow maybe, but I just told me that I gotta clean the bathrooms again, and I can’t be doing that and letting you slack off at the same time.''"

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_exit.ogg"
    show laura tired at Position(xpos=-400, xanchor=0, yalign=0.205) with ease
    play sound "sfx_room_door_wood_close.ogg"

    """
    {color=#34B7EB}That was surprisingly pleasant, at least as far as interactions with Laura go. Maybe she isn’t as abrasive as I thought...

    {color=#34B7EB}Not that it matters too much right now. I’m honestly not really upset that I’ve lost my five minutes of solitude today, but I’d be lying if I said I didn’t miss my one chance to enter the break room today.

    {color=#34B7EB}The refreshing scent, the perfect view from the window, and the astonishingly tasteful decoration... And I bet it looks even better today than it has all week!

    {color=#34B7EB}A break is one thing, but missing out on that experience is enough to bring a tear to the eye...
    Guess I’d better stop thinking about it and try to focus more on my job.
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 3 here
    jump D4I3
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 4 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D4Outro:

    "{color=#34B7EB}I began to reach down for my favorite counter-cleaning rag when I'm interrupted by a familiar shadow slinking its way toward my location."

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_enter.ogg"
    show laura happy at Position(xalign=0.3, yalign=0.205) with ease

    LAURA "{color=#ff3636}''Hey Max, shift’s over. Go home, you did good today.''"

    MAX "{color=#34B7EB}''Really? Well, thanks!''"
    MAX "{color=#34B7EB}''Wait, I did!? That’s, uh, really nice of you to say! Thanks ma’am!''"

    show laura inquire

    LAURA "{color=#ff3636}''You sound surprised! Is it really that rare for you to get complimented?''"

    MAX "{color=#34B7EB}''Well, no... Actually, yes. But from you especially!''"

    show laura angry

    LAURA "{color=#ff3636}''You saying I’m not nice!?''"

    MAX "{color=#34B7EB}''What!? No, no! You’re totally nice! I just, uh... you know, I guess I don’t pay enough attention!?''"

    "{color=#34B7EB}Laura didn’t have an immediate response. She just stood still, unimpressed, before letting out a concealed but noticeable sigh."

    show laura tired

    LAURA "{color=#ff3636}''Fine, I get it. You can stop blubbering.
    It doesn’t matter anyways; I was just trying to say something Edward would say, since you two are so buddy-buddy and all...''"

    "{color=#34B7EB}For the first time I think ever, Laura breaks eye contact with me and turns away. But not a second later, she's back to staring me down like usual."

    show laura angry

    LAURA "{color=#ff3636}''But impression or not, you heard me didn’t you!? Scram, before I kick you out!''"

    play sound "sfx_room_footsteps_exit.ogg"
    show black box at Position(xalign=0, yalign=0) with dissolve
    play sound2 "sfx_room_door_main_close.ogg"
    stop music fadeout 5.0

    """
    {color=#34B7EB}Not wanting to disobey after such a disjointed interaction, I proceed to scram without a word more.

    {color=#34B7EB}I wonder how much Laura actually meant the compliment she gave me...

    {color=#34B7EB}Unlike her usual bombastic, angry reaction to my poor choice of phrasing, she seemed genuinely offended by my surprise for a moment, and then became bombastically angry.
    """
    if Brenda == 1:
        jump BrendaHappy
    else:
        jump BrendaSad

    # (if Brenda didn’t say much)
    label BrendaSad:
    "{color=#34B7EB}Maybe she was just tired from working all day? I hope I didn’t actually hurt her feelings..."

    # (if Brenda told Max everything)
    label BrendaHappy:
    "{color=#34B7EB}But I can’t be thinking about that now! I’ve got something more important to do, and that’s call Ed! If my hunch is right and Ed does have a crush, then I’ve got something to tell him..."

    pause

    jump DAY5
