import pygame
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 800
dis_height = 600

# Initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by ChatGPT')

clock = pygame.time.Clock()
snake_block = 20  # Increase block size
snake_speed = 10  # Adjust speed for larger blocks

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def draw_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
    poison_foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    poison_foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    direction = 'STOP'  # Track current direction
    last_direction = 'STOP'

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            draw_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and last_direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and last_direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and last_direction != 'UP':
                    direction = 'DOWN'

        if direction == 'LEFT':
            x1_change = -snake_block
            y1_change = 0
        elif direction == 'RIGHT':
            x1_change = snake_block
            y1_change = 0
        elif direction == 'UP':
            y1_change = -snake_block
            x1_change = 0
        elif direction == 'DOWN':
            y1_change = snake_block
            x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Screen wrapping logic
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width - snake_block
        if y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - snake_block

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, red, [poison_foodx, poison_foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake's head collides with the body
        for x in snake_List[:-1]:
            if x == snake_Head:
                Length_of_snake -= 1  # Cut the length of the snake
                if Length_of_snake < 1:
                    game_over = True  # Game over if snake length is less than 1
                    game_close = True

        our_snake(snake_block, snake_List)
        draw_score(Length_of_snake - 1)

        pygame.display.update()

        # Check for collision with regular food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        # Check for collision with poisonous food
        if x1 == poison_foodx and y1 == poison_foody:
            poison_foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            poison_foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake -= 2
            if Length_of_snake < 1:
                game_over = True  # Game over if snake length is less than 1
                game_close = True

        last_direction = direction

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

