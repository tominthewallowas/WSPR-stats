# SQL statements

combined="select r.reporter, r. reporter_callsign_count, t.xmit_callsign_count from (select reporter, count(*) as reporter_callsign_count from wspr_stats where reporter='WB7EUX' group by reporter) r, (select xmit_callsign, count(*) as xmit_callsign_count from wspr_stats where xmit_callsign='WB7EUX' group by xmit_callsign) t where r.reporter=t.xmit_callsign"
