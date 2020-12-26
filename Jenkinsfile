pipeline {
    agent any
    options {
            buildDiscarder(
                            logRotator(numToKeepStr: '10')
            )
    }
    stages {
        stage('Hello') {
        options{
                timeout(time: 10, unit: 'SECONDS')
        }
            steps {
                echo '卧槽！！'
                script{
                        def browsers = ['谷歌', '火狐']
                        for(int i = 0; i < browsers.size(); i++) {
                                echo "Testing the ${browsers[i]} browser"
                        }
                }
            }
        }
    }
}