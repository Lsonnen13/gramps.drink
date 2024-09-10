import pygame
import random

pygame.init()

window_width = 750
window_height = 750
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
fps = 60

backround = pygame.image.load("8 bit backround.jpg")
backround = pygame.transform.scale(backround, (window_width, window_height))

blob_size = 50
blob_x = (window_width / 2) - (blob_size / 2)
blob_y = (window_height - blob_size) 
blob_speed = 2
blob_color = (0, 0 , 255)
drink_x = random.randint(0, 750)
drink_y = random.randint(0, 750)

happy_gramps = pygame.image.load("internetGrandpa.png")
happy_gramps = pygame.transform.scale(happy_gramps, (window_width, window_height))
win = False

guesses_left = 6

def draw_guesses(): pass

def check_distance():
    global guesses_left 
    gramps_vect = pygame.math.Vector2(blob_x + (blob_size / 2), blob_y + (blob_size / 2))
    drink_vect = pygame.math.Vector2(drink_x, drink_y)
    guesses_left -= 1
    return gramps_vect.distance_to(drink_vect)

def get_color(distance):
    if distance >= 300:
        return (255, 0, 0)
    if distance < 100: 
        return (0, 255, 0)
    if distance >= 200 and distance < 300:
        difference = 300 - distance
        return (255, int(2.55 * difference), 0)
    if distance >= 100 and distance < 200:
        difference = 200 - distance
        return (255 - int(2.55 * difference), 255, 0)


#main game loop
while guesses_left > 0:
    clock.tick(fps)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dist = check_distance()
                blob_color = get_color(dist)
                print("you have " + str(guesses_left) + " guesses left")
                if dist < 100:
                    win = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] == True:
        blob_y -= blob_speed
    if keys[pygame.K_a] == True:
        blob_x -= blob_speed
    if keys[pygame.K_s] == True:
        blob_y += blob_speed
    if keys[pygame.K_d] == True:
        blob_x += blob_speed
        
    window.fill((0,0,0))
    window.blit(backround, (0, 0))
    blob_rect = pygame.Rect(blob_x, blob_y, blob_size, blob_size)
    pygame.draw.rect(window, blob_color, blob_rect)
    if win == True:
        window.blit(happy_gramps, (0, 0))
    pygame.display.update()