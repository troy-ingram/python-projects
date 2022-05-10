import boto3

ec2 = boto3.client('ec2')
sg_rules = ec2.describe_security_group_rules()
security_groups_rules = sg_rules['SecurityGroupRules']

ec2_resource = boto3.resource('ec2')


#blank dictionary to add violators 
sg_dict = {}

#iterate through security group rules
for security_group_rule in security_groups_rules:
    port_number = security_group_rule.get('FromPort', 'No Port Listed')
    cidrs = security_group_rule.get('CidrIpv4', 'No Cidr Listed')
    #if open to the world and not HTTP or HTTPS then update sg_dict with Rule ID and Group Id
    if cidrs == '0.0.0.0/0' and port_number != 80 and port_number != 443 and not security_group_rule['IsEgress']:
        print(security_group_rule['GroupId'] + ' is in violation and rule will be deleted for port ' + str(port_number) + ' : ' + cidrs)
        sg_dict.update({ security_group_rule['SecurityGroupRuleId'] : security_group_rule['GroupId'] })

#if no entries in sg_dict then there are no rules in violation
if len(sg_dict) == 0:
    print('No Security Group Violations')

#iterate through sg_dict and for each entry revoke ingress using the Security Group ID and the Security Group Rule ID
for RuleID, SGID in sg_dict.items():
    security_group = ec2_resource.SecurityGroup(SGID)
    security_group.revoke_ingress(
        SecurityGroupRuleIds=[
            RuleID,
        ]
    )


