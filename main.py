#jsonify creates a json object which is the response
from flask import Flask, request, jsonify

app = Flask(__name__)

#decorator make the datain the route accesinle to the gunction
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name:': 'John Doe',
        'email': 'jdoe@example.com'
        }

extra = request.args.get('extra')
if extra:
  user_data['extra'] = extra
  
  return jsonify(user_data), 200

@app.route('/create-user', methods=['POST'])
def create_user():
  data = request.get.json()

return jsonify(data), 201

#sets up the Fkask server
if __name__ == '__main__':
    app.run(debug=True)
  
#app.run(host='0.0.0.0', port=8080)

    