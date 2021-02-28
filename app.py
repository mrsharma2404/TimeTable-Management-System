from flask import Flask,render_template,request
import mysql.connector
from flask import *
import logging, os
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key = "abc"  


#this is for record management 
app.add_url_rule('/uploads/<path:filename>', endpoint='uploads',
                 view_func=app.send_static_file)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath
#till here


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/std')
def student():
    return render_template("studentlogin.html")

@app.route('/fac')
def faculty():
    return render_template("facultylogin.html")

@app.route('/adm')
def admin():
    return render_template("adminlogin.html")

@app.route('/slog',methods =["POST"])
def stlogin():
    n1=request.form["t1"]
    n2=request.form["t2"]
    if n1=='admin' and n2=='abcd':
        return render_template('studentbranch.html')
    else:
        return "abcd"

@app.route('/flog',methods =["POST"])
def fclogin():
    n1=request.form["t1"]
    n2=request.form["t2"]
    if n1=='admin' and n2=='abcd':
        return render_template('facultysearch.html')
    else:
        return "abcd"

@app.route('/alog',methods =["POST"])
def adlogin():
    n1=request.form["t1"]
    n2=request.form["t2"]
    if n1=='admin' and n2=='abcd':
        return render_template('a_addnew.html')
    else:
        return "abcd"

@app.route('/sloged',methods =["POST"])
def submit():
    n1=request.form["t11"]
    n2=request.form["t12"]
    n3=request.form["t13"]
    print(n1,n2,n3)
    #if (n1=='B.Tech' and n2=='Fifth Semester') and (n3=='Computer Science Engineering III'):       
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("select * from timetable where batch = '"+n3+"' and semester = '"+n2+"'")
    detail = c.fetchall()               
    return render_template('studentbranch.html',data = detail)
    
    

@app.route('/floged', methods =["POST"])
def search():
    n11=request.form["f1"]  
     
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("SELECT * FROM timetable where faculty_name = '"+n11+"' ")
    fdetail = c.fetchall()           
    con.commit()
    return render_template('facultysearch.html',data = fdetail)
 

@app.route('/addnew', methods= ["POST"])
def submit15():
    n1=request.form["t41"]
    n2=request.form["t42"]
    n3=request.form["t43"]
    n4=request.form["t44"]
    n5=request.form["t45"]
    n6=request.form["t46"]
    n7=request.form["t47"]
    n8=request.form["t48"]
    n9=request.form["t49"]
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("select faculty_name, day, time from timetable where faculty_name = '"+n1+"'  and day = '"+n3+"' and time = '"+n4+"'    ")
    if(c.fetchone()):
        return "Teacher is already assigned for another lacture "
    else:
        c.execute("insert into timetable (faculty_name, date, day, time, classroom, course, semester, batch, subject_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (n1, n2, n3, n4, n5, n6, n7, n8, n9))     
        con.commit()
        return "okay"
    #flash("you are successfuly logged in")  
    #return redirect('/addnew')
    

@app.route('/showtable', methods=["POST"])
def getdetail123():
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("select * from timetable")
    detail = c.fetchall()           
    con.commit()
    return render_template('a_addnew.html',data = detail)

@app.route('/admsearchdetail',methods=['POST'])
def getsearch():
    n31=request.form["t31"]
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("select * from timetable where faculty_name = '"+n31+"' or day = '"+n31+"' or date = '"+n31+"' or subject_code = '"+n31+"' or semester = '"+n31+"' or classroom = '"+n31+"' or time = '"+n31+"' or batch = '"+n31+"' or course = '"+n31+"' ")
    detail = c.fetchall()           
    con.commit()
    return render_template('a_addnew.html',data = detail)


@app.route('/admdelete' , methods=["POST"])
def submit14():
    n61=request.form["t61"]
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("delete from timetable where faculty_name = '"+n61+"' or day = '"+n61+"'  or date = '"+n61+"' ")     
    con.commit()
    return "done"

@app.route('/admonedelete' , methods=["POST"])
def submit144():
    nd1=request.form["t51"]
    nd2=request.form["t52"]
    nd3=request.form["t53"]
    nd4=request.form["t54"]
    nd5=request.form["t55"]
    nd6=request.form["t56"]
    nd7=request.form["t57"]
    nd8=request.form["t58"]
    nd9=request.form["t59"]
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("delete from timetable where faculty_name = '"+nd1+"' and date = '"+nd2+"'  and day = '"+nd3+"' and time = '"+nd4+"'  and classroom = '"+nd5+"'  and course = '"+nd6+"'  and semester = '"+nd7+"'  and batch = '"+nd8+"'   and subject_code = '"+nd9+"'      ")     
    con.commit()
    return "done"







#new updation here for records
##


@app.route('/record0')
def record0():
    return render_template("records0.html")

@app.route('/record')
def record():
    return render_template("records1.html")

@app.route('/record1', methods= ["POST"])
def recsub():
    n1=request.form["fname"]
    n2=request.form["fid"]
    img = request.files['iname']
    
    img_name = secure_filename(img.filename)
    
    create_new_folder(app.config['UPLOAD_FOLDER'])
    saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    
    app.logger.info("saving {}".format(saved_path))

    img.save(saved_path)

    
    n4=request.form["dob"]
    n5=request.form["mob"]
    n6=request.form["add"]
    n7=request.form["jd"]
    n8=request.form["slr"]
    n9=request.form["qfc"]
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("insert into record (faculty_name, faculty_id, image, dob, mobile, address, join_date, salary, qualification) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (n1, n2, img_name, n4, n5, n6, n7, n8, n9))     
    con.commit()
    #flash("you are successfuly logged in")  
    #return redirect('/addnew')
    return "okay"

@app.route('/record2')
def record111():
    return render_template("records2.html")

@app.route('/record3', methods=["POST","GET"])
def rcshow():
    nf1 = request.form['f11']
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("select * from record where faculty_name = '"+nf1+"' ")
    record = c.fetchall()           
    con.commit()
    return render_template('records2.html',data = record)

@app.route('/record4', methods=["POST","GET"])
def rcsshow():
    con=mysql.connector.connect(host="localhost", user="root", password="", db="project2")
    c=con.cursor()
    c.execute("select faculty_name from record ")
    record = c.fetchall()           
    con.commit()
    return render_template('records2.html',data1 = record)



#jinja here 
@app.route('/sum')
def student12():
        return render_template('studentx.html')

@app.route('/result', methods = ['POST', 'GET'])
def result21():
        if request.method == 'POST':
                result = request.form
                return render_template('resultx.html', result = result)



if __name__=='__main__':
    app.run(debug=True)