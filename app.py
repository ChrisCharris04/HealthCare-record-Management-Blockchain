from flask import Flask, jsonify, request
from flask_cors import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)   # allow Streamlit to call API
blockchain = Blockchain()

@app.route('/records/new', methods=['POST'])
def new_record():
    values = request.get_json()
    required = ['patient_id', 'record_type', 'details']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_record(values['patient_id'], values['record_type'], values['details'])
    response = {'message': f'Record will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    block = blockchain.new_block()
    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'records': block['records'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
