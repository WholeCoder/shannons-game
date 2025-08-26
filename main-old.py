# Example file showing a circle moving on screen
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Shannon")

# Load image
shannon_img = pygame.image.load("shannon.jpg")
shannon_rect = shannon_img.get_rect()
shannon_rect.center = (WIDTH // 2, HEIGHT // 2)

# Movement speed
speed = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shannon_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        shannon_rect.x += speed
    if keys[pygame.K_UP]:
        shannon_rect.y -= speed
    if keys[pygame.K_DOWN]:
        shannon_rect.y += speed

    # Keep image within screen bounds
    shannon_rect.x = max(0, min(WIDTH - shannon_rect.width, shannon_rect.x))
    shannon_rect.y = max(0, min(HEIGHT - shannon_rect.height, shannon_rect.y))

    screen.fill((30, 30, 30))  # Fill background
    screen.blit(shannon_img, shannon_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

