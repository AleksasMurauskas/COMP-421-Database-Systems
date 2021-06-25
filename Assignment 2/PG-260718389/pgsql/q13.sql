select count (pid) as numpeople from participate 
where pid in (
	select distinct pid from participate
	where eid in(
		select eid from host
		where oid ='1'));