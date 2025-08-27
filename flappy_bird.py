"""
Flappy Bird clone (pygame)
Requires: pip install pygame
Run: python flappy_bird.py
"""
import pygame, sys, random
   
WIDTH, HEIGHT = 800, 600
PIPE_GAP = 150
PIPE_SPEED = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    bird = pygame.Rect(50, HEIGHT//2, 30, 30)
    gravity, jump = 0.5, -8
    vel = 0
    pipes = []
    score = 0
    frame = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                vel = jump

        vel += gravity
        bird.y += int(vel)

        if frame % 90 == 0:
            h = random.randint(100, HEIGHT-200)
            pipes.append(pygame.Rect(WIDTH, h-HEIGHT, 50, HEIGHT))
            pipes.append(pygame.Rect(WIDTH, h+PIPE_GAP, 50, HEIGHT))
        frame += 1

        for p in pipes:
            p.x -= PIPE_SPEED
        pipes = [p for p in pipes if p.right > 0]

        # collision
        if bird.y > HEIGHT or bird.y < 0 or any(bird.colliderect(p) for p in pipes):
            msg = font.render(f"Game Over! Score: {score}", True, (255,255,255))
            screen.blit(msg, (WIDTH//2-msg.get_width()//2, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        # scoring
        for p in pipes:
            if p.right == bird.left: score += 0.5

        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,0), bird)
        for p in pipes:
            pygame.draw.rect(screen, (0,200,0), p)
        txt = font.render(f"Score: {int(score)}", True, (255,255,255))
        screen.blit(txt, (10,10))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
