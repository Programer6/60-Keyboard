import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoders import Encoders
from kmk.extensions.mcp23017 import MCP23017
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions import Extension

class OledScreen(Extension):
    def __init__(self, i2c_bus):
        displayio.release_displays()

        try:
            display_bus_one = displayio.I2CDisplay(i2c_bus, device_address=0x3C)
            self.display_one = SSD1306(display_bus_one, width=128, height=32)
            self.group_one = displayio.Group()
            self.display_one.show(self.group_one)

            self.layer_label = label.Label(terminalio.FONT, text="Layer: 0", x=2, y=5)
            self.caps_label = label.Label(terminalio.FONT, text="CAPS", x=2, y=25)
            self.num_label = label.Label(terminalio.FONT, text="NUM", x=42, y=25)
            
            self.group_one.append(self.layer_label)
            self.group_one.append(self.caps_label)
            self.group_one.append(self.num_label)
        except (ValueError, RuntimeError):
            self.display_one = None

        try:
            display_bus_two = displayio.I2CDisplay(i2c_bus, device_address=0x3D)
            self.display_two = SSD1306(display_bus_two, width=128, height=64)
            self.group_two = displayio.Group()
            self.display_two.show(self.group_two)

            logo_label = label.Label(terminalio.FONT, text="-- My Keeb --", scale=2, x=10, y=30)
            self.group_two.append(logo_label)
        except (ValueError, RuntimeError):
            self.display_two = None

    def on_state_change(self, key, is_pressed, int_coord):
        if self.display_one:
            self.layer_label.text = f"Layer: {key.active_layers[0]}"
            self.caps_label.hidden = not key.caps_lock_status
            self.num_label.hidden = not key.num_lock_status

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(Encoders())
keyboard.extensions.append(MediaKeys())

i2c = busio.I2C(scl=board.GP9, sda=board.GP8)

oled_ext = OledScreen(i2c_bus=i2c)
keyboard.extensions.append(oled_ext)

mcp23017_ext = MCP23017(
    i2c=i2c,
    device_address=0x20,
    gp_int_a=None,
    gp_int_b=None,
)
keyboard.extensions.append(mcp23017_ext)

keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP10, board.GP11, board.GP12, board.GP13,
    board.GP14, board.GP15,
)
keyboard.row_pins = (
    mcp23017_ext.get_pin('GPB0'), mcp23017_ext.get_pin('GPB1'),
    mcp23017_ext.get_pin('GPB2'), mcp23017_ext.get_pin('GPB3'),
    mcp23017_ext.get_pin('GPB4'),
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.encoder_handler.pins = (
    (board.GP16, board.GP17, None),
    (board.GP18, board.GP19, None),
)

FN = KC.MO(1)
_______ = KC.TRNS

keyboard.keymap = [
    [
        KC.GRAVE, KC.N1,    KC.N2,   KC.N3,    KC.N4,   KC.N5,   KC.N6,    KC.N7,   KC.N8,   KC.N9,    KC.N0,   KC.MINS,  KC.EQL,   KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,    KC.E,     KC.R,    KC.T,    KC.Y,     KC.U,    KC.I,    KC.O,     KC.P,    KC.LBRC,  KC.RBRC,  KC.BSLS,
        KC.CAPS,  KC.A,     KC.S,    KC.D,     KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,     KC.SCLN, KC.QUOT,  KC.ENT,   KC.NO,
        KC.LSFT,  KC.Z,     KC.X,    KC.C,     KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,   KC.SLSH, KC.RSFT,  KC.UP,    KC.NO,
        KC.LCTL,  KC.LGUI,  KC.LALT, KC.SPC,   KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.RGUI, FN,       KC.LEFT, KC.DOWN,  KC.RGHT,  KC.NO,
    ],
    [
        KC.ESC,   KC.F1,    KC.F2,   KC.F3,    KC.F4,   KC.F5,   KC.F6,    KC.F7,   KC.F8,   KC.F9,    KC.F10,  KC.F11,   KC.F12,   KC.DEL,
        _______,  _______,  KC.UP,   _______,  _______, _______, _______, _______, KC.NLCK, KC.PSCR,  _______, _______,  _______,  KC.MUTE,
        _______,  KC.LEFT,  KC.DOWN, KC.RGHT,  _______, _______, _______, _______, _______, _______,  _______, _______,  KC.MPLY,  KC.NO,
        _______,  _______,  _______, _______,  _______, _______, _______, _______, KC.VOLD, KC.VOLU,  KC.MPRV, KC.MNXT,  _______,  KC.NO,
        _______,  _______,  _______, _______,  _______, _______, _______, _______, _______, _______,  _______, _______,  _______,  KC.NO,
    ]
]

keyboard.encoder_handler.map = (
    ( (KC.VOLD, KC.VOLU), (KC.MW_DN, KC.MW_UP) ),
    ( (KC.PGDN, KC.PGUP), (KC.NO, KC.NO) ),
)

if __name__ == '__main__':
    keyboard.go()
