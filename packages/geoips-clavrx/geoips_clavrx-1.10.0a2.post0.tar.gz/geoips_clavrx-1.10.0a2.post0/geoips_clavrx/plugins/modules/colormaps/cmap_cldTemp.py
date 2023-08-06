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

"""Module containing colormap for cloud top temperature product."""
import logging

LOG = logging.getLogger(__name__)

interface = "colormaps"
family = "matplotlib"
name = "cmap_cldTemp"


def call(data_range=[160, 320]):
    """Cloud Top Temperature Colormap for ABI and AHI data.

    Parameters
    ----------
    data_range : list of float, default=[160, 320]
        Min and max value for colormap.
        Ensure the data range matches the range of the algorithm specified
        for use with this colormap
        The cloud top temperature MUST include 180 and 300 (k)

    Returns
    -------
    mpl_colors_info : dict
        Dictionary of matplotlib plotting parameters, to ensure consistent image output
    """
    min_tb = data_range[0]
    max_tb = data_range[1]

    if min_tb > 180 or max_tb < 300:
        raise ("cloud top temperature range MUST include 180 and 300")

    from geoips.image_utils.colormap_utils import create_linear_segmented_colormap

    transition_vals = [
        (min_tb, 170),
        (170, 180),
        (180, 200),
        (200, 220),
        (220, 240),
        (240, 260),
        (260, 280),
        (280, 300),
        (300, max_tb),
    ]
    transition_colors = [
        ("darkorange", "yellow"),
        ("darkred", "red"),
        ("green", "palegreen"),
        ("navy", "deepskyblue"),
        ("#FFFFCC", "#CCFFCC"),
        ("whitesmoke", "silver"),
        ("silver", "grey"),
        ("grey", "dimgrey"),
        ("dimgrey", "black"),
    ]

    # ticks = [xx[0] for xx in transition_vals]

    # special selection of label

    ticks = [160, 170, 180, 200, 220, 240, 260, 280, 300, 320]

    # selection of min and max values for colormap if needed
    min_tb = transition_vals[0][0]
    max_tb = transition_vals[-1][1]

    LOG.info("Setting cmap")
    mpl_cmap = create_linear_segmented_colormap(
        "cmap_cldTemp", min_tb, max_tb, transition_vals, transition_colors
    )

    LOG.info("Setting norm")
    from matplotlib.colors import Normalize

    mpl_norm = Normalize(vmin=min_tb, vmax=max_tb)

    cbar_label = "Cloud Top Temperature (K)"

    # Must be uniform or proportional, None not valid for Python 3
    cbar_spacing = "proportional"
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

    return mpl_colors_info
