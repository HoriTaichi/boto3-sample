import argparse
import boto3

"""
各関数
"""
def set_rule_argument(parser):
    parser.add_argument('--date', action='store', help='DATEはYYYYMMDD形式で入力をお願いします')
    return parser.parse_args()

"""
Main
受け取ったパラメータを解析してEMRを呼ぶ
"""
client = boto3.client('emr')
response = client.run_job_flow(
    Name='EMR動作確認',
    LogUri='s3://hori-bucket-2019/emr/logs',
    ReleaseLabel='emr-5.17.1',
    Instances={
        'MasterInstanceType': 'm3.xlarge',
        'SlaveInstanceType': 'm3.xlarge',
        'InstanceCount': 3,
        'Ec2KeyName': 'horiPrivateKeyPair',
        'Placement': {
            'AvailabilityZone': 'ap-northeast-1a',
        },
    },
    Steps=[
        {
            'Name': 'Apache Spark実行',
            'ActionOnFailure': 'CANCEL_AND_WAIT',
            'HadoopJarStep': {
                'Jar': 'command-runner.jar',
                'Args': [ 'spark-submit',
                    '--master', 'local[4]',
                    '--class', 'SimpleApp', 's3://hori-bucket-2019/emr/target/scala-2.11/simple-project_2.11-1.0.jar',
                ]
            }
        },
    ],
    Applications=[
        {
            'Name': 'Spark',
        },
    ],
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    Tags=[
        {
            'Key': 'user:Application',
            'Value': 'emr-sample'
        },
    ],
)
