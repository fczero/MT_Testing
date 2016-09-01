*** Settings ***
Resource          MTDatabase.robot
Default Tags        Common

*** Test Cases ***
Version Check MT
    [Tags]      Test        Common
    [Template]                  Check MT version info 
    ${Target MT Version LTE}    LTE
    ${Target MT Version 3G}     3G

Version Check SNR
    [Tags]      Test        Common
    [Template]                  Check SNR version info
    ${Target SNR Version LTE}   LTE
    ${Target SNR Version 3G}    3G

#===========================================================================================================
Macro 1247 Name
    [Tags]          1247    Common
    Macro Name For Macro 1247 Should Be ${Macro 1247 name}

Macro 1247 Common Parameters
    [Tags]          1247    Common
    ${target param list} =      Filter Parameter List   1247    ${Macro 1247 new parameters indices}
    ${reference param list} =   Filter Parameter List   1240    ${Macro 1247 old parameters indices}
    Matching Parameter count should be equal    ${target param list}    ${reference param list}
    :FOR      ${div}    IN RANGE    len(${target param list})
    \      Loop Through Parameter Division List       @{target param list}[${div}]    @{reference param list}[${div}]

Macro 1247 Struct Parameters
    [Tags]          1247    Common
    ${parameter list} =        Get Struct Parameters Of Macro       1247
    :FOR      ${div}    IN RANGE    len(${parameter list})
    \      Loop Through Struct Division List       @{parameter list}[${div}]

Macro 1247 New Parameter Names
    [Tags]          1247    Common
    [Setup]             Setup New Parameters     1247   @{Macro 1247 new parameters indices}[0]     0
    [Template]      Check if parameter name is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1247 parameter name}[${index}]

Macro 1247 New Parameter Limit Print String
    [Tags]          1247    Common
    [Setup]             Setup New Parameters     1247   @{Macro 1247 new parameters indices}[0]     0
    [Template]      Check if limit print string is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1247 parameter limit print string}[${index}]

Macro 1247 New Parameter Input Form
    [Tags]          1247    Common
    [Setup]             Setup New Parameters     1247   @{Macro 1247 new parameters indices}[0]     0
    [Template]      Check if input form is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1247 parameter input form}[${index}]

Macro 1247 New Parameter Type
    [Tags]          1247    Common
    [Setup]             Setup New Parameters     1247   @{Macro 1247 new parameters indices}[0]     0
    [Template]      Check if parameter type is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1247 parameter type}[${index}]

Macro 1247 New Parameter Default Number
    [Tags]          1247    Common
    [Setup]             Setup New Parameters     1247   @{Macro 1247 new parameters indices}[0]     0
    [Template]      Check if default number is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1247 parameter limit print string}[${index}]

#===========================================================================================================
Macro 1354 Parameter Names
    [Tags]      English     1354
    [Template]  Check if parameter name is correct
    : FOR   ${index}    IN RANGE    len(@{Macro 1354 affected parameter numbers})
    \   @{Macro 1354 affected parameter numbers}[${index}]         @{Macro 1354 parameter name changes}[${index}]

#===========================================================================================================
Macro 1359 Name
    [Tags]      1359    Common
    Macro Name For Macro 1359 Should Be ${Macro 1359 name}

Macro 1359 Common Parameters
    [Tags]      1359    Common
    ${target param list} =      Filter Parameter List   1359    ${Macro 1359 new parameters indices}
    ${reference param list} =   Filter Parameter List   1354    ${Macro 1359 old parameters indices}
    Matching Parameter count should be equal    ${target param list}    ${reference param list}
    :FOR      ${div}    IN RANGE    len(${target param list})
    \      Loop Through Parameter Division List       @{target param list}[${div}]    @{reference param list}[${div}]

Macro 1359 Struct Parameters
    [Tags]      1359    Common
    ${parameter list} =        Get Struct Parameters Of Macro       1359
    :FOR      ${div}    IN RANGE    len(${parameter list})
    \      Loop Through Struct Division List       @{parameter list}[${div}]

Macro 1359 New Parameter Names
    [Tags]      1359    Common
    [Setup]             Setup New Parameters     1359   @{Macro 1359 new parameters indices}[1]     1
    [Template]      Check if parameter name is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1359 parameter name}[${index}]

Macro 1359 New Parameter Limit Print String
    [Tags]      1359    Common
    [Setup]             Setup New Parameters     1359   @{Macro 1359 new parameters indices}[1]     1
    [Template]      Check if limit print string is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1359 parameter limit print string}[${index}]

Macro 1359 New Parameter Input Form
    [Tags]      1359    Common
    [Setup]             Setup New Parameters     1359   @{Macro 1359 new parameters indices}[1]     1
    [Template]      Check if input form is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1359 parameter input form}[${index}]

