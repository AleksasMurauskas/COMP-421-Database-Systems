select eid, numpeople from (
	select part.eid, count(distinct pid) as numpeople from 
	participate part join (select eid from event
		where type = 'fundraising') as fund_event on part.eid = fund_event.eid
	group by part.eid) 
as maximum
where numpeople >= all (
	select numpeople from (
		select part.eid, count(distinct pid) as numpeople from 
		participate part join (
			select eid from event
			where type = 'fundraising') as fund_event on part.eid = fund_event.eid
	group by part.eid) 
as data_set)
order by eid;
