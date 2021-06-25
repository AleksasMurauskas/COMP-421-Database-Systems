select vid, capacity from venue 
where  (capacity >100) AND ((area ='A' OR area ='B') )
order by capacity DESC, vid;

