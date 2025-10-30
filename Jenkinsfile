pipeline {
  agent any

  triggers {
    pollSCM('H/2 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/rae82aub/videostore_3.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        sh '''
        echo "🐳 Setting up Minikube Docker environment..."
        eval $(minikube docker-env)
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
        echo "🚀 Applying Kubernetes manifests..."
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml

        echo "⏳ Waiting for rollout to complete..."
        kubectl rollout status deployment/django-deployment
        '''
      }
    }

    stage('Get Service URL') {
      steps {
        sh '''
        echo "🌍 Retrieving Django service URL (Mac-friendly)..."
        minikube service list | grep django-service || echo "Service not found."
        '''
      }
    }
  }
}
