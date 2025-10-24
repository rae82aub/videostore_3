pipeline {
  agent any

  triggers {
    pollSCM('H/2 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'YOUR_GITHUB_URL'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        sh '''
        # === Switch Docker to Minikube Docker ===
        eval $(minikube docker-env)

        # === Build Django image inside Minikube Docker ===
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh '''
        # === Apply the updated deployment manifest ===
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml

        # === Wait for rollout to finish ===
        kubectl rollout status deployment/django-deployment
        '''
      }
    }
  }
}
