import boto3

ec2 = boto3.client('ec2')

sg_rules = ec2.describe_security_group_rules()

cidr_violators = []

security_groups_rules = sg_rules['SecurityGroupRules']
#iterate through security groups to see if there are any rules that are not HTTP/HTTPS using 0.0.0.0/0
for security_group_rule in security_groups_rules:
    port_number = security_group_rule.get('FromPort', 'No Port Listed')
    cidrs = security_group_rule.get('CidrIpv4', 'No Cidr Listed')
    if cidrs == '0.0.0.0/0' and port_number != 80 and port_number != 443 and not security_group_rule['IsEgress']:
        print(security_group_rule['GroupId'] + ' in violation ' + str(port_number) + ' : ' + cidrs)
        cidr_violators.append(security_group_rule['SecurityGroupRuleId'])


print(cidr_violators)
        

# for cidr_violator in cidr_violators:    
#     client.security_group.revoke_ingress(
#         SecurityGrouRuleIds=[
#             cidr_violator,
#             ]
    
#     )
