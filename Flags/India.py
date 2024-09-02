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
smoothFactor = 4
smoothing = True
screen = pygame.display.set_mode((screenWidth, screenHeight))


# Define colours
saffron = (255, 103, 31) # Saffron represents courage and sacrifice
white = (255, 255, 255) # The white represents peace and truth
blue = (6, 3, 141)
green = (4, 106, 56) # Green represents faith and chivalry

def drawFlag():
    surfaceHeight = screenHeight * smoothFactor
    surfaceWidth = screenWidth * smoothFactor
    surface = pygame.Surface((surfaceWidth, surfaceHeight))

    surface.fill(white)
    pygame.draw.rect(surface, saffron, [0, 0, surfaceWidth, surfaceHeight / 3])
    pygame.draw.rect(surface, green, [0, surfaceHeight * 2 / 3, surfaceWidth, surfaceHeight / 3])

    # Generates the Ashoka Chakra (Emperor Ashoka's wheel), or Dharmachakra (the wheel of law and duty)
    outerRadius = surfaceHeight * 2 / 13
    innerRadius = surfaceHeight * 2 / 15
    pygame.draw.circle(surface, blue, (surfaceWidth / 2, surfaceHeight / 2), outerRadius)
    pygame.draw.circle(surface, white, (surfaceWidth / 2, surfaceHeight / 2), innerRadius)
    pygame.draw.circle(surface, blue, (surfaceWidth / 2, surfaceHeight / 2), innerRadius / 4)

    angle = math.radians(15)
    halfAngle = math.radians(7.5)
    for counter in range(1, 25):
        x = innerRadius * math.sin(angle * counter)
        y = innerRadius * math.cos(angle * counter)
        newX = x * math.cos(halfAngle) - y * math.sin(halfAngle)
        newY = y * math.cos(halfAngle) + x * math.sin(halfAngle)
        newX += surfaceWidth / 2
        newY += surfaceHeight / 2
        pygame.draw.circle(surface, blue, (newX, newY), surfaceHeight / 100)
    
    # Generates the 24 spokes on the wheel. Each spoke represents different things, including love, courage and patience
    for counter in range (0, 24):
        spokePoints = spokePlotter(surfaceWidth / 2, surfaceHeight / 2 - innerRadius / 4, innerRadius * 0.7, math.radians(25))
        rotatedPoints = []
        for point in spokePoints:
            x = point[0] - surfaceWidth / 2
            y = point[1] - surfaceHeight / 2
            newX = x * math.cos(angle * counter) - y * math.sin(angle * counter)
            newY = y * math.cos(angle * counter) + x * math.sin(angle * counter)
            newX += surfaceWidth / 2
            newY += surfaceHeight / 2
            rotatedPoints.append((newX, newY))

        pygame.draw.polygon(surface, blue, rotatedPoints)

    surface = pygame.transform.smoothscale(surface, (screenWidth, screenHeight))
    return surface

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    running = True

    surface = drawFlag()

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
                    surface = drawFlag()

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(5)

    pygame.quit()