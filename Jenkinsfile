pipeline {
      agent {dockerfile true}
    stages {
        stage('Prepare') {
            steps {
                echo 'This is the Prepare stage - Prepare'
                sh 'pipenv install --dev'
            }
        }
        stage('Test') {
            steps {
                echo 'This is the test stage - Test'
                sh 'pipenv run pytest -v --html=Sample_report.html'
            }
        }
        stage('Build') {
            steps {
                echo 'This is the build stage - Build'
            }
        }
    }
      post {
            always {
                  publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: '', reportFiles: 'Sample_report.html', reportName: 'HTML Report', reportTitles: 'Test report', useWrapperFileDirectly: true])
            }
      }
}
