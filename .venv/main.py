import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    running = True
    count = 0
    def draw(screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text = font.render(str(count), True, (100, 255, 100))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
    draw(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWHIDDEN:
                count += 1
                pygame.display.flip()
                print(count)
    pygame.quit()