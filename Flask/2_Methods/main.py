from json import loads, dumps
from flask import Flask, request, jsonify, send_file
import pandas as pd

# get some data
df = pd.read_csv('././Data/Wing_Financial_Bulk_Update.csv')

# Flask stuff
app = Flask(__name__)

@app.route('/', methods=['GET'])
def default():

    return send_file('../../Data/harold.jpg', mimetype='image/gif')

@app.route('/get_no_args', methods=['GET'])
def get_no_args():

    parsed_df = loads(df.to_json(orient='records'))

    return jsonify(parsed_df)

@app.route('/get_index', methods=['GET'])
def get_index():

    args = request.args

    ix = int(args.get('index'))

    parsed_df = loads(df.iloc[[ix]].to_json(orient='records'))

    return jsonify(parsed_df)

@app.route('/update_index', methods=['POST'])
def update_index():

    args = loads(request.data)

    ix = int(args['index'])

    col = args['column']

    new_value = args['update']

    df.at[ix, col] = new_value
    
    parsed_df = loads(df.iloc[[ix]].to_json(orient='records')) 

    return jsonify(parsed_df)

@app.route('/add_row', methods=['PUT'])
def add_row():

    args = loads(request.data)

    id = int(args['id'])

    address = args['address']

    service_remark = args['service_remark']

    df.loc[len(df.index)] = [id, address, service_remark]
    
    parsed_df = loads(df.iloc[[len(df.index) - 1]].to_json(orient='records')) 

    return jsonify(parsed_df)

@app.route('/delete_row', methods=['DELETE'])
def delete_row():

    args = request.args 

    ix = int(args.get('index'))

    df.drop([ix], axis='index')

    return jsonify({'status': 'deleted', 'index': ix})



app.run()