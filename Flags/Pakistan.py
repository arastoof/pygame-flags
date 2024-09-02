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
green = (0, 64, 26) # Green represents Islam, the majority religion in the country
white = (255, 255, 255) # White represents the religious minorities in the country

def drawFlag():
    surfaceHeight = screenHeight * smoothFactor
    surfaceWidth = screenWidth * smoothFactor
    surface = pygame.Surface((surfaceWidth, surfaceHeight))

    # The green and white together mean unity.
    surface.fill(white)
    greenWidth = surfaceWidth * 3 / 4
    pygame.draw.rect(surface, green, [surfaceWidth / 4, 0, greenWidth, surfaceHeight])

    # Generates the moon, which is a symbol of progress
    moonRadius = surfaceHeight * 4 / 10
    circleOffset = surfaceHeight / 10
    xPosMoon = (surfaceWidth / 4) + (greenWidth / 2)
    yPosMoon = (surfaceHeight / 2)
    xOffset = xPosMoon + circleOffset
    yOffset = yPosMoon - circleOffset
    pygame.draw.circle(surface, white, (xPosMoon, yPosMoon), moonRadius)
    pygame.draw.circle(surface, green, (xOffset, yOffset), moonRadius * 0.9)

    # Generates the star, which is represents knowledge and light
    pygame.draw.polygon(surface, white, rotatedStarPlotter(xOffset * 1.1, yOffset * 5 / 6, moonRadius * 0.3, math.radians(45)))

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