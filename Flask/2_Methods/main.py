from json import loads, dumps
from flask import Flask, request, jsonify
import pandas as pd

# get some data
df = pd.read_csv('././Data/Wing_Financial_Bulk_Update.csv')

# Flask stuff
app = Flask(__name__)

@app.route('/get_no_args', methods=['GET'])
def get_no_args():

    parsed_df = loads(df.to_json(orient='index'))

    return dumps(parsed_df, indent=4)

@app.route('/get_index', methods=['GET'])
def get_index():

    args = request.args

    ix = int(args.get('index'))

    parsed_df = loads(df.iloc[[ix]].to_json(orient='index'))

    return dumps(parsed_df, indent=4)

@app.route('/update_index', methods=['POST'])
def update_index():

    args = request.args

    ix = int(args.get('index'))

    col = args.get('column')

    new_value = args.get('new')


app.run()