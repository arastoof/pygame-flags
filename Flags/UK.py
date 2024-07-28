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

# Function to generate a star rotated through an angle using the starPlotter function
def rotatedRectPlotter(xCentre, yCentre, xSize, ySize, angle):
    rectPoints = rectPlotter(0, 0, xSize, ySize)
    newRectPoints = []
    for (x, y) in rectPoints:
        newRectPoints.append((x * math.cos(angle) - y * math.sin(angle) + xCentre, x * math.sin(angle) + y * math.cos(angle) + yCentre))
    return newRectPoints

# Screen resolution
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (206, 17, 45) # Red represents England and courage
white = (255, 255, 255) # White represents Scotland and purity
blue = (1, 33, 105) # Blue represents Ireland and loyalty

def drawFlag():
    screen.fill(blue)
    
    # The union flag is meant to combine the crosses of the flags of the three nations that have been united under one sovreign:
    # Scotland - Represented by the blue background and the white St Andrew's saltire
    diagonalRectPoints = rotatedRectPlotter(screenWidth / 2, screenHeight / 2, screenHeight / 5, (screenWidth ** 2 + screenHeight ** 2) ** 0.5, math.radians(60))
    pygame.draw.polygon(screen, white, diagonalRectPoints) # Draws the positive white diagonal
    diagonalRectPoints = rotatedRectPlotter(screenWidth / 2, screenHeight / 2, screenHeight / 5, (screenWidth ** 2 + screenHeight ** 2) ** 0.5, math.radians(120))
    pygame.draw.polygon(screen, white, diagonalRectPoints) # Draws the negative white diagonal

    # Ireland - Represented by the red St Patrick's saltire (though only Northern Ireland is in the union, which doesn't have an official flag)
    quadrantCentre = ((screenWidth - (screenWidth / 2 + screenHeight / 6)) / 2, (screenHeight - (screenHeight / 2 - screenHeight / 6) / 2))
    diagonalRectPoints = rotatedRectPlotter(quadrantCentre[0], quadrantCentre[1], screenHeight / 15, (screenWidth ** 2 + screenHeight ** 2) ** 0.5 * 0.5, math.radians(60))
    pygame.draw.polygon(screen, red, diagonalRectPoints) # Draws the bottom left red diagonal

    quadrantCentre = ((screenWidth + (screenWidth / 2 + screenHeight / 6)) / 2, ((screenHeight / 2 - screenHeight / 6) / 2))
    diagonalRectPoints = rotatedRectPlotter(quadrantCentre[0], quadrantCentre[1], screenHeight / 15, (screenWidth ** 2 + screenHeight ** 2) ** 0.5 * 0.5, math.radians(60))
    pygame.draw.polygon(screen, red, diagonalRectPoints) # Draws the top right red diagonal

    quadrantCentre = ((screenWidth - (screenWidth / 2 + screenHeight / 6)) / 2, ((screenHeight / 2 - screenHeight / 6) / 2))
    diagonalRectPoints = rotatedRectPlotter(quadrantCentre[0], quadrantCentre[1], screenHeight / 15, (screenWidth ** 2 + screenHeight ** 2) ** 0.5 * 0.5, math.radians(120))
    pygame.draw.polygon(screen, red, diagonalRectPoints) # Draws the top left red diagonal

    quadrantCentre = ((screenWidth + (screenWidth / 2 + screenHeight / 6)) / 2, (screenHeight - (screenHeight / 2 - screenHeight / 6) / 2))
    diagonalRectPoints = rotatedRectPlotter(quadrantCentre[0], quadrantCentre[1], screenHeight / 15, (screenWidth ** 2 + screenHeight ** 2) ** 0.5 * 0.5, math.radians(120))
    pygame.draw.polygon(screen, red, diagonalRectPoints) # Draws the bottom right red diagonal

    pygame.draw.polygon(screen, white, rectPlotter(screenWidth / 2, screenHeight / 2, screenHeight / 3, screenHeight)) # White vertical
    pygame.draw.polygon(screen, white, rectPlotter(screenWidth / 2, screenHeight / 2, screenWidth, screenHeight / 3)) # White horizontal
    
    # England and Wales - Represented by the straight red St George's cross (though this only uses England's flag)
    pygame.draw.polygon(screen, red, rectPlotter(screenWidth / 2, screenHeight / 2, screenHeight / 5, screenHeight)) # Red vertical
    pygame.draw.polygon(screen, red, rectPlotter(screenWidth / 2, screenHeight / 2, screenWidth, screenHeight / 5)) # Red horizontal

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawFlag()
        pygame.display.update()

    pygame.quit()