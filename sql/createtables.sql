CREATE TABLE wspr_load (
  spot_id int(11) NOT NULL PRIMARY KEY,
  timestamp int(11) DEFAULT NULL,
  reporter varchar(10) DEFAULT NULL,
  reporter_grid varchar(10) DEFAULT NULL,
  signal_noise_ratio int(11) DEFAULT NULL,
  receive_frequency_mhz decimal(12,6) DEFAULT NULL,
  xmit_callsign varchar(10) DEFAULT NULL,
  xmit_grid varchar(10) DEFAULT NULL,
  xmit_power int(11) DEFAULT NULL,
  xmit_drift int(11) DEFAULT NULL,
  distance int(11) DEFAULT NULL,
  azimuth int(11) DEFAULT NULL,
  band int(11) DEFAULT NULL,
  version varchar(10) NOT NULL,
  code int(11) DEFAULT NULL
);

CREATE TABLE wspr_stats (  spot_id int(11) NOT NULL PRIMARY KEY,  timestamp int(11) DEFAULT NULL,  reporter varchar(10) DEFAULT NULL,  reporter_grid varchar(10) DEFAULT NULL,  signal_noise_ratio int(11) DEFAULT NULL,  receive_frequency_mhz decimal(12,6) DEFAULT NULL,  xmit_callsign varchar(10) DEFAULT NULL,  xmit_grid varchar(10) DEFAULT NULL,  xmit_power int(11) DEFAULT NULL,  xmit_drift int(11) DEFAULT NULL,  distance int(11) DEFAULT NULL,  azimuth int(11) DEFAULT NULL,  band int(11) DEFAULT NULL,  version varchar(10) NOT NULL,  code int(11) DEFAULT NULL);

create index wspr_stats_reporter_idx on wspr_stats(reporter);

create index wspr_stats_xmit_callsign_idx on wspr_stats(xmit_callsign);