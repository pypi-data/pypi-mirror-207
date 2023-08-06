import datetime
import json
import os
import site

import accompanist.utility as ut
import matplotlib.lines as lines
from PIL import Image

LOGO_FILE = "logo_trans_small.png"
SHEET_MUSIC_FILE = "sheet_music.json"


class WriteHeaderFooterClass():
    """
    Write header and footer class
    """

    def __init__(self):

        self._dic_box = {
            "facecolor": "White",
            "edgecolor": "#757575",
            "boxstyle": "Round, pad=0.7",
            "linewidth": 3,
        }

    def header_footer(self, fig, page_number, term, color):
        with open(SHEET_MUSIC_FILE, mode="r") as f:
            settings_dict = json.load(f)

        MAIN_COLOR = color

        # Header
        page_title = "AWS WAF Log  (Action: " + settings_dict["action"] + ")"
        log_group = settings_dict["log_group"].replace("aws-waf-logs-", "")
        if len(log_group) > 15:
            log_group = log_group[:15] + "*****"
        fig.add_artist(lines.Line2D([0, 1], [0.94, 0.94], color=MAIN_COLOR, linewidth=80, zorder=0))

        fig.text(0.05, 0.91, page_title, color="#ffffff", fontsize=26, fontweight="bold")
        fig.text(0.71, 0.82, "Log Group: " + log_group, color="#757575", fontsize=14, fontweight="bold", bbox=self._dic_box)
        fig.text(0.7, 0.76, term, color="#757575", fontsize=14)

        # Footer
        fig.add_artist(lines.Line2D([0, 1], [0.0004, 0.0004], color=MAIN_COLOR, linewidth=80, zorder=0))
        fig.text(0.92, 0.02, page_number, color="#949494", fontsize=20, fontweight="bold")

        # Logo
        logo_path = "".join(site.getsitepackages()) + "/accompanist/resource/" + LOGO_FILE
        if os.path.isfile(logo_path):
            fig.figimage(Image.open(logo_path), xo=500, yo=10)
        else:
            warning_logo = "[Warning] Logo file is not found."
            ut.colorize_print(warning_logo, "yellow")


def calc_term(time, utc_offset):
    """
    Show term
    """
    with open(SHEET_MUSIC_FILE, mode="r") as f:
        settings_dict = json.load(f)

    offset = 3600 * utc_offset
    info_utc = "[Info] The current UTC offset is \"" + str(utc_offset) + "\". You can change the offset with an option, --utc-offset N."
    ut.colorize_print(info_utc, "cyan")

    oldest_time = datetime.datetime.fromtimestamp(time[len(time) - 1] / 1000.0 + offset, tz=datetime.timezone.utc).strftime("%m/%d %H:%M")
    latest_time = datetime.datetime.fromtimestamp(time[0] / 1000.0 + offset, tz=datetime.timezone.utc).strftime("%m/%d %H:%M")

    days = str(settings_dict["days"])

    if int(days) > 1:
        term = days + " days (" + oldest_time + " - " + latest_time + ")"
    else:
        term = oldest_time + " - " + latest_time
    return term


def write_header_and_footer(waf_log_time, figs, utc_offset, color):
    """
    Add header and footer
    """
    term = calc_term(waf_log_time, utc_offset)

    write = WriteHeaderFooterClass()

    for fig in (figs):
        page_number = str(figs.index(fig) + 1) + " / " + str(len(figs))
        write.header_footer(fig, page_number, term, color)
