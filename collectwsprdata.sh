#!/bin/bash

#collectwsprdata.sh

#This script downloads the monthly wspr data file, uses awk and gz
#to collect information on a specific callsign, and inserts the resulting
#data into a mysql database table.

cd ${HOME}/bin
. collectwsprdata.conf

echo $0
echo $#

if [ $# -eq 1 ]
then
  wspr_file_name=$wspr_file_base_name_beginning$1$wspr_file_base_name_end
else
  #wspr_file_name=$wspr_file_base_name_beginning$(date --date="1 month ago" +%Y-%m)$wspr_file_base_name_end
  wspr_file_name=$wspr_file_base_name_beginning$(date +%Y-%m)$wspr_file_base_name_end
fi

echo $wspr_file_name
#exit

#Testing download file name
#wspr_file_name=wb7eux.csv.gz

wget $wspr_file_location$wspr_file_name

awk '/WB7EUX/' <(gzip -dc $wspr_file_name) > $output_file_name

mysqlimport -u $user -p$password -h $server --fields-terminated-by=',' -S'/opt/lampp/var/mysql/mysql.sock' $database $output_file_name

#rm $output_file_name $wspr_file_name

