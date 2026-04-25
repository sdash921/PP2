import pygame
import datetime
import os

pygame.init()
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

# Setup paths
base_path = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(base_path, 'images')

def load_img(name):
    return pygame.image.load(os.path.join(images_path, name)).convert_alpha()

# Load assets
image_surface = load_img('clock.png')
mickey        = load_img('mUmrP.png')
hand_l        = load_img('hand_left_centered.png')
hand_r        = load_img('hand_right_centered.png')

CENTER = (WIDTH // 2, HEIGHT // 2)

# Scale
resized_clock = pygame.transform.scale(image_surface, (800, 600))
res_mickey    = pygame.transform.scale(mickey, (350, 350))
# If the hands are still too big/small, change these numbers
hand_l_base   = pygame.transform.scale(hand_l, (120, 120)) 
hand_r_base   = pygame.transform.scale(hand_r, (100, 100))

# HELPER FUNCTION: This fixes the "wobbly" rotation
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=topleft).center)
    surf.blit(rotated_image, new_rect)

clock_engine = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    m = now.minute
    s = now.second

    # Angles
    minutes_angle = -(m * 6 + s * 0.1)
    seconds_angle = -(s * 6) 

    screen.fill(WHITE)

    # Draw Clock Face
    face_rect = resized_clock.get_rect(center=CENTER)
    screen.blit(resized_clock, face_rect)

    # Draw Mickey
    mic_rect = res_mickey.get_rect(center=CENTER)
    screen.blit(res_mickey, mic_rect)

    # Draw Hands using the helper function to keep them perfectly centered
    blit_rotate_center(screen, hand_l_base, CENTER, minutes_angle)
    blit_rotate_center(screen, hand_r_base, CENTER, seconds_angle)

    pygame.display.flip()
    clock_engine.tick(60)  

pygame.quit()