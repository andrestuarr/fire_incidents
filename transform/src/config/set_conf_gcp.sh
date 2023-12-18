#!/bin/bash
export PATH_PROJECT=/src/
export PROJECT_ID=copper-verbena-408405
export FEC_PROCESO=`date +"%Y-%m-%d"`
export DATE_TODAY=`date "+%Y%m%d"`
export GOOGLE_APPLICATION_CREDENTIALS="/src/config/copper-verbena-408405-9684e3a81d7d.json"
gcloud auth activate-service-account srv-lab-access@${PROJECT_ID}.iam.gserviceaccount.com --key-file ${GOOGLE_APPLICATION_CREDENTIALS}
gcloud config set project ${PROJECT_ID}