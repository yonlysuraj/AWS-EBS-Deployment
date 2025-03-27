# AWS Elastic Beanstalk Deployment Guide

## Overview
This repository contains a step-by-step guide to deploying a **Flask web application** on **AWS Elastic Beanstalk (EBS)** using the **AWS CLI and Elastic Beanstalk CLI**.

AWS Elastic Beanstalk is a Platform-as-a-Service (PaaS) that allows developers to deploy and manage applications in the cloud without worrying about the infrastructure.

## Prerequisites
Before deploying, ensure you have the following:

- An **AWS account** ([Sign up here](https://aws.amazon.com/))
- **AWS CLI** installed ([Installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))
- **Elastic Beanstalk CLI (EB CLI)** installed ([Installation guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html))
- **Python 3** installed
- **Flask and dependencies installed** in a virtual environment
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  pip install -r requirements.txt
  ```

## Setting Up AWS Elastic Beanstalk

### 1. Configure AWS Credentials
First, configure your AWS CLI with your access and secret keys:
```bash
aws configure
```
You'll be prompted to enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default AWS Region (e.g., `ap-south-1`)
- Default output format (leave blank for `json`)

### 2. Initialize Elastic Beanstalk
Navigate to your project directory and run:
```bash
eb init
```
- Choose the AWS region.
- Select **Python** as the platform.
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

## Testing the Application
### 1. Manually Test with cURL
Run the following command to test your Flask app's response:
```bash
curl http://my-aws-env.eba-xxxxxx.ap-south-1.elasticbeanstalk.com/
```
Replace the URL with your actual environment URL.

### 2. Load Testing with ApacheBench (ab)
To check performance and auto-scaling, run:
```bash
ab -n 20000 -c 500 http://my-aws-env.eba-xxxxxx.ap-south-1.elasticbeanstalk.com/
```
This will send **20,000 requests** with **500 concurrent connections**.

### 3. Monitor Metrics in CloudWatch
To check NetworkOut statistics, use:
```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name NetworkOut \
  --dimensions Name=AutoScalingGroupName,Value=your-autoscaling-group-name \
  --statistics Average \
  --start-time "$(date -u -d '-10 minutes' +%Y-%m-%dT%H:%M:%SZ)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --period 300 \
  --region ap-south-1
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

## Auto Scaling Configuration
### 1. Scaling Policy
- **Scale Up:** If NetworkOut exceeds **6MB**, a new instance is launched.
- **Scale Down:** If NetworkOut falls below **2MB**, an instance is removed.

### 2. Verify Auto Scaling
Run the following to check recent auto-scaling activities:
```bash
aws autoscaling describe-scaling-activities \
  --auto-scaling-group-name your-autoscaling-group-name \
  --region ap-south-1 \
  --query "Activities[*].[StartTime,StatusCode,Description]" \
  --output table
```

## Conclusion
You've successfully deployed your **Flask application** on AWS Elastic Beanstalk with **Auto Scaling enabled**! 🚀 If you have any issues, refer to the [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html).
