# Soundboard

Soundboard is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Soundboard.
For windows:

```batch
py -m pip install -i https://test.pypi.org/simple/ Soundboard

```
For Mac/Linux:
```bash
pip install -i https://test.pypi.org/simple/ Soundboard
```


## Usage

```python
from Soundboard import *

arr1 =[440 ,450 ,440 ,450 ,440 ,440 ] #Note
arr2 =[1   ,1   ,1   ,1   ,1   ,1   ] #Duration
arr3 =[100 ,10  ,90  ,85  ,80  ,75  ] #Amplitude
arr = []
for i in range(len(arr1)):
    arr.append([arr1[i],arr2[i]*0.4,arr3[i]])
Soundboard.build(arr)
Soundboard.compile("Octaves.wav")
```
### Check our [Github](https://github.com/ghostlypi/Soundboard) for more information and tests!

## License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
