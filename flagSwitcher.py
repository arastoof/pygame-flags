import pygame
import os
import importlib.util

def importFlags(directory):
    flags = []
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != "flagSwitcher.py":
            moduleName = filename[:-3]
            modulePath = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location(moduleName, modulePath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            flags.append(module.drawFlag)
    return flags

pygame.init()

def main():
    # Screen resolution
    screenWidth = 1280
    screenHeight = 720
    smoothFactor = 4
    smoothing = True
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    flags = importFlags('flags')
    current_flag = 0
    running = True

    surface = flags[current_flag](screenWidth * smoothFactor, screenHeight * smoothFactor)

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_flag = (current_flag + 1) % len(flags)
                elif event.key == pygame.K_LEFT:
                    current_flag = (current_flag - 1) % len(flags)
                elif event.key == pygame.K_a:
                    smoothing = not smoothing
                    if smoothing:
                        smoothFactor = 4
                    else:
                        smoothFactor = 1
                surface = flags[current_flag](screenWidth * smoothFactor, screenHeight * smoothFactor)    

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()