def on_button_pressed_a():
    basic.show_number(8)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_arrow(ArrowNames.NORTH_EAST)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_icon(IconNames.HEART)

def on_forever():
    basic.show_string("Jojo")
basic.forever(on_forever)
