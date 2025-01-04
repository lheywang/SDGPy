<a id="generics"></a>

# generics

<a id="generics.generics"></a>

# generics.generics

<a id="generics.generics.SCPIGenerics"></a>

## SCPIGenerics Objects

```python
class SCPIGenerics(SiglentBase)
```

<a id="generics.generics.SCPIGenerics.ClearStatus"></a>

#### ClearStatus

```python
def ClearStatus()
```

PySDG [ClearStatus] :   Clear the status register

    Arguments :
        None

    Returns :
        None

<a id="generics.generics.SCPIGenerics.ReadCMR"></a>

#### ReadCMR

```python
def ReadCMR()
```

PySDG [ReadCMR] :   Read and clear the CMR register

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadDDR"></a>

#### ReadDDR

```python
def ReadDDR()
```

PySDG [ReadDDR] :   Read and clear the DDR register

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadESE"></a>

#### ReadESE

```python
def ReadESE()
```

PySDG [ReadESE] :   Read and clear the ESE register

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadESR"></a>

#### ReadESR

```python
def ReadESR()
```

PySDG [ReadESR] :   Read and clear the ESE register

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadEXR"></a>

#### ReadEXR

```python
def ReadEXR()
```

PySDG [ReadEXR] :   Read and clear the EXR register

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadIDN"></a>

#### ReadIDN

```python
def ReadIDN()
```

PySDG [ReadIDN] :   Read back the device name

    Arguments :
        None

    Returns :
        String : The output of the command

<a id="generics.generics.SCPIGenerics.ReadINR"></a>

#### ReadINR

```python
def ReadINR()
```

PySDG [ReadINR] :   Read and clear the device status

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadOPC"></a>

#### ReadOPC

```python
def ReadOPC()
```

PySDG [ReadOPC] :   Read the Operation Complete status bit.
                    Actually, this function always return 1, because the device respond when the operation is complete...

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadOPT"></a>

#### ReadOPT

```python
def ReadOPT()
```

PySDG [ReadOPT] :   Read the installed options on the device

    Arguments :
        None

    Returns :
        String : The output of the command

<a id="generics.generics.SCPIGenerics.ReadSRE"></a>

#### ReadSRE

```python
def ReadSRE()
```

PySDG [ReadSRE] :   Read the service request enable register value

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.ReadSTB"></a>

#### ReadSTB

```python
def ReadSTB()
```

PySDG [ReadSTB] :   Read the status register

    Arguments :
        None

    Returns :
        Integer : Register value

<a id="generics.generics.SCPIGenerics.SetESE"></a>

#### SetESE

```python
def SetESE(value: int)
```

PySDG [SetESE] :   Write the ESE Register

    Arguments :
        Integer : Value to be written

    Returns :
        self.GetAllErrors() returns (List of errors)

<a id="generics.generics.SCPIGenerics.SetESR"></a>

#### SetESR

```python
def SetESR(value: int)
```

PySDG [SetESR] :   Write the ESR Register

    Arguments :
        Integer : Value to be written

    Returns :
        self.GetAllErrors() returns (List of errors)

<a id="generics.generics.SCPIGenerics.SetOPC"></a>

#### SetOPC

```python
def SetOPC()
```

PySDG [SetOPC] :   Write the OPC (Operation Complete) Status bit

    Arguments :
        None

    Returns :
        self.GetAllErrors() returns (List of errors)

<a id="generics.generics.SCPIGenerics.SetSRE"></a>

#### SetSRE

```python
def SetSRE(value: int)
```

PySDG [SetSRE] :   Write the ESR Register (Service Request Enable Register)

    Arguments :
        Integer : Value to be written

    Returns :
        self.GetAllErrors() returns (List of errors)

