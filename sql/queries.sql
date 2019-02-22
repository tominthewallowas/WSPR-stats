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