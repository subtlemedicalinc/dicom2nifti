# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

import os
import shutil
import tempfile
import unittest

import dicom2nifti.convert_dir as convert_directory
import tests.test_data as test_data


class TestConversionDirectory(unittest.TestCase):
    def test_convert_directory(self):

        tmp_output_dir = tempfile.mkdtemp()
        try:
            convert_directory.convert_directory("/Users/abrys/Downloads/dicom_T1_PRE_501",
                                                "/Users/abrys/Downloads")

        finally:
            shutil.rmtree(tmp_output_dir)



if __name__ == '__main__':
    unittest.main()
