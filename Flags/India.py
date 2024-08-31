import pygame
import math

# Function to plot the spokes on the wheel
def spokePlotter(startX, startY, length, angle):
    spokePoints = []
    
    spokePoints.append((startX, startY)) # Bottom point
    spokePoints.append((startX + (math.tan(angle / 2) * length / 3 ), startY - (length / 3))) # Mid right point
    spokePoints.append((startX, startY - length)) # Top point
    spokePoints.append((startX - (math.tan(angle / 2) * length / 3 ), startY - (length / 3))) # Mid left point

    return spokePoints

# Screen resolution
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
saffron = (255, 103, 31) # Saffron represents courage and sacrifice
white = (255, 255, 255) # The white represents peace and truth
blue = (6, 3, 141)
green = (4, 106, 56) # Green represents faith and chivalry

def drawFlag():
    surface = pygame.Surface((screenWidth, screenHeight))

    surface.fill(white)
    pygame.draw.rect(surface, saffron, [0, 0, screenWidth, screenHeight / 3])
    pygame.draw.rect(surface, green, [0, screenHeight * 2 / 3, screenWidth, screenHeight / 3])

    # Generates the Ashoka Chakra (Emperor Ashoka's wheel), or Dharmachakra (the wheel of law and duty)
    outerRadius = screenHeight * 2 / 13
    innerRadius = screenHeight * 2 / 15
    pygame.draw.circle(surface, blue, (screenWidth / 2, screenHeight / 2), outerRadius)
    pygame.draw.circle(surface, white, (screenWidth / 2, screenHeight / 2), innerRadius)
    pygame.draw.circle(surface, blue, (screenWidth / 2, screenHeight / 2), innerRadius / 4)

    angle = math.radians(15)
    for counter in range(1, 25):
        x = innerRadius * math.sin(angle * counter)
        y = innerRadius * math.cos(angle * counter)
        newX = x * math.cos(math.radians(7.5)) - y * math.sin(math.radians(7.5))
        newY = y * math.cos(math.radians(7.5)) + x * math.sin(math.radians(7.5))
        newX += screenWidth / 2
        newY += screenHeight / 2
        pygame.draw.circle(surface, blue, (newX, newY), 7)
    
    # Generates the 24 spokes on the wheel. Each spoke represents different things, including love, courage and patience
    for counter in range (0, 24):
        spokePoints = spokePlotter(screenWidth / 2, screenHeight / 2 - innerRadius / 4, innerRadius * 0.7, math.radians(25))
        rotatedPoints = []
        for point in spokePoints:
            x = point[0] - screenWidth / 2
            y = point[1] - screenHeight / 2
            newX = x * math.cos(angle * counter) - y * math.sin(angle * counter)
            newY = y * math.cos(angle * counter) + x * math.sin(angle * counter)
            newX += screenWidth / 2
            newY += screenHeight / 2
            rotatedPoints.append((newX, newY))

        pygame.draw.polygon(surface, blue, rotatedPoints)

    return surface

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    surface = drawFlag()
    screen.blit(surface, (0, 0))
    pygame.display.update()

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(5)

    pygame.quit()