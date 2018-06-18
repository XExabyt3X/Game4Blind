import pip
import os
import random
import pygame
import webbrowser
from gtts import gTTS
pygame.init()
clock = pygame.time.Clock()
class Ding(object):
    def __init__(self):
        pygame.mixer.quit()
    def play_note(self, frequency, prefrequency):
        if not frequency == prefrequency:
            pygame.mixer.quit()
        pygame.mixer.init(frequency)
        pygame.mixer.music.load("piano.mp3")
        pygame.mixer.music.play()

'''ik it's a game for blind people but come on, a blank screens pretty boring for "non-blind". ;)'''
        
class Colour(object):
    def __init__(self, start_pos, xywh): #xywh = x y width height #start_pos min 0 max 153
        self.xywh = xywh
        if start_pos < 0 or start_pos > 153:
            raise Exception("Error: " + self + " = Colour(" + str(start_pos) + ")\nstart_pos either above 153 or below 0")
            os._exit(0)
        elif start_pos <= 51:
            self.colour = [255 - start_pos * 5, 255, start_pos * 5]
            self.increase = [False, False, True]
            self.decrease = [True, False, False]
        elif start_pos <= 102:
            start_pos /= 2
            self.colour = [255, start_pos * 5, 255 - start_pos * 5]
            self.increase = [False, True, False]
            self.decrease = [False, False, True]
        else:  #elif start_pos <= 153:
            start_pos /= 3
            self.colour = [start_pos * 5, 255 - start_pos * 5, 255]
            self.increase = [True, False, False]
            self.decrease = [False, True, False]
    def draw(self):
        if self.colour[0] == 255 and self.colour[1] == 255 and self.colour[2] == 0:
            self.increase[2] = True
            self.decrease[0] = True
        if self.colour[0] == 0 and self.colour[1] == 255 and self.colour[2] == 255:
            self.increase[0] = True
            self.decrease[1] = True
        if self.colour[0] == 255 and self.colour[1] == 0 and self.colour[2] == 255:
            self.increase[1] = True
            self.decrease[2] = True
        for i in range(3):
            if self.increase[i]:
                self.colour[i] += 5
                if self.colour[i] >= 255:
                    self.colour[i] = 255
                    self.increase[i] = False
            if self.decrease[i]:
                self.colour[i] -= 5
                if self.colour[i] <= 0:
                    self.colour[i] = 0
                    self.decrease[i] = False
        pygame.draw.rect(screen, self.colour, self.xywh)

'''ik it's a game for blind people but come on, a blank screens pretty boring for "non-blind". ;)'''
        
def loading():
    SCREEN_SIZE = pygame.display.set_mode()
    SCREEN_SIZE = SCREEN_SIZE.get_size()
    WINDOW_SIZE = [400, 300]
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (SCREEN_SIZE[0]/4,SCREEN_SIZE[1]/4)
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.NOFRAME)
    font_1 = pygame.font.SysFont("Arial", 30)
    file_name_to_load = [
            "toofar_left.mp3", "toofar_right.mp3", "toofar_up.mp3", "toofar_down.mp3",
            "finlvl.mp3", "thankyou.mp3", "youwin.mp3", "lvl1.mp3", "lvl2.mp3", "lvl3.mp3", "lvl4.mp3",
            "lvl5.mp3", "lvl6.mp3", "lvl7.mp3"
        ]
    file_path_to_load = []
    for i in file_name_to_load:
        file_path_to_load.append(os.path.join("Assets", i))
    file_data_to_load = [
            "You've gone too far left", "You've gone too far right", "You've gone too far up", "You've gone too far down",
            "You followed the sound to the correct spot",
            "Thank you for playing my game. Please take the time to do this feedback survey at https colon slash slash g o o dot g l slash forms slash 75EkF5X8VZ2lhhtb2. Click the X to close the program.",
            "You completed my game! Great job! It would be greatly appriciated if you send the tiny url link to others.", "Level 1", "Level 2", "Level 3", "Level 4", "Level 5",
            "Level 6", "Level 7"
        ]
    count = 0
    if not os.path.exists("Assets"):
        os.mkdir("Assets")
    for curr_file in file_name_to_load:
        screen.fill([0, 0, 0])
        pygame.draw.rect(screen, [255, 255, 255], [5, 5, 390, 290])
        text_1 = font_1.render("Loading "+curr_file+"...", False, [0, 0, 0])
        screen.blit(text_1, [10, 10])
        pygame.display.flip()
        if not os.path.exists(file_path_to_load[count]):
            tts = gTTS(text=file_data_to_load[count], lang="en")
            tts.save(file_path_to_load[count])
        count += 1
