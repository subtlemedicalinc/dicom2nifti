#!/usr/bin/env bash

# update the api docs
sphinx-apidoc -f -o ../rst ../../dicom2nifti
#rm -Rf ../html
#sphinx-build -b html ../rst ../html