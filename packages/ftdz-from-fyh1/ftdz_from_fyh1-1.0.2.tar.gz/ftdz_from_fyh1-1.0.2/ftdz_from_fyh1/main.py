import pygame as pg
import traceback,random,time,os,sys
pg.init()
if os.path.exists('D:\\'):
    if not os.path.isfile('D:\\score'):
        with open("D:\\score","w") as f:
            f.write('0')
else:
    if not os.path.isfile("C:\\Users\\Public\\score"):
        with open("C:\\Users\\Public\\score","w") as f:
            f.write('0')
class Bullet(pg.sprite.Sprite):
    def __init__(self,ai):
        super().__init__()
        self.ai = ai
        self.c = pg.image.load("bullet1.png")
        self.rect = self.c.get_rect()
        self.rect.midtop = self.ai.br.midtop
        self.y = float(self.rect.y)
    def update(self):
        self.y -= 4
        self.rect.y = self.y
    def draw_b(self):
        self.ai.sc.blit(self.c,self.rect)
class Enemy(pg.sprite.Sprite):
    def __init__(self,ai):
        super().__init__()
        self.ai = ai
        self.image = pg.image.load("olp.png")
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 40
        self.x = float(self.rect.x)
    def update(self):
        self.x += (1.0 * self.ai.fl_d)
        self.rect.x = self.x
    def c_e(self):
        s_r = self.ai.sc_rect
        if self.rect.right >= s_r.right or self.rect.left <= 0:
            return True
class A_B(pg.sprite.Sprite):
    def __init__(self,ai):
        super().__init__()
        self.ai = ai
        self.d = pg.image.load("7801.png")
        self.d_r = self.d.get_rect()
    def update1(self):
        self.d_r.y += self.ai.bspeed
    def d_a_b(self):
        self.ai.sc.blit(self.d,self.d_r)
class Base(pg.sprite.Sprite):
    def __init__(self,ai):
        super().__init__()
        self.ai = ai
        self.e = pg.image.load("base2.png")
        self.e_r = self.e.get_rect()
        self.e_r.x = self.ai.width / 2
        self.e_r.y = self.ai.height - 130
    def update(self):
        if self.ai.b_d:
            self.e_r.x += 4
        else:
            self.e_r.x -= 4
    def c_e(self):
        if self.e_r.right >= 600 or self.e_r.left <= 200:
            return True
    def d_ba(self):
        self.ai.sc.blit(self.e,self.e_r)
class Button:
    def __init__(self,ai):
        self.ai = ai
        self.f = pg.image.load("begin_game1.png")
        self.f1 = pg.image.load("begin_game2.png")
        self.image = self.f
        self.f_r = self.f.get_rect()
        self.f_r.x = 300
        self.f_r.y = 250
    def d_b(self):
        self.ai.sc.blit(self.image,self.f_r)
class Skills:
    def __init__(self,ai):
        self.ai = ai
        self.g = pg.image.load("skills0.png")
        self.g1 = pg.image.load("skills1.png")
        self.g2 = pg.image.load("skills2.png")
        self.g3 = pg.image.load("skills3.png")
        self.g4 = pg.image.load("skills4.png")
        self.g5 = pg.image.load("skills5.png")
        self.g6 = pg.image.load("skills6.png")
        self.g7 = pg.image.load("skills6.png")
        self.image = self.g
        self.g_r = self.g.get_rect()
        self.g_r.x = self.ai.br.x
        self.g_r.bottom = self.ai.br.top
        self.i = 0
    def change(self):
        self.i += 1
        if self.i == 3:
            self.image = self.g1
        if self.i == 6:
            self.image = self.g2
        if self.i == 9:
            self.image = self.g3
        if self.i == 12:
            self.image = self.g4
            self.g_r.y -= 120
        if self.i == 15:
            self.image = self.g5
            self.g_r.y -= 120
        if self.i == 18:
            self.image = self.g6
            self.g_r.y -= 120
        if self.i == 21:
            self.image = self.g7
            self.ai.dz2 = False
            self.i = 0
            self.image = self.g
            self.g_r.bottom = self.ai.br.top
    def d_g(self):
        self.ai.sc.blit(self.image,self.g_r)
