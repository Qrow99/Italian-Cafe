# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image fuck = "IngredientIdle.png"
image fuck2 = "IngredientIdle.png"
image fuck3 = "IngredientIdle.png"
image fuck4 = "IngredientIdle.png"
image stepback = "NextStepIdle.png"
image stepforward = "NextStepIdle.png"

image him = "ThatGuy.png"

# The game starts here.

label start:


    show screen MenuButton
    show screen ResetButton
    show screen ConfirmButton
    show screen Button11
    show screen Button12
    show screen NextButton

    $ drinksizes = 0
    $ drinktypes = 0
    $ step = 1
    $ readyfornext = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show him at Position(xalign=0.3, yalign=0.19)
    show fuck at Position(xalign=0.853, yalign=0.22)
    show fuck2 at Position(xalign=0.853, yalign=0.2995)
    show fuck3 at Position(xalign=0.941, yalign=0.223)
    show fuck4 at Position(xalign=0.941, yalign=0.2995)
    show stepback at Position(xalign=0.77, yalign=0.1846)
    show stepforward at Position(xalign=0.9882, yalign=0.1846)

    # These display lines of dialogue.

    e "You've created a newish Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "This whole coffee making thing also works IN THE BACKGROUND."
    e "So you can make it while talking to people!"
    e "Don't know why you'd want to do that, but you can."

    # This ends the game.

    return
