from cachetools import cached, TTLCache
import os.path 
import pandas as pd

#Write df to excel file
def df_to_excel(df):
    df.to_excel("Palindrome_Output.xlsx", sheet_name="Palindrome")
#Value and Status variables write to df
def to_df(value, status):
    data=[[value, status]]
    df = pd.DataFrame(data, columns=["Previous Values", "Palindrome Status"])
    return df
#Append passing in variable with value and status values 
def append_df(df, value, status):
    new_row = to_df(value, status)
    #combine the existing and newly generated df
    result_df = pd.concat([df.reset_index(drop=True), new_row.reset_index(drop=True)], axis=0)
    #create excel from new df
    df_to_excel(result_df)
#Check if excel file exists
def check_file_exists():
    check = os.path.exists("Palindrome_Output.xlsx")
    return check

#Read excel and output df
def excel_to_df():
    df = pd.read_excel("Palindrome_Output.xlsx", index_col=[0])
    return df
#Return array of previous values from the excel 
def get_previous_vals(df):
    arr = []
    #loop over df values 
    for i, val in df.iterrows():
        #create dict instance of values 
        new_entry = {
            "Previous Values": val["Previous Values"],
            "Palindrome Status": val["Palindrome Status"]
        }
        #add current dict instance to array 
        arr.append(new_entry)
    return arr
#Check if file exists, if so add to it if not create a one
def check_if_file_exists_and_write(txt_input, res):
    if check_file_exists():
        #add to file
        df = excel_to_df()
        append_df(df, txt_input, res)
    else:
        #Create new df and excel file
        df = to_df(txt_input, res)
        df_to_excel(df)



