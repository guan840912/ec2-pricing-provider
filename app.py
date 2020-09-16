from datetime import datetime
import boto3
import json
import sys
def region_map(region:str):
    try:
        region_physical_name = 'mock'
        if region=='us-east-1':
            region_physical_name='US East (N. Virginia)'
        if region=='us-east-2':
            region_physical_name='US East (Ohio)'
        if region=='us-west-1':
            region_physical_name='US West (N. California)'
        if region=='us-west-2':
            region_physical_name='US West (Oregon)'
        if region=='af-south-1':
            region_physical_name='Africa (Cape Town)'
        if region=='ap-east-1':
            region_physical_name='Asia Pacific (Hong Kong)'
        if region=='ap-south-1':
            region_physical_name='Asia Pacific (Mumbai)'
        if region=='ap-northeast-2':
            region_physical_name='Asia Pacific (Seoul)'
        if region=='ap-southeast-1':
            region_physical_name='Asia Pacific (Singapore)'
        if region=='ap-southeast-2':
            region_physical_name='Asia Pacific (Sydney)'
        if region=='ap-northeast-1':
            region_physical_name='Asia Pacific (Tokyo)'
        if region=='ca-central-1':
            region_physical_name='Canada (Central)'
        if region=='eu-central-1':
            region_physical_name='EU (Frankfurt)'
        if region=='eu-west-1':
            region_physical_name='EU (Ireland)'
        if region=='eu-west-2':
            region_physical_name='EU (London)'
        if region=='eu-west-3':
            region_physical_name='EU (Paris)'
        if region=='me-south-1':
            region_physical_name='Middle East (Bahrain)'
        if region=='sa-east-1':
            region_physical_name='South America (Sao Paulo)'
        
    except:
        print ('not_region_keys') 
    return region_physical_name

def ix(dic, n): #don't use dict as  a variable name
    try:
       return list(dic)[n] # or sorted(dic)[n] if you want the keys to be sorted
    except IndexError:
       print ('notenoughkeys')

def getfirstkeyObject(dic):
    try:
        key = ix(dic,0)
        dic2 = dic[key]
        key2 = ix(dic2,0)
        dic3 = dic2[key2]
        key3 = ix(dic3,0)
        dic4 = dic3[key3]
        return dic4["pricePerUnit"]["USD"]
    except:
       pass

def getinstancepricing(instanceType:str or None ,region:str ):
    products_filters=[
            {
                'Field': 'instanceType',
                'Type': 'TERM_MATCH',
                'Value': instanceType
            },
            {
                'Field': 'location',
                'Type': 'TERM_MATCH',
                'Value': region_map(region)
            },
            {
                'Field': 'capacitystatus',
                'Type': 'TERM_MATCH',
                'Value': 'Used'
            },
            {
                'Field': 'operation',
                'Type': 'TERM_MATCH',
                'Value': 'RunInstances'
            },
            {
                'Field': 'operatingSystem',
                'Type': 'TERM_MATCH',
                'Value': 'Linux'
            },
            {
                'Field': 'tenancy',
                'Type': 'TERM_MATCH',
                'Value': 'Shared'
            }
        ]
    if region_map(region) == None:
        print ('No Such Region {}'.format(region))
        pass

    client = boto3.client('pricing',region_name='us-east-1')
    response = client.get_products(
        ServiceCode='AmazonEC2',
        Filters=products_filters
    )

    price_list = response["PriceList"]
    if not price_list:
        res = 'No Such InstanceType {instanceType} or Can not get pricing in Region {region}'.format(instanceType=instanceType,region=region)
        pass
    if price_list:
        terms = json.loads(price_list[0])
        termsOndemand = terms["terms"]["OnDemand"]
        price = format(float(getfirstkeyObject(termsOndemand)),'.4f')
        res = str('%g'%(float(price)))
    return res

