    label D2I3:

    play sound "sfx_room_footsteps_enter.ogg"

    "{color=#34B7EB}As I scrub the counter for seemingly the twenty seventh time in the past minute, my endless monotony is thankfully cut short by the sound of heavy footsteps. At the door, an unusually wide man in a clean suit walks up to the counter."

    show brad neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Hello there, welcome to La Piovosita! Can I get you anything?''"

    BRAD "{color=#d9d97e}''Let me think...''"

    "{color=#34B7EB}His voice is gruff and deep, like Santa Claus gargling a mouthful of nails. He takes a moment to eyeball the menu, audibly scratching his beard in the process, before answering me."

    show brad think

    BRAD "{color=#d9d97e}''Eh, just get me the strongest thing on the menu.''"

    MAX "{color=#34B7EB}''Um, what do you mean by strong exactly? Do you mean like caffeine...?''"

    BRAD "{color=#d9d97e}''...''"
    BRAD "{color=#d9d97e}''...Yes.''"

    MAX "{color=#34B7EB}''Okay, then. I’ll see what I can do!''"
    "{color=#34B7EB}He didn’t sound totally certain about it, but I guess the customer is always right.
    So the drink with the most caffeine... that’d be the Entertainer, right? I think that’s its whole deal..."
    while makingdrink == 0:
        "{color=#34B7EB}He didn’t sound totally certain about it, but I guess the customer is always right.
        So the drink with the most caffeine... that’d be the Entertainer, right? I think that’s its whole deal..."
        pause

    $ makingdrink = 0


# Drink making minigame goes here.
# Anything works
    if coffee == 1 and Chocolate == 1 and espresso == 1:
        jump D2I3good
    else:
        jump D2I3bad


    label D2I3good:
    MAX "{color=#34B7EB}''Alright, this one’s called the Entertainer! It has the most caffeine of anything on the menu!''"

    show brad neutral

    label D2I3bad:
    BRAD "{color=#d9d97e}''Thank you.''"

    "{color=#34B7EB}The man takes a hearty sip and shows no reaction. Wiping his beard of residual coffee, he places the drink back on the counter while failing to cover a burp with his fist."

    MAX "{color=#34B7EB}''How is it?''"

    show brad think

    BRAD "{color=#d9d97e}''It wasn’t really what I was looking for.''"

    MAX "{color=#34B7EB}''I’m sorry to hear that... Do you want me to make you something else?''"

    show brad neutral

    BRAD "{color=#d9d97e}''I’m alright, lad.
    I think I just came in here looking for the wrong thing.''"

    MAX "{color=#34B7EB}''Mind if I ask what exactly you were looking for?''"

    show brad think

    BRAD "{color=#d9d97e}''Hm...
    That depends, how old are you?''"

    MAX "{color=#34B7EB}''I’m twenty one, sir.''"

    show brad shock

    BRAD "{color=#d9d97e}''You’re what!?''"
    BRAD "{color=#d9d97e}''I was guessing around the fifteen mark, and I thought that was conservative! And yet here you are, old enough that I could sit by your side at the bar!
    Kids these days are just looking younger and younger...''"

    MAX "{color=#34B7EB}''What did kids look like back in your day, sir?''"

    show brad neutral

    BRAD "{color=#d9d97e}''Truthfully I don’t think they looked any different...
    You don’t have to pay me any mind, kid. No need to burden yourself by humoring a rambling old man like myself.''"

    MAX "{color=#34B7EB}''Well, maybe I want to humor you.''"

    BRAD "{color=#d9d97e}''I don’t think I could believe that.''"

    MAX "{color=#34B7EB}''I mean, it’s not like I have anything better to do.''"

    "{color=#34B7EB}The man strokes his beard thoughtfully once more, grunting solemnly to himself. He then lets out a hearty laugh, the strength of which causes me to physically flinch."

    show brad happy

    BRAD "{color=#d9d97e}''Gahahaha! I suppose you’re right, lad! Though I’ll have you know I’m far more interesting after a few drinks!''"

    MAX "{color=#34B7EB}''Well, I could make you something else if you want.''"

    show brad neutral

    BRAD "{color=#d9d97e}''...''"

    show brad happy

    BRAD "{color=#d9d97e}''Ha! It seems like you don’t need a thing to be a riot!
    I’ll tell you what, I should be on my way right about now, but if you really want to humor me, then maybe I’ll come back sometime.''"

    "{color=#34B7EB}The man gets up to leave, but as he does so I notice he left his drink on the counter."

    hide brad with dissolve

    MAX "{color=#34B7EB}''Oh, sir, you left your coffee!''"

    BRAD "{color=#d9d97e}''You can keep it.''"

    MAX "{color=#34B7EB}''Are you sure? You barely drank any of it! I can make something else for you if you want!''"

    BRAD "{color=#d9d97e}''Son, there’s only one thing I want you to do for me...''"

    "{color=#34B7EB}He stands in the doorframe, stops for a second, and then turns his head back at me. He then cracks the biggest smile I’ve ever seen, pairing it with a thumbs up on a heavily bandaged left hand."

    BRAD "{color=#d9d97e}''I want you to keep on the straight and narrow, and always do your best!''"

    play sound "sfx_room_footsteps_exit.ogg"

    """
    {color=#34B7EB}The man then turns back around and leaves as if something unbelievably cheesy didn’t just come out of his mouth. Even ignoring the fact that he asked for two things, not one, I have no idea how to react to that.

    {color=#34B7EB}Thankfully I don’t have to since, you know, he left, but what actually just happened?

    {color=#34B7EB}Maybe I could use a drink right about now...
    """



    jump D2I4
