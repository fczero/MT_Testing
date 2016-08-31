*** Settings ***
Documentation     MT Database related keywords
Library           String
Library           Collections
Library           db_helper
Library           compare_macros
#Library           OperatingSystem
#Library           DatabaseLibrary

*** Keywords ***
Macro Name For Macro ${macro} Should Be ${expected}
    ${actual} =     Get Macro Name  ${macro}
    Should be equal as strings      ${actual}  ${expected} 

Setup New Parameters
    [Documentation]     Setup for new parameter checking, sets a test variable named '${parameter list}'
    [Arguments]         ${macro no}     ${parameter indices}    ${div}=0
    ${parameter list items} =   Get Parameter Numbers From Indices      ${macro no}     ${parameter indices}    ${div}
    Set Test Variable   ${parameter list}   ${parameter list items}

Check if parameter name is correct
    [Arguments]                   ${parameter no}        ${expected}
    Check if parameter attribute is correct     ${parameter no}     ${expected}    parameter

#test
Check if parameter name is correct given index
    [Arguments]                   ${parameter index}        ${expected}       ${div}
    Check if parameter attribute is correct from index    ${parameter index}     ${expected}    parameter
#test

Check if exit code value is correct
    [Arguments]                   ${macro no}        ${exit code value}        ${exit code string}
    ${actual} =                   Get Exit Code Attribute     ${macro no}        ${exit code value} 
    Should be equal as strings    ${actual}    ${exit code string}

Check if default number is correct
    [Arguments]                   ${parameter no}        ${limit print string}
    ${actual} =                   Get Parameter Attribute      ${parameter no}     default_number
    ${expected} =       Get Default Value       ${limit print string}
    Log Parameter Info      ${parameter no}
    Should be equal as integers    ${actual}    ${expected}


Check if limit print string is correct
    [Arguments]                   ${parameter no}        ${expected}
    Check if parameter attribute is correct     ${parameter no}     ${expected}    limit_print_string

Check if input form is correct
    [Arguments]                   ${parameter no}        ${expected}
    ${actual} =                   Get Parameter Attribute      ${parameter no}     parameter_input_form
    ${actual text} =    Get Table Value     INPUT_FORM        ${actual}
    ${expected text} =  Get Table Value     INPUT_FORM        ${expected}
    Log Parameter Info      ${parameter no}
    Log Many    ${actual text}      ${expected text}
    Should be equal as integers    ${actual}    ${expected}

Check if parameter type is correct
    [Arguments]                   ${parameter no}        ${expected}
    ${actual} =                   Get Parameter Attribute      ${parameter no}     parameter_type
    ${actual text} =    Get Table Value     DATA_TYPES        ${actual}
    ${expected text} =  Get Table Value     DATA_TYPES        ${expected}
    Log Parameter Info      ${parameter no}
    Log Many    ${actual text}      ${expected text}
    Should be equal as integers    ${actual}    ${expected}

Check if parameter attribute is correct
    [Arguments]                   ${parameter no}        ${expected}    ${attribute}
    ${actual} =                   Get Parameter Attribute      ${parameter no}     ${attribute}
    Log Parameter Info      ${parameter no}
    Should be equal as strings    ${actual}    ${expected}

#test
Check if parameter attribute is correct from index
    [Arguments]                   ${parameter index}        ${expected}    ${attribute}
    ${actual} =                   Get Parameter Attribute      ${parameter no}     ${attribute}
    Log Parameter Info      ${parameter no}
    Should be equal as strings    ${actual}    ${expected}
#test

Check if combo box string is correct
    [Arguments]                   ${parameter no}        ${combo index}       ${combo string}
    ${actual} =                   Get Combo Box Value Attribute    ${parameter no}   ${combo index}    parameter_price_name
    Log Parameter Info      ${parameter no}
    Should be equal as strings    ${actual}    ${combo string}

Check MT version info
    [Arguments]                   ${MT target}             ${RAT}
    ${MT actual} =                Get MT Version           ${RAT} 
    Should be equal as strings    ${MT actual}       ${MT target}

Check SNR version info
    [Arguments]                   ${SNR target}      ${RAT}
    ${SNR actual} =               Get Scenario Version     ${RAT} 
    Should be equal as strings    ${SNR actual}      ${SNR target}

Check if new parameter type is correct
    [Arguments]                    ${macro number}    ${parameter name}    ${parameter type}    ${div}=0
    ${parameter no} =              Get Parameter Number From Name    ${macro number}    ${parameter name}    ${div}
    ${actual} =                    Get Parameter Attribute      ${parameter no}     parameter_type
    Should be equal as integers    ${actual}    ${parameter type}

