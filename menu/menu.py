import pygame

def create_menu(screen):
    # Set up colors
    black = (0, 0, 0)
    green = (0, 255, 0)
    bright_green = (0, 200, 0)

    # Set up font
    font = pygame.font.SysFont(None, 50)

    # Set up buttons
    auto_button = pygame.Rect(100, 100, 200, 50)
    play_button = pygame.Rect(100, 200, 200, 50)
    quit_button = pygame.Rect(100, 300, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw buttons
        pygame.draw.rect(screen, green, auto_button)
        pygame.draw.rect(screen, green, play_button)
        pygame.draw.rect(screen, green, quit_button)

        # Draw button labels
        auto_label = font.render("Auto", True, black)
        play_label = font.render("Play", True, black)
        quit_label = font.render("Quit", True, black)
        screen.blit(auto_label, (auto_button.x + 60, auto_button.y + 10))
        screen.blit(play_label, (play_button.x + 60, play_button.y + 10))
        screen.blit(quit_label, (quit_button.x + 60, quit_button.y + 10))

        # Check if buttons are clicked
        mouse = pygame.mouse.get_pos()
        if auto_button.collidepoint(mouse):
            pygame.draw.rect(screen, bright_green, auto_button)
            if pygame.mouse.get_pressed()[0]:
                return True
        if play_button.collidepoint(mouse):
            pygame.draw.rect(screen, bright_green, play_button)
            if pygame.mouse.get_pressed()[0]:
                return False
        if quit_button.collidepoint(mouse):
            pygame.draw.rect(screen, bright_green, quit_button)
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                quit()

        pygame.display.update()
