from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import time

alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class TypeGridLayout(GridLayout):
    last_key = ""


    def __init__(self, **kwargs):
        super(TypeGridLayout, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.rotor1 = Rotor(1, self)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        keypressed = keycode[1]

        TypeGridLayout.ChangeStuff(self,keypressed)

    def ChangeStuff(self, keycode):

        keycode=keycode.upper()
        if keycode:
            try:
                if keycode in alphabet:
                    keycode = alphabet.index(keycode)
                    self.rotor1.update(self.ids.first_roter.text)
                    x = self.rotor1.run(keycode, True)
                    self.display.text += alphabet[x]
                    self.lightup(alphabet[x])
                    if eval(self.ids.first_roter.text) == 26:
                        self.ids.first_roter.text = "1"
                        if eval(self.ids.second_roter.text) == 26:
                            self.ids.second_roter.text = "1"
                            self.ids.third_roter.text = str(eval(self.ids.third_roter.text) + 1)
                        else:
                            self.ids.second_roter.text = str(eval(self.ids.second_roter.text) + 1)
                    else:
                        self.ids.first_roter.text = str(eval(self.ids.first_roter.text)+1)
            except Exception:
                self.display.text = "Error"

    def lightup(self, char):
        if self.last_key:
            self.ids[self.last_key].background_color = 0.5, 0.5, 0.5, 0.5
            self.ids[char].background_color = 0.0, 1.0, 1.0, 1.0
            self.last_key = char
        else:
            self.ids[char].background_color = 0.0, 1.0, 1.0, 1.0
            self.last_key = char


class Rotor(object):

    def __init__(self, n, TypeGridLayout):
        self.position =  int(TypeGridLayout.ids.first_roter.text)
        if n == 1:
            self.wiring = [[0, 22], [1, 13], [2, 8], [3, 24], [4, 1], [5, 10], [6, 14], [7, 5], [8, 17], [9, 20], [10, 25],
                      [11, 15], [12, 11], [13, 18], [14, 4], [15, 0], [16, 19], [17, 16], [18, 7], [19, 12], [20, 3],
                      [21, 9],
                      [22, 21], [23, 6], [24, 23], [25, 2]]
        if n == 2:
            self.wiring = [[0, 24], [1, 18], [2, 11], [3, 6], [4, 3], [5, 8], [6, 20], [7, 15], [8, 12], [9, 22], [10, 7],
                      [11, 19], [12, 16], [13, 21], [14, 1], [15, 10], [16, 13], [17, 23], [18, 4], [19, 25], [20, 2],
                      [21, 17], [22, 9], [23, 14], [24, 5], [25, 0]]
        if n == 3:
            self.wiring = [[0, 6], [1, 8], [2, 25], [3, 23], [4, 0], [5, 15], [6, 5], [7, 1], [8, 12], [9, 24], [10, 20],
                      [11, 16], [12, 13], [13, 18], [14, 7], [15, 22], [16, 9], [17, 2], [18, 11], [19, 21], [20, 10],
                      [21, 3], [22, 19], [23, 4], [24, 17], [25, 14]]

    def run(self, input, bool):
        if bool:
            input = (input + self.position) % 26
            return self.wiring[input][1]
        else:
            for i in range(26):
                if input == self.wiring[i][1]:
                    output = (self.wiring[i][1] - self.position)
                    while(output<0):
                        output+=26
                    output = output % 26
                    return output
        return -1

    def update(self, n):
        self.position = int(n)

class TypeApp(App):
    def build(self):
        return TypeGridLayout()


TypeApp().run()