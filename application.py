from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
@app.route('/')
def home():
    
    return render_template('home.html') 
    
    
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/statspage/')
def statspage():
    filename = 'Road_Fatalities.csv' 
 
	# to read the csv file using the pandas library 
    data = pd.read_csv(filename, header=0) 
 
    myData = data.values 

    return render_template('statspage.html', myData=myData)




if __name__ == '__main__':
    app.run(debug=True)
