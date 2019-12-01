screen MenuButton():
    imagebutton:
        xalign 0.97 yalign 0.68
        idle "Menu_Idle.PNG"
        hover "Menu_Highlight.PNG"
        action Show("MenuList1"), Play("sound", "sfx_ui_click1.ogg")

screen ResetButton():
    imagebutton:
        xalign 0.97 yalign 0.449
        idle "Reset_Idle.PNG"
        hover "Reset_Highlight.PNG"
        action Notify("reset order"), SetVariable("coffee", 0), SetVariable('Espresso', 0), SetVariable("Milk", 0), SetVariable("Cinnamon", 0), SetVariable("Chocolate", 0), SetVariable("Pumpkin", 0), Play("sound", "sfx_ui_click1.ogg")

screen ConfirmButton():
    imagebutton:
        xalign 0.97 yalign 0.57
        idle "Submit_Idle.PNG"
        hover "Submit_Highlight.PNG"
        action Notify("ORDER UP"), SetVariable("makingdrink", 1), Play("sound", "sfx_ui_click1.ogg"), Play("sound", "sfx_room_coffee_pour.ogg")

screen NextButton():
    imagebutton:
        xalign 0.9882 yalign 0.1846
        idle "Next_Page_Idle.PNG"
        hover "Next_Page_Highlight.PNG"
        action Notify("next"), SetVariable("pagenum", 2),Hide("MilkButton"), Hide("CinnamonButton"),Hide("ChocolateButton"), Hide("PumpkinButton"),Hide("CoffeeButton"), Hide("EspressoButton"), Show("foamButton"), Show("espressoSHOTButton"), Show("whipButton"), Show("creamerButton"), Show("steamedMilk"), Show("Ingredients2"), Play("sound", "sfx_ui_click1.ogg")

screen Ingredients2():
    imagebutton:
        xalign 0.9125 yalign 0.039
        idle "Page2.PNG"

screen Prevbutton():
    imagebutton:
        xalign 0.7719 yalign 0.1846
        idle "Prev_Page_Idle.PNG"
        hover "Prev_Page_Highlight.PNG"
        action Notify("Previous"), SetVariable("pagenum", 1),Show("MilkButton"), Show("CinnamonButton"),Show("ChocolateButton"), Show("PumpkinButton"), Hide("foamButton"), Hide("espressoSHOTButton"), Hide("whipButton"), Hide("creamerButton") , Hide("steamedMilk"), Show("CoffeeButton"), Show("EspressoButton"), Hide("Ingredients2"), Play("sound", "sfx_ui_click1.ogg")

screen CoffeeButton():
    imagebutton:
        xalign 0.853 yalign 0.145
        idle "Coffee_Idle.PNG"
        hover "Coffee_Highlight.PNG"
        action Notify("coffee"), SetVariable("coffee", 1), SetVariable('Espresso', 0), Play("sound", "sfx_ui_click1.ogg")

screen EspressoButton():
    imagebutton:
        xalign 0.941 yalign 0.145
        idle "Espresso_Idle.PNG"
        hover "Espresso_Highlight.PNG"
        action Notify('Espresso'), SetVariable("Espresso", 1), SetVariable("coffee", 0), Play("sound", "sfx_ui_click1.ogg")

screen steamedMilk():
    imagebutton:
        xalign 0.853 yalign 0.145
        idle "SteamedMilk_Idle.PNG"
        hover "SteamedMilk_Highlight.PNG"
        action Notify("Steamed Milk"), SetVariable("steam", 1), Play("sound", "sfx_ui_click1.ogg")
screen MilkButton():
    imagebutton:
        xalign 0.853 yalign 0.2235
        idle "Milk_Idle.PNG"
        hover "Milk_Highlight.PNG"
        action Notify("Milk"), SetVariable("Milk", 1), Play("sound", "sfx_ui_click1.ogg")

screen CinnamonButton():
    imagebutton:
        xalign 0.941 yalign 0.2235
        idle "Cinnamon_Idle.PNG"
        hover "Cinnamon_Highlight.PNG"
        action Notify("Cinnamon"), SetVariable("Cinnamon", 1), Play("sound", "sfx_ui_click1.ogg")

screen ChocolateButton():
    imagebutton:
        xalign 0.853 yalign 0.3
        idle "Chocolate_Idle.PNG"
        hover "Chocolate_Highlight.PNG"
        action Notify("Chocolate"), SetVariable("Chocolate", 1), Play("sound", "sfx_ui_click1.ogg")

