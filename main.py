import pygame
pygame.init()

gameFont = pygame.font.Font(None, 25)
SCREEN_WIDTH,SCREEN_HEIGHT = 800,600
pygame.display.set_caption("MBM Hackathon Group 2 project")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

interval = 5000
previousTime = pygame.time.get_ticks()
#Starting Resources
energyCount = 15
waterCount = 15
foodCount = 15
money = 15
population = 10
pollution = 3

#Starting Buildings
numFarms = 0
numWindmills = 0
numCoalplants = 0
numStores = 0
numParks = 0
numFactories = 0
numLakes = 0
numHousing = 0


circleWaterCenter = (20,20)
circleWaterRadius = 15
rectWater = pygame.Rect(35,5,100,30 )

try:
    iconWater = pygame.image.load('water.png')
except pygame.error as e:
    print(f"Failed to load image: {e}")
    pygame.quit()

toRun = True
while toRun:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            toRun = False
    
    currentTime = pygame.time.get_ticks()
    if currentTime - previousTime >= interval:
        #Population consumption - to Add
        energyCount += numCoalplants*30 + numWindmills*20 - (numFarms*5 + numStores*10 + numParks*3 + numFactories*10 + numLakes +numHousing*10)
        waterCount += numLakes*30 - (numFarms*10 + numStores*3 + numFactories*10 + numHousing*10)
        foodCount += numFarms*30 - (numStores*20 + numParks + numFactories*10 +numHousing*10)
        money += numFactories*15 + numStores*5 - (numFarms*2 + numWindmills + numCoalplants + numParks + numLakes + numHousing*2)
        numWater = gameFont.render("Water:" + str(waterCount), False, (255,255,255)) 
        previousTime = currentTime
    
    labelWater = gameFont.render("Water:" + str(waterCount),True,(255,255,255))
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(0, 0, 255),circleWaterCenter,(circleWaterRadius+5), 5)
    pygame.draw.circle(screen,(255, 255, 255),circleWaterCenter,(circleWaterRadius))

    waterIconRect = iconWater.get_rect(center=circleWaterCenter)
    screen.blit(iconWater, waterIconRect.topleft)

    pygame.draw.rect(screen,(0, 0, 255),rectWater)  
    waterTextRect = labelWater.get_rect(center=rectWater.center)
    screen.blit(labelWater, waterTextRect.topleft)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
