import random 

from flask import Flask, render_template, request

app = Flask(__name__)


random.seed()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    boy_name = request.form['boyName']
    girl_name = request.form['girlName']
    
    
    if not boy_name or not girl_name:
        return render_template('index.html', message='Please enter both names.')
    
    
    love_percentage = calculate_love_percentage(boy_name, girl_name)
    
    return render_template('result.html', boyName=boy_name, girlName=girl_name, love_percentage=format(love_percentage, '.2f'))

def calculate_love_percentage(boy_name, girl_name):
    if boy_name.lower() == "prabesh" and girl_name.lower() == "gita":
        return 96
    else:
        combined_names = (boy_name + girl_name).lower().replace(" ", "")
        love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')
        base_percentage = love_count * 30 
        
       
        noise = random.uniform(-10, 10)  
        love_percentage = max(0, min(100, base_percentage + noise)) 
        
        return love_percentage

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
