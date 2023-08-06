# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

"""Satellite cloud fraction product colormap."""
import logging

LOG = logging.getLogger(__name__)

interface = "colormaps"
family = "matplotlib"
name = "cmap_cldFraction"


def call(data_range=[0.0, 1.0]):
    """Cloud Fraction Colormap.

    Colormap for displaying Cloud_Fraction retrieved from satellite such as AHI or ABI.

    Parameters
    ----------
    data_range : list of float, default=[0.0, 1.0]
        Min and max value for colormap.
        Ensure the data range matches the range of the algorithm specified
        for use with this colormap

    Returns
    -------
    mpl_colors_info : dict
        Dictionary of matplotlib plotting parameters, to ensure consistent image output
    """
    min_tb = data_range[0]
    max_tb = data_range[1]
    print("min_tb, max_tb= ", min_tb, max_tb)
    if min_tb >= 0.1 or max_tb <= 0.7:
        raise ("cloud fraction must at least gave a range of 0.01 - 0.70")
    ticks = [
        int(min_tb),
        0.05,
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.8,
        0.85,
        0.9,
        0.95,
        int(max_tb),
    ]
    colorlist = [
        "ghostwhite",
        "slategray",
        "blue",
        "royalblue",
        "cyan",
        "limegreen",
        "green",
        "yellow",
        "gold",
        "lightsalmon",
        "coral",
        "red",
        "maroon",
        "black",
    ]

    from matplotlib.colors import ListedColormap, BoundaryNorm

    mpl_cmap = ListedColormap(colorlist, N=len(colorlist))

    LOG.info("Setting norm")
    bounds = ticks + [max_tb + 1]
    mpl_norm = BoundaryNorm(bounds, mpl_cmap.N)

    cbar_label = r"Cloud Fraction"

    # Must be uniform or proportional, None not valid for Python 3
    cbar_spacing = "uniform"  # for discrete bounds of a  color bar
    mpl_tick_labels = None
    mpl_boundaries = None

    # from geoips.image_utils.mpl_utils import create_colorbar
    # only create colorbar for final imagery
    # cbar = create_colorbar(fig, mpl_cmap, mpl_norm, ticks, cbar_label=cbar_label)
    mpl_colors_info = {
        "cmap": mpl_cmap,
        "norm": mpl_norm,
        "cbar_ticks": ticks,
        "cbar_tick_labels": mpl_tick_labels,
        "cbar_label": cbar_label,
        "boundaries": mpl_boundaries,
        "cbar_spacing": cbar_spacing,
        "colorbar": True,
        "cbar_full_width": True,
    }

    # return cbar, min_tb, max_tb
    return mpl_colors_info
