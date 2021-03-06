expected_output={
    "interface-information": {
        "physical-interface": [
            {
                "active-alarms": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "00:50:56:ff:56:b6",
                "description": "TEST-DESC:1|TEST#1234 DEV",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "00:50:56:ff:56:b6",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:19 UTC (29w6d 18:56 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "148",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "333",
                        "name": "ge-0/0/0.0",
                        "snmp-index": "606",
                        "traffic-statistics": {
                            "input-packets": "133657033",
                            "output-packets": "129243982"
                        }
                    }
                ],
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/0",
                "oper-status": "Up",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "526",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "2952",
                    "input-pps": "5",
                    "output-bps": "3080",
                    "output-pps": "3"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "local-index": "145",
                "logical-interface": [
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "329",
                        "logical-interface-bandwidth": "0",
                        "name": "lc-0/0/0.32769",
                        "snmp-index": "520",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    }
                ],
                "name": "lc-0/0/0",
                "oper-status": "Up",
                "snmp-index": "519",
                "speed": "800mbps",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "local-index": "147",
                "logical-interface": [
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "330",
                        "logical-interface-bandwidth": "0",
                        "name": "pfe-0/0/0.16383",
                        "snmp-index": "523",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    }
                ],
                "name": "pfe-0/0/0",
                "oper-status": "Up",
                "snmp-index": "522",
                "speed": "800mbps",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "local-index": "146",
                "logical-interface": [
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "331",
                        "logical-interface-bandwidth": "0",
                        "name": "pfh-0/0/0.16383",
                        "snmp-index": "524",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "332",
                        "logical-interface-bandwidth": "0",
                        "name": "pfh-0/0/0.16384",
                        "snmp-index": "525",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    }
                ],
                "name": "pfh-0/0/0",
                "oper-status": "Up",
                "snmp-index": "521",
                "speed": "800mbps",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "00:50:56:ff:37:f9",
                "description": "YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "00:50:56:ff:37:f9",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:19 UTC (29w6d 18:56 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "149",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "334",
                        "name": "ge-0/0/1.0",
                        "snmp-index": "605",
                        "traffic-statistics": {
                            "input-packets": "376821627",
                            "output-packets": "370477594"
                        }
                    }
                ],
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/1",
                "oper-status": "Up",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "527",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "3696",
                    "input-pps": "6",
                    "output-bps": "7736",
                    "output-pps": "9"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "00:50:56:ff:1e:ba",
                "description": "ve-hkgasr01_Gi2[DefaultCost1000]",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "00:50:56:ff:1e:ba",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2020-03-05 16:04:34 UTC (2w6d 12:00 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "150",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "336",
                        "name": "ge-0/0/2.0",
                        "snmp-index": "536",
                        "traffic-statistics": {
                            "input-packets": "210359939",
                            "output-packets": "222589463"
                        }
                    }
                ],
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/2",
                "oper-status": "Up",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "528",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "928",
                    "input-pps": "1",
                    "output-bps": "800",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "alarm-not-present": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "00:50:56:ff:93:cb",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "00:50:56:ff:93:cb",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-10-25 08:50:18 UTC (21w5d 19:15 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "151",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "335",
                        "name": "ge-0/0/3.0",
                        "snmp-index": "537",
                        "traffic-statistics": {
                            "input-packets": "14609",
                            "output-packets": "17416"
                        }
                    }
                ],
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/3",
                "oper-status": "Up",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "529",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "00:50:56:ff:3e:28",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "00:50:56:ff:3e:28",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-hardware-down": True,
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-down": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "152",
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/4",
                "oper-status": "Down",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "530",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "2c:6b:f5:ff:01:1d",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "2c:6b:f5:ff:01:1d",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-hardware-down": True,
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-down": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "153",
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/5",
                "oper-status": "Down",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "531",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "2c:6b:f5:ff:01:1e",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "2c:6b:f5:ff:01:1e",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-hardware-down": True,
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-down": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "154",
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/6",
                "oper-status": "Down",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "532",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "2c:6b:f5:ff:01:1f",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "2c:6b:f5:ff:01:1f",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-hardware-down": True,
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-down": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "155",
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/7",
                "oper-status": "Down",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "533",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "2c:6b:f5:ff:01:20",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "2c:6b:f5:ff:01:20",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-hardware-down": True,
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-down": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "156",
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/8",
                "oper-status": "Down",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "534",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "active-alarms": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "active-defects": {
                    "interface-alarms": {
                        "ethernet-alarm-link-down": True
                    }
                },
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "bpdu-error": "None",
                "current-physical-address": "2c:6b:f5:ff:01:21",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "2c:6b:f5:ff:01:21",
                "if-auto-negotiation": "Enabled",
                "if-config-flags": {
                    "iff-hardware-down": True,
                    "iff-snmp-traps": True,
                    "internal-flags": "0x4000"
                },
                "if-device-flags": {
                    "ifdf-down": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-flow-control": "Enabled",
                "if-media-flags": {
                    "ifmf-none": True
                },
                "if-remote-fault": "Online",
                "interface-flapped": {
                    "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                },
                "interface-transmit-statistics": "Disabled",
                "ld-pdu-error": "None",
                "link-level-type": "Ethernet",
                "local-index": "157",
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/9",
                "oper-status": "Down",
                "pad-to-minimum-frame-size": "Disabled",
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "535",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "traffic-statistics": {
                    "input-bps": "0",
                    "input-pps": "0",
                    "output-bps": "0",
                    "output-pps": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:01:29",
                "hardware-physical-address": "2c:6b:f5:ff:01:29",
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Ethernet",
                "link-type": "Full-Duplex",
                "local-index": "129",
                "mtu": "9192",
                "name": "cbp0",
                "oper-status": "Up",
                "snmp-index": "501",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-type": "Full-Duplex",
                "local-index": "128",
                "name": "demux0",
                "oper-status": "Up",
                "snmp-index": "502",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "local-index": "5",
                "name": "dsc",
                "oper-status": "Up",
                "snmp-index": "5",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "00:50:56:ff:e2:c1",
                "hardware-physical-address": "00:50:56:ff:e2:c1",
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "interface-flapped": {
                    "#text": "2019-08-29 09:03:11 UTC (29w6d 19:02 ago)"
                },
                "link-level-type": "Ethernet",
                "local-index": "65",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4000000"
                        },
                        "local-index": "3",
                        "name": "em1.0",
                        "snmp-index": "24",
                        "traffic-statistics": {
                            "input-packets": "724625563",
                            "output-packets": "793953088"
                        }
                    }
                ],
                "mtu": "1514",
                "name": "em1",
                "oper-status": "Up",
                "snmp-index": "23",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "VxLAN-Tunnel-Endpoint",
                "link-type": "Full-Duplex",
                "local-index": "134",
                "mtu": "Unlimited",
                "name": "esi",
                "oper-status": "Up",
                "snmp-index": "503",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "136",
                "mtu": "Unlimited",
                "name": "fti0",
                "oper-status": "Up",
                "snmp-index": "504",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "137",
                "mtu": "Unlimited",
                "name": "fti1",
                "oper-status": "Up",
                "snmp-index": "505",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "138",
                "mtu": "Unlimited",
                "name": "fti2",
                "oper-status": "Up",
                "snmp-index": "506",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "139",
                "mtu": "Unlimited",
                "name": "fti3",
                "oper-status": "Up",
                "snmp-index": "507",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "140",
                "mtu": "Unlimited",
                "name": "fti4",
                "oper-status": "Up",
                "snmp-index": "508",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "141",
                "mtu": "Unlimited",
                "name": "fti5",
                "oper-status": "Up",
                "snmp-index": "509",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "142",
                "mtu": "Unlimited",
                "name": "fti6",
                "oper-status": "Up",
                "snmp-index": "510",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Flexible-tunnel-Interface",
                "link-type": "Full-Duplex",
                "local-index": "143",
                "mtu": "Unlimited",
                "name": "fti7",
                "oper-status": "Up",
                "snmp-index": "511",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "00:50:56:ff:0a:95",
                "hardware-physical-address": "00:50:56:ff:0a:95",
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "interface-flapped": {
                    "#text": "2019-08-29 09:03:11 UTC (29w6d 19:02 ago)"
                },
                "link-level-type": "Ethernet",
                "local-index": "64",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4000000"
                        },
                        "local-index": "4",
                        "name": "fxp0.0",
                        "snmp-index": "13",
                        "traffic-statistics": {
                            "input-packets": "563129",
                            "output-packets": "805208"
                        }
                    }
                ],
                "mtu": "1514",
                "name": "fxp0",
                "oper-status": "Up",
                "snmp-index": "1",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "link-level-type": "GRE",
                "local-index": "10",
                "mtu": "Unlimited",
                "name": "gre",
                "oper-status": "Up",
                "snmp-index": "8",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "link-level-type": "IP-over-IP",
                "local-index": "11",
                "mtu": "Unlimited",
                "name": "ipip",
                "oper-status": "Up",
                "snmp-index": "9",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:08:09",
                "hardware-physical-address": "2c:6b:f5:ff:08:09",
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Ethernet",
                "link-type": "Full-Duplex",
                "local-index": "132",
                "mtu": "1514",
                "name": "irb",
                "oper-status": "Up",
                "snmp-index": "512",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:08:d8",
                "hardware-physical-address": "2c:6b:f5:ff:08:d8",
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Ethernet",
                "link-type": "Full-Duplex",
                "local-index": "144",
                "logical-interface": [
                    {
                        "address-family": [],
                        "encapsulation": "unknown",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x24004000"
                        },
                        "local-index": "325",
                        "logical-interface-bandwidth": "1Gbps",
                        "name": "jsrv.1",
                        "snmp-index": "514",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    }
                ],
                "mtu": "1514",
                "name": "jsrv",
                "oper-status": "Up",
                "snmp-index": "513",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-loopback": True,
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "local-index": "6",
                "logical-interface": [
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "320",
                        "name": "lo0.0",
                        "snmp-index": "16",
                        "traffic-statistics": {
                            "input-packets": "83",
                            "output-packets": "83"
                        }
                    },
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "322",
                        "name": "lo0.16384",
                        "snmp-index": "21",
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0"
                        }
                    },
                    {
                        "address-family": [],
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True
                        },
                        "local-index": "321",
                        "name": "lo0.16385",
                        "snmp-index": "22",
                        "traffic-statistics": {
                            "input-packets": "33920495",
                            "output-packets": "33920495"
                        }
                    }
                ],
                "name": "lo0",
                "oper-status": "Up",
                "snmp-index": "6",
                "traffic-statistics": {
                    "input-packets": "33920578",
                    "output-packets": "33920578"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "LSI",
                "local-index": "4",
                "mtu": "Unlimited",
                "name": "lsi",
                "oper-status": "Up",
                "snmp-index": "4",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "link-level-type": "GRE",
                "local-index": "66",
                "mtu": "Unlimited",
                "name": "mtun",
                "oper-status": "Up",
                "snmp-index": "12",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "link-level-type": "PIM-Decapsulator",
                "local-index": "26",
                "mtu": "Unlimited",
                "name": "pimd",
                "oper-status": "Up",
                "snmp-index": "11",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "link-level-type": "PIM-Encapsulator",
                "local-index": "25",
                "mtu": "Unlimited",
                "name": "pime",
                "oper-status": "Up",
                "snmp-index": "10",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:08:c8",
                "hardware-physical-address": "2c:6b:f5:ff:08:c8",
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Ethernet",
                "link-type": "Full-Duplex",
                "local-index": "130",
                "mtu": "9192",
                "name": "pip0",
                "oper-status": "Up",
                "snmp-index": "515",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "link-level-type": "PPPoE",
                "link-type": "Full-Duplex",
                "local-index": "131",
                "mtu": "1532",
                "name": "pp0",
                "oper-status": "Up",
                "snmp-index": "516"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Remote-BEB",
                "link-type": "Full-Duplex",
                "local-index": "135",
                "mtu": "Unlimited",
                "name": "rbeb",
                "oper-status": "Up",
                "snmp-index": "517",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-config-flags": {
                    "iff-snmp-traps": True
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "Interface-Specific",
                "local-index": "12",
                "mtu": "Unlimited",
                "name": "tap",
                "oper-status": "Up",
                "snmp-index": "7",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True
                },
                "if-media-flags": {
                    "ifmf-none": True
                },
                "interface-flapped": {
                    "#text": "Never"
                },
                "link-level-type": "VxLAN-Tunnel-Endpoint",
                "link-type": "Full-Duplex",
                "local-index": "133",
                "mtu": "Unlimited",
                "name": "vtep",
                "oper-status": "Up",
                "snmp-index": "518",
                "speed": "Unlimited",
                "traffic-statistics": {
                    "input-packets": "0",
                    "output-packets": "0"
                }
            }
        ]
    }
}