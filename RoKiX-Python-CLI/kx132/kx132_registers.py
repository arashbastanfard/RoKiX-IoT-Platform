# The MIT License (MIT)
#
# Copyright (c) 2018 Kionix Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
# THE SOFTWARE.
# pylint: skip-file
# The MIT License (MIT)
# Copyright (c) 2017 Kionix Inc.
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
class register_base: pass
class registers(register_base):
	def __init__(self):
		self.KX132_MAN_ID                                         = 0x00         # A burst read (reading using the auto-increment) of 4 bytes starting at address 00, returns the manufacturing ID: "K" "i" "o" "n" in ascii codes "0x4B" "0x69" "0x6F" "0x6E"
		self.KX132_PART_ID                                        = 0x01         # A burst read (reading using the auto-increment) of 2 bytes starting at address 01, returns Who-Am-I value ("WAI") as the first byte (LSB) and a 2nd byte (MSB) that returns silicon specific ID.
		self.KX132_XADP_L                                         = 0x02         # ADP accelerometer output x
		self.KX132_XADP_H                                         = 0x03         
		self.KX132_YADP_L                                         = 0x04         # ADP accelerometer output y
		self.KX132_YADP_H                                         = 0x05         
		self.KX132_ZADP_L                                         = 0x06         # ADP accelerometer output z
		self.KX132_ZADP_H                                         = 0x07         
		self.KX132_XOUT_L                                         = 0x08         # Accelerometer output register x
		self.KX132_XOUT_H                                         = 0x09         
		self.KX132_YOUT_L                                         = 0x0A         # Accelerometeroutput register y
		self.KX132_YOUT_H                                         = 0x0B         
		self.KX132_ZOUT_L                                         = 0x0C         # Accelerometer output register z
		self.KX132_ZOUT_H                                         = 0x0D         
		self.KX132_TEMP_OUT_L                                     = 0x0E         # 16-bit temperature sensor output register
		self.KX132_TEMP_OUT_H                                     = 0x0F         
		self.KX132_PED_STP_L                                      = 0x10         # 16bit pedometer step counter register
		self.KX132_PED_STP_H                                      = 0x11         
		self.KX132_COTR                                           = 0x12         # The Command Test Response (COTR) register is used to verify proper integrated circuit functionality.
		self.KX132_WHO_AM_I                                       = 0x13         # This register can be used for supplier recognition
		self.KX132_TSCP                                           = 0x14         # Current Tilt Position Register.
		self.KX132_TSPP                                           = 0x15         # Previous Tilt Position Register.
		self.KX132_INS1                                           = 0x16         # This register contains 2 step counter interrupts and contains the tap/double tap axis specific interrupts. Data is updated at the ODR settings determined by OTDT<2:0> in CNTL3.
		self.KX132_INS2                                           = 0x17         # This register tells which function caused an interrupt.
		self.KX132_INS3                                           = 0x18         # This register reports the axis and direction of detected motion that triggered the wakeup interrupt.
		self.KX132_STATUS_REG                                     = 0x19         # This register reports the status of the interrupt.
		self.KX132_INT_REL                                        = 0x1A         # Interrupt latch release. Latched interrupt source information (INS1-INS3) is cleared and physical interrupt latched pin is changed to its inactive state when this register is read. WMI, BFI and STPWMI are not cleared by this command.
		self.KX132_CNTL1                                          = 0x1B         # Control register 1. Read/write control register that controls the main feature set.
		self.KX132_CNTL2                                          = 0x1C         # Control register 2. Read/write control register that primarily controls tilt position state enabling.
		self.KX132_CNTL3                                          = 0x1D         # Control register 3. Read/write control register that provides control of the Output Data Rate (ODR) for Tilt, Tap, and Wake-up engines.
		self.KX132_CNTL4                                          = 0x1E         # Control register 4. Read/write control register that provides more feature set control.
		self.KX132_CNTL5                                          = 0x1F         # Control register 5. Read/write control register that provides more feature set control. Note that to properly change the value of this register, the PC1 bit in CNTL1 must first be set to 0.
		self.KX132_CNTL6                                          = 0x20         # Control register 6. Read/write control register that provides more feature set control.
		self.KX132_ODCNTL                                         = 0x21         # Output data control register that configures the acceleration outputs.
		self.KX132_INC1                                           = 0x22         # Interrupt control 1. This register controls the settings for the physical interrupt pin INT1
		self.KX132_INC2                                           = 0x23         # Interrupt control 2. This register controls which axis and direction of detected motion can cause an interrupt.
		self.KX132_INC3                                           = 0x24         # Interrupt control 3. This register controls which axis and direction of tap/double tap can cause an interrupt.
		self.KX132_INC4                                           = 0x25         # Interrupt control 4. This register controls routing of an interrupt reporting to physical interrupt pin INT1
		self.KX132_INC5                                           = 0x26         # Interrupt control 5. This register controls the settings for the physical interrupt pin INT2.
		self.KX132_INC6                                           = 0x27         # Interrupt control 6. This register controls routing of interrupt reporting to physical interrupt pin INT2
		self.KX132_INC7                                           = 0x28         # Interrupt Control 7, for pedometer (step counter)
		self.KX132_TILT_TIMER                                     = 0x29         # This register is the initial count register for the tilt position state timer
		self.KX132_TDTRC                                          = 0x2A         # Tap/Double Tap report control.
		self.KX132_TDTC                                           = 0x2B         # This register contains counter information for the detection of a double tap event.
		self.KX132_TTH                                            = 0x2C         # The Tap Threshold High (TTH) register represents the 8-bit jerk high threshold to determine if a tap is detected
		self.KX132_TTL                                            = 0x2D         # The Tap Threshold Low (TTL) register represents the 8-bit (0-255) jerk low threshold to determine if a tap is detected.
		self.KX132_FTD                                            = 0x2E         # This register contains counter information for the detection of any tap event
		self.KX132_STD                                            = 0x2F         # This register contains counter information for the detection of a double tap event
		self.KX132_TLT                                            = 0x30         # This register contains counter information for the detection of a tap event
		self.KX132_TWS                                            = 0x31         # This register contains counter information for the detection of single and double taps.
		self.KX132_FFTH                                           = 0x32         # Freefall interrupt threshold.
		self.KX132_FFC                                            = 0x33         # Freefall interrupt counter.
		self.KX132_FFCNTL                                         = 0x34         # Freefall interrupt control.
		self.KX132_TILT_ANGLE_LL                                  = 0x37         # Tilt Angle Low Limit: This register sets the low-level threshold for tilt angle detection.
		self.KX132_TILT_ANGLE_HL                                  = 0x38         # Tilt Angle High Limit: This register sets the high-level threshold for tilt angle detection.
		self.KX132_HYST_SET                                       = 0x39         # This register sets the Hysteresis that is placed in between the Screen Rotation states.
		self.KX132_LP_CNTL1                                       = 0x3A         # Low Power Control
		self.KX132_LP_CNTL2                                       = 0x3B         # Low Power Control 2: The advanced low power control setting reduces the power consumption
		self.KX132_WUFTH                                          = 0x49         # Wake-up engine thresholds.
		self.KX132_BTSWUFTH                                       = 0x4A         # Wake-up/Back-to-sleep engine thresholds.
		self.KX132_BTSTH                                          = 0x4B         # Back-to-sleep engine thresholds.
		self.KX132_BTSC                                           = 0x4C         # Debounce counter register for the Back-to-Sleep (BTS) engine.
		self.KX132_WUFC                                           = 0x4D         # Debounce counter register for the Wake-up Function (WUF) engine.
		self.KX132_PED_STPWM_L                                    = 0x51         # Pedometer Step Counter Watermark registers (0x51  0x52) set the 16-bit count value used as a watermark threshold for step counting. When the threshold value is exceeded, the interrupt will be reflected the STPWMI bit in INS1 register and on physical interrupt pin if configured.
		self.KX132_PED_STPWM_H                                    = 0x52         # msb part of pedometer watermark
		self.KX132_PED_CNTL1                                      = 0x53         # Pedometer control register 1
		self.KX132_PED_CNTL2                                      = 0x54         # Pedometer control register 2.
		self.KX132_PED_CNTL3                                      = 0x55         # Pedometer control register 3
		self.KX132_PED_CNTL4                                      = 0x56         # Pedometer control register 4
		self.KX132_PED_CNTL5                                      = 0x57         # Pedometer control register 5
		self.KX132_PED_CNTL6                                      = 0x58         # Pedometer control register 6
		self.KX132_PED_CNTL7                                      = 0x59         # Pedometer control register 7
		self.KX132_PED_CNTL8                                      = 0x5A         # Pedometer control register 8
		self.KX132_PED_CNTL9                                      = 0x5B         # Petormeter control register 9
		self.KX132_PED_CNTL10                                     = 0x5C         # Pedometer control register 10
		self.KX132_SELF_TEST                                      = 0x5D         # Self-Test Enable register:
		self.KX132_BUF_CNTL1                                      = 0x5E         # Sample Threshold  determines the number of samples that will trigger a watermark interrupt or will be saved prior to a trigger event. When BRES=1, the maximum number of samples is 86; when BRES=0, the maximum number of samples is 171. The minimum number of samples must be greater than or equal to 2.
		self.KX132_BUF_CNTL2                                      = 0x5F         # Read/write control register that controls sample buffer operation
		self.KX132_BUF_STATUS_1                                   = 0x60         
		self.KX132_BUF_STATUS_2                                   = 0x61         # This register reports the status of the sample buffer trigger function
		self.KX132_BUF_CLEAR                                      = 0x62         # Latched buffer status information and the entire sample buffer are cleared when any data is written to this register
		self.KX132_BUF_READ                                       = 0x63         # Buffer output register
		self.KX132_ADP_CNTL1                                      = 0x64         # Advanced Data Path (ADP) Output Control register 1.
		self.KX132_ADP_CNTL2                                      = 0x65         # Advanced Data Path (ADP) Control register 2.
		self.KX132_ADP_CNTL3                                      = 0x66         # Advanced Data Path (ADP) Control register 3.
		self.KX132_ADP_CNTL4                                      = 0x67         # Advanced Data Path (ADP) Control registers 4, 5 and 6.
		self.KX132_ADP_CNTL5                                      = 0x68         
		self.KX132_ADP_CNTL6                                      = 0x69         
		self.KX132_ADP_CNTL7                                      = 0x6A         # Advanced Data Path (ADP) Control registers 7, 8 and 9.
		self.KX132_ADP_CNTL8                                      = 0x6B         
		self.KX132_ADP_CNTL9                                      = 0x6C         
		self.KX132_ADP_CNTL10                                     = 0x6D         # Advanced Data Path (ADP) Control register 10.
		self.KX132_ADP_CNTL11                                     = 0x6E         # Advanced Data Path (ADP) Control register 11.
		self.KX132_ADP_CNTL12                                     = 0x6F         # Advanced Data Path (ADP) Control registers 12 and 13.
		self.KX132_ADP_CNTL13                                     = 0x70         # ADP Output Control register 13
		self.KX132_ADP_CNTL14                                     = 0x71         # ADP Output Control register 14
		self.KX132_ADP_CNTL15                                     = 0x72         # ADP Output Control register 15
		self.KX132_ADP_CNTL16                                     = 0x73         # ADP Output Control register 16
		self.KX132_ADP_CNTL17                                     = 0x74         # ADP Output Control register 17
		self.KX132_ADP_CNTL18                                     = 0x75         # ADP Output Control register 18.
		self.KX132_ADP_CNTL19                                     = 0x76         # ADP Output Control register 19.
