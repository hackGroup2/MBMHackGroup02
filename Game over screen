import os
import pygame
pygame.init()

# Setup
gameFont = pygame.font.Font(None, 25)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
pygame.display.set_caption("MBM Hackathon Group 2 project")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

interval = 5000
previousTime = pygame.time.get_ticks()
energyCount = 15
waterCount = 15
foodCount = 15
money = 15
population = 10
pollution = 3
pollution_threshold = 50  # Define the pollution threshold for game over
numFarms = numWindmills = numCoalplants = numStores = numParks = numFactories = numLakes = numHousing = 0

circleWaterCenter = (20, 20)
circleWaterRadius = 15
rectWater = pygame.Rect(35, 5, 100, 30)

try:
    dir = os.getcwd() + '\\' + 'water.png'
    iconWater = pygame.image.load(dir)
except pygame.error as e:
    print(f"Failed to load image: {e}")
    pygame.quit()

def game_over_screen(message):
    screen.fill((0, 0, 0))
    gameOverText = gameFont.render(message, True, (255, 0, 0))
    restartText = gameFont.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    gameOverTextRect = gameOverText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
    restartTextRect = restartText.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    screen.blit(gameOverText, gameOverTextRect)
    screen.blit(restartText, restartTextRect)
    pygame.display.update()

def main_game_loop():
    global energyCount, waterCount, foodCount, money, pollution, previousTime
    toRun = True
    while toRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return 'quit'
                elif event.key == pygame.K_r:
                    # Reset game state
                    reset_game()
                    return 'restart'

        currentTime = pygame.time.get_ticks()
        if currentTime - previousTime >= interval:
            energyCount += numCoalplants * 30 + numWindmills * 20 - (numFarms * 5 + numStores * 10 + numParks * 3 + numFactories * 10 + numLakes + numHousing * 10)
            waterCount += numLakes * 30 - (numFarms * 10 + numStores * 3 + numFactories * 10 + numHousing * 10)
            foodCount += numFarms * 30 - (numStores * 20 + numParks + numFactories * 10 + numHousing * 10)
            money += numFactories * 15 + numStores * 5 - (numFarms * 2 + numWindmills + numCoalplants + numParks + numLakes + numHousing * 2)
            pollution += numFactories * 2 + numStores * 1  # Example pollution generation
            previousTime = currentTime

        if energyCount <= 0:
            return 'game_over', "Not enough energy!"
        elif waterCount <= 0:
            return 'game_over', "Not enough water!"
        elif foodCount <= 0:
            return 'game_over', "Not enough food!"
        elif money <= 0:
            return 'game_over', "Not enough money!"
        elif pollution > pollution_threshold:
            return 'game_over', "Pollution is too high!"

        # Rendering
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0, 0, 255), circleWaterCenter, (circleWaterRadius + 5), 5)
        pygame.draw.circle(screen, (255, 255, 255), circleWaterCenter, circleWaterRadius)
        waterIconRect = iconWater.get_rect(center=circleWaterCenter)
        screen.blit(iconWater, waterIconRect.topleft)
        labelWater = gameFont.render("Water:" + str(waterCount), True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 255), rectWater)
        waterTextRect = labelWater.get_rect(center=rectWater.center)
        screen.blit(labelWater, waterTextRect.topleft)
        pygame.display.update()
        clock.tick(60)

def reset_game():
    global energyCount, waterCount, foodCount, money, pollution, numFarms, numWindmills, numCoalplants, numStores, numParks, numFactories, numLakes, numHousing
    energyCount = 15
    waterCount = 15
    foodCount = 15
    money = 15
    pollution = 3
    numFarms = numWindmills = numCoalplants = numStores = numParks = numFactories = numLakes = numHousing = 0

# Main game loop
while True:
    result, message = main_game_loop()
    if result == 'game_over':
        while True:
            game_over_screen(message)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_r:
                        reset_game()
                        break
    elif result == 'quit':
        pygame.quit()
        exit()
