import mysql.connector

def get_store_number():
  try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="xmldata"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT store_no FROM stores")
    myresult = mycursor.fetchone()
    mydb.close()
    return str(myresult[0])
  except:
    print(f"Error:: Database Connection is not established !!!!, So store_id is 56785 for now")
    return "56785"