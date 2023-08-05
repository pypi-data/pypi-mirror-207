# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepar and clean the data. We check and imput for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To run the code
 - We have to create an environment from env.yml file which is attached in this repository .
 - Command to create environment - `conda env create -f env.yml`
 - Command tp see newly created environment - `conda env list`
 - Command to activate the environment - `conda activate mle-dev`
 - Now execute the python script .

 ## To execute the python script
 - We have to go to scripts folder where final script is present .
 - command to run the scripts - `python scripts/mlflowrun.py`
OR

 - We can run individual file from src -> py_packages folder
 - python src/py_packages/ingest.py <--path , --log_level, --log_path --no_console_log>
   python src/py_packages/train.py <--train_folder,--output_folder,--log_level,--log_path,--no_consoler_log>
   python src/py_packages/score.py <--model-folder,--data_folder,--log_level,--log_path,--no_consoler_log>


1) ingest_data : To download the data and split into train and test (arguments can be passed to give download path)
    - While executing the script to terminal , data will get stored as per the default settings
    - Arguments that can be passed : <--path , --log_level, --log_path --no_console_log>
       * --path :: Specify the path for the training dataset
       * --log_level :: Specify the level of log required
       * --log_path :: Specify the location where logs to be created (If not specified no logs will be created)
       * --no_console_log :: Specify the log to console


 2) train : To fit and train different models based on the training data provided
    - Argumentd that can be passed : <--train_folder,--output_folder,--log_level,--log_path,--no_consoler_log>
       * --train_folder :: Specify path with file name where the train data is present.
       * --output_folder :: Specify the location where the trained models pkl files to save.
       * --log_level :: Specify the level of log required
       * --log_path :: Specify the location where logs to be created (If not specified no logs will be created)
       * --no_console_log :: Specify the log to console



 3) score : To check the scores of model on the new data passed.
    - Argumentd that can be passed : <--model-folder,--output-folder,--log_level,--log_path,--no_consoler_log>
      * --model_folder :: Specify the location where the models pkl file saved.
      * --data_folder :: Specify the location where test datasets are present.
      * --log_level :: Specify the level of log required
      * --log_path :: Specify the location where logs to be created (If not specified no logs will be created)
      * --no_console_log :: Specify the log to console




