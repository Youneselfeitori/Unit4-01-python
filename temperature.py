# Created by: Younes Elfeitori
# Created on: Nov 2017
# Created for: ICS3U
# This program converts celsius to fahrenheit
import ui

def calculate_temperature(celsius):
    fahrenheit = 1.8 * celsius + 32
    view['answer_label'].text = "Input temperature in celsius to convert to fahrenheit : " + str(fahrenheit) 
    # the section above calculates celsius to fahrenheit


def celsius_to_fahrengeit_button_touch_up_inside(sender):
    celsius = int(view['celsius_textfield'].text)
    calculate_temperature(celsius)
 # The section above converts celsius to fahrenheit

view = ui.load_view()
view.present('full_screen')

