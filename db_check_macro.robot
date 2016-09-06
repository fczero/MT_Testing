*** Settings ***
Resource          MTDatabase.robot
Default Tags        Common

*** Test Cases ***
Version Check MT
    [Tags]      Test        Common
    [Template]                  Check MT version info 
    ${Target MT Version LTE}    LTE
#    ${Target MT Version 3G}     3G

Version Check SNR
    [Tags]      Test        Common
    [Template]                  Check SNR version info
    ${Target SNR Version LTE}   LTE
#    ${Target SNR Version 3G}    3G

#===========================================================================================================
Macro 3001
    [Tags]    English
    Run Keyword and continue on failure    Check if combo box string is correct    3005    2    ${Macro 3001 combo index 2 string}
    Run Keyword and continue on failure    Check if combo box string is correct    3005    3    ${Macro 3001 combo index 3 string}
    Run Keyword and continue on failure    Check if combo box string is correct    3005    5    ${Macro 3001 combo index 5 string}

Macro 2312
    [Tags]  Common
        Check if combo box string is correct    2766    3    ${Macro 2312 combo index 2 string}
