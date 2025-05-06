--!jinja2

CREATE OR REPLACE TABLE {{ install_db }}.{{ ops_schema }}.TEST_OPERATIONS(KEY STRING, VALUE STRING);

INSERT INTO {{ install_db }}.{{ ops_schema }}.TEST_OPERATIONS
VALUES
('INSTALL_DB','{{ install_db }}'),
('ADMIN_SCHEMA','{{ admin_schema }}'),
('OPS_SCHEMA','{{ ops_schema }}'),
('RESULT_SCHEMA','{{ results_schema }}'),
('INSTALL_STAGE','{{ install_stage }}'),
('OPS_WH','{{ ops_wh }}');

CREATE OR REPLACE STREAMLIT {{ install_db }}.{{ ops_schema }}.STM_STREAMLIT
ROOT_LOCATION = '@{{install_db}}.{{ops_schema}}.{{install_stage}}'
MAIN_FILE = 'serverless_task_migration.py'
QUERY_WAREHOUSE = {{ops_wh}}
COMMENT='{"origin": "sf_sit","name": "sit_serveless_task_migration","version": "{major: 1, minor: 0}"}';
