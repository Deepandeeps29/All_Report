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
                    echo "Test stage exit code: ${exitCode}"
                }
            }
        }

        stage('Send Email Report via Python') {
            when {
                expression { fileExists(REPORT_FILE) }
            }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat "python send_email.py"
                }
            }
        }

        // 🆕 Continuous Delivery Stage
        stage('Deploy Report to Shared Folder') {
            when {
                allOf {
                    expression { fileExists(REPORT_FILE) }
                    expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
                }
            }
            steps {
                // Windows shared folder example: update path accordingly
                bat "copy ${REPORT_FILE} \\\\192.168.1.100\\shared_reports\\%BUILD_NUMBER%_report.html"
            }
        }

        stage('Archive Report') {
            when {
                expression { fileExists(REPORT_FILE) }
            }
            steps {
                archiveArtifacts artifacts: REPORT_FILE, fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Email sent, report deployed if successful.'
        }
    }
}
