#package imports
from flask import Flask, render_template, request, redirect
from flask_smorest import abort
#local file imports 
from palindrome_processing import Palindrome
import storage_system as db

#instace flask app
app = Flask(__name__)

#Palindrome class instance 
palindrome_inst = Palindrome()

#Home Route
@app.route("/")
def get_main_route():
    #Previous value array creation
    array_prev_vals = []
    #Check if data file exists 
    if db.check_file_exists():
        #save data file to dataframe
        df = db.excel_to_df()
        #array from dataframe
        array_prev_vals = db.get_previous_vals(df)
    try:
        #try render index.html file with array     
        return render_template('index.html', previous_value_array=array_prev_vals)
    except KeyError:
        #Raise 404 if page not found 
        abort(404, message="Page not found")

#Post request returned to from html form submit
@app.post("/processing")
def post_req_from_form():
    #Get value from form
    txt_input = request.form.get("textInput")
    #run palindrome on value
    res = palindrome_inst.run(txt_input)
    #Check to see if a storage file exists and write to it
    #Else create new storage file
    db.check_if_file_exists_and_write(txt_input, res)
    try:
        #Load home route 
        return redirect("/")
    except KeyError:
        #Raise 404 if route not found 
        abort(404, message="Page not found")

