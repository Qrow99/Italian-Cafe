    label D2I4:

    """
    {color=#34B7EB}Before I can spend too much time thinking about it, I hear a familiar stomping and clanging, and I immediately see Sahbreena burst through the doors of the coffee shop.
    """

    play sound2 "sfx_room_door_main_open.ogg"
    play sound "sfx_room_door_main_bellchime.ogg"

    """
    {color=#34B7EB}She seems to be in a good mood because she's flashing a tight smile—so tight her braces look like they're about to pop off of her teeth. She immediately darts to the counter and slams what seems to be a new neon pink hydro flask.
    """

    play sound "sfx_room_footsteps_enter.ogg"
    show sahbreena happy at Position(xalign=0.3, yalign=0.205) with dissolve

    """
    {color=#34B7EB}I stand to attention like I was in a military drill and I immediately ready myself to take her order, praying to the scrunchie on my wrist to grant me VSCO girl strength.
    """

    SBNA "{color=#fa9def}''Guess. Who. Got. Over. 1500 followers. On. Click Clock. Thisksksksk girllllll! I'm basically royalty in my school. The ninth graders beg me to follow them!''"

    "{color=#34B7EB}I don't really know how to react, but I'm too afraid to say anything too insulting. Even though she's a kid, I'm afraid what her social media powers could do to a plebian like me."

    MAX "{color=#34B7EB}''Um, good for you! Seems like you've got your life together...''"
    MAX "{color=#34B7EB}''But anyways, what would you like to order, Sahbreena? Maybe something special to commemorate your...accomplishment?''"

    SBNA "{color=#fa9def}''And I OoP! Great idea Maxie! Maybe you can help me choose because of your vasssstttttt knowledge of coffee drinkies.''"

    show sahbreena neutral

    SBNA "{color=#fa9def}''I might be good at everything, like single-handedly saving the planet with my metal straws cuz I'm gonna tell my followers to use them or else I'll block them, but coffee-making is a no no.''"

    MAX "{color=#34B7EB}''Oh thanks, but it's not that special, just something I need to know for the job. From your last drink, it was very sweet with lots of cream—The Dinkles with creamer and lotsksksk of whipped cream?''"

    "{color=#34B7EB}Wow, I really added 'sksksksk' to that, huh? This scrunchie has magical properties."

    show sahbreena happy

    SBNA "{color=#fa9def}''Yesksksk! My go-to-drinkies! Wow, you remembered and even said 'sksksksk' at the end. Heheheeheheh. So whaddya think I should get?''"

    MAX "{color=#34B7EB}''Well I would suggest the 'Benny Goodman' with cinnamon flavoring with a mountain of whipped cream. How does that sound?''"

    SBNA "{color=#fa9def}''O.M.G. That soundsksk yumilicious! I'll have that please! With a cherry on top!''"

    # (A/N: God, I hate myself)

    MAX "{color=#34B7EB}''Yes and no. My manager, Laura, is too cheap to buy cherries. But comin' right up!''"

    show sahbreena angry

    "{color=#34B7EB}I see Sahbreena's eyes flash with a burning rage for a second, but she snaps back to reality and smiles at me again. I am afraid."

    show sahbreena happy

    SBNA "{color=#fa9def}''Okie dokiesksk! Here's my reusable coffee cup and its extra large! I'll wait over there.''"

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_exit.ogg"
    hide sahbreena with dissolve

    "{color=#34B7EB}She tiptoes carefully to a nearby table and stubs her toe in the process. Weirdly out of character, she says a resounding 'FRICK.'"
    "{color=#34B7EB}Ignoring that, did she ask for a Dinkles or a Benny Goodman...? I don't actually remember if she wanted to take my suggestion or not."
    while makingdrink == 0:
        "{color=#34B7EB}Ignoring that, did she ask for a Dinkles or a Benny Goodman...? I don't actually remember if she wanted to take my suggestion or not."
        #pause

    $ makingdrink = 0
    # Coffee making gameplay ensues. You're not allowed to fail because you just can't.

    MAX "{color=#34B7EB}''Sahbreena! You're order is ready!''"

    play sound2 "<from 1.5 to 2.75>sfx_room_footsteps_enter.ogg"
    show sahbreena neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    SBNA "{color=#fa9def}''And I OoP! And I OOp! Wow I'm so excited for my celebratory drink! Yayzies! I knew I could trust your coffee brain Maxieeeee!!''"

    "{color=#34B7EB}As she continues to talk, her voice reaches an unbelievably high pitched tone."

    show sahbreena happy

    SBNA "{color=#fa9def}''This drink looks A-M-A-Z-I-N-G! I totes need to take a selfie with you.''"

    MAX "{color=#34B7EB}''Oh no, you don't need to—''"

    "{color=#34B7EB}She quickly takes out her phone and snaps a shot of herself holding the whipped cream, diabetes grenade in her hand and me in mid-sentence. She times it right so I look like I'm smiling. She's good."

    SBNA "{color=#fa9def}''This one will get thousands of likes heheheh. Don't worry, it'll be good free publicity for your coffee shop! Your manager will have to thank me for all that free moniesss so she'll have to buy those cherries. 'Kay 'kay? I'll be waitinggggg!''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide sahbreena with dissolve
    play sound2 "sfx_room_door_main_close.ogg"

    "{color=#34B7EB}In a flash, I barely get a word in, much less, say goodbye. She's already on her way on who knows where, clanging and almost tripping on the sidewalk. I hope Laura buys cherries."

    jump D2Outro
