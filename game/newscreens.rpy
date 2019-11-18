screen MenuButton():
    imagebutton:
        xalign 0.97 yalign 0.68
        idle "Menu_Idle.PNG"
        hover "Menu_Highlight.PNG"
        action Show("MenuList1")

screen ResetButton():
    imagebutton:
        xalign 0.97 yalign 0.449
        idle "Reset_Idle.PNG"
        hover "Reset_Highlight.PNG"
        action Notify("reset order"), SetVariable("coffee", 0), SetVariable('Espresso', 0), SetVariable("Milk", 0), SetVariable("Cinnamon", 0), SetVariable("Chocolate", 0), SetVariable("Pumpkin", 0)

screen ConfirmButton():
    imagebutton:
        xalign 0.97 yalign 0.57
        idle "Submit_Idle.PNG"
        hover "Submit_Highlight.PNG"
        action Notify("ORDER UP"), SetVariable("makingdrink", 1)

screen NextButton():
    imagebutton:
        xalign 0.9882 yalign 0.1846
        idle "Next_Page_Idle.PNG"
        hover "Next_Page_Highlight.PNG"

screen Backbutton():
    imagebutton:
        xalign 0.7719 yalign 0.1846
        idle "Next_Page_Idle.PNG"
        hover "Next_Page_Highlight.PNG"

screen CoffeeButton():
    imagebutton:
        xalign 0.853 yalign 0.145
        idle "Coffee_Idle.PNG"
        hover "Coffee_Highlight.PNG"
        action Notify("coffee"), SetVariable("coffee", 1), SetVariable('Espresso', 0)

screen EspressoButton():
    imagebutton:
        xalign 0.941 yalign 0.145
        idle "Espresso_Idle.PNG"
        hover "Espresso_Highlight.PNG"
        action Notify('Espresso'), SetVariable("Espresso", 1), SetVariable("coffee", 0)

screen MilkButton():
    imagebutton:
        xalign 0.853 yalign 0.2205
        idle "Milk_Idle.PNG"
        hover "Milk_Highlight.PNG"
        action Notify("Milk"), SetVariable("Milk", 1)

screen CinnamonButton():
    imagebutton:
        xalign 0.941 yalign 0.2235
        idle "Cinnamon_Idle.PNG"
        hover "Cinnamon_Highlight.PNG"
        action Notify("Cinnamon"), SetVariable("Cinnamon", 1)

screen ChocolateButton():
    imagebutton:
        xalign 0.853 yalign 0.3
        idle "Chocolate_Idle.PNG"
        hover "Chocolate_Highlight.PNG"
        action Notify("Chocolate"), SetVariable("Chocolate", 1)

screen PumpkinButton():
    imagebutton:
        xalign 0.941 yalign 0.3
        idle "PumpkinSpice_Idle.PNG"
        hover "PumpkinSpice_Highlight.PNG"
        action Notify("Pumpkin"), SetVariable("Pumpkin", 1)

#screen foamButton():

#screen espressoButton():

#screen creamerButton():

#screen whipButton():

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
        hotspot (0, 86, 40, 166) action Show("MenuList2"), Hide("MenuList1")
        hotspot (0, 167, 40, 247) action Show("MenuList3"), Hide("MenuList1")
        hotspot (0, 248, 40, 328) action Show("MenuList4"), Hide("MenuList1")
        hotspot (0, 329, 40, 410) action Show("MenuList5"), Hide("MenuList1")
        hotspot (705, 0, 740, 35) action Hide("MenuList1")

screen MenuList2():
    imagemap:
        ground "Menu_2.PNG"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1"),  Hide("MenuList2")
        hotspot (0, 86, 40, 166) action Show("MenuList2")
        hotspot (0, 167, 40, 247) action Show("MenuList3"),  Hide("MenuList2")
        hotspot (0, 248, 40, 328) action Show("MenuList4"),  Hide("MenuList2")
        hotspot (0, 329, 40, 410) action Show("MenuList5"),  Hide("MenuList2")
        hotspot (705, 0, 740, 35) action Hide("MenuList2")

screen MenuList3():
    imagemap:
        ground "Menu3.png"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1"),  Hide("MenuList3")
        hotspot (0, 86, 40, 166) action Show("MenuList2"),  Hide("MenuList3")
        hotspot (0, 167, 40, 247) action Show("MenuList3")
        hotspot (0, 248, 40, 328) action Show("MenuList4"),  Hide("MenuList3")
        hotspot (0, 329, 40, 410) action Show("MenuList5"),  Hide("MenuList3")
        hotspot (705, 0, 740, 35) action Hide("MenuList3")

screen MenuList4():
    imagemap:
        ground "Menu4.png"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1"),  Hide("MenuList4")
        hotspot (0, 86, 40, 166) action Show("MenuList2"),  Hide("MenuList4")
        hotspot (0, 167, 40, 247) action Show("MenuList3"),  Hide("MenuList4")
        hotspot (0, 248, 40, 328) action Show("MenuList4")
        hotspot (0, 329, 40, 410) action Show("MenuList5"),  Hide("MenuList4")
        hotspot (705, 0, 740, 35) action Hide("MenuList4")

screen MenuList5():
    imagemap:
        ground "Menu5.png"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1"),  Hide("MenuList5")
        hotspot (0, 86, 40, 166) action Show("MenuList2"),  Hide("MenuList5")
        hotspot (0, 167, 40, 247) action Show("MenuList3"),  Hide("MenuList5")
        hotspot (0, 248, 40, 328) action Show("MenuList4"),  Hide("MenuList5")
        hotspot (0, 329, 40, 410) action Show("MenuList5")
        hotspot (705, 0, 740, 35) action Hide("MenuList5")
