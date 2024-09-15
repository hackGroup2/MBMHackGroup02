class Button:
    def __init__(self,xPos:int,yPos:int,text:str,textColor,buttonColor,colorOnClick,borderColor,width:int,height:int):
        self.xPos = xPos
        self.yPos = yPos
        self.text = text
        self.textColor = textColor
        self.buttonColor = buttonColor
        self.colorOnClick = colorOnClick
        self.borderColor = borderColor
        self.width = width
        self.height = height

    def drawSelf(self):
        buttonText = gameFont.render(self.text,True,self.textColor)
        rectangleDim = pygame.Rect(self.xPos,self.yPos,self.width,self.height)
        if self.checkForClick():
            pygame.draw.rect(screen,self.colorOnClick,rectangleDim,0,3)
        else:
            pygame.draw.rect(screen,self.buttonColor,rectangleDim,0,3)
        pygame.draw.rect(screen,self.borderColor,rectangleDim,2,3)
        textRect = buttonText.get_rect(center=rectangleDim.center)
        screen.blit(buttonText,textRect.topleft)

    def checkForClick(self):
        mousePos = pygame.mouse.get_pos()
        rectangleDim = pygame.Rect(self.xPos,self.yPos,self.width,self.height)
        leftClick = pygame.mouse.get_pressed()[0]
        if leftClick and rectangleDim.collidepoint(mousePos):
            return True
        else:
            
            return False
            
class ResourceCounter:
    def __init__(self,text:str,textColor,iconPath,circleCenter:tuple,circleRadius:int,circleColor,circleBorder:bool,circleBorderColor,rectWidth:int,rectHeight:int,rectColor):
        self.text = text
        self.textColor = textColor
        self.iconPath = iconPath
        self.circleCenter = circleCenter
        self.circleRadius = circleRadius
        self.circleColor = circleColor
        self.circleBorder = circleBorder
        self.circleBorderColor = circleBorderColor 
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
        self.rectColor = rectColor

    def drawSelf(self):
        label = gameFont.render(self.text,True,self.textColor)
        rectangleDim = pygame.Rect(self.circleCenter[0]+(self.circleRadius*0.75),(self.circleCenter[1]-self.circleRadius),self.rectWidth,self.rectHeight)
        pygame.draw.rect(screen,self.rectColor,rectangleDim,0,3)
        textRect = label.get_rect(center=rectangleDim.center)
        screen.blit(label,textRect.topleft)  
        if self.circleBorder:
            pygame.draw.circle(screen,self.circleBorderColor,self.circleCenter,(self.circleRadius+5), 5)
        pygame.draw.circle(screen,self.circleColor,self.circleCenter,self.circleRadius)
        icon = pygame.image.load(self.iconPath)
        iconRect = icon.get_rect(center=self.circleCenter)
        screen.blit(icon,iconRect.topleft)

    def updateText(self,inputText):
        self.text = inputText
        self.drawSelf()

waterIcon = ResourceCounter("Water: "+str(waterCount),"white",getcwd() + '\\' + 'water.png',(46,20),15,"white",True,"blue",110,30,"blue")
foodIcon = ResourceCounter("Food: "+str(foodCount),"white",getcwd() + '\\' + 'water.png',(208,20),15,"white",True,"blue",110,30,"blue")
moneyIcon = ResourceCounter("Money: "+str(money),"white",getcwd() + '\\' + 'water.png',(370,20),15,"white",True,"blue",110,30,"blue")
energyIcon = ResourceCounter("Energy: "+str(energyCount),"white",getcwd() + '\\' + 'water.png',(532,20),15,"white",True,"blue",110,30,"blue")
populationIcon = ResourceCounter("Pop: "+str(population),"white",getcwd() + '\\' + 'water.png',(694,20),15,"white",True,"blue",110,30,"blue")
pollutionIcon = ResourceCounter("Pollution: "+str(pollution),"white",getcwd() + '\\' + 'water.png',(856,20),15,"white",True,"blue",110,30,"blue")
buyFarmButton = Button(50,50,"Buy Farm","white","#007BFF","#0056b3","#003d7a",150,30)
buyWindmillButton = Button(50,125,"Buy Windmill","white","#007BFF","#0056b3","#003d7a",150,30)
buyCoalPlantButton = Button(50,200,"Buy Coal Plant","white","#007BFF","#0056b3","#003d7a",150,30)
buyStoreButton = Button(50,275,"Buy Store","white","#007BFF","#0056b3","#003d7a",150,30)
buyParkButton = Button(50,350,"Buy Park","white","#007BFF","#0056b3","#003d7a",150,30)
buyFactoryButton = Button(50,425,"Buy Factory","white","#007BFF","#0056b3","#003d7a",150,30)
buyLakeButton = Button(50,500,"Buy Lake","white","#007BFF","#0056b3","#003d7a",150,30)
buyHousingButton = Button(50,575,"Buy Housing","white","#007BFF","#0056b3","#003d7a",150,30)

toRun = True
while toRun:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            toRun = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if buyFarmButton.checkForClick():
                if money >= 30:
                    numFarms += 1
                    money -= 30
            if buyWindmillButton.checkForClick():
                if money >= 25:
                    numWindmills += 1
                    money -= 25
            if buyCoalPlantButton.checkForClick():
                if money >= 15:
                    numCoalplants += 1
                    money -= 15
            if buyStoreButton.checkForClick():
                if money >= 45:
                    numStores += 1
                    money -= 45
            if buyParkButton.checkForClick():
                if money >= 15:
                    numParks += 1
                    money -= 15
            if buyFactoryButton.checkForClick():
                if money >= 60:
                    numFactories += 1
                    money -= 60
            if buyLakeButton.checkForClick():
                if money >= 25:
                    numLakes += 1
                    money -= 25
            if buyHousingButton.checkForClick():
                if money >= 25:
                    numHousing += 1
                    money -= 25

            
    
    currentTime = pygame.time.get_ticks()
    if currentTime - previousTime >= interval:
        #Population consumption - to Add
        energyCount += numCoalplants*30 + numWindmills*20 - (numFarms*5 + numStores*10 + numParks*3 + numFactories*10 + numLakes +numHousing*10)
        waterCount += numLakes*30 - (numFarms*10 + numStores*3 + numFactories*10 + numHousing*10)
        foodCount += numFarms*30 - (numStores*20 + numParks + numFactories*10 +numHousing*10)
        money += numFactories*15 + numStores*5 - (numFarms*2 + numWindmills + numCoalplants + numParks + numLakes + numHousing*2)
    
        previousTime = currentTime

    waterIcon.updateText("Water: "+str(waterCount))
    foodIcon.updateText("Food: "+str(foodCount))
    moneyIcon.updateText("Money: "+str(money))
    energyIcon.updateText("Energy: "+str(energyCount))
    populationIcon.updateText("Pop: "+str(population))
    pollutionIcon.updateText("Pollution: "+str(pollution))
    buyFarmButton.drawSelf
    buyWindmillButton.drawSelf()
    buyCoalPlantButton.drawSelf()
    buyStoreButton.drawSelf()
    buyParkButton.drawSelf()
    buyFactoryButton.drawSelf()
    buyLakeButton.drawSelf()
    buyHousingButton.drawSelf()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
