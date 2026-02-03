# pylint: disable=no-member
import pygame as pg
from change_scene import ChangeScene
from elements import MessageWindow
from elements import SelectFrame
from elements import SelectionControl
import get_text as gt
from elements import Fit_rect_size
from elements import End_State

class Stage:
    def __init__(self,end_state):
        self.end_state = end_state


    def blit(self,_events):
        pass

class Start(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/title.jpeg")
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        super().__init__(end_state)
        self.msg = MessageWindow((600,200),30,(248,223,170),30,(116,97,78))
        self.fit_rect_size = Fit_rect_size
        self.title_img = pg.image.load("assets/title_name.PNG").convert_alpha()
        self.fit_title_img = self.fit_rect_size.fit_to_rect(self.title_img,(600,600))
        #print(self.title_img.get_size())
        #print(self.fit_title_img.get_size())
    def update(self,_events):
        self.msg.set_text("\n\nenterで進む→")
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            return Prolog_01(self.end_state)
        return self
    
    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (900, 600))
        screen.blit(self.fit_title_img,(500,300))
        
    
class Prolog_01(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/prolog_01.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        #メッセージ表示クラス起動
        self.msg = MessageWindow()
        super().__init__(end_state)

        self.msg.set_text(
            "今日は9月1日。今日は文化祭だ。\n"
            "朝食を食べていると、通知が鳴る。\n"
            "『朝ご飯は食べた？』\n"
            "『うん。今日は何時に帰ってくる？』\n"
            "『ごめん、わからない』\n"
            "生活リズムの違いから、最近は親ともあまり話さなくなった。\n"
            "進路のこともそろそろ話さないといけないが..."
        )

    def update(self,_events):
        self.steps = self.steps + 1
        self.changer.blit(self.img)
        keys = pg.key.get_pressed()
        if self.steps >= 30:
            if keys[pg.K_RIGHT]:
                return Prolog_02(self.end_state)
        return self
    
    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (100, 590))

class Prolog_02(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/prolog_02.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        self.msg = MessageWindow()
        self.msg.set_text("そんなことを考えつつ家を出て、いつも通り学校へ行く。")
        super().__init__(end_state)

    def update(self,_events):
        self.changer.blit(self.img)
        self.steps = self.steps + 1
        keys = pg.key.get_pressed()
        if self.steps >= 30:
            if keys[pg.K_RIGHT]:
                return Prolog_03(self.end_state)
        return self
    
    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (100, 500))

class Prolog_03(Stage):#暗転
    def __init__(self,end_state):
        self.surf = pg.Surface((1200,800))
        self.surf.fill((0, 0, 0))
        self.steps = 0
        self.msg = MessageWindow()
        self.msg.set_text("...はずだった。")
        super().__init__(end_state)

    def update(self,_events):
        self.steps = self.steps + 1
        keys = pg.key.get_pressed()
        if self.steps >= 30:
            if keys[pg.K_RIGHT]:
                return Prolog_04_01(self.end_state)
        return self
    
    def blit(self, screen):
        screen.blit(self.surf, (0, 0))
        self.msg.blit(screen, (100, 500))



class Prolog_04_01(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/prolog_04.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        super().__init__(end_state)

        #メッセージ表示クラス起動
        self.msg = MessageWindow()

        self.msg.set_text(
            "気づけば、よくわからない場所にいた。本屋？雑貨屋？\n"
            "ここへはどうやってきたのだろうか。\n"
            "少し歩いてみると、一際目立つ人がいる。\n"
        )


    def update(self,_events):
        self.changer.blit(self.img)
        self.steps = self.steps + 1
        keys = pg.key.get_pressed()
        if self.steps >= 30:
            if keys[pg.K_RIGHT]:
                return Prolog_04_02(self.end_state)
        return self
    
    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (100, 590))

