<a id="SDGpy"></a>

# SDGpy

<a id="SDGpy.PySDG"></a>

## PySDG Objects

```python
class PySDG()
```

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

<a id="SDGpy.PySDG.__init__"></a>

#### \_\_init\_\_

```python
def __init__(IP: str)
```

PySDG [init] :  Initialize the class.
                Use some configuration file to initialize properly the oscilloscope, and read it's actual state to make sure to fetch the real state
                May take some time since a lot of network requests are done here !

    Arguments :
        IP : A string IP address, version 4 of where the ressource shall be allocated

    Returns :
        None

<a id="SDGpy.PySDG.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

PySDG [repr] :  Basic print of the connected device.
                Aimed to the developper, and thus expose more informations than the __str__ function !

    Arguments :
        None

    Returns :
        None

<a id="SDGpy.PySDG.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

PySDG [repr] :  Basic print of the connected device.
                Aimed to the user, and thus expose less informations than the __repr__ function !

    Arguments :
        None

    Returns :
        None

<a id="SDGpy.PySDG.GetAllStatus"></a>

#### GetAllStatus

```python
def GetAllStatus()
```

PySDG [GetAllStatus] :  Return the status of the STB, ESR, INR, DDR, CMD, EXR and URR Registers.

    Arguments :
        None

    Returns :
        List of integers with the values in order

<a id="SDGpy.PySDG.EnableBuzzer"></a>

#### EnableBuzzer

```python
def EnableBuzzer()
```

PySDG [EnableBuzzer] :  Enable the device buzzer

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="SDGpy.PySDG.DisableBuzzer"></a>

#### DisableBuzzer

```python
def DisableBuzzer()
```

PySDG [DisableBuzzer] : Disable the device buzzer

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="SDGpy.PySDG.GetBuzzerEnablingState"></a>

#### GetBuzzerEnablingState

```python
def GetBuzzerEnablingState()
```

PySDG [GetBuzzerEnablingState] :    Return the buzzer enabling state (ON or OFF)

Arguments :
    None

Returns :
    True | False

<a id="SDGpy.PySDG.RecallPreset"></a>

#### RecallPreset

```python
def RecallPreset(PresetNumber: int)
```

PySDG [RecallPreset] :  Apply a previously stored list of settings on the device.
                        Can only be called after the call of SavePreset function !
                        If 0 is passed, this is the default config.

    Argument :
        PresentNumber : Integer of the position to store the preset

    Returns :
        self.GetAllErrors() returns (List of errors)
        or
        -1 : Invalid preset ID

<a id="SDGpy.PySDG.SavePresent"></a>

#### SavePresent

```python
def SavePresent(PresetNumber: int)
```

PySDG [SavePresent] :   Store the settings of the device into a defined non volatile memory location.
                        Number 0 is not valid, since this location is the default preset.

    Argument :
        PresentNumber : Integer of the position to store the preset

    Returns :
        self.GetAllErrors() returns (List of errors)
        or
        -1 : Invalid preset ID

<a id="SDGpy.PySDG.ResetDevice"></a>

#### ResetDevice

```python
def ResetDevice()
```

PySDG [ResetDevice] : Perform a software reset of the device

Arguments :
    None

Returns :
    self.GetAllErrors() returns (List of errors)

<a id="SDGpy.PySDG.GetAllErrors"></a>

#### GetAllErrors

```python
def GetAllErrors(print=False)
```

PySDG [GetAllErrors] :  Read the device errors, and until at least one error exist, continue to read it.
                        For each errors, it will be printed in console and returned on a list, with it's lengh in first position.

                        This function also trigger a reading of the status of the device to detect if value where adapted or cancelled.

    Arguments :
        print : Shall we print the decoded output on the console ? Default to false.

    Returns :
        List :
            Index 0 :       Number of errors that occured
            Index 1 - n :   Device errors codes

<a id="SDGpy.PySDG.GetDeviceStatus"></a>

#### GetDeviceStatus

```python
def GetDeviceStatus(print=False)
```

PySDG [GetDeviceStatus] :   Get the device status, and parse it to make it easier to use for developpers or users.
                            Print each status bit

    Argument :
        print : Shall we print the decoded output on the console ? Default to false.

    Returns :
        List of lenght 16, for each bit

<a id="SDGpy.PySDG.GetDeviceOptions"></a>

#### GetDeviceOptions

```python
def GetDeviceOptions()
```

PySDG [GetDeviceOptions] :  Return the list of the installed device options.
                            Function isn't working for now, but the response seems correct.
                            --> Return 0 where it shall return OPC 0...

    Arguments :
        None

    Returns :
        List of String for all options

<a id="SDGpy.PySDG.GetDeviceStatus"></a>

#### GetDeviceStatus

```python
def GetDeviceStatus()
```

PySDG [GetDeviceStatus] :   Read the device status, and parse it to be easier for the user to read !

    Arguments :
        None

    Returns :
        List of lenght 16, for each bit

