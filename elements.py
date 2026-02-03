# pylint: disable=no-member
import pygame as pg
import get_text as gt

class Fit_rect_size:
    @staticmethod
    def fit_to_rect(img,want_size=(1200,800)):
        (w, h) =(img.get_rect().width,img.get_rect().height) # 元の画像の大きさを取得する。
        (size_width, size_height) = want_size# 指定のスケールの大きさを取得する。
        if w == 0 or h == 0 or size_width <= 0 or size_height <= 0:
            return img

        scale = min(want_size[0] / w, want_size[1] / h) # 倍率を求める。‼️小さい方を優先する
        new_size =(int(round(w * scale)), int(round(h * scale))) # 倍率をもとに変換後の画像サイズを求める。
        return pg.transform.scale(img, new_size)
  

class MessageWindow:
    def __init__(
        self,
        size=(1000, 180),
        font_size=15,
        bg_color=(151, 125, 84),
        alpha=240,
        text_color=(245, 204, 138),
        font_name="hiraginosansgb",
        padding=(20, 20),
        line_gap=5,
        select_index=0,
        arrow_x = 110,
        arrow_y = None
    ):
        self.size = size
        self.bg_color = bg_color
        self.alpha = alpha
        self.font = pg.font.SysFont(font_name, font_size)
        self.text_color = text_color
        self.padding_left, self.padding_top = padding
        self.line_gap = line_gap

        self.surf = pg.Surface(size, pg.SRCALPHA)
        self.surf.fill((*bg_color, alpha))

        self.text = ""

        self.select_index = select_index

        self.arrow_x = arrow_x
        if arrow_y is None:
            arrow_y = [660, 680, 700]
        self.arrow_y = arrow_y

        self.flashback_texts =[]

    def set_text(self, text):
        self.text = text
        self._render_text()

    def _render_text(self):
        self.surf.fill((*self.bg_color, self.alpha))

        lines = self.text.split("\n")
        line_height = self.font.get_height()
        ascent = self.font.get_ascent()#メッセージ枠の上側が空くのを直した.
        y = self.padding_top - ascent

        for line in lines:
            text_surf = self.font.render(line, True, self.text_color)
            self.surf.blit(text_surf, (self.padding_left, y))
            y += line_height + self.line_gap

        
    def blit(self, screen, pos):
        screen.blit(self.surf, pos)

class SelectFrame:
    def __init__(self):
        self.default_color = "#f5cc8a"
        self.disable_color = "#919191"#gray: disable select color
        self.end_state = End_State()


    def reset_frame_color(self,num):
        rect_colors = [self.default_color] * num

        if num >= 4 and not self.end_state.allow_other_route:
            rect_colors[1] = self.disable_color
            rect_colors[2] = self.disable_color
            rect_colors[4] = self.disable_color

        return rect_colors
    
    def is_selectable(self, select_id,not_select_num):
        if not self.end_state.second_route_flag:
            return select_id not in not_select_num # 0-based
        return True
    
class SelectionControl:
    def __init__(self,msg,frame,rect_colors):
        self.msg = msg
        self.frame = frame
        self.rect_colors = rect_colors
        self.frame = SelectFrame()
        
        # self.end_state = End_State()
        
    def control_key(self,key,num,search_num = 0,add_num = 1,not_select_num = (10,10,10)):
        key_map = {
            pg.K_1:0,
            pg.K_2:1,
            pg.K_3:2,
            pg.K_4:3,
            pg.K_5:4,
            pg.K_6:5,
        }

        if key in key_map:
            key_id = key_map[key]

            if key_id >= num:
                return False

            if not self.frame.is_selectable(key_id,not_select_num):
                #print(key_id, "まだ選べない")
                return False
            text = gt.select_item(search_num,key_id + add_num)
            self.rect_colors[key_id] = (193,0,0)
            self.msg.set_text(text)

        elif key == pg.K_RETURN:
            text = gt.select_item(search_num,0)
            self.msg.set_text(text)
            self.rect_colors[:] = self.frame.reset_frame_color(num)

            

class End_State:
    def __init__(self):
        self.second_route_flag: bool = False
        self.third_route_flag: bool = False
        self.allow_other_route: bool = False
        self.loop_count = 1

    def reset_state(self):
        if self.second_route_flag:
            self.second_route_flag = False

        if self.third_route_flag:
            self.third_route_flag = False
        
        if self.allow_other_route:
            self.allow_other_route = False
