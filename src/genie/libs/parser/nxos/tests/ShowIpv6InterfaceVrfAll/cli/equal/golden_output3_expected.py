expected_output = {
    "Ethernet2/1": {
        "iod": 36,
        "interface_status": "protocol-up/link-up/admin-up",
        "vrf": "VRF1",
        "enabled": True,
        "ipv6": {
            "2001:db8:1:1::1/64": {
                "ip": "2001:db8:1:1::1",
                "prefix_length": "64",
                "status": "valid",
            },
            "2001:db8:3:3::3/64": {
                "ip": "2001:db8:3:3::3",
                "prefix_length": "64",
                "status": "valid",
            },
            "2001:db8:4:4:a8aa:bbff:feff:8888/64": {
                "ip": "2001:db8:4:4:a8aa:bbff:feff:8888",
                "prefix_length": "64",
                "status": "valid",
            },
            "2001:db8:2:2::2/64": {
                "ip": "2001:db8:2:2::2",
                "prefix_length": "64",
                "status": "valid",
                "anycast": True,
            },
            "ipv6_subnet": "2001:db8:1:1::/64",
            "ipv6_link_local": "fe80::a8aa:bbff:feff:8888 ",
            "ipv6_link_local_state": "default",
            "ipv6_ll_state": "valid",
            "ipv6_virtual_add": "none",
            "ipv6_multicast_routing": "disabled",
            "ipv6_report_link_local": "disabled",
            "ipv6_forwarding_feature": "disabled",
            "multicast_groups": True,
            "ipv6_multicast_groups": [
                "ff02::1",
                "ff02::1:ff00:0",
                "ff02::1:ff00:1",
                "ff02::1:ff00:2",
                "ff02::1:ff00:3",
                "ff02::1:ffbb:cccc",
                "ff02::1:ffbb:cccc",
                "ff02::2",
            ],
            "ipv6_mtu": 1600,
            "ipv6_unicast_rev_path_forwarding": "loose allow default",
            "ipv6_load_sharing": "none",
            "ipv6_last_reset": "never",
            "counters": {
                "unicast_packets_forwarded": 0,
                "unicast_packets_originated": 0,
                "unicast_packets_consumed": 0,
                "unicast_bytes_forwarded": 0,
                "unicast_bytes_originated": 0,
                "unicast_bytes_consumed": 0,
                "multicast_packets_forwarded": 0,
                "multicast_packets_originated": 12,
                "multicast_packets_consumed": 9,
                "multicast_bytes_forwarded": 0,
                "multicast_bytes_originated": 1144,
                "multicast_bytes_consumed": 640,
            },
        },
    }
}