#!/bin/bash

# Variables
APP_NAME="apquiz-app"
DOCKER_IMAGE="your_dockerhub_username/$APP_NAME:latest"
EC2_INSTANCE="your_ec2_instance_ip"
EC2_USER="ec2-user"  # Change if using a different user
KEY_FILE="path_to_your_key.pem"  # Path to your EC2 key pair

# Build the Docker image
docker build -t $DOCKER_IMAGE .

# Push the Docker image to Docker Hub
docker push $DOCKER_IMAGE

# SSH into the EC2 instance and deploy the Docker container
ssh -i $KEY_FILE $EC2_USER@$EC2_INSTANCE << 'EOF'
    # Pull the latest Docker image
    docker pull your_dockerhub_username/apquiz-app:latest

    # Stop and remove the existing container if it exists
    if [ "$(docker ps -q -f name=apquiz-app)" ]; then
        docker stop apquiz-app
        docker rm apquiz-app
    fi

    # Run the new container
    docker run -d -p 80:5000 --name apquiz-app your_dockerhub_username/apquiz-app:latest
EOF

echo "Deployment to EC2 completed successfully!"