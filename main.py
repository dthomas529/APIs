from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name:': 'John Doe',
        'email': 'jdoe@example.com'
        }
#def home():
     #return 'Home'

if app == '__main__':
    app.run(debug=True)
    

