# -*- coding: utf-8 -*-
import db_tables
#                                         ["",
#                                          "",
#                                          ""]

MT_Version                  = "Version 19.00.01"
SNR_Version_LTE                 = "Version 7.00 LTE"
SNR_Version_3G                  = "Version 4.00 3G"

#===========================================================================================================

engVariables  = {'Macro_2345_185_exit_code' : 'Excess of CA Acceptable Execution',
                 'Target_MT_Version_LTE'    : MT_Version,
                 'Target_MT_Version_3G'     : MT_Version,
                 'Target_SNR_Version_LTE'   : SNR_Version_LTE,
                 'Target_SNR_Version_3G'    : SNR_Version_3G}

japVariables  = {'Macro_2345_185_exit_code' : '',
                 'Target_MT_Version_LTE'    : MT_Version,
                 'Target_MT_Version_3G'     : MT_Version,
                 'Target_SNR_Version_LTE'   : SNR_Version_LTE,
                 'Target_SNR_Version_3G'    : SNR_Version_3G}


def get_variables(arg):
    if arg == 'en':
        return engVariables
    elif arg == 'jp':
        return japVariables
