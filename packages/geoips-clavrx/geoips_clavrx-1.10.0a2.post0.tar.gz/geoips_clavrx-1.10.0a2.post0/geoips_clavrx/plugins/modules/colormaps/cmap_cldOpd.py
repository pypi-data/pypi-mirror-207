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

"""Module containing colormap for satellite cloud optical depth products."""
import logging

LOG = logging.getLogger(__name__)

interface = "colormaps"
family = "matplotlib"
name = "cmap_cldOpd"


def call(data_range=[-0.2, 8]):
    """Cloud Optical Depth Colormap.

    Parameters
    ----------
    data_range : list of float, default=[-0.2, 8]
        Min and max value for colormap.
        Ensure the data range matches the range of the algorithm specified
        for use with this colormap.
        CldPhase=0(clear),1(water),2(supercooled),3(mixed),4(ice),5(unknown)

    Returns
    -------
    mpl_colors_info : dict
        Dictionary of matplotlib plotting parameters, to ensure consistent image output
    """
    min_tb = data_range[0]
    max_tb = data_range[1]
    if min_tb >= 1 or max_tb <= 6:
        raise ("cloud OPD must at least gave a range of 0 - 6")
    ticks = [min_tb, 0, 1, 2, 3, 4, 5, 6, 7, max_tb]
    colorlist = [
        "ghostwhite",
        "slategray",
        "blue",
        "royalblue",
        "cyan",
        "green",
        "yellow",
        "lightsalmon",
        "red",
        "black",
    ]

    from matplotlib.colors import ListedColormap, BoundaryNorm

    mpl_cmap = ListedColormap(colorlist, N=len(colorlist))

    LOG.info("Setting norm")
    bounds = ticks + [max_tb + 1]
    mpl_norm = BoundaryNorm(bounds, mpl_cmap.N)

    cbar_label = r"Cloud OPD"

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
