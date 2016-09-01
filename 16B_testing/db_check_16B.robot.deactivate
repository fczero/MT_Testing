*** Settings ***
Library           String
Library           Collections
Library           OperatingSystem
Library           db_helper.py
Library           DatabaseLibrary
Force Tags        English
#Suite Setup       Initialize Paths

*** Test Cases ***
Version Check MT
    [Tags]                      Japanese
    [Template]                  Check MT version info 
    ${Target MT Version LTE}    LTE
    ${Target MT Version 3G}     3G

Version Check SNR
    [Tags]                      Japanese
    [Template]                  Check SNR version info
    ${Target SNR Version LTE}   LTE
    ${Target SNR Version 3G}    3G

API 1020
    Check if combo box string is correct    1036    3    ${Macro 1020 combo index 3 string}

API 1336
    [Template]      Check if parameter attribute is correct
    : FOR    ${index}    IN RANGE    len(@{Macro 1336 affected parameter numbers})
    \   @{Macro 1336 affected parameter numbers}[${index}]         @{Macro 1336 parameter name changes}[${index}]

API 1337
    [Template]      Check if parameter attribute is correct
    : FOR    ${index}    IN RANGE    len(@{Macro 1337 affected parameter numbers})
    \   @{Macro 1337 affected parameter numbers}[${index}]         @{Macro 1337 parameter name changes}[${index}]

API 2391
    [Tags]      Japanese
    Check if exit code value is correct     2391    30    ${Macro 2391 30 exit code string}
    
API 2392
    [Tags]      Japanese
    Check if limit print string is correct   5284       ${Macro 2392 limit print string 1_6}
    Check if limit print string is correct   5285       ${Macro 2392 limit print string 1_8}

API 2393
    [Tags]      Japanese
    Check if exit code value is correct      2393    30     ${Macro 2393 30 exit code string}
    Check if limit print string is correct   5284    ${Macro 2393 limit print string 1_6}
    Check if limit print string is correct   5285    ${Macro 2393 limit print string 1_8}

API 3040
    Check if combo box string is correct    3005    2   ${Macro 3040 combo index 2 string}
    Check if combo box string is correct    3005    3   ${Macro 3040 combo index 3 string}
    Check if combo box string is correct    3005    5   ${Macro 3040 combo index 5 string}

#Check connect to databse
#    [Tags]      test
#    Connect To Database Using Custom Params    sqlite3    database="./cp_combo_name.db"

*** Keywords ***
Check if parameter attribute is correct
    [Arguments]        ${parameter no}        ${parameter name}
    ${actual} =    Get Parameter Attribute      ${parameter no}         parameter
    Should be equal as strings    ${actual}    ${parameter name}

Check if exit code value is correct
    [Arguments]        ${macro no}        ${exit code value}        ${exit code string}
    ${actual} =     Get Exit Code Attribute     ${macro no}        ${exit code value} 
    Should be equal as strings    ${actual}    ${exit code string}

Check if limit print string is correct
    [Arguments]        ${parameter no}        ${limit print string}
    ${actual} =    Get Parameter Attribute      ${parameter no}     limit_print_string
    Should be equal as strings    ${actual}    ${limit print string}

Check if combo box string is correct
    [Arguments]        ${parameter no}        ${combo index}       ${combo string}
    ${actual} =    Get Combo Box Value Attribute    ${parameter no}   ${combo index}    parameter_price_name
    Should be equal as strings    ${actual}    ${combo string}

Check MT version info
    [Arguments]                   ${MT target}             ${RAT}
    ${MT actual} =                Get MT Version           ${RAT} 
    Should be equal as strings    ${MT actual}       ${MT target}

Check SNR version info
    [Arguments]                   ${SNR target}      ${RAT}
    ${SNR actual} =               Get Scenario Version     ${RAT} 
    Should be equal as strings    ${SNR actual}      ${SNR target}

#Initialize Paths
