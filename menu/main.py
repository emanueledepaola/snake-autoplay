# importing libraries
import pygame
# import pygame_menu
import asyncio

# importing project modules
import game
import snake
import fruit
import wall
import autopilot

# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Setup fruit
fruit.init()

# def menu_game():
# 	# Create a menu object
# 	menu = pygame_menu.Menu('SNAKE', game.window_x, game.window_y, theme=game.theme)
	
# 	# Adding features to the menu
# 	menu.add.button('Play', play_game)
# 	menu.add.selector('Periodic boundaries: ', [('Yes', True), ('No', False)], onchange=game.set_periodic)
# 	menu.add.selector('Random walls: ', [('Yes', True), ('No', False)], onchange=game.set_walls)
# 	menu.add.text_input('Name: ')
# 	menu.add.button('Quit', pygame_menu.events.EXIT)
# 	while True:
# 		events = pygame.event.get()
# 		for event in events:
# 			if event.type == pygame.QUIT:
# 				exit()
				
# 		if menu.is_enabled():
# 			menu.update(events)
# 			menu.draw(game_window)
		
# 		pygame.display.update()

def menu_game(screen):
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

		# Refresh menu
		game.update(screen)

def play_game(auto_pilot, screen):

	# Main Function
	while True:

		global change_to, direction, fruit_position, fruit_spawn, score
		# auto_pilot = True
	
		if auto_pilot is False:
			# handling key events
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						change_to = 'UP'
					if event.key == pygame.K_DOWN:
						change_to = 'DOWN'
					if event.key == pygame.K_LEFT:
						change_to = 'LEFT'
					if event.key == pygame.K_RIGHT:
						change_to = 'RIGHT'
		else:
			# asking to the autopilot routine!
			change_to = autopilot.find_path(direction)	

		# We don't want the new direction to be the
		# opposite of the current one
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'

		# Moving the snake
		if direction == 'UP':
			snake.position[1] -= 10
		if direction == 'DOWN':
			snake.position[1] += 10
		if direction == 'LEFT':
			snake.position[0] -= 10
		if direction == 'RIGHT':
			snake.position[0] += 10

		# Check if the fruit was eaten #TODO
		snake.move()

		if fruit.spawn == False:
			fruit.spawn = True
			wall.new_wall()
			fruit.position = fruit.locate()
			for block in wall.body:
				while fruit.position == block:
					fruit.position = fruit.locate()
			
		# Fill the game background
		game.fill(screen)
		
		# Move the snake body
		snake.draw(screen)

		# Spawn the fruit randomly
		fruit.draw(screen)
		
		# Draw the walls
		wall.draw(screen)

		# Periodic boundary conditions
		if snake.position[0] < 0:
			snake.position[0] = game.window_x-10
		if snake.position[0] > game.window_x-10:
			snake.position[0] = 0
		if snake.position[1] < 0:
			snake.position[1] = game.window_y-10
		if snake.position[1] > game.window_y-10:
			snake.position[1] = 0

		# Touching the snake body
		# Implement game over conditions if the snake touches itself #TODO
		for block in snake.body[1:]:
			if snake.position == block:
				game.game_over(screen)
		
		# Touching the wall, game over condition
		for block in wall.body:
			if snake.position == block:
				game.game_over(screen)

		# Refresh game
		game.update(screen)


async def main():

	# menu = True

	# # Initialising game
	# screen = game.init()
	# # game_window = game.init()

	# # while True:
	# 	# if menu:
	# 	# 	auto = menu_game(game_window)
	# 	# 	menu = False
	# 	# else:
	# 	# 	menu = play_game(auto, game_window)
	# 	# await asyncio.sleep(0)

	# 	# Set up colors
	# black = (0, 0, 0)
	# green = (0, 255, 0)
	# bright_green = (0, 200, 0)

	# # Set up font
	# font = pygame.font.SysFont(None, 50)

	# # Set up buttons
	# auto_button = pygame.Rect(100, 100, 200, 50)
	# play_button = pygame.Rect(100, 200, 200, 50)
	# quit_button = pygame.Rect(100, 300, 200, 50)

	# while True:
	# 	for event in pygame.event.get():
	# 		if event.type == pygame.QUIT:
	# 			pygame.quit()
	# 			quit()

	# 	# Draw buttons
	# 	pygame.draw.rect(screen, green, auto_button)
	# 	pygame.draw.rect(screen, green, play_button)
	# 	pygame.draw.rect(screen, green, quit_button)

	# 	# Draw button labels
	# 	auto_label = font.render("Auto", True, black)
	# 	play_label = font.render("Play", True, black)
	# 	quit_label = font.render("Quit", True, black)
	# 	screen.blit(auto_label, (auto_button.x + 60, auto_button.y + 10))
	# 	screen.blit(play_label, (play_button.x + 60, play_button.y + 10))
	# 	screen.blit(quit_label, (quit_button.x + 60, quit_button.y + 10))

	# 	# Check if buttons are clicked
	# 	mouse = pygame.mouse.get_pos()
	# 	if auto_button.collidepoint(mouse):
	# 		pygame.draw.rect(screen, bright_green, auto_button)
	# 		if pygame.mouse.get_pressed()[0]:
	# 			return True
	# 	if play_button.collidepoint(mouse):
	# 		pygame.draw.rect(screen, bright_green, play_button)
	# 		if pygame.mouse.get_pressed()[0]:
	# 			return False
	# 	if quit_button.collidepoint(mouse):
	# 		pygame.draw.rect(screen, bright_green, quit_button)
	# 		if pygame.mouse.get_pressed()[0]:
	# 			pygame.quit()
	# 			quit()

	# 	# Refresh menu
	# 	game.update(screen)

	# Initialising game
	pygame.init()

	# Set up colors
	black        = (  0,   0, 0)
	green        = (  0, 255, 0)
	red          = (255,   0, 0)
	bright_green = (  0, 100, 0)
	bright_red   = (100,   0, 0)

	# Set up font
	font = pygame.font.SysFont(None, 50)

	# Window size
	window_x = 720 ; window_y = 480
	screen = pygame.display.set_mode((window_x,	window_y))
	# Set up buttons
	auto_button = pygame.Rect(400, 100, 200, 50)
	play_button = pygame.Rect(400, 200, 200, 50)
	quit_button = pygame.Rect(400, 300, 200, 50)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# Draw buttons
		pygame.draw.rect(screen, green, auto_button)
		pygame.draw.rect(screen, green, play_button)
		pygame.draw.rect(screen, red,   quit_button)

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
			screen.blit(auto_label, (auto_button.x + 60, auto_button.y + 10))
			if pygame.mouse.get_pressed()[0]:
				print("AUTO")
				# return True
		if play_button.collidepoint(mouse):
			pygame.draw.rect(screen, bright_green, play_button)
			screen.blit(play_label, (play_button.x + 60, play_button.y + 10))
			if pygame.mouse.get_pressed()[0]:
				print("PLAY")
				# return False
		if quit_button.collidepoint(mouse):
			pygame.draw.rect(screen, bright_red, quit_button)
			screen.blit(quit_label, (quit_button.x + 60, quit_button.y + 10))
			if pygame.mouse.get_pressed()[0]:
				pygame.quit()
				quit()

		pygame.display.update()
		await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())