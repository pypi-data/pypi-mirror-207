"""
Module for reading OME_BIN/CST_OME file
"""
import numpy as np
from scipy.io import FortranFile

__all__ = ["read_ome_bin", "read_cst_ome", "read_dome_bin"]


def read_ome_bin(fname, num_bands, num_kpoints, num_spins, endian='big'):
    """
    Read the `ome_bin` file.

    The `omb_bin` file contains the optical matrix elements generated by the `Spectral` task.
    Note that we return the data in the 'C' order with dimensions (num_spins, num_kpoints, 3, num_bands, num_bands)

    Args:
        fname: Name of the file.
        num_bands: Number of bands.
        num_kpoints: Number of kpoints.
        num_spins: Number of spins.
        endian: Endian - CASTEP build instruction defaults to big-endian.

    Returns:
        version: The version number stored in the file.
        header: Header part written in the file.
        om: Optical matrix with dimensions (num_spins, num_kpoins, 3, num_bands, num_bands)
    """

    esymbol = '>' if endian.upper() == 'BIG' else '<'
    version_dtype = '{}f8'.format(esymbol)
    header_dtype = '{}a80'.format(esymbol)
    # Each complex number takes 2*8 bits - both real and imaginary parts are
    # double precision
    array_seg = '{}(3,{num_bands},{num_bands})c16'.format(esymbol,
                                                          num_bands=num_bands)

    om = np.zeros((num_spins, num_kpoints, 3, num_bands, num_bands),
                  dtype=complex)
    with FortranFile(fname, header_dtype=np.dtype(f'{esymbol}u4')) as fhandle:
        version = fhandle.read_record(version_dtype)
        header = fhandle.read_record(header_dtype)[0].decode()
        for ki in range(num_kpoints):
            for si in range(num_spins):
                om[si, ki, :, :, :] = fhandle.read_record(array_seg)
    return version[0], header, om


def read_cst_ome(fname, num_bands, num_kpoints, num_spins, endian='big'):
    """
    Read the `cst_ome` file.

    The `cst_ome` file contains the optical matrix elements generated by the `Spectral` task.
    This is a legacy file format and has slow io, especially for python as one has to use nested
    loops.

    Note that we return the data in the 'C' order with dimensions (num_spins, num_kpoints, 3, num_bands, num_bands)

    Args:
        fname: Name of the file.
        num_bands: Number of bands.
        num_kpoints: Number of kpoints.
        num_spins: Number of spins.
        endian: Endian - CASTEP build instruction defaults to big-endian.

    Returns:
        om: Optical matrix with dimensions (num_spins, num_kpoins, 3, num_bands, num_bands)
    """

    esymbol = '>' if endian.upper() == 'BIG' else '<'
    # Each complex number takes 2*8 bits - both real and imaginary parts are
    # double precision
    elem = '{}c16'.format(esymbol)

    om = np.zeros((num_spins, num_kpoints, 3, num_bands, num_bands),
                  dtype=complex)
    with FortranFile(fname, header_dtype=np.dtype(f'{esymbol}u4')) as fhandle:
        for ki in range(num_kpoints):
            for si in range(num_spins):
                for idx in range(3):
                    for ib1 in range(num_bands):
                        for ib2 in range(num_bands):
                            om[si, ki, idx, ib1, ib2] = fhandle.read_record(
                                elem)
        out = fhandle._fp.read()  # pylint: disable=protected-access
        assert out == b"", "More data exist beyond the specified sizes."
    return om


def read_dome_bin(fname, num_bands, num_kpoints, num_spins, endian="BIG"):
    """
    Read the `dome_bin` file.

    The `dome_bin` file contains the diagonals of the optical matrix (`ome_bin`), which are
    the gradient of the bands. This is file is more compact than `ome_bin` as the diagonal
    elements are real numbers.

    Args:
        fname: Name of the file.
        num_bands: Number of bands.
        num_kpoints: Number of kpoints.
        num_spins: Number of spins.
        endian: Endian - CASTEP build instruction defaults to big-endian.

    Returns:
        version: The version number stored in the file.
        header: Header part written in the file.
        dom: Diagonal elements of the optical matrix with dimensions (num_spin, num_kpoints, 3, num_bands)
    """

    # Each complex number takes 2*8 bits - both real and imaginary parts are
    # double precision
    esymbol = '>' if endian.upper() == 'BIG' else '<'
    version_dtype = '{}f8'.format(esymbol)
    header_dtype = '{}a80'.format(esymbol)
    array_seg = '{}(3,{})f8'.format(esymbol, num_bands)

    dom = np.zeros((num_spins, num_kpoints, 3, num_bands), dtype=float)
    with FortranFile(fname, header_dtype=np.dtype(f'{esymbol}u4')) as fhandle:
        version = fhandle.read_record(version_dtype)
        header = fhandle.read_record(header_dtype)[0].decode()
        for ki in range(num_kpoints):
            for si in range(num_spins):
                dom[si, ki, :, :] = fhandle.read_record(array_seg)
    return version[0], header, dom
