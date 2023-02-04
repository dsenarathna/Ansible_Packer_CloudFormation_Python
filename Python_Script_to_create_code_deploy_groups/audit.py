#!/usr/bin/env python
#
    pip install skew -- install skew before running this script
    List AWS services being used region wise
#
import skew
from skew.arn import ARN
arn = ARN()
services=arn.service.choices()
services.sort()
print('Enumerating all resources in the following services: ' + ' '.join(services) + '\n')
resources = [];
for service in services:
  arn.service.pattern = service
  for resource in arn:
      with open('myAWSServices-listAudit', 'a') as file1:
          file1.write(resource)
      with open('myAWSServices-detailAudit','a') as file2:
          file2.write(resource.data)
  file.close()
