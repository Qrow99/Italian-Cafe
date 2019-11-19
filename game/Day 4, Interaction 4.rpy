    label D4I4:

    play sound "sfx_room_footsteps_enter.ogg"

    """
    {color=#34B7EB}As I ponder how nosy I intend to be in regards to my coworker, two boys enter the building, making idle chat as they walk in. I’m still not quite sure how to address groups of people, since I don’t want to interrupt their conversation, but I’d hate to come off as rude.

    {color=#34B7EB}I guess the basic introduction has worked pretty well thus far, so I won’t bother trying to fix what isn’t broken.
    """

    show chase neutral at Position(xalign=0.5, yalign=0.22) with dissolve
    show roy neutral at Position(xalign=0.1, yalign=0.22) with dissolve

    MAX "{color=#34B7EB}''Hello! Welcome to La Piovosita!''"

    show chase happy

    CHASE "{color=#FFCB70}''Thank you!''"

    ROY "{color=#82C26E}''...''"

    "{color=#34B7EB}The tall one stares at the menu while the other checks his phone. All the while the two continue to chat with each other."

    show chase inquire

    CHASE "{color=#FFCB70}''What do you want to drink?''"

    ROY "{color=#82C26E}''I’ll just have whatever you’re having.''"

    show chase inquire

    CHASE "{color=#FFCB70}''Alright! In that case...
    Can I get two Deep Breaths please?''"

    MAX "{color=#34B7EB}''Sure thing! Just let me...''"

    ROY "{color=#82C26E}''Hold on.''"

    show roy inquire

    ROY "{color=#82C26E}''Hey, did you ask him?''"

    show chase happy

    CHASE "{color=#FFCB70}''Oh yeah, I forgot! Can I get two Deep Breaths without milk, please?''"

    MAX "{color=#34B7EB}''Without milk?''"

    show chase inquire

    CHASE "{color=#FFCB70}''Yeah, I’m lactose intolerant. Is that okay?''"

    MAX "{color=#34B7EB}''Uh, sure! I’ll do the best I can!''"
    while makingdrink == 0:
        "{color=#34B7EB}I don’t think there’s much in the Deep Breath except milk... Guess I’ll just have to improvise?"
        pause

    $ makingdrink = 0