Macro 1359 New Parameter Type
    [Tags]      1359    Common
    [Setup]             Setup New Parameters     1359   @{Macro 1359 new parameters indices}[1]     1
    [Template]      Check if parameter type is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1359 parameter type}[${index}]

Macro 1359 New Parameter Default Number
    [Tags]      1359    Common
    [Setup]             Setup New Parameters     1359   @{Macro 1359 new parameters indices}[1]     1
    [Template]      Check if default number is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1359 parameter limit print string}[${index}]

Macro 1359 Parameter Names
    [Tags]      1359    English
    [Setup]     Setup New Parameters     1359        ${Macro 1359 affected parameter indices}        1
    [Template]  Check if parameter name is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1359 parameter name changes}[${index}]
    
#===========================================================================================================
Macro 1360 Name
    [Tags]      1360    Common
    Macro Name For Macro 1360 Should Be ${Macro 1360 name}

Macro 1360 Common Parameters
    [Tags]      1360    Common
    ${target param list} =      Filter Parameter List   1360    ${Macro 1360 new parameters indices}
    ${reference param list} =   Filter Parameter List   1356    ${Macro 1360 old parameters indices}
    Matching Parameter count should be equal    ${target param list}    ${reference param list}
    :FOR      ${div}    IN RANGE    len(${target param list})
    \      Loop Through Parameter Division List       @{target param list}[${div}]    @{reference param list}[${div}]

Macro 1360 Struct Parameters
    [Tags]      1360    Common
    ${parameter list} =        Get Struct Parameters Of Macro       1360
    :FOR      ${div}    IN RANGE    len(${parameter list})
    \      Loop Through Struct Division List       @{parameter list}[${div}]

Macro 1360 New Parameter Names
    [Tags]      1360    Common
    [Setup]             Setup New Parameters     1360   @{Macro 1360 new parameters indices}[1]     1
    [Template]      Check if parameter name is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1360 parameter name}[${index}]

Macro 1360 New Parameter Limit Print String
    [Tags]      1360    Common
    [Setup]             Setup New Parameters     1360   @{Macro 1360 new parameters indices}[1]     1
    [Template]      Check if limit print string is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1360 parameter limit print string}[${index}]

Macro 1360 New Parameter Input Form
    [Tags]      1360    Common
    [Setup]             Setup New Parameters     1360   @{Macro 1360 new parameters indices}[1]     1
    [Template]      Check if input form is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1360 parameter input form}[${index}]

Macro 1360 New Parameter Type
    [Tags]      1360    Common
    [Setup]             Setup New Parameters     1360   @{Macro 1360 new parameters indices}[1]     1
    [Template]      Check if parameter type is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1360 parameter type}[${index}]

Macro 1360 New Parameter Default Number
    [Tags]      1360    Common
    [Setup]             Setup New Parameters     1360   @{Macro 1360 new parameters indices}[1]     1
    [Template]      Check if default number is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1360 parameter limit print string}[${index}]

#===========================================================================================================
Macro 1361 Name
    [Tags]      1361    Common
    Macro Name For Macro 1361 Should Be ${Macro 1361 name}

Macro 1361 Common Parameters
    [Tags]      1361    Common
    ${target param list} =      Filter Parameter List   1361    ${Macro 1361 new parameters indices}
    ${reference param list} =   Filter Parameter List   1357    ${Macro 1361 old parameters indices}
    Matching Parameter count should be equal    ${target param list}    ${reference param list}
    :FOR      ${div}    IN RANGE    len(${target param list})
    \      Loop Through Parameter Division List       @{target param list}[${div}]    @{reference param list}[${div}]

Macro 1361 Struct Parameters
    [Tags]      1361    Common
    ${parameter list} =        Get Struct Parameters Of Macro       1361
    :FOR      ${div}    IN RANGE    len(${parameter list})
    \      Loop Through Struct Division List       @{parameter list}[${div}]

Macro 1361 New Parameter Names
    [Tags]      1361    Common
    [Setup]             Setup New Parameters     1361   @{Macro 1361 new parameters indices}[1]     1
    [Template]      Check if parameter name is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1361 parameter name}[${index}]

Macro 1361 New Parameter Limit Print String
    [Tags]      1361    Common
    [Setup]             Setup New Parameters     1361   @{Macro 1361 new parameters indices}[1]     1
    [Template]      Check if limit print string is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1361 parameter limit print string}[${index}]

Macro 1361 New Parameter Input Form
    [Tags]      1361    Common
    [Setup]             Setup New Parameters     1361   @{Macro 1361 new parameters indices}[1]     1
    [Template]      Check if input form is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1361 parameter input form}[${index}]

Macro 1361 New Parameter Type
    [Tags]      1361    Common
    [Setup]             Setup New Parameters     1361   @{Macro 1361 new parameters indices}[1]     1
    [Template]      Check if parameter type is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1361 parameter type}[${index}]

