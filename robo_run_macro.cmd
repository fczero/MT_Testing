SET FOLDERNAME=test_results
SET DB_PATH_E=SUT_ENG
SET DB_PATH_J=SUT_JAP
SET JAP_PATH=%FOLDERNAME%/JAPANESE
SET ENG_PATH=%FOLDERNAME%/ENGLISH
timeout 5
call delete_dbs.bat
ROBOCOPY ".\%DB_PATH_J%" "."
call robot -d %JAP_PATH% --variablefile jap_variables_macro.py -i Common -L trace db_check_macro.robot
call delete_dbs.bat
ROBOCOPY ".\%DB_PATH_E%" "."
call robot -d %ENG_PATH% --variablefile eng_variables_macro.py -i Common -L trace db_check_macro.robot
call delete_dbs.bat