class Prolog_04_02(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/prolog_04.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        super().__init__(end_state)
        

        #メッセージ表示クラス起動
        self.msg = MessageWindow()
        self.msg.set_text("？「これは珍しいお客さんだ。どうかされました？」\n"
            "PL「えっと...ここはどこですか？それとあなたは誰？」\n"
            "？「おっとこれはこれは失礼。私はここの「店主」です。」\n"
            "  「ここは本屋兼雑貨屋みたいなところさ。でも、君たちが元いた世界ではないよ。」\n"
            "PL「ここから帰りたいんですけど...学校遅刻するし...」\n"
            "店主「ここから帰る...ですか。そうですね...まずここにどう来たか記憶はありますか？」\n"
            "PL「いえ...」\n"
            "店主「でしたら、そちらをまず見つけてみてはいかがですか？ここにはいろんなものがありますから。」"
            )
        
    def update(self,_events):
        self.changer.blit(self.img)
        self.steps = self.steps + 1
        keys = pg.key.get_pressed()
        if self.steps >= 30:
            if keys[pg.K_RIGHT]:
                return Search_01_1(self.end_state)
        return self
    
    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (100, 590))#文章表示
        
class Search_01_1(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/search_01.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        self.msg = MessageWindow()
        self.msg.set_text(gt.select_item(0,0))
        self.steps = 0
        self.start_step_count = 0
        self.change_scene_wait = False
        self.frame = SelectFrame()
        self.rect_colors = self.frame.reset_frame_color(3)
        self.selector = SelectionControl(self.msg,self.frame,self.rect_colors)
        super().__init__(end_state)

    def update(self,events):
        self.changer.blit(self.img)
        self.steps = self.steps + 1

        for event in events:
            if event.type == pg.KEYDOWN:
                self.selector.control_key(event.key,3)
                if event.key == pg.K_3:
                    self.change_scene_wait = True
            if self.change_scene_wait:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        if self.steps - self.start_step_count >= 100:
                            return FlashBack(self.end_state)

        return self

    def blit(self, screen):
        self.changer.blit(screen)
        pg.draw.rect(screen,self.rect_colors[0],(1050,300,150,100),2)#筆箱
        pg.draw.rect(screen,self.rect_colors[1],(880,520,200,200),2)#袋
        pg.draw.rect(screen,self.rect_colors[2],(850,700,350,100),2)#本
        self.msg.blit(screen, (100, 590))
        # self.msg.draw_select_arrow(screen)#20ずつで1行ずつ

class FlashBack(Stage):
    def __init__(self,end_state):
        self.surf = pg.Surface((1200,800))
        self.surf.fill((0, 0, 0))
        self.msg = MessageWindow()
        self.msg.set_text(gt.get_flashback_text(0,0))
        self.event_count = -1
        self.input_wait = 0
        super().__init__(end_state)

    def update(self,events):
        if self.input_wait > 0:
            self.input_wait -= 1
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.event_count += 1
                    self.input_wait = 10
                    if self.event_count <= 1:
                        self.msg.set_text(gt.get_flashback_text(0,self.event_count+1,True))
                    else:
                        return Search_01_2(self.end_state)
        return self
    
    def blit(self, screen):
        screen.blit(self.surf, (0, 0))
        self.msg.blit(screen, (100, 500))


class Search_01_2(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/search_01.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        self.msg = MessageWindow()
        self.msg.set_text(gt.select_item(0,4))
        self.event_count = -1
        self.input_wait = 0
        super().__init__(end_state)

    def update(self,events):
        self.changer.blit(self.img)
        if self.input_wait > 0:
            self.input_wait -= 1
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.input_wait = 10
                    self.event_count += 1
                    if self.event_count <= 1:
                        self.msg.set_text(gt.select_item(0,4))
                    elif self.event_count <= 2:
                        self.msg.set_text(gt.get_book_text(0,True))
                    elif self.event_count <= 4:
                        self.msg.set_text(gt.select_item(0,5))
                    else:
                        return Search_02(self.end_state)

        return self

    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (100, 500))            

class Search_02(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/search_02.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        self.msg = MessageWindow()
        self.msg.set_text(gt.select_item(1,0))
        self.frame = SelectFrame()
        self.rect_colors = self.frame.reset_frame_color(6)
        self.selector = SelectionControl(self.msg,self.frame,self.rect_colors)
        self.last_key = None
        self.event_count = -1
        self.next_scene_flag = [False] * 6
        self.input_wait = 0
        self.prev_allow = False
        super().__init__(end_state)
        self.select_count = 0
        self.key_pressed_flag = [False] * 6
        self.max_select = 0
    def update(self,events):
       #  #print("allow_other_route",self.end_state.allow_other_route)
       #  #print("second_route_flag",self.end_state.second_route_flag)
       #  #print("third_route_flag",self.end_state.third_route_flag)
       #  #print("prev_allow",self.prev_allow)
       #  #print("select_count",self.select_count)
       #  #print("next_scene_flag",self.next_scene_flag)
        # 最大選択回数の指定
        if self.end_state.loop_count >= 3:
            self.max_select = 6
        elif self.end_state.loop_count == 2:
            self.max_select = 5
        else:
            self.max_select = 3
        if self.end_state.allow_other_route != self.prev_allow:
            self.rect_colors[1] = "#f5cc8a"
            self.rect_colors[2] = "#f5cc8a"
            self.rect_colors[4] = "#f5cc8a"
            # self.prev_allow = self.end_state.allow_other_route
        if self.input_wait > 0:
            self.input_wait -= 1
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.event_count += 1
                    self.input_wait = 10
                    if self.last_key == 1:
                        self.msg.set_text(gt.get_book_text(1,True)+ "\n" + gt.get_talking_text(0,0))
                        self.next_scene_flag[0] = True
                    elif self.last_key == 6:
                        self.msg.set_text(gt.get_book_text(2,True)+ "\n" + gt.get_talking_text(0,0))
                        self.next_scene_flag[5] = True
                    elif self.last_key == "return":
                        return Search_03(self.end_state)
                    self.last_key = None
                #無効化キーの設定
                if self.end_state.allow_other_route:
                    valid = self.selector.control_key(event.key,6,1,6)
                else:
                    valid = self.selector.control_key(event.key,6,1,6,(1,2,4))
                if  valid  == False:
                    continue
                if event.key == pg.K_1:
                    self.last_key = 1
                    if not self.key_pressed_flag[0]:
                        self.key_pressed_flag[0] = True
                        self.select_count += 1

                elif event.key == pg.K_2:
                    self.next_scene_flag[1] = True
                    if not self.key_pressed_flag[1]:
                        self.key_pressed_flag[1] = True
                        self.select_count += 1

                elif event.key == pg.K_3:
                    self.next_scene_flag[2] = True
                    if not self.key_pressed_flag[2]:
                        self.key_pressed_flag[2] = True
                        self.select_count += 1

                elif event.key == pg.K_4:
                    self.next_scene_flag[3] = True
                    if not self.key_pressed_flag[3]:
                        self.key_pressed_flag[3] = True
                        self.select_count += 1

                elif event.key == pg.K_5:
                    self.next_scene_flag[4] = True
                    if not self.key_pressed_flag[4]:
                        self.key_pressed_flag[4] = True
                        self.select_count += 1

                elif event.key == pg.K_6:
                    self.last_key = 6
                    if not self.key_pressed_flag[5]:
                        self.key_pressed_flag[5] = True
                        self.select_count += 1
                selected = {i for i, f in enumerate(self.next_scene_flag) if f}

                if event.key == pg.K_RETURN:
                    self.key_pressed_flag = [False] * 6
                    #最大回数終了後の処理
                    if self.select_count >= self.max_select:
                        self.msg.set_text(gt.get_talking_text(0,1))
                        self.last_key = "return"
                        #エンド分岐処理
                        if self.end_state.loop_count == 1:
                            # 1周目
                            if {0,3,5}.issubset(selected):
                                pass
                            
                        elif self.end_state.loop_count == 2:
                            # 2周目
                            if selected == {0,1,3,4,5}:
                                #print("🚩 second_route_flag が False → True になった")
                                self.end_state.second_route_flag = True
                        else:
                            # 3周目以降
                            if selected == {0,1,3,4,5}:
                                #print("🚩 second_route_flag が False → True になった")
                                self.end_state.second_route_flag = True
                            if selected == {0,1,2,3,4,5}:
                                self.end_state.third_route_flag = True
                                #print("🚩 third_route_flag が False → True になった")
        return self

    def blit(self, screen):
        self.changer.blit(self.img)
        self.changer.blit(screen)
        pg.draw.rect(screen,self.rect_colors[0],(515,250,200,90),2)
        pg.draw.rect(screen,self.rect_colors[1],(965,250,200,90),2)
        pg.draw.rect(screen,self.rect_colors[2],(630,430,220,100),2)
        pg.draw.rect(screen,self.rect_colors[3],(1055,430,100,100),2)
        pg.draw.rect(screen,self.rect_colors[4],(600,600,150,200),2)
        pg.draw.rect(screen,self.rect_colors[5],(795,630,150,170),2)
        self.msg.blit(screen, (100, 600))      
class Search_03(Stage):
    def __init__(self,end_state):
        self.img = pg.image.load("assets/search_03.jpeg")
        self.steps = 0
        self.changer = ChangeScene()
        self.changer.make_image(self.img)
        self.msg = MessageWindow()
        self.msg.set_text(gt.get_talking_text(0,2))
        self.event_count = -1
        self.input_wait = 0
        super().__init__(end_state)
        #print("Search_03:", self.end_state.second_route_flag)
        self.next_scene_flag = False

    def update(self,events):
        self.changer.blit(self.img)
        if self.input_wait > 0:
            self.input_wait -= 1
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.event_count += 1
                    #print(self.event_count)
                    self.input_wait = 10
                    self.msg.set_text(gt.get_talking_text(0,int(self.event_count)+2))
                    if self.event_count >= 4:
                        self.next_scene_flag = True
        if self.next_scene_flag:
            if  self.end_state.second_route_flag:
                #print("go to End02")
                return End_02(self.end_state)
            else:
                #print("go to End01")
                return End_01(self.end_state)
        return self


    def blit(self, screen):
        self.changer.blit(screen)
        self.msg.blit(screen, (100, 600)) 

class End_01(Stage):
    def __init__(self,end_state):
        self.surf = pg.Surface((1200,800))
        self.surf.fill((0, 0, 0))
        self.img = pg.image.load("assets/prolog_04.jpeg")
        self.cross_img = pg.image.load("assets/crosswalk.jpeg")
        self.changer = ChangeScene()
        self.msg = MessageWindow()
        self.msg.set_text(gt.get_flashback_text(1,0))
        self.event_count = -1
        self.input_wait = 0
        super().__init__(end_state)
        self.change_image = False
        self.end_state.loop_count += 1
        self.change_crosswalk_image = False


    def update(self,events):
        if self.input_wait > 0:
            self.input_wait -= 1

        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.input_wait = 10
                    self.event_count += 1
                    # #print("event_count:", self.event_count)
                    if self.event_count <= 4:
                        self.msg.set_text(gt.get_flashback_text(1,int(self.event_count)))
                    elif self.event_count <= 11:
                        self.change_image = True
                        self.msg.set_text(gt.get_ending_text(0,int(self.event_count)-5))
                    else:
                        self.end_state.allow_other_route = True
                        return Start(self.end_state)
                    if self.event_count >= 2:
                        self.change_crosswalk_image = True
                    elif self.event_count >= 4:
                        self.change_crosswalk_image = False
        return self

    def blit(self, screen):
        screen.blit(self.surf, (0, 0))
        if self.change_crosswalk_image:
            self.changer.make_image(self.cross_img)
            self.changer.blit(screen)
        if self.change_image:
            self.changer.make_image(self.img)
            self.changer.blit(screen)
        self.msg.blit(screen, (100, 500))
        

class End_02(Stage):
    def __init__(self,end_state):
        self.surf = pg.Surface((1200,800))
        self.surf.fill((0, 0, 0))
        self.img = pg.image.load("assets/prolog_04.jpeg")
        self.changer = ChangeScene()
        self.msg = MessageWindow()
        self.msg.set_text(gt.get_flashback_text(0,0))
        self.event_count = -1
        self.input_wait = 0
        self.change_image = False
        super().__init__(end_state)
        self.end_state.loop_count += 1


    def update(self,events):
        if self.input_wait > 0:
            self.input_wait -= 1
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.input_wait = 10
                    self.event_count += 1
                    #print("event_count:", self.event_count)
                    if self.event_count <= 2:
                        self.msg.set_text(gt.get_flashback_text(0,int(self.event_count)))
                    elif self.event_count == 3:
                        self.msg.set_text(gt.get_ending_talk_text(0,0))
                    elif self.event_count <= 13:
                        if self.event_count % 2 == 0:
                            self.msg.set_text(gt.get_book_text((int(self.event_count)-4)//2))
                        else:
                            self.msg.set_text(gt.get_ending_talk_text(0,(int(self.event_count)-4)//2+1))
                        if self.end_state.third_route_flag  == True and self.event_count == 12:
                            #print("go to End03")
                            return End_03(self.end_state)
                    elif self.event_count == 14:
                        self.msg.set_text(gt.get_ending_talk_text(0,6))
                    elif self.event_count <= 18:
                        self.msg.set_text(gt.get_ending_text(1,int(self.event_count)-15))
                    else:
                        return Start(self.end_state)
        return self

    def blit(self, screen):
        screen.blit(self.surf, (0, 0))
        if self.change_image:
            self.changer.make_image(self.img)
            self.changer.blit(screen)
        self.msg.blit(screen, (100, 500))
    

class End_03(Stage):
    def __init__(self,end_state):
        self.surf = pg.Surface((1200,800))
        self.surf.fill((0, 0, 0))
        self.img = pg.image.load("assets/prolog_04.jpeg")
        self.changer = ChangeScene()
        self.msg = MessageWindow()
        self.msg.set_text(gt.get_flashback_text(0,0))
        self.event_count = -1
        self.input_wait = 0
        self.select_end_flag = False
        self.finish_end_flag = False
        self.finish_select_flag = False
        super().__init__(end_state)
        self.end_state.loop_count += 1
        self.en = End_State
        self.change_image = False


    def update(self,events):
        if self.input_wait > 0:
            self.input_wait -= 1
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and self.input_wait == 0:
                    self.input_wait = 10
                    self.event_count += 1
                    #print("event_count:", self.event_count)
                    if self.event_count <= 5:
                        self.msg.set_text(gt.get_ending_talk_text(1,self.event_count))
                    elif self.event_count <= 7:
                        self.msg.set_text(gt.get_flashback_text(2,int(self.event_count)-6))
                    elif self.event_count <= 13:
                        self.msg.set_text(gt.get_ending_talk_text(2,int(self.event_count)-8))
                    elif self.event_count == 14:
                        self.msg.set_text(gt.get_selected_ending_text(0,0))
                        self.select_end_flag = True
                    elif self.event_count <= 17 and self.finish_select_flag == True:
                        self.msg.set_text(gt.get_ending_text(2,int(self.event_count)-15))
                    elif self.event_count <= 25 and self.finish_end_flag == False and self.finish_select_flag == True:
                        self.msg.set_text(gt.get_ending_text(2,int(self.event_count)-18))
                    elif self.finish_select_flag == True:
                        return Start(self.end_state)
                    # print(self.event_count)
                    
                    if self.event_count >= 21:
                        self.change_image = False
                        self.surf.fill((0,0,0))
                        # print("black02")

                    elif self.event_count >= 18:
                        self.change_image = True
                        # print("image")

                    elif 24 >= self.event_count >= 9:
                        # print("White02")
                        self.surf.fill((239,242,242))

                    elif  20>= self.event_count >= 6:
                        # print("black01")
                        self.surf.fill((0,0,0))

                    elif 15 >= self.event_count >= 2:
                        # print("white01")
                        self.surf.fill((239,242,242))

                if self.select_end_flag and self.finish_select_flag == False:
                    #print("event_count⭐️:", self.event_count)
                    if event.key == pg.K_1:
                        self.msg.set_text(gt.get_selected_ending_text(1,0))
                        self.finish_select_flag = True
                        self.event_count = 17
                    elif event.key == pg.K_2:
                        self.msg.set_text(gt.get_selected_ending_text(2,0))
                        self.finish_select_flag = True
                        self.finish_end_flag = True
                        self.event_count = 17
        return self

    def blit(self, screen):
        screen.blit(self.surf, (0, 0))
        if self.change_image:
            self.changer.make_image(self.img)
            self.changer.blit(screen)
        self.msg.blit(screen, (100, 500))
