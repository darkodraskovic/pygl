import pygame

key_event_types = [pygame.KEYDOWN, pygame.KEYUP]

mbutton_event_types = [pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]

ACTIONDOWN = pygame.USEREVENT
ACTIONUP = pygame.USEREVENT + 1

key_actions = {}
mbutton_actions = {}
pressed = {}


def bind_key(key, action):
    key_actions[key] = action
    pressed[action] = False


def bind_mbutton(button, action):
    mbutton_actions[button] = action
    pressed[action] = False


def is_pressed(action):
    return pressed[action]


def is_pressed_any():
    return True in pressed.values()


def __handle_action(action, is_pressed):
    pressed[action] = is_pressed
    event = pygame.event.Event(ACTIONDOWN if is_pressed else ACTIONUP, {'action': action})
    pygame.event.post(event)


def handle_keys():
    for event in pygame.event.get(key_event_types):
        if event.key in key_actions:
            action = key_actions[event.key]
            if event.type == pygame.KEYDOWN:
                __handle_action(action, True)
            elif event.type == pygame.KEYUP:
                __handle_action(action, False)

    for event in pygame.event.get(mbutton_event_types):
        if event.button in mbutton_actions:
            action = mbutton_actions[event.button]
            if event.type == pygame.MOUSEBUTTONDOWN:
                __handle_action(action, True)
            elif event.type == pygame.MOUSEBUTTONUP:
                __handle_action(action, False)
