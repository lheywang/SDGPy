# ============================================================================================================
# Generics.py
# lheywang on 21/12/2024
#
# Base file for the generics SCPI class.
# This class could easily be reused with any IEEE 488.1 compliant device.
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase


class SCPIGenerics(SiglentBase):
    def ClearStatus(self):
        """
        PySDG [ClearStatus] :   Clear the status register

            Arguments :
                None

            Returns :
                None
        """

        self.__instr__.write("*CLS")
        return

    def ReadCMR(self):
        """
        PySDG [ReadCMR] :   Read and clear the CMR register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("CMR?")
        return int(Ret.strip().split(" ")[-1])

    def ReadDDR(self):
        """
        PySDG [ReadDDR] :   Read and clear the DDR register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("DDR?")
        return int(Ret.strip().split(" ")[-1])

    def ReadESE(self):
        """
        PySDG [ReadESE] :   Read and clear the ESE register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("*ESE?")
        return int(Ret.strip())

    def ReadESR(self):
        """
        PySDG [ReadESR] :   Read and clear the ESE register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("*ESR?")
        return int(Ret.strip())

    def ReadEXR(self):
        """
        PySDG [ReadEXR] :   Read and clear the EXR register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("EXR?")
        return int(Ret.strip().split(" ")[-1])

    def ReadIDN(self):
        """
        PySDG [ReadIDN] :   Read back the device name

            Arguments :
                None

            Returns :
                String : The output of the command
        """

        return self.__instr__.query("*IDN?").strip()

    def ReadINR(self):
        """
        PySDG [ReadINR] :   Read and clear the device status

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("INR?").strip().split(" ")[-1])

    def ReadOPC(self):
        """
        PySDG [ReadOPC] :   Read the Operation Complete status bit.
                            Actually, this function always return 1, because the device respond when the operation is complete...

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("*OPC?").strip())

    def ReadOPT(self):
        """
        PySDG [ReadOPT] :   Read the installed options on the device

            Arguments :
                None

            Returns :
                String : The output of the command
        """

        return self.__instr__.query("*OPT?").strip()

    def ReadSRE(self):
        """
        PySDG [ReadSRE] :   Read the service request enable register value

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("*SRE?").strip())

    def ReadSTB(self):
        """
        PySDG [ReadSTB] :   Read the status register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("*STB?").strip())

    def SetESE(self, value: int):
        """
        PySDG [SetESE] :   Write the ESE Register

            Arguments :
                Integer : Value to be written

            Returns :
                self.GetAllErrors() returns (List of errors)
        """

        if value > 255 or value < 0:
            return -1

        self.__instr__.write(f"*ESE {value}")
        return self.__baseclass__.GetAllErrors()

    def SetESR(self, value: int):
        """
        PySDG [SetESR] :   Write the ESR Register

            Arguments :
                Integer : Value to be written

            Returns :
                self.GetAllErrors() returns (List of errors)
        """

        if value > 128 or value < 0:
            return -1

        self.__instr__.write(f"*ESR {value}")
        return self.__baseclass__.GetAllErrors()

    def SetOPC(self):
        """
        PySDG [SetOPC] :   Write the OPC (Operation Complete) Status bit

            Arguments :
                None

            Returns :
                self.GetAllErrors() returns (List of errors)
        """
        self.__instr__.write("*OPC")
        return self.__baseclass__.GetAllErrors()

    def SetSRE(self, value: int):
        """
        PySDG [SetSRE] :   Write the ESR Register (Service Request Enable Register)

            Arguments :
                Integer : Value to be written

            Returns :
                self.GetAllErrors() returns (List of errors)
        """

        if value > 256 or value < 0:
            return -1

        self.__instr__.write(f"*SRE {value}")
        return self.__baseclass__.GetAllErrors()
