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

screen = pygame.display.set_mode((1280, 720))
pygame.init()

def main():
    flags = importFlags('flags')
    current_flag = 0
    running = True

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_flag = (current_flag + 1) % len(flags)
                elif event.key == pygame.K_LEFT:
                    current_flag = (current_flag - 1) % len(flags)

        surface = flags[current_flag]()
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()