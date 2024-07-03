import requests

def randomword():
    response = requests.get("https://api.urbandictionary.com/v0/random")
    api_data=response.json()['list'][3]
    print(api_data)
    word_defenition=api_data['definition']
    word=api_data['word']
    print('\n'+word+'\n')
    print(word_defenition+'\n')

def wordData(word):
    response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
    api_data=response.json()
    defenition = (api_data)['list'][0]['definition']
    return defenition


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Text Rendering Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load a font
base_font = pygame.font.Font(None, 32)
Title_font = pygame.font.Font(None, 42)
subTitle_font = pygame.font.Font(None, 20)
heading_text="welcome to dictionary"
subHeading="please enter a word and\npress enter to know  its \nmeaning"
user_text=''

#Rect
InputRect=pygame.Rect(60,100,300,32)
#                      x,y width,height
ButtonRect=pygame.Rect(65,160,100,45)


Color_active=pygame.Color('lightskyblue3')
Color_passive=pygame.Color('gray15')
Color=Color_passive
active=False
btn_color=Color
textbx_color=Color
# Main loop
while True:

    mousePose=pygame.mouse.get_pos()
   # print(mousePose)
    if InputRect.collidepoint(mousePose):
        active=True
        textbx_color=Color_active
    else:
        active=False
        textbx_color=Color_passive

    if ButtonRect.collidepoint(mousePose):
        btn_color=Color_active 
    else:
       btn_color=Color_passive
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if active ==1:
            
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ButtonRect.collidepoint(event.pos):
                if user_text:                    
                    defenition=wordData(user_text)
                        
    
    # Clear the screen
    screen.fill(WHITE)
    
    pygame.draw.rect(screen,textbx_color,InputRect,3)
    pygame.draw.rect(screen,btn_color,ButtonRect)

    # Render text
    text_surface = base_font.render(user_text, True, BLACK)
    text_surface1 = Title_font.render(heading_text, True, BLACK)
    text_surface2 = subTitle_font.render(subHeading, True, BLACK)
    text_surface3 = subTitle_font.render("ENTER", True, WHITE)

    screen.blit(text_surface1, (60, 30))
    screen.blit(text_surface2, (350, 160))
    screen.blit(text_surface, (InputRect.x+10, InputRect.y+5))
    screen.blit(text_surface3, (ButtonRect.x+10, ButtonRect.y+13))

    #input text dynamic width
    InputRect.width=max(250,text_surface.get_width()+15)

    # Update the display
    pygame.display.flip()


