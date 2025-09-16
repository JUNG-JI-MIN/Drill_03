from pico2d import *
import math

# 화면 설정
open_canvas(800, 600)

# 이미지 로드
character = load_image('character.png')
grass = load_image('grass.png')

# 캐릭터 초기 위치 (시작점이자 끝점)
start_x, start_y = 400, 90
x, y = start_x, start_y

# 움직임 상태
movement_mode = "rectangle"  # "rectangle" 또는 "circle"
rect_phase = 0  # 사각형: 0~5 단계
circle_angle = 0

# 사각형 움직임 설정
rect_speed = 3
x_min, x_max = 20, 780
y_min, y_max = 90, 560

# 원형 움직임 설정
circle_center_x = 400
circle_center_y = 325  # (90 + 560) / 2
circle_radius = 150
circle_speed = 0.05

running = True

while running:
    clear_canvas()

    # 캐릭터 움직임
    if movement_mode == "rectangle":
        if rect_phase == 0:  # 1. 400,90 → 780,90 (오른쪽으로)
            x += rect_speed
            if x >= x_max:
                rect_phase = 1
        elif rect_phase == 1:  # 2. 780,90 → 780,560 (아래로)
            y += rect_speed
            if y >= y_max:
                rect_phase = 2
        elif rect_phase == 2:  # 3. 780,560 → 20,560 (왼쪽으로)
            x -= rect_speed
            if x <= x_min:
                rect_phase = 3
        elif rect_phase == 3:  # 4. 20,560 → 20,90 (위로)
            y -= rect_speed
            if y <= y_min:
                rect_phase = 4
        elif rect_phase == 4:  # 5. 20,90 → 400,90 (오른쪽으로 원래 자리)
            x += rect_speed
            if x >= start_x:
                movement_mode = "circle"
                circle_angle = -math.pi / 2  # 원의 맨 아래에서 시작
                rect_phase = 0

    elif movement_mode == "circle":
        circle_angle -= circle_speed  # 반시계방향
        x = circle_center_x + circle_radius * math.cos(circle_angle)
        y = circle_center_y + circle_radius * math.sin(circle_angle)

        # 한 바퀴 완료시 사각형 모드로 전환
        if circle_angle <= -math.pi / 2 - 2 * math.pi:
            movement_mode = "rectangle"
            x, y = start_x, start_y  # 시작점으로 돌아감

    # 이미지 그리기
    grass.draw(400, 30)
    character.draw(x, y)

    update_canvas()

    # 이벤트 처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

    delay(0.01)

close_canvas()
