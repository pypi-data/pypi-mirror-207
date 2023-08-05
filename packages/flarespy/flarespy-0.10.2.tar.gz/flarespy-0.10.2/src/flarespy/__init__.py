from pathlib import Path

PACKAGEDIR = Path(__file__).parent.resolve()
MPLSTYLE = "{}/data/flarespy.mplstyle".format(PACKAGEDIR)

from .flarefinder import load_from_lightkurve
