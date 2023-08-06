from flask import Flask, request, jsonify
from datetime import datetime
from pymongo import MongoClient
import pprint
import gnupg
import tempfile
import os





gpg = gnupg.GPG()
app = Flask(__name__)
mongodb = os.getenv("KALM_DB")
print(mongodb)

client = MongoClient('mongodb://' + mongodb + ':27017/')
db = client['speechmaker']
statements = db['statements']
speeches = db['speeches']
events = db['events']
gpgkeys = db['gpgkeys']



#speeches.delete_many({})
#statements.delete_many({})
#events.delete_many({})
#gpgkeys.delete_many({})

@app.route('/gpgkeys', methods=['GET'])
def get_gpgkeys():
   result = []
   for gpgkey in gpgkeys.find():
     gpgkey['_id'] = str(gpgkey['_id'])
     result.append(gpgkey)
   return jsonify(result)



@app.route('/gpgkeys', methods=['POST'])
def upload_key():
    pp = pprint.PrettyPrinter(indent=4)
    file = request.files['file']
    key_data = file.read()
    with tempfile.NamedTemporaryFile(suffix='.kbx', dir='/tmp', delete=False) as f:
      f.write(key_data)
      key_file_path = f.name
    print('Key file path:', key_file_path)


    pp.pprint(key_data)

    # Import the key into GPG and extract the metadata
    import_result = gpg.import_keys(key_data)
    key = import_result.results[0]
    pp.pprint(key)
    key_metadata = {
              'key_id': key['fingerprint'],
              'key_type': key['type'],
              'key_length': key['length'],
              'creation_date': key['created'],
              'expiration_date': key['expires'],
              'user_ids': key['uids'],
                                                                                        }

   # Store the key and its metadata in MongoDB
    result = gpgkeys.insert_one({
                                 'key_data': key_data,
                                 'key_metadata': key_metadata,
                                  })

    return {'message': 'Key uploaded successfully!', 'key_id': str(result.inserted_id)}




##############################
# speeches
##############################

@app.route('/events', methods=['GET'])
def get_events():
    result = []
    for event in events.find():
        event['_id'] = str(event['_id'])
        result.append(event)
    return jsonify(result)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    token = data['token']
    name = data['name']
    situation = data['situation']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    event = events.find_one({'token': token})
    if event is not None:
        return jsonify({'error': 'Event aleredy exists'}), 404
    else:
        event = {'token': token, 'name': name, 'situation': situation ,  'time': time}
        result = events.insert_one(event)
        event['_id'] = str(result.inserted_id)
        return jsonify(event)

@app.route('/events/<string:event_id>', methods=['PUT'])
def update_event(event_id):
    event = events.find_one({'_id': event_id})
    if event:
        data = request.get_json()
        events.update_one({'_id': event_id}, {'$set': data})
        event.update(data)
        return jsonify(event)
    else:
        return jsonify({'error': 'Event not found'}), 404

@app.route('/events/<string:event_id>', methods=['DELETE'])
def delete_event(event_id):
    result = events.delete_one({'_id': event_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Event deleted'})
    else:
        return jsonify({'error': 'Event not found'}), 404








##############################
# speeches
##############################
@app.route('/speeches', methods=['GET'])
def get_speeches():
    result = []
    for speech in speeches.find():
        speech['_id'] = str(speech['_id'])
        result.append(speech)
    return jsonify(result)

@app.route('/speeches', methods=['POST'])
def create_speech():
    data = request.get_json()
    text = data['text']
    triggeredby = data['triggerstatement']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    speech = {'text': text, 'triggeredby': triggeredby, 'time': time}
    result = speeches.insert_one(speech)
    speech['_id'] = str(result.inserted_id)
    return jsonify(speech)

@app.route('/speeches/<string:speech_id>', methods=['PUT'])
def update_speech(speech_id):
    speech = speeches.find_one({'_id': speech_id})
    if speech:
        data = request.get_json()
        speeches.update_one({'_id': speech_id}, {'$set': data})
        speech.update(data)
        return jsonify(speech)
    else:
        return jsonify({'error': 'Speech not found'}), 404

@app.route('/speeches/<string:speech_id>', methods=['DELETE'])
def delete_speech(speech_id):
    result = speeches.delete_one({'_id': speech_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Speech deleted'})
    else:
        return jsonify({'error': 'Speech not found'}), 404






##################################
# Statements
######################################

@app.route('/statements', methods=['GET'])
def get_statements():
    result = []
    for statement in statements.find():
        statement['_id'] = str(statement['_id'])
        result.append(statement)
    return jsonify(result)

@app.route('/statements', methods=['POST'])
def create_statement():
    data = request.get_json()
    text = data['text']
    used = False
    sender = data['sender']
    target = data['target']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    statement = {'text': text, 'sender': sender, 'target': target, 'time': time, 'used': used }
    result = statements.insert_one(statement)
    statement['_id'] = str(result.inserted_id)
    return jsonify(statement)

@app.route('/statements/<string:statement_id>', methods=['PUT'])
def update_statement(statement_id):
    statement = statements.find_one({'_id': statement_id})
    if statement:
        data = request.get_json()
        statements.update_one({'_id': statement_id}, {'$set': data})
        statement.update(data)
        return jsonify(statement)
    else:
        return jsonify({'error': 'Statement not found'}), 404

@app.route('/statements/<string:statement_id>', methods=['DELETE'])
def delete_statement(statement_id):
    result = statements.delete_one({'_id': statement_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Statement deleted'})
    else:
        return jsonify({'error': 'Statement not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


