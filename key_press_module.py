import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display (required for handling events in pygame)
screen = pygame.display.set_mode((50, 50))
pygame.display.set_caption("Key Press Reader")


# Main loop
running = True
while running:
    # Process events
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:  # Check for key press
            pressed_key = pygame.key.name(event.key)  # Output the key pressed

            if pressed_key == 'up':
                print('FORWARD')
            elif pressed_key == 'down':
                print('REVERSE')
            elif pressed_key == 'left':
                print('LEFT')
            elif pressed_key == 'right':
                print('RIGHT')
            elif pressed_key == 'space':
                print('TERMINATING SESSION')
                sys.exit()
            else:
                print(f'{pressed_key}: NO DEFINED ACTION')
                
        elif event.type == pygame.KEYUP:
            print('NO PRESSED KEY')
            
        if event.type == pygame.QUIT:  # Exit condition
            running = False

# Quit pygame
pygame.quit()
sys.exit()
