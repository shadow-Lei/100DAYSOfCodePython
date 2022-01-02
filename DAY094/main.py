import pygame

pygame.init()
#建立視窗大小寬度x長度 300 x 400
screen = pygame.display.set_mode((300,400))
#建立標題
pygame.display.set_caption(('Space Invanders'))

BLACK = (0,0,0) # 黑色
WHITE = (255,255,255) #白色
GRAY = (192,192,192) #灰色
INDIGODye =(8,46,84)

GAMEOVER=False
###建立背景
def create_bg():
    #以純色當背景
    #先製作畫布
    bg =pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill(BLACK)

    screen.blit(bg,(0,0))


    ###以圖片當背景
    #bg =pygame.image.load('<image path>')
    #bg = bg.convert()
    #bg.bilt(bg,(0,0))
    #pygame.display.update()

clock = pygame.time.Clock()

###創立一個角色類別(簡易太空船)
class Spaceship(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       #設定初始位置
       self.rect.center = (150,380)

       self.last_shot = pygame.time.get_ticks()

    def update(self):
        # 移動的距離
        speed=4

        cooldown=200

        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_LEFT]:
            self.rect.x = self.rect.x - speed if self.rect.x > 4 else 0
        elif keypress[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + speed if self.rect.x < screen.get_size()[0]-self.image.get_size()[0] else screen.get_size()[0] -self.image.get_size()[0]

        time_now = pygame.time.get_ticks()

        #射擊
        #time_now、self.last_shot、cooldown的設置是為了不要一次射擊太多的bullets
        if keypress[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(INDIGODye,5,10,self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)

            self.last_shot=time_now

###Spaceship Bullets
class Bullets(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height,center_x, center_y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.center = (center_x, center_y)

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

        #當2個sprite碰觸到就消除
        if pygame.sprite.spritecollide(self,enemies_group,dokill=True):
            self.kill()

class Enemies(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height,center_x,center_y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.center = (center_x, center_y)


    def update(self):
        global GAMEOVER
        self.rect.y += 1 if not GAMEOVER else 0
        if self.rect.y > screen.get_height() - 50:
            GAMEOVER = True



def create_enemies():
    enemies_rows=2
    enemies_cols=5
    for row in range(enemies_rows):
        for item in range(enemies_cols):
            enemies = Enemies(GRAY,30,30,50+item*50,50+row*50)
            enemies_group.add(enemies)

font=pygame.font.SysFont('Constantia', 30)
def show_text(text,color,x,y):
    # 不可以使用keyword ,ex.font.render(text='',color='')
    text = font.render(text, True, color)
    screen.blit(text, (x,y) )

# create sprite groups
spaceship_group = pygame.sprite.Group()
spaceship=Spaceship(WHITE,25,10)
spaceship_group.add(spaceship)

enemies_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
create_enemies()

gameRun=True

#讓遊戲在while中run
while gameRun:
    # 更新時間以60幀調用一次
    clock.tick(60)
    # 建立背景
    create_bg()

    #當遊戲按了右上角的X之後會結束
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun=False

    #確認敵人數
    if len(enemies_group)==0:
        show_text('You Win!', WHITE, int(screen.get_width() / 2) - 50, int(screen.get_height( ) /2)-50)

    if GAMEOVER:
        #無法使用\n
        show_text('GAME OVER!', WHITE, int(screen.get_width() / 2) - 50, int(screen.get_height() / 2)-50)
        show_text('You Lost!', WHITE, int(screen.get_width() / 2) - 50, int(screen.get_height() / 2))



    spaceship_group.update()
    enemies_group.update()
    bullet_group.update()


    spaceship_group.draw(screen)
    enemies_group.draw(screen)
    bullet_group.draw(screen)
    # 將顯示設定更新
    pygame.display.update()

pygame.quit()
