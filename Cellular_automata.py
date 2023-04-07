import pygame, random, sys, time

screensize = (1200, 800)
screen = pygame.display.set_mode((screensize[0], screensize[1]))
pygame.display.set_caption("procedural generation")

cells = []
cell_size = 5
density = 40
iterations = 6
for y in range(int(screensize[1] / cell_size)):
    for x in range(int(screensize[0] / cell_size)):
        if random.randint(1, 100) > density:
            cell_type = 1
        else:
            cell_type = 0
        cells.append((x * cell_size, y * cell_size, cell_type))

for i in range(iterations):
    screen.fill((0, 0, 0))

    for cell in cells:
        cell_rect = pygame.Surface((cell_size, cell_size))
        if cell[2] == 1:
            c = (34, 204, 0)
        else:
            c = (51, 187, 255)
        cell_rect.fill(c)
        screen.blit(cell_rect, (cell[0], cell[1]))

    new_cells = []
    for cell in cells:
        x = cell[0]
        y = cell[1]
        t = cell[2]
        neighbors = 0

        wall_color = 34

        try:
            if screen.get_at((x, y - cell_size))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x + cell_size, y))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x, y + cell_size))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x - cell_size, y))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x - cell_size, y - cell_size))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x + cell_size, y - cell_size))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x - cell_size, y + cell_size))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x + cell_size, y + cell_size))[0] == wall_color:
                neighbors += 1
        except:
            neighbors += 1
        if neighbors > 4:
            t = 1
        else:
            t = 0
        new_cells.append((x, y, t))

    cells = new_cells
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

print("Generation completed.")

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
