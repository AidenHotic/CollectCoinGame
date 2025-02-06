import pygame
import random
import time

#Initalize pygame
pygame.init()
#math.init()

#Create Screen/tab
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect The Coins")

db3 = True
db2 = True
db = True
rand = random.randint(1, 10)
score = 0
randNum_x = 0
randNum_y = 0 

#set enemies proporties
enemyCubeSpeed = 5
enemyCubeSize = 55

enemyCube1_x = WIDTH//2
enemyCube1_y = HEIGHT - 55
enemyCube1_color = (50, 50 ,50)
enemyCube1_active = False

enemyCube2_x = WIDTH//4
enemyCube2_y = HEIGHT - 55
enemyCube2_color = (50, 50 ,50)
enemyCube2_active = False

enemyCube3_x = WIDTH - 200
enemyCube3_y = HEIGHT - 55
enemyCube3_color = (50, 50 ,50)
enemyCube3_active = False

#Set Cube Proporties
cubeHealth = 3
cubeSize = 50
cube_Speed = 5
cube_x = WIDTH // 2
cube_y = HEIGHT // 2

#Set Coin Proporties
coin_Radius = 20
coin_x = cube_x + 20 
coin_y = cube_y + 20

#Health Coin Proporties
health_Radius = 20
health_x = cube_x - 40
health_y = cube_y + 100

# #Set Freeze Proporties
# randPosY = random.randint(-5, 5)
# randPosX = random.randint(-5, 5)

# freeze_Duration = 2
# freeze_Radius = 20
# freeze_x = cube_x + randPosX * 20
# freeze_y = cube_y + randPosY * 20
# freeze = False

#Set clock
clock = pygame.time.Clock()

running = True
while running:





##########################################################################################################
    #Move enemies
    if enemyCube1_active == True:

        if cube_x > enemyCube1_x:
           enemyCube1_x += 0.5
           if enemyCube1_x == cube_x and enemyCube1_y == cube_y and db == True:
            cubeHealth -= 1
            db = False


        elif cube_x < enemyCube1_x:
            enemyCube1_x -= 0.5
            if enemyCube1_x == cube_x and enemyCube1_y == cube_y and db == True:
                cubeHealth -= 1
                db = False
            

        elif cube_y > enemyCube1_y:
            enemyCube1_y += 0.5
            if enemyCube1_y == cube_y and enemyCube1_x == cube_x and db == True:
                cubeHealth -= 1
                db = False
             

        elif cube_y < enemyCube1_y:
            enemyCube1_y -= 0.5
            if enemyCube1_y == cube_y and enemyCube1_x == cube_x and db == True:
                cubeHealth -= 1
                db = False

#############################################################################################################

    if enemyCube2_active == True:

        if cube_y > enemyCube2_y:
            enemyCube2_y += 1
            if enemyCube2_y == cube_y and enemyCube2_x == cube_x and db2 == True:
                cubeHealth -= 1
                db2 = False
             

        elif cube_y < enemyCube2_y:
            enemyCube2_y -= 1
            if enemyCube2_y == cube_y and enemyCube2_x == cube_x and db2 == True:
                cubeHealth -= 1
                db2 = False


        elif cube_x > enemyCube2_x:
           enemyCube2_x += 1
           if enemyCube2_x == cube_x and enemyCube2_y == cube_y and db2 == True:
            cubeHealth -= 1
            db2 = False


        elif cube_x < enemyCube2_x:
            enemyCube2_x -= 1
            if enemyCube2_x == cube_x and enemyCube2_y == cube_y and db2 == True:
                cubeHealth -= 1
                db2 = False
            


            

#############################################################################################################


    if enemyCube3_active == True:

        if cube_x > enemyCube3_x:
           enemyCube3_x += 2
           if enemyCube3_x == cube_x and enemyCube3_y == cube_y and db3 == True:
            cubeHealth -= 1
            db3 = False


        elif cube_x < enemyCube3_x:
            enemyCube3_x -= 2
            if enemyCube3_x == cube_x and enemyCube3_y == cube_y and db3 == True:
                cubeHealth -= 1
                db3 = False
            

        if cube_y > enemyCube3_y:
            enemyCube3_y += 2
            if enemyCube3_y == cube_y and enemyCube3_x == cube_x and db3 == True:
                cubeHealth -= 1
                db3 = False
             

        elif cube_y < enemyCube3_y:
            enemyCube3_y -= 2
            if enemyCube3_y == cube_y and enemyCube3_x == cube_x and db3 == True:
                cubeHealth -= 1
                db3 = False
                
                
    db = True
    db2 = True
    db3 = True
