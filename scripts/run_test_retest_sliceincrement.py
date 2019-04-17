#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:30:13 2019

@author: vterzopoulos
"""

import json
import pipelines.pipeline
#import uuid

#import technical.utils.logging_tools
#import pipelines.pipeline
#import backend_dao.patients
#import backend_dao.projects
#import backend_dao.studies
#from backend_dao import get_session
#import backend_dao.jobs
#import technical.utils.software_versions
import os

BACKEND_URL = 'https://research.icometrix.com'
BACKEND_USER = 'it@icometrix.com'
BACKEND_PASS = 'UEo7gKUfDh3STge8w3ob'

dest_dir = '/secure-data/business/subsidized/CENTER-TBI/slice_increment_inconsistency/test_retest'


trt_file = '/secure-data/business/subsidized/CENTER-TBI/slice_increment_inconsistency/TRT_inconsistency.json'
with open(trt_file) as j_file:
    trt_data = json.load(j_file)


pipeline_config = 'pipeline_configurations/ct/cross/icobrain.json'
pipeline_parameters = 'pipeline_configurations/ct/cross/icobrain_parameters.json'

pipeline = pipelines.pipeline.Pipeline(pipeline_config,
                                       parameters_json_file=pipeline_parameters)
pipeline.pipeline_sequence.pop(-1)
pipeline.pipeline_sequence.pop(-1)
pipeline.pipeline_sequence.pop(-1)
report_type = 'icobrain_tbi'

for test_retest in trt_data[:1]:
    study_id = test_retest[0][0]['study_id']
    study_dir = os.path.join(dest_dir, study_id)
    os.makedirs(study_dir, exist_ok = True)
    for case in test_retest:
        case = case[0]
        ct_uri = case['uri']
        patient_uri = ct_uri.split('/studies/')[0]
        study_uri = ct_uri.split('/series/')[0]

        run_parameters = {"backend_url": BACKEND_URL,
                  "backend_user": BACKEND_USER,
                  "backend_pass": BACKEND_PASS,
                  "overlay_orientation": {
                      "cor": False,
                      "original": False,
                      "sag": False,
                      "ax": True
                  },
                  "patient_uri": patient_uri,
                  "study_uri": study_uri,
                  "ct_uri": ct_uri,
                  "icobrain_report_type": report_type
                  }


        pipeline.set_delete_temp_folders(False)
        pipeline.run(run_parameters_dict=run_parameters)
        results_file = os.path.join(study_dir, case['id']+case['series_type']+'.json')
        with open(results_file, 'w')   as j_file:
            json.dump(pipeline.get_all_results()[0], j_file, indent = 2)