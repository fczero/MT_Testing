# -*- coding: utf-8 -*-

# class implementation
import sqlite3
import db_tables
import sys
import re
import os

PARAM_COUNT       = db_tables.CP_MACRO_NAME.index('parameter_count')
STRUCT_KEY        = db_tables.CP_PARA_NAME.index('Struct_key')
STR_PARAM_COUNT   = 4
DB_MACRO_NAME_COL = len(db_tables.CP_MACRO_NAME)
NAME              = 0


class MTLibrary:


    def __init__(self, path='.'):
        self.DB_PATH       = path
        self.CP_PARA_NAME  = os.path.join(self.DB_PATH, 'cp_para_name.db')
        self.VER_INFO      = os.path.join(self.DB_PATH, 'VER_INFO.db')
        self.VER_INFO_3G   = os.path.join(self.DB_PATH, '3G_VER_INFO.db')
        self.CP_COMBO_NAME = os.path.join(self.DB_PATH, 'cp_combo_name.db')
        self.CP_END_NAME   = os.path.join(self.DB_PATH, 'cp_end_name.db')
        self.CP_MACRO_NAME = os.path.join(self.DB_PATH, 'cp_macro_name.db')
        self.CP_STR_PTR    = os.path.join(self.DB_PATH, 'cp_str_ptr.db')
        
    def Get_Default_Value(self, limit_print_string):
        """ given a limit print string, returns the default value based on first number
        """
        m = re.match("\D*(\d*)", limit_print_string)
        return m.group(1)
    
    def Get_Table_Value(self, table_name, index):
        table_name = 'db_tables.' + table_name
        table = eval(table_name)
        return (table[int(index)])
    
    def Get_Parameter_Numbers_From_Indices(self, macro_no, parameter_indices_list, div=0):
        """given macro number, parameter list, and division returns list of parameter numbers
        """
        retVal = []
        for ctr, index in enumerate(parameter_indices_list):
            parameter_no = self.Get_Parameter_Number_From_Index(macro_no, parameter_indices_list[ctr], div)
            retVal.append(parameter_no)
        return retVal
    
    def Get_Hex_Parameter_Count(self, key_no):
        """given key number returns hex parameter count
        """
        return  Get_Parameter_Attribute(key_no, 'hex_parameter_count')
    
    def Get_Total_Hex_Parameter_Count(self, struct_key):
        """given struct key returns total hex parameter count
        """
        return  Get_Struct_Attribute(struct_key, 'total_hex_parameter_count')
    
    def Get_Ascii_Parameter_Count(self, key_no):
        """given key number returns hex parameter count
        """
        return  Get_Parameter_Attribute(key_no, 'ascii_parameter_count')
    
    def Get_Parameter_Repeat_Count(self, key_no):
        """given key number returns repeat count
        """
        return  Get_Parameter_Attribute(key_no, 'Repeat_count')
    
    def Get_Parameter_Repeat_Flag(self, key_no):
        """given key number returns repeat count
        """
        return  Get_Parameter_Attribute(key_no, 'Repeat_flg')
    
    def Get_Parameter_Input_Size(self, key_no):
        """given key number returns input size
        """
        return  Get_Parameter_Attribute(key_no, 'input_size')
    
    def Get_Parameter_Display_Size(self, key_no):
        """given key number returns display size
        """
        return  Get_Parameter_Attribute(key_no, 'display_size')
    
    def Get_Total_Ascii_Parameter_Count(self, struct_key):
        """given struct key returns total ascii parameter count
        """
        return  Get_Struct_Attribute(struct_key, 'total_ascii_parameter_cou')
    
    def Get_Non_Struct_Parameters_Of_Struct(self, struct_key):
        parameters          = self.Get_Parameters_Of_Struct(struct_key)
        str_only_parameters = self.Get_Struct_Parameters_Of_Struct(struct_key)
        for  parameter in str_only_parameters:
            if parameter in parameters:
                parameters.remove(parameter)
        return parameters
    
    def Get_Struct_Parameters_Of_Struct(self, struct_key):
        parameter_list = self.Get_Parameters_Of_Struct(struct_key)
        retVal         = []
        for parameter in parameter_list:
            if self.Get_Parameter_Attribute(parameter, 'Struct_key'):
                retVal.append(parameter)
        return retVal
    
    def Get_Parameters_Of_Struct(self, struct_key):
        """ given struct key, returns list of parameters
        """
        struct_info     = self.getStrPtrInfo(struct_key)
        parameter_count = int(struct_info[db_tables.CP_STR_PTR.index('parameter_count')])
        lower_limit     = int(self.Get_Struct_Parameter_Index_Start())
        upper_limit     = lower_limit + parameter_count
        parameter_list  = struct_info[lower_limit:upper_limit]
        return list(parameter_list)
    
    def Get_Struct_Parameter_Index_Start(self):
        return  db_tables.CP_STR_PTR.index('parameter_key_list1')
    
    def Get_Struct_Parameters_Of_Macro(self, macro_number):
        """ given macro number, returns a list of struct parameters 
            format: [[div1 parameters], [div2 parameters], ...]
        """
        params_list =  self.Get_Parameters_Of_Macro(macro_number)
        retVal = []
        for div, paramList in enumerate(params_list):
            divList = []
            for param in paramList:
                if self.Get_Parameter_Attribute(param, 'Struct_key'):
                    divList.append(param)
            retVal.append(divList)
        return retVal
    
    def Get_Struct_Key_From_Parameter(self, key_no):
        return  self.Get_Parameter_Attribute(key_no, 'Struct_key')
    
    def Get_Parameter_Name_From_Key(self, key_no):
        return  self.Get_Parameter_Attribute(key_no, 'parameter')
    
    def Get_Struct_Name_From_Key(self, struct_key):
        return  self.Get_Struct_Attribute(struct_key, 'struct_name')
    
    def Get_Struct_Ptr_Column_Count(self):
        return len(db_tables.CP_STR_PTR)
    
    def Get_Parameter_Column_Count(self):
        return len(db_tables.CP_PARA_NAME)
    
    def Get_Parameter_Column_Name(self, columnIndex):
        return  db_tables.CP_PARA_NAME[columnIndex]
    
    def Get_Macro_Name(self, macro):
        """ given macro number, return the macro name as string
        """
        return self.Get_Macro_Attribute(macro, 'macro_name')
    
    def Get_Macro_Attribute(self, macro, column, div=0):
        """ given parameter number and column name, returns value as string """
        info = self.getMacroInfo(str(macro))
        col = int(db_tables.CP_MACRO_NAME.index(column))
        return (info[div][col])
    
    def Get_Parameter_Info_From_Index(self, macro, index, div=0):
        """ given macro, index, and division;
            return tuple of parameter info for that index.
        """
        info                 = self.getMacroInfo(str(macro))
        paramsAll            = self.getParamsAll(info)
        paramsInfoAll        = self.getParamsInfoAll(paramsAll)
        paramsInfoWithStrAll = self.insertStrParamsAll(paramsInfoAll)
        param_index          = db_tables.CP_PARA_NAME.index('key_no')
        matches              = [param for ctr, param in enumerate(paramsInfoWithStrAll[div])\
                               if ctr == index]
        return matches[0]
    
    def Get_Parameter_Number_From_Index(self, macro, index, div=0):
        """ given macro, index, and division;
            return tuple of parameter info for that parameter index.
        """
        param_number = db_tables.CP_PARA_NAME.index('key_no')
        paramInfo    = self.Get_Parameter_Info_From_Index(macro,\
                                                    index,\
                                                    int(div))
        retVal       = paramInfo[param_number]
        return retVal
    
    def Get_Parameter_Info_From_Name(self, macro, parameter_name, div=0):
        """ given macro, parameter name, and division;
            return tuple of parameter info for that parameter name.
            First match only
        """
        info                 = self.getMacroInfo(str(macro))
        paramsAll            = self.getParamsAll(info)
        paramsInfoAll        = self.getParamsInfoAll(paramsAll)
        paramsInfoWithStrAll = self.insertStrParamsAll(paramsInfoAll)
        param_index          = db_tables.CP_PARA_NAME.index('parameter')
        matches              = [param for param in paramsInfoWithStrAll[div] \
                               if param[param_index] == parameter_name]
        if matches:
            retVal = matches[0]
        else:
            retVal = ()
        return retVal
    
    def Get_Parameter_Number_From_Name(self, macro, parameter_name, div=0):
        """ given macro, parameter name, and division;
            return parameter number.
            First match only
        """
        param_number = db_tables.CP_PARA_NAME.index('key_no')
        paramInfo    = self.Get_Parameter_Info_From_Name(macro,\
                                                    parameter_name,\
                                                    int(div))
        retVal       = paramInfo[param_number]
        return retVal
    
    def Get_Last_Row_From_Table(self, db_name, table_name, column):
        """ given database name and column, returns last row from that table """
        db    = sqlite3.connect(db_name)
        c     = db.cursor()
        query = "select * from {table} where {col} = \
            (SELECT MAX({col}) FROM {table})".format(table=table_name, col=column)
        c.execute(query)
        info  = c.fetchone()
