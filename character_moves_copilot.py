from pico2d import *
import math

# 화면 설정
open_canvas(800, 600)

# 이미지 로드
character = load_image('character.png')
grass = load_image('grass.png')

# 캐릭터 초기 위치
x, y = 90, 550

# 움직임 상태
movement_mode = "rectangle"  # "rectangle" 또는 "circle"
rect_phase = 0  # 사각형: 0=오른쪽, 1=아래, 2=왼쪽, 3=위
circle_angle = 0

# 사각형 움직임 설정
rect_speed = 3
margin = 50

# 원형 움직임 설정
circle_center_x = 400
circle_center_y = 300
circle_radius = 150
circle_speed = 0.05

running = True

while running:
    clear_canvas()

    # 캐릭터 움직임
    if movement_mode == "rectangle":
        if rect_phase == 0:  # 오른쪽으로 이동
            x += rect_speed
            if x >= 800 - margin:
                rect_phase = 1
        elif rect_phase == 1:  # 아래로 이동
            y -= rect_speed
            if y <= margin:
                rect_phase = 2
        elif rect_phase == 2:  # 왼쪽으로 이동
            x -= rect_speed
            if x <= margin:
                rect_phase = 3
        elif rect_phase == 3:  # 위로 이동
            y += rect_speed
            if y >= 600 - margin:
                rect_phase = 0
                movement_mode = "circle"
                circle_angle = 0

    elif movement_mode == "circle":
        circle_angle += circle_speed
        x = circle_center_x + circle_radius * math.cos(circle_angle)
        y = circle_center_y + circle_radius * math.sin(circle_angle)

        # 한 바퀴 완료시 사각형 모드로 전환
        if circle_angle >= 2 * math.pi:
            movement_mode = "rectangle"
            rect_phase = 0
            x, y = margin, 600 - margin

    # 이미지 그리기
    grass.draw(400, 45)
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
