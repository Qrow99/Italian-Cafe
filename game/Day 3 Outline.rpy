    label DAY3:

    show laura happy

    """
    {color=#34B7EB}Today’s classes were not quite as smooth as yesterday’s. Wednesday is my busiest day of the week, and I have classes one after the other all day until I have to go to work.

    {color=#34B7EB}By the time I entered La Piovosita, I had just finished scarfing down the lunch I had packed for myself this morning.
    """

    hide black box with dissolve

    LAURA "{color=#ff3636}''Ah newbie, I’m glad you’re here!''"

    "{color=#34B7EB}That’s surprising."

    LAURA "{color=#ff3636}''Check it out, I just came up with a brilliant idea!''"

    "{color=#34B7EB}Laura extends her arms toward me, revealing a large bottle of air freshener in each hand. I don’t know what to say to that."

    MAX "{color=#34B7EB}''Wow, that is a great idea!''"

    show laura angry

    LAURA "{color=#ff3636}''I haven’t even told you what I’m gonna do yet.''"

    MAX "{color=#34B7EB}''Oh, right. Heheheheh...''"

    show laura happy

    LAURA "{color=#ff3636}''Whatever. It doesn’t matter, because you’re right! This idea is great!
    Let me ask you something newbie, what the difference between this café and a fancy perfume shop?''"

    MAX "{color=#34B7EB}''Uuuuuuh... we don’t sell perfume?''"

    LAURA "{color=#ff3636}''Wrong! Well okay you’re not technically wrong, but fundamentally wrong!
    The real difference is the fact that the café doesn’t smell awful!''"

    MAX "{color=#34B7EB}''Is that a bad thing?''"

    LAURA "{color=#ff3636}''Potentially! You see, if this place smells like fruity crap, then customers will be too distracted by the smell to realize they don’t need to buy anything, and then they will!''"

    MAX "{color=#34B7EB}''That... makes perfect sense!''"

    show laura neutral

    LAURA "{color=#ff3636}''You don’t sound convinced. But that’s fine, I didn’t expect you to understand. Just watch, you’ll see! Once this place smells sufficiently fruity, we’ll have customers up the wazoo!''"

    """
    {color=#34B7EB}Laura confidently aims both of the bottles at the active ceiling fan and sprays about a dozen times.

    {color=#34B7EB}I could see the exact moment she began to regret her life choices as the concentrated scent of mango and apple blasted back toward the ground and, presumably, right back at her.

    {color=#34B7EB}And although I got to see that moment unfold quite clearly, the rest cannot be said about any moment soon after.

    {color=#34B7EB}As the intense cloud of fresh scent permeated the room, causing my eyes to water and plunging both Laura and myself into a fit of coughs and wheezes.
    """

    show laura angry

    LAURA "{color=#ff3636}*cough* ''Oh god, this really is awful!'' *cough* ''Newbie, why did you think this would be a good idea!?''"

    MAX "{color=#34B7EB}*cough* ''I’m sorry!'' *cough*"

    """
    {color=#34B7EB}I'm too busy trying to keep down my recently consumed lunch to get offended. Thankfully, me and Laura’s chorus of violent coughing is interrupted by Ed, who emerges from the break room with a small electric fan in hand.

    {color=#34B7EB}With a quick deactivation of the ceiling fan and the plugging in of the electrical one, the overwhelming musk of artificial fruit soon exited the building.
    """

    show laura angry at Position(xalign=0.5, yalign=0.205) with ease
    show ed neutral at Position(xalign=0.1, yalign=0.205) with ease

    MAX "{color=#34B7EB}''Thanks, Ed.''"

    show laura inquire

    LAURA "{color=#ff3636}''Yes, many thanks are indeed in order. Though I must ask, where’d you get that fan, huh? That better not have come out of company money!''"

    ED "{color=#EBB134}''I bought it myself. The break room gets hot.''"

    show laura neutral

    LAURA "{color=#ff3636}''Hmph. Alright, I’ll accept it.
    Speaking of you spending company money, you’re off cleaning duty today Edward! Today, I have a list of things I need you to pick up from the store down the street.''"

    ED "{color=#EBB134}''I’m guessing air freshener isn’t on there.''"

    show laura angry

    LAURA "{color=#ff3636}''Don’t get smart with me, bub! Look, the main thing you need to get is pumpkin creamer, alright? We can hardly keep that stuff in inventory with how much of the Song of Seasons we’re making! It’s in season, I guess.''"
    LAURA "{color=#ff3636}''So if nothing else, get the pumpkin! Got it, tubby?''"

    ED "{color=#EBB134}''Yup.''"

    show laura neutral

    LAURA "{color=#ff3636}''Great! I’m heading back to my office. Here’s the list. You two slackers just keep doing your jobs.''"

    show laura neutral at Position(xpos=-400, xanchor=0, yalign=0.205) with ease
    show ed neutral at Position(xalign=0.3, yalign=0.205) with ease
    show ed inquire

    ED "{color=#EBB134}''Max, I’m leaving. You okay on your own?''"

    MAX "{color=#34B7EB}''Yeah, I think so! How hard could it be, right...?''"

    hide ed with dissolve

    """
    {color=#34B7EB}Ed responds with a slight raise of his eyebrows and a meager grunt before leaving me alone in the café lobby. Honestly, it’s more than I expected.

    {color=#34B7EB}Not that that matters now, though. Because he’s counting on me to hold the fort while he’s gone, and I won’t let a little anxiety and air freshener induced lightheadedness stop me from doing this café proud!
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 1 here
    jump D3I1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 2 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D3Break:

    "{color=#34B7EB}As I wiped down the counter and quietly hummed along to the song playing over the café’s speakers, Ed burst through the door, sweaty and breathing heavily. In his hands are what I assume to be the items Laura asked him to buy."

    show ed neutral behind black at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Woah! Ed, are you alright? You look exhausted!''"

    ED "{color=#EBB134}''It’s nothing. Just tired from running.''"

    MAX "{color=#34B7EB}''You ran here!? Why?''"

    show ed think

    ED "{color=#EBB134}''I don’t like being late.
    Don’t worry about me. Go take your break.''"

    MAX "{color=#34B7EB}''Are you sure? You can at least cool down for a second; it looks like you need a break more than me.''"

    show ed neutral

    ED "{color=#EBB134}''I’m fine. Just put these in the break room.''"

    show black box at Position(xalign=0, yalign=0) with dissolve
    show ed neutral at Position(xpos=-400, xanchor=0, yalign=0.205) with ease

    """
    {color=#34B7EB}Ed handed me a couple plastic bags filled with miscellaneous items and sent me into the break room with a pat on the back.

    {color=#34B7EB}In response to my fear of potentially putting something in the wrong place, I decide to place the bags on a table so that Ed or Laura can take care of them later.

    {color=#34B7EB}During my break, I decide to do some reading for tomorrow’s classes. It’s difficult to do so without being distracted by the absolute beauty of the break room, but somehow I’ll manage.

    {color=#34B7EB}I have to admit it’s pretty hard, though. With the sheer comfort of the cushion under my rear mixed with the perfect amount of light illuminating the walls, all I want to do is sit back and bask in the glory of such a pleasant room.
    """

    hide black box with dissolve

    """
    {color=#34B7EB}As I finished up my reading and went back up to the counter, I saw Laura pushing Ed out the door, yelling about some more errands for him to run. As she went back to her office, she saw me with my phone in my hand and gave an uncharacteristically serious nod.
    """

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 3 here
    jump D3I3
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Interaction 4 here
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    label D3Outro:

    """
    {color=#34B7EB}I decide to take a quick look at my phone in the hopes that literally anyone tried to contact me during my shift.

    {color=#34B7EB}After taking a minute to recover from my disappointment, I notice that my shift is almost over. Sure enough, someone else had come to this realization as well.
    """

    show laura neutral behind black at Position(xalign=0.3, yalign=0.205) with ease

    LAURA "{color=#ff3636}''Hey newbie, your shift’s over. By the way have you seen Edward around?''"

    MAX "{color=#34B7EB}''Uh, should I have? I didn’t see him come in...''"

    show laura angry

    LAURA "{color=#ff3636}''I told him to get back here before your shift ended so he could work the counter, but it looks like that didn’t happen. I guess I shouldn’t be surprised.''"

    MAX "{color=#34B7EB}''Well he’s probably got a good reason, right? He doesn’t seem like the kind to be late.''"

    show laura inquire

    LAURA "{color=#ff3636}''Oh really? Where’d you get that idea? I could count the number of times he’s come to work on time on my toes! And that’s AFTER the accident!''"

    "{color=#34B7EB}I won’t ask."

    show laura neutral

    LAURA "{color=#ff3636}''It doesn’t matter anyways. I can take care of the counter until he gets back, you just get out of here.''"

    MAX "{color=#34B7EB}''Are you sure? I don’t mind staying a little late to help out if you need me to!''"

    show laura angry

    LAURA "{color=#ff3636}''What? You think I can’t handle this place on my own!? Is that what you’re trying to say!?''"

    MAX "{color=#34B7EB}''N-n-n-no!!! Not at all! In fact, I’m leaving right now! See you tomorrow ma’am!!!''"

    show black box at Position(xalign=0, yalign=0) with dissolve

    """
    {color=#34B7EB}And with that, I was out the door. I hope that uneasy encounters with my boss at the end of my shift won’t become a pattern from here on out...

    {color=#34B7EB}I can’t help but wonder why Ed was late to return back from his errands before the end of my shift. Or maybe I should be more curious as to why he wasn’t late to give me my break.

    {color=#34B7EB}I don’t think he would lie to me, but do I really know that...?

    {color=#34B7EB}Maybe I’ll just ask him about it tomorrow.
    """

    jump DAY4
