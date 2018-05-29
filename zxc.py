import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,255)
mix = (255,127,127)
display_width = 900
display_height = 600
FPS = 15

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Kelner')

pygame.display.update()

gameExit = False
lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()
block_size = 30


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -30
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 30
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_x_change = 0
                lead_y_change = -30
            elif event.key == pygame.K_DOWN:
                lead_y_change = 30
                lead_x_change = 0
            elif event.key == pygame.K_SPACE:
                lead_y_change = 0
                lead_x_change = 0

    if lead_x > 750:
        lead_x = 750
    if lead_x < 50:
        lead_x = 50
    if lead_y > 750:
        lead_y = 750
    if lead_y < 50:
        lead_y = 50
    lead_x += lead_x_change
    lead_y += lead_y_change


    myArray=[[0 for j in range(30)] for i in range(20)]
    myArray[20][30] = 3
    myArray[15][15] = 4
#    print (myArray[3][3])
#   print (myArray[4][4])

    gameDisplay.fill(white)

    
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
#    for x in range(0,30):
 #       for y in range(0,20):
  #          if (myArray[x][y]!=0):
   #             gameDisplay.fill(red,rect=[x,y,block_size,block_size])               
    gameDisplay.fill(red,rect=[200,200,block_size,block_size])
    gameDisplay.fill(red,rect=[400,200,block_size,block_size])
    gameDisplay.fill(blue,rect=[200,350,block_size,block_size])
    gameDisplay.fill(blue,rect=[400,350,block_size,block_size])
    gameDisplay.fill(blue,rect=[600,400,block_size,block_size])
    gameDisplay.fill(blue,rect=[100,500,block_size,block_size])
    gameDisplay.fill(mix,rect=[100,300,block_size,block_size])
    gameDisplay.fill(mix,rect=[30,40,block_size,block_size])
    gameDisplay.fill(mix,rect=[730,550,block_size,block_size])


    pygame.display.update()

    clock.tick(FPS)
    
pygame.quit()
quit()

