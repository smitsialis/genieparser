expected_output = {
    "Serial1/0/2:0": {
        "enabled": True,
        "oper_status": "up",
        "ipv4": {
            "10.70.9.252/24": {
                "ip": "10.70.9.252",
                "prefix_length": "24",
                "secondary": False,
                "broadcast_address": "255.255.255.255",
            }
        },
        "address_determined_by": "non-volatile memory",
        "mtu": 1500,
        "helper_address": ["10.70.7.32", "10.68.56.119"],
        "directed_broadcast_forwarding": False,
        "multicast_groups": ["224.0.0.2", "224.0.0.5", "224.0.0.6"],
        "outbound_access_list": "TO_QIMS",
        "inbound_access_list": "FROM_QIMS",
        "proxy_arp": True,
        "local_proxy_arp": False,
        "security_level": "default",
        "split_horizon": True,
        "icmp": {
            "redirects": "always sent",
            "unreachables": "always sent",
            "mask_replies": "never sent",
        },
        "ip_fast_switching": True,
        "ip_flow_switching": False,
        "ip_cef_switching": True,
        "ip_cef_switching_turbo_vector": True,
        "ip_null_turbo_vector": True,
        "unicast_routing_topologies": {"topology": {"base": {"status": "up"}}},
        "ip_multicast_fast_switching": True,
        "ip_multicast_distributed_fast_switching": False,
        "ip_route_cache_flags": ["CEF", "Fast"],
        "router_discovery": False,
        "ip_output_packet_accounting": False,
        "ip_access_violation_accounting": False,
        "tcp_ip_header_compression": False,
        "rtp_ip_header_compression": False,
        "probe_proxy_name_replies": False,
        "policy_routing": False,
        "network_address_translation": False,
        "bgp_policy_mapping": False,
        "input_features": ["Access List", "MCI Check"],
        "wccp": {
            "redirect_outbound": False,
            "redirect_inbound": False,
            "redirect_exclude": False,
        },
    }
}
