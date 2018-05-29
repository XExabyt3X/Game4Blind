import pip
try:
    import os
except:
    pip.main(['install', 'os'])
    import os
try:
    import random
except:
    pip.main(['install', 'random'])
    import random
try:
    import pygame
except:
    pip.main(['install', 'pygame'])
    import pygame
try:
    from gtts import gTTS
except:
    pip.main(['install', 'gtts'])
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
    screen = pygame.display.set_mode()
    SCREEN_SIZE = (screen.get_width(), screen.get_height())
    WINDOW_SIZE = [400, 300]
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((SCREEN_SIZE[0]/2)-WINDOW_SIZE[0]*1.5,(SCREEN_SIZE[1]/2)-WINDOW_SIZE[1]*1.5)
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.NOFRAME)
    font_1 = pygame.font.SysFont("Arial", 30)
    file_name_to_load = [
            "toofar_left.mp3", "toofar_right.mp3", "toofar_up.mp3", "toofar_down.mp3",
            "youwin.mp3"
        ]
    file_path_to_load = []
    for i in file_name_to_load:
        file_path_to_load.append(os.path.join("Assets", i))
    file_data_to_load = [
            "You've gone too far left", "You've gone too far right", "You've gone too far up", "You've gone too far down",
            "You followed the sound to the correct spot"            
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
loading()
def say(text_to_say):
    pygame.mixer.quit()
    pygame.mixer.init(27562)
    if os.path.exists(os.path.join("Assets", text_to_say)):
        try:
            pygame.mixer.music.load(os.path.join("Assets", text_to_say))
        except:
            raise Exception("Error: File Assets\\"+text_to_say+" was unable to be loaded")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        if text_to_say == "youwin.mp3":
            pygame.time.delay(3200)
        else:
            pygame.time.delay(2200)
    else:
        raise Exception(os.path.join("Assets", text_to_say) + " doesn't exist. idk fam")
    pygame.mixer.quit()
WINDOW_SIZE = [800, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hey you're not blind!")
all_the_colours = []
for i in range(52):
    all_the_colours.append(Colour(i, [i*7.5, i*7.5, 800 - i*15, 800 - i*15]))
GridSize = 2
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
        GridSize *= 2
        Goal_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
        Player_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
        while True:
            if Player_Pos == Goal_Pos:
                Goal_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
                Player_Pos = [random.randint(1, GridSize), random.randint(1, GridSize)]
            else:
                break
    if Player_Pos == Goal_Pos:
        say("youwin.mp3")
        NewRound = True
pygame.quit()
