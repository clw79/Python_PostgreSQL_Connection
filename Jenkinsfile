pipeline {
    agent any

    environment {
        POSTGRES_HOST = '192.168.0.170'
        POSTGRES_PORT = '5432'
        POSTGRES_DB = 'homelab'
        POSTGRES_USER = 'chris'
        POSTGRES_PASSWORD = credentials('postgres-password')
    }

    stages {
        stage('Check Python') {
            steps {
                sh '''
                    echo "Checking Python version..."
                    python3 --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                    echo "Creating virtual environment..."
                    python3 -m venv .venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Activating virtual environment..."
                    . .venv/bin/activate

                    echo "Checking pip version..."
                    python -m pip --version

                    echo "Upgrading pip..."
                    python -m pip install --upgrade pip

                    echo "Installing Python dependencies..."
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browser') {
            steps {
                sh '''
                    echo "Activating virtual environment..."
                    . .venv/bin/activate

                    echo "Installing Playwright Chromium browser..."
                    python -m playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Activating virtual environment..."
                    . .venv/bin/activate

                    echo "Running pytest..."
                    python -m pytest
                '''
            }
        }
    }
}