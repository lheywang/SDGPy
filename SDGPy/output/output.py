# ============================================================================================================
# output.py
# lheywang on 04/01/2024
#
# Base file for the output class
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase


class SiglentOutput(SiglentBase):
    """
    SDGpy [SiglentOutput] : Class herited from SiglentBase, designed to handle all the IOs related to output control.

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :

            Public (XX) :
    """

    def __init__(self, instr, baseclass, channel):
        """
        Overhide the standard class init to store some more advanced data !

        Check SiglentBase doc before !

        Added attributes :
            Private (2) :
                __channel__ :   Descriptor of the channel

            Public (0) :
                None

        Added methods :
            Private (0) :
                None

            Public (0) :
                None
        """
        super().__init__(instr, baseclass)
        self.__channel__ = channel

    def EnableOutput(self):
        """
        SDGpy [Output][EnableOutput] : Enable the channel output

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.write(f"{self.__channel__}:OUTP ON")
        return self.__baseclass__.GetAllErrors()

    def DisableOutput(self):
        """
        SDGpy [Output][DisableOutput] : Disable the channel output

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.write(f"{self.__channel__}:OUTP OFF")
        return self.__baseclass__.GetAllErrors()

    def SetLoad50(self):
        """
        SDGpy [Output][SetLoad50] : Configure the load to 50 Ohms

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:OUTP LOAD,50")
        return self.__baseclass__.GetAllErrors()

    def SetLoad1M(self):
        """
        SDGpy [Output][SetLoad50] : Configure the load to 1M (High-Z)

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:OUTP LOAD,HZ")
        return self.__baseclass__.GetAllErrors()

    def EnableOutputInvert(self):
        """
        SDGpy [Output][SetLoad50] : Invert the output(* -1)

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:OUTP PLRT,INVT")
        return self.__baseclass__.GetAllErrors()

    def DisableOutputInvert(self):
        """
        SDGpy [Output][SetLoad50] : De-invert the output (*1)

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:OUTP PLRT,NOR")
        return self.__baseclass__.GetAllErrors()

    def SetOutputWaveform(self, OutputSignal: str):
        """
        SDGpy [Output][SetOutputWaveform] : Configure the output waveform

            Arguments :
                OutputSignal : SINE | SQUARE | RAMP | PULSE | NOISE | ARB | DC | PRBS | IQ

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid waveform
        """
        if OutputSignal not in [
            "SINE",
            "SQUARE",
            "RAMP",
            "PULSE",
            "NOISE",
            "ARB",
            "DC",
            "PRBS",
            "IQ",
        ]:
            return [1, -1]

        self.__instr__.write(f"{self.__channel__}:BSWV WVPT,{OutputSignal}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputFrequency(self, Frequency: float):
        """
        SDGpy [Output][SetOutputFrequency] : Configure the output frequency in Hz

            Arguments :
                Frequency : Float value (limited to 3 digits)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV FRQ,{Frequency:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputAmplitude(self, Amplitude: float):
        """
        SDGpy [Output][SetOutputAmplitude] : Configure the output amplitude in volts (Vpp)

            Arguments :
                Amplitude : Float value (limited to 3 digits)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV AMP,{Amplitude:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputOffset(self, Offset: float):
        """
        SDGpy [Output][SetOutputOffset] : Configure the output offset

            Arguments :
                Offset : Float value (limited to 3 digits)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV OFST,{Offset:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputCommonOffset(self, Offset: float):
        """
        SDGpy [Output][SetOutputCommonOffset] : Configure the common output offset (only in differential mode)

            Arguments :
                Offset : Float value (limited to 3 digits)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV COM_OFST,{Offset:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetRampSymmetry(self, Symmetry: int):
        """
        SDGpy [Output][SetRampSymetry] : Configure the symetry factor of a ramp

            Arguments :
                Symmetry : Integer value (in %)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Symmetry < 0 or Symmetry > 100:
            return [1, -1]

        self.__instr__.write(f"{self.__channel__}:BSWV SYM,{Symmetry}")
        return self.__baseclass__.GetAllErrors()

    def SetDutyCycle(self, Duty: int):
        """
        SDGpy [Output][SetDutyCycle] : Configure the duty cycle fo square wave

            Arguments :
                Duty : Integer value (in %)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Duty < 0 or Duty > 100:
            return [1, -1]

        self.__instr__.write(f"{self.__channel__}:BSWV DUTY,{Duty}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputPhase(self, Phase: int):
        """
        SDGpy [Output][SetOutputPhase] : Configure the phase of the output

            Arguments :
                Phase : Integer value (in °)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Phase < 0 or Phase > 360:
            return [1, -1]

        self.__instr__.write(f"{self.__channel__}:BSWV PHSE,{Phase}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputNoiseSTDEV(self, Noise: float):
        """
        SDGpy [Output][SetOutputNoiseSTDEV] : Configure the STDEV of the noise output

            Arguments :
                Noise : float value (in V)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV STDEV,{Noise:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputNoiseMEAN(self, Mean: float):
        """
        SDGpy [Output][SetOutputNoiseMEAN] : Configure the MEAN of the noise output

            Arguments :
                Mean : float value (in V)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV MEAN,{Mean:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputPulseWIDTH(self, Width: float):
        """
        SDGpy [Output][SetOutputPulseWIDTH] : Configure the pulse width of an output

            Arguments :
                Width : float value (in s)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV WIDTH,{Width:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputPulseRISE(self, Rise: float):
        """
        SDGpy [Output][SetOutputPulseWIDTH] : Configure the pulse rise time of an output

            Arguments :
                Rise : float value (in s)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV RISE,{Rise:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputPulseFALL(self, Fall: float):
        """
        SDGpy [Output][SetOutputPulseFALL] : Configure the pulse fall time of an output

            Arguments :
                Fall : float value (in s)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV FALL,{Fall:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetOutputDelay(self, Delay: float):
        """
        SDGpy [Output][SetOutputDelay] : Configure the delay of an output

            Arguments :
                Delay : float value (in s)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:BSWV DLY,{Delay:.6f}")
        return self.__baseclass__.GetAllErrors()

    def SetArbWave(self, ID: int):
        """
                SDGpy [Output][SetArbWave] : Configure the arbitrary wave by ID (only built-in ones). Use name for custom ones.

                    Arguments :
                        ID : integer value

                    Returns :
                        self.GetAllErrors()

                    Available Waveforms :
                        0 Sine
                        1 Noise
                        2 StairUp
                        3 StairDn
                        4 Stairud
                        5 Ppulse
                        6 Npulse
                        7 Trapezia
                        8 Upramp
                        9 Dnramp
                        10 ExpFal
                        11 ExpRise
                        12 Logfall
                        13 Logrise
                        14 Sqrt
                        15 Root3
                        16 X^2
                        17 X^3
                        18 Sinc
                        19 Gaussian
                        20 Dlorentz
                        21 Haversine
                        22 Lorentz
                        23 Gauspuls
                        24 Gmonopuls
                        25 Tripuls
                        26 Cardiac
                        27 Quake
                        28 Chirp
                        29 Twotone
                        30 SNR
                        31 Hamming
                        32 Hanning
                        33 Kaiser
                        34 Blackman
                        35 Gausswin
                        36 Triang
                        37 BlackmanH
                        38 Bartlett
                        39 Tan
                        40 Cot
                        41 Sec
                        42 Csc
                        43 Asin
                        44 Acos
                        45 Atan
                        46 Acot
                        47 Square
                        48 SineTra
                        49 SineVer
                        50 AmpALT
                        51 AttALT
                        52 RoundHalf
                        53 RoundsPM
                        54 BlaseiWave
                        55 DampedOsc
                        56 SwingOsc
                        57 Discharge
                        58 Pahcur
                        59 Combin
                        60 SCR
                        61 Butterworth
                        62 Chebyshev1
                        63 Chebyshev2
                        64 TV
                        65 Voice
                        66 Surge
                        67 NA
                        68 Ripple
                        69 Gamma
                        70 StepResp
                        71 BandLimited
                        72 CPulse
                        73 CWPulse
                        74 GateVibr
                        75 LFMPulse
                        76 MCNoise
                        77 AM
                        78 FM
                        79 PFM
                        80 PM
                        81 PWM
                        82 EOG
                        83 EEG
                        84 EMG
                        85 Pulseilogram
                        86 ResSpeed
                        87 ECG1
                        88 ECG2
                        89 ECG3
                        90 ECG4
                        91 ECG5
                        92 ECG6
                        93 ECG7
                        94 ECG8
                        95 ECG9
                        96 ECG10
                        97 ECG11
                        98 ECG12
                        99 ECG13
                        100 ECG14
                        101 ECG15
                        102 LFPulse
                        103 Tens1
                        104 Tens2
                        105 Tens3
                        106 Airy
                        107 Besselj
                        108 Bessely
                        109 Dirichlet
                        110 Erf
                        111 Erfc
                        112 ErfcInv
                        113 ErfInv
                        114 Laguerre
                        115 Legend
                        116 Versiera
                        117 Weibull
                        118 LogNormal
                        119 Laplace
                        120 Maxwell
                        121 Rayleigh
                        122 Cauchy
                        123 CosH
                        124 CosInt
                        125 CotH
                        126 CscH
                        127 SecH
                        128 SinH
                        129 SinInt
                        130 TanH
                        131 ACosH
                        132 ASecH
                        133 ASinH
                        134 ATanH
                        135 ACsch
                        136 ACoth
                        137 Bartlett
                        138 BohmanWin
                        139 ChebWin
                        140 FlattopWin
                        141 ParzenWin
                        142 TaylorWin
                        143 TukeyWin
                        144 Duty01
                        145 Duty02
                        146 Duty04
                        --- --- (+2)
                        192 Duty96
                        193 Duty98
                        194 Duty99
                        195 demo1_375
                        196 demo1_16k
                        197 demo2_3k
                        198 demo2_16k
        """
        self.__instr__.write(f"{self.__channel__}:ARWV INDEX,{ID}")
        return self.__baseclass__.GetAllErrors()
