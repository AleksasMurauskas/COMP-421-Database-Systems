select vid from venue 
where  vid not in (
	select vid from calendar
	where (date ='2020-01-17') and (area ='A'))
order by vid;