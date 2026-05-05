import pygame as pg
import sys
pg.init()

class Scene:
    def __init__(self, width, height):
        self.scene = pg.display.set_mode((width, height))
        self.font = pg.font.SysFont('Roboto', 30)

    def hendler(self, event): 
        if event.type == pg.QUIT:
            return 'quit'
            # pg.quit() 
            # sys.exit()
        
    
    def update(self): pass

    def draw(self): pass

class MainMenu(Scene):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.btn_start = pg.Rect(width//2-50, height-300, 100, 50)
        self.btn_exit = pg.Rect(width-150, height-50, 100, 50)

        self.start_color = (255, 0, 0)
        self.exit_color = (0, 255, 0)

        self.name = 'MainMenu'
    
    @property
    def mouse(self):
        return pg.mouse.get_pos()

    def hendler(self, event):
        #self.mouse = pg.mouse.get_pos()
        super().hendler(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.btn_start.collidepoint(self.mouse):
                    return 'game'
                if self.btn_exit.collidepoint(self.mouse):
                    return 'quit'

    def update(self):
        #mouse = pg.mouse.get_pos()
        if self.btn_start.collidepoint(self.mouse):
            self.start_color = (200, 0, 0)
        else:
            self.start_color = (255, 0, 0)
        
        if self.btn_exit.collidepoint(self.mouse):
            self.exit_color = (0, 200, 0)
        else:
            self.exit_color = (0, 255, 0)

    def draw(self, scene):
        super().draw()
        scene.fill((0, 0, 0))
        pg.draw.rect(scene,self.exit_color, self.btn_exit)
        pg.draw.rect(scene, self.start_color, self.btn_start)
        scene.blit(self.font.render('Начать', True, (0, 0, 0)), (self.btn_start.x+20, self.btn_start.y+10))
        scene.blit(self.font.render('Выход', True, (0, 0, 0)), (self.btn_exit.x+10, self.btn_exit.y+10))
   

width = 800
height = 800

window  = pg.display.set_mode((width, height))
scene =  MainMenu(width, height)

pg.display.set_caption("Игровой проект, по мотивам HMM3")

run = True

current_scene = scene.name
while run:
    for event in pg.event.get():
        scene.hendler(event)
    scene.update()
    scene.draw(window)

    pg.display.flip()
pg.quit()  
