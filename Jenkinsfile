pipeline {
    agent { docker 'python:3.6' }
    stages {
        stage('build') {
            steps {
                sh 'whoami &&\
                    sudo su &&\
                    python --version &&\
                    pip install -r requirements.txt &&\
                    py.test -lsvvv --cov=codecademy --cov-branch tests'
            }
        }
    }
}
