SELECT type , AVG(price) AS averageamount
FROM schedule schd
LEFT JOIN event even ON schd.eid=even.eid
where type is not null
Right JOIN calendar cal on (schd.vid = cal.vid AND schd.date=cal.date)
GROUP BY type
ORDER BY type;