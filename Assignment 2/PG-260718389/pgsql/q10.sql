select vid, area, capacity from venue ven 
where ven.vid in (
	select vid from schedule schd
	where EXISTS ( 
		SELECT oid,eid from host host_obj 
		where (schd.eid = host_obj.eid)and (host_obj.oid ='6'))
order by vid, capacity;


