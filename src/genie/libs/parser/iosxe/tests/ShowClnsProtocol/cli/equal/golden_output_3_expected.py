expected_output = {
    "instance": {
        "null": {
            "process_handle": "0x10000",
            "is_type": "level-1",
            "system_id": "0000.00ff.0002",
            "nsel": "00",
            "manual_area_address": ["47.0002"],
            "routing_for_area_address": ["47.0002"],
            "interfaces": {
                "GigabitEthernet5": {"topology": ["ipv4", "ipv6"]},
                "GigabitEthernet3": {"topology": ["ipv4", "ipv6"]},
                "GigabitEthernet4": {"topology": ["ipv4", "ipv6"]},
                "Loopback0": {"topology": ["ipv4", "ipv6"]},
            },
            "redistribute": "static (on by default)",
            "distance_for_l2_clns_routes": 110,
            "rrr_level": "level-1",
            "metrics": {
                "generate_narrow": "none",
                "accept_narrow": "none",
                "generate_wide": "level-1-2",
                "accept_wide": "level-1-2",
            },
        },
        "default": {
            "process_handle": "0x10001",
            "is_type": "level-1-2",
            "system_id": "0000.0000.0000",
            "nsel": "00",
            "redistribute": "static (on by default)",
            "distance_for_l2_clns_routes": 110,
            "rrr_level": "none",
            "metrics": {
                "generate_narrow": "level-1-2",
                "accept_narrow": "level-1-2",
                "generate_wide": "none",
                "accept_wide": "none",
            },
        },
    }
}
