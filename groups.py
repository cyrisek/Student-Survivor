from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, target_pos):
        # kamera przesuwa sie tak, aby gracz byl na srodku ekranu
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        # podzial na warstwy: najpierw ziemia, potem obiekty
        ground = [s for s in self if hasattr(s, 'ground')]
        objects = [s for s in self if not hasattr(s, 'ground')]

        for layer in [ground, objects]:
            for sprite in sorted(layer, key=lambda s: s.rect.centery):
                pos = sprite.rect.topleft + self.offset
                self.display.blit(sprite.image, pos)
