from timi import bot
import pygame
from pyrogram import filters
from time import time


# Initialize Pygame
pygame.init()

# Set up Pygame display
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set up player character
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_speed = 5

# Set up enemy character
enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_speed = 3

# Set up game state
player_hp = 100
player_score = 0
enemies = []
last_spawn_time = 0

# Create a message handler for incoming messages
@bot.on_message(filters.text)
def handle_message(client, message):
    global player_hp, player_score, player_speed

    # Handle user input
    if message.text == "/up":
        player_rect.move_ip(0, -player_speed)
    elif message.text == "/down":
        player_rect.move_ip(0, player_speed)
    elif message.text == "/left":
        player_rect.move_ip(-player_speed, 0)
    elif message.text == "/right":
        player_rect.move_ip(player_speed, 0)
    elif message.text == "/speed_up":
        player_speed += 1
    elif message.text == "/speed_down":
        player_speed -= 1

    # Draw game objects to screen
    screen.fill((255, 255, 255))
    screen.blit(player_image, player_rect)

    # Spawn enemies at a regular interval
    global last_spawn_time, enemies
    if time() - last_spawn_time > 2:
        last_spawn_time = time()
        enemy_rect_copy = enemy_rect.copy()
        enemy_rect_copy.x = 800
        enemy_rect_copy.y = pygame.time.get_ticks() % 600
        enemies.append(enemy_rect_copy)

    # Move and draw enemies
    for enemy_rect_copy in enemies:
        enemy_rect_copy.move_ip(-enemy_speed, 0)
        screen.blit(enemy_image, enemy_rect_copy)

        # Check for collision with player
        if player_rect.colliderect(enemy_rect_copy):
            player_hp -= 10

        # Check for off-screen enemies
        if enemy_rect_copy.x < -50:
            enemies.remove(enemy_rect_copy)
            player_score += 1

    # Draw player HP and score
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, player_hp, 10))
    score_text = pygame.font.SysFont(None, 24).render("Score: {}".format(player_score), True, (0, 0, 0))
    screen.blit(score_text, (10, 30))

    pygame.display.flip()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.time.wait(10)