class bits(register_base):
	def __init__(self):
		self.KX132_COTR_DCSTR_BEFORE                              = (0x55 << 0)  # before set
		self.KX132_COTR_DCSTR_AFTER                               = (0xAA << 0)  # after set
		self.KX132_WHO_AM_I_WAI_ID                                = (0x3D << 0)  # WAI value for KX132
		self.KX132_TSCP_LE                                        = (0x01 << 5)  # Left state X' negative (x-)
		self.KX132_TSCP_RI                                        = (0x01 << 4)  # Right state X' positive (x+)
		self.KX132_TSCP_DO                                        = (0x01 << 3)  # Down state Y' negative (y-)
		self.KX132_TSCP_UP                                        = (0x01 << 2)  # Up state Y' positive (y+)
		self.KX132_TSCP_FD                                        = (0x01 << 1)  # Face Down state Z negative (z-)
		self.KX132_TSCP_FU                                        = (0x01 << 0)  # Face Up Z positive (z+)
		self.KX132_TSPP_LE                                        = (0x01 << 5)  # Left state X' negative (x-)
		self.KX132_TSPP_RI                                        = (0x01 << 4)  # Right state X' positive (x+)
		self.KX132_TSPP_DO                                        = (0x01 << 3)  # Down state Y' negative (y-)
		self.KX132_TSPP_UP                                        = (0x01 << 2)  # Up state Y' positive (y+)
		self.KX132_TSPP_FD                                        = (0x01 << 1)  # Face Down state Z negative (z-)
		self.KX132_TSPP_FU                                        = (0x01 << 0)  # Face Up Z positive (z+)
		self.KX132_INS1_STPOVI                                    = (0x01 << 7)  # Step counter Overflow interrupt. This bit is cleared when the interrupt latch release register (INT_REL) is read
		self.KX132_INS1_STPWMI                                    = (0x01 << 6)  # Step counter Watermark interrupt. This bit is cleared when either the PED_STPL or PED_STPH step count registers is read.
		self.KX132_INS1_TLE                                       = (0x01 << 5)  # X' negative (x-)
		self.KX132_INS1_TRI                                       = (0x01 << 4)  # X' positive (x+)
		self.KX132_INS1_TDO                                       = (0x01 << 3)  # Y' negative (y-)
		self.KX132_INS1_TUP                                       = (0x01 << 2)  # Y' positive (y+)
		self.KX132_INS1_TFD                                       = (0x01 << 1)  # Z  negative (z-)
		self.KX132_INS1_TFU                                       = (0x01 << 0)  # Z  positive (z+)
		self.KX132_INS2_FFS                                       = (0x01 << 7)  # Free fall Status (FFS) bit. This bit is cleared when the interrupt latch release register (INT_REL) is read.
		self.KX132_INS2_BFI                                       = (0x01 << 6)  # Buffer Full Interrupt (BFI) bit indicates that buffer has been filled. This bit is automatically cleared when at least one sample from the buffer is read.
		self.KX132_INS2_WMI                                       = (0x01 << 5)  # Watermark Interrupt bit indicates that user-defined buffers sample threshold (watermark) has been exceeded when in FIFO or Stream modes. Not used in Trigger mode. This bit is automatically cleared when buffer is read and the content is below the watermark.
		self.KX132_INS2_DRDY                                      = (0x01 << 4)  # Data Ready (DRDY) interrupt bit indicates that new acceleration data is available in output data registers 0x08 to 0x0D. This bit is cleared when acceleration data is read or the interrupt latch release register (INT_REL) is read.
		self.KX132_INS2_TDTS_NOTAP                                = (0x00 << 2)  # 00 = no tap
		self.KX132_INS2_TDTS_SINGLE                               = (0x01 << 2)  # 01 = single tap
		self.KX132_INS2_TDTS_DOUBLE                               = (0x02 << 2)  # 10 = double tap
		self.KX132_INS2_TDTS_NA                                   = (0x03 << 2)  # 11 = does not exist
		self.KX132_INS2_STPINCI                                   = (0x01 << 1)  # Step Counter Increment Interrupt bit. This bit is cleared when the interrupt latch release register (INT_REL) is read.
		self.KX132_INS2_TPS                                       = (0x01 << 0)  # Tilt Position Status bit
		self.KX132_INS3_WUFS                                      = (0x01 << 7)  # Wake up interrupt. This bit is cleared when the interrupt latch release register (INT_REL) is read. WUFS = 1  Motion is above wake up threshold, WUFS = 0  Motion is below wake up threshold
		self.KX132_INS3_BTS                                       = (0x01 << 6)  # Back to sleep interrupt. This bit is cleared when the interrupt latch release register (INT_REL) is read. BTS = 1  Motion is below back to sleep threshold, BTS = 0  Motion is above back to sleep threshold
		self.KX132_INS3_XNWU                                      = (0x01 << 5)  # X' negative (x-)
		self.KX132_INS3_XPWU                                      = (0x01 << 4)  # X' positive (x+)
		self.KX132_INS3_YNWU                                      = (0x01 << 3)  # Y' negative (y-)
		self.KX132_INS3_YPWU                                      = (0x01 << 2)  # Y' positive (y+)
		self.KX132_INS3_ZNWU                                      = (0x01 << 1)  # Z  negative (z-)
		self.KX132_INS3_ZPWU                                      = (0x01 << 0)  # Z  positive (z+)
		self.KX132_STATUS_REG_INT                                 = (0x01 << 4)  # reports the combined (OR) interrupt information according to interrupt setting: 0= no interrupt event, 1= interrupt event has occurred.
		self.KX132_STATUS_REG_WAKE                                = (0x01 << 0)  # reports the wake/back to sleep state; 0 = back-to-sleep state,1 = wake state.
		self.KX132_CNTL1_PC1                                      = (0x01 << 7)  # controls the operating mode.  0= stand-by mode,  1= operating mode.
		self.KX132_CNTL1_RES                                      = (0x01 << 6)  # controls the resolution of the accelerometer output. RES = 0 - low power, higher noise mode. RES = 1 - higher power, lower noise mode
		self.KX132_CNTL1_DRDYE                                    = (0x01 << 5)  # enables the data ready engine. DRDYE = 0  disable, DRDYE = 1 - enable
		self.KX132_CNTL1_GSEL_2G                                  = (0x00 << 3)  # 00 = +/- 2g
		self.KX132_CNTL1_GSEL_4G                                  = (0x01 << 3)  # 01 = +/- 4g
		self.KX132_CNTL1_GSEL_8G                                  = (0x02 << 3)  # 10 = +/- 8g
		self.KX132_CNTL1_GSEL_16G                                 = (0x03 << 3)  # 11 = +/- 16g
		self.KX132_CNTL1_TDTE                                     = (0x01 << 2)  # enables the Tap/Double tap engine. TDTE = 0  disable, TDTE = 1  enable
		self.KX132_CNTL1_PDE                                      = (0x01 << 1)  # enables the Pedometer (step-counter) engine. PDE = 0  disabled, PDE = 1  enable
		self.KX132_CNTL1_TPE                                      = (0x01 << 0)  # enables the Tilt engine.TPE = 0  disable, TPE = 1  enable
		self.KX132_CNTL2_SRST                                     = (0x01 << 7)  # The Software Reset bit initiates software reset, which performs the RAM reboot routine. This bit will remain 1 until the RAM reboot routine is finished.
		self.KX132_CNTL2_COTC                                     = (0x01 << 6)  # The Command Test Control bit is used to verify proper ASIC functionality. COTC = 0  no action, COTC = 1  sets AA to COTR register, when the COTR register is read, COTC is cleared and STR = 55.
		self.KX132_CNTL2_LEM                                      = (0x01 << 5)  # Tilt Left state mask
		self.KX132_CNTL2_RIM                                      = (0x01 << 4)  # Tilt Right state mask
		self.KX132_CNTL2_DOM                                      = (0x01 << 3)  # Tilt Down state mask
		self.KX132_CNTL2_UPM                                      = (0x01 << 2)  # Tilt Up state mask
		self.KX132_CNTL2_FDM                                      = (0x01 << 1)  # Tilt Face Down state mask
		self.KX132_CNTL2_FUM                                      = (0x01 << 0)  # Tilt Face Up state mask
		self.KX132_CNTL3_OTP_1P563                                = (0x00 << 6)  # 1.563Hz
		self.KX132_CNTL3_OTP_6P25                                 = (0x01 << 6)  # 6.25Hz
		self.KX132_CNTL3_OTP_12P5                                 = (0x02 << 6)  # 12.5Hz
		self.KX132_CNTL3_OTP_50                                   = (0x03 << 6)  # 50Hz
		self.KX132_CNTL3_OTDT_12P5                                = (0x00 << 3)  # 12.5Hz
		self.KX132_CNTL3_OTDT_25                                  = (0x01 << 3)  # 25Hz
		self.KX132_CNTL3_OTDT_50                                  = (0x02 << 3)  # 50Hz
		self.KX132_CNTL3_OTDT_100                                 = (0x03 << 3)  # 100Hz
		self.KX132_CNTL3_OTDT_200                                 = (0x04 << 3)  # 200Hz
		self.KX132_CNTL3_OTDT_400                                 = (0x05 << 3)  # 400Hz
		self.KX132_CNTL3_OTDT_800                                 = (0x06 << 3)  # 800Hz
		self.KX132_CNTL3_OTDT_1600                                = (0x07 << 3)  # 1600Hz
		self.KX132_CNTL3_OWUF_0P781                               = (0x00 << 0)  # 0.781Hz
		self.KX132_CNTL3_OWUF_1P563                               = (0x01 << 0)  # 1.563Hz
		self.KX132_CNTL3_OWUF_3P125                               = (0x02 << 0)  # 3.125Hz
		self.KX132_CNTL3_OWUF_6P25                                = (0x03 << 0)  # 6.25Hz
		self.KX132_CNTL3_OWUF_12P5                                = (0x04 << 0)  # 12.5Hz
		self.KX132_CNTL3_OWUF_25                                  = (0x05 << 0)  # 25Hz
		self.KX132_CNTL3_OWUF_50                                  = (0x06 << 0)  # 50Hz
		self.KX132_CNTL3_OWUF_100                                 = (0x07 << 0)  # 100Hz
		self.KX132_CNTL4_C_MODE_RESET                             = (0x00 << 7)  # debounce counter is reset if accelerometer data is below threshold
		self.KX132_CNTL4_C_MODE_DECREMENTED                       = (0x01 << 7)  # debounce counter is decremented if accelerometer data is below threshold
		self.KX132_CNTL4_C_MODE                                   = (0x01 << 7)  # defines debounce counter clear mode
		self.KX132_CNTL4_TH_MODE_ABSOLUTE                         = (0x00 << 6)  # absolute threshold
		self.KX132_CNTL4_TH_MODE_RELATIVE                         = (0x01 << 6)  # relative threshold
		self.KX132_CNTL4_TH_MODE                                  = (0x01 << 6)  # defines wake / back-to-sleep threshold mode. TH_MODE = 0  absolute threshold, TH_MODE = 1  relative threshold
		self.KX132_CNTL4_WUFE_DISABLED                            = (0x00 << 5)  # Wake-Up Function Engine is disabled
		self.KX132_CNTL4_WUFE_ENABLED                             = (0x01 << 5)  # Wake-Up Function Engine is enabled
		self.KX132_CNTL4_WUFE                                     = (0x01 << 5)  # Wake-Up Function Engine enable bit
		self.KX132_CNTL4_BTSE_DISABLED                            = (0x00 << 4)  # Back-to-Sleep Engine is disabled
		self.KX132_CNTL4_BTSE_ENABLED                             = (0x01 << 4)  # Back-to-Sleep Engine is enabled
		self.KX132_CNTL4_BTSE                                     = (0x01 << 4)  # Back-to-Sleep Engine enable bit.
		self.KX132_CNTL4_PR_MODE_STANDARD                         = (0x00 << 3)  # standard operation
		self.KX132_CNTL4_PR_MODE_REJECTED                         = (0x01 << 3)  # reject pulse-like motion only in case motion detection in positive and negative directions is enabled (XPWUE and XNWUE bits are set to 1 in INC2 register).
		self.KX132_CNTL4_PR_MODE                                  = (0x01 << 3)  # defines Pulse Reject mode
		self.KX132_CNTL4_OBTS_0P781                               = (0x00 << 0)  # 0.781Hz
		self.KX132_CNTL4_OBTS_1P563                               = (0x01 << 0)  # 1.5623Hz
		self.KX132_CNTL4_OBTS_3P125                               = (0x02 << 0)  # 3.125Hz
		self.KX132_CNTL4_OBTS_6P25                                = (0x03 << 0)  # 6.25Hz
		self.KX132_CNTL4_OBTS_12P5                                = (0x04 << 0)  # 12.5Hz
		self.KX132_CNTL4_OBTS_25                                  = (0x05 << 0)  # 25Hz
		self.KX132_CNTL4_OBTS_50                                  = (0x06 << 0)  # 50Hz
		self.KX132_CNTL4_OBTS_100                                 = (0x07 << 0)  # 100Hz
		self.KX132_CNTL5_ADPE_DISABLED                            = (0x00 << 4)  # ADP disabled
		self.KX132_CNTL5_ADPE_ENABLED                             = (0x01 << 4)  # ADP enabled
		self.KX132_CNTL5_ADPE                                     = (0x01 << 4)  # Advanced Data Path (ADP) enable. ADPE = 0  Advanced Data Path is disabled.  ADPE = 1  Advanced Data Path is enabled. Outputs are available in XADP, YADP, ZADP registers.
		self.KX132_CNTL5_TSE_DISABLED                             = (0x00 << 2)  # temperature sensor disabled
		self.KX132_CNTL5_TSE_ENABLED                              = (0x01 << 2)  # temperature sensor enabled
		self.KX132_CNTL5_TSE                                      = (0x01 << 2)  # enables the Temperature Sensor output TOUT. TSE = 0  temperature sensor output disabled, TSE = 1  temperature sensor output enabled
		self.KX132_CNTL5_MAN_WAKE                                 = (0x01 << 1)  # manual wake-sleep engine overwrite.MAN_WAKE = 0  default, MAN_WAKE = 1  forces wake state (bit is self-cleared)
		self.KX132_CNTL5_MAN_SLEEP                                = (0x01 << 0)  # manual wake-sleep engine overwrite. MAN_SLEEP = 0  default, MAN_SLEEP = 1  forces sleep state (bit is self-cleared)
		self.KX132_CNTL6_I2C_ALE_DISABLED                         = (0x00 << 7)  # I2C auto release function is disabled
		self.KX132_CNTL6_I2C_ALE_ENABLED                          = (0x01 << 7)  # I2C auto release function is enabled
		self.KX132_CNTL6_I2C_ALE                                  = (0x01 << 7)  # enables the I2C auto release function. I2C_ALE = 0  disabled, I2C_ALE = 1  enabled
		self.KX132_CNTL6_I2C_ALC_0P5                              = (0x00 << 0)  # 0.5sec
		self.KX132_CNTL6_I2C_ALC_1P0                              = (0x01 << 0)  # 1.0sec
		self.KX132_CNTL6_I2C_ALC_2P0                              = (0x02 << 0)  # 2.0sec
		self.KX132_CNTL6_I2C_ALC_4P0                              = (0x03 << 0)  # 4.0sec
		self.KX132_ODCNTL_IIR_BYPASS_NOT_BYPASSED                 = (0x00 << 7)  # IIR filter is not bypassed
		self.KX132_ODCNTL_IIR_BYPASS_BYPASSED                     = (0x01 << 7)  # IIR filter is bypassed
		self.KX132_ODCNTL_IIR_BYPASS                              = (0x01 << 7)  # IIR Filter Bypass mode enable bit
		self.KX132_ODCNTL_LPRO_ODR_9                              = (0x00 << 6)  # IIR filter corner frequency set to ODR/9 (default)
		self.KX132_ODCNTL_LPRO_ODR_2                              = (0x01 << 6)  # IIR filter corner frequency set to ODR/2
		self.KX132_ODCNTL_LPRO                                    = (0x01 << 6)  # Low-Pass filter roll off control. LPRO = 0  filter corner frequency set to ODR/9, LPRO = 1  filter corner frequency set to ODR/2
		self.KX132_ODCNTL_FSTUP_DISABLED                          = (0x00 << 5)  # Fast Start is disabled
		self.KX132_ODCNTL_FSTUP_ENABLED                           = (0x01 << 5)  # Fast Start is enabled
		self.KX132_ODCNTL_FSTUP                                   = (0x01 << 5)  # Fast Start Up Enable bit.
		self.KX132_ODCNTL_OSA_0P781                               = (0x00 << 0)  # 0.781Hz  Low power mode available
		self.KX132_ODCNTL_OSA_1P563                               = (0x01 << 0)  # 1.563Hz  Low power mode available
		self.KX132_ODCNTL_OSA_3P125                               = (0x02 << 0)  # 3.125Hz  Low power mode available
		self.KX132_ODCNTL_OSA_6P25                                = (0x03 << 0)  # 6.25Hz  Low power mode available
		self.KX132_ODCNTL_OSA_12P5                                = (0x04 << 0)  # 12.5Hz Low power mode available
		self.KX132_ODCNTL_OSA_25                                  = (0x05 << 0)  # 25Hz  Low power mode available
		self.KX132_ODCNTL_OSA_50                                  = (0x06 << 0)  # 50Hz  Low power mode available
		self.KX132_ODCNTL_OSA_100                                 = (0x07 << 0)  # 100Hz  Low power mode available
		self.KX132_ODCNTL_OSA_200                                 = (0x08 << 0)  # 200Hz  Low power mode available
		self.KX132_ODCNTL_OSA_400                                 = (0x09 << 0)  # 400Hz
		self.KX132_ODCNTL_OSA_800                                 = (0x0A << 0)  # 800Hz
		self.KX132_ODCNTL_OSA_1600                                = (0x0B << 0)  # 1600Hz
		self.KX132_ODCNTL_OSA_3200                                = (0x0C << 0)  # 3200Hz
		self.KX132_ODCNTL_OSA_6400                                = (0x0D << 0)  # 6400Hz
		self.KX132_ODCNTL_OSA_12800                               = (0x0E << 0)  # 12800Hz
		self.KX132_ODCNTL_OSA_25600                               = (0x0F << 0)  # 25600Hz
		self.KX132_INC1_PW1_50US_10US                             = (0x00 << 6)  # 50us(10us when OSA>1600Hz)
		self.KX132_INC1_PW1_1XOSA                                 = (0x01 << 6)  # width 1*OSA period
		self.KX132_INC1_PW1_2XOSA                                 = (0x02 << 6)  # width 2*OSA period
		self.KX132_INC1_PW1_4XOSA                                 = (0x03 << 6)  # width 4*OSA period
		self.KX132_INC1_IEN1                                      = (0x01 << 5)  # enables/disables the physical interrupt pin 1. 0=disable, 1=enable.
		self.KX132_INC1_IEA1                                      = (0x01 << 4)  # Interrupt active level control for interrupt pin 1, 0=active low, 1=active high.
		self.KX132_INC1_IEL1                                      = (0x01 << 3)  # Interrupt latch control for interrupt pin 1, 0=latched, 1=one pulse
		self.KX132_INC1_STPOL                                     = (0x01 << 1)  # sets the polarity of Self Test. STPOL = 0  Negative, STPOL = 1  Positive
		self.KX132_INC1_SPI3E                                     = (0x01 << 0)  # sets the 3-wire SPI interface. SPI3E = 0  disabled, SPI3E = 1  enabled
		self.KX132_INC2_AOI_OR                                    = (0x00 << 6)  # 0=Or combination of selected directions
		self.KX132_INC2_AOI_AND                                   = (0x01 << 6)  # 1=And combination of selected axes
		self.KX132_INC2_AOI                                       = (0x01 << 6)  # And-Or configuration. 0=Or combination of selected directions, 1=And combination of selected axes
		self.KX132_INC2_XNWUE                                     = (0x01 << 5)  # x negative (x-) mask for WUF, 0=disable, 1=enable.
		self.KX132_INC2_XPWUE                                     = (0x01 << 4)  # x positive (x+) mask for WUF, 0=disable, 1=enable.
		self.KX132_INC2_YNWUE                                     = (0x01 << 3)  # y negative (y-) mask for WUF, 0=disable, 1=enable.
		self.KX132_INC2_YPWUE                                     = (0x01 << 2)  # y positive (y+) mask for WUF, 0=disable, 1=enable.
		self.KX132_INC2_ZNWUE                                     = (0x01 << 1)  # z negative (z-) mask for WUF, 0=disable, 1=enable.
		self.KX132_INC2_ZPWUE                                     = (0x01 << 0)  # z positive (z+) mask for WUF, 0=disable, 1=enable.
		self.KX132_INC3_TMEM                                      = (0x01 << 6)  # enables/disables alternate tap masking scheme. TMEN = 0  alternate tap masking scheme disabled, TMEN = 1  alternate tap masking scheme enabled
		self.KX132_INC3_TLEM                                      = (0x01 << 5)  # x negative (x-): 0 = disabled, 1 = enabled
		self.KX132_INC3_TRIM                                      = (0x01 << 4)  # x positive (x+): 0 = disabled, 1 = enabled
		self.KX132_INC3_TDOM                                      = (0x01 << 3)  # y negative (y-): 0 = disabled, 1 = enabled
		self.KX132_INC3_TUPM                                      = (0x01 << 2)  # y positive (y+): 0 = disabled, 1 = enabled
		self.KX132_INC3_TFDM                                      = (0x01 << 1)  # z negative (z-): 0 = disabled, 1 = enabled
		self.KX132_INC3_TFUM                                      = (0x01 << 0)  # z positive (z+): 0 = disabled, 1 = enabled
		self.KX132_INC4_FFI1                                      = (0x01 << 7)  # Free fall interrupt reported on physical interrupt pin 1, 0=disable, 1=enable.
		self.KX132_INC4_BFI1                                      = (0x01 << 6)  # Buffer full interrupt reported on physical interrupt pin 1, 0=disable, 1=enable.
		self.KX132_INC4_WMI1                                      = (0x01 << 5)  # Watermark interrupt reported on physical interrupt pin 1, 0=disable, 1=enable.
		self.KX132_INC4_DRDYI1                                    = (0x01 << 4)  # Data ready interrupt reported on physical interrupt pin 1, 0=disable, 1=enable.
		self.KX132_INC4_BTSI1                                     = (0x01 << 3)  # Back to sleep interrupt reported in interrupt pin 1
		self.KX132_INC4_TDTI1                                     = (0x01 << 2)  # Tap/Double Tap interrupt reported on physical interrupt pin 1, 0=disable, 1=enable.
		self.KX132_INC4_WUFI1                                     = (0x01 << 1)  # Wake Up (motion detect) interrupt reported pn physical interrupt pin 1, 0=disable, 1=enable (and IEN1=1).
		self.KX132_INC4_TPI1                                      = (0x01 << 0)  # Tilt position interrupt reported on physical interrupt pin 1, 0=disable, 1=enable.
		self.KX132_INC5_PW2_50US_10US                             = (0x00 << 6)  # 50us(10us when OSA>1600Hz)
		self.KX132_INC5_PW2_1XODR                                 = (0x01 << 6)  # width 1*OSAperiod
		self.KX132_INC5_PW2_2XODR                                 = (0x02 << 6)  # width 2*OSA period
		self.KX132_INC5_PW2_4XODR                                 = (0x03 << 6)  # width 4*OSA period
		self.KX132_INC5_IEN2                                      = (0x01 << 5)  # enable/disable physical interrupt pin 2, 0=disable, 1=enable.
		self.KX132_INC5_IEA2                                      = (0x01 << 4)  # Interrupt active level control for interrupt pin 2, 0=active low, 1=active high.
		self.KX132_INC5_IEL2                                      = (0x01 << 3)  # Interrupt latch control for interrupt pin 2, 0=latched, 1=one pulse
		self.KX132_INC5_ACLR2                                     = (0x01 << 1)  # Latched interrupt source information(INS1-INS3) is cleared and physical interrupt-1 latched pin is changed to its inactive state at pulse interrupt-1 trailing edge. Note:WMI, BFI, and STPWMI are not auto-cleared by a pulse interrupt trailing edge. ACLR2 = 0  disable, ACLR2 = 1  enable
		self.KX132_INC5_ACLR1                                     = (0x01 << 0)  # Latched interrupt source information(INS1-INS3) is cleared and physical interrupt-1 latched pin is changed to its inactive state at pulse interrupt-2 trailing edge. Note:WMI, BFI, and STPWMI are not auto-cleared by a pulse interrupt trailing edge. ACLR2 = 0  disable, ACLR2 = 1  enable
		self.KX132_INC6_FFI2                                      = (0x01 << 7)  # Free fall interrupt reported on physical interrupt pin INT2. FFI2 = 0  disable, FFI2 = 1  enable
		self.KX132_INC6_BFI2                                      = (0x01 << 6)  # Buffer full interrupt reported on physical interrupt pin INT2. BF2 = 0  disable, BF2 = 1  enable
		self.KX132_INC6_WMI2                                      = (0x01 << 5)  # Watermark interrupt reported on physical interrupt pin INT2. WMI2 = 0  disable, WMI2 = 1  enable
		self.KX132_INC6_DRDYI2                                    = (0x01 << 4)  # Data ready interrupt reported on physical interrupt pin INT2. DRDYI2 = 0  disable, DRDYI2 = 1  enable
		self.KX132_INC6_BTSI2                                     = (0x01 << 3)  # Back to sleep interrupt reported on physical interrupt pin INT2. BTSI2 = 0  disable, BTSI2 = 1  enable
		self.KX132_INC6_TDTI2                                     = (0x01 << 2)  # Tap/Double Tap interrupt reported on physical interrupt pin 2, 0=disable, 1=enable.
		self.KX132_INC6_WUFI2                                     = (0x01 << 1)  # Wake-Up (motion detect) interrupt reported on physical interrupt pin INT2. WUFI2 = 0  disable, WUFI2 = 1  enable
		self.KX132_INC6_TPI2                                      = (0x01 << 0)  # Tilt position interrupt reported on physical interrupt pin INT. TPI2 = 0  disable, TPI2 = 1  enable
		self.KX132_INC7_STPOVI2                                   = (0x01 << 6)  # Step counter overflow interrupt reported on physical interrupt pin INT2. STPOVI2 = 0  disable, STPOVI2 = 1  enable
		self.KX132_INC7_STPWMI2                                   = (0x01 << 5)  # Step counter watermark interrupt reported on physical interrupt pin INT2. STPWMI2 = 0  disable, STPWMI2 = 1  enable
		self.KX132_INC7_STPINCI2                                  = (0x01 << 4)  # Step counter increment interrupt reported on physical interrupt pin INT2. STPINCI2 = 0  disable, STPINCI2 = 1  enable
		self.KX132_INC7_STPOVI1                                   = (0x01 << 2)  # Step counter overflow interrupt reported on physical interrupt pin INT1. STPOVI1 = 0  disable, STPOVI1 = 1  enable
		self.KX132_INC7_STPWMI1                                   = (0x01 << 1)  # Step counter watermark interrupt reported on physical interrupt pin INT1. STPWMI1 = 0  disable, STPWMI1 = 1  enable
		self.KX132_INC7_STPINCI1                                  = (0x01 << 0)  # Step counter increment interrupt reported on physical interrupt pin INT1. STPINCI1 = 0  disable, STPINCI1 = 1  enable
		self.KX132_TDTRC_DTRE                                     = (0x01 << 1)  # enables/disables the double tap interrupt. DTRE = 0  do not update INS1 or DTDS if double tap occurs, DTRE = 1  update INS1 and DTDS in INS2 with double tap events
		self.KX132_TDTRC_STRE                                     = (0x01 << 0)  # enables/disables single tap interrupt. STRE = 0  do not update INS1 or DTDS if single tap occurs, STRE = 1  update INS1 and DTDS in INS2 single tap events
		self.KX132_FFCNTL_FFIE                                    = (0x01 << 7)  # Free fall engine enable. FFIE = 0  disable, FFIE = 1  enable
		self.KX132_FFCNTL_ULMODE                                  = (0x01 << 6)  # Free fall interrupt latch/un-latch control. ULMODE = 0  latched, ULMODE = 1  unlatched
		self.KX132_FFCNTL_FFDC_NO_DELAY                           = (0x00 << 4)  # no delay
		self.KX132_FFCNTL_FFDC_1                                  = (0x01 << 4)  # 1sec
		self.KX132_FFCNTL_FFDC_2                                  = (0x02 << 4)  # 2sec
		self.KX132_FFCNTL_FFDC_4                                  = (0x03 << 4)  # 4sec
		self.KX132_FFCNTL_DCRM                                    = (0x01 << 3)  # Debounce methodology control. DCRM = 0  count up/down, DCRM = 1  count up/reset
		self.KX132_FFCNTL_OFFI_12P5                               = (0x00 << 0)  # 12.5Hz
		self.KX132_FFCNTL_OFFI_25                                 = (0x01 << 0)  # 25Hz
		self.KX132_FFCNTL_OFFI_50                                 = (0x02 << 0)  # 50Hz
		self.KX132_FFCNTL_OFFI_100                                = (0x03 << 0)  # 100Hz
		self.KX132_FFCNTL_OFFI_200                                = (0x04 << 0)  # 200Hz
		self.KX132_FFCNTL_OFFI_400                                = (0x05 << 0)  # 400Hz
		self.KX132_FFCNTL_OFFI_800                                = (0x06 << 0)  # 800Hz
		self.KX132_FFCNTL_OFFI_1600                               = (0x07 << 0)  # 1600Hz
		self.KX132_LP_CNTL1_AVC_NO_AVG                            = (0x00 << 4)  # No Averaging
		self.KX132_LP_CNTL1_AVC_2_SAMPLE_AVG                      = (0x01 << 4)  # 2 Samples Averaged
		self.KX132_LP_CNTL1_AVC_4_SAMPLE_AVG                      = (0x02 << 4)  # 4 Samples Averaged
		self.KX132_LP_CNTL1_AVC_8_SAMPLE_AVG                      = (0x03 << 4)  # 8 Samples Averaged
		self.KX132_LP_CNTL1_AVC_16_SAMPLE_AVG                     = (0x04 << 4)  # 16 Samples Averaged (default)
		self.KX132_LP_CNTL1_AVC_32_SAMPLE_AVG                     = (0x05 << 4)  # 32 Samples Averaged
		self.KX132_LP_CNTL1_AVC_64_SAMPLE_AVG                     = (0x06 << 4)  # 64 Samples Averaged
		self.KX132_LP_CNTL1_AVC_128_SAMPLE_AVG                    = (0x07 << 4)  # 128 Samples Averaged
		self.KX132_LP_CNTL2_LPSTPSEL                              = (0x01 << 0)  # Digital power shut-off select
		self.KX132_PED_CNTL1_STP_TH_NO_STEP                       = (0x00 << 4)  # No threshold count for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_2                        = (0x01 << 4)  # 2 step threshold for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_4                        = (0x02 << 4)  # 4 step threshold for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_6                        = (0x03 << 4)  # 6 step threshold for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_8                        = (0x04 << 4)  # 8 step threshold for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_10                       = (0x05 << 4)  # 10 step threshold for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_12                       = (0x06 << 4)  # 12 step threshold for start counting
		self.KX132_PED_CNTL1_STP_TH_STEP_14                       = (0x07 << 4)  # 14 step threshold for start counting
		self.KX132_PED_CNTL1_MAG_SCALE_0                          = (0x00 << 0)  # 0
		self.KX132_PED_CNTL1_MAG_SCALE_1                          = (0x01 << 0)  # 1
		self.KX132_PED_CNTL1_MAG_SCALE_2                          = (0x02 << 0)  # 2
		self.KX132_PED_CNTL1_MAG_SCALE_3                          = (0x03 << 0)  # 3
		self.KX132_PED_CNTL1_MAG_SCALE_4                          = (0x04 << 0)  # 4
		self.KX132_PED_CNTL1_MAG_SCALE_5                          = (0x05 << 0)  # 5
		self.KX132_PED_CNTL1_MAG_SCALE_6                          = (0x06 << 0)  # 6
		self.KX132_PED_CNTL1_MAG_SCALE_7                          = (0x07 << 0)  # 7
		self.KX132_PED_CNTL1_MAG_SCALE_8                          = (0x08 << 0)  # 8
		self.KX132_PED_CNTL1_MAG_SCALE_9                          = (0x09 << 0)  # 9
		self.KX132_PED_CNTL1_MAG_SCALE_10                         = (0x0A << 0)  # 10
		self.KX132_PED_CNTL1_MAG_SCALE_11                         = (0x0B << 0)  # 11
		self.KX132_PED_CNTL1_MAG_SCALE_12                         = (0x0C << 0)  # 12
		self.KX132_PED_CNTL1_MAG_SCALE_13                         = (0x0D << 0)  # 13
		self.KX132_PED_CNTL1_MAG_SCALE_14                         = (0x0E << 0)  # 14
		self.KX132_PED_CNTL1_MAG_SCALE_15                         = (0x0F << 0)  # 15
		self.KX132_PED_CNTL2_HPS_1                                = (0x00 << 4)  # Scaling factor 1
		self.KX132_PED_CNTL2_HPS_2                                = (0x01 << 4)  # Scaling factor 2
		self.KX132_PED_CNTL2_HPS_4                                = (0x02 << 4)  # Scaling factor 4
		self.KX132_PED_CNTL2_HPS_8                                = (0x03 << 4)  # Scaling factor 8
		self.KX132_PED_CNTL2_HPS_16                               = (0x04 << 4)  # Scaling factor 16
		self.KX132_PED_CNTL2_HPS_32                               = (0x05 << 4)  # Scaling factor 32
		self.KX132_PED_CNTL2_HPS_64                               = (0x06 << 4)  # Scaling factor 64
		self.KX132_PED_CNTL2_HPS_128                              = (0x07 << 4)  # Scaling factor 128
		self.KX132_PED_CNTL2_PED_ODR_50                           = (0x06 << 0)  # Pedometer ODR 50Hz
		self.KX132_PED_CNTL2_PED_ODR_100                          = (0x0C << 0)  # Pedometer ODR 100Hz
		self.KX132_PED_CNTL3_FCB_0                                = (0x00 << 3)  # Scaling factor 0
		self.KX132_PED_CNTL3_FCB_1                                = (0x01 << 3)  # Scaling factor 1
		self.KX132_PED_CNTL3_FCB_2                                = (0x02 << 3)  # Scaling factor 2
		self.KX132_PED_CNTL3_FCB_3                                = (0x03 << 3)  # Scaling factor 3
		self.KX132_PED_CNTL3_FCB_4                                = (0x04 << 3)  # Scaling factor 4
		self.KX132_PED_CNTL3_FCB_5                                = (0x05 << 3)  # Scaling factor 5
		self.KX132_PED_CNTL3_FCB_6                                = (0x06 << 3)  # Scaling factor 6
		self.KX132_PED_CNTL3_FCB_7                                = (0x07 << 3)  # Scaling factor 7
		self.KX132_PED_CNTL3_FCA_1                                = (0x00 << 0)  # Scaling factor 1
		self.KX132_PED_CNTL3_FCA_2                                = (0x01 << 0)  # Scaling factor 2
		self.KX132_PED_CNTL3_FCA_4                                = (0x02 << 0)  # Scaling factor 4
		self.KX132_PED_CNTL3_FCA_8                                = (0x03 << 0)  # Scaling factor 8
		self.KX132_PED_CNTL3_FCA_16                               = (0x04 << 0)  # Scaling factor 16
		self.KX132_PED_CNTL3_FCA_32                               = (0x05 << 0)  # Scaling factor 32
		self.KX132_PED_CNTL3_FCA_64                               = (0x06 << 0)  # Scaling factor 64
		self.KX132_PED_CNTL3_FCA_128                              = (0x07 << 0)  # Scaling factor 128
		self.KX132_PED_CNTL4_B_CNT_0                              = (0x00 << 4)  # Samples below the zero threshold before setting 0
		self.KX132_PED_CNTL4_B_CNT_1                              = (0x01 << 4)  # Samples below the zero threshold before setting 1
		self.KX132_PED_CNTL4_B_CNT_2                              = (0x02 << 4)  # Samples below the zero threshold before setting 2
		self.KX132_PED_CNTL4_B_CNT_3                              = (0x03 << 4)  # Samples below the zero threshold before setting 3
		self.KX132_PED_CNTL4_B_CNT_4                              = (0x04 << 4)  # Samples below the zero threshold before setting 4
		self.KX132_PED_CNTL4_B_CNT_5                              = (0x05 << 4)  # Samples below the zero threshold before setting 5
		self.KX132_PED_CNTL4_B_CNT_6                              = (0x06 << 4)  # Samples below the zero threshold before setting 6
		self.KX132_PED_CNTL4_B_CNT_7                              = (0x07 << 4)  # Samples below the zero threshold before setting 7
		self.KX132_PED_CNTL4_A_H_0                                = (0x00 << 0)  # Maximum area of the peak 0
		self.KX132_PED_CNTL4_A_H_1                                = (0x01 << 0)  # Maximum area of the peak 1
		self.KX132_PED_CNTL4_A_H_2                                = (0x02 << 0)  # Maximum area of the peak 2
		self.KX132_PED_CNTL4_A_H_3                                = (0x03 << 0)  # Maximum area of the peak 3
		self.KX132_PED_CNTL4_A_H_4                                = (0x04 << 0)  # Maximum area of the peak 4
		self.KX132_PED_CNTL4_A_H_5                                = (0x05 << 0)  # Maximum area of the peak 5
		self.KX132_PED_CNTL4_A_H_6                                = (0x06 << 0)  # Maximum area of the peak 6
		self.KX132_PED_CNTL4_A_H_7                                = (0x07 << 0)  # Maximum area of the peak 7
		self.KX132_PED_CNTL4_A_H_8                                = (0x08 << 0)  # Maximum area of the peak 8
		self.KX132_PED_CNTL4_A_H_9                                = (0x09 << 0)  # Maximum area of the peak 9
		self.KX132_PED_CNTL4_A_H_10                               = (0x0A << 0)  # Maximum area of the peak 10
		self.KX132_PED_CNTL4_A_H_11                               = (0x0B << 0)  # Maximum area of the peak 11
		self.KX132_PED_CNTL4_A_H_12                               = (0x0C << 0)  # Maximum area of the peak 12
		self.KX132_PED_CNTL4_A_H_13                               = (0x0D << 0)  # Maximum area of the peak 13
		self.KX132_PED_CNTL4_A_H_14                               = (0x0E << 0)  # Maximum area of the peak 14
		self.KX132_PED_CNTL4_A_H_15                               = (0x0F << 0)  # Maximum area of the peak 15
		self.KX132_SELF_TEST_MEMS_TEST_ST_OFF                     = (0x00 << 0)  # Self test off
		self.KX132_SELF_TEST_MEMS_TEST_ST_ON                      = (0xCA << 0)  # Self test on
		self.KX132_BUF_CNTL2_BUFE                                 = (0x01 << 7)  # controls activation of the sample buffer. BUFE = 0  sample buffer inactive, BUFE = 1  sample buffer active
		self.KX132_BUF_CNTL2_BRES                                 = (0x01 << 6)  # determines the resolution of the acceleration data samples collected by the sample buffer. BRES = 0  8-bit samples are accumulated in the buffer, BRES = 1  16-bit samples are accumulated in the buffer
		self.KX132_BUF_CNTL2_BFIE                                 = (0x01 << 5)  # buffer full interrupt enable bit. BFIE = 0  buffer full interrupt is disabled, BFIE = 1  buffer full interrupt is enabled and updated in INS2
		self.KX132_BUF_CNTL2_BM_FIFO                              = (0x00 << 0)  # The buffer collects 681 sets of 8-bit low resolution values or 339 sets of 16-bit high resolution values and then stops collecting data, collecting new data only when the buffer is not full
		self.KX132_BUF_CNTL2_BM_STREAM                            = (0x01 << 0)  # The buffer holds the last 681 sets of 8-bit low resolution values or 339 sets of 16-bit high resolution values. Once the buffer is full, the oldest data is discarded to make room for newer data.
		self.KX132_BUF_CNTL2_BM_TRIGGER                           = (0x02 << 0)  # When a trigger event occurs, the buffer holds the last data set of SMP[9:0] samples before the trigger event and then continues to collect data until full. New data is collected only when the buffer is not full.
		self.KX132_BUF_CNTL2_BM_NA                                = (0x03 << 0)  # Not applicable
		self.KX132_BUF_STATUS_2_BUF_TRIG                          = (0x01 << 7)  # reports the status of the buffers trigger function if this mode has been selected
		self.KX132_ADP_CNTL1_RMS_AVC_2_SAMPLE_AVG                 = (0x00 << 4)  # 2 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_4_SAMPLE_AVG                 = (0x01 << 4)  # 4 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_8_SAMPLE_AVG                 = (0x02 << 4)  # 8 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_16_SAMPLE_AVG                = (0x03 << 4)  # 16 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_32_SAMPLE_AVG                = (0x04 << 4)  # 32 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_64_SAMPLE_AVG                = (0x05 << 4)  # 64 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_128_SAMPLE_AVG               = (0x06 << 4)  # 128 Samples Averaged
		self.KX132_ADP_CNTL1_RMS_AVC_256_SAMPLE_AVG               = (0x07 << 4)  # 256 Samples Averaged
		self.KX132_ADP_CNTL1_OADP_0P781                           = (0x00 << 0)  # 0.781Hz
		self.KX132_ADP_CNTL1_OADP_1P563                           = (0x01 << 0)  # 1.563Hz
		self.KX132_ADP_CNTL1_OADP_3P125                           = (0x02 << 0)  # 3.125Hz
		self.KX132_ADP_CNTL1_OADP_6P25                            = (0x03 << 0)  # 6.25Hz
		self.KX132_ADP_CNTL1_OADP_12P5                            = (0x04 << 0)  # 12.5Hz
		self.KX132_ADP_CNTL1_OADP_25                              = (0x05 << 0)  # 25Hz
		self.KX132_ADP_CNTL1_OADP_50                              = (0x06 << 0)  # 50Hz
		self.KX132_ADP_CNTL1_OADP_100                             = (0x07 << 0)  # 100Hz
		self.KX132_ADP_CNTL1_OADP_200                             = (0x08 << 0)  # 200Hz
		self.KX132_ADP_CNTL1_OADP_400                             = (0x09 << 0)  # 400Hz
		self.KX132_ADP_CNTL1_OADP_800                             = (0x0A << 0)  # 800Hz
		self.KX132_ADP_CNTL1_OADP_1600                            = (0x0B << 0)  # 1600Hz
		self.KX132_ADP_CNTL1_OADP_3200                            = (0x0C << 0)  # 3200Hz
		self.KX132_ADP_CNTL1_OADP_6400                            = (0x0D << 0)  # 6400Hz
		self.KX132_ADP_CNTL1_OADP_12800                           = (0x0E << 0)  # 12800Hz
		self.KX132_ADP_CNTL1_OADP_25600                           = (0x0F << 0)  # 25600Hz
		self.KX132_ADP_CNTL2_ADP_BUF_SEL                          = (0x01 << 7)  # Select data to be routed to the sample buffer
		self.KX132_ADP_CNTL2_ADP_WB_ISEL                          = (0x01 << 6)  # Input select for the Wake-up/Back-to-Sleep engines
		self.KX132_ADP_CNTL2_RMS_WB_OSEL                          = (0x01 << 5)  # Select data out to the WUF/BTS engines.
		self.KX132_ADP_CNTL2_ADP_FLT2_BYP                         = (0x01 << 4)  # Advanced Data Path Filter-2 bypass control
		self.KX132_ADP_CNTL2_ADP_FLT1_BYP                         = (0x01 << 3)  # Advanced Data Path Filter-1 bypass control
		self.KX132_ADP_CNTL2_ADP_RMS_OSEL                         = (0x01 << 1)  # Select data out to XADP, YADP, and ZADP registers.
		self.KX132_ADP_CNTL2_ADP_F2_HP                            = (0x01 << 0)  # Filter-2 High-pass enable. 0  Filter-2 is set to Low-pass filter. 1  Filter-2 is set to High-pass filter
		self.KX132_ADP_CNTL11_ADP_F1_OSH                          = (0x01 << 7)  # ADP filter-1 output scale shift value
