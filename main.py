import pygame
import random
import math
# Initialize pygame
pygame.init()

# Displaying pygame on the screen
screen = pygame.display.set_mode((800, 600))

# Icon
glowingBall = pygame.image.load("icons8-tank-50.png")
pygame.display.set_icon(glowingBall)

# Title
pygame.display.set_caption("Arik's Hockey lab")

# Background image
background = pygame.image.load("naruto-2020-art.jpg")

# Player 1
player1_img = pygame.image.load("O.png")
player1_x = 75
player1_y = 150
player1_speed = 5  # Adjust this value as needed

# Player 2
player2_img = pygame.image.load("S - Copy.png")
player2_x = 480
player2_y = 150
player2_speed = 5  # Adjust this value as needed

# Create a clock object to control frame rate
Clock = pygame.time.Clock()


# Function to draw a player
def draw_player(x, y, img):
    screen.blit(img, (x, y))


# Bulletimg
bulletimg = pygame.image.load('A-removebg-preview.png')
bulletX = 75
bulletY = 150
bulletX_change = 15
bulletY_change = 5
bullet_status = "ready"

#score
score_value = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)
textX = 600
textY = 100


def fire_bullet(x, y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bulletimg, (x, y - 10))

def iscollision(player2_X, player2_Y, bulletX, bulletY):
    dX = (math.pow((player2_X - bulletX), 2))
    dY = (math.pow((player2_Y - bulletY), 2))
    distance = math.sqrt(dX + dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance < 32:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(score, (x, y))

def game_over():
    go = font.render("GAME OVER", True, (255,255,255))
    screen.blit(go, (290, 300))


# Load background music
pygame.mixer.music.load("[8-Bit] Itachi's Theme (Senya).mp3")  # Replace with your music file
pygame.mixer.music.set_volume(0.25)  # Set the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 means loop indefinitely


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for collision between bullet and player2
    collision = iscollision(player2_x, player2_y, bulletX, bulletY)
    if collision:
        bullet_status = "ready"  # Reset the bullet
        score_value += 1  # Increase the score

    # Display the score
    show_score(textX, textY)


    # Handle player 1 movement (arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1_x -= player1_speed
    if keys[pygame.K_RIGHT]:
        player1_x += player1_speed
    if keys[pygame.K_UP]:
        player1_y -= player1_speed
    if keys[pygame.K_DOWN]:
        player1_y += player1_speed

    # Boundary checking for player 1
    player1_x = max(0, min(player1_x, 323 - 70))
    player1_y = max(0, min(player1_y, 600 - 76))



    # Handle player 2 movement (WASD keys)
    if keys[pygame.K_a]:
        player2_x -= player2_speed
    if keys[pygame.K_d]:
        player2_x += player2_speed
    if keys[pygame.K_w]:
        player2_y -= player2_speed
    if keys[pygame.K_s]:
        player2_y += player2_speed

    # Bullet loop
    if keys[pygame.K_SPACE]:
        if bullet_status == "ready":
            bulletX = player1_x + 30  # Adjusted the starting position of the bullet
            bulletY = player1_y
            fire_bullet(bulletX, bulletY)

    # Move the bullet
    if bullet_status == "fire":
        bulletX += bulletX_change
        fire_bullet(bulletX, bulletY)

        # Reset bullet when it goes off the screen
        if bulletX >= 800:
            bullet_status = "ready"

    # Boundary checking for player 2
    player2_x = max(323, min(player2_x, 800 - 78))
    player2_y = max(0, min(player2_y, 600 - 76))

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw players
    draw_player(player1_x, player1_y, player1_img)
    draw_player(player2_x, player2_y, player2_img)

    # Draw bullet only when it's fired
    if bullet_status == "fire":
        fire_bullet(bulletX, bulletY)

    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)

pygame.quit()
