copy (
select top_url, url, method from http_requests_view where url not like ('%' || substring(top_url from 8) || '%') and url <> 'https://search.services.mozilla.com/1/firefox/41.0.2/release/en-US/US/default/default'
) to '/tmp/hetero' (format csv);