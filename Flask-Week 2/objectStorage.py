from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import json
import requests
import os
import ibm_boto3
from ibm_botocore.client import Config, ClientError
import webbrowser


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=llg82607;PWD=EdHlqvBrvtwBASW1",'','')
print(conn)

app=Flask(__name__)




#default home page or route
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/hero')
def home():
    return render_template("index.html")


#login page
@app.route('/login1')
def login():
    return render_template('login1.html')

@app.route('/hero')
def hom11():
    return render_template('index.html')
      
@app.route('/test')
def prediction():
    return render_template('test.html')

@app.route('/result',methods = ['POST'])
def abcd():
    if request.method=="POST":
       f=request.files['image']
       basepath=os.path.dirname(__file__) #getting the current path i.e where app.py is present
       #print("current path",basepath)
       filepath=os.path.join(basepath,'uploads',f.filename) #from anywhere in the system we can give image but we want that image later  to process so we are saving it to uploads folder for reusing
       #print("upload folder is",filepath)
       f.save(filepath)
    # connecting with cloud object storage
    
       COS_ENDPOINT = "https://s3.ams03.cloud-object-storage.appdomain.cloud"
       COS_API_KEY_ID = "3T2J7yqxl55YhitAFrnO1ie3oQwMmMqkmw3XVPEmbYWn"
       COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/17189f8889664253b05df231485c4df1:3d33850c-cd49-47df-87bb-ab1543faafcd::"
       cos = ibm_boto3.client("s3",ibm_api_key_id=COS_API_KEY_ID,ibm_service_instance_id=COS_INSTANCE_CRN, config=Config(signature_version="oauth"),endpoint_url=COS_ENDPOINT)
       cos.upload_file(Filename= filepath,Bucket='srikanthtest',Key='test.jpg')
       '''
       url = "https://vehicle-damage-assessment.p.rapidapi.com/run"

       payload = {"draw_result": True,"image": "https://srikanthtest.s3.ams03.cloud-object-storage.appdomain.cloud/test.jpg"}
       headers = {"content-type": "application/json","X-RapidAPI-Key": "080d896cfemsh8f31dd900f9473bp1b1177jsncbe24a43d48b","X-RapidAPI-Host": "vehicle-damage-assessment.p.rapidapi.com"}

       response = requests.request("POST", url, json=payload, headers=headers)
       output = response.json() 
       print(output)
       url = output['output_url']
  
# then call the default open method described above
       
       
       webbrowser.open(url)
       cos.upload_file(Filename= "result/test.jpg",Bucket='srikanthtest',Key='result.jpg')
      
       return  render_template('result.html')
     '''

@app.route('/')
def home31():
    return render_template('index.html')


@app.route('/about')
def home4():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False,port = 5050)
