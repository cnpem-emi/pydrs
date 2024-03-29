ps_models = [
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
    "SWLS_RESONANT_CONVERTER",
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

vars = [
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

# curv = ['wfmref','buf_samples_ctom','buf_samples_mtoc']
curves = ["wfmref_data_0", "wfmref_data_1", "buf_samples_ctom"]

functions = [
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

op_modes = [
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

sig_gen_types = [
    "Sine",
    "DampedSine",
    "Trapezoidal",
    "DampedSquaredSine",
    "Square",
]

wfmref_sync_modes = ["SampleBySample", "SampleBySample_OneCycle", "OneShot"]

versions = [
    "udc_arm",
    "udc_c28",
    "hradc0_cpld",
    "hradc1_cpld",
    "hradc2_cpld",
    "hradc3_cpld",
    "iib_arm",
    "ihm_pic",
]

params = {
    "PS_Name": {"id": 0, "n": 64},
    "PS_Model": {"id": 1, "n": 1},
    "Num_PS_Modules": {"id": 2, "n": 1},
    "Command_Interface": {"id": 3, "n": 1},
    "RS485_Baudrate": {"id": 4, "n": 1},
    "RS485_Address": {"id": 5, "n": 4},
    "RS485_Termination": {"id": 6, "n": 1},
    "UDCNet_Address": {"id": 7, "n": 1},
    "Ethernet_IP": {"id": 8, "n": 4},
    "Ethernet_Subnet_Mask": {"id": 9, "n": 4},
    "Buzzer_Volume": {"id": 10, "n": 1},
    "Freq_ISR_Controller": {"id": 11, "n": 1},
    "Freq_TimeSlicer": {"id": 12, "n": 4},
    "Control_Loop_State": {"id": 13, "n": 1},
    "Max_Ref": {"id": 14, "n": 4},
    "Min_Ref": {"id": 15, "n": 4},
    "Max_Ref_OpenLoop": {"id": 16, "n": 4},
    "Min_Ref_OpenLoop": {"id": 17, "n": 4},
    "PWM_Freq": {"id": 18, "n": 1},
    "PWM_DeadTime": {"id": 19, "n": 1},
    "PWM_Max_Duty": {"id": 20, "n": 1},
    "PWM_Min_Duty": {"id": 21, "n": 1},
    "PWM_Max_Duty_OpenLoop": {"id": 22, "n": 1},
    "PWM_Min_Duty_OpenLoop": {"id": 23, "n": 1},
    "PWM_Lim_Duty_Share": {"id": 24, "n": 1},
    "HRADC_Num_Boards": {"id": 25, "n": 1},
    "HRADC_Freq_SPICLK": {"id": 26, "n": 1},
    "HRADC_Freq_Sampling": {"id": 27, "n": 1},
    "HRADC_Enable_Heater": {"id": 28, "n": 4},
    "HRADC_Enable_Monitor": {"id": 29, "n": 4},
    "HRADC_Type_Transducer": {"id": 30, "n": 4},
    "HRADC_Gain_Transducer": {"id": 31, "n": 4},
    "HRADC_Offset_Transducer": {"id": 32, "n": 4},
    "SigGen_Type": {"id": 33, "n": 1},
    "SigGen_Num_Cycles": {"id": 34, "n": 1},
    "SigGen_Freq": {"id": 35, "n": 1},
    "SigGen_Amplitude": {"id": 36, "n": 1},
    "SigGen_Offset": {"id": 37, "n": 1},
    "SigGen_Aux_Param": {"id": 38, "n": 4},
    "WfmRef_ID_WfmRef": {"id": 39, "n": 4},
    "WfmRef_SyncMode": {"id": 40, "n": 4},
    "WfmRef_Frequency": {"id": 41, "n": 4},
    "WfmRef_Gain": {"id": 42, "n": 4},
    "WfmRef_Offset": {"id": 43, "n": 4},
    "Analog_Var_Max": {"id": 44, "n": 64},
    "Analog_Var_Min": {"id": 45, "n": 64},
    "Hard_Interlocks_Debounce_Time": {"id": 46, "n": 32},
    "Hard_Interlocks_Reset_Time": {"id": 47, "n": 32},
    "Soft_Interlocks_Debounce_Time": {"id": 48, "n": 32},
    "Soft_Interlocks_Reset_Time": {"id": 49, "n": 32},
    "Scope_Sampling_Frequency": {"id": 50, "n": 4},
    "Scope_Source": {"id": 51, "n": 4},
    "": {"id": 61, "n": 1},
    "Password": {"id": 62, "n": 4},
    "Enable_Onboard_EEPROM": {"id": 63, "n": 1},
}

bsmp = {
    "ps_status": {"addr": 0, "format": "H", "size": 2, "egu": ""},
    "ps_setpoint": {"addr": 1, "format": "f", "size": 4, "egu": "A"},
    "ps_reference": {"addr": 2, "format": "f", "size": 4, "egu": "A"},
    "firmware_version": {"addr": 3, "format": "128s", "size": 128, "egu": ""},
    "counter_set_slowref": {"addr": 4, "format": "I", "size": 4, "egu": ""},
    "counter_sync_pulse": {"addr": 5, "format": "I", "size": 4, "egu": ""},
    "siggen_enable": {"addr": 6, "format": "H", "size": 2, "egu": ""},
    "siggen_type": {"addr": 7, "format": "H", "size": 2, "egu": ""},
    "siggen_num_cycles": {"addr": 8, "format": "H", "size": 2, "egu": ""},
    "siggen_n": {"addr": 9, "format": "f", "size": 4, "egu": ""},
    "siggen_freq": {"addr": 10, "format": "f", "size": 4, "egu": "Hz"},
    "siggen_amplitude": {"addr": 11, "format": "f", "size": 4, "egu": "A"},
    "siggen_offset": {"addr": 12, "format": "f", "size": 4, "egu": "A"},
    "siggen_aux_param_0": {"addr": 13, "format": "f", "size": 4, "egu": ""},
    "siggen_aux_param_1": {"addr": 13, "format": "f", "size": 4, "egu": ""},
    "siggen_aux_param_2": {"addr": 13, "format": "f", "size": 4, "egu": ""},
    "siggen_aux_param_3": {"addr": 13, "format": "f", "size": 4, "egu": ""},
    "wfmref_selected": {"addr": 14, "format": "H", "size": 2, "egu": ""},
    "wfmref_sync_mode": {"addr": 15, "format": "H", "size": 2, "egu": ""},
    "wfmref_frequency": {"addr": 16, "format": "f", "size": 4, "egu": "Hz"},
    "wfmref_gain": {"addr": 17, "format": "f", "size": 4, "egu": "A"},
    "wfmref_offset": {"addr": 18, "format": "f", "size": 4, "egu": "A"},
    "p_wfmref_start_0": {"addr": 19, "format": "I", "size": 4, "egu": ""},
    "p_wfmref_end_0": {"addr": 20, "format": "I", "size": 4, "egu": ""},
    "p_wfmref_idx_0": {"addr": 21, "format": "I", "size": 4, "egu": ""},
    "p_wfmref_start_1": {"addr": 22, "format": "I", "size": 4, "egu": ""},
    "p_wfmref_end_1": {"addr": 23, "format": "I", "size": 4, "egu": ""},
    "p_wfmref_idx_1": {"addr": 24, "format": "I", "size": 4, "egu": ""},
    "scope_frequency": {"addr": 25, "format": "f", "size": 4, "egu": "Hz"},
    "scope_duration": {"addr": 26, "format": "f", "size": 4, "egu": "s"},
    "scope source_data": {"addr": 27, "format": "I", "size": 4, "egu": ""},
    "period_sync_pulse": {"addr": 28, "format": "I", "size": 4, "egu": ""},
}
