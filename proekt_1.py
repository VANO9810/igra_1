from pygame import*

okno = display.set_mode((1200,900))
game = True
clock = time.Clock()

Fon = transform.scale(image.load('fon_igri_1.png'), (1200,700))

class GameSprite(sprite.Sprite):
    def __init__(self, pik, x,y):
        super().__init__()
        self.image = transform.scale(image.load(pik), (40,40))
        self.rect  = self.image.get_rect()
        self.rect.x = x       
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def control(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_d]:
            self.rect.x += 3
        if kn[K_a]:
            self.rect.x -= 3
        if kn[K_s]:
            self.rect.y += 3
        if kn[K_w]:
            self.rect.y -= 3   

igrok = Player('geroi.png', 495,495)

class monster (GameSprite):
    def follow(self):
        self.ris()
        kn = key.get_pressed()
        if self.rect.x > igrok.rect.x:
            self.rect.x -= 1
         
        if self.rect.x < igrok.rect.x:
            self.rect.x += 1
        if self.rect.y < igrok.rect.y:
            self.rect.y += 1
        if self.rect.y > igrok.rect.y:
            self.rect.y -= 1

zombi = monster('zombie.png', 50,50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    okno.blit(Fon, (0,0))
    igrok.control()
    zombi.follow()
    clock.tick(60)
    display.update()
