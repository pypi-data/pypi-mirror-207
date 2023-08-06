# frame identifiers
FRID_NOTIF_BOOTED                 = 0x01
FRID_NOTIF_ERROR                  = 0x02
FRID_CMD_RESET                    = 0x03
FRID_CMD_TVS_LOAD                 = 0x04
FRID_RESP_TVS_LOAD                = 0x05
FRID_CMD_RULEROW_LOAD             = 0x06
FRID_RESP_RULEROW_LOAD            = 0x07
FRID_CMD_RULE_LOAD                = 0x08
FRID_RESP_RULE_LOAD               = 0x09
FRID_CMD_FOOTPRINT                = 0x0a
FRID_RESP_FOOTPRINT               = 0x0b
FRID_CMD_PACKET_COMPRESS          = 0x0c
FRID_RESP_PACKET_COMPRESS         = 0x0d
FRID_CMD_PACKET_DECOMPRESS        = 0x0e
FRID_RESP_PACKET_DECOMPRESS       = 0x0f

# field identifiers
FID_IPv6_START                    =  0
FID_IPv6_version                  =  1
FID_IPv6_traffic_class            =  2
FID_IPv6_flow_label               =  3
FID_IPv6_payload_length           =  4
FID_IPv6_next_header              =  5
FID_IPv6_hop_limit                =  6
FID_IPv6_source_prefix            =  7
FID_IPv6_source_IID               =  8
FID_IPv6_destination_prefix       =  9
FID_IPv6_destination_IID          = 10
FID_IPv6_END                      = 11
FID_UDP_START                     = 12
FID_UDP_source_port               = 13
FID_UDP_destination_port          = 14
FID_UDP_length                    = 15
FID_UDP_checksum                  = 16
FID_UDP_END                       = 17

# direction
DIR_up                            = 0
DIR_down                          = 1
DIR_bi                            = 2

# Matching Operators (MO) & Compression/Decompression Actions (CDA)
MOCDA_NONE                        = 0
MOCDA_IGNORE_NOTSENT              = 1
MOCDA_EQUAL_NOTSENT               = 2
MOCDA_IGNORE_COMPUTE              = 3
MOCDA_IGNORE_DEVIID               = 4
