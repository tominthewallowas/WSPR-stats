select count(*) from wspr_stats where xmit_callsign='WB7EUX' or reporter='WB7EUX';

select count(*) from wspr_stats;

select count(*) from wspr_load;

select xmit_callsign, count(*) as xmit_callsign_count from wspr_load where xmit_callsign='WB7EUX' group by xmit_callsign;

select reporter, count(*) as reporter_count from wspr_load where reporter='WB7EUX' group by reporter;
