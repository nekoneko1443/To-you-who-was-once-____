# pylint: disable=no-member
import pygame as pg
import sys
import elements as e
import stages

pg.init()
screen = pg.display.set_mode((1200,800))
screen.fill((0,0,0))
orig_bg = pg.image.load("assets/title.jpeg").convert_alpha()
want_size = (1200,800)
bg = e.Fit_rect_size.fit_to_rect(orig_bg, want_size)
rect_bg = bg.get_rect()
clock = pg.time.Clock()
end_state = e.End_State()
stage = stages.Start(end_state)
pg.key.set_repeat(7, 5)



while True:
    events = pg.event.get()

    # 2-1 画面を初期化する。
    screen.fill(pg.Color("WHITE"))

    screen.blit(bg,rect_bg)
        # 2-4. 画面を表示する。
    stage = stage.update(events)
    stage.blit(screen)

    pg.display.update()
    clock.tick(60) # 画面の更新を1秒間に60回以下のスピードに設定する。

    # 2-5. 閉じるボタンが押されたら終了する。
    for event in events:  # イベント一覧を取得して、各イベントを調べる。
        if event.type == pg.QUIT: # もし、閉じるボタンが押されたら。
            pg.quit()             # PyGame を終了する。これだけではウィンドウは閉じない。
            sys.exit()            # ウィンドウを閉じて、プログラムを終了する。