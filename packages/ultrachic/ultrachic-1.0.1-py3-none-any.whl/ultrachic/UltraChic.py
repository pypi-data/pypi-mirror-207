# built-in
import sys
import struct
import traceback
# third party
from happyserial import HappySerial
# local
from . import UltraDefines as d
from . import UltraPackets

class UltraChic(object):
    
    BANNER = """
       _ _               ___ _     _      
 /\ /\| | |_ _ __ __ _  / __\ |__ (_) ___ 
/ / \ \ | __| '__/ _` |/ /  | '_ \| |/ __|
\ \_/ / | |_| | | (_| / /___| | | | | (__ 
 \___/|_|\__|_|  \__,_\____/|_| |_|_|\___|
          https://github.com/veryverychic/"""

    def __init__(self):
        print(self.BANNER)
    
        self.clihandlers = dict([
            ('x', self._clihandler_CMD_RESET),
            ('t', self._clihandler_CMD_TVS_LOAD),
            ('o', self._clihandler_CMD_RULEROW_LOAD),
            ('r', self._clihandler_CMD_RULE_LOAD),
            ('f', self._clihandler_CMD_FOOTPRINT),
            ('c', self._clihandler_CMD_PACKET_COMPRESS),
            ('d', self._clihandler_CMD_PACKET_DECOMPRESS),
            ('q', self._clihandler_quit),
        ])
        self.serialhandlers = dict([
            (d.FRID_NOTIF_BOOTED,           self._serialhandler_NOTIF_BOOTED),
            (d.FRID_NOTIF_ERROR,            self._serialhandler_NOTIF_ERROR),
            (d.FRID_RESP_TVS_LOAD,          self._serialhandler_RESP_TVS_LOAD),
            (d.FRID_RESP_RULEROW_LOAD,      self._serialhandler_RESP_RULEROW_LOAD),
            (d.FRID_RESP_RULE_LOAD,         self._serialhandler_RESP_RULE_LOAD),
            (d.FRID_RESP_FOOTPRINT,         self._serialhandler_RESP_FOOTPRINT),
            (d.FRID_RESP_PACKET_COMPRESS,   self._serialhandler_RESP_PACKET_COMPRESS),
            (d.FRID_RESP_PACKET_DECOMPRESS, self._serialhandler_RESP_PACKET_DECOMPRESS),
        ])
        self.happy = HappySerial.HappySerial(
            serialport = 'COM47',
            rx_cb      = self._happyserial_rx_cb,
        )
        
        while True:
            cliinput = input('> ').strip()
            if not cliinput:
               continue
            p = cliinput.split()
            for i in range(len(p)):
                try:
                    p[i] = int(p[i])
                except ValueError:
                    pass
            try:
                self.clihandlers.get(p[0],self._clihandler_unknown)(p[1:])
            except Exception as err:
                print('FAIL: {}\n{}'.format(err,traceback.format_exc()))
            else:
                print('done.')
    
    #=== cli
    
    def _clihandler_CMD_TVS_LOAD(self,params):
        i = params[0]
        print(
            'loading TVs {} with description "{}"'.format(
                i,
                UltraPackets.TVS[i]['description'],
            )
        )
        self.happy.tx([d.FRID_CMD_TVS_LOAD]+UltraPackets.TVS[i]['bytes'])
    
    def _clihandler_CMD_RULEROW_LOAD(self,params):
        i = params[0]
        rrjson = UltraPackets.RULEROWS[i]
        print(
            'loading rulerow {}: {}'.format(
                i,
                rrjson,
            )
        )
        rrbytes = struct.pack(
            '<BBBBBB',
            rrjson['fid'],
            rrjson['fl'],
            rrjson['fp'],
            rrjson['dir'],
            rrjson['tvIdx'],
            rrjson['mocda'],
        )
        self.happy.tx([d.FRID_CMD_RULEROW_LOAD]+list(rrbytes))
    
    def _clihandler_CMD_RULE_LOAD(self,params):
        i = params[0]
        rjson = UltraPackets.RULES[i]
        print(
            'loading rule {}: {}'.format(
                i,
                rjson,
            )
        )
        self.happy.tx(
            [d.FRID_CMD_RULE_LOAD]+ \
            [rjson['ruleId']] + \
            rjson['rulerows']
        )
    
    def _clihandler_CMD_FOOTPRINT(self,params):
        self.happy.tx([d.FRID_CMD_FOOTPRINT])
    
    def _clihandler_CMD_PACKET_COMPRESS(self,params):
        pktId = params[0]
        print(
            'compressing packet "{}" with description "{}"'.format(
                pktId,
                UltraPackets.PACKETS[pktId]['description'],
            )
        )
        self.happy.tx([d.FRID_CMD_PACKET_COMPRESS]+UltraPackets.PACKETS[pktId]['decompressed'])
    
    def _clihandler_CMD_PACKET_DECOMPRESS(self,params):
        self.happy.tx([d.FRID_CMD_PACKET_DECOMPRESS])
    
    def _clihandler_CMD_RESET(self,params):
        self.happy.tx([d.FRID_CMD_RESET])
    
    def _clihandler_quit(self,params):
        sys.exit(0)
    
    def _clihandler_unknown(self):
        print('unknown command')
    
    #=== serial
    
    def _happyserial_rx_cb(self,buf):
        self.serialhandlers[buf[0]](buf[1:])
    
    def _serialhandler_NOTIF_BOOTED(self,msg):
        print('NOTIF_BOOTED          ')
    
    def _serialhandler_NOTIF_ERROR(self,msg):
        print('NOTIF_ERROR             error {}'.format(msg))
    
    def _serialhandler_RESP_TVS_LOAD(self,msg):
        (num_bytes,) = struct.unpack('<H', bytes(msg))
        print('RESP_TVS_LOAD           {} bytes loaded'.format(num_bytes))
    
    def _serialhandler_RESP_RULEROW_LOAD(self,msg):
        (num_rulerows,) = struct.unpack('<H', bytes(msg))
        print('RESP_RULEROW_LOAD       {} rulerows loaded'.format(num_rulerows))
    
    def _serialhandler_RESP_RULE_LOAD(self,msg):
        (num_rules,) = struct.unpack('<H', bytes(msg))
        print('RESP_RULE_LOAD          {} rules loaded'.format(num_rules))
    
    def _serialhandler_RESP_FOOTPRINT(self,msg):
        (num_bytes,) = struct.unpack('<H', bytes(msg))
        print('RESP_FOOTPRINT          {} bytes'.format(num_bytes))
    
    def _serialhandler_RESP_PACKET_COMPRESS(self,msg):
        (duration,)  = struct.unpack('<I', bytes(msg[:4]))
        print('compressed:\n{}'.format(self._format_packet(msg[4:])))
        print('RESP_PACKET_COMPRESS    took {} us'.format(duration))
    
    def _serialhandler_RESP_PACKET_DECOMPRESS(self,msg):
        (duration,)  = struct.unpack('<I', bytes(msg))
        print('RESP_PACKET_DECOMPRESS  took {} us'.format(duration))

    #=== helpers
    
    def _format_packet(self,pkt):
        pktbytes        = ['%02x'%b for b in pkt]
        output          = []
        while pktbytes:
            line        = []
            line       += ['    ']
            line       += [' '.join(pktbytes[:8])]
            line       += ['  ']
            line       += [' '.join(pktbytes[8:16])]
            output     += [''.join(line)]
            pktbytes    = pktbytes[16:]
        output         += ['    ({} bytes)'.format(len(pkt))]
        return '\n'.join(output)
