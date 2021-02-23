from gui_files.svg import *

DICE_CAPTION = "I love Lavender!"


def draw_dice(num):

    width, height = 100, 100
    radius = 10
    graphic = create_graphic(width, height)

    draw_rect(graphic, 0, 0, 100, 100, fill="Lavender", stroke="DarkSlateBlue")
    write_text(graphic, 0, 0, num,
               stroke="BlueViolet", fill="Lavender")
    draw_circle(graphic, width/2, height/2, radius * num,
                stroke='SlateBlue', fill='GhostWhite')
    return graphic
