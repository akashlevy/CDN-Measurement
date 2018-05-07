alter table results change `access-control-allow-origin` `access-control-allow-origin` VARCHAR(1024);


create table my_table_copy as
  select * from my_table


COPY tor_hostname_rev_map FROM '/home/ubuntu/tor/revdns.txt' WITH (FORMAT csv);