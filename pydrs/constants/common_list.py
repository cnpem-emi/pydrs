"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """''
======================================================================
                    Listas de Entidades BSMP
        A posição da entidade na lista corresponde ao seu ID BSMP
======================================================================
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" ""

list_ps_models = [
    "Empty",
    "FBP",
    "FBP_DCLink",
    "FAC_ACDC",
    "FAC_DCDC",
    "FAC_2S_ACDC",
    "FAC_2S_DCDC",
    "FAC_2P4S_ACDC",
    "FAC_2P4S_DCDC",
    "FAP",
    "FAP_4P",
    "FAC_DCDC_EMA",
    "FAP_2P2S",
    "FAP_IMAS",
    "FAC_2P_ACDC_IMAS",
    "FAC_2P_DCDC_IMAS",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Invalid",
    "Uninitialized",
]

list_common_vars = [
    "ps_status",
    "ps_setpoint",
    "ps_reference",
    "firmware_version",
    "counter_set_slowref",
    "counter_sync_pulse",
    "siggen_enable",
    "siggen_type",
    "siggen_num_cycles",
    "siggen_n",
    "siggen_freq",
    "siggen_amplitude",
    "siggen_offset",
    "siggen_aux_param",
    "wfmref_selected",
    "wfmref_sync_mode",
    "wfmref_gain",
    "wfmref_offset",
    "p_wfmref_start",
    "p_wfmref_end",
    "p_wfmref_idx",
]

# list_curv = ['wfmref','buf_samples_ctom','buf_samples_mtoc']
list_curv = ["wfmref_data_0", "wfmref_data_1", "buf_samples_ctom"]

list_func = [
    "turn_on",
    "turn_off",
    "open_loop",
    "closed_loop",
    "select_op_mode",
    "reset_interlocks",
    "set_command_interface",
    "set_serial_termination",
    "unlock_udc",
    "lock_udc",
    "cfg_source_scope",
    "cfg_freq_scope",
    "cfg_duration_scope",
    "enable_scope",
    "disable_scope",
    "sync_pulse",
    "set_slowref",
    "set_slowref_fbp",
    "set_slowref_readback_mon",
    "set_slowref_fbp_readback_mon",
    "set_slowref_readback_ref",
    "set_slowref_fbp_readback_ref",
    "reset_counters",
    "cfg_wfmref",
    "select_wfmref",
    "get_wfmref_size",
    "reset_wfmref",
    "cfg_siggen",
    "set_siggen",
    "enable_siggen",
    "disable_siggen",
    "set_param",
    "get_param",
    "save_param_eeprom",
    "load_param_eeprom",
    "save_param_bank",
    "load_param_bank",
    "set_dsp_coeffs",
    "get_dsp_coeff",
    "save_dsp_coeffs_eeprom",
    "load_dsp_coeffs_eeprom",
    "save_dsp_modules_eeprom",
    "load_dsp_modules_eeprom",
    "reset_udc",
]

list_op_mode = [
    "Off",
    "Interlock",
    "Initializing",
    "SlowRef",
    "SlowRefSync",
    "Cycle",
    "RmpWfm",
    "MigWfm",
    "FastRef",
]

list_sig_gen_types = [
    "Sine",
    "DampedSine",
    "Trapezoidal",
    "DampedSquaredSine",
    "Square",
]

list_parameters = [
    "PS_Name",
    "PS_Model",
    "Num_PS_Modules",
    "Command_Interface",
    "RS485_Baudrate",
    "RS485_Address",
    "RS485_Termination",
    "UDCNet_Address",
    "Ethernet_IP",
    "Ethernet_Subnet_Mask",
    "Buzzer_Volume",
    "Freq_ISR_Controller",
    "Freq_TimeSlicer",
    "Control_Loop_State",
    "Max_Ref",
    "Min_Ref",
    "Max_Ref_OpenLoop",
    "Min_Ref_OpenLoop",
    "PWM_Freq",
    "PWM_DeadTime",
    "PWM_Max_Duty",
    "PWM_Min_Duty",
    "PWM_Max_Duty_OpenLoop",
    "PWM_Min_Duty_OpenLoop",
    "PWM_Lim_Duty_Share",
    "HRADC_Num_Boards",
    "HRADC_Freq_SPICLK",
    "HRADC_Freq_Sampling",
    "HRADC_Enable_Heater",
    "HRADC_Enable_Monitor",
    "HRADC_Type_Transducer",
    "HRADC_Gain_Transducer",
    "HRADC_Offset_Transducer",
    "SigGen_Type",
    "SigGen_Num_Cycles",
    "SigGen_Freq",
    "SigGen_Amplitude",
    "SigGen_Offset",
    "SigGen_Aux_Param",
    "WfmRef_ID_WfmRef",
    "WfmRef_SyncMode",
    "WfmRef_Frequency",
    "WfmRef_Gain",
    "WfmRef_Offset",
    "Analog_Var_Max",
    "Analog_Var_Min",
    "Hard_Interlocks_Debounce_Time",
    "Hard_Interlocks_Reset_Time",
    "Soft_Interlocks_Debounce_Time",
    "Soft_Interlocks_Reset_Time",
    "Scope_Sampling_Frequency",
    "Scope_Source",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Password",
    "Enable_Onboard_EEPROM",
]
