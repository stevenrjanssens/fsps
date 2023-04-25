import numpy
import stsynphot as stsyn
from synphot import units, SourceSpectrum, SpectralElement, Observation
from astropy.time import Time

if __name__ == '__main__':
    v_band = SpectralElement.from_filter('johnson_v')
    sun_file = 'https://archive.stsci.edu/hlsps/reference-atlases/cdbs/calspec/sun_reference_stis_002.fits'
    sun_raw = SourceSpectrum.from_file(sun_file)
    sun = sun_raw.normalize(4.83 * units.VEGAMAG, v_band, vegaspec=stsyn.Vega)

    bp = stsyn.band('wfc3,uvis1,f475x')
    obs = Observation(sun, bp, binset=bp.binset)
    magsun_vega = obs.effstim('vegamag', vegaspec=stsyn.Vega)
    print(magsun_vega)

    magsun_ab = obs.effstim('abmag')
    print(magsun_ab)
