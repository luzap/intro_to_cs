"""Constants used by the game declared in another file,
to make access simpler for other game files."""
import os

FPS = 60
WIDTH = 720
HEIGHT = 480
BLOCKSIZE = 10  # Should really be changed dynamically

# The directory scanning pyglet claims to have doesn't seem to work
IMGASSETS = os.path.join("assets", "img")
SOUNDASSETS = os.path.join("assets", "snd")
DEBUG = False


# The GUI elements used for Menu and Highscore scenes
GUIPRESET = {
    "font": "Lucida Grande",
    "font_size": 20,
    "font_size_small": 10,
    "text_color": [0, 0, 0, 255],
    "gui_color": [0, 0, 255, 255],
    "disabled_color": [160, 160, 160, 255],
}

# The look of the Button
BUTTON = {"button": {
    "down": {
        "image": {
            "source": "button-down.png",
            "frame": [6, 6, 6, 6],
            "padding": [12, 12, 4, 2]
        },
        "text_color": [0, 0, 0, 255]
    },
    "up": {
        "image": {
            "source": "button.png",
            "frame": [6, 6, 6, 6],
            "padding": [20, 20, 4, 4]
        }
    }
}
}

# Placeholder: the vscroll is never used but needed for one of the 
# Scenes to work properly
SCROLL = {"vscrollbar": {
    "knob": {
        "image": {
            "source": "vscrollbar.png",
            "region": [0, 16, 16, 16],
            "frame": [0, 6, 16, 4],
            "padding": [0, 0, 0, 0]
        },
        "offset": [0, 0]
    },
    "bar": {
        "image": {
            "source": "vscrollbar.png",
            "region": [0, 64, 16, 16]
        },
        "padding": [0, 0, 0, 0]
    }
}
}


THEMERES = "./assets/theme/"
