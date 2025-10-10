from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Rectangle, Line
from datetime import datetime


class KeyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(background_normal="", background_color=(0.25, 0.28, 0.3, 1), **kwargs)
        self._press_anim_ev = None
        self.bind(on_press=self._animate_press)

    def _animate_press(self, *_):
        self.background_color = (0.4, 0.45, 0.5, 1)
        if self._press_anim_ev:
            self._press_anim_ev.cancel()
        self._press_anim_ev = Clock.schedule_once(self._reset_color, 0.12)

    def _reset_color(self, *_):
        self.background_color = (0.25, 0.28, 0.3, 1)


class NokiaPhoneUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=6, padding=8, **kwargs)

        # State
        self.mode = "idle"  # idle | menu | text
        self.menu_items = [
            "Messages",
            "Contacts",
            "Call log",
            "Settings",
            "Games",
            "Extras",
        ]
        self.selected_index = 0
        self.entered_text = ""
        self._multi_tap_timer = None
        self._last_key = None
        self._last_key_index = 0
        self._multi_tap_timeout_s = 1.0
        self.operator = "Nokia"
        self.signal_level = 4  # 0..4
        self.battery_level = 4  # 0..4

        # Colors/theme (old LCD-ish look)
        Window.clearcolor = (0.08, 0.1, 0.1, 1)
        screen_bg = (0.8, 0.9, 0.8, 1)
        bezel = (0.12, 0.12, 0.12, 1)

        # Phone chassis container
        chassis = BoxLayout(orientation="vertical", padding=14, spacing=10)
        with chassis.canvas.before:
            Color(*bezel)
            self._chassis_rr = RoundedRectangle(radius=[18, 18, 30, 30])
        chassis.bind(pos=self._update_chassis, size=self._update_chassis)

        # LCD area (with status bar, content, softkey hints)
        lcd = BoxLayout(orientation="vertical", padding=8, spacing=6, size_hint_y=None, height=280)
        with lcd.canvas.before:
            Color(*screen_bg)
            self._lcd_rr = RoundedRectangle(radius=[10, 10, 10, 10])
        lcd.bind(pos=self._update_lcd, size=self._update_lcd)

        # Status bar
        self.status_bar = BoxLayout(orientation="horizontal", size_hint_y=None, height=24)
        self.lbl_operator = Label(text=self.operator, color=(0, 0, 0, 1), halign="left", valign="middle")
        self.lbl_clock = Label(text="", color=(0, 0, 0, 1), halign="center", valign="middle")
        self.lbl_status = Label(text="", color=(0, 0, 0, 1), halign="right", valign="middle")
        for lbl in (self.lbl_operator, self.lbl_clock, self.lbl_status):
            lbl.bind(size=self._relabel)
        self.status_bar.add_widget(self.lbl_operator)
        self.status_bar.add_widget(self.lbl_clock)
        self.status_bar.add_widget(self.lbl_status)

        # Content area label
        self.screen_area = Label(text="", color=(0, 0, 0, 1), halign="left", valign="top")
        self.screen_area.bind(size=self._relabel)

        # Softkey hint row (inside the screen like old phones)
        self.softkey_row = BoxLayout(orientation="horizontal")
        self.soft_left_label = Label(text="Menu", color=(0, 0, 0, 1), halign="left")
        self.soft_center_label = Label(text="", color=(0, 0, 0, 1), halign="center")
        self.soft_right_label = Label(text="Names", color=(0, 0, 0, 1), halign="right")
        self.softkey_row.add_widget(self.soft_left_label)
        self.softkey_row.add_widget(self.soft_center_label)
        self.softkey_row.add_widget(self.soft_right_label)

        # Construct LCD box
        screen_box = BoxLayout(orientation="vertical", padding=4, spacing=4)
        screen_box.add_widget(self.status_bar)
        screen_box.add_widget(self.screen_area)
        screen_box.add_widget(self.softkey_row)
        # Backlight overlay
        with screen_box.canvas.after:
            Color(1, 1, 1, 0)
            self._backlight = Rectangle()
        screen_box.bind(pos=self._update_backlight, size=self._update_backlight)

        # D-Pad section
        dpad = GridLayout(cols=3, rows=3, size_hint_y=None, height=140, spacing=6)
        dpad_buttons = {
            (0, 1): ("↑", lambda *_: self._on_dpad("up")),
            (1, 0): ("←", lambda *_: self._on_dpad("left")),
            (1, 1): ("OK", lambda *_: self._on_dpad("center")),
            (1, 2): ("→", lambda *_: self._on_dpad("right")),
            (2, 1): ("↓", lambda *_: self._on_dpad("down")),
        }
        for r in range(3):
            for c in range(3):
                key = (r, c)
                if key in dpad_buttons:
                    txt, cb = dpad_buttons[key]
                    dpad.add_widget(self._make_button(txt, cb))
                else:
                    dpad.add_widget(Widget())

        # Soft keys row (physical)
        softkeys = BoxLayout(orientation="horizontal", size_hint_y=None, height=48, spacing=6)
        softkeys.add_widget(self._make_button("Soft L", lambda *_: self._soft_left()))
        softkeys.add_widget(self._make_button("Back", lambda *_: self._soft_center()))
        softkeys.add_widget(self._make_button("Soft R", lambda *_: self._soft_right()))

        # Keypad (12-key)
        keypad = GridLayout(cols=3, rows=4, spacing=6)
        layout = [
            ("1\n.,?", "1"),
            ("2\nABC", "2"),
            ("3\nDEF", "3"),
            ("4\nGHI", "4"),
            ("5\nJKL", "5"),
            ("6\nMNO", "6"),
            ("7\nPQRS", "7"),
            ("8\nTUV", "8"),
            ("9\nWXYZ", "9"),
            ("*", "*"),
            ("0\n⎵", "0"),
            ("#", "#"),
        ]
        for label, key in layout:
            keypad.add_widget(self._make_button(label, lambda _btn, k=key: self._keypress(k)))

        # Assemble full UI
        outer = BoxLayout(orientation="vertical", padding=10, spacing=8)
        outer.add_widget(screen_box)
        outer.add_widget(dpad)
        outer.add_widget(softkeys)
        outer.add_widget(keypad)

        chassis.add_widget(outer)
        self.add_widget(chassis)

        Clock.schedule_interval(self._tick, 0.5)
        self._update_screen()

    def _relabel(self, instance, value):
        instance.text_size = instance.size

    def _make_button(self, text, on_press):
        return KeyButton(text=text, on_press=on_press)

    def _update_chassis(self, *_):
        if hasattr(self, "_chassis_rr"):
            self._chassis_rr.pos = self.children[0].pos if self.children else self.pos
            self._chassis_rr.size = self.children[0].size if self.children else self.size

    def _update_lcd(self, instance, value):
        if hasattr(self, "_lcd_rr"):
            self._lcd_rr.pos = instance.pos
            self._lcd_rr.size = instance.size

    def _update_backlight(self, instance, value):
        if hasattr(self, "_backlight"):
            self._backlight.pos = instance.pos
            self._backlight.size = instance.size

    def _blink_backlight(self):
        # quick fade-in/out imitation by toggling alpha briefly
        def on():
            self._set_backlight_alpha(0.12)
        def off(*_):
            self._set_backlight_alpha(0.0)
        on()
        Clock.schedule_once(off, 0.1)

    def _set_backlight_alpha(self, a):
        if self._backlight:
            self._backlight.canvas.children[0].rgba = (1, 1, 1, a)

    def _update_screen(self):
        # update status bar
        now = datetime.now().strftime("%H:%M")
        self.lbl_clock.text = now
        sig = "".join(["▂", "▃", "▅", "▇"][i] for i in range(self.signal_level))
        batt = "[" + ("|" * self.battery_level).ljust(4) + "]"
        self.lbl_status.text = f"{sig}  {batt}"
        self.lbl_operator.text = self.operator

        if self.mode == "idle":
            self.soft_left_label.text = "Menu"
            self.soft_center_label.text = ""
            self.soft_right_label.text = "Names"
            date_s = datetime.now().strftime("%d-%m-%Y")
            self.screen_area.text = f"Nokia\n{date_s}\n\nReady"
        elif self.mode == "menu":
            lines = ["— Nokia —", ""]
            for i, item in enumerate(self.menu_items):
                prefix = "> " if i == self.selected_index else "  "
                lines.append(f"{prefix}{item}")
            self.screen_area.text = "\n".join(lines)
            self.soft_left_label.text = "Open"
            self.soft_center_label.text = "Back"
            self.soft_right_label.text = "Exit"
        else:
            header = "Messages > New text"
            body = self.entered_text if self.entered_text else "_"
            self.screen_area.text = f"{header}\n\n{body}"
            self.soft_left_label.text = "Send"
            self.soft_center_label.text = "Clear"
            self.soft_right_label.text = "Opts"

    def _soft_left(self):
        if self.mode == "idle":
            self.mode = "menu"
        elif self.mode == "menu":
            # Open selected
            if self.menu_items[self.selected_index] == "Messages":
                self.mode = "text"
                self.entered_text = ""
        else:
            # Send (no-op demo)
            self.entered_text = "Sent!"
        self._update_screen()

    def _soft_center(self):
        if self.mode == "idle":
            # no-op
            pass
        elif self.mode == "menu":
            # Back from menu exits demo (no-op)
            self.mode = "idle"
            self.selected_index = 0
        else:
            # Clear one character
            if self.entered_text:
                self.entered_text = self.entered_text[:-1]
        self._reset_multi_tap()
        self._update_screen()

    def _soft_right(self):
        if self.mode == "idle":
            # Names placeholder
            self.screen_area.text = "Phonebook\n[Not implemented]"
        elif self.mode == "menu":
            # Exit demo: go to a minimal idle screen
            self.mode = "idle"
            self.selected_index = 0
        else:
            # Options placeholder
            self.entered_text += "\n[Options not implemented]"
        self._update_screen()

    def _on_dpad(self, direction):
        if self.mode == "idle":
            if direction in ("center", "right"):
                self.mode = "menu"
            self._update_screen()
        elif self.mode == "menu":
            if direction == "up":
                self.selected_index = (self.selected_index - 1) % len(self.menu_items)
            elif direction == "down":
                self.selected_index = (self.selected_index + 1) % len(self.menu_items)
            elif direction in ("center", "right"):
                self._soft_left()
            elif direction == "left":
                self._soft_center()
        else:
            # Text mode: left/right move as softkeys, center inserts newline
            if direction == "left":
                self._soft_center()
            elif direction == "right":
                self._soft_right()
            elif direction == "center":
                self.entered_text += "\n"
            elif direction == "up":
                self.entered_text += "^"
            elif direction == "down":
                self.entered_text += "v"
            self._update_screen()

    def _keypress(self, key):
        self._blink_backlight()
        self._on_key(key)

    def _on_key(self, key):
        if self.mode != "text":
            # Jump into text mode when typing from menu
            self.mode = "text"
            self.entered_text = ""

        mapping = {
            "1": [".", ",", "?", "!", "1"],
            "2": ["A", "B", "C", "2"],
            "3": ["D", "E", "F", "3"],
            "4": ["G", "H", "I", "4"],
            "5": ["J", "K", "L", "5"],
            "6": ["M", "N", "O", "6"],
            "7": ["P", "Q", "R", "S", "7"],
            "8": ["T", "U", "V", "8"],
            "9": ["W", "X", "Y", "Z", "9"],
            "0": [" ", "0"],
            "*": ["*"],
            "#": ["#"],
        }

        if key not in mapping:
            return

        if self._last_key == key and self._multi_tap_timer is not None:
            # Cycle current char
            self._last_key_index = (self._last_key_index + 1) % len(mapping[key])
            if self.entered_text:
                self.entered_text = self.entered_text[:-1]
            self.entered_text += mapping[key][self._last_key_index]
        else:
            # Start new char
            self._last_key = key
            self._last_key_index = 0
            self.entered_text += mapping[key][0]

        self._restart_multi_tap_timer()
        self._update_screen()

    def _tick(self, *_):
        # update clock and small status oscillations
        self._update_screen()

    def _restart_multi_tap_timer(self):
        self._cancel_multi_tap_timer()
        self._multi_tap_timer = Clock.schedule_once(lambda *_: self._reset_multi_tap(), self._multi_tap_timeout_s)

    def _cancel_multi_tap_timer(self):
        if self._multi_tap_timer is not None:
            try:
                self._multi_tap_timer.cancel()
            except Exception:
                pass
            self._multi_tap_timer = None

    def _reset_multi_tap(self):
        self._last_key = None
        self._last_key_index = 0
        self._cancel_multi_tap_timer()


class NokiaApp(App):
    def build(self):
        self.title = "Nokia Phone Demo"
        return NokiaPhoneUI()


if __name__ == "__main__":
    NokiaApp().run()