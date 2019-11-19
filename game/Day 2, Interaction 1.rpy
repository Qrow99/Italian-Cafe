    label D2I1:

    """
    {color=#34B7EB}The cafe is quiet. Outside the sun looks like it's just about to begin its descent into the horizon.
    """

    # sound effects

    """
    {color=#34B7EB}A man enters the café, drenched head-to-toe. It isn't raining. He approaches the counter, an eerie smile on his face. His arms are long and thin, and his hands twitch nervously. He's dressed in an oversized trenchcoat. I feel unnerved.
    """

    show alien neutral at Position(xalign=0.3, yalign=0.205) with dissolve

    MAX "{color=#34B7EB}''Hello, sir? How may I help you?''"

    show alien happy

    SM "{color=#d1bc88}''Yes, I believe you can help me.''"

    MAX "{color=#34B7EB}''Oh...kay?''"

    SM "{color=#d1bc88}''I...would like some of that tart bean juice your kind likes to consume. With the...ah...white liquid your domesticated animal excretes from its body?''"

    MAX "{color=#34B7EB}''So...a latte?''"


    # (A/N i was thinking of leaving this out and having the player figure out what he wants. Also yes, i know how that line sounds)

    """
    {color=#34B7EB}The man doesn't respond. He just continues to stare forward, unflinchingly. I wait a moment for a response, assuming he's just deep in thought, but the only sound I hear is a strange, low buzzing noise.

    {color=#34B7EB}Quickly, it stops. I suddenly feel compelled to make this man's drink as quickly as possible.

    {color=#34B7EB}He said he wanted a latte, right? The Fairytale of New York is a latte I'm pretty sure. Guess I should just make that...
    """

    """
    {color=#34B7EB}As I finish making the drink, the man jolts to attention, staring at me now instead of the wall.
    """

    show alien neutral

    SM "{color=#d1bc88}''Sorry. Translator's broken.''"

    MAX "{color=#34B7EB}''Ah, I see..."
    MAX "{color=#34B7EB}''Here...you go..."

    "{color=#34B7EB}The man takes the latte. Then he eats it. Cup and all."

    MAX "{color=#34B7EB}''Ha...ha......enjoy......''"

    SM "{color=#d1bc88}''I don't believe I'll be visiting this quadrant again. Too many bees.''"

    MAX "{color=#34B7EB}''Bees?''"

    SM "{color=#d1bc88}''Yes. Bees. Your kind made a whole movie about them. I mean, what's so great about them anyway?!''"

    MAX "{color=#34B7EB}''I don't know, sir.''"

    SM "{color=#d1bc88}''And your planet's authorities are so touchy.''"

    MAX "{color=#34B7EB}''Planet...?''"

    show alien happy

    SM "{color=#d1bc88}''Speaking of which, I should get going soon. Those crazy UFO people don't rest, do they? Anyway, thanks for the snack! Ciao!''"

    hide alien with dissolve

    """
    {color=#34B7EB}The man leaves. Through the window I can see his silhouette. He takes off his trenchcoat, and four long, insect-like wings spring out. The silhouette changes as he grows four arms, two barbed legs, and a stinger. The creature buzzes away.

    {color=#34B7EB}I suddenly remember that I absolutely hate wasps.
    """


    jump D2I2
