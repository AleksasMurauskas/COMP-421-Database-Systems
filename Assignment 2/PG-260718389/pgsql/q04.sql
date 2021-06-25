select ven.vid, ven.capacity from venue ven
where ven.vid IN(
	select cal.vid from calendar cal
	where (cal.price < 100) and(ven.area = 'C') and (cal.date = '2020-01-16'))
order by ven.vid;