"""
Snake game with pygame
Requires: pip install pygame
Run: python snake_pygame.py
"""
import pygame, random, sys

WIDTH, HEIGHT = 600, 400
CELL = 20

def draw_rect(screen, color, x, y, w, h):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    snake = [(WIDTH//2, HEIGHT//2)]
    direction = (CELL, 0)
    food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    speed = 10
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction!=(0,CELL): direction = (0,-CELL)
                if event.key in (pygame.K_DOWN, pygame.K_s) and direction!=(0,-CELL): direction = (0,CELL)
                if event.key in (pygame.K_LEFT, pygame.K_a) and direction!=(CELL,0): direction = (-CELL,0)
                if event.key in (pygame.K_RIGHT, pygame.K_d) and direction!=(-CELL,0): direction = (CELL,0)

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # collisions
        if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake):
            msg = font.render("Game Over! Press R to Restart or Q to Quit", True, (255,255,255))
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 20))
            pygame.display.flip()
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT: pygame.quit(); sys.exit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_q: pygame.quit(); sys.exit()
                        if e.key == pygame.K_r:
                            main()
                clock.tick(10)

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            speed = min(25, 10 + score//2)
            while True:
                food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
                if food not in snake: break
        else:
            snake.pop()

        screen.fill((0,0,0))
        for x,y in snake:
            draw_rect(screen, (0,200,0), x, y, CELL-2, CELL-2)
        draw_rect(screen, (200,0,0), food[0], food[1], CELL-2, CELL-2)
        score_srf = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_srf, (10,10))
        pygame.display.flip()
        clock.tick(speed)

if __name__ == "__main__":
    main()
