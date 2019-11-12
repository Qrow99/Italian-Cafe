    label D4I3:

    # play sound "sfx_room_bell_enter.ogg"
    play sound "sfx_room_footsteps_enter.ogg"

    "{color=#34B7EB}A girl comes in and the faint sound of explosive EDM accompanies her. She hums along to the music as she walks in, and upon further inspection said music appears to be coming out of a massive headset she has positioned on her shoulders."

    show brenda neutral at Position(xalign=0.3, yalign=0.22) with dissolve

    MAX "{color=#34B7EB}''Welcome to La Piovosita! Can I get you something?''"

    UBND "{color=#b459ff}''Yeah, can I get a...''"

    show brenda angry

    UBND "{color=#b459ff}''Hey wait a minute, who are you?''"

    MAX "{color=#34B7EB}''Well, uh... I’m a barista? Why do you ask?''"

    show brenda inquire

    UBND "{color=#b459ff}''Where’s the big guy? The one who’s usually here?''"

    MAX "{color=#34B7EB}''Are you talking about Ed? Unfortunately he’s sick today, sorry.''"

    show brenda angry

    UBND "{color=#b459ff}''Really? That sucks. I always like chatting with him. Or at him, more accurately. He isn’t much of a talker.''"

    MAX "{color=#34B7EB}''Yeah, that sounds like Ed.''"

    show brenda neutral

    UBND "{color=#b459ff}''Sorry if I came off as rude, by the way. I’m genuinely curious as to who you are. I’ve never seen around before.''"

    MAX "{color=#34B7EB}''Oh, well, my name’s Max. And you probably haven’t seen me because I’m new! This is my first week working, actually.''"

    show brenda happy

    BND "{color=#b459ff}''That makes sense. My name’s Brenda, by the way. Nice to meet ya.
    And you said you started working this week? What’re your shifts like?''"

    MAX "{color=#34B7EB}''I work from three to five every afternoon, and have every day this week.''"

    "{color=#34B7EB}The remark seemed totally normal and uninteresting to me, as true factual statements usually are, but for some reason Brenda gave me a confused look in response."

    show brenda confused

    BND "{color=#b459ff}''That can’t be right.''"

    MAX "{color=#34B7EB}''What do you mean?''"

    show brenda angry

    BND "{color=#b459ff}''There’s no way you work from three to five every day! I’ve come here at four o’ clock on the dime for the past three weeks and I’ve never seen you before in my life!''"

    MAX "{color=#34B7EB}''I’m telling the truth, honestly! I don’t know how we haven’t managed to see each other throughout the whole week, but I’m not lying! Come to think of it, my shift would be kind of a weird thing to lie about...''"

    show brenda confused

    BND "{color=#b459ff}''Hm... Well, you sure don’t look like a liar, but I still don’t get how we haven’t managed to bump into each other all week. I thought the big guy was the only one who worked here, minus the loud red haired lady that comes out from time to time.''"

    MAX "{color=#34B7EB}''I don’t think anyone except us three work here... But yeah I agree it’s quite strange that we haven’t met. Maybe we can talk about it over a drink?''"

    show brenda neutral

    BND "{color=#b459ff}''Sounds good to me. How about a Dark Sun?''"

    MAX "{color=#34B7EB}''I’m on it!''"

    "{color=#34B7EB}Alright, a Dark Sun. For some reason, I feel like I’m supposed to be doing something right now? Not sure why. Weird."

# Drink Minigame here
# Correct answer is a Dark Sun with an extra shot of espresso

    "{color=#34B7EB}I hand her the drink, and she gives it a few good puffs of air before taking a sip. She licks her lips and then puts on a face of rumination, as if she were pondering deeply on the flavor."

# (if the drink is made normally)
    show brenda confused

    BND "{color=#b459ff}''Hm... it’s different than usual.''"

    MAX "{color=#34B7EB}''It is?''"

    BND "{color=#b459ff}''Yeah... did you guys change the menu within the past day?''"

    MAX "{color=#34B7EB}''I don’t think so.''"

    show brenda neutral

    BND "{color=#b459ff}''Huh. Weird. Well, thanks for it regardless! Though I just remembered I’ve got some work to get done, so I’ll talk to you later.
    Oh yeah, and tell the big guy I said hi when he comes back, alright?''"

    MAX "{color=#34B7EB}''I’ll be sure to tell him!''"

