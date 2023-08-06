/*
*
SpliceCommand

	These Splice Command types are consolidated into SpliceCommand.

	     0x0: Splice Null,
	     0x5: Splice Insert,
	     0x6: Time Signal,
	     0x7: Bandwidth Reservation,
	     0xff: Private,

*
*/

class SpliceCommand (SCTE35Base):

    def __init__(self, bites=None):
        self.command_length = 0
        self.name   = None                     
        self.command_type  = None            
        self.identifier  = None             
        self.bites=bites                     
        self.splice_event_id  = None
        self.splice_event_cancel_indicator = None
        self.out_of_network_indicator = None
        self.program_splice_flag  = None
        self.duration_flag  = None
        self.break_auto_return  = None
        self.break_duration  = None
        self.splice_immediate_flag = None 
        self.component_count = None 
        self.components=[] 
        self.unique_program_id = None
        self.AvailNum = None
        self.AvailExpected = None
        self.TimeSpecifiedFlag = None
        self.pts_time = None
        self.pts_time_ticks = None

    }

    // Decode returns a Command by type
    def  Decode(selftype uint8, self,bites=None):
            self.command_type = cmdtype
            switch cmdtype {
            case 0x0:
                    self.spliceNull(gob)
            case 0x5:
                    self.spliceInsert(gob)
            case 0x6:
                    self.timeSignal(gob)
            case 0x7:
                    self.bandwidthReservation(gob)
            case 0xff:
                    self.private(gob)
            }

    }

    // bandwidth Reservation
    def  bandwidthReservation(self,bites=None):
            self.name = "Bandwidth Reservation"
            bitbin.forward(0)
    }

    // private Command
    def  private(self,bites=None):
        """
            Table 12 - private_command
        """

        self.name = "Private Command"
        self.identifier = int.from_bytes(
        self.bites[0:3], byteorder="big"
        )  # 3 bytes = 24 bits
        self.bites = self.bites[3:]

  
    // splice Null
    def  spliceNull(self,bites=None):
        """
        Table 7 - splice_null()
        """
        self.name = "Splice Null"
        self.command_type = 0

    def  spliceInsert(self,bites=None):
        """
        Table 9 - splice_insert()
        """
        bitbin = BitBin(self.bites)
        start = bitbin.idx
        self.name = "Splice Insert"
        self.splice_event_id = bitbin.as_hex(32)
        self.splice_event_cancel_indicator = bitbin.as_flag()
        bitbin.forward(7)
        if not self.splice_event_cancel_indicator :
            self.out_of_network_indicator = bitbin.as_flag()
            self.program_splice_flag = bitbin.as_flag()
            self.duration_flag = bitbin.as_flag()
            self.splice_immediate_flag = bitbin.as_flag()
            bitbin.forward(4)
        if self.program_splice_flag == true :
                if not self.splice_immediate_flag :
                    self.spliceTime(gob)
        else :
            self.component_count = bitbin.as_int(8)
            self.components = []
            for i := range(0, self.component_count):
                self.components[i] = bitbin.as_int(8)          
            if not self.splice_immediate_flag:
                self.spliceTime(gob)
            if self.duration_flag == true :
                    self.parseBreak(gob)   
            self.unique_program_id = bitbin.as_int(16)
            self.avail_num = bitbin.as_int(8)
            self.avail_expected = bitbin.as_int(8)
    

    def  parseBreak(self,bites=None):
            self.break_auto_return = bitbin.as_flag(1)()
            bitbin.forward(6)
            self.break_duration = gob.As90k(33)
    

    def  spliceTime(self,bites=None):
            self.time_specified_flag = bitbin.as_flag(1)()
            if self.time_specified_flag :
                    bitbin.forward(6)
                    self.PTS = gob.As90k(33)
             else :
                    bitbin.forward(7)
            
    

    // time Signal
    def  timeSignal(self,bites=None):
            self.name = "Time Signal"
            self.spliceTime(gob)
    

