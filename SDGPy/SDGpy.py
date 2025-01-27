# ============================================================================================================
# PySDG.py
# lheywang on 17/12/2024
#
# Base file for the whole package class
#
# ============================================================================================================

# Python libraries
import ipaddress
import tomllib
from datetime import datetime
from warnings import warn

# Poetry managed lbraries
import pyvisa  # type: ignore

# Others files
from .communication import SiglentCommunication
from .generics import SCPIGenerics
from .counter import SiglentCounter
from .modulation import SiglentModulation
from .output import SiglentOutput

class PySDG:
    """
    PySDG [class] : Parent class of the PySDG package.
                    Handle actually all of basic SCPI commands, and call subclasses for some advanced functionnalities !

        Attributes :
            Private :
                __ip__ :            ip of the device. Used internally to check it's validity.
                __rm__ :            pyvisa ressource manager
                __instr__ :         Handle to the pyvisa object to interract with the device
                __ConfigFile__ :    Configuration file used for the scope.
                __Config__ :        Parsed configuration toml file
                __Generics__ :      SCPIGenerics class. Used for low level interraction with the device.

            Public :
                ** Standard variables **
                DeviceOpenned :     Get a non 0 value if the device was openned correctly. Otherwise, take 0
                model :             Device model, parsed from *IDN command
                SN :                Device SN, parsed from *IDN command
                Firmware :          Device firmware revision, parsed from *IDN command

        Methods :
            Private :

            Public :

        Parents :
            None

        Subclass :
            None

    """

    def __init__(self, IP: str):
        """
        PySDG [init] :  Initialize the class.
                        Use some configuration file to initialize properly the oscilloscope, and read it's actual state to make sure to fetch the real state
                        May take some time since a lot of network requests are done here !

            Arguments :
                IP : A string IP address, version 4 of where the ressource shall be allocated

            Returns :
                None
        """

        # First, validate the IP and try to open the ressource !
        try:
            self.__ip__ = ipaddress.ip_address(IP)
        except ValueError:
            print(
                "     [ PySDG ] [ Init ] : Incorrect IP was passed to the constructor"
            )
            self.DeviceOpenned = 0
            return

        try:
            self.__rm__ = pyvisa.ResourceManager()
            self.__instr__ = self.__rm__.open_resource(f"TCPIP0::{IP}::inst0::INSTR")
        except:
            print(
                "     [ PySDG ] [ Init ] : Unable to access to the device. Check if the IP is right, or if you can ping it !"
            )
            self.DeviceOpenned = 0
            return

        # Then, request for the IDN command.
        # Typical return : Siglent Technologies,SDS824X HD,SDS08A0C802019,3.8.12.1.1.3.8
        IDN = self.__instr__.query("*IDN?")
        IDN = IDN.split(",")

        # Check if the brand is the right one, or this library isn't going to work !
        if IDN[0].find("Siglent") == -1:
            print("     [ PySDG ] [ Init ] : Found a non Siglent Device on this IP !")
            self.DeviceOpenned = 0
            return

        # Parse some different fields
        self.model = IDN[1]
        self.SN = IDN[2]
        self.Firmware = IDN[3]

        # Load the right configuration file
        # First, replace any space in the name with a "-" to ensure compatibility within different OS
        self.model = self.model.replace(" ", "-")

        # Load the right configuration file without the SDS in front
        self.__ConfigFile__ = self.model[3:] + ".toml"

        self.__Config__ = None
        with open(f"config/{self.__ConfigFile__}", "rb") as f:
            self.__Config__ = tomllib.load(f)

        # Create a generic class, for internal usage only
        self.__Generics__ = SCPIGenerics(self.__instr__, self)

        # Now, initialize some parameters from the configuration file
        self.Channel = []
        for index in range(self.__Config__["Specs"]["Channel"]):
            pass
        # Then, initialize all of the subclass
        # Warning : Some fetures may not be available globally, but due to minor variations they're here for all.


        self.DeviceOpenned = 1
        return

    def __repr__(self):
        """
        PySDG [repr] :  Basic print of the connected device.
                        Aimed to the developper, and thus expose more informations than the __str__ function !

            Arguments :
                None

            Returns :
                None
        """

        print(f"Device on {self.__ip__} : \nType : {self.model} ")
        return

    def __str__(self):
        """
        PySDG [repr] :  Basic print of the connected device.
                        Aimed to the user, and thus expose less informations than the __repr__ function !

            Arguments :
                None

            Returns :
                None
        """

        print(f"Device on {self.__ip__} : \nType : {self.model} ")
        return

    #
    #   STATUS
    #

    def GetAllStatus(self):
        """
        PySDG [GetAllStatus] :  Return the status of the STB, ESR, INR, DDR, CMD, EXR and URR Registers.

            Arguments :
                None

            Returns :
                List of integers with the values in order
        """

        # Querry
        Ret = self.__instr__.query("ALST?")

        # Split comma. Format : ALST STB, Val, ESR..
        # Get only the usefull values
        Ret = Ret.strip().split(",")
        return [
            int(Ret[1]),
            int(Ret[3]),
            int(Ret[5]),
            int(Ret[7]),
            int(Ret[9]),
            int(Ret[11]),
            int(Ret[13]),
        ]

    #
    #   BUZZER
    #

    def EnableBuzzer(self):
        """
        PySDG [EnableBuzzer] :  Enable the device buzzer

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("BUZZ ON")
        return self.GetAllErrors()

    def DisableBuzzer(self):
        """
        PySDG [DisableBuzzer] : Disable the device buzzer

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("BUZZ OFF")
        return self.GetAllErrors()

    def GetBuzzerEnablingState(self):
        """
        PySDG [GetBuzzerEnablingState] :    Return the buzzer enabling state (ON or OFF)

        Arguments :
            None

        Returns :
            True | False
        """
        Ret = self.__instr__.query("BUZZ?").strip().split(" ")[-1]
        if Ret == "ON":
            return True
        return False

    #
    #   STANDARD SCPI COMMANDS
    #

    # =============================================================================================================================================
    """
    Up to this point, all functions shall be working on any device, even other than Siglent ones since they're part
    of the IEEE 488.1 specification.

    In any way, the class can't be constructed without a compatible device, that's why I didn't create a global SCPI engine...
    """
    # =============================================================================================================================================

    def RecallPreset(self, PresetNumber: int):
        """
        PySDG [RecallPreset] :  Apply a previously stored list of settings on the device.
                                Can only be called after the call of SavePreset function !
                                If 0 is passed, this is the default config.

            Argument :
                PresentNumber : Integer of the position to store the preset

            Returns :
                self.GetAllErrors() returns (List of errors)
                or
                -1 : Invalid preset ID
        """
        if PresetNumber > 20 or PresetNumber < 0:
            return [1, -1]

        self.__instr__.write(f"*RCL {PresetNumber}")
        return self.GetAllErrors()

    def SavePresent(self, PresetNumber: int):
        """
        PySDG [SavePresent] :   Store the settings of the device into a defined non volatile memory location.
                                Number 0 is not valid, since this location is the default preset.

            Argument :
                PresentNumber : Integer of the position to store the preset

            Returns :
                self.GetAllErrors() returns (List of errors)
                or
                -1 : Invalid preset ID
        """
        if PresetNumber > 20 or PresetNumber < 1:
            return [1, -1]

        self.__instr__.write(f"*SAV {PresetNumber}")
        return self.GetAllErrors()

    def ResetDevice(self):
        """
        PySDG [ResetDevice] : Perform a software reset of the device

        Arguments :
            None

        Returns :
            self.GetAllErrors() returns (List of errors)
        """

        self.__instr__.write("*RST")
        return self.GetAllErrors()

    # =============================================================================================================================================
    """
    Now, let's define some more advanced functions that will call some previously defined ones.

    It's more aimed at the user, even if the previous ones remains accessibles, since theses functions will provide more content.
    
    """
    # =============================================================================================================================================

    def GetAllErrors(self, toprint=False):
        """
        PySDS [GetAllErrors] :  Read the device errors, and until at least one error exist, continue to read it.
                                For each errors, it will be printed in console and returned on a list, with it's lengh in first position.

                                This function also trigger a reading of the status of the device to detect if value where adapted or cancelled.

            Arguments :
                toprint : (unused) Shall we print the decoded output on the console ? Default to false.

            Returns :
                List :
                    Index 0 :       Number of errors that occured
                    Index 1 - n :   Device errors codes
        """
        stop = False
        codes = []
        errors = []

        while stop == False:
            ret = self.__instr__.query("SYST:ERR?").strip().split(",")
            if int(ret[0]) == 0:
                stop = True
                break
                
            else:
                codes.append(int(ret[0]))
                errors.append(ret[1][1:-1])

        if len(codes) != 0:
            for index, code in enumerate(codes):
                print(f"Error {index:10} : {code:10} : {errors[index]}")

        return [len(codes), codes]