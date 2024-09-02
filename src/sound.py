import logging
from dataclasses import dataclass
from enum import Enum
from pyo import LFO

logger = logging.getLogger(__name__)


class LFOTypes(Enum):
    SAW_UP = 0
    SAW_DOWN = 1
    SQUARE = 2
    TRIANGLE = 3
    PULSE = 4
    BIPOLAR_PULSE = 5
    SAMPLE_AND_HOLD = 6
    MODULATED_SINE = 7


@dataclass
class SynthConfig:
    amplitude: float
    attack: float
    sustain: float
    decay: float
    reverb: float
    voices: float
    lfo_type: LFOTypes


class SynthKey:
    def __init__(self, freq: int = 440, lfo_type: LFOTypes = 0):
        # a.k.a Low Freq. Oscillator
        self.sound = LFO(freq=freq, type=lfo_type)

    def play(self):
        self.sound.out()

    def stop(self):
        self.sound.stop()

    def set_lfo_type(self, lfo_type: LFOTypes):
        self.sound.setType(lfo_type)


class Synth:
    def __init__(self):
        self.key_configs = {
            "C5": {"freq": 523.25},
            "D5": {"freq": 587.33},
            "E5": {"freq": 659.25},
            "F5": {"freq": 698.46},
            "G5": {"freq": 783.99},
            "A5": {"freq": 880},
            "B5": {"freq": 987.77},
            "C6": {"freq": 1046.5},
        }
        self.keys: dict[str, SynthKey] = {}
        self.config_state = SynthConfig(
            amplitude=10,
            attack=0.1,
            sustain=0,
            decay=0,
            reverb=0,
            voices=1,
            lfo_type=LFOTypes.SQUARE,
        )

        self._init_synth_keys()

    def _init_synth_keys(self):
        for key_id, key_config in self.key_configs.items():
            self.keys[key_id] = SynthKey(freq=key_config["freq"])

    def update_synths(self, **kwargs):
        logger.info(f"Updating synths with {kwargs}")
        if lfo_type := kwargs.get("lfo_types"):
            logger.info(f"Changing to {lfo_type}")
            for sk in self.keys.values():
                sk.set_lfo_type(lfo_type)

    def play_key(self, key_id: str):
        self.keys[key_id].play()

    def stop_key(self, key_id: str):
        self.keys[key_id].stop()
