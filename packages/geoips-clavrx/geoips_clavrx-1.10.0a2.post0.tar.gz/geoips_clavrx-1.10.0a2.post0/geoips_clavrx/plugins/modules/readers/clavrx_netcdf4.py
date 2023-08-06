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

"""CLAVR-x NetCDF4 Reader."""
import logging

LOG = logging.getLogger(__name__)

interface = "readers"
family = "standard"
name = "clavrx_netcdf4"


def call(fnames, metadata_only=False, chans=None, area_def=None, self_register=False):
    """Unsupported CLAVR-x NetCDF4 reader."""
    LOG.exception("READER NOT IMPLEMENTED")
    return None
