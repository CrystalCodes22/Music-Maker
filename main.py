import pygame
#import sys
import threading
import time
import random

pygame.init()

#from pygame.locals import *

start = time.perf_counter()

# Initialize Screen
win = pygame.display.set_mode((1500, 1000), 0, 32)
pygame.display.set_caption("Music Maker")

# Putting in a background image
background = pygame.image.load("backgroundImage (2).jpg").convert()

# Importing Sounds
noteA = pygame.mixer.Sound('Sounds/Piano/a.wav')
noteBFlat = pygame.mixer.Sound('Sounds/Piano/b_flat.wav')
noteB = pygame.mixer.Sound('Sounds/Piano/b.wav')
noteC = pygame.mixer.Sound('Sounds/Piano/c.wav')
noteCSharp = pygame.mixer.Sound('Sounds/Piano/c#.wav')
noteD = pygame.mixer.Sound('Sounds/Piano/d.wav')
noteEFlat = pygame.mixer.Sound('Sounds/Piano/e_flat.wav')
noteE = pygame.mixer.Sound('Sounds/Piano/e.wav')
noteF = pygame.mixer.Sound('Sounds/Piano/f.wav')
noteFSharp = pygame.mixer.Sound('Sounds/Piano/f#.wav')
noteG = pygame.mixer.Sound('Sounds/Piano/g.wav')
noteGSharp = pygame.mixer.Sound('Sounds/Piano/g#.wav')

bassA = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_A3_1_forte_arco-normal.wav')
bassAs = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_As3_1_forte_arco-normal.wav')
bassB = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_B3_1_forte_arco-normal.wav')
bassC = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_C3_1_forte_arco-normal.wav')
bassCs = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_Cs3_1_forte_arco-normal.wav')
bassD = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_D3_1_forte_arco-normal.wav')
bassDs = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_Ds3_1_forte_arco-normal.wav')
bassE = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_E3_1_forte_arco-normal.wav')
bassF = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_F3_1_forte_arco-normal.wav')
bassFs = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_Fs3_1_forte_arco-normal.wav')
bassG = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_G3_1_forte_arco-normal.wav')
bassGs = pygame.mixer.Sound('Sounds/Strings/doublebass/.wav/double-bass_Gs3_1_forte_arco-normal.wav')

#guitar5 = pygame.mixer.Sound('Sounds/Guitar1/guitar5.wav')
# guitar1 = pygame.mixer.Sound('Sounds/Guitar1/guitar1.wav')
# guitar2 = pygame.mixer.Sound('Sounds/Guitar1/guitar2.wav')
# guitar3 = pygame.mixer.Sound('Sounds/Guitar1/guitar3.wav')
# guitar4 = pygame.mixer.Sound('Sounds/Guitar1/guitar4.wav')
# guitar5 = pygame.mixer.Sound('Sounds/Guitar1/guitar5.wav')
# guitar6 = pygame.mixer.Sound('Sounds/Guitar1/guitar6.wav')
# guitar7 = pygame.mixer.Sound('Sounds/Guitar1/guitar7.wav')
# guitar8 = pygame.mixer.Sound('Sounds/Guitar1/guitar8.wav')
# guitar9 = pygame.mixer.Sound('Sounds/Guitar1/guitar9.wav')
# guitar10 = pygame.mixer.Sound('Sounds/Guitar1/guitar10.wav')
# guitar11 = pygame.mixer.Sound('Sounds/Guitar1/guitar11.wav')
# guitar12 = pygame.mixer.Sound('Sounds/Guitar1/guitar12.wav')

buttonsToNotes = {0: noteGSharp, 1: noteA, 2: noteBFlat, 3: noteB, 4: noteC, 5: noteCSharp, 6: noteD, 7: noteEFlat,
                  8: noteE, 9: noteF, 10: noteFSharp, 11: noteG}
buttonsToNotesBass = {0: bassA, 1: bassAs, 2: bassB, 3: bassC, 4: bassCs, 5: bassD, 6: bassDs, 7: bassE, 8: bassF,
                      9: bassFs, 10: bassG, 11: bassGs}


# buttonsToNotesGuitar = {0:guitar1, 1:guitar2, 2:guitar3, 3:guitar4, 4:guitar5, 5:guitar6, 6:guitar7, 7:guitar8, 8:guitar9, 9:guitar10, 10:guitar11, 11:guitar12}

# Button Class
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


# Expanding circles class
class expandingCircle():
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        self.radius += 2


bassVar = False


