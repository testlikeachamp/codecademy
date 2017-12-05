pipeline {
    agent {
        docker {
            image 'python:3.6'
            args '-u root:sudo'}
    }
    stages {
        stage('build') {
            steps {
                sh 'whoami &&\
                    python --version &&\
                    pip install -r requirements.txt &&\
                    pytest tests'
            }
        }
    }
    post {
        always {
            archive '**/report.html'
            archive '**/report.xml'
            junit '**/report.xml'
        }
    }
}


