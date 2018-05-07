COPY (
SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN hostname_cname_map hcm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hcm.hostname
JOIN cname_map cm ON
hcm.cname LIKE '%' || cm.cname || '%'
)
TO '/tmp/cname2cdn' (format CSV);

SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN hostname_cname_map hcm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hcm.hostname
JOIN cname_map cm ON
hcm.cname LIKE '%' || cm.cname || '%';

SELECT DISTINCT hrv.top_url, cm.cdn
FROM (SELECT * FROM http_requests_view LIMIT 100000) AS hrv
JOIN hostname_cname_map hcm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hcm.hostname
JOIN cname_map cm ON
hcm.cname LIKE '%' || cm.cname || '%';