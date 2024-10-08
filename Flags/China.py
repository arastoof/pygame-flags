import pygame
import math

# Function to generate a 10 pointed star. x and y are coordinates, r is to do with size.
def starPlotter(x, y, r): 
    starPoints = []
    rAlt = r * 0.4

    for counter in range(0, 5):
        # Outer points
        angle = math.radians(72 * counter - 90)  
        starPoints.append((x + r * math.cos(angle), y + r * math.sin(angle)))
        
        # Inner points
        angle = math.radians(72 * counter - 90 + 36)  
        starPoints.append((x + rAlt * math.cos(angle), y + rAlt * math.sin(angle)))

    return starPoints

# Function to generate a star rotated through an angle using the starPlotter function
def rotatedStarPlotter(xCentre, yCentre, r, angle):
    starPoints = starPlotter(0, 0, r)
    newStarPoints = []
    for (x, y) in starPoints:
        newStarPoints.append((x * math.cos(angle) - y * math.sin(angle) + xCentre, x * math.sin(angle) + y * math.cos(angle) + yCentre))
    return newStarPoints

# Screen resolution
screenWidth = 1280
screenHeight = 720
smoothFactor = 4
smoothing = True
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (238, 28, 37) # Red represents the Chinese Communist Revolution
yellow = (255, 255, 0)

def drawFlag(surfaceWidth, surfaceHeight):
    surface = pygame.Surface((surfaceWidth, surfaceHeight))

    surface.fill(red)

    # The big yellow star represents the Chinese Communist Party
    starX = surfaceWidth / 7
    starY = surfaceHeight / 4
    bigStarSize = surfaceWidth / 10
    pygame.draw.polygon(surface, yellow, starPlotter(starX, starY, bigStarSize))

    # The smaller stars represent the unity of the Chinese people and the 4 main classes
    arcRadius = bigStarSize * 1.3
    rotations = [15, 45, 0, 15]
    for counter in range(1, 5):
        position = (1.6 * starX + arcRadius * math.sin(math.radians(36 * counter)), starY - arcRadius * math.cos(math.radians(36 * counter)))
    # The stars are  oriented towards the big star to represent the CCP's leadership
        pygame.draw.polygon(surface, yellow, rotatedStarPlotter(position[0], position[1], bigStarSize / 4, math.radians(rotations[counter - 1])))

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