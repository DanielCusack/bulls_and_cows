'''
This is a number guessing where the player has to guess a 4 digit random number
where no digit has the same number. The goal of the player is to guess the right
number within 10 guesses. 
After each guess, the player is given feedback on howclose there guess is to the
real number. If the a guess shares a digit with the actual number, then this is
counted as a hit. If the guess shares a number with the actual number but not a
digit, then it is counted as a blow.

For example:
Actual number = 1234
guess         = 1743
In this case guess has 1 hit and 2 blows

'''

import sys
from objects import *

pygame.init()

#------------------------------------------
#Variables of the program
running = True
ww, wh = 640, 480
space=int(ww/32)
#------------------------------------------

def create_window(ww,wh):
    'Create the display window'
    window_width, window_height = ww,wh
    window_title='Bulls and Cows'
    pygame.display.set_caption(window_title)
    return pygame.display.set_mode((window_width, window_height))

def arrange_button(screen, width, height, colour, horiz, vert, spacing):
    'Place number buttons 0 to 9 in a neat fashion'
    buttonlist=[]
    #Place zero button
    buttonlist.append(Number_Button(width, height, (horiz+(width+spacing), vert), colour, '0'))
    buttonlist[-1].make_button()
    buttonlist[-1].place_button(screen)
    #Place buttons 1-9
    for v in range(1,4):
        for h in range(3):
            number = (3*(v-1))+(h+1)
            pos = (horiz+h*(width+spacing), vert+v*(height+spacing))
            buttonlist.append(Number_Button(width, height, pos, colour, str(number)))
            buttonlist[-1].make_button()
            buttonlist[-1].place_button(screen)
    
    return buttonlist


window= create_window(ww,wh)
window.fill((255,255,255))

state= State()
state.set_real_number()

button_list = arrange_button(window, int(ww/16), int(wh/16), (100, 200, 50), int(ww*3/8), int(0.55*wh), space)

quit_button = Quit_Button(int(ww*1/8), int(wh/16), (int(ww*13/16),int(wh*13/16)), (150, 50, 50))
quit_button.make_button()
quit_button.place_button(window)
button_list.append(quit_button)

clear_button = Clear_Button(int(ww*1/8), int(wh/16), (int(ww*13/16),int(wh*11/16)), (50, 50, 150))
clear_button.make_button()
clear_button.place_button(window)
button_list.append(clear_button)

input_button = Input_Button(int(ww*1/8), int(wh/16), (int(ww*7/16),int(wh*7/16)), (50, 150, 150))
input_button.make_button()
input_button.place_button(window)
button_list.append(input_button)

score_board = Score_Board(int(ww*3/8), int(wh/8), (int(ww*5/16),int(wh*1/16)), (100, 100, 100))
score_board.colour_board()
score_board.score_display(window)

input_board = Input_Board(int(ww*1/4), int(wh/8), (int(ww*3/8),int(wh*2/8)), (100, 100, 100))
input_board.colour_board()
input_board.number_display(window)

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                running = False

        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            for button in button_list:
                if button.collisionrect.collidepoint(mouse) and isinstance(button, Number_Button) and button.pushed == False and input_board.inputted_digits != 4:
                    #Add digit to guess
                    button.button_clicked(window)
                    input_board.update_number(window, button.text)
                    pygame.display.update()

                if button.collisionrect.collidepoint(mouse) and isinstance(button, Quit_Button):
                    #Quit the game
                    running = False

                if button.collisionrect.collidepoint(mouse) and isinstance(button, Clear_Button):
                    #Clear the input board and unpush the number buttons to reset the guess
                    input_board.reset_board(window)
                    for i in button_list:
                        if isinstance(i, Number_Button) and i.pushed == True:
                            i.button_clicked(window)
                    pygame.display.update()

                if button.collisionrect.collidepoint(mouse) and isinstance(button, Input_Button) and input_board.inputted_digits == 4:
                    #Check the guess and give feedback. Reset the the input board and number buttons
                    score_board.update_board(window, *state.hit_blow_checker(input_board.number_list))
                    input_board.reset_board(window)
                    for i in button_list:
                        if isinstance(i, Number_Button) and i.pushed == True:
                            i.button_clicked(window)
                    pygame.display.update()
    
    if state.guesses_used == state.total_guess_number or score_board.hit == 4:
        if score_board.hit == 4:
            score_board.colour_board()
            score_board.add_text('You Win!', int(score_board.width/2), int(score_board.height/2))
            score_board.place_board(window)
            pygame.display.update()
            pygame.time.wait(1000)
        else:
            score_board.colour_board()
            score_board.add_text('You Lose!', int(score_board.width/2), int(score_board.height/2))
            score_board.place_board(window)
            pygame.display.update()
            pygame.time.wait(1000)
        
        score_board.reset_board(window)
        input_board.reset_board(window)
        for i in button_list:
            if isinstance(i, Number_Button) and i.pushed == True:
                i.button_clicked(window)
        state.reset_state()
        pygame.display.update()


pygame.quit()
sys.exit()