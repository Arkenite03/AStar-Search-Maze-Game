import pygame
from Classes import spot, color, algorithm

WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Visualizer")


menu_width = 500
MENU = pygame.display.set_mode((menu_width, menu_width))

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			s = spot.Spot(i, j, gap, rows)
			grid[i].append(s)

	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, color.Color.GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, color.Color.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(color.Color.WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col



	

def make_menu():

	run = True
	pygame.font.init()
	bigfont = pygame.font.SysFont('Corbel',45)
	smallfont = pygame.font.SysFont('Corbel',35)
	insfont = pygame.font.SysFont('Corbel',25)
	t1 = smallfont.render('Draw Maze' , True , color.Color.YELLOW)
	t2 = smallfont.render('Get Maze' , True , color.Color.BLUE)
	t3 = smallfont.render('Quit' , True , color.Color.RED)
	t4 = insfont.render('Press c To Get Back To Main Menu' , True , color.Color.RED)
	head = bigfont.render('A* Pathfinding Visualizer' , True , color.Color.BLUE)
	name_1 = insfont.render('By - Vishwa Sharma' , True , color.Color.BLUE)
	name_2 = insfont.render('     Aman Thakur' , True , color.Color.BLUE)

	while(run):
		
		MENU.fill(color.Color.WHITE)

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				x, y = pos

				if(y >= 150 and y <= 200 and x >= 150 and x<= 350):

					# print("clicked")
					main(WIN, WIDTH,True)

				elif(y >= 250 and y <= 300 and x >= 150 and x<= 350):
					main(WIN, WIDTH, False)

				elif(y >= 350 and y <= 400 and x >= 150 and x<= 350):
					run = False


				# print(pos)

		pygame.draw.ellipse(MENU, color.Color.TORQUISE, (150, 150, 200, 50))
		MENU.blit(t1 , (175,160))

		pygame.draw.ellipse(MENU, color.Color.GREEN, (150, 250, 200, 50))
		MENU.blit(t2 , (190,260))

		pygame.draw.ellipse(MENU, color.Color.ORANGE, (150, 350, 200, 50))
		MENU.blit(t3 , (220,360))
		MENU.blit(t4 , (120,420))
		MENU.blit(head , (30,50))
		#MENU.blit(name_1 , (300,460))
		#MENU.blit(name_2 , (340,480))

		pygame.display.update()





def main(win, width, flag):
	ROWS = 50
	grid = make_grid(ROWS, width)

	if(not flag):

		l = {(31, 6), (20, 25), (16, 9), (6, 28), (32, 44), (31, 44), (7, 25), (29, 44), (22, 19), (42, 20), (23, 26), (16, 47), (36, 34), (17, 46), (13, 32), (11, 48), (9, 0), (18, 45), (14, 31), (10, 7), (49, 32), (39, 45), (37, 13), (35, 21), (0, 17), (24, 14), (38, 2), (36, 22), (14, 43), (29, 17), (25, 49), (49, 28), (15, 34), (4, 5), (28, 10), (0, 45), (31, 15), (16, 0), (6, 23), (8, 38), (7, 22), (22, 42), (32, 35), (31, 21), (9, 39), (33, 34), (18, 10), (7, 44), (41, 34), (37, 44), (9, 9), (23, 9), (10, 14), (8, 18), (9, 19), (38, 5), (39, 0), (37, 16), (0, 14), (27, 6), (49, 21), (15, 43), (19, 44), (26, 49), (0, 36), (5, 1), (29, 4), (20, 47), (47, 49), (30, 27), (2, 38), (8, 45), (31, 18), (46, 30), (22, 45), (6, 32), (7, 37), (32, 16), (46, 0), (11, 46), (10, 9), (43, 45), (13, 44), (14, 19), (10, 19), (25, 25), (26, 30), (0, 5), (38, 22), (12, 29), (27, 31), (49, 14), (15, 48), (29, 29), (25, 37), (26, 34), (32, 49), (6, 27), (21, 17), (28, 44), (7, 34), (41, 44), (31, 33), (11, 39), (35, 34), (33, 22), (16, 42), (12, 32), (34, 21), (8, 0), (32, 13), (17, 43), (18, 48), (14, 26), (49, 45), (15, 19), (37, 2), (11, 19), (0, 28), (24, 9), (38, 9), (49, 7), (13, 25), (29, 22), (27, 10), (49, 25), (30, 5), (26, 45), (0, 40), (31, 0), (6, 18), (21, 26), (4, 38), (17, 10), (7, 27), (22, 17), (5, 39), (42, 18), (30, 49), (36, 44), (34, 44), (17, 44), (7, 49), (32, 4), (37, 33), (35, 49), (9, 6), (18, 43), (14, 29), (10, 5), (43, 49), (49, 38), (15, 24), (37, 11), (0, 19), (24, 16), (38, 0), (12, 19), (13, 18), (37, 21), (0, 9), (49, 18), (15, 44), (4, 7), (28, 4), (0, 47), (31, 9), (5, 6), (6, 21), (30, 22), (32, 37), (23, 45), (16, 24), (45, 0), (10, 34), (34, 39), (11, 43), (18, 34), (9, 15), (23, 11), (38, 33), (12, 44), (36, 49), (10, 12), (13, 49), (44, 49), (9, 17), (49, 49), (14, 48), (49, 11), (19, 46), (0, 38), (1, 39), (25, 34), (30, 25), (21, 44), (23, 42), (6, 38), (21, 22), (40, 44), (7, 39), (32, 18), (23, 0), (12, 43), (17, 48), (32, 8), (13, 42), (10, 17), (25, 31), (49, 42), (37, 7), (0, 7), (38, 20), (12, 31), (27, 17), (49, 12), (13, 30), (5, 8), (20, 48), (29, 27), (30, 0), (26, 32), (31, 5), (27, 45), (42, 15), (16, 22), (6, 25), (41, 18), (7, 28), (16, 44), (23, 25), (12, 34), (36, 39), (32, 15), (13, 35), (37, 38), (9, 3), (18, 46), (14, 24), (49, 35), (37, 0), (0, 30), (24, 11), (38, 15), (12, 22), (49, 5), (13, 23), (28, 17), (24, 49), (48, 30), (1, 49), (25, 44), (49, 31), (0, 42), (3, 39), (21, 24), (30, 45), (8, 35), (7, 21), (22, 23), (44, 0), (9, 34), (42, 16), (33, 45), (35, 45), (16, 35), (17, 34), (32, 6), (22, 9), (9, 4), (23, 12), (38, 44), (45, 31), (10, 3), (49, 36), (15, 26), (37, 9), (0, 21), (24, 18), (38, 6), (15, 0), (37, 19), (0, 11), (14, 47), (27, 5), (49, 16), (15, 46), (4, 1), (28, 6), (2, 49), (19, 43), (0, 33), (31, 11), (46, 49), (5, 4), (20, 44), (23, 49), (8, 42), (7, 18), (31, 17), (32, 39), (29, 33), (20, 10), (9, 43), (33, 38), (16, 26), (22, 0), (11, 45), (9, 13), (16, 48), (12, 46), (10, 10), (13, 47), (24, 25), (0, 2), (38, 19), (49, 9), (4, 8), (19, 48), (29, 0), (20, 43), (25, 32), (21, 42), (30, 31), (6, 36), (21, 20), (30, 33), (10, 43), (7, 33), (5, 49), (11, 34), (35, 33), (42, 44), (34, 22), (41, 49), (32, 10), (14, 23), (36, 0), (49, 40), (15, 22), (37, 5), (0, 25), (38, 10), (12, 25), (49, 2), (13, 28), (24, 44), (14, 35), (29, 25), (27, 9), (40, 15), (7, 0), (31, 7), (43, 0), (41, 16), (22, 18), (31, 45), (29, 45), (35, 38), (16, 46), (6, 49), (36, 33), (17, 47), (13, 33), (11, 49), (9, 1), (42, 49), (14, 30), (18, 44), (10, 6), (49, 33), (37, 14), (0, 16), (24, 13), (14, 0), (38, 13), (36, 21), (14, 42), (29, 18), (49, 29), (15, 35), (4, 4), (28, 9), (0, 44), (31, 12), (6, 22), (19, 10), (7, 23), (32, 34), (22, 21), (33, 35), (23, 16), (40, 34), (21, 0), (10, 39), (7, 45), (37, 45), (9, 10), (23, 14), (38, 34), (12, 49), (45, 29), (10, 1), (0, 23), (38, 4), (25, 17), (37, 17), (0, 13), (14, 45), (27, 7), (49, 22), (4, 3), (28, 0), (19, 45), (0, 35), (5, 2), (20, 46), (29, 5), (30, 26), (8, 44), (22, 44), (33, 36), (6, 35), (21, 9), (17, 25), (7, 42), (11, 47), (10, 8), (13, 45), (35, 0), (14, 18), (10, 18), (25, 26), (26, 17), (0, 4), (38, 17), (12, 28), (49, 15), (15, 49), (28, 31), (29, 30), (6, 0), (30, 29), (26, 37), (46, 32), (42, 0), (6, 26), (21, 18), (40, 16), (7, 35), (32, 22), (41, 45), (22, 25), (18, 25), (32, 12), (49, 46), (13, 0), (37, 3), (0, 27), (38, 8), (12, 27), (49, 0), (13, 26), (0, 49), (14, 33), (29, 23), (49, 26), (21, 49), (30, 4), (26, 44), (29, 49), (20, 26), (16, 10), (7, 24), (32, 45), (20, 0), (17, 45), (22, 10), (37, 34), (9, 7), (18, 42), (14, 28), (10, 4), (49, 39), (39, 44), (15, 25), (37, 12), (0, 18), (24, 15), (38, 3), (12, 18), (13, 19), (37, 22), (0, 8), (27, 0), (49, 19), (15, 45), (4, 6), (0, 46), (22, 49), (5, 7), (31, 14), (6, 20), (30, 17), (8, 39), (32, 36), (22, 43), (3, 49), (9, 38), (33, 33), (23, 18), (34, 38), (41, 33), (9, 8), (10, 15), (34, 0), (8, 19), (9, 18), (0, 15), (49, 20), (15, 42), (19, 47), (0, 37), (5, 0), (25, 35), (30, 24), (21, 45), (2, 39), (41, 0), (46, 31), (23, 43), (47, 30), (21, 23), (4, 49), (30, 34), (34, 33), (6, 33), (7, 36), (32, 17), (9, 49), (42, 33), (40, 49), (12, 42), (43, 44), (17, 49), (39, 34), (13, 43), (12, 0), (10, 16), (49, 43), (26, 31), (0, 6), (48, 0), (12, 30), (27, 30), (49, 13), (13, 31), (5, 9), (29, 28), (25, 36), (19, 26), (26, 35), (6, 24), (19, 0), (28, 45), (41, 19), (11, 38), (33, 21), (16, 43), (12, 33), (36, 38), (10, 49), (17, 42), (32, 14), (37, 39), (18, 49), (14, 27), (49, 44), (39, 49), (15, 18), (37, 1), (11, 18), (0, 29), (24, 10), (38, 14), (49, 6), (39, 15), (13, 24), (26, 0), (48, 29), (29, 21), (25, 45), (49, 24), (0, 41), (6, 19), (21, 25), (30, 44), (19, 9), (4, 39), (8, 34), (17, 9), (41, 20), (5, 38), (7, 26), (22, 22), (9, 35), (42, 19), (16, 34), (36, 45), (34, 45), (17, 35), (32, 5), (9, 5), (33, 0), (23, 13), (45, 32), (10, 2), (49, 37), (37, 10), (35, 22), (0, 20), (24, 17), (38, 1), (37, 20), (0, 10), (14, 46), (49, 17), (15, 47), (4, 0), (28, 5), (0, 32), (31, 8), (5, 5), (40, 0), (30, 23), (7, 19), (31, 22), (32, 38), (20, 9), (29, 34), (18, 9), (33, 39), (23, 44), (16, 25), (10, 35), (11, 42), (9, 14), (18, 35), (23, 10), (12, 45), (10, 13), (13, 48), (11, 0), (9, 16), (49, 48), (26, 18), (0, 1), (14, 49), (38, 18), (49, 10), (19, 49), (0, 39), (20, 42), (27, 49), (1, 38), (25, 33), (30, 30), (21, 43), (46, 29), (18, 0), (6, 39), (21, 21), (30, 32), (10, 42), (40, 45), (7, 38), (22, 26), (11, 35), (18, 26), (32, 9), (14, 22), (25, 30), (49, 41), (15, 23), (37, 6), (0, 24), (38, 21), (12, 24), (25, 0), (49, 3), (39, 16), (13, 29), (14, 34), (20, 49), (29, 26), (28, 49), (26, 33), (41, 15), (31, 4), (27, 44), (33, 49), (16, 23), (41, 17), (31, 34), (35, 39), (16, 45), (12, 35), (32, 0), (13, 34), (9, 2), (18, 47), (14, 25), (49, 34), (37, 15), (0, 31), (24, 12), (38, 12), (12, 23), (49, 4), (13, 22), (28, 18), (3, 0), (49, 30), (28, 8), (0, 43), (31, 13), (3, 38), (30, 18), (34, 49), (32, 33), (7, 20), (22, 20), (35, 44), (33, 44), (23, 17), (42, 17), (40, 33), (10, 38), (32, 7), (31, 49), (9, 11), (23, 15), (38, 45), (12, 48), (45, 30), (10, 0), (37, 8), (0, 22), (38, 7), (25, 18), (37, 18), (0, 12), (14, 44), (27, 4), (49, 23), (4, 2), (28, 7), (19, 42), (0, 34), (31, 10), (5, 3), (20, 45), (30, 21), (17, 0), (8, 43), (31, 16), (29, 32), (9, 42), (33, 37), (47, 29), (21, 10), (6, 34), (34, 34), (8, 49), (17, 26), (7, 43), (11, 44), (9, 12), (42, 34), (16, 49), (12, 47), (10, 11), (39, 33), (13, 46), (37, 49), (24, 26), (45, 49), (0, 3), (24, 0), (38, 16), (49, 8), (4, 9), (28, 30), (29, 31), (30, 28), (19, 25), (26, 36), (6, 37), (21, 19), (7, 32), (22, 24), (32, 21), (42, 45), (47, 0), (32, 11), (38, 49), (49, 47), (37, 4), (0, 26), (38, 11), (12, 26), (27, 18), (49, 1), (13, 27), (2, 0), (0, 48), (24, 45), (14, 32), (29, 24), (27, 8), (49, 27)}

		for i in l:
			sp = grid[i[0]][i[1]]
			sp.make_barrier()


	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					k = algorithm.Algorithm()
					k.algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					make_menu()

	pygame.quit()


make_menu()
