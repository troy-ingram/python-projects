import boto3

ec2 = boto3.client('ec2')
sg_rules = ec2.describe_security_group_rules()

ec2_resource = boto3.resource('ec2')


cidr_violators = []
sg_dict = {}

security_groups_rules = sg_rules['SecurityGroupRules']
# print(security_groups_rules)
for security_group_rule in security_groups_rules:
    port_number = security_group_rule.get('FromPort', 'No Port Listed')
    cidrs = security_group_rule.get('CidrIpv4', 'No Cidr Listed')
    if cidrs == '0.0.0.0/0' and port_number != 80 and port_number != 443 and not security_group_rule['IsEgress']:
        print(security_group_rule['GroupId'] + 'is in violation and rule will be deleted for port ' + str(port_number) + ' : ' + cidrs)
        cidr_violators.append(security_group_rule['SecurityGroupRuleId'])
        sg_dict.update({ security_group_rule['SecurityGroupRuleId'] : security_group_rule['GroupId'] })

if len(sg_dict) == 0:
    print('No Security Group Violations')

for x, y in sg_dict.items():
    security_group = ec2_resource.SecurityGroup(y)
    security_group.revoke_ingress(
        SecurityGroupRuleIds=[
            x,
            ]
    )


