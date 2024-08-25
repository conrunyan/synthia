from textual.widgets import Static, Button
from textual import events

from src.sound import Synth


class KeyboardKey(Button):
    def __init__(self, *args, synth_config: dict, **kwargs):
        super().__init__(*args, **kwargs)
        self.synth = Synth(**synth_config)

    async def _on_mouse_down(self, event: events.MouseDown):
        print("Mouse down on the button!", self.id)
        self.synth.play()

    async def _on_mouse_up(self, event: events.MouseDown):
        print("Mouse down on button!", self.id)
        self.synth.stop()


class Keyboard(Static):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys_config = {
            "C5": {"freq": 523.25},
            "D5": {"freq": 587.33},
            "E5": {"freq": 659.25},
            "F5": {"freq": 698.46},
            "G5": {"freq": 783.99},
            "A5": {"freq": 880},
            "B5": {"freq": 987.77},
            "C6": {"freq": 1046.5},
        }
        self.synths = {}

    def _make_key_button(self, key: str, classes: str, synth_config: dict):
        return KeyboardKey(
            label=key,
            id=f"note-{key.lower()}",
            classes=classes,
            synth_config=synth_config,
        )

    def compose(self):
        key_classes = "keyboard-button"
        for key_name, config in self.keys_config.items():
            yield self._make_key_button(key_name, key_classes, config)
