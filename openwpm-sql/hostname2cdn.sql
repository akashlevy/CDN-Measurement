COPY (
SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN cname_map cm ON
hrv.url LIKE '%' || cm.cname || '%'
)
TO '/tmp/cname2cdn' (format CSV);

SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN cname_map cm ON
hrv.url LIKE '%' || cm.cname || '%';

SELECT DISTINCT hrv.top_url, cm.cdn
FROM (SELECT * FROM http_requests_view LIMIT 100000) AS hrv
JOIN cname_map cm ON
hrv.url LIKE '%' || cm.cname || '%';

SELECT cdn, COUNT(*) FROM (
    SELECT DISTINCT hrv.top_url, cm.cdn
    FROM http_requests_view AS hrv
    JOIN cname_map cm ON
    hrv.url LIKE '%' || cm.cname || '%'
) cdn_tab GROUP BY cdn;