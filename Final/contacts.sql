SELECT p_name, email, phoneNbr FROM Person p JOIN Contact c
on p.person_id = c.person_id
Where c.patient_id =(
Select person_id from patient WHERE
email = 'dub.vizer@br.com');