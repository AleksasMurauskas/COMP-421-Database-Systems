select vid, capacity from venue
where (area ='C') and vid IN (
	select vid from calendar
	where (date = '2020-01-16') and (price < 100))
order by vid;
