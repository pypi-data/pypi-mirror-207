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

"""
CLAVR-x hdf4 cloud property data reader.

S.Yang:  1/19/2023
"""

import logging
from datetime import datetime
import numpy as np
import xarray as xr

LOG = logging.getLogger(__name__)

try:
    from pyhdf.HDF import ishdf
except ImportError:
    print(
        "Failed import pyhdf.ishdf in clavrx_hdf4.py " + "If you need it, install it."
    )
try:
    from pyhdf.SD import SD, SDC
except ImportError:
    print(
        "Failed import pyhdf.SD/SDC in clavrx_hdf4.py " + "If you need it, install it."
    )
try:
    from pyhdf.error import HDF4Error
except ImportError:
    print(
        "Failed import pyhdf error in clavrx_hdf4.py " + "If you need it, install it."
    )

interface = "readers"
family = "standard"
name = "clavrx_hdf4"


def parse_metadata(metadatadict):
    """Parse metadata."""
    metadata = {}
    for ii in metadatadict.keys():
        metadata[ii] = metadatadict[ii]

    # Map GOES-RU-IMAGER to "abi" GeoIPS sensor name
    if metadata["sensor"] == "GOES-RU-IMAGER":
        metadata["sensor"] = "abi"

    return metadata


#########################################################################
# READ CLAVR-x CLOUD PROPERTIES
#########################################################################


def read_cloudprops(fname, metadata_only=False):
    """Read CLAVR-x Cloud Properties Data."""
    if ishdf(fname):
        try:
            data = SD(fname, SDC.READ)  # read in all data fields
        except HDF4Error:
            LOG.info("wrong input hdf file %s", fname)
            raise

    # selected cloud variables
    # definiation of variables
    # cira_out = {'latitude':latitude, 'longitude':longitude,
    #     'cloud_type':cld_type,
    #     'cloud_mask':cld_mask,
    #     'cloud_phase':cld_phase,
    #     'cloud_fraction',cld_fract,
    #     'cld_height_acha':cld_hgt,
    #     'cld_height_base_acha':cld_hgt_base,
    #     'cld_height_top_acha':cld_hgt_top,
    #     'cld_temp_acha':cld_temp,
    #     'cloud_water_path':cwp,
    #     'cld_opd_acha':cld_opd,
    #     'cld_reff_acha':cld_reff,
    #     'temp_3_75um_nom',tb_3p75,
    #     'temp_11_0um_nom':tb_11p0,
    #     'solar_zenith_angle':sza}

    # Note:  Values of the attribute 'valid_range' for cloud_type, cloud_mask,
    #        cloud_phase(?) are not valid.
    #        They should be specified with their definitions.

    vars_sel = [
        "latitude",
        "longitude",
        "cloud_type",
        "cloud_mask",
        "cloud_phase",
        "cloud_fraction",
        "cld_height_acha",
        "cld_height_base_acha",
        "cld_height_top_acha",
        "cld_temp_acha",
        "cloud_water_path",
        "cld_opd_acha",
        "cld_reff_acha",
        "temp_3_75um_nom",
        "temp_11_0um_nom",
        "solar_zenith_angle",
    ]

    # process of all variables
    xarrays = {}

    data = SD(fname, SDC.READ)
    data_metadata = parse_metadata(data.attributes())

    # setup attributes
    # If start/end datetime happen to vary, adjust here.
    # start time
    syr = str(data_metadata["START_YEAR"])
    sjd = str(data_metadata["START_DAY"])
    shr = str(int(data_metadata["START_TIME"]))
    smin = str(int((data_metadata["START_TIME"] - int(shr)) * 60))
    ssec = str(int(((data_metadata["START_TIME"] - int(shr)) * 60 - int(smin)) * 60))
    # end time
    eyr = str(data_metadata["END_YEAR"])
    ejd = str(data_metadata["END_DAY"])
    ehr = str(int(data_metadata["END_TIME"]))
    emin = str(int((data_metadata["END_TIME"] - int(ehr)) * 60))
    esec = str(int(((data_metadata["END_TIME"] - int(ehr)) * 60 - int(emin)) * 60))

    sdt = datetime.strptime(syr + sjd + shr + smin + ssec, "%Y%j%H%M%S")
    edt = datetime.strptime(eyr + ejd + ehr + emin + esec, "%Y%j%H%M%S")

    xarrays = xr.Dataset()
    xarrays.attrs["start_datetime"] = sdt
    xarrays.attrs["end_datetime"] = edt
    xarrays.attrs["source_name"] = data_metadata["sensor"].lower()
    xarrays.attrs["platform_name"] = data_metadata["platform"].lower()
    xarrays.attrs["data_provider"] = "cira"
    xarrays.attrs["original_source_filenames"] = data_metadata["FILENAME"]
    xarrays.attrs["sample_distance_km"] = data_metadata["RESOLUTION_KM"]  # 2km
    xarrays.attrs["interpolation_radius_of_influence"] = 3000  # 3km

    if metadata_only:
        LOG.info("metadata_only requested, returning without reading data")
        return {"METADATA": xarrays}

    list_vars = list(data.datasets())

    for var in list_vars:
        if var in vars_sel:
            data_select = data.select(var)  # select this var
            attrs = data_select.attributes()  # get attributes for this var
            data_get = data_select.get()  # get all data of this var
            # mask grids with missing or bad values
            limit1 = attrs["valid_range"][0]
            limit2 = attrs["valid_range"][1]
            if var == "cloud_type":
                limit1 = 0
                limit2 = 13
            if var == "cloud_mask":
                limit1 = 0
                limit2 = 3
            data_get_mask = np.ma.masked_outside(data_get, limit1, limit2, copy=True)
            # convert the scaled/ofset values into the actual values
            data_get_actualvalue = (
                data_get_mask * attrs["scale_factor"] + attrs["add_offset"]
            )
            xarrays[var] = xr.DataArray(data_get_actualvalue)
            # setup attributes for this var (will be applied later from the
            #     extracted files
            # for attrname in attrs:
            #    xarrays[var].attrs[attrname]=attrs[attrname]

    return xarrays


def call(fnames, metadata_only=False, chans=None, area_def=None, self_register=False):
    """Read CLAVR-x hdf4 cloud properties."""
    fname = fnames[0]
    # path='$GEOIPS_TESTDATA_DIR/test_data_cloud/data/himawari8/20201201/'
    # fname = path+'clavrx_H08_202012010700.level2.hdf'

    # print ('test= ', fname)

    # call a subroutine to read cira cloud property file
    # minlon, maxlon, minlat, maxlat: limit of a terget area
    # for the 40deg x 50deg W. Pacific region:
    # minlon, maxlon, minlat, maxlat = [100-150E,10-50N]
    # istat, outputs= read_cloudprops(fname, minlon, maxlon, minlat, maxlat)
    xarrays = read_cloudprops(fname, metadata_only=False)
    return {"DATA": xarrays, "METADATA": xarrays[[]]}
