#!/bin/bash

#load_all_wspr.sh

#This script loads all rows from an existing data file into a sqlite
#database table.  This data is for analysis and design considerations and,
#at this writing, not intended for production.

#cd ${HOME}/tom_bin

cd /cygdrive/c/bingroot/Development/WSPR-stats/
. collectwsprdata.conf

sqlite3 -batch "${db_file}" <<EOF
delete from "${all_load_table}";
vacuum;
.separator "${field_terminater}"
.import "${all_load_filename}" "${all_load_table}"
EOF
