pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    echo "hello world"

                    def a = 10
                    def b = 20
                    def c = a + b

                    echo "Result is: ${c}"
                }
            }
        }
    }
}
