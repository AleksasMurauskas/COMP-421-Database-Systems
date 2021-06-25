import psycopg2
import sys
import pandas as pd
import matplotlib.pyplot as plt


def main():

	movieIndexQuery= """CREATE INDEX employeeNames ON Employee(name);"""

	#connect to database
	passw = "Cinema2078"
	#print("please enter the password for cs421g78:")
	#pw= str(input())
	connection = psycopg2.connect(user="cs421g78",
		password=passw,
		host="comp421.cs.mcgill.ca",
		port="5432",
		database="cs421")
	print("Welcome to the CinemaClub Databse Interace")
	print("")
	display_menu()

	while(1): #infinite loop for user inputs 
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
			processOne(connection)
			print('Do you wish to continue? (Y/N)')
			exitq=input()
			if exitq=='N':
				exit_prog(connection)
			else:
				display_menu()

		elif(int(use_in)==2):
			processTwo(connection)
			print('Do you wish to continue? (Y/N)')
			exitq=input()
			if exitq=='N':
				exit_prog(connection)
			else:
				display_menu()

		elif(int(use_in)==3):
			processThree(connection)
			print('Do you wish to continue? (Y/N)')
			exitq=input()
			if exitq=='N':
				exit_prog(connection)
			else:
				display_menu()

		elif(int(use_in)==4):
			processFour(connection)
			print('Do you wish to continue? (Y/N)')
			exitq=input()
			if exitq=='N':
				exit_prog(connection)
			else:
				display_menu()

		elif(int(use_in)==5):
			processFive(connection)
			print('Do you wish to continue? (Y/N)')
			exitq=input()
			if exitq=='N':
				exit_prog(connection)
			else:
				display_menu()
		else:
			print("Invalid Input, please try again")


def processOne(connection): #Make a New Employee
	print("What is their name?")
	new_name= str(input())
	#new_name= "Aleks"
	print("What is their address?")
	new_add= str(input())
	#new_add= "3434 St. Famille" 
	print("What is their new email?")
	new_email= str(input())
	#new_email= "avm@avm.ca"
	print("Where do they work? please enter a cid")
	new_cid= str(input())
	#new_cid= "1461"
	print("What is new employeeID?")
	new_eid= str(input())
	#new_eid= "11111"
	print("What is their starting salary?")
	new_sal= str(input())
	#new_sal= "500000"
	Query ="INSERT INTO employee(eid, cid, name, email, salary, address) VALUES('"
	Query_with_val = Query+new_eid+"', '"+new_cid+"', '"+new_name+"', '"+new_email+"','"+new_sal+"', '"+new_add+"') RETURNING eid;"
	#dat1 = pd.read_sql_query(Query_fin, connection)
	dat1 = pd.read_sql_query(Query_with_val, connection)
	dat1.set_index(['eid'])
	print(dat1)
	print(Query_with_val)


#confirmed works
def processTwo(connection): #What movie titles are screening on this date
	print("What is the date you would like to select")
	in_date =str(input())
	#in_date ="2121-02-01"
	query = "SELECT name, date from screening s, movie m where s.movieid = m.movieid and date ='2121-02-01'"
	q_input = "SELECT name from screening s, movie m where s.movieid = m.movieid and date ="
	q_fin = q_input+"'"+in_date+"';"

	dat1 = pd.read_sql_query(q_fin, connection)
	dat1.set_index(['name'])
	print("Movie Titles:\n")
	print(dat1)
	print(q_fin)


#confirmed works
def processThree(connection): #How many cinemas are have screened a movie
	print("What movie are you looking for?")
	movie =str(input())
	#movie ="quis urna. Nunc quis arcu"
	query = "SELECT count(cid) from screening s, movie m  where m.name like '%"+movie+"%' and m.movieid=s.movieid"

	dat1 = pd.read_sql_query(query, connection)
	print(dat1)
	print("Number of cinemas that screened the movie:\n")
	print(dat1['count'][0])
	print(query)


def processFour(connection): # How many Items has a customer purchased the
	print("Email of the customer?")
	email =str(input())
	#email='Quisque@sodales.co.uk'
	query="SELECT SUM(quantity) from orders o, customer c where o.custid=c.custid and c.custemail='"+email+"'"
	dat1 = pd.read_sql_query(query, connection)
	print('Total items bought')
	print(dat1['sum'][0])
	print(query)

def processFive(connection): #Show which cinemas have a room larger than 260 seats

	print("What size of room are you looking for?")
	cap=input()
	#cap=280
	query= """select address, nbr as room_nb, capacity from cinema c, room r
			where c.cid=r.cid 
			and r.capacity > """+str(cap)

	dat1 = pd.read_sql_query(query, connection)
	print(dat1.keys())
	dat1.set_index(['address', 'room_nb', 'capacity'])
	print("Cinemas:\n")
	print(dat1)
	print(query)



def exit_prog(connection):
	#close connection to database
	connection = None
	print("Exiting Program")
	sys.exit()


def display_menu():
	print("-----------------Program Menu-----------------")
	print("Enter the associted number to begin a process:")	
	print("0: Redisplay Menu")
	print("1: Create a new Employee")
	print("2: What movie screenings are on this date")
	print("3: How many cinemas are have screened a certain movie")
	print("4: How many Items has a customer purchased ")
	print("5: Show which cinemas have a room larger than x seats")
	print("10: Exit Program")

main()
