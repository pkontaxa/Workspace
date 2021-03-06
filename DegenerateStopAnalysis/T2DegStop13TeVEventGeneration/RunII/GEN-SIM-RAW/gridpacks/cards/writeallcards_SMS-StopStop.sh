#!/bin/sh
JOBS="jobs"
#TEMP="templatecards"
TEMP="SMS-StopStop"
PROC="SMS-StopStop"
PART="_mStop-"

### Create cards and SLHAs for all mass points

for MPROD in {250..800..25}; do
#for MPROD in {167..817..25} {183..833..25} {825..925..50} {1250..1400..50}; do
    MODEL=${PROC}${PART}${MPROD}
    mkdir -p "${JOBS}/${MODEL}"
    cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
    sed "s/%MPROD%/${MPROD}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
    sed "s/%MPROD%/${MPROD}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
    sed "s/%MPROD%/${MPROD}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
done
