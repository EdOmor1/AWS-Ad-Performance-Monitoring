import json
from performance_monitor import monitor_performance

def lambda_handler(event, context):
    result = monitor_performance()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
