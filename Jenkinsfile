pipeline {
      agent {dockerfile true}
    stages {
        stage('Prepare') {
            steps {
                echo 'gkl in stage - Prepare'
                sh 'pipenv install --dev'
            }
        }
        stage('Test') {
            steps {
                echo 'gkl in stage - Test'
                sh 'pipenv run pytest --html=Sample_report.html'
            }
        }
        stage('Build') {
            steps {
                echo 'gkl in stage - Build'
            }
        }
    }
      post {
            always {
                  echo 'gkl before publishing html'
                  publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: '', reportFiles: 'Sample_report.html', reportName: 'HTML Report', reportTitles: 'Gokuls Test report', useWrapperFileDirectly: true])
                  echo 'gkl after publishing html'
            }
      }
}
