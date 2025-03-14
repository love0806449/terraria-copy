import pygame

class EventHandler:
    def __init__()->None:
        EventHandler.events=pygame.event.get()
    def poll_events()->None:
        EventHandler.events=pygame.event.get()
    def keydown(key):
        for event in EventHandler.events:
            if event.type==pygame.KEYDOWN:
                if event.key==key:
                    return True
        return False
    def clicked(leftright=1)->bool:  # 1 for left, 3 for right
        for event in EventHandler.events:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==leftright: # left click
                    return True
        return False
    def clicked_any()->bool:
        for event in EventHandler.events:
            if event.type==pygame.MOUSEBUTTONDOWN:
                return True
        return False