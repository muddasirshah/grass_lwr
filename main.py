from step3_gapfill import apply_gap_filling
import numpy as np
from datetime import datetime
def step2():
        input_folder = "input_folder" #input folder containing at least 3 rasters
        output_folder = "output_folder" #folder containing monthly interpolated raster
        start_date = ""
        end_date = ""
        aoi = "" #pass AOI geojson string here
        try:
            apply_gap_filling(
                                    aoi,
                                    input_folder,
                                    start_date,
                                    end_date,
                                    output_folder,
                                    input_folder,
                                    'NAME', #Variable name e.g. NDVI, output file will have this prefix
                                    'NON_NULL_RASTERS' #correct rasters (eligile for Interpolation), dont change
                                    )
        except Exception as e:
            print(e)
step2()
