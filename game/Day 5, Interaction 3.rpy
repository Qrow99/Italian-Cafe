    label D5I3:


    "{color=#34B7EB}Through the doors enters an equally formidable and familiar man, head hung low and arms firmly crossed."

    play sound "sfx_room_footsteps_enter.ogg"
    play music "mus_main_loop_cafejazz6.ogg" fadein 3.0
    show brad neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Welcome back to La Piovosita, mister!''"

    BRAD "{color=#d9d97e}''Thanks.''"

    MAX "{color=#34B7EB}''Can I get you anything?''"

    BRAD "{color=#d9d97e}''I’m alright.''"

    """
    {color=#34B7EB}The man sits down at the counter and stares into space, hardly even acknowledging me.

    {color=#34B7EB}I was expecting his next appearance here to be eccentric and jovial, seeing as that’s how he left, but now he’s just hanging his head, leaning on the counter. It’s kinda depressing, honestly.
    """

    MAX "{color=#34B7EB}''So, have any wisdom you’d like to share today, sir?''"

    show brad think

    BRAD "{color=#d9d97e}''You’ve no need to continue to humor me, lad. Young people like yourself don’t want to hear the advice of an old man. No one does.''"

    """
    {color=#34B7EB}His demeanor today is a far cry from that of a few days ago. I guess he’s just having a bad morning?

    {color=#34B7EB}Regardless, I’m actually quite happy to see the big man today of all days. Considering I’ve been on a kick of asking random people for advice, I think this guy showing up here today could potentially benefit both of us.
    """

    MAX "{color=#34B7EB}''Actually, sir, I was quite looking forward to talking with you today.''"

    show brad neutral

    BRAD "{color=#d9d97e}''Really, it’s alright kid. You shouldn’t ask people for things you don’t really want.''"

    MAX "{color=#34B7EB}''Well, what if what I really want is to hear the ramblings of an old man?''"

    show brad shock

    BRAD "{color=#d9d97e}''...Is it really?''"

    MAX "{color=#34B7EB}''Only if you’d be willing to humor me.''"

    show brad happy

    BRAD "{color=#d9d97e}''...Hmph. Well, I suppose I could do that!
    I’m sorry for my despondency, lad, It’s been quite a day.
    I’d be happy to do some rambling over a drink! Let’s see here... how about an Entertainer?''"

    MAX "{color=#34B7EB}''Coming right up, sir!''"

    $ order = 1

    while makingdrink == 0:
        "{color=#34B7EB}I’m still not sure how I feel about being called ‘lad,’ but I guess it doesn’t matter. One Entertainer coming up!"
        #pause

    $ makingdrink = 0
    $ order = 0

    python:
        coffee = 0
        Espresso = 0
        Milk = 0
        Cinnamon = 0
        Chocolate = 0
        Pumpkin = 0
        foam = 0
        ExtraShot = 0
        creamer = 0
        whip_cream = 0
        steam = 0
        reset = 1



# Drink making minigame does here
# Any drink works fine.

    """
    {color=#34B7EB}I hand over the steaming cup of caffeine and he immediately brings it to his lips.

    {color=#34B7EB}He takes an immense swig and swallows the scalding drink in a single, manly gulp. He wipes his facial hair of anything that missed his mouth and reveals a great, toothy smile.
    """

    BRAD "{color=#d9d97e}''Alright son, what is it you’d like this old man to flap his gums about?''"

    MAX "{color=#34B7EB}''You got any advice on love?''"

    show brad think

    BRAD "{color=#d9d97e}''Ah, is someone having girl troubles?''"

    MAX "{color=#34B7EB}''More like lack of girl troubles...''"

    BRAD "{color=#d9d97e}''Ah yes, I’ve been there.
    What’s the situation? Looking for your type? Got a crush? If you’re comfortable sharing it, then let me hear it!''"

    MAX "{color=#34B7EB}''Crush. Let's say there’s this girl I like, but I don’t know what to say to her. We’ve talked here and there, but nothing even resembling a full conversation. Where should I even start?''"

    show brad neutral

    BRAD "{color=#d9d97e}''Not much of a basis, huh... Well then, you should start by getting to know her! Ask her some questions! People love to talk, and by the looks of things you’re already not too bad at listening.''"

    MAX "{color=#34B7EB}''Is it really that simple? Just making small talk?''"

    BRAD "{color=#d9d97e}''You have to start somewhere, don’t you? You’ve got to get in her mind before she leaves yours! You may be watching her from afar now, but you never know when this girl may just get up and leave your world forever!''"

    MAX "{color=#34B7EB}''Get up and leave, huh? Guess I didn’t think about that.''"

    show brad happy

    BRAD "{color=#d9d97e}''Many don’t. But hey, that’s why we’re talking, isn’t it? To share life experience!''"

    MAX "{color=#34B7EB}''I guess you’re right.''"

    show brad neutral

    BRAD "{color=#d9d97e}''And one last thing: when the time comes that you do really start to come down with a bad case of feelings, never forget the most effective way of letting someone know how you feel about them.''"

    MAX "{color=#34B7EB}''What’s that?''"

    show brad happy

    BRAD "{color=#d9d97e}''Tell them about it! Hahaha!''"

    MAX "{color=#34B7EB}''Fair enough, I guess!''"

    """
    {color=#34B7EB}The man gives a hearty laugh, slamming his fist onto the counter. It makes me happy to see his mood shift so dramatically.

    {color=#34B7EB}It may be a bit awkward standing in an otherwise silent room with an old man laughing to himself, but I’m happy that a drink and a few words could do that much for him.
    """

    BRAD "{color=#d9d97e}''Haha... Well lad, it seems it’s about time for me to head out.
    It’s been quite a pleasure speaking with you. It makes my heart happy seeing someone as young as yourself taking time out of your day to do good for others.''"

    MAX "{color=#34B7EB}''Likewise.''"

    play sound "sfx_room_footsteps_exit.ogg"
    hide brad with dissolve

    "{color=#34B7EB}As he got up from his seat and began to leave, the memory of his first appearance in the café returned to me. I’ve gotta know..."

    MAX "{color=#34B7EB}''Wait sir! Before you go, is there anything else you need from me?''"

    BRAD "{color=#d9d97e}''Hm? From you? Well, maybe one thing...''"

    "{color=#34B7EB}As I had hoped, the large man swung his head around, presenting a toothy grin and a dramatic thumbs up."

    BRAD "{color=#d9d97e}''I want you to keep being yourself, young man! Just do that, and I’m sure your girl trouble will be gone before you know it! Hahaha!''"

    stop music fadeout 3.0
    play sound2 "sfx_room_door_main_close.ogg"

    jump D5I4
