from __future__ import absolute_import, print_function

"""
This file contains a number of pancake utilities which may be useful in running pancake.
"""

from pandeia.engine.psf_library import PSFLibrary
from pandeia.engine.source import Source

def determine_pandeia_offset(config):
    """
    Uses Pandeia's PSF library to determine which PSF offset pandeia would use for a particular
    configuration (for comparison with the offset that pancake would use in on-the-fly PSF
    generation).
    """
    instrument = config['configuration']['instrument']
    aperture = config['configuration']['aperture']
    scene_sources, reference_sources = [], []
    for source in config['scene']:
        scene_sources.append(Source(config=source))
    if 'psf_subtraction_source' in config['strategy']:
        reference_sources.append(Source(config=config['strategy']['psf_subtraction_source']))
    library = PSFLibrary()
    scene_offsets = library.associate_offset_to_source(scene_sources, instrument, aperture)
    scene_offsets = library.associate_offset_to_source(scene_sources, instrument, aperture)
    return {'scene': scene_offsets, 'reference': reference_offsets}