Macro 1361 New Parameter Default Number
    [Tags]      1361    Common
    [Setup]             Setup New Parameters     1361   @{Macro 1361 new parameters indices}[1]     1
    [Template]      Check if default number is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1361 parameter limit print string}[${index}]

#===========================================================================================================
Macro 1362 Name
    [Tags]      1362    Common
    Macro Name For Macro 1362 Should Be ${Macro 1362 name}

Macro 1362 Common Parameters
    [Tags]      1362    Common
    ${target param list} =      Filter Parameter List   1362    ${Macro 1362 new parameters indices}
    ${reference param list} =   Filter Parameter List   1358    ${Macro 1362 old parameters indices}
    Matching Parameter count should be equal    ${target param list}    ${reference param list}
    :FOR      ${div}    IN RANGE    len(${target param list})
    \      Loop Through Parameter Division List       @{target param list}[${div}]    @{reference param list}[${div}]

Macro 1362 Struct Parameters
    [Tags]      1362    Common
    ${parameter list} =        Get Struct Parameters Of Macro       1362
    :FOR      ${div}    IN RANGE    len(${parameter list})
    \      Loop Through Struct Division List       @{parameter list}[${div}]

Macro 1362 New Parameter Names
    [Tags]      1362    Common
    [Setup]             Setup New Parameters     1362   @{Macro 1362 new parameters indices}[1]     1
    [Template]      Check if parameter name is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1362 parameter name}[${index}]

Macro 1362 New Parameter Limit Print String
    [Tags]      1362    Common
    [Setup]             Setup New Parameters     1362   @{Macro 1362 new parameters indices}[1]     1
    [Template]      Check if limit print string is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1362 parameter limit print string}[${index}]

Macro 1362 New Parameter Input Form
    [Tags]      1362    Common
    [Setup]             Setup New Parameters     1362   @{Macro 1362 new parameters indices}[1]     1
    [Template]      Check if input form is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1362 parameter input form}[${index}]

Macro 1362 New Parameter Type
    [Tags]      1362    Common
    [Setup]             Setup New Parameters     1362   @{Macro 1362 new parameters indices}[1]     1
    [Template]      Check if parameter type is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1362 parameter type}[${index}]

Macro 1362 New Parameter Default Number
    [Tags]      1362    Common
    [Setup]             Setup New Parameters     1362   @{Macro 1362 new parameters indices}[1]     1
    [Template]      Check if default number is correct
    : FOR    ${index}    IN RANGE    len(${parameter list})
    \    @{parameter list}[${index}]         @{Macro 1362 parameter limit print string}[${index}]
#Macro 2389
#    Check if parameter count matches reference macro count   1247    1240    ${Macro 1247 new parameters indices}
#    @{div1} =     create list   1     2       3       4       5       6       7 
#    @{div2} =     create list   8     9       10      11 
#    @{list} =     create list       ${div1}      ${div2}
#    @{in_div1} =        create list         1
#    @{in_div2} =        create list         2
#    @{indices} =  create list       ${in_div1}    ${in_div2}
#    ${output} =  Remove Indices   ${list}        ${indices}
    

#API 1020
#    Check if combo box string is correct    1036    3    ${Macro 1020 combo index 3 string}
#
#API 1336
#    [Template]      Check if parameter name is correct
#    : FOR    ${index}    IN RANGE    len(@{Macro 1336 affected parameter numbers})
#    \   @{Macro 1336 affected parameter numbers}[${index}]         @{Macro 1336 parameter name changes}[${index}]
#
#API 1337
#    [Template]      Check if parameter name is correct
#    : FOR    ${index}    IN RANGE    len(@{Macro 1337 affected parameter numbers})
#    \   @{Macro 1337 affected parameter numbers}[${index}]         @{Macro 1337 parameter name changes}[${index}]
#
#API 2391
#    [Tags]      Japanese
#    Check if exit code value is correct     2391    30    ${Macro 2391 30 exit code string}
#    
#API 2392
#    [Tags]      Japanese
#    Check if limit print string is correct   5284       ${Macro 2392 limit print string 1_6}
#    Check if limit print string is correct   5285       ${Macro 2392 limit print string 1_8}
#
#API 2393
#    [Tags]      Japanese
#    Check if exit code value is correct      2393    30     ${Macro 2393 30 exit code string}
#    Check if limit print string is correct   5284    ${Macro 2393 limit print string 1_6}
#    Check if limit print string is correct   5285    ${Macro 2393 limit print string 1_8}
#
#API 3040
#    Check if combo box string is correct    3005    2   ${Macro 3040 combo index 2 string}
#    Check if combo box string is correct    3005    3   ${Macro 3040 combo index 3 string}
#    Check if combo box string is correct    3005    5   ${Macro 3040 combo index 5 string}

#Check connect to databse
#    [Tags]      test
#    Connect To Database Using Custom Params    sqlite3    database="./cp_combo_name.db"

