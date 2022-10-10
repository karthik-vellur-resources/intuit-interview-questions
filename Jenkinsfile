def podLabel = "a4a-docs-${UUID.randomUUID().toString()}"

podTemplate(name: podLabel, label: podLabel, containers: [
    containerTemplate(name: 'mkdocs', image: 'docker.intuit.com/oicp/standard/base/amzn', alwaysPullImage: true, ttyEnabled: true, command: 'cat')
])

{
    node(podLabel) {
        def branch = env.CHANGE_ID != null ? env.CHANGE_TARGET : env.BRANCH_NAME
        def isPR = env.CHANGE_ID != null

        stage('Build') {
            checkout scm
            container('mkdocs') {
                sh """
                curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
                && sudo yum install -y python3.7 git \
                && sudo python3.7 get-pip.py --no-warn-script-location

                pip install -r requirements.txt
                
                export PATH="/home/appuser/.local/bin:$PATH"
                
                mkdocs --version
                
                git --version
                
                export LC_ALL=en_US.utf8 && export LANG=en_US.utf8
                
                mkdocs build --clean
                """
            }
        }

        if ((branch == 'master') && !isPR) {
            stage('Deploy') {
                container('mkdocs') {
                    withCredentials([usernamePassword(credentialsId: 'mlservice', usernameVariable: 'USERNAME', passwordVariable: 'GH_TOKEN')]) {
                        sh """
                        export PATH="/home/appuser/.local/bin:$PATH" && mkdocs --version
                        git config --global user.email $USERNAME
                        git clone https://${GH_TOKEN}@github.intuit.com/poolhiring/interview-questions.git ./a4a-docs-deploy
                        cd ./a4a-docs-deploy && export LC_ALL=en_US.utf8 && export LANG=en_US.utf8
                        mkdocs gh-deploy -f ${WORKSPACE}/mkdocs.yml
                        """
                    }
                }
            }
        }
    }
}
