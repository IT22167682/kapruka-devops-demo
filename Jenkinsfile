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
        sh 'git log -1 --pretty=format:"%h - %an, %ar : %s"'
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
    stage('Deploy') {
      steps {
        sh '''
          docker stop kapruka-app || true
          docker rm kapruka-app || true
          docker run -d --name kapruka-app --restart unless-stopped \
            -p ${APP_PORT}:${APP_PORT} ${DOCKER_IMAGE}:latest
          sleep 5
        '''
      }
    }
    stage('Verify') {
      steps { sh 'curl -f http://localhost:${APP_PORT}/health' }
    }
  }
  post {
    success { echo "✅ Build #${BUILD_NUMBER} OK — http://localhost:${APP_PORT}" }
    failure { echo "❌ Build failed — check console log." }
    always  {
      sh 'docker ps'
      sh 'docker image prune -f || true'
    }
  }
    stage('Ansible Deploy') {
      steps {
        sh '''
          echo "=== Running Ansible playbook for deployment ==="
          ansible-playbook ~/ansible/deploy.yml
        '''
      }
    }
}