def say(text_to_say):
    pygame.mixer.quit()
    pygame.mixer.init(27562)
    quit_mixer = True
    if os.path.exists(os.path.join("Assets", text_to_say)):
        try:
            pygame.mixer.music.load(os.path.join("Assets", text_to_say))
        except:
            raise Exception("Error: File Assets\\"+text_to_say+" was unable to be loaded")
        pygame.mixer.music.set_volume(1.0)
        if text_to_say == "finlvl.mp3":
            pygame.mixer.music.play()
            pygame.time.delay(3200)
        elif text_to_say == "thankyou.mp3" or text_to_say == "youwin.mp3":
            pygame.mixer.music.play(-1)
            quit_mixer = False
        else:
            pygame.mixer.music.play()
            pygame.time.delay(2200)
    else:
        raise Exception(os.path.join("Assets", text_to_say) + " doesn't exist. idk fam")
    if quit_mixer:
        pygame.mixer.quit()
loading()
WINDOW_SIZE = (550, 550)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game4Blind")
all_the_colours = []
j = WINDOW_SIZE[0]/52
k = WINDOW_SIZE[1]/52
for i in range(52):
    all_the_colours.append(Colour(i, [i*j/2, i*k/2, WINDOW_SIZE[0] - i*j, WINDOW_SIZE[1] - i*k]))
GridSize = 1 #Will become 2 later
NewRound = True
Goal_Pos = [1, 1]
Player_Pos = [1, 1]
Distance = 1
Tone = 0
piano = Ding()
done = False
while not done:
    if Goal_Pos[0] > Player_Pos[0]:
        Distance = Goal_Pos[0] - Player_Pos[0]
    elif Goal_Pos[0] < Player_Pos[0]:
        Distance = Player_Pos[0] - Goal_Pos[0]
    else:
        Distance = 0
    if Goal_Pos[1] > Player_Pos[1]:
        Distance += Goal_Pos[1] - Player_Pos[1]
    elif Goal_Pos[1] < Player_Pos[1]:
        Distance += Player_Pos[1] - Goal_Pos[1]
    else:
        Distance += 0
    Distance += GridSize
    Pretone = Tone
    Tone = int((GridSize/Distance)*50000+22050)
    piano.play_note(Tone, Pretone)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    PressKey = pygame.key.get_pressed()
    if PressKey[pygame.K_LALT] and PressKey[pygame.K_F4]:
        done = True
    if PressKey[pygame.K_w] or PressKey[pygame.K_UP]:
        if Player_Pos[1] == 1:
            say("toofar_up.mp3")
        else:
            Player_Pos[1] -= 1
    if PressKey[pygame.K_s] or PressKey[pygame.K_DOWN]:
        if Player_Pos[1] == GridSize:
            say("toofar_down.mp3")
        else:
            Player_Pos[1] += 1
    if PressKey[pygame.K_a] or PressKey[pygame.K_LEFT]:
        if Player_Pos[0] == 1:
            say("toofar_left.mp3")
        else:
            Player_Pos[0] -= 1
    if PressKey[pygame.K_d] or PressKey[pygame.K_RIGHT]:
        if Player_Pos[0] == GridSize:
            say("toofar_right.mp3")
        else:
            Player_Pos[0] += 1
    for i in range(52):
        all_the_colours[i].draw()
    pygame.display.flip()
    if NewRound:
        NewRound = False
        if GridSize != 2**7:
            GridSize *= 2
        else:
            #COMPLETE GAME
            say("youwin.mp3")
            credit = False
            while not credit:
                KeyPress = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        credit = True
                if KeyPress[pygame.K_LALT] and KeyPress[pygame.K_F4]:
                    credit = True
            webbrowser.open_new("https://goo.gl/forms/75EkF5X8VZ2lhhtb2")
            while True:
                #Credits
                font_1 = pygame.font.SysFont("Comic Sans MS", 21)
                text_thanks = [
                    font_1.render("Thank you for playing my game.", False, [0, 0, 0]),
                    font_1.render("Please take the time to do this feedback survey:", False, [0, 0, 0]),
                    font_1.render("https://goo.gl/forms/75EkF5X8VZ2lhhtb2", False, [0, 0, 0]),
                    font_1.render("Click the X again to close the program.", False, [0, 0, 0])
                    ]
                screen.fill([255, 255, 255])
                pos = 75
                for curr_text in text_thanks:
                    screen.blit(curr_text, [40, pos])
                    pos += 35
                pygame.display.flip()
                say("thankyou.mp3")
                while not done:
                    KeyPress = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                    if KeyPress[pygame.K_LALT] and KeyPress[pygame.K_F4]:
                        done = True
                break
                #Credits
            #COMPLETE GAME            
        #SAY LEVEL
        if not done:
            if GridSize == 2:
                say("lvl1.mp3")
            elif GridSize == 4:
                say("lvl2.mp3")
            elif GridSize == 8:
                say("lvl3.mp3")
            elif GridSize == 16:
                say("lvl4.mp3")
            elif GridSize == 32:
                say("lvl5.mp3")
            elif GridSize == 64:
                say("lvl6.mp3")
            elif GridSize == 128:
                say("lvl7.mp3")
        #SAY LEVEL
        Goal_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
        Player_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
        while True:
            if Player_Pos == Goal_Pos:
                Goal_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
                Player_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
            else:
                break
    if Player_Pos == Goal_Pos:
        say("finlvl.mp3")
        NewRound = True
pygame.quit()
