    label D3I2:

    define MAX = Character("Me", color="#34B7EB")
    define KRN = Character("Mechanical Girl", color="#4BE54B")

    """
    {color=#34B7EB}As the customer made their way out the door, I decided to clean up the counter space in the meantime.

    {color=#34B7EB}It’s essentially just as clean as it was when I got here, save for a minor stain of condensation where the last customer’s drink was, but I still feel like I should be doing... something.

    {color=#34B7EB}Thankfully, the opportunity to do something revealed itself, as another customer made her way through the front door.
    """

    # here is where the sound effects will go when they are made
    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_enter.ogg"

    """
    {color=#34B7EB}As she approached the counter she stared intently around the building, quickly darting her eyes back and forth, though her head remained completely motionless.

    {color=#34B7EB}In fact, a lot of things about her seem kind of... off. Her footsteps are unusually rhythmic, and I don’t think I’ve seen her blink once since she entered the room.
    """

    play music "WBoK_music1_v3.ogg" loop fadein 5.0

    show karen neutral at Position(xalign=0.3, yalign=0.22) with dissolve

    MAX "{color=#34B7EB}''Welcome to La Piovositá’s, miss! How can I help you?''"

    KRN "{color=#4BE54B}''I would like to ask some questions about this establishment.''"

    MAX "{color=#34B7EB}''Um... sure thing?''"

    KRN "{color=#4BE54B}''Thank you.
    Firstly, may I confirm that this establishment is the La Piovositá Café, which is currently under the ownership of Laura Portain?''"

    MAX "{color=#34B7EB}''Sounds right to me. Weirdly specific, but right.''"

    show karen inquire

    KRN "{color=#4BE54B}''I see. Secondly, has this building changed ownership within the past two months?''"

    MAX "{color=#34B7EB}''I, uh... I think so?
    I know it happened pretty recently, but I’ve only been here for, like, a week so I don’t know..."

    KRN "{color=#4BE54B}''Any information is appreciated. Furthermore, may I ask the median caffeine content of all the beverages served here?''"

    MAX "{color=#34B7EB}''Well, uh... I think... I have no idea.
    Hey, not to be rude, but can I get an estimate on how many questions you plan on asking? Not that I have anything else to do, just curious.''"

    show karen neutral

    KRN "{color=#4BE54B}''I currently have 27 queued points of inquiry, with the potential of more to be developed as our conversation continues.''"

    MAX "{color=#34B7EB}''...Alrighy, then. Maybe we should continue this discussion over a drink? How about I whip something up for you real quick?''"

    KRN "{color=#4BE54B}''That would be most appreciated.
    Questions 3-11 are all inquiries regarding this cafè’s menu. Perhaps an adequate place to start would be question 5: What is La Piovosita’s most popular menu item?''"

    MAX "{color=#34B7EB}''Our most popular drink? Coming right up!''"

    "{color=#34B7EB}Most popular drink, huh? Weren’t Ed and Laura saying something about that earlier this afternoon...?"


    # This is where the drink is made
    # Any drink will suffice


    MAX "{color=#34B7EB}''Alright, here it is! The most popular drink on the menu! I think. Be careful, it’s hot!''"

    "{color=#34B7EB}Without hesitation, the girl looked down at her drink, stuck out her hand, and gently placed her index finger into the cup. After a few seconds of complete silence, she removed it and returned her gaze to my direction."

    KRN "{color=#4BE54B}''You are correct. The beverage is significantly above room temperature.''"

    MAX "{color=#34B7EB}''...Right.''"

    "{color=#34B7EB}This girl’s really freaking me out. It’s like she’s not even human! Like a robot or something! But then again, what would a robot be doing at a café? Actually, that gives me an idea..."

    MAX "{color=#34B7EB}''Hey, what are you doing at a café?''"

    show karen inquire

    KRN "{color=#4BE54B}''Pardon me? Is it unusual for people to order a beverages and converse with baristas at cafés such as this?''"

    MAX "{color=#34B7EB}''Well, no. Actually, it isn’t unusual at all when you put it like that. Sorry if I came off as kind of pushy.''"

    show karen neutral

    KRN "{color=#4BE54B}''Apology accepted. However, I do not mind answering your question; my current objective is to obtain knowledge of the establishment, seeing as it has only recently replaced the one which used to stand in its place.''"

    MAX "{color=#34B7EB}''So what you’re saying is, you’re here to check out the place just because it’s new?
    That’s a... surprisingly mundane reason.''"

    KRN "{color=#4BE54B}''Yes. It has come to my attention that 27 percent of online satellite maps still indicate this building to be under its previous ownership, so I came here to confirm if this assertion was accurate.''"

    "{color=#34B7EB}That’s more what I was expecting."

    KRN "{color=#4BE54B}''Although I have not yet acquired all the information I desire, the information I have gathered is sufficient for the day. Additionally, the employees here appear equally ignorant to the majority of the data I desire. Henceforth, I will now be taking my leave. Goodbye.''"

    MAX "{color=#34B7EB}''Really? Well, uh, goodbye then! Have a nice day!''"

    stop music fadeout 5.0
    hide karen with dissolve
    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_exit.ogg"

    "{color=#34B7EB}In the same straight faced, rhythmic fashion she entered, the girl left the building. It then suddenly dawned upon me that she hadn’t taken with her the drink she purchased, nor did she actually, you know, drink any of it. I’m honestly not that surprised."


    # This is the end of the interaction

    return
