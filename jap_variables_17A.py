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
Macro_1247_name                        = u"Pagingメッセージ送信マクロ4"

#to be excluded in the filter parameter list creation
Macro_1247_new_parameters_indices      = [ [5, 7, 8, 9, 10, 11, 15, 16] ]
Macro_1247_old_parameters_indices      = [ [5, 7] ]


Macro_1247_parameter_name              = [u"Paging Frame",
                                          u"Paging送信周期",
                                          u"Paging Hyperframe",
                                          u"eDRX Paging送信周期",
                                          u"PTW start",
                                          u"Paging Time Window",
                                          u"送信メッセージ種別",
                                          u"累積送信回数"]

Macro_1247_parameter_limit_print_string    = [u"0 ～ 511",
                                              u"32, 64, 128, 256, 512",
                                              u"0 ～ 255",
                                              u"1, 2, 4, 6, 8, 10, 12, 14, 16, 32, 64, 128, 256",
                                              u"0 ～ 1023",
                                              u"1 ～ 16",
                                              u"0 ～ 1",
                                              u"1 ～ 64"]

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
Macro_1359_name                        = u"RB使用率報告マクロ4"

#to be excluded in the filter parameter list creation
Macro_1359_new_parameters_indices      = [ [], [0, 32, 33, 34, 35] ]
Macro_1359_old_parameters_indices      = [ [], [0] ]

Macro_1359_parameter_name              = [u"マクロ番号",
                                          u"DL RB使用率(4CC)状態",
                                          u"DL RB使用率(4CC)",
                                          u"DL RB使用率(5CC)状態",
                                          u"DL RB使用率(5CC)"]

Macro_1359_parameter_limit_print_string    = [u"本マクロ番号　1359",
                                              u"0 ～ 4",
                                              u"0 ～ 100",
                                              u"0 ～ 4",
                                              u"1 ～ 100"]

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

#===========================================================================================================
#to be excluded in the filter parameter list creation
Macro_1360_name                        = u"DLチャネル使用状況報告マクロ5"
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

Macro_1360_parameter_name              = [u"マクロ番号",
                                          u"非TM9,非4TxTM4 Wideband CQIのRBS-ID数状態",
                                          u"非TM9,非4TxTM4 RANK1 Wideband CQIのRBS-ID数",
                                          u"非TM9,非4TxTM4 RANK2 Wideband CQIのRBS-ID数",
                                          u"TM4(4×2) Wideband CQIのRBS-ID数状態",
                                          u"TM4(4×2) RANK1 Wideband CQIのRBS-ID数",
                                          u"TM4(4×2) RANK2 Wideband CQIのRBS-ID数",
                                          u"TM4(4×4) Wideband CQIのRBS-ID数状態",
                                          u"TM4(4×4) RANK1 Wideband CQIのRBS-ID数",
                                          u"TM4(4×4) RANK2 Wideband CQIのRBS-ID数",
                                          u"TM4(4×4) RANK3 Wideband CQIのRBS-ID数",
                                          u"TM4(4×4) RANK4 Wideband CQIのRBS-ID数",
                                          u"平均LCPスループット(4CC)状態",
                                          u"平均LCPスループット(4CC)",
                                          u"平均LCPスループット(5CC)状態",
                                          u"平均LCPスループット(5CC)",
                                          u"平均LCPスループット(非TM9,非4TxTM4)状態",
                                          u"平均LCPスループット(非TM9,非4TxTM4)",
                                          u"平均LCPスループット(TM4(4×2))状態",
                                          u"平均LCPスループット(TM4(4×2))",
                                          u"平均LCPスループット(TM4(4×4))状態",
                                          u"平均LCPスループット(TM4(4×4))"]

Macro_1360_parameter_limit_print_string    = [u"本マクロ番号　1360",
                                              u"0 ～ 4",
                                              u"0 ～ 65535",
                                              u"0 ～ 65535",
                                              u"0 ～ 4",
                                              u"0 ～ 65535",
                                              u"0 ～ 65535",
                                              u"0 ～ 4",
                                              u"0 ～ 65535",
                                              u"0 ～ 65535",
                                              u"0 ～ 65535",
                                              u"0 ～ 65535",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295"]

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
#to be excluded in the filter parameter list creation
Macro_1361_name                        = u"MAC SDU送受信レート報告マクロ4"
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

Macro_1361_parameter_name              = [u"マクロ番号",
                                          u"MAC SDU送信レート1(非TM9,非4TxTM4)状態",
                                          u"MAC SDU送信レート1(非TM9,非4TxTM4)",
                                          u"MAC SDU送信レート2(非TM9,非4TxTM4)状態",
                                          u"MAC SDU送信レート2(非TM9,非4TxTM4)",
                                          u"MAC SDU送信レート1(TM4(4×2))状態",
                                          u"MAC SDU送信レート1(TM4(4×2))",
                                          u"MAC SDU送信レート2(TM4(4×2))状態",
                                          u"MAC SDU送信レート2(TM4(4×2))",
                                          u"MAC SDU送信レート1(TM4(4×4))状態",
                                          u"MAC SDU送信レート1(TM4(4×4))",
                                          u"MAC SDU送信レート2(TM4(4×4))状態",
                                          u"MAC SDU送信レート2(TM4(4×4))"]

Macro_1361_parameter_limit_print_string    = [u"本マクロ番号　1361",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295"]

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
Macro_1362_name                        = u"MAC PDU送受信レート報告マクロ5"

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

Macro_1362_parameter_name              = [u"マクロ番号",
                                          u"DL MAC　PDU送信レート(4CC)状態",
                                          u"DL MAC　PDU送信レート(4CC)",
                                          u"DL MAC　PDU送信レート(5CC)状態",
                                          u"DL MAC　PDU送信レート(5CC)",
                                          u"DL MAC　PDU送信レート(非TM9,非4TxTM4)状態",
                                          u"DL MAC　PDU送信レート(非TM9,非4TxTM4)",
                                          u"DL MAC　PDU送信レート(TM4(4×2))状態",
                                          u"DL MAC　PDU送信レート(TM4(4×2))",
                                          u"DL MAC　PDU送信レート(TM4(4×4))状態",
                                          u"DL MAC　PDU送信レート(TM4(4×4))"]

Macro_1362_parameter_limit_print_string    = [u"本マクロ番号　1362",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295",
                                              u"0 ～ 4",
                                              u"0 ～ 4294967295"]

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
