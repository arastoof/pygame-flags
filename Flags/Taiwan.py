import pygame
import math

def trianglePlotter(x, y, size):
    trianglePoints = []

    trianglePoints.append((x, y - size / 2))
    trianglePoints.append((x + size / 4, y + size / 2))
    trianglePoints.append((x - size / 4, y + size / 2))

    return trianglePoints

# Screen resolution
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define colours
red = (254, 0, 0) 
white = (255, 255, 255)
blue = (0, 0, 149) # Blue represents freedom and democracy

def drawFlag():
    # The red field represents the sacrifice of the people to establish the Republic of China
    screen.fill(red)

    canton = (screenWidth / 2, screenHeight / 2)
    pygame.draw.rect(screen, blue, [0, 0, canton[0], canton[1]])

    # The white sun symbolises equality and the people's livelihoods
    circleRadius = canton[1] / 4
    pygame.draw.circle(screen, white, (canton[0] / 2, canton[1] / 2), circleRadius)

    # The 12 rays of the sun represent the 12 months of the year and the 12 traditional Chinese hours
    triangleOffset = circleRadius / 10
    triangleSize = circleRadius / 2
    for counter in range(0, 12):
        angle = math.radians(30) * counter
        xPoint = 0
        yPoint = - circleRadius - triangleSize / 2 - triangleOffset
        trianglePoints = []
        for (x, y) in trianglePlotter(xPoint, yPoint, triangleSize):
            newX = x * math.cos(angle) - y * math.sin(angle)
            newY = y * math.cos(angle) + x * math.sin(angle)
            trianglePoints.append((newX + canton[0] / 2, newY + canton[1] / 2))
        pygame.draw.polygon(screen, white, trianglePoints)

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