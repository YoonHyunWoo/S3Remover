# S3Remover

I had to delete so many buckets so i make this python program

after running code, removed all buckets in account ignore only saveBucketList 
saveBucketList can defined line10 in S3Remover.py

you can running S3Remover will look like 

first you could configure credentials use under code

```bash
aws configurek
```

however not installing aws cli, you can installing awscli:

- **Linux**
    
    ```bash
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    ```
    
- **MacOs**
    
    ```bash
    curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
    sudo installer -pkg AWSCLIV2.pkg -target /
    ```
    
- **Windows**
    
    ```bash
    msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    ```
    

now you can running S3Remover will like this

```bash
python S3Remover.py
```

after few seconds, you can check removed s3 bucket