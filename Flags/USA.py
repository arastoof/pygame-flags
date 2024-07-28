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
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (178, 34, 52) # Red represents hardiness and valour
white = (255, 255, 255) # White represents purity and innocence
blue = (60, 59, 110) # Blue represents vigilance, perseverance and justice

def drawFlag():
    # Generates the stripes. 13 stripes represent 13 original colonies.
    screen.fill(white)
    for counter in range (0, 13, 2):
        pygame.draw.rect(screen, red, [0, (screenHeight / 13) * counter, screenWidth, (screenHeight / 13)])
    
    canton = (screenWidth * 4 / 9, screenHeight * 7 / 13) # Size of the blue part
    pygame.draw.rect(screen, blue, [0, 0, canton[0], canton[1]]) # Draws the blue part of the flag

    # Draws the 50 stars on the blue part of the flag, representing each of the states in the canton
    starSize = (canton[1]) / 10
    for i in range (1, 10):
        if i % 2 != 0:
            for j in range (1, 12, 2):
                pygame.draw.polygon(screen, white, starPlotter(j * 1.22 * starSize, starSize * i, starSize / 2))
        if i % 2 == 0:
            for k in range (2, 12, 2):
                pygame.draw.polygon(screen, white, starPlotter(k * 1.22 * starSize, starSize * i, starSize / 2))

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