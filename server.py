from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def store_file(filename, content):
  """Stores a file with the given filename and content."""
  try:
    with open(filename, 'w') as f:
      f.write(content)
  except Exception as e:
    return False, str(e)
  return True, "File stored successfully"

@app.route('/store', methods=['POST'])
def store():
  """Stores a file uploaded from the client."""
  try:
    filename = request.form['filename']
    content = request.form['content']
    success, message = store_file(filename, content)
    if success:
      return jsonify({'message': message})
    else:
      return jsonify({'error': message}), 500
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@app.route('/list', methods=['GET'])
def list_files():
  """Lists all files in the current directory."""
  try:
    files = os.listdir('.')
    return jsonify({'files': files})
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@app.route('/remove/<filename>', methods=['DELETE'])
def remove_file(filename):
  """Removes a file with the given filename."""
  try:
    os.remove(filename)
    return jsonify({'message': 'File removed successfully'})
  except FileNotFoundError:
    return jsonify({'error': 'File not found'}), 404
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@app.route('/update/<filename>', methods=['PUT'])
def update_file(filename):
  """Updates the contents of a file with the given filename."""
  try:
    content = request.form['content']
    success, message = store_file(filename, content)
    if success:
      return jsonify({'message': message})
    else:
      return jsonify({'error': message}), 500
  except Exception as e:
    return jsonify({'error': str(e)}), 500

# Add additional routes for word count, frequency analysis, etc. (optional)

if __name__ == '_main_':
  app.run(host='0.0.0.0',port=5000,debug=True)
