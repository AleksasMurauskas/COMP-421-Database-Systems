SELECT org.oid
FROM   event even, host host_obj, schedule schd, organization org, venue ven
WHERE  (ven.vid = ALL (
            SELECT venue.vid
            FROM venue
            WHERE (venue.area = 'C')) and (ven.vid = schd.vid) and(org.oid = host_obj.oid) AND (even.eid = host_obj.eid) AND (even.eid = schd.eid))
ORDER BY org.oid;