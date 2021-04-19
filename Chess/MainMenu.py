import pygame as p
from Chess import ChessMain

WIDTH = HEIGHT = 512
LOGO = p.image.load("images/ChessME!.png")
LOGO_X = 5
LOGO_Y = 0


class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            p.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        p.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = p.font.SysFont("comicsans", 60)
            text = font.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 -
                                                                                       text.get_height()/2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def draw_menu(screen, start_button, quit_button):
    screen.fill(p.Color("white"))
    screen.blit(LOGO, (LOGO_X, LOGO_Y))
    start_button.draw(screen, (0, 0, 0))
    quit_button.draw(screen, (0, 0, 0))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    start_button = Button((255, 255, 255), 130, 275, 250, 50, "Start Game")
    quit_button = Button((255, 255, 255), 130, 340, 250, 50, "Quit")
    running = True
    while running:
        for e in p.event.get():
            pos = p.mouse.get_pos()

            if e.type == p.QUIT:
                running = False

            if e.type == p.MOUSEBUTTONDOWN:
                if start_button.is_over(pos):
                    try:
                        ChessMain.main()
                    except:
                        ChessMain.main()
                if quit_button.is_over(pos):
                    running = False

        draw_menu(screen, start_button, quit_button)
        p.display.update()


if __name__ == "__main__":
    main()