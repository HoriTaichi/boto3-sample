import argparse
import boto3

"""
各関数
"""
def set_rule_argument(parser):
    parser.add_argument('--date', action='store', help='DATEはYYYYMMDD形式で入力をお願いします')
    parser.add_argument('--abc', action='store', help='あああああ')
    return parser.parse_args()

"""
Main
受け取ったパラメータを解析して、適したEMRを呼ぶ
"""
client = boto3.client('emr')
response = client.run_job_flow(
    Name='色々変えて見る１',
    LogUri='s3://hori-bucket-2019/output',
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
            'Name': 'horihoriテスト始めるよ',
            'ActionOnFailure': 'CANCEL_AND_WAIT',
            'HadoopJarStep': {
                'Jar': 'command-runner.jar',
                'Args': [ 'spark-submit',
                    '--master', 'local[4]',
                    '--class', 'SimpleApp', 's3://hori-bucket-2019/emr/target/scala-2.11/simple-project_2.11-1.0.jar',
                    '--bucket', 'hori-bucket-2019'
                ]
            }
        },
    ],
    Applications=[
        {
            'Name': 'Hadoop',
        },
        {
            'Name': 'Spark',
        },
    ],
    Configurations=[
        {
           "Classification": "yarn-site",
           "Configurations": [],
           "Properties": {
               "spark.yarn.app.container.log.dir": "/var/log/hadoop-yarn"
            }
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
