import unittest
from db_helper import *
import db_tables
from compare_macros import *


class TestCompareMacros(unittest.TestCase):


    def setUp(self):
#        self.newIndices = [[6,9,12],[0]]
        self.newIndices      = [[6,9,12,13],[0]]
        self.target_macro    = 2204
        self.reference_macro = 2202
#target macro
        target_info          = getMacroInfo(str(self.target_macro))
        target_paramsAll     = getParamsAll(target_info)
        target_paramsInfoAll = getParamsInfoAll(target_paramsAll)
        self.target          = insertStrParamsAll(target_paramsInfoAll)
#reference macro
        ref_info          = getMacroInfo(str(self.reference_macro))
        ref_paramsAll     = getParamsAll(ref_info)
        ref_paramsInfoAll = getParamsInfoAll(ref_paramsAll)
        self.reference    = insertStrParamsAll(ref_paramsInfoAll)

    def test_remove_indices(self):
        filtered_div1_target = removeIndices(self.target[0], self.newIndices[0]) 
        filtered_div1_ref    = removeIndices(self.reference[0],[10])
        #removed default_number column
        #self.assertEqual(len(filtered_div1_target),19)
        self.assertEqual(len(filtered_div1_target),18)
        for i in range(len(filtered_div1_target)):
            for j in range(1, len(filtered_div1_target[i])):
                if j == 17 or j == 24:
                    pass
                else:
                    self.assertEqual(filtered_div1_target[i][j], filtered_div1_ref[i][j])

    def test_compareParams(self):
        filtered_div1_target = removeIndices(self.target[0], self.newIndices[0]) 
        filtered_div1_ref = removeIndices(self.reference[0],[10])
        for i in range(len(filtered_div1_target)):
            #print filtered_div1_target[i]
            diffList = compareParams(filtered_div1_target[i], filtered_div1_ref[i])
            self.assertListEqual(diffList, [])

    def test_compareMacros(self):
        macro_for_checking   = 2204
        reference_macro      = 2202
        target_info          = getMacroInfo(str(macro_for_checking))
        target_paramsAll     = getParamsAll(target_info)
        target_paramsInfoAll = getParamsInfoAll(target_paramsAll)
        target_paramsInfo    = insertStrParamsAll(target_paramsInfoAll)
        ref_info             = getMacroInfo(str(reference_macro))
        ref_paramsAll        = getParamsAll(ref_info)
        ref_paramsInfoAll    = getParamsInfoAll(ref_paramsAll)
        ref_paramsInfo       = insertStrParamsAll(ref_paramsInfoAll)
        newIndices           = [[6,9,12],[0]]
        retVal               = compareMacros(target_paramsInfo, ref_paramsInfo, newIndices)
        div1 = 0
        div2 = 1
#        print retVal
        self.assertListEqual(retVal[div1], [['Number of Message data', ['default_number']]])
        self.assertListEqual(retVal[div2], [])
        
    def test_get_paramslist(self):
        macro_for_checking   = 1407
        reference_macro      = 1402
        
"""
"""

if __name__ == "__main__":
    unittest.main()