#        print 'Last Entry:', info
        return info
    
    def getVerDbFromRat(self, RAT_type):
        """ given RAT type returns the file name of the version database """
        if RAT_type == 'LTE':
            db_name = self.VER_INFO
        else:
            db_name = self.VER_INFO_3G
        return db_name
    
    def Get_MT_Version(self, RAT_type):
        """ returns MTVER info from last version info row in database based on RAT type """
        db_name = self.getVerDbFromRat(RAT_type)
        info = self.Get_Last_Row_From_Table(db_name, 'VER_INFO', 'NO')
        return info[db_tables.VER_INFO.index('MTVER')]
    
    def Get_Scenario_Version(self, RAT_type):
        """ returns VER info from last version info row  in database based on RAT type """
        db_name = self.getVerDbFromRat(RAT_type)
        info = self.Get_Last_Row_From_Table(db_name, 'VER_INFO', 'NO')
        return info[db_tables.VER_INFO.index('VER')]
    
    def getComboInfo(self, key, db_name=None):
        """ given macro number search combo name db returns the list of tuples of queries """
        db_name = db_name or self.CP_COMBO_NAME
        db = sqlite3.connect(db_name)
        c = db.cursor()
        info = []
        for row in c.execute("select * from {} where macro_no =\
            {}".format('cp_combo_name', key)):
            info.append(row)
        db.close()
        return info
    
    def Get_Combo_Box_Value_Attribute(self, key, comboIndex, column):
        """ given parameter number, combo index,  column name returns value as string 
            index is one-based
        """
        info = self.getComboInfo(key)
        col = int(db_tables.CP_COMBO_NAME.index(column))
        return (info[int(comboIndex)-1][col])

    def Get_Combo_Box_Value_Attribute_Using_Value(self, key, comboValue, column):
        """ given parameter number, comboValue,  column name returns value as string 
            returns parameter price name
        """
        info = self.getComboInfo(key)
        col = int(db_tables.CP_COMBO_NAME.index(column))
        pp_col = int(db_tables.CP_COMBO_NAME.index('parameter_price'))
        for index, line in enumerate(info):
            if int(info[int(index)][pp_col]) == int(comboValue):
                return info[int(index)][col]
    
    def getParaInfo(self, key, db_name=None):
        """ given macro number search para name db returns tuple of queries """
        db_name = db_name or self.CP_PARA_NAME
        db = sqlite3.connect(db_name)
        c = db.cursor()
        c.execute("select * from {} where key_no = {}".format('cp_para_name', key))
        info = c.fetchone()
        db.close()
        return info
    
    def getStrPtrInfo(self, struct_key, db_name=None):
        """ given struct key number search str ptr db, returns tuple of queries """
        db_name = db_name or self.CP_STR_PTR
        db = sqlite3.connect(db_name)
        c = db.cursor()
        c.execute("select * from {} where struct_key = {}".format('cp_str_ptr', struct_key))
        info = c.fetchone()
        db.close()
        return info
    
    def Get_Struct_Attribute(self, struct_key, column):
        """ given parameter number, column name returns value as string """
        info = self.getStrPtrInfo(struct_key)
        col = int(db_tables.CP_STR_PTR.index(column))
        return (info[col])
    
    def Get_Struct_Attribute_From_Index(self, struct_key, columnIndex):
        """ given parameter number, column index returns value as string """
        info = self.getStrPtrInfo(struct_key)
        return (info[columnIndex])
    
    def Get_Parameter_Attribute(self, key, column):
        """ given parameter number, column name returns value as string """
        info = self.getParaInfo(key)
        col = int(db_tables.CP_PARA_NAME.index(column))
        return (info[col])
    
    def Get_Parameter_Attribute_From_Index(self, key, columnIndex):
        """ given parameter number, column index returns value as string """
        info = self.getParaInfo(key)
        return (info[columnIndex])
    
    def getEndInfo(self, key, db_name):
        """ given macro number search end name db returns the list of tuple of queries """
        db = sqlite3.connect(db_name)
        c = db.cursor()
        info = []
        for row in c.execute("select * from {} where macro_no = {}".format('cp_end_name', key)):
            info.append(row)
        db.close()
        return info
    
    def Get_Exit_Code_Attribute(self, key, price):
        """ given macro number, parameter price returns value as string """
        db_name = self.CP_END_NAME
        info = self.getEndInfo(key, db_name)
        for row in info:
