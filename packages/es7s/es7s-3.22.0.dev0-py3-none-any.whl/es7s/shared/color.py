# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import pytermor as pt

from .config import get_config


REGULAR_TO_BRIGHT_COLOR_MAP = {
    pt.cv.BLACK:    pt.cv.GRAY,
    pt.cv.RED:      pt.cv.HI_RED,
    pt.cv.GREEN:    pt.cv.HI_GREEN,
    pt.cv.YELLOW:   pt.cv.HI_YELLOW,
    pt.cv.BLUE:     pt.cv.HI_BLUE,
    pt.cv.MAGENTA:  pt.cv.HI_MAGENTA,
    pt.cv.CYAN:     pt.cv.HI_CYAN,
    pt.cv.WHITE:    pt.cv.HI_WHITE,
}


# noinspection PyMethodMayBeStatic
class Color:
    def get_color_name(self) -> str:
        return get_config().get("general", "theme-color", fallback="red")

    def get_theme_color(self, ctype: type = None) -> pt.CT:
        try:
            return pt.resolve_color(self.get_color_name(), ctype)
        except LookupError:
            return pt.cv.RED

    def get_theme_bright_color(self) -> pt.CT:
        try:
            theme_color16 = pt.resolve_color(self.get_color_name(), pt.Color16)
            if theme_color16 in REGULAR_TO_BRIGHT_COLOR_MAP.keys():
                return REGULAR_TO_BRIGHT_COLOR_MAP.get(theme_color16)
        except LookupError:
            pass

        theme_color = self.get_theme_color()
        if isinstance(theme_color, pt.Color256) and theme_color._color16_equiv:
            if theme_color16 := theme_color._color16_equiv in REGULAR_TO_BRIGHT_COLOR_MAP.keys():
                return REGULAR_TO_BRIGHT_COLOR_MAP.get(theme_color16)

        hue, sat, val = theme_color.to_hsv()  # val 50% -> 75%, val 80% -> 90% etc
        return pt.ColorRGB(hex_value=pt.hsv_to_hex(hue, sat, min(1.0, val + (1 - val) / 2)))

    def get_monitor_separator_color(self) -> pt.CT:
        hue, _, _ = self.get_theme_color().to_hsv()
        return pt.ColorRGB(hex_value=pt.hsv_to_hex(hue, 0.59, 0.50))


_color = Color()


def get_color() -> Color:
    return _color