_b=bits()
class enums(register_base):
	def __init__(self):
		self.KX132_INC2_AOI={
			'AND':_b.KX132_INC2_AOI_AND,
			'OR':_b.KX132_INC2_AOI_OR,
		}
		self.KX132_PED_CNTL1_MAG_SCALE={
			'11':_b.KX132_PED_CNTL1_MAG_SCALE_11,
			'10':_b.KX132_PED_CNTL1_MAG_SCALE_10,
			'13':_b.KX132_PED_CNTL1_MAG_SCALE_13,
			'12':_b.KX132_PED_CNTL1_MAG_SCALE_12,
			'15':_b.KX132_PED_CNTL1_MAG_SCALE_15,
			'14':_b.KX132_PED_CNTL1_MAG_SCALE_14,
			'1':_b.KX132_PED_CNTL1_MAG_SCALE_1,
			'0':_b.KX132_PED_CNTL1_MAG_SCALE_0,
			'3':_b.KX132_PED_CNTL1_MAG_SCALE_3,
			'2':_b.KX132_PED_CNTL1_MAG_SCALE_2,
			'5':_b.KX132_PED_CNTL1_MAG_SCALE_5,
			'4':_b.KX132_PED_CNTL1_MAG_SCALE_4,
			'7':_b.KX132_PED_CNTL1_MAG_SCALE_7,
			'6':_b.KX132_PED_CNTL1_MAG_SCALE_6,
			'9':_b.KX132_PED_CNTL1_MAG_SCALE_9,
			'8':_b.KX132_PED_CNTL1_MAG_SCALE_8,
		}
		self.KX132_ODCNTL_LPRO={
			'ODR_9':_b.KX132_ODCNTL_LPRO_ODR_9,
			'ODR_2':_b.KX132_ODCNTL_LPRO_ODR_2,
		}
		self.KX132_PED_CNTL2_HPS={
			'16':_b.KX132_PED_CNTL2_HPS_16,
			'32':_b.KX132_PED_CNTL2_HPS_32,
			'1':_b.KX132_PED_CNTL2_HPS_1,
			'2':_b.KX132_PED_CNTL2_HPS_2,
			'64':_b.KX132_PED_CNTL2_HPS_64,
			'4':_b.KX132_PED_CNTL2_HPS_4,
			'128':_b.KX132_PED_CNTL2_HPS_128,
			'8':_b.KX132_PED_CNTL2_HPS_8,
		}
		self.KX132_INC1_PW1={
			'50US_10US':_b.KX132_INC1_PW1_50US_10US,
			'2XOSA':_b.KX132_INC1_PW1_2XOSA,
			'4XOSA':_b.KX132_INC1_PW1_4XOSA,
			'1XOSA':_b.KX132_INC1_PW1_1XOSA,
		}
		self.KX132_ADP_CNTL1_OADP={
			'200':_b.KX132_ADP_CNTL1_OADP_200,
			'6400':_b.KX132_ADP_CNTL1_OADP_6400,
			'0P781':_b.KX132_ADP_CNTL1_OADP_0P781,
			'3200':_b.KX132_ADP_CNTL1_OADP_3200,
			'12P5':_b.KX132_ADP_CNTL1_OADP_12P5,
			'1600':_b.KX132_ADP_CNTL1_OADP_1600,
			'50':_b.KX132_ADP_CNTL1_OADP_50,
			'1P563':_b.KX132_ADP_CNTL1_OADP_1P563,
			'25600':_b.KX132_ADP_CNTL1_OADP_25600,
			'3P125':_b.KX132_ADP_CNTL1_OADP_3P125,
			'25':_b.KX132_ADP_CNTL1_OADP_25,
			'12800':_b.KX132_ADP_CNTL1_OADP_12800,
			'400':_b.KX132_ADP_CNTL1_OADP_400,
			'100':_b.KX132_ADP_CNTL1_OADP_100,
			'800':_b.KX132_ADP_CNTL1_OADP_800,
			'6P25':_b.KX132_ADP_CNTL1_OADP_6P25,
		}
		self.KX132_CNTL4_C_MODE={
			'RESET':_b.KX132_CNTL4_C_MODE_RESET,
			'DECREMENTED':_b.KX132_CNTL4_C_MODE_DECREMENTED,
		}
		self.KX132_CNTL4_PR_MODE={
			'REJECTED':_b.KX132_CNTL4_PR_MODE_REJECTED,
			'STANDARD':_b.KX132_CNTL4_PR_MODE_STANDARD,
		}
		self.KX132_FFCNTL_FFDC={
			'1':_b.KX132_FFCNTL_FFDC_1,
			'2':_b.KX132_FFCNTL_FFDC_2,
			'NO_DELAY':_b.KX132_FFCNTL_FFDC_NO_DELAY,
			'4':_b.KX132_FFCNTL_FFDC_4,
		}
		self.KX132_INS2_TDTS={
			'DOUBLE':_b.KX132_INS2_TDTS_DOUBLE,
			'SINGLE':_b.KX132_INS2_TDTS_SINGLE,
			'NOTAP':_b.KX132_INS2_TDTS_NOTAP,
			'NA':_b.KX132_INS2_TDTS_NA,
		}
		self.KX132_FFCNTL_OFFI={
			'25':_b.KX132_FFCNTL_OFFI_25,
			'200':_b.KX132_FFCNTL_OFFI_200,
			'12P5':_b.KX132_FFCNTL_OFFI_12P5,
			'1600':_b.KX132_FFCNTL_OFFI_1600,
			'50':_b.KX132_FFCNTL_OFFI_50,
			'400':_b.KX132_FFCNTL_OFFI_400,
			'100':_b.KX132_FFCNTL_OFFI_100,
			'800':_b.KX132_FFCNTL_OFFI_800,
		}
		self.KX132_CNTL4_OBTS={
			'25':_b.KX132_CNTL4_OBTS_25,
			'0P781':_b.KX132_CNTL4_OBTS_0P781,
			'12P5':_b.KX132_CNTL4_OBTS_12P5,
			'50':_b.KX132_CNTL4_OBTS_50,
			'1P563':_b.KX132_CNTL4_OBTS_1P563,
			'3P125':_b.KX132_CNTL4_OBTS_3P125,
			'100':_b.KX132_CNTL4_OBTS_100,
			'6P25':_b.KX132_CNTL4_OBTS_6P25,
		}
		self.KX132_ODCNTL_IIR_BYPASS={
			'NOT_BYPASSED':_b.KX132_ODCNTL_IIR_BYPASS_NOT_BYPASSED,
			'BYPASSED':_b.KX132_ODCNTL_IIR_BYPASS_BYPASSED,
		}
		self.KX132_BUF_CNTL2_BM={
			'NA':_b.KX132_BUF_CNTL2_BM_NA,
			'TRIGGER':_b.KX132_BUF_CNTL2_BM_TRIGGER,
			'FIFO':_b.KX132_BUF_CNTL2_BM_FIFO,
			'STREAM':_b.KX132_BUF_CNTL2_BM_STREAM,
		}
		self.KX132_ADP_CNTL1_RMS_AVC={
			'4_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_4_SAMPLE_AVG,
			'16_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_16_SAMPLE_AVG,
			'256_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_256_SAMPLE_AVG,
			'8_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_8_SAMPLE_AVG,
			'2_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_2_SAMPLE_AVG,
			'128_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_128_SAMPLE_AVG,
			'64_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_64_SAMPLE_AVG,
			'32_SAMPLE_AVG':_b.KX132_ADP_CNTL1_RMS_AVC_32_SAMPLE_AVG,
		}
		self.KX132_PED_CNTL4_B_CNT={
			'1':_b.KX132_PED_CNTL4_B_CNT_1,
			'0':_b.KX132_PED_CNTL4_B_CNT_0,
			'3':_b.KX132_PED_CNTL4_B_CNT_3,
			'2':_b.KX132_PED_CNTL4_B_CNT_2,
			'5':_b.KX132_PED_CNTL4_B_CNT_5,
			'4':_b.KX132_PED_CNTL4_B_CNT_4,
			'7':_b.KX132_PED_CNTL4_B_CNT_7,
			'6':_b.KX132_PED_CNTL4_B_CNT_6,
		}
		self.KX132_CNTL3_OWUF={
			'25':_b.KX132_CNTL3_OWUF_25,
			'0P781':_b.KX132_CNTL3_OWUF_0P781,
			'12P5':_b.KX132_CNTL3_OWUF_12P5,
			'50':_b.KX132_CNTL3_OWUF_50,
			'1P563':_b.KX132_CNTL3_OWUF_1P563,
			'3P125':_b.KX132_CNTL3_OWUF_3P125,
			'100':_b.KX132_CNTL3_OWUF_100,
			'6P25':_b.KX132_CNTL3_OWUF_6P25,
		}
		self.KX132_PED_CNTL4_A_H={
			'11':_b.KX132_PED_CNTL4_A_H_11,
			'10':_b.KX132_PED_CNTL4_A_H_10,
			'13':_b.KX132_PED_CNTL4_A_H_13,
			'12':_b.KX132_PED_CNTL4_A_H_12,
			'15':_b.KX132_PED_CNTL4_A_H_15,
			'14':_b.KX132_PED_CNTL4_A_H_14,
			'1':_b.KX132_PED_CNTL4_A_H_1,
			'0':_b.KX132_PED_CNTL4_A_H_0,
			'3':_b.KX132_PED_CNTL4_A_H_3,
			'2':_b.KX132_PED_CNTL4_A_H_2,
			'5':_b.KX132_PED_CNTL4_A_H_5,
			'4':_b.KX132_PED_CNTL4_A_H_4,
			'7':_b.KX132_PED_CNTL4_A_H_7,
			'6':_b.KX132_PED_CNTL4_A_H_6,
			'9':_b.KX132_PED_CNTL4_A_H_9,
			'8':_b.KX132_PED_CNTL4_A_H_8,
		}
		self.KX132_LP_CNTL1_AVC={
			'4_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_4_SAMPLE_AVG,
			'16_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_16_SAMPLE_AVG,
			'8_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_8_SAMPLE_AVG,
			'NO_AVG':_b.KX132_LP_CNTL1_AVC_NO_AVG,
			'128_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_128_SAMPLE_AVG,
			'2_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_2_SAMPLE_AVG,
			'64_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_64_SAMPLE_AVG,
			'32_SAMPLE_AVG':_b.KX132_LP_CNTL1_AVC_32_SAMPLE_AVG,
		}
		self.KX132_SELF_TEST_MEMS_TEST={
			'ST_OFF':_b.KX132_SELF_TEST_MEMS_TEST_ST_OFF,
			'ST_ON':_b.KX132_SELF_TEST_MEMS_TEST_ST_ON,
		}
		self.KX132_PED_CNTL1_STP_TH={
			'NO_STEP':_b.KX132_PED_CNTL1_STP_TH_NO_STEP,
			'STEP_2':_b.KX132_PED_CNTL1_STP_TH_STEP_2,
			'STEP_10':_b.KX132_PED_CNTL1_STP_TH_STEP_10,
			'STEP_14':_b.KX132_PED_CNTL1_STP_TH_STEP_14,
			'STEP_12':_b.KX132_PED_CNTL1_STP_TH_STEP_12,
			'STEP_8':_b.KX132_PED_CNTL1_STP_TH_STEP_8,
			'STEP_6':_b.KX132_PED_CNTL1_STP_TH_STEP_6,
			'STEP_4':_b.KX132_PED_CNTL1_STP_TH_STEP_4,
		}
		self.KX132_PED_CNTL3_FCA={
			'16':_b.KX132_PED_CNTL3_FCA_16,
			'32':_b.KX132_PED_CNTL3_FCA_32,
			'1':_b.KX132_PED_CNTL3_FCA_1,
			'2':_b.KX132_PED_CNTL3_FCA_2,
			'64':_b.KX132_PED_CNTL3_FCA_64,
			'4':_b.KX132_PED_CNTL3_FCA_4,
			'128':_b.KX132_PED_CNTL3_FCA_128,
			'8':_b.KX132_PED_CNTL3_FCA_8,
		}
		self.KX132_PED_CNTL3_FCB={
			'1':_b.KX132_PED_CNTL3_FCB_1,
			'0':_b.KX132_PED_CNTL3_FCB_0,
			'3':_b.KX132_PED_CNTL3_FCB_3,
			'2':_b.KX132_PED_CNTL3_FCB_2,
			'5':_b.KX132_PED_CNTL3_FCB_5,
			'4':_b.KX132_PED_CNTL3_FCB_4,
			'7':_b.KX132_PED_CNTL3_FCB_7,
			'6':_b.KX132_PED_CNTL3_FCB_6,
		}
		self.KX132_CNTL4_WUFE={
			'DISABLED':_b.KX132_CNTL4_WUFE_DISABLED,
			'ENABLED':_b.KX132_CNTL4_WUFE_ENABLED,
		}
		self.KX132_COTR_DCSTR={
			'AFTER':_b.KX132_COTR_DCSTR_AFTER,
			'BEFORE':_b.KX132_COTR_DCSTR_BEFORE,
		}
		self.KX132_PED_CNTL2_PED_ODR={
			'100':_b.KX132_PED_CNTL2_PED_ODR_100,
			'50':_b.KX132_PED_CNTL2_PED_ODR_50,
		}
		self.KX132_ODCNTL_OSA={
			'200':_b.KX132_ODCNTL_OSA_200,
			'6400':_b.KX132_ODCNTL_OSA_6400,
			'0P781':_b.KX132_ODCNTL_OSA_0P781,
			'3200':_b.KX132_ODCNTL_OSA_3200,
			'12P5':_b.KX132_ODCNTL_OSA_12P5,
			'1600':_b.KX132_ODCNTL_OSA_1600,
			'50':_b.KX132_ODCNTL_OSA_50,
			'1P563':_b.KX132_ODCNTL_OSA_1P563,
			'25600':_b.KX132_ODCNTL_OSA_25600,
			'3P125':_b.KX132_ODCNTL_OSA_3P125,
			'25':_b.KX132_ODCNTL_OSA_25,
			'12800':_b.KX132_ODCNTL_OSA_12800,
			'400':_b.KX132_ODCNTL_OSA_400,
			'100':_b.KX132_ODCNTL_OSA_100,
			'800':_b.KX132_ODCNTL_OSA_800,
			'6P25':_b.KX132_ODCNTL_OSA_6P25,
		}
		self.KX132_INC5_PW2={
			'50US_10US':_b.KX132_INC5_PW2_50US_10US,
			'4XODR':_b.KX132_INC5_PW2_4XODR,
			'1XODR':_b.KX132_INC5_PW2_1XODR,
			'2XODR':_b.KX132_INC5_PW2_2XODR,
		}
		self.KX132_CNTL1_GSEL={
			'4G':_b.KX132_CNTL1_GSEL_4G,
			'2G':_b.KX132_CNTL1_GSEL_2G,
			'8G':_b.KX132_CNTL1_GSEL_8G,
			'16G':_b.KX132_CNTL1_GSEL_16G,
		}
		self.KX132_CNTL6_I2C_ALE={
			'DISABLED':_b.KX132_CNTL6_I2C_ALE_DISABLED,
			'ENABLED':_b.KX132_CNTL6_I2C_ALE_ENABLED,
		}
		self.KX132_ODCNTL_FSTUP={
			'DISABLED':_b.KX132_ODCNTL_FSTUP_DISABLED,
			'ENABLED':_b.KX132_ODCNTL_FSTUP_ENABLED,
		}
		self.KX132_CNTL6_I2C_ALC={
			'2P0':_b.KX132_CNTL6_I2C_ALC_2P0,
			'1P0':_b.KX132_CNTL6_I2C_ALC_1P0,
			'0P5':_b.KX132_CNTL6_I2C_ALC_0P5,
			'4P0':_b.KX132_CNTL6_I2C_ALC_4P0,
		}
		self.KX132_CNTL4_BTSE={
			'DISABLED':_b.KX132_CNTL4_BTSE_DISABLED,
			'ENABLED':_b.KX132_CNTL4_BTSE_ENABLED,
		}
		self.KX132_CNTL4_TH_MODE={
			'RELATIVE':_b.KX132_CNTL4_TH_MODE_RELATIVE,
			'ABSOLUTE':_b.KX132_CNTL4_TH_MODE_ABSOLUTE,
		}
		self.KX132_CNTL3_OTP={
			'1P563':_b.KX132_CNTL3_OTP_1P563,
			'12P5':_b.KX132_CNTL3_OTP_12P5,
			'6P25':_b.KX132_CNTL3_OTP_6P25,
			'50':_b.KX132_CNTL3_OTP_50,
		}
		self.KX132_CNTL5_TSE={
			'DISABLED':_b.KX132_CNTL5_TSE_DISABLED,
			'ENABLED':_b.KX132_CNTL5_TSE_ENABLED,
		}
		self.KX132_CNTL3_OTDT={
			'25':_b.KX132_CNTL3_OTDT_25,
			'200':_b.KX132_CNTL3_OTDT_200,
			'12P5':_b.KX132_CNTL3_OTDT_12P5,
			'1600':_b.KX132_CNTL3_OTDT_1600,
			'50':_b.KX132_CNTL3_OTDT_50,
			'400':_b.KX132_CNTL3_OTDT_400,
			'100':_b.KX132_CNTL3_OTDT_100,
			'800':_b.KX132_CNTL3_OTDT_800,
		}
		self.KX132_CNTL5_ADPE={
			'DISABLED':_b.KX132_CNTL5_ADPE_DISABLED,
			'ENABLED':_b.KX132_CNTL5_ADPE_ENABLED,
		}
