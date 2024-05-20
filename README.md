# AWS-Ad-Performance-Monitoring

## Overview
This project provides a real-time ad performance monitoring system using AWS services.

## Architecture
![Architecture Diagram](diagrams/architecture_diagram.png)

## AWS Services Used
- AWS Lambda
- Amazon RDS
- Amazon SNS
- Amazon CloudWatch

## Features
- Real-time monitoring of ad performance.
- Alerts for performance issues using Amazon SNS.
- Scalable and cost-effective monitoring solution.

## Prerequisites
- AWS account
- API access to advertising platforms (e.g., DV360, Amazon DSP, TradeDesk, CM360).

## Setup

### Step 1: Deploy Infrastructure
1. Deploy the CloudFormation stack using `infrastructure/cloudformation_template.yaml`.

### Step 2: Configure Lambda Functions
1. Update `src/performance_monitor.py` with API credentials and endpoints.
2. Deploy the Lambda functions using the AWS Lambda console or AWS CLI.

## Usage
1. The Lambda function `performance_monitor.py` runs periodically to fetch ad performance data.
2. It sends alerts via Amazon SNS if performance issues are detected.
