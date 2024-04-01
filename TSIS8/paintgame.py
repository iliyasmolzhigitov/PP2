import pygame, sys

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class ColorMode:
    RED = "red"
    BLACK = "black"
    WHITE = "white"
    GREEN = "green"
    BLUE = "blue"

class Mode:
    BRUSH = "draw"
    ERASER = "eraser"
    RECT = "rectangle"
    CIRCLE = "oval"

class Point:
    def __init__(self, x, y, radius, color, mode):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mode = mode

class Brush:
    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.mode = Mode.BRUSH
        self.icon = "brush"
        self.image = pygame.transform.scale(pygame.image.load('paint.smth/brush.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos
        self.width = 15
        self.color_mode = ColorMode.RED
        self.points = []

    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.image = pygame.transform.scale(pygame.image.load(f'paint.smth/{self.icon}.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos

    def add_points(self):
        if self.mode == Mode.BRUSH:
            p = Point(x=self.pos[0], y=self.pos[1], radius=self.width, color=self.color_mode, mode=Mode.BRUSH)
            self.points.append(p)

        if self.mode == Mode.ERASER:
            p = Point(x=self.pos[0], y=self.pos[1], radius=self.width, color=ColorMode.WHITE, mode=Mode.ERASER)
            self.points.append(p)

    def add_points_fig(self):
        if self.mode == Mode.RECT or self.mode == Mode.CIRCLE:
            p = Point(x=self.pos[0], y=self.pos[1], radius=self.width, color=self.color_mode, mode=self.mode)
            self.points.append(p)

    def draw_line_between(self, surf, start, end):
        if (start.mode == Mode.BRUSH and end.mode == Mode.BRUSH) or (
                start.mode == Mode.ERASER and end.mode == Mode.ERASER):
            dx = start.x - end.x
            dy = start.y - end.y
            iterations = max(abs(dx), abs(dy))

            for i in range(iterations):
                progress = 1.0 * i / iterations
                aprogress = 1 - progress
                x = int(aprogress * start.x + progress * end.x)
                y = int(aprogress * start.y + progress * end.y)
                if start.mode == Mode.BRUSH or start.mode == Mode.ERASER:
                    pygame.draw.circle(surf, start.color, (x, y), start.radius)

    def draw_points(self, surf):
        i = 0
        while i < len(self.points) - 1:
            if self.points[i].mode == Mode.BRUSH or self.points[i].mode == Mode.ERASER:
                self.draw_line_between(surf, self.points[i], self.points[i + 1])
            if self.points[i + 1].mode == Mode.RECT:
                rect = pygame.Rect(self.points[i + 1].x, self.points[i + 1].y, 150, 130)
                pygame.draw.rect(surf, self.points[i + 1].color, rect, 1)
            if self.points[i + 1].mode == Mode.CIRCLE:
                pygame.draw.circle(surf, self.points[i + 1].color, (self.points[i + 1].x, self.points[i + 1].y), 40)
            i += 1

    def erase_all(self):
        self.points = []

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Paint")
    fps = pygame.time.Clock()
    brush = Brush()
    pygame.mouse.set_visible(False)

    while True:
        fps.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    brush.mode = Mode.BRUSH
                    brush.icon = 'brush'
                    brush.color_mode = ColorMode.RED

                if event.key == pygame.K_2:
                    brush.mode = Mode.ERASER
                    brush.icon = 'eraser'

                if event.key == pygame.K_3:
                    brush.mode = Mode.RECT
                    brush.icon = 'rectangle'
                    brush.color_mode = ColorMode.RED
                    break

                if event.key == pygame.K_4:
                    brush.mode = Mode.CIRCLE
                    brush.icon = 'circle'
                    brush.color_mode = ColorMode.RED
                    break

                if event.key == pygame.K_d:
                    brush.width += 5

                if event.key == pygame.K_s:
                    brush.width -= 5

            if event.type == pygame.MOUSEBUTTONDOWN and (brush.mode == Mode.RECT or brush.mode == Mode.CIRCLE):
                if brush.color_mode == ColorMode.WHITE:
                    brush.color_mode = ColorMode.RED
                brush.add_points_fig()

            if event.type == pygame.MOUSEMOTION:
                brush.update()
                if brush.mode == Mode.BRUSH or brush.mode == Mode.ERASER:
                    brush.add_points()

        screen.fill((255, 255, 255))
        brush.draw_points(screen)
        screen.blit(brush.image, brush.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
