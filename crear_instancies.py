import csv
import boto3

def crear_servidores():
    ec2 = boto3.client('ec2')
    subnet_id = "subnet-0e233578545ca832b"
    vpc_id = "vpc-036abdf6fe15d3ea0"
    
    sgs = ec2.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['SecurityGroups']
    sg_id = sgs[0]['GroupId']

    creadas = []

    with open('maquinas.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            res = ec2.run_instances(
                ImageId=row['ImageId'],
                InstanceType=row['InstanceType'],
                KeyName='vockey',
                MinCount=1,
                MaxCount=1,
                SubnetId=subnet_id,
                SecurityGroupIds=[sg_id],
                TagSpecifications=[{
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': row['Name']}]
                }]
            )
            inst_id = res['Instances'][0]['InstanceId']
            creadas.append({'Name': row['Name'], 'InstanceId': inst_id})
            print(f"Instancia {row['Name']} creada exitosamente con ID: {inst_id}")

    with open('ids_creats.csv', mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['Name', 'InstanceId'])
        writer.writeheader()
        for c in creadas:
            writer.writerow(c)

if __name__ == '__main__':
    crear_servidores()