Check if new parameter counts are correct 
    [Arguments]                    ${macro number}    ${parameter name}    ${div}=0
    ${parameter no} =              Get Parameter Number From Name    ${macro number}    ${parameter name}    ${div}
    ${actual ascii} =              Get Parameter Attribute      ${parameter no}     ascii_parameter_count
    ${actual hex} =                Get Parameter Attribute      ${parameter no}     hex_parameter_count
    Should be equal as integers    ${actual}    ${parameter type}

Check if parameter count matches reference macro count
#split this into two separate keywords that return the filtered parameter list
    [Documentation]                               Checks new macro against reference macro without the new parameters.
    ...                                           Format of new parameters should be [ [div1 parameters], [div2 parameters], ...]
#    [Arguments]                                   ${target macro}        ${reference macro}    ${new indices}    ${reference indices}=${EMPTY}
#try to run the default argument without any assignment
    [Arguments]                                   ${target macro}        ${reference macro}    ${new indices}    ${reference indices}=
    ${target macro parameters} =                  Get Parameters of Macro   ${target macro}
    ${reference macro parameters} =               Get Parameters of Macro   ${reference macro}
    @{common target macro parameters} =           Remove Indices    ${target macro parameters}    ${new indices}
    ${reference indices length} =   Get Length    ${reference indices}
    @{common reference macro parameters} =        Run Keyword If
    ...    ${reference indices length} == 0       Input without reference indices     ${reference macro parameters}
    ...    ELSE                                   Input with reference indices        ${reference macro parameters}   ${reference indices}
    Matching parameter count should be equal      @{common target macro parameters}     @{common reference macro parameters}



##refactor
#    @{common target param attributes} =    Create List
#    :FOR    ${key}   IN RANGE      len(${common target macro parameters})
#    \       @{attribute list} =    Get Parameter Attribute List     @{common target macro parameters}[${key}]
#    \       Append To List    ${common target param attributes}     @{attribute list}
#
#
##refactor
#Get Parameter Attribute List
#    [Documentation]     Given a parameter key number, returns the list of parameter attributes
#    [Arguments]    ${key number}
#    ${upper limit} =    Get Parameter Column Count 
#    ${return value} =   Create List
#    :FOR    ${index}    IN  RANGE     ${upper limit}
#    \      ${attribute} =     Get Parameter Attribute From Index   ${key number}   ${index}
#    \      Append To List    ${return value}       ${attribute}
#    [Return]              ${return value}

Loop Through Struct Division List
    [Documentation]    Given struct parameter list in [param1, param2,...] format, verify info
    [Arguments]        ${struct parameter list}
    ${loop limit} =    Get Length    ${struct parameter list} 
    :FOR               ${index}        IN RANGE      ${loop limit} 
    \                  ${parameter} =     Set Variable   @{struct parameter list}[${index}]
    \                  ${struct key} =    Get Struct Key From Parameter   ${parameter}
#add checking of ascii count should be < 24000
    \                  Run Keyword And Continue On Failure     Check If Ascii Count Is Valid    ${parameter}
    \                  Run Keyword And Continue On Failure     Check Parameter Hex Count    ${parameter}
    \                  Run Keyword And Continue On Failure     Check Input Size         ${parameter}
    \                  Run Keyword And Continue On Failure     Check Display Size         ${parameter}
    \                  Run Keyword And Continue On Failure     Check Struct Parameter Count        ${struct key}
    \                  Run Keyword And Continue On Failure     Check Struct Hex Size        ${struct key}
    \                  Run Keyword And Continue On Failure     Check Struct Ascii Size        ${struct key}

Check If Ascii Count Is Valid
    [Documentation]            Given a parameter that is a struct, check if the ascii parameter count does not exceed the MT limit
    [Arguments]                ${parameter}
    ${listed parameter ascii count} =    Get Ascii Parameter Count     ${parameter}   
    Log Parameter Info      ${parameter}
    Should Be True      ${listed parameter ascii count} < 240000

Check Input Size
    [Documentation]            Given a parameter that is a struct, check if the input size corresponds to the hex parameter count
    [Arguments]                ${parameter}
    ${struct key} =            Get Struct Key From Parameter    ${parameter}
    ${struct hex count} =       Get Total Hex Parameter Count     ${struct key}   
    ${listed input size} =         Get Parameter Input Size    ${parameter}
    ${expected input size} =     Evaluate   ${struct hex count} / 2       
    Log Parameter Info      ${parameter}
    Should Be Equal     ${listed input size}    ${expected input size}

