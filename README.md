# AWS Elastic Beanstalk Deployment Guide

## Overview
This repository contains a step-by-step guide to deploying a web application on **AWS Elastic Beanstalk (EBS)** using the **AWS CLI and Elastic Beanstalk CLI**.

AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) that allows developers to deploy and manage applications in the cloud without worrying about the infrastructure.

## Prerequisites
Before deploying, ensure you have the following:

- An **AWS account** ([Sign up here](https://aws.amazon.com/))
- **AWS CLI** installed ([Installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))
- **Elastic Beanstalk CLI (EB CLI)** installed ([Installation guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html))
- **Git** installed ([Download here](https://git-scm.com/downloads))
- **Python 3** (if deploying a Python app) or the relevant runtime for your application

## Setting Up AWS Elastic Beanstalk

### 1. Configure AWS Credentials
First, configure your AWS CLI with your access and secret keys:
```bash
aws configure
```
You'll be prompted to enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default AWS Region (e.g., `us-west-2`)
- Default output format (leave blank for `json`)

### 2. Initialize Elastic Beanstalk
Navigate to your project directory and run:
```bash
eb init
```
- Choose the AWS region.
- Select a platform (e.g., Python, Node.js, etc.).
- Choose an application name.
- Select a keypair for SSH access (optional).

### 3. Create an Elastic Beanstalk Environment
To create an environment, run:
```bash
eb create my-aws-env
```
- Replace `my-aws-env` with your environment name.
- Elastic Beanstalk will provision resources like EC2 instances, Load Balancers, and Auto Scaling Groups.

## Deploying the Application
To deploy your application, run:
```bash
eb deploy
```
This uploads the application bundle to AWS and deploys it to your environment.

## Viewing the Application
Once deployed, get the application URL with:
```bash
eb open
```

## Checking Logs
If you encounter issues, view logs with:
```bash
eb logs
```
You can filter errors using:
```bash
eb logs | grep ERROR
```

## Updating the Application
After making changes to your application, commit the changes and deploy:
```bash
git add .
git commit -m "Updated application"
eb deploy
```

## Troubleshooting
If deployment fails, check logs as mentioned above. If issues persist, consider restarting or terminating the environment:
```bash
eb restart
```
To delete and recreate the environment:
```bash
eb terminate my-aws-env
eb create my-aws-env
```

## Managing Environment Variables
To set environment variables, use:
```bash
eb setenv VAR_NAME=value
```
To list environment variables:
```bash
eb printenv
```

## Deleting an Environment
To delete an environment and all its resources:
```bash
eb terminate my-aws-env
```

## Pushing to GitHub
1. Initialize a Git repository (if not already done):
```bash
git init
```
2. Add files and commit:
```bash
git add .
git commit -m "Initial commit"
```
3. Create a GitHub repository and push the code:
```bash
git remote add origin https://github.com/your-username/aws-ebs-deployment.git
git push -u origin main
```

## Conclusion
You've successfully deployed your application on AWS Elastic Beanstalk! íº€ If you have any issues, refer to the [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html).

