Create DATABASE Covid;
Use Database Covid;

CREATE OR REPLACE TABLE covid_data (
    country STRING,
    cases INT,
    todayCases INT,
    deaths INT,
    todayDeaths INT,
    recovered INT,
    active INT,
    critical INT,
    updated TIMESTAMP
);

CREATE OR REPLACE STAGE covid_stage
URL='s3://Bucket_Name/'
CREDENTIALS = (AWS_KEY_ID = 'Acces_key' AWS_SECRET_KEY = 'Secret_Key')
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"');

COPY INTO covid_data
FROM @covid_stage/covid_data_pakistan.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"')
ON_ERROR = 'CONTINUE';

SELECT * FROM covid_data;