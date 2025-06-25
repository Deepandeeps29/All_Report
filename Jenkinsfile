pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
        DEPLOY_USER = 'deepan'
        DEPLOY_HOST = '192.168.68.115'
        DEPLOY_PATH = '/var/www/html/'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token',
                    url: 'https://github.com/Deepandeeps29/Sample.git',
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
                bat "pytest Runnerclass/test_demo_page.py --html=%REPORT_FILE% --self-contained-html"
            }
        }

        stage('Archive and Email Report') {
            steps {
                script {
                    archiveArtifacts artifacts: "${REPORT_FILE}", onlyIfSuccessful: true
                    emailext(
                        subject: "🧪 Selenium Test Report - Build #${BUILD_NUMBER}",
                        body: """
                            <p>Hello Team,</p>
                            <p>Please find the attached <b>HTML Test Report</b> for Jenkins Build #${BUILD_NUMBER}.</p>
                            <p>Regards,<br>Jenkins</p>
                        """,
                        to: 'deepanvinayagam1411@gmail.com',
                        from: 'deepanvinayagam1411@gmail.com',
                        attachLog: false,
                        attachmentsPattern: "${REPORT_FILE}"
                    )
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                bat '"D:\\Program\\Git\\usr\\bin\\scp.exe" -o StrictHostKeyChecking=no report.html deepan@192.168.68.115:/var/www/html/'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Report generated, emailed, and deployed."
        }
    }
}
