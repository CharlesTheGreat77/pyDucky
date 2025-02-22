import time, sys
from pynput.keyboard import Controller, Key

class PyDuck:
    def __init__(self, file_path, delay):
        self.file_path = file_path
        self.delay = delay

        self.keyboard = Controller()
        self.command_map = {
            "ENTER": Key.enter,
            "ESCAPE": Key.esc,
            "SPACE": Key.space,
            "TAB": Key.tab,
            "ESC": Key.esc,
            "UP": Key.up,
            "DOWN": Key.down,
            "LEFT": Key.left,
            "RIGHT": Key.right,
            "CTRL": Key.ctrl,
            "ALT": Key.alt,
            "SHIFT": Key.shift,
            "BACKSPACE": Key.backspace,
            "DELETE": Key.delete,
        } # add more if needed.. didnt even need this much

    def press_key(self, key) -> None:
        self.keyboard.press(key)
        self.keyboard.release(key)
        time.sleep(self.delay)

    def press_combination(self, modifiers, target_key) -> None:
        for modifier in modifiers:
            self.keyboard.press(modifier)

        self.keyboard.press(target_key)
        self.keyboard.release(target_key)
        self.keyboard.release(modifier)
        time.sleep(self.delay)

    def type_string(self, text) -> None:
        for char in text:
            if char.isupper() or char in '!@#$%^&*()_+{}|:"<>?':
                self.keyboard.press(Key.shift)
                self.keyboard.press(char.lower())
                self.keyboard.release(char.lower())
                self.keyboard.release(Key.shift)
            elif char.isdigit(): # having issues with digits in proxmox???
                self.keyboard.press(str(char))
            else:
                self.keyboard.press(char)
                self.keyboard.release(char)
            time.sleep(self.delay)

    def run(self) -> None:
        with open(self.file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.replace('"', "'") # havin a lil issue with the quote handling for proxmox
            parts = line.strip().split(" ", 1)

            if parts[0] == "DELAY" and len(parts) > 1: # baby check
                time.sleep(float(int(parts[1]) / 1000))
            elif parts[0] == "STRING" and len(parts) > 1:
                self.type_string(parts[1])
            elif parts[0] in self.command_map:
                self.press_key(self.command_map[parts[0]])
            else: # modifiers and stuff
                modifiers = []
                target_key = None
                for part in parts:
                    if part in self.command_map:
                        target_key = self.command_map[part]
                    else:
                        modifiers.append(self.command_map.get(part))

                if target_key:
                    # still need to do more testting to see if it accomodates for everything
                    self.press_combination(modifiers, target_key)

ducky = PyDuck(
    sys.argv[1],
    0.01
)

print("[*] Ducky Script ready to go!")
time.sleep(3)
ducky.run()
