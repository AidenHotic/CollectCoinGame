import pygame
import sys

#Initialize Pygame
pygame.init()

#create the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

#Color Values
WHITE = (255, 255, 255)
RED = (255, 0 , 0)

# Ball properties  (speed, size)
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # <-- spawns the ball in the middle of the screen
ball_speed_x, ball_speed_y = 5, 5

#clock to control FPS/Frames Per Second
clock = pygame.time.Clock()

#main game loop / While loop
running = True
while running:

    #Loop through every event/player cmd and find if they try to "Quit"
    #if player tries to "Quit" end the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Update the balls position 
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    #Bounce Ball Off Edges
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:  # If the balls possitions x value is higher then the width fo the screen
        ball_speed_x = -ball_speed_x                              # Reverse the speed of the ball on the x axis

    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT: # If the balls possitions x value is higher then the width fo the screen
        ball_speed_y = -ball_speed_y                              # Reverse the speed of the ball on the x axis

    # Clear Screen
    screen.fill(WHITE)

    # Create the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update The Display
    pygame.display.flip()

    # Control Frame Rate / Tick The clock
    clock.tick(60)

#Quit pygame / When the loop ends because the player "Quits" close the tab
pygame.quit()
sys.exit()