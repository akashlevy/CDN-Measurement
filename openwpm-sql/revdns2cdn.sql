-- REGULAR

COPY (
SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN hostname_rev_map hrm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hrm.hostname
JOIN cname_map cm ON
hrm.rev_hostname LIKE '%' || cm.cname || '%'
)
TO '/tmp/tor_rev2cdn' (format CSV);

SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN hostname_rev_map hrm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hrm.hostname
JOIN cname_map cm ON
hrm.rev_hostname LIKE '%' || cm.cname || '%';

SELECT DISTINCT hrv.top_url, cm.cdn
FROM (SELECT * FROM http_requests_view LIMIT 100000) AS hrv
JOIN hostname_rev_map hrm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hrm.hostname
JOIN cname_map cm ON
hrm.rev_hostname LIKE '%' || cm.cname || '%';

-- TOR

COPY (
SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN tor_hostname_rev_map hrm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hrm.hostname
JOIN cname_map cm ON
hrm.rev_hostname LIKE '%' || cm.cname || '%'
)
TO '/tmp/tor_rev2cdn' (format CSV);

SELECT DISTINCT hrv.top_url, cm.cdn
FROM http_requests_view AS hrv
JOIN tor_hostname_rev_map hrm ON
SUBSTRING(url FROM '.*://([^:/]*)') = hrm.hostname
JOIN cname_map cm ON
hrm.rev_hostname LIKE '%' || cm.cname || '%';

SELECT cm.cdn, COUNT(*)
FROM tor_hostname_rev_map AS hrm
JOIN cname_map cm ON
hrm.rev_hostname LIKE '%' || cm.cname || '%'
GROUP BY cm.cdn
ORDER BY COUNT(*);