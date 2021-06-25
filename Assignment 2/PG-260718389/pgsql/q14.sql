select eid , sum(price) as totalamount from (
	select schd.vid, schd.date, schd.eid, cal.price from 
	calendar cal join schedule schd on cal.vid =schd.vid) 
as temp_join
group by eid
order by eid DESC;