# Goes through buttons, checks which ones are selected and plays the corresponding sounds
def playOnce():
    counter1 = 0
    vel = 130

    guitarTimeInterval = 4000
    pianoTimeInterval = 700

    global x
    global bassVar

    for b in buttons:
        # print("Counter Value " + str(counter) + " Selected Counter: " + str(selected[counter]))

        # pygame.draw.rect(win, (255, 0, 255), (x, 0, 20, 1000))

        if counter1 % 12 == 0 and counter1 != 0:
            pygame.time.delay(500)
            highlights.clear()

        if selected[counter1]:
            print("Play Sound Note " + str(counter1))
            # pygame.mixer.Channel(counter%12).play(buttonsToNotes[counter%12])

            # Chooses random RGB values to create a random color for the circle effect
            red = random.randint(1, 255)
            green = random.randint(1, 255)
            blue = random.randint(1, 255)

            highlights.append(expandingCircle((red, green, blue), b.x + 15, b.y + 15, 40))
            if not bassVar:
                print(bassVar)
                buttonsToNotes[counter1 % 12].play()

            else:
                print(bassVar)
                buttonsToNotesBass[counter1 % 12].play()

        counter1 += 1

        #    if guitarVar == False:
        #        pygame.time.delay(pianoTimeInterval)
        #    
        #    else:
        #        print("About to delay, and 'guitarVar' is True")
        #        if counter == 0:
        #            print("Delay after playing note '0'")
        #            pygame.time.delay(400)
        #        else:
        #            print("Delay after playing a note other than '0'")
        #            pygame.time.delay(guitarTimeInterval)
        #    x += vel
        #    highlights.clear()
        # counter += 1

    x = 95


# Function to switch sounds to bass
def bass():
    global bassVar
    bassVar = True
    threading.Thread(target=playOnce).start()


# Function to clear grid of buttons when called
def clearGrid():
    counter2 = 0

    for b in selected:
        selected[counter2] = False
        counter2 += 1


# Updates screen
def redrawWindow():
    global x

    for b in buttons:
        b.draw(win, (0, 0, 0))
    playButton.draw(win, (0, 0, 0))
    clearButton.draw(win, (0, 0, 0))
    bassButton.draw((win), (0, 0, 0))
    # pygame.draw.rect(win, (255, 0, 255), (x, 0, 20, 1000))

    for c in highlights:
        c.draw(win)


run = True

x = 95

# Creation of grid of buttons
buttons = []
selected = []
for row in range(12):
    for column in range(12):
        buttons.append(button((136, 0, 255), 130 * row + 100, 130 * column + 120, 30, 30, "MM"))
        selected.append(False)

# Creation of control buttons
playButton = button((0, 255, 0), 645, 50, 90, 40, "Piano!")
clearButton = button((0, 255, 0), 765, 50, 90, 40, "Clear!")
bassButton = button((0, 255, 0), 885, 50, 90, 40, "Bass!")
pygame.mixer.set_num_channels(12)

particles = []
highlights = []

# Main Function
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        # Ablility to quit window
        if event.type == pygame.QUIT:
            run = False

        # Detect if mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter = -1

            if playButton.isOver(pos):
                print("Clicked Piano Button")
                guitarVar = False
                threading.Thread(target=playOnce).start()

            if clearButton.isOver(pos):
                print("Clicked Clear Button")
                clearGrid()

            if bassButton.isOver(pos):
                print("Clicked Bass Button")
                bass()

            for button in buttons:
                counter += 1

                if button.isOver(pos):
                    print("Clicked Button")
                    if not selected[counter]:
                        button.color = (255, 0, 0)
                        selected[counter] = True

                    else:
                        button.color = (0, 255, 0)
                        selected[counter] = False

        # Detect when cursor makes a motion
        if event.type == pygame.MOUSEMOTION:
            counter = -1
            for button in buttons:
                counter += 1

                if playButton.isOver(pos):
                    playButton.color = (64, 0, 255)

                else:
                    playButton.color = (0, 153, 255)

                if clearButton.isOver(pos):
                    clearButton.color = (64, 0, 255)

                else:
                    clearButton.color = (0, 153, 255)

                if bassButton.isOver(pos):
                    bassButton.color = (64, 0, 255)

                else:
                    bassButton.color = (0, 153, 255)

                if button.isOver(pos):
                    if not selected[counter]:
                        button.color = (72, 0, 255)

                else:
                    if not selected[counter]:
                        button.color = (136, 0, 255)

    win.blit(background, (0, 0))
    redrawWindow()

    # Particle effect
    mx, my = pygame.mouse.get_pos()
    particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(win, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    pygame.display.update()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')

pygame.quit()
