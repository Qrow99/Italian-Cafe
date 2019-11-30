label D4I2:

    """
    {color=#34B7EB}The shadows and relentless snaps of the preceding figures fade, and in the process I nearly miss the entrance of a thin, short haired girl.
    """

    show errin neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    """
    {color=#34B7EB}As she eyes the menu, I notice her headphones of above average size and the hue of her skin, a shade of pink so bright that it's nearly glowing.

    {color=#34B7EB}Maybe she's sunburnt? Or maybe she's just cold? Hard to tell at this time of year which is more likely...
    """

    MAX "{color=#34B7EB}''Hello, miss! Welcome to La Piovosita! Can I get you anything?''"

    ERN "{color=#ffd6ff}''...''"

    "{color=#34B7EB}Nothing. Wouldn't be the first customer to give me the silent treatment, so I feel much better equipped to handle it this time around."

    MAX "{color=#34B7EB}''Something warm perhaps? Looks like it's a bit chilly out there!''"

    ERN "{color=#ffd6ff}''...''"

    """
    {color=#34B7EB}Still nothing. Okay.

    {color=#34B7EB}While the two of us stand no more than a couple feet apart but apparently far enough to be out of communication's range, the girl quickly turns her head to look over her shoulder before returning her gaze to the menu above me.

    {color=#34B7EB}Usually by this point in time the customer has at least told me their order, so I'm not really sure how to move forward in this scenario.

    {color=#34B7EB}Out of her headphones, I can faintly make out what sounds like loud R&B pumping into her skull. If I can hear it from here, I wonder how loud it is for her...
    """

    MAX "{color=#34B7EB}''Sounds like some nice music you've got playing there.''"

    ERN "{color=#ffd6ff}''...''"

    MAX "{color=#34B7EB}''Anything on the menu look interesting?''"

    ERN "{color=#ffd6ff}''...''"

    MAX "{color=#34B7EB}''Anything at all?''"

    ERN "{color=#ffd6ff}''...''"

    MAX "{color=#34B7EB}''Hey! Can you hear me? I asked if anything on the menu looks interesting!''"

    ERN "{color=#ffd6ff}''...''"

    "{color=#34B7EB}Before taking my next action, I myself take an opportunity to look behind me to determine if a particular red-headed boss may be observing my next move."

    MAX "{color=#34B7EB}''HEY! MISS! CAN I GET YOU A DRINK!?''"

    ERN "{color=#ffd6ff}''...''"

    """
    {color=#34B7EB}I take a moment to accept the reality of the situation and let out a meager sigh.

    {color=#34B7EB}Though I'm not usually one for rudely mumbling my feelings, opting instead to bottle them up as a defense mechanism, I can't help but mutter to myself just this one time.
    """

    MAX "{color=#34B7EB}''You're gonna go deaf if you keep listening to music like that.''"

    show errin inquire

    ERN "{color=#ffd6ff}''I'm sorry, did you say something?''"

    MAX "{color=#34B7EB}''Huh!? No!
    I mean, uh, yes! I was wondering if you wanted anything to drink! Heheheheh...''"

    "{color=#34B7EB}Once again, the girl takes a quick glance behind her shoulder before getting around to answering me."

    show errin neutral

    ERN "{color=#ffd6ff}''A drink would be nice, yes.''"

    MAX "{color=#34B7EB}''Okay, great! What can I get you?''"

    ERN "{color=#ffd6ff}''Anything is fine.''"

    MAX "{color=#34B7EB}''Um, okay? Do you have anything in particular in mind?''"

    ERN "{color=#ffd6ff}''No, I'm fine with anything.''"

    MAX "{color=#34B7EB}''...Alright, then.
    Do you like sweet things? Not that I'm trying to assume anything, but I quite like the Dark Sun, if that sounds appealing to you!''"

    ERN "{color=#ffd6ff}''Whatever works.''"

    MAX "{color=#34B7EB}''Alright... Can you at least give me something to work with?''"
    MAX "{color=#34B7EB}''Do you like chocolate? Cinnamon maybe? Pumpkin spice is popular this time of year, does that sound good to you?''"

    ERN "{color=#ffd6ff}''Mhm. That's fine.''"

    MAX "{color=#34B7EB}''...
    Alright, I'll whip something up for you, I guess!''"

    "{color=#34B7EB}What the heck am I even supposed to make here? I guess I'll get her... something."

    #(literally any drink works)

    MAX "{color=#34B7EB}''Alright, here's a drink! I hope you like it!''"

    "{color=#34B7EB}She takes the cup and lightly blows on it before taking a gentle sip."

    MAX "{color=#34B7EB}''How does it taste?''"

    show errin unsure

    ERN "{color=#ffd6ff}''Hm...''"

    "{color=#34B7EB}For a moment she sits in silence, and a moment after she looks as though she's about the throw up. The expression didn't last long, but it was nearly enough to make me regret getting out of bed this morning."

    show errin neutral

    ERN "{color=#ffd6ff}''I think I did want something a little sweeter after all.''"

    MAX "{color=#34B7EB}''Oh... I'm sorry to hear that.
    Do you want me to make you something else?''"

    ERN "{color=#ffd6ff}''No, I'll keep this one.''"

    MAX "{color=#34B7EB}''...Sounds good.''"

    show errin unsure

    """
    {color=#34B7EB}In the aftermath of our awkward interaction, the girl takes one more look behind her shoulder.

    {color=#34B7EB}Having once again found nothing out of the ordinary there, she takes another light sip of her drink before discreetly spitting it back into the cup.

    {color=#34B7EB}After smacking her lips in what appears to be both regret and disgust, she surprises me with an actual initiation of conversation.
    """

    show errin inquire

    ERN "{color=#ffd6ff}''Have you seen two well dressed individuals pass by here this afternoon?''"

    MAX "{color=#34B7EB}''I don't think so. Was I supposed to?''"

    show errin neutral

    ERN "{color=#ffd6ff}''...No. Just curious.
    Could I get this to go, please?''"

    MAX "{color=#34B7EB}''Well, uh, it's a cup. I think you can take it wherever you want as is.''"

    ERN "{color=#ffd6ff}''I see. I'll be on my way, then.''"

    #SE
    hide errin with dissolve

    """
    {color=#34B7EB}Taking light, nearly silent steps that tonally clash with the music still blasting into her ears, the girl leaves the building, though not before taking cautious glances in every direction on her way out.

    {color=#34B7EB}Frankly not the weirdest customer I've had this week, but I think I'd still put her in the top five.
    """

    jump D4Break
