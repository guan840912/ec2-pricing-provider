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

print ("all region test t2.micro")

region = [  'us-east-1','us-east-2','us-west-2','us-west-1',
            'af-south-1','ap-east-1','ap-south-1','ap-northeast-2',
            'ap-northeast-1','ap-southeast-1','ap-southeast-2',
            'ca-central-1','eu-central-1','eu-west-1',
            'eu-west-2','eu-west-3','eu-north-1','eu-south-1',
            'sa-east-1'
]

def run(instancetype):
    for i in region:
        print(f'{i} USD {getinstancepricing(instancetype,i)}'.format(i))

run('t2.micro')