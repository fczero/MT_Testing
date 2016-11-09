SET FOLDERNAME=test_results
SET DB_PATH_E=SUT_ENG
SET DB_PATH_J=SUT_JAP
SET JAP_PATH=%FOLDERNAME%/JAPANESE
SET ENG_PATH=%FOLDERNAME%/ENGLISH
timeout 5
REM check robocopy behavior with symbolic links
REM call delete_dbs.bat
REM ROBOCOPY ".\%DB_PATH_J%" "."
REM call robot -d %JAP_PATH% --variablefile jap_variables_macro.py -i Common -L trace db_check_macro.robot
REM call delete_dbs.bat
REM ROBOCOPY ".\%DB_PATH_E%" "."
REM call robot -d %ENG_PATH% --variablefile eng_variables_macro.py -i Common -L trace db_check_macro.robot
REM call delete_dbs.bat
