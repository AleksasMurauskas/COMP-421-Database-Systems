SELECT note, pro_name, date, time FROM Observation AS O 
JOIN Professional AS Pr
ON O.hosp_id = Pr.hosp_id
JOIN Patient as Pa
ON O.patient_id = Pa.patient_id
JOIN Person as Pe
ON Pe.person_id = Pa.patient_id
WHERE Pe.p_name = 'Samantha Adam'
AND note = '%breathing%'
ORDER BY date DESC,time DESC
