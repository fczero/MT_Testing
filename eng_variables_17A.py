# -*- coding: utf-8 -*-
import db_tables
#                                         ["",
#                                          "",
#                                          ""]

Target_MT_Version_LTE                  = "Version 19.00.01"
Target_MT_Version_3G                   = Target_MT_Version_LTE
Target_SNR_Version_LTE                 = "Version 7.00 LTE"
Target_SNR_Version_3G                  = "Version 4.00 3G"

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
Macro_1247_name                        = "Paging Message Transmission 4"

#to be excluded in the filter parameter list creation
Macro_1247_new_parameters_indices      = [ [5, 7, 8, 9, 10, 11, 15, 16] ]
Macro_1247_old_parameters_indices      = [ [5, 7] ]


Macro_1247_parameter_name              = ["Paging Frame",
                                          "Paging transmission interval",
                                          "Paging Hyperframe",
                                          "eDRX Paging transmission interval",
                                          "PTW start",
                                          "Paging Time Window",
                                          "Transmission message type",
                                          "Accumulated number of transmission"]

Macro_1247_parameter_limit_print_string    = ["0 .. 511",
                                              "32, 64, 128, 256, 512",
                                              "0 .. 255",
                                              "1, 2, 4, 6, 8, 10, 12, 14, 16, 32, 64, 128, 256",
                                              "0 .. 1023",
                                              "1 .. 16",
                                              "0 .. 1",
                                              "1 .. 64"]

