import numpy
import rasterio


# FUNCTION TAKES IMAGE AS ARGUMMENT AND RETURS A TUPLE OF 3 FLOAT VALUES
def ndvi_values(input_image):
    # SPLIT RED AND NEAR_INFRARED BANDS
    with rasterio.open(input_image) as src:
        red = src.read(3)
    with rasterio.open(input_image) as src:
        nir = src.read(4)

    numpy.seterr(divide='ignore', invalid='ignore')
    ndvi = (nir.astype(float) - red.astype(float)) / (nir.astype(float) + red.astype(float))

    ndvi_dtype = ndvi.dtype
    kwargs = src.meta
    kwargs.update(dtype=ndvi_dtype)
    kwargs.update(count=1)

    return float(numpy.nanmin(ndvi)), float(numpy.nanmax(ndvi)), float(numpy.nanmean(ndvi))


if __name__ == '__main__':
    print(ndvi_values(input('Enter the exact filename with extension:\t')))
