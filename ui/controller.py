import pygame
import redis

PI_IP = '192.168.0.11'
PORT=6379
display_width = 800
display_height = 600

pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mary controller')
r = redis.Redis(PI_IP, port=PORT, db=0) 
font = pygame.font.Font('freesansbold.ttf', 24)

while True:
    events = pygame.event.get()
    control_cmd_key = 'redis_control'
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('LEFT')
                r.set(control_cmd_key, 'LEFT')
            if event.key == pygame.K_RIGHT:
                print('RIGHT')
                r.set(control_cmd_key, 'RIGHT')
            if event.key == pygame.K_UP:
                print('FWD')
                r.set(control_cmd_key, 'FWD')
            if event.key == pygame.K_DOWN:
                print('STOP')
                r.set(control_cmd_key, 'STOP')
    pygame.display.update()
    clock.tick(30)

