# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import shutil
import tempfile
import unittest

import dicom2nifti.convert_dir as convert_directory
from dicom2nifti import settings


class TestConversionDirectory(unittest.TestCase):
    def test_convert_directory(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            settings.enable_resampling()
            settings.set_resample_spline_interpolation_order(1)
            settings.set_resample_padding(-1000)
            settings.disable_validate_slice_increment()
            settings.disable_validate_orthogonal()
            convert_directory.convert_directory("/Users/abrys/Downloads/test",
                                                "/Users/abrys/Downloads")

        finally:
            shutil.rmtree(tmp_output_dir)

    def test_convert_directory2(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            convert_directory.convert_directory("/Users/abrys/Downloads/test",
                                                "/Users/abrys/Downloads")

        finally:
            shutil.rmtree(tmp_output_dir)



if __name__ == '__main__':
    unittest.main()
