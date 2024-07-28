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
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (227, 10, 23) # Red represents the bloodshed of soldiers fighting for Turkey's independence 
white = (255, 255, 255) # White represents the diversity of Turkish cultures

def drawFlag():
    # The Turkish flag has no official meaning, but there are many theories
    screen.fill(red)

    # According to legend, the image of the Turkish flag was formed through the reflection of the moon and the star in the blood of martyrs
    moonRadius = screenHeight / 3
    crescentRadius = screenHeight * 4 / 15
    pygame.draw.circle(screen, white, (screenWidth / 2 - moonRadius, screenHeight / 2), moonRadius)
    pygame.draw.circle(screen, red, (screenWidth / 2 - (crescentRadius * 0.9), screenHeight / 2), crescentRadius)

    starSize = 100
    pygame.draw.polygon(screen, white, rotatedStarPlotter(screenWidth / 2 + starSize / 2, screenHeight / 2, starSize, math.radians(50)))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawFlag()
        pygame.display.update()

    pygame.quit()