import datetime
# import re
import site

import matplotlib.lines as lines
from PIL import Image

import accompanist.version as ve

LOGO_FILE = "logo_trans.png"
VERSION_FILE = "".join(site.getsitepackages()) + "/accompanist/version.py"

# ToDo: Refactor
# verstrline = open(VERSION_FILE, "rt").read()
# VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
# mo = re.search(VSRE, verstrline, re.M)
# verstr = mo.group(1)


def write_front_cover(fig, color):
    """
    Write cover of report
    """
    fig.add_artist(lines.Line2D([0, 1], [0.24, 0.24], color=color, linewidth=306, zorder=0))

    title_1 = "AWS WAF Log"
    title_2 = "Analysis Report"
    today = datetime.date.today()
    creation_date = "Creation Date: " + str(today)
    description = "This report was automatically generated with"

    fig.text(0.1, 0.80, title_1, color="#000000", fontsize=50, fontweight="bold")
    fig.text(0.1, 0.66, title_2, color="#000000", fontsize=50, fontweight="bold")
    fig.text(0.7, 0.52, creation_date, color="#757575", fontsize=18, fontweight="bold")
    fig.text(0.262, 0.3, description, color="#ffffff", fontsize=18)

    logo_location = "".join(site.getsitepackages()) + "/accompanist/resource/" + LOGO_FILE
    fig.figimage(Image.open(logo_location), xo=360, yo=100)

    fig.text(0.44, 0.05, "Version: " + ve.VERSION, color="#ffffff", fontsize=16, fontweight="bold")