class Box:
    def __init__(self,ai):
        self.ai = ai
        self.h = pg.image.load("box1.png")
        self.h1 = pg.image.load("box2.png")
        self.h2 = pg.image.load("box3.png")
        self.a1 = [self.h,self.h1,self.h2]
        self.image = random.choice(self.a1)
        self.h_r = self.image.get_rect()
        self.h_r.x = random.randint(0,800)
        self.h_r.y = 0
    def update(self):
        self.h_r.y += 3
    def d_h(self):
        self.ai.sc.blit(self.image,self.h_r)
class S_B:
    def __init__(self,ai):
        self.ai = ai
        self.font = pg.font.Font("C:\\Windows\\Fonts\\simkai.ttf",28)
        self.p_s()
        self.p_l()
        self.p_li()
        self.p_h_s()
    def p_s(self):
        s_s = "得分：" + str(self.ai.score)
        self.s_i = self.font.render(s_s,True,(0,225,0))
        self.s_r = self.s_i.get_rect()
        self.s_r.right = self.ai.sc_rect.right - 10
        self.s_r.top = 0
    def p_l(self):
        s_l = "关卡：" + str(self.ai.level)
        self.l_i = self.font.render(s_l,True,(0,255,0))
        self.l_r = self.l_i.get_rect()
        self.l_r.y = self.s_r.y + 25
        self.l_r.x = self.s_r.x
    def p_li(self):
        if self.ai.s_s1:
            s_l = "血量：" + str(self.ai.life + self.ai.s_l)
        else:
            s_l = "血量：" + str(self.ai.life)
        self.li_i = self.font.render(s_l,True,(0,255,0))
    def p_h_s(self):
        s_h = "最高分：" + str(self.ai.high_score)
        self.l_h = self.font.render(s_h,True,(0,255,0))
        self.l_h_r = self.l_h.get_rect()
        self.l_h_r.x = 350
    def s_h_s(self):
        self.ai.sc.blit(self.l_h,self.l_h_r)
    def s_li_i(self):
        self.ai.sc.blit(self.li_i,self.li_i.get_rect())
    def s_l_i(self):
        self.ai.sc.blit(self.l_i,self.l_r)
    def s_s_i(self):
        self.ai.sc.blit(self.s_i,self.s_r)
class Life:
    def __init__(self,ai):
        self.ai = ai
        self.life = pg.image.load("life.png")
        self.s_l = pg.image.load("h_1.jpg")
        self.s_l1 = pg.image.load("h_0.jpg")
        self.image = self.s_l
        self.li_r = self.life.get_rect()
        self.li_r.y = 35
        self.s_l_r = self.s_l.get_rect()
        self.s_l_r.y = self.li_r.y + 63
        self.c_c()
    def c_c(self):
        if self.ai.life <= 10:
            self.color = (255,0,0)
        elif self.ai.life < 20:
            self.color = (255,205,0)
        else:
            self.color = (0,255,0)
    def c_d(self):
        pg.draw.line(self.ai.sc,self.color,
            [self.li_r.right,45],[self.ai.life * 3 + self.li_r.right,45])
        if self.ai.s_s1:
            pg.draw.line(self.ai.sc,(0,0,255),
                [self.s_l_r.right + 5,118],[self.ai.s_l * 3 + self.s_l_r.right,118])
            self.ai.sc.blit(self.image,self.s_l_r)
        self.ai.sc.blit(self.life,self.li_r)
class Switch:
    def __init__(self,ai):
        self.ai = ai
        self.i = pg.image.load("开.png")
        self.i1 = pg.image.load("关.png")
        self.image = self.i
        self.i_r = self.i.get_rect()
        self.i_r.x = self.ai.width - 43
        self.i_r.y = 45
    def d_i(self):
        self.ai.sc.blit(self.image,self.i_r)
class Shield:
    def __init__(self,ai):
        self.ai = ai
        self.g = pg.image.load("19.jpg")
        self.g_r = self.g.get_rect()
        self.g_r.top = self.ai.br.top
        self.g_r.x = 420
        self.g_r.y = 600 - 123
    def d_g(self):
        self.ai.sc.blit(self.g,self.g_r)
