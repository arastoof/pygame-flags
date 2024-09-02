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

# Screen resolution
screenWidth = 1280
screenHeight = 720
smoothFactor = 4
smoothing = True
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (178, 34, 52) # Red represents hardiness and valour
white = (255, 255, 255) # White represents purity and innocence
blue = (60, 59, 110) # Blue represents vigilance, perseverance and justice

def drawFlag():
    surfaceHeight = screenHeight * smoothFactor
    surfaceWidth = screenWidth * smoothFactor
    surface = pygame.Surface((surfaceWidth, surfaceHeight))

    # Generates the stripes. 13 stripes represent 13 original colonies.
    surface.fill(white)
    for counter in range (0, 13, 2):
        pygame.draw.rect(surface, red, [0, (surfaceHeight / 13) * counter, surfaceWidth, (surfaceHeight / 13)])
    pygame.draw.rect(surface, red, [0, (surfaceHeight / 14) * 13, surfaceWidth, (surfaceHeight / 13)])
    
    canton = (surfaceWidth * 4 / 9, surfaceHeight * 7 / 13) # Size of the blue part
    pygame.draw.rect(surface, blue, [0, 0, canton[0], canton[1]]) # Draws the blue part of the flag

    # Draws the 50 stars on the blue part of the flag, representing each of the states in the canton
    starSize = (canton[1]) / 10
    for i in range (1, 10):
        if i % 2 != 0:
            for j in range (1, 12, 2):
                pygame.draw.polygon(surface, white, starPlotter(j * 1.22 * starSize, starSize * i, starSize / 2))
        if i % 2 == 0:
            for k in range (2, 12, 2):
                pygame.draw.polygon(surface, white, starPlotter(k * 1.22 * starSize, starSize * i, starSize / 2))
    
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