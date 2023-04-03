import pygame, random, sys, time

screensize = (800, 600)
screen = pygame.display.set_mode((screensize[0], screensize[1]))
pygame.display.set_caption("Conway's Game of Life simulation")

while True:
    cells = []
    cell_size = 10
    density = 40
    iterations = 6

    for y in range(int(screensize[1] / cell_size)):
        for x in range(int(screensize[0] / cell_size)):
            cells.append(x * cell_size)
            cells.append(y * cell_size)
            if random.randint(1, 100) > density:
                cells.append(255)
            else:
                cells.append(0)

    for i in range(iterations):
        screen.fill((255, 255, 255))

        idx = 0
        for i in range(int(len(cells) / 3)):
            cell = pygame.Surface((cell_size, cell_size))
            cell.fill((cells[idx + 2], cells[idx + 2], cells[idx + 2]))
            screen.blit(cell, (cells[idx], cells[idx + 1]))
            idx += 3
        new_cells = []
        idx = 0
        for i in range(int(len(cells) / 3)):
            x = cells[idx]
            y = cells[idx + 1]
            t = cells[idx + 2]
            neighbors = 0

            try:
                if screen.get_at((x, y - cell_size))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1
            try:
                if screen.get_at((x + cell_size, y))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1

            try:
                if screen.get_at((x, y + cell_size))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1
            try:
                if screen.get_at((x - cell_size, y))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1

            try:
                if screen.get_at((x - cell_size, y - cell_size))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1
            try:
                if screen.get_at((x + cell_size, y - cell_size))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1
            try:
                if screen.get_at((x - cell_size, y + cell_size))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1
            try:
                if screen.get_at((x + cell_size, y + cell_size))[0] == 0:
                    neighbors += 1
            except:
                neighbors += 1

            if neighbors > 3:
                t = 0
            else:
                t = 255
                
            new_cells.append(x)
            new_cells.append(y)
            new_cells.append(t)
            idx += 3

        idx = 0
        for i in range(int(len(cells) / 3)):
            cells[idx] = new_cells[idx]
            cells[idx + 1] = new_cells[idx + 1]
            cells[idx + 2] = new_cells[idx + 2]
            idx += 3

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    time.sleep(2)
