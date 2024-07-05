import turtle
import time
from random import random
from random import choice

#Global variables
sayac_click = 0 # Skoru tutan değişken
Turtle_wide = 150 # oyun alanının belirleyen değişken
pos_list = [] # Değişken konumları saklayan liste
game_over = False # Oyunun bittiğini belirten boolean değişken.
cizim_done = False
yuksek_skor = [0]
new_game_choise = ""
new_game_status = False
game_time = 5

# screen ayarları
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Kaplumbağayı yakala")

# Oyun süresini soran turtle
game_time_turtle =turtle.Turtle()
game_time_turtle.hideturtle()

def ask_game_time():
    global game_time
    game_time_turtle.clear()
    game_time = game_area.screen.numinput("Oyun Süresi(s) ", "Min:5 Max:60", minval=5, maxval=60)

# Oyun alanını çizen turtle
game_area = turtle.Turtle()
# Alan çiziliyor mesaj turtle'ı
alan_mes = turtle.Turtle()
# Yüksek skor yazma turtle'ı
skor_max = turtle.Turtle()
skor_max.hideturtle()
# Yeni Oyun turtle
new_game = turtle.Turtle()
new_game.hideturtle()
#score turtle
score_yazi = turtle.Turtle()
#count down turtle
count_down_turtle = turtle.Turtle()
count_down_turtle.hideturtle()
# Ekranda rasstgele görüntülenecek turtle ayarları
turtle1 = turtle.Turtle()
turtle1.penup()
turtle1.shape("turtle")
turtle1.color("green")
turtle1.shapesize(2, 2)

def skor_yaz():
    global yuksek_skor
    yuksek_skor.sort(reverse=True)
    skor_max.clear()
    ekran_wide = score_yazi.screen.window_width() / 2
    ekran_height = score_yazi.screen.window_height() / 2
    skor_max.teleport(-ekran_wide*0.8, ekran_height * 0.8)
    skor_max.write(f"Yüksek \nSkor: {yuksek_skor[0]}", move=False, font=('monaco', 15, 'bold'), align='center')



# Yeni oyuna başlansın mı? Sorusu sorulan fonksiyon.
def new_game_ask():
    global game_over
    global new_game_choise
    global new_game_status
    global sayac_click
    new_game_choise=new_game.screen.textinput("Yeni Oyun?","Yeniden oynamak ister misiniz?(e/h)")
    while (new_game_choise != "e" and new_game_choise != "h"):
        new_game_choise = new_game.screen.textinput("Yeni Oyun?", "Yeniden oynamak ister misiniz?(e/h)")
    if new_game_choise == "e":
        new_game_status = True
        game_over = False
        sayac_click = 0
        print(new_game_choise)
        score_yazi.clear()
        turtle1.clear()
        count_down_turtle.clear()
        game_area.clear()
        start_game_up()
    elif new_game_choise == "h":
        new_game_status = False
        screen.bye()

def countdown(sure=5):
    global game_over
    global new_game_status
    global cizim_done
    global sayac_click
    count_down_turtle.hideturtle()
    count_down_turtle.screen.update()
    ekran_hight = score_yazi.screen.window_height() / 2
    count_down_turtle.teleport(0, ekran_hight * 0.8)
    count_down_turtle.clear()
    if sure > 0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time: {sure}", move=False, font=('monaco', 20, 'bold'), align='center')
        screen.ontimer(lambda: countdown(sure - 1),1000)
    else:
        game_over = True
        new_game_status = False
        cizim_done = False
        turtle1.hideturtle()
        count_down_turtle.clear()
        count_down_turtle.write("Game Over !!!", move=False, font=('monaco', 20, 'bold'), align='center')
        yuksek_skor.append(sayac_click)
        new_game_ask()
# Score bilgisini yazdığım turtle fonksiyonu
def score_turtle(a=0):
    global sayac_click
    global new_game_status
    score_yazi.hideturtle()
    score_yazi.screen.update()
    ekran_yukseklik = score_yazi.screen.window_height()/2
    score_yazi.teleport(0,ekran_yukseklik*0.9)
    score_yazi.write(f"Score: {a}", move=False, font=('monaco', 20, 'bold'), align='center')


# Kaplumbağaya tıklandığında bu bilgili alan ve sayacı 1 artıran fonksiyon.
# score_turtle() çağrılarak ekranda score güncellemesi yapılmıştır.
def click_fonk(Xp,Yp):
    global sayac_click
    sayac_click += 1
    score_yazi.clear()
    score_turtle(sayac_click)
    print(sayac_click)

def random_pos():
    global pos_list
    Xpos = int(random() * Turtle_wide)
    Xpos_neg = int(random() * -Turtle_wide)
    Ypos = int(random() * Turtle_wide)
    Ypos_neg = int(random() * -Turtle_wide)
    pos_list = [Xpos, Ypos, Xpos_neg, Ypos_neg]

# Aşağıda yazılan fonksiyonun içinde kendisini çağırıyoruz.
# screen.ontimer(show_turtle,600) komutla show_turtle fonksiyonunun 600ms
# boyunca çalıştırıp durduruyoruz.ontimer devamlı çalışan bir komut olmadığından bu şekilde yazdık.
# Bu şekildeki yapıya RECURSIVE FUNCTION deniyor. Yani fonksiyonun içinde kendisini çağırmak.
# Bu şekilde bir fonksiyon yazılırsa mutlaka bir çıkış şartının olması gerekir.
# Çıkış şartı yazılmazsa sistem sonsuz döngüde kalır. Yani bi yerde bir if satırıyla döngüden çıkmamız lazım.
def show_turtle():
    if not game_over:
        random_pos()
        turtle1.showturtle()
        X = int(choice(pos_list))
        Y = int(choice(pos_list))
        turtle1.teleport(X, Y)
        turtle1.onclick(click_fonk, 1)
        screen.ontimer(show_turtle,600)

def cizim_mes():
    global cizim_done
    alan_mes.teleport(0,300)
    alan_mes.hideturtle()
    if cizim_done == False:
        alan_mes.write("Oyun Alanı Çiziliyor...", move=False, font=('monaco', 20, 'bold'), align='center')
    else:
        alan_mes.clear()

def game_area_border():
    global cizim_done
    global Turtle_wide
    game_area.clear()
    game_area.showturtle()
    game_area.pendown()
    Turtle_wide=game_area.screen.numinput("Oyun Alanını Belirleyin ","Min:100 Max:200",minval=100,maxval=200)
    game_area.teleport(Turtle_wide+70, Turtle_wide+70)
    game_area.pensize(3)
    game_area.pencolor("red")
    game_area.fillcolor("light green")
    game_area.begin_fill()
    for ciz in range(4):
        game_area.right(90)
        game_area.forward((Turtle_wide*2)+70)
    cizim_done = True
    game_area.penup()
    game_area.hideturtle()
    game_area.end_fill()

# Oyunu çalıştıran fonksiyonları içeren genel fonksiyon
def start_game_up():
    cizim_mes()
    game_area_border()
    ask_game_time()
    cizim_mes()
    countdown(game_time)
    score_turtle() # score = 0 yazmak için ilk çağırmayı yaptım.
    show_turtle()
    skor_yaz()

start_game_up()


turtle.mainloop()