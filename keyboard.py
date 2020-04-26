import pygame

event_types = [pygame.KEYDOWN, pygame.KEYUP]

KEYDOWN = pygame.USEREVENT
KEYUP = pygame.USEREVENT + 1
kbd_event_types = [KEYDOWN, KEYUP]

actions = {}
pressed = {}


def bind_key(key, action):
    actions[key] = action
    pressed[action] = False


def is_pressed(action):
    return pressed[action]


def is_pressed_any():
    return True in pressed.values()


def handle_keys():
    for event in pygame.event.get(event_types):
        if event.type == pygame.KEYDOWN:
            if event.key in actions:
                pressed[actions[event.key]] = True
                pygame.event.post(pygame.event.Event(KEYDOWN, {'action': actions[event.key]}))
        elif event.type == pygame.KEYUP:
            if event.key in actions:
                pressed[actions[event.key]] = False
                pygame.event.post(pygame.event.Event(KEYUP, {'action': actions[event.key]}))


def get():
    return pygame.event.get(kbd_event_types)
