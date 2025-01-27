import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(r'pygame/lunar.png').convert()
        self.rect = pygame.Rect(10,10,30,30)
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.isJumping, self.onGround = False, False
        self.gravity, self.friction = .35, -.12
        self.position, self.velocity = pygame.math.Vector2(0,0), pygame.math.Vector2(0,0)
        self.acceleration = pygame.math.Vector2(0,self.gravity)

    def draw(self, display):
        #display.blit(self.image, (self.rect.x, self.rect.y))
        BLACK = (0,0,0)
        pygame.draw.rect(display,BLACK, self.rect)

        
    def update(self,dt,displayLength):
        self.horizonatal_movement(dt)
        self.vertical_movement(dt,displayLength)
    
    def horizonatal_movement(self,dt):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= .3
        elif self.RIGHT_KEY:
            self.acceleration.x += .3
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x
    
    def vertical_movement(self, dt, displayLength):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7: 
            self.velocity.y = 7
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        if self.position.y > displayLength + 10:
            self.on_ground = True
            self.velocity.y = 0
            self.position.y = -10
        self.rect.bottom = self.position.y


    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False

