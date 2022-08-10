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

list_parameters = {
    "PS_Name":{
        "id": 0, "n": 64},
    "PS_Model":{
        "id": 1, "n": 1},
    "Num_PS_Modules":{
        "id": 2, "n": 1},
    "Command_Interface":{
        "id": 3, "n": 1},
    "RS485_Baudrate":{
        "id": 4, "n": 1},
    "RS485_Address":{
        "id": 5, "n": 4},
    "RS485_Termination":{
        "id": 6, "n": 1},
    "UDCNet_Address":{
        "id": 7, "n": 1},
    "Ethernet_IP":{
        "id": 8, "n": 4},
    "Ethernet_Subnet_Mask":{
        "id": 9, "n": 4},
    "Buzzer_Volume":{
        "id": 10, "n": 1},
    "Freq_ISR_Controller":{
        "id": 11, "n": 1},
    "Freq_TimeSlicer":{
        "id": 12, "n": 4},
    "Control_Loop_State":{
        "id": 13, "n": 1},
    "Max_Ref":{
        "id": 14, "n": 4},
    "Min_Ref":{
        "id": 15, "n": 4},
    "Max_Ref_OpenLoop":{
        "id": 16, "n": 4},
    "Min_Ref_OpenLoop":{
        "id": 17, "n": 4},
    "PWM_Freq":{
        "id": 18, "n": 1},
    "PWM_DeadTime":{
        "id": 19, "n": 1},
    "PWM_Max_Duty":{
        "id": 20, "n": 1},
    "PWM_Min_Duty":{
        "id": 21, "n": 1},
    "PWM_Max_Duty_OpenLoop":{
        "id": 22, "n": 1},
    "PWM_Min_Duty_OpenLoop":{
        "id": 23, "n": 1},
    "PWM_Lim_Duty_Share":{
        "id": 24, "n": 1},
    "HRADC_Num_Boards":{
        "id": 25, "n": 1},
    "HRADC_Freq_SPICLK":{
        "id": 26, "n": 1},
    "HRADC_Freq_Sampling":{
        "id": 27, "n": 1},
    "HRADC_Enable_Heater":{
        "id": 28, "n": 4},
    "HRADC_Enable_Monitor":{
        "id": 29, "n": 4},
    "HRADC_Type_Transducer":{
        "id": 30, "n": 4},
    "HRADC_Gain_Transducer":{
        "id": 31, "n": 4},
    "HRADC_Offset_Transducer":{
        "id": 32, "n": 4},
    "SigGen_Type":{
        "id": 33, "n": 1},
    "SigGen_Num_Cycles":{
        "id": 34, "n": 1},
    "SigGen_Freq":{
        "id": 35, "n": 1},
    "SigGen_Amplitude":{
        "id": 36, "n": 1},
    "SigGen_Offset":{
        "id": 37, "n": 1},
    "SigGen_Aux_Param":{
        "id": 38, "n": 4},
    "WfmRef_ID_WfmRef":{
        "id": 39, "n": 4},
    "WfmRef_SyncMode":{
        "id": 40, "n": 4},
    "WfmRef_Frequency":{
        "id": 41, "n": 4},
    "WfmRef_Gain":{
        "id": 42, "n": 4},
    "WfmRef_Offset":{
        "id": 43, "n": 4},
    "Analog_Var_Max":{
        "id": 44, "n": 64},
    "Analog_Var_Min":{
        "id": 45, "n": 64},
    "Hard_Interlocks_Debounce_Time":{
        "id": 46, "n": 32},
    "Hard_Interlocks_Reset_Time":{
        "id": 47, "n": 32},
    "Soft_Interlocks_Debounce_Time":{
        "id": 48, "n": 32},
    "Soft_Interlocks_Reset_Time":{
        "id": 49, "n": 32},
    "Scope_Sampling_Frequency":{
        "id": 50, "n": 4},
    "Scope_Source":{
        "id": 51, "n": 4},
    "":{"id": 52, "n": 1},
    "":{"id": 53, "n": 1},
    "":{"id": 54, "n": 1},
    "":{"id": 55, "n": 1},
    "":{"id": 56, "n": 1},
    "":{"id": 57, "n": 1},
    "":{"id": 58, "n": 1},
    "":{"id": 59, "n": 1},
    "":{"id": 60, "n": 1},
    "":{"id": 61, "n": 1},
    "Password":{"id": 62, "n": 4},
    "Enable_Onboard_EEPROM":{"id": 63, "n": 1}
}