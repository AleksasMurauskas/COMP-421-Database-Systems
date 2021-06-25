SELECT b_name, Count(patient_id) AS Infected
FROM Patient as Pa
JOIN Person as Pe
ON Pe.person_id = Pa.patient_id
GROUP BY b_name
ORDER BY Infected DESC, b_name 
