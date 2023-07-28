import pymunk
import pygame
import random

class Box:
    def __init__(self, x, y, r):
        # 박스 크기
        print(r)

        self.width, self.height = 10, 10
        
        # 물리 엔진 초기화
        self.space = pymunk.Space()
        self.space.gravity = (0, 1)  # 중력 설정 (x, y)
        
        # 박스 물리 속성 설정
        moment = pymunk.moment_for_box(1, (self.width, self.height))  # 질량 1의 박스의 모멘트 계산
        self.body = pymunk.Body(1, moment)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        self.shape.elasticity = 0.5  # 탄성 설정 (0 ~ 1)
        
        # 물리 공간에 박스 추가
        self.space.add(self.body, self.shape)
        
    def update(self):
        self.space.step(1/60)  # 물리 시뮬레이션 갱신
        
    def draw(self, screen):
        # 박스 그리기
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], self.width, self.height))


# 파이게임 초기화
pygame.init()

# 창 크기 설정
width, height = 1200, 720
screen = pygame.display.set_mode((width, height))

# 창 타이틀 설정
pygame.display.set_caption("Black Background Example")

# 박스 100개를 저장할 리스트
boxes = []

# 100개의 박스 생성
for _ in range(100):
    r = random.random()
    random_x = random.randint(0, width - 10)
    box = Box(random_x, 100, r)
    boxes.append(box)

# 검은 배경 색상 설정
black = (0, 0, 0)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 모든 박스 업데이트
    for box in boxes:
        box.update()

    # 화면에 검은 배경 그리기
    screen.fill(black)

    # 모든 박스 그리기
    for box in boxes:
        box.draw(screen)

    # 창 업데이트
    pygame.display.flip()

    for box in boxes:
        for shape in box.space.shapes:
            if isinstance(shape, pymunk.Poly):
                x, y = shape.body.position
                if x < 0 or x > width or y < 0 or y > height:
                    shape.body.velocity = (-shape.body.velocity.x, -shape.body.velocity.y)

# 파이게임 종료
pygame.quit()
