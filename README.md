# CloudFormation CI/CD monorepo

Requirements:
1. Deploy CloudFormation stack to an account through automation pipeline
    - The template will be checked with liniting and security check


Packages:
1. boto3 - AWS SDK API
2. cfn-lint - AWS linting tool with more verbose and rich functionality
3. cfn_nag_scan - AWS security check tool 


Roadmap:
- [ ]  Write azure pipeline yaml file to run job
    - [x] Install python and ruby runtime 
    - [x] Install cfn-lint and cfn_nag_scan
    - [x] Install python dependencies on the requirements.txt 
    - [x] Run cfn-lint and cfn_nag_scan 
    - [x] Run python script 
    - [x] Run deployment only on master/main branch 
    - [ ] Create change set during a pull request 
- [ ] Write python script 
    - [x] Able to parse manifest yaml file
    - [ ] Able to able to detect changes by describing_stack and compare with original stack
    - [ ] Able to print events during deployment 
    - [ ] Retrieve deployment status