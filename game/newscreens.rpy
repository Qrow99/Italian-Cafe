screen MenuButton():
    imagebutton:
        xalign 0.97 yalign 0.68
        idle "menuidle.PNG"
        hover "menuhover.PNG"
        action Show("MenuList1")

screen ResetButton():
    imagebutton:
        xalign 0.97 yalign 0.449
        idle "resetidle.PNG"
        hover "resethover.PNG"
        action SetVariable("step", 1), SetVariable("drinksizes", 0), SetVariable("drinktypes", 0)

screen ConfirmButton():
    imagebutton:
        xalign 0.97 yalign 0.57
        idle "confirmidle.PNG"
        hover "confirmhover.PNG"
        action Notify("ORDER UP")

screen NextButton():
    if readyfornext >= 1:
        imagebutton:
            xalign 0.9882 yalign 0.1846
            idle "NextStepIdle.PNG"
            hover "NextStepHover.PNG"
            action SetVariable("step", 2), SetVariable("readyfornext", 0)
    else:
        imagebutton:
            xalign 0.9882 yalign 0.1846
            idle "NextStepIdle.PNG"

screen Button11():
    if step >= 2:
        imagebutton:
            xalign 0.853 yalign 0.145
            idle "coffeeidle.PNG"
            hover "coffeehover.PNG"
            action SetVariable("drinktypes", 1), Show("DrinkType")
    elif step >= 1:
        imagebutton:
            xalign 0.853 yalign 0.145
            idle "smallidle.PNG"
            hover "smallhover.PNG"
            action SetVariable("drinksizes", 1), Show("DrinkSize"), SetVariable("readyfornext", 1)

screen Button12():
    if step >= 2:
        imagebutton:
            xalign 0.941 yalign 0.145
            idle "teaidle.PNG"
            hover "teahover.PNG"
            action SetVariable("drinktypes", 2), Show("DrinkType")
    elif step >= 1:
        imagebutton:
            xalign 0.941 yalign 0.145
            idle "largeidle.PNG"
            hover "largehover.PNG"
            action SetVariable("drinksizes", 2), Show("DrinkSize"), SetVariable("readyfornext", 1)

screen DrinkSize():
    if drinksizes >= 2:
        imagebutton:
            xalign 0.84 yalign 0.59
            idle "CupLarge.PNG"
    elif drinksizes >= 1:
        imagebutton:
            xalign 0.84 yalign 0.59
            idle "CupSmall.PNG"

screen DrinkType():
    if drinktypes >= 2:
        if drinksizes >= 2:
            imagebutton:
                xalign 0.84 yalign 0.56
                idle "DrinkTea.PNG"
        else:
            imagebutton:
                xalign 0.84 yalign 0.59
                idle "DrinkTea.PNG"
    elif drinktypes >= 1:
        if drinksizes >= 2:
            imagebutton:
                xalign 0.84 yalign 0.56
                idle "DrinkCoffee.PNG"
        else:
            imagebutton:
                xalign 0.84 yalign 0.59
                idle "DrinkCoffee.PNG"




screen MenuList1():
    imagemap:
        ground "Menu1.png"
        xalign 0.18 yalign 0.2
        hotspot (0, 0, 40, 85) action Show("MenuList1")
        hotspot (0, 86, 40, 166) action Show("MenuList2"), Hide("MenuList1")
        hotspot (0, 167, 40, 247) action Show("MenuList3"), Hide("MenuList1")
        hotspot (0, 248, 40, 328) action Show("MenuList4"), Hide("MenuList1")
        hotspot (0, 329, 40, 410) action Show("MenuList5"), Hide("MenuList1")
        hotspot (705, 0, 740, 35) action Hide("MenuList1")

screen MenuList2():
    imagemap:
        ground "Menu2.png"
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