# Drink minigame here
# If the drink has milk in it, it's a fail. Anything else is fine.
    if coffee == 1 and whip_cream == 1:
        jump d4i4good
    elif milk == 1:
        jump d4i4bad

    MAX "{color=#34B7EB}''Alright, here you go! Two Deep Breaths, special ordered!''"

    show chase happy

    CHASE "{color=#FFCB70}''Thank you very much!''"

    show roy neutral

    ROY "{color=#82C26E}''Yeah.''"

    """
    {color=#34B7EB}The two boys take radically different approaches to consuming their drinks.

    {color=#34B7EB}The tall one immediately takes a large slurp of his beverage, while the short one blows on his before taking a cautious sip. Neither make a particularly disgusted reaction, so that’s at least comforting.
    """


    # (if drink has no milk)
    label d4i4good:
    MAX "{color=#34B7EB}''So, how do you guys like it?''"

    CHASE "{color=#FFCB70}''It’s great, thanks!''"

    ROY "{color=#82C26E}''It’s alright.''"

    CHASE "{color=#FFCB70}''And my stomach isn’t destroying itself at the moment, so I’d say you did a pretty good job!''"

    MAX "{color=#34B7EB}''Well, I’m glad you think so.''"
    MAX "{color=#34B7EB}''Hey, I hope this isn’t too personal, but can I ask why you’d even bother ordering something that might have milk if you’re lactose intolerant? I’m no expert, but I’d think you’d want to avoid it as much as possible.''"

    show chase neutral

    CHASE "{color=#FFCB70}''Well, I can have a little of it and I’ll still be fine.''"

    "{color=#34B7EB}The tall one happily sips his drink, but his partner doesn’t look quite as comfortable."

    show roy embarrassed

    ROY "{color=#82C26E}''It’s because lactose intolerance isn’t like a food allergy.''"
    ROY "{color=#82C26E}''Sure, drink a whole cup of milk and he’ll feel like shit, but for the most part the worst thing he’ll get is a stomach ache...''"

    show roy angry

    ROY "{color=#82C26E}''Which happens a lot because he’s a big idiot who doesn’t care about his digestive system!''"

    show chase happy

    CHASE "{color=#FFCB70}''Yup, that about sums it up!''"

    "{color=#34B7EB}Despite the tone of the short boy being borderline aggressive, the tall one doesn’t react at all. I won’t question it."

    MAX "{color=#34B7EB}''Sounds like you’re pretty knowledgeable about this stuff. Do you have a food allergy?''"

    show roy embarrassed

    ROY "{color=#82C26E}''Well no, but... It’s just good stuff to know, alright? Just in case someone else has one. What of it?''"

    MAX "{color=#34B7EB}''Nothing! I didn’t mean anything by it, I promise.''"

    CHASE "{color=#FFCB70}''It’s because of me. I also have a food allergy.''"

    show roy angry

    ROY "{color=#82C26E}''Well you didn’t have to say it...''"

    """
    {color=#34B7EB}The tall boy finished his drink and exerted a mild sigh as the short one sipped his slowly. He doesn’t look like he’s going to finish it any time soon.

    {color=#34B7EB}I guess both of them knew that too, since they both got up as soon as the first one was finished.
    """

    CHASE "{color=#FFCB70}''Well, that was nice. Thanks for the drink, mister barista guy! We’ll be heading out now.''"

    show roy embarrassed

    ROY "{color=#82C26E}''Yeah, let’s get out of here.''"

    MAX "{color=#34B7EB}''Alright, bye then! Hope to see you back again soon!''"

    hide chase with dissolve
    hide roy with dissolve

    """
    {color=#34B7EB}The short boy grabs his drink and leaves quickly while the tall one lobs his empty cup toward the trash can.

    {color=#34B7EB}He misses by at least a couple feet, and almost doesn’t pick it up before his buddy nags him to do so. They continue to make idle banter all the while.
    """

    ROY "{color=#82C26E}''Sheesh. That barista guy probably thinks I’m a total geek...''"

    CHASE "{color=#FFCB70}''Either that or just a big idiot.''"

    play sound "sfx_room_footsteps_exit.ogg"

    "{color=#34B7EB}The last thing I hear before the doors close is the short boy making a wide range of unintelligible, goblin-like noises."



    # (if drink has milk)
    label d4i4bad:
    MAX "{color=#34B7EB}''So, how do you guys like it?''"

    show roy neutral

    ROY "{color=#82C26E}''It’s alright.''"

    show chase neutral
    # play stomach gurgling sound effect

    CHASE "{color=#FFCB70}''...
    That isn’t good.''"

    show roy inquire

    ROY "{color=#82C26E}''What isn’t?''"

    "{color=#34B7EB}A loud gurgling noise sounded from the tall boy’s stomach. The short boy was visibly concerned, but the one doing the gurgling seemed no worse for wear."

    CHASE "{color=#FFCB70}''Do you guys have a bathroom here?''"

    MAX "{color=#34B7EB}''Uh, yeah. It’s on the right hand side of the back wall.''"

    "{color=#34B7EB}The tall boy made a brisk speed walk in the direction I pointed while the short one glared in my direction."

    show chase neutral at Position(xpos=-400, xanchor=0, yalign=0.22) with ease
    show roy inquire at Position(xalign=0.3, yalign=0.205) with ease
    show roy angry

    ROY "{color=#82C26E}''Hey, what part of ‘no milk’ didn’t you understand!?''"

    MAX "{color=#34B7EB}''I’m sorry! I didn’t mean to, I just...''"

    "{color=#34B7EB}I don’t really have anything to say to that. He’s right, I did screw up the literal only direction they gave me... I hope Laura doesn’t find out about this."

    show roy angry at Position(xalign=0.1, yalign=0.22) with ease
    show chase neutral at Position(xalign=0.5, yalign=0.22) with ease

    CHASE "{color=#FFCB70}''Phew, okay, I think we should be heading home now. I’m not feeling too great.''"

    ROY "{color=#82C26E}''Yeah, I wonder why.''"

    show chase happy

    CHASE "{color=#FFCB70}''Well, see you barista guy!''"

    MAX "{color=#34B7EB}''Uh, bye!? I’m really sorry, by the way!''"

    CHASE "{color=#FFCB70}''It’s alright! Mistakes happen, you know?''"

    hide chase with dissolve
    hide roy with dissolve

    play sound "sfx_room_footsteps_exit.ogg"

    "{color=#34B7EB}The two leave in quite a hurry, with the short one giving me the evil eye until we were out of each other’s view. Did I just do something awful?"
    "{color=#34B7EB}Maybe I should leave the rest of the specialty orders to Ed in the future..."



    jump D4Outro
