*** Settings ***
Resource            MTDb.robot
Default Tags        Common
Library             MTLibrary     ./pnscr0672_dbs


*** Test Cases ***
Version Check MT
    [Tags]                      Test        Common
    [Template]                  Check MT version info 
    ${Target MT Version LTE}    LTE
    ${Target MT Version 3G}     3G

Version Check SNR
    [Tags]                      Test        Common
    [Template]                  Check SNR version info
    ${Target SNR Version LTE}   LTE
    ${Target SNR Version 3G}    3G

#===========================================================================================================
Macro 2345 
    [Tags]          2345    Common
    Given Parameter 5076 and parameter price 185 the parameter price name should be ${Macro_2345_185_exit_code}

#===========================================================================================================
