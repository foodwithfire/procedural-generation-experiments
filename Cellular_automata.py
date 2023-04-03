import pygame, random, sys

screensize = (700, 1400)
screen = pygame.display.set_mode((screensize[0], screensize[1]))
pygame.display.set_caption("Conway's Game of Life simulation")

cells = []
density = 40
iterations = 6

for y in range(int(screensize[1] / 10)):
    for x in range(int(screensize[0] / 10)):
        cells.append(x*10)
        cells.append(y*10)
        if random.randint(1, 100) > density:
            cells.append(255)
        else:
            cells.append(0)

for i in range(iterations):
    screen.fill((255, 255, 255))

    idx = 0
    for i in range(int(len(cells) / 3)):
        cell = pygame.Surface((10, 10))
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
            if screen.get_at((x, y - 10))[0] == 0:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x + 10, y))[0] == 0:
                neighbors += 1
        except:
            neighbors += 1
            
        try:
            if screen.get_at((x, y + 10))[0] == 0:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x - 10, y))[0] == 0:
                neighbors += 1
        except: 
            neighbors += 1

        try:
            if screen.get_at((x - 10, y - 10))[0] == 0:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x + 10, y - 10))[0] == 0:
                neighbors += 1
        except: 
            neighbors += 1
        try:
            if screen.get_at((x - 10, y + 10))[0] == 0:
                neighbors += 1
        except:
            neighbors += 1
        try:
            if screen.get_at((x + 10, y + 10))[0] == 0:
                neighbors += 1
        except: 
            neighbors += 1
        
        if neighbors > 3:
            t = 0
        else:
            t = 255
        """
        cells[idx] = x
        cells[idx + 1] = y
        cells[idx + 2] = t
        """
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
            
while True:
    pygame.display.flip()
