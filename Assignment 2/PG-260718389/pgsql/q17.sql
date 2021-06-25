select vid, count(distinct eid) as numevents from schedule
group by vid union
	select ven.vid, 0 as numevents from venue ven
	where ven.vid not in (select distinct vid from schedule)
order by vid;
