import pygame
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
player1_health = 100

# Player 2
player2_img = pygame.image.load("S - Copy.png")
player2_x = 480
player2_y = 150
player2_speed = 5  # Adjust this value as needed
player2_health = 100

# Bulletimg 1
bulletimg = pygame.image.load('A-removebg-preview.png')
bulletX = 75
bulletY = 150
bulletX_change = 15
bulletY_change = 5
bullet_status = "ready"

# Bulletimg for player 2
bulletimg_player2 = pygame.image.load('1.png')
bulletX_player2 = 480
bulletY_player2 = 150
bulletX_change_player2 = -15  # Adjust this value as needed
bulletY_change_player2 = 0
bullet_status_player2 = "ready"


# Health bar configuration
health_bar_length = 100
health_bar_height = 10
health_bar_color = (255, 0, 0)  # Green color
health_bar_color2 = (255,255,255)

# Function to draw a health bar
def draw_health_bar(x, y, health):
    pygame.draw.rect(screen, health_bar_color, (x, y, health, health_bar_height))

def draw_health_bar2(x, y, health):
    pygame.draw.rect(screen, health_bar_color2,(x,y,health,health_bar_height))
# Function to draw a player
def draw_player(x, y, img):
    screen.blit(img, (x, y))

#score
score_value = 0
score_value2 = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)
textX = 700
textY = 10
textX1 = 10
textX2 = 10
def fire_bullet(x, y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bulletimg, (x, y - 10))

def fire_bullet2(x,y):
    global bullet_status_player2
    bullet_status_player2 =  "fire"
    screen.blit(bulletimg_player2,(x,y-10))

def iscollision(player2_X, player2_Y, bulletX, bulletY):
    dX = (math.pow((player2_X - bulletX), 2))
    dY = (math.pow((player2_Y+20 - bulletY), 2)) #+20 is added to resize the collision in Y axis
    distance = math.sqrt(dX + dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance < 32:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def show_score2(x,y):
    score2 = font.render("Score: " +str(score_value2),True,(255,255,255))
    screen.blit(score2,(x,y))
def game_over():
    go = font.render("GAME OVER", True, (255,255,255))
    screen.blit(go, (290, 300))

def game_won():
    won_text = font.render("Player 1 Wins!", True, (255, 255, 255))
    screen.blit(won_text, (350, 300))
    pygame.display.update()
    pygame.time.delay(10000)  # Display the message for 2 seconds (adjust as needed)

def game_won2():
    won_text = font.render("Player 2 Wins!", True, (255, 255, 255))
    screen.blit(won_text, (350, 300))
    pygame.display.update()
    pygame.time.delay(10000)  # Display the message for 2 seconds (adjust as needed)


# Load background music
# pygame.mixer.music.load("[8-Bit] Itachi's Theme (Senya).mp3")  # Replace with your music file
# pygame.mixer.music.set_volume(0.25)  # Set the volume (0.0 to 1.0)
# pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Create a clock object to control frame rate
Clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    player1_x = max(0, min(player1_x, 423 - 70))
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

    # Boundary checking for player 1
    player2_x = max(400, min(player2_x, 800 - 70))
    player2_y = max(0, min(player2_y, 600 - 76))


    # Bullet loop 1 (player 1)
    if keys[pygame.K_LSHIFT]:
        if bullet_status == "ready":
            bulletX = player1_x + 30  # Adjusted the starting position of the bullet
            bulletY = player1_y
            fire_bullet(bulletX, bulletY)

    # Bullet loop 2 (player 2)
    if keys[pygame.K_RSHIFT]:
        if bullet_status_player2 == "ready":
            bulletX_player2 = player2_x - 30  # Adjusted the starting position of the bullet
            bulletY_player2 = player2_y
            fire_bullet2(bulletX_player2, bulletY_player2)

    # Move the bullet for player 1
    if bullet_status == "fire":
        bulletX += bulletX_change
        fire_bullet(bulletX, bulletY)

        # Reset bullet when it goes off the screen for player 1
        if bulletX >= 800:
            bullet_status = "ready"

    # Move the bullet for player 2
    if bullet_status_player2 == "fire":
        bulletX_player2 += bulletX_change_player2
        fire_bullet2(bulletX_player2, bulletY_player2)

        # Reset bullet when it goes off the screen for player 2
        if bulletX_player2 <= 0:
            bullet_status_player2 = "ready"

    # Check for collision between bullet and player2
    collision = iscollision(player2_x, player2_y, bulletX, bulletY)
    if collision:
        bulletX = 75
        bullet_status = "ready"  # Reset the bullet for player 1
        score_value2 += 1  # Increase the score
        player2_health -= 1  # Decrease health when hit

    # Check for collision between bullet_player2 and player 1
    collision_player2 = iscollision(player1_x, player1_y, bulletX_player2, bulletY_player2)
    if collision_player2:
        bulletX_player2 = 480
        bullet_status_player2 = "ready"  # Reset the bullet for player 2
        score_value += 1  # Increase the score
        player1_health -= 1  # Decrease health when hit

    if score_value2 == 10:
        game_won()
        running= False
    if score_value == 10:
        game_won2()
        running = False

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw players
    draw_player(player1_x, player1_y, player1_img)
    draw_player(player2_x, player2_y, player2_img)

    draw_health_bar(player1_x,player1_y-20,player1_health)
    draw_health_bar2(player2_x,player2_y-20,player2_health)

    # Draw bullets only when they're fired
    if bullet_status == "fire":
        fire_bullet(bulletX, bulletY)

    if bullet_status_player2 == "fire":
        fire_bullet2(bulletX_player2, bulletY_player2)

    show_score(textX,textY)
    show_score2(textX1,textX2)
    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)

pygame.quit()
