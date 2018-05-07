select asorg, count(*) from hostname2asorg GROUP by asorg HAVING COUNT(*) > 10000 ORDER BY COUNT DESC;
-- will need to combine several