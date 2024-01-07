from guizero import App, Box, Text, PushButton, Combo, Slider
from gpiozero import LED
import random

led_pins = [17, 22, 23]
button_pins = [12, 14, 17]
leds = []

for led_pin in led_pins:
    leds.append(LED(led_pin))

def light_led_at_random(leds):
    led = random.choice(leds)
    led.on()

def switch_screen(switch_to):
    hide_all()        
    switch_to.show()
    if switch_to == option2:
        text2.after(2000, diagnostic_found)
    
def hide_all():
    for screen in all_screens:
        screen.hide()

def show_routine(selected_value):
    #set one of the lights randomly before
    if selected_value == "E1":
        text3.value = "You chose...wisely"
    else:
        text3.value = "You chose...poorly"
    switch_screen(option3)

def diagnostic_1():
    ## Press button 1
    ## Press button 3
    ## Rotate arm , write it as text and then rotate, say its completed without logic

    None

def diagnostic_2():
    ## Controller to up
    ## Press button 2
    ## controller to left
    None


def routine_1():
    None

def routine_2():
    None

def routine_3():
    None

def show_diagnostic(selected_value):
    if selected_value == "Yes":
        text4.value= "Step 1:"
        switch_screen(option4)
    else:
        switch_screen(option0)
        light_led_at_random()

def diagnostic_found():
    text2.value = 'Diagnostic found, do you want to walk through?'
    combo2 = Combo(option2, options=["Yes", "No"], align="bottom", command=show_diagnostic)

app = App("Maintanance Helper", layout="grid")

# Create a blank list to hold all the different screens
all_screens = []

# Create a box to contain the menu buttons
menu = Box(app, grid=[0,0], layout="grid")
menu.tk.width = 900
menu.bg = "light blue"

# Option 0 box
option0 = Box(app, width='fill', grid=[1,1])
text0 = Text(option0, "Welcome to the Maintanance Helper")
all_screens.append(option0)


# Option 1 box
option1 = Box(app, width='fill', grid=[1,1])
### light one of the leds randomly

text1 = Text(option1, text="Select the error that you want to fix", align="bottom")
combo = Combo(option1, options=["E1", "E2", "E3"], align="bottom", command=show_routine)
all_screens.append(option1)

# Option 2 box
option2 = Box(app, grid=[1,1])
text2 = Text(option2, text="Running Diagnostic...")
slider = Slider(option2)
all_screens.append(option2)

# Option 3 box
option3 = Box(app, grid=[1,1])
text3 = Text(option3)
all_screens.append(option3)

# Option 4 box
option4 = Box(app, grid=[1,1])
text4 = Text(option4)
all_screens.append(option4)

# Add the screens to the menu box
option1_button = PushButton(menu, text="Maintanance Routines", command=switch_screen, args=[option1], grid=[0,0], align="left")
option2_button = PushButton(menu, text="Run Diagnostics", command=switch_screen, args=[option2], grid=[1,0], align="left")

# Hide all screens and then show the first one
hide_all()
all_screens[0].show()
light_led_at_random(leds)
app.display()