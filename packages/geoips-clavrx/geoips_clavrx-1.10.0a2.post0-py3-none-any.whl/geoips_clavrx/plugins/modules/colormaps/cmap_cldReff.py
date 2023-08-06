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

"""Module containing colormap for effective radius of cloud particles product."""
import logging

LOG = logging.getLogger(__name__)

interface = "colormaps"
family = "matplotlib"
name = "cmap_cldReff"


def call(data_range=[0, 160]):
    """Cloud Particle Effective Radius Colormap.

    Parameters
    ----------
    data_range : list of float, default=[0, 160]
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

    if min_tb > 1 or max_tb < 150:
        raise ("effective radius of cloud particles MUST include 1 and 150")

    from geoips.image_utils.colormap_utils import create_linear_segmented_colormap

    transition_vals = [
        (min_tb, 5),
        (5, 10),
        (10, 15),
        (15, 20),
        (25, 30),
        (30, 40),
        (40, 50),
        (50, 100),
        (100, max_tb),
    ]
    transition_colors = [
        ("white", "lightgray"),
        ("oldlace", "moccasin"),
        ("#F4CD03", "#F2F403"),
        ("#8CF303", "#0FB503"),
        ("#06DCFD", "#0708B5"),
        ("#FFFFCC", "#CCFFCC"),
        ("#CCFFCC", "#6666FF"),
        ("#CC99FF", "#FF99CC"),
        ("red", "black"),
    ]

    # ticks = [xx[0] for xx in transition_vals]

    # special selection of label

    ticks = [0, 10, 20, 30, 40, 50, 75, 100, 120, 160]

    # selection of min and max values for colormap if needed
    min_tb = transition_vals[0][0]
    max_tb = transition_vals[-1][1]

    LOG.info("Setting cmap")
    mpl_cmap = create_linear_segmented_colormap(
        "cmap_cldReff", min_tb, max_tb, transition_vals, transition_colors
    )

    LOG.info("Setting norm")
    from matplotlib.colors import Normalize

    mpl_norm = Normalize(vmin=min_tb, vmax=max_tb)

    cbar_label = "Effective Radius"

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
