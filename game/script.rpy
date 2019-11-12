# NEW THINGS
# A sample interaction is now in
# it only uses placeholder art as well as sounds from the last project
# also the in game ui is darker now, but again still a placeholder so whatever


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Main Characters
define MAX = Character("Me", color="#34B7EB")
define ED = Character("Ed", color="#EBB134")
define LAURA = Character("Laura", color="#ff3636")

# Day 1 characters
define JUNE = Character("Shifty Girl", color="#4969de")

# Day 2 characters
define BRAD = Character("Large Man", color="#d9d97e")

# Day 3 characters
define KRN = Character("Mechanical Girl", color="#4BE54B")

# Day 4 characters
define BND = Character("Brenda", color="#b459ff")
define UBND = Character("Headphone Girl", color="#b459ff")
define CHASE = Character("Tall Boy", color="#FFCB70")
define ROY = Character("Scrawny Boy", color="#82C26E")



image milk = "MilkIdle.PNG"
image Chocolate = "ChocolateIdle.PNG"
image Cinnamon = "Cinnamonidle.PNG"
image PumpkinSpice = "PumpkinIdle.PNG"
image stepback = "NextStepIdle.png"
image stepforward = "NextStepIdle.png"


# The game starts here.

label start:
    show screen MenuButton
    show screen ResetButton
    show screen ConfirmButton
    show screen CoffeeButton
    show screen EspressoButton
    show screen NextButton
    show screen Backbutton


    # Variables
    $ coffee = 0 # variable for Coffeemaking, False = 0, True = 1



    # The Background
    scene bg room


    # Buttons
    show milk at Position(xalign=0.853, yalign=0.22)
    show Chocolate at Position(xalign=0.853, yalign=0.2995)
    show Cinnamon at Position(xalign=0.941, yalign=0.223)
    show PumpkinSpice at Position(xalign=0.941, yalign=0.2995)
    show stepback at Position(xalign=0.77, yalign=0.1846)
    show stepforward at Position(xalign=0.9882, yalign=0.1846)


    # This jumps to day 1
    jump DAY1



    # This jumps to the Karen event
    jump D3I2

    # This ends the game.

    return
