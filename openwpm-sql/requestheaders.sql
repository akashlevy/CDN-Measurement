SELECT COUNT(*)
FROM http_request_headers_view hrhv
WHERE hrhv.name = 'Referer'
JOIN http_request_view



select * from http_header_names WHERE LOWER(name) like 'referer' OR LOWER(name) like 'referrer';
select count(*) from http_request_headers where name_id = 8;


select count(*) from http_request_headers where name_id = 8 join http_request_view on 





(select * from http_header_names WHERE LOWER(name) like 'referer' OR LOWER(name) like 'referrer')

(select * from http_header_names WHERE LOWER(name) like 'origin')

SELECT COUNT(DISTINCT http_request_headers.request_id) FROM http_request_headers WHERE name_id = 8 AND request_id NOT IN
(
    SELECT request_id FROM http_request_headers
    WHERE name_id = 13 OR name_id = 125 OR name_id = 131
    LIMIT 1000
);

