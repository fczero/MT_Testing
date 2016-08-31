# -*- coding: utf-8 -*-

#from db_helper import *
import db_tables
import db_helper
import sys

def compareMacros(target, reference, newIndices):
    """ given target, reference macro numbers and list of new indices
        loops through equivalent parameters
        returns list of tuple of parameters with differences and corresponding indices
        [ ['parameter name',[difflist]] ,['parameter name2',[difflist2]] ]
        [ ['Number of Message data',['limit_print_string', 'default_number']] ,['parameter name2',[difflist2]] ]
        or
        [ div1, div2 ]
        div1 = ['Number of Message data',['limit_print_string', 'default_number']]
        div2 = ['mail notif parameter..',['limit_print_string', 'default_number']]
    """
    #remove new indices first
    #create copies of lists
    filtered_target    = target[:][:]
    filtered_reference = reference[:][:]
    retVal             = []

    #per div
    for i in range(len(reference)):
        if i > 0 :
        #since mail notification is never the same it should be filtered as well
            if len(newIndices[i]):
                filtered_target[i]    = removeIndices(target[i], newIndices[i])
                filtered_reference[i] = removeIndices(reference[i], newIndices[i])
        else:
            filtered_target[i] = removeIndices(target[i], newIndices[i])

    #per div
    for i in range(len(filtered_reference)):
        div = []
#        print "--i = ",i
    #per param
        for j in range(len(filtered_reference[i])):
            diffInfo = []
            diffList = compareParams(filtered_target[i][j], filtered_reference[i][j])
            if diffList:
                parameter_name = filtered_target[i][j][3]
                for k in diffList:
                    diffInfo.append(db_tables.CP_PARA_NAME[k])
                div.append([parameter_name, diffInfo])
        retVal.append(div)
    return retVal


def compareParams(target, reference):
    """ given a target and reference tuple, compares each value 
        returns list of Indices that are not equal
    """
    indexList = []
    for i in range(1, len(reference)):
        if target[i] != reference[i]:
            #ignore Struct Key as it is often different
            if 1:
                if i == db_tables.CP_PARA_NAME.index('Struct_key'):
                    pass
                else:
                    indexList.append(i)
            else:
                indexList.append(i)
                print target[i],
                print " != ",
                print reference[i]
    return indexList

def removeIndices(newMacro, newIndices):
    """ given a list of tuples (parameters) and list of new elements
        returns a copy of the list without the new elements 
    """
    retVal = newMacro[:]
    indices = newIndices[:]
    indices.sort(reverse=True)
    for i in range(len(indices)):
        retVal.pop(indices[i])
    return retVal

#######################################################

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "insufficient arguments:",
        print len(sys.argv) - 1
        print "should be: 2",
        quit(1)
    macro_for_checking = sys.argv[1]
    reference_macro    = sys.argv[2]
#test
    target_info          = getMacroInfo(str(macro_for_checking))
    target_paramsAll     = getParamsAll(target_info)
    target_paramsInfoAll = getParamsInfoAll(target_paramsAll)
    target_paramsInfo    = insertStrParamsAll(target_paramsInfoAll)
    ref_info             = getMacroInfo(str(reference_macro))
    ref_paramsAll        = getParamsAll(ref_info)
    ref_paramsInfoAll    = getParamsInfoAll(ref_paramsAll)
    ref_paramsInfo       = insertStrParamsAll(ref_paramsInfoAll)

    print 'Macro: %s ' % macro_for_checking
    print 'Reference: %s ' % reference_macro

#zero-based indices
    newIndices = [[6,9,12],[0]]
    compareMacros(target_paramsInfo, ref_paramsInfo, newIndices)

