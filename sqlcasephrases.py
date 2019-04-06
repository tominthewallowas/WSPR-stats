'''Contains the ugly parts of sql CASE structures so they don't make the main code unreadable.'''

sql_power_case_phrase = \
    "CASE xmit_power \
    WHEN 0 THEN '1 mw' \
    WHEN 3 THEN '2 mw' \
    WHEN 7 THEN '5 mw' \
    WHEN 10 THEN '10 mw' \
    WHEN 13 THEN '20 mw' \
    WHEN 17 THEN '50 mw' \
    WHEN 20 THEN '100 mw' \
    WHEN 23 THEN '200 mw' \
    WHEN 27 THEN '500 mw' \
    WHEN 30 THEN '1 watt' \
    WHEN 33 THEN '2 watts' \
    WHEN 37 THEN '5 watts' \
    WHEN 40 THEN '10 watts' \
    WHEN 43 THEN '20 watts' \
    ELSE xmit_power + ' dBm' \
    END"

sql_band_case_phrase = \
    "CASE band \
    WHEN 1 THEN '160m' \
    WHEN 3 THEN '80m' \
    WHEN 5 THEN '60m' \
    WHEN 7 THEN '40m' \
    WHEN 10 THEN '30m' \
    WHEN 14 THEN '20m' \
    WHEN 18 THEN '17m' \
    WHEN 21 THEN '15m' \
    WHEN 24 THEN '12m' \
    WHEN 28 THEN '10m' \
    WHEN 50 THEN '6m' \
    ELSE band END"