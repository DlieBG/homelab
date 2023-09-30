import subprocess, schedule, time, os

def job():
    subprocess.run([
        'aws',
        's3',
        'sync',
        '/backup/',
        f's3://{os.getenv("S3_BUCKET_NAME")}/',
        '--endpoint-url',
        f'{os.getenv("S3_ENDPOINT")}',
        '--region',
        f'{os.getenv("S3_REGION")}',
        '--delete'
    ])

schedule.every().day.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
