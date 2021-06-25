import psycopg2
import sys
import pandas as pd
import matplotlib.pyplot as plt


def main():
	#connect to database
	#passw = ######
	#print("please enter the password for cs421g78:")
	#pw= str(input())
	connection = psycopg2.connect(user="postgres",
		password=passw,
		host="comp421.cs.mcgill.ca",
		port="5432",
		database="421 Final")
	print("Welcome to the Hospital database")
	int input_id = argv[1]
	Query ="SELECT pro_name from Professional where hosp_id ="+input_id+";"
	try: #check for SQL Error
		dat1 = pd.read_sql_query(Query_with_val, connection)
		dat1.set_index(['pro_name'])
	except Exception as e:
		print ("Oops! An exception has occured:", e)
        print ("Exception TYPE:", type(e))
        identifaction_failure(connection)
	if(dat1.empty):
		identifaction_failure(connection)
	print("Login Successful. Welcome!")	
	while(1): #infinite loop for user inputs 
		display_menu()
		print("Input:", end=" ")
		use_in= str(input())
		if(use_in==""):
			print("Invalid Input, please try again")
			continue
		elif(int(use_in)==0): #prompted menu to be displayed  
			display_menu()
		elif(int(use_in)==10): # prompted exit 
			exit_prog(connection)
		elif(int(use_in)==1):
			makeObservation(connectionm,input_id)
			print('Do you wish to continue? (Y/N)')
			exitq=input()
			if exitq=='N':
				exit_prog(connection)
			else:
				display_menu()
		else:
			print("Invalid Input, please try again")


def makeObservation(connectionm input_id): #Make Observation 
	print("What is the Patient ID?")
	patID= str(input())
	Query ="SELECT patient_id from Patient where patient_id ="+patID+";"
	try:
		dat2 =pd.read_sql_query(Query)
		dat2.set_index(['patient_id'])
	except Exception as e
		print ("Oops! An exception has occured:", e)
        print ("Exception TYPE:", type(e))
        return
    if(dat2.empty):
		print("The entered Patient ID does not exist within the database.")
		return
	#patID= "1"
	print("What is the Time? hh:mm:ss")
	time= str(input())
	#time= ""
	print("What is the Date? YYYY-MM-DD")
	newDate= str(input())
	#newDate =""
	#new_oid= "1461"
	print("Please Record your observations now")
	new_note= str(input())
	#new_note= "Discomfort Breathing, Fever, Excessive Sweat"
	#dat3= pd.DataFrame({'observe_id' : [new_oid],'time' : [time], 'hosp_id' : [input_id], 'patient_id':[patID], 'note' : [new_note] })
	print("Please Record your observations now")
	oid= str(input())
	Query ="INSERT INTO Observation (observe_id,date,time,hosp_id,patient_id,note) VALUES ("+oid+","+newDate+","+time+",'"+input_id+","+patID+", '"+new_note+"');"
	try:
		cursor = connection.cursor()
		cursor.execute(Query)
		connection.commit()
		cursor.close()
	except Exception as e:
		print ("Oops! An exception has occured:", e)
        print ("Exception TYPE:", type(e))
        print("Please try again!")
        return
	

def identifaction_failure(connection):
	#close connection to database
	connection.close()
	print("Login Attempt failed, Exiting Program")
	sys.exit()


def exit_prog(connection):
	#close connection to database
	connection.close()
	print("Exiting Program")
	sys.exit()

def display_menu():
	print("-----------------Program Menu-----------------")
	print("Enter the associted number to begin a process:")	
	print("0: Redisplay Menu")
	print("1: Enter a petient Observation")
	print("10: Exit Program")

main()