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
red = (227, 10, 23) # Red represents the bloodshed of soldiers fighting for Turkey's independence 
white = (255, 255, 255) # White represents the diversity of Turkish cultures

def drawFlag():
    surfaceHeight = screenHeight * smoothFactor
    surfaceWidth = screenWidth * smoothFactor
    surface = pygame.Surface((surfaceWidth, surfaceHeight))

    # The Turkish flag has no official meaning, but there are many theories
    surface.fill(red)

    # According to legend, the image of the Turkish flag was formed through the reflection of the moon and the star in the blood of martyrs
    moonRadius = surfaceHeight / 3
    crescentRadius = surfaceHeight * 4 / 15
    pygame.draw.circle(surface, white, (surfaceWidth / 2 - moonRadius, surfaceHeight / 2), moonRadius)
    pygame.draw.circle(surface, red, (surfaceWidth / 2 - (crescentRadius * 0.9), surfaceHeight / 2), crescentRadius)

    starSize = surfaceHeight / 7
    pygame.draw.polygon(surface, white, rotatedStarPlotter(surfaceWidth / 2 + starSize / 2, surfaceHeight / 2, starSize, math.radians(50)))

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