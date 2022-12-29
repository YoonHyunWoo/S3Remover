from tqdm import tqdm
import boto3


client = boto3.client('s3')
s3 = boto3.resource('s3')
response = client.list_buckets()
response["Buckets"]
deleteBucketList = []
saveBucketList = ["quiz.sebuung.team"]

print("only this buckes are saved :")
for saveBucket in saveBucketList:
    print('\t', saveBucket,end='')

auth = input("\nrun delete?[Y/N] : ")


if(auth.upper()=="Y"):
    print("start delete..")
    for bucket in tqdm(response["Buckets"]) :
        buff = True
        bucketName = bucket["Name"]
        for saveBucket in saveBucketList:
            if (bucketName == saveBucket):
                buff = False
                break
        if(buff):
            deleteBucketList.append(bucketName)
            try:
                client.delete_bucket(
                Bucket=bucketName,
                )
            except:
                deleteBucket = s3.Bucket(bucketName)
                deleteBucket.object_versions.delete()
                client.delete_bucket(
                Bucket=bucketName,
                )
    
    if (len(deleteBucketList)==0):
        print("Can't find non-saved bucket ")
    else:
        print("bucket : ")
        for bucket in deleteBucketList:
            print('\t', bucket)
        print("are deleted, total : ", len(deleteBucketList))

    
elif(auth.upper()=="N"):
    print("Stop delete")
else:
    print("you can input only 'Y' or 'N'")