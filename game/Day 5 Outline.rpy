    label DAY5:

    show laura tired at Position(xpos=-400, xanchor=0, yalign=0.205) with ease
    show ed sick neutral at Position(xalign=0.3, yalign=0.205) with ease

    """
    {color=#34B7EB}Walking into work, I feel the effects of my first Friday taking hold of me. I’m simultaneously excited to be here and excited to leave. I’m both determined to work and too lazy to want to. I’m two other contradictory things.

    {color=#34B7EB}Yup, I’ve got a spring and my step and I’m ready for my shift! Furthermore, I’m excited to see my coworker again, hoping that he, too, is pumped up by the end-of-the-week vibes as much as I am.
    """

    hide black box with dissolve

    MAX "{color=#34B7EB}''Hey Ed, I’m here- woah! Are you okay!? You look terrible!''"

    ED "{color=#EBB134}''I’m fine.''"

    # (if Brenda)
    if Brenda == 1:
        ED "{color=#EBB134}''I just didn’t sleep.''"

        MAX "{color=#34B7EB}''Really? Why?! Aren’t you sick?''"

        show ed sick think

        ED "{color=#EBB134}''I played 'Guild of Greats' all night.''"

        MAX "{color=#34B7EB}''All night!? Even when you’re sick!?''"

        show ed sick neutral

        "{color=#34B7EB}Ed offered a meager shrug in response."

    else:
        ED "{color=#EBB134}''I’m just nervous.''"

        MAX "{color=#34B7EB}''Nervous? Why?''"

        show ed sick think

        ED "{color=#EBB134}''...''"
        ED "{color=#EBB134}''I meant tired. I’m still sick.''"

        MAX "{color=#34B7EB}''Um, okay. Those are pretty different things, but alright.''"

        show ed sick neutral

        "{color=#34B7EB}Ed offered a meager shrug in response."


    # converge here
    ED "{color=#EBB134}''I’m gonna talk to her today.''"

    MAX "{color=#34B7EB}''What?''"

    ED "{color=#EBB134}''Brenda, the regular here. I’m going to talk to her.''"

    MAX "{color=#34B7EB}''Oh, really? Well, that’s great! You think you’re ready?''"

    show ed sick think

    ED "{color=#EBB134}''Not at all.''"

    MAX "{color=#34B7EB}''Oh, I see..."

    """
    {color=#34B7EB}It occurs to me that I have no idea about anything regarding basic human interaction, let alone how someone could format a first encounter with someone who they have a big fat crush on.

    {color=#34B7EB}I’m happy that Ed’s deciding to make a move, but I’d be lying if I said he had much of a way with words, considering he hardly uses them.

    {color=#34B7EB}I wonder if there’s any way I can help him out...

    {color=#34B7EB}Right on cue, Laura found a way to sneak her way into the main room undetected, and for the first time I’m grateful for it.
    """

    show ed sick think at Position(xalign=0.1, yalign=0.205) with ease
    show laura angry at Position(xalign=0.5, yalign=0.205) with ease

    LAURA "{color=#ff3636}''Edward, you look awful. Also, you’ve been slacking all day! Are you sure you’re actually fit to work today?''"

    show ed sick neutral

    ED "{color=#EBB134}''I’m fine.''"

    show laura inquire

    LAURA "{color=#ff3636}''Really? Could’ve fooled me...
    But if that’s really the case, then you’d better work double time for the rest of the day! Now that Max is here, you know what time it is!''"

    ED "{color=#EBB134}''I’ll get the mop.''"

    show ed sick neutral at Position(xpos=-400, xanchor=0, yalign=0.205) with ease
    show laura inquire at Position(xalign=0.3, yalign=0.205) with ease
    show laura neutral

    LAURA "{color=#ff3636}''Perfect! And Max, I’m assuming you know what to do by this point, so just do it, alright!? I’m going back to my office.''"

    show laura neutral at Position(xpos=-400, xanchor=0, yalign=0.205) with ease

    MAX "{color=#34B7EB}''Uh, yeah! Of course! I’ll just be here, I guess...''"

    """
    {color=#34B7EB}As I am once again left alone at the La Piovosita’s counter, I have little else to do but continue messing around with the thoughts in my head.

    {color=#34B7EB}Considering how much he’s done for me these past couple of weeks, I want to help Ed talk to Brenda, but I have no clue how. It’s not like romantic, or even platonic, advice could just suddenly make itself appear out of nowhere, could it?
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 1 here
    jump D5I1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 2 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D5Break:

    "{color=#34B7EB}Suddenly Ed bursts into the room from the break room, his face bright red and the rest of his body not looking much better."

    show ed sick neutral at Position(xalign=0.3, yalign=0.205) with ease

    ED "{color=#EBB134}''Max, break time.''"

    MAX "{color=#34B7EB}''Jeez, Ed! Are you alright!? You look... well, no better than when I got here, at least.''"

    ED "{color=#EBB134}''I’m fine. Don’t worry about it.''"

    MAX "{color=#34B7EB}''Are you sure?''"

    show ed sick think

    ED "{color=#EBB134}''I said I’m fine. Just go take five.''"

    MAX "{color=#34B7EB}''Uh, alright then. If you say so.''"

    show black box at Position(xalign=0, yalign=0) with dissolve

    """
    {color=#34B7EB}Ed’s never been all that flowery with his words, but this is probably the most pushy I’ve ever heard him. As much as I’d like to try and help calm him down, if he needs space then maybe that’s the best thing I can give him.

    {color=#34B7EB}And hey, you won’t see me complaining about getting another chance to visit the break room. Ed must have spent the entirety of my shift so far in here, because it’s completely spotless from top to bottom.

    {color=#34B7EB}With the tender ray of sunlight that kisses the glass at this time of day, the whole room appears to sparkle in a soft, majestic glow.

    {color=#34B7EB}Sitting in the seat most optimally angled to give the greatest view of the room as a whole, I find myself losing all sense of time and space to the aesthetically immaculate collection of intricate senses and feelings that is the break room.
    """

    hide black box with dissolve

    """
    {color=#34B7EB}And then I leave, and Ed is just standing at the counter, staring at the door.
    """

    MAX "{color=#34B7EB}''Hey Ed, I’m back. You doing alright?''"

    ED "{color=#EBB134}''She’s not here yet.''"

    """
    {color=#34B7EB}Walking back to my post, I can see his foot tapping under and hear him breathe heavily and inconsistently. Somehow, he manages to look even worse than he did five minutes ago. Is he really that nervous?

    {color=#34B7EB}I begin to walk over to him to offer him the advice I’ve accumulated throughout my shift, but an incoming customer interrupts me.
    """

    MAX "{color=#34B7EB}''Oh Ed, I’ll take this one! You just... keep doing what you’re doing.''"

    show ed sick neutral at Position(xpos=-400, xanchor=0, yalign=0.205) with ease

    "{color=#34B7EB}He doesn’t make a move, but I figure that’s as close to an ‘okay’ as I’m getting at this point."

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 3 here
    jump D5I3
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D5I4:

    """
    {color=#34B7EB}Before the faded, yellow smile and wrinkled thumbs up given by the strange man fully fade away, a minor chill courses through my body in reaction to a hand being placed gently on my shoulder.

    {color=#34B7EB}Turning around, I find this hand belongs to the only other person behind the counter. Shocker.
    """

    show ed sick think at Position(xalign=0.3, yalign=0.205) with ease

    """
    {color=#34B7EB}I don’t even know if I should give Ed any advice at this point. I mean, I’ve certainly accumulated a lot throughout the day, but it just seems so... I don’t know, obvious?

    {color=#34B7EB}Being honest, being yourself, it all sounds pretty cheesy doesn’t it? I bet Ed doesn’t even need my advice at this point. In fact, he may even be totally over his nerves by now...
    """

    ED "{color=#EBB134}''I can’t do it.''"

    MAX "{color=#34B7EB}''Do what?''"

    ED "{color=#EBB134}''I couldn’t talk to Brenda. I made her drink, then I froze.''"

    MAX "{color=#34B7EB}''Well you must have said something, right?''"

    show ed sick neutral

    ED "{color=#EBB134}''No more than usual.''"

    "{color=#34B7EB}Out of the corner of my eye I can see Brenda in her usual corner, rapidly clicking and tapping her keyboard like she had yesterday. Clearly, nothing was different."

    MAX "{color=#34B7EB}''Guess you didn’t, huh?''"

    show ed sick think

    ED "{color=#EBB134}''Today’s bad. I’ll talk to her some other time. Next month maybe.''"

    MAX "{color=#34B7EB}''Next month!? You can’t wait that long!''"

    show ed sick inquire

    ED "{color=#EBB134}''Why not?''"

    MAX "{color=#34B7EB}''Because, uh, you don’t know if she’s going to be here that long!''"

    ED "{color=#EBB134}''What?''"

    MAX "{color=#34B7EB}''You don’t know how much longer she’ll want to hang around this café! Heck, you don’t really know that much about her at all! But the only why you can find out is to talk to her, you know?''"

    ED "{color=#EBB134}''...Were you preparing that?''"

    MAX "{color=#34B7EB}''I may have gotten some help...''"

    "{color=#34B7EB}Ed stood still for a moment, looking like I had just spoken to him in several different languages, all long dead."

    show ed sick think

    ED "{color=#EBB134}''Make me your favorite drink.''"

    MAX "{color=#34B7EB}''My what...? Uh, okay, but why?''"

    show ed sick neutral

    ED "{color=#EBB134}''I don’t understand your advice. But a drink I can understand.''"

    MAX "{color=#34B7EB}''I don’t really get what you mean by that, but alright?! I’ll make you the best drink I can, then!''"

    "{color=#34B7EB}Ignoring the potential judgement that could befall me from revealing such information to him, I make Ed my favorite beverage..."

    #(another drink making section goes here. it doesn’t matter what the result is, though.)
    while makingdrink == 0:
        "{color=#34B7EB}Ignoring the potential judgement that could befall me from revealing such information to him, I make Ed my favorite beverage..."
        pause

    $ makingdrink = 0

    "{color=#34B7EB}In a single gulp, Ed finishes the drink. He closes his eyes, scratches his chin, and then nods."

    show ed sick think

    ED "{color=#EBB134}''Alright, I get it.''"

    MAX "{color=#34B7EB}''You do?''"

    show ed sick neutral

    ED "{color=#EBB134}''Sure. Wish me luck.''"

    "{color=#34B7EB}Before I could ask another stupid question, Ed turned around and started marching toward the table at the furthest corner of the room."

    show black box at Position(xalign=0, yalign=0) with dissolve
    show ed sick surprise at Position(xalign=0.1, yalign=0.205) with ease
    show brenda surprise behind black at Position(xalign=0.5, yalign=0.205)

    """
    {color=#34B7EB}With as much confidence as a nervous, partially mute man with a fever could probably muster, my large friend positioned himself next to his target.

    {color=#34B7EB}He cleared his throat, tapped her on the shoulder, and as she removed her headphones he lifted up his arm and...

    {color=#34B7EB}His elbow knocked against her cup of coffee, spilling it all over her lap.

    {color=#34B7EB}For the first couple of moments neither of them said anything. Ed stood completely frozen and bug eyed as Brenda bit her bottom lip, I can only assume as a reaction to having scalding liquid poured all over her.
    """

    hide black box with dissolve

    ED "{color=#EBB134}''I’m so sorry, I’ll get some more napkins.''"

    show brenda inquire

    BND "{color=#b459ff}''Wait, hold on, what did you just say?''"

    show ed sick inquire

    ED "{color=#EBB134}''I said that I’ll get some more napkins.''"

    show brenda happy

    BND "{color=#b459ff}''Huh... that’s eight words. I think that’s the longest sentence I’ve ever heard you say.''"

    """
    {color=#34B7EB}Ed had no response to this. He didn’t say anything, not that I can blame him.

    {color=#34B7EB}Instead, though, he cupped his hand around his mouth and burst out into laughter.
    """

    show ed sick happy

    """
    {color=#34B7EB}Not an awkward, stilted laugh, but a full on guffaw erupted from his mouth and filled the whole room. Not a moment after, Brenda too began to roar with laughter, the two of them alone seeming to almost shake the building.

    {color=#34B7EB}I would certainly join them were I not too busy being impressed by their volume.
    """

    BND "{color=#b459ff}''Hey, I know it’s funny and all, but maybe we can keep joking around after you get those napkins?''"

    ED "{color=#EBB134}''You’re right! I’m sorry! Be right back.''"

    show black box at Position(xalign=0, yalign=0) with dissolve

    """
    {color=#34B7EB}Ed practically sprints to the counter and back; I don’t think I’ve ever seen someone grab napkins with such speed, but it’s not like I’ve paid much attention.

    {color=#34B7EB}For the brief moment he was within my immediate vicinity, I could see Ed not only struggle to keep in his laughter, but also tear up slightly, probably as a result of said laughter.

    {color=#34B7EB}The sight of Ed actually smiling and laughing is just so...unusual. So much so that it distracts me from realizing another entire person had come out to witness Ed’s attempt at human interaction.
    """

    show ending placeholder at Position(xalign=0, yalign=0) with dissolve
    hide black box

    LAURA "{color=#ff3636}''Sheesh. About time he made a freaking move.''"

    MAX "{color=#34B7EB}''Did you know about this? Him having a crush, I mean?''"

    LAURA "{color=#ff3636}''What!? Of course I did! Come on, it was obvious!''"

    MAX "{color=#34B7EB}''Oh yeah, you’re right! I guess it was, heheheh...''"

    LAURA "{color=#ff3636}''You know you don’t have to agree with me all the time, right? It’s not too bad to be wrong now and again.''"

    MAX "{color=#34B7EB}''Really? Does that mean you won’t yell at me?''"

    LAURA "{color=#ff3636}''No, I’ll still yell at you. But I don’t mean everything I say, you know?''"

    MAX "{color=#34B7EB}''You don’t!?''"

    LAURA "{color=#ff3636}''Of course I don’t! How thick are you!?
    If I did, tubby would’ve been fired at least five times by now!''"

    MAX "{color=#34B7EB}''Yeah, I guess that makes sense.''"

    LAURA "{color=#ff3636}''Speaking of Edward, I think it’s about time you get going. If you’re still here, then I can’t force loverboy over there to keep working!
    So you can get off your shift early. My treat.''"

    MAX "{color=#34B7EB}''Actually, ma’am, I think my shift ended ten minutes ago...''"

    LAURA "{color=#ff3636}''Oh, even better then! In that case, scram kid! I don’t wanna see your face around here until next week, or else I might have to pay you for it!''"

    MAX "{color=#34B7EB}''Sounds good to me!''"

    show black box at Position(xalign=0, yalign=0) with dissolve

    """
    {color=#34B7EB}After taking a moment to share a quick goodbye with everyone in the building, I ran out the doors of La Piovosita and into the cool evening air.

    {color=#34B7EB}Despite how much I was looking forward to this moment, my first real weekend, I’m honestly a little sad to be without the various names and faces of the café for even just a couple days.

    {color=#34B7EB}Maybe it’s the fact that I’m new, or the fact that I quite like my coworkers, or even the fact that I’ve yet to experience serving more than, like, three people at one time yet, but I feel like I’m really going to enjoy working as a humble barista for while.

    {color=#34B7EB}Guess I’ll just have to wait until next week.

    {color=#34B7EB}{b}The end! Thanks for playing!
    """
