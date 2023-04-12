This repository contains code that shows how to run STF tests against StreamSets Control Hub 3.x

### Pre-requisites
* [Python 3.4+](https://docs.python.org/3/using/index.html) and pip3 installed
* StreamSets Test Framework [installed](https://streamsets.com/documentation/stf/latest/installation.html) 
* [Access to StreamSets DataOps_Platform](https://docs.streamsets.com/portal/platform-controlhub/controlhub/UserGuide/GettingStarted/GettingStarted_title.html) with an user account in your  organization 
* At least one [StreamSets Data Collector](https://streamsets.com/products/dataops-platform/data-collector/) instance registered with the above StreamSets DataOps Platform instance
and has a label = e.g. 'sdc-5.2.0'

0. Create API Credntials.
Go to StreamSets DataOps instance, from left click on Manage → Api Credentials 
 Make sure to store them. Note the env. variables here CRED_ID and CRED_TOKEN.


1. Set up the following environment variables:

CRED_ID - This is found from the above step of creating API credentials. 

CRED_TOKEN  - This is found from the above step of creating API credentials.

SDC_ID - This corresponds to the above StreamSets Data Collector. It can be founf d eom the UI once you c lick on `Set Up` --> `Engines` and then on that particular SDC.

SDC_LABEL - This is found from the above SDC.

2. Clone this branch of repo. Say the path on the system, after the cloning is $PATH/stf_tests

### Run tests
1. Change to a directory where tests exist

```cd $PATH/stf_tests```

2. Run the following command

```
stf test -vs \
--sch-credential-id ${CRED_ID} \
--sch-token "${CRED_TOKEN}" \
--sch-authoring-sdc "${SDC_ID}" \
--sch-executor-sdc-label "${SDC_LABEL}" \
test_simple_entities.py
 ```

On success, the output will end similar to the following line
```
=================== 1 passed in 74.26s (0:01:14) ===================
```


