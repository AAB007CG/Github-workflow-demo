## Steps for this Branch

1. Created a new feature branch `feature/Agent-202-Sonarcloud`
2. I added the `sonarcloud-demo.yml` which contains the workflow code and `sonar-project.properties` file which contains the credentials. The credentials to be obtained from the Sonarcloud organisation dashboard.
3. In the SonarCloud website we need to create an organisation first by linking our Github account to it and giving access to the specific repositories we want to work on. Once the organization is set we can then Analyze a new project by selecting the Github repo which needs to be analysed.
4. We need to set the Sonar Token in the Github Repository Secrets which is under the security section of the Repo settings.