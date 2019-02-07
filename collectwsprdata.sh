#!/bin/bash

#collectwsprdata.sh

#This script downloads the monthly wspr data file, uses awk and gz
#to collect information on a specific callsign, and inserts the resulting
#data into a sqlite database table.

#cd ${HOME}/tom_bin
cd /cygdrive/c/bingroot/Development/WSPR-stats/
. collectwsprdata.conf

if [ $# -eq 1 ]
then
  wspr_filename=$wspr_file_base_name_beginning$1$wspr_file_base_name_end
else
  wspr_filename=$wspr_file_base_name_beginning$(date +%Y-%m)$wspr_file_base_name_end
fi

echo $wspr_filename

wget $wspr_file_location$wspr_filename

awk '/M0RNR/' <(gzip -dc $wspr_filename) > $output_filename

sqlite3 -batch "${db_file}" <<EOF
delete from wspr_load;
.separator "${field_terminater}"
.import "${output_filename}" "${load_table}"
EOF

rm $output_filename $wspr_filename
