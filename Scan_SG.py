import boto3
import logging 

# Set the log level in the basic configuration.
logging.basicConfig(filename='sg_scanning.log',level=logging.DEBUG)

def get_security_group_rules(ec2_client):
    sg_rules = ec2_client.describe_security_group_rules()
    security_group_rules = sg_rules['SecurityGroupRules']
    return security_group_rules

#iterate through security group rules
def scan_security_group_rules(security_group_rules):
    #blank dictionary to add violators 
    sg_dict = {}
    
    try:
        for security_group_rule in security_group_rules:
            port_number = security_group_rule.get('FromPort', 'No Port Listed')
            cidrs = security_group_rule.get('CidrIpv4', 'No Cidr Listed')
            #if open to the world and not HTTP or HTTPS then update sg_dict with Rule ID and Group Id
            if cidrs == '0.0.0.0/0' and port_number != 80 and port_number != 443 and not security_group_rule['IsEgress']:
                print(security_group_rule['GroupId'] + ' is in violation and rule will be deleted for port ' + str(port_number) + ' : ' + cidrs)
                sg_dict.update({ security_group_rule['SecurityGroupRuleId'] : security_group_rule['GroupId'] })
                
    except:
        logging.info("scan_sgs exception")
        
    return sg_dict

#if no entries in sg_dict then there are no rules in violation
def delete_rules(ec2_resource, sg_rule_violators):
    try:
        if len(sg_rule_violators) == 0:
            print('No Security Group Violations')
        else:
            #iterate through sg_dict and for each entry revoke ingress using the Security Group ID and the Security Group Rule ID
            for RuleID, SGID in sg_rule_violators.items():
                security_group = ec2_resource.SecurityGroup(SGID)
                security_group.revoke_ingress(
                    SecurityGroupRuleIds=[
                        RuleID,
                    ]
                )
    except:
        logging.info("delete_rules exception")

if __name__ == '__main__':
    ec2_client = boto3.client('ec2')
    ec2_resource = boto3.resource('ec2')
    
    security_group_rules = get_security_group_rules(ec2_client)
    sg_rule_violators = scan_security_group_rules(security_group_rules)
    delete_rules(ec2_resource, sg_rule_violators)


