COPY (
SELECT DISTINCT hrv.top_url, hm.cdn
FROM http_responses_view AS hrv
JOIN http_response_headers_view AS hrh ON
hrh.response_id = hrv.id
JOIN header_map hm ON
hrh.name = hm.header_key
AND (hrh.value = hm.header_value OR hm.header_value = '')
)
TO '/tmp/header2cdn' (format CSV);

SELECT DISTINCT hrv.top_url, hm.cdn
FROM http_responses_view AS hrv
JOIN http_response_headers_view AS hrh ON
hrh.response_id = hrv.id
JOIN header_map hm ON
hrh.name = hm.header_key
AND (hrh.value = hm.header_value OR hm.header_value = '');

SELECT DISTINCT hrv.top_url, hm.cdn
FROM (SELECT * FROM http_responses_view LIMIT 10000) AS hrv
JOIN http_response_headers_view AS hrh ON
hrh.response_id = hrv.id
JOIN header_map hm ON
hrh.name = hm.header_key
AND (hrh.value = hm.header_value OR hm.header_value = '');
