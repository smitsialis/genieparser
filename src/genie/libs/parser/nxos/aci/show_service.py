"""ASR1K implementation of show_service.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use


class ShowServiceRedirInfoGroupSchema(MetaParser):
    """Schema for show service redir info group"""

    schema = {
        'group_id': {
            Any(): {
                'name': {
                    Any(): {
                        'destination': {
                            Any(): {
                                'hg_name': {
                                    Any() : {
                                        'oper_st': str,
                                        'oper_st_qual': str,
                                        'tl': int,
                                        'th': int,
                                        'hp': str,
                                        'tracking': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowServiceRedirInfoGroup(ShowServiceRedirInfoGroupSchema):
    """Parser for show service redir info group"""

    cli_command = 'show service redir info group'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # 366   destgrp-366     dest-[2001:172:16:32::10]-[vxlan-2424832 Not attached    enabled    no-oper-grp     0    0     srconly    no      
        # 367   destgrp-367     dest-[172.16.32.40]-[vxlan-2424832]      shangl-PBR::LB4 disabled   tracked-as-down 0    0     srconly    yes
        # 394   destgrp-394     No valid destinations                    Not attached    disabled   no-oper-grp     0    0     srconly    no      
        p1 = re.compile(r'^(?P<group_id>\d+) +(?P<name>\S+) +(?P<destination>'
                        r'(No +valid +destinations)|(\S+)) +(?P<hg_name>'
                        r'(Not +attached)|(\S+)) +(?P<oper_st>\S+) +'
                        r'(?P<oper_st_qual>\S+) +(?P<tl>\d+) +(?P<th>\d+) +'
                        r'(?P<hp>\S+) +(?P<tracking>\S+)$')

        # dest-[172.16.32.20]-[vxlan-2424832]      shangl-PBR::LB2
        p2 = re.compile(r'^(?P<destination>(No +valid +destinations)|(dest-\S+)) +'
                        r'(?P<hg_name>(Not +attached)|(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # 366   destgrp-366     dest-[2001:172:16:32::10]-[vxlan-2424832 Not attached    enabled    no-oper-grp     0    0     srconly    no      
            # 367   destgrp-367     dest-[172.16.32.40]-[vxlan-2424832]      shangl-PBR::LB4 disabled   tracked-as-down 0    0     srconly    yes
            # 394   destgrp-394     No valid destinations                    Not attached    disabled   no-oper-grp     0    0     srconly    no
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_name_dict = ret_dict.setdefault('group_id', {}). \
                    setdefault(int(group['group_id']), {}). \
                    setdefault('name', {}). \
                    setdefault(group['name'], {})
                destination_dict = group_name_dict. \
                    setdefault('destination', {}). \
                    setdefault(group['destination'], {})
                hg_name_dict = destination_dict. \
                    setdefault('hg_name', {}). \
                    setdefault(group['hg_name'], {})
                hg_name_dict.update({'oper_st': group['oper_st']})
                hg_name_dict.update({'oper_st_qual': group['oper_st_qual']})
                hg_name_dict.update({'tl': group['tl']})
                hg_name_dict.update({'th': group['th']})
                hg_name_dict.update({'hp': group['hp']})
                hg_name_dict.update({'tracking': group['tracking']})
                continue

            # dest-[172.16.32.20]-[vxlan-2424832]      shangl-PBR::LB2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                destination_dict = group_name_dict. \
                    setdefault('destination', {}). \
                    setdefault(group['destination'], {})
                hg_name_dict = destination_dict. \
                    setdefault('hg_name', {}). \
                    setdefault(group['hg_name'], {})
                continue

        return ret_dict
