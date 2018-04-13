#!/bin/bash

DIR="/opt/nsivyer/pen-test"
RES_DIR="${DIR}/results"
EXCLUSIONS="${DIR}/exclusions.csv"

RES=$(find $RES_DIR -type f -exec cat {} \; |grep open | grep -vf <(cat $EXCLUSIONS | grep "^[0-9]"))
RES_COUNT=$(find $RES_DIR -type f -exec cat {} \; |grep open | grep -vf <(cat $EXCLUSIONS | grep "^[0-9]") | wc -l )

if [ $RES_COUNT -eq 0 ] ; then
	echo "OK: no open ports detected."
	exit 0
fi
echo "CRITICAL: Open ports detected. $RES"
exit 2
