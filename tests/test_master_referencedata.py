import os

import conftest
import jobs.master_referencedata
# from jobs.master_referencedata import *

spark = conftest.setUp()

def test_master_referencedata():
    print("gkl inside test_master_referencedata")

    test_df1_raw = (jobs.master_referencedata.
               master_referencedata_extract
               (spark, os.getcwd() + '/' + 'test_data/Policy_Input_data.csv'))

    test_df1_transformed = (jobs.master_referencedata.
                            master_referencedata_transform(test_df1_raw))


    expected_df1_raw = (jobs.master_referencedata.
               master_referencedata_extract
               (spark, 'test_data/Policy_Input_data.csv'))

    expected_df1_transformed = (jobs.master_referencedata.
                            master_referencedata_transform(expected_df1_raw))

    assert test_df1_transformed.collect() == expected_df1_transformed.collect()

conftest.tearDown(spark)

#     return (test_df1_transformed)
#
# if __name__ == '__main__':
#     test_df = test_master_referencedata()
#     print(test_df.show())
