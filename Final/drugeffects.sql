SELECT COUNT ( DISTINCT
	CASE 
	when note ='%dizz%' then Pa.patient_id 
	else 0  END 
)
FROM Patient Pa
JOIN Observation O
ON Pa.patient_id=O.patient_id