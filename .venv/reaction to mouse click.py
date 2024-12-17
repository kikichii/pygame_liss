import pygame
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = [(0, 0, 0), (255, 0, 0), (0, 0, 255)]
        self.current_color = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                color = self.colors[self.board[y][x]]
                pygame.draw.rect(screen, (color), (x * self.cell_size + self.left,
                                                 y * self.cell_size + self.top, self.cell_size,
                                                 self.cell_size))

    def render1(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size + self.left,
                                                           y * self.cell_size + self.top, self.cell_size,
                                                           self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if (x >= 0 and x < self.width) and (y >= 0 and y < self.height):
            return x, y
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords is not None:
            x, y = cell_coords
            self.board[y][x] = (self.board[y][x] + 1) % len(self.colors)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        board.render1(screen)
        pygame.display.flip()
    pygame.quit()