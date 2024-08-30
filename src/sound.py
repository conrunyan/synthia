from enum import Enum
from pyo import LFO


class LFOTypes(Enum):
    SAW_UP = 0
    SAW_DOWN = 1
    SQUARE = 2
    TRIANGLE = 3
    PULSE = 4
    BIPOLAR_PULSE = 5
    SAMPLE_AND_HOLD = 6
    MODULATED_SINE = 7


class Synth:
    def __init__(self, freq: int = 440, lfo_type: LFOTypes = 0):
        # a.k.a Low Freq. Oscillator
        self.sound = LFO(freq=freq, type=lfo_type)

    def play(self):
        self.sound.out()

    def stop(self):
        self.sound.stop()

    def set_lfo_type(self, lfo_type: LFOTypes):
        self.sound.type = lfo_type
