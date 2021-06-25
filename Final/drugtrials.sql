SELECT D.drugname,
COUNT  (distinct CASE WHEN status = 'recovered' then Pa.patient_id else NULL END)   AS Recovered,
COUNT ( DISTINCT (
	CASE WHEN status = 'deceased' then Pa.patient_id when status = 'infected' then Pa.patient_id else null END)
) AS NotRecovered
FROM Administration A
JOIN Patient Pa 
ON A.patient_id = Pa.patient_id
JOIN Person as Pe
ON Pe.person_id = Pa.patient_id
JOIN Drug D
ON A.drugname = D.drugname
GROUP BY (D.drugname);