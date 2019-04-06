select count(*) from wspr_stats where xmit_callsign='WB7EUX' or reporter='WB7EUX';

select count(*) from wspr_stats;

select count(*) from wspr_load;

select xmit_callsign, count(*) as xmit_callsign_count from wspr_load where xmit_callsign='WB7EUX' group by xmit_callsign;

select reporter, count(*) as reporter_count from wspr_load where reporter='WB7EUX' group by reporter;

select reporter.* from (select reporter, count(*) as reporter_count from wspr_load where reporter='WB7EUX' group by reporter) reporter;

select xmit.* from (select xmit_callsign, count(*) as xmit_callsign_count from wspr_load where xmit_callsign='WB7EUX' group by xmit_callsign) xmit;

select r.* from (select reporter, count(*) as reporter_callsign_count from wspr_stats where reporter='WB7EUX' group by reporter) r;

select t.* from (select xmit_callsign, count(*) as xmit_callsign_count from wspr_stats where xmit_callsign='WB7EUX' group by xmit_callsign) t;

select r.reporter, r. reporter_callsign_count, t.xmit_callsign_count from (select reporter, count(*) as reporter_callsign_count from wspr_stats where reporter='WB7EUX' group by reporter) r, (select xmit_callsign, count(*) as xmit_callsign_count from wspr_stats where xmit_callsign='WB7EUX' group by xmit_callsign) t where r.reporter=t.xmit_callsign;

-- I think WA7X is a band hopper so I will track his call sign for a while
select band, count(*) as band_count from wspr_stats where xmit_callsign in ('WA7X') group by band

select reporter, reporter_grid, signal_noise_ratio, receive_frequency_mhz, xmit_callsign, xmit_grid, xmit_power, xmit_drift, distance, azimuth from wspr_stats;

# Statements in sqlstatements.py
combined="select r.reporter, r. reporter_callsign_count, t.xmit_callsign_count from (select reporter, count(*) as reporter_callsign_count from wspr_stats where reporter='WB7EUX' group by reporter) r, (select xmit_callsign, count(*) as xmit_callsign_count from wspr_stats where xmit_callsign='WB7EUX' group by xmit_callsign) t where r.reporter=t.xmit_callsign"

distinct_band = "select distinct band from wspr_stats"

reporter_count = "select reporter, count(*) as 'Reporter Count' from wspr_stats where xmit_callsign = 'WB7EUX' group by reporter"

xmit_callsigns = "select distinct xmit_callsign, xmit_grid from wspr_stats order by xmit_callsign"

reporter_callsigns = "select distinct reporter, reporter_grid from wspr_stats order by reporter"

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

select CASE band WHEN 1 THEN '160m' WHEN 3 THEN '80m' ELSE band END as Band,
count(*) from wspr_stats where reporter = 'WB7EUX' or xmit_callsign = 'WB7EUX' group by band

select reporter as Reporter, reporter_grid as 'Rpt Grid', xmit_callsign as 'Transmitter', xmit_grid as 'Xmit Grid', xmit_power as Power, distance as 'Distance(km)', datetime(timestamp, 'unixepoch') as 'Date/Time', signal_noise_ratio as SNR from wspr_stats where reporter = :callsign or xmit_callsign = :callsign order by reporter, xmit_callsign