class masks(register_base):
	def __init__(self):
		self.KX132_COTR_DCSTR_MASK                                = 0xFF         # Command Test Responses
		self.KX132_WHO_AM_I_WAI_MASK                              = 0xFF         
		self.KX132_INS1_TP_MASK                                   = 0x3F         # Tilt Position mask
		self.KX132_INS2_TDTS_MASK                                 = 0x0C         # Tap/Double-Tap Status bit. This bit is cleared when the interrupt latch release register (INT_REL) is read
		self.KX132_INS3_WU_MASK                                   = 0x3F         # Wakeup directions mask
		self.KX132_CNTL1_GSEL_MASK                                = 0x18         # G-range Select (GSEL) bits select the acceleration range of the accelerometer outputs. This range is also called a full-scale range of the accelerometer.
		self.KX132_CNTL2_TP_MASK                                  = 0x3F         # Tilt Position mask
		self.KX132_CNTL3_OTP_MASK                                 = 0xC0         # Tilt Position (OTP) sets the output data rate for the Tilt Position function
		self.KX132_CNTL3_OTDT_MASK                                = 0x38         # Tap/Double-TapTM (OTDT) sets the output data rate for the Directional-Tap function
		self.KX132_CNTL3_OWUF_MASK                                = 0x07         # Wake-Up Function (OWUF) sets the output data rate
		self.KX132_CNTL4_C_MODE_MASK                              = 0x80         # defines debounce counter clear mode
		self.KX132_CNTL4_TH_MODE_MASK                             = 0x40         # defines wake / back-to-sleep threshold mode. TH_MODE = 0  absolute threshold, TH_MODE = 1  relative threshold
		self.KX132_CNTL4_WUFE_MASK                                = 0x20         # Wake-Up Function Engine enable bit
		self.KX132_CNTL4_BTSE_MASK                                = 0x10         # Back-to-Sleep Engine enable bit.
		self.KX132_CNTL4_PR_MODE_MASK                             = 0x08         # defines Pulse Reject mode
		self.KX132_CNTL4_OBTS_MASK                                = 0x07         # sets the output data rate at which the back-to-sleep (motion detection) performs its function during wake state
		self.KX132_CNTL5_ADPE_MASK                                = 0x10         # Advanced Data Path (ADP) enable. ADPE = 0  Advanced Data Path is disabled.  ADPE = 1  Advanced Data Path is enabled. Outputs are available in XADP, YADP, ZADP registers.
		self.KX132_CNTL5_TSE_MASK                                 = 0x04         # enables the Temperature Sensor output TOUT. TSE = 0  temperature sensor output disabled, TSE = 1  temperature sensor output enabled
		self.KX132_CNTL6_I2C_ALE_MASK                             = 0x80         # enables the I2C auto release function. I2C_ALE = 0  disabled, I2C_ALE = 1  enabled
		self.KX132_CNTL6_I2C_ALC_MASK                             = 0x03         # I2C auto release function counter select
		self.KX132_ODCNTL_IIR_BYPASS_MASK                         = 0x80         # IIR Filter Bypass mode enable bit
		self.KX132_ODCNTL_LPRO_MASK                               = 0x40         # Low-Pass filter roll off control. LPRO = 0  filter corner frequency set to ODR/9, LPRO = 1  filter corner frequency set to ODR/2
		self.KX132_ODCNTL_FSTUP_MASK                              = 0x20         # Fast Start Up Enable bit.
		self.KX132_ODCNTL_OSA_MASK                                = 0x0F         # Acceleration Output data rate.
		self.KX132_INC1_PW1_MASK                                  = 0xC0         # Pulse interrupt 1 width configuration
		self.KX132_INC2_AOI_MASK                                  = 0x40         # And-Or configuration. 0=Or combination of selected directions, 1=And combination of selected axes
		self.KX132_INC2_WUE_MASK                                  = 0x3F         # Directions of detected motion mask
		self.KX132_INC3_TM_MASK                                   = 0x3F         # Directions of tap detection mask
		self.KX132_INC5_PW2_MASK                                  = 0xC0         # Pulse interrupt 2 width configuration
		self.KX132_FFCNTL_FFDC_MASK                               = 0x30         # Free fall interrupt delayed clear duration for unlatched mode
		self.KX132_FFCNTL_OFFI_MASK                               = 0x07         # Free fall function output data rate
		self.KX132_LP_CNTL1_AVC_MASK                              = 0x70         # Averaging Filter Control
		self.KX132_WUFTH_WUFTH_L_MASK                             = 0xFF         # lsb part of WUF threshold
		self.KX132_BTSWUFTH_BTSTH_H_MASK                          = 0x70         # msb part of BTS threshold
		self.KX132_BTSWUFTH_WUFTH_H_MASK                          = 0x07         # msb part of WUF threshold
		self.KX132_BTSTH_BTSTH_L_MASK                             = 0xFF         # lsb part of BTS threshold
		self.KX132_BTSC_BTSC_MASK                                 = 0xFF         # Debounce counter register for the Back-to-Sleep (BTS) engine.
		self.KX132_WUFC_WUFC_MASK                                 = 0xFF         # Debounce counter register for the Wake-up Function (WUF) engine.
		self.KX132_PED_STPWM_L_PED_STPWM_MASK                     = 0xFFFF       # lsb part of pedometer watermark
		self.KX132_PED_STPWM_H_PED_STPWM_H_MASK                   = 0xFF         # msb part of pedometer watermark
		self.KX132_PED_CNTL1_STP_TH_MASK                          = 0x70         # It is used to allow a successful start for step detection
		self.KX132_PED_CNTL1_MAG_SCALE_MASK                       = 0x0F         # Scaling factor for the input signal
		self.KX132_PED_CNTL2_HPS_MASK                             = 0x70         # A Scaling factor for the output from the high-pass filter.
		self.KX132_PED_CNTL2_PED_ODR_MASK                         = 0x0F         # Pedometer Engine ODR Select. 1100 = 100Hz, 0110 =  50Hz
		self.KX132_PED_CNTL3_FCB_MASK                             = 0x38         # Scaling factor internal high-pass filter
		self.KX132_PED_CNTL3_FCA_MASK                             = 0x07         # Scaling factor internal high-pass filter
		self.KX132_PED_CNTL4_B_CNT_MASK                           = 0x70         # Samples below the zero threshold before setting
		self.KX132_PED_CNTL4_A_H_MASK                             = 0x0F         # Maximum area of the peak (maximum impact from the floor).
		self.KX132_SELF_TEST_MEMS_TEST_MASK                       = 0xFF         # When 0xCA is written to this register, the MEMS self-test function is enabled. Electrostatic-actuation of the accelerometer, results in a DC shift of the X, Y and Z axis outputs
		self.KX132_BUF_CNTL1_SMP_TH_MASK                          = 0xFF         # sample threshold level
		self.KX132_BUF_CNTL2_BM_MASK                              = 0x03         # selects the operating mode of the sample buffer
		self.KX132_BUF_STATUS_1_SMP_LEV_MASK                      = 0x3FF        # buffer level lsb bits (7-0)
		self.KX132_BUF_STATUS_2_SMP_LEV_H_MASK                    = 0x03         # buffer level msb bits (9-8)
		self.KX132_ADP_CNTL1_RMS_AVC_MASK                         = 0x70         # Number of samples used to calculate RMS output. Each sample is determined by the Advanced Data Path ODR as set by OADP<3:0> bits.
		self.KX132_ADP_CNTL1_OADP_MASK                            = 0x0F         # Output Data Rate (ODR) for Advanced Data Path.
		self.KX132_ADP_CNTL3_ADP_F1_1A_MASK                       = 0x7F         # ADP filter-1 coefficient (1/A)
		self.KX132_ADP_CNTL4_ADP_F1_BA_MASK                       = 0x7FFFFF     # Advanced Data Path (ADP) Control registers 4, 5 and 6.
		self.KX132_ADP_CNTL7_ADP_F1_CA_MASK                       = 0x7FFFFF     # Advanced Data Path (ADP) Control registers 7, 8 and 9.
		self.KX132_ADP_CNTL10_ADP_F1_ISH_MASK                     = 0x1F         # ADP filter-1 input scale shift value
		self.KX132_ADP_CNTL11_ADP_F2_1A_MASK                      = 0x7F         # ADP filter-2 coefficient (1/A)
		self.KX132_ADP_CNTL12_ADP_F2_BA_MASK                      = 0xFFFF       # ADP filter-2 coefficient (B/A)
		self.KX132_ADP_CNTL18_ADP_F2_ISH_MASK                     = 0x1F         # ADP filter-2 input scale shift value
		self.KX132_ADP_CNTL19_ADP_F2_OSH_MASK                     = 0x1F         # ADP filter-2 output scale shift value