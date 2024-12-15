File Store Service
Overview
The File Store Service is a simple HTTP-based file management system built using Flask. It supports operations like adding, updating, removing, listing files, counting words, and listing the most frequent words across all files stored on the server.

Additionally, Part 2 involves deploying the service on a Kubernetes/OpenShift cluster using Minikube or kind for local clusters.

Part 1: The File Store Service
Features
Add files: Upload files to the server with store add file1.txt file2.txt.
List files: View the list of files stored in the server using store ls.
Remove files: Delete files from the server with store rm file.txt.
Update files: Replace the content of an existing file with store update file.txt.
Word Count: Get the total word count of all files stored in the server using store wc.
Frequent Words: List the most frequent words across all stored files, sorted by frequency with store freq-words.
Requirements
To run this service, you need:

Python 3.x installed
Flask for the web server
Docker (optional, for containerization)
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/omdeshmukh24/Filestore.git
cd Filestore
Set up a virtual environment (optional, recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run the server:

bash
Copy code
python server.py
This will start the server and listen on port 5000. You can access it at http://127.0.0.1:5000.

API Endpoints
Add Files

POST /files/add
Upload a file to the server.
Request:
bash
Copy code
curl -X POST -F "file=@file1.txt" http://127.0.0.1:5000/files/add
Response:
json
Copy code
{"message": "File added successfully"}
List Files

GET /files/list
List all files stored on the server.
Request:
bash
Copy code
curl http://127.0.0.1:5000/files/list
Response:
json
Copy code
{"files": ["file1.txt", "file2.txt"]}
Remove File

DELETE /files/remove
Remove a file from the server.
Request:
bash
Copy code
curl -X DELETE -d "file=file1.txt" http://127.0.0.1:5000/files/remove
Response:
json
Copy code
{"message": "File removed successfully"}
Update File

PUT /files/update
Update the content of an existing file or add it if it doesn’t exist.
Request:
bash
Copy code
curl -X PUT -F "file=@file1.txt" http://127.0.0.1:5000/files/update
Response:
json
Copy code
{"message": "File updated successfully"}
Word Count

GET /files/stats
Get the total word count of all files stored.
Request:
bash
Copy code
curl http://127.0.0.1:5000/files/stats
Response:
json
Copy code
{"total_words": 150}
Frequent Words

GET /files/freq-words
Get the most frequent words across all files.
Request:
bash
Copy code
curl http://127.0.0.1:5000/files/freq-words
Response:
json
Copy code
{"words": [{"word": "the", "count": 15}, {"word": "is", "count": 12}]}
Part 2: Kubernetes/OpenShift Deployment
Overview
In this part, the goal is to deploy the File Store Service on a Kubernetes or OpenShift cluster. The solution uses Minikube or kind for local clusters, and Kubernetes manifests to deploy the application.

Requirements for Deployment
Minikube or kind for creating a local Kubernetes cluster.
kubectl to interact with the cluster.
Docker to build container images.
Steps for Kubernetes Deployment
Set up Kubernetes Cluster with Minikube

Install Minikube: Follow the instructions on Minikube documentation.
Start Minikube:
bash
Copy code
minikube start
Build Docker Image

Build the Docker image for the file store service:
bash
Copy code
docker build -t filestore-service .
Create Kubernetes Manifests

Create the deployment.yaml and service.yaml to deploy the service.
Example deployment.yaml:

yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: filestore-service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: filestore-service
  template:
    metadata:
      labels:
        app: filestore-service
    spec:
      containers:
        - name: filestore-service
          image: filestore-service
          ports:
            - containerPort: 5000
Example service.yaml:

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: filestore-service
spec:
  selector:
    app: filestore-service
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
  type: LoadBalancer
Deploy to Kubernetes

Apply the manifests to deploy the service to the Kubernetes cluster:
bash
Copy code
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
Access the Application

Use kubectl to find the external IP or use port-forwarding to access the service:
bash
Copy code
kubectl port-forward svc/filestore-service 5000:5000
Dockerization (Optional)
You can also run the service as a Docker container using the following steps:

Build the Docker image:

bash
Copy code
docker build -t filestore-service .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 filestore-service
The service will be available at http://localhost:5000.