class Help:
    def __init__(self,ai):
        self.ai = ai
        self.l = pg.image.load("help2.png")
        self.l1 = pg.image.load("help1.png")
        self.l3 = pg.image.load("90.jpg")
        self.l2 = pg.image.load("c2.png")
        self.image = self.l
        self.l_r = self.l.get_rect()
        self.l_r.x = self.ai.button.f_r.x
        self.l_r.y = self.ai.button.f_r.y + 120
        self.l2_r = self.l2.get_rect()
        self.l2_r.right = 800
        self.l2_r.bottom = 600
        self.font = pg.font.Font("C:\\Windows\\Fonts\\STXINGKA.TTF",35)
        self.font1 = pg.font.Font("C:\\Windows\\Fonts\\STXINWEI.TTF",22)
    def d_help(self):
        self.ai.sc.blit(self.l3,self.l3.get_rect())
        s_h = self.font.render("飞坦大战帮助",True,(255,255,255))
        text = "ad←→移动飞船，f发射子弹，碰到任意宝箱后空格大招、护盾，金宝箱2次，"
        text1 = "空格大招，h护盾，护盾10滴血。飞船30滴血。坦克子弹速度随关卡增加，5、10关"
        text2 = "换子弹。20关胜利。黄宝箱还加1滴血、蓝宝箱还减1滴血。"
        s_h3 = self.font1.render(text2,True,(0,0,245))
        s_h1 = self.font1.render(text,True,(0,0,255))
        s_h2 = self.font1.render(text1,True,(0,0,250))
        s_h1_r = s_h1.get_rect()
        s_h2_r = s_h2.get_rect()
        s_h3_r = s_h3.get_rect()
        s_h1_r.x = 50
        s_h1_r.y = 50
        s_h2_r.y = s_h1_r.y + 55
        s_h3_r.y = s_h2_r.y + 55
        s_h_r = s_h.get_rect()
        s_h_r.x = 320
        self.ai.sc.blit(s_h3,s_h3_r)
        self.ai.sc.blit(s_h2,s_h2_r)
        self.ai.sc.blit(s_h1,s_h1_r)
        self.ai.sc.blit(s_h,s_h_r)
        self.ai.sc.blit(self.l2,self.l2_r)
    def d_l(self):
        self.ai.sc.blit(self.image,self.l_r)
