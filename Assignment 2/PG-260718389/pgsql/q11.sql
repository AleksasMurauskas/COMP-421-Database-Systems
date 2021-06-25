select distinct pid, pname from person
where pid in(
	select pid from participate
	where eid in (
		select eid from participate
		where pid = '12345678'))
order by pid;