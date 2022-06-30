import pygame

screen = pygame.display.set_mode([width := 700, height := 500])
pygame.display.set_caption('idk if its gonna hit a corner')

velSize = 1
objectVel = [velSize, velSize]
objectPos = [width/2, height/2]
objectSize = [50, 50]

while 1:
    screen.fill((0, 0, 255))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit() 

    objectPos[0] += objectVel[0]
    objectPos[1] += objectVel[1]

    #Detecting if rect is touching the border
    if objectPos[0] <= 0:
        objectVel[0] = velSize 
    elif objectPos[0] + objectSize[0]>= width:
        objectVel[0] = -velSize

    if objectPos[1] <= 0:
        objectVel[1] = velSize
    elif objectPos[1] + objectSize[1]>= height:
        objectVel[1] = -velSize

    if objectPos == [0, 0] or objectPos == [width, height] or objectPos == [width, 0] or objectPos == [0, height]:
        print("YOU HIT THE CORNER")
        quit()

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(objectPos[0], objectPos[1], objectSize[0], objectSize[1]))

    pygame.time.Clock().tick(60)
    pygame.display.flip() 
