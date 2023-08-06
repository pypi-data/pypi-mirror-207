from __future__ import print_function
import volcenginesdkautoscaling
import volcenginesdkcore
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"
    configuration.client_side_validation = True
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    api_instance = volcenginesdkautoscaling.AUTOSCALINGApi()

    try:
        resp = api_instance.describe_scaling_groups(volcenginesdkautoscaling.DescribeScalingGroupsRequest(
            _configuration=configuration
        ))
        pprint(resp)
    except ApiException as e:
        print("Exception when calling AUTOSCALINGApi->describe_scaling_groups: %s\n" % e)