Check Display Size
    [Documentation]            Given a parameter that is a struct, check if the display size corresponds to the hex parameter count
    [Arguments]                ${parameter}
    ${struct key} =            Get Struct Key From Parameter    ${parameter}
    ${struct hex count} =       Get Total Hex Parameter Count     ${struct key}   
    ${listed display size} =         Get Parameter Display Size    ${parameter}
    ${expected display size} =     Evaluate   ${struct hex count} / 2       
    Log Parameter Info      ${parameter}
    Should Be Equal     ${listed display size}    ${expected display size}

Check Parameter Hex Count
    [Documentation]            Given a parameter that is a struct, check if the hex parameter count matches the struct total hex parameter count
    [Arguments]                ${parameter}
    ${struct key} =            Get Struct Key From Parameter    ${parameter}
    ${listed parameter hex count} =    Get Hex Parameter Count     ${parameter}   
    ${struct hex count} =       Get Total Hex Parameter Count     ${struct key}   
    ${repeat flag} =       Get Parameter Repeat Flag        ${parameter}
    ${repeat count} =    Run Keyword If  ${repeat flag}     Get Parameter Repeat Count        ${parameter}
    ...                  ELSE       Evaluate        1
    ${expected hex count} =    Evaluate    ${struct hex count} * ${repeat count}
    Log Parameter Info      ${parameter}
    Should Be Equal         ${listed parameter hex count}      ${expected hex count}

Check Parameter Ascii Count
    [Documentation]            Given a parameter that is a struct, check if the ascii parameter count matches the struct total ascii parameter count
    [Arguments]                ${parameter}
    ${struct key} =            Get Struct Key From Parameter    ${parameter}
    ${listed parameter ascii count} =    Get Ascii Parameter Count     ${parameter}   
    ${struct ascii count} =       Get Total Ascii Parameter Count     ${struct key}   
    ${repeat flag} =       Get Parameter Repeat Flag        ${parameter}
    ${repeat count} =    Run Keyword If  ${repeat flag}     Get Parameter Repeat Count        ${parameter}
    ...                  ELSE       Evaluate        1
    ${expected ascii count} =    Evaluate    ${struct ascii count} * ${repeat count}
    Log Parameter Info      ${parameter}
    Should Be Equal         ${listed parameter ascii count}      ${expected ascii count}

Log Struct Info
    [Documentation]     Given a struct key, logs relevant info for that struct key
    [Arguments]         ${struct key}
    ${struct name} =    Get Struct Name From Key        ${struct key}
    Log Many            ${struct key}           ${struct name}

Log Parameter Info
    [Documentation]     Given a parameter key, logs relevant info for that parameter key
    [Arguments]         ${parameter key}
    ${parameter name} =    Get Parameter Name From Key        ${parameter key}
    Log Many            ${parameter key}           ${parameter name}

Check Struct Hex Size
    [Documentation]                   Given struct key, check if hex size matches the total hex size of parameters
    [Arguments]                       ${struct key}
    ${total hex size} =               Get Total Hex Parameter Count       ${struct key}
    ${parameters total hex size} =    Get Total Hex Size          ${struct key}
    Log Struct Info                   ${struct key}
    Should Be Equal                   ${total hex size}     ${parameters total hex size}

Check Struct Ascii Size
    [Documentation]                     Given struct key, check if ascii size matches the total ascii size of parameters
    [Arguments]                         ${struct key}
    ${total ascii size} =               Get Total Ascii Parameter Count       ${struct key}
    ${parameters total ascii size} =    Get Total Ascii Size   ${struct key}
    Log Struct Info                     ${struct key}
    Should Be Equal                     ${total ascii size}     ${parameters total ascii size}

Check Struct Parameter Count
    [Documentation]    Given struct key, check if listed parameters matches the parameter count
    [Arguments]         ${struct key}
    ${parameter count} =   Get Struct Attribute     ${struct key}       parameter_count 
    ${parameter list} =  Get Parameters Of Struct       ${struct key}
    ${parameter list size} =    Get Length    ${parameter list}
    Log Struct Info     ${struct key}
    Should Be Equal    ${parameter count}     ${parameter list size}

Get Total Hex Size
    [Documentation]    Given struct key, returns sum of hex size of all of its parameters
    [Arguments]         ${struct key}
    ${parameters} =      Get Parameters Of Struct     ${struct key}
    ${hex running total} =      Set Variable    0
    :FOR    ${index}    IN RANGE   len(${parameters}) 
    \      ${parameter} =   Set Variable   @{parameters}[${index}]
    \      ${hex size} =    Get Hex Parameter Count     ${parameter}
    \      ${hex running total} =       evaluate    ${hex running total} + ${hex size}
    [Return]    ${hex running total}

