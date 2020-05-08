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
import Soundboard

arr1 =[440 ,450 ,440 ,450 ,440 ,440 ] #Note
arr2 =[1   ,1   ,1   ,1   ,1   ,1   ] #Duration
arr3 =[100 ,10  ,90  ,85  ,80  ,75  ] #Amplitude
Soundboard.render(arr1,arr2,arr3,"test.wav")
```
### Check our [Github](https://github.com/ghostlypi/Soundboard)

## Documentation

### Render
```python
Soundboard.render(frequency,duration,amplitude,filename)
```
takes in an array of frequencies, and array of durations, and an array of amplitudes and a string filename
#### Note: The arrays must be of equal length or else the program will halt with a notice.
#### Note: The filename string must include a .wav to be playable

### Build
```python
Soundboard.build(arr)
```
takes in an 2 dimensional array - an sequence of note arrays containing 3 values, frequency, duration, and amplitude
```python
Soundboard.build([[frequency,duration,amplitude], ...])
```
#### Note: The build will fail with an error if all 3 values are not filled in for each and every note.
#### Note: Build will return a file called “Build.txt” containing numerical values for speaker positions

### Compile
```python
Soundboard.compile(filename)
```
takes in a filename
#### Note: The filename string must include a .wav to be playable
#### Note: Compile will fail if there is no “Build.txt” in the current directory.

## Author: [Ghostlypi](parthiyer.com)

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


