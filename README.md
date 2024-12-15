# File Store Service

This is a simple File Store Service built with **Python** and **Flask**, which allows users to store, update, delete, and list plain-text files. It also supports basic operations like word count and frequent word analysis on all stored files.

The project also includes a **Docker** setup to run the service as a container, and a **Kubernetes** deployment configuration for scaling and deploying the service in a cloud-native environment.

## Features

### File Operations
- **Add files**: Upload one or more files to the server. Files are stored on the server, and duplicates are avoided.
- **List files**: Retrieve a list of all files stored on the server.
- **Remove files**: Delete a file from the server.
- **Update files**: Replace the contents of an existing file or create a new one if it doesn't exist.
- **Word Count**: Get the total word count across all stored files.
- **Frequent Words**: Get the most or least frequent words from all stored files.

### Bonus Features
- Avoid resending file content if it's already stored (based on hash comparison).
- Handle network interruptions when sending large files.

## Requirements

- Python 3.x
- Flask
- Docker (optional)
- Kubernetes (optional for Part 2)

### Dependencies (in `requirements.txt`)

- Flask

## Setup and Running the Service

### 1. Clone the repository
Clone this repository to your local machine:
```bash
git clone https://github.com/omdeshmukh24/Filestore.git
2. Install dependencies
Create a virtual environment and install the required Python dependencies:

bash
Copy code
cd filestore
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Running the server locally
To run the Flask server locally:

bash
Copy code
python server.py
The service will be running at http://127.0.0.1:5000.

4. Running the server using Docker
You can also build and run the service in a Docker container. First, build the Docker image:

bash
Copy code
docker build -t filestore-service .
Then, run the container:

bash
Copy code
docker run -p 5000:5000 filestore-service
5. Kubernetes Setup (Optional for Part 2)
You can deploy the service to a Kubernetes cluster (or Minikube, Kind, etc.) by applying the deployment manifest:

bash
Copy code
kubectl apply -f deployment.yaml
API Endpoints
1. POST /files/add
Description: Add one or more files to the server.

Usage:

bash
Copy code
curl -X POST -F "file=@<file_path>" http://127.0.0.1:5000/files/add
2. GET /files/list
Description: List all files stored on the server.

Usage:

bash
Copy code
curl http://127.0.0.1:5000/files/list
3. DELETE /files/remove
Description: Remove a file from the server.

Usage:

bash
Copy code
curl -X DELETE http://127.0.0.1:5000/files/remove?filename=<file_name>
4. PUT /files/update
Description: Update a file or create it if it does not exist.

Usage:

bash
Copy code
curl -X PUT -F "file=@<file_path>" http://127.0.0.1:5000/files/update
5. GET /files/stats
Description: Retrieve word count and frequent word statistics from all stored files.

Usage:

bash
Copy code
curl http://127.0.0.1:5000/files/stats
6. GET /files/freq-words
Description: Get the most frequent words from all files. Supports limit and order options.

Usage:

bash
Copy code
curl http://127.0.0.1:5000/files/freq-words?--limit=10&--order=dsc