Macro_1247_parameter_input_form        = [db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field')]

Macro_1247_parameter_type              = [db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short')]

#===========================================================================================================

Macro_1354_affected_parameter_numbers       = [1686,
                                               1687,
                                               1688,
                                               1689,
                                               1690,
                                               1691,
                                               1692,
                                               1693,
                                               1694,
                                               1695,
                                               1696,
                                               1697,
                                               1698,
                                               1699,
                                               1914,
                                               1915,
                                               1916,
                                               1917,
                                               4061,
                                               4062,
                                               4063,
                                               4064,
                                               4065,
                                               4066]

Macro_1354_parameter_name_changes      = ["DL RB utilization rate (status)",
                                          "DL RB utilization rate (value)",
                                          "UL RB utilization rate (status)",
                                          "UL RB utilization rate (value)",
                                          "DL RB utilization rate (DBCH) (status)",
                                          "DL RB utilization rate (DBCH) (value)",
                                          "DL RB utilization rate (PCH) (status)",
                                          "DL RB utilization rate (PCH) (value)",
                                          "DL RB utilization rate (RAR) (status)",
                                          "DL RB utilization rate (RAR) (value)",
                                          "DL RB utilization rate (Voice) (status)",
                                          "DL RB utilization rate (Voice) (value)",
                                          "UL RB utilization rate (Voice) (status)",
                                          "UL RB utilization rate (Voice) (value)",
                                          "DL RB utilization rate (SCell) (status)",
                                          "DL RB utilization rate (SCell) (value)",
                                          "DL RB utilization rate (SCell/Voice) (status)",
                                          "DL RB utilization rate (SCell/Voice) (value)",
                                          "DL RB utilization rate (Non-CA) (status)",
                                          "DL RB utilization rate (Non-CA) (value)",
                                          "DL RB utilization rate (2CC) (status)",
                                          "DL RB utilization rate (2CC) (value)",
                                          "DL RB utilization rate (3CC) (status)",
                                          "DL RB utilization rate (3CC) (value)"]

#===========================================================================================================
Macro_1359_name                        = "RB Utilization Rate Report 4"

#to be excluded in the filter parameter list creation
Macro_1359_new_parameters_indices      = [ [], [0, 32, 33, 34, 35] ]
Macro_1359_old_parameters_indices      = [ [], [0] ]

Macro_1359_parameter_name              = ["API ID",
                                          "DL RB utilization rate (4CC) (status)",
                                          "DL RB utilization rate (4CC) (value)",
                                          "DL RB utilization rate (5CC) (status)",
                                          "DL RB utilization rate (5CC) (value)"]

Macro_1359_parameter_limit_print_string    = ["API ID 1359",
                                              "0 .. 4",
                                              "0 .. 100",
                                              "0 .. 4",
                                              "1 .. 100"]

Macro_1359_parameter_input_form        = [db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field')]

Macro_1359_parameter_type              = [db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short')]

Macro_1359_affected_parameter_indices = [8,
                                         9,
                                         10,
                                         11,
                                         12,
                                         13,
                                         14,
                                         15,
                                         16,
                                         17,
                                         18,
                                         19,
                                         20,
                                         21,
                                         22,
                                         23,
                                         24,
                                         25,
                                         26,
                                         27,
                                         28,
                                         29,
                                         30,
                                         31]

Macro_1359_parameter_name_changes      = ["DL RB utilization rate (status)",
                                          "DL RB utilization rate (value)",
                                          "UL RB utilization rate (status)",
                                          "UL RB utilization rate (value)",
                                          "DL RB utilization rate (DBCH) (status)",
                                          "DL RB utilization rate (DBCH) (value)",
                                          "DL RB utilization rate (PCH) (status)",
                                          "DL RB utilization rate (PCH) (value)",
                                          "DL RB utilization rate (RAR) (status)",
                                          "DL RB utilization rate (RAR) (value)",
                                          "DL RB utilization rate (Voice) (status)",
                                          "DL RB utilization rate (Voice) (value)",
                                          "UL RB utilization rate (Voice) (status)",
                                          "UL RB utilization rate (Voice) (value)",
                                          "DL RB utilization rate (SCell) (status)",
                                          "DL RB utilization rate (SCell) (value)",
                                          "DL RB utilization rate (SCell/Voice) (status)",
                                          "DL RB utilization rate (SCell/Voice) (value)",
                                          "DL RB utilization rate (Non-CA) (status)",
                                          "DL RB utilization rate (Non-CA) (value)",
                                          "DL RB utilization rate (2CC) (status)",
                                          "DL RB utilization rate (2CC) (value)",
                                          "DL RB utilization rate (3CC) (status)",
                                          "DL RB utilization rate (3CC) (value)"]

#===========================================================================================================
Macro_1360_name                        = "DL Channel Utilization Status Report 5"

#to be excluded in the filter parameter list creation
Macro_1360_new_parameters_indices      = [ [], [0,
                                               27,
                                               28,
                                               29,
                                               38,
                                               39,
                                               40,
                                               41,
                                               42,
                                               43,
                                               44,
                                               45,
                                               71,
                                               72,
                                               73,
                                               74,
                                               75,
                                               76,
                                               81,
                                               82,
                                               83,
                                               84] ]

Macro_1360_old_parameters_indices      = [ [], [0,
                                               27,
                                               28,
                                               29,
                                               63,
                                               64] ]

Macro_1360_parameter_name              = ["API ID",
                                          "Number of RBS-ID of non-TM9, non-4TxTM4 Wideband CQI (status)",
                                          "Number of RBS-ID of non-TM9, non-4TxTM4 RANK1 Wideband CQI (value)",
                                          "Number of RBS-ID of non-TM9, non-4TxTM4 RANK2 Wideband CQI (value)",
                                          "Number of RBS-ID of TM4(4x2) Wideband CQI (status)",
                                          "Number of RBS-ID of TM4(4x2) RANK1 Wideband CQI (value)",
                                          "Number of RBS-ID of TM4(4x2) RANK2 Wideband CQI (value)",
                                          "Number of RBS-ID of TM4(4x4) Wideband CQI (status)",
                                          "Number of RBS-ID of TM4(4x4) RANK1 Wideband CQI (value)",
                                          "Number of RBS-ID of TM4(4x4) RANK2 Wideband CQI (value)",
                                          "Number of RBS-ID of TM4(4x4) RANK3 Wideband CQI (value)",
                                          "Number of RBS-ID of TM4(4x4) RANK4 Wideband CQI (value)",
                                          "Average LCP throughput (4CC) (status)",
                                          "Average LCP throughput (4CC) (value)",
                                          "Average LCP throughput (5CC) (status)",
                                          "Average LCP throughput (5CC) (value)",
                                          "Average LCP throughput (non-TM9, non-4TxTM4) (status)",
                                          "Average LCP throughput (non-TM9, non-4TxTM4) (value)",
                                          "Average LCP throughput (TM4(4x2)) (status)",
                                          "Average LCP throughput (TM4(4x2)) (value)",
                                          "Average LCP throughput (TM4(4x4)) (status)",
                                          "Average LCP throughput (TM4(4x4)) (value)"]

Macro_1360_parameter_limit_print_string    = ["API ID 1360",
                                              "0 .. 4",
                                              "0 .. 65535",
                                              "0 .. 65535",
                                              "0 .. 4",
                                              "0 .. 65535",
                                              "0 .. 65535",
                                              "0 .. 4",
                                              "0 .. 65535",
                                              "0 .. 65535",
                                              "0 .. 65535",
                                              "0 .. 65535",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295"]

Macro_1360_parameter_input_form        = [db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field')]

Macro_1360_parameter_type              = [db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long')]

#===========================================================================================================
Macro_1361_name                        = "MAC SDU Transmission/Reception Rate Report 4"

#to be excluded in the filter parameter list creation
Macro_1361_new_parameters_indices      = [ [], [0,
                                               19,
                                               20,
                                               21,
                                               22,
                                               31,
                                               32,
                                               33,
                                               34,
                                               35,
                                               36,
                                               37,
                                               38] ]

Macro_1361_old_parameters_indices      = [ [], [0,
                                               19,
                                               20,
                                               21,
                                               22] ]

Macro_1361_parameter_name              = ["API ID",
                                          "MAC SDU Transmission Rate1 (non-TM9, non-4TxTM4) (status)",
                                          "MAC SDU Transmission Rate1 (non-TM9, non-4TxTM4) (value)",
                                          "MAC SDU Transmission Rate2 (non-TM9, non-4TxTM4) (status)",
                                          "MAC SDU Transmission Rate2 (non-TM9, non-4TxTM4) (value)",
                                          "MAC SDU Transmission Rate1 (TM4(4x2)) (status)",
                                          "MAC SDU Transmission Rate1 (TM4(4x2)) (value)",
                                          "MAC SDU Transmission Rate2 (TM4(4x2)) (status)",
                                          "MAC SDU Transmission Rate2 (TM4(4x2)) (value)",
                                          "MAC SDU Transmission Rate1 (TM4(4x4)) (status)",
                                          "MAC SDU Transmission Rate1 (TM4(4x4)) (value)",
                                          "MAC SDU Transmission Rate2 (TM4(4x4)) (status)",
                                          "MAC SDU Transmission Rate2 (TM4(4x4)) (value)"]

Macro_1361_parameter_limit_print_string    = ["API ID 1361",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295"]

Macro_1361_parameter_input_form        = [db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field')]

Macro_1361_parameter_type              = [db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long')]

#===========================================================================================================
Macro_1362_name                        = "MAC PDU Transmission/Reception Rate Report 5"

#to be excluded in the filter parameter list creation
Macro_1362_new_parameters_indices      = [ [], [0,
                                               25,
                                               26,
                                               27,
                                               28,
                                               29,
                                               30,
                                               35,
                                               36,
                                               37,
                                               38] ]
Macro_1362_old_parameters_indices      = [ [], [0,
                                               25,
                                               26] ]

Macro_1362_parameter_name              = ["API ID",
                                          "DL MAC PDU Transmission Rate3(4CC) (status)",
                                          "DL MAC PDU Transmission Rate3(4CC) (value)",
                                          "DL MAC PDU Transmission Rate3(5CC) (status)",
                                          "DL MAC PDU Transmission Rate3(5CC) (value)",
                                          "DL MAC PDU Transmission Rate (Non-TM9, Non-4TxTM4) (status)",
                                          "DL MAC PDU Transmission Rate (Non-TM9, Non-4TxTM4) (value)",
                                          "DL MAC PDU Transmission Rate (TM4(4x2)) (status)",
                                          "DL MAC PDU Transmission Rate (TM4(4x2)) (value)",
                                          "DL MAC PDU Transmission Rate (TM4(4x4)) (status)",
                                          "DL MAC PDU Transmission Rate (TM4(4x4)) (value)"]

Macro_1362_parameter_limit_print_string    = ["API ID 1362",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295",
                                              "0 .. 4",
                                              "0 .. 4294967295"]

Macro_1362_parameter_input_form        = [db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field'),
                                          db_tables.INPUT_FORM.index('combo box'),
                                          db_tables.INPUT_FORM.index('text field')]

Macro_1362_parameter_type              = [db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long'),
                                          db_tables.DATA_TYPES.index('unsigned short'),
                                          db_tables.DATA_TYPES.index('unsigned long')]

#===========================================================================================================
##to be excluded in the filter parameter list creation
#Macro_0000_new_parameters_indices      = [ [], [0,
#                                               ] ]
#Macro_0000_old_parameters_indices      = [ [], [0,
#                                               ] ]
#
#Macro_0000_parameter_name              = ["API ID",
#                                                ,
#                                                ]
#
#Macro_0000_parameter_limit_print_string    = ["0000",
#                                              ]
#
#Macro_0000_parameter_input_form        = [db_tables.INPUT_FORM.index('text field'),
#                                          ]
#
#Macro_0000_parameter_type              = [db_tables.DATA_TYPES.index('unsigned short'),
#                                          ]
#
#===========================================================================================================

#Macro_1020_combo_index_3_string        = "Blocked (specify at PBLK)"
#Macro_1336_parameter_name_changes      = ["DL MAC PDU Transmission Rate (status)",
#                                          "DL MAC PDU Transmission Rate (value)",
#                                          "DL MAC PDU Transmission Rate (Scell) (status)",
#                                          "DL MAC PDU Transmission Rate (Scell) (value)",
#                                          "DL MAC PDU Transmission Rate (ACK) (status)",
#                                          "DL MAC PDU Transmission Rate (ACK) (value)",
#                                          "DL MAC PDU Transmission Rate (ACK/Scell) (status)",
#                                          "DL MAC PDU Transmission Rate (ACK/Scell) (value)",
#                                          "UL MAC PDU Reception Rate (status)",
#                                          "UL MAC PDU Reception Rate (value)",
#                                          "UL MAC PDU Reception Rate (CRC OK) (status)",
#                                          "UL MAC PDU Reception Rate (CRC OK) (value)"]
#
#Macro_1336_affected_parameter_numbers  = ["1491",
#                                          "1492",
#                                          "1857",
#                                          "1858",
#                                          "1494",
#                                          "1495",
#                                          "1859",
#                                          "1860",
#                                          "1862",
#                                          "1863",
#                                          "1864",
#                                          "1865"]
#Macro_1337_affected_parameter_numbers  = ["1478",
#                                          "1479"]
#Macro_1337_parameter_name_changes      = ["Logical CH(DL) having suprathreshold ave buffered time (status)",
#                                          "Logical CH(DL) having suprathreshold ave buffered time (value)"]
#Macro_2391_30_exit_code_string         = "Assigned CNT Type error"
#Macro_2392_limit_print_string_1_6      = "1 .. 6"
#Macro_2392_limit_print_string_1_8      = "1 .. 8"
#Macro_2393_30_exit_code_string         = "Assigned CNT Type error"
#Macro_2393_limit_print_string_1_6      = "1 .. 6"
#Macro_2393_limit_print_string_1_8      = "1 .. 8"
#Macro_3040_combo_index_2_string        = "Block"
#Macro_3040_combo_index_3_string        = "Release block"
#Macro_3040_combo_index_5_string        = "Forced block"
#