Get Total Ascii Size
    [Documentation]    Given struct key, returns sum of ascii size of all of its parameters
    [Arguments]         ${struct key}
    ${parameters} =      Get Parameters Of Struct     ${struct key}
    ${ascii running total} =      Set Variable    0
    :FOR    ${index}    IN RANGE   len(${parameters}) 
    \      ${parameter} =   Set Variable   @{parameters}[${index}]
    \      ${ascii size} =    Get Ascii Parameter Count     ${parameter}
    \      ${ascii running total} =       evaluate    ${ascii running total} + ${ascii size}
    [Return]    ${ascii running total}


Loop Through Parameter Division List
    [Documentation]    Given two parameter lists in [param1, param2,...] format, compare each element 
    [Arguments]           ${target parameter list}    ${reference parameter list} 
    ${loop limit} =        Get Length    ${target parameter list} 
    :FOR     ${index}        IN RANGE      ${loop limit} 
    \        Compare Parameters     @{target parameter list}[${index}]      @{reference parameter list}[${index}]

Compare Parameters
    [Documentation]    Given two parameters, compare each element's attributes
    [Arguments]           ${target parameter}    ${reference parameter} 
    ${loop limit} =         Get Parameter Column Count
    :FOR     ${index}        IN RANGE      ${loop limit} 
    \      ${member result} =      evaluate    ${index} in ${Skipped Columns List}
    \      Continue For Loop If    ${member result} 
    \      ${target} =     Get Parameter Attribute From Index      ${target parameter}      ${index}
    \      ${reference} =     Get Parameter Attribute From Index      ${reference parameter}      ${index}
    \      ${parameter name}=   Get Parameter Name From Key     ${target parameter}
    \      ${parameter column} =    Get Parameter Column Name   ${index}
    \      Log Many      ${parameter name}  ${parameter column}
    \      Run Keyword and continue on failure   Should Be Equal     ${target}       ${reference}

Filter Parameter List
    [Documentation]    Given a parameter list in [ [div1], [div2], ... ] format and an index list, removes the indices from the list 
    [Arguments]           ${macro number}    ${index list}= 
    ${parameter list} =   Get Parameters of Macro   ${macro number}
    ${index list length} =  Get Length  ${index list}
    @{return value} =     Run Keyword If
#    ...    ${index list length} == 0    Input without reference indices     ${parameter list}
    ...    ${index list length} == 0    Evaluate    ${parameter list}
    ...    ELSE                         Input with reference indices        ${parameter list}   ${index list}
    [Return]      ${return value}

Get Struct Parameters
    [Documentation]    Given a parameter list in [ [div1], [div2], ... ] format,
    ...                return list of struct parameters 
    [Arguments]           ${macro number}    ${index list}= 

Matching parameter count should be equal
    [Arguments]                     ${target parameter list}    ${reference parameter list}
    ${reference} =                  Get Length    ${reference parameter list}
    ${target} =                     Get Length    ${target parameter list}
    Should be equal as integers     ${target}    ${reference}

Input with reference indices
    [Documentation]       Used only for conditional keyword execution based on given indices
    [Arguments]           ${parameters}           ${indices}
    ${return value} =     Remove Indices    ${parameters}       ${indices}
    [Return]              ${return value}

Input without reference indices
    [Documentation]     Used only for conditional keyword execution based on given indices
    [Arguments]         ${parameters}
    [Return]            ${parameters}
     
Remove Indices
    [Documentation]                Removes indices within the list
    [Arguments]                    ${parameter list}       ${indices}
    ${parameter length} =          Get Length    ${parameter list}
    ${indices length} =            Get Length     ${indices}
    Should be equal as integers    ${parameter length}       ${indices length} 
    ${return value} =              Create List
    :FOR   ${i}                    IN RANGE    ${parameter length}
    \                              @{div} =     Remove Indices Per Div   @{parameter list}[${i}]     @{indices}[${i}]
    \                              Append To List    ${return value}       ${div}
    [Return]                       @{return value}

Remove Indices Per Div
    [Documentation]             To be executed as nested for loop for removing indices
    [Arguments]                 ${parameter list}       ${indices}
    ${indices length} =         Get Length   ${indices}
    :FOR                        ${j}   IN RANGE     ${indices length}
    \   ${last element} =       evaluate    ${indices length} - (${j} + 1)
    \   ${popped element} =     Remove From List   ${parameter list}   @{indices}[${last element}]
    [Return]                    @{parameter list}

