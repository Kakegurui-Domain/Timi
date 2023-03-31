
import pygame
from pyrogram*


# Initialize Pygame
pygame.init()

# Set up Pygame display
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set up player character
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# Set up enemy character
enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()

# Set up game state
player_hp = 100
enemy_hp = 100
is_battle = False

# Create a message handler for incoming messages
@ app.on_message(filters.text)
def handle_message(client, message):
    global player_hp, enemy_hp, is_battle

    # Handle user input
    if message.text == "/up":
        player_rect.move_ip(0, -10)
    elif message.text == "/down":
        player_rect.move_ip(0, 10)
    elif message.text == "/left":
        player_rect.move_ip(-10, 0)
    elif message.text == "/right":
        player_rect.move_ip(10, 0)
    elif message.text == "/attack":
        is_battle = True

    # Handle game state
    if is_battle:
        enemy_hp -= 10
        player_hp -= 5

    # Draw game objects to screen
    screen.fill((255, 255, 255))
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, player_hp, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(600, 10, enemy_hp, 10))
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            app.stop()
            quit()

    pygame.time.wait(10)
