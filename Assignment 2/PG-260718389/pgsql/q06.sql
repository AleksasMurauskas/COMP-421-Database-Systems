select oid, oname from organization
where oid in (
	select oid from host
	where eid in (
		select eid from schedule
		where (date ='2020-01-16')))
order by oid;