select oid, oname from organization
where oid in (
	select oid from host
	where eid in (
		select eid from (
			select eid, count (date) as counted_date from schedule
			group by eid)
		as temp_num_count
		where counted_date > 2))
ORDER BY oid;