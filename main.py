#jsonify#jsonify creates a json object which is the response
from flask import Flask, request, jsonify

app = Flask(__name__)

#decorator make the datain the route accesinle to the gunction
@app.route("/get-item/<product_id>")
def get_item(product_id):
    inventory_data = {
      'eggs' : 5,
      'bread' : 2,
      'potatoe' : 3,
      'pork' : 10,
      'chicken' : 8,
      'beef' : 20,
      'plantin' : 1,
      'cilantro': 30
        }

extra = request.args.get('extra')
if extra:
  inventory_data['extra'] = extra
  
  return jsonify(inventory_data), 200

@app.route('/create-item', methods=['POST'])
def create_item():
  data = request.get.json()

return jsonify(data), 201

#sets up the Fkask server
if __name__ == '__main__':
    app.run(debug=True)
  
#app.run(host='0.0.0.0', port=8080)

    