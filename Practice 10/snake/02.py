import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 36)

# Game over text image rendered once for performance
image_game_over = font.render("Game Over", True, colorRED)
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
sc_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))

# Size of each grid cell in pixels
CELL = 30


def draw_grid():
    """Draws a grid over the playing area, skipping the top row (used for HUD)."""
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            if j != 0:  # Skip row 0 — reserved for score/level display
                pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)


class Point:
    """Represents a single grid coordinate (x, y)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


class Snake:
    """
    Manages the snake's body, movement, direction, score, level, and collision checks.
    """
    def __init__(self):
        # Snake starts with 3 segments going horizontally
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1   # Horizontal direction: 1 = right, -1 = left
        self.dy = 0   # Vertical direction:   1 = down,  -1 = up
        self.score = 0
        self.level = 1
        self.alive = True

    def change_direction(self, new_dx, new_dy):
        """
        Updates movement direction.
        Prevents the snake from reversing into itself (e.g. going right when moving left).
        """
        if new_dx == -self.dx and new_dy == -self.dy:
            return  # Ignore opposite direction input
        self.dx = new_dx
        self.dy = new_dy

    def move(self):
        """
        Moves the snake one step in the current direction.
        Each segment copies the position of the one in front of it,
        then the head advances by (dx, dy).
        Also checks for wall and self collisions.
        """
        # Shift each body segment forward (tail to neck)
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Move the head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # --- Wall collision checks ---
        if self.body[0].x > WIDTH // CELL - 1:
            print("Snake hit right wall!")
            self.alive = False
        if self.body[0].x < 0:
            print("Snake hit left wall!")
            self.alive = False
        if self.body[0].y > HEIGHT // CELL - 1:
            print("Snake hit bottom wall!")
            self.alive = False
        if self.body[0].y <= 0:
            # y == 0 is the HUD row, treat it as a wall
            print("Snake hit top wall!")
            self.alive = False

        # --- Self-collision check ---
        # Compare head position against every other body segment
        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                print("Snake hit itself!")
                self.alive = False
                break

    def draw(self):
        """Draws the snake. Head is dark green, body segments are green."""
        head = self.body[0]
        pygame.draw.rect(screen, colorDARK_GREEN, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorGREEN, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_food_collision(self, food):
        """
        Checks if the snake's head is on the food.
        If so: increments score, grows the snake, moves food, and updates level.
        Level increases every 3 foods eaten.
        """
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 1
            print(f"Food eaten! Score: {self.score}")

            # Grow snake by adding a new segment at the current tail position
            self.body.append(Point(self.body[-1].x, self.body[-1].y))

            # Reposition food somewhere safe
            food.generate_random_pos(self.body)

            # Level up every 3 foods
            self.level = 1 + self.score // 3
            print(f"Level: {self.level}")


class Food:
    """Represents the food item on the grid."""
    def __init__(self):
        self.pos = Point(9, 9)  # Default starting position

    def draw(self):
        """Draws the food as a red square."""
        pygame.draw.rect(screen, colorRED, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        """
        Picks a random grid position for food that:
        - Does not overlap any snake segment
        - Is not in row 0 (HUD row / top wall)
        """
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(1, HEIGHT // CELL - 1)  # y=0 is reserved for HUD
            # Only accept the position if it doesn't collide with the snake
            if not any(self.pos.x == s.x and self.pos.y == s.y for s in snake_body):
                break


# --- Game setup ---
FPS = 5          # Base frames per second (speed increases with level)
clock = pygame.time.Clock()

food = Food()
snake = Snake()
food.generate_random_pos(snake.body)  # Place food in a valid starting position

running = True

# --- Main game loop ---
while running:

    score = snake.score
    level = snake.level

    # --- Game Over screen ---
    if not snake.alive:
        # Build final score/level string
        result_str = f"Score: {score}   Level: {level}"
        sc_r = font.render(result_str, True, colorRED)

        screen.fill(colorBLACK)
        screen.blit(image_game_over, image_game_over_rect)  # "Game Over" text
        screen.blit(sc_r, sc_rect)                          # Score + level text
        pygame.display.flip()
        pygame.time.wait(10000)  # Show game over screen for 10 seconds then exit
        break

    # --- Render HUD (score and level) ---
    sc = font.render(f'Score: {score}', True, colorWHITE)
    lv = font.render(f'Level: {level}', True, colorWHITE)

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction(1, 0)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-1, 0)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, 1)
            elif event.key == pygame.K_UP:
                snake.change_direction(0, -1)

    # --- Drawing ---
    screen.fill(colorBLACK)
    draw_grid()

    # --- Update game state ---
    snake.move()
    snake.check_food_collision(food)

    snake.draw()
    food.draw()

    # Draw HUD on top
    screen.blit(sc, (2, 0))
    screen.blit(lv, (120, 0))

    pygame.display.flip()

    # Speed increases with level: each level adds 1 FPS on top of the base
    clock.tick(FPS + level)

pygame.quit()