screen PumpkinButton():
    imagebutton:
        xalign 0.941 yalign 0.3
        idle "PumpkinSpice_Idle.PNG"
        hover "PumpkinSpice_Highlight.PNG"
        action Notify("Pumpkin"), SetVariable("Pumpkin", 1), Play("sound", "sfx_ui_click1.ogg")

screen foamButton():
    imagebutton:
        xalign 0.853 yalign 0.2235
        idle "Foam_Idle.PNG"
        hover "Foam_Highlight.PNG"
        action Notify("foam"), SetVariable("foam", 1), Play("sound", "sfx_ui_click1.ogg")

screen espressoSHOTButton():
    imagebutton:
        xalign 0.941 yalign 0.2235
        idle "EspressoShot_Idle.PNG"
        hover "EspressoShot_Highlight.PNG"
        action Notify("Extra Shot"), SetVariable("ExtraShot", 1), Play("sound", "sfx_ui_click1.ogg")

screen creamerButton():
    imagebutton:
        xalign 0.853 yalign 0.3
        idle "Creamer_Idle.PNG"
        hover "Creamer_Highlight.PNG"
        action Notify("Creamer"), SetVariable("creamer", 1), Play("sound", "sfx_ui_click1.ogg")

screen whipButton():
    imagebutton:
        xalign 0.941 yalign 0.145
        idle "WhippedCream_Idle.PNG"
        hover "WhippedCream_Highlight.PNG"
        action Notify("Whip"), SetVariable("whip_cream", 1), Play("sound", "sfx_ui_click1.ogg")

screen DrinkType():
    if Coffee == 1:
        imagebutton:
            xalign 0.84 yalign 0.59
            idle "DrinkEspresso.PNG"
    elif Espresso == 1:
        imagebutton:
            xalign 0.84 yalign 0.59
            idle "DrinkCoffee.PNG"

screen MenuList1():
    imagemap:
        ground "Menu_1.PNG"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1")
        hotspot (0, 86, 40, 166) action Show("MenuList2"), Hide("MenuList1"), Play("sound", "sfx_room_paper_rustle.ogg")
        hotspot (0, 167, 40, 247) action Show("MenuList3"), Hide("MenuList1")
        hotspot (0, 248, 40, 328) action Show("MenuList4"), Hide("MenuList1")
        hotspot (0, 329, 40, 410) action Show("MenuList5"), Hide("MenuList1")
        hotspot (705, 0, 740, 35) action Hide("MenuList1"), Play("sound", "sfx_ui_click1.ogg")

screen MenuList2():
    imagemap:
        ground "Menu_2.PNG"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1"),  Hide("MenuList2"), Play("sound", "sfx_room_paper_rustle.ogg")
        hotspot (0, 86, 40, 166) action Show("MenuList2")
        hotspot (0, 167, 40, 247) action Show("MenuList3"),  Hide("MenuList2")
        hotspot (0, 248, 40, 328) action Show("MenuList4"),  Hide("MenuList2")
        hotspot (0, 329, 40, 410) action Show("MenuList5"),  Hide("MenuList2")
        hotspot (705, 0, 740, 35) action Hide("MenuList2"), Play("sound", "sfx_ui_click1.ogg")

screen SaveButton():
    imagebutton:
        xalign 0.845 yalign 0.806
        idle "Save_Idle.PNG"
        hover "Save_Highlight.PNG"
        action Play("sound", "sfx_ui_click1.ogg"), ShowMenu('save')

screen BackButton():
    imagebutton:
        xalign 0.845 yalign 0.8863
        idle "Back_Idle.PNG"
        hover "Back_Highlight.PNG"
        action Play("sound", "sfx_ui_click1.ogg"), Rollback()

screen SkipButton():
    imagebutton:
        xalign 0.845 yalign 0.969
        idle "Skip_Idle.PNG"
        hover "Skip_Highlight.PNG"
        action Play("sound", "sfx_ui_click1.ogg"), Skip() alternate Skip(fast=True, confirm=True)

screen HistoryButton():
    imagebutton:
        xalign 0.965 yalign 0.8863
        idle "History_Idle.PNG"
        hover "History_Highlight.PNG"
        action Play("sound", "sfx_ui_click1.ogg"), ShowMenu('history')

screen PrefsButton():
    imagebutton:
        xalign 0.965 yalign 0.806
        idle "Preferences_Idle.PNG"
        hover "Preferences_Highlight.PNG"
        action Play("sound", "sfx_ui_click1.ogg"), ShowMenu('preferences')

screen AutoButton():
    imagebutton:
        xalign 0.965 yalign 0.969
        idle "Auto_Idle.PNG"
        hover "Auto_Highlight.PNG"
        action Preference("auto-forward", "toggle"), Play("sound", "sfx_ui_click1.ogg")
