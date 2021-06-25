select eid, date from schedule schd
where schd.eid in (
	select eid from participate
	where pid = '12345678' and eid not in (
		select eid from participate where pid = '12345679'))
and schd.eid in (
	select eid from event
	where type = 'music') 
order by eid DESC, date;

