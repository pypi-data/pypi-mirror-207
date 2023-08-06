# built-in
# third party
# local
from . import UltraDefines as d

TVS = [
    {
        'description': 'default',
        'bytes': [
            6,     # rule: (1) IPv6 Version
            17,    # rule: (1) IPv6 Next Header
            255,   # rule: (1) IPv6 Hop Limit
            0xfe,  # rule: (8) IPv6 DevPrefix / IPv6 AppPrefix
            0x80,  
            0x00,  # rule: (8) IPv6 AppIID / (1) IPv6 Diffserv / (3) IPv6 Flow Label
            0x00,
            0x00, 
            0x00,
            0x00,
            0x00,
            0x00,
            0x01,
            0x00,  # rule (2): UDP DevPort
            123,
            0x00,  # rule (2): UDP AppPort
            124,
        ],
    },
]

RULEROWS = [
    # row 0
    # // |IPv6 Version    |4 |1 |Bi|6        | ignore | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_version,
        'fl'        : 4,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 0,
        'mocda'     : d.MOCDA_IGNORE_NOTSENT,
    },
    # row 1
    # // |IPv6 Diffserv   |8 |1 |Bi|0        | equal  | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_traffic_class,
        'fl'        : 8,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 5,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 2
    # // |IPv6 Flow Label |20|1 |Bi|0        | equal  | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_flow_label,
        'fl'        : 20,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 5,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 3
    # // |IPv6 Length     |16|1 |Bi|         | ignore | compute-*  ||      |
    {
        'fid'       : d.FID_IPv6_payload_length,
        'fl'        : 16,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 0, # don't care
        'mocda'     : d.MOCDA_IGNORE_COMPUTE,
    },
    # row 4
    # // |IPv6 Next Header|8 |1 |Bi|17       | equal  | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_next_header,
        'fl'        : 8,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 1,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 5
    # // |IPv6 Hop Limit  |8 |1 |Bi|255      | ignore | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_hop_limit,
        'fl'        : 8,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 2,
        'mocda'     : d.MOCDA_IGNORE_NOTSENT,
    },
    # row 6
    # // |IPv6 DevPrefix  |64|1 |Bi|FE80::/64| equal  | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_source_prefix,
        'fl'        : 64,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 3,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 7
    # // |IPv6 DevIID     |64|1 |Bi|         | ignore | DevIID     ||      |
    {
        'fid'       : d.FID_IPv6_source_IID,
        'fl'        : 64,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 0, # don't care
        'mocda'     : d.MOCDA_IGNORE_DEVIID,
    },
    # row 8
    # // |IPv6 AppPrefix  |64|1 |Bi|FE80::/64| equal  | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_destination_prefix,
        'fl'        : 64,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 3,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 9
    # // |IPv6 AppIID     |64|1 |Bi|::1      | equal  | not-sent   ||      |
    {
        'fid'       : d.FID_IPv6_destination_IID,
        'fl'        : 64,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 5,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 10
    # // |UDP DevPort     |16|1 |Bi|123      | equal  | not-sent   ||      |
    {
        'fid'       : d.FID_UDP_source_port,
        'fl'        : 16,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 13,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 11
    # // |UDP AppPort     |16|1 |Bi|124      | equal  | not-sent   ||      |
    {
        'fid'       : d.FID_UDP_destination_port,
        'fl'        : 16,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 15,
        'mocda'     : d.MOCDA_EQUAL_NOTSENT,
    },
    # row 12
    # // |UDP Length      |16|1 |Bi|         | ignore | compute-*  ||      |
    {
        'fid'       : d.FID_UDP_length,
        'fl'        : 16,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 0, # don't care
        'mocda'     : d.MOCDA_IGNORE_COMPUTE,
    },
    # row 13
    # // |UDP checksum    |16|1 |Bi|         | ignore | compute-*  ||      |
    {
        'fid'       : d.FID_UDP_checksum,
        'fl'        : 16,
        'fp'        : 1,
        'dir'       : d.DIR_bi,
        'tvIdx'     : 0, # don't care
        'mocda'     : d.MOCDA_IGNORE_COMPUTE,
    },
]

RULES = [
    {
        'ruleId'    : 1,
        'rulerows'  : [0,1,2,3,4,5,6,7,8,9,10,11,12,13],
    },
]

PACKETS = [
    {
        'description': 'matches RFC8724 rule 0',
        'decompressed': [
            # IPv6
            0x60, 0x00, 0x00, 0x00, # word1
            0x00,  8+8,             # payload length
                          18,       # next header << difference
                              0xff, # hop limit
            0xfe, 0x80, 0x00, 0x00, # source prefix
            0x00, 0x00, 0x00, 0x00,
            0x11, 0x22, 0x33, 0x44, # source IID
            0x55, 0x66, 0x77, 0x88,
            0xfe, 0x80, 0x00, 0x00, # destination prefix
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, # destination IID
            0x00, 0x00, 0x00, 0x01,
            # UDP
            0x00,  123,             # source port
                        0x00,  124, # destination port
            0x00,    8,             # length
                        0xaa, 0xbb, # checksum
            # payload
            0x01, 0x02, 0x03, 0x04,
            0x05, 0x06, 0x07, 0x08
        ],
        'compressed': [
            # ruleId
            0x00,
            # IPv6
            0x60, 0x00, 0x00, 0x00, # word1
            0x00,  8+8,             # payload length
                          18,       # next header << difference
                              0xff, # hop limit
            0xfe, 0x80, 0x00, 0x00, # source prefix
            0x00, 0x00, 0x00, 0x00,
            0x11, 0x22, 0x33, 0x44, # source IID
            0x55, 0x66, 0x77, 0x88,
            0xfe, 0x80, 0x00, 0x00, # destination prefix
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, # destination IID
            0x00, 0x00, 0x00, 0x01,
            # UDP
            0x00,  123,             # source port
                        0x00,  124, # destination port
            0x00,    8,             # length
                        0xaa, 0xbb, # checksum
            # payload
            0x01, 0x02, 0x03, 0x04,
            0x05, 0x06, 0x07, 0x08
        ],
    },
    {
        'description': 'matches RFC8724 rule 1',
        'decompressed': [
            # IPv6
            0x60, 0x00, 0x00, 0x00, # word1
            0x00,  8+8,             # payload length
                          17,       # next header
                              0xff, # hop limit
            0xfe, 0x80, 0x00, 0x00, # source prefix
            0x00, 0x00, 0x00, 0x00,
            0x11, 0x22, 0x33, 0x44, # source IID
            0x55, 0x66, 0x77, 0x88,
            0xfe, 0x80, 0x00, 0x00, # destination prefix
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, # destination IID
            0x00, 0x00, 0x00, 0x01,
            # UDP
            0x00,  123,             # source port
                        0x00,  124, # destination port
            0x00,    8,             # length
                        0xaa, 0xbb, # checksum
            # payload
            0x01, 0x02, 0x03, 0x04,
            0x05, 0x06, 0x07, 0x08
        ],
        'compressed': [
            # ruleId
            0x01,
        ],
    },
]
