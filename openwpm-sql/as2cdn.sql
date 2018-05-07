COPY (
SELECT DISTINCT hrv.top_url, h2aso.asorg
FROM http_requests_view AS hrv
JOIN hostname2asorg h2aso ON
SUBSTRING(url FROM '.*://([^:/]*)') = h2aso.hostname
AND h2aso.hostname <> 'search.services.mozilla.com'
)
TO '/tmp/as2cdn' (format CSV);

SELECT DISTINCT hrv.top_url, h2aso.asorg
FROM http_requests_view AS hrv
JOIN hostname2asorg h2aso ON
SUBSTRING(url FROM '.*://([^:/]*)') = h2aso.hostname
AND h2aso.hostname <> 'search.services.mozilla.com';

SELECT DISTINCT hrv.top_url, h2aso.asorg
FROM (SELECT * FROM http_requests_view LIMIT 100000) AS hrv
JOIN hostname2asorg h2aso ON
SUBSTRING(url FROM '.*://([^:/]*)') = h2aso.hostname
AND h2aso.hostname <> 'search.services.mozilla.com';


COPY (
SELECT top_url FROM site_visits
)
TO '/tmp/top-1m-openwpm.csv' (format CSV);