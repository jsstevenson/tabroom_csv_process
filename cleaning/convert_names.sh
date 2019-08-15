#!/bin/bash

# convert all older files to new naming convention
#ls | sed -En 's/(.*-.*-)([0-9]|finals|semis|quarters|octs|dubs|trips)-(.*)(.csv)/mv & \1\3-\2\4/p' | sh

# catch places where division was excluded for default=open
ls | sed -En 's/(1718-[a-zA-Z]*-)([0-9]|finals|dubs|octs|quarters|semis)(.csv)/mv & \1open-\2\3/p'