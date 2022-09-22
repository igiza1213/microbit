def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
    elif input.button_is_pressed(Button.B):
        pass
basic.forever(on_forever)
