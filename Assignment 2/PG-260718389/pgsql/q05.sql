select pid, pname from person
where pid IN(
	select pid from participate
	where (eid = 5))
order by pid;