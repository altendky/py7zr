#!/usr/bin/env python
#
#    Pure python p7zr implementation
#    Copyright (C) 2019 Hiroshi Miura
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from pkg_resources import DistributionNotFound, get_distribution

from py7zr.exceptions import (Bad7zFile, DecompressionError,
                              UnsupportedCompressionMethodError)
from py7zr.py7zr import (ArchiveInfo, FileInfo, SevenZipFile, is_7zfile,
                         pack_7zarchive, unpack_7zarchive)
from py7zr.properties import (FILTER_LZMA1, FILTER_LZMA2, FILTER_DELTA, FILTER_ARM, FILTER_ARMTHUMB, FILTER_IA64,
                              FILTER_POWERPC, FILTER_SPARC, FILTER_X86, CHECK_CRC32, CHECK_CRC64, CHECK_SHA256,
                              CHECK_NONE, PRESET_EXTREME, PRESET_DEFAULT, FILTER_CRYPTO_AES256_SHA256)

__copyright__ = 'Copyright (C) 2019 Hiroshi Miura'

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = "unknown"

__all__ = ['__version__', 'ArchiveInfo', 'FileInfo', 'SevenZipFile', 'is_7zfile',
           'UnsupportedCompressionMethodError', 'Bad7zFile', 'DecompressionError',
           'pack_7zarchive', 'unpack_7zarchive',
           'FILTER_LZMA1', 'FILTER_LZMA2', 'FILTER_DELTA', 'FILTER_X86', 'FILTER_ARM',
           'FILTER_SPARC', 'FILTER_POWERPC', 'FILTER_IA64', 'FILTER_ARMTHUMB',
           'CHECK_SHA256', 'CHECK_CRC64', 'CHECK_CRC32', 'CHECK_NONE',
           'FILTER_CRYPTO_AES256_SHA256']
