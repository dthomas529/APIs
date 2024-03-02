#jsonify creates a json object which is the response
from flask import Flask, request, jsonify
import boto3 #makes it easy to integrate your Python application, library, or script with AWS services including Amazon S3, Amazon EC2, Amazon DynamoDB, and more

app = Flask(__name__) #creates a Flask application object

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your_region_name')

# Specify the table you want to interact with
table_name = 'your_table_name'
table = dynamodb.Table(table_name)

table_name = 'product_inventory'
table = dynamodb.Table(table_name)


 Define the items to be inserted
items_to_insert = [
    {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    },
    {
        'key1': 'value4',
        'key2': 'value5',
        'key3': 'value6'
    },
    {
        'key1': 'value7',
        'key2': 'value8',
        'key3': 'value9'
    }
]

# Insert each item into the table
for item in items_to_insert:
    table.put_item(Item=item)

print("Items inserted successfully.")


# #decorator (@) makes the data in the route accesible to the function
@app.route('/items', methods=['POST'])#POST request is used to send data (file, form data, etc.) to the server. On successful creation, it returns an HTTP status code of 201.
def create_item():
    data = request.get_json()
    response = table.put_item(Item=data)
    return jsonify(response), 201


# Read item
@app.route('/items/<item_id>', methods=['GET'])#GET request is used to read/retrieve data from a web server. GET returns an HTTP status code of 200 (OK) if the data is successfully retrieved from the server.
def get_item(item_id):
    response = table.get_item(Key={'item_id': item_id})
    item = response.get('Item')
    if item:
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404


# Update item
@app.route('/items/<item_id>', methods=['PUT'])#PUT request is used to modify the data on the server. It replaces the entire content at a particular location with data that is passed in the body payload. If there are no resources that match the request, it will generate one.
def update_item(item_id):
    data = request.get_json()
    response = table.update_item(
        Key={'item_id': item_id},
        UpdateExpression='SET attribute1 = :val1',
        ExpressionAttributeValues={':val1': data['attribute1']}
    )
    return jsonify(response), 200


# Delete item
@app.route('/items/<item_id>', methods=['DELETE'])#A DELETE request is used to delete the data on the server at a specified location.
def delete_item(item_id):
    response = table.delete_item(Key={'item_id': item_id})
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)


# Example: Get an item from the table
response = table.get_item(
    Key={
        'key': 'value'
    }
)

item = response.get('Item')
if item:
    print("Item retrieved:", item)
else:
    print("Item not found.")

# Example: Update an item in the table
update_expression = "SET another_key = :new_value"
expression_attribute_values = {
    ':new_value': 'updated_value'
}

table.update_item(
    Key={
        'key': 'value'
    },
    UpdateExpression=update_expression,
    ExpressionAttributeValues=expression_attribute_values
)

# Example: Delete an item from the table
table.delete_item(
    Key={
        'key': 'value'
    }
)

extra = request.args.get('extra')
if extra:
  inventory_data['extra'] = extra
  
  return jsonify(inventory_data), 200

@app.route('/create-item', methods=['POST'])
def create_item():
  data = request.get.json()

return jsonify(data), 201

#sets up the Flask server
if __name__ == '__main__':
    app.run(debug=True)
  
#app.run(host='0.0.0.0', port=8080)
