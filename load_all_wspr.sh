#!/bin/bash

#collectwsprdata.sh

#This script downloads the monthly wspr data file, uses awk and gz
#to collect information on a specific callsign, and inserts the resulting
#data into a sqlite database table.

#cd ${HOME}/tom_bin

cd /cygdrive/c/bingroot/Development/WSPR-stats/
. collectwsprdata.conf

sqlite3 -batch "${db_file}" <<EOF
delete from wspr_load;
.separator "${field_terminater}"
.import "${all_load_filename}" "${load_table}"
EOF
