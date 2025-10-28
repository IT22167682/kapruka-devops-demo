pipeline {
  agent any

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }

  environment {
    DOCKER_IMAGE = 'kapruka-ecommerce'
    APP_PORT     = '3000'
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
        sh 'git log -1 --pretty=format:"%h - %an, %ar : %s" || true'
      }
    }

    stage('Unit Test (syntax)') {
      steps { sh 'python3 -m py_compile app.py' }
    }

    stage('Build Image') {
      steps {
        sh '''
          docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
          docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
        '''
      }
    }

    stage('Deploy Docker (local)') {
      steps {
        sh '''
          docker stop kapruka-app || true
          docker rm   kapruka-app || true
          docker run -d --name kapruka-app --restart unless-stopped \
            -p ${APP_PORT}:${APP_PORT} ${DOCKER_IMAGE}:latest
          sleep 5
        '''
      }
    }

    stage('Verify (local health)') {
      steps { sh 'curl -f http://localhost:${APP_PORT}/health' }
    }

    stage('Ansible Deploy') {
      steps {
        sh '''
          echo "=== Running Ansible playbook (Jenkins user) ==="
          export ANSIBLE_HOST_KEY_CHECKING=False
          ansible-playbook -i /var/lib/jenkins/ansible/hosts /var/lib/jenkins/ansible/deploy.yml
        '''
      }
    }
  }

  post {
    always  { sh 'docker ps || true' }
    success { echo "✅ Build #${BUILD_NUMBER} completed" }
    failure { echo "❌ Build failed — check Console Output" }
  }
}

