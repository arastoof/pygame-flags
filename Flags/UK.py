import pygame
import math

# Function to plot a rectangle given a central point
def rectPlotter(x, y, xSize, ySize):
    rectPoints = []

    rectPoints.append((x - xSize / 2, y - ySize / 2)) # Top left point
    rectPoints.append((x + xSize / 2, y - ySize / 2)) # Top right point
    rectPoints.append((x + xSize / 2, y + ySize / 2)) # Bottom right point
    rectPoints.append((x - xSize / 2, y + ySize / 2)) # Bottom left point

    return rectPoints

# Function to generate a rectangle rotated through an angle using the rectPlotter function
def rotatedRectPlotter(xCentre, yCentre, xSize, ySize, angle):
    rectPoints = rectPlotter(0, 0, xSize, ySize)
    newRectPoints = []
    for (x, y) in rectPoints:
        newRectPoints.append((x * math.cos(angle) - y * math.sin(angle) + xCentre, x * math.sin(angle) + y * math.cos(angle) + yCentre))
    return newRectPoints

# Screen resolution
screenWidth = 1280
screenHeight = 720
smoothFactor = 4
smoothing = True
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (206, 17, 45) # Red represents England and courage
white = (255, 255, 255) # White represents Scotland and purity
blue = (1, 33, 105) # Blue represents Ireland and loyalty

def drawFlag(surfaceWidth, surfaceHeight):
    surface = pygame.Surface((surfaceWidth, surfaceHeight))

    halfHeight = surfaceHeight / 2
    halfWidth = surfaceWidth / 2

    surface.fill(blue)
    diagonalAngles = (math.radians(60), math.radians(120))
    diagonalSize = (surfaceWidth ** 2 + surfaceHeight ** 2) ** 0.5
    
    # The union flag is meant to combine the crosses of the flags of the three nations that have been united under one sovreign:
    # Scotland - Represented by the blue background and the white St Andrew's saltire
    for counter in range (0, 2):
        diagonalRectPoints = rotatedRectPlotter(halfWidth, halfHeight, surfaceHeight / 5, diagonalSize, diagonalAngles[counter])
        pygame.draw.polygon(surface, white, diagonalRectPoints)

    # Ireland - Represented by the red St Patrick's saltire (though only Northern Ireland is in the union, which doesn't have an official flag)
    baseQuadrantCentreX = (halfWidth + surfaceHeight / 6)
    size = diagonalSize * 0.5
    xMultipliers = (-1, 1, -1, 1)

    for counter in range(0, 4):
        quadrantCentreX = (surfaceWidth + (baseQuadrantCentreX * xMultipliers[counter])) / 2
        quadrantCentreY = (halfHeight - surfaceHeight / 6) / 2
        if (counter == 0 or counter == 3):
            quadrantCentreY = surfaceHeight - quadrantCentreY
        angle = diagonalAngles[0]
        if counter > 1:
            angle = diagonalAngles[1]
        diagonalRectPoints = rotatedRectPlotter(quadrantCentreX, quadrantCentreY, surfaceHeight / 15, size, angle)
        pygame.draw.polygon(surface, red, diagonalRectPoints)
            

    pygame.draw.polygon(surface, white, rectPlotter(halfWidth, halfHeight, surfaceHeight / 3, surfaceHeight)) # White vertical
    pygame.draw.polygon(surface, white, rectPlotter(halfWidth, halfHeight, surfaceWidth, surfaceHeight / 3)) # White horizontal
    
    # England and Wales - Represented by the straight red St George's cross (though this only uses England's flag)
    pygame.draw.polygon(surface, red, rectPlotter(halfWidth, halfHeight, surfaceHeight / 5, surfaceHeight)) # Red vertical
    pygame.draw.polygon(surface, red, rectPlotter(halfWidth, halfHeight, surfaceWidth, surfaceHeight / 5)) # Red horizontal

    surface = pygame.transform.smoothscale(surface, (screenWidth, screenHeight))
    return surface

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    running = True

    surface = drawFlag(screenWidth * smoothFactor, screenHeight * smoothFactor)

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    smoothing = not smoothing
                    if smoothing:
                        smoothFactor = 4
                    else:
                        smoothFactor = 1
                    surface = drawFlag(screenWidth * smoothFactor, screenHeight * smoothFactor)

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(5)

    pygame.quit()