# built-in
import sys
import struct
import traceback
# third party
from happyserial import HappySerial
# local
from . import UltraDefines as d
from . import UltraPackets

class UltraChicCli(object):
    
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
            ('h', self._clihandler_help),
            ('x', self._clihandler_CMD_RESET),
            ('t', self._clihandler_CMD_TVS_LOAD),
            ('o', self._clihandler_CMD_RULEROWS_LOAD),
            ('r', self._clihandler_CMD_RULES_LOAD),
            ('f', self._clihandler_CMD_FOOTPRINT),
            ('c', self._clihandler_CMD_PACKETS_COMPRESS),
            ('d', self._clihandler_CMD_PACKETS_DECOMPRESS),
            ('q', self._clihandler_quit),
        ])
        self.ultrachic = UltraChic(self._notifcb)
        
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
    
    def _clihandler_help(self,params):
        """this help menu"""
        output          = []
        output         += ['available commands:']
        for (k,v)in self.clihandlers.items():
            output     += [' {}: {}'.format(k,v.__doc__)]
        output          = '\n'.join(output)
        print(output)
    
    def _clihandler_CMD_RESET(self,params):
        """reset the nRF5340-DK"""
        self.ultrachic.reset()
    
    def _clihandler_CMD_TVS_LOAD(self,params):
        """loads all tvs from UltraPackets"""
        for (i,tv) in enumerate(UltraPackets.TVS):
            print('loading TV {} with description "{}"'.format(i,tv['description']))
            resp = self.ultrachic.tv_load(UltraPackets.TVS[i]['bytes'])
            print('response: {}'.format(resp))
    
    def _clihandler_CMD_RULEROWS_LOAD(self,params):
        """loads all rulerows from UltraPackets"""
        for (i,rulerow) in enumerate(UltraPackets.RULEROWS):
            print('loading rulerow {}: {}'.format(i,rulerow))
            resp = self.ultrachic.rulerow_load(rulerow)
            print('response: {}'.format(resp))
    
    def _clihandler_CMD_RULES_LOAD(self,params):
        """loads all rules from UltraPackets"""
        for (i,rule) in enumerate(UltraPackets.RULES):
            print('loading rule {}: {}'.format(i,rule))
            resp = self.ultrachic.rule_load(rule)
            print('response: {}'.format(resp))
    
    def _clihandler_CMD_FOOTPRINT(self,params):
        """retrieves the footprints of the rules"""
        resp = self.ultrachic.footprint()
        print('response: {}'.format(resp))
    
    def _clihandler_CMD_PACKETS_COMPRESS(self,params):
        """compresses all packets from UltraPackets"""
        for (i,packet) in enumerate(UltraPackets.PACKETS):
            print('compressing packet {} with description "{}"'.format(i,packet['description']))
            resp = self.ultrachic.packet_compress(packet['compressed'])
            print('response: {}'.format(resp))
            print(self._format_packet(resp['compressed']))
    
    def _clihandler_CMD_PACKETS_DECOMPRESS(self,params):
        """decompresses all packets from UltraPackets"""
        raise NotImplementedError()
    
    def _clihandler_quit(self,params):
        """quite this application"""
        sys.exit(0)
    
    def _clihandler_unknown(self):
        print('unknown command')
    
    #=== notifications
    
    def _notifcb(self,msg):
        print("notification: {}".format(msg))
    
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

class UltraChic(object):
    
    def __init__(self,notifcb):
        
        # store params
        self.notifcb   = notifcb
        
        # local variables
        self.serialhandlers = dict([
            (d.FRID_NOTIF_BOOTED, self._serialhandler_NOTIF_BOOTED),
            (d.FRID_NOTIF_ERROR,  self._serialhandler_NOTIF_ERROR),
        ])
        self.happy = HappySerial.HappySerial(
            serialport = 'COM47',
            rx_cb      = self._happyserial_rx_cb,
        )
    
    #=== public
    
    def reset(self):
        self.happy.tx(
            [d.FRID_CMD_RESET],
            waitforresponse=True
        )
    
    def tv_load(self,tv):
        resp = self.happy.tx(
            [d.FRID_CMD_TVS_LOAD]+tv,
            waitforresponse=True
        )
        (frid,num_bytes) = struct.unpack('<BH', bytes(resp))
        assert(frid==d.FRID_RESP_TVS_LOAD)
        return {
            'num_bytes': num_bytes,
        }
    
    def rulerow_load(self,rulerow):
        rrbytes = struct.pack(
            '<BBBBBB',
            rulerow['fid'],
            rulerow['fl'],
            rulerow['fp'],
            rulerow['dir'],
            rulerow['tvIdx'],
            rulerow['mocda'],
        )
        resp = self.happy.tx(
            [d.FRID_CMD_RULEROW_LOAD]+list(rrbytes),
            waitforresponse=True
        )
        (frid,num_rulerows) = struct.unpack('<BH', bytes(resp))
        assert(frid==d.FRID_RESP_RULEROW_LOAD)
        return {
            'num_rulerows': num_rulerows,
        }
    
    def rule_load(self,rule):
        resp = self.happy.tx(
            [d.FRID_CMD_RULE_LOAD]+[rule['ruleId']]+rule['rulerows'],
            waitforresponse=True
        )
        (frid,num_rules) = struct.unpack('<BH', bytes(resp))
        assert(frid==d.FRID_RESP_RULE_LOAD)
        return {
            'num_rules': num_rules,
        }
    
    def footprint(self):
        resp = self.happy.tx(
            [d.FRID_CMD_FOOTPRINT],
            waitforresponse=True
        )
        (frid,num_bytes) = struct.unpack('<BH', bytes(resp))
        assert(frid==d.FRID_RESP_FOOTPRINT)
        return {
            'num_bytes': num_bytes,
        }
    
    def packet_compress(self,packet):
        resp = self.happy.tx(
            [d.FRID_CMD_PACKET_COMPRESS]+packet,
            waitforresponse=True
        )
        (frid,duration) = struct.unpack('<BI', bytes(resp[:5]))
        assert(frid==d.FRID_RESP_PACKET_COMPRESS)
        return {
            'duration':   duration,
            'compressed': resp[5:]
        }
    
    def packet_decompress(self,packet):
        raise NotImplementedError()
    
    #=== serial
    
    def _happyserial_rx_cb(self,buf):
        self.serialhandlers[buf[0]](buf[1:])
    
    def _serialhandler_NOTIF_BOOTED(self,msg):
        self.notifcb({
            'notiftype': 'NOTIF_BOOTED',
        })
    
    def _serialhandler_NOTIF_ERROR(self,msg):
        self.notifcb({
            'notiftype': 'NOTIF_ERROR',
            'traceback': msg,
        })
