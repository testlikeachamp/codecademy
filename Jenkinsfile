pipeline {
    agent {
        docker {
            image 'python:3.6.3-alpine3.6'
            args '-u root:root'}
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
            archiveArtifacts '**/report.html'
            archiveArtifacts '**/report.xml'
            junit '**/report.xml'
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'HTML Report'
            ]
        }
    }
}
