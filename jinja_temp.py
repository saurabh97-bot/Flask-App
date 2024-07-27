from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Test User"
    return render_template('index.html',test_name=name)


@app.route('/list')
def list_data():
    list_elements = ['AAAP','TESL','MSE','TSO','TESL',"TTR",1,0.02,45.39,2,3,4,5,"Hello","World"]
    return render_template('list.html',ticker=list_elements)

@app.route('/users')
def user_list():
    users = [
        {'name':'Pratik Sir','age':24,'Trainer':'DSA'},
        {'name':'Nikhil Sir','age':28,'Trainer':'React'},
        {'name':'Sudhir Sir','age':32,'Trainer':'Java/Python'},
        {'name':'Saurbh Sir','age':24,'Trainer':'Full Stack'}
    ]

    return render_template('users.html',test_users=users)

@app.route('/dict')
def user_dict():
    users = {
        1: {'name':'Pratik Sir','age':24,'Trainer':'DSA'},
        2: {'name':'Nikhil Sir','age':28,'Trainer':'React'},
        3: {'name':'Sudhir Sir','age':32,'Trainer':'Java/Python'},
        4: {'name':'Saurabh Sir','age':24,'Trainer':'Full Stack'}
    }
    return render_template('dict.html',dict_users=users)

@app.route('/combined')
def combined_func():
     name = "Test User"
     list_elements = ['AAAP','TESL','MSE','MICRO','TCS']
     users = [
        {'name':'Pratik Sir','age':24,'Trainer':'DSA'},
        {'name':'Nikhil Sir','age':28,'Trainer':'React'},
        {'name':'Sudhir Sir','age':32,'Trainer':'Java/Python'},
        {'name':'Saurbh Sir','age':24,'Trainer':'Full Stack'}
    ]
     dict_users = {
        1: {'name':'Pratik Sir','age':24,'Trainer':'DSA'},
        2: {'name':'Nikhil Sir','age':28,'Trainer':'React'},
        3: {'name':'Sudhir Sir','age':32,'Trainer':'Java/Python'},
        4: {'name':'Saurabh Sir','age':24,'Trainer':'Full Stack'}
    }
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005)