#print("us-east-1")
#print("m6g.medium "+getinstancepricing('m6g.medium', 'us-east-1'))
#print("m6g.large "+getinstancepricing('m6g.large','us-east-1'))
#print("t4g.medium "+getinstancepricing('t4g.medium','us-east-1'))
#print("t4g.large "+ getinstancepricing('t4g.large','us-east-1'))
#print("t4g.xlarge "+ getinstancepricing('t4g.xlarge','us-east-1'))
#print("t4g.2xlarge "+ getinstancepricing('t4g.2xlarge','us-east-1')) 
#
#print("ap-northeast-1")
#print("m6g.medium "+getinstancepricing('m6g.medium','ap-northeast-1'))
#print("m6g.large "+getinstancepricing('m6g.large','ap-northeast-1'))
#print("t4g.medium "+getinstancepricing('t4g.medium','ap-northeast-1'))
#print("t4g.large "+ getinstancepricing('t4g.large','ap-northeast-1'))
#print("t4g.xlarge "+ getinstancepricing('t4g.xlarge','ap-northeast-1'))
#print("t4g.2xlarge "+ getinstancepricing('t4g.2xlarge','ap-northeast-1'))

print ("all region test t2.micro")
print("'us-east-1' " + getinstancepricing('t2.micro','us-east-1'))
print("'us-east-2' " + getinstancepricing('t2.micro','us-east-2'))
print("'us-west-1' " + getinstancepricing('t2.micro','us-west-1'))
print("'us-west-2' " + getinstancepricing('t2.micro','us-west-2'))

print("'af-south-1' " + getinstancepricing('t2.micro','af-south-1'))

print("'ap-east-1' " + getinstancepricing('t2.micro','ap-east-1'))
print("'ap-south-1' " + getinstancepricing('t2.micro','ap-south-1'))
print("'ap-northeast-2' " + getinstancepricing('t2.micro','ap-northeast-2'))
print("'ap-southeast-1' " + getinstancepricing('t2.micro','ap-southeast-1'))
print("'ap-southeast-2' " + getinstancepricing('t2.micro','ap-southeast-2'))
print("'ap-northeast-1' " + getinstancepricing('t2.micro','ap-northeast-1'))

print("'ca-central-1' " + getinstancepricing('t2.micro','ca-central-1'))

print("'eu-central-1' " + getinstancepricing('t2.micro','eu-central-1'))
print("'eu-west-3' " + getinstancepricing('t2.micro','eu-west-3'))
print("'eu-west-1' " + getinstancepricing('t2.micro','eu-west-1'))
print("'eu-west-2' " + getinstancepricing('t2.micro','eu-west-2'))
print("'eu-north-1' " + getinstancepricing('t2.micro','eu-north-1'))
print("'eu-south-1' " + getinstancepricing('t2.micro','eu-south-1'))
print("'sa-east-1' " + getinstancepricing('t2.micro','sa-east-1'))


print ("all region test t4g.medium")
print("'us-east-1' " + getinstancepricing('t4g.medium','us-east-1'))
print("'us-east-2' " + getinstancepricing('t4g.medium','us-east-2'))
print("'us-west-1' " + getinstancepricing('t4g.medium','us-west-1'))
print("'us-west-2' " + getinstancepricing('t4g.medium','us-west-2'))

print("'af-south-1' " + getinstancepricing('t4g.medium','af-south-1'))

print("'ap-east-1' " + getinstancepricing('t4g.medium','ap-east-1'))
print("'ap-south-1' " + getinstancepricing('t4g.medium','ap-south-1'))
print("'ap-northeast-2' " + getinstancepricing('t4g.medium','ap-northeast-2'))
print("'ap-southeast-1' " + getinstancepricing('t4g.medium','ap-southeast-1'))
print("'ap-southeast-2' " + getinstancepricing('t4g.medium','ap-southeast-2'))
print("'ap-northeast-1' " + getinstancepricing('t4g.medium','ap-northeast-1'))

print("'ca-central-1' " + getinstancepricing('t4g.medium','ca-central-1'))

print("'eu-central-1' " + getinstancepricing('t4g.medium','eu-central-1'))
print("'eu-west-3' " + getinstancepricing('t4g.medium','eu-west-3'))
print("'eu-west-1' " + getinstancepricing('t4g.medium','eu-west-1'))
print("'eu-west-2' " + getinstancepricing('t4g.medium','eu-west-2'))
print("'eu-north-1' " + getinstancepricing('t4g.medium','eu-north-1'))
print("'eu-south-1' " + getinstancepricing('t4g.medium','eu-south-1'))