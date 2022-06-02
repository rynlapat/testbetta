
import os
from flask import Flask,render_template,request,send_from_directory
import mysql.connector






app = Flask(__name__)

mydatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345678', 
    database = 'newbetta')

mycursor = mydatabase.cursor()



@app.route('/')
def home():
    return render_template("/home.html")

@app.route('/home.html')
def homepage():
    return render_template("/home.html")

@app.route('/type.html')
def secondpage():
   mycursor.execute('SELECT * FROM typebetta where id=1')
   data = mycursor.fetchall()
   return render_template('type.html', output_data = data)

@app.route('/type2.html')
def secondpage2():
   mycursor.execute('SELECT * FROM typebetta where id=2')
   data2 = mycursor.fetchall()
   return render_template('type.html', output_data = data2)

@app.route('/type3.html')
def secondpage3():
   mycursor.execute('SELECT * FROM typebetta where id=3')
   data3 = mycursor.fetchall()
   return render_template('type.html', output_data = data3)

@app.route('/type4.html')
def secondpage4():
   mycursor.execute('SELECT * FROM typebetta where id=4')
   data4 = mycursor.fetchall()
   return render_template('type.html', output_data = data4)

@app.route('/type5.html')
def secondpage5():
   mycursor.execute('SELECT * FROM typebetta where id=5')
   data5 = mycursor.fetchall()
   return render_template('type.html', output_data = data5)

@app.route('/type6.html')
def secondpage6():
   mycursor.execute('SELECT * FROM typebetta where id=6')
   data6 = mycursor.fetchall()
   return render_template('type.html', output_data = data6)

@app.route('/type7.html')
def secondpage7():
   mycursor.execute('SELECT * FROM typebetta where id=7')
   data7 = mycursor.fetchall()
   return render_template('type.html', output_data = data7)

@app.route('/type8.html')
def secondpage8():
   mycursor.execute('SELECT * FROM typebetta where id=8')
   data8 = mycursor.fetchall()
   return render_template('type.html', output_data = data8)

@app.route('/type9.html')
def secondpage9():
   mycursor.execute('SELECT * FROM typebetta where id=9')
   data9 = mycursor.fetchall()
   return render_template('type.html', output_data = data9)

@app.route('/type10.html')
def secondpage10():
   mycursor.execute('SELECT * FROM typebetta where id=10')
   data10 = mycursor.fetchall()
   return render_template('type.html', output_data = data10)

@app.route('/type11.html')
def secondpage11():
   mycursor.execute('SELECT * FROM typebetta where id=11')
   data11 = mycursor.fetchall()
   return render_template('type.html', output_data = data11)

@app.route('/care.html')
def thirdpage():
   mycursor.execute('SELECT * FROM newcare where id=1')
   datacare1 = mycursor.fetchall()
   return render_template('care.html', output_data = datacare1)

@app.route('/care2.html')
def thirdpage2():
   mycursor.execute('SELECT * FROM newcare where id=2')
   datacare2 = mycursor.fetchall()
   return render_template('care.html', output_data = datacare2)

@app.route('/care3.html')
def thirdpage3():
   mycursor.execute('SELECT * FROM newcare where id=3')
   datacare3 = mycursor.fetchall()
   return render_template('care.html', output_data = datacare3)

@app.route('/care4.html')
def thirdpage4():
   mycursor.execute('SELECT * FROM newcare where id=4')
   datacare4 = mycursor.fetchall()
   return render_template('care.html', output_data = datacare4)

@app.route('/care5.html')
def thirdpage5():
   mycursor.execute('SELECT * FROM newcare where id=5')
   datacare5 = mycursor.fetchall()
   return render_template('care.html', output_data = datacare5)

@app.route('/newcare.html')
def thirdpagenew():
   mycursor.execute('SELECT * FROM newcare where id=1')
   datacarenew = mycursor.fetchall()
   return render_template('care.html', output_data = datacarenew)

@app.route('/disease.html')
def fourpage():
   mycursor.execute('SELECT * FROM disease where id=1')
   datadisease1 = mycursor.fetchall()
   return render_template('disease.html', output_data = datadisease1)



@app.route('/disease2.html')
def fourpage2():
   mycursor.execute('SELECT * FROM disease where id=2')
   datadisease2 = mycursor.fetchall()
   return render_template('disease.html', output_data = datadisease2)

@app.route('/disease3.html')
def fourpage3():
   mycursor.execute('SELECT * FROM disease where id=3')
   datadisease3 = mycursor.fetchall()
   return render_template('disease.html', output_data = datadisease3)

@app.route('/disease4.html')
def fourpage4():
   mycursor.execute('SELECT * FROM disease where id=4')
   datadisease4 = mycursor.fetchall()
   return render_template('disease.html', output_data = datadisease4)

@app.route('/disease5.html')
def fourpage5():
   mycursor.execute('SELECT * FROM disease where id=5')
   datadisease5 = mycursor.fetchall()
   return render_template('disease.html', output_data = datadisease5)

@app.route('/classification.html')
def classificationpage():
   return render_template('classification.html')






    
if __name__ == '__main__':
    app.run(debug=True)
