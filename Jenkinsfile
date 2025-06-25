pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
        DEPLOY_USER = 'deepan'                 // replace with your server's username
        DEPLOY_HOST = '192.168.68.115'                 // replace with your server's IP
        DEPLOY_PATH = '/var/www/html/'               // path where report.html should be deployed
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
                bat "pytest tests/test_login.py --html=${REPORT_FILE} --self-contained-html"
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
                script {
                    // Unix shell
                    sh "scp -o StrictHostKeyChecking=no ${REPORT_FILE} ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Report generated, emailed, and deployed."
        }
    }
}
