import pygame
import random

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 360
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock() 

#변수

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
light_GRAY = (224, 224, 224)
small_font = pygame.font.SysFont(None, 36)

CELL_SIZE = 40
COLUMN_COUNT = 9
ROW_COUNT = 9

bodies = [(COLUMN_COUNT // 2, ROW_COUNT // 2)]

class Tile:
    def __init__(self):
        self.bomb = False

grid = [[Tile() for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
BOMB_COUNT = 15
for _ in range(BOMB_COUNT):
    while True:
        column_index = random.randint(0, COLUMN_COUNT - 1)
        row_index = random.randint(0, ROW_COUNT - 1)
        tile = grid[row_index][column_index]
        if not tile.bomb:
            tile.bomb = True #폭탄 설치
            break
        
while True: #게임 루프
    screen.fill(light_GRAY) #단색으로 채워 화면 지우기

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            column_index = event.pos[0] // CELL_SIZE
            row_index = event.pos[1] // CELL_SIZE
            print(column_index, row_index)

    #화면 그리기

    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
            #pygame.draw.rect(screen, BLUE, rect) #커버
            pygame.draw.rect(screen, WHITE, rect, 1)
            pygame.draw.rect(screen, BLACK, [0,0,360,360],3)
            pygame.draw.lines(screen, BLACK, False, [[120, 0], [120, 360]],3)
            pygame.draw.lines(screen, BLACK, False, [[240, 0], [240, 360]],3)
            pygame.draw.lines(screen, BLACK, False, [[0, 120], [360, 120]],3)
            pygame.draw.lines(screen, BLACK, False, [[0, 240], [360, 240]],3)
            tile = grid[row_index][column_index]
            if tile.bomb: 
                dot_image = small_font.render('{}'.format('.'), True, WHITE) 
                screen.blit(dot_image, (CELL_SIZE * column_index + 10, CELL_SIZE * row_index + 10)) #임시로 폭탄 표시

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 