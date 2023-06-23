import pygame
import random


pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake_speed = 10
snake_block = 10

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont('comicsansms', 35)


def your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_list):
    for coord in snake_list:
        pygame.draw.rect(dis, black, [coord[0], coord[1], snake_block, snake_block])


def message(message, color):
    mesg = font_style.render(message, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def game():
    game_over = False
    game_close = False

    x1 = dis_width / 2 
    y1 = dis_height / 2 

    x_change = 0
    y_change = 0

    snake_len = 1
    snake_list = []

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10

    while not game_over:
        while game_close:
            dis.fill(white)
            message('You Lose! Press Q-Quit or C-Play again', red)
            your_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                         game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <= 0:
            game_close = True

        x1 += x_change
        y1 += y_change
        dis.fill(blue)

        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            del snake_list[0]
        
        for coord in snake_list[:-1]:
            if coord == snake_head:
                game_close = True
        
        our_snake(snake_list)
        your_score(snake_len - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10
            snake_len += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()
