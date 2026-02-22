import pygame
import random
import sys


pygame.init()

WIDTH, HEIGHT = 960, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

FPS = 64
WHITE = (0, 0, 160)
RED = (200, 0, 0)
GREEN = (0, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

GRAVITY = 1
PLAYER_SPEED = 5
JUMP_FORCE = 15

image_path = r"C:\Users\kelvi\OneDrive\Área de Trabalho\IFC\Códigos ;-;\Códigos 2025-1\joguineos\IMAGENS JOGO 2"

background_image = pygame.image.load(f"{image_path}\\bg.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

menu_background = pygame.image.load(f"{image_path}\\menu_background.png").convert()
menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))

rank_icon = pygame.image.load(f"{image_path}\\rank_icon.png").convert_alpha()
rank_icon = pygame.transform.scale(rank_icon, (60, 60))

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False
        self.alive = True

    def update(self, platforms):
        if not self.alive:
            return
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED
        self.vel_y += GRAVITY
        dy = self.vel_y
        self.on_ground = False
        for platform in platforms:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.vel_y > 0:
                    dy = platform.rect.top - self.rect.bottom
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    dy = platform.rect.bottom - self.rect.top
                    self.vel_y = 0
        self.rect.x += dx
        self.rect.y += dy

    def jump(self):
        if self.on_ground and self.alive:
            self.vel_y = -JUMP_FORCE

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.direction * 2
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction *= -1

class Trophy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

def show_menu():
    menu_running = True
    while menu_running:
        WIN.blit(menu_background, (0, 0))
        title = font.render("Pressione ENTER para jogar", True, BLACK)
        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                menu_running = False

show_menu()

player = Player(100, 400)
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

floor = Platform(0, HEIGHT - 40, WIDTH, 40)
platforms.add(floor)
all_sprites.add(floor)

platform_layout = [
    (200, 450, 100, 20),
    (350, 400, 100, 20),
    (500, 350, 100, 20),
    (650, 300, 100, 20),
]

for plat in platform_layout:
    p = Platform(*plat)
    platforms.add(p)
    all_sprites.add(p)

for _ in range(3):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    e = Enemy(x, y)
    enemies.add(e)
    all_sprites.add(e)

trophy = Trophy(800, 260)
all_sprites.add(trophy)

all_sprites.add(player)

start_ticks = pygame.time.get_ticks()
game_over = False
victory = False

running = True
while running:
    dt = clock.tick(FPS)
    fps = clock.get_fps()
    frametime = dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    if not game_over and not victory:
        player.update(platforms)
        enemies.update()

        if pygame.sprite.spritecollide(player, enemies, False):
            player.alive = False
            game_over = True

        if pygame.sprite.collide_rect(player, trophy):
            victory = True

    WIN.blit(background_image, (0, 0))
    all_sprites.draw(WIN)

    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    timer_text = font.render(f"Time: {seconds}", True, BLACK)
    fps_text = font.render(f"FPS: {int(fps)}", True, BLACK)
    frametime_text = font.render(f"Frametime: {frametime:.2f} ms", True, BLACK)

    WIN.blit(timer_text, (10, 10))
    WIN.blit(fps_text, (10, 40))
    WIN.blit(frametime_text, (10, 70))

    rank_text = font.render("rank: lixo 3", True, BLACK)
    WIN.blit(rank_text, (WIDTH - 170, 10))
    WIN.blit(rank_icon, (WIDTH - 80, 45))

    if game_over:
        game_over_text = font.render("Game Over", True, RED)
        WIN.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))

    if victory:
        victory_text = font.render("vitoria royalekkk", True, (255, 215, 0))
        WIN.blit(victory_text, (WIDTH // 2 - 120, HEIGHT // 2))

    pygame.display.update()

pygame.quit()
sys.exit()