# (if the drink has an espresso shot)
    show brenda happy

    BND "{color=#b459ff}''Perfection, as usual. Man, you guys have the best drinks here.''"

    MAX "{color=#34B7EB}''Thank you! Is it safe to assume that’s why you come here so often?''"

    show brenda inquire

    BND "{color=#b459ff}''It’s one of the three reasons. I’d say the drink quality falls right in between the fact that there’s free wifi and the fact that it’s marginally cooler in here than it is outside.''"

    MAX "{color=#34B7EB}''Not a big fan of the heat, huh?''"

    show brenda angry

    BND "{color=#b459ff}''I can’t stand anything above, like, sixty degrees. And the dorm I live in doesn't have a functioning AC, so, yeah the fans here are a pretty big plus.''"

    MAX "{color=#34B7EB}''Does your dorm not have wifi either?''"

    show brenda neutral

    BND "{color=#b459ff}''It does, but it’s still nicer to play video games here, on account of the aforementioned heat.''"

    MAX "{color=#34B7EB}''Oh, you play games?''"

    show brenda inquire

    BND "{color=#b459ff}''When I get the chance. Do you?''"

    MAX "{color=#34B7EB}''Not me, but my brother does. What do you play? Chances are he’s talked about it at some point.''"

    BND "{color=#b459ff}''I spend most of my time playing ‘Guild of Greats.’ You heard of it?''"

    MAX "{color=#34B7EB}''Maybe? Is that the one with a big open world and customizable characters and stuff?''"

    show brenda neutral

    BND "{color=#b459ff}''Not even close, but it’s not that important. Anyways, thanks for the drink, I think I’m gonna get started on my play session.
    Oh yeah, and tell the big guy I said hi when he comes back, alright?''"

    MAX "{color=#34B7EB}''I’ll be sure to tell him!''"


# Both correct and incorrect drinks converge here

    play sound "sfx_room_footsteps_exit.ogg"
    hide brenda with dissolve

    """
    {color=#34B7EB}Brenda stands up and makes a beeline for the table in the farthest corner of the room.

    {color=#34B7EB}She takes an exceptionally large laptop out of her bag, slides on her equally large headphones, and I come to the conclusion that the outside world won’t be distracting her any time soon.

    {color=#34B7EB}I still can’t believe I’ve managed to not talk to her at all this week. She couldn’t be lying about coming in every day, right? Why would she? Maybe I’ve seen her around every day, but only ever out of the corner of my eye.

    {color=#34B7EB}Usually I’m too busy needlessly cleaning up the counter or staring anxiously at the door to even acknowledge any other customers in the café, so I’d be willing to bet on it.

    {color=#34B7EB}But what I’m wondering is how she could have come in every single day during my shift without me ever noticing!? Every shift I just stand here until I leave, right?

    {color=#34B7EB}Unless I just somehow managed to serve her and not remember her? I wouldn’t put it past me, but she didn’t recognize me either.

    {color=#34B7EB}Is there anything special about today? A sort of joke holiday or mass amnesia? Probably not.

    {color=#34B7EB}The only difference I can think of is that... Ed isn’t here. He wasn’t here to give me a break. Which he does at the same time every day.

    {color=#34B7EB}I decide to shoot Ed a quick text. ‘Hey, do you know this Brenda girl who just walked in?’

    {color=#EBB134}‘Did she say anything about me?’ {color=#34B7EB}he responds. Not what I was expecting.

    {color=#34B7EB}‘She told me to tell you hi.’ I text. {color=#EBB134}‘Can you tell her hi back?’ {color=#34B7EB}he responds rather quickly.

    {color=#34B7EB}I don’t think I’ll be able to get to her from behind that headset, but Ed doesn’t have to know that.

    {color=#34B7EB}‘Sure thing.’ I respond.

    {color=#34B7EB}He says {color=#EBB134}‘thanks,’ {color=#34B7EB}and I decide there’s no real need to say any more, especially while he’s sick and I’m at work.

    {color=#34B7EB}I wonder why he was so insistent on knowing about what she said. Ed’s never been all that good with subtlety, but he really seemed to be cutting to the chase.

    {color=#34B7EB}Maybe he has a crush on her?

    {color=#34B7EB}I guess I shouldn’t assume stuff like that, but on the other hand, that would explain a lot of the things he did this week... I think I’ll just ask him after my shift.
    """

    jump D4I4
