import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.mcp23017 import MCP23017
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

i2c = busio.I2C(scl=board.GP9, sda=board.GP8)

mcp23017_ext = MCP23017(
    i2c=i2c,
    device_address=0x20,
    pins=[0, 1, 2, 3, 4], 
)
keyboard.extensions.append(mcp23017_ext)

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

FN = KC.MO(1)

keyboard.keymap = [
    [
        KC.GRAVE, KC.N1,    KC.N2,   KC.N3,    KC.N4,   KC.N5,   KC.N6,    KC.N7,   KC.N8,   KC.N9,    KC.N0,   KC.MINS,  KC.EQL,   KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,    KC.E,     KC.R,    KC.T,    KC.Y,     KC.U,    KC.I,    KC.O,     KC.P,    KC.LBRC,  KC.RBRC,  KC.BSLS,
        KC.CAPS,  KC.A,     KC.S,    KC.D,     KC.F,    KC.G,    KC.H,     KC.J,    KC.K,    KC.L,     KC.SCLN, KC.QUOT,  KC.ENT,   KC.NO,
        KC.LSFT,  KC.Z,     KC.X,    KC.C,     KC.V,    KC.B,    KC.N,     KC.M,    KC.COMM, KC.DOT,   KC.SLSH, KC.RSFT,  KC.NO,    KC.NO,
        KC.LCTL,  KC.LGUI,  KC.LALT, KC.SPC,   KC.NO,   KC.NO,   KC.NO,    KC.NO,   KC.RALT, KC.RGUI,  FN,      KC.RCTL,  KC.NO,    KC.NO,
    ],
    [
        KC.ESC,   KC.F1,    KC.F2,   KC.F3,    KC
