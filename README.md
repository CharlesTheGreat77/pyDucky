# PyDucky

## Description 📖
PyDucky is used to test existing *ducky scripts* locally for flipper zero *badusb* development. 
Initially designed to configure proxmox infrastructure quickly, this adds the convenience for
payload development and testing.

## Prerequisite ⚙️
| Language   |
|------------|
| Python3.x  |
```bash
pip3 install pynput
```

# Usage 🔨
```bash
python3 pyDucky.py duckyscript.txt
```

# Ducky Script 🦆
The current implementation *only* supports **Ducky Script V1** scripts to directly work with flipper zero based development.

One can *add/edit* the command mappings inside the python script to add additional functionality.

### Supported Commands 🪖
```python
{
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
    # add more...
}
```

### Key Input speed 🎹
*Edit* the speed at which keys are typed based on the connectivity
```python
ducky = PyDuck(
    sys.argv[1], 
    0.01 # default delay for each keystroke
)
```

### Test Case 🧪
```bash
echo -e "STRING echo 'This is a test!'\nENTER\nDELAY 500" > test.txt
python3 pyDucky.py test.txt
```
* Waits 3 seconds before executing the commands.

# Contributions ❤️
Feel free to contribute as needed!

# Note
I need to fix modifier combinations, bear with me.
