pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Deepandeeps29/All_Report.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def exitCode = bat(script: "pytest Runnerclass/test_demo_page.py --html=${REPORT_FILE} --self-contained-html", returnStatus: true)
                    echo "Exit Code: ${exitCode}"
                }
            }
        }
        stage('Send Email Report') {
            when {
                expression { fileExists('report.html') }
            }
            steps {
                bat 'python send_email.py'
            }
        }
    }
    post {
        always {
            echo 'Jenkins Build Done. Email Sent if Report was found.'
        }
    }
}