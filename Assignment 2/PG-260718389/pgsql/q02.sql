select ven.vid, capacity
from venue ven join calendar cal on  cal.vid=ven.vid
where (price < 100) and (date = '2020-01-16') and (area = 'C')
order by vid;

