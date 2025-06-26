pipeline {
    agent any

    environment {
        REPORT_FILE = 'report.html'
<<<<<<< HEAD
=======
        DEPLOY_USER = 'welcome'
        DEPLOY_HOST = '192.168.68.115'
        DEPLOY_PATH = '/var/www/html/'
>>>>>>> 760bb2294a0a4cc4e1d1e259b44ef3c2d508c959
    }
    stages {
        stage('Checkout') {
            steps {
<<<<<<< HEAD
                git branch: 'main', url: 'https://github.com/Deepandeeps29/All_Report.git'
=======
                git credentialsId: 'f695a64c-2dde-4f15-9c36-a0c6dfe600ad',
                    url: 'https://github.com/Deepandeeps29/All_Report.git',
                    branch: 'main'
>>>>>>> 760bb2294a0a4cc4e1d1e259b44ef3c2d508c959
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
<<<<<<< HEAD
                bat 'python send_email.py'
=======
                bat '"D:\\Program\\Git\\usr\\bin\\scp.exe" -o StrictHostKeyChecking=no report.html welcome@192.168.68.115:/var/www/html/'
>>>>>>> 760bb2294a0a4cc4e1d1e259b44ef3c2d508c959
            }
        }
    }
    post {
        always {
            echo 'Jenkins Build Done. Email Sent if Report was found.'
        }
    }
}