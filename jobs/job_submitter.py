import os

import yaml
import conftest
import jobs.master_referencedata

# print(os.getcwd())
#Reading config.yaml file for input parameters - file path and filename in prod
with open('config.yaml') as config_file:
    parms = yaml.safe_load(config_file)
    print(parms)

prod_input_path = parms.get('prod_input_path')
prod_file_name = parms.get('prod_file_name')

# print(prod_input_path)
# print(prod_file_name)
#
# test_input_path = '/Users/goksmeth/PycharmProjects/jenkins_cicd_poc_v1/tests'
# test_file_name = 'Policy_Input_data.csv'
# prod_input_path = test_input_path
# prod_file_name = test_file_name

if __name__ == "__main__":
    #Setting up SparkSession
    spark = conftest.setUp()

    #Performing data extraction/read operation
    in_df1_raw = jobs.master_referencedata.master_referencedata_extract(spark, prod_input_path + '/' + prod_file_name)

    #Performing data transformation
    in_df1_transformed = jobs.master_referencedata.master_referencedata_transform(in_df1_raw)

    #Load operation skipped as part of this demo

    #Stopping the SparkSession
    conftest.tearDown(spark)