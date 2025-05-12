from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

FPS = 60
clock = time.Clock()
win_width = 700
win_height = 500

ball = GameSprite("ping_pong_files/tenis_ball.png", 200, 200, 3, 50, 50)
pad = Player("ping_pong_files/racket.png", 30, 200, 3, 50, 150)
pad_two = Player("ping_pong_files/racket.png", 520, 200, 3, 50, 150)

window = display.set_mode((win_width, win_height))
display.set_caption("pingpong game")

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((136, 206, 235))
    pad.update()
    pad_two.update()
    ball.reset()
    pad.reset()
    pad_two.reset()
    display.update()
    clock.tick(FPS)



