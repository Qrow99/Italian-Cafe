# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main Characters
define MAX = Character("Me", color="#34B7EB")
define ED = Character("Ed", color="#EBB134")
define LAURA = Character("Laura", color="#ff3636")

# Day 1 characters
define JUNE = Character("Shifty Girl", color="#4969de")
define USBNA = Character("Loud Girl", color="#fa9def")
define SBNA = Character("Sahbreena", color="#fa9def")
define AMC = Character("Amnesty", color="#ff7566")
define UAMC = Character("Redhead Girl", color="#ff7566")


# Day 2 characters
define BRAD = Character("Large Man", color="#d9d97e")
define SM = Character("Strange Man", color="#d1bc88")

# Day 3 characters
define KRN = Character("Mechanical Girl", color="#4BE54B")
define URTO  = Character("Beatnik Guy", color="#e0e0e0")
define UCYN = Character("Beatnik Girl 1", color="#d4d4d4")
define UBGT = Character("Beatnik Girl 2", color="#e8e8e8")


# Day 4 characters
define BND = Character("Brenda", color="#b459ff")
define UBND = Character("Headphone Girl", color="#b459ff")
define CHASE = Character("Tall Boy", color="#FFCB70")
define ROY = Character("Scrawny Boy", color="#82C26E")
define ERN = Character("Thin Girl", color="#ffd6ff")
define ALL = Character("All Beatniks", color="#cccccc")

# Day 5 characters
define RTO  = Character("Roberto", color="#e0e0e0")
define CYN = Character("Cynthia", color="#d4d4d4")
define BGT = Character("Bridget", color="#e8e8e8")




image milk = "MilkIdle.PNG"
image Chocolate = "ChocolateIdle.PNG"
image Cinnamon = "Cinnamonidle.PNG"
image PumpkinSpice = "PumpkinIdle.PNG"
# The original step buttons have thick outlines so they're going, too
'''
image stepback = "NextStepIdle.png"
image stepforward = "NextStepIdle.png"
'''

# The game starts here.

label start:
    show screen MenuButton
    show screen ResetButton
    show screen ConfirmButton
    show screen CoffeeButton
    show screen EspressoButton
    show screen PumpkinButton
    show screen MilkButton
    show screen ChocolateButton
    show screen CinnamonButton
    show screen NextButton
    show screen Prevbutton

# Quick menu, now in a more convenient location
    show screen SaveButton
    show screen BackButton
    show screen SkipButton
    show screen AutoButton
    show screen HistoryButton
    show screen PrefsButton


    # Variables
    python: # actually does the exact same thing as the $, except everything indented is 'real' python
        coffee = 0 # variable for Coffeemaking, False = 0, True = 1
        Milk = 0
        Cinnamon = 0
        Chocolate = 0
        Pumpkin = 0
        pagenum = 0 #will be used later for switching pages (possibly, not quite sure how im gonna do that atm)
        foam = 0
        Espresso = 0
        ExtraShot = 0
        creamer = 0
        whip_cream = 0
        steam = 0
        makingdrink = 0
        chichi = 0
        thirdguy = 0
        secondguy = 0
        firstguy = 0
        Brenda = 0
    # The Background
    scene bg room


    # Buttons
    # Turns out the milk button was asymmetrical on the original background
    # so I'm removing this one. I fixed the actual button, as well
    # show milk at Position(xalign=0.853, yalign=0.223)
    show Chocolate at Position(xalign=0.853, yalign=0.2995)
    show Cinnamon at Position(xalign=0.941, yalign=0.223)
    show PumpkinSpice at Position(xalign=0.941, yalign=0.2995)
    # show stepback at Position(xalign=0.77, yalign=0.1846)
    # show stepforward at Position(xalign=0.9882, yalign=0.1846)


    # This jumps to day 1
    jump DAY1



    # This jumps to the Karen event
    jump D3I2

    # This ends the game.

    return