class A_I:
    def __init__(self):
        self.size = self.width,self.height = 800,600
        self.en = self.width // (80 + 5)
        self.lm,self.rm = False,False
        self.f_d_s = 10
        self.fl_d = 1
        self.life = 30
        self.b_d = True
        self.start = False
        self.dz = 0
        self.dz2 = False
        self.score = 0
        self.a_s = 1
        self.level = 0
        self.start1 = True
        self.s_l = 10
        self.s_s = 0
        self.s_s1 = False
        self.help1 = False
        self.bspeed = 3
        self.win = False
        if os.path.exists("D:\\"):
            with open("D:\\score") as f:
                self.high_score = int(f.read())
        else:
            with open("C:\\Users\\Public\\score") as f:
                self.high_score = int(f.read())
        self.sc = pg.display.set_mode((self.size))
        self.a = pg.image.load("bg2(1).png")
        self.sc_rect = self.sc.get_rect()
        self.b = pg.image.load("player.png")
        self.br = self.b.get_rect()
        self.br.bottom = self.height
        self.button = Button(self)
        self.skills = Skills(self)
        self.box = Box(self)
        self.s_b = S_B(self)
        self.li = Life(self)
        self.sw = Switch(self)
        self.sh = Shield(self)
        self.help = Help(self)
        self.bullet = pg.sprite.Group()
        self.ene = pg.sprite.Group()
        self.a_b = pg.sprite.Group()
        self.base = pg.sprite.Group()
        self.br.left = self.width // 2
        self.c_f()
        self.u_b()
        self.run_game()
    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            self.s_b.p_li()
            self.dz1()
            if self.level >= 20:
                self.win = True
            if not self.s_s1:
                self.s_l = 0
            if self.s_l == 0:
                self.s_s1 = False
            if self.score > self.high_score:
                self.high_score = self.score
                self.s_b.p_h_s()
            if self.start and self.start1 and not self.win:
                for ii in self.base.sprites():
                    for i in self.ene.sprites():
                        if ii.e_r.colliderect(i):
                            self.a_b.remove(i)
                            self.base.remove(ii)
                if self.life <= 0:
                    self.lm,self.rm = False,False
                    self.f_d_s = 10
                    self.fl_d = 1
                    self.life = 30
                    self.b_d = True
                    self.start = False
                    self.dz = 0
                    self.dz2 = False
                    self.score = 0
                    self.a_s = 1
                    self.level = 0
                    self.s_l = 10
                    self.s_s = 0
                    self.s_s1 = False
                    self.bspeed = 3
                self.bullet.update()
                self.c_f_e()
                self.ene.update()
                for bu in self.bullet.copy():
                    if bu.rect.bottom <= 0:
                        self.bullet.remove(bu)
                if self.lm and self.br.left > 0:
                    self.br.x -= 2.5
                    self.sh.g_r.x = self.br.x
                    self.skills.g_r.x = self.br.x
                if self.rm and self.br.right < self.width:
                    self.br.x += 2.5
                    self.sh.g_r.x = self.br.x
                    self.skills.g_r.x = self.br.x
                for i in self.a_b:
                    i.update1()
                coll = pg.sprite.groupcollide(self.bullet,self.ene,True,True)
                if coll:
                    for i in coll.values():
                        self.score += self.a_s * len(i)
                        self.s_b.p_s()
                if not self.ene:
                    self.bullet.empty()
                    self.level += 1
                    self.s_b.p_l()
                    self.c_f()
                    self.bspeed *= 1.2
                for i in self.a_b.sprites():
                    if i.d_r.colliderect(self.br):
                        self.life -= 1
                        self.s_b.p_li()
                        self.li.c_c()
                        self.a_b.remove(i)
                    if i.d_r.y >= self.width:
                        self.a_b.remove(i)
                    for ii in self.base:
                        if i.d_r.colliderect(ii.e_r):
                            self.a_b.remove(i)
                            self.base.remove(ii)
                    if i.d_r.colliderect(self.sh.g_r):
                        if self.s_s:
                            self.a_b.remove(i)
                            self.s_l -= 1
                for i in self.ene.sprites():
                    if i.rect.colliderect(self.skills.g_r):
                        self.ene.remove(i)
                        self.score += 1
                        self.s_b.p_s()
                if not self.a_b:
                    self.u_a_b()
                if not self.base:
                    self.u_b()
                if self.br.colliderect(self.box.h_r):
                    if self.box.image == self.box.h:
                        self.dz += 1
                        self.s_s += 1
                        self.life += 1
                        self.s_b.p_li()
                    if self.box.image == self.box.h1:
                        self.dz += 1
                        self.life -= 1
                        self.s_s += 1
                    if self.box.image == self.box.h2:
                        self.dz += 2
                        self.s_s += 1
                    self.box.h_r.x = random.randint(0,800)
                    self.box.h_r.y = 0
                    self.box.image = random.choice(self.box.a1)
                if self.box.h_r.top >= 600:
                    self.box.h_r.x = random.randint(0,800)
                    self.box.h_r.y = 0
                    self.box.image = random.choice(self.box.a1)
            if self.s_l < 5:
                self.li.image = self.li.s_l1
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if os.path.exists("D:\\"):
                    with open("D:\\score","w") as f:
                        f.write(str(self.high_score))
                else:
                    with open("C:\\Users\\Public\\score") as f:
                        f.write(str(self.high_score))
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_key_down(event)
            elif event.type == pg.KEYUP:
                self.check_key_up(event)
            elif event.type == pg.MOUSEMOTION:
                if self.button.f_r.collidepoint(event.pos):
                    self.button.image = self.button.f1
                else:
                    self.button.image = self.button.f
                if self.help.l_r.collidepoint(event.pos):
                    self.help.image = self.help.l1
                else:
                    self.help.image = self.help.l
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.button.f_r.collidepoint(event.pos):
                    self.start = True
                if self.sw.i_r.collidepoint(event.pos):
                    if self.start1:
                        self.start1 = False
                        self.sw.image = self.sw.i1
                    else:
                        self.start1 = True
                        self.sw.image = self.sw.i
                if self.help.l_r.collidepoint(event.pos):
                    self.help1 = True
                if self.help.l2_r.collidepoint(event.pos):
                    self.help1 = False
    def update_screen(self):
        self.sc.blit(self.a,self.a.get_rect())
        self.sc.blit(self.b,self.br)
        self.ene.draw(self.sc)
        if self.start and self.start1 and not self.win:
            for bullets in self.bullet.sprites():
                bullets.draw_b()
            for i in self.a_b.sprites():
                i.d_a_b()
            self.box.d_h()
            self.box.update()
        else:
            self.button.d_b()
            self.help.d_l()
        for ii in self.base.sprites():
            ii.d_ba()
            if self.start and self.start1:
                ii.update()
                if ii.c_e():
                    if self.b_d:
                        self.b_d = False
                    else:
                        self.b_d = True
        if self.start and self.dz2:
            self.skills.d_g()
        if self.win:
            font = pg.font.Font("C:\\Windows\\Fonts\\STXINGKA.TTF",30)
            win = font.render("胜利！",True,(255,255,250))
            w_r = win.get_rect()
            w_r.y,w_r.x = 300,350
            self.sc.blit(win,w_r)
        self.sw.d_i()
        self.s_b.s_h_s()
        self.s_b.s_s_i()
        self.s_b.s_l_i()
        self.s_b.s_li_i()
        self.li.c_d()
        if self.s_s1:
            self.sh.d_g()
        if self.help1:
            self.help.d_help()
        pg.display.flip()
    def check_key_down(self,event):        
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.lm = True
        elif event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.rm = True
        elif event.key == pg.K_f:
            self.f_b()
        elif event.key == pg.K_q:
            if os.path.exists("D:\\"):
                with open("D:\\score","w") as f:
                    f.write(str(self.high_score))
            else:
                with open("C:\\Users\\Public\\score") as f:
                    f.write(str(self.high_score))
            pg.quit()
            sys.exit()
        elif event.key == pg.K_SPACE:
            if self.dz > 0:
                self.dz -= 1
                self.dz2 = True
        elif event.key == pg.K_h:
            if self.s_s > 0:
                self.s_s -= 1
                self.s_s1 = True
                self.li.image = self.li.s_l
                self.s_l = 10
                self.s_b.p_li()
                self.li.c_d()
    def check_key_up(self,event):
        if event.key == pg.K_a or event.key == pg.K_LEFT:
            self.lm = False
        elif event.key == pg.K_d or event.key == pg.K_RIGHT:
            self.rm = False
    def f_b(self):
        bull = Bullet(self)
        self.bullet.add(bull)
    def c_f(self):
        for ii in range(4):
            for i in range(self.en - 1):
                al = Enemy(self)
                al.x = i * 80 + 80
                al.rect.x = al.x
                al.rect.y = 45 + 25 * 2 * ii
                self.ene.add(al)
        self.u_a_b()
    def c_f_e(self):
        for i in self.ene.sprites():
            if i.c_e():
                self.fl_d *= -1
                break
    def u_a_b(self):
        for i in self.ene.sprites():
            a = A_B(self)
            if self.level > 9:
                a.d = pg.image.load("bullet2.png")
            elif self.level > 4:
                a.d = pg.image.load("bullet.png")
            a.d_r.x = i.rect.x
            a.d_r.top = i.rect.bottom
            self.a_b.add(a)
    def u_b(self):
        for i in range(2):
            for ii in range(5):
                b = Base(self)
                b.e_r.x = b.e_r.y - 50 * ii
                if i == 1:
                    b.e_r.y += 50
                self.base.add(b)
    def dz1(self):
        if self.dz2:
            self.skills.change()
try:
    A_I()
except SystemExit:
    pass
except:
    print("代码有问题，回车")
    traceback.print_exc()
    input()