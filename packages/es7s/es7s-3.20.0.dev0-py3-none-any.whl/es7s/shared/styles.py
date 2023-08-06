# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import pytermor as pt


class Styles(pt.Styles):
    TEXT_DISABLED = pt.Style(fg=pt.cv.GRAY_23, frozen=True)
    TEXT_LABEL = pt.Style(fg=pt.cv.GRAY_35, frozen=True)
    TEXT_DEFAULT = pt.Style(fg=pt.cv.GRAY_62, frozen=True)

    STATUSBAR_BG = pt.NOOP_COLOR

    VALUE_LBL_5 = TEXT_LABEL
    VALUE_UNIT_4 = TEXT_LABEL
    VALUE_FRAC_3 = pt.Style(fg=pt.cv.GRAY_50, frozen=True)
    VALUE_PRIM_2 = TEXT_DEFAULT
    VALUE_PRIM_1 = pt.Style(fg=pt.cv.GRAY_70, bold=True, frozen=True)

    TEXT_ACCENT = pt.Style(fg=pt.cv.GRAY_85, frozen=True)
    TEXT_SUBTITLE = pt.Style(fg=pt.cv.GRAY_93, bold=True, frozen=True)
    TEXT_TITLE = pt.Style(fg=pt.cv.HI_WHITE, bold=True, underlined=True, frozen=True)
    TEXT_UPDATED = pt.Style(fg=pt.cv.HI_GREEN, bold=True, frozen=True)

    BORDER_DEFAULT = pt.Style(fg=pt.cv.GRAY_30, frozen=True)
    FILL_DEFAULT = pt.Style(fg=pt.cv.GRAY_46, frozen=True)

    STDERR_DEBUG = pt.Style(fg=pt.resolve_color("medium purple 7"), frozen=True)
    STDERR_TRACE = pt.Style(fg=pt.resolve_color("pale turquoise 4"), frozen=True)

    # PBAR_BG = pt.Style(bg=pt.cv.GRAY_3)
    PBAR_DEFAULT = pt.Style(TEXT_DEFAULT, bg=pt.cv.GRAY_19, frozen=True)
    PBAR_ALERT_1 = pt.Style(fg=pt.cv.GRAY_7, bg=pt.resolve_color("orange 3"), frozen=True)
    PBAR_ALERT_2 = pt.Style(PBAR_ALERT_1, bg=pt.resolve_color("dark goldenrod"), frozen=True)
    PBAR_ALERT_3 = pt.Style(PBAR_ALERT_1, bg=pt.resolve_color("orange 2"), frozen=True)
    PBAR_ALERT_4 = pt.Style(PBAR_ALERT_1, bg=pt.resolve_color("dark orange"), frozen=True)
    PBAR_ALERT_5 = pt.Style(PBAR_ALERT_1, bg=pt.resolve_color("orange-red 1"), frozen=True)
    PBAR_ALERT_6 = pt.Style(PBAR_ALERT_1, bg=pt.resolve_color("red 3"), frozen=True)
    PBAR_ALERT_7 = pt.Styles.CRITICAL_ACCENT

    DEBUG = pt.Style(
        fg=0x8163A2, bg=0x444, underlined=True, overlined=True, blink=False, frozen=True
    )
    DEBUG_SEP_INT = pt.Style(fg=0x7280E2, frozen=True)
    DEBUG_SEP_EXT = pt.Style(fg=0x7E59A9, frozen=True)
