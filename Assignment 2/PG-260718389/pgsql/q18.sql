select vid, count(distinct eid) as numevents from schedule
group by vid
order by vid;
