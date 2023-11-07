

import os
from flask import Flask,request,session,redirect, url_for, flash
import boto3, botocore

app = Flask(__name__)
app.secret_key = 'khh79kjh2h'
available_country=['India','Singapore','Inodensia','Japan','USA']

ALLOWED_EXTENSIONS = set(['pdf', 'docx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def s3_upload_small_files(inp_file_name, s3_bucket_name, inp_file_key, content_type):
    # client = boto3.s3_client()
    upload_file_response = s3.put_object(Body=inp_file_name,
                                             Bucket=s3_bucket_name,
                                             Key=inp_file_key,
                                             ContentType=content_type)
    print(f"Response - {upload_file_response}")



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return '''
        <h1>Welcome to SearchIn</h1>
            <form method="POST">
                <p1>Enter the country name: </p1>
                <input type="text" name="text_content">
                <input type="submit">
            </form>


            <form action="/upload_files_to_s3" method="POST" enctype="multipart/form-data">
                <label for="user_file">Upload Your Resume:</label>
                 <input type="file" name="file" multiple="true" autocomplete="off" required>
                <br><br>
                <button type="submit">Upload</button>
            </form>
        '''
    session['content'] = request.form['text_content']
    return redirect("/show")

@app.route("/show")
def show():
    if session["content"].lower() in (country.lower() for country in available_country):
        return f'<h1>We operate in :</h1>{session["content"]}'
    else:
        return f'<h1>We done operate in</h1>{session["content"]}'



@app.route('/upload_files_to_s3', methods=['GET', 'POST'])
def upload_files_to_s3():
    if request.method == 'POST':
 
        # If no file is selected
        if 'file' not in request.files:
            flash(f'No files Selected', 'danger')
        
        file_to_upload = request.files['file']
        content_type = request.mimetype
 
        # if files is empty
        if file_to_upload.filename == '':
            flash(f'No files Selected', 'danger')
 
        # file uploaded and check
        if file_to_upload and allowed_file(file_to_upload.filename):
            file_name=file_to_upload.filename
            print(f"The file name to upload is {file_name}")
            print(f"The file full path  is {file_to_upload}")
 
            bucket_name = os.getenv('AWS_BUCKET_NAME')
 
            s3_upload_small_files(file_to_upload, bucket_name, file_name,content_type )
            flash(f'Success - {file_to_upload} Is uploaded to {bucket_name}', 'success')

        else:
            flash(f'Please upload proper formats.', 'danger')
 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)