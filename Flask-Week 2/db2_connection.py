from flask import Flask, render_template,request
import ibm_db
import re

app = Flask(__name__)
app.secret_key = 'a'
con = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=jvk87461;PWD=uN2EU6KgPwwj0sv3;", "", "")
print("DB Connected")

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    name=request.form['name']
    id=request.form['id']
    pas=request.form['pas']
    sql = "SELECT * FROM REGISTER WHERE NAME=?"
    smtp = ibm_db.prepare(con,sql)
    ibm_db.bind_param(smtp, 1, name)
    ibm_db.execute(smtp)
    account=ibm_db.fetch_assoc(smtp)
    print(account)
    if account:
        return render_template('login.html', error=True)
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', id):
        op = "Invalid Email Address"
    else:
        insert_sql = "INSERT INTO REGISTER VALUES (?,?,?)"
        prepSql=ibm_db.prepare(con,insert_sql)
        ibm_db.bind_param(prepSql, 1, name)
        ibm_db.bind_param(prepSql, 2, id)
        ibm_db.bind_param(prepSql, 3, pas)
        ibm_db.execute(prepSql)
        op = "You have successfully registered"
    # print(name,ID,Password)
    #op = "Welcome "+ str(name)
    return render_template('login.html',output=op)

if __name__=='__main__':
    app.run(debug=True)