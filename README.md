# CloudFormation CI/CD monorepo

Requirements:
1. Deploy CloudFormation template to an account as CloudFormation stack 
2. Able to run linting and security check for every template in the repo 
3. Able to show the log in pipeline 
5. Create change set during a pull request 
6. Detect changes in template or somewhere

Packages:
1. boto3 - AWS SDK API
2. cfn-lint - AWS linting tool with more verbose and rich functionality
3. cfn_nag_scan - AWS security check tool 

Roadmap:
- [ ]  Write azure pipeline yaml file to run job
    - [ ] Install python and ruby runtime 
    - [ ] Install cfn-lint and cfn_nag_scan
    - [ ] Install python dependencies on the requirements.txt 
    - [ ] Run cfn-lint and cfn_nag_scan 
    - [ ] Run python script 
    - [ ] Run deployment only on master/main branch 
    - [ ] Create change set during a pull request 
- [ ] Write python script 
    - [ ] Able to parse manifest yaml file
    - [ ] Able to able to detect changes by describing_stack and compare with original stack
    - [ ] Able to print events during deployment 
    - [ ] Retrieve deployment status