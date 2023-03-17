# importing libraries
import pygame
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

# def get_keys():

# 	if game_mode == "auto":
# 		auto_pilot = True
# 	elif game_mode == "std":
# 		auto_pilot = False

# 	# handling key events
# 	for event in pygame.event.get():
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE:
# 				game_mode = None
# 				return
# 			if auto_pilot is False:
# 				if event.key == pygame.K_UP or pygame.K_w:
# 					change_to = 'UP'
# 				if event.key == pygame.K_DOWN or pygame.K_s:
# 					change_to = 'DOWN'
# 				if event.key == pygame.K_LEFT or pygame.K_a:
# 					change_to = 'LEFT'
# 				if event.key == pygame.K_RIGHT or pygame.K_d:
# 					change_to = 'RIGHT'
# 			else:
# 				# asking to the autopilot routine!
# 				change_to = autopilot.find_path(direction)
# 	return

async def main():

	# Initialising game
	screen = game.init()
	while True:

		global change_to, direction, fruit_position, fruit_spawn, score, game_mode

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		pygame.quit()
		# 		quit()

		if game_mode is None:
			game_mode = game.menu(screen)
		else:
			if game_mode == "auto":
				auto_pilot = True
			elif game_mode == "std":
				auto_pilot = False
			print(game_mode)
			print(auto_pilot)

			# handling key events
			# get_keys()
			if auto_pilot is False:
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:# or pygame.K_w:
							change_to = 'UP'
						if event.key == pygame.K_DOWN:# or pygame.K_s:
							change_to = 'DOWN'
						if event.key == pygame.K_LEFT:# or pygame.K_a:
							change_to = 'LEFT'
						if event.key == pygame.K_RIGHT:# or pygame.K_d:
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
		await asyncio.sleep(0)

game_mode = None

if __name__ == "__main__":
    asyncio.run(main())