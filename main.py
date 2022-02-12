"""

Game Name: IDK?

Made By: Penguin Person AKA Lars

TODO:
    Make main menu
    Make F5 show debug menu
    Add gameplay
"""

import pygame, socket, threading
pygame.init()

WIDTH = 1000
HEIGHT = 700

class Window:
    def __init__(self, window):
        self.window = window
        self.window.fill((255,255,255))
        self.gameOpen = True
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.main_menu()
    def main_menu(self):
        pygame.display.set_caption("??? | Main Menu")

        self.backgroundImg = pygame.image.load("sprites/main_menu_background.png")
        
        while self.gameOpen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOpen = False
            self.clock.tick(self.FPS)
            self.draw_img(self.backgroundImg, 0, 0, WIDTH, HEIGHT)
            self.draw_text("Title???", "fonts/font1.ttf", (0,0,0), (255,255,255), 35, 450, 340)
            self.draw_text("Press \"O\" To Play!", "fonts/font1.ttf", (0,0,0), (255,255,255), 35, 350, 390)
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_o]:
                self.game(True)
    def game(self, singleplayer):
        if singleplayer == True:
            pygame.display.set_caption("??? | Game")

            self.playerImage = pygame.image.load("sprites/player_middle.png")

            self.player_x = 100
            self.player_y = 100
            self.username = "Player"

            self.currentSlot = 1
            self.hotbarImage = pygame.image.load("sprites/hotbar.png")
            self.inventory = {"wood": 0, "stick": 1, "stone": 0, "bronze": 0, "iron": 1, "wood_axe": 1, "stone_axe": 0, "bronze_axe": 0, "iron_axe": 0, "wood_pickaxe": 1, "stone_pickaxe": 0, "bronze_pickaxe": 0, "iron_pickaxe": 0,}
            self.woodImage = pygame.image.load("sprites/wood.png")
            self.stickImage = pygame.image.load("sprites/stick.png")
            self.stoneImage = pygame.image.load("sprites/stone.png")
            self.bronzeImage = pygame.image.load("sprites/bronze.png")
            self.ironImage = pygame.image.load("sprites/iron.png")
            self.wood_axeImage = pygame.image.load("sprites/wood_axe.png")
            self.wood_pickaxeImage = pygame.image.load("sprites/wood_pickaxe.png")
            self.hotbar_arrowImage = pygame.image.load("sprites/hotbar_arrow.png")
            self.hotbarSlots = []
            
            while self.gameOpen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameOpen = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        if self.currentSlot != 4:
                            self.currentSlot += 1
                        else:
                            self.currentSlot = 1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        if self.currentSlot != 1:
                            self.currentSlot -= 1
                        else:
                            self.currentSlot = 4
                self.window.fill((255,255,255))
                self.clock.tick(self.FPS)
                self.player(self.player_x, self.player_y, self.username)
                pygame.display.update()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.player_y -= -2
                    self.playerImage = pygame.image.load("sprites/player_middle.png")
                if keys[pygame.K_w]:
                    self.player_y -= 2
                    self.playerImage = pygame.image.load("sprites/player_up.png")
                if keys[pygame.K_d]:
                    self.player_x -= -2
                    self.playerImage = pygame.image.load("sprites/player_right.png")
                if keys[pygame.K_a]:
                    self.player_x -= 2
                    self.playerImage = pygame.image.load("sprites/player_left.png")
    def draw_img(self, image, x, y, size_width=None, size_hight=None):
        if size_width:
            if size_hight:
                image = pygame.transform.scale(image, (size_width, size_hight))
        self.window.blit(image, (x, y))
    def draw_text(self, text="", fontFile="", foreGround=(), backGround=(), fontSize=10, x=0, y=0):
        font = pygame.font.Font(fontFile, fontSize)
        text = font.render(text, False, foreGround, backGround)
        textRect = text.get_rect()
        textRect.center = (WIDTH//2, HEIGHT//2)
        self.window.blit(text, (x, y))
    def player(self, x, y, username):
        self.draw_img(self.playerImage, x, y, 100, 200)
        self.draw_text(username, "fonts/font1.ttf", (0,0,0), (255,255,255), 20, x+10, y-20)
        self.draw_img(self.hotbarImage, (WIDTH/2)-90, HEIGHT-100, 400, 100)
        e = 0
        if self.currentSlot == 1:
            self.draw_img(self.hotbar_arrowImage, (WIDTH/2)-75, HEIGHT-165, 64, 64)
        if self.currentSlot == 2:
            self.draw_img(self.hotbar_arrowImage, (WIDTH/2)+30, HEIGHT-165, 64, 64)
        if self.currentSlot == 3:
            self.draw_img(self.hotbar_arrowImage, (WIDTH/2)+120, HEIGHT-165, 64, 64)
        if self.currentSlot == 4:
            self.draw_img(self.hotbar_arrowImage, (WIDTH/2)+230, HEIGHT-165, 64, 64)
        for i in self.inventory:
            if self.inventory[i] >= 1:
                if i in self.hotbarSlots:
                    pass
                else:
                    self.hotbarSlots += (i,)
        for i in self.hotbarSlots:
            e += (self.hotbarSlots.index(i) + 100)
            if i == "wood":
                self.draw_img(self.woodImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.woodImage, x+80, y+110, 32, 32)

            if i == "stick":
                self.draw_img(self.stickImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.stickImage, x+80, y+110, 32, 32)

            if i == "stone":
                self.draw_img(self.stoneImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.stoneImage, x+80, y+110, 32, 32)

            if i == "bronze":
                self.draw_img(self.bronzeImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.bronzeImage, x+80, y+110, 32, 32)

            if i == "iron":
                self.draw_img(self.ironImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.ironImage, x+80, y+110, 32, 32)

            if i == "wood_axe":
                self.draw_img(self.wood_axeImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.wood_axeImage, x+85, y+115, 32, 32)

            if i == "wood_pickaxe":
                self.draw_img(self.wood_pickaxeImage, (WIDTH/2)-(175-e), HEIGHT-85, 64, 64)
                if self.hotbarSlots[self.currentSlot-1] == i:self.draw_img(self.wood_pickaxeImage, x+85, y+115, 32, 32)

    def new__player(self, x, y):
        while True:
            self.player(x, y)
if __name__ == "__main__":
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    mainClass = Window(win)