# NEW THINGS
# A sample interaction is now in
# it only uses placeholder art as well as sounds from the last project
# also the in game ui is darker now, but again still a placeholder so whatever


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image milk = "MilkIdle.PNG"
image Chocolate = "ChocolateIdle.PNG"
image Cinnamon = "Cinnamonidle.PNG"
image PumpkinSpice = "PumpkinIdle.PNG"
image stepback = "NextStepIdle.png"
image stepforward = "NextStepIdle.png"

image rick = "ThatGuy.png"

# The game starts here.

label start:
    show screen MenuButton
    show screen ResetButton
    show screen ConfirmButton
    show screen CoffeeButton
    show screen EspressoButton
    show screen NextButton
    show screen Backbutton



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rick at Position(xalign=0.3, yalign=0.22)
    show milk at Position(xalign=0.853, yalign=0.22)
    show Chocolate at Position(xalign=0.853, yalign=0.2995)
    show Cinnamon at Position(xalign=0.941, yalign=0.223)
    show PumpkinSpice at Position(xalign=0.941, yalign=0.2995)
    show stepback at Position(xalign=0.77, yalign=0.1846)
    show stepforward at Position(xalign=0.9882, yalign=0.1846)

    # These display lines of dialogue.

    e "You've created a newish Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "This whole coffee making thing also works IN THE BACKGROUND."
    e "So you can make it while talking to people!"
    e "Don't know why you'd want to do that, but you can."

    hide rick

    jump D3I2

    # This ends the game.

    return
