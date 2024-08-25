from pyo import Sine


class Synth:
    def __init__(self, freq: int = 440):
        self.sound = Sine(freq=freq)

    def play(self):
        self.sound.out()

    def stop(self):
        self.sound.stop()
