"""Module to update a raw IMACS fits file with wcs information."""

import glob
from astropy.io import fits
import header_reader

def add_wcs_to_fits(fits_file_name: str, outfile_name: str = ''):
    """Writes wcs information to the fits file."""
    hdu = fits.open(fits_file_name)
    header_information = header_reader.HeaderInformation(fits_file_name)
    wcs = header_information.generate_wcs_object()
    header_wcs = wcs.to_header()
    hdu[0].header = hdu[0].header + header_wcs

    if outfile_name == '':
        outfile_name = fits_file_name.split('.fits')[0] + '.wcs.fits'
    hdu.writeto(outfile_name, overwrite=True)

if __name__ == '__main__':
    #files = glob.glob('/home/tlambert/Downloads/g_band/REDUCED/*science*.fits')
    files = glob.glob('/home/tlambert/Downloads/g_band/SCIENCE/*.fits')
    for file in files:
        add_wcs_to_fits(file)
