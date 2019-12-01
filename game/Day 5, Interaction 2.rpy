    label D5I2:

    """
    {color=#34B7EB}I casually stand at the counter, letting my mind wander. Once again, I hear the familiar sounds of faint music.

    {color=#34B7EB}Instead of one instrument, I hear a full band of music: the strum of a bass guitar, the gentle tap of a drum, jazzy piano and the smooth sax. Have they reached their final form?

    {color=#34B7EB}The upbeat music fills me with excitement and I slightly sway to the beat until I hear the sound of the doorbell jingling. The three of them enter and bob their head as they snap. They twirl and they greet me with a finger gun.

    {color=#34B7EB}I can tell they're in a good mood.
    """

    show roberto neutral at Position(xalign=0.3, yalign=0.205) with dissolve
    show cynthia neutral at Position(xalign=0.0, yalign=0.205) with dissolve
    show bridget neutral at Position(xalign=0.6, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Hey welcome back! What can I get for you all?''"

    show roberto happy

    URTO "{color=#e0e0e0}''Hey there juiceman, the juiceheads are here to drink up that sweet elixir you cook up.''"
    URTO "{color=#e0e0e0}''We want to celebrate because the handcuffs left for town, so we wanted to groove down with other fellow groovies. Stopped by your café to get some energy, maybe get some of that same drink that made me jive.''"

    show cynthia happy

    UCYN "{color=#d4d4d4}''The way he grooved down was amazing! Even though the last drink you made was cool, I want some of that far out juice!''"

    show bridget happy

    UBGT "{color=#d4d4d4}''Same here cool cat, haven't seen old man Roberto move that much in decades.''"

    show roberto neutral

    "{color=#34B7EB}The girl snickers at her sly comment and Roberto rolls his eyes and the other girl gives me pleading puppy dog eyes for the drink. This is one of the easiest orders I've had in days."

    MAX "{color=#34B7EB}''So three orders of The Entertainer coming right up!''"

    """
    {color=#34B7EB}The Beatniks cheer and give me the money with a large tip. They wait nearby while bobbing their heads to the jazz music—I gave up on trying to find out where the source is.
    """
    "{color=#34B7EB}I make the coffee with a sway in my hips. I'm pretty confident in my ability to make the Entertainer at this point."

    #*coffee gameplay*
    while makingdrink == 0:
        "{color=#34B7EB}I make the coffee with a sway in my hips. I'm pretty confident in my ability to make the Entertainer at this point."
        pause

    $ makingdrink = 0

    "{color=#34B7EB}I put the drinks on the counter and call them out."

    MAX "{color=#34B7EB}''Your order is up, Roberto and er uh—''"

    show cynthia neutral

    CYN "{color=#d4d4d4}''Cynthia.''"

    show bridget neutral

    BGT "{color=#d4d4d4}''Bridget. Sorry coffee man, we should've introduced ourselves earlier, but thanks for the juice.''"

    MAX "{color=#34B7EB}''Oh thanks, I'm Max by the way.''"

    "{color=#34B7EB}Roberto snaps his fingers to signal them to leave, but I stop them with a yelp."

    MAX "{color=#34B7EB}''Uh, Hey! Wait! Can I ask you guys something? If you have time?''"

    """
    {color=#34B7EB}I suddenly remembered that I had to ask them something, some advice for Ed. Perhaps these cool cats may have had some experience with love? Anything would help.

    {color=#34B7EB}The music abruptly stops and Roberto stands there in confusion as the other two girls hand him his drink. They walk over to me precariously.
    """

    show roberto happy

    RTO "{color=#e0e0e0}''Yeah we have some time, what's up juiceman? What do you want to ask us?''"

    MAX "{color=#34B7EB}''I have a friend named Ed who works here and I recently found out that he wants to confess to one of the café regulars, Brenda.''"

    MAX "{color=#34B7EB}''I was wondering if you can give some advice on love to help my buddy out? Um, is that okay with you?''"

    "{color=#34B7EB}They smile and the music plays once again, but a little softer and slower. The saxophone has some romantic undertones to it."

    RTO "{color=#e0e0e0}''Oh that's groovy man, yeah I'm hip when it comes to the chicks, I'll lend you some words of wisdom.''"

    show cynthia happy

    CYN "{color=#d4d4d4}''I can give a lil advice, I've written a fair amount of love poems, Daddy-O.''"

    show bridget happy

    BGT "{color=#d4d4d4}''I dig that man, yeah I'm in for giving advice too, after all you've been doing us a favor with your coffee, so time to give back.''"

    MAX "{color=#34B7EB}''Thanks a bunch guys. I really appreciate it!''"

    "{color=#34B7EB}I proceed to take out a notepad and a pen to intently absorb the information."

    show roberto neutral

    RTO "{color=#e0e0e0}''Tell him to not sweat it, man. Be relaxed and confident, don't freak out or you'll freak out the chick too, shows you're loose screw.''"

    show roberto happy

    RTO "{color=#e0e0e0}''If she says yes, cool cool, go and ape it out with your buddies if she says no, that's also cool—it'll be okay in the end. Plenty of other time to go quail hunting ya know?''"

    show cynthia neutral

    CYN "{color=#d4d4d4}''I haven't had much dating experience, but I suggest for the guy to have fun! If the chick says yes, then have some fun casual dates but don't jump in too quickly.''"

    show cynthia happy

    CYN "{color=#d4d4d4}''Get to know the gal first. Hey, he can use some of my love poems if he wants or use it as a mantra so the universe can give him some good energy!''"

    "{color=#34B7EB}She puts a folded piece of paper down the counter."

    show bridget neutral

    BGT "{color=#d4d4d4}''Roberto is a quail chaser and Cynthia is as clueless as a goose.''"
    BGT "{color=#d4d4d4}''I've had boy toy for 3 years so I know what's up and I'm a hipster at love—ask him why he genuinely likes the girl. If he seems into her as a person other than a superficial reason, then you tell him to go for it and just be himself.''"
    BGT "{color=#d4d4d4}''She has to like him for who he is anyway, if not she can blow out of the water. If he likes her for all the wrong reasons, then he can dummy it up.''"

    show bridget happy

    BGT "{color=#d4d4d4}''If he says what he needs to say to her, even if he struggles a little, then that's a whole load off your rocker. If she says yes, then coolio, get to know each other slowly and if you click then you click.''"
    BGT "{color=#d4d4d4}''He'll know what I mean. You just know when you can talk to them for hours without realizing that the day went by in a blink of an eye. If she says no, at least he manned up.''"

    "{color=#34B7EB}Damn, this girl sure knows her stuff. I've filled out pages just with her advice. I take the piece of folded paper and put it in my pocket."

    MAX "{color=#34B7EB}''Thanks so much guys, again, I really do appreciate it. The next time you go here, drinks are on me.''"

    "{color=#34B7EB}...Do I have enough money for that? Oh well, a promise is a promise. I'll just use their tips."

    "{color=#34B7EB}They cheer in unison and Roberto pats me on the shoulder."

    RTO "{color=#e0e0e0}''Thanks man, you're a real angel. Anytime ya need a friend, we're here for ya alright? Laters!''"

    hide roberto with dissolve

    CYN "{color=#d4d4d4}''Good luck with your friend! I believe in you!''"

    hide cynthia with dissolve

    BGT "{color=#d4d4d4}''Au revoir, tell your friend I said hi.''"

    hide bridget with dissolve

    "{color=#34B7EB}And with a flash, they snap out and start dancing like maniacs when they take a sip of their drink. I hope they have fun at their party."


    jump D5Break
