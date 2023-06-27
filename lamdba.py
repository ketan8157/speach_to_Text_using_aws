import json
import boto3
import uuid

transcribe=boto3.client('transcribe')

def lambda_handler(event, context):
    print(event)
    ran=uuid.uuid1().int
    name='s3_get_file_lambda-'+str(ran)
    bucket=event["Records"][0]['s3']['bucket']['name']
    file=event["Records"][0]['s3']['object']['key']
    uri="s3://" + bucket + "/" + file
    print(" the file client put to convert into text : " ,"'" ,uri,"'")
    response=transcribe.start_transcription_job(TranscriptionJobName=name,LanguageCode='en-US',MediaFormat='mp3',Media={
        'MediaFileUri': uri,
        #'RedactedMediaFileUri': 'string'
    },OutputBucketName='transcribeoutputtakeinputfroms3throughlambda',OutputKey=file+"-out-"+str(ran)+".json")
