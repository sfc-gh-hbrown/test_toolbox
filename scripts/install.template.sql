USE WAREHOUSE COMPUTE_WH;
USE ROLE accountadmin;
CREATE OR REPLACE DATABASE INSTALL_TEST;
CREATE SCHEMA IF NOT EXISTS TEST;
CREATE or replace STAGE INSTALL_TEST.TEST.QUICKSTART 
DIRECTORY = (ENABLE = TRUE);

GRANT OWNERSHIP ON STAGE INSTALL_TEST.TEST.QUICKSTART 
TO ROLE public COPY CURRENT GRANTS;

CREATE OR REPLACE TABLE INSTALL_TEST.TEST.TEST_OPERATIONS(KEY STRING, VALUE STRING);

INSERT INTO INSTALL_TEST.TEST.TEST_OPERATIONS
VALUES
('INSTALL_DB','INSTALL_TEST'),
('ADMIN_SCHEMA','TEST'),
('OPS_SCHEMA','TEST'),
('RESULT_SCHEMA','TEST'),
('INSTALL_STAGE','QUICKSTART');


PUT file:////builds/snowflake/solutions/snowflake-labs-emerging-solutions-toolbox-63f264/scripts/install.ipynb @INSTALL_TEST.TEST.QUICKSTART/ auto_compress = false overwrite = true;
-- PUT file:///{{ env.CI_PROJECT_DIR }}/solution/* @INSTALL_TEST.TEST.QUICKSTART/ auto_compress = false overwrite = true;

use role ACCOUNTADMIN;
use DATABASE {{ env.DATAOPS_DATABASE }};
use schema ANALYTICS;
CREATE OR REPLACE NOTEBOOK {{ env.DATAOPS_DATABASE }}.ANALYTICS.Generate_Quickstart
FROM '@{{ env.DATAOPS_DATABASE }}.ANALYTICS.QUICKSTART/docs'
MAIN_FILE = 'Generate_Quickstart.ipynb'
QUERY_WAREHOUSE = '{{ env.DATAOPS_CATALOG_SOLUTION_PREFIX }}_BUILD_WH';

ALTER NOTEBOOK {{ env.DATAOPS_DATABASE }}.ANALYTICS.Generate_Quickstart ADD LIVE VERSION FROM LAST;

EXECUTE NOTEBOOK {{ env.DATAOPS_DATABASE }}.ANALYTICS.Generate_Quickstart();
