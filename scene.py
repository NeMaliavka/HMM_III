import pygame as pg
pg.init()
 
width = 800
height = 800

scene  = pg.display.set_mode((width, height))
pg.display.set_caption("Игровой проект, по мотивам HMM3")

font = pg.font.SysFont('Roboto', 30)
btn_start = pg.Rect(width//2-50, height-300, 100, 50)
btn_exit = pg.Rect(width-150, height-50, 100, 50)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.draw.rect(scene,(255, 255, 0), btn_start)

    pg.draw.rect(scene,(255, 0, 0), btn_exit)
    scene.blit(font.render('Начать', True, (0, 0, 0)), (btn_start.x+20, btn_start.y+10))
    scene.blit(font.render('Выход', True, (0, 0, 0)), (btn_exit.x+10, btn_exit.y+10))


    pg.display.flip()
pg.quit()    