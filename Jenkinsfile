pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
    }

    stages {

        stage('Checkout') {
            steps {
                git credentialsId: 'github-token',
                    url: 'https://github.com/Deepandeeps29/Automation_Pratice_Site.git',
                    branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat "pytest tests/test_login.py --html=${REPORT_FILE} --self-contained-html"
            }
        }

        stage('Send Email Report via Python') {
            steps {
                // Check if the report file exists before sending
                bat 'if exist report.html python send_email.py'
            }
        }

        stage('Archive Report (Optional UI Access)') {
            steps {
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: true
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report'
                ])
            }
        }

        stage('Send Email') {
            steps {
                emailext (
                    subject: "🧪 Test Report - Jenkins Build #${BUILD_NUMBER}",
                    body: "Hello Team,<br><br>Please find the attached <b>HTML Test Report</b> for Jenkins Build #${BUILD_NUMBER}.<br><br>Regards,<br>Jenkins",
                    to: 'deepanvinayagam2912@gmail.com',
                    from: 'deepanvinayagam2912@gmail.com',
                    attachLog: false,
                    attachmentsPattern: 'report.html'
                )
            }
        }
    }

    post {
        always {
            echo "📨 Pipeline finished. Email report was sent using Python script if available."
        }
    }
}