###########################################################################################################

        
        #enemyCube1_y

    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            print(event)
        

        if event.type == pygame.KEYDOWN: 
            

            if event.key == pygame.K_w and cube_y > HEIGHT//8 - cubeSize:
                cube_y -= 20

            elif event.key == pygame.K_s and cube_y < HEIGHT - cubeSize:
                 cube_y += 20
        
            elif event.key == pygame.K_a and cube_x > WIDTH//10 - cubeSize:
                cube_x -= 20

            elif event.key == pygame.K_d and cube_x < WIDTH - cubeSize:
                cube_x += 20

                if cube_x < coin_x + coin_Radius and cube_x + cubeSize > coin_x and cube_y < coin_y + coin_Radius and cube_y + cubeSize > coin_y:


                    if cube_y == coin_y:

                        randNum = random.randint(-10, 10)
                        randPos = randNum * 20
                        score += 1


                        coin_x = cube_x + randPos
                        coin_y = cube_y + randPos
                        

    if coin_x == cube_x + randNum_x * 20 and coin_y == cube_y + randNum_y * 20:

        if cube_y == coin_y:

            randNum_x = random.randint(-10, 10) # Random offset for X position 
            randNum_y = random.randint(-10, 10) # When collision occurs, update the coin's position randomly 
            
            score += 1

            coin_x = cube_x + randNum_x * 20
            coin_y = cube_y + randNum_y * 20

    if health_x == cube_x + randNum_x * 20 and health_y == cube_y + randNum_y * 20:

        if cube_y == health_y:

            randNum_x2 = random.randint(-10, 10) # Random offset for X position 
            randNum_y2 = random.randint(-10, 10) # When collision occurs, update the coin's position randomly 
            
            if cubeHealth < 3:
                cubeHealth += 1

            health_x = cube_x + randNum_x2 * 20
            health_y = cube_y + randNum_y2 * 20






    
    white = (255, 255, 255)
    black = (0, 0, 0)


    #fill/clear the screen
    screen.fill(black) 
    


    #create squares
    if score == 0:
        pygame.draw.rect(screen, enemyCube1_color, (enemyCube1_x, enemyCube1_y, enemyCubeSize, enemyCubeSize)) 
        pygame.draw.rect(screen, enemyCube2_color, (enemyCube2_x, enemyCube2_y, enemyCubeSize, enemyCubeSize))
        pygame.draw.rect(screen, enemyCube3_color, (enemyCube3_x, enemyCube3_y, enemyCubeSize, enemyCubeSize))
    elif score == 1:
        enemyCube1_color = (255, 0, 0)
        enemyCube1_active = True
        pygame.draw.rect(screen, enemyCube1_color, (enemyCube1_x, enemyCube1_y, enemyCubeSize, enemyCubeSize)) 
        pygame.draw.rect(screen, enemyCube2_color, (enemyCube2_x, enemyCube2_y, enemyCubeSize, enemyCubeSize))
        pygame.draw.rect(screen, enemyCube3_color, (enemyCube3_x, enemyCube3_y, enemyCubeSize, enemyCubeSize))
    elif score == 2:
        enemyCube2_color = (255, 0, 0)
        enemyCube2_active = True
        pygame.draw.rect(screen, enemyCube1_color, (enemyCube1_x, enemyCube1_y, enemyCubeSize, enemyCubeSize)) 
        pygame.draw.rect(screen, enemyCube2_color, (enemyCube2_x, enemyCube2_y, enemyCubeSize, enemyCubeSize))
        pygame.draw.rect(screen, enemyCube3_color, (enemyCube3_x, enemyCube3_y, enemyCubeSize, enemyCubeSize))
    elif score == 3:
        enemyCube3_color = (255, 0, 0)
        enemyCube3_active = True
        pygame.draw.rect(screen, enemyCube1_color, (enemyCube1_x, enemyCube1_y, enemyCubeSize, enemyCubeSize)) 
        pygame.draw.rect(screen, enemyCube2_color, (enemyCube2_x, enemyCube2_y, enemyCubeSize, enemyCubeSize))
        pygame.draw.rect(screen, enemyCube3_color, (enemyCube3_x, enemyCube3_y, enemyCubeSize, enemyCubeSize))
    elif score >= 1:
        pygame.draw.rect(screen, enemyCube1_color, (enemyCube1_x, enemyCube1_y, enemyCubeSize, enemyCubeSize)) 
        pygame.draw.rect(screen, enemyCube2_color, (enemyCube2_x, enemyCube2_y, enemyCubeSize, enemyCubeSize))
        pygame.draw.rect(screen, enemyCube3_color, (enemyCube3_x, enemyCube3_y, enemyCubeSize, enemyCubeSize))

    #Create Healthbar

    if cubeHealth == 3:
        pygame.draw.rect(screen, (0, 255, 0), (HEIGHT - 550, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (0, 255, 0), (HEIGHT - 450, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (0, 255, 0), (HEIGHT - 350, WIDTH - 775, 50, 50)) #Healthbar    
    elif cubeHealth == 2:
        pygame.draw.rect(screen, (0, 255, 0), (HEIGHT - 550, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (0, 255, 0), (HEIGHT - 450, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (255, 0, 0), (HEIGHT - 350, WIDTH - 775, 50, 50)) #Healthbar    
    elif cubeHealth == 1:
        pygame.draw.rect(screen, (0, 255, 0), (HEIGHT - 550, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (255, 0, 0), (HEIGHT - 450, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (255, 0, 0), (HEIGHT - 350, WIDTH - 775, 50, 50)) #Healthbar    
    elif cubeHealth == 0:
        pygame.draw.rect(screen, (255, 0, 0), (HEIGHT - 550, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (255, 0, 0), (HEIGHT - 450, WIDTH - 775, 50, 50)) #Healthbar
        pygame.draw.rect(screen, (255, 0, 0), (HEIGHT - 350, WIDTH - 775, 50, 50)) #Healthbar   
        running = False
    



    pygame.draw.rect(screen, (255, 255, 255), (cube_x, cube_y, cubeSize, cubeSize)) #player

    pygame.draw.circle(screen, (255, 255, 0), (coin_x, coin_y), 20) #coin

    pygame.draw.circle(screen, (0, 255, 0), (health_x, health_y), 20) #Health token



    #update the display
    pygame.display.flip()

    #Tick Clock
    clock.tick(60)


#Quit pygame / When the loop ends because the player "Quits" close the tab
pygame.quit()


    
    
        
        

        
