# -*- coding: utf-8 -*-
import db_tables
#                                         ["",
#                                          "",
#                                          ""]

Target_MT_Version_LTE                  = "Version 09.00.00"
Target_MT_Version_3G                   = Target_MT_Version_LTE
Target_SNR_Version_LTE                 = "Version 9.00 LTE"
Target_SNR_Version_3G                  = "Version 3.00 3G"

#skipped parameter name columns during per column checking
Skipped_Columns_List                   = [
                                          db_tables.CP_PARA_NAME.index('key_no'), 
                                          db_tables.CP_PARA_NAME.index('ascii_parameter_count'), 
                                          db_tables.CP_PARA_NAME.index('hex_parameter_count'), 
                                          db_tables.CP_PARA_NAME.index('input_size'),
                                          db_tables.CP_PARA_NAME.index('display_size'),
                                          db_tables.CP_PARA_NAME.index('Struct_key') 
                                          ]

#===========================================================================================================
Macro_2312_combo_index_2_string        = "Intra-RAT(Full Configuration)"