#            print row
            if row[db_tables.CP_END_NAME.index('parameter_price')] == float(price):
                return row[db_tables.CP_END_NAME.index('parameter_price_name')]
    
    def getMacroInfo(self, key, db_name=None):
        """ given macro number search macro name db returns the list of tuples of queries """
        db_name = db_name or self.CP_MACRO_NAME
        db = sqlite3.connect(db_name)
        c = db.cursor()
        info = []
        for row in c.execute("select * from {} where macro_no = {}".format('cp_macro_name', key)):
            info.append(row)
        db.close()
        return info
    
    def getNumParams(self, row):
        """ returns int num of parameters """
        return (int(row[PARAM_COUNT]))
    
    def getParamsAll(self, allMacroInfo):
        """ given list of tuples of queries returns list of list of parameters (list per result) """
        return map(self.getParams, allMacroInfo)
    
    def getParams(self, macroInfo):
        """ given tuples of queries returns list of parameters (list per result) """
        retVal = []
        numOfParams = self.getNumParams(macroInfo)
        for index in range(1, numOfParams+1):
            retVal.append(macroInfo[PARAM_COUNT+index])
        return retVal
    
    def getParamsInfoAll(self, allParamsList):
        """ given list within a list of parameters returns list within a list of tuples of parameters from para name db """
        return map(self.getParamsInfo, allParamsList)
    
    def getParamsInfo(self, paramsList, db_name=None):
        """ given list of parameters
            returns list of tuples of parameters from para name db
        """
        db_name = db_name or self.CP_PARA_NAME
        db = sqlite3.connect(db_name)
        c = db.cursor()
        retVal = []
        for param in paramsList:
    #refactor for unicode support
            c.execute("select * from {} where key_no = {}".format(\
                'cp_para_name', str(param)))
            info = c.fetchone()
            retVal.append(info)
        db.close()
        return retVal
    
    def insertStrParamsAll(self, allParamsInfo):
        """ given list within a list of tuples of parameters
            returns list within a list of tuples of parameters with struct parameters
            inserted after each struct
        """
        return map(self.insertStrParams, allParamsInfo)
    
    
    def insertStrParams(self, paramsInfo):
        """ given list of tuples of parameters
            returns list of tuples of parameters with struct parameters
            inserted after each struct
        """
        retVal = []
    #refactor to pythonic way; enumerate
        ctr = 0
        for param in paramsInfo[:]:
            #print param
            retVal.append(param)
            if param[STRUCT_KEY]:
                #print "---STRUCT"
                structParams = self.getStrParams(param[STRUCT_KEY])
                insertData = self.getParamsInfo(structParams)
                insertData = self.insertStrParams(insertData)
                for data in insertData:
                    #print data
                    retVal.append(data)
                #print "---End of STRUCT"
            ctr += 1
    
        for data in paramsInfo:
            pass
            #print data
        return retVal
    
    def getStrParams(self, key, db_name=None):
        """ given struct key 
            returns list of parameters
        """
        db_name = db_name or self.CP_STR_PTR
        db = sqlite3.connect(db_name)
        c = db.cursor()
        c.execute("select * from {} where struct_key = {}".format('cp_str_ptr', key))
        info = c.fetchone()
        db.close()
        retVal = []
        paramCount = info[STR_PARAM_COUNT]
        ctr = 0
        for value in info[STR_PARAM_COUNT+2:]:
            if value != 0.0:
                ctr += 1
                retVal.append(value)
        return retVal
        
    def getStrParamCount(self, key, db_name=None):
        """ given struct key 
            returns integer count of parameters
        """
        db_name = db_name or self.CP_STR_PTR
        db = sqlite3.connect(db_name)
        c = db.cursor()
        c.execute("select * from {} where struct_key = {}".format('cp_str_ptr', key))
        info = c.fetchone()
        db.close()
        if info:
            return int(info[STR_PARAM_COUNT])
        else:
            return 0
        
    def table_columns(self, db_name):
        db = sqlite3.connect(db_name)
        c = db.cursor()
        c.execute("select * from {}".format(db_name[:-3]))
        for i,v in enumerate(c.description):
            print i, v[0]
        db.close()
    
    def Get_Parameters_Of_Macro(self, macro_number):
        """ given macro number, return the list of list of parameters
            format: [[div1 parameters], [div2 parameters], ...]
        """
        retVal = []
        info = self.getMacroInfo(str(macro_number))
        paramsAll = self.getParamsAll(info)
        paramsInfoAll = self.getParamsInfoAll(paramsAll)
        paramsInfoWithStrAll = self.insertStrParamsAll(paramsInfoAll)
        for div, params in enumerate(paramsInfoWithStrAll):
            divParams = []
            for info in params:
                divParams.append(info[db_tables.CP_PARA_NAME.index('key_no')])
            retVal.append(divParams)
        return retVal
    
    def Remove_indices(self, paramsList, indices):
        pass
    
#######################################################
if __name__ == "__main__":
    """ given database name with extension
        prints table headers
    """
    if len(sys.argv) > 1:
        db_name = sys.argv[1]
    obj = MTLibrary()
    obj.table_columns(db_name)

