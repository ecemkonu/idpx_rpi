from guizero import App, Box, Text, PushButton, Combo, Slider
from gpiozero import LED, Button
import random

led_pins = [17, 22, 23]
button_pins = [5, 6, 16]
leds = []
buttons = []
button_states = [0, 0, 0]
for led_pin in led_pins:
    leds.append(LED(led_pin))
    
for button_pin in button_pins:
    buttons.append(Button(button_pin))

def b1_pressed(button):
    button_states[0] += 1
    button_states[0] = button_states[0] % 2

def b2_pressed(button):
    button_states[1] += 1
    button_states[1] = button_states[1] % 2

def b3_pressed(button):
    button_states[2] += 1
    button_states[2] = button_states[2] % 2



buttons[0].when_pressed = b1_pressed
buttons[1].when_pressed = b2_pressed
buttons[2].when_pressed = b3_pressed

def light_led_at_random(leds):
    led = random.choice(leds)
    led.on()

def switch_screen(switch_to):
    hide_all()        
    switch_to.show()
    if switch_to == option2:
        text2.after(2000, diagnostic_found)
    if switch_to == option0:
        light_led_at_random(leds)

    
def hide_all():
    for screen in all_screens:
        screen.hide()

def show_routine(selected_value):
    #set one of the lights randomly before
    if selected_value == "E1":
        routine_1()
    elif selected_value == "E2":
        routine_2()
    else:
        routine_3()

def enable_option4():
    option4_button.enable()


def d1_s3():
    text4.value = "Step 3: Press button 3"
    text4.after(3000, enable_option4)

def d1_s2():
    text4.value = "Step 2: Rotate the arm to the left"
    text4.after(3000, d1_s3)

def diagnostic_1():
    prev_state = button_states[0]
    text4.value= "Step 1: Press Button 1"
    switch_screen(option4)
    text4.after(3000, d1_s2)

"""
def diagnostic_2():
    text4.value = "Step 1: Press Button 3"
    switch_screen(option4)
    ## Controller to up
    ## Press button 2
    ## controller to left
    None
"""

def routine_1():
    text5.value = "Press B1 once"
    text6.value = "Turn rotating arm clockwise for 1 turn"
    text7.value = "Press B3 twice"
    switch_screen(option5)
    leds[0].off()

def routine_2():
    text5.value= "Turn rotating arm anti-clockwise for 1 turn"
    text6.value = "Press B2 twice"
    text7.value = "Turn rotating arm to the left"
    switch_screen(option5)
    leds[1].off()

def routine_3():
    text5.value = "Press B3 once"
    text6.value = "Turn the rotating arm to the right"
    text7.value = "Press B1 once"
    switch_screen(option5)
    leds[2].off()

def show_diagnostic(selected_value):
    if selected_value == "Yes":
        if random.random() < .5:
            diagnostic_1()
        else:
            # diagnostic_2()
            diagnostic_1() 
    else:
        switch_screen(option0)

def diagnostic_found():
    text2.value = 'Diagnostic found, do you want to walk through?'
    combo2 = Combo(option2, options=["Yes", "No"], align="bottom", command=show_diagnostic)

app = App("Maintanance Helper")

# Create a blank list to hold all the different screens
all_screens = []

# Add space at the top of the buttons
spacer_box = Text(app, text="", width=30, height=1)

# Create a box to contain the menu buttons
menu = Box(app)
menu.tk.width = 900
menu.bg = "light blue"

# Add space at the bottom of the buttons
spacer_box_2 = Text(app, text="", width=30, height=1)

# Option 0 box
option0 = Box(app, width='fill')
text0 = Text(option0, "Welcome to the Maintanance Helper")
all_screens.append(option0)


# Option 1 box
option1 = Box(app, width='fill')
### light one of the leds randomly

text1 = Text(option1, text="Select the error that you want to fix", align="bottom")
combo = Combo(option1, options=["E1", "E2", "E3"], align="bottom", command=show_routine)
all_screens.append(option1)

# Option 2 box
option2 = Box(app)
text2 = Text(option2, text="Running Diagnostic...")
all_screens.append(option2)

# Option 3 box
option3 = Box(app)
text3 = Text(option3)
all_screens.append(option3)

# Option 4 box
option4 = Box(app)
text4 = Text(option4)
option4_button = PushButton(option4, text="Completed", command=switch_screen, args=[option0], align="left")
option4_button.disable()

all_screens.append(option4)

# Option 5 box
option5 = Box(app)
text5 = Text(option5)
text6 = Text(option5)
text7 = Text(option5)
button5 = PushButton(option5, text="Complete", command=switch_screen, args=[option0], align="bottom")
all_screens.append(option5)

# Add the screens to the menu box
option1_button = PushButton(menu, text="Maintanance Routines", command=switch_screen, args=[option1], align="left")
option2_button = PushButton(menu, text="Run Diagnostics", command=switch_screen, args=[option2], align="left")

# Hide all screens and then show the first one
hide_all()
all_screens[0].show()
light_led_at_random(leds)
app.display()