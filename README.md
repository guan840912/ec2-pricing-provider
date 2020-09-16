# ec2-pricing-provider
Easy to get aws ec2 on-demand pricing

## Support Region 

| region | Physical Name |
|--------|---|
|us-east-2|US East (Ohio)|
|us-west-1|US West (N. California)|
|us-west-2|US West (Oregon)|
|af-south-1|Africa (Cape Town)|
|ap-east-1|Asia Pacific (Hong Kong)|
|ap-south-1|Asia Pacific (Mumbai)|
|ap-northeast-2|Asia Pacific (Seoul)|
|ap-southeast-1|Asia Pacific (Singapore)|
|ap-southeast-2|Asia Pacific (Sydney)|
|ap-northeast-1|Asia Pacific (Tokyo)|
|ca-central-1|Canada (Central)|
|eu-central-1|EU (Frankfurt)|
|eu-west-1|EU (Ireland)|
|eu-west-2|EU (London)|
|eu-west-3|EU (Paris)|
|me-south-1|Middle East (Bahrain)|
|sa-east-1|South America (São Paulo)|


```bash 
python app.py

# output
all region test
'us-east-1' 0.0116
'us-east-2' 0.0116
'us-west-1' 0.0138
'us-west-2' 0.0116
'af-south-1' No Such InstanceType t2.micro or Can not get pricing in Region af-south-1
'ap-east-1' No Such InstanceType t2.micro or Can not get pricing in Region ap-east-1
'ap-south-1' 0.0124
'ap-northeast-2' 0.0144
'ap-southeast-1' 0.0146
'ap-southeast-2' 0.0146
'ap-northeast-1' 0.0152
'ca-central-1' 0.0128
'eu-central-1' 0.0134
'eu-west-3' 0.0132
'eu-west-1' 0.0126
'eu-west-2' 0.0132
'eu-north-1' No Such InstanceType t2.micro or Can not get pricing in Region eu-north-1
'eu-south-1' No Such InstanceType t2.micro or Can not get pricing in Region eu-south-1

# all region test t4g.medium
'us-east-1' 0.0336
'us-east-2' 0.0336
'us-west-1' No Such InstanceType t4g.medium or Can not get pricing in Region us-west-1
'us-west-2' 0.0336
'af-south-1' No Such InstanceType t4g.medium or Can not get pricing in Region af-south-1
'ap-east-1' No Such InstanceType t4g.medium or Can not get pricing in Region ap-east-1
'ap-south-1' 0.0224
'ap-northeast-2' No Such InstanceType t4g.medium or Can not get pricing in Region ap-northeast-2
'ap-southeast-1' No Such InstanceType t4g.medium or Can not get pricing in Region ap-southeast-1
'ap-southeast-2' No Such InstanceType t4g.medium or Can not get pricing in Region ap-southeast-2
'ap-northeast-1' 0.0432
'ca-central-1' No Such InstanceType t4g.medium or Can not get pricing in Region ca-central-1
'eu-central-1' 0.0384
'eu-west-3' No Such InstanceType t4g.medium or Can not get pricing in Region eu-west-3
'eu-west-1' 0.0368
'eu-west-2' No Such InstanceType t4g.medium or Can not get pricing in Region eu-west-2
'eu-north-1' No Such InstanceType t4g.medium or Can not get pricing in Region eu-north-1
'eu-south-1' No Such InstanceType t4g.medium or Can not get pricing in Region eu-south-1
```