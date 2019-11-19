#Импортируем необходимые библиотеки
from pygame import *
import random

#Создаем класс спрайтов
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
def Intersect(s1_x, s1_y, s2_x, s2_y):
    if(s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 100) and (s1_y < s2_y + 100):
        return 1
    else:
        return 0
#Будим пайгейм
init()
#Экран
screen = display.set_mode((640,480))
display.set_caption(("Grand Turismo Sport Premium 2D Edition™"))
#Музыка
mixer.music.load("Action Trailer.mp3")
mixer.music.play(-1)
#Импорт спрайтов
#Машина игрока
playercar = Sprite(20, 400, "car_player.png")
#Машина соперника
enemycar = Sprite(random.randrange(100, 500), 0, "car_enemy.png")
#Деревья
tree1 = Sprite(10,0, "tree.png")
tree2 = Sprite(550, 240, "tree.png")
#Дорожная разметка
whiteline1 = Sprite(315, 0, "whiteline.png")
whiteline2 = Sprite(315, 240, "whiteline.png")
#Счет
scorefont = font.Font(None, 69)
#Звук аварии
crasheffect = mixer.Sound("crash.wav")
#Добавим несколько переменных
score = 0
maxscore = 0
quit = 0
#Ура! Основной цикл игры
while quit == 0:
    #Фон
    screen.fill((0, 200, 0))
    screen.fill((200, 200, 200), ((100, 0), (440, 480)))
    #Инициализируем наши спрайты 
    #Деревья
    tree1.render()
    tree1.y += 10
    if (tree1. y > 480):
        tree1.y = - 110
    tree2.render()
    tree2.y += 10
    if (tree2.y > 480):
        tree2.y = -110
    #Дорожная разметка
    whiteline1.render()
    whiteline1.y += 10
    if (whiteline1. y > 480):
        whiteline1.y = -80
    whiteline2.render()
    whiteline2.y += 10
    if (whiteline2.y > 480):
        whiteline2.y = -80
    #Машина соперника
    enemycar.render()
    enemycar.y += 100
    if (enemycar.y > 480):
        enemycar.y = -100
        enemycar.x = random.randrange(100, 500)
    #Пришла пора поработать с мышью
    #Получаем местоположение мыжи и добавляем ему ограничения
    x, y = mouse.get_pos()
    if (x < 100):
        x = 100
    if (x > 500):
        x = 500
    #Привязываем машину игрока к мыши
    playercar.x = x
    playercar.render()
    #Выводим на экран счетчик очков
    scoretext = scorefont.render("Score: " + str(score), True, (255, 255, 255), (0, 0, 0))
    screen.blit(scoretext, (5, 5))
    #Делаем проверку на столкновение машины игрока и машины соперника
    if (Intersect(playercar.x, playercar.y, enemycar.x, enemycar.y)):
        mixer.Sound.play(crasheffect)
    #меняем максимальное количество очков
        if (score > maxscore):
            maxscore = score
        score = 0
    #Делаем возможным выход из игры
    for ourevent in event.get():
        if ourevent.type == QUIT:
            quit = 1
    #Добавляем задержку
    time.delay(15)
    #Прибавляем очки
    score += 1
    #выводим максимальное количество очков
    print("Your max score is: ", maxscore)
    #Обновляем окно
    display.update()
    #Усеееееееее!
    
    
    
    
    
                
    
    

    
    
        
    


    
    
    
    
    
