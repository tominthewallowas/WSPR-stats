# SQL statements

combined="select r.reporter, r. reporter_callsign_count, t.xmit_callsign_count from (select reporter, count(*) as reporter_callsign_count from wspr_stats where reporter='WB7EUX' group by reporter) r, (select xmit_callsign, count(*) as xmit_callsign_count from wspr_stats where xmit_callsign='WB7EUX' group by xmit_callsign) t where r.reporter=t.xmit_callsign"

distinct_band = "select distinct band from wspr_stats"

reporter_count = "select reporter, count(*) as 'Reporter Count' from wspr_stats where xmit_callsign = 'WB7EUX' group by reporter"

xmit_callsigns = "select distinct xmit_callsign, xmit_grid from wspr_stats"

reporter_callsigns = "select distinct reporter, reporter_grid from wspr_stats"

reporter_findings = "select \
    xmit_callsign as 'Xmit Call', \
    CASE xmit_power \
    WHEN 23 THEN '200 mw' \
    WHEN 27 THEN '500 mw' \
    WHEN 30 THEN '1 watt' \
    WHEN 33 THEN '2 watts' \
    WHEN 37 THEN '5 watts' \
    ELSE xmit_power + ' dBm' \
    END as 'Transmit Pwr.', \
    datetime(timestamp, 'unixepoch') as 'Date/Time', \
    signal_noise_ratio as 'SNR', \
    receive_frequency_mhz as 'Rcv Freq', \
    xmit_grid as 'Xmit Grid', \
    distance as 'Dist. (km)', \
    azimuth as 'Azimuth' \
from wspr_stats \
where reporter =  :callsign"

xmit_findings = "select \
    reporter as 'Reporter', \
    datetime(timestamp, 'unixepoch') as 'Date/Time', \
    signal_noise_ratio as 'SNR', \
    receive_frequency_mhz as 'Rcv Freq', \
    reporter_grid as 'Report Grid', \
    CASE xmit_power \
    WHEN 23 THEN '200 mw' \
    WHEN 27 THEN '500 mw' \
    WHEN 30 THEN '1 watt' \
    WHEN 33 THEN '2 watts' \
    WHEN 37 THEN '5 watts' \
    ELSE xmit_power + ' dBm' \
    END as 'Transmit Pwr.', \
    distance as 'Dist. (km)', \
    azimuth as 'Azimuth' \
from wspr_stats \
where xmit_callsign = :callsign"