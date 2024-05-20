import requests
import boto3

sns = boto3.client('sns')

def monitor_performance():
    data = fetch_performance_data()
    
    issues = check_for_issues(data)
    
    if issues:
        send_alert(issues)
    
    return "Performance monitoring completed."

def fetch_performance_data():
    response = requests.get('https://api.example.com/performance')
    return response.json()

def check_for_issues(data):
    issues = []
    for campaign in data['campaigns']:
        if campaign['performance'] < threshold:
            issues.append(campaign)
    return issues

def send_alert(issues):
    message = f"Performance issues detected: {issues}"
    sns.publish(
        TopicArn='arn:aws:sns:region:account-id:topic-name',
        Message=message,
        Subject='Ad Performance Alert'
    )
